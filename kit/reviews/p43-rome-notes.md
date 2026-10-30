# P43 Rome · notes from the figure checkers (30 October 2026)

Backlog row N4 added figures to the 59 written Rome reports. Its checkers (fresh Opus 5.5 agents, one per report) were told to note anything wrong outside the figures and not to fix it. Nothing below was changed; the prose of every report is byte-identical to before N4. These are leads for a corrections pass (proposed row P54), not verified errors: each wants checking against the report and its sources before an edit. A second list records drawing faults in `viz.py` that the checkers met and worked around (proposed row P55).

## Prose and Self-test leads, by report

- **0.2** Self-test answer 10 repeats a phrase ("The battle of c. 496 in which Rome beat the Latins and the Tarquins" twice) and ends "on its side.." with a double full stop.
- **1.5** Self-test 3 adds Servius to the regal names unused in the Republic; the body (Cornell, in "Seven reigns for 244 years") names Numa, Tullus and Ancus.
- **1.6** Self-test 8, "before the fifth-century Volscian advance", against the body's "fit the sixth century, not the fourth".
- **2.1** Self-test 5 dates Livy 43.13 to 169; the body says only "that year".
- **2.2** Mars paragraph: "Seated with Venus in 217, Ares' adultery became…" (dangling participle). Vesta paragraph: "kept the form of a hut, was no inaugurated templum" lacks a conjunction.
- **2.3** The rex sacrorum "fled the Forum" in the body, "fleeing the Comitium" in Self-test 2.
- **2.4** Self-test 4 places the Penates in the "salt-cellar", which the body does not mention; "Servius says" in "The Lares" gives no passage.
- **2.5** Self-test 4 calls the Galli "Phrygian"; the body does not.
- **3.2** Self-test 6 cites Livy 8.9.6–9, the body 8.9.6–8; Self-test 8 cites Dionysius 8.55–56, the body 8.56.2.
- **3.4** Self-test 1 cites Livy 10.11–12 for 298 (the body cites module 0.1); Self-test 6 has the Senate uphold the exemption for Antium and Ostia in 207, which the body does not state.
- **4.1** Self-test 1, "before the Trojan War", against the body's "before the fall of Troy" (Appian).
- **4.2** Self-test 9, "the fleet of 242", a year the body does not give; Self-test 7 cites Polybius 1.37.4–6, the body 1.37.1–4; Self-test 8, "six years", against the body's three at Heircte and two at Eryx.
- **4.5** Self-test 10 gives Cato's fear as the young prizing eloquence over deeds; the body (Plutarch, Cato Maior 22) gives a different reason.
- **5.3** Self-test 2, "Appian gives 70,000 and then 120,000"; the body has about seventy gladiators and 120,000.
- **5.4** Self-test 6 hedges the Pharsalus figures ("about 15,000", "some 200") that the dispute box gives without a hedge.
- **5.6** Atticist dispute box: "Lysias' plainness.." (double full stop).
- **6.3** Self-test 6 gives "loyalty" as a theme of Odes 3.2; the body names only military hardiness. "The Organization of Opinion" (Syme's title) beside "organisation of opinion" later.
- **7.1** Philo, Embassy to Gaius, cited 8–21 in the body and 14–21 in Self-test 5.
- **7.2** Self-test 1, "Alexandria and Judaea", against the body's "Egypt and Judaea"; "ex manubis" in the Jewish War section (the usual form is manubiis, unless the inscription's spelling is quoted).
- **7.3** The diaspora revolt is 116 in the Trajan section and 115–117 in the Gibbon list; "the 10,000 gladiators of 107" gives a year the body does not (Dio 68.15.1); Self-test 7, "Britain and Mauretania", against "Britons, Moors, Germans and Dacians".
- **7.4** "Dio says … and that he himself" in the Severus Alexander section reads as Ulpian but means Dio; Dio "75(75).3.2–3" in the Severus section does not match the report's own book numbering (76(75) from 197).
- **7.5** Self-test 4, "about a hundred procurators", against the body's about 136 under Commodus.
- **8.1** First Decius dispute box: "his naked corpse" with no named antecedent.
- **8.2** Self-test 4 cites Lactantius 7.3, the body 7.3–4.
- **9.3** Self-test 4 credits the rule on dotal land to Augustus; the body cites Gaius 2.63 and names no one. Self-test 3, "could not receive gifts", against the body's "custom voided gifts between spouses".
- **10.1** Self-test 2 cites Caesar's star as Metamorphoses 15.843–850, the body 15.761–850 (narrower, not contradictory).
- **10.2** Self-test 2, "three years after Seneca's death", rests on a death year the body never gives.
- **13.2** "oikeiosis" in the prose, "oikeiōsis" in the table; the first dispute box cites "On Ends 4" with no passage.

## Drawing faults the checkers met in `viz.py`

None stops the build; each made a figure unreadable at phone width until the figure was changed or dropped.

- **timeline:** a span's label is drawn across its bar in the on-accent colour, so on a short span the label spills onto the page and vanishes (1.5, 5.6, 7.4, 8.6); spans that overlap in time share one row and their bars and labels collide (5.6, 7.1, 10.2); an event label near the left edge runs off the drawing (6.4); a tick at 0 is drawn as "AD 0" (1.6).
- **compare and bars:** a row label wider than the 170-unit label column is clipped (3.4, 11.1); values print without thousands separators (770000); a word unit prints with no space ("1200words", 1.2).
- **tree:** with nine or ten leaves the boxes shrink to about 64 units and labels break mid-word (9.1, 10.2); a narrow tree draws in the left half of the 700-unit frame (2.1, the P50 family).
- **objects:** a long attribute in a two-column grid wraps letter by letter (4.5).
- **range:** years BC print as negative numbers (3.5).

## P57: what was restored and what was kept (30 October 2026)

Backlog row P57 revisited the 14 reports above whose figures N4 reshaped or dropped around these drawing faults, all fixed by P55 (content drops were left alone). For each, a fresh Opus 5.5 agent read the report, a note of which fault had touched which figure, the figure contract and `skills/write-unit` §4b, and decided from the report's own text whether the original shape was the better figure; where it was, it redrew it from the text (no original spec survived). A separate fresh agent checked every change; the two FIXes (7.4, 10.2) were re-checked and passed. None failed twice. The prose of every report is byte-identical and no word count moved.

Restored in the original shape (12 figures):

- **1.5** figure 1: the seven kings as seven reigns from the section's table, Romulus to Ancus in one tone and the Tarquins and Servius in another, against the four narrators, in place of one span "The seven kings".
- **1.6** figure 1: the axis ends at a tick at 1 BC in place of the year-0 workaround that left Livy and Dionysius in an unmarked stretch.
- **3.5** figure 2: the two datings of the first ROMANO didrachm (Burnett and *HN Italy* about 310–300; Crawford, *RRC* 13, 280–276) as a range, `"years": true`, in place of timeline spans.
- **4.5** figure 4: Terence's six plays as a span 166–160 beside Plautus, in place of the event N4 made of it.
- **5.6** figure 1: the 45–44 span labelled as the text words it, "The great burst" (cut to "Burst" for the old renderer), and the event "Brutus and Orator".
- **7.1** figure 1: where the sources survive as overlapping spans under the reigns (Annals 1–6, 14–37; Annals 11–16, 47–66; Dio 57–63, 14–68), the gaps drawn as gaps.
- **7.4** figure 3: Macrinus (217–218) and Elagabalus (218–222) as named spans in place of blank bars and two stand-in accession events; the checker's FIX relabelled Ardashir's c. 224 "Ardashir (date approx.)", since the event's date line cannot show "c.".
- **8.6** figures 1, 2 and 4: the text's periods as spans (Vandal Africa 533–534; Alexandria 641–642 and the Arab siege 717–718; the civil wars 1321–1328 and 1341–1347) in place of events at their first years.
- **10.2** figure 1: Tacitus' life (about 56 to about 120) against the Annals (14–68) and Histories (69–96); the checker's FIX took out Suetonius' life, which the next paragraph gives, not the one the figure follows.
- **11.1** figure 3: the compare's labels as the section words them ("Comitium held some 3,600 to 3,800", "Forum held perhaps", "Electoral assemblies seldom exceeded", "Census of citizens in 164"), values unchanged.

Written back (3 figures N4 dropped): **3.4** the compare of the infantry on Polybius' lists of 225 (2.24), six rows from the table; **9.1** the tree of Gaius' scheme (persons, things, actions; nine leaves, 1,104 units wide, scrolling); **10.2** the tree of the ten plays under Seneca's name (eight accepted, *Hercules Oetaeus* doubted, *Octavia* after 68; 1,226 units wide, scrolling).

Kept as they were: **1.2** the text-lengths figure stays dropped (the three word counts are approximate and the section cites no source for them, so a compare would need a caption source the text does not give); **6.4** both figures (the Bastarnae campaign is already the 29–28 span the text gives; the 20 BC start only pads); **7.1** figure 4 (its two spans do not overlap); **8.6** figure 3 (every date in it is a point).

Rome now carries 180 P43 figures (177 + 3): timeline 74, flow 54, matrix 14, tree 14, compare 9, decision 5, bars 5, range 4, objects 1. The P57 checkers' prose notes repeat leads already listed above; one drawing note is new: a timeline event's date line prints a bare year and cannot mark it "c." (1.6, 7.4; the Greek checkers met the same, proposed row P58).
