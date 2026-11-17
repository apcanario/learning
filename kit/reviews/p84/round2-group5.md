<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
19 PASS, 3 FIX.
FIX rome/r-1.3 fig 1: the 390 point's label does not name Heraclides (declaration).
FIX rome/r-6.4 figs 1 and 2: the renderer counts a year 0 between 1 BC and AD 1, so every interval across the era boundary is one year too long.
Report path: the harness refused the write to /home/claude/packets/r2-5/out/report.md, so the full report follows below.

# Figure re-check r2-5 (P84 timelines, P109 matrices)

Checker: claude-opus-5-5. Read only inside /home/claude/packets/r2-5.

| Figure | Verdict | Notes |
|---|---|---|
| brand-b/read-b8 fig 1 (matrix) | PASS | Every row and cell matches the table "B2 §2, claim by claim" (13 Holds, 2 Changed with "Ultra, 10x weekly" and "up to 1M, disputed", 1 Not checked). The key sits under the frame and is whole at 1280, 390 and 320. Its swatch matches the marked cells (same pixel colour). Row labels stay in view while the grid scrolls on phone. It fits at 1280. Minor: in dark, marked cells are only slightly lighter than unmarked ones, but the dot carries the mark. |
| greece/r-1.1 fig 1 (timeline) | PASS | All five phases and dates match the table. Spans sit on the axis in lanes, with dashed guides to the axis. Prepalatial and Protopalatial abut in lane 0 and a gap shows between them. Minor: the Final Palatial label breaks inside the phase name ("(LM II – LM / IIIA2),"). |
| greece/r-10.3 fig 2 (timeline) | PASS | Sixth century (hoplites), after the Persian Wars 480–400 (Phrygian cap) and the fourth century (uniform) match "Are the Trojans foreign?". The points (after 480, c. 424 Hecuba, 415 Trojan Women) match the text. The century labels are drawn as written. Readable at every width. |
| greece/r-11.3 fig 2 (timeline) | PASS | Artaxerxes III r. 359/8–338, Arses 338–336, Sidon 345, Egypt 343/2, and the 338 and 336 events all match Diodorus as the text gives him. The caption carries the doubt about the 338 poisoning. Minor: "(r. 359/8–338)" has no "BC", unlike the other labels. |
| greece/r-11.3 fig 3 (timeline) | PASS | Every date matches the text: Darius III 336–330, the Sogdian revolt 329–328, and the points from 334 to 324. Pixel positions check out. |
| greece/r-3.4 fig 1 (timeline) | PASS | Pindar 462, Apollonius plotted at 250, Valerius bar AD 70–90 (measured at AD 70 and AD 90). Minor: the last tick label "AD 100" is pulled left inside the frame and sits right over the AD 70–90 bar. The bar is also off by the renderer's extra year at the era boundary (see rm64), under 4 px at this scale. |
| greece/r-5.4 fig 1 (timeline) | PASS | Conquest bar measured at 735–715. Revolt "mid-seventh century", 465/4, 421 and 369 all match. The gridline is broken under the span label. |
| greece/r-6.4 fig 2 (timeline) | PASS | Pixel-measured: Aeschylus 525–456, Sophocles 496–406, Euripides 485–406. Points at 484, 468 and 458. All follow the caption's "earlier year" rule and the sections' dates. |
| greece/r-7.1 fig 1 (timeline) | PASS | Points at 317, 316, 312, 311, 309 and 308. The span "Alexander IV and Roxane murdered, 310 or 309" is drawn 310–309. All match Diodorus as the text gives him. |
| greece/r-7.1 fig 2 (timeline) | PASS | Points from 302 to 272 and Pyrrhus in Italy 280–275 all match "Ipsus, 301, and Corupedium, 281". |
| greece/r-7.1 fig 3 (timeline) | PASS | Gonatas 277–239, Chremonidean War 268–261, Doson 229–221, Philip V 221–179. Points at 224, 222, 217, 215, 197, 168 and 148. All in lanes and all match. |
| greece/r-7.1 fig 4 (timeline) | PASS | Eucratides c. 170–145 and the Yuezhi c. 145–130 abut in one lane with a visible gap. Menander c. 155–130. The points match. Minor: the renderer's extra year at the BC/AD boundary moves the AD 10 point by about 2 px (see rm64). |
| rome/r-1.3 fig 1 (timeline) | FIX | Dates are correct (390, 350–260, 300, 200, 168–149, 7 BC). But the 390 point is labelled only "Gallic sack (approx.)". The caption says the figure shows Heraclides' report of the sack, and the figure is about when the stories were written, so the drawing should name him. Minor: Hellanicus ("late fifth century") is dated in the text but is not plotted, and the caption does not say so. |
| rome/r-11.4 fig 2 (timeline) | PASS | All 14 points from 63 to 32 and the Perusine war 41–40 match the text (Fulvia's death in 40 from Plutarch, Antony 30). The figure scrolls 134 px at 1280. Readable on phone. Minor: "Perusine war, 41–40" has no "BC". |
| rome/r-12.4 fig 4 (timeline) | PASS | Augustine about 397–400 and Marlowe 1587–1593 are spans. Dante sits inside the fourteenth century. The 1678–1689 group and Berlioz 1856–1890 are stacked and readable at 1280 (after a 112 px scroll) and at 390. |
| rome/r-13.8 fig 3 (timeline) | PASS | Every date is in the text, including 1634 and 1652 from earlier sections. The one span, "Becomes a classic, 17th–18th centuries", is drawn as written across 1601–1800. Readable at every width. |
| rome/r-4.5 fig 4 (timeline) | PASS | Livius 240, Naevius 235, Plautus c. 205–184, Ennius 204 and 184, Terence 166–160, Adelphoe 160. All match and are readable. |
| rome/r-6.4 fig 1 (timeline) | FIX | Every label and year is in the text. But the renderer counts a year zero between 1 BC and AD 1 (measured: 10 BC to AD 1 = 170 px at 15.45 px a year, which is 11 years; it should be 10). The Pannonian revolt is therefore drawn one year too far from the BC events. |
| rome/r-6.4 fig 2 (timeline) | FIX | Same renderer error: 10 BC to AD 1 is 170 px at 15.4 px a year. AD 7, AD 9 and AD 14–16 sit one year too far from 16 BC, 12–9 BC, 9 BC and c. 4 BC. Labels and years otherwise match the text. |
| ux-ia/read-dd-ia1 fig 7 (matrix) | PASS | Every cell matches the text's list for figure 7. Both keys sit under the frame, are whole at every width, and match the cells exactly (sampled pixels identical in light and dark). Row labels stay in view. It fits at 1280. Minor: tones 2 and 6 are very close, light (220,197,175) against (212,201,175), dark (73,53,40) against (70,61,42). The Strain column is set apart by position anyway. |
| ux-ia/read-dd-ia1 fig 8 (matrix) | PASS | Every cell and tone matches the text's list for figure 8. The three keys are whole at 1280, 390 dark and 320. Row labels stay in view. Minor: the tone 2 and 6 contrast is low (as in fig 7), but each tone-6 cell also says "none in the pages read". |
| ux-ia/read-ia7 fig 5 (matrix) | PASS | Matches the B.1 table. The nine keys sit under the frame and are whole at every width (390 light, 320 dark), and they match the tone-4 cells. Row labels stay in view. It fits at 1280. Minor: the blank (gray) cell has no key. The caption explains it. |

Counts: 19 PASS, 3 FIX.

## FIX: rome/r-1.3 figure 1 (declaration)

In the point dated 390, change the label:
- `"Gallic sack (approx.)"` → `"Gallic sack (approx.), reported by Heraclides"`

(Optional. It only clears a minor note and the figure passes without it: add to the caption, after "Dionysius' Roman Antiquities of 7 BC.", the sentence "Hellanicus (late fifth century) and Aristotle are not plotted.")

## FIX: rome/r-6.4 figures 1 and 2 (renderer)

What it draws wrong: the timeline scale maps a BC year y to −y and an AD year y to +y, so it counts a year 0 that does not exist. Every interval that crosses the era boundary is one year too long. Measured: in fig 1 and fig 2, 10 BC to AD 1 is 170 px at about 15.4 px a year, which is 11 years; the true span is 10. The same error is in greece/r-3.4 fig 1 (100 BC to AD 1 drawn as about 101.6 years) and greece/r-7.1 fig 4, where it is under 4 px.

How it should draw: map BC year y to 1 − y (astronomical numbering: 1 BC = 0, 10 BC = −9) and AD year y to y. Apply this to ticks, span ends, guides and points alike. The declarations need no change. After the fix, re-check rm64 figs 1 and 2. r-3.4 fig 1 and r-7.1 fig 4 shift by under 4 px.

## Sheets opened

- read-b8 fig 1: desktop light and dark; phone light; phone320 light.
- m11 fig 1: desktop light and dark; phone light (all frames); phone dark.
- m103 fig 2: desktop light and dark; phone light.
- m113 fig 2: desktop light and dark; phone light.
- m113 fig 3: desktop light and dark; phone light.
- m34 fig 1: desktop light (zoomed) and dark; phone light.
- m54 fig 1: desktop light (zoomed) and dark; phone light.
- m64 fig 2: desktop light (pixel-measured) and dark; phone light.
- m71 figs 1, 2, 3 and 4: desktop light and dark; phone light.
- rm13 fig 1: desktop light and dark; phone light.
- rm114 fig 2: desktop light and dark; phone light.
- rm124 fig 4: desktop light and dark; phone light.
- rm138 fig 3: desktop light and dark; phone light.
- rm45 fig 4: desktop light and dark; phone light.
- rm64 fig 1: desktop light (pixel-measured) and dark; phone light.
- rm64 fig 2: desktop light and dark; phone light.
- read-dd-ia1 fig 7: desktop light and dark (pixel-sampled); phone light; phone320 light.
- read-dd-ia1 fig 8: desktop light and dark; phone dark; phone320 light.
- read-ia7 fig 5: desktop light; phone light; phone320 dark.
