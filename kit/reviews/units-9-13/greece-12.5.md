# Greece 12.5: Cynics, Cyrenaics and the other Socratic schools

Verdict: fix
Body words: 2716 (target 2500)

## Coverage
- Antisthenes: covered (Xenophon's Symposium, DL 6.2 and 6.10–11, Aristotle's logical testimonia; adds to the founder dispute without restating 6.5's and 7.2's boxes)
- Diogenes of Sinope, the anecdote tradition (DL book 6), what can be known: covered
- Crates and Hipparchia: covered
- Menippus and Cynic writing: covered (with Bion, Teles, Cercidas, Onesicritus)
- Aristippus and the Cyrenaics on pleasure: covered
- Later Cyrenaics (Hegesias, Anniceris, Theodorus): covered
- Megarians and dialectic (Euclides, Eubulides' paradoxes, Diodorus and the Master Argument, Stilpo): covered; Euclides left to module 6.5 by pointer
- Diogenes Laertius as a source and his limits: covered (first section; lateness stated)
- The Cynic as social critic, and the road to Zeno handed to module 12.7: covered
- Lane: 6.5's material (jar, lamp, Laïs, Liar and Heap, Dudley) and 7.2's box are kept to pointers; 12.2's Antisthenes, Euclides and Aeschines material is not repeated (Aeschines is not mentioned at all)

## Findings
1. [error] [attribution] Section "Diogenes of Sinope: what can be known".
   Current: "while Sosicrates and Satyrus said he wrote nothing and gave the tragedies to his follower Philiscus (6.80)"
   Problem: Both said he left nothing in writing, but only Satyrus gives the tragedies to Philiscus. The sentence makes Sosicrates say it too.
   Fix: "while Sosicrates and Satyrus said he wrote nothing, and Satyrus gave the tragedies to his follower Philiscus (6.80)"
   Basis: Diogenes Laertius 6.80, Hicks' Loeb translation on Perseids ("Satyrus adds that the sorry tragedies are by his friend Philiscus, the Aeginetan"), https://fgh.perseids.org/read/greekLit/tlg0004/tlg001/perseus-eng2/6.2.62-6.2.81

2. [should-fix] [accuracy] Section "The Megarians and dialectic".
   Current: "<strong>Diodorus Cronus</strong> got his nickname, "old fogey", from Ptolemy I when he failed to solve a puzzle of Stilpo's at the king's table (2.111–112)."
   Problem: This states an anecdote as fact, in a report whose method is to keep the anecdote apart from the record. Diogenes Laertius 2.111 also calls Diodorus' teacher Apollonius "Cronus", and Strabo says that name passed from teacher to pupil.
   Fix: "<strong>Diodorus Cronus</strong> was nicknamed "old fogey": Strabo says the name passed to him from his teacher Apollonius Cronus (14.2.21), Diogenes Laertius that Ptolemy I gave it when he failed to solve a puzzle of Stilpo's at the king's table (2.111–112)."
   Basis: Diogenes Laertius 2.111 (Apollonius "surnamed Cronus", Diodorus "also surnamed Cronus", then the Ptolemy story); Strabo 14.2.21, quoted in Wikipedia's "Apollonius Cronus" (the epithet transferred from teacher to pupil), https://en.wikipedia.org/wiki/Apollonius_Cronus. Strabo's section number was not checked in the text.

3. [should-fix] [accuracy] Section "The Cynic as social critic, and the road to Zeno" (cosmopolitanism dispute box).
   Current: "Yet the syllogism at 6.72 makes the cosmos the only right commonwealth, a positive claim the Stoics built on."
   Problem: The syllogism at 6.72, which the report gives earlier and in Self-test 5, is the one that ends "all things belong to the wise". The claim that the only right commonwealth is the one in the cosmos is a separate statement in the same section, not that syllogism's conclusion.
   Fix: "Yet 6.72 also makes the cosmos the only right commonwealth, a positive claim the Stoics built on."
   Basis: Diogenes Laertius 6.72 (the syllogism; then, separately, "the only true commonwealth was ... as wide as the universe"), Hicks' Loeb translation on Perseids, https://fgh.perseids.org/read/greekLit/tlg0004/tlg001/perseus-eng2/6.2.58-6.2.76

4. [minor] [accuracy] Section "The doctrine under the anecdotes" (dispute box).
   Current: "answered that it is a philosophy, and the most universal one,"
   Problem: Julian calls Cynicism "in some ways a universal philosophy, and the most natural" (Or. 6, 187d). He does not call it the most universal.
   Fix: "answered that it is a philosophy, in some ways universal and the most natural,"
   Basis: Julian, Oration 6 (To the Uneducated Cynics) 182c and 187d, Wright's Loeb translation, Project Gutenberg 48768, https://gutenberg.org/cache/epub/48768/pg48768-images.html

5. [minor] [attribution] Section "Aristippus and the Cyrenaics" (dispute box).
   Current: "concludes that the founder was no ethical hedonist and had no epistemology,"
   Problem: Tsouna says there is "no evidence ... that Aristippus of Cyrene was interested in epistemology in its own right". That is weaker than "had no epistemology".
   Fix: "concludes that the founder was no ethical hedonist and shows no interest in epistemology,"
   Basis: Tsouna, "The Cyrenaics", Stanford Encyclopedia of Philosophy (2026), https://plato.stanford.edu/entries/cyrenaics/

6. [minor] [accuracy] Section "Diogenes of Sinope: what can be known".
   Current: "and died at Corinth nearly ninety (6.76)"
   Problem: Section 6.76 gives his age. The Craneum at Corinth and the burial by the Isthmus gate come in 6.77–78.
   Fix: "and died at Corinth nearly ninety (6.76–78)"
   Basis: Diogenes Laertius 6.76–78, Perseids (as in finding 1)

7. [minor] [attribution] Section "Diogenes of Sinope: what can be known" (coinage dispute box).
   Current: "Sinope's coins show that its currency was tampered with in the mid-fourth century, and Branham (1996) and Navia (2005) give the story a historical core. If the coins date the exile, Diogenes reached Athens after Antisthenes was dead."
   Problem: The last sentence is the writer's own inference, and it needs the coins' date, which the box does not give. Navia, who is cited for the historical core, is also reported to reconcile the dates with an earlier visit to Athens. As it stands, the box presents the inference as settled.
   Fix: "Debased Sinopean coins of about 350–340 BC led Branham (1996) and Navia (2005) to give the story a historical core. If the coins date the exile, Diogenes reached Athens after Antisthenes' death, and those who keep the link must posit an earlier visit."
   Basis: Wikipedia "Diogenes", citing Branham 1996 p. 90 and Navia 2005 pp. 12–14 for the 350–340 BC coins and for the earlier-visit reconciliation, https://en.wikipedia.org/wiki/Diogenes. Not checked in Branham or Navia themselves.

8. [minor] [register] Section "Diogenes of Sinope: what can be known", and Self-test 2.
   Current: "Two fourth-century witnesses stand outside book 6." and "Which fourth-century evidence stands outside book 6's anecdotes"
   Problem: Theophrastus' mouse survives only in book 6 (6.22), as the same paragraph says. These witnesses are early and independent of the Hellenistic compilers, but they are not outside book 6.
   Fix: "Two witnesses are Diogenes' contemporaries, though one reaches us only through book 6." and "Which contemporary evidence is older than book 6's compilers"
   Basis: Diogenes Laertius 6.22 ("says Theophrastus in the Megarian"); SSR V B 172 for the Theophrastus testimony (Peitho abstract, https://pressto.amu.edu.pl/index.php/peitho/article/view/25896)

9. [minor] [lane] Section "The Cynic as social critic, and the road to Zeno".
   Current: "Zeno of Citium, shipwrecked near Athens, read the second book"
   Problem: The 12.5 prompt hands the road through Crates to Zeno to this module, so the shipwreck, the bookshop and the lentil soup belong here. The 12.7 prompt ("Zeno of Citium, his Cynic training") invites the same anecdotes, so they risk being duplicated.
   Fix: no change to 12.5. When 12.7 is written or checked, it should point back to module 12.5 for the bookshop and lentil-soup anecdotes (DL 7.2–3) and not retell them.
   Basis: greek-syllabus.html, prompts 12.5 and 12.7

## Confirmed
- DL book divisions: Aristippus and the Cyrenaics 2.65–104, Megarians 2.106–120, Antisthenes 6.1–19, Diogenes 6.20–81, Crates to Menippus 6.85–101; Ionian succession Socrates to Zeno at 1.15; Hippobotus' list without the Cynics, 1.19
- Zeno's Chreiai cited at 6.91; lettuce retort with Aristippus winning at 2.68 and Diogenes winning against Plato at 6.58 (Loeb page order on Perseids)
- SSR numbering: Aristippus IV A, Antisthenes V A, Diogenes V B; Rhetoric 1411a24–25 = SSR V B 184, the oldest testimony to Diogenes (Peitho abstract, pressto.amu.edu.pl, article 25896)
- Xenophon, Symposium 4.34–44 (Antisthenes on wealth); DL 6.2 (ponos, Heracles and Cyrus), 6.10–11 (virtue teachable and sufficient, "Socratic strength"), 6.11 (law of virtue), 6.13 (Cynosarges, Haplokyon)
- Aristotle, Metaphysics 1024b32–34, Topics 104b20–21, Metaphysics 1043b23–28 (the Antistheneans, silver like tin)
- DL 6.20–21, the four versions of the coinage scandal (Diocles, Eubulides, Pordalus, the oracle); 6.22, Theophrastus' mouse; 6.29–30 and 6.74, the sale to Xeniades in Menippus' Sale of Diogenes; 6.76–77, the three deaths; 6.79, Demetrius on the same day as Alexander; 6.80, the list of works
- DL 6.69 (breakfast in the agora, parrhēsia the finest thing), 6.70–71 (twofold askēsis, contempt for pleasure most pleasant, defacing the currency), 6.72 (syllogism; wives in common; cosmic commonwealth), 6.103 (enstasis biou)
- Goulet-Cazé, L'ascèse cynique: un commentaire de Diogène Laërce VI 70–71 (Vrin, 1986): title and year
- DL 6.85 (Pera parody of Odyssey 19.172; Hippobotus on Bryson), 6.86 (Door-opener), 6.87 (113th Olympiad; Telephus; about 200 talents, from Antisthenes' Successions), 6.93 (Alexander and Thebes; obscurity and poverty), 6.96–98 (Hipparchia, the stripping, the Theodorus argument, the loom); Sextus, Outlines 1.153 (Crates and Hipparchia in public)
- DL 6.99–101 (Menippus: Phoenician, slave, Hermippus' day-lending and hanging, thirteen books, Nekyia, Wills, Letters from the Gods); Strabo 16.2.29 (spoudogeloios); Cicero, Academica 1.8 (Varro imitated, did not translate); Bion at DL 4.46–58; Cercidas P.Oxy. 1082
- DL 2.65 (drawn by Socrates' fame; first Socratic to charge fees), 2.66 (adaptability; "the king's poodle"); Phaedo 59c (Aegina); Memorabilia 2.1.13 (a stranger everywhere); Metaphysics 996a29–b1 (Aristippus scorning mathematics)
- DL 2.85 (smooth motion the end), 2.86–93 (Cyrenaic doctrine); Sextus, Against the Mathematicians 7.191–192 ("we are whitened")
- Aristocles in Eusebius, Preparation for the Gospel 14.18.31–32 (the grandson "mother-taught", end defined as living pleasantly)
- Tsouna, SEP "The Cyrenaics" (2026): founder no ethical hedonist; argues against Rowe 2015, for whom Aristippus of Cyrene is behind the Theaetetus' kompsoteroi; Mondolfo (1953, 1958) gives that role to the grandson; Hegesias suicide stories "apocryphal" (https://plato.stanford.edu/entries/cyrenaics/)
- Theaetetus 156a, the "subtler" (kompsoteroi); module 12.2 treats the theory at 156a–157c, so the pointer holds
- DL 2.86 (Hegesias the Death-persuader), 2.94–99 (Hegesias, Anniceris, Theodorus); Cicero, Tusculan Disputations 1.83–84 (Ptolemy's ban), 1.102 (Theodorus to Lysimachus); On the Nature of the Gods 1.2, 1.63; DL 10.136–137 (Epicurus against the Cyrenaics)
- DL 2.106 (Megarians, Eristics, Dialecticians), 2.108 (Eubulides' seven arguments); Athenaeus 9.401e (Philitas epitaph)
- Sextus, Outlines 2.110 (Philo's and Diodorus' conditionals); Boethius' report of Diodorus' definition of the possible (Bobzien, SEP "Dialectical School": Boethius, On Interpretation 2nd ed. II.234–235); Epictetus, Discourses 2.19.1–5 (three propositions; Diodorus rejects the third, Cleanthes the first, Chrysippus the second)
- Prior, "Diodoran Modalities", Philosophical Quarterly 1955, the pioneering reconstruction (Bobzien, SEP "Dialectical School", https://plato.stanford.edu/entries/dialectical-school/); Gaskin, The Sea Battle and the Master Argument (de Gruyter, 1995): title and year
- DL 2.115 (Stilpo to Demetrius, Megara taken 307); Seneca, Letters 9.18–19; DL 2.105, 2.125–144 (Elian-Eretrian school)
- DL 6.38 (tragic curse), 6.40 (plucked fowl), 6.45 (great thieves), 6.63 (citizen of the world); Kleingeld and Brown, SEP "Cosmopolitanism": negative claim, no unambiguous positive commitments, the Cynic way of life as the example (https://plato.stanford.edu/entries/cosmopolitanism/)
- Foucault, 1984 course, English translation The Courage of Truth, 2011
- DL 7.2–3 (shipwreck, bookshop, Memorabilia book 2, Crates), 7.3 (lentil soup), 7.4 (Republic on the dog's tail), 7.2 (Stilpo, Xenocrates, Polemo), 7.121 (Apollodorus: Cynicism a short cut to virtue); Cicero, On Duties 1.148
- Branham (1996) and Navia (2005) give the coinage story a historical core (Wikipedia "Diogenes", citing both)
- Pointers: module 6.5 (Antisthenes' dates, Gorgias, madness over pleasure; Euclides, Liar and Heap, Stilpo's apatheia, Sedley's Dialectical school; the Master Argument), module 7.2 (founder dispute), module 12.2 (Antisthenes' Socratic writings; Theaetetus 156a–157c), module 10.4 (Ajax and Odysseus), Rome module 7.1 (Apocolocyntosis), module 7.4 (Lucian), module 11.7 (Onesicritus' education of Alexander): all true of their targets. Modules 12.6 and 12.7 and Rome modules 13.3 (Demetrius, Peregrinus) and 13.6 (Discourses 3.22) were checked against their prompts and match.
- crosscheck.py: no shared passages; the 12.5 to 7.2 box overlap is a different dispute (school or way of life, not the founder), so not a duplicate
- House style: British spelling, no em dashes, five dispute boxes of two to three sentences with names on each side, ten self-test questions whose answers agree with the body, three carry-forward items
