#!/usr/bin/env python3
"""Build the asset catalog that story writing starts from.

Outputs:
  assets/CATALOG.md            every character sprite, cycle, background and
                               hotspot with description/tags (read this first)
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

ROOT = Path(__file__).resolve().parent.parent
CHARS = ROOT / "assets/characters"
BGS = ROOT / "assets/backgrounds"
OUT = ROOT / "assets/catalog"
FONT = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


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


def main():
    lines = ["# Kho asset — mục lục", "",
             "> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.",
             "> Ảnh xem nhanh: `assets/catalog/<nhân vật>.png`, `assets/catalog/backgrounds.png`.", ""]
    problems = []

    for char_dir in sorted(p for p in CHARS.iterdir() if p.is_dir()):
        char = char_dir.name
        meta_path = char_dir / "meta.json"
        meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
        sprites = meta.get("sprites", {})
        files = sorted(p.stem for p in char_dir.glob("*.png"))
        lines += [f"## Nhân vật `{char}` — {meta.get('name', '')}", "",
                  f"- Chiều cao mặc định: `{meta.get('default_h', '?')}` khung hình",
                  f"- Ảnh tham chiếu khi tạo thêm: {', '.join(f'`{r}`' for r in meta.get('reference_images', []))}",
                  f"- Style prompt: {meta.get('style_prompt', '(chưa có)')}", ""]
        if meta.get("cycles"):
            lines += ["**Chu kỳ chuyển động** (dùng `\"cycle\": \"%s/<tên>\"`):" % char, ""]
            for name, frames in meta["cycles"].items():
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
        contact_sheet([(n, char_dir / f"{n}.png") for n in files], OUT / f"{char}.png")

    bg_meta = json.loads((BGS / "meta.json").read_text()) if (BGS / "meta.json").exists() else {}
    bgs = bg_meta.get("backgrounds", {})
    files = sorted(p.stem for p in BGS.glob("*.png"))
    lines += ["## Phông nền", "", bg_meta.get("_coords", ""), "",
              f"- Style prompt: {bg_meta.get('style_prompt', '')}", "",
              "| Phông | Mô tả | floor_y | char_h | Điểm nóng (dùng tên trong `pin.at`) |", "|---|---|---|---|---|"]
    for name in files:
        e = bgs.get(name)
        if not e:
            problems.append(f"background {name}: chưa có mô tả trong assets/backgrounds/meta.json")
            lines.append(f"| `{name}` | **(chưa mô tả)** | | | |")
            continue
        hs = "; ".join(f"`{k}` {v}" for k, v in e.get("hotspots", {}).items())
        lines.append(f"| `{name}` | {e['desc']} | {e.get('floor_y', '')} | {e.get('char_h', '')} | {hs} |")
    lines.append("")
    contact_sheet([(n, BGS / f"{n}.png") for n in files], OUT / "backgrounds.png", thumb_h=180, cols=4)

    ameta = json.loads((ROOT / "assets/audio/meta.json").read_text()) if (ROOT / "assets/audio/meta.json").exists() else {}
    sounds = ameta.get("sounds", {})
    sfiles = sorted({p.stem for p in (ROOT / "assets/audio/sfx").glob("*.*")}) if (ROOT / "assets/audio/sfx").exists() else []
    lines += ["## Âm thanh", "", "Dùng trong cảnh: `\"sfx\": [{\"sound\": <tên>, \"at\": 0.3}]`; nhạc nền: `\"music\"` ở cấp kịch bản.", ""]
    if sfiles:
        lines += ["| Âm thanh | Loại | Mô tả | Tag | Âm lượng |", "|---|---|---|---|---|"]
        for name in sfiles:
            e = sounds.get(name)
            if not e:
                problems.append(f"sound {name}: chưa có mô tả trong assets/audio/meta.json")
                lines.append(f"| `{name}` | ? | **(chưa mô tả)** | | |")
                continue
            lines.append(f"| `{name}` | {e.get('kind', 'sfx')} | {e.get('desc', '')} | {', '.join(e.get('tags', []))} | {e.get('volume', 1)} |")
    else:
        lines.append("(chưa có âm thanh nào)")
    lines.append("")

    if problems:
        lines += ["## Cần bổ sung mô tả", ""] + [f"- {p}" for p in problems] + [""]
    (ROOT / "assets/CATALOG.md").write_text("\n".join(lines))
    n_sprites = sum(1 for _ in CHARS.glob("*/*.png"))
    print(f"catalog: {n_sprites} sprites, {len(files)} backgrounds, {len(sfiles)} sounds -> assets/CATALOG.md, assets/catalog/")
    for p in problems:
        print("  !", p)


if __name__ == "__main__":
    main()
