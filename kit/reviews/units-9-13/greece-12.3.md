# Greece 12.3: Plato

Verdict: keep
Body words: 3392 (target 3000; band 2700–3450). The eight body fixes below together are net zero: checked by applying them to a scratch copy, which `check.py` counts at 3392.

## Coverage
- Life, Sicily and the Seventh Letter's authenticity: covered (Morrow and Ledger against Edelstein and Burnyeat and Frede)
- The Academy: covered (mathematics, division, lawgivers, no orthodoxy; the sceptical Academy pointed to 12.8)
- The dialogue form: thin (canon, tetralogies and chronology are covered; the form itself comes only as Schleiermacher's "planned course", with no word on what the form does: finding 2)
- Chronology debate and stylometry: covered (Campbell, Dittenberger, Lutosławski, Brandwood; Schleiermacher against Hermann; unitarians against developmentalists)
- Forms and the objections of the Parmenides: covered (130b–135c, Vlastos 1954; Sophist on not-being)
- Recollection and the immortal soul (Meno, Phaedo): covered
- The Republic beyond 6.5's outline: covered (Glaucon's classes of goods, the Divided Line, the return to the Cave, Book 9's three proofs, Sachs against Vlastos)
- Love in the Symposium and Phaedrus: covered
- The Timaeus' cosmos: covered
- The Laws: covered
- The unwritten doctrines: covered (Aristotle, Aristoxenus and Simplicius kept apart from the dialogues; Tübingen against Cherniss and Vlastos; Sayre)
- Judgement myths read as method, pointed back to 8.4: covered
- Atlantis in the Timaeus and Critias: covered
- The Phaedrus' charioteer: covered
- Lane, 6.5: life, Academy, stylometric groups, Forms with the Phaedo's sticks, the Sun, the Third Man, the Republic outline, Diotima's ascent and the critique of writing all pointed back to, not retold; but one dispute box restages 6.5's Vlastos against Kahn (finding 1)
- Lane, 8.4: the three judgement myths' contents not retold; the Pindar fragment pointed to 8.4: kept
- Lane, 12.1: Sophist parricide and not-being as difference taken up; Philebus limit and unlimited taken up, but without the Pythagorean link 12.1 hands on (finding 3)
- Lane, 12.2: Phaedo proofs and the Republic after Thrasymachus taken up; Socratic problem and death scene not retold (apart from finding 1)

## Findings
1. [should-fix] [lane] Section "Canon and chronology", dispute box.
   Current: "Developmentalists hold that the doctrines changed: Vlastos (1991) set out ten theses dividing the early Socrates from the Platonic one."
   Problem: The box sets Vlastos (1991) against Kahn (1996) on early Socrates against the Platonic one. That is the exchange module 6.5's Socrates box already gives ("Vlastos (<em>Socrates: Ironist and Moral Philosopher</em>, 1991) held ... Kahn (1996) replied"), and 12.2 already points back to it ("Kahn ..., whose reply to Vlastos module 6.5 gives"). crosscheck.py flags the pair. Keep Shorey, Kahn's proleptic reading and the Owen and Cherniss sentence, which are new, and point back for the Vlastos side.
   Fix: "Developmentalists hold that the doctrines changed, Vlastos (1991) most sharply; module 6.5 gives his exchange with Kahn."
   Basis: greece/r-6.5.html, the box in "Socrates: sources and method"; greece/r-12.2.html, "The Socratic dialogue as a genre"; `python3 crosscheck.py greece 12.3`, section 3.

2. [should-fix] [register] Section "Canon and chronology" (coverage of "the dialogue form").
   Current: "Schleiermacher, introducing his translation from 1804, saw a planned course opening with the <em>Phaedrus</em>;"
   Problem: The prompt asks for "the dialogue form and the chronology debate". The section treats canon and chronology, but the form itself gets only "a planned course", with no word on what the form does. Schleiermacher's point was that the form is the teaching: it makes readers find the answers themselves. One clause makes him the reading of the form the prompt asks for, and repeats nothing of 6.5's "Plato never speaks in his own voice".
   Fix: "Schleiermacher, introducing his translation from 1804, made the form the method: a planned course, opening with the <em>Phaedrus</em>, that leaves readers to find the answers themselves;"
   Basis: Schleiermacher, <em>Platons Werke</em> I.1 (1804), Einleitung: the dialogue form forces the reader's own activity, and the dialogues are ordered as a course beginning with the <em>Phaedrus</em>. A standard reading; not searched.

3. [should-fix] [lane] Section "The unwritten doctrines".
   Current: "contains limit and unlimitedness (16c–17a);"
   Problem: Module 12.1 hands on the <em>Philebus</em> as Plato taking over the Pythagoreans' limit and unlimited: its Philolaus paragraph ends "Plato's <em>Philebus</em> (16c) takes over limit and unlimited (module 12.3)". 12.3 covers 16c but never names the Pythagorean source, so a reader arriving from 12.1 finds no link back.
   Fix: "contains limit and unlimitedness (16c–17a), Philolaus' pair (module 12.1);"
   Basis: greece/r-12.1.html, the Philolaus paragraph (DK 44 B 1–2); Philebus 16c, where the method comes from "the ancients" by way of "some Prometheus", usually read as Pythagoras (Huffman, <em>Philolaus of Croton</em>, 1993).

4. [should-fix] [register] Section "Self-test", question 10.
   Current: "Each follows an argument that has not fully persuaded,"
   Problem: The body says each myth "follows argument that has done what it can", and its third example is that "justice has been proved good in itself". Before Er, Glaucon and Adeimantus are persuaded. The answer contradicts the body for the <em>Republic</em>.
   Fix: "Each follows an argument that has gone as far as it can,"
   Basis: greece/r-12.3.html, "Plato's myths as method", first paragraph.

5. [minor] [lane] Section "Life, Sicily and the Academy".
   Current: "Module 6.5 gives the outline: the birth about 428, the kinship with Critias and Charmides, the disillusion the <em>Seventh Letter</em> describes, the three Syracusan visits and the founding of the Academy."
   Problem: The pointer is accurate but lists five of 6.5's items at length, and the next paragraph tells the visits in detail anyway. A short pointer is enough, and the saving pays for findings 2 and 3.
   Fix: "Module 6.5 gives the outline, from the birth about 428 to the founding of the Academy."
   Basis: greece/r-6.5.html, "Plato: Academy, dialogue, Forms", first paragraph.

6. [minor] [accuracy] Section "Life, Sicily and the Academy".
   Current: "called Plato for his breadth, of shoulders or of style (3.4)"
   Problem: Diogenes gives a robust physique (<em>euexia</em>), breadth of style, or, citing Neanthes, a broad forehead. "Shoulders" is the modern gloss, not his word.
   Fix: "called Plato for his breadth, of build or of style (3.4)"
   Basis: Diogenes Laertius 3.4 (Hicks, Loeb: "because of his robust figure ... others affirm that he got the name from the breadth of his style, or from the breadth of his forehead, as Neanthes affirms").

7. [minor] [accuracy] Section "The Laws".
   Current: "(885b) are answered by the argument"
   Problem: Only the first belief, that the gods do not exist, is answered by the argument for soul's priority (891e–899d), the span cited. Their indifference is answered at 899d–905d and their bribability at 905d–907b. As written, all three rest on one argument.
   Fix: "(885b) are answered, the first by the argument"
   Basis: Plato, Laws 10, 885b, 891e–899d, 899d–905d, 905d–907b.

8. [minor] [attribution] Section "Self-test", question 1.
   Current: "left on wax at Plato's death (Diogenes Laertius 3.37)"
   Problem: Diogenes says only that some report Philip of Opus transcribed the <em>Laws</em>, "which were in wax". "At Plato's death" is a modern inference. The body says it correctly ("Philip transcribed the <em>Laws</em> from wax tablets (3.37)").
   Fix: "transcribed from wax by Philip of Opus (Diogenes Laertius 3.37)"
   Basis: Diogenes Laertius 3.37 (Hicks: "Some say that Philip the Opuntian copied out the Laws, which were in wax").

## Confirmed
- Seventh Letter: 327a (Dion won on the first visit), 328c (fear of being "a man of words only"), 329c (Dion expelled in the fourth month), 333d–e (killers friends through hospitality and the Mysteries, not philosophy), 341c–d (no treatise; the leaping spark), 342a–344d (the digression on name, account, image and knowledge), 350a–b (Archytas' ship): match the passages (Bury's Loeb divisions).
- Diogenes Laertius 3.5 (tragedies burned), 3.6 (Megara with Euclides, after Hermodorus), 3.18–20 (sold at Aegina), 3.37 (Philip, wax, Epinomis), 3.56–61 (Thrasyllus' 36 works in nine tetralogies, the Letters as one).
- Plutarch, Dion 54–57 (Callippus' plot and the murder); Against Colotes 1126c (Aristonymus to Arcadia, Phormio to Elis, Menedemus to Pyrrha); Epicrates fr. 10 K-A in Athenaeus 2.59c–f (the pumpkin).
- Aristotle by Bekker page, each kept apart from the dialogues: Politics 1264b26–27 (Laws written after the Republic); Metaphysics 987a32–b10 (Cratylus, Socratic definitions, Ideas), 987b14–988a17 (intermediates, One and Great-and-Small, Forms as numbers), 1028b21–24 (Speusippus); Nicomachean Ethics 1172b9–15 (Eudoxus); Physics 209b11–16 (<em>agrapha dogmata</em>); On the Heavens 279b32–280a1 (the didactic defence rejected; the commentators give it to Xenocrates).
- Aristoxenus, Elements of Harmonics 2.30–31 (the lecture On the Good, as Aristotle used to tell it).
- Simplicius, Commentary on Aristotle's Physics 151.6: Aristotle, Speusippus and Xenocrates wrote up On the Good (Guthrie, A History of Greek Philosophy 5, citing Phys. 151.6 = Gaiser test. 8, via https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/guthrie-plato.asp?pg=11).
- Stylometry: Campbell's Sophistes and Politicus (1867) with the Laws as fixed point; Dittenberger, Hermes 1881, ti mēn and other particles; Lutosławski, The Origin and Growth of Plato's Logic (1897), about 500 features (BMCR review of stylometric studies, https://bmcr.brynmawr.edu/?p=60534); Brandwood, The Chronology of Plato's Dialogues (1990), middle group Republic, Parmenides, Theaetetus, Phaedrus; the late six avoid hiatus.
- Schleiermacher from 1804 with the Phaedrus first; K. F. Hermann 1839; Shorey 1903; Kahn 1996 (proleptic reading); Vlastos 1991 (the ten theses); Owen, CQ 1953, against Cherniss, AJP 1957, on the Timaeus.
- Seventh Letter box: Morrow 1935; Ledger, Re-counting Plato (1989), finding it Platonic; Edelstein, Plato's Seventh Letter (1966); Burnyeat and Frede, The Pseudo-Platonic Seventh Letter (2015).
- Unwritten doctrines: Krämer 1959, Gaiser 1963, Szlezák 1985, Sayre, Plato's Late Ontology (1983), Cherniss, The Riddle of the Early Academy (1945), Vlastos' review of Krämer in Gnomon 35 (1963) (https://en.wikipedia.org/wiki/Plato%27s_unwritten_doctrines, bibliography).
- Parmenides 127b–c, 130b–e, 131a–e, 132a–b, 132b–c, 132c–133a, 133b–134e, 135b–c, 137c–166c; Vlastos, Phil. Review 1954 (self-predication and non-identity jointly inconsistent); Sophist 237a (quoting DK 28 B 7), 241d, 248e–249a, 257b, 263a–b; Ryle 1939, Cornford 1939; Timaeus 51b–e.
- Meno 80d–e, 81a–c, 82b–85b, 85c–d, 97d–98a; Phaedo 70c–72e, 72e–77a, 78b–80b, 85e–86d, 87b–88b, 92a–95a, 97b–99c, 99c–100b, 100b–e, 102a–107b, 106b–e, 107b, 114d; Phaedrus 245c–246a with Laws 896a; Republic 608d–611a.
- Republic 357b–358a, 358e–359b, 362e–367e, 506d–e, 509d–511e, 510b–511c, 519c–520a, 520e, 576c–580c, 580d–583a, 583b–588a (729 at 587e), 612b–614a, 442e–443b, 617e, 621b–c; Sachs, Phil. Review 1963; Vlastos 1971.
- Symposium 199c–201c, 206a, 206b–e, 208c–209e, 212a; Phaedrus 244a–245c, 246a, 247c, 248c–e, 248e–249a, 249d–252b, 253c–254e, 256a–b; Vlastos 1973 (Platonic Studies); Nussbaum 1986.
- Timaeus 20d–25d, 26e, 27d–28c, 29d, 29e–30a, 30b, 35a–36d, 37d, 47e–48a, 49a, 52a–b, 53c–57c; Critias 108e–121c; Calcidius' partial translation; Vlastos, CQ 1939, Cornford 1937, Tarán 1971; Crantor in Proclus, Strabo 2.3.6 on Posidonius; Vidal-Naquet, REG 1964; Gill, CP 72 (1977).
- Laws 625a–b, 663e–664a, 693d–e, 716c, 720a–e, 722d–723b, 737e–738b (5,040), 739a–e, 885b, 908e–909a (five years; death on relapse), 942a–c, 961a–968e; Popper 1945; Levinson, In Defense of Plato (1953; the real title, hence check.py's soft "Defense").
- Gorgias 523a (a <em>logos</em> Callicles will take for a <em>mythos</em>). 12.3 is right here; 8.4's "each time calling it a <em>mythos</em>" is loose for the Gorgias, but that is outside this review.
- Pointers: 6.5 (life outline, Academy "a circle", Forms with the sticks, the Sun, the Third Man, the Republic outline, the Symposium's setting and ascent, the Phaedrus on writing, Magnesia "second-best") all true; 8.4 (Pindar fr. 133, the three judgement myths) true; 12.1 (Sophist, Philebus) true; 12.2 (Phaedo proofs; Glaucon finds Thrasymachus charmed, not refuted, 358b; Protagoras' measure) true; 12.8 and 12.4 checked against their prompts (sceptical Academy, Neoplatonist One; Aristotle's Metaphysics) and fit.
- No shared seven-word passages with any written module (crosscheck section 2). The 12.2 box crosscheck pairs with this one (Burnet and Taylor against Gigon) shares only generic names and is a different dispute. Owen 1953 and Cherniss 1957 appear in two of 12.3's own boxes, on linked but different questions (the Timaeus' date; whether the Forms were kept).
- Not checked: Edelstein, JHI 1949, read as addressing the parts of the soul argument does not reach (the article text was not reachable; summaries found mention only myth conforming to dialectic). Denyer 2001 and Woodruff 1982 as defenders of authenticity are from knowledge.
- House style: British spelling, no em dashes, ten sections, nine dispute boxes each of two or three sentences with names on both sides, ten self-test questions, three carry-forward items.
