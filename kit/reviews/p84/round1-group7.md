# p84-7 figure re-check (P84 timeline spans)

Checker: claude-opus-5-5, 17 Nov 2026. 17 figures: 13 PASS, 4 FIX.

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-10.10 fig 2 (m1010) | FIX | Troy VIIa's label prints as "TROY VIIA (VII)": uppercasing turns the text's "(VIi)" into "(VII)", which names a different layer. Troy III (2250–2200) and Troy IV (2200–1900) share a lane and a tone and touch, so they read as one bar. All other spans and years match the table in "The nine cities". |
| greece/r-10.4 fig 3 (m104) | FIX | The Ajax label prints "SOPHOCLES, AJAX (PROBABLY 440S), 449–440 BC": the years appear twice, the "s" comes out as "S", and the precise 449–440 drops the text's hedge. Events (c. 424, 415, 409) are correct. |
| greece/r-11.8 fig 2 (m118) | FIX | The span labels print "(270S), AD 270–279" and "(390S), AD 390–399": the years appear twice and the "s" comes out as "S". Events (323, 321, 48 BC, AD 215, 365, c. 390) are correct. Minor: the axis is long and mostly empty (10 phone frames); the year-0 tick reads "1 BC". |
| greece/r-11.8 fig 3 (m118) | PASS | Minor: the Droysen span prints "1836–1843" where the text has "1836–43". |
| greece/r-5.1 fig 1 (m51) | PASS | Minor: the span labels name both ends and are drawn as written, so they carry no "BC" and print "C." for c. Dates match the section and its dispute box. |
| greece/r-5.1 fig 3 (m51) | PASS | All dates match. The Dreros label sits inside its bar and is readable in dark and light. |
| greece/r-6.7 fig 1 (m67) | PASS | Curtius 1st century AD and Justin 2nd–4th century AD are drawn as written and their bars match. The Curtius label sits well to the left of its bar but is legible. |
| greece/r-6.7 fig 2 (m67) | PASS | All five phase spans (334–331, 331–330, 330–327, 327–325, 324–323) match the headings, and every event matches the text. |
| greece/r-6.7 fig 3 (m67) | PASS | "Nineteenth century: Droysen" is drawn as written over 1800–1900. Minor: the event labels use straight quotes. |
| greece/r-6.7 fig 4 (m67) | PASS | The spans 310 or 309 and by 306–305 are drawn as written, and the events are correct. |
| rome/r-1.5 fig 1 (rm15) | PASS | All seven reigns match the table, and the narrators' dates match the opening paragraph. The label plates mask the guides correctly. |
| rome/r-11.8 fig 3 (rm118) | FIX | The label prints "FIRST REPUBLIC, 450–367/6 BC, 450–366 BC": the renderer did not count "367/6" as an end and added the years again. The other spans (366–300 through 43–33) and the events (180, 139, 88) are correct. |
| rome/r-13.1 fig 1 (rm131) | PASS | The span "Epicureans: 173 or 154?" is drawn as written and sits at 173–154. The events are correct. |
| rome/r-3.4 fig 1 (rm34) | PASS | The wars 343–341, 326–304 and 298–290 match the text (peace in 290), and the events are correct. |
| rome/r-3.4 fig 2 (rm34) | PASS | The span "About nineteen Latin colonies, 334–263 BC" matches the text, and all colony dates are correct. |
| rome/r-7.5 fig 3 (rm75) | PASS | Boudica 60–61, the diaspora rising 115–117 and Bar Kokhba 132–135 match the text, and the Judaean war is at 66. |
| rome/r-9.5 fig 1 (rm95) | PASS | The span "Wolf cast, c. 1021–1153" is correct. Minor: the ticks read "AD 1, AD 500" but then "1000, 1500" with no "AD". |

## FIX: greece/r-10.10 figure 2 (m1010)

1. Declaration: the span label `"Troy VIIa (VIi)"` → `"Troy VIIa"` (drawn "Troy VIIa, 1300–1180 BC"). The uppercase rendering makes "VIi" read "VII", which is the wrong layer.
2. Renderer: when one span starts at the exact year another ends (Troy III ends 2200 and Troy IV starts 2200), lane assignment treats the touching spans as free to share a lane, and the two bars draw as one block of the same tone. Treat touching as overlapping when assigning lanes, so the later span goes up a lane, or else leave a visible gap (at least 2 px) between bars that touch in one lane.

## FIX: greece/r-10.4 figure 3 (m104)

Declaration: the span label `"Sophocles, Ajax (probably 440s)"` → `"Sophocles, Ajax (probably)"`. The renderer then draws "Sophocles, Ajax (probably), 449–440 BC", with the years once, the hedge kept and no "440S".

## FIX: greece/r-11.8 figure 2 (m118)

Declaration:
- the span label `"Aurelian destroys the palace quarter (270s)"` → `"Aurelian destroys the palace quarter"` (drawn "…, AD 270–279");
- the span label `"Anti-pagan violence (390s)"` → `"Anti-pagan violence"` (drawn "…, AD 390–399").

## FIX: rome/r-11.8 figure 3 (rm118)

Declaration: the span label `"First republic, 450–367/6 BC"` → `"First republic"`. The renderer then draws "First republic, 450–366 BC". The caption already says that 366 stands for the text's 367/6.

(Renderer alternative: count a split year such as "367/6" as naming an end. Then the label is drawn as written and the declaration stays.)

## Renderer note covering the FIXes above

Span labels are drawn in uppercase, and here case carries meaning: "VIi" becomes "VII", and "440s", "270s" and "390s" become "440S", "270S" and "390S". The declaration changes above fix every case in this packet. A lasting fix is to draw span labels without uppercasing, or to protect lowercase letters that follow a numeral or a roman numeral. The design rule may make this a theme.css matter, so it is raised here, not made a separate verdict.

## Sheets opened

- m1010 fig 2: desktop dark, desktop light, phone light (all frames, plus a zoomed crop of desktop light), phone320 dark.
- m104 fig 3: desktop dark, desktop light, phone light.
- m118 fig 2: desktop dark, desktop light, phone light.
- m118 fig 3: desktop dark, desktop light, phone light.
- m51 fig 1: desktop dark, desktop light, phone light.
- m51 fig 3: desktop dark, desktop light, phone light, phone320 dark.
- m67 figs 1, 2, 3 and 4: desktop dark, desktop light and phone light for each.
- rm15 fig 1: desktop dark, desktop light, phone light (plus a zoomed crop of frame 1).
- rm118 fig 3: desktop dark, desktop light, phone light.
- rm131 fig 1: desktop dark, desktop light, phone light.
- rm34 figs 1 and 2: desktop dark, desktop light and phone light for each.
- rm75 fig 3: desktop dark, desktop light, phone light.
- rm95 fig 1: desktop dark, desktop light, phone light.

Phone dark and phone320 light were not opened for figures where nothing was marginal. The layout matches across widths; only the scroll offsets change.
