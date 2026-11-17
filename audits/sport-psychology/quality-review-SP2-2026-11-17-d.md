Verdict: SP2 · fix · 0 error, 12 should-fix, 4 minor

Model: claude-opus-5-5. Quality review of SP2 (round 5), 17 Nov 2026. The harness refused the write to out/report.md, so this is the full report for the chat to save verbatim. Web: WebSearch first; WebFetch only on URLs a search returned; refused or redirected fetches are listed as not checked and were not retried.

## Findings

1. [should-fix] [claims] §2 Performance; Current: "A systematic review and meta-analysis of 13 studies (1,431 young athletes, 1,323 boys and 108 girls; mostly football, basketball and handball; girls aged 9 to 15, boys 12 to 16) compared early and late maturers within the same age groups. In boys, early maturers were taller and heavier and did better on tests of throwing, grip, jumping, sprinting and agility; endurance (the Yo-Yo test) and flexibility did not differ by maturity. In girls only height and body mass differed, from very few studies ([Albaladejo-Saura et al., 2021](https://doi.org/10.3390/ijerph18010328)). The sample counts, sports, ages and test-by-test results are not verified: the fresh check could open only the abstract at the publisher's page."; Problem: The sample counts, sports, ages and test-by-test results come from a full text nobody opened (Sources: "full text not opened"). A claim from a text that was never opened carries no claim. "The fresh check" is a reviewer note left in the reader's text. The abstract, opened today at the publisher's page, gives 13 studies, SMD 0.37–2.31 (kinanthropometric) and 0.17–2.31 (physical fitness) in boys, and 0.96–1.19 (height and body mass) in girls.; Fix: "A systematic review and meta-analysis of 13 studies of young athletes compared early and late maturers within the same age groups. In boys, the early-maturing groups had higher kinanthropometric values (standardised mean differences 0.37 to 2.31) and better physical-fitness results (0.17 to 2.31); in girls only height and body mass differed (0.96 to 1.19) ([Albaladejo-Saura et al., 2021, abstract read](https://doi.org/10.3390/ijerph18010328)). The abstract gives no sample sizes, sports, ages or test-by-test results, and the full text was not opened, so none is given here."; Basis: https://mdpi.com/1660-4601/18/1/328

2. [should-fix] [claims] §10 One sport, followed over time; Current: "**One sport, followed over time.** A retrospective study of Italian federation rankings from 1994 to 2014 followed 4,864 high and long jumpers from 12 to the end of their careers. Of the athletes who reached the top level as adults, only 10% to 25% had been top-level at 16, and most athletes who were top-level at 16 did not stay there; women's high jump was the exception. The athletes who became the best adults reached their personal bests later (about 21 to 23) and improved faster each year between 13 and 18; adding the yearly rate of improvement predicted adult personal bests better than performance alone ([Boccia et al., 2017](https://doi.org/10.1371/journal.pone.0170744)). One country, two events, observational. Not verified by the fresh check: the publisher's page could not be opened, and the published correction (*PLoS ONE* 2017;12(5):e0178662) was not read; its PubMed record says only that it corrects this article."; Problem: The Sources entry says Boccia et al. (2017) was "not opened". By the brief, a reference that could not be opened carries no claim, yet this paragraph gives six specific findings from it. Today the DOI redirected (not checked). "The fresh check" is a reviewer note in the reader's text.; Fix: "**One sport, followed over time.** One study found follows athletes' national rankings from youth to senior level, in Italian high and long jumpers (Boccia et al., 2017). It could not be opened at its publisher's page or its DOI address, and its published correction was not read, so this unit takes no finding from it."; Basis: https://doi.org/10.1371/journal.pone.0170744 (redirected; not checked)

3. [should-fix] [source log] §3, Cobley citation; Current: "abstract read by the writer; not verified by the quality review of 17 Nov 2026, whose DOI fetch redirected"; Problem: This is a reviewer note in the reader's text. Cobley's DOI redirected again in this review (not checked), so nothing in the sentence is verified.; Fix: "abstract read; not verified, because the DOI address later redirected"; Basis: https://www.doi.org/10.2165/00007256-200939030-00005 (redirected; not checked)

4. [should-fix] [source log] §7, ISSP citation; Current: "full text read at the publisher's page by the writer and by the quality review of 17 Nov 2026"; Problem: A reviewer note in the reader's text. The content was confirmed today at the publisher's page.; Fix: "full text read at the publisher's page"; Basis: https://informahealthcare.com/doi/full/10.1080/1612197X.2020.1737836

5. [should-fix] [source log] Sources, Cobley et al. (2009); Current: "(abstract read, 17 Nov 2026)"; Problem: The entry gives no address, and the body says the source is not verified. Authors, volume, issue and pages could not be checked: the DOI redirected.; Fix: "(abstract read at the DOI address, 17 Nov 2026; on a later attempt the DOI address redirected, so the abstract's content and the authors, volume, issue and pages are not verified)"; Basis: https://www.doi.org/10.2165/00007256-200939030-00005 (redirected; not checked)

6. [should-fix] [bibliography] Sources, Lloyd et al. (2016); Current: "(consensus; full text read on the NSCA's own server, 17 Nov 2026)"; Problem: The entry gives no address. The DOI is not printed on the NSCA text, and PubMed served a reCAPTCHA page, so the DOI is not verified (unsure item 9 admits this, but the entry does not mark it). Everything else checked: the four quotations are verbatim, "training age" does not appear, and the authors and 30(6):1491–1509 are correct.; Fix: "(consensus; full text read on the NSCA's own server, https://dxpprod.nsca.com/globalassets/education/nsca_position_statement_on_ltad.pdf, 17 Nov 2026; the DOI is not printed there and is not verified)"; Basis: https://dxpprod.nsca.com/globalassets/education/nsca_position_statement_on_ltad.pdf

7. [should-fix] [source log] Sources, Paruthi et al. (2016); Current: "abstract read on PubMed by the quality review, 17 Nov 2026"; Problem: A reviewer note, and no address. The PubMed record today gave J Clin Sleep Med 2016;12(6):785–6 and doi 10.5664/jcsm.5866.; Fix: "record read on PubMed, https://pubmed.ncbi.nlm.nih.gov/27250809/, 17 Nov 2026"; Basis: https://pubmed.ncbi.nlm.nih.gov/27250809/

8. [should-fix] [source log] Sources, Paruthi et al. (2016b); Current: "(full text read at the AASM's page, 17 Nov 2026)"; Problem: No address. The content was confirmed at the AASM PDF: 9–12 h and 8–10 h, 13 voting members including a moderator, modified RAND, and 864 articles left after title screening.; Fix: "(full text read at the AASM's page, https://aasm.org/resources/pdf/pediatricsleepdurationmethods.pdf, 17 Nov 2026)"; Basis: https://aasm.org/resources/pdf/pediatricsleepdurationmethods.pdf

9. [should-fix] [source log] Sources, Watson et al. (2015); Current: "full text read on the AASM's page, 17 Nov 2026"; Problem: No address. The content was confirmed: at least 7 h; "may be appropriate for young adults"; 15 experts; 5,314 articles; dual publication in SLEEP 38(6):843–4.; Fix: "full text read on the AASM's page, https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf, 17 Nov 2026"; Basis: https://www.aasm.org/resources/pdf/adultsleepdurationconsensus.pdf

10. [should-fix] [bibliography] Sources, Lorenz & Kray (2022); Current: "*Journal of Youth and Adolescence* 2022;51(9):1693–1707."; Problem: The volume and pages could not be verified. The author's accepted PDF and a BSL record show the journal, 2022, issue 9 and the DOI, but no volume or pages, and no publisher page was returned by search.; Fix: "*Journal of Youth and Adolescence* 2022;51(9):1693–1707 (volume and pages not verified)."; Basis: https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/33069/1/Lorenz-Kray2022_Article_ExploreWithMePeerObservationDe.pdf

11. [should-fix] [bibliography] Sources, Crone & Dahl (2012); Current: "*Nature Reviews Neuroscience* 2012;13(9):636–650."; Problem: The publisher's page (link.springer.com) gives 13, 636–650 and no issue number. The issue is not verified.; Fix: "*Nature Reviews Neuroscience* 2012;13(9):636–650 (issue not verified)."; Basis: https://link.springer.com/article/10.1038/nrn3313

12. [should-fix] [bibliography] Sources, Bergeron et al. (2015); Current: "*British Journal of Sports Medicine* 2015;49(13):843–851."; Problem: The publisher's page (bjsm.bmj.com/content/49/13/843) confirms volume 49, issue 13 and first page 843, but shows neither the title nor an author list (initials only) nor the last page. The last page is not verified.; Fix: "*British Journal of Sports Medicine* 2015;49(13):843–851 (last page not verified)."; Basis: https://bjsm.bmj.com/content/49/13/843.full

13. [minor] [source log] Sources, Boccia et al. (2017); Current: "its PubMed record checked, which says only that it corrects this article; its content not read)"; Problem: The entry gives no address for the PubMed record it says was checked.; Fix: "its PubMed record checked (address not recorded), which says only that it corrects this article; its content not read)"; Basis: n/a (record not re-opened; PubMed served reCAPTCHA in this session)

14. [minor] [grades] Deliverable A, 16 to 18, What to ask for; Current: "SP3 grades the autonomy support behind it [moderate, positive, association; sample ages not known] and [weak, positive, association] in 12- to 18-year-olds;"; Problem: These grades rest on SP3's sources, which are not cited or listed in SP2, so the claim is not sourced where it is made.; Fix: "SP3 grades the autonomy-support evidence behind it (see SP3);"; Basis: sourcing-standard Part 1 ("sourced where it is made")

15. [minor] [grades] Deliverable A, 10 to 12, What to watch; Current: "[moderate, for relative age in sport (Cobley et al., 2009) and in female sport (Smith et al., 2018); practice for the check]"; Problem: The Cobley half of the grade rests on a source the unit marks not verified. Smith (2018), verified today on PubMed (OR 1.25, 95% CI 1.21–1.30), carries the grade only for female sport.; Fix: "[moderate, for relative age in female sport (Smith et al., 2018); the same in sport overall (Cobley et al., 2009) is not verified; practice for the check]"; Basis: https://pubmed.ncbi.nlm.nih.gov/29536262/

16. [minor] [grades] §2, grade on the maturity–performance association; Current: "one meta-analysis of small studies in athletes, rule 4"; Problem: "Small studies" is the stated reason the meta-analysis fails rule 3, but the abstract gives no study sizes and the full text was not opened. The reason actually known is that rule 3's conditions could not be checked.; Fix: "one meta-analysis in athletes, read in abstract, its intervals, sensitivity analyses and study quality not seen, rule 4"; Basis: https://mdpi.com/1660-4601/18/1/328

## Seven passes

- **Claims:** I opened every cited source except Cobley (DOI redirected) and Boccia (DOI redirected). Two claims rest on text that was never opened (findings 1 and 2). All others pass (see Confirmed).
- **Bibliography:** No reference is invented, and every reference exists. Fields not verified: findings 5, 6, 10, 11 and 12.
- **Source log:** The Sources list doubles as the log. Five entries give no address for what was read (findings 5 to 9; minor 13). Each claim that rests on an abstract says so in the body, except Albaladejo's (fixed by finding 1).
- **Grades:** Each grade matches a rule of section 9 and the evidence:
  - Güllich & Barth (2024) [strong] meets rule 3: CIs exclude zero, holds across moderators, MMAT high quality, authors do not flag I²≈75%.
  - Güllich et al. (2023) [weak] fits rule 5.
  - Güllich et al. (2022) [moderate] is by rule 4, with rule 3 not checkable (disclosed).
  - The consensus-only recommendations are [practice] under F14.
  - Minor issues: findings 14 to 16.
- **Population:** Each finding names its sample and design. Transfers of non-athlete data to athletes under 18 are labelled inference in §§2, 5, 6 and 8 and in the table.
- **Scope and safety:**
  - Nothing teaches assessment, diagnosis or treatment.
  - Mood, sleep, eating (Dani's snack), weight class and injury (Sara) each name where the coach's part ends and who takes over.
  - There is no weight-loss method, calorie figure or target weight, and no self-harm method.
  - The information-not-advice line is at line 12.
  - No real person or club is named.
- **Any sport:** Football 4, athletics 4, judo 2, swimming 1, basketball 1, handball 1, ice hockey 1, tennis 1. The largest share is 27%, under a third (matches F25). `kit/private_terms.py` is not in the packet and was not run.

## Part 7, brief and deliverable

- Part 7 passes line by line, except for the source-log, bibliography and opened-source items above.
- Every brief item is covered. Three are thin, each declared unsourced:
  - Self-image (§2)
  - Emotion regulation at 16 to 25 (§6)
  - Athletic identity size (§7)
- Deliverable:
  - The age-and-stage table has all four bands and four columns, and every cell is graded.
  - Development notes are built for Dani, Milan and Sara, followed by the template, whose blanks say what goes in them.
  - Case facts agree with case-register.md, and the added facts are listed there. The case athletes are labelled (fictional) at first use, and the case is never used as evidence.
  - Training ages check: Dani 6, Milan at least 6, Sara 8.
- Tone: no "not X but Y" constructions found.

## Flags naming SP2

These need register updates only; no unit text changes.
- **F22:** says "Cobley et al. (2009) was not opened". The unit now cites its abstract and marks it not verified. The flag should stay open until Cobley is verified at the publisher's page.
- **F28:** satisfied by the unit, which now cites Tzioumakis et al. (2026). The flag can be closed.
- **F42:** partly met:
  - NSCA English text read: met.
  - Sleep statements read on AASM pages and PubMed: met.
  - Boccia still not opened: finding 2 cuts its claims.
- **F16:** states "108 of 1,431" as fact. That figure is not verified (finding 1), and the flag should say so.
- **F4, F12 to F15, F17 to F19, F21, F25, F26:** each agrees with the unit as it stands.

## Figures

All three viz blocks parse as JSON, pass viz.py's check_keys with no message, and render without error through viz.py's render.

1. **range, §4: PASS.**
   - Every label and number is in §4: 2–10; 5.8/5.9/6.1; 14.0/14.4/14.7; 18–20; 25; 28.1/28.7/29.2.
   - The caption names the section and both sources.
   - Range fits competing intervals.
2. **range, §8: PASS.**
   - Every value is in §8: 9–12, 8–10, 8.5–9.5, 7.
   - The caption names the section, the three sources and the "no ceiling" point.
3. **range, §10: PASS.**
   - The values match §10: −0.53 (−0.74 to −0.32), k = 16; 0.56 (0.40 to 0.72), k = 34.
   - The caption names the section and the source, and says the data are correlational.

## Could not verify

- Cobley et al. (2009): abstract, authors, volume, issue and pages. doi.org redirected to link.springer.com (not checked, not retried).
- Boccia et al. (2017): all content. doi.org redirected to journals.plos.org (not checked).
- Albaladejo-Saura et al. (2021): full-text figures (1,431; 1,323/108; sports; ages; Yo-Yo, flexibility). The MDPI page gives the abstract only.
- Lloyd et al. (2016): the DOI. PubMed served reCAPTCHA, and the NSCA PDF does not print it.
- Lorenz & Kray (2022): volume and pages.
- Crone & Dahl (2012): issue.
- Bergeron et al. (2015): last page, and the title and authors on the publisher's page.
- Stambulova et al. (2021): authors and volume on the publisher's page (the page did not show them). They match the JYX repository record: 19(4):524–550.
- Paruthi et al. (2016, jcsm.5866): the author list. The PubMed fetch showed no authors.
- `kit/private_terms.py` was not run (not in the packet).

## Confirmed

- **Bergeron et al. (2015), at bjsm.bmj.com/content/49/13/843.full.** Verbatim:
  - "more related to biological clocks than to coaching and training"
  - "maturity-associated selection/exclusion process commonly occurring during the interval of puberty" (9 to 15)
  - "maturity-related gradient in selection favouring early maturing males in many sports"
  - "older individuals generally outperform younger ones"
  - "preliminary evidence indicating an increased likelihood of injury with insufficient sleep"
  - "should avoid early sport specialisation"
  - "the probability of elite success is highly unlikely" (followed by "for most")
  - "tailored training and even perhaps schooling schedules"

  Also confirmed: peak VO2 +80% girls and +150% boys, ages 8 to 16; girls outscore boys on cycling peak power to about 12; 8.5–9.5 h; burnout and dropout; meeting in November 2014; maturation over about the first two decades.
- **Lloyd et al. (2016), at the NSCA PDF.** The four quotations are verbatim. "Training age" is absent. Definitions match. Authors and 30(6):1491–1509 are correct.
- **Bethlehem et al. (2022), at nature.com.**
  - 123,984 scans; 101,457 people; more than 100 studies; about 10% longitudinal.
  - Peaks: GMV 5.9 (5.8–6.1); sGMV 14.4 (14.0–14.7); WMV 28.7 (28.1–29.2); regional 2 to 10 across 34 areas.
  - "biased towards European and North American populations".
  - Nature 604:525–533.
- **Tervo-Clemmens et al. (2023), at nature.com PDF.**
  - N = 10,766; ages 8 to 35; four datasets (two longitudinal); 23 measures from 17 tasks.
  - "stabilizing to adult-levels in late adolescence (18–20 years old)"; more than 95% of accuracy change before 18; individual variability expected.
  - 14:6922.
- **Foulkes & Blakemore (2018), at link.springer.com.** "obscures meaningful individual variation in development"; SES, culture, peers; 21(3):315–323.
- **Arain et al. (2013), at dovepress.** The abstract names no end age. 9:449–461, eight authors.
- **Crone & Dahl (2012), at link.springer.com.** Cognitive-control evidence "relatively inconsistent"; "more consistent evidence" for limbic responses peaking mid-adolescence; heuristic model; adaptive value.
- **Haddad et al. (2014), at frontiersin.org.**
  - 40 adolescents aged 11 to 18; adults 28 recruited, 4 excluded, aged 20 to 38; peers shown as photographs.
  - No difference alone; d = 0.95 under observation; no within-group test.
- **Lorenz & Kray (2022), at the author's accepted PDF.** N = 184, about 9 to 19; same-age, same-sex webcam peer; "peer observation reduced risk-taking but increased exploration tendencies"; female pre-adolescents; males "not susceptible to peer observation".
- **Sanchis-Sanchis et al. (2020), at frontiersin.org PDF.**
  - 254 pupils aged 9 to 16 in eight schools; FEEL-KJ shows no difference after correction; CERQ shows self-blame, planning and positive refocusing.
  - Partial η² 0.02, with the younger group higher (58.99 vs 54.7), against the abstract.
  - Gender × age partial η² 0.07; "no causal relationships can be established".
- **Stambulova et al. (2021), at informahealthcare.com.** Six layers; normative, non-normative and quasi-normative transitions; transitions "last from several months to years"; Swedish ice hockey four phases; no success rate; dual-career definition verbatim; consequences; Park et al. 126 studies, 1968 to 2010; athletic identity; pp. 524–550; online 10 March 2020.
- **Paruthi et al. (2016b), at the AASM PDF.** 9–12 h and 8–10 h; 13 voting members including a moderator; modified RAND; 864 articles; associations as stated; 12(11):1549–1561.
- **Paruthi et al. (2016), at PubMed.** 12(6):785–6; jcsm.5866.
- **Watson et al. (2015), at the AASM PDF.** At least 7 h; harms as listed; "may be appropriate for young adults"; 15 experts; 5,314 articles; JCSM 11(6):591–592; SLEEP 38:843–4.
- **Albaladejo-Saura et al. (2021), at mdpi.com (abstract).** 13 studies; boys SMD 0.17–2.31 (fitness) and 0.37–2.31 (kinanthropometric); girls height and body mass only, SMD 0.96–1.19; 18(1):328.
- **Smith et al. (2018), at PubMed.** 57 studies, 308 samples, 25 sports, 1984 to 2016; OR 1.25 (1.21–1.30); larger at 11 and under and at 12 to 14, at higher levels, and in team sports and physically demanding individual sports; 48(6):1451–1478. Correction to Table 4 at 48:1989–1990 (rd.springer.com).
- **Ghadirzadeh et al. (2025), at elsevier.es.** 13 studies; 434,838 participants; 5 cohort and 8 cross-sectional; OR 1.36 (1.20–1.53); adolescents 1.34 (1.15–1.56); late menarche not associated; high heterogeneity; publication bias; confounders not consistently controlled; females only; authors and 80:100695.
- **Güllich et al. (2022), at the APS journal page and the issue listing.** 51 reports, 477 effect sizes, 6,096 athletes, 772 world-class; adult and youth findings as stated; 17(1):6–29, three authors.
- **Macnamara et al. (2016), at the APS page and the issue listing.** 18% overall; "accounted for only 1% of the variance in performance among elite-level performers"; no earlier start; 10,000 hours not mentioned; 11(3):333–350.
- **Gallant & Bélanger (2021), at frontiersin.org.** 38 studies, 33 DMSP; tenet 1 supported by all studies that tested it; six studies, five cross-sectional; "specific age ranges have yet to be consistently demonstrated"; specialised after 16; 71% cross-sectional; elite-heavy; 3:741495.
- **Güllich & Barth (2024), at the link.springer.com PDF.**
  - 51 effect sizes; 6,233 athletes; 82% male; 2009 to 2022; nine countries.
  - Junior d −0.53 (−0.74 to −0.32), k = 16; senior d 0.56 (0.40 to 0.72), k = 34; I² 74.94% and 74.83%; heterogeneity not discussed; MMAT high quality.
  - "largely two disparate populations"; turnover 25–47% and 28–55%; 54:697–710.
- **Güllich et al. (2023), at the link.springer.com PDF.** 110 samples and 38,383 juniors; 79 samples and 22,961 seniors; "7.2% identical and 92.8% disparate" (international U17/18 vs seniors); synthesis of percentages, no meta-analysis; 53:1201–1217.
- **Tzioumakis et al. (2026), at frontiersin.org.** Athletes aged 10 to 15; coach-education trial in four countries; empowering and autonomy support rose for a time, then declined; disempowering behaviour fell; 17:1563931; first authors as cited.
