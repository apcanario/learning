# Greece 12.6: Epicurus and the Garden

Verdict: fix
Body words: 2794 (target 2500; 2841 with every fix below applied, inside the 2875 ceiling)

## Coverage
- The life, Samos and Lampsacus, the Garden as a community: covered (DL 10.1–22, the will, Roman cult of the founder; 7.2's dates and garden kept to a pointer)
- Sources: the three letters and the Principal Doctrines (DL book 10): covered (table with section spans)
- Vatican Sayings: covered
- On Nature from the Herculaneum papyri: covered (books 25 and 28 with PHerc. numbers; villa, Philodemus and Piso handed to Rome module 13.3)
- The canon and theory of knowledge: covered
- Atoms, void and the swerve: covered (revisions of Democritus tied to named objections; 7.2's attribution question kept to one sentence)
- The soul and death (Letter to Menoeceus, KD 2): covered by pointer to 7.2 and 8.4, with the physics added
- Pleasure as the absence of pain, the kinds of desire: covered
- Friendship, justice as a compact: covered
- The gods: covered
- The fourfold remedy as Philodemus states it: covered (Greek text, PHerc. 1005)
- Diogenes of Oinoanda's wall: covered
- Hostile tradition (On Ends 2 answering Torquatus in book 1; Plutarch, Against Colotes): covered; Against Colotes is brief but adequate, with the Democritus defence in the canon section
- Point forward to Rome modules 5.6 and 13.3: covered
- Lane: 12.1's hand-off ("Epicurus revised the system") is taken up; 12.5's hand-off (DL 10.136–137) is covered and the Cyrenaic doctrine is contrasted, not retold; 8.4's material is kept to a pointer. The swerve box is a different dispute from 7.2's. The gods box restates 7.2's dispute (finding 3), and the static and kinetic pleasures and the fourfold remedy are restated without pointing back (findings 8 and 9).

## Findings
1. [error] [pointer] Section "The soul and death".
   Current: "Modules 7.2 and 8.4 give KD 2, the <em>Letter to Menoeceus</em> (124–127) and Lucretius' symmetry argument."
   Problem: Module 8.4 gives KD 2 and the Letter to Menoeceus but not the symmetry argument. Its Lucretius sentence is about book 3's allegory of Tantalus and Sisyphus. Only 7.2 has the symmetry argument (3.830–1094).
   Fix: "Modules 7.2 and 8.4 give KD 2 and the <em>Letter to Menoeceus</em> (124–127), and module 7.2 Lucretius' symmetry argument."
   Basis: greece/r-8.4.html, "The Epicurean denial"; greece/r-7.2.html, "Epicureanism", paragraph 2.

2. [should-fix] [lane] Section "The gods and the fourfold remedy" (dispute box).
   Current: " The names in module 7.2's box belong the other way round."
   Problem: The report grades a neighbour rather than just stating the right view. The 12.6 box already gives the correct names. The error in 7.2 is logged separately below for the maintainer.
   Fix: delete (including the leading space).
   Basis: the brief's lane rule; the 7.2 error is confirmed below.

3. [should-fix] [lane] Section "The gods and the fourfold remedy" (dispute box).
   Current: "A. A. Long and David Sedley (<em>The Hellenistic Philosophers</em>, 1987) revived the idealist reading, and Sedley ("Epicurus' theological innatism", 2011) defends it: the gods are our own idealisation of the blessed life, which the scholion's likeness of form suits. David Konstan ("Epicurus on the gods", 2011) restates the realist reading: the gods are compounds of fine atoms whose indestructibility the physics can explain."
   Problem: The box restates 7.2's realist and idealist readings without pointing back to it, so crosscheck flags the two boxes as possible duplicates. The prompt asks 12.6 to point back and go deeper. The 2011 essays supply the deeper part: Sedley's case that the preconception of the gods is innate, and Konstan's case that the physics explains both where the preconception comes from and why the gods are indestructible. This fix and finding 2 touch separate spans and can both be applied.
   Fix: "Module 7.2 sets out the realist and idealist readings. A. A. Long and David Sedley (<em>The Hellenistic Philosophers</em>, 1987) revived the idealist one, the gods as our own idealisation of the blessed life, which the scholion's likeness of form suits, and Sedley ("Epicurus' theological innatism", 2011) adds that our preconception of the gods is innate, not drawn from experience. David Konstan ("Epicurus on the gods", 2011) defends the realist one: the gods are atomic compounds, and the physics can explain both how we come to know them and why they never perish."
   Basis: Fish and Sanders (eds.), Epicurus and the Epicurean Tradition (2011), introduction: Long and Sedley 1987 were "instrumental in reviving the idealist interpretation"; Sedley argues our concept of the gods is innate rather than empirically derived; Konstan gives "a vigorous defence of a realist reading", explaining "the empirical origins of our prolêpsis of the gods" and "the gods' indestructibility" from Epicurean physics (https://assets.cambridge.org/97805211/94785/excerpt/9780521194785_excerpt.pdf); BMCR 2011.11.43 (https://bmcr.brynmawr.edu/?p=39463).

4. [should-fix] [register] Section "Self-test", question 4.
   Current: "How does Epicurean physics support the claim that death is nothing to us?<details><summary>Answer</summary><p>The soul is a body of fine particles that perceives only while housed in the body and scatters when the body breaks up (<em>Letter to Herodotus</em> 63–66). Since all good and bad lies in sensation and death removes sensation, death cannot be bad for the one who dies (<em>Letter to Menoeceus</em> 124–125).</p></details>"
   Problem: This is the third self-test question on the same argument. Module 7.2's question 9 asks it, and its answer shares the wording "death cannot be bad for the one who dies" (crosscheck shingles). Module 8.4's self-test asks it too. The replacement tests the physics that 12.6 adds.
   Fix: "Why, on Epicurus' account, can the soul neither survive the body nor be incorporeal?<details><summary>Answer</summary><p>It is a body of fine particles spread through the frame, which perceives only while housed in the body and scatters when the body breaks up (<em>Letter to Herodotus</em> 63–66). The only incorporeal is void, which neither acts nor is acted on, so an incorporeal soul could neither feel nor act (67).</p></details>"
   Basis: greece/r-7.2.html self-test 9; greece/r-8.4.html self-test; 12.6 body, "The soul and death", paragraph 1.

5. [minor] [pointer] Section "Atoms, void and the swerve".
   Current: "Lucretius (2.216–293; Rome module 5.6) gives it two jobs"
   Problem: Placed here, the pointer suggests that Rome 5.6 treats the swerve. It does not: 5.6 reads Lucretius against the political crisis and leaves the doctrine to Greek module 7.2. "The hostile tradition" already points to Rome 5.6 for Lucretius.
   Fix: "Lucretius (2.216–293) gives it two jobs"
   Basis: rome/r-5.6.html, "Lucretius: physics against fear".

6. [minor] [accuracy] Section "Samos, Lampsacus and the Garden".
   Current: "The will (10.16–21) leaves the garden to Hermarchus,"
   Problem: The will leaves the property to two Athenian heirs, Amynomachus and Timocrates, on condition that they give the garden to Hermarchus and his successors. As a metic, Hermarchus could not inherit Attic land himself.
   Fix: "The will (10.16–21) leaves the garden, through two trustees, to Hermarchus and his successors,"
   Basis: Diogenes Laertius 10.16–17; https://en.wikipedia.org/wiki/Amynomachus ("given to them on condition that they give the Garden to Hermarchus and the other Epicureans").

7. [minor] [accuracy] Section "Diogenes of Oinoanda's wall".
   Current: "He asks that the gods be imagined smiling, so that we smile back instead of fearing them (fr. 19)"
   Problem: The fragment is about statues: "we ought to make statues of the gods genial and smiling, so that we may smile back at them rather than be afraid of them."
   Fix: "He asks that statues of the gods be made genial and smiling, so that we smile back instead of fearing them (fr. 19)"
   Basis: Smith's translation, fr. 19, at https://texts.epicureanfriends.com/05-DiogenesOfOinoanda/

8. [minor] [lane] Section "Pleasure and the kinds of desire".
   Current: "Module 12.5 gives the Cyrenaic doctrine; Diogenes Laertius records the break with it."
   Problem: Module 7.2 already gives static and kinetic pleasure, aponia and ataraxia, from DL 10.136, and the prompt names it as 7.2's material to point back to. The paragraph restates the distinction without a pointer.
   Fix: "Module 12.5 gives the Cyrenaic doctrine and module 7.2 the two kinds of pleasure; Diogenes Laertius records the break."
   Basis: greece/r-7.2.html, "Epicureanism", paragraph 3; the 12.6 prompt.

9. [minor] [lane] Section "The gods and the fourfold remedy".
   Current: "Philodemus states the fourfold remedy (<em>tetrapharmakos</em>, a doctors' word for a four-ingredient salve) in a work"
   Problem: Module 7.2 gives the remedy in English, and the prompt lists it among 7.2's material. The prompt does ask for the remedy "as Philodemus states it", so the Greek and the papyrus belong here, but the report should point back.
   Fix: "Module 7.2 gives the fourfold remedy in English. Philodemus states it (<em>tetrapharmakos</em>, a doctors' word for a four-ingredient salve) in a work"
   Basis: greece/r-7.2.html, "Epicureanism", paragraph 3.

10. [minor] [style] Section "The canon: how anything is known".
    Current: "A distant square tower looks round (Sextus, <em>Against the Mathematicians</em> 7.208–209): the sensation"
    Problem: The example and the attestation rules (7.211–216) are Sextus' report of the Epicurean view. A parenthetical citation attached to a bare statement of doctrine is the pattern AGENT-SPEC asks writers to avoid.
    Fix: "In Sextus' report of the Epicurean view (<em>Against the Mathematicians</em> 7.208–209), a distant square tower looks round: the sensation"
    Basis: AGENT-SPEC.md, "keep the doxographer separate from the philosopher".

## For the maintainer's log: module 7.2 (not to be edited now)
- [error] [attribution] greece/r-7.2.html, section "Epicureanism" (dispute box).
  Current: "On the "realist" reading (Sedley, Long) Epicurus' gods are atomic compounds living between worlds; on the "idealist" reading (Konstan, after Scott) they are thought-constructs, idealisations of the blessed life."
  Problem: The box has the names reversed. Long and Sedley (1987) revived the idealist reading, and Sedley (2011) supports it. Konstan (2011) defends the realist reading. "Scott" cannot stand on the idealist side either. The only Scott that Sedley 2011 cites in this debate is Dominic Scott (Recollection and Experience, 1995, 190–201), whom he lists with Mansfeld 1993 among those who attempted to refute the idealist thesis. Sedley credits F. A. Lange (1866) with first sketching the idealist view.
  Replacement: "On the "realist" reading (Konstan) Epicurus' gods are atomic compounds living between worlds; on the "idealist" reading (Long and Sedley) they are thought-constructs, idealisations of the blessed life."
  (If "after Scott" is wanted, it goes with Konstan on the realist side, but no source here says that Konstan follows Scott.)
  Basis: Fish and Sanders 2011 introduction (link in finding 3); BMCR 2011.11.43 (Sedley restates the idealist position, the gods as "our own graphic idealisation of the life to which we aspire"; Konstan the realist position, the gods as "atomic compounds"); Sedley, "Epicurus' theological innatism", nn. 2–4, in the same volume.

## Confirmed
- DL 10.1: Gargettus, parents Neocles and Chaerestrate, Samian cleruchy, Athens at eighteen, Perdiccas' expulsion, Colophon (Hicks' Loeb)
- DL 10.2: philosophy at fourteen, Apollodorus on Hesiod's Chaos, return to Athens under Anaxicrates (307/6); module 2.1 reads Theogony 116 (greece/r-2.1.html)
- DL 10.8 (jellyfish), 10.13–14 (self-taught; Ariston on Nausiphanes and Pamphilus at Samos); Cicero, On the Nature of the Gods 1.72–73 (Cotta on Pamphilus and Nausiphanes)
- DL 10.10 (garden for eighty minae), 10.11 (no pooling of property, which implies mistrust), 10.15 (died at seventy-two, Ol. 127.2 = 271/0), 10.22 (last-day letter to Idomeneus); On Ends 2.96 addresses the letter to Hermarchus
- Will: birthday on 10 Gamelion, meeting on the twentieth, Metrodorus' children, four slaves freed (Mys, Nicias, Lycon, Phaedrium), Hicks' Loeb via Perseids https://fgh.perseids.org/read/greekLit/tlg0004/tlg001/perseus-eng2/10.1.21-10.1.40
- On Ends 5.3 (portrait on cups and rings); Pliny, Natural History 35.5 (twentieth-day feast); Seneca, Letters 25.5 ("act as if Epicurus were watching")
- DL 10.26 (about three hundred rolls), 10.27 (On Nature, thirty-seven books), 10.31–33 (criteria, dialectic superfluous, nothing refutes sensation, preconception and enquiry), 10.119 (no politics), 10.136–137 (the On Choices quotation; Cyrenaic differences; cradle argument), 10.138 (colophon), 10.139 (scholion on KD 1) (Perseids, as above)
- Letter spans in DL: Herodotus 10.35–83, Pythocles 10.84–116, Menoeceus 10.122–135, KD 10.139–154
- Letter to Herodotus 38–45, 50–51, 54, 56–59, 63–67; Letter to Pythocles 86–87; Letter to Menoeceus 123–135: all section references match the content cited
- KD 1–5, 14, 15, 17, 18, 19–20, 23, 27, 29 scholion (with its examples), 31–35, 37–38; SV 23, 33, 34, 40: content matches the numbers
- Vatican Sayings: found 1888 in a fourteenth-century Vatican manuscript (Vat. gr. 1950) that also contains Marcus Aurelius and Epictetus (https://wiki.epicurism.info/Vatican_Sayings); Wotke as discoverer from general knowledge
- On Nature 25: PHerc. 419, 1634, 697 (one copy), 1420, 1056, 1191 (https://lexicon.cnr.it/ojs/index.php/LP/article/download/103/120/2260); book 28 = PHerc. 1479/1417 (Puglia 1997, in the SPIDER bibliography)
- Tetrapharmakos: PHerc. 1005, column 5, matches Angeli's edition (Agli amici di scuola). The title survives only as "Philodemou Pros tous ...". Some older references number the column 4 (https://epicureanfriends.com/thread/1489-tetrapharmakos-alternate-translations-and-content-of-pherc-1005-from-reviews)
- Diogenes of Oinoanda, Smith numbering: fr. 3 (sunset of life, remedies of salvation), fr. 29 with KD 1 in the lower margin, fr. 30 (one country, the whole earth), fr. 34 (fears of gods, death and pains, desires beyond nature's limits: "the roots of all evils"), fr. 54 (free movement in atoms, which Democritus missed and Epicurus brought to light), fr. 56 (the life of the gods will pass to men) (https://texts.epicureanfriends.com/05-DiogenesOfOinoanda/)
- Oinoanda: Hadrianic on epigraphic grounds, about 25,000 words over about 260 m² (Smith), discovered 1884 (https://en.wikipedia.org/wiki/Diogenes_of_Oenoanda); Smith's Diogenes of Oinoanda: The Epicurean Inscription (1993), title consistent with his 2003 Supplement
- Pleasure box: Nikolsky, "Epicurus on Pleasure", Phronesis 46 (2001), derives the division from Academic doxography related to Carneades' division of ends, reaching Cicero probably through Antiochus; one pleasure described in two ways; Bailey and Rist on the traditional side; Gosling and Taylor (1982) the only earlier doubters (https://handbook.epicureanfriends.com/notes/Nikolsky.html)
- Gods box as it stands: names correct (see the 7.2 entry); Sedley 2011 and Konstan 2011 titles and dates correct (BMCR 2011.11.43)
- Swerve: Lucretius 2.216–293 (raindrops, free will); Cicero, On Fate 22–23 and On Ends 1.19; Letter to Menoeceus 134; SV 40 and On Nature 25 on self-refutation. Furley, Two Studies in the Greek Atomists (1967): minimal parts as a reply to Physics 6, and the swerve's limited role. Bailey 1928, and Sedley 1983 in ΣΥΖΗΤΗΣΙΣ, described correctly (general knowledge)
- Aetius 1.3.18 (weight added to Democritus' size and shape); Aetius 4.3.11 (fourfold soul, nameless element; LS 14C)
- Sextus, Against the Mathematicians 7.208–209 (the tower), 7.211–216 (attestation and contestation)
- On Ends: 1.22 (Cicero on Epicurus' logic), 1.29–72 (Torquatus' speech), 1.30 (cradle), 1.37–38, 1.65–70 (three accounts of friendship), 2.9–10, 2.31–32, 2.60–61 (Decius and "old Imperiosus", Torquatus' ancestor, in chapter 19: https://epicureanfriends.substack.com/p/episode-210-ciceros-on-ends-book-58e), 2.96–99
- On the Nature of the Gods 1.43–45 (Velleius on preconception), 1.49 (quasi corpus, quasi sanguis), 1.93 (Cotta on Leontion)
- Lactantius, On the Anger of God 13.20–21. Glei (Vigiliae Christianae 1988) denied the Epicurean attribution; Larrimore, citing him, suggests a sceptical source, perhaps Carneades, so "Academic source" stands (https://www.epicureanfriends.com/thread-pdf-export/2729/)
- Plutarch, Against Colotes, Moralia 1107d–1127e, and 1108f–1111e on Democritus; consistent with 12.1's use of 1108f–1109a
- Seneca, On the Happy Life 12–13; Dante, Inferno 10.13–15; Republic 358e–359b (Glaucon's contract)
- Pointers checked against targets: 7.2 (dates, garden, women and slaves, KD 1, the swerve-attribution question), 12.1 (Aristotle's complaint, Metaphysics 985b19–20; "Epicurus revised the system (module 12.6)"; B 9), 12.5 (hands DL 10.136–137 to 12.6), 6.5 (ring of Gyges, 359d–360b), 2.1 (Theogony 116), Rome 3.2 (Torquatus, On Ends 2.60–61), Rome 5.6 (reads Lucretius), Rome 13.3 prompt (villa, Philodemus, Piso, Cassius, Atticus)
- 12.7 points to 12.6 for pleasure as the Epicurean first object; 12.6's cradle argument covers it. 12.8's Carneades on the swerve is not duplicated
- House style: no em dashes, British spelling throughout, 10 self-test items, 3 carry-forward items, 4 dispute boxes each with named sides, Greek name forms (Oinoanda, with the Latin form given)
