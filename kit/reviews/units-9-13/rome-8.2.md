# Rome 8.2: Diocletian and the Tetrarchy

Verdict: keep
Body words: 2848 (target 2500); 2860 with every fix below applied (checked with `check.py --target 2500` on a scratch copy)

## Coverage
- Diocletian's rise: covered (Numerian, Aper, Margus, the kept prefect)
- Tetrarchy of two Augusti and two Caesars: covered (table, 1 March 293, "not a partition")
- Jovius and Herculius: covered (Panegyric 10(2); agency, not divinity)
- Porphyry group in Venice: covered, outline only, handed to module 10.3 as the lane note asks
- Provinces into dioceses: covered (Verona List, Zuckerman dispute)
- Separation of civil and military commands: covered, brief (one sentence; *duces*; Constantine completes it)
- Enlarged army and court: covered (John the Lydian, new legions, *comitatus*, residences; late army handed to 9.2)
- Tax reform: covered (*iuga* and *capita*, Optatus' edict of 297, coinage of about 294, indiction pointed back to 0.3)
- Edict on Maximum Prices of 301: covered
- "Dominate", adoration and the debate over dropping the term: covered
- Great Persecution from 303 as Lactantius and Eusebius tell it: covered
- The Manichaeans: covered
- Abdication of 305: covered
- Palace at Split: covered
- Collapse of the system in the following decade: covered as an outline, as the lane note asks (8.3 takes 306 to 312 in detail)

## Findings
1. [should-fix] [attribution] Section "The ancestral gods defended: incest law and the Manichaeans".
   Current: "most scholars, Corcoran and Samuel Lieu among them, prefer 302; Richard Frye and Beate Dignas argued for 297."
   Problem: The writer took the names for 297 from a thesis footnote and was unsure of them. I could not trace a statement by Frye or Dignas dating the rescript to 297. Lieu's side checks out. The spec says to give the view without a name when unsure.
   Fix: "most scholars, Corcoran and Samuel Lieu among them, prefer 302; others have argued for 297."
   Basis: I. Gardner and S. N. C. Lieu, *Manichaean Texts from the Roman Empire* (2004), contents: "25 Edict (rescript) of Diocletian against the sect (AD 302)". Frye and Dignas not checked: the writer's source was a footnote, and searches found nothing.

2. [minor] [attribution] Section "The Great Persecution".
   Current: "At Antioch, when the haruspices could not read the entrails"
   Problem: Lactantius places the failed sacrifice only "in partibus Orientis" (10.1), and Eusebius, *Ecclesiastical History* 8.4, names no city either. Antioch is a modern inference (Barnes's chronology), yet the sentence cites both ancient authors for it.
   Fix: "In the East, probably at Antioch, when the haruspices could not read the entrails"
   Basis: Lactantius, *On the Deaths of the Persecutors* 10.1 (from memory of the Latin: "cum ageret in partibus Orientis"). Not searched.

3. [minor] [accuracy] Section "A rebuilt state: provinces, dioceses, army and court".
   Current: "Lactantius saw provinces chopped into fragments and officials piled on every region, until those who drew pay outnumbered those who paid (7.3–4)."
   Problem: In Lactantius the people who draw pay and outnumber the payers are the multiplied soldiers (7.2–3: "adeo maior esse coeperat numerus accipientium quam dantium", followed by the deserted fields). The fragmented provinces and the swarm of officials come next, at 7.4. The sentence reverses the order and blames the officials for the imbalance.
   Fix: "Lactantius saw soldiers so multiplied that those who drew pay outnumbered those who paid, and provinces chopped into fragments with officials piled on every region (7.3–4)."
   Basis: Lactantius, *On the Deaths of the Persecutors* 7.2–4 (Latin from memory). Self-test answer 4 ("those paid outnumbered those paying (7.3)") still agrees after the fix.

4. [minor] [attribution] Section "The Great Persecution".
   Current: "<em>sine dominico non possumus</em>, "we cannot live without the Lord's day"."
   Problem: The report quotes an ancient text and gives no source. Every other quotation in the report is cited.
   Fix: "<em>sine dominico non possumus</em>, "we cannot live without the Lord's day" (<em>Acts of the Abitinian Martyrs</em>)."
   Basis: the phrase is Emeritus' answer in the Acts of the Abitinian Martyrs (the *Passio* of Saturninus, Dativus and companions). Not searched: well known.

5. [minor] [style] Sections "The Great Persecution" (three places) and the dispute box at its end (one place).
   Current: "Eusebius, <em>Ecclesiastical History</em> 8.4)"; "Eusebius, <em>Ecclesiastical History</em> 8.2.4)"; "Eusebius, <em>Ecclesiastical History</em> 8.17)"; "(<em>Ecclesiastical History</em> 8.1.7–8)"
   Problem: The rest of the Rome course cites Eusebius' history as *Church History*: modules 7.3 and 7.4 do, and so does 8.1, which 8.2 sits beside. Only 8.2 uses *Ecclesiastical History*. Bede's *Ecclesiastical History* in 0.3 and 8.5 is a different work.
   Fix: in each of the four places, "<em>Ecclesiastical History</em>" becomes "<em>Church History</em>". The rest of each string stays as it is, and the word count does not change.
   Basis: `grep` of rome/*.html: r-7.3, r-7.4 and r-8.1 all use "Church History" for Eusebius.

## Confirmed
- Pointer "module 8.1 weighs all three" (HA, Zosimus, breviaries): r-8.1 "Lost and garbled sources" does.
- Pointer "the sort of tale module 8.1 warns against": r-8.1 treats the HA as forgery (and points on to 0.1).
- Pointer "Module 8.1 told how the silver coinage collapsed": r-8.1 "The coin and the prices".
- Pointer "The persecutions of Decius and Valerian are module 8.1's": r-8.1 "Decius: the order to sacrifice" covers both, and it hands 303 to 8.2.
- Pointer "Trajan's rule ... is module 2.5's": r-2.5 (Pliny, *Letters* 10.97).
- Pointer to module 7.5 "government without bureaucracy: a few dozen governors and about a hundred procurators": r-7.5 says "a few dozen governors ... a little over a hundred procurators" (Pflaum), cities doing the work. The petition-and-response pointer is true too. One sentence, no retelling.
- Pointers to module 0.3 (indiction from Diocletian's assessments; "most historians now say 'late empire'"): r-0.3 says both. 0.3's "rebuilt state of module 8.2" hand-off is kept.
- Pointer to Greek module 11.4 for prostration before Persian kings: r-11.4 "Proskynesis at Bactra" with Herodotus 1.134.
- Pointers to unwritten modules match their prompts: 8.3 (York 306, Donatists, 313), 9.1 (Theodosian Code), 9.2 (late army of field and frontier troops), 9.5 (Curia), 10.3 (the Tetrarchs as late antique style).
- Lane: the Great Persecution is told here in full. The army is outlined and handed to 9.2, law to 9.1, the porphyry group to 10.3. Events from 306 to 312 come as a single outline paragraph. `crosscheck.py`: no shared passages and no duplicated dispute boxes with any neighbour.
- Zuckerman, "Sur la liste de Vérone ...", *Travaux et Mémoires* 14 (2002) 617–637: dioceses created in 314 by Constantine and Licinius. It names Seston for 297 and Barnes for 293 (Zuckerman's own summary, academia.edu/2108633).
- John the Lydian, *On the Months* 1.27: fleets 45,562 (romanarmytalk thread citing "De Mens. I.27"). The army figure of 389,704 is given in en.wikipedia "Late Roman army" (after Treadgold).
- Kolb, *Herrscherideologie in der Spätantike* (Akademie Verlag, 2001): Diocletian "took various preexisting trends and molded them into a new and formal court ceremonial" (BMCR 2002.07.02, Epplett).
- Bleicken, *Prinzipat und Dominat* (Wiesbaden 1978): no genuine constitutional transformation behind the division (en.wikipedia "Dominate", citing Bleicken 1978 pp. 8, 22–25).
- Alföldi's ceremonial studies in *Römische Mitteilungen* 49 (1934) and 50 (1935): dates right, and his thesis was gradual development from the Principate (from knowledge).
- Corcoran, *The Empire of the Tetrarchs* (1996): the edict "was probably not widely circulated outside the eastern empire" (en.wikipedia "Edict on Maximum Prices", reporting Corcoran). Find-spots of the copies (Phrygia, Caria, Greece, Crete, Cyrenaica) and the purple silk at 150,000 denarii: same source.
- Edict prices: wheat at 100 denarii the castrensis modius (1.1); farm labourer 25 with keep (7.1a); rhetor 250 a month a pupil (7.71). From knowledge of the text.
- P.Cair.Isid. 1, edict of Aristius Optatus, 16 March 297 (droitromain.univ-grenoble-alpes.fr, Johnson's translation headed "March 16, AD 297"; HGV 17375).
- Panegyric 10(2).11.6 and 7.5–6: Diocletian as Jupiter who oversees, Maximian as Hercules who carries out (uvm.edu translation of Pan. Lat. 10(2)).
- Gibbon, *Decline and Fall* ch. 16: ninety-two martyrs of Palestine, Palestine a sixteenth of the East, "somewhat less than two thousand persons" in all (sacred-texts.com, Gibbon vol. 2).
- Porphyry Tetrarchs: heel of the missing foot found in Istanbul in the 1960s near the Bodrum Mosque, Philadelphion, taken in 1204 (en.wikipedia "Portrait of the Four Tetrarchs").
- *Epitome de Caesaribus* 38.8 (Carinus killed by a tribune whose wife he had violated), 39.6 (the cabbages at Salona), 40.10 (Maximian's parents labouring for wages near Sirmium), 40.16 (Galerius born and buried in Dacia Ripensis): Banchich's translation, roman-emperors.sites.luc.edu/epitome.htm.
- Eutropius 9.19 (Dalmatian; scribe's son or freedman of Anullinus), 9.20 (oath and the killing of Aper), 9.24 ("per aliquot passuum milia purpuratus"), 9.26 (the quoted Latin, adoration, gems), 9.27 (Maximian "invitus paruit"), 9.28 (deified as a private man); Ammianus 14.11.10 (about a mile on foot). From knowledge of the texts.
- Aurelius Victor 39.1 (*domesticos regens*), 39.4 (first after Caligula and Domitian to be called *dominus* and adored), 39.29 (*ut parentem seu dei magni*), 39.31 (*parti Italiae ... tributorum ingens malum*). From knowledge, not fetched.
- Lactantius 7.2 (soldiers multiplied), 7.6–7 (outcome of the price edict), 12–13 (23 February 303, the edict, the man roasted), 15.7 and 16.1 (Gaul spared), 16.4 (Hierocles), 17 (vicennalia, illness), 19 (abdication scene), 26 (census of Rome), 34–35 (edict of 30 April 311, posted at Nicomedia), 42 (statues thrown down). From knowledge.
- Eusebius, *Church History* 8.1.7–8, 8.2.4–5, 8.6.8–10, 8.17; *Martyrs of Palestine* 3.1; *Life of Constantine* 2.50–51 (Apollo and "the just on earth"). From knowledge.
- *Collatio* 6.4 (incest edict, Damascus, 295) and 15.3 (Manichaean rescript to Julianus, Alexandria, 31 March, year lost; leaders burned with their books, *honorati* sent to the mines; "maximi enim criminis est retractare ..."). From knowledge; the punishments were also checked in the philipharland.com translation.
- Jerome, *On Illustrious Men* 80 (Lactantius summoned to Nicomedia); Suetonius, *Domitian* 13.2; Panegyric 11(3).11 (adoration at Milan); Panegyric 7(6) (Capitoline oath, at 15.6); HA *Carus* 14–15 (the druidess and the boar); Syro-Roman Law Book on the *iugum* (5 iugera vineyard; 20, 40, 60 arable). From knowledge.
- Dates: 20 November 284 at Nicomedia; 1 March 293; Carnuntum 11 November 308; Constantius at York 25 July 306; Maxentius 28 October 306; Cirta search 19 May 303, preserved in the *Gesta apud Zenophilum* of 320; Robert Adam's *Ruins ... at Spalatro*, 1764; de Ste. Croix, *HTR* 47 (1954). From knowledge.
- House style: British spelling, no em dashes, no preamble. Five dispute boxes of two or three sentences, each with names on both sides. Self-test answers agree with the body. Carry-forward items transfer.
