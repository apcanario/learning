# Greece 12.8: Sceptics and Neoplatonists: the late schools to 529

Verdict: fix
Body words: 2822 (target 2500)

All body fixes below applied together give 2871 words (band 2250 to 2875, simulated with `check.py --target 2500`). The deletion in finding 7 is needed to stay inside the band.

## Coverage
- Pyrrho and Timon (DL 9.61–116, Aristocles in Eusebius): covered
- Academy's sceptical turn: Arcesilaus, Carneades, Clitomachus, Philo of Larissa: covered
- Antiochus of Ascalon's return to doctrine: covered (Roman following handed to Rome module 13.3)
- Aenesidemus and Sextus Empiricus, *Outlines* and the modes: covered (ten, five and eight modes)
- Middle Platonism in a paragraph (Plutarch and Alcinous): covered, with Numenius
- Plotinus, *Enneads* and Porphyry's *Life*, One, Intellect and Soul argued: One and Intellect covered; Soul thin (stated, not argued; finding 3)
- Porphyry, Iamblichus and theurgy; Proclus: covered
- Hypatia as a philosopher: covered (death pointed back to module 7.4)
- Justinian's measure of 529 and the argument over what it did: covered by a pointer to module 7.4's Cameron/Watts box plus the Alexandria evidence; the 529 box is not repeated
- Damascius, Simplicius and the Persian journey (Agathias 2.30–31): covered
- Hand-off from module 12.7 ("Carneades' charge of circularity is module 12.8's"): missing (finding 2)
- Hand-offs from 12.1 (Xenophanes B 34 via Sextus) and 12.3 (sceptical Academy; *Parmenides* read as Neoplatonist theology): kept

## Findings
1. [error] [attribution] Section "Arcesilaus and Carneades: the Academy turns".
   Current: "Zeno defined the cognitive impression as one that comes from what is, stamped exactly in accordance with it (Sextus, <em>Against the Mathematicians</em> 7.248); Cicero says he added"
   Problem: Sextus at M 7.248 gives the definition as the Stoics', not Zeno's, and gives all three clauses, including the "could not come from what is not" clause the next words say Zeno added later. Cicero, *Academica* 2.77, tells both stages (Zeno's first answer and the addition under Arcesilaus' questioning), so it is the right citation for the whole sentence.
   Fix: "Zeno defined the cognitive impression as one that comes from what is, stamped exactly in accordance with it; Cicero says he added"
   Basis: Sextus, M 7.248 (= LS 40E), Stoic three-clause definition; Cicero, *Academica* 2.77 (Zeno's "ex eo quod esset sicut esset impressum", then the added clause).

2. [should-fix] [lane] Section "Arcesilaus and Carneades: the Academy turns".
   Current: "(Cicero, <em>On Fate</em> 23)."
   Problem: Module 12.7 (Diogenes of Babylon and Antipater) ends "Carneades' charge of circularity is module 12.8's", but 12.8 never tells it, so 12.7's pointer lands on nothing. The source is Plutarch, who charges the Stoic end with circularity and reports that some aimed this at Antipater, driven to such formulas by Carneades; the fix keeps the reporter separate from the claim.
   Fix: add after "(Cicero, <em>On Fate</em> 23).": " Plutarch finds the Stoic end, reasoning well in selecting what accords with nature, circular: the things are worth selecting for the end, and the end is the selecting; Antipater, some said, fell into such formulas under Carneades' pressure (<em>On Common Conceptions</em> 1072e–f)."
   Basis: greece/r-12.7.html, section "Diogenes of Babylon and Antipater of Tarsus"; Plutarch, *On Common Conceptions* ch. 27 (ToposText, https://topostext.org/work/321, §27: Antipater "being pressed by Carneades, fell into these fooleries"; "much of Zeus's Corinth, that is, much reasoning in a circle"). Stephanus letters 1072e–f from memory (*SVF* 3 Antipater 59); the chapter is confirmed.

3. [should-fix] [register] Section "Middle Platonists and Plotinus".
   Current: "Soul orders the cosmos, and time is its life passing from one thing to the next (3.7.11); at the bottom is matter, privation and evil itself (1.8)."
   Problem: The prompt asks for One, Intellect and Soul "argued rather than listed". The One and Intellect are argued, but Soul is only stated. A clause on what Soul is relative to Intellect (its expressed word, thinking one thing after another) argues it and explains why time belongs to it. Also, "(1.8)" is a treatise; label it as the report does for 5.5 and 5.6.
   Fix: "Soul stands to Intellect as spoken word to thought (5.1.3) and thinks one thing after another, where Intellect is all things at once (5.1.4); so it orders the cosmos in succession, and time is its life passing from one thing to the next (3.7.11). At the bottom is matter, privation and evil itself (treatise 1.8)."
   Basis: Plotinus, *Enneads* 5.1.3 (soul as the logos of Intellect, as the spoken word is of the word in the soul); 5.1.4 (soul's objects come one after another, "now Socrates, now a horse"; Intellect is all things); 3.7.11. From knowledge of the text.

4. [should-fix] [register] Section "Self-test".
   Current: "<li>Why did Aenesidemus leave the Academy, and how is he dated?" and "<li>How does Sextus use Xenophanes B 34, and why does he still not count Xenophanes a sceptic?"
   Problem: Eight of ten questions test the sceptics. Nothing tests Middle Platonism, Proclus, Hypatia, 529 or the Persian journey, which make up about half the body. Q8 also tests material module 12.1 handed on rather than this module's core. Replace Q6 and Q8 (whole `<li>` in each case).
   Fix: Q6: "<li>What does Proclus' proposition 35 assert, and why does it make causation a circle rather than a chain?<details><summary>Answer</summary><p>Every effect remains in its cause, proceeds from it and reverts upon it (<em>Elements of Theology</em>, prop. 35). The product is never cut off from its source, and its return completes the movement its procession began.</p></details></li>" Q8: "<li>What does Alexandria show about the reach of Justinian's measure of 529?<details><summary>Answer</summary><p>Malalas' decree went to Athens (<em>Chronicle</em> 18.47). At Alexandria Ammonius had come to terms with the bishop, Philoponus published <em>Against Proclus</em> in 529, and the pagan Olympiodorus still lectured on Plato and Aristotle after 565, so the measure struck Athens and left Alexandria teaching.</p></details></li>"
   Basis: the report's own body (Proclus paragraph; section "529, Damascius and the road to Persia"; Carry forward 3).

5. [should-fix] [lane] Section "Carry forward".
   Current: "<li>Plato's unresolved dialogues produced two readings: inquiry left open, which the Academy from Arcesilaus to Philo practised, and a system withheld, which the Neoplatonists built from the <em>Parmenides</em> and <em>Timaeus</em>. Every later Platonism takes one side.</li>"
   Problem: This repeats module 12.3's Carry forward 2 almost word for word ("a system withheld, as the Tübingen school and the Neoplatonists read it, or inquiry left open, as the sceptical Academy did (module 12.8)"). That leaves this module two carry-forward ideas of its own. The soul-descent question is this module's own transferable idea, and no carry-forward item holds it.
   Fix: "<li>Whether the soul can rise by thought alone, as Plotinus' undescended soul allows (<em>Enneads</em> 4.8.8), or fell entire and needs rites given from above (Iamblichus; Proclus, <em>Elements of Theology</em>, prop. 211), is the late form of the question of philosophy's relation to religion; Iamblichus' answer made the last pagan schools communities of cult as well as of study.</li>"
   Basis: greece/r-12.3.html, Carry forward 2; the report's dispute box on the soul's descent and its Marinus sentence.

6. [minor] [pointer] Section "Pyrrho and Timon".
   Current: "Module 7.2 gives Pyrrho's journey with Alexander and Timon's three-question summary."
   Problem: Module 7.2 gives Timon's summary (indifferent, unmeasurable, undecidable; speechlessness, then freedom from disturbance) but does not frame it as three questions, and 12.8 never states the three questions either, so the reader cannot tell what "three-question" refers to.
   Fix: "Module 7.2 gives Pyrrho's journey with Alexander and Timon's summary."
   Basis: greece/r-7.2.html, section "Scepticism and the Cynics".

7. [minor] [register] Section "Pyrrho and Timon" (dispute box).
   Current: " Sextus claims only that Pyrrho appears to have applied himself to scepticism more fully than his predecessors (<em>Outlines of Pyrrhonism</em> 1.7).</aside>"
   Problem: The box runs to five sentences across two disputes, above the house limit of four. Deleting the last sentence brings it to four and offsets the words added by findings 2 and 3. Because this is the only place the full title appears, give the full title at the next citation.
   Fix: replace with "</aside>"; and in the Academy box change "a Platonist testing his pupils (<em>Outlines</em> 1.232–234)" to "a Platonist testing his pupils (<em>Outlines of Pyrrhonism</em> 1.232–234)".
   Basis: BRIEF.md register (dispute boxes of two to four sentences).

8. [minor] [register] Section "Porphyry, Iamblichus and Proclus" (dispute box).
   Current: "The stakes are practical. If the higher soul"
   Problem: Five sentences; merging two keeps the words and meets the four-sentence limit.
   Fix: "The stakes are practical: if the higher soul"
   Basis: BRIEF.md register.

9. [minor] [attribution] Section "Pyrrho and Timon".
   Current: "his <em>Silloi</em> mock every dogmatist except Pyrrho (9.65)."
   Problem: DL 9.65 quotes Timon's praise of Pyrrho. The description of the *Silloi* as lampoons on the dogmatists is at 9.111.
   Fix: "his <em>Silloi</em> mock every dogmatist except Pyrrho (9.65, 9.111)."
   Basis: Diogenes Laertius 9.65, 9.111; SEP "Timon of Phlius" (https://plato.stanford.edu/archives/sum2014/entries/timon-phlius/) cites 9.111 for the *Silloi*.

10. [minor] [accuracy] Section "Aenesidemus and Sextus Empiricus".
    Current: "Sextus quotes Xenophanes' fragment DK 21 B 34 as a denial"
    Problem: At M 7.49 Sextus gives the sceptical reading as "according to some", and at 7.110 he reports another reading on which Xenophanes removes only infallible knowledge and leaves opinion as criterion. The report presents one reading as Sextus' own.
    Fix: "Sextus quotes Xenophanes' fragment DK 21 B 34 as, on some readings, a denial"
    Basis: Sextus, M 7.49 ("Xenophanes, according to some ...") and 7.110; from knowledge of the text, not checked online.

## Confirmed
- Word count 2822, inside the band (check.py); no em dashes; no American spellings found.
- Pointers: module 7.2 (Arcesilaus' "reasonable", Carneades' persuasive impressions, Bett's metaphysical reading of Pyrrho), module 7.4 (Plotinus' hierarchy and Porphyry's edition; Porphyry's works; Dodds vs Shaw/Addey on theurgy; Hypatia's murder; Malalas, *CJ* 1.11.10 and the Cameron/Watts box; Plutarch as Platonist), module 12.1 (Simplicius preserves the Presocratics; Sextus M 7.49 on B 34), module 12.3 (*Parmenides* second part as Neoplatonist theology; Plutarch and Atticus read the *Timaeus* literally; sceptical Academy set against the Neoplatonists), Rome module 4.5 (155 embassy, Carneades on justice), Rome module 13.3 prompt (Antiochus' Old Academy followed by Varro and Brutus; Cicero the sceptic): all true of their targets.
- No dispute box from 7.2 or 7.4 is repeated. The 529 box stays in 7.4. The Pyrrho box points back to Bett in 7.2 and extends it with the textual crux; the soul-descent box points to 7.4 for the magic/theology quarrel.
- Carneades' attack is told here and the Stoa itself in 12.7, with no duplication beyond the one-sentence statement of the cognitive impression that both need.
- Academy box: Couissin 1929 and Striker 1980 dialectical; Frede 1979 ("Des Skeptikers Meinungen") and 1984, and Cooper 2004 ("Arcesilaus: Socratic and Sceptic"), hold that the residual views are believed without rational warrant: SEP "Arcesilaus" (https://plato.stanford.edu/ENTRIES/arcesilaus/).
- Aristocles in Eusebius: Timon's summary with "Aenesidemus says pleasure"; Aenesidemus' Outline "goes through the nine modes"; Aenesidemus "began just yesterday to stir up this nonsense again at Alexandria in Egypt" (Gifford's translation, https://tertullian.org/fathers/eusebius_pe_14_book14.htm). Section 14.18.29 for the revival and 14.18.11–13 for the modes match Bett (ed.), *Cambridge Companion to Ancient Scepticism*, excerpt (https://assets.cambridge.org/97805211/90251/excerpt/9780521190251_excerpt.pdf).
- Hypatia claims from Graziosi's review of Watts, "In Her Philosopher's Cloak", LRB 39.16 (https://lrb.co.uk/v39/n16/barbara-graziosi/in-her-philosophers-cloak): Watts "insists that she excluded theurgy from her teaching"; her teaching "appealed to both Christians and pagans"; Damascius' Isidore and Hypatia, "philosopher ... differs from a geometer"; Theon's heading "edition revised by my daughter Hypatia, the philosopher".
- Sextus: PH 1.7 (Pyrrho), 1.8 (definition), 1.13 (belief), 1.20 (honey), 1.23–24 (fourfold observances), 1.28–29 (Apelles), 1.164–169 (five modes), 1.180–186 (eight causal modes), 1.206 (purgatives), 1.232–234 (Arcesilaus), 1.235 (Philo); M 7.150–157 (Arcesilaus), 7.166–189 (Carneades' criterion, weightier matters at 7.184), 7.49–52 (gold in the dark at 7.52), 8.481 (ladder), 9.182–184 (sorites). The ten-mode table ranges (1.40–78 to 1.145–163) and examples (quails and hemlock 1.57, Demophon 1.82, apple 1.94, colonnade 1.118, goat's horn 1.129, comet 1.141) are right.
- Diogenes Laertius: 9.61, 9.62 (Antigonus vs Aenesidemus), 9.63, 9.64, 9.66, 9.79–88, 9.88 (Agrippa), 9.109–112, 9.116 (Sextus last but one); 4.28–45, 4.62, 4.67.
- Cicero: *Academica* 1.13, 1.15–42, 1.45, 1.46, 2.11–12 (*Sosus*), 2.28–29, 2.77, 2.78, 2.98–104, 2.132 ("germanissimus Stoicus"), 2.139; *Brutus* 306; *On Fate* 23. Plutarch, *Against Colotes* 1122a–d. Photius, *Bibliotheca* 212.
- Philo dispute: Tarrant, *Scepticism or Platonism?* (1985) and Brittain, *Philo of Larissa: The Last of the Academic Sceptics* (2001), with the views as stated. Sextus box: Burnyeat 1980, Frede 1979, Barnes 1982 (rustic/urbane), with the views as stated.
- Plotinus: *Life* 3 and 23; *Enneads* 5.1.8 (exegete, three Ones of the *Parmenides*), 6.9.1, 5.3.10–11, treatise 5.6, 5.4.1–2, 5.1.6, 5.3.11, treatise 5.5, 3.7.11, 4.8.8, 6.9.11; *Republic* 509b.
- Alcinous, *Handbook* 9–10; Clement, *Stromateis* 1.22 (Numenius); Augustine, *City of God* 10.9; *On the Mysteries* 2.11; Proclus, *Elements* props. 1, 7, 35, 211 and 211 propositions in all; Marinus' Oracles-and-*Timaeus* wish (*Life of Proclus* 38).
- Malalas 18.47 (consulship of Decius, philosophy and law); Philoponus' *Against Proclus* of 529; Olympiodorus after 565; Damascius' opening dilemma in the *Problems and Solutions*; Agathias 2.30–31 (seven names, philosopher-king, clause of 532), Uranius; Priscian's *Solutions* (soul, sleep, tides); Paul the Persian's logic dedicated to Khusro.
- Dates: Arcesilaus c. 316–241; Carneades 214/13–129/8; Philo 159/8–84/3, head 110/09; Timon c. 320–230 (SEP); Plotinus 204/5–270; Proclus 412–485.
