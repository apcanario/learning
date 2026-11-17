Verdict: SP2 · fix · 0 error, 7 should-fix, 8 minor

Quality review of SP2, The developing athlete, 10 to 25. Checker: claude-opus-5-5 (Opus 5.5), in a fresh agent context with live search, 17 Nov 2026. I worked from the packet only and did not edit the unit. Every page I fetched was returned by a search in this agent. Pages that redirected or showed a captcha are marked "not opened" and were not retried. The harness refused the write to out/report.md, so AGENT_RULES applies and the full report follows; save it verbatim.

## Passes

**Claims: FAIL (should-fix).**
- 19 of 24 references were opened at the publisher's page, the issuing body's own page or the DOI address. Most cited claims hold (see Confirmed).
- Four claims stretch or misstate their source:
  - Gallant & Bélanger: the unit says all 38 studies tested the DMSP and gives stage ages the review does not give.
  - Haddad et al.: "the gap arose because" is a causal reading of a within-group change the paper did not test.
  - Lorenz & Kray: the unit says the exploration effect was largest in younger adolescents and that boys did not change. The paper says the effect was clearest in female pre-adolescents and that boys' risk-taking was not changed by peer observation.
  - IOC: girls' lead until about 12 is on cycling peak power, an anaerobic test, but the unit's sentence reads as aerobic.
- Not opened:
  - Boccia et al. (2017): doi.org redirects to PLOS, and no search returned a PLOS address.
  - Stambulova et al. (2021): no Taylor & Francis page was returned, only repository copies.
  - Paruthi et al. (2016, JCSM 12(6)): PubMed showed a captcha; I opened the AASM methodology paper instead.
  - Watson et al. in *Sleep*: I opened the JCSM dual publication on aasm.org instead.
  - Albaladejo-Saura et al. full text: the MDPI page showed the abstract only.
- Claims resting on these are listed under Could not verify.

**Bibliography: PASS for the entries opened; 5 not opened.** I found no reference that does not exist.
- Fields confirmed at the publisher:
  - Albaladejo-Saura; Arain; Bergeron (BJSM 49(13):843); Bethlehem; Cobley.
  - Crone & Dahl (13:636–650; issue not shown).
  - Foulkes & Blakemore; Gallant & Bélanger; Ghadirzadeh; Güllich & Barth; Haddad.
  - Lloyd: confirmed on the NSCA's own server; the DOI is not printed there.
  - Paruthi 2016b; Sanchis-Sanchis; Tervo-Clemmens.
  - Tzioumakis: vol 17, 2026, 1563931, published 5 Aug 2026.
  - Watson: the JCSM version, 11(6):591–592.
- Partly confirmed, because the page opened did not show volume or pages:
  - Güllich et al. 2022 and Macnamara 2016: the APS pages show title and journal only.
  - Lorenz & Kray: issue 9 shown; 51 and 1693–1707 not shown.
  - Smith 2018: 6/2018 shown; 48 and 1451–1478 not shown.
- Not opened: Boccia; Stambulova; Paruthi 2016 (785–786); Watson in *Sleep*.
- Smith et al. (2018) has a published correction to its Table 4 (Sports Medicine 2018;48:1989–1990) that its entry does not mention (minor).

**Source log: FAIL (should-fix).** There is no separate log.
- Entries read in abstract say so: Arain, Cobley, Crone & Dahl, Foulkes & Blakemore, Güllich 2022, Macnamara, Smith.
- These entries do not say what was read or give a date, which Part 7 requires:
  - Unmarked entries: Albaladejo-Saura, Bethlehem, Boccia, Gallant, Ghadirzadeh, Güllich & Barth, Haddad, Lorenz & Kray, Paruthi 2016b, Sanchis-Sanchis, Tervo-Clemmens, Tzioumakis.
  - Consensus entries: Bergeron, Lloyd, Paruthi 2016, Stambulova, Watson.
- Boccia's entry says its correction was not read, but not whether the article itself was opened. F42 says the earlier checker could not open it.
- Unsure-list item 2 is stale: the Stambulova entry now names three authors.

**Grades: PASS with one should-fix.** Grades follow SP1's rules as written, and every technique and recommendation carries one.
- Strong for Güllich & Barth (2024) meets rule 3 on the paper as opened:
  - the CIs exclude zero (Table 2: −0.53, −0.74 to −0.32, k 16; 0.56, 0.40 to 0.72, k 34);
  - moderators are non-significant;
  - the studies are rated high quality.
- I² is about 75% for both estimates. The authors do not discuss it, so rule 4's "heterogeneity its authors flag" does not trigger (minor: report it).
- The section 10 moderate for "junior success as a poor forecast of senior success" has a weak basis (should-fix):
  - Güllich 2022 compares practice histories; it does not test the forecast.
  - Boccia 2017 is unverified.
- F12, F14 and F15 are applied.

**Population: PASS.**
- Each finding names its sample and design:
  - non-athletes: Bethlehem, Tervo-Clemmens, Haddad, Lorenz & Kray, Sanchis-Sanchis, Ghadirzadeh;
  - athletes: the meta-analyses on maturation, relative age, talent programmes and practice;
  - general children and adolescents: AASM.
- Transfers to athletes under 18 are labelled inference (sections 2, 5, 6, 8 and the table).
- Correlations are called correlations (sections 2, 3, 9, 10).

**Scope and safety: PASS.**
- Nothing teaches assessment, diagnosis or treatment. Maturity estimates are left to a qualified person.
- Referrals go to the SP1 scope card, SP9 and DD-SP2: mood, sleep, Dani's snack and weight class, and Sara's sleep and withdrawal.
- No weight-loss method, calorie figure, target weight or self-harm method.
- No law is stated, and the information-not-advice line is present.
- No real person is named.

**Any sport: PASS.**
- Counts by sport: football 4, athletics 4, judo 2, swimming 2 (sections 1 and 9), basketball 1, handball 1, ice hockey 1, tennis 1. The largest share is 4 of 16 (25%).
- Individual, team, weight-class and 400 m sports are all present.
- `kit/private_terms.py` is not in the packet and was not run. Nothing in the unit refers to the Project or its owner.

**Part 7, line by line.**
1. Sourced where made: PASS.
2. Source types: PASS.
3. No video, blog or popular book cited: PASS. The 10,000-hour book is named only as a claim.
4. Source log: FAIL.
5. Entries match the publisher's record: PASS where opened; 5 not opened.
6. Grades: PASS, with one should-fix on a grade's basis.
7. Sample and design stated, correlation called correlation: PASS.
8. Inference labelled: PASS.
9. Effect sizes in the source's own terms: PASS.
10. Popular claims tested (the brain "finishes at 25", 10,000 hours, the brake-and-accelerator account): PASS.
11. Coach's part: PASS.
12. No weight-loss, calorie or self-harm content: PASS.
13. Law and disclaimer: PASS.
14. Real persons: PASS.
15. Sports spread: PASS.
16. Case facts: PASS.
    - All facts the unit adds are in the register's SP2 rows.
    - Training ages agree with the register: Dani 6 years, Milan at least 6, Sara 8.
17. Private terms: not checkable from the packet.
18. Search flag: not applicable (SP2 is search off).
19. Deliverable built on the case, then as a template: PASS.
20. Not advice without evidence: PASS.
21. Links as DOI links: PASS.

**Brief and deliverable.**
- Every item the brief names is present. Two are thin and declared unsourced: pubertal timing and self-image, and emotion regulation from 16 to 25.
- The examination of "finishes at 25" says it went ahead without Somerville (2016) and Sawyer et al. (2018).
- The table is four bands by four columns, and every cell is graded.
- The development notes are built in full for Dani, Milan and Sara with the four required lines, and the template follows.

**Flags naming SP2.**
- F4: dealt with.
- F7 and F24: nothing for the unit to do.
- F12, F13, F14, F16, F17, F18, F19, F21, F26 and F28: dealt with.
- F15: the SP2 side is consistent.
- F22: Cobley is now opened in abstract. The abstract gives no pooled odds ratio, so the unit gives no size for male sport, as it states. The unit's part can be closed.
- F25: recount above (swimming is now 2); the spread holds.
- F42: partly dealt with. NSCA and the two sleep statements are now read at the issuing body's own pages. Boccia is still not opened and is not marked unverified (should-fix below).
- F43: this review.

**Figures.**
1. Section 4, range: FIX (minor). The label should read "Cortical grey matter volume peak". The caption's word "bootstrap" is not in the unit's text.
2. Section 8, range: PASS.
3. Section 10, range: PASS. Its values agree with the paper's Table 2.

All three blocks use only the keys viz.py allows for range. I could not render them because viz.py needs design/theme.css, which is outside the packet.

**Read as the coach in the preamble.** The unit is usable: each section ends in a graded "what to do", and the referral line is clear. Two places overstate:
- Section 5's peer-observation bullets.
- Milan's "none is needed" maturity line. A late-maturing 17-year-old may still be growing.

## Findings

[should-fix] [accuracy] Section 9; Current: "A scoping review of 38 studies testing the developmental model of sport participation (sampling to about 12, specialising from about 13, investing from about 16) found the claim that sampling does not hinder elite participation supported in every retrospective elite-versus-non-elite study"; Problem: the review covers 38 studies of sport participation and physical activity models, 33 of which supported the DMSP. It does not give these stage ages, and "retrospective elite-versus-non-elite" is not its wording; Fix: "A scoping review of 38 studies of sport participation and physical activity models, 33 of them supporting the developmental model of sport participation, found the claim that sampling does not hinder elite participation supported by every study that tested it"; Basis: Gallant & Bélanger (2021), https://www.frontiersin.org/articles/10.3389/fspor.2021.741495/full

[should-fix] [accuracy] Section 5; Current: "the gap arose because the adults became more cautious when observed, while the adolescents did not change"; Problem: the change within each group was not tested. The adolescents' mean rose from 0.400 to 0.458 and the adults' fell from 0.264 to 0.160; the causal reading is the authors' discussion; Fix: "the authors read the gap as adults choosing more safely when observed while adolescents kept choosing risky options at the same rate; the change within each group was not tested"; Basis: Haddad et al. (2014), https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.01476/full

[should-fix] [accuracy] Section 5; Current: "with the largest exploration effect in younger adolescents and no change in boys"; Problem: the paper says "Especially female pre-adolescents increased their openness to explore" and that male adolescents "were not susceptible to peer observation" in risk-taking; it does not say boys' exploration did not change; Fix: "with the exploration effect clearest in female pre-adolescents, and male adolescents' risk-taking not changed by peer observation"; Basis: Lorenz & Kray (2022), https://erasmusmc.mijn.bsl.nl/explore-with-me-peer-observation-decreases-risk-taking-but-incre/20387022 ; https://doi.org/10.1007/s10964-022-01608-2

[should-fix] [accuracy] Section 2; Current: "and girls often outscore boys on peak power until about 12 because they mature earlier"; Problem: in the IOC statement this sentence is about cycling peak power, an anaerobic test; placed after the aerobic sentence, it reads as aerobic; Fix: "and girls often outscore boys on cycling peak power, an anaerobic test, until about 12 because they mature earlier"; Basis: Bergeron et al. (2015), https://bjsm.bmj.com/content/49/13/843.full

[should-fix] [label] Section 10; Current: "One country, two events, observational."; Problem: F42 requires the Boccia claims to be cut or marked unverified. The fresh check could not open the article and its correction was not read. Section 10, the table and three case notes rely on it unmarked; Fix: "One country, two events, observational. Not verified by the fresh check: the publisher's page could not be opened, and the published correction (PMC5441632) was not read."; Basis: flags.md F42; https://doi.org/10.1371/journal.pone.0170744 (redirect, not opened)

[should-fix] [grade] Section 10; Current: "moderate, for junior success as a poor forecast of senior success (Güllich et al., 2022, a meta-analysis read in abstract, and Boccia et al., 2017, one study in athletics, rule 4)"; Problem: Güllich 2022 compares practice histories and does not test junior success as a forecast of senior success; Boccia is unverified; Fix: "moderate, for junior success as a poor forecast of senior success, by inference from the opposite practice histories of higher-performing youth and world-class adult athletes (Güllich et al., 2022, a meta-analysis read in abstract, which does not test the forecast itself) and one study in athletics not verified by the fresh check (Boccia et al., 2017), rule 4"; Basis: https://www.psychologicalscience.org/journals/perspectives/1745691620974772/

[should-fix] [source log] Sources; Current: "2021;18(1):328. https://doi.org/10.3390/ijerph18010328"; Problem: Part 7 requires every entry to say what was read and the date. This entry gives neither, and neither do the other unmarked and consensus entries listed under Source log above. The Albaladejo sample breakdown is not on the publisher's abstract page; Fix: "2021;18(1):328. https://doi.org/10.3390/ijerph18010328 (full text read at <address>, 17 Nov 2026)", and add the same parenthesis to each entry named, taking what was read and the date from the writer's record; Basis: sourcing-standard.md Part 7 item 4; https://mdpi.com/1660-4601/18/1/328

[minor] [accuracy] Development note, Milan; Current: "No maturity estimate on file; at 17 none is needed for coaching decisions: maturity-associated selection falls mostly between about 9 and 15 (IOC) [practice]."; Problem: the IOC passage dates the selection window only; it does not say maturity is irrelevant at 17; Fix: "No maturity estimate on file. At 17 he is past the IOC's window of maturity-associated selection (about 9 to 15); if he is still growing, record his height here as for a younger athlete [practice]."; Basis: https://bjsm.bmj.com/content/49/13/843.full

[minor] [figure] Section 4 figure; Current: "{\"label\": \"Grey matter volume peak (Bethlehem)\""; Problem: the text and the source say cortical grey matter. Separately, in the same figure's caption, replace "with 95% bootstrap intervals" with "with 95% intervals", because "bootstrap" is not in the unit's text; Fix: "{\"label\": \"Cortical grey matter volume peak (Bethlehem)\""; Basis: https://www.nature.com/articles/s41586-022-04554-y

[minor] [label] Section 10; Current: "The primary studies were rated high quality."; Problem: I² is about 75% for both estimates (Table 2) and the unit does not report it; Fix: "The primary studies were rated high quality; heterogeneity was high (I² about 75% for each estimate, the paper's Table 2), which the authors do not discuss."; Basis: https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf

[minor] [bibliography] Sources; Current: "https://doi.org/10.1007/s40279-018-0890-8 (abstract read)"; Problem: the published correction to Table 4 is not noted; Fix: "https://doi.org/10.1007/s40279-018-0890-8 (abstract read; a correction to its Table 4 was published, Sports Medicine 2018;48:1989–1990, https://doi.org/10.1007/s40279-018-0915-3)"; Basis: https://rd.springer.com/content/pdf/10.1007/s40279-018-0915-3.pdf

[minor] [deliverable] Table, about 10 to 12; Current: "Emotion regulation: small differences from 13 to 16, not all in one direction, in one study of school pupils (Sanchis-Sanchis) [weak; inference]."; Problem: the study compares 9 to 12 with 13 to 16; Fix: "Emotion regulation: small differences between 9 to 12 and 13 to 16, not all in one direction, in one cross-sectional study of school pupils (Sanchis-Sanchis) [weak; inference]."; Basis: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2020.00946/pdf

[minor] [accuracy] Section 5; Current: "40 adolescents aged 11 to 18 and 24 adults aged 20 to 38"; Problem: 28 adults were recruited and 4 excluded; 24 is the analysed sample; Fix: "40 adolescents aged 11 to 18 and 24 adults aged 20 to 38 (28 recruited, 4 excluded)"; Basis: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.01476/full

[minor] [deliverable] Table, about 10 to 12; Current: "girls often outscore boys on peak power until about 12 (IOC)"; Problem: the IOC's measure is cycling peak power; Fix: "girls often outscore boys on cycling peak power until about 12 (IOC)"; Basis: https://bjsm.bmj.com/content/49/13/843.full

[minor] [source log] Unsure list item 2; Current: "the entry gives \"Stambulova NB, et al.\" from a repository record"; Problem: the entry now names three authors, so this note is stale; Fix: "the entry gives three authors (Stambulova NB, Ryba TV, Henriksen K) from a repository record, not the publisher's page"; Basis: the unit's Sources list

## Could not verify

- Section 2, Albaladejo-Saura et al. (2021). Not checked:
  - the sample: 1,431 athletes (1,323 boys, 108 girls);
  - the sports, and the ages (girls 9 to 15, boys 12 to 16);
  - which tests differed: throwing, grip, jumping, sprint and agility, but not Yo-Yo or flexibility.
  Reason: the publisher's page shows the abstract only, and the full text was returned only on copies.
- Section 7, Stambulova et al. (2021), every claim. Not checked:
  - the six layers;
  - the three kinds of transition;
  - junior to senior lasting months to years, with the Swedish ice hockey phases;
  - the dual-career quotation;
  - the 126-study retirement review (1968 to 2010) and its factors;
  - athletic identity as a factor.
  Also not checked: 19(4):524–550 and the online date. Reason: no publisher page was returned by search.
- Section 10, the table and the case notes, Boccia et al. (2017). Not checked:
  - 4,864 jumpers, 1994 to 2014;
  - 10% to 25% of top adults were top-level at 16;
  - the women's high jump exception;
  - personal bests at about 21 to 23;
  - faster improvement from 13 to 18, and its predictive value;
  - what the correction changed.
  Reason: the DOI redirects; not opened.
- Paruthi et al. (2016), JCSM 12(6):785–786, record: not opened (PubMed captcha). Its content was checked through Paruthi 2016b.
- Watson et al. (2015), *Sleep* 38(6):843–844, record: not opened. Its content was checked through the JCSM version on aasm.org.
- Bibliography fields not shown on the pages opened:
  - Güllich et al. 2022: 17(1):6–29.
  - Macnamara 2016: 11(3):333–350.
  - Lorenz & Kray: 51, 1693–1707.
  - Smith: 48, 1451–1478.
  - Bergeron: pages and full author list.
  - Crone & Dahl: issue 9.
  - Lloyd: DOI, not printed on the NSCA's server.
- Section 4, Arain et al. (2013): whether the full text names an end age. The abstract names none, as the unit says.
- Milan's note: the SP1 grade cited for phrasing instructions as what to do. SP1 is not in the packet.
- The private-terms check: not in the packet.

## Confirmed

- Lloyd et al. (2016), on the NSCA's server, https://dxpprod.nsca.com/globalassets/education/nsca_position_statement_on_ltad.pdf:
  - the maturation definition (timing, tempo, magnitude) and "individuals of the same chronological age can differ markedly with respect to biological maturity";
  - "the technical competency, training history, and stage of growth and development of the child";
  - "adolescent awkwardness";
  - the definition of early specialisation; overuse injury, "overtraining or dropout", and the "blunting" of the motor skill portfolio;
  - "should not train in excess of 8 months per year in a single sport";
  - the term "training age" does not appear.
- Bergeron et al. (2015), https://bjsm.bmj.com/content/49/13/843.full:
  - the November 2014 meeting; maturation through about the first two decades; "more related to biological clocks than to coaching and training";
  - peak VO2 up about 80% in girls and 150% in boys from 8 to 16;
  - maturity-associated selection at 9 to 15, and the gradient favouring early-maturing males;
  - "older individuals generally outperform younger ones";
  - "should avoid early sport specialisation"; those who specialise after puberty have fewer injuries and adhere longer; diversification;
  - sleep: 8.5–9.5 h, later bedtimes, schedules worsen it, and "preliminary evidence indicating an increased likelihood of injury with insufficient sleep";
  - elite success "highly unlikely"; the disconnect in talent systems; burnout and drop-out.
- Albaladejo-Saura (2021), abstract, https://mdpi.com/1660-4601/18/1/328: 13 studies; in boys, early maturers higher in anthropometry and fitness; in girls, only height and body mass differed.
- Ghadirzadeh (2025), https://www.elsevier.es/en-revista-clinics-22-articulo-the-association-between-age-at-S1807593225001139:
  - 13 studies, 434,838 people; 5 cohort and 8 cross-sectional;
  - OR 1.36 (1.20–1.53); in adolescents, 1.34 (1.15–1.56);
  - later menarche not significant;
  - high heterogeneity, publication bias, confounders not consistently controlled.
- Cobley (2009), https://www.doi.org/10.2165/00007256-200939030-00005: all figures in the abstract as the unit states them; no pooled OR in the abstract.
- Smith (2018), https://www.springermedizin.de/relative-age-effects-across-and-within-female-sport-contexts-a-s/15531364:
  - 57 studies, 308 samples, 25 sports, 1984–2016;
  - OR 1.25 (1.21–1.30);
  - the moderators as the unit gives them.
- Bethlehem (2022), https://www.nature.com/articles/s41586-022-04554-y: all figures and the bias quotation.
- Foulkes & Blakemore (2018), https://link.springer.com/article/10.1038/s41593-018-0078-4: the quotation and the three sources of variation.
- Tervo-Clemmens (2023), https://www.nature.com/articles/s41467-023-42540-8.pdf: all figures, the "18–20" quotation, more than 95% of change before 18, and individual variability.
- Arain (2013), abstract: names no end age. https://www.dovepress.com/maturation-of-the-adolescent-brain-peer-reviewed-fulltext-article-NDT
- Crone & Dahl (2012), https://link.springer.com/article/10.1038/nrn3313:
  - evidence on control regions inconsistent;
  - "rewards, emotional faces and social feedback";
  - the heuristic model and its adaptive value.
- Haddad (2014): no difference when alone; d = 0.95 under observation; fictitious peers in photographs.
- Lorenz & Kray (2022): 184 participants aged 8.59–18.97; a same-age, same-sex peer apparently watching by webcam; the quoted finding.
- Sanchis-Sanchis (2020), full text: every figure in section 6, including partial η² 0.02 with the younger group higher in Table 7, and 0.07, and the "no causal relationships" quotation.
- Paruthi 2016b, https://aasm.org/resources/pdf/pediatricsleepdurationmethods.pdf: the hours; 13 voting members; modified RAND; 864; the associations.
- Watson (2015), https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf: 7 hours or more; the harms; more than 9 "may be appropriate for young adults"; 15 experts; 5,314 articles.
- Güllich et al. (2022), abstract, https://www.psychologicalscience.org/journals/perspectives/1745691620974772/: 51 reports, 477 effects, 6,096 athletes, 772 world-class, and the adult and youth patterns.
- Macnamara (2016), abstract, https://www.psychologicalscience.org/journals/perspectives/1745691616635591/: 18% and 1% of variance; no earlier start; 10,000 hours not mentioned.
- Gallant & Bélanger (2021):
  - six studies on longer participation, five of them cross-sectional;
  - specialisation after 16;
  - the "specific age ranges" quotation;
  - 71% cross-sectional; mostly elite athletes.
- Güllich & Barth (2024), https://link.springer.com/content/pdf/10.1007/s40279-023-01957-3.pdf:
  - 51 effects, 6,233 athletes, 82% male, 2009–2022, nine countries;
  - d −0.53 (−0.74 to −0.32, k 16) and 0.56 (0.40 to 0.72, k 34);
  - high-quality studies;
  - "largely two disparate populations";
  - turnover 25–47% and 28–55%;
  - correlational.
- Tzioumakis (2026), https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1563931/full:
  - coaches randomly assigned; players aged 10–15; four countries;
  - a temporary rise in autonomy support and a fall in disempowering behaviour;
  - vol 17, 1563931.
