# Kho asset — mục lục (bản ngắn)

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.
> Chi tiết từng nhân vật (sprite, hướng, neo, khung chu kỳ): `assets/catalog/<nhân vật>.md` — chỉ mở nhân vật truyện cần.
> Phông (floor_y, char_h, toạ độ điểm nóng): `assets/catalog/backgrounds.md`.
> Style prompt + ảnh tham chiếu (chỉ cần khi viết `asset_requests`; check_story tự ghép vào prompt): `assets/catalog/PROMPTS.md`.
> Ảnh xem nhanh (chỉ mở khi mô tả chữ chưa đủ): `assets/catalog/<nhân vật>.png`, `assets/catalog/backgrounds.png`.

## Nhân vật

| Nhân vật | Tên | Sprite | Cao | Chu kỳ (`"cycle": "<nv>/<tên>"`) |
|---|---|---|---|---|
| `ba_sau` | Bà Sáu bán xôi | 3 | 0.5 |  |
| `boy_hoodie` | Khoa — cậu trai hoodie xanh | 80 | 0.46 | `walk`(6), `flashlight_walk`(6), `tiptoe`(4), `back_walk`(4), `run`(4), `talk`(4), `blink`(5) |
| `cat_tabby` | Mèo mướp nhà bên | 6 | 0.14 | `run`(4) |
| `ghost_mother` | "Mẹ" — ma nữ tóc dài | 13 | 0.66 | `walk`(2) |
| `grandma` | Bà nội | 49 | 0.5 | `walk`(6), `walk_old`(6), `walk_v2`(6), `fake_walk`(4) |
| `hungry_ghost` | Cô hồn đói | 7 | 0.6 |  |
| `mother_alive` | Mẹ lúc còn sống (cùng người với ma "Mẹ") | 26 | 0.62 | `walk`(6), `walk_old`(6), `walk_v2`(6) |
| `props` | Đạo cụ (bát cơm cúng, nhang, dấu tay, dép) | 22 | 0.2 | `fire`(3) |

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
| `bg5_altar_close` | Cận mặt bàn thờ ban đêm: ảnh thờ mẹ (dải băng tang đen) ở giữa, bát hương đồng với 3 nén nhang khói bên trái, 2 nến đỏ, đĩa và chân nến bên phải. Mặt gỗ phía trước trống để đặt đạo cụ (bát cơm). | portrait, portrait_face, incense_bowl, incense_tips, candle_left, candle_right, offering_spot, plate |
| `bg5b_altar_grandpa_lit` | Cận bàn thờ ÔNG nội ban đêm: ảnh thờ ông, bát hương có 3 nén nhang đang cháy khói, 2 nến sáng |  |
| `bg5c_altar_grandpa_cold` | Cùng bố cục bg5b nhưng nguội lạnh: chỉ còn chân nhang trơ trọi, không khói, nến tắt, bụi |  |
| `bg6_kitchen` | Bếp nhà ống ban đêm: bệ bếp lát gạch bên trái (bếp ga 2 lò + nồi nhôm, nồi cơm điện, giá bát, ống đũa), cửa sổ song sắt hắt ánh trăng, ô cửa tối om dẫn ra nhà sau ở giữa-phải. Sàn giữa và phải trống. | doorway, doorway_floor, stove_pot, rice_cooker, window, dish_rack, open_floor |
| `bg6d_kitchen_day` | Bếp (cùng bố cục BG6) chiều nắng vàng trong hồi ức, nồi trên bếp bốc hơi, ô cửa sáng. | doorway, doorway_floor, stove_pot, rice_cooker, window, dish_rack, open_floor |
| `bg7_front_yard` | Sân trước nhà ban đêm: chậu cây + bàn cúng nhỏ ngoài trời bên trái, cổng sắt xếp hoen gỉ chiếm nửa phải, khe hở giữa cổng nhìn ra đường vắng có sương và cột đèn xa. Nền xi măng nứt. | offering_table, offering_table_top, gate_gap, gate_gap_floor, gate_left, gate_right, street_lamp, open_floor |
| `bg7d_front_yard_morning` | Sân trước buổi sáng sớm (cùng bố cục bg7): nắng nhạt, cổng mở hé, ngoài đường có người đạp xe, người đi bộ, hàng quán |  |
| `bg8_bedroom_door` | Trong phòng ngủ nhìn thẳng vào cửa phòng đóng (giữa khung): tay nắm + chốt cài, khe sáng vàng dưới chân cửa hắt lên sàn gỗ; hai tờ tranh vẽ dán tường hai bên. | door_center, door_handle, bolt_lock, door_gap, door_gap_left, door_gap_right |
| `bg9_door_gap` | Góc nhìn nằm sát sàn qua khe dưới cửa (POV của Khoa): khung đen, khe ngang ở giữa (y 0.35–0.69) nhìn ra sàn gạch gian thờ, ánh nến đỏ xa. Nhân vật đặt nhỏ ở xa để lọt trong khe. | slit_center, far_floor, mid_floor, red_glow |
| `bg9b_door_gap_ghosts` | POV qua khe dưới cửa: đám cô hồn ngồi xổm quanh mâm cơm (khe cắt ngang người, thấy gối, chân, tay đen bốc cơm), bát đổ, một con nhỏ ở xa. Vẽ sẵn, không cần sprite. | slit_center, tray, far_ghost |
| `bg9c_door_gap_face` | POV qua khe dưới cửa: một cô hồn áp mặt xuống sàn sát cửa, hốc mắt đen nhìn thẳng vào khe, miệng dính cơm (cú hù). Vẽ sẵn. | slit_center, ghost_face |

## Âm thanh

Dùng trong cảnh: `"sfx": [{"sound": <tên>, "at": 0.3}]`; nhạc nền: `"music"` ở cấp kịch bản.

| Âm thanh | Loại | Mô tả | Âm lượng |
|---|---|---|---|
| `body_fall` | sfx | Người ngã ngửa xuống sàn gỗ | 1.0 |
| `breath_close` | sfx | Hơi thở run rẩy sát tai | 0.7 |
| `cat_hiss` | sfx | Mèo xù lông rít lên rồi chạy mất | 1.0 |
| `chewing_wet` | sfx | Nhiều miệng nhai nhóp nhép, húp vội (lặp được) | 0.8 |
| `chopsticks_clatter` | sfx | Rất nhiều đôi đũa va bát lách cách gấp gáp | 0.8 |
| `clock_tick` | sfx | Đồng hồ tích tắc nhỏ, lặp được | 0.5 |
| `cough_old` | sfx | Bà già ho khù khụ, khô, ba tràng | 1.0 |
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
| `gate_knock_metal` | sfx | Ba tiếng gõ chậm lên cổng sắt gỉ | 1.0 |
| `gate_rattle` | sfx | Cổng sắt xếp bị lay rung lạch cạch | 0.8 |
| `ghost_stinger` | sfx | Tiếng hù jumpscare khi ma xuất hiện (đánh mạnh + rít) | 1.0 |
| `hangup_tone` | sfx | Tiếng tút tút khi đầu dây bên kia cúp máy | 0.7 |
| `heartbeat` | sfx | Tim đập căng thẳng, lặp được | 0.8 |
| `knock_2_hesitant` | sfx | Hai tiếng gõ cửa gỗ ngập ngừng, rồi im | 1.0 |
| `knock_3` | sfx | Cốc… cốc… cốc — ba tiếng gõ cửa gỗ chậm rãi | 1.0 |
| `motorbike_stop` | sfx | Xe máy chạy tới dừng lại rồi tắt máy, trời mưa | 1.0 |
| `night_insects` | sfx | Không khí đêm: dế, tắc kè kêu xa, yên tĩnh (lặp được) | 0.8 |
| `paper_burn` | sfx | Đốt vàng mã trong thùng sắt, lửa lách tách (lặp được) | 0.8 |
| `phone_drop` | sfx | Điện thoại rơi xuống sàn gỗ | 0.9 |
| `phone_ring` | sfx | Chuông điện thoại di động đổ giữa đêm (nhạc chuông mặc định, lặp được) | 0.8 |
| `phone_vibrate` | sfx | Điện thoại rung báo tin nhắn (2 lần) | 0.9 |
| `rain_roof` | sfx | Mưa đều trên mái tôn, nước nhỏ giọt máng (lặp được) | 0.8 |
| `reverse_swell` | sfx | Tiếng rít tăng dần (riser) trước khi hù | 0.8 |
| `rice_scatter` | sfx | Nắm gạo muối rải xuống sân xi măng | 0.8 |
| `ritual_bell` | sfx | Mõ gõ ba tiếng rồi chuông đồng nhỏ ngân | 0.8 |
| `river_lapping` | sfx | Nước sông vỗ nhẹ vào bậc đá ban đêm (lặp được) | 1.0 |
| `rooster_crow` | sfx | Một tiếng gà gáy xa lúc rạng sáng | 1.0 |
| `scissors_hair` | sfx | Kéo cắt một lọn tóc | 1.0 |
| `slipper_drag` | sfx | Tiếng dép lê lẹp xẹp kéo lê trên sàn gạch (lặp được) | 0.8 |
| `spoon_bowl_tap` | sfx | Thìa kim loại gõ khẽ thành bát ba lần | 0.8 |
| `water_drip` | sfx | Nước nhỏ tong tỏng xuống nền gạch (lặp được) | 1.0 |
| `whisper_eerie` | sfx | Tiếng thì thầm rợn người của phụ nữ (không rõ lời) | 0.8 |
| `woman_sob_door` | sfx | Tiếng phụ nữ khóc nghẹn sau cánh cửa gỗ | 0.8 |
