Verdict: SP2 · fix · 0 error, 3 should-fix, 4 minor
Model: claude-opus-5-5 (Opus 5.5). This is the quality review of SP2, run on 17 Nov 2026 with live search, reading only the qr3-SP2 packet. The harness would not let me write out/report.md, so the full report follows.

Passes
- Claims: FAIL. I could not reopen one source, and the unit does not mark its claims. There are also two wording stretches.
- Bibliography: PASS. Every field I opened matched the record. Fields I could not open are listed under Could not verify.
- Source log: FAIL. One entry has no date.
- Grades: PASS. I checked every grade against SP1's key: rules 1 to 5 and the three further rules. The Güllich & Barth grade [strong] meets rule 3:
  - both confidence intervals exclude zero, and every subgroup excludes zero;
  - the authors rate the studies "high methodological quality";
  - no review that disagrees was found.
- Population: PASS.
- Scope and safety: FAIL. The unit touches injury but never says where the coach's part ends or who takes over.
- Any sport: PASS. Each section's mentions counted once, deliverable included: football 5, athletics 4, judo 2, swimming 2, handball 2, basketball 1, ice hockey 1, tennis 1. Football is 5 of 18 (28%), under a third. Nothing in the unit identifies the Project's owner.
- Part 7, line by line: every item is met except three:
  - the F14 note on grades (minor 3);
  - the source-log item (should-fix 3);
  - the coach's-part item (should-fix 2).
  - The rest holds: the disclaimer is present; no weight-loss method, calorie figure or target weight; no self-harm method; no law stated as the reader's; no real person named. Each case athlete is labelled "(fictional)" on first use and agrees with case-facts.md, and the SP2 rows of the register match the facts marked *added*. The deliverable is built in full for Dani, Milan and Sara, and the template says what goes in each blank.
- Brief: every item is covered. Two items are stated as unsourced, as the sourcing rule requires: self-image under maturation (F16) and emotion regulation from 16 to 25 (F19).
- Flags naming SP2: F4, F12, F13, F14, F15, F16, F17, F19, F21, F22, F25, F28 and F42 are each dealt with in the unit.
  - F22 only in part: Cobley was opened in abstract, which gives no pooled figure.
  - F42: Boccia is marked not verified where its claims sit; the NSCA English text was read; Paruthi and Watson were moved off the PubMed Central copies.
  - F43 is this review.
- Figures:
  - (1) Range, section 4: PASS. Every label and number traces to section 4 ("Cortical grey matter volume peaked at 5.9 years (95% interval 5.8 to 6.1)…" and "stabilizing to adult-levels in late adolescence (18–20 years old)"). The caption names the section and the sources, and the kind fits.
  - (2) Range, section 8: PASS. Every value is in section 8's bullets. The caption names the section, the sources and the 7-hour floor, and the kind fits.
  - (3) Range, section 10: PASS. The d values, intervals and k match "d = −0.53, 95% CI −0.74 to −0.32; 16 effects" and "d = 0.56, 0.40 to 0.72; 34 effects". The caption names the section and the source and says the data are correlational.
  - All keys are valid in viz.py's range schema.

Findings
[should-fix] [claims] Section 7; Current: "([Stambulova et al., 2021, consensus](https://doi.org/10.1080/1612197X.2020.1737836))"; Problem: I could not reopen the ISSP stand at its publisher's page: no search returned a tandfonline or DOI address, only university repositories. So I cannot check the six layers, the kinds of transition, the Swedish ice hockey phases, "no success rate", the dual-career quotation or the 126-study review, and the unit does not mark them; Fix: "([Stambulova et al., 2021, consensus](https://doi.org/10.1080/1612197X.2020.1737836); full text read by the writer; not verified by the quality review of 17 Nov 2026, which could not reach the publisher's page)"; Basis: searches on 17 Nov 2026 returned only https://jyx.jyu.fi/jyx/Record/jyx_123456789_68164 and other repository records
[should-fix] [scope] Deliverable B, Sara; Current: "| What I watch | Three transitions at once (senior, injury return, study away from home) [practice; ISSP]."; Problem: the unit touches injury (Sara's hamstring, overuse injury in section 9, sleep and injury in section 8). It never says where the coach's part ends or who takes over, which the preamble requires of every unit that touches injury; Fix: "| What I watch | Three transitions at once (senior, injury return, study away from home) [practice; ISSP]. Her return from the hamstring injury: load and return decisions belong to the doctor or physiotherapist managing it; your part is to follow their plan and report what you see in sessions [practice; the course's scope line]."; Basis: brief.txt (Scope); sourcing-standard.md Part 7, coach's-part item
[should-fix] [source log] Sources, Smith et al. (2018); Current: "(abstract read; a correction to its Table 4"; Problem: the entry gives no date or address, which Part 7 requires; Fix: "(abstract read at the publisher's page, 17 Nov 2026; a correction to its Table 4"; Basis: sourcing-standard.md Part 7; I reopened the abstract at https://www.springermedizin.de/relative-age-effects-across-and-within-female-sport-contexts-a-s/15531364 and the citation at https://pubmed.ncbi.nlm.nih.gov/29536262/
[minor] [claims] Section 9; Current: "33 of them supporting the developmental model of sport participation"; Problem: 33 of the 38 studies were based on the DMSP (5 on LTAD). "Supporting" reads as 33 positive findings; Fix: "33 of them based on the developmental model of sport participation"; Basis: Gallant & Bélanger 2021, https://www.frontiersin.org/articles/10.3389/fspor.2021.741495/full
[minor] [claims] Section 9; Current: "young people who specialise after puberty have fewer injuries and stay in sport longer than those who specialise early"; Problem: the IOC hedges this ("tend to be more consistent performers, have fewer injuries and adhere to sports play longer"), and the unit drops the hedge; Fix: "young people who specialise after puberty tend to have fewer injuries and stay in sport longer than those who specialise early"; Basis: Bergeron et al. 2015, https://bjsm.bmj.com/content/49/13/843.full
[minor] [grades] Deliverable A, 10 to 12; Current: "More than 8 months a year in one sport (NSCA) [practice]."; Problem: this is graded practice from a consensus statement whose underlying studies were not opened, but it lacks the note F14 requires; Fix: "More than 8 months a year in one sport (NSCA) [practice; NSCA consensus; the studies behind it were not opened]."; Basis: flags.md F14; NSCA statement, https://dxpprod.nsca.com/globalassets/education/nsca_position_statement_on_ltad.pdf
[minor] [source log] Sources, Paruthi et al. (2016); Current: "(consensus; not opened: its PubMed record showed a captcha on 17 Nov 2026; its content was read in the methodology paper below)"; Problem: the PubMed record now opens (12(6):785–6, DOI 10.5664/jcsm.5866, modified RAND method, recommendations summarised). A reference marked not opened should not carry a claim, and this one can now be marked as read; Fix: "(consensus; abstract read on PubMed by the quality review, 17 Nov 2026; the hours, panel, search and associations were read in the methodology paper below)"; Basis: https://pubmed.ncbi.nlm.nih.gov/27250809/

Could not verify:
- Section 2, Albaladejo-Saura et al. (2021): the athlete counts, boys and girls, sports, ages and test-by-test results. The unit marks these. Only the abstract opened at https://mdpi.com/1660-4601/18/1/328; it confirms 13 studies, the boys' advantage, and that in girls only height and body mass differed.
- Section 3, Cobley et al. (2009), marked abstract read: the DOI address redirected, so I did not check it.
- Section 10 and the deliverables, Boccia et al. (2017) and its correction, marked not verified: the DOI address redirected, so I did not check it.
- Section 7, Stambulova et al. (2021): see should-fix 1. Authors, volume, issue, pages and online date were not checked against the publisher.
- Bibliography fields not shown on the pages I opened: Lorenz & Kray issue 9; Güllich et al. (2022) authors, volume and pages; Bergeron end page 851; Crone & Dahl issue 9.

Confirmed:
- Section 1:
  - NSCA statement (NSCA server PDF): the quotations "differ markedly with respect to biological maturity" and "the technical competency, training history, and stage of growth and development of the child"; maturation varies in timing, tempo and magnitude; the term "training age" does not appear; no DOI is printed.
  - IOC statement (bjsm.bmj.com full text): "first two decades", "more related to biological clocks than to coaching and training", the November 2014 meeting.
- Section 2:
  - IOC: peak VO2 rises about 80% in girls and 150% in boys from 8 to 16; girls outscore boys until about 12; "maturity-associated selection/exclusion process …" over 9 to 15; "maturity-related gradient … early maturing males".
  - NSCA: "adolescent awkwardness".
  - Ghadirzadeh et al. 2025 (elsevier.es publisher page): 13 studies, 434,838 participants, 5 cohort and 8 cross-sectional; OR 1.36 (1.20–1.53), adolescents 1.34 (1.15–1.56); late menarche not significant; high heterogeneity; publication bias; confounders not consistently controlled; female samples only.
- Section 3:
  - IOC: "older individuals generally outperform younger ones".
  - Smith et al. 2018: 57 studies, 308 samples, 25 sports, 1984–2016; OR 1.25 (1.21–1.30), called "small"; larger at 11 and under and at 12 to 14, at higher levels and in high-demand sports; 48(6):1451–1478.
- Section 4:
  - Bethlehem et al. 2022 (nature.com): 123,984 scans, 101,457 people, more than 100 studies, about 10% longitudinal; peaks 5.9 (5.8–6.1), 14.4 (14.0–14.7) and 28.7 (28.1–29.2); regional peaks about 2 to 10 across 34 areas; "biased towards European and North American populations"; 604:525–533.
  - Foulkes & Blakemore 2018: the quotation and the three sources of variation; 21(3):315–323.
  - Tervo-Clemmens et al. 2023: 10,766 people aged 8 to 35, four datasets (two longitudinal), 23 measures from 17 tasks; fastest change 10 to 15, smaller 15 to 18; "stabilizing to adult-levels in late adolescence (18–20 years old)"; over 95% of the change in accuracy before 18; individual variation expected; 14:6922.
  - Arain et al. 2013: the abstract names no end age; 9:449–461.
- Section 5:
  - Crone & Dahl 2012 key points: inconsistent evidence for slow cognitive-control maturation, more consistent limbic responses, the heuristic model, goal flexibility; 13:636–650.
  - Haddad et al. 2014: 40 adolescents aged 11 to 18 and 24 adults aged 20 to 38 (28 recruited, 4 excluded); fictitious same-age peers; no difference alone; d = 0.95 is the between-group gap under observation; within-group change not tested.
  - Lorenz & Kray 2022: 184 participants aged 8.6 to 19; fictitious same-age, same-sex peer by webcam; the quotation is verbatim; exploration effect clearest in female pre-adolescents; males not susceptible to peer observation; 51:1693–1707.
- Section 6: Sanchis-Sanchis et al. 2020, full text:
  - 254 pupils aged 9 to 16 in eight schools;
  - FEEL-KJ: no age differences after correction;
  - CERQ: self-blame and planning higher and positive refocusing lower at 13 to 16, small effects;
  - latent score η² = 0.02, with 9 to 12 higher (58.99 vs 54.70), against what the abstract says;
  - no gender main effect; interaction η² = 0.07 in the direction stated;
  - "no causal relationships can be established".
- Section 8:
  - Paruthi et al. 2016b (aasm.org): 13 voting members including a moderator, modified RAND method, 864 articles, 9 to 12 h and 8 to 10 h, associations as listed.
  - IOC: 8.5 to 9.5 h and "preliminary evidence indicating an increased likelihood of injury with insufficient sleep".
  - Watson et al. 2015 (aasm.org): 7 or more hours for ages 18 to 60, harms as listed, more than 9 hours "may be appropriate for young adults", 15 experts, 5,314 articles; Sleep 38(6):843–844 and JCSM 11(6):591–592.
- Section 9:
  - IOC: "should avoid early sport specialisation".
  - NSCA: the definition of early specialisation, overuse injury, overtraining or dropout, "should not train in excess of 8 months per year in a single sport".
  - Güllich et al. 2022 abstract: 51 reports, 477 effect sizes, 6,096 athletes, 772 world-class; adult and youth patterns as stated.
  - Gallant & Bélanger 2021: 38 studies; all 8 studies that tested tenet 1 support it; 6 studies (5 cross-sectional) for tenet 2; the after-16 sentence and the quotation; 71% cross-sectional; evidence mostly from elite athletes; 3:741495.
  - Macnamara et al. 2016 abstract: 18%; "accounted for only 1% of the variance in performance among elite-level performers"; no earlier start; no mention of 10,000 hours.
- Section 10:
  - Güllich & Barth 2024 (Springer PDF): 51 effect sizes, 6,233 athletes, 82% male, 2009–2022, nine countries; d values, intervals and k as stated; I² 74.94 and 74.83; studies rated high quality; heterogeneity not discussed; "largely two disparate populations"; turnover 25–47% and 28–55%; 54:697–710.
  - IOC: "the probability of elite success is highly unlikely" (for most) and the "disconnect".
- Deliverable A, 16 to 18: Tzioumakis et al. 2026 (frontiersin.org, final version): players aged 10 to 15; coaches randomly assigned; autonomy support rose short-term and was not sustained; disempowering climate fell; 17:1563931.
