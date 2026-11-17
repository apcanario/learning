<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
12 PASS, 5 FIX:
- m35 fig 3: span label needs "c. 442–401 BC".
- m56 fig 1: Theognis label never fits on a phone; change it to "Theognis, 6th c. (600–501 BC)".
- rm03 fig 1: "c. 1000 BC" and "451–450 BC"; span labels "Conquest and civil war", "Crisis and late empire".
- rm03 fig 2: "Convention, 31 or 27 BC", since the text gives either/or, not a period. rm138 fig 3: label → "Becomes a classic, 17th–18th centuries", because the current label runs far past its bar and is never whole on a phone.
Report not written: the tool refused to let a subagent write /home/claude/packets/p84-3/out/report.md. The full text follows; please save it there.

# p84-3 figure re-check (P84 timeline spans)

Checker: claude-opus-5-5. All positions were measured against the tick scale on the 1280 sheets. Every bar and point falls on the year the text gives, and every bar's two ends drop to the axis by a dashed guide.

| Figure | Verdict | Notes |
|---|---|---|
| greece r-0.3 fig 1 (m03) | PASS | All ten periods sit on their table years. Labels that name both ends are drawn as written ("Archaic (c. 800 or 776 – 480)", "Hellenistic (323–31/30)", "Roman Greece (146 or 27 BC–AD 330)"). Readable at every width. |
| greece r-10.2 fig 4 (m102) | PASS | "Grave Circle A shaft graves, c. 1600–1450" and "Trojan War dates, c. 1300–1180" are right; the second names the range of proposed dates, not a period, and its label says "dates". Points 1300, 1250, 1220, 1184/3 and 1180 are right. |
| greece r-11.3 fig 2 (m113) | PASS | "Artaxerxes III (r. 359/8–338)" and "Arses (Artaxerxes IV), 338–336 BC" are right; the points 345, 343/2, 338 and 336 are right. Minor: on phone frame 1 the in-bar label is cut, but it is whole from frame 2 on. |
| greece r-11.3 fig 3 (m113) | PASS | "Darius III, 336–330 BC" and "Sogdian and Bactrian revolt, 329–328 BC" are right; the events 334, 333, 331, 330, 329 and 324 are right. Minor: the renderer draws a span "329–328" from 329.0 to 328.0, so it is one year wide. It does this the same way in every figure. |
| greece r-3.5 fig 3 (m35) | FIX | The span label drops the "c." the text gives Antigone (c. 442). |
| greece r-5.6 fig 1 (m56) | FIX | Theognis' label is wider than the phone viewport and is never whole in any frame at 390 or 320. It also says the century twice. The years are right (6th c. = 600–501). Other bars and points are right. Minor: Pindar, Bacchylides and Simonides have no comma before their years, unlike Theognis. |
| greece r-5.6 fig 3 (m56) | PASS | All seven life spans and the four points (585, 546, 515, 500) are right, and every label is readable at every width. |
| greece r-7.2 fig 2 (m72) | PASS | The reigns 305–282 and 282–246 and the editors c. 257–180 and c. 216–144 are right; the points 280, 150 and 145 are right. Minor: at phone widths the long Aristophanes label is cut by the frame edge, but it reads across adjacent scroll positions. |
| greece r-8.3 fig 3 (m83) | PASS | "Theodosian laws ban sacrifice, AD 391–392" is right; the points 369, 385, 393, 426, 522 and 551 are right. Minor: the one-year bar is only about 3 px wide on desktop. |
| greece r-9.3 fig 3 (m93) | PASS | "Aldine Aristotle, 1495–1498" is right; the points 1484, 1492, 1498, 1502, 1503, 1504 and 1513 are right. |
| rome r-0.3 fig 1 (rm03) | FIX | All five blocks and all twenty dates are on their years. Two printed event dates lose what the table says, and two span labels read as lists that run into the comma before their years. |
| rome r-0.3 fig 2 (rm03) | FIX | The span now reads as a period, "Convention, 31–27 BC". The text gives alternatives: "the convention of 31 or 27". The points 146, 133, 88, 60, 49, 43, 27 and 23 are right. |
| rome r-0.3 fig 3 (rm03) | PASS | "Transition, AD 439–568" is right; the points 439, 476, 493, 534 and 568 are right. Readable at 320. |
| rome r-13.8 fig 3 (rm138) | FIX | The span label (63 characters) runs far past its bar, over 1800–2000, among the 19th- to 21st-century events. It is never whole at 390 or 320, and on desktop frame 1 it is cut. All 14 points and the 1601–1800 span are right. |
| rome r-4.5 fig 4 (rm45) | PASS | "Plautus, c. 205–184" and "Terence, 166–160" are right; the points 240, 235, 204, 184 and 160 are right. |
| rome r-7.1 fig 1 (rm71) | PASS | All seven spans match the table; the points 31 and 46 are right. Minor: the plate for "Gaius, AD 37–41" sits in lane 0 over AD 41–54, which pushes Claudius up to lane 1. The reigns therefore do not all share one row, but every label carries its years. |
| rome r-7.1 fig 4 (rm71) | PASS | "Boudica, 60 or 61" is drawn as written; "Greek tour, AD 66–67" is right; the points 54, 55, 59, 62, 64, 65, 66 and 68 are right. |

Counts: 12 PASS, 5 FIX.

## FIX: greece r-3.5 figure 3 (m35)
Span label:
- current: `Sophocles's three Theban plays, 442–401 BC`
- replace with: `Sophocles's three Theban plays, c. 442–401 BC`

The text gives Antigone "c. 442 BC", and the caption says "c." marks an approximate date. The new label names both ends, so the renderer draws it as written.

## FIX: greece r-5.6 figure 1 (m56)
Theognis span label:
- current: drawn "Theognis, 6th c. (date uncertain), 600–501 BC"
- replace with: `Theognis, 6th c. (600–501 BC)`

The new label names both ends and fits the phone viewport. The caption already says Theognis' date is disputed (the Suda gives c. 540).

## FIX: rome r-0.3 figure 1 (rm03)
Event dates as printed:
- `1000 BC` (First graves in the Forum) → `c. 1000 BC`
- `451 BC` (Twelve Tables) → `451–450 BC`; the point stays at 451.

Span labels:
- `Conquest, civil war` → `Conquest and civil war`
- `Crisis, late empire` → `Crisis and late empire`

These match the text's "conquest and civil war 264–27" and "crisis and late empire 235–476".

## FIX: rome r-0.3 figure 2 (rm03)
Span label:
- current: drawn "Convention, 31–27 BC"
- replace with: `Convention, 31 or 27 BC`

The new label names both ends, so it is drawn as written. It keeps the text's either/or.

## FIX: rome r-13.8 figure 3 (rm138)
Span label:
- current: `The book becomes a classic, seventeenth and eighteenth centuries`
- replace with: `Becomes a classic, 17th–18th centuries`

The new label is short enough to sit inside the 1601–1800 bar at every width, and it names both ends. The caption already quotes the text's phrase and gives 1601–1800.

## Sheets opened
- 1280 light: all 17 figures.
- 1280 dark: all 17, as montages; m113 fig 2 and m83 fig 3 also zoomed.
- 390 light: all 17.
- 320 light, where a label looked marginal: m72 fig 2, m56 fig 1, rm03 fig 3.
- 390 light, zoomed: rm138 fig 3 (all frames) and rm03 fig 1 (frames 9–10).
- Not opened: phone dark (390 and 320 dark). The desktop dark sheets show no dark-only problem.
