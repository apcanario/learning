# Corrections check, C-SP1

Checker: claude-opus-5-5. Packet ck-SP1; 22 changes; live search, 17 Nov 2026. Every `current` was matched against the named file: each occurs exactly once. No change touches a figure, so step 4 does not apply (row item (a), F10, has no drafted change). Row item (e) has no drafted change: Somerville (2016) and Sawyer et al. (2018) could not be reached; Güllich et al. (2022) and Macnamara et al. (2016) are abstract-only at their publisher's pages, and the abstracts do not change any SP1 claim.

## Change 1
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
The 2022 systematic review of meta-analyses on sport psychology and performance in the course's seed list could not be opened, so this section reports none of its figures
```
Replacement:
```
The 2022 systematic review of meta-analyses on sport psychology and performance in the course's seed list (Lochbaum et al., 2022) could not be opened at its publisher's page, PubMed or DOI address, so it is not verified here; this section reports none of its figures
```
Result: PASS (a not-verified marking. Lochbaum et al. 2022 not opened: search returned only DOAJ, RePEc, repository and catalogue records, no journals.plos.org, PubMed or doi.org address; nothing rests on it. Occurs once.)
Syllabus: no conflict (F2, F11 stay open; unsure item 1 agrees)

## Change 2
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
The original replication in the course list could not be opened for this unit.
```
Replacement:
```
The replication in the course list (Ranehill et al., 2015) could not be opened at its publisher's page, PubMed or DOI address, so it is not verified here and carries no claim.
```
Result: PASS (a not-verified marking. Ranehill et al. 2015 not opened: https://www.psychologicalscience.org/journals/psychological-science/0956797614553946/ failed at its site (client error); no PubMed or doi.org address returned by search, only repository and press copies. Occurs once.)
Syllabus: no conflict (Deliverable B claim 1 row 1 and unsure item 2 agree; F11 stays open)

## Change 3
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
could not be opened for this unit, and no other source of an accepted type on their result was opened
```
Replacement:
```
could not be opened at their publishers' pages, PubMed or DOI addresses (pages refused or behind a browser check; searches returned only repository copies), so they are not verified here, and no other source of an accepted type on their result was opened
```
Result: PASS (a not-verified marking. Hagger et al. 2016 and Vohs et al. 2021 not opened: searches returned only repository, catalogue and press records, no SAGE, PubMed or doi.org address. Occurs once; the sentence reads correctly with the rest of the paragraph.)
Syllabus: no conflict (section 8 willpower and Deliverable C contested row unchanged; F11 stays open)

## Change 4
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
The two meta-analyses in the course list could not be opened.
```
Replacement:
```
Two meta-analyses on academic achievement put this in context: one, with 365,915 participants, on how far mind-sets go with achievement; one, with 57,155 participants, on mind-set interventions. The authors report: "Overall effects were weak for both meta-analyses", though some results supported the view that students of low socioeconomic status or at academic risk might benefit from the interventions ([Sisk et al., 2018, abstract read](https://doi.org/10.1177/0956797617739704)). The abstract gives no pooled effect size, so none is reported here.
```
Result: FAIL as drafted, corrected above. Opened https://www.psychologicalscience.org/journals/psychological-science/0956797617739704/ (abstract only; PubMed https://pubmed.ncbi.nlm.nih.gov/29505339/ served a reCAPTCHA page; SAGE https://journals.sagepub.com/doi/abs/10.1177/0956797617739704 failed). The abstract gives "k = 273, N = 365,915" and "k = 43, N = 57,155" without saying whether k counts studies or effect sizes, so "273 studies" and "43 studies" are not supported (the fresh check, on the full text, counted the 43 as effect sizes). The quotation "Overall effects were weak for both meta-analyses." is exact (8 words). "Some support for benefits" stretched the abstract's "might benefit"; reworded. No pooled d in the abstract: confirmed.
Syllabus: no conflict (Deliverable C weak row still rests on Yeager; growth-mindset grade [weak, positive and small, outside sport] unchanged)

## Change 5
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
The effect was real, small and conditional, on school grades, in adolescents. Nothing in it measured sport.
```
Replacement:
```
The effect was real, small and conditional, on school grades, in adolescents. Both meta-analyses concern academic achievement; nothing in them or in the experiment measured sport.
```
Result: PASS (occurs once; same abstract opened at https://www.psychologicalscience.org/journals/psychological-science/0956797617739704/: both meta-analyses are on academic achievement)
Syllabus: no conflict

## Change 6
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
- Steffen PR, Hedges D,
```
Replacement:
```
- Sisk VF, Burgoyne AP, Sun J, Butler JL, Macnamara BN. To what extent and under which circumstances are growth mind-sets important to academic achievement? Two meta-analyses. *Psychological Science* 2018;29(4):549–571. https://doi.org/10.1177/0956797617739704 (abstract read on the journal's page at the Association for Psychological Science, which shows title and abstract only; authors, year, volume and pages are from the fresh check's record and were not shown on the page opened)
- Steffen PR, Hedges D,
```
Result: PASS (occurs once; https://www.psychologicalscience.org/journals/psychological-science/0956797617739704/ opened, abstract only, shows no authors, year, volume or pages; the entry says so and where the fields come from. PubMed served a reCAPTCHA page. Placement before Steffen keeps the list order.)
Syllabus: no conflict

## Change 7
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
For coaching: do not treat 25, or any age, as the point at which an athlete becomes able to decide [practice]; SP2 deals with age and maturation.
```
Replacement:
```
For coaching: do not treat 25, or any age, as the point at which an athlete becomes able to decide [weak, against the claim]. A behavioural study pooled four datasets, two followed over time and two measured once, from 10,766 people aged 8 to 35, not described as athletes; its 23 measures of executive function, among them inhibition, working memory and planning, were found "stabilizing to adult-levels in late adolescence (18–20 years old)" ([Tervo-Clemmens et al., 2023](https://doi.org/10.1038/s41467-023-42540-8)). It measures these functions, not decisions in sport, and comes from outside sport: weak by rule 5. SP2 deals with age and maturation and grades its matching recommendation for 19- to 25-year-olds the same way.
```
Result: PASS (occurs once. Opened https://www.nature.com/articles/s41467-023-42540-8.pdf, full text to 100,000 of 117,254 characters: four datasets, Luna and NCANDA longitudinal, NKI-Rockland and PNC cross-sectional; N = 196 + 831 + 588 + 9,151 = 10,766; ages 8 to 35; 23 measures from 17 tasks targeting inhibition, attention, working memory, switching and planning; quotation "stabilizing to adult-levels in late adolescence (18–20 years old)" exact, 9 words; athletes not mentioned. Grade [weak, against the claim] by rule 5: one study outside sport, as SP2 section 4 grades its matching recommendation.)
Syllabus: no conflict (SP2 line on 19- to 25-year-olds: [weak, against the claim; one large behavioural study outside sport, rule 5]; F12 met. See New 1: Deliverable B claim 2 row 5 now contradicts it)

## Change 8
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
- Yeager DS, et al.
```
Replacement:
```
- Tervo-Clemmens B, Calabro FJ, Parr AC, Fedor J, Foran W, Luna B. A canonical trajectory of executive function maturation from adolescence to adulthood. *Nature Communications* 2023;14:6922. https://doi.org/10.1038/s41467-023-42540-8
- Yeager DS, et al.
```
Result: PASS (occurs once; authors, journal, year, volume and article number match the publisher PDF https://www.nature.com/articles/s41467-023-42540-8.pdf and SP2's entry)
Syllabus: no conflict

## Change 9
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
Three further rules. The direction goes beside the grade (weak, no benefit shown; moderate, positive). A grade from adults, students or non-athletes applied to an athlete under 18 carries the label inference. A correlational meta-analysis can earn strong for an association, never for a cause.
```
Replacement:
```
Four further rules. The direction goes beside the grade (weak, no benefit shown; moderate, positive). A grade from adults, students or non-athletes applied to an athlete under 18 carries the label inference. A correlational meta-analysis can earn strong for an association, never for a cause. A consensus or position statement is graded by rule 2 when the agreement is itself the evidence: the experts agreed on the claim and no study tests it. The IOC's division between recognising and referring, and assessing (section 2), is practice: it came from a consensus process, and no study opened for this unit tests it against any other division. When the statement says its recommendation rests on studies that test the claim, and says what those studies were, the grade comes from those studies by rules 3 to 5: SP2's sleep hours by age come from consensus statements built on studies outside sport, so they are weak by rule 5. Where those studies could not be opened, the grade stays practice, with the note "the studies behind it were not opened", as SP2 and SP3 grade such statements.
```
Result: FAIL as drafted, corrected above. No outside source; checked against SP2: its sleep hours are graded [weak, positive, for the hours by age (consensus built on studies outside sport, rule 5 ...)], and they include the IOC adolescent range, which is not a sleep-medicine statement, so "sleep-medicine" is dropped. The drafted rule says nothing of the case F14 names (a statement whose studies could not be opened); read literally it would regrade SP2's [practice; ISSP] entries (the ISSP stand names its review, Park et al. 2013, per F20) and SP3's [practice; IOC consensus; the studies behind it were not opened]. The added last sentence states the interim grading F14 sets, so the new rule agrees with SP2 and SP3. Occurs once.
Syllabus: conflict as drafted: with F14 and with SP2's and SP3's [practice] grades for statements whose studies were not opened; the corrected text removes it. If the chat holds that any wording on F14's case belongs to syllabus review S-SP1, drop the last sentence and leave F14 open there. Row (d)'s condition holds: no preamble or brief change.

## Change 10
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
**Inference**: added whenever the grade comes from adults, students or non-athletes and is applied to an athlete under 18.
```
Replacement:
```
**Inference**: added whenever the grade comes from adults, students or non-athletes and is applied to an athlete under 18. A consensus or position statement is practice when the agreement is the evidence (the IOC division in the practice row), and is graded from its studies by rules 3 to 5 when it says which studies test the claim (SP2's sleep hours: weak, outside sport); section 9 gives the rule.
```
Result: PASS (occurs once; no outside source; agrees with C9 as corrected and with SP2's sleep grade)
Syllabus: no conflict, provided C9 is applied as corrected (the key points to section 9 for the full rule)

## Change 11
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
**"Harsh coaching builds toughness."** No peer-reviewed source found that shows it does. In the one study opened (section 2), athletes who reported a more controlling coach reported lower need satisfaction, associated in turn with fear of failure (cross-sectional; [Hu et al., 2023](https://doi.org/10.3389/fpsyg.2023.1106916)) [weak, against the claim]. The reviews on controlling coaching in the course list could not be opened; SP3 and DD-SP1 must open them.
```
Replacement:
```
**"Harsh coaching builds toughness."** No peer-reviewed source found that shows it does. Three surveys, each measured at one time, point the other way. In the first (section 2), athletes who reported a more controlling coach reported lower need satisfaction, associated in turn with fear of failure ([Hu et al., 2023](https://doi.org/10.3389/fpsyg.2023.1106916)). In 103 male footballers aged 12 to 17, a more controlling coaching style went with more thwarting of their psychological needs, and that thwarting with burnout ([Morales-Sánchez et al., 2020](https://doi.org/10.3390/ijerph17134909)). In 479 handball players aged 16 and 17 on regional teams, a coach-created climate centred on comparison with others went with more fear of failure, and through it with more anxiety and lower self-confidence before competition; this study measured the climate, not controlling behaviour ([Gómez-López et al., 2020](https://doi.org/10.3390/ijerph17020592)). Each is a correlation: none can show cause. A practitioner article on developing resilience, which reports no test of its own, notes that environments of extreme challenge with no support have been created in the name of toughening performers up, and distinguishes its approach from "the unethical and inappropriate imposition of adversity" ([Fletcher & Sarkar, 2016, abstract and notes read](https://doi.org/10.1080/21520704.2016.1255496)). Grade: [weak, against the claim] (rule 5: correlational studies, no controlled test). The reviews by Bartholomew et al. (2009, 2011) in the course list could not be opened; DD-SP1 must open them.
```
Result: FAIL as drafted, corrected above (two wordings). Opened https://mdpi.com/1660-4601/17/13/4909 (Morales-Sánchez et al. 2020, full text: 103 male players aged 12 to 17, one club, one questionnaire session, controlling style to need thwarting beta 0.53, thwarting to burnout 0.66): holds. Opened https://mdpi.com/1660-4601/17/2/592 (Gómez-López et al. 2020, full text: 479 players, 250 boys and 229 girls, aged 16 and 17, regional championship teams, ego climate to fear of failure 0.37, fear of failure to somatic 0.44 and cognitive anxiety 0.51 and self-confidence -0.22 (CI excludes zero), CSAI-2R answered for "just before the competition"; climate measured, not controlling behaviour): holds, but the paper defines the ego climate by social comparison and attention to the stars, so "centred on beating others" becomes "centred on comparison with others". Opened https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496 (abstract, acknowledgments and notes 1 to 7 only): quotation "the unethical and inappropriate imposition of adversity" exact (7 words); the note says such environments "have been created under the guise of" toughening up, so "have been used to toughen performers up" becomes "have been created in the name of toughening performers up". No test reported: confirmed. Occurs once.
Syllabus: no conflict with SP3 section 10 (same three surveys, same grade, same rule) or F27/F31 (Bartholomew left to DD-SP1). See New 2 and New 3: Deliverable B claim 3 still says one study

## Change 12
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
- Gouttebarge V, Bindra A,
```
Replacement:
```
- Fletcher D, Sarkar M. Mental fortitude training: An evidence-based approach to developing psychological resilience for sustained success. *Journal of Sport Psychology in Action* 2016;7(3):135–157. https://doi.org/10.1080/21520704.2016.1255496 (abstract and notes read; the page opened shows no authors, title, volume or pages: they are given as SP3 gives them, from the course's seed list)
- Gómez-López M, Chicau Borrego C, Marques da Silva C, Granero-Gallegos A, González-Hernández J. Effects of motivational climate on fear of failure and anxiety in teen handball players. *International Journal of Environmental Research and Public Health* 2020;17(2):592. https://doi.org/10.3390/ijerph17020592
- Gouttebarge V, Bindra A,
```
Result: FAIL as drafted, corrected above. https://informahealthcare.com/doi/full/10.1080/21520704.2016.1255496 shows no title, journal, year or author names at all, so the drafted entry implied the surnames and title were on the page. Corrected to SP3's entry, with the fields' origin stated. Gómez-López entry checked against https://mdpi.com/1660-4601/17/2/592: authors match. Occurs once.
Syllabus: no conflict once corrected (drafted entry differed from SP3's Sources entry for the same paper)

## Change 13
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
- Mustile M, Kourtis D,
```
Replacement:
```
- Morales-Sánchez V, Crespillo-Jurado M, Jiménez-López D, Morillo-Baro JP, Hernández-Mendo A, Reigal RE. Relationships between controlling interpersonal coaching style, basic psychological need thwarting, and burnout, in adolescent soccer players. *International Journal of Environmental Research and Public Health* 2020;17(13):4909. https://doi.org/10.3390/ijerph17134909
- Mustile M, Kourtis D,
```
Result: PASS (occurs once; authors, volume 17, issue 13, article 4909 match https://mdpi.com/1660-4601/17/13/4909)
Syllabus: no conflict (matches SP3's entry)

## Change 14
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
A systematic review of mental toughness and individual differences (the abstract does not give the number of studies or their populations) reports that about 50% of the variation in mental toughness can be accounted for by genetic factors, and associations with positive traits, coping and outcomes in education and mental health; it mentions possible interventions and reports no tests of them in its abstract ([Lin et al., 2017, abstract read](https://doi.org/10.3389/fpsyg.2017.01345)). For a programme that installs it: no peer-reviewed source found.
```
Replacement:
```
A systematic review of mental toughness and individual differences (51 papers describing 56 studies, in school pupils, students, employees, military candidates and athletes) reports, from four twin studies, that "Approximately 50% of the variation in MT can be accounted for by genetic factors", and associations with positive traits, coping and outcomes in education and mental health. On developing it, the review reports two psychological skills training programmes in athletes that raised later mental toughness ratings, without saying whether they had control groups, and concludes that there is, at present, a lack of empirical support for the importance of such interventions, and that the suggestion that they would boost performance remains speculative ([Lin et al., 2017](https://doi.org/10.3389/fpsyg.2017.01345)). Neither programme study was opened for this unit. For a programme that installs it as a trait: no peer-reviewed source found.
```
Result: FAIL as drafted, corrected above. Opened https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01345/pdf (full text): "Fifty-one papers (describing 56 studies) were included"; four behavioural-genetics studies, all twin designs; abstract quotation "Approximately 50% of the variation in MT can be accounted for by genetic factors" exact (14 words); Gucciardi et al. 2009a,b, two PST programmes in athletes, "Both interventions worked to increase subsequent ratings of MT", control groups not stated. The review's conclusion is "a lack of empirical support for the importance of interventions to increase MT" and that suggestions on interventions boosting performance "remain speculative": the drafted "interventions ... lack empirical support so far" turned a claim about their importance into one about their effect, and contradicted the sentence before it. "Military recruits" corrected to "military candidates", the review's word. Occurs once.
Syllabus: no conflict

## Change 15
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
https://doi.org/10.3389/fpsyg.2017.01345 (abstract read)
```
Replacement:
```
https://doi.org/10.3389/fpsyg.2017.01345
```
Result: PASS (occurs once; full text opened as for C14)
Syllabus: no conflict

## Change 16
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
([Steffen et al., 2022, abstract read](https://doi.org/10.3389/fpsyt.2022.802606))
```
Replacement:
```
([Steffen et al., 2022](https://doi.org/10.3389/fpsyt.2022.802606))
```
Result: PASS (occurs once. Opened https://frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.802606/full, full text to 100,000 of 128,341 characters: review article; triune model "does not accurately explain how the brain functions in everyday life"; emotion and cognition "interdependent"; no purely emotional or purely cognitive circuits; "amygdala hijack" and "hijack" absent)
Syllabus: no conflict

## Change 17
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
https://doi.org/10.3389/fpsyt.2022.802606 (abstract read)
```
Replacement:
```
https://doi.org/10.3389/fpsyt.2022.802606
```
Result: PASS (occurs once; as C16)
Syllabus: no conflict

## Change 18
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
([Sturt et al., 2012, abstract read](https://doi.org/10.3399/bjgp12X658287))
```
Replacement:
```
([Sturt et al., 2012](https://doi.org/10.3399/bjgp12X658287))
```
Result: PASS (occurs once. Opened https://bjgp.org/content/62/604/e757, full text: 10 experimental studies, 5 RCTs with samples 22 to 106, conditions anxiety, weight, morning sickness, substance misuse, MRI claustrophobia; no sport outcome; quotation "There is little evidence that NLP interventions improve health-related outcomes" exact; "limited quantity and quality of NLP research" supports the unit's "few and weak studies")
Syllabus: no conflict

## Change 19
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
https://doi.org/10.3399/bjgp12X658287 (abstract read)
```
Replacement:
```
https://doi.org/10.3399/bjgp12X658287
```
Result: PASS (occurs once; as C18)
Syllabus: no conflict

## Change 20
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
([Güllich & Barth, 2024, abstract and parts of the full text read](https://doi.org/10.1007/s40279-023-01957-3))
```
Replacement:
```
([Güllich & Barth, 2024](https://doi.org/10.1007/s40279-023-01957-3))
```
Result: PASS (occurs once. Opened https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf, full text: k = 51, N = 6,233, 82% male, 2009 to 2022; junior d = -0.53 (-0.74 to -0.32, k = 16), senior d = 0.56 (0.40 to 0.72, k = 34); no significant moderation by individual or team sport, level or programme type; primary studies high quality (MMAT); no disagreeing review mentioned; quotation "effects on short-term junior performance versus long-term senior performance are opposite" exact, 10 words. Strong for the association by rule 3 holds.)
Syllabus: no conflict (SP2 uses the same figures and grade)

## Change 21
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
([Mustile et al., 2024, abstract and methods read](https://doi.org/10.3389/fnhum.2024.1412307))
```
Replacement:
```
([Mustile et al., 2024](https://doi.org/10.3389/fnhum.2024.1412307))
```
Result: PASS (occurs once. Opened https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2024.1412307/pdf, full text: 24 recruited, 21 analysed, 18 to 44, athletic status not reported; overlap of beta and alpha changes; "motor imagery requires additional cortical resources")
Syllabus: no conflict

## Change 22
File: hub.py
Current:
```
Known gaps. (1) References named in the unit or in the writer's notes that the writer did not open, and on which no claim rests: the Delphi study on the coach's role in athlete mental health (Bissett et al., 2020); the 2022 review of sport psychology meta-analyses (Lochbaum et al., 2022), so the unit says nothing on how far psychological variables relate to performance; the original power-posing study and its replication (Ranehill et al., 2015); the two ego-depletion replications (Hagger et al., 2016; Vohs et al., 2021); the grit meta-analysis (Credé et al., 2017); the growth-mindset meta-analyses (Sisk et al., 2018); the reviews on controlling coaching (Bartholomew et al., 2009 and 2011; Fletcher and Sarkar, 2016); Wegner's papers on ironic effects (1994, 1998) and Woodman et al. (2015); Somerville (2016) and Güllich et al. (2022). (2) Claims read from an abstract or summary only: the IOC mental health tools (Gouttebarge et al., 2021), the intervention meta-analysis of Brown and Fletcher (2017), the deliberate-practice meta-analysis (Macnamara et al., 2016), the mental toughness review (Lin et al., 2017), the triune-brain review (Steffen et al., 2022) and the neuro-linguistic programming review (Sturt et al., 2012); the facial-expression review (Barrett et al., 2019) from the publisher's summary page only; the early-specialisation meta-analysis (Güllich and Barth, 2024) from its abstract and parts of the full text; the imagery EEG study (Mustile et al., 2024) from its abstract and methods. (3) 15 fixes from the check are held, because each needed a reference that could not be opened at its publisher's page, an index or a DOI address in the fixing session (search returned only repository copies or press releases, a redirect that may not be followed, or a blocked page), and no fix may rest on a source that was not opened: six on ego depletion (Hagger et al., 2016; Vohs et al., 2021), six on the power-posing replication (Ranehill et al., 2015), two on the size of growth-mindset effects (Sisk et al., 2018) and one on psychological variables and performance (Lochbaum et al., 2022). They will be applied when those references are opened at their publishers' pages. (4) Ego depletion carries no grade: no source of an accepted type on the replications was opened, so the grade key's contested row has no worked example. (5) The unit runs to about 7,000 words before its Sources, over the brief's length guide; it is kept at that length because the topic needs it: the scope line, the grades and the claim checks are what every later unit builds on.
```
Replacement:
```
Known gaps. (1) References named in the unit or its notes that were not opened, on which no claim rests: the Delphi study on the coach's role in athlete mental health (Bissett et al., 2020); the 2022 review of sport psychology meta-analyses (Lochbaum et al., 2022), so the unit says nothing on how far psychological variables relate to performance; the power-posing replication (Ranehill et al., 2015); the two ego-depletion replications (Hagger et al., 2016; Vohs et al., 2021); the grit meta-analysis (Credé et al., 2017); the reviews on controlling coaching (Bartholomew et al., 2009 and 2011); Wegner's papers on ironic effects (1994, 1998) and Woodman et al. (2015); the two studies of training programmes that the mental toughness review reports; Somerville (2016) and Sawyer et al. (2018); and the multi-sport practice meta-analysis (Güllich et al., 2022), reachable at its publisher's page in abstract only, which SP2 cites. Lochbaum, Ranehill, Hagger, Vohs, Somerville and Sawyer were sought again at their publishers' pages, PubMed and DOI addresses in the corrections pass of 17 Nov 2026 and could not be opened there (refused, redirected or behind a browser check); they stay open for the next corrections pass. (2) Claims read from an abstract or summary only: the IOC mental health tools (Gouttebarge et al., 2021), the intervention meta-analysis of Brown and Fletcher (2017), the deliberate-practice meta-analysis (Macnamara et al., 2016) and the growth-mindset meta-analyses (Sisk et al., 2018), each sought in full and reachable only in abstract; the practitioner article on challenge and support (Fletcher and Sarkar, 2016), abstract and notes only; the facial-expression review (Barrett et al., 2019), from the publisher's summary page only. Read in full in the corrections pass: the mental toughness review (Lin et al., 2017), which corrected the unit's entry, and the triune-brain review (Steffen et al., 2022), the neuro-linguistic programming review (Sturt et al., 2012), the early-specialisation meta-analysis (Güllich and Barth, 2024) and the imagery EEG study (Mustile et al., 2024), which confirmed it. (3) 13 of the 15 fixes held from the fresh check are still held, because each needs a reference that could not be opened at its publisher's page, PubMed or a DOI address: six on ego depletion (Hagger et al., 2016; Vohs et al., 2021), six on the power-posing replication (Ranehill et al., 2015) and one on psychological variables and performance (Lochbaum et al., 2022). The two on growth-mindset effects were applied from the abstract of Sisk et al. (2018) on its publisher's page; it gives no pooled effect size, so the unit gives none. (4) Ego depletion carries no grade, and the grade key's contested row has no worked example, until the replications are opened. (5) The unit runs to about 7,000 words before its Sources, over the brief's length guide; it is kept at that length because the topic needs it: the scope line, the grades and the claim checks are what every later unit builds on.
```
Result: FAIL as drafted, corrected above. Item (1) said Güllich et al. (2022) could not be opened at its publisher's page; https://www.psychologicalscience.org/journals/perspectives/1745691620974772/ serves its abstract (full text not shown), as SP2 read it. Corrected so it is listed as abstract-only and dropped from the could-not-be-opened list. Checked: Macnamara et al. 2016 https://www.psychologicalscience.org/journals/perspectives/1745691616635591/ abstract only; Brown & Fletcher 2017 https://www.springermedizin.de/effects-of-psychological-and-psychosocial-interventions-on-sport/12118340 abstract only (login wall), figures confirmed; Somerville (2016), Sawyer et al. (2018) and Gouttebarge et al. (2021): searches returned no publisher, PubMed or doi.org address with full text. Items (2) to (5) agree with C1 to C21 and with C4, C11, C12, C14 as corrected; the corrected unit runs to about 7,210 words before Sources, so "about 7,000" holds. No double quotes; fits the double-quoted Python string; occurs once in hub.py.
Syllabus: no conflict

## New 1
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
| 5. Has it held up? | One very large study; this unit opened no other. |
```
Replacement:
```
| 5. Has it held up? | One very large study of brain measures. A behavioural study of executive function in 10,766 people aged 8 to 35, not athletes, found it at adult levels by 18 to 20 (section 8; [Tervo-Clemmens et al., 2023](https://doi.org/10.1038/s41467-023-42540-8)). |
```
Result: PASS (Deliverable B, claim 2: after C7 the unit opens a second study on this claim, so "this unit opened no other" is false. Source as C7 (https://www.nature.com/articles/s41467-023-42540-8.pdf).)
Syllabus: no conflict (agrees with SP2 section 4)

## New 2
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
| 5. Has it held up? | One survey; this unit opened no replication. |
```
Replacement:
```
| 5. Has it held up? | Two more surveys, each measured at one time, point the same way: a controlling style with need thwarting and burnout in footballers aged 12 to 17, and an ego-involving climate with fear of failure in handball players aged 16 and 17 (section 8). No controlled test was opened. |
```
Result: PASS (Deliverable B, claim 3: after C11, section 8 rests the entry on three surveys; the worked sheet still says one. Sources as C11 (https://mdpi.com/1660-4601/17/13/4909; https://mdpi.com/1660-4601/17/2/592).)
Syllabus: no conflict (SP3 section 10: "now rests on three surveys instead of one")

## New 3
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
| **Grade** | **Weak** (rule 5: one study), and its direction is against the claim. For the claim that harshness builds toughness: no peer-reviewed source found. |
```
Replacement:
```
| **Grade** | **Weak** (rule 5: three correlational studies, no controlled test), and its direction is against the claim. For the claim that harshness builds toughness: no peer-reviewed source found. |
```
Result: PASS (Deliverable B, claim 3: same cause as New 2; the grade basis must match section 8 and SP3.)
Syllabus: no conflict

## New 4
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
4. Section 7, grit and growth mindset: Credé et al. (2017) and Sisk et al. (2018) were not opened; the unit uses a 2025 grit review in adults (physical activity) and Yeager et al. (2019) instead.
```
Replacement:
```
4. Section 7, grit and growth mindset: Credé et al. (2017) was not opened; Sisk et al. (2018) was read in abstract on its publisher's page, which gives no pooled effect size, so the unit gives none; the unit uses a 2025 grit review in adults (physical activity) and Yeager et al. (2019) for the experiment.
```
Result: PASS (Unsure list item 4 is stale after C4 to C6. Source as C4 (https://www.psychologicalscience.org/journals/psychological-science/0956797617739704/).)
Syllabus: no conflict

## New 5
File: hub.py
Current:
```
33 findings were applied and 15 held
```
Replacement:
```
33 findings were applied and 15 held (two of the 15 were applied in the corrections pass of 17 Nov 2026; see Known gaps, item 3)
```
Result: PASS (Reading-page intro, in the same string as C22: the count is historical and would read as current beside C22's item (3). No outside source. Occurs once in hub.py; no double quotes.)
Syllabus: no conflict

**Summary:** 22 changes: 16 PASS (C1 to C3 as not-verified markings), 6 FAIL as drafted with corrected text given (C4, C9, C11, C12, C14, C22); 1 syllabus conflict as drafted (C9, removed by the correction); 5 new problems (New 1 to New 5), each with a replacement.
