# p84-8 figure re-check (P84 timeline spans)

Checker: claude-opus-5-5. 17 figures. PASS 14, FIX 3.

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-10.11 fig 3 (m1011) | PASS | Finley 1000–800, Morris 800–700, Raaflaub/van Wees c. 750–650 match the table in "Four modern positions"; century labels get their years appended. Minor: "c. 750–650" is drawn as written without "BC" while the other two carry it. |
| greece/r-10.5 fig 3 (m105) | FIX | "Cult appears (7th century)" and "Stele to Menelaus (5th century)" have no years printed. Other spans correct (mansions 1450–1200, no use 1200–700); events c. 1450, c. 1200, c. 650 match the text. Minor: "Two Mycenaean mansions, 1450–1200 BC" drops the text's "c." (caption covers it). |
| greece/r-12.4 fig 1 (m124) | PASS | Academy 367–347 BC matches; events 384, 348, 348/7, c. 345, c. 341, 322 match. Minor: the 348 and 348/7 dots almost coincide; their leaders separate the labels. |
| greece/r-12.4 fig 4 (m124) | PASS | Avicenna AD 980–1037, Averroes 1126–1198, Aquinas 1225–1274; events 1210, 1215, 1255, 1270, 1277 all match. |
| greece/r-5.3 fig 1 (m53) | FIX | Years correct (double-grip c. 700–675, Chigi c. 650–640, Argos c. 720). But the long Chigi label runs left across the full width of the double-grip bar in the row above it. At 390 frames 1–2 and 320 frame 2 it is the only label in view, over the brown bar, with its own bar and years off-screen. |
| greece/r-5.3 fig 2 (m53) | PASS | Corinth c. 657–584, Sicyon c. 655–555, Mytilene c. 590–580, Athens 561/0–510, Samos c. 538–522 match the table; label plates cover the dashed guides. |
| greece/r-5.3 fig 4 (m53) | PASS | Span c. 640–560 matches the dispute; events c. 600, c. 550, from c. 515 match. |
| greece/r-7.4 fig 1 (m74) | FIX | Spans and events correct (146 BC, 44 BC, 27 BC–AD 15, 15–44, 44–67, AD 67), but the senate label prints its year twice: "Returned to the senate (44), AD 44–67". Minor: "(15–44)" has no AD beside a BC/AD axis. |
| greece/r-7.4 fig 2 (m74) | PASS | Measured: Plotinus 204/5–270, Porphyry c. 234–305, Iamblichus c. 245–325, Julian 361–363, Proclus 412–485; events 244, 432, 448 match. Minor: the caption does not name the three events (244, 432, 448). |
| rome/r-0.1 fig 2 (rm01) | PASS | Annals 14–68, Histories 69–96, HA 117–244 and 260–284 (the gap is shown), Amm. 353–378, events AD 30 and c. 390 all match. |
| rome/r-10.2 fig 2 (rm102) | PASS | Annals 14–68, Histories 69–96, Tacitus about 56 to about 120; events 88, 97, 98 match. |
| rome/r-12.1 fig 1 (rm121) | PASS | Eclogues c. 42–38, Georgics c. 36–29, Aeneid 29–19 BC; events 70, 55, 40, 29, after 23 and 19 match. Minor: "Aeneid, 29–19 BC" sits over the Georgics bar and "Georgics, c. 36–29 BC" under the Aeneid bar. Each label abuts its own bar and carries its years, so it reads correctly by row. Minor: "at Cremona" for the toga is implied by the text's sequence, not stated outright. |
| rome/r-13.4 fig 2 (rm134) | PASS | Vespasian 69–79, Domitian 81–96; events April 46 BC, 42, 59, 65, 66, 93 match. Minor: "93, after August" has no "AD" where the other events do. |
| rome/r-3.5 fig 1 (rm35) | PASS | Sicily 278–276; events 282, 280, 279, 278, 275 match. Minor: the year range is drawn from the start of 278 to the start of 276. |
| rome/r-5.6 fig 1 (rm56) | PASS | On the Republic 54–51, great burst 45–44; events 60, 56, 55, 46, 45, 44, 43 match. Minor: bars run from the start of the first year to the start of the last, so On Duties ("late in 44") sits at the burst's end rather than inside it. |
| rome/r-8.1 fig 2 (rm81) | PASS | Barbalissos, Antioch c. 252–253; events c. 240, 244, c. 256, 260 match. |
| rome/r-8.1 fig 3 (rm81) | PASS | Gallic emperors AD 260–274; events 270, 272, 274 match. |

All 17 do what CHANGE describes: spans sit on the axis with lane 0 lowest, dashed end-guides, tick labels above the top lane with gridlines, and labels on plates (checked by zoom: the plates cover the guides). They also read correctly in dark mode. Only m105 fails the years-on-every-span requirement.

## FIX 1 · greece/r-10.5 figure 3 (m105)

Problem: two century-named spans print no years. Morris's "Eighth century" in m1011 gets ", 800–700 BC" appended, but "(7th century)" and "(5th century)" do not. The renderer appears to treat a label containing a digit as already naming both ends.

Declaration change. These labels name both ends, so the renderer draws them as written:
- span label `"Cult appears (7th century)"` → `"Cult appears (7th century, 700–600 BC)"`
- span label `"Stele to Menelaus (5th century)"` → `"Stele to Menelaus (5th century, 500–400 BC)"`

Renderer note, so other figures are not hit the same way: count a label as naming both ends only if it contains both endpoint years (or a year range). Ordinal centuries such as "7th" should not count.

## FIX 2 · greece/r-5.3 figure 1 (m53)

Problem: the Chigi label is long ("Chigi olpe: earliest clear picture of massed ranks (c. 650–640)"). It covers the whole double-grip bar (700–675) in the row above it. On phone it shows over the wrong bar with its own bar and years scrolled out of view. The text's description is already in the caption ("the earliest picture of the phalanx … the Protocorinthian Chigi olpe").

Declaration change:
- span label `"Chigi olpe: earliest clear picture of massed ranks (c. 650–640)"` → `"Chigi olpe (c. 650–640)"`

At 1280 and 390 the shortened label ends clear of the double-grip bar. At 320 it may graze the bar's last few pixels, with its years beside it.

## FIX 3 · greece/r-7.4 figure 1 (m74)

Problem: the label names only one end, "(44)", so the renderer correctly appends ", AD 44–67". The year then prints twice: "Returned to the senate (44), AD 44–67".

Declaration change:
- span label `"Returned to the senate (44)"` → `"Returned to the senate"` (renderer prints "Returned to the senate, AD 44–67")

Optional, not required: `"Imperial command with Macedonia and Moesia (15–44)"` → `"Imperial command with Macedonia and Moesia"`. It would then print with AD, like its neighbour.

## Sheets opened

- Desktop light, all 17: sheets/desktop-*-light.png (m1011 f3, m105 f3, m124 f1, m124 f4, m53 f1, m53 f2, m53 f4, m74 f1, m74 f2, rm01 f2, rm102 f2, rm121 f1, rm134 f2, rm35 f1, rm56 f1, rm81 f2, rm81 f3).
- Desktop dark, all 17: sheets/desktop-*-dark.png.
- Phone 390 light, all 17: sheets/phone-*-light.png. Opened as crops; m1011 at full scale, the rest at 0.55.
- Phone 320 light, marginal cases: sheets/phone320-m53-fig-01-timeline-frames-light.png, sheets/phone320-m105-fig-03-timeline-frames-light.png.
- Phone dark and the other 320 sheets: not opened. Nothing in the desktop-dark or 390 checks was marginal in a way that depends on theme.
