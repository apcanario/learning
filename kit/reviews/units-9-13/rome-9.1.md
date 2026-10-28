# Rome 9.1: Roman law

Verdict: fix
Body words: 2833 (target 2500)

## Coverage
- ius, fas and mos: covered
- the Twelve Tables and the pontiffs' interpretation: covered (the Tables' history and clauses pointed back to 3.1 and 2.4, as the lane note asks)
- the praetor's edict and the formulary system: covered
- the classical jurists (Q. Mucius Scaevola, Labeo, Gaius, Papinian, Ulpian, Paul): covered (Severan careers pointed back to 7.4)
- Gaius' Institutes and the Verona palimpsest of 1816: covered
- persons, things and actions: covered
- paternal power, slavery and manumission in law: covered (kept apart from 9.3, which hands the forms of manumission, the Junian Latins and the Augustan limits to 9.1)
- citizenship and its grades: covered (short; Republican ladder pointed back to 3.4)
- criminal law and its penalties (sack, crucifixion, the arena): covered
- the Theodosian Code of 438: covered
- Justinian's Corpus (Code, Digest, Institutes, Novels): thin. The Digest's method is analysed, but the Code is never described and the Novels are never named, though 8.6 hands analysis of the law to 9.1 ("outlined here and analysed in module 9.1"). See finding 3.
- Bologna and the civil-law world: covered

## Findings
1. [error] [accuracy] Section "Criminal law and its penalties".
   Current: "Sulla's courts for murder, forgery, treason and bribery punished with interdiction from water and fire, exile in effect."
   Problem: Sulla's ambitus law did not carry interdiction. The Bobbio scholiast says men convicted under the lex Cornelia were barred from office for ten years, and that the lex Calpurnia of 67 then added a fine and a lifetime ban. Exile for bribery came only with Cicero's law of 63.
   Fix: "Sulla's courts for murder, forgery and treason punished with interdiction from water and fire, exile in effect."
   Basis: Scholia Bobiensia on Pro Sulla 17 (pp. 78–79 Stangl), https://www.attalus.org/translate/bobiensia.html

2. [should-fix] [register] Section "The jurists" (first dispute box).
   Current: "the authorities of the other school that it belongs to the maker (2.79)"
   Problem: Nobody is named on the second side. Gaius names the Proculians in his Res cottidianae, as excerpted in the Digest: "Nerva and Proculus are of opinion that the maker owns that thing."
   Fix: "Nerva and Proculus that it belongs to the maker (2.79; Gaius, <em>Digest</em> 41.1.7.7)"
   Basis: Digest 41.1.7.7 (Watson translation), quoted at https://sententiaeantiquae.com/2015/12/07/who-gets-the-mead-who-would-want-it-yuk/

3. [should-fix] [lane] Section "From the jurists to the codes".
   Current: "Friedrich Bluhme showed in 1820 that the extracts in each title fall into three blocks, Sabinian, edictal and Papinianist, as if three subcommittees had read in parallel.</p>"
   Problem: The prompt names Code, Digest, Institutes and Novels. 8.6 gives only their dates and hands the analysis to 9.1. Here the Code is cited once (2.57.1) but never described, and the Novels are missing entirely. One analytical sentence covers both without repeating 8.6's history.
   Fix: "Friedrich Bluhme showed in 1820 that the extracts in each title fall into three blocks, Sabinian, edictal and Papinianist, as if three subcommittees had read in parallel. The Code's twelve books ran from Hadrian to Justinian himself, and the Novels kept changing the law: Novel 118 (543) based intestate succession on blood kinship and ended the agnates' priority.</p>"
   Basis: rome/r-8.6.html ("The law is outlined here and analysed in module 9.1"; it already gives 529/534 and "mostly in Greek", so the fix avoids both). Novel 118 of 543 and the Code's range beginning with Hadrian are standard (Smith's Dictionary, "Novellae" and "Codex", LacusCurtius). Applying all six fixes to a scratch copy gives 2869 words, inside the 2875 ceiling.

4. [should-fix] [attribution] Section "Paternal power, slavery and manumission".
   Current: "voted by the curiate assembly after the pontiffs' inquiry (1.99)"
   Problem: Gaius 1.99 says only that adrogation happens "by the people's authority", with the three questions put. The curiate comitia and the pontiffs' presiding come from Gellius.
   Fix: "voted by the curiate assembly after the pontiffs' inquiry (1.99; Gellius 5.19)"
   Basis: Gellius 5.19 (Rolfe translation: "the so-called comitia curiata are summoned under the authority of the pontiffs"), https://cts.perseids.org/read/latinLit/phi1254/phi001/perseus-eng1/5.19

5. [minor] [accuracy] Section "The jurists".
   Current: "The jurist was a senator who advised for nothing"
   Problem: This overstates. Late Republican jurists included equites such as Trebatius and Ofilius, Gaius was no senator, and the Severans held equestrian prefectures (7.4 says so).
   Fix: "The Republican jurist was usually a senator who advised for nothing"
   Basis: not checked further: standard prosopography (Kunkel, Herkunft und soziale Stellung der römischen Juristen); rome/r-7.4.html on the equestrian prefects.

6. [minor] [figure] Section "Persons, things and actions".
   Current: "The Tables' fixed twenty-five asses for assault grew absurd"
   Problem: The money figure is not sourced at the point where it is stated. Gellius gives it only in the Veratius anecdote.
   Fix: "The Tables' fixed twenty-five asses for assault (Gaius 3.223) grew absurd"
   Basis: Gaius, Institutes 3.223 (XXV assium for other iniuriae).

## Confirmed
- Pointers checked against targets: 9.3 (the council of kin, emancipation by triple sale, Pedanius); 3.1 (Tables 451–449, Flavius 304 via Livy 9.46.5, provocatio); 2.4 (funeral rules, malum carmen); 7.5 (the governor's edict modelled on the praetor's, Latin right and citizenship through office); 7.4 (Severan jurists, 212, honestiores and humiliores after Garnsey); 7.2 (Digest 1.4.1); 8.2 (Gregorian and Hermogenian codes); 8.3 (manumission in church; Constantine's laws in the codes); 8.4 (CTh 16.10); 8.6 (outline handed to 9.1); 3.4 (ladder of statuses); 4.4 (first quaestio perpetua 149); 5.3 (Gavius crucified, Verrines 2.5.162; Spartacus' six thousand); 9.4 (executions as spectacle, "the legal penalty is module 9.1's"). All true.
- Hand-offs kept: 0.3's "(module 9.1)", 7.4's "Module 9.1 takes their law further", 8.2's "module 9.1 follows to the Theodosian Code", 8.4's "module 9.1's subject" and 9.3's manumission hand-off are all met. Nothing is requoted from 3.1 (the marriage ban, Annals 6.16), 2.4, 7.2 (lex de imperio, Digest 1.4.1), 7.4 (Digest 1.3.31) or 7.5 (lex Irnitana ch. 85, Digest 1.18.13). The dates of the Justinianic Code are not repeated from 8.6.
- 9.1 and 9.3 do not duplicate each other beyond one-line pointers. Perpetua, Malleolus, Veratius, Macedo and the Giv'at ha-Mivtar heel appear in no other Rome report.
- The Ennius line (On the Republic 5.1, via Augustine, City of God 2.21) also appears in 4.5 and 5.6. Here it serves a different point (mos), in one sentence, so it is acceptable.
- Celsus in Ulpian, Digest 1.1.1 pr.; Isidore, Etymologies 5.2.2; Varro, On the Latin Language 6.29–30; Julian, Digest 1.3.32.1.
- Pomponius, Digest 1.2.2.6, .7 (Flavius stole the book), .35, .38 (Tripertita, "cradle"), .41 (Q. Mucius, eighteen books), .47 (Labeo against Capito), .49 (ius respondendi); Tacitus, Annals 3.75.
- Gaius 1.7, 1.8, 1.9–11, 1.13–15, 1.17, 1.18, 1.22, 1.29, 1.37–38, 1.42–46, 1.48, 1.53, 1.78, 1.96, 1.119, 1.134, 1.159–162, 2.2–9, 2.14a–22, 2.79, 2.87, 2.102–104, 3.56, 3.88, 3.89, 3.92, 3.182, 4.2–3, 4.11, 4.12, 4.30, 4.39–43, 4.48, 4.69–74, 4.75: contents match (from the text of the Institutes).
- Justinian, Institutes 1.5.3 (lex Iunia Norbana; all freedmen citizens) and 2.1.25 (the middle view on specification).
- Livy 6.42.11 (urban praetor); Livy 7.16.7 (the twentieth on manumission, 357); Cicero, Verrines 2.1.109 ("legem annuam", checked at https://fgh.perseids.org/read/latinLit/phi0474/phi005/perseus-eng2/2.1.105-2.1.109); On Duties 3.60 (Aquillius, "collega et familiaris meus"); On the Orator 1.212; Asconius on Pro Cornelio for the law of 67.
- Papinian, Digest 1.1.7.1; Ulpian, Digest 1.1.10 pr.–1; Eutropius 8.17 (Salvius Julianus composed the perpetual edict under Hadrian); CJ 2.57.1 (342).
- Niebuhr in Verona in 1816, Jerome over Gaius, Savigny's identification, Göschen's edition of 1820.
- Ulpian, Digest 14.6.1 and Suetonius, Vespasian 11 (SC Macedonianum); Florentinus, Digest 1.5.4.1; Ulpian, Digest 50.17.32; SC Silanianum AD 10, Digest 29.5; Suetonius, Augustus 40.4; the lex Fufia Caninia of 2 BC; the lex Aelia Sentia of AD 4.
- Acts 22.25–29 and 25.10–12; Polybius 6.14.7.
- Callistratus, Digest 48.19.28 pr. (the ladder of penalties); Gaius, Digest 47.9.9 (arsonist); Gellius 20.1.13 (Veratius) and 20.1.53 (Tarpeian Rock); Periochae 68 (Malleolus, 101); Pro Roscio Amerino 70–72; Rhetorica ad Herennium 1.23; Modestinus, Digest 48.9.9 pr. (the animals, Hadrian's rule); Juvenal 8.213–214.
- CTh 9.15.1 for Constantine's parricide law (Zalewski 2023 abstract, https://doaj.org/article/b710c13f233a4b11a64c7d6e6cc3406b).
- Mommsen (Römisches Strafrecht, 1899) on the ape, Cloud (1971) on the lex Pompeia replacing the sack with interdiction, and Bauman (1996) cautioning whether Pompey changed the penalty: all as reported at https://en.wikipedia.org/wiki/Poena_cullei.
- Tacitus, Histories 4.11 (servili supplicio); Verrines 2.5.165; Giv'at ha-Mivtar, 1968; Aurelius Victor, Caesares 41.4; Passion of Perpetua 6 (Hilarianus, procurator, 203).
- Law of Citations 426 (CTh 1.4.3, with the five jurists and the tie to Papinian); CTh 1.1.5 (429); the Code promulgated 15 February 438, in force 1 January 439; the Breviary of 506 with the Epitome Gai.
- Deo auctore (530); Tanta 1 (nearly 2,000 books, over 3,000,000 lines, about 150,000); Lenel, Palingenesia iuris civilis (1889); Bluhme (1820), three masses.
- Gradenwitz, Interpolationen in den Pandekten (1887); Beseler; Index interpolationum (1929–1935); Wieacker, Textstufen klassischer Juristen (1960); Kaser.
- Marturi placitum of 1076; Accursius' gloss; the Reichskammergericht of 1495; the BGB of 1900; the Code civil of 1804 and its three-book order; Chile 1855; Japan in the 1890s; Odofredus on Pepo and Irnerius as "lucerna iuris"; Burchard of Ursperg on Matilda; Radding, The Origins of Medieval Jurisprudence (1988).
- Self-test answers agree with the body. The carry-forward items transfer. Dispute boxes run two or three sentences (box 1 aside, see finding 2). No em dashes, British spelling, and Cicero titles follow the convention.
