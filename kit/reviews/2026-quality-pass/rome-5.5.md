# Rome 5.5: Antony, Octavian and Cleopatra

Verdict: fix
Body words: 2794 (target 2500)

## Coverage
- aftermath of the Ides, the funeral and the will: covered (Antony's speech handed to 11.7)
- Octavian's arrival as Caesar's heir and his private army: covered
- Cicero's Philippics and the war of Mutina: covered (but see finding 2 on the pointer)
- triumvirate of 43, proscriptions, Cicero's death: covered
- Philippi and the deaths of Brutus and Cassius: covered
- Perusia, Fulvia, Brundisium, Sextus Pompey, Naulochus: covered
- Antony in the East, the Parthian disaster, the Donations: covered
- Cleopatra as Ptolemaic queen and as Roman propaganda, pointing back to Greek 7.1 and 7.3: covered
- propaganda war, Antony's will, declaration of war on Cleopatra alone: covered
- Actium, the deaths of Antony and Cleopatra, the annexation of Egypt: covered
- the poets' Actium (Virgil's shield, Odes 1.37, Propertius) against the battle: covered

## Findings
1. [error | accuracy] Section "Caesar's heir and Cicero's war: Octavian and Mutina".
   Current: "called himself Gaius Julius Caesar; "Octavian" is a modern convenience."
   Problem: The name is ancient. Cicero calls him Octavianus in a letter of June 44, and Dio says that by adoption he was named Gaius Julius Caesar Octavianus (46.47); what is true is that he never used it.
   Fix: "called himself Gaius Julius Caesar; "Octavian" renders the Octavianus of Cicero's letters (<em>Letters to Atticus</em> 15.12.2), a name he never used."
   Basis: Att. 15.12.2 ("in Octaviano ... satis ingeni"), noted as Cicero's first use of the name: https://epistulae.substack.com/p/10-june-44-bce-to-atticus-at-rome ; Dio 46.47, Cary translation: https://lexundria.com/dio/46.47/cy

2. [error | pointer] Section "Caesar's heir and Cicero's war: Octavian and Mutina".
   Current: "(module 5.6 and deep dive module 11.5 treat them as oratory)"
   Problem: Module 5.6 never mentions the Philippics; its Cicero section treats the speeches in general, the Pro Sestio and the rhetorical works, and hands the Catilinarians to 5.3. Deep dive 11.5's prompt does name the Philippics.
   Fix: "(deep dive module 11.5 treats them as oratory)"
   Basis: rome/r-5.6.html (no occurrence of "Philippic"); roman-syllabus.html data-id 11.5 ("the Philippics and his death in 43 BC").

3. [should-fix | register] Section "The war of words, the will and the declaration" (dispute box).
   Current: "Modern historians divide between those who suspect forgery or selective reading by Octavian and those who find the clauses plausible for a man already living as a Hellenistic king."
   Problem: Both modern sides are unnamed; the house register wants names on each side.
   Fix: "Ronald Syme (<em>The Roman Revolution</em>, 1939) found the discovery suspiciously opportune; J. R. Johnson (1978) argued that the will was genuine and that its legal flaws tell for its authenticity."
   Basis: Johnson, "The Authenticity and Validity of Antony's Will", L'Antiquité Classique 47 (1978) 494–503 ("Antony's Will was authentic (not a forgery by Octavian)"; "Any supposed legal flaw ... is evidence for authenticity"): https://sites.uclouvain.be/antclas/AC_1978_art_13.htm ; Crook, JRS 47 (1957) 36–38, written against Syme's "An opportune discovery": https://www.cambridge.org/core/journals/journal-of-roman-studies/article/abs/legal-point-about-mark-antonys-will/C79C649971ABB3268331219CED808509 . Crook's abstract names Syme's phrase but not the book; The Roman Revolution is the obvious source but was not checked. Length about neutral.

4. [minor | figure] Section "Perusia, Brundisium and Sextus Pompey".
   Current: "on land confiscated from eighteen Italian towns"
   Problem: The count is unattributed.
   Fix: "on land confiscated from eighteen Italian towns (Appian 4.3)"
   Basis: Appian, Civil Wars 4.3 (the eighteen cities promised to the soldiers).

5. [minor | accuracy] Section "The war of words, the will and the declaration".
   Current: ""She is my wife" (<em>Augustus</em> 69)"
   Problem: Editors punctuate "uxor mea est" either as a statement or as a question ("Is she my wife?"), which reverses Antony's meaning; the report gives one reading as the text.
   Fix: ""She is my wife", or, as some editors punctuate it, "Is she my wife?" (<em>Augustus</em> 69)"
   Basis: not checked online; the two punctuations of Suetonius, Augustus 69.2 are a known crux. Optional.

6. [minor | style] Section "Actium and Alexandria, 31–30" and "Self-test", question 6.
   Current: "Octavian's memoirs, cited by Plutarch, gave not more than 5,000 dead" (body) and "how did Octavian's memoirs handle his own part?" (question 6)
   Problem: The memoirs were written by Augustus after 27 BC; the report itself says "Augustus later wrote" of the same work's comet passage.
   Fix: "Augustus' memoirs, cited by Plutarch, gave not more than 5,000 dead" and "how did Augustus' memoirs handle his own part?"
   Basis: Suetonius, Augustus 85.1 (thirteen books, down to the Cantabrian war); house convention in AGENT-SPEC.md.

## Confirmed
- Livy, Periochae 120: "the names of 130 senators" among the proscribed; head and right hand on the Rostra: https://livius.org/sources/content/livy/livy-periochae-116-120
- Lange, "The Battle of Actium: A Reconsideration", CQ 61.2 (2011) 607–622, sets the ancient view that Antony fought for victory against Kromayer's breakout consensus, which almost all recent accounts follow; the report's "most modern accounts accept a planned breakout ... while Carsten Lange (2011) argues that Antony fought to win" matches: https://vbn.aau.dk/da/publications/the-battle-of-actium-a-reconsideration
- Appian 2.118 (Lepidus' legion on the island), 4.2 (the river islet, near Mutina; Plutarch puts the meeting near Bononia), 4.5 (about 300 senators, 2,000 equestrians), 4.8–11 (the edict), 4.32–34 (1,400 women), 4.108 (nineteen legions each; 20,000 cavalry against 13,000), 5.48–49, 5.123–126.
- Plutarch, Cicero 46 (two days; "more than two hundred"), 48; Antony 20 (300), 22, 26, 27, 36, 37 (60,000 infantry), 50 (twenty-seven days; 20,000 foot, 4,000 horse, more than half to disease), 53, 54 (the Donations as reported), 58–59, 60, 61 (500 ships, 100,000 foot, 12,000 horse; 250 ships, 80,000 foot), 64 (sixty Egyptian ships kept; sails aboard), 66, 68 (5,000 dead, 300 ships, from the memoirs), 81, 86; Brutus 41 (Artorius, from the memoirs), 43.
- Suetonius, Julius 83 (three quarters; 300 sesterces; gardens), 84; Augustus 13, 15 ("scribunt quidam" the 300 at the altar), 27.1 ("inceptam utroque acerbius exercuit"), 68, 91 (a friend's dream; Plutarch names Artorius).
- Cicero, Philippics 1.1 (the Athenian precedent), 1.3 (dictatorship abolished), 2.93 (700 million at the temple of Ops); Letters to Atticus 16.8.1 (500 denarii a man); Letters to Friends 11.20.1 (tollendum).
- Res Gestae 1.1, 25.1 (about 30,000 slaves), 25.2 ("sponte sua"), 25.3 (over 700 senators), 27.1; Pliny 2.93–94, 7.148; Velleius 2.66, 2.74.4, 2.85; Tacitus, Annals 1.10, 2.59; Dio 50.3, 50.4 (fetial spear), 50.5, 50.15; Periochae 120.
- Horace, Epode 9.11–16; Odes 1.37.13 ("vix una sospes navis"), 21, 32; Aeneid 8.678–679, 688, 698–706; Propertius 3.11.39, 4.6.
- van Minnen 2000 (Ancient Society 30) on the Canidius papyrus and its "ginesthoi"; Murray and Petsas, Octavian's Campsite Memorial for the Actian War (1989); Wyke, The Roman Mistress (2002); Roller, Cleopatra: A Biography (2010).
- Pointers checked against targets: Greek 6.3 (amnesty of 403), Greek 7.1 (Ptolemies as basileis and pharaohs), Greek 7.3 (Cleopatra's alliance with Caesar; Tarn 1931; Plutarch, Antony 86 and Strabo on asp or poison), 5.3, 5.4, 6.1, 6.3; not-yet-written targets against their syllabus prompts: 11.2 (march of 43), 11.4 (Hortensia, Fulvia), 11.5 (Philippics), 11.7 (Antony's funeral speech), 12.3 (the shield).
- Syllabus deep dive 12.1 ("module 5.5 places the poem in the season of Brundisium") and 12.3 ("modules 6.3 and 5.5 read ... its Actium") are true of this report.
- Not checked (Orosius text pages unreachable): Orosius 6.19 on the fleets; the figures recalled for it, 230 beaked ships for Octavian and 170 for Antony, are the report's.
