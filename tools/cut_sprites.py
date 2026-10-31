#!/usr/bin/env python3
"""Cut character pose sheets into individual transparent PNG sprites.

Background removal: near-white pixels connected to the image border become
transparent (flood fill), so white areas enclosed by outlines (face, shoes)
stay opaque. Each sheet is split on a fixed grid, then cropped to content.

Usage: python3 tools/cut_sprites.py [source-filter ...]   (reads tools/sprites.json)
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
WHITE_THRESHOLD = 215  # min channel value counted as background
PAD = 16


def remove_background(img: Image.Image, light_beams: bool = False) -> Image.Image:
    rgb = np.asarray(img.convert("RGB"))
    light = (rgb.min(axis=2) >= WHITE_THRESHOLD).astype(np.uint8) * 255
    # pad with a light border so the fill reaches every edge region
    mask = Image.fromarray(np.pad(light, 1, constant_values=255)).copy()  # copy: fromarray buffer is read-only
    ImageDraw.floodfill(mask, (0, 0), 128)
    bg = np.asarray(mask)[1:-1, 1:-1] == 128
    alpha = Image.fromarray(np.where(bg, 0, 255).astype(np.uint8))
    # soften the cut edge slightly so it blends over dark scenes
    alpha = alpha.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    alpha = np.asarray(alpha).astype(np.float32) / 255
    rgb = rgb.astype(np.float32)
    if not light_beams:
        return Image.fromarray(np.dstack([rgb, alpha * 255]).astype(np.uint8))

    # pale-yellow light beams (flashlight) fade into the white paper: turn them
    # into a translucent glow instead of a hard cut. Opt-in per sheet: beige
    # clothing matches the same colour test.
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    beam = (r >= 200) & (g >= 170) & (r - b >= 12)
    glow = np.clip((r - b) / 90, 0, 1)
    glow = np.asarray(Image.fromarray((np.where(beam, glow, 0) * 255).astype(np.uint8))
                      .filter(ImageFilter.GaussianBlur(10))).astype(np.float32) / 255
    # the beam itself and its faded fringe; dark outlines of the torch stay as drawn
    use_glow = (glow > 0.03) & (rgb.min(axis=2) >= 150) & (beam | (alpha < 0.5))
    a = np.where(use_glow, np.clip(glow * 2.2, 0, 0.85), alpha)
    # flat warm colour: re-using the paper pixels would amplify their noise
    rgb = np.where(use_glow[..., None], np.array([255, 232, 150], np.float32), rgb)
    out = np.dstack([rgb, a * 255]).astype(np.uint8)
    return Image.fromarray(out)


def drop_specks(img: Image.Image, min_ratio: float = 0.02) -> Image.Image:
    """Clear small opaque islands touching the cell edge (spill from neighbour cells).

    Small islands inside the cell are kept: they are effect marks
    (shake lines, shock bursts, a falling phone).
    """
    alpha = np.asarray(img.getchannel("A")).copy()
    labels = Image.fromarray((alpha > 20).astype(np.uint8) * 255).copy()
    sizes = {}
    next_id = 1
    for y, x in zip(*np.where(np.asarray(labels) == 255)):
        if labels.getpixel((int(x), int(y))) != 255:
            continue
        ImageDraw.floodfill(labels, (int(x), int(y)), next_id)
        sizes[next_id] = int((np.asarray(labels) == next_id).sum())
        next_id = next_id % 254 + 1 if next_id < 254 else 1
        if next_id == 1:
            break  # too many islands; leave as is
    if not sizes:
        return img
    lab = np.asarray(labels)
    biggest = max(sizes.values())
    edge_ids = set(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]).tolist())
    for k, n in sizes.items():
        if n < biggest * min_ratio and k in edge_ids:
            alpha[lab == k] = 0
    out = img.copy()
    out.putalpha(Image.fromarray(alpha))
    return out


def gutters(alpha: np.ndarray, n: int, axis: int, search: float = 0.2) -> list[int]:
    """Split positions along axis: the emptiest line near each even grid line."""
    profile = (alpha > 20).sum(axis=1 - axis)
    length = len(profile)
    cuts = [0]
    for k in range(1, n):
        ideal = length * k / n
        lo, hi = int(ideal - length / n * search), int(ideal + length / n * search)
        window = profile[lo:hi]
        best = np.flatnonzero(window == window.min())
        cuts.append(lo + int(best[len(best) // 2]))  # middle of the emptiest band
    return cuts + [length]


def clear_paper_white(img: Image.Image, threshold: int = 240) -> Image.Image:
    """Make enclosed paper-white gaps transparent (e.g. between strands of flying hair).

    Only for sprites whose skin/eyes are not paper white: pure-white eyes or
    shoes would be punched out too, so this is opt-in per sprite.
    """
    arr = np.asarray(img).copy()
    paper = arr[..., :3].min(axis=2) >= threshold
    # opening: drop crayon-texture specks (a few px wide), keep real gaps,
    # then grow a little to include the anti-aliased rim
    paper = np.asarray(Image.fromarray(paper.astype(np.uint8) * 255)
                       .filter(ImageFilter.MinFilter(5))
                       .filter(ImageFilter.MaxFilter(9))) > 0
    arr[..., 3] = np.where(paper, 0, arr[..., 3])
    out = Image.fromarray(arr)
    return out.putalpha(out.getchannel("A").filter(ImageFilter.GaussianBlur(0.8))) or out


def clear_holes(img: Image.Image, points, threshold: int = 230) -> Image.Image:
    """Make the enclosed paper-white region around each point transparent
    (a gap between arm and body, under a stool). Points are fractions of the
    cropped sprite; unlike clear_paper_white this leaves white rice and eyes alone."""
    arr = np.asarray(img).copy()
    paper = Image.fromarray((arr[..., :3].min(axis=2) >= threshold).astype(np.uint8) * 255).copy()
    for fx, fy in points:
        ImageDraw.floodfill(paper, (int(fx * img.width), int(fy * img.height)), 128)
    hole = np.asarray(paper.filter(ImageFilter.MaxFilter(5))) == 128
    hole |= np.asarray(paper) == 128
    arr[..., 3] = np.where(hole, 0, arr[..., 3])
    return Image.fromarray(arr)


def crop_to_content(img: Image.Image) -> Image.Image | None:
    a = np.asarray(img.getchannel("A"))
    ys, xs = np.where(a > 20)
    if len(xs) == 0:
        return None
    x0, x1 = max(xs.min() - PAD, 0), min(xs.max() + PAD + 1, img.width)
    y0, y1 = max(ys.min() - PAD, 0), min(ys.max() + PAD + 1, img.height)
    return img.crop((x0, y0, x1, y1))


def main():
    cfg = json.loads((ROOT / "tools/sprites.json").read_text())
    only = sys.argv[1:]  # optional: only sheets whose source path contains one of these
    for sheet in cfg["sheets"]:
        if only and not any(o in sheet["source"] for o in only):
            continue
        src = Image.open(ROOT / sheet["source"])
        out_dir = ROOT / sheet["out_dir"]
        out_dir.mkdir(parents=True, exist_ok=True)
        rows, cols = sheet["grid"]
        cut = remove_background(src, sheet.get("light_beams", False))
        alpha = np.asarray(cut.getchannel("A"))
        ys, xs = gutters(alpha, rows, axis=0), gutters(alpha, cols, axis=1)
        boxes = sheet.get("boxes")  # irregular sheets: [x0, y0, x1, y1] per name instead of the grid
        sprites = {}
        for i, name in enumerate(sheet["names"]):
            if not name:
                continue
            r, c = divmod(i, cols)
            cell = cut.crop(tuple(boxes[i]) if boxes else (xs[c], ys[r], xs[c + 1], ys[r + 1]))
            if name in sheet.get("clear_white", []):
                cell = clear_paper_white(cell)
            # keep_box: animation frames cut with equal boxes keep their box, so the
            # still part (e.g. a bucket under changing flames) stays in place
            keep = name in sheet.get("keep_box", [])
            sprite = drop_specks(cell) if keep else crop_to_content(drop_specks(cell))
            if sprite is None:
                print(f"  ! empty cell {name}")
                continue
            if name in sheet.get("holes", {}):
                sprite = clear_holes(sprite, sheet["holes"][name])
            if name in sheet.get("rotate", {}):  # Gemini drew it the wrong way round (e.g. footprints)
                sprite = sprite.rotate(sheet["rotate"][name], expand=True)
            sprites[name] = sprite
        if sheet.get("same_height") and sprites:
            # cycle frames: render scales every frame to the same height, so pad the
            # top to a common height; the body then dips instead of growing
            top = max(s.height for s in sprites.values())
            for name, s in sprites.items():
                padded = Image.new("RGBA", (s.width, top), (0, 0, 0, 0))
                padded.paste(s, (0, top - s.height))
                sprites[name] = padded
        if sheet.get("align_head") and sprites:
            # cycle frames are placed by their centre: pad left/right so the head sits
            # at the same x in every frame, otherwise the body jitters as stride changes
            heads = {}
            for name, s in sprites.items():
                a = np.asarray(s.getchannel("A"))[: max(1, s.height // 4)] > 128
                heads[name] = np.nonzero(a)[1].mean() if a.any() else s.width / 2
            half = max(max(heads[n], s.width - heads[n]) for n, s in sprites.items())
            for name, s in sprites.items():
                w = int(np.ceil(2 * half))
                padded = Image.new("RGBA", (w, s.height), (0, 0, 0, 0))
                padded.paste(s, (round(half - heads[name]), 0))
                sprites[name] = padded
        for name, sprite in sprites.items():
            sprite.save(out_dir / f"{name}.png")
            print(f"  {name}.png {sprite.size}")


if __name__ == "__main__":
    main()
