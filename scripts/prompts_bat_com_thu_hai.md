# Prompt Gemini — "Bát cơm thứ hai"

## Nhân vật `mother_alive` — Mẹ lúc còn sống

Thứ tự: ME0 (nhân vật mẫu) → duyệt → ME-A, ME-B. Ảnh tham chiếu của Khoa: `build/refs/` (ghép sẵn từ sprite, nền trắng, không chữ).
Cùng người phụ nữ với ma `ghost_mother` (cùng áo cardigan be, váy xám đậm) nhưng là người bình thường:
tỉ lệ người thật kiểu chibi, mặt hiền lộ rõ, tóc búi gọn, đi dép lê nâu mòn gót. Không mặc đồ trắng.

### ME0 — nhân vật mẫu (1 ảnh, 1:1)
Đính kèm (đúng thứ tự): ① ảnh ma "Mẹ" (lấy trang phục) ② `build/refs/ref_boy_style.png` (lấy nét vẽ, tỉ lệ).

```
A full-body character design of a kind, gentle Vietnamese mother in her late thirties, standing straight, front view, arms relaxed at her sides, a soft warm smile. She wears the SAME outfit as the ghost woman in the first reference image — a faded beige cardigan over a long dark gray dress — but she is a normal living woman, NOT a ghost: normal human proportions (normal arm length, normal neck), healthy light skin with a little warmth in the cheeks, her black hair neatly tied back in a low bun with a few loose strands, her whole face clearly visible, simple dot eyes and a small smile in the same style as the boy in the second reference image. On her feet: worn dark brown plastic slippers. She is an adult, about one and a half times as tall as the boy in the reference. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, minimal flat colors, the same art style as the reference images. Never white clothing. Pure plain white background, centered, full body visible with space around her, no text, no shadow on the ground. 1:1.
```

### ME-A — các dáng trong hồi ức (2x3, 16:9)
Đính kèm: ① ME0 ② `build/refs/ref_boy_style.png`.

```
Same woman as the first reference image (a kind Vietnamese mother, black hair tied in a low bun, faded beige cardigan over a long dark gray dress, worn dark brown plastic slippers, face clearly visible), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions, dot eyes and minimal flat colors as the references. Never white clothing. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects, every pose drawn at the same scale. Poses (left to right, top to bottom): 1) side view facing right, standing and stirring a small cooking pot she holds by the handle with a ladle in her other hand, calm and content; 2) side view facing right, standing, one hand cupped beside her mouth calling someone to come and eat, warm smile; 3) side view facing right, sitting on a simple low wooden stool, holding a rice bowl close to her chin with chopsticks, eating; 4) side view facing right, sitting on the same wooden stool, carefully laying her chopsticks horizontally across the top of the empty rice bowl in her hand, a small habitual gesture; 5) side view facing right, standing and holding out a full bowl of rice with both hands as if handing it to a child, gentle smile; 6) front view, standing with both hands clasped in front of her, smiling softly at the viewer, like a portrait.
```

### ME-B — chu kỳ đi lê dép (2x3, 16:9)
Đính kèm: ① ME0 ② `build/refs/ref_boy_walk_cycle.png` (chu kỳ đi 6 khung của Khoa, để Gemini thấy cách chia khung).

```
Same woman as the first reference image (a kind Vietnamese mother, black hair tied in a low bun, faded beige cardigan over a long dark gray dress, worn dark brown plastic slippers, face clearly visible), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions, dot eyes and minimal flat colors as the references. Never white clothing. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects. A 6-frame walking animation cycle, all frames side view facing right, exactly the same size, same height and the same ground line, relaxed slow homely walk, slippers slightly dragging at the heel: 1) left foot forward touching the ground (contact); 2) weight down on the left foot, body slightly lower; 3) right leg passing the left, body upright; 4) right foot forward touching the ground (contact); 5) weight down on the right foot, body slightly lower; 6) left leg passing the right, body upright.
```

### Sau khi có ảnh
Gửi Claude kèm mã (ME0 / ME-A / ME-B). Claude cắt nền, đặt tên sprite, ghi `facing`, đo đường chân, tạo chu kỳ `walk`.

---

## Nhân vật `grandma` — Bà nội

Thứ tự: BN0 (nhân vật mẫu) → duyệt → BN-A, BN-B.
Bà ngoài 70, nhỏ người, hơi còng, tóc bạc búi sau gáy, áo bà ba nâu sẫm, quần đen ống rộng, dép tổ ong đen.
Mặt nghiêm, nhiều nếp nhăn, mắt chấm cùng kiểu Khoa. Không mặc đồ trắng, không đeo khăn tang trắng.

### BN0 — nhân vật mẫu (1 ảnh, 1:1)
Đính kèm (đúng thứ tự): ① ME0 (mẹ, để đồng bộ tỉ lệ người lớn) ② `build/refs/ref_boy_style.png`.

```
A full-body character design of a small, elderly Vietnamese grandmother in her seventies, standing, front view, slightly hunched back, hands clasped in front of her, a serious, worried but loving expression. Silver-gray hair pulled back into a small bun at the nape, a wrinkled kind face clearly visible, simple dot eyes in the same style as the characters in the reference images. She wears a plain dark brown traditional Vietnamese "ao ba ba" blouse with long sleeves and loose black trousers, simple black sandals. She is only a little taller than the boy and noticeably shorter than the woman in the first reference image. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, minimal flat colors, the same art style as the reference images. Never white clothing, no white headscarf. Pure plain white background, centered, full body visible with space around her, no text, no shadow on the ground. 1:1.
```

### BN-A — các dáng chính (2x3, 16:9)
Đính kèm: ① BN0 ② `build/refs/ref_boy_style.png`.

```
Same elderly woman as the first reference image (a small Vietnamese grandmother, slightly hunched, silver-gray hair in a small bun, dark brown "ao ba ba" blouse, loose black trousers, black sandals, wrinkled face clearly visible), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions, dot eyes and minimal flat colors as the references. Never white clothing. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects, every pose drawn at the same scale. Poses (left to right, top to bottom): 1) side view facing right, standing and leaning forward, both hands reaching out at chest height as if firmly holding a child's hands, serious stern face, warning; 2) side view facing right, standing with head bowed, holding three lit incense sticks between both palms raised to her forehead, thin wisps of smoke, praying; 3) side view facing right, standing, holding a small bowl against her hip and flinging a handful of rice and salt grains outward with her other hand, grains scattering in the air; 4) side view facing right, sitting slumped on the ground hugging her knees, head lowered, exhausted and grieving; 5) side view facing right, standing, holding a rice bowl in one hand and scooping rice into it with a wooden rice paddle in the other hand, calm, eyes lowered; 6) front view, standing still, head bowed so low that her face is hidden in shadow, arms hanging at her sides, eerie and silent.
```

| # | Dáng | Dùng cho cảnh |
|---|---|---|
| 1 | Nắm tay dặn dò | Bà dặn ba điều |
| 2 | Thắp nhang khấn | Cúng cơm, lễ cúng cô hồn |
| 3 | Rải gạo muối | Lễ cúng cô hồn ngoài sân |
| 4 | Ngồi sụp ôm gối | Sau đám tang, đêm bà kiệt sức |
| 5 | **Xới bát cơm** | **Cảnh kết: bát cơm thứ hai** |
| 6 | Cúi mặt khuất bóng | Cảnh kết, nhịp rợn cuối |

### BN-B — chu kỳ đi chậm, còng (2x3, 16:9)
Đính kèm: ① BN0 ② `build/refs/ref_boy_walk_cycle.png`.

```
Same elderly woman as the first reference image (a small Vietnamese grandmother, slightly hunched, silver-gray hair in a small bun, dark brown "ao ba ba" blouse, loose black trousers, black sandals, wrinkled face clearly visible), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions, dot eyes and minimal flat colors as the references. Never white clothing. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects. A 6-frame walking animation cycle, all frames side view facing right, exactly the same size, same height and the same ground line, a slow careful elderly walk, back slightly hunched, one hand resting on her lower back, short steps: 1) left foot forward touching the ground (contact); 2) weight down on the left foot, body slightly lower; 3) right leg passing the left, body upright; 4) right foot forward touching the ground (contact); 5) weight down on the right foot, body slightly lower; 6) left leg passing the right, body upright.
```

### Sau khi có ảnh
Gửi Claude kèm mã (BN0 / BN-A / BN-B).

---

## Nhân vật `hungry_ghost` — Cô hồn đói

Thứ tự: CH0 (nhân vật mẫu) → duyệt → CH-A.
Bóng người gầy trơ xương, cổ dài nhỏ như que, bụng hơi phình, da xám tro xanh, bàn tay đen đến cổ tay,
quấn giẻ rách màu tối, hốc mắt đen sâu, không có mặt rõ ràng. Không có màu trắng (kể cả mắt).
Cô hồn không đi lại trên màn hình mà hiện ra hoặc mờ đi tại chỗ, nên không cần chu kỳ đi.
Cảnh "chen chúc" ghép từ nhiều sprite (lật ngang, đổi cỡ, làm tối) chứ không vẽ cả đám trong một hình.

### CH0 — nhân vật mẫu (1 ảnh, 1:1)
Đính kèm (đúng thứ tự): ① ảnh ma "Mẹ" (lấy độ rợn, nét ma) ② `build/refs/ref_boy_style.png`.

```
A full-body character design of a starving hungry ghost from Vietnamese folklore, standing hunched, front view. An emaciated skeletal body with visible ribs, an unnaturally long thin neck like a stick, a slightly swollen belly, ash gray-blue skin, both hands and forearms stained pitch black up to the wrists, long thin bony fingers. Wrapped in torn, ragged dark brown and gray cloth. Sparse stringy black hair. Deep hollow pitch-black eye sockets with no pupils, a small dark gaping mouth, no clear facial features. Creepy and pitiful at the same time, the same eerie mood as the ghost woman in the first reference image. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, minimal flat colors, the same art style as the reference images. About as tall as the boy in the second reference image. Absolutely no white anywhere on the character, no white eyes, no white clothing. Pure plain white background, centered, full body visible with space around it, no text, no shadow on the ground. 1:1.
```

### CH-A — các dáng (2x3, 16:9)
Đính kèm: ① CH0 ② ảnh ma "Mẹ".

```
Same hungry ghost as the first reference image (emaciated skeletal body, very long thin stick-like neck, slightly swollen belly, ash gray-blue skin, pitch black hands up to the wrists, long bony fingers, torn dark ragged cloth, hollow pitch-black eye sockets), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions and minimal flat colors as the references. Absolutely no white on the character. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects, every pose drawn at the same scale. Poses (left to right, top to bottom): 1) side view facing right, crouching low over a rice bowl on the ground, greedily stuffing a fistful of rice into its mouth with a black hand; 2) side view facing right, crouching, head suddenly raised and turned toward the viewer, hollow black eyes staring, frozen; 3) front view, standing hunched, arms hanging limp, long neck tilted slightly to one side, staring at the viewer; 4) side view facing right, crawling low on all fours, long neck stretched forward, bony spine showing; 5) side view facing right, standing and reaching one long black hand forward with spread bony fingers, grasping for food; 6) back view, standing hunched with its back to the viewer, head turned slightly so one hollow eye is visible over its shoulder.
```

| # | Dáng | Dùng cho cảnh |
|---|---|---|
| 1 | Cúi bốc cơm ăn | Nhìn trộm qua khe cửa, tiếng nhai nhóp nhép |
| 2 | Ngẩng lên nhìn | Nhịp hù: bị phát hiện đang nhìn trộm |
| 3 | Đứng còng chính diện | Ghép đám chen chúc ngoài cổng |
| 4 | Bò | Bóng thấp thoáng sát đất |
| 5 | Vươn tay đen | Dấu tay đen, giành mâm cơm |
| 6 | Quay lưng ngoái lại | Ghép đám đông, cảnh lễ cúng cô hồn |

### Sau khi có ảnh
Gửi Claude kèm mã (CH0 / CH-A).

---

## Thêm dáng cho Khoa (`boy_hoodie`) — sheet KH-M (2x3, 16:9)
Đính kèm: ① `build/refs/ref_boy_style.png`.
Đã có sẵn, không vẽ lại: nhìn qua mắt mèo (K5), trùm chăn (G3/L5), ngồi ôm gối (E3), với nắm cửa (G5).

```
Same boy as the reference image: messy spiky black hair, dark moss-green hoodie with drawstrings and front pocket, dark charcoal-gray pants, white sneakers. Hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, dot eyes, minimal flat colors. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects except the small props named below, every pose drawn at the same scale. Poses (left to right, top to bottom): 1) side view facing right, kneeling on both knees, head bowed, holding three lit incense sticks between both palms raised to his forehead, thin wisps of smoke, sad; 2) side view facing right, standing, carefully carrying a full bowl of rice with both hands in front of his chest, a pair of chopsticks stuck upright in the rice, solemn; 3) side view facing right, sitting on a simple low wooden stool, holding a rice bowl and chopsticks, eating quietly, lonely; 4) side view facing right, sitting on the same low wooden stool holding a rice bowl, head turned sharply to look back over his shoulder at something behind him, eyes wide, frozen with fear; 5) lying flat on his back on the ground, unconscious, eyes closed, arms limp, side view with head to the left; 6) side view facing right, lying on his stomach on the floor, chin on the ground, one eye pressed close to peek through a low gap, hands flat beside his face, terrified.
```

| # | Dáng | Dùng cho cảnh |
|---|---|---|
| 1 | Quỳ thắp nhang | Cúng cơm cho mẹ |
| 2 | Bưng bát cơm cắm đũa | Đặt bát cơm lên bàn thờ |
| 3 | Ngồi ăn một mình | Bữa cơm sau khi mẹ mất |
| 4 | Ngồi ăn, ngoái lại sợ | Ghế của mẹ bị kéo ra, tiếng dép |
| 5 | Nằm ngất | Sau cao trào đêm 49 |
| 6 | Nằm sấp nhìn qua khe dưới cửa | Nhìn trộm cô hồn, bóng mẹ ở khe sáng đêm 49 |

---

## Thêm dáng cho ma "Mẹ" (`ghost_mother`)
Đính kèm cho cả hai sheet: ① ảnh gốc ma "Mẹ" ② một sheet ma "Mẹ" đã có (để giữ đúng tỉ lệ).

### GM-M — dáng mới (2x3, 16:9)

```
Same ghost woman as the reference images: unnaturally tall and thin, very pale gray-white skin, long straight black hair covering most of her face, faded beige cardigan, long dark gray dress, bare feet, arms slightly too long. Same hand-drawn crayon / colored-pencil style with thick black outlines, simple proportions, minimal flat colors. Never white clothing. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects except a simple low wooden stool where named, every pose drawn at the same scale. Poses (left to right, top to bottom): 1) back view, sitting perfectly still on a simple low wooden stool, back straight, long black hair hanging down her back, head slightly bowed; 2) sitting on the same stool seen from behind, but her head turned unnaturally far around over her shoulder to look at the viewer, a gentle mother's smile with completely black hollow eyes; 3) side view facing right, standing, face buried in both hands, shoulders hunched, crying silently; 4) side view facing right, crouching low beside a rice bowl on the ground, eating rice with her bare fingers, hair hanging over her face so it is hidden; 5) back view, standing, slowly turning her head over her right shoulder, half of a pale face visible through the hair, one black eye; 6) bust close-up, front view, hair parted from her face, pale sad face with thin black tears running from black hollow eyes, mouth slightly open as if speaking softly.
```

| # | Dáng | Dùng cho cảnh |
|---|---|---|
| 1 | Ngồi quay lưng trên ghế | Ghế của mẹ, Khoa thấy bóng ngồi ở bàn ăn |
| 2 | Ngồi ngoái đầu, mắt đen cười | Nhịp hù ở bàn ăn |
| 3 | Đứng úp mặt khóc | Bóng đổ sau cửa, mở đầu và đêm 49 (render thành bóng đen) |
| 4 | Ngồi bốc cơm ăn | Nhìn trộm: không rõ là mẹ hay cô hồn |
| 5 | Quay lưng, ngoảnh lại | Đêm 49: "mẹ quay lại" |
| 6 | Cận mặt, chảy lệ đen, nói | Câu thoại "Sao con lại gọi…" |

### GM-W — chu kỳ đi 6 khung (2x3, 16:9)
Chu kỳ `walk` hiện có chỉ 2 khung (GH7, GH8), chưa đạt quy tắc tối thiểu 4 khung, nên vẽ bộ đầy đủ thay thế.

```
Same ghost woman as the reference images: unnaturally tall and thin, very pale gray-white skin, long straight black hair covering her face, faded beige cardigan, long dark gray dress, bare feet, arms slightly too long hanging limp. Same hand-drawn crayon / colored-pencil style with thick black outlines, minimal flat colors. Never white clothing. Character sheet, 16:9, pure plain white background, 6 poses arranged in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, no background objects. A 6-frame walking animation cycle, all frames side view facing right, exactly the same size, same height and the same ground line, a slow, stiff, unnatural walk, head bowed, arms dangling: 1) left foot forward touching the ground (contact); 2) weight down on the left foot, body slightly lower; 3) right leg passing the left, body upright; 4) right foot forward touching the ground (contact); 5) weight down on the right foot, body slightly lower; 6) left leg passing the right, body upright.
```

### Sau khi có ảnh
Gửi Claude kèm mã (KH-M / GM-M / GM-W).

---

## Bổ sung: mẹ gác đũa ngang bát — ME-A4 (1 ảnh, 1:1)
Sheet ME-A thiếu dáng này (chi tiết gài cho cú lật cuối). Đính kèm: ① ME0.

```
Same woman as the reference image (kind Vietnamese mother, black hair in a low bun, faded beige cardigan, long dark gray dress, dark brown slippers), same hand-drawn crayon style, thick black outlines, chibi proportions, dot eyes. Side view facing left, sitting on a simple low wooden stool, holding an EMPTY rice bowl in one hand at chest height and with the other hand carefully laying a pair of chopsticks HORIZONTALLY across the top rim of the bowl, both chopsticks lying flat side by side across the bowl, a small habitual gesture, calm gentle face looking down at the bowl. Never white clothing. Pure plain white background, full body, no text, no shadow. 1:1.
```

---

## Phông nền (mỗi ảnh riêng, 16:9)
Bối cảnh mặc định: **nhà ống ở thị trấn** (dùng lại phòng ngủ + hành lang có sẵn), **bỏ cảnh đám tang ngoài đồng** (bà dặn ba điều ngay trong gian thờ).
Đính kèm cho mọi phông: ① `assets/backgrounds/bg2_hallway.png` (giữ nét vẽ, tông màu). Thêm ảnh khác nếu ghi.
Bản "ngày" dùng cho hồi ức: đính kèm thêm bản đêm tương ứng để giữ nguyên bố cục.

### BG4 — gian nhà chính, bàn thờ + bàn ăn (đêm)
```
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat side view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones, lots of empty floor space in the lower third, no text. The main room of a narrow Vietnamese town house: on the back wall at the LEFT, a high wooden ancestral altar shelf with a small framed portrait photo, a brass incense bowl with a few incense sticks, two small red candles glowing faintly, a plate of fruit and a bowl of rice; on the RIGHT side, a low wooden dining table with two simple low wooden stools, one stool pulled slightly away from the table; patterned old ceramic floor tiles, a wall calendar, a closed door to the kitchen at the far right. The only warm light is a faint red glow from the altar candles.
```

### BG4d — gian nhà chính (ngày, hồi ức)
Đính kèm thêm: ② BG4.
```
Exactly the same room and layout as the second reference image, same hand-drawn crayon / colored-pencil style and thick black outlines, 16:9, empty scene with no people, no text, but now in the warm late afternoon of a happy memory: soft golden sunlight through an open window, warm cream and honey tones, the altar has NO portrait photo and no candles, only a small vase of flowers, a pot of steaming food on the dining table, cozy and peaceful, lots of empty floor space in the lower third.
```

### BG5 — cận bàn thờ (đêm)
Đính kèm thêm: ② ME0 (để vẽ ảnh thờ đúng mặt mẹ).
```
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the first reference image, 16:9, close-up front view, no people, no text, dark night lighting with a faint warm red candle glow. Close-up of the top of a Vietnamese ancestral altar: in the back center a framed portrait photo of the smiling woman from the second reference image (head and shoulders, black frame with a small black mourning ribbon in the top corner), a brass incense bowl full of ash with three burning incense sticks and rising thin smoke on the left, two small red candles on both sides; the front center of the altar surface is a large EMPTY wooden area (leave it completely clear), deep shadows around the edges.
```

### BG6 — bếp (đêm)
```
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat side view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones with faint cold moonlight from a small window, lots of empty floor space in the lower third, no text. A small old Vietnamese town-house kitchen: a tiled counter with a two-burner gas stove and an aluminium pot on the left, a rice cooker, a hanging shelf with bowls and chopsticks in a holder, a small window above the counter, a narrow doorway on the right leading to darkness, old ceramic floor tiles, the middle and right of the floor left empty.
```

### BG6d — bếp (ngày, hồi ức)
Đính kèm thêm: ② BG6.
```
Exactly the same kitchen and layout as the second reference image, same hand-drawn crayon / colored-pencil style and thick black outlines, 16:9, empty scene with no people, no text, but now in warm late afternoon light of a happy memory: golden sunlight through the window, steam rising from the pot on the stove, warm cream and honey tones, cozy and peaceful, lots of empty floor space in the lower third.
```

### BG7 — sân trước và cổng sắt (đêm)
```
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, simple shapes, 16:9, flat side view like a 2D stage, empty scene with no people and no characters, dark night lighting in deep blue and gray tones with faint cold moonlight, lots of empty floor space in the lower third, no text. The small paved front yard of a Vietnamese town house at night: a tall rusty iron folding gate across the right half of the frame with the empty dark street visible through its bars, a single dim street lamp far away, a potted plant and a small outdoor offering table on the left, cracked cement floor, wisps of mist near the ground beyond the gate.
```

### BG8 — cửa phòng ngủ nhìn từ trong, khe sáng (đêm 49)
Đính kèm thêm: ② `assets/backgrounds/bg1_bedroom.png`.
```
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference images, simple shapes, 16:9, flat front view, empty scene with no people, no text, very dark night lighting in deep blue and black. Inside the same bedroom as the second reference image, facing its closed wooden bedroom door in the center of the frame, the door is plain with a metal handle and a simple bolt lock, a bright thin horizontal line of warm yellow light shining through the gap under the door onto the floor, walls fading into darkness, empty floor in the lower third.
```

### BG9 — nhìn qua khe dưới cửa (góc nhìn của Khoa)
```
Background illustration for a horror animation, same hand-drawn crayon / colored-pencil texture and thick black outlines as the reference image, 16:9, no people, no text. Point of view of someone lying on the floor peeking through the narrow gap under a door: the whole frame is solid black except a wide horizontal slit across the middle (about one third of the frame height), and through the slit a low ground-level view of an old ceramic-tiled floor stretching away, dimly lit by a faint red candle glow from far away, empty floor in the middle of the slit, deep shadows.
```

---

## Đạo cụ cận cảnh — sheet DC (2x3, 16:9)
Đính kèm: ① `build/refs/ref_boy_style.png`. Đạo cụ đặt lên BG5 (cận bàn thờ) hoặc mặt bàn.

```
Prop sheet in the same hand-drawn crayon / colored-pencil texture with thick black outlines and minimal flat colors as the reference image. 16:9, pure plain white background, 6 objects arranged in a 2x3 grid with wide empty space between them, objects must not overlap or touch each other or the image edges, every object drawn large, slightly from above (three-quarter view), with a THICK black outline all the way around, no text, no labels, no shadows. Objects (left to right, top to bottom): 1) a gray ceramic rice bowl heaped with white rice, a whole peeled boiled egg on top and a pair of wooden chopsticks stuck straight up in the rice; 2) the same gray rice bowl half eaten, the rice messy, with a pair of wooden chopsticks laid horizontally across the top rim of the bowl; 3) the same gray rice bowl completely empty and licked clean, with broken pieces of eggshell beside it; 4) a brass incense bowl full of gray ash with three incense sticks, one of them snapped in half and bent over, no smoke; 5) two smeared black handprints with long thin fingers, like soot marks, just the marks themselves; 6) a pair of worn dark brown plastic slippers, side by side, the heels worn down.
```

| # | Đạo cụ | Dùng cho cảnh |
|---|---|---|
| 1 | Bát cơm cúng, đũa cắm thẳng, trứng | Cúng cơm đêm đầu |
| 2 | Bát vơi, đũa gác ngang | **Dấu hiệu "mẹ về"**, gài cho cú lật |
| 3 | Bát sạch trơn + vỏ trứng | Leo thang: thứ khác đã ăn |
| 4 | Bát hương, nhang gãy | Điềm xấu |
| 5 | Dấu tay đen | Leo thang, cô hồn |
| 6 | Đôi dép của mẹ | Tiếng dép, đêm 49 |

---

## Âm thanh (ElevenLabs Sound Effects)
Đặt tên file đúng mã. Thời gian = thanh Duration (không ghi vào prompt).
Dùng lại có sẵn: footsteps_slow, floor_creak, heartbeat, whisper_eerie, knock_3, door_handle_rattle, ghost_stinger, reverse_swell, drone_low, breath_close, body_fall, clock_tick.

| Mã (tên file) | Thời gian | Prompt |
|---|---|---|
| slipper_drag | 12s | Slow shuffling footsteps of plastic house slippers dragging on a ceramic tile floor, heels scraping, quiet house at night, seamless loop |
| chopsticks_clatter | 4s | Many wooden chopsticks clattering against ceramic bowls at once, hurried, in a dark empty room |
| spoon_bowl_tap | 3s | A metal spoon slowly tapping the rim of a ceramic bowl three times, quiet room, slight echo |
| chewing_wet | 8s | Greedy wet chewing and slurping of rice, several mouths eating fast, close and unsettling, seamless loop |
| woman_sob_door | 10s | A woman crying softly and choking back sobs, muffled behind a closed wooden door, quiet night |
| rain_roof | 30s | Steady rain falling on a metal roof and dripping from gutters at night, seamless loop |
| night_insects | 30s | Quiet Southeast Asian night ambience, crickets and geckos chirping, distant and calm, seamless loop |
| dog_howl | 5s | A single dog howling long and mournfully in the far distance at night |
| door_creak_open | 3s | An old wooden bedroom door slowly creaking open, long eerie squeak of the hinges |
| door_bolt_lock | 1.5s | A small metal bolt lock slid shut on a wooden door, sharp click |
| gate_rattle | 3s | An old iron folding gate rattling and shaking as if someone outside is pulling it, metallic clanks |
| ritual_bell | 6s | A Buddhist wooden fish block knocked slowly three times followed by a small brass prayer bell ringing, temple reverb |
| paper_burn | 15s | Paper offerings burning in a metal bin outdoors, crackling fire and soft flutter, seamless loop |
| rice_scatter | 2s | A handful of rice grains and salt thrown onto a cement yard, light pattering |

## Nhạc nền (ElevenLabs Music, 60s)

| Mã (tên file) | Prompt |
|---|---|
| music_memory_sad | Gentle melancholic piano with soft warm strings, nostalgic and tender, slow tempo, remembering a loving mother, no drums, seamless loop |
| music_tension_rise | Slow-building horror tension underscore, low pulsing strings and dissonant high violins, creeping dread that grows steadily, no melody, seamless loop |


---

# Đợt sửa sau bản xem trước (2026-10-30)

## BK — Bà nắm tay Khoa (1 sheet 2 dáng, 16:9)
Đính kèm: ① `assets/source/grandma_base.png` ② `build/refs/ref_boy_style.png`

```
Two characters drawn TOGETHER in each pose: the elderly grandmother from the first reference image (small, slightly hunched, silver hair in a bun, dark brown ao ba ba blouse, loose black trousers, black sandals) and the boy from the second reference image (messy spiky black hair, dark moss-green hoodie, dark charcoal-gray pants, white sneakers). The grandmother is only a little taller than the boy. Same hand-drawn crayon / colored-pencil texture, thick black outlines, simple chibi proportions, dot eyes, minimal flat colors. 16:9, pure plain white background, 2 separate groups side by side with a very wide empty gap between them, groups must not touch each other or the image edges, no text, no ground shadows, both groups at the same scale. Group 1 (left): side view, the grandmother on the left facing right, the boy on the right facing left, she firmly holds both of the boy's hands in hers at chest height, leaning toward him with a serious, worried, tearful face, the boy looks up at her, sad and scared. Group 2 (right): side view, the grandmother on the left facing right, bending to whisper into the boy's ear with one hand cupped beside her mouth, her other hand on his shoulder, the boy stands still facing left, eyes wide.
```

## BG9b, BG9c — Nhìn qua khe dưới cửa, cô hồn vẽ sẵn trong cảnh (16:9)
Đính kèm: ① `assets/backgrounds/bg9_door_gap.png` (giữ đúng khung khe cửa) ② `assets/source/hungry_ghost_base.png`

**BG9b — đám cô hồn ăn quanh mâm**
```
Exactly the same composition as the first reference image: the whole frame is solid black except the same wide horizontal slit across the middle, a low ground-level view through the gap under a door onto an old ceramic-tiled floor, dim red candle glow from far away. Same hand-drawn crayon / colored-pencil texture and thick black outlines, 16:9, no text. Now, seen through the slit at floor level: several starving hungry ghosts like the creature in the second reference image crouch around a low tray of rice bowls on the floor in the middle distance; because of the low point of view the top edge of the slit cuts them off, so we mostly see their bony knees, ragged dark cloth, thin gray legs and their long pitch-black hands grabbing rice from the bowls and stuffing it upward out of view; a couple of overturned bowls and spilled rice on the tiles, one ghost further back shown whole but small and hunched. Creepy, dark, the red glow behind them.
```

**BG9c — một con ngẩng lên nhìn thẳng vào khe (cú hù)**
```
Exactly the same composition as the first reference image: solid black frame with the same wide horizontal slit across the middle, ground-level view under a door. Same hand-drawn crayon / colored-pencil texture and thick black outlines, 16:9, no text. Now one hungry ghost like the creature in the second reference image has lowered its head all the way to the floor, close to the door, its face turned sideways and pressed against the tiles, filling the middle of the slit, staring straight into the gap at the viewer with deep hollow pitch-black eye sockets, a dark gaping mouth with grains of rice around it, one long black hand flat on the floor beside its face. The rest of the tray and other ghosts are blurred dark shapes behind it in the red glow. Terrifying.
```

## ME-W2 — Mẹ đi, bước rõ (2x3, 16:9)
Đính kèm: ① `assets/source/mother_alive_base.png` ② `build/refs/ref_boy_walk_cycle.png`

```
Same woman as the first reference image (kind Vietnamese mother, black hair tied in a low bun, faded beige cardigan, long dark gray dress, worn dark brown plastic slippers, face clearly visible), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions, dot eyes and minimal flat colors. Never white clothing. Character sheet, 16:9, pure plain white background, 6 poses in a 2x3 grid with wide empty space between poses, poses must not overlap or touch each other or the image edges, no text, no labels, no ground shadows. A 6-frame walking animation cycle like the boy's cycle in the second reference image, all frames side view facing right, exactly the same size and the same ground line. Make the motion CLEARLY VISIBLE: the dress is a little shorter so both ankles and slippers are always visible, the dress hem swings with each step, long clear strides, both arms swing clearly opposite to the legs: 1) left foot far forward heel touching the ground, right foot far back on its toes, right arm forward; 2) weight on the left foot, knees bent, body lowest; 3) right leg passing the left leg, body highest, arms by her sides; 4) right foot far forward heel touching, left foot far back, left arm forward; 5) weight on the right foot, body lowest; 6) left leg passing the right, body highest.
```

## BN-W2 — Bà đi, bước rõ (2x3, 16:9)
Đính kèm: ① `assets/source/grandma_base.png` ② `build/refs/ref_boy_walk_cycle.png`

```
Same elderly grandmother as the first reference image (small, slightly hunched, silver hair in a bun, dark brown ao ba ba blouse, loose black trousers, black sandals), same hand-drawn crayon / colored-pencil style, thick black outlines, chibi proportions, dot eyes. Character sheet, 16:9, pure plain white background, 6 poses in a 2x3 grid with wide empty space between poses, no overlap, no text, no ground shadows. A 6-frame walking animation cycle like the boy's cycle in the second reference image, all frames side view facing right, exactly the same size and ground line, a slow hunched old-lady walk but with CLEARLY VISIBLE steps: one hand resting on her lower back, the other arm swinging, trousers showing clearly which leg is forward: 1) left foot forward heel down, right foot back on its toes; 2) weight on the left foot, body lowest; 3) right leg passing the left, body highest; 4) right foot forward heel down, left foot back; 5) weight on the right foot, body lowest; 6) left leg passing the right, body highest.
```

## DC1b — Bát cơm cúng, đũa cắm THẲNG ĐỨNG (1:1)
Đính kèm: ① `assets/source/props_sheet_DC.png` (giữ đúng kiểu bát)

```
The same gray ceramic rice bowl as the first object in the reference image, same hand-drawn crayon / colored-pencil texture, thick black outline all the way around, minimal flat colors, three-quarter view from slightly above. The bowl is heaped with white rice with a whole peeled boiled egg on top, and a pair of wooden chopsticks stuck PERFECTLY VERTICAL, straight up and parallel, side by side, planted in the very center of the rice like a Vietnamese offering bowl for the dead — the chopsticks are NOT tilted and NOT crossed. 1:1, pure plain white background, centered, the bowl drawn large with space around it, no text, no shadow.
```

## VM — Đốt vàng mã (1 sheet 2x3, 16:9)
Đính kèm: ① `assets/source/grandma_base.png` ② `assets/source/props_sheet_DC.png`

```
Same hand-drawn crayon / colored-pencil texture, thick black outlines, minimal flat colors as the references. 16:9, pure plain white background, 6 items in a 2x3 grid with wide empty space between them, items must not overlap or touch each other or the image edges, no text, no labels, no ground shadows, items 1-3 drawn at exactly the same size and position in their cells. Top row — a 3-frame flicker animation of the same small rusty old metal bucket used for burning joss paper, three-quarter view, filled with burning Vietnamese gold-and-red joss paper, bright orange and yellow flames rising above the rim, dark gray (never white) smoke, glowing embers; only the flame shapes change between frames: 1) flames leaning left; 2) flames tall and straight; 3) flames leaning right with a few flying sparks. Bottom row — the grandmother from the first reference image (small, hunched, silver hair bun, dark brown ao ba ba blouse, loose black trousers, black sandals), side view facing right: 4) crouching low and dropping a stack of gold joss paper forward into a fire in front of her (the fire itself not drawn), solemn face lit warmly; 5) standing, holding a thick stack of gold-and-red joss paper against her chest, head bowed; 6) a loose stack of folded gold-and-red joss paper lying on the ground (prop only).
```


---

## Làm lại chu kỳ đi (lần 3, không đính kèm ảnh Khoa)

### ME-W3 — Mẹ đi (2x3, 16:9)
Đính kèm: ① `assets/source/mother_alive_base.png`

```
Same woman as the reference image (kind Vietnamese mother, black hair tied in a low bun, faded beige cardigan, long dark gray dress that ends at mid-calf so both ankles are always visible, worn dark brown plastic slippers, face clearly visible), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions, dot eyes, minimal flat colors. Never white clothing. Animation sheet, 16:9, pure plain white background, 6 frames in a 2x3 grid (read left to right, top to bottom), wide empty space between frames, frames must not overlap or touch each other or the image edges, no text, no numbers, no labels, no ground shadows, no ground line. A smooth 6-frame walk cycle, every frame a strict side view facing RIGHT, the character exactly the same size in every frame, feet always resting on the same imaginary ground level, head at the same height except where noted. Each frame must look clearly different in the legs and arms:
1) CONTACT: long stride, left leg stretched far forward with the heel just touching the ground and toes up, right leg stretched far back on its toes, right arm swung forward, left arm swung back.
2) DOWN: left foot flat on the ground taking the weight, left knee bent, right foot lifting off behind, body slightly lower, arms halfway.
3) PASSING: standing on the straight left leg, the right leg bent at the knee and lifted, passing right next to the left leg, both feet close together under the body, arms hanging by her sides, body slightly higher.
4) CONTACT: the mirror of frame 1 — right leg stretched far forward heel touching, left leg far back on its toes, left arm forward, right arm back.
5) DOWN: the mirror of frame 2 — right foot flat taking the weight, right knee bent, left foot lifting behind, body slightly lower.
6) PASSING: the mirror of frame 3 — standing on the straight right leg, the left leg bent and passing next to it, feet close together, arms by her sides, body slightly higher.
The dress hem swings with the legs. Calm, homely walk.
```

### BN-W3 — Bà đi (2x3, 16:9)
Đính kèm: ① `assets/source/grandma_base.png`

```
Same elderly grandmother as the reference image (small, slightly hunched, silver hair in a bun, dark brown ao ba ba blouse, loose black trousers, black sandals, wrinkled kind face, dot eyes), drawn in the same hand-drawn crayon / colored-pencil style with thick black outlines, simple chibi proportions, minimal flat colors. Animation sheet, 16:9, pure plain white background, 6 frames in a 2x3 grid (read left to right, top to bottom), wide empty space between frames, frames must not overlap or touch each other or the image edges, no text, no numbers, no labels, no ground shadows, no ground line. A smooth 6-frame walk cycle of a slow, slightly hunched old woman, every frame a strict side view facing RIGHT, exactly the same size in every frame, feet always on the same imaginary ground level. Her LEFT hand rests on her lower back in every frame; only her right arm swings. Short but clearly visible steps, the loose trousers clearly show which leg is in front. Each frame must look clearly different in the legs:
1) CONTACT: left leg forward with the heel touching the ground, right leg back on its toes, right arm swung forward.
2) DOWN: left foot flat taking the weight, knee bent, right foot lifting behind, body slightly lower.
3) PASSING: standing on the left leg, the right leg bent and passing right next to it, feet close together under the body, right arm by her side, body slightly higher.
4) CONTACT: the mirror of frame 1 — right leg forward heel touching, left leg back on its toes, right arm swung back.
5) DOWN: the mirror of frame 2 — right foot flat taking the weight, left foot lifting behind, body slightly lower.
6) PASSING: the mirror of frame 3 — standing on the right leg, the left leg passing next to it, feet close together, body slightly higher.
```
