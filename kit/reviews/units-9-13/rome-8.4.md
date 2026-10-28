# Rome 8.4: Julian, Theodosius and the end of the old gods

Verdict: fix
Body words: 2827 (target 2500)

## Coverage
- Sons of Constantine and Constantius II: covered (succession table, homoian policy, CTh 16.10.2, Rome visit of 357, altar removed)
- Julian's reign: covered
- Julian's pagan church: covered (high priests, letter to Arsacius, authenticity dispute)
- Misopogon: covered
- Death in Persia, 363: covered
- Ammianus as eyewitness: covered (points back to module 0.1 and does not repeat its outline)
- Valens, the Danube crossing, Adrianople 378: covered
- Theodosius and the settlement of the Goths: covered (thin on the debate, see finding 5)
- Thessalonica and Ambrose: covered
- Altar of Victory, Symmachus and Ambrose, 384: covered
- Laws against sacrifice and temples in the 390s: covered (penalty of 392 misstated, finding 1)
- Serapeum 391: covered
- Frigidus 394: covered
- End of the Vestals: covered
- End of the Olympic Games: covered by the pointer to Greek module 7.4, as the prompt asks; the Olympic dispute box is not repeated
- Slow Christianisation of the aristocracy: covered
- Lane hand-offs: all kept (starts with the sons in 337, ends with Theodosius' death in 395, Greek East handed to Greek module 7.4, Vestals' end and the Alexandrian Serapeum taken, Code to 9.1, late army to 9.2)

## Findings
1. [error] [accuracy] Section "Law, the Serapeum and the Frigidus".
   Current: "and on 8 November 392 every form of sacrifice, down to incense before household gods, treated as treason (16.10.12)."
   Problem: CTh 16.10.12 treats only blood sacrifice and reading the entrails "ad exemplum maiestatis" (§1). Incense offered to images, including the household gods banned in the preamble, is punished by forfeiture of the house or estate where it was offered (§2: "ea domo seu possessione multabitur"), not as treason.
   Fix: "and on 8 November 392 every form of cult forbidden, down to incense before household gods: sacrifice and reading entrails counted as treason, incense cost the house where it burned (16.10.12)."
   Basis: Latin of CTh 16.10.12.1–2 quoted in https://www.sglp.uzh.ch/static/veranstaltungen/FS_2012/FS12_2221_dossier3.pdf (Mommsen's text; Pharr's translation agrees).

2. [should-fix] [register] Section "Self-test", question 8.
   Current: "Sacrifice and visits to shrines, and then every form of cult down to household incense, treated as treason (<em>Codex Theodosianus</em> 16.10.10–12)."
   Problem: The answer repeats the error in finding 1. Once the body is fixed it will also contradict the body.
   Fix: "Sacrifice and visits to shrines, and then every form of cult down to household incense, with sacrifice and reading entrails treated as treason and incense punished by loss of the house (<em>Codex Theodosianus</em> 16.10.10–12)."
   Basis: as finding 1.

3. [minor] [style] Section "The altar of Victory, 384".
   Current: "The altar stood in the senate house where Augustus had placed it in 29 BC, with a statue of Victory from Tarentum (Dio 51.22.1–2)"
   Problem: House style is Octavian before 27 BC. Dio 51.22.1–2 also records only the statue from Tarentum and its dedication in the Curia Julia, not the altar, so the sentence cites him for more than he says.
   Fix: "The altar stood in the senate house before the statue of Victory from Tarentum that Octavian set up there in 29 BC (Dio 51.22.1–2)"
   Basis: Dio 51.22.1–2 (Loeb, Cary): the statue only. The altar is attested later (Herodian 5.5.7; Symmachus, <em>Relatio</em> 3.5).

4. [minor] [attribution] Section "The slow conversion of the senatorial aristocracy".
   Current: "Marius Victorinus, the rhetorician honoured with a statue in Trajan's forum, asked whether walls made Christians, then professed his faith in public (Augustine, <em>Confessions</em> 8.2.4)."
   Problem: Augustine puts the statue "in the Roman forum" (<em>Confessions</em> 8.2.3). Trajan's forum comes from Jerome's <em>Chronicle</em> for 354. The public profession is told at 8.2.5, not 8.2.4.
   Fix: "Marius Victorinus, the rhetorician honoured with a statue in Trajan's forum (Jerome, <em>Chronicle</em>, s.a. 354), asked whether walls made Christians, then professed his faith in public (Augustine, <em>Confessions</em> 8.2.4–5)."
   Basis: Augustine, <em>Confessions</em> 8.2.3 ("statuam Romano foro meruerat"), 8.2.4 ("ergo parietes faciunt christianos?"), 8.2.5; Jerome, <em>Chronicle</em> s.a. 354 ("statuam in foro Traiani meruit"). Not checked online: these are well-known texts.

5. [minor] [register] Section "Theodosius: the Goths, Thessalonica and Ambrose".
   Current: "Whether this was something new, an undefeated people inside the empire on its own terms, is debated; module 8.5 follows these Goths under Alaric."
   Problem: The report flags the disagreement but names no one on either side, and the spec asks for names on each side.
   Fix: "Whether this was something new, an undefeated people inside the empire on its own terms, is debated: Peter Heather (<em>Goths and Romans</em>, 1991) thinks so, while Malcolm Errington (<em>Chiron</em>, 1996) sees a surrender followed by patronage; module 8.5 follows these Goths under Alaric."
   Basis: R. M. Errington, "Theodosius and the Goths", <em>Chiron</em> 26 (1996) 1–27: "patronage after deditio, not that of equal partners negotiating a foedus" (https://publications.dainst.org/journals/chiron/article/view/1019/5386). Heather, <em>Goths and Romans 332–489</em> (Oxford, 1991), ch. 5, on the autonomy granted in 382.

6. [minor] [accuracy] Section "Valens, the Goths and Adrianople".
   Current: "driven by the Huns (31.2)."
   Problem: 31.2 is the ethnography of the Huns. Their attack on the Greuthungi and Tervingi, and the Tervingi's flight towards Thrace, come in 31.3.
   Fix: "driven by the Huns (31.2–3)."
   Basis: Ammianus 31.2–3 (Rolfe, Loeb).

7. [minor] [accuracy] Section "The last Vestals and the last Games".
   Current: "The last glimpse is Zosimus', a century later:"
   Problem: Zosimus' story is set in 394. Prudentius, writing around 402, still describes Vestals sitting at the gladiatorial games and turning their thumbs (<em>Against Symmachus</em> 2.1064–1113). That may be rhetoric, but it makes "last glimpse" too strong.
   Fix: "The last story of a Vestal is Zosimus', a century later:"
   Basis: Prudentius, <em>Against Symmachus</em> 2.1064–1113 (the "pollice verso" passage). Zosimus 5.38 sets the story after Theodosius' victory over Eugenius (https://www.livius.org/sources/content/zosimus/zosimus-new-history-5/zosimus-new-history-5.38).

Length note: findings 1, 3, 4, 5, 6 and 7 together bring the body to 2870 words. That is inside the +15 percent ceiling of 2875, but only just. If the maintainer adds anything else, shorten finding 5's fix (for example, drop the two titles).

Crosscheck note: the flagged overlap between dispute boxes in 8.4 and 0.3 is a false positive. They share only the name Peter Brown, and the topics differ (Thessalonica against "did Rome fall"). No passages are shared with any other report.

## Confirmed
- Ammianus 31.12.3 (scouts' 10,000), 31.12.6 (Sebastianus for battle, Victor for waiting), 31.12.7 (courtiers against sharing the glory with Gratian), 31.12.11 (eight miles, heat towards noon), 31.12.17 (return of Alatheus' and Saphrax's cavalry): https://lexundria.com/amm/31.12/y
- Ammianus 31.4.6 (the number like the sands; Ammianus is quoting Virgil, <em>Georgics</em> 2.105–106, a nuance only) and 31.4.11 (dogs traded for slaves): https://lexundria.com/amm/31.4/y
- Ammianus 25.3.3 (no breastplate), 25.3.6 (spear in the liver, "incertum unde"), 25.3.23 (Maximus and Priscus, death about midnight): https://lexundria.com/amm/25.3/y
- Brown, <em>Power and Persuasion in Late Antiquity</em> (1992) p. 111: "no dramatic encounter at the church door"; McLynn, <em>Ambrose of Milan</em> (1994; reprinted 2014) on the penance as face-saving for the emperor; Theodoret 5.17 (7,000) and 5.18 (eight months); Sozomen 7.25 (Butheric and the charioteer): https://en.wikipedia.org/wiki/Massacre_of_Thessalonica
- Van Nuffelen (2002) on forgery, citing anachronistic "Hellenismos"; Bouffartigue (2005) defending authenticity on philological grounds: https://classicalstudies.org/annual-meeting/156/abstract/authenticity-julian%E2%80%99s-epistle-22-and-its-role-emperor%E2%80%99s-pagan-project
- Only Theodoret (5.22) has the mice; Rufinus 11.23 has the soldier's double axe and the burning, with no mice and no books: https://penelope.uchicago.edu/~grout/encyclopaedia_romana/greece/paganism/serapeum.html and https://roger-pearse.com/weblog/2014/04/17/rufinus-account-of-the-fall-of-the-temple-of-serapis-in-alexandria
- Gibbon, chapter 28, cites Orosius 6.15 for the emptied book-chests: https://ccel.org/g/gibbon/decline/volume1/nt28/046.htm
- Orosius 7.33 on Valens burned by the Goths he had condemned to burn, as divine judgement: https://mmp.acdh-dev.oeaw.ac.at/archiv/stelle/detail/5873
- Ambrose's sermon on Psalm 36 is the earliest source for the wind at the Frigidus: https://en.wikipedia.org/wiki/Battle_of_the_Frigidus
- Salzman, <em>The Making of a Christian Aristocracy</em> (2002): 414 aristocrats ("several hundred" is fair), and women did not convert earlier than men: https://bmcr.brynmawr.edu/?p=22925
- Zosimus 5.38: the old woman as the only Vestal left; necklace from the statue of Rhea, the Mother of the Gods: livius.org (as above)
- CIL VI 2145 records Concordia's statue of Praetextatus and Paulina's statue of her in return
- From standard texts: CTh 16.10.2 (341) "cesset superstitio..."; CTh 13.3.5 dated 17 June 362; CTh 16.10.10 (24 February 391, to Albinus, prefect of Rome) and 16.10.11 (16 June 391, Egypt); Symmachus, <em>Relatio</em> 3.7 (Constantius left the Vestals' privileges and filled the priesthoods), 3.9 (Hannibal and the Senones), 3.10 (the quotation); Ambrose, <em>Letters</em> 17 and 18 = CSEL 72 and 73; <em>Letters</em> 40–41 (Callinicum); <em>Letter</em> 51 (penance); <em>On the Death of Theodosius</em> 34; Ammianus 22.5.2–4, 22.10.7, 22.13.1–2, 22.16.12–13, 23.2.6, 24.7.4, 25.4.17, 25.7.9–11, 26.4.3, 27.3.13–14 (137 bodies), 31.5.5–7, 31.13.12–19, 31.16.9; Julian, <em>Letter</em> 22 (Arsacius, the quotation) and <em>Letter</em> 36 (teachers) in Wright's numbering; Sozomen 5.16 preserving the Arsacius letter; Consularia Constantinopolitana s.a. 382 for 3 October; Themistius, <em>Oration</em> 16; Claudian, <em>On the Third Consulship of Honorius</em> 96–98, addressed to Honorius; Augustine, <em>City of God</em> 5.26 (Claudian quoted, golden thunderbolts); Jerome, <em>Against John of Jerusalem</em> 8; Prudentius, <em>Against Symmachus</em> 1 (the Anicii)
- Dates: 22 May 337; 9 September 337; Gallus executed 354; Strasbourg 357; Paris 360; 3 November 361; 5 March and 26 June 363; Jovian's death February 364; 9 August 378; 19 January 379; 15 May 392; 5–6 September 394; 17 January 395; the table of reigns
- Modern works as named: Bloch, "A New Document of the Last Pagan Revival in the West" (<em>Harvard Theological Review</em> 1945); Cameron, <em>The Last Pagans of Rome</em> (2011); Bagnall, "Alexandria: Library of Dreams" (<em>Proceedings of the American Philosophical Society</em> 2002); Salzman, <em>On Roman Time</em> (1990); Brown, <em>JRS</em> 51 (1961)
- Pointers: module 0.1 (Ammianus, a Greek of Antioch writing Latin at Rome around 390); module 2.3 (Vestals; the Lupercalia to Gelasius around 495); module 2.5 (Praetextatus' priesthoods, CIL VI 1779); Greek module 7.4 (Libanius, <em>Oration</em> 30; table of CTh 16.10.10 and 12; the Olympic end); module 8.5 (opens with Theodosius' death at Milan; Alaric as leader of the Goths settled in 382); 9.1 and 9.2 checked against their prompts (Theodosian Code; the late army)
- Plausible but not reached online, with no reason to doubt: Paulinus, <em>Life of Ambrose</em> 26 (Eugenius grants the altar at the request of Flavianus and Arbogast); Libanius, <em>Oration</em> 18.274–275; Eunapius, <em>Lives of the Sophists</em> 472 and 474–475 (Boissonade pages; Wright's Loeb pp. 423 and 433–435 hold the monks passage and Julian going to Maximus); Orosius 7.35.19; Symmachus, <em>Letters</em> 2.36; section 25 of the sermon on Psalm 36
