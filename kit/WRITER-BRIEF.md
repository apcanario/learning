# Brief for report writers

Give this file, plus the module's id, output path, target length and any extra files to read, to each writer. Writers run in parallel, one module each.

You are writing one report for a course in Personal Mythology, a self-study compendium of long-form reports on history and mythology. Greece is course 1 and is complete (78 reports). Rome is course 2: units 0 to 10, 11.1, 11.2, 13.1 and 13.2 (59 reports) are written; 11.3 to 11.8, 12.1 to 12.8 and 13.3 to 13.8 remain. Your report must read as if the same author wrote the Greek core.

Working directory: the kit folder (it contains `AGENT-SPEC.md`, `check.py`, the syllabi, `greece/` and `rome/`). Do not edit any file there except your own report, your notes file and your bibliography file (below).

## Read first, in full
1. `AGENT-SPEC.md`: the writing spec. Follow it exactly: fragment rules, allowed elements, dispute boxes, the Self-test and Carry forward format, and the rules for your course.
2. The quality bar: `greece/r-4.2.html`, `greece/r-6.3.html`, `greece/r-8.1.html` (the Fable review's baseline, scored in `audits/greece-13.1-rubric.md`), plus the extra files named in your task. Match their register: dense, declarative, mostly short sentences; precise citations (author, work, book.chapter or line); dispute boxes of two to four sentences with named sources or scholars on each side; tables only for genuinely tabular material; self-test questions that test understanding rather than trivia, with answers of one to three sentences that cite where apt; carry-forward items that are transferable ideas, one or two sentences each.
3. Your prompt is the `<pre>` of your module (`data-id="<id>"`) in the course syllabus: `roman-syllabus.html` for Rome, `greek-syllabus.html` for Greece. It is your contract: cover every item it names.

## Stay in your lane
- The other modules of your unit are being written at the same time. Read their prompts in the syllabus so you know their scope; do not cover their material beyond a sentence, and hand off by number ("module 2.3").
- Reports already written for your course are in its folder (`rome/r-<id>.html`). Skim the ones your task names; point back to them instead of repeating them.
- Where your prompt points back to a Greek module, open `greece/r-<id>.html` to see what it already covers, then point back ("Greek module 7.3") instead of retelling it. Greek reports point to Rome as "Rome module 13.2".
- Your task's lane note quotes what written reports already say about your module. Those hand-offs are promises your report must keep; check each against its report before relying on it.

## Rules that matter most
- Accuracy first. Never invent a citation. If you are not sure of a chapter or line number, cite the author and work only. Use web search to check a date or a contested scholarly point when you are genuinely unsure; do not search for things you know. Do not put words in quotation marks unless you are sure of the wording.
- Length: the target in your prompt is a guide, not a limit. Write what the topic needs, whether that is 2,000 words or 6,000; never pad, never cut substance to hit a number. Plan section budgets first and write the file in one pass. `check.py` notes the count against the target; it does not fail on it.
- No em dashes: the house style uses colons, semicolons and commas. En dashes only in number ranges (1.7–9, 753–509 BC). No emoji.
- British spelling. No preamble, no closing filler. Begin with the first `<h2>`.
- Figures: after the draft is written, go through it section by section and ask whether the content has a shape. Where it does, declare a figure of the matching kind (dated events: timeline; a sequence: flow; a hierarchy or line of descent: tree; numbers compared: compare or bars; a trend over time: line; two measures: scatter; competing estimates: range; a rule with branches: decision; items by sections: matrix; a lifecycle: states; the full table, with every kind, is `skills/write-unit/SKILL.md` §4b). Where nothing has a shape, declare nothing; one to four figures a report is a guide. Declare it, never draw it: `<figure class="viz" data-viz="timeline"><script type="application/json">{…}</script><figcaption>…</figcaption></figure>`, the fields as in `viz.py`'s docstring, placed directly after the paragraph or table it draws; `build.py` draws it. Every date, number and name in it must already be in your sourced text, and the caption says what it shows and where its data comes from (module section, ancient author and passage, or modern work). `check.py` parses and draws every declaration, fails any other figure or script, and leaves figures out of the word count. `rome/r-0.3.html` has the worked example (the anchor dates as a timeline).
- Never use the Artifact tool or any publishing tool: edit your file on disk only. Publishing is the maintainer's job, and a stray publish creates a page on the owner's account.
- **Lessons from the last quality pass (41 errors in 39 reports):**
  - Name a modern scholar for a view only when you are sure that scholar argued it; otherwise state the view unnamed, or search.
  - Every number of dead, troops, money or people names its source.
  - Neighbours must not repeat each other's dispute boxes and anecdotes: each has one home, the others point to it.
  - Open a report before writing "module X covers Y".
  - Recurring slips: a modern book's year or title not matching the edition named; an ancient author cited for what only a later author says; a Self-test answer contradicting the body; a dispute box with nobody named on one side; Dio's Loeb and Boissevain book numbers confused.
  - Philosophy: quote fragments only from the edition you cite, and keep the reporter separate from the claim ("Aristotle says Thales held …").
- Other writers share your scratch folder. Name any temporary file after your module (`tmp-2.3-body.html`, never `body.html`), and before you finish confirm that your report's Self-test and Carry forward are about your module.

## When the file is written
Run `python3 check.py <course>/r-<id>.html` from the kit folder. Fix every HARD failure and any genuine soft warning (a US spelling, preamble), then re-run until it prints OK.

Then write your notes file, `reviews/units-9-13/<course>-<id>-writer.md`: up to ten lines listing the claims you were unsure about or could not verify (citations, figures, attributions to modern scholars), one per line. The checker starts there.

Then write your bibliography, `bibliography/<course>/r-<id>.md` (Pedro's rule, 27 October 2026: every unit keeps its sources for future checks). Two lists. **Ancient sources:** every ancient author and work you cite, one line each, with the edition or translation you relied on where you know it and the passages used. **Modern works:** every modern work you cite or drew on, one line each, with author, full title, place or journal, and year of the edition you name. Nothing that is not in the report; nothing in the report that is not here. `biblio.py` extracts a machine list from the report on every build (`bibliography/<course>/unit-<n>.md`) and links to yours; yours is the one that counts.

Reply with only: the final check.py output line, and the same list. Do not paste the report.
