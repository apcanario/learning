# Corrections pass P61, 30 October 2026 (body faults outside P54/P59)

The faults listed in the last section of `corrections-2026-10-30.md` ("Found in the pass, outside it"), worked as backlog row P61 (confirmed by Pedro 30 Oct 2026, 16:51, to run with N6 in the same chat). Opus 5.5 throughout, each agent a fresh isolated context (P31).

Procedure. One fresh fixer per report saw only its report, its items from that section (verbatim), `AGENT-SPEC.md`, `WRITER-BRIEF.md` and, for Greek 1.2, 1.3, 4.2, 10.9, 10.10 and 10.12, the reports they cross-reference (1.2: 10.10, 10.2; 1.3: 5.1; 4.2: 10.10; 10.9: 4.1; 10.10: 10.3; 10.12: 10.10, 10.3). For each item it decided real, not real or unsettled, and proposed the smallest exact replacement; an outside source was checked with search. A second fresh agent per report, shown the proposals and their evidence but not the fixer's reasons, checked each replacement against the report and the cited source (PASS or FAIL; a figure edit also had to draw). Only PASSes were applied, then `check.py` (no HARD line) and `register.py` with each report's model unchanged. A changed figure then went through P58's figure check: a fresh agent checked it against the report's text (PASS, FIX or DROP), a FIX was applied and re-checked by another fresh agent. Reports with no proposed edit had no checker.

Counts: 24 reports; 16 corrected (Greek 1.1, 2.2, 2.4, 4.2, 4.5, 6.6, 7.3, 9.3, 10.3, 10.10, 11.4, 11.8, 12.2; Rome 2.5, 5.4, 7.4), 33 replacements passed and applied, 1 failed (Greek 5.4); 9 items not real; 0 unsettled. Figures changed: Greek 1.1 fig. 1, 2.4 fig. 2, 6.6 fig. 2, 9.3 fig. 2; three PASS on the first figure check, one FIX (9.3) passed the re-check; none dropped. After every report `check.py` OK; `verify.py` figure rules run at the build.

Each line gives the item (shortened), then the text replaced and its replacement (shortened), or the reason it was left.

### Greece 0.1 (words 2,789, unchanged)
- **Left (not real).** Figure 1's caption "at least five centuries": the body's Linear B paragraph still says "at least five centuries older than Homer", so caption and text agree.

### Greece 1.1 (words 2,974 → 2,993)
- **Fixed.** Platon's scheme has four phases; the table listed Final Palatial under it. `and Nikolaos Platon's palatial phases.` → `and Nikolaos Platon's four palatial phases (Prepalatial, Protopalatial, Neopalatial, Postpalatial), to which some later…`; `<th>Platon phase</th>` → `<th>Palatial phase</th>`.
- **Fixed (figure 1, title and caption).** `Bronze Age Crete: Platon's phases, …` → `Bronze Age Crete: palatial phases (Platon's four, with the later Final Palatial), …`; caption `Platon's palatial phases, with Evans's…` → `Platon's palatial phases plus the later Final Palatial, with Evans's…`. Figure check PASS. Basis: Wikipedia, "Minoan chronology".

### Greece 1.2 (words 2,746, unchanged)
- **Left (not real).** Cross-references to module 10.10 (twice) and 10.2: 10.10 has Calder and Traill against Easton on the treasure and the Korfmann–Kolb lower-city quarrel; 10.2 has the Mask of Agamemnon.

### Greece 1.3 (words 2,853, unchanged)
- **Left (not real).** "Nine Self-test questions": the Self-test has ten, each with its answer.
- **Left (not real).** Cross-reference to module 5.1: 5.1's population section argues Morris against Snodgrass on the burial record.

### Greece 2.2 (words 3,117 → 3,125)
- **Fixed.** The Zeus dispute box gave "born earlier" (Iliad 15.166) to Poseidon; at 15.165–167 it is Zeus's own claim in the message Iris carries. `Homer's Poseidon resents Zeus as a brother "born earlier" (Iliad 15.166)` → `Homer's Zeus, in the message Iris carries to Poseidon, calls himself "born earlier" (Iliad 15.166), a claim Pos…`. Self-test answer already agreed.

### Greece 2.4 (words 2,929 → 2,932)
- **Fixed (text tree and figure 2).** Hellen's sons reordered to Dorus, Xuthus, Aeolus, as Apollodorus 1.7.3 and Catalogue of Women fr. 9 give them; no label changed. Figure check PASS.

### Greece 4.2 (words 3,280 → 3,274)
- **Fixed.** Cross-reference to module 10.10: 10.10 treats whether the war happened as Finley against Latacz with a middle ground, and the Korfmann–Kolb quarrel there is about the lower city. `a separate question, argued between Korfmann and Kolb and treated in module 10.10.` → `a separate question, treated in module 10.10.`

### Greece 4.5 (words 2,835, unchanged)
- **Fixed.** Self-test 2 put "470s or 450s BC" before Aeschylus' trilogy of 458, which fails for 454. `in the 470s or 450s BC, before Aeschylus' trilogy of 458` → `The ancient scholia date the ode to 474 or 454 BC, so it may come before or after…`. Basis: BMCR 2008.08.37 (on Finglass, Pindar: Pythian Eleven).

### Greece 5.4 (words 2,796, unchanged)
- **Left (check FAIL).** The timeline prints 650 BC for a revolt the text dates only "mid-seventh century". The proposal gave the event `"date": "mid-seventh century"`; `viz.py` (P58) stops the build when a date line does not contain the event's year, so the edit cannot draw. The figure keeps its current data; proposed row P63.

### Greece 6.6 (words 2,962 → 2,981)
- **Fixed (sourcing).** No ancient source gives the allied total at Chaeronea (Diodorus 16.85.5 gives Philip's numbers only) and no named scholar was found for 35,000. `perhaps 35,000 allied Greeks faced Philip's 30,000 foot and 2,000 horse` → `the allied Greeks faced Philip's 30,000 foot and 2,000 horse. No ancient source gives the allied total; the figure of about 35,000 often quoted for it is an unsourced estimate.`
- **Fixed (figure 2, label and caption).** `Allied Greeks (perhaps)` → `Allied Greeks (unsourced estimate)`; caption `The text gives these numbers without a source…` → `The text gives Philip's numbers without a source…`. Figure check PASS.

### Greece 7.3 (words 2,857 → 2,866)
- **Fixed (body and Self-test 7).** The OGIS 338 box said the decree treats the will's ratification as fact; the decree says the will must still be ratified by the Romans. `refers to the will's ratification as fact` → `cites the will and says that Rome had still to ratify it`; Self-test 7 `treats the will and its ratification by Rome as fact;` → `cites the will and says that Rome had still to ratify it;`. Neither fixer nor checker could open the inscription page (PHI blocked by the proxy); the clause (δεῖ δὲ ἐπικυρωθῆναι τὴν διαθήκην ὑπὸ Ῥωμαίων) and the identification OGIS 338 = IvP I 249 (Austin no. 248) rest on attalus.org and a PHI search hit. Worth a look in P48.
- **Fixed.** Polybius 6.56: `kept the masses honest and magistrates accountable` → `kept the masses in check through fear and the magistrates honest`. Basis: Paton's Loeb, 6.56.11, 13–15 (LacusCurtius). Self-test 10 already agreed.

### Greece 9.3 (words 2,783, unchanged)
- **Fixed (figure 2).** Step 3 dated Michael Scot to the twelfth century in Toledo. Fixer: `"Latin translation in Toledo", "note": "twelfth century: Gerard of Cremona, Michael Scot"` → `"Latin translation", "note": "Gerard of Cremona in twelfth-century Toledo: Aristotle; Michael Scot in the early thirteenth century: Averroes"`. Figure check FIX: the flow also drew a stage the text does not have ("Arabic commentary: Ibn Rushd" between Baghdad and Gerard); the stage was removed, step 1's note put in the text's words and step 3 renamed "Latin translation from Arabic". Re-check PASS.

### Greece 10.2 (words 3,190, unchanged)
- **Left (not real).** "Nine Self-test questions": the Self-test has ten.

### Greece 10.3 (words 3,283 → 3,279)
- **Fixed (body and Self-test 10).** Suetonius, Divus Julius 6.1 names Venus only. `derived the family from Venus through Aeneas' son Iulus (Suetonius…6.1)` → `derived the family from Venus (Suetonius…6.1)`; Self-test 10 now credits Iulus to Virgil, Aeneid 1.267–288, and Venus to Suetonius.

### Greece 10.9 (words 3,587, unchanged)
- **Left (not real).** Cross-reference to module 4.1: 4.1's "The wedding on Pelion and the Judgement of Paris" tells the courtship, Themis' prophecy and the marriage to Peleus.

### Greece 10.10 (words 3,158, unchanged)
- **Fixed.** Self-test 3: `Troy II, c. 2500–2300 BC` → `Troy II, c. 2550–2250 BC`, as the body and table. The body did not carry the fault.
- **Left (not real).** Cross-reference to module 10.3: 10.3's "Wilusa and the Luwian hypothesis" treats Watkins and the Luwian question.

### Greece 10.12 (words 3,880, unchanged)
- **Left (not real).** Cross-references to module 10.10 (twice) and 10.3: each names material its target treats.

### Greece 11.4 (words 2,921 → 2,930)
- **Fixed (body and Self-test 8).** Arrian 5.3.1–4 gives Eratosthenes' examples as Prometheus' cave, the Caucasus moved to India and the cattle branded with Heracles' club, not Aornos. Body `like Heracles' failure at Aornos` and Self-test 8 `like Prometheus' cave and Heracles at Aornos` → `like Prometheus' cave, a Caucasus moved to India and cattle branded with Heracles' club`. The report's other Aornos reference (Arrian 4.28) is untouched. Basis: Chinnock's translation, Wikisource.

### Greece 11.8 (words 2,872, unchanged)
- **Fixed.** Day-by-day table: the Sarapis consultation `27` → `26`. Basis: Plutarch, Alexander 76.3–4 (Perrin, Loeb 1919). No figure carries the date.

### Greece 12.2 (words 3,358 → 3,363)
- **Fixed (body and its Self-test answer).** Frogs 1491–1495 calls it graceful not to sit chattering beside Socrates; "as a fashion" dropped in both places. Basis: Living Poets (Durham), Greek and translation.

### Greece 12.7 (words 2,870, unchanged)
- **Left (not real).** "Nine Self-test questions": the Self-test has ten.

### Rome 2.5 (words 2,736, unchanged)
- **Fixed.** Carry forward 3: `Roman games beside Phrygian eunuchs` → `Roman games beside self-castrated Galli`, the body's own description.

### Rome 5.4 (words 3,218 → 3,228)
- **Fixed (table, Pharsalus box, Self-test 2 and 6).** Caesar's qualifiers restored where the Latin has them: about 368,000 Helvetii (Gallic War 1.29), scarcely 500 Nervii (2.28), about 40,000 at Avaricum and scarcely 800 escaped (7.28), about 250,000 foot (7.76), about 15,000 Pompeians killed for no more than 200 men and about 30 centurions (Civil War 3.99). Unhedged figures left as they were. Basis: The Latin Library texts.

### Rome 7.4 (words 2,836 → 2,849)
- **Fixed.** Dio's "a source of constant wars and great expense" concerns the conquest beyond the Euphrates in 195, made while Byzantium was under siege; it moved from the Ctesiphon and Hatra paragraph to the one on 193–196 with its occasion (Dio 75(75).1.1, 3.2–3). Basis: Cary's Loeb, LacusCurtius.

## Left for later
- **Greece 5.4.** The revolt "in the mid-seventh century" prints as 650 BC in its timeline: a date line cannot carry a century without its year. Proposed row P63 (a `date` that names a century, or a rule for undated events).
- **Greece 7.3.** The OGIS 338 clause was not read on a page in this pass (above); the P48 Fable check can confirm it.
