---
check: corrections check of the findings of quality-review-SP1-2026-11-18.md, W-SP4, 18 Nov 2026
model: claude-opus-5-5 (stated by the agent)
saved: by the main chat verbatim from the agent's reply (the harness refused the agent a report file)
---

Model: claude-opus-5-5
12 findings checked: 11 PASS (Changes 1–9, 11, 12) and 1 FAIL (Change 10, with an Alt). None held. 1 new finding (New 1). No syllabus conflicts. I did not modify the unit, and every Current below still occurs exactly once in files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md. A script counted each one, then applied the passing replacements plus New 1 in order to a copy in memory. Each Current stayed unique as the earlier replacements went in, and once they were all in, no "Abt" or "editorial" was left in the unit.

Web: every address I fetched came back verbatim from a search in this agent. I could not check the PubMed page for Abt et al. (32558628): it served an empty shell, and I did not retry it. No other fetch failed.

## Change 1
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
Replace "just relax" with a specific, practised cue that says what to do [weak, positive; for a 17-year-old an inference, the review's samples being mostly adults; the ironic-effects review in section 8 tested instructions about what to avoid; a meta-analysis of self-talk in sport that tests such cues was not opened for this unit, and SP5 grades it]
```
Replacement:
```
Replace "just relax" with a specific, practised cue that says what to do [practice; the studies behind it were not opened: the ironic-effects review in section 8 tested instructions about what to avoid, and a meta-analysis of self-talk in sport that tests such cues was not opened for this unit; SP5 grades it]
```
Result: PASS. On the repository page (acikerisim.uludag.edu.tr/.../full), the abstract says the review covers instructions to avoid. It does not mention relaxation or self-talk. No source opened for the unit tests a "do this" cue. That makes practice, with the F14 note, the convention.
Quote: "cognitive load-induced avoidant instructions" (Bartura et al., abstract, Uludağ repository page)
Syllabus: no conflict. This follows F14 (carried), and SP5's brief still grades self-talk ("self-talk (instructional and motivational, matched to the task)"). The next sentence's ironic-effects grade [weak, positive], which F6 relies on, is unchanged.

## Change 2
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
"q": "Failed replication, or reviews that disagree?"
```
Replacement:
```
"q": "Pre-registered or multi-site replication failed, or two reviews reach opposite conclusions?"
```
Result: PASS. Checked against the unit itself: section 9's rule 1 and the contested row of Deliverable C. The figure now asks no broader question than the rule does. I could not check whether kit/viz.py fits the longer label, because that file is outside the folder.
Quote: "Contested if a pre-registered or multi-site replication failed to find an effect" (unit §9, rule 1)
Syllabus: no conflict. This matches F8's rule as written.

## Change 3
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
**The studies are small.** An editorial in the *Journal of Sports Sciences* reported that in a random sample of 120 papers submitted to the journal, the median sample size was 19, and only 12 of the 120 reported a power calculation made before the study ([Abt et al., 2020, editorial, reporting the editors' own audit of submissions; not a listed source type](https://doi.org/10.1080/02640414.2020.1776002)). The sample covers sport and exercise science as a whole. The editorial explains that small samples miss real effects more often, overestimate the effects they do find, and replicate less often. Inside sport psychology,
```
Replacement:
```
**The studies are small.** Inside sport psychology,
```
Result: PASS on the standard. The unit itself says the editorial is "not a listed source type", and Part 7 item 2 lists the only types allowed. I could not open the editorial's figures at PubMed, but this does not matter for a cut. After the cut, "Inside sport psychology" has nothing to contrast with. It still reads correctly.
Quote: "Each source is one of: a consensus or position statement ... a systematic review" (sourcing-standard Part 7)
Syllabus: no conflict, and no brief quotes these figures. The SP1 brief asks "why most studies are small". Section 5 still shows that they are small, with Rupprecht et al.'s sample counts. The consequences sentence (small samples miss effects and overestimate them) goes with the cut. If the maintainer wants it back, it needs an accepted source.

## Change 4
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
- Abt G, Boreham C, Davison G, Jackson R, Nevill A, Wallace E, Williams M. Power, precision, and sample size estimation in sport and exercise science research. *Journal of Sports Sciences* 2020;38(17):1933–1935. https://doi.org/10.1080/02640414.2020.1776002 (editorial; authors, title, volume and pages not shown on the page opened, taken from a university repository record: not verified)

```
(The Current includes the line's trailing newline.)
Replacement:
```
```
Result: PASS once Change 3 is applied, because nothing else in the unit cites Abt. Apply it only together with Change 3.
Quote: "nothing is listed that it does not cite" (sourcing-standard Part 1)
Syllabus: no conflict. Abt is not in the course bibliography (files/bibliography.md), and no brief names it.

## Change 5
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
*g* = 0.99 (95% CI 0.68 to 1.30), with low certainty (
```
Replacement:
```
*g* = 0.99 (95% CI 0.68 to 1.30), with certainty the authors rate low to very low (
```
Result: PASS. The certainty wording comes from the abstract on mdpi.com/2076-328X/14/3/207. That page's abstract does not show g = 0.99 or its confidence interval, so I did not re-verify those numbers here, and the change does not alter them.
Quote: "in improving service accuracy and technique in tennis players is low to very low" (Deng et al., abstract)
Syllabus: no conflict.

## Change 6
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
Dani is 14: the sample includes her band.
```
Replacement:
```
Dani is 14: the sample's youngest band (10 to 14) includes her age.
```
Result: PASS. In Hu et al.'s Methods (frontiersin.org/.../fpsyg.2023.1106916/full) the bands are 10–14 (n = 32), 15–19, 20–24 and 25 and over, 252 in total.
Quote: "Participants were aged in their 10–14 years old (n = 32, 12.7%)" (Hu et al., Methods)
Syllabus: no conflict. Dani is 14 in case-facts.md.

## Change 7
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
I raise the concern with her parents and with the person below.
```
Replacement:
```
I raise the concern with the person below, and with her parents as that person advises.
```
Result: PASS. This is a scope fix and needs no outside source. The card's own question ("Who may I speak to about a minor's health, and with whose consent?") is left open, so the card should not commit to telling the parents first.
Quote: "Who may I speak to about a minor's health, and with whose consent?" (unit, Dani's card)
Syllabus: no conflict. SP9's brief leaves the timing to SP9 ("the limits of confidentiality with a minor, and when parents are told"). DD-SP2's line ("with a parent for a minor") is about the weight-class decision and is not affected. F9's "noticed and referred, with no comment on weight" still holds.

## Change 8
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
Grade: [contested] by rule 1.
```
Replacement:
```
Grade: [contested, no effect shown in the preregistered analyses] by rule 1.
```
Result: PASS. Source: the Vohs et al. record at digitalcommons.unf.edu/unf_faculty_publications/1132. The direction is narrowed to the preregistered analyses, which is accurate: the exploratory analysis found d = 0.08. Deliverable C's list of directions says "no benefit shown", while this wording follows the unit's existing "no effect shown" (the power-pose entries).
Quote: "Hence, preregistered analyses did not find evidence for a depletion effect." (Vohs et al., abstract, UNF record)
Syllabus: no conflict.

## Change 9
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
for sport performance, no peer-reviewed source found [contested].
```
Replacement:
```
for sport performance, no peer-reviewed source found [contested, no effect shown in the preregistered analyses].
```
Result: PASS, for the same reason as Change 8.
Quote: "preregistered analyses did not find evidence for a depletion effect" (Vohs et al., UNF record)
Syllabus: no conflict.

## Change 10
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
the associations with competitive performance in that review are mixed and mostly cross-sectional [weak, positive, for an association]
```
Replacement (the reviewer's, not applied):
```
the associations with competitive performance in that review are mixed and mostly cross-sectional [weak, positive for physical activity, mixed for competitive performance; associations only]
```
Result: FAIL. The finding says the review calls the competitive-performance results mixed, and it does not. On frontiersin.org/.../fspor.2025.1563382/full I read the whole page in two parts. "Mixed" appears only about sex as a moderator and in one reference title. The abstract reports positive relationships "in competitive settings". The exceptions are in the Results: one study found no difference in grit between international and national wrestlers, and another found no difference in resilience across levels. The current grade [weak, positive, for an association] agrees with the review. The unit's own word "mixed" is what overstates.
Alt Current:
```
the associations with competitive performance in that review are mixed and mostly cross-sectional [weak, positive, for an association]
```
Alt Replacement:
```
the review reports mostly positive associations with competitive performance, with exceptions, in mostly cross-sectional studies [weak, positive, for an association]
```
Quote: "Most of the studies found positive relationships between grit, resilience, and PA outcomes" (Martin et al., abstract)
Syllabus: no conflict, for the finding or the Alt. Note for the maintainer, with no change proposed: section 7's sentence "while others found no association or mixed results" covers the review as a whole. The "no association" results there are about resilience and physical activity, not grit and competition. Check it at the next pass.

## Change 11
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
the five jobs rest on the IOC tools' abstract, one meta-analysis and one study.
```
Replacement:
```
the five jobs rest on the IOC tools' paper (full text read 18 Nov 2026), one meta-analysis read in abstract and one survey.
```
Result: PASS. Today, PMC7788187 serves the full text (Methods, Results, Discussion; the reference list is cut off). The unit's Sources list gives Brown & Fletcher as "abstract read". Hu et al. is a cross-sectional survey.
Quote: "was developed for athletes and their entourage" (Gouttebarge et al., PMC7788187)
Syllabus: no conflict. F3 still stands: the Delphi study is not opened.

## Change 12
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
*Psychological Science* 2021. https://doi.org/10.1177/0956797621989733
```
Replacement:
```
*Psychological Science* 2021;32(10):1566–1581 (volume, issue and pages from a university repository record, https://digitalcommons.unf.edu/unf_faculty_publications/1132, read 18 Nov 2026; not the publisher's record). https://doi.org/10.1177/0956797621989733
```
Result: PASS. The UNF record gives the full citation, including 32(10), 1566–1581. The entry's existing note ("co-authors, volume and pages not shown on the page opened: not verified") is still true of the APS page and can stay. The record also lists co-authors (Schmeichel, Lohmann, Gronau, ...), but the fix does not add them, and I have not either.
Quote: "Psychological science, 32(10), 1566–1581" (UNF record)
Syllabus: no conflict.

## New 1
File: files/SP1-what-a-coach-can-do-and-how-to-tell-evidence-from-noise.md
Current:
```
J Sports Sci editorial (authors, headline), tennis imagery meta-analysis (author surnames), Rupprecht et al. (title, authors, year, volume, issue, pages from the seed list), Reinebo et al. (issue number), Vohs et al. (co-authors, volume, pages)
```
Replacement:
```
tennis imagery meta-analysis (author surnames), Rupprecht et al. (title, authors, year, volume, issue, pages from the seed list), Reinebo et al. (issue number), Vohs et al. (co-authors; volume, issue and pages from a university repository record, not the publisher's)
```
Result: PASS. This is item 7 of the Unsure list. After Changes 3 and 4 the editorial is no longer cited, and after Change 12 the volume and pages come from the UNF record. Apply only if Changes 3, 4 and 12 are applied.
Quote: "Psychological science, 32(10), 1566–1581" (UNF record)
Syllabus: no conflict.

## Records
None. No reading-page known-gaps text needs changing beyond what is above.
