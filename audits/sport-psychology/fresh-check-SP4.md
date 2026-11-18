---
audit: fresh check
unit: SP4 · Anxiety, arousal and performing under pressure
course: sport-psychology · Sport Psychology for Coaches
model: claude-opus-5-5
date: 2026-11-18
chat: https://claude.ai/code/session_01KMmgQzkkwQTdz1FagqESmS
verdict: fix · 1 errors, 8 should-fix, 8 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

# Fresh check · SP4 · Anxiety, arousal and performing under pressure

Checker: claude-opus-5-5, isolated agent context, 18 Nov 2026. I have not seen the unit written. Inputs: unit.md, brief.txt, sourcing-standard.md (Part 1 and Part 7), case-facts.md, notes.md, unsure.md, sources.md. Live search and fetch were used. Two fetches were refused and are reported as not checked: the BJSM full text through a library proxy (bjsm-bmj-com.bibliotheek.ehb.be), and the Lochbaum PMC copy (reCAPTCHA; the MDPI page was read instead). SP1's filed text is not in the packet, so check (4) is made against the quotation of SP1's card in notes.md.

## Pass 1 · Claims
Result: 1 error and 6 should-fix. Most numbered claims PASS (see Confirmed). The failures: one design claim taken from an unopened paper, one red-flag sign stretched beyond its source, one finding reported selectively, and one internal contradiction.

## Pass 2 · Bibliography
Result: 1 minor. The entries match the records I opened. The exceptions: the Iniesta-Sepúlveda issue and author order can now be set from a publisher-side record, and the Arent & Landers DOI is still unverified (no search in this run returned it).

## Pass 3 · Source log
Result: PASS. Every Sources entry is in sources.md with its address, what was read and the date. The not-opened Smith, Smoll & Cumming (2007) entry is logged as not opened. Smith 2007 is not relied on for any number or grade, but one design word rests on it (finding E1).

## Pass 4 · Grades
Result: 2 should-fix. Grades mostly follow SP1's key as the unit states it. Two tags claim more support than the cited source gives: the avoidance cycle is called "clinical consensus", and Milan's referral decision is tagged "IOC consensus".

## Pass 5 · Population
Result: 2 minor. The samples and age bands are stated throughout, and inference is labelled in sections 3, 4, 5 and 7. Row 1 of the table carries an elite-athlete statement to every age band without a label. The Rosebrock sample is described too narrowly.

## Pass 6 · Scope and safety
Result: PASS. The unit says it is recognition only and is information, not advice. Legal duties are put as questions, each with a body to consult. Weight figures and methods are absent, there is no self-harm method, no real person is named, and SMHRT-1 is not reproduced. Each topic says where the coach's part ends and who takes over.

## Pass 7 · Any sport
Result: PASS. The examples span football, athletics, judo, swimming, basketball, handball, volleyball, gymnastics, rowing, golf, shooting, tennis and figure skating. Football stays under a third once the brief-mandated Milan deliverable is set aside, and individual, team, weight-class, judged and endurance sports are all present.

## Specific checks
1. **The table "sets no threshold of its own".** FAIL as worded. The table does set thresholds of its own: "across a season" and "six weeks" in row 7 (also used in row 4 and the decision figure), and "for weeks" in row 3. All three are graded [practice], and unsure.md item 10 says so, so the grading is right. Every other ordinary range and referral point is cited (Reardon, ISSF, Grossbard) or graded practice. Only the sentence claiming "no threshold of its own" is false (S1).
2. **Reardon et al. (2019) Table 4.** I re-read the same university-hosted copy, with the same column scrambling. The attributions are as the unit gives them: social anxiety disorder "Symptoms must be persistent, typically lasting 6 months or more"; panic disorder "1 month or more of persistent concern"; generalised anxiety disorder (Table 3) "occurring most days for at least 6 months", "a number of events or activities" and "significant distress or impairment in important areas of functioning". The panic and social anxiety attributions follow the DSM-5 structure the table reproduces. The publisher's full text was not checked (the fetch was refused). The 6.0% / 14.6% prevalence figures, "do not appear to differ markedly", "is to be expected" and the "fear of negative evaluation" sentence all PASS.
3. **Smith, Smoll & Cumming (2007) is not relied on.** Mostly met: no number, finding or grade rests on it. One word does: "randomised". Smoll et al. (2007, JYD) say only "Similar anxiety reductions were found in a more recent study…" and give no design. The claim therefore rests on an unopened paper, which the course's sourcing rule bars (E1).
4. **Milan's referral-now row against SP1's card.** Consistent. notes.md quotes SP1's card as referring "Nausea, broken sleep and avoidance that persist or spread beyond match days". Milan's pattern has persisted for five years, so SP1's own "persist" branch is already met. SP4's referral now agrees with SP1 and does not tighten it as notes.md says. The unit does not say that SP1 agrees (M5). The Deliverable A grade tag overclaims (S5).
5. **Invented case facts.** The three *added* facts are marked in the unit and listed in notes.md. None contradicts case-facts.md. Two problems remain. Section 10 says nobody has asked Milan what he thinks, while Deliverable A records his words from a check-in (S4). And "Milan's coach has started the two check-in questions" is implied by two added facts but is not listed as an added fact (M7). The facts about Sara and Dani agree with the register.

## Findings

[error] [attribution] §7 Coach and parent training
Current: that study is the randomised trial of the coach programme (Smith, Smoll & Cumming, 2007)
Problem: "Randomised" is a design claim taken from a paper that was not opened. The source that was opened (Smoll et al., 2007, JYD) gives no design for the "more recent study". The course's rule is that a reference that could not be opened carries no claim.
Fix: they cite it as Smith, Smoll & Cumming (2007), and give no design for it
Basis: https://jyd.pitt.edu/ojs/jyd/article/view/358/344 ("Similar anxiety reductions were found in a more recent study using a multidimensional sport performance trait anxiety measure… (Smith, Smoll, & Cumming, 2007)"; no design stated)

[should-fix] [deliverable] Deliverable B, opening paragraph
Current: The table sets no threshold of its own: each ordinary range and each referral point is taken from a cited source or is graded practice, and says which.
Problem: Rows 3, 4 and 7 and the decision figure set thresholds of the unit's own ("for weeks", "across a season", "six weeks"). They are graded practice, which is correct, but the sentence denies they exist.
Fix: The table's only thresholds of its own are "for weeks" (row 3), "across a season" and "six weeks" (rows 4 and 7): they are graded practice, set by this unit for a coach, and no study opened sets them. Every other ordinary range and referral point is taken from a cited source, and each cell says which.
Basis: unit rows 3, 4 and 7; unsure.md item 10

[should-fix] [accuracy] Deliverable B, row 9
Current: sweating, breathlessness or chest symptoms
Problem: The SMHRT-1 red flag as the ISSF page gives it names "sweating or shortness of breath". "Chest symptoms" is not in the source.
Fix: sweating or shortness of breath
Basis: https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool ("marked physical symptoms such as sweating or shortness of breath")

[should-fix] [accuracy] §10 Vocabulary bullet
Current: Cognitive: not yet known; nobody has asked him what he thinks before a match.
Problem: This contradicts Deliverable A, which records Milan's words from a check-in (an *added* fact).
Fix: Cognitive: not in the case register; the profile below records what he said once his coach began the check-ins in section 9 (an added fact).
Basis: unit Deliverable A, "The thoughts" line; notes.md, case facts

[should-fix] [accuracy] §7 A controlling coaching style
Current: a controlling coach style went with more expressive suppression (hiding one's emotions), and a need-supportive style with more cognitive reappraisal;
Problem: The finding is reported selectively. The study also found that controlling coaching went with more reappraisal (β = 0.20), which the authors call "seemingly paradoxical".
Fix: a controlling coach style went with more expressive suppression (hiding one's emotions) and, which the authors call paradoxical, also with more cognitive reappraisal; a need-supportive style went with more reappraisal;
Basis: https://www.mdpi.com/2075-4663/13/9/284 (controlling → suppression β = 0.20; need-supportive → reappraisal β = 0.19; controlling → reappraisal β = 0.20, "seemingly paradoxical finding")

[should-fix] [label] §7 Emotion regulation from 16 to 25 (same omission)
Current: and a need-supportive coach with more reappraisal [weak
Problem: The summary repeats the selective reading above.
Fix: and both need-supportive and, paradoxically, controlling coach styles with more reappraisal in one study [weak
Basis: as above

[should-fix] [label] Deliverable A, Normal-or-refer result
Current: so I offer referral now, whatever the answer about spread [practice; IOC consensus; the studies behind it were not opened].
Problem: The decision rests on row 7, whose season threshold is the unit's own with no source, and on row 8. Tagging it "IOC consensus" claims a source the row 7 threshold does not have.
Fix: so I offer referral now, whatever the answer about spread [practice; row 7's duration is this unit's referral point, not a source's; row 8 follows the IOC consensus's "significant distress or impairment"; the studies behind it were not opened].
Basis: unit row 7 ("no source sets a coach's duration"); Reardon et al. 2019 Table 3 (copy cited above)

[should-fix] [label] §7 Avoidance, grade
Current: [practice; clinical consensus outside sport; the studies behind it were not opened]
Problem: The only source is the introduction of one primary study (Rosebrock et al., 2022), not a consensus statement. Calling it "clinical consensus" claims a source type that was not opened.
Fix: [practice; a model stated in the introduction of one clinical study outside sport; no study opened tests it in athletes]
Basis: https://pmc.ncbi.nlm.nih.gov/articles/PMC9378026 (introduction: avoidance "maintains the threat cognition via the prevention of the receipt of disconfirmatory evidence")

[should-fix] [accuracy] §5, Gröpel & Mesagno
Current: A systematic review of 47 choking-intervention studies with athletes (62% of them experienced athletes, mostly collegiate and club level;
Problem: Calling them all "with athletes" and the samples "mostly collegiate and club level" stretches the source. 38% of the studies were not with experienced athletes, and the source says most used "trained novices, or club or collegiate participants".
Fix: A systematic review of 47 choking-intervention studies across 15 sports (62% of them with experienced athletes; most with trained novices or club or collegiate participants, few with elite athletes;
Basis: https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134 ("A total of 47 separate studies across 15 different sports"; "Twenty-nine studies (62%) comprised experienced athletes"; "most… used trained novices, or club or collegiate participants, with fewer studies focused on elite athletes")

[minor] [label] Deliverable B, row 1, ordinary range
Current: Expected before competing: the IOC calls pre-competition state anxiety expected among elite athletes at major events (Reardon et al., 2019) [practice; IOC consensus; the studies behind it were not opened].
Problem: An elite-athlete statement is used as the ordinary range for every band from about 10 upwards, without the inference label.
Fix: Expected before competing: the IOC calls pre-competition state anxiety expected among elite athletes at major events (Reardon et al., 2019) [practice; IOC consensus; the studies behind it were not opened; for non-elite and younger athletes, the unit's inference].
Basis: Reardon et al. 2019, p. 673 ("Pre-competitive (ie, state) anxiety is to be expected among elite athletes competing at major events")

[minor] [accuracy] §7 Avoidance, Rosebrock sample
Current: the study is of a questionnaire in people with psychosis, outside sport
Problem: The sample was 198 patients with psychosis plus 1,947 non-clinical adults.
Fix: the study develops a questionnaire in patients with psychosis and non-clinical adults, outside sport
Basis: https://pmc.ncbi.nlm.nih.gov/articles/PMC9378026

[minor] [attribution] §5, Wergin et al.
Current: such as tennis or figure skating
Problem: In the continuous-choking passage the review's single-task examples are "shooting sports or jumps in gymnastics". Tennis and figure skating are named in a different section (team collapse) as racket and choreography-based sports. The attribution is acceptable but loose.
Fix: such as racket sports like tennis or choreography-based sports like figure skating (the review's examples in another section)
Basis: https://www.frontiersin.org/articles/10.3389/fpsyg.2022.930025/full

[minor] [accuracy] §6 table, 16 to 18 row
Current: answering once during a national championship
Problem: The paper names both a "national Championship" and a "Championship of Autonomic Selections", and its players were selected for regional championships.
Fix: answering once during a championship of regional selections
Basis: https://core.ac.uk/download/322669511.pdf (Gómez-López et al. 2020, procedure)

[minor] [attribution] Sources, Iniesta-Sepúlveda
Current: *Child Psychiatry & Human Development* 2021;52.
Problem: The issue can now be given. A publisher-side record lists the authors in the unit's order, with issue 1.
Fix: *Child Psychiatry & Human Development* 2021;52(1).
Basis: https://scalda.mijn.bsl.nl/the-relationship-of-family-accommodation-with-pediatric-anxiety-/17865704 (authors Iniesta-Sepúlveda, Rodríguez-Jiménez, Lebowitz, Goodman, Storch; issue 1/2021)

[minor] [attribution] Sources, Iniesta-Sepúlveda, parenthesis (companion to the fix above)
Current: the repository lists the five authors in another order and gives no issue or pages: author order, issue and pages not verified)
Fix: the repository lists the five authors in another order; author order and issue 1 confirmed on a Springer-hosted record, https://scalda.mijn.bsl.nl/the-relationship-of-family-accommodation-with-pediatric-anxiety-/17865704; pages not verified)
Basis: as above

[minor] [coverage] Deliverable B, Applied to the case, Milan
Current: are met: offer referral now, by his profile. Row 6 not yet asked.
Problem: The unit does not say that SP1's card already points the same way. By notes.md's quotation, the card refers on symptoms that "persist or spread", and Milan's have persisted for five years.
Fix: are met: offer referral now, by his profile; this agrees with his SP1 scope card, whose referral sign (symptoms that persist or spread beyond match days) is met on persistence. Row 6 not yet asked.
Basis: notes.md (SP1 card quotation); case-facts.md ("Since about 12")

[minor] [style] notes.md (not the unit)
Problem: "Milan's coach has started the two check-in questions" is implied by two *added* facts but is not in the added-facts table.
Fix: Add a row to the notes' case-facts table: "Milan's coach has started the two check-in questions (section 9) | Milan".
Basis: unit Deliverable A, "The thoughts" and "The body" lines

Length: the body is about 7,960 words by word count, above the brief's 2,000–6,000. The brief also says "do not cut to a target", and SP1 to SP3 are of similar length. No finding.

## Figures (7)

1. **range, §2.** Every label and number traces to §2: "cognitive anxiety had a small negative correlation with performance (r = −0.10)…" (−0.27, −0.06, 0.24), and "r = 0.25 (95% CI 0.19 to 0.30)". The values match Woodman & Hardy (2003, PubMed abstract) and Lochbaum et al. (2022, MDPI). The caption names the section, both sources and the correlational limit. Range fits estimates with an interval set beside point values. **PASS.**
2. **flow, §7.** "safe serve, backward pass, no grip" traces to §7 ("serves safe…passes backwards…avoids taking a grip"). "the avoidance gets the credit" traces to "the person credits the avoidance". "worry, nausea, broken sleep" is in the unit's text (§10, "Somatic: nausea, broken sleep") but not in §7. "the same worry" restates "the fear is never tested". The caption names the section and source and says the sport examples are illustrations. Flow fits a sequence; the cycle's return is implied by the last step. **PASS.**
3. **decision, Deliverable B.** The branches match rows 9 and 10, 6, 7, and 5 and 8 in the table's order. The caption names §8, Deliverable B, Reardon et al. (2019) and the ISSF SMHRT-1 page, and says the order and referral points are the unit's, graded practice. Decision fits a rule with branches. The red-flag question mentions no chest symptoms, so it is unaffected by the row 9 fix. **PASS.**

## Confirmed
- Reardon et al. 2019: "Pre-competitive (ie, state) anxiety is to be expected…"; "patterns of symptom onset, duration and severity should be used to differentiate"; GAD 6.0% clinician-confirmed and 14.6% self-report; "do not appear to differ markedly"; the duration criteria for GAD, social anxiety and panic; "number of events or activities"; "significant distress or impairment…"; fear of negative evaluation; graded exposure within psychotherapy. Read on the copy at https://www.psychiatry.wisc.edu/wp-content/uploads/2023/10/2019-Mental-health-in-elite-athletes-International-Olympic-Committee-consensus-statement-2019.pdf (publisher's page not checked).
- Woodman & Hardy 2003: 48 studies; r = −0.10 and 0.24; men −0.22 and women −0.03; high standard −0.27 and low −0.06. https://pubmed.ncbi.nlm.nih.gov/12846532/
- Craft et al. 2003: "appeared weak"; self-confidence had the strongest and most consistent relationship. https://www.sciencegate.app/document/10.1123/jsep.25.1.44
- Lochbaum et al. 2022: 41 studies, 49 samples, 3,711 athletes, 24 sports, 15 countries; r = 0.25 (0.19 to 0.30); I² = 64.49; individual 0.29 against team 0.14; male 0.35 against female 0.07; objective larger than subjective; quality not a moderator; "Most participants were adolescents and young adults"; the premise "overstated". https://mdpi.com/1660-4601/19/11/6381
- Arent & Landers 2003: 104 college-age participants; 20 to 90% of heart rate reserve; cash prize; quadratic trend, 13.2%; best at 60 and 70%; only SAS somatic anxiety added. RQES 74(4):436–444. https://sponet.de/sponet/Record/4008366 (DOI still unverified)
- Duncan et al. 2016: 18 physically active adults, mean age about 23.6; 3 and 8 mph tasks; "partial support" for the catastrophe model; no hysteresis; 16(1):27–35. https://e-space.mmu.ac.uk/620537/8/4034137.pdf and https://pureportal.coventry.ac.uk/en/publications/effects-of-increasing-and-decreasing-physiological-arousal-on-ant-2/
- Vine et al. 2016: demand and resource evaluations; one bipolar continuum; higher cardiac output and lower total peripheral resistance in challenge; no correlation between self-reports and markers in some studies; attentional control theory; explicit monitoring and reinvestment; shorter quiet eye in free throws. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01671/pdf
- Hase et al. 2019: 38 studies; "support emerged for the performance benefits of a challenge state"; the designs; variation in measures; 8(2):123–144. https://researchportal.bath.ac.uk/en/publications/the-relationship-between-challenge-and-threat-states-and-performa/
- Hase et al. 2025: 62 studies, 2017 to 2024, N = 7,418; mean ages 13.26 to 72; CTI during .16 (.03 to .29) and before .08 (.02 to .14); cognitive evaluations in low-risk-of-bias studies .18 (.12 to .24); "All mean effect sizes… small"; no moderation by age, gender or year; 65.0% low risk of bias; limited publication bias; the domains; the author list. https://www.excli.de/vol24/2024-7995/EXCLI-24-151.xml
- Hill et al. 2010: "pejorative colloquial term… sub-optimal sporting performance under stressful conditions". https://researchportal.port.ac.uk/en/publications/choking-in-sport-a-review/
- Oudejans et al. 2011: 70 expert athletes; worries often, movement execution hardly ever; fits distraction better; 24:59–73. https://research.vu.nl/en/publications/thoughts-and-attention-of-athletes-under-pressure-skill-focus-or-/
- Roberts et al. 2019: gaze studies point to distraction; dual-task studies "have often favoured self-focus"; "distraction alone or distraction in combination with self-focus"; self-paced against externally paced sports. https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1374432
- Gröpel & Mesagno 2019: 68% of studies with mean age 20 to 40; golf most common (K = 15); four in actual competition; medium quality; interventions based on both models effective. https://informahealthcare.com/doi/abs/10.1080/1750984X.2017.1408134
- Wergin et al. 2022: single-task sports fit both theories better; "continuous choking"; early underperformances evoke further negative thoughts. https://www.frontiersin.org/articles/10.3389/fpsyg.2022.930025/full
- Grossbard et al. 2009: N = 1,038 aged 9 to 14; equal fit at 9 to 11 and 12 to 14; "modestly related"; worry highest in girls and older athletes; boys reported more concentration disruption. https://researchportal.bath.ac.uk/en/publications/competitive-anxiety-in-young-athletes-differentiating-somatic-anx/
- Smith et al. 2006: five-item subscales; grade 4 readability; structure held at ages 9 to 10; 28(4):479–501. https://researchportal.bath.ac.uk/en/publications/measurement-of-multidimensional-sport-performance-anxiety-in-chil/
- Sagar et al. 2007: nine athletes aged 14 to 17, interviewed; diminished perception of self, no sense of achievement, emotional cost of failure; consistent with adult findings. https://dspace.stir.ac.uk/handle/1893/7722
- Gómez-López et al. 2020: 479 players aged 16 and 17; β = 0.37, 0.51, 0.44 and −0.22. https://core.ac.uk/download/322669511.pdf
- O'Rourke et al. 2011: youth swimmers across a season; the pressure-by-climate findings as stated in the unit. https://informahealthcare.com/doi/abs/10.1080/10413200.2011.552089
- Iniesta-Sepúlveda et al. 2021: under 19; "Positive moderate association was observed for measures administered to parents"; small for child report. https://repositorio.ucam.edu/handle/10952/7194?show=full
- Fröjdö Regborn et al. 2025: 93 athletes aged 15 to 17; Dragonskolan; 12 months; suppression worse and reappraisal better for mental health; both rose over the year; demands explanation; causality cannot be inferred (selective reporting noted in finding S3). https://www.mdpi.com/2075-4663/13/9/284
- Robazza et al. 2023: N = 424; central Italy; ages 16 to 36, mean 23.08; 71% regional; reappraisal linked to excitement and happiness; autonomy and relatedness linked to reappraisal; age could not be examined; the cross-sectional quotation. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2023.1205102/pdf
- Smoll et al. 2007 (JYD): basketball; ages 9 to 15; matched quasi-experimental design; 75- and 60-minute workshops; SAS-2 25.44 to 23.98 against 24.12 to 27.01; coach and parent contributions cannot be separated; Smith et al. (2007) listed at 29, 38–58. https://jyd.pitt.edu/ojs/jyd/article/view/358/344
- Rosebrock et al. 2022: the introduction states the safety-behaviour model; 50(3):257–268. https://pmc.ncbi.nlm.nih.gov/articles/PMC9378026
- Gouttebarge et al. 2021: SMHAT-1 for physicians and licensed or registered professionals, ages 16 and older; SMHRT-1 "developed for athletes and their entourage"; screening tools sit inside SMHAT-1. https://bjsm.bmj.com/content/early/2020/09/18/bjsports-2020-102411.abstract
- ISSF SMHRT-1 page: recognise, not diagnose; the red-flag list; "can be freely copied"; © 2025. https://issf-sports.org/issf/health/ioc-sport-mental-health-recognition-tool
- Cox et al. 2003: 17-item CSAI-2R; JSEP 25:519–533. https://coachsci.sdsu.edu:443/csa/vol125/cox.htm

Not checked: the publisher's full text of Reardon et al. 2019 (library-proxy fetch refused); the Arent & Landers DOI (no search returned it); SP1's filed card text (not in the packet).

SP4 · verdict: pass-with-fixes (fix) · error 1 · should-fix 8 · minor 8 · figures 3 PASS. No REWRITE is open; nothing blocks the next unit once these fixes are applied.
