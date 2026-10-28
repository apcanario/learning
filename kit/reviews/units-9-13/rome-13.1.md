# Rome 13.1: Philosophy comes to Rome

Verdict: fix
Body words: 2,822 (target 2,500); 2,831 with all fixes below applied (tested on a scratch copy with `check.py --target 2500`)

## Coverage
- 4.5's three episodes (181, 161, 155), a sentence each with a pointer: covered
- Censors' edict of 92 (Suetonius, Gramm. 25; Gellius 15.11.2), displeasure without expulsion: covered
- Athenaeus 12.547a, the two Epicureans under a Lucius Postumius: covered (with Aelian)
- What the measures show: covered (Gruen; "None of these measures names a doctrine")
- Panaetius in Scipio's household, pointer to 4.5 (Velleius 1.13.3, "Scipionic circle"), kept to what he taught Romans: covered
- Posidonius at Rhodes, Cicero as student, Pompey as general: covered
- Philodemus with Piso handed to 13.3: covered (pointer)
- Diodotus in Cicero's house: covered
- Athenodorus Cordylion with Cato, introduced as 13.4's prompt requires: covered
- Athenodorus son of Sandon with Augustus, Strabo 14.5.14 keeping them apart: covered
- Arius Didymus at Augustus' court: covered
- Athens and Rhodes as finishing school: covered
- Cicero's Latin philosophy in outline, pointer to 5.6: covered
- Why Romans took the ethics and left the theory (the question Greek 12.7 hands on): covered
- What Roman suspicion was about: covered
- Tacitus, Agricola 4: covered
- Format (8 sections, 4 dispute boxes, 10 questions, 3 carry-forward items): covered

## Findings
1. [error] [accuracy] Section "Panaetius and the Romans who heard him".
   Current: "Cicero's Scipio recalls discussing the state with Panaetius in Polybius' presence"
   Problem: At On the Republic 1.34 it is Laelius who speaks, remembering that Scipio often discussed the state with Panaetius in front of Polybius ("memineram persaepe te cum Panaetio disserere solitum coram Polybio"). Scipio does not recall it himself.
   Fix: "Cicero's Laelius recalls Scipio discussing the state with Panaetius in Polybius' presence"
   Basis: Cicero, De re publica 1.34, Latin Library text (thelatinlibrary.com/cicero/repub1.shtml), speaker Laelius.

2. [error] [accuracy] Section "Posidonius at Rhodes", dispute box.
   Current: "Cicero's list of his teachers (<em>On the Nature of the Gods</em> 1.6) supports Plutarch, but the <em>Brutus</em> is a history of oratory with no reason to name a philosopher."
   Problem: The Brutus does name philosophers in the very passage cited: Philo (306), Diodotus (309) and six months with Antiochus at Athens on this same journey (315). The report's next section uses Brutus 306–316 for exactly these men. So the box's explanation for the silence is false and contradicts the body. Its silence about Posidonius is real and should be stated as it is.
   Fix: "Cicero's list of his teachers (<em>On the Nature of the Gods</em> 1.6) supports Plutarch, though the <em>Brutus</em>, which names Philo, Diodotus and Antiochus, is silent."
   Basis: Cicero, Brutus 306, 309, 315–316 (known text); the report's own section "Athens and Rhodes: the finishing school".

3. [error] [attribution] Section "Edicts and expulsions, 181–92 BC".
   Current: "In 155 Carneades argued for justice one day and against it the next, and Cato urged the Senate to send the embassy home (Plutarch, <em>Cato Maior</em> 22)."
   Problem: The single citation covers both clauses, but Plutarch, Cato Maior 22 has the embassy, Carneades' charm and Cato's demand, not the two speeches on justice. Those come from Lactantius, drawing on On the Republic 3. Module 4.5 and Greek module 7.2 both credit Lactantius.
   Fix: "In 155 Carneades argued for justice one day and against it the next (Lactantius, <em>Divine Institutes</em> 5.14), and Cato urged the Senate to send the embassy home (Plutarch, <em>Cato Maior</em> 22)."
   Basis: Lactantius, Divine Institutes 5.14.3–5 (the ANF translation numbers it book 5, ch. 15: ccel.org/ccel/schaff/anf07.iii.ii.v.xv.html, "disputed copiously on the subject of justice ... on the next day the same man overthrew his own argument"); rome/r-4.5.html and greece/r-7.2.html.

4. [minor] [attribution] Section "Panaetius and the Romans who heard him".
   Current: "Posidonius named Rutilius, Tubero and Mucius Scaevola as the only Romans who kept Fannius' sumptuary law (Athenaeus 6.274)."
   Problem: Athenaeus does not name Posidonius in the Fannian passage (6.274c–e). He cites him for Roman frugality just before it. Jacoby (FGrHist 87 F 59) and Edelstein–Kidd (F 265) print 6.273a–275b as Posidonius, so the attribution is the editors' inference. Keep the reporter separate from the claim.
   Fix: "Athenaeus, probably following Posidonius, names Rutilius, Tubero and Mucius Scaevola as the only Romans who kept Fannius' sumptuary law (6.274c–e)."
   Basis: Athenaeus 6.273–275, Loeb translation on LacusCurtius (penelope.uchicago.edu/Thayer/E/Roman/Texts/Athenaeus/6E*.html): "As Poseidonius says" comes two paragraphs before "Mucius Scaevola, Aelius Tubero, and Rutilius Rufus ... observed ... the Fannian Law"; attalus.org fragment list (Jacoby F 59 = Kidd 265, Athen. 6.273a–275b).

5. [minor] [accuracy] Section "Posidonius at Rhodes".
   Current: "Strabo calls him Pompey's friend (11.1.6)." and "gained a patron and a subject for his <em>Histories</em>."
   Problem: Strabo 11.1.6 says Posidonius "among other works wrote also the history of Pompey", which is a separate work. The 52-book Histories continuing Polybius are not shown to have reached Pompey's eastern wars, and how far they ran is disputed.
   Fix: replace the first with "Strabo calls him Pompey's friend and says he wrote Pompey's history (11.1.6)." and the second with "gained a patron and a subject."
   Basis: Strabo 11.1.6, Loeb translation on LacusCurtius (penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/11A*.html).

6. [minor] [pointer] Section "Why the Romans took the ethics".
   Current: "Greek module 12.7 ends by asking why Romans kept"
   Problem: 12.7 does not ask the question. Its first carry-forward item says Romans kept the ethics and left the rest, "as Rome module 13.1 asks why", which hands the question to this module.
   Fix: "Greek module 12.7 hands on the question why Romans kept"
   Basis: greece/r-12.7.html, Carry forward 1.

7. [minor] [accuracy] Section "Why the Romans took the ethics", list item 1.
   Current: "Virtue is not possessed like an art unless it is used, and"
   Problem: This turns Cicero's contrast round. He says an art can be held as knowledge even when unused, but virtue lies wholly in its use ("nec vero habere virtutem satis est quasi artem aliquam nisi utare ... virtus in usu sui tota posita est").
   Fix: "Virtue, unlike an art, cannot be held without being used, and"
   Basis: Cicero, On the Republic 1.2 (Latin Library text, opening confirmed).

8. [minor] [accuracy] Section "Edicts and expulsions, 181–92 BC".
   Current: "Consuls of that name held office in 173 and 154, so the date is uncertain."
   Problem: Earlier consuls named Lucius Postumius held office after Epicurus opened his school (305, 294, 291, 234, 229, 215). The years 173 and 154 are the plausible candidates, not the only ones.
   Fix: "The likely consuls of that name held office in 173 and 154, so the date is uncertain."
   Basis: consular fasti (known); en.wikipedia.org/wiki/Alcaeus_and_Philiscus (173 or 154, after Gruen 1990/1996, p. 177).

9. [minor] [register] Section "Why the Romans took the ethics", list item 3.
   Current: "and Romans kept the two apart,"
   Problem: "The two" can be read as Stoic theology and Epicurean indifference, the nearest pair. The point is that philosophy and public cult were kept apart.
   Fix: "and Romans kept school and cult apart,"
   Basis: sense of the passage; rome/r-2.1.html (Varro's natural theology is "for the schools, not the forum").

10. [minor] [register] Section "Self-test", question 3.
    Current: "Gelzer and von Ungern-Sternberg found no evidence for Plotius' politics."
    Problem: The answer merges the two scholars. In the body (and in fact), Gelzer refuted Marx's thesis of a political tendency, and von Ungern-Sternberg concluded that nothing certain can be said about Plotius' politics.
    Fix: "Gelzer rejected the thesis, and von Ungern-Sternberg found nothing certain about Plotius' politics."
    Basis: von Ungern-Sternberg, "Die populären Beispiele in der Schrift des Auctors ad Herennium", Chiron 3 (1973) 143–162 (publications.dainst.org/journals/chiron/article/view/755/5124): Gelzer, Kleine Schriften I (1962) 211ff., refuted Marx; "Über die politische Haltung des Plotius Gallus läßt sich also nichts Sicheres sagen".

11. [minor] [style] Section "Self-test", question 7.
    Current: "the son of Sandon taught Augustus, was honoured"
    Problem: The teaching came before 27 BC. The body rightly says "the young Octavian", and house style is Octavian before 27.
    Fix: "the son of Sandon taught Octavian, was honoured"
    Basis: AGENT-SPEC.md, Rome course; Strabo 14.5.14.

## Confirmed
- Seam with 13.2 (as now on disk): Panaetius' On Proper Functions and the four personae belong to 13.2, and 13.1 only points there. Posidonius' doctrine appears in 13.2 only as Galen's and Seneca's evidence, while Rhodes and his visitors are 13.1's. Cicero's Stoic coinages are in 13.2's table, and 13.1 gives one line with a pointer to 5.6. No dispute box, anecdote or Self-test question is shared. 13.2's "how Greek teachers got into Roman houses is deep dive module 13.1" is true.
- Unit 13 is "Deep dive III" in roman-syllabus.html, so "deep dive module 13.x" is correct.
- Pointers checked against their targets: 4.5 (181 with Livy 40.29, 161 with Gellius 15.11.1, 155 and Cato, Panaetius with Velleius 1.13.3, the Scipionic circle box); 5.6 (the works of 45–44, his reason from On the Nature of the Gods 1.7, the coinages, Lucretius on the poverty of Latin); 2.1 (Scaevola's and Varro's three theologies, Cotta at On the Nature of the Gods 3.5–6); 5.1 (Blossius, the Stoic, and the Capitol remark from On Friendship 37); 5.2 (Rutilius condemned by an equestrian jury in 92); Greek 7.2 (outlines the systems); Greek 7.3 (the boy finished at Athens or Rhodes, "as Cicero did"); Greek 12.7 (Panaetius' dropped doctrines, Posidonius' embassy of 87/86 with Marius 45, the travels, Athenodorus at Pergamum with Diogenes Laertius 7.34, the Stobaean epitome "usually credited to Arius Didymus"); Greek 12.8 (Philo's doctrine, Antiochus' Roman following to 13.3).
- Prompts of unwritten neighbours: 13.3 owns Philodemus and Piso, Antiochus and the Old Academy, and Cratippus with Cicero's son, so all three pointers fit. 13.4 asks 13.1 to introduce Athenodorus Cordylion, which it does without telling Cato's Stoicism. The "restless and meddling" charge (Annals 14.57) fits 13.4's Stoic-opposition debate.
- Gruen, Studies in Greek Culture and Roman Policy (Brill 1990; UC Press paperback 1996), ch. V "Philosophy, Rhetoric, and Roman Anxieties" (ucpress.edu table of contents). That he took the expulsions as symbolic is confirmed by BMCR 1994.02.11 (review of Gruen 1992): "The senate's periodic expulsion of Greek philosophers, rhetoricians, and diviners in G.'s view had only symbolic significance."
- Marx's edition of the Rhetorica ad Herennium, 1894, and his thesis: von Ungern-Sternberg cites F. Marx, Incerti auctoris de ratione dicendi ad C. Herennium libri IV (1894), whose thesis linked the edict to Marius and Plotius. Gelzer's rejection: "Die angebliche politische Tendenz in der dem C. Herennius gewidmeten Rhetorik", Kleine Schriften I (1962). Von Ungern-Sternberg, Chiron 3 (1973) 143–162 (dainst.org).
- Zeller's "eclecticism", and Dillon and Long (eds.), The Question of "Eclecticism": Studies in Later Greek Philosophy (University of California Press, 1988), whose introduction re-examines "the traditional (since Zeller) characterization" (publishing.cdlib.org).
- Göransson, Albinus, Alcinous, Arius Didymus (Studia Graeca et Latina Gothoburgensia 61, 1995). BMCR 1995.12.08 (Brad Inwood) describes "a more general reconsideration of the traditional portrait of Arius Didymus as a doxographer", so the report's wording is accurate and rightly states no more.
- Rawson 1985 and Volk 2021 (titles and years) are correct.
- Athenaeus 12.547a and Aelian, Historical Miscellany 9.12 (en.wikipedia.org/wiki/Alcaeus_and_Philiscus).
- Athenaeus 6.274c–e names Mucius Scaevola, Aelius Tubero and Rutilius Rufus as the only observers of the Fannian law, and calls them followers of the Stoa (LacusCurtius Loeb). Only the Posidonius attribution needed a hedge (finding 4).
- On Ends 4.23 (Panaetius to Tubero on enduring pain: Wikipedia, "Q. Aelius Tubero (Stoic)", citing Fin. 4.9.23); 2.24 (Laelius heard Diogenes, then Panaetius: Smith's Dictionary "de Fin. 2.8"); 4.79 (softened Stoic harshness: Smith "de Fin. 4.28"); 5.8 (Staseas kept by Piso "for many years": book 5, ch. 3, monadnock.net).
- On Duties 3.10: "P. Rutilium Rufum ... qui Panaetium audierat", reported through a letter of Posidonius (studentville.it Latin text).
- Pro Murena 75 (Tubero, the goatskins and Samian ware, the lost praetorship). Q. Fabius Maximus was Scipio's nephew through his brother (patruus).
- Strabo 11.1.6 calls Posidonius "a friend of Pompey" (LacusCurtius).
- Plutarch, Pompey 42 (on the return from the East, at Rhodes, a talent to each sophist; Posidonius wrote up his discourse against Hermagoras: perseids).
- Plutarch, Cicero 3.4 (fear of Sulla, health as pretext), 4.2 (plan to move to Athens), 4.4 (Apollonius son of Molon, and Posidonius at Rhodes) (lexundria).
- Plutarch, Cicero 39 and Caesar 54 are left to 5.6 and 13.4, and 13.1 does not use them.
- Letters to Atticus 2.20 for Diodotus' death and legacy: the passage is 2.20.6 ("Diodotus mortuus est; reliquit nobis HS fortasse centiens"), and the section could be added.
- Letters to Atticus 2.1.2: Posidonius frightened off by the memoir of the consulship.
- Tacitus, Annals 4.43 (the Massilians cite Smyrna's adoption of the exiled Rutilius as citizen) and Agricola 4 (wording and Massilia).
- On the Orator 1.229–230 (Rutilius refuses supplication; the Socrates comparison follows).
- Suetonius, On Grammarians and Rhetoricians 25 (edict) and 26 (Cicero's letter to Titinius on Plotius); Gellius 15.11.1–2.
- On the Orator 3.93–94 ("ludus impudentiae"); Tacitus, Dialogue on Orators 35.1.
- On the Nature of the Gods 1.6 (Diodotus, Philo, Antiochus, Posidonius); Brutus 306–316 (Philo in 88, Molon, Diodotus, Antiochus six months, Asia, Rhodes, "prope mutatus"); Brutus 309 (Diodotus "nuper est domi meae mortuus"); Tusculan Disputations 5.113 (blind Diodotus, the lyre, geometry); Tusculan Disputations 2.61 (Pompey "decedens ex Syria", the gout); Pliny, Natural History 7.112 (lictor and fasces).
- Strabo 14.5.14 (Cordylion with Cato; the son of Sandon, Caesar's teacher, Boethus, reform of Tarsus); Plutarch, Cato Minor 10; Diogenes Laertius 7.34; Plutarch, Sayings of Kings and Commanders 207c (the alphabet).
- Suetonius, Augustus 89.1; Plutarch, Antony 80–81 ("polykaisarie"); Dio 51.16 (same numbering in Loeb and Boissevain); Seneca, Consolation to Marcia 4–5.
- On Ends 1.16 (Phaedrus and Zeno); Nepos, Atticus 2–4; Suetonius, Julius 4; Horace, Epistles 2.2.43–45; Plutarch, Brutus 24; On Ends 5.1–5; Academica 2.5–7; On Ends 1.1–3; Augustine, Confessions 3.4.7 (the Hortensius and "annum aetatis undevicensimum" are both in that chapter).
- On Duties 1.19 and 1.153–158; Seneca, Letters 48.6; Tacitus, Annals 14.57; Tusculan Disputations 2.1 and On the Orator 2.156 (Ennius' Neoptolemus); Suetonius, Nero 52.
- All four dispute boxes have two to four sentences with named sources or scholars on each side. No em dashes, and British spelling throughout.

## Errors noticed in other reports
- None found in the passages of 4.5, 5.6, 2.1, 5.1, 5.2, 13.2, Greek 7.2, 7.3, 12.7 and 12.8 checked for this review.
