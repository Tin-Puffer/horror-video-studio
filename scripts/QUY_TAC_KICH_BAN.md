# Quy tắc viết kịch bản — Horror Video Studio

Bộ quy tắc đã thống nhất giữa người dùng và Claude (2026-10-29). Mọi kịch bản mới **bắt buộc** theo.
Bắt đầu từ `templates/kich_ban_mau.json`; kiểm tra bằng `python3 tools/check_story.py` (tự cảnh báo vi phạm).

## 1. Kịch bản là nguồn sự thật duy nhất
- File JSON quyết định **mọi** cấu hình, vị trí, kích thước: `settings` (video, giọng, thời gian, âm thanh, phụ đề, giao diện điện thoại…), `characters`, từng cảnh, từng lớp. Không gắn cứng trong code.
- Kịch bản **tự chứa đủ**: nhúng định nghĩa các giọng đang dùng vào `voice_presets`, có đủ khối `settings.audio`, `settings.timing`, `settings.subtitles`.
- Sự thật về asset (hướng quay, điểm neo, chu kỳ, điểm nóng, đường sàn) nằm ở `meta.json` của kho — kịch bản chỉ gọi tên.
- Đường dẫn công cụ của máy chỉ nằm trong `config.local.json`.

## 2. Asset: dùng lại trước, thiếu thì yêu cầu
- Đọc `assets/CATALOG.md` (bản ngắn) trước khi viết, rồi `assets/catalog/<nhân vật>.md` của các nhân vật truyện dùng; ảnh `assets/catalog/*.png` chỉ xem khi cần. Ưu tiên tối đa asset có sẵn.
- Thiếu thì khai báo `asset_requests` (gom ít sheet nhất):
  - **sheet nhân vật** 2×3, `pose` tiếng Anh, `desc`/`tags` tiếng Việt, `facing`, `anchors_needed`; prompt luôn kèm style prompt + ảnh tham chiếu của nhân vật.
  - **chu kỳ chuyển động ≥ 4–6 khung khác nhau rõ rệt**, cùng cỡ, cùng đường chân.
  - **phông** 16:9, không người, tông xanh-xám đêm, nét sáp màu; chừa sàn trống; không vẽ thứ mà sprite đã có (vd giường).
  - **âm thanh**: `prompt` tiếng Anh cho ElevenLabs + `length` + `search` (từ khoá Pixabay/Freesound) + `desc` tiếng Việt.
  - Nhân vật mới: không mặc đồ trắng (bị cắt nhầm thành nền).
- Gemini hay vẽ ngược hướng/khác yêu cầu → khi nạp phải xem lại và ghi `facing` theo hình thật.

## 3. Lời kể (giọng đọc + phụ đề)
- Ngôi thứ nhất, giọng kể chuyện kinh dị; **câu dài, liền mạch, có câu nối và chi tiết miêu tả** (cảm giác, âm thanh, ánh sáng).
- Mỗi cảnh 1–2 câu, tối đa khoảng **35–40 chữ**.
- **Không chèn `[n]` giữa câu.** Mỗi chỗ cắt bị đọc như hết câu → chữ cuối nặng, rời rạc. Chỉ dùng nghỉ **≥ 0.5s** cho nhịp kịch tính (trước câu của ma, sau một tiết lộ).
- **Tiếng động thì dùng âm thanh, không đọc thành lời** ("Cốc. Cốc. Cốc." → `sfx: knock_3`, cảnh không lời).
- **Chỉ một giọng: người kể ở ngôi thứ nhất** (quy tắc bổ sung 2026-10-29). Không dùng giọng riêng cho mẹ, ma,
  giọng qua điện thoại hay bất kỳ ai khác — không `{"say", "voice"}`, không `scene.voice`.
  Lời của người khác được người kể **thuật lại** trong câu kể, ví dụ: *"…giọng mẹ vang lên từ bên kia cánh cửa,
  bảo tôi mau mở cửa vì ngoài trời lạnh lắm."* hoặc trích ngắn trong câu: *"…một giọng khàn đặc thì thầm bảo tôi ra mở cửa."*
  Không khí rợn người (giọng méo, thì thầm) tạo bằng âm thanh (`whisper_eerie`, `breath_close`…) chứ không bằng đổi giọng.
- Tốc độ đạt yêu cầu: **~3.5–4.6 chữ/giây** mỗi cảnh (trừ câu ma cố ý chậm).

## 4. Giọng mặc định (đã chốt — demo 18)
- `settings.voice`: `{"preset": "clone_ke_chuyen", "merge_pause_below": 0.45, "trim_chunks": true, "chunk_gap": 0.12, "max_inner_pause": 0.18, "split_sentences": true}`
  (đọc từng câu; sau khi dựng chạy `tools/check_voice.py --fix` để nghe lại và đọc lại câu lỗi)
- `clone_ke_chuyen` = giọng clone (VieNeu), `tempo` 1.15, `soften_endings` "all".
- Kịch bản chỉ nhúng đúng một giọng trong `voice_presets`: `clone_ke_chuyen`.
- Clone giọng người khác chỉ khi người dùng xác nhận đã được phép.

## 5. Hoạt cảnh
- **Di chuyển luôn dùng chu kỳ** (`cycle`: walk, run, tiptoe, flashlight_walk, back_walk; ma: walk) — không cho ảnh tĩnh trượt ngang.
- Hướng: dùng `"face": "auto"` (hoặc left/right), **không dùng `flip`**.
- Tốc độ khớp bước chân: đi ≈ 0.12–0.2 khung/giây, chạy ≥ 0.3 khung/giây (đơn vị: chiều ngang khung hình).
- **Liên tục giữa các cảnh**: nhân vật bắt đầu đúng chỗ cảnh trước để lại; thứ đang đuổi theo thì vẫn ở trong khung.
- Đứng yên có `breathe` (mặc định của nhân vật); đang run sợ thì `jitter`.
- Chạm vật trên phông dùng `pin` + điểm nóng (`door_handle`…). Tỉ lệ chibi: tay ngang ngực không với tới tay nắm cửa ở góc toàn thân → dùng dáng giơ tay (K1/K2).
- Nhân vật đứng sàn: `"y": "floor"`.

## 6. Camera
- Dùng mốc `camera.keys` (p, zoom, x, y, ease). **Lia trái/phải/lên/xuống cần zoom ≥ 1.15** (khung không ra ngoài phông).
- `handheld` 4–9 cho cảnh căng thẳng; đẩy vào chậm-nhanh dần (`ease: in`) trước khi hù.
- Jumpscare: `fade_in: 0`, `flash`, `shake` mạnh, sfx `ghost_stinger` (volume 1.6–2.4).

## 7. Âm thanh
- Mọi cảnh có âm thanh không khí hoặc tiếng động khớp hành động (bước chân, tim đập, đồng hồ…); âm lặp có `loop` + `length`.
- Nhạc nền `drone_low` theo đoạn (`music`), **cố ý cắt nhạc** ở khoảnh khắc im lặng/tiết lộ, tự nhỏ khi có lời đọc.
- `settings.audio`: `normalize_db` −18, `trim_silence` true, `limiter_ceiling_db` −2. Âm lượng tương đối chỉnh bằng `volume` từng cue.

## 8. Thời gian & phụ đề
- `settings.timing`: `lead` 0.25, `tail` 0.45 (khoảng lặng giữa cảnh ngắn).
- `settings.subtitles`: `split` "sentence" (từng câu, tối đa 2 dòng, chạy theo giọng).

## 9. Quy trình làm việc
1. `tools/catalog.py` → đọc mục lục → viết kịch bản từ mẫu.
2. `tools/check_story.py` (hết LỖI, xử lý cảnh báo quy tắc) → `tools/story_md.py` (bản đọc được).
3. Dựng nháp bằng `--preview`: **chất lượng thật thấp** (640×360, 10 fps) và **số cảnh `#21` ở góc** để người dùng góp ý theo số cảnh (`settings.preview` trong mẫu; bản Full HD không có số). **Tự kiểm tra trước khi báo**: xem khung hình (ffmpeg), đo **cao độ giọng** trong video, **chữ/giây** từng cảnh, **độ to** các tiếng quan trọng, đỉnh ≤ −1 dB.
4. Sao lưu kịch bản vào `build/backups/` trước khi sửa lớn.
5. Người dùng nói "không dựng lại video" thì chỉ sửa kịch bản/asset. Người dùng tự xuất trong Studio.
