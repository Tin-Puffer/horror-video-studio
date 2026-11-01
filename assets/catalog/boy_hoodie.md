# Nhân vật `boy_hoodie` — Khoa — cậu trai hoodie xanh

> Tự sinh bởi `python3 tools/catalog.py`. Đừng sửa tay: sửa `meta.json` rồi chạy lại.

- Chiều cao mặc định: `0.46` khung hình

**Chu kỳ chuyển động** (dùng `"cycle": "boy_hoodie/<tên>"`):

- `walk`: 6 khung — H1_walk_contact_a, H2_walk_down_a, H3_walk_pass_a, H4_walk_contact_b, H5_walk_down_b, H6_walk_pass_b
- `flashlight_walk`: 6 khung — I1_flashlight_walk_contact_a, I2_flashlight_walk_down_a, I3_flashlight_walk_pass_a, I4_flashlight_walk_contact_b, I5_flashlight_walk_down_b, I6_flashlight_walk_pass_b
- `tiptoe`: 4 khung — J1_tiptoe_a, J2_tiptoe_together, J3_tiptoe_b, J2_tiptoe_together
- `back_walk`: 4 khung — J4_back_walk_a, J5_back_walk_together, J6_back_walk_b, J5_back_walk_together
- `run`: 4 khung — C4_run_step_a, C5_run_step_b, C6_run_step_c, C5_run_step_b
- `blink`: 5 khung — D1_face_neutral, D1_face_neutral, D1_face_neutral, D1_face_neutral, D4_face_blink
- `run_away`: 4 khung — S1_run_away_a, S2_run_away_b, S3_run_away_c, S4_run_away_d
- `run_jacket`: 6 khung — U1_run_jacket_1, U2_run_jacket_2, U3_run_jacket_3, U4_run_jacket_4, U5_run_jacket_5, U6_run_jacket_6
- `talk`: 4 khung — D2_face_talk_small, D3_face_talk_open, D2_face_talk_small, D1_face_neutral

| Sprite | Hướng | Mô tả | Tag | Neo |
|---|---|---|---|---|
| `00_idle_front_smile` | front | Đứng thẳng chính diện, mỉm cười nhẹ | đứng, chính diện, vui, bình thường |  |
| `A2_side_nervous_sweat` | right | Đứng nghiêng nhìn ngang, đổ mồ hôi | đứng, nghiêng, lo, nghe ngóng |  |
| `A3_call_out_hand_mouth` | left | Đưa tay lên miệng gọi to | gọi, nói, tay |  |
| `A4_walk_reach_out` | right | Bước tới, đưa tay ra ngang ngực | đi, với tay, chạm | hand |
| `A6_closeup_shock` | front | Cận mặt, mắt trợn, há miệng | cận mặt, sốc, jumpscare, sợ |  |
| `B1_stand_worried` | front | Đứng lo lắng, tay trước ngực | đứng, lo, chính diện |  |
| `B2_look_phone` | front | Đứng nhìn điện thoại | điện thoại, đứng, đọc tin |  |
| `B3_look_back_over_shoulder` | front | Quay lưng, ngoái nhìn qua vai | quay lưng, ngoái lại, bị theo dõi |  |
| `B4_shock_arms_up` | right | Giật mình giơ hai tay, ngã ngửa | sốc, ngã, giật mình |  |
| `C4_run_step_a` | right | Chạy hoảng, khung 1 | chạy, chu kỳ, sợ |  |
| `C5_run_step_b` | right | Chạy hoảng, khung 2 (bay người) | chạy, chu kỳ, sợ |  |
| `C6_run_step_c` | right | Chạy hoảng, khung 3 | chạy, chu kỳ, sợ |  |
| `D1_face_neutral` | front | Cận mặt, miệng ngậm | cận mặt, im, khẩu hình |  |
| `D2_face_talk_small` | front | Cận mặt, miệng hé | cận mặt, nói, khẩu hình |  |
| `D3_face_talk_open` | front | Cận mặt, miệng mở to | cận mặt, nói, khẩu hình |  |
| `D4_face_blink` | front | Cận mặt, nhắm mắt | cận mặt, chớp mắt, ngủ |  |
| `D5_face_whisper_scared` | front | Cận mặt, thì thầm sợ hãi, mồ hôi | cận mặt, thì thầm, sợ |  |
| `D6_face_crying` | front | Cận mặt, khóc | cận mặt, khóc, tuyệt vọng |  |
| `E2_back_stand` | front | Quay lưng đứng yên | quay lưng, đứng, nhìn bóng tối |  |
| `E3_crouch_hug_knees_shaking` | front | Ngồi ôm gối run rẩy (có vạch run) | ngồi, trốn, run, sợ |  |
| `E5_cover_mouth_hold_breath` | front | Bịt miệng nín thở (nửa người) | bịt miệng, nín thở, sợ |  |
| `E6_crouch_cover_ears` | front | Ngồi bịt tai, nhắm mắt | ngồi, bịt tai, sợ |  |
| `F1_flashlight_forward` | left | Đứng soi đèn pin phía trước | đèn pin, đứng, bóng tối |  |
| `F4_phone_call_scared` | front | Nghe điện thoại, sợ | điện thoại, nghe gọi, sợ |  |
| `F5_drop_phone_shock` | left | Đánh rơi điện thoại vì sốc | điện thoại, rơi, sốc |  |
| `F6_phone_show_screen` | left | Giơ màn hình điện thoại ra | điện thoại, tin nhắn, sợ |  |
| `G1_bed_sleeping` | front | Ngủ trên giường (sprite có giường) | giường, ngủ, đêm |  |
| `G2_bed_wake_startled` | front | Giật mình ngồi dậy trên giường | giường, tỉnh dậy, giật mình |  |
| `G3_bed_blanket_chin_scared` | front | Kéo chăn lên cằm, mặt tái | giường, chăn, sợ |  |
| `G4_rub_sleepy_eyes` | front | Đứng dụi mắt ngái ngủ | đứng, ngái ngủ |  |
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
| `M7_lie_prone_back_view` | front | Nằm sấp nhìn từ phía sau (đế giày gần người xem, đầu hướng vào trong), hai tay chống sàn cạnh đầu — ghé nhìn qua khe cửa trên phông nhìn thẳng | nằm sấp, nhìn trộm, khe cửa, sau lưng |  |
| `N1_sit_hug_knees_drowsy` | front | Áo khoác đen: ngồi bó gối dưới sàn, gà gật buồn ngủ | canh linh cữu, buồn ngủ |  |
| `N2_kneel_strike_match` | right | Áo khoác đen: quỳ quẹt diêm, ánh lửa nhỏ hắt lên mặt sợ hãi | quẹt diêm |  |
| `N3_crouch_hold_talisman` | right | Áo khoác đen: ngồi xổm cầm lá bùa vàng gấp tư run run, mắt trợn | lá bùa, sợ |  |
| `N4_tiptoe_peer_down` | right | Áo khoác đen: kiễng chân bám mép (quan tài), nghiêng người nhìn xuống, tay cầm que diêm | quan tài, nhìn trộm |  |
| `N5_stuff_pocket_guilty` | front | Áo khoác đen: nhét lá bùa vào túi áo, liếc ngang tội lỗi | giấu bùa, tội lỗi |  |
| `N6_step_back_frozen` | right | Áo khoác đen: đứng đơ, lùi một bước, mặt tái cứng | lùi lại, sợ |  |
| `O1_mourn_hold_incense_bowl` | front | Áo xô be: đứng ôm bát hương trước ngực, mắt đỏ | đưa tang, bát hương |  |
| `O2_mourn_frozen_pocket` | front | Áo xô be: đứng chết lặng, một tay thọc sâu trong túi siết chặt | chết lặng, lá bùa |  |
| `O3_hold_broken_chopstick` | right | Áo hoodie: cầm chiếc đũa gãy đôi định vứt vào sọt rác, mặt có lỗi | đũa gãy |  |
| `O4_sit_stool_eat_chat` | right | Áo hoodie: ngồi ghế đẩu ăn cơm, vừa ăn vừa kể chuyện vui (có ghế) | bữa cơm, vui |  |
| `O5_mourn_look_up` | right | Áo xô be: đứng ngước nhìn lên cao (con quạ), bất an | quạ, nghĩa địa |  |
| `P1_bed_awake_grip_jacket` | front | Nằm mắt mở thao láo, tay nắm chiếc áo khoác đen treo đầu giường (có giường) | giường, mất ngủ |  |
| `Q1_mourn_kneel_back` | away | Áo xô be: quỳ QUAY LƯNG về người xem, hướng về bàn thờ, chắp tay cúi đầu | tang lễ, quay lưng |  |
| `Q2_frozen_hands_mouth` | front | Áo hoodie: đứng đơ người (quay trái), hai tay bịt miệng, mắt trợn | sốc, ông mất |  |
| `Q3_kneel_mat_worried` | front | Áo hoodie: quỳ ngồi trên gót (quay phải), lo sợ lắng nghe | lo lắng, chiếu |  |
| `R1_floor_box_spare_chopsticks` | right | Ngồi xếp bằng dưới sàn, cẩn thận bỏ đôi đũa dư chữ xấu vào hộp gỗ nhỏ, cặp sách mở trước mặt | đũa dư, ngồi |  |
| `S1_run_away_a` | away | Chạy ra xa (sau lưng) khung 1: chân trái chạm đất, chân phải đá ra sau | chạy, sau lưng |  |
| `S2_run_away_b` | away | Chạy ra xa khung 2: hai chân nhấc khỏi đất giữa không trung | chạy, sau lưng |  |
| `S3_run_away_c` | away | Chạy ra xa khung 3: chân phải chạm đất, chân trái đá ra sau | chạy, sau lưng |  |
| `S4_run_away_d` | away | Chạy ra xa khung 4: hai chân nhấc khỏi đất (bắt chéo ngược lại) | chạy, sau lưng |  |
| `T2_raise_hand_knock_talisman` | right | Áo khoác đen: cầm lá bùa, giơ tay ngập ngừng định gõ cửa | gõ cửa, lá bùa |  |
| `T4_kneel_hold_chopsticks` | front | Áo khoác đen: quỳ (quay trái) hai tay cầm đôi đũa run bần bật, mắt hoảng | đổi đũa, run |  |
| `U1_run_jacket_1` | right | Áo khoác đen: chạy hoảng loạn, khung 1/6 | chạy, chu kỳ, áo khoác |  |
| `U2_run_jacket_2` | right | Áo khoác đen: chạy hoảng loạn, khung 2/6 | chạy, chu kỳ, áo khoác |  |
| `U3_run_jacket_3` | right | Áo khoác đen: chạy hoảng loạn, khung 3/6 | chạy, chu kỳ, áo khoác |  |
| `U4_run_jacket_4` | right | Áo khoác đen: chạy hoảng loạn, khung 4/6 | chạy, chu kỳ, áo khoác |  |
| `U5_run_jacket_5` | right | Áo khoác đen: chạy hoảng loạn, khung 5/6 | chạy, chu kỳ, áo khoác |  |
| `U6_run_jacket_6` | right | Áo khoác đen: chạy hoảng loạn, khung 6/6 | chạy, chu kỳ, áo khoác |  |
| `V1_sneak_peek_scared` | left | Áo hoodie: rón rén khom người nhìn trộm (quay trái), tay siết ngực áo, mắt mở to sợ | nhìn trộm, rón rén, sợ |  |
