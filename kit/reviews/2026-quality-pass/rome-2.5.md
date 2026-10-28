# Rome 2.5: New gods: Cybele, Bacchus, Isis, Mithras and the Christians

Verdict: fix
Body words: 2739 (target 2500)

## Coverage
- evocatio and Juno of Veii, 396 (Livy 5.21–22): covered
- Aesculapius from Epidaurus to the Tiber Island, 291: covered
- the Magna Mater of 204: Sibylline advice, Claudia Quinta and the ship, Megalesia, the Galli, the ban on citizens: covered
- the Bacchanalia in Livy 39.8–19 and the Tiriolo bronze: covered
- expulsions of astrologers, Jews and Isiacs: covered
- Isis and Serapis, late Republic and empire; Apuleius, Metamorphoses 11: covered
- Mithras, the tauroctony, the mithraea under Santa Prisca and San Clemente: covered (San Clemente thin)
- the "oriental religions" and the debate since Cumont: covered
- Judaism at Rome: covered
- first encounters with the Christians (Annals 15.44; Pliny, Letters 10.96–97 and Trajan's reply), stopping before the persecutions: covered
- pointer to Greek module 8.2 for the mysteries: covered

## Findings
1. [error] [accuracy] Section "The Magna Mater, 204 BC".
   Current: "and on 4 April 204 she was lodged on the Palatine, the day becoming the Megalesia (29.14.5–14)"
   Problem: The cited passage dates the arrival "pridie idus Apriles", 12 April. Livy has the goddess carried into the temple of Victory on the Palatine and the day made a holiday. The Megalesia of the calendars opened on 4 April, so the report merges two dates and credits both to Livy.
   Fix: "and on 12 April 204 she was lodged in the temple of Victory on the Palatine, the day made a holiday (29.14.5–14); the Megalesia of the calendars opened on 4 April"
   Basis: Livy 29.14.14. The translation quoted at https://www.keytoumbria.com/ROMAN_REPUBLIC/Temple_of_Magna_Mater.html reads "conveyed her into the temple of Victory, in the Palatine on [12th] April, which was made a holiday". The calendar dates (4 April for the ludi, 10 April for the temple's dies natalis) are at https://en.wikipedia.org/wiki/Aprilis. thelatinlibrary.com (Livy 29) was blocked, so I could not check the Latin directly.
2. [error] [attribution] Section "Mithras: the bull, the cave and the grades".
   Current: "Clauss (<em>Cultus Mithrae</em>, 1990)"
   Problem: No such title exists. Clauss's prosopography is Cultores Mithrae: die Anhängerschaft des Mithras-Kultes (Stuttgart, 1992). His 1990 book, the general study, is Mithras: Kult und Mysterien (English, The Roman Cult of Mithras, 2000).
   Fix: "Clauss (<em>Mithras: Kult und Mysterien</em>, 1990)"
   Basis: Journal of Roman Archaeology review headed "Manfred Clauss, Cultores Mithrae ... (HABES 10, Franz Steiner Verlag, Stuttgart 1992)" (cambridge.org); Routledge page for The Roman Cult of Mithras (routledge.com/products/9780415929783).
3. [should-fix] [lane] Section "Evocatio: calling a god out of an enemy city".
   Current: "Livy calls the companion tale of soldiers in the tunnel overhearing the Veientine haruspex fitter for the stage than for belief (5.21.8–9)."
   Problem: Module 3.3 retells the whole evocatio, not just the siege. It has Camillus' prayer to Juno Regina (5.21.1–3), the stage-tale verdict (5.21.8–9), the youths in white and the nod (5.22.3–7), the Aventine temple of 392, and a self-test question on the rite. All of that is then repeated here. This report's prompt owns the rite. The tunnel tale belongs to the siege, so it can go from here.
   Fix: delete this sentence. Outside this group, the maintainer should also cut 3.3's account of the rite to the sentence that already points here ("Evocatio as a mechanism is module 2.5") and replace 3.3's self-test question 4 ("How did Camillus bring Juno Regina to Rome, as Livy tells it?").
   Basis: rome/r-3.3.html, the paragraph on Camillus in 396 and self-test question 4.
4. [minor] [pointer] Section "The "oriental religions" since Cumont".
   Current: "(Burkert, <em>Ancient Mystery Cults</em>, 1987)"
   Problem: Greek module 8.2 opens its section "Isis, Cybele, Mithras: imports through a Greek filter" with the same Cumont-against-Burkert point. A back-pointer would avoid the look of a second treatment.
   Fix: "(Burkert, <em>Ancient Mystery Cults</em>, 1987; Greek module 8.2)"
   Basis: greece/r-8.2.html.

## The unit 7 pointers to this report
Each was checked against 2.5, and none is a mismatch.
- 7.1, "he punished the Christians, which module 2.5 examines with Annals 15.44": true. 2.5 gives Annals 15.44.2–5, Suetonius, Nero 16.2, and the Shaw and Jones dispute. 2.5's own pointer to 7.1 for the fire of 64 is also true (7.1 dates it 19 July 64, Annals 15.38–40).
- 7.2, Isis, "a cult whose Flavian fortunes module 2.5 follows": true but brief. 2.5 gives the triumvirs' temple of 43, Vespasian and Titus at the Iseum before the triumph of 71 (Josephus, Jewish War 7.123), Domitian's rebuilding of the Iseum, and the Pompeian Iseum after 62. 2.5 does not mention Domitian's escape in Isiac dress, which 7.2 tells, so nothing is duplicated.
- 7.2, "The Temple tax diverted to Jupiter Capitolinus is module 2.5's": true in one sentence (Jewish War 7.218, two drachmas a year after 70). This is the "Jews at Rome" hand-off. It is thin but not false.
- 7.3, Pliny and Trajan on the Christians (Letters 10.96–97) and Christians executed under the rescript: true. 2.5 has both letters in detail.
- 7.5, "Module 2.5 reads the letters on the Christians (10.96–97)": true. The dates also agree: 7.5 says Pliny was sent about 110, and 2.5 has him governing about 110–112.

## Confirmed
Checked against the texts as I know them, unless a URL is given.
- Livy 5.21.3 (the prayer), 5.22.3–7 (youths in white, "Visne Romam ire, Iuno?", the nod, light to carry, only a priest of one gens touches the image), 5.31.3 (392), 5.21.8–9 ("ad ostentationem scaenae")
- Macrobius, Saturnalia 3.9.7–8 (the Carthage formula, si deus si dea); the Isaura Vetus inscription of P. Servilius Vatia (75 BC); Pliny, Natural History 28.18 (Rome's secret tutelary name)
- Beard, North and Price 1998; Blomart 1997 (in Cancik and Rüpke, eds., Römische Reichsreligion und Provinzialreligion); Gustafsson, Evocatio Deorum (Uppsala, 2000)
- Livy 4.25.3; 22.9–10 and 23.31.9; 10.47.6–7 (293: Aesculapius found in the Books); Periocha 11; Valerius Maximus 1.8.2; Ovid, Metamorphoses 15.622–744; Suetonius, Claudius 25.2; Wissowa 1912; Orlin 2010; Greek 8.2 on incubation and the Tiber Island
- Livy 29.10.4–5 (the oracle of 205), 29.11.7 (Attalus gives the stone), 29.14.8 and 29.14.12 (Nasica; Claudia Quinta's single clause), 36.36.3–4 (temple, 191); Ovid, Fasti 4 (the ship); Herodian 1.11 (Claudia a Vestal); Cicero, On Old Age 45; Dionysius 2.19.4–5; Valerius Maximus 7.7.6 (Genucius, 77); Varro, On the Latin Language 6.15 (Pergamon); Gruen 1990; Beard 1994
- Livy 39.8 (Graecus ignobilis, sacrificulus et vates), 39.13.8–14 (Paculla Annia: three days a year by day, made five nights a month; men admitted; none over twenty; "alterum iam prope populum"), 39.16.6, 39.17.6 (over 7,000), 39.18.5 (more killed than imprisoned), 39.18.8–9; CIL I² 581 (Tiriolo, found 1640: no male priest, no magister, no common fund, no oaths, five at most, two men and three women, a Senate of at least 100); North, PCPS 25 (1979); Walsh, G&R 43 (1996)
- Expulsions table, row by row: Valerius Maximus 1.3.3 (139); Tertullian, To the Nations 1.10; Dio 40.47 and 42.26; Dio 49.43.5 (Agrippa, 33); Dio 53.2.4 and 54.6.6 (28, 21); Annals 2.32 (16), 2.85 (19, 4,000 freedmen), Josephus, Jewish Antiquities 18.65–84; Suetonius, Claudius 25.4; Dio 60.6.6; Annals 12.52; Histories 2.62, 1.22; Acts 18.2; Orosius 7.6.15; Lüdemann 1980; Riesner 1994
- Serapeum at Puteoli by 105 (lex parieti faciendo, CIL I² 698); Dio 47.15.4 (43 BC); Josephus, Jewish War 7.123; CIL X 846 (N. Popidius Celsinus, aged six)
- Apuleius, Metamorphoses 11.5, 11.13, 11.23 ("nocte media vidi solem"), 11.26–30, 11.27 (Madauros); Griffiths 1975; Winkler 1985
- Statius, Thebaid 1.719–720; Porphyry, On the Cave of the Nymphs 6; Jerome, Letters 107.2; Vermaseren and van Essen at Santa Prisca; Justin, First Apology 66; Tertullian, Prescription against Heretics 40; Renan, Marc-Aurèle (1882)
- Cumont 1906; Burkert 1987; CIL VI 1779 (Praetextatus, died 384: augur, pontifex, pater patrum); J. Z. Smith, Drudgery Divine (1990); Bonnet, Pirenne-Delforge and Praet (eds.), 2009, from the 2006 centenary conference; Alvar, Romanising Oriental Gods (2008)
- Pro Flacco 66–69 (59 BC); Josephus, Jewish Antiquities 14.213–216; Philo, Embassy to Gaius 155–158; Horace, Satires 1.9.69–70; Tacitus, Histories 5.4–5; Josephus, Jewish War 7.218; Tertullian, Apology 21.1 ("religio licita"); Rajak, JRS 74 (1984)
- Annals 15.44.2–5 (Christus executed by Pontius Pilatus; "odio humani generis"; dogs, crosses, torches); Suetonius, Nero 16.2; Shaw, JRS 105 (2015); C. P. Jones, NTS 63 (2017)
- Pliny, Letters 10.96 (three times asked; obstinacy punished; incense and wine to the image; hymn before dawn, "quasi deo"; the oath; two ancillae called ministrae; "superstitionem pravam et immodicam") and 10.97 ("conquirendi non sunt"; "nec nostri saeculi est"); Tertullian, Apology 2.6–9; de Ste. Croix, P&P 26 (1963); Sherwin-White, P&P 27 (1964) and the 1966 commentary
- Pointers checked against their targets: 2.1, 2.3, 3.3, 7.1, Greek 8.2 (incubation; the Ptolemaic Isis with Sarapis; the Greek mediation of Mithras), 8.1 (Decius' order of universal sacrifice, per its syllabus prompt)
- Incoming pointers that describe this report correctly: 2.1 (superstitio for foreign cults), 2.2 (Juno Regina; the Bacchic cult), 2.3 (the Magna Mater), 3.3 (evocatio), 4.3 (the Idaean Mother)
- Source-criticism intervals are given for Veii (some 370 years), Apollo (four centuries) and Aesculapius (nearly three centuries)
