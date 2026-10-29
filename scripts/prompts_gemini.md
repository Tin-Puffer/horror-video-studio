# Prompt Gemini — tạo thêm asset cho boy_hoodie

Cách dùng: đính kèm `assets/source/boy_hoodie_base.png` (và 1 sheet cũ) làm ảnh tham chiếu, dán prompt.
Mỗi sheet 2 hàng × 3 cột, nền trắng → chạy được `tools/cut_sprites.py`.

## Phần style chung (đã nằm sẵn trong mỗi prompt)
Same character as the reference image: a boy with messy spiky black hair, dark moss-green hoodie with drawstrings and front pocket, dark charcoal-gray pants, white sneakers. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, dot eyes, minimal flat colors. Character sheet, 16:9, pure plain white background, 6 full-body poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch, no text, no labels, no shadows on the ground, no background objects.

## Sheet C — khung chuyển động đi/chạy
...6 poses (left to right, top to bottom): 1) walking to the right, left leg forward, worried face; 2) walking to the right, right leg forward, worried face; 3) walking to the right, legs passing together mid-step, worried face; 4) running to the right in panic, left leg forward, mouth open; 5) running to the right, both feet off the ground mid-stride; 6) running to the right, right leg forward, arms swinging.

## Sheet D — khẩu hình & mặt (cận cảnh)
...6 head-and-shoulders close-up portraits, all facing front, same size and position: 1) neutral, mouth closed; 2) talking, mouth slightly open; 3) talking, mouth wide open "ah"; 4) eyes closed (blink); 5) whispering scared, small "o" mouth, sweat drop; 6) crying in fear, tears, trembling lips.

## Sheet E — trốn & sợ hãi
...6 poses: 1) seen fully from behind, walking away into the distance; 2) seen from behind, standing still; 3) crouching and hugging knees, terrified, shaking; 4) hiding, pressed against an invisible wall, peeking to the right; 5) covering his own mouth with both hands, holding breath, wide eyes; 6) covering both ears and squeezing eyes shut, crouching.

## Sheet F — đèn pin & điện thoại
...6 poses: 1) holding a flashlight pointing forward, nervous; 2) holding a flashlight pointing down, walking slowly; 3) shining phone flashlight forward, scared; 4) holding phone to ear, listening, frightened; 5) dropping the phone in shock, phone falling; 6) holding phone up showing the screen toward the viewer, terrified.

## Sheet G — ở nhà ban đêm
...6 poses: 1) lying in bed asleep under a blanket (simple bed); 2) sitting up in bed, startled awake; 3) sitting up in bed, pulling blanket up to his chin, scared; 4) standing, rubbing sleepy eyes with one hand; 5) reaching for a door handle (draw only the hand reaching, no door); 6) tiptoeing carefully, sneaking.

---

# Cho kịch bản "Cuộc gọi lúc 3 giờ sáng" (scripts/kich_ban_cuoc_goi_3h.md)

Thứ tự: GH0 (nhân vật mẫu) → GH-A, GH-B (đính kèm GH0 + 1 sheet boy_hoodie) → BG1–BG3b (đính kèm 1 sheet boy_hoodie).

## GH0 — nhân vật mẫu "Mẹ" (1 ảnh, 1:1)
A full-body character design of a creepy ghost woman who pretends to be a mother, standing straight, front view, arms hanging down at her sides. Unnaturally tall and thin with a slightly too-long neck and arms that reach below her knees, very pale gray-white skin, long straight black hair falling over her face so only one dark hollow eye shows, a faded beige cardigan over a long dark gray dress, bare feet with long toes. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi-like shapes and minimal flat colors, the same art style as the reference image, cute-creepy rather than gory. Pure plain white background, centered, full body visible with space around her, no text, no shadow on the ground. 1:1.

## GH-A — 6 dáng chính trong kịch bản (2x3, 16:9)
Same ghost woman as the first reference image (tall thin pale woman, long black hair covering her face, faded beige cardigan, long dark gray dress, bare feet, arms too long), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines as the references. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects. Poses (left to right, top to bottom): 1) standing far away facing the viewer, head bowed, hair hiding her whole face, arms hanging limp; 2) extreme close-up of one wide-open bloodshot eye with a tiny black pupil, strands of black hair around it, pale skin; 3) half of her body leaning in from the right side as if peeking around a door frame, head tilted sideways at an unnatural angle, one eye visible; 4) close-up of her face lunging toward the viewer, hair flying back, hollow black eyes, mouth stretched into a far-too-wide grin; 5) side view, one extremely long thin arm reaching forward to the right with long bony fingers; 6) crawling on all fours toward the viewer, head raised, hair dragging on the ground.

## GH-B — dáng bổ sung (2x3, 16:9)
[Dán nguyên đoạn đầu của GH-A, từ "Same ghost woman" đến hết "no background objects."] Poses: 1) walking slowly to the right, left foot forward, head bowed, arms limp; 2) walking slowly to the right, right foot forward, head bowed; 3) standing seen from behind, long hair down her back; 4) only a pale long-fingered hand with dark fingernails scratching downward, as if on a door; 5) standing still and smiling sweetly with her face visible, looking almost like a normal kind mother but with eyes that are completely black; 6) head only, upside down, hanging from above with hair falling downward, staring.

## Phông nền — tạo từng ảnh riêng (16:9)
Phần style chung (đã có sẵn trong từng prompt dưới đây).

BG1 phòng ngủ:
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat side view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones with only faint cold moonlight, lots of empty floor space in the lower third, no text. A small bedroom at 3 AM with NO bed (leave the right half of the floor empty), a closed bedroom door on the left, a window in the middle with moonlight and thin curtains, a small nightstand with a digital clock, a few posters on the wall, wooden floor.

BG2 hành lang:
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat side view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones with only faint cold moonlight, lots of empty floor space in the lower third, no text. A long narrow hallway inside a house running horizontally across the whole frame, wooden floor, two closed doors along the back wall, a small framed family photo, a light switch, both ends of the hallway fading into darkness.

BG3 cửa chính:
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat front view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones, lots of empty floor space in the lower third, no text. The front door of a house seen from inside, in the center, with a small round peephole, a lock and a door handle, a shoe rack with slippers on one side, a coat hook on the other, a thin line of faint yellow light under the door.

BG3b qua mắt mèo:
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, 16:9, no people, no text. The view through a door peephole: a circular fisheye lens view in the center surrounded by solid black, inside the circle a distorted, curved, empty apartment corridor at night lit by a single dim flickering ceiling light, a closed door across the corridor.
