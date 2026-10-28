# Brief for a Greek 13.2 auditor

You are auditing ONE report of the Personal Mythology Greek course under module 13.2 of its syllabus. You write one Markdown file and change nothing else. You never edit the report.

Kit folder: the path you are given (`KIT`). All paths below are relative to it.

## Read, in this order
1. `audits/greece-13.1-rubric.md`: the eight dimensions with anchors, the scoring rules, the four Fable baselines, and the blank scorecard you fill in.
2. The audit prompt: module 13.2 in `greek-syllabus.html` (search for `data-id="13.2"`).
3. `AGENT-SPEC.md`: the house style and citation conventions the report must follow.
4. The report: `greece/r-<id>.html`. Its prompt: the entry `<id>` in `prompts-greece.json` (the prompt is the contract; coverage is scored against it).
5. Earlier checks, where they exist: unit 12 reports have `reviews/units-9-13/greece-<id>.md` (a fresh checker's findings) and `greece-<id>-writer.md` (the writer's unsure list); units 10 and 11 have none, so start from the report itself. Search `provenance.json` `review_notes` for the id: some reports have shared-passage notes from `crosscheck.py greece`.
6. The curated bibliography `bibliography/greece/r-<id>.md` (written by a Sonnet agent on 27 October 2026, unverified): its "Not resolved" list and "(not verified)" marks tell you which references were hardest to pin down. Treat it as a lead, not an authority.
7. Every module the report points to ("module 4.2", "deep dive module 10.9", "Rome module 3.1"): open the target (`greece/r-4.2.html`, `rome/r-3.1.html`) and check the pointer describes it correctly and that the report does not retell it. Pointers are mostly unnumbered in units 10 and 11 ("the Iliad module") and numbered in unit 12.

## How to work
- Read the whole report. Run `python3 check.py greece/r-<id>.html` from KIT for the body word count. Length does not score: the target is a guide (Pedro, 27 October 2026); mark padding, never length. Dimension 8 is scored on spelling, filler, mannered phrasing, markup and structure only.
- Fact-check at least 15 of the most checkable claims (dates, names, numbers, book and line citations, "X argued Y" about modern scholars). Prefer the claims a checker left open or the writer marked unsure, then the ones the argument rests on. Verify from your own knowledge first and use web search where you are not certain; a citation you cannot open is "unverifiable", not "wrong". Never mark a claim wrong without naming the source that shows it.
- Keep the reporter separate from the claim (a figure of Plutarch's cited to Xenophon is a citation slip on dimension 2, not a factual error on dimension 1, unless the figure itself is wrong).
- Dimension 1 is scored on your errata table: 5 for no factual error, 4 for one slip, 3 for two, 2 for three or four, 1 for five or more or one load-bearing error. Three or more names-and-forms slips (misspelt or inconsistent Greek names) count as one factual error.
- Verdict: pass (no dimension below 4 and no factual error), revise (a list of edits fixes it), rewrite (two or more dimensions below 3, or more than two factual errors).
- Every erratum must be an exact replacement: the current text copied verbatim from the HTML (so `s.count(old) == 1` would hold), the corrected text, and the source. Errata are what the maintainer applies; vague items are useless.

## Output
Write `audits/greece-13.2-r-<id>.md` with this shape:

```
# Greek 13.2: report <id> <title>

Run with Fable 5.1, 27 October 2026. Model: <from provenance.json>. Cohort: Greek Opus (units 10 to 12).
Target: <n> words   Body: <n> (<±%>)   check.py: OK / FAIL (<reason>)

## 1 Coverage
<one line per item the prompt names: covered / thin / missing, with where in the report>
## 2 Fact-check
<numbered table, at least 15 rows: claim | verdict (correct / wrong / unverifiable) | note and source>
## 3 Disputes
<per box: real? both sides named? fair? ; missing disputes>
## 4 Cross-references
<per pointer: target opened; accurate? repeated? contradicted?>
## 5 Depth
<3 strongest, 3 weakest, with why>
## 6 Self-test
<per question: answer right? needs the report?>
## 7 Style
<spelling, filler or padding, mannered phrasing, markup, names and forms; the word count is recorded, not scored>
## 8 Scores
| 1 Acc | 2 Cit | 3 Cov | 4 Depth | 5 Disp | 6 Quiz | 7 Carry | 8 Style | Mean |
with a one-line justification per dimension.
## Verdict
pass / revise / rewrite, one sentence why. Then "Factual errors: n" (the count that the decision rule uses).
## Errata
| # | Location | Current text (verbatim) | Corrected text | Source | Kind (factual / citation / names / pointer / style) |
## Revise items
<anything that is not an exact replacement but the verdict requires: one line each; empty if pass>
```

Be terse and concrete. Do not praise. Do not edit any file but your own output. When done, reply with only: the id, the mean, the verdict, the number of factual errors, and the number of errata rows.
