<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
Counts: 15 PASS, 5 FIX.
FIX: read-a8 fig 3 has no conditional lawyer cell for R17. rm14 fig 1 needs "about"/"from" moved into the event dates. rm34 fig 2's caption names the wrong section for the citizen-colony dates. viz fig 19 breaks a long label so "line," sits alone on its own line (renderer). m12 fig 3: "the" is clipped at 1280 px and no visible part of the drawing covers it (renderer).
Report: the harness refused the write to out/report.md, so the full report follows. My zoom crops are in /home/claude/packets/r3-1/out/z/.

# Figure re-check r3-1

Checker: claude-opus-5-5. 20 figures: 15 PASS, 5 FIX.

| Figure | Verdict | Notes |
|---|---|---|
| brand-a/read-a8 fig 3 (matrix) | FIX | All drawn cells match register lines R1–R32, except one. R17's Professional column reads "Neither; lawyer if the DGC writes", and the Disclosure row has no lawyer cell. The key sits under the frame and is never scrolled or faded. Desktop fits the column. Phone pins the row-label column. Minor: R25's co-owner Shōmen has no column. |
| greece/r-1.2 fig 1 (timeline) | PASS | The five LH phases, the LH I high chronology, the palace destructions 1200–1180 and the takeover c. 1450 all match the Chronology table. Every span label carries its years. Readable at all widths. |
| greece/r-1.2 fig 3 (timeline) | FIX (renderer) | Data matches "Linear B and its decipherment": 1900, Kober in the 1940s, 1941, 1 July 1952, 1953 JHS 73 and 1956. The clipped "the" asked about is present at 1280 px in both themes. See the FIX section. |
| greece/r-1.2 fig 4 (timeline) | PASS | Madduwatta (fifteenth century), Alaksandu c. 1280, Tawagalawa c. 1250 and Shaushgamuwa c. 1220 all match the text. Readable at 390 and 320. |
| greece/r-3.1 fig 2 (timeline) | PASS | Pindar early 5th c., Pherecydes c. 450, Andromeda 412, Ovid 8 CE and Apollodorus 1st–2nd c. CE all match. I measured the tick gridlines. 100 BCE to 1 CE is spaced as 100 years, with no year 0. Events are placed to the pixel. |
| greece/r-3.7 fig 1 (timeline) | PASS | 438 BC, c. 100 BC, c. 29 BC and c. AD 8 all match the text and the "Ovid's method and agenda" section. Long labels wrap cleanly at 320. |
| greece/r-6.5 fig 1 (timeline) | PASS | All five spans match the table. The Thrasymachus in-bar label breaks onto two lines inside a taller bar, at both phone widths. |
| greece/r-7.1 fig 4 (timeline) | PASS | All dates match the section. Eucratides (170–145) and the Yuezhi (145–130) abut in one lane, with a visible gap at 145. The step from 50 BC to AD 1 measures 50 years. |
| greece/r-7.4 fig 1 (timeline) | PASS | All seven dates measured on the axis are exact, across 1 BC to AD 1. The "Imperial command…" label breaks with "(AD 15–44)" whole on its last line. Minor: the tick at -1 reads "1 BC" beside "AD 50". A tick at 1 ("AD 1") would read more naturally. Not wrong. |
| rome/home fig 1 (timeline) | PASS | All 3 bars and 11 events match Rome 3.1, including 421 (4.43), 409 and 172. Minor: the caption's "Licinian-Sextian" twice. The module says "Licinio-Sextian". Both forms are standard. |
| rome/r-1.4 fig 1 (timeline) | FIX | The dates match the text. The events read "200 BC / Fabius Pictor (about)", "7 BC / Dionysius (from)" and "AD 100 / Plutarch (about)". The qualifier is cut off from the date it qualifies. |
| rome/r-12.7 fig 1 (timeline) | PASS | All 12 works plus the 1953–1965 span match the three named sections. The stacking is dense but nothing overlaps at any width. |
| rome/r-13.8 fig 3 (timeline) | PASS | All 15 events and the 1601–1800 span match the text (Gataker 1652 in the transmission section, Casaubon 1634 in the first section). It is wider than the 15% limit, so it scrolls on desktop, which is correct. |
| rome/r-3.4 fig 1 (timeline) | PASS | The three wars and 17 events match both sections. |
| rome/r-3.4 fig 2 (timeline) | FIX | All placements are right. The caption's source sentence is wrong for the citizen colonies. See the FIX section. Minor: Sora and Interamna (313–312, named only by edge in the war section) are not drawn. Acceptable. |
| rome/r-8.5 fig 1 (matrix) | PASS | The lot of 411 matches Hydatius as the text gives it. The key sits under the frame. On the phone the row labels stay pinned while scrolling. |
| rome/r-9.5 fig 1 (timeline) | PASS | All dates match the Capitoline section. Minor: "1471 / Twins added after 1471" repeats the year. Setting date "after 1471" and label "Twins added" would be tidier. Optional. |
| viz-examples fig 19 (timeline) | FIX (renderer) | Spans carry their years as specified: written-out, "c." date, decade, century, 27 BC–AD 14. Kings and Republic abut with a gap at 509. Bad line break: the long label wraps as "…on one / line, / 4th century BC", leaving "line," orphaned on its own line. |
| viz-examples fig 20 (timeline) | PASS | Edge labels are aligned inward and nothing is cut at either end, at any width. Minor: the figure is about 1,670 px wide (desktop scrolls 972 px, phone 1,342 px) for four events at the two ends. If the renderer widens the axis to separate the dots 2 years apart (-500/-498, 199/200), that widening buys nothing, because the labels stack anyway. |
| viz-examples fig 28 (timeline) | PASS | Each date is drawn as given. I measured the ticks. The span from 100 BCE to 100 CE is spaced as 199 years, and 14 CE is exact. |

## FIX: brand-a/read-a8 figure 3

The register's R17 has Professional "Neither; lawyer if the DGC writes". The Disclosure (R17–R18) row has no lawyer cell, so the figure says no lawyer is ever involved there.

- Disclosure (R17–R18) row, LAWYER column: add the cell value `if DGC writes`, in the same tone as `if unclear`.
- Key: add the entry `if DGC writes` with the text `a lawyer only if the DGC writes about it`.

## FIX (renderer): greece/r-1.2 figure 3. The 1952 label at 1280 px

- **Seen?** Yes, in both the light and dark 1280 sheets. Second line of the 1952 label, "the BBC (1 July)": the ascenders of "t" and "h" are cut by a straight horizontal edge at about cap height. The pixel rows show the "h" stem starting only at x-height. The edge stops between "the" and "BBC", and the "B" is whole. The same line is whole at 390 px and 320 px.
- **Does anything in the drawing cover it?** Nothing visible. No bar, guide, line or plate lies at that spot. I boosted the contrast of the dark crop and found no plate edge there. The nearest drawn items are the 1953 stem (to the right of "(1 July)") and the label's own first line above it, and neither reaches "the".
- **What is left.** The cut is in the screenshot itself, with a hard edge and the same position in both themes. So it is either a background-coloured, invisible element drawn after that line (for example a label plate sized or placed for another line), or a clip produced by the desktop scaling (this figure is within 15% of 700 units, so it is scaled to the column). Either way it lies in the renderer, not in the declaration.
- **Change.** In the desktop-scaled timeline, make sure nothing is drawn over a wrapped event label's later lines. Draw all label plates before any label text, and size each plate from the line it belongs to. Then capture the 1280 frame again and confirm "the" is whole.

## FIX: rome/r-1.4 figure 1

Move each qualifier into the event's date, as the renderer already supports for fig 28.
- Event at -200: label `Fabius Pictor (about)` → label `Fabius Pictor`, date `about 200 BC`.
- Event at -7: label `Dionysius (from)` → label `Dionysius`, date `from 7 BC`.
- Event at 100: label `Plutarch (about)` → label `Plutarch`, date `about AD 100`.

## FIX: rome/r-3.4 figure 2

The caption says the dates come from the two war sections. Antium (338), Tarracina (329) and Minturnae and Sinuessa (296), and the span "334–263", are dated only in Colonies and roads as instruments of control.

Replace the caption's first sentence with: "Dated colony foundations named in this report, citizen colonies marked, the rest Latin: the citizen colonies' dates and the span of about nineteen Latin colonies, 334–263, from the section Colonies and roads as instruments of control; the Latin colonies' dates from The First and Second Samnite Wars, 343–304 and Sentinum and the end of Samnite independence, 298–264; the report cites Livy 8.22–23 for Fregellae and no passage for the other dates."

## FIX (renderer): viz-examples figure 19

When a side label wider than 220 units breaks, the renderer puts the trailing date on a line by itself even when the last words fit beside it. The result is "A long side label that a phone / frame could not show whole on one / line, / 4th century BC", which is the same at 1280, 390 and 320.

Change: keep the trailing date whole, but fill the last line greedily. Put the date on the same line as the preceding words when the two fit within the line width ("line, 4th century BC"), and start a new line only when they do not.

## Sheets opened

- Desktop light and dark (full or zoomed crops) for all 20 figures.
- Phone 390 light for all 20, in chunks.
- Phone 390 dark (overview) for m12 fig 3.
- Phone 320 dark for m12 fig 3, m12 fig 4, m37, m65, read-a8 (first and last frames), and viz 20 (end).
- Pixel measurements of tick and gridline positions on the desktop sheets for m31, m74, viz 28 and m12 fig 3.
