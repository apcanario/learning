# Rome 9.4: Bread, baths and games

Verdict: fix
Body words: 2833 (target 2500; band 2250 to 2875). With every fix below applied the count is 2868 (checked with `check.py --target 2500` on a scratch copy), so the fixes fit the band with almost nothing to spare. Any further addition needs a matching cut.

## Coverage
- Population estimates: covered (Res Gestae 15, Brunt and Hopkins against Storey, regionary catalogues, Scheidel).
- Housing (domus and insula, fire and collapse, Juvenal 3): covered.
- Water, aqueducts and Frontinus' On Aqueducts: covered; Appia and Anio Vetus handed back to modules 3.4 and 3.5 as the lane note asks.
- Grain supply, Ostia and the dole: covered; the grain laws as politics handed to deep dive module 11.3.
- Patronage and the morning salutation: covered (new material, as the lane note asks).
- Baths as a social institution: covered; Caracalla handed back to module 7.4.
- Food and the dinner party: covered, brief but adequate.
- Gladiators, origins: handed back to module 1.2 (counts as covered); types, schools, munus, epitaphs (Flamma), Colosseum machinery (Beste): covered.
- Chariot racing and the colours: covered.
- Wild-beast hunts: covered.
- Executions as spectacle: covered; the legal penalty handed to module 9.1.
- Theatre and pantomime: covered.
- Juvenal's "bread and circuses" (10.81) and what it gets wrong: covered.
- Pompeii and Herculaneum as the town-level check: covered.
- Lane note: the Colosseum's dedication and Alföldy point back to 7.2 without retelling the hundred days or Dio's nine thousand animals; gladiator origins (1.2), Trajan's 123 days (7.3, not mentioned), Caesar's 320 pairs (5.3, pointer), the fire of 64 (7.1), the Baths of Caracalla (7.4) and the Appia and Anio Vetus (3.4, 3.5) are all pointers, not retellings. All hand-offs kept.

## Findings
1. [minor] [attribution] Section "Bread: the annona and the dole".
   Current: "Each drew five modii of wheat a month (Sallust, <em>Histories</em> 3.48.19)"
   Problem: The sentence is about the Augustan dole, but Macer's speech in Sallust gives the ration under the law of 73 BC; the imperial ration is the same figure by inference, not by Sallust's statement.
   Fix: "Each drew five modii of wheat a month (Sallust, <em>Histories</em> 3.48.19, for 73 BC)"
   Basis: Sallust, Histories 3.48.19 Maurenbrecher (speech of Licinius Macer, set in 73 BC: "quinis modiis libertatem omnium aestumavere").

2. [minor] [lane] Section "The Roman day: salutation, baths, dinner".
   Current: "Richard Saller (<em>Personal Patronage under the Early Empire</em>, 1982) showed"
   Problem: Module 7.5 already cites the same book for the same thesis ("argued that patronage, not seniority, moved careers"); crosscheck.py flags the shared passage. One sentence is within the lane rule, but a pointer saves the reader the déjà vu.
   Fix: "Richard Saller (<em>Personal Patronage under the Early Empire</em>, 1982; module 7.5) showed"
   Basis: rome/r-7.5.html, Saller sentence in the patronage section.

3. [minor] [accuracy] Section "The Roman day: salutation, baths, dinner".
   Current: "and built the first imperial <em>thermae</em>"
   Problem: As written, the sentence puts the Baths of Agrippa in his aedileship of 33 BC; they were begun in 25 BC and fed by the Virgo of 19 BC.
   Fix: "and later built the first imperial <em>thermae</em>"
   Basis: Dio 53.27.1 (the Laconian sudatorium, 25 BC); Frontinus, On Aqueducts 10 (Virgo, 19 BC).

4. [minor] [style] Section "The Roman day: salutation, baths, dinner".
   Current: "so mixed bathing went on."
   Problem: Read as a consequence, it says the ban made mixed bathing continue; the intended inference is that the ban shows mixed bathing had been happening.
   Fix: "so mixed bathing had gone on."
   Basis: Historia Augusta, Hadrian 18.10 ("lavacra pro sexibus separavit").

5. [minor] [accuracy] Section "The Roman day: salutation, baths, dinner".
   Current: "up to nine guests reclined"
   Problem: Three couches of three held nine diners including the host, not nine guests.
   Fix: "up to nine diners reclined"
   Basis: standard triclinium arrangement (Horace, Satires 2.8 seats nine with the host Nasidienus).

6. [minor] [accuracy] Section "The arena: gladiators, beasts and the condemned".
   Current: "collected executions staged as myth, such as"
   Problem: Laureolus, the example given, is the bandit of a mime, not a figure of myth; Self-test 8's answer ("mythological or historical scenes") fits neither.
   Fix: "collected executions staged as myth or drama, such as"; and in Self-test 8, replace "Executions of condemned criminals staged as mythological or historical scenes" with "Executions of condemned criminals staged as mythological or dramatic scenes"
   Basis: Martial, On the Spectacles 9 (7) (Laureolus, with Prometheus as the mythological comparison); Coleman, JRS 80 (1990) 44–73, discusses the Laureolus mime.

7. [should-fix] [accuracy] Section "The arena: gladiators, beasts and the condemned" (dispute box on flooding).
   Current: "Suetonius places Titus' sea fight in the old naumachia (<em>Titus</em> 7.3)."
   Problem: The box sets Suetonius against Dio, but Dio reports a second sea fight in Augustus' old basin in the very next sentence (66.25.3); the difference is that Suetonius mentions only the naumachia, not that the two contradict each other on the venue.
   Fix: "Suetonius mentions only a sea fight in the old naumachia (<em>Titus</em> 7.3), where Dio puts a second."; and in Self-test 9, replace "Suetonius puts the sea fight in the old naumachia (<em>Titus</em> 7.3)" with "Suetonius mentions only a sea fight in the old naumachia (<em>Titus</em> 7.3)"
   Basis: Dio 66.25.3 (sea fight in the grove of Gaius and Lucius, Augustus' basin); confirmed via https://en.wikipedia.org/wiki/Naumachia_of_Augustus citing Dio 66.25.3.

8. [error] [accuracy] Section "Circus and stage" (dispute box on seating).
   Current: "Pliny, half a century later, gives"
   Problem: Dionysius published the Roman Antiquities in 7 BC and Pliny dedicated the Natural History in AD 77: some eighty years apart, not fifty.
   Fix: "Pliny, some eighty years later, gives"
   Basis: Dionysius, Roman Antiquities 1.7.2 (twenty-two years in Rome from 30 BC); Pliny, Natural History, preface (dedication to Titus, consul for the sixth time, AD 77).

9. [should-fix] [attribution] Section "Circus and stage".
   Current: ", brought to Rome, Jerome's <em>Chronicle</em> says, by Pylades in 22 BC."
   Problem: Jerome does not say Pylades brought pantomime to Rome; he says that, whereas earlier performers sang and danced themselves, Pylades was the first at Rome to have a chorus and pipe accompany him. The report cites him for a modern inference.
   Fix: "; Jerome's <em>Chronicle</em> makes Pylades, in 22 BC, the first at Rome to have a chorus and piper accompany him."
   Basis: Jerome, Chronicle under 22 BC: "Pylades Cilex pantomimus, cum veteres ipsi canerent atque saltarent, primus Romae chorum et fistulam sibi praecinere fecit" (text and date as quoted in Rheinisches Museum, https://journals.ub.uni-koeln.de/index.php/rhm/article/download/10783/11001/22108).

10. [error] [accuracy] Section ""Bread and circuses"".
   Current: "The shows were occasional gifts, and gladiators were never a regular part of the republican festival calendar."
   Problem: Juvenal's word is <em>circenses</em>, and the races were not occasional gifts but fixed days of the state festivals (the Ludi Romani, Plebeii, Apollinares and others ended in circus days; the Calendar of 354 lists 64 days of races). Only the gladiatorial <em>munera</em> were occasional gifts. Self-test 10 repeats the claim.
   Fix: "The races came on fixed festival days, and gladiatorial shows were occasional gifts, never part of the republican festival calendar."; and in Self-test 10, replace "shows were occasional;" with "races came on festival days and gladiatorial shows were occasional;"
   Basis: Livy's notices of the Ludi Romani and Plebeii as annual festivals; Calendar of 354 (Fasti of Filocalus), 177 festival days of which 64 circus; not fetched: standard reference knowledge.

11. [minor] [accuracy] Section ""Bread and circuses"" (dispute box).
   Current: "are both the view from the senatorial benches."
   Problem: Fronto was a senator and consul, but Juvenal was not; his persona is a poor client and his own rank is at most equestrian.
   Fix: "are both the view from the front rows."
   Basis: Fronto, suffect consul 142; Juvenal's status uncertain (the Aquinum inscription CIL X 5382, if his, makes him at most an equestrian officer).

12. [error] [accuracy] Section "Pompeii and Herculaneum: the town-level check".
   Current: "yielded a diet of fish, sea urchin, figs and eggs that no text records."
   Problem: Texts do record these foods; the report itself cites Pliny, Letters 1.15, whose menu includes eggs and whose rival dinner had sea urchins (<em>echinos</em>). What the sewer adds is the diet of ordinary tenants and shopkeepers, whose garbage chutes fed it.
   Fix: "showed that the shopkeepers and tenants above it ate fish, sea urchin, figs and eggs, a diet no text records for such people."
   Basis: Pliny, Letters 1.15 ("ova bina", "ostrea, vulvas, echinos, Gaditanas"); Herculaneum Conservation Project reports via https://www.thehistoryblog.com/?p=11565 (86 m tunnel, waste from apartments and shops above; fish, sea urchins, figs, walnuts, eggs).

## Confirmed
- Res Gestae 15.2 (5 BC, 60 denarii to 320,000 urban plebs) and 15.4 (2 BC, grain recipients "a little more than 200,000"); 22.1 (about 10,000 fighters, eight munera); 22.3 (26 hunts, about 3,500 beasts).
- Storey, "The population of ancient Rome", Antiquity 1997: about 450,000 from Pompeii and Ostia densities (Cambridge abstract).
- Regionary catalogues: about 46,600 insulae.
- Strabo 5.3.7 (Augustus' seventy-foot limit on public streets); vigiles AD 6, seven cohorts of freedmen (Suetonius, Augustus 30.1; Dio 55.26.4–5).
- Cicero, Letters to Atticus 14.9.1 (two shops collapsed, the rest cracking, mice moved out).
- Juvenal 3.190–196, 3.197–202, 3.223–225 (Sora), 3.232–238, 3.268–277, 3.58–125, 3.36–37 (verso pollice), 1.95–96 (sportula), Satire 5 (Trebius), 10.77–81 (panem et circenses).
- Frontinus, On Aqueducts 4 (441 years), 16 (idle pyramids), 107 (grant not passing to heir or buyer), 116 (about 240 public and 460 imperial staff); Frontinus as curator under Nerva in 97, former governor of Britain.
- Pliny, Natural History 36.121 (Agrippa as aedile: 700 lacus, 500 salientes, 130 castella, 170 free baths).
- Aqueduct dates: Marcia 144, Tepula 125, Claudia and Anio Novus finished 52.
- Josephus, Jewish War 2.383 and 2.386 (Africa eight months, Egypt four), as Agrippa II's speech; Tacitus, Annals 3.54 (life of the people tossed on sea and storm).
- Claudius' harbour begun 42 (Dio 60.11; Suetonius, Claudius 20.3); crusts in the Forum (Suetonius, Claudius 18.2) and fifteen days' grain (Tacitus, Annals 12.43); Gaius, Institutes 1.32c (10,000 modii, six years).
- Suetonius, Julius 41.3 (list cut from 320,000 to 150,000, vacancies by lot), and module 5.4 says the same.
- Persius 5.73–75 (tesserula, scabiosum far); Suetonius, Augustus 42.3 (thought of abolishing the dole, desisted); Tacitus, Annals 1.7 (Turranius prefect of the grain supply in 14).
- Martial 4.8 (hours of the day), 1.59 (sportula of a hundred quadrantes), 2.14 (Selius); Commentariolum petitionis 34–38 (salutatores, deductores, adsectatores).
- Horace, Satires 1.3.6–7 (ab ovo usque ad mala) and 1.3.137 (quadrans bath); Seneca, Letters 56.1–2; Marcus Aurelius, Meditations 8.24; Historia Augusta, Hadrian 18.10; Pliny, Letters 1.15, 2.6, 9.6; Suetonius, Nero 16.2.
- Tertullian, On the Spectacles 10 (Pompey's theatre as temple of Venus) and 12 (munus as service to the dead); Livy 23.30.15 (22 pairs, 216 BC); Livy 39.22.2 (lions and panthers, 186 BC).
- Petronius 117.5 and Seneca, Letters 37.1 (the gladiator's oath); CIL X 7297 (Flamma: 30 years, 34 fights, 21 wins, 9 stans, 4 missus).
- Corbeill, Nature Embodied (2004): upright thumb hostile, thumb pressed on the closed fist for mercy, from Pliny, Natural History 28.25 (Encyclopaedia Romana summary); Gérôme, Pollice Verso, 1872.
- Seneca, Letters 7.3–5; Strabo 6.2.6 (Selurus); Coleman, "Fatal Charades", JRS 1990; Cicero, Letters to Friends 7.1.3 (pity for the elephants).
- Beste: 60 capstans and drains for a flooded arena (Mueller, Smithsonian 2011, https://www.smithsonianmag.com/history/secrets-of-the-colosseum-75827047/); Dio 66.25.2–3 (Titus floods the amphitheatre).
- Dio 49.43.2 (Agrippa's dolphins and eggs); CIL VI 10048 (Diocles: 4,257 starts, 1,462 wins, 35,863,120 sesterces, 24 years); Dionysius 3.68.3 (150,000) and Pliny, Natural History 36.102 (250,000); Cameron, Circus Factions (1976).
- Suetonius, Augustus 44 (seating by rank); Tacitus, Annals 1.77 (theatre riot of 15, soldiers and a centurion killed) and 4.14 (actors expelled in 23); Dio 54.17 (Pylades' retort to Augustus).
- Fronto, Preamble to History (annona and spectacula); Cicero, Pro Sestio 106 (contio, comitia, games and gladiatorial shows); Veyne, Le pain et le cirque (1976); Hopkins, Death and Renewal (1983).
- CIL X 852 (Pompeii amphitheatre, Quinctius Valgus and Porcius, at their own cost, about 70 BC); Tacitus, Annals 14.17 (riot of 59, ten-year ban); Wallace-Hadrill, Houses and Society in Pompeii and Herculaneum (1994); Allison, Pompeian Households (2004).
- Pointers checked against their targets and true: 7.1 (fire of 64 and rebuilding; Sejanus' fall with Juvenal 10), 3.4 (Aqua Appia), 3.5 (Anio Vetus from Pyrrhus' spoils), 5.4 (grain list cut), 6.1 (cura annonae accepted in 22), 7.4 (Baths of Caracalla), 9.3 (Trimalchio), 1.2 (gladiator origins and the first show of 264), 5.3 (320 pairs as aedile in 65), 7.2 (dedication in 80, Alföldy, the eruption of 79), 1.5 (Tarquinius Priscus lays out the Circus Maximus), 8.6 (Nika riot), 7.3 (Cleander killed in 190 after a grain-shortage crowd), 7.5 (euergetism, local magnates' gifts); 9.1 and 11.3 (unwritten) checked against their prompts. No dispute box duplicated in 9.2, 9.3 or any pointed target.
