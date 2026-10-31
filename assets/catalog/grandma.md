# Nhân vật `grandma` — Bà nội

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.

- Chiều cao mặc định: `0.5` khung hình

**Chu kỳ chuyển động** (dùng `"cycle": "grandma/<tên>"`):

- `walk`: 6 khung — D1_walk_1, D2_walk_2, D3_walk_3, D4_walk_4, D5_walk_5, D6_walk_6
- `walk_old`: 6 khung — B1_walk_1, B2_walk_2, B3_walk_3, B4_walk_4, B5_walk_5, B3_walk_3
- `walk_v2`: 6 khung — C1_walk_1, C2_walk_2, C3_walk_3, C4_walk_4, C5_walk_5, C6_walk_6
- `fake_walk`: 4 khung — G1_fake_walk_1, G2_fake_walk_2, G3_fake_walk_3, G4_fake_walk_4

| Sprite | Hướng | Mô tả | Tag | Neo |
|---|---|---|---|---|
| `00_stand_front` | front | Đứng chính diện, hai tay đan trước bụng, hiền và lo lắng | đứng, chính diện |  |
| `A1_hold_hands_warn` | right | Nghiêng người nắm chặt hai tay đứa trẻ (có đôi tay trẻ con trong hình), nghiêm mặt dặn dò | dặn dò, nắm tay, cảnh báo |  |
| `A2_incense_pray` | right | Cúi đầu chắp ba nén nhang đang cháy, khấn | thắp nhang, khấn, cúng, bàn thờ |  |
| `A3_scatter_rice_salt` | left | Ôm bát, vung tay rải gạo muối (hạt bay trong hình) | rải gạo muối, cúng cô hồn, sân |  |
| `A4_sit_hug_knees_grief` | front | Ngồi bệt ôm gối, cúi đầu, kiệt sức đau buồn | ngồi, buồn, khóc, kiệt sức |  |
| `A5_scoop_rice` | left | Đứng cầm bát, dùng muôi gỗ xới cơm, mắt nhìn xuống | xới cơm, bát cơm thứ hai, bữa cơm |  |
| `A6_head_bowed_face_hidden` | front | Đứng im, cúi gằm, mặt chìm trong bóng tối | cúi mặt, rợn, bí ẩn, chính diện |  |
| `B1_walk_1` | right | Đi chậm lưng còng, tay chống lưng, khung 1/6 | đi, chu kỳ, già |  |
| `B2_walk_2` | right | Đi chậm lưng còng, tay chống lưng, khung 2/6 | đi, chu kỳ, già |  |
| `B3_walk_3` | right | Đi chậm lưng còng, tay chống lưng, khung 3/6 | đi, chu kỳ, già |  |
| `B4_walk_4` | right | Đi chậm lưng còng, tay chống lưng, khung 4/6 | đi, chu kỳ, già |  |
| `B5_walk_5` | right | Đi chậm lưng còng, tay chống lưng, khung 5/6 | đi, chu kỳ, già |  |
| `B6_walk_6` | right | Đi chậm lưng còng, tay chống lưng, khung 6/6 (mặt bị mờ, không dùng trong chu kỳ) | đi, chu kỳ, già |  |
| `C1_walk_1` | right | Đi chậm lưng còng, tay chống lưng, bước rõ, khung 1/6 | đi, chu kỳ |  |
| `C2_walk_2` | right | Đi chậm lưng còng, tay chống lưng, bước rõ, khung 2/6 | đi, chu kỳ |  |
| `C3_walk_3` | right | Đi chậm lưng còng, tay chống lưng, bước rõ, khung 3/6 | đi, chu kỳ |  |
| `C4_walk_4` | right | Đi chậm lưng còng, tay chống lưng, bước rõ, khung 4/6 | đi, chu kỳ |  |
| `C5_walk_5` | right | Đi chậm lưng còng, tay chống lưng, bước rõ, khung 5/6 | đi, chu kỳ |  |
| `C6_walk_6` | right | Đi chậm lưng còng, tay chống lưng, bước rõ, khung 6/6 | đi, chu kỳ |  |
| `D1_walk_1` | right | Đi chậm, tay chống lưng, chu kỳ chuẩn, khung 1/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D2_walk_2` | right | Đi chậm, tay chống lưng, chu kỳ chuẩn, khung 2/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D3_walk_3` | right | Đi chậm, tay chống lưng, chu kỳ chuẩn, khung 3/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D4_walk_4` | right | Đi chậm, tay chống lưng, chu kỳ chuẩn, khung 4/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D5_walk_5` | right | Đi chậm, tay chống lưng, chu kỳ chuẩn, khung 5/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D6_walk_6` | right | Đi chậm, tay chống lưng, chu kỳ chuẩn, khung 6/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `E1_hold_boy_hands` | right | Bà (trái) nắm chặt hai tay Khoa (phải), bà rưng rưng, Khoa sợ — HAI nhân vật chung một hình (h ≈ 0.5 cho cả cặp) | bà, Khoa, nắm tay, dặn dò |  |
| `E2_whisper_boy_ear` | right | Bà (trái) cúi ghé tai thì thầm, tay đặt vai Khoa (phải), Khoa mở to mắt — HAI nhân vật chung một hình | bà, Khoa, thì thầm, dặn dò |  |
| `F1_sit_porch_gaze` | right | Ngồi ghế tre thấp, nhìn xa xăm về phía phải (bến sông), buồn | ngồi, hiên, nhìn xa |  |
| `F2_bed_rub_oil_boy` | left | HAI nhân vật + giường: bà ngồi mép giường xoa dầu gió lên trán Khoa đang nằm | giường, dặn dò, dầu gió |  |
| `F3_cough_hunched` | left | Đứng còng, tay che miệng ho khù khụ, tay kia chống lưng | ho, còng |  |
| `F4_sit_stool_three_fingers` | right | Ngồi ghế đẩu, giơ ba ngón tay, nghiêm mặt dặn ám hiệu | ám hiệu, dặn dò |  |
| `F5_hold_effigy_back` | away | Quay lưng, ôm hình nhân giấy mặc áo hoodie và xấp vàng mã | hình nhân, quay lưng |  |
| `F6_hug_boy_bed_dark` | front | HAI nhân vật + giường: bà ôm chặt Khoa, cả hai run sợ, bà thì thầm | giường, ôm, sợ |  |
| `G1_fake_walk_1` | right | Bà giả đi thẳng lưng, khung 1/4 (chạm) | bà giả, đi |  |
| `G2_fake_walk_2` | right | Bà giả đi thẳng lưng, khung 2/4 (hạ) | bà giả, đi |  |
| `G3_fake_walk_3` | right | Bà giả đi thẳng lưng, khung 3/4 (chạm chân kia) | bà giả, đi |  |
| `G4_fake_walk_4` | right | Bà giả đi thẳng lưng, khung 4/4 (hạ chân kia) | bà giả, đi |  |
| `G5_sit_porch_wet_smile` | front | Bà giả ngồi bệt ướt sũng, nước nhỏ tong tỏng, ngẩng lên cười hiền | bà giả, ướt, cười |  |
| `G6_stand_dark_smile` | front | Bà giả đứng thẳng im lìm, nửa mặt trong bóng tối, cười hơi quá rộng | bà giả, rợn |  |
| `H1_bed_hold_wrist_whisper` | left | HAI nhân vật + giường: bà giả nằm nghiêng siết cổ tay Khoa, ghé tai thì thầm; Khoa mở trừng mắt | bà giả, giường, thì thầm |  |
| `H2_bed_edge_stroke_head` | left | HAI nhân vật + giường: bà giả ngồi mép giường xoa đầu Khoa, cười hiền | bà giả, giường, dặn dò |  |
| `H3_sit_back_turned` | away | Bà giả ngồi ghế tre quay lưng, thẳng đơ, tóc ướt bết | bà giả, quay lưng |  |
| `H4_sit_offer_food` | left | Bà giả ngồi ghế đẩu gắp thức ăn đưa sang trái, không ăn, nhìn chằm chằm cười | bà giả, bữa cơm |  |
| `H5_closeup_hand_wrist` | right | Cận bàn tay nhăn nheo trắng bệch như ngâm nước siết cổ tay Khoa (tay áo xanh rêu) | cận, tay, bà giả |  |
| `H6_closeup_face_smile` | front | Cận mặt bà giả cười rất hiền, tóc ướt, giọt nước nhỏ từ cằm (cú hù cuối) | cận, bà giả, hù |  |
| `I1_back_incense_closeup` | away | Cận từ sau lưng, từ vai trở lên, hai tay giơ ba nén nhang khói bay (tiền cảnh trước bàn thờ) | thắp nhang, quay lưng, cận |  |
| `I2_fake_look_down_side` | right | Bà giả đứng nghiêng (quay phải), cúi nhìn xuống đất, cười đơ (nhìn con mèo) | bà giả, nhìn xuống |  |
| `J1_back_carry_effigy` | away | Quay lưng đi ra, ôm hình nhân (đầu hình nhân ló qua vai) và xấp vàng mã | hình nhân, quay lưng, ra bến sông |  |
| `J2_side_carry_effigy` | right | Nghiêng (quay phải), đi chậm, bế hình nhân trước ngực như bế đứa trẻ, xấp vàng mã bên trên | hình nhân, đi, ra bến sông |  |
