# Corrections check, C-SP3 (claude-opus-5-5)

Checked 17 Nov 2026. Every `current` was counted in the packet file named: each occurs exactly once.

## Change 1
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
```viz
{"kind": "range", "caption": "Perceived autonomy support and four kinds of motivation: pooled correlations (ρ) from 131 samples, 38,844 participants in sport and exercise. From section 1 of this unit: Mossman et al. (2024), International Review of Sport and Exercise Psychology, abstract. Correlational; ages not given in the abstract.", "unit": "", "min": -0.3, "max": 0.5, "ticks": [-0.2, 0, 0.2, 0.4], "decimals": 2, "rows": [{"label": "Autonomous motivation", "low": 0.39, "high": 0.39, "point": 0.39, "tone": 2}, {"label": "Introjected regulation", "low": 0.16, "high": 0.16, "point": 0.16, "tone": 3}, {"label": "External regulation", "low": -0.01, "high": -0.01, "point": -0.01, "tone": 4}, {"label": "Amotivation", "low": -0.19, "high": -0.19, "point": -0.19, "tone": 1}]}
```
```
Replacement:
```
```viz
{"kind": "line", "caption": "Perceived autonomy support and four kinds of motivation: pooled correlations (ρ) from 131 samples, 38,844 participants in sport and exercise, in the order section 1 gives them, from autonomous motivation to amotivation; the line joins four separate estimates and shows no change over time. From section 1 of this unit: Mossman et al. (2024), International Review of Sport and Exercise Psychology, abstract. Correlational; ages not given in the abstract.", "x": ["Autonomous motivation", "Introjected regulation", "External regulation", "Amotivation"], "unit": "", "decimals": 2, "min": -0.3, "max": 0.5, "yticks": [-0.2, 0, 0.2, 0.4], "ylabel": "ρ", "series": [{"values": [0.39, 0.16, -0.01, -0.19], "tone": 2}]}
```
```
Result: PASS. Viz: the JSON parses; check_keys finds no undocumented key; viz.render (packet viz.py, theme.css stubbed in memory, nothing written) draws a wide SVG 700x311 and a phone SVG (svg.viz-alt) 258x350; all four points and their value labels (0.39, 0.16, -0.01, -0.19) are in the phone drawing's opening frame; the y axis runs -0.3 to 0.5 with ticks -0.20 to 0.40. Every number matches section 1 (ρ = .39, .16, −.01, −.19; 131 samples, 38,844 participants), and the order of the x labels is section 1's. Source opened: https://informahealthcare.com/doi/abs/10.1080/1750984X.2022.2031252 (publisher's abstract: 1,320 correlations, 131 samples, 38,844 participants; .39, .16, −.01, −.19; no moderation by culture or sport). PHONE LABELS BREAK INSIDE WORDS, plainly: on the phone drawing every one of the four x labels breaks mid-word, rendered as 'Autono / mous / motiva / tion', 'Introj / ected / regula / tion', 'Extern / al / regula / tion', 'Amotiv / ation'. The wide drawing keeps whole labels. This is a renderer limit of the line kind (labels wrapped at the column width, about 40 units at 258); shorter labels would still break ('Autonomous' is ten characters). The fresh agent's re-check on the page shots that F40 requires must judge this; it is not a reason to drop the figure.
Syllabus: no conflict. F40 is met in kind (another kind that shows all four points in the phone's opening frame); its 'fresh agent's re-check on the page shots' is still owed and must see the mid-word label breaks. No other unit relies on the figure.

## Change 2
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
One widely used questionnaire for young athletes asks them to rate items such as
```
Replacement:
```
One questionnaire, the Perceived Motivational Climate in Sport Questionnaire (PMCSQ-2), used in a study of teen handball players, asks athletes to rate items such as
```
Result: PASS. Opened https://mdpi.com/1660-4601/17/2/592 (MDPI, publisher): instrument is the Perceived Motivational Climate in Sport Questionnaire (PMCSQ-2), Spanish version, 29 items; the items read 'On this team, the coach emphasizes always trying to do your best' and 'On this team, the coach gives most of his or her attention to the stars.'; the unit's two quotations are exact substrings, each under 15 words. The page does not call the questionnaire widely used, so cutting 'widely used' is right.
Syllabus: no conflict. Section 5 ('The questionnaire item quoted in section 1') still points to it; S9 and C7 of the self-audit cite Gómez-López for the item, unchanged.

## Change 3
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
479 handball players aged 16 and 17 selected for regional championships in Spain (250 boys, 229 girls) answered once during a championship.
```
Replacement:
```
479 handball players aged 16 and 17 (250 boys, 229 girls), selected for their regions' teams in Spanish championships, answered once, during the championship.
```
Result: PASS. Opened https://mdpi.com/1660-4601/17/2/592: 479 players, 250 boys and 229 girls, aged 16 (40.1%) and 17 (59.9%); players 'selected to compete in the Spanish Regional Championships' and who 'belong to the regional handball team'; data collected 'during the Championship of Autonomic Selections' at the teams' hotels, one collection. The replacement reads the source correctly. Note: the original wording echoed the page's own English ('Spanish Regional Championships'), so it was loose rather than false; the replacement is the clearer reading. The page also calls it 'the national Championship' in the procedure; 'Spanish championships' covers both. β = 0.37, r = −0.31, task direct path β = −0.09 n.s. confirmed.
Syllabus: no conflict. Section 2's table, section 10 and section 11 ('ages 16 to 17') unchanged.

## Change 4
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
found reasons including other interests, not being as good as wanted, lack of fun, pressure from parents, peers or coaches, and conflict with the coach; the authors conclude that most of the reasons are controllable
```
Replacement:
```
found reasons including other things to do, failure to improve competence, lack of enjoyment, boredom, pressure from parents, coaches or others, and conflict with the coach; the authors conclude that the main reasons are "controllable by the athletes"
```
Result: PASS. Opened https://mdpi.com/2075-4663/5/3/50 (MDPI, publisher): six studies, ages 5 to 30, Canada 4, USA 1, Spain 1; reasons 'conflicts with their trainers', 'other things to do', 'competence improvements' failure', 'parents, couples or trainers' pressure', 'lack of enjoyment', 'get bored'; Conclusions: the main reasons leading to dropout in swimming are 'controllable by the athletes' (quotation exact, 4 words). Text total 727 against a table summing to about 955, as the unit already says. Rendering 'couples' as 'others' is a defensible non-commitment.
Syllabus: no conflict. No brief or flag relies on the list; F41 asked for it.

## Change 5
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
The IOC consensus statement asks coaches to focus on "each athlete's personal assets and mastery orientation" ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Replacement:
```
The IOC consensus statement asks coaches to focus on "each athlete's personal assets and mastery orientation" ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Result: FAIL. The premise is wrong: the publisher's page opens. Opened https://bjsm.bmj.com/content/49/13/843.full (bjsm.bmj.com, the publisher; full article text shown). Section 5's phrase is in the 'Coaching' recommendation: 'Provide a challenging and enjoyable sporting climate that focuses on each athlete's personal assets and mastery orientation.' The quotation is word for word, so no 'not verified' marking is warranted; withdraw the change and leave the text as it stands (the Replacement below is the current text, unchanged). PubMed (https://www.pubmed.gov/26084524/) redirected and was not checked.
Syllabus: no conflict with the withdrawal. Applying the change would conflict with F41 (which allows marking only what cannot be checked) and with section 5's steps, which SP7 takes ('the autonomy-supportive and controlling behaviours SP7 decides by').

## Change 6
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
The IOC statement asks for "a challenging and enjoyable sporting climate" ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Replacement:
```
The IOC statement asks for "a challenging and enjoyable sporting climate" ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Result: FAIL. The premise is wrong: the publisher's page opens. Opened https://bjsm.bmj.com/content/49/13/843.full (bjsm.bmj.com, the publisher; full article text shown). Section 7's phrase is in the same 'Coaching' recommendation: 'Provide a challenging and enjoyable sporting climate that focuses...'. The quotation is word for word, so no 'not verified' marking is warranted; withdraw the change and leave the text as it stands (the Replacement below is the current text, unchanged). PubMed (https://www.pubmed.gov/26084524/) redirected and was not checked.
Syllabus: no conflict with the withdrawal.

## Change 7
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
The IOC consensus statement on youth athletic development describes athlete burnout
```
Replacement:
```
The IOC consensus statement on youth athletic development describes athlete burnout
```
Result: FAIL. The premise is wrong: the publisher's page opens. Opened https://bjsm.bmj.com/content/49/13/843.full (bjsm.bmj.com, the publisher; full article text shown). Section 8's five phrases are on the page word for word: 'a recognised part of competitive youth sport' (burnout and subsequent drop-out), 'psychological overload (self or coach/parent induced)' (after 'inappropriate and unrealistic demands and expectations'), 'overuse injury, overtraining and burnout', 'systems that promote over-training' (safeguarding section), 'autonomy-supportive, mastery-oriented sporting climates' and 'in less stress and more intrinsic motivation'. The unit's paraphrases around them hold. The quotation is word for word, so no 'not verified' marking is warranted; withdraw the change and leave the text as it stands (the Replacement below is the current text, unchanged). PubMed (https://www.pubmed.gov/26084524/) redirected and was not checked.
Syllabus: no conflict with the withdrawal. Section 8's IOC lines feed SP9 (F32); marking them unverified would have weakened what SP9 takes.

## Change 8
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
that result "in less stress and more intrinsic motivation" ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Replacement:
```
that result "in less stress and more intrinsic motivation" ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Result: FAIL. The premise is wrong: the publisher's page opens. Opened https://bjsm.bmj.com/content/49/13/843.full (bjsm.bmj.com, the publisher; full article text shown). 'that result in less stress and more intrinsic motivation' is on the page word for word. The quotation is word for word, so no 'not verified' marking is warranted; withdraw the change and leave the text as it stands (the Replacement below is the current text, unchanged). PubMed (https://www.pubmed.gov/26084524/) redirected and was not checked.
Syllabus: no conflict with the withdrawal.

## Change 9
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
while noting that putting such advice into practice is hard ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Replacement:
```
while noting that putting such advice into practice is hard ([Bergeron et al., 2015, consensus](https://doi.org/10.1136/bjsports-2015-094962)).
```
Result: FAIL. The premise is wrong: the publisher's page opens. Opened https://bjsm.bmj.com/content/49/13/843.full (bjsm.bmj.com, the publisher; full article text shown). Section 9's phrases are on the page word for word: 'maladaptive perfectionistic tendencies, prompted by elevated parental expectations and criticism' and 'parents reportedly welcome advice on how to become a better sporting parent', followed by 'although implementation is a challenge', which the unit's 'putting such advice into practice is hard' paraphrases fairly. The appended sentence 'These two quotations are the writer's and are not verified.' is also withdrawn. The quotation is word for word, so no 'not verified' marking is warranted; withdraw the change and leave the text as it stands (the Replacement below is the current text, unchanged). PubMed (https://www.pubmed.gov/26084524/) redirected and was not checked.
Syllabus: no conflict with the withdrawal. SP8 and SP10 extend the parents' page (SP3 brief 'Gives'; F37), which section 9 grounds.

## Change 10
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
(consensus; full text read; authors, title, volume and pages from the course's seed list, as the page showed initials only)
```
Replacement:
```
(consensus; full text read by the writer; the fresh check could not open it; the corrections check opened the full text at its publisher's page, https://bjsm.bmj.com/content/49/13/843.full, on 17 Nov 2026 and found the quotations in sections 5, 7, 8 and 9 word for word; authors, title, volume and pages from the course's seed list, as the page showed initials only and no journal details)
```
Result: FAIL. The status it records is wrong: opened https://bjsm.bmj.com/content/49/13/843.full (publisher; full text; contributor initials only, no journal name, volume or pages shown), and every IOC quotation in sections 5, 7, 8 and 9 is there word for word. The drafter's clause on the Amsterdam UMC record rests on a page this check did not open and is left out. Corrected replacement below records the verification.
Syllabus: no conflict. Unsure list item 2 must change with it (New 1).

## Change 11
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
and their behaviour was observed with a validated observational system at three points in the season.
```
Replacement:
```
and their behaviour was filmed and coded with a validated observation system, the Multidimensional Motivational Climate Observation System (MMCOS), at three points in the season.
```
Result: PASS. Opened https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full (Frontiers, publisher; final version, full text): the observation system is the 'Multidimensional Motivational Climate Observation System' (MMCOS), cited as Smith et al., 2015; coaches were filmed at three points (T1 first 4 weeks, T2 about 1 month after the workshop, T3 4 to 6 weeks before the season's end). The MMCOS paper itself is not cited, only named as the trial names it; correct.
Syllabus: no conflict. F39 asks for MMCOS to be cited once opened; it is named, not cited, consistently with C12.

## Change 12
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
it is not a validated instrument, and its counts are for your own comparison over time;
```
Replacement:
```
it is not a validated instrument (the football trial in section 3 used one, the MMCOS; its development paper, Smith et al., 2015, could not be opened at its publisher's page, PubMed or a DOI address, so the twenty behaviours have not been checked against it), and its counts are for your own comparison over time;
```
Result: PASS (a 'not opened' marking that carries no claim from the unopened paper). Opened https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full: names MMCOS and gives the reference Smith N, Tessier D, Tzioumakis Y, Quested E, Appleton P, Sarrazin P, et al. (2015) J Sport Exerc Psychol 37:4-22, doi 10.1123/jsep.2014-0059. Smith et al. (2015) not opened by this check either: searches returned only institutional records (Curtin, Birmingham, UPC, Thessaly), a thesis and aggregators; no Human Kinetics page, PubMed record or DOI address.
Syllabus: no conflict. F39 stays open (the MMCOS paper not opened); SP7 (F39's other target) unaffected.

## Change 13
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
([Tzioumakis et al., 2026, abstract of the provisionally accepted version read](https://doi.org/10.3389/fpsyg.2026.1563931)). The abstract read gives no effect sizes and reports no athlete outcomes; the final version (August 2026) gives the players' ages as 10 to 15.
```
Replacement:
```
([Tzioumakis et al., 2026, full text of the final version read](https://doi.org/10.3389/fpsyg.2026.1563931)). The workshop lasted about six hours; the players were aged 10 to 15. The paper reports no standardised effect sizes and measured no athlete outcomes; the authors call the gains in support "short-term, but not sustained".
```
Result: PASS. Opened https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full: 68 coaches (England 17, France 11, Spain 18, Greece 22), randomly assigned, 36/32; workshop 'approximately 6-h'; 'athletes aged 10 to 15 years'; disempowering b = −0.26 and ego-involving b = −0.21 declined; autonomy (b = 1.38) and relatedness support (b = 1.06) rose T1 to T2 then fell; Discussion: the programme 'produced short-term, but not sustained' improvements in the empowering dimensions (quotation exact, 4 words); only R² reported, no standardised effect sizes; no athlete outcomes (named as future work). Also opened https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1563931/full: provisionally accepted (received 20 Jan 2025, accepted 21 Nov 2025); abstract names no instrument, no player ages, no effect sizes, no athlete outcomes.
Syllabus: no conflict. Section 3's closing paragraph (about six hours; faded within the season) and the self-audit's 'gain in autonomy support faded within the season' agree with the full text.

## Change 14
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
https://doi.org/10.3389/fpsyg.2026.1563931 (abstract of the provisionally accepted version read)
```
Replacement:
```
https://doi.org/10.3389/fpsyg.2026.1563931 (full text of the final version read at the publisher's page in the correction session; the writer had read the abstract of the provisionally accepted version, https://doi.org/10.3389/fpsyg.2025.1563931)
```
Result: PASS. Opened https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full: Frontiers in Psychology 17 (2026), article 1563931, published 5 August 2026; 14 authors shown, Tzioumakis to Duda, then '+5 more'. Opened https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1563931/full: the provisionally accepted version at that address. The placement of the five unseen authors in the entry (before Duda) is not confirmed by the page; left to the filer against Crossref, as the drafter says.
Syllabus: no conflict.

## Change 15
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
5. Section 3: the writer read the PAPA trial (Tzioumakis et al.) in abstract only, from the provisionally accepted version; the fresh check and the re-check opened the final 2026 version (Frontiers in Psychology 17:1563931), from which the unit takes only the citation, the players' ages (10 to 15) and the workshop's length (about six hours); it reports no standardised effect sizes and no athlete outcomes.
```
Replacement:
```
5. Section 3: the writer read the PAPA trial (Tzioumakis et al.) in abstract only, from the provisionally accepted version; the correction session read the final 2026 version (Frontiers in Psychology 17:1563931) in full at the publisher's page, from which the unit takes the citation, the observation system (MMCOS), the players' ages (10 to 15), the workshop's length (about six hours) and the authors' "short-term, but not sustained"; it reports no standardised effect sizes and no athlete outcomes.
```
Result: PASS. Opened https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full: MMCOS, ages 10 to 15, about six hours and 'short-term, but not sustained' all confirmed (see Change 13).
Syllabus: no conflict.

## Change 16
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
SP7 must look for that evidence again.
```
Replacement:
```
One such study, of youth athletes' perceived and preferred coach feedback and team motivational climate (Stein, Bloom & Sabiston, 2012, Psychology of Sport and Exercise), was found only as a copy on an author's university site, not at its publisher's page, so nothing is reported from it and the grade stands. SP7 must look for that evidence again.
```
Result: PASS (names a lead not opened; no claim rests on it). Stein, Bloom & Sabiston (2012) not opened by this check: searches returned a McGill Sport Psychology lab PDF (https://www.mcgill.ca/sportpsych/files/...), sport-iat records and unrelated pages; no ScienceDirect page, PubMed record or DOI address, so not fetched. The description is from the search titles only ('Influence of perceived and preferred coach feedback on youth athletes' perceptions of team motivational climate', Psychology of Sport and Exercise 13 484-490), which the replacement's wording matches. The grade stays [practice] by SP1's rule 2 as quoted in fresh-check-SP1.md (no study of any design tests the claim); SP1's full key is not in the packet, only its rules as the SP1 fresh check quotes them.
Syllabus: no conflict. F18 and F30 leave the evidence to SP7; F30 already names Stein, Bloom & Sabiston (2012) as SP7's lead; the grade stays practice.

## Change 17
File: hub.py
Current:
```
Known gaps. (1) References named in the unit or its notes that were not opened, on which no claim rests (11 not opened in all): the reviews on controlling coaching (Bartholomew et al., 2009 and 2011) and the Controlling Coach Behaviors Scale paper (Bartholomew et al., 2010), so the harsh-coaching regrade rests on three cross-sectional surveys and a practitioner article's notes; the randomised Mastery Approach to Coaching trial on performance anxiety (Smith, Smoll and Cumming, 2007); the reward meta-analysis (Deci, Koestner and Ryan, 1999), so the unit states no effect of rewards on intrinsic motivation; the dropout review (Crane and Temple, 2015); the American Academy of Pediatrics clinical report on overuse, overtraining and burnout (Brenner et al., 2024) and the ECSS/ACSM overtraining consensus (Meeusen et al., 2013), so the burnout section gives no definition, sign list or recovery time from them; the observation system used in the football trial (MMCOS; Smith et al., 2015). Most were reachable only as repository copies, behind PubMed's reCAPTCHA, or by a fetch that was refused. No published critique of the challenge-and-support model was found. (2) Claims read from an abstract or summary only: the autonomy-support meta-analysis (Mossman et al., 2024), whose moderate grade was set without its sensitivity analyses or study quality and whose sample ages are unknown; the burnout model review (Gustafsson et al., 2011); the PAPA football trial (Tzioumakis et al., 2026), read by the writer in the abstract of its provisionally accepted version, with the final 2026 version opened by the checkers; the practitioner article on challenge and support (Fletcher and Sarkar, 2016), abstract and notes only. (3) The fresh check could not open: the IOC consensus statement on youth athletic development (Bergeron et al., 2015), so its quotations in sections 5, 7, 8 and 9 were checked by the writer only; the numbers of the handball study (Gómez-López et al., 2020); the details of the emotional-abuse study (Adams et al., 2024) beyond its sample size, mean age and sports; the dropout review in swimming (Monteiro et al., 2017) beyond its abstract, whose stated total of 727 participants does not match its table, so the unit gives no total. (4) Thin: no study tests any single coach behaviour alone, only styles and climates as bundles; no behavioural study of peer or coach evaluation in front of others in young athletes was opened, so the advice on public or private feedback is graded practice; no study of how selection, playing time or attention are communicated was opened; effort has no row, no study opened having measured it as an outcome of coach behaviour. The twenty behaviours of the self-audit are not a validated observation instrument.
```
Replacement:
```
Known gaps. (1) References named in the unit or its notes that were not opened at a publisher's page, PubMed or a DOI address, on which no claim rests (10 in all): the reviews on controlling coaching (Bartholomew et al., 2009 and 2011) and the Controlling Coach Behaviors Scale paper (Bartholomew et al., 2010), left to DD-SP1, so the harsh-coaching regrade rests on three cross-sectional surveys and a practitioner article's notes; the randomised Mastery Approach to Coaching trial on performance anxiety (Smith, Smoll and Cumming, 2007); the reward meta-analysis (Deci, Koestner and Ryan, 1999), and no other source on rewards and intrinsic motivation in sport could be opened, so the unit states no effect of rewards on intrinsic motivation; the dropout review (Crane and Temple, 2015); the American Academy of Pediatrics clinical report on overuse, overtraining and burnout (Brenner et al., 2024) and the ECSS/ACSM overtraining consensus (Meeusen et al., 2013), so the burnout section gives no definition, sign list or recovery time from them; the paper of the observation system used in the football trial (MMCOS; Smith et al., 2015), so the self-audit's twenty behaviours have not been checked against it; and the study of youth athletes' perceived and preferred coach feedback (Stein, Bloom and Sabiston, 2012). Most were reachable only as repository or author copies, or behind PubMed's browser check. No published critique of the challenge-and-support model was found. (2) Claims read from an abstract or summary only: the autonomy-support meta-analysis (Mossman et al., 2024), whose moderate grade was set without its sensitivity analyses or study quality and whose sample ages are unknown; the burnout model review (Gustafsson et al., 2011); the practitioner article on challenge and support (Fletcher and Sarkar, 2016), abstract and notes only, its main text not visible at the publisher's page in any session. The PAPA football trial (Tzioumakis et al., 2026) was read in full in its final version at the correction. (3) The IOC consensus statement on youth athletic development (Bergeron et al., 2015), which the fresh check could not open, was opened in full at its publisher's page by the corrections check, and its quotations in sections 5, 7, 8 and 9 were found word for word. The handball study (Gómez-López et al., 2020), the emotional-abuse study (Adams et al., 2024) and the swimming dropout review (Monteiro et al., 2017) were opened at their publishers' pages at the correction and their claims checked; three statements were corrected (the questionnaire no longer called widely used; the handball players' selection; the review's conclusion that the main reasons are controllable by the athletes). The swimming review's stated total of 727 participants does not match its table, so the unit gives no total. (4) Thin: no study tests any single coach behaviour alone, only styles and climates as bundles; no behavioural study of peer or coach evaluation in front of others in young athletes was opened, so the advice on public or private feedback is graded practice; no study of how selection, playing time or attention are communicated to young athletes was found, so section 5's steps stay practice; effort has no row, no study opened having measured it as an outcome of coach behaviour. The twenty behaviours of the self-audit are not a validated observation instrument. (5) The autonomy-support figure is drawn as a line figure, because the compare figure cannot draw values below zero; on a phone its category labels break inside words.
```
Result: FAIL, in part (3) only. Its statement that Bergeron et al. (2015) could not be opened by the correction and that its quotations are marked not verified is wrong: opened https://bjsm.bmj.com/content/49/13/843.full, every quotation word for word (Changes 5 to 10). Part (3) also undercounts the corrections (the handball sentence also lost 'widely used', C2). Everything else checked: (1) lists ten references, and ten are named (Bartholomew 2009, 2010, 2011; Smith, Smoll & Cumming 2007; Deci et al. 1999; Crane & Temple 2015; Brenner 2024; Meeusen 2013; Smith 2015 MMCOS; Stein 2012); Adams et al. (2024) opened at https://www.frontiersin.org/articles/10.3389/fspor.2024.1428682/full (Frontiers, publisher: 20 former college athletes, 19 to 44, nine sports, USA, qualitative; most accepted some physical punishment; punitive conditioning described as arbitrary, unsafe and cruel, with injury and fear), so section 4 holds; Gómez-López and Monteiro as in Changes 2 to 4; PAPA as in Change 13; part (5) matches the phone drawing (Change 1). The corrected replacement contains no double quote, so it sits in the intro's double-quoted literal. Corrected text below.
Syllabus: no conflict once corrected. Uncorrected, part (3) would contradict the unit after Changes 5 to 10 are withdrawn. Bartholomew stays with DD-SP1 (F31), Brenner and Meeusen with SP9 (F32), Smith, Smoll & Cumming with SP4 (F33), as the text says.

## New 1
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
2. Every quotation was taken from the fetch tool's extraction of the page, not from a direct view of the text; the IOC phrases and Fletcher & Sarkar's note 7 should be checked word for word.
```
Replacement:
```
2. Every quotation was taken from the fetch tool's extraction of the page, not from a direct view of the text; the IOC phrases were checked word for word at the publisher's page (https://bjsm.bmj.com/content/49/13/843.full) by the corrections check on 17 Nov 2026; Fletcher & Sarkar's note 7 should still be checked word for word.
```
Result: Unsure list item 2 says the IOC phrases are unchecked; they were checked at https://bjsm.bmj.com/content/49/13/843.full. Occurs once.
Syllabus: no conflict

## New 2
File: hub.py
Current:
```
1 was held: the autonomy-support figure stays a range, because the compare figure cannot draw negative values.
```
Replacement:
```
1 was held: the autonomy-support figure stayed a range, because the compare figure cannot draw negative values; the corrections pass redrew it as a line figure.
```
Result: The read-sp3 intro's 'How it was made' still says the figure stays a range, which contradicts Change 1 and part (5) of Change 17's Known gaps. The drafter left it to the filer; it must be changed in the same pass or the page contradicts itself. Occurs once; no double quote.
Syllabus: no conflict

## New 3
File: SP3-motivation-and-the-climate-you-create.md
Current:
```
**Public and private feedback (F18).**
```
Replacement:
```
**Public and private feedback.**
```
Result: The paragraph Change 16 edits carries an internal flag code, '(F18)', in a heading of a public course. Minor; cut it. Occurs once.
Syllabus: no conflict

Summary: 17 changes: 11 PASS (C1-C4, C11-C16), 6 FAIL (C5-C9 withdraw: the IOC statement opens at bjsm.bmj.com and every quotation is word for word; C10 and C17 corrected to record that). 3 new findings. C1 passes, but its phone drawing breaks all four x labels inside words; F40's fresh re-check on the page shots is still owed.
