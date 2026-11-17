Verdict: SP3 · fix · 0 error, 6 should-fix, 7 minor

Model: claude-opus-5-5. Quality review of SP3 (Sport Psychology for Coaches), round 6, 17 Nov 2026, with live search. I re-opened every source in this agent and relied on no earlier review note. The harness would not let me write out/report.md, so the full report follows for the chat to save verbatim.

## Findings

f1 [should-fix] [figure] Section 1, figure 1 (line kind); Current: "{"kind": "line", "caption": "Perceived autonomy support and four kinds of motivation: pooled correlations (ρ) from 131 samples, 38,844 participants in sport and exercise, in the order section 1 gives them: Auton. = autonomous motivation, Intro. = introjected regulation, Ext. = external regulation, Amot. = amotivation. The line joins four separate estimates and shows no change over time. From section 1 of this unit: Mossman et al. (2024), International Review of Sport and Exercise Psychology, abstract. Correlational; ages not given in the abstract.", "x": ["Auton.", "Intro.", "Ext.", "Amot."], "unit": "", "decimals": 2, "min": -0.3, "max": 0.5, "yticks": [-0.2, 0, 0.2, 0.4], "ylabel": "ρ", "series": [{"values": [0.39, 0.16, -0.01, -0.19], "tone": 2}]}"; Problem: the figure compares four separate estimates that have no order in time, but draws them as a line. The kind does not fit the data's shape, which is why the caption has to warn that the line means nothing. In kit/viz.py, compare and bars refuse negative values (tested: "compare draws values of 0 or more"). Range with low = high draws each estimate as a point on one signed axis, and it rendered without error here. Fix: "{"kind": "range", "caption": "Perceived autonomy support and four kinds of motivation: pooled correlations (ρ) from 131 samples, 38,844 participants in sport and exercise, in the order section 1 gives them; each diamond is one estimate. From section 1 of this unit: Mossman et al. (2024), International Review of Sport and Exercise Psychology, abstract. Correlational; ages not given in the abstract.", "unit": "", "min": -0.3, "max": 0.5, "ticks": [-0.2, 0, 0.2, 0.4], "rows": [{"label": "Autonomous motivation", "low": 0.39, "high": 0.39, "tone": 2}, {"label": "Introjected regulation", "low": 0.16, "high": 0.16, "tone": 2}, {"label": "External regulation", "low": -0.01, "high": -0.01, "tone": 2}, {"label": "Amotivation", "low": -0.19, "high": -0.19, "tone": 2}]}"; Basis: audit-units §3, figures paragraph (numbers compared: compare or bars; a trend: line); kit/viz.py render test; values from https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252.

f2 [should-fix] [bibliography] Sources, Mossman et al.; Current: "(abstract read; authors, volume and pages from the course's seed list)"; Problem: the publisher page opened (informahealthcare.com, abstract only) shows no authors, volume, issue, pages or year. These fields are not verified at a publisher, PubMed or Crossref record, and the seed list was checked for existence only, yet the entry does not say "not verified". The abstract's numbers were confirmed. Fix: "(abstract read at the publisher's page, https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252, 17 Nov 2026; authors, volume, issue, pages and year not verified: taken from the course's seed list, not shown on the page opened)"; Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252.

f3 [should-fix] [bibliography] Sources, Bergeron et al.; Current: "authors, title, volume and pages from the course's seed list, as the page showed initials only and no journal details)"; Problem: the publisher page shows only the contributors' initials. Its address gives volume 49, issue 13 and first page 843. The authors and the end page 851 are not verified, and the entry does not say so. Fix: "volume 49, issue 13 and first page 843 as in the publisher's address; authors and end page not verified: taken from the course's seed list, as the page showed initials only and no journal details)"; Basis: https://bjsm.bmj.com/content/49/13/843.full.

f4 [should-fix] [bibliography] Sources, Fletcher & Sarkar; Current: "(abstract and notes read; bibliographic details from the course's seed list)"; Problem: the publisher page shows only the abstract, acknowledgements and notes. It gives no authors, journal, volume, issue, pages or year, so every bibliographic field is unverified, and the entry does not say so. Fix: "(abstract and notes read at the publisher's page, https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496, 17 Nov 2026; authors, journal, year, volume, issue and pages not verified: taken from the course's seed list, not shown on the page opened)"; Basis: https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496.

f5 [should-fix] [bibliography] Sources, Gustafsson et al.; Current: "(abstract read; bibliographic details from the course's seed list)"; Problem: the publisher page shows only the abstract and no citation fields. The fields are not verified at a publisher, PubMed or Crossref record, and the entry does not say so. Southern Cross University's research portal shows the same 4(1):3–24, but an institutional record corroborates; it is not the publisher. Fix: "(abstract read at the publisher's page, https://informahealthcare.com/doi/full/10.1080/1750984X.2010.541927, 17 Nov 2026; authors, volume, issue, pages and year not verified at the publisher: taken from the course's seed list)"; Basis: https://informahealthcare.com/doi/full/10.1080/1750984X.2010.541927.

f6 [should-fix] [bibliography] Sources, Burke et al.; Current: "(authors and journal from Ulster University's research record; not shown on the publisher page opened)"; Problem: neither the full-text page nor the abstract page at the publisher shows the authors or the journal. Ulster's record (Burke, Sharp, Woods, Paradis; International Review of Sport and Exercise Psychology) is not a publisher, PubMed or Crossref record, so these fields are unverified and the entry must say so. Pages 208–235 and the online date of 7 November 2021 were confirmed at the publisher. Fix: "(authors and journal not verified: taken from Ulster University's research record, not shown on the publisher page opened)"; Basis: https://informahealthcare.com/doi/full/10.1080/1750984X.2021.1992793; https://pure.ulster.ac.uk/en/publications/enhancing-parental-support-through-parent-education-programs-in-y/.

f7 [minor] [accuracy] Section 2 table, Hu et al. row; Current: "aged 10 to over 25, in six Chinese provinces"; Problem: the paper's oldest band is "25 and above" (≥25 in Table 1), so the range includes 25-year-olds. Fix: "aged 10 to 25 and over, in six Chinese provinces"; Basis: https://frontiersin.org/articles/10.3389/fpsyg.2023.1106916/full.

f8 [minor] [accuracy] Section 2, closing grade; Current: "athletes aged 10 to over 25; no causal"; Problem: as f7. Fix: "athletes aged 10 to 25 and over; no causal"; Basis: as f7.

f9 [minor] [accuracy] Section 10; Current: "one across 10 to over 25"; Problem: as f7. Fix: "one across 10 to 25 and over"; Basis: as f7.

f10 [minor] [accuracy] Deliverable C, the "Why" paragraph of the parents' page; Current: "athletes aged 10 to over 25 with lower"; Problem: as f7. Fix: "athletes aged 10 to 25 and over with lower"; Basis: as f7.

f11 [minor] [accuracy] Section 1, Mossman et al.; Current: "and associations with need satisfaction"; Problem: the abstract reports "strong positive associations between autonomy support and athlete basic psychological needs". It does not use the term "need satisfaction" or report on it. Fix: "and strong positive associations with athletes' basic psychological needs"; Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252.

f12 [minor] [population] Deliverable, opening paragraph; Current: "the [moderate] grade for autonomy support as a whole comes from Mossman et al. (2024), section 1."; Problem: self-audit rows S1–S4 and S10 apply the [moderate] grade to Dani's and Milan's squads, who are under 18, but the meta-analysis gives no ages. The grade key requires a grade applied to under-18s from samples not shown to include them to carry the inference label. Fix: "the [moderate] grade for autonomy support as a whole comes from Mossman et al. (2024), section 1; its abstract gives no ages, so for athletes under 18 that grade is the unit's inference, and the evidence opened in 12- to 18-year-olds is weak (section 2)."; Basis: grade-key-SP1-section9.md ("A grade from adults, students or non-athletes applied to an athlete under 18 carries the label inference"); https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252.

f13 [minor] [source log] Unsure list, item 1; Current: "journal inferred from the DOI prefix"; Problem: this contradicts the Sources entry, which says the journal came from Ulster University's research record. Fix: "journal from Ulster University's research record, not verified at the publisher"; Basis: unit.md Sources, Burke et al.; https://pure.ulster.ac.uk/en/publications/enhancing-parental-support-through-parent-education-programs-in-y/.

## The seven passes

**Claims.** I re-opened every cited claim at its publisher (at PubMed Central for Monteiro). All PASS except f11 (a wording stretch) and f7–f10 (the age band).
- Gao et al. (2024) opened at https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1291711/full, an address a search returned.
- The page confirms: 29 studies (26 quantitative, 3 qualitative); 9,185 athletes and 2,191 parents; 82.8% cross-sectional; inclusion ages 10–19.
- Findings confirmed: parental autonomy support with self-determined motivation; pressure with controlled motivation and amotivation, with one contrary study (Amado et al., 2015); support with enjoyment; parents against coaches mixed.
- The quotation "the manner and extent of their involvement are key" is exact.
- Gao is PASS, so the unit needs no "not verified" there.

No claim in the body is marked unverified where it is in fact verified. No editing instruction or reviewer-process note sits in the body text (sections 1–11 and the Deliverable). Process notes appear only in Sources, which serves as the unit's source log, and in the unsure list.

**Bibliography.** Thirteen entries match their publisher records field by field: Adams, Gao, Gómez-López, Gu & Cheng, Haberstock, Hu, Lewis, Monteiro, Morales-Sánchez, Smoll, Tzioumakis (14 names shown plus "+5 more", as the entry says), Zhang Wang & Shao, and Zhang Du & Tao. Five entries have fields that were not verified at a publisher and are not marked so: f2–f6. No reference turned out not to exist.

**Source log.** SP3 has no separate log; the Sources list gives the address, what was read and the date for every entry. Claims resting on an abstract say so in the text (Mossman, Gustafsson; "abstract and notes" for Fletcher & Sarkar). PASS, with f13.

**Grades.** Every grade names or follows a rule of section 9:
- Mossman [moderate, association]: rule 4, on a stated reading, with its fallback to weak.
- Zhang Wang & Shao [moderate]: rule 4 (k = 4–5, wide CI).
- Single surveys and the two controlled studies [weak]: rule 5.
- Gao [weak]: rule 5.
- Untested steps [practice]: rule 2.
- Harsh-coaching regrade [weak, against]: rule 5.

Each grade has its direction beside it. PASS, with f12.

**Population.** Each finding names its sample and design, and correlations are called correlations. Transfers to under-18s are labelled inference in sections 4, 5, 6 and 7. f12 is the one gap.

**Scope and safety.** PASS on every check:
- Nothing teaches assessment, diagnosis or treatment.
- Burnout and referral end at the scope card (section 8).
- Abuse and safeguarding concerns go to the welfare or safeguarding officer (sections 4 and 9). Consent for filming is put as a question (Deliverable A).
- No weight-loss method, calorie figure or target weight, and no self-harm method.
- No law is stated as the reader's.
- The disclaimer is in the opening paragraph and on each parents' page.
- No real person is named against the rule.

**Any sport.** The unit's 17 examples:
- Judo (Dani): self-audit column, three changes, session plan, parents' page.
- Football (Milan): the same four.
- 400 m (Sara): the same four.
- One each for swimming, gymnastics, volleyball, rowing and tennis (section 2).

Each case sport supplies 4 of 17 (24%), so none is above a third. Individual, team and timed sports are all present. PASS.

## Part 7, line by line
- Sourced where made: PASS.
- Source types: PASS (no blog, video or press report cited).
- Source log: PASS, with f13.
- Publisher match: f2–f6.
- Grades: PASS, with f12.
- Sample and design: PASS.
- Inference labels: f12.
- Effect sizes in the source's terms: PASS (ρ, r, β, SMD, I² as the papers give them).
- Popular claims named and set against evidence: PASS (harsh coaching, exercise as punishment, praise in public / correct in private, high challenge–high support).
- Coach's part: PASS.
- Weight and self-harm: PASS.
- Law: PASS.
- Real persons: PASS.
- Three kinds of sport, none above a third: PASS.
- Case facts labelled "(fictional)" on first use and agreeing with case-register.md: PASS (every invented fact is marked *added* and appears in the register's SP3 rows).
- Owner's details: none seen.
- Search flag: off, not applicable.
- Deliverable built on the case and given as templates: PASS.
- Not advice without evidence: PASS.
- Links given as DOI links: PASS.

## Brief and deliverable completeness
PASS. Coverage by section:
- s1: self-determination theory (the three needs; supporting a need against thwarting it) and achievement goal theory, with youth evidence and its design.
- s2: the behaviours one by one, with outcomes and whether each finding is correlational; effort stated as unmeasured.
- s3: coach-training interventions, with samples.
- s4: rewards, punishment, exercise as punishment.
- s5: selection, playing time, attention.
- s6: high challenge–high support and what it rests on.
- s7: enjoyment and dropout.
- s8: burnout and overtraining per consensus; the AAP and ECSS/ACSM statements were not opened, and the unit says so.
- s9: parents.

Deliverable:
- A 20-behaviour self-audit (S1–S10, C1–C10), built on all three case squads, with a template.
- Three session plans, each written twice (judo as the individual sport, football as the team sport, 400 m as the timed sport), with a template.
- A parents' page for Dani's squad, adapted for Milan's, and for adult Sara given to the athlete, with a template.

## Flags naming SP3
- F26: section 11 builds on SP2's table and development note. Met.
- F27: section 10 states the regrade as the flag says. Consistent.
- F28: consistent with the grades in sections 1–3.
- F29: consistent with section 2 ("What no study opened here does is test any single behaviour on its own").
- F30: section 5 grades public/private feedback as practice and names Stein, Bloom & Sabiston (2012) as not opened. A search here returned only a copy on McGill's site and catalogue records. Consistent.
- F35: section 4 states no effect of rewards. Consistent.
- F37: the parents' page is built for the start of a season and given to the athlete for Sara. Consistent.
- F41: every item now checked at its publisher in this review. The IOC quotations in sections 5, 7, 8 and 9 were found word for word at bjsm.bmj.com; the Gómez-López numbers, Adams beyond the sample size and Monteiro in full text at PMC all hold. Nothing is left to cut or mark, so F41 can close.
- F44: this review.

## Figures
All three blocks parse as JSON and render with kit/viz.py. To render them I ran a copy of viz.py outside the packet against a stub theme file, because design/theme.css is not in the packet.
1. Line, section 1. Labels and numbers trace to the section 1 text ("ρ = .39 ... −.19", 131 samples, 38,844); the caption names the section and the source. The kind does not fit: FIX (f1).
2. Compare, section 1. 313, 12, 9, 334 and 177 trace to the section 1 text; the caption names the section and the source: PASS.
3. Line, section 3. 25.44, 23.98, 24.12, 27.01, the range 15 to 60, about 12 weeks and ages 9 to 15 trace to section 3. It shows change over time in two groups; the caption names the section, the source and the design: PASS.

## Could not verify
- Mossman et al. (2024): authors, volume, issue, pages, year (not on the publisher page opened).
- Bergeron et al. (2015): the author list and the end page (the publisher page shows initials only).
- Fletcher & Sarkar (2016): all bibliographic fields, and the main text (not visible).
- Gustafsson et al. (2011): the citation fields at the publisher (confirmed only at Southern Cross University's portal).
- Burke et al. (2021): authors, journal, volume and issue at the publisher (confirmed only at Ulster's record).
- Tzioumakis et al. (2026): the five authors not shown on the publisher page, and the initials of all authors (the fetch gave surnames only).
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7013665/ (Gómez-López at PMC): redirected, not checked. The paper was verified at mdpi.com instead.

## Confirmed
- Mossman et al. 2024: 1,320 correlations, 131 samples, N = 38,844; ρ = .39, .16, −.01, −.19; well-being and distress; no moderation by culture or type of sport; competence and relatedness support, structure and involvement listed; no ages given. https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252
- Gómez-López et al. 2020: 479 players (250 boys, 229 girls) aged 16–17, on regional teams at Spanish championships, data taken during the championship; PMCSQ-2 items quoted exactly; r = 0.43 and −0.31; mediation through fear of failure to somatic and cognitive anxiety; task-climate path non-significant. https://mdpi.com/1660-4601/17/2/592
- Gu & Cheng 2026: 177 studies, 334 effect sizes (313/12/9); r = 0.27, CI 0.22–0.32 in the table and 0.20–0.32 in the text; I² = 98.45% overall, none for the task subgroup; "pattern of association"; coding of undesirable outcomes not stated. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1716745/full
- Morales-Sánchez et al. 2020:
  - 103 male footballers aged 12–17, one club, convenience sample, one session.
  - CCBS four subscales; negative conditional support defined; Bartholomew et al. 2010 cited as the scale's origin.
  - Thwarting "stronger" than the absence of satisfaction.
  - β = 0.53, indirect effect 0.35; ABQ's three dimensions.
  - The autonomy-supportive description and recommendations.
  - https://mdpi.com/1660-4601/17/13/4909
- Hu et al. 2023: 252 athletes on professional teams in six provinces, team and individual sports, cross-sectional; γ = −0.46; mediation through constrained commitment; no direct effect on fear of failure. https://frontiersin.org/articles/10.3389/fpsyg.2023.1106916/full
- Zhang, Du & Tao 2025: 325 athletes aged 12–18 in China, two waves two weeks apart, coach-rated development, "causation cannot be established". https://www.frontiersin.org/articles/10.3389/fpsyg.2024.1433171/full
- Zhang, Wang & Shao 2022:
  - 21 studies, 1,199 participants aged 5–19; 9 cross-sectional, 12 longitudinal.
  - Enjoyment r = 0.45 (0.42–0.49, k = 4).
  - Coach support r = 0.43 (0.08–0.69, k = 4) and SMD 0.68 (0.27–1.10, k = 5).
  - Intention SMD 1.13; enjoyment and persistence not pooled.
  - Sports listed include judo, handball and ice hockey.
  - https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.871936/full
- Smoll et al. 2007:
  - Workshops of 75 and 60 minutes; 17 + 17 teams, 34 coaches.
  - 82/69 athletes analysed, 151 aged 9–15 (mean 11.6); about 12 weeks apart; SAS-2 range 15–60.
  - Means 25.44→23.98 and 24.12→27.01; interactions significant for the total and all three subscales.
  - Quasi-experimental; only athletes whose families attended were counted; no behaviour data; no effect sizes.
  - The first author presented the workshops; Smoll & Smith wrote the manuals.
  - The guideline list.
  - https://jyd.pitt.edu/ojs/jyd/article/view/358/344
- Tzioumakis et al. 2026:
  - 68 coaches in four countries, randomised 36/32; the Empowering Coaching programme; MMCOS described as "validated"; three time points.
  - Disempowering and ego-involving behaviour declined; gains in autonomy and relatedness support were temporary.
  - About 6 hours of workshop; players aged 10–15; no standardised effect sizes; no athlete outcomes; "short-term, but not sustained".
  - Volume 17, published 5 August 2026.
  - https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full
- Adams et al. 2024: 20 former college athletes, nine sports, mean age 26.0 (19–44), US, interpretive description; some physical punishment accepted; punitive conditioning described as arbitrary, unsafe or cruel; accounts of injury and fear; 6:1428682. https://www.frontiersin.org/articles/10.3389/fspor.2024.1428682/full
- Lewis et al. 2023: 48 analysed, non-disabled adults aged 18–40; positive social comparative feedback did not improve retention against no feedback; perceived competence rose in RT+POS and CONTROL, not in RT ONLY; 13:1005705, 24 January 2023. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.1005705/pdf
- Haberstock et al. 2024: 101 team-sport athletes, M = 28.68, no range given, 39.6% with a physical disability, cross-sectional; a peer-created disempowering climate went with autonomy and relatedness frustration; 54(4):609–614. https://link.springer.com/article/10.1007/s12662-024-00980-4
- Fletcher & Sarkar 2016: the quotations from notes 3 and 7 are exact ("the world's best athletes and teams"; "extreme challenge-no support environments"; "the unethical and inappropriate imposition of adversity"); the 2012 and Rio Olympics are mentioned; no model is named; no test is reported. https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496
- Bergeron et al. 2015: all ten quotations in sections 5, 7, 8 and 9 found word for word. https://bjsm.bmj.com/content/49/13/843.full
- Gustafsson et al. 2011: burnout described from a process and a state perspective; the model covers antecedents, early signs, consequences, personality, coping and environment; "not to present the definitive model". https://informahealthcare.com/doi/full/10.1080/1750984X.2010.541927
- Monteiro et al. 2017: six studies, ages 5–30, four from Canada, studies from 1982 and 1985, mixed designs, the reasons listed, "controllable by the athletes"; 727 participants in the text against about 955 in the table. https://pmc.ncbi.nlm.nih.gov/articles/PMC5968952
- Gao et al. 2024: as under Claims. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1291711/full
- Burke et al. 2021: 12 studies, ages 5–18, tennis and soccer most common, MMAT 20–100%, all five quantitative studies significant, "difficult to draw concrete conclusions", "clear absence of sport-specific measures"; pp. 208–235, online 7 November 2021. https://informahealthcare.com/doi/full/10.1080/1750984X.2021.1992793
- Stein, Bloom & Sabiston (2012): a search found it only as a copy on McGill's site and in catalogue records, as section 5 says.
