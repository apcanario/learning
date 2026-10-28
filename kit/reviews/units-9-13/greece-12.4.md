# Greece 12.4: Aristotle

Verdict: fix
Body words: 3390 (target 3000)

## Coverage
- Life: Stagira: covered by the 6.5 pointer ("the frame, from Stagira in 384"); nothing added
- Twenty years in the Academy (dialogues, Protrepticus via Bywater, Plato's death): covered
- Assos and Lesbos (Hermias, Erastus and Coriscus, Pythias, the hymn, Theophrastus): covered
- Tutor to Alexander, pointed to 6.7 (Mieza); Callisthenes pointed to 11.5 and 11.7: covered (pointers true; nothing retold)
- The Lyceum (peripatos, 158 constitutions, Pythian list, pupils' histories, the will): covered
- Withdrawal to Chalcis: covered by the 6.5 pointer only (6.5 has the charge and Aelian 3.36); the hymn sentence links to it
- Corpus as lecture notes; Strabo 13.1.54, Plutarch, Sulla 26, Athenaeus 1.3a–b; Andronicus' edition and date: covered
- Logic and the syllogism (Categories, Prior and Posterior Analytics, Topics, endoxa): covered
- Physics and the four causes (four causes pointed to 6.5; change, nature, motion, place, time, void, teleology): covered
- Metaphysics on substance (Γ, Z, Θ) and the unmoved mover (Λ): covered
- Biology (History of Animals, Parts of Animals, Generation of Animals, Pyrrha lagoon): covered
- On the Soul: covered
- Nicomachean Ethics beyond the mean (eudaimonia, friendship, contemplative life): covered
- Politics (household, natural slavery, classification of constitutions): covered
- Poetics and Rhetoric: covered
- Afterlife: Arabic commentators and Aquinas: covered
- Lane: 6.5's four causes, biology observations, function argument and mean, six constitutions, katharsis dispute and life outline kept to pointers; 6.7's Mieza and 11.5/11.7's Callisthenes boxes not repeated: kept. But 6.5's Jaeger thesis, Scepsis doubt and break with Plato are not pointed back to (finding 4)
- Neighbours: 12.3 tells Aristotle's genealogy of the Forms and the unwritten doctrines; 12.4 tells neither. Shared dates (Plato's death 348/7, Academy from 367) agree with 6.5 and 12.3

## Findings
1. [error] [pointer] Section "Rhetoric and Poetics".
   Current: "calling it a knack (462b–465a; module 12.2)."
   Problem: Module 12.2 never treats the Gorgias' denial that rhetoric is an art. Its Gorgias citations are 472b–c, 474c–475e and 495a–499b (the elenchus, Polus and Callicles); the knack passage (462b–465a) appears in no Greek report. The pointer vouches for something its target does not hold.
   Fix: "calling it a knack (462b–465a)."
   Basis: greece/r-12.2.html, sections on the elenchus and the paradoxes (grep for "Gorgias"); Plato, Gorgias 462b–465a.

2. [should-fix] [accuracy] Section "The life beyond the outline", first dispute box.
   Current: "F. Nuyens (1939; French edition 1948) found the same three stages in the theory of the soul."
   Problem: Nuyens used Jaeger's method and found three stages of his own (Platonist dualism; an instrumentalist middle stage; the hylomorphism of On the Soul). But he put the History of Animals and Parts of Animals in the middle stage, not last. So on the biology, the point the box goes on to dispute, he sided with Lee against Jaeger. "The same three stages" makes him Jaeger's ally on exactly that point.
   Fix: "F. Nuyens (1939; French edition 1948) applied the method to the theory of the soul." (−2 words)
   Basis: S. Cantin's review of Nuyens, L'évolution de la psychologie d'Aristote, Laval théologique et philosophique 4 (1948), https://assets.erudit.tech/en/revue/ltp/1948/v4/n2/1019812ar.pdf. It sets out the initial, transitional and final periods and puts the History of Animals and Parts of Animals in the transitional period.

3. [should-fix] [attribution] Section "Metaphysics: substance and the unmoved mover", dispute box.
   Current: "Michael Woods (1967), Alan Code (1986) and Michael Loux (<em>Primary Ousia</em>, 1991) held that form is universal, shared by every man but predicated of matter rather than of individuals"
   Problem: "Predicated of matter rather than of individuals" is the view of Code (matter "has" form) and Loux (form universal over the parcels of matter it is predicated of). Woods' solution is different: form is universal but not "said universally" (katholou legomenon), so Z13 does not exclude it. The sentence gives Woods an argument he did not make.
   Fix: "Alan Code (1986) and Michael Loux (<em>Primary Ousia</em>, 1991) held that form is universal, shared by every man but predicated of matter rather than of individuals" (−3 words)
   Basis: S. Marc Cohen, Z13 lecture handout, https://faculty.washington.edu/smcohen/433/Z13Lecture.pdf (Woods [1967]: "Forms are universals (but are not spoken of universally)"; Code [1986]: "Form is universal with respect to matter"; Loux [1991]: "universal in relation to the parcels of matter it is predicated of").

4. [should-fix] [pointer] Sections "The life beyond the outline" (dispute box), "Lecture notes and the cellar at Scepsis" and "Logic: categories, syllogism, demonstration".
   Current: "Werner Jaeger (<em>Aristoteles</em>, 1923) mapped the corpus on to the life" / "Most now read the treatises as courses revised over decades, which no single chronology fits." / "Strabo (13.1.54) tells how they came down." / "Its ontology is anti-Platonic:"
   Problem: The prompt names Andronicus' edition with the doubted Scepsis cellar, the break with Plato and Jaeger's developmental thesis among what 6.5 already gives, and says "point back to it for each". The report points back for the life, four causes, biology, ethics, Politics and Poetics, but not for these three. The box's closing sentence also restates 6.5's own conclusion ("recent scholarship treats them as concurrent inquiries").
   Fix: "Werner Jaeger (<em>Aristoteles</em>, 1923; module 6.5) mapped the corpus on to the life" / "Most now read the treatises as courses revised over decades." / "Strabo (13.1.54; module 6.5) tells how they came down." / "Its ontology is anti-Platonic (module 6.5):" (net +1 word)
   Basis: greek-syllabus.html, prompt 12.4; greece/r-6.5.html, section "Aristotle" (break with Plato, Andronicus) and its closing dispute box (Jaeger; Scepsis "doubted, since Hellenistic authors knew some of them").

5. [minor] [style] Section "Rhetoric and Poetics".
   Current: "Umberto Eco's <em>The Name of the Rose</em> (1980)"
   Problem: English title with the Italian edition's date. The English translation (William Weaver) is 1983. AGENT-SPEC wants the title and date of a single edition.
   Fix: "Umberto Eco's <em>Il nome della rosa</em> (1980)" (−1 word)
   Basis: Il nome della rosa, Bompiani, 1980; The Name of the Rose, trans. W. Weaver, 1983 (standard bibliographic facts).

6. [minor] [register] Section "Self-test", question 5.
   Current: "The treatises use dialectic to reach and test principles that demonstration cannot prove."
   Problem: The body never says dialectic reaches principles. It gives first principles to induction and <em>nous</em> (Posterior Analytics 2.19) and shows dialectic only in how the treatises open, with appearances and puzzles. The answer adds a claim the reader cannot check against the body. Self-test text does not count toward the body.
   Fix: "The treatises use dialectic to set out the appearances and puzzles; first principles themselves are grasped by induction and <em>nous</em>."
   Basis: body, section "Logic: categories, syllogism, demonstration", third paragraph.

Net effect of fixes on body words: −7 (3390 to about 3383).

## Confirmed
- Andronicus' date: Moraux 1973 "late 70s", Gottschalk 1987 "perhaps in the 60s", Düring 1957 after Cicero's death from Cicero's silence (SEP "Commentators on Aristotle", supplement, Spring 2016 archive, https://plato.stanford.edu/archives/Spr2016/entries/aristotle-commentators/supplement.html)
- Barnes, "Roman Aristotle" (1997), among those who argue that both stories (Strabo's cellar, Athenaeus' sale) can be right (R. Janko, SCS abstract, "Aristotle's Manuscripts and the Fate of his Library", https://classicalstudies.org/annual-meeting/155/abstract/aristotle%E2%80%99s-manuscripts-and-fate-his-library)
- Primavesi, Philologus 151 (2007): a modified Strabo; the treatises keep the pre-Hellenistic 24-letter book labels; those absent from the Hellenistic catalogue came from a collection out of circulation until about 100 BC (De Gruyter abstract, https://www.degruyterbrill.com/document/doi/10.1515/phil-2007-0105/html)
- Athenaeus 1.3a–b: Neleus sold to Ptolemy Philadelphus for Alexandria (Janko abstract; standard text)
- Plutarch, Sulla 26: Tyrannion arranged the books, Andronicus got copies, published them and drew up the current tables; Porphyry, Life of Plotinus 24 on Andronicus dividing the works into treatises (standard texts)
- Strabo 13.1.54: Neleus' heirs, the trench, Attalid collecting, Apellicon's faulty copies, Sulla, Tyrannion, the later Peripatetics declaiming theses (standard text)
- Strabo 13.1.57: Hermias sent for Aristotle and Xenocrates and married his brother's daughter to Aristotle (https://people.well.com/user/aquarius/strabo.htm); Diogenes Laertius 5.3 "daughter or niece"
- FD III 1.400: decree to praise and crown Aristotle and Callisthenes for the Pythian victor list, dated "ante 329" (https://poetivaganti.chs.harvard.edu/?p=9869)
- Aelian, Varia Historia 14.1: Aristotle's letter to Antipater on losing the Delphic honours (Stanley's translation, https://penelope.uchicago.edu/aelian/varhist14.html)
- Diogenes Laertius 5.7–8 (hymn to Virtue naming Hermias), 5.11–16 (will: Antipater executor, Herpyllis provided for) (https://fgh.perseids.org/read/greekLit/tlg0004/tlg001/perseus-eng2/5.1.6-5.1.20); 5.2 peripatos; 5.27 constitutions of 158 cities; 5.22–27 catalogue
- History of Animals: "the star-fish is a great pest in the Strait of Pyrrha" (https://www.ellopos.net/elpenor/greek-texts/ancient-Greece/aristotle/history-animals-b.asp?pg=19)
- Hardie 1965 dominant against inclusive end, Aristotle's position dominant but his exposition confused (https://ojs.sites.ufsc.br/index.php/peri/article/view/5264/4806); Ackrill 1974; Kraut 1989
- Jaeger, Aristoteles (1923), three stages with the biology in the Lyceum years; Lee, CQ 42 (1948) on biological place-names; Owen 1960 ("Logic and Metaphysics in Some Earlier Works of Aristotle"), anti-Platonist early logic and coining "focal meaning"; Owen, "Tithenai ta phainomena" (1961)
- Łukasiewicz 1951; Corcoran 1974; Smiley 1973; Sedley, Phronesis 1991; Sorabji 1974 against Burnyeat 1992; Frede and Patzig 1988 (particular forms); Janko 1984 on the Tractatus Coislinianus; Rhodes 1981 on the Athenaion Politeia; Leroi, The Lagoon (2014); Düring 1957; Bywater 1869
- Bekker references the writer flagged, checked against the passages described: Parts of Animals 639b11–21; Generation of Animals 729a9–11, 736b27–28, 737a27–28; Politics 1260a12–14, 1254b27–1255a1, 1281a40–b10, 1293b33–34, 1328b33–1329a2; Metaphysics 1006a11–24, 1041b27–28; Nicomachean Ethics 1101a6–8, 1160a31–1161a9 (8.10); Sophistical Refutations 184b1–3. The other Bekker, Stephanus and Summa references match their passages too (Categories 1b25–27, 2a11–19, 2b5–6; Prior Analytics 24b18–20, 25b37–39; Posterior Analytics 71b19–22; Topics 100b21–23; Physics 192b21–23, 201a10–11, 212a20–21, 219b1–2, 200a10–13; Metaphysics 1003a33–b10, 1005b19–20, 1028b2–4, 1028b33–36, 1029a10–28, 1038b8–12, 1049b4–5, 1071b3–22, 1072b3, 1074b34–35, 1075a11–15; On the Soul 412a27–b6, 424a17–24, 429a24, 430a1, 430a10–25; NE 1097a25–b21, 1098a18–20, 1155a22–26, 1166a31–32, 1169b33–1170a4, 1174b31–33, 1177b33, 1178a9–10; Rhetoric 1354a1, 1355b25–26, 1378a30–32; Poetics 1448b4–19, 1451b5–11; Gorgias 462b–465a; Summa Theologiae I q.2 a.3, I q.46 a.2)
- Pointers true: 6.7 (Mieza, 343 to about 340), 11.5 and 11.7 (Callisthenes), 7.3 (Sulla ships Apellicon's library), 7.4 (Marcus Aurelius' chairs of 176), 9.3 (Hunayn, Baghdad, Toledo), 12.1 (Physical Opinions; Aristotle's answer to Parmenides, Physics 191a23–b34); 12.7, 12.8 and Rome 13.3 fit their prompts
- Inferno 4.131 and 4.144; Kant, B viii (1787); Paris 1210 and 1215, statutes of 1255, Tempier's 219 propositions of 1277; Aquinas, On the Unity of the Intellect (1270)
