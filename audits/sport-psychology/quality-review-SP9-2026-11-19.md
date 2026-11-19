---
audit: quality review
unit: SP9 · Wellbeing, red flags and referral
course: sport-psychology
model: claude-opus-5-5
date: 2026-11-19
chat: https://claude.ai/code/session_01KMmgR2iBxJPhjunwizCmdb
verdict: keep · 0 error, 7 should-fix, 9 minor (applied below)
---

The reviewer's final report, verbatim, from its hand-back. Saved before any finding was applied.

Model: claude-opus-5-5. Quality review of SP9 (docs/public-courses.md §3 rule 13), 19 Nov 2026. Packet read: files/SP9-wellbeing-red-flags-and-referral.md, briefs/SP9.txt, syllabus-flags.md, case-facts.md, sourcing-standard.md, audit-units-SKILL.md. Live search used; every fetch was of a URL a search in this agent returned.

Verdict: SP9 · keep · 0 error, 7 should-fix, 9 minor

(Keep by audit-units §3: keep = no errors. The should-fix lines are still exact replacements and should be applied.)

## Findings

[should-fix] [accuracy] §1 Elite adults; Current: "and describes the overall prevalence as similar to that in the general population"; Problem: the consensus says only that the prevalence of *depressive symptoms* appears similar in elite athletes and the general population. "Overall prevalence" reads as all mental health symptoms, which goes further than the source; Fix: "and says that the prevalence of depressive symptoms in elite athletes and in the general population appears to be similar"; Basis: Reardon et al. 2019, "the prevalence of depressive symptoms in elite athletes and the general population appears to be similar", https://bjsm.bmj.com/lookup/doi/10.1136/bjsports-2019-100715
[should-fix] [accuracy] §2 What a coach does with risk factors; Current: "Sara (fictional) carries several factors the sources name at once: eight months back from a hamstring injury, her first senior season, university away from home."; Problem: of these three, the sources opened name only injury (FEPSAC summary; Reardon et al.). Neither a first senior season nor living away from home is named in Kuettel & Larsen's abstract, Gwyther et al.'s abstract, FEPSAC's summary or the IOC consensus. The unit's preceding sentence attributes these to SP2's transitions; Fix: "Sara (fictional) carries one factor the sources opened name, an injury and the months back from it (eight months back from a hamstring injury), and two of SP2's transitions at once: her first senior season and university away from home."; Basis: FEPSAC position statements page (injuries, overtraining, career termination), https://fepsac.com/position-statements/ ; Gwyther et al. 2024 abstract (sex, athlete status, relationships with coaches, parents and peers), https://pubmed.ncbi.nlm.nih.gov/39122370/
[minor] [population] §2 grade bracket; Current: "ages not given in the abstracts, so for under-18s outside the sampled ages as far as is known"; Problem: Gwyther et al.'s abstract gives ages (elite youth, mean age 12 to 17). The protective factors in the sentence come only from Kuettel & Larsen, whose abstract gives none; Fix: "the protective factors are Kuettel and Larsen's, whose abstract gives no ages, so for under-18s outside the sampled ages as far as is known; Gwyther et al.'s risk factors come from elite youth athletes of mean age 12 to 17"; Basis: https://experts.mcmaster.ca/display/publication3461383 (abstract: "elite youth athlete populations (mean age 12-17 years)")
[should-fix] [label] §4 introduction; Current: "No source opened gives a coach a number of days or weeks for any sign."; Problem: the "What you can see" lists under low mood, disordered eating, injury and perfectionism (and the vignettes) cite no source. Only the general toolkit line (moods, performance, social interactions, p. 29) and the ISSF red flags are sourced. The unit says the time points are its own but not the sign lists, so they read as sourced (Part 1: "A claim that cannot be sourced is said to be unsourced"); Fix: "No source opened gives a coach a number of days or weeks for any sign. The lists of what you can see under each heading are this unit's own, drawn from the sources named in each paragraph; no source opened gives a coach a tested list of signs, and they are not a checklist."; Basis: sourcing-standard Part 1 per unit; IOC toolkit p. 29, https://stillmed.olympics.com/media/Document Library/IOC/Athletes/Safe-Sport-Initiatives/IOC-Mental-Health-In-Elite-Athletes-Toolkit-2021.pdf
[should-fix] [accuracy] §4 Burnout and overtraining; Current: "Add what you can see on the training log: performance falling over weeks while training holds or rises, illness or niggles that keep returning."; Problem: these signs of overtraining have no source. Meeusen et al. (2013) and Brenner et al. (2024) were not opened (F32, F140), and in this review PubMed served reCAPTCHA for Meeusen (PMID 23247672), so it remains unopened at an allowed address; Fix: "Add what you can see on the training log (the unit's own list; the overtraining consensus statements were not opened, F32): performance falling over weeks while training holds or rises, illness or niggles that keep returning."; Basis: syllabus-flags F32, F140; sourcing-standard Part 7 line 1
[should-fix] [population] §5 What it does not do; Current: "It was written for elite athletes, mostly adults; using it with a squad of 11- to 17-year-olds is this unit's inference."; Problem: no source opened says "mostly adults". The paper's abstract gives an age (16 and older) only for the companion assessment tool, SMHAT-1, and the ISSF page gives no age or level for the recognition tool; Fix: "The paper that presents it concerns elite athletes, and its companion assessment tool is for those aged 16 and older; neither the paper's abstract nor the ISSF page gives an age for the recognition tool, so using it with a squad of 11- to 17-year-olds is this unit's inference."; Basis: Gouttebarge et al. 2021 abstract, https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract ; ISSF page, https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool
[minor] [attribution] §3 Of clubs and organisations; Current: "pp. 39, 47, 51 and 61, read 18 Nov 2026"; Problem: in the toolkit as read, p. 61 is "Career Transition Support". The referral lead ("designate a referral lead") is on p. 62 (§3.3.7 checklist), and making the plan known is on pp. 50 to 51 and 63. The text extraction printed only odd folios, so ±1 page is possible; Fix: "pp. 39, 47, 50 to 51 and 62 to 63, read 18 Nov 2026"; Basis: IOC toolkit 2021, https://stillmed.olympics.com/media/Document Library/IOC/Athletes/Safe-Sport-Initiatives/IOC-Mental-Health-In-Elite-Athletes-Toolkit-2021.pdf
[minor] [coverage] §6 The words, step 3; Current: "An editorial reviewing 13 papers (2001 to 2013)"; Problem: the common coaching belief that asking about suicide plants the idea is the claim under examination here, but the unit never names it as a claim (Part 7: a popular claim is named and set against its evidence). Whether it is on the course's seed list could not be checked, because the list is not in the packet; Fix: "The common belief that asking about suicide puts the idea into someone's head is not supported by the evidence opened here: an editorial reviewing 13 papers (2001 to 2013)"; Basis: Dazzi et al. 2014, https://www.cambridge.org/core/product/FCAEE9E5BC840D76CF10AEBECD921AC9
[should-fix] [label] Deliverable, introduction; Current: "every other fact about Sara comes from the case register or earlier units' added facts."; Problem: five facts this unit invented, and which the register now records under SP9, are not marked *added*: (1) worry, nausea or sleep beyond competition "not yet asked" (table A); (2) the coach records her words with the date (§4 and table A); (3) follow-up every two weeks after her first appointment (plan B); (4) the coach's other groups include minors (plan B, travel; script C3); (5) the coach knows about her five hours' sleep and raises it in C1, though the base register says he has not asked. The sentence as written is therefore false; Fix: "every other fact about Sara comes from the case register or earlier units' added facts, except these, also invented by this unit and not marked below: that she has not yet been asked whether her worry, nausea or poor sleep spreads beyond competition; that her coach records her words as she says them, with the date; his follow-up every two weeks after her first appointment; that his other two groups include athletes under 18; and that he knows of her short sleep and raises it in script C1, though the case register says he has not asked about it."; Basis: case-facts.md, base entry "has not asked about the sleep" and SP9 rows 120 to 125
[minor] [coverage] Deliverable B, Competition-day version; Current: "covers my other athlete;"; Problem: SP8's case facts give two athletes from the coach's other groups competing on the first day, and the cover coach is named only for the long jumper's warm-up. The singular hides the second athlete; Fix: "covers my other athletes;"; Basis: case-facts.md, SP8 row "Two athletes from her coach's other groups compete on the first day..."
[should-fix] [figure] §7 decision figure, caption; Current: "is the unit's own.\", \"root\"" (in the file: is the unit's own.", "root"); Problem: the tree sends every non-red-flag sign to the "about two weeks" test. Section 4 and table A say eating, weight or body concerns have no two-week wait, so a reader following the figure would wait on a skipped-meal sign. The figure does not draw this exception and the caption does not say it is left out; Fix (caption, exact JSON fragment): "is the unit's own. Not drawn: a sign about eating, weight or body skips the two-week wait and goes at once to the person for medical concerns (section 4).\", \"root\"" (in the file: is the unit's own. Not drawn: a sign about eating, weight or body skips the two-week wait and goes at once to the person for medical concerns (section 4).", "root"); Basis: the unit's §4 ("For this area there is no two-week wait") and table A row "First sign: no waiting"
[minor] [figure] §3 matrix figure, caption; Current: "as sections 3 and 8 of this unit draw it"; Problem: the rows "Recognise and first conversation" and "Decide return to play" are drawn from sections 4, 6 and 9 as well, so the caption names too few sections; Fix: "as sections 3, 4, 6, 8 and 9 of this unit draw it"; Basis: the unit's §§4, 6, 9
[minor] [deliverable] Deliverable A; Current: "**Built for Sara.** Red flags first, then concerns."; Problem: the brief gives the columns as "sign, how long, what to do, who to call", but the table orders them Sign, Who to call, What to do, How long. All four are present, and the order is not explained; Fix: "**Built for Sara.** Red flags first, then concerns. The columns are the brief's four (sign, how long, what to do, who to call), with who to call placed second so that the number is read first."; Basis: briefs/SP9.txt, Deliverable
[minor] [bibliography] Sources, Bissett; Current: "Bissett, Kroshus, Hebard (initials not shown on the page read)."; Problem: the authors' first names are on record (James E. Bissett, Emily Kroshus, Stephen Hebard). The DOAJ record lists Kroshus first, so the order is unconfirmed at the publisher; Fix: "Bissett JE, Kroshus E, Hebard S (names from the DOAJ record, https://library.kab.ac.ug/Record/doaj-art-de8556f2179d44e7a0a92a141fc25044/Description, which lists Kroshus first; order as in the course's seed list, not checked at the publisher)."; Basis: that record
[minor] [bibliography] Sources, Walsh; Current: "(authors as in SP8's record of the article; the course's seed list gives Walsh, et al.)"; Problem: the full author list is now confirmed on two records, so the entry no longer needs to rely on SP8. Records disagree on the issue: University of Arizona gives 55(7):356–368, BISp/LIDA gives 55(6); Fix: "(authors as on the LJMU repository copy, https://researchonline.ljmu.ac.uk/id/eprint/16297/, and the University of Arizona record, https://experts.arizona.edu/en/publications/sleep-and-the-athlete-narrative-review-and-2021-expert-consensus-/, which gives 55(7):356–368; the BISp record gives issue 6)"; Basis: those records
[minor] [population] §4 Perfectionism; Current: "A meta-analysis of 14 studies (3,496 athletes aged 11 to 55)"; Problem: the samples are not all elite (they include school and university athletes and dancers, as well as junior elite), although the title says "Elite Athletes". The unit's "athletes" is right, but the sample's range should be stated; Fix: "A meta-analysis of 14 studies (3,496 athletes aged 11 to 55, from school and university athletes to junior elite, despite the title's \"elite\")"; Basis: Yang et al. 2023, https://www.mdpi.com/2227-9032/11/10/1417

## Fresh check (audit-units §3), items 1 to 7

(1) Coverage. Every brief item is present and in order:
- prevalence: covered, but thin, because the meta-analysis was not opened (F131) and the unit says so;
- risk and protective factors: covered;
- what the consensus statements ask: covered;
- signs with how long and how much: covered, with overtraining thin (should-fix above);
- IOC tool, read on its page and dated: covered;
- first conversation: covered;
- urgent risk: covered;
- referral route: covered;
- return and follow-up: covered;
- the coach's own wellbeing: covered.

(2) Accuracy. 19 sources opened, all PASS on the claims checked (Confirmed below), except two stretches: the §1 "overall prevalence" and the §2 Sara risk factors (should-fix).
(3) Figures say whose they are: PASS.
(4) Labels: correlation called correlation (Yang): PASS. The unsourced sign lists are not labelled (should-fix).
(5) Deliverable: present in full for Sara, then as templates whose blanks say what goes in them. It follows the body, and the table's column order is minor.
(6) Errata: no audit report in the packet; pointers to SP1 to SP8 were not checkable, because those units are not in the packet.
(7) Figures:
- Fig 1 (range, §1): every label and number is in §1's text (40, 14, 28, 8, 11 to 41, 0 to 14); the caption names the section and the source; the kind fits. PASS.
- Fig 2 (matrix, §3): cells trace to §§3, 4, 6, 8 and 9; the caption names too few sections. FIX (minor, above).
- Fig 3 (decision, §7): labels trace to §§4 and 7; the eating exception is missing. FIX (should-fix, caption above).
- Fig 4 (flow, §8): steps trace to §§6, 8 and 9; caption fine; kind fits. PASS.

## Seven passes

Claims: PASS, apart from the 3 accuracy findings above. Opened:
- Reardon (publisher's page, full text in two parts);
- Gwyther (PubMed and McMaster abstract);
- Kuettel & Larsen (publisher's abstract);
- FEPSAC summary;
- Henriksen (publisher's page);
- Bissett (publisher's full text);
- IOC toolkit PDF;
- ISSF page;
- Gouttebarge 2021 (abstract);
- Mountjoy (PubMed);
- Walsh (LJMU repository copy, not the bjsm page the unit used);
- Tranaeus (St Mary's repository copy);
- Yang (MDPI);
- Dazzi (Cambridge page and PDF);
- SafeSport;
- NSPCC (two pages);
- Sport Integrity Australia;
- Kang & Lee (Frontiers).

Not opened: none of the cited works. Walsh and Tranaeus were read on repository copies of the published articles, because the unit's publisher addresses were not returned by my searches.

Bibliography: FIX (minor, 2 entries above). Checked field by field:
- Reardon 53(11):667–699, first three authors: PASS (Arizona record).
- Gwyther, all fields: PASS (McMaster, PubMed).
- Kuettel & Larsen 13(1):231–265: PASS (BISp); initials not verified.
- Henriksen, seven authors, 18(5):553–560, 2020: PASS (idrottsforum issue listing; BL "Issue 5 (2nd September 2020)").
- Gouttebarge 2021 55(1):30–37: PASS (BISp); 15 authors: PASS (publisher).
- Mountjoy 57(17):1073–1097: PASS (PubMed).
- Tranaeus, authors and 54(7):1733–1748: PASS (repository PDF, BISp).
- Yang, authors and 11(10):1417: PASS.
- Dazzi 44:3361–3363, editorial: PASS (Cambridge PDF).
- Kang & Lee 16:1666035: PASS.
- Walsh: authors PASS; issue disputed (7 or 6).
- Bissett: 6(1):e000676 PASS; initials, see finding.
- No nonexistent reference.

Source log: PASS. Every abstract-only source (Gwyther, Kuettel & Larsen, Mountjoy, Gouttebarge 2021, Dazzi, Henriksen in part) says so at the point of citation. Every Sources entry is cited in the text. Gouttebarge 2019 and Moesch 2018 are named as not opened and carry no claim.

Grades: PASS with notes.
- The grades follow the preamble's summary of SP1's key and the SP2 convention ("[practice; ...; the studies behind it were not opened]").
- Walsh's sleep ranges are graded [weak], "as SP2 grades them", while the preamble's convention would give [practice]. This is the open conflict F47 [cross-unit], so no fix is given.
- Yang [moderate] fits "meta-analysis of small or mixed studies".
- Dazzi [weak, outside sport] fits.
- §2 is graded [weak] on scoping reviews of correlational and qualitative work. That is defensible, but qualitative findings are not an "association".

Population: FIX (2 minor, 1 should-fix above).
- Labelled correctly: Bissett's adult athletes; Gwyther's elite youth of mean age 12 to 17, travelling internationally; Kang & Lee's elite coaches only; Walsh's inference for under-18s; Dazzi's adolescents and adults, outside sport; the tool used with 11 to 17 as inference.
- No sample is stated for Tranaeus. It is a consensus, so this is acceptable.

Scope and safety: PASS.
- Nothing teaches assessment, diagnosis or treatment. "Asking is not assessing" is stated, and return is left to a licensed practitioner.
- No weight-loss method, calorie figure or target weight.
- No self-harm method; §7 says "Do not ask for details of how".
- Every legal or reporting duty is put as a question with the body to consult.
- SafeSport, NSPCC and Sport Integrity Australia are given as examples, "not stated here as yours".
- The information-not-advice line is in the preamble.
- No real athlete, coach or club is named.

Any sport: PASS.
- Body examples outside the case: rowing, basketball, gymnastics, cycling, volleyball and swimming (2), plus the pitch, pool and office settings.
- Case: athletics/Sara (sections 2 and 4: 4 mentions), judo/Dani (1), football/Milan (1).
- Athletics supplies about 4 of about 13 body examples, at or under a third. The deliverable is Sara's by the brief.
- No sport supplies more than a third. The packet gives no description of the owner, so "recognisable to the owner's reader" could only be checked as: no person, club, place or region is named.

## Sourcing-standard Part 7, line by line

1 sourced where made: FIX (overtraining signs; sign lists). 2 source types: PASS. Walsh and Tranaeus were read on repository copies of the publisher's article, and the unit cites the publisher's pages. 3 no blogs or press: PASS. The NSPCC "news-and-blogs" page is NSPCC Sport's own safeguarding guidance, the issuing body's page. 4 source log: PASS. 5 bibliography: FIX (minor). 6 grades: PASS (F47 noted). 7 sample and design: PASS. 8 inference label: PASS. 9 effect sizes in the source's terms (r with 95% CI, I²): PASS. 10 popular claims: minor (asking about suicide); the seed list was not in the packet. 11 coach's part: PASS. 12 weight and self-harm: PASS. 13 law: PASS. 14 real names: PASS. 15 three kinds of sport, ≤⅓: PASS. 16 case labelled "(fictional)" and agreeing: FIX (unmarked added facts). 17 private terms: the script was not runnable here, and no owner details appear. 18 search-on dates: PASS (18 Nov 2026 on every page). 19 deliverable built and templated: PASS. 20 not advice without evidence: PASS. Every [practice] point says whose it is. 21 links as DOI links: PASS.

## Read as the coach

A coach of 10- to 25-year-olds can use it on a phone: the red-flag table opens with the urgent three steps, and the minor/adult split is explicit. Points of friction:
- The red-flag table puts "who to call" before "how long" (minor above).
- The decision figure would mislead on eating signs (should-fix above).
- The preamble's grading conventions are dense for a non-psychologist, but they are explained once.

## Brief and deliverable

Every Cover item is met in order. The deliverable is in full:
- A: red-flag table, 14 rows for Sara, plus template.
- B: referral plan for Sara, with competition-day and travel rows and the completion of SP4's table, plus template.
- C: three scripts for Sara (athlete, parent, club), plus template.

Built for Sara as the brief names. The facts the unit invents are listed in case-facts under SP9, but five are not marked in the unit (should-fix).

## Confirmed

- Reardon 2019: depressive symptoms 4% to 68%; similar to general population (for depressive symptoms); GAD 6.0% clinician-confirmed to 14.6% self-report; social anxiety 14.7%; panic 4.5%; ~64% of Olympic athletes significant insomnia symptoms; "can potentially unmask or precipitate mental health disorders"; "minimal prospective research in this area"; "Within sport, coaches are often the primary interpersonal interface with the athlete"; "Coaches can ensure that training is age and developmentally appropriate"; younger athletes, coaches communicate importance of mental healthcare to parents; "Coaches should feel comfortable discussing eating disorders and RED-S"; "develop and rehearse a mental health emergency action management plan"; "clarity on what constitutes an emergency"; review of procedures after any incident; body image "may be the strongest predictor of eating disorders in athletes". https://bjsm.bmj.com/lookup/doi/10.1136/bjsports-2019-100715
- Gwyther 2024: 33 studies, 5,826 athletes, mean age 12 to 17, travelling internationally; DE 16, anxiety 7, depression 5; DE caseness 0–14% boys, 11–41% girls; depression 7% mixed, 14%/40%; anxiety 8%/28%; caseness definition; risk factors sex, athlete status, social/relationship factors with coaches, parents, peers; competition level contradictory. https://pubmed.ncbi.nlm.nih.gov/39122370/ ; https://experts.mcmaster.ca/display/publication3461383
- Kuettel & Larsen 2020: 9 reviews, 43 empirical studies, 84% quantitative; personal and sport-environmental; qualitative: autonomy, positive relations, adequate recovery. https://informahealthcare.com/doi/abs/10.1080/1750984X.2019.1689574
- FEPSAC PS 12 (2018): injuries, overtraining, career termination; six European countries; single gold standard hard to define. https://fepsac.com/position-statements/
- Henriksen 2020: "The environment can nourish or malnourish athlete mental health"; "Sometimes 'everybody's business' means 'nobody's responsibility'" (opening confirmed); "building and maintaining a network of service providers and setting up a system of referral"; seven panellists. https://informahealthcare.com/doi/abs/10.1080/1612197X.2019.1570473
- Bissett 2020: 15 experts (2 coaches, 3 athletes, 8 licensed MH professionals, 2 health educators), all athletes over 18; two rounds; mean ≥7 of 9; three areas (culture, addressing mental health, ongoing support); "Coaches should foster team cultures that support athlete mental health"; "facilitate referral to appropriate support"; return to play "should be determined by a licensed mental health practitioner and not a coach"; maintaining athletes' privacy; moderating demands not feasible; coaches' own support questioned; country not stated. https://bmjopensem.bmj.com/content/6/1/e000676
- IOC toolkit 2021: "All sporting organisations should develop a Mental Health Emergency Action Plan (MHEAP)" (p. 47); written by medical team with licensed MH experts (p. 51); entourage check the club has one (p. 39); coaches "are in a position to recognise differences in moods, performance, social interactions" (p. 29); "significant and/or persistent" (p. 41); SMHRT-1 by the IOC MHWG for athletes, coaches, family, entourage; "not a diagnostic tool" (p. 41); "Listen to and validate the athlete's concerns"; "Offer to contact your club/team's sports medicine physician and/or licensed mental health provider"; follow up within 24 hours "to determine if further action is needed"; "Contact emergency services"; "Stay with the athlete until help arrives (if it is safe for you)"; follow MHEAP reporting procedures (p. 41); "Respect their right to make their own decisions related to seeking further help" (p. 41); "you can only encourage and support an athlete in seeking further help" (p. 39); specialist referral "will usually be made by the team doctor" (p. 39). URL above.
- ISSF page: "to recognise mental health problems but not to diagnose them"; "list of athlete experiences (thoughts, feelings, behaviours, physical changes)"; five red flags word for word as the unit gives them; "seek immediate help"; freely copied, revision needs IOC MHWG approval; undated, © 2025. https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool
- Gouttebarge 2021: SMHRT-1 "for athletes and their entourage (eg, friends, fellow athletes, family and coaches)"; SMHAT-1 for sports medicine physicians and licensed/registered health professionals, elite athletes "aged 16 years and older"; online 18 Sep 2020; 15 authors. https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract
- Mountjoy 2023: REDs harms in female and male athletes; "further evidence of the interplay between mental health and REDs"; REDs Clinical Assessment Tool version 2; 57(17):1073–1097. https://pubmed.ncbi.nlm.nih.gov/37752011/
- Walsh 2021: 7–9 h adults, 8–10 h teenagers; poor mental health incl. "maladaptive perfectionism and hyperarousal"; "refer athletes to a sleep specialist for clinical diagnosis, when necessary"; questionnaire validated in athletes; Box 2 "Bank sleep": "a poor night's sleep the night before competition should not affect their performance"; 1–3 nights partial restriction "a more real-world scenario, remains unclear". https://researchonline.ljmu.ac.uk/id/eprint/16297/
- Tranaeus 2024: "injured athletes are at risk for a variety of mental health issues, including clinical anxiety"; re-injury concerns delay or prevent return; "physical and psychological readiness to RTS do not necessarily coincide"; 7 authors. https://research.stmarys.ac.uk/id/eprint/6344/1/s40279-024-02045-w.pdf
- Yang 2023: 14 studies, 3,496 athletes, 11–55; SPP–exhaustion r = 0.150 (0.025 to 0.271), I² 91%; SPP–devaluation r = 0.138 (0.009 to 0.261), I² 88%; SOP–devaluation r = −0.246 (−0.344 to −0.143), I² 86%; overall I² 94%; heterogeneity unexplained by moderators; correlational. https://www.mdpi.com/2227-9032/11/10/1417
- Dazzi 2014: 13 papers 2001–2013, adolescents and adults, general and at-risk; none showed a statistically significant increase in ideation; editorial; 44:3361–3363; online 7 July 2014. https://www.cambridge.org/core/product/FCAEE9E5BC840D76CF10AEBECD921AC9
- SafeSport MAAPP: "All one-on-one in-program contact between an Adult Participant and a Minor Athlete must be observable and interruptible", except emergencies; "may not transport a Minor Athlete one-on-one during in-program travel"; lodging follows the one-on-one policy; last modified 23 Dec 2025; applies to the US Olympic and Paralympic Movement. https://maapp.uscenterforsafesport.org/how-it-works/
- NSPCC Sport, responding: "without leading or intrusive questions"; "I promise I won't tell anyone" / "You can't promise this"; last updated 07 Jan 2026. https://sport.nspcc.org.uk/news-and-blogs/2026-01-how-to-respond-to-child-abuse-concerns-in-your-sport/
- NSPCC Sport, away day trips: "provide adequate staff and volunteers for the trip"; "everyone must be aware of their responsibility and what to do in the event of an emergency"; used alongside the overnight-trips briefing; updated 24 Nov 2022. https://sport.nspcc.org.uk/resource-library/best-practice/away-day-trips/
- Sport Integrity Australia: ADHD stimulants "are banned in-competition"; WADA Prohibited List "S6 Stimulants"; TUE in advance or planned retroactive TUE by level; undated; no headline. https://www.sportintegrity.gov.au/what-we-do/anti-doping/substance-education/responsible-use-of-adhd-medication-sport
- Kang & Lee 2025: 101 studies 2010–2024; elite definition (professional leagues, national teams, national/international championships); burnout 40, stress 32; stressors; few interventions incl. 6-week mindfulness with US college (NCAA) coaches and 6-week mental skills with five British elite coaches; mostly Western contexts. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1666035/full

## Flags naming SP9

Dealt with in the unit:
- F3: all three sources opened (FEPSAC as its summary only); mismatch raised as F128.
- F8: key applied.
- F9: "To whom" and "Urgent route" filled in B.
- F14: SP2 convention used.
- F17: youth prevalence found, elite only; gap stated as F132.
- F21: Walsh opened.
- F24 and F38: packet notes; publisher addresses used.
- F26: age bands used.
- F48: SP1 wording kept, plus "outside the sampled ages".
- F69: §8 stop-rule route.
- F87: §8 level-3 question.
- F99: kept silent on autism.
- F100: dated on the SIA page.
- F117: both Walsh statements given.
- F121: two codes dated.
- F122: competition-day version in §10 and B.
- F123 and F124: practice kept.
- F127: resolved.

Correctly still open:
- F32: Meeusen and Brenner not opened. I also could not open Meeusen (PubMed reCAPTCHA); the unit should label its overtraining signs (should-fix).
- F47: cross-unit.
- F53 / F129: Table 4 not reproduced at the publisher.
- F54 (PDF part) / F98 / F130: SMHRT-1 PDF unread. My search returned no IOC address for it, only federation copies.
- F128: syllabus review.
- F131: Gouttebarge 2019 still unopened. PubMed returned an empty page, and no publisher page was returned.
- F132, F133, F134, F135, F136, F137, F138, F139, F140, F142, F143: open as stated.
- F141: the Mountjoy pages 1073–1097 are confirmed on PubMed. Henriksen's year 2020 is now confirmed by the idrottsforum issue listing (vol. 18, 2020, issue 5, pp. 553–560) and the BL catalogue ("Issue 5 (2nd September 2020)"); that part can close at filing.
- F149: this review.

Not dealt with: none.

## Could not verify

- IOC toolkit page numbers: the text extraction printed only odd folios, so p. 61 vs 62 (referral lead) and pp. 50/51 are ±1.
- Walsh 2021 issue number: 7 (Arizona, BL) against 6 (BISp); not read at the publisher's page.
- Bissett et al. author order and initials at the publisher: the publisher's page showed no byline; the DOAJ record lists Kroshus first.
- Kuettel & Larsen initials: no record returned them.
- Dazzi issue number: not printed in the PDF text.
- Reardon et al. insomnia 64%: which study, and which Games or country, sits behind it; the consensus cites ref. 79 only.
- IOC toolkit exact wording "serious and immediate danger to the athlete or to others": the extraction summarised it; the other emergency-pathway quotes were confirmed verbatim.
- Henriksen's "Sometimes 'everybody's business' means 'nobody's responsibility'": the opening was confirmed and the remainder was not shown in full.
- Cross-unit pointers (SP1 §9 key and rule numbers, SP3 burnout dimensions from young footballers, SP4 rows 6 and 9, SP5 stop rule, SP6 cap at level 3, SP7 states, SP8 sections): those units are not in the packet.
- Course popular-claims list (seed bibliography): not in the packet.
- `kit/private_terms.py`: not in the packet; not run.
- Gouttebarge 2019 meta-analysis, Meeusen 2013, the SMHRT-1 PDF: not opened (empty or reCAPTCHA pages; no IOC address returned by search).
