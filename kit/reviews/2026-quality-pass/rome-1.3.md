# Rome 1.3: Before Romulus: Evander, Hercules and Aeneas

Verdict: fix
Body words: 2695 (target 2500)

## Coverage
- Hellanicus as Dionysius 1.72 reports him; Damastes: covered
- the Aristotelian Achaeans and the burnt ships: covered
- Heraclides Ponticus' "Greek city": covered
- Callias; Timaeus and the Lavinium relics: covered
- rival Greek founders (Rhomos, sons of Odysseus and Circe, Latinus in Theogony 1011–1016): covered
- Saturn and the Golden Age, Janus, Picus, Faunus: covered
- Evander on the Palatine, Hercules and Cacus, the Ara Maxima: covered
- Aeneas in Greek tradition (Iliad 20.307–308, Hymn to Aphrodite): covered
- Etruscan vases and Veii statuettes: covered (statuette date overstated, finding 1)
- the Lavinium heroon: covered
- the Roman version in Fabius, Naevius, Ennius, Cato and Varro (landing, Latinus and Lavinia, Turnus and Mezentius, Lavinium, Ascanius and Alba): covered
- the Alban king list: covered
- why a Trojan ancestor: covered
- diplomacy: Segesta, Ilium, Acarnanians, Flamininus at Delphi, Pyrrhus: covered
- the Julii through Iulus: covered
- pointers to Greek 7.3 and 10.12; Aeneid left to unit 12: covered (7.3 pointer overstated, finding 2)

## Findings
1. [error] [accuracy] Section "Etruscan images and the tomb at Lavinium".
   Current: "Alföldi and Galinsky dated the Veii statuettes around 500, the date behind the "sixth-century" statuettes of Greek module 7.3; later study puts them in the fourth century, after Rome took Veii in 396, which reverses the inference."
   Problem: The date is still disputed, so "later study puts them in the fourth century" is too firm. Proposals run from the sixth to the first century BC: Haynes puts them after 396, while Martinelli and Paolucci (2006) argue for the early fifth century, and the 2023 Colosseum exhibition labelled a Veii statuette fifth-century. Galinsky's dating could not be confirmed. As a result, the correction logged for Greek 7.3 in provenance.json review_notes ("fourth century") should not be applied as worded. Greek 7.3's "sixth-century" should become "of disputed date".
   Fix: "The Veii statuettes were once dated about 500, the date behind the "sixth-century" statuettes of Greek module 7.3, but their date is disputed: Martinelli and Paolucci (2006) put them early in the fifth century, Sybille Haynes (2000) after Rome took Veii in 396, which would reverse the inference."
   Basis: P. Mountford, "Aeneas: an Etruscan foundation legend", ASCS 32 proceedings (https://www.ascs.org.au/news/ascs32/Mountford.pdf): "Suggested dates range from the sixth to the first century B.C."; Haynes for after 396; Martinelli and Paolucci for the early fifth century. Parco archeologico del Colosseo, Il viaggio di Enea (2023), caption "Da Veio. V sec. a.C." (https://colosseo.it/sito/wp-content/uploads/2023/01/Mostra_Il-Viaggio-Di-Enea.pdf). Galinsky's view on the date: not checked (book not online).
2. [should-fix] [pointer] Section "The claim at work: diplomacy and the Julii".
   Current: "Greek module 7.3 sets the kinship diplomacy in the conquest of the East"
   Problem: Greek 7.3 narrates the conquest of the East but gives the kinship diplomacy a single sentence (Erskine on Greek cities exploiting the kinship, in "Captive Greece: the reverse conquest"). It has nothing on Ilium, Lampsacus or Flamininus' Delphic dedication.
   Fix: "Greek module 7.3 narrates the conquest of the East in which the kinship was invoked"
   Basis: greece/r-7.3.html, all sections read; the only kinship sentence is the Erskine one.
3. [should-fix] [accuracy] Section "Rival founders: Rhomos, the sons of Circe, Latinus".
   Current: "Xenagoras gave the pair three sons, Rhomos, Anteias and Ardeias"
   Problem: Coming straight after Agrios and Latinos, "the pair" reads as those two brothers. Xenagoras actually makes the three sons children of Odysseus and Circe.
   Fix: "Xenagoras gave Odysseus and Circe three more sons, Rhomos, Anteias and Ardeias"
   Basis: Dionysius, Roman Antiquities 1.72.5.
4. [minor] [style] Sections "Saturn, Janus, Picus and Faunus", "Etruscan images and the tomb at Lavinium", "The Roman version: Fabius Pictor to Varro".
   Current: "<em>De lingua Latina</em>" (four times) and "<em>Res rusticae</em> 2.4.18"
   Problem: Most of the course (0.1, 0.2, 0.3, 1.1, 2.1, 2.2, 2.4, 2.5) writes On the Latin Language and On Agriculture. AGENT-SPEC fixes only Cicero's titles, so this is a consistency point, not a rule.
   Fix: "<em>On the Latin Language</em>" in all four places; "<em>On Agriculture</em> 2.4.18"
   Basis: grep of rome/*.html (14 uses of On the Latin Language against 12 of De lingua Latina, the latter in 1.3, 1.5, 2.3, 3.1 and 3.5).

## Confirmed
- Dionysius 1.72–73 catalogue: Hellanicus ("with Odysseus", Rhome, the burnt ships) and Damastes 1.72.2; Aristotle's Achaeans at "Latinion" 1.72.3–4; Callias 1.72.5.
- Heraclides Ponticus in Plutarch, Camillus 22.2. Kept overlap with 3.3: still near-verbatim (13 shared seven-word runs). In 1.3 it is a bullet among Greek founders and in 3.3 a sentence among outside witnesses, so it reads as a deliberate echo, not a duplicate box; no change.
- Timaeus: 814/3 with Carthage, Dionysius 1.74.1; October Horse mocked, Polybius 12.4b–c; Lavinium heralds' staffs and Trojan pottery, Dionysius 1.67.4.
- Solmsen, "Aeneas founded Rome with Odysseus", HSCP 90 (1986).
- Theogony 1011–1016 (Agrios and Latinos; Tyrsenians); Plutarch, Romulus 2.1 (Rhomanos; Rhomos sent by Diomedes); Livy 1.49.9 (Mamilius from Ulysses and Circe); Hyginus, Fabulae 127 (Telemachus and Circe parents of Latinus); Dionysius 1.43 and Justin 43.1 (Hercules).
- Ovid, Fasti 1.238, 1.90, 1.229–240; Justin 43.1.3; Varro 5.42 and 5.64; Macrobius, Saturnalia 1.7.19–24; Aeneid 7.45–49; Dionysius 1.31.2.
- Evander sixty years before the war, Dionysius 1.31.1; Palatium and the Lupercalia, Livy 1.5.1–2; letters, 1.7.8; Victory and Ceres, Dionysius 1.32–33; "more than twelve centuries" is right on that date.
- Cacus: Livy 1.7.4–11, Dionysius 1.39–42, Aeneid 8.185–275, Propertius 4.9, Diodorus 4.21.2 (Cacius and Pinarius); Bolsena mirror with Cacu and the Vibennae.
- Ara Maxima: Livy 1.7.3 (quotation exact), 1.7.12–15; Plutarch, Roman Questions 18 and 60; Potitii and Appius Claudius 312, Livy 9.29.9–11; Bayet (1926) against van Berchem (Melqart).
- Iliad 20.307–308; Strabo 13.1.53 on the "over all" reading; Hymn to Aphrodite 196–199; Iliou Persis in Proclus; Aineia coins; Thucydides 6.2.3; Menecrates, Dionysius 1.48.3.
- Tabula Iliaca "after Stesichorus", Aeneas "departing for Hesperia"; Galinsky (1969) against Horsfall, "Stesichorus at Bovillae?" (JHS 1979).
- Attic vases of Aeneas and Anchises: Schauenburg's 58, earliest about 520; of those with provenance, most from southern Etruria (Mountford, above).
- Heroon: Dionysius 1.64.4–5; Livy 1.2.6 (Jupiter Indiges); Penates at Lavinium, Varro 5.144; consuls' sacrifice, Macrobius 3.4.11; yearly treaty with the Laurentes, Livy 8.11.15; sow and piglets, Varro, On Agriculture 2.4.18.
- Tauromenium catalogue of Fabius; Cicero, On Divination 1.43; Servius on Aeneid 1.273 (Naevius and Ennius: Romulus Aeneas' grandson through a daughter).
- Cato: Mezentius and the Vinalia, Macrobius 3.5.10; Aborigines Greek, Dionysius 1.11.1; 432 years, 1.74.2.
- Livy's Alban list 1.3.6–10 exact; Dionysius 1.70–71; Allodius and the thunder 1.71.3; Silvius and Iulus 1.70.3–4.
- Gruen, Culture and Identity in Republican Rome (1992); Erskine, Troy between Greece and Rome (2001); Dionysius 1.61–62, 1.89.1.
- Diplomacy table: Pausanias 1.12.1; Zonaras 8.9 and Verrines 2.4.72; Justin 28.1–2; Suetonius, Claudius 25.3; Livy 22.9–10 and 23.31; 29.12.14; Plutarch, Flamininus 12; Livy 37.37.1–3; 38.39.10; Holleaux (1921).
- Julii: Tacitus, Annals 11.24; Livy 1.3.2 (quotation exact); Bovillae altar "by Alban law"; Suetonius, Julius 6.1; denarius of 47–46.
- Greek 10.12 pointers true: it covers Naevius and Ennius as poets, Venus Genetrix and the lusus Troiae.
- Source-date rule met throughout (two centuries before Roman history; seven centuries for Hellanicus; five for Homer; twelve for Evander; nearly a thousand for the Roman writers).
