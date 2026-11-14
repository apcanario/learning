# Legend re-check: 25 matrix figures (phone 390 px and desktop, light)

Checker: claude-opus-5-5. Every sheet in shots/ was opened (50 images); frame 1 of each phone sheet was also cropped at full resolution (out/crops/) to read the legend at legibility size. Checked: the legend only.

Result: 25 PASS, 0 FIX.

| # | Figure | Verdict | Notes |
|---|---|---|---|
| 1 | m41 fig 2 | PASS | 3 keys stacked under the grid in phone frame 1, all whole. Desktop stacked, clean. |
| 2 | read-a1 fig 2 | PASS | 4 keys whole in phone frame 1 ("yes" and "no" share a row). The "not reached" text wraps with a lone "it" on line 2, at phone and desktop; legible, no overlap. |
| 3 | read-a8 fig 3 | PASS | 9 keys stacked, all whole in phone frame 1; two-line texts clear of neighbours. Desktop clean. Outside this check: several key swatch colours do not match the grid cells they explain (grid "owns", "confirms", "label" and "enforces" cells are blue; their keys are green, tan, tan and tan). |
| 4 | read-dd-a1 fig 4 | PASS | 4 keys whole in phone frame 1. The 3-line "partial" text is centred on its swatch, so its first line comes up to within a few px of the "own words" text above, at phone and desktop. Close, no overlap. The gap above "unpub." is larger than the others. |
| 5 | read-dd-ia1 fig 7 | PASS | 2 keys, whole. Desktop clean. |
| 6 | read-dd-ia1 fig 8 | PASS | 3 keys, whole; "tone 6" wraps to 2 lines cleanly. Desktop clean. |
| 7 | read-dd-ia2 fig 3 | PASS | 3 keys, whole. Desktop clean. |
| 8 | read-dd-ia3 fig 1 | PASS | 2 keys, whole. Desktop clean. |
| 9 | read-dd-ia3 fig 4 | PASS | 6 keys stacked, whole in phone frame 1. At desktop the figure also scrolls (2 frames): frame 1 shows the whole legend; in frame 2 it has scrolled off to the left with the drawing. This is the same behaviour as on phone and is not a cut in frame 1. |
| 10 | read-ia1 fig 4 | PASS | 2 keys, whole. Desktop clean. Outside this check: the green "help, download" cell has no key. |
| 11 | read-ia10 fig 2 | PASS | 4 keys, whole in phone frame 1. At desktop the figure scrolls: legend whole in frame 1, scrolled off left in frame 2 (expected). |
| 12 | read-ia11 fig 6 | PASS | 2 keys, whole. Desktop clean. |
| 13 | read-ia12 fig 2 | PASS | 2 keys, whole; "tone 6" text wraps to 2 lines cleanly. Desktop clean. |
| 14 | read-ia3 fig 2 | PASS | 2 keys, whole. Desktop clean. |
| 15 | read-ia3 fig 4 | PASS | 2 keys, whole; both texts wrap to 2 lines cleanly. Desktop clean. |
| 16 | read-ia4 fig 8 | PASS | 2 keys, whole. Desktop clean. |
| 17 | read-ia5 fig 7 | PASS | 2 keys, whole. Desktop clean. |
| 18 | read-ia6 fig 1 | PASS | 2 keys, whole. Desktop clean. |
| 19 | read-ia6 fig 5 | PASS | 2 keys, whole. Desktop clean. |
| 20 | read-ia7 fig 5 | PASS | 9 keys stacked, all whole in phone frame 1, including the 4-line "edit" and "manage" texts. Desktop clean. |
| 21 | read-ia9 fig 2 | PASS | 4 keys, whole. Desktop clean. |
| 22 | read-pb2 fig 1 | PASS | 3 keys, whole in phone frame 1. At desktop the 3-line "source found" text sits about 8 px under the grid's bottom edge, which is tight but does not overlap. |
| 23 | read-pb8 fig 4 | PASS | 5 keys, whole in phone frame 1; the wide "on objection or change" swatch pushes its text into a 3-line column that still ends inside the frame. Line spacing to "if a hit" above is tight but there is no overlap. At desktop the drawing overflows by only 2 px, so a second frame exists, and in it the left-edge scroll fade lies over the left part of every key swatch ("owns", "answers", "if unclear", "if a hit", "on objection or change"). The text is still legible and nothing is cut, but a 2 px overflow that triggers the fade is worth removing. |
| 24 | rm121 fig 2 | PASS | 5 keys, whole in phone frame 1. At desktop the figure scrolls: legend whole in frame 1, scrolled off in frame 2 (expected). |
| 25 | rm31 fig 3 | PASS | 1 key ("most"), whole in phone frame 1. At desktop the figure scrolls: legend whole in frame 1, scrolled off left in frame 2 (expected). Outside this check: the blue cells (confers, elects, declares, hears, passes) have no key. |

## Across all 25
- Phone frame 1: every key's swatch and text is whole and legible. No text is cut at the frame's right edge, and the sticky label column's fade lies over no key: the keys sit at the left, under the label column, below the grid.
- Overlap: no key's text overlaps another key, the grid or the caption, at phone or at desktop. Spacing is tightest in dd-a1 (multi-line "partial" text close to the key above), pb2 desktop (text close to the grid) and pb8 (multi-line text close to "if a hit").
- Desktop: every legend is stacked one key per row (a1 shares one row between two keys) and is whole in frame 1. In figures that also scroll at desktop (dd-ia3 fig 4, ia10, pb8, rm121, rm31), the legend scrolls with the drawing in later frames, as it does on phone.
- Not legend placement, and so not graded: a8 swatch colours do not match their grid cells; ia1 and rm31 have cell tones with no key.
