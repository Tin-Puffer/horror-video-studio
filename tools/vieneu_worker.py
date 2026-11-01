#!/usr/bin/env python3
"""VieNeu-TTS worker, run with the Python that has `vieneu` + the Dubber package.

Speaks JSON lines on stdin/stdout so the model (~1.6 GB) loads once per render:
  {"cmd": "say", "text": "...", "voice": "preset:Hải Đăng" | "clone:<id>", "out": "/path.wav",
   "temperature": 0.4, "top_k": 50}  (optional sampling settings, SDK defaults when left out)
  {"cmd": "clone", "audio": "/path", "name": "Tên", "start": 0.0}
  {"cmd": "list"}
Each request gets one reply line: {"ok": true, ...} or {"ok": false, "error": "..."}.
Cloned voices live in Dubber's voice library, so Dubber sees them too; a clone that
is not there is read from the project's assets/voices/vieneu/<id>/ (argv[2] = project root).
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

    project_voices = Path(sys.argv[2]) / "assets/voices/vieneu" if len(sys.argv) > 2 else None

    def resolve(spec: str):
        if spec not in voices:
            kind, _, name = spec.partition(":")
            if kind != "clone":
                voices[spec] = name
            elif lib.clone_exists(name) or project_voices is None:
                voices[spec] = lib.load_voice_data(name)
            else:  # shipped with the project (assets/voices/vieneu/<id>/voice.json)
                voices[spec] = lib.load_voice_data(name, root=project_voices)
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
                    opts = {k: req[k] for k in ("temperature", "top_k") if req.get(k) is not None}
                    audio = sdk.infer(clean_text(req["text"]), voice=resolve(req["voice"]), **opts)
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
