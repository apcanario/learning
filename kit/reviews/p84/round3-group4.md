<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
PASS 16, FIX 1.
- read-dd-pb2 fig 1: the "Own digital product" row's opens and enters cells are drawn in the "her count only" key tone. The caption says keyed tones mark only the timeline column. Give them the blue row tone.
- m12 fig 3 (the clipped "the" in the 1952 label) is not in this packet, so I could not check it.
The harness refused the write to out/report.md, so the full report follows.

# r3-4 figure re-check

Checker: claude-opus-5-5. I read only from /home/claude/packets/r3-4. I checked positions by measuring pixels per year against the tick gridlines on the 1280 px sheets.

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-1.1 fig 1 (m11, timeline) | PASS | All five phases match the table's Evans ranges (c. 3100–1900, 1900–1700, 1700–1450, 1450–1300, 1300–1050) and sit at their years. Prepalatial and Protopalatial abut with a short gap. Minor: the Final Palatial label breaks in the middle of a phase name, "(LM II – LM / IIIA2),", but stays readable. Minor: at 390 and 320 px the in-bar Prepalatial label starts half under the right fade and is whole by the next scroll stop. |
| greece/r-1.3 fig 1 (m13, timeline) | PASS | All eight table rows are drawn at their years. Hattusa and Troy VIIa share 1180, with their labels stacked. Gridlines and guides break behind labels. Nothing is cut at 1280 or 390 px. |
| greece/r-1.3 fig 3 (m13, timeline) | PASS | The four phases (1190–1070, 1070–1025, 1025–900, 900–760) match the table. Minor: at 1280 px the last "C" of "Submycenaean, 1070–1025 BC" ends exactly on the x of the 900 BC guide. The guide breaks behind the label, so nothing overlaps, but the C reads as joined to the dashes. |
| greece/r-11.8 fig 2 (m118, timeline) | PASS | 323, 321 and 48 BC, AD 215, the 270s, 365, the 390s and c. 390 all sit at their years. The 1 BC to AD 1 step is one year: 100 BC to 1 BC is 99 years and 1 BC to AD 100 is 100, at even spacing. The figure is far wider than 115%, so it correctly scrolls. Minor: the 323 and 321 dots overlap. Minor: "Aurelian destroys the palace / quarter / (270s)" leaves "quarter" alone on its line, though "quarter (270s)" would fit on one. |
| greece/r-3.5 fig 3 (m35, timeline) | PASS | 467 (Laius and Seven), c. 442, c. 429, c. 409, 405 and 401 sit at their years. The span c. 442–401 matches the text's "forty years". At 390 and 320 px the in-bar label is whole at a middle scroll stop. |
| greece/r-6.3 fig 1 (m63, timeline) | PASS | All 17 events from 433 to 411 sit at their years, and the spans 431–421 and 415–413 are drawn with their labels. At 1280 px it correctly scrolls (390 px). At 320 px the taller in-bar label is whole at scroll 258. Minor: "From the outbreak to the Peace of / Nicias," splits "Peace of Nicias" across two lines. |
| greece/r-6.3 fig 3 (m63, timeline) | PASS | 410, 407, 406, 405, spring 404, the Thirty 404–403 with Phyle in winter 404/3, and autumn 403 all match the section. |
| greece/r-7.2 fig 2 (m72, timeline) | PASS | Ptolemy I (305–282) and Ptolemy II (282–246) are drawn with Aristophanes (c. 257–180), Aristarchus (c. 216–144), Zenodotus (fl. c. 280), the papyri after about 150 and the flight around 145. All sit at their years. |
| personal-brand-pb/read-dd-pb2 fig 1 (matrix) | FIX | All 27 cells match §3's nine lines. The keys are under the frame. At 390 and 320 px the row-label column is pinned. The fault: the "Own digital product" row uses the "her count only" key tone in all three cells, which contradicts the caption (see FIX 1). |
| ux-ia/read-ia6 fig 5 (matrix) | PASS | All 10 rows and 40 cells match the B.5 table. The tone-6 cells are exactly the caption's list of stops. It fits the desktop column. At 390 and 320 px it scrolls with the row labels pinned and the keys under the frame. Minor: the key swatches read "tone 3" and "tone 6" instead of sample text. The caption uses the same words, so it is consistent, but these are internal names. Optional fix: use "[no claims]" and "[no connection]" as the swatch texts. |
| rome/r-1.3 fig 1 (rm13, timeline) | PASS | 390 (approx.), Timaeus 350–260 (approx.), 300 (approx.), 200 (approx.), Cato 168–149 and 7 BC match the sections. Cato's guides break behind the Timaeus label. |
| rome/r-11.5 fig 2 (rm115, timeline) | PASS | All 13 events and 4 spans sit at their years: 106, 75, 70, 68, 63, 58–57, 56, 51–50, 49, 48–47, 45, 44–43 and 43. The Brundisium and Philippics guides break behind the "Cilicia, 51–50" label. |
| rome/r-13.5 fig 1 (rm135, timeline) | PASS | Spacing measured across 1 BC to AD 1 has no year 0: 4 BC is 4 years left of AD 1. All later events sit at their years. At 1280 px it correctly scrolls (134 px), being more than 15% over. Minor: the birth, "between about 4 and 1 BC", is a dot at 4 BC, the early end of the range. The label gives the range, so this is not wrong, but a short 4–1 BC span would show the uncertainty better. |
| rome/r-3.1 fig 2 (rm31, timeline) | PASS | 449, 445, 443, 421, 409, 405, 400 and the span 444–367 match the section. Minor: the in-bar label breaks onto three lines inside a 560 px bar. That follows the 220-unit rule. |
| rome/r-6.1 fig 1 (rm61, timeline) | PASS | Spacing measured across the BC/AD boundary is correct (2 BC to AD 4 is 5 years). The span 31–23 and all eight events sit at their years. Tick labels are centred on their gridlines. |
| rome/r-7.1 fig 2 (rm71, timeline) | PASS | AD 14, 15, 16, 17, 19, 23, 25, 27, 29, 31 and 37 match both sections. |
| rome/r-9.4 fig 2 (rm94, timeline) | PASS | 312, 272, 144, 125 and 33 BC and AD 52 sit at their years. 100 BC to AD 1 is 100 years and AD 1 to AD 100 is 99. |

## The m12 question (greece/r-1.2 figure 3)

m12 is not in this packet: figures.md does not list it, and there is no text or sheet for it. So I cannot say whether the tops of "the" in the 1952 label's second line are clipped at 1280 px, or whether anything in the drawing covers them. It needs a packet that includes its sheets.

## FIX 1: personal-brand-pb/read-dd-pb2 figure 1

In the "Own digital product" row, two cells are filled with the "her count only" key tone: "since 8 Jun 2027" (OPENS TO MARA) and "her net sales" (ENTERS THE MODEL AS). Measured: light (182,206,197), dark (25,52,51), the same as the key swatch. The other eight rows' non-timeline cells use the blue row tone: light (182,204,213), dark (31,44,54). Read by the key, those two cells would mean "a rate exists only from her own sales". But the caption says "Blue cells carry the row tone only; the two keyed tones mark the timeline column's readings."

Change to the declaration: set the "Own digital product" row's tone to the same blue row tone as the other eight rows. Keep the "her count only" tone only on that row's TIMELINE SOURCED cell, "her count only". If the green comes from cell tones on the two cells rather than from a row tone, remove the tone from "since 8 Jun 2027" and "her net sales". The caption then stands as written.

## Sheets opened

- Desktop 1280 dark and light: all 16 figures (32 sheets).
- Phone 390 light: all 16 figures.
- Phone 320 light: m11, m13 fig 3, m35 fig 3, m63 fig 1, read-dd-pb2, read-ia6, rm31.
- Phone 390 dark: none opened. Dark mode was checked on the desktop sheets, and nothing at phone width was marginal in colour.

Crops and two small PIL helpers (crop.py, frames.py) are in /home/claude/packets/r3-4/out/. I wrote nothing else there.
