#!/usr/bin/env python3
"""VieNeu-TTS worker, run with the Python that has `vieneu` + the Dubber package.

Speaks JSON lines on stdin/stdout so the model (~1.6 GB) loads once per render:
  {"cmd": "say", "text": "...", "voice": "preset:Hải Đăng" | "clone:<id>", "out": "/path.wav"}
  {"cmd": "clone", "audio": "/path", "name": "Tên", "start": 0.0}
  {"cmd": "list"}
Each request gets one reply line: {"ok": true, ...} or {"ok": false, "error": "..."}.
Cloned voices live in Dubber's voice library, so Dubber sees them too.
"""
import json
import sys
from pathlib import Path


def main():
    sys.path.insert(0, sys.argv[1])  # Dubber project root
    from dubber.core.tts import voice_library as lib
    from dubber.core.tts.vieneu_tts import clean_text, shared_vieneu, write_wav

    sdk = None
    voices = {}

    def resolve(spec: str):
        if spec not in voices:
            kind, _, name = spec.partition(":")
            voices[spec] = lib.load_voice_data(name) if kind == "clone" else name
        return voices[spec]

    out = sys.stdout
    sys.stdout = sys.stderr  # keep library prints off the reply channel
    for line in sys.stdin:
        try:
            req = json.loads(line)
            if req["cmd"] == "list":
                reply = {"voices": [{"id": v.id, "name": v.name, "kind": v.kind} for v in lib.list_voices()]}
            else:
                sdk = sdk or shared_vieneu()
                if req["cmd"] == "say":
                    audio = sdk.infer(clean_text(req["text"]), voice=resolve(req["voice"]))
                    write_wav(Path(req["out"]), audio, sdk.sample_rate)
                    reply = {"sample_rate": sdk.sample_rate}
                elif req["cmd"] == "clone":
                    entry = lib.add_clone(Path(req["audio"]), req["name"], sdk, float(req.get("start", 0)))
                    reply = {"id": entry.id, "name": entry.name}
                else:
                    raise ValueError(f"unknown cmd {req['cmd']}")
            out.write(json.dumps({"ok": True, **reply}, ensure_ascii=False) + "\n")
        except Exception as e:  # report and keep serving
            out.write(json.dumps({"ok": False, "error": f"{type(e).__name__}: {e}"}, ensure_ascii=False) + "\n")
        out.flush()


if __name__ == "__main__":
    main()
