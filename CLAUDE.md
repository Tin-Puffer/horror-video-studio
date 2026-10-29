# Horror Video Tool

Làm video hoạt hình kinh dị kể chuyện (tiếng Việt) từ sprite vẽ tay nét sáp màu do Gemini tạo.
Kho asset tăng liên tục — luôn làm việc dựa trên mục lục, không dựa trí nhớ.

## Nguyên tắc
- **Kịch bản JSON quyết định mọi cấu hình, vị trí, kích thước** (settings / characters / scenes / layers).
  `tools/render.py` chỉ là bộ máy; không thêm hằng số cố định vào code — thêm khoá cấu hình có giá trị mặc định trong `DEFAULTS`.
- Sự thật về asset (mô tả, tag, hướng quay, điểm neo, chu kỳ, điểm nóng của phông) nằm trong `meta.json`, không nằm trong kịch bản.
- Trao đổi với người dùng bằng tiếng Việt.

## Viết kịch bản mới (video thật)
1. `python3 tools/catalog.py`, rồi đọc `assets/CATALOG.md` và xem ảnh `assets/catalog/*.png`.
2. Viết `scripts/<truyen>.json` (mẫu: `scripts/cuoc_goi_3h.json`). Ưu tiên dùng lại asset có sẵn:
   `"cycle": "boy_hoodie/walk"` cho di chuyển, `"face": "auto"`, `"y": "floor"`,
   `"pin": {"point": "hand", "at": "<hotspot>"}` khi tay phải chạm vật trên phông.
   Lưu ý tỉ lệ chibi: tay ngang ngực không với tới tay nắm cửa ở góc toàn thân (dùng K1/K2 giơ tay lên).
   Viết chi tiết: camera theo mốc `"camera": {"keys": [{"p","zoom","x","y","ease"}], "handheld": n}` (lia cần zoom > 1),
   âm thanh từng cảnh `"sfx": [{"sound","at","volume","loop","length"}]`, nhạc nền `"music"` ở cấp kịch bản (tự nhỏ khi có lời đọc).
3. Thứ gì chưa có → thêm vào `"asset_requests"` (sheet 2x3 cho nhân vật có sẵn, background, character_base cho nhân vật mới);
   viết `pose`/`scene`/`design` bằng tiếng Anh, `desc`/`tags` tiếng Việt, ghi `facing`, `anchors_needed`, `hotspots_needed`.
   Âm thanh thiếu → `"kind": "sound"` với `search` (từ khoá tiếng Anh cho Pixabay/Freesound), `sound_kind` sfx|music.
   Gom yêu cầu thành ít sheet nhất; chu kỳ chuyển động cần ≥ 4 khung khác nhau rõ rệt.
4. `python3 tools/check_story.py scripts/<truyen>.json` → phải hết LỖI; danh sách prompt cho người dùng ở `build/<truyen>_requests.md`.
5. `python3 tools/story_md.py scripts/<truyen>.json` → bản kịch bản đọc được `scripts/<truyen>.md` (tự sinh, không sửa tay).
6. Có thể dựng nháp ngay khi chưa đủ asset (khung giữ chỗ, âm thanh thiếu phát tiếng bíp): `python3 tools/render.py scripts/<truyen>.json --preview`.

## Khi người dùng gửi ảnh mới
1. Ảnh thuộc yêu cầu nào → `python3 tools/ingest.py scripts/<truyen>.json <request_id> <ảnh>`.
   Ảnh không thuộc yêu cầu nào → thêm mục vào `tools/sprites.json` + `meta.json` như ingest làm.
2. Xem kết quả cắt trên nền tối (và nền đỏ để soi lỗ thủng); xử lý: `light_beams` (vệt đèn pin), `clear_white` (giấy kẹt giữa tóc).
3. Ghi `facing` đúng theo hình thật (Gemini hay vẽ ngược hướng yêu cầu), đo `anchors`/`hotspots` còn thiếu.
4. Phông nền: `tools/prep_backgrounds.py` xoá logo Gemini; sửa chi tiết sai (vd đồng hồ) trong `FIXES`.
5. `python3 tools/catalog.py` — hết dòng "chưa có mô tả".

## Giao diện (Horror Video Studio)
- `python3 tools/studio.py` hoặc bấm đúp `studio.command` → http://localhost:8765 (stdlib, không cần cài gì).
- `tools/studio.py` (API: kịch bản, catalog, xem trước 1 khung bằng chính render.py, kiểm tra, xuất video) + `tools/studio.html` (giao diện).
- Thêm tính năng render mới → thêm điều khiển tương ứng trong studio.html; khoá lạ vẫn sửa được qua "JSON lớp/cảnh".

## Dựng video
- `python3 tools/render.py scripts/<truyen>.json [--preview] [--scenes 7-13.5] [--no-subtitles]` → `build/`.
- Giọng: piper (đường dẫn trong `config.local.json`, không lên git), người dùng chọn `ngochuyennew` đọc tất cả. Âm thanh SFX/nhạc người dùng tự thêm sau.
- Sau khi dựng: trích khung hình bằng ffmpeg và tự xem trước khi báo người dùng.

## Bản đồ thư mục
- `assets/audio/sfx/` âm thanh + `assets/audio/meta.json` · `assets/source/` ảnh gốc (không sửa) · `assets/characters/<char>/` sprite + `meta.json` · `assets/backgrounds/` phông + `meta.json`
- `tools/` cut_sprites, prep_backgrounds, catalog, check_story, ingest, render, studio · `scripts/` kịch bản + prompt · `build/` đầu ra
