# Nhân vật `props` — Đạo cụ (bát cơm cúng, nhang, dấu tay, dép)

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.

- Chiều cao mặc định: `0.2` khung hình

**Chu kỳ chuyển động** (dùng `"cycle": "props/<tên>"`):

- `fire`: 3 khung — VM1_fire_bucket_1, VM2_fire_bucket_2, VM3_fire_bucket_3

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
| `HP1_footprints_trail_toward` | front | Dãy dấu chân bùn — Gemini vẽ lẫn hướng (dấu xa hướng ra, dấu gần hướng vào): KHÔNG dùng cho cảnh đi vào nhà; ghép từ HP2/HP3 | dấu chân, bùn, đi vào |  |
| `HP2_footprint_left_toward` | front | Một dấu chân TRÁI bùn ướt, mũi chân hướng về người xem (đã xoay 180° khi cắt: rotate trong sprites.json) | dấu chân, trái |  |
| `HP3_footprint_right_toward` | front | Một dấu chân PHẢI bùn ướt, mũi chân hướng về người xem (đã xoay 180° khi cắt: rotate trong sprites.json) | dấu chân, phải |  |
| `VM1_fire_bucket_1` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 1/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM2_fire_bucket_2` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 2/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM3_fire_bucket_3` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 3/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM4_grandma_crouch_drop_paper` | right | Bà ngồi xổm thả xấp vàng mã xuống (mặt hắt ánh lửa) | bà, vàng mã, đốt |  |
| `VM5_grandma_hold_paper` | right | Bà đứng ôm xấp vàng mã trước ngực, cúi đầu | bà, vàng mã |  |
| `VM6_joss_paper_stack` | front | Xấp vàng mã đỏ vàng nằm dưới đất | vàng mã, đạo cụ |  |
