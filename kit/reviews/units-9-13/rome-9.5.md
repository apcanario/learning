# Rome 9.5: Reading a site: Rome on foot

Verdict: fix
Body words: 2844 (target 2500; band 2250–2875). All fixes below applied to a scratch copy give 2865, still in band.

## Coverage
- Point back to Greek module 9.2: covered (opening paragraph, true of its target: "Everything standing on the rock belongs to one generation")
- Capitoline: temple platform covered; Tabularium covered; Capitoline Museums with the wolf, equestrian Marcus Aurelius and the Fasti covered
- Forum: Lapis Niger, Regia, temple of Vesta and House of the Vestals, Curia, Rostra, temples of Saturn, Castor and the deified Julius, the basilicas, arches of Septimius Severus and Titus: all covered
- Palatine: Iron Age huts, House of Augustus, House of Livia, Flavian palace: covered
- Imperial Fora, Trajan's Markets and Column: covered
- Colosseum and Arch of Constantine: covered
- Circus Maximus, Forum Boarium, Sant'Omobono: covered
- Campus Martius: Pantheon, Ara Pacis, Largo Argentina covered; Mausoleum covered (its look-for, the Res Gestae wall, is shared with the Ara Pacis)
- Baths of Caracalla: covered
- Palazzo Massimo: garden room from Livia's villa and the bronze Boxer covered
- For each stop what is there, which module, one thing to look for: covered (a few stops give two look-fors: Marcus Aurelius, the basilicas, the Arch of Titus, the Ara Pacis)
- Disputes, 10-question self-test, 3 carry-forward items: covered (4 dispute boxes)

## Findings
1. [error] [attribution] Section "The Capitoline" (Tabularium dispute box).
   Current (a): "The name rests, as Pier Luigi Tucci (2005) stresses, on a lost inscription"
   Current (b): "Nicholas Purcell (1993) argued that the word fits any record office and the identification is unsafe; Filippo Coarelli (2010) reads the building as the platform of a large Sullan temple."
   Problem: The box mixes up the positions. In the writer's own source (Wikipedia's summary), the point that the substructure was one record office among many is Tucci's; Purcell's point is that the inscriptions do not name the building. Tucci's main thesis, which the title of his article states, is that the temple of Juno Moneta stood on the substructure, and the box drops it, so Tucci appears only as the man who "stresses" the inscription. The side that defends the traditional name is also left unnamed. In the fix, the sides are Tucci (a record office, with Juno Moneta on top) against Coarelli (the foundations of a temple, not an archive).
   Fix (a): "The name rests on a lost inscription"
   Fix (b): "Nicholas Purcell (1993) argued that the inscriptions do not name the building; Pier Luigi Tucci (2005) took it for one record office among many, with the temple of Juno Moneta on top; Filippo Coarelli (2010) reads it as the foundations of a large Sullan temple."
   Basis: https://en.wikipedia.org/wiki/Tabularium (Purcell: the inscriptions "did not name the building"; Tucci: "likely a Tabularium", one of many record offices, Juno Moneta rededicated on the substructure about 78 BC; Coarelli: "foundations (substructio) of a large temple of the Sullan period"); title of Tucci, "'Where high Moneta leads her steps sublime': the 'Tabularium' and the Temple of Juno Moneta", JRA 18 (2005) 6–33 (https://www.cambridge.org/core/journals/journal-of-roman-archaeology/article/where-high-moneta-leads-her-steps-sublime-the-tabularium-and-the-temple-of-juno-moneta/B19607734522AEAB32F25238B967E98A). I have not read the works themselves; the abstracts are paywalled.

2. [minor] [register] Section "Self-test" (question 2), follows from finding 1.
   Current: "Purcell doubts that it was the state archive, and Coarelli makes it a temple platform."
   Problem: With the box corrected, the answer should name Tucci's position too and give Purcell's point as the box states it.
   Fix: "Purcell argues that the inscriptions do not name the building, Tucci sets the temple of Juno Moneta on it, and Coarelli makes it a temple platform."
   Basis: as finding 1.

3. [should-fix] [accuracy] Section "The Forum, west end" (the Rostra).
   Current: "The platform displayed Octavius' head in 87 (module 5.2) and Cicero's head and hands in 43 (module 5.5)."
   Problem: The platform you see at the Forum's west end is the one Caesar moved there in 44 and Augustus rebuilt. In 87 Octavius' head was shown on the old Rostra by the Comitium, so "the platform" puts the event on the wrong layer, in a report whose first carry-forward item is "which layer you are looking at". The sentence before already calls the platform of 338 a "predecessor".
   Fix: "Before Caesar moved it here in 44 (Dio 43.49.1), the platform displayed Octavius' head in 87 (module 5.2); Cicero's head and hands followed in 43 (module 5.5)."
   Basis: Dio 43.49.1 (the Rostra moved from the middle of the Forum to its present position, among the events of 44 BC), https://lexundria.com/dio/43.49.1/cy; module 5.2 (Octavius' head on the Rostra, Appian 1.71).

4. [minor] [pointer] Section "The Forum, west end" (the basilicas).
   Current: "(<em>Res Gestae</em> 20.3; module 6.2)"
   Problem: Module 6.2 cites the building list of Res Gestae 19–21 but never mentions the Basilica Julia, and no written report does. The citation is enough on its own, and the stop already names its owners (modules 4.5 and 10.3).
   Fix: "(<em>Res Gestae</em> 20.3)"
   Basis: rome/r-6.2.html, section "Brick and marble" (the list names the Curia, temples, the Lupercal, the Capitol, Pompey's theatre, aqueducts, roads and a forum, but no basilica); grep of rome/*.html for "Basilica Julia".

5. [minor] [register] Section "The Imperial Fora, Trajan's Markets and the Column" (Markets dispute box).
   Current: "The museum now housed there reads"
   Problem: One side of the box is an unnamed "museum". The reading does come from the museum's own site, which credits no scholar, so the fix names the institution, at a cost of one word.
   Fix: "The Museo dei Fori Imperiali there reads"
   Basis: https://mercatiditraiano.it/en/node/6917 (a "multi-functional centre", administrative units with offices and records, "perhaps" the Procurator Fori Divi Traiani; no scholar named).

6. [minor] [accuracy] Section "The Imperial Fora, Trajan's Markets and the Column" (Markets dispute box).
   Current: "Corrado Ricci, who cleared the complex in 1926–34,"
   Problem: The writer cites the Oslo FLT page for these dates, but that page dates Ricci's works to 1924–29, with the restoration going on until 1934. Some other sources give 1926. The maintainer should pick one source and match it.
   Fix: "Corrado Ricci, who cleared the complex in 1924–34," (or keep 1926 and cite a source that gives it)
   Basis: https://flt.hf.uio.no/texts/work/219 (works "between 1924 and 1929", restoration until 1934; Ricci, "Il mercato di Traiano", Capitolium 5 (1929) 541–55).

7. [minor] [style] Section "The Forum, east end and the Sacred Way" (temple of Castor).
   Current: "dedicated, Livy says, in 484"
   Problem: AGENT-SPEC asks that, for anything before about 300 BC, the report say how many centuries after the event the source wrote. Module 2.2 does this for the same kind of claim ("nearly five centuries later").
   Fix: "dedicated, Livy says nearly five centuries later, in 484"
   Basis: AGENT-SPEC.md, Rome course rules; Livy 2.42.5, written in the 20s BC.

## Confirmed
- Lane hand-offs are kept: 6.2 ("the walk module 9.5"), 8.2 (the Curia as Diocletian's rebuilding after the fire of 283), 8.3 ("module 9.5 puts it on the walk"), 9.2 (the Arch of Titus records the triumph of 71; 9.5 points to 9.2 for it).
- None of the four boxes repeats a box in a neighbouring report. Crosscheck section 3 is empty. Tucci, Purcell, Carettoni, Iacopi with Tedone in this role, Ricci, Frothingham, Conforto and Pensabene appear in no other report. Wilson Jones appears in 10.3 only for the Pantheon porch.
- Disputes in home modules are pointed to and not retold: 1.5 (the size of the Capitoline platform: Stamper against Mura Sommella, Cifani and Hopkins), 1.4 (Lupercal), 6.2 (sacrificer, goddess, sundial), 9.4 (flooding the Colosseum; Circus seating, Dionysius' 150,000 against Pliny's 250,000), 2.2 (the foundation date of Saturn's temple), 10.3 and 8.3 (decline).
- Shared passages with home modules (crosscheck section 2) are single clauses with the owner credited: 0.1 "a record no one could have kept", 1.5 "cappellaccio tufa, about 54 by 62 metres", 7.4 (the Geta line), 8.3 (the instinctu divinitatis gloss), 10.3 (Portunus, the Boxer).
- The pointers below were checked against their targets, and all hold.
- Capitoline: 2.2 (the triad); 1.5 (cappellaccio, 54 by 62 metres, platform dispute); 7.2 (Capitol burned 69, rebuilt from June 70, Histories 4.53); 8.5 (Procopius, Wars 3.5.3–5, half the gilded roof, 455); 10.3 (Tabularium of 78 BC with engaged half-columns; Theatre of Marcellus and Colosseum in storeys); 1.4 (wolf cast in a single pour, Carruba; radiocarbon 1021–1153; twins after 1471); 0.1 and 0.3 (Fasti found 1546; Romulus over the Caeninenses); 10.4 (horseman at the Lateran taken for Constantine); 7.3 (Marcus' reign).
- Forum, west end: 2.2 (Saturn: treasury, woollen bonds, Saturnalia, 497 dispute); 5.4 (reserve treasury, Plutarch, Caesar 35); 3.3 (Antium's beaks, Livy 8.14.12); 5.2 (Octavius' head, Appian 1.71); 5.5 (Cicero's head and hands); 8.3 and 10.3 (Constantine speaking from the Rostra on the arch frieze); 7.4 (arch of 203, "restoring the state and extending the empire", Geta's line recut, dowel holes); 10.3 (Severan panels).
- Lapis Niger: 1.5 (Boni 1899, altar, column stump, cippus of 570–550 naming a rex); 0.1 (as a source); 1.4 (Festus: Romulus' tomb, Faustulus or Hostus Hostilius; Coarelli's Volcanal).
- Curia and basilicas: 8.2 (fire of 283); 5.4 (Clodius' pyre, 52); 8.4 (altar of Victory, Symmachus, 384); 4.5 and 10.3 (Basilica Porcia; Livy 39.44.7 in 10.3); 8.5 (sack of 410).
- Forum, east end: 6.2 (deified Julius dedicated in 29 on the site of the pyre, prows from Actium, Dio 51.19.2, 51.22.2); 1.6 (Castor vowed at Regillus, dedicated 484, Livy 2.20.12, 2.42.5); 0.2 (twins at Juturna's spring, Dionysius 6.13); 1.5 (Regia, Frank Brown, late seventh to later sixth century, bucchero rex, too small for a palace); 2.1 (spears of Mars in the Regia); 2.3 (October Horse; Vestals buried alive at the Colline Gate); 6.2 (house of the rex sacrorum given to the Vestals, Dio 54.27.3); 8.4 (the end of the Vestals); 9.2 (Sacred Way as the triumphal route); 7.3 (temple of Antoninus and Faustina); 7.2 (Arch of Titus, CIL VI 945); 10.3 (spoils panel, gate seen at an angle).
- Palatine: 1.4 (huts, hut of Romulus, Dionysius 1.79.11, "a village, not a founder"; Lupercal of 2007 dispute); 6.2 (Hortensius' house, Suetonius, Augustus 72.1 "modest"; lightning; Apollo dedicated 9 October 28 BC; Palatium as the word for palace); 10.3 (Second style; Domitian's palace leading to the Pantheon); 9.3 (Livia as Julia Augusta by Augustus' will, Tacitus, Annals 1.8); 7.2 (Domitian's palace); 10.2 (Statius' Silvae).
- Imperial Fora: 10.4 (Via dell'Impero opened 28 October 1932); 5.4 (Forum of Caesar and Venus Genetrix, 46); 6.2 (Mars Ultor vowed before Philippi; the exedrae with Aeneas and the Julii against Romulus and the great men); 7.2 (vessels in the Temple of Peace, Jewish War 7.158–162); 7.3 (Column dedicated 113, inscription about the hill, Trajan's ashes); 9.2 (Cichorius and Coulston on the frieze as evidence); 10.3 (the frieze as art). "No written module describes" Trajan's Markets: true, checked by grep.
- Colosseum and arch: 7.2 (Vespasian, Nero's lake, dedication in 80, Alföldy); 9.4 ("was a machine", hypogeum dated to Domitian, flooding dispute); 10.3 (radial vaults; Tuscan, Ionic and Corinthian storeys); 8.3 (Senate's arch of 315, decennalia, CIL VI 1139, reused Trajanic, Hadrianic and Aurelian sculpture).
- River quarter: 1.5 (Circus laid out by Tarquinius Priscus, Livy 1.35.8); 9.4 (colours and seating); 9.2 (triumphs through the Circus); 7.2 (Circus arch, CIL VI 944, 80–81, Pompey 63 BC); 0.2 (Forum Boarium at the Tiber Island crossing); 1.3 (Ara Maxima's Greek rite, Livy 1.7.3; Sant'Omobono terracotta Hercules and Minerva of about 530); 4.3 (Gauls and Greeks buried alive, Livy 22.57.6); 2.2 (round marble Hercules Victor); 10.3 (Portunus of about 100 BC, columns free in the porch and engaged round the cella); 1.5 (Fortuna and Mater Matuta given to Servius; fill of about 500); 1.1 (La Rocca's eighth-century Greek pottery from Sant'Omobono).
- Campus Martius: 5.2 (Catulus at Vercellae, 101); 5.4 (Senate in the hall of Pompey's theatre, 15 March 44); 7.3 (Pantheon begun under Trajan, Hetland); 6.2 (Dio 53.27.3, Caesar inside and Augustus in the porch); 10.3 (second pediment; dome); 7.3 (column of Marcus finished by 193, the Adrastus inscription); 10.3 (its frieze against Trajan's); 6.2 (Mausoleum begun 28 BC, Suetonius, Augustus 100.4; Ara Pacis dedicated 30 January 9 BC; Rehak, Buchner and Heslin disputes); 10.4 (Mausoleum isolated, Ara Pacis reassembled beside it, Res Gestae wall); 10.3 (front figures cut deep, those behind shallow).
- Baths and museum: 7.4 (inaugurated 216; 1,600 seats by Olympiodorus' count; Farnese pieces in the 1540s); 9.4 (bathing); 10.3 (bath plan; Santa Maria degli Angeli); 2.5 (Mithraism); 6.2 (Prima Porta statue found at Livia's villa); 10.3 (garden room, Second style dissolving the wall; Boxer, a Hellenistic original found on the Quirinal); Greek 9.1 (lost bronzes, copper lips); 2.3 (Fasti Antiates, the one pre-Julian calendar, in the Palazzo Massimo).
- Pointers to unwritten modules match their prompts: 11.3 (the burning of the Senate house in 52 BC); 11.7 (the hall of Pompey's theatre, the murder, Antony's funeral speech); 13.7 ("the rain miracle on the column against the Christian versions of it"; sources include "the column and the equestrian statue").
- House of Augustus box: Carettoni's identification, Iacopi and Tedone (filled in after 36 BC), Wiseman's rejection, and Wiseman's modest house in the area of the later domus Augustana. Source: BMCR 2020.09.23 (Johannes Lipps), https://bmcr.brynmawr.edu/?p=49345.
- Arch of Constantine box: Frothingham (AJA 1912, a Domitianic origin); Conforto and others, Adriano e Costantino (Electa 2001); Pensabene and Panella, Arco di Costantino tra archeologia e archeometria (1999); Wilson Jones, "Genesis and Mimesis", JSAH 59 (2000), for a single Constantinian design. From my own knowledge.
- Trajan's Markets: Ricci, "Il mercato di Traiano", Capitolium 5 (1929) (FLT, https://flt.hf.uio.no/texts/work/219); the museum's reading as a multi-functional centre, offices and records, perhaps the procurator (mercatiditraiano.it).
- Vestal base of 364 with the name erased: CIL VI 32422 (EAGLE Q6066, https://wiki.eagle-network.eu/wiki/Item:Q6066).
- Citations that are right as given: Suetonius, Tiberius 20 (Castor rebuilt in his and his brother's name); Suetonius, Julius 88 (the curia walled up); Res Gestae 20.3 (the basilica between Castor and Saturn, finished); Suetonius, Augustus 101.4 (Res Gestae on bronze before the Mausoleum); Statius, Silvae 4.2 (thanks to Domitian for a palace dinner); Dio 53.27.3 (book 53 has the same number in the Loeb and Boissevain).
- Monument facts that are right as given: the temple of Saturn inscription incendio consumptum restituit; the Curia as a church in the seventh century (Sant'Adriano, 630); Valadier's travertine restoration of the Arch of Titus (1820s); St Peter on Trajan's Column in 1587 and St Paul on Marcus' in 1589; the hypogeum of the Colosseum; the Circus Maximus arch found in 2015; temple B at Largo Argentina as Fortuna Huiusce Diei; the Pantheon inscription text; the Mithraeum under the Baths of Caracalla; the Farnese pieces in Naples; the garden room's double fence; the Boxer's copper inlays; Livia's lead pipe and the Io and Argus panel; three re-erected columns of Venus Genetrix; the Markets behind the north-eastern exedra.
- House style: no em dashes; British spelling (chiselled, colours); Octavian before 27 BC and Augustus after, used correctly throughout; the Self-test answers agree with the body, apart from question 2 once finding 1 is applied; the carry-forward items transfer.
