# Rome 4.1: Carthage and Dido

Verdict: keep
Body words: 2819 (target 2500)

## Coverage
- Phoenician expansion west and Tyre: covered
- Foundation date, Timaeus' 814/813 against the eighth-century archaeology: covered
- Elissa before Virgil: Timaeus (FGrHist 566 F 82): covered
- Justin's epitome of Trogus 18.4–6: covered
- Oxhide and the Byrsa: covered
- Suicide to avoid marrying Iarbas: covered
- Virgil's rewriting and the chronological impossibility the ancients noticed: covered (book 4 handed to deep dive 12.4 explicitly)
- The state in Aristotle, Politics 2.11, and Polybius 6.51: covered
- Suffetes, council and assembly: covered
- Magonids and Barcids: covered (Barcids handed to 4.2 and 4.3 explicitly)
- Empire in Africa, Sardinia, Spain and western Sicily: covered
- Baal Hammon, Tanit, Melqart: covered
- Tophet from Diodorus 20.14 to Salammbô and the modern argument: covered
- Treaties in Polybius 3.22–26: covered
- Mago, Hanno's Periplus, the Punic of the Poenulus: covered
- Punica fides: covered

## Findings
1. [should-fix] [register] Section "Self-test".
   Current: "The earliest pottery and the Chapelle Cintas belong to the mid-eighth century"
   Problem: The body was corrected in the unit 4 pass to put the Chapelle Cintas "in the second half of the eighth century"; model answer 1 still carries the old, tighter date, so answer and body disagree.
   Fix: "The earliest pottery belongs to the mid-eighth century and the Chapelle Cintas to its second half"
   Basis: the report's section "Qart-hadasht: the date of the foundation"; review_notes in provenance.json (Chapelle Cintas date loosened in the unit 4 pass).

2. [should-fix] [lane] Section "The treaties with Rome" (dispute box).
   Current: "Diodorus (16.69.1) calls the treaty of 348 the first, and Mommsen accordingly redated Polybius' first treaty; most now, Walbank and Cornell among them, accept a date near 509, which the Pyrgi tablets make plausible. Livy (9.43.26) records a renewal "for the third time" in 306 that Polybius omits, and some identify it with Philinus' treaty; Servius, on Dido's curse at <em>Aeneid</em> 4.628, knew a treaty keeping each people off the other's shores."
   Problem: The first sentence repeats module 1.6's dispute box on the same question (Diodorus 16.69, Mommsen, Cornell for 509, the Pyrgi tablets beside it); the Servius clause repeats module 4.2's war-guilt box, where it does its work as evidence for Philinus. One home for each, with pointers.
   Fix: "Diodorus (16.69.1) calls the treaty of 348 the first; module 1.6 sets out why most, Walbank and Cornell among them, keep Polybius' date near 509. Livy (9.43.26) records a renewal "for the third time" in 306 that Polybius omits, and some identify it with the treaty Philinus cited (module 4.2)."
   Basis: rome/r-1.6.html, "The first treaty with Carthage" and its dispute box; rome/r-4.2.html, second dispute box under "Messana, 264: a hesitant Senate and a people that voted"; crosscheck pre-run, section 2 (1.6 ~ 4.1, 4.1 ~ 4.2).

3. [minor] [accuracy] Section "The treaties with Rome" (table).
   Current: "consuls Brutus and Horatius, 28 years before Xerxes crossed to Greece: 509/8"
   Problem: Twenty-eight years before Xerxes' crossing of 480 is 508/7, which is how module 1.6 converts the same synchronism; 509 is the Varronian year of the first consuls. The course now gives two conversions of one date (0.1 also has 509/8).
   Fix: "consuls Brutus and Horatius, 28 years before Xerxes crossed to Greece: 508/7 (509 in Varro's reckoning)"
   Basis: Polybius 3.22.1–2; rome/r-1.6.html ("508/7"); rome/r-0.1.html ("509/8").

4. [minor] [accuracy] Section "Gods and the tophet".
   Current: "in 1975–79, Lawrence Stager's team"
   Problem: The ASOR Punic Project began in 1975, but Stager's excavation of the tophet ran from 1976 to 1979.
   Fix: "in 1976–79, Lawrence Stager's team"
   Basis: L. E. Stager, Byvanck Lecture 2014: "In 1976 we began excavations in the Tophet of Carthage"; its bibliography lists "The Stager Excavations (1976-1979)" (https://www.babesch.org/new_site/wp-content/uploads/2023/01/BABESCH_Byvanck_Lecture_2014_Stager.pdf).

5. [minor] [style] Section "Punica fides: the Roman stereotype".
   Current: "Cicero (<em>On the Agrarian Law</em> 2.95)"
   Problem: AGENT-SPEC puts Cicero's speeches under Latin titles, and the speeches against Rullus are speeches, not invectives. The English title is used the same way in 2.3, 3.4, 5.1, 5.2 and 5.3, so this is a course-wide call for the maintainer.
   Fix: "Cicero (<em>De lege agraria</em> 2.95)"
   Basis: AGENT-SPEC.md, Rome citation conventions; grep of rome/*.html (six reports use "On the Agrarian Law").

6. [minor] [register] Section "Self-test".
   Current: "Two "kings" (the suffetes), a council of elders"
   Problem: Aristotle does not say how many kings there were; the pair comes from the Punic and Latin evidence the body cites, so the answer credits Aristotle with more than he says.
   Fix: ""Kings" (the suffetes, a pair in Punic and Latin evidence), a council of elders"
   Basis: Aristotle, Politics 2.11, 1272b37–1273a6; the report's section "The Carthaginian state".

7. [minor] [lane] Section "Self-test".
   Current: "What did the first two treaties in Polybius protect for each side, and what was Philinus' claim?"
   Problem: Module 4.2's second question tests Philinus' claim; the third treaty, which only this module covers, goes untested.
   Fix: question: "What did the first two treaties in Polybius protect for each side, and what did the third add?"; in the answer replace "Philinus claimed a treaty barred Romans from Sicily and Carthaginians from Italy, which Polybius denied existed (3.26)." with "The third, at Pyrrhus' invasion, confirmed the earlier terms, let each side help the other against him and had Carthage supply the ships (3.25)."
   Basis: rome/r-4.2.html, self-test question 2; Polybius 3.25.

## Confirmed
- Smith, Avishai, Greene and Stager 2011 (Antiquity 85, 859–874): most infants died at about one to one and a half months; Stager 2014 gives 67 percent in the one-to-two-month cohort, so "cluster at one to two months" stands (https://www.cambridge.org/core/product/7F572DE957BE72A634867AC52E6BD2E8; Byvanck Lecture above).
- Docter, Chelbi, Maraoui Telmini and others 2008, in Sagona (ed.), Beyond the Homeland (ANES Suppl. 28) 379–422: dates from the lowest Bir Massouda layer fall in the last quarter of the ninth century into the early eighth (https://research.rug.nl/en/publications/new-radiocarbon-dates-from-carthage-bridging-the-gap-between-hist/; summary in https://open.rstfen.cnr.it/index.php/rsf/article/download/26/5/143).
- Jerome, Against Jovinian 1.43: Dido chose to burn rather than marry again (https://bkv.unifr.ch/works/ccel2061/versions/against-jovinianus/divisions/45).
- Appian, Punica 1: Carthage founded fifty years before Troy's capture (https://www.livius.org/sources/content/appian/appian-the-punic-wars/appian-the-punic-wars-1/).
- Pointers true: 1.3 (Timaeus' synchronism of Rome and Carthage), 4.2 (the crossing), 4.2 and 4.3 (Barcids), 4.4 (149); deep dive 12.4's prompt matches the hand-off of book 4, and its claim that 4.1 covers Timaeus, Trogus, Naevius and Varro's Anna and the chronological objections is true; 12.2's prompt pointer (Venus' account, sources traced in 4.1) is true.
- Checked from the texts as known, no search needed: Dionysius 1.74.1; Josephus, Against Apion 1.125–126 (143 years and eight months); Justin 18.4–6 and 18.6.9 (72 years); Velleius 1.2.3; Strabo 3.5.5; Macrobius, Saturnalia 5.17.5–6; Servius on Aeneid 1.340, 4.628, 4.682; Aristotle, Politics 2.11; Polybius 3.22–26, 6.51, 6.56, 3.28.2; Livy 9.43.26, 21.4.9, 33.46–47; Herodotus 1.166, 7.165–167; Thucydides 6.2.6; Arrian, Anabasis 2.24.5; Diodorus 20.14.4–6; Plutarch, On Superstition 13; Tertullian, Apology 9.2; Pliny 2.169, 6.200, 18.22; Varro, On Agriculture 1.1.10; Columella 1.1.13; Sallust, Jugurtha 108.3; Odyssey 14.288–289; Eissfeldt 1935; Moscati 1987; Schwartz and others 2010; Xella, Quinn and others 2013; Germain 1957; Prag 2006; Quinn 2018.
- Not checked online (text sites refused in this session), consistent with the standard texts: Pliny 16.216 (Utica's beams, 1,178 years) and 18.35; Diodorus 5.16 (Ebusus, 160 years); Justin 19.1–2; Plautus, Poenulus 930–949 and 113; Stager's 20,000 urns for 400–200 (Stager and Wolff, BAR 1984).
