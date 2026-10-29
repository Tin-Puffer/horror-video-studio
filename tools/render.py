#!/usr/bin/env python3
"""Render a storyboard JSON (scripts/*.json) into an MP4 with narration.

Usage:
  python3 tools/render.py scripts/cuoc_goi_3h.json            # full quality
  python3 tools/render.py scripts/cuoc_goi_3h.json --preview  # settings.preview, fast
  python3 tools/render.py scripts/cuoc_goi_3h.json --scenes 16-19 --preview

The storyboard decides every asset's configuration, position and size. This
file only holds fallback defaults (DEFAULTS); anything there can be overridden
in the storyboard:

  settings     global: video size/fps, voice, timing, look, subtitles, phone UI,
               layer defaults. Deep-merged over DEFAULTS.
  characters   per-character layer defaults, keyed by the folder in
               assets/characters (e.g. "ghost_mother": {"glow": true}).
  scenes       list of scenes.

Scene keys (all optional except bg):
  bg              background name in assets/backgrounds, or "black"
  text            narration (TTS + subtitle). "[0.6]" = 0.6 s pause. Or a list of
                  strings / {"say": "...", "voice": {...}} / {"pause": s} for per-line voices
  voice           per-scene voice overrides (merged over settings.voice; "preset" names a
                  voice from the storyboard's "voice_presets" or assets/audio/voice_presets.json)
  duration        fixed length (s); otherwise narration + lead/tail, at least min_duration
  layers          list of sprites / phone UI drawn in order, see draw_layer()
  camera          {"keys": [{"p", "zoom", "x", "y", "ease"}...], "handheld": n}  or
                  {"zoom": [from, to], "focus": [x, y] | [[x0,y0],[x1,y1]], "ease"}  see camera_at()
                  (panning needs zoom > 1: the frame never leaves the background)
  sfx             sound cues in the scene, see mix_audio(); story-level "music" too
  shake           {"amp": px@1080p, "from": p, "to": p}  p = 0..1 of the scene
  flash           [p, ...]  white flash moments
  flicker         0..1 random light flicker strength
  bg_dim          0..1 darken the background (phone UI scenes)
  title_text      centered caption
  fade_in/out     seconds from/to black
Layer keys: see draw_layer(). Layer values given as [a, b] are interpolated
across the layer's lifetime. A layer's settings resolve as
settings.layer < characters[<folder>] < the layer itself.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import random
import re
import subprocess
import textwrap
import wave
from functools import lru_cache
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent

DEFAULTS = {
    "video": {"size": [1920, 1080], "fps": 24, "crf": 20, "preset": "medium"},
    "preview": {"size": [960, 540], "fps": 12, "preset": "veryfast"},
    "voice": {
        "piper": "piper",            # piper-tts executable (PATH), or set in config.local.json
        "models_dir": "voices",      # folder with <model>.onnx + .onnx.json (relative to the project)
        "engine": "piper",           # "piper" or "vieneu" (VieNeu-TTS: preset voices + voice cloning)
        "vieneu_voice": "preset:Hải Đăng",  # VieNeu: "preset:<name>" or "clone:<id>" (tools/clone_voice.py)
        "vieneu_python": "python3", "dubber_root": "",  # where vieneu + the Dubber package live
        "model": "ngochuyennew", "length_scale": 1.0, "sentence_silence": 0.3,
        # phrasing (see tts): pauses shorter than this are read as a comma, not a cut;
        # soften_endings "none" | "final" | "all" (full stops read as commas);
        # trim_chunks drops engine silence around each chunk (+ chunk_gap seconds)
        "merge_pause_below": 0.45, "soften_endings": "none", "trim_chunks": True, "chunk_gap": 0.12,
        "max_sec_per_word": 0.5,     # run-on guard: longer per word = the engine kept going
        "max_inner_pause": 0.35,     # silences inside a line are cut to this (0 = keep)
        # voice colour (see voice_filters): pitch (semitones), tempo, reverb 0..1,
        # lowpass/highpass Hz, volume dB; piper: noise_scale (expressiveness), noise_w (rhythm variation)
        "sample_rate": 44100,        # narration rate; every engine/preset is resampled to it
    },
    "timing": {"lead": 0.4, "tail": 0.7, "min_duration": 2.5, "fade_in": 0.15, "fade_out": 0.0},
    "audio": {"sample_rate": 44100, "narration_volume": 1.0, "sfx_volume": 1.0, "music_volume": 0.5,
              "duck": 0.35,            # music gain while narration speaks
              "placeholder_beep": True,  # audible stand-in for sounds not in the library yet
              "trim_silence": True, "trim_threshold": 0.08,  # fraction of the file's peak
              "normalize_db": -18,
              "limiter_ceiling_db": -2.0},  # loudness of every sound before volume; null = as recorded
    "fonts": {"regular": "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
              "bold": "/System/Library/Fonts/Supplemental/Arial Bold.ttf"},
    "look": {
        "night_tint": [0.80, 0.84, 0.98],      # multiplies character colours when layer.tint
        "glow_color": [170, 200, 230],         # rim colour when layer.glow
        "glow_strength": 0.55, "glow_size": 9,
        "vignette": {"start": 0.65, "spread": 0.75, "power": 1.6, "max_alpha": 200},
        "flash": {"length": 0.25, "max_alpha": 230},
        "bob_hz": 1.6, "breathe_hz": 0.35,
    },
    "subtitles": {"enabled": True, "size": 0.042, "line_height": 0.055, "bottom": 0.06,
                  "wrap": 48, "color": [240, 240, 240], "stroke": [0, 0, 0],
                  "split": "sentence",   # "sentence": one sentence at a time, timed with the voice; "none": whole text
                  "min_chars": 18},      # shorter sentences are shown together with the next
    "title": {"size": 0.06, "color": [225, 225, 230]},
    "phone": {"clock": "03:00", "call_label": "Cuộc gọi đến…", "call_sub": "Di động",
              "decline": "Từ chối", "accept": "Trả lời", "message_time": "Vừa xong",
              "message_wrap": 15, "glow_color": [120, 160, 255, 90]},
    "layer": {"x": 0.5, "y": 0.95, "h": 0.45, "fps": 8, "flip": None, "face": None,
              "tint": True, "glow": False, "breathe": 0.0},
}
CHARACTERS: dict = {}
STORY: dict = {}


def deep_merge(base: dict, over: dict) -> dict:
    out = copy.deepcopy(base)
    for k, v in (over or {}).items():
        out[k] = deep_merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


# machine-specific settings (tool paths, fonts) stay out of git: config.local.json
_LOCAL = ROOT / "config.local.json"
if _LOCAL.exists():
    DEFAULTS = deep_merge(DEFAULTS, {k: v for k, v in json.loads(_LOCAL.read_text()).items() if not k.startswith("_")})
CFG: dict = DEFAULTS


@lru_cache(maxsize=None)
def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(CFG["fonts"]["bold" if bold else "regular"], size)


# ---------------------------------------------------------------- narration

PAUSE = re.compile(r"\[(\d+(?:\.\d+)?)\]")


@lru_cache(maxsize=None)
def library_presets() -> dict:
    path = ROOT / "assets/audio/voice_presets.json"
    return json.loads(path.read_text()).get("presets", {}) if path.exists() else {}


def voice_presets() -> dict:
    """Shared library (assets/audio/voice_presets.json) < the storyboard's own "voice_presets",
    so a storyboard can carry the exact voices it was made with."""
    return {**library_presets(), **STORY.get("voice_presets", {})}


def resolve_voice(*layers: dict | None) -> dict:
    """Layers applied left to right; in each layer its "preset" goes first, then the
    layer's own keys. Pass only what was written (not defaults merged in), otherwise
    the defaults would override the preset — use narration_voice() for scenes."""
    out = {}
    for layer in layers:
        if not layer:
            continue
        if layer.get("preset"):
            out = deep_merge(out, voice_presets()[layer["preset"]])
        out = deep_merge(out, {k: v for k, v in layer.items() if k != "preset"})
    return out


def narration_voice(scene_voice: dict | None = None) -> dict:
    """Voice for a scene: defaults < storyboard settings.voice (its preset, then its keys) < scene voice."""
    written = deep_merge(STORY.get("voice", {}), STORY.get("settings", {}).get("voice", {}))
    return {**resolve_voice(DEFAULTS["voice"], written, scene_voice), "sample_rate": CFG["voice"]["sample_rate"]}


def speech_items(text) -> list:
    """Scene text -> [("say", str, voice_override) | ("pause", seconds)].
    text: "plain [0.6] text" (a [n] marker = n seconds of silence) or a list of
    strings / {"say": str, "voice": {...}} / {"pause": n}."""
    items = []
    for part in (text if isinstance(text, list) else [text]):
        if isinstance(part, dict) and "pause" in part:
            items.append(("pause", float(part["pause"])))
            continue
        say, over = (part, None) if isinstance(part, str) else (part["say"], part.get("voice"))
        pos = 0
        for m in PAUSE.finditer(say):
            if say[pos:m.start()].strip():
                items.append(("say", say[pos:m.start()].strip(), over))
            items.append(("pause", float(m.group(1))))
            pos = m.end()
        if say[pos:].strip():
            items.append(("say", say[pos:].strip(), over))
    return items


def spoken_text(text) -> str:
    """What the subtitle shows: the spoken words without pause markers."""
    return " ".join(i[1] for i in speech_items(text) if i[0] == "say")


def voice_filters(v: dict, sr: int) -> str:
    """ffmpeg filter chain for the voice colour settings (piper itself has no pitch control)."""
    f = [f"aresample={sr}"]  # engines output 22.05k (piper) / 48k (VieNeu): work at one known rate
    if v.get("pitch"):  # semitones; resample trick keeps the duration
        r = 2 ** (v["pitch"] / 12)
        f += [f"asetrate={sr * r:.0f}", f"aresample={sr}", f"atempo={1 / r:.5f}"]
    if v.get("tempo") and v["tempo"] != 1:
        f.append(f"atempo={v['tempo']}")
    if v.get("highpass"):
        f.append(f"highpass=f={v['highpass']}")
    if v.get("lowpass"):
        f.append(f"lowpass=f={v['lowpass']}")
    if v.get("reverb"):
        a = v["reverb"]
        f.append(f"aecho=0.8:0.88:45|95|160:{0.45 * a:.3f}|{0.32 * a:.3f}|{0.2 * a:.3f}")
    if v.get("volume"):
        f.append(f"volume={v['volume']}dB")
    return ",".join(f)


_VIENEU = None


def vieneu(req: dict, v: dict) -> dict:
    """Send one request to the VieNeu worker (started on first use, model loaded once)."""
    global _VIENEU
    if _VIENEU is None or _VIENEU.poll() is not None:
        _VIENEU = subprocess.Popen([v["vieneu_python"], str(ROOT / "tools/vieneu_worker.py"), v["dubber_root"], str(ROOT)],
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, encoding="utf-8")
    _VIENEU.stdin.write(json.dumps(req, ensure_ascii=False) + "\n")
    _VIENEU.stdin.flush()
    reply = json.loads(_VIENEU.stdout.readline())
    if not reply.get("ok"):
        raise RuntimeError(f"VieNeu: {reply.get('error')}")
    return reply


# settings that change what a chunk sounds like, per engine (others don't invalidate the cache)
_ENGINE_KEYS = {"piper": ("model", "length_scale", "sentence_silence", "noise_scale", "noise_w"),
                "vieneu": ("vieneu_voice",)}
_COLOUR_KEYS = ("pitch", "tempo", "highpass", "lowpass", "reverb", "volume", "sample_rate")


def tts_chunk(text: str, v: dict) -> np.ndarray:
    """One piece of speech as float32 at v["sample_rate"], cached in build/tts/.
    piper: speed = length_scale; VieNeu has no speed control, use "tempo"."""
    engine = v.get("engine", "piper")
    ident = {k: v.get(k) for k in _ENGINE_KEYS[engine] + _COLOUR_KEYS}
    key = hashlib.sha1(json.dumps([text, engine, ident] if engine != "piper" else [text, v],
                                  sort_keys=True).encode()).hexdigest()[:16]
    path = ROOT / "build/tts" / f"{key}.wav"
    sr = v["sample_rate"]
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = path.with_suffix(".raw.wav")
        if engine == "vieneu":
            vieneu({"cmd": "say", "text": text, "voice": v["vieneu_voice"], "out": str(raw)}, v)
        else:
            models = Path(v["models_dir"]).expanduser()
            model = (models if models.is_absolute() else ROOT / models) / f"{v['model']}.onnx"
            cmd = [v["piper"], "-m", str(model), "-f", str(raw),
                   "--length-scale", str(v["length_scale"]), "--sentence-silence", str(v["sentence_silence"])]
            for opt in ("noise_scale", "noise_w"):
                if v.get(opt) is not None:
                    cmd += [f"--{opt.replace('_', '-')}", str(v[opt])]
            subprocess.run(cmd, input=text.encode(), check=True, capture_output=True)
        chain = voice_filters(v, sr)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-ac", "1", "-ar", str(sr)]
                       + (["-af", chain] if chain else []) + [str(path)], check=True)
        raw.unlink()
    with wave.open(str(path)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768


def phrase_plan(text, voice: dict) -> list:
    """speech_items with short pauses folded into the phrase: TTS engines read every
    chunk as a finished sentence (falling, lengthened last word), so a chunk is only
    cut at pauses >= voice["merge_pause_below"]; shorter ones become a comma."""
    limit = voice.get("merge_pause_below", 0) or 0
    plan = []
    for item in speech_items(text):
        prev = plan[-1] if plan else None
        if item[0] == "pause" and item[1] < limit and prev and prev[0] == "say":
            plan[-1] = ("say", prev[1] if prev[1].rstrip()[-1:] in ",.…!?:;" else prev[1] + ",", prev[2], True)
            continue
        if item[0] == "say" and prev and prev[0] == "say" and len(prev) == 4 and prev[2] == item[2]:
            plan[-1] = ("say", prev[1] + " " + item[1], item[2])  # glued across a folded pause
            continue
        plan.append(item)
    return [p[:3] if p[0] == "say" else p for p in plan]


def soften(text: str, mode: str) -> str:
    """Lighter sentence endings for the TTS input (subtitles keep the real punctuation).
    "final": the chunk's closing full stop becomes a comma; "all": every full stop does."""
    if mode == "all":
        text = re.sub(r"\.(?=\s|$)", ",", text)
    elif mode == "final":
        text = re.sub(r"\.\s*$", ",", text)
    return text


def squeeze_pauses(x: np.ndarray, sr: int, longest: float) -> np.ndarray:
    """Shorten silences inside a chunk to at most `longest` seconds (engines sometimes
    leave multi-second holes mid-sentence); pauses meant by the script are separate."""
    hop = int(sr * 0.02)
    n = len(x) // hop
    if n == 0 or longest <= 0:
        return x
    loud = np.sqrt((x[: n * hop].reshape(n, hop) ** 2).mean(axis=1)) > 10 ** (-40 / 20)
    keep, run = [], 0
    max_run = int(longest / 0.02)
    for i, a in enumerate(loud):
        run = 0 if a else run + 1
        if a or run <= max_run:
            keep.append(i)
    return np.concatenate([x[i * hop:(i + 1) * hop] for i in keep] + [x[n * hop:]])


def trim_silence(x: np.ndarray, sr: int, keep: float = 0.06) -> np.ndarray:
    """Drop the engine's own silence around a chunk; pauses come from the script."""
    loud = np.flatnonzero(np.abs(x) > 10 ** (-40 / 20))
    if not len(loud):
        return x
    k = int(keep * sr)
    return x[max(0, loud[0] - k):loud[-1] + k]


def speak_checked(text: str, v: dict, sr: int) -> np.ndarray:
    """One line, guarded against run-on synthesis: neural engines sometimes keep
    babbling after the last word (seen with a closing comma or "à?"). When the result
    is far longer than the words need, try other endings and keep the shortest."""
    words = len(text.split())
    limit = max(1.2, words * v.get("max_sec_per_word", 0.5)) / v.get("tempo", 1.0)
    first = soften(text, v.get("soften_endings", "none"))
    bare = text.rstrip(" ,.…!?:;")
    tried = []
    for cand in dict.fromkeys([first, text, bare + ".", bare + "!"]):
        chunk = tts_chunk(cand, v)
        length = len(trim_silence(chunk, sr)) / sr
        if length <= limit:
            return chunk
        tried.append((length, chunk))
    return min(tried, key=lambda c: c[0])[1]


def tts(text, voice: dict) -> np.ndarray:
    """Narration for a scene's text as int16 at voice["sample_rate"] (pauses and per-line voices applied)."""
    sr = voice["sample_rate"]
    parts = []
    for item in phrase_plan(text, voice):
        if item[0] == "pause":
            parts.append(np.zeros(round(item[1] * sr), np.float32))
        else:
            # every chunk at the scene's rate, whatever engine/preset made it;
            # a line with its own preset is that voice, not the narrator plus changes
            base = DEFAULTS["voice"] if item[2] and item[2].get("preset") else voice
            v = {**resolve_voice(base, item[2]), "sample_rate": sr}
            chunk = speak_checked(item[1], v, sr)
            if v.get("max_inner_pause"):
                chunk = squeeze_pauses(chunk, sr, v["max_inner_pause"])
            parts.append(trim_silence(chunk, sr) if v.get("trim_chunks") else chunk)
            if v.get("trim_chunks"):
                parts.append(np.zeros(int(sr * v.get("chunk_gap", 0.12)), np.float32))
    out = np.concatenate(parts) if parts else np.zeros(0, np.float32)
    return (np.clip(out, -1, 1) * 32767).astype(np.int16)


# ---------------------------------------------------------------- sound



@lru_cache(maxsize=None)
def audio_meta() -> dict:
    path = ROOT / "assets/audio/meta.json"
    return json.loads(path.read_text()) if path.exists() else {}


def sound_file(name: str) -> Path | None:
    for ext in ("wav", "mp3", "ogg", "m4a", "flac", "aiff"):
        p = ROOT / "assets/audio/sfx" / f"{name}.{ext}"
        if p.exists():
            return p
    return None


@lru_cache(maxsize=None)
def load_sound(name: str, sr: int) -> np.ndarray:
    """Mono float32 samples of a library sound; a short beep if it is not there yet."""
    path = sound_file(name)
    if path is None:
        MISSING.add(f"sound {name}")
        if not CFG["audio"]["placeholder_beep"]:
            return np.zeros(1, np.float32)
        t = np.arange(int(sr * 0.18)) / sr
        beep = 0.15 * np.sin(2 * np.pi * 880 * t) * np.exp(-t * 18)
        return np.concatenate([beep, np.zeros(int(sr * 0.7))]).astype(np.float32)  # gap so loops stay beeps
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-f", "f32le", "-ac", "1", "-ar", str(sr), "-"],
                         check=True, capture_output=True).stdout
    clip = np.frombuffer(raw, np.float32).copy()
    aud = CFG["audio"]
    peak = float(np.abs(clip).max()) if len(clip) else 0.0
    if peak <= 0:
        return clip
    if aud["trim_silence"]:  # cue times mean "the sound starts here", so drop leading silence
        loud = np.flatnonzero(np.abs(clip) > peak * aud["trim_threshold"])
        clip = clip[max(0, loud[0] - int(sr * 0.01)):]
    if aud.get("normalize_db") is not None:
        # generated files differ by 30+ dB: bring the audible part to one loudness,
        # so "volume" in the storyboard means the same thing for every sound
        active = clip[np.abs(clip) > peak * 0.05]
        rms = float(np.sqrt((active ** 2).mean()))
        gain = 10 ** (aud["normalize_db"] / 20) / max(rms, 1e-9)
        gain = min(gain, 0.89 / peak)  # keep peaks under -1 dB
        clip *= gain
    return clip


def place(track: np.ndarray, clip: np.ndarray, start: float, sr: int, gain: float = 1.0,
          length: float | None = None, loop: bool = False, fade_in: float = 0.0, fade_out: float = 0.0):
    """Add clip into track at start seconds (optionally looped / cut to length, with fades)."""
    i0 = max(0, round(start * sr))
    n = round(length * sr) if length else len(clip)
    if loop and len(clip):
        clip = np.tile(clip, n // len(clip) + 1)
    clip = clip[: min(n, len(track) - i0)].astype(np.float32) * gain
    if not len(clip):
        return
    env = np.ones(len(clip), np.float32)
    if fade_in:
        k = min(len(clip), round(fade_in * sr))
        env[:k] = np.linspace(0, 1, k)
    if fade_out:
        k = min(len(clip), round(fade_out * sr))
        env[-k:] = np.minimum(env[-k:], np.linspace(1, 0, k))
    track[i0:i0 + len(clip)] += clip * env


def mix_audio(plan, starts: dict, narr_spans, total: float, sr: int) -> np.ndarray:
    """Narration + scene sfx + story music (ducked under narration), as float -1..1.

    scene "sfx": [{"sound": name, "at": p (0..1 of scene) | "t": seconds, "volume": 1,
                   "loop": false, "length": s, "fade_in": s, "fade_out": s}]
    story "music": [{"sound": name, "from": scene id, "to": scene id (inclusive),
                     "volume": 1, "fade_in": s, "fade_out": s, "duck": true}]
    Volumes multiply settings.audio.*_volume and the sound's default volume in assets/audio/meta.json."""
    aud, timing = CFG["audio"], CFG["timing"]
    n = round(total * sr)
    voice, sfx, music = (np.zeros(n, np.float32) for _ in range(3))
    defaults = audio_meta().get("sounds", {})
    for s, dur, speech in plan:
        t0 = starts[s["id"]]
        if len(speech):
            v = speech.astype(np.float32) / 32768
            src = CFG["voice"]["sample_rate"]
            v = np.interp(np.arange(round(len(v) * sr / src)) * src / sr, np.arange(len(v)), v).astype(np.float32)
            place(voice, v, t0 + timing["lead"], sr, aud["narration_volume"])
        for cue in s.get("sfx", []):
            at = cue["t"] if "t" in cue else cue.get("at", 0) * dur
            gain = cue.get("volume", 1.0) * defaults.get(cue["sound"], {}).get("volume", 1.0) * aud["sfx_volume"]
            place(sfx, load_sound(cue["sound"], sr), t0 + at, sr, gain, cue.get("length"),
                  cue.get("loop", False), cue.get("fade_in", 0), cue.get("fade_out", 0))
    ids = list(starts)
    for m in STORY.get("music", []):
        a = m.get("from", ids[0])
        b = m.get("to", ids[-1])
        in_range = [i for i in ids if float(a) <= float(i) <= float(b)]
        if not in_range:
            continue
        start = starts[in_range[0]]
        last = in_range[-1]
        end = starts[last] + next(d for s, d, _ in plan if s["id"] == last)
        gain = m.get("volume", 1.0) * defaults.get(m["sound"], {}).get("volume", 1.0) * aud["music_volume"]
        tmp = np.zeros(n, np.float32)
        place(tmp, load_sound(m["sound"], sr), start, sr, gain, end - start, m.get("loop", True),
              m.get("fade_in", 1.0), m.get("fade_out", 1.0))
        if m.get("duck", True):
            env = np.ones(n, np.float32)
            for a0, a1 in narr_spans:
                env[round(a0 * sr):round(a1 * sr)] = aud["duck"]
            k = round(0.25 * sr)  # smooth the gain changes
            env = np.convolve(env, np.ones(k) / k, mode="same").astype(np.float32)
            tmp *= env
        music += tmp
    out = voice + sfx + music
    # soft limiter: only the loud peaks above the knee are squeezed (a single
    # jump-scare hit must not turn the whole film down)
    ceil = 10 ** (aud["limiter_ceiling_db"] / 20)  # below 0 dB: AAC encoding overshoots peaks
    knee = ceil * 0.9
    mag = np.abs(out)
    over = mag > knee
    out[over] = np.sign(out[over]) * (knee + (ceil - knee) * np.tanh((mag[over] - knee) / (ceil - knee)))
    return out


# ---------------------------------------------------------------- images

MISSING: set = set()


def placeholder(label: str, w: int, h: int, color=(90, 90, 110)) -> Image.Image:
    """Stand-in for an asset that is requested but not made yet."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((2, 2, w - 3, h - 3), max(4, w // 12), fill=(*color, 150), outline=(230, 230, 240, 220), width=3)
    f = font(max(14, h // 14))
    d.multiline_text((w / 2, h / 2), "\n".join(textwrap.wrap(label.split("/")[-1].replace("_", " "), 12)),
                     font=f, fill=(255, 255, 255), anchor="mm", align="center")
    return im


@lru_cache(maxsize=None)
def background(name: str, w: int, h: int) -> Image.Image:
    if name == "black":
        return Image.new("RGBA", (w, h), (0, 0, 0, 255))
    path = ROOT / "assets/backgrounds" / f"{name}.png"
    if not path.exists():
        MISSING.add(f"background {name}")
        im = Image.new("RGBA", (w, h), (35, 38, 50, 255))
        ImageDraw.Draw(im).text((w / 2, h * 0.12), f"[PHÔNG CHƯA CÓ] {name}", font=font(h // 22),
                                fill=(220, 220, 230), anchor="mm")
        return im
    im = Image.open(ROOT / "assets/backgrounds" / f"{name}.png").convert("RGBA")
    scale = max(w / im.width, h / im.height)  # cover
    im = im.resize((math.ceil(im.width * scale), math.ceil(im.height * scale)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


@lru_cache(maxsize=None)
def sprite_src(name: str, tint: bool, glow: bool) -> Image.Image:
    look = CFG["look"]
    path = ROOT / "assets/characters" / f"{name}.png"
    if not path.exists():
        MISSING.add(f"sprite {name}")
        return placeholder(name, 400, 760)
    im = Image.open(path).convert("RGBA")
    if tint:
        arr = np.asarray(im).astype(np.float32)
        arr[..., :3] *= np.array(look["night_tint"], np.float32)
        im = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    if glow:  # pale rim so dark hair/clothes read against dark rooms
        size = look["glow_size"] | 1
        a = im.getchannel("A").filter(ImageFilter.MaxFilter(size)).filter(ImageFilter.GaussianBlur(size + 1))
        rim = Image.new("RGBA", im.size, (*look["glow_color"], 0))
        rim.putalpha(a.point(lambda v: v * look["glow_strength"]))
        rim.alpha_composite(im)
        im = rim
    return im


@lru_cache(maxsize=512)
def sprite_scaled(name: str, height: int, flip: bool, tint: bool, glow: bool) -> Image.Image:
    im = sprite_src(name, tint, glow)
    im = im.resize((max(1, round(im.width * height / im.height)), height), Image.LANCZOS)
    return im.transpose(Image.FLIP_LEFT_RIGHT) if flip else im


@lru_cache(maxsize=None)
def phone_ui(kind: str, name: str, message: str, height: int, ui_json: str) -> Image.Image:
    """A simple smartphone showing an incoming call or a message.
    Texts come from settings.phone, overridable per layer."""
    ui = json.loads(ui_json)
    W, H = 600, 1200  # drawing canvas; the result is scaled to `height`
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, W, H), 80, fill=(12, 12, 14, 255))
    d.rounded_rectangle((18, 18, W - 18, H - 18), 66, fill=(28, 32, 44, 255))
    d.rounded_rectangle((W // 2 - 70, 34, W // 2 + 70, 62), 14, fill=(8, 8, 10, 255))  # notch
    d.text((60, 90), ui["clock"], font=font(30, True), fill=(230, 230, 235))
    if kind == "call":
        d.text((W // 2, 300), ui["call_label"], font=font(34), fill=(180, 185, 200), anchor="mm")
        d.ellipse((W // 2 - 90, 380, W // 2 + 90, 560), fill=(70, 80, 100))
        d.text((W // 2, 470), name[:1], font=font(90, True), fill=(230, 230, 240), anchor="mm")
        d.text((W // 2, 640), name, font=font(64, True), fill=(250, 250, 255), anchor="mm")
        d.text((W // 2, 710), ui["call_sub"], font=font(30), fill=(150, 155, 170), anchor="mm")
        for cx, col, label in ((150, (220, 60, 60), ui["decline"]), (450, (60, 190, 90), ui["accept"])):
            d.ellipse((cx - 60, 920, cx + 60, 1040), fill=col)
            d.text((cx, 1080), label, font=font(28), fill=(200, 200, 210), anchor="mm")
    else:
        d.rectangle((18, 130, W - 18, 230), fill=(38, 42, 56, 255))
        d.ellipse((50, 145, 120, 215), fill=(70, 80, 100))
        d.text((85, 180), name[:1], font=font(40, True), fill=(230, 230, 240), anchor="mm")
        d.text((140, 180), name, font=font(46, True), fill=(250, 250, 255), anchor="lm")
        lines = textwrap.wrap(message, ui["message_wrap"])
        f = font(50)
        bh = 50 + 66 * len(lines)
        d.rounded_rectangle((40, 300, W - 40, 300 + bh), 34, fill=(58, 64, 82, 255))
        for i, line in enumerate(lines):
            d.text((72, 326 + 66 * i), line, font=f, fill=(245, 245, 250))
        d.text((48, 322 + bh), ui["message_time"], font=font(28), fill=(140, 145, 160))
    glow = Image.new("RGBA", (W + 160, H + 160), (0, 0, 0, 0))
    glow.paste(Image.new("RGBA", (W, H), tuple(ui["glow_color"])), (80, 80), im.getchannel("A"))
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    glow.alpha_composite(im, (80, 80))
    return glow.resize((round(glow.width * height / glow.height), height), Image.LANCZOS)


@lru_cache(maxsize=None)
def vignette(w: int, h: int) -> Image.Image:
    v = CFG["look"]["vignette"]
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    r = np.sqrt(((xx - w / 2) / (w / 2)) ** 2 + ((yy - h / 2) / (h / 2)) ** 2)
    a = np.clip((r - v["start"]) / v["spread"], 0, 1) ** v["power"] * v["max_alpha"]
    out = np.zeros((h, w, 4), np.uint8)
    out[..., 3] = a.astype(np.uint8)
    return Image.fromarray(out)


@lru_cache(maxsize=None)
def circle_mask(w: int, h: int, cx: float, cy: float, r: float) -> Image.Image:
    m = Image.new("L", (w, h), 0)
    R = r * h
    ImageDraw.Draw(m).ellipse((cx * w - R, cy * h - R, cx * w + R, cy * h + R), 255)
    return m.filter(ImageFilter.GaussianBlur(h * 0.01))


# ---------------------------------------------------------------- frame

def lerp(v, p: float):
    if isinstance(v, list):
        return v[0] + (v[1] - v[0]) * p
    return v


def ease(p: float, kind: str | None) -> float:
    if kind == "out":
        return 1 - (1 - p) ** 3
    if kind == "in":
        return p ** 3
    return p * p * (3 - 2 * p) if kind == "smooth" else p


def sprite_meta(name: str) -> dict:
    """Facts about one sprite from assets/characters/<char>/meta.json
    ("sprites".<name>: desc, tags, facing, anchors), overridable in the
    storyboard under characters.<char>.sprites.<name>."""
    char, _, sprite = name.partition("/")
    base = {"facing": "front", "anchors": {}, **load_meta(char).get("sprites", {}).get(sprite, {})}
    return deep_merge(base, CHARACTERS.get(char, {}).get("sprites", {}).get(sprite, {}))


@lru_cache(maxsize=None)
def load_meta(char: str) -> dict:
    path = ROOT / "assets/characters" / char / "meta.json"
    return json.loads(path.read_text()) if path.exists() else {}


@lru_cache(maxsize=None)
def bg_meta(name: str) -> dict:
    path = ROOT / "assets/backgrounds/meta.json"
    data = json.loads(path.read_text()) if path.exists() else {}
    return data.get("backgrounds", {}).get(name, {})


def cycle_frames(ref: str) -> list:
    """"char/cycle" -> ["char/sprite", ...] from meta.json "cycles"."""
    char, _, cyc = ref.partition("/")
    return [f"{char}/{n}" for n in load_meta(char)["cycles"][cyc]]


def hotspot(bg: str, value):
    """A point [x, y] given directly or as the name of a background hotspot."""
    if isinstance(value, str):
        spots = bg_meta(bg).get("hotspots", {})
        if value not in spots:
            MISSING.add(f"hotspot {bg}.{value}")
            return [0.5, 0.5, 0.45]
        return spots[value]
    return value


def camera_at(cam: dict, p: float) -> tuple[float, float, float]:
    """(zoom, focus x, focus y) at scene progress p.
    Keyframes: {"keys": [{"p": 0, "zoom": 1, "x": .5, "y": .5}, {"p": 1, "zoom": 1.4, "x": .3, "ease": "in"}]}
    (a key's "ease" shapes the move that ends on it; missing values carry over).
    Simple form: {"zoom": [from, to], "focus": [x, y] or [[x0, y0], [x1, y1]], "ease": "smooth"}."""
    if "keys" in cam:
        keys, cur = [], {"zoom": 1.0, "x": 0.5, "y": 0.5}
        for k in sorted(cam["keys"], key=lambda k: k.get("p", 0)):
            cur = {**cur, **{n: k[n] for n in ("zoom", "x", "y") if n in k}}
            keys.append((k.get("p", 0), cur, k.get("ease", "smooth")))
        if p <= keys[0][0]:
            v = keys[0][1]
        elif p >= keys[-1][0]:
            v = keys[-1][1]
        else:
            for (p0, a, _), (p1, b, e) in zip(keys, keys[1:]):
                if p0 <= p <= p1:
                    q = ease((p - p0) / max(1e-6, p1 - p0), e)
                    v = {n: a[n] + (b[n] - a[n]) * q for n in a}
                    break
        return v["zoom"], v["x"], v["y"]
    q = ease(p, cam.get("ease", "smooth"))
    focus = cam.get("focus", [0.5, 0.5])
    if isinstance(focus[0], list):
        fx, fy = lerp([focus[0][0], focus[1][0]], q), lerp([focus[0][1], focus[1][1]], q)
    else:
        fx, fy = focus
    return lerp(cam.get("zoom", 1.0), q), fx, fy


def resolve_layer(layer: dict, bg: str) -> dict:
    """settings.layer < meta default_h < characters[<folder>] < layer.
    "cycle" expands to frames; "y": "floor" uses the background's floor_y."""
    layer = dict(layer)
    if "cycle" in layer:
        layer["frames"] = cycle_frames(layer["cycle"])
    first = layer.get("sprite") or (layer.get("frames") or [""])[0]
    first = first if isinstance(first, str) else first["sprite"]
    char = first.split("/")[0] if "/" in first else None
    defaults = {k: v for k, v in CHARACTERS.get(char, {}).items() if k != "sprites"}
    meta_h = {"h": load_meta(char)["default_h"]} if char and "default_h" in load_meta(char) else {}
    out = {**CFG["layer"], **meta_h, **defaults, **layer}
    if out.get("y") == "floor":
        out["y"] = bg_meta(bg).get("floor_y", CFG["layer"]["y"])
    return out


def wants_flip(layer: dict, name: str, frame_flip: bool) -> bool:
    """Explicit "flip" wins; otherwise "face" (left/right/auto) is compared with
    the sprite's own facing. "auto" faces the direction the layer moves in x."""
    if "flip" in layer and layer["flip"] is not None:
        return bool(layer["flip"]) != frame_flip
    face = layer.get("face")
    if face == "auto":
        xs = layer.get("x")
        face = ("right" if xs[1] > xs[0] else "left") if isinstance(xs, list) else None
    native = sprite_meta(name)["facing"]
    flip = face in ("left", "right") and native in ("left", "right") and face != native
    return flip != frame_flip


def draw_layer(canvas: Image.Image, layer: dict, p: float, t: float, rng: random.Random, bg: str = ""):
    """Layer keys: sprite | frames+fps | ui ("call"/"message", name, message,
    plus any settings.phone key), x, y (feet baseline, 0..1), h (height, 0..1 of
    frame), flip, start/end (0..1 of scene), bob (px@1080p), jitter (px@1080p),
    tint, glow, clip_circle [cx, cy, r], ease ("in"/"out"/"smooth"),
    face ("left"/"right"/"auto": flip to face that way, using the sprite's
    facing from meta.json), pin {"point": anchor, "at": [x, y]} (place the
    sprite so that anchor lands on a point of the frame, overrides x/y),
    breathe (idle scale amplitude, e.g. 0.008).
    A frame in "frames" may be "char/sprite" or {"sprite": ..., "flip": true}.
    "cycle": "char/name" = frames from meta.json cycles. "y": "floor" = the
    background's floor_y. pin.at and clip_circle may name a background hotspot.
    Missing sprites render as a labelled placeholder (see asset_requests)."""
    layer = resolve_layer(layer, bg)
    start, end = layer.get("start", 0.0), layer.get("end", 1.0)
    if not (start <= p < end or (p >= 1 and end >= 1)):
        return
    lp = ease(min(1.0, (p - start) / max(1e-6, end - start)), layer.get("ease"))
    W, H = canvas.size
    h = lerp(layer["h"], lp) * H
    if layer.get("breathe"):
        h *= 1 + layer["breathe"] * math.sin(t * 2 * math.pi * CFG["look"]["breathe_hz"])
    h = round(h)
    anchor = None
    if "ui" in layer:
        ui = {k: layer.get(k, v) for k, v in CFG["phone"].items()}
        im = phone_ui(layer["ui"], layer.get("name", ""), layer.get("message", ""), h,
                      json.dumps(ui, sort_keys=True, ensure_ascii=False))
    else:
        name, frame_flip = layer.get("sprite"), False
        if "frames" in layer:
            frames = layer["frames"]
            frame = frames[int(t * layer["fps"]) % len(frames)]
            name, frame_flip = (frame, False) if isinstance(frame, str) else (frame["sprite"], frame.get("flip", False))
        flip = wants_flip(layer, name, frame_flip)
        im = sprite_scaled(name, h, flip, layer["tint"], layer["glow"])
        point = sprite_meta(name)["anchors"].get(layer["pin"]["point"]) if layer.get("pin") else None
        if point:
            ax, ay = point
            anchor = ((1 - ax) if flip else ax, ay)
        elif layer.get("pin"):  # placeholder or unmeasured sprite: centre it on the point
            anchor = (0.5, 0.5)
    if anchor:
        px, py = hotspot(bg, layer["pin"]["at"])[:2]
        x = px * W - anchor[0] * im.width
        y = py * H - anchor[1] * im.height
    else:
        x = lerp(layer["x"], lp) * W - im.width / 2
        y = lerp(layer["y"], lp) * H - im.height
    if layer.get("bob"):
        y -= abs(math.sin(t * 2 * math.pi * CFG["look"]["bob_hz"])) * layer["bob"] * H / 1080
    if layer.get("jitter"):
        j = layer["jitter"] * H / 1080
        x += rng.uniform(-j, j)
        y += rng.uniform(-j, j)
    if "clip_circle" in layer:
        layer["clip_circle"] = hotspot(bg, layer["clip_circle"])
        tmp = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        tmp.paste(im, (round(x), round(y)), im)
        mask = circle_mask(W, H, *layer["clip_circle"])
        a = np.minimum(np.asarray(tmp.getchannel("A")), np.asarray(mask))
        tmp.putalpha(Image.fromarray(a))
        canvas.alpha_composite(tmp)
    else:
        canvas.paste(im, (round(x), round(y)), im)


def subtitle_parts(text: str, min_chars: int, max_chars: int = 96) -> list[str]:
    """Sentences, long ones cut at commas so each part fits two subtitle lines."""
    parts = []
    for sent in (p for p in re.split(r"(?<=[.!?…:])\s+", text) if p.strip()):
        cur = ""
        for piece in re.split(r"(?<=,)\s+", sent):
            if cur and len(cur) + 1 + len(piece) > max_chars:
                parts.append(cur)
                cur = piece
            else:
                cur = f"{cur} {piece}".strip()
        parts.append(cur)
    merged = []
    for p in parts:
        if merged and len(merged[-1]) < min_chars:
            merged[-1] += " " + p
        else:
            merged.append(p)
    return merged


def subtitle_at(scene: dict, t: float) -> str:
    """The subtitle shown at time t: with split "sentence", each sentence stays up for
    its share (by length) of the time the narration speaks."""
    text = spoken_text(scene["text"])
    sub = CFG["subtitles"]
    if sub.get("split", "none") != "sentence" or "_speech" not in scene:
        return text
    parts = subtitle_parts(text, sub.get("min_chars", 18), sub["wrap"] * 2)
    start, length = scene["_speech"]
    q = min(max((t - start) / max(length, 1e-6), 0), 0.9999) * sum(len(p) for p in parts)
    for p in parts:
        if q < len(p):
            return p
        q -= len(p)
    return parts[-1]


def subtitle(canvas: Image.Image, text: str):
    sub = CFG["subtitles"]
    W, H = canvas.size
    f = font(round(H * sub["size"]))
    lines = textwrap.wrap(text, sub["wrap"])
    d = ImageDraw.Draw(canvas)
    lh = round(H * sub["line_height"])
    y0 = H - round(H * sub["bottom"]) - lh * len(lines)
    for i, line in enumerate(lines):
        d.text((W / 2, y0 + i * lh), line, font=f, fill=tuple(sub["color"]), anchor="mt",
               stroke_width=max(2, H // 300), stroke_fill=tuple(sub["stroke"]))


def render_frame(scene: dict, t: float, dur: float, size: tuple[int, int], rng: random.Random) -> Image.Image:
    W, H = size
    look, timing = CFG["look"], CFG["timing"]
    p = t / dur if dur else 0
    canvas = background(scene["bg"], W, H).copy()
    if scene.get("bg_dim"):
        canvas.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, round(255 * scene["bg_dim"]))))
    for layer in scene.get("layers", []):
        draw_layer(canvas, layer, p, t, rng, scene["bg"])

    cam = scene.get("camera")
    if cam:
        z, fx, fy = camera_at(cam, p)
        if cam.get("handheld"):  # slow drifting sway, like a phone in a shaking hand
            a = cam["handheld"] / 1000
            fx += a * (math.sin(t * 1.3) + 0.5 * math.sin(t * 3.1 + 1))
            fy += a * (math.sin(t * 1.7 + 2) + 0.5 * math.sin(t * 2.6))
            z = max(z, 1 + 2.5 * a)  # keep the frame covered while swaying
        cw, ch = W / z, H / z
        x0 = min(max(fx * W - cw / 2, 0), W - cw)
        y0 = min(max(fy * H - ch / 2, 0), H - ch)
        canvas = canvas.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))

    sh = scene.get("shake")
    if sh and sh.get("from", 0) <= p <= sh.get("to", 1):
        a = sh["amp"] * H / 1080
        dx, dy = rng.uniform(-a, a), rng.uniform(-a, a)
        canvas = canvas.transform((W, H), Image.AFFINE, (1, 0, dx, 0, 1, dy), Image.BICUBIC)

    canvas.alpha_composite(vignette(W, H))
    if scene.get("flicker") and rng.random() < scene["flicker"]:
        canvas.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, rng.randint(60, 140))))
    fl = look["flash"]
    for fp in scene.get("flash", []):
        dt = t - fp * dur
        if 0 <= dt < fl["length"]:
            alpha = round(fl["max_alpha"] * (1 - dt / fl["length"]))
            canvas.alpha_composite(Image.new("RGBA", (W, H), (255, 255, 255, alpha)))

    if scene.get("title_text"):
        ti = CFG["title"]
        ImageDraw.Draw(canvas).text((W / 2, H / 2), scene["title_text"], font=font(round(H * ti["size"]), True),
                                    fill=tuple(ti["color"]), anchor="mm")
    elif scene.get("text") and CFG["subtitles"]["enabled"]:
        subtitle(canvas, subtitle_at(scene, t))

    fi = scene.get("fade_in", timing["fade_in"])
    fo = scene.get("fade_out", timing["fade_out"])
    k = 1.0
    if fi and t < fi:
        k = t / fi
    if fo and t > dur - fo:
        k = min(k, (dur - t) / fo)
    if k < 1:
        canvas.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, round(255 * (1 - k)))))
    return canvas.convert("RGB")


# ---------------------------------------------------------------- main

def main():
    global CFG, CHARACTERS, STORY
    ap = argparse.ArgumentParser()
    ap.add_argument("story")
    ap.add_argument("--preview", action="store_true", help="use settings.preview size/fps")
    ap.add_argument("--scenes", help="e.g. 16-19 or 5")
    ap.add_argument("--no-subtitles", action="store_true")
    ap.add_argument("-o", "--output")
    args = ap.parse_args()

    story = json.loads(Path(args.story).read_text())
    CFG = deep_merge(DEFAULTS, story.get("settings", {}))
    if "voice" in story:  # older storyboards kept the voice at top level
        CFG["voice"] = deep_merge(CFG["voice"], story["voice"])
    if args.no_subtitles:
        CFG["subtitles"]["enabled"] = False
    CHARACTERS = story.get("characters", {})
    STORY = story

    scenes = story["scenes"]
    if args.scenes:
        a, _, b = args.scenes.partition("-")
        lo, hi = float(a), float(b or a)
        scenes = [s for s in scenes if lo <= s["id"] <= hi]
    video = deep_merge(CFG["video"], CFG["preview"]) if args.preview else CFG["video"]
    size, fps = tuple(video["size"]), video["fps"]
    out = Path(args.output or story["output"])
    if args.preview and not args.output:
        out = out.with_name(out.stem + "_preview.mp4")
    out = ROOT / out if not out.is_absolute() else out
    out.parent.mkdir(parents=True, exist_ok=True)

    # narration first: it decides each scene's length
    voice, timing, aud = CFG["voice"], CFG["timing"], CFG["audio"]
    sr = aud["sample_rate"]
    plan, starts, t0 = [], {}, 0.0
    narr_spans = []  # (start, end) seconds where narration speaks, for music ducking
    for s in scenes:
        sv = narration_voice(s.get("voice"))
        speech = tts(s["text"], sv) if s.get("text") else np.zeros(0, np.int16)
        speech_len = len(speech) / voice["sample_rate"]
        dur = s.get("duration") or max(s.get("min_duration", timing["min_duration"]),
                                       timing["lead"] + speech_len + timing["tail"])
        plan.append((s, dur, speech))
        s["_speech"] = (timing["lead"], speech_len)  # for sentence-by-sentence subtitles
        starts[s["id"]] = t0
        if len(speech):
            narr_spans.append((t0 + timing["lead"], t0 + timing["lead"] + speech_len))
        t0 += dur
    total = t0
    mix = mix_audio(plan, starts, narr_spans, total, sr)
    wav_path = out.with_suffix(".wav")
    with wave.open(str(wav_path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((mix * 32767).astype(np.int16).tobytes())
    plan = [(s, d) for s, d, _ in plan]

    total = sum(d for _, d in plan)
    print(f"{len(plan)} scenes, {total:.1f}s, {size[0]}x{size[1]}@{fps} -> {out}", flush=True)
    ff = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{size[0]}x{size[1]}", "-r", str(fps), "-i", "-",
         "-i", str(wav_path),
         "-c:v", "libx264", "-preset", video["preset"], "-crf", str(video.get("crf", 20)),
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-shortest", str(out)],
        stdin=subprocess.PIPE)
    total_frames, done = sum(round(d * fps) for _, d in plan), 0
    for s, dur in plan:
        rng = random.Random(str(s["id"]))
        for i in range(round(dur * fps)):
            ff.stdin.write(render_frame(s, i / fps, dur, size, rng).tobytes())
            done += 1
            if done % fps == 0:  # machine-readable, for the Studio progress bar
                print(f"progress {done}/{total_frames}", flush=True)
        print(f"  scene {s['id']:>4}  {dur:5.1f}s", flush=True)
    ff.stdin.close()
    ff.wait()
    wav_path.unlink()
    for m in sorted(MISSING):
        print("  placeholder (chưa có asset):", m)
    print("done:", out)


if __name__ == "__main__":
    main()
