#!/usr/bin/env python3
"""Check that this machine can render: python libs, ffmpeg, fonts, voices.

  python3 tools/doctor.py

Prints one line per check with what to do when it fails. Run it first on a new machine.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
problems = 0


def check(ok: bool, what: str, fix: str = ""):
    global problems
    print(("  OK   " if ok else "  THIẾU ") + what + ("" if ok else f"\n         → {fix}"))
    problems += not ok


def main():
    print("Horror Video Studio — kiểm tra máy")
    check(sys.version_info >= (3, 9), f"Python {sys.version.split()[0]}", "cài Python 3.9+")
    for mod in ("PIL", "numpy"):
        try:
            __import__(mod)
            check(True, f"thư viện {mod}")
        except ImportError:
            check(False, f"thư viện {mod}", "pip install -r requirements.txt")
    check(shutil.which("ffmpeg") is not None, "ffmpeg", "macOS: brew install ffmpeg · Windows: winget install ffmpeg")

    import render
    v = render.DEFAULTS["voice"]
    check((ROOT / "config.local.json").exists(), "config.local.json",
          "tạo file theo README (đường dẫn piper / VieNeu / font của máy này)")
    for key in ("regular", "bold"):
        check(Path(render.DEFAULTS["fonts"][key]).exists(), f"font {key}: {render.DEFAULTS['fonts'][key]}",
              'đặt "fonts" trong config.local.json tới font có dấu tiếng Việt (vd Arial)')

    # narrator voice of the template
    tpl = json.loads((ROOT / "templates/kich_ban_mau.json").read_text())
    render.STORY = tpl
    narr = render.resolve_voice(render.DEFAULTS["voice"], tpl["settings"]["voice"])
    print(f"  ..   giọng kể của mẫu: {tpl['settings']['voice'].get('preset')} (engine {narr.get('engine')})")
    if narr.get("engine") == "vieneu":
        py, dub = narr.get("vieneu_python"), narr.get("dubber_root")
        check(bool(dub) and Path(dub, "dubber").is_dir(), f"Dubber ở {dub!r}",
              'cài Dubber, đặt "dubber_root" trong config.local.json')
        r = subprocess.run([py or "python3", "-c", "import vieneu"], capture_output=True)
        check(r.returncode == 0, f"VieNeu-TTS trong {py!r}",
              'trong Dubber: pip install -e ".[vieneu]" rồi đặt "vieneu_python" = Python đó')
        if r.returncode == 0 and dub:
            try:
                x = render.tts_chunk("Kiểm tra giọng đọc.", {**narr, "sample_rate": 44100})
                check(len(x) > 4410, "đọc thử bằng giọng kể (VieNeu)")
            except Exception as e:  # report, keep checking
                check(False, "đọc thử bằng giọng kể (VieNeu)", str(e)[:200])
    else:
        check(shutil.which(narr.get("piper", "piper")) is not None or Path(narr.get("piper", "")).exists(),
              f"piper ({narr.get('piper')})", "pip install piper-tts, tải giọng vào voices/")

    sounds = list((ROOT / "assets/audio/sfx").glob("*.*"))
    check(len(sounds) > 0, f"{len(sounds)} âm thanh trong kho")
    print("Xong:", "máy sẵn sàng dựng video." if not problems else f"{problems} mục cần xử lý.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
