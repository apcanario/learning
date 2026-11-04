**Check of the Academy home hero (P92, fourth pass)**

Sources: only the files in /home/claude/p92check/hero-4/. I looked at all 12 first-screen shots, all four parts of the 390 px motion sheets and both 1280 px motion sheets. I read hero-markup.html, theme-excerpt.css, contrast-tokens.txt and verify-hero-lines.txt in full. I read data-extract.json through targeted reads and searches across all 24 width, theme and motion keys.

## Findings

None is an error or a should-fix.

1. **minor**: the link's accessible name contains two middle dots, so a screen reader may say them aloud (hero-markup.html line 7). The name is "What's new · IA7 · 3 Nov" (the "→" is correctly aria-hidden). Some screen readers at higher punctuation levels read "·" aloud. The static line was deliberately changed so its dots are never spoken (`.harea-sr` commas), but the link was not. Wrapping each dot in `aria-hidden` with a screen-reader-only comma, as the static line does, would make the two consistent.
2. **minor**: at phone widths a contour line runs through the outlined link (shots 320px, 360px and 390px, both themes). The link's background is transparent, so a line crosses inside its box just left of or through the "→". The lede line "place. Pick up" is crossed too. Every measure passes: the arrow's lowest is 5.09:1 and the lede's lowest is 5.04:1 (verify-hero-lines.txt). It is cosmetic only.
3. **minor**: some row labels in verify-hero-lines.txt don't give their width. "home phone", "home tablet" and "home desktop" are presumably 390, 768 and 1280 px, while the other rows say phone320, phone360 and phone430. A reader has to infer which width each unlabelled row covers.
4. **minor (cosmetic)**: under reduced motion at 320 to 390 px the static line wraps to three lines, leaving "Technology ·" alone on the middle line (shots 320px, 360px and 390px). It reads fine and stays inside the column; at 430 px and up it is two lines or one.

## Confirmed

**Rises traced to the data**
- Area words are summed from the course units in `sources`. History is Greece 246,589 + Rome 263,904 = 510,493. Marketing is course A, 74,284. Technology is course B, 82,023. User Experience is IA1 to IA7, 66,866; the planned IA units with no word count are left out.
- At one contour per 22,000 words, levels are 23, 3, 3 and 3. The markup's `data-rings` and `layouts` (both layouts, every key) agree.
- I counted closed rings in the markup:
  - Tall layout: History 22, Marketing 2, Technology 2, User Experience 2, plus the open stretches of the shared lowest ring.
  - Wide layout: 22, 2, 3 (Technology's lowest ring stands on its own) and 2.
  - This matches the extract's fifth field and the rule that every small rise closes at least two rings of its own.
- Stroke colours equal the area tones in both themes.
- The lowest shared ring changes colour along its length: teal near Marketing, red near History, blue near User Experience (light shots at 320 to 430 px).

**Placement of the rises**
- Tall layout at 320 and 390 px: all four rises sit inside the visible width of the cropped square, and each small rise's own rings sit above the fade. User Experience's own rings end around unit 873, against the fade starting near 880. Only the shared lowest stretch reaches into the fade.
- Wide layout at 1280 px: Marketing's leftmost line lands at about x 331 (about 323 at full drift), clear of the 300 px sidebar. The shot agrees, at about 330. User Experience's own rings end around unit 442, above the fade starting near 505.

**The cycling line and the static line**
- The cycling line shows History, Marketing, Technology, User Experience in that order, each in its tone (dark: #ff6b6b, #2a9d8f, #9b5de5, #457b9d; light: #bd0000, #006b5e, #7400fe, #0062a0). Technology shares purple with Rome and course B, as designed.
- Each word holds 3 s of the 12 s cycle. Each fades out over 3% of the cycle while the next fades in, and the −.4 s offset puts one fully shown word at 0, 3, 6, 9 and 12 s. The motion sheets show exactly that in both themes.
- The cycling line is CSS only, aria-hidden, with no link or focus stop.
- The static line reads "History · Marketing · Technology · User Experience". Its dots are aria-hidden with screen-reader commas (`staticSr`).
- Under reduced motion the static line shows and the cycling line does not (`staticShown` true, `lineShown` false). With motion allowed the reverse holds, and the static line stays readable to a screen reader only.

**Lede and link**
- The lede is the text as it was.
- The link reads "What's new · IA7 · 3 Nov" and goes to `#new`, matching the newest unit, IA7 of 2026-11-03.
- It is 44 px tall, with a transparent background and a 1 px solid border: outlined, monospace, text weight, not a filled button.

**Legibility over the contours**
- Every text passes at every width and theme, in both reduced motion and with motion allowed, at drift 0, 15 and 30 s, with each word shown in turn.
- Area words need 3:1: the lowest are 3.31 (dark User Experience) and 3.47 (light Marketing, desktop).
- The lede needs 4.5:1: lowest 5.04 light, 5.47 dark.
- The link needs 4.5:1: text at least 9.57, arrow at least 5.09.
- The headline is at least 8.76.
- contrast-tokens.txt agrees with these at opacity .2 in both themes. The shots show nothing hard to read.

**Height and the first heading's peek**
- The hero is 70% of the screen at every width: 448/640, 546/780, 591/844, 652/932, 717/1024 and 560/800 px.
- The first area heading starts above the screen's bottom edge at every width (568, 666, 711, 772, 858 and 701 px). The History heading peeks in every shot.
- The copy sits in the lower part of the hero, with the contours above it.

**Width and layout**
- Page scroll width equals the viewport at all six widths, so nothing scrolls sideways at 320 or 360 px. Nothing is cut or off an edge in any shot.
- At 1280 px the contour layer runs from 300 to 1280 px beside the sidebar. The column runs 410 to 1170 px (760 px wide) with the copy at 426 to 1154 px.
- 768 px shows the tall layout and 1280 px shows the wide one. At 1100 px and up the area words are 34 px.

**Motion**
- With motion allowed, the only animations are the layer's drift (transform only) and the four words (opacity and transform). None is on a tile.
- The drift is 8 × 6 px over 30 s, alternating. The drawings are 12 px larger on every side, so no edge ever shows.
- Under reduced motion no animation runs (`anims` is empty in all twelve reduced-motion keys), so the background is still.

**The contour layer**
- It is aria-hidden, holds no text and is drawn at build time: 14,016 bytes, under 20 KB.
- The lines fade out over the hero's last 10% through a mask.
- LCP is 132 ms and the longest task is 0 ms, on a local server without throttling (the given caveat applies).

**Overall impression**
- The hero reads as the 2026 pattern asked for: type first, the action in view on the first screen, quiet motion beside the headline rather than behind it, and a still fallback for every animation.
- History's honest dominance gives the field a clear focal point. The light theme reads best; in the dark theme the smaller rises are faint (a given).
- The hero itself carries no totals. The counts in the 768 px and 1280 px track header ("2 courses · 157 reports · 8 planned") come from P91 and sit outside the hero.

## Renderer notes

- Phone and tablet shots are at scale 2 (the 768 px shot is 1536×2048 pixels); desktop shots are at scale 1. The motion sheets were shown to me downscaled (780×6000 shown at 260×2000, 980×2930 shown at 669×2000). I judged their colours and word order, not fine line detail. The part-2 images are only the bottom of moment 5.
- The motion sheets crop to the hero's own box. At 1280 px the outer Marketing ring reaches into the 22 px strip above the hero, which the sheets leave out. The first-screen shot shows it whole just under the top bar.
- Contrast was measured with each word fully shown. The 0.36 s cross-fades, when two words overlap at partial opacity, were not measured; that is not a WCAG requirement.
- Dark-theme lines at .2 are close to the limit of what a downscaled image shows. My judgement of whether the teal, purple and blue rises can be seen comes from the full-size first-screen shots.

**PASS**
