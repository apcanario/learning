**Findings**

1. **should-fix** (verify-hero-lines.txt, contrast-tokens.txt, theme-excerpt.css). With motion allowed, the contrast is only shown at two widths and one moment. `verify-hero-lines.txt` measures the moving state at 390 px ("home phone motion") and 1280 px only. The cycling line at 320, 360, 430 and 768 px is never measured while it moves. In that state each word sits alone at the left of the grid, not where it sits in the static line that the reduced-motion runs measured. No line says which drift moment was measured, and the drift moves the whole layer by up to 8 × 6 px (`topo-drift`).
   - The static runs show that overlapping lines go below `contrast.py`'s "lowest over a line" figure, so the token check is not a floor:
     - 768 dark, "User Experience": 3.14, against the token figure of 3.18.
     - 768 light, "User Experience": 3.41, against 3.52.
     - 360 light, lede: 4.76, against 5.12.
   - The 768 dark margin is 0.14 above the 3:1 it needs. A translate can carry one of those close line pairs under a word that verify never measured in that position.
   - Fix: measure the moving state at every width, at both drift extremes (or the five sheet moments), with each area word shown in turn. Print the drift moment in each line.
2. **minor** (hero-markup.html: the UX paths at y 750–880 of 1000 in the tall layout and 410–530 of 571 in the wide one; theme-excerpt.css `.topo` mask `#000 72%`). In both layouts the User Experience rise sits wholly in the band where the mask fades the lines out. On top of the given low opacity, its lines read as grey rather than blue in both themes.
   - 390 and 768 shots: the bottom-right rings are pale grey-blue in light and near-invisible in dark.
   - Of the four rises, this is the one whose tone is hardest to identify.
   - Moving that rise above the fade band, within the fixed layout, would fix it.
3. **minor** (1280px-first-screen-*.png; the wide Marketing path at x 18–162). At 1280 px the Marketing rise is clipped at the sidebar edge (x = 300): its outer ring and part of the second are cut. On phones its outer ring and Technology's run off the left and right screen edges (390 and 430 shots). This is acceptable for a background, but on the desktop Marketing reads as the weakest "one rise per area".

**Confirmed**

- **Rises traced to the data.** The source sums check out:
  - History: Greece 246,589 + Rome 263,904 = 510,493.
  - Marketing: brand-a = 74,284.
  - Technology: brand-b = 82,023.
  - User Experience: IA1–IA7 = 66,866.

  These match `built.layouts` for both `tall` and `wide`, and the `data-words` attributes in the markup. Levels are floor(words / 22,000): 23, 3, 3, 3. I counted the rings in the markup for each layout:
  - Tall, History: 21 closed rings plus 2 rings split into stretches, 23 in all.
  - Wide, History: 22 closed plus 1 split, 23.
  - Marketing, Technology and User Experience: 3 each in both layouts.
  - Shared stretches: the lowest rings are split into stretches across the History, Marketing and User Experience groups, so they change colour along their length.

  Each rise's stroke colour equals its area's tone in both themes. `topoBytes` is 14,042 (under 20 KB). The layer is `aria-hidden`, holds no text, and its SVGs are `focusable="false"`. Rise positions are the same at every width within each layout.
- **Cycling line.** It runs History, Marketing, Technology, User Experience, in red, teal, purple, blue. The computed colours are the theme's tones in both themes, and Rome and course B share purple.
  - Pure CSS: a 12 s cycle with delays of k × 3 s − 0.4 s, cross-fading over 3% of the cycle.
  - The sheets show exactly one word at each of 0, 3, 6, 9 and 12 s, at 390 and 1280 px in both themes; 12 s returns to History.
  - The line is `aria-hidden`, has no link and no focus stop.
- **Static line.** It is "History · Marketing · Technology · User Experience" and is not `aria-hidden`.
  - Under reduced motion it shows and the cycling line does not (`staticShown` true, `lineShown` false), and `anims` is empty at every width.
  - With motion allowed it is visually hidden but still read by a screen reader.
- **Lede.** It matches the agreed text exactly.
- **Link.** It reads "What's new · IA7 · 3 Nov", goes to `#new`, and opens in the same tab (`new` in the data is `data-target`).
  - It is 44 px tall at every width, with a transparent background and a 1 px solid border.
  - It is in the mono face at 12.5 px with text weight, not a filled button. Its arrow is `aria-hidden`.
  - IA7 on 2026-11-03 is the newest unit in the sources.
- **Contrast.** Every measured text clears what it needs at every width and theme under reduced motion, and at 390 and 1280 px with motion allowed. The lowest figures:
  - Dark area word: 3.14, needs 3.
  - Light area word: 3.41, needs 3.
  - Lede: 4.76, needs 4.5.
  - Link: 10.75, needs 4.5.

  In every shot the words read clearly over the densest History rings.
- **Height and peek.** `heroH` is 70% at all six widths (448/640, 546/780, 591/844, 652/932, 717/1024, 560/800). The first area heading's top sits at 568, 666, 711, 772, 858 and 701 px, inside the viewport in every case, and "History" is visibly peeking in every first-screen shot.
- **No sideways scroll.** Scroll width equals the viewport width at all six widths, 320 and 360 px included. Nothing is cut and nothing runs off an edge in any shot. At 320 px the static line wraps to three balanced lines and the link fits.
- **Desktop.** At 1280 px the layer runs from 300 to 1280 px and the copy from 426 to 1154 px, inside the 410–1170 px column. The wide layout shows from 1100 px and the tall one below it (768 px reads `tall`).
- **Motion.**
  - Only transform and opacity animate: the drift is transform only, the words opacity and transform.
  - Nothing animates on a tile.
  - The drift is 8 × 6 px, alternating, over 30 s, inside a 12 px overscan, so no edge ever shows.
  - LCP is 104 ms with no long tasks.
- **Overall.** The hero is type first, the action is in view on every first screen, and the motion sits beside the headline. It reads as quiet, current and well made beside the 2026 patterns.

**Renderer notes**

- The motion sheets were displayed at about one third of full size (390 px) and two thirds (1280 px). I could confirm which word shows at each moment, but could not judge sub-pixel line overlaps or measure the drift offset by eye.
- The 768 px shots were downscaled slightly for display.
- `data-extract.json` (18,480 lines) was read in part: the 320 px entries in full, and for every other width and mode the words, tones, static line, link, layouts, `topoBox`, `heroH`, `first`, `scroll` and `layout` fields by search and offset. Tile and card fields were not read beyond 360 px.
- `verify-hero-lines.txt` labels "home phone" and "home phone motion" without a width; from the brief I take them to be 390 px.
- The LCP figure comes from a local server with no CPU or network throttling, so it is not representative of a phone. The hero itself carries no script.

**FIX**
