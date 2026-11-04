P93 tile check (tiles-4): report

I used only Read, Glob and Grep, and only inside the tiles-4 folder.

## Findings

1. **minor: "modules written" breaks onto two lines on every history unit tile.** Files: `shots/desktop-greece-tiles-dark-part1.png`, `shots/tablet-greece-tiles-dark-part1.png` and `shots/phone320-greece-tiles-light-part1.png` (every Greece and Rome unit tile); `theme-excerpt.css` line 126.
   - The stats sit in `repeat(3,minmax(0,1fr))`. The first label wraps to "modules / written" while the third column has spare width. This happens at every width, including the 358 px half-width tile at 768 and 1280.
   - Nothing is cut and stats stay level across a row, so this is a looks issue only.
   - Suggested fix: size the columns to their content, for example `grid-template-columns:repeat(3,auto);justify-content:space-between`. Or give the first column more room (`1.3fr 1fr 1fr`).

2. **minor: a theme comment does not match its rule.** File: `theme-excerpt.css` line 228.
   - The comment says "while a unit tile is open **its row's** tiles take their own heights". The rule `.cgrid:has(>details.course.live[open]){align-items:start}` acts on the whole grid. The README says "the tiles of its grid".
   - With today's grids (2, 3, 3, 2, 3, 1 tiles) this changes nothing you can see.
   - Suggested fix: change the comment to say "its grid's tiles".

3. **minor, outside the tiles but in this folder: `contrast.txt` says PASS while printing figures under 4.5:1 for small text.** File: `contrast.txt` lines 35–101.
   - The P93 hero pairs "over two stacked" lines include:
     - dark crumb, eyebrow, lede and flag (muted): 3.60
     - dark eyebrow course label, blue: 3.09
     - dark eyebrow course label, purple: 3.26
     - light eyebrow course label, gold: 3.75
     - light muted texts: 4.28
   - The file still ends "P93: ALL NEW PAIRS PASS".
   - These are worst cases worked out from the tokens. The theme says `verify.py` measures the built page at five poses, but I could not see that output.
   - Suggested fix: either label the two-stacked column as a worst-case record that is not a pass criterion, or show the built-page measurement that it never occurs under small text. Whoever checks the course-home heroes should settle this; it does not touch the tiles.

No error and no should-fix.

## Confirmed

**Sources (`data-extract.json` → `sources`)**
- Every unit's module or section words add up to its total:
  - Greece U0–U12 and Rome U0–U13, module by module.
  - A1–DD-A2, B1–DD-B3 and IA1–IA7, section by section.
- Area totals match: History 510,493 (Greece 246,589 + Rome 263,904), Marketing 72,380, Technology 80,140, User Experience 65,537.
- Hours match at 15,000 words per hour, rounded:
  - Courses: 16.4, 17.6, 4.8, 5.3, 4.4.
  - Every unit tile I computed (all Greece, Rome U0/U1/U13, all A, all IA, B1, B3).
  - Personal brand 4.8 and Building with AI 5.3 match the README's "about 3% lower" note.

**1. Same fields, same classes, patch matches sources**
- All 948 tiles across the 72 tile runs have class `course live`. The only extras are the `ghost` and `pending` modifiers.
- Their children come in exactly three shapes:
  - link: 504 tiles
  - disclosure (adds `svg.chev`): 348 tiles
  - ghost (no `cstats`): 96 tiles
- Those counts match 12 runs × (42 links, 29 disclosures, 8 ghosts).
- Each tile's `rises` matches its sources, one rise per written part with its words. Planned parts sit in `plan`:
  - Greece U13 and Rome U14 (the Quality audits, not run yet): 5 and 6 flat rings.
  - IA8–DD-IA3: one ring each.
  - The home IA tile: 8 planned rings.
- `unseen` is empty everywhere.
- `spots` mark exactly the parts under one contour level (largest part ÷ 5.5) and no others: A6 §4; DD-A2 §1 (406 < 409); B3 §1–5; B4 §2–5; B5 §1, §6; B7 §2–6, §9; DD-B2 §8; DD-B3 §3, §5; IA2 §3, §4, §7; IA7 §8, §9. That is 10 tiles per run, 120 in all.
- Ring counts in `tile-markup.html` match the same interval (IA1: 5/3/1/1/2/1/1; Greece U0: 5/5/5).
- Every patch is 4:1 (263×66, 239×60, 205×51, 309×77), sits inside its tile (`pin` true, `sw` false) and is `aria-hidden`.
- Tones follow the theme: all 474 dark-theme tiles use the dark palette and all 474 light-theme tiles use the light palette.

**2. History tiles open to their rows**
- 48 opened tiles: Greece U0/U1 and Rome U0/U1 × 12 runs.
- Opened tiles report `clipped` false with the line shown whole (3–6 lines). `rows` equals the module ids and the rises (3, 3, 3, 6).
- The shots show the 0.1–0.3 and 1.1–1.3 rows under the patch at phone, tablet and desktop. An opened tile stays in its column and its neighbour does not stretch.
- Every closed tile shows exactly 2 lines; no closed tile reports any other count.

**3. Markdown tiles link to their reading pages or briefs**
- A1–DD-A2 go to `#read-a1` … `#read-dd-a2`, and IA1–IA7 to `#read-ia1` … `#read-ia7`. B3 goes to `#read-b3` (markup).
- Unwritten IA8–DD-IA3 are `pending`, show 0/0/0.0, have one dashed ring and link to `#ux-ia-b-ia8` … `#ux-ia-b-dd-ia3`.
- The pending rule is dashed (`phone320-ux-ia-tiles-dark-part5.png`).

**4. Ghost tiles**
- All 8 planned courses appear in order. Each has the outlined chip "History · Egypt" … "Japan", the title, its scope clamped to 2 lines, no stats, no pill and one dashed ring. Each opens and has no link.
- The dashed outline and the dashed top rule in its tone show in both themes.
- The CSS specificity of `.course.live.ghost .cname` beats the solid Swiss-pass chip.

**5. Columns**
- Every grid is 1 column at 320, 360, 390 and 430, and 2 columns at 768 and 1280.
- A lone tile is exactly half: home 342 of 342, course homes 358 of 358 (desktop and tablet shots).
- Side by side, stats and patches sit level, with the slack above the stats (Greece U2/U3 and B-unit rows in the shots).

**6. Nothing cut, no sideways scroll**
- Scroll width equals page width in all 84 runs.
- `bad` is empty in all of them.
- At 320 the chip breaks only between its two parts ("Information architecture · / DD-IA2"), without widening the tile.

**7. Light paper**
- Page #e8e4dc and card #f0ede6. The tokens contain no white.
- Chips on accents are 5.75–5.94:1. Toned pills on the card are 7.02–7.09:1 in light and 5.71–12.00:1 in dark. The plain pill is 8.02 (light) and 6.66 (dark); the ghost chip 15.01/15.75; the tile line 8.02/6.66. All are at least 4.5:1.

## Renderer notes

- Images arrived downscaled: phone 640→533 px wide, tablet 1536→1280, desktop 1280→1067 for 2,400 px parts. Fine strokes (spots, dashed rings) are judged at reduced size.
- I viewed a sample, not every image: desktop home dark and light, desktop Greece dark, desktop Rome light part 3, tablet Greece dark, tablet brand-b light, phone 320 home dark part 2, phone 320 Greece light part 1, and phone 320 ux-ia dark parts 1 and 5. For the rest I relied on the data extract.
- No shot shows a ghost opened, so the spine view rests on `tile-markup.html` only.
- The shots are taken under reduced motion only; ring clearance during the move rests on `pin` as reported.

PASS