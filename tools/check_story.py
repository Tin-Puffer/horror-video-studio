#!/usr/bin/env python3
"""Check a storyboard against the asset library and write the asset request list.

  python3 tools/check_story.py scripts/<story>.json

- every sprite / cycle / background / hotspot / anchor the story uses must exist,
  or be listed in the story's "asset_requests"
- writes build/<story>_requests.md: one ready-to-paste Gemini prompt per
  missing asset (style prompt of the character + layout + poses), with the
  reference images to attach
- writes build/<story>_refs/<nn>_<request_id>/: the reference images to attach + prompt.txt,
  one folder per open request (folders of finished requests are removed; ingest.py removes its own)
- exit code 1 if something is missing and not requested

asset_requests entries:
  {"id": "boy_hoodie_sheet_L", "kind": "sheet", "character": "boy_hoodie",
   "grid": [2, 3], "why": "cảnh 5, 9",
   "note": "<English, optional: overrides the style for this sheet, e.g. a ghost version>",
   "refs": ["<extra reference image, e.g. a second character in the poses>"],
   "sprites": [{"name": "L1_open_fridge", "pose": "<English pose>", "desc": "<VN>",
                "tags": [...], "facing": "right", "anchors_needed": ["hand"]}, ...]}
  {"id": "bg4_bathroom", "kind": "background", "scene": "<English scene>",
   "desc": "<VN>", "tags": [...], "floor_y": 0.95, "char_h": 0.46, "refs": ["<layout reference>"],
   "hotspots_needed": ["mirror", "sink"]}
  {"id": "neighbor_base", "kind": "character_base", "character": "neighbor",
   "name": "<VN>", "design": "<English full description>", "default_h": 0.5}
  {"id": "knock_3", "kind": "sound", "sound_kind": "sfx" | "music", "desc": "<VN>",
   "search": "<English keywords for Pixabay/Freesound>", "length": "~2s", "tags": [...], "volume": 1.0}
"""
from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHARS = ROOT / "assets/characters"
BGS = ROOT / "assets/backgrounds"

SHEET_LAYOUT = ("Character sheet, 16:9, pure plain white background, {n} poses arranged in a "
                "{r}x{c} grid with wide empty space between poses, poses must not overlap or touch "
                "each other or the image edges, same character size in every pose, no text, no labels, "
                "no ground shadows, no background objects.")
BASE_LAYOUT = ("A full-body character design, standing straight, front view, arms at the sides. "
               "Hand-drawn crayon / colored-pencil texture, thick black outlines, simple shapes and minimal "
               "flat colors, the same art style as the reference image. Pure plain white background, "
               "centered, full body visible with space around, no text, no shadow on the ground, "
               "never white clothing. 1:1.")


def load_json(path: Path) -> dict:
    return json.loads(path.read_text()) if path.exists() else {}


def char_meta(char: str) -> dict:
    return load_json(CHARS / char / "meta.json")


def sprite_exists(ref: str) -> bool:
    return (CHARS / f"{ref}.png").exists()


SOUND_EXT = ("wav", "mp3", "ogg", "m4a", "flac", "aiff")


def sound_exists(name: str) -> bool:
    return any((ROOT / "assets/audio/sfx" / f"{name}.{e}").exists() for e in SOUND_EXT)


def collect_sounds(story: dict) -> dict:
    sounds = {}
    for s in story["scenes"]:
        for cue in s.get("sfx", []):
            sounds.setdefault(cue["sound"], []).append(s["id"])
    for m in story.get("music", []):
        sounds.setdefault(m["sound"], []).append("nhạc nền")
    return sounds


def collect(story: dict):
    """(sprites, cycles, backgrounds, hotspot uses, anchor uses) referenced by the story."""
    sprites, cycles, bgs, hotspots, anchors = {}, {}, {}, [], []
    for s in story["scenes"]:
        sid = s["id"]
        if s.get("bg") and s["bg"] != "black":
            bgs.setdefault(s["bg"], []).append(sid)
        for L in s.get("layers", []):
            refs = []
            if "sprite" in L:
                refs.append(L["sprite"])
            for f in L.get("frames", []):
                refs.append(f if isinstance(f, str) else f["sprite"])
            if "cycle" in L:
                cycles.setdefault(L["cycle"], []).append(sid)
            for r in refs:
                sprites.setdefault(r, []).append(sid)
            for key in ("pin", "clip_circle"):
                at = L.get(key, {}).get("at") if key == "pin" else L.get(key)
                if isinstance(at, str):
                    hotspots.append((s["bg"], at, sid))
            if L.get("pin"):
                for r in refs:
                    anchors.append((r, L["pin"]["point"], sid))
    return sprites, cycles, bgs, hotspots, anchors


PAUSE_MARK = re.compile(r"\[(\d+(?:\.\d+)?)\]")


def narration_parts(text) -> list[tuple[str, bool]]:
    """(text, is_narrator) for a scene's text (string or list form)."""
    if isinstance(text, str):
        return [(text, True)]
    out = []
    for part in text or []:
        if isinstance(part, str):
            out.append((part, True))
        elif "say" in part:
            out.append((part["say"], not part.get("voice")))
    return out


def rule_warnings(story: dict) -> list[str]:
    """Agreed storyboard rules (scripts/QUY_TAC_KICH_BAN.md) that can be checked mechanically."""
    w = []
    st = story.get("settings", {})
    used_presets = {st.get("voice", {}).get("preset")} | {
        p.get("voice", {}).get("preset") for s in story["scenes"] if isinstance(s.get("text"), list)
        for p in s["text"] if isinstance(p, dict)} | {s.get("voice", {}).get("preset") for s in story["scenes"]}
    missing = sorted(p for p in used_presets - {None} if p not in story.get("voice_presets", {}))
    if missing:
        w.append(f"giọng chưa nhúng vào voice_presets của kịch bản: {missing} (§1)")
    for block in ("audio", "timing", "subtitles"):
        if block not in st:
            w.append(f"thiếu settings.{block} (§1)")
    if st.get("subtitles", {}).get("split") != "sentence":
        w.append('phụ đề nên để settings.subtitles.split = "sentence" (§8)')
    extra = sorted(set(story.get("voice_presets", {})) - {st.get("voice", {}).get("preset")})
    if extra:
        w.append(f"chỉ dùng giọng người kể — bỏ các giọng phụ khỏi voice_presets: {extra} (§3)")
    for s in story["scenes"]:
        sid = s["id"]
        if s.get("voice"):
            w.append(f"cảnh {sid}: có giọng riêng cho cảnh — chỉ dùng giọng người kể (§3)")
        if any(not narrator for _, narrator in narration_parts(s.get("text"))):
            w.append(f"cảnh {sid}: có câu đọc bằng giọng khác — để người kể thuật lại (§3)")
        for txt, narrator in narration_parts(s.get("text")):
            if narrator:
                short = [float(n) for n in PAUSE_MARK.findall(txt) if float(n) < 0.5]
                if short:
                    w.append(f"cảnh {sid}: ngắt nghỉ ngắn {short} giữa lời kể — viết liền mạch, chỉ nghỉ ≥ 0.5s (§3)")
                if re.search(r"\b(Cốc|Cộc|Rầm|Két|Bùm)\b[.!…]", txt):
                    w.append(f"cảnh {sid}: tiếng động đang được đọc thành lời — dùng sfx (§3)")
        words = sum(len(PAUSE_MARK.sub("", t).split()) for t, _ in narration_parts(s.get("text")))
        if words > 45:
            w.append(f"cảnh {sid}: lời đọc {words} chữ — tách cảnh (≤ ~40 chữ/cảnh) (§3)")
        cam = s.get("camera", {})
        keys = cam.get("keys", [])
        if keys:
            xs = [k["x"] for k in keys if "x" in k]
            ys = [k["y"] for k in keys if "y" in k]
            zmin = min([k.get("zoom", 1.0) for k in keys] or [1.0])
            if zmin < 1.15 and (max(xs or [0]) - min(xs or [0]) > 0.02 or max(ys or [0]) - min(ys or [0]) > 0.02):
                w.append(f"cảnh {sid}: camera lia khi zoom {zmin} < 1.15 — khung sẽ kẹt mép phông (§6)")
        if s.get("text") is None and not s.get("sfx") and s.get("bg") != "black" and not s.get("title_text"):
            w.append(f"cảnh {sid}: cảnh không lời mà cũng không có âm thanh (§7)")
        for L in s.get("layers", []):
            if L.get("flip") is not None:
                w.append(f"cảnh {sid}: lớp dùng flip — dùng \"face\" (§5)")
            moving = isinstance(L.get("x"), list) and abs(L["x"][1] - L["x"][0]) > 0.08
            if moving and "sprite" in L and not L.get("pin"):
                w.append(f"cảnh {sid}: {L['sprite']} di chuyển bằng ảnh tĩnh — dùng cycle (§5)")
    return w


def request_prompt(req: dict) -> tuple[str, list[str]]:
    kind = req["kind"]
    if kind == "sheet":
        meta = char_meta(req["character"])
        r, c = req.get("grid", [2, 3])
        poses = "; ".join(f"{i + 1}) {sp['pose']}" for i, sp in enumerate(req["sprites"]))
        note = f"{req['note']} " if req.get("note") else ""
        prompt = (f"{meta.get('style_prompt', '')} {note}{SHEET_LAYOUT.format(n=r * c, r=r, c=c)} "
                  f"Poses (left to right, top to bottom): {poses}.")
        return prompt, meta.get("reference_images", []) + req.get("refs", [])
    if kind == "background":
        bg = load_json(BGS / "meta.json")
        return f"{bg.get('style_prompt', '')} {req['scene']}", bg.get("reference_images", []) + req.get("refs", [])
    if kind == "sound":
        if req.get("prompt"):
            return (f"{req['prompt']}\n(ElevenLabs Sound Effects, Duration {req.get('length', 'Auto')}; "
                    f"hoặc tìm \"{req['search']}\" trên pixabay.com/sound-effects)", [])
        return (f"Tìm trên pixabay.com/sound-effects hoặc freesound.org với từ khoá: \"{req['search']}\" "
                f"(độ dài {req.get('length', 'tuỳ')}). Tải về dạng mp3/wav.", [])
    if kind == "character_base":
        refs = [m for m in (char_meta(d.name).get("reference_images", [])[:1]
                            for d in CHARS.iterdir() if d.is_dir()) if m]
        return f"{req['design']} {BASE_LAYOUT}", [refs[0][0]] if refs else []
    raise ValueError(f"unknown request kind {kind}")


def write_ref_folders(stem: str, open_reqs: list) -> None:
    """build/<stem>_refs/<nn>_<id>/ = reference images to attach + prompt.txt, so nothing has to be looked up."""
    base = ROOT / "build" / f"{stem}_refs"
    shutil.rmtree(base, ignore_errors=True)
    for i, req in enumerate(open_reqs, 1):
        prompt, refs = request_prompt(req)
        folder = base / f"{i:02d}_{req['id']}"
        folder.mkdir(parents=True)
        missing = []
        for r in refs:
            src = ROOT / r
            if src.exists():
                shutil.copy(src, folder / src.name)
            else:
                missing.append(r)
        note = [f"Mã yêu cầu: {req['id']} ({req['kind']})", f"Dùng cho: {req.get('why', req.get('desc', ''))}", ""]
        if req["kind"] == "sheet":
            note += ["Ô (trái→phải, trên→dưới): " + ", ".join(sp["name"] for sp in req["sprites"]), ""]
        if req["kind"] == "sound":
            note += [f"Âm thanh: {req.get('desc', '')}", f"Độ dài: {req.get('length', 'tuỳ')}", ""]
        if refs:
            note += ["Kéo hết ảnh trong thư mục này vào Gemini, rồi dán prompt dưới đây.", ""]
        if missing:
            note += ["(Máy này không có, bỏ qua: " + ", ".join(missing) + ")", ""]
        (folder / "prompt.txt").write_text("\n".join(note + ["PROMPT:", prompt, ""]))


def main():
    path = Path(sys.argv[1])
    story = json.loads(path.read_text())
    requests = story.get("asset_requests", [])
    requested_sprites = {f"{r['character']}/{sp['name']}" for r in requests if r["kind"] == "sheet"
                         for sp in r["sprites"]}
    requested_bgs = {r["id"] for r in requests if r["kind"] == "background"}
    requested_chars = {r["character"] for r in requests if r["kind"] == "character_base"}
    requested_sounds = {r["id"] for r in requests if r["kind"] == "sound"}

    sprites, cycles, bgs, hotspots, anchors = collect(story)
    errors, pending = [], []

    for ref, scenes in sorted(sprites.items()):
        if sprite_exists(ref):
            continue
        (pending if ref in requested_sprites else errors).append(f"sprite {ref} (cảnh {scenes})")
    for ref, scenes in sorted(cycles.items()):
        char, _, name = ref.partition("/")
        if name not in char_meta(char).get("cycles", {}):
            errors.append(f"cycle {ref} không có trong meta.json (cảnh {scenes})")
    for bg, scenes in sorted(bgs.items()):
        if (BGS / f"{bg}.png").exists():
            continue
        (pending if bg in requested_bgs else errors).append(f"background {bg} (cảnh {sorted(set(scenes))})")
    bg_meta = load_json(BGS / "meta.json").get("backgrounds", {})
    for bg, name, sid in hotspots:
        if name not in bg_meta.get(bg, {}).get("hotspots", {}):
            target = pending if bg in requested_bgs else errors
            target.append(f"hotspot {bg}.{name} (cảnh {sid}) — cần đo sau khi có phông")
    for ref, point, sid in anchors:
        char, _, name = ref.partition("/")
        if point not in char_meta(char).get("sprites", {}).get(name, {}).get("anchors", {}):
            target = pending if ref in requested_sprites else errors
            target.append(f"anchor {ref}.{point} (cảnh {sid}) — cần đo sau khi có sprite")
    for char in {r.split("/")[0] for r in sprites}:
        if not (CHARS / char).is_dir() and char not in requested_chars:
            errors.append(f"nhân vật {char} chưa có và chưa được yêu cầu (character_base)")

    sounds = collect_sounds(story)
    for name, where in sorted(sounds.items()):
        if not sound_exists(name):
            (pending if name in requested_sounds else errors).append(f"âm thanh {name} ({where})")

    warnings = rule_warnings(story)

    used = [r for r in sprites if sprite_exists(r)]
    print(f"{path.name}: {len(story['scenes'])} cảnh, dùng lại {len(used)} sprite + "
          f"{sum(1 for b in bgs if (BGS / f'{b}.png').exists())} phông + "
          f"{sum(1 for n in sounds if sound_exists(n))}/{len(sounds)} âm thanh có sẵn")

    # request list for the user
    open_reqs = []
    for req in requests:
        if req["kind"] == "sheet":
            done = all(sprite_exists(f"{req['character']}/{sp['name']}") for sp in req["sprites"])
        elif req["kind"] == "background":
            done = (BGS / f"{req['id']}.png").exists()
        elif req["kind"] == "sound":
            done = sound_exists(req["id"])
        else:
            done = (CHARS / req["character"]).is_dir()
        if not done:
            open_reqs.append(req)
    out = ROOT / "build" / f"{path.stem}_requests.md"
    out.parent.mkdir(exist_ok=True)
    md = [f"# Asset cần tạo cho `{path.name}`", "",
          "Mỗi mục: đính kèm ảnh tham chiếu, dán prompt vào Gemini, gửi ảnh kết quả cho Claude kèm mã yêu cầu.",
          f"Ảnh cần đính kèm + prompt đã gom sẵn theo từng mục trong `build/{path.stem}_refs/`.", ""]
    for req in open_reqs:
        prompt, refs = request_prompt(req)
        md += [f"## `{req['id']}` ({req['kind']})", "",
               f"- Dùng cho: {req.get('why', '')}",
               f"- Đính kèm: {', '.join(f'`{r}`' for r in refs) or '(không)'}"]
        if req["kind"] == "sheet":
            md += ["- Ô (trái→phải, trên→dưới): " + ", ".join(sp["name"] for sp in req["sprites"])]
        if req["kind"] == "sound":
            md += [f"- Âm thanh: {req.get('desc', '')}", f"- Độ dài: {req.get('length', 'tuỳ')}"]
        md += ["", "```", prompt, "```", ""]
    if not open_reqs:
        md.append("Không còn asset nào cần tạo.")
    out.write_text("\n".join(md))
    write_ref_folders(path.stem, open_reqs)

    for w in warnings:
        print("  quy tắc:", w)
    for p in pending:
        print("  chờ asset:", p)
    for e in errors:
        print("  LỖI:", e)
    print(f"  {len(open_reqs)} yêu cầu asset đang mở -> {out.relative_to(ROOT)}")
    if open_reqs:
        print(f"  ảnh tham chiếu + prompt từng yêu cầu -> build/{path.stem}_refs/")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
