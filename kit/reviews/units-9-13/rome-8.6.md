# Rome 8.6: The Rome that did not fall

Verdict: fix
Body words: 2832 (target 2500; band 2250 to 2875. With every fix below applied to a scratch copy, check.py counts 2859)

## Coverage
- Why the East survived: covered (money, geography and walls, Persia, control of generals; Jones 1964)
- Justinian's reconquests: covered (Africa 533–534, Italy 535–552, Spain, Lombards 568)
- Corpus of Civil Law: covered in outline, handed to module 9.1 as the lane note asks
- Hagia Sophia: covered as a building of the reign; art reading sent to module 10.3 (see finding 7)
- Persian and Arab wars, loss of the eastern provinces: covered
- Romaioi and "Byzantine" as an early modern coinage: covered (Wolf 1557 with pointer to module 0.3)
- Macedonian dynasty: covered (Basil I to Basil II, Basilika, Constantine VII)
- Charlemagne in 800 and a rival Roman empire: covered (812 recognition, 962, 1157, 1254, 1806)
- Manzikert, the Crusades and 1204: covered
- Palaiologan revival: covered; fall to Mehmed II in 1453: handed to module 0.3 as the lane note asks (the report never gives the date; see finding 6)
- Last fragments (Morea 1460, Trebizond 1461): covered, as 0.3 hands them on
- Afterlives (Third Rome, Holy Roman Empire to 1806, Kayser-i Rum): covered
- Pointer to Greek modules 7.4 and 9.3 for Byzantine preservation of texts: present

## Findings
1. [error] [accuracy] Section "Dynasties and the Macedonian height".
   Current: "murdered his patron in 867 and founded the longest dynasty in the empire's history."
   Problem: The Macedonian dynasty ruled 867–1056 (189 years); the Palaiologan dynasty, in the report's own table, ruled 1259–1453 (194 years) and is the longest.
   Fix: "murdered his patron in 867 and founded a dynasty that ruled for almost two centuries."
   Basis: the report's table; Wikipedia, "Palaiologos" (https://en.wikipedia.org/wiki/Palaiologos: "the last and longest-ruling dynasty"); "Macedonian dynasty" (867 to 1056).

2. [error] [accuracy] Section "Justinian: reconquest, plague, law and the Great Church".
   Current: "A commission led by the quaestor Tribonian issued a Code"
   Problem: The ten-man commission of 528 that produced the Code of 529 was headed by John the Cappadocian; Tribonian sat on it and led the later commissions (the Digest from December 530, the Institutes, the revised Code of 534).
   Fix: "Commissions on which the jurist Tribonian sat, leading them from 530, issued a Code"
   Basis: Wikipedia, "Code of Justinian" (https://en.wikipedia.org/wiki/Code_of_Justinian); Bury, History of the Later Roman Empire, ch. 23 on LacusCurtius (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/BURLAT/23*.html): ten jurists for the Code, the Digest commission "under the presidency of Tribonian".

3. [minor] [register] Section "The afterlives of the Roman title".
   Current: "repeats Philotheus' formula, which looks like official doctrine."
   Problem: The side opposed to Poe is the reader's inference, not a named scholar. The box names a source on that side, but it reads as Poe against nobody.
   Fix: "repeats Philotheus' formula, and Hildegard Schaeder (<em>Moskau das dritte Rom</em>, 1929) made it the core of Muscovite political ideology."
   Basis: title confirmed from the de Gruyter page for the 1957 second edition (https://www.degruyterbrill.com/isbn/9783112320389, subtitle "Studien zur Geschichte der politischen Theorien in der slawischen Welt"). The first edition (Hamburg 1929) and her reading as state ideology are from knowledge: the maintainer should confirm before applying.

4. [minor] [register] Section "Persians and Arabs: the seventh-century amputation".
   Current: "a deliberate reform of Heraclius; John Haldon"
   Problem: The dispute box is a single sentence, against the brief's two to four.
   Fix: "a deliberate reform of Heraclius. John Haldon"
   Basis: BRIEF.md, register.

5. [minor] [style] Sections "Romaioi: Romans who spoke Greek" and "The Palaeologan revival and the last fragments".
   Current: "<h2>Romaioi: Romans who spoke Greek</h2>" and "<h2>The Palaeologan revival and the last fragments</h2>"
   Problem: The headings use different forms from the body: the body has <em>Rhomaioi</em> (as module 0.3 does), and "Palaiologan", "Palaiologos" and "Palaiologina".
   Fix: "<h2>Rhomaioi: Romans who spoke Greek</h2>" and "<h2>The Palaiologan revival and the last fragments</h2>"
   Basis: internal consistency; rome/r-0.3.html line 84.

6. [minor] [lane] Section "The Palaeologan revival and the last fragments".
   Current: "The siege and fall of 1453 are told in module 0.3."
   Problem: The prompt names "the fall to Mehmed II in 1453", and 0.3 gives it a single sentence. 8.6 never states the date of the event its self-test and carry-forward rest on. A clause gives that anchor without retelling 0.3.
   Fix: "The siege and fall of 1453, when Mehmed II took the city on 29 May, are told in module 0.3."
   Basis: rome/r-0.3.html line 84; prompt 8.6.

7. [minor] [pointer] Section "Justinian: reconquest, plague, law and the Great Church".
   Current: "Reading the building as art is module 10.3;"
   Problem: Module 10.3 is unwritten, and its prompt does not name Hagia Sophia. It covers domes through the Pantheon and "late antique style (the Tetrarchs, the Arch of Constantine)". The pointer holds only if 10.3's writer is told.
   Fix: no change here if Hagia Sophia is added to module 10.3's lane note (as this module's lane note assumes). Otherwise: "Late antique style, the frame for reading it as art, is module 10.3;"
   Basis: roman-syllabus.html, prompt 10.3.

## Confirmed
- Hand-off from 8.5: rome/r-8.5.html line 49 sends the regalia to Constantinople and says "module 8.6 begins there"; 8.6 opens there and does not retell 476.
- Module 0.3 (rome/r-0.3.html line 84) has Mehmed II, Constantine XI, the Rhomaioi, Wolf 1557, and sends "the Morea to 1460, Trebizond to 1461" to 8.6. 8.6 points back for 1453 and Wolf and covers the fragments (Mistra 1460, Trebizond August 1461, David executed 1463, Theodoro 1475, Andreas 1494 and 1502).
- Pointer "Constantine's New Rome (module 8.3)": rome/r-8.3.html has "A new Rome on the Bosporus". The one sentence on canon 3 of 381 overlaps 8.3's Dagron box, which is acceptable at that length.
- Pointer "porphyry Tetrarchs of module 8.2": rome/r-8.2.html line 15 has them at St Mark's, looted after 1204.
- Pointer to Greek 7.4 for 529: greece/r-7.4.html has the 529 ban (Malalas 18.47, Cod. Just. 1.11.10) and the Cameron/Watts dispute.
- Pointer to Greek 7.4 and 9.3 for copying in minuscule: 7.4 has the ninth-century change to minuscule, Photius, Arethas, books to Italy. 9.3 ("Byzantium and the Arabic transmission") has Photius' ninth-century revival, the Suda and the Palaiologan editors, though it does not use the word minuscule. True as written.
- Pointer to module 9.1 (unwritten): prompt includes Justinian's Corpus (Code, Digest, Institutes, Novels). The outline here stays within one paragraph.
- Pointer to module 10.4 (unwritten): prompt names Charlemagne and the Holy Roman Empire.
- crosscheck.py: no shared passages, no duplicated dispute boxes.
- Procopius, Wars 1.24.54, more than 30,000 dead in the Nika riot: Encyclopaedia Romana (https://penelope.uchicago.edu/encyclopaedia%5Fromana/circusmaximus/nika.html). Theodora's speech at 1.24.33–37 matches the standard Loeb sectioning but was not checked to the section.
- Procopius, Secret History 19.7, 3,200 centenaria (writer checked on LacusCurtius); Wars 2.23 for 5,000 then 10,000 a day.
- Jones, The Later Roman Empire (1964): the East's survival shows internal weaknesses cannot have been a major factor (ch. 25). Known formulation, consistent with the summary.
- Mordechai, Eisenberg et al., "The Justinianic Plague: an inconsequential pandemic?", PNAS 2019; Harper, The Fate of Rome (2017); Haldon, Byzantium in the Seventh Century (1990); Ostrogorsky, History of the Byzantine State (English 1956) and its formula of Roman state, Greek culture, Christian faith; Kaldellis, Romanland (2019); Vryonis (1971); Stephenson (2003); Poe (2001) title.
- Cheynet, "Mantzikert: un désastre militaire?", Byzantion 50 (1980): title confirmed by search results.
- Dates checked from standard knowledge: Theodosian Walls 413 and 447; Gainas 400; Aspar 471; Theoderic sent 488; Nika January 532; Hagia Sophia 27 December 537, dome 558, second dedication 562; plague at Pelusium 541 and Constantinople 542; Busta Gallorum 552; Lombards 568; Phocas 602; Antioch 613; Jerusalem 614; siege of 626; Nineveh December 627; Yarmuk 636; Alexandria 641–642; Carthage 698; siege of 717–718; Kallinikos in Theophanes; 797 Irene; Annals of Lorsch; Einhard, Life of Charles 28; Aachen 812; 962, 1157, 1254, 6 August 1806; Crete 961; Antioch 969; Bulgaria annexed 1018; Anna and Vladimir c. 988; Skylitzes' 15,000 and Kekaumenos' 14,000; Manzikert 26 August 1071; Attaleiates and Psellos; Clermont 1095; Myriokephalon 1176; 1182 massacre; Zara 1202; 12 April 1204; three-eighths to Venice; Trebizond April 1204; 25 July 1261; Lyons 1274; Gallipoli 1354; Ankara 1402; Florence 1439; Kayser-i Rum; George of Trebizond's letter; Zoe/Sophia 1472; Ivan IV 1547; patriarchate 1589; Philotheus to Vasily III.
- Self-test answers agree with the body; ten questions, three carry-forward items; no em dashes; British spelling.
