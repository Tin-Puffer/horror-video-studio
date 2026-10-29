# Hướng dẫn dựng video

## Xuất video
```
python3 tools/render.py scripts/cuoc_goi_3h.json            # Full HD 1080p, ~3 phút
python3 tools/render.py scripts/cuoc_goi_3h.json --preview  # bản nháp 540p, ~1 phút
python3 tools/render.py scripts/cuoc_goi_3h.json --preview --scenes 16-19   # chỉ vài cảnh
python3 tools/render.py scripts/cuoc_goi_3h.json --no-subtitles             # không phụ đề
```
Kết quả nằm trong `build/`. Giọng đọc được lưu cache ở `build/tts/`, nên sửa hình không phải tạo lại giọng.

## Sửa kịch bản
Mở `scripts/cuoc_goi_3h.json`. Mỗi cảnh có:
- `bg`: phông (bg1_bedroom, bg2_hallway, bg3_front_door, bg3b_peephole, black)
- `text`: lời đọc + phụ đề. Độ dài cảnh tự khớp với lời đọc
- `layers`: nhân vật. `sprite` = tên file trong assets/characters (không có .png),
  `x` = vị trí ngang (0 trái → 1 phải), `y` = chân nhân vật (0 trên → 1 dưới),
  `h` = chiều cao (tỉ lệ khung hình), `flip` = lật ngang, `start`/`end` = xuất hiện từ/đến (0→1 của cảnh).
  Giá trị dạng `[a, b]` = chuyển động từ a đến b (ví dụ `"x": [0.1, 0.6]` là đi sang phải).
  `frames` + `fps` = chuỗi khung (đi, chạy, nói, chớp mắt).
- Hiệu ứng: `camera` (zoom), `shake` (rung), `flash` (chớp trắng), `flicker` (đèn chập chờn), `bg_dim`.
Chi tiết đầy đủ: đầu file `tools/render.py`.

## Truyện mới
Copy file json, đổi `title`, `output` và các cảnh.
