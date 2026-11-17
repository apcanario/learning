# Re-check r2-8: P84 timelines and P109 matrices

Checker: claude-opus-5-5. 22 figures. PASS 22, FIX 0.

| Figure | Verdict | Notes |
|---|---|---|
| read-bw7 fig 2 (matrix) | PASS | Rows and cells match the §4 division paragraph. Three keys sit under the frame, whole at 1280 and 390, and their tones match the cells exactly in light and dark (sampled). Fits at 390 without scrolling; row labels wrap and stay readable. |
| m1010 fig 2 (timeline) | PASS | Ten spans match the table in "The nine cities". Every label carries its years. Troy VI and VIIa are in their own tone, as the caption says. Minor: the table's "c." is not on the labels; the caption covers it ("Every date is approximate"). |
| m104 fig 3 (timeline) | PASS | *Ajax* is drawn as written ("probably 440s", decade rule). *Hecuba* c. 424, *Trojan Women* and *Palamedes* 415, *Philoctetes* 409 all match §"Sophocles", §"Euripides" and the Palamedes section. |
| m117 fig 1 (timeline) | PASS | Diodorus c. 60–30 BC, Plutarch c. AD 100–120, Arrian 2nd century, Justin 2nd–4th century, Curtius AD 41 and 323 BC all match the table and the caption. Trogus is not placed, as the caption says. |
| m117 fig 3 (timeline) | PASS | Minor: "Armenian, by the 5th century" and "Julius Valerius, early 4th century" are drawn as whole-century bars. That is acceptable because the caption says the figure is "by century". Walter of Châtillon (c. 1180) is not drawn; this is right, because the text says he follows Curtius, not the Romance. |
| m41 fig 2 (matrix) | PASS | Every cell checked against "Iphigenia". Apollodorus' fate cell is blank because that section gives no fate. The three keys are under the frame and whole at every width; their tones equal the cells (sampled, light and dark). Minor: the neutral blank tone and the "neither" tone are close in light, but the cells' text tells them apart. |
| m61 fig 1 (timeline) | PASS | c. 550, c. 546, 539, Cambyses 530–522, Darius 522–486, by 500 and 490 all match the text. |
| m66 fig 1 (timeline) | PASS | The spans carry their years. Split years are placed at the first year, as the caption says. "Spartan hegemony, 404–371" rests on the text's 404 and "Leuctra ended Spartan hegemony" (371). |
| m66 fig 3 (timeline) | PASS | 359, 358, 357, 354, 352, 348, 346, 340, 338 and 336 match the three sections. The Third Sacred War (356–346) and Philip's reign (359–336) carry their years. |
| m84 fig 2 (timeline) | PASS | "Stelai almost vanish (c. 500–430)" and "Family-group reliefs, c. 430–317" are drawn as written. Dexileos 394/3 and 317 Demetrius match the text. Phone frames read clean. |
| read-dd-pb1 fig 1 (matrix) | PASS | Cells match §9. Four keys sit under the scroller at 390, whole and outside the fade, with tones equal to the cells (sampled). Row labels stay in view in every frame. |
| read-dd-pb1 fig 2 (timeline) | PASS | Every date matches §3 to §10. The Anderson bar is labelled with its years, Sep 2016–Mar 2020. Minor: at 1280 the figure is 6 px wider than the column, so it scrolls and shows the "scroll sideways" hint. The matrix scale-to-fit rule (P109) does not cover timelines; extending it to them would remove this. |
| read-dd-pb1 fig 3 (matrix) | PASS | Cells match the at-a-glance table and §3 to §8 (for example, Wicks's cadence is "own", in his words via Campaign; Itsines's "earns" is "press", via Startup Daily). Four keys are under the frame with tones equal to the cells. Row labels stay in view at 390. |
| rm118 fig 3 (timeline) | PASS | All ten spans match "Flower: which republic fell?". Abutting spans stop short of each other. Long labels break onto lines with their years on the last line. The first republic is drawn as "450–367/6", as the caption says. |
| rm131 fig 1 (timeline) | PASS | 181, 161, 155 and 92 match the text. The Epicurean bar, "173 or 154?", names both ends, and the caption says the bar is not a duration. |
| rm33 fig 2 (timeline) | PASS | c. 437, 406, 398, 396 and the third war 406–396 match "Veii: the ten-year siege". |
| rm52 fig 2 (timeline) | PASS | c. 157, 119, 107, 104–100 and 86 match the section. The caption names the sources from other sections. |
| rm73 fig 3 (timeline) | PASS | All five reigns carry their years. 106, 115, 132, 165, c. 170, 177 and 180 match the sections. No spans overlap within a lane. |
| rm86 fig 1 (timeline) | PASS | 527–565, 533–534, 532, 536, 540, 552 and 568 match the Justinian section. |
| rm86 fig 2 (timeline) | PASS | 602, 610, 614, 626, 627, 636, 641–642, 698 and 717–718 match the text. Minor: the phone frames have tall empty space under the axis on the right because the staggered labels are on the left. Nothing is cut. |
| rm86 fig 4 (timeline) | PASS | 1261, 1274, the civil wars 1321–1328 and 1341–1347, 1354, 1402, 1439, 1453, 1461 and 1475 match "The Palaiologan revival". Minor: Mistra (1460) is not drawn; it is not needed. |
| read-ia9 fig 2 (matrix) | PASS | The grid matches §3.2 and IA2's table as the section reads it (for example, the inventory is F2 in Discover, per §1). The keys are under the frame and whole at 390. The single tone 5 matches the caption. |
| read-ia9 fig 6 (matrix) | PASS | The cells match §5 and Deliverable C, RV-01 to RV-12 (conditions in brackets for RV-03 and RV-06; triggers for RV-04, 05, 07, 08, 11 and 12). Row labels stay in view in every phone frame. It has no key because every cell is one tone named in its text; the caption says so. |

## FIX sections

None.

## Sheets opened

- Desktop light and dark: every figure.
- Phone 390 light, every figure. For the long sheets, the frames were cropped. Matrices: the first and last frames. Timelines: every frame.
- Crops at 1280 for m104, m117 fig 1 and fig 3, m66 fig 1, rm118, rm131, rm33, rm73 and rm86 fig 2.
- Pixel tone samples for keys against cells: bw7 fig 2, m41 fig 2, pb1 fig 1, pb1 fig 3, light and dark.
- The 320 and phone-dark sheets were not needed: nothing at 390 was marginal.
