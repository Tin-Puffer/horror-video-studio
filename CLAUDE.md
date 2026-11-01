# Horror Video Tool

Làm video hoạt hình kinh dị kể chuyện (tiếng Việt) từ sprite vẽ tay nét sáp màu do Gemini tạo.
Kho asset tăng liên tục — luôn làm việc dựa trên mục lục, không dựa trí nhớ.

## QUY TẮC KỊCH BẢN (bắt buộc)
Mọi kịch bản mới theo **`scripts/QUY_TAC_KICH_BAN.md`** (đã thống nhất với người dùng) và bắt đầu từ
**`templates/kich_ban_mau.json`** (có sẵn mọi thiết lập đã chốt). `tools/check_story.py` tự cảnh báo vi phạm
(dòng "quy tắc:") — phải xử lý hết trước khi giao.

## Máy mới (làm đầu tiên)
1. `python3 tools/doctor.py` — liệt kê thứ còn thiếu kèm cách sửa (Python libs, ffmpeg, font, config.local.json,
   Dubber + VieNeu, đọc thử giọng kể). Cài/sửa từng mục, chạy lại tới khi "máy sẵn sàng".
2. Dubber (chứa VieNeu-TTS) là dự án riêng của người dùng, không nằm trong repo này — hỏi người dùng nơi lấy.
3. Kiểm tra: `python3 tools/check_story.py scripts/cuoc_goi_3h.json` rồi `python3 tools/render.py scripts/cuoc_goi_3h.json --preview --scenes 1-3`.

## Dùng AI / máy khác
- Viết kịch bản bằng AI khác: `python3 tools/make_brief.py` → gửi `build/brief.zip` (hoặc BRIEF_VIET_KICH_BAN.md + ảnh).
- Máy khác: clone repo, cài Python/ffmpeg/piper/VieNeu (Dubber), tạo `config.local.json`. Giọng clone có sẵn trong
  `assets/voices/vieneu/` (chỉ voice.json + meta.json, không có bản ghi gốc) — worker tự đọc từ đó.

## Nguyên tắc
- **Kịch bản JSON quyết định mọi cấu hình, vị trí, kích thước** (settings / characters / scenes / layers).
  `tools/render.py` chỉ là bộ máy; không thêm hằng số cố định vào code — thêm khoá cấu hình có giá trị mặc định trong `DEFAULTS`.
- Sự thật về asset (mô tả, tag, hướng quay, điểm neo, chu kỳ, điểm nóng của phông) nằm trong `meta.json`, không nằm trong kịch bản.
- Trao đổi với người dùng bằng tiếng Việt.

## Viết kịch bản mới (video thật)
1. `python3 tools/catalog.py`, rồi đọc `assets/CATALOG.md` (bản ngắn: nhân vật + chu kỳ, phông + tên điểm nóng, âm thanh).
   Chỉ mở `assets/catalog/<nhân vật>.md` của nhân vật truyện dùng (và `backgrounds.md` khi cần toạ độ/floor_y);
   `PROMPTS.md` chỉ khi viết `asset_requests`. Ảnh `assets/catalog/*.png` chỉ xem khi mô tả chữ chưa đủ — không đọc cả kho.
2. Viết `scripts/<truyen>.json`, copy từ `templates/kich_ban_mau.json` (ví dụ đầy đủ: `scripts/cuoc_goi_3h.json`). Ưu tiên dùng lại asset có sẵn:
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
   Yêu cầu được xếp theo **đợt** (yêu cầu dùng ảnh của yêu cầu khác làm tham chiếu — `refs` trỏ tới file sẽ được tạo, base của
   nhân vật mới, hoặc `"after"` — tự sang đợt sau). `build/<truyen>_refs/<nn>_<id>/`: ảnh tham chiếu đánh số `1_…, 2_…` (prompt gọi
   "attached image 2"); mục chưa tới đợt chỉ có prompt.txt ghi rõ chờ gì — không chép ảnh thay thế. Nạp xong một đợt thì chạy lại check_story.
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

## Giọng đọc
- **Mặc định:** preset `clone_ke_chuyen` (giọng clone người dùng chốt, bản demo 18: tempo 1.15, soften_endings "all").
- **Cách viết lời kể (người dùng yêu cầu):** câu dài, liền mạch, có câu nối và miêu tả; KHÔNG chèn [n] giữa câu
  (mỗi chỗ cắt bị đọc như hết câu → chữ cuối nặng, rời rạc). Chỉ dùng nghỉ ≥ 0.5s cho khoảnh khắc kịch tính (câu của ma).
- Bộ bảo vệ VieNeu trong render.py: gộp nghỉ ngắn (merge_pause_below), chống đọc lan man (max_sec_per_word),
  nén lặng giữa câu (max_inner_pause), đọc từng câu một (`split_sentences`: VieNeu tự chặt đoạn dài giữa cụm từ và hay
  lặp/nuốt chữ khi câu dài; câu > `max_chunk_chars` cắt ở dấu phẩy). Sau khi đổi giọng/lời: đo chữ/giây từng cảnh
  (~3.5–4.6 là ổn) và cao độ trong video.
- **Nghe lại trước khi giao preview:** `python3 tools/check_voice.py scripts/<truyen>.json --fix` — chuyển giọng thành chữ
  (PhoWhisper qua Python của Dubber, `tools/asr_worker.py`), so với lời kịch bản, câu lệch/lặp/kéo dài thì đọc lại (VieNeu mỗi
  lần đọc một khác) và giữ bản sát nhất → `build/<truyen>_voice_check.md`. Câu còn báo lỗi thì xem cột "Nghe được":
  công cụ nghe nhầm chữ lặp có chủ ý (tích tắc tích tắc) thì bỏ qua.
- Giọng mẫu có tên: `assets/audio/voice_presets.json` (model, length_scale, noise_scale, noise_w, sentence_silence, pitch, reverb, lowpass, volume).
- Kịch bản: `settings.voice` / `scene.voice` / từng câu `{"say": "...", "voice": {"preset": "ma_me"}}`; `[0.6]` trong lời = nghỉ 0.6s.
- Engine: `piper` (nhanh, chỉnh tốc độ bằng length_scale) hoặc `vieneu` (VieNeu-TTS của Dubber: 25 giọng có sẵn
  `preset:<tên>` + giọng clone; tốc độ chỉnh bằng `tempo`). VieNeu chạy qua `tools/vieneu_worker.py` bằng Python của Dubber
  (`vieneu_python`, `dubber_root` trong config.local.json). Mọi câu được đưa về `voice.sample_rate` (44.1 kHz).
- Clone giọng: `python3 tools/clone_voice.py <file> "<Tên>" [--start giây]` (lấy 3–8s sạch, một người nói, không nhạc)
  → lưu vào thư viện giọng của Dubber + thêm preset vào voice_presets.json. Chỉ clone giọng của người đã đồng ý.
- So sánh giọng: sửa `assets/audio/voice_demos.json` rồi `python3 tools/voice_demo.py` → `build/voice_demos/*.mp3`.

## Dựng video
- `python3 tools/render.py scripts/<truyen>.json [--preview] [--scenes 7-13.5] [--no-subtitles]` → `build/`.
- **Bản preview gửi người dùng góp ý (bắt buộc):** chất lượng thật thấp (`settings.preview`: 640×360, 10 fps, crf 34, âm 64k)
  và số cảnh ở góc trái trên (`#21`, khoá `preview.scene_label`) để người dùng góp ý theo số cảnh. Bản Full HD không có số cảnh.
- Giọng: piper (đường dẫn trong `config.local.json`, không lên git), người dùng chọn `ngochuyennew` đọc tất cả. Âm thanh SFX/nhạc người dùng tự thêm sau.
- Sau khi dựng: trích khung hình bằng ffmpeg và tự xem trước khi báo người dùng.

## Bản đồ thư mục
- `assets/audio/sfx/` âm thanh + `assets/audio/meta.json` · `assets/source/` ảnh gốc (không sửa) · `assets/characters/<char>/` sprite + `meta.json` · `assets/backgrounds/` phông + `meta.json`
- `tools/` cut_sprites, prep_backgrounds, catalog, check_story, ingest, render, studio · `scripts/` kịch bản + prompt · `build/` đầu ra
- `assets/retired.json`: asset đã xoá có chủ ý (không video nào dùng) — check_story coi yêu cầu cũ là xong, cut_sprites/prep_backgrounds không tạo lại. Dọn kho: chỉ bỏ thứ không kịch bản nào dùng (đếm cả `sprite`, `cycle`, `frames`, `bg`, `sound`).
