# Rome 5.1: The Gracchi

Verdict: fix
Body words: 2837 (target 2500)

## Coverage
- Agrarian problem in Appian (Civil Wars 1.7–13) and Plutarch: covered
- Modern revision, decline of the peasantry (Rathbone, Rosenstein, de Ligt): covered (Rathbone in one clause, on the 2008 chapter)
- Tiberius' land law: covered
- Deposition of Octavius: covered
- Pergamene bequest: covered
- Killing by Scipio Nasica and the senators: covered
- Land commission and its boundary stones: covered (with the Polla stone)
- Gaius' grain law: covered
- Equestrian juries: covered
- Colonies: covered
- Citizenship for the Latins: covered
- First final decree and Gaius' death in 121: covered
- Cornelia and the letter attributed to her: covered (deep dive 11.4 named for more)
- Gracchi as heroes or demagogues in Cicero, Sallust, Velleius, Plutarch: covered (Tacitus added)
- Why ancient writers saw 133 as the beginning of the end: covered

## Findings
1. [error] [accuracy] Section "Heroes or demagogues".
   Current: "his comparison ranks Tiberius first of the four in virtue (<em>Comparison</em> 6)"
   Problem: The Comparison of Agis and Cleomenes with the Gracchi has five chapters; the verdict that Tiberius led all four in virtue closes chapter 5 (5.6). There is no chapter 6. The report's other citation of the work (5.1, the deposition as the gravest charge) is right.
   Fix: "his comparison ranks Tiberius first of the four in virtue (<em>Comparison</em> 5.6)"
   Basis: Perrin's text with section numbers, https://lexundria.com/plut_comp_ag_gracch/5/prr (chapter 5 marked "end"; verdict in section 6; deposition charge in section 1); CTS text, https://cts.perseids.org/read/greekLit/tlg0007/tlg053/perseus-eng2/5.1-5.6.

2. [error] [attribution] Section "Cornelia" (dispute box), and self-test 9.
   Current (box): "a rhetorical exercise in her admired style would deceive only once detached from its context."
   Current (self-test 9 answer): "and a style admired by Cicero (<em>Brutus</em> 211) invited imitation, so a later exercise cannot be excluded (Instinsky, 1971)."
   Problem: Instinsky does not propose a rhetorical exercise. His suggestion, offered as a possibility hardly considered before, is a letter-fiction in the work of a historian who used the letter form and may have been close to the Gracchi's time; school exercises he mentions only in general. The point about a fiction misleading once detached from its context is his and should stay.
   Fix (box): "the letter may be a fiction in the work of a historian close to the Gracchi's time, deceiving only once detached from its context."
   Fix (self-test 9 answer): "and Instinsky (1971) suggested a fiction in the work of a historian close to the Gracchi's time."
   Basis: H. U. Instinsky, "Zur Echtheitsfrage der Brieffragmente der Cornelia, Mutter der Gracchen", Chiron 1 (1971) 177–190, p. 189 ("ein Fragment aus dem Werk eines Historikers ..., der sich der Form des Briefes bediente"; "Der Autor könnte der Zeit der Gracchen noch nahestehen"), p. 184 (rhetorical school exercises only in general; fiction surviving "als Bruchstück"), https://publications.dainst.org/journals/chiron/article/view/294/4902.

3. [should-fix] [register] Section "The modern revision: a vanishing peasantry?" (dispute box).
   Current: "The traditional reading credits the jump to the commission's allottees, who now had property to declare; another"
   Problem: The box names no modern scholar on either side; the bar asks for names. De Ligt's 2012 explanation of the 125/124 jump can be named on the first side. The evasion reading still needs a named holder: Wikipedia ("Gracchi brothers") cites de Ligt 2006, p. 602 (apparently his chapter in Rosenstein and Morstein-Marx, A Companion to the Roman Republic) for draft-dodgers not reporting to the censors; the writers removed an unverified de Ligt attribution here, so name him on that side only after checking that page.
   Fix: "The traditional reading credits the jump to the commission's allottees, who now had property to declare, and de Ligt (2012) adds a lowered property threshold for service; another"
   Basis: BMCR 2013.01.40, review of de Ligt, Peasants, Citizens and Soldiers (2012): the lowered threshold "combined with the Gracchan reforms, boosted the figures in the census returns of 125/124 BC", https://bmcr.brynmawr.edu/?p=37690; https://en.wikipedia.org/wiki/Gracchi_brothers (note 15, de Ligt 2006, p. 602; secondary only).

4. [minor] [style] Sections "Pergamon, a second tribunate and the killing on the Capitol" and "Heroes or demagogues".
   Current: "(Cicero, <em>Laelius</em> 37)" and "(<em>Laelius</em> 41)"
   Problem: Cicero's treatises go by English title; Rome 4.5 and 5.6 call this one On Friendship.
   Fix: "(Cicero, <em>On Friendship</em> 37)" and "(<em>On Friendship</em> 41)"
   Basis: AGENT-SPEC.md citation conventions; rome/r-4.5.html, rome/r-5.6.html.

5. [minor] [attribution] Section "Gaius Gracchus' programme, 123–122".
   Current: "Varro said he made the state two-headed, a source of civil discord."
   Problem: The only quotation in the list without a source. The line survives as a fragment of Varro quoted by Nonius.
   Fix: "Varro said he made the state two-headed, a source of civil discord (in Nonius)."
   Basis: Varro, fragment (bicipitem civitatem fecit, discordiarum civilium fontem) preserved by Nonius, usually assigned to On the Life of the Roman People; from memory, not checked online.

6. [minor] [attribution] Section "Pergamon, a second tribunate and the killing on the Capitol" (dispute box).
   Current: "Donald Earl read the veiling as the dress of sacrifice;"
   Problem: On the writers' unverified list (Earl via Linderski 2002), and the only modern view in the report given without work or date. I could not confirm it online. If the maintainer confirms it in Earl's book (or in Linderski's account of Earl), add the reference; if not, it should not stand as Earl's.
   Fix (once confirmed): "Donald Earl (<em>Tiberius Gracchus</em>, 1963) read the veiling as the dress of sacrifice;"
   Basis: not checked: Earl, Tiberius Gracchus: A Study in Politics (Brussels 1963) and Linderski, "The Pontiff and the Tribune: the Death of Tiberius Gracchus", Athenaeum 90 (2002) 339–366 (bibliographic details confirmed at https://uvm.edu/~bsaylor/rome/gracchibiblio.html) not available to me.

With all six applied the body is 2866 words, inside the band (top 2875); the fixes add 29 words in all, most of them in findings 2 and 3, so drop 5 and 6 first if other edits add length.

## Confirmed
- Plutarch, Tiberius Gracchus 19: touching his head (19.2), Scaevola's refusal and Nasica's call (19.3), toga over head (19.4), clubs and bench legs (19.5), Satureius and more than 300 dead, none by iron (19.6) (https://lexundria.com/plut_tg/19/prr).
- Plutarch, Tiberius Gracchus 8: Blossius, Cornelia's complaint, Gaius' pamphlet on Etruria within 8.3–8.7, drafters of the law and the mild first law at 9 (https://cts.perseids.org/read/greekLit/tlg0007/tlg052/perseus-eng1/Tiberius.8.3-Tiberius.8.7; https://cts.perseids.org/read/greekLit/tlg0007/tlg052/perseus-eng1/Tiberius.8.5-Tiberius.9.3). The lexundria pages for chapters 8 and 9 (https://lexundria.com/plut_tg/8/prr, https://lexundria.com/plut_tg/9/prr) were blocked, so section numbers 8.7 and 9.4–5 are not checked to the section.
- Comparison 5.1: the deposition of his colleague is "the greatest of the accusations against Tiberius" (lexundria, as above).
- Periochae 60: Fregellae and Opimius, 394,736 citizens, grain at six and one-third asses, 600 knights added to the Senate (https://test.livius.org/sources/content/livy/livy-periochae-56-60?level=5).
- Garnsey and Rathbone, JRS 75 (1985): regularity and storage, shortages of 142, 138 and 129, Heichelheim's Mediterranean-wide price rise rejected, the grain subsidised but paid for (https://faculty.uml.edu/ethan_Spanier/Teaching/documents/rathboneGGracchus.pdf).
- Rathbone, "Poor peasants and silent sherds", in de Ligt and Northwood (eds), People, Land and Politics (Brill 2008) 305–332 (https://kclpure.kcl.ac.uk/portal/en/publications/poor-peasants-and-silent-sherds/); argument as summarised not checked.
- De Ligt, "Poverty and Demography: the Case of the Gracchan Land Reforms", Mnemosyne 57 (2004) 725–757 (https://uvm.edu/~bsaylor/rome/gracchibiblio.html); de Ligt 2012 blames rural poverty on population growth, with more slaves and less colonisation alongside (BMCR 2013.01.40), so "rather than to slaves replacing citizens" stands.
- Polla stone: Mommsen's Popillius Laenas and Wiseman's T. Annius Rufus, praetor 131, are the two leading attributions; a 2016 PBSR study ("The Lapis Pollae: date and contexts") dates it before 131 and finds no attribution secure, so "date and link to the Gracchan scheme are disputed" is right (https://www-cambridge-org.ezproxyberklee.flo.org/core/journals/papers-of-the-british-school-at-rome/article/lapis-pollae-date-and-contexts/48768508B9BE3EFD0CA8304DF36F34EF).
- Instinsky's title, journal and year (Chiron 1, 1971) and his view that "genuine or forged" is too crude a choice (dainst, as above).
- Checked from the texts as known: Appian, Civil Wars 1.1–2, 1.7–12, 1.14, 1.16, 1.18–27; Plutarch, Tiberius Gracchus 1, 10, 12, 14, 15, 20.1, 20.3, 21.4, Gaius Gracchus 5, 9, 11, 13, 16, 17; Cicero, De haruspicum responso 43, De lege agraria 2.10, On Friendship 37 and 41, On Duties 1.76 and 2.43, On the Republic 1.31, On Divination 1.56, Tusculan Disputations 3.48, Pro Rabirio perduellionis reo 12, Verrines 2.3.12, Against Catiline 1.4, Brutus 211; Caesar, Civil War 1.5; Velleius 1.15.4, 2.2–2.4, 2.6, 2.7; Sallust, Jugurtha 42; Tacitus, Annals 3.27; Valerius Maximus 9.4.3; Pliny, Natural History 34.31 and the base inscribed Cornelia Africani f. Gracchorum; Odyssey 1.47; Periochae 56, 58, 59, 61; the Tabula Bembina's 450 jurors.
- Pointers true: module 3.1 (the 500-iugera cap dated 367, plebiscites binding from 287, Camillus' and Opimius' temples of Concord, annalists writing after 133), module 4.4 (Mancinus' treaty negotiated by Tiberius, the slave-run estate, publicani, Asia's tithe let at Rome from 123), module 4.5 (rival dates of decline), module 5.6 (Sallust's theory of decline), deep dives 11.3 (grain laws to Clodius; the final decree as legalised violence), 11.4 (Cornelia) and 11.8 (explanations of the fall), all as their prompts in roman-syllabus.html describe them. Pointers into this report from 3.1, 4.4, 5.2 and 5.3 are true.
- The shared line with module 0.3 (Plutarch's first civil strife since the kings to end in bloodshed, Tiberius Gracchus 20.1) is one sentence in each, used by 0.3 to justify a period boundary; this report is its home.
