# Kho asset — mục lục (bản ngắn)

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.
> Chi tiết từng nhân vật (sprite, hướng, neo, khung chu kỳ): `assets/catalog/<nhân vật>.md` — chỉ mở nhân vật truyện cần.
> Phông (floor_y, char_h, toạ độ điểm nóng): `assets/catalog/backgrounds.md`.
> Style prompt + ảnh tham chiếu (chỉ cần khi viết `asset_requests`; check_story tự ghép vào prompt): `assets/catalog/PROMPTS.md`.
> Ảnh xem nhanh (chỉ mở khi mô tả chữ chưa đủ): `assets/catalog/<nhân vật>.png`, `assets/catalog/backgrounds.png`.

## Nhân vật

| Nhân vật | Tên | Sprite | Cao | Chu kỳ (`"cycle": "<nv>/<tên>"`) |
|---|---|---|---|---|
| `ba_sau` | Bà Sáu bán xôi | 2 | 0.5 |  |
| `boy_hoodie` | Khoa — cậu trai hoodie xanh | 95 | 0.46 | `walk`(6), `flashlight_walk`(6), `tiptoe`(4), `back_walk`(4), `run`(4), `blink`(5), `run_away`(4), `run_jacket`(6), `talk`(4) |
| `cat_tabby` | Mèo mướp nhà bên | 6 | 0.14 | `run`(4) |
| `co_ut` | Cô Út (em gái út của bố) | 4 | 0.58 |  |
| `ghost_mother` | "Mẹ" — ma nữ tóc dài | 8 | 0.66 | `walk`(2) |
| `grandma` | Bà nội | 47 | 0.5 | `walk`(6), `fake_walk`(4) |
| `hungry_ghost` | Cô hồn đói | 7 | 0.6 |  |
| `mother_alive` | Mẹ lúc còn sống (cùng người với ma "Mẹ") | 31 | 0.62 | `walk`(6) |
| `ong_noi` | Ông nội | 17 | 0.58 |  |
| `props` | Đạo cụ (bát cơm cúng, nhang, dấu tay, dép) | 57 | 0.2 | `fire`(3), `crow_fly`(4) |
| `thay_tu` | Thầy Tư (thầy cúng) | 10 | 0.58 |  |

## Phông nền

| Phông | Mô tả | Điểm nóng (`pin.at`) |
|---|---|---|
| `bg10_river_wharf` | Bến sông thị trấn ban đêm: bậc đá xuống mặt nước đen, sương mỏng, bụi tre bên phải, bờ xa có một đốm đèn |  |
| `bg11_peephole_yard` | Nhìn qua mắt mèo cửa chính: khung tròn giữa nền đen, sân xi măng ánh trăng bị bóp méo, cổng sắt xa |  |
| `bg12_bedside_drawer` | Cận tủ đầu giường gỗ, ngăn kéo mở: khăn tay, lược gỗ, tràng hạt của bà, chừa chỗ trống giữa ngăn đặt lọ dầu |  |
| `bg1_bedroom` | Phòng ngủ ban đêm, KHÔNG có giường (dùng sprite G1–G3). Cửa phòng bên trái, cửa sổ ánh trăng giữa, tủ đầu giường + đồng hồ 03:00, nửa phải sàn trống. | bedroom_door, bedroom_door_handle, window, clock, bed_spot |
| `bg1c_corner_night` | Góc phòng ngủ ban đêm, Khoa vẽ sẵn: ngồi co ro trong góc, bịt hai tai, MẮT MỞ TRỪNG nhìn về phía cửa (trái), khe sáng vàng dưới cửa, mép giường bên phải. | boy_face, door, door_gap |
| `bg1d_corner_dawn` | Góc phòng ngủ lúc rạng đông (đã chỉnh sáng), Khoa vẫn ngồi bịt tai, mắt đỏ thâm quầng, thức trắng cả đêm. | boy_face, door |
| `bg2_hallway` | Hành lang dài nằm ngang, sàn gỗ, 2 cửa đóng, ảnh gia đình mờ trên tường, hai đầu tối. | door_left, door_right, family_photo, far_end |
| `bg3_front_door` | Cửa chính nhìn từ trong nhà, ở giữa; lỗ mắt mèo (cao, quá tầm cậu bé), tay nắm bên trái cửa, tủ giày bên trái, móc áo bên phải, khe sáng vàng dưới cửa. | door_handle, peephole, door_center, door_bottom_y, shoe_rack, coat_hooks |
| `bg3b_peephole` | Góc nhìn qua mắt mèo: khung tròn giữa nền đen, hành lang chung cư bị bóp méo, đèn trần mờ. | lens_circle, corridor_floor, far_door |
| `bg4_main_room` | Gian nhà chính ban đêm: bàn thờ treo tường bên trái (ảnh thờ, bát hương, 2 nến đỏ, đĩa hoa quả, bát cơm), bàn ăn thấp + 2 ghế đẩu bên phải, lịch treo tường, cửa xuống bếp sát mép phải. Nửa trái sàn trống. | altar_shelf, altar_portrait, altar_rice, altar_incense, dining_table, table_top_y, stool_left, stool_right, kitchen_door, calendar, open_floor |
| `bg4d_main_room_day` | Gian nhà chính (cùng bố cục BG4) chiều nắng ấm trong hồi ức: kệ chỉ có bình hoa + bát, không ảnh thờ; nồi canh bốc khói trên bàn ăn. | altar_shelf, altar_portrait, altar_rice, altar_incense, dining_table, table_top_y, stool_left, stool_right, kitchen_door, calendar, open_floor |
| `bg4e_main_room_day_bo` | Gian chính ban ngày (như bg4d): kệ thờ trên tường có di ảnh bố, bát hương, 2 nến; bàn ăn nồi canh, ghế đẩu | altar_shelf, dining_table |
| `bg5_altar_close` | Cận mặt bàn thờ ban đêm: ảnh thờ mẹ (dải băng tang đen) ở giữa, bát hương đồng với 3 nén nhang khói bên trái, 2 nến đỏ, đĩa và chân nến bên phải. Mặt gỗ phía trước trống để đặt đạo cụ (bát cơm). | portrait, portrait_face, incense_bowl, incense_tips, candle_left, candle_right, offering_spot, plate |
| `bg5b_altar_grandpa_lit` | Cận bàn thờ ÔNG nội ban đêm: ảnh thờ ông, bát hương có 3 nén nhang đang cháy khói, 2 nến sáng |  |
| `bg5c_altar_grandpa_cold` | Cùng bố cục bg5b nhưng nguội lạnh: chỉ còn chân nhang trơ trọi, không khói, nến tắt, bụi |  |
| `bg6_kitchen` | Bếp nhà ống ban đêm: bệ bếp lát gạch bên trái (bếp ga 2 lò + nồi nhôm, nồi cơm điện, giá bát, ống đũa), cửa sổ song sắt hắt ánh trăng, ô cửa tối om dẫn ra nhà sau ở giữa-phải. Sàn giữa và phải trống. | doorway, doorway_floor, stove_pot, rice_cooker, window, dish_rack, open_floor |
| `bg6d_kitchen_day` | Bếp (cùng bố cục BG6) chiều nắng vàng trong hồi ức, nồi trên bếp bốc hơi, ô cửa sáng. | doorway, doorway_floor, stove_pot, rice_cooker, window, dish_rack, open_floor |
| `bg7_front_yard` | Sân trước nhà ban đêm: chậu cây + bàn cúng nhỏ ngoài trời bên trái, cổng sắt xếp hoen gỉ chiếm nửa phải, khe hở giữa cổng nhìn ra đường vắng có sương và cột đèn xa. Nền xi măng nứt. | offering_table, offering_table_top, gate_gap, gate_gap_floor, gate_left, gate_right, street_lamp, open_floor |
| `bg7d_front_yard_morning` | Sân trước buổi sáng sớm (cùng bố cục bg7): nắng nhạt, cổng mở hé, ngoài đường có người đạp xe, người đi bộ, hàng quán |  |
| `bg8_bedroom_door` | Trong phòng ngủ nhìn thẳng vào cửa phòng đóng (giữa khung): tay nắm + chốt cài, khe sáng vàng dưới chân cửa hắt lên sàn gỗ; hai tờ tranh vẽ dán tường hai bên. | door_center, door_handle, bolt_lock, door_gap, door_gap_left, door_gap_right |
| `bg9b_door_gap_ghosts` | POV qua khe dưới cửa: đám cô hồn ngồi xổm quanh mâm cơm (khe cắt ngang người, thấy gối, chân, tay đen bốc cơm), bát đổ, một con nhỏ ở xa. Vẽ sẵn, không cần sprite. | slit_center, tray, far_ghost |
| `bg9c_door_gap_face` | POV qua khe dưới cửa: một cô hồn áp mặt xuống sàn sát cửa, hốc mắt đen nhìn thẳng vào khe, miệng dính cơm (cú hù). Vẽ sẵn. | slit_center, ghost_face |
| `bgL10_altar_four_portraits` | Bàn thờ đêm có 4 di ảnh: ông, mẹ, bà và khung thứ tư phủ kín vải đen; mặt trước trống để đặt bát cơm | offering_spot |
| `bgL10b_altar_four_portraits` | Bàn thờ 4 di ảnh (ông, mẹ, bà, khung phủ vải đen), lư hương nhỏ ở giữa mép trước, chỗ trống trước từng di ảnh để đặt bát | offering_spot, incense |
| `bgL11_ong_bed_corner_night` | Góc nhà cạnh gian thờ ban đêm: bàn thờ treo nhỏ (ảnh bố), đồng hồ quả lắc trên tường, cửa sổ trăng; sàn trống đặt giường tre (sprite) | bed_spot, clock |
| `bgL12_living_room_day` | Phòng khách buổi sáng xám: chiếu cói giữa nhà, tủ thấp, khay trà, bàn thờ trên cao; sàn trống | mat_center |
| `bgL13_home_altar_bo` | Cận bàn thờ cũ trong nhà (ảnh bố), nửa phải là tường trống để treo gương phủ vải đỏ | portrait, mirror_spot |
| `bgL14_grandma_comb_coffin` | Vẽ sẵn: bà ngồi ghế thấp bên quan tài, chải tóc bạc cho ông (thấy đầu ông trên mép quan tài), thì thầm | grandma, ong_head |
| `bgL14b_grandma_by_coffin` | Góc thấp: thành quan tài che kín (không thấy ông), bà ngồi ghế đẩu bên phải, lược trong lòng, tay đặt lên thành quan tài thì thầm | grandma |
| `bgL15_khoa_bed_awake_night` | Vẽ sẵn: Khoa nằm mắt mở thao láo trên giường, tay nắm áo khoác đen treo đầu giường, đồng hồ gần 3 giờ | boy, clock |
| `bgL15b_khoa_bed_awake_plain` | Vẽ sẵn: Khoa nằm thao láo, hai tay để trên chăn (không chạm áo khoác treo đầu giường) | boy |
| `bgL16_market_morning` | Đầu chợ quê buổi sáng: mái bạt, gánh rau, hàng xôi bốc hơi; bậc đá trống ở tiền cảnh, nắng sớm | stone_step |
| `bgL16b_market_side_step` | Đầu chợ buổi sáng: đường giữa thông, bậc đá trước một sạp đóng cửa ở mép trái tiền cảnh | stone_step |
| `bgL17_cemetery_night_grave` | Nghĩa địa đêm: mộ ông mới đắp đất đỏ, bia nhỏ, cây gạo khô bên phải, sương mỏng; chừa chỗ quỳ và chỗ sau bia | grave_head, behind_headstone, crow_branch |
| `bgL17b_two_graves_day` | Ban ngày âm u: hai mộ cạnh nhau (mộ ông đất se mặt có lỗ nhỏ ở đầu, mộ mẹ đất tươi), cây gạo khô | hole, crow_branch |
| `bgL17c_two_graves_small_hole` | Hai mộ cạnh nhau ban ngày; đầu mộ ông chỉ có một lỗ nhỏ trẻ con bới, đất vương vãi | hole, crow_branch |
| `bgL18_field_path_night` | Bờ ruộng đêm chạy ngang khung, cỏ may rạp trong gió, xa xa hàng cây và cây gạo khô | path |
| `bgL19_mirror_ong_behind_mom` | Vẽ sẵn: trong gương, mẹ (áo xô, tóc xoã) xới cơm, ông áo the đứng sau đặt tay lên tay mẹ cầm muôi | mirror |
| `bgL19b_mirror_khoa_alone` | Vẽ sẵn: cùng gương, chỉ còn Khoa đứng một mình giữa gian thờ tối, sau lưng hai bát cơm | mirror |
| `bgL19c_mirror_ong_whisper` | Vẽ sẵn: trong gương, mẹ bưng bát cơm, ông áo the đứng sau đặt tay lên tay mẹ, ghé tai thì thầm | mirror |
| `bgL1_porch_day` | Hiên nhà ống chiều nắng vàng: cửa gỗ bên trái, nền gạch, cây bưởi già sai quả bên phải, tường rào thấp |  |
| `bgL1n_porch_night` | Hiên nhà (cùng bố cục bgL1) ban đêm, ánh trăng qua lá bưởi, đèn vàng hắt ra từ cửa |  |
| `bgL20b_wake_coffin_mom_open` | Gian thờ đám tang mẹ (cùng bố cục bgL2): quan tài mở nắp, di ảnh mẹ |  |
| `bgL21b_altar_three` | Cận bàn thờ: ảnh ông (giữa), ảnh bố, ảnh mẹ mới; nhang khói, nến; mặt bàn trống đặt bát | offering_ong, offering_me |
| `bgL22_backyard_morning` | Sân sau bếp buổi sáng xám: cửa bếp bên trái, giếng gạch, chum nước, dây phơi, bụi chuối; nền đất trống | open_ground |
| `bgL23_house_roof_dusk` | Sân trước lúc chạng vạng nhìn lên nóc nhà mái rêu (chỗ quạ đậu) và cây bưởi bên phải | roof_ridge, pomelo_branch |
| `bgL24_altar_ong_bo_cold` | Cận bàn thờ nguội: ảnh ông + ảnh bố nhỏ bên cạnh, nến tắt; mặt bàn trống đặt bát | offering_left, offering_right |
| `bgL25_mom_bed_sick_night` | Vẽ sẵn: mẹ ốm nằm trên giường trong phòng mẹ ban đêm | bed_foot |
| `bgL25b_mom_bed_bowl_morning` | Vẽ sẵn (đêm/rạng sáng): mẹ ngủ, bát cơm sát gối, đũa gác ngang miệng bát chĩa vào mặt mẹ | bowl |
| `bgL25c_mom_bed_sit_bowl_morning` | Vẽ sẵn (đêm/rạng sáng): mẹ ngồi dậy trên giường, siết chăn, nhìn bát cơm cạnh gối | bowl |
| `bgL25d_mom_dead_morning` | Vẽ sẵn: sáng sớm lạnh, mẹ (áo xô) nằm mất trên giường, bình thản như ngủ |  |
| `bgL25e_mom_bedroom_day` | Phòng mẹ buổi sáng nắng, giường gọn; sàn trái trống | open_floor |
| `bgL25h_mom_stroke_khoa_night` | Vẽ sẵn: phòng mẹ ban đêm, mẹ nằm đưa tay xoa đầu Khoa ngồi ghế cạnh giường cúi đầu khóc | mother, boy |
| `bgL25k_mom_knit_collar` | Vẽ sẵn: mẹ ngồi trên giường cố đan cổ áo len, tay run; Khoa ngồi cạnh nhìn |  |
| `bgL25m_khoa_hold_mom_hand` | Vẽ sẵn: mẹ (áo xô, tóc xoã) nằm thở yếu, Khoa ngồi bệt áp tay mẹ lên má khóc |  |
| `bgL25n_mom_bedroom_night` | Phòng ngủ của mẹ ban đêm: giường gỗ đôi to sát tường (đầu giường bên trái), màn buộc, tủ nhỏ; sàn trái trống | pillow, bed_foot, open_floor |
| `bgL25s_khoa_feed_soup` | Vẽ sẵn: chiều, Khoa ngồi mép giường bón canh cho mẹ trong phòng mẹ |  |
| `bgL26_mom_sewing_tunic` | Vẽ sẵn: mẹ ngồi khóc bên máy khâu, bộ áo xô may xong nằm trên bàn máy, áo len rơi dưới gầm | mother |
| `bgL27_khoa_peek_door_day` | Góc nhìn của Khoa nép sau cánh cửa buồng: chỉ thấy bàn tay bám mép cửa, khe cửa nhìn ra gian thờ (ảnh bố, bàn ăn) | boy |
| `bgL28_khoa_calendar_night` | Vẽ sẵn: Khoa đứng khoanh ngày trên tờ lịch treo tường dưới ánh đèn bàn | calendar |
| `bgL29_grandma_room_portrait` | Vẽ sẵn: phòng bà ban đêm đèn dầu, bà ngồi mép giường ôm di ảnh ông khóc thì thầm | grandma |
| `bgL2_wake_coffin` | Gian thờ đám tang ban đêm: quan tài gỗ mở nắp (nắp dựng tường phải) đặt giữa, đầu bên trái; bàn thờ có di ảnh ông, 2 nến, vòng hoa giấy; chiếu trước |  |
| `bgL2c_wake_coffin_closed` | Gian thờ (cùng bố cục bgL2) sáng đưa tang: nắp quan tài đã đóng đinh, phủ khăn đỏ vàng |  |
| `bgL2n_wake_candles_out` | Gian thờ (cùng bố cục bgL2) nến đã tắt, tối om, chỉ còn ba đầu nhang đỏ lập loè | coffin_head |
| `bgL30_khoa_dig_grave_night` | Vẽ sẵn: Khoa (áo khoác đen) quỳ bới lỗ nhỏ ở đầu mộ ông, đèn pin nằm cạnh |  |
| `bgL31_mirror_opposite_room` | Nhìn qua khung cửa sang phòng đối diện: tấm vải đỏ đang tuột khỏi chiếc gương lớn | mirror |
| `bgL3a_coffin_top_hands_chest` | Cận từ trên xuống trong quan tài: ông nằm, áo the, hai tay đặt trên ngực, góc lá bùa vàng ló dưới gối |  |
| `bgL3c_coffin_face_smile` | Cận mặt ông trong quan tài (ảo giác): mắt hé mở nhìn thẳng, miệng cười toác rợn người, ánh que diêm | face |
| `bgL3d_coffin_top_full` | Nhìn thẳng từ trên xuống: quan tài nằm ngang (đầu trái, chân phải), thấy trọn cả người ông (đủ chân, đúng tỉ lệ), tay đặt ngực; lá bùa khuất dưới gối nên không thấy | face, hands, pillow, feet |
| `bgL3e_coffin_top_full_dropped` | Cùng khung bgL3d: tay phải buông thõng cạnh gối, chỉ còn ánh que diêm, khoé miệng hơi nhếch | face, dropped_hand, match |
| `bgL3f_coffin_hand_talisman` | Cùng khung bgL3d: một bàn tay áo nâu (thầy Tư) thò vào từ mép trên, nhét mảnh giấy vàng gấp tư xuống dưới gối ông | pillow, talisman |
| `bgL3m_coffin_mom_hand_talisman` | Cận từ trên: mẹ (áo xô) nằm trong quan tài, chỉ đỏ ở cổ tay, tay thầy Tư nhét bùa dưới gối |  |
| `bgL4_procession_field` | Đoàn đưa tang nhỏ xa đi trên bờ ruộng gặt trơ gốc, trời âm u, giấy tiền bay |  |
| `bgL5_cemetery_burial_day` | Nghĩa địa ngoài đồng ban ngày âm u: huyệt mới đào có quan tài, đống đất đỏ, xẻng; cây gạo khô trụi lá bên phải |  |
| `bgL5b_burial_shoveling` | Cùng nghĩa địa bgL5: bốn người áo xô xúc đất đỏ lấp huyệt, vài người cúi đầu đứng nhìn | grave |
| `bgL6_old_village_altar_sepia` | Hồi ức (tông nâu sepia): nhà gỗ làng cũ, bàn thờ dài nhiều di ảnh, hàng bốn bát cơm, trẻ con ló nhìn qua cửa |  |
| `bgL7_mom_room_day` | Phòng của mẹ ban ngày: cửa sổ nắng, kệ vải, cuộn chỉ, ma-nơ-canh; chừa trống chỗ đặt máy may (sprite) | machine_spot |
| `bgL7n_mom_room_night` | Phòng mẹ ban đêm (cùng bố cục bgL7), chừa chỗ máy may + nửa phải trống đặt giường (sprite) | machine_spot, bed_spot |
| `bgL8_house_alley_dusk` | Con hẻm lúc chạng vạng, cuối hẻm là căn nhà ống mái rêu với cây bưởi già, một ô cửa sáng đèn |  |
| `bgL9_main_room_altar_ong` | Gian chính (cùng bố cục bg4) đêm: bàn thờ có ảnh ông (giữa) + ảnh bố; bàn ăn để trống | altar_shelf, dining_table |
| `bgL9d_main_room_altar_ong_day` | Gian chính có bàn thờ ông (cùng bố cục bgL9) buổi sáng xám | altar_shelf, dining_table |
| `bgL9m_main_room_altar_three` | Gian chính đêm: kệ thờ có ảnh ông, bố, mẹ và hai bát cơm | altar_shelf |
| `bgL9s_grandma_asleep_table` | Vẽ sẵn: bà gục đầu ngủ trên bàn ăn trong gian thờ ban đêm; bàn thờ có một bát cơm trước ảnh ông | grandma |

## Âm thanh

Dùng trong cảnh: `"sfx": [{"sound": <tên>, "at": 0.3}]`; nhạc nền: `"music"` ở cấp kịch bản.

| Âm thanh | Loại | Mô tả | Âm lượng |
|---|---|---|---|
| `bamboo_whittle` | sfx | Dao nhỏ gọt khắc tre lách tách, lặp được | 0.6 |
| `body_fall` | sfx | Người ngã ngửa xuống sàn gỗ | 1.0 |
| `breath_close` | sfx | Hơi thở run rẩy sát tai | 0.7 |
| `cat_hiss` | sfx | Mèo xù lông rít lên rồi chạy mất | 1.0 |
| `chant_murmur` | sfx | Ông thầy khấn lầm rầm không rõ lời, lặp được | 0.5 |
| `chewing_wet` | sfx | Nhiều miệng nhai nhóp nhép, húp vội (lặp được) | 0.8 |
| `chickens_cluck` | sfx | Mấy con gà mái cục tác, mổ thóc trong sân | 0.6 |
| `chopsticks_clatter` | sfx | Rất nhiều đôi đũa va bát lách cách gấp gáp | 0.8 |
| `chopsticks_tap_2` | sfx | Đầu đũa tre gõ khẽ vào miệng bát sứ HAI tiếng | 0.9 |
| `clock_chime_3` | sfx | Đồng hồ quả lắc gõ ba tiếng boong ngân | 0.9 |
| `clock_tick` | sfx | Đồng hồ tích tắc nhỏ, lặp được | 0.5 |
| `cloth_slide` | sfx | Tấm vải từ từ trượt xuống rồi rơi khẽ xuống sàn | 0.8 |
| `coffin_nails` | sfx | Búa đóng đinh dài vào gỗ quan tài, từng nhát chát chúa | 0.9 |
| `cough_old` | sfx | Bà già ho khù khụ, khô, ba tràng | 1.0 |
| `crow_caw` | sfx | Một con quạ kêu khàn khàn (1–2 tiếng) | 0.9 |
| `dog_howl` | sfx | Một con chó tru dài thê lương từ xa | 0.8 |
| `door_bang` | sfx | Đập cửa gỗ dồn dập, hoảng loạn | 1.0 |
| `door_bolt_lock` | sfx | Chốt cửa kim loại gài lại, tách gọn | 0.8 |
| `door_creak_open` | sfx | Cửa gỗ phòng ngủ từ từ mở kẽo kẹt dài | 0.8 |
| `door_handle_rattle` | sfx | Tay nắm cửa bị vặn lạch cạch | 0.9 |
| `door_scratch` | sfx | Móng tay cào chậm lên cửa gỗ từ phía bên ngoài, lặp được | 0.9 |
| `door_slam` | sfx | Đóng sầm cửa gỗ | 0.9 |
| `drone_low` | music | Nhạc nền u ám trầm, lặp được | 0.7 |
| `flashlight_click` | sfx | Tiếng bật công tắc đèn pin | 0.9 |
| `flicker_buzz` | sfx | Đèn chập chờn rè điện | 0.7 |
| `floor_creak` | sfx | Sàn gỗ kêu kẽo kẹt một tiếng | 0.8 |
| `footsteps_run` | sfx | Tiếng chạy gấp trên sàn gỗ | 0.8 |
| `footsteps_slow` | sfx | Bước chân chậm trên sàn gỗ, lặp được | 0.7 |
| `frogs_night` | sfx | Ếch nhái kêu ran ven sông ban đêm (lặp được) | 1.0 |
| `funeral_band` | sfx | Kèn trống đám ma Việt (kèn bầu, trống) buồn, lặp được | 0.6 |
| `gate_knock_metal` | sfx | Ba tiếng gõ chậm lên cổng sắt gỉ | 1.0 |
| `gate_rattle` | sfx | Cổng sắt xếp bị lay rung lạch cạch | 0.8 |
| `ghost_stinger` | sfx | Tiếng hù jumpscare khi ma xuất hiện (đánh mạnh + rít) | 1.0 |
| `hangup_tone` | sfx | Tiếng tút tút khi đầu dây bên kia cúp máy | 0.7 |
| `heartbeat` | sfx | Tim đập căng thẳng, lặp được | 0.8 |
| `knitting_needles` | sfx | Que đan len gõ lách cách nhẹ, chậm, lặp được | 0.6 |
| `knock_2_hesitant` | sfx | Hai tiếng gõ cửa gỗ ngập ngừng, rồi im | 1.0 |
| `knock_3` | sfx | Cốc… cốc… cốc — ba tiếng gõ cửa gỗ chậm rãi | 1.0 |
| `market_morning` | sfx | Chợ quê buổi sáng: tiếng người nói xa, rao hàng, xe đạp, lặp được | 0.5 |
| `match_strike` | sfx | Quẹt diêm bùng lửa | 0.9 |
| `memory_piano` | music | Piano buồn nhẹ, hoài niệm (cho đoạn kỷ niệm gia đình), lặp được | 0.5 |
| `motorbike_stop` | sfx | Xe máy chạy tới dừng lại rồi tắt máy, trời mưa | 1.0 |
| `mourners_cry` | sfx | Tiếng nhiều người khóc than đám tang, xa, lặp được | 0.5 |
| `night_insects` | sfx | Không khí đêm: dế, tắc kè kêu xa, yên tĩnh (lặp được) | 0.8 |
| `old_man_breath` | sfx | Ông già thở nặng nhọc, khò khè, lặp được | 0.6 |
| `old_man_cough` | sfx | Ông già ho khan từng tràng | 0.9 |
| `paper_burn` | sfx | Đốt vàng mã trong thùng sắt, lửa lách tách (lặp được) | 0.8 |
| `phone_drop` | sfx | Điện thoại rơi xuống sàn gỗ | 0.9 |
| `phone_ring` | sfx | Chuông điện thoại di động đổ giữa đêm (nhạc chuông mặc định, lặp được) | 0.8 |
| `phone_vibrate` | sfx | Điện thoại rung báo tin nhắn (2 lần) | 0.9 |
| `rain_roof` | sfx | Mưa đều trên mái tôn, nước nhỏ giọt máng (lặp được) | 0.8 |
| `reverse_swell` | sfx | Tiếng rít tăng dần (riser) trước khi hù | 0.8 |
| `rice_ladle_scoop` | sfx | Muôi gỗ xới cơm lạo xạo vào bát sứ, chậm, từng muôi | 0.8 |
| `rice_scatter` | sfx | Nắm gạo muối rải xuống sân xi măng | 0.8 |
| `ritual_bell` | sfx | Mõ gõ ba tiếng rồi chuông đồng nhỏ ngân | 0.8 |
| `river_lapping` | sfx | Nước sông vỗ nhẹ vào bậc đá ban đêm (lặp được) | 1.0 |
| `rooster_crow` | sfx | Một tiếng gà gáy xa lúc rạng sáng | 1.0 |
| `scissors_hair` | sfx | Kéo cắt một lọn tóc | 1.0 |
| `sewing_machine` | sfx | Máy khâu đạp chân cũ chạy lạch cạch đều, lặp được | 0.6 |
| `shovel_dirt` | sfx | Xúc đất hất xuống nắp gỗ, từng xẻng | 0.8 |
| `slipper_drag` | sfx | Tiếng dép lê lẹp xẹp kéo lê trên sàn gạch (lặp được) | 0.8 |
| `soil_dig_hands` | sfx | Bới đất ẩm bằng tay, sột soạt, lặp được | 0.7 |
| `spoon_bowl_tap` | sfx | Thìa kim loại gõ khẽ thành bát ba lần | 0.8 |
| `water_drip` | sfx | Nước nhỏ tong tỏng xuống nền gạch (lặp được) | 1.0 |
| `whisper_eerie` | sfx | Tiếng thì thầm rợn người của phụ nữ (không rõ lời) | 0.8 |
| `wind_field` | sfx | Gió đồng thổi rì rào qua ruộng, lặp được | 0.6 |
| `wind_gust_candle` | sfx | Một luồng gió lạnh lùa qua phòng (thổi tắt nến) | 0.8 |
| `wings_flap` | sfx | Chim lớn vỗ cánh bay lên | 0.8 |
| `woman_sob_door` | sfx | Tiếng phụ nữ khóc nghẹn sau cánh cửa gỗ | 0.8 |
| `wood_block_slow` | sfx | Tiếng mõ gỗ gõ đều đều chậm (tụng kinh), lặp được | 0.5 |
