# Rome 12.1: Virgil and the making of the poem

Verdict: fix
Body words: 3696 (target 2500; the target is a guide, rule of 27 October 2026, no cut asked)

## Coverage
- Virgil's life as Donatus and Servius give it, and how much is inference from the poems: covered
- The *Eclogues* as a book: covered
- The fourth *Eclogue*'s child and the candidates (with module 5.5's Brundisium dating): covered
- The *Georgics* as a didactic poem and its models (Hesiod, Aratus, Lucretius): covered
- The prose draft in twelve books (*Life* 23): covered
- The bear licking its cubs (*Life* 22 for the *Georgics*, Gellius 17.10 for his verse in general): covered, with the prompt's distinction kept
- The reading of books 2, 4 and 6 to Augustus and Octavia: covered
- The unfinished half-lines: covered
- The deathbed wish to burn the manuscript and publication by Varius and Tucca: covered
- The poem's models (Homer, Apollonius, Ennius, Naevius, Lucretius, Greek tragedy): covered
- The metre: covered
- Reading in translation, comparing Dryden, Fitzgerald, Fagles, Ahl, Ruden, Bartsch: covered
- Pointers back to module 6.3: confiscations (covered), *Georgics* passages on Caesar (covered), Atella (covered), Servius' Gallus story (covered); Maecenas and the patronage of poets: missing (see finding 2)

## Findings
1. [error] [accuracy] Section "The order to burn it" (and the flow figure).
   Current: "In 19, aged fifty-two, Virgil set out for Greece and Asia"
   Problem: Donatus, *Life* 35, says *anno aetatis quinquagesimo secundo*, "in his fifty-second year", an ordinal, not an age; and on the report's own dates (born 15 October 70, travelling in summer 19) Virgil was fifty. "Aged fifty-two" contradicts the first section. The flow figure repeats it in the step label "Journey to Greece, aged fifty-two".
   Fix: "In 19, in what Donatus calls his fifty-second year, Virgil set out for Greece and Asia"; and in the flow figure's JSON replace "Journey to Greece, aged fifty-two" with "Journey to Greece, 19 BC".
   Basis: Durham "Vita Suetonii vulgo Donatiana", §35, *anno aetatis quinquagesimo secundo* (https://livingpoets.dur.ac.uk/w/index.php/Vita_Suetonii_vulgo_Donatiana); Rolfe on LacusCurtius, §35 (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Suetonius/de_Poetis/Vergil*.html).

2. [should-fix] [lane] Section "The Georgics: a didactic poem and its models".
   Current: "and dedicated to Maecenas, teach farming"
   Problem: The prompt says module 6.3 already covers Maecenas and the patronage of poets and asks for a pointer back for each item. The report points back for the confiscations, the Caesar passages, Atella and Gallus, but never for Maecenas or patronage (Pollio appears only as the giver of Alexander and the consul of *Eclogue* 4).
   Fix: "and dedicated to Maecenas (module 6.3 covers him and the patronage of poets), teach farming"
   Basis: prompt 12.1 in `roman-syllabus.html`; `rome/r-6.3.html`, section "Maecenas and the friendship of poets", which covers Maecenas, Pollio and patronage.

3. [should-fix] [attribution] Section "The order to burn it", dispute box on the Helen episode.
   Current: "Nicholas Horsfall's commentary (<em>Virgil, Aeneid 2</em>, 2008) adds that they clash with Deiphobus' account of Helen in the underworld (6.494–547)."
   Problem: The clash with Deiphobus' account is not Horsfall's addition: Servius himself gives it as one of the reasons the lines were cut, and it was the standard objection long before 2008. "Adds" credits Horsfall with the argument. Horsfall 2008 is rightly on the "against" side.
   Fix: "Nicholas Horsfall's commentary (<em>Virgil, Aeneid 2</em>, 2008) also rejects them, pressing the clash with Deiphobus' account of Helen in the underworld (6.494–547) that Servius already gives as a reason for the cut."
   Basis: CAMWS 2016 abstract "Blaming Helen: Inconsistency in Aeneid 6 and Odyssey 24" (the clash is "one of two objections Servius claimed led to the episode's excision"; Horsfall 2008 listed among arguments against; Bleisch 1999 on 6.494–547) (https://camws.org/sites/default/files/meeting2016/118.BlamingHelenInconsistency.pdf).

4. [should-fix] [figure] Timeline figure caption.
   Current: "Atella from <em>Life</em> 27"
   Problem: The text never cites *Life* 27; it points to module 6.3 for Atella. A caption names the passage the text cites (R-1 figure lesson).
   Fix: in the text, after "Module 6.3 has the reading to Octavian at Atella in 29" add " (<em>Life</em> 27)"; the caption can then stand. (Or change the caption to "Atella from module 6.3".)
   Basis: the report's text against its caption; `rome/r-6.3.html` cites Donatus, *Life* 27 for Atella.

5. [should-fix] [figure] Flow figure, step "Varius and Tucca edit at Augustus' order".
   Current: "Life 37, 40–41"
   Problem: The text cites *Life* 40 (the will) and 41 (publication at Augustus' wish), never *Life* 37. The figure names a passage the text does not.
   Fix: "Life 40–41"
   Basis: the report's text against the figure declaration; *Life* 37 (heirs; Varius and Tucca revise at Augustus' order) exists, but is not in the text (LacusCurtius summary, URL as in finding 1).

6. [minor] [accuracy] Section "The ancient lives and what they rest on".
   Current: "His father was a potter, or more probably a hired man who married his employer's daughter"
   Problem: *Life* 1 reads *quem quidam opificem figulum, plures Magi cuiusdam viatoris initio mercennarium*: "some" say a potter, "more" say a hired man. Donatus counts reports; "more probably" turns the count into a judgement of likelihood.
   Fix: "His father was a potter, some said, or, as more said, a hired man who married his employer's daughter"
   Basis: Durham text, §1 (URL as in finding 1).

7. [minor] [accuracy] Section "The ancient lives and what they rest on".
   Current: "took the toga of manhood on his fifteenth birthday, in 55, under the same two consuls (<em>Life</em> 6)"
   Problem: The Latin as printed in the Durham text reads *XVII anno natali suo*; fifteen is what the consuls of 55 imply, and Rolfe's version gives it. The report notes the parallel variant at *Life* 25 but not here.
   Fix: "took the toga of manhood on his fifteenth birthday, in 55, under the same two consuls (<em>Life</em> 6; the transmitted numeral is seventeen, the consuls give fifteen)"
   Basis: Durham text, §6, *XVII anno natali suo accepit isdem illis consulibus iterum duobus, quibus erat natus*; LacusCurtius summary of Rolfe, §6, "at fifteen" (URLs as in finding 1).

8. [minor] [style] Section "Making the Aeneid".
   Current: "to the Miseno passage (6.164–165; <em>Life</em> 34)"
   Problem: "Miseno" is a Latin case form; the English name of the trumpeter is Misenus.
   Fix: "to the passage on Misenus (6.164–165; <em>Life</em> 34)"
   Basis: *Aeneid* 6.162–165; Donatus, *Life* 34.

9. [minor] [accuracy] Section "The order to burn it", dispute box.
   Current: "No manuscript of Virgil has it; it survives only through Servius"
   Problem: The lines are absent from the ancient capital manuscripts and the main Carolingian ones, but a few late medieval manuscripts carry them, taken from Servius. "No manuscript" overstates.
   Fix: "None of the ancient or principal medieval manuscripts has it; it survives through Servius"
   Basis: not checked by search; from knowledge of the apparatus at 2.567 (Mynors' OCT).

10. [minor] [register] Self-test, question 4.
    Current: "the expected child of Antony and Octavia after Brundisium (Clausen, 1994)"
    Problem: The question asks who proposed each candidate; the body says Clausen "makes the strongest case" for this child, not that he proposed it (the identification is older). The answer should match the body.
    Fix: "the expected child of Antony and Octavia after Brundisium (argued most fully by Clausen, 1994)"
    Basis: the report's own dispute box; Wikipedia "Eclogue 4" gives the Antony–Octavia identification to "other scholars" without Clausen as originator (https://en.wikipedia.org/wiki/Eclogue_4).

## Confirmed
- Donatus, *Life* 2: born on the Ides of October, first consulship of Pompey and Crassus, at Andes near Mantua (LacusCurtius; Durham).
- *Life* 6–7: boyhood at Cremona to the toga, then Milan and Rome (LacusCurtius).
- *Life* 8, 11, 16: tall, dark, rustic, poor health; "Parthenias" at Naples; slow of speech, from Melissus (Durham; LacusCurtius).
- *Life* 9: Alexander, Pollio's gift, the Alexis of *Eclogue* 2 (LacusCurtius).
- *Life* 17–18: the juvenilia list (Catalepton, Priapea, Epigrams, Dirae, Ciris, Culex) (LacusCurtius).
- *Life* 19–20: the farm and the veteran; *Georgics* for Maecenas (LacusCurtius).
- *Life* 21: a work matching both Homeric poems, with Rome's and Augustus' origins (LacusCurtius).
- *Life* 22: the she-bear simile told of the *Georgics*; *Life* 23: prose draft in twelve books, versified in no fixed order; *Life* 24: the struts (LacusCurtius).
- *Life* 25: *Bucolica triennio, Georgica VII, Aeneida XI*; Rolfe's version twelve; the report's note of the variant is right (Durham; LacusCurtius).
- *Life* 31: *expeditione Cantabrica*, asking for the first outline (*hypographe*) or any section (*kolon*) (Durham).
- *Life* 32: three books, 2, 4 and 6, "much later"; Octavia fainted at *tu Marcellus eris* (Durham; LacusCurtius).
- *Life* 33, 34: small readings; Eros and the two half-lines *quo non praestantior alter*, *Martemque accendere cantu* (LacusCurtius).
- *Life* 35: met Augustus at Athens, fever at Megara, death at Brundisium a few days later, XI Kal. Oct. (21 September), consuls Sentius and Lucretius (Durham).
- *Life* 36: burial on the road to Puteoli; the epitaph's Latin as quoted (Durham).
- *Life* 38 (Sulpicius of Carthage), 39 (Varius refused; the book-boxes), 40 (the will's condition), 41 (light correction, half-lines left, *quem tibi iam Troia* the exception), 42 (Nisus: two books reordered, opening lines removed) (LacusCurtius; Durham).
- *Life* 46: Hercules' club answer (LacusCurtius).
- Horsfall 1995 (*A Companion to the Study of Virgil*, p. 4) treats the life as "not biographical fact, as we understand it" (SCS abstract "Between Biography and Commentary", https://classicalstudies.org/between-biography-and-commentary-ancient-horizon-expectations-virgil%E2%80%99s-vita).
- Austin, "Virgil, *Aeneid* 2.567–88", *CQ* 11 (1961) for authenticity; Goold, "Servius and the Helen Episode", *HSCP* 74 (1970) against; Horsfall 2008 against; Deiphobus scene 6.494–547 (CAMWS 2016 abstract).
- Bartsch: Profile Books, UK, November 2020; Random House, US, February 2021; no added lines, no more than six feet a line (BMCR 2021.04.22, https://bmcr.brynmawr.edu/?p=62415; UChicago News, https://news.uchicago.edu/story/new-aeneid-translation-channels-vergils-pure-latin).
- Fitzgerald's opening "I sing of warfare and a man at war." quoted exactly (New Criterion, "Arms & the age", https://newcriterion.com/article/arms-the-age/). Dryden's line and Fagles' "Wars and a man I sing" match the published openings (from knowledge). All three modern quotations are a single short phrase; none runs to a passage.
- Clausen, *A Commentary on Virgil, Eclogues* (Oxford, 1994) favours the Antony–Octavia child; Wikipedia "Eclogue 4" lists that candidate and Clausen's Hercules reading of *pacatum*.
- Pointers: module 6.3 (confiscations, Caesar passages 1.498–514, 3.10–48, 4.559–566, Atella with *Life* 27, Servius' Gallus story, Propertius 2.34.65–66) says what is claimed; module 5.5 places *Eclogue* 4 in the season of Brundisium, autumn 40, Antony's marriage to Octavia; module 10.1 has *deductum carmen* (*Eclogue* 6.5) and the "little *Aeneid*" (13.623–14.608); module 10.2 has Lucan's anti-*Aeneid* and Statius; module 4.5 and Greek module 10.12 have Naevius' Aeneas and Ennius' hexameter, and Greek 10.12 Macrobius on Naevius' storm and Venus' complaint; Greek module 2.4 has the Five Ages; Greek modules 3.4 and 7.2 have Apollonius; module 5.6 has Lucretius; Greek modules 4.2 and 4.4 the *Iliad* and *Odyssey*. Pointers to unwritten modules match their prompts: 12.4 (Dido), 12.5 (Anchises' doctrine), 12.7 (the ending, 12.950–952, and the optimist/pessimist split), 12.8 (the Christian reading of *Eclogue* 4; Dryden's translation as reception); 12.2 and 12.3 (book by book).
- Citations confirmed from knowledge: *Eclogues* 4.1, 4.4–7, 4.11, 6.1, 6.4–5, 9.47; Aratus, *Phaenomena* 96–136; Catullus 64.323–381, 66.39 (and *Aeneid* 6.460); *Georgics* 1.121–146 (*labor omnia vicit improbus* 1.145–146), 2.136–176, 2.176, 2.490–494, 3.478–566, 4.147–148; Lucretius 6.1138–1286; Quintilian 10.1.56; Seneca, *Letters* 86.15; Pliny, *Natural History* 7.114; Gellius 17.10; Macrobius, *Saturnalia* 1.24.11, 6.2; Servius on 4.1 (book 4 from Apollonius 3) and on *Eclogue* 4.11 (Asconius and Asinius Gallus); *Aeneid* 1.534, 2.66, 3.255–257, 3.340, 3.658, 4.469–473, 5.835–871, 6.164–165, 6.347–361, 6.846, 6.883, 7.122–127, 8.596, 12.435–436, 12.951; Ennius' *unus homo* line in Cicero, *On Old Age* 10; Sophocles, *Ajax* 550–551; Statius, *Thebaid* 12.816–817; Tarn, *JRS* 1932; Norden, *Die Geburt des Kindes* (1924); Knauer (1964); Sparrow (1931); Jackson Knight (1939); Wilkinson (1969); Thomas (1988); Armstrong and others (2004).
- Scansion of 1.1 as given (two dactyls, two spondees, a dactyl, a closing foot; caesura after *cano*) is right.
- House style: no em dashes; British spelling ("labor" flagged by `check.py` is the Latin *labor*); Octavian for 29, Augustus from 26 on; Cicero's treatise in English.
