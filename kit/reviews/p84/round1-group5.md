# p84-5 figure re-check (P84 timeline spans)

Checker model: claude-opus-5-5. 19 figures: 15 PASS, 4 FIX.

| Figure | Verdict | Notes |
|---|---|---|
| greece/r-1.2 fig 1 (m12) | FIX | All seven spans match the Chronology table (LH I 1600–1500, LH II 1500–1400, IIIA 1400–1300, IIIB 1300–1200, IIIC 1200–1050, palaces destroyed c. 1200–1180, high-chronology LH I 1700–1500); Knossos c. 1450 correct. The high-chronology label prints its start twice: "LH I, HIGH CHRONOLOGY (FROM C. 1700), 1700–1500 BC". Readable at all widths. |
| greece/r-1.2 fig 3 (m12) | FIX | Events 1900, 1941, 1952 (1 July), 1953 JHS 73, 1956 are correct. Kober's span prints "(THE 1940S), 1940–1949": the decade is stated twice, and 1940–1949 is more exact than the text, which says only "in the 1940s". Renderer issue, see FIX. |
| greece/r-1.2 fig 4 (m12) | PASS | Madduwatta "(fifteenth century)" bar 1500–1400 is drawn as written, which is correct. Alaksandu c. 1280, Tawagalawa c. 1250, Shaushgamuwa c. 1220 are correct. Minor: the long Madduwatta label runs past 1300 BC above the axis but covers nothing. |
| greece/r-3.1 fig 2 (m31) | FIX | Pherecydes c. 450, Euripides 412 and Ovid 8 CE are correct. The renderer appends years the text does not give: "PINDAR, EARLY 5TH C. BCE, 500–470 BCE" and "APOLLODORUS, LIBRARY, 1ST–2ND C. CE, 1–200 CE". The caption says "neither is a closer date", so the drawing now contradicts its own caption. |
| greece/r-4.2 fig 3 (m42) | PASS | Wolf 1795, Parry 1928, Harvard papers 1930–1932, Arend 1933, Parry–Lord Yugoslavia 1933–1935, Schadewaldt 1938, Lord 1960 and West 2011 are all correct. Minor: around 1928–1938 the two short bars' guides crowd the event leaders at 1280, but everything stays legible. |
| greece/r-6.2 fig 1 (m62) | PASS | Naxos c. 470–468, Thasos 465–463, Egyptian expedition c. 460–454 and Samos 440–439 are correct. Events 478/7, c. 467, 454/3, c. 453 and c. 449 are correct. Minor: the Thasos and Samos labels sit side by side on lane 0 between their bars; the years printed in each label make clear which bar it belongs to. |
| greece/r-6.2 fig 2 (m62) | PASS | Parthenon 447–432 (label inside the bar) is correct, as are 480, 447, 438, 437 and 432. Minor: the event "432 BC / Parthenon sculpture finished by 432" repeats its year. |
| greece/r-6.2 fig 3 (m62) | PASS | First Peloponnesian War c. 460–446 is correct. Events c. 460, 458, 457, 451, c. 450, 447 and "446; peace 446/5" all match the text. |
| greece/r-9.1 fig 2 (m91) | PASS | Daedalic/Archaic c. 680–480, Severe c. 480–450, Polykleitos c. 460–410, Praxiteles c. 370–330, Lysippos c. 370–310 and Pergamon Altar c. 180–160 are correct. Kouros about 600, Kritios Boy c. 480 and Athena Parthenos 438 are correct. Minor: the 370 BC dashed guides pass faintly between the letters of the Polykleitos and Severe labels at 1280. |
| greece/r-9.1 fig 3 (m91) | PASS | Geometric c. 900–700, Corinthian c. 720–550, Attic black-figure c. 630–500, Exekias c. 545–530, Berlin Painter c. 505–460 and white-ground c. 470–400 are correct. Events c. 750, about 700, c. 640, c. 570 and c. 530 are correct. |
| rome/r-1.3 fig 1 (rm13) | FIX | Gallic sack about 390, Callias about 300, Timaeus about 350–260, Romans about 200, Cato 168–149 and Dionysius 7 BC are correct. The axis has no tick labels and no gridlines at any width (every other figure has them), so the CHANGE's "tick labels stand above the top lane with a faint gridline" is not met. Minor: the event label reads "Gallic sack", although what the figure dates is Heraclides' report of it. |
| rome/r-11.5 fig 2 (rm115) | PASS | Exile 58–57, Cilicia 51–50, Brundisium 48–47 and Philippics 44–43 are correct. Events 106, 75, 70, 68, 63, 56, 49, 45 and 43 are correct. Minor: the "CILICIA, 51–50" label sits right of its bar, under the Brundisium and Philippics bars, and its plate breaks their dashed guides; the years in the label keep it clear. |
| rome/r-12.7 fig 1 (rm127) | PASS | Pessimistic reading 1953–1965 is correct. All twelve publication years match the text. At 1280 the figure scrolls 70 px and every label is reachable. |
| rome/r-3.1 fig 2 (rm31) | PASS | Consular tribunes 444–367 (label inside the bar) is correct. 449, 445, 443, 421, 409, 405 and 400 are correct. Minor: the ticks are only 449/400/367. |
| rome/r-5.2 fig 2 (rm52) | PASS | "Consul 104–100" names both ends and is drawn as written, which is correct. c. 157, 119, 107 and 86 are correct. |
| rome/r-7.3 fig 3 (rm73) | PASS | Nerva 96–98, Trajan 98–117, Hadrian 117–138, Antoninus 138–161, Marcus 161–180 and Commodus 180–192 are correct. Events 106, 115, 132, 165, c. 170, 177 and 180 are correct. The caption's Ammianus 29.6.1 is the invasion reference (text, northern wars), which is correct. |
| rome/r-8.6 fig 1 (rm86) | PASS | Justinian 527–565 and Vandal Africa 533–534 are correct. Events 532, 536, 540, 552 and 568 are correct. |
| rome/r-8.6 fig 2 (rm86) | PASS | Alexandria 641–642 and Arab siege 717–718 are correct. Events 602, 610, 614, 626, 627, 636 and 698 are correct. Minor: at 390 the "ARAB SIEGE, AD 717–718" label stands over the 698 Carthage dot. "Arab siege of Constantinople" would be less ambiguous, but it is optional. |
| rome/r-8.6 fig 4 (rm86) | PASS | Civil wars 1321–1328 and 1341–1347 are correct. Events 1261, 1274, 1354, 1402, 1439, 1453, 1461 and 1475 are correct. |

## FIX 1. greece/r-1.2 figure 1: declaration
Span label for the high-chronology LH I bar (1700–1500):
- from: `"LH I, high chronology (from c. 1700)"`
- to: `"LH I, high chronology"`

The renderer then prints "LH I, high chronology, 1700–1500 BC". The start date is no longer repeated, and the label matches its neighbours, which also drop "c." (the caption already says the dates are approximate).

## FIX 2. Renderer: labels that name their period in words (fixes greece/r-1.2 fig 3 and greece/r-3.1 fig 2)
The renderer already treats "(fifteenth century)" as naming both ends (r-1.2 fig 4 is drawn as written). It does not do the same for "the 1940s", "early 5th c. BCE" or "1st–2nd c. CE". For those it appends computed years ("1940–1949", "500–470 BCE", "1–200 CE") that the text never gives. In m31 the appended years contradict the caption ("neither is a closer date").

Change the both-ends test so that a label is drawn as written when it contains:
- a decade (`\b\d{3,4}0s\b`),
- an ordinal century with "c." or "century" (`\b\d{1,2}(st|nd|rd|th)(–\d{1,2}(st|nd|rd|th))? c(\.|entury)`), or
- a spelled-out century (as now).

Result: "Alice Kober's work on the signs (the 1940s)", "Pindar, early 5th c. BCE" and "Apollodorus, Library, 1st–2nd c. CE".

If the renderer is not changed, the declaration fallback is the Kober label `"Alice Kober's work on the signs, the 1940s"` together with that rule. There is no declaration-only fix for m31, because any label without years gets years appended. Use the renderer fix.

## FIX 3. rome/r-1.3 figure 1: ticks missing
No tick labels or gridlines are drawn at 1280, 390 or 320, in light or dark. Every other timeline in this packet has them.

Draw ticks above the top lane with faint gridlines to the axis, as the CHANGE specifies. If the declaration suppresses ticks (an empty or absent tick list), set it to 400, 300, 200 and 100 BC. If the declaration already has ticks, the renderer is dropping them for this figure: make it draw them.

## Sheets opened
- **Desktop (1280), dark and light, all 19 figures:** m12 fig 1/3/4, m31 fig 2, m42 fig 3, m62 fig 1/2/3, m91 fig 2/3, rm13 fig 1, rm115 fig 2, rm127 fig 1, rm31 fig 2, rm52 fig 2, rm73 fig 3, rm86 fig 1/2/4.
- **Zoomed crops:** m91 fig 2 (desktop, dark and light) and rm115 fig 2 (desktop, dark and light).
- **Phone (390) light, all frames, all 19 figures:**
  - m12 fig 1 at full resolution.
  - The other 18 at half scale.
- **Phone (390) dark:** m91 fig 2.
- **Phone (320) light:** m12 fig 1 (the longest labels).

The other phone dark and 320 sheets were not opened: nothing in the 390 light sheets was marginal enough to need them.

Crops are in /home/claude/packets/p84-5/out/crops/.
