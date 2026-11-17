<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
22 figures checked: 20 pass, 2 need a fix.
FIX rome/home fig 1 (declaration): "consular tribunes" starts at 449 but should start at 444, and the "Tables, 494–449" bar wrongly dates the Tables. Also a renderer problem: the timeline is 6 px too wide at 1280, so it scrolls on desktop.
FIX read-dd-ia3 fig 4 (renderer): on desktop the grid still scrolls, and the row labels scroll out of view. They stay pinned on the phone but not on desktop.
The harness refused the write to out/report.md, so the full report follows below.

# r2-7 figure re-check report

Checker: claude-opus-5-5. Rechecked against P84 (timelines) and P109 (matrices).

| Figure | Verdict | Notes |
|---|---|---|
| building-with-ai-bw/read-bw5 fig 2 (matrix) | PASS | Every mark matches the build order in Deliverable 1b (rows BW3–BW10, columns BW1–BW9). The key sits under the frame, matches the cell tone, and is whole at 320, 390 and 1280. Row labels stay pinned on phone. |
| greece/r-1.3 fig 1 (timeline) | PASS | All 8 table rows are on their dates. Spans sit on the axis with their years, and guides break at labels. Minor: Ugarit is drawn in a different tone that the caption doesn't explain. |
| greece/r-1.3 fig 3 (timeline) | PASS | The phases match the table, and LH IIIC/Submycenaean leave the abutment gap. Minor: at 1280, the label "Submycenaean, 1070–1025 BC" touches the 900 guide. |
| greece/r-11.6 fig 1 (timeline) | PASS | Matches the table, 330–324, and Sogdiana/Swat leave the abutment gap. Minor: "Spring 329" repeats the year in the stem label. |
| greece/r-12.8 fig 2 (timeline) | PASS | Bars use the earlier year as the caption says. Events at 268, 155, 110/09 and 88 match the text. |
| greece/r-12.8 fig 4 (timeline) | PASS | Bars and events (200, 415, 529, 532, 565) match the text. Minor: event labels repeat their year ("AD 415 / Hypatia murdered, 415"), and *Against Proclus* is not in italics. |
| greece/r-5.6 fig 1 (timeline) | PASS | Matches the table, with Theognis as the 6th century (600–501), which the caption explains. Minor: "Pindar c. 518–438" has no comma, while "Theognis, 6th c." does. |
| greece/r-5.6 fig 3 (timeline) | PASS | All spans and floruits match the text. Guides break at labels (checked zoomed in). |
| greece/r-7.2 fig 2 (timeline) | PASS | The reigns, the editors' dates, c. 150 and c. 145 match the text. Minor: two labels put the years in brackets where the others use a comma. |
| greece/r-8.3 fig 3 (timeline) | PASS | 369, 385, 391–392, 393, 426, 522 and 551 match the text, and the dispute box exists. Minor: the 391–392 bar is a sliver, but its label gives the years. |
| greece/r-9.3 fig 3 (timeline) | PASS | All dates (1484 to 1513) match the text. |
| rome/home fig 1 (timeline) | FIX | See below. |
| rome/r-1.5 fig 1 (timeline) | PASS | The reigns match the table, and the narrators' dates match the opening paragraph. |
| rome/r-11.6 fig 1 (timeline) | PASS | Books 1–7 run 58–52 and book 8 runs 51–50. The events match the table and text. |
| rome/r-11.6 fig 3 (timeline) | PASS | 1828, 1855, 1861–65, 1865, 1901, 1903 and 1991–97 match the text. The Reddé label wraps with its years on the last line. Minor: titles in the event labels are not in italics. |
| rome/r-3.1 fig 2 (timeline) | PASS | The 444–367 span and the events at 449, 445, 443, 421, 409, 405 and 400 match the text. |
| rome/r-3.1 fig 3 (matrix) | PASS | Matches the assemblies paragraph. Both new keys are whole at every width and match the cell tones. Row labels stay pinned on phone. |
| rome/r-7.2 fig 2 (timeline) | PASS | 66, 67, 70, 71, 73 or 74, and 80–81 match the text. |
| rome/r-7.2 fig 3 (timeline) | PASS | The reigns and events match the text, and Vespasian/Titus leave the abutment gap. |
| ux-ia/read-dd-ia3 fig 1 (matrix) | PASS | Cells match §1.2 word for word. The "tone 5"/"tone 3" key labels are what the text names its legend. The keys are whole at every width. |
| ux-ia/read-dd-ia3 fig 4 (matrix) | FIX | Every cell matches the A.2 table and its "stronger part" rules, and the 6 keys are whole. The fault is the desktop row labels; see below. |
| ux-ia/read-dd-ia3 fig 5 (matrix) | PASS | Matches the A.4 description. No key is needed (one tone). Row labels stay pinned on phone. Minor: the row labels leave out the RV IDs that the caption cites. |

## FIX: rome/home.html figure 1 (timeline)

Declaration changes:
1. Second span: change `"from": -449` to `"from": -444`. The label stays `"consular tribunes"` and will draw as "consular tribunes, 444–367 BC". Rome 3.1 says "from 444 military tribunes with consular power … until 367" (Livy 4.6.8), and Rome 3.1 fig 2 uses the same dates.
2. First span: replace `{"from": -494, "to": -449, "label": "Tables", "tone": 6}` with `{"from": -451, "to": -449, "label": "Decemvirs", "tone": 6}`. The current "Tables, 494–449 BC" dates the Twelve Tables to 494–449, which contradicts the caption's 451–449. Rome 3.1's own section is headed "The Decemvirate and the Twelve Tables, 451–449". The events at -494 and -451 stay.
3. Caption: add after the first sentence: "Bars: the decemvirate, 451–449; military tribunes with consular power in place of the consuls in about two years out of three, 444–367; the offices opened from the Licinian-Sextian laws to the lex Hortensia, 367–287."

Renderer change: at 1280 the figure is 6 px wider than its column, so it scrolls and shows "scroll sideways for the whole figure" on desktop. A timeline that overflows the desktop column slightly should scale to fit, as P109 now does for matrices up to 15% wider. Recheck after change 2.

## FIX: ux-ia/read-dd-ia3.html figure 4 (matrix)

Renderer change: at 1280 the grid is still 201 px wider than the column, more than the 15% that P109 scales away, so it scrolls. Once scrolled (frame 2 of 2), the row labels (New variant … Translate term) are out of view; only fragments like "cides" and "told" are left. On phone the row-label column stays pinned. It should also stay pinned on desktop whenever the grid scrolls. The declaration needs no change.

## Sheets opened

- Desktop 1280 light and dark: all 22 figures. Zoomed in on m13 fig 3, m128 fig 4 and m56 fig 3 to check that guides break at labels.
- Phone 390 light: every frame of all 22 figures (13 frames for read-dd-ia3 fig 4).
- Phone 320 light: read-bw5 fig 2 (frames 1–4) and m13 fig 1 (all frames).
- Text: around every marker in m13, m116, m128, m56, m72, m83, m93, rm15, rm116, rm31 (also the source for rome/home), rm72, read-bw5 (§4 and Deliverable 1b) and read-dd-ia3 (§1.2, A.2, A.4).
