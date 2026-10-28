# Rome 10.3: Reading Roman art and architecture

Verdict: fix
Body words: 2833 (target 2500)

## Coverage
- Etruscan and Greek inheritance: covered (Vitruvius 4.7, Varro in Pliny 35.154, Portunus, round temple; points back to module 1.2 and Greek module 9.1)
- Republican portrait and verism: covered (dispute box with names on both sides)
- Ancestor masks: covered by pointer to module 2.4, and used in the verism box
- Barberini Togatus: covered
- Copies of Greek sculpture and what "Roman copy" means: covered (Mummius, Cicero's letters, Pasiteles and Stephanus, Farnese Hercules and Bull; Kopienkritik and the Ridgway/Marvin dispute left to Greek module 9.1)
- Historical relief, Ara Pacis to Arch of Titus: covered
- Spiral friezes of Trajan and Marcus: covered
- Four Pompeian styles: covered
- Villa of the Mysteries: covered (Maiuri against Veyne)
- Mosaic: covered
- Concrete, arch and vault: covered
- Temple on a podium, basilica, bath, amphitheatre: covered (short bullets, enough for the brief)
- Pantheon's dome: covered
- Imperial portrait as propaganda; erasure of the condemned: covered (Flower's memory sanctions; Geta handed to module 7.4)
- Sarcophagi and myth in funerary art: covered (Cumont, Nock, Zanker and Ewald)
- Late antique style (Tetrarchs, Arch of Constantine) as change, not decline: covered
- Point back to Greek module 9.1: done three times, each true of the target
- Lane hand-offs: all kept. 2.4 (masks, Flower) pointed to, not retold; 6.2 sundial box not repeated, Ara Pacis read for relief technique only; 7.1 Golden House painting taken (Famulus, grotesque); 7.2 Arch of Titus and 7.3 columns read as art; Pantheon taken as a building without retelling Hetland; 7.4 Arch of Severus relief and Farnese Bull taken, tondo left to 7.4; 8.2 Tetrarchs, 8.3 Arch of Constantine and 8.6 Hagia Sophia given the late antique frame. One breach found: the Capitoline Wolf (finding 1).

## Findings
1. [should-fix] [lane] Section "The inheritance: an Etruscan plan and a Greek grammar".
   Current: "<aside class="dispute"><strong>Where sources disagree.</strong> Since Winckelmann the bronze Capitoline Wolf has been dated on style to the fifth century BC. Anna Maria Carruba, who restored it, argued in 2006 that its single-pour casting is a medieval technique, and radiocarbon dating of its core in 2007 pointed to the eleventh or twelfth century AD.</aside>"
   Problem: Module 1.4 already tells this in full (Winckelmann's Etruscan dating, Carruba's restoration and single-pour argument, 2006, the Salento radiocarbon date of 1021 to 1153). It appears in a paragraph and a table there, not a dispute box, so crosscheck.py did not flag it. The facts are right, but the box repeats a neighbour's material.
   Fix: "<p>The bronze Capitoline Wolf, long the textbook Etruscan casting, warns against dating on style alone: module 1.4 gives the case for the eleventh or twelfth century AD.</p>"
   Basis: rome/r-1.4.html line 44 and the table at line 40; facts confirmed at https://en.wikipedia.org/wiki/Capitoline_Wolf (Winckelmann's fifth-century attribution; Carruba from 1997; radiocarbon at Salento, February 2007, 1021 to 1153).

2. [error] [accuracy] Section "The inheritance: an Etruscan plan and a Greek grammar".
   Current: "Rome added the plain Tuscan column and the Composite capital, Ionic volutes over Corinthian acanthus, first seen on the Arch of Titus."
   Problem: The Arch of Titus (AD 81 to 82) is the first prominent surviving use of the Composite capital, not its first appearance. The capital was developed by Augustus' reign. The writer gave this claim from memory.
   Fix: "Rome added the plain Tuscan column and the Composite capital, Ionic volutes over Corinthian acanthus, whose earliest prominent surviving use is on the Arch of Titus."
   Basis: EPFL Graph Search summary of the Composite order article (https://graphsearch.epfl.ch/fr/concept/2706622): the arch is the "first prominent surviving example"; the order was "probably developed a little before Augustus's reign, and certainly well-developed before his death".

3. [error] [accuracy] Section "Concrete, arch and dome".
   Current: "<li><strong>The amphitheatre</strong>, an oval of seats on radial vaults, from Pompeii's to the Colosseum (modules 7.2 and 9.4).</li>"
   Problem: Pompeii's amphitheatre (about 70 BC) has no radial vaults. Its seats rest on earth dug from the arena and banked against the town walls. The contrast between the two buildings is the actual architectural point.
   Fix: "<li><strong>The amphitheatre</strong>, an oval of seats, banked on earth at Pompeii and carried on radial vaults in the Colosseum (modules 7.2 and 9.4).</li>"
   Basis: Encyclopaedia Romana, "Amphitheatrum" (https://penelope.uchicago.edu/~grout/encyclopaedia_Romana/gladiators/amphitheatrum.html): "The soil excavated for the arena was banked to form the seating, stabilized on the south and east by the town walls."

4. [should-fix] [accuracy] Section "Concrete, arch and dome".
   Current: "symmetrical round a vaulted hall from Trajan's baths onward"
   Problem: The writer meant Trajan's baths as the first symmetrical imperial plan (writer's list, from memory). Nero's baths of about AD 62 are usually taken as the first axial, symmetrical imperial bath, and Titus' baths were symmetrical too. Trajan's baths made the type monumental.
   Fix: "symmetrical round a vaulted hall, probably from Nero's baths and at full scale from Trajan's"
   Basis: https://en.wikipedia.org/wiki/Baths_of_Nero: "probably the first 'imperial-type' complex of baths, with a monumental scale and symmetrical, axially-planned design".

5. [should-fix] [attribution] Section "Self-test", question 3.
   Current: "and colossal versions such as the Farnese Bull (Pliny 36.34)"
   Problem: Pliny 36.34 describes the Rhodian group by Apollonius and Tauriscus in Pollio's collection, not the Farnese Bull. The body is careful ("usually taken as a version of the group"). The answer drops that hedge and cites Pliny as if he attested the Farnese marble.
   Fix: "and colossal versions such as the Farnese Bull, usually taken as a version of the group Pliny saw in Pollio's collection (36.34)"
   Basis: Pliny, Natural History 36.34; the report's own body text in "Greek statues in Roman settings".

6. [minor] [register] Section "The republican portrait: verism and the ancestors".
   Current: "Chronology tells against the masks, which are older than the style."
   Problem: As worded, the argument fails, because a source is always older than what derives from it. The point is that the masks were displayed for generations before verism appeared, so they cannot explain why it appeared when it did. The sentence also passes an unattributed verdict on a dispute that is still open: the Greece & Rome article of 1987 that the writer used argues that the masks' influence is underrated.
   Fix: "Chronology is the difficulty: the masks were displayed for generations before the style appears, so they cannot by themselves explain why it arose in the first century BC."
   Basis: "Verism and the Ancestral Portrait", Greece & Rome 34 (1987), Cambridge Core page and notes (https://core-cms.cambridgecore.org/core/journals/greece-and-rome/article/verism-and-the-ancestral-portrait/DE25D7923FD3A0B21D33EB392CA26F14).

7. [minor] [accuracy] Section "The inheritance: an Etruscan plan and a Greek grammar".
   Current: "an antiquarian's claim, made five centuries later"
   Problem: Varro wrote in the mid first century BC, about 450 years after the traditional date of 493. The spec asks how many centuries separate event and source, so the gap should be stated closely.
   Fix: "an antiquarian's claim, made some four and a half centuries later"
   Basis: Varro 116 to 27 BC; temple of Ceres dedicated 493 BC (Dionysius, Roman Antiquities 6.94).

## Confirmed
- Every cross-reference resolves to a written report that says what the pointer claims: 1.2 (temple form, Vitruvius 4.7); Greek 9.1 (orders, sculpture, Parthenon frieze as procession, Roman marbles of lost bronzes); 9.3 (freedmen's reliefs of a couple's busts); 2.4 (masks, Flower; the turn from burning to burial); 4.3 (Marcellus, Syracusan art, Livy 25.40); 4.4 (Paullus' triumph with statues and paintings); 5.3 (Verres stripping temples); 6.2 (Ara Pacis figures, Mars Ultor, the Augustan type unchanged from about 27 BC); 7.1 (Golden House); 7.2 (Arch of Titus, Colosseum); 7.3 (columns, Pantheon begun under Trajan); 9.2 (Coulston on the Column as evidence); 9.4 (baths, Colosseum); 7.4 (Arch of Severus, Farnese Bull and Hercules, Geta); 8.2 (Tetrarchs); 8.3 (Arch of Constantine); 8.6 (Hagia Sophia)
- No shared passages and no duplicated dispute boxes with any report (crosscheck.py); the sundial and Ara Pacis identity boxes of 6.2 are not repeated
- Cicero, Letters to Atticus 1.8, 1.9 and 1.10 all ask for statues suited to a gymnasium (also 1.6): https://topostext.org/work/785
- Letters to Friends 7.23 to M. Fadius Gallus: Bacchants and a Mars (known text)
- Velleius 1.13.4 (Mummius and the contractors); 1.11.5 (Metellus' first marble temple) (known text)
- Pliny, Natural History 35.22 to 23 (Messalla 263 BC; Mancinus), 35.110 (Philoxenus for Cassander), 35.120 (Famulus), 35.154 (Varro on Damophilus and Gorgasus), 36.34 (Dirce group in Pollio's collection), 36.39 (Pasiteles' five books), 36.184 (Sosus), 36.189 (Sulla's pavement at Praeneste; glass mosaic on vaults) (known text)
- Capitoline Wolf facts as stated (Winckelmann's fifth-century date, Carruba 2006, radiocarbon 2007, 1021 to 1153): Wikipedia, Capitoline Wolf
- Verism box sources: Zadoks-Josephus Jitta 1932 as the earliest full exposition of the mask theory, Drerup 1980 restating it, Richter JRS 1955 and Smith JRS 1981 for Greek sources (Greece & Rome 1987 notes, Cambridge Core)
- Penelope Davies, "The Politics of Perpetuation: Trajan's Column and the Art of Commemoration", AJA 1997, 41 to 65 (Perseus JSTOR index)
- Veyne, "Conduct without belief and works of art without viewers", Diogenes 1988; Veyne, Lissarrague and Frontisi-Ducroux, Les mystères du gynécée, 1998; Maiuri, La Villa dei Misteri, 1931
- Davies, Hemsoll and Wilson Jones, Art History 10.2 (1987), on the 50-foot and 40-foot shafts; Dio 53.27.2 and 69.7.1; sixteen granite columns; five rings of 28 coffers; span equal to height
- Mau 1882; Vitruvius 7.5.1 to 4 and 7.5.3 to 4 on reeds and monsters; Vitruvius 2.6.1 on Puteolan dust; Vitruvius 4.7 on the Tuscan temple
- Tabularium 78 BC; Basilica Porcia 184 BC (Livy 39.44.7); Santa Maria degli Angeli in Diocletian's baths
- Historia Augusta, Hadrian 26.1; Eusebius, Life of Constantine 4.15; Suetonius, Domitian 23.1; Pliny, Panegyricus 52.4 to 5; Cancelleria frieze A recut from Domitian to Nerva; Flower, The Art of Forgetting, 2006, and damnatio memoriae as an early modern term
- Cumont 1942; Nock, "Sarcophagi and Symbolism", AJA 1946; Zanker and Ewald, Mit Mythen leben, 2004; Great Ludovisi about 250 to 260 in Palazzo Altemps; Junius Bassus 359
- Berenson, The Arch of Constantine, or the Decline of Form (English ed. 1954); Riegl, Spätrömische Kunstindustrie 1901; Bianchi Bandinelli's arte plebea; Elsner, PBSR 2000; Wickhoff in Die Wiener Genesis, 1895
- Barberini Togatus: late first century BC, head ancient but not original (Centrale Montemartini; writer checked)
- House style: British spelling, no em dashes, Augustus used only for after 27 BC, length within band (2833 against a ceiling of 2875; the fixes above shorten it slightly)
