# Rome 4.5: Polybius, Cato and the Greek invasion of Rome

Verdict: fix
Body words: 2783 (target 2500)

## Coverage
- Polybius as hostage and friend of Scipio Aemilianus: covered
- Book 6, the mixed constitution (consuls, Senate, people): covered
- The cycle of constitutions: covered
- The army camp and the aristocratic funeral as causes of strength: covered
- Criticisms of the analysis: covered
- Livius Andronicus' Odusia and first plays of 240: covered
- Naevius' Punic War: covered
- Ennius' Annales and the Latin hexameter: covered
- Plautus and Terence and their Greek originals: covered
- Fabius Pictor writing in Greek: covered (work and Polybius' criticism handed to 0.1 explicitly)
- Cato as the anti-Hellene who knew Greek: covered
- Origines: covered
- On Agriculture: covered (handed to 4.4 explicitly)
- Censorship of 184: covered
- Philosophers' embassy of 155 and Carneades on both sides of justice: covered
- The "Scipionic circle" and its modern critics: covered
- Horace, Epistles 2.1.156: covered
- Point back to Greek 7.3: covered

## Findings
1. [error] [attribution] Section "Philosophers in the Senate, 155 BC".
   Current: "and in 181 had burned books of Numa found to contain Pythagorean doctrine (Livy 40.29)"
   Problem: Livy describes the Greek books as philosophy; the Pythagorean label is Valerius Antias', which Livy rejects as a plausible lie fitted to the false belief that Numa heard Pythagoras (40.29.8). The report cites Livy for the claim he denies, and the prompt for deep dive 13.1 now relies on this sentence.
   Fix: "and in 181 had burned books ascribed to Numa, Greek works of philosophy that Valerius Antias called Pythagorean, a claim Livy rejects (40.29)"
   Basis: Livy 40.29.7–8; J. Richardson, "Numa and Pythagoras: Did Livy Misrepresent Valerius Antias?", Histos 18 (2024) 38–51, on Livy's charge against Antias (https://histos.org/index.php/histos/article/view/11).

2. [minor] [pointer] Section "Comedy in Greek dress: Plautus and Terence".
   Current: "Titus Maccius Plautus wrote from about 205"
   Problem: Module 5.6 points here for "comic poets from Umbria and Carthage"; Terence's Carthage is given, Plautus' Umbria is not.
   Fix: "Titus Maccius Plautus, from Sarsina in Umbria, wrote from about 205"
   Basis: rome/r-5.6.html (pointer to 4.5); Festus, s.v. Ploti, and Jerome, Chronicle, for Sarsina (not checked online).

3. [minor] [lane] Section "Greek history and Latin prose: Fabius Pictor and Cato".
   Current: "the head of a household should be a seller, not a buyer (2.7); module 4.4 uses it as evidence"
   Problem: Module 4.4 quotes the same precept (2.7) as part of its evidence, and the crosscheck lists it as a shared passage (4.4 ~ 4.5). Another line gives the self-portrait without repeating the neighbour.
   Fix: "its preface ranks the farmer above the trader and the moneylender and says the bravest soldiers come from farmers (preface 1–4); module 4.4 uses the estate as evidence"
   Basis: rome/r-4.4.html; Cato, On Agriculture, preface 1–4; crosscheck pre-run, section 2.

4. [minor] [accuracy] Section "The "Scipionic circle" and captive Greece".
   Current: "The epigram concerns literary taste, and its chronology is loose, since Livius' first play preceded Hannibal's war."
   Problem: Horace's words are "post Punica bella" (2.1.162), which fit Livius' play of 240 if he meant the first war; calling the chronology loose assumes he meant the second.
   Fix: "The epigram concerns literary taste, and its chronology is vague: <em>post Punica bella</em> fits Livius' first play of 240 only if Horace meant the first war."
   Basis: Horace, Epistles 2.1.161–163; not checked against Brink's commentary.

5. [minor] [style] Section "The "Scipionic circle" and captive Greece" (last dispute box).
   Current: "Calpurnius Piso to 154, "
   Problem: The other three dates carry citations and Piso's does not; modules 4.4 and 5.6 point to this box for the rival dates.
   Fix: "Calpurnius Piso to 154 (Pliny, <em>Natural History</em> 17.244), "
   Basis: Pliny, Natural History 17.244 (Piso dates the overthrow of modesty to the consulship of 154).

## Confirmed
- Polybius 28.6: cavalry commander under Archon in 170/169 (Smith's Dictionary, citing Polybius 28.3 and 28.6, https://cts.perseids.org/read/pdlrefwk/viaf88890045/003/perseus-eng1/P.polybius_4); 39.5 (40.8–10 in the older numbering): the commissioners left him to go round the cities and settle their laws.
- Plutarch, Philopoemen 21: Polybius carried the urn (same entry).
- Pseudo-Lucian, Long Lives 22: thrown from his horse riding in from the country, died at eighty-two (https://cts.perseids.org/read/greekLit/tlg0062/tlg011/perseus-eng2/21-22).
- Lactantius renders Carneades' second speech: no natural justice, justice that serves others is folly, and Romans who gave back their conquests would return to huts (Epitome 56, https://sacred-texts.com/chr/ecf/007/0070244.htm; Divine Institutes 5.14–16).
- The prompt for deep dive 13.1 is true of this report: the decree of 161 (Gellius 15.11.1), the books of Numa in 181 and the embassy of 155 with Carneades' two speeches are all here, once finding 1 is applied.
- Pointers true: Greek 7.3 (fewer than 300 of the thousand came home; Polybius' answer in brief; Horace's line framing tutors, loot and gods), Greek 7.2 (Carneades' graded scepticism), Greek 10.12 (Naevius' Bellum Punicum opening with Aeneas), 0.1 (Polybius as a source; Fabius Pictor and Polybius' criticism; Wiseman on drama at the games), 3.5 (Livius' Tarentine origin), 4.1, 4.4, and 9.2 (prompt includes camp, decimation and rewards). Pointers into this report from 3.1, 5.1 and 5.6 (mixed constitution; rival dates of decline) are true.
- Checked from the texts as known: Polybius 1.1.5, 3.4, 6.2, 6.3–10, 6.11–18, 6.27–32, 6.37–39, 6.42–44, 6.48–52, 6.53–54, 6.56, 6.57, 31.11–15, 31.23–24, 31.25, 38.21–22; Plutarch, Cato Maior 2, 3, 9, 12, 16–19, 22, 23; Tacitus, Annals 4.33; Cicero, On the Republic 2.1–2, 5.1, Brutus 60, 71, 72, 79, On Old Age 26, Tusculan Disputations 1.3, On Ends 1.9; Gellius 2.23, 3.3.15, 15.11.1, 17.17.1, 17.21.45, 18.9.5; Nepos, Cato 1.4; Plautus, Trinummus 19; Terence, Andria 9–21, Adelphoe 15–21; Suetonius, Life of Terence; Pliny 29.14; Dionysius 1.11.1; Livy 7.2, 39.6.7, 39.40–44; Pausanias 7.11; Velleius 1.13.3; Horace, Epistles 2.1.69–71, 156–163; Walbank 1972 and Commentary; Champion 2004; Millar 1984; Hölkeskamp 2010; Mouritsen 2001; Feeney 2016; Fraenkel 1922; Handley 1968; Astin 1967 and 1978; Gruen 1992; Strasburger 1966; Zetzel 1972; Wallace-Hadrill 2008.
