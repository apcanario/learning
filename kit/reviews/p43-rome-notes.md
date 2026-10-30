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
