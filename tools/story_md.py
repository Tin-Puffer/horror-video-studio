#!/usr/bin/env python3
"""Readable shooting script (Markdown) generated from a storyboard JSON.

  python3 tools/story_md.py scripts/<story>.json   -> scripts/<story>.md

Always regenerate instead of editing the .md: the JSON is the source of truth.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import render  # noqa: E402

EASE_VN = {"smooth": "mượt", "linear": "đều", "in": "chậm rồi nhanh dần", "out": "nhanh rồi chậm dần", None: "mượt"}


def where(x: float) -> str:
    return "trái" if x < 0.4 else "phải" if x > 0.6 else "giữa"


def camera_text(cam: dict | None, dur: float) -> str:
    if not cam:
        return "Máy đứng yên, toàn cảnh."
    parts = []
    if "keys" in cam:
        keys = sorted(cam["keys"], key=lambda k: k.get("p", 0))
        cur = {"zoom": 1.0, "x": 0.5, "y": 0.5}
        for i, k in enumerate(keys):
            nxt = {**cur, **{n: k[n] for n in ("zoom", "x", "y") if n in k}}
            t = k.get("p", 0) * dur
            if i == 0:
                z0 = nxt["zoom"]
                frame = "toàn cảnh" if z0 <= 1.01 else "cận x%g vào bên %s" % (z0, where(nxt["x"]))
                parts.append(f"{t:.1f}s: khung {frame}")
            else:
                moves = []
                if abs(nxt["zoom"] - cur["zoom"]) > 0.01:
                    moves.append(f"{'đẩy vào' if nxt['zoom'] > cur['zoom'] else 'kéo ra'} x{nxt['zoom']:g}")
                if abs(nxt["x"] - cur["x"]) > 0.01:
                    moves.append(f"lia {'phải' if nxt['x'] > cur['x'] else 'trái'}")
                if abs(nxt["y"] - cur["y"]) > 0.01:
                    moves.append(f"{'hạ máy xuống' if nxt['y'] > cur['y'] else 'ngước máy lên'}")
                if moves:
                    t0 = keys[i - 1].get("p", 0) * dur
                    parts.append(f"{t0:.1f}–{t:.1f}s: {', '.join(moves)} ({EASE_VN.get(k.get('ease'), k.get('ease'))})")
                else:
                    parts.append(f"đến {t:.1f}s: giữ khung")
            cur = nxt
    else:
        z = cam.get("zoom", 1.0)
        if isinstance(z, list):
            parts.append(f"{'đẩy vào' if z[1] > z[0] else 'kéo ra'} từ x{z[0]:g} đến x{z[1]:g} suốt cảnh")
    if cam.get("handheld"):
        parts.append(f"rung tay nhẹ ({cam['handheld']})")
    return "; ".join(parts) + "."


def layer_text(L: dict, cat_desc) -> str:
    if "ui" in L:
        return f"📱 Màn hình điện thoại ({'cuộc gọi đến' if L['ui'] == 'call' else 'tin nhắn'}) từ {L.get('name', '')}" + \
               (f": “{L['message']}”" if L.get("message") else "")
    if "cycle" in L:
        name = f"chu kỳ `{L['cycle']}`"
    elif "frames" in L:
        name = f"{len(L['frames'])} khung luân phiên"
    else:
        name = f"`{L['sprite']}` ({cat_desc(L['sprite'])})"
    bits = [name]
    x = L.get("x")
    if isinstance(x, list):
        bits.append(f"di chuyển {where(x[0])} → {where(x[1])}")
    elif x is not None:
        bits.append(f"đứng bên {where(x)}")
    if L.get("pin"):
        bits.append(f"neo `{L['pin']['point']}` vào `{L['pin']['at']}`" if isinstance(L["pin"].get("at"), str) else "neo vào điểm trên phông")
    if L.get("start") or L.get("end", 1) < 1:
        bits.append(f"xuất hiện {L.get('start', 0):g}→{L.get('end', 1):g} của cảnh")
    for k, vn in (("glow", "viền sáng"), ("jitter", "run rẩy"), ("face", "hướng")):
        if L.get(k):
            bits.append(f"{vn} {L[k]}" if k == "face" else vn)
    return ", ".join(bits)


def main():
    path = Path(sys.argv[1])
    story = json.loads(path.read_text())
    render.CFG = render.deep_merge(render.DEFAULTS, story.get("settings", {}))
    timing, voice = render.CFG["timing"], render.CFG["voice"]
    descs = {}

    def cat_desc(ref: str) -> str:
        char, _, name = ref.partition("/")
        if ref not in descs:
            meta = render.load_meta(char).get("sprites", {}).get(name)
            req = next((sp for r in story.get("asset_requests", []) if r.get("character") == char
                        for sp in r.get("sprites", []) if sp["name"] == name), None)
            descs[ref] = meta["desc"] if meta else (f"CHƯA CÓ — {req['desc']}" if req else "CHƯA CÓ")
        return descs[ref]

    out = [f"# {story['title']}", ""]
    if story.get("logline"):
        out += [f"> {story['logline']}", ""]
    out += [f"_Tự sinh từ `{path.name}` bằng `tools/story_md.py` — sửa JSON (hoặc Studio) rồi chạy lại._", ""]
    for m in story.get("music", []):
        out.append(f"- 🎵 Nhạc nền `{m['sound']}`: cảnh {m.get('from', 'đầu')} → {m.get('to', 'cuối')}, "
                   f"âm lượng {m.get('volume', 1)}, tự nhỏ lại khi có lời đọc")
    out.append("")
    t_total = 0.0
    for s in story["scenes"]:
        speech = render.tts(s["text"], voice) if s.get("text") else []
        dur = s.get("duration") or max(s.get("min_duration", timing["min_duration"]),
                                       timing["lead"] + len(speech) / voice["sample_rate"] + timing["tail"])
        out += [f"## Cảnh {s['id']} — {s['bg']}  ·  {t_total:.1f}s → {t_total + dur:.1f}s ({dur:.1f}s)", ""]
        if s.get("text"):
            out.append(f"**Lời đọc:** {s['text']}")
        if s.get("title_text"):
            out.append(f"**Chữ trên màn hình:** {s['title_text']}")
        out.append(f"**Camera:** {camera_text(s.get('camera'), dur)}")
        fx = []
        if s.get("shake"):
            sh = s["shake"]
            fx.append(f"rung {sh['amp']}px ({sh.get('from', 0) * dur:.1f}–{sh.get('to', 1) * dur:.1f}s)")
        fx += [f"chớp trắng {p * dur:.1f}s" for p in s.get("flash", [])]
        if s.get("flicker"):
            fx.append(f"đèn chập chờn {s['flicker']}")
        if fx:
            out.append(f"**Hiệu ứng:** {', '.join(fx)}")
        if s.get("sfx"):
            cues = [f"{(c['t'] if 't' in c else c.get('at', 0) * dur):.1f}s `{c['sound']}`"
                    + (" (lặp" + (f" {c['length']}s" if c.get("length") else "") + ")" if c.get("loop") else "")
                    for c in s["sfx"]]
            out.append(f"**Âm thanh:** {' · '.join(cues)}")
        for L in s.get("layers", []):
            out.append(f"- {layer_text(L, cat_desc)}")
        out.append("")
        t_total += dur
    out[2:2] = [f"**Tổng thời lượng:** {t_total:.0f}s ({t_total / 60:.1f} phút) · {len(story['scenes'])} cảnh", ""]
    dest = path.with_suffix(".md")
    dest.write_text("\n".join(out))
    print("->", dest)


if __name__ == "__main__":
    main()
