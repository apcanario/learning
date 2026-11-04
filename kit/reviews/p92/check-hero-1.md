**Check: the Academy home's hero (P92, 4 Nov 2026), hero-1**

**Findings**

1. **minor** (`shots/430px-first-screen-*.png`, `shots/768px-first-screen-*.png`, `theme-excerpt.css` line 13). The hero's text is centred vertically in a 70svh box, which leaves a lot of empty space above and below the text block on the larger screens.
   - At 430 px there is about 210 CSS px between the top bar and "Academy", and about 230 px between the link and the History band.
   - At 768 px the gaps are about 265 px and 285 px, and the text fills about 200 of the hero's 717 px.
   - The contours fill part of that space, and the 70% height is Pedro's decision. Aligning the text block to the top or bottom of the box (`justify-content`) would keep the 70% height and the peek while making the text feel less adrift.
2. **minor** (`theme-excerpt.css` line 32 and the `harea` keyframes). The comment says each word comes in "the next crossing as it goes". The timing does not cross:
   - History finishes fading out at 2.6 s, global time (22–25% of its cycle, delay −0.4 s).
   - Marketing only starts fading in at 2.6 s. For about 0.1 s around each handover both words are near zero opacity.
   - The sheets show no fault and the behaviour is acceptable, but the comment misdescribes it. Either fix the comment, or overlap the fades if a real cross-fade was meant.
3. **minor** (`verify-hero-lines.txt`). Each row prints only the lowest ratio across the 11 (or 8) texts, against no stated threshold.
   - The figure is 3.15–3.27, and the lowest text is always an area word, which only needs 3:1.
   - The pixel measure therefore does not show that the small texts (lede, link, arrow) clear 4.5:1.
   - `contrast-tokens.txt` does cover them in the worst case: lede and arrow 4.59 (light) and 5.26 (dark) with a full line directly under the glyph; link 8.59 / 12.42. So nothing fails.
   - The verify output should print each text's own lowest ratio and its threshold (3:1 or 4.5:1).
4. **minor** (`data-extract.json` `built`). Every `words`, `tones` and stroke colour is the dark-theme token (rgb(255,107,107), …). The extract carries no light-theme readout. I confirmed the light tones only from the shots and `contrast-tokens.txt` (#bd0000, #006b5e, #7400fe, #0062a0).
5. **minor** (`shots/*-dark.png`). In the dark theme, at --topo-a 0.22, the teal, purple and blue rises are barely visible. The purple one at 320 and 360 px is hardly visible at all. In dark, "each area's lines in its tone" reads as faint red plus near-invisible others. The light theme shows all four tones clearly. This is the cost of keeping the text contrast, so it is noted, not a fault.

**Confirmed**

- **Rises traced to the data, both layouts.**
  - Each course's units sum to its area's `sources` figure:
    - Greece 246,589 + Rome 263,904 = 510,493 (History)
    - brand-a = 74,284 (Marketing)
    - brand-b = 82,023 (Technology)
    - IA1–IA7 = 66,866 (User Experience)
  - Levels are floor(words / 22,000): 23, 3, 3, 3. These match the `built` `layouts` for tall and wide at every width, and the markup's `data-words` and `data-rings`.
  - I counted rings in the paths:
    - Tall layout: History has 21 closed rings plus 2 shared rings (open stretches M242/M715 and M380/M675) = 23. Marketing has 2 closed plus the outermost shared ring. User Experience has 1 closed plus the 2 shared rings. Technology has 3 closed.
    - Wide layout: History has 22 closed plus 1 shared ring = 23. Marketing has 2 closed plus 1 shared. User Experience has 2 closed plus 1 shared. Technology has 3 closed.
  - The shared rings change colour along their length: teal near Marketing, blue round the User Experience lobe, red elsewhere. This is visible in the light shots at every width. History dominates, as the brief says it should.
- **Stroke tones.** Each rise's stroke matches its area tone in both layouts (classes ct-t1, ct-t3, ct-t5, ct-t4).
- **The cycling line.**
  - Words and order are History, Marketing, Technology, User Experience (--k 0–3), each in its tone (computed colours equal `tones`).
  - It cycles one word at a time, 3 s each, on a 12 s cycle, by CSS alone.
  - The words are spans: no link, no focus stop. `p.harea` is aria-hidden.
  - The motion sheets (390 and 1280, dark and light) show History, Marketing, Technology, User Experience, then History again at 0, 3, 6, 9 and 12 s, each in its tone.
- **The static line.**
  - It reads "History · Marketing · Technology · User Experience", each name in its tone and the dots in muted. It has no aria attribute.
  - With reduced motion it is shown (`staticShown` true, `lineShown` false) and nothing runs (`anims` []).
  - With motion allowed it is visually hidden but kept for screen readers (clip-path inset(50%)), and the cycling line shows.
  - It appears correctly in all 12 first-screen shots.
- **The lede.** "Every self-study course in one place. Pick up where you left off." matches at every width.
- **The link.**
  - Text "What's new · IA7 · 3 Nov". The newest unit is IA7, 2026-11-03, so the text matches.
  - href `#new`, height 44 px, background transparent, 1 px solid border in --line-2, mono 12.5 px. It is an outlined link, not a filled button.
  - The arrow is aria-hidden.
- **The contour layer itself.**
  - aria-hidden and focusable=false. It holds paths only, no text.
  - 14,042 bytes, under 20 KB.
  - The lines fade out over the hero's lowest 28% (mask from 72%).
- **Legibility.**
  - Pixel-measured lowest ratios: 3.23 (dark) and 3.15 (light) at 320, 360, 390, 430, 768 and 1280 px; 3.27 and 3.17 at the desktop with motion. All are at least 3:1 for the 28 px and 34 px words.
  - The token worst cases agree: dark blue 3.18, light teal 3.15.
  - In the shots every text reads cleanly over the densest History rings in both themes, including at moments where the drift has moved the lines.
- **Height and peek.** The hero is 70% of the viewport at every width:

  | Width | Hero / viewport | First area heading top |
  |---|---|---|
  | 320 | 448 / 640 | 568 |
  | 360 | 546 / 780 | 666 |
  | 390 | 591 / 844 | 711 |
  | 430 | 652 / 932 | 772 |
  | 768 | 717 / 1024 | 858 |
  | 1280 | 560 / 800 | 701 |

  The History heading is fully visible at the bottom of every phone shot.
- **No sideways scroll.** `scroll` equals the width at 320, 360, 390, 430, 768 and 1280. Nothing is cut and nothing runs off an edge in the shots; only the background lobes run past the edge, as intended.
- **Desktop layout.**
  - At 1280 the contour layer spans 300–1280, the full width beside the 300 px sidebar.
  - The text sits at 426–1154 inside the 760 px column (410–1170), a 16 px gutter on each side.
  - The `wide` layout is shown at 1280, and `tall` at 768 and below.
- **Motion.**
  - The drift is `transform` only, 8 × 6 px over 30 s, alternating, on `.topo-l`. The drawing is 12 px larger on every side, so no edge shows during the drift.
  - The words animate `opacity` and `transform` only.
  - No animation runs on a tile, and course patches never move.
  - Nothing runs under reduced motion.
  - LCP is 180 ms with no long task (390 px, motion allowed).
- **Rest of the home.** The order is hero, then four areas, then rules, links, New since and links. There is no shelf and the hero carries no totals.
- **Overall.** The hero is type-first, with the action in view and quiet motion beside the headline. It reads as current and well made against the 2026 patterns.

**Renderer notes**

- Phone and tablet shots are at device scale 2, the desktop at scale 1, as the brief says.
- The motion sheets were displayed downscaled (390 px sheet at 1/3, 1280 px sheet at about 0.68). Tones and word identity were clear at that scale, but drift offsets of 6–8 px can only be judged approximately by eye.
- `390px-hero-motion-*-part2-of-2.png` holds only the tail of the fifth moment: the foot of the User Experience lobe under the fade.
- The grey label bands belong to the sheets, not the page.
- The strip of contours above the hero (`top:-22px`) is outside the motion sheets, as the brief says.
- `data-extract.json` is 6,606 lines. I read the reduced-motion and motion-allowed records in full for 320, 360 and 390, and the hero fields for 430, 768 and 1280, both modes.
- Desktop was tested only at 1280; no wider desktop was shot.

**PASS**
