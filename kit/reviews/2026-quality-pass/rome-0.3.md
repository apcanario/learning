# Rome 0.3: The timeline spine, 1000 BC to AD 476

Verdict: fix
Body words: 2733 (target 2500)

## Coverage
- Period names and ranges (Iron Age Italy, regal, early, middle and late Republic, Principate, third-century crisis, late empire) and why the boundaries fall where they do: covered
- 15 to 20 anchor dates, one sentence each: covered (20), but none between 27 BC and AD 284 (finding 3)
- Consular years and the Fasti: covered
- Years from the foundation and the dates of Timaeus, Ennius, Fabius Pictor, Cincius, Cato, Polybius and Varro: covered
- Emperors' regnal years: covered
- The indiction: covered
- The foundation date problem: covered
- Seven kings for 244 years: covered (pointer to 1.5)
- Dictator years and the Varronian chronology: covered
- 390 or 387 for the Gallic sack: covered
- First consuls and the Capitoline temple: covered
- When the Republic "ended": covered
- 476 as a convention and 1453 as a different kind of end: covered
- A clean dated list to copy out: covered

## Findings
1. [error] [attribution] Section "The periods and why the boundaries fall where they do".
   Current: "to the decades after 367 and above all after 287."
   Problem: Hölkeskamp's book (subtitled "Studien zur sozialen und politischen Geschichte der Römischen Republik im 4. Jh. v. Chr.") places the formation of the patricio-plebeian nobility in the course of the fourth century, from the Licinio-Sextian laws to the end of the Conflict of the Orders; module 3.1 gives "the generations after 367". "Above all after 287" puts the main process in the third century.
   Fix: "to the decades between the Licinio-Sextian laws of 367 and the lex Hortensia of 287."
   Basis: BMCR 2012.09.30, review of the second edition: the nobility emerged "in the course of the fourth century BC" (https://bmcr.brynmawr.edu/?p=38511); rome/r-3.1.html.

2. [should-fix] [lane] Section "The big chronological problems" (sub-section "The first consuls and the Capitoline temple").
   Current: "<aside class="dispute"><strong>Where sources disagree.</strong> Einar Gjerstad (<em>Early Rome</em>, 1953–73) argued from Forum stratigraphy"
   Problem: The box duplicates module 1.6's box under "Athens 510, Rome 509" (Gjerstad's end of the monarchy about 450, Cornell's answer from the treaty and Flavius' inscription, the Athenian parallel), which is the natural home; 1.6 also has the full Athens comparison.
   Fix: delete the aside, and add after "as if several traditions had been stacked.": " Gjerstad's lowering of the end of the monarchy to about 450, and the suspicious closeness of 509 to Athens' 510, are weighed in module 1.6."
   Basis: rome/r-1.6.html, "Athens 510, Rome 509" and its dispute box.

3. [should-fix] [register] Section "The anchor dates: a list to copy out".
   Current: "<tr><td>AD 284</td><td>Diocletian emperor</td>"
   Problem: The list jumps from 27 BC to AD 284: the Principate, a quarter of the span, has no anchor, and AD 235, the boundary used by the period table and by the five-block peg below the list, is missing. AD 1453 lies outside the list's stated span and already has its own section.
   Fix: delete the row "<tr><td>AD 1453</td><td>Constantinople falls to Mehmed II, 29 May</td><td>The last Roman state ends with its emperor on the walls.</td></tr>" and add before the AD 284 row: "<tr><td>AD 235</td><td>Severus Alexander murdered</td><td>The last stable dynasty ends; fifty years of short reigns and usurpers begin.</td></tr>"
   Basis: prompt 0.3 (span 1000 BC to AD 476, with a closing note on 1453); the report's own period table.

4. [should-fix] [register] Section "Self-test" (question 9).
   Current: "Augustus himself claimed to have restored the <em>res publica</em> (<em>Res Gestae</em> 34)."
   Problem: Res Gestae 34 says he transferred the res publica to the Senate and people ("transtuli"), as the body correctly quotes; "restored" (res publica restituta) is the wording of the Fasti Praenestini and the Laudatio Turiae, not of RG 34.
   Fix: "Augustus himself claimed to have transferred the <em>res publica</em> to the Senate and people (<em>Res Gestae</em> 34)."
   Basis: Res Gestae 34.1 (Latin text); the report's own section "When did the Republic end?".

5. [minor] [accuracy] Section "Years from the founding: seven ancient answers".
   Current: "<td>c. 751 BC</td>"
   Problem: The row's own basis, Olympiad 7.1 (Dionysius 1.74.2), is 752/1; "c. 751" blurs Cato into Polybius' 751/0 on the next row.
   Fix: "<td>752/1 BC</td>"
   Basis: Dionysius 1.74.2 (Loeb text: Cato's 432 years after Troy fall in the first year of the seventh Olympiad).

6. [minor] [accuracy] Section "The periods and why the boundaries fall where they do".
   Current: "ends as the settlement turns urban"
   Problem: The report's own section on the foundation date, and module 1.5, put the urban transformation (the first Forum paving) in the later seventh century; c. 730 is the start of the orientalising phase, Latial IVA in module 1.1.
   Fix: "ends as the orientalising phase begins (module 1.1)"
   Basis: rome/r-0.3.html, "The foundation date"; rome/r-1.5.html, "Seven reigns for 244 years"; rome/r-1.1.html phase table.

7. [minor] [style] Section "The big chronological problems" (sub-section "When did the Republic end?").
   Current: "Augustus claimed no ending: in 28–27 BC he "transferred the <em>res publica</em>" to the Senate and people (<em>Res Gestae</em> 34)."
   Problem: House style is Octavian before 27 BC; as written, "Augustus" performs the act of 28 BC.
   Fix: "Augustus claimed no ending: in the <em>Res Gestae</em> he wrote that in 28–27 BC he had "transferred the <em>res publica</em>" to the Senate and people (34)."
   Basis: AGENT-SPEC.md, Rome course naming rule.

## Confirmed
- Dionysius 1.74.1: Timaeus 38 years before the first Olympiad (814/13); Fabius Olympiad 8.1 (748/7); Cincius Olympiad 12.4 (729/8) (Loeb text).
- Dionysius 1.74.3: Polybius Olympiad 7.2 (751/0); 1.74.4: the Gallic sack in Pyrgion's archonship, Olympiad 98.1 (388/7) (Loeb text).
- Varro, On Agriculture 3.1.2: Ennius' "septingenti sunt paulo plus aut minus anni" (Latin text).
- Plutarch, Romulus 12: Tarutius' horoscope for Varro, Olympiad 6.3 (Perrin text).
- Censorinus, De die natali 21: AD 238 the 991st year by Varro's count (Latin text).
- Polybius 1.5.1 (start where Timaeus stopped), 1.6.1–2 (King's Peace and Rhegium), 3.22.1–2 (twenty-eight years before Xerxes, 508/7) (text).
- Pliny, Natural History 33.19: Flavius' Concord shrine 204 years after the Capitoline dedication (Latin text).
- Livy 7.3.5–7 (nail law), 2.8.6–8 (first-year dedication), 2.1.1, 3.33.1 ("anno trecentesimo altero"), 6.35.10 (five years of anarchy), 6.1.2, 6.1.11 (18 July) (Latin text).
- Diodorus 15.75.1: one year of anarchy (text).
- Tacitus, Histories 3.72 (Horatius iterum consul); Annals 1.1 ("nomine principis") and 1.3 ("qui rem publicam vidisset") (Latin text).
- Plutarch, Tiberius Gracchus 20.1: first civil strife since the kings to end in bloodshed (Perrin text).
- Res Gestae 4 (tribunician power XXXVII) and 34 ("transtuli"); Dio 53.17 (strictly a monarchy from 27); Sallust, Catiline 10; Velleius 2.1 (texts).
- Luke 3:1; Justinian, Novel 47 (537); Marcellinus Comes s.a. 476 ("Hesperium Romanae gentis imperium ... periit") (texts).
- Dictator years 333, 324, 309, 301; consular year from 1 January in 153; Basilius the last private consul, 541; indiction from 1 September 312; Dionysius Exiguus 525; Bede 731 (standard).
- Anchor-date details: Actium 2 September 31; 16 January 27; Milvian Bridge 28 October 312; Constantinople dedicated 11 May 330; Theodosius died 395; western consuls to 534; Julius Nepos to 480; Hieronymus Wolf 1557; Morea 1460, Trebizond 1461 (standard).
- Block arithmetic: 244, 245, 237, 261 (no year zero) and 241 years.
- Modern: Croke, "A.D. 476: the manufacture of a turning point", Chiron 13 (1983); Gjerstad 1953–73; Syme 1939; Gruen 1974; Flower 2010 (end of the republic of the nobles with Sulla's march, 88); Brown 1971; Goffart 1980; Heather 2005; Ward-Perkins 2005.
- Not-yet-written pointers match their syllabus prompts: 8.2 (Diocletian's rebuilt state, the Dominate debate), 8.5 (the fall debate), 8.6 (the East to 1453), 9.1 (Twelve Tables), 11.8 (why the Republic fell).
- Written pointers true of their targets: module 0.1 (fasti and pontifical records), 1.1 (first Forum graves), 1.3 (Romulus as Aeneas' grandson), 1.4 (Carandini's wall), 1.5 (seven reigns), 2.3 (the pre-Julian drift of about three months), Greek module 0.3 (archons and Olympiads).
- Incoming pointers true of 0.3: from 1.4 (rival dates), 1.5 (variants), 2.3 (conversion of years), 3.1 (anarchy), 3.3 (390 against 387/6).
