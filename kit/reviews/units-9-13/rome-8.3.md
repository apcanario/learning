# Rome 8.3: Constantine

Verdict: fix
Body words: 3399 (target 3000)

All proposed fixes applied together give 3429 words (checked on a scratch copy with `check.py`), which is inside the band (2700 to 3450).

## Coverage
- proclamation at York: covered
- wars of the Tetrarchs: covered (306–312 told from Constantine's side; 316 and 324 against Licinius)
- Milvian Bridge 312: covered
- the vision, comparing Lactantius, Eusebius' Life and the panegyric's Apollo: covered (table plus discussion, Weiss dispute)
- "Edict of Milan" and what it actually was: covered
- Arch of Constantine and its reused reliefs: covered (art handed to 10.3)
- Donatist dispute: covered
- Arius and the Council of Nicaea: covered
- killing of Crispus and Fausta: covered
- foundation of Constantinople in 330: covered
- legislation: covered
- deathbed baptism: covered
- debate on sincerity and timing (Burckhardt, A. H. M. Jones, Barnes, Lenski): covered (table plus Drake in a dispute box)

## Findings
1. [error] [accuracy] Section "The evidence: panegyrists, a bishop and a hostile historian".
   Current: "The Latin panegyrics spoken before him in Gaul (<em>Panegyrici Latini</em> VII(6) of 307, VI(7) of 310, V(8) of 311, XII(9) of 313 and Nazarius' IV(10) of 321) give the official line of each year"
   Problem: Nazarius' panegyric of March 321 was delivered at Rome before the Senate, and none of the emperors it honoured was present. It was not spoken before Constantine, and not in Gaul.
   Fix: "The Latin panegyrics (<em>Panegyrici Latini</em> VII(6) of 307, VI(7) of 310, V(8) of 311 and XII(9) of 313, spoken before him in Gaul, and Nazarius' IV(10), spoken at Rome in his absence in 321) give the official line of each year"
   Basis: https://en.wikipedia.org/wiki/Panegyrici_Latini (IV(10): "delivered in Rome before the Senate"; "none of the honoured emperors was present"); Nixon and Rodgers, *In Praise of Later Roman Emperors* (1994), introduction to IV(10).

2. [should-fix] [pointer] Section "The emperor and the bishops: Donatists, Arius, Nicaea".
   Current: "the formula outlived him and became the test of orthodoxy that module 8.4 follows."
   Problem: Module 8.4 does not follow the Nicene formula becoming the test of orthodoxy. It mentions the formula once, as what Constantius II's homoian creed of 359 set aside, and has nothing on Theodosius' Nicene settlement or the council of 381. The pointer promises something the target does not contain.
   Fix: "the formula outlived him, and module 8.4 follows Constantius II's attempt to replace it."
   Basis: rome/r-8.4.html, section "The sons of Constantine, 337–361" (the only Nicene reference: "set aside the Nicene formula of module 8.3, he imposed that creed through councils in 359"); grep of r-8.4.html for Nicene, Nicaea, 381, orthodox.

3. [minor] [attribution] Section "The sign: three versions of one vision".
   Current: "The thesis is widely followed but moves Eusebius' story two years and a country away from Lactantius' battlefield."
   Problem: "Widely followed" names no follower. The writer suspected Barnes, and that is right: Barnes backed Weiss in a 1998 review and again in 2011, saying the thesis explains all the early evidence.
   Fix: "Barnes (2011) adopted the thesis as explaining all the early evidence, but it moves Eusebius' story two years and a country away from Lactantius' battlefield."
   Basis: University of Ottawa thesis on the 310 vision, https://ruor.uottawa.ca/bitstreams/c14b9a8f-5979-46f1-a76c-8cd09aabaa51/download (Barnes "wholeheartedly supported Weiss in a 1998 review"; in 2011 said it "explains all the early evidence"). The same thesis confirms the report's summary of Weiss: one vision in 310, reinterpreted as Christ's after the dream before the Milvian Bridge.

4. [minor] [accuracy] Section "From York to Rome, 306–312".
   Current: "Minervina, mother of Constantine's eldest son Crispus, was set aside."
   Problem: The sources do not say what became of Minervina. Whether she was a wife or a concubine, and whether she was divorced or had died by 307, is uncertain, so "set aside" states one reading as fact.
   Fix: "Minervina, mother of Constantine's eldest son Crispus, vanishes from the record, dead or divorced."
   Basis: own knowledge (Zosimus 2.20.2 calls her a concubine; *Pan. Lat.* VII(6).4.1 implies a lawful marriage; no source records her fate). Not searched.

5. [minor] [figure] Section "The emperor and the bishops: Donatists, Arius, Nicaea".
   Current: "about 300 by Athanasius'; the later 318"
   Problem: Eusebius' count is cited (*Life* 3.8) but Athanasius' count names no work.
   Fix: "about 300 by Athanasius' (<em>On the Decrees of Nicaea</em> 3); the later 318"
   Basis: https://fourthcentury.com/?p=21391 (Athanasius, *De decretis* 3.1, bishops "numbered about 300"; also 37.1). Schaff, *History of the Christian Church* 3, https://www.ccel.org/ccel/schaff/hcc3.iii.xii.iv.html, puts the 318 in *Ad Afros* 2.

6. [minor] [pointer] Section "Baptism, death and the debate over the conversion".
   Current: "belong to module 10.4."
   Problem: Module 10.4's prompt (reception of Rome) does not name the Silvester legend or the Donation of Constantine. Its "Rome as an idea after 476 (the papacy ...)" and its Renaissance items could take them, but nothing guarantees that the 10.4 writer will.
   Fix: no change to the report. Add to the lane note for 10.4: "8.3 hands over the legend of Constantine's baptism by Silvester and the Donation of Constantine (Valla, 1440)."
   Basis: roman-syllabus.html, prompt data-id="10.4".

7. [minor] [style] Section "Baptism, death and the debate over the conversion" (table).
   Current: "<em>Constantine: Dynasty, Religion and Power</em> (2011)"
   Problem: The title is cut off part-way through. The book is *Constantine: Dynasty, Religion and Power in the Later Roman Empire* (Wiley-Blackwell, 2011).
   Fix: "<em>Constantine: Dynasty, Religion and Power in the Later Roman Empire</em> (2011)"
   Basis: publisher listing, https://bookwire.bowker.com/book/USA/Constantine-9781444396249-Barnes-Timothy-D-33196351

8. [minor] [register] Section "Self-test", question 1.
   Current: "two years before any Christian version."
   Problem: The first Christian account (Lactantius) was written about 314–315, four or five years after 310. Only the Christian sign it describes is set two years later, so the answer does not match the dates in the body's table.
   Fix: "two years before the Christian sign of 312."
   Basis: the report's own table ("c. 314–315" for Lactantius; "after 337" for Eusebius).

## Confirmed
- *Pan. Lat.* XII(9).3.3, "vix enim quarta parte exercitus" (openstarts.units.it article, fn. 32, citing Paneg. XII (IX) 3.3). The writer was unsure of this.
- Optatus, appendix 3 is Constantine's letter to Aelafius, which fears God may be moved "not only against the human race, but also against me myself" (https://tertullian.org/fathers/optatus_11_appendices.htm). The writer was unsure of this.
- Jones and Skeat, "Notes on the Genuineness of the Constantinian Documents in Eusebius's Life of Constantine", *JEH* 5 (1954) 196–200, on the papyrus (Cambridge abstract page). The writer was unsure of this.
- Weiss's thesis is summarised fairly (Ottawa thesis above), and Weiss 1993, English 2003, is correct.
- Places and dates of VII(6) 307, VI(7) 310 (Trier), V(8) 311 (Trier) and XII(9) 313 (Trier) (Wikipedia, Panegyrici Latini).
- *Epitome de Caesaribus* 41 for Crocus (Wikipedia, Chrocus; section 41.3 from own knowledge).
- Eusebius' more than 250 at Nicaea (*Life* 3.8) (Schaff, ccel).
- Pointers. Module 0.3 lists 28 October 312 and 11 May 330 among its anchor dates (rome/r-0.3.html table). Module 1.2 cites CIL XI 5265 for games at Volsinii (rome/r-1.2.html, Fanum Voltumnae section). Greek module 7.4, "Christianity in the Greek cities", covers Justin, Clement, Origen and Basil on Greek philosophy. Module 8.4 opens with the killings of 337 and starts "Module 8.3 ends with Constantine's death". The prompts of modules 9.1 (Theodosian Code), 9.2 (late field and frontier army), 9.5 (Colosseum and Arch of Constantine stop) and 10.3 (Arch of Constantine as late antique style) match their pointers.
- Lanes. Module 8.2 tells 306–312 in outline and hands the Donatists and the settlement of 313 to 8.3. Module 8.3 points back for the 305 abdications, the persecution of 303 and Galerius' edict of 311. Carnuntum and Maximian's end get only a sentence or two each and are not told at length in both. The Great Persecution is not retold. Eusebius' history is cited as *Church History* throughout. The dispute boxes flagged by `crosscheck.py` share names only and are not duplicates. The source sentence on Lactantius overlaps 8.2's by one sentence, which is acceptable.
- Own knowledge, not searched: Lactantius 18–19, 24, 24.9, 25, 29–30, 32, 44.5 (Latin as quoted), 44.8, 46, 48. *Church History* 9.9.5–8, 9.9.10–11, 10.5.2–14, 10.5.15–24, 10.6, 10.7. *Life* 1.27–32, 1.28.1, 1.51–54, 2.45, 2.64–72, 3.10–20, 3.48, 3.54, 4.26, 4.56–64, 4.73. Zosimus 2.15.1–2 (figures), 2.29.2–4, 2.30, 2.31.2–3. Eutropius 10.6 and 10.8. Ammianus 14.11.20 (Pola). Aurelius Victor, *Caesares* 40.25. Philostorgius 1.7, 2.4, 2.9. Socrates 1.7 and 1.8. Sozomen 1.5. Julian, *Caesars* 336a–b. Libanius, *Oration* 30.6. Jerome, *Chronicle* s.a. 330 (Latin as quoted) and s.a. 337. *CIL* VI 1139. The CTh and CJ citations in "The legislation". Hispellum's condition on "contagious superstition". Burckhardt 1853, Grégoire 1938, Seeck 1891, Anastos 1967, Dagron 1974, Williams 1987, Hanson 1988, Evans Grubbs 1995, Drake 2000, Barnes 1981 and 1984, Lenski 2016 and their summaries. Valla 1440.
- No em dashes or American spellings. 8 dispute boxes, each two to four sentences. 10 self-test questions and 3 carry-forward items. The other self-test answers agree with the body.
