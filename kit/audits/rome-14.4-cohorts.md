# Rome 14.4: the sample against the Greek baseline, and the stratum decision

Run with Fable 5.1, 27 October 2026. Inputs: the twelve Rome 14.2 scorecards (`audits/rome-14.2-r-*.md`) and the four Greek baselines of 13.1 (`audits/greece-13.1-rubric.md`). The Greek Opus cohort (10.4, 10.7 to 10.12, units 11 and 12) has no scorecards yet; Greek 13.2 has not run, so that comparison waits for 13.4.

## The sample

Twelve Rome reports, all Opus 5.5, stratified by how they had been checked before this review. Every one was audited under 14.2, fixed under 14.5 (errata applied, `check.py` OK) and its flag cleared.

| Stratum | Reports | Means | Stratum mean | Factual errors per report | Verdicts |
|---|---|---|---|---|---|
| 1, quality-pass "keep" (13 reports) | 0.1, 1.4, 1.6, 4.2, 7.3 | 4.9, 4.9, 4.8, 4.4, 4.8 | 4.76 | 0, 1, 0, 1, 0 | 3 pass, 2 revise |
| 2, quality-pass "fix" (26) | 2.3, 3.5, 5.2, 6.4 | 4.6, 4.6, 4.8, 4.6 | 4.65 | 1, 0, 0, 0 | 3 pass, 1 revise |
| 3, fresh-checker pipeline (17) | 8.3, 9.2, 11.2 | 4.9, 4.6, 4.7 | 4.73 | 0, 0, 1 | 2 pass, 1 revise |
| All | 12 | 4.4 to 4.9 | 4.72 | 4 in 12 (none with more than one) | 8 pass, 4 revise, 0 rewrite |

The four factual errors: 1.4 "the literature begins about 200 BC" (the Roman literature); 2.3 Pliny "thought Cornelia innocent" (he withholds judgement, Letters 4.11.9); 4.2 "more than 20,000" mercenaries (Polybius 1.67.13: about 20,000); 11.2 Sulla's letter to the Senate dated 83 (written from the East in 85 or 84, Appian 1.77). None is load-bearing.

## The eight shared dimensions

| Dimension | Greek Fable baseline (4): mean, range, worst | Rome sample (12): mean, range, worst |
|---|---|---|
| 1 Accuracy | 5.0, 5–5 | 4.67, 4–5, 1.4 / 2.3 / 4.2 / 11.2 |
| 2 Citation | 4.75, 4–5, 6.3 | 4.25, 4–5, nine reports at 4 |
| 3 Coverage | 4.75, 4–5, 4.2 | 4.50, 4–5, six at 4 |
| 4 Depth | 5.0, 5–5 | 4.83, 4–5, 6.4 / 9.2 |
| 5 Disputes | 5.0, 5–5 | 4.67, 4–5, 0.1 / 3.5 / 4.2 / 5.2 |
| 6 Self-test | 4.75, 4–5, 8.1 | 4.75, 4–5, 4.2 / 6.4 / 11.2 |
| 7 Carry-forward | 5.0, 5–5 | 4.83, 4–5, 4.2 / 9.2 |
| 8 Style | 4.0, 2–5, 2.1 | 4.92, 4–5, 4.2 |
| Mean of the eight | 4.78 | 4.68 |

Rome only, dimensions 9 to 11: Source criticism 4.80 (4–5, two at 4: 1.6 and 2.3, for undated secondary witnesses; n/a for 6.4 and 11.2); Cross-reference integrity 4.92 (one 4: 3.5's loose pointer to 4.3, now fixed); Names and forms 4.92 (one 4: 4.2's Acragas for Agrigentum, now fixed). No false pointer in about 110 pointers opened.

Other measures:
- Factual errors per 1,000 words: Rome 0.11 (4 in 36,459 body words); Greek Fable 0 (0 in 12,297), though the Greek set has a citation slip (6.3) and a quiz slip (8.1) of the same weight as two of Rome's four.
- Length: Rome +12.3 percent over target on average, every report inside the −10/+15 band, the tightest at +7 (5.2) and the loosest at +14 (6.4, 8.3, 9.2, 11.2). Greek Fable +19 percent, two of four outside the band (2.1 at +45, 8.1 at +16).
- Verdicts: Rome 8 pass, 4 revise, 0 rewrite, and all four revises were a handful of exact replacements. Greek Fable by the same rule: 3 pass, 1 revise (2.1 on length alone).

## Is the difference more than noise?

The variation inside the Greek Fable cohort is 0.3 on the overall mean (4.6 to 4.9) and one point on every dimension but Style (three points). The Rome sample's overall means run 4.4 to 4.9, and its mean of the eight shared dimensions is 0.10 below the Greek baseline: inside the Greek spread, so noise. Dimension by dimension the only gap larger than the Greek spread is none; the nearest is Citation, 0.5 below, within the one-point Greek range but systematic (below).

Patterns that are real rather than noise:
1. **Modern works named without title or date.** Nine of twelve Rome reports scored 4 on Citation, almost every time for a surname and year with no title (Beaumont 1939, Ogilvie, Beloch, Tarn 1907, Tipps 1985, Hoyos 1985, Scullard, Momigliano, Breeze, Isaac, Gelzer). The ancient citations are as precise as the Greek ones (book and section throughout). Fixed in the twelve; likely present across the other 46 and worth one mechanical pass (search for a surname followed by a bare year) when they are next touched.
2. **One item thin per report.** Six reports scored 4 on Coverage for a single prompt item given a clause (the Luperci in 2.3, auxiliaries in 6.4, the Wall in 7.3, the coinage dispute in 3.5). The Greek baseline has the same fault in 4.2. Not a cohort difference.
3. **Dispute boxes with one modern side unnamed** (0.1, 4.2) and a box that is a reading rather than a dispute (5.2). Two of twelve; fixed.
4. **Length discipline is better in Rome** than in the Fable-written Greek core, and every Rome sample is in band. (Moot after this session: Pedro ruled on 27 October that the target is a guide and length does not score; it did not change any verdict here, since the four revises were all for errata.)
5. Not found: Livy treated as more reliable than he is (every regal claim carries its reporter and the gap; dimension 9 mean 4.8); retelling of Greek modules (no pointer repeats its target beyond a clause); hedging; weak self-tests (6 mean 4.75, equal to Greek); thinner argument (Depth 4.83 against 5.0, two reports with an inventory section each).

**Does Rome read as if the same author wrote it?** Yes: the same structure, register and citation habits as the Greek core, with one systematic difference, modern works cited by surname and year alone, and a small residue of slips of the kind the quality pass and fresh checkers were catching (a verdict given to an author who withholds it, a date moved a year or two, "more than" for "about").

## Decision (rule fixed in NEXT-SESSION.md on 27 October 2026)

A stratum is cleared on its sample when its mean is at least 4.4 and no report has more than one factual error. All three qualify: 4.76, 4.65 and 4.73, with a maximum of one error per report.

- Stratum 1: the 8 unsampled reports (2.2, 3.1, 3.3, 4.1, 4.4, 5.4, 6.1, 7.2) are marked "Opus 5.5, reviewed with Fable 5.1 (sampled)".
- Stratum 2: the 22 unsampled reports are marked the same.
- Stratum 3: the 14 unsampled reports (8.1, 8.2, 8.4, 8.5, 8.6, 9.1, 9.3, 9.4, 9.5, 10.1 to 10.4, 11.1, 13.1, 13.2) are marked the same.
- Applied with the clearance, since their exact replacements were already verified: the review_notes corrections to 3.1 (Livy's sources "besides Fabius Pictor") and 6.1 (Judge's 1974 reading fits the aureus of 28, published 1999), and the 1.6 auditor's note on 4.1 (its treaty box named Walbank where 1.6 names Beaumont).
- 10.5, the capstone, keeps its flag and is audited on its own, as planned.

Rome reports to fix, in priority order: none outstanding from the sample (all twelve fixed). Follow-ups, in order: 10.5's own audit; the 14.3 overlap checks on the core pairings and on 11.1/11.2 (11.2 repeats about 7 percent of 5.2 to 5.5, 9.2 about 2 percent of 3.4 and 6.4, by the auditors' counts: both well inside the 70-percent rule); a mechanical title-and-date pass over the 44 sampled-clear reports.
