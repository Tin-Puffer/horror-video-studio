# Kho asset — mục lục

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.
> Ảnh xem nhanh: `assets/catalog/<nhân vật>.png`, `assets/catalog/backgrounds.png`.

## Nhân vật `boy_hoodie` — Khoa — cậu trai hoodie xanh

- Chiều cao mặc định: `0.46` khung hình
- Ảnh tham chiếu khi tạo thêm: `assets/source/boy_hoodie_base.png`, `assets/source/boy_hoodie_sheet_C.png`
- Style prompt: Same character as the reference images: a boy with messy spiky black hair, dark moss-green hoodie with drawstrings and front pocket, dark charcoal-gray pants, white sneakers. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, dot eyes, minimal flat colors.

**Chu kỳ chuyển động** (dùng `"cycle": "boy_hoodie/<tên>"`):

- `walk`: 6 khung — H1_walk_contact_a, H2_walk_down_a, H3_walk_pass_a, H4_walk_contact_b, H5_walk_down_b, H6_walk_pass_b
- `flashlight_walk`: 6 khung — I1_flashlight_walk_contact_a, I2_flashlight_walk_down_a, I3_flashlight_walk_pass_a, I4_flashlight_walk_contact_b, I5_flashlight_walk_down_b, I6_flashlight_walk_pass_b
- `tiptoe`: 4 khung — J1_tiptoe_a, J2_tiptoe_together, J3_tiptoe_b, J2_tiptoe_together
- `back_walk`: 4 khung — J4_back_walk_a, J5_back_walk_together, J6_back_walk_b, J5_back_walk_together
- `run`: 4 khung — C4_run_step_a, C5_run_step_b, C6_run_step_c, C5_run_step_b
- `talk`: 4 khung — D2_face_talk_small, D3_face_talk_open, D2_face_talk_small, D1_face_neutral
- `blink`: 5 khung — D1_face_neutral, D1_face_neutral, D1_face_neutral, D1_face_neutral, D4_face_blink

| Sprite | Hướng | Mô tả | Tag | Neo |
|---|---|---|---|---|
| `00_idle_front_smile` | front | Đứng thẳng chính diện, mỉm cười nhẹ | đứng, chính diện, vui, bình thường |  |
| `A1_walk_sad` | right | Đi bộ, mặt buồn/lo | đi, buồn, lo |  |
| `A2_side_nervous_sweat` | right | Đứng nghiêng nhìn ngang, đổ mồ hôi | đứng, nghiêng, lo, nghe ngóng |  |
| `A3_call_out_hand_mouth` | left | Đưa tay lên miệng gọi to | gọi, nói, tay |  |
| `A4_walk_reach_out` | right | Bước tới, đưa tay ra ngang ngực | đi, với tay, chạm | hand |
| `A5_walk_scared_clutch` | left | Đi rụt rè, nắm tay trước ngực | đi, sợ, rụt rè |  |
| `A6_closeup_shock` | front | Cận mặt, mắt trợn, há miệng | cận mặt, sốc, jumpscare, sợ |  |
| `B1_stand_worried` | front | Đứng lo lắng, tay trước ngực | đứng, lo, chính diện |  |
| `B2_look_phone` | front | Đứng nhìn điện thoại | điện thoại, đứng, đọc tin |  |
| `B3_look_back_over_shoulder` | front | Quay lưng, ngoái nhìn qua vai | quay lưng, ngoái lại, bị theo dõi |  |
| `B4_shock_arms_up` | right | Giật mình giơ hai tay, ngã ngửa | sốc, ngã, giật mình |  |
| `B5_run_scared` | right | Chạy hoảng loạn (1 khung) | chạy, sợ |  |
| `B6_sit_fallen` | right | Ngã ngồi dưới đất | ngồi, ngã, kiệt sức |  |
| `C1_walk_step_a` | right | Đi (bộ cũ 3 khung) chân trước | đi, chu kỳ |  |
| `C2_walk_step_b` | right | Đi (bộ cũ 3 khung) chân sau | đi, chu kỳ |  |
| `C3_walk_step_pass` | right | Đi (bộ cũ 3 khung) chân lướt qua | đi, chu kỳ |  |
| `C4_run_step_a` | right | Chạy hoảng, khung 1 | chạy, chu kỳ, sợ |  |
| `C5_run_step_b` | right | Chạy hoảng, khung 2 (bay người) | chạy, chu kỳ, sợ |  |
| `C6_run_step_c` | right | Chạy hoảng, khung 3 | chạy, chu kỳ, sợ |  |
| `D1_face_neutral` | front | Cận mặt, miệng ngậm | cận mặt, im, khẩu hình |  |
| `D2_face_talk_small` | front | Cận mặt, miệng hé | cận mặt, nói, khẩu hình |  |
| `D3_face_talk_open` | front | Cận mặt, miệng mở to | cận mặt, nói, khẩu hình |  |
| `D4_face_blink` | front | Cận mặt, nhắm mắt | cận mặt, chớp mắt, ngủ |  |
| `D5_face_whisper_scared` | front | Cận mặt, thì thầm sợ hãi, mồ hôi | cận mặt, thì thầm, sợ |  |
| `D6_face_crying` | front | Cận mặt, khóc | cận mặt, khóc, tuyệt vọng |  |
| `E1_back_walk_away` | front | Quay lưng bước đi (1 khung) | quay lưng, đi |  |
| `E2_back_stand` | front | Quay lưng đứng yên | quay lưng, đứng, nhìn bóng tối |  |
| `E3_crouch_hug_knees_shaking` | front | Ngồi ôm gối run rẩy (có vạch run) | ngồi, trốn, run, sợ |  |
| `E4_hide_peek_wall` | left | Nép tường nhìn trộm (có vạch tường dọc) | trốn, nhìn trộm, tường |  |
| `E5_cover_mouth_hold_breath` | front | Bịt miệng nín thở (nửa người) | bịt miệng, nín thở, sợ |  |
| `E6_crouch_cover_ears` | front | Ngồi bịt tai, nhắm mắt | ngồi, bịt tai, sợ |  |
| `F1_flashlight_forward` | left | Đứng soi đèn pin phía trước | đèn pin, đứng, bóng tối |  |
| `F2_flashlight_walk_down` | left | Đi soi đèn pin xuống đất (1 khung) | đèn pin, đi |  |
| `F3_phone_light_forward` | left | Soi đèn điện thoại phía trước | điện thoại, đèn, sợ |  |
| `F4_phone_call_scared` | front | Nghe điện thoại, sợ | điện thoại, nghe gọi, sợ |  |
| `F5_drop_phone_shock` | left | Đánh rơi điện thoại vì sốc | điện thoại, rơi, sốc |  |
| `F6_phone_show_screen` | left | Giơ màn hình điện thoại ra | điện thoại, tin nhắn, sợ |  |
| `G1_bed_sleeping` | front | Ngủ trên giường (sprite có giường) | giường, ngủ, đêm |  |
| `G2_bed_wake_startled` | front | Giật mình ngồi dậy trên giường | giường, tỉnh dậy, giật mình |  |
| `G3_bed_blanket_chin_scared` | front | Kéo chăn lên cằm, mặt tái | giường, chăn, sợ |  |
| `G4_rub_sleepy_eyes` | front | Đứng dụi mắt ngái ngủ | đứng, ngái ngủ |  |
| `G5_reach_door_handle` | left | Đưa tay ra ngang ngực (không với tới tay nắm cửa ở góc toàn thân) | với tay, cửa | hand |
| `G6_tiptoe_sneak` | left | Rón rén (1 khung) | rón rén, đi |  |
| `H1_walk_contact_a` | right | Đi thường, khung 1/6 | đi, chu kỳ |  |
| `H2_walk_down_a` | right | Đi thường, khung 2/6 | đi, chu kỳ |  |
| `H3_walk_pass_a` | right | Đi thường, khung 3/6 | đi, chu kỳ |  |
| `H4_walk_contact_b` | right | Đi thường, khung 4/6 | đi, chu kỳ |  |
| `H5_walk_down_b` | right | Đi thường, khung 5/6 | đi, chu kỳ |  |
| `H6_walk_pass_b` | right | Đi thường, khung 6/6 | đi, chu kỳ |  |
| `I1_flashlight_walk_contact_a` | right | Đi cầm đèn pin, khung 1/6 | đi, đèn pin, chu kỳ |  |
| `I2_flashlight_walk_down_a` | right | Đi cầm đèn pin, khung 2/6 | đi, đèn pin, chu kỳ |  |
| `I3_flashlight_walk_pass_a` | right | Đi cầm đèn pin, khung 3/6 | đi, đèn pin, chu kỳ |  |
| `I4_flashlight_walk_contact_b` | right | Đi cầm đèn pin, khung 4/6 | đi, đèn pin, chu kỳ |  |
| `I5_flashlight_walk_down_b` | right | Đi cầm đèn pin, khung 5/6 | đi, đèn pin, chu kỳ |  |
| `I6_flashlight_walk_pass_b` | right | Đi cầm đèn pin, khung 6/6 | đi, đèn pin, chu kỳ |  |
| `J1_tiptoe_a` | right | Rón rén, khung 1/3 | rón rén, chu kỳ, sợ |  |
| `J2_tiptoe_together` | right | Rón rén, khung 2/3 | rón rén, chu kỳ, sợ |  |
| `J3_tiptoe_b` | right | Rón rén, khung 3/3 | rón rén, chu kỳ, sợ |  |
| `J4_back_walk_a` | front | Quay lưng bước đi, khung 1/3 | quay lưng, đi, chu kỳ |  |
| `J5_back_walk_together` | front | Quay lưng bước đi, khung 2/3 | quay lưng, đi, chu kỳ |  |
| `J6_back_walk_b` | front | Quay lưng bước đi, khung 3/3 | quay lưng, đi, chu kỳ |  |
| `K1_reach_up_open` | right | Kiễng chân giơ tay lên cao, bàn tay mở | với tay, cửa, tay nắm cửa, kiễng chân | hand |
| `K2_reach_up_grip` | right | Kiễng chân giơ tay lên cao, nắm chặt (cầm tay nắm cửa) | với tay, cửa, tay nắm cửa, nắm | hand |
| `K3_pull_back_fear` | right | Rụt tay về ngực, ngả người ra sau sợ hãi | sợ, rụt tay, lùi |  |
| `K4_ear_listen` | right | Áp tai nghe ngóng, mắt mở to | nghe, áp tai, cửa, tường |  |
| `K5_peephole_look` | right | Kiễng chân áp mắt nhìn qua lỗ, tay áp cửa | mắt mèo, nhìn trộm, cửa |  |
| `K6_slide_down_door` | right | Tựa lưng vào cửa trượt xuống, kinh hãi | tựa cửa, ngồi, sợ |  |
| `L1_look_up_terrified` | front | Ngửa mặt nhìn lên trần, kinh hãi | nhìn lên, trần nhà, sợ, sốc |  |
| `L2_flashlight_point_far` | right | Đứng yên giơ đèn pin soi xa phía trước | đèn pin, soi xa, đứng, sợ |  |
| `L3_freeze_flashlight_off` | right | Đứng đơ người, đèn pin đã tắt hạ xuống | đơ người, đèn pin, sợ, run |  |
| `L4_back_against_door` | front | Đứng chính diện nhắm chặt mắt, tay xoè (dùng như áp lưng vào cửa) | tựa cửa, trốn, sợ, đứng |  |
| `L5_peek_from_blanket` | front | Ngồi trùm chăn kín người, chỉ lộ đôi mắt | chăn, trốn, ngồi, sợ |  |
| `L6_slow_turn_head` | right | Quay lưng, từ từ ngoái đầu qua vai (nhìn sang phải) | quay lưng, ngoái lại, sợ |  |

## Nhân vật `ghost_mother` — "Mẹ" — ma nữ tóc dài

- Chiều cao mặc định: `0.66` khung hình
- Ảnh tham chiếu khi tạo thêm: `assets/source/ghost_mother_base.png`, `assets/source/ghost_mother_sheet_A.png`
- Style prompt: Same ghost woman as the reference images: unnaturally tall and thin, very pale gray-white skin, long straight black hair covering her face, faded beige cardigan, long dark gray dress, bare feet, arms slightly too long. Same hand-drawn crayon / colored-pencil style with thick black outlines. Never white clothing.

**Chu kỳ chuyển động** (dùng `"cycle": "ghost_mother/<tên>"`):

- `walk`: 2 khung — GH7_walk_step_a, GH8_walk_step_b

| Sprite | Hướng | Mô tả | Tag | Neo |
|---|---|---|---|---|
| `GH0_stand_front` | front | Đứng chính diện, tóc che mặt, một mắt đen rỗng | đứng, chính diện |  |
| `GH10_hand_scratch` | front | Chỉ bàn tay cào (có vệt cào) | tay, cào cửa |  |
| `GH11_fake_smile_black_eyes` | front | Đứng cười hiền như người mẹ, mắt đen kịt | đứng, giả làm mẹ, cười |  |
| `GH12_upside_down_head` | front | Đầu treo ngược từ trên xuống | treo ngược, trần nhà, jumpscare |  |
| `GH1_stand_far_head_bowed` | front | Đứng xa, cúi đầu, tóc che kín mặt | đứng, xa, cúi đầu |  |
| `GH2_eye_closeup` | front | Cận một con mắt đỏ ngầu (khối vuông kín khung, dùng với clip_circle) | cận, mắt, jumpscare, mắt mèo |  |
| `GH3_peek_from_right_tilted` | left | Ló nửa người, nghiêng đầu bất thường | ló, nhìn trộm, cửa |  |
| `GH4_closeup_lunge_grin` | front | Cận mặt lao tới, cười toác (jumpscare) | cận mặt, jumpscare, cười |  |
| `GH5_long_arm_reach` | right | Vươn cánh tay dài bất thường | với tay, tay dài | hand |
| `GH6_crawl` | front | Bò bằng bốn chi | bò |  |
| `GH7_walk_step_a` | right | Bước đi chậm, khung 1/2 | đi, chu kỳ |  |
| `GH8_walk_step_b` | right | Bước đi chậm, khung 2/2 | đi, chu kỳ |  |
| `GH9_back_stand` | front | Quay lưng đứng | quay lưng, đứng |  |

## Phông nền

Toạ độ là tỉ lệ khung hình 16:9 (x 0 trái→1 phải, y 0 trên→1 dưới). floor_y = đường chân nhân vật đứng ở tiền cảnh; char_h = chiều cao nhân vật khuyến nghị.

- Style prompt: Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat side view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones with only faint cold moonlight, lots of empty floor space in the lower third, no text.

| Phông | Mô tả | floor_y | char_h | Điểm nóng (dùng tên trong `pin.at`) |
|---|---|---|---|---|
| `bg1_bedroom` | Phòng ngủ ban đêm, KHÔNG có giường (dùng sprite G1–G3). Cửa phòng bên trái, cửa sổ ánh trăng giữa, tủ đầu giường + đồng hồ 03:00, nửa phải sàn trống. | 0.95 | 0.46 | `bedroom_door` [0.1, 0.55]; `bedroom_door_handle` [0.145, 0.49]; `window` [0.34, 0.35]; `clock` [0.48, 0.53]; `bed_spot` [0.7, 0.95] |
| `bg2_hallway` | Hành lang dài nằm ngang, sàn gỗ, 2 cửa đóng, ảnh gia đình mờ trên tường, hai đầu tối. | 0.97 | 0.46 | `door_left` [0.34, 0.5]; `door_right` [0.705, 0.5]; `family_photo` [0.5, 0.36]; `far_end` [0.86, 0.9] |
| `bg3_front_door` | Cửa chính nhìn từ trong nhà, ở giữa; lỗ mắt mèo (cao, quá tầm cậu bé), tay nắm bên trái cửa, tủ giày bên trái, móc áo bên phải, khe sáng vàng dưới cửa. | 0.96 | 0.46 | `door_handle` [0.44, 0.478]; `peephole` [0.5, 0.205]; `door_center` [0.5, 0.45]; `door_bottom_y` [0.5, 0.79]; `shoe_rack` [0.23, 0.72]; `coat_hooks` [0.73, 0.35] |
| `bg3b_peephole` | Góc nhìn qua mắt mèo: khung tròn giữa nền đen, hành lang chung cư bị bóp méo, đèn trần mờ. | 0.66 | 0.3 | `lens_circle` [0.5, 0.5, 0.49]; `corridor_floor` [0.6, 0.66]; `far_door` [0.5, 0.5] |

## Âm thanh

Dùng trong cảnh: `"sfx": [{"sound": <tên>, "at": 0.3}]`; nhạc nền: `"music"` ở cấp kịch bản.

| Âm thanh | Loại | Mô tả | Tag | Âm lượng |
|---|---|---|---|---|
| `body_fall` | sfx | Người ngã ngửa xuống sàn gỗ | ngã | 1.0 |
| `breath_close` | sfx | Hơi thở run rẩy sát tai | thở, sợ | 0.7 |
| `clock_tick` | sfx | Đồng hồ tích tắc nhỏ, lặp được | đồng hồ, im lặng | 0.5 |
| `door_bang` | sfx | Đập cửa gỗ dồn dập, hoảng loạn | đập cửa | 1.0 |
| `door_handle_rattle` | sfx | Tay nắm cửa bị vặn lạch cạch | tay nắm cửa, cửa | 0.9 |
| `door_scratch` | sfx | Móng tay cào chậm lên cửa gỗ từ phía bên ngoài, lặp được | cào cửa, ma | 0.9 |
| `door_slam` | sfx | Đóng sầm cửa gỗ | cửa, đóng sầm | 0.9 |
| `drone_low` | music | Nhạc nền u ám trầm, lặp được | nhạc nền, u ám | 0.7 |
| `flashlight_click` | sfx | Tiếng bật công tắc đèn pin | đèn pin | 0.9 |
| `flicker_buzz` | sfx | Đèn chập chờn rè điện | đèn, chập chờn | 0.7 |
| `floor_creak` | sfx | Sàn gỗ kêu kẽo kẹt một tiếng | sàn gỗ, bước chân | 0.8 |
| `footsteps_run` | sfx | Tiếng chạy gấp trên sàn gỗ | bước chân, chạy | 0.8 |
| `footsteps_slow` | sfx | Bước chân chậm trên sàn gỗ, lặp được | bước chân, chậm | 0.7 |
| `ghost_stinger` | sfx | Tiếng hù jumpscare khi ma xuất hiện (đánh mạnh + rít) | jumpscare, ma xuất hiện | 1.0 |
| `hangup_tone` | sfx | Tiếng tút tút khi đầu dây bên kia cúp máy | điện thoại, cúp máy | 0.7 |
| `heartbeat` | sfx | Tim đập căng thẳng, lặp được | tim đập, căng thẳng | 0.8 |
| `knock_3` | sfx | Cốc… cốc… cốc — ba tiếng gõ cửa gỗ chậm rãi | gõ cửa | 1.0 |
| `phone_drop` | sfx | Điện thoại rơi xuống sàn gỗ | điện thoại, rơi | 0.9 |
| `phone_ring` | sfx | Chuông điện thoại di động đổ giữa đêm (nhạc chuông mặc định, lặp được) | điện thoại, chuông | 0.8 |
| `phone_vibrate` | sfx | Điện thoại rung báo tin nhắn (2 lần) | điện thoại, rung, tin nhắn | 0.9 |
| `reverse_swell` | sfx | Tiếng rít tăng dần (riser) trước khi hù | căng thẳng, trước jumpscare | 0.8 |
| `whisper_eerie` | sfx | Tiếng thì thầm rợn người của phụ nữ (không rõ lời) | thì thầm, ma | 0.8 |
