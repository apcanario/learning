<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
27 figures checked: 24 PASS, 3 FIX.
FIX rome/r-12.1 fig 2 (matrix): at 1280 the grid scrolls and the row labels scroll out of view. Renderer fix: pin the row-label column at every width.
FIX rome/r-3.4 fig 2 (timeline): at 320 the in-bar label "About nineteen Latin colonies, 334–263 BC" never shows whole. Fix: label "About 19 Latin colonies", or the renderer wraps wide in-bar labels.
FIX ux-ia/read-ia4 fig 8 (matrix): the key swatches and the caption say "tone 5" and "tone 3". Fix: rename the keys and reword the caption.
The harness refused the write to out/report.md, so the full report follows.

# r2-1 figure re-check (P84 timelines, P109 matrices)

Checker: claude-opus-5-5. 27 figures. PASS 24, FIX 3.

| Figure | Verdict | Notes |
|---|---|---|
| brand-a/read-a1 fig 2 (matrix) | PASS | Cells match §6: season label in the title, no syllabus, miss named, artefact not reached. Keys sit under the frame, whole at 1280, 390 and 320, and their tones match the cells. Minor: at 1280 the "not reached" key wraps, leaving "it" alone on its second line. |
| building-with-ai-bw/read-dd-bw3 fig 2 (matrix) | PASS | Columns follow §3. Keys are whole, row labels stay pinned on the phone and the grid fits at 1280. Minor: "redone" in the Wrong tool row has the "group" tone, whose key reads "read against the task type"; the text reads it against the routing table. |
| greece/r-10.11 fig 3 (timeline) | PASS | Finley 1000–800, Morris 800–700 and Raaflaub/van Wees c. 750–650, as in the table. Finley and Morris abut in lane 0 with the gap. Minor: at 320 the in-bar label "Finley: tenth to ninth century" is whole only at scroll positions between the sampled frames. |
| greece/r-10.5 fig 3 (timeline) | PASS | 1450, 1200, no use 1200–700, cult in the 7th century, aryballos c. 650 and the 5th-century stele, all as in the text. Guides and gridlines break at labels. |
| greece/r-11.8 fig 2 (timeline) | PASS | 323, 321, 48 BC, AD 215, the 270s, 365, c. 390 and the 390s, as in the text. Undated visits are left out, as the caption says. |
| greece/r-11.8 fig 3 (timeline) | PASS | All publication years match the text. At 390 the Droysen span label breaks onto three lines with its years on the last. |
| greece/r-4.2 fig 3 (timeline) | PASS | 1795, 1928, 1930–32, 1933, 1933–35, 1938, 1960 and 2011, as in the text. Minor: the two bars of 2–3 years are thin at 1280 but readable. |
| greece/r-6.2 fig 1 (timeline) | PASS | 478/7, c. 470–468, c. 467, 465–463, c. 460–454, 454/3, c. 453, c. 449 and 440–439, as in the text. |
| greece/r-6.2 fig 2 (timeline) | PASS | 480, 447, 447–432, 438, 437 and 432, as in the text. |
| greece/r-6.2 fig 3 (timeline) | PASS | c. 460, 458, 457, 451, c. 450, 447, 446 and 446/5, as in the text. Minor: at 320 the in-bar label "First Peloponnesian War, c. 460–446" (about 240 css px) is never whole in a sampled frame and only just fits between the fades. The renderer fix in FIX 2 would cover it. |
| greece/r-9.1 fig 2 (timeline) | PASS | c. 680–480, c. 480–450, c. 460–410, c. 370–330, c. 370–310, c. 180–160, about 600, c. 480 and 438, as in the text. Daedalic and Severe abut with the gap. |
| greece/r-9.1 fig 3 (timeline) | PASS | All style and painter dates match "Vase painting". Red-figure is drawn as an event at c. 530, as the caption says. |
| rome/r-0.1 fig 2 (timeline) | PASS | Annals 14–68, Histories 69–96, HA 117–244 and 260–284 with the gap, Amm. 353–378, AD 30 and c. 390. Minor: the two HA spans sit in different lanes (lane 2 and lane 0), so the gap reads less clearly as a gap in one work. |
| rome/r-10.2 fig 2 (timeline) | PASS | About 56 to about 120, 88, 97 and 98. Annals 14–68 and Histories 69–96 abut with the gap. |
| rome/r-12.1 fig 1 (timeline) | PASS | 70, 55, 40, c. 42–38, c. 36–29, 29, 29–19, after 23 and 19, as in the text and caption. |
| rome/r-12.1 fig 2 (matrix) | FIX | Data correct: D for odd poems, S for even; pairs 1–9, 2–8, 3–7, 4–6; 5 the middle; 10 the close. Keys are whole under the frame at every width, and row labels stay pinned at 390 and 320. At 1280 the grid scrolls (258 px) and the row labels scroll away with it (frame 2, dark and light). |
| rome/r-3.4 fig 1 (timeline) | PASS | All dates match the two sections, with the Via Appia at 312. Minor: at 1280 the figure scrolls by only 70 px. |
| rome/r-3.4 fig 2 (timeline) | FIX | Dates correct: 338, 329, 328, 314, 296, 291, 273, 268 and 263, and about nineteen Latin colonies in 334–263. At 320 the in-bar label is about 282 css px, wider than the frame between its fades, so it is never readable whole. |
| rome/r-7.4 fig 3 (timeline) | PASS | 193–211, 211–217, 217–218, 218–222, 222–235, 197, 212, c. 224 and 232, as in the text. Severus and Caracalla abut with the gap. |
| rome/r-9.3 fig 4 (timeline) | PASS | c. 135, 104 and 73–71, as in the text. Minor: the 104 event reads "Salvius, Athenion" without saying the second Sicilian war began then; the caption carries that. |
| ux-ia/read-ia1 fig 4 (matrix) | PASS | Roles and surfaces match section 5. The new keys are whole at every width and match the cell tones. Minor: on phones the third key's text wraps to four short lines. |
| ux-ia/read-ia4 fig 8 (matrix) | FIX | All twelve rows match table B.3. Keys are whole, tones match, row labels stay pinned and the grid fits at 1280. But the key swatches read "tone 5" and "tone 3", and the caption says "Rows tone 5 … tone 3 marks". These are renderer terms the reader cannot interpret. |
| viz-examples fig 1 (timeline) | PASS | Matches the declaration. Abutting spans are separated and every span label carries its years. |
| viz-examples fig 17 (timeline) | PASS | Matches the declaration. Every short span carries its years. |
| viz-examples fig 18 (timeline) | PASS | Matches the declaration. Overlapping spans are stacked with no collisions. |
| viz-examples fig 19 (timeline) | PASS | "Siege, 41–40" and "A decade (280s)" are drawn as written, and "A reign" takes its date "c. 670–640 BC". "A principate, 27 BC–AD 14" carries its years. The long label breaks onto lines with "4th century BC" last. Kings and Republic abut with the gap. |
| viz-examples fig 8 (matrix) | PASS | Matches the declaration, and the keys are whole at every width. Minor: "own team" has no key. In light mode the tone-6 "export" cells (rgb 212,201,175) are close to the empty-cell fill (215,209,197), so only the mark text tells them apart. |

## FIX 1: rome/r-12.1 figure 2 (matrix), renderer

What it draws wrong: at 1280 the matrix is more than 15% wider than the column, so it scrolls by 258 px. The row-label column scrolls with the cells. Scrolled to the end, none of the seven row labels ("Form" … "Gallus, lovesick in Arcadia, given a farewell") is in view. At 390 and 320 the same column stays pinned.

How it should draw it: pin the row-label column at every width where the grid scrolls, not only at phone widths. That means the same sticky first column with its opaque background, with the left fade starting after it. A desktop reader scrolled to columns 7–10 then still sees which row each "pair", "middle" and "close" belongs to.

## FIX 2: rome/r-3.4 figure 2 (timeline), declaration or renderer

Declaration: in the span 334–263, change "label": "About nineteen Latin colonies" to "label": "About 19 Latin colonies". It is then drawn as "About 19 Latin colonies, 334–263 BC", about 240 css px, which just fits at 320.

Renderer (the fuller fix): when a label inside a bar is wider than the scroller's visible width minus its two fades, break it onto two lines inside a taller bar, with the years on the last line. Side labels already follow this rule above 220 units. The other option is to keep the in-bar label inside the visible part of the bar as the frame scrolls. Either way it also covers the marginal 320 cases in greece/r-6.2 fig 3 and greece/r-10.11 fig 3.

## FIX 3: ux-ia/read-ia4 figure 8 (matrix), declaration

- Legend item "mark": "tone 5": change to "mark": "term". Its "means" stays "a catalogue term, shared across surfaces".
- Legend item "mark": "tone 3": change to "mark": "also listed". Its "means" stays "a cross-listing in the app, assumed".
- Caption sentence: replace "Rows tone 5, shared terms; tone 3 marks a cross-listing shown in the app, assumed and untested (IA3, section 3.3; rule R6)." with "Each row's cells give the item's shared catalogue terms; a filled cell in the last column is a cross-listing shown in the app, assumed and untested (IA3, section 3.3; rule R6)."

## Sheets opened

- **Desktop (1280), dark and light:** every figure, except these, opened light only: read-ia4-fig-08, rm34-fig-01, and viz-examples fig-17, fig-18 and fig-19. For rm121-fig-02 I also opened frame 2 of the dark sheet. I zoomed into m118-fig-02, m42-fig-03, m62-fig-01, m91-fig-02, rm01-fig-02 and viz-examples-fig-19.
- **Phone (390), light:** every figure, all frames.
- **Phone (320):**
  - rm121-fig-02, dark: frame 1 with its keys.
  - read-a1-fig-02, dark: first and last frames.
  - rm34-fig-02, m62-fig-03 and rm102-fig-02, light: all frames.
  - m1011-fig-03, m91-fig-02 and rm01-fig-02, light: the top part of every frame.
- **Phone (390), dark:** none.
- **Colour samples:** pixel colours from desktop-viz-examples-fig-08, dark and light.
