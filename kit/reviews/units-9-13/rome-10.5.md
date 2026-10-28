# Rome 10.5: Capstone: the whole thing in one sitting

Verdict: fix (five errors, each a one-sentence edit, over 9,547 words; scaled to a 2,500-word report this is about one error, under the rewrite threshold)
Body words: 9547 (capstone mode, 40 questions; no word target; `check.py` OK, 6 sections, 3 disputes)

## Coverage

Format: 15 short-answer, 10 connections, 10 "who says this and why doubt it", 5 essays, model answers, ten gaps with one follow-up prompt each, Carry forward. Matches the prompt.

| Q | Modules drawn on |
|---|---|
| A1 | 0.3, 1.1, 1.4 |
| A2 | 0.1, 1.4, 1.5, 9.5 |
| A3 | 1.5, 1.6, 2.3 |
| A4 | 1.3; Greek 10.12 |
| A5 | 2.4, 3.1; Greek 5.5, 8.4 |
| A6 | 3.3, 3.4, 5.2, 7.4, 7.5 |
| A7 | 2.2; Greek 2.2 |
| A8 | 2.5 |
| A9 | 0.1, 2.4, 3.1, 3.2, 4.5 |
| A10 | 2.1, 5.4 |
| A11 | 4.3, 4.4 |
| A12 | 3.3, 7.5, 9.1 |
| A13 | 8.6, 9.1 |
| A14 | 7.4, 7.5, 9.2 |
| A15 | 8.3, 10.4 |
| B1 | 3.1, 3.2 (5.1 implicit) |
| B2 | 1.6, 3.2, 5.4, 10.4 |
| B3 | 3.1, 5.1, 5.2, 5.3, 6.1 |
| B4 | 3.4, 3.5, 4.3, 5.2 |
| B5 | 3.1, 4.5; Greek 5.4 |
| B6 | 2.4, 6.2, 8.2; Greek 7.1, 11.4 |
| B7 | 1.2, 2.1, 2.3, 8.3, 8.5 |
| B8 | 1.6, 3.2, 9.3 |
| B9 | 0.3, 6.4, 7.4, 8.1, 8.2 |
| B10 | 1.3, 1.4, 6.2, 6.3 |
| C1 | 0.1, 1.1, 1.2, 1.3 |
| C2 | 3.3 |
| C3 | 0.1, 4.2, 4.4 |
| C4 | 4.1 |
| C5 | 5.1 |
| C6 | 5.3, 5.6 |
| C7 | 6.1, 6.4 |
| C8 | 7.2, 7.3 |
| C9 | 8.3 |
| C10 | 7.3, 9.4, 10.2 |
| D1 | 0.1, 0.2, 1.3, 1.4, 1.6, 2.1, 2.2, 3.1, 3.2 |
| D2 | 5.2, 5.3, 5.5, 6.1, 6.4, 7.1, 7.2, 7.4, 8.1, 8.2, 8.3, 8.5, 8.6, 9.2 |
| D3 | 1.1, 1.3, 2.2, 3.1, 3.2, 3.4, 4.5, 5.6, 7.5, 8.6, 9.1, 10.1, 10.3; Greek 3.7, 6.2, 8.1 |
| D4 | 0.3, 7.5, 8.5, 8.6 |
| D5 | 2.1, 2.5, 8.1, 8.2, 8.3, 8.4 |

- All 53 other core modules are touched at least once. Integration is good in Parts B to D: legend to the age that wrote it (B1, B2, C2, D1), source to bias (all of Part C), institution to long consequence (B3, B7, B9, D2), Rome to the Greek course (A4, A5, A7, B5, B6, D3).
- Thin or missing: slavery (module 9.3, named in the prompt) has no question; only D3's clause on freed slaves touches it. Geography (0.2) appears only in a clause of D1 (Lacus Curtius, Juturna). Ovid (10.1) and Roman art (10.3) appear only inside D3; the Julio-Claudians (7.1) only in a clause of D2; Tacitus is cited throughout but never examined as a source in Part C. Women, apart from Lucretia and Verginia as legends, are absent.
- Duplicated Self-test questions. Most of Part A recycles core Self-test questions, often with near-verbatim answers: A7 = 2.2 ("What happened at the lectisternium of 217..."); A8 = 2.5 ("What does the Tiriolo bronze show about the senate's aims..."); A10 = 5.4 ("What was Bibulus doing when he 'watched the sky' in 59..."); A12 = 7.5 ("What did the lex Irnitana provide..."); A13 = 9.1 (two questions, Verona palimpsest and the Digest); A14 = 9.2 ("What did a military diploma grant, to whom, and how did the grant change?", answer nearly word for word); A15 = 10.4 ("What did the Silvester legend and the Donation of Constantine each claim..."). Partial overlaps: A2 (0.1, 1.5), A3 (2.3), A6 (3.3), A9 (2.4), A11 (4.3); in Part C, C10 (9.4, "What does Juvenal's panem et circenses get wrong, and what does Pompeii add?"), C4 (4.1), C6 (5.3), C9 (8.3). Parts B and D are new questions. Finding 7 replaces A14, the worst case, with a slavery question.

## Findings

1. [error | pointer] Section "How to sit this exam" (dispute box).
   Current: "Several model answers take a position on open points: whether Polybius' first treaty with Carthage belongs near 509 or, as Diodorus (16.69) and Mommsen held, to 348; whether the city held about a million people (Brunt, Hopkins) or under half that (Storey); whether Constantine's sign"
   Problem: No model answer mentions the first treaty with Carthage or the population of Rome (searched all 40 answers: "treaty" occurs only for 338, the Gallic withdrawal, Philinus and the barbarian settlements; "million" only for sesterces). Only the Constantine point is taken (C9). The scholars named are right (module 1.6 dispute box; module 9.4), but the box describes an exam that is not this one.
   Fix: "Several model answers take a position on open points: whether the tophet's infants were sacrificed (Smith, Stager, Xella, Quinn) or died naturally (Moscati, Schwartz); whether Marius made the army proletarian, which Rich and Cadiou doubt; whether Constantine's sign"
   Basis: C4 ("Opinion now leans to sacrifice") and D2 ("though Rich and Cadiou doubt that Marius made the army proletarian") do take these positions; modules 4.1 and 5.2 dispute boxes.

2. [should-fix | register] Section "How to sit this exam".
   Current: "Allow about three hours:"
   Problem: The stated timings add to 255 minutes: 15 × 2 = 30, 20 × 5 = 100, 5 × 25 = 125. The marks (30 + 50 + 50 + 70 = 200) and thresholds are consistent; the time is not.
   Fix: "Allow about four and a quarter hours:"
   Basis: arithmetic. Greek module 9.4 has the same slip (noted below).

3. [error | accuracy] Section "Part A: short answer (15)", A1.
   Current: "because each writer counted the consular colleges back to the first consuls and added a royal span of about 240 years fixed in advance (module 0.3)"
   Problem: Module 0.3 says the opposite of "each writer": "Set Timaeus and Ennius aside and the dates fall between 753 and 728, which suggests a common method". Timaeus' 814/13, the first date in this very sentence, was a synchronism with Carthage, not a count of consular colleges, and the method is an inference, not a fact.
   Fix: "because most of them, Timaeus excepted, seem to have counted the consular colleges back to the first consuls and added a royal span of about 240 years fixed in advance (module 0.3)"
   Basis: rome/r-0.3.html, section on the foundation date (table from Dionysius 1.74 and the paragraph after it).

4. [should-fix | register] Section "Part A: short answer (15)", A7.
   Current: "the equation of Roman and Greek gods was a dated act, not a fact of nature"
   Problem: Module 2.2 treats the equation as an old habit already at work when Romans began to write (Livius Andronicus' Camena, Ennius' list of the twelve), and its dispute box says 217 "may have formalised rather than invented" an older Italian twelve. What was dated was the official pairing, not the equation.
   Fix: "the state's pairing of its gods as Greek couples was a dated act, not a fact of nature"
   Basis: rome/r-2.2.html, "The system: triad, twelve and the lectisternium of 217" and "Interpretatio graeca and interpretatio romana".

5. [minor | pointer] Section "Part A: short answer (15)", A12.
   Current: "makes the town's courts follow the governor's edict (ch. 85; module 9.1)"
   Problem: Module 9.1 never mentions the lex Irnitana; chapter 85 is in module 7.5 (already cited in the answer). Module 9.1 covers the praetor's edict, which governors' edicts copied.
   Fix: "makes the town's courts follow the governor's edict (ch. 85), itself modelled on the praetor's (module 9.1)"
   Basis: rome/r-7.5.html (lex Irnitana paragraph); rome/r-9.1.html, "The praetor's edict and the formula".

6. [minor | accuracy] Section "Part A: short answer (15)", A13.
   Current: "It is the one classical textbook to survive whole and unrevised"
   Problem: The Verona codex is almost complete, not whole; papyri (P.Oxy. XVII 2103, PSI XI 1182) were used to check and supplement it. Module 9.1 says "the one classical textbook to survive" and that Gaius showed classical law "whole and unrevised", which is a different claim.
   Fix: "It is the one classical textbook to survive nearly whole and unrevised"
   Basis: https://en.wikipedia.org/wiki/Institutes_(Gaius) ("almost complete version"); rome/r-9.1.html.

7. [should-fix | register] Section "Part A: short answer (15)", A14 (duplication and coverage).
   Current: "<li>What did a military diploma grant, and how did the grant change between the first surviving diploma and the last?
<details><summary>Model answer</summary><p>After twenty-five years' service an auxiliary, a non-citizen provincial, received citizenship for himself and his children and lawful marriage with one wife, by an imperial constitution posted at Rome; the diploma was his certified copy on two bronze tablets sealed by seven witnesses (module 9.2). The earliest surviving dates from 52; around 140, on the usual reading, children born during service ceased to be covered; the last auxiliary diploma dates from 203, nine years before the edict of 212 made nearly every free inhabitant a citizen (module 7.4). Army service had been the provincial's road to citizenship, as local office was the townsman's (module 7.5).</p></details></li>"
   Problem: Question and answer repeat module 9.2's Self-test question almost word for word ("What did a military diploma grant, to whom, and how did the grant change?"), while slavery, which the prompt names, has no question anywhere in the exam. The army is already examined in B9 and D2. The facts in the current answer are right (earliest diploma 52, last auxiliary diploma 203).
   Fix: "<li>What did formal manumission give a Roman slave and his son, and why did Philip V hold the practice up to Larisa?
<details><summary>Model answer</summary><p>A slave formally freed by a Roman citizen became a citizen, took his patron's first and family names and owed him respect and often agreed days of work; he could not hold office at Rome, but his freeborn son was a full citizen, as Horace, a freedman's son, became a military tribune (<em>Satires</em> 1.6.45–48; module 9.3). Urging Larisa in 214 to enlarge its citizen body, Philip V cited the Romans, who enrolled freed slaves and had sent colonies to nearly seventy places (Syll.³ 543; modules 3.4, 9.3); Athens had confined citizenship to children of two Athenians in 451/0 (Greek module 6.2). Manumission was also a means of control, as Bradley read it, and after the revolts of about 135 to 71 it offered the able a way out (module 9.3). Rome grew its citizen body from its slaves as well as its allies.</p></details></li>"
   Basis: rome/r-9.2.html Self-test; rome/r-9.3.html, "Manumission and the freedmen" and the revolts paragraph; rome/r-3.4.html (Philip V, Syll.³ 543); greece/r-6.2.html (law of 451/0); diploma dates confirmed at https://en.wikipedia.org/wiki/Roman_military_diploma.

8. [error | accuracy] Section "Part B: connections (10)", B1.
   Current: "Livy wrote books 2 to 6 in the 20s BC from annalists who all wrote after 133:"
   Problem: Livy names Fabius Pictor, "by far the oldest authority", in these very books (2.40.10, on Coriolanus' death; module 3.2 dispute box). Module 3.1 lists the five named annalists who wrote after 133 but does not say they were Livy's only sources.
   Fix: "Livy wrote books 2 to 6 in the 20s BC, naming Fabius Pictor rarely and chiefly annalists who wrote after 133:"
   Basis: Livy 2.40.10; rome/r-3.2.html (Coriolanus dispute box and Self-test); rome/r-3.1.html, "Livy books 2 to 10 and the Gracchan lens".

9. [should-fix | accuracy] Section "Part B: connections (10)", B1.
   Current: "in Cincius' and Piso's version Servilius Ahala kills Maelius as a private man at the senate's bidding"
   Problem: The answer offers this as Gracchan projection, but module 3.2's dispute box makes the opposite point too: if this Cincius is the annalist of about 200, as Dionysius' editors assume, the private killing predates the Gracchi, which complicates the retrojection. Naming Cincius as an author in a list of post-133 projections contradicts the answer's own first sentence. A full-mark answer would put the case on the "both ways" side as well.
   Fix: replace with "in Piso's version Servilius Ahala kills Maelius as a private man at the senate's bidding"; and replace "Yet the traffic runs both ways. The tribunate the Gracchi used" with "Yet the traffic runs both ways. Dionysius found the private killing in Cincius too, if he is the annalist of about 200 (module 3.2). The tribunate the Gracchi used"
   Basis: Dionysius 12.4.2–5; rome/r-3.2.html (Maelius dispute box and Self-test "Why does the Cincius and Piso version of Maelius' death matter?").

10. [should-fix | accuracy] Section "Part B: connections (10)", B3.
    Current: "It lay quiet until Tiberius Gracchus legislated through the plebeian council over the Senate's head in 133 and had a vetoing colleague deposed (module 5.1)."
    Problem: The tribunate did not lie quiet between 287 and 133: Flaminius carried his land law as tribune in 232 against the Senate (Polybius 2.21.7–8), tribunes jailed the consuls of 151 over the levy (Periochae 48) and the ballot laws of 139 and 137 were tribunician; deep dive module 11.1 records the last two. The usual view is a tribunate mostly working with the nobility.
    Fix: "Mostly an instrument of the nobility after 287, though tribunes jailed the consuls of 151 over the levy (deep dive module 11.1), it became a weapon again when Tiberius Gracchus legislated through the plebeian council over the Senate's head in 133 and had a vetoing colleague deposed (module 5.1)."
    Basis: rome/r-11.1.html (Periochae 48; ballot laws, Cicero, On the Laws 3.35–37); Polybius 2.21.7–8.

11. [should-fix | register] Section "Part B: connections (10)", B8.
    Current: "But the cases are famous because rare."
    Problem: Module 9.3 makes a second point the answer leaves out: the famous cases mix paternal with public authority, since Brutus and Torquatus acted as consuls (Livy 2.5, 8.7), and only cases like Fulvius in 63 show a father acting as father. The answer cites both as proof that "the legends make paternal power absolute".
    Fix: "But the cases are famous because rare, and Brutus and Torquatus acted as consuls as well as fathers (module 9.3)."
    Basis: rome/r-9.3.html, paragraph beginning "The limits were real".

12. [minor | accuracy] Section "Part B: connections (10)", B10.
    Current: "a Trojan Caesar who will close the gates of war (1.257–296)"
    Problem: Module 6.3 sets out the dispute over whether the Caesar of 1.286 is Julius (Servius, Dobbin) or Augustus, and in the text the gates are shut in the age that follows, not explicitly by the Caesar. The answer silently takes one side.
    Fix: "a Trojan Caesar, Julius or Augustus, and the gates of war shut (1.257–296)"
    Basis: rome/r-6.3.html (Jupiter's prophecy and Self-test "Why is the identity of the Caesar at Aeneid 1.286 disputed?").

13. [minor | accuracy] Section "Part C: sources and their bias (10)", C2.
    Current: "Doubt it because the nearer witnesses are the sparer."
    Problem: Only Polybius is nearer. Diodorus wrote at the same time as Livy, Strabo under Augustus and Suetonius in the second century AD; the point (Mommsen's) is that the other versions are sparer and the oldest has no rescue.
    Fix: "Doubt it because every other version is sparer, and the earliest knows no rescue."
    Basis: rome/r-3.3.html (dispute box on the Gauls' departure).

14. [should-fix | register] Section "Part C: sources and their bias (10)", C7.
    Current: "Doubt it because the <em>Res Gestae</em> lies by arrangement and silence rather than by statement."
    Problem: The quotation omits the half-sentence that module 6.1 makes central: after 27 he "excelled all in auctoritas" while claiming no more potestas (34.3). A full-mark answer should notice that the source itself concedes superior authority; the model answer never mentions auctoritas.
    Fix: "Doubt it because the <em>Res Gestae</em> lies by arrangement and silence rather than by statement. The quotation leaves out the clause between: he excelled all in <em>auctoritas</em>, influence, while claiming no more <em>potestas</em> (34.3)."
    Basis: Res Gestae 34.3; rome/r-6.1.html (paragraph beginning "The theory came later").

15. [minor | attribution] Section "Part C: sources and their bias (10)", C7.
    Current: "Judge argued that <em>res publica</em> meant the commonwealth, so that what was restored was order and legality, as on the aureus of 28, not a constitution."
    Problem: Judge's article is of 1974; the aureus of 28 was published by Rich and Williams in 1999 (module 6.1). As written, Judge is made to argue from a coin he could not have known.
    Fix: "Judge argued that <em>res publica</em> meant the commonwealth, so that what was restored was order and legality, not a constitution, a reading the aureus of 28, published in 1999, fits."
    Basis: rome/r-6.1.html, first section (aureus "published by John Rich and Jonathan Williams in 1999") and dispute box (Judge, 1974).

16. [error | accuracy] Section "Part D: essays (5)", D1.
    Current: "Romulus and Remus reached the page about 200 BC, five and a half centuries after Varro's date"
    Problem: Callias, about 300 BC, already had Rhomos and Rhomylos as sons of Rhome and Latinus (Dionysius 1.72.5; module 1.3), and Fabius took the twins' story from the Greek Diocles of Peparethus (Plutarch, Romulus 3.1; modules 0.1, 1.4). About 200 BC is the first Roman narrative. The answer's own preceding paragraph says Greeks wrote Rome's prehistory first.
    Fix: "Romulus and Remus appear in Greek writers from about 300 BC and in Roman prose about 200 BC, five and a half centuries after Varro's date"
    Basis: rome/r-1.3.html (Callias in the list of Greek versions); rome/r-1.4.html first paragraph ("No Roman wrote the story down until about 200 BC"); rome/r-0.1.html (Fabius "took the foundation story itself from a Greek, Diocles").

17. [should-fix | accuracy] Section "Part D: essays (5)", D2 and D4.
    Current (D2): "and on generals, Stilicho, Aetius, Ricimer, who made and unmade emperors"
    Current (D4): "while generals from Stilicho to Ricimer made and unmade emperors"
    Problem: Of the three, only Ricimer made and unmade emperors (module 8.5's table: Majorian to Glycerius). Stilicho governed for Honorius and was accused only of planning a throne for his son; Aetius backed the usurper John in 425 but ruled for Valentinian III, who killed him.
    Fix (D2): "and on generals, Stilicho and Aetius who governed for emperors and Ricimer who made and unmade them"
    Fix (D4): "while generals from Stilicho to Ricimer ruled in the emperors' names and Ricimer made and unmade them"
    Basis: rome/r-8.5.html (Stilicho, "Aetius and Attila, 425–454", "Ricimer and the last emperors, 455–476").

18. [minor | accuracy] Section "Part D: essays (5)", D4.
    Current: "Gibbon's immoderate greatness or his pusillanimous clergy (module 8.5)"
    Problem: Gibbon's clergy preached "patience and pusillanimity" (chapter 38, as module 8.5 quotes it); they are not themselves called pusillanimous.
    Fix: "Gibbon's immoderate greatness or his clergy preaching patience and pusillanimity (module 8.5)"
    Basis: rome/r-8.5.html, "Gibbon and Pirenne: why and when".

19. [should-fix | lane] Section "Where the gaps will still be", gap 2 (The Aeneid as a poem).
    Current: "After deep dive unit 12, write a short essay on the close of book 12: Juno's reconciliation with Jupiter, Turnus' plea and his killing, set against Anchises' charge to spare the conquered in book 6, with the main Augustan and pessimistic readings of the ending and the evidence each relies on."
    Problem: The gap is real for the core, and the note rightly sends the reader to unit 12, but the follow-up asks for exactly what the queued deep dives do: 12.3 covers book 12's duel, Juno's reconciliation and Turnus' death, 12.5 Anchises' charge (6.847–853), 12.6 the reconciliation, and 12.7 the ending at 12.950–952 as a test case with Putnam's pessimistic and Galinsky's Augustan readings.
    Fix: "After deep dive unit 12, write a short essay comparing the endings of the Aeneid and of Statius' Thebaid: Turnus killed in anger at Aeneid 12.938–952 against Anchises' charge to spare the conquered (6.851–853), and Theseus marching from Athens and its altar of Clemency to force the burial of the Argive dead in Thebaid 12, asking how far Statius' ending answers Virgil's and what each says about clemency under an emperor."
    Basis: roman-syllabus.html prompts 12.3, 12.5, 12.6, 12.7; rome/r-10.2.html (Thebaid 12, Theseus and the altar of Clemency), which makes the new prompt build on the course rather than repeat it.

20. [error | accuracy] Section "Where the gaps will still be", gap 3 (Roman philosophy).
    Current: "After deep dive unit 13, write a short report comparing three Roman deaths staged as philosophy under one man's rule: Cato at Utica, Seneca in 65 and Thrasea Paetus in 66, using Plutarch's Cato Minor, Tacitus' Annals and Seneca's Letters, and asking how far the exemplary Stoic death was a political act."
    Problem: Two faults. Cato died at Utica in 46 BC after Caesar's victory, Seneca and Thrasea under Nero: not "one man's rule". And the prompt duplicates queued deep dives: 13.4 covers Cato as a Stoic life, Thrasea's death in 66 (Annals 16.21–35) and "the exemplary deaths", and 13.5 Seneca's death "as a Socratic performance (Annals 15.60–64)".
    Fix: "After deep dive unit 13, write a short report on how Latin Christianity took over Roman philosophy: Lactantius' Divine Institutes against the philosophers, Ambrose's On Duties as a Christian rewriting of Cicero's, Augustine's debts to Cicero's Hortensius, Varro and the Platonists in the Confessions and the City of God, and Boethius' Consolation of Philosophy, written in prison under Theoderic, asking what the Latin West kept of the Stoa and the Academy."
    Basis: roman-syllabus.html prompts 13.4, 13.5, 13.8 (none takes the Christian Latin reception); Boethius appears in the course only as Aristotle's translator (Greek modules 7.4, 12.4); Hortensius and Augustine only in a sentence each (modules 10.2, 13.1).

21. [should-fix | accuracy] Section "Where the gaps will still be", gap 8 (Science, medicine and engineering).
    Current: "Galen appeared once, for the plague (module 7.3), and Pliny, Frontinus and Vitruvius as sources (modules 9.4, 10.2, 10.3); how Romans studied nature and built was never a subject."
    Problem: How Romans built was a subject: module 9.4 has a section "Water: the aqueducts and Frontinus" and module 10.3 a section "Concrete, arch and dome" (Puteolan concrete, vaults, the Pantheon). The follow-up then asks again for "aqueducts, concrete". Galen also appears in module 4.3 (burning mirrors).
    Fix: "Galen appeared for the plague (module 7.3), Pliny, Frontinus and Vitruvius as sources, and aqueducts and concrete as buildings (modules 9.4, 10.2, 10.3); how Romans studied nature, and why their technology went no further, was never a subject."; and in the prompt replace "Pliny's Natural History as a system of knowledge, aqueducts, concrete, mills and mines" with "Pliny's Natural History as a system of knowledge, water-mills and mines"
    Basis: rome/r-9.4.html, rome/r-10.3.html section headings; rome/r-4.3.html (Galen on burning mirrors).

22. [minor | accuracy] Section "Where the gaps will still be", gap 7 (Parthia and Persia).
    Current: "the course never looked from the Iranian plateau, as Greek module 11.3 did for the Achaemenids."
    Problem: Module 8.1 calls Shapur I's trilingual inscription "the best witness" and narrates his three campaigns from it; module 7.4 gives Ardashir's claim through Dio. The course looked once, briefly.
    Fix: "the course looked from the Iranian plateau only through Shapur's inscription in module 8.1, never as Greek module 11.3 did for the Achaemenids."
    Basis: rome/r-8.1.html, "Shapur I, Valerian and the rock of Naqsh-e Rustam".

23. [minor | register] Section "Where the gaps will still be", gap 1 (How the Republic actually worked).
    Current: "the contiones, and what Quintus Cicero's handbook on electioneering says a new man had to do."
    Problem: The prompt omits the main narrative source for the elections of 64, Asconius' commentary on Cicero's In toga candida; without it a fresh chat will build the report on the handbook alone. (The rest of the prompt goes beyond deep dive 11.1, which mentions the handbook in one sentence.)
    Fix: "the contiones, Asconius' commentary on Cicero's In toga candida, and what Quintus Cicero's handbook on electioneering says a new man had to do."
    Basis: rome/r-11.1.html (handbook "of 64 BC" in one sentence); not otherwise checked: Asconius' commentary on In toga candida is the standard source for the campaign.

24. [minor | accuracy] Section "Carry forward", item 2.
    Current: "the haruspices a fixture of Christian emperors' palaces"
    Problem: The course has one Christian emperor, Constantine, keeping consultation of haruspices when lightning struck the palace (Theodosian Code 16.10.1; module 8.3), and Pompeianus' Tuscan diviners in 408 (module 8.5); "a fixture of palaces" overstates it.
    Fix: "the haruspices consultants to a Christian emperor when lightning struck his palace"
    Basis: rome/r-8.3.html (laws paragraph); B7's own model answer.

## Gaps check (task item 4)
- Gap 1, the Republic at work: real for the core; covered by queued deep dives 11.1 (written) and 11.3, as the note says. Follow-up (elections of 64) goes beyond them; see finding 23. Partly overlaps queued 11.5 (Cicero's consulship), acceptable.
- Gap 2, the Aeneid as a poem: real for the core; covered by queued deep dive unit 12 (12.1 to 12.8). Follow-up duplicates 12.3, 12.5, 12.7: finding 19.
- Gap 3, Roman philosophy: real for the core; covered by deep dive unit 13 (13.1, 13.2 written). Follow-up wrong and duplicative: finding 20. The description's "Stoic doctrine ... did not" is true of the Rome core only; Greek modules 7.2 and 12.7 give the doctrine.
- Gap 4, the economy: real (glimpses in 4.4, 7.5, 8.1, 9.3; no queued module). Prompt usable and specific; it names evidence (Monte Testaccio, wrecks, Greenland lead) and the Finley debate.
- Gap 5, the Church before Constantine: real (persecution in 2.5, 8.1, 8.2; bishops in 8.3). Prompt usable; names Dura-Europos, Justin, Tertullian, Perpetua, Marcion, Origen.
- Gap 6, Judaea and the Jews: real (2.5 expulsions and Rajak on community grants; 7.1, 7.2, 7.3 revolts). Prompt usable.
- Gap 7, Parthia and Persia: real, slightly overstated: finding 22. Prompt usable.
- Gap 8, science and technology: real for science and medicine, overstated for building: finding 21.
- Gap 9, transmission of Latin texts: real; the course has only single discoveries (10.2, 10.4, 9.1), Greek module 9.3 does the Greek side. "107 of Livy's 142 books" is right (35 survive).
- Gap 10, the successor kingdoms: real; 8.5 stops at 476, 8.6 treats Justinian's wars from Constantinople. Prompt usable. Gregory the Great died in 604.

## Errors noticed in other reports
- greece/r-9.4.html, "How to sit this exam": the same timing arithmetic, "Allow about three hours" for timings that add to 255 minutes (15 × 2 + 20 × 5 + 5 × 25).
- rome/r-1.4.html: "No Roman wrote the story down until about 200 BC" is right, but "The literature begins about 200 BC" (section "The earliest evidence") and the carry-forward "The foundation story was first written down about 200 BC" overstate it: Callias (about 300) named Rhomos and Rhomylos (Dionysius 1.72.5; module 1.3), and Fabius followed the Greek Diocles of Peparethus (Plutarch, Romulus 3.1), as the same report says.
- rome/r-6.1.html, dispute box: "E. A. Judge (...1974) argued that ... what was restored was its order and legality, as on the aureus of 28" attaches to a 1974 argument a coin the same report says was published in 1999. Suggest "..., a reading the aureus of 28, published in 1999, fits."
- rome/r-3.1.html, "Livy books 2 to 10 and the Gracchan lens": "Livy's named sources, Piso, Valerius Antias, Claudius Quadrigarius, Licinius Macer and Aelius Tubero, wrote after 133" omits Fabius Pictor, whom Livy names in book 2 (2.40.10; module 3.2). Not wrong as a list, but it misled 10.5 (finding 8); "Livy's named sources besides Fabius" would close it.

## Confirmed
- Varro asked Tarutius to cast Romulus' horoscope (Plutarch, Romulus 12); the writer's doubt is unfounded: Plutarch says Varro set Tarutius the task.
- Dionysius 1.74 range Timaeus 814/13 to Cincius 729/8 (module 0.3 table).
- Forum graves to about 1000 BC; Wiseman's "no more than an accident" on Carandini's wall (modules 1.1, 1.4).
- Lapis Niger cippus, Boni 1899, CIL I² 1, about 570–550 BC, sakros esed, recei, kalatorem; Festus' guesses of Romulus, Faustulus, Hostus Hostilius (modules 0.1, 1.4, 1.5, 9.5).
- Livy 2.2.1–2 on the rex sacrorum; Festus' order; Plutarch, Roman Questions 63; Dolabella 180 BC, Livy 40.42 (modules 1.5, 2.3). "So awkward an office is unlikely to be invented" is a fair inference, not a misattribution.
- Hellanicus in Dionysius 1.72.2, "with Odysseus", ascription disputed; Iliad 20.307–308; Segesta 263 (Zonaras 8.9); Flamininus "leader of the Aeneadae" (Plutarch, Flamininus 12) (module 1.3).
- Livy 3.31.8; Cicero, On the Laws 2.58–59, 2.64; Pomponius, Digest 1.2.2.4; Pliny 34.21; Gaius, Digest 10.1.13 (modules 2.4, 3.1).
- Settlement of 338, Livy 8.14; Cales 334; lex Julia 90, lex Plautia Papiria 89 (modules 3.3, 3.4, 5.2).
- Lectisternium of 217, Livy 22.10.9, the six couples (module 2.2).
- Tiriolo bronze CIL I² 581 and its clauses; North 1979; Pliny, Letters 10.96 (module 2.5).
- Polybius 6.53–54; Cicero, Brutus 62; Livy 8.40.4–5; 306 Fabii; Valerii and the appeal law (modules 0.1, 2.4, 3.1, 3.2, 4.5).
- Bibulus, Suetonius, Julius 20.1; Cicero, De domo sua 39–40; Cato's oath, Julius 30.3 (modules 2.1, 5.4).
- Peace of 201 (Polybius 15.18; Livy 30.37); Plutarch, Cato Maior 26–27; Appian, Punica 76–81, eighty stades (modules 4.3, 4.4).
- Lex Irnitana: 1981, El Saucejo, six of ten tablets, Pliny 3.30, chapters 21 and 85 (module 7.5).
- Niebuhr 1816, Savigny, Gaius 1.8, French Civil Code 1804, Digest 9,000 extracts from 39 jurists, Gradenwitz, Beseler, Wieacker, Kaser (module 9.1).
- Diplomas: earliest 52, change about 140, last auxiliary 203 (module 9.2; https://en.wikipedia.org/wiki/Roman_military_diploma).
- Actus Silvestri, Donation, Valla 1440, Alfonso and Eugenius IV, satraps; Eusebius, Life of Constantine 4.61–62 (modules 8.3, 10.4).
- B1: Dionysius 12.4.2–5; Piso consul 133; Gellius 6.3.37; Camillus' Concord and Momigliano (modules 3.1, 3.2).
- B2: Livy 2.1.7, 1.59, 2.5; Dionysius 5.18 on Brutus' children; denarius of 54; Suetonius, Julius 76–79; David's Brutus 1789; Dante, Inferno 4.127 and 34.61–67 (modules 1.6, 3.2, 5.4, 10.4).
- B3: Cicero, On the Laws 3.22; Res Gestae 4.4; Tacitus, Annals 3.56 (modules 5.2, 6.1).
- B4: Polybius 2.24 (Samnites 77,000; about three-fifths allied, module 3.4's computation); Lacinian tablet, Polybius 3.56.4; 3.77, 3.85; Livy 27.9–10; Appius Claudius (Plutarch, Pyrrhus 18–19).
- B5: Polybius 1.1.5, 6.3–10, 6.11–18, 6.57; Millar, Hölkeskamp, Mouritsen (module 4.5).
- B6: Tacitus, Annals 4.56 (Smyrna, 195); Suetonius, Augustus 50; Dio 51.20.6–7; Pola; Proculus parallel; Aurelius Victor 39 on Diocletian (modules 6.2, 8.2; Greek 7.1, 11.4).
- B7: Cicero, On Divination 1.72, 2.50; 163 BC Gracchus; Servius on the comet of 44; Tacitus, Annals 11.15 (AD 47); Theodosian Code 9.16.1, 16.10.1; Zosimus 5.41 (modules 1.2, 2.3, 8.3, 8.5).
- B8: Gaius 1.55; Seneca, On Mercy 1.15; Marcian, Digest 48.9.5; Shaw, Saller, Frier (module 9.3).
- B9: 225 and 300 denarii; Dio 79(78).36.3, 280 million sesterces, Loeb numbering with Boissevain's in brackets as house style requires; antoninianus about half silver in 215; P.Cair.Isid. 1 of 297; indiction (modules 0.3, 6.4, 7.4, 8.1, 8.2).
- B10: Aeneid 6.791–805, 8.714–728; Forum of Augustus dedicated 2 BC; Suetonius, Augustus 31.5; Augustus' chariot group in the Forum (Res Gestae 35.1; module 6.2), which settles the writer's doubt.
- C1: Dionysius 1.5.1, 1.61–62, 1.89–90, 1.28–30, 1.11.1; Livy 1.5.1 (modules 0.1, 1.2, 1.3).
- C2: Livy 5.49.1–7; Polybius 2.18.3, 2.22.5; Diodorus 14.116–117; Strabo 5.2.3; Suetonius, Tiberius 3.2; Plutarch, Camillus 22; Pliny 3.57 (Theopompus only, cited jointly, acceptable); Suetonius, Augustus 7.2; Mommsen (module 3.3).
- C3: Polybius 1.11.1–3, 1.14, 3.26; Harris; Hoyos; Livy 31.6–8 (modules 4.2, 4.4).
- C4: Diodorus 20.14.4–6; Plutarch, On Superstition 13; tophet scholarship as in module 4.1.
- C5: Appian, Civil Wars 1.7; Plutarch, Tiberius Gracchus 8.7; Rosenstein; de Ligt; census figures; Rathbone (module 5.1).
- C6: Letters to Atticus 2.1.3; Against Catiline 4.10; Sallust, Catiline 31.6 (modules 5.3, 5.6).
- C7: Res Gestae 34.1, 34.3, 35.2; Dio 53.12.3; Tacitus, Annals 1.2; no triumph outside the family after 19 BC (modules 6.1, 6.4).
- C8: Dio 69.20, 68.3, 69.1; Tacitus, Histories 1.16.1; Pliny, Panegyricus 7.4–6; Machiavelli, Discourses 1.10 (module 7.3).
- C9: Life of Constantine 1.27–32, 1.28.1; Pan. Lat. VI(7).21.3–5; Lactantius 44.5–6; Church History 9.9.10–11; Weiss; Barnes 2011; CIL VI 1139; Sol on coins into the 320s (module 8.3).
- C10: Juvenal 10.77–81; Fronto; five modii, about 200,000; Pro Sestio 106; Cleander 190; Pompeii notices (modules 9.4, 10.2). Dating "between about 110 and the late 120s" covers Satire 10, though it is the range of the whole corpus.
- D1: Dionysius 2.18–19; Augustine, City of God 6.5; Ennius' Aventine; Promathion; Wiseman's sixty-one versions; Dumézil, Wiseman, Feeney (modules 0.1, 1.4, 2.1).
- D2: Polybius 6.19–21, 6.39; plebiscite of 107; Nola 88; 500 denarii (Letters to Atticus 16.8); Claudius' donative; Tacitus, Histories 1.4; Dio 77(76).15.2; Procopius, Wars 5.1.4–8; eighteen months after 305; Aspar 471, Theoderic 488 (modules 5.2, 5.5, 7.1, 7.2, 7.4, 8.2, 8.5, 8.6, 9.2).
- D3: Horace, Epistles 2.1.156 in context; Euboean pottery at Sant'Omobono; Livius Andronicus 240; Feeney; Cicero's coinages; temple of Portunus; Athens 451/0; Gruen; Woolf (modules 1.1, 4.5, 5.6, 7.5, 10.3; Greek 6.2, 8.1).
- D4: Marcellinus Comes and Croke 1983; Jones 1964; Procopius' 130,000 pounds for 468; Brown, Goffart, Heather, Ward-Perkins, Wickham, Koepke and Baten (modules 0.3, 8.5, 8.6). Part D dispute box: Heather 2005, Halsall 2007, de Ste. Croix, Sherwin-White, all as in modules 8.5 and 2.5.
- D5: Juno Regina 396, Aesculapius 293, Magna Mater 204; Rajak on community grants; Rives 1999; Collatio 6.4, 15.3; Theodosian Code 16.10.2; laws of 391–392; Relatio 3.10 (modules 2.5, 8.1, 8.2, 8.4).
- Gaps dispute box: Finley, The Ancient Economy (1973); Hopkins, "Taxes and Trade in the Roman Empire" (JRS 1980; module 7.5); Shapur's battle against Zosimus' parley (1.36; module 8.1).
- Mark scheme: 30 + 50 + 50 + 70 = 200; Part C's 1 + 2 + 2 = 5; thresholds consistent with Greek module 9.4.
- House style: British spelling throughout; no em dashes (en dashes only in ranges); Cicero's treatises in English and speeches in Latin; Dio's Loeb numbers with Boissevain's in brackets where they differ; Octavian and Augustus used correctly by date.
