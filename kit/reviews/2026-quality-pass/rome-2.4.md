# Rome 2.4: House, family and the dead

Verdict: fix
Body words: 2844 (target 2500; ceiling 2875, so the fixes below are kept word-neutral or close to it)

## Coverage
- the paterfamilias as priest of the household: covered
- the Lares: household Lar, the Pompeian lararia and their snakes, the crossroads Lares and Augustus' reorganisation: covered
- the Penates and Vesta at the hearth: covered (Vesta thin, handed to 2.3)
- the Genius of the master and the Juno of the woman: covered
- rites of passage (naming day, bulla, toga of manhood, confarreatio and its alternatives): covered
- the aristocratic funeral in Polybius 6.53–54 (masks, eulogy, parade): covered
- cremation and inhumation, roadside tombs, columbaria, epitaphs: covered
- the Manes, Parentalia, Feralia, Lemuria and the black beans, the mundus: covered
- ghosts in Plautus' Mostellaria and Pliny, Letters 7.27: covered
- private magic: curse tablets, amulets, Pliny, Natural History 30, Apuleius' Apology: covered
- pointer to Greek module 8.4 for the Greek comparison: covered

## Findings
1. [error] [pointer] Section "Penates, Vesta, the Genius and the Juno".
   Current: "(modules 1.3 and 2.2)"
   Problem: Module 2.2 never mentions the Penates or Lavinium's Penates. Module 1.3 does: "Lavinium kept Rome's Penates", and the consuls sacrificed there.
   Fix: "(module 1.3)"
   Basis: rome/r-2.2.html (no occurrence of "Penates"); rome/r-1.3.html.
2. [should-fix] [attribution] Section "The Manes and the days of the dead".
   Current: "Plutarch (<em>Romulus</em> 11) puts Romulus' foundation pit"
   Problem: This is a foundation-era story, but the box does not say that the teller wrote some eight centuries later.
   Fix: "Plutarch (<em>Romulus</em> 11), eight centuries on, puts Romulus' foundation pit"
   Basis: AGENT-SPEC source-criticism rule.
3. [minor] [style] Section "The Lares: house and crossroads".
   Current: "(module 11.3)"
   Problem: 11.3 is a deep dive (unit 11, "Deep dive I"), and AGENT-SPEC wants deep dives named as such. Its syllabus prompt does cover the collegia, their banning and revival.
   Fix: "(deep dive module 11.3)"
   Basis: AGENT-SPEC; roman-syllabus.html, 11.3.
4. [minor] [style] Section "The Manes and the days of the dead".
   Current: "(module 12.5)"
   Problem: 12.5 is a deep dive (unit 12, "Deep dive II: the Aeneid"). The target is right, since its prompt covers book 6 against Odyssey 11.
   Fix: "(deep dive module 12.5)"
   Basis: AGENT-SPEC; roman-syllabus.html, 12.5.
5. [minor] [style] Sections "The household as a congregation", "Penates, Vesta, the Genius and the Juno" and Self-test question 1.
   Current: "<em>De agricultura</em>" (twice) and "<em>On the Birthday</em>"
   Problem: The group cites the same works two ways. 2.1 and 2.2 cite Cato as On Agriculture, as the course does twelve times, against twice here. 2.3 cites Censorinus as De die natali, as the course does four times, against once here.
   Fix: "<em>On Agriculture</em>" (both places) and "<em>De die natali</em>"
   Basis: count of citation forms across rome/*.html.

## Confirmed
Checked against the texts as I know them, unless a URL is given.
- Festus s.v. publica sacra; Cato, On Agriculture 2.1, 5.3–4 (only at the Compitalia; no haruspex or Chaldaean), 143.2 (the vilica's crowns on the Kalends, Nones and Ides); Cicero, On the Laws 2.22 and 2.47–53; Livy 5.46.2–3 (Fabius Dorsuo; also in 3.3, for a different purpose, which is acceptable)
- Plautus, Aulularia prologue (incense, wine, garlands; the pot under the hearth); Servius on Aeneid 5.85 (genius loci shown as a snake); Aeneid 5.84–96
- Festus s.v. pilae (effigies for the free, balls for slaves); collegia banned in 64 BC; Pliny, Natural History 3.66 (265 compita Larium); Ovid, Fasti 5.145–146; Dio 55.8 (the reform of 7 BC)
- Apuleius, On the God of Socrates 15 (Lar familiaris and larva); Samter 1901; Flower, The Dancing Lares and the Serpent in the Garden (2017)
- Cicero, On the Nature of the Gods 2.68 (penus or penitus); Censorinus 3.1 and 2.2–3 (no blood on the birthday; written AD 238); Seneca, Letters 110.1; Pliny, Natural History 2.16; Horace, Odes 3.17.14–16 and Epistles 2.1.143–144
- Macrobius, Saturnalia 1.16.36 (dies lustricus, eighth and ninth day); Juvenal 5.164–165; Persius 5.30–31; Ovid, Fasti 3.771–788; Gaius, Institutes 1.110–113 (usus with the trinoctium, coemptio, confarreatio with Jupiter Farreus and ten witnesses); Tacitus, Annals 4.16 (AD 23); Plutarch, Roman Questions 87; Catullus 61; Varro in Nonius (three asses)
- On the Laws 2.58–59 and 2.64 (Twelve Tables funeral clauses; Solon); Polybius 6.53–54 in every detail given (upright on the Rostra; wooden shrines; actors of similar build; praetexta, purple, gold; ivory chairs; oldest ancestor first); Pliny, Natural History 35.6; Sallust, Jugurtha 4.5–6; Tacitus, Annals 3.76; Dio 56.34 (Romulus and Pompey at Augustus' funeral); Flower, Ancestor Masks (1996)
- On the Laws 2.56–57 and Pliny, Natural History 7.187 (the Cornelii and Sulla); Varro, On the Latin Language 5.23 (os resectum); Scipio Barbatus, consul 298, Saturnian epitaph; CIL VI 15346 (Claudia); CIL XIV 2112 (Lanuvium, AD 136); Horace, Satires 1.8.8–16; Nock, HThR 25 (1932); Morris 1992
- On the Laws 2.22 ("suos leto datos divos habento"); Ovid, Fasti 2.533–638 (Parentalia, Feralia, Caristia; offerings at 535–542; the howling dead at 547–556; Tacita at 571–582), 5.419–492 and 5.429–444 (Lemuria; "Manes exite paterni"); Gellius 10.15.12; Macrobius, Saturnalia 1.16.16–18 (mundus patet: 24 August, 5 October, 8 November); Plutarch, Romulus 11; Warde Fowler, JRS 2 (1912)
- Plautus, Mostellaria (the murdered guest refused by Acheron); Pliny, Letters 7.27 (to Sura; Athenodorus); Lucian, Lover of Lies 30–31; Suetonius, Caligula 59
- Pliny, Natural History 28.17–18, 30.1, 30.12 (senatus consultum of 97 BC), 30.14–17, 28.39 (fascinum); about 130 tablets at Bath; Tacitus, Annals 2.69; Horace, Satires 1.8.23–33; Apuleius, Apology 25–26, at Sabratha about 158–159; Cicero, On the Republic 4.12 in Augustine, City of God 2.9; Rives, Classical Antiquity 22 (2003)
- Pointers checked against their targets: 2.1, 2.3, 6.2 (which itself points back here for the crossroads reform), Greek 8.4 (Solon's funeral law; Anthesteria "Out of doors, Keres"; Genesia; bones in hero cult), Greek 8.1 (curse tablets; Graf), 1.1 (cremation and inhumation in Latium), 1.4 (Remus' ghost and the Lemuria), 9.3 and 10.3 (per their syllabus prompts: manus marriage; ancestor masks and verism)
- Incoming pointers that describe this report correctly: 3.2 (the funeral), 6.2 (the crossroads reform), 7.1 (Germanicus' curse tablets)
