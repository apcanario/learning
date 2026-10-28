# Rome 5.3: Pompey, Crassus, Cicero and Catiline

Verdict: fix
Body words: 2717 (target 2500)

## Coverage
- Lepidus' revolt: covered
- Sertorius in Spain: covered
- Spartacus' slave war of 73–71 and its sources: covered
- Consulship of Pompey and Crassus in 70 and the dismantling of Sulla's system: covered
- Verres and the Verrines: covered
- Gabinian law and the pirate command: covered
- Manilian law and the Mithridatic command: covered
- Pompey's settlement of the East and the end of the Seleucids, pointing back to Greek 7.3: covered
- Cicero's consulship and the conspiracy of 63: covered
- Sallust's Catiline compared with Cicero's four speeches: covered (table and comparison paragraph)
- Execution of the conspirators without trial: covered
- Caesar's early career: covered
- Clodius and the Bona Dea scandal: covered
- The alliance of 60: covered
- Why "first triumvirate" is a modern label: covered (the label's own date, first attested 1681, could be added but is not required)

## Findings
1. [error] [accuracy] Section "Carry forward", item 1.
   Current: "Pompey's career from 77 to 62 was a run of commands voted over senatorial objection,"
   Problem: The Spanish command of 77 was the Senate's own grant, on Philippus' motion, as the report itself says in its first section; only the Gabinian and Manilian commands were carried by the people over senatorial objection.
   Fix: "Pompey's career from 77 to 62 was a run of commands, the greatest of them voted by the people over senatorial objection,"
   Basis: the report's section "Sulla's system under attack: Lepidus and Sertorius" (Cicero, Philippics 11.18); Plutarch, Pompey 17 and 25; Cicero, De imperio Cn. Pompei 62.

2. [should-fix] [accuracy] Section "Pompey's return and the alliance of 60" (dispute box).
   Current: "Dio (37.54–58), Plutarch (<em>Caesar</em> 13–14) and the Livian epitome (<em>Periochae</em> 103) put the compact before Caesar's election in 60; Suetonius sets it after the election (<em>Julius</em> 19), Velleius in the consulship (2.44.1)."
   Problem: Dio is not a clean witness for "before": at 37.54.3 Caesar courts the two, still enemies, "won them over and was unanimously elected", and the reconciliation and compact are narrated after the election (37.55–58); modern lists count Dio with Suetonius and Velleius. Appian, who does put the compact before the election (Civil Wars 2.9), is missing.
   Fix: "Plutarch (<em>Caesar</em> 13–14), Appian (<em>Civil Wars</em> 2.9) and the Livian epitome (<em>Periochae</em> 103) put the compact before Caesar's election in 60; Dio has him win both men over before it but narrates the compact after (37.54–58), Suetonius sets it after the election (<em>Julius</em> 19), Velleius in the consulship (2.44.1)."
   Basis: Dio 37.54, https://www.lexundria.com/dio/37.54/cy, and 37.56, https://lexundria.com/dio/37.56/cy; Appian, Civil Wars 2.9 (Pompey's sworn support for the consulship, then Crassus brought in, then the election), https://cts.perseids.org/read/greekLit/tlg0551/tlg017/perseus-eng2/2.1.4-2.2.13; Periochae 103.6, pact while Caesar was a candidate, https://www.livius.org/sources/content/livy/livy-periochae-101-105/; Wikipedia, "First Triumvirate" (Plutarch, Livy and Appian before the election; Velleius, Suetonius and Dio after, citing Gruen), https://en.wikipedia.org/wiki/First_Triumvirate.

3. [minor] [pointer] Section "The great commands: the Gabinian and Manilian laws".
   Current: "Lucullus had driven Mithridates from Pontus and taken Tigranocerta (Greek module 7.3), but"
   Problem: Greek 7.3 has Lucullus drive Mithridates from Pontus (73–67) but never mentions Tigranocerta or Tigranes, so the pointer is true of only half its clause. Tigranes also appears in the next section without introduction.
   Fix: "Lucullus had driven Mithridates from Pontus (Greek module 7.3) and in 69 taken Tigranes' capital, Tigranocerta, but"
   Basis: greece/r-7.3.html, section "Mithridates, Sulla and Pompey (89–63)"; Plutarch, Lucullus 25–29 (Tigranocerta, 69).

4. [minor] [style] Sections "The year 70: Pompey, Crassus and the end of Sulla's constitution" and "The great commands: the Gabinian and Manilian laws".
   Current: "<em>On the Command of Gnaeus Pompeius</em> 62"; "(Cicero, <em>Pompeius</em> 32–33;"; "(<em>Pompeius</em> 35)"; "(<em>Pompeius</em> 28)"; and "(<em>Actio prima</em> 56)"
   Problem: Cicero's speeches go by Latin title (this one is De imperio Cn. Pompei); the Verrines are cited as Verrines elsewhere in the report (2.5, 2.5.162), so the first actio should be Verrines 1.56.
   Fix: "<em>De imperio Cn. Pompei</em> 62"; "(Cicero, <em>De imperio</em> 32–33;"; "(<em>De imperio</em> 35)"; "(<em>De imperio</em> 28)"; "(<em>Verrines</em> 1.56)"
   Basis: AGENT-SPEC.md citation conventions.

5. [minor] [style] Section "Pompey's return and the alliance of 60", and self-test 10.
   Current: "under the Lex Titia of 43" and "as by the Lex Titia of 43."
   Problem: The report writes lex in lower case for other laws, as module 5.5 does for this one ("The lex Titia of 27 November").
   Fix: "under the lex Titia of 43" and "as by the lex Titia of 43."
   Basis: rome/r-5.5.html; rome/r-5.2.html (lex Mamilia, lex Julia).

6. [minor] [accuracy] Section "Sulla's system under attack: Lepidus and Sertorius".
   Current: "promised to restore the confiscated land (Appian, <em>Civil Wars</em> 1.107)."
   Problem: Appian has Lepidus oppose the public funeral in the paragraph before the land promise (1.105), so the single citation covers only the second claim.
   Fix: "promised to restore the confiscated land (Appian, <em>Civil Wars</em> 1.105, 1.107)."
   Basis: Appian, Civil Wars 1.105–110, https://cts.perseids.org/read/greekLit/tlg0551/tlg017/perseus-eng2/1.12.105-1.13.110 ("Lepidus and his faction opposed this"; then the promise to restore the land); section numbers inferred from the passage's range.

With all six applied the body is 2740 words, inside the band (2250–2875).

## Confirmed
- Appian, Civil Wars 1.116: about seventy gladiators, the army grown to 70,000 (so self-test 2's 70,000 is right); 1.117: 120,000 foot, turned back; 1.118: decimation of the consular legions, with the alternative version; 1.120: 6,000 crucified on the road between Capua and Rome (https://www.livius.org/sources/content/appian/appian-spartacus/). No other ancient source for the crucifixions is known to me or cited there, so "Appian alone" stands.
- Appian, Mithridatic Wars 94: 270 ships, 120,000 foot, 4,000 horse, twenty-five legates, 6,000 talents; 95: forty days in the west and an equal time in the east (https://www.livius.org/sources/content/appian/appian-the-mithridatic-wars/appian-the-mithridatic-wars-19/).
- Appian, Civil Wars 2.5–6: Caesar's proposal of custody in Italian towns until Catiline was beaten, then trial; 2.9: Varro's Tricaranus (Perseids, as above).
- "First triumvirate" appears in no ancient source; first attested in 1681 (Wikipedia, "First Triumvirate", as above). Ancient terms: Velleius' potentiae societas, the epitome's conspiratio, Suetonius' societas.
- Periochae 103.6: the pact while Caesar was a candidate (Livius, as above).
- Checked from the texts as known: Sallust, Histories 1.55, 1.77 and 3.48 Maurenbrecher; Sallust, Catiline 18–20, 28, 31.6, 35, 40–41, 44–45, 48–49, 51.27, 51.43, 52–54, 61; Cicero, Philippics 11.18, Verrines 1.56, 2.5.5–7 and 2.5.162, De imperio Cn. Pompei 14–19, 28, 32–33, 35, 62, De lege agraria 2.3, Pro Murena 52, Against Catiline 4.7–10, Letters to Atticus 1.16.5, 2.1.3, 2.1.8, 2.3.3; Asconius on In a White Toga; Plutarch, Pompey 15, 16, 20–22, 24–26, 28, 33, 45, Crassus 8–12, Sertorius 14, 18, 22, 26, Lucullus 20 and 34, Cicero 7, 8, 22, 29, Caesar 2, 5–7, 9–11, 13–14; Suetonius, Julius 1, 9, 18, 19, 74; Velleius 2.30.5–6, 2.31.2, 2.40.3, 2.44.1; Dio 37.26–28, 37.49–50; Josephus, Jewish Antiquities 14.72; Pliny, Natural History 7.97–98; Horace, Odes 2.1.1; Periochae 97, 98, 99; Marx to Engels, 27 February 1861; Seager, Historia 1964; Bradley 1989. Figures already confirmed in the unit 5 pass (Appian 1.116 and 1.118, Velleius 2.30.5–6) not rechecked.
- Pointers true: module 5.2 (ends with Sulla's death in 78), module 0.1 (table of Plutarch, Appian and Dio; Appian the continuous narrative), module 5.6 (Sallust as a writer; it hands the speeches against Catiline back to this report), module 5.1 (Octavius' deposition; Opimius' decree), module 5.5 (the lex Titia board of five years), Greek module 7.3 (Syria annexed in 64, the Seleucids ended by decision without a battle), module 9.3 and deep dives 11.3, 11.4 (Sempronia) and 11.5 as their prompts describe them. Pointers into this report from 5.2, 5.4, 5.5 and 5.6 are true.
- The Crassus feast at ten thousand tables also appears in 2.2 (Hercules' tithe) and the Clodius hand-off sentence also appears in 5.4; each is one sentence with its own purpose. Sallust's one sentence on the First Catilinarian (31.6) is also noted in 5.6 as a point about Sallust's design; one sentence each, no duplication of substance.
