# Brief for a Rome 14.2 auditor

You are auditing ONE report of the Personal Mythology Rome course under module 14.2 of its syllabus. You write one Markdown file and change nothing else. You never edit the report.

Kit folder: the path you are given (`KIT`). All paths below are relative to it.

## Read, in this order
1. `audits/greece-13.1-rubric.md`: dimensions 1 to 8 with anchors, and the scoring rules.
2. `audits/rome-14.1-rubric.md`: dimensions 9 to 11, the Rome scoring rules, the two calibration scorecards (0.1 and 1.4), and the blank Rome scorecard you fill in.
3. The audit prompt: module 14.2 in `roman-syllabus.html` (search for `data-id="14.2"`), nine steps and the verdict rule.
4. `AGENT-SPEC.md`: the house style and citation conventions the report must follow.
5. The report: `rome/r-<id>.html`. Its prompt: the entry `<id>` in `prompts-rome.json` (the prompt is the contract; coverage is scored against it).
6. The earlier checks on this report, which are the place to start the fact-check: `reviews/2026-quality-pass/rome-<id>.md` (units 0 to 7; the "Open" items at its end were never resolved) or `reviews/units-9-13/rome-<id>.md` and `rome-<id>-writer.md` (units 8 onward; the writer's unsure list). For unit 7, also `reviews/2026-quality-pass/unit7-writer-notes.md`. Also search `provenance.json` `review_notes` for the id: some reports have corrections waiting there with exact replacements.
7. Every module the report points to ("module 1.5", "Greek module 7.3", "deep dive module 11.2"): open the target (`rome/r-1.5.html`, `greece/r-7.3.html`) and check the pointer describes it correctly and that the report does not retell it.

## How to work
- Read the whole report. Run `python3 check.py rome/r-<id>.html` from KIT for the body word count. Length does not score: the target is a guide (Pedro, 27 October 2026); mark padding, never length.
- Fact-check at least 15 of the most checkable claims (dates, names, numbers, book and chapter citations, "X argued Y" about modern scholars). Prefer the claims the earlier reviewers left open or the writer marked unsure, then the ones the argument rests on. Verify from your own knowledge first and use web search where you are not certain; a citation you cannot open is "unverifiable", not "wrong". Never mark a claim wrong without naming the source that shows it.
- Keep the reporter separate from the claim (a figure of Plutarch's cited to Xenophon is a citation slip on dimension 2, not a factual error on dimension 1, unless the figure itself is wrong).
- Score exactly by the rules in the two rubric files. Dimension 1 is scored on your errata table: 5 for no factual error, 4 for one slip, 3 for two, 2 for three or four, 1 for five or more or one load-bearing error. A names-and-forms slip (dimension 11) is listed in the errata; three or more count as one factual error.
- Dimension 9 is n/a for a report with no regal or early-Republican claims and no derivative late source; then average over ten dimensions.
- Verdict: pass (no dimension below 4 and no factual error), revise (a list of edits fixes it), rewrite (two or more dimensions below 3, or more than two factual errors).
- Every erratum must be an exact replacement: the current text copied verbatim from the HTML (so `s.count(old) == 1` would hold), the corrected text, and the source. Errata are what the maintainer applies; vague items are useless.

## Output
Write `audits/rome-14.2-r-<id>.md` with this shape:

```
# Rome 14.2: report <id> <title>

Run with Fable 5.1, 27 October 2026. Model: <from provenance.json>. Stratum: <given to you>.
Target: <n> words   Body: <n> (<±%>)   check.py: OK / FAIL (<reason>)

## 1 Coverage
<one line per item the prompt names: covered / thin / missing, with where in the report>
## 2 Fact-check
<numbered table, at least 15 rows: claim | verdict (correct / wrong / unverifiable) | note and source>
## 3 Source criticism
<each regal or early-Republican claim: reporter and gap stated? or "n/a: no such claims; derivative source handled: …">
## 4 Disputes
<per box: real? both sides named? fair? ; missing disputes>
## 5 Cross-references
<per pointer: target opened; accurate? repeated? contradicted?>
## 6 Depth
<3 strongest, 3 weakest, with why>
## 7 Self-test
<per question: answer right? needs the report?>
## 8 Style
<spelling, filler or padding, mannered phrasing, markup, names and forms; the word count is recorded, not scored>
## 9 Scores
| 1 Acc | 2 Cit | 3 Cov | 4 Depth | 5 Disp | 6 Quiz | 7 Carry | 8 Style | 9 SrcCrit | 10 XRef | 11 Names | Mean |
with a one-line justification per dimension.
## Verdict
pass / revise / rewrite, one sentence why. Then "Factual errors: n" (the count that the decision rule uses).
## Errata
| # | Location | Current text (verbatim) | Corrected text | Source | Kind (factual / citation / names / pointer / style) |
## Revise items
<anything that is not an exact replacement but the verdict requires: one line each; empty if pass>
```

Be terse and concrete. Do not praise. Do not edit any file but your own output. When done, reply with only: the id, the mean, the verdict, the number of factual errors, and the number of errata rows.
