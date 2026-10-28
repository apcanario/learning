# Rome 3.1: The Struggle of the Orders

Verdict: keep
Body words: 2783 (target 2500)

## Coverage
- patricians and plebeians, and the debate over the original distinction: covered
- first secession of 494: covered
- Menenius Agrippa's fable of the belly: covered
- tribunes of the plebs and their sacrosanctity: covered
- plebeian council: covered
- aediles: covered
- debt-bondage (nexum): covered
- Decemvirate and Twelve Tables (what survives, how it survives, what it shows): covered
- Appius Claudius and Verginia: covered (the exemplum handed explicitly to module 3.2)
- second secession: covered
- Valerio-Horatian laws: covered
- Canuleian law: covered
- military tribunes with consular power: covered
- Licinio-Sextian laws and the first plebeian consul: covered
- lex Ogulnia: covered
- lex Hortensia: covered
- patricio-plebeian nobility: covered
- consuls, praetors, censors and dictator: covered (table)
- Senate and the three assemblies: covered
- the cursus honorum taking shape: thin (one sentence, on iteration only)
- reliability of Livy 2 to 10 and Gracchan projection: covered

## Findings
1. [should-fix] [pointer] Section "Livy books 2 to 10 and the Gracchan lens".
   Current: "wrote after 133 and had seen the Gracchi and Sulla's suppression of the tribunate (module 5.1)."
   Problem: Piso, the first name in the list, was consul in 133 and wrote long before Sulla, so "had seen ... Sulla's suppression" is untrue of him. Module 5.1 covers the Gracchi; Sulla's curbing of the tribunate is in module 5.2.
   Fix: "wrote after 133: Piso amid the Gracchan crisis, the rest after Sulla had curbed the tribunate (modules 5.1 and 5.2)."
   Basis: rome/r-5.1.html (Gracchi); rome/r-5.2.html, self-test "What did Sulla do to the tribunate and the courts?"; Piso's consulship 133 and censorship 120.

2. [should-fix] [register] Section "The settlement: nobility, magistrates, Senate and assemblies" (thin coverage).
   Current: "No law yet fixed the cursus honorum: the Genucian ten-year rule restrained iteration, yet Valerius Corvus held six consulships."
   Problem: The prompt asks for "the cursus honorum taking shape". The report gives one sentence on re-election and says nothing about the order of offices or when the order became law.
   Fix: add after "yet Valerius Corvus held six consulships.": " Rank was already ordered, the censorship normally going to former consuls, but the sequence stayed a matter of custom until the lex Villia annalis of 180 set minimum ages for each office (Livy 40.44.1; deep dive module 11.1)."
   Basis: Livy 40.44.1 (the rogatio of the tribune L. Villius, 180 BC); roman-syllabus.html, module 11.1 prompt ("the cursus honorum after the lex Villia annalis of 180 BC"). About 40 words; body stays inside the band.

3. [should-fix] [register] Section "Self-test", question 7.
   Current: "and the first plebeian quaestors in 409, decades after the offices were opened."
   Problem: The body opens the quaestorship in 421 (Livy 4.43) and has plebeians first win it in 409. That is twelve years, not decades. Only the consular tribunate (444 to 400) fits "decades".
   Fix: "and the first plebeian quaestors in 409 (4.54.2–3): forty-four and twelve years after the two offices were opened."
   Basis: the report's own dates (444, 421, 409, 400); Livy 4.43, 4.54.2–3, 5.12.9.

4. [should-fix] [lane] Section "Livy books 2 to 10 and the Gracchan lens", dispute box.
   Current: "Wiseman (<em>Clio's Cosmetics</em>, 1979) shows plausible invention as accepted historical method."
   Problem: This repeats module 0.1's dispute box on annalistic method (Badian and Forsythe; Wiseman's "creative reconstruction"; Cornell and Oakley), which crosscheck section 3 flags as 0.1 ~ 3.1. The rest of the box (Mitchell; Raaflaub and Cornell's two phases) is specific to the orders and should stay.
   Fix: "Module 0.1 gives Wiseman's case that such reconstruction was accepted method."
   Basis: rome/r-0.1.html, dispute box beginning "Badian and, later, Gary Forsythe"; xc-rome-pre.txt section 3.

5. [minor] [accuracy] Section "Patricians and plebeians: what the distinction was", and Carry forward 3.
   Current: "in the 20s BC, four to five centuries after the events;"
   Problem: Books 2 to 10 run to 293. The fourth-century half of the story (367 to 293) lies under three and a half centuries before Livy, so the range misstates the gap that the source-criticism rule asks for.
   Fix: "in the 20s BC, three to five centuries after the events;"
   Also, Carry forward 3. Current: "were written four to five centuries after the events" Fix: "were written three to five centuries after the events"
   Basis: arithmetic. 509 to about 25 BC is 484 years; 367 to 25 BC is 342; 293 to 25 BC is 268.

6. [minor] [style] Section "The settlement: nobility, magistrates, Senate and assemblies", and Carry forward 1.
   Current: "the system at its height, module 11.1."
   Problem: 11.1 is in Deep dive I (unit 11), and AGENT-SPEC asks for the form "deep dive module 11.7".
   Fix: "the system at its height, deep dive module 11.1."
   Also, Carry forward 1. Current: "(modules 4.5 and 11.1)" Fix: "(module 4.5 and deep dive module 11.1)"
   Basis: AGENT-SPEC.md, Rome course; roman-syllabus.html, "UNIT 11 Deep dive I: the fall of the Republic".

7. [minor] [lane] Section "The settlement: nobility, magistrates, Senate and assemblies".
   Current: "dates the formation of this patricio-plebeian nobility to the generations after 367."
   Problem: This is nearly the same wording as module 0.3's dispute box (crosscheck section 2, 0.3 ~ 3.1, six shared shingles). 0.3 adds "above all after 287". A pointer ties the two.
   Fix: "dates the formation of this patricio-plebeian nobility to the generations after 367 (module 0.3)."
   Basis: rome/r-0.3.html, dispute box on Hölkeskamp and Flower.

## Confirmed
- Livy 1.8.7 (patres, patricii); Livy 2.16.4–5 (Attius Clausus and his clients, the year of Publicola's fourth consulship, 504); Livy 1.33.2 (Ancus gives the Aventine to the Latins); Dionysius 2.9–10 (patrons and clients).
- Livy 2.23.3–7 (the old centurion, 495); 2.32.1–2 (Sacred Mount across the Anio); 2.32.3 (Piso's Aventine); 2.32.8 (Menenius dear to the plebs as of plebeian origin); Dionysius 6.86 (the fable); Xenophon, Memorabilia 2.3.18 (brothers like hands and feet).
- Livy 2.33.2–3 (two tribunes co-opting three); Dionysius 6.89 (five); Livy 2.58.1 (Piso: two to five in 471); 3.30.7 (ten in 457); 2.56–58 (Publilian law, 471).
- Livy 3.55.6–10 (the jurists on sacrosanctity from the old oath); 3.55.7 (head forfeit to Jupiter); 3.55.13 (decrees lodged with the plebeian aediles at the temple of Ceres); Dionysius 6.90, 6.94 (aediles; the temple dedicated in 493).
- Varro, De lingua Latina 7.105: Manilius and Mucius Scaevola on nexum, and abolition under the dictator C. Poetelius Libo Visolus (313).
- Livy 8.28 and 8.28.1 ("velut aliud initium libertatis", 326); Livy 7.16.1 (the unciarium faenus of 357); Tacitus, Annals 6.16 (the Twelve Tables' ceiling).
- Livy 3.9 (Terentilius, 462); 3.31.8 (embassy to Athens, 454); 3.34.6 ("fons omnis publici privatique iuris"); 3.37.4 (two tables added); 3.44–48, 3.50–52; 3.57.10 (bronze tables); Diodorus 12.24 (Verginia).
- Cicero, On the Republic 2.63 ("inhumanissima lege"); On the Laws 2.59 (learnt as a boy), 2.59–64 (funeral limits after Solon), 3.44 (no privilegia; capital cases before the maximus comitiatus).
- Gellius 20.1.48–49 ("tertiis nundinis partis secanto"), 20.1.12 (twenty-five asses); Gaius, Institutes 1.132; Servius on Aeneid 6.609; Pliny, Natural History 28.17–18; Godefroy (1616); Crawford, Roman Statutes (1996).
- Pomponius, Digest 1.2.2.4 and Pliny, Natural History 34.21 on Hermodorus of Ephesus; Gaius, Digest 10.1.13 on Solon's boundary rule; Lambert (1902) on Sextus Aelius.
- Livy 9.46.5 (Gnaeus Flavius, 304).
- Livy 4.1–6 (Canuleius, 445); 4.6.8 and 4.7.2 (the two reasons for consular tribunes); 4.8 (censorship, 443); 4.43 (quaestorship opened, 421); 4.54.2–3 (plebeian quaestors, 409); 5.12.9 (P. Licinius Calvus, 400); Tacitus, Annals 11.22 (elected quaestors from 447). Forsythe ties the consular tribunate to a military redesign that included the censorship, and Cornell is cited for no plebeians from 444 to 401 and no tribune's triumph (https://en.wikipedia.org/wiki/Consular_tribune).
- Livy 6.34.5–10 (Fabia and the lictor's rod); 6.35.4–5 (the rogations); 6.35.10 (five years without curule magistrates); 6.42 (the 367 settlement, praetor and curule aediles).
- Table: Livy 7.17.6 (first plebeian dictator, 356); 7.22.10 (first plebeian censor, 351); 7.42.1–2 (Genucian plebiscites, 342); 8.12.14–16 (Publilian laws, 339); 8.15.9 (Publilius Philo, praetor 337); 10.6–9 (Ogulnian law, pontiffs to eight and augurs to nine); 10.9.3–6 (Valerian appeal law, 300).
- Periocha 11 and Pliny, Natural History 16.37 (Hortensius, the Janiculum, the law carried in the oak grove); Gellius 15.27.4 (Laelius Felix); Gaius, Institutes 1.3.
- Von Fritz, Historia 1 (1950), on 367 as an administrative reform; patrician pairs of consuls in several years from 355 to 343 and none after 342.
- Livy 7.16.9 (Licinius Stolo fined for 1,000 iugera with his son); Gelzer (1912); Hölkeskamp (1987); both consuls first plebeian in 172.
- Festus on the Ovinian law ("ex omni ordine optimum quemque"); M. Valerius Corvus' six consulships; Cicero, On the Republic 2.2 (Cato on a constitution built by many men over centuries).
- Livy 7.9.5 (Macer seeking praise for his family); 10.9.3 ("semper a familia eadem"); Sallust, Histories 3 (Macer's speech, 73); Livy 2.41 (Cassius' bill with Latins and Hernici); Mommsen (Hermes 1871) on the three demagogues; Plutarch, Camillus 42 (Concord vowed in 367); Momigliano, "Camillus and Concord", CQ 1942; Gabba (1991); Gellius 6.3.37 (Cato's 500 iugera in 167); Livy 6.1.2–3.
- Raaflaub, Social Struggles in Archaic Rome (1986; 2nd edn 2005), two-phase model; Mitchell, Patricians and Plebeians (1990).
- Pointers checked and true: 0.1 (Livy and Dionysius; the table gives Dionysius 30 to 7 BC); Greek 5.5 (Solon's reforms of 594/3 and loans on the person); 3.2 (Verginia as exemplum; Mommsen's three would-be kings); 1.6 (Publicola's appeal law); 0.3 (the anarchy, five years in Livy against one in Diodorus); 1.5 (the centuriate classes); 4.5 (Polybius' mixed constitution); 11.1 (syllabus: cursus after the lex Villia, the Millar debate).
- Momigliano's "Camillus and Concord" stays at home here, where it serves the reliability question. The repeat in 3.3 is flagged in rome-3.3.md.
