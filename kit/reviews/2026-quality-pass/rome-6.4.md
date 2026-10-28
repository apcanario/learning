# Rome 6.4: Empire without end

Verdict: fix
Body words: 2826 (target 2500)

## Coverage
- "Empire without end" (Aeneid 1.279) against the advice to keep within limits (Annals 1.11): covered
- Professional army: twenty-eight legions covered (shown to be a modern sum); auxiliaries covered briefly (citizenship on discharge handed to 9.2); praetorian guard covered; military treasury covered; terms of service covered
- Conquest of north-west Spain, the Alps and the Danube lands: covered
- Egypt as the emperor's personal province: covered
- Parthian standards in 20 BC and the Prima Porta breastplate: covered
- Germany, Drusus and Tiberius, Varus in AD 9: covered
- Kalkriese: covered
- Client kings such as Herod: covered
- Provinces of the Senate and of Caesar: covered
- The Res Gestae's map of the world: covered

## Findings
1. [error] [attribution] Section "Germany: Drusus, Tiberius and Varus".
   Current: "dying on the return after a fall from his horse (Dio 55.1–2)"
   Problem: Dio says Drusus died of disease on the way, before reaching the Rhine; the fall from his horse is in Livy's epitome.
   Fix: "dying on the return, after a fall from his horse in Livy's epitome (<em>Periochae</em> 142), of disease in Dio (55.1.4)"
   Basis: Dio 55.1.4, Cary's translation at LacusCurtius (https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/55*.html): "died on the way of some disease before reaching the Rhine"; Livy, Periochae 142 (the horse fell on his leg; he died on the thirtieth day), not fetched.

2. [should-fix] [figure] Section "Germany: Drusus, Tiberius and Varus".
   Current: "Modern estimates of 15,000 to 20,000 soldiers are reckoned from paper strengths."
   Problem: An unnamed modern estimate; the course rule is a named one. The common 15,000 to 20,000 dead goes back to a magazine article, while a published reckoning from paper strengths exists.
   Fix: "Reckoning from paper strengths, Michael McNally (<em>Teutoburg Forest AD 9</em>, 2011) puts Varus' force at about 17,000 soldiers and 3,800 servants."
   Basis: https://en.wikipedia.org/wiki/Battle_of_the_Teutoburg_Forest (McNally 2011, 21–22, for about 17,000 combatants and 3,800 servants; the 15,000–20,000 dead cited to Bordewich, Smithsonian 2005); not checked against McNally's book.

3. [minor] [accuracy] Section "Client kings and the provinces of the Senate and of Caesar".
   Current: "all styled proconsul and, outside Africa, without legions."
   Problem: Illyricum was a public province with legions until it passed to Augustus in 11 BC, so the statement holds only from then.
   Fix: "all styled proconsul and, once Illyricum passed to Caesar in 11 BC (Dio 54.34.4), without legions outside Africa."
   Basis: Dio 54.34.4 (https://lexundria.com/dio/54.34.4/cy): "After this Dalmatia was given over into the keeping of Augustus", as needing a permanent army.

4. [minor] [lane] Section "The Res Gestae's map of the world" (dispute box).
   Current: "Benjamin Isaac (<em>The Limits of Empire</em>, 1990) and C. R. Whittaker (<em>Frontiers of the Roman Empire</em>, 1994) denied any such doctrine."
   Problem: Module 0.2's box gives the same books with titles and dates (crosscheck: 11 shared shingles, 8 shared names); after the pointer to 0.2 the titles only repeat the neighbour. The Augustan application, which is this box's reason to exist, is untouched.
   Fix: "Benjamin Isaac and C. R. Whittaker, whose books module 0.2 cites, denied any such doctrine."
   Basis: rome/r-0.2.html (Luttwak, Isaac, Whittaker, Mattern box); crosscheck run of 25 October, sections 2 and 3 (6.4 ~ 0.2).

## Confirmed
- Velleius 2.97.1, 2.97.4, 2.110.3 (about 200,000 infantry and 9,000 cavalry), 2.111.1 (in sight of Rome within ten days), 2.117.1 (three legions, as many alae, six cohorts), 2.118.2 (citizenship and equestrian rank), 2.119.2 (forests, marshes, ambush), 2.119.5 (head sent by Maroboduus), 2.95, 2.96: LacusCurtius, https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Velleius_Paterculus/2D%2A.html.
- Dio 55.10.10 (two praetorian prefects), 55.23.1–2 (terms of AD 5; twenty-three or, as others say, twenty-five legions), 55.25.2–3 and 55.25.5 (military treasury; kings and communities, no private citizens; five per cent on inheritances): LacusCurtius Dio 55, as above.
- Strabo 4.6.7: some 36,000 Salassi sold (https://en.wikipedia.org/wiki/Salassi, citing Strabo).
- Kalkriese: Wolters' argument that Lower Rhine bronze circulated longer, with the site identified as Caecina's "causeways" of AD 15, and Wigg-Wolf's reply that the coin profiles separate a Varian from a Germanicus horizon, Kalkriese belonging to the first: Drinkwater's review of Lehmann and Wiegels (eds.) 2007, https://sehepunkte.de/2008/09/13856.html; Werz 2019 on Wolters' later countermark study (https://ejournals.uni-muenster.de/ozean/article/view/2476).
- Kalkriese turf wall re-examined since 2016 as possibly a Roman emergency camp; the near-complete lorica segmentata: https://the-past.com/news/uncovering-kalkriese/. Clunn's 1987 finds and the VAR countermarks: Wikipedia, as above.
- Brunt's 1963 JRS review of Meyer argued that Augustus aimed at world conquest (BMCR 1991.01.03, https://bmcr.brynmawr.edu/?p=19667). Gruen, "The Imperial Policy of Augustus" (1990): the summary fits the chapter as known; not checked online.
- Aeneid 1.278–279, 1.287; Annals 1.11.4, 1.17, 1.61, 1.63–68, 1.78, 2.1, 2.59, 4.5; Suetonius, Augustus 20, 21.3, 23.1–2, 25.1, 38.1, 47, 48, 49.1, 101.4; Tiberius 16.1; Dio 51.24, 53.12, 53.23, 53.25, 53.26.3, 53.26.5, 54.11, 54.22, 54.25.6, 56.18.2–3, 56.19–22, 56.23.2–4, 56.33.5–6; Strabo 16.1.28, 16.4.22–24, 17.1.12, 17.1.54; Res Gestae 3.3, 16, 17.2, 26–33; Epitome de Caesaribus 1.6; Florus 2.30; Tacitus, Agricola 14; Macrobius 2.4.11; Horace, Epistles 1.12.27–28; Pliny 3.17, 3.136–137; CIL XIII 8648: checked from the texts as known.
- Millar, "The Emperor, the Senate and the Provinces" (JRS 1966); Nicolet (1991); Luttwak (1976); Isaac (1990); Whittaker, Frontiers of the Roman Empire (English edition 1994): attributions and dates correct.
- Pointers true: 6.3 (prophecy as programme); 5.2 (Marian reforms as background); 11.2 and 9.2 true of their prompts; 4.4 (tributum not levied after 167; the Republican governor); 5.5 (Egypt taken in 30); 5.4 (Carrhae); 6.2 (Mars Ultor; the statue as a whole); 7.1 (Germanicus' campaigns); 6.1 (the division of 27 as a constitutional act); 7.5 (later government); 0.2 (the general frontier quarrel).
- Pointers into this report true: 6.1 (twice), 6.2, 7.1 ("module 6.4 quotes their complaints, 1.17": 6.4 paraphrases them closely, ten asses against two denarii and men kept under the banner; "asks whether Kalkriese is that battle": the Wolters box; Germanicus handed to 7.1), 7.2 (Caesar's 225 denarii, the first rise under Domitian), 7.3 (twice, the advice to keep within limits), 7.5 (Augustus dividing the provinces between proconsuls by lot and his own legates; the inheritance and sales taxes of the military treasury). 7.5 has no pointer to 6.4 for client kings: nothing to check.
- Overlap with 5.5 (Egypt under an equestrian prefect, Annals 2.59, RG 27.1) is one sentence there; this report owns the topic. Gallus' fall here and in 6.3, and Balbus' triumph here and in 6.1, are one sentence or clause each: acceptable.
- House style: Octavian before 27 and Augustus after; no em dashes; British spelling.
