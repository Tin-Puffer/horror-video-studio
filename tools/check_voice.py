#!/usr/bin/env python3
"""Listen back to the narration: transcribe every synthesized line and compare it with the script.

  python3 tools/check_voice.py scripts/<story>.json [--scenes 7-13] [--fix] [--tries 5]

Flags a line when the speech-to-text differs too much from the text (swallowed or slurred words), when a word
pair is heard more often than written (repeats), when a silence falls where the text has no punctuation
(wrong phrasing, "bố | tôi còn chưa ra đời"), when it runs far longer than its words need, or when its pitch sits
> MAX_PITCH_OFF semitones away from the narrator's median (separate takes can drift up or down). --fix deletes the cached take of each flagged line and asks
the engine for new takes (VieNeu samples, so every take differs), keeping the closest one.
Report: build/<story>_voice_check.md. Needs tools/asr_worker.py's model (downloaded on first use).
"""
from __future__ import annotations

import argparse
import math
import difflib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render  # noqa: E402

ROOT = render.ROOT
MODEL = "vinai/PhoWhisper-base"
MAX_ERR = 0.15       # word error rate (tones ignored) above this = flagged
MAX_SEC_WORD = 0.55  # seconds per word (after tempo) above this = flagged (dragging / babbling)
MAX_PITCH_OFF = 2.0  # semitones a take may sit above/below the narrator's median pitch (sounds like another voice)
REF_F0 = 0.0         # set in main(): median pitch of all takes
MIN_PAUSE = 0.45     # a silence this long inside a line must sit at punctuation (shorter ones are\n                     # squeezed to max_inner_pause by render.py and pass as a breath)


def words(text: str) -> list:
    """Lower-case words without tone marks: speech-to-text often mishears a tone (tre/trẻ),
    which is not what we look for (repeated, swallowed, slurred words)."""
    text = unicodedata.normalize("NFD", text.lower().replace("đ", "d"))
    return re.findall(r"[^\W_]+", "".join(c for c in text if unicodedata.category(c) != "Mn"))


def error_rate(ref: list, hyp: list) -> float:
    """Word edit distance / len(ref)."""
    d = list(range(len(hyp) + 1))
    for i, r in enumerate(ref, 1):
        prev, d[0] = d[0], i
        for j, h in enumerate(hyp, 1):
            prev, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, prev + (r != h))
    return d[-1] / max(1, len(ref))


def repeats(ref: list, hyp: list) -> str:
    """A word pair heard more often than the text has it ("tỉ mẩn khắc … thì mẩn khắc", "ông ông")."""
    def pairs(ws):
        out = {}
        for a, b in zip(ws, ws[1:]):
            out[(a, b)] = out.get((a, b), 0) + 1
        return out
    want = pairs(ref)
    extra = [" ".join(k) for k, n in pairs(hyp).items() if n > want.get(k, 0) and k in want]
    doubled = [hyp[i] for i in range(len(hyp) - 1) if hyp[i] == hyp[i + 1] and ref.count(hyp[i]) < 2]
    return ", ".join(extra + doubled)


def silences(path: Path, least: float) -> list:
    """(start, end) seconds of silences >= least inside the speech of a take."""
    import wave
    import numpy as np
    with wave.open(str(path)) as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    hop = int(sr * 0.02)
    n = len(x) // hop
    loud = np.sqrt((x[:n * hop].reshape(n, hop) ** 2).mean(axis=1)) > 10 ** (-38 / 20)
    on = np.flatnonzero(loud)
    if not len(on):
        return []
    out, start = [], None
    for k in range(on[0], on[-1] + 1):
        if not loud[k] and start is None:
            start = k
        elif loud[k] and start is not None:
            if (k - start) * 0.02 >= least:
                out.append((start * 0.02, k * 0.02))
            start = None
    return out


def bad_pauses(text: str, heard: dict, path: Path) -> list:
    """Silences inside the take that do not fall where the text has punctuation: "bố | tôi còn chưa ra đời".
    Whisper stretches the word after a silence over it, so a silence belongs before the word whose span holds it."""
    raw = text.split()
    ref = [words(w)[0] if words(w) else "" for w in raw]
    hw = heard.get("words", [])
    hyp = [words(w[0])[0] if words(w[0]) else "" for w in hw]
    match = {}
    for blk in difflib.SequenceMatcher(None, hyp, ref, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            match[blk.a + k] = blk.b + k
    out = []
    for a, b in silences(path, MIN_PAUSE):
        mid = (a + b) / 2
        i = next((k for k, w in enumerate(hw) if w[1] <= mid <= (w[2] or w[1])), None)
        if i is None or i == 0 or i not in match:
            continue
        j = match[i]
        if j > 0 and not re.search(r"[,.;:!?…]$", raw[j - 1]):
            out.append(f"{raw[j - 1]} | {raw[j]} ({b - a:.1f}s)")
    return out


def transcribe(paths: list) -> dict:
    py = render.CFG["voice"].get("vieneu_python", "python3")
    with tempfile.TemporaryDirectory() as tmp:
        src, dst = Path(tmp) / "in.json", Path(tmp) / "out.json"
        src.write_text(json.dumps([str(p) for p in paths]))
        subprocess.run([py, str(ROOT / "tools/asr_worker.py"), MODEL, str(src), str(dst)], check=True)
        return json.loads(dst.read_text())


def pitch(path: Path) -> float:
    """Median pitch (Hz) of the voiced frames of a take, by autocorrelation (70-400 Hz)."""
    import wave
    import numpy as np
    with wave.open(str(path)) as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    step = 4 if sr > 30000 else 2
    x, sr = x[::step], sr // step  # enough for speech pitch, 4x faster
    win, hop = int(sr * 0.04), int(sr * 0.02)
    lo, hi = int(sr / 400), int(sr / 70)
    f0 = []
    for i in range(0, len(x) - win, hop):
        fr = x[i:i + win] - x[i:i + win].mean()
        if np.sqrt((fr ** 2).mean()) < 0.02:
            continue
        ac = np.correlate(fr, fr, "full")[win - 1:]
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.4 * ac[0]:
            f0.append(sr / k)
    return float(np.median(f0)) if f0 else 0.0


def judge(line: dict, heard: dict) -> dict:
    ref, hyp = words(line["text"]), words(heard["text"])
    err = error_rate(ref, hyp)
    rep = repeats(ref, hyp)
    pauses = bad_pauses(line["text"], heard, line["path"])
    slow = line["sec"] / max(1, len(ref)) > MAX_SEC_WORD
    f0 = pitch(line["path"])
    off = abs(12 * math.log2(f0 / REF_F0)) if f0 and REF_F0 else 0.0  # semitones from the narrator's usual pitch
    score = err + 0.3 * len(pauses) + (0.5 if rep else 0) + (0.5 if slow else 0) + 0.25 * max(0.0, off - 1)
    return {**line, "heard": heard["text"], "err": err, "repeat": rep, "pauses": pauses, "slow": slow,
            "pitch": off, "score": score,
            "bad": err > MAX_ERR or bool(rep) or bool(pauses) or slow or off > MAX_PITCH_OFF}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("story")
    ap.add_argument("--scenes", help="e.g. 16-19 or 5")
    ap.add_argument("--fix", action="store_true", help="retake flagged lines")
    ap.add_argument("--tries", type=int, default=5, help="retake rounds")
    args = ap.parse_args()

    story = json.loads(Path(args.story).read_text())
    render.CFG = render.deep_merge(render.DEFAULTS, story.get("settings", {}))
    render.STORY = story
    scenes = [s for s in story["scenes"] if s.get("text")]
    if args.scenes:
        a, _, b = args.scenes.partition("-")
        scenes = [s for s in scenes if float(a) <= s["id"] <= float(b or a)]

    lines = []
    for s in scenes:
        sv = render.narration_voice(s.get("voice"))
        for item in render.tts_lines(s["text"], sv):
            if item[0] != "say":
                continue
            v = item[2]
            audio, path, sent = render.speak_take(item[1], v, v["sample_rate"])
            sec = len(render.trim_silence(audio, v["sample_rate"])) / v["sample_rate"]
            lines.append({"scene": s["id"], "text": item[1], "v": v, "path": path, "sec": sec})
    global REF_F0
    pitches = [p for p in (pitch(l["path"]) for l in lines) if p]
    REF_F0 = sorted(pitches)[len(pitches) // 2] if pitches else 0.0
    print(f"{len(lines)} câu, cao độ giọng trung bình {REF_F0:.0f} Hz, đang nghe lại...")
    heard = transcribe([l["path"] for l in lines])
    results = [judge(l, heard[str(l["path"])]) for l in lines]

    if args.fix:  # rounds: new takes for every line still flagged, heard in one batch, best take kept
        todo = [k for k, r in enumerate(results) if r["bad"]]
        for k in todo:
            shutil.copy(results[k]["path"], results[k]["path"].with_suffix(".best.wav"))
            results[k]["retaken"] = True
        for rnd in range(args.tries):
            if not todo:
                break
            fresh = {}
            for k in todo:
                r = results[k]
                r["path"].unlink()
                audio, _, _ = render.speak_take(r["text"], r["v"], r["v"]["sample_rate"])
                fresh[k] = len(render.trim_silence(audio, r["v"]["sample_rate"])) / r["v"]["sample_rate"]
            heard = transcribe([results[k]["path"] for k in todo])
            for k in todo:
                r = results[k]
                new = judge({**r, "sec": fresh[k]}, heard[str(r["path"])])
                if (new["bad"], new["score"]) < (r["bad"], r["score"]):
                    results[k] = {**new, "retaken": True}
                    shutil.copy(r["path"], r["path"].with_suffix(".best.wav"))
            todo = [k for k in todo if results[k]["bad"]]
            print(f"  lượt {rnd + 1}: còn lỗi {len(todo)}")
        for r in results:
            best = r["path"].with_suffix(".best.wav")
            if best.exists():
                shutil.move(best, r["path"])

    bad = [r for r in results if r["bad"]]
    stem = Path(args.story).stem
    md = [f"# Kiểm tra giọng đọc — {stem}", "",
          f"{len(results)} câu · lỗi: {len(bad)} · đã đọc lại: {sum(1 for r in results if r.get('retaken'))}", "",
          "| Cảnh | Sai | Lặp | Ngắt sai | Chậm | Lệch cao độ | Kịch bản | Nghe được |", "|---|---|---|---|---|---|---|---|"]
    for r in results:
        if r["bad"] or r.get("retaken"):
            md.append(f"| {r['scene']} | {r['err']:.0%} | {r['repeat']} | {'; '.join(r['pauses'])} | {'x' if r['slow'] else ''} | {r['pitch']:.1f} | "
                      f"{r['text']} | {r['heard']} |")
    out = ROOT / "build" / f"{stem}_voice_check.md"
    out.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"lỗi còn lại: {len(bad)}/{len(results)} -> {out}")


if __name__ == "__main__":
    main()
