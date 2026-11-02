# P87, P88 · Dio inventory (drafter)

A fresh Opus 5.5 agent, 2 Nov 2026 (row A-1): every Cassius Dio citation in the Greece and Rome reports and bibliographies listed and checked against Cary's Loeb on LacusCurtius; its report, verbatim. A separate checker's verdicts are in `p87-p88-dio-checker.md`; the log entry is in `log.md`.

# Cassius Dio citation check: Greece and Rome courses (2 Nov 2026)

Scope: courses/greece, courses/rome, kit/bibliography/greece, kit/bibliography/rome in /home/claude/learning. Nothing in the repo was edited. Working notes: /tmp/claude-0/-home-claude/ee713100-cbe9-5b5e-babd-b94a6313762a/scratchpad/dio/worklog.md

## 1. Slips: exact text and replacement

Each "current text" occurs exactly once on the line given (checked by script). It is also unique in its file, with one exception: in greece 7.4, `(Dio Cassius 72.31.3;` appears once on line 29 and once on line 150, so match it by line. All replacements use en dashes as the files do and contain no em dashes.

### List A slips (two numbers)
Loeb 80 holds traditional 79 (chs 1-21, margin LXXIX) and then traditional 80 (Alexander, chs 1-5). Where Loeb and margin agree, the convention calls for a single number, so `80(80)` should be `80`. Caveat: LacusCurtius prints no numeral where the chapters restart for Alexander. The mapping rests on that restart (see section 2). Scott's commentary is titled with "80(80)" (OUP listing, search result only), so a checker may decide to keep the form. Under the convention as stated, these are slips.

| file:line | current text | replacement |
|---|---|---|
| courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:96 | `(80(80).1.1, 2.2)` | `(80.1.1, 2.2)` |
| courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:96 | `(80(80).4.2–5.1)` | `(80.4.2–5.1)` |
| courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:98 | `(80(80).3–4)` | `(80.3–4)` |
| courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:122 | `(80(80).1.2–3)` | `(80.1.2–3)` |
| courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:166 | `(Dio 80(80).3–4)` | `(Dio 80.3–4)` |
| kit/bibliography/rome/r-7.4.md:7 | `80(80).1.1; 80(80).1.2–3; 80(80).2.2; 80(80).3–4; 80(80).4.2–5.1.` | `80.1.1; 80.1.2–3; 80.2.2; 80.3–4; 80.4.2–5.1.` |

Conditional (NOT CHECKED, because the Loeb 75 page was refused): `75(75)` has the same problem. If Loeb 75 ends with traditional 75.1-3, as the Loeb 76 page implies by opening at ch.4 without a numeral, then the convention gives:
- courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:36: `(75(75).1.1, 3.2–3)` becomes `(75.1.1, 3.2–3)`
- kit/bibliography/rome/r-7.4.md:7: `75(75).3.2–3;` becomes `75.3.2–3;`

### List B slips (single number where Loeb and margin differ)
| file:line | current text | replacement | why |
|---|---|---|---|
| courses/greece/11.8-death-body-and-afterlives.md:90 | `(Dio 76.13.2)` | `(Dio 76(75).13.2)` | Loeb 76 ch.13.2 (the tomb locked) is traditional 75 |
| courses/greece/11.8-death-body-and-afterlives.md:121 | `(Dio 78.7–9;` | `(Dio 78(77).7–9;` | Loeb 78 (phalanx 7.1, Aristotelians 7.3) is traditional 77 |
| courses/greece/7.4-greece-under-the-empire-and-the-end-of-antiquity.md:29 | `(Dio Cassius 72.31.3;` | `(Dio Cassius 72(71).31.3;` | Loeb 72 carries margin LXXI throughout |
| courses/greece/7.4-greece-under-the-empire-and-the-end-of-antiquity.md:150 | `(Dio Cassius 72.31.3;` | `(Dio Cassius 72(71).31.3;` | same |
| kit/bibliography/greece/r-7.4.md:11 | `69.16; 72.31.3.` | `69.16; 72(71).31.3.` | same |
| kit/bibliography/greece/r-11.8.md:13 | `68.29–30; 76.13.2; 78.7–9.` | `68.29–30; 76(75).13.2; 78(77).7–9.` | as for 11.8 |
| kit/bibliography/greece/unit-11.md:257 | `- Dio 68.29–30; 76.13.2; 78.7–9` | `- Dio 68.29–30; 76(75).13.2; 78(77).7–9` | as for 11.8 |
| courses/rome/7.2-the-year-of-four-emperors-and-the-flavians.md:78 | `(Dio 66.15)` | `(Dio 65(66).15)` | Berenice is Loeb 65.15 (margin LXVI). Loeb 66 opens at ch.17. This is the same error as the earlier Rome 7.2 "66.15" fix, still present in the vault file |
| kit/bibliography/rome/r-7.2.md:6 | `65(66).13; 66.15; 66.25` | `65(66).13; 65(66).15; 66.25` | same; 66.25 is right (Loeb 66) |
| kit/bibliography/rome/unit-7.md:75 | `- Dio 66.15` | `- Dio 65(66).15` | same |
| courses/rome/13.5-seneca.md:32 | `put to death (60.31.2)` | `put to death (61(60).31.2)` | traditional 60.29-35 is printed in Loeb 61 under margin LX |
| courses/rome/13.5-seneca.md:46 | `urged the murder (61.12.1)` | `urged the murder (62(61).12.1)` | traditional 61.11-21 is in Loeb 62 under margin LXI |
| kit/bibliography/rome/r-13.5.md:8 | `from 60.29 on` | `from 61(60).29 on` | Loeb 61, margin LX |
| kit/bibliography/rome/r-13.5.md:8 | `60.31.2 (Messalina` | `61(60).31.2 (Messalina` | same |
| kit/bibliography/rome/r-13.5.md:8 | `61.12.1 (Seneca said` | `62(61).12.1 (Seneca said` | Loeb 62, margin LXI |
| courses/rome/7.1-the-julio-claudians.md:107 | `(60.35.3)` | `(61(60).35.3)` | "Pumpkinification" is in Loeb 61, margin LX |
| kit/bibliography/rome/r-7.1.md:7 | `60.35.3 (the` | `61(60).35.3 (the` | same |
| courses/rome/7.1-the-julio-claudians.md:133 | `(Dio 63.17.5–6)` | `(Dio 62(63).17.5–6)` | Corbulo's "Your due!" is in Loeb 62 under margin LXIII (traditional 63.1-21) |
| kit/bibliography/rome/r-7.1.md:7 | `62.16–18; 63.17.5–6.` | `62.16–18; 62(63).17.5–6.` | same |
| kit/bibliography/rome/unit-7.md:29 | `60.19–23; 63.17.5–6` | `60.19–23; 62(63).17.5–6` | same |

There are 20 text replacements. They cover 22 citation occurrences: r-11.8:13 and unit-11:257 each fix two.


## Table A: every two-number citation (grouped by line)
| file:line | citation(s) as written | passage | Loeb book / margin | verdict |
|---|---|---|---|---|
| rome/10.5-capstone-the-whole-thing-in-one-sitting.md:126 | 79(78).36.3 | 280 million a year | Loeb 79, trad 78 (chain) | CONFIRMED |
| rome/13.3-the-rival-schools-at-rome.md:100 | 72(71).31.3 | teachers at Athens | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.3-the-rival-schools-at-rome.md:103 | 72(71).31.3 | teachers at Athens | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.4-cato-and-the-stoic-opposition.md:68 | 65(66).12 | Helvidius abuses Vespasian | Loeb 65, margin LXVI (ch.1-16) | CONFIRMED |
| rome/13.4-cato-and-the-stoic-opposition.md:72 | 65(66).13 | expulsion of philosophers | Loeb 65, margin LXVI (ch.1-16) | CONFIRMED |
| rome/13.6-musonius-rufus-and-epictetus.md:22 | 65(66).13.2 | all expelled but Musonius | Loeb 65, margin LXVI (ch.1-16) | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:16 | 72(71).34 | death, age, watchword | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:24 | 72(71).6 | frailty, theriac | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:28 | 72(71).36.1 | ivory shoulders | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:52 | 72(71).35 | teachers | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:58 | 72(71).35 | teachers | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:70 | 72(71).6 | frailty, theriac | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:72 | 72(71).8–10 | rain miracle | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:74 | 72(71).9 | Xiphilinus on the Christians | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:80 | 72(71).22–23; 72(71).17; 72(71).24–26; 72(71).27; 72(71).28; 72(71).28–30 | Cassius proclaimed; peace with Iazyges; speech to soldiers; Cassius killed; the head; papers burned, pardons | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:82 | 72(71).22.3 | Faustina urges Cassius | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:86 | 72(71).29; 72(71).31; 72(71).34 | Faustina dies; honours for Faustina; death, age, watchword | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:94 | 72(71).22–23; 72(71).17; 72(71).24–26; 72(71).27; 72(71).28; 72(71).28–30 | Cassius proclaimed; peace with Iazyges; speech to soldiers; Cassius killed; the head; papers burned, pardons | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:100 | 72(71).22; 72(71).33 | Cassius revolt / Commodus summoned; Crispina / Bellona spear / death | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:112 | 72(71).33; 72(71).33; 72(71).34; 72(71).34 | Crispina / Bellona spear / death; death, age, watchword | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:114 | 72(71).33 | Crispina / Bellona spear / death | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:116 | 72(71).36.3–4 | verdict, gold to iron | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:128 | 72(71).22–23; 72(71).33 | Cassius proclaimed; Crispina / Bellona spear / death | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:160 | 72(71).8 | rain miracle, Arnuphis | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:164 | 72(71).22.3 | Faustina urges Cassius | Loeb 72, margin LXXI | CONFIRMED |
| rome/13.7-marcus-aurelius-a-life.md:172 | 72(71).33; 72(71).36.4 | Crispina / Bellona spear / death; gold to iron and rust | Loeb 72, margin LXXI | CONFIRMED |
| rome/7.2-the-year-of-four-emperors-and-the-flavians.md:76 | 65(66).13 | expulsion of philosophers | Loeb 65, margin LXVI (ch.1-16) | CONFIRMED |
| rome/7.3-the-adoptive-emperors.md:95 | 73(72).14.3 | plague, 2,000 a day | Loeb 73, margin LXXII | CONFIRMED |
| rome/7.3-the-adoptive-emperors.md:99 | 72(71).33 | Crispina / Bellona spear / death | Loeb 72, margin LXXI | CONFIRMED |
| rome/7.3-the-adoptive-emperors.md:105 | 73(72).2; 73(72).4.4; 73(72).9–10; 73(72).12.4; 73(72).13 | peace with Marcomanni; Pompeianus attack; Perennis; 25 consuls; Cleander killed | Loeb 73, margin LXXII | CONFIRMED |
| rome/7.3-the-adoptive-emperors.md:107 | 73(72).15.2–3; 73(72).19.3; 73(72).21.1–2 | renaming Rome, months; secutor fees; ostrich, laurel | Loeb 73, margin LXXII | CONFIRMED |
| rome/7.3-the-adoptive-emperors.md:109 | 73(72).22.2; 73(72).22.4–5 | consul from barracks; poison, Narcissus | Loeb 73, margin LXXII | CONFIRMED |
| rome/7.3-the-adoptive-emperors.md:111 | 72(71).36.4 | gold to iron and rust | Loeb 72, margin LXXI | CONFIRMED |
| rome/7.3-the-adoptive-emperors.md:172 | 72(71).36.4; 73(72).21 | gold to iron and rust; ostrich, laurel | Loeb 72, margin LXXI; Loeb 73, margin LXXII | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:14 | 74(73).10 | Pertinax killed | Loeb 74, trad 73 (no numeral shown; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:16 | 74(73).11.2–5; 74(73).12 | auction bids; Julianus in Senate | Loeb 74, trad 73 (no numeral shown; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:18 | 74(73).13 | Julianus dines | Loeb 74, trad 73 (no numeral shown; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:20 | 74(73).17.4–5 | Julianus killed | Loeb 74, trad 73 (no numeral shown; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:26 | 74(73).10; 74(73).11; 74(73).17 | Pertinax killed; auction; Julianus falls | Loeb 74, trad 73 (no numeral shown; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:32 | 77(76).17.4 | Severus born | Loeb 77, trad 76 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:34 | 75(74).1.1–2; 75(74).2.4–6 | praetorians banished; Italian youth | Loeb 75 (page refused) | NOT CHECKED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:36 | 75(74).6–8; 75(74).10–14; 75(75).1.1, 3.2–3 | Niger defeated; Byzantium siege; Mesopotamia "constant wars" | Loeb 75 (page refused) | NOT CHECKED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:36 | 76(75).6.1; 76(75).8.1–4 | 150,000 at Lugdunum; speech of 197 | Loeb 76, trad 75 (chs 4-16; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:38 | 76(75).9.4; 76(75).10–12 | Ctesiphon; Hatra | Loeb 76, trad 75 (chs 4-16; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:48 | 76(75).14.6; 77(76).3–4; 77(76).13.2; 77(76).15.2 | Plautianus statues; Plautianus killed; 50,000 dead in Britain; dying advice | Loeb 76, trad 75 (chs 4-16; chain); Loeb 77, trad 76 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:52 | 76(75).15.6–7; 78(77).18.2; 79(78).23–24 | Domna to philosophy; Domna's correspondence; Domna starves | Loeb 76, trad 75 (chs 4-16; chain); Loeb 78, trad 77 (chain); Loeb 79, trad 78 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:60 | 79(78).31–32; 80(79).17–20 | Maesa wins legion; Elagabalus killed | Loeb 79, trad 78 (chain); Loeb 80, margin LXXIX (chs 1-21) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:66 | 78(77).2.3–4; 78(77).4.1 | Geta killed; 20,000 killed / Papinian | Loeb 78, trad 77 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:68 | 78(77).12.5 | Geta's name banned | Loeb 78, trad 77 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:70 | 78(77).7–8; 78(77).22–23; 78(77).9–10; 79(78).5 | Macedonian phalanx; Alexandria massacre; exactions, sword remark; Caracalla killed | Loeb 78, trad 77 (chain); Loeb 79, trad 78 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:84 | 78(77).9.4–5 | taxes, citizenship | Loeb 78, trad 77 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:88 | 79(78).11; 79(78).41; 79(78).26–27; 79(78).36.3; 79(78).28; 79(78).31–32; 79(78).38–40 | Macrinus a Moor; first non-senator; peace with Artabanus; 280 million a year; recruits on old terms; Maesa wins legion; Macrinus defeated | Loeb 79, trad 78 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:90 | 80(79).9.3; 80(79).11.1; 80(79).17–20 | marries a Vestal; Elagabal above Jupiter; Elagabalus killed | Loeb 80, margin LXXIX (chs 1-21) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:96 | 80(80).1.1, 2.2; 80(80).4.2–5.1 | Ulpian killed; Dio's consulship outside Rome | Loeb 80, Alexander chs 1-5 = trad 80 (restart; no numeral) | SLIP |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:98 | 80(80).3–4 | Ardashir | Loeb 80, Alexander chs 1-5 = trad 80 (restart; no numeral) | SLIP |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:112 | 74(73).17; 76(75).6; 77(76).15; 79(78).5; 79(78).38–40; 80(79).17–20 | Julianus falls; Lugdunum; Severus dies; Caracalla killed; Macrinus defeated; Elagabalus killed | Loeb 74, trad 73 (no numeral shown; chain); Loeb 76, trad 75 (chs 4-16; chain); Loeb 77, trad 76 (chain); Loeb 79, trad 78 (chain); Loeb 80, margin LXXIX (chs 1-21) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:118 | 78(77).4.1 | 20,000 killed / Papinian | Loeb 78, trad 77 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:122 | 73(72).23 | how Dio wrote his history | Loeb 73, margin LXXII | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:122 | 80(80).1.2–3 | Dio seldom in Rome | Loeb 80, Alexander chs 1-5 = trad 80 (restart; no numeral) | SLIP |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:130 | 74(73).11 | auction | Loeb 74, trad 73 (no numeral shown; chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:134 | 75(74).1–2 | praetorians, new guard | Loeb 75 (page refused) | NOT CHECKED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:138 | 77(76).15.2 | dying advice | Loeb 77, trad 76 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:142 | 78(77).2; 78(77).12.5 | Geta killed; Geta's name banned | Loeb 78, trad 77 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:146 | 78(77).18.2 | Domna's correspondence | Loeb 78, trad 77 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:150 | 78(77).9.4–5 | taxes, citizenship | Loeb 78, trad 77 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:158 | 79(78).36.3; 79(78).28 | 280 million a year; recruits on old terms | Loeb 79, trad 78 (chain) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:162 | 80(79).11.1 | Elagabal above Jupiter | Loeb 80, margin LXXIX (chs 1-21) | CONFIRMED |
| rome/7.4-the-severans-and-the-citizenship-of-212.md:166 | 80(80).3–4 | Ardashir | Loeb 80, Alexander chs 1-5 = trad 80 (restart; no numeral) | SLIP |
| rome/7.5-how-the-empire-worked.md:120 | 77(76).10 | Bulla Felix | Loeb 77, trad 76 (chain) | CONFIRMED |
| kb/rome/r-10.5.md:9 | 79(78).36.3 | 280 million a year | Loeb 79, trad 78 (chain) | CONFIRMED |
| kb/rome/r-13.3.md:23 | 72(71).31.3 | teachers at Athens | Loeb 72, margin LXXI | CONFIRMED |
| kb/rome/r-13.4.md:10 | 65(66).12; 65(66).13 | Helvidius abuses Vespasian; expulsion of philosophers | Loeb 65, margin LXVI (ch.1-16) | CONFIRMED |
| kb/rome/r-13.6.md:8 | 65(66).13.2 | all expelled but Musonius | Loeb 65, margin LXVI (ch.1-16) | CONFIRMED |
| kb/rome/r-13.7.md:9 | 72(71).6; 72(71).8–10; 72(71).17; 72(71).22; 72(71).22–23; 72(71).24–26; 72(71).27; 72(71).28; 72(71).28–30; 72(71).29; 72(71).31; 72(71).33; 72(71).34; 72(71).35; 72(71).36.1; 72(71).36.3–4 | frailty, theriac; rain miracle; peace with Iazyges; Cassius revolt / Commodus summoned; Cassius proclaimed; speech to soldiers; Cassius killed; the head; papers burned, pardons; Faustina dies; honours for Faustina; Crispina / Bellona spear / death; death, age, watchword; teachers; ivory shoulders; verdict, gold to iron | Loeb 72, margin LXXI | CONFIRMED |
| kb/rome/r-7.2.md:6 | 65(66).13 | expulsion of philosophers | Loeb 65, margin LXVI (ch.1-16) | CONFIRMED |
| kb/rome/r-7.3.md:8 | 72(71).33; 72(71).36.4; 73(72).2; 73(72).4.4; 73(72).9–10; 73(72).12.4; 73(72).13; 73(72).14.3; 73(72).15.2–3; 73(72).19.3; 73(72).21.1–2; 73(72).22.2; 73(72).22.4–5 | Crispina / Bellona spear / death; gold to iron and rust; peace with Marcomanni; Pompeianus attack; Perennis; 25 consuls; Cleander killed; plague, 2,000 a day; renaming Rome, months; secutor fees; ostrich, laurel; consul from barracks; poison, Narcissus | Loeb 72, margin LXXI; Loeb 73, margin LXXII | CONFIRMED |
| kb/rome/r-7.4.md:7 | 73(72).23; 74(73).10; 74(73).11.2–5; 74(73).12; 74(73).13; 74(73).17.4–5; 76(75).6.1; 76(75).8.1–4; 76(75).9.4; 76(75).10–12; 76(75).14.6; 76(75).15.6–7; 77(76).3–4; 77(76).13.2; 77(76).15.2; 77(76).17.4; 78(77).2.3–4; 78(77).4.1; 78(77).7–8; 78(77).9.4–5; 78(77).9–10; 78(77).12.5; 78(77).18.2; 78(77).22–23; 79(78).5; 79(78).11; 79(78).23–24; 79(78).26–27; 79(78).28; 79(78).31–32; 79(78).36.3; 79(78).38–40; 79(78).41; 80(79).9.3; 80(79).11.1; 80(79).17–20 | how Dio wrote his history; Pertinax killed; auction bids; Julianus in Senate; Julianus dines; Julianus killed; 150,000 at Lugdunum; speech of 197; Ctesiphon; Hatra; Plautianus statues; Domna to philosophy; Plautianus killed; 50,000 dead in Britain; dying advice; Severus born; Geta killed; 20,000 killed / Papinian; Macedonian phalanx; taxes, citizenship; exactions, sword remark; Geta's name banned; Domna's correspondence; Alexandria massacre; Caracalla killed; Macrinus a Moor; Domna starves; peace with Artabanus; recruits on old terms; Maesa wins legion; 280 million a year; Macrinus defeated; first non-senator; marries a Vestal; Elagabal above Jupiter; Elagabalus killed | Loeb 73, margin LXXII; Loeb 74, trad 73 (no numeral shown; chain); Loeb 76, trad 75 (chs 4-16; chain); Loeb 77, trad 76 (chain); Loeb 78, trad 77 (chain); Loeb 79, trad 78 (chain); Loeb 80, margin LXXIX (chs 1-21) | CONFIRMED |
| kb/rome/r-7.4.md:7 | 75(74).1.1–2; 75(74).2.4–6; 75(74).6–8; 75(74).10–14; 75(75).3.2–3 | praetorians banished; Italian youth; Niger defeated; Byzantium siege; Mesopotamia "constant wars" | Loeb 75 (page refused) | NOT CHECKED |
| kb/rome/r-7.4.md:7 | 80(80).1.1; 80(80).1.2–3; 80(80).2.2; 80(80).3–4; 80(80).4.2–5.1 | Ulpian prefect; Dio seldom in Rome; Ulpian killed; Ardashir; Dio's consulship outside Rome | Loeb 80, Alexander chs 1-5 = trad 80 (restart; no numeral) | SLIP |
| kb/rome/r-7.5.md:6 | 77(76).10 | Bulla Felix | Loeb 77, trad 76 (chain) | CONFIRMED |

## Table B: every single-number citation in Loeb 61-80
| citation as written | file:line (each occurrence) | passage | Loeb book / margin per source | verdict |
|---|---|---|---|---|
| 60.29 | kb/rome/r-13.5.md:8 | start of epitome text (r-13.5 note) | Loeb 61, margin LX (trad 60.29-35) | SLIP |
| 60.31.2 | kb/rome/r-13.5.md:8, rome/13.5-seneca.md:32 | Messalina has Polybius killed | Loeb 61, margin LX | SLIP |
| 60.35.3 | kb/rome/r-7.1.md:7, rome/7.1-the-julio-claudians.md:107 | "Pumpkinification" | Loeb 61, margin LX | SLIP |
| 61.3.1 | kb/rome/r-13.5.md:8, kb/rome/r-7.1.md:7, kb/rome/unit-13.md:219, rome/13.5-seneca.md:40, rome/7.1-the-julio-claudians.md:111 | Seneca writes Nero's speech | Loeb 61, margin LXI (trad 61.1-10) | CONFIRMED |
| 61.4.1 | kb/rome/r-13.5.md:8, rome/13.5-seneca.md:40 | Seneca and Burrus rule | Loeb 61, margin LXI | CONFIRMED |
| 61.10 | kb/rome/r-13.5.md:8, rome/13.5-seneca.md:52, rome/13.5-seneca.md:56 | charges against Seneca | Loeb 61, margin LXI | CONFIRMED |
| 61.10.2 | rome/13.5-seneca.md:171, rome/13.5-seneca.md:34 | book from exile, hypocrisy | Loeb 61, margin LXI | CONFIRMED |
| 61.12.1 | kb/rome/r-13.5.md:8, rome/13.5-seneca.md:46 | Seneca urged Agrippina's murder | Loeb 62, margin LXI (trad 61.11-21) | SLIP |
| 62.1.1 | kb/rome/r-7.1.md:7, rome/7.1-the-julio-claudians.md:119 | 80,000 dead | Loeb 62, margin LXII (trad 62.1-29) | CONFIRMED |
| 62.2 | kb/rome/r-7.5.md:6, kb/rome/unit-7.md:182, rome/7.5-how-the-empire-worked.md:106, rome/7.5-how-the-empire-worked.md:116 | Seneca's loans | Loeb 62, margin LXII | CONFIRMED |
| 62.2.1 | kb/rome/r-13.5.md:8, kb/rome/r-7.1.md:7, rome/13.5-seneca.md:52, rome/7.1-the-julio-claudians.md:121 | Seneca's loans | Loeb 62, margin LXII | CONFIRMED |
| 62.12.6 | kb/rome/r-7.1.md:7, rome/7.1-the-julio-claudians.md:121 | Boudica dies of illness | Loeb 62, margin LXII | CONFIRMED |
| 62.16–18 | kb/rome/r-7.1.md:7, rome/7.1-the-julio-claudians.md:125, rome/7.1-the-julio-claudians.md:193 | the fire | Loeb 62, margin LXII | CONFIRMED |
| 62.18 | greece/10.12-troy-after-antiquity.md:27, kb/greece/r-10.12.md:6 | Nero sings of Troy | Loeb 62, margin LXII | CONFIRMED |
| 62.24.1 | rome/13.5-seneca.md:137 | Seneca and Rufus in the plot | Loeb 62, margin LXII | CONFIRMED |
| 62.25 | kb/rome/r-13.5.md:8 | Seneca's death | Loeb 62, margin LXII | CONFIRMED |
| 62.25.1–2 | rome/13.5-seneca.md:137 | Seneca's death, Paulina | Loeb 62, margin LXII | CONFIRMED |
| 63.17.5–6 | kb/rome/r-7.1.md:7, kb/rome/unit-7.md:29, rome/7.1-the-julio-claudians.md:133 | Corbulo "Your due!" | Loeb 62, margin LXIII (trad 63.1-21) | SLIP |
| 65.13.2 | kb/rome/r-13.6.md:8 | gloss "Loeb 65.13.2" in r-13.6 | Loeb 65, margin LXVI | CONFIRMED (as a Loeb reference) |
| 66.13 | kb/rome/r-13.6.md:8 | gloss "Boissevain 66.13" in r-13.6 | Loeb 65, margin LXVI | LABEL (see section 4) |
| 66.15 | kb/rome/r-7.2.md:6, kb/rome/unit-7.md:75, rome/7.2-the-year-of-four-emperors-and-the-flavians.md:78 | Berenice on the Palatine | Loeb 65 (chs 1-16), margin LXVI; Loeb 66 begins at ch.17 | SLIP |
| 66.25 | kb/rome/r-7.2.md:6, rome/7.2-the-year-of-four-emperors-and-the-flavians.md:84 | nine thousand animals | Loeb 66 (chs 17-26), trad 66 | CONFIRMED |
| 66.25.2–3 | kb/rome/r-9.4.md:7, rome/9.4-bread-baths-and-games.md:101, rome/9.4-bread-baths-and-games.md:159 | flooding, sea fight | Loeb 66, trad 66 | CONFIRMED |
| 67.7 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:51 | Decebalus subsidies | Loeb 67, no numeral | CONFIRMED |
| 67.13 | kb/rome/r-13.4.md:10, kb/rome/unit-13.md:182, rome/13.4-cato-and-the-stoic-opposition.md:140, rome/13.4-cato-and-the-stoic-opposition.md:76, rome/13.4-cato-and-the-stoic-opposition.md:90 | Senecio | Loeb 67, no numeral | CONFIRMED |
| 68.1.2 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:25 | informer slaves executed | Loeb 68, no numeral (displaced LXXV fragment only) | CONFIRMED |
| 68.3 | kb/rome/r-10.5.md:9, kb/rome/unit-10.md:213, rome/10.5-capstone-the-whole-thing-in-one-sitting.md:164 | Nerva adopts Trajan | Loeb 68 | CONFIRMED |
| 68.3.3 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:140, rome/7.3-the-adoptive-emperors.md:25 | Aelianus | Loeb 68 | CONFIRMED |
| 68.3.4 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:25, rome/7.3-the-adoptive-emperors.md:37 | adoption of Trajan | Loeb 68 | CONFIRMED |
| 68.13 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:51 | Danube bridge | Loeb 68 | CONFIRMED |
| 68.14.5 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:57 | Arabia annexed | Loeb 68 | CONFIRMED |
| 68.15.1 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:51 | 123 days of games | Loeb 68 | CONFIRMED |
| 68.19–20 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:57 | Parthamasiris | Loeb 68 | CONFIRMED |
| 68.29.1 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:57 | wish to go to India | Loeb 68 | CONFIRMED |
| 68.29–30 | greece/11.8-death-body-and-afterlives.md:120, kb/greece/r-11.8.md:13, kb/greece/unit-11.md:257 | India; Alexander's room | Loeb 68 | CONFIRMED |
| 68.31 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:57 | Hatra | Loeb 68 | CONFIRMED |
| 68.32 | kb/rome/r-7.3.md:8, kb/rome/r-7.5.md:6, kb/rome/unit-7.md:119, kb/rome/unit-7.md:182, rome/7.3-the-adoptive-emperors.md:130, rome/7.3-the-adoptive-emperors.md:57, rome/7.5-how-the-empire-worked.md:106, rome/7.5-how-the-empire-worked.md:116 | Jewish diaspora revolt | Loeb 68 | CONFIRMED |
| 69.1 | kb/rome/r-10.5.md:9, kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/10.5-capstone-the-whole-thing-in-one-sitting.md:164, rome/7.3-the-adoptive-emperors.md:148, rome/7.3-the-adoptive-emperors.md:37, rome/7.3-the-adoptive-emperors.md:41 | Plotina and the adoption | Loeb 69, no numeral | CONFIRMED |
| 69.2 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:63 | no senator killed | Loeb 69 | CONFIRMED |
| 69.4 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:83 | Apollodorus | Loeb 69 | CONFIRMED |
| 69.6.3 | kb/rome/r-7.5.md:6, rome/7.5-how-the-empire-worked.md:128, rome/7.5-how-the-empire-worked.md:16 | "cease being emperor" | Loeb 69 | CONFIRMED |
| 69.7.1 | kb/rome/r-10.3.md:6, rome/10.3-reading-roman-art-and-architecture.md:96 | court in the Pantheon | Loeb 69 | CONFIRMED |
| 69.9 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:67 | camps, discipline | Loeb 69 | CONFIRMED |
| 69.11.2–3 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:73 | Antinous | Loeb 69 | CONFIRMED |
| 69.12.1–2 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:160, rome/7.3-the-adoptive-emperors.md:79 | Aelia Capitolina | Loeb 69 | CONFIRMED |
| 69.13.2 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:77 | Julius Severus | Loeb 69 | CONFIRMED |
| 69.13–14 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:130, rome/7.3-the-adoptive-emperors.md:160 | Bar Kokhba war, formula | Loeb 69 | CONFIRMED |
| 69.14.1–3 | kb/rome/r-7.3.md:8, rome/7.3-the-adoptive-emperors.md:77 | losses, formula omitted | Loeb 69 | CONFIRMED |
| 69.16 | greece/7.4-greece-under-the-empire-and-the-end-of-antiquity.md:37, kb/greece/r-7.4.md:11 | Olympieion, Panhellenion | Loeb 69 | CONFIRMED |
| 69.20 | kb/rome/r-10.5.md:9, kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/10.5-capstone-the-whole-thing-in-one-sitting.md:164, rome/7.3-the-adoptive-emperors.md:144, rome/7.3-the-adoptive-emperors.md:29 | adoption speech | Loeb 69 | CONFIRMED |
| 70.1.1 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:14, rome/7.3-the-adoptive-emperors.md:164 | Antoninus missing from copies | Loeb 70, no numeral at ch.1 | CONFIRMED |
| 71.1 | kb/rome/r-13.7.md:9, kb/rome/unit-13.md:278, rome/13.7-marcus-aurelius-a-life.md:64 | Lucilla married to Lucius (1.3) | Loeb 71, no numeral | CONFIRMED |
| 71.1.2 | kb/rome/r-13.7.md:9, kb/rome/unit-13.md:278, rome/13.7-marcus-aurelius-a-life.md:52, rome/13.7-marcus-aurelius-a-life.md:58 | Sextus the Boeotian | Loeb 71, no numeral | CONFIRMED |
| 71.2 | kb/rome/r-7.3.md:8, kb/rome/unit-7.md:119, rome/7.3-the-adoptive-emperors.md:95 | Elegeia | Loeb 71, no numeral | CONFIRMED |
| 72.31.3 | greece/7.4-greece-under-the-empire-and-the-end-of-antiquity.md:150, greece/7.4-greece-under-the-empire-and-the-end-of-antiquity.md:29, kb/greece/r-7.4.md:11 | teachers at Athens | Loeb 72, margin LXXI | SLIP |
| 76.13.2 | greece/11.8-death-body-and-afterlives.md:90, kb/greece/r-11.8.md:13, kb/greece/unit-11.md:257 | Severus locks Alexander's tomb | Loeb 76 (chs 4-16), trad 75 (chain; see section 2) | SLIP |
| 78.7–9 | greece/11.8-death-body-and-afterlives.md:121, kb/greece/r-11.8.md:13, kb/greece/unit-11.md:257 | phalanx 7.1; Aristotelians 7.3 | Loeb 78, trad 77 (chain; see section 2) | SLIP |

## 2. Pages that established each mapping
These are Bill Thayer's LacusCurtius pages reproducing Cary's Loeb. Each URL came from a WebSearch in this agent and was read with WebFetch. A "margin numeral" is a Roman-numeral heading that LacusCurtius prints in the body.

| Loeb book | URL | numerals in the body, and the chapter where each starts | mapping |
|---|---|---|---|
| 61 | https://penelope.uchicago.edu/Thayer/e/roman/texts/cassius_dio/61*.html | LX at ch.29 (runs to 35); LXI at ch.1 (page ends 10.6) | Loeb 61 = trad 60.29-35 + 61.1-10 (31.2 Polybius; 35.3 "Pumpkinification"; 61.3.1, 4.1, 10.1-3) |
| 62 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/62%2A.html | LXI at ch.11; LXII at ch.1; LXIII at ch.1 (runs to 21) | Loeb 62 = trad 61.11-21 + 62.1-29 + 63.1-21 (61.12.1 Seneca "incited"; 62.1, 2, 12.6, 16-18, 24.1, 25.1-2; 63.17.5-6 Corbulo) |
| 63 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/63%2A.html | no numeral at the opening ch.22; LXIV at ch.1 | Loeb 63 starts at trad 63.22 |
| 65 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/65%2A.html | LXVI before ch.1; no other numeral; chs 1-16 | Loeb 65 = trad 66.1-16 (12 Helvidius; 13.1a-2 expulsion, Musonius, Demetrius, Hostilianus; 15.3-5 Agrippa and Berenice) |
| 66 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/66%2A.html | none; chs 17-26 | Loeb 66 = trad 66.17-26 (25.1 nine thousand beasts; 25.2-3 flooding) |
| 67 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/67%2A.html | none; chs 1-18 | same number (7.2-4 Decebalus; 13.2 Senecio) |
| 68 | https://penelope.uchicago.edu/Thayer/e/roman/texts/cassius_dio/68*.html | none for Trajan, chs 1-33; a displaced Severan fragment headed LXXV between ch.30 and ch.31 | same number |
| 69 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/69*.html | none | same number (1.3-4, 2.4, 4, 6.3, 7.1, 9.2-3, 11.2-3, 12.1-2, 13.2, 14.3, 16.1-2, 20.2-5) |
| 70 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/70*.html | none at ch.1; LXIX on a displaced fragment ("15 3 When Pharasmenes"); LXXI before "1 1 So much of the account of Antoninus is now extant" at the end | Loeb 70 = trad 70 (1.1 the gap in Dio's copies), then trad 71.1.1 |
| 71 | https://penelope.uchicago.edu/Thayer/e/roman/texts/cassius_dio/71*.html | none; begins at 1.2 | trad 71 (1.2 Sextus; 1.3 Lucilla; 2 Vologaesus, Elegeia) |
| 72 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/72%2A.html | LXXI at the start; no other numeral; chs 1-36 | Loeb 72 = trad 71 throughout (6, 8-9, 17, 22, 24, 27-29, 31.3, 33, 34, 35, 36.1, 36.3-4) |
| 73 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/73*.html | LXXII before ch.1; no other numeral; chs 1-24 | Loeb 73 = trad 72 (2, 4.4, 9, 12.4, 13, 14.3, 15.2-3, 19.3, 21.1-2, 22.2, 22.4-5, 23) |
| 74 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/74%2A.html | none (checked twice); chs 1-17 starting at 1 | trad 73, from the chain below (10, 11.4-5, 12, 13, 17.4-5) |
| 75 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/75%2A.html | FETCH REFUSED (robots_disallowed); not retried | NOT CHECKED |
| 76 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/76%2A.html | none at the opening ch.4; displaced fragments headed LXXIV (9.5) and LXXV (5.4) after ch.8; then chs 9-16 | trad 75.4-16 (6.1, 8.1-4, 9.4, 10-13, 13.2 tomb, 14.6, 15.6-7, 16.4) |
| 77 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/77%2A.html | none (checked twice); chs 1-17 starting at 1 | trad 76 (4.3-5 Plautianus, 10 Bulla, 13.2, 15.2, 17.4) |
| 78 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/78%2A.html | none (checked twice); chs 1-24 starting at 1 | trad 77 (2.3-4, 4.1, 7.1, 7.3, 9.4, 10.4, 12.5, 18.2, 22-23) |
| 79 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/79%2A.html | none (checked twice); chs 1-41 | trad 78 (5, 11, 23-24, 27, 28, 31-32, 36, 38-40, 41) |
| 80 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/80%2A.html | LXXIX before ch.1 (Elagabalus, chs 1-21); no numeral where the numbering restarts at ch.1 for Alexander (chs 1-5 and a fragment) | trad 79 (9.3, 11.1, 17, 20.2), then trad 80 (1.2-3, 2.2, 3.2-4.1, 4.2, 5.1) |
| (home) | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/ | n/a | Cary follows Boissevain's numbering. Margin numerals mark "only the principal text of Dio". |

How Loeb 74 to 80 were mapped (inference, stated plainly). For these books LacusCurtius shows no numeral at the head of Loeb 74, 77, 78, 79 or at Alexander's section of Loeb 80. The chapter numbers follow the traditional book: Loeb 66 opens at ch.17, Loeb 76 at ch.4, Loeb 61 at 60.29 and Loeb 63 at 63.22. A restart at ch.1 therefore marks a new traditional book. The pages read give these anchors:
- LXXII printed at Loeb 73 ch.1, running to ch.24.
- A restart at Loeb 74 ch.1, which makes it trad 73.
- Loeb 75, not read.
- Loeb 76 opens at ch.4 with no numeral, which makes it trad 75 continued. Loeb 75 must therefore end with trad 75.1-3.
- Restarts at Loeb 77, 78 and 79, which make them trad 76, 77 and 78.
- LXXIX printed at Loeb 80 ch.1.

The chain from LXXII to LXXIX has no slack, so it fixes 74(73), 76(75), 77(76), 78(77) and 79(78). The fragment headings on the Loeb 76 page (LXXIV, LXXV) agree with it. So does the title of A. G. Scott's commentary, "books 79(78)-80(80)", seen only in search results. The 7.4 and 10.5 citations in these books are marked CONFIRMED on that basis. The checker should know that no LacusCurtius page shows those five margin numerals directly. The Internet Archive scan of Loeb vol. IX did not come up in four searches (only vols. 6 and 8 did), so it was not used.

Cary's own notes cite cross-references inconsistently: "LXI (LXII).18" on the Loeb 66 page, "lxii (lxi).18" on the Loeb 69 page, and "LXXIV (LXXV).11" on the Loeb 76 page. They were not used as evidence.

## 3. Counts (per citation occurrence)
- **List A** (two numbers): 211 occurrences in 9 Rome unit files and 9 Rome bibliography files. **190 confirmed, 10 slips** (all `80(80)`, in 7.4 and r-7.4), **11 not checked** (all Loeb 75: `75(74)` x9 and `75(75)` x2; the two `75(75)` are also conditional slips of form). No reversed pair, no off-by-one and no out-of-range chapter turned up.
- **List B** (single number, Loeb 61-80 or apparently so): 164 occurrences in scope. Book 60 chapters 1-28 are excluded because they sit before the LX numeral on the Loeb 61 page, so Loeb 60 = trad 60.1-28. **142 confirmed** (books 61.1-10, 62, 66.17-26, 67-71, which match), **22 slips**, **0 not checked**. One of the 142 is r-13.6's gloss "Boissevain 66.13". The number is the right traditional one, but the label is wrong (section 4).
- Not Cassius Dio and left out: Suetonius (*Julius*, *Augustus*, *Tiberius*), Plutarch (*Alexander*), Catullus, Seneca's *Letters*, Sallust, Livy, Justinian's *Novel* 78.5, and journal volume numbers.

## 4. A wrong label (not a number slip, separate from the counts)
Ten places describe the bracketed number as "Boissevain's". This is backwards. Cary's Loeb follows Boissevain's division (Thayer's Cassius Dio home page: Cary "follows the standard system used in the Boissevain edition"). So the first number is the Loeb's and Boissevain's, and the bracketed number is the traditional one printed in the margin. The numbers themselves are right. Proposed wording follows; every current text occurs once in its file:
| file:line | current text | replacement |
|---|---|---|
| courses/rome/7.3-the-adoptive-emperors.md:14 | `with Boissevain's in brackets where they differ` | `with the traditional book number, printed in the Loeb's margin, in brackets where they differ` |
| courses/rome/7.4-the-severans-and-the-citizenship-of-212.md:14 | `with Boissevain's in brackets, since the two editions number these books differently` | `with the traditional book number, printed in the Loeb's margin, in brackets, since the two numberings differ in these books` |
| courses/rome/13.7-marcus-aurelius-a-life.md:16 | `with Boissevain's in brackets (72(71).34)` | `with the traditional number from the Loeb's margin in brackets (72(71).34)` |
| kit/bibliography/rome/r-7.3.md:8 | `with Boissevain's in brackets where they differ` | `with the traditional (margin) number in brackets where they differ` |
| kit/bibliography/rome/r-7.4.md:7 | `with Boissevain's in brackets where the two differ` | `with the traditional (margin) number in brackets where the two differ` |
| kit/bibliography/rome/r-7.5.md:6 | `Loeb book 77, Boissevain 76,` | `Loeb book 77, traditional 76,` |
| kit/bibliography/rome/r-13.3.md:23 | `(Loeb numbering, Boissevain's in brackets;` | `(Loeb numbering, the traditional margin number in brackets;` |
| kit/bibliography/rome/r-13.4.md:10 | `Loeb book numbers with Boissevain's in brackets (Loeb number not verified).` | `Loeb book numbers with the traditional (margin) number in brackets.` (this check confirmed Loeb 65.12 and 65.13 on LacusCurtius, so "(Loeb number not verified)" can go if the auditor accepts it) |
| kit/bibliography/rome/r-13.6.md:8 | `(Loeb 65.13.2, Boissevain 66.13:` | `(Loeb 65.13.2, traditional 66.13:` |
| kit/bibliography/rome/r-13.7.md:3 | `Dio is cited by the Loeb book numbers with Boissevain's in brackets;` | `Dio is cited by the Loeb book numbers with the traditional (margin) number in brackets;` |

kit/bibliography/rome/r-13.5.md:8 says "(Loeb book numbers; ...)" but cites single numbers that are traditional where the two differ. The fixes in section 1 deal with this.

## Content notes outside this check (flagged only)
- The Rome 13.7 and 7.3 citations 72(71).33 for the death on 17 March and the physicians: my fetch summary put the death notice and the physicians in ch.34, with the age in an unnumbered passage before 35. The book mapping is confirmed, but the chapter was not checked.
- Rome 7.4:32 cites 77(76).17.4 for "born at Lepcis Magna ... on 11 April 145". The LacusCurtius 77.17.4 gives the date but does not name Lepcis.
- Loeb 68's page has a displaced Severan fragment headed "LXXV" between ch.30 and ch.31, and the Loeb 70 page has one headed "LXIX". Neither affects any cited chapter.
