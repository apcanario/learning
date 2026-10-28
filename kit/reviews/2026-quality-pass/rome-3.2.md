# Rome 3.2: The legends of the early Republic

Verdict: fix
Body words: 2758 (target 2500)

## Coverage
- Coriolanus and his mother: covered
- Cincinnatus called from the plough: covered
- the 306 Fabii at the Cremera: covered
- Spurius Cassius, Spurius Maelius and Manlius Capitolinus as would-be kings: covered
- Manlius Torquatus executing his son: covered
- the devotio of the Decii: covered
- Marcus Curtius and the chasm: covered
- the women (Coriolanus' mother and wife, Verginia, the Sabine mothers): covered
- Horatius, Mucius Scaevola, Cloelia and the geese left to modules 1.6 and 3.3: respected (none retold)
- the exemplum as the Roman form of myth, and Livy's preface: covered
- family traditions and funeral orations as source: covered (funeral by explicit hand-off to modules 0.1 and 2.4, plus Polybius 6.54)
- Greek models (Coriolanus and Themistocles; the Fabii and the three hundred): covered
- Wiseman's theory of historical drama: covered
- Valerius Maximus as handbook: covered

## Findings
1. [error] [attribution] Section "Coriolanus and his mother".
   Current: "was dedicated at the fourth milestone of the Via Latina (2.40.11–12)."
   Problem: Livy 2.40.11–12 records the dedication but gives no road or milestone. The fourth milestone of the Via Latina comes from Valerius Maximus 1.8.4.
   Fix: "was dedicated (2.40.11–12) at the fourth milestone of the Via Latina (Valerius Maximus 1.8.4)."
   Basis: Livy 2.40.8–12, Perseus translation, has no location (https://cts.perseids.org/read/latinLit/phi0914/phi001/perseus-eng3/2.40.8-2.40.12); Valerius Maximus 1.8.4 is the cited source for the location (https://en.wikipedia.org/wiki/Temple_of_Fortuna_Muliebris).

2. [error] [attribution] Section "Families, funerals and the stage", dispute box.
   Current: "mostly on recent events, and Cornell finds the family and cult channels sufficient."
   Problem: The report's own Cornell source, "Coriolanus: myth, history and performance" (2003, cited in the next section), traces the Coriolanus story's survival to pre-literary "ballad, epic, or play", the kind of activity Wiseman stresses. It does not set family and cult against the stage. No other Cornell text is cited for the claim.
   Fix: "mostly on recent events; Cornell (2003) counts ballad, epic and play among the possible pre-literary carriers of the Coriolanus story."
   Basis: BMCR review of Braund and Gill (eds), Myth, History and Culture in Republican Rome (2003), https://bmcr.brynmawr.edu/?p=23163. Not checked against Cornell's chapter itself; if the maintainer has a Cornell text for the family-and-cult view, cite it instead.

3. [should-fix] [accuracy] Section "Torquatus, the Decii and Curtius", dispute box.
   Current: "which would make the story nearly contemporary;"
   Problem: Ennius was born in 239 and wrote the Annals late in life, about a century after Asculum. Skutsch's placement would make the story early and in verse, not contemporary.
   Fix: "which would put the story into Latin verse within about a century;"
   Basis: Ennius' dates (born 239; Annals composed in the 180s and 170s). The dispute itself is confirmed: Cornell, "Ennius, Annals VI: a reply", CQ 37 (1987) 514–516, rejects the Ausculum placement of lines 191–194 (https://www.cambridge.org/core/journals/classical-quarterly/article/abs/ennius-annals-vi-a-reply/438E63202E36AEA141EF4F58C08B6418).

4. [should-fix] [lane] Section "Torquatus, the Decii and Curtius", dispute box.
   Current: "The grandson's devotio is doubtful: Zonaras, epitomising Cassius Dio, says Pyrrhus learnt of the plan and it failed, and Dionysius' account of Ausculum has none."
   Problem: Module 3.5 has a full dispute box on the same question, with the same evidence (Cicero, Tusculan Disputations 1.89; Dio and Zonaras 8.5; Dionysius' silence) plus Kent (2020), and its self-test question 3 repeats it. Asculum is 3.5's battle, so the evidence belongs there. 3.2 should keep what is its own: the Ennius fragment and the suspicion that the father's devotio copies the son's.
   Fix: "The grandson's devotio is doubtful (module 3.5 sets out the evidence)."
   Basis: rome/r-3.5.html, dispute box beginning "Did a third Decius Mus devote himself at Asculum".

5. [minor] [style] Section "Torquatus, the Decii and Curtius" (body and dispute box).
   Current: "Cicero adds a grandson at Ausculum in 279"
   Problem: Module 3.5 and its prompt spell the battle Asculum. Neighbouring reports should use one form.
   Fix: "Cicero adds a grandson at Asculum in 279"; in the dispute box, change "Ausculum" to "Asculum" as well (once if finding 4 is applied, twice if not).
   Basis: prompts-rome.json 3.5; rome/r-3.5.html.

6. [minor] [style] Section "Three men who aimed at kingship" (twice).
   Current: "(Cicero, <em>On His House</em> 101)" and "(<em>On His House</em> 101)"
   Problem: De domo sua is a speech, and AGENT-SPEC asks for speeches by Latin title. The English form is used elsewhere too (2.1, 5.4), so change all of them or none.
   Fix: "(Cicero, <em>De domo sua</em> 101)" and "(<em>De domo sua</em> 101)"
   Basis: AGENT-SPEC.md, citation conventions.

## Confirmed
- Livy 2.33.5–9 (the bronze column of the treaty made by Cassius alone, his colleague away at the war); 2.34–35 (grain of 491, exile to Attius Tullius); 2.39.5 (Cluilian trench, five miles); 2.40.1, 2.40.5–8; 2.40.10–11 (Fabius Pictor, "longe antiquissimum auctorem", old age in exile).
- Dionysius 8.39 (Valeria), 8.56.2 (the statue speaks), 8.57–59 (killed); Plutarch, Coriolanus 39, 33–36 (Volumnia, Vergilia); Cicero, Brutus 41–43 (suicide; Atticus; Clitarchus' bull's blood); Thucydides 1.138.4, 1.136–137. Praenomen Gnaeus in Livy, Gaius in Dionysius and Plutarch.
- Livy 3.26.7 ("qui omnia prae divitiis humana spernunt"), 3.26.8–10 (four iugera, digging or ploughing, Racilia), 3.29.7 (sixteenth day), 3.13.8–10 (Kaeso's sureties); Livy 4.13 gives "his eightieth year" (https://fgh.perseids.org/read/latinLit/phi0914/phi001/perseus-eng3/4.13.7-4.14.2).
- A Fabius consul every year from 485 to 479 (Fasti).
- Livy 2.49 (306, right-hand arch of the Carmental gate); Ovid, Fasti 2.193–204; Dionysius 9.15.3 (4,000 clients and friends), 9.22.1–3 (survivor rejected as mythical and theatrical); Livy 2.50.11, 6.1.11 (18 July), 3.1.1 (the survivor consul in 467).
- Cicero, Philippics 2.114; Livy 2.41.1–3, 2.41.10–12; Pliny, Natural History 34.30 (censors of 158); Livy 4.13–16 (Maelius, Ahala, Aequimaelium, Minucius' gilded ox); 6.11.7, 6.14, 6.20.10–14.
- Mommsen (Hermes 1871) grouping the three; Lintott, Historia 19 (1970); Plutarch, Tiberius Gracchus 19; Cicero, Against Catiline 1.3; Dionysius 12.4.2–5 (Cincius and Piso: no dictator).
- Livy 7.9–10 and Gellius 9.13 (Quadrigarius); Livy 8.7, 8.7.22, 8.8.1, 4.29.5–6.
- Livy 8.6.9–10 (the dream), 8.9.6–8 (the formula), 8.10.11–12 (substitute legionary; seven-foot image), 8.11.1; Virgil, Aeneid 6.824–825; Livy 7.6.1–6 (Curtius, 362); Suetonius, Augustus 57.1.
- Livy 1.13 (Sabine women); Ovid, Fasti 3.167–258 (Matronalia); Livy 3.48.5 (the butcher's knife); Dionysius 11.28–37; Livy 10.23.1–10 (Plebeian Chastity, 296).
- Livy, Preface 10; Quintilian 12.2.30; Roller (2018); Chaplin (2000).
- Sallust, Catiline 52.30 (Aulus Manlius, Gallic war); Cicero, On Ends 1.23–24, 2.60–61; Suetonius, Augustus 31.5.
- Polybius 6.54.4–5; Ovid, Fasti 2.237; Plutarch, Fabius Maximus 1.2; Valerius Maximus 5.8.3 (Torquatus, 140); Brutus' denarius of 54 (RRC 433/2).
- Livy 7.2 (stage games, 364); Livy 5.21.9 (Latin text correct); praetextae titles (Naevius' Romulus, Ennius' Sabinae, Accius' Aeneadae or Decius); Flower, "Fabulae praetextae in context", CQ 1995.
- Dionysius 7.1.4–6 (Licinius and Gellius on Dionysius I); Herodotus 7.202, 7.229–231.
- Parallela minora 5 (Anchurus and Curtius) and 18 (Codrus and Publius Decius) (https://cts.perseids.org/read/greekLit/tlg0007/tlg085/perseus-eng4/0-19).
- Mommsen, Hermes 4 (1870) on Coriolanus. Cornell (2003) argues that the legend's elements fit aristocratic society of about 500 (BMCR review above), which is consistent with the report's summary.
- Valerius Maximus 9.11.ext.4 (Sejanus); 5.4.1, 4.4.7, 5.6.2, 5.6.5–6, 2.7.6, 5.8.2; Julius Paris and Januarius Nepotianus; Bloomer (1992), Skidmore (1996), Langlands (2018).
- Pointers checked and true: 0.1 (funeral eulogies corrupting the record; three explanations of the Lacus Curtius); 10.4 (syllabus: Shakespeare's Roman plays); 3.3 (Manlius on the Capitol); 3.4 (Sentinum); 3.5 (grandson at Asculum); 1.4 (the Sabine women); 3.1 (Verginia's politics); 1.6 (Livy's preface; Lucretia and Verginia paired); 2.4 (the funeral after Polybius 6.53–54).
