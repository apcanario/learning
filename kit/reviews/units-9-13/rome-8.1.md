# Rome 8.1: The third-century crisis

Verdict: fix
Body words: 2824 (target 2500)

## Coverage
- Maximinus Thrax and the soldier emperors: covered (Herodian on 235–238, Harzhorn, table of reigns)
- Sasanians, Shapur I, capture of Valerian in 260, Naqsh-e Rustam reliefs: covered (Ardashir handed back to 7.4 as the lane note asks)
- Goths and Decius' death at Abritus in 251: covered
- Decius' order of universal sacrifice and the Egyptian libelli: covered
- Plague of Cyprian: covered (mortality method dispute handed back to 7.3)
- Gallienus and the Gallic empire: covered
- Odaenathus and Zenobia: covered
- Aurelian, reunification, the wall, Sol Invictus: covered
- Debasement of the silver coinage and inflation: covered
- Lost and garbled sources (Historia Augusta, Zosimus, breviaries, Dexippus): covered (case against the Historia Augusta handed back to 0.1)
- Modern argument over "crisis": covered
- Lane hand-offs: all kept (starts with Maximinus' reign; Shapur after a pointer to 7.4's Ardashir; antoninianus picked up from 7.4; Historia Augusta, plague and frontier disputes not repeated; Decius' order and libelli new here; stops at 284 with pointers to 8.2)

## Findings
1. [error] [accuracy] Section "Shapur I, Valerian and the rock of Naqsh-e Rustam".
   Current: "Roman writers knew of no battle: Zosimus says Philip engineered a grain shortage and turned the troops against Gordian (1.18–19), Eutropius that Philip's treachery killed him (9.2)."
   Problem: Not all Roman writers omit a battle. Zonaras and Malalas have Gordian die after falling from his horse in battle, and the Thirteenth Sibylline Oracle, which the report later lists as a contemporary control, has him fall on campaign; even Zosimus elsewhere says he lost his life fighting in enemy country (3.32.4).
   Fix: "Most Roman writers blame Philip instead: Zosimus says he engineered a grain shortage and turned the troops against Gordian (1.18–19), Eutropius that his treachery killed him (9.2); the Byzantine chroniclers Zonaras and Malalas have Gordian die after a fall from his horse in battle."
   Basis: https://en.wikipedia.org/wiki/Battle_of_Misiche (Zonaras and Malalas via Shahbazi 2017; Sib. Or. 13.13–20); Zosimus 3.32.4 at https://www.livius.org/sources/content/zosimus/zosimus-new-history-3/zosimus-new-history-3.32/

2. [error] [pointer] Section "Aurelian: reunification, the wall and the Sun".
   Current: "The Historia Augusta's nearly fifty miles (<em>Aurelian</em> 39.2) is fiction; much still stands (module 9.5)."
   Problem: Module 9.5 is unwritten, and its prompt (the walking route) does not include the Aurelian Wall or the pyramid of Cestius among its stops, so the pointer claims a coverage the prompt does not give.
   Fix: "The Historia Augusta's nearly fifty miles (<em>Aurelian</em> 39.2) is fiction; much still stands."
   Basis: roman-syllabus.html, prompt data-id="9.5".

3. [should-fix] [register] Section "Self-test", question 6.
   Current: "It also shows the regime defending the frontier with Roman forms rather than marching on Rome."
   Problem: The body says nothing like this, and the victory of 24–25 April 260 was won by the governor in Raetia, probably before Postumus' usurpation; the altar only shows Raetia under Postumus' consuls by September. The answer credits the Gallic regime with a victory the body does not give it.
   Fix: delete.
   Basis: body text of the section "Gallienus and the Gallic empire"; the altar dates the battle to 24–25 April and the dedication to September 260 under Postumus and Honoratianus.

4. [minor] [accuracy] Section "Decius: the order to sacrifice and the death at Abritus".
   Current: "and Lactantius gives Decius a beast's death in punishment (<em>On the Deaths of the Persecutors</em> 4)"
   Problem: Lactantius has Decius killed in battle and his stripped, unburied corpse left as food for beasts and birds; "a beast's death" misstates it.
   Fix: "and Lactantius leaves his naked corpse to the beasts and birds in punishment (<em>On the Deaths of the Persecutors</em> 4)"
   Basis: Lactantius, On the Deaths of the Persecutors 4.3 ("pabulum ferarum ac volucrum").

5. [minor] [attribution] Section "Decius: the order to sacrifice and the death at Abritus".
   Current: "defeated Philip near Verona in 249 (Zosimus 1.21–22)"
   Problem: Zosimus 1.22 describes the battle but does not name the place; Verona comes from the Latin tradition.
   Fix: "defeated Philip near Verona in 249 (Zosimus 1.21–22; the place from Eutropius 9.3)"
   Basis: https://www.livius.org/sources/content/zosimus/zosimus-new-history-1/zosimus-new-history-1.22 (no place named); Eutropius 9.3 ("senior Veronae").

6. [minor] [attribution] Section "Gallienus and the Gallic empire".
   Current: "In 268, besieging the rebel Aureolus in Milan, he died in a plot devised by his prefect Heraclianus and known to Claudius (Zosimus 1.40)."
   Problem: Zosimus has Gallienus setting out against Aureolus and killed at supper on the march; the siege of Milan comes from Aurelius Victor and the Historia Augusta, not from the author cited.
   Fix: "In 268, marching against the rebel Aureolus at Milan, he died in a plot devised by his prefect Heraclianus and known to Claudius (Zosimus 1.40)."
   Basis: https://www.livius.org/sources/content/zosimus/zosimus-new-history-1/zosimus-new-history-1.40

7. [minor] [attribution] Section "Aurelian: reunification, the wall and the Sun".
   Current: "In 275, near Byzantium, officers deceived by a secretary's forged list of the condemned killed him (Zosimus 1.62)."
   Problem: Zosimus places the murder outside Perinthus (Heraclea), not near Byzantium, and has Eros forge a letter in the emperor's hand telling the men they were to die; the list is the Historia Augusta's version.
   Fix: "In 275, outside Perinthus in Thrace, officers deceived by a secretary's forged order for their own execution killed him (Zosimus 1.62)."
   Basis: https://www.livius.org/sources/content/zosimus/zosimus-new-history-1/zosimus-new-history-1.62/

8. [minor] [accuracy] Section "Maximinus and the soldier emperors" (table).
   Current: "<td>found dead; killed after defeat by Diocletian</td>"
   Problem: Eutropius has Diocletian beat Carinus at the Margus, but Aurelius Victor and the Epitome have Carinus killed by his own officers, and module 8.2 follows them; the table should not contradict its neighbour.
   Fix: "<td>found dead; killed by his own officers at the Margus</td>"
   Basis: rome/r-8.2.html, section "Sources and the rise of Diocles" (Aurelius Victor 39; Epitome 38.8).

9. [minor] [pointer] Section "Gallienus and the Gallic empire".
   Current: "(module 9.2, and module 0.2 for the dispute over defence in depth)"
   Problem: Module 0.2's dispute box is about Luttwak's grand strategy and the river frontiers; it never mentions defence in depth.
   Fix: "(module 9.2, and module 0.2 for the dispute over Luttwak's grand strategy)"
   Basis: rome/r-0.2.html, dispute box at line 76.

10. [minor] [accuracy] Section "Lost and garbled sources".
   Current: "identified in 2008–2009"
   Problem: The Austrian Academy's project page says Jana Grusková identified the fragments in 2007–2009.
   Fix: "identified between 2007 and 2009"
   Basis: https://www.oeaw.ac.at/scythica-vindobonensia/history

11. [minor] [style] Section "Aurelian: reunification, the wall and the Sun".
   Current: "Steven Hijmans (1996; 2009) argued"
   Problem: AGENT-SPEC asks for the title with the date of a modern work; neither title is given.
   Fix: "Steven Hijmans (<em>Sol: The Sun in the Art and Religions of Rome</em>, 2009) argued"
   Basis: https://heurist.huma-num.fr/heurist/judaism_and_rome/view/4043 (Hijmans 2009, Groningen thesis).

## Confirmed
- Word count 2824 within band 2250–2875 (check.py); with every fix above applied to a scratch copy it is 2868, still within band; 10 sections, 5 dispute boxes, 10 self-test questions, 3 carry-forward items; no em dashes; British spelling.
- Herodian 7.1.1–2 on Maximinus' low and barbarian origin (Livius, Herodian 7.1); 7.3, 7.4–5, 7.9, 7.10, 8.5, 8.8 for the events of 235–238 match Herodian's book divisions.
- Harzhorn battlefield found by hobby archaeologists in 2008, coins dating it 227 to shortly after 240 (CoinsWeekly, "The Battle at Harzhorn on display").
- Zosimus 1.18 (grain ships diverted), 1.23 (Gallus and the fen), 1.24 (plunder, captives, annual payment), 1.36 (plague, parley, small retinue), 1.38 (Saloninus and Silvanus surrendered and killed), 1.39 (Nisibis, Ctesiphon twice, murder at Emesa at a birthday), 1.42 (320,000 men, 6,000 ships), 1.44 (Zabdas, 70,000 against 50,000), 1.49 (wall begun by Aurelian, finished by Probus), 1.55 (female camel, caught at the Euphrates), 1.56 (Longinus condemned), 1.59 (Zenobia's death by illness or refusing food), 1.61 (Palmyra razed; temple of the Sun with statues of Helios and Bel): all checked on Livius.
- Aurelius Victor 33.8 for Postumus' death over Mainz and Zosimus 1.38.2 for Cologne (De Imperatoribus Romanis, Postumus).
- Libelli: 47 known, dated 4 June to 14 July 250; the Petesouchos priestess is W.Chr. 125 (Claytor, Tyche 30, Luther College libellus).
- Dexippus fragments in Vind. hist. gr. 73, Grusková and Martin, published from 2014 on Decius' Gothic war and the invasion of Greece (ÖAW project page).
- Eutropius 9.3 (millennium), 9.14 (moneyers and Felicissimus; Felicissimus article cites Victor 35.6 and HA Aurelian 38.2–4 for the 7,000 soldiers).
- ŠKZ figures: 500,000 denarii from Philip, 60,000 at Barbalissos, 70,000 with Valerian, captured with the prefect and senators; Misiche 244.
- Pointers checked against targets: 7.4 (ends with Maximinus' proclamation; Ardashir and Dio's report; antoninianus "module 8.1 follows the debasement"); 2.5 (Trajan's rescript "held until Decius' order of 250 (module 8.1)"); 7.3 (Gilliam, Littmans, Duncan-Jones dispute); 0.1 (Dessau, Syme, Momigliano box; Enmann's lost imperial history; Historia Augusta trap); Greek 7.4 (Herulian sack of 267); 8.2 (persecution of 303, iuga and capita tax in kind, Diocletian's system); 8.3 and 9.2 pointers consistent with their prompts.
- Incoming pointers from 8.2 ("module 8.1 weighs all three", "the sort of tale module 8.1 warns against", "Module 8.1 told how the silver coinage collapsed", Decius and Valerian persecutions) are all met; no overlap with 8.4 or 8.5.
- Modern works: Rives, "The Decree of Decius and the Religion of Empire", JRS 1999; Harper, The Fate of Rome, 2017; Harl, Coinage in the Roman Economy, 300 B.C. to A.D. 700, 1996; Rathbone, "Monetisation, not price-inflation, in third-century AD Egypt?", 1996; MacMullen, "The Epigraphic Habit in the Roman Empire", AJP 1982; Rostovtzeff 1926; Alföldy, GRBS 1974; Strobel 1993; Witschel 1999; Liebeschuetz 2007; Halsberghe 1972: titles and dates as given.
- Augsburg altar: found 1992, victory of 24–25 April 260 over the Semnones or Iuthungi, dedicated 11 September 260 under Postumus' consulship.
- P.Oxy. 12.1411 (260, Oxyrhynchite strategos orders bankers to accept the divine coin); Cyprian, On Mortality 14 and To Demetrianus 3; Eusebius, Church History 6.39, 6.41, 7.13, 7.21–22; Lactantius, On the Deaths of the Persecutors 5; Historia Augusta, Gallienus 5.5 and 13.8, Aurelian 39.2.
