**Findings**

1. **Should-fix: a markdown unit's patch can show far fewer islands than it has sections.** This rests on `shots/desktop-brand-b-tiles-light-part1.png` and `shots/phone430-brand-b-tiles-light-part1.png`, read against `data-extract.json` (brand-b runs and `sources.courses.brand-b.tiles`).
   - **B3 · Prompting that holds up:** the data lists 6 rises (§1 1217, §2 600, §3 522, §4 835, §5 496, §6 6923 words). The tile paints one island, §6, at both 430 and 1280 px. The 1280 shot is almost 1:1, so this is not a downscaling loss. On the same page, B1's sections of about 440 to 590 words draw visible islands.
   - **B4:** 6 sections; only 2 islands show (the 4173-word §6 and one speck).
   - **B7:** 10 sections; about 4 show, two of them single-pixel dots.
   - **DD-B3 and DD-A2:** their smaller sections are dots.
   - **Greece U9:** 4 modules, one of them 8088 words. The tablet and desktop shots show about 3 islands. This one is less certain, because those images were downscaled for me.
   - **Cause (inferred):** island size is scaled to the unit's own largest part, so a section under roughly a quarter of the largest one falls below the first ring and draws nothing.
   - **Why it matters:** check 1 asks for one visible rise per written part. The `<g>` elements exist (the data counts them), but the reader cannot see them. The given that "a unit of few parts draws smaller islands" covers smaller islands, not missing ones.
   - **Fix:** give every written part at least one visible ring, for example a floor radius.
2. **Minor: the data's class set leaves out the modifier classes.** This rests on `data-extract.json` against `tile-markup.html`. All 948 tile records give `cls` as "course live", but the built markup carries `course live ghost` and `course live pending`, and the shots show both styles (dashed ghosts; dashed rules on IA8 to DD-IA3 and on the Quality audit units). The page is right; the extract's `cls` field reads only the base classes, so it cannot prove that the ghost and pending classes are present on every tile.

**Confirmed**

- **Same fields, same classes:**
  - All 948 tile records across 84 runs (6 pages, 6 widths, 2 themes) share the base class "course live".
  - Child sets come in three shapes:
    - link: ctop, ctitle, p, cstats, topo-patch (504 records)
    - disclosure: the same plus chev (348)
    - ghost: ctop, ctitle, p, topo-patch, chev, with no cstats (96)
  - Every patch has `aria-hidden` true and `pin` true (inside its tile); none has `sw` true.
  - `bad` is [] in all 84 runs.
- **Patches match their sources:**
  - Greece's 13 units and Rome's 14 match the source word counts exactly; their rises sum to the units' words (e.g. Greece U0: 2789+3049+2775 = 8613; Rome U10 = 21214).
  - Markdown sections sum to the unit: IA1 to 5412, A1 to 5280, B3 to 10593.
  - Planned parts are flat rings only: Greece U13 (5), Rome U14 (6), IA8 to DD-IA3 (one each), and the home's IA course (7 rises plus 8 plan rings).
- **Stats against sources:**
  - Course totals equal the area totals: Greece's day total 221673 is U0 to U11; brand-a 72380, brand-b 80140, IA 65537.
  - Hours at about 15,000 words an hour match: 4.8, 5.3 and 4.4 for the three markdown courses; Greece U0 0.6, U9 1.1, IA1 0.4. Personal brand's 4.8 and Building with AI's 5.3 agree with the stated word recount.
- **History units open to their rows:**
  - Rows equal module ids: U0 m01 to m03 gives 3 rows; U10 has 12 mods and 12 rows; U13 5/5; Rome U14 6/6.
  - In the shots, Greece and Rome units 0 and 1 are open with their rows (0.1 to 0.3, 1.1 to 1.3, 1.1 to 1.6) and their whole line (3 to 6 lines, never clipped).
  - Opened tiles keep their own heights side by side, at 768 and 1280.
- **Markdown units link correctly:** each href equals its reading page (#read-a1 … #read-dd-b3, #read-ia1 … #read-ia7). Unwritten IA8 to DD-IA3 link to their briefs (#ux-ia-b-ia8 … #ux-ia-b-dd-ia3), with stats 0/0/0.0 and one dashed ring.
- **Ghost tiles:**
  - 96 records (8 per run, 12 home runs).
  - Each has its chip (History · Egypt … Japan), no pill, empty stats, 2 lines clipped and a single dashed ring.
  - The shots show the dashed outline, the outlined chip and the dashed top rule in its tone.
- **Columns:**
  - All 120 phone grids (320 to 430 px) have 1 column.
  - At 768 and 1280 px every grid has 2 columns.
  - Lone tiles equal half the grid: 342 = 342 on the home, 358 = 358 on Greece and Rome.
- **Edges:**
  - Scroll width equals page width in all 84 runs.
  - No part runs past a tile's edge, and every patch is pinned inside its tile.
  - The only width notes in verify are the hero contours below 390 px, which the row sets, not the tiles.
  - `verify-lines.txt` reports no FAIL line.
- **Light theme:**
  - Tokens are paper #e8e4dc, card #f0ede6, ink #1b1915, with no white.
  - Light runs carry the light accents (e.g. stroke #bd0000).
  - `contrast.txt` reports every P93 pair passing, and the shots show the warm paper with cream tiles.

**Renderer notes**

- **Images shown downscaled:** phone and tablet parts reached me at 183 to 439 px wide from originals of up to 7000 px tall, so specks under a few CSS pixels may be lost. Finding 1 rests on the 1280 px shot, shown almost 1:1.
- **Shots sampled, not all read:** of about 180 shots I read 10. Desktop: home, Greece, Building with AI (light), IA (dark). Tablet: Greece dark, Personal brand light. Phones: 390 home dark, 320 Rome light, 320 IA dark, 430 Building with AI light. For the rest I relied on `data-extract.json`.
- **No class proof for modifiers:** the extract has no per-tile record of the ghost and pending modifier classes (see finding 2).

**FIX**

FIX, because finding 1 (should-fix) stands.