# Rome 1.5: The seven kings

Verdict: fix
Body words: 3399 (target 3000)

## Coverage
- each king with his institutions (Romulus' Senate and curiae; Numa, Egeria, priesthoods, calendar; Tullus, Horatii and Curiatii, Alba; Ancus and Ostia; Priscus and Demaratus; Servius' census, centuries, tribes; Superbus and the Capitoline temple): covered
- 244 years for seven reigns; why the first kings look schematic: covered
- Servius as Mastarna: Lyon tablet, François Tomb, the Vibennae: covered
- "great Rome of the Tarquins": Forum paving, Regia, Comitium and Lapis Niger (rex), Sant'Omobono, Capitoline platform, Cloaca Maxima: covered
- the Servian reforms and whether the centuriate assembly can be so early: covered
- nature of the kingship: election, interrex, rex sacrorum, warlords (Vibennae, Porsenna): covered
- modern positions from the hypercritics to Cornell and Carandini: covered
- Lucretia and the fall left to 1.6: respected

## Findings
1. [error] [accuracy] Section "The seven and who tells them".
   Current: "he survives only through Dionysius and Livy."
   Problem: Fabius' fragments come through many later writers, not just these two. The course itself cites him through Plutarch (Romulus 3.1), Polybius (1.14, 3.8–9), Cicero (On Divination 1.43) and the Tauromenium catalogue (modules 0.1, 1.3, 1.4).
   Fix: "he survives only in fragments quoted by later writers."
   Basis: T. J. Cornell (ed.), The Fragments of the Roman Historians (2013), Fabius Pictor; rome/r-0.1.html, r-1.3.html, r-1.4.html.
2. [error] [accuracy] Section "Romulus to Ancus: founder, priest, warrior, builder", dispute box.
   Current: "Livy 1.18.2 and Cicero, <em>On the Republic</em> 2.28–29, reject it on chronology, since Pythagoras reached Croton under Servius Tullius;"
   Problem: Livy puts Pythagoras under Servius Tullius, but Cicero dates his arrival in Italy to the fourth year of Tarquinius Superbus.
   Fix: "Livy 1.18.2 and Cicero, <em>On the Republic</em> 2.28–29, reject it on chronology, since Pythagoras came to Italy under Servius Tullius (Livy) or Tarquinius Superbus (Cicero);"
   Basis: Cicero, On the Republic 2.28, "quartum iam annum regnante Lucio Tarquinio Superbo" (text at https://www.studentville.it/appunti/libro-2-par-28-3/); Livy 1.18.2, "Servio Tullio regnante".
3. [error] [accuracy] Section "Seven reigns for 244 years", dispute box; and Self-test, question 3 answer.
   Current: "Numa, Ancus, Tullus and Servius are archaic names that fell out of use in the Republic, and no later forger would choose them."
   Problem: Servius stayed a common Republican first name (Servius Sulpicius Galba, consul 144; Servius Sulpicius Rufus, consul 51; the Servii Cornelii), so the argument fails for him. The self-test answer repeats the mistake.
   Fix (box): "Numa, Tullus and Ancus are first names no Republican Roman used, and no later forger would choose them."
   Fix (self-test 3, current "Cornell notes that Numa, Ancus, Tullus and Servius are archaic names out of use in the Republic, which no forger would pick."): "Cornell notes that Numa, Tullus and Ancus are first names no Republican Roman used, which no forger would pick."
   Basis: Broughton, Magistrates of the Roman Republic, consuls of 144 and 51 BC. Whether Cornell includes Servius: not checked (book not online). The fix keeps his argument for the three names it fits.
4. [should-fix] [accuracy] Section "The great Rome of the Tarquins", bullet "The Forum".
   Current: "Gjerstad's date was c. 575, and recent boreholes in the Forum Boarium may lower it again."
   Problem: The clause is unsourced and unclear: it is not said which date would be lowered, or in which direction. The Forum Boarium cores (Brock and Terrenato) date Bronze Age deposits by the river, not the Forum's first floor.
   Fix: "Gjerstad's date was c. 575."
   Basis: A. L. Brock and N. Terrenato, "Rome in the Bronze Age: late second-millennium BC radiocarbon dates from the Forum Boarium", Antiquity 90 (2016) (https://core-cms.cambridgecore.org/core/journals/antiquity/article/rome-in-the-bronze-age-late-secondmillennium-bc-radiocarbon-dates-from-the-forum-boarium/FC330DF9331002E9D359398E09204073).
5. [minor] [style] Section "The seven and who tells them", table.
   Current: "<td>534–510</td>"
   Problem: The section heading gives 753–509 and module 0.3 gives Superbus as 534–509.
   Fix: "<td>534–509</td>"
   Basis: rome/r-0.3.html ("Tarquinius Superbus (534–509)").
6. [minor] [lane] Section "Seven reigns for 244 years".
   Current: "Seven reigns in 244 years average thirty-five years each. That is implausible in any monarchy, more so in an elective one choosing grown men, in which five of the seven vanished, were killed or were expelled. Well-documented dynasties average around twenty years a reign."
   Problem: Module 0.3 ("Seven kings for 244 years") makes the same argument: thirty-five years, long dynasties "seldom average much above twenty", and Dionysius 4.6–7 on the second Tarquin. Both prompts name the problem, so neither is wrong. 1.5 is the fuller home.
   Fix: none here; module 0.3's reviewer could cut 0.3's paragraph to its anchor dates and a pointer to module 1.5.
   Basis: rome/r-0.3.html; prompts 0.3 and 1.5 in prompts-rome.json.
7. [minor] [style] Sections "Romulus to Ancus" and "Servius Tullius as the Etruscan Mastarna".
   Current: "<em>De lingua Latina</em> 5.55" and "<em>De lingua Latina</em> 5.46"
   Problem: Most of the course (0.1, 0.2, 1.1, 2.1, 2.2) writes On the Latin Language.
   Fix: "<em>On the Latin Language</em> 5.55" and "<em>On the Latin Language</em> 5.46"
   Basis: grep of rome/*.html.

## Confirmed
- Livy 6.1.2 (records lost in the Gallic fire); Book 1 about 27–25 BC; Dionysius from 7 BC; On the Republic 2 in the 50s.
- King table: Hostus Hostilius as Tullus' grandfather (Livy 1.22.1); Priscus' works; Servius from Ocresia; colonies at Signia and Circeii (1.56.3).
- Romulus: patres 1.8.7; lictors 1.8.2–3; curiae and the three centuries of knights 1.13.6–8; 300 Celeres 1.15.8; curia Faucia, Livy 9.38.15; Etruscan tribe names, Varro 5.55.
- Numa: inauguration 1.18.6–10; Janus 1.19.2; months and intercalation 1.19.6–7; priesthoods 1.20; Egeria 1.21.3; books of Numa 181 BC, Livy 40.29.3–14; Pythagoras' statue in the Comitium, Pliny 34.26.
- Tullus: "ferocior etiam Romulo" 1.22.2; 1.24–31; Herodotus 1.82 (Thyrea).
- Ancus: 1.32–33; Ostia castrum not earlier than the fourth century; Marcii Reges, Suetonius, Julius 6.1.
- Priscus: Demaratus (Livy 1.34.2; Dionysius 3.46–47; Republic 2.34); Pliny 35.152 (Eucheir, Diopos, Eugrammos); 1.34.8–9, 1.35, 1.38.6–7, 1.40–41.
- Servius: 1.39, 1.41.6 (quotation), 1.42–45, 80,000 on Fabius' authority 1.44.2; Ephesian model 1.45.2; Tullia 1.48.7; Dionysius 4.2 and Ovid, Fasti 6.627–636.
- Superbus: 1.49.3 (quotation), 1.55–56; Aristotle, Politics 1313b; Dionysius 4.6–7 against Fabius, following Piso; Livy 1.46.4; Tarquin's death in 495, 2.21.5.
- Dumézil, Mitra-Varuna (1940); Momigliano, History and Theory 23 (1984).
- Claudius' speech: Lyon 1528, CIL XIII 1668, "Tusce Mastarna ei nomen erat"; Tacitus, Annals 11.24; Suetonius, Claudius 42.2.
- François Tomb (1857), names as painted; Avile Vipiienas at Portonaccio, second quarter or middle of the sixth century (https://en.wikipedia.org/wiki/Aulus_Vibenna); Varro 5.46; Tacitus, Annals 4.65; Arnobius 6.7.
- Pasquali's "la grande Roma dei Tarquini" (1936) and the 1990 exhibition.
- Regia: bucchero bowl fragment of 530–500 found in 1899 under the Republican pavement, inscribed rex (CIL I² 2830: https://www.keytoumbria.com/ROMAN_REPUBLIC/Archaic_Inscriptions.html); Plutarch, Numa 14; Fasti 6.263–264.
- Lapis Niger cippus, Boni 1899, CIL I² 1, about 570–550, words as quoted (agrees with 0.1).
- Sant'Omobono: Dionysius 4.27; Livy 5.19.6; Hercules and Minerva about 540–530; ivory lion tessera with an Etruscan name.
- Capitoline temple: Vulca, Pliny 35.157; Horatius' dedication, Livy 2.8.6–8; Dionysius 4.61; Stamper's temple "about 34 meters wide by 38.30 meters long" on a platform (BMCR 2006.04.22, https://bmcr.brynmawr.edu/?p=25090); Hopkins, The Genesis of Roman Architecture (2016).
- Cloaca: Livy 1.38.6 and 1.56.2; vaulted conduit later (agrees with 0.2's Hopkins box).
- Servian classes: Livy's census figures and arms (1.43), 193 centuries in Dionysius 4.16–18; voting 1.43.10–11; twenty-one tribes by 495, 2.21.7; Gellius 6.13; Fraccaro (1931); pay from 406; Livy 1.60 for 509.
- Interregnum, Livy 1.17.5–6; last interrex 52 BC; Attus Clausus 504, Livy 2.16.4; rex sacrorum, 2.2.1–2; Regifugium 24 February; Q.R.C.F.
- Niebuhr, Pais, Gjerstad (founding about 575, kings to about 450), Alföldi (1965), Cornell (1995), Carandini (1997, 2007), Wiseman, "Reading Carandini" (JRS 2001), Smith (1996), Fulminante.
- Gabii: one clause with a pointer to 1.6, so no duplicate of the kept overlap.
- Pointers to 0.3, 1.3, 1.4, 1.6, 2.3 and Greek 5.3 (Lycurgus; Cypselus and the Bacchiads; tyranny) and 5.5 (Solon's classes, Cleisthenes' tribes) checked true.
