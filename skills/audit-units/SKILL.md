---
name: audit-units
description: "Run a Learning Project check: the fresh check of one new unit before filing, or the six-month staleness check of a search-on unit. Use when a fresh check or a staleness check is due."
---

# Check units

Checks report; they never edit a unit. The procedure is `method.md` §5 (fresh check) and §6 (staleness check); the prompts are used verbatim. The four-unit Fable audit is retired: the Fable stage closed on 15 Nov 2026 (S-NOAUDIT), and no Fable audit or Fable fresh check runs. The audit reports already in `audits/` and `kit/audits/` stay as the record.

**The course's entry.** Every course is one entry, `courses/<id>/course.toml`, read by `kit/courses.py` (S-DEC1). For a markdown course (Brand + AI, User Experience, any new one) the entry gives the paths used below: `id` (its fresh-check reports go in `audits/<id>/`), `data` (the course's `hub.py`; its `units_data.py` sits in the same folder), `vault` (the filed units) and `sourcing_part` (its own part of `sourcing-standard.md`; without the key, Part 2 for a markdown course and Part 3 for a history course, as `kit/howbuilt.py` has it). Below, `<id>`, `<data>`, `<data folder>`, `<vault>` and `<sourcing part>` mean those values for the unit's course; no step names one course's folders.

## 1. Check you may run
- The check runs on Opus 5.5. If you are not, say so in your first line and stop.
- This is a new chat, or an isolated agent context, used for nothing else, that has not seen the unit written (method §4, P31).
- Identify the check:
  - **Fresh check:** one unit, just written, before it is filed (§3).
  - **Staleness check:** one search-on unit whose six-month date has come (`courses-index.md`, the staleness table).

## 2. Gather
- The unit in full: attached, pasted, or read from its vault path (`courses-index.md`).
- `<sourcing part>` of `sourcing-standard.md`, and Part 1.
- Personal Mythology also: the module prompt, `AGENT-SPEC.md`, the writer's unsure list (its fresh check is `method.md` §5, briefed with `kit/reviews/units-9-13/BRIEF.md`).
If the unit is missing, ask for it; do not check from memory.

## 3. Fresh check of one markdown-course unit (§3b in older prompts; Brand + AI since 28 Oct 2026, User Experience from IA1)
A new Opus 5.5 chat (or isolated agent context) per unit, before filing, that has not seen the unit written. Fill the braces from the course's entry (`{sourcing part}`; `{data folder}`; `{audit errata}`: every audit report in `audits/<id>/` (`audit-*.md` or `.html`; Brand + AI's Audit 1 is also the artifact https://claude.ai/artifact/2uA7uLCuUAGRZuUoywpaRj), the record of the audits run before the Fable stage closed, or, when there is none, "no audit report: skip it") and paste the prompt, then the unit's full text:

> Fresh check of one markdown-course unit (method.md §5; the §1 override now requires a fresh checker for every unit of a markdown course). You have not seen this unit written. Do not edit it; report. Read sourcing-standard.md Part 1 and {sourcing part}, the unit's brief in {data folder}/units_data.py, and {audit errata} for the errata it had to apply. Then: (1) Coverage: every item the brief names, covered / thin / missing. (2) Accuracy: open every source the unit cites for a number, a date, a named dataset or an attribution, with live search; confirm the figure, date, sample size and that the claim is what the source says, not a stretch of it; label each PASS / FAIL / unverifiable. Start from the writer's unsure list at the end of the unit. (3) Figures: every number says whose figure it is. (4) Labels: anecdote, vendor and correlational data labelled. (5) Deliverable: present in full, follows from the evidence, usable alone. (6) Errata applied: each erratum of those audit reports that touches this unit is actually applied; pointers to other written units (the course's filed units in the Project knowledge) say what those units say. Output: a findings list, one per line: [error | should-fix | minor] [accuracy | attribution | figure | label | coverage | deliverable | style] section; Current: exact quoted text; Problem; Fix: exact replacement text; Basis: source with URL. Then Confirmed: claims checked and found right, one per line with source. Then one line: unit code, verdict keep | fix | rewrite (keep = no errors; fix = a list of edits fixes it; rewrite = more than three errors), counts by severity. The unit's full text follows.

**Figures (P41, 29 Oct 2026).** When the unit declares figures (` ```viz ` blocks), paste this paragraph after the prompt above, before the unit's text, and the checker adds a section (7) to its output: "(7) Figures: for each ```viz block, in order: its kind and the section it sits in; every label, date and number in it traced to the unit's own text (quote the line), any that is not there is an error; the caption says what the figure shows and names the section and the source the data comes from, otherwise should-fix; the kind fits the shape of the data (dated events: timeline; a sequence: flow; a hierarchy: tree or sitemap; numbers compared: compare or bars; a trend: line; two measures: scatter; competing estimates: range; a rule with branches: decision; items by sections: matrix; a lifecycle: states; a journey across actors: swimlanes; screens: wireflow; things and relationships: objects), otherwise should-fix with the kind it should be. Report each figure PASS or FIX, a FIX with the exact replacement JSON or caption." A figure finding is applied like any other, as an exact replacement; after a second FIX the figure is fixed against both reports and checked a third time; a figure that fails its third check is fixed against every report so far and checked again by a new agent, as many times as it takes, and is never dropped (Pedro, 3 Nov 2026, 09:40: "Don't drop figures, they need to succeed"; until then P85 and every later row dropped a figure that failed its third check). A figure fixed after a FIX is re-checked by a new agent given the unit's text with its figures taken out, the captions and the figure as the reader sees it: `python3 verify.py --shots <dir> --page <panel id>` saves, for each figure, its opening frame and a sheet of every frame a reader scrolls it across, half a frame apart, phone and desktop, dark and light (`<width>-<panel>-fig-<nn>-<kind>-frames-<theme>.png`, P89, 2 Nov 2026).

Before applying any finding, the maintainer saves the checker chat's final report verbatim as `audits/<id>/fresh-check-<code>.md`, with the front matter `audits/README.md` sets out. Then the maintainer applies every finding as an exact replacement (each `Current:` string must occur once), adds a line under the unit's unsure list ("Fresh check <date> (<model>): <verdict> · <counts>; all applied; report `audits/<id>/fresh-check-<code>.md`"), and only then files (`file-unit`). A `rewrite` verdict sends the unit back to a new writing chat from its brief.

## 4. Staleness check
Use the "Staleness check" prompt in `method.md` §6 exactly as written, with live search. Search today for every fact in the unit that can change. Output: the table the prompt asks for and a verdict, CURRENT · PATCH (the lines to change, each an exact replacement: current text copied verbatim, it must occur once, corrected text, source) · REWRITE (the sections). No praise, no filler.

## 5. Record
- Fresh check: the report saved as above; the unit filed by `file-unit`.
- Staleness check: save the report as `audits/<id>/staleness-<code>-<yyyy-mm-dd>.md`; apply a PATCH as exact replacements with a dated erratum note in the unit; add a `CHANGELOG` row in `<data>` and bump `VERSION`; record the check and the next due date in `courses-index.md`, then `python3 kit/index_check.py`; rebuild and republish (`file-unit`, step 5).
- A REWRITE blocks every new unit until the unit is rewritten in a new chat from its brief. Say so in the last line.
