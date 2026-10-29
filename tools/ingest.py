#!/usr/bin/env python3
"""Bring a generated image into the asset library for one asset request.

  python3 tools/ingest.py scripts/<story>.json <request_id> <image.png | sound.mp3>

sheet           -> assets/source/<id>.png, sprites.json entry, cut, meta.json entries
background      -> assets/source/<id>.png, watermark removed, backgrounds/meta.json entry
character_base  -> assets/source/<char>_base.png, new character folder + meta.json
sound           -> assets/audio/sfx/<id>.<ext>, assets/audio/meta.json entry
Then rebuilds the catalog. Anchors and hotspots listed as *_needed are reported
so they can be measured on the new image (they are not guessed).
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def rw_json(path: Path, update):
    data = json.loads(path.read_text()) if path.exists() else {}
    update(data)
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False))


def run(*cmd):
    subprocess.run([sys.executable, "-W", "ignore", *cmd], cwd=ROOT, check=True)


def main():
    story_path, req_id, image = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
    story = json.loads(story_path.read_text())
    req = next(r for r in story.get("asset_requests", []) if r["id"] == req_id)
    kind = req["kind"]
    todo = []

    if kind == "sheet":
        char = req["character"]
        src = f"assets/source/{req_id}.png"
        shutil.copy(image, ROOT / src)

        def add_sheet(cfg):
            cfg["sheets"] = [s for s in cfg["sheets"] if s["source"] != src]
            entry = {"source": src, "out_dir": f"assets/characters/{char}",
                     "grid": req.get("grid", [2, 3]), "names": [sp["name"] for sp in req["sprites"]]}
            for opt in ("light_beams", "clear_white"):
                if opt in req:
                    entry[opt] = req[opt]
            cfg["sheets"].append(entry)
        rw_json(ROOT / "tools/sprites.json", add_sheet)
        run("tools/cut_sprites.py", src)

        def add_meta(meta):
            sprites = meta.setdefault("sprites", {})
            for sp in req["sprites"]:
                e = sprites.setdefault(sp["name"], {})
                e.update({k: sp[k] for k in ("desc", "tags", "facing") if k in sp})
                for a in sp.get("anchors_needed", []):
                    if a not in e.get("anchors", {}):
                        todo.append(f"đo anchor '{a}' cho {char}/{sp['name']}")
            for name, frames in req.get("cycles", {}).items():
                meta.setdefault("cycles", {})[name] = frames
        rw_json(ROOT / f"assets/characters/{char}/meta.json", add_meta)

    elif kind == "background":
        shutil.copy(image, ROOT / f"assets/source/{req_id}.png")
        run("tools/prep_backgrounds.py")

        def add_bg(meta):
            e = meta.setdefault("backgrounds", {}).setdefault(req_id, {})
            e.update({k: req[k] for k in ("desc", "tags", "floor_y", "char_h") if k in req})
            e.setdefault("hotspots", {})
            todo.extend(f"đo hotspot '{h}' cho {req_id}" for h in req.get("hotspots_needed", [])
                        if h not in e["hotspots"])
        rw_json(ROOT / "assets/backgrounds/meta.json", add_bg)

    elif kind == "sound":
        dest = ROOT / "assets/audio/sfx" / f"{req_id}{image.suffix.lower()}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        for old in dest.parent.glob(f"{req_id}.*"):
            old.unlink()
        shutil.copy(image, dest)

        def add_sound(meta):
            e = meta.setdefault("sounds", {}).setdefault(req_id, {})
            e.update({k: req[k] for k in ("desc", "tags", "volume") if k in req})
            e["kind"] = req.get("sound_kind", "sfx")
        rw_json(ROOT / "assets/audio/meta.json", add_sound)

    elif kind == "character_base":
        char = req["character"]
        src = f"assets/source/{char}_base.png"
        shutil.copy(image, ROOT / src)
        (ROOT / f"assets/characters/{char}").mkdir(parents=True, exist_ok=True)

        def add_sheet(cfg):
            cfg["sheets"] = [s for s in cfg["sheets"] if s["source"] != src]
            cfg["sheets"].append({"source": src, "out_dir": f"assets/characters/{char}",
                                  "grid": [1, 1], "names": [f"{char}_base_front"]})
        rw_json(ROOT / "tools/sprites.json", add_sheet)
        run("tools/cut_sprites.py", src)

        def add_meta(meta):
            meta.update({"name": req.get("name", char), "default_h": req.get("default_h", 0.46),
                         "reference_images": [src],
                         "style_prompt": f"Same character as the reference image: {req['design']}"})
            meta.setdefault("sprites", {})[f"{char}_base_front"] = {
                "desc": "Ảnh mẫu: đứng chính diện", "tags": ["đứng", "chính diện"], "facing": "front"}
        rw_json(ROOT / f"assets/characters/{char}/meta.json", add_meta)
        todo.append(f"kiểm tra style_prompt của {char} trong meta.json")

    run("tools/catalog.py")
    print(f"ingested {req_id} ({kind})")
    for t in todo:
        print("  còn việc:", t)


if __name__ == "__main__":
    main()
