# Corrections pass, 30 October 2026 (P54, Rome; P59, Greece)

The Prose and Self-test leads the figure checkers noted (`p43-rome-notes.md`, N4 and P57; `p43-greece-notes.md`, N5) were leads, not verified errors. For each report with leads, one fresh Opus 5.5 agent saw only the report, its leads, `AGENT-SPEC.md` and `WRITER-BRIEF.md` and decided for each lead whether it was real and the smallest exact replacement that fixed it (a Self-test answer that said more than the body was fixed in the answer, never by adding to the body; a lead needing an outside source was checked with search, and left if search could not settle it; a lead repeated by the re-checker counted once). A second fresh Opus 5.5 agent per report, not shown the first one's reasons, checked each replacement against the report: PASS or FAIL. Only PASSes were applied, as exact replacements, then `check.py` (no HARD line) and `register.py` with each report's model unchanged. No figure was changed by this pass.

Counts: Rome 28 reports, 32 fixed, 2 proposals failed the check, 8 leads not real or out of scope, 0 unsettled. Greece 78 reports, 394 fixed, 27 failed the check, 91 not real or out of scope, 6 unsettled.

Each line below gives the lead (shortened), then for a fix the text replaced and its replacement (both shortened), and for a lead left the reason.

### Rome 0.2 (words 2,751, unchanged)

- **Fixed.** Self-test answer 10 repeats 'The battle of c. 496 in which Rome beat the Latins and the Tarquins' and ends 'on its side..' with a double full stop. `The battle of c. 496 in which Rome beat the Latins and the Tarquins The battle of c. 496 in which Rome beat the Latins …` → `The battle of c. 496 in which Rome beat the Latins and the Tarquins (Livy 2.19–20); in Dionysius (6.13) Castor and Poll…`

### Rome 1.5 (words 3,395, unchanged)

- **Fixed.** Self-test 3 adds Servius to the regal names unused in the Republic; the body (Cornell) names Numa, Tullus and Ancus. `Cornell notes that Numa, Ancus, Tullus and Servius are archaic names` → `Cornell notes that Numa, Tullus and Ancus are archaic names`

### Rome 1.6 (words 2,859, unchanged)

- **Fixed.** Self-test 8 'before the fifth-century Volscian advance' vs body's 'fit the sixth century, not the fourth' `which fits before the fifth-century Volscian advance.` → `which fits the sixth century, not the fourth.`

### Rome 2.1 (words 2,789, unchanged)

- **Fixed.** Self-test 5 dates Livy 43.13 to 169; the body says only "that year". `In 169 one was refused because it happened on private ground` → `One was refused because it happened on private ground`

### Rome 2.2 (words 3,377 → 3,380)

- **Fixed.** Mars paragraph: 'Seated with Venus in 217, Ares' adultery became…' is a dangling participle `Seated with Venus in 217, Ares' adultery became Rome's genealogy` → `Once Mars was seated with Venus in 217, Ares' adultery became Rome's genealogy`
- **Fixed.** Same fault in Self-test answer 6: 'Seated with Venus in 217, the Odyssean adultery became…' (not a separate lead; found while fixing lead 1) `Seated with Venus in 217, the Odyssean adultery became` → `Once Mars was seated with Venus in 217, the Odyssean adultery became`
- **Left (not real).** Vesta paragraph: 'kept the form of a hut, was no inaugurated templum' lacks a conjunction It is a three-part list of predicates, 'kept the form of a hut, was no inaugurated templum (Gellius 14.7.7) and had no image', with the conjunction before the last item as usual.

### Rome 2.3 (words 2,864, unchanged)

- **Fixed.** Rex sacrorum 'fled the Forum' in the body, 'fleeing the Comitium' in Self-test 2. `fleeing the Comitium after his sacrifice` → `fleeing the Forum after his sacrifice`

### Rome 2.4 (words 2,849 → 2,852)

- **Fixed.** Self-test 4 places the Penates in the salt-cellar, which the body does not mention `present in hearth, table and salt-cellar;` → `present in hearth and table;`
- **Fixed.** "Servius says" in "The Lares" gives no passage `usually shown, Servius says, as a serpent;` → `usually shown, Servius says (on <em>Aeneid</em> 5.95), as a serpent;`

### Rome 2.5 (words 2,736, unchanged)

- **Fixed.** Self-test 4 calls the Galli "Phrygian"; the body does not. `but her eunuch Galli were Phrygian and citizens were barred by law and decree from joining their procession or rites` → `but citizens were barred by law and decree from joining the procession or rites of her eunuch Galli`

### Rome 3.2 (words 2,759, unchanged)

- **Fixed.** Self-test 6 cites Livy 8.9.6–9 for the devotio, the body 8.9.6–8. `devotes the enemy's legions with himself to the gods below; then, veiled, in the purple-bordered toga girt in the Gabin…` → `devotes the enemy's legions with himself to the gods below (8.9.6–8); then, veiled, in the purple-bordered toga girt in…`
- **Left (not real).** Self-test 8 cites Dionysius 8.55–56 for the temple of Fortuna Muliebris, the body 8.56.2. Different claims: Dionysius 8.55 narrates the women's request, the senate's decree and the temple's dedication, 8.56 the speaking statue (body's 8.56.2); 8.55–56 is right for the temple as commemorat…

### Rome 3.4 (words 2,822, unchanged)

- **Fixed.** Self-test 1 cites Livy 10.11–12 for 298, where the body cites module 0.1 and gives no Livy passage `the Scipio Barbatus epitaph contradicts Livy 10.11–12 on 298.` → `the Scipio Barbatus epitaph contradicts Livy's provinces for 298.`
- **Fixed.** Self-test 6 has the Senate uphold the exemption only for Antium and Ostia in 207, which the body does not state `who claimed exemption from the legions; in 207 the Senate upheld the claim only for Antium and Ostia (Livy 27.38).` → `who still claimed exemption from the legions in 207 (Livy 27.38).`

### Rome 4.1 (words 2,800, unchanged)

- **Fixed.** Self-test 1 says Appian put the foundation "before the Trojan War"; body says "before the fall of Troy" `Appian put it before the Trojan War.` → `Appian put it before the fall of Troy.`

### Rome 4.2 (words 2,842, unchanged)

- **Fixed.** Self-test 9 says "the fleet of 242", a year the body does not give `How was the fleet of 242 paid for` → `How was Rome's last fleet paid for`
- **Fixed.** Self-test 8 says Hamilcar held out "six years", against the body's three at Heircte and two at Eryx `From Heircte and then Eryx he held out for six years,` → `He held Heircte for three years and Eryx for two more,`
- **Left (not real).** Self-test 7 cites Polybius 1.37.4–6, the body 1.37.1–4 The two ranges cite different claims and both are right: 1.37.1–3 the storm, the 80 survivors of 364 and the greatest disaster, 1.37.4–6 the commanders ignoring the pilots' warnings (Polybius 1.37, P…

### Rome 4.5 (words 2,830, unchanged)

- **Fixed.** Self-test 10 gives Cato's fear as the young prizing eloquence over deeds; the body (Cato Maior 22) gives a different reason. `Cato feared that the young would prize eloquence over deeds and urged the Senate to send them home (Plutarch, <em>Cato …` → `Cato urged the Senate to send them home quickly, so that Roman youth would listen to the laws and magistrates as before…`

### Rome 5.3 (words 2,740, unchanged)

- **Fixed.** Self-test 2 says Appian gives 70,000 and then 120,000; the body has only about seventy gladiators and 120,000. `Appian gives 70,000 and then 120,000,` → `Appian gives 120,000 foot,`

### Rome 5.4 (words 3,218, unchanged)

- **Fixed.** Self-test 6 hedges the Pharsalus figures ("about 15,000", "some 200") that the dispute box gives without a hedge. `Caesar claims about 15,000 Pompeians killed and more than 24,000 surrendered for a loss of some 200 men` → `Caesar claims 15,000 Pompeians killed and more than 24,000 surrendered for a loss of 200 men`

### Rome 5.6 (words 2,826, unchanged)

- **Fixed.** Atticist dispute box: "Lysias' plainness.." (double full stop). `wanted Lysias' plainness.. Cicero replied` → `wanted Lysias' plainness. Cicero replied`

### Rome 6.3 (words 3,334, unchanged)

- **Fixed.** Self-test 6 gives 'loyalty' as a theme of Odes 3.2; the body names only military hardiness. `military virtue and loyalty (3.2.13)` → `military hardiness (3.2.13)`
- **Fixed.** Syme's chapter title 'The Organization of Opinion' beside 'organisation of opinion' later. `Syme's "organisation of opinion"` → `Syme's "organization of opinion"`

### Rome 7.1

- **Left (not real).** Philo, Embassy to Gaius, cited 8–21 in the body and 14–21 in Self-test 5 Both ranges are right for what each cites: the body's 8–21 covers the accession, the seven golden months (to 13) and the illness and recovery; Self-test 5 cites only the illness of the eighth month a…

### Rome 7.2 (words 2,734, unchanged)

- **Fixed.** Self-test 1 says Vespasian was proclaimed in "Alexandria and Judaea"; the body says "Egypt and Judaea". `Vitellius on the Rhine and Vespasian in Alexandria and Judaea; only Otho` → `Vitellius on the Rhine and Vespasian in Egypt and Judaea; only Otho`
- **Left (not real).** "ex manubis" in the Jewish War section; the usual form is manubiis. The report quotes the inscription's own spelling: Alföldy's reconstruction of CIL VI 40454a reads [ex] manubIs (I longa), printed as manubis (Judaism and Rome database, record 143, after Alföldy 1995…

### Rome 7.3 (words 3,342 → 3,357)

- **Fixed.** Diaspora revolt dated 116 in the Trajan section but 115–117 in the Gibbon list `In 116 the conquered cities rose and a Jewish revolt spread through Cyrene, Egypt and Cyprus` → `In 116 the conquered cities rose and a Jewish revolt, which Eusebius dates from Trajan's eighteenth year, 115 (<em>Chur…`
- **Fixed.** 'The 10,000 gladiators of 107' gives a year the body does not (Dio 68.15.1) `The 10,000 gladiators of 107,` → `The 10,000 gladiators of the Dacian victory games,`
- **Fixed.** Self-test 7 says 'Britain and Mauretania' against the body's 'Britons, Moors, Germans and Dacians' `even it records wars in Britain and Mauretania and risings in several provinces (5.4–5).` → `even it records wars with Britons, Moors, Germans and Dacians and risings among the Jews and in Achaea and Egypt (5.4–5…`

### Rome 7.4 (words 2,836, unchanged)

- **Fixed.** "Dio says ... and that he himself" in the Severus Alexander section reads as Ulpian but means Dio `and that he himself, hated by them for disciplining the Pannonian legions` → `and that Dio himself, hated by them for disciplining the Pannonian legions`
- **Left (not real).** Dio "75(75).3.2-3" in the Severus section does not match the report's numbering 76(75) from 197 The passage belongs to the Osroene/Adiabene campaign of 195: Loeb book 75 holds Boissevain 74 plus Boissevain 75.1-3, and Loeb 76 begins at Boissevain 75.4, so the bulwark-of-Syria passage is Loeb 75…

### Rome 7.5 (words 3,253, unchanged)

- **Fixed.** Self-test 4 says 'about a hundred procurators' against the body's about 136 under Commodus `a few dozen governors, about a hundred procurators on Pflaum's count` → `a few dozen governors, a little over a hundred procurators on Pflaum's count`

### Rome 8.1 (words 2,868, unchanged)

- **Fixed.** First Decius dispute box: "his naked corpse" has no named antecedent `Lactantius leaves his naked corpse` → `Lactantius leaves Decius' naked corpse`

### Rome 8.2

- **Left (not real).** Self-test 4 cites Lactantius 7.3, the body 7.3–4. Body 7.3–4 covers two claims (pay-takers outnumbering payers, and provinces cut up with officials piled on); the answer cites only the first, which is 7.3 (De mortibus persecutorum 7.3 'maior esse co…

### Rome 9.3 (words 2,848, unchanged)

- **Fixed.** Self-test 4 credits the rule on dotal land to Augustus; the body cites Gaius 2.63 and names no one. `Augustus forbade him to sell Italian dotal land without her consent (Gaius 2.63)` → `he could not sell Italian dotal land without her consent (Gaius 2.63)`
- **Left (check FAIL).** Self-test 3 says the wife 'could not receive gifts' where the body says 'custom voided gifts between spouses'. Fault is real, but the new text breaks the series 'she stayed..., kept her property, and gifts ... were void' into a faulty parallel (predicates then an independent clause); use e.g. '...kept her pro…

### Rome 10.1

- **Left (not real).** Self-test 2 cites Caesar's star as Metamorphoses 15.843–850, the body 15.761–850 (narrower, not contradictory). Both ranges are right for what they cite: the body's 15.761–850 covers the whole episode (Venus' alarm at 761–764, Jupiter's reply, the rescue), and 15.843–850 is exactly the catasterism ('Vix ea fat…

### Rome 10.2 (words 2,865, unchanged)

- **Fixed.** Self-test 2, "three years after Seneca's death", rests on a death year the body never gives. `postdates 68, three years after Seneca's death.` → `postdates 68.`

### Rome 13.2 (words 2,840, unchanged)

- **Fixed.** First dispute box cites "On Ends 4" with no passage `only in words (<em>On Ends</em> 4), the charge` → `only in words (<em>On Ends</em> 4.72), the charge`
- **Left (check FAIL).** "oikeiosis" in the prose (3 times), "oikeiōsis" in the table Not a real fault: the table's Greek column marks long vowels throughout (kathēkon, katorthōma, proēgmenon, prokoptōn) and οἰκείωσις has an omega; dropping the macron there makes that cell an outlier …

### Greece 0.1 (words 2,784 → 2,789)

- **Fixed.** Self-test 1 answer gives "speech" or "utterance"; body gives only "utterance" (noted twice) `<p>Simply "speech" or "utterance". The contrast` → `<p>Simply "utterance". The contrast`
- **Fixed.** Self-test 8 answer dates the tablets c. 1200 BC but names Khania, which the body does not date `the tablets show his name in Greece c. 1200 BC` → `the Pylos tablets show his name in Greece c. 1200 BC`
- **Fixed.** Self-test 6 answer "It is now dated to the first or second century AD" drops the body's hedge `It is now dated to the first or second century AD.` → `Most scholars date it to the first or second century AD.`
- **Fixed.** Work titles cited as references are unitalicised in places but italicised elsewhere (part 1 of 7) `(Olympian 1.28–29)` → `(<em>Olympian</em> 1.28–29)`
- **Fixed.** Work titles cited as references are unitalicised in places but italicised elsewhere (part 2 of 7) `(Theogony 27–28)` → `(<em>Theogony</em> 27–28)`
- **Fixed.** Work titles cited as references are unitalicised in places but italicised elsewhere (part 3 of 7) `(quoted at Plato, Phaedrus 243a)` → `(quoted at Plato, <em>Phaedrus</em> 243a)`
- **Fixed.** Work titles cited as references are unitalicised in places but italicised elsewhere (part 4 of 7) `(Olympian 1.36–53)` → `(<em>Olympian</em> 1.36–53)`
- **Fixed.** Work titles cited as references are unitalicised in places but italicised elsewhere (part 5 of 7) `(Olympian 1; Olympian 9.35–41)` → `(<em>Olympian</em> 1; <em>Olympian</em> 9.35–41)`
- **Fixed.** Work titles cited as references are unitalicised in places but italicised elsewhere (part 6 of 7) `(Theogony 278–279)` → `(<em>Theogony</em> 278–279)`
- **Fixed.** Work titles cited as references are unitalicised in places but italicised elsewhere (part 7 of 7) `<p>Pindar, Olympian 1, refusing` → `<p>Pindar, <em>Olympian</em> 1, refusing`
- **Left (check FAIL).** Linear B paragraph: "at least five centuries older than Homer" overstates for Pylos (c. 1200 BC vs Homer 750-700 BC); caption repeats it Fault only partly real (Zeus, Poseidon, Ares, Paean are at Knossos c. 1400-1370 BC, well over five centuries before Homer), and the fix cannot reach the figcaption's identical "at least five centurie…
- **Left (not real).** Transliteration mixed: Sophilos, Kleitias, Exekias beside Cypselus, Polygnotus, Stasinus, Uranus Each name is in its standard English form, as AGENT-SPEC asks: the vase painters are conventionally Sophilos, Kleitias, Exekias in English scholarship (Beazley), while Cypselus, Polygnotus, Stasinus,…

### Greece 0.2 (words 3,048 → 3,049)

- **Fixed.** Self-test 7 answer names Archias and 733 BC; the body gives only 'Naxos first (734), Syracuse a year later by Corinthians' `Corinthians under Archias, the year after Naxos, traditionally 733 BC, according to Thucydides 6.3.` → `Corinthians, the year after Naxos (734), according to Thucydides 6.3.`
- **Fixed.** Self-test 9 answer names Hippodameia; the body's Olympia row says only 'Pelops' chariot race' `Pelops' race for Hippodameia` → `Pelops' chariot race`
- **Fixed.** Self-test 2 calls the seven regions 'traditional sub-regions'; the body calls them compartments and its seven (Herodotus 8.73) are peoples `Name the seven traditional sub-regions of the Peloponnese.` → `Name the seven regional compartments of the Peloponnese.`
- **Fixed.** Inconsistent spelling: 'the capes of Argolis' (mental-map paragraph) against 'Argolid' (map block and Peloponnese table) `the capes of Argolis, Laconia` → `the capes of the Argolid, Laconia`

### Greece 0.3 (words 2,746 → 2,775)

- **Fixed.** Anchor dates: 'Fifteen dates' but the table has sixteen rows (c. 1450 to AD 529); also raised on re-check `Fifteen dates. The first two are approximate; everything from 776 is a traditional or recorded date.` → `Sixteen dates. The first two and the fourth (c. 750–700) are approximate; the rest are traditional or recorded dates.`
- **Fixed.** Mental map: '195 years that separate 1200 and the end of the Early Iron Age at 1000': 1200 to 1000 is 200, and the table ends the Early Iron Age at c. 800; also raised on re-check `close to the 195 years that separate 1200 and the end of the Early Iron Age at 1000` → `close to the 200 years between the end of the collapse (c. 1150) and the first recovery at Lefkandi (c. 950)`
- **Fixed.** Self-test 10: 'Alan Cameron argued there was no single formal closing', but the body only says the question is argued between Cameron and Watts in module 7.4; also raised on re-check `Alan Cameron argued there was no single formal "closing" of the Academy, so 529 is a conventional endpoint.` → `whether anything was formally "closed" is disputed, so 529 is a conventional endpoint.`
- **Fixed.** (re-check) Heading 'The nine periods and their boundaries' but the table has ten rows `The boundaries below are the ones used in most current handbooks; where a boundary is genuinely contested, the table sa…` → `The boundaries below are the ones used in most current handbooks, with the Bronze Age collapse given a row of its own a…`
- **Left (check PASS).** Anchor dates: 'The first two are approximate; everything from 776 is a traditional or recorded date', but c. 750–700 BC is also approximate; also raised on re-check c. 750–700 is approximate, so 'everything from 776' was wrong; naming the fourth row fixes it; same edit as item 1, apply once.
- **Left (not real).** Periods note gives the Archaic start as 800, 776 or 750, but the table offers only 'c. 800 (or 776)' No contradiction: the table flags the boundary as contested and the note expands the options; the figure caption explicitly describes this split ('800 or 776 in the table, 750 also in the note'), so …

### Greece 1.1 (words 2,974, unchanged)

- **Fixed.** Self-test 2 answer says 'excavated by Nikolaos Platon from 1961'; body says only 'found by Platon in 1961' `Zakros, excavated by Nikolaos Platon from 1961.` → `Zakros, found by Nikolaos Platon in 1961.`
- **Fixed.** Self-test 8 answer: 'restored heads and cat of the snake goddess figurines'; body says only the smaller figure's head and cat are modern `the restored heads and cat of the snake goddess figurines` → `the restored head and cat of the smaller snake goddess figurine`
- **Fixed.** Self-test 9 answer: 'roughly six centuries before Homer'; body gives no date for Homer `roughly six centuries before Homer` → `centuries before Homer`
- **Fixed.** Self-test 10 answer quotes 'broad Knossos' (Iliad 18.590–2); body never uses the phrase `A dancing-floor for Ariadne in "broad Knossos" (Iliad 18.590–2)` → `A dancing-floor for Ariadne at Knossos (Iliad 18.590–2)`
- **Fixed.** Stray space before closing tag: 'the rock-crystal rhyton. </p>' `including the rock-crystal rhyton. </p>` → `including the rock-crystal rhyton.</p>`
- **Left (check FAIL).** Self-test 1 answer omits Final Palatial from Platon's phases Platon's own scheme has four phases (Prepalatial, Protopalatial, Neopalatial, Postpalatial); Final Palatial is a later variant, so the answer is right and the replacement spreads the body's misattrib…
- **Left (check FAIL).** Spelling: 'Eleuthia at Amnisos' against 'Eileithyia' elsewhere in the same item and in Carry forward 3 Not a misspelling: 'Eleuthia' is the standard Ventris–Chadwick rendering of the tablet's e-re-u-ti-ja, deliberately set against Homer's Eileithyia in the same sentence; normalising it erases that dis…

### Greece 1.2 (words 2,746, unchanged)

- **Fixed.** Self-test 2 answer dates the Trojan War horizon c. 1250–1180 BC; the body gives no range `three to four centuries before any Trojan War horizon of c. 1250–1180 BC.` → `three to four centuries before any plausible Trojan War horizon.`
- **Fixed.** Self-test 4 answer calls Chadwick's role 'philological collaboration'; body says only Ventris 'published with John Chadwick' `John Chadwick's philological collaboration` → `John Chadwick's collaboration`
- **Fixed.** Self-test 8 answer quotes 'over Wilusa', which is not a phrase of the body's quotation `a past dispute "over Wilusa" now settled` → `a past dispute over Wilusa now settled`
- **Fixed.** Self-test 6 answer lists Eileithyia among the 'Olympian gods'; body does not call her Olympian `(also Ares, Dionysus, Eileithyia)` → `(also Ares, Dionysus)`
- **Fixed.** Carry forward 1 says kingship was lost in the gap; body has Homer's basileus as 'king' and Agamemnon's 'petty kingship', so what was lost is the wanax's palace kingship `in which writing, palaces and kingship were lost` → `in which writing, palaces and palace kingship were lost`
- **Left (check FAIL).** Self-test 7 answer says Pylos mainly produced textiles and flax with women workers; body puts textiles at Knossos, flax at Pylos, and does not tie the rationed women to textile work Not minimal and partly not a real fault: the body makes textiles the chief industry with Pylos's flax as its Pylos instance, so 'textiles' is supported; only 'women workers' lacks body support, yet t…
- **Left (not real).** Spelling 'Hector' (Iliad 6.117) against 'Hektor' (e-ko-to) in Religion and burial and in 'Achilleus, Hektor and Alexandra' (repeated in re-check) 'Hektor' appears only as the Linear B name (e-ko-to), paired with the transliterated 'Achilleus'; the Homeric hero takes the standard English form 'Hector' as AGENT-SPEC requires (cf. Ajax, Odysseus)…
- **Left (unsettled).** Cross-references 'module 10.10' (twice) and 'module 10.2' cannot be checked from this file Settling it needs greece/r-10.10.html (Calder and Traill v. Easton on the Troy treasure; Korfmann–Kolb on the Lower Town) and greece/r-10.2.html (the Mask of Agamemnon), which this agent may not open…

### Greece 1.3 (words 2,848 → 2,853)

- **Fixed.** Dark Age paragraph ends the phases at Early Geometric (c. 900-850); the table below ends with Early and Middle Geometric (900-760) `and Early Geometric (c. 900&ndash;850), labels` → `and Early and Middle Geometric (c. 900&ndash;760), labels`
- **Fixed.** Sea Peoples: 'Ekwesh as Achaeans' dangles; Ekwesh is not among the five Medinet Habu names and is never introduced `(Denyen as Danaans, Ekwesh as Achaeans, Shekelesh as Sicels)` → `(Denyen as Danaans, Ekwesh, from Merneptah's list, as Achaeans, Shekelesh as Sicels)`
- **Fixed.** Self-test 1 answer: 'Levantine and Egyptian scripts served temples, merchants and courts that survived' is not in the body `had no reason to be passed on. Levantine and Egyptian scripts served temples, merchants and courts that survived.</p>` → `had no reason to be passed on.</p>`
- **Fixed.** Self-test 4 answer: 'grain requests from Hatti and Ugarit'; the body has grain sent to Hatti and demanded from Ugarit, not by it `and textual grain requests from Hatti and Ugarit.` → `and texts on grain sent to Hatti and demanded from Ugarit.`
- **Fixed.** Self-test 2 answer: Pylos 'around 1180'; body gives it only as the same moment as 1190-1180 `The fire that destroyed the palace around 1180 baked` → `The fire that destroyed the palace around 1190&ndash;1180 baked`
- **Fixed.** Self-test italics (b): 'Iliad 10.261-265' and 'basileus' in roman in the Homer memory/distortion answer (the ninth and last quiz item) `Accurate: the boar's-tusk helmet (Iliad 10.261&ndash;265), bronze weaponry, or the Catalogue of Ships' Mycenaean geogra…` → `Accurate: the boar's-tusk helmet (<em>Iliad</em> 10.261&ndash;265), bronze weaponry, or the Catalogue of Ships' Mycenae…`
- **Fixed.** (re-check) Self-test 5 answer: 'Perati traded with Egypt and the Levant'; body says only it buried a community with Egyptian and Levantine imports `Perati traded with Egypt and the Levant` → `Perati's graves held Egyptian and Levantine imports`
- **Left (check FAIL).** Self-test 6 answer: 'four sacrificed horses'; body says only 'four horses, one with an iron bit' / Self-test answers 6 and 9 (leads say 6, 9, 10 / 6, 10): 'Iliad 23' (a) answer 6 Dropping 'sacrificed' fixes no real fault: the body itself says the burial matched Patroclus' 'slaughtered horses'; only the Iliad italics change is warranted.
- **Left (unsettled).** Dispute after Nichoria: 'is argued in module 5.1' cannot be checked from this report Settling it needs greece/r-5.1.html, which this pass may not open; open: whether module 5.1 actually treats Morris against Snodgrass on the burial record (AGENT-SPEC: open a report before writing 'mo…

### Greece 2.1 (words 2,907 → 2,908)

- **Fixed.** Self-test 4 answer: cave on Mount Aigaion 'near Lyktos'; body says only that Rheia is sent to Lyktos and Gaia hides the child on Mount Aigaion. `A cave on Mount Aigaion near Lyktos in Crete (477–484).` → `A cave on Mount Aigaion in Crete, after Rheia is sent to Lyktos (477–484).`
- **Fixed.** Self-test 5 answer cites (497–500) for the stone at Pytho; body cites 498–500. `as a sign for mortals (497–500)` → `as a sign for mortals (498–500)`
- **Fixed.** Self-test 6 answer cites (624–663) and says the Hundred-Handers 'bury the Titans under rocks'; body cites 639–663 and says they hurl rocks (687–712). `they bury the Titans under rocks while Zeus burns the battlefield.` → `they hurl rocks at the Titans while Zeus burns the battlefield.`
- **Fixed.** Spelling: 'Typhoeus' in the Typhon paragraph and the family tree, 'Typhon' elsewhere; the report never says they are one name. `Gaia bears a last child to Tartarus: Typhoeus, with` → `Gaia bears a last child to Tartarus: Typhoeus (Typhon), with`
- **Left (check FAIL).** Kumarbi parallels paragraph says 'three kings ending in a storm-god'; the paragraph above, the flow and the motif table give four (Alalu, Anu, Kumarbi, Teshub). Not a real fault: the sentence lists features shared with Hesiod, whose succession is three kings (Ouranos, Kronos, Zeus ~ Anu, Kumarbi, Teshub, Alalu having no Greek match); 'four kings' makes the c…
- **Left (check FAIL).** Self-test 10 answer: 'an anthropogony from the Titans' ashes'; body says only 'dismembered by the Titans, from whose remains mankind comes'. Fault is real ('ashes' is not in the body) but the fix is not minimal: changing 'ashes' to 'remains' suffices, whereas the rewrite drops 'anthropogony' and adds the dismemberment.
- **Left (not real).** Family tree (pre): Apate under Nyx, 'Zeus + Hera: Hebe, Ares, Eileithyia' and 'Hera alone: Hephaestus' not stated in the body. The tree is accurate to Hesiod within ranges the body cites: Apate (Deceit) among Nyx's children in 211–232 (Theogony 224), Hera's children and Hephaestus at 921–929 (theoi.com, Evelyn-White); the ou…

### Greece 2.2 (words 3,116 → 3,117)

- **Fixed.** Hera, Domains and epithets: capital 'Her' after a semicolon following (Iliad 4.51–52) `(<em>Iliad</em> 4.51–52); Her hostility` → `(<em>Iliad</em> 4.51–52). Her hostility`
- **Fixed.** Self-test 3 answer makes Poseidon call Zeus the elder at Iliad 13.355 and 15.166; body gives no such speaker at 13.355 `Homer's Poseidon calls him the elder brother (<em>Iliad</em> 13.355, 15.166)` → `Homer makes Zeus the elder (<em>Iliad</em> 13.355, 15.166)`
- **Fixed.** Self-test 4 answer: 'Odysseus invokes Zeus as avenger of suppliants and strangers'; body only says the Cyclops episode is a crime against Zeus `The guest–host relationship. Odysseus invokes Zeus as avenger of suppliants and strangers against Polyphemus (<em>Odyss…` → `The guest–host relationship. The Cyclops episode is a crime against Zeus Xenios (<em>Odyssey</em> 9.270–271).`
- **Fixed.** Self-test 6 answer: 'centuries before Herodotus' or the Thracian-origin theory's dates'; body gives no dates for either `around 1200 BC, centuries before Herodotus' or the Thracian-origin theory's dates.</p>` → `around 1200 BC.</p>`
- **Fixed.** Self-test 1 question: 'the earliest firm evidence for a cult of the Twelve Gods at Athens'; body never calls the altar the earliest `Which ancient structure gives the earliest firm evidence for a cult of "the Twelve Gods" at Athens` → `Which ancient structure attests a cult of "the Twelve Gods" at Athens`
- **Fixed.** 'Against the Titans': 'What they lack' – 'they' meant as the Titans but nearest names are Uranus, Cronus, Zeus `What they lack is a stable distribution of honours.` → `What the Titans lack is a stable distribution of honours.`
- **Left (not real).** Poseidon's lot speech cited as Iliad 15.187–193 (Poseidon, Defining myths) and 15.187–199 (Against the Titans) The two citations support different claims: the lot division itself runs 15.187–193, while 'Zeus should keep to his share' (let him stay in his third portion) is at 15.194–195, so 187–199 is the righ…
- **Left (not real).** Inconsistent form: '(Homeric Hymn 3.25–126)' against '(Hymn 3.146–164)' and '(Hymn 3.300–374)' under Apollo Full form at first citation, short form after it within the same section, as the report also does for Demeter's Hymn ('The Hymn says ... (2.3)'); not an inconsistency.
- **Left (not real).** Spelling: Latinised 'Hephaestus' throughout but temple is 'Hephaisteion' Building and festival names are transliterated throughout the report (Heraion, Thesmophoria, Plynteria, kerykeion); 'Hephaisteion' is the standard English name of the temple and matches 'Argive Herai…

### Greece 2.3 (words 2,932 → 2,934)

- **Fixed.** Self-test 2 answer says 'Hecate, in her cave, and Helios'; the body never mentions a cave (also raised in re-check). `Hecate, in her cave, and Helios.` → `Hecate and Helios.`
- **Fixed.** Self-test 6 answer states 'continuing his kingship' as fact; the body gives it only as Sourvinou-Inwood's reading in a dispute box that calls the question contested (also raised in re-check). `continuing his kingship, not weighing lives` → `not weighing lives`
- **Fixed.** Inconsistent name: 'Pyriphlegethon' in the geography paragraph and table, but 'ringed by Phlegethon' in the Aeneid 6 paragraph, with no note that they are the same river (also raised in re-check). `ringed by Phlegethon,` → `ringed by Phlegethon (Homer's Pyriphlegethon),`
- **Left (check FAIL).** (re-check) Self-test 4 answer says 'with her ascent at autumn sowing'; the body says only 'from harvest to sowing' and gives sowing as October, so the answer infers rather than states. Fault not real: the body says the months below run 'from harvest to sowing' and that grain is sown in October, which directly entails an ascent at autumn sowing (and the answer's 'in summer' rests on…

### Greece 2.4 (words 2,931 → 2,929)

- **Fixed.** Stemma <pre class="tree"> duplicates figure 2; its line "Hellen (or Hellen son of Zeus)" is awkward `Hellen (or Hellen son of Zeus)` → `Hellen (some say son of Zeus)`
- **Fixed.** Sons of Hellen para 2: "a father whose Athenian marriage is to a foreign woman" is muddled; Creusa is the Athenian, Xuthus the outsider `through a father whose Athenian marriage is to a foreign woman.` → `through a father, Xuthus, who married the Athenian Creusa.`
- **Fixed.** Self-test 1 cites Theogony 535–560 (body: 551, 556–557, 507–616) and says "burned bones and fat" (body: "burn white bones") `burned bones and fat for the gods and kept the meat for themselves (Hesiod, <em>Theogony</em> 535–560).` → `burned white bones for the gods and kept the meat for themselves (Hesiod, <em>Theogony</em> 551–557).`
- **Fixed.** Self-test 4: "may post-date his death in 456 BC"; body says only the play "dates after 456 BC" `it is not by Aeschylus and may post-date his death in 456 BC;` → `it is not by Aeschylus and may date after 456 BC;`
- **Fixed.** Self-test 8: laas/laos pun "first attested in Pindar, Olympian 9"; body gives the pun in the Apollodorus account `which become people (<em>laos</em>); first attested in Pindar, <em>Olympian</em> 9.</p>` → `which become people (<em>laos</em>); so Apollodorus, <em>Library</em> 1.7.2.</p>`
- **Fixed.** Self-test 9: "Xuthus, Hellen's third son"; body never says third son `They are sons of Xuthus, Hellen's third son,` → `They are sons of Xuthus, a son of Hellen,`

### Greece 2.5 (words 2,962 → 2,967)

- **Fixed.** Self-test 1 asks for the Muses 'as Hesiod lists them'; the body never gives Hesiod's order and its table puts Calliope first (also re-check). `Name the nine Muses as Hesiod lists them and say who` → `Name Hesiod's nine Muses and say who`
- **Fixed.** Self-test 6 answer adds the road to Sparta, Pan's complaint of neglect and his promise of help; the body says only that Philippides met Pan before Marathon (also re-check). `Philippides met Pan on the road to Sparta before Marathon; Pan complained of neglect and promised help, and after the v…` → `Philippides met Pan before Marathon, and Athens then founded`
- **Fixed.** Carry forward 3: 'imperial god' for Asclepius is not in the body (which ends at Rome, 293 BC); 'saviours of sailors in the Hymns' when the body cites only Homeric Hymn 33. `Asclepius rose from Homeric mortal to imperial god; the Dioscuri are dead men in the <em>Iliad</em> and saviours of sai…` → `Asclepius rose from Homeric mortal to god of the largest healing cult in the Mediterranean; the Dioscuri are dead men i…`
- **Fixed.** Cult table: 'Nyx's and Eris's children' sits as a blanket literary entry although Nemesis, the Moirai and Hypnos are in the cult columns and the body gives Thanatos a Spartan shrine (Plutarch, Cleomenes 9) (re-check). `Hypnos; Glaucus (Anthedon); Nike (as Athena Nike)</td><td>Pontus; Nereus; Proteus; Amphitrite; Triton; Eos; Selene; Ple…` → `Hypnos; Thanatos (Sparta); Glaucus (Anthedon); Nike (as Athena Nike)</td><td>Pontus; Nereus; Proteus; Amphitrite; Trito…`
- **Left (not real).** Self-test 2 answer: 'the first keeps it among the primordial dark powers' is not stated in the body, whose dispute box gives only West's reading of the Zeus-Themis version (also re-check). The body supports it: it lists the Moirai among Night's fatherless children (Theogony 211-232) and glosses that list as 'cosmology by genealogy: dark things are kin because they arrive together'; the…

### Greece 2.6 (words 3,274 → 3,272)

- **Fixed.** Self-test 7 answer: 'Pholus of Silenus and a nymph'; body gives only 'son of Silenus' (also re-check) `Pholus of Silenus and a nymph.` → `Pholus of Silenus.`
- **Fixed.** Table, Sirens row: 'Achelous + a Muse' under 'Parents (earliest source)'; earlier sources (Euripides Helen 167–169: Earth; Sophocles fr. 861: Phorcys) give other parents (also re-check) `<td>Sirens</td><td>Achelous + a Muse</td>` → `<td>Sirens</td><td>disputed</td>`
- **Fixed.** Self-test 8 answer attributes the Sirens' drowning to Apollodorus, Epitome 7.19; body gives drowning to Lycophron (re-check) / Self-test 8 question 'Which two monsters die without any hero killing them?' admits Talos (k… `Which two monsters die without any hero killing them?<details><summary>Answer</summary><p>The Sirens, who drown themsel…` → `Which two monsters kill themselves?<details><summary>Answer</summary><p>The Sirens, who drown themselves (Lycophron, <e…`
- **Fixed.** Cerberus 'the one brood-mate the hero does not kill' and Self-test 4 question: Chimaera, Sphinx, Sow are also not killed by Heracles (re-check) [body] `the one brood-mate the hero does not kill.` → `the one brood-mate Heracles faces and does not kill.`
- **Fixed.** Cerberus 'the one brood-mate the hero does not kill' and Self-test 4 question: Chimaera, Sphinx, Sow are also not killed by Heracles (re-check) [question] `Which of Typhon and Echidna's children is not killed by Heracles, and what happens instead?` → `Which of Typhon and Echidna's children does Heracles face without killing, and what happens instead?`
- **Left (check FAIL).** Self-test 1 answer cites Theogony 233–239; body cites 233–336 for the kin-group (also re-check) Fault not real: Theogony 233-239 is the exact passage for Pontus and Gaia's children (237-239 name Thaumas, Phorcys, Ceto, Eurybia), lies inside the body's 233-336 and does not contradict it; widenin…
- **Left (not real).** Self-test 7 answer: 'the cloud Nephele'; body's Centaurs section says only 'a cloud' The name is in the report body: the <pre class="tree"> genealogy (not a viz figure) reads 'Centaurus (Ixion + Nephele)', so the answer agrees with the body.
- **Left (not real).** Table, Typhon row: key source 'Theogony 853'; body cites 820–880 and 821–822 853 lies inside the body's cited 820–880 and is the line where Zeus takes up thunder and lightning to strike Typhoeus (Perseus, Evelyn-White, Th. 850–885); a key line within a cited range is not a co…

### Greece 3.1 (words 3,086 → 3,103)

- **Fixed.** Andromeda's mother spelled 'Cassiepea' (para 1) and 'Cassiopeia' (para 2); 'Cassiepea' is not a standard form (lead and re-check). `Cepheus and Cassiepea` → `Cepheus and Cassiopeia`
- **Fixed.** Self-test 8 says 'Acrisius is not killed' where the body says only 'Acrisius apparently still alive' (lead and re-check). `there is no discus and Acrisius is not killed.` → `there is no discus, and Acrisius is apparently still alive.`
- **Fixed.** Self-test 1 says the phrase shows the religious sense of 'hero' emerging as the epics took shape; the body says scholars suspect a later religious idea leaking into the epic. `and it suggests the religious sense of "hero" was emerging as the epics took shape.` → `and scholars suspect it is a later religious idea leaking into the epic.`
- **Fixed.** Hero-pattern table's 'hero shrine on the Argos–Mycenae road' is uncited in the body, and the body's Athens precinct is for Dictys and Clymene, not Perseus (lead and re-check). `Pausanias 2.18.1 reports Perseus still worshipped on Seriphos in the second century CE, and a precinct at Athens for Di…` → `Pausanias 2.18.1 reports a hero shrine of Perseus beside the road from Mycenae to Argos, Perseus still worshipped on Se…`
- **Fixed.** Self-test 7 says Apollodorus 'knows only a variant'; the body says he 'reports a variant'. `Apollodorus knows only a variant that she rivalled` → `Apollodorus reports a variant that she rivalled`
- **Left (not real).** Clymene, named in the Athens precinct sentence, appears nowhere else in the report. Pausanias 2.18.1 names her only as one of the 'saviours of Perseus'; the sentence says so (kept in the combined fix above), and adding an identity would be a new claim.

### Greece 3.2 (words 3,500, unchanged)

- **Fixed.** Self-test 1: question's 'born to rule Mycenae' and answer's 'a Perseid born that day would rule' go beyond the body (Iliad 19: 'a man of his blood ... to rule all his neighbours'); repeated in re-check `born to rule Mycenae, according to Homer?<details><summary>Answer</summary><p>In <em>Iliad</em> 19.95–133 Zeus swore th…` → `born to rule all his neighbours, according to Homer?<details><summary>Answer</summary><p>In <em>Iliad</em> 19.95–133 Ze…`
- **Fixed.** Self-test 2: answer's 'the labours earn nothing and the madness is pure divine malice' is not in the body (Youth, para. 2 and dispute box); repeated in re-check `Euripides puts it after, so the labours earn nothing and the madness is pure divine malice.` → `Euripides puts it after, so the labours are irrelevant to it: the madness strikes a man who has nothing left to earn.`
- **Fixed.** Self-test 10: answer's 'the Cynosarges gymnasium' not in the body, which says only 'his precinct at Cynosarges'; repeated in re-check `the Cynosarges gymnasium;` → `his precinct at Cynosarges (Herodotus 6.116);`
- **Left (not in scope).** Figure 1 (re-check, minor): Heracleidae tree draws the Argeads under Temenus, a fact from the following Macedon paragraph; caption omits that gap Concerns a figure inside <figure class="viz">; out of scope, and the checker itself says it is not a figure fault.

### Greece 3.3 (words 3,238, unchanged)

- **Fixed.** Self-test Q4 (also re-check): 'Apollodorus, Epitome 1.5–6' in roman where the body italicises Epitome `Apollodorus, Epitome 1.5–6).` → `Apollodorus, <em>Epitome</em> 1.5–6).`
- **Fixed.** Self-test Q6 (also re-check): '(Odyssey 11)' and '(Theogony 947–949)' in roman where the body italicises them `(Odyssey 11); abandoned for Aigle (Hesiod fr. 298); made Dionysus' immortal wife (Theogony 947–949)` → `(<em>Odyssey</em> 11); abandoned for Aigle (Hesiod fr. 298); made Dionysus' immortal wife (<em>Theogony</em> 947–949)`
- **Fixed.** Self-test Q9 (also re-check): 'giant skeleton with bronze weapons' and 'buried in the Theseion in the city centre' go beyond the body `found a giant skeleton with bronze weapons and brought it to Athens as Theseus' bones on Delphi's instruction; they wer…` → `found a coffin with a body of great size, a bronze spear and a sword, and brought the remains to Athens as Theseus' bon…`
- **Fixed.** Hephaisteion placed 'in the Agora' (The vase evidence) but 'above the Agora' (dispute box after figure 2) `The Hephaisteion in the Agora (c. 450)` → `The Hephaisteion above the Agora (c. 450)`
- **Left (not real).** (re-check) 'between about 570 and 510' in 'Making a rival to Heracles' carries no BC The report mostly gives bare dates (c. 570, c. 500–490, 476/5, in 490), BC is established earlier ('around 500 BC', Bacchylides dispute box), and no date in context can be read as AD; the most-used f…

### Greece 3.4 (words 2,850, unchanged)

- **Fixed.** Orpheus and the Sirens cited as 4.891–919 (The ship and the crew) and 4.891–921 (The return routes); repeated in re-check `sings down the Sirens (4.891–919)` → `sings down the Sirens (4.891–921)`
- **Fixed.** Self-test 2 answer adds 'he is too old to go himself', not in the body; repeated in re-check `brought home, and that he is too old to go himself (Pythian 4.156–167).` → `brought home (Pythian 4.156–167).`
- **Fixed.** Self-test 10 question makes Hesiod's Medeius the eponym of the Medes; body ties the name only to Medea or Medus `Which two different fathers are given for Medea's son who gave his name to the Medes?` → `Which two different fathers are given for Medea's son, and what is he called in each?`
- **Fixed.** Self-test 9 answer names 'Hera Akraia'; the Eumelus passage in the body says only 'Hera's temple' `She hides each newborn in the temple of Hera Akraia expecting immortality` → `She hides each newborn in Hera's temple expecting immortality`
- **Fixed.** Inconsistent spelling: 'a pan-Hellenic charter' against 'a Panhellenic heroine' `a pan-Hellenic charter` → `a Panhellenic charter`

### Greece 3.5 (words 3,460 → 3,462)

- **Fixed.** Self-test 5 answer: 'first founders and wallers of Thebes' and 'the acropolis (Cadmeia)' say more than the body (Odyssey quoted only as 'first founded'; acropolis not named Cadmeia) `calls the twins the first founders and wallers of Thebes. Pausanias 9.5.6 assigned Cadmus the acropolis (Cadmeia)` → `calls the twins the first founders of Thebes. Pausanias 9.5.6 assigned Cadmus the acropolis`
- **Fixed.** Self-test 9 answer: 'and Athena recoiled' is not in the body, which says only that Athena withholds the immortality she was bringing `ate his brains, and Athena recoiled` → `ate his brains, so Athena withheld the immortality she was bringing`
- **Fixed.** Self-test 9 answer: 'fleeing Periclymenus by the Ismenus'; the body (Amphiaraus row) does not name the Ismenus `fleeing Periclymenus by the Ismenus,` → `fleeing Periclymenus,`
- **Fixed.** Self-test 10 answer gives as a third inconsistency that Antigone opens with both brothers dead while Colonus shows Polynices alive; the body states only two inconsistencies `Give three points on which Sophocles's three Theban plays are inconsistent.<details><summary>Answer</summary><p>Oedipus…` → `Give two points on which Sophocles's three Theban plays are inconsistent.<details><summary>Answer</summary><p>Oedipus d…`
- **Fixed.** Self-test 3 answer: 'reclaimed by deceit for Callirhoe'; the body says Alcmaeon lied to get the heirlooms back but never says Callirhoe received them `reclaimed by deceit for Callirhoe` → `sought back by deceit for Callirhoe`
- **Fixed.** Epigoni section, last paragraph: 'Four generations after Harmonia's wedding' is not supported; Phayllus lived in the Third Sacred War `Four generations after Harmonia's wedding` → `Long after Harmonia's wedding`
- **Fixed.** (re-check) 'Creon's line will be reckoned Spartan-born' reads as Sparta, not the Spartoi; Self-test 2 repeats 'Spartan-born' (founding section) `Creon's line will be reckoned Spartan-born` → `Creon's line will be reckoned descended from the Spartoi`
- **Fixed.** (re-check) same lead, second place: Self-test 2 answer 'was counted Spartan-born' `was counted Spartan-born` → `was counted descended from the Spartoi`
- **Left (check FAIL).** (re-check) Phoenician Women paragraph: 'he would go to the stars for Tyranny'; capital T inconsistent with lower-case usage elsewhere Not a real inconsistency: the capital marks Eteocles's personified Tyranny, 'greatest of the gods' (Phoen. 506), a different sense from the lower-case concept in Carry forward.
- **Left (not real).** (re-check) Self-test 8 answer gives the Aeschylean gates in an order the body's table does not state Every champion-gate pair in the answer matches the table; the answer asserts no sequence, and the order listed is Aeschylus's own (Seven 375-652).
- **Left (not in scope).** (re-check) Figure 2 records Laius and Seven at 467 BC but not the trilogy's Oedipus Lead concerns a figure; no figure may change.

### Greece 3.6 (words 2,944, unchanged)

- **Fixed.** Self-test 8 answer names Teres, father of Sitalces; the body names only Sitalces (lead and re-check, treated once) `the mythical Tereus and Teres, father of Athens' Thracian ally Sitalces.` → `the mythical Tereus and Athens' Thracian ally Sitalces.`
- **Fixed.** Self-test 5 answer makes Myrtilus' curse an explanation of Atreus' and Thyestes' crimes; the body says the curse made the deaths of Agamemnon and Clytemnestra seem fated `the curse is one explanation for the crimes of Atreus and Thyestes and their descendants.` → `the curse, with Thyestes', made the deaths of Agamemnon and Clytemnestra seem fated.`

### Greece 3.7 (words 2,850 → 2,853)

- **Fixed.** Self-test 4 answer gives a reason for cutting Leucippus ('so Apollo's desire is unrivalled') that the body does not state (also the re-check lead) `Who is Leucippus and why does Ovid omit him?<details><summary>Answer</summary><p>In Parthenius 15 and Pausanias 8.20 he…` → `Who is Leucippus and what does Ovid do with him?<details><summary>Answer</summary><p>In Parthenius 15 and Pausanias 8.2…`
- **Fixed.** Self-test 7 asks for 'the earliest literary evidence'; body never calls Aristotle or Aristophanes the earliest / (re-check) Self-test 7 answer 'The full narratives are Ovid's' overstates: body says only the touch is tol… `What is the earliest literary evidence for the golden touch and for the asses' ears of Midas?<details><summary>Answer</…` → `What literary evidence before Ovid is there for the golden touch and for the asses' ears of Midas?<details><summary>Ans…`
- **Fixed.** Lycaon paragraph mixes 'Zeus Lycaeus', 'the Lycaean rite' with 'Mount Lykaion' `The ash altar on Mount Lykaion has been excavated` → `The ash altar on Mount Lycaeus has been excavated`
- **Fixed.** Table last row lists 'Homer, Hesiod, Herodotus, Sappho' as earliest Greek evidence for a group including Lycaon, whose body witnesses are Pausanias, Apollodorus, Plato `<td>Homer, Hesiod, Herodotus, Sappho</td>` → `<td>Homer, Hesiod, Herodotus, Sappho, Plato</td>`
- **Fixed.** (re-check) 'Lament for Bion 123–124' (Orpheus) and 'Bion's Lament' (Adonis) may be taken for the same work `Bion's <em>Lament</em> is the Hellenistic pathetic treatment` → `Bion's <em>Lament for Adonis</em> is the Hellenistic pathetic treatment`
- **Left (not in scope).** (re-check) Straight quotes in body vs curly quotes in figure captions The only curly quotes are in figure captions, which may not change; the body is consistent in straight quotes.

### Greece 4.1 (words 3,684 → 3,686)

- **Fixed.** Self-test 9 answer gives contrary winds as the cause, but the body says Aeschylus adopts none of the causes of Artemis' anger, only the portent of eagles and a hare. `has her gagged and sacrificed, with contrary winds as the cause and no rescue;` → `has her gagged and sacrificed, with no rescue and none of the three causes of Artemis' anger, only the portent of eagle…`
- **Fixed.** Self-test 10 answer says the Cypria and Apollodorus name Hector; the body cites only the Cypria for the killer. `the <em>Cypria</em> and Apollodorus name Hector` → `the <em>Cypria</em> names Hector`
- **Fixed.** Self-test 3 answer puts Electra in 'Homer's genealogy'; the body does not say Homer names her. `Zeus and Electra, Dardanus, Erichthonius` → `Zeus, Dardanus, Erichthonius`
- **Fixed.** Date style: Iphigenia among the Taurians (c. 414) and Iphigenia at Aulis (405) lack BC, unlike every other play date. `<em>Iphigenia among the Taurians</em> (c. 414), where she is Artemis' priestess until Orestes arrives, and <em>Iphigeni…` → `<em>Iphigenia among the Taurians</em> (c. 414 BC), where she is Artemis' priestess until Orestes arrives, and <em>Iphig…`
- **Fixed.** Spelling of the city: 'Ilios' in "Troy before Priam" against 'Ilion' in the tree and in Sack of Ilion. `before Ilios existed on the plain` → `before Ilion existed on the plain`
- **Left (not real).** Citation style: 'Hyginus, Fabulae 91' against bare 'Hyginus 92', 'Hyginus 95' elsewhere. Fabulae 91 is the first Hyginus citation; full title on first mention, bare number after, is the report's pattern (Apollodorus, Library 3.12.1–3 then Apollodorus 3.12.3).

### Greece 4.2 (words 3,280, unchanged)

- **Fixed.** Self-test 3 answer has the 1/24 gods correspondence in the reverse direction to the body `a divine quarrel in 1 is answered by a divine council in 24` → `the quarrel of gods in 1 answers the council of gods in 24`
- **Fixed.** Self-test 6 answer settles fate as a norm Zeus upholds; the body's dispute box leaves it open `not because it is impossible, so fate is a norm Zeus upholds rather than an absolute limit.` → `not because it is impossible, so fate can in principle be broken; the scene supports all three readings of what fate is…`
- **Fixed.** Self-test 10 asks where each omitted event is foreshadowed; the Wooden Horse answer gives no Iliad foreshadowing (lead given twice) `the Wooden Horse (not in the <em>Iliad</em> at all; <em>Odyssey</em> 8.492–520)` → `the death of Priam (his own vision of his body eaten by dogs at his door, 22.66–76)`
- **Fixed.** (re-check) 'about fifty days' in What the Iliad is vs 'about 51 days' in Structure and Self-test 2 `telling about fifty days` → `telling about 51 days`
- **Fixed.** (re-check) Self-test 9 answer says 9.381–384 'praises the wealth' of Egyptian Thebes; body says only 'the reference' `because 9.381–384 praises the wealth of Egyptian Thebes` → `because of the reference to Egyptian Thebes (9.381–384)`
- **Left (not real).** BC marked on 'eighth century BC' but not on 740–730, 1300/1180, 750–725, after 663 BC is given at the first date of the passage and every later date sits in the same BC context (Bronze Age, Hittite texts, seventh century); house style does not require the era on every date.
- **Left (unsettled).** (re-check) Dispute box cross-reference 'treated in module 10.10' (Korfmann and Kolb) unverified Settling it needs greece/r-10.10.html, which this pass may not open; open: whether module 10.10 exists and covers the Korfmann–Kolb debate on the historicity of the Trojan War.

### Greece 4.3 (words 3,179 → 3,183)

- **Fixed.** Self-test 2 answer says Proclus' summaries are 'preserved by Photius'; the body says Photius describes the Chrestomathy and Iliad manuscripts preserve it (also re-check). `preserved by Photius (<em>Bibliotheca</em> cod. 239) and in <em>Iliad</em> manuscripts` → `described by Photius (<em>Bibliotheca</em> cod. 239) and preserved in <em>Iliad</em> manuscripts`
- **Fixed.** 'Pyrrhus kills Polites' uses Virgil's name for Neoptolemus without identifying them (also re-check). `Pyrrhus kills Polites` → `Pyrrhus, as Virgil calls Neoptolemus, kills Polites`
- **Left (check FAIL).** Self-test 5 answer says archaic art shows an ankle wound; the body says the Chalcidian amphora shows an arrow in the lower leg (also re-check). Fault not real: the body's 'Apollodorus ... also says the ankle' treats the Chalcidian amphora's wound as at the ankle, and the vase does show the arrow in the ankle, so 'ankle wound' already agrees …
- **Left (not real).** Self-test 6 answer 'Odysseus wins' is implied but never stated in the body. The body states it: the Aethiopis paragraph says Odysseus' purification of Achilles foreshadows 'his inheritance of Achilles' arms', and Ajax's madness follows the judgement.
- **Left (not real).** 'the Little Iliad, in Tzetzes' fragment, has Neoptolemus take him captive' reads as if one Tzetzes fragment exists and lacks a fragment number. The Aeneas lines come from the same Tzetzes quotation on Lycophron 1268 as the Astyanax lines cited as fr. 29 West (Evelyn-White prints them together as one fragment), so 'Tzetzes' fragment' points b…
- **Left (not real).** Carry forward 3 names the Nostoi, which the body never mentions. A carry-forward item may point ahead to later material; the body anchors it (Athena's anger falls on the fleet, the Odyssey), and naming the next Cycle poem makes no unsupported claim.
- **Left (not real).** Witnesses paragraph: 'Quoted fragments and testimonia in scholia, Pausanias and Tzetzes, collected by ...' and the following items are verbless sentences. Deliberate enumeration after 'The other witnesses are of four kinds.'; style, not an error of fact or grammar the spec forbids.

### Greece 4.4 (words 3,559 → 3,567)

- **Fixed.** Self-test 6 answer: 'bow and arrows' vs body's 'bow'; 'Macalla near Croton' merges Lycophron's and Strabo's lists `<p>Petelia, Crimissa, Chone and Macalla near Croton (Lycophron, Strabo); Heracles' bow and arrows in the temple` → `<p>Crimissa, Petelia and Macalla (Lycophron); Petelia, Crimissa and Chone near Croton (Strabo); Heracles' bow in the te…`
- **Fixed.** Self-test 8 answer: payoff (other Cyclopes hear 'no one' is hurting Polyphemus and leave) not in the body `It pays off at 9.405–414 when the other Cyclopes hear that "no one" is hurting Polyphemus and leave.</p>` → `It pays off at 9.405–414.</p>`
- **Fixed.** Self-test 10 answer calls the chorizontes 'Hellenistic critics'; the body does not `<p>Hellenistic critics (Xenon, Hellanicus)` → `<p>Ancient critics (Xenon, Hellanicus)`
- **Fixed.** Menelaus in Egypt dispute box: 'Alan Lloyd's commentary' has no title or date `Alan Lloyd's commentary leans to the latter.` → `Alan Lloyd's commentary (<em>Herodotus Book II: Commentary 99–182</em>, 1988) leans to the latter.`
- **Left (check FAIL).** Self-test 9 answer cites 23.177–230; body cites the Penelope scene as 23.85–230 No real fault: 23.177-230 (Penelope orders the bed moved, through the recognition) lies within the body's 23.85-230 and is the more precise, correct reference for the bed test.

### Greece 4.5 (words 2,834 → 2,835)

- **Fixed.** Sophocles' Electra: 'usually placed 420–410' lacks BC. `(date unknown; usually placed 420–410)` → `(date unknown; usually placed 420–410 BC)`
- **Left (check FAIL).** Self-test 2 answer gives Pyth. 11.22–25 and a date (470s or 450s BC) the body lacks; 450s contradicts 'before Aeschylus' trilogy of 458'. The fault is real and the citation now matches the body, but the new text adds a date ('first half of the fifth century BC') that the body does not give, which is the fault the lead names, and its 'p…
- **Left (not real).** Self-test 1 answer cites Od. 11.421–423 for Cassandra's killing; body cites only Od. 11.405–434. 11.421–423 is the correct narrower reference for Cassandra's death and lies inside the body's 11.405–434; it adds no claim.

### Greece 5.1 (words 2,900 → 2,905)

- **Fixed.** Dispute box: Nestor's cup shows epic Nestor known 'in the 720s', but body dates the cup c. 740–720. `epic Nestor was known to Greeks in the 720s` → `epic Nestor was known to Greeks by c. 720`
- **Fixed.** Hesiod section: '(27–41, 38–39, 263–264)' cites 38–39 inside 27–41, reading as a doubled reference. `(27–41, 38–39, 263–264)` → `(27–41; the phrase at 38–39 and 263–264)`
- **Fixed.** Population surge: 'and Theran tradition' lacks an article (noted twice). `and Theran tradition of drought-driven emigration` → `and the Theran tradition of drought-driven emigration`
- **Fixed.** Self-test 3 answer: 'a Levantine port that merely consumed Greek pottery' goes beyond the body's 'native port that Greek traders visited'. `or a Levantine port that merely consumed Greek pottery.` → `or a native port that Greek traders visited and where some Greek pottery was consumed by locals.`
- **Fixed.** Self-test 5 answer: '(27–41)' after the Theogony reference reads as Theogony 27–41; body gives Works and Days 27–41. `the dispute with Perses (27–41)` → `the dispute with Perses (<em>Works and Days</em> 27–41)`
- **Fixed.** Spelling: 'Pithekoussai' throughout but 'Pithecusae' once in the Livy paraphrase, unmarked. `moved from Pithecusae to Cumae` → `moved from Pithekoussai to Cumae`
- **Left (check FAIL).** Self-test 8 answer: 'Stone Doric temples begin ... at Isthmia'; body lists Isthmia as one of three seventh-century examples, not the start. Fault is real, but adding '(c. 690–650)' is a change the fault does not need; 'belong to the seventh century, as at Isthmia' alone would fix it.
- **Left (check FAIL).** Carry forward 2: window 'roughly 750–650' ends before West's Iliad poet c. 680–640 given in the body. No real fault: 'roughly 750–650' already covers West's own approximate c. 680–640, and '750–640' adds false precision under 'roughly'.
- **Left (not real).** Self-test 4 answer: 'sixth-century Athenian Panathenaic performance' while the dispute box gives no century. The century is in the body: the box itself is framed by Peisistratus (Cicero, Hipparchus) and Jensen's 'sixth-century Athens', and Carry forward 2 says Athens shaped transmission in the sixth century…

### Greece 5.2 (words 2,711 → 2,710)

- **Fixed.** blockquote nested inside <p> in 'What a polis was' para 1; citation left as stray text (noted twice) `in Sicily: <blockquote>men are the city, not walls or empty ships.</blockquote> (Thucydides 7.77.7).</p>` → `in Sicily:</p> <blockquote>men are the city, not walls or empty ships (Thucydides 7.77.7).</blockquote>`
- **Fixed.** Self-test 8: 'under Pharaonic control' and 'Greeks had no territory or independent polis there' not in body (noted twice) `a trading port in Egypt under Pharaonic control, shared by nine Greek cities with a common Hellenion; the Greeks had no…` → `a licensed trading port in Egypt that Amasis granted to the Greeks, shared by nine Greek cities with a common Hellenion…`
- **Fixed.** Self-test 4: deme 'made the basis of Athenian citizenship by Cleisthenes' not in body (noted twice) `Deme: a territorial village or ward, made the basis of Athenian citizenship by Cleisthenes in 508/7.` → `Deme: a territorial village or ward, the building block of Cleisthenes' ten new tribes in 508/7.`
- **Fixed.** Self-test 5: 'choose and lay out the site'; body says only 'laid out the site' (noted twice) `choose and lay out the site` → `lay out the site`
- **Fixed.** Carry forward 2: colonies 'doubled the Greek world between 750 and 550', not in body (noted twice) `and they doubled the Greek world between 750 and 550;` → `and they carried the Greek world from Massalia to the Crimea;`
- **Fixed.** Chronology: Alalia c. 540-535 followed by 'By 550 the frontier had hardened'; Self-test 10 says Alalia marks the hardening `By 550 the frontier had hardened into spheres:` → `After Alalia the frontier hardened into spheres:`
- **Fixed.** Self-test 1: 'most were far too small to be called states'; body says 'not quite a state' and 'Most were tiny' `and most were far too small to be called states.` → `and most were tiny.`
- **Left (check FAIL).** Cyrene range given as Herodotus 4.150-159 (section, table, figure) and 4.150-158 (Cyrene paragraph) (noted twice) Fault not real: 4.150-158 correctly bounds the Theran and Cyrenaean versions through the move to the mainland (4.158), whereas 4.159 covers Battus II and later settlers; widening the range makes this…
- **Left (check FAIL).** Self-test 10 cites Herodotus 1.166; body cites 1.166-167 Fault not real: Herodotus 1.166 alone covers the battle and the Phocaeans leaving Corsica, so the narrower citation does not disagree with the body's 1.166-167; the change is cosmetic, not a correcti…
- **Left (not real).** Olbia/Scyles cited as Herodotus 4.17-18, 78-79 in table and 4.78-80 in Black Sea paragraph (noted twice) Different claims: the table cites Herodotus for Olbia as a site (4.17–18; Scyles' house at the Borysthenites' city, 4.78–79); the body cites Scyles' death, which is 4.80. Both ranges are right for wh…
- **Left (not real).** Possessive spelled two ways: 'Thucydides'' vs 'Herodotus's' Consistent with the standard British convention (New Hart's Rules): Greek names in -es take the apostrophe alone (Thucydides'), other names in -s take 's (Herodotus's, Odysseus's).

### Greece 5.3 (words 2,941, unchanged)

- **Fixed.** Self-test answer 2 calls it the 'Chigi vase'; body and figure 1 call it the 'Chigi olpe' (also raised on re-check) `The Protocorinthian Chigi vase, about 650 to 640 BC.` → `The Protocorinthian Chigi olpe, about 650 to 640 BC.`
- **Left (not real).** 'Coinage from Lydia' dates (Artemision c. 600, Croesus c. 550, Aegina c. 550, owls c. 515) carry no citation; Herodotus 1.94 covers only Lydian priority Not a fault under AGENT-SPEC: the cite-every-figure rule covers counts (dead, troops, money, people, distances), not standard archaeological dates; the text already attributes the Artemision date to …
- **Left (not real).** Table in 'The age of tyrants' lists Psammetichus for Corinth but the body never mentions him The table row cites Aristotle, Politics 5.1315b, which names Psammetichus son of Gordias as the third Cypselid ruler (three years); a table entry sourced in its own row need not be repeated in the bo…
- **Left (not real).** Dreros law: body says the kosmos may not hold office again 'for ten years'; Self-test answer 6 says 'within ten years' (re-check) Same meaning in both places (no second term as kosmos inside a ten-year interval); the answer agrees with the body, so there is no inconsistency to fix.

### Greece 5.4 (words 2,793 → 2,796)

- **Fixed.** Self-test 4 answer: 'Herodotus already knew rival accounts of the laws' origin' is not in the body (also the re-check) / Self-test 4 answer: 'his dates vary by centuries between authors' goes beyond the body (also the r… `<p>He received hero-cult; his dates vary by centuries between authors; Plutarch admits nothing about him is undisputed;…` → `<p>He received hero-cult; his dates vary between authors; Plutarch admits nothing about him is undisputed.</p>`
- **Fixed.** Self-test 10 question: 'from 480' while the body never dates Demaratus' figure (also the re-check) `Trace Spartiate numbers from 480 to the 240s` → `Trace Spartiate numbers from Demaratus' figure to the 240s`
- **Fixed.** Peloponnesian League: 'dissolved after Leuctra in 371, when Epaminondas freed Messenia' can read as dating the freeing to 371 `The League dissolved after Leuctra in 371, when Epaminondas freed Messenia.` → `The League dissolved after Leuctra in 371 and Epaminondas' liberation of Messenia in 369.`
- **Fixed.** Self-test 7 answer credits partible inheritance to Aristotle (Politics 1270a); in the body it is Hodkinson's explanation `large dowries under partible inheritance (Politics 1270a)` → `large dowries (Politics 1270a)`
- **Fixed.** Self-test 9 answer: 'a new law' allowed only one king on campaign; body does not call it a new law `Because a new law allowed only one king on campaign,` → `Because after 506 only one king could lead an army,`
- **Left (not real).** Italics: agoge italic in the body ('The word agoge') but roman in the Kennell dispute box The report uses roman 'agoge' most (h2, dispute box, mirage section, Carry forward); the single italic is the word cited as a word, which is conventional.

### Greece 5.5 (words 2,933 → 2,935)

- **Fixed.** Self-test 1 answer cites Plutarch, Solon 17 for the repeal and says 'homicide laws'; body cites only Athenaion Politeia 7.1 and says 'homicide law' (also re-check) `and Athenaion Politeia 7.1 and Plutarch, Solon 17 say Solon kept only the homicide laws.` → `and Athenaion Politeia 7.1 says Solon kept only the homicide law.`
- **Fixed.** Self-test 2 answer: 'a council of about 400' vs body's 401, and 'unknown to Aristotle's Politics' not in body (also re-check) `(a council of about 400, citizenship for those bearing arms) and is unknown to Aristotle's Politics; it is regarded` → `(a council of 401 by lot, citizenship for those bearing arms); it is regarded`
- **Fixed.** Self-test 6 answer: 'driven in a chariot into Athens'; body says only 'driven into the city' (also re-check) `dressed as Athena and driven in a chariot into Athens` → `dressed as Athena and driven into the city`
- **Fixed.** Self-test 7 answer: 'most scholars regard it as a later construction'; body names Davison and West against Merkelbach and Nagy (also re-check) `most scholars regard it as a later construction` → `Davison and West treat it as a late construction`
- **Fixed.** Cleisthenes 'problem solved' paragraph dates a review of the roll to 510; body never dates it `whom a review in 510 had threatened` → `whom a review of the citizen roll had threatened`
- **Fixed.** Other laws and his poetry: <blockquote> inside a <p> after 'Fr. 5 states his principle:' splits the paragraph (also re-check) `Fr. 5 states his principle: <blockquote>I gave the people as much privilege as suffices.</blockquote> Herodotus barely` → `Fr. 5 states his principle:</p> <blockquote>I gave the people as much privilege as suffices.</blockquote> <p>Herodotus …`

### Greece 5.6 (words 3,024 → 3,025)

- **Fixed.** Self-test 1 answer adds Mimnermus to the excluded poets; body names only Archilochus, Tyrtaeus, Solon and Theognis (also re-check) `Archilochus, Tyrtaeus, Mimnermus, Solon and Theognis, because` → `Archilochus, Tyrtaeus, Solon and Theognis, because`
- **Fixed.** Self-test 3 answer adds Paris, family, Anactoria and Lydian chariots/infantry not in body (also re-check) `That the most beautiful thing on earth is whatever one loves, proved by Helen's choice of Paris over her family, and ap…` → `That the most beautiful thing is whatever one loves, with Helen as proof; the speaker prefers the beloved to cavalry.`
- **Fixed.** Self-test 4 answer adds 'as witness before the court of Time'; body says only Earth called to witness (also re-check) `from whom he pulled up the boundary stones, as witness before the court of Time.` → `from whom he pulled up the boundary stones, as witness.`
- **Fixed.** Self-test 5 asks for 'four conditions' and counts Near Eastern contact, which the body says does not explain the leap; body cites three (also re-check) `Name the four conditions usually cited for the birth of philosophy in Ionia.<details><summary>Answer</summary><p>Contac…` → `Beyond borrowed Egyptian and Babylonian knowledge, name the three conditions usually cited for the birth of philosophy …`
- **Fixed.** Self-test 7 answer adds land and sea mixed and long cycles of change; body says only the earth had once been mud (also re-check) `That land and sea had once been mixed and the earth had been mud, so that the earth undergoes long cycles of change (Hi…` → `That the earth had once been mud (Hippolytus`
- **Fixed.** Table 'The poets, in order': Mimnermus (c. 630) listed after Sappho and Alcaeus (c. 600) (also re-check) / Table, Alcaeus row: 'fr. 6, 129, 332' names no edition, unlike every other fragment row (also re-check) `<tr><td>Alcman</td><td>Sparta</td><td>c. 620</td><td>choral (partheneia)</td><td>fr. 1 PMGF</td></tr> <tr><td>Sappho</t…` → `<tr><td>Mimnermus</td><td>Colophon/Smyrna</td><td>c. 630</td><td>elegy</td><td>fr. 1, 2 West</td></tr> <tr><td>Alcman</…`
- **Fixed.** Section 'The symposium as setting': <blockquote> inside <p>, invalid HTML (also re-check) `Alcaeus fr. 346 opens <blockquote>Let us drink. Why wait for the lamps? There is a finger of daylight left.</blockquote…` → `Alcaeus fr. 346 opens:</p> <blockquote>Let us drink. Why wait for the lamps? There is a finger of daylight left.</block…`
- **Left (not real).** Floruit column holds life spans (Simonides, Pindar, Bacchylides) and an office year (Solon) (re-check) Each entry marks its kind (a range, 'archon'), so nothing is misdated; renaming the column would desync the timeline figure's caption, which cites 'the table's Floruit column' and may not change.

### Greece 6.1 (words 2,765, unchanged)

- **Fixed.** Self-test 1 answer says the Naxos expedition was 'funded by Persia'; the body does not say so. `promised to the satrap Artaphernes and funded by Persia; facing ruin` → `promised to the satrap Artaphernes; facing ruin`
- **Fixed.** Self-test 3 answer says the Spartans 'marched from Sparta in three days'; the body does not state it. `2,000 arrived after the battle, having marched from Sparta in three days (Herodotus 6.106, 6.120)` → `2,000 arrived after the battle (Herodotus 6.106, 6.120)`
- **Fixed.** Self-test 6 answer says Aristides 'commanded at Plataea'; the body never says so. `He was recalled before Salamis and commanded at Plataea.` → `He was recalled before Salamis.`
- **Fixed.** Self-test 8 answer sets the ships against 'the Acropolis palisade'; the body never presents the palisade as the rival reading of the oracle. `Themistocles argued it meant the ships, not the Acropolis palisade, and that` → `Themistocles argued it meant the ships, and that`
- **Fixed.** Self-test 10 answer adds 'and this applies to his whole work' to the 7.152 rule; the body does not give that scope. `not to believe all of it, and this applies to his whole work (Herodotus 7.152)` → `not to believe all of it (Herodotus 7.152)`

### Greece 6.2 (words 2,954 → 2,958)

- **Fixed.** Self-test 3 answer names a Byzantium revolt of 440 that the body never mentions `Euboea (446) and Byzantium (440) were lesser or concurrent revolts.` → `Euboea also revolted in 446.`
- **Fixed.** Self-test 6 answer says the 'additional' powers were 'probably' audit/vetting and guardianship of the laws; body says uncertain `Its "additional" powers, probably the audit and vetting of magistrates and a general guardianship of the laws, went to` → `Its "additional" powers, whose content is uncertain (reconstructions range from the audit and vetting of magistrates to…`
- **Fixed.** Self-test 7 answer says Pericles 'obtained' an exemption; body says he 'sought' one `(Pericles obtained an exemption for his son by Aspasia)` → `(Pericles sought an exemption for his son by Aspasia)`
- **Fixed.** Self-test 10 answer cites Protagoras 319 (not in body) and Republic 488–489 (body: 488a–489a) `(Republic 488–489, Protagoras 319)` → `(Republic 488a–489a)`
- **Fixed.** Athenaion Politeia introduced as 'attributed to Aristotle' but later called 'Aristotle's text' (dispute box) (1 of 2) `is uncertain; Aristotle's text speaks only of "additional powers".` → `is uncertain; the <em>Athenaion Politeia</em> speaks only of "additional powers".`
- **Fixed.** Athenaion Politeia introduced as 'attributed to Aristotle' but later 'Aristotle's bare "because of the number of citizens"' (2 of 2) `and Aristotle's bare "because of the number of citizens"` → `and the <em>Athenaion Politeia</em>'s bare "because of the number of citizens"`
- **Left (not real).** Self-test 5 answer: 'Ephialtes carried the Areopagus reforms in his absence'; body only implies it Body says the timing was political because Cimon was at Ithome and that 'he opposed the reforms on his return', which states the reforms passed while he was away.

### Greece 6.3 (words 3,192, unchanged)

- **Fixed.** Peace of Nicias section: 'His extravagance' follows King Agis, so the 6.15 sentence about Alcibiades reads as about Agis `restored Spartan prestige (5.64–74). His extravagance made` → `restored Spartan prestige (5.64–74). Alcibiades' extravagance made`
- **Fixed.** Self-test 3 answer: 'fleet and reserve' and 'private ambition and gain, above all in Sicily' go beyond the body (fleet raids and tribute; 2.65 says only the plan would have worked had successors kept to it; factional am… `use the fleet and reserve to outlast Sparta, and make no new conquests. Thucydides says his successors did the opposite…` → `use the fleet to raid the Peloponnese and keep tribute flowing, and make no new conquests. Thucydides says it would hav…`
- **Fixed.** Self-test 4 answer: 'deprive Athens of the party inside every city that might open its gates' is not the body's argument; cites 3.42–48 where body cites 3.37–48 `killing the demos would deprive Athens of the party inside every city that might open its gates.` → `killing the demos along with the oligarchs would teach every subject city that revolt has no exit.`
- **Left (check FAIL).** Self-test 5 answer: Thermopylae image and citation 4.38–40 not in body (body 4.29–41); 'Lacedaemonian hoplites' vs body's 'survivors' Not minimal: only the Thermopylae image is a real fault; '292 Lacedaemonian hoplites' is correct and consistent with the body's 420 hoplites, and 4.38-40 is an accurate narrower citation within 4.29-…
- **Left (not real).** Self-test 10 answer: 'King Pausanias, outflanking Lysander' vs body 'jealous of him' The body says Pausanias, jealous of Lysander, brokered reconciliation instead of the crushing Lysander moved for; 'outflanking' describes that same outcome and contradicts nothing.
- **Left (not real).** Self-test 7 answer: '500 Athenian colonists' where body says '500 colonists planted (5.116.4)' The body's subject is Athens taking Melos, so the colonists are Athenian by implication; Thucydides 5.116.4 says Athens sent 500 colonists of its own.
- **Left (not real).** Self-test 9 answer: 'as a presiding prytanis' where body says only 'Socrates, presiding' Same claim; 'prytanis' only names the office in which he presided (Plato, Apology 32b, has his tribe holding the prytany), and adds no new fact.

### Greece 6.4 (words 4,670 → 4,671)

- **Fixed.** Self-test 1 answer gives Elaphebolion as (March/April); body says (late March). `<p>Dionysia in Elaphebolion (March/April),` → `<p>Dionysia in Elaphebolion (late March),`
- **Fixed.** Self-test 2 answer adds 'victory feast' not in body and drops 'from 449' for actors. `<p>Training, costume, upkeep and victory feast of the chorus; about thirty minae. The state paid poet and actors.</p>` → `<p>Training, costume and upkeep of the chorus; about thirty minae. The state paid poet and, from 449, actors.</p>`
- **Fixed.** Self-test 3 answer says tablets were 'drawn and counted' and speaks of ten judges/ten urns; body says only five were counted. `only five of their ten tablets were drawn and counted.` → `only five of their ten tablets were counted.`
- **Fixed.** Self-test 4 answer gives Aeschylus a 'reduced chorus', not in body. `<p>Aeschylus: second actor, reduced chorus, primacy of speech.` → `<p>Aeschylus: second actor, primacy of speech.`
- **Fixed.** Euripides section and Self-test 7: 'seven' school plays plus 'alphabetic ten' makes seventeen, not nineteen. `which is why nineteen plays survive: seven from the same school selection as the other two sevens, and the "alphabetic"…` → `which is why nineteen plays survive: ten from the same school selection as the other two sevens, and the "alphabetic" n…`
- **Fixed.** (same lead) Self-test 7 answer repeats the seven + ten count. `<p>Seven come from the selected school edition like the other sevens; ten more (<em>Helen</em> to <em>Hippolytus</em>, …` → `<p>Ten come from the selected school edition, against seven each for the others; nine more (<em>Helen</em> to <em>Cyclo…`
- **Fixed.** Origins: '(1448a29–b2)' names no work after a Herodotus citation; it is the Poetics. `The Peloponnesians claimed both genres (1448a29–b2).` → `The Peloponnesians claimed both genres (<em>Poetics</em> 1448a29–b2).`
- **Fixed.** Poetics section: 'Golden and Nussbaum (The Fragility of Goodness, 1986)' gives Nussbaum's book to both. `Golden and Nussbaum (<em>The Fragility of Goodness</em>, 1986) clarification;` → `Golden, and Nussbaum in <em>The Fragility of Goodness</em> (1986), clarification;`

### Greece 6.5 (words 3,476 → 3,478)

- **Fixed.** Self-test 3 answer gives Dover the 'modelled on Socrates' trial' claim the body gives to most scholars (also re-check) `fits a pattern Dover showed was modelled on Socrates' trial.` → `belongs among the fifth-century impiety trials Dover showed rest on late evidence; most scholars treat it as fiction mo…`
- **Fixed.** Self-test 6 answer adds 'in the same respect' and the inner-conflict inference not in the body (also re-check) `Appetitive, spirited, reasoning. One thing cannot at once want and refuse the same object in the same respect, so inner…` → `Appetitive, spirited, reasoning, distinguished because one thing cannot at once want and refuse the same object (436b t…`
- **Fixed.** Self-test 7 answer states the Third Man argument's content, which the body only names (also re-check) `<p>If the Form of Largeness is itself large, it and large things share a feature requiring a further Form, without end.…` → `<p>A regress objection to the Forms, which Aristotle named the Third Man; Plato raises it in the <em>Parmenides</em> (1…`
- **Fixed.** Self-test 8 answer: 'which may be extreme' not in the body `the right amount for the situation, which may be extreme; some acts` → `the right amount for the situation; some acts`
- **Fixed.** (re-check) Trial section: 'Critias and Charmides ... were among them' reads as among the 1,500 killed; sense is among the Thirty `Plato's relatives, were among them, and Alcibiades` → `Plato's relatives, were among the regime's leaders, and Alcibiades`
- **Left (not real).** Self-test 10 answer credits Stilpo's line with logic the body gives to Eubulides and Diodorus The answer says Stilpo's school's logic, and the body places Stilpo in Euclides' school ('His school turned to logic ... Stoic logic grew from this ground'); the lead itself calls it acceptable.
- **Left (not real).** Carry forward 1: 'the Stoics by identifying nature with reason and law' not stated in the body Carry-forward items point ahead to later modules, not back to the body; the claim is the standard Stoic position (Diogenes Laertius 7.87 to 88: life in agreement with nature, the common law that is r…

### Greece 6.6 (words 2,962, unchanged)

- **Fixed.** Self-test 5 answer adds 'under their own constitutions'; body says only 'free and autonomous' (lead and re-check) `members free and autonomous under their own constitutions;` → `members free and autonomous;`
- **Fixed.** Self-test 9 answer: 'control of Thermopylae'; body says Philip only marched through it in 346 (lead and re-check) `after 346, control of Thermopylae, and the presidency` → `after 346, and the presidency`
- **Fixed.** Self-test 2 answer: 'with the satrap Pharnabazus'; body says 'for Pharnabazus'; 'with' implies joint command (lead and re-check) `commanding a Persian fleet with the satrap Pharnabazus,` → `commanding a Persian fleet for Pharnabazus,`
- **Fixed.** Heading 'The Second Athenian League, 378–': open en dash with no end date (lead and re-check) `<h2>The Second Athenian League, 378–</h2>` → `<h2>The Second Athenian League, 378–338</h2>`
- **Fixed.** Self-test 6 answer: 'the cavalry fought first'; body says only that the cavalry drove the Spartan horse into their own infantry (re-check) `the cavalry fought first and drove the Spartan horse into their own line.` → `the cavalry drove the Spartan horse into their own infantry.`
- **Fixed.** Carry forward 1: 'Thebes after 371 ... used a common peace guaranteeing it'; the body never says so (re-check) `and every hegemon in turn, Sparta after 387, Thebes after 371 and Philip at Corinth in 338/7, used a common peace` → `and Sparta after 387 and Philip at Corinth in 338/7 each used a common peace`
- **Fixed.** Carry forward 3: 'Diodorus' compression of Ephorus'; Ephorus is not mentioned in the body (re-check) `Xenophon's silence on Epaminondas, Demosthenes' portrait of Philip and Diodorus' compression of Ephorus all shape` → `Xenophon's silence on Epaminondas and Demosthenes' portrait of Philip both shape`
- **Left (check FAIL).** Chaeronea: 'perhaps 35,000 allied Greeks faced Philip's 30,000 foot and 2,000 horse' carries no citation Diodorus 16.85.5 is right for Philip's 30,000 foot and 2,000 horse, but 'perhaps 35,000' still has no owner (AGENT-SPEC needs an ancient author or a named modern estimate), and the parenthesis says o…
- **Left (not real).** Carry forward 2: 'Theban dependence on two men' is an inference, not stated in the body A fair distillation: the body makes Epaminondas one of the three things Theban power rested on, and narrates Pelopidas' death (364) and Epaminondas' (362) followed by Xenophon's 'confusion and disord…

### Greece 6.7 (words 3,624, unchanged)

- **Fixed.** Self-test 1 answer: 'both served on the campaign' and 'Ptolemy, writing as a king, would have found lying dishonourable' are not in the body (also the re-check) `and why does he trust them?<details><summary>Answer</summary><p>Ptolemy son of Lagus and Aristobulus of Cassandreia (Ar…` → `and how does he use them?<details><summary>Answer</summary><p>Ptolemy son of Lagus and Aristobulus of Cassandreia (Arri…`
- **Fixed.** Self-test 10 answer: 'the infant Alexander IV' though the body says Roxane was pregnant at the Babylon settlement (also the re-check) `and the infant Alexander IV, son of Roxane.` → `and Alexander IV, Roxane's son, not yet born.`
- **Fixed.** (re-check) Roxane paragraph: 'first marriage, at thirty' but born July 356 and married spring 327 makes him 28 `first marriage, at thirty, was` → `first marriage, at twenty-eight, was`
- **Left (not real).** Inconsistent possessive: Chares', Xerxes' against Curtius's, Darius's, Philotas's British convention (MHRA Style Guide 2.5.1, mhra.org.uk) gives Greek names in -es the apostrophe alone (Xerxes', Demosthenes') and other names in -s an apostrophe and s; the report follows it consist…
- **Left (not in scope).** (re-check) Straight quotes in body vs curly quotes in figure captions The only curly quotes are in figcaptions inside figure.viz, which may not change; the body uses straight quotes throughout and is consistent.

### Greece 7.1 (words 2,989 → 2,993)

- **Fixed.** Self-test Q2 answer adds 'and sceptre'; body names only Alexander's empty throne and diadem (also re-check). `<p>Alexander's empty throne with diadem and sceptre, before which` → `<p>Alexander's empty throne and diadem, before which`
- **Fixed.** Self-test Q3 answer assigns autumn 312 to Macedonian and spring 311 to Babylonian reckoning; body does not (also re-check). `the era runs from autumn 312 (Macedonian) or spring 311 (Babylonian reckoning).` → `the era runs from autumn 312 or spring 311.`
- **Fixed.** Self-test Q6 answer: 'allies assigned it to Seleucus' and 'six Syrian Wars' not in body (also re-check). `<p>The allies assigned it to Seleucus, but Ptolemy, who had not fought, occupied it; Seleucids claimed it as spear-won …` → `<p>Ptolemy, who had not fought, kept it, but the Seleucids claimed it as spear-won land (Polybius 5.67), and the claim …`
- **Fixed.** Self-test Q7: 'Seleucus had killed Lysimachus', 'in 281' for the stabbing and the question's 'a few months earlier' go beyond the body (also re-check). `<li>Who killed Seleucus I, where, and what had happened a few months earlier?<details><summary>Answer</summary><p>Ptole…` → `<li>Who killed Seleucus I, where, and what had happened just before?<details><summary>Answer</summary><p>Ptolemy Ceraun…`
- **Fixed.** 'Antigonus took the diadem, gave his son one, and the other four followed': the other four are never named. `Antigonus took the diadem, gave his son one, and the other four followed (Plutarch, <em>Demetrius</em> 17–18).` → `Antigonus took the diadem and gave his son one (Plutarch, <em>Demetrius</em> 17–18); Ptolemy, Seleucus, Lysimachus and …`
- **Left (not real).** (re-check) Diodotus' secession given as 'around 250' twice, while the Seleucid dispute box gives '256 or 246'. 'Around 250' is an approximate midpoint consistent with the 256/246 alternatives the dispute box already flags as uncertain; the lead itself calls it not contradictory.

### Greece 7.2 (words 2,878 → 2,880)

- **Fixed.** Self-test 9 answer: 'Good and evil consist in sensation' premise is not in the body (also re-check) `<p>Good and evil consist in sensation; death ends sensation because the soul's atoms disperse; so death cannot be bad f…` → `<p>The soul is an atomic compound that disperses at death, so where death is, we are not, and death is nothing to us (K…`
- **Fixed.** Self-test 2 answer adds 'Greek', 'first systematic bibliography', 'compiled at the Alexandrian Library' (also re-check) `A 120-book catalogue of Greek authors and works arranged by genre, the first systematic bibliography, compiled at the A…` → `A 120-book catalogue of authors and works arranged by genre, the ancestor of every bibliography.`
- **Fixed.** Self-test 3 answer: 'introduced by Zenodotus' and 'the vulgate' go beyond the body `who introduced it, and why does it matter that athetised lines were kept?<details><summary>Answer</summary><p>A margina…` → `who used it, and why does it matter that athetised lines were kept?<details><summary>Answer</summary><p>A marginal stro…`
- **Fixed.** Self-test 8 answer lists death among indifferents; body lists health, wealth, pain and reputation `(wealth, pain, death)` → `(wealth, pain, reputation)`
- **Fixed.** Hero paragraph: 'Pneumatica with its steam-driven aeolipile, temple automata and the Metrica' reads as if the Metrica were part of the Pneumatica `left the <em>Pneumatica</em> with its steam-driven aeolipile, temple automata and the <em>Metrica</em>;` → `left the <em>Pneumatica</em>, with its steam-driven aeolipile and temple automata, and the <em>Metrica</em>;`
- **Fixed.** Inconsistent citation form: 'fr. 1 Pfeiffer' and 'Epigram 28 Pf.' in the same paragraph `Epigram 28 Pf. begins` → `Epigram 28 Pfeiffer begins`

### Greece 7.3 (words 2,856 → 2,857)

- **Fixed.** Self-test 3 answer: Gruen's 'in good faith' is not in the body (also re-check) `Gruen saw Rome borrowing a standard Hellenistic slogan in good faith.` → `Gruen saw Rome borrowing an old Hellenistic slogan and meaning roughly what the Antigonids and Ptolemies had meant by i…`
- **Fixed.** Self-test 6 answer: 'fewer than 300 returned' vs body 'fewer than 300 of the thousand were alive' `fewer than 300 returned.` → `fewer than 300 were still alive.`
- **Fixed.** Italics: Self-test answers set Sallust's Histories (7), Plutarch, Sulla 26 (8), OGIS 338 (7) and deisidaimonia (10) in roman (also re-check) `Plutarch, Sulla 26)` → `Plutarch, <em>Sulla</em> 26)`
- **Fixed.** Gods and ancestors: 'Apollo in 431' is the only date in the list without a citation `Apollo in 431, Asclepius` → `Apollo in 431 (Livy 4.29), Asclepius`
- **Fixed.** Achaean War dispute box: 'in 27 BC' is the only body date carrying BC `constituted the province in 27 BC,` → `constituted the province in 27,`
- **Left (check FAIL).** Self-test 7 answer: 'appears only' and 'ratification by Rome' go beyond the body; OGIS 338 and Sallust's Histories set in roman (also re-check) This aligns the answer to a body error: OGIS 338 (IvP 249) says the will still had to be ratified by the Romans (Berlin Antikensammlung description: 'noch bestätigt werden muss'), so 'refers to the w…
- **Left (check FAIL).** Self-test 10 answer: 'masses in order and magistrates honest' vs body 'masses honest and magistrates accountable'; deisidaimonia in roman This aligns the answer to an inaccurate body paraphrase: Polybius 6.56 says religious fear holds the fickle multitude in check and keeps magistrates handling public money honest, which the old answer…
- **Left (not real).** Self-test 5 answer: 'lunar eclipse of 21 June 168' not stated in body Body gives Pydna on 22 June 168 with the eclipse the night before, so 21 June follows directly; the total lunar eclipse fell on 21 June 168 BC (eclipsewise.com, LE -0167 Jun 21, greatest at 18:38 UT).

### Greece 7.4 (words 2,691 → 2,697)

- **Fixed.** Self-test 8 (Isagoge) answer names Aristotle's Categories and Boethius' translation; the body says only that the Isagoge became the medieval logic primer (lead given twice). `Porphyry's introduction to Aristotle's <em>Categories</em>; through Boethius' Latin translation it became the standard …` → `A logic work by Porphyry of Tyre that became the medieval logic primer.`
- **Fixed.** Long ending, last paragraph: 'went to the Persian court of Khusro I, returned under the peace of 532' lacks a conjunction (lead given twice). `Khusro I, returned under` → `Khusro I and returned under`
- **Fixed.** Long ending dispute box: 'Tardieu's Harran thesis for Simplicius' dangles; Harran and the thesis are not introduced anywhere. `Tardieu's Harran thesis for Simplicius is widely cited` → `Tardieu's thesis that Simplicius then settled at Harran, in Mesopotamia, is widely cited`
- **Left (not real).** Self-test 1 answer has 'Colonia Laus Iulia Corinthiensis'; the body has 'the colony Laus Iulia Corinthiensis' (lead given twice). Colonia is the Latin for 'colony': the body gives the same name with the word translated, so the two forms agree and nothing is inconsistent.
- **Left (not real).** Self-test 6 answer puts both the Pan story and the silent-oracles question in On the Obsolescence of Oracles; the body gives the silence question to the three Delphic dialogues together. The body lists On the Obsolescence of Oracles among the dialogues on why shrines have fallen silent and places the Pan story in De defectu 419b–d; the answer specifies within what the body says, and …
- **Left (not in scope).** Figure 1 label "Nero's “liberation” of Greece" uses curly quotes where the body uses straight quotes. Inside a figure; no figure may change.

### Greece 8.1 (words 2,907 → 2,905)

- **Fixed.** Dispute box under 'A religion with no name': 'Burkert and Price' names Price with no work or date and nowhere else in the report `Burkert and Price treat ritual as primary` → `Burkert treats ritual as primary`
- **Fixed.** Self-test 2 answer gives water twice; body's procession step has the basket, water belongs to step 2 `Procession with garlanded animal, basket and water;` → `Procession with garlanded animal and basket;`
- **Fixed.** Self-test 6 answer: 'by lot from all citizens' vs body 'from all Athenian women' `by lot from all citizens (priestess` → `by lot from all Athenian women (priestess`
- **Fixed.** Self-test 8 answer: birth purified by 'washing', which the body never names for birth `Birth (washing, waiting days per the Cyrene law)` → `Birth (waiting days per the Cyrene law)`
- **Fixed.** Self-test 9 answer: 'stood on or touched the cut pieces' vs body 'sworn standing on the cut pieces' `stood on or touched the cut pieces` → `stood on the cut pieces`
- **Left (not real).** Spelling: 'Asclepius' and 'Heracles' in prose beside 'Asklepieia' and 'Herakleia' in the calendar table Different categories, each consistent: persons and gods take standard English forms per AGENT-SPEC (Heracles, Asclepius), while every festival in the table is a Greek transliteration (Panathenaia, Th…

### Greece 8.2 (words 3,663, unchanged)

- **Fixed.** Self-test 1 answer drops the annual Bysios stage and makes every seventh Apollo's birthday `<p>The seventh of each month, Apollo's birthday; in` → `<p>The seventh: at first once a year, on the seventh of Bysios, Apollo's birthday, later the seventh of every month; in`
- **Fixed.** Self-test 2 answer says consultation was refused; body says only the day was unpropitious `if not, consultation was refused (Plutarch` → `if not, the day was unpropitious (Plutarch`
- **Fixed.** Self-test 4 says Croesus misread three responses incl. the test oracle, and adds 'failed to ask follow-up questions' `<li>Which three Herodotean responses did Croesus misread, and how did the Pythia defend herself?<details><summary>Answe…` → `<li>Which two Herodotean responses did Croesus misread, and how did the Pythia defend herself?<details><summary>Answer<…`
- **Fixed.** Self-test 9 credits Hipponion with undercutting Zuntz; body credits Pelinna and Olbia `to Dionysiac initiation, which undercut Zuntz's denial that the tablets were Orphic.</p>` → `to Dionysiac initiation.</p>`
- **Fixed.** Self-test 10 calls Cilicia Greek-speaking and Cilicia/Commagene the first attested worshippers `its first attested worshippers are in Greek-speaking Cilicia and Commagene,` → `its earliest notice is Plutarch's Cilician pirates, its Greek intermediaries are visible in Commagene,`
- **Fixed.** Carry forward 1 says priority rights were sold; body says granted to favoured states `on priority rights sold to cities,` → `on priority rights granted to favoured cities,`
- **Fixed.** Carry forward 2 names a Spartan king who was Eleusinian and Samothracian initiate; body has no such person `the same person could be a Spartan king, an Eleusinian initiate and a Samothracian ring-wearer,` → `the same person could be an Eleusinian initiate and a Samothracian ring-wearer,`
- **Fixed.** Orphism dispute box: 'Bernabé and Graf and Johnston (2007)' reads ambiguously `Bernabé and Graf and Johnston (2007) hold` → `Bernabé, and Graf and Johnston (2007), hold`

### Greece 8.3 (words 3,548, unchanged)

- **Fixed.** Self-test 4: 'A race, usually a diaulos' hedges where the body says flatly 'a diaulos run in helmet and shield'. `A race, usually a diaulos, run in helmet and shield` → `A diaulos run in helmet and shield`
- **Fixed.** Self-test 5: Cynisca victor 'without being present'; body says only 'without competing in person'. `without being present` → `without competing in person`
- **Fixed.** Self-test 6: Zanes 'inscribed with warnings'; body says only Pausanias read their inscriptions and names the bribers. `, lining the way into the stadium, inscribed with warnings; Pausanias` → `, lining the way into the stadium; Pausanias`
- **Fixed.** Self-test 10: 'inscriptions and site evidence suggest' contests into the fifth century; body credits only work on the inscriptions (Ebert, Sinn). `inscriptions and site evidence suggest` → `inscriptions suggest`
- **Left (check FAIL).** Self-test 7: '(IG I3 131)' loses the superscript the body prints (IG I<sup>3</sup> 131). Adds a <sup> element, which is not among AGENT-SPEC's permitted elements (the body's existing use does not make it valid), and 'IG I3 131' is an accepted plain-text form in the plain-text Self-test a…
- **Left (not real).** Theagenes 'won Olympic boxing in 480 and pankration in 476' gives no BC where the paragraph elsewhere does. The report routinely omits BC once the era is clear (c. 470–457, around 430, in 415, in 448 in the same paragraph); no fault against the spec.

### Greece 8.4 (words 2,714 → 2,723)

- **Fixed.** Self-test 1 answer: 'without strength or memory' overstates the body ('without strength or, usually, mind'); repeated in re-check `a witless image (<em>eidolon</em>) without strength or memory` → `an image (<em>eidolon</em>) without strength or, usually, mind`
- **Fixed.** Self-test 3 question: 'and what tells us about its function?' lacks a subject; repeated in re-check `What is a white-ground lekythos and what tells us about its function?` → `What is a white-ground lekythos and what detail tells us about its function?`
- **Fixed.** Self-test 3 answer: 'Attic' and 'deposited at graves' are not in the body; repeated in re-check `A fifth-century Attic oil flask painted with funerary scenes (tomb visits, Charon, Hermes) and deposited at graves;` → `A fifth-century oil flask painted with funerary scenes (tomb visits, Charon, Hermes);`
- **Fixed.** Self-test 5 answer: 'tower of Cronus on the Isle of the Blessed' and '(Olympian 2.68–80)' vs body 'tower of Cronus and the Isle of the Blessed', 2.56–80; repeated in re-check `tower of Cronus on the Isle of the Blessed` → `tower of Cronus and the Isle of the Blessed`
- **Fixed.** Self-test 6 answer: reason 'living judges were deceived by fine bodies, clothes and witnesses' not in body; citation 523a–524a vs body 523a–527a; repeated in re-check `The <em>Gorgias</em> (523a–524a): living judges were deceived by fine bodies, clothes and witnesses, so Zeus had the de…` → `The <em>Gorgias</em> (523a–527a): Zeus strips the dead of their bodies so that scarred souls are seen naked.`
- **Fixed.** Self-test 9 answer: '("where two winds blow", the bellows)'; body never explains the riddle as the bellows; repeated in re-check `("where two winds blow", the bellows)` → `("where two winds blow")`
- **Fixed.** Self-test 10 answer: 'curse tablets were deposited in their graves' extends to all four categories; body says graves of the untimely dead `curse tablets were deposited in their graves to use them as couriers` → `curse tablets were deposited in graves of the untimely dead to use them as couriers`
- **Fixed.** Brasidas at Amphipolis: quotation 'enclosed his tomb, and sacrifice to him as a hero, with games and yearly offerings' breaks tense, 'ever afterwards' cut; repeated in re-check `buried him inside the city before the agora, "enclosed his tomb, and sacrifice to him as a hero, with games and yearly …` → `buried him inside the city before the agora and enclosed his tomb; they "ever afterwards sacrifice to him as a hero", w…`
- **Fixed.** Ghosts: 'Oracles of the dead at Ephyra, Tainaron, Heraclea Pontica and Avernus are attested by Herodotus 5.92'; 5.92 covers only the Thesprotian oracle `Oracles of the dead at Ephyra, Tainaron, Heraclea Pontica and Avernus are attested by Herodotus 5.92, where Periander's…` → `Oracles of the dead are known at Ephyra, Tainaron, Heraclea Pontica and Avernus; at the Thesprotian one, on the Acheron…`

### Greece 8.5 (words 2,888, unchanged)

- **Fixed.** Farm, agora... para 1: '(Demosthenes 20.31–32), and The agora was' is a spliced sentence (stray 'and' before capital 'The') `a year (Demosthenes 20.31–32), and The agora was market` → `a year (Demosthenes 20.31–32). The agora was market`
- **Fixed.** Marriage... para 1: <blockquote> nested inside <p> (Demosthenes 59.122), invalid HTML leaving a stray </p> `states the purposes: <blockquote>hetairai for pleasure, concubines for daily care, wives to bear legitimate children</b…` → `states the purposes:</p> <blockquote>hetairai for pleasure, concubines for daily care, wives to bear legitimate childre…`
- **Fixed.** Self-test 2: 'interest paid at 18 per cent a year'; body says only 'paid 18 per cent interest' `interest paid at 18 per cent a year;` → `interest paid at 18 per cent;`
- **Fixed.** Self-test 10: 'corrupted the wife's loyalty and threatened the legitimacy of heirs'; body gives only the threat to legitimacy `Because it corrupted the wife's loyalty and threatened the legitimacy of heirs,` → `Because it threatened the legitimacy of heirs,`
- **Fixed.** Slaves and metics para 4: 'conventional and unjust (1253b20–23)' cited without book and chapter, unlike '1.3, 1253b' elsewhere `conventional and unjust (1253b20–23)` → `conventional and unjust (1.3, 1253b20–23)`

### Greece 9.1 (words 2,987 → 2,988)

- **Fixed.** Vase painting, Red-figure: Euthymides' boast 'as never Euphronios' is unmarked, so it reads as a garbled sentence (also re-check) `writes on one amphora, as never Euphronios.` → `writes on one amphora, <em>as never Euphronios</em>.`
- **Fixed.** Polykleitos and the canon: <blockquote> nested inside <p> is invalid HTML; following sentences fall outside the paragraph (also re-check) `and Philo Mechanicus quotes him: <blockquote>Perfection comes about little by little through many numbers.</blockquote>…` → `and Philo Mechanicus quotes him:</p> <blockquote>Perfection comes about little by little through many numbers.</blockqu…`
- **Fixed.** Self-test 5 answer: 'quotations in Galen' (body: Galen reports, only Philo quotes), 'Pliny's notice' (body cites Pliny only for the Diadoumenos), 'probably' vs body's 'almost certainly' (also re-checks) `probably the Doryphoros; known from quotations in Galen and Philo Mechanicus and from Pliny's notice.` → `almost certainly the Doryphoros; known from Galen's account of its doctrine and a quotation in Philo Mechanicus.`
- **Left (not real).** (re-check) Transliteration mixed (Kallimachos, Kallikrates, Polykleitos, Hephaistos, Peirithoos beside Phidias, Heracles, Dionysus); each name consistent, convention not Gods and heroes take the standard English forms AGENT-SPEC asks for, artists' names the k-forms standard in English art history; every name is spelled one way throughout, so there is no error to fix,…

### Greece 9.2 (words 2,744, unchanged)

- **Fixed.** The slopes: 'four-century sequence' runs from the Peisistratids (6th c. BC) to the Odeon (AD 160–174), about seven centuries (also re-check) `The slope is a four-century sequence:` → `The slope is a seven-century sequence:`
- **Fixed.** Areopagus and Pnyx: 'the one place where you stand where the sovereign body stood' has a doubled 'where' `this is the one place where you stand where the sovereign body stood` → `this is the one place you can stand where the sovereign body stood`
- **Fixed.** Self-test 7 answer: 'the archaeology shows no phase securely datable to 404/3' says more than the body (also re-check) `the archaeology shows no phase securely datable to 404/3, and the later phases are themselves disputed.` → `Homer Thompson tied it to the second phase, about 404/3, but others doubt the Thirty built anything, and the phase date…`
- **Fixed.** Self-test 3: asks for 'two reasons', the answer lists three (also re-check) `No altar or priestess of Athena Parthenos is attested, Pausanias never calls it a temple, and the ancient cult image` → `No altar or priestess of Athena Parthenos is attested, and Pausanias never calls it a temple; the ancient cult image`
- **Fixed.** Walking orders, Day 2 midday: 'Hadrian's Library' is nowhere in the body and not in the one-day Skipped row (lead and re-check) `Roman Agora, Tower of the Winds, Hadrian's Library; lunch in Plaka` → `Roman Agora, Tower of the Winds; lunch in Plaka`
- **Fixed.** Walking orders, Day 1 midday: 'Philopappos Hill' is called 'the Hill of the Muses' in the body `Philopappos Hill and the Pnyx; lunch in Koukaki` → `Hill of the Muses and the Pnyx; lunch in Koukaki`
- **Fixed.** Possessives of -s names inconsistent: 'Pericles'' against 'Pheidias's', 'Theseus's', 'Ephialtes's', 'Cleisthenes's', 'Alkamenes's' (lead and re-check; occurrence 1 of 2) `Pericles' speech of 431/0` → `Pericles's speech of 431/0`
- **Fixed.** Possessives of -s names inconsistent: 'Euripides'' (same lead, occurrence 2 of 2) `from Euripides' lost` → `from Euripides's lost`
- **Fixed.** (re-check) Self-test 10 answer: 'Shaft Grave V dates to about 1550–1500 BC'; the body dates the Mask, not the grave `Shaft Grave V dates to about 1550–1500 BC` → `The mask dates to about 1550–1500 BC`
- **Left (not real).** Self-test 4 cites 'Pausanias 1.26.5–27.2'; body cites 1.26.5–27.1 (Erechtheion) and 1.18.2, 1.27.2 (Pandroseion) The answer names the sea and trident marks (1.26.5) and the olive in the Pandroseion (1.27.2: 'About the olive they have nothing to say...'), so 1.26.5–27.2 spans both body citations; Perseus, Pausan…

### Greece 9.3 (words 2,773 → 2,783)

- **Fixed.** Byzantium section: Averroes' commentaries rendered into Latin by 'twelfth-century Toledo (Gerard of Cremona, Michael Scot)'; Ibn Rushd d. 1198, Gerard d. 1187, Scot's Averroes work is thirteenth-century; Figure 2 repeat… `Ibn Rushd (Averroes) wrote the commentaries that twelfth-century Toledo (Gerard of Cremona, Michael Scot) rendered into…` → `Gerard of Cremona in twelfth-century Toledo rendered Aristotle into Latin from Arabic, and Michael Scot in the early th…`
- **Fixed.** Current wave, games paragraph: 'puts Herodotus on a boat with the player, muddles its chronology freely' lacks 'and' `puts Herodotus on a boat with the player, muddles its chronology freely.` → `puts Herodotus on a boat with the player and muddles its chronology freely.`
- **Fixed.** Self-test 3 answer: 'for which there was no interest' is not in the body `not Homer, poetry or myth, for which there was no interest and no theatre to make sense of tragedy.` → `not Homer, poetry or myth: Homer was known only by name, and there was no theatre to make sense of tragedy.`
- **Fixed.** Self-test 7 answer: 'shaft graves at Mycenae date to the sixteenth century BC' is not in the body `The shaft graves at Mycenae date to the sixteenth century BC, about three centuries before any plausible date for a Tro…` → `The mask from the shaft graves at Mycenae is about three centuries older than any possible Trojan War.`
- **Fixed.** Self-test 8 answer (Vernant): 'knowledge, fate and pollution'; body says 'knowledge and pollution' `the play concerns knowledge, fate and pollution, not repressed wish` → `the play concerns knowledge and pollution, not repressed wish`
- **Fixed.** Self-test 10 answer: 'rape by Neptune in Athena's temple'; body says Poseidon and gives no temple `(rape by Neptune in Athena's temple)` → `(rape by Poseidon)`
- **Left (not real).** Victorian schools dispute box: 'argued in modules 10.10 and 10.2' in descending order; check the numbers The order is respective: the treasure is argued in 10.10 ('Troy the place: Hisarlik and the historicity question', Calder/Traill/Easton on Priam's Treasure) and the mask in 10.2 ('Agamemnon and the k…

### Greece 9.4 (words 8,087 → 8,088)

- **Fixed.** Tyrtaeus and the Rhetra described two ways: Part A Q5 'paraphrases it' vs Part C Q1 'is the first to quote it' `Tyrtaeus in the seventh century is the first to quote it` → `Tyrtaeus in the seventh century is the first to paraphrase it`
- **Fixed.** 'about' dropped: Part A Q9 and Part C Q3 say Theseus cycle on vases 'from about 510'; Carry forward 2 says 'Theseus in 510' `Theseus in 510, the Furies in 458` → `Theseus in about 510, the Furies in 458`
- **Left (not in scope).** Figures 3 and 4 drawing model answers sit outside the collapsed details, breaking the closed-book rule Lead concerns figures; out of scope (and the report has only two figures, both on the scoring rules, not on model answers).

### Greece 10.1 (words 2,955 → 2,959)

- **Fixed.** Self-test 1 says Pindar 'first states' the son would 'overthrow' his father; body says 'clearest statement' and 'mightier than his father'. `Which source first states that Thetis' son by a god would overthrow his father` → `Which source gives the clearest statement that Thetis' son by a god would be mightier than his father`
- **Fixed.** Self-test 9 calls the Odyssey a 'later text' than the Aethiopis; the body never says so. `which later text makes the shade regret death` → `which text makes the shade regret death`
- **Fixed.** Self-test 10 cites Plutarch, Alexander 15; body gives 15.8–9. `Plutarch, <em>Alexander</em> 15, adds` → `Plutarch, <em>Alexander</em> 15.8–9, adds`
- **Fixed.** 'Pelion and Scyros': Chiron 'raises him with his wife Philyra'; Philyra is Chiron's mother (wife Chariclo); check Nemean 3.43. `who raises him with his wife Philyra` → `who raises him in the home of his own mother, Philyra`
- **Fixed.** 'Menis, Briseis, and the Shield': 'Benoit de Sainte-Maure' usually spelt 'Benoît'. `Benoit de Sainte-Maure` → `Benoît de Sainte-Maure`

### Greece 10.2 (words 3,190, unchanged)

- **Fixed.** Sceptre para 1: 'two steps from a god's forge' does not match the six-hand-over chain just given. `The authority is two steps from a god's forge,` → `The authority is six hand-overs from a god's forge,`
- **Fixed.** Self-test 7 answer: 'every Odyssey account ... 11.405–434 ... at a banquet'; body cites 11.385–464 and gives the banquet only for Proteus (and the shade's 'died at dinner'), not Zeus or Nestor. `4.512–537; 11.405–434) Aegisthus kills him at a banquet with Clytemnestra's complicity.` → `4.512–537; 11.385–464) Aegisthus kills him with Clytemnestra's complicity.`
- **Fixed.** Self-test 8 answer: 'Odysseus returns disguised and tests Penelope'; body says only that he does everything Agamemnon did not. `Odysseus returns disguised and tests Penelope;` → `Odysseus lands in secret and does not trust his house as Agamemnon did;`
- **Fixed.** Self-test 2 answer: wanax 'with the largest temenos'; body says only three times that of the lawagetas (PY Er 312). `the palace ruler with the largest <em>temenos</em>,` → `the palace ruler whose <em>temenos</em> is three times that of the <em>lawagetas</em>,`
- **Fixed.** Self-test 9 answer: 'no name is attached to anyone at Mycenae'; body says narrower: no Linear B tablet from Mycenae names a king. `but no name is attached to anyone at Mycenae.` → `but no Linear B tablet from Mycenae names a king.`
- **Left (not real).** Citation form: 'Pindar (Pythian 11.22–25)' in carpet paragraph vs 'Pindar (Pyth. 11.31–32)' in the next aside. Different passages (the motive question vs Amyclae); full title at first mention, abbreviation after, is the report's pattern (Herodotus 1.67–68, then Hdt. 7.159).
- **Left (not real).** Section title 'Iphigenia: four moral weights' beside figure 1 caption's 'five sources'. Five sources carry four placements of the weight (Cypria and Hesiodic Catalogue share the divine, rescued version); the counts measure different things, and the caption is a figure, which may not cha…

### Greece 10.3 (words 3,279 → 3,283)

- **Fixed.** Self-test 4 answer cites 22.99–107; body cites only 22.104 for Hector's admission `22.99–107, calling it his own <em>atasthaliai</em>.` → `calling it his own <em>atasthaliai</em> (22.104).`
- **Fixed.** Self-test 5 answer cites 24.725–775; body gives funeral 24.719–804, Helen 24.762–775 `Andromache, Hecuba, Helen (24.725–775).` → `Andromache, Hecuba, Helen (24.719–804).`
- **Fixed.** Self-test 7 answer cites Hera's argument as 16.440–457; body has 16.431–461 `(16.440–457)` → `(16.431–461)`
- **Fixed.** Self-test 8 answer says 'Phrygian slave' in Orestes; body says 'Phrygian eunuch' `the cowardly Phrygian slave in Euripides'` → `the cowardly Phrygian eunuch in Euripides'`
- **Fixed.** Self-test 10 answer identifies Iulus with Ascanius (not stated in body) and cites Divus Julius 6 where body has 6.1 `Through Iulus, identified with Aeneas' son Ascanius, and so to Venus; Caesar's funeral speech for Julia (Suetonius, <em…` → `Through Aeneas' son Iulus, and so to Venus; Caesar's funeral speech for Julia (Suetonius, <em>Divus Julius</em> 6.1)`
- **Fixed.** 'Iris remarks that the allies are of "many tongues" (2.803–804; 4.437–438)': 4.437–438 is narrator, not Iris `Iris remarks that the allies are of "many tongues" (2.803–804; 4.437–438)` → `Iris (2.803–804) and the narrator (4.437–438) remark that the allies are of "many tongues"`
- **Fixed.** 'Pausanias adds that she ended in Asia with Pergamus' has no passage cited `Pausanias adds that she ended` → `Pausanias (1.11.2) adds that she ended`

### Greece 10.4 (words 3,371, unchanged)

- **Fixed.** Self-test 7 answer: 'best of mortals in counsel and speech' is not in the body (13.287-310: best among gods for metis as he is among mortals) `That he is the best of mortals in counsel and speech, and she is famous among the gods for metis;` → `That she is best among the gods for metis as he is among mortals;`
- **Fixed.** Self-test 8 question: 'Pindar's and Euripides' hostility ... converge' subject-verb disagreement `Why do Pindar's and Euripides' hostility to Odysseus` → `Why do Pindar's and Euripides' hostilities to Odysseus`
- **Fixed.** Self-test 8 answer cites Iphigenia at Aulis for Odysseus as demagogue; body cites it (524) only for the insult 'son of Sisyphus' / Self-test 8 answer: Pindar's 'fame outran his deeds' vs body (Nemean 7) 'fame exceeds hi… `makes him the man whose fame outran his deeds because Homer's sweet speech and the Danaans' secret ballots favoured tal…` → `makes him the man whose fame exceeded his sufferings because Homer's sweet speech and the Danaans' secret ballots favou…`
- **Fixed.** Self-test 10 question: 'Dante's Ulisse' - body never uses the Italian form; uses Latin/later 'Ulysses' `Dante's Ulisse` → `Dante's Ulysses`
- **Fixed.** Self-test 5 answer: 'one of whom' attaches to the spies; body has one of the girls arguing `Trojan girls, overheard by Greek spies, one of whom argues with Athena's prompting for Odysseus over Ajax.` → `Trojan girls, overheard by Greek spies; one of the girls argues, with Athena's prompting, for Odysseus over Ajax.`

### Greece 10.5 (words 3,534, unchanged)

- **Fixed.** Self-test 1: question and answer say the Cypria is the first text to make Nemesis Helen's mother; the body never says first, and its dispute box leaves priority undecided. `and which text first makes Nemesis her mother?<details><summary>Answer</summary><p>Leda (the swan, Euripides Helen 17–2…` → `and which text makes Nemesis her mother?<details><summary>Answer</summary><p>Leda (the swan, Euripides Helen 17–21) and…`
- **Fixed.** Self-test 5: answer says the drug is given 'so no one can react'; the body says only that the drug lets the room sit through the second story. `She has just drugged the wine with a pain-killing Egyptian pharmakon, so no one can react.` → `She has just drugged the wine with a pain-killing Egyptian pharmakon, which lets the room sit through the second story.`
- **Left (check FAIL).** Self-test 6: answer quotes Republic 586c as saying men fought over the eidolon 'as Stesichorus says'; the body quotes 586c only as 'the eidolon of Helen, in ignorance of the truth'. Fault not real: Republic 586c does say the eidolon was fought over 'as Stesichorus says' (Stesichoros phesi), which fits the body's framing of 586c within the Palinode; the replacement removes the St…
- **Left (not real).** Afterlives: 'Pallinode' (H.D.'s part title) beside 'Palinode' everywhere else; could read as a typo. H.D.'s Helen in Egypt (1961) titles its first part 'Pallinode' in her own spelling (cf. Cambridge, Modernist Hellenism, chapter 'Pallinodes and Eidola'); the report quotes the title correctly.

### Greece 10.6 (words 3,324, unchanged)

- **Fixed.** Self-test Q4: 'Patroclus plays the role of Cleopatra' and 'returns only when his own people are desperate' go beyond the body `and returns only when his own people are desperate, so the gifts no longer matter; Patroclus plays the role of Cleopatr…` → `and returns too late, in Book 18, when the gifts no longer matter; Cleopatra, the wife who moves Meleager, inverts the …`
- **Fixed.** Self-test Q9: 'the gap at the collarbone (22.322–325)'; body says 'the gap at the throat' `so Achilles knows the gap at the collarbone (22.322–325)` → `so Achilles knows the gap at the throat (22.322–325)`
- **Fixed.** Self-test Q10: 'Weaving a purple cloak and ordering a hot bath for Hector's return'; body says only 'weaving and heating Hector's bath' `Weaving a purple cloak and ordering a hot bath for Hector's return (22.440–446).` → `Weaving and heating Hector's bath (22.440–446).`
- **Fixed.** Blockquote order: Book 9 has 9.412–413 before 9.378 and 9.401 (part 1 of 2) `<blockquote>My homecoming is lost, but my fame will be imperishable (9.412–413)</blockquote> <blockquote>I count him at…` → `<blockquote>I count him at the worth of a splinter (9.378)</blockquote> <blockquote>Not worth my life are all the posse…`
- **Fixed.** Blockquote order: Book 22 has 22.304–305 before 22.262 (part 2 of 2) `<blockquote>Let me not die without a struggle and without glory (22.304–305)</blockquote> <blockquote>There are no trus…` → `<blockquote>There are no trustworthy oaths between lions and men (22.262)</blockquote> <blockquote>Let me not die witho…`
- **Fixed.** Inconsistent term: 'a dance-floor' (Book 18, and figure) against 'the dancing-floor' ('The Shield and the world outside') `the dancing-floor recalls Andromache's wedding veil` → `the dance-floor recalls Andromache's wedding veil`
- **Left (not real).** Self-test Q2: answer quotes 'I would feel shame...' (6.442 = 22.105); body blockquote has 'deep shame' at 6.441–442 The repeated line is 6.442 = 22.105 (aideomai Trōas kai Trōadas helkesipeplous), as the body itself says twice; 'deep' renders mal' ainōs at the end of 6.441, which is not repeated in Book 22, so the…
- **Left (not real).** Self-test Q8: sceptre oath cited 1.234–244; body gives the sceptre as 1.234–237 within the speech 1.225–244 Different referents: the oath itself runs from 'by this sceptre' (1.234) to its end (1.244), inside the body's 1.225–244; the body's 1.234–237 cites only the leafless-sceptre image, which the answer'…
- **Left (not real).** 'The maids who mourned Hector alive at 6.500': the Book 6 section says only 'They mourned Hector' and mentions no maids The Greek at 6.498–500 has Andromache find her many handmaids (amphipoloi) and rouse lament in them; they mourn Hector alive. The cross-reference is accurate and does not contradict the Book 6 quotat…

### Greece 10.7 (words 3,240 → 3,238)

- **Fixed.** Self-test 3: answer gives the Greek word mythos, which the body never gives (also re-check). `Telemachus substitutes "speech" (<em>mythos</em>), and` → `Telemachus substitutes "speech", and`
- **Fixed.** Self-test 7: 'news of his son Neoptolemus' prowess'; body says only 'news of Neoptolemus' (also re-check). `news of his son Neoptolemus' prowess.` → `news of his son Neoptolemus.`
- **Fixed.** Self-test 8: answer gives only 11.602–604 as suspected in antiquity, omitting Aristarchus' athetesis of 11.568–627 (also re-check). `<p>11.602–604 (Heracles' phantom and deified self), attributed in the scholia to Onomacritus; modern analysts` → `<p>11.602–604 (Heracles' phantom and deified self), attributed in the scholia to Onomacritus, and the whole stretch 11.…`
- **Fixed.** Self-test 9: 'no background or suspense'; body says 'everything foregrounded', no suspense. `with no background or suspense, unlike Genesis` → `with no background, unlike Genesis`
- **Fixed.** Inconsistent italics: kleos italic 3 times, roman 6 (Agamemnon section, Nostos against kleos body, Carry forward 3); metis italic in body, roman in Carry forward 3. `good fame (<em>kleos</em>) may be his` → `good fame (kleos) may be his`
- **Fixed.** Inconsistent italics (continued): kleos in 'The Cyclops read in full'. `abandons <em>outis</em> for <em>kleos</em> and shouts` → `abandons <em>outis</em> for kleos and shouts`
- **Fixed.** Inconsistent italics (continued): kleos in 'The ending'. `Penelope's undying <em>kleos</em> against` → `Penelope's undying kleos against`
- **Fixed.** Inconsistent italics (continued): metis (and bie) roman in Carry forward 3. `nostos over kleos, metis over bie, oikos` → `nostos over kleos, <em>metis</em> over <em>bie</em>, oikos`
- **Left (not real).** Self-test 4: question cites the simile as 8.523–531, body as 8.523–524 (also re-check). The body cites only the quoted line pair; the full simile runs 8.523–531 (ὡς δὲ γυνή at 523, closing ὣς Ὀδυσεύς at 531), so the question's range is right (Dickinson College Commentaries, Od. 8.521–53…
- **Left (not real).** Self-test 6: 'curse to Poseidon (9.528–535)' and 'late, solitary return'; body cites 9.534–535, says 'prayer', 'lose all his comrades' (also re-check). The prayer runs 9.528 (κλῦθι, Ποσείδαον) to 9.535, with 9.536 'so he spoke praying' (Dickinson College Commentaries, Od. 9.500–566); the body quotes only its last lines, links Poseidon's anger to the…
- **Left (not real).** Self-test 5: Outis/mē tis/metis; body uses outis at 9.502–505 without a gloss, the 9.366 quote gives only 'Nobody'. The answer says nothing the body lacks: the body quotes 'Nobody is my name' (9.366), glosses 'nobody (mē tis)' and then uses outis for that name, so the term is glossed by context; the rule forbids f…
- **Left (not real).** (re-check) Self-test 1: 'cattle of Helios (1.8–9)' while the body's dispute box cites the cattle at 1.7–9. 1.7 is the recklessness line (atasthaliēisin), which the same answer cites separately; the cattle are named at 1.8–9 (βοῦς Ὑπερίονος Ἠελίοιο / ἤσθιον), so the answer is exact and the body's 1.7–9 sim…
- **Left (not real).** (re-check) Demodocus' first song cited as 8.72–82 in one section and 8.75–78 in another. Different scopes: 8.72–82 is the song with its frame, 8.75–78 the lines on the quarrel of the 'best of the Achaeans' (ἄριστοι Ἀχαιῶν, 8.78), which is the point made in 'Metis against bie'.

### Greece 10.8 (words 3,936, unchanged)

- **Fixed.** Self-test 5 answer cites Iliad 2.558; the body gives 2.557–8 (also the re-check lead) `Through the disputed line <em>Iliad</em> 2.558` → `Through the disputed line <em>Iliad</em> 2.557–8`
- **Fixed.** Self-test 6 answer says Polybius, Strabo and Plutarch show the practice was real; the body rests that on the inscription alone (also the re-check lead) `regulating the supplying families, together with Polybius, Strabo and Plutarch, shows the practice was real.` → `regulating the supplying families shows the practice was real.`
- **Fixed.** Self-test 10 answer states Apollo's punishment as fact; the body gives it only as Pindar's version, not Euripides' (also the re-check lead) `according to Euripides. This was Apollo's punishment for killing Priam at an altar.` → `according to Euripides. In Pindar this was Apollo's punishment for killing Priam at an altar.`
- **Left (not real).** Self-test 7 answer links the Pithekoussai debate to Iliad 11.632–7, which the dispute box does not cite The body cites 11.632–7 for Nestor's golden cup and the Pithekoussai paragraph contrasts the clay cup with "the heavy golden one of legend"; the answer combines two body statements without adding a c…
- **Left (not real).** Locrian dispute box: "the claim that the rite went back to the Bronze Age" has no matching claim in the body The body presents the rite as atonement for Ajax's crime at the sack of Troy, running "for a thousand years, so the story ran"; that is the legend's claim of a Trojan War (Bronze Age) origin the box …

### Greece 10.9 (words 3,599 → 3,587)

- **Fixed.** Self-test 3: '16.658: Hector recognises the turning of Zeus' sacred scales and flees'; 'the turning' is not in the body. `16.658: Hector recognises the turning of Zeus' sacred scales and flees.` → `16.658: Hector recognises Zeus' sacred scales and flees.`
- **Fixed.** Inconsistent form: body 'Homeric Problems (first century AD)' vs Self-test 10 '(Homeric Problems, 1st century AD)' (also re-check). `Heraclitus (Homeric Problems, 1st century AD)` → `Heraclitus (Homeric Problems, first century AD)`
- **Fixed.** Deception of Zeus dispute box names Janko twice; the closing 'Janko (vol. 4, 1992) reads the episode as both comic and cosmological' repeats the earlier Janko sentence (also re-check). `Janko (vol. 4, 1992) reads the episode as both comic and cosmological.</aside>` → `</aside>`
- **Fixed.** Self-test 8: 'Homer makes gods into men' keeps only half the chiasmus the body gives ('makes his men gods and his gods men'). `said Homer makes gods into men, and the theomachy` → `said Homer makes his men gods and his gods men, and the theomachy`
- **Fixed.** Self-test 4: 'every god will then want to save a favourite son'; body (16.431-61 paragraph) says only 'a favourite'. `every god will then want to save a favourite son.` → `every god will then want to save a favourite.`
- **Left (unsettled).** 'told in module 4.1': check that module 4.1 tells the courtship of Thetis and Themis' prophecy. Settling it needs greece/r-4.1.html, which this agent is barred from opening; the maintainer or checker should confirm 4.1 covers the courtship, Themis' prophecy and the marriage to Peleus.

### Greece 10.10 (words 3,158, unchanged)

- **Fixed.** Troy II dated 'roughly 2500–2300 BC' in body and Self-test 3 vs 'c. 2550–2250 BC' in table (body sentence) `in the mid-third millennium BC (roughly 2500–2300 BC)` → `in the mid-third millennium BC (roughly 2550–2250 BC)`
- **Fixed.** Self-test 6: 'large lower city (about 27 hectares, several thousand people)' but body's 27 ha is the whole site, 'perhaps' `had a large lower city (about 27 hectares, several thousand people)` → `had a large lower city (the whole site perhaps 27 hectares, with several thousand people)`
- **Fixed.** Units of length: 'about 6 km' and table 'about 90 m' vs 'metres' spelled out in prose `about 6 km from the Dardanelles` → `about 6 kilometres from the Dardanelles`
- **Left (check FAIL).** Self-test 3: Troy II 'c. 2500–2300 BC' vs table; and 'Taken from Berlin by Soviet forces in 1945' says more than the body (combined) Date fix is right, but the Berlin half is not a real fault (body: given to Berlin 1881, disappeared 1945, taken by a Soviet trophy brigade) and the rewrite adds an unneeded 1881 clause while 'lost th…
- **Left (check FAIL).** Self-test 8: 'equal "brother"' not said of the Tawagalawa letter in body; 'nearest text to a Hittite-Ahhiyawan dispute over Troy' not in body Leaves the 'equal brother' half of the lead untouched, and the new clause merely restates the preceding 'over which the two had been hostile'; ending at 'have made peace.' would be the minimal fix.
- **Left (not real).** Self-test 2: coring rebuttal stated more firmly than the dispute box's 'partly answered' The dispute box itself says coring by Kraft and colleagues 'showed' the shoreline lay much closer to the citadel; 'partly' qualifies how far it answers Strabo, not the coring result, and the answer c…
- **Left (unsettled).** Dispute box: 'The Luwian-language question (Watkins on the Trojans' speech) belongs to module 10.3' – dangling or misnamed? 'module 10.3' is the form AGENT-SPEC prescribes for a sibling Greek module, so the wording is right; whether 10.3 actually covers the Luwian question and Watkins needs greece/r-10.3.html or the sylla…

### Greece 10.11 (words 2,734, unchanged)

- **Fixed.** Self-test 7 answer says Eumaeus was 'kidnapped by Phoenicians'; the body says 'carried off by a Phoenician slave-woman'. / Self-test 7 answer says 'not a hereditary caste' and 'capture, trade and birth'; the body says '… `Slavery was a fall in status, not a hereditary caste. Eumaeus was a king's son kidnapped by Phoenicians and sold to Lae…` → `Slavery was a fall in status, not an innate condition. Eumaeus was a king's son carried off by a Phoenician slave-woman…`
- **Fixed.** Self-test 6 answer 'whether gift exchange can still contain violence' differs from the body's 'whether goods can still buy back what violence has taken'. `whether gift exchange can still contain violence` → `whether goods can still buy back what violence has taken`
- **Left (not real).** 'colonial foundations like Scheria's' implies archaeology supplied the fictional Scheria's foundation. The phrase is a comparison: archaeology found eighth-century colonial foundations of the kind the poem describes for Scheria (as with the temples and Phoenician traders in the same list); it does not…

### Greece 10.12 (words 3,899 → 3,880)

- **Fixed.** Medieval Troy paras 2-3: Lydgate's Troy Book introduced twice, dated 1412–20 and 1412–1420 (with re-check) `was translated across Europe; Lydgate's <em>Troy Book</em> (1412–20) is Guido turned into English verse at four times t…` → `was translated across Europe. Boccaccio's`
- **Fixed.** Dares and Dictys: papyrus is P.Tebt. 2.268 in body and Self-test 5 but P.Tebt. 268 in dispute box (with re-check) `the Tebtunis papyrus (P.Tebt. 268)` → `the Tebtunis papyrus (P.Tebt. 2.268)`
- **Fixed.** Self-test 2 answer: 'Trojan by descent but Italian by name'; body says 'Latin by name' (with re-check) `Rome is Trojan by descent but Italian by name` → `Rome is Trojan by descent but Latin by name`
- **Fixed.** Self-test 6 asks for 'three reasons'; the answer gives four (with re-check) `<li>Give three reasons medieval readers preferred Dares and Dictys to Homer.` → `<li>Give four reasons medieval readers preferred Dares and Dictys to Homer.`
- **Fixed.** Self-test 9 answer: 'taken from Berlin in 1945'; body says only 'vanished in 1945' `It was taken from Berlin in 1945 and has been acknowledged` → `It vanished from Berlin in 1945 and has been acknowledged`
- **Fixed.** Early modern section: 'Achilles of Benoît, Guido and Lydgate, who kill Hector ... and send the Myrmidons' makes the authors the subject (re-check) `who kill Hector unguarded and send the Myrmidons against Troilus` → `who kills Hector unguarded and sends the Myrmidons against Troilus`
- **Fixed.** Suetonius cited as Julius 39.2, Augustus 43.2, Nero 38.2 in body but 39, 43, 38 in Self-tests 3-4 (re-check) `Suetonius (<em>Julius</em> 39; <em>Augustus</em> 43) records that Caesar and Augustus staged it, and that Augustus drop…` → `Suetonius (<em>Julius</em> 39.2; <em>Augustus</em> 43.2) records that Caesar and Augustus staged it, and that Augustus …`
- **Left (not real).** Dares and Dictys dispute box: 'the tin box'; body says only 'a box in Dictys' tomb' (with re-check) The definite article refers back to the body's box, and 'tin' is accurate: the Latin prologue has the tablets in a tin box (arcula stagnea); see en.wikipedia.org/wiki/Dictys_Cretensis and the prologu…
- **Left (unsettled).** Schliemann dispute box: two consecutive cross-references to module 10.10; confirm both belong there Settling it needs the 10.10 and 10.3 reports, which this agent may not open; open is whether 10.10 covers both the treasure dispute and the Kolb–Korfmann quarrel (if so, the two sentences could merge…

### Greece 11.1 (words 2,737, unchanged)

- **Fixed.** Self-test 7 answer spells 'pezetairoi'; the body's army list has 'Pezhetairoi' (also the re-check lead on the same spelling) / (re-check) Formatting: Self-test work titles not italicised; 'Theophrastus HP 3.12.2' abbrev… `Theophrastus HP 3.12.2 on the sarissa; Demosthenes 9.48–50 on year-round war; Demosthenes 2.17 on the pezetairoi` → `Theophrastus, <em>Historia Plantarum</em> 3.12.2 on the sarissa; Demosthenes 9.48–50 on year-round war; Demosthenes 2.1…`
- **Fixed.** Self-test 1 answer: Badian 'suspected it of being Alexander I's own propaganda'; body applies Badian's reading to 5.17–21 and 9.44–45, not 5.22 `It also shows that the claim had to be argued, and Badian suspected it of being Alexander I's own propaganda.` → `It also shows that the claim had to be argued.`
- **Fixed.** Self-test 2 answer: 'semi-independent cantons' is not the body's wording (also the re-check lead) `Until Philip II the uplands were semi-independent cantons.` → `Until Philip II bound them to the crown, their loyalty was negotiable.`
- **Fixed.** Self-test 8: 'the seventh' marriage is never numbered in the body, and 'the powerful Attalus' is not in the body / (re-check) Self-test 8 answer: 'fully Macedonian' and 'Epirote' are not in the body, which has only Atta… `Cleopatra was a Macedonian noblewoman, niece of the powerful Attalus. A son by her could be presented as fully Macedoni…` → `Cleopatra was a Macedonian noblewoman, niece of Attalus. A son by her could be presented as the "legitimate" heir Attal…`
- **Fixed.** (re-check) Formatting: Self-test work titles not italicised (Self-test 4, 'Politics 7.1324b') `Aristotle (Politics 7.1324b)` → `Aristotle (<em>Politics</em> 7.1324b)`
- **Fixed.** (re-check) Formatting: Self-test work titles not italicised (Self-test 9, 'Politics 5.1311b' and 'Phoenix 1963') `(Aristotle, Politics 5.1311b; Diodorus 16.93). E. Badian, "The Death of Philip II" (Phoenix 1963).` → `(Aristotle, <em>Politics</em> 5.1311b; Diodorus 16.93). E. Badian, "The Death of Philip II" (<em>Phoenix</em> 1963).`
- **Fixed.** (re-check) Formatting: Self-test work titles not italicised (Self-test 10, 'Isocrates' Philippus') `How does Isocrates' Philippus, though` → `How does Isocrates' <em>Philippus</em>, though`
- **Left (not real).** (re-check) Self-test 5 answer: 'the pottery dates' where the body says 'the pottery' 'The pottery dates' is only the dating of the pottery, which is the sole sense in which the body's 'the pottery' is an argument; the answer gives no date and adds no claim.

### Greece 11.2 (words 2,724, unchanged)

- **Fixed.** Self-test 5 answer adds 'and horses' and 'passed through harmlessly to be dealt with in the rear'; body says only drivers shot and lanes opened for the rest (also re-check) `The Agrianians and javelin men shot the drivers and horses, and the infantry opened lanes so that the surviving chariot…` → `The Agrianians and javelin men shot the drivers, and the infantry opened lanes for the rest (Arrian 3.13.5–6).`
- **Fixed.** Self-test 7 answer: 'Weeks of noisy feints' (body: night after night) and 'about 5,000 horse and 6,000 foot' (table: no 'about') (also re-check) `Weeks of noisy feints along the bank dulled Porus' reactions. Alexander then took about 5,000 horse and 6,000 foot` → `Night after night, noisy feints along the bank dulled Porus' reactions. Alexander then took 5,000 horse and 6,000 foot`
- **Fixed.** Self-test 8 answer: 'allowed him to blockade both harbours'; body says only that Tyre, outnumbered, closed its two harbours (also re-check) `That gave him command of the sea, allowed him to blockade both harbours, and let him use ship-mounted rams against the …` → `That gave him command of the sea: outnumbered, Tyre closed its two harbours, and he could bring ship-mounted rams again…`
- **Fixed.** Self-test 9 answer: 'question his figures for the army's size and train'; body says only 'dispute many of his figures' (also re-check) `question his figures for the army's size and train.` → `dispute many of his figures.`
- **Fixed.** Self-test 3 answer: 'reached Issus on Alexander's line of communication'; body says Darius 'came down behind him at Issus' `reached Issus on Alexander's line of communication` → `came down behind him at Issus`
- **Left (not real).** Table: Diodorus' Granicus figures and Curtius/Diodorus Gaugamela losses carry no passage while neighbouring figures do AGENT-SPEC allows author and work only where the writer is not sure of the passage; each figure names its author, so the rule is met. Adding passages would be a new citation, outside this pass.
- **Left (not real).** (re-check) Table, Hydaspes Decisive move: 'Coenus took the Indian horse from behind' states as fact what the dispute box calls contested The body states the same (Coenus sent 'to fall on the Indian cavalry from behind', Arrian 5.16.3); the dispute box contests Coenus' route to that position, not that he struck the Indian horse from be…

### Greece 11.3 (words 2,748 → 2,751)

- **Fixed.** Self-test 2 answer: stray comma before '(Diodorus 16.40–51)' (also re-check) / Self-test 2 answer: 'crushed the Phoenician revolt' not in body, which says only 'burned rebel Sidon in 345' (also re-check) `He crushed the Phoenician revolt and burned Sidon (345), reconquered Egypt in 343/2 after some sixty years of independe…` → `He burned rebel Sidon (345), reconquered Egypt in 343/2 after some sixty years of independence (Diodorus`
- **Fixed.** Self-test 1 answer: 'a royal inspector reporting directly to the king' goes beyond body's 'a real office of royal inspection' (also re-check) `It was probably a royal inspector reporting directly to the king, enlarged` → `It was probably a real office of royal inspection, enlarged`
- **Fixed.** Self-test 4 answer: 'burn the crops and countryside to starve Alexander's army' goes beyond body's 'burn the crops' (also re-check) `burn the crops and countryside to starve Alexander's army, and take` → `burn the crops and take`
- **Fixed.** Offers section: 'During the siege of Tyre' cited to Arrian 2.25.1–3 and Plutarch 29.7–8, but dispute box says Plutarch sets it at Tyre in 331 after Egypt; Plutarch range 29.7–8 vs 29.7–9 (also re-check on the range) `During the siege of Tyre, Darius offered` → `During the siege of Tyre, according to Arrian, Darius offered`
- **Fixed.** Same lead, Self-test 7 part: question repeats 'during the siege of Tyre' while the answer cites Plutarch too `What did Darius offer during the siege of Tyre` → `What did Darius offer at Tyre`
- **Fixed.** (re-check) Self-test 5 answer: 'his greater numbers and cavalry could not deploy'; body mentions numbers only `his greater numbers and cavalry could not deploy` → `his greater numbers could not deploy`
- **Fixed.** (re-check) Naming: body 'the Hall of a Hundred Columns' vs Self-test 8 'the Hundred Columns Hall' `the Apadana and the Hundred Columns Hall` → `the Apadana and the Hall of a Hundred Columns`
- **Left (not real).** Gaugamela section: 'Astronomical Diaries I, year −330' is an astronomical year beside BC dates, unexplained −330 is the diary's designation in Sachs and Hunger's own numbering (astronomical years), so the citation is correct as the edition names it; the paragraph and Self-test 8 give the battle as 1 Octobe…

### Greece 11.4 (words 2,920 → 2,921)

- **Fixed.** Self-test 3 answer lists the sweating statue of Orpheus and the eagle at Gaugamela, which are not in the body (also re-check) `Any three of: Philip's dream of the lion seal on Olympias' womb; the sweating statue of Orpheus; the bird dropping a st…` → `Any three of: Philip's dream of the lion seal on Olympias' womb; the bird dropping a stone at Gaza; the birds eating th…`
- **Fixed.** Self-test 6 answer 'son of Amun-Ra' against body 'son of Ra and of Amun' (also re-check) `any pharaoh was by definition son of Amun-Ra` → `any pharaoh was by definition son of Ra and of Amun`
- **Fixed.** The journey: 'adds two reasons' followed by three clauses joined by 'and', so the count is unclear `the oracle was reputed infallible, and Perseus and Heracles had consulted it, and Alexander` → `the oracle was reputed infallible and had been consulted by Perseus and Heracles; and Alexander`
- **Fixed.** Self-test 10 answer says Arrian is better supported by the letter to Cleomenes and the relief; body says only that Arrian's 'hero' fits the Pella evidence `Arrian's version is better supported by the letter to Cleomenes ordering hero-shrines and by the votive relief from Pel…` → `Arrian's version is more cautious and fits the votive relief from Pella dedicated to Hephaestion as hero.`
- **Fixed.** Self-test 2 answer 'lay badly wounded'; body 'lay wounded' `as he lay badly wounded (Arrian 6.10.2)` → `as he lay wounded (Arrian 6.10.2)`
- **Fixed.** Self-test 7 answer cites Herodotus 1.134 for 'the Great King was not a god'; body cites 1.134 only for the scale of greeting `For Persians, proskynesis was a social gesture of deference to a superior, and the Great King was not a god (Herodotus …` → `For Persians, proskynesis was a social gesture of deference to a superior (Herodotus 1.134), and the Great King was not…`
- **Left (check FAIL).** Self-test 8 answer adds Prometheus' cave; body names only Heracles' failure at Aornos (also re-check) Arrian 5.3.1-4 gives Eratosthenes' examples as Prometheus' cave, the Caucasus and the club-branded cattle, not Aornos, so the fault is in the body; the replacement deletes the one correct example and…
- **Left (not real).** Siwa dated 'winter of 332/1' in The journey but '331' in Did he believe it? and Carry forward Compatible forms: a winter 332/1 visit falls in early 331, and the timeline figure already pairs them ('Siwa (winter 332/1)' at 331).
- **Left (not real).** 324 section: Hyperides, Against Demosthenes cited without fragment or column number AGENT-SPEC allows author and work only where the writer is not confident of the number; the citation is not wrong, and adding a column number would be a new citation.

### Greece 11.5 (words 2,752 → 2,758)

- **Fixed.** Heading 'Breaking the old guard, 330–327' vs Carry forward 'broken in 330–328'; body has Coenus dying 326 `Philip's men, bound by kinship, were broken in 330–328,` → `Philip's men, bound by kinship, were broken in 330–326,`
- **Fixed.** Parmenion's killers named as Cleander, Sitalces, Menidas (Arrian 3.26.3–4), but 'After India' calls Cleander, Sitalces and Heracon 'Parmenion's killers' `executed Cleander, Sitalces and Heracon (Parmenion's killers)` → `executed Cleander, Sitalces and Heracon (whom Curtius names among Parmenion's killers)`
- **Fixed.** Self-test 3 cites '(Diodorus 17.80; Curtius 7.2)' where the body cites Arrian 3.27.4 and Diodorus 17.80.4; 'letters home were censored' vs body 'soldiers' letters were opened' `letters home were censored, and malcontents were put in a separate disciplinary unit (Diodorus 17.80; Curtius 7.2).` → `soldiers' letters were opened, and malcontents were put in a separate disciplinary unit (Arrian 3.27.4; Diodorus 17.80.…`
- **Fixed.** Self-test 9 dates the executions '325–324'; body gives only 'Emerging from Gedrosia' `the executions of 325–324 were` → `the executions after Gedrosia were`
- **Fixed.** Self-test 10: 'Dropped: proskynesis for Greeks and Macedonians'; body says only 'proskynesis for Greeks' `Dropped: proskynesis for Greeks and Macedonians,` → `Dropped: proskynesis for Greeks,`
- **Fixed.** Self-test 2: 'too dangerous to leave in command'; body has Arrian judge it 'unsafe to leave alive' a father whose son had been executed `was too dangerous to leave in command.` → `was too dangerous to leave alive.`
- **Fixed.** Opis dispute box: 'On the Fortune of Alexander (329)': bare '329' reads as a year; it is the Moralia page `<em>On the Fortune of Alexander</em> (329)` → `<em>On the Fortune of Alexander</em> (<em>Moralia</em> 329)`
- **Fixed.** Self-test 5: 'died in India of obesity and lice'; body has 'died in India, obese and lice-ridden', a state not a cause `died in India of obesity and lice (Arrian` → `died in India, obese and lice-ridden (Arrian`

### Greece 11.6 (words 2,888 → 2,890)

- **Fixed.** Self-test 5 answer adds 'helped end the Sogdian resistance' and 'signalled that Iranian elites could join the ruling class', not in the body `It bound Oxyartes' family, the leading Bactrian aristocrats, to the regime and helped end the Sogdian resistance. It al…` → `It bound Oxyartes' family, the leading Bactrian aristocrats, to the regime. It also made an Iranian woman the probable …`
- **Fixed.** Self-test 7 answer adds 'would balance Taxiles' and 'royal magnanimity'; body says only that Alexander reconciled Porus with Taxiles `more cheaply than a satrap and would balance Taxiles. It also fitted the image of royal magnanimity in the "as a king" …` → `more cheaply than a satrap. Alexander also enlarged his territory and reconciled him with Taxiles.`
- **Fixed.** Self-test 6 answer says Eratosthenes called 'both' (Aornos and Nysa) flattery; body gives his verdict only on Nysa/Dionysus and Prometheus' cave `and he records Eratosthenes' view that both were flattery.` → `and he records Eratosthenes' view that the Nysa stories were flattery.`
- **Fixed.** Self-test 2 answer 'nose and ears' vs body 'nose and ear-lobes' `Mutilation of the nose and ears` → `Mutilation of the nose and ear-lobes`
- **Fixed.** Assessment calls it 'Achilles' shield' at the Mallian town; body says only 'the sacred shield from Troy' `and Achilles' shield at the Mallian town` → `and the sacred shield from Troy at the Mallian town`
- **Fixed.** Assessment 'Persian court dress' vs body 'Median dress' (Arrian 4.7.4) `Iranian cavalry, Persian court dress, Roxane` → `Iranian cavalry, Median dress, Roxane`
- **Fixed.** Carry forward 1: Hyphasis as 'the first limit Alexander's own troops imposed on him' is not in the body `The army's refusal there is the first limit Alexander's own troops imposed on him.` → `The army's refusal there was, on most scholars' reading, a real limit that Alexander's own troops imposed on him.`
- **Fixed.** Spelling: satrapy 'Aria' beside city 'Alexandria in Areia' in the same paragraph `the foundation of Alexandria in Areia` → `the foundation of Alexandria in Aria`
- **Left (not real).** Assessment: Callisthenes' protest and 'Iranian cavalry' are not described in the body Both are accurate summaries of passages the body cites or sits beside: Callisthenes' opposition to proskynesis is in Arrian 4.10-12 (body cites 4.10-14), Cleitus' outburst in 4.8-9, and the Iranian c…

### Greece 11.7 (words 3,206 → 3,215)

- **Fixed.** Opening sentence: 'at least 270 years' after 323 BC conflicts with the table's Diodorus date c. 60–30 BC (263 years at earliest); also noted on re-check. `written at least 270 years` → `written at least 260 years`
- **Fixed.** Self-test 3 answer: 'Plutarch draws on both it and the Arrian tradition' is not in the body; also noted on re-check. `Plutarch draws on both it and the Arrian tradition.` → ``
- **Fixed.** Self-test 4 answer: 'shifts blame for the slaughter' to Perdiccas; body mentions no slaughter or blame. `which shifts blame for the slaughter to Ptolemy's later enemy` → `which diminishes Ptolemy's later enemy`
- **Fixed.** Self-test 7 answer: 'Vespasian (AD 69/70)' where the body says 'Vespasian after 69'; also noted on re-check. `Vespasian (AD 69/70)` → `Vespasian (after AD 69)`
- **Fixed.** Romance dispute box: stray comma before '(Theodor Nöldeke, ...)'; also noted on re-check. / Romance dispute box: 'the Syriac Romance' has no referent; the list names only the Syriac Alexander Legend (c. 630), a differen… `The older view that the Syriac Romance was translated from a lost Middle Persian version, implying an early Iranian ado…` → `The older view that the Syriac version of the Romance (distinct from the <em>Alexander Legend</em>) was translated from…`
- **Fixed.** Possessives in -s inconsistent: 'Aristobulus's book' against 'Curtius'', 'Nearchus'', 'Darius''. `Aristobulus's book` → `Aristobulus' book`
- **Left (not in scope).** Figure 1 caption uses curly quotes and apostrophes where the body uses straight ones. Inside <figure class="viz">; no figure may change.

### Greece 11.8 (words 2,872, unchanged)

- **Fixed.** Length of the illness (1 of 2): 'What killed him' says 'roughly twelve days of fever' beside the heading 'Eleven days in Daesius' and the table 18 to 28 Daesius (also the re-check lead) `roughly twelve days of fever` → `roughly eleven days of fever`
- **Fixed.** Length of the illness (2 of 2): theory table 'drink alone does not explain twelve days' (re-check lead) `drink alone does not explain twelve days` → `drink alone does not explain eleven days`
- **Fixed.** Self-test 2 answer: 'Diodorus says it allowed worship as a god'; body says 'sacrifice as to a god' (Diodorus 17.115.6) `Diodorus says it allowed worship as a god.` → `Diodorus says it allowed sacrifice as to a god.`
- **Fixed.** Self-test 6 answer: 'White hellebore was known to Greek medicine'; body names only Veratrum album 'known to Greek physicians' (also the re-check lead) `White hellebore was known to Greek medicine` → `It was known to Greek physicians`
- **Fixed.** Self-test 8 answer: 'The funeral carriage left Babylon in 321'; body gives 321 only for Ptolemy meeting it in Syria (also the re-check lead) `The funeral carriage left Babylon in 321 and was diverted by Ptolemy in Syria to Egypt.` → `The funeral carriage left Babylon and in 321 was diverted by Ptolemy in Syria to Egypt.`
- **Left (check FAIL).** Self-test 7 answer: 'Arrian records the story but does not believe it'; body says only he records it 'so as not to seem ignorant of it' (7.27.3) (also the re-check lead) Fault is real, but the replacement also changes 'the story' to 'it', which is not needed and leaves the first 'it' ambiguous after 'some versions say Aristotle advised'; use 'Arrian records the story…
- **Left (not real).** 'Eleven days in Daesius' table: no row for Daesius 23, and the text does not say the day is missing The table follows Plutarch 76, which dates no entry to the 23rd (Perrin, Loeb 1919, via lexundria.com and perseids.org); listing only the dated days is not an error and the table claims no unbroken r…
- **Left (not in scope).** (found while checking the table lead, not in LEADS) Table row dates the Sarapis consultation to Daesius 27 Outside the leads; not applied. Plutarch 76 puts it on the 26th: 'he was speechless, as he was also on the twenty-sixth ... During this day, too, Python and Seleucus were sent to the temple of Serapi…
- **Left (not real).** 'The body': the possible ends of the tomb (270s, 365, 390s) carry no citation The three dates are correct for well-known events (Aurelian's sack of Alexandria's palace quarter c. 272; the tsunami of 21 July 365; the anti-pagan violence of the 390s, Serapeum 391/2), the sentenc…

### Greece 12.1 (words 3,472 → 3,474)

- **Fixed.** Simplicius' commentary titled two ways: 'Commentary on Aristotle's Physics' 144.25–28 vs 'Commentary on the Physics' 24.26–25.1 (also the re-check) `(<em>Commentary on Aristotle's Physics</em> 144.25–28)` → `(<em>Commentary on the Physics</em> 144.25–28)`
- **Fixed.** Burkert first named without first name ('Burkert and Zhmud'); Zhmud never gets a first name or a work `the dispute between Burkert and Zhmud` → `the dispute between Walter Burkert and Leonid Zhmud`
- **Fixed.** Self-test 1 answer: 'the frame of a material cause is his too' and 'Thales left no words of his own' go beyond the body (also the re-check) `and the frame of a material cause is his too. Thales left no words of his own.` → `and the frame, his four causes, is his too; for Thales there is only Aristotle's guess at an argument.`
- **Fixed.** Self-test 7 answer: 'so infinitely many stages are crossed in infinitely many moments' not in the body (also the re-check) `, so infinitely many stages are crossed in infinitely many moments` → ``
- **Fixed.** Self-test 9 answer: 'Both fault the absence of a working final cause'; body ties final causes only to the Empedocles objection (also the re-check) `Both fault the absence of a working final cause:` → `Both fault an account of order in which no cause does the work:`
- **Fixed.** Self-test 10 answer: 'read and cited within the fifth century'; body dates the commentator 'about 400 BC or a little earlier' (also the re-check) `being read and cited within the fifth century` → `already being read and cited`
- **Left (not real).** Self-test 8 answer: 'uncuttable, unchanging atoms'; body says 'uncuttable ones' and 'properties of Melissus' One', not 'unchanging' Body says each atom has the properties of Melissus' One and gives B 8 (hot becoming cold means 'we did not see rightly'), so the One, and each atom, is unchanging by the body's own account.

### Greece 12.2 (words 3,357 → 3,358)

- **Fixed.** Gorgias' title spelled 'On Not Being' (heading, body, Self-test 4) and 'On Not-Being, or On Nature' (Sextus paragraph). `<em>On Not-Being, or On Nature</em>` → `<em>On Not Being, or On Nature</em>`
- **Fixed.** Self-test 2 answer adds 'settled by events' and 'not everyone is a measure even of his own future'; body (177c–179b) says only that doctor or legislator judges better than layman. `Judgements about what will prove healthy or advantageous are settled by events, and experts make them better than layme…` → `Judgements about what will prove healthy or advantageous are made better by doctor or legislator than by layman, so not…`
- **Fixed.** Self-test 8 question says 'the daimonion'; the body calls it only 'the sign'. `accounts of the daimonion differ` → `accounts of Socrates' sign differ`
- **Fixed.** Self-test 9 answer says Critias and Alcibiades 'went bad after leaving'; body (1.2.14–16, 1.2.39) says they behaved well with him and left once they thought themselves his superiors. `behaved while with him and went bad after leaving` → `behaved well while with him, and left once they thought themselves his superiors`
- **Fixed.** Self-test 6 answer: Frogs 'still treats him as the type of the talking intellectual'; body (1491–1499) says it 'treats sitting chattering beside Socrates as a fashion'. Looser paraphrase. `still treats him as the type of the talking intellectual` → `still treats sitting chattering beside Socrates as a fashion`

### Greece 12.3 (words 3,392 → 3,393)

- **Fixed.** Self-test 1 answer: 'too little of the late style to be ordered' and 'the first group' are not what the body says (also re-check) `Stylometry measures closeness to that late style; the first group shows too little of it to be ordered, so its priority…` → `Style cannot settle the first group's internal order; that the short Socratic dialogues come first is inferred from con…`
- **Fixed.** Self-test 2 answer: Tübingen case said to rest on the Phaedrus, which the body never ties to it (also re-check) `the Tübingen case rests on the <em>Phaedrus</em> and on Aristotle's reports.` → `the Tübingen case rests on Aristotle's reports and on reading the dialogues' deferrals as reserve.`
- **Fixed.** Self-test 7 answer: describes the ascent ('from one body to beauty in general'), which the body leaves to module 6.5 (also re-check) `The ascent passes from one body to beauty in general and leaves the individual behind;` → `The ascent leaves the individual beloved behind;`
- **Fixed.** Self-test 8 answer: 'whose pieces can be regrouped' goes beyond the body's 'can change into one another' `built from the half-equilateral triangle, whose pieces can be regrouped; earth's cube` → `built from the half-equilateral triangle, so they can change into one another; earth's cube`
- **Fixed.** Carry forward 3: 'Demiurge' never used in the body ('the maker'); 'and the receptacle, and the judgement' reads as a slip (also re-check) `The charioteer, the Demiurge and the receptacle, and the judgement of souls passed into` → `The charioteer, the maker, the receptacle and the judgement of souls passed into`
- **Fixed.** (re-check) Life, Sicily and the Academy para 2: spark passage (341c–d) cited as part of the digression (342a–344d), though it precedes it `The <em>Letter</em>'s digression (342a–344d) explains why Plato wrote no treatise: name, account, image and even knowle…` → `The <em>Letter</em> explains why Plato wrote no treatise: the thing itself is grasped only after long shared inquiry, s…`
- **Fixed.** (re-check) Self-test 5 answer: 'while it exists' not in body; 'many bodies ... many cloaks' where body has 'several' `A soul might outlast many bodies, as a weaver outlasts many cloaks, and still perish (87b–88b). The final argument show…` → `A soul might outlast several bodies, as a weaver outlasts several cloaks, and still perish (87b–88b). The final argumen…`

### Greece 12.4 (words 3,383, unchanged)

- **Fixed.** Self-test 7 asks for three readings of the productive intellect, but the Averroes reading concerns the receptive intellect; the question is too narrow for the body-faithful answer. `Give three readings of the productive intellect of <em>On the Soul</em> 3.5.` → `Give three readings of the two intellects of <em>On the Soul</em> 3.5.`
- **Fixed.** Self-test 6 answer swaps desire and love: 'as an object of love and thought moves those who desire it' against the body's 'as an object of desire and thought moves: it moves by being loved'. `It moves as an object of love and thought moves those who desire it (1072b3), its own activity being thinking of thinki…` → `It moves as an object of desire and thought moves, by being loved (1072b3), its own activity being thinking of thinking.`
- **Fixed.** Self-test 9 answer cites one range (1254b27–1255b4) where the body gives two passages, 1254b27–1255a1 and 1255a3–b4. `war enslaves the well-born (1254b27–1255b4).` → `war enslaves the well-born (1254b27–1255a1, 1255a3–b4).`
- **Fixed.** Self-test 2 answer has Eudemus ask for a sound text of the Physics; the body says of a passage of the Physics. `Eudemus' request to Theophrastus for a sound text of the <em>Physics</em> shows` → `Eudemus' request to Theophrastus for a sound text of a passage of the <em>Physics</em> shows`
- **Left (not in scope).** Quotation marks: straight quotes in the body, curly quotes in the figure captions. The curly quotes occur only inside figure captions (<figure class="viz">); the body is consistent with straight quotes, and no figure may change.

### Greece 12.5 (words 2,747 → 2,748)

- **Fixed.** Stilpo paragraph: 'Demetrius Poliorcetes, who took Megara in 307' lacks BC, unlike every other date in the report. `who took Megara in 307, whether` → `who took Megara in 307 BC, whether`
- **Fixed.** Self-test 3 answer: 'the oracle story looks like an aetiology of the slogan'; body never calls it an aetiology or names a slogan (also re-check). / Self-test 3 answer: 'the <em>Pordalus</em> has Diogenes confess' drops … `Diocles blames the father, Eubulides blames Diogenes, the <em>Pordalus</em> has Diogenes confess, and the oracle versio…` → `Diocles blames the father, Eubulides blames Diogenes, Diogenes is said to confess it in his <em>Pordalus</em>, and the …`
- **Fixed.** Self-test 7 answer: 'systematic Cyrenaic hedonism is third-generation' is an inference the body does not state (also re-check). `If so, systematic Cyrenaic hedonism is third-generation,` → `If so, the Cyrenaic end was first defined by the founder's grandson, not the founder,`
- **Fixed.** Self-test 9 answer: 'what logicians now call an opaque context' uses a term not in the body (also re-check). `It isolates what logicians now call an opaque context.` → ``
- **Left (not real).** Self-test 8 answer: 'life and death are indifferent' vs body's 'equally choiceworthy' (2.94–96). 'Indifferent' restates 'equally choiceworthy' without adding a claim; the answer agrees with the body.

### Greece 12.6 (words 2,857, unchanged)

- **Fixed.** Self-test 5 answer: 'so happiness depends on satisfying the first and dropping the last' goes beyond the body; 'empty desires have no limit' rewords KD 15 as the body gives it. `Natural wealth is limited and easy to get, while empty desires have no limit (KD 15), so happiness depends on satisfyin…` → `Nature's wealth is limited and easy to get, the wealth of empty opinion unlimited (KD 15); whoever is not hungry, thirs…`
- **Fixed.** Self-test 8 answer assigns topics to KD 1-4 ('the gods, death, the limit of pleasure, the endurance of pain'); the body only says the clauses follow KD 1-4 and never gives KD 4. `The clauses summarise KD 1–4 in order: the gods, death, the limit of pleasure, the endurance of pain.` → `The clauses follow KD 1–4 in order.`
- **Left (not real).** 'Samos, Lampsacus and the Garden' gives 341–270 and then death in 271/0 without reconciling them. 271/0 is the Athenian archon year (Pytharatus, DL 10.15) spanning 271 and 270 BC, so it agrees with the end date 270; there is no conflict to reconcile.
- **Left (not real).** 'The sources': On Piety has no PHerc. number while On Signs (PHerc. 1065) and On Death (PHerc. 1050) do. On Piety survives across several rolls (PHerc. 1077, 1098, 1428 and others; Obbink's edition), so no single number fits; AGENT-SPEC permits author and work only, and adding numbers would be a new cit…

### Greece 12.7 (words 2,853 → 2,870)

- **Fixed.** Self-test 8 answer says pleasure 'cannot be the natural end, as Epicurus claimed'; body only makes pleasure the Epicurean first object and a by-product (also the re-check lead). `Pleasure is only a by-product, so it cannot be the natural end, as Epicurus claimed.` → `Pleasure, which Epicurus made the first object, is only a by-product that supervenes once the animal has what suits it.`
- **Fixed.** Stobaeus cited as 2.75–76 / 2.76 (page) and as 2.7 (chapter) without telling the reader which system is which. `usually credited to Arius Didymus (2.7).` → `usually credited to Arius Didymus (<em>Anthology</em> 2.7; its passages are cited here by the volume and page of Wachsm…`
- **Left (not in scope).** Quotation marks: body and table use straight quotes, figure captions use curly quotes. Body, table and Self-test use straight quotes consistently; the only curly quotes are inside figure captions, which may not change.
- **Left (not in scope).** (re-check) Figure 2 caption: plural subject with singular 'is left out'. Inside <figure class="viz">; no figure may change.
- **Left (not real).** (re-check) Self-test 1 answer says 'kept its substance' where the body says 'kept its things'. A faithful paraphrase of Cicero's res/verba contrast; the answer says no more than the body.

### Greece 12.8 (words 2,828, unchanged)

- **Fixed.** Self-test 3 answer says Carneades' grades answer the inaction charge; the body never says so `What are Carneades' grades of persuasive impression, and what objection do they answer?<details><summary>Answer</summar…` → `What are Carneades' grades of persuasive impression, and which matters call for the higher grades?<details><summary>Ans…`
- **Fixed.** Self-test 5 answer: 'nearly a genuine Stoic (2.132)' alters the body's 'but for a very few changes, a most genuine Stoic' `which made him, Cicero says, nearly a genuine Stoic (2.132)` → `which made him, Cicero says, but for a very few changes, a most genuine Stoic (2.132)`
- **Fixed.** Carry forward 1: 'Iamblichus' answer made the last pagan schools communities of cult' goes beyond the body `Iamblichus' answer made the last pagan schools communities of cult as well as of study` → `Iamblichus' answer made Proclus' school at Athens a community of cult as well as of study`
- **Left (not real).** Carry forward 2: Latin Outlines of 1562, Montaigne and Descartes not in body, unsourced A forward pointer, and accurate: Henri Estienne's (Stephanus') Latin Outlines, 1562, with Montaigne and Descartes among those it reached (Wikipedia 'Sextus Empiricus'; standard in Popkin, History of …
- **Left (not real).** Carry forward 3: pseudo-Dionysius, Theology of Aristotle and Book of Causes not in body, unsourced A forward pointer, and accurate: pseudo-Dionysius draws on Proclus; the Theology of Aristotle is an Arabic paraphrase of Enneads 4-6; the Book of Causes (Liber de causis) is drawn from Proclus' Eleme…
- **Left (not real).** 'His pupil Antiochus of Ascalon read them' depends on the Philo paragraph; figure 2 sat between them On disk the Philo and Antiochus paragraphs are adjacent; figure 2 now follows the Antiochus paragraph (already moved). Figure placement is in any case out of scope.
- **Left (not real).** Spelling: 'Khusro I' in the body against 'Khosroes' in Priscian's title Deliberate: the title keeps the traditional form of its Latin source (Solutiones ad Chosroem; English translation 'Priscian: Answers to King Khosroes of Persia', Bloomsbury); the body consistently us…
- **Left (not real).** Self-test 1 answer: 'indeterminacy of things' where the body says 'the nature of things' The body states that nature as things being 'equally indifferent, unmeasurable and undecidable', which is what 'indeterminacy' names; the answer says no more than the body.

## Found in the pass, outside it (left for a later row)

Faults the fixers and checkers met that a Self-test fix could not reach, or that lay outside the leads. None was applied here; each is a proposed backlog row (P61).

- **Greece 1.1.** The body table lists Final Palatial under the Platon phase; Platon's scheme is four phases (checker).
- **Greece 1.3.** The Self-test has nine questions; AGENT-SPEC asks for ten. The same holds for Greece 10.2 and 12.7.
- **Greece 1.2, 1.3, 4.2, 10.9, 10.10, 10.12.** Cross-references to other modules ("module 4.1", "module 10.3", "module 10.10") could not be settled: the fixer sees only its own report.
- **Greece 0.1.** Figure 1's caption says "at least five centuries" where the corrected text no longer does.
- **Greece 2.2.** The Zeus dispute box misreads Iliad 15.166 (checker).
- **Greece 2.4.** A tree's order of children differs from Apollodorus' (checker).
- **Greece 4.5.** Pindar's dates are given out of order (checker).
- **Greece 5.4.** An event dated "mid-seventh century" in the text has no year a date line can carry; its figure prints 650 BC.
- **Greece 6.6.** The allied 35,000 is unsourced, and the figure caption now differs from the corrected text.
- **Greece 7.3.** The OGIS 338 dispute box says the decree treats the will's ratification as fact; the decree (IvP 249) says Rome had still to ratify it. The Polybius 6.56 sentence should read that fear keeps the masses in check and the magistrates honest. Both are body faults; the Self-test answers were left as they were.
- **Greece 9.3.** The body now separates Gerard of Cremona (Aristotle from Arabic) from Michael Scot (Averroes, from about 1217); figure 2's third step still says "twelfth century: Gerard of Cremona, Michael Scot".
- **Greece 10.3.** The body cites Suetonius, Divus Julius 6.1 for descent through Iulus; Suetonius names Venus only.
- **Greece 10.10.** Self-test 3 still dates Troy II 2500–2300; the body and table say c. 2550–2250 (the proposal failed on its other half).
- **Greece 11.4.** Arrian 5.3.1–4 gives Eratosthenes' examples as Prometheus' cave, the moved Caucasus and the branded cattle, not Aornos; the body and Self-test 8 need fixing together.
- **Greece 11.8.** The day-by-day table dates the Sarapis consultation to Daesius 27; Plutarch, Alexander 76 puts it on the 26th.
- **Greece 12.2.** Aristophanes, Frogs 1491–1495 says it is graceful not to sit chattering beside Socrates; the body's "as a fashion" may misread it.
- **Rome 2.5.** Carry forward 3's "Phrygian eunuchs" says more than the body (checker).
- **Rome 5.4.** Caesar's figures are hedged in the Latin and not in the English (checker).
- **Rome 7.4.** Dio's remark sits in the wrong paragraph (checker).
