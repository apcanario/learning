# Rome 13.7: Marcus Aurelius: a life

Verdict: fix
Body words: 4098 (target 3000; the target is a guide, rule of 27 October 2026)

## Coverage
- Birth in 121 as Marcus Annius Verus and family: covered
- Hadrian's nickname 'Verissimus': covered (with Justin, *First Apology* 1)
- Adoptions of 138: covered, pointed back to module 7.3
- Marriage to Faustina the Younger and the children: covered
- Apprenticeship under Antoninus (*Meditations* 1.16): covered
- Fronto and Mai's palimpsests from 1815: covered
- Herodes Atticus, pointed back to Greek module 7.4: covered (target checked)
- Junius Rusticus and the turn to philosophy (*Meditations* 1.7): covered
- Accession in 161 and the partnership with Lucius as Marcus lived it: covered
- Carnuntum and Sirmium, the wars in outline: covered
- Rain miracle on the column against the Christian versions: covered
- Avidius Cassius' revolt of 175, the rumours about Faustina, her death at Halala: covered
- Commodus Augustus in 177: covered
- Martyrs of Lyon in 177 (Eusebius, *Church History* 5.1): covered
- Death in 180: covered
- Sources (*Historia Augusta*, Dio's epitomators, Herodian 1, Fronto, column, equestrian statue): covered
- Birley, *Marcus Aurelius* (1966, revised 1987): covered
- Lane note from 7.3 (the rain miracle, Cassius' revolt, Commodus' elevation, Lyon): all taken up; the plague, Parthian war, invasion, auction and column pointed back, not retold

## Findings
1. [error] [attribution] Section "Teachers: Fronto, Herodes and Rusticus".
   Current: "Dio names Rusticus and Apollonius of Chalcedon as Marcus' Stoic teachers"
   Problem: Dio 72(71).35 calls him Apollonius of Nicomedia. Chalcedon comes from the *Historia Augusta* (*Marcus* 2.7). This is the reporter-and-claim error the 25 October lessons warn about.
   Fix: "Dio names Rusticus and Apollonius of Nicomedia (the <em>Historia Augusta</em>'s Apollonius of Chalcedon, 2.7) as Marcus' Stoic teachers"
   Basis: Dio's Book 72 epitome as quoted by Donald Robertson (https://donaldrobertson.name/?p=4178): "Junius Rusticus and Apollonius of Nicomedeia". Smith's *Dictionary* s.v. Apollonius 18 (https://cts.perseids.org/read/pdlrefwk/viaf88890045/003/perseus-eng1/A.apollonius_18): "according to Dio Cassius (71.35) of Nicomedia". *Historia Augusta*, *Marcus* 2.7 on LacusCurtius (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Historia_Augusta/Marcus_Aurelius/1*.html): Apollonius of Chalcedon.

2. [error] [attribution] Section "Teachers: Fronto, Herodes and Rusticus" (dispute box).
   Current: "argued for the Trajanic jurist Titius Aristo, so that the crisis was boredom with legal study, and Birley (1987) accepted this."
   Problem: Champlin's reading is the opposite. On his view, reading Aristo convinced Marcus that Roman law stood far above rhetoric and deserved serious study, so the turn was from rhetoric to jurisprudence, not boredom with law. The box's last sentence repeats the mistake: "On the second view this is a conversion letter; on the first it is a young lawyer's restlessness."
   Fix: "argued for the Trajanic jurist Titius Aristo, so that the turn was from rhetoric to the study of law, and Birley (1987) accepted this." Also replace "On the second view this is a conversion letter; on the first it is a young lawyer's restlessness." with "On the second view this is a conversion to philosophy; on the first, if a conversion at all, it is one from rhetoric to jurisprudence."
   Basis: Görgemanns, "Der Bekehrungsbrief Marc Aurels", *Rheinisches Museum* 134, pp. 96 to 109, main text and n. 3 (https://journals.ub.uni-koeln.de/index.php/rhm/article/download/10593/10811/21918). It summarises Champlin (JRS 64, 1974, 136–159; *Fronto and Antonine Rome*, 1980): "Wenn überhaupt von einer Bekehrung die Rede sein könne, dann sei es eine von der Rhetorik zur Jurisprudenz". Birley (1987) and Gärtner (1983) follow Champlin; Hadot, *Annuaire EPHE* 92 (1983–84), 331–336, argues against him.

3. [should-fix] [register] Section "Self-test", question 5.
   Current: "if the jurist Titius Aristo (Champlin, Birley), it records a young man tired of legal study."
   Problem: The answer repeats the misreading in finding 2 and must agree with the corrected body.
   Fix: "if the jurist Titius Aristo (Champlin, Birley), it records a turn from rhetoric to the study of law."
   Basis: as finding 2.

4. [should-fix] [attribution] Section "177: Commodus Augustus and the martyrs of Lyon" (dispute box).
   Current: "Timothy Barnes (\"Eusebius and the Date of the Martyrdoms\", 1978)"
   Problem: The writer's own source, the Judaism and Rome record, cites the view that Eusebius may be completely wrong and that the persecution may fall after 180 to Barnes, *Early Christian Hagiography and Roman History* (2010), p. 61. It cites the 1978 paper only for Eusebius' unease with Latin sources. The writer did not read either work, so the view should go to the work that is cited for it. Update `bibliography/rome/r-13.7.md` to match.
   Fix: "Timothy Barnes (<em>Early Christian Hagiography and Roman History</em>, 2010)"
   Basis: https://heurist.huma-num.fr/judaism_and_rome/tpl/public-record/1248 and https://heurist.huma-num.fr/heurist/judaism_and_rome/view/2711 (the 1978 paper: *Les Martyrs de Lyon (177)*, ed. Rougé and Turcan, 137–143; no summary of its argument). Not checked against either Barnes text.

5. [should-fix] [figure] Section "Death, 180, and the image" (timeline caption).
   Current: "Commodus as Augustus, <em>Marcus</em> 27.5;"
   Problem: The text cites *Marcus* 27.5 only for the tribunician power and gives the rank of Augustus from coins and inscriptions without a passage. *Marcus* 27.5 does not say Augustus. The caption must name the passage the text cites for each item (R-1 lesson).
   Fix: "Commodus' tribunician power, <em>Marcus</em> 27.5 (the text gives his rank of Augustus from coins and inscriptions, without a passage);"
   Basis: *Historia Augusta*, *Marcus* 27.5 on LacusCurtius (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Historia_Augusta/Marcus_Aurelius/2*.html): colleague in the tribunician power, with no mention of Augustus.

6. [should-fix] [figure] Section "175: Avidius Cassius and Faustina" (flow figure).
   Current: "{\"label\": \"Letters burned, supporters pardoned\", \"note\": \"Dio 72(71).29–30\"}"
   Problem: The text says Marcus "destroyed the rebels' papers unread" and cites Dio 72(71).28–30. The figure says "burned", a word the text does not use, and cites 29–30. A figure must carry the text's words and citation (R-1).
   Fix: "{\"label\": \"Papers destroyed unread, supporters pardoned\", \"note\": \"Dio 72(71).28–30\"}"
   Basis: the report's own text, section "175: Avidius Cassius and Faustina".

7. [minor] [accuracy] Section "The heir, 138–161", and "Self-test" question 3.
   Current: "spent only two nights away from him (7.2)" and "apart only two nights (<em>Marcus</em> 7.2)"
   Problem: The twenty-three years are at 7.2, but the two nights are at 7.3.
   Fix: "spent only two nights away from him (7.2–3)" and "apart only two nights (<em>Marcus</em> 7.2–3)"
   Basis: *Historia Augusta*, *Marcus* 7.2–3 on LacusCurtius (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Historia_Augusta/Marcus_Aurelius/1*.html).

8. [minor] [accuracy] Section "Family and boyhood, 121–138".
   Current: "Dio adds a body so frail that at first it could not bear the cold, and a habit of eating only at night (72(71).6)."
   Problem: Set inside the boyhood paragraph, the sentence reads as if it describes the boy. Dio is describing the emperor on campaign, who at first could not stand the cold when addressing the assembled soldiers.
   Fix: "Dio, describing the emperor on campaign, adds a body so frail that at first it could not bear the cold, and a habit of eating only at night (72(71).6)."
   Basis: Dio 72(71).6.3–4 (Loeb, tr. Cary), from my own reading. Not re-checked online: the LacusCurtius page for Book 72 was refused (robots).

9. [minor] [accuracy] Section "Family and boyhood, 121–138".
   Current: "the boy was brought up by his paternal grandfather, twice consul and prefect of the city (1.1–2, 1.10)"
   Problem: Marcus Annius Verus was consul three times (suffect 97, ordinary 121 and 126). The *Historia Augusta* has two because it counts at Marcus' birth in 121. The report states the number as fact for the man who raised him after 124.
   Fix: "the boy was brought up by his paternal grandfather, consul for the third time in 126 and prefect of the city (1.2, 1.10)"
   Basis: https://en.wikipedia.org/wiki/Marcus_Annius_Verus_(grandfather_of_Marcus_Aurelius) (consul 97, 121, 126; urban prefect); *Marcus* 1.2 and 1.5 on LacusCurtius.

10. [minor] [figure] Section "Teachers: Fronto, Herodes and Rusticus" (tree figure).
    Current: "Marcus credits Diognetus with his wish for a plank bed and a skin (<em>Meditations</em> 1.6)."
    Problem: The tree files Diognetus under "Philosophy", but the text never calls him a philosophy teacher. Every name in a figure must sit in the text with the text's qualifiers (R-1). *Meditations* 1.6 does credit Diognetus with first acquainting Marcus with philosophy, so the fix goes in the text.
    Fix: "Marcus credits Diognetus, who first acquainted him with philosophy, with his wish for a plank bed and a skin (<em>Meditations</em> 1.6)."
    Basis: *Meditations* 1.6 (philosophy, then Bacchius, Tandasis and Marcianus; dialogues in boyhood; the plank bed and skin), from my own reading.

11. [minor] [lane] Section "Sources for the life".
    Current: "this module uses two entries, 1.7 and 1.16, for the life"
    Problem: The report also uses 1.6 (Diognetus) and 1.17 (brother, wife), so the self-description undercounts. Module 13.8 repeats the 1.6 plank-bed detail in one clause, which is acceptable at that length.
    Fix: "this module uses two entries, 1.7 and 1.16, for the life, and single details from 1.6 and 1.17"
    Basis: the report itself; `rome/r-13.8.html`, section "Book 1: a catalogue of debts".

12. [minor] [register] Section "177: Commodus Augustus and the martyrs of Lyon" (dispute box).
    Current: "Against both readings, the churches' letter in Eusebius shows Caesar, consulted directly, confirming death for the name (5.1.47).</aside>"
    Problem: The box runs to five sentences against the two-to-four standard. Its last sentence repeats the paragraph before it, which already gives the reply at 5.1.47.
    Fix: "</aside>" (delete the sentence)
    Basis: the report itself; register standard in BRIEF.md.

## Confirmed
- Born at Rome on the Caelian, 26 April 121, in his grandfather's second consulship (*Marcus* 1.5); Succuba (1.4); father died while praetor (1.2); Domitia Lucilla, daughter of Calvisius Tullus, and the aunt Galeria Faustina (1.3); Catilius Severus, then Annius Verus after the toga of manhood (1.9–10): LacusCurtius, *Marcus* part 1.
- Ucubi (Espejo) in Baetica as the family seat: Wikipedia, Marcus Annius Verus (grandfather).
- Verissimus, knights at six (4.1); Salian priest in his eighth year (4.2); cloak at twelve and couch with skins (2.6); Sextus as Plutarch's nephew (3.2); Rusticus' kiss, second consulship and statues (3.3–5): LacusCurtius.
- HA makes him eighteen at the adoption (5.1: "but eighteen years of age"; also 5.6, "in his eighteenth year"); ivory-shoulders dream (5.2); betrothal to Ceionius' daughter broken off (4.5, 6.2); tribunician power after the birth of a daughter (6.6): LacusCurtius.
- Lucius made equal Augustus (7.5); Brundisium and the return to Rome over the glory of the war (9.4–5); Lucius' death by stroke on the journey (14.8): LacusCurtius.
- *Marcus* 17.4–5 (auction), 19.1–9 (Caieta, the Chaldaean blood, the dowry reply), 23.7 (cleared her in his letters), 24.4 (thunderbolt and rain), 24.6 ("some say", Faustina), 24.9 (Cassius a public enemy), 25.3 (head buried), 25.6 (no senator killed), 26.4 (Halala in the Taurus foothills), 26.9 (colony and temple), 27.1 (Eleusis), 27.5 (tribunician power), 28.3–6 (refusing food; the plague; "if he proves worthy"), 28.10 (wished Commodus dead): LacusCurtius, *Marcus* part 2.
- *Commodus* 1.2 (Lanuvium, the day before the Kalends of September, with his twin Antoninus) and 12.4–5 (hailed imperator; triumph on 23 December in the year of Pollio and Aper, 176): LacusCurtius, *Commodus*.
- Dio 71.1.2 (Sextus the Boeotian, heard as emperor) and 71.1.3 (Lucilla married to Lucius), Loeb and Boissevain alike: LacusCurtius Book 71.
- Rain miracle at Boissevain 71.8–10 (Loeb 72), with Harnuphis invoking Mercury/Hermes and Xiphilinus' Christian insertion at 71.9: Livius, "Cassius Dio on the Rain Miracle".
- Dio citation form: Loeb 72 with Boissevain 71 in brackets, Loeb and Boissevain 71 unbracketed for chapters 1–2. This matches AGENT-SPEC.md and module 7.3 (72(71).33 for the death).
- Kovács, *Marcus Aurelius' Rain Miracle and the Marcomannic Wars* (2009): 171 against the literary 174; "a strong case that no coins of Marcus Aurelius can be linked to the miracle"; reviewer Andy Fear, BMCR 2009.09.15, "given Kovács's premises this is an eminently reasonable position": https://bmcr.brynmawr.edu/?p=26514.
- Fronto suffect consul 142; death perhaps 166–167; Mai's Ambrosian palimpsest of 1815, from Bobbio, overwritten with the acts of Chalcedon; the Vatican leaves published 1823: Wikipedia, Marcus Cornelius Fronto.
- Fronto, *Ad M. Caesarem* 4.13, Marcus at twenty-five reading Aristo; Champlin, "The Chronology of Fronto", JRS 64 (1974); Görgemanns in *Rheinisches Museum* 134; Hadot 1983–84: Görgemanns' article and n. 3 (URL above).
- Keresztes, "Marcus Aurelius a Persecutor?", *Harvard Theological Review* 61 (1968), 321–341; the abstract cites Justin, Melito and Athenagoras as showing no belief that Marcus persecuted, and Tertullian calling him a protector: https://www.cambridge.org/core/journals/harvard-theological-review/article/abs/marcus-aurelius-a-persecutor/E8F76CB327530CF310251FDFCC1ADDF2.
- Oliver and Palmer, "Minutes of an Act of the Roman Senate", *Hesperia* 24.4 (1955), 320–349 (ASCSA listing). The senate's ruling of 176 that allowed condemned criminals as cheap gladiators, and the scholars who linked it to Lyon, with "no firm evidence": Judaism and Rome record 1248. The *trinqui* and the Gallic priests were not checked against the article.
- Eusebius' two dates, 177 (*Church History*) and 166–167 (*Chronicle*): Judaism and Rome record 1248.
- Gibbon, *Decline and Fall*, chapter 4: "It has been objected to Marcus, that he sacrificed the happiness of millions to a fond partiality for a worthless boy". He gives it as an objection, as the report says: Standard Ebooks, chapter 4.
- Pointers checked against their targets: module 7.3 (adoptions of 138 via *Hadrian* 24.1; the HA's Marcus "mostly sober", Avidius Cassius "padded with invention and forged letters"; Vindobona or Sirmium; the column and module 10.3; first emperor with a son); Greek module 7.4 (Herodes, trial at Sirmium 174; chairs of 176; Eleusis 176); module 13.3 (reads the chairs of 176); module 13.4 (Arulenus Rusticus killed by Domitian, 93); module 13.6 (Epictetus' teaching; hands 1.7 to 13.7); module 13.8 (weighs the debt; Mill and the Victorian argument over Lyon, "which module 13.7 tells"); module 10.4 (the Lateran horseman taken for Constantine); module 10.3 (column of Marcus); module 2.5 (Trajan's rule to Pliny, sacrifice pardons).
- Seams: no dispute box, anecdote or Self-test question is told in both 13.7 and 13.6 or 13.8, apart from the one-clause 1.6 plank bed (finding 11). The place notes ("among the Quadi on the Granua", "at Carnuntum") are left to 13.8, and the chairs at Athens get one sentence pointing to Greek 7.4 and 13.3.
- From my own reading, not searched: Eusebius, *Church History* 5 preface 1 and 5.1.9–62 (Vettius Epagathus, Pothinus, Sanctus, Biblis, Attalus, 5.1.47, Alexander, Blandina and Ponticus, the Rhône); 5.5.1–6 (Apollinaris, Tertullian); 4.26.5–6 (Melito); Tertullian, *Apology* 5; Claudian, *Sixth Consulship of Honorius* (inclines to Marcus' virtue); *Meditations* 1.7, 1.16, 1.17 and 11.3; Galen, *On Prognosis* (excused in 168); Dio 72(71).22–36 as cited apart from finding 8; Justin, *First Apology* 1; *Acts of Justin*; the equestrian statue moved by Paul III in 1538.
- House style: no em dashes; British spelling; *Church History*; modules referred to by number in the house form.
