**Findings**

1. **Should-fix. Desktop: the Marketing and Technology shelves sit at different heights.** Files: `shots/desktop-home-dark-part1-of2.png`, `shots/desktop-home-light-part1-of2.png`, and the end frames of both `desktop-rise-*.png`. On the desktop these two tracks sit side by side, but their bottoms do not line up. Personal brand's spines end and its rule sits about 8–9 CSS px higher than Building with AI's. Measured on the screenshot (displayed at 1067 px wide): rule at y≈540 against y≈547, and the course names at y≈553 against y≈561. The cause is that each track is anchored at the top and its spines hang from that, so the track with the tallest spine (B3, `--h` 0.160, against A8's 0.107) ends lower. On a drawing meant to read as a bookshelf, two neighbouring shelves at different heights looks like a mistake, and it is the first thing the desktop reader sees. The History row is fine: Greece, Rome and the volume all end at the same line.
2. **Should-fix (evidence gap, not a fault seen on the page). The 768 px screenshots stop before the User Experience shelf.** Files: `shots/tablet-home-dark-part1-of5.png`, `shots/tablet-home-light-part1-of5.png`. Both end just under "Building with AI 11 of 11", where the User Experience marker is starting to show. The tablet part 2 that holds the IA row is not in the folder. So at 768 px I could not check the lit IA7 spine, its label, the wrapping of the planned spines, or the right edge (checks 3, 5 and 6 at this width).
3. **Minor. Tablet (768 px): the shelf hugs the left side.** Same files as finding 2. Greece takes about 380 of the 728 px available, and Rome wraps onto the next line. Marketing and Technology are stacked rather than side by side as on the desktop, even though both would fit on one line (about 308 px each). The result is a large empty area on the right of the hero. The brief sets no rule for tablet; this is an aesthetic note only.
4. **Minor. Dark theme: unit codes on the purple and steel-blue spines are low contrast.** Files: `shots/desktop-home-dark-part1-of2.png`, `desktop-rise-dark.png`. The codes are dark text on medium purple (Rome, Building with AI) and on muted steel blue (IA). By my estimate that is about 4.5:1, and the text is about 10 CSS px on the desktop. It can be read in the shots, but it is the weakest text on the shelf. Light theme (white on dark red, purple, teal and blue) is clear.
5. **Minor. On phones some rows end with an orphan, and the IA7 pair leaves a gap.** Files: `shots/phone-home-*-part1-of5.png`, `shots/phone320-*-part2-of5.png`, `shots/phone360-*-part2-of5.png`. At 390 px, Greece U12 wraps onto a row of its own. At 320, 360 and 390 px, IA7 and its label wrap together, which leaves the first IA row at six spines with empty space after IA6. This is correct behaviour (the label stays beside its spine and the order is kept); it is noted only as a look.

**Confirmed**

- **Counts and order (check 1).** Every count, the order and the written/planned split match `sources_shelf`:
  - Greece: 13 spines, U0–U12, all solid.
  - Rome: 14 spines, U0–U13, all solid.
  - Personal brand: 11 spines (A1–A9, DD-A1, DD-A2).
  - Building with AI: 11 spines (B1–B8, DD-B1–DD-B3).
  - Information architecture: 15 spines. IA1–IA7 are solid; IA8–IA12 and DD-IA1–DD-IA3 have class `ghost` (dashed outline, no fill in every shot).
  - That makes 64 spines, plus one ghosted volume reading "8 planned". Its `title` lists Egypt, Persia, Norse, Celts, England, Scotland, China and Japan, in the order given in `planned_history_courses`.
- **Links (checks 1 and 4).**
  - Every spine's `href` is `#` + its `data-target`, and every `data-target` equals the `opens` value in `sources_shelf`. Written history units go to `greece-uN` / `rome-uN`, written markdown units to `read-…`, planned IA units to `ux-ia-b-…`.
  - The newest label links to `#new` (its `data-target` is `new`).
  - The volume goes to `#planned-courses`. The brief names no target for it, and the markup supplied does not show that id existing on the page; the desktop shot does show a "Planned · 8 courses, in the intended order" panel under History.
- **Grouping.** The four tracks appear in order: History, Marketing, Technology, User Experience. Each has its name with a coloured marker, and each course's name and count sit under its group: "Greece 13 of 13", "Rome 14 of 14", "Personal brand 11 of 11", "Building with AI 11 of 11", "Information architecture 7 of 15". Course colours are as given.
- **Heights (check 2).**
  - I recomputed every `--h` from the words given as (words − 5079) / (40190 − 5079). All 64 match to three decimals. The scale is linear, so more words always gives a taller spine.
  - The ghost spines use 9552 words, which is 66866 ÷ 7, the mean of the IA units written, as the extract says.
  - Measured heights agree with the theme's ranges. Desktop: U10 is 210 px and U0 about 74 px, against 60 + 0.101 × 150 = 75. Phone: U10 about 103 px (expected 104), U0 about 49 px (expected 50), B1 about 44 px.
  - Spines are 24–25 px wide.
  - Visible orders agree everywhere: U10 is Greece's tallest, U12 Rome's, A8 Personal brand's, B3 Building with AI's, and U0 and U1 are almost level.
- **Lit spine (check 3).** IA7 is the only spine with class `lit`. It glows in its blue in both themes at every width shown. The label beside it, inside `shelf-pair`, reads "← Newest · IA7 · 3 Nov"; the arrow is `aria-hidden`, so what is read out is exactly "Newest · IA7 · 3 Nov". It stays directly beside IA7 at 320, 360, 390, 430 and 1280 px, in both themes.
- **Titles (check 4).** Every spine has a `title`, identical to its `aria-label`, that names its code and title. Planned spines end with "(planned)".
- **Edges (check 5).** Nothing is cut at 320, 360, 390, 430 or 1280 px in either theme. Spines and rules stay inside the 16 px gutter; at 320 px the content's right edge is about 304 CSS px. No sideways scroll shows at 320 or 360 px: the shots are exactly two times the viewport width and the shelf fits within it. The IA7 glow stays inside the viewport. The only "cut" codes are where the screenshot itself is divided into parts at 390 px.
- **First screen on phones.** Only the headline, the lede and the shelf appear in the first screen at every phone width.
- **Legibility (check 6).** Codes are readable on solid spines (light theme strongly so) and on ghost spines (grey inside the dashed outline). Long codes fit inside 44–52 px spines, including DD-IA1, DD-IA2, DD-IA3 and DD-A1. The volume's rotated "8 planned", the labels, the counts and the newest label read in both themes.
- **Desktop impact (check 7).**
  - Full-bleed: the hero (headline, lede, shelf and totals) starts at one left edge, about 332 CSS px, just right of the 300 px sidebar. It runs to about 1225–1248 px, while the sections below keep the narrower column.
  - Totals are set big beside the headline: 56 units written, 49 hours of reading, 5 courses live.
  - The totals are right. Units: 13 + 14 + 11 + 11 + 7 = 56. Hours: 733,666 words ÷ 250 ÷ 60 = 48.9, which rounds to 49. Courses live: 5.
  - The course-card hours also agree with the words: 16, 18, 5.0 and 5.5.
- **Rise.** The two-frame sheet shows the staggered rise in both themes. At 160 ms Greece is part-risen, Rome's first spines are just appearing, and the later tracks are still empty. In the end frame every spine is at rest and the label is in. The 66 animations are the 64 spines, the volume and the label; the `--i` indices run 0–64, with the volume at 27.

**Renderer notes**

- **To fix finding 1:** anchor the tracks in each desktop row to the bottom, so their shelves share one line (for example `align-items: end` on the container that places Marketing and Technology side by side, or a shared baseline for the shelf rules).
- **Tablet size:** the tablet shots are three times CSS size (2304 px wide for 768), not two times as `BRIEF.md` says. Tablet part 2 (or 3) is needed to check the IA row at 768 px.
- **Rise frames are cropped tight:** the totals' "LIVE" touches the frame's right edge, and the headline touches its left. That is the crop, not the page; the full desktop shot shows about 32 px of margin.
- **Planned heights:** ghost spines all take the course mean word count, so they render at one uniform height. That is consistent with the extract. The caption says height is "its length in words"; if the owner wants it exact, it could say planned heights are an estimate.
- **Title and label are identical:** `title` and `aria-label` carry the same text on every spine. Browsers normally suppress the duplicate description, so nothing needs to change. The volume link carries no `--h`; its height is fixed by the theme, which reads correctly.

**FIX**
