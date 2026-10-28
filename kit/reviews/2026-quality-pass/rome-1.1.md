# Rome 1.1: The peoples of Iron Age Italy

Verdict: fix
Body words: 2808 (target 2500)

## Coverage
- Final Bronze Age background (Terramare, Proto-Villanovan cremation cemeteries): covered
- Villanovan culture (biconical urns, hut urns, shift to inhumation, warrior elite): covered
- Latial culture and its phases: covered
- Early cemeteries of Rome (Forum burials, Esquiline) and of the Alban Hills: covered
- Osteria dell'Osa: covered
- Latins as a people; Latin festival, Diana at Aricia, thirteen altars at Lavinium: covered
- Latin League: covered
- Sabines: covered (closing section)
- Oscan- and Umbrian-speaking peoples; Samnites; Iguvine Tables: covered
- Veneti, Ligurians, Messapians, Picenes: thin (one line each)
- Languages, Indo-European and not, and the spread of the alphabet: covered
- Greek colonies seen from Italy (Pithekoussai and Cumae; Magna Graecia and Sicily): covered (Magna Graecia and Sicily thin)
- Nestor cup and the first writing in Latium: covered
- Phoenicians in the west: covered
- Pointer back to Greek module 5.2: covered
- Sabines as a first case of method, with pointer to module 1.4: covered

## Findings
1. [error] [accuracy] Section "The Sabines: a first exercise in method".
   Current: "The story is first attested in Ennius, more than five centuries after the supposed events"
   Problem: Fabius Pictor, the first Roman historian and slightly earlier than Ennius' Annales, already told it: Plutarch cites Fabius for the seizure of the Sabine women in the fourth month after the foundation.
   Fix: "The story is first attested in Fabius Pictor (Plutarch, <em>Romulus</em> 14.1), more than five centuries after the supposed events"
   Basis: Plutarch, Romulus 14.1, "in the fourth month after the founding of the city, as Fabius writes" (https://lexundria.com/plut_rom/14/prr).

2. [should-fix] [lane] Section "Sabellic Italy and the other peoples".
   Current: "Arnaldo Momigliano objected that Vofionus is barely understood and the scheme imposed."
   Problem: Module 2.1 ("Origins: numen and the three functions") gives the Iguvine Jupiter, Mars and Vofionus as Dumézil's evidence and Momigliano's objection (History and Theory, 1984); module 1.5 repeats Momigliano against the scheme. This is a third box on the same quarrel. As 2.1 and 1.5 report it, Momigliano's objection is to the method as unfalsifiable; an objection by him specific to Vofionus could not be confirmed.
   Fix: delete the aside, and add at the end of the preceding paragraph, after "exactly as Cato's farmer does (<em>On Agriculture</em> 141).": " The text is Hellenistic, so how much Iron Age ritual it preserves is unknown; Dumézil's reading of its triad is weighed in module 2.1."
   Basis: rome/r-2.1.html and rome/r-1.5.html; a search for a Momigliano statement on Vofionus found none (not conclusive).

3. [should-fix] [lane] Section "Greeks and Phoenicians, seen from Italy".
   Current: "Barry Powell (<em>Homer and the Origin of the Greek Alphabet</em>, 1991) took the cup as evidence that the alphabet was adopted to record hexameter"
   Problem: Whether the cup's joke presupposes our Iliad is Greek material, already covered by Greek module 5.1 and argued in a dispute box in Greek module 10.8 ("Nestor: speech, Pylos and a cup"); the spec says refer to the Greek module and do not retell. The second half of the box (the bones) is new and worth keeping.
   Fix: replace the box's first sentence, from "Barry Powell" to "an older oral tradition about Nestor.", with "Whether the joke presupposes our <em>Iliad</em> is Greek module 10.8."
   Basis: greece/r-10.8.html and greece/r-5.1.html; AGENT-SPEC.md, Rome course rules.

4. [should-fix] [lane] Section "The Latins: shared cults and the League".
   Current: " The priest, the <em>rex Nemorensis</em>, held office by killing his predecessor (Strabo 5.3.12), Frazer's starting point in <em>The Golden Bough</em>."
   Problem: The same anecdote, with the same citation, is in module 0.2 (Lake Nemi row, with Frazer) and in module 2.2 (Diana); here the point of the bullet is Cato's list without Rome.
   Fix: delete.
   Basis: rome/r-0.2.html, "Myths pinned to places"; rome/r-2.2.html, Diana profile.

5. [should-fix] [figure] Section "Latial culture: Rome, the Alban Hills and Osteria dell'Osa".
   Current: "by two and a half centuries or nearly four."
   Problem: Raising c. 1000 BC by the box's own fifty to a hundred years puts the oldest graves 300 to 350 years before 753, not nearly four centuries.
   Fix: "by two and a half centuries, or by up to three and a half."
   Basis: arithmetic from the box's own figures.

6. [minor] [accuracy] Section "The Latins: shared cults and the League".
   Current: "whose bronze Cicero still saw (<em>Pro Balbo</em> 53)"
   Problem: Cicero says "we remember" that it was recently to be seen on a bronze column behind the Rostra (nuper ... meminimus ... fuisse), implying it was gone by 56 BC; module 3.3 has it right ("Cicero remembered its bronze column").
   Fix: "whose bronze column Cicero remembered behind the Rostra (<em>Pro Balbo</em> 53)"
   Basis: Pro Balbo 53, "even lately we remember that this was to be found engraved and inscribed on a brazen column behind the rostra" (https://attalus.org/cicero/balbus.html).

7. [minor] [accuracy] Section "The Latins: shared cults and the League" (dispute box).
   Current: "dated by Polybius (3.22) to 509"
   Problem: Modules 0.3 and 1.6 convert Polybius' synchronism (twenty-eight years before Xerxes crossed) to 508/7.
   Fix: "dated by Polybius (3.22) to 508/7"
   Basis: Polybius 3.22.1–2; rome/r-0.3.html; rome/r-1.6.html.

8. [minor] [accuracy] Section "Languages and alphabets".
   Current: "<tr><td>Etruscan, Raetic</td><td>Not Indo-European</td><td>c. 700</td></tr>"
   Problem: c. 700 is right for Etruscan, but Raetic inscriptions begin in the fifth century BC.
   Fix: "<tr><td>Etruscan, Raetic</td><td>Not Indo-European</td><td>c. 700 (Etruscan); 5th c. (Raetic)</td></tr>"
   Basis: not checked online: standard handbook dating of the Raetic corpus (fifth to first centuries BC).

9. [minor] [accuracy] Section "The Sabines: a first exercise in method".
   Current: "And Rome conquered the Sabines in 290, just before Fabius Pictor wrote."
   Problem: 290 is some ninety years before Fabius wrote, about 200 BC; "just before" overstates the closeness.
   Fix: "And Rome conquered the Sabines in 290, less than a century before Fabius Pictor wrote."
   Basis: dates in the report and in module 0.1.

## Confirmed
- Gigante and colleagues, PLoS One 2021: more than one individual in tomb 168, at least three adults, none a child; Buchner's earlier identification a juvenile of about 10 to 14 (https://doaj.org/article/f5d7bfb3c3074c73998b5be7b30bc17a; https://www.livescience.com/tomb-nestors-cup-multiple-individuals). Note for the maintainer: Greek 5.1 ("a child's cremation") and Greek 10.8 ("a boy's cremation grave") now contradict this; outside this pass.
- Strabo 5.3.12: the Nemi priest a runaway slave who has killed his predecessor (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Strabo/5C*.html).
- Velleius 1.7.2–4: Cato's Capua founded about 260 years before its capture; Velleius prefers about 830 years before his own day (Loeb text).
- Strabo 5.4.2 (woodpecker of the Picentes) and 5.4.12 (bull of the Samnites, wolf of the Hirpini) (Loeb text).
- Livy 4.37 (Capua taken, 423) and 4.44 (Cumae, 421) (Latin text).
- Livy 1.13.5 (Quirites from Cures), 1.13.8 (Titienses), 2.16.4–5 (Attus Clausus, 504), 1.18.4 ("disciplina tetrica ac tristi veterum Sabinorum"), 1.7.8 (Evander and letters), 1.1 (Antenor and the Veneti) (Latin text).
- Tacitus, Annals 11.14: Demaratus taught the Etruscans, Evander the Aborigines (Latin text).
- Dionysius 4.49: Superbus founds the Latin festival for forty-seven peoples; 6.95: the Cassian treaty (Loeb text).
- Pliny, Natural History 3.69: the populi Albenses who took meat on the Alban Mount (Latin text).
- Cato, Origines, in Priscian: Egerius Baebius, "dictator Latinus", and the eight peoples as listed, Rome absent (FRH fragment text).
- Festus, citing Cincius: Latin meetings at the caput Ferentinae down to the consul P. Decius Mus, 340 (Lindsay text).
- Varro, On the Latin Language 5.74 (Tatius' altars "Sabinum linguam olent", with Saturn, Sol, Vulcan and Diana) and 5.144 (Lavinium, "dii Penates nostri") (Latin text).
- Herodotus 7.170: Cretan Iapygians and the slaughter of the Tarentines (text).
- Thucydides 6.2.6 (Phoenicians round Sicily) and 6.3 (Naxos 734, Syracuse 733) (text).
- Cato, On Agriculture 141: the paired-synonym lustration prayer (Latin text).
- Iguvine Tables found at Gubbio in 1444; Jupiter, Mars and Vofionus Grabovius at the gates; second triad with Fisus Sancius; Etruscans and Naharci cursed (standard editions).
- Dates and finds: Gozzadini at Villanova 1853; Boni's Forum cemetery from 1902; the 2006 cremation under the Forum of Caesar; Visconti 1817; Pinza 1905; Osteria dell'Osa, Bietti Sestieri 1992; Castagnoli's thirteen altars; Weinstock, JRS 1960; Marsiliana tablet; Buchner and Ridgway 1993; Huelva, González de Canales 2004; L'Amastuola, Burgers and Crielaard (standard).
- Modern titles and dates: Helbig 1879; Alföldi 1965; Cornell 1995; Poucet 1967; Powell 1991; Guarducci 1980; Ferro and Formigli 2011 (standard).
- Pointers true of their targets: module 1.2 (Etruscan origins), 1.3 (Aeneas' shrine at Lavinium), 1.4 (Palatine huts; Sabines in legend), 1.6 (Tarquinius Superbus' refuge at Cumae), Greek module 5.2 (colonisation).
- Incoming pointers true of 1.1: from 0.2 (cults and league), 0.3 (first Forum graves), 1.4 (Forum cemetery from the tenth century), 2.4 (both rites from the start), 3.3 (the league's older history; Lepontic by the sixth century), 3.4 (the Samnites' Sabellic background).
