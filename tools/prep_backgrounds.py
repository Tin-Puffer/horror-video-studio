#!/usr/bin/env python3
"""Clean generated backgrounds: hide the Gemini watermark, apply per-image fixes.

Usage: python3 tools/prep_backgrounds.py   (assets/source/bg*.png -> assets/backgrounds/)
"""
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
# Gemini sparkle logo position on 2752x1536 output (bottom-right corner)
WATERMARK = (2580, 1365, 2700, 1485)


def remove_watermark(im: Image.Image) -> Image.Image:
    x0, y0, x1, y1 = WATERMARK
    w = x1 - x0
    patch = im.crop((x0 - w - 10, y0, x0 - 10, y1))  # same-height texture just to the left
    mask = Image.new("L", (w, y1 - y0), 0)
    ImageDraw.Draw(mask).rectangle((6, 6, w - 6, y1 - y0 - 6), 255)
    im.paste(patch, (x0, y0), mask.filter(ImageFilter.GaussianBlur(5)))
    return im


def set_clock(im: Image.Image, text: str = "03:00") -> Image.Image:
    """Repaint the bedside alarm clock display (bg1)."""
    box = (1282, 810, 1392, 848)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle(box, 4, fill=(22, 27, 36))
    font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 30)
    glow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    gd.text((cx, cy), text, font=font, fill=(150, 200, 255, 255), anchor="mm")
    halo = glow.filter(ImageFilter.GaussianBlur(4))
    out = im.convert("RGBA")
    out.alpha_composite(halo)
    out.alpha_composite(glow)
    return out.convert("RGB")


FIXES = {
    "bg1_bedroom": [set_clock],
}


def main():
    out_dir = ROOT / "assets/backgrounds"
    out_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted((ROOT / "assets/source").glob("bg*.png")):
        im = remove_watermark(Image.open(src).convert("RGB"))
        for fix in FIXES.get(src.stem, []):
            im = fix(im)
        im.save(out_dir / src.name)
        print(f"  {src.name} {im.size}")


if __name__ == "__main__":
    main()
