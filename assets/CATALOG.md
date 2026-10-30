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
| `M1_kneel_incense` | right | Quỳ chắp ba nén nhang đang cháy, mắt nhắm buồn | quỳ, thắp nhang, cúng, bàn thờ |  |
| `M2_carry_rice_bowl` | right | Đứng bưng bát cơm cắm đũa thẳng bằng hai tay | bát cơm, cúng cơm, bưng |  |
| `M3_sit_stool_eat` | right | Ngồi ghế đẩu ăn cơm một mình (có ghế) | ngồi, ăn cơm, ghế đẩu, cô đơn |  |
| `M4_sit_stool_look_back_fear` | left | Ngồi ghế đẩu cầm bát, ngoái lại, mắt mở to sợ hãi (có ghế) | ngồi, ngoái lại, sợ, ghế đẩu |  |
| `M5_lie_unconscious` | left | Nằm ngửa bất tỉnh, đầu bên trái | nằm, ngất, bất tỉnh |  |
| `M6_lie_peek_under_door` | left | Nằm sấp áp mặt nhìn qua khe dưới cửa, sợ (mép cửa đen ở rìa trái) | nằm sấp, nhìn trộm, khe cửa, sợ |  |
| `M7_lie_prone_back_view` | front | Nằm sấp nhìn từ phía sau (đế giày gần người xem, đầu hướng vào trong), hai tay chống sàn cạnh đầu — ghé nhìn qua khe cửa trên phông nhìn thẳng | nằm sấp, nhìn trộm, khe cửa, sau lưng |  |

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

## Nhân vật `grandma` — Bà nội

- Chiều cao mặc định: `0.5` khung hình
- Ảnh tham chiếu khi tạo thêm: `assets/source/grandma_base.png`, `assets/source/grandma_sheet_A.png`
- Style prompt: Same elderly woman as the reference images: a small Vietnamese grandmother, slightly hunched, silver-gray hair in a small bun, dark brown "ao ba ba" blouse, loose black trousers, black sandals, wrinkled face clearly visible. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, dot eyes, minimal flat colors. Never white clothing.

**Chu kỳ chuyển động** (dùng `"cycle": "grandma/<tên>"`):

- `walk`: 6 khung — D1_walk_1, D2_walk_2, D3_walk_3, D4_walk_4, D5_walk_5, D6_walk_6
- `walk_old`: 6 khung — B1_walk_1, B2_walk_2, B3_walk_3, B4_walk_4, B5_walk_5, B3_walk_3
- `walk_v2`: 6 khung — C1_walk_1, C2_walk_2, C3_walk_3, C4_walk_4, C5_walk_5, C6_walk_6

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

## Nhân vật `hungry_ghost` — Cô hồn đói

- Chiều cao mặc định: `0.6` khung hình
- Ảnh tham chiếu khi tạo thêm: `assets/source/hungry_ghost_base.png`, `assets/source/hungry_ghost_sheet_A.png`
- Style prompt: Same hungry ghost as the reference images: emaciated skeletal body with visible ribs, very long thin neck, slightly swollen belly, ash gray-blue skin, pitch black hands up to the wrists, long bony fingers, torn dark brown ragged cloth, long stringy black hair, hollow pitch-black eye sockets. Hand-drawn crayon / colored-pencil texture, thick black outlines, minimal flat colors. Absolutely no white on the character.

| Sprite | Hướng | Mô tả | Tag | Neo |
|---|---|---|---|---|
| `00_stand_front` | front | Đứng thẳng chính diện, gầy trơ xương, mắt đen rỗng, miệng há | đứng, chính diện, đám đông |  |
| `A1_crouch_eat_rice` | right | Ngồi xổm bốc cơm nhét vào miệng, bát cơm dưới đất (có bát) | ăn cơm, bốc, ngồi xổm, nhìn trộm |  |
| `A2_crouch_look_up` | right | Ngồi xổm, ngẩng phắt lên nhìn, mắt đen rỗng | ngồi xổm, nhìn, hù, phát hiện |  |
| `A3_stand_front` | front | Đứng còng chính diện, tay buông thõng, nhìn thẳng | đứng, chính diện, đám đông, ngoài cổng |  |
| `A4_back_look_over_shoulder` | left | Quay lưng, ngoái đầu nhìn qua vai | quay lưng, ngoái lại, đám đông |  |
| `A5_reach_black_hand` | right | Lom khom vươn bàn tay đen xương xẩu ra chộp | vươn tay, tay đen, chộp |  |
| `A6_crawl` | right | Bò bốn chân sát đất, cổ vươn dài, xương sống lồi | bò, sát đất, bóng |  |

## Nhân vật `mother_alive` — Mẹ lúc còn sống (cùng người với ma "Mẹ")

- Chiều cao mặc định: `0.62` khung hình
- Ảnh tham chiếu khi tạo thêm: `assets/source/mother_alive_base.png`, `assets/source/mother_alive_sheet_A.png`
- Style prompt: Same woman as the reference images: a kind Vietnamese mother, black hair tied in a low bun, faded beige cardigan over a long dark gray dress, worn dark brown plastic slippers, face clearly visible. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, dot eyes, minimal flat colors. Never white clothing.

**Chu kỳ chuyển động** (dùng `"cycle": "mother_alive/<tên>"`):

- `walk`: 6 khung — D1_walk_1, D2_walk_2, D3_walk_3, D4_walk_4, D5_walk_5, D6_walk_6
- `walk_old`: 6 khung — B1_walk_1, B2_walk_2, B6_walk_6, B4_walk_4, B5_walk_5, B6_walk_6
- `walk_v2`: 6 khung — C1_walk_1, C2_walk_2, C3_walk_3, C4_walk_4, C5_walk_5, C6_walk_6

| Sprite | Hướng | Mô tả | Tag | Neo |
|---|---|---|---|---|
| `00_stand_front` | front | Đứng chính diện, mỉm cười hiền | đứng, chính diện, hồi ức |  |
| `A1_stir_pot` | right | Đứng cầm nồi khuấy canh, mãn nguyện | nấu ăn, bếp, hồi ức |  |
| `A2_call_to_eat` | left | Đứng khum tay bên miệng gọi con về ăn cơm, cười tươi | gọi, bữa cơm, hồi ức |  |
| `A3_sit_eat_eyes_closed` | left | Ngồi ghế đẩu, và cơm, mắt nhắm (có ghế) | ngồi, ăn cơm, ghế đẩu, hồi ức |  |
| `A4_portrait_front` | front | Đứng chính diện, hai tay đan trước bụng, cười nhẹ như ảnh chân dung | chân dung, ảnh thờ, chính diện, hồi ức |  |
| `A5_sit_eat` | left | Ngồi ghế đẩu, cầm bát và đũa ăn cơm (có ghế) | ngồi, ăn cơm, ghế đẩu, hồi ức |  |
| `A6_offer_rice_bowl` | left | Đứng đưa bát cơm đầy bằng hai tay cho con | bát cơm, đưa, hồi ức |  |
| `A7_sit_chopsticks_over_bowl` | left | Ngồi ghế đẩu, cầm bát, đưa đôi đũa ngang trên miệng bát (sắp gác đũa), cười hiền (có ghế) | ngồi, gác đũa, ghế đẩu, hồi ức |  |
| `B1_walk_1` | right | Đi lê dép, khung 1/6 | đi, chu kỳ, dép |  |
| `B2_walk_2` | right | Đi lê dép, khung 2/6 | đi, chu kỳ, dép |  |
| `B3_walk_3` | right | Đi lê dép, khung 3/6 (mặt bị mờ, không dùng trong chu kỳ) | đi, chu kỳ, dép |  |
| `B4_walk_4` | right | Đi lê dép, khung 4/6 | đi, chu kỳ, dép |  |
| `B5_walk_5` | right | Đi lê dép, khung 5/6 | đi, chu kỳ, dép |  |
| `B6_walk_6` | right | Đi lê dép, khung 6/6 | đi, chu kỳ, dép |  |
| `C1_walk_1` | right | Đi lê dép, váy ngắn hơn lộ cổ chân, vung tay, bước rõ, khung 1/6 | đi, chu kỳ |  |
| `C2_walk_2` | right | Đi lê dép, váy ngắn hơn lộ cổ chân, vung tay, bước rõ, khung 2/6 | đi, chu kỳ |  |
| `C3_walk_3` | right | Đi lê dép, váy ngắn hơn lộ cổ chân, vung tay, bước rõ, khung 3/6 | đi, chu kỳ |  |
| `C4_walk_4` | right | Đi lê dép, váy ngắn hơn lộ cổ chân, vung tay, bước rõ, khung 4/6 | đi, chu kỳ |  |
| `C5_walk_5` | right | Đi lê dép, váy ngắn hơn lộ cổ chân, vung tay, bước rõ, khung 5/6 | đi, chu kỳ |  |
| `C6_walk_6` | right | Đi lê dép, váy ngắn hơn lộ cổ chân, vung tay, bước rõ, khung 6/6 | đi, chu kỳ |  |
| `D1_walk_1` | right | Đi bước rõ, chu kỳ chuẩn, khung 1/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D2_walk_2` | right | Đi bước rõ, chu kỳ chuẩn, khung 2/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D3_walk_3` | right | Đi bước rõ, chu kỳ chuẩn, khung 3/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D4_walk_4` | right | Đi bước rõ, chu kỳ chuẩn, khung 4/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D5_walk_5` | right | Đi bước rõ, chu kỳ chuẩn, khung 5/6 (chạm-hạ-lướt) | đi, chu kỳ |  |
| `D6_walk_6` | right | Đi bước rõ, chu kỳ chuẩn, khung 6/6 (chạm-hạ-lướt) | đi, chu kỳ |  |

## Nhân vật `props` — Đạo cụ (bát cơm cúng, nhang, dấu tay, dép)

- Chiều cao mặc định: `0.2` khung hình
- Ảnh tham chiếu khi tạo thêm: `assets/source/props_sheet_DC.png`
- Style prompt: Prop in the same hand-drawn crayon / colored-pencil texture with thick black outlines and minimal flat colors, three-quarter view, thick black outline all around.

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
| `VM1_fire_bucket_1` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 1/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM2_fire_bucket_2` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 2/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM3_fire_bucket_3` | front | Xô sắt gỉ đốt vàng mã, lửa cháy, khung 3/3 (chu kỳ fire, xô đứng yên) | vàng mã, lửa, cúng |  |
| `VM4_grandma_crouch_drop_paper` | right | Bà ngồi xổm thả xấp vàng mã xuống (mặt hắt ánh lửa) | bà, vàng mã, đốt |  |
| `VM5_grandma_hold_paper` | right | Bà đứng ôm xấp vàng mã trước ngực, cúi đầu | bà, vàng mã |  |
| `VM6_joss_paper_stack` | front | Xấp vàng mã đỏ vàng nằm dưới đất | vàng mã, đạo cụ |  |

## Phông nền

Toạ độ là tỉ lệ khung hình 16:9 (x 0 trái→1 phải, y 0 trên→1 dưới). floor_y = đường chân nhân vật đứng ở tiền cảnh; char_h = chiều cao nhân vật khuyến nghị.

- Style prompt: Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat side view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones with only faint cold moonlight, lots of empty floor space in the lower third, no text.

| Phông | Mô tả | floor_y | char_h | Điểm nóng (dùng tên trong `pin.at`) |
|---|---|---|---|---|
| `bg1_bedroom` | Phòng ngủ ban đêm, KHÔNG có giường (dùng sprite G1–G3). Cửa phòng bên trái, cửa sổ ánh trăng giữa, tủ đầu giường + đồng hồ 03:00, nửa phải sàn trống. | 0.95 | 0.46 | `bedroom_door` [0.1, 0.55]; `bedroom_door_handle` [0.145, 0.49]; `window` [0.34, 0.35]; `clock` [0.48, 0.53]; `bed_spot` [0.7, 0.95] |
| `bg1c_corner_night` | Góc phòng ngủ ban đêm, Khoa vẽ sẵn: ngồi co ro trong góc, bịt hai tai, MẮT MỞ TRỪNG nhìn về phía cửa (trái), khe sáng vàng dưới cửa, mép giường bên phải. | 0.95 | 0.4 | `boy_face` [0.5, 0.42]; `door` [0.12, 0.5]; `door_gap` [0.15, 0.86] |
| `bg1d_corner_dawn` | Góc phòng ngủ lúc rạng đông (đã chỉnh sáng), Khoa vẫn ngồi bịt tai, mắt đỏ thâm quầng, thức trắng cả đêm. | 0.95 | 0.4 | `boy_face` [0.5, 0.45]; `door` [0.17, 0.5] |
| `bg2_hallway` | Hành lang dài nằm ngang, sàn gỗ, 2 cửa đóng, ảnh gia đình mờ trên tường, hai đầu tối. | 0.97 | 0.46 | `door_left` [0.34, 0.5]; `door_right` [0.705, 0.5]; `family_photo` [0.5, 0.36]; `far_end` [0.86, 0.9] |
| `bg3_front_door` | Cửa chính nhìn từ trong nhà, ở giữa; lỗ mắt mèo (cao, quá tầm cậu bé), tay nắm bên trái cửa, tủ giày bên trái, móc áo bên phải, khe sáng vàng dưới cửa. | 0.96 | 0.46 | `door_handle` [0.44, 0.478]; `peephole` [0.5, 0.205]; `door_center` [0.5, 0.45]; `door_bottom_y` [0.5, 0.79]; `shoe_rack` [0.23, 0.72]; `coat_hooks` [0.73, 0.35] |
| `bg3b_peephole` | Góc nhìn qua mắt mèo: khung tròn giữa nền đen, hành lang chung cư bị bóp méo, đèn trần mờ. | 0.66 | 0.3 | `lens_circle` [0.5, 0.5, 0.49]; `corridor_floor` [0.6, 0.66]; `far_door` [0.5, 0.5] |
| `bg4_main_room` | Gian nhà chính ban đêm: bàn thờ treo tường bên trái (ảnh thờ, bát hương, 2 nến đỏ, đĩa hoa quả, bát cơm), bàn ăn thấp + 2 ghế đẩu bên phải, lịch treo tường, cửa xuống bếp sát mép phải. Nửa trái sàn trống. | 0.95 | 0.46 | `altar_shelf` [0.3, 0.36]; `altar_portrait` [0.31, 0.24]; `altar_rice` [0.4, 0.33]; `altar_incense` [0.31, 0.33]; `dining_table` [0.73, 0.6]; `table_top_y` [0.73, 0.585]; `stool_left` [0.585, 0.8]; `stool_right` [0.86, 0.78]; `kitchen_door` [0.96, 0.5]; `calendar` [0.7, 0.35]; `open_floor` [0.3, 0.95] |
| `bg4d_main_room_day` | Gian nhà chính (cùng bố cục BG4) chiều nắng ấm trong hồi ức: kệ chỉ có bình hoa + bát, không ảnh thờ; nồi canh bốc khói trên bàn ăn. | 0.95 | 0.46 | `altar_shelf` [0.3, 0.36]; `altar_portrait` [0.31, 0.24]; `altar_rice` [0.4, 0.33]; `altar_incense` [0.31, 0.33]; `dining_table` [0.73, 0.6]; `table_top_y` [0.73, 0.585]; `stool_left` [0.585, 0.8]; `stool_right` [0.86, 0.78]; `kitchen_door` [0.96, 0.5]; `calendar` [0.7, 0.35]; `open_floor` [0.3, 0.95] |
| `bg5_altar_close` | Cận mặt bàn thờ ban đêm: ảnh thờ mẹ (dải băng tang đen) ở giữa, bát hương đồng với 3 nén nhang khói bên trái, 2 nến đỏ, đĩa và chân nến bên phải. Mặt gỗ phía trước trống để đặt đạo cụ (bát cơm). | 0.8 | 0.3 | `portrait` [0.5, 0.32]; `portrait_face` [0.5, 0.26]; `incense_bowl` [0.27, 0.6]; `incense_tips` [0.27, 0.33]; `candle_left` [0.35, 0.43]; `candle_right` [0.66, 0.43]; `offering_spot` [0.52, 0.78]; `plate` [0.76, 0.59] |
| `bg6_kitchen` | Bếp nhà ống ban đêm: bệ bếp lát gạch bên trái (bếp ga 2 lò + nồi nhôm, nồi cơm điện, giá bát, ống đũa), cửa sổ song sắt hắt ánh trăng, ô cửa tối om dẫn ra nhà sau ở giữa-phải. Sàn giữa và phải trống. | 0.95 | 0.46 | `doorway` [0.69, 0.38]; `doorway_floor` [0.69, 0.66]; `stove_pot` [0.14, 0.5]; `rice_cooker` [0.31, 0.43]; `window` [0.42, 0.17]; `dish_rack` [0.15, 0.22]; `open_floor` [0.62, 0.95] |
| `bg6d_kitchen_day` | Bếp (cùng bố cục BG6) chiều nắng vàng trong hồi ức, nồi trên bếp bốc hơi, ô cửa sáng. | 0.95 | 0.46 | `doorway` [0.69, 0.38]; `doorway_floor` [0.69, 0.66]; `stove_pot` [0.14, 0.5]; `rice_cooker` [0.31, 0.43]; `window` [0.42, 0.17]; `dish_rack` [0.15, 0.22]; `open_floor` [0.62, 0.95] |
| `bg7_front_yard` | Sân trước nhà ban đêm: chậu cây + bàn cúng nhỏ ngoài trời bên trái, cổng sắt xếp hoen gỉ chiếm nửa phải, khe hở giữa cổng nhìn ra đường vắng có sương và cột đèn xa. Nền xi măng nứt. | 0.95 | 0.46 | `offering_table` [0.28, 0.47]; `offering_table_top` [0.28, 0.455]; `gate_gap` [0.69, 0.45]; `gate_gap_floor` [0.69, 0.64]; `gate_left` [0.5, 0.35]; `gate_right` [0.88, 0.35]; `street_lamp` [0.68, 0.19]; `open_floor` [0.5, 0.95] |
| `bg8_bedroom_door` | Trong phòng ngủ nhìn thẳng vào cửa phòng đóng (giữa khung): tay nắm + chốt cài, khe sáng vàng dưới chân cửa hắt lên sàn gỗ; hai tờ tranh vẽ dán tường hai bên. | 0.97 | 0.46 | `door_center` [0.5, 0.53]; `door_handle` [0.555, 0.53]; `bolt_lock` [0.58, 0.46]; `door_gap` [0.5, 0.855]; `door_gap_left` [0.41, 0.855]; `door_gap_right` [0.59, 0.855] |
| `bg9_door_gap` | Góc nhìn nằm sát sàn qua khe dưới cửa (POV của Khoa): khung đen, khe ngang ở giữa (y 0.35–0.69) nhìn ra sàn gạch gian thờ, ánh nến đỏ xa. Nhân vật đặt nhỏ ở xa để lọt trong khe. | 0.6 | 0.2 | `slit_center` [0.5, 0.52]; `far_floor` [0.5, 0.45]; `mid_floor` [0.5, 0.6]; `red_glow` [0.45, 0.37] |
| `bg9b_door_gap_ghosts` | POV qua khe dưới cửa: đám cô hồn ngồi xổm quanh mâm cơm (khe cắt ngang người, thấy gối, chân, tay đen bốc cơm), bát đổ, một con nhỏ ở xa. Vẽ sẵn, không cần sprite. | 0.6 | 0.2 | `slit_center` [0.5, 0.52]; `tray` [0.53, 0.6]; `far_ghost` [0.49, 0.37] |
| `bg9c_door_gap_face` | POV qua khe dưới cửa: một cô hồn áp mặt xuống sàn sát cửa, hốc mắt đen nhìn thẳng vào khe, miệng dính cơm (cú hù). Vẽ sẵn. | 0.6 | 0.2 | `slit_center` [0.5, 0.52]; `ghost_face` [0.43, 0.48] |

## Âm thanh

Dùng trong cảnh: `"sfx": [{"sound": <tên>, "at": 0.3}]`; nhạc nền: `"music"` ở cấp kịch bản.

| Âm thanh | Loại | Mô tả | Tag | Âm lượng |
|---|---|---|---|---|
| `body_fall` | sfx | Người ngã ngửa xuống sàn gỗ | ngã | 1.0 |
| `breath_close` | sfx | Hơi thở run rẩy sát tai | thở, sợ | 0.7 |
| `chewing_wet` | sfx | Nhiều miệng nhai nhóp nhép, húp vội (lặp được) | nhai, cô hồn, ăn | 0.8 |
| `chopsticks_clatter` | sfx | Rất nhiều đôi đũa va bát lách cách gấp gáp | đũa, bát, cô hồn | 0.8 |
| `clock_tick` | sfx | Đồng hồ tích tắc nhỏ, lặp được | đồng hồ, im lặng | 0.5 |
| `dog_howl` | sfx | Một con chó tru dài thê lương từ xa | chó tru, đêm, điềm | 0.8 |
| `door_bang` | sfx | Đập cửa gỗ dồn dập, hoảng loạn | đập cửa | 1.0 |
| `door_bolt_lock` | sfx | Chốt cửa kim loại gài lại, tách gọn | chốt cửa, khoá | 0.8 |
| `door_creak_open` | sfx | Cửa gỗ phòng ngủ từ từ mở kẽo kẹt dài | cửa, kẽo kẹt, mở cửa | 0.8 |
| `door_handle_rattle` | sfx | Tay nắm cửa bị vặn lạch cạch | tay nắm cửa, cửa | 0.9 |
| `door_scratch` | sfx | Móng tay cào chậm lên cửa gỗ từ phía bên ngoài, lặp được | cào cửa, ma | 0.9 |
| `door_slam` | sfx | Đóng sầm cửa gỗ | cửa, đóng sầm | 0.9 |
| `drone_low` | music | Nhạc nền u ám trầm, lặp được | nhạc nền, u ám | 0.7 |
| `flashlight_click` | sfx | Tiếng bật công tắc đèn pin | đèn pin | 0.9 |
| `flicker_buzz` | sfx | Đèn chập chờn rè điện | đèn, chập chờn | 0.7 |
| `floor_creak` | sfx | Sàn gỗ kêu kẽo kẹt một tiếng | sàn gỗ, bước chân | 0.8 |
| `footsteps_run` | sfx | Tiếng chạy gấp trên sàn gỗ | bước chân, chạy | 0.8 |
| `footsteps_slow` | sfx | Bước chân chậm trên sàn gỗ, lặp được | bước chân, chậm | 0.7 |
| `gate_rattle` | sfx | Cổng sắt xếp bị lay rung lạch cạch | cổng sắt, rung, ngoài cổng | 0.8 |
| `ghost_stinger` | sfx | Tiếng hù jumpscare khi ma xuất hiện (đánh mạnh + rít) | jumpscare, ma xuất hiện | 1.0 |
| `hangup_tone` | sfx | Tiếng tút tút khi đầu dây bên kia cúp máy | điện thoại, cúp máy | 0.7 |
| `heartbeat` | sfx | Tim đập căng thẳng, lặp được | tim đập, căng thẳng | 0.8 |
| `knock_3` | sfx | Cốc… cốc… cốc — ba tiếng gõ cửa gỗ chậm rãi | gõ cửa | 1.0 |
| `night_insects` | sfx | Không khí đêm: dế, tắc kè kêu xa, yên tĩnh (lặp được) | côn trùng, đêm, không khí | 0.8 |
| `paper_burn` | sfx | Đốt vàng mã trong thùng sắt, lửa lách tách (lặp được) | vàng mã, lửa, cúng | 0.8 |
| `phone_drop` | sfx | Điện thoại rơi xuống sàn gỗ | điện thoại, rơi | 0.9 |
| `phone_ring` | sfx | Chuông điện thoại di động đổ giữa đêm (nhạc chuông mặc định, lặp được) | điện thoại, chuông | 0.8 |
| `phone_vibrate` | sfx | Điện thoại rung báo tin nhắn (2 lần) | điện thoại, rung, tin nhắn | 0.9 |
| `rain_roof` | sfx | Mưa đều trên mái tôn, nước nhỏ giọt máng (lặp được) | mưa, mái tôn, không khí | 0.8 |
| `reverse_swell` | sfx | Tiếng rít tăng dần (riser) trước khi hù | căng thẳng, trước jumpscare | 0.8 |
| `rice_scatter` | sfx | Nắm gạo muối rải xuống sân xi măng | gạo muối, cúng cô hồn | 0.8 |
| `ritual_bell` | sfx | Mõ gõ ba tiếng rồi chuông đồng nhỏ ngân | mõ, chuông, cúng, tang | 0.8 |
| `slipper_drag` | sfx | Tiếng dép lê lẹp xẹp kéo lê trên sàn gạch (lặp được) | dép, bước chân, mẹ | 0.8 |
| `spoon_bowl_tap` | sfx | Thìa kim loại gõ khẽ thành bát ba lần | thìa, bát, tiếng động lạ | 0.8 |
| `whisper_eerie` | sfx | Tiếng thì thầm rợn người của phụ nữ (không rõ lời) | thì thầm, ma | 0.8 |
| `woman_sob_door` | sfx | Tiếng phụ nữ khóc nghẹn sau cánh cửa gỗ | khóc, mẹ, sau cửa | 0.8 |
