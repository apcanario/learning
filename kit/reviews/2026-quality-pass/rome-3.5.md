# Rome 3.5: Pyrrhus and the Greek south

Verdict: fix
Body words: 2824 (target 2500)

## Coverage
- Tarentum and the insult to the Roman envoy in the theatre: covered
- Pyrrhus' landing: covered
- Heraclea (280) and Asculum (279): covered
- the elephants: covered
- the "Pyrrhic victory" (Plutarch, Pyrrhus 21): covered by explicit hand-off to Greek module 7.3, which quotes it
- Cineas' embassy and the Senate as an assembly of kings: covered
- Appius Claudius Caecus' speech: covered
- Fabricius and the offer to poison Pyrrhus, and the Roman self-image it served: covered
- Pyrrhus in Sicily: covered (briefly, with hand-off to Greek module 7.3)
- Beneventum (275): covered
- fall of Tarentum (272): covered
- the Campanian garrison at Rhegium and its punishment: covered
- Rome's first silver coinage on the Greek model: covered
- Pyrrhus' Achillean claim against a Trojan Rome: covered (with pointer to module 1.3)
- what Greek Italy gave Rome before Latin literature: covered
- how the war made the Greek world notice Rome (Timaeus, Lycophron's Alexandra): covered
- concentration on Roman sources and legends, with Greek 7.3 for the Greek side: respected

## Findings
1. [error] [attribution] Section "Tarentum and the soiled toga (282)".
   Current: "and in 282 Gaius Fabricius relieved it (Livy, <em>Periochae</em> 12)."
   Problem: Periocha 12 mentions neither Thurii's relief nor Fabricius. Periocha 11 records only the decision to help Thurii against the Lucanians, and Fabricius is first named in Periocha 13. Valerius Maximus 1.8.6 is the source for Fabricius relieving Thurii as consul, and Pliny, Natural History 34.32 for the Thurians' statue of him.
   Fix: "and in 282 Gaius Fabricius relieved it (Livy, <em>Periochae</em> 11; Valerius Maximus 1.8.6)."
   Basis: https://www.livius.org/sources/content/livy/livy-periochae-11-15/ (Per. 11.12 on Thurii; Fabricius at 13.3 and 13.11); https://www.attalus.org/names/l/luscinus.html (Valerius Maximus 1.8.6; Pliny 34.32).

2. [error] [pointer] Section "Heraclea and Asculum as Rome remembered them (280–279)".
   Current: "his army and order of battle are in Greek module 7.3."
   Problem: Greek 7.3 gives only the army's size ("some 25,000 men and twenty elephants") and the names of the two battles. It has no order of battle.
   Fix: "the size of his army is in Greek module 7.3."
   Basis: greece/r-7.3.html, section "First contact: Pyrrhus and the Illyrian wars (280–219)".

3. [should-fix] [pointer] Section "Tarentum and the soiled toga (282)".
   Current: "a violated envoy made the war just in fetial terms (module 4.4),"
   Problem: Module 4.4 says "The fetial rite itself is module 2.3" and deals with the fetials only as legal advisers on overseas wars. The demand for redress and the declaration are in 2.3.
   Fix: "a violated envoy made the war just in fetial terms (modules 2.3 and 4.4),"
   Basis: rome/r-2.3.html, "The brotherhoods: Salii, Arvals, Luperci, fetials"; rome/r-4.4.html.

4. [minor] [attribution] Section "Cineas, the blind censor and the assembly of kings".
   Current: "and, Cato later boasted, by their wives (Livy 34.4.6)."
   Problem: The boast comes in the speech that Livy wrote for Cato in the Oppian law debate of 195. The citation is to Livy, so the speaker should be Livy's Cato.
   Fix: "and, Livy's Cato later boasted, by their wives (Livy 34.4.6)."
   Basis: Livy 34.2–4 (Cato's speech, Livy's composition).

5. [minor] [style] Section "Sicily, Beneventum and elephants at Rome (278–275)".
   Current: "(Frontinus, <em>Aqueducts</em> 1.6)"
   Problem: Module 3.4 cites the same work as "<em>On Aqueducts</em> 5", by chapter. Neighbouring reports should use one form.
   Fix: "(Frontinus, <em>On Aqueducts</em> 6)"
   Basis: rome/r-3.4.html, "Appius Claudius Caecus".

6. [minor] [style] Section "Achilles against Troy, and the Greek world looks west".
   Current: "(<em>Aeneid</em> 6.836–840; deep dive unit 12)."
   Problem: AGENT-SPEC asks for deep dives as "deep dive module X.Y", and a module exists for book 6, including the parade of heroes.
   Fix: "(<em>Aeneid</em> 6.836–840; deep dive module 12.5)."
   Basis: AGENT-SPEC.md, Rome course; roman-syllabus.html, module 12.5 prompt.

## Confirmed
- Plutarch's Pyrrhus follows Hieronymus and the royal memoirs; Zonaras 8.2–6; Gellius 3.8 (Antias names Timochares of Ambracia, Quadrigarius names Nicias and quotes the consuls' letter).
- Appian, Samnite History 7 (Cornelius, ten ships, sightseeing, the Lacinian treaty, the garrison expelled from Thurii); Dio and Zonaras name Lucius Valerius; Dionysius 19.5 (Philonides).
- Periocha 14.9 (a Carthaginian fleet helps Tarentum, breaking the treaty); Periocha 15 (silver first used; Ariminum and Beneventum) (Livius.org, as above).
- Plutarch, Pyrrhus 14 (Cineas' words worth more than arms), 15 (storm), 16 (the order of the barbarians), 17 (Dionysius' nearly 15,000 and 13,000; Hieronymus' 7,000 and under 4,000), 18–19 (Appius; the council of kings; the hydra), 20 (the elephant behind the curtain; Saturnalia parole), 21 (the poison letter; Hieronymus' 6,000; the memoirs' 3,505; Dionysius' single day), 23 (wrestling ground), 25 (Maleventum).
- Varro, De lingua Latina 7.39 and Pliny, Natural History 8.16 (Lucanian oxen; first elephants at Rome in Curius' triumph); Eutropius 2.11, 2.14.
- Dionysius 20.1 (300 ox-wagons).
- Dio and Zonaras have Decius survive a frustrated devotio; Cicero names him among the Decii who died; Kent (2020) calls it a later fabrication (https://en.wikipedia.org/wiki/Publius_Decius_Mus_(consul_279_BC)). This box is the proposed single home for the dispute (finding 4 in rome-3.2.md).
- Justin 18.1–2: a second battle, then Mago with 120 ships, then Fabricius' terms and Cineas' embassy (https://www.attalus.org/translate/justin2.html#18.2).
- Appian, Samnite History 10 (the terms); Cicero, On Old Age 16 (two lines of Ennius) and Brutus 61 (Appius' speech extant); Livy 34.4.6.
- Dionysius 19.13–18 (Fabricius' speech on poverty); Cicero, On Duties 3.86–87, 1.38 ("digna Aeacidarum genere sententia"); Gellius 4.8 (Rufinus, ten pounds of silver); Plutarch, Cato Maior 2 (Curius' turnips); Livy 42.47 ("nova sapientia").
- Polybius 3.25 (the treaty of 279/8, module 4.1); Dionysius 20.9 (Locri's treasury); Livy 29.18 (the Locrians against Pleminius, 204).
- Pliny, Natural History 3.105 (Maleventum renamed); Frontinus, On Aqueducts 6 (Anio Vetus from Pyrrhic spoils); Frontinus, Stratagems 4.1.14; Livy 35.14.8.
- Zonaras 8.6 (Milo and Papirius Cursor); Orosius 4.3.1–2; the Locrian stater of Roma and Pistis.
- Polybius 1.7.6–13 (Rhegium; more than 300 taken alive), 1.10.4; Livy 28.28 (4,000); Valerius Maximus 2.7.15.
- Velleius 1.14.7 (Cosa and Paestum, 273); Fasti Triumphales (Sallentini and Messapians, 266; Volsinii, 264).
- Crawford, RRC 20 (Hercules and wolf) dated 269–266; RRC 13 (Mars and horse's head); Pliny, Natural History 33.44; Morgantina and the denarius about 211; Aelian, On Animals 1.38.
- Cicero, Pro Balbo 55; Pliny, Natural History 34.26 (Pythagoras and Alcibiades); 7.214 (Messalla's sundial, 263, ninety-nine years).
- Polybius 1.20.14 (ships from Tarentum, Locri, Velia and Naples for the crossing of 264).
- Cicero, Brutus 72–73 (Livius Andronicus, 240; Accius' 209 refuted); Ennius born at Rudiae in 239.
- Pausanias 1.12.1; Cicero, On Divination 2.116; Virgil, Aeneid 6.836–840 (the Aeacid as Perseus).
- Syll.³ 392 (Dodona dedication); Dionysius 1.6.1 (Hieronymus, then Timaeus with a separate work on Pyrrhus); Polybius 1.5.1; Dionysius 20.14 and Valerius Maximus 4.3.9 (Ptolemy's gifts, 273); Valerius Maximus 6.6.5 (the Apollonian envoys).
- Lycophron, Alexandra 1226–1230, 1435–1450. Hornblower (2015) dates the poem about 190 and agrees with Beloch and Gruen that the figure is Flamininus; Momigliano argued for the third century from the silence on the First Punic War (https://bmcr.brynmawr.edu/?p=35659).
- Pointers checked and true: Greek 7.3 (campaign summary; Plutarch, Pyrrhus 21 quoted for "Pyrrhic victory"; Sicily 278–276; Livy 42.47); 3.2 and 3.4 (the earlier Decii); 3.4 (Appius' censorship of 312); 4.3 (no negotiation with an invader after Cannae); 4.1 (the third treaty); 4.2 (wrestling ground; the fleet at Tarentum as breach); 1.4 (the ROMANO wolf didrachm of about 269–266); 1.5 (Numa and Pythagoras); 4.5 (Livius Andronicus and Ennius); 1.3 (Pyrrhus as Achilles' heir against Trojans).
