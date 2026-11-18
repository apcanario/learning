Verdict: SP9 · fix · 0 error · 8 should-fix · 12 minor

Model: claude-opus-5-5. Quality review, docs/public-courses.md §3 rule 13; fresh check of audit-units-SKILL.md §3 with its Figures paragraph. Read only /tmp/sp9-quality; web per the rule (search first, fetch only search-returned URLs). Date 18 Nov 2026.

## Findings

[should-fix] [attribution] §3; Current: "\"All sporting organisations should develop a Mental Health Emergency Action Plan (MHEAP)\""; Problem: not the source's words: the toolkit reads "All sports organisations should develop a Mental Health Emergency Action Plan", and "(MHEAP)" is not inside that sentence (Part 1: quoted words are exact); Fix: "\"All sports organisations should develop a Mental Health Emergency Action Plan\" (MHEAP)"; Basis: IOC Mental Health in Elite Athletes Toolkit 2021, https://stillmed.olympics.com/media/Document Library/IOC/Athletes/Safe-Sport-Initiatives/IOC-Mental-Health-In-Elite-Athletes-Toolkit-2021.pdf

[should-fix] [accuracy] §7; Current: "\"Stay with the athlete until help arrives\", and"; Problem: the toolkit's step continues "(if it is safe for you)"; cutting the condition removes a safety qualifier the same section needs for harm to others; Fix: "\"Stay with the athlete until help arrives (if it is safe for you)\", and"; Basis: IOC toolkit 2021, p. 41, URL above

[should-fix] [deliverable] §7 step 3; Current: "call the emergency number** where you are, and stay with the athlete until help arrives."; Problem: (a) the same safety condition is missing; (b) a sudden overwhelming-fear episode is a red flag that needs medical help at once (§4, table A, SP4 row 9), but sections 7 and the decision figure send any red flag without immediate danger to a same-day route, so a coach who judges "no danger" could delay medical help; Fix: "call the emergency number** where you are, and stay with the athlete until help arrives, if it is safe for you (IOC toolkit, p. 41). A sudden episode of overwhelming fear with marked physical symptoms needs medical help at once, whatever you judge about danger (section 4)."; Basis: toolkit p. 41 (URL above); ISSF page, https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool

[should-fix] [figure] §7 decision figure; Current: "{\"outcome\": \"Do not leave them alone; urgent route the same day\", \"tone\": 1}"; Problem: the "no immediate danger" branch tells the reader "the same day" for every red flag, including the panic-like episode the text sends to medical help at once, and table A's urgent line says "call [the urgent contact] at once"; the urgent route can delay help; Fix: "{\"outcome\": \"Do not leave them alone; urgent contact at once; sudden fear: medical help at once\", \"tone\": 1}"; Basis: unit §4 ("needs medical help at once"), table A ("call [the urgent contact] at once"); ISSF page (URL above)

[should-fix] [accuracy] §4 Perfectionism; Current: "heterogeneity was very high (I² = 94%) and unexplained"; Problem: 94% is the I² of the total effect across all 77 effect sizes; the three associations quoted have I² of 91% (SPP–exhaustion), 88% (SPP–devaluation) and 86% (SOP–devaluation); Fix: "heterogeneity was very high (I² = 94% across all effect sizes pooled; 86% to 91% for these three associations) and unexplained"; Basis: Yang et al. 2023, https://www.mdpi.com/2227-9032/11/10/1417

[should-fix] [accuracy] §4 Sleep; Current: "one of its boxed points says athletes can be confident that"; Problem: the Box 2 sentence is about athletes who have banked sleep in the nights before; without that condition it reads as a general claim the consensus does not make (F117 asks both statements to be stated as the source gives them); Fix: "one of its boxed points, on banking extra sleep in the nights before, says athletes can be confident that"; Basis: Walsh et al. 2021, Box 2 and abstract, read on the LJMU repository copy https://researchonline.ljmu.ac.uk/16297/1/Walsh%202020_%20Sleep%20and%20the%20Athlete%202021_%20Consensus%20Review_%20BJSM_%20With%20Supplementary%20Material.pdf (not the publisher's page)

[should-fix] [coverage] Deliverable B, completing SP4's table; Current: "| 1 to 4 (ordinary nerves, worry, sleep the night before, avoidance inside competition) | Nobody yet: profile, check-ins, review (SP4). | None. |"; Problem: SP4's rows 1 to 4 each carry a "When to refer" point (row 2: worry about many things beyond sport, most days; row 3: short sleep on ordinary nights for weeks; row 4: avoidance growing into whole competitions); "Nobody yet" leaves those referrals without a "To whom", the gap F54 asked SP9 to close; Fix: "| 1 to 4 (ordinary nerves, worry, sleep the night before, avoidance inside competition) | Inside the ordinary range: nobody yet; profile, check-ins, review (SP4). When the row's own \"When to refer\" is met (worry about many things beyond sport, short sleep on ordinary nights for weeks, avoidance growing into whole competitions): as rows 5 to 8. | None, unless a red flag appears. |"; Basis: filed/SP4 Deliverable B rows 1 to 4

[should-fix] [coverage] §3, SP1's scope line; Current: "The difference is raised in the notes."; Problem: the unit has no notes section, so the reader is pointed to nothing; F3 asks that a mismatch be raised as a flag on SP1, which the unit's text does not show was done (no notes in the packet); Fix: "The difference is raised as a flag on SP1 for the course's syllabus review."; Basis: flags.txt F3

[minor] [style] Preamble; Current: "; see the notes)"; Problem: as above, no notes section in the unit; Fix: ")"; Basis: unit.md

[minor] [accuracy] §4; Current: "Two weeks matches SP4's \"for weeks\" (row 3)"; Problem: SP4 sets no number; two weeks is this unit's reading of "for weeks", not a match; Fix: "Two weeks is this unit's reading of SP4's \"for weeks\" (row 3)"; Basis: filed/SP4 Deliverable B note above the table

[minor] [deliverable] §7 step 5; Current: "and do not decide yourself how serious it is."; Problem: steps 3 and 4 ask the coach to decide whether there is immediate danger; as written, step 5 contradicts them; Fix: "and do not judge how serious it is beyond step 3's one question: is there danger now, or can you not tell?"; Basis: unit §7

[minor] [label] §6 Where and when (Any sport); Current: "the side of the track, an office"; Problem: athletics supplies 5 of 14 body examples (Sara in §2 and three times in §4, plus "the track"), above a third; Fix: "the side of the pool, an office"; Basis: brief.txt (no sport above a third)

[minor] [label] Deliverable, Sara's profile; Current: "coach: 20 years' experience, sees her four times a week and coaches two other groups."; Problem: the unit makes Sara's coach a man ("he", "his") throughout; the register gives no gender and the fact is not marked added; Fix: "coach (a man, *added*): 20 years' experience, sees her four times a week and coaches two other groups."; Basis: case-facts.md, Sara

[minor] [figure] §3 matrix caption; Current: "as section 3 of this unit draws it from"; Problem: the "onward" mark (licensed practitioner refers on) is sourced in §8 (team doctor, toolkit p. 39), not §3; Fix: "as sections 3 and 8 of this unit draw it from"; Basis: unit §8

[minor] [attribution] Sources, Dazzi; Current: "read by the fresh checker 18 Nov 2026"; Problem: contradicts the Sources header ("Every address was opened by the writer") and puts process in the reader's bibliography; Fix: "read 18 Nov 2026"; Basis: unit.md Sources header

[minor] [attribution] Sources, ISSF; Current: "Web page presenting the IOC Sport Mental Health Recognition Tool (the page's own headline was not shown in the text read; its title element reads \"ISSF - International Shooting Sport Federation\")"; Problem: the page's heading is "The IOC Sport Mental Health Recognition Tool" under the banner "Inside ISSF" (write-unit §4c: title is the page's own headline); Fix: "*The IOC Sport Mental Health Recognition Tool.* Web page (under the banner \"Inside ISSF\")"; Basis: https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool

[minor] [attribution] Sources, NSPCC; Current: "*How to respond to child abuse concerns in your sport.* Web page"; Problem: the page's headline is "How to respond to child abuse concerns"; "in your sport" is only in its title element; Fix: "*How to respond to child abuse concerns.* Web page"; Basis: https://sport.nspcc.org.uk/news-and-blogs/2026-01-how-to-respond-to-child-abuse-concerns-in-your-sport/

[minor] [attribution] Sources, Mountjoy; Current: "- Mountjoy, et al. 2023"; Problem: no initials or co-authors; Fix: "- Mountjoy M, Ackerman KE, Bailey DM, Burke LM, Constantini N, et al. 2023"; Basis: Norwegian School of Sport Sciences repository record (not publisher), https://nih.brage.unit.no/nih-xmlui/handle/11250/3135521?show=full; citation 57(17):1073–1097 also on PubMed https://pubmed.ncbi.nlm.nih.gov/37752011/

[minor] [attribution] Sources, Tranaeus; Current: "Wiese Bjornstal D, et al."; Problem: the article has seven authors; "et al." stands for one, Ivarsson A; Fix: "Wiese Bjornstal D, Ivarsson A."; Basis: University of Minnesota record https://experts.umn.edu/en/publications/50-years-of-research-on-the-psychology-of-sport-injury-a-consensu/ and St Mary's copy of the published PDF https://research.stmarys.ac.uk/id/eprint/6344/1/s40279-024-02045-w.pdf

[minor] [style] Unsure list; Current: "# SP9 unsure list"; Problem: a second, level-1 heading inside "## Unsure list"; Fix: "" (delete the line); Basis: unit.md

## Confirmed

- Reardon et al. 2019: depressive symptoms "ranges from 4% to 68%"; prevalence "appears to be similar" to general population; GAD 6.0% clinician-confirmed, 14.6% self-report; social anxiety 14.7%, panic 4.5% self-report; ~64% Olympic athletes significant insomnia symptoms; "unmask or precipitate"; "minimal prospective research"; "Coaches should feel comfortable discussing eating disorders and RED-S with athletes"; "Dissatisfaction with body image may be the strongest predictor of eating disorders in athletes" — https://bjsm.bmj.com/lookup/doi/10.1136/bjsports-2019-100715 (first 100,000 characters)
- Gwyther et al. 2024: mean age 12–17, travelling internationally; 33 studies, 5,826 athletes; DE k=16, anxiety 7, depression 5; caseness DE 0–14% males, 11–41% females; depression 7% mixed, 14%/40%; anxiety 8%/28%; risk factors sex, athlete status, coach/parent/peer relations; competition level contradictory — https://ouci.dntb.gov.ua/works/4LMwdALl (abstract copy); PubMed summary https://pubmed.ncbi.nlm.nih.gov/39122370/; citation 58(17):1011–1019 and authors https://experts.mcmaster.ca/display/publication3461383
- Kuettel & Larsen 2020: 9 reviews, 43 empirical studies, 84% quantitative; personal and sport-environmental domains; autonomy, positive relations, recovery highlighted as protective by qualitative studies — https://informahealthcare.com/doi/abs/10.1080/1750984X.2019.1689574; 13(1):231–265 — https://lida.sport-iat.de/ta/Record/4068022
- FEPSAC PS 12 (2018): injuries, overtraining, career termination may raise risk; six countries; competencies, certification, boundaries and health systems vary; single standard hard to define (source: "golden standard"; the unit paraphrases without quotes) — https://fepsac.com/position-statements/
- Henriksen et al. 2020: three quotations exact; seven panellists; 18(5):553–560, 2 Sep 2020 — https://informahealthcare.com/doi/abs/10.1080/1612197X.2019.1570473; https://eld.bl.uk/catalog/100160678397_0x000001
- Bissett et al. 2020: 15 experts (2 coaches, 3 athletes over 18, 8 licensed MH professionals, 2 health educators); two rounds; mean ≥7 kept; "Coaches should foster team cultures that support athlete mental health"; "facilitate referral to appropriate support"; RTP "should be determined by a licensed mental health practitioner and not a coach"; privacy; moderating demands "not deemed feasible"; coaches' own support; panel country not stated — https://bmjopensem.bmj.com/content/6/1/e000676
- IOC toolkit 2021: coaches "are in a position to recognise differences in moods, performance, social interactions"; "significant and/or persistent"; "the SMHRT-1 is not a diagnostic tool"; developed by the IOC MHWG for athletes, coaches, family, entourage; MHEAPs usually developed by medical team with licensed MH experts; check club has a MHEAP and understand your role; designate a referral lead; "Listen to and validate the athlete's concerns"; "Offer to contact your club/team's sports medicine physician and/or licensed mental health provider"; follow up within 24 hours "to determine if further action is needed"; "serious and immediate danger to the athlete or to others"; "Contact emergency services"; reporting procedures; "Respect their right…"; "you can only encourage and support an athlete in seeking further help"; referral "will usually be made by the team doctor" — toolkit URL above
- ISSF page: undated, © 2025; "to recognise mental health problems but not to diagnose them"; five red flags word for word; "seek immediate help"; may be freely copied; revision needs MHWG approval — ISSF URL above
- Gouttebarge et al. 2021: SMHRT-1 "developed for athletes and their entourage"; SMHAT-1 for sports medicine physicians and licensed/registered professionals, elite athletes aged 16 and older; online Sept 2020; 15 authors; 55(1):30–37 — https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract; https://experts.mcmaster.ca/display/publication1926186
- Mountjoy et al. 2023: health and performance outcomes in female and male athletes; interplay between mental health and REDs; REDs CAT2 introduced for clinicians; 57(17):1073–1097 — https://pubmed.ncbi.nlm.nih.gov/37752011/
- Walsh et al. 2021: 7–9 h adults, 8–10 h teenagers; "maladaptive perfectionism and hyperarousal" among risk factors; validated questionnaires; "refer athletes to a sleep specialist for clinical diagnosis, when necessary"; "a more real-world scenario, remains unclear"; authors; 55(7):356–368, online 3 Nov 2020 — LJMU copy (above); https://eld.bl.uk/catalog/100132399187_0x000001
- Tranaeus et al. 2024: three quotations exact; 54(7):1733–1748 — St Mary's copy and UMN record (above)
- Yang et al. 2023: 14 studies, 3,496 athletes aged 11–55, elite; r = 0.150 (0.025 to 0.271), 0.138 (0.009 to 0.261), −0.246 (−0.344 to −0.143); variance unexplained; 11(10):1417 — MDPI URL above
- Dazzi et al. 2014: editorial, online 7 July 2014; 13 papers 2001–2013 (introduction); adults and adolescents, general and at-risk; "None found a statistically significant increase in suicidal ideation…" — https://www.cambridge.org/core/product/FCAEE9E5BC840D76CF10AEBECD921AC9
- Kang & Lee 2025: 101 studies 2010–2024; elite definition; burnout 40, stress 32; stressors; Longshore & Sachs six-week mindfulness with NCAA coaches; Olusoga et al. six-week MST with five British elite coaches; mostly Western; 16:1666035 — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1666035/full
- NSPCC Sport (respond page): updated 7 Jan 2026; "without leading or intrusive questions"; "I promise I won't tell anyone" / "You can't promise this" — NSPCC URL above
- NSPCC Sport (away day trips): updated 24 Nov 2022; both quotations; separate overnight briefing; "formerly CPSU" — https://sport.nspcc.org.uk/resource-library/best-practice/away-day-trips/
- U.S. Center for SafeSport MAAPP page: observable-and-interruptible quotation and emergency exception; transport rule; lodging; modified 23 Dec 2025; 2025 MAAPP; applies to Olympic & Paralympic Movement adults — https://maapp.uscenterforsafesport.org/how-it-works/
- Sport Integrity Australia: "are banned in-competition"; S6 Stimulants; TUE in advance or planned retroactive by level; undated, no headline — https://www.sportintegrity.gov.au/what-we-do/anti-doping/substance-education/responsible-use-of-adhd-medication-sport
- Pointers: SP1 scope line and Sara's scope card (filed/SP1 §2 and deliverable); SP2 menarche association in girls and women outside sport; SP3 burnout's three dimensions from the footballers' study (Morales-Sánchez); SP4 rows 3, 6, 9, 10 and screening kept with licensed professionals; SP5 stop rule wording; SP6 referral cap 3 and the question to the person referred to; SP7 flat/withdrawn/tearful rows and "no added load to 'lift' her"; SP8 second adult (section 6), not making sleep a demand, long jumper covered by another group's coach: all say what SP9 says they say, except SP4 rows 1 to 4 (finding above).

## (7) Figures

1. range, §1 — PASS. Every label and number is in §1 (Gwyther: 0–14, 11–41, 14/40, 8/28); caption names section, source, abstract-only; 7% mixed-sex point stated as not drawn; kind fits.
2. matrix, §3 — FIX (minor): "onward" comes from §8; caption replacement above. Other cells traced to §3 (Delphi, IOC consensus, toolkit, think tank).
3. decision, §7 — FIX (should-fix): "no danger" outcome replacement above. Other labels trace to §4, §6, §7 and table A; "Keep the baseline sheet; check in" rests on SP7 and SP4 references and no sentence of SP9, acceptable as a summary.
4. flow, §8 — PASS. Steps match §8 and §9; caption names sources and the unit's own order.

## Passes

**Claims.** 18 sources opened; every cited claim checked against them PASS except: toolkit misquote (should-fix), "stay with" condition (should-fix), Yang I² (should-fix), Walsh Box 2 context (should-fix). Not opened: Reardon's "primary interpersonal interface", "age and developmentally appropriate", parents of younger athletes, MHEAP quotations and post-incident review (after character 100,000 of the publisher's page; my continuation fetch was refused, so not checked); Reardon Table 4 (not shown on the publisher's page); the SMHRT-1 PDF (no search returned it); Moesch et al. 2018 article.

**Bibliography.** Field by field against publisher or registry: Gwyther, Henriksen, Walsh, Tranaeus, Gouttebarge 2021, Mountjoy (pages), Kuettel (journal, volume, issue, pages), Yang, Kang & Lee, Bissett (journal, volume, article number) match. Errors in authors: Mountjoy and Tranaeus (minor, above). Not verified: Bissett initials and issue, Kuettel initials, Reardon end page 699 and its first three authors, Dazzi volume and pages 44:3361–3363, toolkit "Spring 2021". No non-existent reference found.

**Source log.** No sources.md in the packet. The unit says "abstract read" for Gwyther, Kuettel & Larsen, Mountjoy, Dazzi, Gouttebarge 2021, and "abstract and propositions" for Henriksen, both where cited and in Sources: PASS. Dazzi's 13 papers and years come from the introduction, which Sources records. Every Sources entry records address, what was read and date: PASS. Sources header vs Dazzi entry wording (minor, above).

**Grades.** Against SP1 §9: Yang [moderate, association; rule 4, unexplained heterogeneity] PASS; risk and protective factors [weak, positive, association; rule 5, correlational/qualitative] PASS; Dazzi [weak; outside sport, rule 5] PASS; sleep ranges [weak] follows SP2 (F47 still open); consensus-only recommendations [practice] with the F14 note PASS; time points [practice; the unit's own] PASS. No technique or recommendation found without a grade.

**Population.** Samples named: elite youth mean 12–17 travelling internationally; elite adults (studies unopened, said so); Yang 11–55; Bissett adult athletes; Kang & Lee elite coaches; Dazzi adolescents and adults outside sport. Transfers labelled: 10–12 and club athletes as inference; sleep ranges as inference for under-18s; SMHRT-1 for 11–17 as inference; "outside the sampled ages" used per SP5–SP8. PASS.

**Scope and safety.** No assessment, diagnosis or treatment taught (questionnaires left to the clinician; "asking is not assessing"); no weight-loss method, calorie figure or target weight; no method of self-harm; no law stated as the reader's (SafeSport, NSPCC, SIA given as examples, with questions and bodies to ask); information-not-advice line present; no real person named against the rule; no confidentiality promise a coach cannot keep with a minor; no crisis or referral service named as the reader's; the burden is never on the child (§6, §8, C1 template). One failure: the urgent route can delay help for a panic-like red flag (three should-fix above: §7 quotation, §7 step 3, decision figure).

**Any sport.** Body examples by sport: athletics 5, football 2, judo 1, rowing 1, basketball 1, gymnastics 1, cycling 1, volleyball 1, swimming 1 (14). Athletics at 36% is above a third (minor fix brings it to 4/14). The deliverable is athletics by the brief's choice of Sara. Individual, team, weight-class and judged sports present. Nothing found that identifies the Project's owner; kit/private_terms.py is not in the packet and was not run.

## Part 7, line by line

1 sourced where made: PASS. 2 source types: PASS (consensus labelled; issuing bodies' pages dated). 3 no video/blog/press: PASS. 4 source log: PASS (see Source log). 5 Sources vs publisher/Crossref: FAIL in two author fields (minor); partly unverified. 6 grades per SP1: PASS. 7 sample and design, correlation named: PASS. 8 inference label: PASS. 9 effect sizes in source's terms with sample: PASS except Yang's I² (should-fix). 10 popular claims: no claim from the course list is named; the seed list is not in the packet, so not checked. 11 coach's part and who takes over: PASS. 12 weight/calorie/self-harm: PASS. 13 no law as the reader's, information not advice: PASS. 14 no real person named: PASS. 15 three kinds of sport, none above a third: FAIL by one example (minor). 16 case facts labelled and agree with the register: PASS except the coach's gender (minor). 17 private terms: not run. 18 search-on dates: PASS (all issuing-body pages dated 18 Nov 2026). 19 deliverable on Sara then template: PASS. 20 not advice without evidence: PASS. 21 links as DOI links: PASS.

## Read as the coach

The order is usable on a phone: what's common, what to look for, what to say, what to do now, whom to call. Table A is wide (five columns) and will need horizontal scrolling. The urgent steps are clear and correctly ordered, except for the panic-like episode (findings above). The scripts are usable aloud.

## Brief and deliverable

Every brief item is covered. Thin: "read on its own page" for the IOC tool, because the IOC's PDF failed and the ISSF page and toolkit stand in, as the unit says. Deliverable A (sign, how long, what to do, who to call), B (referral plan with blanks, competition-day version, SP4 completion) and C (three scripts) are built in full for Sara, each with a template: PASS.

## Flags, one by one

| Flag | Proposed | How SP9 deals with it |
|---|---|---|
| F3 | Open Delphi, IOC 2019, FEPSAC; check scope line; raise mismatch on SP1 | Delphi and IOC opened in full; FEPSAC summary page only (unsure 10). Scope line checked in §3. Mismatch says "raised in the notes" but no notes are in the unit (should-fix). Partly met. |
| F8 | Use SP1 §9 unchanged | Met (preamble; grades checked). |
| F14 | Consensus-only: [practice] with note | Met throughout. |
| F17 | Youth-athlete prevalence from opened sources; build the referral route | Met: Gwyther 2024 (abstract); §1 routes the menarche link to the route. |
| F21 | List Walsh at publisher's page and open it | Met with caveat: read at bjsm.bmj.com/node/121079, identity inferred (unsure 5). |
| F24 | Publisher addresses, not PMC | Met; PubMed used for two abstracts. |
| F47 | One convention pending S-SP1 | Not settled; unit follows SP2 for sleep ranges ([weak]) and SP3 for other consensus ([practice]). Acceptable until S-SP1. |
| F48 | Keep SP1's wording for inference | Met: "outside the sampled ages" for other bands. |
| F53 | Read Reardon at publisher's page, Table 4, before filling referral lines | Publisher's page read; Table 4 not shown, so not met; disclosed (unsure 2). Referral lines filled regardless. |
| F54 | Fill SP4's To whom and Urgent route; read SMHRT-1 PDF; check ISSF red flags against it | Lines filled (rows 1–4 gap: should-fix). PDF returned a server error: not met; disclosed (unsure 3). |
| F69 | Route for distress in skill practice | Met: §8 and table A row. |
| F87 | How to ask the person referred to | Met: §8 four steps and script, B row, C1 line. |
| F98 | Open the tool itself before the red-flag table | Not met (server error); disclosed. |
| F99 | Find a source or keep silent on autism | Met: silent, §8. |
| F100 | Date the current anti-doping rule on a NADO page | Met: Sport Integrity Australia, read 18 Nov 2026; WADA list not opened (unsure 9). |
| F117 | State both Walsh statements | Met, but Box 2's banking-sleep condition is dropped (should-fix). |
| F121 | Date current supervision codes on issuing bodies' pages | Met: NSPCC Sport and SafeSport, dated; overnight briefing not opened. |
| F122 | Competition-day version of red-flag table and plan | Met in B and §10; table A has the event medical service in one row only (template "Who to call" covers where you compete). |
| F123 | Date a federation rule only if a real example is needed | Not needed in SP9; nothing stated. |
| F124 | Carry debrief, reset, time-sharing as practice | Met: §10. |
| F127 | Quality review | This report. |

## Could not verify

1. Reardon et al. 2019: "Within sport, coaches are often the primary interpersonal interface with the athlete"; "Coaches can ensure that training is age and developmentally appropriate"; coaches communicating the importance of mental healthcare to parents of younger athletes; "to develop and rehearse a mental health emergency action management plan"; "clarity on what constitutes an emergency, who should be contacted and when"; review of procedures after an incident (beyond character 100,000; continuation fetch refused).
2. Reardon Table 4 (social anxiety, panic rows): tables not on the publisher's page.
3. SMHRT-1's own list (PDF): no search returned it.
4. ISSF page's description of the tool as a list of thoughts, feelings, behaviours and physical changes (not in my extraction).
5. IOC toolkit page numbers: my reading placed "All sports organisations…" on p. 46, the referral lead on p. 62, and "significant and/or persistent" and "not a diagnostic tool" on p. 40 (the last two inferred); the unit cites pp. 39, 47, 51, 61 and p. 41. Not settled; the filer should check the PDF's printed page numbers.
6. Bibliographic fields: Bissett initials and issue; Kuettel initials; Reardon end page and authors; Dazzi 44:3361–3363; toolkit "Spring 2021"; Moesch et al. 2018 (38:61–71).
7. The writer's notes: the list of *added* facts and the F3 flag text (no notes file in the packet).
8. Popular-claims list (seed bibliography not in the packet): whether SP9 should name one (for example, that asking about suicide puts the idea in someone's head).
9. kit/private_terms.py not run (not in packet).
10. Walsh read on a repository copy, not the publisher's page.
