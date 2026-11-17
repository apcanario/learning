<!-- Saved verbatim by the H-4 chat from the agent's final reply: the agent's harness refused its write to out/report.md. -->

claude-opus-5-5
16 figures: 10 PASS, 6 FIX.
FIX: m73 fig 1 has colliding tick labels at both ends, and a gridline drawn over its span bar; m73 fig 4 has colliding tick labels "50 BC30 BC"; rome/home fig 1 has span labels "Tables" and "consular tribunes" whose new years name the wrong period; rm14 fig 1 prints Ennius as a false-precise 189–170 and reads "Livy (about)"; rm116 fig 3 and rm93 fig 4 have span labels that name people, so the years read as their dates.
The report did not get written. The harness refused to let me write /home/claude/packets/p84-6/out/report.md ("Subagents should return findings as text"), so the full report is below. out/ holds only scratch crops in out/tmp/.

# p84-6 figure re-check (P84 timeline spans)

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-1.3 fig 1 (m13) | PASS | All spans and events match the "What collapsed, and when" table: Thebes 1250–1225, Ugarit 1190–1185, Pylos/Mycenae/Tiryns/Midea 1190–1180, LH IIIC 1130–1070, plus 1208, 1180 ×2 and 1177. Plates cover the dashed guides. Minor: the 1100 gridline shows through the LH IIIC bar (FIX 1B). |
| greece/r-1.3 fig 3 (m13) | PASS | LH IIIC 1190–1070, Submycenaean 1070–1025, Protogeometric 1025–900, Early and Middle Geometric 900–760 all match the phase table. |
| greece/r-11.7 fig 1 (m117) | PASS | Diodorus c. 60–30 BC, Plutarch's Life c. AD 100–120, Arrian 2nd c. AD, Justin 2nd–4th c. AD, 323 BC and Curtius AD 41 all match the table and caption. |
| greece/r-11.7 fig 3 (m117) | PASS | Alpha 3rd c., Julius Valerius early 4th c., Armenian by the 5th c., Leo 10th c., Nizami 12th c., Syriac c. 630, Ferdowsi c. 1010: as the text gives them. Minor: "early 4th century" is drawn across the whole century (the caption says "by century"). The ticks mix "AD 200" with a bare "1000". |
| greece/r-4.3 fig 4 (m43) | PASS | All 5 spans (570–560, 520–470 ×2, 500–470, 449–440) and all 10 events match their sections, and the positions are correct. Minor: "probably 440s, 449–440 BC" gives the decade twice. |
| greece/r-6.3 fig 1 (m63) | PASS | Spans 431–421 (outbreak to the Peace of Nicias) and 415–413 (Sicilian expedition), and every event, match. The figure scrolls even at 1280. |
| greece/r-6.3 fig 3 (m63) | PASS | "The Thirty; Phyle (winter 404/3), 404–403 BC" matches: from the terms of spring 404 to the amnesty of autumn 403. Events 410–403 match. Minor: the label gives the years twice. |
| greece/r-7.3 fig 1 (m73) | FIX | Data correct. Tick labels collide at every width ("282 BC281 BC", "272 BC271 BC"). The 277 gridline runs through the Sicilian-detour bar and makes it look like two bars. |
| greece/r-7.3 fig 4 (m73) | FIX | All 7 spans and 8 events match. Tick labels "50 BC30 BC" collide at every width. |
| rome/home fig 1 (rome) | FIX | "Tables, 494–449 BC": the Tables are 451–449 and 494 is the secession. "consular tribunes, 449–367 BC": Rome 3.1 dates them "from 444". The caption does not mention the spans. |
| rome/r-1.4 fig 1 (rm14) | FIX | "Ennius, 189–170 BC" where the text says "180s and 170s". "Livy (about), 27–25 BC" misplaces "about". Everything else matches. |
| rome/r-11.6 fig 1 (rm116) | PASS | Books 1–7 58–52, Book 8 by Hirtius 51–50, and events 58–51 all match the table. Minor: years are drawn as points, so seven campaign years fill six intervals. |
| rome/r-11.6 fig 3 (rm116) | FIX | Years correct. The span label "Reddé and von Schnurbein, 1991–1997" names the people, not the excavations. |
| rome/r-3.3 fig 2 (rm33) | PASS | Third war 406–396, and c. 437, 406, 398 and 396, all match. Minor: the 400 gridline runs over the bar. |
| rome/r-5.5 fig 1 (rm55) | PASS | Philippics 44–43, Perusia 41–40, war with Sextus 38–36, and events 44–30 all match. |
| rome/r-7.4 fig 3 (rm74) | PASS | The five reigns 193–235 and events 197, 212, c. 224 and 232 all match. |
| rome/r-9.3 fig 4 (rm93) | FIX | "Spartacus, 73–71 BC" names the man. The text says "Spartacus' war of 73–71", and the events use "Eunus' war". |

## FIX 1: m73 fig 1, plus a renderer change for all figures
A. Renderer: if an edge tick label, once pinned inside the frame, would overlap the next tick label, do not print the edge label (keep its gridline). Or in the declaration: in "ticks", remove -282 and -271.
B. Renderer: draw gridlines beneath span bars, or stop each gridline at the top of the bar it meets. It also shows in m13 fig 1 (1100), rm33 fig 2 (400) and rome fig 1 (400), but only here does it split a bar.

## FIX 2: m73 fig 4
"ticks": remove -30 (the Egypt event already prints 30 BC at the end of the axis). FIX 1A also fixes this.

## FIX 3: rome/home fig 1
- Span 1: "label": "Tables" → "Secession to the Twelve Tables" (keep -494 to -449).
- Span 2: "from": -449 → -444; "label": "consular tribunes" → "Consular tribunes". Source, Rome 3.1: "from 444 military tribunes with consular power … until 367".
- Span 3: "label": "offices open" → "Offices opened, Licinian-Sextian laws to lex Hortensia" (367–287, as the section dates it).
- Caption: add "The bars mark the secession to the Twelve Tables (494–449), the consular tribunes (444–367) and the opening of the offices from the Licinian-Sextian laws to the lex Hortensia (367–287)."

## FIX 4: rm14 fig 1
- Ennius span: "label": "Ennius" → "Ennius' Annales, 180s and 170s BC". If the renderer's test for a label that already names both ends does not recognise decades, it should append nothing to any label that already contains a date.
- Livy span: "label": "Livy (about)" → "Livy, about 27–25 BC".

## FIX 5: rm116 fig 3
Span: "label": "Reddé and von Schnurbein" → "Reddé and von Schnurbein's excavations".

## FIX 6: rm93 fig 4
Span: "label": "Spartacus" → "Spartacus' war".

## Sheets opened
- Desktop dark and light for all 16 figures.
- Phone (390) light for all 16, with full-resolution crops for m13 fig 1, m43 and m73 fig 4.
- Phone320 light for rome (frames 1–2) and phone320 dark for rm14 (frames 1–3).
- Not opened: phone dark for every figure, and phone320 for the other 14. Nothing I saw was borderline.
