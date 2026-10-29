#!/usr/bin/env python3
"""Clone a voice from a recording and register it as a named voice preset.

  python3 tools/clone_voice.py <audio file> <tên giọng> [--start 12.5] [--preset ten_preset]

Uses 3–8 s of the file from --start (pick a clean stretch: one speaker, no music).
The clone is stored in Dubber's VieNeu voice library and added to
assets/audio/voice_presets.json, so storyboards use it as {"preset": "<ten_preset>"}.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import render  # noqa: E402


def slug(name: str) -> str:
    s = unicodedata.normalize("NFKD", name.replace("đ", "d").replace("Đ", "D")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_") or "giong_clone"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("name")
    ap.add_argument("--start", type=float, default=0.0)
    ap.add_argument("--preset")
    a = ap.parse_args()
    v = render.DEFAULTS["voice"]
    reply = render.vieneu({"cmd": "clone", "audio": str(Path(a.audio).resolve()), "name": a.name, "start": a.start}, v)
    preset = a.preset or slug(a.name)
    path = ROOT / "assets/audio/voice_presets.json"
    data = json.loads(path.read_text())
    data["presets"][preset] = {"desc": f"Giọng clone: {a.name}", "engine": "vieneu",
                               "vieneu_voice": reply["id"], "sample_rate": 44100}
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False))
    print(f"đã clone '{a.name}' → {reply['id']}  (preset: {preset})")


if __name__ == "__main__":
    main()
