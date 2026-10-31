#!/usr/bin/env python3
"""Pack everything another AI needs to write storyboards for this project.

  python3 tools/make_brief.py   -> build/brief/ + build/brief.zip

BRIEF_VIET_KICH_BAN.md (one file: task, rules, JSON reference, asset catalog,
template, full example) + the catalog contact sheets for AIs that can see images.
Regenerate after adding assets so the catalog in the brief is current.
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "build/brief"

TASK = """# Hồ sơ cho AI viết kịch bản — Horror Video Studio

## Vai trò và nhiệm vụ
Bạn viết **kịch bản JSON** cho một công cụ dựng video hoạt hình kinh dị kể chuyện tiếng Việt
(sprite vẽ tay nét sáp màu, một người kể ở ngôi thứ nhất). Công cụ đọc JSON và tự dựng video:
giọng đọc, nhân vật, chu kỳ chuyển động, camera, hiệu ứng, âm thanh, phụ đề.

Đầu vào: ý tưởng / truyện (có thể bằng tiếng nước ngoài). Đầu ra bạn phải trả về:
1. **Một file JSON hoàn chỉnh** theo đúng cấu trúc ở mục "Tài liệu JSON", bắt đầu từ "Kịch bản mẫu".
2. **Danh sách asset còn thiếu** nằm trong `asset_requests` của chính file JSON (chỉ khi kho không có).
3. Một đoạn ngắn giải thích lựa chọn (độ dài, số cảnh, asset dùng lại / cần tạo).

Bắt buộc:
- Tuân thủ **toàn bộ** "Quy tắc kịch bản" bên dưới (đặc biệt: một giọng người kể duy nhất, câu liền mạch, không chèn [n] < 0.5s giữa câu, tiếng động dùng sfx, di chuyển bằng cycle + face auto, camera lia cần zoom ≥ 1.15).
- **Chỉ dùng tên sprite / chu kỳ / phông / điểm nóng / âm thanh có trong "Mục lục kho"** — không bịa tên. Thứ chưa có thì khai báo trong `asset_requests` và vẫn dùng tên đó trong cảnh (công cụ hiện khung giữ chỗ).
- Giữ nguyên các khối `settings`, `characters`, `voice_presets` của mẫu trừ khi có lý do.
- JSON hợp lệ (không chú thích, không dấu phẩy thừa).

Người dùng sẽ kiểm tra bằng `python3 tools/check_story.py scripts/<truyen>.json` — mọi dòng "LỖI" và "quy tắc:" phải được xử lý.
"""


def section(title: str, body: str, lang: str = "") -> str:
    fence = f"```{lang}\n{body.rstrip()}\n```" if lang else body.rstrip()
    return f"\n\n---\n\n# {title}\n\n{fence}\n"


def json_reference() -> str:
    sys.path.insert(0, str(ROOT / "tools"))
    import render
    parts = [render.__doc__, render.draw_layer.__doc__, render.camera_at.__doc__, render.mix_audio.__doc__,
             render.speech_items.__doc__]
    defaults = json.dumps(render.DEFAULTS, indent=1, ensure_ascii=False)
    import check_story
    return ("\n\n".join(p.strip() for p in parts if p) +
            "\n\nasset_requests:\n" + check_story.__doc__.split("asset_requests entries:")[1].strip() +
            "\n\nGiá trị mặc định (settings) khi kịch bản không ghi:\n" + defaults)


def main():
    subprocess.run([sys.executable, "-W", "ignore", str(ROOT / "tools/catalog.py")], check=True, capture_output=True)
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True)
    md = TASK
    md += section("Quy tắc kịch bản", (ROOT / "scripts/QUY_TAC_KICH_BAN.md").read_text())
    md += section("Tài liệu JSON (khoá và ý nghĩa)", json_reference(), "text")
    cat = ROOT / "assets/catalog"
    details = [cat / "backgrounds.md"] + sorted(p for p in cat.glob("*.md") if p.stem not in ("backgrounds", "PROMPTS"))
    md += section("Mục lục kho asset", "\n\n".join(p.read_text().rstrip() for p in
                                                  [ROOT / "assets/CATALOG.md", *details, cat / "PROMPTS.md"]))
    md += section("Kịch bản mẫu (bắt đầu từ đây)", (ROOT / "templates/kich_ban_mau.json").read_text(), "json")
    example = ROOT / "scripts/cuoc_goi_3h.json"
    sys.path.insert(0, str(ROOT / "tools"))
    import check_story
    issues = check_story.rule_warnings(json.loads(example.read_text()))
    note = ("Dùng để học cách bố trí cảnh, camera, âm thanh, chu kỳ chuyển động."
            + ("\n\n**Ví dụ này được làm trước một số quy tắc — KHÔNG bắt chước các điểm sau:**\n"
               + "\n".join(f"- {i}" for i in issues) if issues else ""))
    md += section("Ví dụ đầy đủ đã hoàn thiện: Cuộc gọi lúc 3 giờ sáng",
                  note + "\n\n```json\n" + example.read_text().rstrip() + "\n```")
    (OUT / "BRIEF_VIET_KICH_BAN.md").write_text(md)
    shutil.copytree(ROOT / "assets/catalog", OUT / "anh_kho_asset")
    zip_path = shutil.make_archive(str(ROOT / "build/brief"), "zip", OUT)
    print(f"-> {OUT / 'BRIEF_VIET_KICH_BAN.md'} ({len(md) // 1000} nghìn ký tự)")
    print(f"-> {zip_path}")


if __name__ == "__main__":
    main()
