# Nhân vật `props` — Đạo cụ (bát cơm cúng, nhang, dấu tay, dép)

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.

- Chiều cao mặc định: `0.2` khung hình

**Chu kỳ chuyển động** (dùng `"cycle": "props/<tên>"`):

- `fire`: 3 khung — VM1_fire_bucket_1, VM2_fire_bucket_2, VM3_fire_bucket_3
- `crow_fly`: 4 khung — LD5_crow_fly_1, LD6_crow_fly_2, LD7_crow_fly_3, LD8_crow_fly_4

| Sprite | Hướng | Mô tả | Tag | Neo |
|---|---|---|---|---|
| `DC1_bowl_chopsticks_upright` | front | Bát cơm cúng đầy, trứng luộc bên trên, đôi đũa cắm thẳng giữa bát | bát cơm, cúng, đũa cắm thẳng, trứng |  |
| `DC1b_bowl_chopsticks_vertical` | front | Bát cơm cúng đầy, trứng luộc, đôi đũa cắm THẲNG ĐỨNG song song giữa bát (thay DC1) | bát cơm, cúng, đũa cắm thẳng, trứng |  |
| `DC2_bowl_chopsticks_across` | front | Bát cơm vơi, đũa gác ngang miệng bát (thói quen của mẹ) | bát cơm, vơi, đũa gác ngang, mẹ về |  |
| `DC3_bowl_empty_eggshell` | front | Bát sạch trơn, vỏ trứng vỡ bên cạnh | bát cơm, sạch trơn, vỏ trứng, leo thang |  |
| `DC4_incense_broken` | front | Bát hương đồng, một nén nhang gãy gập, không khói | bát hương, nhang gãy, điềm xấu |  |
| `DC5_black_handprints` | front | Hai dấu tay đen ngón dài như muội than | dấu tay, đen, cô hồn |  |
| `DC6_mother_slippers` | front | Đôi dép nhựa nâu mòn gót của mẹ | dép, mẹ, đêm 49 |  |
| `HN1_paper_effigy_hoodie` | front | Hình nhân giấy ngồi, mặc áo hoodie xanh rêu của Khoa, lọn tóc buộc chỉ đỏ trước ngực | hình nhân, thế mạng |  |
| `HN2_wooden_clog_upside_down` | front | Một chiếc guốc mộc nằm úp sấp trên bậc đá ướt | guốc, bến sông |  |
| `HN3_sandal_upside_down_puddle` | front | Một chiếc dép nhựa đen của bà úp sấp trong vũng nước, bùn sông bám gót | dép, vũng nước |  |
| `HN4_muddy_footprints_trail` | front | Dãy dấu chân trần bùn ướt đi xa dần (nằm trên nền) | dấu chân, bùn |  |
| `HN5_single_wet_footprint` | front | Một dấu chân trần bùn ướt đơn lẻ (dùng để hiện dần từng dấu) | dấu chân, bùn |  |
| `HN6_wind_oil_bottle` | front | Lọ dầu gió xanh nhỏ, nắp vặn chặt, phủ bụi mỏng | dầu gió, bụi |  |
| `HP2_footprint_left_toward` | front | Một dấu chân TRÁI bùn ướt, mũi chân hướng về người xem (đã xoay 180° khi cắt: rotate trong sprites.json) | dấu chân, trái |  |
| `HP3_footprint_right_toward` | front | Một dấu chân PHẢI bùn ướt, mũi chân hướng về người xem (đã xoay 180° khi cắt: rotate trong sprites.json) | dấu chân, phải |  |
| `LB1_talisman_folded` | front | Lá bùa giấy vàng gấp tư, lộ vết mực đỏ | lá bùa |  |
| `LB2_talisman_open` | front | Lá bùa mở ra: chữ mực đỏ ngoằn ngoèo, dấu triện đỏ | lá bùa |  |
| `LB3_chopsticks_named` | front | Đôi đũa tre khắc tên (nét nghiêng, gọn) | đũa khắc tên |  |
| `LB4_chopsticks_spare_carved` | front | Đôi đũa dư: chữ khắc run run kín cả bốn mặt | đũa dư |  |
| `LB5_chopstick_broken` | front | Chiếc đũa tre gãy đôi, đầu gãy tua | đũa gãy |  |
| `LB6_chopstick_holder` | front | Ống đũa tre cắm nhiều đôi đũa khắc tên | ống đũa |  |
| `LC1_bowl_full_chopsticks_across` | front | Bát cơm xới đầy nén chặt, đôi đũa gác ngang miệng bát | bát cơm, bàn thờ |  |
| `LC3_mirror_red_cloth` | front | Gương treo tường phủ kín tấm vải đỏ | gương, kiêng |  |
| `LC4_wall_clock_three` | front | Đồng hồ quả lắc treo tường chỉ đúng 3 giờ | đồng hồ, 3 giờ |  |
| `LD1_crow_perched` | right | Quạ đậu im trên mẩu cành | quạ |  |
| `LD2_crow_caw` | right | Quạ đậu, há mỏ kêu | quạ, kêu |  |
| `LD3_crow_look_down` | right | Quạ nghiêng đầu nhìn xuống | quạ |  |
| `LD5_crow_fly_1` | right | Quạ bay 1/4 (cánh lên) | quạ, bay |  |
| `LD6_crow_fly_2` | right | Quạ bay 2/4 | quạ, bay |  |
| `LD7_crow_fly_3` | right | Quạ bay 3/4 (cánh xuống) | quạ, bay |  |
| `LD8_crow_fly_4` | right | Quạ bay 4/4 | quạ, bay |  |
| `LE4_matchbox_lit_match` | front | Bao diêm cũ và que diêm đang cháy | diêm |  |
| `LF1_bowl_chopsticks_upright` | front | Bát cơm xới đầy, đôi đũa CẮM THẲNG ĐỨNG giữa bát | bát cơm, bàn thờ |  |
| `LF2_bowl_upright_steaming` | front | Bát cơm cắm đũa đứng, còn bốc khói | bát cơm, nóng |  |
| `LF3_chopsticks_khoa` | front | Đôi đũa tre khắc rõ chữ KHOA, nét nghiêng gọn | đũa khắc tên |  |
| `LG1_chopsticks_spare_ugly` | front | Đôi đũa dư: giống đũa LF3 nhưng chữ KHOA khắc xấu, run, xiêu vẹo (một lần mỗi chiếc) | đũa dư, đũa khắc tên |  |
| `LH10_bagua_mirror` | front | Gương bát quái bát giác đỏ vàng | gương bát quái |  |
| `LH1_sweater_unfinished` | front | Áo len đỏ sẫm đan dở (thiếu cổ), que đan và cuộn len | áo len, đan dở |  |
| `LH2_mourning_tunic_folded` | front | Bộ áo xô be may xong, đường kim thẳng tắp | áo xô, tang |  |
| `LH3_calendar_circled` | front | Tờ lịch treo tường, nhiều ngày khoanh bút chì, một ngày khoanh đậm | lịch, đếm ngày |  |
| `LH4_fingertips_needle_marks` | front | Cận bàn tay phụ nữ, mười đầu ngón chi chít vết kim, máu khô | vết kim, cận |  |
| `LH5_rice_under_nails` | front | Cận bàn tay, vài hạt cơm nguội dính dưới móng tay | hạt cơm, móng tay, cận |  |
| `LH6_mirror_bare` | front | Gương treo tường khung gỗ, không phủ, mặt kính tối | gương |  |
| `LH7_red_cloth_floor` | front | Tấm vải đỏ nhàu rơi dưới sàn | vải đỏ, gương |  |
| `LH8_pencil_case_talisman` | front | Hộp bút mở, lá bùa gấp tư giấu dưới đáy | hộp bút, lá bùa |  |
| `LH9_sewing_machine_covered` | front | Máy khâu đạp chân phủ kín tấm khăn xám | máy khâu, tang |  |
| `LJ1_chopsticks_plain` | front | Đôi đũa tre trơn, không khắc chữ | đũa, trơn |  |
| `LJ2_chopsticks_spare_top_carved` | front | Đôi đũa dư: chữ KHOA khắc run run ở ĐẦU TRÊN đũa, đủ bốn mặt; phần còn lại trơn | đũa dư, khắc tên |  |
| `LJ3_box_closed_rubberband` | front | Hộp giấy dài hẹp đậy nắp, quấn dây chun đỏ (dài hơn đôi đũa) | hộp, đũa dư |  |
| `LJ4_box_open_spare` | front | Hộp mở, đôi đũa dư nằm dọc bên trong (thấy đầu khắc chữ) | hộp, đũa dư |  |
| `LJ5_box_open_red_soil` | front | Hộp mở, không còn đũa, chỉ còn nhúm đất đỏ ẩm (P3) | hộp, đất đỏ |  |
| `LK1_chopsticks_burning` | front | Đôi đũa khắc tên nằm chéo trên đĩa đất nung, đang cháy, khói xám bốc lên | đốt đũa, lửa |  |
| `VM1_fire_bucket_1` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 1/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM2_fire_bucket_2` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 2/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM3_fire_bucket_3` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 3/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM4_grandma_crouch_drop_paper` | right | Bà ngồi xổm thả xấp vàng mã xuống (mặt hắt ánh lửa) | bà, vàng mã, đốt |  |
| `VM6_joss_paper_stack` | front | Xấp vàng mã đỏ vàng nằm dưới đất | vàng mã, đạo cụ |  |
