# Stratified-sample audit of one unit: {CODE} (course PB, Audit {AUDIT})

Date: 14 November 2026. You are one fresh, isolated auditor. Your folder is `{FOLDER}`. Read only inside it; write only inside `{FOLDER}/out/`.

**First line of everything you write and of your final reply:** `Model: <your exact model ID>`. If your model is neither claude-fable-5-2 nor claude-fable-5-1, write that line to `out/audit.md`, change nothing else, and stop.

## What is in the folder
- `unit.md`: the unit you audit ({CODE}; its search flag was {SEARCH}). You never edit it.
- `brief.txt`: its brief (preamble with the reader persona, the course goal, the sourcing rules; Aim, Takes, Gives; the unit brief).
- `sourcing-parts-1-and-5.md`: the sourcing standard, Parts 1 and 5.
- `case-facts.md`: the register of invented facts about Mara Venn, the fictional running example.
- `fresh-check-{CODE}.md`: the earlier fresh-check report on this unit. Its findings were applied before filing. Read it so you do not re-report what was fixed; reuse none of its verdicts.
- `others/`: the other eleven units of the course, only to check this unit's pointers to them ("PB3 §2 shows...").

## Rules
- Nothing in your context outside this folder is a source. Do not use any memory, past-chat, Projects, connector, Artifact or Agent tool, and no tool whose name starts with `mcp__`. Tools you use: Read, Write, Edit, Bash (for `grep`, `wc`, `python3` inside the folder), WebSearch, WebFetch.
- **Web rule.** WebSearch first. WebFetch only a URL that a search in this same agent returned verbatim: never one typed from memory, copied from a file, edited, or reached by a redirect. A site's refusal, redirect or timeout is "not checked" and is never retried or fetched from a copy, cache or mirror. A tool-permission refusal or hold is retried once; if refused again, record it as "not checked: permission" with the URL or tool, and carry on.
- The owner is asleep and has approved every outside read in advance. Never ask a question, never wait for an approval, never call a tool that waits for an answer. Where a choice is open, take the most reasonable reading, record it and go on.
- Write your files as you go, so a restart loses little: record the sample in `out/audit.md` before checking anything, then add each verdict as you reach it. If `out/` already holds working files from a lost run, resume from them and say so in the report.
- A source that cannot be opened is "unverifiable", not FAIL.
- Do not fix the unit; report.

## The audit prompt (docs/method.md §6, verbatim)

{VERBATIM}

## Additions for this run
1. Record the sample before checking anything (one claim per `##` section, including the deliverable and the template where they carry a checkable claim).
2. A source that cannot be opened is "unverifiable", not FAIL. Claims you check beyond the sample while a source is open are listed under "Also checked" and counted in the totals; the decision rule is applied to the sample only.
3. If more than one sampled claim in ten is FAIL, audit this unit in full in this same agent: every cited claim, same procedure. Say so in the verdict.
4. Every correction is an exact replacement: `Current` copied verbatim from `unit.md`, and it must occur exactly once in the unit. Check each with `grep -c -F -- '<current>' unit.md` (it must print 1; a Current must sit on one line). Give the corrected text and the source URL. One erratum per changed passage; if the same wrong figure occurs in several places (body, a `viz` block, the deliverable, the template, Sources), give one erratum for each occurrence, each with enough surrounding text to occur once.
5. Check each `viz` figure: every label, date and number in it against the unit's own text; report each PASS or FIX, a FIX as an exact replacement like any other erratum (mark it `"figure": true`).
6. Check Mara's facts against `case-facts.md`, and the unit's pointers to other units against `others/`. A finding that contradicts another unit or the register, or that could only be settled by changing the brief, is reported with `"kind": "flag"`; it will not be applied as an erratum.
7. Verdict for the unit: PASS / FULL AUDIT RUN, with the result / REWRITE with the sections named. Since you audit one unit, give "the three most consequential errors" for this unit (fewer if there are fewer; "none" is an answer).
8. Count, by reading the unit: its words (`wc -w`), its `##` sections, and the number of cited claims in the whole unit (each sentence or table row that rests a number, date, quotation, attribution or mechanism on a cited source counts once). A full count is wanted, an estimate is not: use a script or tally section by section and show the per-section tallies.

## Output files (all in `out/`)
- `audit.md`: the report. First line `Model: ...`. Then: heading with the unit code, date, search on; Provenance and Sample (recorded first); the table (section, claim, source, verdict, note); Also checked; Not checked (each URL or tool refused, with the reason); failure rate; figures; deliverable; course goal and standard; verdict; the most consequential errors; the bibliography line; the changelog line; Errata (each: id `{CODE}-n`, severity error | should-fix | minor, section, Current, Fix, Basis with URL).
- `errata.json`: a JSON list, one object per erratum or flag: `{"id": "{CODE}-1", "unit": "{CODE}", "kind": "erratum" | "flag", "severity": "error" | "should-fix" | "minor", "verdict": "FAIL" | "STALE" | "other", "section": "...", "current": "...", "fix": "...", "basis": "... with URL", "figure": false}`. `current` and `fix` are the exact strings, with no markdown wrapping added. An empty list is `[]`.
- `claims.json`: a JSON list, one object per claim checked (sampled and also-checked): `{"n": 1, "section": "...", "sampled": true, "kind": "number" | "date" | "quotation" | "attribution" | "mechanism" | "recommendation", "claim": "short", "source": "URL or reference", "verdict": "PASS" | "FAIL" | "STALE" | "unverifiable"}`.
- `stats.json`: `{"unit": "{CODE}", "model": "...", "words": 0, "sections": 0, "cited_claims_in_unit": 0, "claims_sampled": 0, "claims_checked_total": 0, "fail_sampled": 0, "fail_total": 0, "stale_total": 0, "unverifiable_total": 0, "full_audit_run": false, "verdict": "PASS", "web_searches": 0, "web_fetches": 0, "not_checked": ["url or tool: reason"]}`.
- `DONE`: written last, one line with the verdict, only when the three JSON files parse (`python3 -c "import json;[json.load(open(f)) for f in ('out/errata.json','out/claims.json','out/stats.json')]"`) and every erratum's Current has been counted once with `grep -c -F`.

Your final reply is `out/audit.md` verbatim, nothing before its `Model:` line and nothing after the report.
