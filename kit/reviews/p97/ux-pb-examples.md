Model: claude-opus-5-5

All 15 compare figures pass at 320 px and 390 px, in dark and light. I opened all 60 sheets. Every sheet says "frame 1 of 1 (the whole figure fits)". I measured bar lengths in pixels, and every bar matched its value to within about 1 px.

| figure | 320 | 390 | verdict | note |
|---|---|---|---|---|
| read-dd-ia2 fig 1 | fits | fits | PASS | The 10 rows match §1.6 in order: 78, 66, 66, 81, 86, 87, 46, 9, 14, 10 %. Scale is 0–100. The two "failed by IA" rows use their own tone, as the caption says (tone 6). The "87%" value sits right at the end of its track but is not clipped. |
| read-dd-ia2 fig 4 | fits | fits | PASS | The 10 layers match §4.2: 22, 15, 10.5, 8, 7, 3, 2, 2, 1.5, 1.5 days. Ratios are exact (for example 15/22 and 1.5/22). "22 days" runs past the end of the track but stays whole. One tone throughout, as the caption says. |
| read-dd-ia3 fig 3 | fits | fits | PASS | The three rows match the text and caption: around 200, around 400, around 4,000. The 200 and 400 bars are about 1/20 and 1/10 of the 4,000 bar, as they should be. "around 4,000" is whole beside the full bar. |
| read-ia10 fig 1 | fits | fits | PASS | Support 26, Marketing 13, Content team 5, Legal 3, Product 2, Sales 2, Partnerships 1. These sum to 52, which matches the text and caption. The labels sit in a column to the left and line up with their bars. |
| read-ia4 fig 2 | fits | fits | PASS | The five Zaphiris structures and times match the text: 36.0, 32.2, 32.4, 21.0, 20.3 s. The scale checks: the 32.2 and 32.4 bars are 0.89–0.90 of the 36.0 bar. The values on the three longest rows run slightly past the track end but are whole. |
| read-ia6 fig 3 | fits | fits | PASS | The 12 employee tasks T-01 to T-12 are all present, in the table's order, with its frequencies: 8, 3, 2, 1.5, 1.5, 1, 0.5, 0.5, 0.3, 0.1, 0.1 a month, and once. The bars are to scale. "Join from HR's invitation" has no bar, correctly, since "once" is not a monthly rate. Minor style point: the whole numbers are shown as "8.0 / 3.0 / 2.0 / 1.0" where the table says 8, 3, 2, 1. The values are the same. The caption's note that paying with the card does not open the app explains why the longest bar is a task done at the till. |
| read-pb1 fig 1 | fits | fits | PASS | 0.20%, 1.86%, 8.65%, 30.77% match the §2 table. The 0.20% bar is a correct hairline. Labels read "None added", "1–11 videos" and so on, which are the table's bands. "30.77%" goes past the track but is whole. |
| read-pb1 fig 2 | fits | fits | PASS | 0.12, 0.26, 0.44, 0.66 % match Buffer's figures in §3, and the bars are exactly to scale. The figure adds a "No posts (baseline) 0.00%" row. The text's own "against weeks with no posts" implies it, so it adds no new data. The rows use mixed tones (3–5 and 10+ stand out) and the caption does not explain them; this is a style point only. |
| read-pb1 fig 3 | fits | fits | PASS | The seven bands and 1.26, 0.59, 0.53, 0.51, 0.48, 0.30, 0.24 % match §6 and the caption's source, and the bars are to scale. "1.26%" runs past the track end but is whole. |
| read-pb3 fig 2 | fits | fits | PASS | Reels 4.9%, Image posts 3.5%, Carousels 2.6% match the text, and the bars are to scale. The caption's source matches the text: Fanpage Karma, 7 Aug 2026, more than 3 million posts, January to April 2026, accounts under 10,000. |
| viz-examples fig 2 | fits | fits | PASS | It matches the viz block exactly: 64, 41, 27, 18, 3 % against max 100, with the block's tones (3, 3, 4, 2, 5). "Browse the catalogue" wraps onto two lines but stays beside its bar. |
| viz-examples fig 20 | fits | fits | PASS | It matches the page's description: a label wider than the old label column, which now wraps; large values with digit separators; and the word unit "men" with a space before it. The values are 1,200, 770,000 and 337,022, and the bars are to scale: 337,022 is 0.44 of the longest, and 1,200 is a hairline. The page text gives no viz block for this figure, so I checked it against that description only. |

**FAIL details:** none.

Points across all figures:
- Values on or near the longest bar often run past the end of its grey track. They are never clipped or overlapped, and they are clearly tied to their row.
- Every tone is legible in dark and light. The thinnest marks (0.1, 0.20% and 1,200) are hairlines, which is correct for their values, and their value labels stay readable.
- Every caption fits what its figure shows.
- Each sheet is exactly one frame at both widths.
