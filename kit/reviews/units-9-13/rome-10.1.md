# Rome 10.1: Ovid and the Roman remaking of Greek myth

Verdict: fix
Body words: 2793 (target 2500)

## Coverage
- Structure from Chaos to the apotheosis of Caesar: covered
- Roman frame (council as Senate, Jupiter and Augustus, Caesar's star): covered
- Stories invented or transformed (Echo and Narcissus, Pyramus and Thisbe, Arachne, Pygmalion, Medusa): covered
- Stories taken from lost Hellenistic poets: thin (one tested case, the Minyads; the rest is a pointer to Greek 3.7, which lists poets, not stories)
- Roman names and why they stuck: covered
- The Fasti as counterpart for Roman myth: covered
- The Heroides: covered
- Later life (Ovide moralisé, Chaucer, Shakespeare, Titian, Bernini): covered (Titian brief, with a true pointer to Greek 9.3)
- Point back to Greek modules 0.1 and 3.7: covered
- Lane hand-offs: Greek 3.7 (points back, no retelling of its Greek evidence; carry-forward 2 echoes the 0.1/3.7 "how Roman" argument, see finding 3); Greek 0.1 (pointed back to, Medusa extended rather than repeated); Rome 6.3 (pointed back to and taken further); Rome 0.1 (Vertumnus and Pomona and Numa kept to a mention); Fasti read as a poem, with pointers to 2.3, 2.4 and 6.3: all kept

## Findings
1. [error] [accuracy] Section "The Heroides: myth in the heroine's voice".
   Current: "fifteen verse letters from women of myth to the men who left them, among them"
   Problem: Not all fifteen are to men who left the writer, and one of the examples named is a clear counter-case: Phaedra's letter (4) is a declaration of love to her stepson Hippolytus, who has never been hers to leave. Hermione's (8) and Laodamia's (13) are also to men absent, not deserting.
   Fix: "fifteen verse letters from women of myth to absent husbands and lovers, most of whom have left them, among them"
   Basis: Ovid, Heroides 4, 8 and 13 (contents); +5 words.

2. [should-fix] [accuracy] Section "The lost Hellenistic shelf".
   Current: "enter the poem through them. The Hellenistic catalogues"
   Problem: The prompt asks which stories Ovid took from lost Hellenistic poets. The report tests one (the Minyads) and points to Greek 3.7, which lists the poets but not the stories, so this prompt item is thin. Antoninus Liberalis gives several more Nicandrian controls in one sentence.
   Fix: add after "enter the poem through them.": "Antoninus also gives Nicander's versions of the Pierides' contest with the Muses (9; Ovid's book 5), Battus (23; book 2), Byblis (30; book 9) and a girl turned boy, Leucippus where Ovid has Iphis (17; book 9)."
   Basis: Antoninus Liberalis, Metamorphoses 9 (Emathides, Nicander book 4), 17 (Leucippus, Nicander book 2), 23 (Battus, Nicander book 1), 30 (Byblis, Nicander book 2), from memory, not rechecked; +37 words, which keeps the report inside the band (about 2841 with all fixes, maximum 2875).

3. [should-fix] [lane] Section "Carry forward".
   Current: "a story first found in him is Roman until a Greek witness appears, and even then it is told in his words."
   Problem: This restates Greek 0.1's third carry-forward ("anything known only from them is Roman until a Greek source confirms it") and its rule 6. It also sits awkwardly beside Greek 3.7's first carry-forward ("Absence of a Greek source is usually absence of evidence") and repeats 3.7's closing "how Roman" argument, which the lane note says 10.1 must not repeat. The carry-forward should be this module's own finding, the Antoninus test.
   Fix: "where Antoninus Liberalis allows a test, the plot is Hellenistic and the frame, voice and texture are Ovid's."
   Basis: greece/r-0.1.html (section "How a scholar decides between variants", item 6, and Carry forward 3); greece/r-3.7.html (closing section and Carry forward 1).

4. [minor] [accuracy] Section "A Roman poem that taught Europe Greek myth".
   Current: "If the emended reading <em>illa</em> is right in line 2, the gods are thanked for changing the poet's own undertakings too, from elegy to epic."
   Problem: Most manuscripts read illas; illa is a variant in two manuscripts, which Anderson treats as Lejay's 1894 conjecture and Kovacs thinks may be one, so "emended" overstates a contested point. The gods are also called on, not thanked: "for you changed those too" gives the reason for the prayer.
   Fix: "If the minority reading <em>illa</em> is right in line 2, the gods have changed the poet's own undertakings too, from elegy to epic."
   Basis: D. Kovacs, "Ovid, Metamorphoses 1.2", Classical Quarterly (abstract), https://www.cambridge.org/core/journals/classical-quarterly/article/abs/ovid-metamorphoses-12/7700BCC8A82EE775BC5CA7484CC860EB (illa recommended by Lejay 1894 and championed by Kenney 1976; a variant in two manuscripts).

5. [minor] [accuracy] Section "Afterlives: from the Ovide moralisé to Bernini".
   Current: "Chaucer read him unmoralised."
   Problem: Chaucer used the Ovide moralisé as a source beside the Latin (Lowes, PMLA 1918; Meech, PMLA 1930–31), though he left its allegories out. As written, the sentence suggests he did not use it at all.
   Fix: "Chaucer used the <em>Ovide moralisé</em> beside the Latin but left its morals behind."
   Basis: Chaucer Bibliography entries "Chaucer and the 'Ovide Moralisé'", https://chaucer.lib.utsa.edu/items/show/272862 and https://chaucer.lib.utsa.edu/items/show/272795 (the articles themselves not read); +9 words.

## Confirmed
- Ovide moralisé date: 10.1's "early fourteenth century" is right. greece/r-9.3.html needs the change: replace "the thirteenth-century <em>Ovide moralisé</em>" with "the early fourteenth-century <em>Ovide moralisé</em>". Cambridge introduction (Murray and Boyd) calls it fourteenth-century, c. 1320: https://www.cambridge.org/core/books/medieval-french-ovide-moralise/introduction/08112967879A355D4A7B6373EC0BFA9D
- "some 12,000 Latin lines into about 72,000 French ones": same Cambridge introduction.
- Wheeler, Narrative Dynamics in Ovid's Metamorphoses (Tübingen 2000): calls Otis "block-like" and "too reductive"; repetition and narrative continuity; deferred closure. Alden Smith, BMCR 2001.11.23, https://bmcr.brynmawr.edu/2001/2001.11.23/
- Heroides box: Lachmann 1848 (seminal doubts), Tarrant 1981 (HSCP, against), Courtney 1997 ("Echtheitskritik: Ovidian and non-Ovidian Heroides again", defends, citing Amores 2.18), Thorsen 2014 (answers Tarrant point by point), Kenney 1996 (doubles Ovidian, against Courtney's 1965 metrical doubts): stylometric survey, https://arxiv.org/abs/2202.11864
- Pyramus box: Nicolaus' Progymnasmata (river and spring) and the Nea Paphos mosaic: https://en.wikipedia.org/wiki/Pyramus_and_Thisbe. Named sources on each side, so the box meets the bar.
- Pointers all true of their targets: Greek 0.1 (Ovid as trap; Medusa, Met. 4.790–803, against Theogony 278–279); Greek 3.7 (Greek evidence for Narcissus and Echo, Pygmalion, Arachne; Hellenistic sources listed; Hardie and Feeney on the Jupiter and princeps parallel); Rome 6.3 (career, Chaos to apotheosis, 15.858–860, 15.871–872, exile, Augustan days of the Fasti); Rome 2.2 (equations and their misfit); Rome 2.3 (Fasti as source; "trust the actions... over the reasons"); Rome 2.4 (Fasti as source); Rome 1.6 (Lucretia, Fasti 2.685–852); Greek 9.3 (Greek lost in the Latin West; Bulfinch 1855, Latin-named; Titian's poesie); Rome 10.4 prompt (reception of Rome at large).
- crosscheck.py: no shared seven-word passages, no duplicated dispute boxes.
- Callimachus, Aetia fr. 1.3 Pfeiffer (one continuous song); Virgil, Eclogue 6.5 (deductum carmen); Met. 1.3–4: known.
- Met. 1.168–176 (Milky Way, nobles and plebs, Palatia caeli); 1.199–205 (Caesareo sanguine; Auguste): known.
- Met. 13.623–14.608 (the "little Aeneid"); 14.581–608 (Aeneas made Indiges); 14.805–851 (Romulus Quirinus, Hersilia Hora); 15.165; 15.622–744 (Aesculapius); 15.746–761 (no greater deed than fathering Augustus; "ne foret hic... mortali semine cretus"); 15.858–860; 15.871–879 (vivam): known.
- Pliny, Natural History 2.93–94 (Augustus on the comet of July 44 BC); Tristia 1.7 (copy burned, final revision lacking): known.
- Pyramus 4.55–166, 4.53 (vulgaris fabula non est), 4.73, 4.121–124, 4.166; coeamus at 3.386–387; augusta gravitate 6.73; 6.129–130; Pygmalion's gifts including amber; Perseus as Medusa's narrator at the wedding feast: known.
- Tristia 4.10.43–44 (Macer's birds, snakes and herbs); Antoninus Liberalis 10 (Nicander book 4 and Corinna; Hippasus; bat, owl, eagle-owl); Met. 4.389–415 (all bats): known.
- Fasti 2.3; 3.167–258; 5.183–378; 5.1–110; 6.1–100; 1.461–586; 2.193–242; 3.259–392; 3.523–696; 4.417–620; Tristia 2.549–552 ("sex... totidemque"); 1.536 (Julia Augusta, AD 14); 1.3 (Germanicus, translator of Aratus); 6.797–812 (Clio, Philippus, Marcia, Augustus' first cousin, wife of Paullus Fabius Maximus): known.
- Heinze, "Ovids elegische Erzählung" (1919); Hinds, The Metamorphosis of Persephone (1987): titles, dates and positions right.
- Ars Amatoria 3.345–346 (ignotum hoc aliis ille novavit opus); Propertius 4.3: known.
- Traube's aetas Ovidiana as the twelfth and thirteenth centuries; Arnulf of Orléans (twelfth century), John of Garland (thirteenth); Philomena surviving only in the Ovide moralisé; Golding 1567; Meres 1598; Book of the Duchess, Legend of Good Women, Wife of Bath's Midas; Titus 4.1; Tempest 5.1 after Met. 7 via Golding; Bernini 1622–25 for Scipione Borghese, Met. 1.548–552, Barberini's couplet: known.
- House style: British spelling, no em dashes, no preamble or filler; Augustus used correctly throughout; self-test answers agree with the body; length within band.
