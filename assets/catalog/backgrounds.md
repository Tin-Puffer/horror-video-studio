# Phông nền

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.

Toạ độ là tỉ lệ khung hình 16:9 (x 0 trái→1 phải, y 0 trên→1 dưới). floor_y = đường chân nhân vật đứng ở tiền cảnh; char_h = chiều cao nhân vật khuyến nghị.

| Phông | Mô tả | floor_y | char_h | Điểm nóng (dùng tên trong `pin.at`) |
|---|---|---|---|---|
| `bg10_river_wharf` | Bến sông thị trấn ban đêm: bậc đá xuống mặt nước đen, sương mỏng, bụi tre bên phải, bờ xa có một đốm đèn | 0.95 | 0.46 |  |
| `bg11_peephole_yard` | Nhìn qua mắt mèo cửa chính: khung tròn giữa nền đen, sân xi măng ánh trăng bị bóp méo, cổng sắt xa | 0.7 | 0.3 |  |
| `bg12_bedside_drawer` | Cận tủ đầu giường gỗ, ngăn kéo mở: khăn tay, lược gỗ, tràng hạt của bà, chừa chỗ trống giữa ngăn đặt lọ dầu | 0.8 | 0.3 |  |
| `bg1_bedroom` | Phòng ngủ ban đêm, KHÔNG có giường (dùng sprite G1–G3). Cửa phòng bên trái, cửa sổ ánh trăng giữa, tủ đầu giường + đồng hồ 03:00, nửa phải sàn trống. | 0.95 | 0.46 | `bedroom_door` [0.1, 0.55]; `bedroom_door_handle` [0.145, 0.49]; `window` [0.34, 0.35]; `clock` [0.48, 0.53]; `bed_spot` [0.7, 0.95] |
| `bg1c_corner_night` | Góc phòng ngủ ban đêm, Khoa vẽ sẵn: ngồi co ro trong góc, bịt hai tai, MẮT MỞ TRỪNG nhìn về phía cửa (trái), khe sáng vàng dưới cửa, mép giường bên phải. | 0.95 | 0.4 | `boy_face` [0.5, 0.42]; `door` [0.12, 0.5]; `door_gap` [0.15, 0.86] |
| `bg1d_corner_dawn` | Góc phòng ngủ lúc rạng đông (đã chỉnh sáng), Khoa vẫn ngồi bịt tai, mắt đỏ thâm quầng, thức trắng cả đêm. | 0.95 | 0.4 | `boy_face` [0.5, 0.45]; `door` [0.17, 0.5] |
| `bg2_hallway` | Hành lang dài nằm ngang, sàn gỗ, 2 cửa đóng, ảnh gia đình mờ trên tường, hai đầu tối. | 0.97 | 0.46 | `door_left` [0.34, 0.5]; `door_right` [0.705, 0.5]; `family_photo` [0.5, 0.36]; `far_end` [0.86, 0.9] |
| `bg3_front_door` | Cửa chính nhìn từ trong nhà, ở giữa; lỗ mắt mèo (cao, quá tầm cậu bé), tay nắm bên trái cửa, tủ giày bên trái, móc áo bên phải, khe sáng vàng dưới cửa. | 0.96 | 0.46 | `door_handle` [0.44, 0.478]; `peephole` [0.5, 0.205]; `door_center` [0.5, 0.45]; `door_bottom_y` [0.5, 0.79]; `shoe_rack` [0.23, 0.72]; `coat_hooks` [0.73, 0.35] |
| `bg3b_peephole` | Góc nhìn qua mắt mèo: khung tròn giữa nền đen, hành lang chung cư bị bóp méo, đèn trần mờ. | 0.66 | 0.3 | `lens_circle` [0.5, 0.5, 0.49]; `corridor_floor` [0.6, 0.66]; `far_door` [0.5, 0.5] |
| `bg4_main_room` | Gian nhà chính ban đêm: bàn thờ treo tường bên trái (ảnh thờ, bát hương, 2 nến đỏ, đĩa hoa quả, bát cơm), bàn ăn thấp + 2 ghế đẩu bên phải, lịch treo tường, cửa xuống bếp sát mép phải. Nửa trái sàn trống. | 0.95 | 0.46 | `altar_shelf` [0.3, 0.36]; `altar_portrait` [0.31, 0.24]; `altar_rice` [0.4, 0.33]; `altar_incense` [0.31, 0.33]; `dining_table` [0.73, 0.6]; `table_top_y` [0.73, 0.585]; `stool_left` [0.585, 0.8]; `stool_right` [0.86, 0.78]; `kitchen_door` [0.96, 0.5]; `calendar` [0.7, 0.35]; `open_floor` [0.3, 0.95] |
| `bg4d_main_room_day` | Gian nhà chính (cùng bố cục BG4) chiều nắng ấm trong hồi ức: kệ chỉ có bình hoa + bát, không ảnh thờ; nồi canh bốc khói trên bàn ăn. | 0.95 | 0.46 | `altar_shelf` [0.3, 0.36]; `altar_portrait` [0.31, 0.24]; `altar_rice` [0.4, 0.33]; `altar_incense` [0.31, 0.33]; `dining_table` [0.73, 0.6]; `table_top_y` [0.73, 0.585]; `stool_left` [0.585, 0.8]; `stool_right` [0.86, 0.78]; `kitchen_door` [0.96, 0.5]; `calendar` [0.7, 0.35]; `open_floor` [0.3, 0.95] |
| `bg4e_main_room_day_bo` | Gian chính ban ngày (như bg4d): kệ thờ trên tường có di ảnh bố, bát hương, 2 nến; bàn ăn nồi canh, ghế đẩu | 0.95 | 0.46 | `altar_shelf` [0.3, 0.33]; `dining_table` [0.73, 0.6] |
| `bg5_altar_close` | Cận mặt bàn thờ ban đêm: ảnh thờ mẹ (dải băng tang đen) ở giữa, bát hương đồng với 3 nén nhang khói bên trái, 2 nến đỏ, đĩa và chân nến bên phải. Mặt gỗ phía trước trống để đặt đạo cụ (bát cơm). | 0.8 | 0.3 | `portrait` [0.5, 0.32]; `portrait_face` [0.5, 0.26]; `incense_bowl` [0.27, 0.6]; `incense_tips` [0.27, 0.33]; `candle_left` [0.35, 0.43]; `candle_right` [0.66, 0.43]; `offering_spot` [0.52, 0.78]; `plate` [0.76, 0.59] |
| `bg5b_altar_grandpa_lit` | Cận bàn thờ ÔNG nội ban đêm: ảnh thờ ông, bát hương có 3 nén nhang đang cháy khói, 2 nến sáng | 0.8 | 0.6 |  |
| `bg5c_altar_grandpa_cold` | Cùng bố cục bg5b nhưng nguội lạnh: chỉ còn chân nhang trơ trọi, không khói, nến tắt, bụi | 0.8 | 0.6 |  |
| `bg6_kitchen` | Bếp nhà ống ban đêm: bệ bếp lát gạch bên trái (bếp ga 2 lò + nồi nhôm, nồi cơm điện, giá bát, ống đũa), cửa sổ song sắt hắt ánh trăng, ô cửa tối om dẫn ra nhà sau ở giữa-phải. Sàn giữa và phải trống. | 0.95 | 0.46 | `doorway` [0.69, 0.38]; `doorway_floor` [0.69, 0.66]; `stove_pot` [0.14, 0.5]; `rice_cooker` [0.31, 0.43]; `window` [0.42, 0.17]; `dish_rack` [0.15, 0.22]; `open_floor` [0.62, 0.95] |
| `bg6d_kitchen_day` | Bếp (cùng bố cục BG6) chiều nắng vàng trong hồi ức, nồi trên bếp bốc hơi, ô cửa sáng. | 0.95 | 0.46 | `doorway` [0.69, 0.38]; `doorway_floor` [0.69, 0.66]; `stove_pot` [0.14, 0.5]; `rice_cooker` [0.31, 0.43]; `window` [0.42, 0.17]; `dish_rack` [0.15, 0.22]; `open_floor` [0.62, 0.95] |
| `bg7_front_yard` | Sân trước nhà ban đêm: chậu cây + bàn cúng nhỏ ngoài trời bên trái, cổng sắt xếp hoen gỉ chiếm nửa phải, khe hở giữa cổng nhìn ra đường vắng có sương và cột đèn xa. Nền xi măng nứt. | 0.95 | 0.46 | `offering_table` [0.28, 0.47]; `offering_table_top` [0.28, 0.455]; `gate_gap` [0.69, 0.45]; `gate_gap_floor` [0.69, 0.64]; `gate_left` [0.5, 0.35]; `gate_right` [0.88, 0.35]; `street_lamp` [0.68, 0.19]; `open_floor` [0.5, 0.95] |
| `bg7d_front_yard_morning` | Sân trước buổi sáng sớm (cùng bố cục bg7): nắng nhạt, cổng mở hé, ngoài đường có người đạp xe, người đi bộ, hàng quán | 0.95 | 0.46 |  |
| `bg8_bedroom_door` | Trong phòng ngủ nhìn thẳng vào cửa phòng đóng (giữa khung): tay nắm + chốt cài, khe sáng vàng dưới chân cửa hắt lên sàn gỗ; hai tờ tranh vẽ dán tường hai bên. | 0.97 | 0.46 | `door_center` [0.5, 0.53]; `door_handle` [0.555, 0.53]; `bolt_lock` [0.58, 0.46]; `door_gap` [0.5, 0.855]; `door_gap_left` [0.41, 0.855]; `door_gap_right` [0.59, 0.855] |
| `bg9b_door_gap_ghosts` | POV qua khe dưới cửa: đám cô hồn ngồi xổm quanh mâm cơm (khe cắt ngang người, thấy gối, chân, tay đen bốc cơm), bát đổ, một con nhỏ ở xa. Vẽ sẵn, không cần sprite. | 0.6 | 0.2 | `slit_center` [0.5, 0.52]; `tray` [0.53, 0.6]; `far_ghost` [0.49, 0.37] |
| `bg9c_door_gap_face` | POV qua khe dưới cửa: một cô hồn áp mặt xuống sàn sát cửa, hốc mắt đen nhìn thẳng vào khe, miệng dính cơm (cú hù). Vẽ sẵn. | 0.6 | 0.2 | `slit_center` [0.5, 0.52]; `ghost_face` [0.43, 0.48] |
| `bgL10_altar_four_portraits` | Bàn thờ đêm có 4 di ảnh: ông, mẹ, bà và khung thứ tư phủ kín vải đen; mặt trước trống để đặt bát cơm | 0.8 | 0.6 | `offering_spot` [0.5, 0.64] |
| `bgL10b_altar_four_portraits` | Bàn thờ 4 di ảnh (ông, mẹ, bà, khung phủ vải đen), lư hương nhỏ ở giữa mép trước, chỗ trống trước từng di ảnh để đặt bát | 0.8 | 0.6 | `offering_spot` [0.5, 0.62]; `incense` [0.49, 0.6] |
| `bgL11_ong_bed_corner_night` | Góc nhà cạnh gian thờ ban đêm: bàn thờ treo nhỏ (ảnh bố), đồng hồ quả lắc trên tường, cửa sổ trăng; sàn trống đặt giường tre (sprite) | 0.95 | 0.46 | `bed_spot` [0.5, 0.85]; `clock` [0.46, 0.34] |
| `bgL12_living_room_day` | Phòng khách buổi sáng xám: chiếu cói giữa nhà, tủ thấp, khay trà, bàn thờ trên cao; sàn trống | 0.93 | 0.46 | `mat_center` [0.52, 0.82] |
| `bgL13_home_altar_bo` | Cận bàn thờ cũ trong nhà (ảnh bố), nửa phải là tường trống để treo gương phủ vải đỏ | 0.95 | 0.5 | `portrait` [0.31, 0.24]; `mirror_spot` [0.68, 0.35] |
| `bgL14_grandma_comb_coffin` | Vẽ sẵn: bà ngồi ghế thấp bên quan tài, chải tóc bạc cho ông (thấy đầu ông trên mép quan tài), thì thầm | 0.95 | 0.5 | `grandma` [0.73, 0.5]; `ong_head` [0.29, 0.45] |
| `bgL14b_grandma_by_coffin` | Góc thấp: thành quan tài che kín (không thấy ông), bà ngồi ghế đẩu bên phải, lược trong lòng, tay đặt lên thành quan tài thì thầm | 0.95 | 0.42 | `grandma` [0.72, 0.55] |
| `bgL15_khoa_bed_awake_night` | Vẽ sẵn: Khoa nằm mắt mở thao láo trên giường, tay nắm áo khoác đen treo đầu giường, đồng hồ gần 3 giờ | 0.95 | 0.46 | `boy` [0.665, 0.52]; `clock` [0.92, 0.62] |
| `bgL15b_khoa_bed_awake_plain` | Vẽ sẵn: Khoa nằm thao láo, hai tay để trên chăn (không chạm áo khoác treo đầu giường) | 0.95 | 0.46 | `boy` [0.6, 0.6] |
| `bgL16_market_morning` | Đầu chợ quê buổi sáng: mái bạt, gánh rau, hàng xôi bốc hơi; bậc đá trống ở tiền cảnh, nắng sớm | 0.93 | 0.46 | `stone_step` [0.4, 0.7] |
| `bgL16b_market_side_step` | Đầu chợ buổi sáng: đường giữa thông, bậc đá trước một sạp đóng cửa ở mép trái tiền cảnh | 0.93 | 0.46 | `stone_step` [0.18, 0.72] |
| `bgL17_cemetery_night_grave` | Nghĩa địa đêm: mộ ông mới đắp đất đỏ, bia nhỏ, cây gạo khô bên phải, sương mỏng; chừa chỗ quỳ và chỗ sau bia | 0.95 | 0.42 | `grave_head` [0.53, 0.63]; `behind_headstone` [0.475, 0.56]; `crow_branch` [0.7, 0.27] |
| `bgL17b_two_graves_day` | Ban ngày âm u: hai mộ cạnh nhau (mộ ông đất se mặt có lỗ nhỏ ở đầu, mộ mẹ đất tươi), cây gạo khô | 0.95 | 0.42 | `hole` [0.29, 0.72]; `crow_branch` [0.68, 0.215] |
| `bgL17c_two_graves_small_hole` | Hai mộ cạnh nhau ban ngày; đầu mộ ông chỉ có một lỗ nhỏ trẻ con bới, đất vương vãi | 0.95 | 0.42 | `hole` [0.28, 0.72]; `crow_branch` [0.68, 0.215] |
| `bgL18_field_path_night` | Bờ ruộng đêm chạy ngang khung, cỏ may rạp trong gió, xa xa hàng cây và cây gạo khô | 0.9 | 0.36 | `path` [0.5, 0.76] |
| `bgL19_mirror_ong_behind_mom` | Vẽ sẵn: trong gương, mẹ (áo xô, tóc xoã) xới cơm, ông áo the đứng sau đặt tay lên tay mẹ cầm muôi | 0.95 | 0.5 | `mirror` [0.49, 0.43] |
| `bgL19b_mirror_khoa_alone` | Vẽ sẵn: cùng gương, chỉ còn Khoa đứng một mình giữa gian thờ tối, sau lưng hai bát cơm | 0.95 | 0.5 | `mirror` [0.49, 0.43] |
| `bgL19c_mirror_ong_whisper` | Vẽ sẵn: trong gương, mẹ bưng bát cơm, ông áo the đứng sau đặt tay lên tay mẹ, ghé tai thì thầm | 0.95 | 0.5 | `mirror` [0.5, 0.42] |
| `bgL1_porch_day` | Hiên nhà ống chiều nắng vàng: cửa gỗ bên trái, nền gạch, cây bưởi già sai quả bên phải, tường rào thấp | 0.93 | 0.46 |  |
| `bgL1n_porch_night` | Hiên nhà (cùng bố cục bgL1) ban đêm, ánh trăng qua lá bưởi, đèn vàng hắt ra từ cửa | 0.93 | 0.46 |  |
| `bgL20b_wake_coffin_mom_open` | Gian thờ đám tang mẹ (cùng bố cục bgL2): quan tài mở nắp, di ảnh mẹ | 0.95 | 0.42 |  |
| `bgL21b_altar_three` | Cận bàn thờ: ảnh ông (giữa), ảnh bố, ảnh mẹ mới; nhang khói, nến; mặt bàn trống đặt bát | 0.8 | 0.6 | `offering_ong` [0.75, 0.66]; `offering_me` [0.63, 0.66] |
| `bgL22_backyard_morning` | Sân sau bếp buổi sáng xám: cửa bếp bên trái, giếng gạch, chum nước, dây phơi, bụi chuối; nền đất trống | 0.93 | 0.48 | `open_ground` [0.6, 0.85] |
| `bgL23_house_roof_dusk` | Sân trước lúc chạng vạng nhìn lên nóc nhà mái rêu (chỗ quạ đậu) và cây bưởi bên phải | 0.95 | 0.46 | `roof_ridge` [0.52, 0.06]; `pomelo_branch` [0.75, 0.3] |
| `bgL24_altar_ong_bo_cold` | Cận bàn thờ nguội: ảnh ông + ảnh bố nhỏ bên cạnh, nến tắt; mặt bàn trống đặt bát | 0.8 | 0.6 | `offering_left` [0.47, 0.7]; `offering_right` [0.65, 0.68] |
| `bgL25_mom_bed_sick_night` | Vẽ sẵn: mẹ ốm nằm trên giường trong phòng mẹ ban đêm | 0.93 | 0.5 | `bed_foot` [0.85, 0.8] |
| `bgL25b_mom_bed_bowl_morning` | Vẽ sẵn (đêm/rạng sáng): mẹ ngủ, bát cơm sát gối, đũa gác ngang miệng bát chĩa vào mặt mẹ | 0.93 | 0.5 | `bowl` [0.63, 0.57] |
| `bgL25c_mom_bed_sit_bowl_morning` | Vẽ sẵn (đêm/rạng sáng): mẹ ngồi dậy trên giường, siết chăn, nhìn bát cơm cạnh gối | 0.93 | 0.5 | `bowl` [0.64, 0.6] |
| `bgL25d_mom_dead_morning` | Vẽ sẵn: sáng sớm lạnh, mẹ (áo xô) nằm mất trên giường, bình thản như ngủ | 0.93 | 0.5 |  |
| `bgL25e_mom_bedroom_day` | Phòng mẹ buổi sáng nắng, giường gọn; sàn trái trống | 0.93 | 0.5 | `open_floor` [0.3, 0.85] |
| `bgL25h_mom_stroke_khoa_night` | Vẽ sẵn: phòng mẹ ban đêm, mẹ nằm đưa tay xoa đầu Khoa ngồi ghế cạnh giường cúi đầu khóc | 0.93 | 0.5 | `mother` [0.69, 0.55]; `boy` [0.61, 0.6] |
| `bgL25k_mom_knit_collar` | Vẽ sẵn: mẹ ngồi trên giường cố đan cổ áo len, tay run; Khoa ngồi cạnh nhìn | 0.93 | 0.5 |  |
| `bgL25m_khoa_hold_mom_hand` | Vẽ sẵn: mẹ (áo xô, tóc xoã) nằm thở yếu, Khoa ngồi bệt áp tay mẹ lên má khóc | 0.93 | 0.5 |  |
| `bgL25n_mom_bedroom_night` | Phòng ngủ của mẹ ban đêm: giường gỗ đôi to sát tường (đầu giường bên trái), màn buộc, tủ nhỏ; sàn trái trống | 0.93 | 0.5 | `pillow` [0.7, 0.5]; `bed_foot` [0.82, 0.8]; `open_floor` [0.3, 0.85] |
| `bgL25s_khoa_feed_soup` | Vẽ sẵn: chiều, Khoa ngồi mép giường bón canh cho mẹ trong phòng mẹ | 0.93 | 0.5 |  |
| `bgL26_mom_sewing_tunic` | Vẽ sẵn: mẹ ngồi khóc bên máy khâu, bộ áo xô may xong nằm trên bàn máy, áo len rơi dưới gầm | 0.93 | 0.5 | `mother` [0.42, 0.5] |
| `bgL27_khoa_peek_door_day` | Góc nhìn của Khoa nép sau cánh cửa buồng: chỉ thấy bàn tay bám mép cửa, khe cửa nhìn ra gian thờ (ảnh bố, bàn ăn) | 0.95 | 0.5 | `boy` [0.18, 0.85] |
| `bgL28_khoa_calendar_night` | Vẽ sẵn: Khoa đứng khoanh ngày trên tờ lịch treo tường dưới ánh đèn bàn | 0.95 | 0.46 | `calendar` [0.21, 0.4] |
| `bgL29_grandma_room_portrait` | Vẽ sẵn: phòng bà ban đêm đèn dầu, bà ngồi mép giường ôm di ảnh ông khóc thì thầm | 0.95 | 0.5 | `grandma` [0.33, 0.55] |
| `bgL2_wake_coffin` | Gian thờ đám tang ban đêm: quan tài gỗ mở nắp (nắp dựng tường phải) đặt giữa, đầu bên trái; bàn thờ có di ảnh ông, 2 nến, vòng hoa giấy; chiếu trước | 0.95 | 0.42 |  |
| `bgL2c_wake_coffin_closed` | Gian thờ (cùng bố cục bgL2) sáng đưa tang: nắp quan tài đã đóng đinh, phủ khăn đỏ vàng | 0.95 | 0.42 |  |
| `bgL2n_wake_candles_out` | Gian thờ (cùng bố cục bgL2) nến đã tắt, tối om, chỉ còn ba đầu nhang đỏ lập loè | 0.95 | 0.42 | `coffin_head` [0.36, 0.53] |
| `bgL30_khoa_dig_grave_night` | Vẽ sẵn: Khoa (áo khoác đen) quỳ bới lỗ nhỏ ở đầu mộ ông, đèn pin nằm cạnh | 0.95 | 0.42 |  |
| `bgL31_mirror_opposite_room` | Nhìn qua khung cửa sang phòng đối diện: tấm vải đỏ đang tuột khỏi chiếc gương lớn | 0.95 | 0.46 | `mirror` [0.73, 0.5] |
| `bgL32_khoa_rice_sack_bed` | Vẽ sẵn chiều: Khoa quỳ đẩy bao gạo buộc chặt miệng vào gầm giường, mặt quyết tâm | 0.95 | 0.46 |  |
| `bgL32b_rice_sack_pulled_out` | Rạng sáng: bao gạo bị lôi ra giữa sàn, sợi dây cởi ra đặt ngay ngắn bên cạnh, gạo vương | 0.95 | 0.46 |  |
| `bgL33_khoa_lock_cupboard` | Vẽ sẵn chiều: Khoa vặn chìa khoá đồng khoá tủ gỗ, nồi cơm nhôm ở trong | 0.95 | 0.46 |  |
| `bgL33b_cupboard_open_empty` | Rạng sáng: tủ bếp mở toang, ngăn trống trơn, chìa khoá còn cắm ổ | 0.95 | 0.46 |  |
| `bgL34_kitchen_stove_warm_dawn` | Góc bếp rạng sáng: bếp củi đất, nồi cơm nhôm còn ấm, tro còn vài đốm đỏ, khói mỏng; nửa phải trống | 0.95 | 0.46 |  |
| `bgL35_khoa_watch_mat_altar` | Vẽ sẵn đêm: Khoa ngồi bó gối trên chiếu trước bàn thờ, chăn mỏng khoác vai, tay nắm đèn pin, mắt mở trừng | 0.95 | 0.46 |  |
| `bgL35c_khoa_mat_dawn_key` | Vẽ sẵn rạng sáng: Khoa ngồi trên chiếu, chăn tuột, tay cầm chìa khoá tủ ngơ ngác; trên kệ ba bát cơm | 0.95 | 0.46 |  |
| `bgL36_grandma_doorway_stare` | Vẽ sẵn sáng xám: bà đứng ở cửa buồng, tay vịn khung cửa, nhìn trân trân về phía bàn thờ | 0.95 | 0.5 |  |
| `bgL37_khoa_kneel_confess` | Vẽ sẵn: Khoa quỳ khóc giơ lá bùa nhàu trước mặt bà đang đứng nhìn xuống | 0.95 | 0.5 |  |
| `bgL37b_khoa_bow_floor` | Vẽ sẵn: Khoa cúi rạp trán xuống nền gạch, lá bùa dưới đất; bà đứng, tay hơi đưa ra | 0.95 | 0.5 |  |
| `bgL38_grandma_sit_talisman_khoa` | Vẽ sẵn: bà ngồi bệt cạnh Khoa, cầm lá bùa nhàu trong lòng, kể chuyện; Khoa nép vào bà ngước nhìn | 0.95 | 0.5 |  |
| `bgL39_pagoda_boy_sepia` | Hồi ức sepia: bà cụ dắt cậu bé đầu cạo trọc tới cổng chùa, sư đứng đợi, cậu bé ngoái lại | 0.95 | 0.4 |  |
| `bgL3a_coffin_top_hands_chest` | Cận từ trên xuống trong quan tài: ông nằm, áo the, hai tay đặt trên ngực, góc lá bùa vàng ló dưới gối | 0.95 | 0.4 |  |
| `bgL3c_coffin_face_smile` | Cận mặt ông trong quan tài (ảo giác): mắt hé mở nhìn thẳng, miệng cười toác rợn người, ánh que diêm | 0.95 | 0.4 | `face` [0.5, 0.45] |
| `bgL3d_coffin_top_full` | Nhìn thẳng từ trên xuống: quan tài nằm ngang (đầu trái, chân phải), thấy trọn cả người ông (đủ chân, đúng tỉ lệ), tay đặt ngực; lá bùa khuất dưới gối nên không thấy | 0.95 | 0.4 | `face` [0.245, 0.38]; `hands` [0.44, 0.45]; `pillow` [0.245, 0.37]; `feet` [0.8, 0.45] |
| `bgL3e_coffin_top_full_dropped` | Cùng khung bgL3d: tay phải buông thõng cạnh gối, chỉ còn ánh que diêm, khoé miệng hơi nhếch | 0.95 | 0.4 | `face` [0.245, 0.43]; `dropped_hand` [0.59, 0.66]; `match` [0.5, 0.93] |
| `bgL3f_coffin_hand_talisman` | Cùng khung bgL3d: một bàn tay áo nâu (thầy Tư) thò vào từ mép trên, nhét mảnh giấy vàng gấp tư xuống dưới gối ông | 0.95 | 0.4 | `pillow` [0.24, 0.37]; `talisman` [0.3, 0.37] |
| `bgL3m_coffin_mom_hand_talisman` | Cận từ trên: mẹ (áo xô) nằm trong quan tài, chỉ đỏ ở cổ tay, tay thầy Tư nhét bùa dưới gối | 0.95 | 0.4 |  |
| `bgL40_young_couple_sepia` | Hồi ức sepia: ông bà thời trẻ ngồi cạnh nhau trên hiên nhà gỗ, bà cười e thẹn, ông nhìn bà thương mà lo | 0.95 | 0.46 |  |
| `bgL41_grandma_gate_night` | Vẽ sẵn đêm: bà đứng ở cổng sắt hé mở, ôm hai đôi đũa trước ngực, nhìn ra con đường tối om, sợ hãi | 0.95 | 0.46 |  |
| `bgL42_grandma_hug_khoa_dawn` | Vẽ sẵn: nắng sớm tràn vào, hai bà cháu ngồi ôm nhau khóc trước bàn thờ có ba bát cơm | 0.95 | 0.5 |  |
| `bgL44_grandma_teach_incense` | Vẽ sẵn: bà đứng sau Khoa, tay bà đỡ tay cháu cắm ba nén nhang thẳng hàng vào bát hương | 0.95 | 0.5 |  |
| `bgL46_grandma_knit_window` | Vẽ sẵn chiều nắng: bà ngồi bên cửa sổ đan nốt cổ áo len đỏ, bên cạnh máy khâu phủ khăn | 0.93 | 0.5 |  |
| `bgL47_grandma_sweater_on_khoa` | Vẽ sẵn: Khoa mặc áo len đỏ đã có cổ, bà chỉnh cổ áo rồi ngắm, cười; Khoa ngơ ngác | 0.93 | 0.5 |  |
| `bgL48_dinner_grandma_watch` | Vẽ sẵn tối: Khoa (áo len đỏ) ăn cơm có miếng cá; bà (áo bà ba tím mận, trâm bạc) ngồi nhìn, bát đũa của bà để nguyên | 0.95 | 0.46 |  |
| `bgL49_alley_night_two` | Vẽ sẵn đêm không trăng: hai bà cháu (nhìn từ sau) nắm tay đi trong hẻm tối, vệt đèn pin nhỏ | 0.95 | 0.3 |  |
| `bgL4_procession_field` | Đoàn đưa tang nhỏ xa đi trên bờ ruộng gặt trơ gốc, trời âm u, giấy tiền bay | 0.95 | 0.3 |  |
| `bgL50_field_two_walk_night` | Vẽ sẵn đêm (góc rộng): hai bà cháu nắm tay đi trên bờ ruộng gốc rạ, đom đóm, đèn pin nhỏ | 0.9 | 0.2 |  |
| `bgL51_two_graves_night_hole` | Đêm: hai mộ cạnh nhau (mộ ông có lỗ nhỏ ở đầu, mộ mẹ đất mới), cây gạo khô, sương mỏng | 0.95 | 0.42 |  |
| `bgL52_grandma_hand_mom_grave` | Vẽ sẵn đêm: bà quỳ đặt bàn tay lên nấm đất mới của mộ mẹ thì thầm; Khoa (áo len) đứng sau soi đèn | 0.95 | 0.42 |  |
| `bgL53_grandma_dig_bury` | Vẽ sẵn đêm: bà quỳ bới lỗ ở đầu mộ ông bằng tay, lá bùa và đũa KHOA cạnh lỗ; Khoa soi đèn | 0.95 | 0.42 |  |
| `bgL53b_grandma_pat_earth` | Vẽ sẵn đêm: hố đã lấp, bà quỳ vỗ nhẹ nấm đất, đôi đũa của bà nằm ngay ngắn trên đó; Khoa đứng soi đèn | 0.95 | 0.42 |  |
| `bgL54_chopsticks_on_mound` | Cận đêm: bàn tay bà (tay áo lụa tím) đặt đôi đũa khắc tên lên nấm đất đỏ vừa lấp, ánh đèn pin | 0.95 | 0.4 |  |
| `bgL55_ghost_behind_headstone` | Vẽ sẵn đêm: bóng ông đứng sau bia mộ trong sương; bà quỳ không quay lại, nắm chặt tay Khoa | 0.95 | 0.42 |  |
| `bgL56_khoa_walk_away_field` | Vẽ sẵn đêm (góc rộng): Khoa (áo len) đi một mình về phía người xem, cúi đầu khóc, xa sau lưng là nghĩa địa | 0.9 | 0.3 |  |
| `bgL58_grandma_dead_grave_morning` | Vẽ sẵn rạng sáng: bà ngồi tựa mộ ông, đầu nghiêng như ngủ, trâm bạc, một tay đặt trên nấm đất trống | 0.95 | 0.42 |  |
| `bgL59_khoa_cry_altar` | Vẽ sẵn sáng xám: Khoa (áo len) ngồi sụp trước bàn thờ ba bát cơm, ôm chặt mình, khóc nấc | 0.95 | 0.46 |  |
| `bgL5_cemetery_burial_day` | Nghĩa địa ngoài đồng ban ngày âm u: huyệt mới đào có quan tài, đống đất đỏ, xẻng; cây gạo khô trụi lá bên phải | 0.95 | 0.42 |  |
| `bgL5b_burial_shoveling` | Cùng nghĩa địa bgL5: bốn người áo xô xúc đất đỏ lấp huyệt, vài người cúi đầu đứng nhìn | 0.95 | 0.42 | `grave` [0.44, 0.62] |
| `bgL60_wake_coffin_grandma` | Gian thờ đám tang bà (cùng bố cục bgL2c) ban ngày: quan tài đã đóng, di ảnh bà | 0.95 | 0.42 |  |
| `bgL61_khoa_porch_cat_lap` | Vẽ sẵn chiều nắng: Khoa ngồi bậc hiên, mèo mướp cuộn tròn ngủ trong lòng, Khoa mỉm cười | 0.93 | 0.46 |  |
| `bgL62_dinner_co_ut_khoa` | Vẽ sẵn tối: cô Út ngồi mâm cơm cầm ống đũa tò mò ngắm tên khắc, Khoa ngồi đối diện kể chuyện | 0.95 | 0.46 |  |
| `bgL63_khoa_porch_sweater_dusk` | Vẽ sẵn chạng vạng: Khoa (áo len) ngồi một mình bậc hiên nhìn cây bưởi | 0.93 | 0.46 |  |
| `bgL6_old_village_altar_sepia` | Hồi ức (tông nâu sepia): nhà gỗ làng cũ, bàn thờ dài nhiều di ảnh, hàng bốn bát cơm, trẻ con ló nhìn qua cửa | 0.95 | 0.46 |  |
| `bgL7_mom_room_day` | Phòng của mẹ ban ngày: cửa sổ nắng, kệ vải, cuộn chỉ, ma-nơ-canh; chừa trống chỗ đặt máy may (sprite) | 0.93 | 0.5 | `machine_spot` [0.4, 0.8] |
| `bgL7n_mom_room_night` | Phòng mẹ ban đêm (cùng bố cục bgL7), chừa chỗ máy may + nửa phải trống đặt giường (sprite) | 0.93 | 0.5 | `machine_spot` [0.3, 0.88]; `bed_spot` [0.6, 0.95] |
| `bgL8_house_alley_dusk` | Con hẻm lúc chạng vạng, cuối hẻm là căn nhà ống mái rêu với cây bưởi già, một ô cửa sáng đèn | 0.95 | 0.3 |  |
| `bgL9_main_room_altar_ong` | Gian chính (cùng bố cục bg4) đêm: bàn thờ có ảnh ông (giữa) + ảnh bố; bàn ăn để trống | 0.95 | 0.46 | `altar_shelf` [0.31, 0.33]; `dining_table` [0.73, 0.62] |
| `bgL9d_main_room_altar_ong_day` | Gian chính có bàn thờ ông (cùng bố cục bgL9) buổi sáng xám | 0.95 | 0.46 | `altar_shelf` [0.31, 0.33]; `dining_table` [0.73, 0.62] |
| `bgL9m_main_room_altar_three` | Gian chính đêm: kệ thờ có ảnh ông, bố, mẹ và hai bát cơm | 0.95 | 0.46 | `altar_shelf` [0.3, 0.33] |
| `bgL9md_main_room_altar_three_day` | Gian chính ban ngày xám: kệ thờ ba di ảnh (ông, bố, mẹ), mặt kệ trống đặt bát; sàn trái trống | 0.95 | 0.46 |  |
| `bgL9s_grandma_asleep_table` | Vẽ sẵn: bà gục đầu ngủ trên bàn ăn trong gian thờ ban đêm; bàn thờ có một bát cơm trước ảnh ông | 0.95 | 0.46 | `grandma` [0.8, 0.7] |
