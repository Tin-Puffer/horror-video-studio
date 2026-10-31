"""Sinh scripts/tieng_goi_thu_ba.json từ mẫu templates/kich_ban_mau.json.
Chạy: python3 scripts/gen_tieng_goi_thu_ba.py  (sửa lời/cảnh ở đây rồi chạy lại).
Truyện gốc + dàn ý đã duyệt: scripts/kich_ban_tieng_goi_thu_ba.md"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
story = json.loads((ROOT / "templates/kich_ban_mau.json").read_text(encoding="utf-8"))
story["title"] = "Tiếng gọi thứ ba"
story["output"] = "build/tieng_goi_thu_ba.mp4"
story["logline"] = ("Bà dặn Khoa: nửa đêm ai gọi tên thì đừng thưa, người thật gọi ba lần, ma chỉ gọi được hai. "
                    "Rồi thứ ngoài cổng học được cách gọi lần thứ ba, và người nằm cạnh Khoa mỗi đêm chưa chắc đã là bà.")
story["settings"]["audio"]["narration_volume"] = 1.4   # góp ý 3: giọng kể nổi hơn nền
story["settings"]["audio"]["duck"] = 0.28
story["characters"] = {
    "boy_hoodie": {"h": 0.46, "y": 0.96, "tint": True, "glow": False, "breathe": 0.008},
    "grandma": {"h": 0.5, "breathe": 0.006},
    "props": {"h": 0.3, "breathe": 0},
    "cat_tabby": {"h": 0.13, "breathe": 0.01},
    "ba_sau": {"h": 0.5, "breathe": 0.006},
}

# ============================================================ YÊU CẦU ASSET
FAKE_NOTE = ("IMPORTANT for this whole sheet: this is the SAME grandmother but subtly wrong, as if she drowned: "
             "her back is perfectly straight (NOT hunched), skin pale bluish-gray (not white), clothes soaked dark "
             "and clinging, gray hair loose from the bun and hanging in wet strands, a calm gentle smile, eyes "
             "small and dull without any shine.")
FAKE = "the drowned grandmother"
BOY_REFS = ["assets/source/boy_hoodie_base.png"]
# ảnh gốc của bà / đạo cụ (assets/source) không lên git → đính kèm sprite đã cắt làm tham chiếu
GMA_REFS = ["assets/characters/grandma/00_stand_front.png", "assets/characters/grandma/D1_walk_1.png"]
BOY = "the boy Khoa (messy spiky black hair, dark moss-green hoodie, charcoal pants)"
BED_TXT = "lying on a simple low wooden bed with a dark blue blanket"

story["asset_requests"] = [
    {"id": "grandma_sheet_F", "kind": "sheet", "character": "grandma", "grid": [2, 3],
     "why": "bà thật: ngồi hiên nhìn bến, xoa dầu cho Khoa, ho, dạy ám hiệu, mang hình nhân, ôm Khoa trong bóng tối",
     "note": "Where the boy appears he is the boy from the extra reference image.", "refs": GMA_REFS + BOY_REFS,
     "sprites": [
         {"name": "F1_sit_porch_gaze", "pose": "sitting on a tiny low bamboo stool, side view facing right, hunched, "
          "hands resting on her knees, gazing far away with a sad longing face",
          "desc": "Ngồi ghế tre thấp, nhìn xa xăm về phía phải (bến sông), buồn", "tags": ["ngồi", "hiên", "nhìn xa"],
          "facing": "right"},
         {"name": "F2_bed_rub_oil_boy", "pose": f"TWO characters together: {BOY} {BED_TXT}, the grandmother sitting on "
          "the bed edge leaning over him, rubbing medicated oil on his forehead with one hand, a small green oil "
          "bottle in the other hand, tender caring face",
          "desc": "HAI nhân vật + giường: bà ngồi mép giường xoa dầu gió lên trán Khoa đang nằm",
          "tags": ["giường", "dặn dò", "dầu gió"], "facing": "left"},
         {"name": "F3_cough_hunched", "pose": "standing very hunched, one hand covering her mouth while coughing hard, "
          "the other hand on her lower back, eyes squeezed shut, side view facing right",
          "desc": "Đứng còng, tay che miệng ho khù khụ, tay kia chống lưng", "tags": ["ho", "còng"], "facing": "right"},
         {"name": "F4_sit_stool_three_fingers", "pose": "sitting on a low wooden stool, leaning forward, holding up "
          "three fingers of one hand, very serious stern face, whispering, side view facing right",
          "desc": "Ngồi ghế đẩu, giơ ba ngón tay, nghiêm mặt dặn ám hiệu", "tags": ["ám hiệu", "dặn dò"],
          "facing": "right"},
         {"name": "F5_hold_effigy_back", "pose": "seen from behind, walking away, hugging a paper effigy doll dressed "
          "in a small moss-green hoodie and a bundle of red-gold joss paper against her chest",
          "desc": "Quay lưng, ôm hình nhân giấy mặc áo hoodie và xấp vàng mã", "tags": ["hình nhân", "quay lưng"],
          "facing": "away"},
         {"name": "F6_hug_boy_bed_dark", "pose": f"TWO characters together: {BOY} and the grandmother sitting up on a "
          "low wooden bed under a dark blue blanket, she hugs him tightly, both trembling and wide-eyed with fear, "
          "she whispers into his ear",
          "desc": "HAI nhân vật + giường: bà ôm chặt Khoa, cả hai run sợ, bà thì thầm",
          "tags": ["giường", "ôm", "sợ"], "facing": "right"},
     ]},
    {"id": "grandma_sheet_G", "kind": "sheet", "character": "grandma", "grid": [2, 3],
     "why": "bà giả: đi thẳng lưng (chu kỳ fake_walk), ngồi ướt sũng dưới hiên, đứng cười trong bóng tối",
     "note": FAKE_NOTE, "refs": GMA_REFS,
     "cycles": {"fake_walk": ["G1_fake_walk_1", "G2_fake_walk_2", "G3_fake_walk_3", "G4_fake_walk_4"]},
     "sprites": [
         {"name": "G1_fake_walk_1", "pose": "walking cycle frame 1 of 4, side view facing right, CONTACT: "
          "left heel touching the ground far forward, right leg far back, arms hanging still, upright posture",
          "desc": "Bà giả đi thẳng lưng, khung 1/4 (chạm)", "tags": ["bà giả", "đi"], "facing": "right"},
         {"name": "G2_fake_walk_2", "pose": "walking cycle frame 2 of 4, side view facing right, DOWN: "
          "left foot flat, right knee bent lifting the foot, body slightly lower",
          "desc": "Bà giả đi thẳng lưng, khung 2/4 (hạ)", "tags": ["bà giả", "đi"], "facing": "right"},
         {"name": "G3_fake_walk_3", "pose": "walking cycle frame 3 of 4, side view facing right, CONTACT: "
          "right heel touching the ground far forward, left leg far back (mirror of frame 1)",
          "desc": "Bà giả đi thẳng lưng, khung 3/4 (chạm chân kia)", "tags": ["bà giả", "đi"], "facing": "right"},
         {"name": "G4_fake_walk_4", "pose": "walking cycle frame 4 of 4, side view facing right, DOWN: "
          "right foot flat, left knee bent lifting the foot, body slightly lower",
          "desc": "Bà giả đi thẳng lưng, khung 4/4 (hạ chân kia)", "tags": ["bà giả", "đi"], "facing": "right"},
         {"name": "G5_sit_porch_wet_smile", "pose": "sitting flat on the ground with legs folded to one "
          "side, completely soaked, water dripping from hair and sleeves, looking up with a warm gentle smile, "
          "front view",
          "desc": "Bà giả ngồi bệt ướt sũng, nước nhỏ tong tỏng, ngẩng lên cười hiền", "tags": ["bà giả", "ướt", "cười"],
          "facing": "front"},
         {"name": "G6_stand_dark_smile", "pose": "standing perfectly straight and still, hands folded in "
          "front, face half in shadow, a calm smile that is a little too wide, front view",
          "desc": "Bà giả đứng thẳng im lìm, nửa mặt trong bóng tối, cười hơi quá rộng", "tags": ["bà giả", "rợn"],
          "facing": "front"},
     ]},
    {"id": "grandma_sheet_H", "kind": "sheet", "character": "grandma", "grid": [2, 3],
     "why": "bà giả: nằm cạnh giữ cổ tay Khoa, xoa đầu Khoa, ngồi quay lưng, gắp thức ăn, cận tay, cận mặt",
     "note": FAKE_NOTE + " Where the boy appears he is the boy from the extra reference image.", "refs": GMA_REFS + BOY_REFS,
     "sprites": [
         {"name": "H1_bed_hold_wrist_whisper", "pose": f"TWO characters together: {BOY} {BED_TXT}, lying on his back "
          f"with terrified wide-open eyes; beside him the drowned grandmother, lying on her side, her pale wrinkled hand gripping "
          "his wrist, her lips at his ear whispering",
          "desc": "HAI nhân vật + giường: bà giả nằm nghiêng siết cổ tay Khoa, ghé tai thì thầm; Khoa mở trừng mắt",
          "tags": ["bà giả", "giường", "thì thầm"], "facing": "right"},
         {"name": "H2_bed_edge_stroke_head", "pose": f"TWO characters together: {BOY} {BED_TXT}, eyes open, uneasy; "
          "the drowned grandmother sitting on the bed edge stroking his hair with a pale hand, smiling gently",
          "desc": "HAI nhân vật + giường: bà giả ngồi mép giường xoa đầu Khoa, cười hiền",
          "tags": ["bà giả", "giường", "dặn dò"], "facing": "left"},
         {"name": "H3_sit_back_turned", "pose": "sitting on a tiny low bamboo stool seen completely from "
          "behind, very straight back, wet hair strands hanging down her back, motionless",
          "desc": "Bà giả ngồi ghế tre quay lưng, thẳng đơ, tóc ướt bết", "tags": ["bà giả", "quay lưng"],
          "facing": "away"},
         {"name": "H4_sit_offer_food", "pose": "sitting on a low wooden stool, side view facing left, "
          "holding a rice bowl in one hand and reaching out chopsticks with food toward someone, not eating, "
          "staring with a fixed smile",
          "desc": "Bà giả ngồi ghế đẩu gắp thức ăn đưa sang trái, không ăn, nhìn chằm chằm cười",
          "tags": ["bà giả", "bữa cơm"], "facing": "left"},
         {"name": "H5_closeup_hand_wrist", "pose": "close-up filling the frame: an old pale bluish-gray wrinkled hand, "
          "skin pruned like it has been in water for days, fingers tightly gripping a child's wrist in a "
          "moss-green hoodie sleeve, water drops on the skin",
          "desc": "Cận bàn tay nhăn nheo trắng bệch như ngâm nước siết cổ tay Khoa (tay áo xanh rêu)",
          "tags": ["cận", "tay", "bà giả"], "facing": "right"},
         {"name": "H6_closeup_face_smile", "pose": f"close-up head and shoulders of the drowned grandmother, front view, smiling "
          "very gently, dull black-dotted eyes, a drop of water falling from her chin",
          "desc": "Cận mặt bà giả cười rất hiền, tóc ướt, giọt nước nhỏ từ cằm (cú hù cuối)",
          "tags": ["cận", "bà giả", "hù"], "facing": "front"},
     ]},
    {"id": "props_sheet_HN", "kind": "sheet", "character": "props", "grid": [2, 3],
     "why": "hình nhân, chiếc guốc của cô em út, chiếc dép của bà, dấu chân bùn, lọ dầu gió",
     "refs": ["assets/characters/props/DC6_mother_slippers.png", "assets/characters/props/DC1_bowl_chopsticks_upright.png"],
     "sprites": [
         {"name": "HN1_paper_effigy_hoodie", "pose": "a paper effigy doll of a boy sitting upright, body of folded "
          "paper and bamboo sticks, simple ink-painted face with dot eyes, wearing a small real moss-green hoodie, "
          "a lock of black hair tied with red thread pinned on its chest",
          "desc": "Hình nhân giấy ngồi, mặc áo hoodie xanh rêu của Khoa, lọn tóc buộc chỉ đỏ trước ngực",
          "tags": ["hình nhân", "thế mạng"], "facing": "front"},
         {"name": "HN2_wooden_clog_upside_down", "pose": "a single old Vietnamese wooden clog (guoc moc) lying upside "
          "down on a wet stone step, a little water around it",
          "desc": "Một chiếc guốc mộc nằm úp sấp trên bậc đá ướt", "tags": ["guốc", "bến sông"], "facing": "front"},
         {"name": "HN3_sandal_upside_down_puddle", "pose": "a single black plastic sandal lying upside down in a small "
          "dark puddle of water, thick black river mud on the heel",
          "desc": "Một chiếc dép nhựa đen của bà úp sấp trong vũng nước, bùn sông bám gót", "tags": ["dép", "vũng nước"],
          "facing": "front"},
         {"name": "HN4_muddy_footprints_trail", "pose": "a trail of six wet muddy bare footprints on the ground seen "
          "at a low angle, going away into the distance and getting smaller, wet dark mud",
          "desc": "Dãy dấu chân trần bùn ướt đi xa dần (nằm trên nền)", "tags": ["dấu chân", "bùn"], "facing": "front"},
         {"name": "HN5_single_wet_footprint", "pose": "one single wet muddy bare footprint on the ground, seen at a "
          "low angle, glistening water",
          "desc": "Một dấu chân trần bùn ướt đơn lẻ (dùng để hiện dần từng dấu)", "tags": ["dấu chân", "bùn"],
          "facing": "front"},
         {"name": "HN6_wind_oil_bottle", "pose": "a tiny old glass bottle of green Vietnamese medicated oil (dau gio) "
          "with a screw cap, covered with a thin layer of dust, standing upright",
          "desc": "Lọ dầu gió xanh nhỏ, nắp vặn chặt, phủ bụi mỏng", "tags": ["dầu gió", "bụi"], "facing": "front"},
     ]},
    {"id": "bg10_river_wharf", "kind": "background",
     "scene": "A small-town river wharf at night: wide worn stone steps going down into black still river water on "
              "the left and center, thin mist over the water, a clump of bamboo on the right edge, a far opposite "
              "bank with one tiny lamp, empty flat stone landing in the lower third for characters.",
     "desc": "Bến sông thị trấn ban đêm: bậc đá xuống mặt nước đen, sương mỏng, bụi tre bên phải, bờ xa có một đốm đèn",
     "tags": ["bến sông", "đêm", "nước"], "floor_y": 0.95, "char_h": 0.46,
     "hotspots_needed": ["steps", "water_edge", "far_lamp", "landing"]},
    {"id": "bg11_peephole_yard", "kind": "background",
     "scene": "Point of view through a door peephole: a round fisheye lens circle in the middle of a pure black "
              "frame, inside the circle a distorted moonlit concrete front yard of a Vietnamese tube house, a "
              "rusty folding iron gate in the distance, empty, no people.",
     "desc": "Nhìn qua mắt mèo cửa chính: khung tròn giữa nền đen, sân xi măng ánh trăng bị bóp méo, cổng sắt xa",
     "tags": ["mắt mèo", "sân", "POV"], "floor_y": 0.7, "char_h": 0.3,
     "hotspots_needed": ["lens_circle", "yard_floor", "gate"]},
    {"id": "cough_old", "kind": "sound", "sound_kind": "sfx", "length": "~3s", "volume": 1.0,
     "desc": "Bà già ho khù khụ, khô, ba tràng", "tags": ["ho", "bà"],
     "prompt": "An elderly woman coughing, dry hacking cough in three bursts, indoors, close",
     "search": "old woman cough"},
    {"id": "frogs_night", "kind": "sound", "sound_kind": "sfx", "length": "~20s", "volume": 1.0,
     "desc": "Ếch nhái kêu ran ven sông ban đêm (lặp được)", "tags": ["ếch", "đêm"],
     "prompt": "Chorus of frogs and toads croaking near a river at night, steady ambience, seamless loop",
     "search": "frogs night ambience"},
    {"id": "rooster_crow", "kind": "sound", "sound_kind": "sfx", "length": "~4s", "volume": 1.0,
     "desc": "Một tiếng gà gáy xa lúc rạng sáng", "tags": ["gà gáy", "sáng"],
     "prompt": "A single rooster crowing far away at dawn in a quiet village",
     "search": "rooster crow distant"},
    {"id": "motorbike_stop", "kind": "sound", "sound_kind": "sfx", "length": "~5s", "volume": 1.0,
     "desc": "Xe máy chạy tới dừng lại rồi tắt máy, trời mưa", "tags": ["xe máy"],
     "prompt": "A small motorbike approaching, slowing down and stopping, engine idles then turns off, light rain",
     "search": "motorbike arrive stop engine off"},
    {"id": "gate_knock_metal", "kind": "sound", "sound_kind": "sfx", "length": "~3s", "volume": 1.0,
     "desc": "Ba tiếng gõ chậm lên cổng sắt gỉ", "tags": ["gõ", "cổng sắt"],
     "prompt": "Three slow knocks on a rusty iron gate, metallic hollow clang, night silence",
     "search": "knock metal gate"},
    {"id": "knock_2_hesitant", "kind": "sound", "sound_kind": "sfx", "length": "~3s", "volume": 1.0,
     "desc": "Hai tiếng gõ cửa gỗ ngập ngừng, rồi im", "tags": ["gõ cửa"],
     "prompt": "Two slow hesitant knocks on a wooden door, a long pause between them, then silence",
     "search": "two knocks wooden door"},
    {"id": "water_drip", "kind": "sound", "sound_kind": "sfx", "length": "~10s", "volume": 1.0,
     "desc": "Nước nhỏ tong tỏng xuống nền gạch (lặp được)", "tags": ["nước", "nhỏ giọt"],
     "prompt": "Slow water drips from soaked clothes falling onto a tile floor, quiet room, seamless loop",
     "search": "water dripping floor"},
    {"id": "river_lapping", "kind": "sound", "sound_kind": "sfx", "length": "~20s", "volume": 1.0,
     "desc": "Nước sông vỗ nhẹ vào bậc đá ban đêm (lặp được)", "tags": ["sông", "nước"],
     "prompt": "Calm dark river water gently lapping against stone steps at night, seamless loop",
     "search": "river water lapping stone"},
    {"id": "cat_hiss", "kind": "sound", "sound_kind": "sfx", "length": "~2s", "volume": 1.0,
     "desc": "Mèo xù lông rít lên rồi chạy mất", "tags": ["mèo"],
     "prompt": "A cat hissing angrily then running away quickly",
     "search": "cat hiss"},
    {"id": "scissors_hair", "kind": "sound", "sound_kind": "sfx", "length": "~1.5s", "volume": 1.0,
     "desc": "Kéo cắt một lọn tóc", "tags": ["kéo", "tóc"],
     "prompt": "Old metal scissors cutting a lock of hair, two crisp snips, close",
     "search": "scissors cutting hair"},
]

# ---------- lượt 2: theo góp ý (scripts/gop_y_tieng_goi_thu_ba.md, mục 5–12)
ALTAR = ("Close-up of a small Vietnamese family altar at night, same composition as the attached altar image: a framed "
         "black-and-white portrait photo in the middle showing an old Vietnamese GRANDFATHER (thin face, short gray "
         "hair, old collared shirt, kind serious look), no black mourning ribbon, a brass incense bowl on the left, two "
         "red candles, a small fruit plate on the right, an empty wooden surface in the front for props.")
story["asset_requests"] += [
    {"id": "bg5b_altar_grandpa_lit", "kind": "background", "refs": ["assets/backgrounds/bg5_altar_close.png"],
     "why": "cảnh 26: bà thật thắp hương (mục 5)",
     "scene": ALTAR + " Three incense sticks are burning with thin curling smoke, the two candles are lit with a warm glow.",
     "desc": "Cận bàn thờ ÔNG nội ban đêm: ảnh thờ ông, bát hương có 3 nén nhang đang cháy khói, 2 nến sáng",
     "tags": ["bàn thờ", "ông", "nhang cháy"], "floor_y": 0.8, "char_h": 0.6,
     "hotspots_needed": ["portrait", "incense_bowl", "offering_spot"]},
    {"id": "bg5c_altar_grandpa_cold", "kind": "background", "refs": ["assets/backgrounds/bg5_altar_close.png"],
     "why": "cảnh 76: bà giả không thắp hương nữa (mục 9) — đính kèm thêm ảnh bg5b vừa tạo để giữ đúng bố cục",
     "scene": ALTAR + " Everything is the SAME as the lit version but abandoned: NO smoke, only short burnt-out incense "
              "stubs sticking up in cold gray ash, both candles are out with no flame, a thin layer of dust, colder "
              "and darker mood.",
     "desc": "Cùng bố cục bg5b nhưng nguội lạnh: chỉ còn chân nhang trơ trọi, không khói, nến tắt, bụi",
     "tags": ["bàn thờ", "ông", "nguội lạnh"], "floor_y": 0.8, "char_h": 0.6,
     "hotspots_needed": ["portrait", "incense_bowl", "offering_spot"]},
    {"id": "bg7d_front_yard_morning", "kind": "background", "refs": ["assets/backgrounds/bg7_front_yard.png"],
     "why": "cảnh 82–84 (bà Sáu), 95–96 (sáng mở cổng) (mục 12)",
     "scene": "IMPORTANT: this is a DAYTIME image, ignore the night lighting described above; the yard itself stays "
              "empty, only tiny far-away figures on the street outside the gate. The SAME front yard as "
              "the attached image (potted plant and small outdoor offering table on the left, rusty folding iron "
              "gate on the right half, cracked concrete floor) but in the early morning: soft pale sunlight, light "
              "blue sky, long soft shadows, the gate half open, outside on the street small far-away people: a woman "
              "riding a bicycle and a man walking, a tiny street food stall with steam. Empty concrete yard in the "
              "lower third.",
     "desc": "Sân trước buổi sáng sớm (cùng bố cục bg7): nắng nhạt, cổng mở hé, ngoài đường có người đạp xe, người đi bộ, hàng quán",
     "tags": ["sân", "buổi sáng", "cổng"], "floor_y": 0.95, "char_h": 0.46,
     "hotspots_needed": ["gate_gap", "gate_gap_floor", "gate_left", "open_floor"]},
    {"id": "bg12_bedside_drawer", "kind": "background", "refs": ["assets/backgrounds/bg1_bedroom.png"],
     "why": "cảnh 81: lọ dầu gió trong ngăn kéo tủ đầu giường (mục 11)",
     "scene": "Close-up of the old wooden bedside cabinet from the attached bedroom, seen from slightly above, its top "
              "drawer pulled half open; inside the drawer an old folded handkerchief, a wooden comb and a string of "
              "brown prayer beads, with an EMPTY clear spot in the middle of the drawer for a small bottle; a little "
              "dust, cold moonlight from the side.",
     "desc": "Cận tủ đầu giường gỗ, ngăn kéo mở: khăn tay, lược gỗ, tràng hạt của bà, chừa chỗ trống giữa ngăn đặt lọ dầu",
     "tags": ["ngăn kéo", "tủ đầu giường", "cận"], "floor_y": 0.8, "char_h": 0.3,
     "hotspots_needed": ["drawer_spot"]},
    {"id": "grandma_sheet_I", "kind": "sheet", "character": "grandma", "grid": [1, 2],
     "why": "cảnh 26: bà thắp nhang nhìn từ sau (mục 5); cảnh 77: bà giả nhìn con mèo (mục 10)",
     "refs": GMA_REFS,
     "sprites": [
         {"name": "I1_back_incense_closeup", "pose": "close-up seen from BEHIND, from the shoulders up (head, bun and "
          "shoulders filling the frame), both hands raised in front of her face holding three lit incense sticks with "
          "thin smoke rising above her head, head slightly bowed in prayer",
          "desc": "Cận từ sau lưng, từ vai trở lên, hai tay giơ ba nén nhang khói bay (tiền cảnh trước bàn thờ)",
          "tags": ["thắp nhang", "quay lưng", "cận"], "facing": "away"},
         {"name": "I2_fake_look_down_side", "pose": "the drowned version of the grandmother (back perfectly straight, "
          "pale bluish-gray skin, soaked dark clothes, loose wet gray hair), standing side view facing right, head "
          "tilted down looking at something small on the ground, a fixed calm smile",
          "desc": "Bà giả đứng nghiêng (quay phải), cúi nhìn xuống đất, cười đơ (nhìn con mèo)",
          "tags": ["bà giả", "nhìn xuống"], "facing": "right"},
     ]},
    {"id": "props_sheet_HP", "kind": "sheet", "character": "props", "grid": [1, 3],
     "why": "dấu chân bùn đi VÀO nhà (mục 6, 7): cảnh 29, 30, 35, 60, 83, 84",
     "refs": ["assets/characters/props/HN5_single_wet_footprint.png", "assets/characters/props/HN4_muddy_footprints_trail.png"],
     "sprites": [
         {"name": "HP1_footprints_trail_toward", "pose": "a trail of six wet muddy bare footprints on the ground seen at "
          "a low angle, coming TOWARD the viewer: the toes of every footprint point DOWN toward the viewer, the far "
          "footprints at the top are small and the near ones at the bottom are big, alternating left and right foot",
          "desc": "Dãy dấu chân bùn ướt đi VỀ PHÍA người xem (mũi chân hướng xuống, xa nhỏ gần to, trái phải xen kẽ)",
          "tags": ["dấu chân", "bùn", "đi vào"], "facing": "front"},
         {"name": "HP2_footprint_left_toward", "pose": "one single wet muddy bare LEFT footprint on the ground seen at a "
          "low angle, toes pointing DOWN toward the viewer",
          "desc": "Một dấu chân TRÁI bùn ướt, mũi chân hướng về người xem", "tags": ["dấu chân", "trái"], "facing": "front"},
         {"name": "HP3_footprint_right_toward", "pose": "one single wet muddy bare RIGHT footprint on the ground seen at a "
          "low angle, toes pointing DOWN toward the viewer",
          "desc": "Một dấu chân PHẢI bùn ướt, mũi chân hướng về người xem", "tags": ["dấu chân", "phải"], "facing": "front"},
     ]},
    {"id": "cat_tabby_sheet_A", "kind": "sheet", "character": "cat_tabby", "grid": [2, 3],
     "why": "cảnh 77: mèo mướp thấy bà giả thì xù lông rít rồi bỏ chạy (mục 10)",
     "cycles": {"run": ["A3_run_1", "A4_run_2", "A5_run_3", "A6_run_4"]},
     "sprites": [
         {"name": "A1_stand_look", "pose": "standing on four legs, side view facing right, tail up, curious, looking ahead",
          "desc": "Đứng bốn chân nhìn tới (quay phải), đuôi dựng", "tags": ["mèo", "đứng"], "facing": "right"},
         {"name": "A2_arch_hiss", "pose": "arched back with all fur puffed up, tail bristled straight up, ears flat, mouth "
          "wide open hissing showing fangs, side view facing right",
          "desc": "Cong lưng xù lông, đuôi dựng, tai cụp, há miệng rít nhe nanh (quay phải)",
          "tags": ["mèo", "xù lông", "rít"], "facing": "right"},
         {"name": "A3_run_1", "pose": "running cycle frame 1 of 4, side view facing right: front legs stretched forward, "
          "back legs stretched back, body long", "desc": "Chạy, khung 1/4 (duỗi)", "tags": ["mèo", "chạy"], "facing": "right"},
         {"name": "A4_run_2", "pose": "running cycle frame 2 of 4, side view facing right: front paws landing, back legs "
          "coming forward", "desc": "Chạy, khung 2/4 (chạm trước)", "tags": ["mèo", "chạy"], "facing": "right"},
         {"name": "A5_run_3", "pose": "running cycle frame 3 of 4, side view facing right: all four legs gathered under "
          "the body, back curved", "desc": "Chạy, khung 3/4 (gom)", "tags": ["mèo", "chạy"], "facing": "right"},
         {"name": "A6_run_4", "pose": "running cycle frame 4 of 4, side view facing right: back legs pushing off, front "
          "legs reaching forward", "desc": "Chạy, khung 4/4 (đẩy)", "tags": ["mèo", "chạy"], "facing": "right"},
     ]},
    {"id": "grandma_sheet_J", "kind": "sheet", "character": "grandma", "grid": [1, 2],
     "why": "cảnh 61: bà ôm ĐÚNG con hình nhân của cảnh 56–58 (F5 vẽ con rối khác) ra bến sông",
     "note": "The paper effigy she carries must be EXACTLY the effigy in the extra reference image "
             "(HN1_paper_effigy_hoodie): a boy doll of folded paper and bamboo sticks, simple ink face, wearing a "
             "small moss-green hoodie, beige paper legs on bamboo sticks, a lock of black hair tied with red thread "
             "on its chest, about half her height.",
     "refs": GMA_REFS + ["assets/characters/props/HN1_paper_effigy_hoodie.png"],
     "sprites": [
         {"name": "J1_back_carry_effigy", "pose": "seen from behind, walking away, hugging the paper effigy against "
          "her chest so its head shows over her shoulder, a bundle of red-gold joss paper under the other arm, "
          "hunched as usual", "desc": "Quay lưng đi ra, ôm hình nhân (đầu hình nhân ló qua vai) và xấp vàng mã",
          "tags": ["hình nhân", "quay lưng", "ra bến sông"], "facing": "away"},
         {"name": "J2_side_carry_effigy", "pose": "side view facing right, walking slowly hunched, carrying the paper "
          "effigy in both arms in front of her like a sleeping child, joss paper bundle on top, sad determined face",
          "desc": "Nghiêng (quay phải), đi chậm, bế hình nhân trước ngực như bế đứa trẻ, xấp vàng mã bên trên",
          "tags": ["hình nhân", "đi", "ra bến sông"], "facing": "right"},
     ]},
    {"id": "ba_sau_sheet_A", "kind": "sheet", "character": "ba_sau", "grid": [1, 3],
     "why": "cảnh 82–84: bà Sáu bán xôi kéo Khoa lại kể chuyện dấu chân (mục 12)",
     "sprites": [
         {"name": "A1_stand_basket", "pose": "standing, front view, basket of sticky rice on one arm, friendly face",
          "desc": "Đứng chính diện, khoác thúng xôi, mặt hiền", "tags": ["bà Sáu", "đứng"], "facing": "front"},
         {"name": "A2_lean_whisper", "pose": "leaning forward, side view facing left, one hand cupped beside her mouth "
          "whispering, the other hand reaching out as if pulling someone closer, worried face",
          "desc": "Nghiêng người (quay trái), che miệng nói nhỏ, tay kia kéo người lại gần, mặt lo lắng",
          "tags": ["bà Sáu", "thì thầm"], "facing": "left"},
         {"name": "A3_point_far", "pose": "side view facing right, arm stretched out pointing far into the distance, "
          "frightened uneasy face", "desc": "Quay phải, duỗi tay chỉ ra xa (về phía bến sông), mặt sợ hãi",
          "tags": ["bà Sáu", "chỉ tay"], "facing": "right"},
     ]},
]

S = []  # scenes


def cam(*keys, handheld=None):
    c = {"keys": [dict(zip(("p", "zoom", "x", "y", "ease"), k)) for k in keys]}
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


def walk(char, x, fps=2.5, end=None, cyc="walk", **kw):
    d = {"cycle": f"{char}/{cyc}", "fps": fps, "x": x, "y": "floor", "face": "auto", "breathe": 0, **kw}
    if end:
        d["end"] = end
    return d


# Chỗ ngồi đo trên BG4 (dùng lại từ Bát cơm thứ hai)
BOY_SEAT = dict(x=0.59, y=0.83, h=0.46)
GMA_SEAT = dict(x=0.85, y=0.81, h=0.55)
BED = dict(x=0.7, y=0.95, h=0.54)            # sprite giường đôi (bà + Khoa) trên bg1_bedroom
FAKE_SEAT = dict(x=0.86, y=0.82, h=0.46)     # bà giả ngồi ghế đẩu phải, ngang tỉ lệ Khoa (góp ý 8)


def trail(p0, p1, n=6, spread=0.045, start=None, **kw):
    """Dãy dấu chân bùn đi VỀ PHÍA người xem: p = (x, y, h) dấu xa → dấu gần, trái/phải xen kẽ (góp ý 6–7).
    start = (s0, s1): các dấu hiện dần lần lượt."""
    out = []
    for i in range(n):
        t = i / max(1, n - 1)
        x, y, h = (a + (b - a) * t for a, b in zip(p0, p1))
        foot = "HP2_footprint_left_toward" if i % 2 == 0 else "HP3_footprint_right_toward"
        # người đi VỀ PHÍA người xem: chân trái của họ nằm bên PHẢI khung hình
        layer = L(f"props/{foot}", x + (spread if i % 2 == 0 else -spread) * h / p1[2], y, h=h, **kw)
        if start:
            layer["start"] = start[0] + (start[1] - start[0]) * t
        out.append(layer)
    return out


YARD_TRAIL = ((0.69, 0.68, 0.045), (0.63, 0.99, 0.16))   # gần như thẳng xuống, khớp mũi chân   # từ khe cổng (gate_gap_floor) về phía cửa nhà
FIRE = {"cycle": "props/fire", "fps": 6, "x": 0.56, "y": 0.96, "h": 0.32, "tint": False, "breathe": 0}

FROGS = lambda n=12, v=0.45: sfx("frogs_night", 0, v, True, n)
INSECTS = lambda n=12, v=0.4: sfx("night_insects", 0, v, True, n)
RAIN = lambda n=12, v=0.55: sfx("rain_roof", 0, v, True, n)
RIVER = lambda n=12, v=0.5: sfx("river_lapping", 0, v, True, n)
CLOCK = lambda n=10, v=0.3: sfx("clock_tick", 0, v, True, n)


def day(layer):
    return {**layer, "tint": False}


# ============================================================ 1. MỞ ĐẦU (móc câu)
a_open = scene("bg1_bedroom",
               "Đêm qua, bà gọi tên tôi ba lần từ ngoài cổng, đúng ba lần, rồi gõ lên cánh cổng sắt ba tiếng, "
               "y hệt như ám hiệu mà bà đã dạy tôi.",
               [L("boy_hoodie/G2_bed_wake_startled", 0.7, 0.95, h=0.54)],
               cam((0, 1.15, 0.6, 0.6), (1, 1.4, 0.68, 0.62, "in"), handheld=3),
               [FROGS(12, 0.35), sfx("gate_knock_metal", 0.62, 1.0)], fade_in=1.5)
scene("bg1_bedroom",
      "Tôi suýt bật dậy chạy ra mở cổng, nhưng một bàn tay lạnh ngắt đã giữ chặt cổ tay tôi lại, bởi vì bà đang nằm ngay bên cạnh tôi.",
      [L("grandma/H1_bed_hold_wrist_whisper", **BED)],
      cam((0, 1.3, 0.68, 0.62), (1, 1.8, 0.7, 0.66, "in"), handheld=4),
      [sfx("heartbeat", 0, 0.7, True, 10), sfx("breath_close", 0.55, 0.6)])
scene("bg1_bedroom", duration=2.6, fade_in=0, bg_dim=0.35,
      layers=[L("grandma/H5_closeup_hand_wrist", 0.5, 1.02, h=[0.9, 1.0], tint=False)],
      sounds=[sfx("water_drip", 0, 0.6, True, 2.6), sfx("reverse_swell", 0.1, 0.5)])
scene("bg1_bedroom",
      "Tôi tên là Khoa, và đêm qua tôi đã không đáp lại lời bà gọi. Để các bạn hiểu vì sao đến giờ tôi vẫn không biết mình đã làm đúng hay sai, tôi phải kể lại từ đầu.",
      [L("boy_hoodie/G3_bed_blanket_chin_scared", 0.7, 0.95, h=0.5, jitter=1)],
      cam((0, 1.2, 0.62, 0.6), (1, 1.3, 0.65, 0.6)),
      [FROGS(12, 0.3), CLOCK(12, 0.25)])
scene("black", duration=4.0, fade_in=0.6, fade_out=1.0, title_text="TIẾNG GỌI THỨ BA",
      sounds=[sfx("gate_knock_metal", 0.4, 0.7)])
a_open_end = len(S)

# ============================================================ 2. VỀ Ở VỚI BÀ
a_home = scene("bg7_front_yard",
               "Năm tôi mười ba tuổi, bố mẹ vào Sài Gòn làm ăn, gửi tôi về ở với bà nội trong căn nhà ống cuối thị trấn, "
               "cách bến sông chưa đầy trăm bước chân.",
               [walk("boy_hoodie", [1.1, 0.45], fps=3.5, end=0.7), L("boy_hoodie/B1_stand_worried", 0.45, start=0.7)],
               cam((0, 1.2, 0.6, 0.6), (1, 1.2, 0.45, 0.6, "smooth")),
               [INSECTS(12, 0.4), sfx("footsteps_slow", 0.1, 0.5, True, 6), sfx("gate_rattle", 0.02, 0.5)], fade_in=1.2)
scene("bg2_hallway",
      "Căn nhà hẹp và sâu, quanh năm ẩm mùi rêu, tường loang những vệt nước như ai vẽ bản đồ, và đêm nào gió từ sông cũng lùa qua khe cửa, mang theo một luồng hơi lạnh tanh mùi nước sông.",
      [walk("boy_hoodie", [0.12, 0.55], fps=3.5, end=0.85), L("boy_hoodie/B3_look_back_over_shoulder", 0.55, start=0.85)],
      cam((0, 1.2, 0.3, 0.6), (1, 1.2, 0.55, 0.6, "smooth")),
      [sfx("footsteps_slow", 0.05, 0.5, True, 8), sfx("floor_creak", 0.7, 0.5)])
scene("bg4_main_room",
      "Bà tôi đau lưng đã nhiều năm, đi đâu cũng còng xuống, một tay chống ngang hông, bước từng bước chậm rãi trên nền gạch.",
      [walk("grandma", [0.92, 0.45], fps=2.5, end=0.9, bob=2), L("grandma/00_stand_front", 0.45, start=0.9)],
      cam((0, 1.2, 0.6, 0.6), (1, 1.2, 0.45, 0.6, "smooth")),
      [sfx("slipper_drag", 0, 0.5, True, 9), INSECTS(10, 0.3)])
a_cough = scene("bg6_kitchen",
                "Cứ chập tối là bà lại ho, những tràng ho khù khụ vang khắp căn nhà hẹp, nghe như có gì đó mắc nghẹn mãi trong lồng ngực bà.",
                [L("grandma/F3_cough_hunched", 0.55, face="right")],
                cam((0, 1.2, 0.5, 0.6), (1, 1.35, 0.55, 0.58)),
                [sfx("cough_old", 0.15, 1.0), sfx("cough_old", 0.65, 0.8), INSECTS(10, 0.3)])
scene("bg7_front_yard",
      "Ông mất sớm, bà ở một mình đã lâu, và tối nào bà cũng kéo chiếc ghế tre ra hiên, ngồi lặng lẽ nhìn về phía bến sông cho đến khi trời tối hẳn.",
      [L("grandma/F1_sit_porch_gaze", 0.32, h=0.42)],
      cam((0, 1.3, 0.38, 0.62), (1, 1.45, 0.42, 0.58, "smooth")),
      [FROGS(12, 0.5), sfx("dog_howl", 0.75, 0.25)])
a_rule = scene("bg1_bedroom",
               "Tối đầu tiên, bà ngồi bên mép giường, vừa xoa dầu gió lên trán tôi, vừa dặn một điều mà bà bắt tôi phải thuộc như thuộc tên mình.",
               [L("grandma/F2_bed_rub_oil_boy", **BED)],
               cam((0, 1.2, 0.65, 0.6), (1, 1.4, 0.7, 0.62)),
               [FROGS(12, 0.3), CLOCK(12, 0.25)])
scene("bg1_bedroom",
      "Bà bảo nửa đêm nghe ai gọi tên thì tuyệt đối không được lên tiếng đáp lại, dù chỉ một tiếng dạ, vì người nhà thật bao giờ cũng gọi đủ ba lần, còn ma chỉ gọi được hai lần.",
      [L("grandma/F2_bed_rub_oil_boy", **BED)],
      cam((0, 1.4, 0.7, 0.62), (1, 1.8, 0.66, 0.55, "in")),
      [CLOCK(12, 0.3), sfx("whisper_eerie", 0.7, 0.25)])
scene("bg1_bedroom",
      "Gọi mà không ai đáp, thì nó sẽ tự bỏ đi. Tôi hỏi bà sao lại sợ đến thế, bà im lặng rất lâu, rồi kể cho tôi nghe chuyện của cô em út.",
      [L("grandma/F2_bed_rub_oil_boy", **BED)],
      cam((0, 1.6, 0.66, 0.55), (1, 1.6, 0.72, 0.6, "smooth")),
      [CLOCK(10, 0.3)], fade_out=0.8)
a_home_end = len(S)

# ============================================================ 3. CHUYỆN CÔ EM ÚT
a_aunt = scene("bg10_river_wharf",
               "Hồi bà còn con gái, hai chị em ngủ chung một giường. Một đêm tháng bảy, từ ngoài bến sông vọng vào tiếng mẹ gọi tên hai chị em.",
               camera=cam((0, 1.2, 0.4, 0.55), (1, 1.4, 0.45, 0.6, "smooth")),
               sounds=[RIVER(12, 0.55), FROGS(12, 0.3), sfx("whisper_eerie", 0.6, 0.45)], fade_in=1.5, bg_dim=0.15)
scene("bg1_bedroom",
      "Bà nghe thấy, nhưng bà sợ, nên nằm im trùm chăn kín đầu. Còn cô em út thì ngái ngủ, khẽ dạ một tiếng, rồi xỏ đôi guốc mộc đi ra ngoài.",
      [L("boy_hoodie/L5_peek_from_blanket", 0.7, h=0.36)],
      cam((0, 1.3, 0.7, 0.62), (1, 1.5, 0.7, 0.66)),
      [sfx("heartbeat", 0.2, 0.4, True, 8), sfx("footsteps_slow", 0.6, 0.4, length=3, fade_out=1.0)], bg_dim=0.3)
scene("bg10_river_wharf",
      "Sáng hôm sau, người ta chỉ thấy một chiếc guốc mộc nằm úp sấp trên bậc đá bến sông.",
      [L("props/HN2_wooden_clog_upside_down", 0.45, 0.9, h=0.14)],
      cam((0, 1.3, 0.45, 0.75), (1, 1.9, 0.45, 0.82, "in")),
      [RIVER(8, 0.6)], min_duration=4.0)
scene("bg10_river_wharf",
      "Ba ngày sau cái xác mới nổi lên, và những người vớt xác đều bảo, lúc kéo lên bờ, mặt cô ấy [0.6] vẫn còn đang cười.",
      camera=cam((0, 1.25, 0.35, 0.6), (1, 1.7, 0.3, 0.68, "in"), handheld=3),
      sounds=[RIVER(10, 0.5), sfx("reverse_swell", 0.65, 0.5)], bg_dim=0.2)
scene("bg1_bedroom",
      "Bà bảo cả đời bà vẫn tự hỏi, nếu đêm ấy người lên tiếng đáp lại là bà thì sao. Rồi bà quay đi chùi vội nước mắt, và tôi nghe tiếng bà ho vọng mãi dưới bếp.",
      [walk("grandma", [0.55, 0.13], fps=2.5, bob=2, end=0.8)],   # khuất ở cửa phòng (bedroom_door)
      cam((0, 1.2, 0.45, 0.6), (1, 1.2, 0.3, 0.6, "smooth")),
      [sfx("slipper_drag", 0, 0.4, True, 4, 0, 1), sfx("cough_old", 0.6, 0.45)], fade_out=1.3)
scene("bg1_bedroom",
      "Lúc ấy, tôi chỉ nghĩ đó là chuyện ngày xưa của người già.",
      [L("boy_hoodie/G1_bed_sleeping", 0.7, 0.95, h=0.5)],
      cam((0, 1.2, 0.68, 0.6), (1, 1.3, 0.7, 0.62)),
      [FROGS(6, 0.3)], fade_out=1.2)
a_aunt_end = len(S)

# ============================================================ 4. TIẾNG GỌI ĐẦU TIÊN
a_first = scene("bg1_bedroom",
                "Một tháng sau, lần đầu tiên tôi nghe thấy tiếng gọi.",
                [L("boy_hoodie/G1_bed_sleeping", 0.7, 0.95, h=0.5)],
                cam((0, 1.15, 0.6, 0.6), (1, 1.3, 0.68, 0.62, "in")),
                [FROGS(6, 0.4), CLOCK(6, 0.3)], fade_in=1.5, min_duration=3.5)
scene("bg7_front_yard",
      "Đã quá nửa đêm, cả thị trấn chìm trong tiếng ếch nhái, thì từ ngoài cổng vọng vào giọng mẹ tôi, gọi tên tôi hai lần, dịu dàng và mệt mỏi như vừa xuống xe khách.",
      camera=cam((0, 1.2, 0.6, 0.55), (1, 1.7, 0.69, 0.48, "in"), handheld=3),
      sounds=[FROGS(12, 0.55), sfx("whisper_eerie", 0.45, 0.5), sfx("whisper_eerie", 0.7, 0.45)])
scene("bg1_bedroom",
      "Chân tôi đã chạm xuống nền gạch lạnh thì chợt nhớ đến lời bà, và tôi ngồi im trong bóng tối, chờ tiếng gọi thứ ba.",
      [L("boy_hoodie/G2_bed_wake_startled", 0.7, 0.95, h=0.54, jitter=1)],
      cam((0, 1.3, 0.68, 0.6), (1, 1.6, 0.7, 0.62, "in"), handheld=3),
      [sfx("heartbeat", 0, 0.6, True, 10), CLOCK(10, 0.35)])
scene("bg1_bedroom", duration=3.5,
      layers=[L("boy_hoodie/G2_bed_wake_startled", 0.7, 0.95, h=0.54, jitter=1)],
      camera=cam((0, 1.6, 0.7, 0.62), (1, 1.8, 0.7, 0.6)),
      sounds=[CLOCK(3.5, 0.6)])
scene("bg1_bedroom",
      "Tiếng gọi thứ ba không bao giờ đến.",
      [L("boy_hoodie/G3_bed_blanket_chin_scared", 0.7, 0.95, h=0.5, jitter=1)],
      cam((0, 1.5, 0.7, 0.62), (1, 1.5, 0.7, 0.62)),
      [FROGS(5, 0.3)], min_duration=3.2)
scene("bg4d_main_room_day",
      "Sáng hôm sau, tôi gọi điện vào Sài Gòn, mẹ bảo đêm qua mẹ trực ca ở xưởng đến sáng, rồi còn hỏi sao giọng tôi run thế.",
      [day(L("boy_hoodie/F4_phone_call_scared", 0.35))],
      cam((0, 1.2, 0.35, 0.6), (1, 1.35, 0.35, 0.58)),
      [sfx("hangup_tone", 0.88, 0.4)], fade_in=1.0)
scene("bg5b_altar_grandpa_lit",
      "Tôi không dám kể với mẹ. Bà nghe tôi kể lại thì chẳng nói gì, chỉ lặng lẽ thắp thêm ba nén nhang trên bàn thờ, khấn rất lâu.",
      [L("grandma/I1_back_incense_closeup", 0.28, 1.12, h=0.8)],   # tiền cảnh, nhìn từ sau lưng
      cam((0, 1.2, 0.45, 0.5), (1, 1.35, 0.48, 0.45)),
      [sfx("ritual_bell", 0.1, 0.4), sfx("cough_old", 0.75, 0.3)])
a_first_end = len(S)

# ============================================================ 5. LEO THANG
a_esc = scene("bg7_front_yard",
              "Từ đó, đêm nào nó cũng gọi. Có đêm là giọng bố, trầm và khàn như mỗi lần bố say, có đêm là giọng thằng Tùng cùng lớp rủ tôi ra sông tắm đêm.",
              camera=cam((0, 1.2, 0.69, 0.5), (1, 1.4, 0.69, 0.45, "smooth"), handheld=2),
              sounds=[FROGS(12, 0.5), sfx("whisper_eerie", 0.2, 0.45), sfx("whisper_eerie", 0.6, 0.45)], fade_in=1.0)
scene("bg7_front_yard",
      "Và đêm sau bao giờ cũng gần hơn đêm trước, từ ngoài cổng vào đến giữa sân, rồi đến sát cánh cửa chính.",
      camera=cam((0, 1.3, 0.75, 0.5), (1, 1.6, 0.3, 0.7, "in"), handheld=3),
      sounds=[FROGS(10, 0.4), sfx("footsteps_slow", 0.2, 0.4, True, 5, 0.5, 1.0), sfx("heartbeat", 0.4, 0.5, True, 6)])
scene("bg7_front_yard",
      "Sáng nào ra sân tôi cũng thấy những dấu chân ướt in trên nền gạch, bùn đen và tanh mùi nước sông, đi thẳng từ cổng vào rồi dừng lại trước cửa.",
      [*trail(*YARD_TRAIL), L("boy_hoodie/B1_stand_worried", 0.22)],
      cam((0, 1.25, 0.45, 0.65), (1, 1.6, 0.55, 0.75, "smooth")),
      [INSECTS(10, 0.25)])
scene("bg7_front_yard",
      "Nhưng nó vẫn chỉ gọi được hai lần.",
      trail(*YARD_TRAIL),
      cam((0, 1.6, 0.55, 0.75), (1, 1.9, 0.6, 0.8)),
      [sfx("whisper_eerie", 0.4, 0.3)], min_duration=3.5, fade_out=1.0)
a_mine = scene("bg2_hallway",
               "Rồi đến cái đêm, tôi nghe nó gọi bằng chính giọng của tôi.",
               [L("boy_hoodie/G4_rub_sleepy_eyes", 0.2)],
               cam((0, 1.2, 0.3, 0.6), (1, 1.4, 0.3, 0.6, "in")),
               [CLOCK(6, 0.3)], fade_in=1.2, min_duration=3.5)
scene("bg2_hallway",
      "Tôi trở dậy đi vệ sinh, vừa bước ra hành lang thì từ phía cửa chính, vọng lại tiếng một thằng bé gọi bà hai lần, rõ ràng từng chữ.",
      [walk("boy_hoodie", [0.2, 0.5], fps=4, cyc="tiptoe", end=0.7), L("boy_hoodie/K4_ear_listen", 0.5, start=0.7)],
      cam((0, 1.2, 0.3, 0.6), (1, 1.4, 0.55, 0.6, "smooth"), handheld=3),
      [sfx("floor_creak", 0.1, 0.5), sfx("whisper_eerie", 0.55, 0.55), sfx("whisper_eerie", 0.8, 0.5)])
scene("bg2_hallway",
      "Đó là giọng tôi, từ cách tôi kéo dài chữ cuối, cho đến tiếng hít mũi khe khẽ mỗi khi tôi sợ.",
      [L("boy_hoodie/A6_closeup_shock", 0.5, 1.02, h=[0.85, 0.95])],
      cam((0, 1.0, 0.5, 0.5), (1, 1.0, 0.5, 0.5)),
      [sfx("heartbeat", 0, 0.8, True, 8), sfx("breath_close", 0.3, 0.6)], bg_dim=0.3)
scene("bg3_front_door",
      "Tôi rón rén đến sát cửa, ghé mắt nhìn qua lỗ mắt mèo. Ngoài sân trống không, ánh trăng bạc phếch rọi xuống nền gạch.",
      [L("boy_hoodie/K5_peephole_look", 0.47, h=0.5, face="left")],
      cam((0, 1.2, 0.5, 0.55), (1, 1.6, 0.48, 0.45, "in")),
      [sfx("heartbeat", 0, 0.6, True, 9), sfx("floor_creak", 0.15, 0.4)])
a_peep = scene("bg11_peephole_yard",
               "Rồi ngay trước mắt tôi, một dấu chân ướt từ từ hiện lên trên nền sân, rồi dấu thứ hai, dấu thứ ba, như có ai vô hình đang chậm rãi bước về phía cánh cửa.",
               trail((0.5, 0.71, 0.05), (0.5, 0.9, 0.12), n=5, spread=0.05, start=(0.15, 0.8),
                     clip_circle=[0.5, 0.5, 0.49]),   # từ khe cổng xuống mép dưới mắt mèo (về phía cửa)
               cam((0, 1.15, 0.5, 0.55), (1, 1.25, 0.5, 0.62, "in")),
               [sfx("water_drip", 0.2, 0.5, True, 10), sfx("heartbeat", 0, 0.8, True, 12), sfx("reverse_swell", 0.75, 0.6)])
scene("bg3_front_door", duration=1.4, fade_in=0, flash=[0.0], shake={"amp": 10, "from": 0, "to": 0.5},
      layers=[L("boy_hoodie/K3_pull_back_fear", 0.56, face="left")],
      sounds=[sfx("door_handle_rattle", 0, 1.4)])
scene("bg2_hallway",
      "Tôi lùi lại, và trong phòng, tôi nghe tiếng bà trở mình thật khẽ. Bà đã nghe thấy tiếng gọi ấy, nhưng bà không đáp lại.",
      [walk("boy_hoodie", [0.55, 0.2], fps=4, cyc="back_walk")],
      cam((0, 1.3, 0.45, 0.6), (1, 1.4, 0.3, 0.6, "smooth"), handheld=3),
      [sfx("floor_creak", 0.5, 0.5), sfx("heartbeat", 0, 0.5, True, 9)], fade_out=1.0)
a_esc_end = len(S)

# ============================================================ 6. PHẠM LỖI
a_err = scene("bg7_front_yard",
              "Rồi tôi phạm lỗi.",
              camera=cam((0, 1.2, 0.5, 0.6), (1, 1.3, 0.5, 0.6)),
              sounds=[RAIN(4, 0.5)], fade_in=1.5, min_duration=3.0, bg_dim=0.1)
scene("bg7_front_yard",
      "Hôm ấy bà sang bên kia sông ăn giỗ, dặn tôi ở nhà khoá cửa cẩn thận, rồi chống lưng đi khuất sau cánh cổng sắt.",
      [{**walk("grandma", [0.4, 0.69], fps=2.5, bob=2, end=0.85), "y": [0.95, 0.66], "h": [0.5, 0.34]},
       L("boy_hoodie/E2_back_stand", 0.18)],   # đi ra khe cổng rồi khuất
      cam((0, 1.2, 0.45, 0.6), (1, 1.3, 0.6, 0.6, "smooth")),
      [RAIN(10, 0.4), sfx("gate_rattle", 0.82, 0.5)], fade_out=1.0)
scene("bg4_main_room",
      "Trời vừa chập tối, mưa lắc rắc trên mái tôn, thì ngoài cổng có tiếng gọi tên tôi bằng đúng giọng bà, khàn khàn, xen một tiếng ho rất khẽ.",
      [L("boy_hoodie/B3_look_back_over_shoulder", 0.3)],
      cam((0, 1.2, 0.35, 0.6), (1, 1.4, 0.3, 0.6)),
      [RAIN(12, 0.55), sfx("whisper_eerie", 0.5, 0.4), sfx("cough_old", 0.75, 0.3)])
scene("bg4_main_room",
      "Còn chưa đến giờ cơm tối, tôi không nghĩ ma lại đến sớm như thế, nên tôi buột miệng dạ một tiếng thật to.",
      [L("boy_hoodie/A3_call_out_hand_mouth", 0.3, face="left")],
      cam((0, 1.4, 0.3, 0.6), (1, 1.6, 0.3, 0.58, "in")),
      [RAIN(10, 0.5)])
scene("bg7_front_yard", duration=4.0,
      camera=cam((0, 1.3, 0.69, 0.5), (1, 1.6, 0.69, 0.48, "in"), handheld=2),
      sounds=[RAIN(4, 0.7)])
scene("bg7_front_yard",
      "Ngoài cổng im bặt, không có tiếng bước chân, không có tiếng mở cổng, chỉ có tiếng mưa.",
      camera=cam((0, 1.6, 0.69, 0.48), (1, 1.8, 0.69, 0.48)),
      sounds=[RAIN(8, 0.7)], min_duration=4.0)
scene("bg4_main_room",
      "Tôi đứng chôn chân giữa nhà, không dám ra mở cổng mà cũng không dám quay vào trong, và nửa tiếng ấy dài như cả một đêm.",
      [L("boy_hoodie/B1_stand_worried", 0.4, jitter=1)],
      cam((0, 1.2, 0.4, 0.6), (1, 1.35, 0.4, 0.6)),
      [RAIN(12, 0.5), CLOCK(12, 0.4), sfx("heartbeat", 0.2, 0.5, True, 8)])
scene("bg4_main_room",
      "Mỗi lần gió giật cánh cổng kêu lạch xạch, tôi lại tưởng có ai đang đứng ngoài đó lay nó.",
      [L("boy_hoodie/E3_crouch_hug_knees_shaking", 0.14, h=0.36, jitter=2)],
      cam((0, 1.3, 0.25, 0.6), (1, 1.5, 0.2, 0.62)),
      [RAIN(8, 0.5), sfx("gate_rattle", 0.3, 0.7), sfx("gate_rattle", 0.75, 0.5)])
scene("bg7_front_yard",
      "Rồi tiếng xe máy dừng lại trước cổng, bà về bằng xe ôm, áo mưa còn nhỏ nước tong tỏng.",
      [walk("grandma", [0.8, 0.45], fps=2.5, bob=2, end=0.85), L("grandma/00_stand_front", 0.45, start=0.85)],
      cam((0, 1.2, 0.65, 0.6), (1, 1.2, 0.5, 0.6, "smooth")),
      [sfx("motorbike_stop", 0, 0.8), RAIN(8, 0.45), sfx("gate_rattle", 0.4, 0.5)])
scene("bg4_main_room",
      "Nghe tôi kể, mặt bà xám lại. Bà bảo tôi đã lên tiếng đáp lại nó rồi, giờ nó biết trong nhà này có đứa nghe được nó, nó sẽ không chịu đi nữa.",
      [L("grandma/E1_hold_boy_hands", 0.45, h=0.5)],
      cam((0, 1.3, 0.45, 0.62), (1, 1.6, 0.45, 0.6, "in")),
      [RAIN(10, 0.35), sfx("whisper_eerie", 0.7, 0.3)])
a_sig = scene("bg6_kitchen",
              "Tối ấy, ngồi dưới bếp bên ánh đèn vàng, bà hạ giọng dạy tôi một ám hiệu mới.",
              [L("grandma/F4_sit_stool_three_fingers", 0.45, h=0.42), L("boy_hoodie/M3_sit_stool_eat", 0.72, h=0.42, face="left")],
              cam((0, 1.2, 0.55, 0.6), (1, 1.4, 0.55, 0.6)),
              [INSECTS(8, 0.3)])
scene("bg6_kitchen",
      "Từ nay nếu là bà gọi, bà sẽ gọi đủ ba lần rồi gõ cửa ba tiếng, thiếu một tiếng thôi cũng không được mở.",
      [L("grandma/F4_sit_stool_three_fingers", 0.45, h=0.42), L("boy_hoodie/M3_sit_stool_eat", 0.72, h=0.42, face="left")],
      cam((0, 1.5, 0.45, 0.58), (1, 1.9, 0.45, 0.55, "in")),
      [INSECTS(8, 0.25), sfx("knock_3", 0.6, 0.35)])
a_third = scene("bg8_bedroom_door",
                "Đêm đó, lần đầu tiên, [0.6] tôi nghe thấy tiếng gọi thứ ba.",
                [L("boy_hoodie/L5_peek_from_blanket", 0.2, h=0.36, jitter=1)],
                cam((0, 1.2, 0.4, 0.62), (1, 1.6, 0.5, 0.66, "in"), handheld=3),
                [sfx("whisper_eerie", 0.1, 0.5), sfx("whisper_eerie", 0.35, 0.5), sfx("whisper_eerie", 0.85, 0.7)],
                fade_in=1.0)
scene("bg8_bedroom_door",
      "Nó gọi tên tôi ba lần, rồi gõ lên cánh cửa hai tiếng, ngập ngừng, như một đứa trẻ đang quên mất bài.",
      camera=cam((0, 1.5, 0.5, 0.62), (1, 2.0, 0.5, 0.66, "in"), handheld=4),
      sounds=[sfx("heartbeat", 0, 0.7, True, 9), sfx("knock_2_hesitant", 0.6, 1.0)])
scene("bg1_bedroom",
      "Bà ôm chặt tôi trong bóng tối, run bần bật, thì thầm rằng nó nghe được hết rồi, mọi lời nói trong căn nhà này nó đều nghe được hết.",
      [L("grandma/F6_hug_boy_bed_dark", **BED, jitter=1)],
      cam((0, 1.3, 0.68, 0.6), (1, 1.7, 0.7, 0.62, "in"), handheld=3),
      [sfx("heartbeat", 0, 0.6, True, 10), sfx("breath_close", 0.4, 0.5)], bg_dim=0.25)
scene("bg8_bedroom_door",
      "Đêm hôm sau, [0.6] nó gõ đủ ba tiếng.",
      camera=cam((0, 1.6, 0.5, 0.66), (1, 2.1, 0.5, 0.68, "in"), handheld=5),
      sounds=[sfx("knock_3", 0.55, 1.3), sfx("heartbeat", 0, 0.8, True, 6)], min_duration=4.5)
scene("bg8_bedroom_door", duration=1.3, fade_in=0, flash=[0.0], shake={"amp": 14, "from": 0, "to": 0.6}, bg_dim=0.3,
      layers=[L("grandma/G6_stand_dark_smile", 0.5, 0.97, h=[0.6, 0.75], ease="out", glow=True)],
      sounds=[sfx("ghost_stinger", 0, 1.8)])
scene("black", duration=1.5)
a_err_end = len(S)

# ============================================================ 7. HÌNH NHÂN THẾ MẠNG
a_eff = scene("bg4_main_room",
              "Sáng hôm sau, bà dậy từ rất sớm, cắt một lọn tóc của tôi rồi nhét vào một hình nhân giấy, khoác lên nó chiếc áo cũ của tôi.",
              [L("props/HN1_paper_effigy_hoodie", **{**GMA_SEAT, "h": 0.36}), L("grandma/00_stand_front", 0.45),
               L("boy_hoodie/B1_stand_worried", 0.25)],
              cam((0, 1.2, 0.5, 0.6), (1, 1.35, 0.6, 0.6)),
              [sfx("scissors_hair", 0.15, 0.9), INSECTS(8, 0.2)], fade_in=1.2)
scene("bg4_main_room",
      "Bà đặt nó ngồi trên ghế trong gian thờ, trông giống tôi đến rợn người, rồi bảo đây là hình nhân thế mạng, nửa đêm phải đem ra bến sông đốt.",
      [L("props/HN1_paper_effigy_hoodie", **{**GMA_SEAT, "h": 0.36})],
      cam((0, 1.3, 0.75, 0.6), (1, 1.8, 0.84, 0.58, "in")),
      [sfx("ritual_bell", 0.1, 0.4)])
scene("bg4_main_room",
      "Bà bảo phải để nó tưởng đã bắt được tôi rồi. Cả ngày hôm ấy tôi không dám nhìn vào gian thờ, vì cái đầu giấy ấy như hơi nghiêng đi, về phía tôi.",
      [L("props/HN1_paper_effigy_hoodie", **{**GMA_SEAT, "h": 0.36}),
       L("boy_hoodie/B3_look_back_over_shoulder", 0.4)],
      cam((0, 1.3, 0.6, 0.6), (1, 1.6, 0.8, 0.6, "in"), handheld=2),
      [sfx("whisper_eerie", 0.6, 0.3), sfx("floor_creak", 0.75, 0.4)])
scene("bg7_front_yard",
      "Chiều hôm ấy, bà ôm bát gạo muối đi một vòng quanh nhà, vừa đi vừa rải, vừa lầm rầm khấn những câu tôi không hiểu.",
      [L("grandma/A3_scatter_rice_salt", 0.45, face="right")],
      cam((0, 1.2, 0.45, 0.6), (1, 1.3, 0.5, 0.6)),
      [sfx("rice_scatter", 0.2), sfx("rice_scatter", 0.6, 0.8), sfx("ritual_bell", 0.05, 0.35)])
scene("bg7_front_yard",
      "Gạo muối rơi lạo xạo trên nền sân, phủ lên cả những dấu chân bùn đã khô.",
      trail(*YARD_TRAIL),
      cam((0, 1.5, 0.55, 0.75), (1, 1.8, 0.58, 0.8)),
      [sfx("rice_scatter", 0.1, 0.7)], min_duration=3.5)
scene("bg7_front_yard",
      "Gần nửa đêm, bà ôm hình nhân và xấp vàng mã đi ra cổng. Trước khi đi, bà quay lại dặn, ai gọi cũng không được mở, kể cả bà, cho đến khi trời sáng.",
      [L("grandma/J1_back_carry_effigy", 0.6), L("boy_hoodie/E2_back_stand", 0.2)],
      cam((0, 1.2, 0.45, 0.6), (1, 1.35, 0.6, 0.55, "smooth")),
      [FROGS(12, 0.4), sfx("gate_rattle", 0.85, 0.5)])
a_wait = scene("bg3_front_door",
               "Tôi ngồi co ro sau cánh cửa, đếm từng tiếng tích tắc của chiếc đồng hồ treo tường. Một giờ. Hai giờ. Bà vẫn chưa về.",
               [L("boy_hoodie/E3_crouch_hug_knees_shaking", 0.62, h=0.36, jitter=1)],
               cam((0, 1.2, 0.55, 0.62), (1, 1.4, 0.6, 0.66)),
               [CLOCK(14, 0.6), FROGS(14, 0.3)])
scene("bg3_front_door",
      "Khoảng hai giờ, tiếng ếch nhái ngoài kia bỗng im bặt cùng một lúc, như có ai vừa đi ngang qua bờ ao.",
      [L("boy_hoodie/K4_ear_listen", 0.62, h=0.42)],
      cam((0, 1.4, 0.6, 0.6), (1, 1.6, 0.6, 0.58, "in")),
      [sfx("frogs_night", 0, 0.5, True, 3.5, 0, 0.1), CLOCK(10, 0.4)])
scene("bg10_river_wharf",
      "Qua khe cửa, tôi thấy phía bến sông có một đốm lửa nhỏ bùng lên, cháy một lúc rồi tắt phụt, và tôi biết bà đã đốt xong hình nhân.",
      [FIRE],
      cam((0, 1.6, 0.56, 0.75), (1, 1.3, 0.5, 0.6, "smooth")),
      [sfx("paper_burn", 0, 0.5, True, 10, 0.5, 1.5), RIVER(10, 0.3)])
scene("bg10_river_wharf",
      "Nhưng bà vẫn không về.",
      camera=cam((0, 1.3, 0.5, 0.6), (1, 1.5, 0.45, 0.62)),
      sounds=[RIVER(5, 0.4)], min_duration=3.5, fade_out=0.8)
a_3am = scene("bg3_front_door",
              "Gần ba giờ sáng, có tiếng gọi tên tôi đủ ba lần, rồi ba tiếng gõ cửa, và tiếng ho khù khụ quen thuộc.",
              [L("boy_hoodie/L4_back_against_door", 0.5, h=0.46, jitter=1)],
              cam((0, 1.3, 0.5, 0.6), (1, 1.6, 0.5, 0.58, "in"), handheld=3),
              [sfx("whisper_eerie", 0.1, 0.5), sfx("knock_3", 0.45, 1.2), sfx("cough_old", 0.8, 0.7)])
scene("bg3_front_door",
      "Bà nài nỉ tôi mở cửa, bảo bà ướt hết rồi, lạnh lắm. Tôi cắn chặt môi đến bật máu, nhất quyết không đáp một lời.",
      [L("boy_hoodie/E5_cover_mouth_hold_breath", 0.5, 1.0, h=0.6, jitter=2)],
      cam((0, 1.2, 0.5, 0.6), (1, 1.4, 0.5, 0.6, "in"), handheld=4),
      [sfx("woman_sob_door", 0.3, 0.7, True, 8), sfx("water_drip", 0, 0.4, True, 10)])
scene("bg3_front_door",
      "Bà đứng ngoài đó gọi, rồi khóc, tiếng khóc nghèn nghẹn như người bị nước tràn vào họng, cho đến khi tiếng gà gáy đầu tiên vang lên.",
      [L("boy_hoodie/E3_crouch_hug_knees_shaking", 0.5, h=0.36, jitter=2)],
      cam((0, 1.4, 0.5, 0.62), (1, 1.6, 0.5, 0.66)),
      [sfx("woman_sob_door", 0, 0.8, True, 10, 0, 2.0), sfx("rooster_crow", 0.82, 0.8)])
a_dawn = scene("bg7_front_yard",
               "Trời hửng sáng tôi mới dám mở cửa. Bà ngồi bệt dưới hiên, quần áo ướt sũng, tóc bết nước, rồi ngẩng lên cười hiền với tôi.",
               [L("grandma/G5_sit_porch_wet_smile", 0.32, h=0.34), L("boy_hoodie/B1_stand_worried", 0.12)],
               cam((0, 1.2, 0.3, 0.62), (1, 1.6, 0.32, 0.66, "in")),
               [sfx("water_drip", 0, 0.6, True, 10), sfx("rooster_crow", 0.1, 0.4)], fade_in=1.5)
scene("bg7_front_yard",
      "Bà khen tôi ngoan lắm, rồi bảo xong rồi, từ nay nó sẽ không gọi nữa.",
      [L("grandma/G5_sit_porch_wet_smile", 0.32, h=0.34)],
      cam((0, 1.8, 0.32, 0.6), (1, 2.1, 0.32, 0.56, "in")),
      [sfx("water_drip", 0, 0.6, True, 6)])
scene("bg7_front_yard",
      "Và đúng là [0.5] nó không gọi nữa.",
      camera=cam((0, 1.2, 0.5, 0.6), (1, 1.3, 0.5, 0.6)),
      sounds=[INSECTS(5, 0.3)], min_duration=3.5, fade_out=1.2)
a_eff_end = len(S)

# ============================================================ 8. BÌNH YÊN GIẢ
a_calm = scene("bg4d_main_room_day",
               "Những ngày sau đó bình yên đến lạ. Bà khoẻ hẳn ra, chập tối không còn ho, lưng cũng chẳng thấy đau, đi lại thẳng tắp và nhẹ tênh.",
                              [day(walk("grandma", [0.9, 0.45], fps=2.5, cyc="fake_walk", end=0.85, h=0.54)),
                day(L("grandma/G6_stand_dark_smile", 0.45, h=0.54, start=0.85))],
               cam((0, 1.2, 0.6, 0.6), (1, 1.2, 0.45, 0.6, "smooth")),
               [sfx("footsteps_slow", 0, 0.3, True, 8)], fade_in=1.2)
scene("bg4d_main_room_day",
      "Bà bảo chắc ra sông gặp gió lạnh mà khỏi. Tôi cười theo, nhưng không hiểu sao trong lòng cứ thấy gờn gợn.",
      [day(L("grandma/G6_stand_dark_smile", 0.45, h=0.54)), day(L("boy_hoodie/B1_stand_worried", 0.25))],
      cam((0, 1.3, 0.4, 0.6), (1, 1.45, 0.42, 0.55)),
      [sfx("clock_tick", 0, 0.2, True, 8)])
scene("bg4_main_room",
      "Bữa cơm nào bà cũng gắp thức ăn cho tôi, gắp đầy bát, rồi ngồi nhìn tôi ăn mà không động đũa.",
      [L("boy_hoodie/M3_sit_stool_eat", **BOY_SEAT), L("grandma/H4_sit_offer_food", **FAKE_SEAT)],
      cam((0, 1.25, 0.68, 0.6), (1, 1.45, 0.75, 0.6)),
      [sfx("spoon_bowl_tap", 0.3, 0.3), CLOCK(10, 0.25)])
scene("bg4_main_room",
      "Có lần bà đưa tay vuốt tóc tôi, và tôi giật mình, vì bàn tay bà lạnh ngắt, da nhăn nheo trắng bệch như người ngâm nước rất lâu.",
      [L("boy_hoodie/M4_sit_stool_look_back_fear", **BOY_SEAT), L("grandma/H4_sit_offer_food", **FAKE_SEAT)],
      cam((0, 1.45, 0.75, 0.6), (1, 1.9, 0.65, 0.55, "in")),
      [sfx("water_drip", 0.4, 0.4, True, 6), sfx("breath_close", 0.5, 0.4)])
scene("bg5c_altar_grandpa_cold",
      "Chỉ có vài điều nho nhỏ làm tôi khó chịu. Bà không thắp hương trên bàn thờ nữa, bát hương nguội lạnh, chân nhang cắm trơ trọi.",
      camera=cam((0, 1.2, 0.45, 0.5), (1, 1.6, 0.27, 0.58, "smooth")),
      sounds=[CLOCK(10, 0.3)])
scene("bg7_front_yard",
      "Con mèo mướp nhà bên cứ thấy bà là xù lông, rít lên một tiếng rồi bỏ chạy.",
      [L("grandma/I2_fake_look_down_side", 0.35, h=0.54),
       L("cat_tabby/A1_stand_look", 0.55, h=0.18, face="left", end=0.3),
       L("cat_tabby/A2_arch_hiss", 0.55, h=0.2, face="left", jitter=2, start=0.3, end=0.55),
       # chạy ra khe cổng rồi khuất (không chạy xuyên tường)
       {"cycle": "cat_tabby/run", "fps": 10, "x": [0.55, 0.69], "y": [0.95, 0.67], "h": [0.16, 0.06],
        "face": "auto", "breathe": 0, "start": 0.55, "end": 0.85}],
      cam((0, 1.3, 0.45, 0.65), (1, 1.4, 0.55, 0.6, "smooth")),
      [sfx("cat_hiss", 0.32, 1.0), INSECTS(8, 0.3)])
scene("bg7_front_yard",
      "Tối tối bà không còn ra hiên ngồi nhìn bến sông nữa, mà lại ngồi quay lưng về phía ấy, thẳng đơ, im lìm.",
      [L("grandma/H3_sit_back_turned", 0.3, h=0.36)],
      cam((0, 1.3, 0.35, 0.62), (1, 1.6, 0.32, 0.6, "in")),
      [FROGS(10, 0.45)])
scene("bg1_bedroom",
      "Và đêm nào nằm cạnh bà, tôi cũng ngửi thấy thoang thoảng mùi tanh của bùn sông.",
      [L("grandma/H2_bed_edge_stroke_head", **BED)],
      cam((0, 1.2, 0.68, 0.6), (1, 1.5, 0.7, 0.62)),
      [FROGS(8, 0.3), sfx("water_drip", 0.3, 0.3, True, 6)])
a_oil = scene("bg1_bedroom",
              "Một tối, tôi lục ngăn kéo tìm lọ dầu gió bà vẫn xoa cho tôi mỗi đêm.",
              [L("boy_hoodie/B1_stand_worried", 0.35)],
              cam((0, 1.2, 0.4, 0.6), (1, 1.3, 0.35, 0.6)),
              [sfx("floor_creak", 0.2, 0.4)])
scene("bg12_bedside_drawer",
      "Lọ dầu vẫn nằm đó, nắp vặn chặt, lớp bụi mỏng trên nắp còn nguyên. Từ cái đêm bà ra sông, bà chưa mở nó lần nào.",
      [L("props/HN6_wind_oil_bottle", 0.495, 0.515, h=0.11)],   # chỗ trống giữa ngăn kéo
      cam((0, 1.2, 0.5, 0.5), (1, 2.0, 0.5, 0.46, "in")),
      [sfx("heartbeat", 0.4, 0.5, True, 8)])
a_sau = scene("bg7d_front_yard_morning",
              "Sáng hôm sau, bà Sáu bán xôi đầu ngõ kéo tôi lại, hỏi nhỏ đêm hôm ấy bà tôi đi đâu mà lội nước thế.",
              [day(L("boy_hoodie/B1_stand_worried", 0.42)), day(L("ba_sau/A2_lean_whisper", 0.62))],
              cam((0, 1.2, 0.5, 0.6), (1, 1.35, 0.52, 0.58)),
              [sfx("rooster_crow", 0.05, 0.25), sfx("footsteps_slow", 0.1, 0.25, True, 3)], fade_in=1.0)
scene("bg7d_front_yard_morning",
      "Bà Sáu bảo sáng ấy dậy sớm thổi xôi, thấy một dãy dấu chân ướt từ bến sông đi ngược lên, thẳng vào cổng nhà tôi.",
      [*trail(*YARD_TRAIL, tint=False), day(L("ba_sau/A3_point_far", 0.38, face="right"))],
      cam((0, 1.3, 0.69, 0.55), (1, 1.6, 0.55, 0.75, "smooth")),
      [sfx("water_drip", 0.2, 0.3, True, 6)])
scene("bg7d_front_yard_morning",
      "Nhưng lạ lắm, dấu chân chỉ có một chiều đi lên, [0.5] chẳng có chiều nào đi xuống.",
      trail(*YARD_TRAIL, tint=False),
      cam((0, 1.6, 0.55, 0.75), (1, 2.0, 0.6, 0.8, "in")),
      [sfx("reverse_swell", 0.5, 0.5)], min_duration=4.0)
scene("bg1_bedroom",
      "Tối hôm đó, bà ngồi bên mép giường, hỏi tôi rất nhẹ nhàng, hôm trước tôi đã đáp lời nó ra sao, rồi bảo tôi thử dạ lại một tiếng cho bà nghe.",
      [L("grandma/H2_bed_edge_stroke_head", **BED)],
      cam((0, 1.3, 0.66, 0.6), (1, 1.7, 0.62, 0.55, "in"), handheld=2),
      [CLOCK(12, 0.35), sfx("breath_close", 0.6, 0.35)])
scene("bg1_bedroom",
      "Tôi không hiểu vì sao, nhưng cổ họng tôi cứng lại, [0.5] và tôi không đáp.",
      [L("boy_hoodie/G3_bed_blanket_chin_scared", 0.7, 0.95, h=0.5, jitter=1)],
      cam((0, 1.5, 0.7, 0.6), (1, 1.7, 0.7, 0.62)),
      [CLOCK(6, 0.45)], min_duration=4.0)
scene("bg1_bedroom", duration=2.0, fade_in=0, bg_dim=0.4,
      layers=[L("grandma/H6_closeup_face_smile", 0.5, 1.03, h=[0.85, 0.95], tint=False)],
      sounds=[sfx("water_drip", 0, 0.7, True, 2.0), sfx("whisper_eerie", 0.1, 0.4)])
a_calm_end = len(S)

# ============================================================ 9. KẾT
a_end = scene("bg1_bedroom",
              "Cho đến đêm qua.",
              [L("grandma/H1_bed_hold_wrist_whisper", **BED)],
              cam((0, 1.2, 0.66, 0.6), (1, 1.3, 0.68, 0.6)),
              [FROGS(5, 0.3)], fade_in=1.5, min_duration=3.0)
scene("bg7_front_yard",
      "Đêm qua, có ai đó gọi tên tôi ba lần từ ngoài cổng, gõ ba tiếng, rồi ho những tràng khù khụ quen thuộc đến thắt lòng.",
      camera=cam((0, 1.25, 0.69, 0.5), (1, 1.7, 0.69, 0.45, "in"), handheld=3),
      sounds=[FROGS(12, 0.35), sfx("whisper_eerie", 0.15, 0.5), sfx("gate_knock_metal", 0.45, 1.1), sfx("cough_old", 0.8, 0.8)])
scene("bg7_front_yard",
      "Giọng ấy khóc, bảo tôi ra mở cổng cho bà, bà bị nhốt ngoài này lâu lắm rồi, dưới nước lạnh lắm.",
      [L("grandma/A6_head_bowed_face_hidden", 0.69, 0.64, h=0.3, glow=True)],
      cam((0, 1.8, 0.69, 0.45), (1, 2.2, 0.69, 0.42, "in"), handheld=3),
      [sfx("woman_sob_door", 0.1, 0.8, True, 9), sfx("water_drip", 0, 0.4, True, 9)])
scene("bg1_bedroom",
      "Bàn tay lạnh ngắt bên cạnh siết chặt cổ tay tôi, bà thì thầm bảo tôi đừng lên tiếng.",
      [L("grandma/H1_bed_hold_wrist_whisper", **BED)],
      cam((0, 1.4, 0.68, 0.6), (1, 2.0, 0.72, 0.62, "in"), handheld=3),
      [sfx("breath_close", 0.3, 0.8), sfx("heartbeat", 0, 0.7, True, 10)])
scene("bg1_bedroom",
      "Tôi đã không đáp lại lời bà.",
      [L("grandma/H5_closeup_hand_wrist", 0.5, 1.02, h=0.95, tint=False)],
      cam((0, 1.0, 0.5, 0.5), (1, 1.0, 0.5, 0.5)),
      [sfx("heartbeat", 0, 0.7, True, 4)], min_duration=3.5, bg_dim=0.4)
scene("bg1_bedroom",
      "Suốt đêm ấy, bàn tay bên cạnh không lúc nào buông cổ tay tôi ra, còn tiếng gọi ngoài cổng thì nhỏ dần, nhỏ dần, rồi tắt hẳn.",
      [L("grandma/H1_bed_hold_wrist_whisper", **BED)],
      cam((0, 1.3, 0.68, 0.6), (1, 1.25, 0.6, 0.6, "smooth")),
      [sfx("woman_sob_door", 0, 0.5, True, 10, 0, 4.0), CLOCK(10, 0.3)])
scene("bg10_river_wharf",
      "Chỉ còn lại tiếng khóc rất khẽ, xa dần về phía bến sông.",
      [L("grandma/A6_head_bowed_face_hidden", 0.45, h=0.32, glow=True, end=0.6)],
      cam((0, 1.3, 0.45, 0.6), (1, 1.5, 0.4, 0.66)),
      [RIVER(6, 0.5), sfx("woman_sob_door", 0, 0.3, True, 5, 0, 3)], min_duration=4.5, fade_out=1.2)
a_morning = scene("bg7d_front_yard_morning",
                  "Sáng nay mở cổng, tôi thấy một chiếc dép nhựa của bà nằm úp sấp dưới chân cột, ướt sũng, bùn sông còn bám đặc ở gót.",
                  [L("props/HN3_sandal_upside_down_puddle", 0.72, 0.95, h=0.17, tint=False)],
                  cam((0, 1.2, 0.6, 0.6), (1, 1.9, 0.72, 0.85, "in")),
                  [sfx("rooster_crow", 0.05, 0.4), sfx("gate_rattle", 0.15, 0.5)], fade_in=1.5)
scene("bg7d_front_yard_morning",
      "Bên cạnh là một vũng nước nhỏ, đọng lại như có ai đã đứng đó rất lâu, rất lâu.",
      [L("props/HN3_sandal_upside_down_puddle", 0.72, 0.95, h=0.17, tint=False)],
      cam((0, 1.9, 0.72, 0.85), (1, 2.2, 0.72, 0.86)),
      [sfx("water_drip", 0, 0.5, True, 7)], min_duration=4.0)
scene("bg10_river_wharf", duration=3.0, fade_in=0.6, fade_out=0.6, bg_dim=0.2,
      layers=[L("props/HN2_wooden_clog_upside_down", 0.45, 0.9, h=0.14)],
      camera=cam((0, 1.6, 0.45, 0.8), (1, 1.9, 0.45, 0.82)),
      sounds=[RIVER(3, 0.5)])
scene("bg4d_main_room_day",
      "Trong nhà, bà gọi tôi vào ăn sáng. Bà gọi hai lần, [0.6] rồi thôi.",
      [day(L("grandma/G6_stand_dark_smile", 0.6, h=0.54))],
      cam((0, 1.2, 0.55, 0.6), (1, 1.6, 0.6, 0.5, "in")),
      [sfx("spoon_bowl_tap", 0.2, 0.3)], min_duration=5.0)
a_last = scene("bg1_bedroom",
               "Tối nay, lúc tắt đèn, bà ngồi bên mép giường xoa đầu tôi, và dặn một điều mới mà bà bắt tôi phải thuộc như thuộc tên mình.",
               [L("grandma/H2_bed_edge_stroke_head", **BED)],
               cam((0, 1.2, 0.66, 0.6), (1, 1.5, 0.64, 0.56)),
               [FROGS(10, 0.3), CLOCK(10, 0.3)], fade_in=1.0)
scene("bg1_bedroom",
      "Từ giờ trở đi, nửa đêm mà nghe ai gọi đủ ba lần, [0.6] thì tuyệt đối đừng đáp lại.",
      [L("grandma/H2_bed_edge_stroke_head", **BED)],
      cam((0, 1.5, 0.64, 0.56), (1, 2.2, 0.62, 0.5, "in"), handheld=2),
      [CLOCK(8, 0.4), sfx("reverse_swell", 0.55, 0.6)], min_duration=5.0)
scene("bg1_bedroom", duration=1.6, fade_in=0, flash=[0.0], shake={"amp": 16, "from": 0, "to": 0.6}, bg_dim=0.4,
      layers=[L("grandma/H6_closeup_face_smile", 0.5, 1.05, h=[0.75, 1.2], ease="out", glow=True)],
      sounds=[sfx("ghost_stinger", 0, 2.2)])
scene("black", duration=4.0, fade_in=0.3,
      sounds=[sfx("gate_knock_metal", 0.5, 0.6), sfx("water_drip", 0, 0.4, True, 4, 0, 1.5)])

story["scenes"] = S
# nhạc nền: chỉ drone_low — cố ý cắt ở khoảnh khắc im lặng/tiết lộ
story["music"] = [
    {"sound": "drone_low", "from": 1, "to": a_open_end - 1, "volume": 0.6, "fade_in": 2.5, "fade_out": 1.5},
    {"sound": "drone_low", "from": a_aunt, "to": a_aunt_end, "volume": 0.5, "fade_in": 3, "fade_out": 2},
    {"sound": "drone_low", "from": a_first + 1, "to": a_first + 2, "volume": 0.5, "fade_in": 2, "fade_out": 0.05},
    {"sound": "drone_low", "from": a_mine, "to": a_peep, "volume": 0.6, "fade_in": 2.5, "fade_out": 0.05},
    {"sound": "drone_low", "from": a_third, "to": a_err_end - 2, "volume": 0.7, "fade_in": 2, "fade_out": 0.05},
    {"sound": "drone_low", "from": a_wait, "to": a_dawn - 1, "volume": 0.6, "fade_in": 3, "fade_out": 2},
    {"sound": "drone_low", "from": a_oil, "to": a_calm_end - 1, "volume": 0.55, "fade_in": 3, "fade_out": 0.05},
    {"sound": "drone_low", "from": a_end + 1, "to": a_morning - 1, "volume": 0.7, "fade_in": 2, "fade_out": 2},
    {"sound": "drone_low", "from": a_last, "to": len(S) - 2, "volume": 0.6, "fade_in": 2, "fade_out": 0.05},
]
story["parts"] = {"_note": "Điểm cắt cho video ngắn (render --scenes a-b)",
                  "phan_1": [1, a_esc_end], "phan_2": [a_err, a_eff_end], "phan_3": [a_calm, len(S)]}
out = ROOT / "scripts/tieng_goi_thu_ba.json"
out.write_text(json.dumps(story, ensure_ascii=False, indent=1), encoding="utf-8")
print(out, len(S), "cảnh")
