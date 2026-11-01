# Rome 11.7: The Ides of March

Verdict: fix
Body words: 4347 (target 2500; guide only, no cut asked)

## Coverage
- Honours of 45–44 and the kingship question: covered (points back to 5.4 for the honours list and the Lupercalia; adds the sitting, the oath, Cotta's rumour; modern dispute box)
- The conspirators (Brutus, Cassius, Decimus, Trebonius, Casca) and their motives: covered (5.4's hand-off kept)
- Omens, Calpurnia's dream, Spurinna's warning: covered
- The meeting in the hall of Pompey and the murder: covered
- Caesar's last words and the Greek "you too, child": covered
- Aftermath, amnesty, will: covered (amnesty, acts and 300 sesterces pointed to 5.5 in one sentence; two new details added)
- Antony's funeral speech: covered (5.5's hand-off kept: Suetonius, Appian, Plutarch, Dio and Cicero compared)
- Comparing Nicolaus, Plutarch, Suetonius, Appian and Dio: covered (opening table, matrix figure, comparisons throughout)
- Afterlife from Cicero's "feast of the Ides" to Shakespeare: covered (10.4's hand-off kept: play set against Plutarch in a table)
- Whether the murder could have restored the Republic: covered (structural question pointed to 11.8, correctly)

## Findings
1. [error] [accuracy] Section "The murder".
   Current: "Suetonius and Appian count twenty-three wounds (<em>Julius</em> 82.3; Appian 2.117), Nicolaus thirty-five (24), Plutarch and Dio only many;"
   Problem: Plutarch's *Caesar* 66 gives twenty-three wounds; only his *Brutus* 17 says "many blows". The same slip is in the matrix figure and Self-test 7 (findings 2 and 3).
   Fix: "Suetonius, Appian and Plutarch's <em>Caesar</em> count twenty-three wounds (<em>Julius</em> 82.3; Appian 2.117; <em>Caesar</em> 66), Nicolaus thirty-five (24); Plutarch's <em>Brutus</em> (17) and Dio (44.19) say only many;"
   Basis: Plutarch, *Caesar* 66, Perrin's translation via Perseids (https://cts.perseids.org/read/greekLit/tlg0007/tlg048/perseus-eng2/65.2-66.7): "received twenty-three"; *Brutus* 17 via Perseids: "many blows", no number.

2. [error] [figure] Section "The murder" (matrix figure).
   Current: "{"label": "Wounds", "cells": ["35", "many", "23", "23", "many"]}"
   Problem: Plutarch's cell is wrong for the same reason as finding 1. The caption already cites *Caesar* 66 and *Brutus* 17.
   Fix: "{"label": "Wounds", "cells": ["35", "23 (Caesar 66); many (Brutus 17)", "23", "23", "many"]}"
   Basis: as finding 1.

3. [error] [register] Section "Self-test", question 7.
   Current: "Twenty-three according to Suetonius (<em>Julius</em> 82.3) and Appian (2.117), thirty-five according to Nicolaus (24); Plutarch and Dio say only many."
   Problem: The answer repeats the error in finding 1. It must match the body once that is fixed.
   Fix: "Twenty-three according to Suetonius (<em>Julius</em> 82.3), Appian (2.117) and Plutarch's <em>Caesar</em> (66), thirty-five according to Nicolaus (24); Plutarch's <em>Brutus</em> (17) and Dio (44.19) say only many."
   Basis: as finding 1.

4. [error] [attribution] Section "The morning and the hall of Pompey".
   Current: "Appian says the conspirators weighed other places and chose the Senate because senators not in the plot would join once they saw the deed (2.114)."
   Problem: Suetonius is the one who reports that other places were weighed: the elections on the Campus Martius, the Sacred Way, the entrance to the theatre (*Julius* 80.4). Appian says only that they looked for a time and place and chose the Senate unanimously, for the reason given. The writer's unsure list flagged this.
   Fix: "Suetonius says they weighed attacking him at the elections on the Campus Martius, on the Sacred Way or at the entrance to the theatre before choosing the Senate (<em>Julius</em> 80.4); Appian says they chose the Senate because senators not in the plot would join once they saw the deed (2.114)."
   Basis: Suetonius, *Julius* 80.4, Rolfe via Lexundria (https://lexundria.com/suet_jul/80/r); Appian 2.111–115, White's translation via Perseids (https://cts.perseids.org/read/greekLit/tlg0551/tlg017/perseus-eng2/2.16.111-2.16.115): "They sought a time and place"; "they unanimously chose the Senate as the place", with no other places named. The page has no section numbers, so 2.114 is not pinned, but it falls in this range.

5. [should-fix] [accuracy] Section "The conspirators and their motives".
   Current: "<li><strong>Publius Servilius Casca</strong>, tribune of the plebs in 44, who struck first.</li>"
   Problem: On the Ides, Casca was tribune-elect. He took office in December 44 and is normally listed as tribune of 43.
   Fix: "<li><strong>Publius Servilius Casca</strong>, tribune-elect for 43, who struck first.</li>"
   Basis: Wikipedia, "Publius Servilius Casca" ("plebeian tribune in 43 BC"; "In December 44 BC, Casca assumed office"). The secondary source was checked; Broughton was not.

6. [should-fix] [lane] Section "Antony's funeral speech" (dispute box).
   Current: "The most theatrical version is the one Shakespeare's tradition did not use; Shakespeare took Plutarch's."
   Problem: This is stated as settled, but it is disputed. Aldo Setaioli argued that the Tudor English translation of Appian (by "W.B.", 1578) shaped both funeral speeches in the play, including Antony's theatrical touches. The Internet Shakespeare Editions list Appian as a possible source. The prompt asks for disagreements to be flagged.
   Fix: "Shakespeare built chiefly on Plutarch's, though Aldo Setaioli (\"Antony's speech in Shakespeare's <em>Julius Caesar</em> and the ancient sources\", <em>Prometheus</em>, 2017) argued that the Tudor English Appian (1578) shaped both funeral speeches."
   Basis: Setaioli, *Prometheus* 43 (2017), abstract at https://oaj.fupress.net/index.php/prometheus/article/view/1051; Internet Shakespeare Editions, sources of the tragedies (https://internetshakespeare.uvic.ca/Library/SLT/reference/sources/sourcetragedies.html): Appian, *Civil Wars*, trans. W.B., 1578, listed as a possible source.

7. [minor] [figure] Section "The murder" (matrix figure).
   Current: ""despairs, veils himself""
   Problem: The text never says that Appian's Caesar veils himself. It says only that "Appian makes the turning point a wound in the thigh from Brutus (2.117)". Under the figure lesson, every item in a figure must be in the text. (The detail itself is correct in Appian.)
   Fix: ""gives up after Brutus' thigh wound""
   Basis: Appian 2.117 via Perseids (https://cts.perseids.org/read/greekLit/tlg0551/tlg017/perseus-eng2/2.16.116-2.17.120); BACKLOG.md, figure lesson "the text's own words".

8. [minor] [figure] Section "The morning and the hall of Pompey" (flow figure caption).
   Current: "The morning of the Ides in the order this report tells it, from the sections"
   Problem: The report does not tell the morning in this order. Spurinna's exchange and Artemidorus' note come in "Omens and warnings", before Decimus fetches Caesar in the next section. The figure is a reconstruction drawn from several sources, and its caption should claim only that.
   Fix: "The morning of the Ides in the order of events the sources cited give, from the sections"
   Basis: the report, sections "Omens and warnings" and "The morning and the hall of Pompey"; BACKLOG.md, figure lesson "the caption".

9. [minor] [accuracy] Section "Afterlife: from the feast of the Ides to Shakespeare" (table).
   Current: "<td>Leaves Spurinna unnamed and the warning in five words.</td>"
   Problem: Plutarch's seer in *Caesar* 63 is already unnamed, so Shakespeare changes nothing here. The name Spurinna comes from Suetonius and Valerius Maximus.
   Fix: "<td>Keeps Plutarch's unnamed seer (Suetonius names him Spurinna) and puts the warning in five words.</td>"
   Basis: Plutarch, *Caesar* 63 ("a certain seer"), Perrin via Perseids; Suetonius, *Julius* 81.2.

10. [minor] [attribution] Section "The murder", sub-section "The last words".
   Current: "and Malone claimed it for Richard Edes's lost Latin play <em>Caesar Interfectus</em> (1582)"
   Problem: The sources disagree on whether Malone made this claim. The Lost Plays Database says Malone argued only for an earlier English Caesar play, and that the link between the tag and Edes appears in later school editions (1896, 1905). Wikipedia credits it to Malone. The play is dated about 1580–83, with 1582 the commonest date.
   Fix: "and it has been traced, without direct evidence, to Richard Edes's lost Latin play <em>Caesar Interfectus</em> (about 1582)"
   Basis: Lost Plays Database, "Caesar Interfectus" (https://lostplays.folger.edu/Caesar_Interfectus); Wikipedia, "Et tu, Brute?".

11. [minor] [attribution] Section "Could the murder have restored the Republic?" (dispute box).
   Current: "one reviewer, G. Matthew Adkins, objected that the Republic had been failing for some ninety years before the Ides."
   Problem: Adkins wrote "at least 90 years" and dated the decline from Tiberius Gracchus in 133. The view the box gives Strauss is Adkins's reading of him; it is accurate to the review, but the writer did not check it against the book.
   Fix: "one reviewer, G. Matthew Adkins, objected that the Republic had been in decline for at least ninety years before the Ides, since the killing of Tiberius Gracchus in 133."
   Basis: Adkins, *Washington Independent Review of Books*, 13 May 2015 (https://cpanel.washingtonindependentreviewofbooks.com/bookreview/the-death-of-caesar-the-story-of-historys-most-famous-assassination): "a somewhat greater focus on the military aspects of the conspiracy, including the role of Caesar's general Decimus"; a system "that should have survived, with only some reforms"; "in decline for at least 90 years".

## Confirmed
- Nicolaus (Hall's chapters, CSUN edition, https://www.csun.edu/~hcfll004/nicolaus.html): more than eighty conspirators and the list of motives (19); Licinius and Cassius with the diadem (21); Calpurnia's fears, "Brutus" as an intimate friend leading Caesar in (23–24); Cassius at the face, Decimus at the thigh, Marcus Brutus cut in the hand, thirty-five wounds (24); no last words; the body carried home by three slaves (26); Decimus' gladiators (26).
- Plutarch, *Caesar* 66: Brutus Albinus (Decimus) keeps Antony talking; Casca's first blow with the cries in Latin and Greek; Caesar covers his head on seeing Brutus' dagger; the divine power that led the deed to Pompey's statue (Perseids).
- Plutarch, *Brutus* 17: Trebonius keeps Antony at the door; Brutus wounded in the hand (Perseids). *Brutus* 20: seventy-five drachmas, sparing Antony as the first mistake, the eulogy and the robe, Cinna (Perseids).
- Plutarch, *Antony* 13: Trebonius sounded Antony on the way back from Spain, and Antony kept silent (Lexundria); Narbo comes from Cicero, *Philippics* 2.34 (Lexundria), which the report cites with it.
- Appian 2.116–120: the heartless victim; Popilius Laenas; Trebonius and Antony; Cimber; Casca; Cassius at the face, Brutus at the thigh, the veiled fall at Pompey's statue; twenty-three wounds; Lepidus' legion; the Capitol with gladiators; the analysis of the plebs (Perseids, White).
- Appian 2.143–147: Piso brings the body; decrees ("sacred and inviolable", "father of his country") and oaths; the robe on a spear; the Pacuvius line in Caesar's voice; the turning wax image with twenty-three wounds; the crowd burns "the senate-chamber where Caesar was slain" (Perseids).
- Dio 44.19: Trebonius detains Antony; "many wounds"; the truest account says he could say nothing, and some add "you too, child?" (Lexundria, Cary).
- Suetonius, *Julius* 80.3–4, 81.1–4, 82.1–3: Lucius Brutus' statue; more than sixty conspirators; Capys and Balbus; the horses; Spurinna's "not later than the Ides"; the bird; both dreams; Decimus; the unread note; "come but not gone"; "why, this is violence!"; the wound below the throat; the groan and the Greek words; twenty-three wounds and Antistius; three slaves (Livius and Lexundria).
- Cicero, *On Divination* 1.119 (heartless ox on the day of the golden throne and purple) and 2.36–37 (Marcus' reply), Falconer via LacusCurtius; this resolves the writer's unsure item.
- Cicero, *Letters to Atticus* 14.4: "Idus Martiae consolantur" (sententiaeantiquae, quoting the text).
- Horsfall, "The Ides of March: Some New Problems", *Greece & Rome* 21.2 (1974), 191–199: asks why the Ides and the Curia Pompei were chosen, and notes the sources' inconsistencies (Cambridge abstract).
- North, "Caesar at the Lupercalia", *JRS* 98 (2008), 144–160: the rite had no element of coronation (Cambridge abstract); the box's compression of his argument is fair.
- Sedley 1997 dates Cassius' Epicureanism to 48, when he stopped resisting Caesar, and doubts that it drove the murder (secondary summary, liquisearch; the Cambridge abstract page redirected and was not fetched).
- Russell 1980, pp. 123–128: *kai su* as an apotropaic formula against the evil eye, on mosaics and inscriptions; a curse; "lad" (Gwern PDF of the article). The editor and place (Marshall, *Vindex Humanitatis*, Armidale) were not confirmed from that PDF.
- Ziogas, *Antichthon* 50 (2016), 134–153: the funerary-epigram reading, "You too, son, will die"; Ziogas discusses *Galba* 4 as the only other *kai su, teknon* in Suetonius, and also Russell (Durham repository record and accepted manuscript).
- Monterroso and CSIC, October 2012: a structure three metres wide in the Curia of Pompey at Torre Argentina, read as Augustus' closure of the spot (ScienceDaily, 10 October 2012).
- Booth: Winter Garden, New York, 1864, a benefit for the Shakespeare statue in Central Park; John Wilkes as Antony, Edwin as Brutus, Junius as Cassius; the diary line "For doing what Brutus was honored for"; *sic semper tyrannis* (LitHub).
- *The True Tragedie of Richard Duke of Yorke* printed 1595 with "Et tu, Brute" (Wikipedia, "Et tu, Brute?").
- Morstein-Marx, *Julius Caesar and the Roman People* (Cambridge, 2021): title, publisher and year (Cambridge page).
- Pointers checked against their targets: 1.6 (Lucius Brutus); 5.4 (the honours, the Lupercalia box, the outline of the murder, the motives handed to 11.7); 5.5 (the amnesty, the acts, the will and 300 sesterces; the funeral versions handed to 11.7); 6.2 (Mars Ultor vowed at Philippi); 7.1 (Cremutius Cordus, 25); 10.4 (Dante's Brutus and Cassius in Lucifer's mouths; *Julius Caesar* among the Roman plays, its comparison with the sources left to 11.7); 11.3 (the Senate house burned at Clodius' funeral, 52); 11.4 (Servilia and the paternity rumour, which 11.4 calls generally rejected; Sempronia as Decimus' mother or stepmother); 11.8 prompt (Dio's view that monarchy was inevitable for an empire).
- No dispute box or self-test question repeats one in 5.4, 5.5 or 10.4: 5.4's Lupercalia box sets ancient versions against each other, 11.7's sets modern scholars; 11.7's Q2 leaves out the Lupercalia.
- House style: no em dashes; British spelling; citation conventions kept (*On Divination*, *On Duties*, *Letters to Friends*, *Philippics*).
- Not checked: Pelling 2011 as the place that weighs Pollio as the common source (plausible, not confirmed); Valerius Maximus 8.11.2; Plutarch, *Caesar* 63's citation of Livy (consistent with my knowledge, not fetched).
