# Horror Video Studio

Công cụ làm video hoạt hình kinh dị kể chuyện (tiếng Việt) từ sprite vẽ tay: viết kịch bản JSON → tự tạo giọng đọc, ghép nhân vật lên phông, chu kỳ chuyển động, camera, hiệu ứng, âm thanh, phụ đề → xuất MP4.

Kèm giao diện **Studio** để chỉnh cảnh và xem trước, cùng một **kho asset tự mô tả** để viết kịch bản biết dùng lại gì và cần tạo thêm gì.

Ví dụ có sẵn: `scripts/cuoc_goi_3h.json` (Cuộc gọi lúc 3 giờ sáng) và `scripts/nguoi_dung_cuoi_hanh_lang.json` (Người đứng cuối hành lang).

## Cài đặt

Cần Python 3.9+ và [ffmpeg](https://ffmpeg.org).

```bash
pip install -r requirements.txt     # Pillow, numpy, piper-tts
```

Giọng đọc dùng [piper](https://github.com/rhasspy/piper). Tải một giọng tiếng Việt (file `.onnx` + `.onnx.json`, ví dụ `vi_VN-vais1000-medium` từ [piper-voices](https://huggingface.co/rhasspy/piper-voices/tree/main/vi/vi_VN)) vào thư mục `voices/`, rồi đặt tên giọng trong kịch bản: `"settings": {"voice": {"model": "vi_VN-vais1000-medium"}}`.

Đường dẫn riêng của máy (piper ở chỗ khác, font khác trên Windows/Linux) ghi vào `config.local.json` (không đưa lên git):

```json
{
 "voice": {"piper": "/đường/dẫn/tới/piper", "models_dir": "~/thu-muc-giong"},
 "fonts": {"regular": "C:/Windows/Fonts/arial.ttf", "bold": "C:/Windows/Fonts/arialbd.ttf"}
}
```

## Dùng

```bash
python3 tools/studio.py                                   # giao diện: http://localhost:8765 (macOS: bấm đúp studio.command)
python3 tools/render.py scripts/cuoc_goi_3h.json --preview  # bản nháp nhanh
python3 tools/render.py scripts/cuoc_goi_3h.json            # Full HD → build/
```

| Công cụ | Việc |
|---|---|
| `tools/render.py` | Dựng video từ kịch bản JSON (mọi cấu hình nằm trong kịch bản) |
| `tools/studio.py` + `studio.html` | Giao diện chỉnh cảnh, xem trước khung hình thật, thư viện asset, xuất video |
| `tools/catalog.py` | Sinh mục lục kho `assets/CATALOG.md` + ảnh tổng hợp `assets/catalog/` |
| `tools/check_story.py` | Kiểm tra kịch bản với kho, xuất danh sách asset cần tạo kèm prompt |
| `tools/ingest.py` | Nạp ảnh/âm thanh mới vào kho theo yêu cầu trong kịch bản |
| `tools/story_md.py` | Sinh kịch bản dạng đọc được (`.md`) từ JSON |
| `tools/cut_sprites.py`, `tools/prep_backgrounds.py` | Cắt sheet nhân vật nền trắng thành PNG trong suốt; làm sạch phông nền |

Quy trình chi tiết (viết kịch bản, khai báo asset còn thiếu, nạp asset): xem `CLAUDE.md` và `scripts/HUONG_DAN_DUNG_VIDEO.md`.

## Kịch bản

```json
{"title": "...", "settings": {...}, "characters": {...}, "music": [...], "asset_requests": [...],
 "scenes": [{"id": 1, "bg": "bg2_hallway", "text": "Lời đọc…",
   "camera": {"keys": [{"p": 0, "zoom": 1.2, "x": 0.3}, {"p": 1, "x": 0.6, "ease": "in"}], "handheld": 5},
   "sfx": [{"sound": "knock_3", "at": 0.2}],
   "layers": [{"cycle": "boy_hoodie/flashlight_walk", "x": [0.1, 0.5], "y": "floor", "face": "auto"}]}]}
```

Danh sách đầy đủ các khoá: đầu file `tools/render.py`.

## Asset

- `assets/characters/<nhân vật>/` sprite PNG + `meta.json` (mô tả, tag, hướng quay, điểm neo, chu kỳ)
- `assets/backgrounds/` phông + `meta.json` (đường sàn, điểm nóng như `door_handle`)
- `assets/audio/sfx/` âm thanh + `meta.json`

Hình ảnh được tạo bằng Google Gemini; âm thanh được tạo bằng ElevenLabs Sound Effects. Ảnh gốc chưa cắt (`assets/source/`) không có trong repo, nên muốn cắt lại sheet cũ cần ảnh gốc.
