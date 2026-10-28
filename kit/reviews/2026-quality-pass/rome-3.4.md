# Rome 3.4: The Samnite Wars and the Roman system in Italy

Verdict: fix
Body words: 2789 (target 2500)

## Coverage
- the Samnites and their federation: covered
- the three Samnite Wars: covered
- the Caudine Forks (321) and the yoke: covered
- Sentinum (295) against Samnites, Gauls, Etruscans and Umbrians, and Decius Mus' devotio: covered (devotio as exemplum handed to module 3.2)
- Appius Claudius Caecus, the Via Appia of 312 and the first aqueduct: covered
- Latin and citizen colonies and the roads as instruments of control: covered
- the alliance system, what the allies owed and got: covered
- the formula togatorum: covered
- the manipular legion against the phalanx: covered
- Roman and allied manpower in 225 (Polybius 2.24): covered (full table)
- why Rome united Italy when no Greek city united Greece, with Greek modules 5.2 and 6.2: covered
- grades of citizenship in Republican Italy, as module 7.4 points here ("the graded statuses of Republican Italy (module 3.4)"): covered, in the status table (full citizens, citizens without the vote, Latins, allies) and in Carry forward 2

## Findings
1. [error] [accuracy] Section "The alliance system and the formula togatorum".
   Current: "and lent them to Rome in 260 (1.20.14)."
   Problem: Polybius 1.20.14 is about the ships borrowed for Rome's first crossing to Messana, in 264. Module 3.5 cites the same passage correctly for 264.
   Fix: "and lent them to Rome for the crossing of 264 (1.20.14)."
   Basis: Polybius 1.20.13–14, Loeb translation quoted at https://novoscriptorium.com/2019/05/03/how-when-and-for-what-reasons-the-romans-first-took-to-the-sea/; rome/r-3.5.html, "Ships and letters".

2. [error] [accuracy] Section "Appius Claudius Caecus", dispute box.
   Current: "and the elogium in the Forum of Augustus records only towns taken from the Samnites, the road, the water and a temple."
   Problem: The elogium also lists his offices, his rout of a Sabine and Etruscan army and his prevention of peace with Pyrrhus. What it leaves out is the controversial side of the censorship: freedmen's sons, the humble spread through all the tribes, the Potitii. The full text is known from the copy at Arretium.
   Fix: "and the elogium of the Forum of Augustus, known from a copy at Arretium, lists his offices, Samnite towns taken, a Sabine and Etruscan army routed, peace with Pyrrhus prevented, the road, the water and the temple of Bellona, but nothing of freedmen or the Potitii."
   Basis: CIL XI 1827 = ILS 54 ("complura oppida de Samnitibus cepit, Sabinorum et Tuscorum exercitum fudit, pacem fieri cum Pyrrho rege prohibuit, in censura viam Appiam stravit et aquam in urbem adduxit, aedem Bellonae fecit"); summary and image at https://www.ancientrome.ru/art/artworken/img.htm?id=6189.

3. [error] [accuracy] Section "Why Rome united Italy and no Greek city united Greece", item 2.
   Current: "was resented as confiscation and vanished in 404."
   Problem: The cleruchies were lost in 404 but came back in the fourth century. The charter of the Second Athenian League (377) renounced Athenian land in allied territory, and Athens then sent cleruchs to Samos from 365, and later to Potidaea and the Chersonese.
   Fix: "was resented as confiscation, renounced in the charter of the Second Athenian League in 377 and revived at Samos in 365."
   Basis: not searched (standard): the Decree of Aristoteles, IG II² 43 (378/7); Diodorus 18.18.9 (the Samians restored in 322 after forty-three years of exile).

4. [should-fix] [register] Section "Self-test", question 6.
   Current: "A citizen colony was some 300 Roman families guarding a coast, exempt from the legions (Livy 27.38)."
   Problem: Livy 27.38 shows no settled exemption. In 207 the maritime colonies claimed it, and the Senate upheld it only for Antium and Ostia while the enemy was in Italy. The body correctly says "claimed".
   Fix: "A citizen colony was some 300 Roman families guarding a coast, who claimed exemption from the legions; in 207 the Senate upheld the claim only for Antium and Ostia (Livy 27.38)."
   Basis: Livy 27.38.3–5, quoted at https://www.keytoumbria.com/Umbria/Maritime_Colonies_(338_-_241_BC).html.

5. [should-fix] [lane] Section "Sentinum and the end of Samnite independence, 298–264", dispute box.
   Current: "Inscriptions disagree too: the epitaph of Scipio Barbatus, consul in 298, credits him with towns in Samnium and all Lucania, where Livy (10.11–12) sends him to Etruria."
   Problem: Module 0.1 has a full dispute box on the same epitaph against the same passage of Livy (CIL I² 7; Wachter's dating), and crosscheck section 3 flags 0.1 ~ 3.4. The epitaph concerns 298, not Sentinum. A pointer keeps self-test question 1 supported.
   Fix: "The epitaph of Scipio Barbatus, consul in 298, contradicts Livy's provinces for that year (module 0.1)."
   Basis: rome/r-0.1.html, dispute box beginning "The epitaph of Lucius Cornelius Scipio Barbatus".

6. [should-fix] [figure] Section "Colonies and roads as instruments of control".
   Current: "<strong>Citizen colonies</strong>: about 300 Roman families as a coastal garrison,"
   Problem: The figure is unsourced. Livy gives 300 colonists for Tarracina, and the number is usually extended to the other maritime colonies.
   Fix: "<strong>Citizen colonies</strong>: about 300 Roman families as a coastal garrison (Livy 8.21.11, for Tarracina),"
   Basis: Livy 8.21.11; https://www.keytoumbria.com/Umbria/Maritime_Colonies_(338_-_241_BC).html ("documented only for Tarracina in 329").

7. [minor] [figure] Section "Sentinum and the end of Samnite independence, 298–264".
   Current: "Livy gives 25,000 enemy dead against 8,700 Romans."
   Problem: The figures are attributed but carry no chapter.
   Fix: "Livy gives 25,000 enemy dead against 8,700 Romans (10.29)."
   Basis: Livy 10.29: 25,000 killed and 8,000 captured, 7,000 dead in Decius' army and 1,700 in Fabius' (https://fgh.perseids.org/read/latinLit/phi0914/phi001/perseus-eng3/10.29.13-10.30.7).

8. [minor] [style] Section "Colonies and roads as instruments of control".
   Current: "(<em>On the Agrarian Law</em> 2.73)"
   Problem: De lege agraria is a speech, and AGENT-SPEC asks for speeches by Latin title. The English form is used elsewhere too (2.3, 4.1, 5.1, 5.2, 5.3), so change all of them or none.
   Fix: "(<em>De lege agraria</em> 2.73)"
   Basis: AGENT-SPEC.md, citation conventions.

## Confirmed
- Livy 7 to 10 ends in 293; Oakley's commentary on books 6 to 10; Polybius 2.18–23.
- Salmon (1967), Dench (1995), Scopacasa (2015); touto and meddix tuticus; Monte Vairano; Pietrabbondante; the four peoples (Pentri, Caudini, Hirpini, Carricini).
- Livy 7.19.4 and Diodorus 16.45.8 (treaty of 354); Livy 7.29–31 (Capua's deditio); Diodorus' silence on the First War.
- Livy 8.22–23 (Fregellae, 328); 8.23.12 (Publilius Philo, the first prorogation).
- Livy 9.2–6 (Caudium); 9.3 (Herennius Pontius' advice); 9.5.2 ("Claudiusque etiam scribit", sponsio not foedus); 600 equites as hostages; 9.8–11 (Postumius strikes the fetial); 9.12–15.
- Diodorus 19.72 (Lautulae plainly a defeat) against Livy 9.23; Livy 9.44–45 (Bovianum 305, peace 304); 10.3 (Vestini, 302).
- Livy 10.16–18 (Gellius Egnatius); 10.27–29 (Sentinum); 10.30 (exaggerated totals rejected); Polybius 2.19.5–6 (Samnites and Gauls only); Diodorus 21.6.1 (Duris, 100,000).
- Livy 10.38–42 (the linen legion at Aquilonia); Periocha 11 (Curius, 290); Polybius 2.20 (Vadimon, 283); colony dates Venusia 291, Paestum and Cosa 273, Beneventum and Ariminum 268, Aesernia 263.
- Frontinus, On Aqueducts 5: 11,190 paces, 11,130 underground and 60 above, "anno post initium Samnitici belli tricesimo"; Livy 9.29.9–11 (Potitii); 9.46.10–15 (the humble in all tribes; the censors of 304); Staveley, Historia 1959.
- Livy 27.38 (claim of the maritime colonies); Livy 8.16 (Cales, 2,500); 10.1 (Alba Fucens, 6,000); nineteen Latin colonies from Cales (334) to Aesernia (263) by count.
- Cicero, On the Agrarian Law 2.73 ("propugnacula imperi"); thirty-five tribes in 241; Gellius 16.13.9 ("effigies parvae simulacraque"); Salmon, Roman Colonization (1969); Bispham (2006).
- Polybius 6.39.15 (allies' grain free); Cicero, Pro Balbo 35–36 (the majesty clause); Livy 10.3–5 (Arretium, 302).
- Lex agraria of 111 (formula togatorum); Livy 27.9–10 (twelve and eighteen colonies, Fregellae, "ex formula"); 29.15 (double levy in 204).
- Toynbee, Hannibal's Legacy (1965), the formula as a maximum; Brunt, Italian Manpower (1971), a sliding scale (https://en.wikipedia.org/wiki/Formula_togatorum).
- Livy 8.8.3 (scutum after pay); Sallust, Catiline 51.38; the Ineditum Vaticanum; Polybius 18.28–32.
- Polybius 2.24 figures checked line by line (consular legions 20,800 and 1,200; allies 30,000 and 2,000; Sabines and Etruscans over 50,000 and 4,000; Umbrians and Sarsinates, Veneti and Cenomani 20,000 each; reserves 20,000 and 1,500, 30,000 and 2,000; Sicily and Tarentum 8,400 and 400; lists for Latins, Samnites, Iapygians and Messapians, Lucanians, the four Sabellic peoples, Romans and Campanians; totals over 700,000 and about 70,000). The report's 325,000 citizens of some 770,000 and "three-fifths allied" follow from them.
- Herodotus 7.234 (about 8,000 Spartans); Aristotle, Politics 1270a (not a thousand), 1326b; Syll.³ 543 (Philip V to Larisa, nearly seventy colonies); Dionysius 2.16–17; Tacitus, Annals 11.24.
- Salmon, The Making of Roman Italy (1982); Mouritsen, Italian Unification (1998); no Latin colony defected after Cannae. Crosscheck section 3 pairs 3.4 with 5.2 on Mouritsen, but the two make different points (unification as retrospective here, the allies' war aims in 5.2): no duplication.
- Pointers checked and true: 1.1 (Sabellic origins); 3.3 (the Latin War; the settlement of 338); 3.2 (devotio as exemplum); 3.5 (Pyrrhus; Appius' speech); 0.2 (roads; the geographical half of the answer); 9.2 (syllabus: the manipular legion in Polybius book 6); 4.3 (Hannibal's strategy against the alliance; defections after Cannae); Greek 6.2 (citizenship law of 451/0; tribute; allied lawsuits at Athens); Greek 5.2 (the colony independent from the start); 5.2 (the revolt of 91).
- Module 7.4's pointer into this report is true (see Coverage).
