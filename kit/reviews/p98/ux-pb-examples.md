Model: claude-opus-5-5

(The harness refused to let me write /tmp/p98/recheck/ux-pb-examples/REPORT.md because subagents may not write report files, so the report is only here.)

Scope: P98 recheck of 15 compare and bars figures (PB1 figs 1–3, PB3 figs 1–3, PB4 fig 3, DD-IA2 figs 1 and 4, IA10 fig 1, IA11 fig 2, IA4 fig 2, IA6 fig 3, viz-examples figs 13 and 21). I read only /tmp/p98/recheck/ux-pb-examples/. For every figure I opened the 320 px sheet, the 390 px sheet (one dark, one light) and the 1280 px sheet, and checked each label and value against the unit text, or against the declaration for the examples. To check the rule that a value sits wholly on its track or wholly beyond it, I enlarged the track ends of the 1280 px sheets. Every sheet is a single frame ("the whole figure fits"), so nothing scrolls at any width.

| figure | 320 | 390 | 1280 | verdict | note |
|---|---|---|---|---|---|
| PB1 fig 1 (compare) | ok | ok | ok | PASS | 0.20/1.86/8.65/30.77% match §2 table ("\| None \| 27,360,211 \| 0.20% \|" … "\| 52 or more \| 883,403 \| 30.77% \|"). 30.77% sits beyond the track on phone and wholly on it at 1280. |
| PB1 fig 2 (compare) | ok | ok | ok | PASS | 0.12/0.26/0.44/0.66 match §3 ("higher by 0.12% in weeks with 1–2 posts, 0.26% with 3–5, 0.44% with 6–9 and 0.66% with 10 or more"). The new caption sentence about tones is present. |
| PB1 fig 3 (compare) | ok | ok | ok | PASS | Values match §6 ("1.26% at 1–99 subscribers, 0.59% at 100–499 … 0.24% at 1 million or more"). |
| PB3 fig 1 (bars) | ok | ok | ok | PASS | The 95/79, 91/64, 85/41, 65/21 and 84/51 pairs match the §2 table. |
| PB3 fig 2 (compare) | ok | ok | ok | PASS | 4.9/3.5/2.6 match §3 ("4.9% of followers for Reels, 3.5% for image posts and 2.6% for carousels"). |
| PB3 fig 3 (bars, stacked) | ok | ok | ok | FAIL | Values match D2 "Hours per four weeks" (Capture 2.0/4.0/8.0, Long-form edit 4.0/8.0/16.0, …, totals "11.75 of 12", "24.0 of 24", "39.0 of 40"). Fault (e): Capture and Log are drawn in the same tone, which is red in light and coral in dark, so the legend shows two identical swatches and the last segment of each bar cannot be told from the first by colour. |
| PB4 fig 3 (bars, stacked) | ok | ok | ok | FAIL | Values match D2's fortnight table: Week A 1.0+4.0+0.5+0.25+0.25 = 6.0; Week B 1.0+1.0+3.0+0.75+0.25 = 6.0. They also match the §7 recovery weeks: "the edit at about 8 minutes (3.0) … packaging 1.0, two Instagram posts … (1.0) … scheduling 0.25. With capture 1.0 and the log 0.25 that week is 6.5 hours". Same fault (e) as PB3 fig 3: Capture and Log share one tone. |
| DD-IA2 fig 1 (compare) | ok | ok | ok | PASS | All ten rows match §1.6 ("MeasuringU, tasks, 2011, 78; … NN/g sites, failed by IA, 2009, 10"). 86% and 87% sit beyond the track on phone and on it at 1280. |
| DD-IA2 fig 4 (compare) | ok | ok | ok | PASS | Matches §4.2 ("Objects 22; Roles 15; Top level 10.5; Vocabulary 8; Addresses 7; Reports 3; Lower labels 2; Queues 2; Lists 1.5; Landing 1.5"). |
| IA10 fig 1 (compare) | ok | ok | ok | PASS | Matches §2.3 ("Support 26, Marketing 13, Content team 5, Legal 3, Product 2, Sales 2, Partnerships 1"), which sums to 52 as the caption says. |
| IA11 fig 2 (bars, stacked) | ok | ok | ok | PASS | Successes 12/11/12/11/10/9/4/10/11/9 of 12 match the TT-A table ("T7 Past message \| 70% \| 4 \|" and the rest). Failures are 12 minus success. |
| IA4 fig 2 (compare) | ok | ok | ok | PASS | Matches §2.1 ("2 links a page, 6 levels, 36.0; 4 links a page, 3 levels, 32.2; 16 then 4, 2 levels, 32.4; 4 then 16, 2 levels, 21.0; 8 links a page, 2 levels, 20.3"). |
| IA6 fig 3 (compare) | ok | ok | ok | PASS | The P98 fix is in place: the figure prints 8, 3, 2, 1. All twelve rows match the A.1 table ("T-01 \| Pay with my card \| … \| 8 a month", …, "T-12 \| Join from HR's invitation \| … \| once"). |
| viz-examples fig 13 (bars, stacked) | ok | ok | ok | PASS | Matches examples-figure-13.json: title, Perqo card tone 4 (blue), Reimbursed claims tone 2, segments 5.6/0.2, 4.2/1.1, 3.1/0.6, 0.9/1.4, totals 5.8/5.3/3.7/2.3, caption. |
| viz-examples fig 21 (bars) | ok | ok | ok | FAIL | Fault (a): the drawing does not match its declaration. The sheets show "LONG LABELS IN BARS", Draft/Final, 770,000 / 412,000 words and 1,200 / 900 words, with caption "A test case for the renderer (P55) …". examples-figure-21.json is byte-identical to examples-figure-13.json (same md5, 45147ca2…). Either the declaration supplied is wrong or the figure is. The drawing itself fits and is legible at all widths. |

## Fixes

**PB3 fig 3.** Add a sentence to the caption. Replacement caption text:
> D2, the hours table: Mara's planning estimates per four weeks (Mara, fictional), totals 11.75, 24.0 and 39.0. The per-video and per-post hours are PB1's D2 planning figures; no dataset gives hours per piece (§6). Capture and Log share a tone: Capture is the first segment of each bar, Log the last.

The alternative is a series fix: give Log its own tone. All six tones are already used here, so this needs either a seventh tone in the renderer or a merged series. A merged series could be Email and Log as one entry, `{"name": "Email and log", ...}` with values 1.25 / 1.5 / 2.0, but that departs from the D2 table's separate lines, so the caption fix is preferred.

**PB4 fig 3.** Replacement caption text:
> Hours per week by line, §5 and §7 (Mara, fictional): weeks A and B total 6.0 each; each recovery week totals 6.5. The per-line hours are PB1 D2 and PB3 D2's planning figures, split into weeks by this unit; the 8-minute edit's 3.0 hours is PB3's estimate. No dataset gives hours per piece. Capture and Log share a tone: Capture is the first segment of each bar, Log the last.

**viz-examples fig 21.** Supply figure 21's own declaration in place of the duplicate examples-figure-21.json, then re-check the drawing against it. If the duplicate reflects what the page actually declares, figure 21's declaration on viz-examples.html has to be restored to the long-label test case the sheets show. That case is kind "bars", title "Long labels in bars", series Draft and Final, rows "A row label far wider than the old label column allowed" (770,000 / 412,000 words) and "Another" (1,200 / 900 words), and caption "A test case for the renderer (P55); its names, dates and numbers are invented and claim nothing." I cannot see the source, so I cannot say which of the two is wrong.

## Minor notes (not faults)

- minor: PB3 fig 3 and PB4 fig 3 print two decimals (24.00 h, 39.00 h, 6.00 h, 6.50 h, 4.00 h), while the text and captions give 24.0, 39.0, 6.0, 6.5 and 4.0. The values are the same; the second decimal is forced by 11.75, 0.75 and 0.25. IA6 fig 3 was fixed for the same kind of mismatch, so the owner may want trailing zeros trimmed.
- minor: PB1 fig 2's "No posts (baseline) 0.00%" row is not a figure in the text. It is the reference level by definition ("Against weeks with no posts").
- minor: PB3 fig 1's caption says "The age rows of the table in §2", but the figure also draws the All adults row (84% / 51%, which is in the table).
- minor: PB1 fig 1 and PB3 fig 2 colour their rows in different tones without saying the tones carry no meaning, as PB1 fig 2's caption now does.
- minor: viz-examples fig 13 omits the segment value of the small Food segment (0.2) at every width, and of Mobility (0.6) at 320 and 390 px. The totals are printed, so the omitted segment values can be worked out from them.
- minor: DD-IA2 figs 1 and 4, IA10 fig 1, IA11 fig 2, IA4 fig 2 and IA6 fig 3 have no in-figure title; the caption carries what each shows. This is consistent across the UX unit.
- minor: at 1280 px, several values sit on the track close to its end (DD-IA2 fig 4 "22 days", IA4 fig 2 "36.0s", PB1 fig 1 "30.77%"). Enlarged, each sits wholly on the track; none crosses the edge.
