# Rome 9.2: The army

Verdict: fix
Body words: 2854 (target 2500; upper limit 2875, so fixes must not add net words; the fixes below net about 10 fewer)

## Coverage
- citizen militia and the census classes: covered (Polybius' levy, oath and pay; the classes handed to module 1.5)
- manipular legion in Polybius book 6 (hastati, principes, triarii, velites): covered
- the camp: covered (points back to module 4.5; adds the tessera and Josephus' camp)
- decimation: covered (takes 4.5 further with the rarity argument; Crassus pointed to 5.3)
- rewards for valour: covered (Gellius' crowns, Maxfield, Caelius)
- changes associated with Marius and the cohort legion: covered (recruitment doubt left to 5.2, client army to 11.2)
- Augustan professional army, pay, length of service: covered (terms by pointer to 6.4; Domitian, P.Gen.Lat. 1)
- auxiliaries and citizenship on discharge (diplomas): covered
- soldier's life from Vindolanda tablets and tombstones: covered (no overlap with the tablets used in 7.5)
- equipment and engineering: covered
- the triumph as ritual: covered (origins dispute left to 1.2)
- late army of field and frontier troops: covered (takes 8.1 and 8.2 further without repeating them)
- army as political actor from Sulla to the soldier emperors: covered, but partly retells 7.1 and 7.2 (finding 1)

## Findings
1. [should-fix] [lane] Section "The army as political actor".
   Current: "In 41 the praetorians made Claudius emperor, and he promised each of them 15,000 sesterces, the first Caesar, Suetonius says, to buy the soldiers' loyalty (<em>Claudius</em> 10.4). On 1 January 69 the legions of Upper Germany refused the oath to Galba (Tacitus, <em>Histories</em> 1.55), and the year revealed the secret of empire: that an emperor could be made elsewhere than at Rome (1.4)."
   Problem: Module 7.1 already tells Claudius' accession with the same figure and the same Suetonian phrase ("the first Caesar to buy the soldiers' loyalty", 10.4), and module 7.2 tells the oath refusal of 1 January 69 (<em>Histories</em> 1.55) and the secret of empire (1.4). 9.2 retells both and points to neither. The bare "41" also follows "Sulla's march of 88" with no era marker.
   Fix: "In AD 41 the guard made Claudius emperor for a donative (module 7.1), and in 69 the provincial armies showed that an emperor could be made elsewhere than at Rome (Tacitus, <em>Histories</em> 1.4; module 7.2)."
   Basis: rome/r-7.1.html, "Claudius: the guard's emperor"; rome/r-7.2.html, "Galba and the secret of empire".

2. [should-fix] [register] Section "Self-test", question 10.
   Current: "<li>What did Tacitus call the secret of empire revealed in 69, and how did the third century change the officers as well as the electors?<details><summary>Answer</summary><p>That an emperor could be made elsewhere than at Rome (<em>Histories</em> 1.4): the provincial armies chose rulers. In the third century"
   Problem: Module 7.2's self-test already asks this question ("What did Tacitus mean by the 'secret of empire' (<em>Histories</em> 1.4) ..."). Once finding 1 is applied, the body no longer explains it here. The question should test what this module adds.
   Fix: "<li>How did the soldiers' oath bind the army to the emperor, and how did the third century change who commanded the legions?<details><summary>Answer</summary><p>Soldiers swore to the emperor, renewed the oath each 1 January (Tacitus, <em>Histories</em> 1.55) and on his accession day (Pliny, <em>Letters</em> 10.52), and carried his image among the standards. In the third century" (the rest of the answer unchanged)
   Basis: rome/r-7.2.html, Self-test question 2.

3. [error] [attribution] Section "The citizen militia: census, levy and oath".
   Current: "Citizens rated above 400 drachmas served between seventeen and forty-six, ten campaigns in the cavalry or sixteen in the infantry; poorer men rowed (6.19)."
   Problem: Polybius 6.19 gives only the upper limit: ten campaigns in the cavalry or sixteen in the infantry before the age of forty-six. The minimum age of seventeen comes from other sources (Gellius 10.28, after Tubero; Gaius Gracchus' law in Plutarch, <em>Gaius Gracchus</em> 5.1), not from Polybius.
   Fix: "Citizens rated above 400 drachmas owed ten campaigns in the cavalry or sixteen in the infantry before the age of forty-six; poorer men rowed (6.19)."
   Basis: Polybius 6.19.2 (Shuckburgh translation, quoted at novoscriptorium.com/2020/04/14/the-roman-military-system-according-to-polybius/: "sixteen years before reaching the age of forty-six"; no age of seventeen in 6.19–21).

4. [error] [attribution] Section "The manipular legion and its discipline".
   Current: "Octavian decimated cohorts that gave way in Dalmatia and fed the survivors barley (Suetonius, <em>Augustus</em> 24.2)"
   Problem: Suetonius 24.2 states the practice in general ("cohortes, si quae cessissent loco, decimatas hordeo pavit") and names no campaign. The Dalmatian case comes from Appian and Dio.
   Fix: "Octavian decimated a cohort that gave way in Dalmatia and fed the survivors barley (Appian, <em>Illyrian Wars</em> 26; Dio 49.38), as Suetonius says he did with any cohort that yielded (<em>Augustus</em> 24.2)"
   Basis: Appian, Illyrian Wars 26 (livius.org/sources/content/appian/appian-the-illyrian-wars/appian-the-illyrian-wars-6); Dio 49.38, Cary translation (lexundria.com/dio/49.38/cy).

5. [should-fix] [attribution] Section "Equipment and engineering", dispute box.
   Current: " Segmented armour found at auxiliary forts supports him."
   Problem: The verdict is unattributed, and it is not Coulston's argument. His 1989 paper cites no finds of segmented armour at auxiliary forts and rests on the frieze's figure types. Such finds are ambiguous anyway, because legionary detachments could account for them. Deleting it saves seven words.
   Fix: delete.
   Basis: J. C. Coulston, "The Value of Trajan's Column as a Source for Military Equipment", in C. van Driel-Murray (ed.), <em>Roman Military Equipment: the Sources of Evidence</em>, BAR S476 (1989), 31–44 (a-r-m-e-s.org/wp-content/uploads/2023/09/476-031-044-Coulston.pdf).

6. [should-fix] [register] Section "Self-test", question 7.
   Current: "Segmented armour from auxiliary forts supports him against the literal reading that goes back to Cichorius."
   Problem: The answer repeats the unsupported claim from finding 5.
   Fix: "He thus rejected the literal reading that goes back to Cichorius."
   Basis: as finding 5. Coulston's note 25 names Cichorius among the "very literal" early commentators.

7. [minor] [accuracy] Section "The army as political actor".
   Current: "renewed the oath each 1 January and on the anniversary of his accession (Pliny, <em>Letters</em> 10.52)"
   Problem: Pliny 10.52 reports only the accession-day oath. The 1 January oath is attested by Tacitus, <em>Histories</em> 1.55, which finding 1 removes from later in the paragraph.
   Fix: "renewed the oath each 1 January (Tacitus, <em>Histories</em> 1.55) and on the anniversary of his accession (Pliny, <em>Letters</em> 10.52)"
   Basis: Pliny, Letters 10.52; Tacitus, Histories 1.55.

8. [minor] [pointer] Section "The triumph".
   Current: "and the Arch of Titus records (module 9.5)"
   Problem: Module 7.2 already tells the triumph of 71, with Simon's execution, <em>Jewish War</em> 7.123–157 and the Arch of Titus. 9.5 is unwritten.
   Fix: "and the Arch of Titus records (modules 7.2 and 9.5)"
   Basis: rome/r-7.2.html, paragraph beginning "In 71 Vespasian and Titus triumphed".

9. [minor] [pointer] Section "Equipment and engineering".
   Current: "In peace soldiers built roads, aqueducts and walls (module 7.5)"
   Problem: Module 7.5 says the army built roads and forts, and that legionaries built Hadrian's Wall. It does not mention aqueducts.
   Fix: "In peace soldiers built roads, forts and walls (module 7.5)"
   Basis: rome/r-7.5.html, paragraphs beginning "Most soldiers in most years" and "Hadrian, the <em>Historia Augusta</em> says".

10. [minor] [pointer] Section "The late army: field and frontier".
    Current: "and credits Constantine with the formal division of troops."
    Problem: Module 8.2 only reports the usual attribution ("is usually credited to Constantine"). It does not make the attribution itself.
    Fix: "and notes that the formal division of troops is usually credited to Constantine."
    Basis: rome/r-8.2.html, paragraph beginning "John the Lydian".

11. [minor] [pointer] Section "Equipment and engineering".
    Current: "appears by AD 9 at Kalkriese (module 6.4) and"
    Problem: Module 6.4's dispute box leaves the date of Kalkriese open (Wolters' AD 15 against Wigg-Wolf). A flat "by AD 9" overstates what the pointer's target says.
    Fix: "appears at Kalkriese, probably the Varian battlefield of AD 9 (module 6.4), and"
    Basis: rome/r-6.4.html, Kalkriese dispute box.

12. [minor] [accuracy] Section "The soldier's life: tablets and tombstones".
    Current: "(<em>Jewish War</em> 3.70–109)"
    Problem: The span is forty sections. The drill epigram is at 3.75, and the report cites the camp separately (3.76–84).
    Fix: "(<em>Jewish War</em> 3.75)"
    Basis: Josephus, Jewish War 3.75 (Whiston 3.5.1).

13. [minor] [style] Section "The citizen militia: census, levy and oath".
    Current: "Pay began, Livy says, at the siege of Veii in 406"
    Problem: The spec requires that, for an event before about 300 BC, the report says how many centuries after it the source wrote. The 471 decimation does this; the Veii pay does not.
    Fix: "Pay began, Livy says nearly four centuries later, at the siege of Veii in 406"
    Basis: AGENT-SPEC.md, Rome course rules.

## Confirmed
- Lane note: 3.4 (Polybius 6.19–42, "module 9.2") kept; 9.2 describes the legion without retelling 3.4's comparison with the phalanx.
- Lane note: 4.5 kept; the camp, cudgel, decimation and Polybius' rewards are pointed back to, not retold; the tessera (6.34), Gellius' crowns and Maxfield take it further.
- Lane note: 5.2 kept; cohort not credited to Marius (Polybius 11.23.1), recruitment doubt pointed to 5.2, client army to deep dive 11.2.
- Lane note: 6.4 kept; "regular citizenship on discharge came later" is answered by the diploma paragraph (regular from Claudius).
- Lane note: 7.4 kept; 300 denarii since Domitian explained (Suetonius, Domitian 7.3: fourth stipendium; 1,000-sesterce deposit cap after Antonius Saturninus' revolt in a double camp); the line between legion and auxiliary losing its legal basis after 212 delivered.
- Lane note: 7.5 kept; tablets used (Tab. Vindol. II 291, III 628, II 346) do not overlap 7.5's (II 154, 343, 164, 344).
- Lane note: 1.2 triumph origins and 5.3 Crassus pointed back, not retold; 0.2 Luttwak neither retold nor needed.
- Lane note: 8.1 hand-off ("inscriptions show a slower change ... module 9.2") delivered in the third-century paragraph; 8.2, 8.3, 8.4 and 8.5 hand-offs of the late army delivered.
- Pointers true of their targets: 1.5 (classis and Livy 1.43), 3.4 (formula togatorum), 4.4 (triumph cash), 6.4 (Augustan terms, Caelius cenotaph, triumphs ended after Balbus 19 BC), 7.4 (Caracalla's pay rise, Pertinax and the sale, Parthian legions under equestrian commanders), 8.4 (Goths of 382), 8.5 (Ricimer making and unmaking emperors), 5.2 (Sulla's march of 88).
- Duncan-Jones 1990 appears in 7.5's dispute box on a different question (taxation); no duplicate box.
- Polybius 6.20.8–9 (4,200/5,000 infantry, 300 cavalry), 6.21.1–3 (oath), 6.21.7–8 (age and wealth), 6.21.9, 6.23 (mail above 10,000 drachmas), 6.24.9 (centurions), 6.39.12–15 (pay): from knowledge and the Shuckburgh text at novoscriptorium.com.
- Livy 22.38.1–5 (first sworn oath imposed by the tribunes in 216); Livy 2.59.11 (Appius Claudius, 471); Livy 4.59.11–4.60 (pay at Veii, tributum): from knowledge.
- Tacitus, Annals 3.21.1 (Apronius, "rarum ... e vetere memoria"); Annals 1.23 ("Bring another"); Annals 11.20 (Corbulo's canal); Annals 4.4: from knowledge.
- Brunt, "Conscription and Volunteering in the Roman Imperial Army" (Scripta Classica Israelica 1, 1974): opens with Mommsen's view that after Marius the legions were mainly volunteers; argues conscription was far more common in the Principate; triumph of the voluntary principle due to local recruiting; cites Annals 4.4.2 (scriptaclassica.org/index.php/sci/article/download/299/161/653).
- Coulston 1989 year and title: BAR S476, 1989 (a-r-m-e-s.org prelims); his conclusion that the Column "cannot be employed as an independent source for military equipment".
- Diplomas: earliest AD 52; children born in service excluded about 140; last auxiliary diplomas 203; seven witnesses (en.wikipedia.org/wiki/Roman_military_diploma; romaninscriptionsofbritain.org/instrumentum/2401).
- Beard 2007: rules "varied, fragile and changing"; "one rule held firm: the general was to remain outside of the city walls" (De Re Militari review, deremilitari.org/REVIEWS/Beard_RomanTriumph.htm); confirmed at review level only, as the writer flagged.
- Agathias 645,000 and Jones's similar total of about 600,000 from Notitia unit strengths; Duncan-Jones judged Jones's unit sizes too high (en.wikipedia.org/wiki/Late_Roman_army).
- Isaac, "The meaning of the terms limes and limitanei", JRS 78 (1988); Historia Augusta, Severus Alexander 58.4: from knowledge.
- Aurelius Victor 40.25 and Zosimus 2.17 (praetorians disbanded); Zosimus 2.33 (magistri), 2.34 (frontiers stripped, theatres); Ammianus 16.10.8 (cataphracts as statues), 15.12.3 (no Gaul cuts off his thumb); Vegetius 1.20 and 2.6 (1,105): from knowledge.
- RIB 200 (Favonius Facilis), RIB 201 (Longinus Sdapeze, Sardica), RIB 1172 (Flavinus, ala Petriana, 25 years, 7 years' service); ILS 2487 (Lambaesis, 128); Tab. Vindol. II 291, III 628, II 346: from knowledge.
- Caesar, Gallic War 4.17–18 (ten days), 7.69 and 7.74 (eleven and fourteen miles); Pliny, Natural History 33.111–112 (Verrius, minium), 28.39 (fascinus), 22.6–13 (grass crown); Tertullian, Apology 33.4; Suetonius, Julius 49.4, 51; Gellius 5.6 and 5.6.20–23; Plutarch, Marcellus 22; Valerius Maximus 2.8.1; Josephus, Jewish War 7.123–157: from knowledge.
- Suetonius, Claudius 10.4 and Gaius 9; Dio 60.24.3 (soldiers given the rights of married men); Plutarch, Gaius Gracchus 5.1; Aurelius Victor 33.34: from knowledge.
- Breeze, JRS 59 (1969), first cohort and Inchtuthil (ten barracks for the first cohort against six); Forni 1953; Maxfield 1981: from knowledge.
- P.Gen.Lat. 1 (AD 81, Q. Julius Proculus of Damascus, deductions for hay, food, boots and straps, Saturnalia, standards, clothing): from knowledge (Fink, Roman Military Records on Papyrus 68); not found online.
- Not checked: "senatorial legates and tribunes of legions ... last attested in the 260s" (no source found; the Gallienic shift to equestrian prefects about 261–267 is consistent with it).
- House style: British spelling throughout, no em dashes, Octavian and Augustus used correctly, citations in house form.
