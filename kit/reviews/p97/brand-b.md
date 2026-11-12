Model: claude-opus-5-5

I read only the files in /tmp/p97/recheck/brand-b/: FIGURES.txt, each page's -text and -captions file, and all 44 frame sheets (11 figures × 320/390 px × dark/light). Every sheet says the whole figure fits in frame 1 of 1. For the scale check I measured bar lengths in pixels against the values; every ratio was within about 1%.

**All 11 figures pass. None fail.**

| figure | 320 | 390 | verdict | note |
|---|---|---|---|---|
| read-b2 fig 1 | fits | fits | PASS | Values match the Output column: Fable $50, Opus $20, Sonnet $10, Haiku $0.50 (prompt up to 100K). The bars are in the 1:20:40:100 ratio, and Haiku's 1% is drawn as a hairline. Note: the Haiku over-100K row ($2.50) is left out. The figure's own Haiku label says "(prompt up to 100K)", and the caption's ratio uses four models, so this is not a fault. If you want the figure to match "The Output column" exactly, add "(prompt up to 100K)" to the caption. Style: the Haiku value text runs past the end of the grey track. |
| read-b2 fig 3 | fits | fits | PASS | Matches the text's Reading 4: Sol 0.59, Opus medium 2.45, Argon 3.84, Fable high 7.56, with the effort level in each label. The bars are to scale (Argon is 0.508 of Fable, Opus 0.324, Sol 0.078). Style: "7.56" sits half on the track end and half off it, but it is readable. |
| read-b4 fig 2 | fits | fits | PASS | 200K window, 259K at 3.5 and 336K at 2.7 all match §3. The bars are to scale (0.595 and 0.771 of 336). Style: the value labels spill past the track end, but they are readable. Unlike the other figures, this one has no title line; the caption carries the units. |
| read-b4 fig 4 | fits | fits | PASS | All seven shares match F1: 26.8, 24.4, 21.8, 12.6, 8.7, 5.1 and 0.5%. They are sorted by size, which is fine, and all are to scale. Minor: the teal bar marks the five files F1 keeps ("rules, map, queue"), but neither the caption nor a legend says so. A short clause in the caption would explain it. |
| read-b5 fig 1 | fits | fits | PASS | 186 / 200 / 1,024 / 1,536 match the caption sources and Deliverable A ("description is 186 characters"). All bars are to scale. |
| read-b5 fig 2 | fits | fits | PASS | 16, 11, 6, 5 and 3 match §3's five features. The track spans 19, so each bar is a share of the 19 skills, and each is exact. |
| read-b6 fig 1 | fits | fits | PASS | 1×, 4× and 15× match §1. The text cites "about 4×" (the agents line) and "about 15×" (the multi-agent line), both from Hadfield et al. Bars are to scale. Minor: the figure drops the "about". |
| read-b7 fig 1 | fits | fits | PASS | 28, 20, 18 and 17% match §8, and the labels match the category names. Bars are to scale. |
| read-b8 fig 2 | fits | fits | PASS | 930K against 370K matches §3, and I re-checked the arithmetic: 2,000 × 465 = 930,000, and 110 + 130 + 130 = 370. Bars are to scale (0.398). Style: "930 k tokens" straddles the track end. |
| read-dd-b2 fig 1 | fits | fits | PASS | 15, 15, 7, 6, 6, 2 and 2 match §2 and add up to 53. Bars are to scale, and each label sits on its own row. Minor: four colours group the categories (writing, build, audit, questions), but the caption does not explain them. |
| read-dd-b2 fig 3 | fits | fits | PASS | 18, 1, 0, 0, 2 and 1 match §4 ("Eighteen of the 22 began on 28 October; one … 29 October, two on 1 November and one on 2 November, none on 30 or 31 October") and add up to 22. The zero days are shown as empty tracks with "0". Bars are to scale. |

**Points across all figures (style only, not failures):**
- **Readability:** every figure is legible in both dark and light. Labels, bars and values are never clipped, and each label is clearly attached to its own bar.
- **Same drawing at both widths:** the 390 px drawings are the same width as the 320 px ones. The figure does not widen on the larger screen, but nothing is lost.
- **Value labels at the track end:** where a value label is placed at the end of its bar, it sometimes overlaps the boundary of the grey track (b2 fig 1 Haiku, b2 fig 3 Fable, b4 fig 2, b4 fig 4 rows 2–3, b8 fig 2). It reads fine. Placing those labels wholly on the track, or wholly outside it, would look cleaner.

No FAIL details to report.
