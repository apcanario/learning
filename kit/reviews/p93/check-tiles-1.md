**Findings**

1. **Error: the two-line clamp breaks wherever two tiles share a row.** It happens from 768 px, closed tiles, both themes. When a tile's title is shorter than its neighbour's, the row stretches the tile, and its line (`flex:1 1 auto`, theme-excerpt.css §7, line 225) grows taller than two lines. The `overflow:hidden` then clips at that taller box, so a third line shows under the "…" that ends line 2. Examples in the shots:
   - `shots/tablet-greece-tiles-light-part1.png`: Unit 3 shows "…keep…" then "asking who told this story and what they got". Unit 8 shows "…festivals, oracles,…" then "mysteries. This unit is the practice behind".
   - `shots/desktop-brand-a-tiles-dark-part1.png`: A3 ("long-form per milestone, three posts a week"), A5 ("are not clickbait, editing in under 4 h."), A8 ("training partners and minors, time budget") and A9 ("each, share of followers who ever buy, the").
   - `shots/desktop-ux-ia-tiles-light-part1.png` and `shots/tablet-ux-ia-tiles-dark-part1.png`: IA3, IA6, IA9 and IA11.

   This breaks the row's "a two-line line" on every page with paired tiles. One-column phones are not affected. `data-extract.json` reports `"lines": 2, "clipped": true` for every one of these tiles, so its line measure misses this (see Renderer notes). A likely fix: set the clamp's own `max-height` (2 × line-height), or move the `flex:1` slack off the `p` and onto a spacer or the patch.

2. **Should-fix: the "soon" pill is not in the contrast record.** It sits on 7 pending IA tiles (IA9–IA12, DD-IA1–3), 84 instances across the runs.
   - `contrast.txt` measures only `pill live/prog/unck/next`.
   - The "soon" pill falls back to the base `.pill` colour, `var(--dim)` (theme-excerpt.css line 47), and the dark shot shows it grey (`shots/phone-ux-ia-tiles-dark-part1.png`).
   - From the tokens, dark `--dim #6b6b78` on `--card #131316` comes to about 3.5:1 for 10 px text, under 4.5:1. This is my own arithmetic, not a measured figure.
   - Light is fine: dim on card is 5.95 in `contrast.txt`.
   - Give it a 78% mix like the other pills, or measure it.

3. **Minor: a tile's stats can wrap onto two lines at 768 px.** In `shots/tablet-greece-tiles-light-part1.png`, Unit 10's stats wrap ("12 modules written 12 in all" / "2.7 h of reading"). Its neighbour, Unit 11, keeps one line, so the two patches in that row do not sit level.

4. **Minor (outside the tiles):** `verify-lines.txt` line 8 records the lowest light text on the phone at 4.29:1 (`rm01 span.bn`), under 4.5. It is not a tile, but it is an open number in the run.

**Confirmed**

- **One class set everywhere.** All 948 tiles across 84 runs report `cls` "course live" and a patch inside the tile (`pin` true, no false). None runs past its edge (`sw` true appears 0 times). Every run's `bad` list is empty (84 of 84).
- **Fields per kind (children):**
  - Link tiles: `div.ctop span.ctitle p div.cstats div.topo.topo-patch`.
  - History disclosures: the same plus `svg.chev`.
  - Ghosts: no `cstats`, plus a chevron.
  - `tile-markup.html` matches all of this: `.ghost` and `.pending` are added, the patch viewBox is 720×180 (4:1).
- **Patches match their sources (spot-checked at 320 dark).**
  - Home course rises equal each course's unit words: Greece U0–U12, Rome U0–U13, A1–DD-A2, B1–DD-B3 and IA1–IA7. IA's 8 planned units are flat rings.
  - Greece unit tiles: U0 (2789/3049/2775) through U3 and U12 match their modules. U13's 5 planned modules are flat, its stats 0/5/0.0, pill "not run yet".
  - Markdown tiles: A1 (7 sections, 5,280 words), A2 (8 sections, 5,621 words), IA1 (7 sections) and IA7 (9 sections, 12,672 words) match their section words.
  - Pending IA8–DD-IA3: one plan ring each, stats 0/0/0.0.
- **History tiles open to their rows.** All 348 disclosure tiles carry mods and rows. Opened Greece U0 has 3 rows (m01–m03) and U1 has 3. Rome U0 has 3 and U1 has 6 (rm11–rm16); the shots show them (e.g. `phone320-rome-tiles-light-part1.png`). All 48 opened tiles show their line whole (`clipped` false, 3–6 lines). While one is open, its neighbour does not stretch (tablet Greece, Unit 0 and Unit 1 rows).
- **Markdown links.**
  - All 22 brand tiles go to `#read-a1`…`#read-dd-b3`, matching `pages`.
  - IA1–IA7 go to `#read-ia1`–`#read-ia7`.
  - IA8–DD-IA3 go to their briefs, `#ux-ia-b-ia8`…`#ux-ia-b-dd-ia3`, matching `briefs`.
  - The home's course tiles go to `#greece`, `#rome`, `#brand-a`, `#brand-b` and `#ux-ia`.
- **Ghost tiles (96 = 8 × 12 runs).** Each has the chip ("History ·" plus the place), the title, a 2-line clamped scope, no pill, no stats, one dashed plan ring and a dashed outline. In the shots the chip is outlined and the scope reads in muted text.
- **Columns.**
  - 1 column at 320, 360, 390 and 430 px; 2 columns at 768 and 1280 px, on every grid.
  - Lone tiles are half the grid's width at 768 px and up (342 = 342 on the home, 358 = 358 on the Greece and Rome units).
  - Below 768 px a lone tile is the full column, as the one-column rule sets.
  - Grid counts match: Greece 2+3+3+2+3+1 = 14, Rome 3+3+3+2+3+1 = 15, home 2/8/1/1/1, brand 11, IA 15.
- **No sideways scroll.** Scroll width equals the page width in all 84 runs.
- **Light paper.**
  - Tokens: `--bg #e8e4dc`, `--card #f0ede6`, `--on-accent #f5f2eb`, no white.
  - The light shots show cream cards on tinted track bands.
  - `contrast.txt` puts every P93 light and dark pair at 4.5:1 or above (chips 4.57–12.57, pills 5.71–12.00, tile text 6.66–15.75).
- **Tones by role.** Course B and Rome share purple `#9b5de5`. History units carry their own syllabus tones (e.g. Greece U0 gold, U1 orange).

**Renderer notes**

- The data's line count did not catch Finding 1. It reports 2 lines and clipped for tiles whose shots plainly show a third line, so it seems to count the clamp, not what is painted. Finding 1 rests on the images alone.
- The phone shots are long strips scaled down for me (780×7000 shown at 223×2000). Small text there I read from data, not pixels. I opened 9 of the shots, not all ~150: phone ux-ia dark, phone home dark, phone320 Rome light, tablet Greece light, tablet ux-ia dark, desktop brand-a dark, desktop ux-ia light, desktop home light, and others only through the data.
- The extract's `cls` drops the `ghost`/`pending` modifiers that `tile-markup.html` shows. I took the modifiers from the markup.
- `verify-lines.txt` is 694 lines; I read lines 1–203 and searched the rest.
- I took everything under reduced motion, still, as the brief says.

**FIX**