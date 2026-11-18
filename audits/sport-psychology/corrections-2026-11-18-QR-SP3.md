---
check: corrections check of the findings of quality-review-SP3-2026-11-18.md, W-SP4, 18 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file)
---

Model: claude-opus-5-5
Summary: 7 findings worked. 5 PASS (Changes 1–5), 1 FAIL with an Alt (Change 6), 1 held (Change 7). No syllabus conflicts, no New findings, no Records changes. Every Current below occurs exactly once in files/SP3-motivation-and-the-climate-you-create.md (checked with grep -oF | wc -l: 1 each). I edited no files.

## Change 1
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
Persistent exhaustion, loss of interest in the sport, and a performance slide that rest does not fix are things to notice
```
Replacement:
```
Persistent exhaustion, devaluing the sport and a reduced sense of accomplishment, the three dimensions the footballers' study measured, are things to notice
```
Result: PASS
Quote: Morales-Sánchez et al. 2020, full-text PDF (mdpi-res.com, from search): "physical/emotional exhaustion, sport devaluation and reduced sense of accomplishment."
The problem is real. Nothing opened supports "a performance slide that rest does not fix". The paper's introduction links burnout to "decreased physical performance", but it does not mention rest. "Persistent" is the unit's own coaching word and is not the study's term. The sentence carries "[practice; the course's scope line]", so that word is acceptable.
Syllabus: no conflict. The SP9 brief builds its own signs list ("the signs a coach can see ... of burnout and overtraining, ... each with how long and how much before it is a concern"). It does not take SP3's list. The register is unaffected, and Sara's (fictional) referral line stays.

## Change 2
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
Build a climate low in controlling behaviour and keep loads and rest planned [practice; IOC consensus; the studies behind it were not opened].
```
Replacement:
```
Build a climate low in controlling behaviour [weak, association, for controlling style with need thwarting and burnout in 12- to 17-year-old boys, section 2] and keep loads and rest planned [practice; IOC consensus; the studies behind it were not opened].
```
Result: PASS
Quote: SP1 §9 rule 2: "A claim tested only by correlational studies has no controlled test but is not practice." The new grade matches SP3 §2's table row for Morales-Sánchez 2020 ([weak, association]), and that paper's sample is 103 male players aged 12 to 17 (PDF).
Syllabus: no conflict. It agrees with SP3 §10 and §11 and with SP1's entry (weak, three surveys). F48 (the scope of the inference label) is untouched, because the grade names its sample.

## Change 3
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
one Spanish club, one questionnaire session, convenience sample
```
Replacement:
```
one Spanish club, questionnaires completed before a training session, convenience sample
```
Result: PASS
Quote: Morales-Sánchez 2020 PDF: "The data collection was done before a training session".
The PDF does not say whether this was one sitting. It says the data were collected in May at the end of the 2016–2017 season, and that the sample was "chosen for convenience".
Syllabus: no conflict. SP1's "each measured once" still holds, because the design is cross-sectional.

## Change 4
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
the designs are mixed: cross-sectional, qualitative and one prospective
```
Replacement:
```
the designs are mixed: cross-sectional, qualitative, one mixed-methods and one prospective
```
Result: PASS
Quote: Monteiro et al. 2017, PMC5968952, Table 1, Gould et al. (1982): "Mixed methodology with questionnaire and interview".
The table gives the full split: 2 cross-sectional (Brown 1985; Salguero 2003), 2 qualitative (Fraser-Thomas 2008a, 2008b), 1 prospective (Pelletier 2001) and 1 mixed-methods (Gould 1982).
Syllabus: no conflict.

## Change 5
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
and the authors describe their model as a pattern of associations and do not claim it as a causal mechanism
```
Replacement:
```
and the authors describe their model as a pattern of association rather than a confirmed causal mechanism, though their abstract uses causal wording
```
Result: PASS
Quote: Gu & Cheng 2026, frontiersin.org full text, §4.6: "a pattern of association rather than a confirmed causal mechanism". The abstract says the climate is a "psychological architect" that "influences longer-term behavior". Only part of the page was read: characters 0 to 100,000 of 231,766, which included the abstract and §4.6.
Syllabus: no conflict.

## Change 6
File: files/SP3-motivation-and-the-climate-you-create.md
Current:
```
and pressure with less self-driven motivation
```
Replacement (reviewer's Fix, not applied):
```
and pressure with more motivation that depends on outside pressure, or none at all
```
Result: FAIL (the Fix narrows the source)
Quote: Gao et al. 2024, frontiersin.org full text, reporting Lienhart et al. 2019: "perceived pressure positively predicted maladaptive outcomes (controlled forms of motivation...)".
The problem is real: "less self-driven" blurs the review's finding of more controlled motivation and more amotivation (Sánchez-Miguel 2013: pressure "positively associated with sport amotivation"). But "controlled motivation" covers introjected regulation (guilt, self-worth) as well as external regulation, and SP3 §1 defines both. "Depends on outside pressure" names only the external part. The page was read only to character 100,000 of 221,132. My fetch of the rest was refused, so it is not checked, and any definition of "controlled motivation" in the paper was not seen.
Alt:
```
and pressure with more motivation driven by pressure, guilt or reward, or with none at all
```
The Alt follows SP3 §1's own definitions of introjected and external regulation and matches the unit's §9 summary ("more controlled motivation and amotivation"). Apply only if the caller accepts it as a correction under rule 12.
Syllabus: no conflict. The SP3 brief: "the parents' page SP8 and SP10 extend". The change is to the wording of one line, not to the page's structure.

## Change 7
Change 7: held, not applied. Figure 1 keeps "kind": "range" under F40 (C-SP3). F40 stays open.

Records: none.

Notes
- Web fetches I opened: the Morales-Sánchez PDF (mdpi-res.com), PMC5968952, the Gu & Cheng full text at frontiersin.org, and the Gao full text at frontiersin.org (first part only). One fetch was refused: the second part of the Gao page. It is reported as not checked and was not retried.
- In passing: the Morales-Sánchez PDF reports a mean age of 14.91 with SD 5.56, which is implausible for a 12–17 range. SP3 does not use that figure, so I raise no finding.
