**Findings**

1. **Should-fix: on phones and the tablet, User Experience has no peak of its own** (`hero-markup.html`, tall SVG, group `ct-t4`; shots 320–768 px).
   - In the tall layout (below 1100 px), the User Experience group has four stretches of line and none of them closes into a ring: `M700 771…`, `M695 736…`, `M685 697…` and `M700 673…` (a 30-unit fragment). Every one of them is a piece of a ring that also goes round History.
   - Marketing and Technology each have a top that closes in the same layout. Marketing has `M330 144…z` and `M330 173…z`; Technology has `M635 159…z` and `M645 184…z`.
   - In the shots, User Experience therefore shows only as a blue edge on History's outer rings at the lower right. You can see it at 390 and 430 light (x ≈ 640–830 image px, y ≈ 900–1170) and at 768. It does not read as a rise.
   - The data gives User Experience 3 levels (66,866 words), the same as Marketing (74,284) and Technology (82,023). On the phone it reads as History's shoulder, not as one of four areas.
   - The merge the brief accepts is on the desktop only, and there User Experience still keeps two closed rings of its own (`M735 329…z`, `M750 368…z`; visible at 1010–1135, 395–535 in the 1280 shots).
   - Fix: move the User Experience rise in the tall layout far enough from History that its top two rings close, keeping it inside a 390 px view. Then re-run `verify.py`.

2. **Minor: on the desktop, Marketing's outer line touches the sidebar at the end of the drift** (`1280px-first-screen-*.png`, `1280px-hero-motion-*.png` moment 5).
   - At rest, the leftmost teal line sits about 8 px from the sidebar border (x ≈ 308).
   - The drift moves the layer 8 px left (`topo-drift`, −8 px, 6 px), so at 30 s the line reaches the border. The sheet shows it about 3–4 px from the edge.
   - Nothing is cut, but "clear of the sidebar" holds only at the start of the sweep. Moving the rise about 10 viewBox units right in the wide layout would settle it.

3. **Minor: the hero's padding rule has a dead value** (`theme-excerpt.css` l.37–38).
   - `.panel.root>.hero.hhome` sets `padding:0 calc(...) 24px` and then overrides the bottom with `padding-bottom:clamp(28px,9svh,96px)`, so the `24px` never applies.
   - Writing the shorthand once would be cleaner.

4. **Minor: the static line's separator dots may be read aloud** (`hero-markup.html` l.5).
   - The static line's separators (`<span class="harea-dot">&nbsp;· </span>`) are announced as "dot" or "middle dot" by some screen readers at higher punctuation settings. Other readers will then hear "History dot Marketing dot…".
   - Making the dot `aria-hidden` and putting a visually hidden comma in its place would keep the pause without voicing the glyph. Hiding the span as it stands would also hide the spaces, so the words could run together.

**Confirmed**

- **Each area's words, sources against built.** The course units add up exactly to the area totals:
  - Greece 246,589 + Rome 263,904 = 510,493 (History)
  - brand-a = 74,284 (Marketing)
  - brand-b = 82,023 (Technology)
  - ux-ia IA1–IA7 = 66,866 (User Experience)
- **Levels.** One contour every 22,000 words, rounded down, gives History 23 and the other three areas 3 each. `layouts` matches this for both tall and wide at every width and theme, and so do the `data-words` and `data-rings` attributes in the markup.
- **Ring counts in the markup.**
  - Tall History: 19 closed rings plus 4 lowest rings drawn as stretches, 23 in all.
  - Wide History and wide Marketing, Technology and User Experience: 3 levels each, each including stretches shared with History. This is consistent with the rule that a stretch of line takes the colour of the rise that dominates it there.
- **Rise colours.** Each rise's stroke equals its area's tone in both themes. Dark: red ff6b6b, teal 2a9d8f, purple 9b5de5, blue 457b9d. Light: red bd0000, teal 006b5e, purple 7400fe, blue 0062a0.
- **Cycling line.**
  - Order is History, Marketing, Technology, User Experience (`--k` 0–3), each word in its tone, one at a time every 3 s by CSS alone, with a 3% cross-fade. The motion sheets show History, Marketing, Technology, User Experience, History at 0, 3, 6, 9 and 12 s, at 390 and 1280, in both themes.
  - The line has `aria-hidden`, no link and no focus stop.
  - The static line is visually hidden but readable by a screen reader when motion is allowed. It shows under reduced motion: `staticShown` is true and `lineShown` is false in every reduced-motion state, and the reverse in every motion-allowed state.
  - Its text is "History · Marketing · Technology · User Experience", each name in its tone and the dots muted.
- **Lede.** Reads as specified at every width.
- **What's new link.**
  - Text is "What's new · IA7 · 3 Nov", which matches the newest unit (IA7, 2026-11-03).
  - It goes to `#new`, is 44 px tall, has a transparent background and a 1 px solid border, and is set in mono at 12.5 px. It is outlined, not filled, in every shot.
- **Contour layer.**
  - Marked `aria-hidden`, with no text in it (paths only).
  - `topoBytes` is 13,884, under 20 KB.
  - The fade covers the last 16% (mask at 84%).
  - One layout shows at a time: tall from 320 to 768 px, wide at 1280 px.
- **Legibility.** Every measured text is at or above what it needs, at every width, in both themes, with motion allowed and reduced. The lowest values:
  - Dark area words: 3.20 at 430 px with reduced motion (User Experience); 3.24 on the tablet; 3.31 elsewhere. Each needs 3.
  - Light: 3.51 for Marketing. Needs 3.
  - Lede, light: 4.82 at 320 and 360 px. Needs 4.5.
  - Link: 9.57 or more. Arrow: 5.56 or more.
  - The shots agree: every text reads cleanly over the History rings in both themes.
- **Height and the peek.**
  - The hero is 70% of the screen at every width: 448 of 640, 546 of 780, 591 of 844, 652 of 932, 717 of 1024 and 560 of 800.
  - The first area heading's top is inside the viewport each time: 568, 666, 711, 772, 858 and 701. The History heading shows at the foot of every phone and tablet shot.
- **Sideways scroll and edges.**
  - Page scroll width equals the viewport at 320, 360, 390, 430, 768 and 1280.
  - Nothing is cut: the static line wraps to 3 lines at 320 to 390 px and 2 at 430, and the lede wraps cleanly.
- **Desktop.** The contour layer runs from 300 to 1280 (full width beside the sidebar). The copy runs from 426 to 1154 inside the 410–1170 column.
- **Motion.**
  - With motion allowed there are five animations: the drift, which animates transform only, and four word animations, which animate opacity and transform. None is on a tile.
  - The drift is 8 × 6 px over 30 s, alternating, on a layer drawn 12 px larger on every side, so no edge ever shows.
  - With reduced motion there are no animations.
- **Overall.** The hero is quiet, type first and current. The action is visible without scrolling. Motion sits beside the headline in the cycling word, and the drift behind it is barely perceptible.

**Renderer notes**

- The contrast measures were taken only at the two ends of the drift (0 and 30 s). In between, two lines can pass closer than a pixel. The pixel measures already fall below `contrast.py`'s single-line value: the light lede is 4.82 against the model's 5.12, and the dark static User Experience at 430 px is 3.20 against 3.31. So the token model is not a lower bound. The margins left are 0.32 and 0.20.
- LCP (112 ms) and longest task (0 ms) come from a fresh load from a local server, with no CPU or network throttling. They do not show phone-class INP or LCP.
- The phone motion sheets are clipped to the hero's own box, so the 22 px strip of contours under the top bar is visible only in the first-screen shots.
- At 1280 px the shots are at scale 1, and the 1280 motion sheets were displayed at about 0.68, so the closeness to the sidebar in finding 2 is estimated from pixels, not measured.
- Dark-theme faintness of the teal, purple and blue lines was seen as described in the brief and is not reported.

**FIX**
