claude-opus-5-5

# Corrections check, round 2, C-SP5 (row W-SP6), Sport Psychology for Coaches

Date: 18 Nov 2026. Packet: /tmp/w/corr2 (read only). files/ not changed. Every Current below was counted with `grep -cF` in its file: 1 each.

Sources opened (each URL returned verbatim by a WebSearch in this agent):
- Vohs et al. (2021): https://bura.brunel.ac.uk/bitstream/2438/28246/1/FullText.pdf (Brunel repository copy; full text: main article, supplement, references; version not stated on the file; first 100,000 of 111,664 characters read)
- Hagger et al. (2016): https://nature.berkeley.edu/garbelottoat/wp-content/uploads/hagger-chatzisarantis-2016.pdf (copy of the published PDF, header "2016, Vol. 11(4) 546–573"; first 100,000 of 131,427 characters read)
- Ranehill et al. (2015): https://www.zne.uzh.ch/dam/jcr:e5fc4c3c-d50e-4aa9-96ab-4389e426d20d/Psychological%20Science-2015-Ranehill-0956797614553946.pdf (OnlineFirst PDF, "published on March 25, 2015")
- Sisk et al. (2018): https://englelab.gatech.edu/articles/2018/Sisk,%20Burgoyne%20et%20al.%20(2018)%20-%20Mindset%20and%20Academic%20Achievement.pdf (copy of the published PDF, Psychological Science 2018, 29(4), 549–571)

Not opened:
- Sawyer et al. (2018): the only publisher page for the article that a search returned, https://www.thelancet.com/journals/lanchi/article/PIIS2352-4642(18)30022-1/ppt, was refused by the harness; not retried. The other publisher page returned (…/references) holds only the reference list and was not fetched (it would be the same article and the rule bars a second attempt). No publisher abstract or full-text page was returned by three searches. PubMed (30169257) was returned but is not the publisher's page this task requires.
- None of the four SP1 sources was opened at its publisher's own page; each was read on a copy a search returned, which this task accepts.

## Change 1
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
| 5. Has it held up? | The hormone part did not hold in this test. No sport performance study found. |
```
Replacement:
```
| 5. Has it held up? | The hormone part did not hold in this test or in the replication; the replication found higher self-reported feelings of power. No sport performance study found. |
```
Result: PASS. Held fix F11 (fresh check line 39, Deliverable B claim 1 question 5), the only Ranehill fix not yet in the filed text. Ranehill et al. (2015), UZH copy opened: testosterone "t(196) = −1.405, p = .162, d = −0.200", cortisol "p = .272", both not significant; self-reported feelings of power "t(193) = 2.399, p = .017, d = 0.344". https://www.zne.uzh.ch/dam/jcr:e5fc4c3c-d50e-4aa9-96ab-4389e426d20d/Psychological%20Science-2015-Ranehill-0956797614553946.pdf
Syllabus: no conflict. Brief SP1 asks for "the replication record as cautionary cases, each from its replication study"; section 7 and section 8 of SP1 already say the same of Ranehill.

## Change 2
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
([Vohs et al., 2021, abstract read](https://doi.org/10.1177/0956797621989733))
```
Replacement:
```
([Vohs et al., 2021, full text read on a repository copy](https://doi.org/10.1177/0956797621989733))
```
Result: PASS. New 1 of round 1 settled: sections 7 and Sources are true, section 8's "abstract read" is not. The Brunel copy holds the full article, not only the abstract: it gives "Confirmatory tests found a non-significant result, d = 0.06", Bayes factor 4.4 under an informed prior δ = 0.30 (SD = 0.15), the full-sample exploratory "statistically significant effect (d = 0.08)", "the depletion effect was larger for participants reporting more fatigue", 2,375 women and 1,130 men, mean age 20.92, 23 of 36 laboratories in the US; version not stated on the file. https://bura.brunel.ac.uk/bitstream/2438/28246/1/FullText.pdf. The label now matches section 7 and the Deliverable C contested row word for word.
Syllabus: no conflict.

## Change 3
File: SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
an interval that includes zero ([Hagger et al., 2016, read on a copy of the published PDF](https://doi.org/10.1177/1745691616652873)).
```
Replacement:
```
an interval that includes zero; its participants were undergraduate students aged 18 to 30 ([Hagger et al., 2016, read on a copy of the published PDF](https://doi.org/10.1177/1745691616652873)).
```
Result: PASS. Residue of held fix F11 (fresh check line 25, the ego-depletion error), whose Fix stated the replications' samples; the filed text gives Vohs et al.'s sample but not Hagger et al.'s (Part 7: a finding states its sample). Hagger et al. copy opened: "Multiple laboratories (k = 23, total N = 2,141)", "d = 0.04, 95% CI [−0.07, 0.15]", participants undergraduates who took part "for course credit or payment" and had to be 18 to 30 years old. https://nature.berkeley.edu/garbelottoat/wp-content/uploads/hagger-chatzisarantis-2016.pdf
Syllabus: no conflict.

## Change 4
File: SP2-the-developing-athlete-10-to-25.md
Result: FAIL. Sawyer et al. (2018) not opened (publisher page refused; see Not opened). No change to SP2: its section 4 and unsure-list item 5 still say truly that Sawyer et al. could not be opened. F23 stays open for Sawyer.
Syllabus: no conflict.

## Held fixes of F11 already in the filed SP1 text (no change needed)

Fifteen held fixes: six ego depletion, six power posing, two growth mindset, one Lochbaum. Lochbaum (fresh check line 33) was closed by C-SP1. Of the other fourteen, Changes 1 and 3 above carry what is left; the rest are already in the filed text and agree with the sources opened:

- Line 25, section 7 ego depletion: filed text reports Vohs (36 labs, 3,531, d = 0.06 n.s.) and Hagger (23 labs, 2,141, d = 0.04, −0.07 to 0.15) from the replications themselves; Miyake & Carruth gone. PASS (Brunel and Berkeley copies). Sample residue: Change 3.
- Line 26, section 8 willpower: Vohs and Hagger cited, [contested]. PASS; label fixed by Change 2.
- Line 27, Deliverable C contested row: Vohs figures and the 23-laboratory replication. PASS (Brunel, Berkeley copies).
- Line 28, Miyake & Carruth Sources entry: `grep -cF "Miyake"` = 0. Done.
- Line 29, Hagger Sources entry: present; "2016;11(4):546–573" matches the PDF header. PASS.
- Line 30, Vohs Sources entry: present; "32(10), 1566–1581" on the Brunel file. PASS.
- Line 35, section 7 growth mindset: k = 273, N = 365,915, r = .10 (.08 to .13); k = 43, N = 57,155, d = 0.08 (0.02 to 0.14); "Overall effects were weak for both meta-analyses"; low SES or academically at risk "might benefit". PASS (Georgia Tech copy).
- Line 43, Sisk Sources entry: five authors, 29(4):549–571, DOI. PASS (Georgia Tech copy).
- Line 36, section 7 power posing: 200 (102 men, 98 women), random assignment, two poses for 3 min against the original's 1 min, no effect on testosterone, cortisol or financial risk-taking, higher self-reported power, no ages or population given. PASS (UZH copy).
- Line 37, section 8 power pose: Ranehill and Metzler cited. PASS (UZH copy).
- Line 38, Deliverable B q1: "The first replication (Ranehill et al., 2015) is reported in section 7; the original was not opened." PASS.
- Line 40, Deliverable B grade: rule 5, two controlled studies, not pre-registered or multi-site. PASS: the UZH copy mentions no preregistration and describes a single study; extended from 100 to 200 participants.
- Line 42, Ranehill Sources entry: present. Volume, issue and pages (26(5):653–656) come from the HHS record, which was not opened here; the OnlineFirst copy shows none. Not checked; not part of the held fix's text.
- Line 39: Change 1.

Not changed (outside what a correction names): SP1 unsure-list item 2 still calls Metzler & Grèzes "a single randomised test" on which power posing "rests", although section 7 now leads with Ranehill. Flag for the next pass; not changed under limits (a) to (f).
