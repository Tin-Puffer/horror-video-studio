# Người đứng cuối hành lang

**Tổng thời lượng:** 109s (1.8 phút) · 19 cảnh

> 3 giờ sáng, Khoa ra bếp uống nước và thấy một người mặc áo của mẹ đứng cuối hành lang. Mỗi lần đèn pin chớp tắt, nó lại gần hơn. Cậu khoá mình trong phòng — nhưng thứ đó chưa bao giờ ở ngoài cửa.

_Tự sinh từ `nguoi_dung_cuoi_hanh_lang.json` bằng `tools/story_md.py` — sửa JSON (hoặc Studio) rồi chạy lại._

- 🎵 Nhạc nền `drone_low`: cảnh 0 → 12, âm lượng 0.8, tự nhỏ lại khi có lời đọc
- 🎵 Nhạc nền `drone_low`: cảnh 14 → 16, âm lượng 0.6, tự nhỏ lại khi có lời đọc

## Cảnh 0 — black  ·  0.0s → 4.0s (4.0s)

**Chữ trên màn hình:** NGƯỜI ĐỨNG CUỐI HÀNH LANG
**Camera:** Máy đứng yên, toàn cảnh.

## Cảnh 1 — bg1_bedroom  ·  4.0s → 10.3s (6.3s)

**Lời đọc:** Đêm đó, _(nghỉ 0.3s)_ tôi tỉnh dậy vì khát nước. _(nghỉ 0.6s)_ Đồng hồ chỉ đúng ba giờ sáng.
**Camera:** 0.0s: khung cận x1.25 vào bên phải; đến 3.4s: giữ khung; 3.4–6.3s: đẩy vào x1.45, lia trái, ngước máy lên (mượt).
**Âm thanh:** 0.0s `clock_tick` (lặp 8s)
- `boy_hoodie/G1_bed_sleeping` (Ngủ trên giường (sprite có giường)), đứng bên phải, xuất hiện 0→0.5 của cảnh
- `boy_hoodie/G2_bed_wake_startled` (Giật mình ngồi dậy trên giường), đứng bên phải, xuất hiện 0.5→1 của cảnh

## Cảnh 2 — bg1_bedroom  ·  10.3s → 16.0s (5.7s)

**Lời đọc:** Mẹ tôi đi công tác. _(nghỉ 0.5s)_ Cả căn nhà… _(nghỉ 0.3s)_ chỉ còn mỗi mình tôi.
**Camera:** 0.0s: khung cận x1.3 vào bên phải; đến 2.0s: giữ khung; 2.0–5.7s: lia trái (mượt).
**Âm thanh:** 2.6s `floor_creak` · 4.6s `floor_creak`
- `boy_hoodie/G4_rub_sleepy_eyes` (Đứng dụi mắt ngái ngủ), đứng bên phải, xuất hiện 0→0.35 của cảnh
- chu kỳ `boy_hoodie/tiptoe`, di chuyển phải → trái, xuất hiện 0.35→1 của cảnh, hướng auto

## Cảnh 3 — bg2_hallway  ·  16.0s → 21.9s (5.9s)

**Lời đọc:** Hành lang tối om. _(nghỉ 0.5s)_ Tôi bật đèn pin, _(nghỉ 0.3s)_ rón rén đi về phía bếp.
**Camera:** 0.0s: khung cận x1.2 vào bên trái; 0.0–5.9s: lia phải (mượt); rung tay nhẹ (5).
**Âm thanh:** 0.2s `flashlight_click` · 0.6s `footsteps_slow` (lặp 5s)
- chu kỳ `boy_hoodie/flashlight_walk`, di chuyển trái → giữa, hướng auto

## Cảnh 4 — bg2_hallway  ·  21.9s → 29.9s (8.1s)

**Lời đọc:** Và rồi… _(nghỉ 0.6s)_ tôi thấy nó. _(nghỉ 0.6s)_ Ở cuối hành lang, _(nghỉ 0.4s)_ có ai đó đang đứng quay lưng về phía tôi.
**Camera:** 0.0s: khung toàn cảnh; đến 3.6s: giữ khung; 3.6–8.1s: đẩy vào x1.9, lia phải, hạ máy xuống (chậm rồi nhanh dần).
**Âm thanh:** 2.0s `heartbeat` (lặp 6s) · 4.8s `reverse_swell`
- `ghost_mother/GH9_back_stand` (Quay lưng đứng), đứng bên phải
- `boy_hoodie/L2_flashlight_point_far` (Đứng yên giơ đèn pin soi xa phía trước), đứng bên trái

## Cảnh 5 — bg2_hallway  ·  29.9s → 36.1s (6.1s)

**Lời đọc:** Tóc dài. _(nghỉ 0.5s)_ Áo len màu be. _(nghỉ 0.6s)_ Giống hệt chiếc áo mẹ tôi hay mặc.
**Camera:** 0.0s: khung cận x1.9 vào bên phải; 0.0–6.1s: đẩy vào x2.1, lia phải, ngước máy lên (mượt).
**Hiệu ứng:** đèn chập chờn 0.12
**Âm thanh:** 0.9s `flicker_buzz` · 0.0s `heartbeat` (lặp 6s)
- `ghost_mother/GH9_back_stand` (Quay lưng đứng), đứng bên phải

## Cảnh 6 — bg2_hallway  ·  36.1s → 40.7s (4.7s)

**Lời đọc:** Mẹ… _(nghỉ 0.4s)_ mẹ về rồi à? _(nghỉ 0.5s)_ Tôi thì thầm.
**Camera:** 0.0s: khung toàn cảnh; 0.0–4.7s: đẩy vào x1.08 (mượt); rung tay nhẹ (4).
**Âm thanh:** 0.0s `breath_close`
- `boy_hoodie/D5_face_whisper_scared` (Cận mặt, thì thầm sợ hãi, mồ hôi), đứng bên giữa

## Cảnh 7 — bg2_hallway  ·  40.7s → 49.3s (8.6s)

**Lời đọc:** Đèn pin chớp tắt. _(nghỉ 0.6s)_ Khi nó sáng lại… _(nghỉ 0.6s)_ người đó đã quay mặt về phía tôi. _(nghỉ 0.5s)_ Và đứng gần hơn.
**Camera:** 0.0s: khung cận x1.25 vào bên phải; đến 3.4s: giữ khung; 3.4–3.9s: đẩy vào x1.45, lia phải (nhanh rồi chậm dần); 3.9–8.6s: đẩy vào x1.5 (mượt).
**Hiệu ứng:** chớp trắng 3.6s, đèn chập chờn 0.45
**Âm thanh:** 2.6s `flicker_buzz` · 3.6s `ghost_stinger`
- `ghost_mother/GH9_back_stand` (Quay lưng đứng), đứng bên phải, xuất hiện 0→0.42 của cảnh
- `ghost_mother/GH1_stand_far_head_bowed` (Đứng xa, cúi đầu, tóc che kín mặt), đứng bên phải, xuất hiện 0.42→1 của cảnh, viền sáng

## Cảnh 8 — bg2_hallway  ·  49.3s → 54.6s (5.3s)

**Lời đọc:** Nó bắt đầu bước tới. _(nghỉ 0.5s)_ Chậm rãi. _(nghỉ 0.5s)_ Từng bước một.
**Camera:** 0.0s: khung cận x1.2 vào bên giữa; 0.0–5.3s: đẩy vào x1.35, lia trái (chậm rồi nhanh dần).
**Âm thanh:** 0.3s `footsteps_slow` (lặp 5s) · 0.0s `heartbeat` (lặp 6s)
- `boy_hoodie/L3_freeze_flashlight_off` (Đứng đơ người, đèn pin đã tắt hạ xuống), đứng bên trái, run rẩy
- chu kỳ `ghost_mother/walk`, di chuyển phải → giữa, viền sáng, hướng auto

## Cảnh 9 — bg2_hallway  ·  54.6s → 57.8s (3.2s)

**Lời đọc:** Tôi quay đầu… _(nghỉ 0.2s)_ bỏ chạy.
**Camera:** 0.0s: khung cận x1.2 vào bên giữa; 0.0–3.2s: đẩy vào x1.28, lia trái (mượt); rung tay nhẹ (9).
**Âm thanh:** 0.6s `footsteps_run`
- chu kỳ `ghost_mother/walk`, di chuyển giữa → giữa, viền sáng, hướng auto
- `boy_hoodie/L3_freeze_flashlight_off` (Đứng đơ người, đèn pin đã tắt hạ xuống), đứng bên trái, xuất hiện 0→0.18 của cảnh, run rẩy
- chu kỳ `boy_hoodie/run`, di chuyển trái → trái, xuất hiện 0.18→0.75 của cảnh, hướng auto

## Cảnh 10 — bg1_bedroom  ·  57.8s → 62.2s (4.3s)

**Lời đọc:** Tôi đóng sầm cửa phòng, _(nghỉ 0.3s)_ áp lưng vào cánh cửa.
**Camera:** 0.0s: khung cận x1.35 vào bên trái; 0.0–4.3s: kéo ra x1.25, lia phải, hạ máy xuống (nhanh rồi chậm dần); rung tay nhẹ (5).
**Hiệu ứng:** rung 10px (0.0–0.5s)
**Âm thanh:** 0.0s `door_slam`
- `boy_hoodie/L4_back_against_door` (Đứng chính diện nhắm chặt mắt, tay xoè (dùng như áp lưng vào cửa)), đứng bên trái

## Cảnh 11 — bg1_bedroom  ·  62.2s → 74.7s (12.5s)

**Lời đọc:** Cốc. _(nghỉ 0.5s)_ Cốc. _(nghỉ 0.5s)_ Cốc. _(nghỉ 0.6s)_ Ngoài cửa, giọng mẹ tôi vang lên: _(nghỉ 0.5s)_ Khoa ơi… _[giọng vn_ma_me]_ _(nghỉ 0.7s)_ mở cửa… _[giọng vn_ma_me]_ _(nghỉ 0.5s)_ cho mẹ. _[giọng vn_ma_me]_
**Camera:** 0.0s: khung cận x1.25 vào bên trái; 0.0–12.5s: đẩy vào x1.45, lia trái, ngước máy lên (mượt).
**Hiệu ứng:** rung 4px (0.2–2.7s)
**Âm thanh:** 0.2s `knock_3` · 3.7s `heartbeat` (lặp 6s)
- `boy_hoodie/L4_back_against_door` (Đứng chính diện nhắm chặt mắt, tay xoè (dùng như áp lưng vào cửa)), đứng bên trái, run rẩy

## Cảnh 12 — bg1_bedroom  ·  74.7s → 81.2s (6.5s)

**Lời đọc:** Tay nắm cửa bắt đầu xoay. _(nghỉ 0.5s)_ Tôi trượt người xuống, _(nghỉ 0.3s)_ dùng hết sức ghì chặt cánh cửa.
**Camera:** 0.0s: khung cận x1.2 vào bên trái; 0.0–6.5s: đẩy vào x1.6, lia trái (chậm rồi nhanh dần).
**Hiệu ứng:** rung 5px (0.3–5.9s)
**Âm thanh:** 0.3s `door_handle_rattle` (lặp 4s) · 3.6s `knock_3`
- `boy_hoodie/K6_slide_down_door` (Tựa lưng vào cửa trượt xuống, kinh hãi), đứng bên trái, run rẩy

## Cảnh 13 — bg1_bedroom  ·  81.2s → 85.2s (4.0s)

**Lời đọc:** Rồi… _(nghỉ 0.8s)_ mọi thứ im bặt.
**Camera:** 0.0s: khung toàn cảnh; 0.0–4.0s: đẩy vào x1.05 (mượt).
- chu kỳ `boy_hoodie/blink`, đứng bên giữa

## Cảnh 14 — bg1_bedroom  ·  85.2s → 90.2s (5.0s)

**Lời đọc:** Tôi ngồi trùm chăn ở góc phòng rất lâu. _(nghỉ 0.5s)_ Không dám thở mạnh.
**Camera:** 0.0s: khung cận x1.1 vào bên giữa; 0.0–5.0s: đẩy vào x1.3, hạ máy xuống (mượt).
**Âm thanh:** 0.0s `clock_tick` (lặp 8s)
- `boy_hoodie/L5_peek_from_blanket` (Ngồi trùm chăn kín người, chỉ lộ đôi mắt), đứng bên phải

## Cảnh 15 — bg1_bedroom  ·  90.2s → 96.6s (6.3s)

**Lời đọc:** Rồi tôi nghe thấy tiếng thì thầm. _(nghỉ 0.6s)_ Nhưng nó không phát ra… _(nghỉ 0.4s)_ từ ngoài cửa.
**Camera:** 0.0s: khung cận x1.3 vào bên giữa; 0.0–6.3s: đẩy vào x1.5, ngước máy lên (chậm rồi nhanh dần); rung tay nhẹ (3).
**Âm thanh:** 0.9s `whisper_eerie` · 3.2s `breath_close`
- `boy_hoodie/L6_slow_turn_head` (Quay lưng, từ từ ngoái đầu qua vai (nhìn sang phải)), đứng bên giữa

## Cảnh 16 — bg1_bedroom  ·  96.6s → 100.7s (4.2s)

**Lời đọc:** Mà là từ… _(nghỉ 0.7s)_ ngay phía trên đầu tôi.
**Camera:** 0.0s: khung cận x1.35 vào bên giữa; đến 1.7s: giữ khung; 1.7–4.2s: ngước máy lên (chậm rồi nhanh dần).
**Âm thanh:** 1.5s `reverse_swell`
- `boy_hoodie/L1_look_up_terrified` (Ngửa mặt nhìn lên trần, kinh hãi), đứng bên giữa

## Cảnh 17 — bg1_bedroom  ·  100.7s → 102.9s (2.2s)

**Camera:** 0.0s: khung toàn cảnh; 0.0–0.6s: đẩy vào x1.18 (nhanh rồi chậm dần); 0.6–2.2s: đẩy vào x1.22 (mượt).
**Hiệu ứng:** rung 16px (0.0–1.1s), chớp trắng 0.1s
**Âm thanh:** 0.0s `ghost_stinger`
- `ghost_mother/GH12_upside_down_head` (Đầu treo ngược từ trên xuống), đứng bên giữa, xuất hiện 0→0.35 của cảnh, viền sáng
- `ghost_mother/GH12_upside_down_head` (Đầu treo ngược từ trên xuống), đứng bên giữa, xuất hiện 0.35→1 của cảnh, viền sáng, run rẩy

## Cảnh 18 — black  ·  102.9s → 108.8s (5.9s)

**Lời đọc:** Có những thứ… _(nghỉ 0.6s)_ đã ở trong nhà… _(nghỉ 0.5s)_ từ trước khi bạn khoá cửa.
**Chữ trên màn hình:** Có những thứ… đã ở trong nhà từ trước khi bạn khoá cửa.
**Camera:** Máy đứng yên, toàn cảnh.
