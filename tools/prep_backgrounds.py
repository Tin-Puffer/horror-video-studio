#!/usr/bin/env python3
"""Clean generated backgrounds: hide the Gemini watermark, apply per-image fixes.

Usage: python3 tools/prep_backgrounds.py   (assets/source/bg*.png -> assets/backgrounds/)
"""
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

from render import DEFAULTS

ROOT = Path(__file__).resolve().parent.parent
# Gemini sparkle logo position on 2752x1536 output (bottom-right corner)
WATERMARK = (2580, 1365, 2700, 1485)


def remove_watermark(im: Image.Image, box=None) -> Image.Image:
    # Gemini sometimes outputs half size (1376x768): scale the logo box to the image
    sx, sy = im.width / 2752, im.height / 1536
    x0, y0, x1, y1 = box or (round(WATERMARK[0] * sx), round(WATERMARK[1] * sy),
                             round(WATERMARK[2] * sx), round(WATERMARK[3] * sy))
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
    mono = [p for p in ("/System/Library/Fonts/Menlo.ttc", "C:/Windows/Fonts/consola.ttf") if Path(p).exists()]
    font = ImageFont.truetype(mono[0] if mono else DEFAULTS["fonts"]["regular"], 30)
    glow = Image.new("RGBA", im.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    cx, cy = (box[0] + box[2]) / 2, (box[1] + box[3]) / 2
    gd.text((cx, cy), text, font=font, fill=(150, 200, 255, 255), anchor="mm")
    halo = glow.filter(ImageFilter.GaussianBlur(4))
    out = im.convert("RGBA")
    out.alpha_composite(halo)
    out.alpha_composite(glow)
    return out.convert("RGB")


def dawn_light(im: Image.Image) -> Image.Image:
    """Night picture -> early dawn: lift the shadows and wash in pale gray-blue
    morning light from the upper right (the window side)."""
    a = np.asarray(im.convert("RGB")).astype(np.float32) / 255
    a = a ** 0.72  # lift dark tones
    h, w = a.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    glow = np.clip(1.0 - np.hypot((xx - w) / w, yy / h) / 1.3, 0, 1)[..., None] * 0.22
    a = a * (1 - glow) + np.array([0.80, 0.84, 0.92]) * glow
    a = a * 0.9 + a.mean(axis=2, keepdims=True) * 0.1  # a little less saturated
    return Image.fromarray((a.clip(0, 1) * 255).astype(np.uint8))


FIXES = {
    "bg1_bedroom": [set_clock],
    # ảnh nửa cỡ, logo nằm lệch chỗ thường
    "bgL25_mom_bed_sick_night": [lambda im: remove_watermark(im, (1220, 605, 1305, 692))],
    "bg1d_corner_dawn": [dawn_light],
}


def main():
    out_dir = ROOT / "assets/backgrounds"
    out_dir.mkdir(parents=True, exist_ok=True)
    ret_path = ROOT / "assets/retired.json"
    retired = set(json.loads(ret_path.read_text()).get("backgrounds", [])) if ret_path.exists() else set()
    for src in sorted((ROOT / "assets/source").glob("bg*.png")):
        if src.stem in retired:  # removed on purpose, don't recreate
            continue
        im = remove_watermark(Image.open(src).convert("RGB"))
        for fix in FIXES.get(src.stem, []):
            im = fix(im)
        im.save(out_dir / src.name)
        print(f"  {src.name} {im.size}")


if __name__ == "__main__":
    main()
