# Rome 13.3: The rival schools at Rome

Verdict: fix
Body words: 3800 (target 2500; the target is a guide, no cut asked)

## Coverage
- Module 5.6 pointed back to (Lucretius, Amafinius, Philodemus under Piso, Cassius), with more depth: covered
- Philodemus, Piso and the Villa of the Papyri library: covered
- Cassius the tyrannicide: covered
- Atticus: covered
- Horace's "pig from Epicurus' herd" (*Epistles* 1.4.16): covered
- New Academy, Cicero the sceptic, what his scepticism let him do: covered
- Antiochus' Old Academy, followed by Varro and Brutus: covered
- Peripatetics; Cratippus as teacher of Cicero's son at Athens: covered
- Nigidius Figulus: covered
- The Sextii: covered
- Neopythagoreans: thin (one paragraph of names; enough for the prompt)
- Cynics under the empire: Demetrius, friend of Seneca and Thrasea: covered (Thrasea's death handed to 13.4, correctly)
- Lucian's *On the Death of Peregrinus* told in full (Greek 7.4 names it only): covered
- Why the Stoa won the senatorial class: covered
- Marcus Aurelius' chairs at Athens, 176, and what they show: covered
- Lane notes: Greek 12.6's forward pointer (Roman Epicureans) and Greek 12.8's hand-off (Cicero and the Academy at Rome, Antiochus' Roman following) both kept without retelling the Greek doctrine; Greek 12.5's hand-off of Demetrius and Peregrinus kept: covered

## Findings
1. [error] [accuracy] Section "Epicureans in public life: Cassius, Atticus and the pig".
   Current: "<em>On the Nature of the Gods</em> 1, show that the school had consular spokesmen"
   Problem: Neither speaker was a consul. Lucius Manlius Torquatus, the speaker of *On Ends* 1, reached the praetorship (49) and died in 46; his father was consul in 65. Gaius Velleius is introduced by Cicero only as a senator.
   Fix: "<em>On the Nature of the Gods</em> 1, show that the school had spokesmen in the Senate"
   Basis: Wikipedia, "Lucius Manlius Torquatus (praetor 49 BC)" (praetor 49, propraetor 48–46, died 46); Smith, *Dictionary of Greek and Roman Biography*, "C. Velleius" (a senator, Cicero, *On the Nature of the Gods* 1.15).

2. [error] [accuracy] Section "Nigidius, the Sextii and the Pythagoreans".
   Current: "and the young Seneca kept off meat for a year until his father, fearing that it would look like a foreign cult under Tiberius, made him stop (108.17–22)."
   Problem: Seneca says the reverse about his father's motive. Under Tiberius abstinence from certain meats was read as a sign of foreign cult, but his father "did not fear slander but hated philosophy" (*non calumniam timebat sed philosophiam oderat*, *Letters* 108.22). Deep dive module 13.5 gives it correctly.
   Fix: "and the young Seneca kept off meat for a year, until, at a time when abstaining from certain meats was taken as a sign of foreign cults, his father, who did not fear slander but hated philosophy, asked him to eat as before (108.17–22)."
   Basis: Seneca, *Letters* 108.22 (Latin from memory, matching `rome/r-13.5.html`, section "Corduba and the elder Seneca": "his father, who did not fear slander but hated philosophy, asked him to eat properly again (Letters 108.17–22)").

3. [error] [pointer] Section "Nigidius, the Sextii and the Pythagoreans".
   Current: "Pythagoras had an old Roman legend, as Numa's teacher, which Livy rejects on chronology (1.18) and module 2.1 touches."
   Problem: Module 2.1 does not touch the legend of Pythagoras as Numa's teacher; it mentions Pythagoras only in passing (Plutarch crediting Numa, in agreement with Pythagoras, with a ban on images, and Stoic and Pythagorean critiques of images). The legend, with Livy 1.18.2 rejecting it on chronology, is in module 1.5's dispute box.
   Fix: "Pythagoras had an old Roman legend, as Numa's teacher, which Livy rejects on chronology (1.18.2) and module 1.5 weighs."
   Basis: `rome/r-1.5.html` dispute box ("Some made Numa a pupil of Pythagoras. Livy 1.18.2 and Cicero, On the Republic 2.28–29, reject it on chronology"); `rome/r-2.1.html` (Pythagoras only at Numa 8 and the images dispute).

4. [should-fix] [attribution] Section "Epicureans in public life: Cassius, Atticus and the pig".
   Current: "so that his conspiracy in 44 needs explaining against his school, not from it."
   Problem: This overstates Sedley. He dates the conversion to about 48, links it to Cassius' withdrawal from the war, and concludes that Epicureanism is unlikely to have been the main motive for the conspiracy. He then sets out how Cassius could justify the murder within Epicurean terms. "Against his school" says the opposite of that second step.
   Fix: "so that his school did not drive him to the conspiracy of 44, though Sedley shows how Cassius could justify it in Epicurean terms."
   Basis: Sedley, "The Ethics of Brutus and Cassius", *JRS* 87 (1997) 41–53, opening extract on Cambridge Core (https://www.cambridge.org/core/product/F1C0581B87E61A866526B2F6939DA446): Cassius an Epicurean "just three or four years" by March 44; withdrawal of 48; Sedley will propose how Cassius justified the murder within Epicureanism.

5. [should-fix] [attribution] Section "Antiochus and the Old Academy: Lucullus, Varro, Brutus".
   Current: "John Moles is among those who read him so."
   Problem: The writer names no work and took the attribution from Sedley's notes without checking it (writer's note 3). Moles' own *Commentary on Plutarch's Brutus* says that Plutarch "glosses over Brutus' Stoic characteristics, preferring instead to emphasize Brutus the Academic". That accepts Stoic traits but does not plainly call Brutus a Stoic. As it stands, the Stoic side of the box rests on an unverified name.
   Fix: "John Moles (<em>A Commentary on Plutarch's Brutus</em>, 2017) finds Stoic characteristics in Brutus that Plutarch plays down." Alternatively, the maintainer can check which Moles work Sedley 1997 cites (possibly his article on Brutus' last words in *Latomus*, 1983; not verified) and name that.
   Basis: Moles, *A Commentary on Plutarch's Brutus*, Histos Supplement 7 (2017, ed. C. Pelling), https://histos.org/index.php/histos/article/download/681/672/780 (General Characteristics); Histos Supplements list, https://histos.org/HistosSupplements.html.

6. [should-fix] [accuracy] Section "Nigidius, the Sextii and the Pythagoreans".
   Current: "and the son's medical writings, used by Pliny, add a third face."
   Problem: The text treats as fact that Sextius Niger, the pharmacologist Pliny cites, is the philosopher's son. The identification is commonly made but not established.
   Fix: "and if, as many think, the son is the Sextius Niger whose pharmacology Pliny used, he adds a third face."
   Basis: Wikipedia, "Sextius Niger" (Pliny's "Sextio Nigro, qui graece scripsit"; Niger "may be identical" with the philosopher's son, "many think" so).

7. [should-fix] [lane] Section "Nigidius, the Sextii and the Pythagoreans".
   Current: "Sextius forbade meat; Seneca's teacher Sotion gave Pythagoras' reasons and Sextius' own, and the young Seneca kept off meat for a year"
   Problem: Deep dive module 13.5 tells the same anecdote at the same length (Sotion, the year without meat, the father under Tiberius, *Letters* 108.17–22), and it points to 13.3 only for the Sextii. Each anecdote should have one home, and Seneca's youth belongs to 13.5. Self-test 8 here uses the Tiberian detail, so any cut should keep one clause for it.
   Fix: apply finding 2 here, and leave it to the maintainer to shorten one of the two tellings (in 13.5, "module 13.3 has the Sextii and the year without meat" would do).
   Basis: `rome/r-13.5.html`, section "Corduba and the elder Seneca".

8. [should-fix] [pointer] Section "Epicureans in public life: Cassius, Atticus and the pig".
   Current: "The Garden told the wise man to stay out of politics unless something intervened (Greek module 12.6)."
   Problem: Greek 12.6 gives the rule ("the wise man stays out of politics (10.119)") but not the exception. "Unless something intervenes" is Seneca's report of Epicurus (*On Leisure* 3.2), which deep dive module 13.2 gives.
   Fix: "The Garden told the wise man to stay out of politics (Greek module 12.6), unless, Seneca adds, something intervened (<em>On Leisure</em> 3.2)."
   Basis: `greece/r-12.6.html`, section "Friendship, and justice as a compact"; `rome/r-13.2.html` (*On Leisure* 3.2).

9. [minor] [style] Section "Nigidius, the Sextii and the Pythagoreans".
   Current: "Claudianus Mamertus, a Christian writer of the fifth century, says the Sextii taught"
   Problem: There is no citation. The passage names Sextius father and son together, so "the Sextii" is right.
   Fix: "Claudianus Mamertus, a Christian writer of the fifth century, says the Sextii taught" → add after "without place,": " (<em>On the State of the Soul</em> 2.8)" so that it reads "says the Sextii taught that the soul is incorporeal and without place (<em>On the State of the Soul</em> 2.8),"
   Basis: Wikipedia, "Sextius Niger", quoting *De statu animae* 2.8: "apud quos Sextius pater, Sextius filius ... philosophati sunt". The incorporeality wording is not checked against the Latin.

10. [minor] [register] Section "Self-test", question 4.
    Current: "Horace applies it to himself in a verse letter to Tibullus"
    Problem: The body hedges ("to Albius, usually taken to be Tibullus"). The answer drops the hedge.
    Fix: "Horace applies it to himself in a verse letter to Albius, usually taken to be Tibullus"
    Basis: the body, section "Epicureans in public life".

11. [minor] [accuracy] Section "The Peripatetics and Cratippus".
    Current: "Late in the second century Alexander of Aphrodisias"
    Problem: *On Fate* is dedicated to Septimius Severus and Caracalla as joint emperors, so it was written between 198 and 209, about 200 rather than late in the second century.
    Fix: "About 200 Alexander of Aphrodisias"
    Basis: not checked by search; joint reign of Severus and Caracalla 198–209.

12. [minor] [figure] Section "Why the Stoa won, and the chairs of 176", the matrix.
    Current: "Nigidius, Quintus Sextius"
    Problem: The text leaves Sextius' school between Pythagoreanism and Stoicism ("Pythagorean in diet and Stoic in tone", and the dispute box). The figure files him as a Pythagorean without the text's qualifier. The caption also omits the passage behind the "none" cells: the four salaried schools are Lucian's list (*Eunuch* 3), which the text cites.
    Fix: "Nigidius, Quintus Sextius (disputed)"; and in the caption replace "as cited in Greek module 7.4." with "as cited in Greek module 7.4, with Lucian, <em>Eunuch</em> 3, for the four salaried schools."
    Basis: R-1 figure lessons (the text's qualifiers; the caption names the passages).

13. [minor] [figure] Section "Why the Stoa won, and the chairs of 176", the timeline caption.
    Current: "Philo: Greek module 12.8;"
    Problem: The caption should name the passage the text cites, or say that the text gives the date without one. The text gives 88 with only a pointer. Greek 12.8 cites Cicero, *Brutus* 306.
    Fix: "Philo: the year as the section Cicero the sceptic gives it, citing Greek module 12.8 (Cicero, <em>Brutus</em> 306);"
    Basis: `greece/r-12.8.html`, section "Clitomachus, Philo and Antiochus".

14. [minor] [accuracy] Section "The Cynics under the empire".
    Current: "Lucian, who was there, laughed at the father, recalling the murder,"
    Problem: Lucian laughed when Peregrinus called on his father's spirits, remembering the story of the murder (§37). "Laughed at the father" reads oddly and has no section number.
    Fix: "Lucian, who was there, laughed when he called on his father, recalling the murder (37),"
    Basis: Lucian, *On the Death of Peregrinus* 37, Harmon's Loeb translation at https://tertullian.org/rpearse/lucian/peregrinus.htm ("when he invoked those of his father as well ... I could not control my laughter").

## Confirmed
- Cicero, *Against Piso* 37: Piso as an Epicurean "product of the sty rather than the school" (attalus.org translation, §37). Writer's note 1 is cleared.
- *Against Piso* 68–72 (the unnamed Greek companion), Asconius on §68 naming Philodemus, *On Ends* 2.119 (Siro and Philodemus "excellent men and very learned"), Philodemus from Gadara, *On the Good King* addressed to a young relative of Piso, *On Vices* addressed to Virgil, Varius, Plotius Tucca and Quintilius Varus, about 800 rolls as an estimate, the *AP* 11.44 invitation to the twentieth (SEP, "Philodemus", https://plato.stanford.edu/entries/philodemus/).
- Papaccio's 40–20 BC date for the villa from its floors and Esposito's 40–25 BC for the paintings, in Lapatin (ed.) 2019 (BMCR 2020.01.40, https://bmcr.brynmawr.edu/2020/2020.01.40). Writer's note 4 is cleared for these two.
- Sedley, "The Ethics of Brutus and Cassius", *JRS* 87 (1997): Cassius' conversion about 48 and its link to his withdrawal; Momigliano's 1941 *JRS* review as the seminal survey of politicised Epicureans (Cambridge Core extract). Momigliano's "heroic Epicureanism", with virtue active (summary at liquisearch, "Gaius Cassius Longinus: Epicureanism"), supports the gloss "Epicureanism turned political". Writer's note 2 is cleared in substance. Not checked: the review was of Farrington's *Science and Politics in the Ancient World* (from memory; the writer's bibliography leaves this open).
- Moles' Brutus commentary is Histos Supplement 7, 2017 (histos.org).
- Lucian, *Eunuch*: an imperial salary of 10,000 drachmas a year, the same for Stoics, Platonists, Epicureans and Peripatetics; a Peripatetic vacancy; judges the "most prominent and oldest and wisest men in the city" (translation at people.well.com). Section number 3 not checked.
- Lucian, *Peregrinus*: §10 parricide, 11–14 Christians and the governor of Syria, 15 estate to Parium, 17 Agathobulus, 18 expelled by the city prefect, 19–20 Herodes and the near-stoning, the announcement, the pyre at Harpina 20 stades from Olympia at night as the moon rose, the invocation of mother and father (35–36), the vulture invented (38–39), the grey-haired witness (40), love of glory (Wikipedia "Peregrinus Proteus"; tertullian.org Harmon translation).
- Gellius 12.11, Ammianus 29.1.39, Athenagoras, *Embassy* 26 on Peregrinus (Wikipedia "Peregrinus Proteus").
- Anaxilaus of Larissa expelled in 28 BC for magic, after Eusebius' *Chronicle* (Wikipedia "Anaxilaus").
- Sextius father and son as philosophers in Claudianus Mamertus, *On the State of the Soul* 2.8 (Wikipedia "Sextius Niger"). Writer's note 5 is cleared ("the Sextii" is right).
- Philostratus, *Lives of the Sophists* 566 for the chairs and for Theodotus' appointment by Marcus (Smith's *Dictionary*, citing VS 566; Gibbon's note, citing Lucian's *Eunuch*, Philostratus p. 566 and Dio 71). Herodes' choice of the philosophers not checked by search; from memory it is right.
- Greek 7.4 records the chairs of 176 (Dio 72.31.3; VS 566), names *On the Death of Peregrinus* only, and gives Herodes Atticus: pointers true.
- Greek 12.5 hands Demetrius and Peregrinus to Rome 13.3; Greek 12.6 hands Philodemus, Cassius, Atticus and the villa to it and gives the will's twentieth; Greek 12.8 gives Philo in Rome in 88, Antiochus' Sosus and the Old Academy, Numenius and Middle Platonism, and hands Antiochus' Roman following to 13.3: pointers true.
- Module 5.6: Amafinius, Philodemus under Piso, Cassius (Plutarch, *Brutus* 37) each in a sentence; Nepos' *Atticus* on refusing office and helping each side: pointers true.
- Module 13.1: Philo and Cicero's student years, Brutus 315 and Antiochus, Staseas with Pupius Piso and Alexander with Crassus, Brutus drawing the young Romans at Athens into his army (Plutarch, *Brutus* 24): pointers true.
- Module 13.2: Cicero argues *On Fate* as an Academic; *officium* and the personae: pointers true. Module 13.5 (written): Seneca's use of Epicurus and the nightly review, *On Anger* 3.36: pointers true. 13.4 (unwritten): Demetrius at Thrasea's death, the expulsions, Cato's death as example: consistent with its prompt. Module 13.6 (written) treats Demetrius only as "module 13.3's Cynic": no duplication.
- House style: no em dashes; British spelling; Cicero's treatises in English and invectives in English (*Against Piso*, *Against Vatinius*); Dio given as 72(71).31.3 (Loeb with Boissevain); Octavian used for the period before 27 BC.
- Register: eight dispute boxes of two or three sentences, each with a named source or scholar on both sides; ten self-test questions whose answers agree with the body, except Q4's hedge (finding 10); three carry-forward items that transfer.
