I'm continuing a self-study project called **Personal Mythology**: a compendium of courses on the history and mythology of different cultures, published as one claude.ai artifact. Greece (course 1) is complete; Rome (course 2) has 59 of 79 reports. Everything written with Opus 5.5 is flagged for review with Fable 5.1. All 59 Rome reports and 72 of the 78 Greek reports are reviewed; **six Greek reports are still flagged: 11.1, 11.2, 11.4, 11.5, 11.6, 11.8.** This session finishes the review. It must run on Fable 5.1; if it is not, say so and stop.

## What I've attached

- `personal-mythology-kit.zip`. Unzip it into its own folder and read, in this order: `README.md`, `FABLE-REVIEW.md` (the queue; it opens with the review alert), the last two entries of `review_notes` in `provenance.json`, `audits/greece-13.4-cohorts.md` (the interim cohort decision and why the stratum was split), `audits/AUDIT-BRIEF-GREECE.md` (the brief each auditor agent gets) and one Greek scorecard as a model (`audits/greece-13.2-r-10.8.md`). Run `python3 build.py` and confirm it reproduces `personal-mythology.html` byte for byte before changing anything.

The live artifact is https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH (update it, never create a new one; read it with the Artifact tool first). The Rome syllabus is published at https://claude.ai/artifact/AEgHdAEpeLo1rtfBcuBbVy and the Greek syllabus at https://claude.ai/artifact/EdV1Nkt9HVEoApdMstbANm; republish either only if it changes. Publishing works best delegated to one small agent per page (read the page, publish the local file once with its `url`, never retry or force).

## Done on 27 October 2026 (sessions 1 to 3 of the review): don't redo

1. **Greek 13.1, Rome 14.6, 14.1** (session 1), **Rome 14.2, 14.5, 14.4** (session 2): every Rome report reviewed; no Rome report is flagged.
2. **Session 3:** curated bibliographies for all 137 reports (Sonnet 5.5 agents; `bibliography/<course>/r-<id>.md`; flagged in `artefacts`). Greek 13.2 sample (10.4, 10.9, 11.3, 11.7, 12.1, 12.6) audited; the stratum split under 13.4: unit 12's unsampled six cleared "(sampled)", units 10 and 11 audited in full. Done and cleared: 10.4, 10.7, 10.8, 10.9, 10.10, 10.11, 10.12, 11.3, 11.7, 12.1, 12.6, every erratum and revise item applied. Rome 14.3 (16 pairs) and Greek 13.3 (six repeated disputes homed; six high-signal pairs read): all pass; fixes applied. Three report slips from the bibliography agents fixed.
3. Every correction that was waiting is applied. No report fails `check.py` (length is advisory).

## The order of work now

4. **Finish Greek 13.2 and 13.5 on the six flagged reports: 11.1, 11.2, 11.4, 11.5, 11.6, 11.8.** One fresh agent per report with the prompt: "KIT = <path>. Read KIT/audits/AUDIT-BRIEF-GREECE.md first and follow it exactly. Audit Greek report <id>. Write KIT/audits/greece-13.2-r-<id>.md. Change nothing else. Note from the maintainer: the sample found dispute boxes with unnamed sides to be the cohort's systematic weakness; give each box's named parties particular attention, and make every fix an exact replacement with a reference you are sure of (never invent one)." At most five at once. Apply each scorecard's errata yourself as exact replacements (the errata table parses mechanically: copy the pattern used in session 3, `s.count(old)==1` then replace), then the revise items by hand, run `python3 check.py greece/r-<id>.html`, and set the report's `provenance.json` entry to `"Opus 5.5, reviewed with Fable 5.1"`. Verify any reference an auditor supplies that you are not certain of before writing it into a report; where no modern name can be given with certainty, recast the box around the ancient evidence rather than invent a name. Known pointer work from 13.3 to fold in when 11.5 and 11.6 are open: 11.5's Callisthenes box should point to 11.7 (the home); 11.5 is the home for Iollas/Antipater, Opis (Tarn against Badian) and the "reign of terror"; 11.6 is the home for Spann on the Hyphasis and the Gedrosia losses; 11.7's Mallian-town box is the home and 11.6's should point to it.
5. **Update `audits/greece-13.4-cohorts.md`** with the six new scorecards (the table, the per-dimension means, the decision line), and `FABLE-REVIEW.md` will then show no flagged report. Rebuild and publish.
6. **Fable spot-check of the curated bibliographies** (clears the `artefacts` flag): pick one Rome and two Greek units, open every "(not verified)" reference in their `r-<id>.md` files by web search, correct or confirm, note the hit rate in `audits/bibliography-spot-check.md`, and set the entry to `"Sonnet 5.5, spot-checked with Fable 5.1 (sampled)"` if the error rate is under about one in ten; otherwise say what is wrong and leave it flagged.
7. **Greek 13.3, the rest** (lower priority; the 32 pairs with no mechanical signal): read them in groups of six with `audits/OVERLAP-BRIEF.md` and `audits/overlap.py` for the figures, if the session has room. The pairs are in the Greek syllabus module 13.3; the six done are 6.7 → 11.5, 11.6, 11.7; 4.1 → 10.5; 4.4 → 10.7; 6.5 → 12.2.
8. **Housekeeping when convenient:** the title-and-date pass over the 44 sampled-clear Rome reports (search for a surname followed by a bare year with no title; the curated bibliographies now list every such case under "Not resolved" or as "(identified from context)", so start from those files); the light read of the flagged kit documents (`README.md`, `BACKLOG.md`, `SYLLABUS-CHANGES.md`, `CHANGELOG.md`, `build.py:roothome`, the code) that clears the last `artefacts` entries.
9. **Two rules of 27 October 2026 apply throughout:** length is a guide, not a law (`check.py` notes the count and never fails on it; dimension 8 scores padding, not length), and every unit keeps its sources (`biblio.py` runs on every build; a writer leaves `bibliography/<course>/r-<id>.md` beside each new report).

**Standing cadence (Pedro's decision, 27 October 2026):** the sample-first review runs at the end of every four written units of any course, on one in four of the reports written since the last review, same scorecard, same decision rule. `review_due.py` says when it is due; a writing session that sees FABLE REVIEW DUE stops at its unit boundary and says so. Lesson of session 3: when a sample splits by provenance, split the stratum.

Writing the 20 unwritten Rome modules is the backlog (`BACKLOG.md`), not this session's job, unless I say otherwise.

## At the end of the session

- `python3 build.py`, then `python3 verify.py`; it must print ALL CHECKS PASSED.
- Publish to the same artifact (and either syllabus if it changed).
- Update `README.md` ("Where things stand"), add the session to `CHANGELOG.md` (entry, "At a glance" row, "Where things stand"), add a `review_notes` entry, and rewrite this `NEXT-SESSION.md` to say exactly where the next session resumes.
- Send me the updated kit zip, and summarise in a few lines: what was reviewed, verdicts, what changed, what is left in the queue.

## Rules

- Never weaken a flag without doing the review: an entry mentions Fable 5.1 only if Fable 5.1 actually reviewed or wrote it.
- Keep the design rules in `README.md` and the house style in `AGENT-SPEC.md`.
- Be direct and terse; one-line progress updates as audits land.
