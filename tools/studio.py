#!/usr/bin/env python3
"""Horror Video Studio — local web editor for storyboards.

  python3 tools/studio.py            # opens http://localhost:8765

Edits scripts/*.json, previews any frame with the real renderer, checks the
story against the asset library, and runs renders. Standard library only.
"""
from __future__ import annotations

import io
import json
import mimetypes
import os
import random
import re
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import render  # noqa: E402

PORT = 8765
PREVIEW_SIZE = (960, 540)
SERVE_DIRS = ("assets", "build")
RENDER_LOCK = threading.Lock()  # render.py keeps its config in module globals
JOBS: dict[str, dict] = {}


# ---------------------------------------------------------------- helpers

def story_path(name: str) -> Path:
    if not re.fullmatch(r"[\w\-]+\.json", name):
        raise ValueError("tên kịch bản không hợp lệ")
    return ROOT / "scripts" / name


def catalog() -> dict:
    chars = {}
    for d in sorted(p for p in (ROOT / "assets/characters").iterdir() if p.is_dir()):
        meta = render.load_meta.__wrapped__(d.name)
        files = sorted(p.stem for p in d.glob("*.png"))
        chars[d.name] = {
            "name": meta.get("name", d.name), "default_h": meta.get("default_h"),
            "cycles": meta.get("cycles", {}),
            "sprites": {f: meta.get("sprites", {}).get(f, {"desc": "(chưa mô tả)", "tags": [], "facing": "front"})
                        for f in files}}
    bg_meta = json.loads((ROOT / "assets/backgrounds/meta.json").read_text())
    bgs = {p.stem: bg_meta.get("backgrounds", {}).get(p.stem, {"desc": "(chưa mô tả)", "hotspots": {}})
           for p in sorted((ROOT / "assets/backgrounds").glob("*.png"))}
    ameta_path = ROOT / "assets/audio/meta.json"
    ameta = json.loads(ameta_path.read_text()).get("sounds", {}) if ameta_path.exists() else {}
    sounds = {}
    for f in sorted((ROOT / "assets/audio/sfx").glob("*.*")) if (ROOT / "assets/audio/sfx").exists() else []:
        sounds[f.stem] = {**ameta.get(f.stem, {"desc": "(chưa mô tả)"}), "url": f"/files/assets/audio/sfx/{f.name}"}
    vp = ROOT / "assets/audio/voice_presets.json"
    presets = json.loads(vp.read_text()).get("presets", {}) if vp.exists() else {}
    return {"characters": chars, "backgrounds": bgs, "sounds": sounds, "voice_presets": presets}


def configure(story: dict):
    """Point render.py's globals at this story's settings (caches reset when they change)."""
    cfg = render.deep_merge(render.DEFAULTS, story.get("settings", {}))
    if "voice" in story:
        cfg["voice"] = render.deep_merge(cfg["voice"], story["voice"])
    chars = story.get("characters", {})
    render.STORY = story  # story-level voice_presets / music
    if cfg != render.CFG or chars != render.CHARACTERS:
        render.CFG, render.CHARACTERS = cfg, chars
        for fn in (render.font, render.sprite_src, render.sprite_scaled, render.phone_ui, render.vignette):
            fn.cache_clear()
    render.load_meta.cache_clear()  # meta.json may change after ingest
    render.library_presets.cache_clear()
    render.bg_meta.cache_clear()


def scene_duration(scene: dict) -> float:
    timing = render.CFG["timing"]
    if scene.get("duration"):
        return scene["duration"]
    voice = render.narration_voice(scene.get("voice"))
    speech = render.tts(scene["text"], voice) if scene.get("text") else []
    return max(scene.get("min_duration", timing["min_duration"]),
               timing["lead"] + len(speech) / render.CFG["voice"]["sample_rate"] + timing["tail"])


def frame_png(story: dict, index: int, p: float) -> tuple[bytes, float]:
    with RENDER_LOCK:
        configure(story)
        scene = story["scenes"][index]
        dur = scene_duration(scene)
        # seeded per scene like render.py, so shake/jitter look the same
        rng = random.Random(str(scene["id"]))
        img = render.render_frame(scene, p * dur, dur, PREVIEW_SIZE, rng)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=85)
    return buf.getvalue(), dur


def start_job(args: list[str], label: str) -> str:
    """Run a tool in the background; the same command never runs twice at once."""
    cmd = " ".join(args)
    for job in JOBS.values():
        if job["cmd"] == cmd and not job["done"]:
            return job["id"]
    job_id = str(int(time.time() * 1000))
    job = {"id": job_id, "cmd": cmd, "label": label, "log": [], "done": False, "ok": None,
           "output": None, "progress": 0.0, "started": time.time()}
    JOBS[job_id] = job

    def run():
        env = {**os.environ, "PYTHONUNBUFFERED": "1"}  # lines must arrive as they are printed
        proc = subprocess.Popen([sys.executable, "-W", "ignore", *args], cwd=ROOT, env=env,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in proc.stdout:
            line = line.rstrip()
            m = re.match(r"progress (\d+)/(\d+)", line)
            if m:
                job["progress"] = int(m.group(1)) / int(m.group(2))
                continue
            job["log"].append(line)
            m = re.search(r"-> (\S+\.mp4)", line) or re.search(r"done: (\S+\.mp4)", line)
            if m:
                job["output"] = str(Path(m.group(1)).resolve().relative_to(ROOT))
        job["ok"] = proc.wait() == 0
        if job["ok"]:
            job["progress"] = 1.0
        job["done"] = True
    threading.Thread(target=run, daemon=True).start()
    return job_id


# ---------------------------------------------------------------- http

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def send(self, body: bytes, ctype: str, status=HTTPStatus.OK, headers=None):
        self.send_response(status)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(body)

    def send_json(self, data, status=HTTPStatus.OK):
        self.send(json.dumps(data, ensure_ascii=False).encode(), "application/json; charset=utf-8", status)

    def body_json(self):
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def serve_file(self, rel: str):
        path = (ROOT / rel).resolve()
        if not any(path.is_relative_to(ROOT / d) for d in SERVE_DIRS) or not path.is_file():
            return self.send_json({"error": "not found"}, HTTPStatus.NOT_FOUND)
        ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        size = path.stat().st_size
        rng = self.headers.get("Range")
        if rng:  # video seeking
            m = re.match(r"bytes=(\d*)-(\d*)", rng)
            start = int(m.group(1) or 0)
            end = int(m.group(2)) if m.group(2) else size - 1
            with open(path, "rb") as f:
                f.seek(start)
                data = f.read(end - start + 1)
            return self.send(data, ctype, HTTPStatus.PARTIAL_CONTENT,
                             {"Content-Range": f"bytes {start}-{end}/{size}", "Accept-Ranges": "bytes"})
        self.send(path.read_bytes(), ctype, headers={"Accept-Ranges": "bytes"})

    def do_GET(self):
        url = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        try:
            if url.path == "/":
                return self.send((ROOT / "tools/studio.html").read_bytes(), "text/html; charset=utf-8")
            if url.path.startswith("/files/"):
                return self.serve_file(unquote(url.path[len("/files/"):]))
            if url.path == "/api/stories":
                return self.send_json(sorted(p.name for p in (ROOT / "scripts").glob("*.json")))
            if url.path == "/api/story":
                return self.send_json(json.loads(story_path(q["name"]).read_text()))
            if url.path == "/api/catalog":
                return self.send_json(catalog())
            if url.path == "/api/job":
                return self.send_json(JOBS[q["id"]])
            if url.path == "/api/jobs":  # running first, then the latest finished ones
                jobs = sorted(JOBS.values(), key=lambda j: (j["done"], -j["started"]))
                return self.send_json(jobs[:5])
            self.send_json({"error": "not found"}, HTTPStatus.NOT_FOUND)
        except Exception as e:  # report to the UI instead of dropping the connection
            self.send_json({"error": f"{type(e).__name__}: {e}"}, HTTPStatus.INTERNAL_SERVER_ERROR)

    def do_POST(self):
        url = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        try:
            if url.path == "/api/story":  # save, keeping a backup of the previous version
                path = story_path(q["name"])
                data = self.body_json()
                if path.exists():
                    bdir = ROOT / "build/backups"
                    bdir.mkdir(parents=True, exist_ok=True)
                    shutil.copy(path, bdir / f"{path.stem}.{time.strftime('%Y%m%d-%H%M%S')}.json")
                path.write_text(json.dumps(data, indent=1, ensure_ascii=False))
                return self.send_json({"ok": True})
            if url.path == "/api/frame":
                data = self.body_json()
                png, dur = frame_png(data["story"], int(data["index"]), float(data["p"]))
                return self.send(png, "image/jpeg", headers={"X-Duration": f"{dur:.2f}"})
            if url.path == "/api/check":
                path = story_path(q["name"])
                res = subprocess.run([sys.executable, "tools/check_story.py", str(path)], cwd=ROOT,
                                     capture_output=True, text=True)
                req = ROOT / "build" / f"{path.stem}_requests.md"
                return self.send_json({"ok": res.returncode == 0, "log": res.stdout + res.stderr,
                                       "requests": req.read_text() if req.exists() else ""})
            if url.path == "/api/render":
                args = ["tools/render.py", str(story_path(q["name"]))]
                label = f"{q['name']} — " + ("cảnh " + q["scenes"] if q.get("scenes") else
                                             "bản nháp" if q.get("preview") == "1" else "Full HD")
                if q.get("preview") == "1":
                    args.append("--preview")
                if q.get("scenes"):  # own file, so the full preview is not overwritten
                    args += ["--scenes", q["scenes"],
                             "-o", f"build/{story_path(q['name']).stem}_scene_{q['scenes']}.mp4"]
                return self.send_json({"job": start_job(args, label)})
            if url.path == "/api/catalog/rebuild":
                res = subprocess.run([sys.executable, "-W", "ignore", "tools/catalog.py"], cwd=ROOT,
                                     capture_output=True, text=True)
                return self.send_json({"log": res.stdout + res.stderr})
            self.send_json({"error": "not found"}, HTTPStatus.NOT_FOUND)
        except Exception as e:
            self.send_json({"error": f"{type(e).__name__}: {e}"}, HTTPStatus.INTERNAL_SERVER_ERROR)


def main():
    server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
    url = f"http://localhost:{PORT}"
    print(f"Horror Video Studio: {url}  (Ctrl+C để tắt)")
    if "--no-browser" not in sys.argv:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
