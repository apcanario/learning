# Greece 12.1: The Presocratics

Verdict: fix
Body words: 3369 (target 3000)

## Coverage
- Milesians (Thales, Anaximander, Anaximenes): covered; argument, Aristotle's objections and the next step (Diogenes of Apollonia) all present
- Xenophanes: covered
- Pythagoras and the Pythagoreans, with Philolaus: covered (Pythagoras rightly brief, pointed to 5.6; Philolaus full)
- Heraclitus: covered
- Parmenides, Zeno's paradoxes and Melissus: covered; the four motion paradoxes pointed back to 5.6, Aristotle's two answers and the place and millet arguments added
- Empedocles: covered
- Anaxagoras: covered
- Leucippus and Democritus: covered
- Evidence problem: Aristotle, Metaphysics A; Theophrastus; Simplicius: covered
- Diels' Die Fragmente der Vorsokratiker and DK numbering: covered (with Laks and Most)
- Derveni papyrus as a witness to early philosophical reading, theogony pointed back to 2.1 and 8.2: covered
- Strasbourg Empedocles: covered
- Pointers back to 5.6 for each item it holds: covered for the evidence base, core claims, Parmenides' inference, Zeno's paradoxes and the Pythagoras, flux, monism and Strasbourg disputes; missing for the Ionia question (finding 2)

## Findings
1. [error] [attribution] Section "Xenophanes and the Pythagoreans".
   Current: "Aristotle reports a central fire circled by ten bodies, the tenth a counter-earth invented to reach the perfect ten (<em>Metaphysics</em> 986a8–12), and objects that heavy bodies cannot be built from weightless numbers (1090a30–35)."
   Problem: In a paragraph on Philolaus this makes Aristotle report Philolaus' system, but Aristotle names Philolaus only once (Eudemian Ethics 1225a30, an apothegm) and gives the central fire and counter-earth to "the Pythagoreans"; the system is assigned to Philolaus by later doxography. The cited Metaphysics passage also has the ten bodies and counter-earth but no central fire, which is in On the Heavens.
   Fix: "Aristotle, who names Philolaus only once, reports of the Pythagoreans a central fire (<em>On the Heavens</em> 293a20–b1) circled by ten bodies, the tenth a counter-earth invented to reach the perfect ten (<em>Metaphysics</em> 986a8–12), and objects that heavy bodies cannot be built from weightless numbers (1090a30–35); later doxography (Aëtius 2.7.7) gives the system to Philolaus."
   Basis: SEP "Philolaus" (Huffman), section on the cosmos: Aristotle "only refers to Philolaus once by name" (EE 1225a30), elsewhere to "the so-called Pythagoreans"; Aëtius 2.7.7 cited for the central fire; Metaphysics 986a8–12 and On the Heavens 293a20–b1 from the Bekker text.

2. [should-fix] [pointer] Section "The Milesians: arguing for a principle".
   Current: "<p>Module 5.6 gives the core claims: water, the boundless, air, the floating earth, equidistance, condensation and rarefaction.</p>"
   Problem: The prompt lists 5.6's question of why philosophy began in Ionia among the things to point back to; the report never mentions Ionia or 5.6's section on it.
   Fix: "<p>Module 5.6 asks why philosophy began in Ionia and gives the core claims: water, the boundless, air, the floating earth, equidistance, condensation and rarefaction.</p>"
   Basis: prompt for 12.1 in greek-syllabus.html; greece/r-5.6.html, section "Why philosophy began in Ionia".

3. [should-fix] [attribution] Section "Parmenides and Zeno".
   Current: "F. M. Cornford and J. E. Raven (<em>Pythagoreans and Eleatics</em>, 1948) built on it."
   Problem: The parenthesis reads as a joint book; <em>Pythagoreans and Eleatics</em> (1948) is Raven's alone. Cornford's Tannery-based reading of Zeno came earlier and elsewhere.
   Fix: "F. M. Cornford and, in <em>Pythagoreans and Eleatics</em> (1948), J. E. Raven built on it."
   Basis: J. E. Raven, Pythagoreans and Eleatics: An Account of the Interaction between the Two Opposed Schools during the Fifth and Early Fourth Centuries B.C. (Cambridge, 1948), sole author; known, not searched.

4. [should-fix] [accuracy] Section "Xenophanes and the Pythagoreans".
   Current: "Aristotle speaks only of the so-called Pythagoreans."
   Problem: Overstated. The treatises speak almost always of "the Pythagoreans" or "the so-called Pythagoreans", but Pythagoras is named at Rhetoric 1398b14 (and at Metaphysics 986a29–30, possibly interpolated), and Aristotle's lost work on the Pythagoreans told stories of the man himself.
   Fix: "Aristotle's treatises speak almost always of the so-called Pythagoreans."
   Basis: Rhetoric 2.23, 1398b14 (Alcidamas: the Italians honoured Pythagoras); SEP "Pythagoreanism" section 2.3 (Aristotle treated Pythagoras as a wonder-working founder of a way of life, citing Huffman 1993, 31–34).

5. [minor] [accuracy] Section "Fragments, testimonia and the making of a canon".
   Current: "<em>Metaphysics</em> A (983a24–993a10)"
   Problem: The range stops at the end of chapter 9, but the next clause cites the lisping image at 993a15–16, which is in chapter 10 (993a11–27).
   Fix: "<em>Metaphysics</em> A (983a24–993a27)"
   Basis: Bekker pagination of Metaphysics A.10 (993a11–27); Book alpha begins at 993a30.

6. [minor] [accuracy] Section "Heraclitus: the argument behind the riddles".
   Current: "(DK 28 B 6.8–9)"
   Problem: The sentence quotes the "two-headed" mortals, which is B 6.5; lines 8–9 hold only the "same and not the same" and the back-turning path.
   Fix: "(DK 28 B 6.4–9)"
   Basis: text of DK 28 B 6 (dikranoi at line 5, palintropos at line 9).

7. [minor] [attribution] Section "Xenophanes and the Pythagoreans".
   Current: "Burkert (<em>Weisheit und Wissenschaft</em>, 1962; English 1972) argued for a genuine core, and Carl Huffman (<em>Philolaus of Croton</em>, 1993) brought most scholars to accept about eleven fragments (B 1–7, 6a, 13, 16, 17)"
   Problem: Huffman's own SEP entry credits the consensus on the eleven fragments to Burkert's 1962 arguments, with Huffman's edition defending it; the box gives Huffman the credit for persuading most scholars.
   Fix: "Burkert (<em>Weisheit und Wissenschaft</em>, 1962; English 1972) argued for a genuine core, now generally put at about eleven fragments (B 1–7, 6a, 13, 16, 17) and defended by Carl Huffman (<em>Philolaus of Croton</em>, 1993)"
   Basis: SEP "Philolaus": "some 11 fragments are genuine (Frs. 1–6, 6a, 7, 13, 16 and 17)", consensus credited to Burkert 1962; Burkert accepts 6b and A26, Huffman rejects them (so the rest of the box is right).

8. [minor] [pointer] Section "Empedocles and the Strasbourg papyrus".
   Current: "Lucretius praised Empedocles as a poet (1.716–733) before dismantling his roots (Rome module 5.6)."
   Problem: Placed after "dismantling his roots", the pointer implies Rome 5.6 covers Lucretius' critique of Empedocles; Rome 5.6 has a Lucretius section but never mentions Empedocles.
   Fix: "Lucretius (Rome module 5.6) praised Empedocles as a poet (1.716–733) before dismantling his roots."
   Basis: rome/r-5.6.html, section "Lucretius: physics against fear" (no mention of Empedocles).

9. [minor] [pointer] Section "Parmenides and Zeno".
   Current: "(<em>Sophist</em> 241d–259b; module 12.3)"
   Problem: The 12.3 prompt names neither the Sophist nor the Philebus (the same applies to "(module 12.3)" after Philebus 16c), so the pointer may land on nothing; module 6.5 already says the Sophist treats not-being as difference.
   Fix: "(<em>Sophist</em> 241d–259b; module 6.5)"
   Basis: prompt for 12.3 in greek-syllabus.html; greece/r-6.5.html, section "The Republic, the Symposium, the late dialogues".

Fixes 1 to 4 add about 30 words, leaving the body near 3400, inside the band (2700 to 3450).

## Confirmed
- Lane against 5.6: no core claim retold beyond a clause; none of 5.6's disputes repeated (Burkert/Zhmud, Kirk and Marcovich against Popper and Barnes, Owen/Curd, Osborne and Inwood on one poem, Mansfeld on the trial, Furley); the four motion paradoxes pointed back, not retold (greece/r-5.6.html).
- Every "Module 5.6 gives ..." pointer is true of 5.6, including the sufficient-reason argument found in Anaximander and the Strasbourg two-poem question (greece/r-5.6.html).
- Derveni lane: 2.1 has the theogony and the aidoion dispute, 8.2 the pyre near Thessaloniki; 12.1 retells neither (greece/r-2.1.html, greece/r-8.2.html).
- crosscheck.py: no shared passages; the only box overlap (with 4.2, on Janko and Burkert) is a false positive about Homer's date.
- Pointers to unwritten neighbours: 12.2 (Gorgias' On Not Being, pseudo-Aristotelian MXG), 12.6 (atoms and swerve), 12.7 (Stoic physics), 12.8 (Sextus and scepticism) are all in their prompts.
- DK numbers match the quoted text: 12 B 1; 13 B 1 (Plutarch, On the Principle of Cold 947f); 21 B 14–16, 18, 23–26, 34, 38; 22 B 9, 23, 31, 36, 51, 55, 59, 60, 61, 88, 107, 111, 129; 28 B 7, 8.7–11, 8.22–31, 8.42–49; 30 B 1–3, 6, 7, 8; 31 B 8, 13, 61, 96, 109, 139; 44 B 1–4, 6; 59 B 3, 10, 11, 12, 17; 64 B 2; 67 B 2; 68 B 9, 11, 117, 125, 156, 169–297, 191; 70 B 1. No testimonium is cited as B.
- Simplicius, Commentary on the Physics 144.25–28 (copies Parmenides for the book's rarity) and 24.26–25.1 (Anaximenes, DK 13 A 5).
- Aristotle by Bekker page, all matching their content: Metaphysics 983b20–27, 984b15–18, 985a18–29, 985b19–20, 986a8–12, 986b21–27, 987a32–b1, 993a15–16, 1005b23–26, 1009b11–17, 1010a10–15, 1090a30–35; Physics 186a10–16, 186a24–25, 187a26–188a18, 191a23–b34, 198b16–199a8, 203b6–15, 204b22–29, 209a23–25, 233a21–31, 250a19–22, 263a4–b9; On the Heavens 294a28–b1, 295b10–34; On Generation and Corruption 314a18–20, 316a14–b16, 325a2–b5; Parts of Animals 642a17–24; On the Soul 404b11–15.
- Sextus, Against the Mathematicians 7.49 (B 34) and 7.135–139 (B 9, B 11); Diogenes Laertius 9.72 (B 117) and 2.10 (Aegospotami); Pliny, Natural History 2.149 (467); Plutarch, Pericles 26 (Melissus, 441/0) and Against Colotes 1108f (B 156); Theophrastus, On the Senses 49–83.
- Plato: Republic 600a–b (Pythagoras' only mention), Phaedo 61d–e, Sophist 241d and 242d, Parmenides 128c–e, Philebus 16c.
- Diels, Doxographi Graeci 1879; Vorsokratiker 1903, Kranz from the fifth edition (1934–37), sixth 1951–52; A, B, C divisions; Heraclitus ordered alphabetically by citing author; Laks and Most, Loeb 2016, P/D/R.
- Cherniss 1935, Guthrie JHS 1957, Mansfeld and Runia, Aëtiana from 1997.
- Bywater 1868 ("showed that a few of the fragments were spurious and then assumed that all the rest were as well"), Huffman's dates c. 470–c. 385, Burkert and Huffman differing over B 6b: SEP "Philolaus".
- Heraclitus/Parmenides box: Bernays 1850 and Graham 2002 (Parmenides answers Heraclitus), Reinhardt 1916 (reverse order), Zeller and Mansfeld 1964 (neither knew the other): Peitho 15 (2024), "Seneca's Heraclitus DK 22 B 49a and Parmenides", footnotes 2–4 (https://pressto.amu.edu.pl/index.php/peitho/article/view/45352). Hippolytus palintropos against Plutarch palintonos for B 51.
- Empedocles box: O'Brien 1969 and Wright 1981 (symmetrical cycle, two cosmogonies and zoogonies) against Bollack and Long 1974 (one); Trépanier 2003 (ensemble d as a distinct zoogony under Strife) and Laks 2001 challenging: SEP "Empedocles" (Spring 2016 archive).
- Strasbourg papyrus: Akhmim/Panopolis, acquired 1904, strips backing the bronze leaves of a funerary crown, copy of the late first century AD, Martin 1990, marginal sign at line 300 of the book: Universalis, "Empédocle", section 7 (https://www.universalis.fr/encyclopedie/empedocle/7-le-papyrus-de-strasbourg/); Martin and Primavesi 1999.
- Derveni box: Janko 1997 (Diagoras), Betegh 2004 (full title correct; "an Orphic priest rather than a sophist or Presocratic physikos"): Janko, BMCR 2005.01.27 (https://bmcr.brynmawr.edu/2005/2005.01.27). Burkert's Stesimbrotus (ZPE 62, 1986) and Kahn's Euthyphro (1997) known. Column IV overlapping B 3 and B 94.
- Owen, "Zeno and the Mathematicians" (1957–58); Tannery 1885; Russell, The Principles of Mathematics (1903) on motion; Kahn's veridical "is"; Vlastos 1945–46 on Democritus' ethics.
- Self-test answers agree with the body; carry-forward items transfer; seven dispute boxes, each two to three sentences with names on each side; British spelling, no em dashes.
