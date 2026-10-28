# Rome 9.3: Family, women and slaves

Verdict: fix
Body words: 2833 (target 2500; band 2250 to 2875; all fixes below together bring it to 2848, tested on a scratch copy)

## Coverage
- familia and paterfamilias, paternal power and its real limits: covered (Ulpian, Gaius, Livy, Sallust, Seneca, Marcian, Saller)
- marriage with and without manus, divorce and dowry: covered (manus forms handed back to 2.4 as the lane note asks)
- age at marriage and demography (Saller and Shaw): covered (Hopkins, Shaw, Saller, Bagnall and Frier, Frier)
- Roman women in public and private: covered
- Cornelia and Hortensia's speech of 42 BC: covered by pointer (5.1, 5.5, deep dive 11.4), half a line each as the lane note asks
- Livia and the imperial women: covered (Livia, Agrippina, Julia Domna, one line each with pointers)
- Laudatio Turiae: covered, with identification dispute
- gap between law and practice: covered
- childhood, wet nurses and schooling: covered
- slavery, numbers: covered (Brunt, Scheidel)
- slavery, sources (war, birth, trade, exposure): covered (Scheidel–Harris box; exposure via Boswell–Harris box)
- slavery, work, agricultural gangs and household slaves: covered (Cato pointed to 4.4; Varro, Columella, Treggiari)
- slave wars in Sicily and Spartacus: covered (Eunus pointed to 4.4; second war told from Diodorus 36; Spartacus pointed to 5.3)
- manumission and freedmen as a class, Trimalchio and the epitaphs: covered (forms of manumission pointed to 9.1)
- modern study (Treggiari, Dixon, Bradley): covered
- point back to Greek module 8.5: covered (see finding 7 on wording)

Lane note: all hand-offs kept. Familia law and marriage without manus taken from 2.4; no Spartacus retelling and the revolt placed within slavery, as 5.3 promises; no Eunus narrative and no Hopkins–Rosenstein box; Cornelia, Hortensia and Livia's marriage left to 11.4; Laudatio Turiae, Trimalchio as social type and Saller and Shaw on age at marriage are new here; 10.2 left the Satyricon as literature. 9.4 (written) hands "its freedman host" to 9.3, and 9.3 covers him. No dispute box duplicated (crosscheck finds none); the shared Bradley 1989 citation with 5.3 makes a different point.

## Findings
1. [error] [attribution] Section "Familia and paterfamilias".
   Current: "Richard Saller ("Familia, domus and the Roman conception of the family", <em>Phoenix</em> 1984) showed that <em>paterfamilias</em> usually meant a property owner"
   Problem: The 1984 Phoenix article is on the senses of familia and domus. The argument that paterfamilias in ordinary usage meant the estate owner is Saller's later article in Classical Philology 94 (1999).
   Fix: "Richard Saller ("Pater familias, mater familias, and the gendered semantics of the Roman household", <em>Classical Philology</em> 1999) showed that <em>paterfamilias</em> usually meant a property owner"
   Basis: Saller, CP 94.2 (1999) 182–197 (https://www.journals.uchicago.edu/doi/10.1086/449430); Wikipedia "Pater familias" cites CP 1999 p. 182 for "most commonly used to refer to the estate owner". I could not see the 1984 article's text, so the maintainer may want to confirm it does not make the same claim.

2. [should-fix] [register] Section "Manumission and the freedmen".
   Current: "John D'Arms (<em>Commerce and Social Standing in Ancient Rome</em>, 1981) answered that commerce carried less stigma"
   Problem: The box names only one side. Veyne and Finley are named in the paragraph before it but not in the box itself (a recurring slip in the brief).
   Fix: "John D'Arms (<em>Commerce and Social Standing in Ancient Rome</em>, 1981) answered Veyne and Finley that commerce carried less stigma"
   Basis: AGENT-SPEC.md: dispute boxes name a source or scholar on each side.

3. [should-fix] [register] Section "Self-test", question 6.
   Current: "most sons were free of paternal power by adulthood"
   Problem: The body says "most men had lost their fathers before they married" (and Q2's answer says the same), and it puts men's marriage at about thirty. "By adulthood" is a stronger claim than the body makes, and Saller's simulations do not support it at age twenty.
   Fix: "most men were free of paternal power by the time they married"
   Basis: body, section "Familia and paterfamilias", and Q2 answer; Saller 1994 as summarised in BMCR (https://bmcr.brynmawr.edu/?p=20585): "a significant proportion of fathers will have died by the time their sons reached adulthood".

4. [minor] [attribution] Section "Women: law, practice and the Laudatio Turiae".
   Current: "Valerius Maximus (6.7.2) and Appian (4.44) tell how Turia hid her husband Quintus Lucretius Vespillo in the proscriptions,"
   Problem: Appian tells the story of Lucretius hidden by "his wife" in a double roof but does not name her. The name Turia comes only from Valerius Maximus.
   Fix: "Valerius Maximus (6.7.2) tells how Turia hid her husband Quintus Lucretius Vespillo in the proscriptions, a story Appian tells without her name (4.44),"
   Basis: Appian, Civil Wars 4.44 (Perseus/Perseids translation, https://cts.perseids.org/read/greekLit/tlg0551/tlg017/perseus-eng2/4.6.39-4.6.44): "he went to his wife, by whom he was concealed between the planks of a double roof".

5. [minor] [accuracy] Section "Manumission and the freedmen".
   Current: "Petronius' Trimalchio is the type drawn by a senatorial pen."
   Problem: The report states as fact that the author was the senator in Tacitus (Annals 16.18–19). That is the usual view, not a certain one. 10.2 owns the authorship question, so a hedge is enough here.
   Fix: "Petronius' Trimalchio is the type drawn by a probably senatorial pen."
   Basis: standard handbooks (identification with T. Petronius, Tacitus, Annals 16.18–19, is the communis opinio but rests on inference). Not searched.

6. [minor] [attribution] Section "Familia and paterfamilias".
   Current: "while Aulus Fulvius, who had his son killed for setting out to join Catiline, acted as father (Sallust, <em>Catiline</em> 39.5)"
   Problem: In the cited passage Sallust gives the praenomen (A. Fulvius, "senatoris filius") to the son, not the father. Later sources and handbooks disagree over whose praenomen it is, so the safe course is to drop it.
   Fix: "while the senator Fulvius, who had his son killed for setting out to join Catiline, acted as father (Sallust, <em>Catiline</em> 39.5)"
   Basis: Sallust, Catiline 39.5, Perseus translation (https://fgh.perseids.org/read/latinLit/phi0631/phi001/perseus-eng2/39): "Aulus Fulvius, a senator's son ... his father ordered to be put to death"; Smith, Dictionary s.v. Fulvius 4 (A. Fulvius as the conspirator).

7. [minor] [pointer] Section "How the study of the Roman family changed".
   Current: "Greek module 8.5 gives the comparison: the Roman father's power"
   Problem: Greek 8.5 gives the Athenian side only (the kyrios for life, metics). It never says that freed slaves at Athens became metics, nor anything about Rome. The comparison is 9.3's own, so the pointer should not credit 8.5 with it.
   Fix: "Against the Athenian household of Greek module 8.5, the Roman father's power"
   Basis: greece/r-8.5.html, sections "The oikos and the kyrios" and "Slaves and metics".

8. [minor] [accuracy] Section "Marriage, manus, dowry and divorce".
   Current: "and at her father's death became one of the few Romans who owned property outright."
   Problem: This sits awkwardly with the report's own demography (most men free of paternal power before marrying, so many adults were sui iuris owners). The point is that she owned in her own right, not that owners were few.
   Fix: "and at her father's death became an owner of property in her own right."
   Basis: internal consistency with section "Familia and paterfamilias" and Self-test 6.

## Confirmed
- Ulpian, Digest 50.16.195 (senses of familia) and 50.16.195.2 (a childless man or a ward is paterfamilias).
- Gaius, Institutes 1.55 (patria potestas peculiar to Romans); 1.132 (Twelve Tables, son sold three times); 1.110–113 and 1.111 ("filiae locum"); 1.157 (lex Claudia ends agnatic tutelage of women); 1.190 (levitas animi "more specious than true"); 2.63 (lex Iulia on dotal land); 2.274 (Voconian law).
- Livy 2.5 (Brutus) and 8.7 (Manlius Torquatus) as consuls; Seneca, On Mercy 1.15 (Tarius, Augustus in the council, son exiled to Massilia); Marcian, Digest 48.9.5 (Hadrian, hunt, "in pietate debet, non atrocitate consistere").
- Dionysius 2.26–27 on Romulus' paternal power; Saller, Continuity and Change 1 (1986) and Patriarchy, Property and Death in the Roman Family (1994) (https://www.cambridge.org/core/journals/continuity-and-change/article/patria-potestas-and-the-stereotype-of-the-roman-family/B4AD07E3BC9D98046015831C455DF3E4).
- Ulpian, Digest 50.17.30 ("nuptias non concubitus sed consensus facit"); Digest 23.2.4 (twelve); Digest 24.1.1 (gifts between spouses void by custom); Ulpian, Rules 6.10 (a sixth per child, no more than three sixths, for fault of the wife or her father).
- Sulla and Pompey each married five times.
- Gellius 4.3.1–2 (Servius Sulpicius, Carvilius Ruga, 523 AUC = 231 BC); Dionysius 2.25.7; Valerius Maximus 2.1.4; Valerius Maximus 2.9.2 (L. Antonius expelled by the censors of 307).
- Hopkins, Population Studies 1965; Shaw, JRS 77 (1987); Saller, CP 82 (1987); Bagnall and Frier, The Demography of Roman Egypt (1994); Frier, CAH XI (2000), e0 about 25.
- Valerius Maximus 8.3.2 (Afrania) and Digest 3.1.1.5 (Carfania, edict on postulating for others); Cicero, On Old Age 14 (Cato urged the Voconian law); Pro Murena 27; CIL X 810 (Eumachia); CIL IV 1136 (Julia Felix); Livy 34.1–8 (Oppian law repeal, 195 BC).
- Tacitus, Annals 1.8 (Livia into the Julian family as Augusta) and 13.5 (Agrippina behind a curtain).
- Laudatio Turiae: CIL VI 41062 / ILS 8393; late first century BC; 41 years of marriage; the Lepidus episode and bruises; the divorce offer. Horsfall called the laudator an "utterly improbable ex-consul"; Osgood, Turia: A Roman Woman's Civil War (2014), treats the couple as unknown wealthy equestrians; Mommsen popularised the identification (Wikipedia, Laudatio Turiae, https://en.wikipedia.org/wiki/Laudatio_Turiae). Valerius Maximus 6.7.2 names Turia and Q. Lucretius.
- P.Oxy. 4.744 (Hilarion, Alexandria, 1 BC); Pliny, Letters 10.65–66 (threptoi); Boswell, The Kindness of Strangers (1988); Harris, JRS 84 (1994).
- Tacitus, Dialogue 29.1; Gellius 12.1 (Favorinus); Pliny, Letters 6.3 (nurse's farm, 100,000 sesterces); Bradley, "Wet-nursing at Rome" (in Rawson 1986); Horace, Epistles 2.1.70–71 (Orbilius); Quintilian 1.3.14; Harris, Ancient Literacy (1989).
- Finley, Ancient Slavery and Modern Ideology (1980), five slave societies; Brunt, Italian Manpower (1971); Scheidel, JRS 95 (2005); Scheidel, JRS 87 (1997); Harris, JRS 89 (1999) (writer checked online; titles and years agree).
- Plutarch, Caesar 15 (a million captured); Varro, On Agriculture 1.17.1; Columella 1.6.3 (ergastulum windows out of reach); Treggiari, "Jobs in the Household of Livia", PBSR 43 (1975).
- Tacitus, Annals 14.42–45 (Pedanius Secundus, AD 61); Seneca, Letters 47.1.
- Diodorus 36.3–10 (decree of 104, Licinius Nerva's manumissions stopped, Salvius and Athenion, Aquillius); Bradley, Slavery and Rebellion in the Roman World (1989) and Slaves and Masters in the Roman Empire (1984).
- Syll.³ 543 (Philip V to Larisa, 214 BC); Horace, Satires 1.6.45–48; Taylor, AJP 82 (1961); CIL VI 9499 (Hermia and Philematium, "gremio" at seven).
- Petronius, Satyricon 75–76 (from Asia, fourteen years "ad delicias", thirty million lost in a day, ten million in one voyage, land and lending) and 71 (epitaph: seviratus, thirty million, never heard a philosopher); Veyne, Annales 1961; Finley, The Ancient Economy (1973); D'Arms (1981).
- Rawson (ed.), The Family in Ancient Rome (1986); Treggiari, Roman Marriage (1991); Dixon, The Roman Mother (1988) and The Roman Family (1992); Bradley, Discovering the Roman Family (1991); Saller and Shaw, JRS 74 (1984); Martin, JRS 86 (1996).
- Pointers checked true of their targets: 2.4 (household priesthood; manus forms, Gaius 1.110–113; naming day, bulla, toga virilis); 4.4 (second-century captives; Cato's estate; Eunus, Diodorus 34/35.2); 5.1 (Cornelia); 5.3 (Spartacus; its pointer "Module 9.3 places the revolt within the institution" is honoured); 5.5 (Hortensia, Appian 4.32–34); 6.1 (Livia); 6.2 (Augustan marriage laws; freeborn mother of three freed from guardianship); 7.1 (Agrippina); 7.4 (Julia Domna, mother of the camps); 7.5 (imperial slaves and freedmen kept the accounts); 8.3 (unilateral divorce confined to grave causes, 331); 9.1, 10.2 and deep dive 11.4 against their prompts.
- House style: British spelling, no em dashes, no preamble or closing filler; 8 sections, 8 dispute boxes, 10 self-test items, 3 carry-forward items.
