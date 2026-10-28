# Rome 5.2: Marius and Sulla

Verdict: fix
Body words: 3189 (target 3000)

## Coverage
- Jugurthine War as Sallust tells it, and his theme of senatorial corruption: covered
- Marius the new man and his seven consulships: covered
- The "Marian reforms" and the modern doubts: covered (Gabba, Rich, Cadiou; client army handed to 11.2 explicitly)
- Cimbri and Teutones, Arausio, Aquae Sextiae, Vercellae: covered
- Saturninus and 100 BC: covered
- Social War of 91–88 and Livius Drusus: covered
- The Italian state, Corfinium and its coins: covered
- Citizenship grants: covered (lex Julia, lex Plautia Papiria, the tribal limits)
- Mithridates and the massacre of Romans in Asia: covered
- Sulla's march on Rome in 88, the first by a Roman army: covered
- Marius' return, the terror of 87, Cinna: covered
- Sulla's war in the East, pointing back to Greek 7.3 for the sack of Athens: covered
- Return, Colline Gate, proscriptions: covered
- Dictatorship and its reforms, retirement and death: covered
- Sulla's lost memoirs and how Plutarch used them: covered
- The Social War as rome/r-7.4.html's pointer needs it (the war and the enfranchisement after it): covered

## Findings
1. [error] [accuracy] Section "Sulla's memoirs and Plutarch".
   Current: "but for Marius he had little else beyond Posidonius (<em>Marius</em> 45)"
   Problem: Marius 45 itself names a second witness, the historian Gaius Piso, for Marius' last days, beside Posidonius on his illness; and the paragraph before has Plutarch drawing on Rutilius and Catulus as well. The claim that he had little else is unsupported.
   Fix: "and for Marius' last days he names Posidonius and the historian Gaius Piso (<em>Marius</em> 45)"
   Basis: Plutarch, Marius 45 (Perrin), https://lexundria.com/plut_mar/45/prr: "Poseidonius the philosopher" on the pleurisy, "a certain Caius Piso, an historian" on the final days.

2. [should-fix] [attribution] Section "Sulla's memoirs and Plutarch".
   Current: "his boldest unplanned ventures went best, the gods spoke in dreams, a goddess from Cappadocia handed him a thunderbolt before the march on Rome (<em>Sulla</em> 6–9); hence Felix"
   Problem: Plutarch names the memoirs for the first two claims (Sulla 6: "in his Memoirs he writes", and the dedication to Lucullus urging trust in dreams). The goddess with the thunderbolt (9) is introduced with "it is said", with no source named, so the sentence credits the memoirs with more than Plutarch does.
   Fix: "his boldest unplanned ventures went best and the gods spoke in dreams (<em>Sulla</em> 6); Plutarch adds, as hearsay, that a goddess from Cappadocia handed him a thunderbolt before the march on Rome (9); hence Felix"
   Basis: Sulla 6, https://fgh.perseids.org/read/greekLit/tlg0007/tlg033/perseus-eng2/6.1-6.12; Sulla 8–9, https://cts.perseids.org/read/greekLit/tlg0007/tlg033/perseus-eng2/8.3-9.7 ("It is said, also, that to Sulla himself there appeared in his dreams a goddess").

3. [should-fix] [register] Section "Self-test", question 3.
   Current: "Gabba saw the change as the end of a long slide, while Rich and Cadiou doubt that the army became proletarian at all."
   Problem: The body credits Rich (1983) only with denying the manpower shortage; the doubt that the army became proletarian is Cadiou's. The model answer should match the body.
   Fix: "Gabba saw the change as the end of a long slide; Rich denies the manpower shortage behind it, and Cadiou doubts that the army became proletarian at all."
   Basis: the report's own dispute box in "Marius, the new man, and the "Marian reforms""; J. W. Rich, "The supposed Roman manpower shortage of the later second century BC", Historia 32 (1983) 287–331 (title as known; not checked online).

4. [minor] [accuracy] Section "Sulla's memoirs and Plutarch".
   Current: "Plutarch read the memoirs and cites them by book."
   Problem: Plutarch cites the memoirs often but gives a book number only for the twenty-second, the one Sulla was writing two days before he died (Sulla 37, quoted later in this report).
   Fix: "Plutarch read the memoirs and cites them often."
   Basis: Plutarch, Sulla 6, 19, 37 and Marius 26, 35 (memoirs cited by name, not by book); Sulla 6 checked at the Perseids link above.

5. [minor] [pointer] Section "Civil war, the Colline Gate and the proscriptions (83–81 BC)".
   Current: "(Plutarch, <em>Pompey</em> 6; module 5.3)"
   Problem: Module 5.3 does not treat 83 or the three Picene legions; it takes up Pompey from 77. The pointer is true only of his later career.
   Fix: "(Plutarch, <em>Pompey</em> 6; module 5.3 follows his rise)"
   Basis: rome/r-5.3.html, sections "Sulla's system under attack: Lepidus and Sertorius" onwards.

6. [minor] [style] Section "The dictator's settlement, retirement and death".
   Current: "(<em>Laws</em> 3.22)"
   Problem: Elsewhere in the report, and in the self-test, the treatise is On the Laws.
   Fix: "(<em>On the Laws</em> 3.22)"
   Basis: AGENT-SPEC.md citation conventions.

7. [minor] [style] Section "Sulla's memoirs and Plutarch".
   Current: "(Cicero, <em>Brutus</em>);"
   Problem: The only Cicero citation in the report without a section; Catulus' book on his consulship and deeds, in Xenophon's manner, is Brutus 132.
   Fix: "(Cicero, <em>Brutus</em> 132);"
   Basis: Cicero, Brutus 132 (chapter 35 in the old numbering, as cited in the Wikipedia article on Catulus, https://wikipedia2006.classicistranieri.com/en/q/u/i/Quintus_Lutatius_Catulus_cc80.html); from the text as known.

8. [minor] [lane] Section "Mithridates and the march on Rome (88 BC)" (dispute box).
   Current: "Valerius Maximus (9.2 ext. 3) and Memnon of Heraclea (22.9) give 80,000 dead; Plutarch gives 150,000 (<em>Sulla</em> 24)"
   Problem: Greek module 7.3 gives the same massacre figures, so the two overlap; the overlap has a reason, since both prompts name the massacre. But Greek 7.3 assigns 150,000 to Memnon, and Memnon 22.9 has 80,000; this report is the correct one. No change here.
   Fix: none in this report. In greece/r-7.3.html replace "150,000 in Memnon (<em>FGrH</em> 434 F 22)" with "150,000 in Plutarch (<em>Sulla</em> 24)", or add a pointer from Greek 7.3 to this box.
   Basis: Memnon 22.9, "on that one day 80,000 people were killed by the sword", https://www.attalus.org/translate/memnon2.html; greece/r-7.3.html, section "Mithridates, Sulla and Pompey (89–63)".

With all eight applied the body is 3204 words, inside the band (2700–3450).

## Confirmed
- Periochae 67.2: Valerius Antias' 80,000 soldiers and 40,000 servants and camp followers at Arausio; 68.3: 200,000 killed and 90,000 captured at Aquae Sextiae; 68.6: 160,000 killed and 60,000 captured in the Cimbric battle (https://www.livius.org/sources/content/livy/livy-periochae-66-70). The 160,000 is the Livius translation's figure; some editions read 140,000, as the writers' note says.
- Memnon 25.2: 80 triremes and 3,000 talents at Dardanus; 22.9: 80,000 killed (https://www.attalus.org/translate/memnon2.html).
- Hinard (1985): over 520 proscribed, 75 known by name (51 senators, 24 knights), first list of 80, then 440 in two parts (Wikipedia, "Sulla's proscription", citing Hinard 1985, 52, 61–63, 109–110, https://en.wikipedia.org/wiki/Sulla%27s_proscription).
- Plutarch has Sulla pursued into Marius' house (Sulla 8; https://cts.perseids.org/read/greekLit/tlg0007/tlg033/perseus-eng2/8.3-9.7), and Marius 35 adds that Sulla's memoirs deny he fled there (https://cts.perseids.org/read/greekLit/tlg0007/tlg031/perseus-eng2/35.1-35.5), so "Plutarch says" is right.
- Sulla 6 cites the memoirs for unplanned ventures going best and, in their dedication to Lucullus, for trusting dreams (Perseids, as above).
- The abdication range 81–79 stands without the Vervaet attribution, which the report no longer makes.
- Checked from the texts as known: Sallust, Jugurtha 5.1, 7–11, 16, 26, 27–29, 32–35, 38, 40, 41, 44–53, 64, 73, 85, 86, 95.2–4, 102–113; Cicero, Brutus 128, On the Laws 2.14 and 3.38, On the Republic 2.40, Pro Archia 7, Pro Roscio Amerino 6 and 128, De lege agraria 3.5, Against Piso 50; Asconius on the lex Licinia Mucia (on Pro Cornelio); Velleius 2.11.1, 2.12.5, 2.13.2, 2.15, 2.20.2, 2.23.2, 2.27.1–5, 2.28, 2.32.3; Plutarch, Marius 3, 6, 10, 12, 13, 18–21, 25–28, 30, 31, 33, 37–40, 43–45, Sulla 10, 19, 22, 24, 25, 30, 31, 34, 37, 38, Crassus 2 and 6, Pompey 6, Lucullus 1 and 27; Appian, Civil Wars 1.3, 1.29–32, 1.34–39, 1.49, 1.55–60, 1.64–65, 1.71, 1.78, 1.84–86, 1.95, 1.98–104, Mithridatic Wars 11–23, 51–60; Diodorus 37.2; Strabo 4.1.13, 5.4.2; Caesar, Gallic War 1.7, 1.12; Pliny, Natural History 10.16, 22.12; Polybius 6.19.2, 11.23; Livy 1.43, 33.10; Periochae 63, 88, 89; Valerius Maximus 9.2.1, 9.2 ext. 3; Tacitus, Annals 11.22; Suetonius, Julius 77; Dio 43.9; ILS 8888; Gabba 1949; Brunt, JRS 1965; Mouritsen 1998; Cadiou 2018; Keaveney 1982.
- Pointers true: module 4.4 (Jugurtha's Numidians at Numantia; the extortion court of 149), module 5.6 (metus hostilis, Jugurtha 41), module 5.1 (the final decree), module 2.3 (colleges of fifteen under Sulla; co-optation), module 0.1 (Appian the only continuous narrative from the Gracchi to Sulla; the Periochae), module 5.3 (Asia's later debts; Lepidus; the system gone by 70), Greek module 7.3 (sack of Athens on 1 March 86, Chaeronea, Orchomenus), deep dives 11.2, 11.3 and module 9.2 as their prompts describe them. The pointer into this report from rome/r-7.4.html (the Social War) and those from 3.4, 5.3 and 6.4 are true.
- The dispute box on Italian aims shares Mouritsen with 3.4's box but makes a different point (war aims, not the process of unification); no duplication.
