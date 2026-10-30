# P43 Greece · notes from the figure checkers (30 October 2026)

Backlog row N5 added figures to the 78 Greek reports. Its checkers and re-checkers (fresh Opus 5.5 agents, one per report and stage) were told to note anything wrong outside the figures and not to fix it. Nothing below was changed: the prose of every report is byte-identical to before N5 and no word count moved. The prose leads are copied from the agents' notes as they wrote them, the checker's first and the re-checker's after (marked "(re-check)"), so a slip both saw appears twice. They are leads for a corrections pass (proposed row P59), not verified errors: each wants checking against the report and its sources before an edit. The drawing faults are summarised first; they go to proposed row P58.

## Drawing faults the checkers met in `viz.py`

None stops the build and none made a figure wrong; each makes a figure read worse. Every one was met on a figure drawn with the P55 renderer.

- **range, a row whose low equals its high** prints its single value two or three times: once above the diamond when a point is given, and once under each end with its source tag (1.1 and 1.2 "1400 BC" twice, 5.1 "850 BC" twice, 6.1 "1,700,000 men" three times, 8.5 "400,000" twice, 9.4 three values three times each, 10.10 "1250 BC" twice). In 1.2 the end label is also drawn offset outward from the bar end, so it does not sit under the value it names. A zero-width row should print its value once, with one source tag, or be drawn as a point.
- **timeline, wrapping an event label** breaks between "c." and its year, leaving "c." at the end of a line and the number alone on the next (5.1 "c. 670", 7.1 "(c. 185)", 7.2 "c. 145", 9.1 "c. 600", "c. 750", "c. 530", 10.2 "c. 1180", 12.4 "(from c. 345)", "(c. 341)"). The wrap should keep "c." with the number after it.
- **timeline, the event's date line** prints a bare first year: "476/5" is tagged "476 BC", "c. 500, or after 490" and "c. 450" lose their "c." (3.3, 3.7, 10.2; Rome 1.6's checker saw the same). So the date reads more exact than the text, and where the label repeats the date to keep the "c." every event shows its date twice. The date line also writes "BC"/"AD" while 3.1 writes BCE/CE throughout, so that figure mixes the two notations. An event field for an approximate or split year, or a label with no date line, would fix both.
- **objects, a link label in a narrow gap** is wrapped mid-word ("prepare" / "s" / "busines" / "s" in 5.4, "conced" / "es" in 10.9). P55's rule that a label is never cut is not applied to objects link labels; the renderer should widen the gap or move the label. 5.4's checker rearranged the boxes so the link runs vertically; 10.9's broken label ran out of the drawing and failed `verify.py`, so this chat rearranged its grid the same way (each pairing a column, the links vertical; no label, box or link changed).
- **range, a word unit** is printed after every value without number agreement ("1 heads", 2.6; fixed in the data by moving the unit into the title).
- **tree, a one-child chain** is drawn hard against the left edge of the 700-unit drawing with the rest empty (8.1; that figure was dropped for its content).

## A lesson for the figure pass

Both of 9.4's figures were dropped: 9.4 is a closed-book exam, and each figure drew a model answer hidden in a Self-test `<details>`, which a figure cannot sit inside, so it would have shown the answer under the question. §4b says nothing about exams or hidden answers; proposed row P60 adds one line.

## Prose and Self-test leads, by report

### 0.1

- Self-test 1, answer: "Simply \"speech\" or \"utterance\"". The body (first paragraph) gives only "utterance"; "speech" is not stated there.
- Self-test 8, answer: "the tablets show his name in Greece c. 1200 BC". The body dates Pylos c. 1200 BC but gives no date for the Khania tablet, which the answer names alongside Pylos.
- (re-check) "Material sources", Linear B paragraph: "show the core Olympian names at least five centuries older than Homer". With Pylos at "c. 1200 BC" and Homer "conventionally placed around 750–700 BC", the gap is 450–500 years; only Knossos (c. 1400–1370 BC) clears five centuries. Figure 1's caption repeats the claim, and the figure's own dates show the tension. Consider "some five centuries" or naming Knossos.
- (re-check) Self-test 6 answer: "It is now dated to the first or second century AD." The body says "Most scholars date it to the first or second century AD"; the answer drops the hedge.
- (re-check) Self-test 1 answer: "Simply \"speech\" or \"utterance\"." The body gives only "utterance"; "speech" is not stated there (harmless, but beyond the body).
- (re-check) Transliteration is mixed: Greek-style "Sophilos", "Kleitias", "Exekias" beside Latinised "Cypselus", "Polygnotus", "Stasinus", "Uranus".
- (re-check) Work titles cited as references are unitalicised in places ("Theogony 27–28", "Theogony 278–279", "Olympian 1.28–29") but italicised elsewhere ("<em>Theogony</em> 188–206").

### 0.2

- Self-test 7, answer: "Corinthians under Archias, the year after Naxos, traditionally 733 BC". The body ("The West and the Black Sea") names no Archias and gives no 733; it says only "Naxos first (734), Syracuse a year later by Corinthians".
- Self-test 9, answer: "Pelops' race for Hippodameia". The body (Myth and place table, Olympia row) says only "Pelops' chariot race"; Hippodameia is not named.
- Self-test 2: "Name the seven traditional sub-regions of the Peloponnese." The body calls the table's seven rows "compartments" and counts seven *peoples* (Herodotus 8.73); it never calls the seven regions traditional.
- Inconsistent spelling: "the capes of Argolis" (mental-map paragraph) against "Argolid" (map block and Peloponnese table).

### 0.3

- "The anchor dates: a list to copy out", first sentence: "Fifteen dates." The table that follows has sixteen rows (c. 1450 to AD 529).
- Same paragraph: "The first two are approximate; everything from 776 is a traditional or recorded date." The fourth row, "c. 750–700 BC", is also approximate.
- "A mental map for memorising", last paragraph: "close to the 195 years that separate 1200 and the end of the Early Iron Age at 1000". 1200 to 1000 is 200 years, and the period table ends the Early Iron Age at c. 800, not 1000.
- Self-test 10, answer: "Alan Cameron argued there was no single formal "closing" of the Academy". The body (dispute note after "Hellenistic to Late Antique") says only that the question "is argued between Cameron and Watts in module 7.4"; it neither gives Cameron's first name nor says which side he takes.
- "The nine periods and their boundaries", paragraph after the table and figure ("Two boundaries deserve a note"): the Archaic start is given as 800, 776 or 750, but the table offers only "c. 800 (or 776)".
- (re-check) Heading "The nine periods and their boundaries": the table under it has ten rows (Early Bronze Age to Late Antique).
- (re-check) "Fifteen dates. The first two are approximate": the table under it has sixteen rows.
- (re-check) Same paragraph, "everything from 776 is a traditional or recorded date": the table's "c. 750–700 BC" row, after 776, is approximate.
- (re-check) A mental map, "close to the 195 years that separate 1200 and the end of the Early Iron Age at 1000": 1200 to 1000 is 200 years, and the period table ends the Early Iron Age at c. 800, not 1000.
- (re-check) Self-test 10 answer, "Alan Cameron argued there was no single formal 'closing' of the Academy": the body says only that the question "is argued between Cameron and Watts in module 7.4" and attributes no position to Cameron.

### 1.1

- Self-test 1, answer: "Platon's palatial scheme (Prepalatial, Protopalatial, Neopalatial, Postpalatial)" omits Final Palatial, which the opening table gives as one of Platon's phases.
- Self-test 2, answer: "excavated by Nikolaos Platon from 1961"; the body says only that Zakros "was found by Platon in 1961".
- Self-test 8, answer: "the restored heads and cat of the snake goddess figurines"; the body says only "the smaller figure's head, and the cat on it, are modern" (one head, not heads).
- Self-test 9, answer: "roughly six centuries before Homer"; the body gives no date for Homer (only that the myths were "reshaped between the eighth and first centuries BC").
- Self-test 10, answer: quotes "broad Knossos" (Iliad 18.590–2); the body never uses that phrase (its only Homeric epithet quoted for Knossos is "great city Knossos", in "What, if anything, do they preserve?" item 1).
- Spelling: "Eleuthia at Amnisos" (item 2 of "What, if anything, do they preserve?") against "the cave of Eileithyia" in the same item and "Eileithyia at Amnisos" in Carry forward 3. "Eleuthia" may be meant as the Linear B transliteration, but the text does not say so.
- "The palaces, and what a 'palace' was", first paragraph: a stray space before the closing tag, "the rock-crystal rhyton. </p>".

### 1.2

- Self-test 2, answer: "three to four centuries before any Trojan War horizon of c. 1250–1180 BC". The body gives no date for the Trojan War horizon ("well before any plausible Trojan War horizon"); the 1250–1180 figure is stated only in the answer.
- Self-test 4, answer: "John Chadwick's philological collaboration". The body says only that Ventris "published with John Chadwick"; "philological" is not in the body.
- Self-test 7, answer: "Textiles and flax, with women workers rationed and counted". The body puts the textile accounting at Knossos ("Knossos counted some 100,000 sheep, set wool targets ... tracked cloth through workshops; Pylos ran flax"); it does not say Pylos mainly produced textiles. The rationed women are at Pylos, but the body does not tie them to textile work.
- Self-test 8, answer: a past dispute "over Wilusa" in quotation marks. The body's quotation is "the matter of Wilusa over which we were at enmity"; "over Wilusa" is not a phrase of it.
- Inconsistent spelling: "Hector's ankles and neck (Iliad 6.117)" in "How much Homer remembers", against "Hektor" (e-ko-to) in "Religion and burial" and "Achilleus, Hektor and Alexandra" in the same section.
- (re-check) Spelling inconsistency: "Hektor" in "Religion and burial" ("<em>e-ko-to</em> (Hektor)") and in "How much Homer remembers" ("Achilleus, Hektor and Alexandra"), but "Hector" in the same section's list ("strikes Hector's ankles and neck (Iliad 6.117)").
- (re-check) Self-test 2 answer gives a date the body does not: "any Trojan War horizon of c. 1250–1180 BC". The body says only "well before any plausible Trojan War horizon" and gives no range for it.
- (re-check) Self-test 4 answer: "John Chadwick's philological collaboration". The body says only that Ventris "published with John Chadwick"; "philological" is not in the body (minor).
- (re-check) Self-test 6 answer lists Eileithyia among the "Olympian gods" in brackets ("also Ares, Dionysus, Eileithyia"); the body does not call her Olympian (minor).
- (re-check) Carry forward 1: "a four-century gap in which writing, palaces and kingship were lost". The body says writing and palaces went, but also that Homer's "Agamemnon's Mycenae is a petty kingship" and his basileus is "king"; what the body says was lost is the wanax's palace kingship, not kingship as such.
- (re-check) Cross-references "module 10.10" (twice) and "module 10.2" could not be checked from this file; if those modules do not exist in the Greece course they are dangling.

### 1.3

- "The Dark Age in the ground", first paragraph: "Early Geometric (c. 900&ndash;850)", while the table directly below has "Early and Middle Geometric | 900&ndash;760". The two periodisations differ without comment.
- "Sea Peoples": "Ekwesh as Achaeans" is given as one of the "other identifications", but Ekwesh is not among the five Medinet Habu names just listed and is not introduced anywhere (it is a Merneptah-list name). As written it dangles.
- Self-test 1, answer: "Levantine and Egyptian scripts served temples, merchants and courts that survived" (and the question's "Phoenician and Egyptian scripts survived the same crisis"). The body says nothing about other scripts surviving or what they served.
- Self-test 4, answer: "textual grain requests from Hatti and Ugarit". The body has Merneptah sending grain to Hatti and a Hittite king demanding a grain ship from Ugarit: the request was made to Ugarit, not by it.
- Self-test 6, answer: "four sacrificed horses". The body says "four horses, one with an iron bit in its mouth"; "slaughtered horses" is said only of Patroclus' funeral.
- Self-test 2, answer: "around 1180". The body gives Pylos only as "at roughly the same moment" as 1190&ndash;1180 (table: c. 1190&ndash;1180); 1180 is the end of that range, not stated as Pylos's date.
- "Where sources disagree" after Nichoria: "is argued in module 5.1": a cross-reference to another module that cannot be checked from this report.
- Self-test answers 6, 9 and 10: "Iliad 23", "Iliad 10.261&ndash;265" and "basileus" are in roman type; the body italicises <em>Iliad</em> and <em>basileus</em> throughout.
- (re-check) Self-test 1, answer: "Levantine and Egyptian scripts served temples, merchants and courts that survived." The body never says these scripts survived or whom they served; it states only that Linear B was a palace instrument.
- (re-check) Self-test 4, answer: "textual grain requests from Hatti and Ugarit". The body has Merneptah sending grain to Hatti and a Hittite king demanding a grain ship from Ugarit; Ugarit made no request. Should read "from Hatti" (to Egypt and Ugarit).
- (re-check) Self-test 5, answer: "Perati traded with Egypt and the Levant". The body says only that Perati "buried a community with Egyptian and Levantine imports".
- (re-check) Self-test 6 and 10, answers: "Iliad 23", "Iliad 10.261–265" and "basileus" are in roman; the body italicises *Iliad* and *basileus*.
- (re-check) "The Dark Age in the ground", first paragraph: the period "divides into Submycenaean (c. 1070–1025), Protogeometric (c. 1025–900) and Early Geometric (c. 900–850)", while the table that follows ends with "Early and Middle Geometric | 900–760". Not a contradiction, but the two lists differ in their last phase.

### 2.1

- "The Hittite Kumarbi cycle", paragraph after figure 3: "three kings ending in a storm-god", while the paragraph above and the motif table ("Alalu, Anu, Kumarbi, Teshub") give four kings.
- Self-test 4, answer: "A cave on Mount Aigaion near Lyktos in Crete (477–484)". The body says Rheia is sent to Lyktos and Gaia hides the child in a cave on Mount Aigaion; it does not say the cave is near Lyktos.
- Self-test 5, answer: "Zeus set it up at Pytho (Delphi) as a sign for mortals (497–500)". The body cites 498–500 for the stone at Pytho.
- Self-test 10, answer: "with an anthropogony from the Titans' ashes". The body says only "dismembered by the Titans, from whose remains mankind comes": no ashes, and "whose" there could be Dionysus or the Titans.
- (re-check) Self-test 10 answer: "an anthropogony from the Titans' ashes". The body says only "dismembered by the Titans, from whose remains mankind comes"; "ashes" is not in the body, and the body's "whose" leaves open whether the remains are the Titans' or Dionysus's.
- (re-check) Self-test 4 answer: "A cave on Mount Aigaion near Lyktos in Crete (477–484)". The body says Rheia "is sent to Lyktos in Crete; Gaia hides the newborn in a cave on Mount Aigaion"; it does not say the cave is near Lyktos.
- (re-check) Self-test 5 answer cites "(497–500)"; the body cites the stone at Pytho as "(498–500)".
- (re-check) Self-test 6 answer cites "(624–663)" and says the Hundred-Handers "bury the Titans under rocks"; the body cites 639–663 for their release and says they "hurl three hundred rocks at a time" (687–712), not that they bury the Titans.
- (re-check) Family tree (pre block): "Nemesis, Apate, Eris, Moirai..." under Nyx; Apate is named nowhere in the body (the body's list at 211–232 is "Moros, Thanatos, Hypnos, Nemesis, Eris and her brood"). Likewise "Zeus + Hera ──► Hebe, Ares, Eileithyia" and "Hera alone ──► Hephaestus" are not stated in the body, which says only that Zeus's marriage with Hera "add[s] a sphere to the regime (901–929)".
- (re-check) Spelling: the monster is "Typhoeus" in "Typhon, the Giants..." paragraph 1 and the family tree, "Typhon" in the heading, the dispute box, "What the parallels tell us" and Carry forward 2; the text never says the two are the same name's variants.

### 2.2

- Hera, Domains and epithets: "ties her to her favourite city (<em>Iliad</em> 4.51–52); Her hostility". Capital H after a semicolon.
- Self-test 3, answer: "Homer's Poseidon calls him the elder brother (<em>Iliad</em> 13.355, 15.166)". The body (Zeus, dispute box) gives Poseidon's words at 15.166 only; at 13.355 it says "Zeus is explicitly the elder", without making Poseidon the speaker.
- Self-test 4, answer: "Odysseus invokes Zeus as avenger of suppliants and strangers against Polyphemus". The body says only that "the Cyclops episode is a crime against Zeus (<em>Odyssey</em> 9.270–271)"; Odysseus' invocation is not in it.
- Self-test 6, answer: "centuries before Herodotus' or the Thracian-origin theory's dates". The body gives no date for either.
- Self-test 1: "the earliest firm evidence for a cult of 'the Twelve Gods' at Athens". The body does not call the altar the earliest evidence.
- Inconsistent citation of the same passage: Poseidon, Defining myths, "(<em>Iliad</em> 15.187–193)"; "What an Olympian is", Against the Titans, "(<em>Iliad</em> 15.187–199)".
- Inconsistent citation form for the same hymn: "(<em>Homeric Hymn</em> 3.25–126)" against "(Hymn 3.146–164)" and "(Hymn 3.300–374)" under Apollo.
- (re-check) Hera, Domains and epithets: "ties her to her favourite city (<em>Iliad</em> 4.51–52); Her hostility to Zeus's children": the word after the semicolon is capitalised.
- (re-check) Citation range differs for the same passage: Poseidon, Defining myths, has "(<em>Iliad</em> 15.187–193)"; "Against the Titans" has "(<em>Iliad</em> 15.187–199)".
- (re-check) Self-test 3 answer: "Homer's Poseidon calls him the elder brother (<em>Iliad</em> 13.355, 15.166)". The body attributes only 15.166 to Poseidon ("born earlier"); at 13.355 it says only "Zeus is explicitly the elder", without giving the speaker.
- (re-check) Self-test 4 answer: "Odysseus invokes Zeus as avenger of suppliants and strangers against Polyphemus". The body says only that "the Cyclops episode is a crime against Zeus" (<em>Odyssey</em> 9.270–271); it never says that Odysseus invokes Zeus.
- (re-check) Self-test 6 answer: "centuries before Herodotus' or the Thracian-origin theory's dates". The body gives no date for either view and never says "centuries".
- (re-check) Self-test 1 question: "the earliest firm evidence for a cult of 'the Twelve Gods' at Athens". The body never calls the altar the earliest evidence.
- (re-check) "Against the Titans": "Uranus is castrated by Cronus, Cronus deposed by Zeus, and Zeus alone ends the cycle ... What they lack is a stable distribution of honours". "They" is meant to be the Titans, but the nearest names are Uranus, Cronus and Zeus.
- (re-check) Spelling: "Hephaestus" is Latinised throughout, but the temple is "Hephaisteion" (Hephaestus, Cult).

### 2.3

- Self-test 2, answer: "Hecate, in her cave, and Helios." The body ("Only Hecate and Helios hear her cry") never mentions a cave.
- Self-test 6, answer: "continuing his kingship, not weighing lives" is stated as fact; the body gives it only as Sourvinou-Inwood's reading in the dispute box after "The judges", where whether Homer's Minos judges the dead at all is "contested".
- Inconsistent name: "Pyriphlegethon" in "The geography of the underworld" (paragraph and table) but "ringed by Phlegethon" in "From Homer to Virgil" (Aeneid 6 paragraph), with no note that they are the same river.
- (re-check) Self-test 2, answer: "Hecate, in her cave, and Helios." The body says only "Only Hecate and Helios hear her cry"; no cave is mentioned.
- (re-check) Self-test 6, answer: "He is giving judgements to the dead who bring disputes to him, continuing his kingship, not weighing lives." The body attributes "continuing his earthly kingship" to Sourvinou-Inwood and calls the question "contested" (dispute box after "The judges"); the answer states it as settled.
- (re-check) Self-test 4, answer: "with her ascent at autumn sowing". The body says only that her months below are those the seed-corn spends in storage "from harvest to sowing"; it never names autumn sowing as her ascent (it gives sowing as October, so this is an inference, not a statement).
- (re-check) Inconsistent naming of the fire river: the table and "The geography of the underworld" use "Pyriphlegethon" ("rings Tartarus in Aeneid 6.550-551"), while "From Homer to Virgil" says "ringed by Phlegethon" with no note that they are the same river.

### 2.4

- §"The sons of Hellen": the ASCII stemma (`<pre class="tree">`) directly above figure 2 draws the same tree; one of the two is now redundant. Its line "Hellen (or Hellen son of Zeus)" is also awkwardly worded.
- §"The sons of Hellen", para 2: "through a father whose Athenian marriage is to a foreign woman" is muddled: Creusa is the Athenian; the outsider in that marriage is Xuthus.
- Self-test 1 cites "<em>Theogony</em> 535–560"; the body gives 551 and 556–557 (and 507–616 for the whole episode), never 535–560. It also says "burned bones and fat"; the body says "burn white bones".
- Self-test 4: "may post-date his death in 456 BC"; the body says only that the play "dates after 456 BC" and never says 456 BC is Aeschylus's death.
- Self-test 8: "first attested in Pindar, <em>Olympian</em> 9" for the laas/laos pun; the body gives the pun in the Apollodorus account and says only that Pindar has "a stone race", after the <em>Catalogue of Women</em>.
- Self-test 9: "Xuthus, Hellen's third son"; the body never calls him the third son (only the stemma's order implies it).

### 2.5

- Self-test 1, answer: "Clio, Euterpe, Thalia, Melpomene, Terpsichore, Erato, Polymnia, Ourania and Calliope (Theogony 75–79)". The question asks for the Muses "as Hesiod lists them"; the body never gives Hesiod's order, and its table lists Calliope first.
- Self-test 6, answer: "Philippides met Pan on the road to Sparta before Marathon; Pan complained of neglect and promised help". The body (Pan) says only "Philippides met Pan before Marathon"; the road to Sparta, the complaint of neglect and the promise of help are not in it.
- Self-test 2, answer: "the first keeps it among the primordial dark powers". The body's dispute box gives only West's reading of the Zeus–Themis version; this reading of the Nyx version is not stated there.
- Carry forward 3: "Asclepius rose from Homeric mortal to imperial god" ("imperial" is not in the body, which ends his spread at Rome in 293 BC); "saviours of sailors in the Hymns" (the body cites one, Homeric Hymn 33).
- (re-check) Self-test 1, answer: "Clio, Euterpe, Thalia, Melpomene, Terpsichore, Erato, Polymnia, Ourania and Calliope" is given as the order "as Hesiod lists them", but the body never states Hesiod's order; its table puts Calliope first.
- (re-check) Self-test 6, answer: "Philippides met Pan on the road to Sparta before Marathon; Pan complained of neglect and promised help" adds details the body does not state (body: "Philippides met Pan before Marathon and how Athens then founded his cave shrine").
- (re-check) Self-test 2, answer: "the first keeps it among the primordial dark powers" is an interpretation the body does not state (the body's dispute box gives only West's reading of the Zeus–Themis version).
- (re-check) Cult table, "Essentially literary" column: "Nyx's and Eris's children" sits as a blanket entry while Nyx's children Nemesis, the Moirai and Hypnos appear in the cult columns, and the body says Thanatos had a Spartan shrine (Plutarch, Cleomenes 9).

### 2.6

- Self-test 7, answer: "Pholus of Silenus and a nymph". The body gives only "Pholus (son of Silenus, 2.5.4)"; "and a nymph" is not in the body.
- Self-test 1, answer: "Phorcys and Ceto, children of Pontus and Gaia, *Theogony* 233–239". The body cites the line range 233–336 for the kin-group and never gives 233–239.
- Self-test 7, answer: "the cloud Nephele". The body's Centaurs section says only "a cloud" / "the cloud"; the name Nephele appears only in the genealogy diagram ("Centaurus (Ixion + Nephele)").
- Table, Sirens row: "Achelous + a Muse" under "Parents (earliest source)". The body's sources for that parentage are Apollodorus, *Epitome* 7.18–19; the dispute aside cites earlier sources with other parents (Euripides, *Helen* 167–169: Earth; Sophocles fr. 861 Radt: Phorcys), so this is not the earliest source's parentage.
- Table, Typhon row: key source "*Theogony* 853". The body cites 820–880 and 821–822, never 853.
- (re-check) Self-test 1 answer: "Phorcys and Ceto, children of Pontus and Gaia, *Theogony* 233–239." The body cites only *Theogony* 233–336 for the kin-group; the line range 233–239 is not in the body.
- (re-check) Self-test 7 answer: "Pholus of Silenus and a nymph." The body says only "Pholus (son of Silenus, 2.5.4)"; "and a nymph" is not in the body.
- (re-check) Self-test 8 answer: "The Sirens, who drown themselves after a ship passes (Apollodorus, *Epitome* 7.19)". The body gives Apollodorus only "fated to die when a ship passed unharmed" and attributes the drowning to Lycophron: "Lycophron, *Alexandra* 712–737, has them drown themselves."
- (re-check) Self-test 8 question: "Which two monsters die without any hero killing them?" The body also has Talos die without a hero: "The one monster killed by a witch, not a hero." The question admits a third answer.
- (re-check) Self-test 4 question: "Which of Typhon and Echidna's children is not killed by Heracles" and the body's Cerberus entry, "the one brood-mate the hero does not kill". The body's own list has the Chimaera killed by Bellerophon, the Sphinx dying after Oedipus answers and the Crommyonian Sow killed by Theseus, so Cerberus is not the only one of the brood Heracles does not kill.
- (re-check) Table, Sirens row, "Parents (earliest source)": "Achelous + a Muse". The body cites Euripides, *Helen* 167–169 (Earth) and Sophocles fr. 861 Radt (Phorcys), both earlier than Apollodorus, the body's source for Achelous and Melpomene.

### 3.1

- Inconsistent spelling of Andromeda's mother: "Andromeda, daughter of Cepheus and Cassiepea" (Andromeda and the sea monster, first paragraph), then "Perseus, Andromeda, Cepheus, Cassiopeia and Cetus" (second paragraph).
- Self-test 8 states more than the body: the answer says "there is no discus and Acrisius is not killed", where the body's dispute box says only "Acrisius apparently still alive".
- Self-test 1 shifts the body's claim: the answer says the phrase "suggests the religious sense of 'hero' was emerging as the epics took shape", where the body says "scholars suspect a later religious idea leaking into the epic".
- The hero-pattern table's Perseus entry "hero shrine on the Argos–Mycenae road" has no citation in the body; Pausanias 2.18.1 is cited only for Seriphos and the Athens precinct. (Figure 1 repeats this note from the table.)
- (re-check) Inconsistent spelling, "Andromeda and the sea monster": paragraph 1 has "Cepheus and Cassiepea"; paragraph 2 has "Cepheus, Cassiopeia and Cetus". ("Cassiepea" is also not a standard form; the usual Greek form is Cassiepeia.)
- (re-check) Dangling reference, "The return, the discus and the Perseid dynasty", paragraph 1: "a precinct at Athens for Dictys and Clymene as 'the saviours of Perseus'". Clymene appears nowhere else in the report.
- (re-check) Table vs body, hero-pattern table, last row: "hero shrine on the Argos–Mycenae road; cult on Seriphos and at Athens". The body never mentions a shrine on the Argos–Mycenae road, and the Athens precinct it describes is for Dictys and Clymene, not Perseus.
- (re-check) Self-test 8 answer: "there is no discus and Acrisius is not killed." The body is more cautious: "Acrisius apparently still alive."
- (re-check) Self-test 7 answer: "Apollodorus knows only a variant that she rivalled Athena's beauty." The body says Apollodorus "reports a variant", not that this is the only version he knows.

### 3.2

- Self-test 1, answer: "Zeus swore that a Perseid born that day would rule". The body (Birth, para. 2) says "a man of his blood will be born that day to rule all his neighbours"; "Perseid" in the oath is the answer's, not the body's. The question's "born to rule Mycenae" also names a city the body never ties to Eurystheus.
- Self-test 2, answer: "the madness is pure divine malice". The body (Youth, para. 2) says madness "strikes a man who has finished the civilising work and has nothing left to earn"; "pure divine malice" is not stated there.
- Self-test 10, answer: "the Cynosarges gymnasium". The body (The politics, Athens) speaks only of "his precinct at Cynosarges"; no gymnasium is mentioned.
- (re-check) Self-test 1, question and answer: "born to rule Mycenae" and "Zeus swore that a Perseid born that day would rule". The body (Birth section) says only "a man of his blood will be born that day to rule all his neighbours"; it names neither Mycenae as the realm nor "Perseid" as the oath's term.
- (re-check) Self-test 2, answer: "the labours earn nothing and the madness is pure divine malice". The body says madness after the labours "makes them irrelevant to it" and strikes "a man who has finished the civilising work and has nothing left to earn"; "pure divine malice" is not stated.
- (re-check) Self-test 10, answer: "the Cynosarges gymnasium". The body (Athens paragraph) says only "his precinct at Cynosarges"; a gymnasium is not mentioned.
- (re-check) Figure 1 (re-check), minor: it draws the Argeads as children of Temenus, a fact from the Macedon paragraph that follows, while it sits after the Heracleidae paragraph; the caption notes the gap between Hyllus and the great-grandsons but not the one between Temenus and the Argeads ("by their own claim" softens it). Not a figure fault.

### 3.3

- Self-test answers, formatting: titles that the body italicises appear without italics: Q4 "Apollodorus, Epitome 1.5–6"; Q6 "(Odyssey 11)" and "(Theogony 947–949)".
- Self-test Q9 answer: "found a giant skeleton with bronze weapons". The body (Cimon and the bones) says "a coffin with a body of great size, a bronze spear and a sword". The answer also says the bones "were buried in the Theseion". The body says "in the middle of the city, in a precinct", and its dispute box says "The Theseion itself has never been found". The answer is close but goes slightly beyond the body.
- Inconsistent placing of the Hephaisteion: "The Hephaisteion in the Agora (c. 450)" (The vase evidence) against "the marble temple above the Agora that older maps call the 'Theseion' is the Hephaisteion" (dispute box after figure 2).
- (re-check) Self-test answers 4 and 6: titles are set in roman where the body italicises them: "Apollodorus, Epitome 1.5–6" (answer 4); "(Odyssey 11)" and "(Theogony 947–949)" (answer 6).
- (re-check) Self-test answer 9: "they were buried in the Theseion in the city centre". The body (Cimon and the bones) says only "buried them in the middle of the city, in a precinct"; the name Theseion is given to that precinct only in the following "Where sources disagree" aside ("The Theseion itself has never been found"). Consistent, but the answer joins two places the body keeps apart.
- (re-check) "Making a rival to Heracles", first paragraph: "between about 570 and 510" carries no BC; the first BC in that section is "Around 510–500 BC" in the next subsection.

### 3.4

- Sirens citation inconsistent: "The ship and the crew" has "sings down the Sirens (4.891–919)"; "The return routes" has "Orpheus outsings the Sirens (4.891–921)".
- Self-test 2 answer adds what the body does not state: "and that he is too old to go himself (Pythian 4.156–167)". The body says only "Phrixus' ghost demands his soul and the fleece be brought home".
- Self-test 10 question, "Medea's son who gave his name to the Medes", applies the eponym to Hesiod's Medeius; the body never says Medeius gave his name to the Medes (it says "Whether the Medes were named from Medea or Medus splits Herodotus from the mythographers").
- (re-check) Self-test 2 answer: "and that he is too old to go himself (Pythian 4.156–167)". The body ("Pelias and the one-sandalled man") gives only the demand of Phrixus' ghost and says nothing of Pelias' age.
- (re-check) Self-test 9 answer: "She hides each newborn in the temple of Hera Akraia". The body's Eumelus passage says only "Hera's temple"; it names Akraia only for the cult Euripides' Medea announces.
- (re-check) Orpheus and the Sirens are cited two ways: "sings down the Sirens (4.891–919)" ("The ship and the crew") and "Orpheus outsings the Sirens (4.891–921)" ("The return routes").
- (re-check) Inconsistent spelling: "a pan-Hellenic charter" ("The ship and the crew") against "a Panhellenic heroine" (dispute box, "After Corinth").

### 3.5

- Self-test 5 answer: "calls the twins the first founders and wallers of Thebes". The body quotes *Odyssey* 11.260–265 only as "first founded the seat of seven-gated Thebes"; "wallers" is not in the body. The same answer says Pausanias assigned "Cadmus the acropolis (Cadmeia)", but the body says only "the acropolis"; "Cadmeia" does not appear there as the acropolis's name. The body has only "Cadmeian" script.
- Self-test 9 answer: "and Athena recoiled" and "fleeing Periclymenus by the Ismenus". The body says only "so Athena withholds the immortality she was bringing" and does not name the Ismenus.
- Self-test 10 answer: "*Antigone* opens with both brothers dead, while *Colonus* shows Polynices alive and being cursed" is given as an inconsistency. The body ("The lost epics and the three tragedians") lists two inconsistencies (Oedipus's death and Creon's character), not this one. This third point follows from the plots but is not stated as a contradiction.
- Self-test 3 answer: "reclaimed by deceit for Callirhoe". The body says Alcmaeon lied to Phegeus to get the heirlooms back, but it never says he recovered them before he was killed.
- "The Epigoni, the sack and the necklace", last paragraph: "Four generations after Harmonia's wedding". The body gives no count of generations from the wedding to Phayllus, who lived in the Third Sacred War. The figure looks like it counts only to Acarnan and Amphoterus.
- (re-check) Self-test 8 answer gives the Aeschylean gates in an order ("Tydeus (Proetid), Capaneus (Electran), Eteoclus (Neistan), Hippomedon (Onca), Parthenopaeus (Northern), Amphiaraus (Homoloid), Polynices (Seventh)"); the body's table lists the champions in a different order and states no gate sequence.
- (re-check) Self-test 9 answer: "fleeing Periclymenus by the Ismenus"; the body (table, Amphiaraus row) does not mention the Ismenus.
- (re-check) Self-test 10 answer: "<em>Antigone</em> opens with both brothers dead, while <em>Colonus</em> shows Polynices alive and being cursed"; the body does not state this inconsistency (it gives only the Ismene line and the three Creons).
- (re-check) Self-test 5 answer: "the acropolis (Cadmeia)"; the body (line 45) says only "the acropolis".
- (re-check) Founding section: "Creon's line will be reckoned Spartan-born"; "Spartan" reads as Sparta, not the Spartoi (the Self-test 2 answer repeats "Spartan-born").
- (re-check) Phoenician Women paragraph: "he would go to the stars for Tyranny"; the capital T is inconsistent with lower-case usage elsewhere.
- (re-check) Figure 2 records Aeschylus's Laius and Seven at 467 BC but not the trilogy's Oedipus, which the text places in the same trilogy (not a fault in the figure: the text gives an explicit date only for Laius and Seven).

### 3.6

- Self-test 8, answer: "He wants to deny any link between the mythical Tereus and Teres, father of Athens' Thracian ally Sitalces." The body (section "Procne, Philomela and Tereus") names Sitalces but never Teres; the answer states what the body does not.
- Self-test 5, answer: "the curse is one explanation for the crimes of Atreus and Thyestes and their descendants." The body (section "The house of Tantalus", closing paragraph) gives Myrtilus' curse as what made "the deaths of Agamemnon and Clytemnestra seem fated", not as an explanation of Atreus' and Thyestes' crimes; a slight stretch beyond the body.
- (re-check) Self-test 8, answer: "He wants to deny any link between the mythical Tereus and Teres, father of Athens' Thracian ally Sitalces." The body (section "Procne, Philomela and Tereus", last paragraph) names only Sitalces ("notably Sitalces, whose connection Thucydides is anxious to dissociate from the barbaric Tereus"); Teres is not in the body.

### 3.7

- Self-test 4, answer: "Ovid cuts him so Apollo's desire is unrivalled and Cupid's arrow supplies the motive." The body ("Apollo's loves", Daphne paragraph) says only that Ovid "cuts Leucippus" and that the Cupid's-arrow motive "is his"; it gives no reason for the cut.
- Self-test 7 asks for "the earliest literary evidence" for the golden touch and the asses' ears; the body (Midas, "Hubris and the gods' justice") says the touch "is a proverb in Aristotle" and the ears "are in Aristophanes, Plutus 287", but never calls either the earliest.
- Inconsistent transliteration in one paragraph (Lycaon, "Shape, sex and hospitality"): "Zeus Lycaeus" and "the Lycaean rite" beside "Mount Lykaion".
- Table, last row: "Homer, Hesiod, Herodotus, Sappho" as the earliest Greek evidence for a group that includes Lycaon, whose Greek witnesses in the body are Pausanias, Apollodorus and Plato.
- (re-check) Self-test 4, answer: "Ovid cuts him so Apollo's desire is unrivalled and Cupid's arrow supplies the motive." The body (Daphne paragraph) says only that Ovid "cuts Leucippus" and that Cupid's arrow motivates Apollo; "so Apollo's desire is unrivalled" is a reason the body does not state.
- (re-check) Self-test 7, answer: "The full narratives are Ovid's." The body says the golden touch "is told fully only in Ovid", but for the asses' ears only that "Ovid adds the barber and the whispering reeds"; it does not say the ears' full narrative is first or only Ovid's.
- (re-check) Possible confusion of two titles: "Lament for Bion 123–124" (Orpheus section, the poem mourning Bion) and "Bion's Lament is the Hellenistic pathetic treatment" (Adonis paragraph, Bion's Lament for Adonis). A reader checking citations may take them for the same work; "Bion's Lament for Adonis" would separate them.
- (re-check) Quotation marks: the body uses straight quotes ("Augustus", "hated by Minerva", "do not seek to become Zeus"), the figure captions curly ones (“Love that fails: Orpheus and Eurydice”, “Hubris and the gods' justice”).

### 4.1

- Self-test 9 (answer): "with contrary winds as the cause". The body ("Iphigenia", and its dispute box) gives the Strymon winds as circumstance and says the causes of Artemis' anger are three stories "none adopted by Aeschylus, whose portent is eagles devouring a pregnant hare". The answer names a cause the body says Aeschylus does not give.
- Self-test 10 (answer): "the <em>Cypria</em> and Apollodorus name Hector". The body ("Protesilaus and the landing") says only "the <em>Cypria</em> named Hector"; Apollodorus is not cited for the killer.
- Self-test 3 (answer): "Zeus and Electra, Dardanus, ... Priam (<em>Iliad</em> 20.215–241)" under the question "in Homer's genealogy". The body names Electra in a paragraph that cites both Homer and Apollodorus 3.12.1–3 and does not say Homer names her.
- Date style: "<em>Iphigenia among the Taurians</em> (c. 414)" and "<em>Iphigenia at Aulis</em> (405)" ("Iphigenia") carry no BC, while every other play date in the report does ("(415 BC)", "(412 BC)", "(438 BC)", "(409 BC)").
- Citation style: "Hyginus, <em>Fabulae</em> 91" ("The house of Priam") against bare "Hyginus 92", "Hyginus 95" and the rest elsewhere.
- (re-check) Self-test 10, answer: "the <em>Cypria</em> and Apollodorus name Hector". The body ("Protesilaus and the landing") says only "the <em>Cypria</em> named Hector"; it never says Apollodorus names him.
- (re-check) Self-test 3, answer: "Zeus and Electra, Dardanus, ... Priam (<em>Iliad</em> 20.215–241)" under "Homer's genealogy". The body cites Electra in the same sentence as Apollodorus' expansion ("Apollodorus, <em>Library</em> 3.12.1–3 expands it. Dardanus, son of Zeus and the Pleiad Electra"); it does not state that Homer names Electra.
- (re-check) Inconsistent date style: "Iphigenia": "<em>Iphigenia among the Taurians</em> (c. 414)" and "<em>Iphigenia at Aulis</em> (405)" have no BC, whereas elsewhere the report writes "(415 BC)", "(412 BC)", "(409 BC)", "(438 BC)".
- (re-check) Inconsistent spelling of the city: "before Ilios existed on the plain" ("Troy before Priam") against "Ilion" in "<em>Sack of Ilion</em>" and the tree ("founds Ilion").

### 4.2

- Self-test 3, answer: "a divine quarrel in 1 is answered by a divine council in 24". The body (Structure) has the reverse direction: "the quarrel of gods in 1 answers the council of gods in 24".
- Self-test 6, answer: "so fate is a norm Zeus upholds rather than an absolute limit". The body leaves this open: the dispute box gives three readings and says "The Sarpedon scene is the crux and supports all three"; the answer settles what the body does not.
- Self-test 10 asks for "one passage where each is foreshadowed", but the answer for the Wooden Horse gives "(not in the <em>Iliad</em> at all; <em>Odyssey</em> 8.492–520)", which is not a foreshadowing in the poem; question and answer do not match.
- BC marking is inconsistent in The Homeric Question section: "the second half of the eighth century BC" carries BC, but "by about 740–730", "around 1300 and again around 1180", "around 750–725" and "after 663" do not.
- (re-check) "What the Iliad is": "telling about fifty days" against "Structure": "The poem narrates about 51 days" (and Self-test 2, "About 51 days"). Both approximate, but the count is given two ways.
- (re-check) Self-test 9 answer: "because 9.381–384 praises the wealth of Egyptian Thebes" — the body says only "the reference to Egyptian Thebes (9.381–384)"; "praises the wealth" is not stated there.
- (re-check) Self-test 10: the question asks for "one passage where each is foreshadowed", but the answer for the Wooden Horse gives "not in the Iliad at all; Odyssey 8.492–520", which is not a foreshadowing.
- (re-check) "The Homeric Question and the current view", dispute aside: "treated in module 10.10" — a cross-reference to another module, not verifiable from this report; check it exists and covers Korfmann and Kolb.

### 4.3

- Self-test 2, answer: "preserved by Photius (<em>Bibliotheca</em> cod. 239) and in <em>Iliad</em> manuscripts". The body says Proclus' work is "described by Photius" and "preserved for the Trojan poems in manuscripts of the <em>Iliad</em>"; it does not say Photius preserves the summaries.
- Self-test 5, answer: "Archaic art shows an ankle wound". The body says the Chalcidian amphora shows "an arrow in the lower leg"; "ankle" comes only from Apollodorus and Hyginus.
- Self-test 6, answer: "Odysseus wins." The body's account of the <em>Little Iliad</em> judgement implies it but never states it.
- "Priam and Astyanax": "Pyrrhus kills Polites" uses Virgil's name for Neoptolemus without saying they are the same person; everywhere else the report says Neoptolemus.
- "Aeneas and the Roman claim": "the <em>Little Iliad</em>, in Tzetzes' fragment, has Neoptolemus take him captive" reads as if only one Tzetzes fragment exists; the one cited earlier (fr. 29 West, in Tzetzes) is the Astyanax fragment, and this one has no fragment number.
- "Carry forward" 3: "the <em>Nostoi</em>" is not mentioned anywhere in the body (a forward reference with no anchor in this report).
- (re-check) Self-test 2, answer: "preserved by Photius (<em>Bibliotheca</em> cod. 239) and in <em>Iliad</em> manuscripts". The body says the Chrestomathy is "described by Photius (<em>Bibliotheca</em> cod. 239) and preserved for the Trojan poems in manuscripts of the <em>Iliad</em>": Photius describes it, he does not preserve the summaries.
- (re-check) Self-test 5, answer: "Archaic art shows an ankle wound". The body says the Chalcidian amphora shows "an arrow in the lower leg"; the ankle is Apollodorus' and Hyginus' word, not the vase's.
- (re-check) "The sack", Priam paragraph: "Pyrrhus kills Polites" uses Virgil's name for Neoptolemus without saying they are the same person; everywhere else the report says Neoptolemus.
- (re-check) "Three lost poems", witnesses paragraph: "Quoted fragments and testimonia in scholia, Pausanias and Tzetzes, collected by Bernabé, Davies and West (Loeb <em>Greek Epic Fragments</em>, 2003)." is a sentence without a main verb (the following kinds are likewise verbless); intentional list style, but it reads as a fragment.

### 4.4

- Self-test 6, answer: "Heracles' bow and arrows" — the body (Philoctetes in Italy) says only "Heracles' bow". The answer also puts "Macalla near Croton" under "(Lycophron, Strabo)"; the body has Lycophron name Macalla and Strabo place Petelia, Crimissa and Chone "near Croton".
- Self-test 8, answer: "when the other Cyclopes hear that 'no one' is hurting Polyphemus and leave" — the body (The wanderings in order) gives the pun and 9.405–414 but not this payoff.
- Self-test 9, answer: "(23.177–230)" — the body cites the Penelope scene as "23.85–230"; 23.177 appears nowhere in the body.
- Self-test 10, answer: "Hellenistic critics (Xenon, Hellanicus)" — the body does not call the chorizontes Hellenistic.
- Menelaus in Egypt, dispute box: "Alan Lloyd's commentary" — no title or date, so the reader cannot check it (Lloyd's commentary on Herodotus Book 2 is presumably meant).

### 4.5

- Self-test 2, answer: "Pindar, *Pythian* 11.22–25, in the 470s or 450s BC, before Aeschylus' trilogy of 458." The body gives no date for *Pythian* 11 (it cites only "*Pythian* 11.17–37"), so the date is stated only in the answer; and "450s" would include years after 458, which contradicts "before Aeschylus' trilogy of 458". The line range 11.22–25 also appears only here.
- Self-test 1, answer: cites "11.421–423" for Cassandra's killing; the body cites only "*Od.* 11.405–434" (within that range, so not wrong, but not in the body).
- "Sophocles' Electra", first paragraph: "usually placed 420–410" gives no BC, while every other date in the report carries it.

### 5.1

- "Homer fixed in writing", dispute box: "the Nestor's cup joke is the only external evidence that epic Nestor was known to Greeks in the 720s". The body dates the cup "c. 740–720", so "in the 720s" narrows the text's own date to its lower end; "by c. 720" would match.
- "Hesiod: a person with a biography", first paragraph: "(27–41, 38–39, 263–264)". 38–39 lies inside 27–41, so the citation repeats itself; presumably 38–39 is meant to point to "gift-devouring kings", but as written it reads as a doubled reference.
- "The population surge": "Hesiod's advice to raise one son and Theran tradition of drought-driven emigration" lacks an article ("the Theran tradition").
- Self-test 3, answer: "a Levantine port that merely consumed Greek pottery". The body says "a native port that Greek traders visited and where some Greek pottery was consumed by locals"; "merely" and "Levantine" for "native" go slightly beyond it, but the sense holds.
- Self-test 4, answer: "passed through sixth-century Athenian Panathenaic performance". The dispute box it draws on says "Athens was the 'Panathenaic bottleneck'" without a century; the sixth century comes from the Peisistratid context and the Carry forward, so it is supported, though not stated in the box itself.
- (re-check) Self-test 5, answer: "Also the Muses on Helicon (<em>Theogony</em> 22–34) and the dispute with Perses (27–41)." Coming straight after the *Theogony* reference, "(27–41)" reads as *Theogony* 27–41; the body gives *Works and Days* 27–41.
- (re-check) Self-test 8, answer: "Stone Doric temples begin in the seventh century at Isthmia." The body names Isthmia as one of three seventh-century examples ("Isthmia, c. 690–650; Corinth's old temple; Thermon"), not as the place they begin.
- (re-check) "The population surge": "Hesiod's advice to raise one son and Theran tradition of drought-driven emigration" is missing an article ("the Theran tradition").
- (re-check) Spelling: "Pithekoussai" throughout, "Pithecusae" once in the Livy paraphrase ("the Chalcidians moved from Pithecusae to Cumae"). Probably deliberate (Livy's Latin form), but unmarked.
- (re-check) Carry forward 2: "datable only within a window of roughly 750–650" while the body gives West's Iliad poet c. 680–640; the window's end is rounded past a date the body states.

### 5.2

- "What a polis was", first paragraph: a `<blockquote>` sits inside `<p>` ("...in Sicily: <blockquote>men are the city, not walls or empty ships.</blockquote> (Thucydides 7.77.7).</p>"). Invalid HTML: the browser closes the paragraph before the quote, so "(Thucydides 7.77.7)." is left as a stray line with a dangling `</p>`.
- Inconsistent Herodotus range for Cyrene: "Herodotus 4.150–159" ("How a colony was founded", table, figure 3 caption) against "Herodotus gives Theran and Cyrenaean versions (4.150–158)" ("The main waves and sites", Cyrene paragraph).
- Inconsistent Herodotus range for Scyles/Olbia: table "Herodotus 4.17–18, 78–79" against "(Herodotus 4.78–80)" in the Black Sea paragraph.
- Self-test 10 cites "(Herodotus 1.166)"; the body cites "Herodotus 1.166–167".
- Self-test 8 states what the body does not: "under Pharaonic control" and "the Greeks had no territory or independent polis there" (body: "a licensed trading port", granted by Amasis).
- Self-test 4 states what the body does not: the deme "made the basis of Athenian citizenship by Cleisthenes" (body: ten tribes built from 139 demes, cutting across kin loyalties; nothing on citizenship being based on the deme).
- Self-test 5: "choose and lay out the site"; the body says only that the oikist "laid out the site".
- Carry forward 2: colonies "doubled the Greek world between 750 and 550"; the body gives no such figure or claim.
- (re-check) "What a polis was", para 1: a `<blockquote>` sits inside a `<p>` ("...in Sicily: <blockquote>men are the city, not walls or empty ships.</blockquote> (Thucydides 7.77.7).</p>"). That HTML is invalid: the browser closes the paragraph early, so "(Thucydides 7.77.7)." is left as loose text.
- (re-check) Cyrene citation range is inconsistent: "Herodotus 4.150–159" ("How a colony was founded", and the table) against "Herodotus gives Theran and Cyrenaean versions (4.150–158)" ("Cyrene").
- (re-check) Scyles citation is inconsistent: table "Herodotus 4.17–18, 78–79" against "killed for it (Herodotus 4.78–80)" ("The Black Sea").
- (re-check) The possessive is spelled two ways: "Thucydides' Sicilian dates" (Osborne box) against "Herodotus's account" / "Herodotus's eventual definition".
- (re-check) The chronology conflicts: "Colonisation and Greek identity", para 3, puts Alalia at "around 540–535" and then says "By 550 the frontier had hardened into spheres". Self-test 10 says Alalia "marks the hardening", which would be after 550.
- (re-check) Self-test 1: "most were far too small to be called states". The body says "not quite a state" (because a polis was a community) and "Most were tiny", but never that they were too small to be states.
- (re-check) Self-test 4: "Deme: ... made the basis of Athenian citizenship by Cleisthenes". The body says only that Cleisthenes built ten tribes "from 139 demes". It does not say demes became the basis of citizenship.
- (re-check) Self-test 5: "choose and lay out the site". The body says the oikist "laid out the site", not that he chose it.
- (re-check) Self-test 8: "under Pharaonic control ... the Greeks had no territory or independent polis there". The body says "a licensed trading port" that Amasis "granted" and says nothing about territory or an independent polis.
- (re-check) Carry forward 2: "they doubled the Greek world between 750 and 550". The body never states "doubled".

### 5.3

- Self-test, question 2 answer: "The Protocorinthian Chigi vase, about 650 to 640 BC." The body ("The hoplite panoply and the phalanx") and figure 1 call it the "Chigi olpe"; one name throughout would be cleaner.
- "Coinage from Lydia": the section's dates (Artemision c. 600, Croesus c. 550, Aegina c. 550, owls c. 515) carry no citation; Herodotus 1.94 is cited only for Lydian priority. Worth a source in the text, since figure 4 draws those dates.
- Table in "The age of tyrants": Psammetichus is listed for Corinth but appears nowhere in the body text.
- (re-check) Inconsistent name: body, "The hoplite panoply and the phalanx", calls it "the Protocorinthian Chigi olpe"; Self-test answer 2 says "The Protocorinthian Chigi vase".
- (re-check) Slight drift: body, "Lawgivers and the first written codes", says the Dreros law forbids the kosmos "to hold office again for ten years"; Self-test answer 6 says "to hold office again within ten years".

### 5.4

- Self-test 4, answer: "Herodotus already knew rival accounts of the laws' origin". The body never says this; it cites Herodotus 1.65–66 only for Lycurgus giving the laws and the Delphic greeting, and 1.65 for crediting him with the ephorate.
- Self-test 4, answer: "his dates vary by centuries between authors". The body gives the two datings (Xenophon: contemporary with the Heraclids; Aristotle: the first Olympiad) but never says the gap is "centuries".
- Self-test 9: "Trace Spartiate numbers from 480 to the 240s". The body never dates Demaratus' figure to 480 (Herodotus 7.234 is given with no year).
- "The Peloponnesian League": "The League dissolved after Leuctra in 371, when Epaminondas freed Messenia" sits against "liberation in 369" ("Messenia and the helots") and "Thebes invaded in 370/69" ("Spartan women and property"). As written, the sentence can be read as dating the freeing of Messenia to 371.
- (re-check) Self-test 4, answer: "his dates vary by centuries between authors" goes further than the body, which says only that Xenophon makes him contemporary with the Heraclids and Aristotle with the first Olympiad; "Herodotus already knew rival accounts of the laws' origin" is not in the body at all (the body cites Herodotus 1.65-66 for Lycurgus giving the laws, with no rival account).
- (re-check) Self-test 7, answer: "through heiresses (patrouchoi) and large dowries under partible inheritance (Politics 1270a)". In the body, partible inheritance is Hodkinson's explanation (Property and Wealth in Classical Sparta, 2000), not Aristotle's, so the citation to Politics 1270a credits Aristotle with Hodkinson's mechanism.
- (re-check) Self-test 9, answer: "Because a new law allowed only one king on campaign". The body says "after 506 only one king could lead an army" (Herodotus 5.75) and does not call it a new law.
- (re-check) Self-test 10, question: "Trace Spartiate numbers from 480 to the 240s". The body never dates Demaratus' figure to 480 ("Demaratus tells Xerxes Sparta has about 8,000 men").
- (re-check) Inconsistent italics: agoge is italic in the body ("The word <em>agoge</em> is not attested") but roman in the dispute box under "The agoge, the syssitia and the krypteia" ("much of Plutarch's agoge").

### 5.5

- Self-test 1, answer: "Athenaion Politeia 7.1 and Plutarch, Solon 17 say Solon kept only the homicide laws". The body cites only Athenaion Politeia 7.1 for the repeal; it cites Plutarch, Solon 17 for Demades' quip about blood.
- Self-test 2, answer: "a council of about 400" and "is unknown to Aristotle's Politics". The body gives "a council of 401 by lot" and says nothing about the Politics' silence.
- Self-test 6, answer: "driven in a chariot into Athens". The body says only "driven into the city"; no chariot.
- Self-test 7, answer: "most scholars regard it as a later construction". The body names Davison and West for that view against Merkelbach and Nagy; it does not say "most scholars".
- Cleisthenes, "The problem solved" paragraph: "the status of men of doubtful descent whom a review in 510 had threatened". The body nowhere dates a review to 510; the factions section mentions only fear of "a review of the citizen roll".
- Other laws and his poetry, last paragraph: "Fr. 5 states his principle: <blockquote>…</blockquote>" puts a blockquote inside a <p>, which the browser closes early, splitting the paragraph.
- (re-check) Self-test 1, answer: "Athenaion Politeia 7.1 and Plutarch, Solon 17 say Solon kept only the homicide laws." The body cites Plutarch, Solon 17 only for Demades' quip; the repeal is cited to Athenaion Politeia 7.1 alone. Also "homicide laws" (plural) against the body's "homicide law".
- (re-check) Self-test 2, answer: "a council of about 400" — the body says "a council of 401 by lot". The answer's "is unknown to Aristotle's Politics" is not stated in the body.
- (re-check) Self-test 6, answer: "driven in a chariot into Athens" — the body says only "driven into the city"; no chariot.
- (re-check) Self-test 7, answer: "most scholars regard it as a later construction" — the body names Davison and West for that view, Merkelbach defending a core and Nagy's model; it does not say "most scholars".
- (re-check) "The Heliaia and the right of appeal" / "Other laws and his poetry", paragraph on Solon's poetry: "Fr. 5 states his principle: <blockquote>I gave the people as much privilege as suffices.</blockquote> Herodotus barely treats Solon..." — a blockquote inside a <p> is invalid HTML; the browser closes the paragraph before the blockquote and leaves "Herodotus barely treats Solon ... father of democracy." as loose text outside any <p>.

### 5.6

- Self-test 1, answer: "Archilochus, Tyrtaeus, Mimnermus, Solon and Theognis". The body (section "The lyric age and its genres") lists the canon's exclusions as "Archilochus, Tyrtaeus, Solon and Theognis"; Mimnermus is not named there.
- Self-test 3, answer: "proved by Helen's choice of Paris over her family, and applied to the absent Anactoria, whom the speaker prefers to Lydian chariots and infantry". The body says only "taking Helen as proof" (and "Sappho's preference of the beloved to cavalry" later); Paris, the family, Anactoria and the Lydian chariots and infantry appear nowhere in the body.
- Self-test 4, answer: "as witness before the court of Time". The body says only "calls the black Earth to witness that he pulled up her boundary stones"; the court of Time is not in the body.
- Self-test 5: question "Name the four conditions usually cited"; the body says borrowed data "does not explain the leap" and that "three further conditions are usually cited", so the answer's first item (contact with Egyptian and Babylonian knowledge) is not one of the conditions the body counts.
- Self-test 7, answer: "That land and sea had once been mixed ... so that the earth undergoes long cycles of change". The body says only that he "inferred that the earth had once been mud"; mixing and cycles are not in the body.
- Section "The poets, in order", table: the heading says "in order" but Mimnermus (c. 630) is listed after Sappho and Alcaeus (c. 600).
- Same table, Alcaeus row: "fr. 6, 129, 332" gives no edition, where every other row names one (West, Voigt, PMG, PMGF).
- Section "The symposium as setting", first paragraph: a <blockquote> sits inside a <p> ("Alcaeus fr. 346 opens <blockquote>Let us drink. ...</blockquote> Theognis addresses ..."), which is invalid HTML; the browser closes the paragraph before the quotation and leaves the rest as loose text.
- (re-check) Self-test 1 answer lists "Archilochus, Tyrtaeus, Mimnermus, Solon and Theognis"; the body (section "The lyric age and its genres") names only "Archilochus, Tyrtaeus, Solon and Theognis" as excluded. Mimnermus is added by the answer.
- (re-check) Self-test 3 answer: "applied to the absent Anactoria, whom the speaker prefers to Lydian chariots and infantry". The body's account of fr. 16 mentions neither Anactoria nor Lydian chariots and infantry (only "Sappho's preference of the beloved to cavalry" in "What is new compared with epic").
- (re-check) Self-test 4 answer: "as witness before the court of Time". The body says only that fr. 36 "calls the black Earth to witness"; no court of Time.
- (re-check) Self-test 5: asks for "the four conditions usually cited" and the answer counts "Contact with Egyptian and Babylonian knowledge through trade" as one. The body says borrowed data "does not explain the leap" and that "three further conditions are usually cited".
- (re-check) Self-test 7 answer: "land and sea had once been mixed ... so that the earth undergoes long cycles of change". The body says only that he "inferred that the earth had once been mud".
- (re-check) Table "The poets, in order": the rows are not in date order (Mimnermus "c. 630" after Sappho and Alcaeus "c. 600"), though the heading says "in order".
- (re-check) Same table: the "Floruit" column holds life spans for Simonides "c. 556–468", Pindar "c. 518–438", Bacchylides "c. 520–450" and an office year for Solon "594/3 archon".
- (re-check) Same table: Alcaeus' anchor text "fr. 6, 129, 332" gives no edition, where every other fragment row names one (West, Voigt, PMG, PMGF).
- (re-check) Section "The symposium as setting": "Alcaeus fr. 346 opens <blockquote>…</blockquote>" puts a blockquote inside a <p>, which is invalid HTML; the browser closes the paragraph before the quote and leaves the following sentence ("Theognis addresses fellow drinkers; …") outside it.

### 6.1

- Self-test 1, answer: "funded by Persia". The body (Ionian Revolt section) says Aristagoras promised Artaphernes an easy conquest of Naxos and failed; it does not say Persia funded it.
- Self-test 3, answer: "having marched from Sparta in three days (Herodotus 6.106, 6.120)". The body says only that "Two thousand Spartans arrived after the full moon"; the three-day march is not stated.
- Self-test 6, answer: "He was recalled before Salamis and commanded at Plataea." The body says "The exiles were recalled before Xerxes arrived" and has Aristides arrive from Aegina at Salamis (8.79); it never says he commanded at Plataea.
- Self-test 10, answer: "and this applies to his whole work". The body gives the rule at 7.152 ("he must report what is said, not believe all of it") without that extension.
Self-test answers that state what the body does not:
- (re-check) Q1 answer: "funded by Persia" — the body (Ionian Revolt, para 1) says only that Aristagoras promised Artaphernes an easy conquest of Naxos and failed; no Persian funding is stated.
- (re-check) Q3 answer: "having marched from Sparta in three days" — the body (Marathon, para 3) says only "Two thousand Spartans arrived after the full moon"; the three-day march is not in the body.
- (re-check) Q6 answer: "He was recalled before Salamis and commanded at Plataea." — the body says "The exiles were recalled before Xerxes arrived" and has Aristides arrive from Aegina before Salamis, but never says he commanded at Plataea.
- (re-check) Q8 answer: "not the Acropolis palisade" — the body mentions the Acropolis "wooden barricade" (8.51–53) but never presents it as the rival reading of the oracle.
- (re-check) Q10 answer: "and this applies to his whole work" — the body (Herodotus: method, para 1) gives the rule at 7.152 but not its scope.

### 6.2

- Self-test 3, answer: "Euboea (446) and Byzantium (440) were lesser or concurrent revolts." The body mentions Euboea's revolt in 446 but never Byzantium's revolt of 440.
- Self-test 6, answer: "Its \"additional\" powers, probably the audit and vetting of magistrates and a general guardianship of the laws". The body's dispute box says reconstructions range from audit and vetting to *eisangeliai* and that Hignett doubted any formal guardianship; "probably" states more than the body.
- Self-test 7, answer: "Pericles obtained an exemption for his son by Aspasia". The body says Pericles "sought an exemption".
- Self-test 10, answer: cites "Protagoras 319", which the body never cites, and "Republic 488–489" where the body gives "488a–489a".
- Self-test 5, answer: "Ephialtes carried the Areopagus reforms in his absence". The body implies but does not state that the reforms passed while Cimon was at Ithome.
- Attribution of the *Athenaion Politeia*: "the *Athenaion Politeia* attributed to Aristotle" (The fifty years and their sources) against "Aristotle's text speaks only of 'additional powers'" (dispute box, Cimon, Ephialtes and the Areopagus) and "Aristotle's bare 'because of the number of citizens'" (Pericles and the reforms of the 450s).
- (re-check) Self-test 3, answer: "Euboea (446) and Byzantium (440) were lesser or concurrent revolts." The body mentions no revolt of Byzantium in 440; Byzantium appears only as the place where Pausanias disgraced himself.
- (re-check) Self-test 7, answer: "(Pericles obtained an exemption for his son by Aspasia)". The body says he "sought an exemption"; it does not say he obtained one.
- (re-check) Self-test 6, answer: "Its \"additional\" powers, probably the audit and vetting of magistrates and a general guardianship of the laws". The body's dispute box says reconstructions range from audit and vetting to hearing eisangeliai, and that Hignett doubted a formal guardianship existed; "probably" states more than the body does.
- (re-check) Self-test 10, answer: "(Republic 488–489, Protagoras 319)". The body cites Republic 488a–489a and 557a–564a and Gorgias 515e; it never cites Protagoras 319.
- (re-check) Attribution of the Athenaion Politeia: introduced as "attributed to Aristotle" (The fifty years and their sources), then given as "Aristotle's text speaks only of" (Cimon, Ephialtes dispute box) and "Aristotle's bare \"because of the number of citizens\"" (Pericles and the reforms of the 450s) without the qualification.

### 6.3

- "The Peace of Nicias and the rise of Alcibiades", second paragraph: "where King Agis won decisively and restored Spartan prestige (5.64–74). His extravagance made the Athenians suspect him of aiming at tyranny" — "His" now follows Agis, so the sentence about Alcibiades (6.15) reads as if about Agis. Dangling reference.
- Self-test 3, answer: "Thucydides says his successors did the opposite, pursuing private ambition and gain, above all in Sicily" — the body (2.65) says only that the plan "would have worked had Pericles' successors kept to it"; private ambition and Sicily as the example are not stated there. Also "use the fleet and reserve to outlast Sparta": the body names no reserve.
- Self-test 4, answer: "killing the demos would deprive Athens of the party inside every city that might open its gates" — the body gives Diodotus' point as "will teach every subject city that revolt has no exit". The answer also cites 3.42–48 where the body cites the speeches as 3.37–48.
- Self-test 5, answer: "contradicting the Thermopylae image of Spartans who never yield" and the citation 4.38–40 — the body mentions neither Thermopylae nor 4.38–40 (it cites 4.29–41). It also says "Lacedaemonian hoplites" where the body says "survivors".
- Self-test 10, answer: "King Pausanias, outflanking Lysander" — the body says Pausanias was "jealous of him"; minor difference of emphasis.
- (re-check) Self-test 3, answer: "use the fleet and reserve to outlast Sparta" — the body (Archidamian War section) gives "use the fleet to raid the Peloponnese and keep tribute flowing"; no financial reserve is mentioned. Same answer: "pursuing private ambition and gain, above all in Sicily" — the body says only that the plan "would have worked had Pericles' successors kept to it" (2.65) and "factional ambition after Pericles (2.65)"; "gain" is not in the body.
- (re-check) Self-test 4, answer: "killing the demos would deprive Athens of the party inside every city that might open its gates" — the body gives Diodotus' point as "killing the demos along with the oligarchs will teach every subject city that revolt has no exit". The answer states an argument the body does not. The answer also cites "(3.42–48)" where the body cites 3.37–48 and 3.45.
- (re-check) Self-test 5, answer: "contradicting the Thermopylae image of Spartans who never yield" — Thermopylae is not in the body, which says only "the first time Spartans had done so, a shock to Greece (4.29–41)". The answer cites 4.38–40 and says "Lacedaemonian hoplites"; the body says "292 survivors".
- (re-check) Self-test 7, answer: "500 Athenian colonists settled" — the body says "500 colonists planted (5.116.4)" without "Athenian".
- (re-check) Self-test 9, answer: "as a presiding prytanis" — the body says only "Socrates, presiding".

### 6.4

- Self-test 1 answer: "Dionysia in Elaphebolion (March/April)"; the body (Two festivals) says "Elaphebolion (late March)".
- Self-test 2 answer: "Training, costume, upkeep and victory feast of the chorus"; the body names training, costume and upkeep only, no victory feast. The same answer's "The state paid poet and actors" drops the body's "from 449" for actors.
- Self-test 3 answer: "only five of their ten tablets were drawn and counted"; the body says only "of their ten tablets only five were counted", and never says "ten judges" or ten tribal urns outright (it says "names from each tribe were sealed in urns").
- Self-test 4 answer: "Aeschylus: second actor, reduced chorus, primacy of speech"; the body (Theatre, masks, chorus) gives Aeschylus the second actor and "gave the lead to speech" only; "reduced chorus" is not in the body.
- Euripides section and Self-test 7: "nineteen plays survive: seven from the same school selection as the other two sevens, and the 'alphabetic' ten"; seven plus ten is seventeen, not nineteen.
- (re-check) Self-test 1 answer: "Dionysia in Elaphebolion (March/April)"; the body (Two festivals) says "Elaphebolion (late March)".
- (re-check) Self-test 2 answer: "Training, costume, upkeep and victory feast of the chorus"; the body names "training, costume and upkeep" only, no victory feast. The same answer's "The state paid poet and actors" drops the body's "from 449" for actors.
- (re-check) Self-test 4 answer: "Aeschylus: second actor, reduced chorus, primacy of speech"; the body (Theatre, masks, chorus) gives the second actor and "gave the lead to speech", not a reduced chorus.
- (re-check) Origins, first paragraph: "The Peloponnesians claimed both genres (1448a29–b2)." The citation names no work and follows a Herodotus reference (5.67), so it reads as Herodotus; it is the Poetics.
- (re-check) Aristotle's Poetics, second paragraph: "Golden and Nussbaum (<em>The Fragility of Goodness</em>, 1986) clarification" attributes the book to both; it is Nussbaum's alone, and Golden's work goes uncited.

### 6.5

- Self-test 3, answer: "fits a pattern Dover showed was modelled on Socrates' trial". The body (dispute aside after "Nomos, physis and fear") says Dover showed the impiety trials "rest on late evidence"; the "modelled on Socrates'" reading is given to "most scholars", not to Dover.
- Self-test 6, answer: "in the same respect, so inner conflict proves distinct parts". The body (Republic paragraph) says only "one thing cannot at once want and refuse the same object"; "in the same respect" and the inner-conflict inference are not in the body.
- Self-test 7, answer: "If the Form of Largeness is itself large, it and large things share a feature requiring a further Form, without end." The body ("Plato: Academy, dialogue, Forms") names "the regress Aristotle called the Third Man (132a to b)" but never states the argument.
- Self-test 8, answer: "the right amount for the situation, which may be extreme". The body says "courage is the right amount of fear for this situation"; it does not say the mean may be extreme.
- Self-test 10, answer: "Stilpo the Megarian, whose school's logic fed Stoic dialectic". The body credits Stilpo himself only with teaching apatheia and teaching Zeno; logic is credited to the school generally ("Stoic logic grew from this ground"). Acceptable, but the answer attributes to Stilpo's line what the body gives to Eubulides and Diodorus.
- Carry forward 1: "the Stoics by identifying nature with reason and law". Not stated in the body.
- (re-check) Self-test 3, answer: "fits a pattern Dover showed was modelled on Socrates' trial". The body ("Where sources disagree", after "Nomos, physis and fear") says Dover showed the impiety trials "rest on late evidence" and that "most scholars treat this one as fiction modelled on Socrates'"; the answer gives Dover the modelling claim the body gives to most scholars.
- (re-check) Self-test 7, answer: "If the Form of Largeness is itself large, it and large things share a feature requiring a further Form, without end." The body ("Plato: Academy, dialogue, Forms") names only "the regress Aristotle called the Third Man (132a to b)"; the argument's content is stated only in the answer.
- (re-check) Self-test 6, answer: "in the same respect" is not in the body, which says "one thing cannot at once want and refuse the same object (436b to 441c)".
- (re-check) "The trial of 399 and the death", second paragraph: "In 404 the Thirty under Critias killed perhaps 1,500 citizens; Critias and Charmides, Socrates' associates and Plato's relatives, were among them". "Among them" reads as among the 1,500 killed; the sense is among the Thirty.

### 6.6

- Self-test 5, answer: "members free and autonomous under their own constitutions". The body ("The Second Athenian League, 378–") says only "free and autonomous"; nothing about their own constitutions.
- Self-test 9, answer: "control of Thermopylae". The body says Philip "marched through Thermopylae" in 346; it does not say he took control of it.
- Self-test 2, answer: "commanding a Persian fleet with the satrap Pharnabazus". The body says "commanding a Persian fleet for Pharnabazus".
- Carry forward 2: "Theban dependence on two men". The body never states this dependence as such; it is an inference from the Thebes sections.
- Chaeronea paragraph: "perhaps 35,000 allied Greeks faced Philip's 30,000 foot and 2,000 horse" carries no citation of its own; the nearest citations are Plutarch, *Camillus* 19 (the date) and Diodorus 16.85–86 (the deployment).
- Heading "The Second Athenian League, 378–": the open en dash with no end date; every other heading closes its range.
- (re-check) Self-test 2 answer: "commanding a Persian fleet with the satrap Pharnabazus" — the body says "commanding a Persian fleet for Pharnabazus"; "with" implies joint command.
- (re-check) Self-test 5 answer: "members free and autonomous under their own constitutions" — the body says only "free and autonomous"; constitutions are not mentioned.
- (re-check) Self-test 6 answer: "the cavalry fought first" — the body says the cavalry drove the Spartan horse into their own infantry, not that it fought first.
- (re-check) Self-test 9 answer: "control of Thermopylae" — the body says Philip "marched through Thermopylae" in 346 (and was blocked there in 352); it does not state he controlled it.
- (re-check) Carry forward 1: "Thebes after 371 ... used a common peace guaranteeing it" — the body nowhere says Thebes used a common peace after 371.
- (re-check) Carry forward 3: "Diodorus' compression of Ephorus" — Ephorus is not mentioned anywhere in the body.
- (re-check) Heading "The Second Athenian League, 378–": open-ended range with a trailing dash, unlike every other dated heading.

### 6.7

- Self-test 1, answer: "Both served on the campaign, and Ptolemy, writing as a king, would in Arrian's view have found lying dishonourable." The body ("The sources problem") gives only Arrian's method (follow Ptolemy and Aristobulus where they agree, the more plausible where they differ); it never states that both served on the campaign or the reason that lying would be dishonourable for a king.
- Self-test 10, answer: "the infant Alexander IV, son of Roxane". The body ("Immediate legacy") says "Roxane was pregnant" at the settlement and the settlement "added Roxane's son as Alexander IV"; it never calls him an infant, and at the Babylon settlement he was not yet born.
- Inconsistent possessive: "by Chares' account" ("The sources problem") and "Xerxes' burning of Athens" (Persepolis aside) against "Curtius's date" (first aside), "Darius's cavalry", "Darius's successor", "Philotas's guilt".
- (re-check) "Bactria and Sogdiana", Roxane paragraph: "That Alexander's first marriage, at thirty, was to an Iranian" -- the body puts his birth in July 356 and the marriage in spring 327, which makes him 28, not thirty.
- (re-check) Self-test 1, answer: "Both served on the campaign, and Ptolemy, writing as a king, would in Arrian's view have found lying dishonourable." The body gives Arrian's method (follow them where they agree, the more plausible where they differ) but never states either reason given here.
- (re-check) Self-test 10, answer: "the infant Alexander IV" -- the body says only that Roxane was pregnant and that her son was "added" as Alexander IV; at the Babylon settlement in 323 he was not yet born, so "infant" is not in the body and sits awkwardly with "Roxane was pregnant".
- (re-check) Quotation marks: the body uses straight quotes ("the vulgate", "as a king", "reign of terror") while the figure captions use curly ones (“The sources problem”, “Immediate legacy”).

### 7.1

- Self-test Q2 answer: "Alexander's empty throne with diadem and sceptre" — the body (Eumenes paragraph) names only "Alexander's empty throne and diadem"; no sceptre.
- Self-test Q3 answer: "autumn 312 (Macedonian) or spring 311 (Babylonian reckoning)" — the body says only "counted from autumn 312 or spring 311"; it does not assign the two reckonings.
- Self-test Q6 answer: "The allies assigned it to Seleucus, but Ptolemy ... occupied it" and "producing six Syrian Wars" — the body says only that Ptolemy "kept Coele-Syria" and that the claim "poisoned the two dynasties for a century"; neither the allies' assignment nor six Syrian Wars is in the body.
- Self-test Q7 answer: "after Seleucus had killed Lysimachus at Corupedium in February" and the question's "a few months earlier" — the body says "at Corupedium in February 281 Lysimachus fell" and does not date the stabbing.
- "Antigonus took the diadem, gave his son one, and the other four followed" (Demetrius paragraph after figure 1): "the other four" are never named.
- (re-check) Self-test 2, answer: "Alexander's empty throne with diadem and sceptre". The body (section "Perdiccas, Antipater, Craterus and Eumenes, 323–316") says "Alexander's empty throne and diadem"; no sceptre.
- (re-check) Self-test 3, answer: "autumn 312 (Macedonian) or spring 311 (Babylonian reckoning)". The body gives "autumn 312 or spring 311" but does not tie either date to a reckoning.
- (re-check) Self-test 6, answer: "The allies assigned it to Seleucus" and "producing six Syrian Wars". The body says only that Ptolemy "kept Coele-Syria" and that the claim "poisoned the two dynasties for a century"; it states neither the allies' assignment nor six Syrian Wars.
- (re-check) Self-test 7, answer: "near Lysimacheia in 281, after Seleucus had killed Lysimachus at Corupedium in February" and the question's "a few months earlier". The body says "Lysimachus fell" (not that Seleucus killed him) and gives no year for Seleucus' death and no interval between the two events.
- (re-check) Diodotus' secession: the body twice says "around 250" (Seleucid section and "The far edge"), while the Seleucid dispute box gives "256 or 246". Not contradictory, but the far-edge section does not point to the alternative dates.

### 7.2

- Self-test 9, answer: "Good and evil consist in sensation; death ends sensation because the soul's atoms disperse". The body (Epicureanism, second paragraph) says the soul "disperses at death" and "where death is, we are not", but never states the premise that good and evil consist in sensation.
- Self-test 2, answer: "A 120-book catalogue of Greek authors and works arranged by genre, the first systematic bibliography, compiled at the Alexandrian Library." The body says "a 120-book catalogue of authors and works by genre, the ancestor of every bibliography"; it does not say "Greek", "first systematic" or that it was compiled at the Library. Minor.
- (re-check) Self-test 9 answer: "Good and evil consist in sensation; death ends sensation because the soul's atoms disperse" — the body never states that good and evil consist in sensation (it gives atomism and "where death is, we are not").
- (re-check) Self-test 3 answer: "introduced by Zenodotus" and "the vulgate still contains lines they rejected" — the body says Zenodotus "marked suspect lines with a horizontal stroke (the obelos)", not that he introduced it, and never uses "vulgate" (it says "the Iliad still contains lines its greatest ancient editor rejected").
- (re-check) Self-test 2 answer: "the first systematic bibliography, compiled at the Alexandrian Library" — the body says "the ancestor of every bibliography" and does not place the compiling in the Library.
- (re-check) Self-test 8 answer: "(wealth, pain, death)" — the body's list of indifferents is "health, wealth, pain and reputation"; death is not named.
- (re-check) "Science: measuring the world", Hero paragraph: "left the Pneumatica with its steam-driven aeolipile, temple automata and the Metrica" reads as if the Metrica were part of the Pneumatica.
- (re-check) Inconsistent citation form: "fr. 1 Pfeiffer" and "Epigram 28 Pf." in the same paragraph.

### 7.3

- Self-test 3, answer: "Gruen saw Rome borrowing a standard Hellenistic slogan in good faith." The body says Gruen held Rome "meant roughly what the Antigonids and Ptolemies had meant by it"; "in good faith" is not in the body.
- Self-test 5, answer: "By the lunar eclipse of 21 June 168". The body gives Pydna "on 22 June" and the eclipse "the night before"; it never states 21 June.
- Self-test 7, answer: "the forgery allegation appears only in Mithridates' letter in Sallust's Histories". The body names that letter as the source of the allegation but does not say "only". The same answer says the decree treats "its ratification by Rome as fact"; the body says "refers to the will's ratification as fact", without "by Rome".
- Self-test 10, answer: "kept the masses in order and magistrates honest (6.56)". The body (Why Rome won) says it "kept the masses honest and magistrates accountable".
- Self-test 6, answer: "fewer than 300 returned". The body says "fewer than 300 of the thousand were alive" at the release.
- Italics: the Self-test answers set titles and Greek terms in roman where the body italicises them: "Sallust's Histories" (7), "Plutarch, Sulla 26" (8), "OGIS 338" (7), "deisidaimonia" (10).
- Gods and ancestors: "Apollo in 431" is the one date in that list without a citation; Asclepius, the lectisternium and the Great Mother each cite Livy.
- (re-check) Self-test 3, answer: "Gruen saw Rome borrowing a standard Hellenistic slogan in good faith." The body says only that Rome "meant roughly what the Antigonids and Ptolemies had meant by it"; "in good faith" is not stated.
- (re-check) Self-test 7, answer: "treats the will and its ratification by Rome as fact". The body says the decree "refers to the will's ratification as fact"; "by Rome" is not in the body.
- (re-check) Self-test answers drop the italics the body uses for titles and terms: "OGIS 338" and "Sallust's Histories" (7), "Plutarch, Sulla 26" (8), "deisidaimonia" (10).
- (re-check) "Where sources disagree" under "The Achaean War and the sack of Corinth": "constituted the province in 27 BC" is the only date in the body carrying "BC"; every other date is bare.

### 7.4

- Self-test, Isagoge answer: "through Boethius' Latin translation it became the standard first logic text of the medieval West". The body says only "the *Isagoge* that became the medieval logic primer"; Boethius is not in the body.
- Self-test, first answer: "Colonia Laus Iulia Corinthiensis"; the body has "the colony Laus Iulia Corinthiensis". This is inconsistent naming, not an error.
- "The long ending", last paragraph: "Damascius, the last head of the Academy, and Simplicius went to the Persian court of Khusro I, returned under the peace of 532." An "and" is missing before "returned".
- "The long ending", dispute aside: "Tardieu's Harran thesis for Simplicius is widely cited and widely doubted." This reference dangles: Harran and the thesis are not introduced anywhere in the report.
- (re-check) "The long ending" section, last paragraph: "Damascius, the last head of the Academy, and Simplicius went to the Persian court of Khusro I, returned under the peace of 532." A conjunction is missing ("... Khusro I and returned under the peace of 532").
- (re-check) Self-test 8, answer: "Porphyry's introduction to Aristotle's *Categories*; through Boethius' Latin translation it became the standard first logic text of the medieval West." The body says only "the *Isagoge* that became the medieval logic primer"; it names neither the *Categories* nor Boethius.
- (re-check) Self-test 6, answer: "Both are in *On the Obsolescence of Oracles*". The body places the Pan story in *De defectu* (419b–d), but gives the question of why shrines have fallen silent to the three Delphic dialogues together ("debating why the oracle now answers in prose and why shrines have fallen silent"), not to *On the Obsolescence of Oracles* alone.
- (re-check) Self-test 1, answer: "Colonia Laus Iulia Corinthiensis"; the body writes "the colony Laus Iulia Corinthiensis". Inconsistent form of the name.
- (re-check) Figure 1 label: "Nero's “liberation” of Greece" uses curly quotes; the body writes "liberation" with straight quotes.

### 8.1

- "Where sources disagree" under "A religion with no name": "Burkert and Price treat ritual as primary" — Price is named nowhere else in the report and has no work or date (dangling reference).
- Self-test 2 answer: "Procession with garlanded animal, basket and water; lustral water and hand-washing" — water is given twice; the body's procession step carries the basket, and the water belongs to step 2 only.
- Self-test 6 answer: "by lot from all citizens (priestess of Athena Nike, IG I³ 35)" — the body says chosen by lot "from all Athenian women".
- Self-test 8 answer: "Birth (washing, waiting days per the Cyrene law)" — the body names no washing for birth, only that the woman pollutes the roof and those in the house for three days.
- Self-test 9 answer: "stood on or touched the cut pieces" — the body says only "sworn standing on the cut pieces".
- Spelling: "Asclepius's precinct" (State, deme, household, individual) beside "Asklepieia" (calendar table); "Heracles" (The Athenian year) beside "Herakleia" (table). Latinised and Greek transliterations mixed.

### 8.2

- Self-test 1, answer: "The seventh of each month, Apollo's birthday". The body says consultation "originally fell once a year on the seventh of the month Bysios, Apollo's birthday", and only later monthly; the answer drops the annual stage and makes every seventh "Apollo's birthday".
- Self-test 2, answer: "if not, consultation was refused". The body says only "if it failed to tremble, the day was unpropitious"; refusal is not stated, and the body's own story of a Pythia "forced to prophesy on a bad day" cuts against it.
- Self-test 4, question and answer: "Which three Herodotean responses did Croesus misread" ... "and the earlier test oracle". The body says Delphi answered the test "correctly" (1.46-49); nothing says Croesus misread it. The answer's "Croesus had failed to ask follow-up questions (1.91)" is not in the body, which gives only the empire-was-his-own and half-Median-Cyrus explanations.
- Self-test 9, answer: "which undercut Zuntz's denial that the tablets were Orphic". The body credits that turn to "the Pelinna finds, naming Bacchus, and the Olbia bone plaques", not to Hipponion.
- Self-test 10, answer: "its first attested worshippers are in Greek-speaking Cilicia and Commagene". The body has Plutarch's "Cilician pirates" and Antiochus I in Commagene but does not call Cilicia Greek-speaking or call these the first worshippers.
- Carry forward 1: "priority rights sold to cities". The body says promanteia was "the right of priority that Delphi granted to favoured states such as Chios"; sale is not stated.
- Carry forward 2: "the same person could be a Spartan king, an Eleusinian initiate and a Samothracian ring-wearer". The body gives no such person; its Samothracian Spartan is unnamed and not a king.
- "Orphism, the gold tablets and the Pythagoreans", dispute aside: "Bernabé and Graf and Johnston (2007)" reads ambiguously (double "and"); "Bernabé, and Graf and Johnston (2007)" would separate the authorities.

### 8.3

- Self-test 4, answer: "A race, usually a diaulos, run in helmet and shield". The body says flatly "a diaulos run in helmet and shield"; "usually" is a hedge the body does not give.
- Self-test 5, answer: "so Cynisca of Sparta could be Olympic victor in 396 and 392 BC without being present". The body says owners won "without competing in person" and does not say Cynisca was absent.
- Self-test 6, answer: "inscribed with warnings". The body says only that Pausanias "read their inscriptions and names the bribers"; it does not say what the inscriptions said.
- Self-test 7, answer: "(IG I3 131)". The body prints IG I<sup>3</sup> 131; the answer loses the superscript.
- Self-test 10, answer: "inscriptions and site evidence suggest contests continued into the fifth century". The body attributes the fifth-century claim to "Recent work on the Olympia inscriptions (Ebert, Sinn)"; "site evidence" is a looser gloss (the body's site evidence is the Phidias workshop still in use, which it does not tie to contests).
- "Prizes, rewards at home", Theagenes: "won Olympic boxing in 480 and pankration in 476" gives no BC, where the rest of the paragraph does (464 BC, 448 implied). Clear from context, but inconsistent.

### 8.4

- Self-test 1, answer: "without strength or memory" overstates the body, which says "without strength or, usually, mind" (Homeric psyche section).
- Self-test 3, question: "and what tells us about its function?" has lost its subject (e.g. "what detail tells us").
- Self-test 3, answer: "A fifth-century Attic oil flask ... deposited at graves": the body calls it "the characteristic fifth-century vessel" and shows women bringing offerings "to the stele"; it does not say Attic or that lekythoi were deposited at graves.
- Self-test 5, answer: "the tower of Cronus on the Isle of the Blessed" and "(Olympian 2.68–80)"; the body has "to the tower of Cronus and the Isle of the Blessed" and cites 2.56–80.
- Self-test 6, answer: "living judges were deceived by fine bodies, clothes and witnesses": the body gives no reason beyond "so scarred souls are seen naked"; the answer states what the body does not.
- Self-test 9, answer: "('where two winds blow', the bellows)": the body never explains the riddle as the bellows.
- Self-test 10, answer: "curse tablets were deposited in their graves": the body says in "graves of the untimely dead", one of the four categories, not all of them.
- Brasidas at Amphipolis: the quotation "enclosed his tomb, and sacrifice to him as a hero" mixes past and present tense without the elided "have ever since"; reads as a slip.
- (re-check) Self-test 3, question: "What is a white-ground lekythos and what tells us about its function?" is ungrammatical (missing subject, e.g. "what feature tells us"). Its answer adds "Attic" and "deposited at graves", which the body ("The characteristic fifth-century vessel is the white-ground lekythos") does not state.
- (re-check) Self-test 1, answer: "without strength or memory"; the body says "without strength or, usually, mind" (and the body's qualifier "usually" is dropped).
- (re-check) Self-test 5, answer: "the tower of Cronus on the Isle of the Blessed"; the body says "to the tower of Cronus and the Isle of the Blessed".
- (re-check) Self-test 6, answer: "living judges were deceived by fine bodies, clothes and witnesses" and the citation "523a–524a"; the body gives no such reason and cites "523a–527a".
- (re-check) Self-test 9, answer: "a smith's yard (\"where two winds blow\", the bellows)"; the body never mentions the bellows.
- (re-check) "Brasidas at Amphipolis": the quotation "enclosed his tomb, and sacrifice to him as a hero, with games and yearly offerings" has a tense break ("enclosed ... sacrifice"); the translation's "to this day" (or equivalent) appears to have been cut.
- (re-check) "Ghosts and the restless dead": "Oracles of the dead at Ephyra, Tainaron, Heraclea Pontica and Avernus are attested by Herodotus 5.92"; the Melissa story in 5.92 concerns the Thesprotian oracle (Ephyra) only, so the citation does not cover the other three sites.

### 8.5

- "Farm, agora, food, clothing, gymnasium", first paragraph: "sent 400,000 medimnoi of grain a year (Demosthenes 20.31–32), and The agora was market, court, cult-centre and gossip-exchange" — a sentence is spliced: "and" followed by a capitalised "The"; something is missing or the "and" is stray.
- "Marriage, dowry, the epikleros, divorce", first paragraph: "Demosthenes 59 (<em>Against Neaera</em>) 122 states the purposes: <blockquote>…</blockquote></p>" — a blockquote sits inside a <p>, which is invalid HTML; browsers close the paragraph before the quote and leave a stray </p>.
- Self-test 2: "interest paid at 18 per cent a year" — the body says "paid 18 per cent interest", without "a year".
- Self-test 10: "Because it corrupted the wife's loyalty and threatened the legitimacy of heirs" — the body gives only the threat to legitimacy ("because it threatened legitimacy"); the wife's loyalty is not stated there.
- "Slaves and metics", fourth paragraph: "he admits others thought slavery conventional and unjust (1253b20–23)" — cited without the book and chapter, where the unit elsewhere writes "1.3, 1253b"; inconsistent citation form.
- (re-check) "Farm, agora, food, clothing, gymnasium", first paragraph: "(Demosthenes 20.31–32), and The agora was market, court, cult-centre and gossip-exchange" — a sentence is spliced: dangling "and" followed by a capital "The".
- (re-check) "Marriage, dowry, the epikleros, divorce", first paragraph: "Demosthenes 59 (<em>Against Neaera</em>) 122 states the purposes: <blockquote>…</blockquote></p>" — a blockquote nested inside a <p>, which is invalid HTML (the browser closes the paragraph before the quote).
- (re-check) Self-test 10: "Because it corrupted the wife's loyalty and threatened the legitimacy of heirs" — the body says only that adultery "threatened legitimacy"; "corrupted the wife's loyalty" is not stated in the body.
- (re-check) Self-test 2: "interest paid at 18 per cent a year" — the body says "paid 18 per cent interest" without "a year".

### 9.1

- "Vase painting", Red-figure item: "Euthymides writes on one amphora, as never Euphronios." The boast is quoted without quotation marks or italics, so it reads as a garbled sentence; it needs to be marked as the inscription ("as never Euphronios").
- "Polykleitos and the canon": a `<blockquote>` sits inside a `<p>` ("Philo Mechanicus quotes him: <blockquote>Perfection comes about little by little through many numbers.</blockquote> The Doryphoros…"), which is invalid HTML; browsers close the paragraph before the quote, so the following sentences fall outside it.
- Self-test 5 answer: "known from quotations in Galen and Philo Mechanicus and from Pliny's notice". The body cites Pliny (34.55–56) only for listing the Diadoumenos, not for anything about the Kanon. The answer also says "probably the Doryphoros" where the body says "almost certainly".
- (re-check) Polykleitos and the canon: "Philo Mechanicus quotes him: <blockquote>Perfection comes about little by little through many numbers.</blockquote> The Doryphoros systematises..." The blockquote sits inside a <p>, which is invalid HTML: the browser closes the paragraph before the quote, so "The Doryphoros systematises ... his Diadoumenos." falls outside any <p> and the closing </p> is stray.
- (re-check) Self-test 5 answer: "known from quotations in Galen and Philo Mechanicus". The body has Galen report what the Kanon said ("Galen ... says it located beauty in the commensurability"), not quote it; only Philo quotes.
- (re-check) Self-test 5 answer: "probably the Doryphoros"; the body says "almost certainly the Doryphoros".
- (re-check) Vase painting, Red-figure: "Euthymides writes on one amphora, as never Euphronios." The inscription is given without quotation marks, so it reads as the report's own (ungrammatical) sentence rather than Euthymides' words.
- (re-check) Transliteration is mixed across the report (Kallimachos, Kallikrates, Polykleitos, Hephaistos, Peirithoos beside Phidias, Heracles, Dionysus). Each name is spelled the same every time it appears; the convention is not.

### 9.2

- "The slopes", last sentence: "The slope is a four-century sequence: tyrant's cult, democratic festival, Hellenistic royal gift, Roman private benefaction." The Peisistratid cult (sixth century BC) to the Odeon (AD 160–174) is about seven centuries, not four.
- "The Areopagus and the Pnyx", second paragraph: "this is the one place where you stand where the sovereign body stood" has a doubled "where" that reads awkwardly.
- Self-test 7 answer: "the archaeology shows no phase securely datable to 404/3" says more than the body, which says only that Homer Thompson tied the turn to the second phase, about 404/3, and that "others doubt the Thirty built anything".
- Self-test 3: the question asks for "two reasons"; the answer gives three ("No altar or priestess ... attested, Pausanias never calls it a temple, and the ancient cult image ... stayed in the Erechtheion").
- Self-test 4 answer cites "Pausanias 1.26.5–27.2"; the body cites "Pausanias 1.26.5–27.1" for the Erechtheion and "1.18.2, 1.27.2" for the Pandroseion.
- "Walking orders" table: "Hadrian's Library" (Day 2, midday) appears nowhere in the body; "Philopappos Hill" (Day 1, midday, two days) is called "the Hill of the Muses" in the body.
- Possessives of names in -s are inconsistent: "Pheidias's", "Ephialtes's", "Cleisthenes's", "Alkamenes's", "Theseus's" against "Euripides' lost Erechtheus" and "Pericles' speech of 431/0".
- (re-check) "The slopes", last sentence: "The slope is a four-century sequence: tyrant's cult, democratic festival, Hellenistic royal gift, Roman private benefaction." The sequence runs from the Peisistratids (sixth century BC) to the Odeon (AD 160–174), about seven centuries, not four.
- (re-check) Walking orders table, two-day plan, Day 2 midday: "Roman Agora, Tower of the Winds, Hadrian's Library; lunch in Plaka". Hadrian's Library is not described anywhere in the body; it is the only stop in the table with no section behind it (and the one-day "Skipped" row does not list it).
- (re-check) Self-test 7 answer: "the archaeology shows no phase securely datable to 404/3, and the later phases are themselves disputed". The body (Pnyx dispute box) says Thompson tied the turned bema to the second phase, about 404/3, and that "others doubt the Thirty built anything"; it does not state that the archaeology shows no phase securely datable to 404/3.
- (re-check) Self-test 10 answer: "Shaft Grave V dates to about 1550–1500 BC". The body dates the Mask, not the grave: "The Mask of Agamemnon, from Shaft Grave V ... dates to about 1550–1500 BC".
- (re-check) Self-test 3: asks for "two reasons" and the answer gives three ("No altar or priestess ... attested, Pausanias never calls it a temple, and the ancient cult image ... stayed in the Erechtheion").
- (re-check) Possessives of names in -s are inconsistent: "Pericles' speech of 431/0" and "Euripides' lost Erechtheus" against "Pheidias's direction", "Theseus's black sail", "Ephialtes's reforms", "Cleisthenes's Council", "Alkamenes's bronze".

### 9.3

- "Byzantium and the Arabic transmission", second paragraph: "Ibn Rushd (Averroes) wrote the commentaries that twelfth-century Toledo (Gerard of Cremona, Michael Scot) rendered into Latin". A dating problem, not a typo: Ibn Rushd died in 1198 and Gerard of Cremona in 1187, and Michael Scot's Toledo translations date from about 1217, so the Latin Averroes was early-thirteenth-century work. Figure 2's third step repeats the text ("twelfth century: Gerard of Cremona, Michael Scot"). If the text changes, the figure's note has to change with it.
- "The current wave", games paragraph: "puts Herodotus on a boat with the player, muddles its chronology freely." An "and" is missing before "muddles", so the sentence trails off.
- Self-test 3, answer: "for which there was no interest". The body says that Homer was known only by name and that myth did not travel this route. It does not mention a lack of interest.
- Self-test 7, answer: "The shaft graves at Mycenae date to the sixteenth century BC". The body gives no date for the shaft graves. It says only that the mask is "three centuries older than any possible Trojan War".
- Self-test 8, answer (Vernant): "the play concerns knowledge, fate and pollution". The body says "knowledge and pollution". "fate" is added.
- Self-test 10, answer: "rape by Neptune in Athena's temple". The body names Poseidon (rendered "Poseidon" throughout) and does not mention Athena's temple. The answer adds a setting the body does not state, and it mixes the Roman and Greek names.
- "Victorian schools" dispute box: "argued in modules 10.10 and 10.2". The cross-references are listed in descending order. Check that the numbers are right.

### 9.4

- Tyrtaeus and the Rhetra, two descriptions that do not match. Part A, question 5 says "Tyrtaeus fr. 4 (West) paraphrases it". Part C, question 1 says "Tyrtaeus in the seventh century is the first to quote it".
- "about" is dropped from a date. Part A, question 9 and Part C, question 3 say Theseus's cycle appears on vases "from about 510". Carry forward 2 says "Theseus in 510".
- Figures 3 and 4 (not a prose slip but worth a note): any figure that draws a model answer has to sit outside the collapsed `<details>`. That shows answer content before the reader opens the answer, which breaks the "Closed book" rule in "How to sit this exam".

### 10.1

- Self-test 1 asks "Which source first states that Thetis' son by a god would overthrow his father": the body calls Pindar, *Isthmian* 8.26–48, "The clearest statement", not the first; it also says "mightier than his father", not "overthrow".
- Self-test 9 asks "which later text makes the shade regret death" and answers *Odyssey* 11: the body never says the *Odyssey* is later than the *Aethiopis*.
- Self-test 10 cites "Plutarch, *Alexander* 15"; the body gives "15.8–9".
- "Pelion and Scyros": "who raises him with his wife Philyra". In Pindar Philyra is Chiron's mother (his wife is Chariclo); worth checking against *Nemean* 3.43.
- "Menis, Briseis, and the Shield": "Benoit de Sainte-Maure" is usually spelt "Benoît".

### 10.2

- "The sceptre: a genealogy of authority", para 1: "The authority is two steps from a god's forge". In the chain the paragraph has just given (Hephaestus, Zeus, Hermes, Pelops, Atreus, Thyestes, Agamemnon), Agamemnon is six hand-overs from the forge, and Pelops is three. The count does not match any reading of the chain.
- Self-test 7, answer: "In every *Odyssey* account (1.35–43; 3.254–312; 4.512–537; 11.405–434) Aegisthus kills him at a banquet". The body cites Book 11 only as 11.385–464 and never cites 11.405–434. It gives the banquet only for Proteus's account (4.512–537), not for "every" account; Zeus (1.35–43) and Nestor (3.254–312) are not said to place it at a banquet.
- Self-test 8, answer: "Odysseus returns disguised and tests Penelope". The body says only "Odysseus does everything he did not"; it does not mention disguise or testing Penelope.
- Self-test 2, answer: "the *wanax* is the palace ruler with the largest *temenos*". The body says his *temenos* is "three times that of the *lawagetas*" (PY Er 312), not that it is the largest.
- (re-check) Self-test 7, answer: "In every *Odyssey* account (1.35–43; 3.254–312; 4.512–537; 11.405–434) Aegisthus kills him at a banquet". The body gives the banquet only in Proteus's version (4.512–537), and cites the Hades scene as 11.385–464, not 11.405–434; the reference 11.405–434 appears nowhere in the body.
- (re-check) Self-test 8, answer: "Odysseus returns disguised and tests Penelope". The body says only "Odysseus does everything he did not"; it never states the disguise or the testing of Penelope.
- (re-check) Self-test 9, answer: "no name is attached to anyone at Mycenae". The body says narrower: "no Linear B tablet from Mycenae names a king".
- (re-check) Self-test 2, answer: "the *wanax* is the palace ruler with the largest *temenos*". The body says his *temenos* is "three times that of the *lawagetas*", not that it is the largest.
- (re-check) Inconsistent citation form: "Pindar (*Pythian* 11.22–25)" in the carpet paragraph against "Pindar (*Pyth*. 11.31–32)" in the following aside.
- (re-check) Section title "Iphigenia: four moral weights" while figure 1's caption says "five sources" (the Hesiodic *Catalogue* is the fifth); not an error, but the two counts sit side by side.

### 10.3

- Self-test 4, answer: "Hector admits it alone outside the gate, 22.99–107". The body ("Death and judgement") cites only 22.104 for this admission; the range 22.99–107 appears nowhere in the body.
- Self-test 5, answer: "Andromache, Hecuba, Helen (24.725–775)". The body gives the funeral as 24.719–804 and Helen's lament as 24.762–775; 24.725 is not cited in the body.
- Self-test 7, answer: "(16.440–457)". The body ("The allies") cites Hera's argument as 16.431–461.
- Self-test 8, answer: "the cowardly Phrygian slave in Euripides' Orestes". The body says "a cowardly Phrygian eunuch".
- Self-test 10, answer: "Through Iulus, identified with Aeneas' son Ascanius". The body calls Iulus "Aeneas' son Iulus" and names Ascanius separately (Forum of Augustus) but never states that the two are identified. The answer also cites "Divus Julius 6" where the body has 6.1.
- (re-check) Self-test 4 answer: "Hector admits it alone outside the gate, 22.99–107" — the body cites only 22.104 for this passage; the range 22.99–107 is not in the body.
- (re-check) Self-test 5 answer: "Andromache, Hecuba, Helen (24.725–775)" — the body gives the funeral as 24.719–804 and Helen's lament as 24.762–775; 24.725 does not appear.
- (re-check) Self-test 7 answer: "(16.440–457)" — the body cites Hera's argument as 16.431–461.
- (re-check) Self-test 8 answer: "the cowardly Phrygian slave in Euripides' Orestes" — the body calls him "a cowardly Phrygian eunuch".
- (re-check) Self-test 10 answer: "Iulus, identified with Aeneas' son Ascanius" — the body never states this identification; it names "Aeneas' son Iulus" and, separately, "Aeneas with Anchises and Ascanius".
- (re-check) "Are the Trojans foreign?", first paragraph: "Iris remarks that the allies are of \"many tongues\" (2.803–804; 4.437–438)" — the second citation is in the Book 4 battle narrative, not a speech of Iris; the attribution covers both references.
- (re-check) "Hecuba and Andromache after Troy": "Pausanias adds that she ended in Asia with Pergamus" — no passage cited (only 1.11.1 earlier in the same paragraph, for the three sons).

### 10.4

- Self-test 7, answer: "That he is the best of mortals in counsel and speech" — the body (Metis section, Odyssey 13.287–310) says only that she is best among gods for metis "as he is among mortals"; "counsel and speech" is not in the body.
- Self-test 8, question: "Why do Pindar's and Euripides' hostility to Odysseus converge" — subject and verb disagree ("hostility ... do"; "hostilities" or "does").
- Self-test 8, answer: "Euripides (<em>Hecuba</em>, <em>Trojan Women</em>, <em>Iphigenia at Aulis</em>) makes him the demagogue whose persuasion wins assemblies" — the body cites <em>Iphigenia at Aulis</em> (524) only for the insult "son of Sisyphus", not for Odysseus as demagogue.
- Self-test 10, question: "Dante's Ulisse" — the body never uses the Italian form "Ulisse" (it says "him"/Odysseus; Latin "Ulysses" elsewhere).
- (re-check) Self-test 5, answer: "Trojan girls, overheard by Greek spies, one of whom argues with Athena's prompting for Odysseus" — "one of whom" grammatically attaches to the spies; the body (Cyclic section) has one of the girls arguing.
- (re-check) Self-test 7, answer: "he is the best of mortals in counsel and speech, and she is famous among the gods for metis" — the body (13.287–310) says she is best among gods for metis as he is among mortals; "counsel and speech" is not in the body.
- (re-check) Self-test 8, answer: Pindar makes him "the man whose fame outran his deeds" — the body (Nemean 7) says his fame "exceeds his sufferings".
- (re-check) Self-test 8, answer: cites Euripides' "Iphigenia at Aulis" as making him the demagogue whose persuasion wins assemblies — the body cites Iphigenia at Aulis 524 only for the insult "son of Sisyphus".
- (re-check) Self-test 10: "Dante's Ulisse" — the body uses "Ulysses" for the Latin and later figure throughout and never "Ulisse".

### 10.5

- Self-test 1, answer: "first in the Cypria". The body says only that the Nemesis genealogy is "older and stranger", and its dispute box says "Whether the Cypria's Nemesis is older than the swan or a learned alternative to it cannot be decided"; it never says the Cypria is the first text to make Nemesis her mother.
- Self-test 6, answer: Plato, Republic 586c, says men fought over her eidolon "as Stesichorus says". The body quotes 586c only as "the eidolon of Helen, in ignorance of the truth"; the words "as Stesichorus says" are not in the body.
- Self-test 5, answer: "so no one can react". The body says the drug "is precisely what lets the room sit through the second story"; the answer's wording goes further than the body.
- Afterlives: "Pallinode" (H.D.'s part title) beside "Palinode" everywhere else. This is H.D.'s own spelling, so probably intended, but a reader could take it for a typo.

### 10.6

- Self-test 2, answer: "I would feel shame before the Trojans and the Trojan women with trailing robes" (6.442 = 22.105). The body's blockquote in Book 6 reads "I would feel deep shame before the Trojans..." and cites it as (6.441–442). The wording and the line reference differ.
- Self-test 4, answer: "Patroclus plays the role of Cleopatra." The body says only that Cleopatra "inverts the name Patroclus" (The three speeches of Book 9). It does not say Patroclus plays her role. "returns only when his own people are desperate" is also looser than the body's "when the enemy fired the city" and "returning too late, in 18, when the gifts are worthless".
- Self-test 7, answer: the sceptre oath is cited as (1.234–244). The body gives the sceptre image as (1.234–237), within the second attack (1.225–244).
- Self-test 8, answer: "the gap at the collarbone (22.322–325)". The body says "the gap at the throat (22.322–325)" (Book 16 mirrors Book 22).
- Self-test 9, answer: "Weaving a purple cloak and ordering a hot bath". The body says "she had been weaving and heating Hector's bath (22.440–446)". It mentions no purple cloak, and it says "heating" rather than "ordering".
- Blockquote order: in Book 9, (9.412–413) comes before (9.378) and (9.401). In Book 22, (22.304–305) comes before (22.262). Every other book lists its quotations in line order.
- (re-check) Self-test Q2 answer: "I would feel shame before the Trojans and the Trojan women with trailing robes"; the body quotes the same lines as "I would feel deep shame before the Trojans..." (Book 6 quotes, 6.441–442).
- (re-check) Self-test Q4 answer: "returns only when his own people are desperate ... Patroclus plays the role of Cleopatra". The body says only that Cleopatra's name "inverts the name Patroclus" and that Achilles returns "too late, in 18, when the gifts are worthless". It never says Patroclus plays Cleopatra's role.
- (re-check) Self-test Q8 answer: "(1.234–244)". The body gives the sceptre as 1.234–237 and the second attack as 1.225–244.
- (re-check) Self-test Q9 answer: "the gap at the collarbone (22.322–325)". The body says "the gap at the throat (22.322–325)".
- (re-check) Self-test Q10 answer: "Weaving a purple cloak and ordering a hot bath for Hector's return". The body says only "she had been weaving and heating Hector's bath (22.440–446)". "Purple cloak" and "ordering" are not in the body.
- (re-check) "How the seven books speak to each other", Book 6 sets up Book 22: "The maids who mourned Hector alive at 6.500". The Book 6 section (quote at 6.500) says "They mourned Hector in his house" and does not mention maids.
- (re-check) Inconsistent term: "a dance-floor" (Book 18 Shield paragraph, and figure 2) against "the dancing-floor" ("The Shield and the world outside").

### 10.7

- Self-test 4: "What does the simile at 8.523–531 do?" The body cites the simile as 8.523–524.
- Self-test 6: "Polyphemus' curse to Poseidon (9.528–535)". The body cites the curse as 9.534–535 only.
- Self-test 3: "Telemachus substitutes "speech" (<em>mythos</em>)". The body never gives the Greek word *mythos*.
- Self-test 7: "news of his son Neoptolemus' prowess". The body says only "news of Neoptolemus (11.538–540)"; "prowess" is not in it.
- Self-test 8: the question asks which lines "were suspected in antiquity". The answer gives only 11.602–604 and leaves out Aristarchus' athetesis of 11.568–627, which the body also reports as ancient.
- Self-test 9: "no background or suspense". The body says "everything foregrounded"; "suspense" is not in it.
- Self-test 5: "<em>Outis</em>/<em>mē tis</em>/<em>metis</em>". *Outis* first appears in the body at 9.502–505 ("abandons <em>outis</em> for <em>kleos</em>") without a gloss; the quote at 9.366 gives only "Nobody".
- Inconsistent italics: *kleos* is italic in "The Telemachy" ("good fame (<em>kleos</em>)"), "The Cyclops read in full" and "The ending", but roman in "Agamemnon and Achilles" ("kleos survives as a father's pleasure"), "Nostos against kleos" (body, four times) and Carry forward 3. *metis* is italic in the Cyclops section and in "Metis against bie", but roman in Carry forward 3 ("metis over bie").
- (re-check) Self-test 1, answer: "The cattle of Helios (1.8–9)". The body never cites 1.8–9; it cites the cattle at "1.7–9" (dispute in "An unreliable narrator?").
- (re-check) Self-test 3, answer: "Telemachus substitutes \"speech\" (<em>mythos</em>)". The body gives "speech" but never the Greek word <em>mythos</em>.
- (re-check) Self-test 4, question: "What does the simile at 8.523–531 do?". The body cites the simile as "(8.523–524)".
- (re-check) Self-test 6, answer: "Polyphemus' curse to Poseidon (9.528–535)" and "the late, solitary return". The body cites only 9.534–535, calls it "Polyphemus' prayer" without naming Poseidon as its addressee, and says "lose all his comrades", not "solitary".
- (re-check) Self-test 7, answer: "news of his son Neoptolemus' prowess". The body says only "news of Neoptolemus (11.538–540)"; "prowess" is not in it.
- (re-check) Self-test 8, answer: names only 11.602–604 as suspected in antiquity, while the body's dispute aside says Aristarchus athetised "the whole stretch from 11.568 to 627" in antiquity.
- (re-check) Inconsistent citation of Demodocus' first song: "(8.72–82)" in "Calypso, Nausicaa and the Phaeacians" and "(8.75–78)" in "Metis against bie".

### 10.8

- Self-test 5 answer: "Through the disputed line <em>Iliad</em> 2.558": the body gives the passage as "<em>Iliad</em> 2.557–8" (section "Ajax son of Telamon").
- Self-test 6 answer: "together with Polybius, Strabo and Plutarch, shows the practice was real". The body rests the historicity on the inscription alone ("so the practice was historical"). It cites Polybius and Strabo only for disputes over the tribute's origin and Plutarch for its end, not as proof that the practice was real.
- Self-test 10 answer: "This was Apollo's punishment for killing Priam at an altar." The body gives this as what Pindar says ("Pindar (<em>Paean</em> 6.112–20) says Apollo had sworn …"), not as fact.
- Self-test 7 answer: "whether its joke presupposes our <em>Iliad</em> (11.632–7) or an older traditional cup of Nestor". The dispute box frames Powell's view as the <em>Iliad</em> being "known in the West by about 720 BC" and gives no line reference. The link to 11.632–7 comes from the earlier Nestor paragraph. This is a small stretch, not an error.
- Locrian maidens dispute box: "which contradicts the claim that the rite went back to the Bronze Age". The body never makes that claim in so many words; it only says "For a thousand years, so the story ran". The reference is slightly dangling.
- (re-check) Self-test 5, answer: "Through the disputed line *Iliad* 2.558" — the body gives "*Iliad* 2.557–8 places his twelve ships beside the Athenians".
- (re-check) Self-test 6, answer: "together with Polybius, Strabo and Plutarch, shows the practice was real" — the body rests the historicity on the inscription alone ("so the practice was historical"); it has Polybius and Timaeus arguing over the tribute and Strabo dating its start to the Persian period, and does not say either shows it was real.
- (re-check) Self-test 10, answer: "This was Apollo's punishment for killing Priam at an altar." — the body gives this only as Pindar's version ("Pindar (*Paean* 6.112–20) says Apollo had sworn…"), not as the cause in Euripides' Orestes version too.

### 10.9

- Self-test, scales answer: "16.658: Hector recognises the turning of Zeus' sacred scales and flees." The body quotes only "recognised the sacred scales of Zeus" (16.658); "the turning" is not in the body.
- Inconsistent form: body "Heraclitus' Homeric Problems (first century AD)"; Self-test "Heraclitus (Homeric Problems, 1st century AD)".
- "The Deception of Zeus", dispute box: "Janko sets out the sacred-marriage parallels ..." and, three sentences later, "Janko (vol. 4, 1992) reads the episode as both comic and cosmological." The same scholar's view is stated twice; the second sentence partly repeats the first.
- "Thetis, pity and the limits of immortality": "told in module 4.1" is a cross-reference to another module; check that 4.1 is the module that tells the courtship and Themis' prophecy.
- Self-test, theomachy answer: "Homer makes gods into men"; the body gives "Homer makes his men gods and his gods men". The answer keeps only half the chiasmus.
- (re-check) "Where sources disagree" aside after the Deception of Zeus: Janko is named twice in one aside, first bare ("Janko sets out the sacred-marriage parallels and takes the demonstration ... seriously") and then with his reference as if new ("Janko (vol. 4, 1992) reads the episode as both comic and cosmological"); the two sentences say much the same thing.
- (re-check) Inconsistent form: body "Heraclitus' Homeric Problems (first century AD)" vs Self-test 10 "Homeric Problems, 1st century AD".
- (re-check) Self-test 4 answer: "every god will then want to save a favourite son"; the body (16.431–61 paragraph) says only "every god will want to save a favourite".

### 10.10

- "Schliemann's trench and Priam's Treasure" vs "The nine cities": the body says "The treasure belongs to Troy II, in the mid-third millennium BC (roughly 2500–2300 BC)", while the table dates Troy II "c. 2550–2250 BC". Self-test 3 repeats "c. 2500–2300 BC".
- Self-test 3 answer: "Taken from Berlin by Soviet forces in 1945". The body says only that "The treasure disappeared in 1945" and was "taken by a Soviet trophy brigade"; it never says it was taken from Berlin in 1945.
- Self-test 6 answer: "a large lower city (about 27 hectares, several thousand people)". The body says "the whole covering perhaps 27 hectares", meaning citadel plus lower city, not the lower city alone, and it gives "perhaps", not "about".
- Self-test 2 answer: "Coring has since shown that the coastline was much closer to the mound in the Bronze Age". The body (dispute box) says only that it "has been partly answered by geology", so the answer states the rebuttal more firmly than the body does.
- Dispute box under "Wilusa and Alaksandu": "belongs to module 10.3". This report is 10.10, so 10.3 is a sibling unit, not a module. The reference may be dangling or misnamed; check it.
- (re-check) Troy II dates disagree inside the report: the paragraph after the treasure timeline says "in the mid-third millennium BC (roughly 2500–2300 BC)" and Self-test 3 repeats "c. 2500–2300 BC", while the table in "The nine cities" gives Troy II as "c. 2550–2250 BC".
- (re-check) Self-test 3 answer: "Taken from Berlin by Soviet forces in 1945". The body says only "The treasure disappeared in 1945" and "taken by a Soviet trophy brigade"; it never says it was taken from Berlin in 1945.
- (re-check) Self-test 8 answer: "whom he treats as an equal \"brother\"" and "the nearest text to a Hittite-Ahhiyawan dispute over Troy". The body says Ahhiyawa's king is addressed as a "brother" in the Hittite texts generally, not in the Tawagalawa letter specifically, and nowhere calls it the nearest text to such a dispute.
- (re-check) "Troy in the Hittite texts", dispute box: "The Luwian-language question (Watkins on the Trojans' speech) belongs to module 10.3." Watkins appears nowhere else in the report; the cross-reference cannot be checked from this report.
- (re-check) Units of length: "about 6 km" and "about 90 m" (table) against "about 200 metres", "about 400 metres" and "nine or ten metres" in prose.

### 10.11

- Self-test 7, answer: "Eumaeus was a king's son kidnapped by Phoenicians and sold to Laertes." The body ("Slavery and the fate of captured women") says he was "carried off by a Phoenician slave-woman and sold to Laertes". The answer names a different agent than the body does.
- Self-test 7, answer: "Slavery was a fall in status, not a hereditary caste." The body says "Slavery is a fall in status, not an innate condition" and lists birth as a source of slaves ("Slaves come through capture, purchase and birth"). "Not a hereditary caste" sits awkwardly beside slavery by birth and is not what the body states. The same answer also gives "capture, trade and birth" where the body has "capture, purchase and birth".
- "Which world? The historicity debate", paragraph after figure 3: "Later archaeology also gave the eighth century texture: temples, colonial foundations like Scheria's, Phoenician traders". Scheria is the poem's fictional city (its walls and temples are cited from Odyssey 6.7–10 earlier), so archaeology cannot have supplied "Scheria's" foundation. The phrasing needs to say that Scheria resembles the colonial foundations archaeology found.
- Self-test 6, answer: "whether gift exchange can still contain violence" paraphrases the body's "whether goods can still buy back what violence has taken". The two are close but not the same claim. This is a minor point.

### 10.12

- Medieval Troy, para 2 and para 3: Lydgate's *Troy Book* is introduced twice, with the date in two forms: "Lydgate's <em>Troy Book</em> (1412–20) is Guido turned into English verse" and "John Lydgate's <em>Troy Book</em> (1412–1420), written for Henry, Prince of Wales, put Guido into some 30,000 English lines".
- Dares and Dictys: the papyrus is "P.Tebt. 2.268" in the body and Self-test 5 but "P.Tebt. 268" in the dispute box.
- Dares and Dictys dispute box: "the 'discovery' of the tin box"; the body says only "in a box in Dictys' tomb".
- Self-test 2 answer: "Rome is Trojan by descent but Italian by name"; the body says "Trojan by blood and Latin by name", and the same answer's first sentence says "called Latin".
- Self-test 6: asks for "three reasons"; the answer gives four.
- Self-test 9 answer: "It was taken from Berlin in 1945"; the body says only that it "vanished in 1945".
- Schliemann dispute box: "is argued in module 10.10. The Kolb–Korfmann quarrel over the lower town is in module 10.10": two cross-references to one module in consecutive sentences; worth confirming both belong to 10.10.
- (re-check) Self-test 2 answer: "Rome is Trojan by descent but Italian by name"; the body (Rome section) says "Trojan by blood and Latin by name", and the same answer's previous sentence says "called Latin".
- (re-check) Medieval Troy section: Lydgate's Troy Book is introduced twice, first as "Lydgate's <em>Troy Book</em> (1412–20) is Guido turned into English verse at four times the length", then as "John Lydgate's <em>Troy Book</em> (1412–1420), written for Henry, Prince of Wales, put Guido into some 30,000 English lines"; the date form also differs (1412–20 / 1412–1420).
- (re-check) Dares and Dictys: the papyrus is "P.Tebt. 2.268" in the body and Self-test 5 but "P.Tebt. 268" in the dispute box.
- (re-check) Dares and Dictys dispute box: "the 'discovery' of the tin box" refers back to a box the body calls only "a box in Dictys' tomb"; "tin" appears nowhere else.
- (re-check) Early modern section: "the medieval Achilles of Benoît, Guido and Lydgate, who kill Hector unguarded and send the Myrmidons against Troilus" makes the three authors the subject of "kill" and "send"; the Achilles of those texts is meant.
- (re-check) Self-test 6 asks for "three reasons" and the answer gives four.
- (re-check) Rome section and Self-tests 3-4 cite Suetonius differently: "Julius 39.2; Augustus 43.2", "Nero 38.2" in the body; "Julius 39; Augustus 43", "Nero 38" in the Self-test.

### 11.1

- Self-test 7, answer: "Demosthenes 2.17 on the pezetairoi" spells the term without the h; the body's list spells it "Pezhetairoi" (the body's "pezetairoi" in the Anaximenes/Theopompus aside is Theopompus' own usage, so the answer should follow the list).
- Self-test 1, answer: "Badian suspected it of being Alexander I's own propaganda". The body says Badian read "the murdered Persian envoys (5.17–21) and the warning before Plataea (9.44–45)" as the king's apologetics; it does not say he applied this to the Olympic episode of 5.22.
- Self-test 2, answer: "Until Philip II the uplands were semi-independent cantons." The body says the uplands had "kings of their own" and their loyalty was "negotiable"; "cantons" is the answer's own word, not the body's.
- Self-test 8, answer: "why did the seventh threaten Alexander" and "the powerful Attalus". The body never numbers Cleopatra as the seventh marriage (the table lists her last, without a count), and never calls Attalus powerful.
- (re-check) Spelling: the body uses "Pezhetairoi" (army list) and "pezhetairoi" (dispute aside), keeping "pezetairoi" only for Theopompus' own usage; Self-test 7's answer has "Demosthenes 2.17 on the pezetairoi", where the body (army list) says "Pezhetairoi ... Demosthenes mentions them by 349 (2.17)".
- (re-check) Self-test 8's answer says "A son by her could be presented as fully Macedonian and \"legitimate\", which undercut the son of the Epirote Olympias". The body gives only Attalus' prayer for a "legitimate" heir and calls Olympias "a Molossian princess"; "fully Macedonian" and "Epirote" are not in the body.
- (re-check) Self-test 2's answer: "Until Philip II the uplands were semi-independent cantons." The body says the highland kingdoms had "kings of their own" and that binding them was Philip's first achievement; "semi-independent cantons" is not in the body.
- (re-check) Self-test 5's answer: "the pottery dates"; the body says only "the pottery".
- (re-check) Formatting: in the Self-test, work titles are not italicised ("Politics 7.1324b", "Phoenix 1963", "Isocrates' Philippus"), and "Theophrastus HP 3.12.2" abbreviates the body's "Historia Plantarum".

### 11.2

- Self-test 5, answer: "shot the drivers and horses" and "passed through harmlessly to be dealt with in the rear". The body (Gaugamela, Course) says only "shot the drivers, and the infantry opened lanes for the rest (3.13.5–6)": no horses, nothing about the rear.
- Self-test 7, answer: "Weeks of noisy feints along the bank". The body (Hydaspes, Situation) says "night after night"; no duration in weeks is given.
- Self-test 8, answer: "allowed him to blockade both harbours, and let him use ship-mounted rams". The body (Tyre) says "Outnumbered, Tyre closed its two harbours"; it never says Alexander blockaded them.
- Self-test 9, answer: "question his figures for the army's size and train". The body (Logistics: Engels) says only "dispute many of his figures"; which figures is not stated.
- Self-test 3, answer: "reached Issus on Alexander's line of communication". The body says Darius "came down behind him at Issus"; "line of communication" is not in the body (a reasonable gloss, but an added claim).
- Table, Granicus row, Opponents column: Arrian's "20,000 horse, nearly 20,000 Greek mercenaries" is cited to 1.14.4, Diodorus' counter-figure carries no chapter; likewise Curtius and Diodorus at Gaugamela losses ("under 300 (Curtius), 500 (Diodorus)") carry no passage while the neighbouring figures do.
- (re-check) Self-test 5 answer: "shot the drivers and horses" and "passed through harmlessly to be dealt with in the rear". The body (Gaugamela, Course) says only "Agrianians and javelin men shot the drivers, and the infantry opened lanes for the rest"; horses and the rear are not in the body.
- (re-check) Self-test 7 answer: "Weeks of noisy feints" and "about 5,000 horse and 6,000 foot". The body says "night after night" (no duration) and the table gives "5,000 horse, 6,000 foot" without "about".
- (re-check) Self-test 8 answer: "That gave him command of the sea, allowed him to blockade both harbours". The body says only "Outnumbered, Tyre closed its two harbours"; a Macedonian blockade is not stated.
- (re-check) Self-test 9 answer: "question his figures for the army's size and train". The body says "Critics accept the framework but dispute many of his figures"; which figures is not stated.
- (re-check) Table, Hydaspes row, Decisive move: "while Coenus took the Indian horse from behind" states as fact what the Hydaspes dispute box calls contested ("Coenus' route is contested, round behind the Indian line or a direct attack on the Indian right").

### 11.3

- Self-test 2, answer: stray comma before the citation: "after some sixty years of independence, (Diodorus 16.40–51)".
- Self-test 2, answer: "He crushed the Phoenician revolt and burned Sidon (345)": the body says only that he "burned rebel Sidon in 345"; it does not mention a Phoenician revolt.
- Self-test 1, answer: "a royal inspector reporting directly to the king": the body says only "a real office of royal inspection"; "reporting directly to the king" is not in the body.
- Self-test 4, answer: "burn the crops and countryside to starve Alexander's army": the body says "burn the crops"; "countryside" and "to starve" go beyond it (the body's reason is that Alexander "was short of money and supplies").
- "The offers and Parmenion's remark" says the offer came "During the siege of Tyre", citing Plutarch, Alexander 29.7–8; the dispute box that follows says "Plutarch (Alexander 29.7–9) sets the exchange at Tyre in 331, after Egypt", i.e. not during the siege (332). The two statements disagree, and the Plutarch range differs (29.7–8 vs 29.7–9). Self-test 7 repeats "during the siege of Tyre".
- "Gaugamela and the Babylonian diary": "Astronomical Diaries I, year −330" is the astronomical year number (= 331 BC) and sits beside BC dates elsewhere in the report without explanation; a reader may take it as an error.
- (re-check) Self-test 2 answer: "after some sixty years of independence, (Diodorus 16.40–51)" has a stray comma before the parenthesis.
- (re-check) Self-test 2 answer: "He crushed the Phoenician revolt and burned Sidon (345)": the body says only "burned rebel Sidon in 345"; a Phoenician revolt is not stated.
- (re-check) Self-test 4 answer: "burn the crops and countryside to starve Alexander's army": the body says "burn the crops"; "countryside" and "starve" are not in it.
- (re-check) Self-test 5 answer: "where his greater numbers and cavalry could not deploy": the body says the plain "cancelled out his numbers"; cavalry is not mentioned there.
- (re-check) Self-test 1 answer: "a royal inspector reporting directly to the king": the body says "a real office of royal inspection"; "reporting directly to the king" is not stated.
- (re-check) Inconsistent naming: body "the Hall of a Hundred Columns" (Persepolis dispute aside) vs Self-test 8 "the Hundred Columns Hall".
- (re-check) Inconsistent citation: body "Plutarch, Alexander 29.7–8" (The offers and Parmenion's remark) vs the following dispute aside "Plutarch (Alexander 29.7–9)".

### 11.4

- Self-test 3, answer: "the sweating statue of Orpheus" and "the eagle at Gaugamela" are not in the body. Aristander's omens in "Piety in practice" are the lion seal, the bird at Gaza, the barley meal, the eclipse and the Jaxartes sacrifices.
- Self-test 8, answer: "like Prometheus' cave and Heracles at Aornos". The body (Dionysus as model) names only "like Heracles' failure at Aornos". Prometheus' cave is not in the body.
- Self-test 6, answer: "son of Amun-Ra". The body (Pharaoh and king of Babylon) says "son of Ra and of Amun". This is a small inconsistency.
- "The journey", first paragraph: "adds two reasons: the oracle was reputed infallible, and Perseus and Heracles had consulted it, and Alexander 'traced part of his birth to Ammon'". The sentence announces two reasons and then gives three clauses joined by "and", so the count is unclear.
- (re-check) Self-test 3 answer lists "the sweating statue of Orpheus" and "the eagle at Gaugamela"; neither appears in the body (Piety in practice names only the lion seal, Gaza bird, Alexandria barley, Gaugamela eclipse, Jaxartes).
- (re-check) Self-test 8 answer: "like Prometheus' cave and Heracles at Aornos"; the body (Dionysus as model) names only "Heracles' failure at Aornos". Prometheus' cave is not in the body.
- (re-check) Self-test 10 answer says Arrian's version "is better supported by the letter to Cleomenes ordering hero-shrines and by the votive relief"; the body says only that Arrian's "hero" "fits the Pella evidence". The letter is Arrian's own report, not independent support.
- (re-check) Self-test 2 answer: "lay badly wounded"; the body says "lay wounded".
- (re-check) Self-test 7 answer cites Herodotus 1.134 for "the Great King was not a god"; the body cites 1.134 for the scale of greeting only and gives the non-divinity uncited.
- (re-check) Self-test 6 answer: "son of Amun-Ra"; the body says "son of Ra and of Amun".
- (re-check) Siwa date: "In the winter of 332/1" (The journey) against "Siwa in 331" (Did he believe it?) and "the Siwa greeting of 331" (Carry forward). Not wrong, but the two forms sit side by side.
- (re-check) 324 section: "(Hyperides, <em>Against Demosthenes</em>; ...)" has no fragment or column number, unlike every other citation.

### 11.5

- "Breaking the old guard, 330–327" (heading) against Carry forward item 1, "Philip's men, bound by kinship, were broken in 330–328": the two ranges disagree, and the body has Coenus, the last of them at court, dying in 326.
- "Phrada: Philotas and Parmenion" names Parmenion's killers as "Cleander, Sitalces and Menidas" (Arrian 3.26.3–4); "After India" then says "executed Cleander, Sitalces and Heracon (Parmenion's killers)". Heracon is not among the killers named earlier, and Menidas is not accounted for.
- Self-test 3 answer cites "(Diodorus 17.80; Curtius 7.2)"; the body cites Arrian 3.27.4 and Diodorus 17.80.4 for these changes and never cites Curtius 7.2 for them. The answer also says "letters home were censored" where the body says "soldiers' letters were opened".
- Self-test 9 answer dates the executions "325–324"; the body gives no dates for them, only "Emerging from Gedrosia".
- Self-test 10 answer: "Dropped: proskynesis for Greeks and Macedonians"; the body says only "They dropped proskynesis for Greeks".
- Self-test 2 answer: "too dangerous to leave in command"; the body has Arrian judge it "unsafe to leave alive" a father whose son he had executed.
- Opis dispute box: "Plutarch's rhetorical <em>On the Fortune of Alexander</em> (329)": the bare "329" reads as a year (329 BC); it is presumably the Moralia page and could say so.
- (re-check) Self-test 3, answer: "(Diodorus 17.80; Curtius 7.2)". The body cites these changes to Arrian 3.27.4 and Diodorus 17.80.4. It does not cite Curtius 7.2 for them; it cites Curtius 6.7–7.2 only for the plot.
- (re-check) Self-test 9, answer: "the executions of 325–324". The body never dates the purge. It says only "Emerging from Gedrosia".
- (re-check) Self-test 10, answer: "proskynesis for Greeks and Macedonians". The body says only "They dropped proskynesis for Greeks".
- (re-check) Self-test 5, answer: "died in India of obesity and lice". The body has "died in India, obese and lice-ridden", which describes his state and does not give a cause of death.
- (re-check) "Opis, 324" dispute box: "Plutarch's rhetorical *On the Fortune of Alexander* (329)". The bare "(329)" reads as a year. It is a Moralia page (329), but nothing marks it as one.

### 11.6

- Self-test 5 answer: "helped end the Sogdian resistance" and "signalled that Iranian elites could join the ruling class" — the body says only that the marriage "tied the most powerful Bactrian family to the regime" and "made an Iranian woman the probable mother of the heir".
- Self-test 7 answer: "would balance Taxiles" and "fitted the image of royal magnanimity" — the body says Alexander "reconciled him with Taxiles"; neither balancing nor magnanimity is stated.
- Self-test 6 answer: "he records Eratosthenes' view that both were flattery" — the body gives Eratosthenes' verdict on the Nysa/Dionysus stories (and on Prometheus' cave), not on Heracles at Aornos.
- Self-test 2 answer: "Mutilation of the nose and ears" — the body has "his nose and ear-lobes".
- Assessment: "Achilles' shield at the Mallian town" — the body calls it only "the sacred shield from Troy"; Achilles is never named there.
- Assessment: "Persian court dress" — the body (Arrian 4.7.4) has "Median dress".
- Assessment: "Cleitus, Callisthenes and Coenus each voiced the Macedonian protest" — the body never describes a protest by Callisthenes (he appears only as possible propagandist for Didyma; the proskynesis crisis is mentioned without him). "Iranian cavalry" is likewise not in the body.
- Carry forward 1: "the first limit Alexander's own troops imposed on him" — the body says the Hyphasis was "the first point clearly beyond any Persian frontier", not that the refusal was the first such limit.
- Spelling: "Aria" (satrapy, lines in the first section) beside "Alexandria in Areia" — likely deliberate (the city's conventional name), but the two forms sit in one paragraph without comment.

### 11.7

- "A structural problem, not a gap", first sentence: "Every narrative of Alexander that survives was written at least 270 years after his death" conflicts with the table's Diodorus date "c. 60–30 BC" (60 BC is 263 years after 323 BC). Figure 1, drawn from the table, makes the gap visible.
- Self-test 3, answer: "Plutarch draws on both it and the Arrian tradition." The body never says this; it says only that Plutarch names "about two dozen" authors, plus letters.
- Self-test 7, answer: "Vespasian (AD 69/70)". The body gives "Vespasian after 69"; "69/70" is not in the body.
- "The Alexander Romance", dispute aside: "implying an early Iranian adoption, (Theodor Nöldeke, ..." has a stray comma before the parenthesis.
- (re-check) "A structural problem, not a gap", first sentence: "written at least 270 years after his death ... in June 323 BC". The table dates Diodorus "c. 60–30 BC", which at its earliest is about 263 years after 323 BC, so "at least 270" does not hold against the report's own table.
- (re-check) Self-test 3 answer: "Plutarch draws on both it and the Arrian tradition." The body never says this; it says only that he names "about two dozen" authors and, on the Amazon queen (Alexander 46), lists Cleitarchus alongside Aristobulus and Ptolemy.
- (re-check) Self-test 4 answer: "which shifts blame for the slaughter to Ptolemy's later enemy." The body (Ptolemy and Aristobulus) mentions no slaughter and no blame; it says only that Ptolemy "has Perdiccas attack without orders".
- (re-check) Self-test 7 answer: "Vespasian (AD 69/70)". The body says "Vespasian after 69"; "70" is not in the body.
- (re-check) "The Alexander Romance", dispute box: "the Syriac Romance". The list above it names only the Syriac "Alexander Legend (c. 630)", a different work, so "the Syriac Romance" has nothing in the body to refer to.
- (re-check) Same dispute box, punctuation: "implying an early Iranian adoption, (Theodor Nöldeke, ...) has been challenged" — comma before the parenthesis.
- (re-check) Possessives of names in -s are inconsistent: "Aristobulus's book" (Ptolemy and Aristobulus) against "Curtius' date", "Nearchus' voyage", "Darius' troops".
- (re-check) Figure 1 caption uses curly quotes and apostrophes ("Alexander’s", “The five surviving narratives”) where the body uses straight ones throughout.

### 11.8

- "What killed him", first paragraph: "All the accounts describe roughly twelve days of fever" sits beside the section headed "Eleven days in Daesius" (table, 18 to 28 Daesius) and Aristobulus' death "on 30 Daesius" (thirteen days). The count is not reconciled.
- "Eleven days in Daesius", table: no row for Daesius 23; the text does not say the day is missing from the sources.
- Self-test 2 answer: "Diodorus says it allowed worship as a god"; the body says "sacrifice as to a god" (Diodorus 17.115.6).
- Self-test 6 answer: "White hellebore was known to Greek medicine"; the body never gives the common name "white hellebore", only *Veratrum album*.
- Self-test 7 answer: "Arrian records the story but does not believe it"; the body says only that he records it "so as not to seem ignorant of it" (7.27.3).
- Self-test 8 answer: "The funeral carriage left Babylon in 321"; the body gives 321 for Ptolemy meeting it in Syria, not for its departure from Babylon.
- "The body", paragraph after the list of visitors: the possible ends of the tomb (270s, 365, 390s) carry no citation in the text ("Possible ends for the tomb are Aurelian's destruction ...").
- (re-check) Self-test 6 answer: "White hellebore was known to Greek medicine". The body names only "*Veratrum album*" ("known to Greek physicians") and never gives the name "white hellebore".
- (re-check) Self-test 8 answer: "The funeral carriage left Babylon in 321". The body says only "In 321 Ptolemy met it in Syria" and that building the carriage "took two years"; it does not date the departure from Babylon.
- (re-check) Self-test 7 answer: "Arrian records the story but does not believe it". The body says Arrian (7.27.3) "records the poison story only so as not to seem ignorant of it"; it does not state his disbelief.
- (re-check) Length of the illness: the heading is "Eleven days in Daesius" (table 18 to 28 Daesius), while "What killed him" says "roughly twelve days of fever" and the theory table "drink alone does not explain twelve days". The "roughly" covers it, but the two counts sit a few lines apart.

### 12.1

- Inconsistent title for the same work: "Fragments, testimonia…" has "<em>Commentary on Aristotle's Physics</em> 144.25–28"; "The Milesians…" has "<em>Commentary on the Physics</em> 24.26–25.1".
- Burkert first appears without a first name ("the dispute between Burkert and Zhmud"; "Burkert (<em>Weisheit und Wissenschaft</em>, 1962; English 1972)"); "Walter Burkert" is given only later, in the Derveni dispute. Zhmud never gets a first name or a work.
- Self-test 1 answer: "the frame of a material cause is his too" and "Thales left no words of his own": the body says Aristotle reads predecessors through "his own four causes" and "No Presocratic book survives", but never names the material cause or says Thales left no words.
- Self-test 7 answer: "so infinitely many stages are crossed in infinitely many moments": the body says only that Aristotle made "time divisible like distance" (233a21–31).
- Self-test 8 answer: "uncuttable, unchanging atoms": the body says "uncuttable ones" and that each atom "has the properties of Melissus' One", not "unchanging".
- Self-test 9 answer: "Both fault the absence of a working final cause": the body ties final causes only to the Empedocles objection ("hence final causes"); for Anaxagoras it says only that Mind is wheeled in "when at a loss".
- Self-test 10 answer: "shows Presocratic texts being read and cited within the fifth century": the body dates the commentator "about 400 BC or a little earlier", which does not establish the fifth century.
- (re-check) Inconsistent title: "Simplicius ... (<em>Commentary on Aristotle's Physics</em> 144.25–28)" in "Fragments, testimonia and the making of a canon", but "<em>Commentary on the Physics</em> 24.26–25.1" in the Anaximenes paragraph (and the figure 1 caption).
- (re-check) Self-test 10 answer: "shows Presocratic texts being read and cited within the fifth century"; the body dates the commentator "about 400 BC or a little earlier" and does not say "within the fifth century".
- (re-check) Self-test 7 answer: "so infinitely many stages are crossed in infinitely many moments"; the body says only that Aristotle made "time divisible like distance" (233a21–31).
- (re-check) Self-test 1 answer: "Thales left no words of his own"; the body says only "For Thales there is only Aristotle's guess at an argument" and "No Presocratic book survives".
- (re-check) Self-test 9 answer: "Both fault the absence of a working final cause"; the body ties final causes to the Empedocles objection ("hence final causes") but not to the Anaxagoras complaint ("wheels Mind in only when at a loss").

### 12.2

- Inconsistent title spelling: the Gorgias section heading and Self-test 4 write "On Not Being"; the paragraph under that heading gives Sextus' title as "On Not-Being, or On Nature". Choose one form.
- Self-test 2, answer: "Judgements about what will prove healthy or advantageous are settled by events" and "not everyone is a measure even of his own future". The body (177c–179b) says only that doctor or legislator judges these better than a layman, "so not everyone is a measure". The point about events and "his own future" is not in the body.
- Self-test 8, question: "the daimonion". The body calls it only "the sign"; the Greek term appears nowhere else in the report.
- Self-test 9, answer: "behaved while with him and went bad after leaving". The body (1.2.14–16, 1.2.39) says they "behaved well while with him, and left once they thought themselves his superiors"; it does not say they went bad after leaving.
- Self-test 6, answer: the Frogs "still treats him as the type of the talking intellectual". The body (1491–1499) has "treats sitting chattering beside Socrates as a fashion". This is a looser paraphrase, not a contradiction.

### 12.3

- Self-test 1, answer: "Stylometry measures closeness to that late style; the first group shows too little of it to be ordered" — the body ("a large first group whose internal order style cannot settle") never gives this reason.
- Self-test 2, answer: "the Tübingen case rests on the <em>Phaedrus</em> and on Aristotle's reports" — the body never ties the Tübingen case to the <em>Phaedrus</em> (its critique of writing is left to module 6.5); the body's Tübingen paragraph cites <em>Republic</em> 506d–e.
- Self-test 7, answer: "The ascent passes from one body to beauty in general and leaves the individual behind" — the body states only "Unlike the ascent, the palinode keeps the beloved"; the ascent itself is left to module 6.5.
- Self-test 8, answer: "whose pieces can be regrouped" — the body says only that the three "can change into one another".
- Carry forward 3: "The charioteer, the Demiurge and the receptacle, and the judgement of souls passed into" — "Demiurge" appears nowhere else (the <em>Timaeus</em> section says "The maker"), and the list's punctuation ("and the receptacle, and the judgement of souls passed") reads as a dangling clause; a comma is missing after "souls" or one "and" should go.
- (re-check) "Life, Sicily and the Academy", para 2: "The *Letter*'s digression (342a–344d) explains why Plato wrote no treatise: ... like light kindled from a leaping spark (341c–d)." The spark passage cited (341c–d) lies before the digression's stated range, yet is given as part of it.
- (re-check) Self-test 1, answer: "the first group shows too little of it to be ordered, so its priority rests on content." The body says only that style cannot settle the first group's internal order and that the short Socratic dialogues' priority is inferred from content; it does not give "too little of the late style" as the reason, and it speaks of the short Socratic dialogues, not the whole group.
- (re-check) Self-test 2, answer: "the Tübingen case rests on the *Phaedrus* and on Aristotle's reports." The body never ties the Tübingen case to the *Phaedrus* (it names Aristotle, Aristoxenus, Simplicius and Szlezák's reading of *Republic* 506d–e).
- (re-check) Self-test 5, answer: "The final argument shows soul cannot admit death while it exists" — "while it exists" is not in the body; and "many bodies ... many cloaks" where the body has "several".
- (re-check) Self-test 7, answer: "The ascent passes from one body to beauty in general and leaves the individual behind" — the body does not describe the ascent (it defers it to module 6.5).
- (re-check) Carry forward 3: "The charioteer, the Demiurge and the receptacle, and the judgement of souls passed into..." — "Demiurge" is never used in the body, which says "the maker"; the list's "and ..., and" reads as a slip.

### 12.4

- Self-test 7 asks "Give three readings of the productive intellect of *On the Soul* 3.5", but the answer's second reading is about the other intellect: "Averroes made the receptive intellect, too, one and separate for all humans." The body (dispute after "The biologist at Pyrrha and the soul") says the same, so the answer is faithful to the body; the question's wording is what is too narrow.
- Self-test 6 answer: "It moves as an object of love and thought moves those who desire it (1072b3)". The body says "as an object of desire and thought moves: it moves by being loved (1072b3)"; the answer swaps desire and love. Small, but it is not the body's wording.
- Self-test 9 answer cites "(1254b27–1255b4)" as one range; the body gives two passages, "1254b27–1255a1" and "1255a3–b4".
- Quotation marks: the body uses straight quotes ("golden river of speech", "exoteric", "master of those who know", "Roman Aristotle"), while the figure captions use curly quotes (“The life beyond the outline”). One style throughout would be cleaner.
- (re-check) Self-test 2, answer: "Eudemus' request to Theophrastus for a sound text of the <em>Physics</em>". The body (dispute after the Scepsis section) says "a sound text of a passage of the <em>Physics</em>"; the answer widens it to the whole work.

### 12.5

- "The Megarians and dialectic", Stilpo paragraph: "Demetrius Poliorcetes, who took Megara in 307" has no era; every other date in the report gives BC ("around 300 BC", "328–325 BC", "about 350–340 BC").
- Self-test 3, answer: "but the oracle story looks like an aetiology of the slogan." The body never calls the oracle version an aetiology or links it to a slogan; it only lists the version (6.20–21) and, separately, the defacing of the currency at 6.71.
- Self-test 3, answer: "the <em>Pordalus</em> has Diogenes confess" drops the body's hedge, "Diogenes is said to confess it in his <em>Pordalus</em>".
- Self-test 7, answer: "If so, systematic Cyrenaic hedonism is third-generation" is an inference the body does not state.
- Self-test 9, answer: "It isolates what logicians now call an opaque context." The term is not in the body, which says only "Identicals cannot always be swapped after 'know'."
- Self-test 8, answer: "life and death are indifferent"; the body says "equally choiceworthy" (2.94–96). Close, but not the body's wording.
- (re-check) Self-test 3, answer: "The coins confirm that Sinope's currency was tampered with" is stronger than the body, which says only that debased Sinopean coins of about 350-340 BC "led Branham (1996) and Navia (2005) to give the story a historical core".
- (re-check) Self-test 3, answer: "the oracle story looks like an aetiology of the slogan" refers to a slogan the body never names as such (the nearest is "To deface the currency is to give custom less authority than nature (6.71)"), and the body does not call the oracle story an aetiology.
- (re-check) Self-test 9, answer: "It isolates what logicians now call an opaque context" uses a term the body does not give (the body says "Identicals cannot always be swapped after 'know'").
- (re-check) Self-test 7, answer: "systematic Cyrenaic hedonism is third-generation" is an inference the body does not state in those words (the body has the grandson, "mother-taught" by Arete, first defining the end).

### 12.6

- Self-test 5, answer: "so happiness depends on satisfying the first and dropping the last" states a conclusion the body does not. The body gives only KD 15 ("Nature's wealth is limited and easy to get, the wealth of empty opinion unlimited") and SV 33. The answer's "empty desires have no limit" also rewords the body's "the wealth of empty opinion unlimited".
- Self-test 8, answer: "the gods, death, the limit of pleasure, the endurance of pain" assigns topics to KD 1–4. The body says only "The four clauses follow KD 1–4 in order", and never gives the content of KD 4.
- "Samos, Lampsacus and the Garden": the section gives Module 7.2's "(341–270)" and then "He died of a kidney stone in 271/0" without remarking on the different death dates. Both are sourced, but the reader is left to reconcile them.
- "The sources" paragraph: "such as <em>On Piety</em>, <em>On Signs</em> (PHerc. 1065) and <em>On Death</em> (PHerc. 1050)" gives no PHerc. number for <em>On Piety</em> while its neighbours have one.

### 12.7

- Self-test 8 answer: "Pleasure is only a by-product, so it cannot be the natural end, as Epicurus claimed." The body (Chrysippus: oikeiosis and the end) makes pleasure "the Epicurean first object" and a by-product of the first impulse; it does not say Epicurus made it the natural end, nor argue from by-product to "not the end".
- Stobaeus references mix systems: "Stobaeus (2.75–76)" and "Stobaeus 2.76" (Chrysippus: oikeiosis and the end; Diogenes of Babylon and Antipater) against "an epitome of Stoic ethics usually credited to Arius Didymus (2.7)" (The sources). 2.7 reads as a chapter, 2.75–76 as pages; a reader checking citations is not told which.
- Quotation marks: the table has Diogenes "of Babylon" and the body "Dion has died", "up to us", "Middle Stoa" in straight quotes; the figure captions use curly “ ”.
- (re-check) Figure 2 caption: "Justice and the community of rational beings (3.62–64), which the text reaches ... is left out." Plural subject with singular verb; "are left out".
- (re-check) Self-test 8 answer: "Pleasure is only a by-product, so it cannot be the natural end, as Epicurus claimed." The body ("Chrysippus: oikeiosis and the end") calls pleasure "the Epicurean first object", not the end; the answer states more than the body does.
- (re-check) Self-test 1 answer: "kept its substance" where the body says "kept its things" (paraphrase; harmless but not the body's words).

### 12.8

- Self-test 3, answer: "They answer the charge that a sceptic who withholds assent cannot act, by offering a guide to action that claims no truth." The body never says Carneades' grades answer the inaction charge; it gives the grades (Against the Mathematicians 7.166–189) and, separately, Plutarch's reply for Arcesilaus (Against Colotes 1122a–d) and Clitomachus' assent "given to the persuasive in action".
- Self-test 5, answer: "which made him, Cicero says, nearly a genuine Stoic (2.132)". The body has "but for a very few changes, a most genuine Stoic"; "nearly" turns Cicero's "most genuine, with few changes" into "not quite".
- Carry forward 2: "Through the Latin <em>Outlines</em> of 1562 it returned to Montaigne and Descartes." The date 1562, Montaigne and Descartes appear nowhere in the body and have no source.
- Carry forward 3: "it passed into Christian theology through the pseudo-Dionysius and into Arabic and Latin philosophy through the <em>Theology of Aristotle</em> and the <em>Book of Causes</em>". None of these is in the body; unsourced.
- Section "Clitomachus, Philo and Antiochus": "His pupil Antiochus of Ascalon read them" depends on the preceding paragraph (Philo, the Roman Books); figure 2 as placed sat between them (moved in verdicts).
- Spelling: "Khusro I" (body, dispute aside) against "Khosroes" in Priscian's title "Solutions to the Problems Raised by Khosroes"; probably deliberate (a title), but the reader meets two forms of one name.
- (re-check) Self-test 3, answer: "They answer the charge that a sceptic who withholds assent cannot act, by offering a guide to action that claims no truth." The body gives Carneades' grades (Against the Mathematicians 7.166–189) but never says they answer the inaction objection; the only reply to that charge in the body is Plutarch's, for Arcesilaus (Against Colotes 1122a–d).
- (re-check) Self-test 5, answer: "which made him, Cicero says, nearly a genuine Stoic (2.132)". The body has "Cicero calls him, but for a very few changes, a most genuine Stoic"; "nearly" alters the reported words.
- (re-check) Self-test 1, answer: "The manuscripts make the indeterminacy of things the reason"; the body says "the nature of things". Minor wording drift.
- (re-check) Carry forward 2: "Through the Latin Outlines of 1562 it returned to Montaigne and Descartes." Neither the 1562 edition nor Montaigne or Descartes appears in the body, and the sentence carries no source.
- (re-check) Carry forward 3: "through the pseudo-Dionysius and into Arabic and Latin philosophy through the Theology of Aristotle and the Book of Causes" is not in the body and is unsourced.
- (re-check) Carry forward 1: "Iamblichus' answer made the last pagan schools communities of cult as well as of study" goes beyond the body, which does not say this.

