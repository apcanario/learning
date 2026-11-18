Verdict: SP7 · fix · 1 error, 4 should-fix, 4 minor

(The harness refused the agent's write to out/report.md; the agent returned the full report as its reply and the chat saved it verbatim.)

Model: claude-opus-5-5 (Opus 5.5). Fresh check, isolated agent context, live search 18 Nov 2026. Sources opened only by WebFetch of URLs that my own searches returned.

## Findings

[error] [accuracy] §4 "In teams, in athletes", Tamminen et al. 2016; Current: "efforts to improve a teammate's emotional state went with the athlete's own greater enjoyment and commitment, and efforts to worsen it with less enjoyment;"; Problem: the abstract does not report that efforts to worsen a *teammate's* state went with less enjoyment. The negative link with enjoyment is for athletes' *self*-worsening strategies, meaning efforts that worsen their own state; Fix: "efforts to improve a teammate's emotional state went with the athlete's own greater enjoyment and commitment, and strategies that worsened the athlete's own emotional state went with less enjoyment;"; Basis: Tamminen KA et al. 2016, JSEP 38(6):541–555, abstract on the University of Toronto repository, "athletes' self-worsening emotion regulation strategies were negatively associated with enjoyment", https://utoronto.scholaris.ca/items/b9851e86-aab8-41bf-be61-e44f4c256595

[should-fix] [accuracy] §9 "Between cultures", Barrett et al. 2019; Current: "and that studies in small remote cultures found no facial configuration specific to a given emotion"; Problem: this stretches the source. The review calls the production evidence from small-scale remote cultures inconclusive: it rates specificity "unknown" and found no systematic studies of spontaneous movements. It does not report a finding that no specific configuration exists. The writer read only the first part of the full text, and this claim comes from a later part; Fix: "and that the evidence on how people in small, remote cultures move their faces during emotion was, in its authors' judgement, inconclusive"; Basis: Barrett et al. 2019, PSPI 20(1):1–68, full text on PubMed Central (section on small-scale cultures, Table 4), "expression production studies in small-scale, remote cultures is inconclusive", https://pmc.ncbi.nlm.nih.gov/articles/PMC6640856

[should-fix] [accuracy] §11 "What the studies show", Gale et al. 2023; Current: "Those conflicts were with working colleagues, not athletes."; Problem: the abstract says only that the conflicts were with "significant working others". It does not say that athletes were excluded, so "not athletes" is unsupported; Fix: "The abstract describes the other parties only as significant working others and does not say whether athletes were among them."; Basis: Gale LA et al. 2023, QRSEH 15(3):417–430, abstract on Northumbria University's research portal, "significant working others", https://researchportal.northumbria.ac.uk/en/publications/repairing-relationship-conflict-in-community-sport-work-offender-/

[should-fix] [accuracy] §5 "What follows for you", first bullet; Current: "as signs they will interpret, often wrongly [weak"; Problem: "often wrongly" is not in van Kleef et al. 2019. That study measured whether coaches' displays predicted players' emotions, inferences and team outcomes, not whether players read the displays accurately. The clause adds an unsourced claim under a [weak] grade; Fix: "as signs they will interpret [weak"; Basis: van Kleef GA et al. 2019, PSE 41:1–11, abstract on the University of Amsterdam's repository, https://dare.uva.nl/id/1292444c-3492-41e7-a862-48243aaeded8

[should-fix] [figure] §3 second viz block (range); Current: "{"kind": "range""; Problem: the block plots five single point estimates of different associations (low = high = point). That is numbers compared, so the kind should be bars or compare. Range is for competing estimates of one quantity; Fix: not given as exact JSON, because the packet does not include kit/viz.py's schema for bars or compare and I will not invent one. The rows, values and caption can stay as they are; only the kind and its field names change; Basis: audit-units-SKILL.md §3, Figures paragraph (P41).

[minor] [accuracy] §1 "What follows for you", fourth bullet; Current: "You will read athletes you share attention with more accurately than athletes you watch from a distance; in a team, that is most of the squad most of the time [weak"; Problem: the study compared coaches in individual and team sports, with shared cognitive focus mediating the difference. "Watch from a distance" and "most of the squad most of the time" are the unit's own extrapolation and are not marked as such; Fix: "Coaches in individual sports, who shared more of their athlete's focus, read the athlete more accurately than coaches in team sports; in a team sport, expect to misread more often [weak"; Basis: Lorimer R, Jowett S 2009, PSE 10(1):152–158, abstract on Abertay University's research record, https://rke.abertay.ac.uk/en/publications/empathic-accuracy-in-coach-athlete-dyads-who-participate-in-team-/

[minor] [attribution] Sources, Smoll et al. 2007; Current: "*Journal of Youth Development* 2007;2(1):0701FA002."; Problem: the publisher's record gives pages 19–36, and the article prints the ID 0701FA002. The entry gives only the ID; Fix: "*Journal of Youth Development* 2007;2(1):19–36 (Article 0701FA002)."; Basis: Journal of Youth Development article page, https://jyd.pitt.edu/ojs/jyd/article/view/358

[minor] [figure] §3 "How regulation develops", McRae et al. 2012; Current: "The abstract read does not give the sample size or say which way the curve bends, so this unit states only that reappraisal ability changed with age across 10 to 22 and not in a straight line."; Problem: the full text, which is open on PubMed Central, gives the sample, so the unit can state it; Fix: "The full text (PubMed Central, read 18 Nov 2026) gives 38 participants: 12 older children, 10 adolescents and 16 young adults, the last aged 18 to 23 there. It does not say in words which way the curve bends, so this unit states only that reappraisal ability changed with age across 10 to 22 and not in a straight line."; Basis: McRae K et al. 2012, SCAN 7(1):11–22, https://pmc.ncbi.nlm.nih.gov/articles/PMC3252634

[minor] [style] Deliverable, opening paragraph (case facts); Current: "Scripts are this unit's own wording; no study opened tested any of them. Grades follow SP1's key."; Problem: the scripts name events that are neither in case-facts.md nor marked *added*: Dani's coach raising his voice "after the second round, in front of the squad"; Milan's coach shouting "On Saturday … after five minutes"; Milan "starting, on the criteria I gave the squad". The brief requires every invented fact to be listed in the notes, and I could not see the notes; Fix: "Scripts are this unit's own wording; no study opened tested any of them. Events named inside the scripts (a raised voice after a round, a touchline shout, a starting place) illustrate the wording and are not facts added to the case. Grades follow SP1's key."; Basis: case-facts.md (packet); brief.txt, running-case rule.

Every Current string above was checked with grep -cF and occurs exactly once in unit.md.

## Passes

**Coverage.** Every brief item is covered: face and posture; baseline, deviation and asking; regulation across the four bands (19 to 25 is thin, and the unit says no study opened compares it); interpersonal regulation and younger athletes; the coach's expressed emotion; the four requests against the SP3 needs and SP4 avoidance, with the reasoning shown; the seven states with ask, do, do not and grade; feedback after an error; differences between athletes, sexes and cultures; diagnosis as questions; repair. Deliverable: baseline sheets (training, before and after competing) for Dani, Milan and Sara plus a template; the general state-response table, three per-athlete tables and a template; five scripts per athlete plus a template. All are built in full. Length: about 6,150 words before the Deliverable and about 4,400 in it (11,800 with Sources), against the brief's 2,000–6,000. Recorded, not a finding.

**Flags.** (a) Grade key from SP1 section 9: stated in the preamble (line 12) and applied throughout. (b) Single SP3 behaviours not graded as tested: §6 says so in so many words, and requests are [practice]. §8 point 4, "never punish the mistake", is graded "as part of the package", which is honest and acceptable. (c) SP4 "how nervous" and SP6 "how much pressure" kept apart: §2, all three baseline sheets and the template keep them in separate lines, "never averaged or compared". PASS. (d) Sex, culture and diagnosis: sex rests on two opened sources (Sanchis-Sanchis, Wei); culture rests on Barrett (overstated, see finding); diagnosis rests on Reardon 2019 for ADHD, and autism is explicitly left unsaid. PASS apart from the Barrett finding.

**Claims** (each opened by me):
- Barrett 2019, six emotions, variation across cultures, "often communicates something other than an emotional state", recommendation of descriptive terms: PASS (PMC). Remote-culture claim in §9: FAIL (see finding).
- Aviezer 2012: PASS (Princeton record abstract).
- Lorimer & Jowett 2009, 40 dyads, individual > team, mediated by shared focus, session length: PASS.
- Friesen 2018, one coach and 3 athletes aged 18–20, national or international, anger and enthusiasm against anxiety and calmness, case study, small sample as a limitation: PASS (JYX full text).
- Fröjdö Regborn 2025, N 93, ages 15–17, three waves over about 12 months, β −0.33 and 0.34, coach style β 0.20, 0.20 and 0.19, "paradoxical", suppression unreliable at T1 (α 0.44), "causality cannot be inferred", both strategies rose: PASS (MDPI).
- Robazza 2023, N 424, ages 16–36, mean 23.08, mostly regional, cross-sectional, autonomy and relatedness to pleasant emotion via reappraisal, competence and relatedness to less suppression: PASS.
- Sanchis-Sanchis 2020, N 254, ages 9–16, eight schools, Valencian Community, age effect larger than gender, interaction direction: PASS. The age-direction question SP2 raised is not settled by the unit and was not checkable in the text I opened.
- McRae 2012, age groups and "linear and quadratic" quotation: PASS.
- Tamminen 2016, N 451 and 38 teams: PASS. Worsening clause: FAIL (finding).
- Tamminen 2021, N 509, 50 teams, Canada and UK, mean age 19.0, cross-sectional retrospective, received regulation not associated once self-regulation was in the model and associated when it was removed: PASS.
- Morris 2007, three routes and adolescence: PASS (PMC).
- van Kleef 2019, two studies (baseball/softball cross-sectional; soccer before, during and after), happiness and performance quotation: PASS. "Often wrongly": FAIL (finding).
- McMurtry 2010, N 100, ages 5–10, venipuncture, own-parent clips and vignettes: PASS (Dalhousie record).
- Smoll 2007, N 151, ages 9–15, basketball, matched quasi-experimental design across two programmes, coach behaviour not recorded, four Mastery Approach to Coaching guidelines on mistakes: PASS (JYD full text).
- Saemi 2011, N 28, mean age 10.6, beanbags, 3 best vs 3 worst of 6, retention one day later, intrinsic motivation: PASS.
- Chiviacowsky et al. 2007, N 40, ages not given, no retention difference: PASS.
- Chiviacowsky & Wulf 2007, KR-good better at retention: PASS (abstract). That this sample was adults was not shown on the page opened: unverifiable.
- Gouttebarge 2021, entourage including coaches, N 360 at two forums, the three attendee groups, modified Delphi: PASS. Per the methods, the Delphi was applied to SMHAT-1; the unit's "one of two tools built from…" is acceptable.
- ISSF page, "recognise… not diagnose", red-flag wording, undated with © 2025 footer: PASS.
- Reardon 2019, ADHD wording, "scant data" quotation, features, psychosocial interventions including education for coaches, WADA in-competition ban and TUE: PASS. Autism not found in the first part: consistent with the unit's hedge.
- Wachsmuth 2017, 80 papers and 6 direct: PASS. Wachsmuth 2018, N 22 and the coach central: PASS.
- Gale 2023, N 18, accounts, apologies, concern, acceptance: PASS. "Not athletes": FAIL (finding).
- Wei 2025, N 698, ages 12–18, three schools in Yantai and Weihai, Shandong, basketball, soccer, swimming and badminton, "multi-wave" in the abstract against "cross-sectional" in the discussion, team-sport interaction β 0.057, ΔR² 0.009, individual sports not significant, effects called small or modest: PASS (Frontiers full text).

**Bibliography** (against publisher, PubMed Central or repository records; Crossref itself not opened, because no search returned a Crossref URL):
- Matching field by field: Aviezer, Barrett, Chiviacowsky 2007, Friesen, Fröjdö Regborn, Gale, Gouttebarge (55(1):30–37, issue Jan 2021), ISSF, Lorimer, McRae (DOI confirmed on PMC), Morris (authors and DOI confirmed on PMC), Reardon (53(11):667–699, Arizona record), Robazza, Saemi (the publisher's primary title is Portuguese; the English title appears on the English page), Sanchis-Sanchis, Tamminen 2016, Tamminen 2021, van Kleef, Wachsmuth 2018, Wei.
- Smoll: pages missing (minor finding).
- Chiviacowsky & Wulf: title, journal, 78(2):40–47 and DOI match; authors not shown on the record opened, so unverified.
- McMurtry: Pain 150:52–58 and DOI match; the record gives "Megan McMurtry", so the initials "CM" are not verified; issue not shown.
- Wachsmuth 2017: the repository gives 2016 with 10(1):84–107; the print year 2017 is not verified.
- No reference was found to be non-existent.

**Source log.** Not available to this check (not in the packet). Instead I checked that every abstract-only claim says so in the unit. It does, at every citation: Aviezer, Lorimer, Gouttebarge, McRae, Tamminen ×2, Morris, van Kleef ×3 mentions, McMurtry, Saemi, Chiviacowsky ×2, Wachsmuth ×2, Gale. Barrett and Reardon are labelled as partial full-text reads. PASS.

**Grades.**
- §1 face [weak, review outside sport]: fits rule 5.
- §1 the Friesen case study [weak] and Lorimer [weak]: fit.
- §3 regulation [weak]: two correlational athlete samples and non-sport studies, so fits.
- §4 [weak] for the associations and [practice] for the age-band behaviours: fit.
- §5 [weak]: two field studies, abstract only; fits.
- §6 [practice] throughout, McMurtry [weak, outside sport, inference]: fit.
- §7 and the state-response table: [practice] or SP5's and SP1's carried grades, each stated.
- §8 package [weak], feedback timing [contested] (the null child study against two positives), wording [practice]: fit the key.
- §10 [practice; IOC consensus; studies not opened]: fits the course convention stated in the preamble.
- No grade exceeds its evidence. PASS.

**Population.**
- Every study names its sample: children 5–10; pupils 9–16; 10–22 laboratory; athletes 15–17; adolescents 12–18; adult athletes; community coaches.
- Where a sample is missing (Lorimer, van Kleef, Tamminen 2016 ages), the unit says so.
- Transfers to under-18s are labelled inference (§1 bullets, §4 Morris, §5 bullets, §6 McMurtry, §8 Saemi, state-table rows), and §8 uses "outside the sampled ages" for 16–25.
- PASS, apart from the §1 extrapolation (minor finding).

**Scope and safety.**
- Nothing teaches assessment, diagnosis or treatment. §2 says a baseline "is not a test"; §10 says "you do not assess, diagnose or treat".
- No weight-loss method, calorie figure or target weight. Dani's food concern is routed to her scope card with no comment on food or body.
- No method of self-harm.
- Disclaimer at line 12.
- No law is stated as the reader's. TUE and reporting routes are questions with the body to consult (national anti-doping organisation; club welfare or safeguarding officer; national sport body). The WADA rule is attributed to the 2019 statement and dated.
- No real athlete, coach or club is named.
- PASS.

**Any sport.** I counted examples by sport, treating each case athlete's sheet, table and script set as one example each:
- judo 4 (§8 judoka plus Dani ×3)
- football 4 (§5 Milan's coach plus Milan ×3)
- athletics/400 m 4 (§7 Sara plus Sara ×3)
- gymnastics 2, and tennis, rowing, volleyball, hockey, racket sport 1 each

Total 19; the largest share is 4/19, about 21%, under a third. The spread covers individual, team, weight-class (judo), judged (gymnastics) and endurance (rowing). PASS.

**Part 7, line by line.**
- Sourced where made: yes, except the three FAIL clauses above.
- Source types: yes. ISSF is a federation's reproduction of the IOC tool and is labelled as such.
- No video, blog or press source: yes.
- Source log: not checkable (see above).
- Sources against records: see Bibliography.
- Five grades per SP1 key: yes.
- Sample and design stated; correlation called correlation: yes.
- Adult-to-young inference labelled: yes.
- Effect sizes in the source's terms with sample: yes (β values with N 93; Wei β and ΔR² with N 698).
- Popular claims set against evidence: yes (face reading; harsh coaching carried from SP1 and SP3).
- Coach's part and handover: yes.
- Weight and self-harm: yes.
- Law as question, disclaimer: yes.
- No real persons: yes.
- Three or more kinds of sport, none above a third: yes.
- Case labelled "(fictional)" on first use, agrees with case-facts.md, never evidence: yes, apart from the unmarked script events (minor finding). Sara's "SP6 routine" is SP5 skills kept at SP6's review, which is acceptable.
- Private terms: kit/private_terms.py is not in the packet, so not run; nothing about the Project's owner appears on reading.
- Search flag: off for SP7, so not applicable.
- Deliverable in full and as templates: yes.
- Does not read as advice without evidence: yes. Each section separates tested from practice.
- Links as DOI links: yes.

**Read as the coach in the preamble.** The unit is usable: it tells the coach plainly which parts are untested, and the tables work standalone on a phone. Two things would make a checking coach stop. The §4 Tamminen misreading is one, because it inverts what was measured. The §9 culture sentence is the other, because it states more than the review found.

**Figures (7).**
- Figure 1, flow, §2: every label traces to §2's text ("Observe, compare, ask"; "write down their words"; SP4's table and the red flag the same day; "so you rewrite it"). The caption names the section, the SMHRT-1/ISSF source and SP4. Kind fits a sequence. PASS.
- Figure 2, range, §§3 and 5: every value traces to the text (−0.33, 0.34 in §3; 0.20, 0.20, 0.19 in §5). The caption names the sections, the source and the design. The kind does not fit point estimates of different associations; it should be bars or compare. FIX (should-fix; exact JSON not given, see finding).
- Figure 3, decision, §6: the questions and outcomes trace to §6 ("A sore hamstring goes to the medical plan; illness, exhaustion or a red flag goes to your scope card"; "Offer a smaller step instead … agreed with the athlete"; "say when you will come back"; "give one, from what they have already practised … afterwards ask them what they would choose"). The caption names the section, SP3 and SP4, and says the rule is untested. Kind fits a rule with branches. PASS.

**Cross-unit pointers not verifiable here** (the other units are not in the packet):
- SP1 section 9 key and rule numbers
- SP1's harsh-coaching grade and SP3's regrade
- SP2's note on Sanchis-Sanchis
- SP4 normal-or-refer rows 5–8
- SP5 breathing grades
- SP6 debrief question 4 and step-down rule
- SP2 and SP4 calling for Sara's referral

## Claims I could not verify
- Chiviacowsky & Wulf 2007: author names, and that the sample was adults ("the adult study").
- McMurtry 2010: first-author initials and issue number.
- Wachsmuth 2017: print year 2017.
- Aviezer 2012: number and kind of observers (the unit says the abstract does not give them; consistent).
- Lorimer 2009: accuracy figures, ages, sports (the unit says these are not given; consistent).
- van Kleef 2019: sample sizes and ages (the unit says these are not given; consistent).
- Sanchis-Sanchis 2020: direction of age on the overall score in the results tables.
- Reardon 2019: absence of autism in the unread remainder.
- Every cross-unit pointer listed above.
- Every *added* case fact, against the writer's notes (not in the packet).

## Confirmed
- Barrett 2019, six emotions; variation across cultures and situations; scowl quotation; descriptive-term recommendation — https://pmc.ncbi.nlm.nih.gov/articles/PMC6640856
- Aviezer 2012, body not face at peak intensity; face-body composites — https://collaborate.princeton.edu/en/publications/body-cues-not-facial-expressions-discriminate-between-intense-pos/
- Lorimer & Jowett 2009, 40 dyads; individual > team; shared focus; session length — https://rke.abertay.ac.uk/en/publications/empathic-accuracy-in-coach-athlete-dyads-who-participate-in-team-/
- Friesen 2018, case study of 1 coach and 3 athletes aged 18–20; desired-emotion mismatch; congruence and performance — https://jyx.jyu.fi/bitstream/handle/123456789/57932/1/ruiz10413200.2017.pdf
- Fröjdö Regborn 2025, all figures in §§3 and 5 — https://www.mdpi.com/2075-4663/13/9/284
- Robazza 2023, sample and paths — https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1205102/text
- Sanchis-Sanchis 2020, sample and gender-by-age interaction — https://public-pages-files-2025.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.00946/text
- McRae 2012, age groups and quotation — https://dspace.mit.edu/handle/1721.1/88513
- Tamminen 2016, N 451 and 38 teams; other-improving efforts; team climate — https://utoronto.scholaris.ca/items/b9851e86-aab8-41bf-be61-e44f4c256595
- Tamminen 2021, all of §4's description — https://researchportal.port.ac.uk/en/publications/the-effect-of-self-and-interpersonal-emotion-regulation-on-athlet/
- Morris 2007, three routes and adolescence — https://pmc.ncbi.nlm.nih.gov/articles/PMC2743505/
- van Kleef 2019, designs, findings and quotation — https://dare.uva.nl/id/1292444c-3492-41e7-a862-48243aaeded8
- McMurtry 2010, N 100, ages 5–10, both tasks — https://dalspace.library.dal.ca/handle/10222/74861?show=full
- Smoll 2007, N 151, quasi-experimental design, Mastery Approach to Coaching guidelines, behaviour not recorded — https://jyd.pitt.edu/ojs/jyd/article/view/358/344
- Saemi 2011 — https://revistas.usp.br/rbefe/article/view/16860
- Chiviacowsky et al. 2007 — https://revistas.usp.br/rbefe/en/article/view/16652
- Chiviacowsky & Wulf 2007, finding — https://lida.sport-iat.de/ta/Record/4012854?lng=en
- Gouttebarge 2021, entourage, N 360, three groups — https://pmc.ncbi.nlm.nih.gov/articles/PMC7788187
- ISSF SMHRT-1 page, red flag and "not diagnose" — https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool
- Reardon 2019, ADHD paragraph; WADA and TUE — https://www.psychiatry.wisc.edu/wp-content/uploads/2023/10/2019-Mental-health-in-elite-athletes-International-Olympic-Committee-consensus-statement-2019.pdf
- Reardon 2019, issue 11 — https://experts.arizona.edu/en/publications/mental-health-in-elite-athletes-international-olympic-committee-c/
- Wachsmuth 2017, 80 and 6 — https://repository.lboro.ac.uk/articles/journal_contribution/Conflict_among_athletes_and_their_coaches_What_is_the_theory_and_research_so_far_/9619040
- Wachsmuth 2018, N 22; coach central — https://repository.lboro.ac.uk/articles/journal_contribution/Managing_conflict_in_coach-athlete_relationships/9618692
- Gale 2023, N 18; forms of repair; acceptance — https://researchportal.northumbria.ac.uk/en/publications/repairing-relationship-conflict-in-community-sport-work-offender-/
- Wei 2025, all of §9's description — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1636707/full

Not checked under the web rule: one PubMed fetch, which returned a browser check, and one PMC address, which redirected; the same records were checked through other URLs from the search results.
