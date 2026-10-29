---
name: audit-units
description: Run a Learning Project audit with Fable 5.1: the four-unit stratified-sample audit, the six-month staleness check, or the per-unit fresh check of a Brand + AI unit. Use when an audit or fresh check is due.
---

# Audit units

Audits check what Opus wrote. They report; they never edit a unit. The procedure is `method.md` §6; the prompts there are used verbatim.

## 1. Check you may run
- The audit runs on Fable 5.1. If you are not Fable 5.1, say so in your first line and stop.
- This is a new chat, or an isolated agent context, used for nothing else (method §4, P31).
- Open `courses-index.md` and identify the audit:
  - **Stratified-sample audit:** the four units written in one hub since its last audit (Brand + AI counts A and B together; Personal Mythology counts its new modules). Never mix hubs in one audit.
  - **Staleness check:** one search-on unit whose six-month date has come.
  - **Fresh check:** one Brand + AI unit, just written, before it is filed (§3b).

## 2. Gather
- The units in full: attached, pasted, or read from their vault paths (`courses-index.md`).
- The course's part of `sourcing-standard.md`, and Part 1.
- Personal Mythology also: the module prompts, `AGENT-SPEC.md`, the writer's unsure lists and the fresh checker's findings where they exist.
If a unit is missing, ask for it; do not audit from memory.

## 3. Run
- **Sample audit:** use the "Stratified-sample audit" prompt in `method.md` §6 exactly as written, with the four codes and paths filled in. Record the sample (one checkable claim per section per unit: a number, a named source, a mechanism or a recommendation) before checking anything. Check each against its source with live search; mark PASS, FAIL or STALE; a source you cannot open is "unverifiable", not FAIL.
- **Decision rule:** a unit with more than one claim in ten FAIL is audited in full, same chat. For a Personal Mythology module the full audit is the kit's scorecard (`audits/AUDIT-BRIEF.md` for Rome, `audits/AUDIT-BRIEF-GREECE.md` for Greece; rubric in `audits/greece-13.1-rubric.md` and `audits/rome-14.1-rubric.md`), with exact-replacement errata. If the sample splits by provenance (units written with and without a checker), say so: the stratum is split and the weaker side is audited in full.
- **Staleness check:** use the "Staleness check" prompt in `method.md` §6 exactly as written. Search today for every fact in the unit that can change.

## 3b. Fresh check of one Brand + AI unit (in force since Audit 1, 28 Oct 2026)
A new Fable 5.1 chat (or isolated agent context) per unit, before filing, that has not seen the unit written. Paste this prompt, then the unit's full text:

> Fresh check of one Brand + AI unit (method.md §5; the §1 override now requires a fresh checker for every Brand + AI unit). You have not seen this unit written. Do not edit it; report. Read sourcing-standard.md Part 1 and Part 2, the unit's brief in units_data.py, and the Audit 1 report (artifact https://claude.ai/artifact/2uA7uLCuUAGRZuUoywpaRj) for the errata it had to apply. Then: (1) Coverage: every item the brief names, covered / thin / missing. (2) Accuracy: open every source the unit cites for a number, a date, a named dataset or an attribution, with live search; confirm the figure, date, sample size and that the claim is what the source says, not a stretch of it; label each PASS / FAIL / unverifiable. Start from the writer's unsure list at the end of the unit. (3) Figures: every number says whose figure it is. (4) Labels: anecdote, vendor and correlational data labelled. (5) Deliverable: present in full, follows from the evidence, usable alone. (6) Errata applied: each Audit 1 erratum that touches this unit is actually applied; pointers to other written units (B1, B2, A9, A2, A6 in the Project knowledge) say what those units say. Output: a findings list, one per line: [error | should-fix | minor] [accuracy | attribution | figure | label | coverage | deliverable | style] section; Current: exact quoted text; Problem; Fix: exact replacement text; Basis: source with URL. Then Confirmed: claims checked and found right, one per line with source. Then one line: unit code, verdict keep | fix | rewrite (keep = no errors; fix = a list of edits fixes it; rewrite = more than three errors), counts by severity. The unit's full text follows.

Before applying any finding, the maintainer saves the checker chat's final report verbatim as `audits/brand-ai/fresh-check-<code>.md`, with the front matter `audits/README.md` sets out. Then the maintainer applies every finding as an exact replacement (each `Current:` string must occur once), adds a line under the unit's unsure list ("Fresh check <date> (Fable 5.1): <verdict> · <counts>; all applied; report `audits/brand-ai/fresh-check-<code>.md`"), and only then files (`file-unit`). A `rewrite` verdict sends the unit back to a new writing chat from its brief.

## 4. Report
Exactly the output the prompt asks for: per-unit tables, failure rates, a verdict per unit (PASS · FULL AUDIT RUN with its result · REWRITE with the sections named, or CURRENT · PATCH · REWRITE for staleness), the three most consequential errors in plain language, one line for the bibliography, one for the changelog. Every correction is an exact replacement: current text copied verbatim (it must occur once in the unit), corrected text, source. No praise, no filler.

## 5. Record
- The course's Audits page in Academy: a log row (date, units sampled, claims checked, failures, verdict, what changed). For Brand + AI, add it to `AUDIT_LOG` in `generator/data/brand-ai/hub.py`, raise `AUDITS_RUN`, set `NEXT_AUDIT`, add a `CHANGELOG` row, rebuild and republish (`file-unit`, step 5). For Personal Mythology, the kit's `audits/` file and `provenance.json` (`"Opus 5.5, reviewed with Fable 5.1"`, or `"… (sampled)"`) as the kit's rules say.
- `courses-index.md`: the audit row's status, the hub's counter reset to 0, any REWRITE noted on the unit's row. Then `python3 kit/index_check.py` (it checks the rows against the vault and the data files; `verify.py` runs it too).
- A REWRITE blocks every new unit until the unit is rewritten in a new chat from its brief. Say so in the last line.
