# Rome 2.1: What Roman religion was

Verdict: fix
Body words: 2733 (target 2500)

## Coverage
- religio and superstitio: covered
- why "belief" is the wrong question: covered
- pax deorum, do ut des, vows and their fulfilment: covered
- ritual exactness and instauratio: covered
- the state as religious actor, magistrates as officiants: covered
- prodigies and their expiation as Livy records them: covered
- Varro's three theologies via City of God book 6: covered
- Varro's 170 years without images: covered
- numen, the "animism" theory and its collapse: covered
- Dumézil's three functions and the archaic triad: covered
- the "no mythology" claim and the modern answers (Dumézil, Wiseman, Feeney, Beard, North and Price): covered
- religion and politics: augury in elections, On the Nature of the Gods, On Divination: covered

## Findings
1. [error] [attribution] Section "Origins: numen and the three functions".
   Current: "the second to Mars, the third to Janus Quirinus (Plutarch, <em>Marcellus</em> 8)"
   Problem: Plutarch gives the third spoils to Quirinus; "Janus Quirinus" is the reading of the law as Festus quotes it (s.v. opima spolia, p. 204 L).
   Fix: "the second to Mars, the third to Quirinus (Plutarch, <em>Marcellus</em> 8; Festus, quoting the law, has Janus Quirinus)"
   Basis: Plutarch, Marcellus 8.9, Perrin translation: "the second to Mars, and the third to Quirinus" (https://lexundria.com/plut_marc/8/prr). The LacusCurtius page for Marcellus (penelope.uchicago.edu) was blocked, so I did not use it.
2. [should-fix] [attribution] Section "The pax deorum, do ut des and the vow".
   Current: "Livy's lectisternium of 364 BC was held to secure it (7.2.2)"
   Problem: This is a pre-300 BC event, but the sentence does not say who tells the story or how long after. Livy wrote about three and a half centuries later.
   Fix: "Livy, writing some three and a half centuries later, says the lectisternium of 364 BC was held to secure it (7.2.2)"
   Basis: AGENT-SPEC source-criticism rule; Livy 7.2.2.
3. [should-fix] [attribution] Section "Varro's three theologies and the gods without images".
   Current: "Plutarch credits Numa, in agreement with Pythagoras, with the ban (<em>Numa</em> 8)."
   Problem: The regal-period claims (Varro's 170 years, Numa's ban) carry no interval between the event and the writer.
   Fix: "Plutarch, some eight centuries after Numa's supposed reign, credits him, in agreement with Pythagoras, with the ban (<em>Numa</em> 8)." Also replace "Varro also claimed that Romans worshipped" with "Varro, writing some five centuries after the period, also claimed that Romans worshipped".
   Basis: AGENT-SPEC source-criticism rule. Varro wrote the Antiquities about 47 BC; the period is 753 to 583.
4. [should-fix] [register] Section "Varro's three theologies and the gods without images".
   Current: "The imageless Rome may be philosophy rather than memory, echoing Stoic and Pythagorean critiques of images."
   Problem: This is the only dispute box in the report with no named source or scholar on either side. Ovid is cited, but only for a single fact.
   Fix: "Warde Fowler and the numen school (below) read the imageless Rome as memory; it may instead be philosophy, echoing the Stoic and Pythagorean critiques of images that Varro and Plutarch share."
   Basis: the report's own next section lists Varro's 170 years among the numen school's evidence. Augustine, City of God 4.31 has Varro's case from purity of worship, and Plutarch, Numa 8 has the Pythagorean link.
5. [should-fix] [lane] Section "Origins: numen and the three functions".
   Current: "Momigliano (<em>History and Theory</em>, 1984) objected that the system cannot be falsified and ignores Roman evidence that does not fit."
   Problem: Module 1.5 has the same objection, with the same citation, in a dispute box ("Momigliano (History and Theory, 1984) attacked the scheme as unfalsifiable and blind to Roman evidence"). Module 1.1 has a Dumézil and Momigliano box on the Iguvine triad. The prompt makes 2.1 the home for the trifunctional thesis, so this box should stay and the earlier ones should point here.
   Fix: in 2.1, after "all called Grabovius" add " (module 1.1)". In 1.5, which is outside this group, replace its Momigliano sentence with "Momigliano's objection is weighed in module 2.1."
   Basis: crosscheck section 3 (1.1 ~ 2.1); text of rome/r-1.1.html and rome/r-1.5.html.
6. [should-fix] [lane] Section "A people without myths?".
   Current: "(module 0.1 gave the source problem)"
   Problem: Module 0.1 has a dispute box on this same debate: Rose, Dumézil turning myth into history, and Wiseman and Feeney's replies. The two reports overlap and the pointer undersells 0.1. 2.1's prompt owns the debate.
   Fix: "(module 0.1 gave the source problem and a first sketch of this debate)". The maintainer may also want to cut 0.1's box to a pointer to 2.1.
   Basis: rome/r-0.1.html, box beginning "Whether Rome had a mythology is disputed."
7. [minor] [accuracy] Section "Origins: numen and the three functions".
   Current: "Dumézil (<em>Archaic Roman Religion</em>, 1966)"
   Problem: The French original appeared in 1966 and the English translation in 1970. The English title should not carry the French date.
   Fix: "Dumézil (<em>La religion romaine archaïque</em>, 1966; English 1970)"
   Basis: Payot, Paris 1966; translated by P. Krapp, University of Chicago Press 1970 (not looked up: known).
8. [minor] [style] Section "The state as worshipper".
   Current: "the dictator Fabius told the senate that he had erred more by neglecting ceremonies and auspices than by rashness (22.9.7)"
   Problem: "he" reads as Fabius. Livy means Flaminius.
   Fix: "the dictator Fabius told the senate that Flaminius had erred more by neglecting ceremonies and auspices than by rashness (22.9.7)"
   Basis: Livy 22.9.7, "peccatum a C. Flaminio consule".
9. [minor] [style] Sections "Ritual exactness and instauratio", "The state as worshipper" and Self-test question 4.
   Current: "<em>On the Response of the Haruspices</em>" (twice) and "<em>On His House</em>"
   Problem: These are speeches, so AGENT-SPEC wants Latin titles. 2.3 also uses the plural form "On the Responses of the Haruspices", which is inconsistent with this report.
   Fix: "<em>De haruspicum responso</em>" (both places) and "<em>De domo sua</em>"
   Basis: AGENT-SPEC citation conventions. 5.4 also uses "On His House", so the change is course-wide.
10. [minor] [lane] Section "A people without myths?".
   Current: "answer to Odin and Tyr (<em>Mitra-Varuna</em>, 1940)"
   Problem: Module 1.6 has the same Cocles and Scaevola comparison in a dispute box. The bullet is needed here because the prompt asks for it, but it should point back.
   Fix: "answer to Odin and Tyr (<em>Mitra-Varuna</em>, 1940; module 1.6)"
   Basis: rome/r-1.6.html, Porsenna dispute box.

## Confirmed
Checked against the texts as I know them, unless a URL is given.
- Gaius, Institutes 2.4 (res religiosae left to the di Manes); Cicero, On the Nature of the Gods 2.8 (religio, id est cultu deorum), 2.72 (relegere; superstitiosi), 1.116 (pietas iustitia adversum deos), 3.5–6 (Cotta: credere without a reason), 1.4, 3.95, 2.10–11 (Ti. Gracchus, consul 163, presiding)
- Lactantius, Divine Institutes 4.28 (religare); On Divination 2.148–149, 2.74 (left lightning; principes as interpreters), 2.51 (Cato's haruspex), 2.70 (augury kept for opinion and the state)
- Livy 7.2.2 (lectisternium of 364 for the pax deorum); 7.3 (dictator to drive the nail, 363); 21.63 (Flaminius); 22.9.7; 22.10 (ver sacrum: pontifex maximus says it needs the people; the clauses on theft, death, wrong day); 33.44 and 34.44 (performed 195, repeated 194); 21.62 (prodigies of 218/17: the infant in the Forum Holitorium, the ox on the third floor); 1.31.4 (nine-day rite under Tullus); 43.13.1–2 and 43.13.6 (Livy's scruple; two prodigies refused, private and foreign ground, 169)
- Pliny, Natural History 28.11 (prayer read from a text, with a checker, a silencer and a flute-player); Cato, On Agriculture 132, 139 (si deus si dea), 141; Plutarch, Coriolanus 25.3 (a sacrifice performed thirty times; https://lexundria.com/plut_cor/25/prr)
- Cicero, De haruspicum responso 23 (instauratio clause); De domo sua 1; On the Laws 2.31 (alio die)
- Augustine, City of God 6.4, 6.5, 4.27 (Scaevola), 4.31 (170 years), 4.8 (Forculus, Cardea, Limentinus); Plutarch, Numa 8; Pliny, Natural History 35.157 (Vulca under Tarquinius Priscus, citing Varro); Ovid, Fasti 6.295–298
- Servius auctus on Georgics 1.21 (Fabius Pictor's twelve gods for Tellus and Ceres); Varro, On the Latin Language 7.85 (numen as imperium, from nutus); Servius on Aeneid 1.292 (Mars tranquillus = Quirinus); Festus on ordo sacerdotum; Iguvine Tables (Jupiter, Mars, Vofionus Grabovius); Lavinium plaque to Castor and Pollux as qurois
- Dionysius 2.18–19 (Romulus rejects the Greek myths); Polybius 6.56.6–12
- Scheid, Quand faire, c'est croire (2005); Beard, North and Price, Religions of Rome (1998); C. King, Classical Antiquity 22 (2003); Warde Fowler 1911; Latte 1960; Bendlin 2000; Rüpke 2016; MacBain 1982; Rosenberger 1998; Rasmussen 2003; Rose, "Numen inest" (HThR 1935); Wagenvoort, Roman Dynamism (1947); Dumézil, Jupiter Mars Quirinus (1941) and Mitra-Varuna (1940); Momigliano, History and Theory 23 (1984); Wiseman, The Myths of Rome (2004); Feeney 1998, after Veyne; Beard and Schofield, JRS 76 (1986)
- Julius Obsequens' surviving lists run from 190 BC to 11 BC
- Pointers checked against their targets: Greek 8.1 (no Greek word for religion; priests attached to a single sanctuary), Greek 2.1 (castration, swallowing, Titanomachy), 0.1 (Varro's Antiquities through Augustine), 1.5 (Vulca's Jupiter), 2.2 (Capitoline triad), 2.3, 2.4, 2.5 (superstitio for the Christians; new cults through the Sibylline Books), 5.4 (Bibulus watching the sky in 59)
