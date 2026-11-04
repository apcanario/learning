**Findings**

1. **Should-fix: at 320 px, Information architecture's unit tiles are wider than their grid.** File: `data-extract.json`, runs "ux-ia 320px dark reduced" and "ux-ia 320px light reduced".
   - Every one of the 15 tiles measures `w` 299. The grid reports half 138, so the grid itself is 288 (2 × 138 + the 12 px gap). The column has grown 11 px past the grid's right edge.
   - Every other page fills its grid exactly at 320: Greece, Rome, brand-a and brand-b are 288 in a 288 grid, and the home is 264 in 264. At 360 the IA tiles fit (328 in 328), as they do at 390, 430, 768 and 1280.
   - Likely cause, from `theme-excerpt.css`: `.course.live .cname{white-space:nowrap}` keeps the whole chip on one line. The longest chip, "INFORMATION ARCHITECTURE · DD-IA1/2/3", is 33 monospace characters at 11 px with .1em spacing, about 254 px, plus 16 px of padding: about 270 px. The tile's content box at 320 is about 273 px. A `1fr` grid column (minmax(auto, 1fr)) will not shrink below that, so the whole column widens.
   - Effect: the right gutter drops to about 5 px against 16 on the left. The page does not scroll sideways (scroll 320 = 320), and nothing inside a tile is cut (`bad` is empty).
   - The extract's own checks miss this. "bad" tests parts against the tile's edge, not the tile against its grid.
   - Fix options: let the chip break between its two `.cpart`s below about 340 px, or give the grid `minmax(0,1fr)` / the tile `min-width:0` so the chip has to wrap.

No other error or should-fix found.

**Confirmed**

- **Same classes and fields everywhere.** All 948 tiles in 84 runs have the class set "course live". Modifiers are only ghost and pending.
  - Children by kind: a linked tile has ctop, ctitle, p, cstats, topo-patch. A history unit (disclosure) adds svg.chev. A ghost has no cstats.
  - Every patch is 4:1 and sits inside its tile (`pin` true in all 948). None is past the tile's edge (`sw` false in all 948). `unseen` is empty in all 948.
- **Patches match their sources.** Rises are one per written part, with the source's word count:
  - Greece U0 is 2789/3049/2775 and U9 includes 9.4 at 8088. U10's 12 modules match.
  - B3 is 1217/600/522/835/496/6923, summing to the stat 10,593.
  - IA1–IA7 section words match.
  - On the home, the course tiles' rises are their units' words. Information architecture adds 8 planned rings (IA8–DD-IA3).
  - Unwritten units are flat: Greece U13 has 5 planned, Rome U14 has 6, IA8–DD-IA3 one ring each.
  - Spot rings appear only on the small markdown sections, e.g. B3 §1–§5, B7 §2–6 and §9, DD-B2 §8, IA2 §3, §4 and §7.
- **History tiles open to their rows.** The row count equals the number of module ids for every tile: U0 3, U2 6, U10 12, Greece U13 5, Rome U14 6.
  - In the shots, Greece U0 and U1 and Rome U0 and U1 are open. The 768 light Greece shot shows rows 0.1–0.3 and 1.1–1.3.
  - Opened tiles show their line whole (3 to 6 lines, not cut). Closed ones stop at 2 lines.
- **Markdown tiles link correctly.** Written units go to their reading pages (`#read-b1` … `#read-dd-b3`, `#read-a1` …, `#read-ia1`–`#read-ia7`). Unwritten IA8–DD-IA3 are marked pending, show stats of 0, and go to their briefs (`#ux-ia-b-ia8` …). The IA8 pill is "next"; the rest are "soon".
- **Ghost tiles.** All 8 planned courses, in the source order, have:
  - the chip (e.g. "History · Egypt");
  - the title;
  - the line at 2 lines;
  - no stats and no pill;
  - one dashed ring (`plan`), on a dashed tile outline;
  - a chip outlined in its tone, with text in the body colour (contrast 15.01 light, 15.75 dark).
- **Columns.** One column at 320, 360, 390 and 430 px; two columns at 768 and 1280 px, in every grid.
  - Lone tiles are half the grid: at 768/1280 the home is 342 = half 342 and Greece/Rome 358 = half 358.
  - At 768 the planned grid's ghosts are 325 each in two columns.
- **Nothing cut, no sideways scroll.** Scroll width equals the viewport in all 84 runs, and `bad` is empty in all 84. The one exception is the grid overrun in finding 1.
- **Light theme.**
  - Tokens: paper #e8e4dc, card #f0ede6, no white anywhere. The light run's patch strokes are the light accents (#bd0000, #7400fe, #0062a0, #006b5e, #9c4500, #7c5800).
  - `contrast.txt`: every P93 tile pair passes. Lowest small-text pair is the dark "pill next" at 5.71. Light chips are 5.75–5.94, plain pills 8.02 on a card, and the light tile line and labels 8.02.
  - The 768 light Greece shot shows cream paper and cards with no white surface.
- **Hours.** The home shows Personal brand 4.8 and Building with AI 5.3, as the givens say.

**Renderer notes**

- The phone images (640 × 7000) reach me shrunk to 183 px wide, and the tablet images to 439 px. At that size I cannot see an 11 px overrun or a 1–2 px spot ring. Finding 1 rests on the measured numbers, not on the image.
- A spot ring is r 4–5 in a 720-unit viewBox, so about 1.5–1.8 px radius on a 263 px phone patch. It barely shows in the shrunk images, so I cannot judge from them how visible it is at real size.
- I opened only a sample of the images: 320 ux-ia and brand-b dark, 768 Greece light and 768 home dark. The other pages and widths are checked from the data only.

**FIX**: finding 1 stands as a should-fix.