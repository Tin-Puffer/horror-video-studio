#!/usr/bin/env python3
"""Build the asset catalog that story writing starts from.

Outputs:
  assets/CATALOG.md            short index: characters + cycle names, backgrounds +
                               hotspot names, sounds (read this first)
  assets/catalog/<char>.md     every sprite of one character: facing, desc, tags, anchors
  assets/catalog/backgrounds.md  floor_y, char_h, hotspot coordinates
  assets/catalog/PROMPTS.md    style prompts + reference images (for asset_requests)
  assets/catalog/<char>.png    labelled contact sheet per character
  assets/catalog/backgrounds.png
Also reports sprites that exist on disk but have no description in meta.json,
and meta entries whose file is missing.

Usage: python3 tools/catalog.py
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from render import DEFAULTS

ROOT = Path(__file__).resolve().parent.parent
CHARS = ROOT / "assets/characters"
BGS = ROOT / "assets/backgrounds"
OUT = ROOT / "assets/catalog"
FONT = DEFAULTS["fonts"]["regular"]  # this machine's font (config.local.json)


def contact_sheet(items: list[tuple[str, Path]], out: Path, thumb_h: int = 220, cols: int = 8):
    f = ImageFont.truetype(FONT, 15)
    cells = []
    for label, path in items:
        im = Image.open(path).convert("RGBA")
        im = im.resize((max(1, round(im.width * thumb_h / im.height)), thumb_h))
        if im.width > thumb_h * 1.6:
            im = im.resize((round(thumb_h * 1.6), round(im.height * thumb_h * 1.6 / im.width)))
        cells.append((label, im))
    cw = round(thumb_h * 1.6) + 10
    rows = (len(cells) + cols - 1) // cols
    sheet = Image.new("RGBA", (cw * cols, (thumb_h + 30) * rows), (28, 32, 46, 255))
    d = ImageDraw.Draw(sheet)
    for i, (label, im) in enumerate(cells):
        x, y = (i % cols) * cw, (i // cols) * (thumb_h + 30)
        sheet.alpha_composite(im, (x + (cw - im.width) // 2, y + thumb_h - im.height))
        d.text((x + cw / 2, y + thumb_h + 4), label, font=f, fill=(235, 235, 120), anchor="mt")
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.convert("RGB").save(out)


def write(path: Path, lines: list[str]):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines))


def main():
    # Short index (read first) + one detail file per character / backgrounds, so writing a story only
    # loads the characters it uses and the cost stays flat as the library grows.
    head = "> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại."
    index = ["# Kho asset — mục lục (bản ngắn)", "", head,
             "> Chi tiết từng nhân vật (sprite, hướng, neo, khung chu kỳ): `assets/catalog/<nhân vật>.md` — chỉ mở nhân vật truyện cần.",
             "> Phông (floor_y, char_h, toạ độ điểm nóng): `assets/catalog/backgrounds.md`.",
             "> Style prompt + ảnh tham chiếu (chỉ cần khi viết `asset_requests`; check_story tự ghép vào prompt): `assets/catalog/PROMPTS.md`.",
             "> Ảnh xem nhanh (chỉ mở khi mô tả chữ chưa đủ): `assets/catalog/<nhân vật>.png`, `assets/catalog/backgrounds.png`.", "",
             "## Nhân vật", "", "| Nhân vật | Tên | Sprite | Cao | Chu kỳ (`\"cycle\": \"<nv>/<tên>\"`) |", "|---|---|---|---|---|"]
    prompts = ["# Style prompt + ảnh tham chiếu", "", head,
               "> check_story.py tự ghép style prompt + ảnh tham chiếu vào prompt của `asset_requests`;",
               "> file này để tham khảo khi viết `design` cho nhân vật mới cho cùng nét vẽ.", ""]
    problems = []

    for char_dir in sorted(p for p in CHARS.iterdir() if p.is_dir()):
        char = char_dir.name
        meta_path = char_dir / "meta.json"
        meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
        sprites = meta.get("sprites", {})
        files = sorted(p.stem for p in char_dir.glob("*.png"))
        cycles = meta.get("cycles", {})
        index.append(f"| `{char}` | {meta.get('name', '')} | {len(files)} | {meta.get('default_h', '?')} | "
                     f"{', '.join(f'`{n}`({len(f)})' for n, f in cycles.items())} |")
        prompts += [f"## `{char}` — {meta.get('name', '')}", "",
                    f"- Ảnh tham chiếu: {', '.join(f'`{r}`' for r in meta.get('reference_images', []))}",
                    f"- Style prompt: {meta.get('style_prompt', '(chưa có)')}", ""]
        lines = [f"# Nhân vật `{char}` — {meta.get('name', '')}", "", head, "",
                 f"- Chiều cao mặc định: `{meta.get('default_h', '?')}` khung hình", ""]
        if cycles:
            lines += ["**Chu kỳ chuyển động** (dùng `\"cycle\": \"%s/<tên>\"`):" % char, ""]
            for name, frames in cycles.items():
                lines.append(f"- `{name}`: {len(frames)} khung — {', '.join(frames)}")
            lines.append("")
        lines += ["| Sprite | Hướng | Mô tả | Tag | Neo |", "|---|---|---|---|---|"]
        for name in files:
            e = sprites.get(name)
            if not e:
                problems.append(f"{char}/{name}: chưa có mô tả trong meta.json")
                lines.append(f"| `{name}` | ? | **(chưa mô tả)** | | |")
                continue
            anchors = ", ".join(e.get("anchors", {}))
            lines.append(f"| `{name}` | {e.get('facing', 'front')} | {e.get('desc', '')} | "
                         f"{', '.join(e.get('tags', []))} | {anchors} |")
        for name in sprites:
            if name not in files:
                problems.append(f"{char}/{name}: có trong meta.json nhưng thiếu file PNG")
        lines.append("")
        write(OUT / f"{char}.md", lines)
        if files:  # a character created for an open asset request has no sprites yet
            contact_sheet([(n, char_dir / f"{n}.png") for n in files], OUT / f"{char}.png")
    index.append("")

    bg_meta = json.loads((BGS / "meta.json").read_text()) if (BGS / "meta.json").exists() else {}
    bgs = bg_meta.get("backgrounds", {})
    files = sorted(p.stem for p in BGS.glob("*.png"))
    prompts += ["## Phông nền", "",
                f"- Ảnh tham chiếu: {', '.join(f'`{r}`' for r in bg_meta.get('reference_images', []))}",
                f"- Style prompt: {bg_meta.get('style_prompt', '')}", ""]
    index += ["## Phông nền", "", "| Phông | Mô tả | Điểm nóng (`pin.at`) |", "|---|---|---|"]
    lines = ["# Phông nền", "", head, "", bg_meta.get("_coords", ""), "",
             "| Phông | Mô tả | floor_y | char_h | Điểm nóng (dùng tên trong `pin.at`) |", "|---|---|---|---|---|"]
    for name in files:
        e = bgs.get(name)
        if not e:
            problems.append(f"background {name}: chưa có mô tả trong assets/backgrounds/meta.json")
            lines.append(f"| `{name}` | **(chưa mô tả)** | | | |")
            index.append(f"| `{name}` | **(chưa mô tả)** | |")
            continue
        hs = "; ".join(f"`{k}` {v}" for k, v in e.get("hotspots", {}).items())
        lines.append(f"| `{name}` | {e['desc']} | {e.get('floor_y', '')} | {e.get('char_h', '')} | {hs} |")
        index.append(f"| `{name}` | {e['desc']} | {', '.join(e.get('hotspots', {}))} |")
    lines.append("")
    index.append("")
    write(OUT / "backgrounds.md", lines)
    write(OUT / "PROMPTS.md", prompts)
    contact_sheet([(n, BGS / f"{n}.png") for n in files], OUT / "backgrounds.png", thumb_h=180, cols=4)

    ameta = json.loads((ROOT / "assets/audio/meta.json").read_text()) if (ROOT / "assets/audio/meta.json").exists() else {}
    sounds = ameta.get("sounds", {})
    sfiles = sorted({p.stem for p in (ROOT / "assets/audio/sfx").glob("*.*")}) if (ROOT / "assets/audio/sfx").exists() else []
    index += ["## Âm thanh", "", "Dùng trong cảnh: `\"sfx\": [{\"sound\": <tên>, \"at\": 0.3}]`; nhạc nền: `\"music\"` ở cấp kịch bản.", ""]
    if sfiles:
        index += ["| Âm thanh | Loại | Mô tả | Âm lượng |", "|---|---|---|---|"]
        for name in sfiles:
            e = sounds.get(name)
            if not e:
                problems.append(f"sound {name}: chưa có mô tả trong assets/audio/meta.json")
                index.append(f"| `{name}` | ? | **(chưa mô tả)** | |")
                continue
            index.append(f"| `{name}` | {e.get('kind', 'sfx')} | {e.get('desc', '')} | {e.get('volume', 1)} |")
    else:
        index.append("(chưa có âm thanh nào)")
    index.append("")

    if problems:
        index += ["## Cần bổ sung mô tả", ""] + [f"- {p}" for p in problems] + [""]
    write(ROOT / "assets/CATALOG.md", index)
    n_sprites = sum(1 for _ in CHARS.glob("*/*.png"))
    print(f"catalog: {n_sprites} sprites, {len(files)} backgrounds, {len(sfiles)} sounds -> assets/CATALOG.md, assets/catalog/")
    for p in problems:
        print("  !", p)


if __name__ == "__main__":
    main()
