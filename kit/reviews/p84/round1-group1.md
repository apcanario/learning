<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md ("Subagents should return findings as text"). -->

claude-opus-5-5
17 PASS, 4 FIX.
FIX: r-10.12 fig 2 Leontius "(1360s), 1360–1369" doubled and too precise · r-10.12 fig 3 Calvert "(1860s), 1860–1869" same · r-3.3 fig 2 labels are sentences that run 50–90 years past their bars and print "480s or 470s, 489–470" · viz-examples fig 1 "Scale, 2024–2027" prints a year still to come.
Report not written: the harness blocked the file write to /home/claude/packets/p84-1/out/report.md ("Subagents should return findings as text"). Its full content is below for you to save there. out/ is empty; my temporary crops are deleted.

# p84-1 figure re-check (P84 timeline spans)

Checker: claude-opus-5-5. Packet files only.

| Figure | Verdict | Notes |
|---|---|---|
| brand-a/read-dd-a1 fig 2 | PASS | Span "Abdaal: junior doctor, 2018–2020" matches §2 ("junior doctor from 2018 to 2020"), lane 0, guides drop to 2018 and 2020. Minor: events sit on whole years (15 May, June, 24 Oct 2017 share one dot at 2017.0; Boyd "by 11 Nov 2015" at 2015.0); events are unchanged by P84 and each label carries its exact date. |
| greece/r-10.12 fig 2 | FIX | Leontius span prints "Latin prose (1360s), 1360–1369": doubled, and 1360–1369 is more precise than the text ("in the 1360s"). On 390 px the long label runs on to about 1600 and reads as a period. Chapman Odyssey 1614–1615, Pope Iliad 1715–1720 and Odyssey 1725–1726 match the text. |
| greece/r-10.12 fig 3 | FIX | Same fault: "Calvert's trial trenches (1860s), 1860–1869". The text says only "in the 1860s". On the phone the label runs to about 1950. |
| greece/r-12.6 fig 1 | PASS | "Epicurus, 341–270 (module 7.2)" is drawn as written and matches the text. Minor: the 271/0 death dot sits just inside the bar's 270 end, which is consistent with the two datings the caption names. |
| greece/r-3.3 fig 2 | FIX | Years are right: Heracles c. 570–510, cycle cups c. 510–500, Bacchylides 480s/470s, Codrus cup c. 440–430. But the labels are sentences, so each beside-label runs 50–90 years past its bar. On phone and 320 px, frames 1–2 show "Bacchylides 17 and 18, probably 480s or 470s, 489–470 BC" alone over 560–500 BC, and the Codrus label sits over 480–445 BC. "480s or 470s, 489–470" is doubled, and 489–470 is spurious precision. |
| greece/r-5.4 fig 1 | PASS | "Conquest of Messenia, roughly 735–715" matches "Between roughly 735 and 715". |
| greece/r-6.4 fig 2 | PASS | Aeschylus c. 525/4–456/5, Sophocles c. 496–406/5 and Euripides c. 485/480–406 match the sections. Bars start and end at the earlier year, as the caption says. |
| greece/r-7.1 fig 1 | PASS | "Alexander IV and Roxane murdered, 310 or 309" is drawn as written. Minor: the 310–309 bar shows an either/or date, not a period; the label says so. |
| greece/r-7.1 fig 2 | PASS | "Pyrrhus in Italy, 280–275 BC" matches "after Italy (280–275)". |
| greece/r-7.1 fig 3 | PASS | Gonatas 277–239, Chremonidean War 268–261, Doson 229–221 and Philip V 221–179 match the text; bar ends pixel-checked against the event scale. |
| greece/r-7.1 fig 4 | PASS | Eucratides c. 170–145, Menander I c. 155–130 and Yuezhi c. 145–130 ("between about 145 and 130") match. Minor: these labels carry no "BC" on an axis that runs into AD. |
| rome/r-10.4 fig 1 | PASS | "Biondo, Roma instaurata, 1444–1446" matches "1444–46". |
| rome/r-10.4 fig 4 | PASS | Arc du Carrousel 1806–1808 and Vendôme column 1806–1810 match. |
| rome/r-13.5 fig 1 | PASS | "Corsica, 41–49" and "Withdrawal, 62–65" match the section headings. Withdrawal stacks to lane 1 because Corsica's label takes lane 0; both are readable at every width. |
| rome/r-4.3 fig 4 | PASS | "Hannibal in Italy, 218–203 BC" matches 218 and "left Italy in the autumn of 203" (Livy 30.20). |
| rome/r-6.1 fig 1 | PASS | "Consul every year, 31–23 BC" matches "a consulship Augustus held every year from 31 to 23"; bar pixel-checked 31→23. Minor: on 390 px frame 2 the label sits alone over 20–10 BC (see renderer note). |
| rome/r-8.5 fig 3 | PASS | "ESF programme, 1993–1998" matches. Minor: the label stretches over 1930–1990, above the Pirenne/Brown/Hodges dots; it reads correctly at 1280. |
| viz-examples fig 1 | FIX | "Scale, 2024–2027" now prints a year still to come, under a title "Perqo, 2018 to 2026". |
| viz-examples fig 17 | PASS | All four spans print the declared years; the stacking is correct. |
| viz-examples fig 18 | PASS | Overlaps stack correctly (Interval rises to lane 2 over the era); every label carries its years. |
| viz-examples fig 19 | PASS | "Kings, 753–509 BC", "A reign, c. 670–640 BC" (from "date"), "Republic, 509–27 BC" and "A principate, 27 BC–AD 14" show the CHANGE working. Minor: "Siege, 41–40" is drawn as written and carries no BC on an axis that crosses into AD (test data only). |

## FIX: greece/r-10.12 fig 2

Leontius Pilatus span:
- `"label": "Leontius Pilatus, Latin prose (1360s)"` → `"label": "Leontius Pilatus, Latin prose"`, and add `"date": "1360s"`. It prints "Leontius Pilatus, Latin prose, 1360s".

## FIX: greece/r-10.12 fig 3

Calvert span:
- `"label": "Calvert's trial trenches (1860s)"` → `"label": "Calvert's trial trenches"`, and add `"date": "1860s"`.

## FIX: greece/r-3.3 fig 2

Shorten the four span labels and move the years into `"date"`. Neils' 520s is already in the caption.
- Heracles span: `"label": "c. 570–510: Heracles outnumbers every other figure on Attic black-figure"` → `"label": "Heracles leads Attic black-figure"`, `"date": "c. 570–510 BC"`.
- Cycle cups span: `"label": "c. 510–500: Theseus cycle cups appear (Neils: earliest in the 520s)"` → `"label": "Theseus cycle cups"`, `"date": "c. 510–500 BC"`.
- Bacchylides span: `"label": "Bacchylides 17 and 18, probably 480s or 470s"` → `"label": "Bacchylides 17 and 18"`, `"date": "480s or 470s BC"`.
- Codrus span: `"label": "c. 440–430: Codrus Painter cup, BM E 84"` → `"label": "Codrus Painter cup, BM E 84"`, `"date": "c. 440–430 BC"`.

These old labels are read off the drawing, not the declaration: match them to its exact strings.

## FIX: viz-examples fig 1

Scale span: keep `"to": 2027` and add `"date": "2024 on"`, so it prints "Scale, 2024 on". Alternatively, `"date": "2024–2026"`.

## Renderer note (minor, no change required)

A beside-label much longer than its bar runs on over later years and, in phone frames, is often seen without its bar. Examples: rm61, rm85, m71 fig 1, m54, and m33. Possible improvement: when a beside-label is wider than about three times its bar, or crosses another bar's guide, place it above the bar or wrap it to two lines instead of running it along the lane. The declaration fixes above cure the only misleading case (m33).

## Sheets opened

- Desktop light: all 21 figures.
- Desktop dark: read-dd-a1-02, m33-02, m1012-02, m1012-03, m71-03, m71-04, viz-01, viz-17, viz-18, viz-19.
- Phone (390) light: read-dd-a1-02, m1012-02, m1012-03, m126-01, m33-02, m54-01, m64-02, m71-01, m71-02, m71-03, m71-04, rm104-01, rm104-04, rm135-01, rm43-04, rm61-01, rm85-03, viz-01, viz-17, viz-18, viz-19.
- Phone 320 dark: m33-02, viz-19.
