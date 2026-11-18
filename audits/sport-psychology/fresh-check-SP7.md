---
audit: fresh check
unit: SP7 · Reading and responding to an athlete
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-18
chat: https://claude.ai/code/session_01KMmgR1qQW9xKHp3R39b5Yz
verdict: fix · 0 errors, 7 should-fix, 9 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: SP7 · fix · 0 error, 7 should-fix, 9 minor · model claude-opus-5-5
(The harness refused the write to out/report.md, so the full report follows here.)
Model: Opus 5.5 (claude-opus-5-5), fresh checker, isolated context; did not see the unit written. Checked 18 Nov 2026 with live search. Every URL below was returned by a WebSearch in this run and then opened by WebFetch. No reference is invented; the row is not stopped.

## Findings
[should-fix] [label] §8 Feedback after good trials or after poor ones; Current: "[weak, mixed; rule 5; for athletes, inference]"; Problem: the brief's key gives "contested" for failed replications. Chiviacowsky et al. (2007) tested whether the adult good-trials effect held in children and found no difference at retention; its abstract says this disagrees with the adult result. "Mixed" is not one of the five grades; Fix: "[contested; one failed replication in children (Chiviacowsky et al., 2007) against one positive study in children and one in adults; rule 4; for athletes, inference]"; Basis: Chiviacowsky et al. 2007 abstract, https://revistas.usp.br/rbefe/en/article/view/16652
[should-fix] [attribution] §1 How accurate coaches are; Current: "Three athletes and one coach: an exploratory study, and the authors say so."; Problem: neither "exploratory" nor "explorative" appears in the full text. The authors call it a "case study" and name the small sample as a limitation; Fix: "Three athletes and one coach: the authors call it a case study and give the small sample as a limitation."; Basis: Friesen et al. 2018 full text, https://jyx.jyu.fi/bitstream/handle/123456789/57932/1/ruiz10413200.2017.pdf
[should-fix] [accuracy] §2 What the sources support; Current: "a survey of 360 active and former elite athletes and a modified Delphi consensus process ([Gouttebarge et al., 2021, consensus, abstract read]"; Problem: the abstract calls all 360 athletes, but the Methods say the 360 attendees were athletes, coaches in elite sport or representatives of sport governing bodies, surveyed at the IOC and IPC athletes' forums in 2019. SP1 was right, which settles the first contradiction in the notes. The source log needs a row for the PMC full text; Fix: "a survey of 360 people at two athletes' forums (athletes, coaches in elite sport and representatives of governing bodies, by the methods; the abstract names only athletes) and a modified Delphi consensus process ([Gouttebarge et al., 2021, consensus, abstract read, methods read on PubMed Central]"; Basis: https://pmc.ncbi.nlm.nih.gov/articles/PMC7788187
[should-fix] [attribution] Deliverable A, Dani; Current: "| Listens, nods, tries it straight away; looks to her coach after every exchange. | Case register. |"; Problem: "listens, nods, tries it straight away" is not in the register or the notes, yet it is labelled as coming from the register; Fix: "| Listens, nods, tries it straight away (*added*); looks to her coach after every exchange. | Case register; *added*: listens, nods, tries it straight away. |"; Basis: case-facts.md (packet)
[should-fix] [attribution] Deliverable A, Sara; Current: "| Asks for the numbers; writes them in her log, to the tenth of a second. | Case register. |"; Problem: "asks for the numbers" is invented, labelled as coming from the register, and not in the notes; Fix: "| Asks for the numbers (*added*); writes them in her log, to the tenth of a second. | Case register; *added*: asks for the numbers. |"; Basis: case-facts.md (packet)
[should-fix] [style] §11 What follows, step 5; Current: "With a minor, tell the parents what happened if the club's welfare or safeguarding officer advises it; a concern about how an adult has treated a minor goes to that officer (SP1, DD-SP1)."; Problem: this states a reporting route as fact. Part 7 requires a reporting duty to be put as a question, with the body to consult; Fix: "With a minor, ask the club's welfare or safeguarding officer whether the parents should be told what happened; for a concern about how an adult has treated a minor, ask that officer, or your national sport body, what the reporting route is (SP1, DD-SP1)."; Basis: sourcing-standard.md Part 7 (packet)
[should-fix] [figure] §3, second viz block; Current: "{"kind": "range", "caption": "Standardised associations" (the start of the whole line 70, which occurs once; replace the whole line); Problem: the five rows are separate point estimates (low = high = point), not competing estimates of one quantity. The skill's kind list puts compared numbers under compare or bars. kit/viz.py's bars schema is not in the packet, so check these field names before building; Fix: "{"kind": "bars", "caption": "Standardised associations (β) between emotion regulation, coach style and general mental health in 93 athletes aged 15 to 17 at one Swedish sports school, followed over 12 months. Higher scores on the health questionnaire mean worse health. From sections 3 and 5 of this unit: Fröjdö Regborn et al. (2025), Sports. Observational; the authors say causality cannot be inferred.", "unit": "", "rows": [{"label": "Reappraisal and health score", "value": -0.33, "tone": 2}, {"label": "Suppression and health score", "value": 0.34, "tone": 1}, {"label": "Controlling coach and suppression", "value": 0.2, "tone": 1}, {"label": "Controlling coach and reappraisal", "value": 0.2, "tone": 4}, {"label": "Need-supportive coach and reappraisal", "value": 0.19, "tone": 2}]}"; Basis: audit-units-SKILL.md Figures paragraph; https://www.mdpi.com/2075-4663/13/9/284
[minor] [attribution] Deliverable A, Dani; Current: "Arrives on time, changes quickly, warms up beside the same two girls (*added*). Says little."; Problem: "arrives on time, changes quickly" is not in the notes' list of invented facts; Fix: "Arrives on time, changes quickly, warms up beside the same two girls (all *added*). Says little."; Basis: notes.md, case-facts.md
[minor] [accuracy] §3 What goes with what; Current: "In 424 competitive athletes in Italy aged 16 to 36"; Problem: no country is named in the full text or record read, and none in the source log; Fix: "In 424 competitive athletes aged 16 to 36"; Basis: https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1205102/text ; https://jyx.jyu.fi/handle/123456789/88576?show=full
[minor] [accuracy] §3 19 to 25; Current: "The Italian sample covers it without analysing age."; Problem: same as the finding above; Fix: "The sample of 424 competitive athletes aged 16 to 36 (section 3) covers it without analysing age."; Basis: as above
[minor] [accuracy] §9 Between sexes; Current: "in basketball, football, swimming and badminton, measured once,"; Problem: the paper's abstract says "multi-wave data" and its limitations say "cross-sectional design". "Measured once" settles a question the paper leaves open; Fix: "in basketball, football, swimming and badminton (the abstract calls the data multi-wave, the limitations call the design cross-sectional),"; Basis: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1636707/full
[minor] [attribution] Deliverable C, Sara script 4; Current: "That goes to the physio's plan; let's ask them together."; Problem: the physio is an invented fact, not in the register or the notes; Fix: "That goes to whoever manages your hamstring rehabilitation; let's ask them together."; Basis: case-facts.md
[minor] [label] §1 fourth bullet; Current: "[weak, for the association; one study in coach–athlete dyads, abstract read, rule 5]"; Problem: the abstract gives no ages, yet the bullet is applied to every age without an inference label; Fix: "[weak, for the association; one study in coach–athlete dyads, abstract read, rule 5; ages not given, so for under-18s, inference]"; Basis: https://rke.abertay.ac.uk/en/publications/empathic-accuracy-in-coach-athlete-dyads-who-participate-in-team-/
[minor] [attribution] §2; Current: "([ISSF, The IOC Sport Mental Health Recognition Tool, undated, read 18 Nov 2026]("; Problem: the red flags are quoted from a federation's reproduction of the IOC tool, not from the issuing body's own page. The page carries a © 2025 footer and no other date; Fix: "([ISSF, The IOC Sport Mental Health Recognition Tool, a federation's reproduction of the IOC tool, undated (footer © 2025), read 18 Nov 2026; the IOC's own copy not opened]("; Basis: https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool
[minor] [style] Deliverable B, Angry row; Current: "a safeguarding concern goes to the welfare officer."; Problem: this states a reporting route as fact (Part 7); Fix: "for a safeguarding concern, ask the club's welfare or safeguarding officer what the route is."; Basis: sourcing-standard.md Part 7
[minor] [accuracy] §5 fourth bullet; Current: "that gap is what SP3's self-audit films"; Problem: the register's SP3 facts say the coach was "observed" and "scored by a colleague", not filmed; Fix: "that gap is what SP3's self-audit observes"; Basis: case-facts.md SP3 rows
(Every Current above was confirmed with grep -cF: each occurs once.)

## Skill items
(1) Coverage: every brief item is covered. 19 to 25 is thin, and the unit says so instead of filling the gap. Popular claims are named and set against evidence.
(2) Accuracy: see Claims below. Unsure list: 1 settled (PMC shows the authors and DOI 10.1111/j.1467-9507.2007.00389.x). 2 settled (the JYD landing page shows DOI 10.5195/jyd.2007.358). 3 open (Dalhousie gives "Megan"). 4 partly settled (the authors are not on any record opened; Chiviacowsky et al. 2007 calls it the adult study). 5 settled (55(1):30–37 per PMC). 6 issue 11 not seen. 7 settled (2017;10(1):84–107 per BISp). 8 my read gives the same direction as the writer's (younger lower). 10 PMC gives n = 38; the unit's wording is still true of the abstract read.
(3) Figures: every number says whose it is: PASS.
(4) Labels: designs are labelled; the one exception is the Friesen finding above.
(5) Deliverable: all three tools are built in full for Dani, Milan and Sara, then given as templates whose blanks say what goes in them. Each is usable alone: PASS.
(6) Errata: no audit report is in the packet. Pointers to SP1 to SP6 were not checked (those units are not in the packet).
(7) Figures: Figure 1 (flow, §2): PASS; labels trace to §2 and the kind fits. Figure 2 (range, §3 and §5): numbers trace to the β values in §3 and §5, the caption is adequate, the kind needs a FIX (above). Figure 3 (decision, §6): PASS; the branches trace to §6 ("A sore hamstring goes to the medical plan…", "Offer a smaller step instead", "say when you will come back").

## Claims
PASS (opened by me): Barrett 2019 (the quotation, variation across cultures, remote cultures, neutral descriptive terms); Aviezer 2012; Lorimer & Jowett 2009; Friesen 2018 (sample and findings); Fröjdö Regborn 2025 (all β values, n, alpha, "causality cannot be inferred", "paradoxical"); Robazza 2023 (except "Italy"); Sanchis-Sanchis 2020; McRae 2012; Tamminen 2016; Tamminen 2021; Morris 2007; van Kleef 2019 (anger "not" conducive); McMurtry 2010 (venipuncture; both tasks); Smoll 2007 (quotation, tone of voice, 151 athletes aged 9 to 15, contributions inseparable, behaviour not recorded); Saemi 2011; Chiviacowsky et al. 2007; Chiviacowsky & Wulf 2007 (finding); Reardon 2019 (ADHD quotation, features, education, WADA and TUE); ISSF page; Wachsmuth 2017 and 2018; Gale 2023; Wei 2025 (n, sports, β 0.057, ΔR² 0.009, "modest").
FAIL: Friesen "exploratory"; Gouttebarge "360 athletes".
Not opened: claims resting on SP1 to SP6 (grade key, ironic-effects grade, SP5 breathing grades, SP4 accommodation and table rows). PubMed 23197536 not checked (reCAPTCHA); ncbi PMC12425922 not checked (redirect).

## Bibliography
All 24 entries exist and match their records: Aviezer, Barrett, Friesen, Fröjdö Regborn, Gale, Gouttebarge (all 15 authors in order), Lorimer, McRae, Morris, Robazza, Saemi, Chiviacowsky et al., Smoll, Tamminen 2016, Tamminen 2021, van Kleef, Wachsmuth 2017, Wachsmuth 2018, Wei.
Partly confirmed: Reardon (issue 11 not seen); McMurtry (initials unsettled; volume, pages and DOI match); Chiviacowsky & Wulf (authors not on any record opened; journal, 78(2):40–47 and DOI match).

## Source log
Every Sources entry has a row in sources.md. Abstract-only claims say "abstract read". The Gouttebarge fix needs a new log row for PMC.

## Grades
Grades follow the key except §8, where "mixed" should be contested. SP1's rule numbers were not checked (SP1 is not in the packet).

## Population
Samples are named throughout. Inference labels are present, except Lorimer & Jowett (finding above). "Outside the sampled ages" is used for Smoll at 16 to 25.

## Scope and safety
- Nothing teaches assessment, diagnosis or treatment.
- No weight-loss method, calorie figure or target weight.
- No method of self-harm.
- The TUE question is put as a question for the national anti-doping organisation.
- Two reporting routes are stated as fact (findings above).
- No real person is named.
- Claims about sex and culture rest on sources opened.

## Any sport
The body's examples are spread across racket sport, volleyball, gymnastics (2), rowing, tennis, judo, hockey, football and 400 m. The deliverable is split equally between judo, football and athletics. The largest share for any sport is about 21%: PASS.
Owner recognisability: not checked. Neither kit/private_terms.py nor the owner's details are in the packet, and context outside the packet may not be used.

## Part 7 line by line
PASS on all lines except: grades (§8); inference (Lorimer); law and reporting (two routes); register agreement (Dani and Sara entries; the physio). Owner terms: not checked. The advice disclaimer is present. The unit does not read as advice without evidence.

## Notes check
- Case facts: not listed but invented in the unit:
  - Dani: arrival and changing; "listens, nods"; SP4 check-in and her wishes marked "not yet asked"; the hypothetical states and the scenarios in scripts 2 to 4.
  - Milan: a Monday session; "criteria I gave the squad"; "second half full of forward passes".
  - Sara: "asks for the numbers"; a physio; "first 200 exactly on plan".
- Contradictions: the Gouttebarge entry is settled in SP1's favour by the PMC methods. The other three entries are accurate.
- Needs: the DD-SP1 line misstates the source. The 6 of 80 papers studied interpersonal conflict directly, not repair.
  - Replacement: "DD-SP1: repair after a coach's harmful behaviour has almost no evidence (only 6 of 80 papers on coach–athlete conflict studied interpersonal conflict directly, and none of the three studies opened tests a repair); DD-SP1 should not cite SP7's repair steps as tested."

## Confirmed
- Barrett et al. 2019, PSPI 20(1):1–68. https://pmc.ncbi.nlm.nih.gov/articles/PMC6640856 ; https://www.psychologicalscience.org/publications/emotional-expressions-reconsidered-challenges-to-inferring-emotion-from-human-facial-movements.html
- Aviezer et al. 2012, Science 338(6111):1225–1229. https://collaborate.princeton.edu/en/publications/body-cues-not-facial-expressions-discriminate-between-intense-pos/
- Lorimer & Jowett 2009, 40 dyads. https://rke.abertay.ac.uk/en/publications/empathic-accuracy-in-coach-athlete-dyads-who-participate-in-team-/
- Friesen et al. 2018, athletes aged 18 to 20; athletes and coach wanted different emotions. https://jyx.jyu.fi/bitstream/handle/123456789/57932/1/ruiz10413200.2017.pdf
- Fröjdö Regborn et al. 2025, β values. https://www.mdpi.com/2075-4663/13/9/284
- Robazza et al. 2023, 424 athletes, M 23.08, cross-sectional. https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1205102/text
- Sanchis-Sanchis et al. 2020. https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.00946/text
- McRae et al. 2012. https://pmc.ncbi.nlm.nih.gov/articles/PMC3252634
- Tamminen et al. 2016. https://utoronto.scholaris.ca/items/b9851e86-aab8-41bf-be61-e44f4c256595
- Tamminen et al. 2021. https://researchportal.port.ac.uk/en/publications/the-effect-of-self-and-interpersonal-emotion-regulation-on-athlet/
- Morris et al. 2007. https://pmc.ncbi.nlm.nih.gov/articles/PMC2743505/
- van Kleef et al. 2019. https://dare.uva.nl/id/1292444c-3492-41e7-a862-48243aaeded8
- McMurtry et al. 2010. https://dalspace.library.dal.ca/handle/10222/74861
- Smoll et al. 2007. https://jyd.pitt.edu/ojs/jyd/article/view/358/344 ; https://jyd.pitt.edu/ojs/jyd/article/view/358
- Saemi et al. 2011. https://revistas.usp.br/rbefe/article/view/16860
- Chiviacowsky et al. 2007. https://revistas.usp.br/rbefe/en/article/view/16652
- Chiviacowsky & Wulf 2007. https://informahealthcare.com/doi/abs/10.1080/02701367.2007.10599402
- Reardon et al. 2019. https://www.psychiatry.wisc.edu/wp-content/uploads/2023/10/2019-Mental-health-in-elite-athletes-International-Olympic-Committee-consensus-statement-2019.pdf
- Gouttebarge et al. 2021, BJSM 55(1):30–37. https://pmc.ncbi.nlm.nih.gov/articles/PMC7788187 ; https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract
- ISSF red flags. https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool
- Wachsmuth et al. 2017. https://lida.sport-iat.de/twm/Record/4042861?lng=en ; https://repository.lboro.ac.uk/articles/journal_contribution/Conflict_among_athletes_and_their_coaches_What_is_the_theory_and_research_so_far_/9619040
- Wachsmuth et al. 2018. https://repository.lboro.ac.uk/articles/journal_contribution/Managing_conflict_in_coach-athlete_relationships/9618692
- Gale et al. 2023. https://researchportal.northumbria.ac.uk/en/publications/repairing-relationship-conflict-in-community-sport-work-offender-/
- Wei et al. 2025. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1636707/full
