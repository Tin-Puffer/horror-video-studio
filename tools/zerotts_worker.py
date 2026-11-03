#!/usr/bin/env python3
"""ZeroTTS worker, run with the Python that has `zerotts` ("zerotts_python" in config.local.json).

Speaks JSON lines on stdin/stdout so the model (~900 MB, ONNX) loads once per render:
  {"cmd": "say", "text": "...", "voice": "duytu", "out": "/path.wav", "cfg_scale": 1.0}
"voice" is a pack in the project's assets/voices/zerotts/<name>/ (voice.npz from a zeroweight.ai
voice zip) or one of the model's built-in voices (huuduc, giahuy, kimoanh, ...).
Each request gets one reply line: {"ok": true, ...} or {"ok": false, "error": "..."}.
"""
import json
import sys
from pathlib import Path


def main():
    project_voices = Path(sys.argv[1]) / "assets/voices/zerotts"
    out = sys.stdout
    sys.stdout = sys.stderr  # keep library prints off the reply channel
    import numpy as np
    from zerotts import ZeroTTS, normalize_vi_text
    from zerotts.voices import load_voice_dir

    tts, voices = None, {}

    def resolve(name: str):
        if name not in voices:
            pack = project_voices / name
            voices[name] = load_voice_dir(pack, name) if (pack / "voice.npz").exists() else name
        return voices[name]

    for line in sys.stdin:
        try:
            req = json.loads(line)
            if req["cmd"] != "say":
                raise ValueError(f"unknown cmd {req['cmd']}")
            tts = tts or ZeroTTS.from_pretrained("zeroweight-ai/ZeroTTS")
            opts = {k: req[k] for k in ("cfg_scale",) if req.get(k) is not None}
            audio = tts.synthesize(normalize_vi_text(req["text"]), voice=resolve(req["voice"]), **opts)
            tts.save_audio(np.asarray(audio), req["out"])
            out.write(json.dumps({"ok": True, "sample_rate": tts.sample_rate}) + "\n")
        except Exception as e:  # report and keep serving
            out.write(json.dumps({"ok": False, "error": f"{type(e).__name__}: {e}"}, ensure_ascii=False) + "\n")
        out.flush()


if __name__ == "__main__":
    main()
