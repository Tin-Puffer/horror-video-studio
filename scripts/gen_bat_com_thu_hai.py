"""Sinh scripts/bat_com_thu_hai.json từ mẫu templates/kich_ban_mau.json.
Chạy: python scripts/gen_bat_com_thu_hai.py  (sửa lời/cảnh ở đây rồi chạy lại)."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
story = json.loads((ROOT / "templates/kich_ban_mau.json").read_text(encoding="utf-8"))
story["title"] = "Bát cơm thứ hai"
story["output"] = "build/bat_com_thu_hai.mp4"
story["logline"] = ("Sau khi mẹ mất, Khoa phá lời bà dặn, gọi mẹ giữa đêm tháng bảy. Tiếng gọi ấy dẫn cả bầy cô hồn đói "
                    "vào nhà, và kẻ ngày ngày ngồi ăn cạnh cậu chưa chắc đã là mẹ.")
story["characters"] = {
    "boy_hoodie": {"h": 0.46, "y": 0.96, "tint": True, "glow": False, "breathe": 0.008},
    "ghost_mother": {"tint": True, "glow": True, "breathe": 0.005},
    "mother_alive": {"h": 0.6, "breathe": 0.006},
    "grandma": {"h": 0.5, "breathe": 0.006},
    "hungry_ghost": {"h": 0.58, "glow": True, "breathe": 0.006},
    "props": {"h": 0.3, "breathe": 0},
}
story["asset_requests"] = []

S = []  # scenes


def cam(*keys, handheld=None):
    c = {"keys": [dict(zip(("p", "zoom", "x", "y", "ease"), k)) for k in keys]}
    for k in c["keys"]:
        if k.get("ease") is None:
            k.pop("ease", None)
    if handheld:
        c["handheld"] = handheld
    return c


def sfx(sound, at=0.0, volume=1.0, loop=False, length=None, fade_in=0, fade_out=0):
    d = {"sound": sound, "at": at, "volume": volume}
    if loop:
        d["loop"] = True
    if length:
        d["length"] = length
    if fade_in:
        d["fade_in"] = fade_in
    if fade_out:
        d["fade_out"] = fade_out
    return d


def scene(bg, text=None, layers=(), camera=None, sounds=(), **kw):
    s = {"id": len(S) + 1, "bg": bg}
    if text:
        s["text"] = text
    if camera:
        s["camera"] = camera
    s["sfx"] = list(sounds)
    s["layers"] = list(layers)
    s.update(kw)
    S.append(s)
    return s["id"]


def L(sprite, x=0.5, y="floor", **kw):
    return {"sprite": sprite, "x": x, "y": y, **kw}


# Chỗ ngồi đo trên BG4/BG4d: ghế đẩu của sprite trùm đúng ghế đẩu vẽ trong phông
BOY_SEAT = dict(x=0.59, y=0.83, h=0.46)      # ghế trái, quay phải vào bàn
MOM_SEAT = dict(x=0.85, y=0.81, h=0.55)      # ghế phải, quay trái vào bàn
BY_TABLE = dict(x=0.76, y=0.9, h=0.46)       # đứng sát mép bàn, cạnh ghế phải
BOWL_EMPTY_SEAT = dict(x=0.79, y=0.61, h=0.075)  # bát cơm trên mặt bàn, trước ghế trống


FIRE = {"cycle": "props/fire", "fps": 6, "x": 0.56, "y": 0.96, "h": 0.32, "tint": False, "breathe": 0}  # xô vàng mã cháy


def day(layer):  # flashback: warm daylight, no night tint
    return {**layer, "tint": False}


INSECTS = lambda n=12, v=0.45: sfx("night_insects", 0, v, True, n)
RAIN = lambda n=12, v=0.55: sfx("rain_roof", 0, v, True, n)

# ============================================================ 1. MỞ ĐẦU — ĐÊM 49 (móc câu)
a_open = scene("bg8_bedroom_door",
               "Đêm thứ bốn mươi chín sau ngày mẹ mất, tôi nằm co ro trong bóng tối và nghe thấy tiếng mẹ khóc nghẹn "
               "ngay sau cánh cửa phòng mình, quen thuộc đến mức tim tôi thắt lại.",
               camera=cam((0, 1.15, 0.5, 0.6), (1, 1.4, 0.5, 0.66, "in"), handheld=4),
               sounds=[INSECTS(14, 0.35), sfx("woman_sob_door", 0.15, 0.9, True, 12, 1.0)], fade_in=1.5)
scene("bg8_bedroom_door",
      "Mẹ van tôi mở cửa, giọng run run bảo rằng ngoài này đông lắm, chúng nó không cho mẹ đi, rồi mẹ cứ thế khóc mãi không thôi.",
      [L("boy_hoodie/L5_peek_from_blanket", 0.2, h=0.36, jitter=2)],
      cam((0, 1.25, 0.32, 0.62), (1, 1.25, 0.42, 0.62)),
      [sfx("woman_sob_door", 0, 1.0, True, 12), sfx("heartbeat", 0.3, 0.6, True, 8)])
scene("bg8_bedroom_door",
      "Bà nội đã dặn rằng dù nghe thấy gì cũng không được mở cánh cửa ấy, nhưng trước đêm nay, tôi đã phá hai lời dặn của bà rồi.",
      camera=cam((0, 1.3, 0.55, 0.55), (1, 1.9, 0.555, 0.53, "in"), handheld=5),
      sounds=[sfx("woman_sob_door", 0, 0.7, True, 6, 0, 1.5), sfx("heartbeat", 0, 0.9, True, 12),
              sfx("door_handle_rattle", 0.82, 1.2)])
scene("black", duration=4.0, fade_in=0.6, fade_out=1.0, title_text="BÁT CƠM THỨ HAI",
      sounds=[sfx("ritual_bell", 0.05, 0.9)])
a_open_end = len(S)

# ============================================================ 2. HỒI ỨC — MẸ LÚC CÒN SỐNG (ban ngày)
a_mem = scene("bg6d_kitchen_day",
              "Mẹ tôi là một người phụ nữ hiền lành, chiều nào cũng đứng bên chiếc bếp ga cũ trong căn nhà ống nhỏ, "
              "khuấy nồi canh thơm lừng trong lúc nắng chiều rọi qua ô cửa sổ.",
              [day(L("mother_alive/A1_stir_pot", 0.42, face="left"))],
              cam((0, 1.2, 0.4, 0.6), (1, 1.3, 0.38, 0.6)),
              [sfx("paper_burn", 0, 0.15, True, 12, 1.5, 1.5)], fade_in=1.2)
scene("bg4d_main_room_day",
      "Đến bữa, mẹ lại khum tay gọi vọng lên gác bảo tôi xuống ăn cơm, giọng mẹ ấm áp đến mức bây giờ nhắm mắt lại, tôi vẫn còn nghe thấy.",
      [day(L("mother_alive/A2_call_to_eat", 0.62, 0.88, h=0.56)),
       # tốc độ khớp sải chân: Khoa 3.5 khung/giây ≈ 0.09 khung hình/giây, rồi dừng lại đứng cười
       day({"cycle": "boy_hoodie/walk", "fps": 3.5, "x": [-0.12, 0.28], "y": "floor", "face": "auto", "breathe": 0, "end": 0.6}),
       day(L("boy_hoodie/00_idle_front_smile", 0.28, start=0.6))],
      cam((0, 1.2, 0.38, 0.6), (1, 1.2, 0.45, 0.6)),
      [sfx("footsteps_slow", 0.1, 0.5, True, 5)])
scene("bg4d_main_room_day",
      "Hai mẹ con ngồi bên chiếc bàn gỗ thấp, mẹ gắp cho tôi miếng ngon nhất rồi mới và cơm, vừa ăn vừa hỏi chuyện trường lớp bằng giọng nhẹ nhàng.",
      [day(L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT)), day(L("mother_alive/A5_sit_eat", **MOM_SEAT))],
      cam((0, 1.25, 0.68, 0.6), (1, 1.4, 0.72, 0.6)),
      [sfx("spoon_bowl_tap", 0.3, 0.35)])
scene("bg4d_main_room_day",
      "Ăn xong, mẹ luôn gác đôi đũa nằm ngang trên miệng bát, một thói quen cả đời mẹ không bỏ, dù ngày trước bố tôi đã cằn nhằn không biết bao nhiêu lần.",
      [day(L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT)), day(L("mother_alive/A7_sit_chopsticks_over_bowl", **MOM_SEAT))],
      cam((0, 1.4, 0.72, 0.6), (1, 2.0, 0.84, 0.55, "smooth")),
      [sfx("spoon_bowl_tap", 0.75, 0.3)])
scene("bg6d_kitchen_day",
      "Mẹ còn có một đôi dép nhựa nâu đã mòn vẹt gót, đi đâu cũng lẹp xẹp kéo lê một bên, tôi mua đôi mới mấy lần mà mẹ vẫn chẳng chịu thay.",
      [day(L("props/DC6_mother_slippers", 0.6, 0.93, h=0.2))],
      cam((0, 1.3, 0.6, 0.75), (1, 1.6, 0.6, 0.8)),
      [sfx("slipper_drag", 0.1, 0.5, length=4, fade_out=0.8)])
scene("bg6d_kitchen_day",
      "Tiếng dép ấy đi theo tôi suốt tuổi thơ, sáng sớm vọng ra từ bếp, tối muộn vọng lên ngoài cửa phòng, và tôi chưa bao giờ nghĩ có ngày mình lại sợ nó.",
      # mẹ 2.5 khung/giây ≈ 0.13 khung hình/giây: vào từ tiền cảnh bên phải (sàn trống), đi tới bếp ga rồi đứng khuấy nồi
      [day({"cycle": "mother_alive/walk", "fps": 2.5, "x": [1.15, 0.42], "y": "floor", "face": "auto", "breathe": 0, "bob": 2, "end": 0.69}),
       day(L("mother_alive/A1_stir_pot", 0.42, face="left", start=0.69))],
      cam((0, 1.15, 0.5, 0.6), (1, 1.15, 0.5, 0.6)),
      [sfx("slipper_drag", 0, 0.75, True, 12)], fade_out=0.8)
a_mem_end = len(S)

# ============================================================ 3. MẸ MẤT — BA LỜI DẶN
a_death = scene("bg5_altar_close",
                "Rồi mẹ mất vào một chiều mưa đầu tháng bảy âm lịch, đột ngột đến mức tôi chưa kịp nói với mẹ một lời nào cho tử tế.",
                camera=cam((0, 1.15, 0.5, 0.45), (1, 1.5, 0.5, 0.32)),
                sounds=[RAIN(12, 0.6), sfx("ritual_bell", 0.4, 0.5)], fade_in=1.5)
scene("bg4_main_room",
      "Những ngày tang lễ trôi qua trong mùi nhang khói và tiếng mõ đều đều, tôi chỉ biết ngồi ôm gối ở góc nhà, nhìn tấm ảnh mẹ cười hiền trên bàn thờ.",
      [L("boy_hoodie/E3_crouch_hug_knees_shaking", 0.14, h=0.36, jitter=1)],
      cam((0, 1.2, 0.25, 0.55), (1, 1.3, 0.25, 0.45)),
      [RAIN(12, 0.5), sfx("ritual_bell", 0.1, 0.35)])
scene("bg4_main_room",
      "Đêm cuối cùng của tang lễ, bà nội chống lưng bước tới bên tôi, đôi mắt đỏ hoe, rồi bà kéo tôi đứng dậy trước bàn thờ mẹ.",
      [L("boy_hoodie/B1_stand_worried", 0.22),
       # bà 2.5 khung/giây ≈ 0.08 khung hình/giây, đi ra từ cửa bếp (mép phải) rồi dừng trước mặt Khoa
       {"cycle": "grandma/walk", "fps": 2.5, "x": [0.92, 0.45], "y": "floor", "face": "auto", "breathe": 0, "bob": 2, "end": 0.9},
       L("grandma/00_stand_front", 0.45, start=0.9)],
      cam((0, 1.2, 0.45, 0.6), (1, 1.2, 0.35, 0.6)),
      [RAIN(10, 0.45), sfx("footsteps_slow", 0.05, 0.4, True, 5)])
scene("bg4_main_room",
      "Bà nắm chặt tay tôi bằng những ngón tay lạnh ngắt, ghé sát tai dặn ba điều, và bắt tôi nhắc lại từng điều một cho đến khi thuộc lòng.",
      [L("grandma/E1_hold_boy_hands", 0.45, h=0.5, end=0.55), L("grandma/E2_whisper_boy_ear", 0.45, h=0.5, start=0.55)],
      cam((0, 1.3, 0.45, 0.62), (1, 1.6, 0.45, 0.62)),
      [RAIN(10, 0.4)])
scene("bg5_altar_close",
      "Điều thứ nhất, cúng cơm cho mẹ xong phải đợi nén nhang tàn hẳn rồi mới được dọn mâm, tuyệt đối không được vội vàng.",
      [L("props/DC1b_bowl_chopsticks_vertical", 0.52, 0.83, h=0.42)],
      cam((0, 1.2, 0.45, 0.5), (1, 1.45, 0.5, 0.6)),
      [RAIN(9, 0.3), sfx("ritual_bell", 0.05, 0.35)])
scene("bg4_main_room",
      "Điều thứ hai, trời tối thì tuyệt đối không được gọi tên mẹ, vì người đã khuất nghe tiếng con gọi sẽ không nỡ mà đi.",
      [L("grandma/A6_head_bowed_face_hidden", 0.45, h=0.5)],
      cam((0, 1.4, 0.45, 0.62), (1, 1.9, 0.45, 0.58, "in"), handheld=3),
      [RAIN(9, 0.3), sfx("whisper_eerie", 0.6, 0.35)])
scene("bg8_bedroom_door",
      "Và điều thứ ba, đêm thứ bốn mươi chín, dù nghe thấy bất cứ điều gì, tôi cũng không được bước chân ra khỏi phòng.",
      camera=cam((0, 1.15, 0.5, 0.6), (1, 1.6, 0.5, 0.75, "in")),
      sounds=[RAIN(9, 0.25), sfx("dog_howl", 0.55, 0.6)], fade_out=0.8)

# ============================================================ 4. TUẦN ĐẦU — BÁT CƠM VƠI
a_week = scene("bg4_main_room",
               "Từ hôm đó, chiều nào tôi cũng xới một bát cơm thật đầy, đặt lên trên một quả trứng luộc và cắm thẳng đôi đũa tre vào giữa bát.",
               [L("boy_hoodie/M2_carry_rice_bowl", 0.42, face="left")],
               cam((0, 1.2, 0.38, 0.55), (1, 1.3, 0.35, 0.5)),
               [INSECTS(10, 0.4), sfx("footsteps_slow", 0.05, 0.4, length=2)], fade_in=1.0)
scene("bg4_main_room",
      "Rồi tôi quỳ xuống thắp ba nén nhang, nhìn làn khói xám uốn lượn qua tấm ảnh mẹ, thì thầm kể cho mẹ nghe chuyện trong ngày như hồi mẹ còn sống.",
      [L("boy_hoodie/M1_kneel_incense", 0.4, h=0.34, face="left")],
      cam((0, 1.3, 0.38, 0.62), (1, 1.45, 0.36, 0.56)),
      [INSECTS(11, 0.35), sfx("ritual_bell", 0.15, 0.3)])
scene("bg5_altar_close",
      "Tuần đầu tiên trôi qua yên ả, sáng nào bát cơm cũng còn nguyên, quả trứng vẫn nằm đó, đôi đũa vẫn cắm thẳng như lúc tôi đặt xuống.",
      [L("props/DC1b_bowl_chopsticks_vertical", 0.52, 0.83, h=0.42)],
      cam((0, 1.2, 0.5, 0.55), (1, 1.3, 0.52, 0.6)),
      [sfx("clock_tick", 0, 0.4, True, 10)])
scene("bg5_altar_close",
      "Cho đến một buổi sáng, khi bưng mâm xuống, tôi khựng lại, bởi bát cơm đã vơi đi một góc nhỏ như có ai vừa ăn vài miếng.",
      [L("props/DC2_bowl_chopsticks_across", 0.52, 0.82, h=0.26)],
      cam((0, 1.2, 0.5, 0.55), (1, 1.6, 0.52, 0.7, "in")),
      [sfx("clock_tick", 0, 0.35, True, 6, 0, 1), sfx("heartbeat", 0.4, 0.5, True, 6)])
scene("bg5_altar_close",
      "Đôi đũa không còn cắm thẳng nữa mà nằm gác ngang trên miệng bát, đúng y như thói quen cả đời của mẹ.",
      [L("props/DC2_bowl_chopsticks_across", 0.52, 0.82, h=0.26)],
      cam((0, 1.6, 0.52, 0.7), (1, 2.2, 0.52, 0.72, "smooth")),
      [sfx("heartbeat", 0, 0.45, True, 7)])
scene("bg4_main_room",
      "Lạ thay, tôi không thấy sợ, trong lòng chỉ dâng lên một cảm giác ấm áp kỳ lạ, vì tôi tin rằng mẹ vẫn còn về thăm tôi.",
      [L("boy_hoodie/00_idle_front_smile", 0.35)],
      cam((0, 1.25, 0.35, 0.6), (1, 1.35, 0.33, 0.55)),
      [INSECTS(9, 0.35), sfx("spoon_bowl_tap", 0.7, 0.2)])

# ============================================================ 5. TIẾNG DÉP BAN ĐÊM
a_steps = scene("bg1_bedroom",
                "Những đêm sau, nằm trong bóng tối, tôi bắt đầu nghe thấy tiếng dép lẹp xẹp từ dưới bếp vọng lên, chậm rãi, kéo lê một bên.",
                [L("boy_hoodie/G1_bed_sleeping", 0.7, 0.95, h=0.5)],
                cam((0, 1.2, 0.6, 0.6), (1, 1.35, 0.68, 0.65)),
                [INSECTS(10, 0.35), sfx("slipper_drag", 0.2, 0.45, True, 9, 1.0)], fade_in=1.0)
scene("bg6_kitchen",
      "Đó y hệt tiếng đôi dép mòn gót mẹ đi suốt mấy năm không chịu thay, có đêm còn xen lẫn tiếng thìa khẽ gõ vào thành bát, rồi mọi thứ lại im bặt.",
      [L("props/DC6_mother_slippers", 0.69, 0.7, h=0.07)],
      cam((0, 1.2, 0.45, 0.55), (1, 1.6, 0.66, 0.6, "smooth"), handheld=3),
      [sfx("slipper_drag", 0, 0.7, True, 6, 0, 1.0), sfx("spoon_bowl_tap", 0.55, 0.6)])
scene("bg1_bedroom",
      "Một đêm, tôi lấy hết can đảm trở dậy, rón rén đi xuống bếp xem thử, tim đập thình thịch theo từng bước chân trần trên sàn lạnh.",
      [L("boy_hoodie/G2_bed_wake_startled", 0.7, 0.95, h=0.54)],
      cam((0, 1.3, 0.68, 0.6), (1, 1.3, 0.68, 0.6)),
      [INSECTS(10, 0.3), sfx("heartbeat", 0.3, 0.6, True, 7)])
scene("bg6_kitchen", duration=4.5,
      layers=[{"cycle": "boy_hoodie/tiptoe", "fps": 6, "x": [0.95, 0.6], "y": "floor", "face": "auto", "breathe": 0}],
      camera=cam((0, 1.2, 0.7, 0.6), (1, 1.2, 0.6, 0.6), handheld=4),
      sounds=[sfx("floor_creak", 0.2, 0.7), sfx("heartbeat", 0, 0.6, True, 4.5)])
scene("bg4_main_room",
      "Bếp vắng tanh, nhưng ngoài gian thờ, chiếc ghế đẩu mẹ vẫn ngồi mỗi bữa cơm đã bị ai đó kéo lệch ra khỏi bàn, như vừa có người đứng dậy.",
      [L("boy_hoodie/A2_side_nervous_sweat", 0.35, face="right", jitter=1)],
      cam((0, 1.2, 0.4, 0.6), (1, 1.7, 0.6, 0.68, "in"), handheld=4),
      [sfx("clock_tick", 0, 0.4, True, 10), sfx("floor_creak", 0.15, 0.4)])
scene("bg4_main_room",
      "Tôi đứng lặng hồi lâu rồi tự nhủ chắc mẹ chỉ về ngồi ăn với tôi một chút thôi, và tôi đẩy chiếc ghế lại chỗ cũ, khẽ chúc mẹ ngủ ngon.",
      [L("boy_hoodie/A4_walk_reach_out", 0.49, 0.88, h=0.44, face="right")],
      cam((0, 1.35, 0.55, 0.62), (1, 1.4, 0.58, 0.64)),
      [sfx("clock_tick", 0, 0.35, True, 10), sfx("floor_creak", 0.5, 0.3)], fade_out=0.8)

# ============================================================ 6. ĐÊM 21 — TIẾNG GỌI
a_call = scene("bg1_bedroom",
               "Đêm thứ hai mươi mốt, nỗi nhớ mẹ dâng lên đến nghẹt thở, tôi trùm chăn kín đầu mà nước mắt cứ thế chảy ra không sao ngăn được.",
               [L("boy_hoodie/L5_peek_from_blanket", 0.68, h=0.36)],
               cam((0, 1.2, 0.62, 0.62), (1, 1.5, 0.68, 0.7)),
               [RAIN(12, 0.5), sfx("slipper_drag", 0.1, 0.35, True, 10, 1.0)], fade_in=1.0)
scene("bg1_bedroom",
      "Và trước khi kịp nghĩ đến lời bà dặn, môi tôi đã khẽ bật ra hai tiếng mẹ ơi.",
      [L("boy_hoodie/D6_face_crying", 0.5, 1.02, h=0.95)],
      cam((0, 1.15, 0.5, 0.5), (1, 1.25, 0.5, 0.46)),
      [RAIN(7, 0.4), sfx("slipper_drag", 0, 0.45, True, 5.5, 0, 0)])
scene("bg1_bedroom", duration=3.0, bg_dim=0.45,
      layers=[L("boy_hoodie/L5_peek_from_blanket", 0.68, h=0.36)],
      camera=cam((0, 1.5, 0.68, 0.7), (1, 1.6, 0.68, 0.7)),
      sounds=[sfx("heartbeat", 0.2, 0.7, True, 2.8)])
scene("bg6_kitchen",
      "Ngay lúc ấy, tiếng dép dưới bếp đột ngột dừng lại, và cả căn nhà chìm vào một sự im lặng nặng nề đến mức tôi nghe rõ cả tiếng tim mình.",
      camera=cam((0, 1.2, 0.6, 0.5), (1, 1.8, 0.69, 0.42, "in"), handheld=5),
      sounds=[sfx("heartbeat", 0, 0.8, True, 11), sfx("dog_howl", 0.75, 0.55)], fade_out=1.0)
a_call_end = len(S)

# ============================================================ 7. LEO THANG
a_esc = scene("bg5_altar_close",
              "Sáng hôm sau, bát cơm trên bàn thờ sạch trơn không còn lấy một hạt, quả trứng chỉ còn lại mấy mảnh vỏ vỡ vụn nằm vương vãi bên cạnh.",
              [L("props/DC3_bowl_empty_eggshell", 0.52, 0.82, h=0.3)],
              cam((0, 1.2, 0.5, 0.55), (1, 1.6, 0.52, 0.68, "in")),
              [sfx("clock_tick", 0, 0.35, True, 10), sfx("reverse_swell", 0.55, 0.5)], fade_in=0.8)
scene("black",
      "Còn nén nhang tôi thắp tối qua thì gãy gập ngay giữa bát hương, như bị ai đó bẻ quặt xuống.",
      [L("props/DC4_incense_broken", 0.5, 0.85, h=0.62)],
      cam((0, 1.15, 0.5, 0.5), (1, 1.3, 0.5, 0.42)),
      [sfx("heartbeat", 0, 0.5, True, 7)])
scene("bg4_main_room",
      "Tối đó tôi xới bát cơm đầy hơn, sáng ra vẫn sạch trơn, tôi xới thêm một bát nữa, và sáng hôm sau, cả hai bát đều trống rỗng.",
      [L("boy_hoodie/M2_carry_rice_bowl", 0.42, face="left")],
      cam((0, 1.2, 0.38, 0.55), (1, 1.4, 0.35, 0.45)),
      [INSECTS(10, 0.3), sfx("clock_tick", 0, 0.3, True, 10)])
scene("bg5_altar_close", duration=3.2,
      layers=[L("props/DC3_bowl_empty_eggshell", 0.38, 0.82, h=0.27), L("props/DC3_bowl_empty_eggshell", 0.64, 0.83, h=0.27)],
      camera=cam((0, 1.3, 0.51, 0.66), (1, 1.45, 0.51, 0.68)),
      sounds=[sfx("reverse_swell", 0, 0.6)])
scene("bg1_bedroom",
      "Rồi đến cái đêm tôi nghe thấy tiếng bát đũa lách cách ngoài gian thờ, không phải của một đôi đũa mà là rất nhiều đôi, va vào nhau gấp gáp.",
      [L("boy_hoodie/G3_bed_blanket_chin_scared", 0.7, 0.95, h=0.5, jitter=1)],
      cam((0, 1.2, 0.65, 0.6), (1, 1.45, 0.7, 0.6, "in")),
      [sfx("chopsticks_clatter", 0.2, 0.8, True, 9), INSECTS(10, 0.2)])
scene("bg1_bedroom",
      "Xen lẫn trong đó là những tiếng nhai nhóp nhép, húp xì xụp, như có cả một mâm người đang ăn vội vàng trong bóng tối.",
      [L("boy_hoodie/G3_bed_blanket_chin_scared", 0.7, 0.95, h=0.5, jitter=2)],
      cam((0, 1.45, 0.7, 0.6), (1, 1.8, 0.7, 0.55, "in"), handheld=4),
      [sfx("chewing_wet", 0, 0.8, True, 9), sfx("chopsticks_clatter", 0, 0.5, True, 9)])
scene("bg8_bedroom_door",
      "Tôi run rẩy bò xuống sàn, áp má vào nền gỗ lạnh ngắt, rồi ghé mắt nhìn qua khe hở nhỏ dưới chân cửa.",
      [L("boy_hoodie/M7_lie_prone_back_view", 0.5, 1.22, h=0.42)],
      cam((0, 1.2, 0.5, 0.65), (1, 1.6, 0.5, 0.8, "in")),
      [sfx("chewing_wet", 0, 0.5, True, 8), sfx("floor_creak", 0.15, 0.5)])
scene("bg9b_door_gap_ghosts",
      "Trong ánh nến đỏ leo lét, tôi thấy thấp thoáng những cái bóng gầy rộc ngồi xổm quanh mâm cơm, đôi tay đen đúa bốc cơm nhét vào miệng.",
      camera=cam((0, 1.2, 0.35, 0.53), (1, 1.2, 0.65, 0.53, "smooth"), handheld=3),
      sounds=
      [sfx("chewing_wet", 0, 0.9, True, 10), sfx("chopsticks_clatter", 0.1, 0.5, True, 9)])
scene("bg9b_door_gap_ghosts",
      "Một cái bóng bỗng ngừng nhai, rồi ngẩng phắt lên, nhìn thẳng về phía khe cửa nơi tôi đang nằm.",
      camera=cam((0, 1.25, 0.5, 0.52), (1, 1.9, 0.49, 0.42, "in"), handheld=4),
      sounds=[sfx("chewing_wet", 0, 0.7, True, 8, 0, 0.6), sfx("heartbeat", 0.4, 0.7, True, 5)])
scene("bg9c_door_gap_face", duration=2.6, fade_in=0, flash=[0.0], shake={"amp": 12, "from": 0, "to": 0.45},
      camera=cam((0, 1.25, 0.45, 0.5), (1, 1.45, 0.43, 0.48, "out")),
      sounds=[sfx("ghost_stinger", 0, 1.8)])
scene("bg1c_corner_night",
      "Tôi lùi lại, bịt chặt hai tai, ngồi co ro trong góc phòng đến tận sáng mà không dám nhắm mắt lấy một lần.",
      camera=cam((0, 1.15, 0.45, 0.55), (1, 1.75, 0.5, 0.45, "in"), handheld=4),
      sounds=[sfx("heartbeat", 0, 0.7, True, 9), sfx("chewing_wet", 0, 0.25, True, 6, 0, 3), sfx("breath_close", 0.35, 0.5),
              sfx("clock_tick", 0.5, 0.35, True, 5, 1.0)], fade_out=1.2)
scene("bg1d_corner_dawn", duration=4.0, fade_in=1.5, fade_out=1.0,
      camera=cam((0, 1.6, 0.5, 0.47), (1, 1.4, 0.5, 0.5, "smooth")),
      sounds=[sfx("clock_tick", 0, 0.35, True, 4, 0, 1.0), sfx("breath_close", 0.4, 0.3)])
scene("bg4_main_room",
      "Sáng ra, quanh mâm cơm có những dấu tay đen in khắp mặt bàn gỗ, dấu của rất nhiều bàn tay gầy guộc với những ngón dài khẳng khiu.",
      [L("props/DC5_black_handprints", 0.69, 0.63, h=0.06), L("props/DC5_black_handprints", 0.785, 0.625, h=0.055)],
      cam((0, 1.3, 0.6, 0.55), (1, 2.6, 0.73, 0.6, "smooth")),
      [sfx("clock_tick", 0, 0.35, True, 10), sfx("reverse_swell", 0.5, 0.4)], fade_in=0.8)
scene("bg4_main_room",
      "Tôi nhìn chúng rất lâu, và tôi biết chắc rằng không có bàn tay nào trong số ấy là của mẹ.",
      [L("props/DC5_black_handprints", 0.69, 0.63, h=0.06), L("props/DC5_black_handprints", 0.785, 0.625, h=0.055)],
      cam((0, 2.6, 0.73, 0.6), (1, 3.0, 0.73, 0.6)),
      [sfx("heartbeat", 0, 0.5, True, 7)])
scene("bg4_main_room",
      "Bà nội đứng nhìn những dấu tay ấy thật lâu, rồi chậm rãi quay sang hỏi tôi có gọi mẹ vào ban đêm hay không.",
      [L("grandma/A6_head_bowed_face_hidden", 0.55), L("boy_hoodie/B1_stand_worried", 0.3)],
      cam((0, 1.25, 0.45, 0.6), (1, 1.4, 0.48, 0.6)),
      [sfx("clock_tick", 0, 0.35, True, 9)])
scene("bg4_main_room",
      "Tôi cúi gằm mặt không đáp, bà ngồi sụp xuống bậc cửa, giọng run run bảo rằng tháng bảy là tháng cửa âm mở toang.",
      [L("grandma/A4_sit_hug_knees_grief", 0.92, 0.97, h=0.3), L("boy_hoodie/B1_stand_worried", 0.55)],
      cam((0, 1.3, 0.6, 0.65), (1, 1.5, 0.72, 0.68)),
      [sfx("clock_tick", 0, 0.3, True, 9), sfx("whisper_eerie", 0.7, 0.3)])
scene("bg4_main_room",
      "Bà bảo tôi chỉ gọi có một người, nhưng những kẻ đói khát lang thang ngoài kia đều đã nghe thấy, và chúng đã lần theo tiếng gọi ấy mà vào nhà.",
      [L("grandma/A4_sit_hug_knees_grief", 0.92, 0.97, h=0.3)],
      cam((0, 1.5, 0.8, 0.7), (1, 2.0, 0.88, 0.75, "in")),
      [sfx("dog_howl", 0.6, 0.6)], fade_out=1.0)
a_esc_end = len(S)

# ============================================================ 8. LỄ CÚNG CÔ HỒN — TIẾNG GỌI NGOÀI CỔNG
a_rit = scene("bg7_front_yard",
              "Chiều hôm ấy, bà bày một mâm cúng cô hồn ngoài sân, vừa lâm râm khấn vái vừa vốc từng nắm gạo muối rải ra phía cổng sắt.",
              [L("grandma/A3_scatter_rice_salt", 0.45, face="right")],
              cam((0, 1.2, 0.45, 0.6), (1, 1.3, 0.5, 0.6)),
              [sfx("rice_scatter", 0.25), sfx("rice_scatter", 0.6, 0.8), sfx("ritual_bell", 0.05, 0.4)], fade_in=1.0)
scene("bg7_front_yard",
      "Bà đốt một xấp vàng mã trong chiếc thùng sắt cũ, khói bay mù mịt, miệng lẩm bẩm xin các vong đã no thì đi đi, đừng quay lại nữa.",
      [L("boy_hoodie/E2_back_stand", 0.18), L("props/VM4_grandma_crouch_drop_paper", 0.42, 0.95, h=0.3, tint=False),
       FIRE],
      cam((0, 1.25, 0.42, 0.62), (1, 1.5, 0.5, 0.62)),
      [sfx("paper_burn", 0, 0.8, True, 12), sfx("ritual_bell", 0.75, 0.3)])
scene("bg7_front_yard", duration=4.0,
      layers=[L("props/VM6_joss_paper_stack", 0.42, 0.97, h=0.07), FIRE],
      camera=cam((0, 1.6, 0.56, 0.7), (1, 2.0, 0.56, 0.66, "smooth")),
      sounds=[sfx("paper_burn", 0, 0.9, True, 4.0, 0, 0.8), sfx("whisper_eerie", 0.5, 0.25)])
scene("bg4_main_room",
      "Mấy đêm sau, căn nhà yên tĩnh trở lại, bát cơm trên bàn thờ còn nguyên, và tôi đã ngỡ rằng mọi chuyện thế là xong.",
      [L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT)],
      cam((0, 1.2, 0.62, 0.6), (1, 1.3, 0.66, 0.6)),
      [INSECTS(10, 0.45), sfx("clock_tick", 0, 0.25, True, 10)])
scene("bg7_front_yard",
      "Cho đến một đêm, tôi nghe tiếng cổng sắt rung lạch cạch, rồi một giọng khàn đặc từ ngoài đường vọng vào, gọi tên tôi rất chậm.",
      camera=cam((0, 1.2, 0.6, 0.5), (1, 1.8, 0.69, 0.45, "in"), handheld=4),
      sounds=[sfx("gate_rattle", 0.15, 1.0), sfx("whisper_eerie", 0.55, 0.8), INSECTS(10, 0.2)])
scene("bg7_front_yard",
      "Qua song cổng, giữa làn sương, tôi thấy một cái bóng cổ dài đứng im, khuôn mặt hõm sâu ngước về phía cửa sổ phòng tôi.",
      [L("hungry_ghost/A3_stand_front", 0.69, 0.64, h=0.34)],
      cam((0, 1.8, 0.69, 0.45), (1, 2.3, 0.69, 0.42, "in"), handheld=4),
      [sfx("whisper_eerie", 0.1, 0.7), sfx("heartbeat", 0, 0.7, True, 9), sfx("gate_rattle", 0.8, 0.6)], fade_out=1.0)
a_rit_end = len(S)

# ============================================================ 9. ĐÊM 49 — CAO TRÀO
a_49 = scene("bg4_main_room",
             "Đêm thứ bốn mươi chín, bà tắt hết đèn trong nhà, đặt mâm cơm cuối cùng lên bàn thờ, rồi lặng lẽ dắt tôi về phòng.",
             [L("grandma/A5_scoop_rice", 0.64, 0.86, h=0.46), L("boy_hoodie/B1_stand_worried", 0.42)],
             cam((0, 1.2, 0.5, 0.55), (1, 1.3, 0.48, 0.52)),
             [INSECTS(10, 0.3), sfx("ritual_bell", 0.1, 0.3)], fade_in=1.2, bg_dim=0.2)
scene("bg8_bedroom_door",
      "Bà khoá cửa phòng tôi từ bên ngoài, dặn dù có chuyện gì cũng phải nằm yên, vì đêm nay là đêm mẹ phải đi.",
      [L("boy_hoodie/B1_stand_worried", 0.25)],
      cam((0, 1.2, 0.45, 0.6), (1, 1.5, 0.58, 0.5, "in")),
      [sfx("door_bolt_lock", 0.2, 1.1), INSECTS(9, 0.25)])
scene("bg8_bedroom_door",
      "Gần nửa đêm, tiếng dép lẹp xẹp lại vang lên dưới bếp, chậm rãi đi lên, và lần này nó dừng lại ngay trước cửa phòng tôi.",
      [L("boy_hoodie/L5_peek_from_blanket", 0.18, h=0.36, jitter=1)],
      cam((0, 1.2, 0.4, 0.62), (1, 1.6, 0.5, 0.8, "in")),
      [sfx("slipper_drag", 0, 0.6, True, 9, 1.0, 0.1), sfx("heartbeat", 0.5, 0.6, True, 6)])
scene("bg8_bedroom_door",
      "Rồi mẹ khóc, mẹ bảo mẹ muốn đi mà không đi được, chúng nó bám lấy mẹ, chúng nó đói lắm, con ra tiễn mẹ một đoạn thôi con.",
      camera=cam((0, 1.5, 0.5, 0.75), (1, 1.9, 0.5, 0.8, "in"), handheld=4),
      sounds=[sfx("woman_sob_door", 0, 1.0, True, 11), sfx("heartbeat", 0, 0.6, True, 11)])
scene("bg8_bedroom_door",
      "Tôi bịt chặt hai tai, nhưng tiếng khóc như rót thẳng vào đầu, mỗi tiếng nấc lại kéo tôi lại gần cánh cửa thêm một chút.",
      [L("boy_hoodie/E6_crouch_cover_ears", 0.24, h=0.4, jitter=2)],
      cam((0, 1.3, 0.3, 0.65), (1, 1.3, 0.4, 0.65), handheld=5),
      [sfx("woman_sob_door", 0, 1.1, True, 11), sfx("whisper_eerie", 0.5, 0.4)])
scene("bg8_bedroom_door",
      "Không biết từ lúc nào, tôi đã đứng trước cửa, bàn tay đặt lên nắm cửa lạnh buốt.",
      [L("boy_hoodie/K2_reach_up_grip", 0.5, h=0.52, face="right")],
      cam((0, 1.3, 0.5, 0.6), (1, 1.7, 0.53, 0.55, "in")),
      [sfx("woman_sob_door", 0, 0.7, True, 7, 0, 2.0), sfx("heartbeat", 0, 0.9, True, 7)])
scene("bg8_bedroom_door",
      "Cánh cửa bà đã khoá từ bên ngoài, không hiểu vì sao, lại khẽ mở ra.",
      [L("boy_hoodie/K2_reach_up_grip", 0.5, h=0.52, face="right")],
      cam((0, 1.7, 0.53, 0.55), (1, 2.2, 0.5, 0.55, "in")),
      [sfx("door_creak_open", 0.35, 1.2)])
scene("bg4_main_room",
      "Gian thờ tối om, chỉ còn ba đốm nhang đỏ lập loè, và mẹ đứng quay lưng về phía tôi, ngay cạnh chiếc ghế mẹ vẫn ngồi mỗi bữa cơm.",
      [L("ghost_mother/GH9_back_stand", 0.88, 0.86, h=0.48)],
      cam((0, 1.2, 0.5, 0.55), (1, 1.5, 0.75, 0.6, "smooth"), handheld=3),
      [sfx("heartbeat", 0, 0.5, True, 10), sfx("chewing_wet", 0.5, 0.3, True, 5, 1.5)], bg_dim=0.3, fade_in=0.8)
scene("bg4_main_room",
      "Quanh mẹ, chen chúc kín cả gian nhà, là những cái bóng gầy rộc cổ dài ngoẵng, cúi gằm xuống mâm, bốc cơm từ bát của mẹ mà ăn ngấu nghiến.",
      [L("hungry_ghost/A1_crouch_eat_rice", 0.6, 0.84, h=0.3),
       L("ghost_mother/GH9_back_stand", 0.88, 0.86, h=0.48),
       L("hungry_ghost/A5_reach_black_hand", 0.68, 0.92, h=0.42, face="right"),
       L("hungry_ghost/A6_crawl", 0.38, 0.98, h=0.22, face="right"),
       L("hungry_ghost/A1_crouch_eat_rice", 0.78, 0.98, h=0.36, face="left")],
      cam((0, 1.3, 0.4, 0.62), (1, 1.3, 0.72, 0.62, "smooth"), handheld=4),
      [sfx("chewing_wet", 0, 1.0, True, 11), sfx("chopsticks_clatter", 0.1, 0.6, True, 10)], bg_dim=0.3)
scene("bg4_main_room",
      "Mẹ từ từ quay đầu lại, đôi mắt mẹ đen kịt không còn lòng trắng, và mẹ thì thầm, như trách, như thương, [0.7] sao con lại gọi.",
      [L("hungry_ghost/A1_crouch_eat_rice", 0.6, 0.84, h=0.3),
       L("ghost_mother/GH9_back_stand", 0.88, 0.86, h=0.48, end=0.35),
       L("ghost_mother/GH11_fake_smile_black_eyes", 0.88, 0.86, h=0.48, start=0.35),
       L("hungry_ghost/A1_crouch_eat_rice", 0.78, 0.98, h=0.36, face="left")],
      cam((0, 1.6, 0.8, 0.6), (1, 2.6, 0.88, 0.5, "in"), handheld=3),
      [sfx("chewing_wet", 0, 0.5, True, 10), sfx("whisper_eerie", 0.65, 0.9)], bg_dim=0.3)
scene("bg4_main_room",
      "Tất cả những cái bóng cùng lúc ngừng ăn, và ngẩng lên nhìn tôi.",
      [L("hungry_ghost/A3_stand_front", 0.48, 0.86, h=0.46),
       L("hungry_ghost/A2_crouch_look_up", 0.6, 0.84, h=0.3, face="left"),
       L("ghost_mother/GH11_fake_smile_black_eyes", 0.88, 0.86, h=0.48),
       L("hungry_ghost/A2_crouch_look_up", 0.36, 0.98, h=0.34),
       L("hungry_ghost/A2_crouch_look_up", 0.78, 0.98, h=0.36, face="left")],
      cam((0, 1.25, 0.62, 0.6), (1, 1.4, 0.62, 0.58, "in"), handheld=5),
      [sfx("reverse_swell", 0.1, 0.9)], bg_dim=0.3)
scene("bg4_main_room", duration=1.6, fade_in=0, bg_dim=0.45, flash=[0.0], shake={"amp": 16, "from": 0, "to": 0.6},
      sounds=[sfx("ghost_stinger", 0, 2.2)],
      layers=[{"sprite": "ghost_mother/GH4_closeup_lunge_grin", "x": 0.5, "y": 1.05, "h": [0.7, 1.25], "ease": "out", "glow": True}])
scene("black", duration=3.0, fade_in=0, sounds=[sfx("heartbeat", 0.2, 0.6, length=2.5, fade_out=1.0)])
a_49_end = len(S)

# ============================================================ 10. KẾT — BÁT CƠM THỨ HAI
a_end = scene("bg8_bedroom_door",
              "Sáng hôm sau, bà tìm thấy tôi nằm ngất lịm trước cửa phòng, bà ôm tôi khóc rồi bảo hồn mẹ đã đi rồi, đã yên rồi.",
              [L("boy_hoodie/M5_lie_unconscious", 0.5, 0.99, h=0.13), L("grandma/A6_head_bowed_face_hidden", 0.75)],
              cam((0, 1.25, 0.6, 0.7), (1, 1.35, 0.6, 0.72)),
              [INSECTS(10, 0.25), sfx("clock_tick", 0, 0.3, True, 10)], fade_in=1.5)
scene("bg4_main_room",
      "Nhưng từ hôm ấy, bữa cơm nào bà cũng lặng lẽ xới thêm một bát, đặt trước chiếc ghế trống bên cạnh tôi.",
      [L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT), L("grandma/A5_scoop_rice", **BY_TABLE)],
      cam((0, 1.2, 0.68, 0.6), (1, 1.35, 0.72, 0.6)),
      [sfx("spoon_bowl_tap", 0.4, 0.3), INSECTS(9, 0.25)])
scene("bg4_main_room",
      "Tôi hỏi bát ấy là cho ai, bà chỉ cúi mặt xuống mâm, không trả lời.",
      [L("props/DC1b_bowl_chopsticks_vertical", **BOWL_EMPTY_SEAT), L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT),
       L("grandma/A6_head_bowed_face_hidden", **BY_TABLE)],
      cam((0, 1.35, 0.68, 0.6), (1, 1.6, 0.74, 0.56, "in")),
      [sfx("clock_tick", 0, 0.35, True, 7)])
scene("bg4_main_room",
      "Mỗi tối, tôi vẫn cảm thấy có ai đó ngồi sát bên mình, im lặng ăn cùng, hơi lạnh phả nhẹ vào một bên má.",
      [L("props/DC1b_bowl_chopsticks_vertical", **BOWL_EMPTY_SEAT), L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT)],
      cam((0, 1.3, 0.65, 0.6), (1, 1.7, 0.8, 0.62, "smooth")),
      [sfx("chewing_wet", 0.3, 0.15, True, 6, 1.0, 1.0), sfx("breath_close", 0.6, 0.4)])
scene("bg5_altar_close",
      "Sáng ra bát cơm ấy luôn sạch trơn, và tôi đã tự nhủ rằng đó là mẹ, rằng mẹ chưa bao giờ thật sự rời xa tôi.",
      [L("props/DC3_bowl_empty_eggshell", 0.52, 0.82, h=0.3)],
      cam((0, 1.2, 0.5, 0.45), (1, 1.35, 0.5, 0.32)),
      [sfx("clock_tick", 0, 0.3, True, 10)])
scene("bg4_main_room",
      "Cho đến sáng nay, khi tôi để ý đến đôi đũa.",
      [L("props/DC1b_bowl_chopsticks_vertical", **BOWL_EMPTY_SEAT), L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT)],
      cam((0, 1.3, 0.66, 0.6), (1, 1.7, 0.72, 0.6, "in")),
      [sfx("clock_tick", 0, 0.4, True, 4, 0, 0.5)], min_duration=3.2)
scene("bg4d_main_room_day",
      "Mẹ tôi cả đời luôn gác đũa nằm ngang trên miệng bát.",
      [day(L("mother_alive/A7_sit_chopsticks_over_bowl", **MOM_SEAT))],
      cam((0, 1.6, 0.8, 0.58), (1, 1.9, 0.84, 0.55)),
      [sfx("spoon_bowl_tap", 0.3, 0.25)], fade_in=0.6, fade_out=0.6, min_duration=3.5)
scene("bg5_altar_close",
      "Còn kẻ ngồi cạnh tôi mỗi bữa cơm thì cắm thẳng đôi đũa xuống giữa bát, như bát cơm cúng người chết.",
      [L("props/DC1b_bowl_chopsticks_vertical", 0.52, 0.83, h=0.42)],
      cam((0, 1.2, 0.52, 0.6), (1, 2.0, 0.52, 0.62, "in")),
      [sfx("heartbeat", 0, 0.6, True, 8), sfx("reverse_swell", 0.6, 0.6)])
scene("bg4_main_room",
      "Vậy mẹ tôi đã đi đâu?",
      [L("props/DC1b_bowl_chopsticks_vertical", **BOWL_EMPTY_SEAT), L("boy_hoodie/M4_sit_stool_look_back_fear", **BOY_SEAT),
       L("hungry_ghost/A4_back_look_over_shoulder", 0.4, 0.95, h=0.52, start=0.55)],
      cam((0, 1.4, 0.66, 0.6), (1, 1.4, 0.5, 0.6, "smooth"), handheld=3),
      [sfx("whisper_eerie", 0.5, 0.6)], min_duration=4.5, bg_dim=0.2)
scene("black", duration=4.0, fade_in=0.5,
      sounds=[sfx("slipper_drag", 0.1, 0.5, length=3.5, fade_out=1.5), sfx("spoon_bowl_tap", 0.6, 0.35)])

story["scenes"] = S
# nhạc nền: chỉ drone_low (chưa có nhạc buồn / nhạc căng) — cố ý cắt ở khoảnh khắc im lặng
story["music"] = [
    {"sound": "drone_low", "from": 1, "to": a_open_end - 1, "volume": 0.6, "fade_in": 2.5, "fade_out": 1.5},
    {"sound": "drone_low", "from": a_steps, "to": a_call + 1, "volume": 0.45, "fade_in": 3, "fade_out": 0.05},
    {"sound": "drone_low", "from": a_esc, "to": a_esc_end, "volume": 0.6, "fade_in": 3, "fade_out": 2},
    {"sound": "drone_low", "from": a_rit + 3, "to": a_rit_end, "volume": 0.6, "fade_in": 1.5, "fade_out": 1.5},
    {"sound": "drone_low", "from": a_49, "to": a_49_end - 3, "volume": 0.75, "fade_in": 3, "fade_out": 0.05},
    {"sound": "drone_low", "from": a_end + 5, "to": len(S), "volume": 0.6, "fade_in": 2, "fade_out": 2},
]
story["parts"] = {"_note": "Điểm cắt cho video ngắn (render --scenes a-b)",
                  "phan_1": [1, a_call_end], "phan_2": [a_call_end + 1, a_49_end], "phan_3": [a_end, len(S)]}
out = ROOT / "scripts/bat_com_thu_hai.json"
out.write_text(json.dumps(story, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(S), "cảnh")
