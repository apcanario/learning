# Rome 12.5: Book 6 of the Aeneid

Verdict: fix
Body words: 5271 (target 2500; advisory only under the 27 October rule, no cut asked)

## Coverage
- Cumae, the Sibyl and the golden bough: covered
- The descent, the monsters at the entrance and Charon: covered
- Palinurus, the unburied and the fields of mourning (Dido's meeting handed to module 12.4): covered
- Deiphobus: covered
- Tartarus and its sinners: covered
- Elysium and Musaeus: covered
- Anchises' doctrine of the world-soul and rebirth, with Platonic and Pythagorean sources: covered (Stoic and Lucretian strands added)
- Parade of heroes from the Alban kings, pointing back to module 6.3 for Augustus, Brutus, Caesar and Pompey, Marcellus: covered
- Anchises' charge, the arts left to others, 6.847–853: covered
- Gates of horn and ivory (6.893–898) and the arguments over the exit: covered
- Comparisons with *Odyssey* 11, pointing back to Greek modules 4.4 and 10.7: covered
- The book's afterlife in Dante: covered
- Lane note: 2.4 ("Greek in plan") kept and answered; 3.5 (6.836–840 as Perseus, the Ennian oracle) kept without retelling; 6.3 (the precept, 6.851–853) taken up in full: all kept
- Successors pointed to modules 10.1 (Ovid) and 10.2 (Lucan, Silius): covered

## Findings
1. [error] [accuracy] Section "Elysium, Musaeus and Anchises' doctrine".
   Current: "the founders of Troy, Ilus, Assaracus and Dardanus, keep their chariots and arms and feast in a laurel grove where the Eridanus rises (6.648–659)"
   Problem: Those who feast and sing the paean in the laurel grove are "others" (*conspicit, ecce, alios … vescentis*, 6.656–658), not the Trojan founders, whose part ends with the chariots, arms and horses (6.651–655).
   Fix: "the founders of Troy, Ilus, Assaracus and Dardanus, keep their chariots and arms, and others feast and sing a paean in a laurel grove where the Eridanus rises (6.648–659)"
   Basis: Virgil, *Aeneid* 6.648–659 (Mynors), checker's reading of the Latin; not searched.

2. [error] [accuracy] Bibliography file `bibliography/rome/r-12.5.md`, "Modern works".
   Current: "William Everett, "Upon Virgil, *Aeneid* VI., vv. 893–898", *Harvard Studies in Classical Philology* 11 (1900) 153–155."
   Problem: The article appeared in *The Classical Review*, not *HSCP*. The report body ("William Everett (1900)") is right; only the bibliography entry is wrong.
   Fix: "William Everett, "Upon Virgil, *Aeneid* VI., vss. 893–898", *Classical Review* 14 (1900) 153–154."
   Basis: Cambridge Core record, *Classical Review* 14.3 (April 1900) 153–154, https://www.cambridge.org/core/journals/classical-review/article/upon-virgil-aeneid-vi-vss-893898/3EF0ED57E7F8A347734D23D58C2DDAFA; also cited so in the Sydney article on the gates, https://openjournals.library.sydney.edu.au/SSSC/article/view/7327/7746.

3. [should-fix] [pointer] Section "The gates of horn and ivory", dispute box.
   Current: "The political readings belong to deep dive module 12.7."
   Problem: Module 12.7 does not take the political readings of the gate; it mentions the gate once, after Marcellus, and hands the question back here ("module 12.5 weighs why"). The two pointers are circular. The box also runs to six sentences against the two to four of the quality bar.
   Fix: "Deep dive module 12.7 sets the exit beside Marcellus in the debate over the poem's politics."
   Basis: `rome/r-12.7.html`, section "Test cases: Marcellus, the shield and Dido" ("a few lines later Aeneas leaves the underworld by the gate of false dreams (6.893–898; module 12.5 weighs why)").

4. [should-fix] [pointer] Section "Book 6 in Dante's Inferno".
   Current: "Anchises' cleansing by wind, water and fire is nearer to Dante's Purgatory, whose reading belongs with the rest of the reception in deep dive module 12.8."
   Problem: Module 12.8 reads *Purgatorio* only for Statius, Beatrice and the Marcellus lilies; it says nothing of purgation or of book 6's doctrine, so the pointer promises a reading that is not there.
   Fix: "Anchises' cleansing by wind, water and fire is nearer to Dante's Purgatory, up whose mountain Virgil leads Dante in deep dive module 12.8."
   Basis: `rome/r-12.8.html`, section "Dante's guide" (Virgil "leads through Hell and up the mountain"; *Purgatorio* 21.97–98, 22.67–73, 30.21, 30.48–51; nothing on purgation).

5. [minor] [register] Section "Elysium, Musaeus and Anchises' doctrine", dispute box "Does every soul return?".
   Current: "On the first reading the Romans of the parade, coming to Lethe, are souls not yet pure, a consequence some readers draw on their way to a darker reading of the book."
   Problem: An unnamed "some readers" view, and the fifth sentence of a box the quality bar keeps to two to four.
   Fix: delete.
   Basis: the quality bar's dispute boxes (`greece/r-6.3.html`); AGENT-SPEC, "Dispute boxes name a source or scholar on each side".

6. [minor] [accuracy] Section "The descent: the threshold, Charon and the unburied".
   Current: "The leaves descend from Glaucus' generations of men (<em>Iliad</em> 6.146–149) by way of Bacchylides, whose Heracles saw the shades beside the Cocytus like leaves shaken on Ida (Bacchylides 5)."
   Problem: "By way of Bacchylides" states a line of descent as fact. Whether Virgil read Bacchylides is uncertain; Clark (2001), with Norden and Lloyd-Jones, derives the Cocytus simile from a common lost account of Heracles' descent.
   Fix: "The leaves descend from Glaucus' generations of men (<em>Iliad</em> 6.146–149), and Bacchylides had already set them beside the Cocytus, where his Heracles saw the shades like leaves shaken on Ida (Bacchylides 5)."
   Basis: R. J. Clark, *PCPS* 47 (2001) 103–116, n. 34 as summarised on the Cambridge Core page, https://cambridge.org/core/journals/cambridge-classical-journal/article/how-vergil-expanded-the-underworld-in-aeneid-6/30C8C715A4D911B856AF734FF30B9F93.

7. [minor] [accuracy] Section "Book 6 in Dante's Inferno".
   Current: "where Virgil's boat sinks under Aeneas' weight"
   Problem: The boat does not sink: it groans and ships water through its seams (6.413–414), as the report itself says earlier.
   Fix: "where Virgil's boat groans and ships water under Aeneas' weight"
   Basis: *Aeneid* 6.413–414; the report's own section "The descent: the threshold, Charon and the unburied".

8. [minor] [attribution] Section "Cumae, the Sibyl and the golden bough".
   Current: "the oldest Greek city in Italy (module 0.2 gives the site)"
   Problem: Pithecusae on Ischia is older; "oldest" is Strabo's claim (5.4.4), which module 0.2 attributes to him.
   Fix: "the oldest Greek city in Italy, Strabo says (5.4.4; module 0.2 gives the site)"
   Basis: `rome/r-0.2.html`, table row on Cumae ("The oldest Greek city in Italy (Strabo 5.4.4)").

9. [minor] [lane] Section "Book 6 and Odyssey 11".
   Current: "The differences are at the root."
   Problem: Module 12.2 already gives this contrast in nearly the same words ("changed at the root: Odysseus calls the dead up to a trench of blood, Aeneas goes down bodily, and where Tiresias tells one man how to get home, Anchises shows a people its history"), and Self-test 3 repeats it. Developing it here is right, but the report should say it is taking 12.2's sentence further.
   Fix: "Deep dive module 12.2 gives the difference at the root in a sentence; it runs through the whole book."
   Basis: `rome/r-12.2.html`, book 6 outline.

10. [minor] [style] Pointers throughout.
   Current: "the clash between his two accounts is module 12.1's"; "one reason for doubting those lines (module 12.1)"; "teaches the opposite, an immortal soul (module 12.1)"; "Ennius' line turned to the second person (6.841–846; module 12.1)"; "Octavia's fainting at the reading is told in module 12.1"; "which becomes Dido's silence (module 12.4)"; "Sychaeus' ashes (<em>Inferno</em> 5.61–62; module 12.4)"; "Dido's meeting is module 12.4's" (figure caption)
   Problem: AGENT-SPEC refers to deep dives as "deep dive module 12.x"; the report uses that form elsewhere (12.2, 12.4, 12.6, 12.7, 12.8) but drops it in these places.
   Fix: insert "deep dive " before "module 12.1" and "module 12.4" in each.
   Basis: AGENT-SPEC, Rome course conventions.

11. [minor] [pointer] Section "Elysium, Musaeus and Anchises' doctrine".
   Current: "Anchises' <em>principio</em> opens as a Lucretian lesson opens and teaches the opposite, an immortal soul (module 12.1)."
   Problem: Module 12.1 says only that Anchises' account "answers Lucretian mortalism" and hands it here (deep dive module 12.5); it does not have the *principio* point. The pointer is true of the general claim, not of the detail.
   Fix: "Anchises' <em>principio</em> opens as a Lucretian lesson opens and teaches the opposite, an immortal soul, as deep dive module 12.1 notes in handing the passage here."
   Basis: `rome/r-12.1.html`, section on the poem's models (Lucretius).

12. [minor] [style] Section "Self-test", question 3.
   Current: "How does Book 6 change the situation"
   Problem: Lower case "book 6" everywhere else in running text.
   Fix: "How does book 6 change the situation"
   Basis: house usage in the report.

13. [minor] [accuracy] Bibliography file, Segal entry.
   Current: "Charles Segal, "*Aeternum per saecula nomen*: The Golden Bough and the Tragedy of History", *Arion* 4 (1965) 617–657 and 5 (1966) 34–72."
   Problem: The report says "articles of 1965–68"; the bibliography stops at 1966. The 1968 article, the one most directly on the hesitation (cited as Segal 1968, pp. 75, 77–78, in the Wikipedia summary the writer used), is missing.
   Fix: add the 1968 article with its title and journal once confirmed (believed to be "The Hesitation of the Golden Bough: A Reexamination", *Hermes* 96 (1968) 74–79; not confirmed by search).
   Basis: Wikipedia, "Golden Bough (Aeneid)", https://en.wikipedia.org/wiki/Golden_Bough_(Aeneid); title and journal not checked: the search did not return a record.

14. [minor] [register] Section "The gates of horn and ivory", dispute box.
   Current: "<aside class="dispute"><strong>Where sources disagree.</strong> Why the ivory gate? Servius takes"
   Problem: Six sentences (five after finding 3's replacement if the question stays), against the two to four of the quality bar.
   Fix: "<aside class="dispute"><strong>Where sources disagree.</strong> Servius takes"
   Basis: the quality bar's dispute boxes.

## Confirmed
- Norden (1903) took an eschatological work of Posidonius as the source for Cicero and Virgil; later scholars put the ideas in the Platonic tradition: *Rheinisches Museum* article, n. 7, https://journals.ub.uni-koeln.de/index.php/rhm/article/download/9633/9851/20958
- Everett (1900) argued that false dreams came before midnight, so the ivory gate gives the hour; Norden followed him in the 1926 edition (Berlin, p. 348): N. Reed, "The Gates of Sleep in *Aeneid* 6", *CQ* 1973, https://www.cambridge.org/core/journals/classical-quarterly/article/gates-of-sleep-in-aeneid-6/54A8025F0E96006ADB42E486DE070A90
- Austin (1977, p. 276): Aeneas and the Sibyl, not *verae umbrae*, cannot use the horn gate; Otis, "Three Problems of *Aeneid* 6", *TAPA* 90 (1959) 165–179, the exit marks a dream needing interpretation; Boyle, *The Chaonian Dove* (Brill, 1986) 142–145, Anchises' promises "cruel lies"; Servius on 6.893, the episode false: Sydney article, https://openjournals.library.sydney.edu.au/SSSC/article/view/7327/7746
- Bartsch, "Ars and the Man: The Politics of Art in Virgil's *Aeneid*", *CP* 93 (1998) 322–342, the ivory gate casts an ominous pall: https://en.wikipedia.org/wiki/Gates_of_horn_and_ivory
- Servius tried to discredit the reading of the hesitation as a sign against Aeneas; Thomas, *Virgil and the Augustan Reception* (2001) 99–100, infers it was already current; Brooks, "Discolor aura" (1953); Segal 1965 and 1968; Servius links the bough to the rex Nemorensis; Frazer 1890: https://en.wikipedia.org/wiki/Golden_Bough_(Aeneid)
- Conington: the lines "among the hardest in Virgil"; Page: all souls reborn; Williams, Austin and others: the pure souls remain in Elysium: McIntosh, CAMWS 2005 abstract, https://camws.org/meeting/2005/abstracts2005/mcintosh.html
- Clark, "How Vergil Expanded the Underworld in *Aeneid* 6", *PCPS* 47 (2001) 103–116; Norden's lost katabasis of Heracles; Lloyd-Jones' support for an early epic of the descent (P.Oxy. 2622; about 550 BC): Cambridge Core, https://cambridge.org/core/journals/cambridge-classical-journal/article/how-vergil-expanded-the-underworld-in-aeneid-6/30C8C715A4D911B856AF734FF30B9F93
- Servius on 6.609 preserves the Twelve Tables' *patronus si clienti fraudem fecerit, sacer esto*: Lewis and Short s.v. *cliens*, https://alatius.com/ls/index.php?l=cliens
- Pausanias 10.28.2: Polygnotus followed the *Minyas* in painting Charon: Perseus/Scaife text, https://cts.perseids.org/read/greekLit/tlg0525/tlg001/perseus-eng2/10.28.2-10.30.2
- Propertius 4.11: Perseus claims Achilles as ancestor (poem confirmed; line 39 not confirmed by search): https://www.poetryintranslation.com/PITBR/Latin/PropindexABC.php
- Lane hand-offs: `rome/r-2.4.html` ("Virgil's is Greek in plan (deep dive module 12.5)"), `rome/r-3.5.html` (6.836–840 usually Perseus; Ennius' oracle, Cicero, *On Divination* 2.116), `rome/r-6.3.html` ("The precept to spare the conquered (6.851–853) belongs to deep dive module 12.5"): all kept, none retold beyond a sentence
- Pointers true of their targets: module 0.2 (Cumae, Strabo 5.4.4); 1.3 (Livy 1.3.6 Silvius son of Ascanius, Dionysius 1.70 posthumous son of Lavinia); 1.6 (Sibylline Books sold to Tarquin); 2.4 (no Roman map of the underworld); 3.5; 4.4 (Corinth to Mummius in 146); 6.3 (parade, Catiline on the shield, Carmen Saeculare); 10.1 (little *Aeneid*, Pythagoras' speech in *Metamorphoses* 15); 10.2 (Lucan's Erictho inverting *Aeneid* 6; Silius); 10.4 (Dante's providential Rome); 12.1 (Palinurus' two accounts, Helen episode and Deiphobus, Ennius' Fabius line, Octavia fainting); 12.2 (book 6 left in outline); 12.4 (Dido at 6.450–476, Ajax's silence as model); 12.6 (vow of a temple and shrine, 6.69–74); 12.7 (Marcellus test case; the precept against the ending); 12.8 (Dante's choice of Virgil); Greek 4.4 and 10.7 (*Odyssey* 11; scholia's objection that Odysseus could not see into Hades from his pit; Elpenor; trust in the Apologoi); Greek 5.6 and 12.1 (Pythagorean transmigration); Greek 8.4 (*Phaedo* 81c–d, Lucretius 3 on Acheron); Greek 12.3 (*Timaeus* 30b, 35a–36d; *Phaedrus* 248e–249a); Greek 12.7 (pneuma, Chrysippus' passions)
- *Aeneid* 6 line references checked against the checker's knowledge of the text (Daedalus 14–33; Deiphobe 36; *deus, ecce deus* 46; prophecy 83–97; *facilis descensus* 126–129; bough 136–148, 205–211; Misenus 162–174, 234–235; forecourt 273–281; monsters 285–294; Charon 298–304; similes 305–312; *tendebantque manus* 314; Palinurus 337–383, 376; boat 413–414; Cerberus 417–425; the groups 426–449; Deiphobus 494–546; Tartarus 548–627; Elysium 638–675; doctrine 724–751 (28 lines); parade 756–886; charge 847–853; gates 893–898; Caieta 900)
- *Odyssey* 4.274–289, 4.561–569, 11.51–80, 11.204–208, 11.225–332 (Phaedra, Procris, Eriphyle), 11.489–491, 11.563–564, 19.560–567; *Iliad* 6.146–149, 8.16; Plato, *Charmides* 173a, *Republic* 363c–d, 614b–621d, *Phaedo* 82e, 113e, *Gorgias* 525c; Cicero, *On the Republic* 6.13, *On Duties* 1.35; Horace, *Carmen Saeculare* 51–52; Apollodorus 2.5.12; Bacchylides 5 (Ida); Strabo 5.4.5: checker's knowledge, not searched
- Dante, *Inferno* 2.13–15, 2.20–24, 2.32, 3.91–93, 3.109, 3.112–117, 3.124–126, 4.106–111, 4.122, 5.4–12, 5.61–62, 6.25–27, 8.13–24, 9.37–48, 13.10, 31.98: checker's knowledge of the Petrocchi text, not searched
- Augustine, *City of God* 14.5 (6.719–721) and 21.13 (the purgations): writer confirmed in translation; not rechecked
- Knauer, *Die Aeneis und Homer* (Göttingen, 1964): checker's knowledge
- No em dashes; British spelling (the only check.py flag, "labor", is the Latin *hic labor est*); no figure of dead, troops or money needs a source
