# Rome 0.2: Italy and the Mediterranean: the shape of Rome's world

Verdict: fix
Body words: 2759 (target 2500)

## Coverage
- Site of Rome: Tiber Island crossing: covered
- Site of Rome: salt route of the Via Salaria: covered
- Site of Rome: the hills and what seven meant: covered
- Site of Rome: marshy Forum valley and its drainage: covered
- Site of Rome: Campus Martius: covered
- Latium and the Alban Hills: covered
- Regions and peoples (Etruria, Umbria, Sabine country, Samnium, Campania, Apulia, Lucania, Bruttium, Cisalpine Gaul and the Po) and the Apennine spine: covered
- Why Italy, unlike Greece, could be unified by land: covered
- Islands (Sicily, Sardinia, Corsica) and the sea lanes to Carthage and Greece: covered
- Roads (Appia, Flaminia, Aemilia, Egnatia): covered
- Mare nostrum, provinces in outline, frontiers on the Rhine, Danube and Euphrates: covered
- Myths pinned to places (Palatine and Lupercal, Capitol and Tarpeian Rock, Aventine, Lavinium, Alba Longa, Lake Nemi, Cumae and the Sibyl, Lake Regillus): covered
- Text mental map: covered
- Pointer back to Greek module 0.2: covered

## Findings
1. [error] [figure] Section "The shape of Italy: a mental map".
   Current: "with Carthage 140 kilometres from its western cape"
   Problem: About 140 to 145 km is the width of the Sicilian Channel from Lilybaeum to Cape Bon, as the report itself says under "The islands and the sea lanes" ("about 140 from Cape Bon"). Carthage lies a little over 200 km from Lilybaeum.
   Fix: "with Cape Bon in Africa 140 kilometres from its western cape"
   Basis: great-circle arithmetic from coordinates (Marsala 37.80 N, 12.43 E; Cape Bon 37.08 N, 11.05 E, about 145 km; Carthage 36.85 N, 10.32 E, about 213 km); the report's own later figure.

2. [error] [attribution] Section "Self-test" (question 10).
   Current: "with Castor and Pollux fighting on its side (Livy 2.19–20)"
   Problem: Livy gives the battle and the dictator's vow of a temple to Castor (2.20.12), but not the twins fighting; the epiphany in the battle and at Juturna's spring is Dionysius 6.13, as module 1.6 makes clear ("Dionysius (6.13) adds that two horsemen of superhuman stature led the Roman charge").
   Fix: "The battle of c. 496 in which Rome beat the Latins and the Tarquins (Livy 2.19–20); in Dionysius (6.13) Castor and Pollux fought on its side."
   Basis: Livy 2.19–20 (Latin text); rome/r-1.6.html, "Aristodemus of Cumae, Aricia and Lake Regillus".

3. [should-fix] [pointer] Section "Myths pinned to places".
   Current: "<td>Thirteen altars and a heroon. Module 1.3</td>"
   Problem: Module 1.3 covers the heroon (Sommella's excavation, "Etruscan images and the tomb at Lavinium") but never mentions the thirteen altars, which are in module 1.1.
   Fix: "<td>Thirteen altars (module 1.1) and a heroon (module 1.3)</td>"
   Basis: rome/r-1.3.html (no "altar" anywhere); rome/r-1.1.html, "The Latins: shared cults and the League".

4. [minor] [style] Section "The islands and the sea lanes".
   Current: "For Sicily and the south as Greek worlds, point back to Greek module 0.2."
   Problem: The prompt's instruction copied into the prose; the opening section already makes the hand-off to Greek module 0.2.
   Fix: delete.
   Basis: prompt 0.2; first paragraph of the report.

5. [minor] [style] Throughout (body, tables and self-test).
   Current: "Cicero (On the Republic 2.5–11)"
   Problem: Every ancient work title in 0.2 is in roman type (On the Republic, Natural History, On the Latin Language, Georgics, Fasti, Annals, Aeneid, Res Gestae, Verrines, Gallic War, Jugurtha, Romulus, Pompey, Julius), while modern titles are italicised; 0.1, 0.3, 1.1 and the Greek quality-bar reports italicise both.
   Fix: wrap each ancient title in em, for example "Cicero (<em>On the Republic</em> 2.5–11)", "along it (<em>Natural History</em> 31.89)", "(Varro, <em>On the Latin Language</em> 5.41–54)", including the table cells and self-test answers.
   Basis: greece/r-2.1.html and rome/r-0.1.html for the convention.

6. [minor] [style] Section "Mare nostrum, the provinces and the frontiers".
   Current: "<li><strong>Augustus and after</strong>: Egypt 30"
   Problem: Egypt was annexed in 30 BC by Octavian; house style is Octavian before 27 BC.
   Fix: "<li><strong>Octavian, Augustus and after</strong>: Egypt 30"
   Basis: AGENT-SPEC.md, Rome course naming rule.

## Confirmed
- Strabo 5.3.2: Rome founded "in a place which was suitable more as a matter of necessity than of choice" (repeated 5.3.7) (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/5C*.html).
- Strabo 5.3.12: the Nemi priest a runaway slave who has killed his predecessor; Strabo 5.3.8 on the Campus Martius (same LacusCurtius page).
- Cicero, On the Republic 2.5–11: Romulus' inland site praised, safe from pirates (Latin text).
- Livy 1.33.6 (Pons Sublicius under Ancus), 1.38.6 (Priscus drains the low ground), 1.56.2 (Cloaca Maxima), 1.16.1 (Goat's Marsh), 2.5.2 (Tarquins' land to Mars) (Latin text).
- Pliny, Natural History 31.89: the Salaria named for salt carried to the Sabines (Latin text).
- Plutarch, Romulus 25: salt-works taken from Veii (Perrin text).
- Varro, On the Latin Language 6.24 (Septimontium "ab his septem montibus"); Festus, citing Antistius Labeo, lists eight places (Palatium, Velia, Fagutal, Subura, Cermalus, Oppius, Caelius, Cispius) (texts).
- Virgil, Georgics 2.535; Ovid, Fasti 6.401 ("udae tenuere paludes") (Latin text).
- Tacitus, Annals 12.24 (Romulus' pomerium), 1.9 ("mari Oceano aut amnibus longinquis saeptum"), 1.11 ("coercendi intra terminos") (Latin text).
- Pliny, Natural History 3.39 ("numine deum electa") and 3.68–70 (populi Albenses) (Latin text).
- Polybius 2.24: more than 700,000 foot and 70,000 horse in 225; Polybius 1.10–11 on Messana (text).
- Cicero, Verrines 2.2.5: Cato's "cellam penariam rei publicae" (Latin text).
- Dionysius 3.67.5: aqueducts, roads and sewers as Rome's three most magnificent works (Loeb text).
- Livy 9.29.6 (Appia, 312), 39.2.10 (Aemilia, Placentia to Ariminum, 187); Diodorus 20.36 (Appius spends the revenues) (texts).
- Via Flaminia 220 under Flaminius as censor; Egnatius milestone found near Thessalonica; Strabo 7.7.4 on the Egnatia from Polybius (standard).
- Colony dates: Cales 334, Venusia 291, Ariminum 268, Brundisium 244, Paestum 273, Placentia and Cremona 218; Sabines full citizens 268 (standard; Velleius 1.14).
- Province dates as listed (Sicily 241, Sardinia and Corsica 238, Spains 197, Asia 133, Cilicia c. 102, Bithynia and Cyrene 74, Crete 67, Syria 64, Transalpina c. 121) (standard).
- Gellius 13.14: Aventine outside the pomerium because of Remus' unfavourable birds, until Claudius (Latin text).
- Livy 1.55.5–6 (head on the Capitol), 5.47 (geese), 6.20.12 (Manlius from the Rock), 2.42.5 (temple of Castor dedicated 484); Dionysius 6.13 (twins at Juturna's spring); Dionysius 4.62 (Sibylline Books) (texts).
- Res Gestae 19 (Lupercal) and 26 (Elbe) (Latin text).
- Distances: Strait of Messina about 3 km; Strait of Otranto about 72 km; Alban Hills about 20 km south-east of Rome (maps).
- Ammerman, "On the Origins of the Forum Romanum", AJA 94 (1990); Hopkins, The Genesis of Roman Architecture (Yale, 2016); Harris 1979; Luttwak 1976; Isaac 1990; Whittaker 1994; Mattern 1999; Maiuri's excavation of 1932; Frazer 1890.
- Pointers true of their targets: Greek module 0.2 (the West; the polis and geography), modules 1.1 (cults and league), 1.2, 1.4 (Lupercal; Ennius' augury), 1.6 (Carthage treaty; Lake Regillus).
- Incoming pointers true of 0.2: from 3.4 (roads; geographical half of unification), 4.4 (provinces in outline), 6.4 (frontier quarrel).
