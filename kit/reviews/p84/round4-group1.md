<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
13 figures checked: 12 PASS, 1 FIX.
FIX: Greece 5.5 figure 3. Its two span labels say "546–527" and "527–511"; the text, and the figure's own point labels, say c. 546, 527/6 and 511/10.
Greece 1.2 figure 3: the ascenders of "the" in the 1952 label are whole at 1280. Rome 13.4: no year 0. A8: the lawyer cell and key are drawn. Keys sit under the frame and row labels stay pinned on phone.
Report: the harness refused the write to out/report.md, so the full report is below.

# r4-1 figure re-check, round 4 (P84 timelines, P109 matrices)

Checker: claude-opus-5-5, fresh agent. Read only the packet: figures.md, text/, sheets/.

| Figure | Verdict | Notes |
|---|---|---|
| brand-a/read-a8.html fig 3 (matrix) | PASS | Every cell matches the register's Owner and Professional columns R1–R32: acts (R1–R12, accountant owns R3 and R8), if unclear (R13), optional (R15–R16, R19), if DGC writes (R17, the added cell, with its key), reviews (R22/R25, R26), policy (R23), sign (R22, R25), label (R18, R25), enforces (R29). Keys sit under the frame at every width. Row labels stay pinned at 390 and 320. Minor: R25's co-owner Shōmen has no column. It is his brand ("Him (Shōmen)", R26), so "owns" covers it. The two "label" cells come from R18/R25's constraint text, not from the Owner column. |
| greece/r-1.3.html fig 1 (timeline) | PASS | All eight rows of the table drawn at their dates. Spans carry their years. The BC labels are whole at every width. Minor: the Ugarit span is brown, between red spans, with no key. The other timelines in this packet vary span tones the same way, so this reads as the renderer's way of telling neighbouring lanes apart, not as a meaning. |
| greece/r-10.5.html fig 3 (timeline) | PASS | c. 1450, c. 1200, 1450–1200, no use 1200–700, cult 7th century BC, c. 650, stele 5th century BC: all in "The Menelaion and Mycenaean Laconia". Century labels carry BC as written. |
| greece/r-3.3.html fig 2 (timeline) | PASS | Measured against the gridlines at 1280: Bacchylides 489–470, Codrus cup 440–430, and the points at 510, 500, 490, 478, 476, 450 are all where the text puts them. Dashed guides break at labels and bars (checked at 320). |
| greece/r-4.2.html fig 3 (timeline) | PASS | Dates match both sections. Minor: book titles in point labels are roman, not italic. The two narrow 1930–32 and 1933–35 spans sit close together but their labels sit apart and are readable. |
| greece/r-5.1.html fig 3 (timeline) | PASS | All dates match the bulleted list. Minor: span labels ("c. 750–700", "c. 690–650") have no BC, while point labels and ticks do. They are readable against the BC axis. |
| greece/r-5.5.html fig 3 (timeline) | FIX | All 15 points are correct. The two span labels give "546–527" and "527–511". The text and the figure's own point labels give "c. 546", "527/6" and "511/10". |
| greece/r-6.3.html fig 1 (timeline) | PASS | Every event from 433 to 411 matches the sections. The in-bar label "From the outbreak to the Peace of Nicias, 431–421 BC" breaks onto two lines inside a taller bar at 320 and 390 and shows whole. |
| personal-brand-pb/read-dd-pb2.html fig 1 (matrix) | PASS | All 27 cells match §3 items 1–9. Every row is in the blue row tone, as the caption says. Keys sit under the frame. Row labels stay pinned at 390 and 320. Minor: in light mode the green of "her count only" is close to the row blue. The text in the cell tells them apart. |
| rome/r-11.6.html fig 3 (timeline) | PASS | 1828, 1855, 1861–1865, 1865, 1901, 1903, 1991–1997 all match the text. |
| rome/r-13.4.html fig 2 (timeline) | PASS | No year 0: gridline spacing measured at 1280 is 40 BC→AD 1 166 px (40 years), AD 1→AD 40 161.5 px (39 years), AD 40→AD 80 166 px (40 years). Spans 69–79 and 81–96 sit on those years. Minor: the AD 65 dot is half under the AD 66 dot. Both labels are separate and readable. |
| rome/r-3.4.html fig 2 (timeline) | PASS | 338, 329, 328, 314, 296, 291, 273, 268, 263 and the span 334–263 match the text. The corrected caption is accurate. The in-bar label breaks inside the bar at 320. |
| greece/r-1.2.html fig 3 (timeline) | PASS | At 1280 light and dark, the ascenders of "the" in "the BBC (1 July)" (the 1952 label's second line) are whole, checked at 4× zoom. All dates match "Linear B and its decipherment". |

Totals: 12 PASS, 1 FIX.

## FIX: greece/r-5.5.html figure 3

The two spans' labels give years that the text never gives in that form. The figure's own point labels for the same moments use the text's form: "c. 546 BC" for the third attempt, "527/6 BC" for Peisistratus' death, "511/10 BC" for Hippias leaving. The caption's rule that archon years are placed at their first year covers where a span is drawn, not what its label says. Change these declaration fields:

- Peisistratus span "date": `546–527` → `c. 546–527/6`. The label then reads "Peisistratus rules after the third attempt, c. 546–527/6 BC".
- Hippias span "date": `527–511` → `527/6–511/10`. The label then reads "Hippias rules, 527/6–511/10 BC".

Keep both spans' positions as they are (start at the first year). This round's renderer draws split years as written. Check that the longer Peisistratus label still breaks before its date and keeps the date whole on the last line.

## Sheets opened

- desktop light, every figure: all 13 `sheets/desktop-*-light.png`
- desktop dark, every figure: all 13 `sheets/desktop-*-dark.png`
- phone 390 light, every figure: all 13 `sheets/phone-*-light.png`, split into frames
- phone 320 light, every figure: all 13 `sheets/phone320-*-light.png`, split into frames
- Zoomed crops: m12 at 1280 light and dark (the 1952 label); m33 at 1280 light (span edges measured to the pixel) and 320 light frame 4 (dashed guides breaking at labels); m55 at 1280 light (span labels); rm134 at 1280 light (gridline spacing, no year 0)
- Phone dark sheets were not opened. Nothing in the light phone sheets or the dark desktop sheets was close enough to a limit to need them.

(Working crops from the check are in /home/claude/packets/r4-1/out/z/, which is inside the allowed out/ folder. Nothing else was written.)
