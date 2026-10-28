# Rome 2.3: Priests, augury and the calendar

Verdict: fix
Body words: 2810 (target 2500)

## Coverage
- the great colleges (pontifices and pontifex maximus, augurs, quindecimviri and the Sibylline Books, epulones) and how members were chosen: covered
- the flamines, the Flamen Dialis and his taboos (Gellius 10.15): covered
- the rex sacrorum as the king's religious ghost: covered
- the Vestals: selection, privileges, fire, live burial: covered
- the Salii: covered
- the Arval Brothers and their inscribed records: covered
- the Luperci: covered (one sentence, plus the Lupercalia row in the table)
- the fetials and the spear: covered
- augury and the auspices, the templum, the sacred chickens, Claudius Pulcher at Drepana: covered
- haruspices and the Etruscan discipline: covered (the discipline handed off to 1.2)
- the calendar from Romulus' ten months and Numa to the late-Republican confusion and the Julian reform: covered
- the Fasti Antiates Maiores: covered
- a year of festivals (Lupercalia, Parilia, Vestalia, Consualia, October Horse, Saturnalia): covered
- Ovid's Fasti and its traps: covered

## Findings
1. [error] [accuracy] Section "The brotherhoods: Salii, Arvals, Luperci, fetials".
   Current: "their minutes were cut on marble there from 21 BC to the AD 240s"
   Problem: The datable inscribed protocols run to AD 304. The 240s are where the main series thins out, not where it ends.
   Fix: "their minutes were cut on marble there from 21 BC to AD 304"
   Basis: Scheid, Commentarii fratrum Arvalium qui supersunt: les copies épigraphiques des protocoles annuels de la confrérie arvale (21 av.–304 ap. J.-C.), 1998 (title as given in the Classical Review notice, cambridge.org); https://en.wikipedia.org/wiki/Acta_Arvalia ("The datable entries span from 21 BC to 304 AD").
2. [should-fix] [attribution] Section "Priests without a priestly caste".
   Current: "Tradition gave nearly every priesthood to Numa (Livy 1.20; module 1.5), but the colleges grew with the governing class."
   Problem: This covers regal-period material: Numa's priesthoods, and later the Flamen Dialis and the Salii, all from Livy 1.20 and 1.27. The report never says who tells it or how long after.
   Fix: "Tradition, written down some six centuries later, gave nearly every priesthood to Numa (Livy 1.20; module 1.5), but the colleges grew with the governing class."
   Basis: AGENT-SPEC source-criticism rule.
3. [should-fix] [attribution] Section "The calendar from Romulus to Caesar".
   Current: "Tradition gave Romulus ten months, March to December, 304 days"
   Problem: The ten-month year comes from antiquarians, from Junius Gracchanus to Censorinus (AD 238), writing six to ten centuries after Romulus' supposed date. The report does not say so.
   Fix: "Writers of six to ten centuries later gave Romulus ten months, March to December, 304 days"
   Basis: Censorinus 20.2 names Junius Gracchanus, Fulvius, Varro and Suetonius, and Ovid is Augustan; AGENT-SPEC source-criticism rule.
4. [should-fix] [attribution] Section "The brotherhoods: Salii, Arvals, Luperci, fetials".
   Current: "In Livy's procedure (1.32.5–14) the envoy calls Jupiter"
   Problem: The dispute box gives three regal founders, but the report never says that Livy wrote six centuries after Ancus' supposed reign.
   Fix: "In Livy's procedure (1.32.5–14), set down some six centuries after Ancus' supposed reign, the envoy calls Jupiter"
   Basis: AGENT-SPEC source-criticism rule.
5. [should-fix] [lane] Section "Haruspices in Roman service".
   Current: "Cato wondered that one haruspex could see another without laughing (<em>On Divination</em> 2.51)."
   Problem: 2.1 quotes the same jibe with the same citation, where it belongs, in its account of On Divination. 2.1 also tells the 163 BC Gracchus episode (On the Nature of the Gods 2.10–11) in one sentence. Here the same episode turns on the haruspices, which gives a reason to keep it in both, so only the Cato line needs to go.
   Fix: delete.
   Basis: rome/r-2.1.html, section "One activity: religion and politics"; crosscheck section 2 (2.1 ~ 2.3).
6. [minor] [accuracy] Section "The king's heirs: rex sacrorum, pontifex maximus, flamines".
   Current: "a man in chains entering his house was freed and the fetters dropped through the roof"
   Problem: In Gellius the fetters are drawn up through the impluvium onto the roof and let down into the street. They are not dropped through the roof.
   Fix: "a man in chains entering his house was freed and the fetters drawn up through the roof opening and let down into the street"
   Basis: Gellius 10.15.8, "vincula per impluvium in tegulas subduci atque inde foras in viam demitti".
7. [minor] [style] Section "The brotherhoods: Salii, Arvals, Luperci, fetials".
   Current: "yet Augustus had his name inserted into it (<em>Res Gestae</em> 10.1)"
   Problem: The Senate decreed the insertion in 29 BC, so by house style it was Octavian's name, and it was done by senatus consultum.
   Fix: "yet in 29 BC the Senate had Octavian's name inserted into it (<em>Res Gestae</em> 10.1; Dio 51.20.1)"
   Basis: Res Gestae 10.1, "senatus consulto"; Dio 51.20.1 (29 BC); AGENT-SPEC (Octavian until 27 BC).
8. [minor] [style] Sections "Priests without a priestly caste" and "Haruspices in Roman service".
   Current: "<em>On the Agrarian Law</em>" and "<em>On the Responses of the Haruspices</em>"
   Problem: These are speeches, so AGENT-SPEC wants Latin titles. 2.1 uses the singular "Response", so the two reports also disagree.
   Fix: "<em>De lege agraria</em>" and "<em>De haruspicum responso</em>"
   Basis: AGENT-SPEC citation conventions. "On the Agrarian Law" is also used elsewhere in the course (six uses).

## Confirmed
Checked against the texts as I know them, unless a URL is given.
- Livy 10.6–9 (lex Ogulnia: pontiffs 4 to 8, augurs 4 to 9; agrees with 3.1); 6.42.2 (decemviri sacris faciundis, half plebeian, 367); 33.42.1 (tresviri epulones, 196); Res Gestae 9.1 ("quattuor amplissima collegia")
- Cicero, De lege agraria 2.18 (lex Domitia of 104: 17 of 35 tribes, a minority); Dio 37.37.1 (Labienus, 63); Plutarch, Roman Questions 99 (augurs keep office even if convicted)
- Tacitus, Annals 6.12 (Sibylline Books replaced after 83, Erythrae among the sources); Suetonius, Augustus 31.1 (under Palatine Apollo)
- Festus s.v. ordo sacerdotum (pontifex maximus fifth); Varro, De lingua Latina 6.27–28; Plutarch, Roman Questions 63 (rex barred from office and from addressing the people; sacrifice in the Comitium, then flight); Livy 40.42 (Dolabella, 180)
- Livy 1.20.1–2; Gellius 10.15 (horse, army in array, oath, knots, pierced ring, she-goat, raw meat, ivy, beans, the apex, quotidie feriatus); Plutarch, Roman Questions 111 (animate statue); Suetonius, Julius 1; Dio 54.36.1 (Flamen Dialis filled in 11 BC)
- Ovid, Fasti 6.291; Gellius 1.12 (ages 6 to 10, patrima et matrima, Labeo and Capito, "te, Amata, capio" at 1.12.14); Dionysius 2.67.2 (thirty years, ten, ten and ten); Livy 26.27.14 (Palladium), 28.11.6 (flogging, 206), 22.57.2–3 (Opimia and Floronia); Plutarch, Numa 10; Ovid, Fasti 6.457–460; Pliny, Letters 4.11; Suetonius, Domitian 8.3–4
- Beard, JRS 70 (1980) and 1995; Parker, AJP 125 (2004)
- Livy 1.20.4 and 1.27.7 (Palatine and Colline Salii); Ovid, Fasti 3.259–392 (Mamurius and the ancilia); Quintilian 1.6.40; CIL VI 2104 (Carmen Arvale, acts of AD 218, "enos Lases iuvate"); Scheid, Romulus et ses frères (1990); Suetonius, Julius 76.1 (Luperci Iuliani); Pro Caelio 26
- Livy 1.32.5–14 (thirty-three days; spear "ferratam aut praeustam sanguineam"; three adult witnesses) and 1.24.7–8; Ovid, Fasti 6.205–208; Dio 50.4.5 (Octavian, 32 BC); Dionysius 2.72; Cicero, On the Republic 2.31; Wiedemann, CQ 36 (1986); Rich 1976; Watson 1993
- Festus' five kinds of signs; On Divination 2.82 (left lucky for a Roman, right for a Greek), 2.71–74 (chickens); Varro, De lingua Latina 7.6–9 (templum); Gellius 14.7.7; Livy 10.40 (Aquilonia, 293); On the Nature of the Gods 2.7 ("let them drink"); Polybius 1.49–52; Periochae 19; Valerius Maximus 1.4.3; Suetonius, Tiberius 2.2
- On the Nature of the Gods 2.10–11 (163: the rogator's death, "Tuscos ac barbaros", the consuls of 162 resign)
- Censorinus 20.2–3 and 20.7; Ovid, Fasti 1.27–44; Livy 1.19.6; months of 29 or 31 days, a February of 28; F, N, C; Caelius in Letters to Friends 8.6.5 (Curio, 50); 445 days in 46; Pliny, Natural History 18.211 (Sosigenes); Macrobius, Saturnalia 1.14.13–15 and 1.13.21 (Tuditanus and Cassius Hemina); Michels 1967; Rüpke 2011; Livy 9.46.5 (Cn. Flavius, 304)
- Fasti Antiates Maiores: painted 84–55 BC, found at Antium in 1915, thirteen columns, Palazzo Massimo
- Festival table, dates and sources; Ovid, Fasti 4.731–734 (suffimen: calf ash, horse's blood, bean-straw) and 4.725–728 (Ovid carrying the ash); 2.685–852 (Regifugium); Gelasius around 495; Polybius 12.4b (Timaeus on the October Horse); Frazer's Fasti (1929); Beard, PCPS 33 (1987)
- Pointers checked against their targets: 1.5 (Numa's priesthoods; the rex sacrorum, Livy 2.2), 1.6 (the Sibylline Books bought by a Tarquin), 0.1 (Annales Maximi; Verrius Flaccus at Praeneste), Greek 8.1 (archon basileus oversees the cults), Greek 8.3 (contests), 4.4 (fetials as legal certifiers), 4.2 (Drepana: 93 ships taken), 1.2 (disciplina Etrusca), 0.3 (three months' drift), 6.3 (Fasti of AD 2–8, rededicated in exile), 6.2 (Augustus in the colleges; pontifex maximus from 12 BC), 2.1, 2.5
- Incoming pointers that describe this report correctly: 4.2 (chickens), 4.3 (the Vestals of 216), 4.4 (the fetial rite), 5.2 (colleges of fifteen), 5.4 (Julian year; Lupercalia), 6.2, 6.3, 0.3, 1.5, 7.2 (Cornelia's burial)
