<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
Counts: 17 PASS, 6 FIX (23 figures).
FIX 1, renderer (m03 fig 1 and m53 fig 1): label wrap splits the years ("…BC–AD / 330", "(c. / 1950–1450)"). The date must stay whole on the last line.
FIX 2–4, declarations: m53 fig 2's Athens label puts its years mid-label; m74 fig 1's "(15–44)" has no AD; rm85 fig 1's cells take four tones against one key.
FIX 5, caption: read-ia6 fig 5 "Blank cells: none" contradicts the many blank cells in the grid.
Report path: the harness refused the write to /home/claude/packets/r2-4/out/report.md, so the full report follows.

# Re-check r2-4: P84 timelines and P109 matrices

Checker: claude-opus-5-5. 23 figures: 17 PASS, 6 FIX.

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-0.3 fig 1 (timeline, m03) | FIX (renderer) | All ten periods are where the table puts them. Spans sit on the axis with dashed guides, and the tick labels and gridlines are above the top lane. But the label wrap splits the years: "Roman Greece (146 or 27 BC–AD / 330)" breaks inside the date, and "Minoan palatial Crete (c. / 1950–1450)" and "Bronze Age collapse (c. / 1200–1150)" leave "(c." stranded on line 1. See F1. |
| greece/r-10.2 fig 4 (timeline, m102) | PASS | Grave Circle A c. 1600–1450, Trojan War dates c. 1300–1180, Troy VI c. 1300, Lion Gate and "Treasury of Atreus" c. 1250, "Tomb of Clytemnestra" c. 1220, Eratosthenes 1184/3 and Troy VIIa c. 1180 all match the text and the gridlines. Minor: the caption's "(1876)" is not drawn; it reads correctly as a source note. |
| greece/r-11.1 fig 1 (timeline, m111) | PASS | Archelaus c. 413–399, Amyntas III 393–370/69 and Philip at Thebes about 368–365 are measured exactly. The five table events are correct, and every label is whole in some frame at 390. |
| greece/r-12.6 fig 1 (timeline, m126) | PASS | Span 341–270 (module 7.2), 307/6, 306, 271/0 and "aged 72" match the text, and the positions are measured. |
| greece/r-3.3 fig 2 (timeline, m33) | PASS | Heracles c. 570–510, cycle cups c. 510–500, Bacchylides 480s or 470s (drawn 489–470), Codrus cup c. 440–430 and the events 510, c. 500/after 490, 490, 478/7, 476/5 and c. 450 are correct. The guides and gridlines break at the label plates. |
| greece/r-5.3 fig 1 (timeline, m53) | FIX (renderer) | The dates are correct (c. 720, c. 700–675, c. 650–640). The label wraps to "Double-grip shield appears (c. / 700–675)" at every width. See F1. |
| greece/r-5.3 fig 2 (timeline, m53) | FIX (declaration) | All six tyrannies are measured exactly against the table. The Athens label wraps to "Athens: Peisistratids (561/0–510, / interrupted)", so its years are not on the last line. See F2. |
| greece/r-5.3 fig 4 (timeline, m53) | PASS | Span 640–560 measured exactly. The events c. 600, c. 550 and from c. 515 match the text. |
| greece/r-7.4 fig 1 (timeline, m74) | FIX (declaration) | Dates and positions are correct. "Imperial command with Macedonia and Moesia (15–44)" has no era on an axis that crosses BC/AD; the next lane says "AD 44–67". At 390 px the label sits under the 50 BC tick while its bar is off-screen, so it reads as BC. See F3. |
| greece/r-7.4 fig 2 (timeline, m74) | PASS | Plotinus 204/5–270, Porphyry c. 234–305, Iamblichus c. 245–325, Julian 361–363, Proclus 412–485 and the events 244, 432 and 448 match the text. |
| rome/r-1.1 fig 1 (timeline, rm11) | PASS | The three spans match the text. Minor: the span labels drop the text's "c."; the caption covers it ("Approximate dates"). |
| rome/r-10.4 fig 1 (timeline, rm104) | PASS | 1341, 1345, 1347, 1354, 1373, Biondo 1444–1446, 1448 and about 1519 match the text, and every label is whole at 320 and 390. |
| rome/r-10.4 fig 4 (timeline, rm104) | PASS | 1799, 1802, 1804, Arc 1806–1808, Vendôme 1806–1810, 1809 and 1811 are correct and measured. |
| rome/r-13.7 fig 3 (timeline, rm137) | PASS | Every date and gloss matches the text (26 April 121, 138, about 146, 145, 31 August 161, early 169, 175 spring/winter, 177, 17 March 180, and the spans 138–161, 161–169, 169–176, 178–180). The guides break at the label plates. |
| rome/r-4.4 fig 3 (timeline, rm44) | PASS | Viriathus' war 147–139 is measured exactly. All 11 events match the text, and all labels are whole at 320. |
| rome/r-6.1 fig 1 (timeline, rm61) | PASS | Consul every year 31–23 BC is measured. 29, 28, 27, 23, 22 and 2 BC and AD 4 and 14 match the text. |
| rome/r-8.5 fig 3 (timeline, rm85) | PASS | Every publication year matches the text, and the ESF span 1993–1998 is in lane 0. |
| brand-b/read-b4 fig 1 (matrix) | PASS | Cells match the §2 definitions. The key sits under the frame and stays whole at 320/390/1280, and its tone matches the filled cells. The row labels stay in view while scrolling. Minor: in dark mode the filled tone (31,44,54) is close to the empty cell (30,30,36), but the dots and words carry the meaning. |
| personal-brand-pb/read-pb2 fig 1 (matrix) | PASS | Cells match §2 for each class and pattern. The three keys are whole under the frame at 390, and their tones match the cells. The row labels stay in view across all 7 frames. |
| rome/r-8.5 fig 1 (matrix, rm85) | FIX (declaration) | The cells match Hydatius s.a. 411. The one key ("411 shared out by lot in 411") is blue like the Hasding Vandals cell, but the Sueves, Alans and Siling Vandals cells are tan, teal and purple. The key does not match their tones, and the extra tones imply a distinction that the key does not explain. See F4. |
| ux-ia/read-ia12 fig 2 (matrix) | PASS | The rungs C0–C5 and their three columns match §3.3. Tone 6 is on the C2 and C3 proxy cells as the text says. The keys are whole under the frame. The matrix fits the column at 1280, and the row labels stay in view at 390. |
| ux-ia/read-ia6 fig 1 (matrix) | PASS | The rows match §3.5. The tone-6 cells are measured, and their tones match the keys exactly. The keys are under the frame and the row labels stay in view at 390. |
| ux-ia/read-ia6 fig 5 (matrix) | FIX (caption) | The cells match the B.5 table, and the nine stops the caption lists are all tone 6. The keys are whole and match the cells. But "Blank cells: none, as in B.5's table." reads as "there are no blank cells", while the grid has many blank cells (B.5's "none" cells). See F5. |

## F1. Renderer: wrapped span labels must keep the date expression whole (m03 fig 1, m53 fig 1)

What it draws wrong: when a span label wider than 220 units breaks onto lines, the break falls by width alone. In a label written with its years, it can break inside the date: "Roman Greece (146 or 27 BC–AD / 330)", "Minoan palatial Crete (c. / 1950–1450)", "Bronze Age collapse (c. / 1200–1150)", "Double-grip shield appears (c. / 700–675)". The P84 rule is that the years go on the last line.

How it should draw it: treat the trailing date expression as one unbreakable unit and put it whole on the last line. In a label drawn as written, the unit runs from the "(" that opens the years, or from "c."/"about" before them, to the end. In a label with its date appended, it is the appended ", <date>". Break the text before the unit. If the unit alone is wider than 220, break it only at its "–" or after "or". Expected results:

- "Roman Greece / (146 or 27 BC–AD 330)"
- "Minoan palatial Crete / (c. 1950–1450)"
- "Bronze Age collapse / (c. 1200–1150)"
- "Double-grip shield appears / (c. 700–675)"

## F2. greece/r-5.3 fig 2: Athens span label

Change the span's label from `Athens: Peisistratids (561/0–510, interrupted)` to `Athens: Peisistratids, interrupted (561/0–510)`.

## F3. greece/r-7.4 fig 1: era on the middle span

Change the span's label from `Imperial command with Macedonia and Moesia (15–44)` to `Imperial command with Macedonia and Moesia (AD 15–44)`.

## F4. rome/r-8.5 fig 1: cell tones against the single key

Give every filled cell the key's tone, which is the tone of the Hasding Vandals × Gallaecia cell. Change the tone of Sueves × Gallaecia, Alans × Lusitania, Alans × Carthaginiensis and Siling Vandals × Baetica to that tone. The one key "shared out by lot in 411" then matches every filled cell. The row labels already say who got which province.

## F5. ux-ia/read-ia6 fig 5: caption sentence

Replace `Blank cells: none, as in B.5's table.` with `A blank cell is "none" in B.5's table.`

## Sheets opened

- Desktop 1280, dark and light: all 23 figures (46 sheets).
- Phone 390, light: all 23 figures. Full frames, keys and captions included, for read-b4, read-pb2, rm85 fig 1, read-ia12 fig 2, read-ia6 figs 1 and 5, and rm44 fig 3. For the other timelines, the drawing area of every frame.
- Phone 320: rm104 fig 1 light, rm44 fig 3 light, read-b4 fig 1 dark.
- Zoomed crops and pixel measurements on desktop light for m111, m126, m33, m53 fig 4, rm137, rm44 and rm61; tone samples for read-b4 (dark and light) and read-ia6 fig 1.
- Phone dark sheets were not opened apart from read-b4 at 320. Desktop dark showed no problem that depends on the dark theme beyond the read-b4 note.
