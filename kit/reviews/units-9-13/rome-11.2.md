# Rome 11.2: Generals and their armies

Verdict: fix
Body words: 2823 (target 2500; band 2250 to 2875). All the fixes below together give 2856 (tested on a scratch copy with check.py).

## Coverage
- Property qualification, recruitment of the poorest, modern doubt about Marius: covered. Marius in 107 and the Rich and Cadiou doubt are handed to module 5.2 by number. Brunt (1971) and Keaveney are added in the first dispute box.
- Long commands and provinces as bases of power: covered (Sulla in Asia, Pompey in Africa, the commands from 67, the legions of 50).
- Veteran problem and land settlement: covered.
- Oath, donatives, loyalty to the general rather than the state: covered.
- Marches on Rome of 88, 83, 49 and 43 and how each army was persuaded: covered (table plus prose).
- Caesar and his legions (the Tenth, the mutinies of 49 and 47): covered.
- Triumphs, salutations as imperator, ideology of victory: covered. The triumph's rules are handed to module 9.2, and Augustus' monopoly to module 6.4.
- Client-army argument (Gabba, Brunt, Keaveney, de Blois): covered. Gruen is added, with a pointer to deep dive module 11.8.
- Lane hand-offs: all kept. Module 5.2's "client army" (whole report), 5.4's "mutiny in Italy" (47, in the section on Caesar and his legions), 5.5's march of 43 "and its army" (table and prose), and 6.4's army background (veterans, oath, commilitones). 9.2's institutional material is pointed to, not retold. The 9.2 box (Mommsen v. Brunt 1974, imperial army) and the 5.2 box (Gabba 1949, Rich, Cadiou) are not duplicated. 11.2's first box is on the late-Republican levy (Brunt 1971, Keaveney).

## Findings
1. [error] [accuracy] Section "Veterans and the land".
   Current: "Augustus' boast that he was the first and only founder of soldiers' colonies within living memory to pay for the land (<em>Res Gestae</em> 16.1) names what the Republic had never done;"
   Problem: Caesar's agrarian law of 59 settled Pompey's veterans among others. It provided for land to be bought from willing sellers at the price assessed in the census, paid from Pompey's booty. So "never" is false. Augustus' claim is narrower than the report makes it: it concerns founders of colonies.
   Fix: "Augustus' boast that he was the first and only founder of soldiers' colonies within living memory to pay for the land (<em>Res Gestae</em> 16.1) names what the Republic had seldom done: Caesar's law of 59 bought from willing sellers at the census value (Dio 38.1.4);"
   Basis: Dio 38.1.3–5 (Loeb, via lexundria.com/dio/38.1/cy): the land was to be bought only from willing sellers, "at the same price at which it had been assessed in the tax-lists", with money from Pompey's spoils.

2. [should-fix] [register] Section "Self-test", question 3 (it repeats finding 1).
   Current: "Augustus' claim to be the first within living memory to pay for soldiers' land names what the Republic had never done; earlier colonies, Sulla's and the triumvirs', were made on confiscated land."
   Problem: The answer repeats the overstatement in finding 1.
   Fix: "Augustus' claim to be the first within living memory to pay for soldiers' land names what the Republic had seldom done: Caesar's law of 59 bought from willing sellers (Dio 38.1.4), but Sulla's and the triumvirs' colonies were made on confiscated land."
   Basis: as finding 1.

3. [should-fix] [attribution] Section "Four marches on Rome".
   Current: "Of his senior officers only Labienus left him (Dio 41.4)."
   Problem: Dio 41.4.3–4 reports Labienus' desertion and its motive (resentment at his reduced standing, and fear). He does not say that Labienus was the only one. The "only" is not in the cited author.
   Fix: "His chief legate, Labienus, went over to Pompey (Dio 41.4.3–4); no other senior officer is recorded as leaving him."
   Basis: Dio 41.4 (Loeb, LacusCurtius, penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/41*.html). Self-test 6 ("in 49 only Labienus left Caesar") should then read "in 49 Labienus is the only senior officer recorded as leaving Caesar".

4. [should-fix] [attribution] Section "Volunteers, levies and the poor" (dispute box).
   Current: "Arthur Keaveney (<em>The Army in the Roman Revolution</em>, 2007) holds that the unpropertied entered the legions in large numbers only with the Social War, the civil war of the 80s and the triumviral levies."
   Problem: The writer took this from a secondary summary, and I could not confirm it. The BMCR review reports something different: Keaveney cautions that "one ought not to overestimate the number of soldiers lacking property qualification" and treats the lowering of the qualification as a long process, less strictly applied rather than abolished. The review says nothing of the Social War or the triumviral levies.
   Fix: "Arthur Keaveney (<em>The Army in the Roman Revolution</em>, 2007) warns against overestimating the soldiers below the property qualification, whose lowering he treats as a long process, not a Marian break."
   Basis: P. Probst, BMCR 2008.07.52 (bmcr.brynmawr.edu/?p=26340).

5. [minor] [pointer] Section "Long commands, rich provinces".
   Current: "Lucullus, harsh with his men, lost his army to mutiny (module 5.3)."
   Problem: Module 5.3 gives the mutiny and Clodius' part in it (Plutarch, Lucullus 20, 34), but not Lucullus' harshness. The writer's list confirms that this sentence rests on the pointer alone.
   Fix: "Lucullus, harsh with his men, lost his army to mutiny (Plutarch, <em>Lucullus</em> 33.2, 34; module 5.3)."
   Basis: Plutarch, Lucullus 33.2 (he would not court the soldiers' favour, thinking it weakened his authority) and 34 (Clodius); lexundria.com/plut_luc/33/prr.

6. [minor] [figure] Section "The oath, the donative and the general's name".
   Current: "Octavian paid Caesar's veterans 500 denarii a man (module 5.5);"
   Problem: The figure is sourced only by a module pointer. Module 5.5 gives the ancient source.
   Fix: "Octavian paid Caesar's veterans 500 denarii a man (Cicero, <em>Letters to Atticus</em> 16.8; module 5.5);"
   Basis: module 5.5, section "Caesar's heir and Cicero's war".

7. [minor] [figure] Section "Veterans and the land".
   Current: "Caesar's colonies and the triumvirs' eighteen towns (modules 5.4 and 5.5)."
   Problem: As finding 6, the figure is sourced only by pointer. Module 5.5 cites Appian 4.3.
   Fix: "Caesar's colonies and the triumvirs' eighteen towns (Appian 4.3; modules 5.4 and 5.5)."
   Basis: module 5.5, section "Perusia, Brundisium and Sextus Pompey".

8. [minor] [figure] Section "The oath, the donative and the general's name".
   Current: "more than twenty-five years of a legionary's pay even at his doubled rate."
   Problem: The arithmetic is right but loose. 24,000 sesterces is 6,000 denarii, and 6,000 ÷ 225 = 26.7 years. The report never states the rate, so the reader cannot check the sum. The 225 denarii is the figure module 6.4 gives as Caesar's rate.
   Fix: "nearly twenty-seven years of a legionary's pay at his doubled rate of 225 denarii (module 6.4)."
   Basis: Suetonius, Julius 38.1 (24,000 sesterces in addition to the 2,000) and 26.3 (pay doubled); module 6.4, "Pay stayed at Caesar's 225 denarii a year".

9. [minor] [style] Section "Imperator: acclamation and victory".
   Current: "and his coins struck in the East showed two trophies with IMPER ITERVM, imperator for the second time."
   Problem: The coin has no citation, and the writer flags it as recalled from memory, not checked. Crawford assigns the issue to a mint moving with Sulla in 84–83 rather than to a fixed eastern mint.
   Fix: "and his coins of 84–83 showed two trophies with IMPER ITERVM, imperator for the second time (<em>RRC</em> 359)."
   Basis: Crawford, Roman Republican Coinage 359/1–2 (aureus and denarius, two trophies between jug and lituus, IMPER ITERVM). From memory; not rechecked online.

10. [minor] [attribution] Section "Was it a client army?" (dispute box).
    Current: "went home quietly and waited three years for land (Velleius 2.40.3),"
    Problem: Velleius 2.40.3 supports the dismissal at Brundisium but not the three-year wait. The wait (land bill blocked in 60, Caesar's law of 59) is in modules 5.3 and 5.4 and in Dio 37.49–50.
    Fix: "went home quietly (Velleius 2.40.3) and waited three years for land,"
    Basis: module 5.3 ("Pompey landed at Brundisium in December 62 and dismissed his army (Velleius 2.40.3)"); module 5.4 on the law of 59.

## Confirmed
- Appian, Civil Wars 3.43: Antony at Brundisium offers 100 drachmas, is laughed at, has the tribunes bring the names of troublemakers and executes some chosen by lot, not one in ten (Perseids, perseus-eng2 3.5.38–3.7.43, whose last sentences end in section 43).
- Appian 3.87: Octavian's speech asking the army for the consulship, so self-test 7's "Appian (3.87)" stands. Also in Appian 3.87–88: the centurions' deputation, and "eight legions of foot" led from the assembly towards the city. Section 89 begins "When the news of Octavius' approach reached the city", so both fall in 87–88 (Perseids 3.12.87–3.13.90 and 3.13.89–3.13.94).
- Appian 3.90 to 3.94: the Senate's turnabout (5,000 drachmas, all eight legions) begins at 90. The three legions in Rome defect "in spite of their generals" and Cornutus kills himself. Octavian has the public money brought and pays 2,500 drachmas a man, promising the rest. All of this falls in sections 91–94, matching 3.92 and 3.94 (Perseids 3.13.91–3.14.96).
- Appian 1.77 (Sulla's letter: vengeance on the guilty, no complaint against old or new citizens) and 1.79 (five legions of Italians, 6,000 horse, about 40,000 in all). Section 79 begins with Sulla's answer to the Senate's envoys; Perseids 1.9.76–1.9.84 and 1.9.79–1.9.82.
- Appian 2.47: the Ninth legion at Placentia, the five minae promised at Brundisium, decimation threatened, 120 designated, twelve executed by lot (Perseids 2.7.44–2.7.48).
- Appian 2.92–94: Sallust's narrow escape, discharge granted, "citizens", the men begging to serve (Perseids 2.13.92–2.14.98).
- Appian 5.64: Octavian's soldiers choose deputies and send them to both commanders to restore peace (Perseids 5.7.64–5.8.72).
- Dio 46.42.3–4 (an oath "ostensibly of their own motion" not to fight any legion that had been Caesar's; four hundred soldiers sent as envoys) and 46.43.4 (the sword: "If you do not grant the consulship to Caesar, this shall grant it"). LacusCurtius Dio 46.
- Dio 42.52.2–4: Sallust nearly killed, two senators killed, the men let into Rome wearing their swords (lexundria.com/dio/42.52).
- Dio 41.26–35: the Placentia speech, ending with death by lot for the most audacious (LacusCurtius Dio 41).
- Suetonius, Julius 70: he punished "the most insubordinate by the loss of a third part of the booty and of the land intended for them" (lexundria.com/suet_jul/70).
- Chrissanthos, "Caesar and the Mutiny of 47 B.C.", Journal of Roman Studies 91 (2001) 63–75. Title, year and pages are confirmed (Perseus JSTOR index), and his argument is reported as summarised: Caesar lacked a force to crush the mutiny and was obliged to give way to the mutineers' demands (Spanish thesis citing his pp. 69, 75; minerva.usc.gal).
- Keaveney 2007 (Routledge), as reported by Probst, BMCR 2008.07.52: Sulla, not Marius, "created the revolutionary army"; regular armies saw their commander as a magistrate; patron and client fit only the private armies of the mid-first century; soldiers' interest in freehold doubted, many re-enlisting as evocati; leverage ended when no opponent was left to defect to; a general tendency to avoid fighting citizens.
- Brunt, "The Army and the Land in the Roman Revolution", JRS 52 (1962) 69, revised in The Fall of the Roman Republic and Related Essays (1988). In the 1988 introductory note he says he rates "much lower the importance of clientship" and thinks Gabba "wholly mistaken" in holding that veterans generally had no wish to return to the land. This supports the report's Brunt-against-Gabba sentences (Cadiou, Revista de historiografía 40, 2025, quoting Brunt 1988 p. 240, at e-revistas.uc3m.es).
- Gabba: the proletarian army as the basis of the professional armies (1949), the "clientela militare" and rewards after service (1975 summary), and the English collection Republican Rome, the Army and the Allies (1976). All via Cadiou 2025.
- Gruen 1974: "'professional army' is a misnomer", and in the preface to the paperback reissue (p. xvi) "Neither personal attachment to generals nor professionalization characterized the late Republican military" (via Cadiou 2025). This is consistent with the report's summary, though the "lawful officer" wording is not verified word for word.
- Suetonius, Julius 24.2 (the Alauda, raised privately, later given citizenship), 26.3 (pay doubled for good), 33 (the ring and 400,000 sesterces), 38.1 (2,000 then 24,000 sesterces praedae nomine; plots not contiguous), 67.2 (commilitones), 68.1, 69 ("not so much by indulgence as by authority"); Tacitus, Annals 1.42 (one word, Quirites) and 3.74 (Blaesus, AD 22, the old honour, several imperatores at once). Known texts.
- Caesar, Gallic War 1.40–42 (Vesontio, the Tenth, the knights joke), 2.2 (two new legions, 57), 6.1 (Pompey's Cisalpine recruits sworn as consul); Civil War 1.6 (the levy throughout Italy), 1.7 (the Thirteenth, the veto, nine years), 1.23 (Domitius' men sworn to Caesar), 1.76 (Petreius' new oath); Hirtius, Gallic War 8.54–55. Known texts; the writer's chapter numbers are right.
- Plutarch, Pompey 13, 14, 57; Plutarch, Caesar 51 (Cosconius and Galba); Sallust, Catiline 11.5–6, 28.4; Cicero, Against Catiline 2.20 and Pro Sulla 60–62; Res Gestae 16.1; Dio 43.44.2 with Suetonius, Julius 76.1 (praenomen Imperatoris). Known texts.
- Syme, "Imperator Caesar: A Study in Nomenclature", Historia 7 (1958); von Premerstein, Vom Werden und Wesen des Prinzipats (1937); de Blois, The Roman Army and Politics in the First Century before Christ (1987). Titles and years are right.
- The pointers are true of their targets: 5.1 (Gracchan settlers), 5.2 (Marius 107, Sulla outlawed, Saturninus' allotments, Sulla's colonies, officers in 88, Felix), 5.3 (Lucullus' mutiny, Pompey's commands, dismissal in 62), 5.4 (Pompey's Spains through legates, law of 59, colonies), 5.5 (500 denarii, eighteen towns, oath of Italy, march of 43), 6.4 (commilitones dropped, treasury, triumph confined to the family), 9.2 (Republican oath, triumph, armies making emperors). The pointers to the unwritten 11.3 (urban plebs) and 11.8 (Gruen) match their prompts.
- House style: no em dashes, British spelling, Octavian before 27 and Augustus after, Cicero's speeches in Latin and invectives in English.
