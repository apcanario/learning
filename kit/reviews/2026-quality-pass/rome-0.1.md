# Rome 0.1: How we know anything: the sources

Verdict: keep
Body words: 3384 (target 3000)

## Coverage
- First historians in Greek (Fabius Pictor, Cincius Alimentus) and why Greek: covered
- Cato's Origines: covered
- Latin annalists (Cassius Hemina, Calpurnius Piso, Valerius Antias, Claudius Quadrigarius, Licinius Macer), known in fragments, and the charge of invention: covered
- Raw material (Annales Maximi, consular and triumphal lists, family archives, funeral orations) and Cicero's and Livy's complaints: covered
- Polybius as outsider's analysis: covered
- Livy (142 books, 35 surviving, preface on legend): covered
- Dionysius and the Greek-city thesis: covered (content handed to module 1.3)
- Diodorus: covered
- Plutarch's Roman Lives: covered
- Appian and Cassius Dio for the later Republic: covered
- Antiquarians (Varro, Verrius Flaccus through Festus, Gellius, Macrobius): covered
- Imperial historians in outline (Velleius, Tacitus, Suetonius, Historia Augusta, Ammianus): covered
- Inscriptions (Lapis Niger, Duenos vase, Satricum stone, Scipio epitaphs, Res Gestae, Lyon tablet): covered
- Coins as propaganda: covered
- Pyrgi tablets: covered
- Archaeology in the Forum and on the Palatine: covered
- Hypercritical tradition (Niebuhr, Mommsen, Pais, Forsythe): covered
- Cornell, Carandini, Wiseman's dramatic inventions: covered
- How to judge a story first found in Livy: covered
- The four traps (Livy 1 as history, Dionysius as independent, the Historia Augusta, Ovid): covered
- Pointer back to Greek module 0.1: covered

## Findings
1. [should-fix] [lane] Section "The defining problem: a past written down late".
   Current: "T. P. Wiseman (<em>The Myths of Rome</em>, 2004) and Denis Feeney (<em>Literature and Religion at Rome</em>, 1998) reply that Rome had abundant myths of its own, told as history and performed on stage."
   Problem: The whole box restates the debate that module 2.1 owns (its prompt names "why the Romans are said to have had no mythology", and its section "A people without myths?" gives Rose, Dumézil, Wiseman and Feeney a bullet each). It also folds Feeney into Wiseman's stage thesis, whereas 2.1 gives Feeney a different answer (the question assumes a Greek definition of myth).
   Fix: replace the whole aside with: "<aside class="dispute"><strong>Where sources disagree.</strong> Whether Rome had a mythology of its own is disputed. H. J. Rose held that Romans had gods without stories and borrowed myths from Greece; Georges Dumézil (<em>Mythe et épopée</em>, 1968–73) and T. P. Wiseman (<em>The Myths of Rome</em>, 2004), in different ways, find Roman myth told as history. Module 2.1 weighs the answers.</aside>"
   Basis: rome/r-2.1.html, sections "Origins: numen and the three functions" and "A people without myths?"; prompt 2.1 in prompts-rome.json.

2. [should-fix] [lane] Section "Material sources".
   Current: "Carthaginian ties with Etruscan rulers at that date make Polybius' date for Rome's first treaty with Carthage (509/8; 3.22) credible against Mommsen, who moved it to 348."
   Problem: This is module 1.6's dispute box in one sentence (Mommsen, 348, the Pyrgi argument for the early date). It also gives Polybius' date as 509/8, where modules 0.3 and 1.6 convert his synchronism ("twenty-eight years before Xerxes crossed to Greece", 3.22.2) to 508/7.
   Fix: "Their bearing on Rome's first treaty with Carthage, which Polybius dates to 508/7 (3.22), is weighed in module 1.6."
   Basis: Polybius 3.22.1–2; rome/r-1.6.html, "The documentary evidence"; rome/r-0.3.html, "The first consuls and the Capitoline temple".

3. [error] [pointer] Section "Sulla's system under attack: Lepidus and Sertorius" in rome/r-5.3.html (an incoming pointer; not a fault in 0.1 and not counted against its verdict).
   Current: "now joined by a contemporary, Cicero; module 0.1 surveys these sources."
   Problem: 0.1 surveys Plutarch, Appian and Dio but never mentions Sallust, and treats Cicero only as a witness to the early record. The late-Republican writers are introduced in module 5.6, which covers Sallust's Histories and Cicero.
   Fix (in rome/r-5.3.html): "now joined by a contemporary, Cicero; module 0.1 surveys the later narratives and module 5.6 introduces Sallust and Cicero as writers."
   Basis: rome/r-0.1.html (no mention of Sallust anywhere); rome/r-5.6.html (Sallust's Catiline, Jugurtha and Histories; Cicero as orator, philosopher and letter writer).

## Confirmed
- 0.1 does not present Sallust, Caesar or Cicero as historians; its only late-Republican narratives are Appian and Dio, as its prompt asks; 5.6 introduces the late-Republican writers (review_notes; rome/r-5.6.html).
- Livy 6.1.2: most records perished in the burning of the city (Latin text).
- Livy 22.57.5 and 23.11.1–6: Fabius Pictor sent to Delphi after Cannae and his return (Latin text).
- Livy 21.38.3: Cincius Alimentus writes that he was Hannibal's prisoner (Latin text).
- Dionysius 1.6.2: Fabius and Cincius exact on their own times, summary on the period after the foundation (Loeb text).
- Plutarch, Romulus 3.1: Fabius followed Diocles of Peparethus in most points (Perrin text).
- Polybius 1.14 and 3.8–9: Fabius partisan; Hasdrubal's ambition as Fabius' cause of the war (text).
- Polybius 39.1: Postumius Albinus' apology for his Greek and Cato's mockery (text).
- Nepos, Cato 3.3–4: kings in book 1, Italian origins in books 2–3, generals unnamed (Latin text).
- Pliny, Natural History 8.11: Cato named the elephant Surus (Latin text).
- Pliny, Natural History 17.244: Piso dates the overthrow of chastity to the censors of 154 BC (Latin text).
- Dionysius 2.38–40: Piso's Tarpeia tries to disarm the Sabines (Loeb text).
- Livy 33.10.8 (Antias' exaggerated numbers) and 33.10.10 (Polybius "non incertum auctorem") (Latin text).
- Livy 4.7.12, 4.20.8, 4.23.1–3 and 7.9.5: Macer, the linen books, Tubero, and Macer's family glory (Latin text).
- Cicero, On the Orator 2.52 (pontifex maximus' whitened board until P. Mucius); Servius on Aeneid 1.373 (eighty books) (texts).
- Gellius 2.28.6 (Cato on dear grain and eclipses); Cicero, On the Laws 1.6 ("nihil ieiunius") and 2.59 (Twelve Tables learnt as boys) (texts).
- Cicero, On the Republic 1.25: the eclipse of about 350 AUC in Ennius and the Annales Maximi, earlier ones calculated back to Romulus (Latin text).
- Cicero, Brutus 62 (false triumphs, consulships, genealogies), 75 (Cato on banquet songs), 41–43 (Atticus on rhetoricians lying about Coriolanus) (Latin text).
- Livy 8.40.4–5: funeral eulogies and false captions; no contemporary writer (Latin text).
- Polybius 1.1.5 (under fifty-three years), 3.22–26 (treaties in the aediles' archive), 6.53–54 (imagines and funeral speech) (text).
- Livy 1.19.3 (Augustus' single closure of Janus), 1.4.7 (Larentia as lupa), 1.18.2 (Numa and Pythagoras), Preface 6, 7 and 10 (Latin text).
- Dionysius 1.7.2 (arrival at the end of the civil war), 1.3.4 (publication in 7 BC), 1.7.3 (annalists named), 1.79.11 (hut of Romulus) (Loeb text).
- Plutarch, Demosthenes 2.2 (Latin learnt late), Romulus 8 (the story's dramatic character), Camillus 22.4 (Aristotle's Lucius) (Perrin text).
- Augustine, City of God 6.3 (41 books, 25 human and 16 divine) and 6.5 (three theologies); Suetonius, On Grammarians 17 (Verrius' calendar at Praeneste) (texts).
- Lapis Niger found by Boni in 1899, CIL I² 1, recei, kalatorem, sakros esed; Duenos vase found 1880, CIL I² 4 (standard corpora).
- Res Gestae 1.1 "dominatione factionis"; Suetonius, Augustus 101.4 (bronze before the Mausoleum) (texts).
- Lyon tablet found 1528, ILS 212, against Tacitus, Annals 11.24 (standard corpora).
- Barbatus elogium CIL I² 7 against Livy 10.12.3 (Etruria to Barbatus, Samnium to Fulvius) (texts).
- Wachter (1987) holds the surviving Barbatus text original, with its opening erased; the traditional view a replacement (https://en.wikipedia.org/wiki/Sarcophagus_of_Lucius_Cornelius_Scipio_Barbatus, citing Wachter).
- Frier (1979): the eighty-book edition "more probably a massive reworking of materials in the Augustan period", and its role in shaping the tradition rested on insecure foundations (https://press.umich.edu/Books/L/Libri-Annales-Pontificum-Maximorum).
- RRC 20/1, wolf and twins, 269–266 BC; RRC 235/1, Sex. Pompeius Fostlus, 137 BC (Crawford).
- Table: Livy 1–10 to 293 and 21–45 for 218–167; Dionysius 1–10 and most of 11; Diodorus 1–5 and 11–20; Dio 36–60, 69 BC to AD 46; Appian's Civil Wars 133–35 BC.
- Historia Augusta: Hadrian to Carus, Carinus and Numerian, six names, gap 244–260; Dessau, Hermes 1889; Momigliano 1954; Enmann 1884.
- Modern titles and dates: Beaufort 1738; Niebuhr 1811–32; Mommsen 1854–56; Pais 1898–99; Forsythe 2005; Cornell 1995 and FRH 2013; Carandini 1997 and 2006; Wiseman 1979, 1995, 1998, "Reading Carandini" JRS 2001, 2004; Oakley 1997–2005; Badian 1966; Gelzer on Fabius (Hermes 1933); Leuze 1909; Perl 1957; Dumézil 1968–73.
- Varro, On the Latin Language 5.148–150: three explanations of the Lacus Curtius (Procilius, Piso, Cornelius and Lutatius) (Latin text).
- Pointers true of their targets: Greek module 0.1 (sources; "Treating Ovid as Greek"), module 1.3 (Dionysius' Greek-city thesis), 1.4 (Carandini's wall), 1.6 (Satricum stone, Publicola possible).
- Incoming pointers true of 0.1: from 1.6, 2.1, 2.3, 3.1, 3.2, 3.3, 4.5, 5.2, 5.6, 6.1 and 6.3 (crosscheck section 1).
- Gabii as Zopyrus (shared with 1.6) was kept by the cohesion review as 0.1's method example; not re-flagged.
