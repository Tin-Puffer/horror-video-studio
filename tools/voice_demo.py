#!/usr/bin/env python3
"""Voice demos: the same short passage read with each voice preset / combination.

  python3 tools/voice_demo.py                 # all demos -> build/voice_demos/*.mp3
  python3 tools/voice_demo.py ke_chuyen_tram  # only demos whose name contains this

Demos are defined in assets/audio/voice_demos.json (passage + per-role presets),
so new combinations are added there, not here.
"""
from __future__ import annotations

import json
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import render  # noqa: E402


def main():
    cfg = json.loads((ROOT / "assets/audio/voice_demos.json").read_text())
    only = sys.argv[1:]
    out_dir = ROOT / "build/voice_demos"
    out_dir.mkdir(parents=True, exist_ok=True)
    base = render.DEFAULTS["voice"]
    sr = base["sample_rate"]
    for demo in cfg["demos"]:
        if only and not any(o in demo["name"] for o in only):
            continue
        roles = demo["roles"]
        parts = []
        for line in cfg[demo.get("passage", "passage")]:
            # "override" applies to the narrator / Khoa only; other roles keep their preset as is
            over = demo.get("override") if line["role"] in ("narrator", "khoa") else None
            voice = {**render.resolve_voice(base, {"preset": roles[line["role"]]}, over), "sample_rate": sr}
            parts.append(render.tts(line["text"], voice).astype(np.float32) / 32768)
            parts.append(np.zeros(int(sr * line.get("after", 0.5)), np.float32))
        audio = np.concatenate(parts)
        wav = out_dir / f"{demo['name']}.wav"
        with wave.open(str(wav), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(sr)
            w.writeframes((np.clip(audio, -1, 1) * 32767).astype(np.int16).tobytes())
        mp3 = wav.with_suffix(".mp3")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(wav), "-b:a", "160k", str(mp3)], check=True)
        wav.unlink()
        print(f"  {mp3.name:28s} {len(audio) / sr:5.1f}s  {demo['desc']}")


if __name__ == "__main__":
    main()
