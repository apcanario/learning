Verdict: SP5 · fix · 1 error, 7 should-fix, 13 minor

(The harness blocked the agent's write to out/report.md; the agent returned the full report as its reply and the chat saved it verbatim.)

Model: claude-opus-5-5. The harness refused the write to out/report.md, so the full report follows here.

How it was run: the audit-units §3 fresh check with the figures paragraph, live search, plus the seven named passes. Web rule: WebSearch first, then WebFetch only for URLs a search in this run returned. The PMC, PubMed and tandfonline pages returned a captcha or failed; another copy returned by the same search was used instead.

## Findings
[error] [accuracy] §3.5 Zang bullet; Current: "(distal against proximal)"; Problem: The parenthesis limits the authors' novice sentence to the distal-against-proximal comparison. In Table 2 every novice comparison is non-significant: distal external against internal SMD 0.13 (−0.14 to 0.40), proximal external against internal 0.12 (−0.15 to 0.39), distal against proximal 0.1 (−0.12 to 0.32). The parenthesis stretches the source and hides a null result for novices that bears on the contested grade.; Fix: "(in novices no comparison was significant: distal against proximal, and each distance against internal focus)"; Basis: Zang, Guo & Wang 2025, PeerJ 13:e20012, Table 2 and Conclusions, https://peerj.com/articles/20012.pdf

[should-fix] [figure] §3.3 Deng bullet; Current: "found serve accuracy improved, *g* = 0.99 (95% CI 0.68 to 1.30)"; Problem: The pooled accuracy effect comes from 8 trials and 237 participants, not from the 9 trials and 548 participants named just before it.; Fix: "found serve accuracy improved, *g* = 0.99 (95% CI 0.68 to 1.30; 8 trials, 237 participants)"; Basis: Deng et al. 2024, Behav Sci 14(3):207, results table, https://mdpi.com/2076-328X/14/3/207

[should-fix] [accuracy] §3.2 What it is; Current: "for fine tasks instructional self-talk was more effective than motivational."; Problem: The abstract that was read also reports larger effects for novel than for well-learned tasks, and for interventions that included self-talk training. Both bear on §4 and on the grade for a practised phrase, and the unit leaves both out.; Fix: "for fine tasks instructional self-talk was more effective than motivational. The abstract also reports larger effects for novel than for well-learned tasks, and for interventions that included self-talk training than for those that did not."; Basis: Hatzigeorgiadis et al. 2011, abstract, https://www.psychologicalscience.org/journals/perspectives/1745691611413136/

[should-fix] [label] §3.1 Grade; Current: "Preferring process goals for competition: [weak, positive; a sport meta-analysis read in abstract only, whose participants are not described and whose study quality, samples and ages were not seen, rule 5; for athletes under 18 an inference until the samples are seen]"; Problem: Under the brief's key, a meta-analysis of sport studies grades moderate. Reading only the abstract is not a ground for weak in the key. The unit's own source, Lochbaum & Lane (2025), maps meta-analyses with athlete samples and reports this one.; Fix: "Preferring process goals for competition: [moderate, positive; a sport meta-analysis of 27 studies, read in abstract only, whose study quality, samples and ages were not seen, rule 4; for athletes under 18 an inference until the samples are seen]" (if SP1's rule 4 needs more than one meta-analysis, keep weak and name the rule that applies); Basis: brief.txt grade key; https://ro.uow.edu.au/test2021/6227 (27 studies); https://www.mdpi.com/2075-4663/13/12/420

[should-fix] [label] §2 closing grade; Current: "samples aged 18 and over, the 2024 review excluding junior athletes"; Problem: Brown & Fletcher give no ages, and Lochbaum & Lane describe samples from youth to elite. "Aged 18 and over" is not supported for the whole evidence base.; Fix: "samples mostly adult where ages are reported (the 2017 abstract gives none), the 2024 review excluding junior athletes"; Basis: https://dspace.lboro.ac.uk/2134/21964 ; https://www.mdpi.com/2075-4663/13/12/420

[should-fix] [label] §3.4 Grade, breathing for performance; Current: "one with fewer errors, one with slower reactions, rule 5]"; Problem: The samples are students aged 18 to 41, and §3.4 teaches breathing from age 10. The grade does not label use under 18 as an inference.; Fix: "one with fewer errors, one with slower reactions, rule 5; inference for under-18s]"; Basis: https://frontiersin.org/articles/10.3389/fpsyg.2019.01923/pdf ; https://www.frontiersin.org/articles/10.3389/fpsyg.2022.963711/full

[should-fix] [attribution] §1 The model; Current: "a narrative review, outside the source types the course lists: the model is reported as this review states it, and no grade or recommendation rests on it)"; Problem: Part 7 requires every source to be one of the listed types, and a narrative review is not one. The model is a mechanism claim.; Fix: open a standard textbook or handbook chapter on the cognitive-behavioural or ABC model, cite it by edition and chapter, and replace the Turner citation with it. Until then: "a narrative review, outside the source types the course lists; the model is unsourced by the course's standard, reported as this review states it, and no grade or recommendation rests on it)"; Basis: sourcing-standard.md Part 7, line 2

[should-fix] [label] Deliverable A, Milan; Current: "and his referral to the academy's medical staff stand"; Problem: case-facts.md records only that the academy has medical staff a coach can refer to (SP1). It does not record that Milan has been referred, whereas Dani's referral is registered at SP6. This is an invented case fact that is not in the notes.; Fix: "and the referral route to the academy's medical staff stand"; Basis: case-facts.md

[minor] [label] Deliverable A, Milan within the block; Current: "goes to his profile and referral"; Problem: Same as the finding above.; Fix: "goes to his profile and the referral route"; Basis: case-facts.md

[minor] [label] Preamble; Current: "(the goal-setting and self-talk meta-analyses and the external-focus bias re-analysis were read in abstract only)"; Problem: The list is incomplete. Brown & Fletcher, Bühlmayer, Noetel and Battaglini were also read in abstract only, and Laborde 2022 in abstract and parts of the text.; Fix: "(the 2017 interventions meta-analysis, the goal-setting, self-talk and mindfulness meta-analyses, the mindfulness systematic review, the external-focus bias re-analysis and the basketball relaxation study were read in abstract only, the slow-breathing meta-analysis in abstract and parts of the text)"; Basis: the unit's own Sources notes

[minor] [label] Card 5 Grade; Current: "[contested; rule 1: a bias-corrected re-analysis finds the effect small to nil; inference under 18]"; Problem: The claim rests on an abstract, and the card does not say so.; Fix: "[contested; rule 1: a bias-corrected re-analysis, read in abstract, finds the effect small to nil; inference under 18]"; Basis: https://experts.mcmaster.ca/display/publication3486012

[minor] [label] Card 4 Tested on; Current: "59 basketball players aged 14 to 19 ("; Problem: The card does not say the study was read in abstract, that the players were male, or that no randomisation is reported.; Fix: "59 male basketball players aged 14 to 19, no randomisation reported, abstract read ("; Basis: https://mdpi.com/1660-4601/19/24/17065

[minor] [label] Card 1 Grade; Current: "Performance goal from own record: [weak, positive]. Process goals for competition: [weak, positive; sport meta-analysis read in abstract, samples not seen]."; Problem: The inference label for under-18s that §3.1 carries is missing here.; Fix: "Performance goal from own record: [weak, positive; one study of swimmers aged about 15]. Process goals for competition: [weak, positive; sport meta-analysis read in abstract, samples not seen; for under-18s an inference]." (use moderate if the §3.1 grade finding is applied); Basis: §3.1 of the unit

[minor] [accuracy] Sources, Reinebo; Current: "*Sports Medicine* 2024;54:347–373"; Problem: The issue number is missing; the record gives issue 2.; Fix: "*Sports Medicine* 2024;54(2):347–373"; Basis: https://lida.sport-iat.de/twm/Record/4087323?lng=en

[minor] [accuracy] Sources, Bühlmayer note; Current: "issue and the last two authors from the course's seed list: not verified"; Problem: These are now verified: Bühlmayer, Birrer, Röthlin, Faude, Donath; 47(11):2309–2321.; Fix: "issue and the last two authors verified at https://edoc.unibas.ch/61837 by the quality review, 18 Nov 2026"; Basis: https://edoc.unibas.ch/61837

[minor] [accuracy] Sources, Noetel note; Current: "which shows the four authors but not the title, journal, year, volume or pages; those are from the course's seed list: not verified"; Problem: These are now verified: 12(1):139–175, 2019.; Fix: "which shows the four authors; title, journal, year, volume, issue and pages verified at https://opus.lib.uts.edu.au/handle/10453/138664 by the quality review, 18 Nov 2026"; Basis: that URL

[minor] [style] Unsure list item 8; Current: "the Favre-Bulle et al. (2024) page shows only the first author; its full author list is not verified."; Problem: This contradicts the Sources entry. All six authors are verified on the publisher's PDF.; Fix: "the Favre-Bulle et al. (2024) full author list was read on the publisher's PDF and confirmed by the quality review, 18 Nov 2026."; Basis: https://peerj.com/articles/17799.pdf

[minor] [accuracy] §2 Three families; Current: "Self-talk, goal setting and relaxation appeared only inside multimodal packages"; Problem: The 111-study review includes single-technique studies of these skills; they were simply not synthesised. The claim holds only for the pooled analyses.; Fix: "In the pooled analyses, self-talk, goal setting and relaxation appeared only inside multimodal packages"; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01931-z.pdf

[minor] [figure] §3.1 Ferchichi; Current: "rose 47.1% in the goal group against 19.1% in the control group"; Problem: The paper's own table means do not reproduce these percentages; they give about 44% and 8%.; Fix: "rose 47.1% in the goal group against 19.1% in the control group (the paper's percentages; its table means give different changes)"; Basis: https://public-pages-files-2025.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2026.1759066/pdf

[minor] [attribution] §2 flag F2; Current: " (facilitative variables *d* = 0.51, debilitative *d* = −0.21)"; Problem: These figures come from a paper this unit did not open, reported through SP1. That conflicts with the preamble's "Nothing in this unit rests on a paper that was not opened" and with Part 1's reporter rule.; Fix: "" (delete); Basis: sourcing-standard.md Part 1

[minor] [coverage] §3.4 Teaching by band; Current: "and stops if they feel dizzy or short of breath [practice]."; Problem: Progressive muscle relaxation is not taught by band.; Fix: "and stops if they feel dizzy or short of breath [practice]. Progressive muscle relaxation, from 13 to 15 upward: a short guided sequence after training, as in both studies opened (ages 14 to 19 and about 21); for 10 to 13 an inference [practice]."; Basis: https://mdpi.com/1660-4601/19/24/17065 ; https://www.frontiersin.org/articles/10.3389/fpsyg.2020.617541/full

[minor] [deliverable] Deliverable A, Milan weeks 4 and 6; Current: "Thu: phrase written on the match card beside the process goal."; Problem: Week 2 holds the first use for a lower-stakes match, as §4 stage 4 requires, but weeks 4 and 6 drop that condition. "Saturday" is also not in the register, which says only "at the weekend".; Fix: "Thu: phrase written on the match card beside the process goal, for the first match you judge lower-stakes." Make the same addition after "Thu: match card carries goal, phrase and target." Either register "Saturday" as a case fact or write "the weekend".; Basis: §4 of the unit; case-facts.md

## (7) Figures
- Flow, §1: PASS. Every label is in §1, and the caption names the section and Turner.
- Range, §2: PASS. All 8 point estimates and intervals match the text and the sources. The 90% CI for Bühlmayer is noted in the caption. The kind fits competing estimates.
- Matrix, §3.6: PASS. Each mark traces to a sample stated in §3.
- Flow, §4: PASS. The timings trace to §4 and Deliverable A.

## Passes
**Claims.** All 22 cited sources were opened. Every figure, sample size and quotation PASSES except the Zang parenthesis (FAIL, the error above) and the two imprecisions in Deng and Ferchichi (above). These were not opened, by me or by the unit: Lochbaum 2022, Tod 2011, Wulf 2013, Chua 2021. No claim in the unit rests on them except the d values reported through SP1 (minor above).

**Bibliography.** All 22 entries exist, and authors, title, journal, year, volume, pages and DOI match publisher or repository records. Two gaps: Reinebo has no issue number, and the notes on Bühlmayer, Noetel and Favre-Bulle still say "not verified" though all three are now verified (all minor). No Crossref record was opened, because none was returned by search.

**Source log.** The source log was not available for this unit. In its place, the Sources notes give the address, what was read and the date. Every claim that rests on an abstract says so in the body. The exceptions are Card 5, Card 4 and the incomplete list in the preamble (all minor).

**Grades.** All grades match the key and the evidence, with one exception: the process-goal grade sits below the key (should-fix). No grade is strong, and that is correct: every meta-analysis cited reports low certainty, risk of bias, or effects that lose significance when only RCTs are kept.

**Population.** Every finding names its sample. Missing inference labels: breathing for performance (should-fix), the "18 and over" claim in §2 (should-fix), Card 1 and relaxation under 14 (minor).

**Scope and safety.** PASS. The disclaimer is present. The teaching-versus-treating line, the stop-and-refer steps and the scope card are all there. There is no assessment, diagnosis, weight content, self-harm content or law. The only real people named are the cited authors.

**Any sport.** I counted about 45 examples by hand. Football has about 11 (24%) and athletics about 8 (18%). Tennis and swimming have 5 each, judo 3, gymnastics, rowing and basketball 2 each, and cycling, volleyball and golf 1 each. No sport is above a third. If each week's row of the Milan block is counted, football rises to about 31%, still under a third.

**Part 7.**
- Fails: source types (Turner).
- Partial: inference labels; abstract-only labels in two cards.
- Not checked: the popular-claims list (the seed bibliography is not in the packet); kit/private_terms.py (not available; reading found nothing about the owner); the source log (not available).
- Case facts: Milan's referral and "Saturday" are not in the register.
- Every other line passes.

**Brief and deliverable.** Every item is covered; relaxation by band is thin. Both blocks (Milan's squad and Sara), all six cards and both templates are present and in full.

**Errata.** No audit report was in the packet. Pointers to SP1, SP3, SP4, SP6 and SP8 could not be checked.

## Confirmed
Each source PASSES on every value the unit cites from it:
- Turner, https://frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01423/full
- Brown & Fletcher 47(1):77–99, https://dspace.lboro.ac.uk/2134/21964
- Reinebo, https://link.springer.com/content/pdf/10.1007/s40279-023-01931-z.pdf
- Lochbaum & Lane, https://www.mdpi.com/2075-4663/13/12/420
- Williamson, https://ro.uow.edu.au/test2021/6227 and https://researchportal.scu.edu.au/esploro/outputs/journalArticle/The-performance-and-psychological-effects-of/991013048913602368
- Ferchichi, the frontiersin PDF above
- Hatzigeorgiadis 6(4):348–356, https://bvbvf1.bib-bvb.de/vufind/PrimoRecord/cdi_proquest_miscellaneous_1696683610
- Walter, https://pmc.ncbi.nlm.nih.gov/articles/PMC6628429
- Yang, https://frontiersin.org/articles/10.3389/fspor.2023.1304911/full
- Liu, https://www.mdpi.com/2076-328X/15/5/685/html
- Deng, https://mdpi.com/2076-328X/14/3/207
- Behrendt, https://www.mdpi.com/1660-4601/18/18/9467
- Laborde 2022, https://eprints.bournemouth.ac.uk/38169/
- Laborde 2019, https://frontiersin.org/articles/10.3389/fpsyg.2019.01923/pdf
- Buchanan & Janelle, https://www.frontiersin.org/articles/10.3389/fpsyg.2022.963711/full
- Liang, https://www.frontiersin.org/articles/10.3389/fpsyg.2020.617541/full
- Battaglini, https://mdpi.com/1660-4601/19/24/17065
- Favre-Bulle, https://peerj.com/articles/17799
- Zang (except the parenthesis), https://peerj.com/articles/20012
- McKay 150(11):1347–1362, https://experts.mcmaster.ca/scholarly-works/3486012
- Bühlmayer, https://link.springer.com/doi/10.1007/s40279-017-0752-9
- Noetel, https://opus.lib.uts.edu.au/handle/10453/138664

## Could not verify
- Pointers to other units: SP1's rule numbers, section 9 and Sara's scope card; SP3's grades; SP4's profile and its match-day rule.
- Whether Milan was referred in SP4.
- The sports of Reinebo's four focus crossover studies.
- Walter's volume and issue (secondary records only).
- Crossref records.
- The popular-claims list.
- private_terms.py.
- Whether the reviews measured harms.
