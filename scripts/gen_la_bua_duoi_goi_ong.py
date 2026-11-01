"""Sinh kịch bản "Lá bùa dưới gối ông" (3 phần × ~15 phút) từ mẫu templates/kich_ban_mau.json.

    python3 scripts/gen_la_bua_duoi_goi_ong.py [1|2]  → scripts/la_bua_duoi_goi_ong_p<n>.json (mặc định Phần 1)

Lời kể lấy NGUYÊN VĂN từ bản đã duyệt scripts/kich_ban_la_bua_duoi_goi_ong.md (mỗi đoạn văn → 1..n cảnh,
tách ở ranh giới câu, ≤ 45 chữ/cảnh). Sửa lời thì sửa file md rồi chạy lại; ở đây chỉ dàn hình, camera, âm thanh.
Asset cần tạo: ASSET_REQUESTS (Phần 1), ASSET_REQUESTS_P2 (Phần 2).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = (ROOT / "scripts/kich_ban_la_bua_duoi_goi_ong.md").read_text(encoding="utf-8")


def paragraphs(start: str, end: str) -> list[str]:
    sec = MD[MD.index(start):MD.index(end)]
    return [p.strip() for p in sec.split("\n\n")
            if p.strip() and not p.lstrip().startswith(("#", "---", "*", ">"))]


def chunks(par: str, limit: int = 45) -> list[str]:
    """Tách đoạn văn thành các cảnh ở ranh giới câu (không bao giờ cắt giữa câu)."""
    out, cur = [], []
    for sent in re.split(r"(?<=[.!?…])\s+", par):
        if cur and len(" ".join(cur + [sent]).split()) > limit:
            out.append(" ".join(cur))
            cur = []
        cur.append(sent)
    out.append(" ".join(cur))
    return out


# ============================================================ CHUNG
BOY_REF = "assets/source/boy_hoodie_base.png"
GMA_REF = "assets/characters/grandma/00_stand_front.png"
MOM_REF = "assets/characters/mother_alive/00_stand_front.png"
ONG_BASE = "assets/characters/ong_noi/ong_noi_base_front.png"     # có sau khi nạp ong_noi_base
THAY_BASE = "assets/characters/thay_tu/thay_tu_base_front.png"    # có sau khi nạp thay_tu_base
UT_BASE = "assets/characters/co_ut/co_ut_base_front.png"          # có sau khi nạp co_ut_base
PORTRAIT_BG = "assets/backgrounds/bg5b_altar_grandpa_lit.png"     # ảnh thờ ông có sẵn → ông phải giống ảnh này
# "bản gốc" của đồ vật xuất hiện ở nhiều sheet — sheet sau đính kèm để vẽ giống hệt (check_story tự xếp sang đợt sau)
JACKET_REF = "assets/characters/boy_hoodie/N5_stuff_pocket_guilty.png"   # áo khoác đen mẹ may (sheet N)
BAMBOO_BED_REF = "assets/characters/ong_noi/A4_sit_bed_watch_clock.png" # giường tre của ông (sheet ông A)
SPARE_REF = "assets/characters/props/LB4_chopsticks_spare_carved.png"    # đôi đũa dư (sheet LB) — bản có chữ KHOA: LF4
COFFIN_REF = "assets/backgrounds/bgL2_wake_coffin.png"                   # quan tài (phông gian thờ)
MOM_PORTRAIT = "assets/characters/mother_alive/A4_portrait_front.png"     # mặt mẹ cho di ảnh
COFFIN_STYLE = ("Illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black "
                "outlines as the reference image, simple shapes, 16:9, dark night lighting in deep blue and gray tones, "
                "warm candlelight only near the candles, no text.")   # cảnh nhìn từ trên xuống, có người → không dùng style chung
SAME_JACKET = " The black jacket must be EXACTLY the jacket in the LAST attached image (same cut, pockets, zip)."
STYLE_KIDS = "simple chibi proportions, dot eyes, hand-drawn crayon / colored-pencil texture, thick black outlines, minimal flat colors"
BOY = "the boy Khoa from the reference image (messy spiky black hair, dark moss-green hoodie, charcoal pants, white sneakers)"
ONG = ("the grandfather from the reference image (thin elderly Vietnamese man, swept-back silver-gray hair, "
       "deep forehead wrinkles, faded gray-blue collared shirt, dark brown trousers)")
GMA = "the small hunched grandmother from the reference image (silver-gray bun, dark brown ao ba ba blouse)"
MOM = "the mother from the reference image (black low bun, faded beige cardigan, long dark gray dress)"
BAMBOO_BED = "a low old bamboo bed"
JACKET = ("IMPORTANT for this whole sheet: the boy wears a DARK BLACK padded zip-up jacket over his moss-green "
          "hoodie (the green hood shows at the collar), same charcoal pants and white sneakers. The jacket has two "
          "deep front pockets.")
# Phần 2: đồ vật/trang phục lặp lại ở nhiều sheet — mô tả cố định để Gemini vẽ giống nhau
MOM_BED = "simple low dark wooden bed with a gray-blue blanket and a pale pillow"
MOM_BED_REF = "assets/characters/mother_alive/H1_bed_lie_sick.png"            # giường của mẹ (sheet H)
SWEATER = "a small dark-red knitted child's sweater, body and both sleeves finished, the collar unfinished with loose yarn"
TUNIC = ("a loose coarse BEIGE gauze Vietnamese mourning tunic (light beige / unbleached, NOT white) that she sewed herself")
MOURN = ("Where the pose says MOURNING he wears a traditional Vietnamese mourning outfit over his clothes: a loose "
         "coarse BEIGE gauze tunic (light beige / unbleached, NOT white) and a beige gauze headband.")

ASSET_REQUESTS = [
    # ---------------------------------------------------- nhân vật mới (ĐỢT 1)
    {"id": "ong_noi_base", "kind": "character_base", "character": "ong_noi", "name": "Ông nội", "default_h": 0.58,
     "why": "nhân vật chính Phần 1 — phải giống ảnh thờ ông trong phông bg5b_altar_grandpa_lit",
     "refs": [PORTRAIT_BG, BOY_REF, GMA_REF],
     "design": ("Same art style as the reference images. A thin, gentle, quiet elderly Vietnamese grandfather in "
                "his late seventies: EXACTLY the man in the framed portrait on the altar in attached image 1  (swept-back silver-gray hair, high forehead with deep wrinkles, tired kind eyes, thin face, "
                "slightly protruding ears). He wears a faded gray-blue short-sleeved collared button shirt, "
                "dark brown trousers, simple dark wooden clogs. Slightly stooped, a little taller than the "
                "grandmother in attached image 3. " + STYLE_KIDS + ". Never white clothing.")},
    {"id": "thay_tu_base", "kind": "character_base", "character": "thay_tu", "name": "Thầy Tư (thầy cúng)",
     "default_h": 0.58, "why": "thầy cúng xem giờ, viết bùa (cả 3 phần)", "refs": [BOY_REF, GMA_REF],
     "design": ("Same art style as the reference images. A lean old Vietnamese village ritual master (thay cung) "
                "in his sixties: thin gray goatee and thin mustache, sharp narrow eyes, small round glasses, "
                "a black turban-like khan dong headwrap, a long dark-brown traditional ao dai robe for men over "
                "black trousers, a faded cloth shoulder bag, a string of dark wooden prayer beads on his wrist. "
                "Serious, mysterious expression. " + STYLE_KIDS + ". Never white clothing.")},
    {"id": "co_ut_base", "kind": "character_base", "character": "co_ut", "name": "Cô Út (em gái út của bố)",
     "default_h": 0.58, "why": "cô Út về chịu tang ông (P1), lên ở với Khoa (P3)", "refs": [MOM_REF, BOY_REF],
     "design": ("Same art style as the reference images. A warm Vietnamese countryside woman in her early thirties, "
                "the boy's aunt: round friendly face, shoulder-length black hair tied in a short ponytail, a "
                "faded maroon long-sleeve blouse, dark navy trousers, plastic sandals, a small cloth bag. "
                + STYLE_KIDS + ". Never white clothing.")},

    # ---------------------------------------------------- sheet nhân vật mới (ĐỢT 2 — chờ base)
    {"id": "ong_noi_sheet_A", "kind": "sheet", "character": "ong_noi", "grid": [2, 3],
     "why": "P1: khắc đũa ngoài hiên, gõ đũa bữa cơm, giật lại chiếc đũa gãy, thức canh đồng hồ, kể chuyện, dúi đũa cho Khoa",
     "note": "Where the boy appears he is " + BOY + ".", "refs": [BOY_REF],
     "sprites": [
         {"name": "A1_sit_stool_carve", "pose": "sitting on a tiny low wooden stool, side view facing right, hunched over, "
          "carving letters into a thin bamboo chopstick with a small knife, a few bamboo sticks on his lap, calm focused face",
          "desc": "Ngồi ghế đẩu thấp khắc tên lên đũa tre bằng dao nhỏ (quay phải)", "tags": ["khắc đũa", "hiên"], "facing": "right"},
         {"name": "A2_sit_stool_tap_chopsticks", "pose": "sitting on a low wooden stool, side view facing left, a rice bowl "
          "in one hand, with his chopsticks gently tapping twice on the tips of another pair of chopsticks held out toward "
          "him from the left, warm loving smile (stool included)",
          "desc": "Ngồi ghế đẩu cầm bát, gõ đầu đũa (gõ vào tên trên đũa của Khoa), cười hiền (có ghế)",
          "tags": ["bữa cơm", "gõ đũa"], "facing": "left"},
         {"name": "A3_stand_snatch_broken", "pose": "standing, side view facing left, holding up a broken bamboo chopstick he "
          "just snatched, the other hand raised with one finger in warning, suddenly stern serious face",
          "desc": "Đứng giơ chiếc đũa gãy vừa giật lại, tay kia giơ ngón tay cảnh báo, mặt nghiêm", "tags": ["đũa gãy", "nghiêm"],
          "facing": "left"},
         {"name": "A4_sit_bed_watch_clock", "pose": f"at night, sitting upright on the edge of {BAMBOO_BED}, three-quarter view "
          "facing left, hands gripping his knees, staring up at something high on the wall with a tense, watchful face "
          "(bamboo bed included)",
          "desc": "Đêm, ngồi thẳng mép giường tre, nhìn lên tường (đồng hồ), căng thẳng canh giờ (có giường)",
          "tags": ["canh giờ", "đêm", "giường tre"], "facing": "left"},
         {"name": "A5_sit_tell_story", "pose": "sitting on a low wooden stool, front view, holding a rice bowl on his knee, "
          "looking far away with a serious haunted face, lips slightly open as if telling an old story (stool included)",
          "desc": "Ngồi ghế đẩu, nhìn xa xăm, nghiêm mặt kể chuyện cũ (có ghế)", "tags": ["kể chuyện"], "facing": "front"},
         {"name": "A6_give_chopsticks_boy", "pose": "TWO characters together: the grandfather sitting on a low stool on the "
          "left, pressing a pair of bamboo chopsticks into both hands of the boy standing on the right; the old man's hands "
          "tremble, gentle sad smile; the boy looks at the chopsticks curiously",
          "desc": "HAI nhân vật: ông ngồi ghế dúi đôi đũa vào tay Khoa (đứng bên phải), tay run, cười buồn",
          "tags": ["đũa dư", "ông cháu"], "facing": "right"},
     ]},
    {"id": "ong_noi_sheet_B", "kind": "sheet", "character": "ong_noi", "grid": [2, 3],
     "why": "P1: ho, nằm giường tre lúc hấp hối, mất (mắt hé mở), ngồi trước bàn thờ với bà, cận tay khắc đũa; P2–3: bóng ông",
     "note": ("Where the grandmother appears she is " + GMA + ". The bamboo bed must be EXACTLY the bed in the "
              "LAST attached image."), "refs": [GMA_REF, BAMBOO_BED_REF],
     "sprites": [
         {"name": "B1_bed_dying_grandma_hold", "pose": f"TWO characters together with {BAMBOO_BED}: the grandfather lying on his "
          "back on the bed, eyes closed, mouth open breathing heavily, very weak; the grandmother sits on a low stool beside "
          "the bed holding his hand in both of hers, worried face (side view, head of the bed on the left)",
          "desc": "HAI nhân vật + giường tre: ông nằm thở nặng nhọc, bà ngồi ghế cạnh nắm tay ông (đầu giường bên trái)",
          "tags": ["hấp hối", "giường tre"], "facing": "right"},
         {"name": "B2_bed_dead_eyes_open_grandma", "pose": f"TWO characters together with {BAMBOO_BED}, same layout as the "
          "previous pose: the grandfather lies completely still, peaceful face but his eyes are still half open staring "
          "upward-left; the grandmother leans over him crying, one hand gently over his eyes to close them",
          "desc": "HAI nhân vật + giường tre: ông đã mất, mắt còn hé mở; bà cúi khóc, đưa tay vuốt mắt ông",
          "tags": ["ông mất", "vuốt mắt"], "facing": "right"},
         {"name": "B3_back_sit_altar_with_grandma", "pose": "TWO characters seen completely from behind, sitting side by side "
          "on two low stools facing away from us (toward an altar that is not drawn), the grandmother on the right holding "
          "the grandfather's hand, both very still, heads slightly bowed",
          "desc": "HAI nhân vật quay lưng: ông bà ngồi cạnh nhau trước bàn thờ, bà nắm tay ông", "tags": ["bàn thờ", "lời hứa"],
          "facing": "away"},
         {"name": "B4_sit_stool_cough", "pose": "sitting hunched on a low stool, side view facing right, coughing hard into "
          "his fist, eyes squeezed shut, the other hand on his chest, thin and tired",
          "desc": "Ngồi ghế đẩu còng lưng ho vào nắm tay, tay kia ôm ngực", "tags": ["ho", "ốm"], "facing": "right"},
         {"name": "B5_closeup_hands_carve", "pose": "close-up filling the frame: two old wrinkled hands, one holding a thin "
          "bamboo chopstick, the other carving small letters into it with the tip of a small knife, bamboo shavings falling",
          "desc": "Cận đôi tay già khắc chữ lên chiếc đũa tre, vụn tre rơi", "tags": ["cận", "khắc đũa"], "facing": "right"},
         {"name": "B6_ghost_stand_still", "pose": "the grandfather as a ghost: standing perfectly still, slightly hunched, "
          "arms hanging limp, skin pale gray-blue (not white), eyes hidden in shadow, faint cold glow around his outline, "
          "front view",
          "desc": "Bóng ông (ma): đứng im, lưng hơi còng, tay buông thõng, da xám xanh, mắt chìm trong bóng tối",
          "tags": ["ma", "bóng ông"], "facing": "front"},
     ]},
    {"id": "thay_tu_sheet_A", "kind": "sheet", "character": "thay_tu", "grid": [2, 3],
     "why": "P1: lật lịch xem giờ, tái mặt, viết bùa, đặt bùa vào quan tài, quát, khấn quay lưng",
     "sprites": [
         {"name": "A1_sit_mat_almanac", "pose": "sitting cross-legged on a straw mat, side view facing right, an old open "
          "almanac book on his lap, counting on the fingertips of one hand, frowning",
          "desc": "Ngồi xếp bằng trên chiếu, lật lịch cũ, bấm đốt ngón tay (quay phải)", "tags": ["xem giờ"], "facing": "right"},
         {"name": "A2_sit_mat_pale", "pose": "same seated pose on the straw mat, but frozen, face drained pale, eyes wide, "
          "the counting hand stopped in mid-air",
          "desc": "Ngồi trên chiếu, đơ người, mặt tái mét, tay bấm đốt dừng giữa chừng", "tags": ["giờ trùng", "tái mặt"],
          "facing": "right"},
         {"name": "A3_write_talisman", "pose": "kneeling at a tiny low wooden table, side view facing right, writing red "
          "characters with a brush on a long yellow paper talisman, ink stone beside him, lips moving in prayer",
          "desc": "Quỳ bên bàn thấp viết bùa mực đỏ lên giấy vàng, miệng khấn", "tags": ["viết bùa"], "facing": "right"},
         {"name": "A4_place_talisman_bend", "pose": "standing bent forward at the waist, side view facing left, both hands "
          "reaching low in front of him placing a small folded yellow paper down carefully, solemn face",
          "desc": "Đứng cúi gập người đặt lá bùa gấp tư xuống thấp (vào quan tài)", "tags": ["đặt bùa"], "facing": "left"},
         {"name": "A5_stand_point_stern", "pose": "standing, side view facing left, pointing sharply forward with one finger, "
          "shouting a warning, stern angry eyebrows",
          "desc": "Đứng chỉ tay quát, mặt nghiêm khắc (quay trái)", "tags": ["quát", "dặn"], "facing": "left"},
         {"name": "A6_back_pray_incense", "pose": "standing seen completely from behind, holding three burning incense sticks "
          "raised in both hands before his face, head bowed, praying, thin smoke rising",
          "desc": "Đứng quay lưng, giơ ba nén nhang khấn lầm rầm", "tags": ["khấn", "quay lưng"], "facing": "away"},
     ]},
    {"id": "co_ut_sheet_A", "kind": "sheet", "character": "co_ut", "grid": [1, 3],
     "why": "P1: ôm Khoa; P3: gọi điện, nấu cơm hát", "note": "Where the boy appears he is " + BOY + ".", "refs": [BOY_REF],
     "sprites": [
         {"name": "A1_hug_boy", "pose": "TWO characters together: the aunt kneeling on one knee hugging the boy tightly, "
          "her eyes teary, the boy standing with his arms hanging, sad",
          "desc": "HAI nhân vật: cô Út quỳ một gối ôm chặt Khoa, rưng rưng", "tags": ["ôm", "chịu tang"], "facing": "right"},
         {"name": "A2_phone_worried", "pose": "standing, holding an old mobile phone to her ear, worried face, other hand on "
          "her chest, side view facing left",
          "desc": "Đứng nghe điện thoại, lo lắng (quay trái)", "tags": ["điện thoại"], "facing": "left"},
         {"name": "A3_cook_humming", "pose": "standing at an unseen stove, side view facing right, stirring a pot with a "
          "long ladle, humming happily with a soft smile",
          "desc": "Đứng khuấy nồi, ngân nga hát (quay phải)", "tags": ["nấu cơm", "bình yên"], "facing": "right"},
     ]},

    # ---------------------------------------------------- nhân vật có sẵn: sheet mới (ĐỢT 1)
    {"id": "mother_alive_sheet_E", "kind": "sheet", "character": "mother_alive", "grid": [2, 3],
     "why": "P1: ướm áo khoác cho Khoa, may máy, ôm bà khóc, cúi bên quan tài rơi nước mắt, ngủ gục ghế, ôm áo the ngoài hiên",
     "note": ("Where the boy appears he is " + BOY + ", and in pose 1 he wears a NEW dark black padded zip-up jacket over "
              "his green hoodie. Where the grandmother appears she is " + GMA + "." + SAME_JACKET),
     "refs": [BOY_REF, GMA_REF, JACKET_REF],
     "sprites": [
         {"name": "E1_fit_jacket_boy", "pose": "TWO characters together: the mother kneeling in front of the boy, zipping up "
          "the new black jacket she made for him to his chin, proud tender smile; the boy stands smiling shyly",
          "desc": "HAI nhân vật: mẹ quỳ kéo khoá chiếc áo khoác đen mới may cho Khoa, cười tự hào", "tags": ["áo khoác", "mẹ con"],
          "facing": "right"},
         {"name": "E2_sit_sewing_machine", "pose": "sitting on a low stool at an old black treadle sewing machine on a small "
          "wooden table, side view facing right, both hands guiding dark cloth under the needle, focused (machine and table included)",
          "desc": "Ngồi may bên máy khâu đạp chân cũ (có máy + bàn), quay phải", "tags": ["máy khâu"], "facing": "right"},
         {"name": "E3_hug_grandma_cry", "pose": "TWO characters together: the mother hugging the grandmother's shoulders "
          "from the side, crying; the grandmother stands still, head bowed, nodding quietly, looking at her own wrinkled hands",
          "desc": "HAI nhân vật: mẹ ôm chầm vai bà khóc, bà lặng lẽ cúi đầu nhìn đôi tay", "tags": ["khóc", "trùng tang"],
          "facing": "right"},
         {"name": "E4_bend_coffin_tear", "pose": "bending forward at the waist, side view facing left, both hands reaching low "
          "as if straightening someone's collar, shoulders trembling, a single visible tear falling from her cheek",
          "desc": "Cúi người chỉnh vạt áo (cho ông trong quan tài), vai run, một giọt nước mắt rơi", "tags": ["khâm liệm", "nước mắt"],
          "facing": "left"},
         {"name": "E5_sleep_armchair", "pose": "asleep slumped in an old wooden armchair, head tilted to one side, hands on her "
          "lap, exhausted, front view (armchair included)",
          "desc": "Thiếp đi trên ghế dựa gỗ, đầu nghiêng (có ghế)", "tags": ["ngủ gục", "kiệt sức"], "facing": "front"},
         {"name": "E6_sit_hug_old_shirt", "pose": "sitting on a low stool, side view facing right, hugging an old folded dark "
          "blue traditional ao the robe against her chest, staring blankly into the distance, empty grieving face",
          "desc": "Ngồi ghế đẩu ôm chiếc áo the cũ của ông, nhìn vô định (quay phải)", "tags": ["tang", "hiên"], "facing": "right"},
     ]},
    {"id": "mother_alive_sheet_F", "kind": "sheet", "character": "mother_alive", "grid": [1, 1],
     "why": "P1 vẽ lại E4 (Gemini vẽ mẹ chỉnh cổ áo cho Khoa): mẹ cúi xuống quan tài chỉnh vạt áo cho ông, rơi nước mắt",
     "sprites": [
         {"name": "F1_bend_into_coffin_tear", "pose": "ALONE, NO other person in the image: standing and bending deeply "
          "forward at the waist, side view facing LEFT, both arms reaching DOWN low in front of her toward something below "
          "the frame (an open coffin that is not drawn), hands at knee height as if straightening the collar of a person "
          "lying there, shoulders trembling, one visible tear falling from her cheek",
          "desc": "Một mình, cúi gập người (quay trái), hai tay với xuống thấp chỉnh vạt áo cho ông trong quan tài (không vẽ), một giọt nước mắt rơi",
          "tags": ["khâm liệm", "nước mắt"], "facing": "left"},
     ]},
    {"id": "grandma_sheet_K", "kind": "sheet", "character": "grandma", "grid": [2, 3],
     "why": "P1: chải tóc cho ông bên quan tài, xua mèo bằng chổi, tựa cửa run, gật đầu lặng lẽ, lau ống đũa, đặt bát lên bàn thờ",
     "sprites": [
         {"name": "K1_sit_comb_coffin", "pose": "sitting on a low stool, side view facing left, one arm raised forward at "
          "shoulder height holding a dark horn comb, gently combing (the coffin is not drawn), tender sad face, lips moving softly",
          "desc": "Ngồi ghế thấp, giơ lược sừng chải tóc (cho ông trong quan tài, quan tài không vẽ), thì thầm", "tags": ["chải tóc", "tang"],
          "facing": "left"},
         {"name": "K2_shoo_broom", "pose": "swinging a short straw broom forward to shoo something away, startled frightened "
          "face, side view facing right",
          "desc": "Vung chổi xua (con mèo), mặt hoảng (quay phải)", "tags": ["xua mèo", "chổi"], "facing": "right"},
         {"name": "K3_lean_back_door_tremble", "pose": "standing with her back pressed flat against a closed door (door edge "
          "drawn as a vertical line behind her), both hands trembling at her chest, eyes closed tight",
          "desc": "Đứng tựa lưng vào cửa, hai tay run trước ngực, nhắm mắt", "tags": ["run", "sợ"], "facing": "front"},
         {"name": "K4_nod_look_hands", "pose": "standing, head lowered, slowly nodding, looking down at her own open wrinkled "
          "hands, resigned as if she had expected this news for years, front view",
          "desc": "Đứng cúi đầu gật lặng lẽ, nhìn đôi bàn tay mình (như đã biết trước)", "tags": ["lặng lẽ", "biết trước"],
          "facing": "front"},
         {"name": "K5_wipe_chopstick_holder", "pose": "standing, side view facing left, wiping a bamboo chopstick holder full "
          "of chopsticks with a cloth, slow absent-minded movements, empty gaze",
          "desc": "Đứng lau đi lau lại ống đũa tre, mắt vô hồn (quay trái)", "tags": ["ống đũa", "tang"], "facing": "left"},
         {"name": "K6_raise_bowl_altar", "pose": "standing on tiptoe, side view facing left, both hands raising a full rice "
          "bowl with chopsticks laid across its rim up toward a high shelf (not drawn), solemn",
          "desc": "Kiễng chân nâng bát cơm (đũa gác ngang) đặt lên bàn thờ cao (quay trái)", "tags": ["bàn thờ", "bát cơm"],
          "facing": "left"},
     ]},
    {"id": "grandma_sheet_L", "kind": "sheet", "character": "grandma", "grid": [1, 1],
     "why": "P1 vẽ lại K1 (Gemini vẽ bà tự chải tóc mình): bà chải tóc cho ông nằm trong quan tài",
     "sprites": [
         {"name": "L1_comb_into_coffin", "pose": "sitting on a low stool, side view facing RIGHT, leaning forward, her right "
          "arm stretched FAR forward and DOWN at waist height holding a dark horn comb, combing the hair of someone lying "
          "in front of her below the frame (NOT her own hair, the comb is far away from her head), tender sad face looking "
          "down at that person, lips moving softly",
          "desc": "Ngồi ghế thấp quay phải, vươn tay xa về phía trước–xuống chải tóc cho ông nằm trong quan tài (không chải tóc mình)",
          "tags": ["chải tóc", "tang"], "facing": "right"},
     ]},
    {"id": "boy_hoodie_sheet_N", "kind": "sheet", "character": "boy_hoodie", "grid": [2, 3],
     "why": "P1 đêm canh linh cữu (áo khoác đen mẹ may): ngồi bó gối, quẹt diêm, nhặt lá bùa, kiễng nhìn quan tài, nhét bùa vào túi, lùi lại",
     "note": JACKET,
     "sprites": [
         {"name": "N1_sit_hug_knees_drowsy", "pose": "sitting on the floor hugging his knees, head nodding, eyelids half "
          "closed, fighting sleep, front view",
          "desc": "Áo khoác đen: ngồi bó gối dưới sàn, gà gật buồn ngủ", "tags": ["canh linh cữu", "buồn ngủ"], "facing": "front"},
         {"name": "N2_kneel_strike_match", "pose": "kneeling on the floor, side view facing right, striking a match on a small "
          "matchbox, a tiny flame lighting up his frightened face from below",
          "desc": "Áo khoác đen: quỳ quẹt diêm, ánh lửa nhỏ hắt lên mặt sợ hãi", "tags": ["quẹt diêm"], "facing": "right"},
         {"name": "N3_crouch_hold_talisman", "pose": "crouching, side view facing right, holding a small folded yellow paper "
          "in trembling fingers right in front of his face, eyes wide with horror, sweat drops",
          "desc": "Áo khoác đen: ngồi xổm cầm lá bùa vàng gấp tư run run, mắt trợn", "tags": ["lá bùa", "sợ"], "facing": "right"},
         {"name": "N4_tiptoe_peer_down", "pose": "standing on tiptoes, side view facing right, both hands gripping an edge in "
          "front of his chest (the coffin is not drawn), leaning forward peering down, terrified, holding a lit match",
          "desc": "Áo khoác đen: kiễng chân bám mép (quan tài), nghiêng người nhìn xuống, tay cầm que diêm", "tags": ["quan tài", "nhìn trộm"],
          "facing": "right"},
         {"name": "N5_stuff_pocket_guilty", "pose": "standing, front view, stuffing a small folded yellow paper into his "
          "jacket's front pocket, glancing sideways guiltily",
          "desc": "Áo khoác đen: nhét lá bùa vào túi áo, liếc ngang tội lỗi", "tags": ["giấu bùa", "tội lỗi"], "facing": "front"},
         {"name": "N6_step_back_frozen", "pose": "standing frozen, side view facing right, one foot stepping slowly backward, "
          "hands half raised, face pale and stiff with fear",
          "desc": "Áo khoác đen: đứng đơ, lùi một bước, mặt tái cứng", "tags": ["lùi lại", "sợ"], "facing": "right"},
     ]},
    {"id": "boy_hoodie_sheet_O", "kind": "sheet", "character": "boy_hoodie", "grid": [2, 3],
     "why": "P1 đám tang (áo xô màu be) + đời thường: ôm bát hương, chết lặng, quỳ lạy, ngước nhìn quạ, cầm đũa gãy, ngồi ăn trò chuyện",
     "note": MOURN,
     "sprites": [
         {"name": "O1_mourn_hold_incense_bowl", "pose": "MOURNING: standing front view, holding a brass incense bowl against "
          "his chest with both hands, eyes red, very sad",
          "desc": "Áo xô be: đứng ôm bát hương trước ngực, mắt đỏ", "tags": ["đưa tang", "bát hương"], "facing": "front"},
         {"name": "O2_mourn_frozen_pocket", "pose": "MOURNING: standing front view, one hand thrust deep into his pocket "
          "clutching something, frozen, pale, staring straight ahead in shock",
          "desc": "Áo xô be: đứng chết lặng, một tay thọc sâu trong túi siết chặt", "tags": ["chết lặng", "lá bùa"], "facing": "front"},
         {"name": "O3_hold_broken_chopstick", "pose": "in his normal hoodie: standing, side view facing right, holding the two "
          "halves of a broken bamboo chopstick over a small trash basket, guilty face",
          "desc": "Áo hoodie: cầm chiếc đũa gãy đôi định vứt vào sọt rác, mặt có lỗi", "tags": ["đũa gãy"], "facing": "right"},
         {"name": "O4_sit_stool_eat_chat", "pose": "in his normal hoodie: sitting on a low wooden stool, side view facing right, "
          "rice bowl and chopsticks in hand, chatting happily with his mouth open, cheerful (stool included)",
          "desc": "Áo hoodie: ngồi ghế đẩu ăn cơm, vừa ăn vừa kể chuyện vui (có ghế)", "tags": ["bữa cơm", "vui"], "facing": "right"},
         {"name": "O5_mourn_look_up", "pose": "MOURNING: standing, side view facing right, head tilted up looking at something "
          "high in a tree, uneasy frightened face",
          "desc": "Áo xô be: đứng ngước nhìn lên cao (con quạ), bất an", "tags": ["quạ", "nghĩa địa"], "facing": "right"},
         {"name": "O6_mourn_kneel_bow", "pose": "MOURNING: kneeling on a straw mat, side view facing left, hands pressed "
          "together, bowing his head low",
          "desc": "Áo xô be: quỳ trên chiếu chắp tay cúi lạy", "tags": ["tang lễ", "lạy"], "facing": "left"},
     ]},
    {"id": "boy_hoodie_sheet_P", "kind": "sheet", "character": "boy_hoodie", "grid": [1, 2],
     "why": "P1: nằm thao láo nắm áo khoác treo đầu giường; cất đôi đũa dư vào hộp nhỏ",
     "note": "The hanging black jacket and the chopsticks must match the attached images 3 and 4 exactly." ,
     "refs": [JACKET_REF, SPARE_REF],
     "sprites": [
         {"name": "P1_bed_awake_grip_jacket", "pose": "lying on his back in a simple low wooden bed with a dark blue blanket, "
          "eyes wide open staring at the ceiling, one arm reaching out gripping a black jacket hanging on a hook at the "
          "bed's head (bed, hook and jacket included), front view",
          "desc": "Nằm mắt mở thao láo, tay nắm chiếc áo khoác đen treo đầu giường (có giường)", "tags": ["giường", "mất ngủ"],
          "facing": "front"},
         {"name": "P2_sit_put_chopsticks_box", "pose": "sitting on the floor, side view facing right, carefully putting a pair "
          "of bamboo chopsticks into a small cardboard box, an open school backpack beside him",
          "desc": "Ngồi bệt cất đôi đũa dư vào chiếc hộp nhỏ, cặp sách mở bên cạnh", "tags": ["đũa dư", "hộp"], "facing": "right"},
     ]},

    # ---------------------------------------------------- đạo cụ (ĐỢT 1)
    {"id": "props_sheet_LB", "kind": "sheet", "character": "props", "grid": [2, 3],
     "why": "lá bùa, đôi đũa khắc tên (của Khoa, đôi dư khắc kín bốn mặt), đũa gãy, ống đũa",
     "sprites": [
         {"name": "LB1_talisman_folded", "pose": "a small rectangle of yellow paper folded in four, red ink marks showing "
          "through, slightly crumpled", "desc": "Lá bùa giấy vàng gấp tư, lộ vết mực đỏ", "tags": ["lá bùa"], "facing": "front"},
         {"name": "LB2_talisman_open", "pose": "a long yellow paper talisman unfolded flat, covered with wriggling red ink "
          "characters and a red seal stamp", "desc": "Lá bùa mở ra: chữ mực đỏ ngoằn ngoèo, dấu triện đỏ", "tags": ["lá bùa"],
          "facing": "front"},
         {"name": "LB3_chopsticks_named", "pose": "a pair of plain bamboo chopsticks lying diagonally, simple dark carved "
          "letters burned into the top of each stick, neat slanted carving", "desc": "Đôi đũa tre khắc tên (nét nghiêng, gọn)",
          "tags": ["đũa khắc tên"], "facing": "front"},
         {"name": "LB4_chopsticks_spare_carved", "pose": "a pair of bamboo chopsticks lying diagonally, shaky uneven dark "
          "letters carved all along every side of both sticks, clumsy trembling carving", "desc": "Đôi đũa dư: chữ khắc run run kín cả bốn mặt",
          "tags": ["đũa dư"], "facing": "front"},
         {"name": "LB5_chopstick_broken", "pose": "one bamboo chopstick snapped into two pieces with splintered ends",
          "desc": "Chiếc đũa tre gãy đôi, đầu gãy tua", "tags": ["đũa gãy"], "facing": "front"},
         {"name": "LB6_chopstick_holder", "pose": "a tall bamboo chopstick holder tube filled with several pairs of bamboo "
          "chopsticks, each with small carved letters on top", "desc": "Ống đũa tre cắm nhiều đôi đũa khắc tên",
          "tags": ["ống đũa"], "facing": "front"},
     ]},
    {"id": "props_sheet_LC", "kind": "sheet", "character": "props", "grid": [2, 3],
     "why": "bát cơm cúng đũa gác ngang (nguội / còn bốc khói), gương phủ vải đỏ, đồng hồ quả lắc 3 giờ, áo khoác đen treo, lịch cũ",
     "note": "Pose 5 (the hanging jacket) must be EXACTLY the black jacket worn by the boy in attached image 2.",
     "refs": [JACKET_REF],
     "sprites": [
         {"name": "LC1_bowl_full_chopsticks_across", "pose": "a ceramic rice bowl filled to a pressed dome with white rice, a "
          "pair of bamboo chopsticks laid neatly across the rim", "desc": "Bát cơm xới đầy nén chặt, đôi đũa gác ngang miệng bát",
          "tags": ["bát cơm", "bàn thờ"], "facing": "front"},
         {"name": "LC2_bowl_steaming_chopsticks_across", "pose": "the same rice bowl with chopsticks across the rim, the rice "
          "freshly steaming with thick white curls of steam", "desc": "Bát cơm còn bốc khói nghi ngút, đũa gác ngang",
          "tags": ["bát cơm", "nóng"], "facing": "front"},
         {"name": "LC3_mirror_red_cloth", "pose": "a rectangular wall mirror in a dark wooden frame completely covered by a "
          "draped red cloth hanging down", "desc": "Gương treo tường phủ kín tấm vải đỏ", "tags": ["gương", "kiêng"],
          "facing": "front"},
         {"name": "LC4_wall_clock_three", "pose": "an old wooden wall pendulum clock, round face with Roman numerals, hands "
          "pointing at exactly three o'clock, brass pendulum below", "desc": "Đồng hồ quả lắc treo tường chỉ đúng 3 giờ",
          "tags": ["đồng hồ", "3 giờ"], "facing": "front"},
         {"name": "LC5_black_jacket_hanging", "pose": "a dark black padded zip-up jacket hanging on a wall hook, two deep "
          "front pockets", "desc": "Chiếc áo khoác đen (mẹ may) treo trên móc", "tags": ["áo khoác"], "facing": "front"},
         {"name": "LC6_lunar_almanac", "pose": "an old open lunar almanac book with yellowed pages, grids of small "
          "characters and red marks", "desc": "Cuốn lịch âm cũ mở ra, giấy ố vàng", "tags": ["lịch", "xem giờ"], "facing": "front"},
     ]},
    {"id": "props_sheet_LD", "kind": "sheet", "character": "props", "grid": [2, 4],
     "why": "con quạ đen: đậu, kêu, nghiêng đầu nhìn xuống, xoè cánh đáp; chu kỳ bay 4 khung",
     "note": ("This whole sheet is ONE black crow (dark blue-black feathers, sharp beak, small shiny eye) in the same "
              "crayon style, same size in every pose, side view facing right unless stated."),
     "cycles": {"crow_fly": ["LD5_crow_fly_1", "LD6_crow_fly_2", "LD7_crow_fly_3", "LD8_crow_fly_4"]},
     "sprites": [
         {"name": "LD1_crow_perched", "pose": "perched still on a short bare branch stub (included), looking ahead",
          "desc": "Quạ đậu im trên mẩu cành", "tags": ["quạ"], "facing": "right"},
         {"name": "LD2_crow_caw", "pose": "perched, beak wide open cawing, neck stretched", "desc": "Quạ đậu, há mỏ kêu",
          "tags": ["quạ", "kêu"], "facing": "right"},
         {"name": "LD3_crow_look_down", "pose": "perched, head tilted far down looking at the ground below, one eye "
          "glinting", "desc": "Quạ nghiêng đầu nhìn xuống", "tags": ["quạ"], "facing": "right"},
         {"name": "LD4_crow_land", "pose": "landing, wings spread wide, legs forward", "desc": "Quạ xoè cánh đáp xuống",
          "tags": ["quạ"], "facing": "right"},
         {"name": "LD5_crow_fly_1", "pose": "flying cycle frame 1 of 4: wings fully up", "desc": "Quạ bay 1/4 (cánh lên)",
          "tags": ["quạ", "bay"], "facing": "right"},
         {"name": "LD6_crow_fly_2", "pose": "flying cycle frame 2 of 4: wings level spread wide", "desc": "Quạ bay 2/4",
          "tags": ["quạ", "bay"], "facing": "right"},
         {"name": "LD7_crow_fly_3", "pose": "flying cycle frame 3 of 4: wings fully down", "desc": "Quạ bay 3/4 (cánh xuống)",
          "tags": ["quạ", "bay"], "facing": "right"},
         {"name": "LD8_crow_fly_4", "pose": "flying cycle frame 4 of 4: wings half folded rising", "desc": "Quạ bay 4/4",
          "tags": ["quạ", "bay"], "facing": "right"},
     ]},
    {"id": "props_sheet_LE", "kind": "sheet", "character": "props", "grid": [2, 3],
     "why": "hộp nhỏ cất đũa dư (đóng / mở có đũa / mở chỉ còn đất đỏ — P3), bao diêm, búa đinh quan tài, nắm gạo + đồng xu",
     "note": "The chopsticks inside the box in pose 2 must be EXACTLY the shaky-carved chopsticks in attached image 2.",
     "refs": [SPARE_REF],
     "sprites": [
         {"name": "LE1_box_closed_rubberband", "pose": "a small worn cardboard box, lid closed, a rubber band wrapped around "
          "it", "desc": "Hộp giấy nhỏ đậy nắp, quấn dây chun", "tags": ["hộp", "đũa dư"], "facing": "front"},
         {"name": "LE2_box_open_chopsticks", "pose": "the same small box with the lid open, a pair of bamboo chopsticks with "
          "shaky carved letters lying inside", "desc": "Hộp mở, bên trong là đôi đũa dư khắc run run", "tags": ["hộp", "đũa dư"],
          "facing": "front"},
         {"name": "LE3_box_open_red_soil", "pose": "the same small box open, NO chopsticks inside, only a small damp heap of "
          "dark red earth", "desc": "Hộp mở, không còn đũa, chỉ còn nhúm đất đỏ ẩm (P3)", "tags": ["hộp", "đất đỏ"], "facing": "front"},
         {"name": "LE4_matchbox_lit_match", "pose": "a small old matchbox and one burning match with a tiny bright flame",
          "desc": "Bao diêm cũ và que diêm đang cháy", "tags": ["diêm"], "facing": "front"},
         {"name": "LE5_hammer_coffin_nails", "pose": "an old wooden-handled hammer and three long rusty iron nails",
          "desc": "Búa cán gỗ và mấy chiếc đinh dài gỉ (đóng quan tài)", "tags": ["đóng quan tài"], "facing": "front"},
         {"name": "LE6_rice_coins_saucer", "pose": "a small saucer with a pinch of white rice and three old coins",
          "desc": "Đĩa nhỏ có nhúm gạo và ba đồng xu (khâm liệm)", "tags": ["khâm liệm"], "facing": "front"},
     ]},

    # ---------------------------------------------------- phông nền
    {"id": "bgL1_porch_day", "kind": "background", "refs": ["assets/backgrounds/bg7d_front_yard_morning.png"],
     "why": "P1: ông khắc đũa ngoài hiên, gãy đũa, dúi đũa dư, ông ho",
     "scene": ("IMPORTANT: this is a warm LATE-AFTERNOON image with soft golden sunlight, ignore the night lighting "
               "described above; match the daylight crayon look of attached image 2. The front porch of a narrow old Vietnamese tube house: worn tiled porch floor across "
               "the lower third, an old wooden double door half open on the far left, a faded yellow wall, on the right "
               "a small front yard with a big old pomelo tree heavy with round green fruit, a low brick wall and a small "
               "iron gate behind it, long soft shadows. Empty porch floor in the lower third."),
     "desc": "Hiên nhà ống chiều nắng vàng: cửa gỗ bên trái, nền gạch, cây bưởi già sai quả bên phải, tường rào thấp",
     "tags": ["hiên", "cây bưởi", "chiều"], "floor_y": 0.93, "char_h": 0.46,
     "hotspots_needed": ["stool_spot", "door", "pomelo_tree"]},
    {"id": "bgL1n_porch_night", "kind": "background", "refs": ["assets/backgrounds/bgL1_porch_day.png"],
     "why": "P1: mẹ ôm áo the ngoài hiên đêm sau đám tang; P3: Khoa ngồi hiên",
     "scene": ("The SAME porch as attached image 2 (same layout: wooden door left, tiled floor, pomelo tree right, low "
               "wall and gate) but at NIGHT: deep blue darkness, faint cold moonlight through the pomelo leaves, a dim "
               "yellow light from the half-open door. Empty porch floor in the lower third."),
     "desc": "Hiên nhà (cùng bố cục bgL1) ban đêm, ánh trăng qua lá bưởi, đèn vàng hắt ra từ cửa",
     "tags": ["hiên", "cây bưởi", "đêm"], "floor_y": 0.93, "char_h": 0.46,
     "hotspots_needed": ["stool_spot", "door", "pomelo_tree"]},
    {"id": "bgL8_house_alley_dusk", "kind": "background", "refs": ["assets/backgrounds/bg7_front_yard.png"],
     "why": "P1 cảnh mở: căn nhà ống cuối hẻm",
     "scene": ("IMPORTANT: DUSK, the sky deep orange fading to blue, ignore the night lighting described above. A narrow "
               "Vietnamese town alley seen from its entrance, small tube houses on both sides with tangled electric wires; "
               "at the far dead end of the alley, a narrow old two-storey tube house with a faded mossy tiled roof and a "
               "big old pomelo tree leaning over its low front wall, one warm yellow window lit. Empty alley ground in "
               "the lower third."),
     "desc": "Con hẻm lúc chạng vạng, cuối hẻm là căn nhà ống mái rêu với cây bưởi già, một ô cửa sáng đèn",
     "tags": ["hẻm", "nhà ống", "chạng vạng"], "floor_y": 0.95, "char_h": 0.3, "hotspots_needed": ["house", "alley_floor"]},
    {"id": "bgL6_old_village_altar_sepia", "kind": "background", "refs": ["assets/backgrounds/bg4_main_room.png"],
     "why": "P1 hồi ức: nhà bị trùng tang ở làng cũ, bàn thờ có thêm bát cơm",
     "scene": ("IMPORTANT: this is a faded old MEMORY image in brownish sepia tones, ignore the blue night lighting "
               "described above. Inside an old wooden village house with dark beams and a packed earth floor: a long "
               "wooden altar table against the back wall with several faded portraits, incense smoke, and a row of FOUR "
               "rice bowls with chopsticks laid across, the fourth bowl slightly apart from the others; a wooden door "
               "ajar with village children peeking in from outside as tiny silhouettes. Empty floor in the lower third."),
     "desc": "Hồi ức (tông nâu sepia): nhà gỗ làng cũ, bàn thờ dài nhiều di ảnh, hàng bốn bát cơm, trẻ con ló nhìn qua cửa",
     "tags": ["hồi ức", "làng cũ", "trùng tang"], "floor_y": 0.95, "char_h": 0.46,
     "hotspots_needed": ["bowls", "fourth_bowl", "door"]},
    {"id": "bgL2_wake_coffin", "kind": "background", "refs": [PORTRAIT_BG, "assets/backgrounds/bg4_main_room.png"],
     "why": "P1: gian thờ đặt linh cữu ông (3 ngày tang, đêm canh linh cữu)",
     "scene": ("The main room of a small Vietnamese tube house turned into a funeral wake at night: a dark lacquered "
               "wooden coffin with its LID OFF (the lid leaning against the right wall) rests on two wooden trestles "
               "across the center, head end on the left; behind it a funeral altar table with the SAME framed portrait "
               "of the old man as in attached image 2 (room style like attached image 3), two tall red candles, a brass incense bowl with smoke, "
               "paper wreaths on stands, a beige mourning cloth hanging above; a straw mat on the floor in front. "
               "Empty floor in the lower third."),
     "desc": "Gian thờ đám tang ban đêm: quan tài gỗ mở nắp (nắp dựng tường phải) đặt giữa, đầu bên trái; bàn thờ có di ảnh ông, 2 nến, vòng hoa giấy; chiếu trước",
     "tags": ["đám tang", "linh cữu", "đêm"], "floor_y": 0.95, "char_h": 0.42,
     "hotspots_needed": ["coffin_head", "coffin_foot", "coffin_rim_y", "portrait", "candle_left", "mat"]},
    {"id": "bgL2c_wake_coffin_closed", "kind": "background", "refs": ["assets/backgrounds/bgL2_wake_coffin.png"],
     "why": "P1: sáng đưa tang, nắp quan tài đã đóng đinh",
     "scene": ("The SAME funeral wake as attached image 2 (same layout) but on the funeral MORNING in dim gray daylight: "
               "the coffin LID IS NOW CLOSED and nailed shut, a red-and-gold funeral cloth draped over it, the candles lit. "
               "Empty floor in the lower third."),
     "desc": "Gian thờ (cùng bố cục bgL2) sáng đưa tang: nắp quan tài đã đóng đinh, phủ khăn đỏ vàng",
     "tags": ["đám tang", "đóng nắp"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["coffin_head", "coffin_lid"]},
    {"id": "bgL3a_coffin_top_hands_chest", "kind": "background", "refs": [PORTRAIT_BG, ONG_BASE, COFFIN_REF],
     "why": "P1: cận nhìn từ trên xuống trong quan tài — ông nằm, tay đặt ngực, lá bùa dưới gối",
     "scene": ("A top-down close-up looking straight down into an open dark wooden coffin at night, candlelight: the old "
               "grandfather (face exactly as the portrait in attached image 2, same man as attached image 3) lies peacefully on his back inside the SAME coffin as attached image 4 (same wood and lining), eyes closed, wearing a dark blue "
               "traditional ao the robe, both hands folded neatly on his chest; plain rice paper sheets lining the coffin; "
               "his head rests on a small pillow, and a corner of a folded yellow paper talisman peeks out from under the "
               "pillow. The face is clearly the man from the portrait."),
     "desc": "Cận từ trên xuống trong quan tài: ông nằm, áo the, hai tay đặt trên ngực, góc lá bùa vàng ló dưới gối",
     "tags": ["quan tài", "cận", "lá bùa"], "floor_y": 0.95, "char_h": 0.4,
     "hotspots_needed": ["face", "right_hand", "pillow_talisman"]},
    {"id": "bgL3b_coffin_top_hand_dropped", "kind": "background", "refs": ["assets/backgrounds/bgL3a_coffin_top_hands_chest.png"],
     "why": "P1: cùng cận quan tài nhưng tay phải ông buông thõng cạnh gối, lá bùa đã mất — ánh que diêm",
     "scene": ("EXACTLY the same top-down coffin close-up as attached image 2 (same framing, same face) but now lit only "
               "by the small warm flicker of a single match from below the frame, deep shadows: the old man's RIGHT hand "
               "is no longer on his chest, it has slipped down beside the pillow, fingers slightly curled as if they just "
               "pushed something out; NO talisman under the pillow any more; the corners of his mouth curve up very "
               "slightly into the faintest smile."),
     "desc": "Cùng cận quan tài (ánh que diêm): tay phải ông buông thõng cạnh gối, ngón co, lá bùa đã mất, khoé miệng hơi nhếch",
     "tags": ["quan tài", "cận", "rợn"], "floor_y": 0.95, "char_h": 0.4,
     "hotspots_needed": ["face", "dropped_hand", "pillow"]},
    {"id": "bgL4_procession_field", "kind": "background", "refs": ["assets/backgrounds/bg7d_front_yard_morning.png"],
     "why": "P1: đoàn đưa tang đi qua cánh đồng gặt, giấy tiền bay",
     "scene": ("IMPORTANT: overcast gray DAYTIME, ignore the night lighting described above; small far-away people ARE "
               "allowed in this image. A wide view of harvested rice fields with stubble under a heavy gray sky; along a "
               "narrow raised dirt path in the middle distance walks a small Vietnamese funeral procession: tiny figures "
               "in beige mourning gauze, a coffin carried on bamboo poles under a red-and-gold canopy, white and gold "
               "funeral banners, pale paper money fluttering in the wind; a line of bamboo and a far village behind. "
               "Empty field in the lower third."),
     "desc": "Đoàn đưa tang nhỏ xa đi trên bờ ruộng gặt trơ gốc, trời âm u, giấy tiền bay",
     "tags": ["đưa tang", "cánh đồng"], "floor_y": 0.95, "char_h": 0.3, "hotspots_needed": ["procession"]},
    {"id": "bgL5_cemetery_burial_day", "kind": "background", "refs": ["assets/backgrounds/bg7d_front_yard_morning.png"],
     "why": "P1: hạ huyệt, con quạ trên cây gạo khô",
     "scene": ("IMPORTANT: overcast gray DAYTIME, ignore the night lighting described above. A small rural Vietnamese "
               "field cemetery: old graves and weathered tombstones scattered in the grass, in the center an open fresh "
               "grave pit with a dark coffin lowered inside, a mound of dark RED earth and two shovels beside it, incense "
               "sticks in the ground; on the right a tall dry leafless kapok tree (cay gao) with crooked bare branches "
               "against the gray sky. No people. Empty ground in the lower third."),
     "desc": "Nghĩa địa ngoài đồng ban ngày âm u: huyệt mới đào có quan tài, đống đất đỏ, xẻng; cây gạo khô trụi lá bên phải",
     "tags": ["nghĩa địa", "hạ huyệt", "cây gạo"], "floor_y": 0.95, "char_h": 0.42,
     "hotspots_needed": ["grave_pit", "dirt_mound", "crow_branch"]},

    # ================================================= GÓP Ý PREVIEW 1 (2026-10-31)
    {"id": "ong_noi_sheet_D", "kind": "sheet", "character": "ong_noi", "grid": [1, 2],
     "why": "giờ Dần (#34): ông NẰM thức canh giờ trên giường tre, thiếp đi rồi giật mình — thay cho ông ngồi canh (A4)",
     "note": ("The bamboo bed must be EXACTLY the bed in the LAST attached image, head of the bed on the LEFT, the whole bed "
              "drawn in both poses, same size. Night, the grandfather alone (no other person). Full body, never cropped."),
     "refs": [BAMBOO_BED_REF],
     "sprites": [
         {"name": "D1_bed_lie_side_watch_clock", "pose": "lying in the bamboo bed under a thin blanket, head on the pillow at the "
          "left. IMPORTANT: we look at the bed from the FRONT and the clock hangs high on the wall BEHIND the bed, on the far side "
          "away from us, so he TWISTS his head BACKWARD over his shoulder, neck craned, chin raised, looking UP and AWAY from us at "
          "that wall (clock not drawn): we see the BACK and side of his silver head and only the edge of his cheek and one tired "
          "open eye (three-quarter rear view of the head), his body still lying toward us",
          "desc": "Đêm, nằm nghiêng trên giường tre (đầu giường bên trái), mặt hướng người xem, mắt mở thao láo ngước lên (đồng hồ)",
          "tags": ["giờ Dần", "thức canh", "giường tre"], "facing": "right"},
         {"name": "D2_bed_jolt_awake", "pose": "on the same bamboo bed, he has just JOLTED awake from a doze: pushing himself "
          "up on one elbow, head and shoulders turned sharply BACKWARD and AWAY from us toward the wall BEHIND the bed to check the "
          "clock high up there (not drawn), three-quarter rear view: we see the back of his head and his raised shoulder, one "
          "wide frightened eye at the edge of his face, the blanket slipping off",
          "desc": "Ngồi bật dậy trên giường tre, quay lưng nửa người, ngoái nhìn sang phải lên tường (đồng hồ), mặt hốt hoảng; chăn tuột",
          "tags": ["giờ Dần", "giật mình", "giường tre"], "facing": "right"},
     ]},
    {"id": "ong_noi_sheet_C", "kind": "sheet", "character": "ong_noi", "grid": [2, 2],
     "why": "góp ý #17 #20-23 #41: ông đứng đủ chân giật đũa gãy, ngồi ghế ăn cơm / kể chuyện (không kèm bàn, tỉ lệ nhỏ), nằm nhắm mắt",
     "note": ("Where the grandmother appears she is " + GMA + ". The bamboo bed must be EXACTLY the bed in the LAST attached "
              "image. Full body, never cropped."), "refs": [GMA_REF, BAMBOO_BED_REF],
     "sprites": [
         {"name": "C1_stand_snatch_broken_full", "pose": "FULL BODY from head to feet: standing, side view facing left, holding "
          "up a broken bamboo chopstick he just snatched, the other hand raised with one finger in warning, suddenly stern face",
          "desc": "Đứng ĐỦ CHÂN (quay trái) giơ chiếc đũa gãy vừa giật lại, tay kia giơ ngón tay cảnh báo, mặt nghiêm",
          "tags": ["đũa gãy", "nghiêm"], "facing": "left"},
         {"name": "C2_sit_stool_eat_side", "pose": "sitting on a tiny low wooden stool, side view facing left, a rice bowl in "
          "one hand, chopsticks in the other gently tapping the bowl, warm smile, NO table (stool included)",
          "desc": "Ngồi ghế đẩu thấp (quay trái) cầm bát, gõ đũa, cười hiền — không kèm bàn (có ghế)", "tags": ["bữa cơm"],
          "facing": "left"},
         {"name": "C3_sit_stool_tell_story_side", "pose": "sitting on a tiny low wooden stool, three-quarter view facing left, "
          "rice bowl resting on his knee, looking far away with a serious haunted face, lips open telling an old story, NO table",
          "desc": "Ngồi ghế đẩu thấp (quay trái), bát đặt trên gối, nhìn xa xăm kể chuyện cũ — không kèm bàn", "tags": ["kể chuyện"],
          "facing": "left"},
         {"name": "C4_bed_eyes_closed_grandma_cry", "pose": "TWO characters with the bamboo bed, same layout as the bed in the "
          "last image (head of the bed on the left): the grandfather lies still on his back, eyes FULLY CLOSED, peaceful; the "
          "grandmother sits on a low stool beside the bed crying, one hand resting on his chest",
          "desc": "HAI nhân vật + giường tre: ông nằm nhắm hẳn mắt, bà ngồi cạnh khóc, tay đặt lên ngực ông",
          "tags": ["ông mất", "nhắm mắt"], "facing": "right"},
     ]},
    {"id": "mother_alive_sheet_G", "kind": "sheet", "character": "mother_alive", "grid": [2, 2],
     "why": "góp ý #20-22 #43-47 #52 #59-60: mẹ ngồi ăn quay lưng, đứng lo lắng, quỳ chiếu lo lắng, cúi vào quan tài nhìn từ sau lưng",
     "sprites": [
         {"name": "G1_sit_stool_eat_back", "pose": "seen completely from BEHIND: sitting on a tiny low wooden stool facing away "
          "from us, eating, a rice bowl raised in front of her (stool included)",
          "desc": "Ngồi ghế đẩu QUAY LƯNG về người xem, đang ăn cơm (có ghế)", "tags": ["bữa cơm", "quay lưng"], "facing": "away"},
         {"name": "G2_stand_worried", "pose": "standing, front view, both hands clasped tightly at her chest, worried frightened face",
          "desc": "Đứng chính diện, hai tay nắm chặt trước ngực, lo sợ", "tags": ["lo lắng"], "facing": "front"},
         {"name": "G3_kneel_mat_worried", "pose": "kneeling sitting back on her heels on the floor, side view facing right, hands "
          "on her lap, listening with a worried pale face",
          "desc": "Quỳ ngồi trên gót (quay phải), tay đặt trên đùi, lo lắng lắng nghe", "tags": ["lo lắng", "chiếu"], "facing": "right"},
         {"name": "G4_topdown_back_lean", "pose": "seen from ABOVE and BEHIND (bird's-eye view from behind her): we see the back "
          "of her head with the low bun, her shoulders and the beige cardigan, both arms reaching forward and down as if leaning "
          "over an open coffin to straighten someone's collar; only head, shoulders and arms, cut at the waist",
          "desc": "Nhìn từ TRÊN và SAU LƯNG: gáy (búi tóc), vai, hai tay vươn xuống chỉnh áo (đặt ở mép dưới khung quan tài nhìn từ trên)",
          "tags": ["khâm liệm", "từ trên"], "facing": "away"},
     ]},
    {"id": "thay_tu_sheet_B", "kind": "sheet", "character": "thay_tu", "grid": [1, 3],
     "why": "góp ý #54 #56: gấp tờ giấy làm tư (không phải phong bì), quát nhìn từ trên xuống, đặt mảnh giấy gấp tư",
     "sprites": [
         {"name": "B1_fold_paper_four", "pose": "standing, front view, holding a square sheet of yellow paper with red ink in "
          "both hands, folding it in half and in half again into a small square (folded in four, NOT an envelope)",
          "desc": "Đứng gấp tờ giấy vàng mực đỏ làm tư thành ô vuông nhỏ (không phải phong bì)", "tags": ["gấp bùa"], "facing": "front"},
         {"name": "B2_topdown_lean_point", "pose": "seen from ABOVE (bird's-eye view): leaning forward over something below from "
          "the far side, head and shoulders foreshortened toward us, one arm pointing sharply down, shouting angrily",
          "desc": "Nhìn từ TRÊN xuống: thầy chồm người từ phía bên kia, chỉ tay xuống, quát (đặt ở mép trên khung quan tài)",
          "tags": ["quát", "từ trên"], "facing": "front"},
         {"name": "B3_place_folded_square", "pose": "bending forward, side view facing left, carefully pushing a SMALL folded "
          "yellow square of paper under a pillow that is not drawn, hands low, solemn",
          "desc": "Cúi người (quay trái) nhét mảnh giấy vàng gấp tư nhỏ xuống dưới gối (gối không vẽ)", "tags": ["đặt bùa"],
          "facing": "left"},
     ]},
    {"id": "grandma_sheet_M", "kind": "sheet", "character": "grandma", "grid": [1, 2],
     "why": "góp ý #68 #43-45: bà ngủ gục bên chiếc bàn nhỏ, bà quỳ chiếu lo lắng",
     "sprites": [
         {"name": "M1_slump_asleep_table", "pose": "sitting on a low stool, slumped forward asleep with her head resting on her "
          "folded arms on a small low wooden table (table included), side view facing right, exhausted",
          "desc": "Ngồi ghế thấp gục đầu lên tay ngủ bên chiếc bàn nhỏ (có bàn), quay phải", "tags": ["ngủ gục", "kiệt sức"],
          "facing": "right"},
         {"name": "M2_kneel_mat_worried", "pose": "kneeling sitting back on her heels, side view facing right, hands clasped "
          "on her lap, worried face, listening",
          "desc": "Quỳ ngồi trên gót (quay phải), tay đan trên đùi, lo lắng", "tags": ["lo lắng", "chiếu"], "facing": "right"},
     ]},
    {"id": "boy_hoodie_sheet_Q", "kind": "sheet", "character": "boy_hoodie", "grid": [1, 3],
     "why": "góp ý #61 #40 #43-45: quỳ lạy quay lưng về bàn thờ (áo xô), đứng đơ bịt miệng ở cửa, quỳ chiếu lo lắng",
     "note": MOURN,
     "sprites": [
         {"name": "Q1_mourn_kneel_back", "pose": "MOURNING: kneeling seen completely from BEHIND, facing away toward an altar "
          "that is not drawn, hands pressed together in prayer, head bowed",
          "desc": "Áo xô be: quỳ QUAY LƯNG về người xem, hướng về bàn thờ, chắp tay cúi đầu", "tags": ["tang lễ", "quay lưng"],
          "facing": "away"},
         {"name": "Q2_frozen_hands_mouth", "pose": "in his normal hoodie: standing frozen, side view facing left, both hands "
          "pressed over his mouth, eyes wide with shock, knees slightly bent",
          "desc": "Áo hoodie: đứng đơ người (quay trái), hai tay bịt miệng, mắt trợn", "tags": ["sốc", "ông mất"], "facing": "left"},
         {"name": "Q3_kneel_mat_worried", "pose": "in his normal hoodie: kneeling sitting back on his heels, side view facing "
          "right, hands on his knees, scared worried face, listening",
          "desc": "Áo hoodie: quỳ ngồi trên gót (quay phải), lo sợ lắng nghe", "tags": ["lo lắng", "chiếu"], "facing": "right"},
     ]},
    {"id": "props_sheet_LF", "kind": "sheet", "character": "props", "grid": [1, 4],
     "why": "góp ý #1 #19 #35 #46 #101: bát cơm cắm đũa thẳng đứng (nguội / bốc khói), đũa khắc rõ chữ KHOA, đôi đũa dư khắc KHOA run run kín bốn mặt",
     "sprites": [
         {"name": "LF1_bowl_chopsticks_upright", "pose": "a plain ceramic rice bowl filled with a pressed dome of white rice, a "
          "pair of bamboo chopsticks stuck STRAIGHT UP vertically in the center of the rice, side view",
          "desc": "Bát cơm xới đầy, đôi đũa CẮM THẲNG ĐỨNG giữa bát", "tags": ["bát cơm", "bàn thờ"], "facing": "front"},
         {"name": "LF2_bowl_upright_steaming", "pose": "the same bowl with chopsticks stuck straight up in the rice, thick curls "
          "of steam rising from the hot rice", "desc": "Bát cơm cắm đũa đứng, còn bốc khói", "tags": ["bát cơm", "nóng"],
          "facing": "front"},
         {"name": "LF3_chopsticks_khoa", "pose": "a pair of plain bamboo chopsticks lying diagonally, each with the four capital "
          "letters K H O A clearly carved and darkened near the top, neat slanted letters", "desc": "Đôi đũa tre khắc rõ chữ KHOA, nét nghiêng gọn",
          "tags": ["đũa khắc tên"], "facing": "front"},
         {"name": "LF4_chopsticks_spare_khoa", "pose": "a pair of bamboo chopsticks lying diagonally, the word KHOA carved again "
          "and again all along every side of both sticks in shaky, trembling, uneven letters", "desc": "Đôi đũa dư: chữ KHOA khắc run run lặp kín bốn mặt",
          "tags": ["đũa dư"], "facing": "front"},
     ]},
    {"id": "bgL10_altar_four_portraits", "kind": "background", "refs": [PORTRAIT_BG, ONG_BASE, MOM_PORTRAIT, GMA_REF],
     "why": "góp ý #1/#2: bàn thờ có 4 di ảnh (ông, mẹ, bà, khung thứ tư phủ vải đen)",
     "scene": ("A close-up of a family altar at night in the same style and framing as attached image 2: on the dark wooden altar "
               "stand FOUR framed portraits side by side in a row: 1) the old grandfather from attached image 3, 2) the mother from "
               "attached image 4, 3) the grandmother from attached image 5 — all as black-and-white portrait photos with black "
               "mourning ribbons — and 4) a fourth frame on the far right completely covered by a draped BLACK cloth so nothing "
               "can be seen. A brass incense bowl with smoke, two red candles, the wooden front of the altar empty for rice bowls."),
     "desc": "Bàn thờ đêm có 4 di ảnh: ông, mẹ, bà và khung thứ tư phủ kín vải đen; mặt trước trống để đặt bát cơm",
     "tags": ["bàn thờ", "4 di ảnh"], "floor_y": 0.8, "char_h": 0.6, "hotspots_needed": ["offering_spot"]},
    {"id": "bgL7_mom_room_day", "kind": "background", "refs": ["assets/backgrounds/bg4d_main_room_day.png"],
     "why": "góp ý #10: phòng của mẹ (góc may) thay cho gian chính",
     "scene": ("IMPORTANT: warm DAYTIME, ignore the night lighting described above; match attached image 2's warm look. The "
               "mother's small room in a tube house: a window with soft sunlight on the left, wooden shelves with rolls of fabric, "
               "spools of thread and a tin of buttons, a dress form, a narrow bed edge on the far right; the floor area at the "
               "left-center is EMPTY (a sewing machine will be added later, do NOT draw one)."),
     "desc": "Phòng của mẹ ban ngày: cửa sổ nắng, kệ vải, cuộn chỉ, ma-nơ-canh; chừa trống chỗ đặt máy may (sprite)",
     "tags": ["phòng mẹ", "may vá", "ngày"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["machine_spot"]},
    {"id": "bgL11_ong_bed_corner_night", "kind": "background", "refs": ["assets/backgrounds/bg4_main_room.png"],
     "why": "góp ý #31 #37-41 #93: góc nhà kê giường tre của ông (cạnh gian thờ), cũng dùng trống trơn khi giường đã dọn",
     "scene": ("A corner of the main room of a tube house at night, right beside the family altar: a small wall altar shelf on "
               "the upper left with a small portrait of a young man (the father) and an incense bowl, an old wooden pendulum clock "
               "high on the wall, a small window with cold moonlight, a hanging bulb turned off. The floor in the lower half is "
               "EMPTY (a bamboo bed will be added later, do NOT draw a bed)."),
     "desc": "Góc nhà cạnh gian thờ ban đêm: bàn thờ treo nhỏ (ảnh bố), đồng hồ quả lắc trên tường, cửa sổ trăng; sàn trống đặt giường tre (sprite)",
     "tags": ["góc nhà", "giường ông", "đêm"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["bed_spot", "clock"]},
    {"id": "bgL12_living_room_day", "kind": "background", "refs": ["assets/backgrounds/bg4d_main_room_day.png"],
     "why": "góp ý #43-45 #47: phòng khách nơi thầy Tư ngồi xem giờ, cả nhà ngồi quanh",
     "scene": ("IMPORTANT: gray early-MORNING daylight, ignore the night lighting described above. The living room of a modest "
               "Vietnamese tube house: a large straw mat spread in the middle of the tiled floor, a low wooden cabinet, a thermos "
               "and tea cups on a small tray, an ancestral altar shelf high on the back wall, a wooden door ajar with pale light. "
               "The mat and floor in the lower half are empty."),
     "desc": "Phòng khách buổi sáng xám: chiếu cói giữa nhà, tủ thấp, khay trà, bàn thờ trên cao; sàn trống",
     "tags": ["phòng khách", "sáng"], "floor_y": 0.93, "char_h": 0.46, "hotspots_needed": ["mat_center"]},
    {"id": "bgL13_home_altar_bo", "kind": "background", "refs": ["assets/backgrounds/bg4_main_room.png"],
     "why": "góp ý #48: bàn thờ cũ trong nhà (ảnh bố), bên cạnh tường trống để treo gương phủ vải đỏ",
     "scene": ("IMPORTANT: dim gray MORNING light. A close view of the house's wall altar shelf: a small framed black-and-white "
               "portrait of a young man (the father) with a black mourning ribbon, a brass incense bowl, two candles, a plate "
               "of fruit. The RIGHT HALF of the wall next to the altar is EMPTY plain wall (a covered mirror will be added later)."),
     "desc": "Cận bàn thờ cũ trong nhà (ảnh bố), nửa phải là tường trống để treo gương phủ vải đỏ",
     "tags": ["bàn thờ", "bố"], "floor_y": 0.95, "char_h": 0.5, "hotspots_needed": ["mirror_spot"]},
    {"id": "bgL3d_coffin_top_full", "kind": "background", "style": COFFIN_STYLE, "refs": ["assets/backgrounds/bgL2_wake_coffin.png", ONG_BASE],
     "why": "góp ý #51 #53 #57: vẽ lại cận quan tài — thấy ĐỦ người ông (cả chân), đúng tỉ lệ, KHÔNG thấy lá bùa (nằm khuất dưới gối)",
     "scene": ("IMPORTANT: this background INCLUDES one person lying in a coffin. Looking straight DOWN from above at an open "
               "wooden coffin (same coffin, red lining and candles as attached image 2) lying HORIZONTALLY across the frame: "
               "head on the LEFT, feet on the RIGHT. The coffin is SMALL in the frame, it takes only the middle 70% of the width, "
               "with dark floor boards and a white funeral cloth visible on ALL FOUR sides around it, nothing touches the edges "
               "of the picture. Inside lies the old grandfather from attached image 3, his WHOLE body visible from the top of his "
               "head to the tips of both FEET (wearing white socks), normal adult proportions, legs as long as a real person's. "
               "Both hands folded on his chest, eyes closed, peaceful, his head on a small white pillow. Nothing else on the "
               "pillow or in the coffin: no paper, no talisman, no text. Two candles at the head end."),
     "desc": "Nhìn thẳng từ trên xuống: quan tài nằm ngang (đầu trái, chân phải), thấy trọn cả người ông (đủ chân, đúng tỉ lệ), tay đặt ngực; lá bùa khuất dưới gối nên không thấy",
     "tags": ["quan tài", "cận"], "floor_y": 0.95, "char_h": 0.4, "hotspots_needed": ["face", "hands", "pillow"]},
    {"id": "bgL3e_coffin_top_full_dropped", "kind": "background", "style": COFFIN_STYLE, "refs": ["assets/backgrounds/bgL3d_coffin_top_full.png"],
     "why": "góp ý #77: cùng khung bgL3d nhưng tay phải buông cạnh gối, ánh que diêm",
     "scene": ("Edit attached image 2, keep everything the same (framing, whole body with feet, face, style) and change ONLY: "
               "his LEFT hand stays on his chest; his RIGHT arm now lies straight along his side and the right hand rests palm-down "
               "on the sheet beside the pillow, fingers slightly curled, clearly connected to the arm (exactly two arms, two hands); "
               "the candles are out and the only light is a small match flame at the bottom edge; "
               "the corners of his lips lift a tiny bit."),
     "desc": "Cùng khung bgL3d: tay phải buông thõng cạnh gối, chỉ còn ánh que diêm, khoé miệng hơi nhếch",
     "tags": ["quan tài", "rợn"], "floor_y": 0.95, "char_h": 0.4, "hotspots_needed": ["face", "dropped_hand"]},
    {"id": "bgL3c_coffin_face_smile", "kind": "background", "style": COFFIN_STYLE, "refs": ["assets/backgrounds/bgL3d_coffin_top_full.png"],
     "why": "góp ý #80: ảo giác chớp nhoáng — mặt ông cười rợn trong ánh que diêm",
     "scene": ("An extreme close-up of the same old man's face from attached image 2, lying on the pillow in the coffin, lit from "
               "below by a single match: his eyes have slid open a crack, staring straight up at us, and his mouth is stretched "
               "into a wide, unnatural, terrifying smile, deep shadows, cold blue-gray skin."),
     "desc": "Cận mặt ông trong quan tài (ảo giác): mắt hé mở nhìn thẳng, miệng cười toác rợn người, ánh que diêm",
     "tags": ["ảo giác", "hù"], "floor_y": 0.95, "char_h": 0.4, "hotspots_needed": ["face"]},
    {"id": "bgL10b_altar_four_portraits", "kind": "background", "refs": ["assets/backgrounds/bgL10_altar_four_portraits.png"],
     "why": "góp ý #1/#2 (lần 2): bát cơm đè lên lư hương — lư hương nhỏ ở giữa, chừa chỗ trống trước từng di ảnh",
     "scene": ("The SAME altar as attached image 2 (same four portraits in the same order, the fourth frame covered by the black "
               "cloth, same candles, same style and night light) but rearranged: the altar top is WIDER and DEEPER and completely "
               "clean (no stains); a SMALL brass incense bowl with three incense sticks stands exactly in the CENTER at the front "
               "edge, between the 2nd and 3rd portraits; directly in front of EACH of the four portraits there is an EMPTY space on "
               "the altar top (four rice bowls will be added later, do NOT draw bowls); the two candles at the far left and far right ends."),
     "desc": "Bàn thờ 4 di ảnh (ông, mẹ, bà, khung phủ vải đen), lư hương nhỏ ở giữa mép trước, chỗ trống trước từng di ảnh để đặt bát",
     "tags": ["bàn thờ", "4 di ảnh"], "floor_y": 0.8, "char_h": 0.6, "hotspots_needed": ["offering_spot"]},
    {"id": "props_sheet_LG", "kind": "sheet", "character": "props", "grid": [1, 1],
     "refs": ["assets/characters/props/LF3_chopsticks_khoa.png"],
     "why": "góp ý #35: đôi đũa dư — cùng đôi đũa chữ đẹp (LF3) nhưng chữ KHOA khắc xấu, run, nguệch ngoạc",
     "sprites": [
         {"name": "LG1_chopsticks_spare_ugly", "pose": "the SAME pair of bamboo chopsticks as the LAST attached image, same angle, "
          "but the word KHOA near the top is carved CLUMSILY: crooked, uneven letters of different sizes, shaky scratched strokes "
          "that slip off the line, as if carved by a trembling old hand; the word appears only ONCE on each stick",
          "desc": "Đôi đũa dư: giống đũa LF3 nhưng chữ KHOA khắc xấu, run, xiêu vẹo (một lần mỗi chiếc)",
          "tags": ["đũa dư", "đũa khắc tên"], "facing": "front"}]},
    {"id": "bg4e_main_room_day_bo", "kind": "background",
     "refs": ["assets/backgrounds/bg4d_main_room_day.png", "assets/backgrounds/bgL11_ong_bed_corner_night.png"],
     "why": "góp ý #20-23: gian chính ban ngày như bg4d nhưng bàn thờ trên kệ có di ảnh bố (như cảnh đêm)",
     "scene": ("IMPORTANT: warm DAYTIME light exactly like attached image 2. The SAME main room as attached image 2, keep everything "
               "the same (layout, colors, dining table with the steaming pot, stools, calendar, door), and change ONLY the wall "
               "shelf on the upper left: it becomes a small family altar with the framed black-and-white portrait of the young "
               "father from attached image 3 (same face, black mourning ribbon), a small brass incense bowl with incense sticks "
               "and two small candles, the flower vase moved to the side."),
     "desc": "Gian chính ban ngày (như bg4d): kệ thờ trên tường có di ảnh bố, bát hương, 2 nến; bàn ăn nồi canh, ghế đẩu",
     "tags": ["gian chính", "ban ngày", "bữa cơm"], "floor_y": 0.85, "char_h": 0.46, "hotspots_needed": ["altar_shelf"]},
    {"id": "boy_hoodie_sheet_S", "kind": "sheet", "character": "boy_hoodie", "grid": [1, 4],
     "why": "góp ý #42: chu kỳ chạy rõ ràng — chạy ra xa, nhìn từ SAU LƯNG (4 khung khác nhau rõ)",
     "cycles": {"run_away": ["S1_run_away_a", "S2_run_away_b", "S3_run_away_c", "S4_run_away_d"]},
     "sprites": [
         {"name": "S1_run_away_a", "pose": "RUN CYCLE frame 1, seen from BEHIND running away from the viewer: LEFT foot planted, "
          "RIGHT leg kicked far back with the sole showing, right arm swung forward, left arm back, body leaning forward",
          "desc": "Chạy ra xa (sau lưng) khung 1: chân trái chạm đất, chân phải đá ra sau", "tags": ["chạy", "sau lưng"], "facing": "away"},
         {"name": "S2_run_away_b", "pose": "RUN CYCLE frame 2, seen from BEHIND: both feet OFF the ground in mid-air, legs "
          "crossing, arms close to the body, small jump",
          "desc": "Chạy ra xa khung 2: hai chân nhấc khỏi đất giữa không trung", "tags": ["chạy", "sau lưng"], "facing": "away"},
         {"name": "S3_run_away_c", "pose": "RUN CYCLE frame 3, seen from BEHIND: RIGHT foot planted, LEFT leg kicked far back with "
          "the sole showing, left arm swung forward, right arm back (mirror of frame 1)",
          "desc": "Chạy ra xa khung 3: chân phải chạm đất, chân trái đá ra sau", "tags": ["chạy", "sau lưng"], "facing": "away"},
         {"name": "S4_run_away_d", "pose": "RUN CYCLE frame 4, seen from BEHIND: both feet off the ground again, legs crossing the "
          "other way, body bouncing up",
          "desc": "Chạy ra xa khung 4: hai chân nhấc khỏi đất (bắt chéo ngược lại)", "tags": ["chạy", "sau lưng"], "facing": "away"}]},
    {"id": "boy_hoodie_sheet_R", "kind": "sheet", "character": "boy_hoodie", "grid": [1, 1],
     "refs": ["assets/characters/props/LG1_chopsticks_spare_ugly.png"],
     "why": "góp ý #36: Khoa ngồi dưới sàn cất đôi đũa dư chữ xấu vào hộp nhỏ, bỏ vào cặp sách (vẽ sau khi có LG1)",
     "sprites": [
         {"name": "R1_floor_box_spare_chopsticks", "pose": "sitting cross-legged on the FLOOR (no chair, no bed), side view "
          "facing left, carefully putting the pair of chopsticks from the LAST attached image into a small open wooden box held in "
          "his lap; an open school backpack lies on the floor right in front of him, ready for the box; quiet, careful face",
          "desc": "Ngồi xếp bằng dưới sàn, cẩn thận bỏ đôi đũa dư chữ xấu vào hộp gỗ nhỏ, cặp sách mở trước mặt", "tags": ["đũa dư", "ngồi"],
          "facing": "left"}]},
    {"id": "bgL3f_coffin_hand_talisman", "kind": "background", "style": COFFIN_STYLE,
     "refs": ["assets/backgrounds/bgL3d_coffin_top_full.png"],
     "why": "góp ý #56: cùng khung quan tài bgL3d, chỉ thấy bàn tay thầy Tư nhét lá bùa gấp tư xuống dưới gối",
     "scene": ("Edit attached image 2, keep everything the same (framing, coffin, the old man with the whole body, face, candles, "
               "style) and add ONLY: one thin old man's hand in a dark brown sleeve with a wooden prayer-bead bracelet reaching in "
               "from the TOP edge of the picture, sliding a small square of yellow paper folded in four (red ink marks) under the "
               "edge of the pillow beside the old man's head. Only the hand and the sleeve are visible, no other part of that person."),
     "desc": "Cùng khung bgL3d: một bàn tay áo nâu (thầy Tư) thò vào từ mép trên, nhét mảnh giấy vàng gấp tư xuống dưới gối ông",
     "tags": ["quan tài", "lá bùa"], "floor_y": 0.95, "char_h": 0.4, "hotspots_needed": ["pillow"]},
    {"id": "bgL14b_grandma_by_coffin", "kind": "background",
     "refs": ["assets/backgrounds/bgL14_grandma_comb_coffin.png", GMA_REF],
     "why": "góp ý #65: chỉ bà ngồi bên quan tài thì thầm — góc thấp, thành quan tài che kín, không thấy ông",
     "scene": ("IMPORTANT: this background INCLUDES one person. The same funeral room by candlelight as attached image 2, seen "
               "from LOW down near the floor: the tall dark wooden side of the coffin fills the lower middle of the picture and "
               "completely hides whoever lies inside (nobody visible in the coffin); the small grandmother from attached image 3 "
               "sits on a low stool at the right beside the coffin, the horn comb resting in her lap, one wrinkled hand laid on "
               "the coffin rim, her head tilted close to it as if whispering, sad gentle face. Altar, portrait and candles behind."),
     "desc": "Góc thấp: thành quan tài che kín (không thấy ông), bà ngồi ghế đẩu bên phải, lược trong lòng, tay đặt lên thành quan tài thì thầm",
     "tags": ["đám tang", "bà", "đêm"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["grandma"]},
    {"id": "bgL14_grandma_comb_coffin", "kind": "background",
     "refs": ["assets/backgrounds/bgL2_wake_coffin.png", ONG_BASE, GMA_REF],
     "why": "góp ý #63-65: bà ngồi chải tóc cho ông trong quan tài (vẽ sẵn cả hai người)",
     "scene": ("IMPORTANT: this background INCLUDES two people. A closer side view at night by candlelight in the funeral room of "
               "attached image 2: the open coffin edge runs across the lower middle; the old grandfather from attached image 3 lies "
               "inside with only his head and shoulders visible above the rim, eyes closed, peaceful; beside the coffin the small "
               "grandmother from attached image 4 sits on a low stool, leaning over, gently combing his silver hair with a dark horn "
               "comb, her lips moving as if talking softly to him, tender and sad."),
     "desc": "Vẽ sẵn: bà ngồi ghế thấp bên quan tài, chải tóc bạc cho ông (thấy đầu ông trên mép quan tài), thì thầm",
     "tags": ["chải tóc", "tang", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.5, "hotspots_needed": ["grandma", "ong_head"]},
    {"id": "bgL2n_wake_candles_out", "kind": "background", "refs": ["assets/backgrounds/bgL2_wake_coffin.png"],
     "why": "góp ý #73: gian thờ sau khi gió thổi tắt nến — chỉ còn đầu nhang đỏ",
     "scene": ("The SAME funeral room as attached image 2 (same layout, open coffin, lid leaning on the right) but both candles are "
               "OUT (no flame, thin smoke from the wicks), the room is very dark, only three incense tips glow red on the altar and "
               "a faint cold moonlight on the floor."),
     "desc": "Gian thờ (cùng bố cục bgL2) nến đã tắt, tối om, chỉ còn ba đầu nhang đỏ lập loè",
     "tags": ["đám tang", "nến tắt"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["coffin_head"]},
    {"id": "bgL5b_burial_shoveling", "kind": "background", "refs": ["assets/backgrounds/bgL5_cemetery_burial_day.png"],
     "why": "góp ý #92: mọi người xúc đất đỏ lấp huyệt",
     "scene": ("IMPORTANT: this background INCLUDES small people. The SAME cemetery as attached image 2 (same graves, kapok tree, "
               "gray sky) but now four villagers in beige mourning gauze stand around the grave shoveling dark RED earth onto the "
               "coffin, clods of earth falling, the mound getting smaller, a few mourners watching with heads bowed."),
     "desc": "Cùng nghĩa địa bgL5: bốn người áo xô xúc đất đỏ lấp huyệt, vài người cúi đầu đứng nhìn",
     "tags": ["hạ huyệt", "xúc đất"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["grave"]},
    {"id": "bgL9_main_room_altar_ong", "kind": "background", "refs": ["assets/backgrounds/bg4_main_room.png", PORTRAIT_BG],
     "why": "góp ý #95 #96 #99: gian chính sau khi ông mất — bàn thờ có ảnh ông + ảnh bố, ống đũa trên bàn ăn",
     "scene": ("The SAME main room as attached image 2 (same layout: wall altar shelf on the left, low dining table and stools on "
               "the right) at night, but the altar shelf now holds the old grandfather's framed portrait from attached image 3 in "
               "the middle with a black ribbon, the small portrait of the young father beside it, incense, two candles; the dining table "
               "is bare (a chopstick holder will be added later). Empty floor on the left."),
     "desc": "Gian chính (cùng bố cục bg4) đêm: bàn thờ có ảnh ông (giữa) + ảnh bố; bàn ăn để trống",
     "tags": ["gian thờ", "ông", "đêm"], "floor_y": 0.95, "char_h": 0.46,
     "hotspots_needed": ["altar_shelf", "dining_table"]},
    {"id": "bgL15_khoa_bed_awake_night", "kind": "background",
     "refs": ["assets/backgrounds/bg1_bedroom.png", "assets/characters/boy_hoodie/P1_bed_awake_grip_jacket.png", BOY_REF],
     "why": "góp ý #97-98: ảnh tĩnh vẽ sẵn Khoa nằm thao láo, áo khoác treo đầu giường",
     "scene": ("IMPORTANT: this background INCLUDES the boy. The bedroom of attached image 2 at night, moonlight through the "
               "window: the boy from attached image 4 lies on his back in a simple wooden bed under a dark blue blanket, eyes wide "
               "open staring at the ceiling, one hand gripping the black jacket that hangs on a hook at the head of the bed (as in "
               "attached image 3); the clock on the bedside table shows nearly three."),
     "desc": "Vẽ sẵn: Khoa nằm mắt mở thao láo trên giường, tay nắm áo khoác đen treo đầu giường, đồng hồ gần 3 giờ",
     "tags": ["phòng ngủ", "mất ngủ", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["boy"]},

    # ---------------------------------------------------- âm thanh
    {"id": "crow_caw", "kind": "sound", "sound_kind": "sfx", "desc": "Một con quạ kêu khàn khàn (1–2 tiếng)",
     "search": "crow caw single", "length": "~2s", "tags": ["quạ"], "volume": 0.9},
    {"id": "funeral_band", "kind": "sound", "sound_kind": "sfx", "desc": "Kèn trống đám ma Việt (kèn bầu, trống) buồn, lặp được",
     "search": "vietnamese funeral music suona drum", "length": "~20s", "tags": ["đám ma", "kèn trống"], "volume": 0.6},
    {"id": "mourners_cry", "kind": "sound", "sound_kind": "sfx", "desc": "Tiếng nhiều người khóc than đám tang, xa, lặp được",
     "search": "funeral mourners crying wailing", "length": "~15s", "tags": ["khóc than"], "volume": 0.5},
    {"id": "wood_block_slow", "kind": "sound", "sound_kind": "sfx", "desc": "Tiếng mõ gỗ gõ đều đều chậm (tụng kinh), lặp được",
     "search": "wooden fish mokugyo slow buddhist", "length": "~15s", "tags": ["mõ", "tang lễ"], "volume": 0.5},
    {"id": "chant_murmur", "kind": "sound", "sound_kind": "sfx", "desc": "Ông thầy khấn lầm rầm không rõ lời, lặp được",
     "search": "man murmuring prayer chant low", "length": "~10s", "tags": ["khấn"], "volume": 0.5},
    {"id": "coffin_nails", "kind": "sound", "sound_kind": "sfx", "desc": "Búa đóng đinh dài vào gỗ quan tài, từng nhát chát chúa",
     "search": "hammer nailing wood heavy slow", "length": "~6s", "tags": ["đóng quan tài"], "volume": 0.9},
    {"id": "shovel_dirt", "kind": "sound", "sound_kind": "sfx", "desc": "Xúc đất hất xuống nắp gỗ, từng xẻng",
     "search": "shovel dirt falling on coffin wood", "length": "~6s", "tags": ["hạ huyệt"], "volume": 0.8},
    {"id": "chopsticks_tap_2", "kind": "sound", "sound_kind": "sfx", "desc": "Đầu đũa tre gõ khẽ vào miệng bát sứ HAI tiếng",
     "search": "chopsticks tap ceramic bowl", "length": "~1.5s", "tags": ["đũa gõ bát"], "volume": 0.9},
    {"id": "sewing_machine", "kind": "sound", "sound_kind": "sfx", "desc": "Máy khâu đạp chân cũ chạy lạch cạch đều, lặp được",
     "search": "old treadle sewing machine", "length": "~10s", "tags": ["máy khâu"], "volume": 0.6},
    {"id": "match_strike", "kind": "sound", "sound_kind": "sfx", "desc": "Quẹt diêm bùng lửa", "search": "match strike ignite",
     "length": "~1.5s", "tags": ["diêm"], "volume": 0.9},
    {"id": "wind_field", "kind": "sound", "sound_kind": "sfx", "desc": "Gió đồng thổi rì rào qua ruộng, lặp được",
     "search": "wind open field grass", "length": "~15s", "tags": ["gió đồng"], "volume": 0.6},
    {"id": "wind_gust_candle", "kind": "sound", "sound_kind": "sfx", "desc": "Một luồng gió lạnh lùa qua phòng (thổi tắt nến)",
     "search": "cold wind gust whoosh indoor", "length": "~2s", "tags": ["gió", "nến tắt"], "volume": 0.8},
    {"id": "bamboo_whittle", "kind": "sound", "sound_kind": "sfx", "desc": "Dao nhỏ gọt khắc tre lách tách, lặp được",
     "search": "whittling wood knife carving", "length": "~8s", "tags": ["khắc đũa"], "volume": 0.6},
    {"id": "clock_chime_3", "kind": "sound", "sound_kind": "sfx", "desc": "Đồng hồ quả lắc gõ ba tiếng boong ngân",
     "search": "pendulum clock chime three strikes", "length": "~5s", "tags": ["đồng hồ", "3 giờ"], "volume": 0.9},
    {"id": "old_man_breath", "kind": "sound", "sound_kind": "sfx", "desc": "Ông già thở nặng nhọc, khò khè, lặp được",
     "search": "old man labored breathing wheezing", "length": "~10s", "tags": ["hấp hối"], "volume": 0.6},
    {"id": "old_man_cough", "kind": "sound", "sound_kind": "sfx", "desc": "Ông già ho khan từng tràng", "search": "old man cough",
     "length": "~4s", "tags": ["ho"], "volume": 0.9},
    {"id": "memory_piano", "kind": "sound", "sound_kind": "music", "desc": "Piano buồn nhẹ, hoài niệm (cho đoạn kỷ niệm gia đình), lặp được",
     "search": "sad nostalgic piano ambient loop", "length": "~60s", "tags": ["nhạc", "hồi ức"], "volume": 0.5},
]

ASSET_REQUESTS_P2 = [
    # ================================================= PHẦN 2 — BÁT CƠM THỨ HAI
    # ---------------------------------------------------- mẹ
    {"id": "mother_alive_sheet_H", "kind": "sheet", "character": "mother_alive", "grid": [2, 3],
     "why": "P2: mẹ ốm nằm giường, ngồi nhìn bát cơm đầu giường, đan áo len bên đèn dầu, Khoa bón canh, đan cổ áo tay run, vuốt tóc Khoa",
     "note": ("The bed in every pose with a bed is the SAME " + MOM_BED + " (head of the bed on the LEFT, whole bed drawn, same "
              "size). The sweater is always " + SWEATER + ". Where the boy appears he is " + BOY + ". The mother is thin, "
              "pale, hollow cheeks, tired eyes (she is getting sick)."),
     "refs": [BOY_REF],
     "sprites": [
         {"name": "H1_bed_lie_sick", "pose": "lying on her back in the bed under the blanket, head on the pillow at the left, eyes "
          "closed, pale and gaunt, one thin hand on the blanket",
          "desc": "Nằm ốm trên giường gỗ (đầu giường bên trái), mắt nhắm, gầy rộc (có giường)", "tags": ["ốm", "giường"], "facing": "right"},
         {"name": "H2_bed_sit_stare_bowl", "pose": "sitting up in the same bed, blanket on her legs, frozen, staring down at the pillow "
          "beside her (where a rice bowl will be placed, not drawn), hands clutching the blanket, scared",
          "desc": "Ngồi dậy trên giường, nhìn trân trân xuống cạnh gối (bát cơm), hai tay siết chăn (có giường)",
          "tags": ["bát cơm", "sợ", "giường"], "facing": "right"},
         {"name": "H3_sit_knit_lamp", "pose": "sitting on a low stool, side view facing right, knitting the sweater with two long "
          "needles, a small glass oil lamp glowing on a tiny stool beside her (lamp included), tired but tender, slightly hunched",
          "desc": "Ngồi ghế đẩu đan áo len bên đèn dầu nhỏ (có đèn), mệt nhưng dịu dàng", "tags": ["đan len", "đèn dầu"], "facing": "right"},
         {"name": "H4_bed_khoa_feed_soup", "pose": "TWO characters: the mother sits up in the bed leaning on the pillow; the boy sits "
          "on the edge of the bed holding a small bowl of soup and feeding her one spoonful, careful and sad",
          "desc": "HAI nhân vật + giường: mẹ ngồi tựa gối, Khoa ngồi mép giường bón từng thìa canh",
          "tags": ["bón canh", "mẹ con", "giường"], "facing": "right"},
         {"name": "H5_bed_knit_collar_tremble", "pose": "sitting up in the bed, holding the sweater and the two knitting needles, "
          "trying to knit the collar but her thin hands tremble (small tremble lines), a weak gentle smile",
          "desc": "Ngồi trên giường cố đan nốt cổ áo len, tay run, cười yếu ớt (có giường)", "tags": ["đan len", "giường"],
          "facing": "right"},
         {"name": "H6_bed_stroke_boy_hair", "pose": "TWO characters: the mother lies in the bed, head on the pillow at the left, "
          "reaching up one thin hand to stroke the hair of the boy who sits on a low stool beside the bed with his head bowed, "
          "crying, tears falling",
          "desc": "HAI nhân vật + giường: mẹ nằm đưa tay vuốt tóc Khoa, Khoa ngồi ghế cạnh giường cúi đầu khóc",
          "tags": ["mẹ con", "khóc", "giường"], "facing": "right"},
     ]},
    {"id": "mother_alive_sheet_I", "kind": "sheet", "character": "mother_alive", "grid": [2, 3],
     "why": "P2: buổi sáng khoẻ lại (áo hoa) đi chợ với Khoa, ngồi máy khâu khóc với bộ áo xô, nằm mất trong áo xô, Khoa áp tay mẹ lên má",
     "note": ("Where the boy appears he is " + BOY + ". The bed is EXACTLY the bed in the LAST attached image. "
              "FLORAL means: an old faded light-blue blouse with small white flowers instead of the cardigan, hair neatly combed "
              "in her low bun. MOURNING means: " + TUNIC + "."),
     "refs": [BOY_REF, MOM_BED_REF],
     "sprites": [
         {"name": "I1_floral_comb_hair", "pose": "FLORAL: standing side view facing right, combing her long black hair with a "
          "wooden comb before tying it, a rare bright smile in the morning",
          "desc": "Áo hoa cũ: đứng chải tóc, cười tươi hiếm hoi (buổi sáng khoẻ lại)", "tags": ["áo hoa", "chải tóc"], "facing": "right"},
         {"name": "I2_market_step_xoi_boy", "pose": "TWO characters sitting side by side on a low stone step: the mother (FLORAL) and "
          "the boy, each holding a small banana-leaf packet of sticky rice, eating, the mother smiling warmly at him",
          "desc": "HAI nhân vật: mẹ (áo hoa) và Khoa ngồi bậc đá ăn xôi lạc, mẹ cười", "tags": ["chợ", "xôi", "mẹ con"], "facing": "right"},
         {"name": "I3_hold_boy_hand", "pose": "TWO characters standing: the mother (FLORAL) holding the boy's hand tightly in both her "
          "hands, looking down at him with a sad tender smile; the boy looks up laughing",
          "desc": "HAI nhân vật đứng: mẹ (áo hoa) siết tay Khoa, cười buồn; Khoa ngước lên cười", "tags": ["dặn dò", "mẹ con"],
          "facing": "right"},
         {"name": "I4_sew_machine_cry_tunic", "pose": "sitting at an old black treadle sewing machine on a small wooden table (machine "
          "and table included), side view facing right, holding up a finished beige gauze mourning tunic in both hands, "
          "crying, small red prick dots on all her fingertips",
          "desc": "Ngồi bên máy khâu cầm bộ áo xô vừa may xong, khóc; đầu ngón tay chi chít vết kim (có máy)",
          "tags": ["áo xô", "máy khâu", "khóc"], "facing": "right"},
         {"name": "I5_lie_dead_tunic", "pose": "MOURNING, hair loose: lying on her back in the bed (no blanket on her chest), eyes "
          "closed, calm peaceful face like sleeping, both hands folded on her chest, small red prick dots on her fingertips",
          "desc": "Áo xô, tóc xoã: nằm mất trên giường, bình thản, hai tay đặt trên ngực, ngón tay vết kim (có giường)",
          "tags": ["mẹ mất", "áo xô", "giường"], "facing": "right"},
         {"name": "I6_bed_khoa_hold_hand_cheek", "pose": "TWO characters: the mother (MOURNING, hair loose) lies in the bed, eyes "
          "closed, breathing weakly; the boy sits on the floor beside the bed, pressing her limp hand against his cheek with both "
          "hands, eyes red, crying",
          "desc": "HAI nhân vật + giường: mẹ (áo xô) nằm thở yếu, Khoa ngồi bệt áp tay mẹ lên má khóc",
          "tags": ["đêm 49", "mẹ con", "giường"], "facing": "right"},
     ]},
    {"id": "mother_alive_sheet_J", "kind": "sheet", "character": "mother_alive", "grid": [1, 4],   # Gemini vẽ 1 hàng
     "why": "P2 đêm 49: mẹ mộng du trong áo xô xới cơm, Khoa nắm tay mẹ, mẹ cúi chào di ảnh",
     "note": ("In ALL poses she wears " + TUNIC + ", her long black hair LOOSE down her back (no bun), eyes CLOSED, sleepwalking, "
              "calm blank face. Where the boy appears he is " + BOY + "."),
     "refs": [BOY_REF],
     "sprites": [
         {"name": "J1_sleepwalk_stand", "pose": "standing still, side view facing LEFT, arms hanging, head slightly lowered",
          "desc": "Áo xô, tóc xoã, mắt nhắm: đứng im (quay trái), tay buông", "tags": ["mộng du", "áo xô"], "facing": "left"},
         {"name": "J2_sleepwalk_scoop_rice", "pose": "side view facing LEFT, holding an empty rice bowl in one hand and slowly scooping "
          "rice into it with a wooden rice paddle from a small pot held against her hip, eyes closed",
          "desc": "Mộng du (quay trái): cầm bát không, dùng muôi gỗ xới cơm từ nồi nhỏ, mắt nhắm", "tags": ["mộng du", "xới cơm"],
          "facing": "left"},
         {"name": "J3_khoa_grab_mom_hand", "pose": "TWO characters: the boy (on the right) grabbing the mother's cold hand with both "
          "hands, looking up at her face, crying out; the mother (on the left) does not open her eyes, head tilted slightly toward "
          "him, lips parted as if whispering",
          "desc": "HAI nhân vật: Khoa (phải) nắm tay mẹ gọi, mẹ (trái) nhắm mắt nghiêng đầu thì thầm", "tags": ["mộng du", "mẹ con"],
          "facing": "left"},
         {"name": "J4_sleepwalk_bow_portrait", "pose": "side view facing LEFT, bowing her head politely as if greeting someone she "
          "knows, hands together in front, eyes closed",
          "desc": "Mộng du (quay trái): khẽ cúi đầu chào (di ảnh ông) như chào người quen", "tags": ["mộng du", "chào"],
          "facing": "left"},
     ]},
    {"id": "mother_alive_sheet_K", "kind": "sheet", "character": "mother_alive", "grid": [1, 2],
     "why": "vẽ lại I5/I6 của sheet I: I5 mẹ mặc áo len nâu thay vì áo xô, I6 bị vẽ HAI cậu bé",
     "note": ("The bed is EXACTLY the bed in attached image 4. The mother wears EXACTLY the beige gauze mourning tunic of "
              "attached image 5 (" + TUNIC + "), long black hair LOOSE, NO sweater, NO cardigan. Where the boy appears he is "
              + BOY + " — draw the boy ONLY ONCE, never two boys."),
     "refs": [BOY_REF, MOM_BED_REF, "assets/characters/mother_alive/J1_sleepwalk_stand.png"],
     "sprites": [
         {"name": "K1_lie_dead_tunic", "pose": "ALONE: lying on her back on top of the bed (blanket only over her legs), the beige "
          "gauze mourning tunic clearly visible, eyes closed, calm peaceful face like sleeping, both hands folded on her chest, "
          "small red prick dots on her fingertips",
          "desc": "Áo xô, tóc xoã: nằm mất trên giường, bình thản, hai tay đặt trên ngực, ngón tay vết kim (có giường)",
          "tags": ["mẹ mất", "áo xô", "giường"], "facing": "right"},
         {"name": "K2_bed_khoa_hold_hand_cheek", "pose": "EXACTLY TWO characters, ONE mother and ONE boy: the mother lies in the bed "
          "in the beige tunic, eyes closed, breathing weakly; the boy (only one boy) sits on the floor in FRONT of the bed, "
          "holding her limp hand with both hands and pressing it against his cheek, eyes red, crying. Nobody behind the bed",
          "desc": "HAI nhân vật + giường: mẹ (áo xô) nằm thở yếu, MỘT Khoa ngồi bệt trước giường áp tay mẹ lên má khóc",
          "tags": ["đêm 49", "mẹ con", "giường"], "facing": "right"},
     ]},
    # ---------------------------------------------------- bà, ông, thầy Tư, Khoa
    {"id": "grandma_sheet_N", "kind": "sheet", "character": "grandma", "grid": [2, 4],
     "why": "P2: đứng nhìn bát cơm, cận mặt sợ, đổ cơm cho gà, xua quạ bằng sào, ngồi canh bàn thờ, nghe điện thoại, ôm di ảnh ông khóc, gấp áo len",
     "note": "The sweater (pose 8) is " + SWEATER + ".",
     "sprites": [
         {"name": "N1_back_stare_altar", "pose": "seen from BEHIND, standing still, arms hanging limp at her sides, head raised, "
          "staring up at something high in front of her (an altar, not drawn)",
          "desc": "Quay lưng đứng im, tay buông thõng, ngước nhìn lên (bàn thờ)", "tags": ["bát cơm", "quay lưng"], "facing": "away"},
         {"name": "N2_closeup_face_fear", "pose": "CLOSE-UP of her face and shoulders, front view: pale face, eyes not surprised but "
          "full of a very old fear, lips pressed together",
          "desc": "Cận mặt: tái đi, ánh mắt không ngạc nhiên mà sợ một nỗi sợ rất cũ", "tags": ["cận mặt", "sợ"], "facing": "front"},
         {"name": "N3_feed_chickens", "pose": "standing side view facing right, tipping a rice bowl to pour rice onto the ground for "
          "three small brown hens pecking at her feet (hens included)",
          "desc": "Đổ bát cơm cho mấy con gà mổ dưới chân (có gà)", "tags": ["đổ cơm", "gà"], "facing": "right"},
         {"name": "N4_pole_shoo_crow", "pose": "standing side view facing right, swinging a long bamboo pole upward with both hands, "
          "looking up angrily and scared (at a crow up high, not drawn)",
          "desc": "Vung cây sào tre dài lên cao xua (con quạ), ngước nhìn", "tags": ["xua quạ", "sào"], "facing": "right"},
         {"name": "N5_sit_chair_guard", "pose": "sitting upright on a small wooden chair (chair included), side view facing LEFT, hands "
          "on her knees, eyes wide open, keeping watch through the night",
          "desc": "Ngồi ghế gỗ (quay trái) canh đêm, mắt mở to (có ghế)", "tags": ["canh bàn thờ", "đêm"], "facing": "left"},
         {"name": "N6_phone_forced_smile", "pose": "standing front view, holding an old mobile phone to her ear, forcing a calm smile "
          "while her eyes are sad",
          "desc": "Đứng nghe điện thoại, gượng cười, mắt buồn", "tags": ["điện thoại", "giấu chuyện"], "facing": "front"},
         {"name": "N7_sit_bed_portrait_cry", "pose": "sitting on the edge of a simple wooden bed (bed edge included), side view facing "
          "right, holding a small framed portrait of an old man against her chest, crying, whispering",
          "desc": "Ngồi mép giường ôm tấm di ảnh nhỏ của ông, khóc thì thầm (có mép giường)", "tags": ["lời hứa", "khóc"],
          "facing": "right"},
         {"name": "N8_fold_sweater", "pose": "standing side view facing right, gently folding the unfinished sweater in her hands, "
          "head bowed, sad",
          "desc": "Đứng gấp chiếc áo len đan dở, cúi đầu", "tags": ["áo len", "tang"], "facing": "right"},
     ]},
    {"id": "ong_noi_sheet_E", "kind": "sheet", "character": "ong_noi", "grid": [1, 1],
     "why": "P2: mẹ mơ thấy ông đứng cuối giường gõ đũa vào miệng bát hai cái",
     "sprites": [
         {"name": "E1_ghost_tap_bowl", "pose": "the grandfather as a quiet ghost in a dark blue traditional ao the funeral robe, grayish "
          "pale skin, standing still, side view facing LEFT, holding a rice bowl in one hand and gently tapping its rim with a pair "
          "of chopsticks, silent sad face, eyes in shadow",
          "desc": "Bóng ông (áo the, da xám) đứng (quay trái) cầm bát gõ đũa vào miệng bát", "tags": ["ma", "gõ đũa", "giấc mơ"],
          "facing": "left"},
     ]},
    {"id": "thay_tu_sheet_C", "kind": "sheet", "character": "thay_tu", "grid": [1, 4],   # Gemini vẽ 1 hàng: C1, C3, C4, C2
     "why": "P2: rắc gạo muối, treo gương bát quái, ngồi chiếu giảng chuyện đổi đũa, lắc đầu từ chối",
     "sprites": [
         {"name": "C1_scatter_rice_salt", "pose": "standing side view facing right, flinging a handful of rice and salt from a small "
          "bowl, grains flying in an arc (grains included)",
          "desc": "Đứng vung tay rắc gạo muối (hạt bay trong hình)", "tags": ["gạo muối", "trừ tà"], "facing": "right"},
         {"name": "C3_sit_mat_explain", "pose": "sitting cross-legged, front view slightly turned right, one hand raised with two "
          "fingers up as he explains something grave, serious low-voiced face",
          "desc": "Ngồi xếp bằng, giơ tay giảng giải, mặt nghiêm trầm", "tags": ["giảng", "đổi đũa"], "facing": "front"},
         {"name": "C4_sit_mat_shake_head", "pose": "sitting cross-legged, front view, eyes closed, shaking his head, one palm raised "
          "outward in refusal",
          "desc": "Ngồi xếp bằng, nhắm mắt lắc đầu, giơ bàn tay từ chối", "tags": ["từ chối", "đổi mạng"], "facing": "front"},
              {"name": "C2_hang_bagua_mirror", "pose": "standing on tiptoe, side view facing LEFT, reaching both arms high above his head "
          "to hang a small red-and-gold octagonal bagua mirror (mirror included, nothing else above him)",
          "desc": "Kiễng chân giơ cao tay treo gương bát quái (quay trái)", "tags": ["gương bát quái"], "facing": "left"},
]},
    {"id": "boy_hoodie_sheet_T", "kind": "sheet", "character": "boy_hoodie", "grid": [2, 2],
     "why": "P2: khoanh lịch đếm ngày, cầm bùa giơ tay định gõ cửa phòng bà, quỳ bới đất ở đầu mộ, quỳ cầm đôi đũa run",
     "note": JACKET + " Pose 1 has NO jacket (just the hoodie)." + SAME_JACKET,
     "refs": [JACKET_REF],
     "sprites": [
         {"name": "T1_circle_calendar", "pose": "NO jacket: standing side view facing right in front of a paper wall calendar "
          "(calendar included), circling a date with a pencil, some days already circled, worried face",
          "desc": "Áo hoodie: đứng khoanh ngày trên tờ lịch treo tường bằng bút chì (có lịch)", "tags": ["lịch", "đếm ngày"],
          "facing": "right"},
         {"name": "T2_raise_hand_knock_talisman", "pose": "black jacket: standing side view facing right, one hand raised hesitating "
          "to knock (a door, not drawn), the other hand holding a small square of yellow paper folded in four with red marks",
          "desc": "Áo khoác đen: cầm lá bùa, giơ tay ngập ngừng định gõ cửa", "tags": ["gõ cửa", "lá bùa"], "facing": "right"},
         {"name": "T3_kneel_dig_grave", "pose": "black jacket, at night: kneeling side view facing LEFT, digging a small hole in dark "
          "RED earth with bare hands, dirty hands, a lit flashlight lying on the ground beside him",
          "desc": "Áo khoác đen: quỳ bới đất đỏ bằng tay (quay trái), đèn pin nằm cạnh", "tags": ["nghĩa địa", "bới đất"],
          "facing": "left"},
         {"name": "T4_kneel_hold_chopsticks", "pose": "black jacket, at night: kneeling side view facing LEFT, holding a pair of "
          "bamboo chopsticks upright with both dirty hands at his chest, trembling (tremble lines), terrified wide eyes",
          "desc": "Áo khoác đen: quỳ (quay trái) hai tay cầm đôi đũa run bần bật, mắt hoảng", "tags": ["đổi đũa", "run"],
          "facing": "left"},
     ]},
    # ---------------------------------------------------- đạo cụ
    {"id": "props_sheet_LH", "kind": "sheet", "character": "props", "grid": [2, 5],
     "why": "P2: áo len đan dở, bộ áo xô, lịch khoanh ngày, ngón tay vết kim, hạt cơm dưới móng, gương trần, vải đỏ dưới sàn, hộp bút giấu bùa, máy khâu phủ khăn, gương bát quái",
     "sprites": [
         {"name": "LH1_sweater_unfinished", "pose": SWEATER + " lying flat, two knitting needles and a ball of yarn beside it",
          "desc": "Áo len đỏ sẫm đan dở (thiếu cổ), que đan và cuộn len", "tags": ["áo len", "đan dở"], "facing": "front"},
         {"name": "LH2_mourning_tunic_folded", "pose": "a finished loose coarse BEIGE gauze mourning tunic laid flat, very straight neat "
          "stitches",
          "desc": "Bộ áo xô be may xong, đường kim thẳng tắp", "tags": ["áo xô", "tang"], "facing": "front"},
         {"name": "LH3_calendar_circled", "pose": "a paper wall calendar page with a grid of days, many days circled in pencil, one "
          "far day circled heavily twice",
          "desc": "Tờ lịch treo tường, nhiều ngày khoanh bút chì, một ngày khoanh đậm", "tags": ["lịch", "đếm ngày"], "facing": "front"},
         {"name": "LH4_fingertips_needle_marks", "pose": "close-up of a woman's thin hand, palm up, every fingertip covered in tiny "
          "needle pricks with dried red dots of blood",
          "desc": "Cận bàn tay phụ nữ, mười đầu ngón chi chít vết kim, máu khô", "tags": ["vết kim", "cận"], "facing": "front"},
         {"name": "LH5_rice_under_nails", "pose": "close-up of a woman's hand, fingers curled, a few white grains of cooked rice stuck "
          "under the fingernails",
          "desc": "Cận bàn tay, vài hạt cơm nguội dính dưới móng tay", "tags": ["hạt cơm", "móng tay", "cận"], "facing": "front"},
         {"name": "LH6_mirror_bare", "pose": "a tall rectangular wall mirror in a dark wooden frame, uncovered, the glass dark and "
          "empty, faint reflections",
          "desc": "Gương treo tường khung gỗ, không phủ, mặt kính tối", "tags": ["gương"], "facing": "front"},
         {"name": "LH7_red_cloth_floor", "pose": "a red cloth crumpled in a heap on the floor",
          "desc": "Tấm vải đỏ nhàu rơi dưới sàn", "tags": ["vải đỏ", "gương"], "facing": "front"},
         {"name": "LH8_pencil_case_talisman", "pose": "an open old school pencil case with pencils, and a small square of yellow paper "
          "folded in four with red marks hidden at the bottom under the pencils",
          "desc": "Hộp bút mở, lá bùa gấp tư giấu dưới đáy", "tags": ["hộp bút", "lá bùa"], "facing": "front"},
         {"name": "LH9_sewing_machine_covered", "pose": "an old black treadle sewing machine on its small wooden table, completely "
          "covered with a plain gray cloth",
          "desc": "Máy khâu đạp chân phủ kín tấm khăn xám", "tags": ["máy khâu", "tang"], "facing": "front"},
         {"name": "LH10_bagua_mirror", "pose": "a small octagonal red-and-gold bagua mirror with trigram marks around a round mirror",
          "desc": "Gương bát quái bát giác đỏ vàng", "tags": ["gương bát quái"], "facing": "front"},
     ]},
    # ---------------------------------------------------- phông nền
    {"id": "bgL9d_main_room_altar_ong_day", "kind": "background", "refs": ["assets/backgrounds/bgL9_main_room_altar_ong.png"],
     "why": "P2: buổi sáng bà thấy bát cơm thứ hai, bà dặn Khoa, thầy Tư đứng trước bàn thờ",
     "scene": ("IMPORTANT: cold gray EARLY MORNING light, ignore the night lighting described above. The SAME main room as "
               "attached image 2 (same layout, altar shelf with the grandfather's portrait and the small father's portrait on the "
               "left, calendar, dining table and stools on the right, door at the far right), pale daylight from the right, "
               "candles unlit. Empty floor on the left."),
     "desc": "Gian chính có bàn thờ ông (cùng bố cục bgL9) buổi sáng xám",
     "tags": ["gian thờ", "sáng"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["altar_shelf", "dining_table"]},
    {"id": "bgL7n_mom_room_night", "kind": "background", "refs": ["assets/backgrounds/bgL7_mom_room_day.png"],
     "why": "P2: mẹ ốm, đan áo len bên đèn, máy khâu chạy lúc 3 giờ, Khoa ngồi bên giường mẹ",
     "scene": ("The SAME room as attached image 2 (same window, cloth shelves, spools, dress form) at NIGHT: deep blue dark, "
               "cold moonlight from the window, a faint warm glow on the left. Keep the empty floor where the sewing machine "
               "goes, and ALSO leave the right half of the floor empty for a bed (not drawn)."),
     "desc": "Phòng mẹ ban đêm (cùng bố cục bgL7), chừa chỗ máy may + nửa phải trống đặt giường (sprite)",
     "tags": ["phòng mẹ", "đêm"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["machine_spot", "bed_spot"]},
    {"id": "bgL16_market_morning", "kind": "background", "refs": ["assets/backgrounds/bg7d_front_yard_morning.png"],
     "why": "P2: mẹ con ngồi ăn xôi trên bậc đá đầu chợ, nắng sớm",
     "scene": ("IMPORTANT: warm EARLY MORNING sunlight, ignore the night lighting described above. The entrance of a small "
               "Vietnamese town market: canvas awnings, baskets of vegetables, a xoi sticky-rice stall with steaming pots, a few "
               "small far-away shoppers, and in the foreground a wide low worn STONE STEP running across the lower third, empty, "
               "golden sunlight on it."),
     "desc": "Đầu chợ quê buổi sáng: mái bạt, gánh rau, hàng xôi bốc hơi; bậc đá trống ở tiền cảnh, nắng sớm",
     "tags": ["chợ", "sáng", "hồi ức"], "floor_y": 0.93, "char_h": 0.46, "hotspots_needed": ["stone_step"]},
    {"id": "bgL17_cemetery_night_grave", "kind": "background", "refs": ["assets/backgrounds/bgL5_cemetery_burial_day.png"],
     "why": "P2 đêm 48: Khoa quỳ bới đất ở đầu mộ ông, quạ trên cây gạo, bóng ông sau bia",
     "scene": ("The SAME field cemetery as attached image 2 (same dry leafless kapok tree on the right) but at NIGHT, deep blue "
               "darkness, thin mist: the pit is now filled into a NEW grave mound of bare dark RED earth with no grass yet, a small "
               "plain stone headstone standing at its head, wilted funeral flowers; old weathered graves behind in the dark. "
               "Leave empty ground in front of the head of the grave (someone will kneel there) and empty space just behind "
               "the headstone. No people."),
     "desc": "Nghĩa địa đêm: mộ ông mới đắp đất đỏ, bia nhỏ, cây gạo khô bên phải, sương mỏng; chừa chỗ quỳ và chỗ sau bia",
     "tags": ["nghĩa địa", "đêm", "mộ ông"], "floor_y": 0.95, "char_h": 0.42,
     "hotspots_needed": ["grave_head", "behind_headstone", "crow_branch"]},
    {"id": "bgL17b_two_graves_day", "kind": "background", "refs": ["assets/backgrounds/bgL17_cemetery_night_grave.png"],
     "why": "P2: đưa tang mẹ — hai nấm mộ cạnh nhau, lỗ đất nhỏ Khoa bới vẫn còn ở đầu mộ ông",
     "scene": ("IMPORTANT: overcast gray DAYTIME, ignore the night lighting described above. The SAME cemetery as attached image 2 "
               "(same kapok tree on the right) with TWO graves side by side: the left one is the grandfather's (red earth already "
               "dried and crusted, his small headstone), with a small hand-dug hole still open at its head; the right one is a "
               "brand-new fresh mound of wet red earth with incense sticks and paper flowers. No people."),
     "desc": "Ban ngày âm u: hai mộ cạnh nhau (mộ ông đất se mặt có lỗ nhỏ ở đầu, mộ mẹ đất tươi), cây gạo khô",
     "tags": ["nghĩa địa", "hai mộ", "ngày"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["hole", "crow_branch"]},
    {"id": "bgL18_field_path_night", "kind": "background", "refs": ["assets/backgrounds/bgL4_procession_field.png"],
     "why": "P2 đêm 48: Khoa soi đèn pin đi trên bờ ruộng ra nghĩa địa, rồi bỏ chạy về",
     "scene": ("The SAME rice fields as attached image 2 at NIGHT: deep blue darkness, a narrow raised dirt path between the "
               "harvested paddies running ACROSS the picture from left to right in the lower third, tall wild grass bent by the "
               "wind, far away a dark line of trees and the black silhouette of a dry kapok tree. No people. Empty path."),
     "desc": "Bờ ruộng đêm chạy ngang khung, cỏ may rạp trong gió, xa xa hàng cây và cây gạo khô",
     "tags": ["cánh đồng", "đêm"], "floor_y": 0.9, "char_h": 0.36, "hotspots_needed": ["path"]},
    {"id": "bgL19_mirror_ong_behind_mom", "kind": "background",
     "refs": ["assets/backgrounds/bgL13_home_altar_bo.png", ONG_BASE, "assets/characters/mother_alive/J2_sleepwalk_scoop_rice.png"],
     "why": "P2 đêm 49: trong gương, ông đứng sau lưng mẹ cùng cầm muôi xới cơm",
     "scene": ("IMPORTANT: this background INCLUDES two people seen in a mirror. A close view of a tall wall mirror in a dark wooden "
               "frame (a red cloth lies on the floor below it), in the dark altar room at night: in the glass we see the REFLECTION "
               "of the mother from attached image 4 (beige gauze mourning tunic, long loose hair, eyes closed) scooping rice into a "
               "bowl, and standing right BEHIND her the grandfather from attached image 3 in a dark blue ao the funeral robe, grayish "
               "skin, his dry thin right hand laid over her hand on the wooden rice paddle, guiding it. Only in the mirror; dim red "
               "candle glow."),
     "desc": "Vẽ sẵn: trong gương, mẹ (áo xô, tóc xoã) xới cơm, ông áo the đứng sau đặt tay lên tay mẹ cầm muôi",
     "tags": ["gương", "ông", "mẹ", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.5, "hotspots_needed": ["mirror"]},
    {"id": "bgL19b_mirror_khoa_alone", "kind": "background",
     "refs": ["assets/backgrounds/bgL19_mirror_ong_behind_mom.png", BOY_REF],
     "why": "P2: nhìn lại gương — chỉ còn Khoa đứng giữa gian thờ tối trước hai bát cơm",
     "scene": ("IMPORTANT: this background INCLUDES the boy seen in the mirror. The SAME mirror and framing as attached image 2, but "
               "in the glass there is only the small boy from attached image 3 standing alone in the dark altar room, frightened, "
               "and behind him on the altar two full rice bowls with chopsticks standing upright. Nobody else."),
     "desc": "Vẽ sẵn: cùng gương, chỉ còn Khoa đứng một mình giữa gian thờ tối, sau lưng hai bát cơm",
     "tags": ["gương", "Khoa", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.5, "hotspots_needed": ["mirror"]},
    {"id": "bgL20_wake_coffin_mom", "kind": "background", "refs": ["assets/backgrounds/bgL2c_wake_coffin_closed.png", MOM_PORTRAIT],
     "why": "P2: tang mẹ — gian thờ có quan tài mẹ, di ảnh mẹ",
     "scene": ("The SAME funeral room as attached image 2 (same layout, coffin in the middle with the head on the left) but this is "
               "the MOTHER's wake: the coffin lid is open and leaning on the right wall, and the framed portrait on the altar is "
               "the woman from attached image 3 with a black ribbon; two candles, paper wreaths. Night."),
     "desc": "Gian thờ đám tang mẹ: quan tài mở nắp, di ảnh mẹ băng đen, nến, vòng hoa",
     "tags": ["đám tang", "mẹ", "đêm"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["coffin_head"]},
    {"id": "bgL21_altar_ong_me", "kind": "background", "refs": [PORTRAIT_BG, MOM_PORTRAIT],
     "why": "P2: bàn thờ hai di ảnh ông và mẹ đặt cạnh nhau, khói nhang",
     "scene": ("A close view of the same altar as attached image 2 at night, but now TWO framed portraits stand side by side: the "
               "grandfather (left, as in attached image 2) and the woman from attached image 3 (right), both with black ribbons; "
               "incense smoke curling between them, two lit candles. Leave the wooden altar top empty in front of each portrait "
               "for a rice bowl."),
     "desc": "Cận bàn thờ đêm: di ảnh ông (trái) và mẹ (phải) cạnh nhau, khói nhang; chỗ trống trước mỗi ảnh đặt bát",
     "tags": ["bàn thờ", "ông", "mẹ"], "floor_y": 0.8, "char_h": 0.6, "hotspots_needed": ["offering_left", "offering_right"]},
    # ---------------------------------------------------- âm thanh
    {"id": "knitting_needles", "kind": "sound", "sound_kind": "sfx", "desc": "Que đan len gõ lách cách nhẹ, chậm, lặp được",
     "prompt": "Soft slow clicking of two wooden knitting needles, quiet room", "search": "knitting needles clicking",
     "length": "~10s", "tags": ["đan len"], "volume": 0.6},
    {"id": "rice_ladle_scoop", "kind": "sound", "sound_kind": "sfx", "desc": "Muôi gỗ xới cơm lạo xạo vào bát sứ, chậm, từng muôi",
     "prompt": "Wooden paddle slowly scooping cooked rice from a pot into a ceramic bowl, scrape, one scoop at a time",
     "search": "scooping rice bowl spoon", "length": "~8s", "tags": ["xới cơm"], "volume": 0.8},
    {"id": "chickens_cluck", "kind": "sound", "sound_kind": "sfx", "desc": "Mấy con gà mái cục tác, mổ thóc trong sân",
     "prompt": "A few hens clucking and pecking grain in a small yard", "search": "hens clucking yard",
     "length": "~8s", "tags": ["gà"], "volume": 0.6},
    {"id": "market_morning", "kind": "sound", "sound_kind": "sfx", "desc": "Chợ quê buổi sáng: tiếng người nói xa, rao hàng, xe đạp, lặp được",
     "prompt": "Distant morning village market ambience, people chatting, bicycle bells, vendors calling, Asian town",
     "search": "asian morning market ambience", "length": "~20s", "tags": ["chợ"], "volume": 0.5},
    {"id": "cloth_slide", "kind": "sound", "sound_kind": "sfx", "desc": "Tấm vải từ từ trượt xuống rồi rơi khẽ xuống sàn",
     "prompt": "A cloth slowly sliding off a mirror and dropping softly to the floor", "search": "cloth slide fall",
     "length": "~3s", "tags": ["vải", "gương"], "volume": 0.8},
    {"id": "soil_dig_hands", "kind": "sound", "sound_kind": "sfx", "desc": "Bới đất ẩm bằng tay, sột soạt, lặp được",
     "prompt": "Digging into damp soil with bare hands, scraping dirt, close", "search": "digging dirt hands",
     "length": "~6s", "tags": ["bới đất"], "volume": 0.7},
    {"id": "wings_flap", "kind": "sound", "sound_kind": "sfx", "desc": "Chim lớn vỗ cánh bay lên",
     "prompt": "A large crow flapping its wings and taking off", "search": "crow wings flapping take off",
     "length": "~2s", "tags": ["quạ", "vỗ cánh"], "volume": 0.8},
    # ================================================= GÓP Ý PREVIEW P2 #1 (2026-11-01)
    # ảnh tham chiếu của phông: ảnh 1 luôn là ảnh style chung (bg2_hallway), refs bắt đầu từ "attached image 2"
    {"id": "props_sheet_LJ", "kind": "sheet", "character": "props", "grid": [1, 5],
     "why": "góp ý #40–41: đũa trơn không chữ; #61–62: đũa dư chỉ khắc ở đầu trên (4 mặt), hộp dài hơn đôi đũa (P3 dùng tiếp)",
     "note": ("Poses 3, 4 and 5 are the SAME small box: a narrow rectangular old cardboard box, clearly LONGER than a pair of "
              "chopsticks so the chopsticks lie flat inside with room to spare, a red rubber band around it when closed. "
              "The spare chopsticks of pose 2 are the SAME pair shown inside the box in pose 4."),
     "sprites": [
         {"name": "LJ1_chopsticks_plain", "pose": "a pair of plain bamboo chopsticks lying side by side, NO carving, NO letters",
          "desc": "Đôi đũa tre trơn, không khắc chữ", "tags": ["đũa", "trơn"], "facing": "front"},
         {"name": "LJ2_chopsticks_spare_top_carved", "pose": "a pair of square bamboo chopsticks lying side by side; ONLY near the "
          "TOP (thick) end of each chopstick the name KHOA is carved in shaky uneven letters, repeated on each of its four faces "
          "(we see two faces, carving visible on both); the rest of each chopstick is plain smooth bamboo",
          "desc": "Đôi đũa dư: chữ KHOA khắc run run ở ĐẦU TRÊN đũa, đủ bốn mặt; phần còn lại trơn",
          "tags": ["đũa dư", "khắc tên"], "facing": "front"},
         {"name": "LJ3_box_closed_rubberband", "pose": "the box closed with its lid, a red rubber band wrapped around it",
          "desc": "Hộp giấy dài hẹp đậy nắp, quấn dây chun đỏ (dài hơn đôi đũa)", "tags": ["hộp", "đũa dư"], "facing": "front"},
         {"name": "LJ4_box_open_spare", "pose": "the same box open, lid beside it, the spare chopsticks of pose 2 lying inside "
          "lengthwise (carved top ends visible)",
          "desc": "Hộp mở, đôi đũa dư nằm dọc bên trong (thấy đầu khắc chữ)", "tags": ["hộp", "đũa dư"], "facing": "front"},
         {"name": "LJ5_box_open_red_soil", "pose": "the same box open, NO chopsticks inside, only a small pinch of damp dark red "
          "soil at the bottom",
          "desc": "Hộp mở, không còn đũa, chỉ còn nhúm đất đỏ ẩm (P3)", "tags": ["hộp", "đất đỏ"], "facing": "front"},
     ]},
    {"id": "bgL22_backyard_morning", "kind": "background", "refs": ["assets/backgrounds/bg6d_kitchen_day.png"],
     "why": "góp ý #5: bà đổ bát cơm cho gà ở sân sau",
     "scene": ("IMPORTANT: cool gray EARLY MORNING light, ignore the night lighting described above. The small BACKYARD behind the "
               "kitchen of attached image 2: the kitchen back door open on the left, an old brick well and a big clay water jar, a "
               "bamboo clothesline, a banana plant and a low brick wall at the back, bare packed-earth ground. No people, no "
               "animals. Empty ground in the lower third."),
     "desc": "Sân sau bếp buổi sáng xám: cửa bếp bên trái, giếng gạch, chum nước, dây phơi, bụi chuối; nền đất trống",
     "tags": ["sân sau", "sáng"], "floor_y": 0.93, "char_h": 0.48, "hotspots_needed": ["open_ground"]},
    {"id": "bgL23_house_roof_dusk", "kind": "background",
     "refs": ["assets/backgrounds/bgL8_house_alley_dusk.png", "assets/backgrounds/bgL1_porch_day.png"],
     "why": "góp ý #9: cùng căn nhà, cùng giờ chạng vạng như cảnh quạ đậu nóc nhà (#8) — bà đứng sân xua quạ",
     "scene": ("IMPORTANT: DUSK, deep orange sky fading to blue, ignore the night lighting described above. Standing in the small "
               "front yard of the house of attached image 2 and looking UP at it: the mossy tiled roof edge of the old tube house "
               "across the upper part (its ridge clearly visible, a good spot for a bird to perch), the big pomelo tree of attached "
               "image 3 on the right with its branches against the sky, the low front wall. Empty yard ground in the lower third."),
     "desc": "Sân trước lúc chạng vạng nhìn lên nóc nhà mái rêu (chỗ quạ đậu) và cây bưởi bên phải",
     "tags": ["nóc nhà", "cây bưởi", "chạng vạng"], "floor_y": 0.95, "char_h": 0.46,
     "hotspots_needed": ["roof_ridge", "pomelo_branch"]},
    {"id": "bgL9s_grandma_asleep_table", "kind": "background", "refs": ["assets/backgrounds/bgL9_main_room_altar_ong.png", GMA_REF],
     "why": "góp ý #15: bà gục ngủ trên chiếc bàn ăn có sẵn trong gian thờ, trên bàn thờ chỉ có một bát cơm",
     "scene": ("IMPORTANT: this background INCLUDES one person. The SAME room as attached image 2 at night (same altar shelf with "
               "the grandfather's portrait and the small father's portrait, same dining table and stools): the small grandmother "
               "of attached image 3 sits on one of the stools at the dining table, slumped forward asleep with her head on her "
               "folded arms on the table top, exhausted. On the altar shelf ONE full rice bowl with chopsticks standing upright in "
               "front of the grandfather's portrait, the candles burned low."),
     "desc": "Vẽ sẵn: bà gục đầu ngủ trên bàn ăn trong gian thờ ban đêm; bàn thờ có một bát cơm trước ảnh ông",
     "tags": ["gian thờ", "bà", "ngủ gục"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["grandma"]},
    {"id": "bgL24_altar_ong_bo_cold", "kind": "background",
     "refs": ["assets/backgrounds/bg5c_altar_grandpa_cold.png", "assets/backgrounds/bgL9_main_room_altar_ong.png"],
     "why": "góp ý #16: cận bàn thờ phải có cả ảnh thờ bố (như gian thờ bgL9), mặt bàn trống để đặt bát",
     "scene": ("The SAME close view of the altar as attached image 2 (cold, candles out, incense stubs, dust), but next to the "
               "grandfather's portrait stands the SMALL framed portrait of the young father exactly as on the altar of attached "
               "image 3. Leave the wooden altar top in front of the portraits EMPTY (rice bowls will be added)."),
     "desc": "Cận bàn thờ nguội: ảnh ông + ảnh bố nhỏ bên cạnh, nến tắt; mặt bàn trống đặt bát",
     "tags": ["bàn thờ", "ông", "bố"], "floor_y": 0.8, "char_h": 0.6, "hotspots_needed": ["offering_left", "offering_right"]},
    {"id": "bgL25n_mom_bedroom_night", "kind": "background", "refs": ["assets/backgrounds/bgL9_main_room_altar_ong.png"],
     "why": "góp ý #17–23: phòng ngủ riêng của mẹ (không phải phòng may), giường to đặt sát tường",
     "scene": ("The mother's small BEDROOM in the same old house as attached image 2, at NIGHT, deep blue darkness with cold "
               "moonlight from a small window on the left: a LARGE old dark wooden double bed pushed tight AGAINST the back wall on "
               "the right half of the room, its headboard at the LEFT end, a gray-blue blanket and a pale pillow, a mosquito net "
               "tied up above it; a small wardrobe, a bedside stool. The left part of the floor is empty (someone will sit there). "
               "No people."),
     "desc": "Phòng ngủ của mẹ ban đêm: giường gỗ đôi to sát tường (đầu giường bên trái), màn buộc, tủ nhỏ; sàn trái trống",
     "tags": ["phòng mẹ", "đêm", "giường"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["pillow", "bed_foot", "open_floor"]},
    {"id": "bgL25_mom_bed_sick_night", "kind": "background",
     "refs": ["assets/backgrounds/bgL25n_mom_bedroom_night.png", MOM_REF],
     "why": "góp ý #17, #20, #54: mẹ ốm nằm trên giường mới",
     "scene": ("IMPORTANT: this background INCLUDES one person. The SAME bedroom and bed as attached image 2 at night: the mother of "
               "attached image 3, thin and pale with hollow cheeks, lies on her back in the bed under the blanket, head on the "
               "pillow at the left, eyes closed, one thin hand on the blanket. Space at the foot of the bed stays empty."),
     "desc": "Vẽ sẵn: mẹ ốm nằm trên giường trong phòng mẹ ban đêm",
     "tags": ["phòng mẹ", "mẹ ốm", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["bed_foot"]},
    {"id": "bgL25b_mom_bed_bowl_morning", "kind": "background", "refs": ["assets/backgrounds/bgL25_mom_bed_sick_night.png"],
     "why": "góp ý #18: bát cơm đặt sát gối mẹ, đũa nằm ngang miệng bát, đầu đũa chĩa thẳng về phía mẹ",
     "scene": ("IMPORTANT: cold gray EARLY MORNING light, ignore the night lighting described above. The SAME bedroom, bed and "
               "sleeping mother as attached image 2, and on the bed right beside her pillow a full bowl of rice with a pair of "
               "bamboo chopsticks laid ACROSS the top of the bowl, their tips pointing straight at the mother's face. The bowl is "
               "clearly visible and large enough to read."),
     "desc": "Vẽ sẵn sáng xám: mẹ ngủ, bát cơm sát gối, đũa gác ngang miệng bát chĩa về phía mẹ",
     "tags": ["bát cơm", "đầu giường", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["bowl"]},
    {"id": "bgL25c_mom_bed_sit_bowl_morning", "kind": "background", "refs": ["assets/backgrounds/bgL25b_mom_bed_bowl_morning.png"],
     "why": "góp ý #19: mẹ tỉnh dậy ngồi im nhìn bát cơm",
     "scene": ("IMPORTANT: this background INCLUDES one person. The SAME morning bedroom, bed and rice bowl as attached image 2, but "
               "the mother is now SITTING UP in the bed, blanket over her legs, frozen, staring down at the rice bowl beside her "
               "pillow, both hands clutching the blanket, scared."),
     "desc": "Vẽ sẵn sáng xám: mẹ ngồi dậy trên giường nhìn trân trân bát cơm cạnh gối",
     "tags": ["bát cơm", "mẹ", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["bowl"]},
    {"id": "bgL25e_mom_bedroom_day", "kind": "background", "refs": ["assets/backgrounds/bgL25n_mom_bedroom_night.png"],
     "why": "góp ý #23: buổi sáng mẹ khoẻ lại chải tóc trong phòng mình",
     "scene": ("IMPORTANT: warm EARLY MORNING sunlight through the window, ignore the night lighting described above. The SAME "
               "bedroom as attached image 2, the bed neatly made, mosquito net tied up. Empty floor on the left. No people."),
     "desc": "Phòng mẹ buổi sáng nắng, giường gọn; sàn trái trống",
     "tags": ["phòng mẹ", "sáng"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["open_floor"]},
    {"id": "bgL16b_market_side_step", "kind": "background", "refs": ["assets/backgrounds/bgL16_market_morning.png"],
     "why": "góp ý #24: bậc đá nằm ở mép trái chứ không chắn giữa đường",
     "scene": ("IMPORTANT: warm EARLY MORNING sunlight, ignore the night lighting described above. The SAME market entrance as "
               "attached image 2 (awnings, vegetable baskets, sticky-rice stall), but the market road runs open through the "
               "middle, and a low worn STONE STEP (in front of a closed shop) sits only on the LEFT side of the foreground, wide "
               "enough for two people to sit on, golden sunlight on it."),
     "desc": "Đầu chợ buổi sáng: đường giữa thông, bậc đá trước một sạp đóng cửa ở mép trái tiền cảnh",
     "tags": ["chợ", "sáng"], "floor_y": 0.93, "char_h": 0.46, "hotspots_needed": ["stone_step"]},
    {"id": "bgL15b_khoa_bed_awake_plain", "kind": "background",
     "refs": ["assets/backgrounds/bgL15_khoa_bed_awake_night.png", BOY_REF],
     "why": "góp ý #28, #51: Khoa chỉ nằm thức không ngủ được, không đưa tay lên áo",
     "scene": ("IMPORTANT: this background INCLUDES the boy. The SAME bedroom and bed as attached image 2 at night, the black jacket "
               "still hanging on its hook at the head of the bed, but the boy of attached image 3 lies on his back with BOTH hands "
               "resting on the blanket on his chest, eyes wide open staring at the ceiling, unable to sleep; he does NOT touch the "
               "jacket."),
     "desc": "Vẽ sẵn: Khoa nằm thao láo, hai tay để trên chăn (không chạm áo khoác treo đầu giường)",
     "tags": ["phòng ngủ", "mất ngủ", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["boy"]},
    {"id": "bgL26_mom_sewing_tunic", "kind": "background",
     "refs": ["assets/backgrounds/bgL7_mom_room_day.png", MOM_REF, "assets/characters/props/LH2_mourning_tunic_folded.png"],
     "why": "góp ý #31: vẽ sẵn mẹ ngồi khóc bên máy khâu, bộ áo xô nằm trên bàn máy",
     "scene": ("IMPORTANT: this background INCLUDES one person, gray morning light. The SAME sewing room as attached image 2: an "
               "old black treadle sewing machine on its wooden table by the window, and lying on the machine table the finished "
               "beige gauze mourning tunic of attached image 4, neatly sewn; the mother of attached image 3 sits on a stool at the "
               "machine, looking at the tunic and crying, her fingertips covered in tiny red needle pricks; a half-knitted dark-red "
               "child's sweater lies on the floor under the table."),
     "desc": "Vẽ sẵn: mẹ ngồi khóc bên máy khâu, bộ áo xô may xong nằm trên bàn máy, áo len rơi dưới gầm",
     "tags": ["máy khâu", "áo xô", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["mother"]},
    {"id": "bgL27_khoa_peek_door_day", "kind": "background",
     "refs": ["assets/backgrounds/bgL9d_main_room_altar_ong_day.png", BOY_REF],
     "why": "góp ý #36: Khoa nép sau cánh cửa buồng nhìn vào gian thờ",
     "scene": ("IMPORTANT: this background INCLUDES the boy, gray morning light. Seen from just inside a side room: on the RIGHT "
               "the edge of a half-open wooden door and its frame fill the foreground, and the boy of attached image 3 hides "
               "behind it, only half of his body and one wide frightened eye showing as he peeks out, one hand gripping the hem of "
               "his hoodie; through the gap we see the main room of attached image 2 with the altar shelf."),
     "desc": "Vẽ sẵn: Khoa nép sau cánh cửa buồng (bên phải), hé mắt nhìn ra gian thờ",
     "tags": ["nép cửa", "nghe lén", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.5, "hotspots_needed": ["boy"]},
    {"id": "bgL28_khoa_calendar_night", "kind": "background",
     "refs": ["assets/backgrounds/bg1_bedroom.png", BOY_REF, "assets/characters/props/LH3_calendar_circled.png"],
     "why": "góp ý #52: vẽ sẵn Khoa khoanh ngày trên lịch treo tường",
     "scene": ("IMPORTANT: this background INCLUDES the boy. The bedroom of attached image 2 at night, a small desk lamp glowing: "
               "the boy of attached image 3 stands at the wall, side view, circling a date with a pencil on the paper wall "
               "calendar of attached image 4 (many days already circled), worried face."),
     "desc": "Vẽ sẵn: Khoa đứng khoanh ngày trên tờ lịch treo tường dưới ánh đèn bàn",
     "tags": ["lịch", "đếm ngày", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["calendar"]},
    {"id": "bgL29_grandma_room_portrait", "kind": "background",
     "refs": ["assets/backgrounds/bg1_bedroom.png", GMA_REF, PORTRAIT_BG],
     "why": "góp ý #57–58: phòng bà, bà ngồi ôm di ảnh ông khóc (vẽ sẵn)",
     "scene": ("IMPORTANT: this background INCLUDES one person. The grandmother's small old bedroom at night in the same house as "
               "attached image 2, lit by a small oil lamp: a narrow wooden bed, an old chest, a wooden comb and prayer beads on a "
               "shelf; the grandmother of attached image 3 sits on the edge of the bed holding a small framed portrait of the "
               "grandfather (the man in attached image 4) against her chest, tears on her cheeks, whispering to it."),
     "desc": "Vẽ sẵn: phòng bà ban đêm đèn dầu, bà ngồi mép giường ôm di ảnh ông khóc thì thầm",
     "tags": ["phòng bà", "lời hứa", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.5, "hotspots_needed": ["grandma"]},
    {"id": "bgL25h_mom_stroke_khoa_night", "kind": "background",
     "refs": ["assets/backgrounds/bgL25_mom_bed_sick_night.png", BOY_REF],
     "why": "góp ý preview P2 #2 (#68–71): phòng mẹ, mẹ nằm xoa đầu Khoa ngồi cạnh giường khóc",
     "scene": ("IMPORTANT: this background INCLUDES two people. The SAME bedroom, bed and sick mother as attached image 2 at "
               "night: the mother lies in the bed, eyes open, tired gentle face, reaching one thin hand out to stroke the hair of "
               "the boy of attached image 3, who sits on a low stool right beside the bed, head bowed, crying, tears falling on "
               "the back of her hand. Draw the boy only once."),
     "desc": "Vẽ sẵn: phòng mẹ ban đêm, mẹ nằm đưa tay xoa đầu Khoa ngồi ghế cạnh giường cúi đầu khóc",
     "tags": ["phòng mẹ", "mẹ con", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["mother", "boy"]},
    {"id": "props_sheet_LK", "kind": "sheet", "character": "props", "grid": [1, 1],
     "why": "góp ý preview P2 #2: hình minh hoạ đốt đũa riêng (không dùng xô đốt vàng mã)",
     "sprites": [
         {"name": "LK1_chopsticks_burning", "pose": "a pair of bamboo chopsticks with names carved on them, lying crossed on a "
          "small cracked clay dish, burning with small orange flames, a thin curl of gray smoke rising, the carved letters "
          "blackening; nothing else",
          "desc": "Đôi đũa khắc tên nằm chéo trên đĩa đất nung, đang cháy, khói xám bốc lên", "tags": ["đốt đũa", "lửa"],
          "facing": "front"},
     ]},
    # ================================================= GÓP Ý PREVIEW P2 #3 (cảnh 67–117, 2026-11-01)
    {"id": "boy_hoodie_sheet_U", "kind": "sheet", "character": "boy_hoodie", "grid": [1, 6],
     "why": "góp ý #82: chu kỳ chạy hoảng loạn mặc áo khoác đen (chạy qua cánh đồng đêm 48)",
     "note": (JACKET + " A RUN CYCLE of 6 frames, all in strict side view facing RIGHT, same size, same head height, feet "
              "on the same ground line, panicked face, arms pumping, the frames clearly different: 1) right foot strikes "
              "the ground in front; 2) body low, weight on right foot; 3) pushing off, both feet off the ground; 4) left "
              "foot strikes the ground in front; 5) body low, weight on left foot; 6) pushing off, both feet off the ground."
              + SAME_JACKET),
     "refs": [JACKET_REF],
     "sprites": [
         {"name": f"U{k}_run_jacket_{k}", "pose": f"run cycle frame {k} of 6 (see the note)",
          "desc": f"Áo khoác đen: chạy hoảng loạn, khung {k}/6", "tags": ["chạy", "chu kỳ", "áo khoác"], "facing": "right"}
         for k in range(1, 7)
     ]},
    {"id": "boy_hoodie_sheet_V", "kind": "sheet", "character": "boy_hoodie", "grid": [1, 1],
     "why": "góp ý #88: Khoa rón rén theo mẹ ra gian thờ, nép người nhìn trộm",
     "sprites": [
         {"name": "V1_sneak_peek_scared", "pose": "in his green hoodie at night, side view facing LEFT, standing half-crouched "
          "on tiptoe, leaning forward to peek, one hand clutching the front of his hoodie at his chest, the other hand "
          "raised as if touching a wall edge (no wall drawn), wide frightened eyes",
          "desc": "Áo hoodie: rón rén khom người nhìn trộm (quay trái), tay siết ngực áo, mắt mở to sợ",
          "tags": ["nhìn trộm", "rón rén", "sợ"], "facing": "left"},
     ]},
    {"id": "mother_alive_sheet_L", "kind": "sheet", "character": "mother_alive", "grid": [1, 1],
     "why": "góp ý #89: mẹ mộng du đã xới cơm xong, hai tay bưng bát cơm to",
     "note": "She wears EXACTLY the beige gauze mourning tunic and the loose long hair of the LAST attached image, eyes closed.",
     "refs": ["assets/characters/mother_alive/J1_sleepwalk_stand.png"],
     "sprites": [
         {"name": "L1_sleepwalk_hold_bowl", "pose": "side view facing LEFT, standing still, holding with BOTH hands in front of "
          "her chest a LARGE full bowl of rice packed into a dome, eyes closed, calm blank face",
          "desc": "Mộng du (quay trái): hai tay bưng bát cơm đầy to trước ngực, mắt nhắm", "tags": ["mộng du", "bát cơm"],
          "facing": "left"},
     ]},
    {"id": "bgL30_khoa_dig_grave_night", "kind": "background",
     "refs": ["assets/backgrounds/bgL17_cemetery_night_grave.png", BOY_REF, JACKET_REF],
     "why": "góp ý #77: vẽ sẵn Khoa quỳ bới đất ở đầu mộ ông",
     "scene": ("IMPORTANT: this background INCLUDES the boy. The SAME night cemetery and grandfather's new red-earth grave as "
               "attached image 2, seen a little closer: the boy of attached image 3, wearing the black jacket of attached image "
               "4, kneels at the HEAD of the grave right beside the small headstone, digging a SMALL hole in the red earth with "
               "his bare dirty hands; his lit flashlight lies on the ground beside him throwing a cone of light on the hole; "
               "a folded yellow paper and a pair of chopsticks lie next to his knee. Thin mist, the dry kapok tree behind."),
     "desc": "Vẽ sẵn: Khoa (áo khoác đen) quỳ bới lỗ nhỏ ở đầu mộ ông, đèn pin nằm cạnh",
     "tags": ["nghĩa địa", "bới đất", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["boy", "hole"]},
    {"id": "bgL25s_khoa_feed_soup", "kind": "background",
     "refs": ["assets/backgrounds/bgL25_mom_bed_sick_night.png", BOY_REF],
     "why": "góp ý #84: vẽ sẵn Khoa bón canh cho mẹ trong phòng mẹ (chiều ngày 49)",
     "scene": ("IMPORTANT: this background INCLUDES two people, soft late-afternoon light through the window, ignore the night "
               "lighting described above. The SAME bedroom and bed as attached image 2: the thin pale mother sits up leaning on "
               "the pillow; the boy of attached image 3 sits on the edge of the bed holding a small bowl of crab soup and gently "
               "feeding her one spoonful. Draw the boy only once."),
     "desc": "Vẽ sẵn: chiều, Khoa ngồi mép giường bón canh cho mẹ trong phòng mẹ",
     "tags": ["phòng mẹ", "bón canh", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["mother", "boy"]},
    {"id": "bgL25k_mom_knit_collar", "kind": "background",
     "refs": ["assets/backgrounds/bgL25_mom_bed_sick_night.png", BOY_REF, "assets/characters/props/LH1_sweater_unfinished.png"],
     "why": "góp ý #85: vẽ sẵn mẹ ngồi trên giường cố đan cổ áo len, tay run",
     "scene": ("IMPORTANT: this background INCLUDES two people, soft late-afternoon light through the window, ignore the night "
               "lighting described above. The SAME bedroom and bed as attached image 2: the thin mother sits up in bed holding "
               "the unfinished dark-red sweater of attached image 4 and two knitting needles, trying to knit the collar, her thin "
               "hands trembling, the yarn slipping; the boy of attached image 3 sits beside the bed watching her sadly."),
     "desc": "Vẽ sẵn: mẹ ngồi trên giường cố đan cổ áo len, tay run; Khoa ngồi cạnh nhìn",
     "tags": ["phòng mẹ", "áo len", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["mother"]},
    {"id": "bgL31_mirror_opposite_room", "kind": "background",
     "refs": ["assets/backgrounds/bgL19_mirror_ong_behind_mom.png", "assets/backgrounds/bgL9_main_room_altar_ong.png"],
     "why": "góp ý #90: tấm vải đỏ tuột khỏi chiếc gương lớn trong căn phòng đối diện",
     "scene": ("Night, very dark. Seen from the altar room of attached image 3, looking through an open doorway into the room "
               "OPPOSITE: inside it stands the SAME tall wooden-framed mirror as attached image 2, and the red cloth that covered "
               "it is sliding off, half of the dark glass already showing, the cloth falling in a heap onto the floor. No people "
               "visible; the glass shows only darkness."),
     "desc": "Nhìn qua khung cửa sang phòng đối diện: tấm vải đỏ đang tuột khỏi chiếc gương lớn",
     "tags": ["gương", "vải đỏ", "đêm 49"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["mirror"]},
    {"id": "bgL25m_khoa_hold_mom_hand", "kind": "background",
     "refs": ["assets/backgrounds/bgL25_mom_bed_sick_night.png", BOY_REF, "assets/characters/mother_alive/J1_sleepwalk_stand.png"],
     "why": "góp ý #97–98: vẽ sẵn Khoa ngồi bệt bên giường áp tay mẹ lên má",
     "scene": ("IMPORTANT: this background INCLUDES two people. The SAME bedroom and bed as attached image 2 at night: the mother "
               "now wears the beige gauze mourning tunic of attached image 4, long black hair loose on the pillow, lying on her "
               "side, eyes closed, breathing weakly; the boy of attached image 3 sits slumped on the floor beside the bed, holding "
               "her limp hand with both hands pressed against his cheek, crying. Draw the boy only once."),
     "desc": "Vẽ sẵn: mẹ (áo xô, tóc xoã) nằm thở yếu, Khoa ngồi bệt áp tay mẹ lên má khóc",
     "tags": ["phòng mẹ", "đêm 49", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["mother", "boy"]},
    {"id": "bgL25d_mom_dead_morning", "kind": "background",
     "refs": ["assets/backgrounds/bgL25e_mom_bedroom_day.png", "assets/characters/mother_alive/J1_sleepwalk_stand.png"],
     "why": "góp ý #99: trời sáng, mẹ nằm mất trên giường trong áo xô",
     "scene": ("IMPORTANT: this background INCLUDES one person, pale cold early morning light, ignore the night lighting "
               "described above. The SAME bedroom and bed as attached image 2: the mother in the beige gauze mourning tunic of "
               "attached image 3 lies on her side as if asleep, peaceful face, eyes closed, long hair loose, her hands resting "
               "on her chest with tiny red needle pricks on the fingertips. Very still and quiet."),
     "desc": "Vẽ sẵn: sáng sớm lạnh, mẹ (áo xô) nằm mất trên giường, bình thản như ngủ",
     "tags": ["phòng mẹ", "mẹ mất", "vẽ sẵn"], "floor_y": 0.93, "char_h": 0.5, "hotspots_needed": ["mother"]},
    {"id": "bgL20b_wake_coffin_mom_open", "kind": "background",
     "refs": ["assets/backgrounds/bgL2_wake_coffin.png", MOM_PORTRAIT],
     "why": "góp ý #100: đám tang mẹ giống hệt gian thờ đám ông (quan tài mở nắp), chỉ thay di ảnh bằng mẹ",
     "scene": ("The SAME funeral room as attached image 2, exactly the same layout (open coffin in the middle with the head on "
               "the left, the lid leaning on the right wall, two candles, paper wreaths, mat in front), but the framed portrait "
               "on the altar is the woman of attached image 3 with a black ribbon."),
     "desc": "Gian thờ đám tang mẹ (cùng bố cục bgL2): quan tài mở nắp, di ảnh mẹ",
     "tags": ["đám tang", "mẹ", "đêm"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["coffin_head"]},
    {"id": "bgL3m_coffin_mom_hand_talisman", "kind": "background", "style": COFFIN_STYLE,
     "refs": ["assets/backgrounds/bgL3f_coffin_hand_talisman.png", "assets/characters/mother_alive/J1_sleepwalk_stand.png"],
     "why": "góp ý #102: như cảnh tay thầy Tư nhét bùa dưới gối ông, nhưng người nằm là mẹ",
     "scene": ("The SAME top-down view of an open coffin as attached image 2 (same framing, candles, the thin hand in a dark "
               "brown sleeve reaching in from the TOP edge), but the person lying in the coffin is the woman of attached image "
               "3: beige gauze mourning tunic, long black hair spread on the pillow, eyes closed, hands on her chest, a thin RED "
               "thread tied around her wrist; the hand slides a small yellow paper folded in four under her pillow."),
     "desc": "Cận từ trên: mẹ (áo xô) nằm trong quan tài, chỉ đỏ ở cổ tay, tay thầy Tư nhét bùa dưới gối",
     "tags": ["quan tài", "mẹ", "lá bùa"], "floor_y": 0.95, "char_h": 0.4, "hotspots_needed": ["pillow"]},
    {"id": "bgL17c_two_graves_small_hole", "kind": "background",
     "refs": ["assets/backgrounds/bgL17b_two_graves_day.png"],
     "why": "góp ý #108–109: lỗ đất ở đầu mộ ông quá to — chỉ là một lỗ nhỏ một đứa trẻ bới bằng tay",
     "scene": ("IMPORTANT: overcast gray DAYTIME, ignore the night lighting described above. The SAME two graves, headstones and "
               "kapok tree as attached image 2, but at the head of the left (grandfather's) grave there is only a SMALL shallow "
               "hand-dug hollow, about the size of a child's two hands, with a few clods of red earth scattered around and small "
               "finger marks in the soil. Everything else unchanged. No people."),
     "desc": "Hai mộ cạnh nhau ban ngày; đầu mộ ông chỉ có một lỗ nhỏ trẻ con bới, đất vương vãi",
     "tags": ["nghĩa địa", "hai mộ"], "floor_y": 0.95, "char_h": 0.42, "hotspots_needed": ["hole", "crow_branch"]},
    {"id": "bgL21b_altar_three", "kind": "background",
     "refs": ["assets/backgrounds/bgL24_altar_ong_bo_cold.png", MOM_PORTRAIT],
     "why": "góp ý #110: cận bàn thờ có đủ ảnh ông, ảnh bố cũ và thêm ảnh mẹ; mặt bàn trống đặt bát",
     "scene": ("The SAME close view of the altar as attached image 2 (grandfather's portrait in the middle, the small old "
               "portrait of the young father), now with incense smoke and two lit candles, and a NEW framed portrait of the "
               "woman of attached image 3 with a black ribbon standing on the other side. Leave the wooden altar top in front of "
               "the grandfather and the mother EMPTY (rice bowls will be added)."),
     "desc": "Cận bàn thờ: ảnh ông (giữa), ảnh bố, ảnh mẹ mới; nhang khói, nến; mặt bàn trống đặt bát",
     "tags": ["bàn thờ", "ông", "bố", "mẹ"], "floor_y": 0.8, "char_h": 0.6, "hotspots_needed": ["offering_ong", "offering_me"]},
    {"id": "bgL9m_main_room_altar_three", "kind": "background",
     "refs": ["assets/backgrounds/bgL9_main_room_altar_ong.png", MOM_PORTRAIT],
     "why": "góp ý #113, #116: gian thờ sau tang mẹ — kệ thờ có ảnh ông, ảnh bố và ảnh mẹ",
     "scene": ("The SAME room as attached image 2 at night (same altar shelf, dining table, stools, calendar, door), but the altar "
               "shelf now holds THREE portraits: the grandfather, the small father, and the woman of attached image 3 with a "
               "black ribbon; two full rice bowls with chopsticks standing upright, incense smoke. Empty floor on the left."),
     "desc": "Gian chính đêm: kệ thờ có ảnh ông, bố, mẹ và hai bát cơm",
     "tags": ["gian thờ", "ba di ảnh", "đêm"], "floor_y": 0.95, "char_h": 0.46, "hotspots_needed": ["altar_shelf"]},
    {"id": "bgL19c_mirror_ong_whisper", "kind": "background",
     "refs": ["assets/backgrounds/bgL19_mirror_ong_behind_mom.png", ONG_BASE,
              "assets/characters/mother_alive/L1_sleepwalk_hold_bowl.png"],
     "why": "góp ý preview P2 #4 (#91): trong gương — mẹ bưng bát cơm, ông đứng sau đặt tay lên tay mẹ, ghé tai thì thầm (không xới cơm, không thấy bàn thờ)",
     "scene": ("IMPORTANT: this background INCLUDES two people seen in a mirror. The SAME tall wooden-framed mirror, dark room and "
               "red cloth on the floor as attached image 2. In the glass: the mother of attached image 4 (beige gauze mourning "
               "tunic, long loose hair, eyes closed) stands holding a full bowl of rice with both hands; right behind her the "
               "grandfather of attached image 3 in a dark blue ao the funeral robe, grayish skin, lays his dry thin right hand "
               "over her hands on the bowl and leans down close to her ear, whispering. Only darkness behind them in the mirror "
               "(NO altar, NO candles, NO rice pot, NO paddle)."),
     "desc": "Vẽ sẵn: trong gương, mẹ bưng bát cơm, ông áo the đứng sau đặt tay lên tay mẹ, ghé tai thì thầm",
     "tags": ["gương", "ông", "mẹ", "vẽ sẵn"], "floor_y": 0.95, "char_h": 0.5, "hotspots_needed": ["mirror"]},
]


# ============================================================ BỘ DỰNG CẢNH
S = []


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


def silent(bg, seconds, layers=(), camera=None, sounds=(), **kw):
    """Cảnh không lời (đánh dấu *[Không lời …]* trong md)."""
    return scene(bg, None, layers, camera, sounds, duration=seconds, **kw)


def L(sprite, x=0.5, y="floor", **kw):
    return {"sprite": sprite, "x": x, "y": y, **kw}


def day(layer):
    return {**layer, "tint": False}


def walk(char, x, fps=2.5, end=None, cyc="walk", **kw):
    d = {"cycle": f"{char}/{cyc}", "fps": fps, "x": x, "y": "floor", "face": "auto", "breathe": 0, **kw}
    if end:
        d["end"] = end
    return d


def beat(par, *shots):
    """Một đoạn văn → các cảnh: mỗi phần lời (tách theo câu) dùng một shot (dict tham số scene), thiếu thì lặp shot cuối."""
    first = None
    for k, txt in enumerate(chunks(par)):
        sh = dict(shots[min(k, len(shots) - 1)])
        bg = sh.pop("bg")
        sid = scene(bg, txt, **sh)
        first = first or sid
    return first


def V(bg, layers=(), camera=None, sounds=(), **kw):
    return {"bg": bg, "layers": list(layers), "camera": camera, "sounds": list(sounds), **kw}


# âm thanh nền hay dùng
INSECTS = lambda n=12, v=0.35: sfx("night_insects", 0, v, True, n)
CLOCK = lambda n=10, v=0.3: sfx("clock_tick", 0, v, True, n)
WIND = lambda n=12, v=0.45: sfx("wind_field", 0, v, True, n)
WOOD = lambda n=12, v=0.35: sfx("wood_block_slow", 0, v, True, n)
BAND = lambda n=14, v=0.4: sfx("funeral_band", 0, v, True, n)

# chỗ đặt trên phông có sẵn (đo ở truyện trước) / ước lượng cho phông mới — chỉnh lại sau khi có phông
STOOL_L = dict(x=0.585, y=0.835, h=0.46)       # bg4: ghế đẩu trái
STOOL_R = dict(x=0.86, y=0.78, h=0.5)        # bg4: ghế đẩu phải
GATE_GAP = [0.625, 0.04, 0.76, 0.62]   # bg7: khe giữa hai cánh cổng sắt — quạ bay ngoài xa chỉ hiện trong khe
BED_D = dict(x=0.5, y=0.93, h=0.4)          # giường tre ông nằm một mình (sheet D) trên bgL11: nhỏ hơn bản có bà
BED_ONG = dict(x=0.5, y=0.95, h=0.52)        # giường tre ông trên bgL11 (góc nhà cạnh gian thờ)
PORCH_STOOL = dict(x=0.32, y=0.93, h=0.5)    # bgL1: ghế đẩu ngoài hiên
COFFIN_HEAD = dict(x=0.28, y=0.95)           # bgL2: phía đầu quan tài
COFFIN_SIDE = dict(x=0.5, y=0.95)
COFFIN_FOOT = dict(x=0.72, y=0.95)

# ============================================================ PHẦN 1 — GIỜ DẦN
def part1():
    P = paragraphs("## Mở đầu", "## Phần 2")
    assert len(P) == 72, f"md Phần 1 đổi số đoạn ({len(P)}) — rà lại chỉ số đoạn bên dưới"

    # ---- mở đầu: bốn bát cơm
    BOWLS4 = [L("props/LF1_bowl_chopsticks_upright", x, 0.625, h=0.14) for x in (0.33, 0.44, 0.565, 0.67)]   # bgL10b: trước từng di ảnh, lư hương ở giữa
    a_open = beat(P[0],
                  V("bgL10b_altar_four_portraits", BOWLS4[:3], cam((0, 1.15, 0.5, 0.55), (1, 1.3, 0.42, 0.6, "smooth")),
                    [INSECTS(14, 0.3), CLOCK(14, 0.25)], fade_in=2.0),
                  V("bgL10b_altar_four_portraits", BOWLS4, cam((0, 1.3, 0.62, 0.55), (1, 1.9, 0.8, 0.55, "in")),
                    [CLOCK(14, 0.3), sfx("heartbeat", 0.3, 0.4, True, 10)]))
    beat(P[1], V("bg7_front_yard", [walk("props", [0.58, 0.8], fps=6, cyc="crow_fly", y=0.22, h=0.035, start=0.25, end=0.8, clip_rect=GATE_GAP)],
                 cam((0, 1.2, 0.55, 0.45), (1, 1.35, 0.5, 0.4, "smooth")), [INSECTS(14, 0.3), sfx("crow_caw", 0.6, 0.7)]))
    beat(P[2],
         V("bgL2_wake_coffin", [L("boy_hoodie/N5_stuff_pocket_guilty", 0.62)],
           cam((0, 1.2, 0.6, 0.6), (1, 1.4, 0.62, 0.58)), [sfx("heartbeat", 0, 0.5, True, 10), WOOD(10, 0.2)], bg_dim=0.3),
         V("black", [L("props/LB2_talisman_open", 0.5, 0.85, h=[0.6, 0.75], glow=True, tint=False)],
           None, [sfx("reverse_swell", 0.5, 0.6)]))
    silent("black", 4.5, title_text="LÁ BÙA DƯỚI GỐI ÔNG", fade_in=0.8, fade_out=1.0,
           sounds=[sfx("chopsticks_tap_2", 0.6, 0.8), sfx("crow_caw", 2.6, 0.5)])
    silent("black", 3.0, title_text="Phần 1 — Giờ Dần", fade_in=0.5, fade_out=0.8, sounds=[CLOCK(3, 0.4)])
    a_open_end = len(S)

    # ---- gia đình (kỷ niệm ấm — nhạc piano)
    a_home = beat(P[3], V("bgL8_house_alley_dusk", [], cam((0, 1.25, 0.4, 0.55), (1, 1.25, 0.6, 0.5, "smooth")),
                          [sfx("night_insects", 0, 0.2, True, 12)], fade_in=1.2))
    beat(P[4], V("bg4_main_room", [], cam((0, 1.2, 0.5, 0.55), (1, 1.8, 0.31, 0.3, "smooth")), [CLOCK(10, 0.2)]))
    beat(P[5], V("bgL7_mom_room_day", [day(L("mother_alive/E2_sit_sewing_machine", 0.25, h=0.55))],
                 cam((0, 1.2, 0.42, 0.6), (1, 1.35, 0.4, 0.62)), [sfx("sewing_machine", 0, 0.5, True, 6, 0, 1.2)]))
    beat(P[6], V("bg6d_kitchen_day", [day(walk("grandma", [0.8, 0.35], fps=2.5, end=0.85)),
                                      day(L("grandma/A5_scoop_rice", 0.35, start=0.85))],
                 cam((0, 1.2, 0.6, 0.6), (1, 1.2, 0.4, 0.6, "smooth")), [sfx("slipper_drag", 0, 0.4, True, 8)]))
    beat(P[7], V("bg4_main_room", [L("mother_alive/E1_fit_jacket_boy", 0.35, h=0.5)],
                 cam((0, 1.2, 0.38, 0.62), (1, 1.4, 0.36, 0.6)), [INSECTS(10, 0.2)]))
    beat(P[8], V("bg4_main_room", [L("mother_alive/E1_fit_jacket_boy", 0.35, h=0.5)],
                 cam((0, 1.4, 0.36, 0.6), (1, 1.7, 0.36, 0.58, "smooth")), [INSECTS(10, 0.2)]))
    beat(P[9],
         V("bgL1_porch_day", [day(L("ong_noi/A1_sit_stool_carve", **PORCH_STOOL))],
           cam((0, 1.2, 0.45, 0.6), (1, 1.35, 0.38, 0.62)), [sfx("bamboo_whittle", 0, 0.5, True, 12)]),
         V("black", [day(L("ong_noi/B5_closeup_hands_carve", 0.5, 1.0, h=0.95))], cam((0, 1.0, 0.5, 0.5), (1, 1.15, 0.5, 0.5)),
           [sfx("bamboo_whittle", 0, 0.6, True, 12)]))
    beat(P[10], V("bg4e_main_room_day_bo", [day(L("props/LB6_chopstick_holder", 0.665, 0.585, h=0.1))],
                  cam((0, 1.3, 0.7, 0.55), (1, 1.8, 0.73, 0.52, "smooth")), [sfx("bamboo_whittle", 0, 0.3, True, 10)]))
    beat(P[11],
         V("bgL1_porch_day", [day(L("boy_hoodie/O3_hold_broken_chopstick", 0.62)), day(L("ong_noi/C1_stand_snatch_broken_full", 0.8, face="left"))],
           cam((0, 1.2, 0.65, 0.6), (1, 1.3, 0.7, 0.6))),
         V("bgL1_porch_day", [day(L("ong_noi/C1_stand_snatch_broken_full", 0.6, face="left"))],
           cam((0, 1.5, 0.6, 0.55), (1, 1.9, 0.6, 0.5, "in")), [sfx("whisper_eerie", 0.7, 0.15)]))
    beat(P[12], V("black", [day(L("props/LF3_chopsticks_khoa", 0.5, 0.8, h=0.5))],
                  cam((0, 1.15, 0.5, 0.5), (1, 1.3, 0.5, 0.5)), [sfx("chopsticks_tap_2", 0.6, 0.8)]))
    # bữa cơm: ông đầu mâm (ghế phải), Khoa ghế trái, bà đứng xới cơm, mẹ ngồi quay lưng ở tiền cảnh
    DINNER = [day(L("ong_noi/C2_sit_stool_eat_side", 0.86, 0.8, h=0.42, face="left")), day(L("boy_hoodie/O4_sit_stool_eat_chat", **STOOL_L)),
              day(L("grandma/A5_scoop_rice", 0.44, 0.9, h=0.44)), day(L("mother_alive/G1_sit_stool_eat_back", 0.72, 1.04, h=0.5))]
    beat(P[13], V("bg4e_main_room_day_bo", DINNER, cam((0, 1.2, 0.7, 0.6), (1, 1.3, 0.72, 0.6)),
                  [sfx("chopsticks_clatter", 0, 0.15, True, 12)]))
    beat(P[14], V("bg4e_main_room_day_bo", DINNER, cam((0, 1.35, 0.72, 0.6), (1, 1.15, 0.6, 0.6, "smooth")),
                  [sfx("night_insects", 0, 0.15, True, 12)]))
    beat(P[15], V("bg4e_main_room_day_bo", DINNER, cam((0, 1.3, 0.6, 0.6), (1, 1.4, 0.66, 0.6, "smooth"))))  # Khoa hỏi
    TELL = [day(L("ong_noi/C3_sit_stool_tell_story_side", 0.86, 0.8, h=0.42, face="left")), DINNER[1]]
    silent("bg4e_main_room_day_bo", 2.2, TELL, cam((0, 1.5, 0.8, 0.55), (1, 1.75, 0.84, 0.52, "smooth")),   # ông khựng lại
           [CLOCK(3, 0.3)])
    a_aunt = beat(P[16], V("bg4e_main_room_day_bo", TELL, cam((0, 1.75, 0.84, 0.52), (1, 1.9, 0.85, 0.5))),  # ông nhìn ra sân, bắt đầu kể
                  V("bgL6_old_village_altar_sepia", [], cam((0, 1.2, 0.3, 0.5), (1, 1.2, 0.6, 0.5, "smooth")),
                           [sfx("wind_field", 0, 0.25, True, 14)], fade_in=1.0),
                  V("bgL6_old_village_altar_sepia", [], cam((0, 1.35, 0.55, 0.45), (1, 1.5, 0.7, 0.45, "smooth")),
                    [sfx("ritual_bell", 0.2, 0.4)]),
                  V("bgL6_old_village_altar_sepia", [], cam((0, 1.2, 0.8, 0.55), (1, 1.2, 0.85, 0.6)),
                    [sfx("wind_field", 0, 0.2, True, 10)]))
    beat(P[17], V("bgL6_old_village_altar_sepia", [], cam((0, 1.3, 0.6, 0.45), (1, 2.0, 0.72, 0.42, "in")),
                  [sfx("reverse_swell", 0.5, 0.5)]))
    beat(P[18],
         V("bg4e_main_room_day_bo", [DINNER[0], DINNER[1]],
           cam((0, 1.4, 0.78, 0.6), (1, 1.4, 0.72, 0.6)), [sfx("chopsticks_tap_2", 0.25, 0.8)]),
         V("bg4_main_room", [L("ong_noi/B3_back_sit_altar_with_grandma", 0.31, h=0.42)],
           cam((0, 1.25, 0.32, 0.55), (1, 1.45, 0.31, 0.45, "smooth")), [CLOCK(12, 0.25)], fade_out=0.6))
    a_home_end = len(S)

    # ---- ông ốm, đêm ông mất
    a_sick = beat(P[19], V("bgL1_porch_day", [day(L("ong_noi/B4_sit_stool_cough", **PORCH_STOOL))],
                           cam((0, 1.2, 0.4, 0.6), (1, 1.35, 0.35, 0.6)),
                           [sfx("old_man_cough", 0.15, 0.9), sfx("old_man_cough", 0.65, 0.7), sfx("wind_field", 0, 0.2, True, 10)]))
    beat(P[20],
         V("bgL11_ong_bed_corner_night", [L("ong_noi/D1_bed_lie_side_watch_clock", **BED_D, face="left", end=0.74),     # nằm thức, rồi giật mình
                                          L("ong_noi/D2_bed_jolt_awake", **{**BED_D, "h": BED_D["h"] * 1072 / 752}, face="left", start=0.74)],  # lật gương cả hai: ông ngoái về phía đồng hồ (trái); D2 cao hơn nên h theo tỉ lệ
           cam((0, 1.25, 0.5, 0.55), (1, 1.25, 0.5, 0.55)), [CLOCK(12, 0.4), sfx("breath_close", 0.74, 0.45)], bg_dim=0.2),  # đổi D1→D2 đúng chữ "giật mình"; máy đứng yên: đổi D1→D2 không lệch
         V("black", [L("props/LC4_wall_clock_three", 0.5, 0.9, h=0.8)], cam((0, 1.15, 0.5, 0.5), (1, 1.25, 0.5, 0.45, "smooth")),
           [CLOCK(12, 0.5), sfx("rooster_crow", 0.55, 0.35)]))                                          # gà gáy: hết giờ Dần
    beat(P[21], V("bgL1_porch_day", [day(L("ong_noi/B4_sit_stool_cough", **PORCH_STOOL))],
                  cam((0, 1.3, 0.35, 0.6), (1, 1.3, 0.4, 0.6)), [sfx("wind_field", 0, 0.25, True, 10)]))
    beat(P[22],
         V("bgL1_porch_day", [day(L("ong_noi/A6_give_chopsticks_boy", 0.45, h=0.52))], cam((0, 1.2, 0.45, 0.6), (1, 1.45, 0.45, 0.58))),
         V("black", [day(L("props/LG1_chopsticks_spare_ugly", 0.5, 0.78, h=0.5))], cam((0, 1.0, 0.5, 0.5), (1, 1.2, 0.5, 0.5))),
         V("bg1_bedroom", [L("boy_hoodie/R1_floor_box_spare_chopsticks", 0.58, 0.86, h=0.34)], cam((0, 1.2, 0.6, 0.62), (1, 1.4, 0.6, 0.65))))
    a_night = beat(P[23], V("bgL11_ong_bed_corner_night",
                            [L("ong_noi/B1_bed_dying_grandma_hold", **BED_ONG),
                             walk("mother_alive", [1.05, 0.82], fps=2.0, cyc="walk")],
                            cam((0, 1.2, 0.55, 0.6), (1, 1.3, 0.55, 0.6)), [sfx("old_man_breath", 0, 0.4, True, 12), CLOCK(12, 0.3)]))
    beat(P[24], V("bg1_bedroom", [L("boy_hoodie/G3_bed_blanket_chin_scared", 0.7, 0.95, h=0.5)],
                  cam((0, 1.2, 0.62, 0.6), (1, 1.45, 0.68, 0.62, "in")),
                  [sfx("old_man_breath", 0, 0.5, True, 12), CLOCK(12, 0.45)]))
    a_death = beat(P[25], V("bgL11_ong_bed_corner_night", [L("ong_noi/B1_bed_dying_grandma_hold", **BED_ONG)],
                            cam((0, 1.4, 0.5, 0.6), (1, 1.6, 0.48, 0.62)),
                            [sfx("clock_chime_3", 0.0, 0.9), sfx("old_man_breath", 0, 0.4, False, 2.5, 0, 1.0),
                             sfx("woman_sob_door", 0.55, 0.5)]))
    beat(P[26], V("bgL11_ong_bed_corner_night", [L("ong_noi/B2_bed_dead_eyes_open_grandma", **BED_ONG),
                                    L("boy_hoodie/Q2_frozen_hands_mouth", 0.88, jitter=1)],
                  cam((0, 1.2, 0.6, 0.6), (1, 1.5, 0.5, 0.55, "in")), [sfx("woman_sob_door", 0, 0.4)]))
    beat(P[27], V("bgL11_ong_bed_corner_night", [L("ong_noi/B2_bed_dead_eyes_open_grandma", **BED_ONG, end=0.65),
                                    L("ong_noi/C4_bed_eyes_closed_grandma_cry", **BED_ONG, start=0.65)],
                  cam((0, 1.5, 0.48, 0.62), (1, 1.7, 0.5, 0.64, "smooth")), [sfx("woman_sob_door", 0, 0.45), CLOCK(10, 0.2)],
                  fade_out=1.0))
    a_death_end = len(S)

    # ---- thầy Tư, giờ trùng, kiêng kỵ, khâm liệm, lá bùa
    a_thay = beat(P[28], V("bg7d_front_yard_morning", [day(walk("boy_hoodie", [0.3, 0.69], fps=6, cyc="run_away", y=[0.97, 0.66], h=[0.46, 0.16]))],
                           cam((0, 1.2, 0.5, 0.6), (1, 1.2, 0.62, 0.55, "smooth")), [sfx("footsteps_run", 0, 0.5)], fade_in=0.8))
    beat(P[29], V("bgL12_living_room_day", [day(L("thay_tu/A1_sit_mat_almanac", 0.56, h=0.35))] + [day(L("mother_alive/G3_kneel_mat_worried", 0.2, h=0.42)), day(L("grandma/M2_kneel_mat_worried", 0.32, h=0.38)), day(L("boy_hoodie/Q3_kneel_mat_worried", 0.8, h=0.34, face="left"))],
                  cam((0, 1.2, 0.5, 0.62), (1, 1.35, 0.55, 0.6)), [sfx("chant_murmur", 0, 0.3, True, 10)]))
    beat(P[30], V("bgL12_living_room_day", [day(L("thay_tu/A2_sit_mat_pale", 0.56, h=0.35))] + [day(L("mother_alive/G3_kneel_mat_worried", 0.2, h=0.42)), day(L("grandma/M2_kneel_mat_worried", 0.32, h=0.38)), day(L("boy_hoodie/Q3_kneel_mat_worried", 0.8, h=0.34, face="left"))],
                  cam((0, 1.4, 0.56, 0.62), (1, 1.9, 0.56, 0.6, "in")), [sfx("reverse_swell", 0.4, 0.5)]))
    THREE = [L("props/LF1_bowl_chopsticks_upright", x, 0.72, h=0.24, start=st, tint=False)
             for x, st in ((0.3, 0.15), (0.5, 0.45), (0.7, 0.75))]
    beat(P[31],
         V("bgL12_living_room_day", [day(L("thay_tu/A2_sit_mat_pale", 0.56, h=0.35))] + [day(L("mother_alive/G3_kneel_mat_worried", 0.2, h=0.42)), day(L("grandma/M2_kneel_mat_worried", 0.32, h=0.38)), day(L("boy_hoodie/Q3_kneel_mat_worried", 0.8, h=0.34, face="left"))], cam((0, 1.5, 0.56, 0.66), (1, 1.7, 0.56, 0.68))),
         V("black", THREE, None, [sfx("chopsticks_tap_2", 0.15, 0.4), sfx("chopsticks_tap_2", 0.45, 0.5),
                                  sfx("chopsticks_tap_2", 0.75, 0.6)]))
    beat(P[32], V("bgL12_living_room_day", [day(L("mother_alive/E3_hug_grandma_cry", 0.45, h=0.55))],
                  cam((0, 1.25, 0.6, 0.6), (1, 1.5, 0.6, 0.55)), [sfx("woman_sob_door", 0, 0.35)]))
    beat(P[33],
         V("bg1_bedroom", [L("props/LC3_mirror_red_cloth", 0.8, 0.62, h=0.36)], cam((0, 1.2, 0.6, 0.5), (1, 1.45, 0.78, 0.5, "smooth"))),
         V("bg7d_front_yard_morning", [day(L("cat_tabby/A1_stand_look", 0.35, h=0.13))], cam((0, 1.4, 0.38, 0.75), (1, 1.6, 0.36, 0.78))))
    beat(P[34], V("bgL2_wake_coffin", [L("thay_tu/A5_stand_point_stern", 0.78)], cam((0, 1.2, 0.6, 0.6), (1, 1.35, 0.7, 0.58)),
                  [WOOD(10, 0.3)]))
    beat(P[35], V("bgL3d_coffin_top_full", [], cam((0, 1.15, 0.5, 0.5), (1, 1.2, 0.44, 0.48, "smooth")),
                  [sfx("chant_murmur", 0, 0.4, True, 10), WOOD(10, 0.2)]))
    beat(P[36], V("bgL3d_coffin_top_full", [L("mother_alive/G4_topdown_back_lean", 0.46, 0.34, h=0.5)],   # mẹ cúi từ mép trên quan tài
                  cam((0, 1.05, 0.45, 0.45), (1, 1.15, 0.44, 0.45)), [sfx("woman_sob_door", 0, 0.35), WOOD(10, 0.2)]))
    silent("bgL3d_coffin_top_full", 2.4, camera=cam((0, 1.6, 0.44, 0.45), (1, 1.8, 0.44, 0.45)),
           sounds=[sfx("water_drip", 0.6, 0.7)])                                             # giọt nước mắt rơi xuống tay phải
    beat(P[37], V("bgL2_wake_coffin", [L("mother_alive/G2_stand_worried", 0.36, h=0.5),                  # thầy quát, mẹ hốt hoảng
                                        L("thay_tu/A5_stand_point_stern", 0.74, h=0.44, face="left")],
                  cam((0, 1.2, 0.55, 0.6), (1, 1.3, 0.6, 0.58, "in"), handheld=3), [sfx("door_slam", 0.05, 0.4)]))
    beat(P[38],
         V("bgL2_wake_coffin", [L("thay_tu/A3_write_talisman", 0.65, h=0.42)], cam((0, 1.3, 0.65, 0.62), (1, 1.5, 0.65, 0.6)),
           [sfx("chant_murmur", 0, 0.4, True, 12)]),
         V("bgL3f_coffin_hand_talisman", [], cam((0, 1.15, 0.4, 0.45), (1, 1.6, 0.3, 0.37, "in")),   # chỉ thấy tay thầy nhét bùa dưới gối
           [sfx("chant_murmur", 0, 0.4, True, 12)]))
    beat(P[39],
         V("bgL3d_coffin_top_full", [], cam((0, 1.2, 0.35, 0.42), (1, 1.8, 0.25, 0.38, "in")), [sfx("ritual_bell", 0.1, 0.5)]),
         V("bgL2_wake_coffin", [L("thay_tu/A5_stand_point_stern", 0.7)], cam((0, 1.3, 0.7, 0.55), (1, 1.5, 0.72, 0.52)),
           [WOOD(12, 0.25)]),
         V("bgL2_wake_coffin", [L("grandma/K4_nod_look_hands", 0.22), L("mother_alive/G2_stand_worried", 0.36, h=0.56),
                                L("boy_hoodie/B1_stand_worried", 0.52), L("thay_tu/A5_stand_point_stern", 0.8)],
           cam((0, 1.3, 0.25, 0.6), (1, 1.3, 0.75, 0.6, "smooth")), [WOOD(12, 0.25)]))
    a_thay_end = len(S)

    # ---- ba ngày tang lễ
    a_wake = beat(P[40],
                  V("bgL2_wake_coffin", [day(L("boy_hoodie/Q1_mourn_kneel_back", 0.5, 1.0, h=0.4))],
                    cam((0, 1.2, 0.5, 0.6), (1, 1.35, 0.52, 0.6)), [BAND(14, 0.25), WOOD(14, 0.3), sfx("mourners_cry", 0, 0.25, True, 14)],
                    bg_dim=0.15),
                  V("bgL2_wake_coffin", [day(L("co_ut/A1_hug_boy", 0.55, h=0.5))],
                    cam((0, 1.3, 0.55, 0.6), (1, 1.5, 0.55, 0.58)), [WOOD(12, 0.25)], bg_dim=0.15))
    beat(P[41],
         V("bgL14b_grandma_by_coffin", [], cam((0, 1.15, 0.5, 0.52), (1, 1.25, 0.58, 0.52)), [INSECTS(12, 0.3), CLOCK(12, 0.2)]),
         V("bgL14b_grandma_by_coffin", [], cam((0, 1.3, 0.66, 0.55), (1, 1.45, 0.68, 0.56, "smooth")), [INSECTS(12, 0.3)]))
    beat(P[42], V("bgL14b_grandma_by_coffin", [], cam((0, 1.15, 0.6, 0.55), (1, 1.3, 0.66, 0.5, "smooth")), [INSECTS(12, 0.3)]))
    beat(P[43], V("bgL2_wake_coffin", [L("cat_tabby/A2_arch_hiss", 0.88, h=0.13, face="left"), L("grandma/L1_comb_into_coffin", 0.2, h=0.46)],
                  cam((0, 1.3, 0.75, 0.65), (1, 1.6, 0.86, 0.75, "in")), [sfx("cat_hiss", 0.55, 1.0)]))
    beat(P[44], V("bgL2_wake_coffin", [L("grandma/K2_shoo_broom", 0.7, end=0.45), L("grandma/K3_lean_back_door_tremble", 0.86, start=0.45)],
                  cam((0, 1.3, 0.75, 0.6), (1, 1.4, 0.82, 0.6), handheld=3),
                  [sfx("door_slam", 0.42, 0.7), sfx("breath_close", 0.6, 0.4)]))
    a_vigil = beat(P[45], V("bgL2_wake_coffin", [L("grandma/M1_slump_asleep_table", 0.2, h=0.4), L("mother_alive/E5_sleep_armchair", 0.88, h=0.5),
                                                  L("boy_hoodie/N1_sit_hug_knees_drowsy", 0.62, h=0.36)],
                            cam((0, 1.08, 0.55, 0.55), (1, 1.15, 0.55, 0.55)), [CLOCK(12, 0.3), INSECTS(12, 0.25)]))
    beat(P[46], V("bgL2_wake_coffin", [], cam((0, 1.3, 0.5, 0.4), (1, 1.6, 0.48, 0.32, "smooth")),
                  [CLOCK(12, 0.3), sfx("dog_howl", 0.7, 0.3)]))
    beat(P[47], V("bgL2_wake_coffin", [L("boy_hoodie/N1_sit_hug_knees_drowsy", 0.62, h=0.36)],
                  cam((0, 1.4, 0.62, 0.65), (1, 1.6, 0.62, 0.68)), [CLOCK(12, 0.3)]))
    silent("bgL2_wake_coffin", 4.0, [L("boy_hoodie/N1_sit_hug_knees_drowsy", 0.62, h=0.36)],
           cam((0, 1.6, 0.62, 0.68), (1, 1.7, 0.6, 0.68)), [CLOCK(4, 0.35), sfx("dog_howl", 0.4, 0.2)], flicker=0.08)
    a_wind = beat(P[48], V("bgL2n_wake_candles_out", [L("boy_hoodie/N6_step_back_frozen", 0.62, h=0.4)],
                           cam((0, 1.3, 0.55, 0.6), (1, 1.3, 0.58, 0.6), handheld=5),
                           [sfx("wind_gust_candle", 0.0, 0.9), sfx("heartbeat", 0.3, 0.5, True, 8)], bg_dim=0.1))
    beat(P[49], V("bgL2n_wake_candles_out", [L("boy_hoodie/N2_kneel_strike_match", 0.55, h=0.38)],
                  cam((0, 1.5, 0.55, 0.7), (1, 1.7, 0.55, 0.72)), [sfx("match_strike", 0.35, 0.9)], bg_dim=0.1))
    beat(P[50], V("black", [L("props/LB1_talisman_folded", 0.5, 0.82, h=0.5, tint=False),
                            L("props/LE4_matchbox_lit_match", 0.2, 0.95, h=0.3, tint=False)],
                  cam((0, 1.0, 0.5, 0.5), (1, 1.2, 0.5, 0.5, "in")), [sfx("heartbeat", 0, 0.7, True, 6)]))
    beat(P[51],
         V("bgL2n_wake_candles_out", [L("boy_hoodie/N4_tiptoe_peer_down", 0.45, h=0.44)], cam((0, 1.4, 0.42, 0.6), (1, 1.6, 0.38, 0.55)),
           [sfx("heartbeat", 0, 0.6, True, 10)], bg_dim=0.1),
         V("bgL3e_coffin_top_full_dropped", [], cam((0, 1.15, 0.5, 0.5), (1, 1.7, 0.57, 0.62, "in"), handheld=3),
           [sfx("heartbeat", 0, 0.7, True, 10), sfx("reverse_swell", 0.5, 0.6)]))
    beat(P[52], V("bgL3e_coffin_top_full_dropped", [], cam((0, 1.6, 0.3, 0.45), (1, 2.3, 0.27, 0.43, "in")),
                  [sfx("match_strike", 0.0, 0.3), sfx("whisper_eerie", 0.6, 0.35)], flash=[0.82], fade_out=0.3))
    silent("bgL3c_coffin_face_smile", 1.2, camera=cam((0, 1.15, 0.5, 0.5), (1, 1.35, 0.5, 0.5, "in")), sounds=[sfx("ghost_stinger", 0, 1.4)],
           flash=[0.0], shake={"amp": 14, "from": 0, "to": 0.5}, fade_in=0)
    silent("black", 0.8, sounds=[sfx("heartbeat", 0, 0.6, True, 0.8)])
    beat(P[53], V("bgL2n_wake_candles_out", [L("boy_hoodie/N3_crouch_hold_talisman", 0.6, h=0.4, jitter=1)],
                  cam((0, 1.4, 0.6, 0.65), (1, 1.6, 0.6, 0.62)), [sfx("heartbeat", 0, 0.5, True, 10)], bg_dim=0.1))
    beat(P[54], V("bgL2n_wake_candles_out", [L("boy_hoodie/N5_stuff_pocket_guilty", 0.6, h=0.44)],
                  cam((0, 1.4, 0.6, 0.6), (1, 1.7, 0.6, 0.62, "in")), [sfx("breath_close", 0.4, 0.4)], bg_dim=0.1))
    a_dawn = beat(P[55], V("bgL2_wake_coffin", [L("boy_hoodie/N5_stuff_pocket_guilty", 0.78, h=0.46)],
                           cam((0, 1.8, 0.78, 0.7), (1, 2.0, 0.76, 0.68)), [sfx("rooster_crow", 0.1, 0.4)], bg_dim=0.2))
    beat(P[56], V("bgL2_wake_coffin", [L("thay_tu/A6_back_pray_incense", 0.49, h=0.56), L("boy_hoodie/N6_step_back_frozen", 0.17, 1.02, h=0.52)],
                  cam((0, 1.25, 0.38, 0.62), (1, 1.35, 0.42, 0.6, "smooth")), [sfx("chant_murmur", 0, 0.45, True, 12)], bg_dim=0.15))
    a_wake_end = len(S)

    # ---- đưa tang
    a_fun = beat(P[57],
                 V("bgL2_wake_coffin", [day(L("boy_hoodie/O1_mourn_hold_incense_bowl", 0.5, h=0.44))],
                   cam((0, 1.2, 0.5, 0.6), (1, 1.35, 0.5, 0.58)), [BAND(14, 0.5), sfx("mourners_cry", 0, 0.35, True, 14)], bg_dim=0.1),
                 V("bgL2_wake_coffin", [day(L("boy_hoodie/O1_mourn_hold_incense_bowl", 0.5, h=0.44))],
                   cam((0, 1.35, 0.5, 0.58), (1, 1.5, 0.5, 0.55)), [BAND(14, 0.5)], bg_dim=0.1))
    beat(P[58], V("bgL2c_wake_coffin_closed", [],
                  cam((0, 1.3, 0.35, 0.55), (1, 1.6, 0.3, 0.5, "in")),
                  [sfx("coffin_nails", 0.1, 1.0), sfx("coffin_nails", 0.55, 0.9), BAND(10, 0.2)]))
    beat(P[59], V("bgL2c_wake_coffin_closed", [day(L("boy_hoodie/O2_mourn_frozen_pocket", 0.6, h=0.46))],
                  cam((0, 1.4, 0.6, 0.55), (1, 1.8, 0.6, 0.45, "in")), [sfx("coffin_nails", 0.2, 0.6), sfx("heartbeat", 0, 0.4, True, 6)]))
    beat(P[60], V("bgL4_procession_field", [], cam((0, 1.25, 0.3, 0.5), (1, 1.25, 0.7, 0.5, "smooth")),
                  [BAND(14, 0.45), WIND(14, 0.5)]))
    a_crow = beat(P[61], V("bgL5_cemetery_burial_day", [day(L("props/LD1_crow_perched", 0.66, 0.35, h=0.09)),
                                                        day(L("boy_hoodie/O5_mourn_look_up", 0.42, h=0.44))],
                           cam((0, 1.2, 0.45, 0.6), (1, 1.7, 0.66, 0.33, "smooth")), [WIND(12, 0.4), sfx("crow_caw", 0.85, 0.5)]))
    beat(P[62], V("bgL5b_burial_shoveling", [],
                  cam((0, 1.3, 0.5, 0.6), (1, 1.6, 0.5, 0.66, "smooth")),
                  [sfx("shovel_dirt", 0.05, 0.8), sfx("shovel_dirt", 0.45, 0.7), WIND(12, 0.35)], fade_out=1.0))
    a_fun_end = len(S)

    # ---- đêm sau đám tang: bát cơm thứ hai
    a_after = beat(P[63], V("bgL11_ong_bed_corner_night", [], cam((0, 1.2, 0.4, 0.6), (1, 1.3, 0.55, 0.65, "smooth")),
                            [INSECTS(12, 0.3), CLOCK(12, 0.25)], fade_in=1.0))
    beat(P[64],
         V("bgL1n_porch_night", [L("mother_alive/E6_sit_hug_old_shirt", **PORCH_STOOL)], cam((0, 1.2, 0.38, 0.6), (1, 1.4, 0.36, 0.6)),
           [INSECTS(12, 0.35)]),
         V("bgL9_main_room_altar_ong", [L("grandma/K5_wipe_chopstick_holder", 0.62)], cam((0, 1.3, 0.65, 0.55), (1, 1.4, 0.66, 0.55)),
           [CLOCK(10, 0.3)]))
    beat(P[65], V("bgL9_main_room_altar_ong", [L("grandma/K6_raise_bowl_altar", 0.42, face="left")], cam((0, 1.3, 0.38, 0.5), (1, 1.5, 0.33, 0.4, "smooth")),
                  [sfx("ritual_bell", 0.5, 0.4), CLOCK(10, 0.25)]))
    beat(P[66], V("bgL15_khoa_bed_awake_night", [],
                  cam((0, 1.2, 0.65, 0.6), (1, 1.4, 0.68, 0.62)), [CLOCK(12, 0.4), INSECTS(12, 0.25)]))
    a_tap = beat(P[67], V("bgL15_khoa_bed_awake_night", [],
                          cam((0, 1.3, 0.5, 0.55), (1, 1.7, 0.5, 0.5, "in")), [CLOCK(8, 0.5)]))
    beat(P[68], V("bgL9_main_room_altar_ong", [], cam((0, 1.6, 0.35, 0.4), (1, 1.9, 0.38, 0.35)),
                  [sfx("chopsticks_tap_2", 0.05, 1.0), sfx("chopsticks_tap_2", 0.45, 1.0), CLOCK(8, 0.2)], bg_dim=0.3))
    beat(P[69], V("bg2_hallway", [walk("boy_hoodie", [0.15, 0.6], fps=2.2, end=0.9, cyc="tiptoe"),
                                  L("boy_hoodie/K3_pull_back_fear", 0.6, start=0.9)],
                  cam((0, 1.2, 0.3, 0.6), (1, 1.2, 0.6, 0.6, "smooth")), [sfx("heartbeat", 0, 0.5, True, 10), sfx("floor_creak", 0.5, 0.5)]))
    BOWLS2 = [L("props/LF1_bowl_chopsticks_upright", 0.42, 0.8, h=0.34),
              L("props/LF1_bowl_chopsticks_upright", 0.6, 0.8, h=0.34)]
    a_bowl2 = beat(P[70], V("bg5c_altar_grandpa_cold", BOWLS2, cam((0, 1.2, 0.5, 0.55), (1, 2.0, 0.6, 0.68, "in")),
                            [sfx("reverse_swell", 0.4, 0.6), CLOCK(10, 0.3)]))
    silent("bg5c_altar_grandpa_cold", 3.0, BOWLS2, cam((0, 2.0, 0.6, 0.68), (1, 2.3, 0.6, 0.7)), [sfx("heartbeat", 0, 0.6, True, 3)])
    beat(P[71], V("bg7_front_yard", [walk("props", [0.8, 0.58], fps=6, cyc="crow_fly", y=0.2, h=0.03, start=0.2, end=0.75, clip_rect=GATE_GAP)],
                  cam((0, 1.3, 0.5, 0.4), (1, 1.6, 0.5, 0.36, "in")), [sfx("crow_caw", 0.35, 1.0), INSECTS(8, 0.2)]))
    silent("black", 3.0, title_text="Còn tiếp", fade_in=1.0, fade_out=1.0,
           sounds=[sfx("chopsticks_tap_2", 0.8, 0.6)])
    return dict(
        title="Lá bùa dưới gối ông — Phần 1: Giờ Dần",
        requests=ASSET_REQUESTS,
        output="build/la_bua_duoi_goi_ong_p1.mp4",
        logline=("Ông mất vào giờ Dần ngày Dần, thầy cúng đặt lá bùa trấn trùng dưới gối ông. Đêm canh linh cữu, "
                 "Khoa nhặt được lá bùa rơi dưới chân quan tài và giấu nó đi — rồi trên bàn thờ xuất hiện bát cơm thứ hai."),
        music=[
        {"sound": "drone_low", "from": 1, "to": a_open_end, "volume": 0.6, "fade_in": 2.5, "fade_out": 1.5},
        {"sound": "memory_piano", "from": a_home, "to": a_home_end, "volume": 0.45, "fade_in": 2.5, "fade_out": 2.5},
        {"sound": "drone_low", "from": a_sick, "to": a_death_end, "volume": 0.5, "fade_in": 3, "fade_out": 2},
        {"sound": "drone_low", "from": a_thay + 1, "to": a_thay_end, "volume": 0.55, "fade_in": 2.5, "fade_out": 1.5},
        {"sound": "drone_low", "from": a_vigil, "to": a_wake_end, "volume": 0.65, "fade_in": 2.5, "fade_out": 0.05},
        {"sound": "drone_low", "from": a_crow, "to": a_fun_end, "volume": 0.5, "fade_in": 2, "fade_out": 2},
        {"sound": "drone_low", "from": a_tap, "to": len(S) - 1, "volume": 0.65, "fade_in": 2, "fade_out": 0.05},
    ],
    )


# ============================================================ PHẦN 2 — BÁT CƠM THỨ HAI
# chỗ đặt trên phông mới của Phần 2 (đo trên ảnh đã nạp)
MOM_BED_POS = dict(x=0.6, y=0.97, h=0.42)       # bgL7/bgL7n: giường mẹ giữa-phải (sprite có giường, đầu giường bên trái)
MACHINE = dict(x=0.3, y=0.9, h=0.45)            # bgL7/bgL7n: chỗ máy khâu dưới vệt sáng cửa sổ
ALTAR_MOM = dict(x=0.42, y=0.95, h=0.6)         # bgL9: mẹ đứng trước kệ thờ (kệ ở x 0.17–0.43)
SHELF_BOWL = dict(y=0.375, h=0.085)             # bgL9: bát cơm trên kệ thờ (ông x 0.29, mẹ x 0.34)
GRAVE_KNEEL = dict(x=0.56, y=0.78, h=0.28)      # bgL17: quỳ trước đầu mộ ông (bia ở x 0.53, mộ 0.48–0.74)
BEHIND_STONE = dict(x=0.475, y=0.56, h=0.2)     # bgL17: sát sau bia mộ, bên trái
KAPOK = dict(x=0.7, y=0.27, h=0.075)            # bgL17: cành ngang cây gạo
KAPOK_DAY = dict(x=0.68, y=0.215, h=0.075)      # bgL17b: cành cây gạo
SHELF_BOWL_D = dict(y=0.375, h=0.085)             # bgL9d: bát cơm trên kệ thờ (ông x 0.29, bát thứ hai x 0.34)
ALTAR_BOWL = dict(y=0.76, h=0.3)                # bgL24 (cận bàn thờ ông + bố): trước ảnh ông x 0.47, trước ảnh bố x 0.64
HALL_DOOR = dict(y=0.78, h=0.36)                # bg2: đứng sát cửa phòng bà (cửa phải x 0.63–0.78, chân cửa y 0.72)


def part2():
    P = paragraphs("## Phần 2", "## Phần 3")
    # góp ý preview 1 (#38): thêm lời thầy Tư giải thích vì sao trùng lần theo đũa và vì sao không huỷ đũa được
    WHY_NAME = P.pop(30)     # "Tôi chợt nhớ đến cái hôm tôi hỏi ông…" (sau đoạn "gọi là đổi đũa")
    NO_BURN = P.pop(31)      # "Bà hỏi hay là đem đốt hết số đũa ấy đi…" (sau đoạn cách đổi đũa)
    assert WHY_NAME.startswith("Tôi chợt nhớ") and NO_BURN.startswith("Bà hỏi hay là đem đốt")
    assert len(P) == 82, f"md Phần 2 đổi số đoạn ({len(P)}) — rà lại chỉ số đoạn bên dưới"
    BOWLS2 = [L("props/LF1_bowl_chopsticks_upright", 0.42, 0.8, h=0.34),
              L("props/LF1_bowl_chopsticks_upright", 0.6, 0.8, h=0.34)]
    ONG_BOWL_D = day(L("props/LF1_bowl_chopsticks_upright", 0.29, **SHELF_BOWL_D))          # bgL9d: bát của ông
    TWO_BOWLS_D = [ONG_BOWL_D, day(L("props/LF1_bowl_chopsticks_upright", 0.34, **SHELF_BOWL_D))]
    MAT = [day(L("grandma/M2_kneel_mat_worried", 0.32, h=0.38)), day(L("mother_alive/G3_kneel_mat_worried", 0.2, h=0.42)),
           day(L("boy_hoodie/Q3_kneel_mat_worried", 0.8, h=0.34, face="left"))]
    THAY_TALK = day(L("thay_tu/C3_sit_mat_explain", 0.56, h=0.35))

    # ---- mở đầu phần 2
    silent("black", 4.0, title_text="LÁ BÙA DƯỚI GỐI ÔNG", fade_in=0.8, fade_out=0.8,
           sounds=[sfx("chopsticks_tap_2", 0.6, 0.8), sfx("crow_caw", 2.4, 0.5)])
    silent("black", 3.0, title_text="Phần 2 — Bát cơm thứ hai", fade_in=0.5, fade_out=0.8, sounds=[CLOCK(3, 0.4)])
    a_open_end = len(S)

    # ---- sáng hôm sau: bà thấy bát cơm thứ hai
    a_morning = beat(P[0], V("bgL9d_main_room_altar_ong_day", TWO_BOWLS_D + [day(L("grandma/N1_back_stare_altar", 0.36))],
                             cam((0, 1.2, 0.45, 0.6), (1, 1.45, 0.34, 0.5, "smooth")), [CLOCK(12, 0.25)], fade_in=1.0))
    beat(P[1], V("bgL9d_main_room_altar_ong_day", [day(L("grandma/N2_closeup_face_fear", 0.5, 1.08, h=1.0))],
                 cam((0, 1.0, 0.5, 0.5), (1, 1.12, 0.5, 0.5, "smooth")), [sfx("heartbeat", 0, 0.3, True, 10)], bg_dim=0.3))
    beat(P[2], V("bgL22_backyard_morning", [day(L("grandma/N3_feed_chickens", 0.4, h=0.48))],
                 cam((0, 1.2, 0.4, 0.6), (1, 1.35, 0.4, 0.62)), [sfx("chickens_cluck", 0, 0.5, True, 12)]))
    beat(P[3], V("bgL9d_main_room_altar_ong_day", [ONG_BOWL_D, day(L("grandma/E1_hold_boy_hands", 0.45, h=0.5))],
                 cam((0, 1.25, 0.42, 0.6), (1, 1.5, 0.4, 0.55, "smooth")), [CLOCK(10, 0.2)]))
    beat(P[4], V("bgL9d_main_room_altar_ong_day", [ONG_BOWL_D, day(L("boy_hoodie/B1_stand_worried", 0.45, face="right")),
                                                   day(L("grandma/00_stand_front", 0.62, end=0.5)),
                                                   day(walk("grandma", [0.62, 1.1], fps=2.5, start=0.5))],
                 cam((0, 1.25, 0.52, 0.6), (1, 1.4, 0.5, 0.58)), [CLOCK(10, 0.2), sfx("slipper_drag", 3.0, 0.3, True, 6)]))

    # ---- con quạ, con mèo
    a_crow = beat(P[5], V("bgL8_house_alley_dusk",
                          [walk("props", [0.25, 0.53], fps=6, cyc="crow_fly", y=0.2, h=0.035, end=0.45),
                           L("props/LD2_crow_caw", 0.53, 0.235, h=0.035, start=0.45)],
                          cam((0, 1.25, 0.45, 0.45), (1, 1.6, 0.53, 0.32, "smooth")),
                          [sfx("wings_flap", 0.3, 0.5), sfx("crow_caw", 0.55, 0.8), sfx("crow_caw", 0.85, 0.6)], fade_in=0.8))
    beat(P[6], V("bgL23_house_roof_dusk", [L("grandma/N4_pole_shoo_crow", 0.45, 0.92, face="right"),
                                           walk("props", [0.95, 0.6], fps=6, cyc="crow_fly", y=0.12, h=0.05, end=0.55),
                                           L("props/LD3_crow_look_down", 0.525, 0.08, h=0.06, start=0.55)],
                 cam((0, 1.15, 0.48, 0.52), (1, 1.18, 0.52, 0.5, "smooth")),
                 [sfx("wings_flap", 0.1, 0.8), sfx("crow_caw", 0.3, 0.6)]))
    beat(P[7], V("bgL1_porch_day", [day(L("mother_alive/G2_stand_worried", 0.18, h=0.56)),
                                    day(L("cat_tabby/A2_arch_hiss", 0.72, h=0.13, face="left", end=0.72)),
                                    day(walk("cat_tabby", [0.72, 1.1], fps=8, cyc="run", start=0.72))],
                 cam((0, 1.2, 0.45, 0.6), (1, 1.3, 0.6, 0.62, "smooth")), [sfx("cat_hiss", 0.62, 1.0)]))

    # ---- bát cơm nóng hổi, dép mẹ, hạt cơm dưới móng tay
    a_bowl = beat(P[8], V("bgL24_altar_ong_bo_cold", [L("props/LF1_bowl_chopsticks_upright", 0.47, **ALTAR_BOWL),
                                                    L("props/LF2_bowl_upright_steaming", 0.64, **ALTAR_BOWL)],
                          cam((0, 1.2, 0.5, 0.55), (1, 1.7, 0.6, 0.66, "in")), [sfx("reverse_swell", 0.4, 0.5), CLOCK(10, 0.3)]))
    beat(P[9], V("bg6_kitchen", [], cam((0, 1.3, 0.45, 0.5), (1, 1.7, 0.31, 0.45, "smooth")), [CLOCK(8, 0.2), INSECTS(8, 0.15)],
                 bg_dim=0.2))
    beat(P[10],
         V("black", [L("props/DC6_mother_slippers", 0.5, 0.85, h=0.4, tint=False, end=0.55),
                     L("props/LH5_rice_under_nails", 0.5, 0.95, h=0.75, tint=False, start=0.55)],
           cam((0, 1.0, 0.5, 0.5), (1, 1.2, 0.5, 0.5)), [sfx("heartbeat", 0.5, 0.4, True, 6)]),
         V("bgL9d_main_room_altar_ong_day", TWO_BOWLS_D + [day(L("mother_alive/G2_stand_worried", 0.45, h=0.58))],
           cam((0, 1.3, 0.45, 0.55), (1, 1.45, 0.45, 0.5))))
    beat(P[11], V("bgL9s_grandma_asleep_table", [],
                  cam((0, 1.2, 0.42, 0.55), (1, 1.35, 0.55, 0.6, "smooth")), [CLOCK(12, 0.35), sfx("clock_chime_3", 0.5, 0.5)]))
    # #16: sáng ra — cận bàn thờ (ảnh ông + bố), một bát (bát của mẹ bà đã đổ đi), rồi bát thứ hai hiện lại
    silent("bgL24_altar_ong_bo_cold", 3.0, [L("props/LF1_bowl_chopsticks_upright", 0.47, **ALTAR_BOWL),
                                           L("props/LF1_bowl_chopsticks_upright", 0.64, **ALTAR_BOWL, start=0.55)],
           cam((0, 1.2, 0.5, 0.6), (1, 1.4, 0.52, 0.64)), [sfx("chopsticks_tap_2", 0.5, 0.6), CLOCK(3, 0.3)])
    a_bowl_end = len(S)

    # ---- mẹ yếu đi, bát cơm đầu giường, giấc mơ, đan áo len
    a_weak = beat(P[12], V("bgL25_mom_bed_sick_night", [],
                           cam((0, 1.2, 0.6, 0.6), (1, 1.4, 0.64, 0.62)), [INSECTS(12, 0.25), CLOCK(12, 0.2)], fade_in=0.8))
    # bát vẽ sẵn trong bgL25b quá to → phông mẹ ngủ + sprite bát nhỏ sát gối, đũa gác ngang chĩa về phía mẹ
    beat(P[13], V("bgL25_mom_bed_sick_night", [L("props/LC1_bowl_full_chopsticks_across", 0.62, 0.585, h=0.05)],
                  cam((0, 1.2, 0.58, 0.55), (1, 1.7, 0.63, 0.55, "in")), [sfx("reverse_swell", 0.5, 0.5), CLOCK(10, 0.25)]))
    beat(P[14],
         V("bgL25c_mom_bed_sit_bowl_morning", [], cam((0, 1.2, 0.6, 0.55), (1, 1.6, 0.66, 0.55, "smooth"))),
         V("bgL25_mom_bed_sick_night", [L("ong_noi/E1_ghost_tap_bowl", 0.92, 0.95, h=0.42, glow=True)],   # đứng sát chân giường (bên phải)
           cam((0, 1.2, 0.75, 0.6), (1, 1.45, 0.85, 0.5, "smooth")),
           [sfx("chopsticks_tap_2", 0.6, 1.0), sfx("whisper_eerie", 0.2, 0.15)], bg_dim=0.3, flicker=0.06))
    beat(P[15], V("bgL25n_mom_bedroom_night", [L("mother_alive/H3_sit_knit_lamp", 0.3, h=0.46)],
                  cam((0, 1.2, 0.35, 0.6), (1, 1.4, 0.3, 0.6, "smooth")), [sfx("knitting_needles", 0, 0.5, True, 12)]))
    beat(P[16], V("bgL25n_mom_bedroom_night", [L("mother_alive/H3_sit_knit_lamp", 0.3, h=0.46)],
                  cam((0, 1.4, 0.3, 0.6), (1, 1.7, 0.3, 0.55, "smooth")),
                  [sfx("knitting_needles", 0, 0.5, True, 10), sfx("breath_close", 0.5, 0.25)]))

    # ---- buổi sáng đi chợ (hồi ức ấm)
    a_market = beat(P[17], V("bgL25e_mom_bedroom_day", [day(L("mother_alive/I1_floral_comb_hair", 0.3, h=0.56))],
                             cam((0, 1.2, 0.35, 0.6), (1, 1.35, 0.3, 0.55, "smooth")), [sfx("rooster_crow", 0.2, 0.25)], fade_in=1.0))
    beat(P[18], V("bgL16b_market_side_step", [day(L("mother_alive/I2_market_step_xoi_boy", 0.2, 0.85, h=0.4))],
                  cam((0, 1.2, 0.35, 0.6), (1, 1.35, 0.28, 0.62)), [sfx("market_morning", 0, 0.4, True, 14)]))
    beat(P[19], V("bgL16b_market_side_step", [day(L("mother_alive/I2_market_step_xoi_boy", 0.2, 0.85, h=0.4))],
                  cam((0, 1.35, 0.28, 0.62), (1, 1.6, 0.26, 0.62, "smooth")), [sfx("market_morning", 0, 0.3, True, 14)]))
    beat(P[20],
         V("bgL16b_market_side_step", [day(L("mother_alive/I3_hold_boy_hand", 0.3, 1.06, h=0.6))],
           cam((0, 1.2, 0.35, 0.6), (1, 1.4, 0.3, 0.62)), [sfx("market_morning", 0, 0.3, True, 12)]),
         V("bgL16b_market_side_step", [day(L("mother_alive/I3_hold_boy_hand", 0.3, 1.06, h=0.6))],
           cam((0, 1.4, 0.3, 0.62), (1, 1.9, 0.3, 0.68, "smooth")), [sfx("market_morning", 0, 0.2, True, 10)], fade_out=1.0))
    a_market_end = len(S)

    # ---- máy khâu lúc 3 giờ, bộ áo xô
    a_sew = beat(P[21], V("bgL15b_khoa_bed_awake_plain", [],
                          cam((0, 1.2, 0.6, 0.6), (1, 1.4, 0.62, 0.6, "in")),
                          [sfx("sewing_machine", 0, 0.5, True, 12), sfx("clock_chime_3", 0.6, 0.8)], fade_in=0.5))
    silent("bgL7n_mom_room_night", 3.0, [L("mother_alive/E2_sit_sewing_machine", **MACHINE)],
           cam((0, 1.3, 0.4, 0.62), (1, 1.5, 0.4, 0.6)), [sfx("sewing_machine", 0, 0.6, True, 3)], bg_dim=0.4)
    beat(P[22], V("black", [L("props/LH4_fingertips_needle_marks", 0.5, 0.95, h=0.75, tint=False, end=0.55),
                            L("props/LH1_sweater_unfinished", 0.5, 0.85, h=0.5, start=0.55)],
                  cam((0, 1.0, 0.5, 0.5), (1, 1.15, 0.5, 0.5)), [sfx("heartbeat", 0, 0.3, True, 10)]))
    beat(P[23],
         V("bgL26_mom_sewing_tunic", [],
           cam((0, 1.15, 0.5, 0.55), (1, 1.4, 0.5, 0.5, "smooth")), [sfx("woman_sob_door", 0.4, 0.4)]))
    a_sew_end = len(S)

    # ---- thầy Tư làm lễ, cách đổi đũa
    a_thay = beat(P[24], V("bgL1_porch_day", [day(L("thay_tu/C1_scatter_rice_salt", 0.5, end=0.5)),
                                              day(L("thay_tu/C2_hang_bagua_mirror", 0.2, 0.97, h=0.8, start=0.5))],
                           cam((0, 1.2, 0.45, 0.6), (1, 1.3, 0.38, 0.45, "smooth")),
                           [sfx("rice_scatter", 0.1, 0.7), sfx("paper_burn", 0, 0.3, True, 10), sfx("ritual_bell", 0.6, 0.4)]))
    beat(P[25],
         V("bgL9d_main_room_altar_ong_day", [ONG_BOWL_D, day(L("thay_tu/A6_back_pray_incense", 0.4, h=0.56))],
           cam((0, 1.2, 0.4, 0.55), (1, 1.45, 0.33, 0.45, "smooth")), [sfx("chant_murmur", 0, 0.3, True, 10)]),
         V("bgL3d_coffin_top_full", [L("mother_alive/G4_topdown_back_lean", 0.46, 0.34, h=0.5)],
           cam((0, 1.1, 0.45, 0.45), (1, 1.5, 0.44, 0.45, "smooth")), [sfx("water_drip", 0.6, 0.6)], bg_dim=0.2))
    beat(P[26], V("bgL9d_main_room_altar_ong_day", [ONG_BOWL_D, day(L("thay_tu/A5_stand_point_stern", 0.55))],
                  cam((0, 1.3, 0.55, 0.55), (1, 1.8, 0.55, 0.45, "in")), [sfx("reverse_swell", 0.4, 0.5)]))
    beat(P[27], V("bgL27_khoa_peek_door_day", [],
                  cam((0, 1.15, 0.5, 0.5), (1, 1.4, 0.55, 0.48, "in")), [sfx("heartbeat", 0, 0.6, True, 10)]))
    beat(P[28], V("bgL12_living_room_day", [day(L("thay_tu/C3_sit_mat_explain", 0.56, h=0.35))] + MAT,
                  cam((0, 1.2, 0.5, 0.62), (1, 1.3, 0.45, 0.62, "smooth")), [sfx("chant_murmur", 0, 0.15, True, 12)]))
    beat(P[29], V("bgL12_living_room_day", [THAY_TALK] + MAT, cam((0, 1.4, 0.56, 0.62), (1, 1.7, 0.56, 0.6, "in"))))
    DINNER_P1 = [day(L("ong_noi/C2_sit_stool_eat_side", 0.86, 0.8, h=0.42, face="left")),
                 day(L("boy_hoodie/O4_sit_stool_eat_chat", **STOOL_L))]   # bữa cơm Phần 1 (hồi ức)
    # lý do ông khắc đũa (giữ người) để dành cho Phần 3 — ở đây thầy chỉ nói vì sao trùng lần theo cái tên
    beat(WHY_NAME,
         V("bg4e_main_room_day_bo", DINNER_P1, cam((0, 1.3, 0.72, 0.6), (1, 1.45, 0.76, 0.58, "smooth")),
           [sfx("chopsticks_tap_2", 0.4, 0.6)], fade_in=0.6),
         V("bgL12_living_room_day", [THAY_TALK] + MAT, cam((0, 1.5, 0.56, 0.6), (1, 1.75, 0.56, 0.58, "smooth"))))
    beat(P[30],
         V("bgL12_living_room_day", [THAY_TALK] + MAT, cam((0, 1.6, 0.56, 0.6), (1, 1.7, 0.56, 0.6))),
         V("black", [L("props/LB1_talisman_folded", 0.5, 0.75, h=0.4, tint=False)],
           cam((0, 1.0, 0.5, 0.5), (1, 1.2, 0.5, 0.5)), [WIND(12, 0.25), sfx("rooster_crow", 0.85, 0.2)]),
         V("black", [L("props/LJ1_chopsticks_plain", 0.42, 0.72, h=0.5, tint=False),
                     L("props/LJ1_chopsticks_plain", 0.58, 0.7, h=0.5, tint=False, start=0.5)],
           cam((0, 1.0, 0.5, 0.5), (1, 1.2, 0.5, 0.5)), [WIND(12, 0.25), sfx("chopsticks_tap_2", 0.5, 0.5)]))
    beat(NO_BURN,
         V("bgL12_living_room_day", [THAY_TALK] + MAT, cam((0, 1.5, 0.35, 0.64), (1, 1.6, 0.35, 0.62))),
         V("black", [L("props/LK1_chopsticks_burning", 0.5, 0.7, h=0.45, tint=False, end=0.5),
                     L("props/LB5_chopstick_broken", 0.55, 0.72, h=0.4, tint=False, start=0.5)],
           cam((0, 1.0, 0.5, 0.5), (1, 1.15, 0.5, 0.5)), [sfx("paper_burn", 0, 0.4, True, 8, 0, 1.0)]),
         V("bgL12_living_room_day", [day(L("thay_tu/C4_sit_mat_shake_head", 0.56, h=0.35))] + MAT,
           cam((0, 1.5, 0.56, 0.6), (1, 1.7, 0.56, 0.58, "in"))))
    THREE = [L("props/LF1_bowl_chopsticks_upright", x, 0.72, h=0.24, start=st, tint=False)
             for x, st in ((0.3, 0.15), (0.5, 0.45), (0.7, 0.75))]
    beat(P[31],
         V("bgL12_living_room_day", [THAY_TALK] + MAT, cam((0, 1.7, 0.56, 0.6), (1, 1.8, 0.56, 0.58))),
         V("black", THREE, None, [sfx("chopsticks_tap_2", 0.15, 0.4), sfx("chopsticks_tap_2", 0.45, 0.5),
                                  sfx("chopsticks_tap_2", 0.75, 0.6)]),
         V("bgL9_main_room_altar_ong", [L("props/LB6_chopstick_holder", 0.7, 0.585, h=0.1)],
           cam((0, 1.3, 0.7, 0.55), (1, 2.0, 0.7, 0.55, "smooth")), [CLOCK(12, 0.25)]),
         V("bgL12_living_room_day", [THAY_TALK] + MAT, cam((0, 1.2, 0.3, 0.62), (1, 1.2, 0.7, 0.62, "smooth"))),
         V("bg5b_altar_grandpa_lit", [], cam((0, 1.15, 0.5, 0.5), (1, 1.4, 0.5, 0.42, "smooth")), [WOOD(12, 0.25)]),
         V("bgL24_altar_ong_bo_cold", [L("props/LF1_bowl_chopsticks_upright", 0.47, **ALTAR_BOWL),
                                       L("props/LF1_bowl_chopsticks_upright", 0.64, **ALTAR_BOWL)],
           cam((0, 1.2, 0.5, 0.6), (1, 1.6, 0.58, 0.66, "in")), [sfx("reverse_swell", 0.5, 0.5), CLOCK(12, 0.25)]))
    beat(P[32],
         V("bgL12_living_room_day", [day(L("thay_tu/C4_sit_mat_shake_head", 0.56, h=0.35))] + MAT,
           cam((0, 1.4, 0.56, 0.62), (1, 1.5, 0.56, 0.6))),
         V("bgL12_living_room_day", [day(L("thay_tu/C4_sit_mat_shake_head", 0.56, h=0.35))] + MAT,
           cam((0, 1.5, 0.32, 0.66), (1, 1.9, 0.32, 0.68, "smooth")), [CLOCK(8, 0.2)], fade_out=0.8))
    a_thay_end = len(S)

    # ---- Khoa hiểu ra, đếm ngày, cô Út, lời hứa của bà, đôi đũa dư
    a_count = beat(P[33], V("bgL15b_khoa_bed_awake_plain", [],
                            cam((0, 1.2, 0.55, 0.6), (1, 1.5, 0.62, 0.55, "in")), [CLOCK(12, 0.4), INSECTS(12, 0.2)], fade_in=0.8))
    beat(P[34],
         V("bgL28_khoa_calendar_night", [], cam((0, 1.15, 0.5, 0.55), (1, 1.4, 0.58, 0.45, "smooth")), [CLOCK(12, 0.35)]))
    beat(P[35],
         V("black", [L("props/LH3_calendar_circled", 0.5, 0.95, h=0.85, tint=False)],
           cam((0, 1.0, 0.5, 0.5), (1, 1.25, 0.5, 0.5, "smooth")), [CLOCK(10, 0.4)]),
         V("bgL25_mom_bed_sick_night", [], cam((0, 1.2, 0.5, 0.55), (1, 1.5, 0.42, 0.5, "smooth")),
           [sfx("whisper_eerie", 0.4, 0.15), CLOCK(8, 0.25)]))
    beat(P[36], V("bgL9d_main_room_altar_ong_day", [day(L("boy_hoodie/F4_phone_call_scared", 0.62, end=0.5, face="left")),
                                                    day(L("boy_hoodie/B1_stand_worried", 0.75, start=0.5, face="left")),
                                                    day(L("grandma/N6_phone_forced_smile", 0.55, start=0.5))],
                  cam((0, 1.3, 0.62, 0.58), (1, 1.4, 0.64, 0.58)), [sfx("phone_ring", 0, 0.4, False, 2.0, 0, 0.5)]))
    beat(P[37], V("bg2_hallway", [walk("boy_hoodie", [0.3, 0.64], fps=2.2, end=0.55, cyc="tiptoe", **HALL_DOOR),
                                  L("boy_hoodie/T2_raise_hand_knock_talisman", 0.64, start=0.55, **HALL_DOOR)],
                  cam((0, 1.2, 0.45, 0.6), (1, 1.4, 0.66, 0.5, "smooth")),
                  [sfx("heartbeat", 0, 0.4, True, 12), sfx("woman_sob_door", 0.7, 0.2)]))
    beat(P[38],
         V("bgL29_grandma_room_portrait", [], cam((0, 1.15, 0.5, 0.55), (1, 1.35, 0.52, 0.52)),
           [sfx("woman_sob_door", 0, 0.3), CLOCK(10, 0.2)]),
         V("bgL29_grandma_room_portrait", [], cam((0, 1.4, 0.52, 0.5), (1, 1.8, 0.52, 0.45, "smooth")),
           [sfx("woman_sob_door", 0.2, 0.45)]))
    beat(P[39], V("bg2_hallway", [L("boy_hoodie/T2_raise_hand_knock_talisman", 0.64, end=0.45, **HALL_DOOR),
                                  walk("boy_hoodie", [0.64, 0.25], fps=2.0, start=0.45, **HALL_DOOR)],
                  cam((0, 1.4, 0.66, 0.5), (1, 1.3, 0.45, 0.58, "smooth")), [sfx("woman_sob_door", 0, 0.3)], fade_out=0.8))
    beat(P[40],
         V("bg1_bedroom", [L("boy_hoodie/R1_floor_box_spare_chopsticks", 0.58, 0.86, h=0.34)],
           cam((0, 1.2, 0.6, 0.62), (1, 1.45, 0.6, 0.66)), [INSECTS(10, 0.2)], fade_in=0.6),
         V("black", [L("props/LJ2_chopsticks_spare_top_carved", 0.5, 0.7, h=0.52, tint=False)],
           cam((0, 1.0, 0.5, 0.5), (1, 1.3, 0.5, 0.5, "smooth")), [sfx("bamboo_whittle", 0, 0.15, True, 6)]))
    beat(P[41], V("black", [L("props/LJ4_box_open_spare", 0.5, 0.72, h=0.6, tint=False, end=0.6),
                            L("props/LJ3_box_closed_rubberband", 0.5, 0.72, h=0.6, tint=False, start=0.6)],
                  cam((0, 1.0, 0.5, 0.5), (1, 1.1, 0.5, 0.5))))
    a_count_end = len(S)

    # ---- bên giường mẹ (lời xin lỗi không nói ra)
    BEDSIDE = []   # góp ý preview #2: phông vẽ sẵn mẹ xoa đầu Khoa trong phòng mẹ (bgL25h)
    a_bedside = beat(P[42], V("bgL25h_mom_stroke_khoa_night", BEDSIDE, cam((0, 1.2, 0.6, 0.58), (1, 1.45, 0.64, 0.58)),
                              [CLOCK(12, 0.2)], fade_in=0.8))
    beat(P[43], V("bgL25h_mom_stroke_khoa_night", BEDSIDE, cam((0, 1.45, 0.64, 0.58), (1, 1.8, 0.63, 0.58, "smooth")),
                  [sfx("water_drip", 0.3, 0.4)]))
    beat(P[44], V("bgL25h_mom_stroke_khoa_night", BEDSIDE, cam((0, 1.7, 0.68, 0.55), (1, 1.85, 0.69, 0.55))))
    beat(P[45], V("bgL25h_mom_stroke_khoa_night", BEDSIDE, cam((0, 1.6, 0.66, 0.56), (1, 1.2, 0.6, 0.58, "smooth")),
                  [CLOCK(12, 0.3)], fade_out=1.5))
    a_bedside_end = len(S)

    # ---- đêm 48: ra nghĩa địa
    a_48 = beat(P[46], V("bgL15b_khoa_bed_awake_plain", [], cam((0, 1.3, 0.6, 0.55), (1, 1.5, 0.62, 0.55)),
                         [CLOCK(8, 0.4)], fade_in=0.8))
    beat(P[47], V("bgL9_main_room_altar_ong", [L("props/LB6_chopstick_holder", 0.7, 0.585, h=0.1),
                                               walk("boy_hoodie", [0.3, 0.6], fps=2.2, end=0.5, cyc="tiptoe"),
                                               L("boy_hoodie/A4_walk_reach_out", 0.6, start=0.5)],
                  cam((0, 1.2, 0.45, 0.6), (1, 1.35, 0.62, 0.58, "smooth")),
                  [sfx("heartbeat", 0, 0.35, True, 12), sfx("floor_creak", 0.3, 0.4)]))
    silent("bg7_front_yard", 3.0, [walk("boy_hoodie", [0.35, 0.69], fps=2.5, cyc="flashlight_walk", h=0.42)],
           cam((0, 1.2, 0.5, 0.6), (1, 1.3, 0.65, 0.55, "smooth")), [sfx("gate_rattle", 1.6, 0.4), INSECTS(3, 0.3)])
    beat(P[48], V("black", [L("props/LB3_chopsticks_named", 0.38, 0.8, h=0.4, tint=False),
                            L("props/LF3_chopsticks_khoa", 0.62, 0.8, h=0.4, tint=False),
                            L("props/LB1_talisman_folded", 0.5, 0.95, h=0.25, tint=False, start=0.5)],
                  cam((0, 1.0, 0.5, 0.5), (1, 1.2, 0.5, 0.5)), [sfx("heartbeat", 0, 0.4, True, 10)]))
    beat(P[49], V("bgL18_field_path_night", [walk("boy_hoodie", [-0.05, 0.75], fps=2.5, cyc="flashlight_walk", h=0.3, y=0.78)],
                  cam((0, 1.2, 0.3, 0.55), (1, 1.2, 0.7, 0.55, "smooth")),
                  [sfx("frogs_night", 0, 0.5, False, 7, 0, 1.5), WIND(14, 0.45)]))
    beat(P[50], V("bgL30_khoa_dig_grave_night", [],
                  cam((0, 1.15, 0.5, 0.55), (1, 1.45, 0.52, 0.6, "smooth")),
                  [sfx("soil_dig_hands", 0.3, 0.6, True, 6), WIND(12, 0.35)]))
    silent("bgL17_cemetery_night_grave", 5.0, [L("boy_hoodie/T4_kneel_hold_chopsticks", **GRAVE_KNEEL, jitter=1)],
           cam((0, 1.5, 0.58, 0.65), (1, 1.75, 0.6, 0.66)), [WIND(5, 0.5), sfx("heartbeat", 0, 0.4, True, 5)])
    a_ghost = beat(P[51],
                   V("bgL17_cemetery_night_grave", [L("props/LD2_crow_caw", **KAPOK),
                                                    L("boy_hoodie/T4_kneel_hold_chopsticks", **GRAVE_KNEEL, jitter=1)],
                     cam((0, 1.4, 0.7, 0.4), (1, 1.6, 0.8, 0.32, "smooth")), [sfx("crow_caw", 0.2, 1.0), WIND(10, 0.3)]),
                   V("bgL17_cemetery_night_grave", [L("ong_noi/B6_ghost_stand_still", **BEHIND_STONE, start=0.35),
                                                    L("boy_hoodie/L2_flashlight_point_far", 0.65, h=0.4, face="left")],
                     cam((0, 1.3, 0.55, 0.6), (1, 1.9, 0.4, 0.58, "in"), handheld=4),
                     [sfx("flashlight_click", 0.1, 0.6), sfx("reverse_swell", 0.1, 0.5), sfx("ghost_stinger", 0.35, 1.0)],
                     flicker=0.1))
    beat(P[52], V("bgL17_cemetery_night_grave", [L("boy_hoodie/T4_kneel_hold_chopsticks", **{**GRAVE_KNEEL, "h": 0.3}, jitter=2)],
                  cam((0, 1.6, 0.6, 0.66), (1, 1.9, 0.6, 0.62, "in"), handheld=5), [sfx("heartbeat", 0, 0.7, True, 10)]))
    beat(P[53], V("bgL18_field_path_night", [walk("boy_hoodie", [0.95, -0.15], fps=8, cyc="run_jacket", h=0.3, y=0.78)],
                  cam((0, 1.25, 0.7, 0.55), (1, 1.25, 0.3, 0.55, "smooth"), handheld=6),
                  [sfx("footsteps_run", 0, 0.6), sfx("heartbeat", 0, 0.6, True, 12), WIND(12, 0.4),
                   sfx("door_slam", 0.92, 0.6)]))
    beat(P[54], V("bg1_bedroom", [L("boy_hoodie/L5_peek_from_blanket", 0.7, h=0.42, jitter=1)],
                  cam((0, 1.2, 0.65, 0.6), (1, 1.7, 0.7, 0.6, "in")), [sfx("breath_close", 0.1, 0.5), CLOCK(10, 0.3)],
                  fade_out=1.2))
    a_48_end = len(S)

    # ---- ngày 49: bát canh, chiếc áo len
    a_49 = beat(P[55], V("bgL25s_khoa_feed_soup", [], cam((0, 1.2, 0.6, 0.58), (1, 1.45, 0.64, 0.56, "smooth")),
                         [sfx("spoon_bowl_tap", 0.6, 0.3)], fade_in=1.0))
    beat(P[56], V("bgL25k_mom_knit_collar", [], cam((0, 1.2, 0.6, 0.58), (1, 1.6, 0.66, 0.55, "smooth")),
                  [sfx("knitting_needles", 0.2, 0.3, True, 6)]))
    beat(P[57], V("black", [L("props/LH1_sweater_unfinished", 0.5, 0.85, h=0.55, tint=False)],
                  cam((0, 1.0, 0.5, 0.5), (1, 1.2, 0.5, 0.5, "smooth")), [], fade_out=1.5))
    a_49_end = len(S)

    # ---- đêm 49: mẹ mộng du xới cơm, gương
    a_night49 = beat(P[58], V("bgL15b_khoa_bed_awake_plain", [],
                              cam((0, 1.2, 0.6, 0.55), (1, 1.5, 0.6, 0.5, "in")),
                              [CLOCK(12, 0.5), sfx("clock_chime_3", 0.7, 0.9), sfx("footsteps_slow", 0.85, 0.3)], fade_in=1.0))
    beat(P[59], V("bgL9_main_room_altar_ong", [L("mother_alive/J1_sleepwalk_stand", **ALTAR_MOM),
                                               L("boy_hoodie/V1_sneak_peek_scared", 0.82, h=0.44)],
                  cam((0, 1.2, 0.6, 0.6), (1, 1.4, 0.45, 0.55, "smooth")), [sfx("heartbeat", 0, 0.4, True, 10), CLOCK(10, 0.25)],
                  bg_dim=0.2))
    beat(P[60], V("bgL9_main_room_altar_ong", [L("mother_alive/L1_sleepwalk_hold_bowl", **ALTAR_MOM, end=0.75),
                                               L("mother_alive/J1_sleepwalk_stand", **ALTAR_MOM, start=0.75),
                                               L("props/LF1_bowl_chopsticks_upright", 0.29, **SHELF_BOWL),
                                               L("props/LF1_bowl_chopsticks_upright", 0.34, **SHELF_BOWL, start=0.75)],
                  cam((0, 1.4, 0.42, 0.55), (1, 1.8, 0.36, 0.45, "smooth")),
                  [sfx("footsteps_slow", 0, 0.25, False, 3), sfx("chopsticks_tap_2", 0.78, 0.5)], bg_dim=0.2))
    beat(P[61], V("bgL31_mirror_opposite_room", [],
                  cam((0, 1.15, 0.5, 0.5), (1, 1.6, 0.5, 0.45, "in")),
                  [sfx("cloth_slide", 0.35, 0.9), sfx("reverse_swell", 0.4, 0.5)], bg_dim=0.2))
    beat(P[62], V("bgL19c_mirror_ong_whisper", [], cam((0, 1.15, 0.5, 0.5), (1, 1.55, 0.5, 0.42, "in")),
                  [sfx("whisper_eerie", 0.45, 0.35), sfx("breath_close", 0.75, 0.25)], flicker=0.06))
    ALTAR2 = [L("props/LF1_bowl_chopsticks_upright", 0.29, **SHELF_BOWL), L("props/LF1_bowl_chopsticks_upright", 0.34, **SHELF_BOWL)]
    beat(P[63], V("bgL9_main_room_altar_ong", ALTAR2 + [L("mother_alive/J3_khoa_grab_mom_hand", **{**ALTAR_MOM, "x": 0.45})],
                  cam((0, 1.3, 0.45, 0.55), (1, 1.6, 0.45, 0.5, "in"), handheld=4),
                  [sfx("footsteps_run", 0, 0.4, False, 1.0), sfx("heartbeat", 0.2, 0.6, True, 10)], bg_dim=0.2))
    beat(P[64],
         V("bgL9_main_room_altar_ong", ALTAR2 + [L("mother_alive/J3_khoa_grab_mom_hand", **{**ALTAR_MOM, "x": 0.45})],
           cam((0, 1.8, 0.4, 0.42), (1, 2.1, 0.38, 0.4, "smooth")), [sfx("whisper_eerie", 0.3, 0.35)], bg_dim=0.25),
         V("bgL9_main_room_altar_ong", ALTAR2 + [L("mother_alive/J4_sleepwalk_bow_portrait", **ALTAR_MOM),
                                        L("boy_hoodie/Q2_frozen_hands_mouth", 0.7)],
           cam((0, 1.3, 0.5, 0.55), (1, 1.4, 0.45, 0.5)), [CLOCK(10, 0.25)], bg_dim=0.25))
    beat(P[65], V("bgL19b_mirror_khoa_alone", [], cam((0, 1.15, 0.5, 0.5), (1, 1.45, 0.5, 0.45, "in")),
                  [sfx("reverse_swell", 0.2, 0.4)]))
    a_alone = silent("bgL9_main_room_altar_ong", 4.0,
                     [L("boy_hoodie/E2_back_stand", 0.38), L("props/LF1_bowl_chopsticks_upright", 0.29, **SHELF_BOWL),
                      L("props/LF1_bowl_chopsticks_upright", 0.34, **SHELF_BOWL)],
                     cam((0, 1.2, 0.4, 0.6), (1, 1.35, 0.36, 0.55)), [INSECTS(4, 0.35)], bg_dim=0.35)
    beat(P[66], V("bgL25m_khoa_hold_mom_hand", [], cam((0, 1.2, 0.6, 0.58), (1, 1.45, 0.64, 0.58)),
                  [sfx("old_man_breath", 0, 0.15, True, 12), CLOCK(12, 0.25)]))
    beat(P[67], V("bgL25m_khoa_hold_mom_hand", [], cam((0, 1.45, 0.64, 0.58), (1, 1.75, 0.66, 0.56, "smooth")),
                  [sfx("rooster_crow", 0.15, 0.5), sfx("old_man_breath", 0, 0.12, False, 6, 0, 3.0)], fade_out=2.0))
    a_night49_end = len(S)

    # ---- tang mẹ
    a_fun = beat(P[68], V("bgL25d_mom_dead_morning", [], cam((0, 1.2, 0.6, 0.58), (1, 1.6, 0.66, 0.56, "smooth")),
                          [WOOD(12, 0.2)], fade_in=1.5))
    beat(P[69],
         V("bgL20b_wake_coffin_mom_open", [day(L("co_ut/A1_hug_boy", 0.55, h=0.5))],
           cam((0, 1.2, 0.55, 0.6), (1, 1.4, 0.55, 0.58)), [BAND(12, 0.3), sfx("mourners_cry", 0, 0.25, True, 12)], bg_dim=0.1),
         V("bgL8_house_alley_dusk", [], cam((0, 1.25, 0.5, 0.55), (1, 1.4, 0.53, 0.5, "smooth")),
           [BAND(10, 0.15), INSECTS(10, 0.25)]))
    beat(P[70], V("bgL3m_coffin_mom_hand_talisman", [], cam((0, 1.15, 0.45, 0.45), (1, 1.5, 0.35, 0.4, "in")),
                  [sfx("chant_murmur", 0, 0.35, True, 12), WOOD(12, 0.2)]))
    beat(P[71],
         V("bgL20b_wake_coffin_mom_open", [L("thay_tu/A5_stand_point_stern", 0.7)], cam((0, 1.3, 0.68, 0.55), (1, 1.45, 0.7, 0.52)),
           [WOOD(10, 0.25)]),
         V("bgL5b_burial_shoveling", [], cam((0, 1.2, 0.5, 0.6), (1, 1.5, 0.5, 0.66, "smooth")), [WIND(12, 0.35)], bg_dim=0.2))
    beat(P[72], V("bgL20b_wake_coffin_mom_open", [day(L("grandma/A4_sit_hug_knees_grief", 0.3, h=0.36)),
                                            day(L("boy_hoodie/O2_mourn_frozen_pocket", 0.72, h=0.46))],
                  cam((0, 1.2, 0.5, 0.6), (1, 1.45, 0.68, 0.55, "smooth")),
                  [sfx("heartbeat", 0, 0.35, True, 12), sfx("mourners_cry", 0, 0.15, True, 12)], bg_dim=0.1))
    beat(P[73], V("black", [L("props/LH8_pencil_case_talisman", 0.5, 0.85, h=0.5, tint=False)],
                  cam((0, 1.0, 0.5, 0.5), (1, 1.3, 0.5, 0.5, "in")), [sfx("breath_close", 0.3, 0.35), CLOCK(10, 0.3)]))
    beat(P[74],
         V("bgL4_procession_field", [], cam((0, 1.25, 0.3, 0.5), (1, 1.25, 0.6, 0.5, "smooth")), [BAND(10, 0.4), WIND(10, 0.4)]),
         V("bgL17c_two_graves_small_hole", [day(L("boy_hoodie/O2_mourn_frozen_pocket", 0.75, h=0.42))],
           cam((0, 1.2, 0.55, 0.6), (1, 1.8, 0.4, 0.62, "in")), [WIND(12, 0.35), sfx("heartbeat", 0.4, 0.35, True, 8)]))
    beat(P[75], V("bgL17c_two_graves_small_hole", [day(L("props/LD3_crow_look_down", **KAPOK_DAY))],
                  cam((0, 1.3, 0.75, 0.4), (1, 1.2, 0.5, 0.55, "smooth")), [WIND(12, 0.4)]))
    beat(P[76], V("bgL21b_altar_three", [L("props/LF1_bowl_chopsticks_upright", 0.79, 0.545, h=0.15),     # mặt bàn trống trước ảnh ông
                                         L("props/LF1_bowl_chopsticks_upright", 0.69, 0.545, h=0.15)],      # cạnh bát ông, không đè lư hương
                  cam((0, 1.3, 0.7, 0.42), (1, 1.6, 0.72, 0.42, "smooth")), [WOOD(12, 0.2), sfx("ritual_bell", 0.2, 0.3)]))
    beat(P[77],
         V("bgL7_mom_room_day", [day(L("grandma/N8_fold_sweater", 0.6))],
           cam((0, 1.2, 0.58, 0.6), (1, 1.4, 0.6, 0.58)), [CLOCK(10, 0.2)], bg_dim=0.2),
         V("bgL7_mom_room_day", [day(L("props/LH9_sewing_machine_covered", **MACHINE))],
           cam((0, 1.25, 0.42, 0.62), (1, 1.6, 0.4, 0.62, "smooth")), [CLOCK(8, 0.2)], bg_dim=0.2, fade_out=1.0))
    a_fun_end = len(S)

    # ---- bà ho, tiếng muôi xới cơm
    a_end = beat(P[78], V("bgL9m_main_room_altar_three", [L("grandma/F3_cough_hunched", 0.45)],
                          cam((0, 1.2, 0.45, 0.6), (1, 1.4, 0.45, 0.58)),
                          [sfx("cough_old", 0.2, 0.8), sfx("cough_old", 0.7, 0.6), CLOCK(10, 0.2)], fade_in=1.0))
    beat(P[79], V("bgL8_house_alley_dusk", [L("props/LD1_crow_perched", 0.53, 0.235, h=0.035)],
                  cam((0, 1.3, 0.5, 0.4), (1, 1.9, 0.53, 0.28, "smooth")), [INSECTS(10, 0.25)]))
    beat(P[80], V("bgL15b_khoa_bed_awake_plain", [], cam((0, 1.2, 0.6, 0.55), (1, 1.5, 0.62, 0.52, "in")),
                  [sfx("cough_old", 0.1, 0.5), CLOCK(12, 0.4)]))
    beat(P[81], V("bgL9m_main_room_altar_three", [], cam((0, 1.3, 0.35, 0.45), (1, 2.0, 0.31, 0.36, "in")),
                  [sfx("rice_ladle_scoop", 0.1, 0.9, True, 8)], bg_dim=0.45))
    silent("black", 3.5, title_text="Còn tiếp", fade_in=1.0, fade_out=1.0,
           sounds=[sfx("rice_ladle_scoop", 0, 0.6, True, 3, 0, 1.0)])

    return dict(
        title="Lá bùa dưới gối ông — Phần 2: Bát cơm thứ hai",
        requests=ASSET_REQUESTS_P2,
        output="build/la_bua_duoi_goi_ong_p2.mp4",
        logline=("Bát cơm thứ hai cứ xuất hiện trên bàn thờ, mỗi lần một gần mẹ hơn. Thầy Tư nói về cách đổi đũa rồi từ chối "
                 "làm. Khoa vẫn giấu lá bùa — và đêm thứ bốn mươi chín, ông đến dắt mẹ đi."),
        music=[
            {"sound": "drone_low", "from": 1, "to": a_bowl_end, "volume": 0.5, "fade_in": 2.5, "fade_out": 2},
            {"sound": "memory_piano", "from": a_weak + 3, "to": a_market_end, "volume": 0.4, "fade_in": 2.5, "fade_out": 2.5},
            {"sound": "drone_low", "from": a_sew, "to": a_thay_end, "volume": 0.5, "fade_in": 2, "fade_out": 2},
            {"sound": "drone_low", "from": a_count, "to": a_count_end, "volume": 0.45, "fade_in": 2, "fade_out": 2},
            {"sound": "memory_piano", "from": a_bedside, "to": a_bedside_end, "volume": 0.4, "fade_in": 2, "fade_out": 2.5},
            {"sound": "drone_low", "from": a_48, "to": a_ghost + 1, "volume": 0.6, "fade_in": 2, "fade_out": 0.05},
            {"sound": "memory_piano", "from": a_49, "to": a_49_end, "volume": 0.35, "fade_in": 2, "fade_out": 2},
            {"sound": "drone_low", "from": a_night49, "to": a_alone - 1, "volume": 0.65, "fade_in": 2, "fade_out": 0.05},
            {"sound": "drone_low", "from": a_alone + 1, "to": a_night49_end, "volume": 0.4, "fade_in": 3, "fade_out": 2},
            {"sound": "drone_low", "from": a_end, "to": len(S) - 1, "volume": 0.6, "fade_in": 2, "fade_out": 0.05},
        ],
    )


# ============================================================ GHI FILE
PARTS = {1: part1, 2: part2}
PART = int(sys.argv[1]) if len(sys.argv) > 1 else 1
meta = PARTS[PART]()
story = json.loads((ROOT / "templates/kich_ban_mau.json").read_text(encoding="utf-8"))
story["title"] = meta["title"]
story["output"] = meta["output"]
story["logline"] = meta["logline"]
story["settings"]["audio"]["narration_volume"] = 1.4
story["settings"]["audio"]["duck"] = 0.28
story["settings"]["voice"]["tempo"] = 1.05        # người dùng chọn bản C (chậm hơn 1.15 của preset, bớt giật)
story["settings"]["voice"]["level_db"] = -20      # mọi câu cùng độ to
story["settings"]["audio"]["limiter_ceiling_db"] = -3.0   # AAC đẩy đỉnh lên ~2 dB (preview 64k chạm 0 dB ở -2)
story["characters"] = {
    "boy_hoodie": {"h": 0.46, "breathe": 0.008},
    "grandma": {"h": 0.5, "breathe": 0.006},
    "mother_alive": {"h": 0.6, "breathe": 0.006},
    "ong_noi": {"h": 0.56, "breathe": 0.005},
    "thay_tu": {"h": 0.56, "breathe": 0.005},
    "co_ut": {"h": 0.56, "breathe": 0.006},
    "props": {"h": 0.2, "breathe": 0},
    "cat_tabby": {"h": 0.13, "breathe": 0.01},
}
story["asset_requests"] = meta["requests"]
story["scenes"] = S
story["music"] = meta["music"]
out = ROOT / f"scripts/la_bua_duoi_goi_ong_p{PART}.json"
out.write_text(json.dumps(story, ensure_ascii=False, indent=1), encoding="utf-8")
print(out.relative_to(ROOT), len(S), "cảnh")
