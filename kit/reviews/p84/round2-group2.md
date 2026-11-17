# r2-2 figure re-check report

Checker: claude-opus-5-5. 22 figures: 16 PASS, 6 FIX.

| Figure | Verdict | Notes |
|---|---|---|
| brand-a/read-a8 fig 3 (matrix) | FIX | (B) holds: the keys sit under the frame at 1280/390/320, whole, not faded. Every cell's tone matches its key, checked by pixel in light and dark. Row labels stay in view while scrolling. Data: the Tax row (R1–R12) is wrong against the register (see FIX 1). |
| greece/r-0.1 fig 1 (timeline) | FIX | Dates match "Material sources" and "The archaic poets". (A) holds except the line breaks. "Linear B at Knossos (c. 1400–1370 / BC)" and "Homer (conventionally c. 750–700 / BC)" break inside the years, leaving "BC)" alone on the last line at every width (see FIX 2). |
| greece/r-0.1 fig 2 (timeline) | FIX | Aristarchus span "2nd c. BC" has no date in the text, and he sits in "Compilers and transmitters", not "The archaic poets" (FIX 3). Pausanias' label breaks as "(c. AD / 150–180)" (renderer, FIX 2). The other 14 spans and points match the text. |
| greece/r-10.8 fig 4 (matrix) | PASS | Cells match the hero sections and "Cults, colonies and the uses of Troy". Keys whole and tone-matched at every width. Row labels stay in view. |
| greece/r-12.4 fig 1 (timeline) | PASS | Minor: Fall of Olynthus (348) and Plato dies (348/7) share one dot, with their labels stacked. This is readable. |
| greece/r-12.4 fig 4 (timeline) | PASS | All dates match "Afterlife" and line 79 (1270). Guides break at the Averroes label plate. |
| greece/r-4.3 fig 4 (timeline) | PASS | Every vase and play date matches its section. Minor: wrapped labels leave a trailing comma at the end of a line ("others," / "Etruria,") before the years line. |
| greece/r-6.3 fig 1 (timeline) | PASS | 433–411, both spans and 17 points match. It scrolls at 1280 (390 px), which is acceptable. |
| greece/r-6.3 fig 3 (timeline) | FIX | Span 404–403 is labelled "The Thirty; Phyle (winter 404/3)". The split year is drawn as written, so the Thirty read as dated winter 404/3 only (FIX 4). Points match. |
| greece/r-7.3 fig 1 (timeline) | PASS | 281–272 matches "Pyrrhus in Italy". |
| greece/r-7.3 fig 4 (timeline) | PASS | All 7 spans and 8 points match. Guides break at label plates. Minor: in dark, the Perseus and Aquinas-type blue bars have low contrast but are visible. |
| personal-brand-pb/read-dd-pb2 fig 1 (matrix) | FIX | Keys whole, under the frame, tone-matched. But the blue cells (two of the three columns) have no key and the caption does not explain them. "RPM" is not in the text (FIX 5). Every other cell matches §3 items 1–9. |
| rome/r-0.2 fig 1 (timeline) | PASS | Roads and colonies match. Via Egnatia c. 146–120 is drawn as written. |
| rome/r-0.2 fig 2 (timeline) | PASS | All 14 provinces and Caesar's Gaul 58–50 match. It scrolls at 1280 (198 px). |
| rome/r-0.2 fig 3 (timeline) | PASS | Rhine 58–55, 53, 20, AD 9, AD 14, AD 117 match. |
| rome/r-13.4 fig 2 (timeline) | PASS | Minor: the point date "93, after August" lacks the "AD" the other AD points carry; could be "AD 93, after August". |
| rome/r-3.5 fig 1 (timeline) | PASS | 282–275 and the Sicily span 278–276 match. |
| rome/r-5.5 fig 1 (timeline) | PASS | Three spans and 11 points match. |
| rome/r-7.5 fig 3 (timeline) | PASS | 60–61, 66, 115–117, 132–135 match "The limits of the system". |
| rome/r-9.5 fig 1 (timeline) | PASS | 78 BC, 69/70, 455, c. 1021–1153, 1471, 1546 match "The Capitoline". |
| ux-ia/read-ia10 fig 2 (matrix) | PASS | Scales to fit at 1280. Keys whole at every width. Row labels stay in view. The empty cells agree with 3.1 (sales: no wireflow or state diagram; leadership: no F3). Minor: all four keys share the row tone, so they differ only by word, and the caption's "tone 5" is internal wording. |
| ux-ia/read-ia5 fig 7 (matrix) | PASS | All 17 rows checked against table C.2 and the module list M-01–M-27: every req/opt mark is correct. Keys whole. Minor: "Rows tone 1" in the caption is internal wording. |

## FIX 1 · brand-a/read-a8 fig 3: declaration
The register's Professional column for R1, R3, R4 and R6–R12 is "Accountant", not "Accountant confirms" (that applies only to R2 and R5). R3 and R8 have Owner = Accountant. The cell "confirms", with the key "a contabilista certificado confirms it", understates the role. The caption also says "Every assignment is the register's own".
- Tax and social security row, Accountant cell: label "confirms" → "acts".
- Key: replace "confirms" / "a contabilista certificado confirms it" with "acts" / "a contabilista certificado does the line or confirms it, and owns R3 and R8". Keep the same tone.

## FIX 2 · renderer: breaking a long span label
When a label beside its bar is wider than 220 units, the renderer breaks it by width only. If the label already carries its years (as written, e.g. "(c. 1400–1370 BC)"), the break can fall inside the date. The result is "…(c. 1400–1370" / "BC)" (r-0.1 fig 1: Linear B at Knossos and Homer) and "…(c. AD" / "150–180)" (r-0.1 fig 2: Pausanias). This breaks CHANGE's "its years on the last [line]".
Fix: treat the trailing date expression as one unbreakable unit. That is the final parenthesis holding a year, or the text after the last comma that holds a year. Break only before it, so the whole date goes on the last line. If the unit alone is wider than 220, put it on its own last line, whole.

## FIX 3 · greece/r-0.1 fig 2: declaration
The Aristarchus span (label "Aristarchus, editor of Homer", date "2nd c. BC") is not dated anywhere in the report. Line 57 only says the A-scholia "go back to Aristarchus". Remove that span. In the caption, change "the Homeric Hymns; Aristarchus and the scholia)" to "the Homeric Hymns)". The figure keeps its 14 other entries.

## FIX 4 · greece/r-6.3 fig 3: declaration
Span 404–403, label "The Thirty; Phyle (winter 404/3)" → "The Thirty, 404–403 BC; Phyle seized winter 404/3". The text has the Thirty appointed after the spring-404 terms and ended by the autumn-403 amnesty, and Phyle seized "in winter 404/3".

## FIX 5 · personal-brand-pb/read-dd-pb2 fig 1: declaration
- YouTube ads row, "Enters the model as" cell: "0 until her own RPM" → "0 until both thresholds met". The text says "enters at zero until her Studio shows both thresholds met, then at her own revenue per thousand views"; "RPM" is nowhere in the text.
- Caption: add a final sentence, "Blue cells carry the row tone only; the two keyed tones mark the timeline column's readings." Without it, the blue cells in two of the three columns are the one tone with no key.

## Sheets opened
- Desktop 1280 light, all 22.
- Desktop 1280 dark, all except m63 fig 1, rm02 fig 2, read-a8 and read-ia10 (their light sheets were checked; the dark of read-a8 was checked by pixel sampling).
- Phone 390 light: m01 fig 1, m01 fig 2, m108 fig 4, m124 fig 1, m124 fig 4, m43 fig 4, m63 fig 1, m63 fig 3, m73 fig 4, rm02 fig 2, rm134 fig 2, read-a8 fig 3, read-dd-pb2 fig 1, read-ia10 fig 2, read-ia5 fig 7.
- Phone 320 light: read-a8 fig 3.
- Not opened: phone 390 light for m73 fig 1, rm02 figs 1 and 3, rm35, rm55, rm75, rm95; phone dark sheets; the other 320 sheets. Nothing in their desktop sheets was marginal.
