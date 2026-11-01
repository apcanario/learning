# Rome 12.6: The gods of the Aeneid

Verdict: fix
Body words: 3724 (target 2500; the target is a guide, rule of 27 October 2026, no cut asked)

## Coverage
- Juno's anger and its causes: covered
- Jupiter's prophecy in book 1 (module 6.3 reads it; a sentence): covered (a short paragraph that keeps to the two points this module needs, pointing to 6.3)
- The reconciliation in book 12: covered (its terms and meaning; the event handed to module 12.3)
- Venus as mother: covered
- Neptune, Apollo, Allecto, Iris and Mercury: covered (table plus paragraph)
- Fate and the limits of Jupiter: covered
- Pietas against furor, and Aeneas' pietas under test: covered
- Stoic and Epicurean readings, pointing to deep dive 13.2, Greek 12.7, module 5.6 and Greek 12.6: covered (pointers present; see findings 2, 3 and 7 on their wording)
- Virgil's gods compared with Homer's, pointing back to Greek 10.9: covered
- Roman religion inside the poem: Penates covered; the Sibyl covered; the Ara Maxima with module 1.3 covered; Apollo at Actium with module 5.5 covered
- Lane note 2.2 (Ennius reconciled Juno in the Hannibalic war, Servius on 1.281): kept, in the reconciliation dispute box and Self-test 4, without retelling 2.2's cult titles (pointed to instead)

## Findings
1. [error] [pointer] Section "Fate and the limits of Jupiter".
   Current: "The Stoic answer would make fate and Zeus one: the chain of causes and the divine reason, as Greek module 12.7 sets out from Chrysippus."
   Problem: Greek 12.7 gives fate as the chain of causes (section "Chrysippus: pneuma, mixture, fate and the conflagration") and god as the active principle, reason, but never says the school identified fate with Zeus. The pointer credits 12.7 with the very identification the paragraph turns on.
   Fix: "The Stoic answer would make fate and Zeus one: Greek module 12.7 sets out Chrysippus' fate as the chain of causes and god as the active reason in matter, and Diogenes Laertius gives the school's formula that god, mind, fate and Zeus are one (7.135)."
   Basis: `greece/r-12.7.html` (fate as chain of causes, Cicero, *On Divination* 1.125–127; two principles, DL 7.134; no identification of fate with Zeus); Diogenes Laertius 7.135 (*hen t' einai theon kai noun kai heimarmenēn kai Dia*); Casali, BMCR 2024.10.47 ("orthodox Stoicism identifies heimarmene with Zeus") (https://bmcr.brynmawr.edu/?p=84497). Add DL 7.135 to `bibliography/rome/r-12.6.md`.

2. [should-fix] [accuracy] Section "Fate and the limits of Jupiter".
   Current: "The <em>Aeneid</em> has passages that read that way (10.112–113) and passages that do not (8.398, 4.696)."
   Problem: 10.112–113, *rex Iuppiter omnibus idem. fata viam invenient*, has Jupiter stand aside and leave the way to the fates: it separates the two, and is the report's own example of Jupiter's neutrality two sections earlier. It is a poor witness for fate as Jupiter's will. The passages that read that way are Dido's *fata Iovis* (4.614, already cited in the section) and Helenus' *sic fata deum rex / sortitur* (3.375–376), which Casali cites against Zanker.
   Fix: "The <em>Aeneid</em> has passages that read that way (Dido's <em>fata Iovis</em>, 4.614; the king of the gods allotting the fates, 3.375–376) and passages that do not (8.398, 4.696)."
   Basis: Casali, BMCR 2024.10.47: "some passages, such as Aeneid 3.375-6, link fate to Jupiter's will" (https://bmcr.brynmawr.edu/?p=84497); *Aeneid* 10.111–113, 4.614. Add 3.375–376 to the bibliography.

3. [should-fix] [pointer] Section "Fate and the limits of Jupiter".
   Current: "Rome module 13.2 ends by asking how far Virgil's fate is Stoic."
   Problem: Deep dive 13.2 does not end on the question, and does not ask it: in the middle of the report, at the close of its section "Fate and responsibility in Latin", it says "Deep dive module 12.6 asks how far Virgil's fate is Stoic", handing the question here. Also the house form for a deep dive in the Rome course is "deep dive module 13.2", as the prompt has it.
   Fix: "Deep dive module 13.2 hands this module the question of how far Virgil's fate is Stoic."
   Basis: `rome/r-13.2.html`, section "Fate and responsibility in Latin" (its sixth of nine sections); `AGENT-SPEC.md`, Rome course ("to deep dives as 'deep dive module 11.7'").

4. [should-fix] [register] Section "The agents: Neptune, Apollo, Allecto, Iris and Mercury".
   Current: "Two of the agents in the table have no Homeric model."
   Problem: Only Allecto is then shown to lack one. The next sentence, on Apollo's words to Ascanius, gives no reason for Apollo to lack a Homeric model, and he plainly has one (the table itself retells his Homeric promise at 3.97–98); Neptune, Iris and Mercury are Homeric too.
   Fix: "One agent in the table has no Homeric model."
   Basis: the report's own table and paragraph.

5. [should-fix] [register] Self-test, question 1.
   Current: "What causes does the poem give for Juno's anger, and which of them is new with Virgil?" and, in the answer, "The Carthaginian cause is Virgil's; it turns a Homeric hatred into a forecast of the Punic wars."
   Problem: The report's own dispute box has Ennius put Juno's appeasement in the second Punic war (Servius on 1.281), which implies a Juno hostile to Rome through the Carthaginian wars before Virgil; Feeney (1984) discusses the Ennian Juno in just these terms. Calling the Carthaginian cause "Virgil's" contradicts the body's evidence.
   Fix: question: "What causes does the poem give for Juno's anger, and which of them is not in Homer?"; answer's last sentence: "The Carthaginian cause is not in Homer; it turns a Homeric hatred into a forecast of the Punic wars, a link Ennius' date for her appeasement, the second Punic war, already implies."
   Basis: the report's dispute box in "Jupiter: the prophecy, the council and the reconciliation"; Feeney, *CQ* 34 (1984) 179–194, abstract and notes on Cambridge Core (Buchheit and Büchner on Juno's enmity ending only in the Hannibalic war in Ennius) (https://www.cambridge.org/core/journals/classical-quarterly/article/abs/reconciliations-of-juno/DD23F6C2B5FCB1EB8EE7D64FFCA2AD47).

6. [should-fix] [figure] Flow figure after "Jupiter: the prophecy, the council and the reconciliation".
   Current: `{"label": "Reconciliation", "note": "12.791–842"}` and `{"label": "Scipio", "note": "Juno brought to Rome in the third war, Servius on 12.841"}` and, in the caption, "in the order the sections “Juno's anger and its causes” and “Jupiter: the prophecy, the council and the reconciliation” give it"
   Problem: (a) The range 12.791–842 is in the figure and caption but nowhere in the text, which cites 12.793, 12.819–828, 12.833, 12.834–840 and 12.841 (R-1: every number in a figure is in the text). (b) The Scipio step drops the text's qualifier: the text says whether the goddess was ever summoned to Rome "is uncertain". (c) The figure runs in order of events, not in the sections' order (the Servius 12.841 box sits in the first section, the Hannibal forecast in the second).
   Fix: (a) in the text, "The reconciliation of book 12 is told as an event by module 12.3" becomes "The reconciliation of book 12 (12.791–842) is told as an event by module 12.3"; (b) the Scipio note becomes "Servius on 12.841: Juno brought to Rome in the third war; whether she was is uncertain"; (c) the caption phrase becomes "from the sections “Juno's anger and its causes” and “Jupiter: the prophecy, the council and the reconciliation”, in the order of events".
   Basis: the report's text against its figure declaration; `BACKLOG.md`, "Figures: the text's own words" and "Figures: the caption".

7. [minor] [style] Sections "Stoic and Epicurean readings".
   Current: "and their Roman forms Rome module 13.2's"; "the figure Rome module 13.2 calls the Romans' characteristic reader"; "(<em>Letters</em> 107.11; Rome module 13.2)"
   Problem: Within the Rome course a deep dive is "deep dive module 13.2", the prompt's own wording; "Rome module" is the Greek course's form.
   Fix: "and their Roman forms deep dive module 13.2's"; "the figure deep dive module 13.2 calls the Romans' characteristic reader"; "(<em>Letters</em> 107.11; deep dive module 13.2)"
   Basis: `AGENT-SPEC.md`, Rome course; prompt 12.6.

8. [minor] [style] Section "Jupiter: the prophecy, the council and the reconciliation".
   Current: "Two words in it belong to this module."
   Problem: What follows are two passages (1.262 and 1.279–282), not two words.
   Fix: "Two passages in it belong to this module."
   Basis: the report's text.

9. [minor] [attribution] Section "Stoic and Epicurean readings", dispute box.
   Current: "and read the Helen episode of book 2, where Venus checks his rage, as its correction."
   Problem: "its" reads as the correction of the school's doctrine. The review the writer relied on says Fish takes the Helen episode as "the necessary corrective moment for transforming Aeneas' anger".
   Fix: "and read the Helen episode of book 2, where Venus checks his rage, as the corrective moment that transforms Aeneas' anger."
   Basis: BMCR 2005.04.64 (https://bmcr.brynmawr.edu/?p=24377); Fish's chapter is "Anger, Philodemus' Good King, and the Helen Episode of the *Aeneid*".

10. [minor] [lane] Section "Stoic and Epicurean readings".
    Current: "the wandering moon and the labours of the sun (1.740–746)."
    Problem: Module 12.1 already reads Iopas' song as Lucretius set inside the poem (section "The poem's models"), and 12.2 points to 12.1 for it. A pointer avoids a third unmarked reading.
    Fix: "the wandering moon and the labours of the sun (1.740–746; module 12.1)."
    Basis: `rome/r-12.1.html`, "The poem's models", Lucretius paragraph; `rome/r-12.2.html`, book 1.

11. [minor] [register] Two dispute boxes run to five sentences (quality bar: two to four).
    Current: "When did Juno make peace with Rome? Ennius, as Servius reports on 1.281, put it in the second Punic war:" and "The poem's gods are too passionate for Epicurus and too partisan for Chrysippus."
    Problem: The first box opens with a rhetorical question; the second closes on an unattributed verdict that belongs in the body, not in a box of named positions.
    Fix: "Ennius, as Servius reports on 1.281, put Juno's peace with Rome in the second Punic war:"; and delete "The poem's gods are too passionate for Epicurus and too partisan for Chrysippus." from the box (or move it to the end of the paragraph before the box).
    Basis: `BRIEF.md`, register; quality-bar boxes in `greece/r-2.1.html` etc.

12. [minor] [accuracy] Section "Stoic and Epicurean readings".
    Current: "and Lucretius, the poet Virgil read most closely after Homer, is module 5.6's."
    Problem: An unsourced ranking; Ennius has as good a claim (module 12.1 lists Homer, Apollonius, Ennius, Naevius and Lucretius as models without ranking them).
    Fix: "and Lucretius, whom Virgil read closely, is module 5.6's."
    Basis: `rome/r-12.1.html`, "The poem's models".

## Confirmed
- Casali, BMCR 2024.10.47: groups Heinze, Bailey (and Lyne) as identifying fate with Jupiter's will; Zanker separates Stoic world fate from Jupiter as its mouthpiece and occasional guardian; events "in suspension"; Chrysippean compatibilism; Casali holds Virgil inconsistent, Stoic fate not to be equated with Rome's destiny, Stoic psychology irrelevant to the characters (https://bmcr.brynmawr.edu/?p=84497). Heinze 1903 and Bailey 1935 titles and years right.
- Feeney 1991 (BMCR 1992.02.08): Juno's multiple natures "Tanit, Hera, physical allegory of aer, goddess of marriage"; Jupiter's perspective "unavailable as a neutral, dispassionate vantage-point" (https://bmcr.brynmawr.edu/?p=19807).
- Feeney, "The Reconciliations of Juno", *CQ* 34.1 (1984) 179–194: questions the conventional "definitive transformation of Juno" at 12.791–842; notes tie her enmity to Carthage and the Hannibalic war in Ennius (abstract and notes, Cambridge Core, URL in finding 5). "Hostility resumes in Roman history" not checked beyond the abstract and notes (full text fetch refused).
- *Vergil, Philodemus, and the Augustans* (University of Texas Press, 2004), eds David Armstrong, Jeffrey Fish, Patricia A. Johnston, Marilyn B. Skinner (https://www.ubcpress.ca/vergil-philodemus-and-the-augustans); Fish's argument on *On Anger* (anger allowed without pleasure in punishment) (BMCR 2005.04.64).
- Servius on 12.841, "sed constat bello Punico secundo exoratam Iunonem, tertio vero bello a Scipione sacris quibusdam etiam Romam esse translatam"; Macrobius, *Saturnalia* 3.9's Carthage formula addresses "si deus, si dea est" and names no Juno; the transfer doubted (Orbis Romanus article on Macrobius 3.9 and Juno Caelestis, https://cyberleninka.ru/article/n/macrobius-saturnalia-3-9-and-the-roman-cult-of-iuno-caelestis).
- Augustine, *City of God* 9.4 quotes *Aeneid* 4.449 on the unmoved mind in its discussion of the Stoic and Peripatetic passions (https://bkv.unifr.ch/works/cpl-313/versions/the-city-of-god/divisions/248).
- Bowra, "Aeneas and the Stoic Ideal", *Greece &amp; Rome* (1933): title and year (Cambridge Core listing); his thesis not checked beyond the title.
- Lane 2.2: `rome/r-2.2.html` gives Ennius' reconciliation in the Hannibalic war via Servius on 1.281 and points to deep dive 12.6; kept here. Module 2.2 also has Juno's cult titles and Caesar's Venus Genetrix (46), as pointed.
- Pointers true of their targets: module 6.3 (prophecy 1.257–296 and Horace, *Odes* 3.3 Juno forbidding Troy rebuilt); module 1.3 (Penates at Lavinium, consuls' sacrifice; Ara Maxima Greek rite bareheaded, Potitii and Pinarii; Aeneas carrying father and gods as pietas); module 5.5 (Actium on the shield, Actian Apollo 698–706); module 5.6 (Lucretius); Greek 12.6 (gods and swerve); Greek 10.9 (plan of Zeus, scales, Sarpedon, partisans, double motivation, Olympian comedy, allegorists); Greek 10.12 (Venus Genetrix); module 10.2 (Lucan without Olympians; Silius' Juno and Hannibal); module 12.2 (statesman simile 1.148–153); module 12.1 (Siro and Philodemus); unwritten 12.3, 12.4 and 12.7 against their prompts (reconciliation as an event of book 12; Dido; the ending at 12.950–952).
- Seneca, *Letters* 107.11 and Cleanthes' prayer as 13.2 gives them; 13.2's progressor as the reader Roman books address.
- No duplicated Self-test question or dispute box with 12.1 or 12.2; 12.2 explicitly hands Juno's motives and theology to 12.6.
- Lucretius 2.651 (*nec bene promeritis capitur neque tangitur ira*, end of 2.646–651); Cicero, *On the Nature of the Gods* 1.116 (Cotta, pietas as justice towards the gods) and 2.66 (Balbus, air consecrated as Juno, sister and wife of Jupiter); *Res Gestae* 34.2 (shield: virtus, clementia, iustitia, pietas); Suetonius, *Augustus* 31.1 (Sibylline Books in gilded cases under Palatine Apollo); Horace, *Odes* 3.3.30–33; Euripides, *Heracles* (Iris and Lyssa sent by Hera): from knowledge.
- *Aeneid* references checked from knowledge of the OCT and found right: 1.10, 1.11, 1.19–22, 1.26–28, 1.33, 1.37–49, 1.39, 1.65–75, 1.124–156, 1.229–253, 1.254, 1.262, 1.279–282, 1.294–296, 1.297–304, 1.314–405, 1.378, 1.407–408, 1.657–722, 1.740–746, 2.293–297, 2.314–317, 2.594–595, 2.602–603, 2.610–612, 2.717, 3.97–98, 3.147–171, 3.403–409, 3.435–440, 4.68–69, 4.90–128, 4.361, 4.379–380, 4.393, 4.449, 4.614, 4.696, 5.709–710, 5.803–811, 5.815, 6.69–74, 7.293–294, 7.312, 7.313–316, 7.323, 7.327, 7.620–622, 8.268–272, 8.398, 8.679, 8.704–706, 8.720, 9.641, 10.11–13, 10.18–95, 10.112–113, 10.467, 10.470–471, 10.517–520, 10.622–627, 12.134–160, 12.311–317, 12.411–424, 12.725–727, 12.793, 12.819–828, 12.829, 12.833, 12.840, 12.841, 12.843–886 (the Dirae born with Megaera, at Jupiter's throne), 12.946–949.
- Not checked: Servius on 1.47 reading Juno as air (searches returned no text of the note); the second figure (tree) checked against the text and found consistent.
- House style: British spelling, no em dashes, no preamble or closing filler.
