**Findings**

1. Minor. On phones the IA7 spine and its label wrap together as one unit, so the first IA row stops short. Seen in `shots/phone320-*-part2`, `phone360-*-part2` and `phone-*-part2` (390 px). Row 1 holds only IA1 to IA6 and leaves about five empty slots. IA7, the label and the first ghosts start row 2. The order is still right and the label still sits beside its spine. The ragged row just makes IA7 look a little cut off from IA1 to IA6. At 430 px and wider, IA7 stays on the row with the others. Either keep this deliberately or shorten the label on narrow screens.
2. Minor, not checkable from the files. The "Newest · IA7 · 3 Nov" label is a link, but it is set as a single line of small text. The 44 px tap-target rule covers spines and is met. The shots cannot show whether the label's own box is at least 44 px tall on a phone.
3. Minor, not checkable from the files. The "8 planned" volume links to `#planned-courses`, and the brief does not say where it should go. The obvious target is the "Planned · 8 courses, in the intended order" panel in the History track. Nothing in this folder shows that this panel has the id `planned-courses`.

**Confirmed**

- **Spine count and order** (`shelf-markup.html` against `sources_shelf`):
  - Greece has 13 spines (U0 to U12) and Rome 14 (U0 to U13), all solid, each linking to `#greece-uN` / `#rome-uN` with a matching `data-target`.
  - Personal brand has 11 (A1 to A9, DD-A1, DD-A2) and Building with AI 11 (B1 to B8, DD-B1 to DD-B3), each linking to `read-…`.
  - Information architecture has 15. IA1 to IA7 are solid and link to `read-ia1…7`. IA8 to IA12 and DD-IA1 to DD-IA3 are ghosted and link to `ux-ia-b-…`.
  - Total: 64 spines. The animation order (`--i`) runs 0 to 64 without gaps, with the volume at 27.
- **Grouping**: tracks are History, Marketing, Technology and User Experience. Each course's name and count sit under its group: "13 of 13", "14 of 14", "11 of 11", "11 of 11", "7 of 15".
- **Planned history courses**: one dashed volume labelled "8 planned" under the label "Planned". Its `title` lists Egypt, Persia, Norse, Celts, England, Scotland, China and Japan in the sources' order.
- **Heights**:
  - I recomputed every `--h` as (words − 5079) / (40190 − 5079). All 64 match to three decimals, so the scale is linear and more words never gives a shorter spine.
  - Planned IA spines use 9552 words, which is the mean of IA1 to IA7 (66,866 / 7).
  - Measured in the shots: the shortest spine (B1) is about 44 px on phones, and Greece U10 is 210 px on the desktop. The visible order is right (Greece U10 > U12 > U6 ≈ U11; Rome U12 > U11 > U13).
- **Sizes**: spines are 24 px wide on phones. No spine code is clipped, including short ones (DD-A2 at 0.025, DD-B2 at 0.028) and ghosted ones (DD-IA1 to DD-IA3).
- **Lit spine and label**: IA7 is the only `spine lit`, with a blue glow in both themes. This matches `newest_unit` (IA7, 3 Nov 2026). The label reads "Newest · IA7 · 3 Nov" (the "←" is `aria-hidden`), links to `#new`, and sits right next to IA7 at every width (the `shelf-pair` wrapper keeps them together). What's new on the page lists IA7 on 3 Nov first.
- **Hover text and links**: every spine's `title` (and `aria-label`) gives its code and unit title, and ghosted ones add "(planned)". All links match `sources_shelf`.
- **Totals**:
  - Units written: 56 (13 + 14 + 11 + 11 + 7).
  - Courses live: 5.
  - Hours: 49. All written words add up to 733,666, and 733,666 / 250 / 60 = 48.9, which rounds to 49.
  - Per-course hours on the cards also agree: Greece 16.4 → 16, Rome 17.6 → 18, A 4.95 → 5.0, B 5.47 → 5.5, IA 4.46 → 4.5.
- **Edges and sideways scroll**:
  - At 320 px the rightmost content ends at about 296 px CSS against a 304 px content edge. At 360 px it ends at about 324 against 344. At 430 px it ends at about 408 against 414.
  - Nothing is cut at any width in either theme. The IA7 glow spreads into the left margin but is not clipped.
  - Edges that look cut at the boundary between screenshot parts, or on the desktop sidebar, are from the screenshots, not the page.
- **First phone screen**: only the top bar, headline, lede and shelf appear in it at every phone width.
- **Legibility in both themes**: spine codes are dark on the dark-theme colours and white on the light-theme colours. My estimated contrast is about 4.7:1 or better. Ghosted codes, the "8 planned" text, the labels, counts and the newest label are all readable.
- **Desktop impact**:
  - The hero runs the full width beside the 300 px sidebar, with one left edge for headline, lede and shelf. Marketing and Technology sit side by side.
  - The totals 56 / 49 / 5 are set large at top right.
  - The rise sheets show the staggered rise: at 160 ms Greece is at about 60% height and Rome is climbing in a stair-step, and at the end everything is at rest with the label in place. The caption counts 66 animations, which matches 64 spines plus the volume plus the label.
  - The resting frame matches the reduced-motion desktop shots.
- **Tablet (768 px)**: Rome and the volume share a row, Marketing and Technology share a row, and IA1 to DD-IA3 with the label fit on one row. Nothing is cut.

**Renderer notes**

- The lit label (`a.shelf-lit`) has no `--i`, but the caption counts it among the 66 animations, so it must be timed some other way (presumably after the last spine). Check it still starts after the shelf if the number of spines changes.
- On phones the IA7 + label pair needs about 186 px. Below roughly 400 px it pushes IA7 onto a new row (Finding 1). A shorter label at narrow widths, or letting the label drop below the spine, would remove the gap.
- Confirm that `#planned-courses` exists in the shell and opens the History "Planned" panel (Finding 3). Also check the label link's tap height on phones (Finding 2).
- I could not verify that the rise is turned off under reduced motion from these files. I only know the screenshots were taken with it on.
- Tablet (768 px) shows no totals. The brief asks for them only on the desktop, so this is consistent, not a fault.

**PASS**
