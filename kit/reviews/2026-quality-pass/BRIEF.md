# Quality pass, Rome course: brief for reviewers

Session of 25 October 2026, run with Opus 5.5. This is a quality pass on every Rome report and on the two reshaped syllabi. It is not the Fable review and clears no flag. Reviewers never edit reports: the maintainer verifies each finding before applying it, because reviewers can be wrong.

Working directory: the kit folder (`AGENT-SPEC.md`, `roman-syllabus.html`, `prompts-rome.json`, `provenance.json`, `greece/`, `rome/`). Do not edit any file except your own review files. Never use the Artifact tool or any publishing tool.

## Read first

1. `AGENT-SPEC.md`: the writing spec and the citation conventions.
2. The quality bar, in full: `greece/r-2.1.html`, `greece/r-4.2.html`, `greece/r-6.3.html`, `greece/r-8.1.html`. Note their register: dense, declarative prose; precise citations; dispute boxes of two to four sentences with named sources or scholars on each side; self-test questions that test understanding, with answers of one to three sentences; carry-forward items that are transferable ideas.
3. For each report you review: its prompt (the entry for its id in `prompts-rome.json`, or the `<pre>` of its `data-id` in `roman-syllabus.html`), the report in full, the other reports in your group, the reports either side of your group, and every report your reports point to ("module X.Y", "Greek module X.Y": open the target and check).
4. The writers' unverified lists in `review_notes` in `provenance.json` (units 4 to 6; your task gives the lists for unit 7). Start there.

## What to check, for every report

1. **Coverage.** Every item the prompt names: covered, thin or missing. An item the prompt names but the report hands off by number to a module that owns it counts as covered if the hand-off is explicit.
2. **Accuracy.** Dates, names, numbers, book and chapter citations, and every "X argued Y" about a modern scholar. Use web search to confirm anything doubtful (Perseus, LacusCurtius, Livius.org, Attalus.org, the Loeb text, publishers' pages, JSTOR abstracts). Do not search for what you know; do search before calling something wrong.
3. **Figures.** Every number of dead, troops, money, population or distance says whose figure it is (an ancient author with a citation, or a named modern estimate).
4. **Lanes and pointers.** No retelling of another module's material beyond a sentence; every pointer true of its target; no dispute box or anecdote duplicated in a neighbour without a reason.
5. **Register** against the quality bar: dispute boxes of two to four sentences with names on each side; self-tests that test understanding (and model answers that are correct); carry-forward items that transfer.
6. **House style.** British spelling, no em dashes, no preamble or closing filler, the citation conventions in `AGENT-SPEC.md` (Cicero's treatises by English title, speeches by Latin title, invectives in English; Plutarch's Cato Maior and Cato Minor; Octavian before 27 BC, Augustus after).

## What to return

One Markdown file per report: `reviews/2026-quality-pass/rome-<id>.md`, in this shape:

```
# Rome <id>: <title>

Verdict: keep | fix | rewrite
Body words: N (target T)

## Coverage
- item: covered / thin / missing (one line each)

## Findings
1. [error | should-fix | minor] [accuracy | attribution | figure | pointer | lane | register | style] Section "<h2 heading>".
   Current: "<exact quoted text, short>"
   Problem: <one or two sentences>
   Fix: "<exact replacement text>" (or: delete; or: add after "<anchor>": "<text>")
   Basis: <source checked, with URL or citation; or "not checked: reason">

## Confirmed
- <claims you checked and found right, one per line, with the source; so nobody rechecks them>
```

Severity: **error** = wrong fact, misattribution, false pointer, wrong citation; **should-fix** = unsourced figure, duplication, lane breach, weak or wrong self-test answer, thin coverage; **minor** = style. Verdict: **keep** = no errors; **fix** = a list of edits fixes it; **rewrite** = more than three errors or two of the six checks badly failed.

Proposed fixes must follow the house style (British spelling, no em dashes) and keep the report within its length band (−10 to +15 percent of target). Quote current text exactly, so the maintainer can find it.

Reply with one line per report: id, verdict, and the count of findings by severity. Nothing else.
