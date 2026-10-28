# Rome 13.2: Stoicism made Roman

Verdict: fix
Body words: 2837 (target 2500); with all fixes below applied, tested on a scratch copy: 2840 (band 2250 to 2875)

## Coverage
- Point back to Greek module 7.2 (system outline) and Greek module 12.7 (Zeno to Chrysippus), without restating: covered (opening paragraph; later pointers for oikeiosis, evil, compatibilism, archer, Posidonius)
- Preferred and dispreferred indifferents as the space of a public career: covered
- Hierocles' circles as a Roman-era statement of oikeiosis: covered
- The passions and their therapy: covered (Tusculan Disputations 3–4, On Anger 2.1–4)
- Providence and the good man's suffering (On Providence): covered
- Seneca's two commonwealths (On Leisure 4.1) as the Roman cosmic city: covered
- Fate and responsibility (On Fate, Gellius 7.2, Letters 107.11), compatibilism left to Greek 12.7: covered
- Panaetius' four personae and On Duties as an ethic of role and office: covered
- The sage, the person making progress, the Stoic paradoxes: covered
- Critics: Pro Murena 61–66 and Horace, Satires 1.3 and 2.3: covered
- Hand-offs from Greek 12.7 (Seneca's Latin of Cleanthes, Hierocles' circles, the four personae): all three delivered, and 12.7's wording of each hand-off ("belongs to Rome module 13.2", "are Rome module 13.2's") matches
- Hand-off from 13.1 (On Proper Functions as model of On Duties, and the four personae): delivered
- What deep dive module 12.6's prompt expects (the Stoic doctrines for reading the Aeneid: fate, providence, the passions): delivered, with a pointer back to 12.6

## Findings
1. [error] [accuracy] Section "Fate and responsibility in Latin".
   Current: "The physiognomist Zopyrus read in Socrates' face a dull man given to women; Socrates owned these natural vices and said reason had overcome them (10–11)."
   Problem: In On Fate 10 Socrates says nothing. Alcibiades laughs at the charge, and in 11 Cicero comments that natural vices can be uprooted by will, study and discipline. Socrates' own reply, that the vices were born in him but cast out by reason, is in Tusculan Disputations 4.80, not On Fate. Self-test 8's answer repeats the slip.
   Fix: "The physiognomist Zopyrus read in Socrates' face a dull man given to women; will, study and discipline, Cicero answers, uproot such natural vices (10–11)."
   And in Self-test 8, current: "Socrates overcame by reason the vices Zopyrus read in his face (10–11)." Fix: "will, study and discipline, not nature, uproot vices such as those Zopyrus read in Socrates' face (10–11)."
   Basis: Latin of On Fate 10 at https://www.studentville.it/appunti/paragrafo-10-7/ (Socrates does not speak; "in quo Alcibiades cachinnum dicitur sustulisse"); On Fate 11 "non est id positum in naturalibus causis, sed in voluntate, studio, disciplina"; Tusculan Disputations 4.80 "ab ipso autem Socrate sublevatus, cum illa sibi insita, sed ratione a se deiecta diceret". Smith's Dictionary, "Zopyrus" 4 (https://cts.perseids.org/read/pdlrefwk/viaf88890045/003/perseus-eng1/Z.zopyrus_4), which cites both passages together, is the likely source of the blend.

2. [minor] [style] Section "Providence and the two commonwealths", the dispute box.
   Current: "Seneca makes the charge a defence:"
   Problem: Set after Plutarch, the present tense makes Seneca (On Leisure, about AD 62) look as if he answers Plutarch (about AD 100). The charge is older than both, but the box should not invert the dates of the sources.
   Fix: "Seneca had already made the charge a defence:"
   Basis: AGENT-SPEC, Rome course: keep the date of the event and the date of the source apart. Seneca's text (On Leisure 6.4: "Nos certe sumus qui dicimus et Zenonem et Chrysippum maiora egisse quam si duxissent exercitus, gessissent honores, leges tulissent") checked at https://campus.hubscuola.it/content/uploads/2019/08/c4_lat_seneca7.pdf.

3. [minor] [accuracy] Section "Fate and responsibility in Latin".
   Current: "Tacitus gives the Stoic view as a senator heard it:"
   Problem: Tacitus names no school. Annals 6.22 gives the view to "alii" ("fatum quidem congruere rebus putant, sed non e vagis stellis..."), and the label "Stoic" is the modern reading. Its choice of a life after which the order is fixed has a Platonic ring (Republic 617e), which is why it is usually called Stoic, not proved so. "As a senator heard it" is also unclear: Tacitus says only "mihi haec ac talia audienti".
   Fix: "Tacitus reports an unnamed school's view, usually read as Stoic:" (word-neutral)
   Basis: Tacitus, Annals 6.22 (text as I know it, not reopened online).

4. [minor] [style] Section "Fate and responsibility in Latin".
   Current: "Module 12.6 asks how far Virgil's fate is Stoic."
   Problem: 12.6 is in unit 12, "Deep dive II: the Aeneid" (roman-syllabus.html). AGENT-SPEC says to refer to deep dives as "deep dive module X.Y", as the report does for 13.1 and 13.3 to 13.8.
   Fix: "Deep dive module 12.6 asks how far Virgil's fate is Stoic."
   Basis: roman-syllabus.html, unit 12 heading; AGENT-SPEC, Rome course.

5. [minor] [accuracy] Section "Panaetius' four personae: an ethic of role".
   Current: "and the study of causes and of character (95.65)"
   Problem: Letters 95.65 gives Posidonius' persuasion, consolation, exhortation and the inquiry into causes (aetiologia). His "ethologia", the description of each virtue, is in 95.66.
   Fix: "and the study of causes and of character (95.65–66)"
   Basis: Seneca, Letters 95.65–66 (text as I know it, not reopened online).

## Confirmed
- Letters to Atticus 16.11.4 (Atticus' query about the title, and "I have no doubt that καθῆκον corresponds with officium") and 16.14.3 (Atticus doubted the word in political matters: "Don't we say the officium of consuls, of the Senate, of generals?"): https://www.attalus.org/cicero/atticus16.html. This supports "the name of the duties of office". The sections could be added: 16.11.4, 16.14.3.
- Sorabji, Emotion and Peace of Mind (2000): Seneca concedes to Posidonius that the mind can be moved involuntarily but denies that this is yet an emotion. The box's "a concession to Posidonius that keeps them outside emotion" matches. BMCR review: https://bmcr.brynmawr.edu/?p=22418
- Inwood, "Seneca and Psychological Dualism" (1993; reprinted in Reading Seneca, 2005): Seneca is an orthodox monist who adds to Chrysippus' psychology without changing it, and widens it to responses below assent. NDPR https://ndpr.nd.edu/news/reading-seneca-stoic-philosophy-at-rome/ and BMCR 2007.06.45 https://bmcr.brynmawr.edu/?p=25714. The two positions differ enough for a dispute box.
- Gill 1988: title, Oxford Studies in Ancient Philosophy 6, 169–199 (https://tulliana.eu/bibliografia/personhood-and-personality-the-four-personae-theory-in-cicero-de-officiis-i/?lang=en). Roller, "Selfhood, Exemplarity, and Cicero's Four Personae", cites Gill 1988: 173–75 among attempts to reconstruct the Panaetian structure (https://classics.jhu.edu/wp-content/uploads/sites/20/2024/07/Selfhood-Exemplarity-Cicero.pdf), so "reconstructs its Panaetian form" stands. Gill's main thesis is the personhood/personality distinction, which the sentence does not need.
- Nussbaum, "Patriotism and Cosmopolitanism", Boston Review, October 1994: the concentric circles image and the case for cosmopolitan education. Walzer's reply in the same forum ("Spheres of Affection", 1 October 1994) discusses her circles and "draw the outermost circle in": https://www.bostonreview.net/?p=176413
- Gellius 9.5.8, Hierocles "vir sanctus et gravis": https://en.wikipedia.org/wiki/Hierocles_(Stoic). The papyrus was found 1901 and published 1906 (von Arnim and Schubart, Berliner Klassikertexte 4). Stobaeus 4.27.23 (Hense 4.671–673) = LS 57G, and the order of the circles and "call cousins brothers" as given.
- Plutarch, On Stoic Self-Contradictions ch. 2 (1033b–c): Zeno, Cleanthes and Chrysippus wrote on politics, held no office and lived abroad at leisure. Checked: https://cts.perseids.org/read/greekLit/tlg0007/tlg136/perseus-eng2/2
- Seneca, On Leisure 6.4 (Zeno and Chrysippus did more than if they had led armies, held office or passed laws, for the whole human race): checked at the hubscuola PDF above.
- On Fate 7–8 (thin air of Athens; Pompey's portico or the Campus), 23–25 (Carneades: voluntary motion needs no external cause, swerve unnecessary), 1–2 (Hirtius, Puteoli, 44). Also Gellius 7.2.1–3 (definition, On Providence book 4), 7.2.15 (Cicero's lost "Chrysippus aestuans laboransque ... intricatur"). From the text, not reopened online.
- Tusculan Disputations 3.6 (medicine of the mind); 3.7 for perturbationes over morbi (4.10 repeats the choice; 3.7 is right); 3.76 (Cleanthes, Peripatetics, Epicurus, Chrysippus; Cicero's own Consolation); 3.77 (Cleanthes consoles the wise man); 4.11–14 (four passions, three constantiae, none for distress). From the text.
- On Ends 3.16 (conciliari, commendari), 3.22 (archer), 3.48 (drowning, puppies), 3.51–52 (court analogy; producta, praeposita, reiecta), 3.57 (Chrysippus and Diogenes on repute; successors against Carneades), 3.75 (Tarquinius, Sulla, Crassus), 4.74 (apud imperitos ... coronae datum). From the text.
- On Duties 1.8 (medium and perfect officium; rectum = katorthōma), 1.46, 1.53–58 (degrees, then patria and parents first), 1.107, 1.108, 1.110, 1.112 (Cato at Utica), 1.113 (Ulysses and Ajax), 1.114, 1.115, 1.117–118, 1.124, 3.13–16 (Decii, Scipios, likeness of wisdom). From the text.
- On the Laws 2.5 (two patriae, the civitas first in caritas). From the text.
- Seneca: On Providence 1.1, 2.1, 2.6, 2.9–12, ch. 3 examples, 4.6, 4.7, 6.7; On Leisure 3.2, 4.1, 8; On the Happy Life 17.3, 26.1; On Anger 1.9, 1.17 (Aristotle), 2.4.1 (three movements); Letters 42.1, 75 (three classes), 94.1–2, 95.52–53, 107.11 (five lines, last "Ducunt volentem fata, nolentem trahunt"), 116.5. From the text.
- Epictetus, Handbook 53: four lines, ending with the unwilling bad man following all the same. Gellius 19.1 (the fifth book of Epictetus, now lost); Augustine, City of God 9.4. Hippolytus, Refutation 1.21 = SVF 2.975 (dog and cart, Zeno and Chrysippus). From the text.
- Pro Murena 61 (paradoxes, cock and father), 62, 63–64; Plutarch, Cato Minor 21 (the comic consul). From the text.
- Horace, Satires 1.3.96–98 and 124–139; Satires 2.3 (Damasippus, Stertinius, Saturnalia; line 326 is the last); Epistles 1.1.106–108. Stoic Paradoxes, prooemium 4, six paradoxes, 46 BC, to Brutus. From the text.
- Pointers checked against targets: Greek 7.2 (Stoicism section: cylinder at On Fate 42–43, preferred indifferents, passions as false judgements, city of gods and men); Greek 12.7 (school Zeno to Chrysippus; oikeiosis; evil from opposites and by-products; compatibilism; archer at On Ends 3.22; Posidonius' irrational powers; On Ends 4 charge against Zeno; evidence for On Proper Functions as model, Letters to Atticus 16.11.4); 13.1 (house philosophers, Panaetius and Posidonius; no duplicated anecdote, dispute or Self-test question); 10.2 (Persius, Stoic in doctrine); 13.3 (New Academy, Cicero the sceptic); 13.4 (Seneca's Cato; Stoic opposition); 13.5 (wealth and On the Happy Life; withdrawal in 62; On Anger 3.36); 13.6 (Epictetus, roles); 13.8 (cosmic city); 13.6 and 13.8 for Epictetus and Marcus in Greek.
- 13.1/13.2 seam: Panaetius' life and Roman pupils stay in 13.1, his personae and Letters 116.5 in 13.2. Posidonius at Rhodes stays in 13.1, his passions and Letters 95.65 in 13.2. Cicero's coinages stay in module 5.6 (qualitas, moralis, beatitudo), and 13.2's table of Stoic renderings does not repeat them. Neither report repeats the other's dispute boxes or Self-test questions, and the pointers between them are true in both directions.
- House style: no em dashes; British spelling (check.py clean); Cicero's treatises in English and Pro Murena in Latin; Cato Minor; Seneca's dialogues in English; five dispute boxes of three or four sentences, with sources or scholars named on each side.

## Errors noticed in other reports
- None found in the parts of Greek 7.2, Greek 12.7 and Rome 13.1 read for this check.
