**Findings**

1. **should-fix** (shots `768px-home-*-part2-of-4.png`, `768px-home-*-part3-of-4.png`, `1280px-home-*-part1-of-2.png`, `1280px-home-*-part2-of-2.png`). From 768 px, the sub-label of each closed rule block is not aligned with the others. It floats somewhere in the middle of the row instead of sitting at a fixed column:
   - At 768 px, "the method of the track" (Why history and myth together) starts about 708 display-px in. "8 courses, in the intended order" (Planned), in the block directly below it, starts about 497. "the constants" (How every course works) starts about 713.
   - At 1280 px it is the same: about 692 against 587.
   - Why and Planned are stacked one on top of the other, so the mismatch is plain to see and reads as uneven. `theme-excerpt.css` only lays out `details.rules>summary` below 768 px (line 58). From 768 px the summary falls back to a rule elided from the excerpt, which apparently spaces three items (title, sub-label, `::after`) across the row by their widths.
   - The fix: from 768 px, give the sub-label a fixed place, either a set column in a grid like the phone rule or right-aligned next to the +. Both themes are affected.
2. **minor** (`320px-home-dark-part2-of-4.png`, `320px-home-light-part2-of-4.png`). At 320 px, Planned's sub-label breaks to leave "order" alone on the second line. Why's title also takes two lines ("WHY HISTORY AND MYTH / TOGETHER"). Neither is cut, and both read correctly. The lone "order" is the only orphan on the page. It is gone from 360 px.
3. **minor** (all light shots). The page and the cards follow the e-ink rule: a warm grey-cream page, cards a little lighter, near-black ink, no pure white anywhere. The four area bands, however, are clearly tinted: History pinkish, Marketing grey-green, Technology lavender, User Experience grey-blue. The Technology lavender and the History pink are the most coloured surfaces on a page that is otherwise paper. The rules do not forbid the bands, so this is not an error. I note it because "e-ink paper" could be read as asking for less colour in them.

**Confirmed**

- **Order** (`data-extract.json` `order`, every width, both themes, both motion settings): hero, then the four `section.track` blocks (History, Marketing, Technology, User Experience), then How every course works, the site links, New since, and the one link to What's new, last on the page. The shots and `home-markup.html` agree.
- **Area headers**: `heads` is [label false, name true, lede false, count false] for all four sections at 320, 360, 390 and 430, and all true at 768 and 1280. The shots match.
  - Phones: only the name shows, with no rule of its own, and the first tile's rule in the tone closes the header.
  - From 768 px: TRACK label, name, lede, count, and a 2 px rule in the tone.
  - The counts are "2 courses · 157 reports · 8 planned", "1 course · 11 of 11 units" (twice) and "1 course · 7 of 15 units". These agree with the sources: 13 + 14 units, 78 + 79 reports in the sidebar, and IA with 7 written and 8 null.
- **Tiles**: there are five, each the link to its course home (`#greece`, `#rome`, `#brand-a`, `#brand-b`, `#ux-ia`), and each carries the same fields:
  - the chip (area · course) with the status pill under it;
  - the title, under its full name;
  - the tile line, two lines with no ellipsis at any width;
  - the three stats.
  - The stats check out at 250 words a minute: Greece 246,589 words gives 16 h, Rome 263,904 gives 18, A 74,284 gives 5.0, B 82,023 gives 5.5, IA 66,866 gives 4.5. "In all" is 13, 14, 11, 11 and 15.
  - History's word total, 510,493, equals Greece plus Rome.
- **Patches**: in every `built` state, each card's `rises` equal its course's written units, codes and words exactly as in `sources`, in order.
  - The `plan` lists are empty for the four complete courses. IA's is IA8–IA12 and DD-IA1–DD-IA3, matching its eight null units, drawn as eight dashed rings.
  - `data-rings` in the markup equals the extract's `rings`.
  - Rings rise monotonically with words in every course, and the thresholds are consistent across courses.
  - The patches are `aria-hidden="true"` and static (`anims` is empty under reduced motion, and only the hero's animations run when motion is allowed).
  - Each patch is the full content width at 4:1: pw/ph is 239/60, 279/70, 309/77, 333/83 and 309/77. `cw` is the card's own width.
  - The drawing is the same at every width (one viewBox 0 0 720 180).
  - Strokes are the theme roles: Greece red, Rome purple, A teal, B purple, IA blue. The light values are #bd0000, #7400fe, #006b5e and #0062a0.
- **History blocks**: after History's tiles come "Why history and myth together" and the folded Planned list ("8 courses, in the intended order", eight `details.course.soon`).
- **New since**: six rows matching `new_since_rows` (IA7, IA6, IA5, IA4, IA3, DD-B2). The heading is "New since 2 Nov", the oldest row's day. One link to What's new follows, last on the page.
- **Site links**: Backlog, Figure kinds, Changelog. One to a row from 320 to 430 px, three across at 768 and 1280.
- **Columns**: one column below 768 px. From 768 px Greece and Rome sit side by side at equal height, and Marketing's, Technology's and UX's lone tiles are half-width.
- **No sideways scroll**: `scroll` equals the viewport at every width. Nothing in the hero text or tiles is cut at an edge in any shot.
- **Light theme**: as described in finding 3, the page and cards meet the e-ink rule.
- **verify.py**: `verify-home-lines.txt` ends ALL CHECKS PASSED, and its tile, head, row and page figures match the extract.

**Renderer notes**

- The rings do not step at exact fifths of the largest unit. The observed thresholds are about 0.38, 0.55, 0.73 and 0.88 of it. Because of this, Rome U11 (31,767 words, 91% of U12) shows five rings, the same as U12. They are consistent and monotonic, so this is within the given density rule. It is a note, not a finding.
- The hero's contour layer bleeds past the viewport edges at every width (for example, the green and purple rises at the phone edges). That is the intended full-bleed layer, and no hero text is cut.
- Outside my scope (the hero has its own checker): the hero lede still says "Pick up where you left off.", although the home has no Continue (P91).
- The sidebar ends at the first screen's height in the 1280 px captures. That is the capture, as the brief says.

**FIX**
