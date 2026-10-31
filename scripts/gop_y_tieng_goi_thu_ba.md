# Góp ý chờ sửa — Tiếng gọi thứ ba

**Trạng thái: đã sửa cả 12 mục (2026-10-30), chờ người dùng duyệt bản nháp.**

Ghi lại góp ý của người dùng, sửa một lượt khi đã góp ý xong (sửa ở `scripts/gen_tieng_goi_thu_ba.py`, rồi chạy lại).

1. **Chữ "thưa" khó hiểu** (lượt 2: người dùng thấy vẫn tối nghĩa → bỏ hẳn chữ "thưa" trong lời đọc, thay bằng "đáp lại / lên tiếng / dạ" ở 14 cảnh): giữ chữ "thưa", nhưng giải thích một lần ở cảnh bà dặn luật (cảnh 12) bằng cách thêm
   *"…tuyệt đối đừng thưa, dù chỉ một tiếng dạ…"*. Rà lại cả truyện để chỗ nào "thưa" đứng một mình vẫn rõ nghĩa.
2. **Giọng đọc lỗi ở "hơi lạnh tanh tanh" (cảnh 7):** VieNeu đọc vấp ở từ láy lặp, câu lại kết thúc đúng chỗ đó.
   Viết lại cho tiếng cuối câu chắc, ví dụ *"…lùa vào khe cửa một luồng hơi lạnh mang theo mùi tanh của nước sông."*
   Cảnh 79 cũng kết bằng "tanh tanh" → sửa luôn, ví dụ *"…ngửi thấy thoang thoảng mùi tanh của bùn sông."*
   Sau khi sửa: nghe lại hai cảnh này trong bản nháp.
3. **Giọng kể cần to hơn:** tăng `settings.audio.narration_volume` (đang 1.0) và/hoặc hạ nền khi có lời
   (`duck` đang 0.35). Sau khi dựng: đo độ to lời kể so với nhạc/sfx, đỉnh vẫn ≤ −1 dB, không vỡ tiếng.
4. **Bà đi xuyên tường (cảnh 18, phòng ngủ, "Bà bảo cả đời bà vẫn tự hỏi…"; người dùng gọi là cảnh 15):**
   bà đang đi sang trái ra khỏi khung (x 0.55 → −0.15) xuyên qua tường. Sửa: đi tới cửa phòng (hotspot
   `bedroom_door` x ≈ 0.1–0.15) rồi dừng/biến mất ở cửa, cảnh kết bằng tối dần (`fade_out` ~1–1.5s) để chuyển cảnh.
   Rà các cảnh khác có nhân vật đi ra khỏi khung cũng xử lý tương tự (đi tới cửa/cổng + tối dần).
5. **Bàn thờ đang thờ ảnh mẹ (phông `bg5_altar_close` của Bát cơm thứ hai) — sai với truyện này.**
   Dùng ở cảnh 26 (bà thắp nhang), 76 (bát hương nguội), 81 (lọ dầu gió).
   - Phông mới: cận bàn thờ, ảnh thờ là **ông nội** (truyện đã nói "ông mất sớm"; bố còn sống ở Sài Gòn nên
     không thờ bố được), không băng tang mới, cùng bố cục bát hương/nến/chỗ trống phía trước để đặt đạo cụ.
   - Sprite mới cho cảnh 26: bà nhìn **từ phía sau, khung từ vai trở lên**, hai tay giơ ba nén nhang trước bàn thờ
     (đặt ở tiền cảnh, che một phần bàn thờ).
   - Cảnh 81 (lọ dầu gió): lọ dầu nằm trong ngăn kéo theo lời kể → cân nhắc đặt ở phông phòng ngủ thay vì bàn thờ.
   → thêm 2 yêu cầu asset (1 phông + 1 sprite), tạo thư mục ref như lần trước.
6. **Dãy dấu chân bùn đang đi NGƯỢC (đi ra xa, mũi chân hướng vào trong) — phải là đi từ cổng/bến sông VÀO nhà.**
   Sprite `props/HN4_muddy_footprints_trail`, dùng ở cảnh 29, 30, 60, 83, 84 — người dùng đã chỉ ra 29 và 83 (cảnh 84 là chi tiết then chốt
   "chỉ có một chiều đi lên").
   - Chính: yêu cầu asset mới — dãy dấu chân đi **về phía người xem**: mũi chân hướng xuống/về phía camera,
     dấu xa nhỏ ở trên, dấu gần to ở dưới, lệch trái–phải xen kẽ.
   - Dự phòng (không cần Gemini): ghép dãy từ `HN5_single_wet_footprint` (mũi chân hướng phải → ghi `facing`
     trong meta, dùng `face` để lật), đặt từ khe cổng (`gate_gap_floor`) xuống tiền cảnh, to dần.
   → gom chung lượt yêu cầu asset với mục 5.
7. **Cảnh 35 (nhìn qua mắt mèo): dấu chân hiện dần cũng ngược hướng và sai chỗ.** Hiện 3 dấu `HN5` mũi chân hướng
   sang phải, nằm giữa sân gần cổng. Phải là: từng dấu hiện lần lượt **từ khe cổng xuống dần phía dưới vòng
   mắt mèo (về phía cửa = về phía người xem)**, mũi chân hướng xuống/về camera, dấu sau to hơn dấu trước,
   trái–phải xen kẽ, dấu cuối sát mép dưới vòng tròn (như sắp chạm cửa) và vẫn nằm trong vòng mắt mèo (clip_circle).
   → asset mới: **một dấu chân trái + một dấu chân phải, mũi chân hướng về người xem** (gom cùng lượt mục 5–6);
   đo hotspot `lens_circle`, `yard_floor`, `gate` của `bg11_peephole_yard` để đặt cho chuẩn.
8. **Cảnh 74 & 75 (bữa cơm, bà giả `H4_sit_offer_food`): bà quá to.** Đang dùng `GMA_SEAT` h 0.55 (đo cho sprite mẹ
   của Bát cơm). Giảm về ngang tỉ lệ Khoa ngồi (~0.44–0.46), ghế đẩu của sprite trùm đúng ghế phải trên phông
   (hotspot `stool_right`), đầu bà thấp hơn hoặc ngang đầu Khoa. Kiểm tra lại cả hình nhân `HN1` đặt ở `GMA_SEAT` (cảnh 56–58).
9. **Cảnh 76 (bà không thắp hương nữa):** bổ sung mục 5 — phông bàn thờ hiện có sẵn 3 nén nhang **đang cháy** và thờ mẹ,
   mâu thuẫn với lời kể "bát hương nguội lạnh". Phông bàn thờ ông cần **2 bản cùng bố cục**:
   - `…_lit`: nhang đang cháy, khói (cảnh 26, lúc bà còn thắp hương);
   - `…_cold`: bát hương nguội, chỉ còn chân nhang cắm trơ trọi, không khói, nến tắt, hơi bụi (cảnh 76).
   Bỏ đạo cụ `DC4_incense_broken` (của Bát cơm) ở cảnh 76 nếu phông `_cold` đã thể hiện đủ.
10. **Cảnh 77 cần con mèo mướp (nhà bên) thấy bà giả thì xù lông, rít, bỏ chạy.** Nhân vật mới `cat_tabby`
    (mèo mướp vằn xám-nâu, cùng nét sáp, không trắng), 1 sheet 2×3: ngồi/đứng bình thường nhìn, lưng cong xù
    lông rít (há miệng, nhe nanh), và chu kỳ chạy ≥ 4 khung (chạy ngang, facing right). Cảnh 77: mèo đứng gần bà
    → xù lông rít (khớp sfx `cat_hiss`) → chạy ra khỏi khung về phía cổng (cycle, dừng ở khe cổng / tối dần, xem mục 4).
    Nhân vật mới: tạo meta + style_prompt trước (character_base hoặc gộp vào sheet với style tự viết) — chọn
    cách ít lượt Gemini nhất; gom cùng lượt asset mục 5–7.
11. **Cảnh 81 (lọ dầu gió): không đặt trên bàn thờ** (chốt ý đề xuất ở mục 5). Cần asset mới: **tủ đầu giường gỗ
    có ngăn kéo đang mở** (cùng kiểu tủ đầu giường trên `bg1_bedroom`), nhìn cận, trong ngăn có vài đồ lặt vặt
    của bà (khăn tay, lược, tràng hạt…), chừa chỗ đặt `HN6_wind_oil_bottle` trong/trên ngăn kéo.
    Cảnh 80 (Khoa lục ngăn kéo) → cảnh 81 cận ngăn kéo mở + lọ dầu bụi, camera đẩy chậm vào nắp lọ.
    Gom cùng lượt asset mục 5–10.
12. **Cảnh 82 (bà Sáu bán xôi kéo Khoa lại): cần phông BUỔI SÁNG và có người ngoài đường.**
    - Phông mới `bg7d_front_yard_morning`: cùng bố cục `bg7_front_yard` (cổng sắt, chậu cây, bàn cúng) nhưng sáng sớm
      trời trong, nắng nhạt, cổng mở hé, ngoài đường có hàng quán/xe đạp mờ xa. Dùng cho mọi cảnh ban ngày ở sân:
      82, 83, 84 (bà Sáu kể), 95–96 ("Sáng nay mở cổng"); cân nhắc 69–70 (rạng đông) dùng bản này chỉnh tối hơn.
    - Nhân vật mới **bà Sáu** (hàng xóm bán xôi đầu ngõ, áo nâu sẫm/xanh, nón lá, gánh/thúng xôi; không mặc trắng):
      đứng ngoài cổng kéo tay/ghé tai nói nhỏ với Khoa, chỉ tay về phía bến sông.
    - Người qua đường: 1–2 bóng người đi xe đạp/đi bộ ngoài đường (sprite nhỏ, chu kỳ đi đơn giản) để có
      không khí sáng sớm — có thể vẽ sẵn trong phông nếu muốn ít asset.
    Gom cùng lượt asset mục 5–11.
