# Checker brief: new reports (Rome units 8 to 13, Greek unit 12)

Sessions from 25 October 2026, run with Opus 5.5. Each new report gets one fresh checker that has not seen it written. This is not the Fable review and clears no flag. Checkers never edit reports: the maintainer verifies each finding before applying it, because checkers can be wrong.

Working directory: the kit folder (`AGENT-SPEC.md`, `WRITER-BRIEF.md`, `roman-syllabus.html`, `greek-syllabus.html`, `prompts-rome.json`, `prompts-greece.json`). The reports are Markdown files in the vault beside it, `../courses/greece/<id>-<slug>.md` and `../courses/rome/<id>-<slug>.md` (P71-3, 1 November 2026); read them there. Do not edit any file except your own findings file. Never use the Artifact tool or any publishing tool.

## Read first

1. `AGENT-SPEC.md`: the writing spec, the content rules and the citation conventions for the report's course (Rome, or Greece with the philosophy conventions: Diels–Kranz, Stephanus, Bekker, *SVF*, Diogenes Laertius by book and section).
2. The quality bar, in full: Greek 2.1, 4.2, 6.3 and 8.1 (`../courses/greece/2.1-*.md` and so on; for Greek philosophy also 6.5 and 7.2). Note their register: dense, declarative prose; precise citations; dispute boxes of two to four sentences with named sources or scholars on each side; self-test questions that test understanding, with answers of one to three sentences; carry-forward items that are transferable ideas.
3. For the report you check:
   - its prompt: the `<pre>` of its `data-id` in the course syllabus (`roman-syllabus.html` for Rome, `greek-syllabus.html` for Greece);
   - the report in full (its vault file);
   - the prompts of its neighbours in the unit, and the written neighbours themselves;
   - every report it points to ("module X.Y", "Greek module X.Y", "Rome module X.Y", "deep dive module X.Y"): open the target and check that it says what the pointer claims. A pointer to an unwritten module is checked against that module's prompt;
   - the lane note in your task: the hand-offs written reports make to this module. Check that the report keeps each one (covers what was handed to it, and does not retell what the earlier report already told);
   - the writer's list of unsure claims, `reviews/units-9-13/<course>-<id>-writer.md`. Start there.

## What to check

1. **Coverage.** Every item the prompt names: covered, thin or missing. An item handed off explicitly by number to the module that owns it counts as covered.
2. **Accuracy.** Dates, names, numbers, book and chapter citations, and every "X argued Y" about a modern scholar. Use web search to confirm anything doubtful (Perseus, LacusCurtius, Livius.org, Attalus.org, the Stanford Encyclopedia of Philosophy, the Loeb text, publishers' pages, JSTOR abstracts). Do not search for what you know; do search before calling something wrong.
3. **Figures.** Every number of dead, troops, money, population or distance says whose figure it is.
4. **Lanes and pointers.** No retelling of another module's material beyond a sentence; every pointer true of its target; no dispute box or anecdote duplicated in a neighbour without a reason.
5. **Register** against the quality bar: dispute boxes of two to four sentences with names on each side; self-tests that test understanding, with answers that agree with the body; carry-forward items that transfer.
6. **House style.** British spelling, no em dashes, no preamble or closing filler, the citation conventions in `AGENT-SPEC.md`. Rome: Octavian before 27 BC, Augustus after; Cicero's treatises in English, speeches in Latin; Dio by Loeb book with Boissevain's in brackets where they differ. Greece: Greek name forms; fragments quoted from the edition cited; the doxographer kept separate from the philosopher.

Recurring slips from the last quality pass, worth a deliberate look: a modern book's year or title not matching the edition named; an ancient author cited for what only a later author says; a Self-test answer contradicting the body; a dispute box with nobody named on one side; a figure with no source; a pointer that misdescribes its target.

## What to return

One Markdown file: `reviews/units-9-13/<course>-<id>.md` (for example `rome-8.1.md`, `greece-12.3.md`), in this shape:

```
# <Course> <id>: <title>

Verdict: keep | fix | rewrite
Body words: N (target T)

## Coverage
- item: covered / thin / missing (one line each)

## Findings
1. [error | should-fix | minor] [accuracy | attribution | figure | pointer | lane | register | style] Section "<## heading>".
   Current: "<exact quoted text, short, copied from the file>"
   Problem: <one or two sentences>
   Fix: "<exact replacement text>" (or: delete; or: add after "<anchor>": "<text>")
   Basis: <source checked, with URL or citation; or "not checked: reason">

## Confirmed
- <claims you checked and found right, one per line, with the source; so nobody rechecks them>
```

Severity: **error** = wrong fact, misattribution, false pointer, wrong citation; **should-fix** = unsourced figure, duplication, lane breach, weak or wrong self-test answer, thin coverage; **minor** = style. Verdict: **keep** = no errors; **fix** = a list of edits fixes it; **rewrite** = more than three errors or two of the six checks badly failed.

Proposed fixes must follow the house style (British spelling, no em dashes) and keep the report within its length band (−10 to +15 percent of target; `python3 check.py <path>` prints the count). Quote current text exactly as it stands in the file, including any Markdown inside the span (`*Aeneid*`, `**Where sources disagree.**`), so the maintainer can find it with an exact match.

Reply with one line: id, verdict, and the count of findings by severity. Nothing else.
