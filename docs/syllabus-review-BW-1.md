# Syllabus review BW-1: course BW after DD-BW3

Row S-BW (P125; Pedro, 16 Nov 2026, 23:45). Run on 17 Nov 2026 by a chat on Opus 5.5 (claude-opus-5-5; the row asked for Fable, recorded and carried on), with Pedro present to confirm each brief change. Rules: `docs/public-courses.md` §3, rules 6, 7 and 12 (a brief changes only here, and only as Pedro confirms; a correction is made in the chat that finds it, checked first). Inputs: `generator/data/building-with-ai/syllabus-flags.md` (F1 to F123), `units_data.py` with `AIMS`, `case-academy.md`, the thirteen filed units (`courses/building-with-ai/`), and, for the case-file needs, a fresh Opus 5.5 records extractor's report on the Project's records (`audits/building-with-ai/syllabus-review-BW-1-records.md`, saved from its `out/case-lines.md`). The course is complete (13 of 13): no unit is blocked, and the aim is briefs that match what was filed.

## 1 · What was sorted

Every flag whose status was `open` on 17 Nov 2026 (61), and the five `carried` flags the row names as case-fact needs (F83, F92, F99, F108, F109): 66 lines. Not sorted, because neither open nor named: the other carried flags (their units dealt with them) and the resolved ones (F25, F59, F98, F101, F112, F123). Two carried flags ask the syllabus review a question and get an answer in §4 without a line of their own: F11 (tier vocabulary) and F32 (which scheduled task).

The kinds, as in S-PB1:
- **(a)** a brief, Aim, Takes or Gives line, or the shared preamble, that does not match what was filed or what the case file holds: an exact replacement in `units_data.py`, applied only as Pedro confirms.
- **(b)** a filed unit that holds a mistake, a stale pointer or a statement the records now contradict: an exact replacement, checked by a fresh corrections checker with live search before it is applied, with a dated note in the unit and a line in the hub's `CHANGELOG`.
- **(c)** a fact the case file lacks that the Project's records hold, or a §9 line where they hold none: appended to `case-academy.md`, dated, private details removed.
- **(d)** left open, with the reason: a rule for the staleness checks of 15 and 16 May 2027 or for a later pass, a vendor page still to load, or the filling of unit cells from the facts (c) adds (carried proposal CP-4).

After the changes, (a), (b) and (c) flags are set to `resolved (S-BW, 17 Nov 2026: …)`; each (c) flag whose units still say "not in the case file", or now contradict the case file, is set to `carried (S-BW, 17 Nov 2026: case file C…; the units: CP-4)` and is resolved by the chat that works CP-4; every other (c) flag is `resolved (S-BW, 17 Nov 2026: …)`; (d) flags keep `open` and gain "S-BW (17 Nov 2026): left open; <reason>."

## 2 · The table

| Flag | Kind | Touches | The change |
|---|---|---|---|
| F4 | c | case file §7, §9 | C2 (surfaces, memory, the knowledge's size, token totals, a failure traced to a chat's length, usage-limit stops); §9 line N1 (plan, per-unit token measure, retrieval mode). BW1's rows 3, 10, 11 and 12 still say "no instance in the case file": CP-4 |
| F18 | c | case file §2, §3, §4, §5, §8, §9 | C1, C3, C4, C5 (model by task type, the drafts' writing model, the research agents' model, the auditing models); §9 lines N2, N3. BW2's "not recorded" cells: CP-4 |
| F19 | c | case file §2, §9 | C1 (briefs and prompts: this course's preamble and briefs are public; the staleness prompt is in the method); §9 N4 (no private brief, fresh-check prompt or audit prompt text). BW3's [UNKNOWN] examples stand |
| F21 | c | case file §2, §9 | C1 (length is a guide, set 27 Oct 2026); §9 N5. BW3 §3 stands |
| F23 | d | BW3 | Left open: Google's prompt-design page still to load; the staleness checks of 15–16 May 2027 retry it (with F34, F48, F68, F74, F75, F76, F87, F120) |
| F24 | — | BW3 | Resolved, no change: each worked example stays whole so it can be pasted; the owner's override stands (a later chat shows only filled lines if he asks) |
| F26 | c | case file §7 | C2 (the seventeen findings: layer, fix, severity, status on 16 Nov 2026; a kind only where the audit names one). BW4 §7 and its Deliverable: CP-4 |
| F28 | c | case file §7 | C2 (mirror lag: three instances, the site behind the repository, the second publishing place behind the first, and the mirror rule). BW4 §5's case example: CP-4 |
| F29 | c | case file §7, §9 | C2 (stopped and restarted work: instances); §9 N6 (no count). BW3 §5 and BW4 §4 stand |
| F34 | d | BW4 | Left open: OpenAI's pages still to load; retried at the staleness checks |
| F35 | c | case file §1, §2, §9 | C1, C6 (one build order with dates; the decision dates); §9 N7 (no spec, no non-goals). BW5's [NOT IN CASE FILE] cells: CP-4 |
| F41 | d | BW5, DD-BW1 | Left open: a standing citation rule (the exact URL read) for the staleness checks and any corrections pass; no unit remains to receive it |
| F42 | b | BW3 | B4 below: BW3's convention gains a pointer to BW5 §5 and §9 |
| F43 | a | BW6 Takes line | A2 below (BW6's Takes line reads BW1, BW2, BW3, BW5). BW5 Deliverable 1b row 6 stands: BW5 reads each Takes entry from the Gives lines of the units named, and BW2's Gives line does not name BW6 (fresh check, finding 2) |
| F45 | c | case file §5, §9 | C5 (findings not applied as given, per unit); §9 N8 (no total, no false-alarm rate). BW6 §6 stands |
| F46 | c | case file §3, §4, §9 | C3, C4 (claims and sections in the audits); §9 N9. BW6's [UNKNOWN] N: CP-4 |
| F47 | c | case file §4 | C4 (Audit 2's date, model, units; 3 of the 10 stale claims sampled). BW6 Deliverable H: CP-4 |
| F48 | d | BW6 | Left open: OpenAI's deep-research pages still to load; retried at the staleness checks |
| F51 | — | BW6 | Resolved by decision: BW6 stays search off; its live-read product facts are re-read with the staleness checks of 16 May 2027, recorded on F88 and by B8's note under the index's staleness table |
| F52 | a + b | the shared preamble; BW9 §8 | A1 below: the case line in the case file's own wording, as F98, F112 and F123 did in three units; B7 below corrects BW9 §8 |
| F60 | b | BW7 | B2 below: BW7's two pointers to BW8 say what BW8 does |
| F61 | b | BW6, BW8 | B3 below: BW6's stratified draw in four places, and BW8's sentence that called its draw a departure |
| F62 | c | case file §7 | C2 (four skills in the repository, installed by hand). BW8 §5 and §7: CP-4 |
| F63 | c | case file §1 | C6 (no INDEX.md, INSTRUCTIONS.md or BUILD-ORDER.md; their equivalents). BW8 Deliverable F: CP-4 |
| F64 | c | case file §7 | C2 (no scheduled task; unattended runs instead). BW8, BW9: CP-4 |
| F68 | d | BW8, BW10 | Left open: OpenAI's and Anthropic's pages still to load; retried at the staleness checks |
| F69 | d | BW8 and later checks | Left open: a standing citation rule (the page, not the .md copy) |
| F70 | d | BW8 to DD-BW1 | Left open: a standing citation rule (the bare address); BW9's two ?m=1 citations are already gone (corrections C-BW9-1, C-BW9-2) |
| F71 | c | case file §7, §9 | C2 (agents' tools where transcripts were kept, commits and branches, caps, who publishes); §9 N10. BW9's [NOT IN CASE FILE] cells: CP-4 |
| F73 | d | DD-BW1 | Left open: the keynote recording, at DD-BW1's staleness check of 16 May 2027 (F94) |
| F74 | d | BW9 | Left open: OpenAI's Codex pages still to load |
| F75 | d | BW7, BW9 | Left open: the auto-mode figures and the Chrome announcement still to load |
| F76 | d | BW9 | Left open: no Google page found yet |
| F77 | d | later checks | Left open: a standing citation rule (Claude Code alias against API lineup) |
| F78 | d | later checks | Left open: a standing rule (a fresh-context check that is not a fork) |
| F82 | d | a private unit's staleness check | Left open: an instruction to that check; no BW text changes |
| F83 | c | case file §7, §9 | C2 (where private material is kept), with F4's lines; §9 N1, N3, N11. BW10's blanks: CP-4 |
| F87 | d | BW8, BW10 | Left open: pages still to read at their plain addresses |
| F88 | d | BW2, BW5, BW9, BW10 | Left open until the checks run; gains BW6's and DD-BW3's live-read pages (F51, F119) |
| F89 | b | BW7 | B6 below: a check only, of whether BW7's 22 Sep 2023 and the publisher's 18 Sep 2023 are two postings; a text change only if the checker finds BW7 wrong |
| F90 | — | BW7, BW9 | Resolved, no change (the page loaded and agrees with BW7) |
| F91 | — | DD-BW1 | Resolved, no change (DD-BW1 states both dates; no other unit dates the post) |
| F92 | c | case file §2, §9 | C1 (rows run with the owner away); §9 already records the rest (16 Nov 2026). DD-BW1's cells: CP-4 |
| F94 | d | DD-BW1 | Left open until DD-BW1's staleness check |
| F96 | — | DD-BW1 | Resolved, no change: the new material is in DD-BW1; no brief needs it |
| F97 | d | DD-BW1 | Left open until DD-BW1's staleness check |
| F99 | c + b | case file §7; DD-BW2 §7 and Part 1 G | C2 (a publish repeated on 4 Nov 2026; a failed deploy retriggered on 9 Nov 2026; first refusals; missed deploys); B5 below corrects DD-BW2's "records none". The brief's parenthesis stands: the record holds one |
| F102 | c | case file §5, §9 | C5 (who applied findings), with F45's lines; §9 N8 (no count by kind) |
| F103 | c | case file §5 | C5 (all 36 written by Opus 5.5; the rows are in build order, not a known order of writing). DD-BW2 §3: CP-4 |
| F104 | c | case file §5, §9 | C5 (the history courses' check pipeline); §9 N13 |
| F105 | c | case file §4, §9 | C4 (Audit 2), C7 (why Audits 3 onward did not run). DD-BW2 §4, BW6 H: CP-4 |
| F106 | c | case file §5 | C5 (the one rewrite verdict was read as fix; all findings applied; not rewritten). DD-BW2 §3: CP-4 |
| F107 | c | case file §6, §9 | C8 (retrofit figure passes: counts, drops after two failures, the checkers' model); §9 N14 |
| F108 | c | case file §8 | C9 (the review's ten ranked changes with their counts). DD-BW3: CP-4 |
| F109 | c | case file §8, §9 | C9 (how long chats stayed open), N1, N3 |
| F110 | c | case file §1, §9 | C6 (start date; the two history courses' word counts); §9 N15 |
| F113 | a | DD-BW3 brief | A3 below: the brief asks for what DD-BW3 did, DD-BW2 Part 2's changes restated. With C9 the case file now also holds the review's own list; setting it beside Part D is CP-4 |
| F114 | d | DD-BW3 | Left open: C9 gives the review's definition of a turn; the records define no ask (§9 N16); stating the case's turn beside DD-BW3's own is CP-4 |
| F115 | d | DD-BW3 | Left open with F121: a standing rule for any correction of a grade in BW10 Part 1, DD-BW1 Part 2 or DD-BW2 Part 2 |
| F116 | c | case file §8, §9 | C9 (how the chats were listed, the fields, breakdowns, pattern counts, rules tested, the review's date); §9 N16. DD-BW3 §6, Parts A and B: CP-4 |
| F117 | c | case file §8 | C9 (the review's own statement that the six days were a heavy-building week, not typical) |
| F118 | c | case file §8, §9 | C9 (where the working files were kept); §9 N17 |
| F119 | d | DD-BW3 | Left open until the check; its four pages are now named on F88 |
| F120 | d | DD-BW3, BW1, BW9 | Left open: the vendors' session-list and chat-search pages still to read |
| F121 | d | DD-BW2, DD-BW3 | Left open: a standing rule for any correction of DD-BW2 Part 2 (CP-4 included) |
| F122 | — | DD-BW3 | Resolved, no change (met) |

Count: 66 lines. (a) 3 (F52, F43, F113). (b) corrections B2 to B8 for 7 flags (F42, F51 and F119's record note, F52, F60, F61, F89, F99; F52 and F99 also (a) or (c)). (c) 31: 30 table lines (F99's c + b among them) and F113's case half. (d) 23 (F23, F34, F41, F48, F68, F69, F70, F73, F74, F75, F76, F77, F78, F82, F87, F88, F94, F97, F114, F115, F119, F120, F121). Resolved with no change: 6 (F24, F51, F90, F91, F96, F122).

## 3 · The exact changes

### Kind (a): briefs, applied only as Pedro confirms

Each is an exact replacement in `generator/data/building-with-ai/units_data.py`; the Current text occurs once in the file.

**A1 · The shared preamble's case line (F52; also F98, F112, F123).** Every unit's open brief and the course's Briefs page.

| Current | New |
|---|---|
| "Running case: Academy (real), a library of self-study courses built by one person with Claude in October and November 2026, each unit written by one model from a brief, checked by a fresh context and audited by sample. " | "Running case: Academy (real), a library of self-study courses built by one person with Claude in October and November 2026, with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library. " |

The New wording is the one the corrections checks passed for DD-BW1, DD-BW2 and DD-BW3. BW9 §8 (the one filed unit that still quotes the old line, "each unit written by one model from a brief, checked by a fresh context and audited by sample (Academy case file §1, §2)") is corrected by B7 below, whether or not A1 is confirmed.

**A2 · BW6's Takes line in `AIMS` (F43).**

| Current | New |
|---|---|
| "B6 as source material; BW1, BW2, BW5" | "B6 as source material; BW1, BW2, BW3, BW5" |

BW6 uses all four, each by section (BW3's templates 3 and 9 for its checker brief).

**A3 · DD-BW3's brief, last clause (F113).**

| Current | New |
|---|---|
| and the worked example's highest-leverage changes restated so they apply to any reader. | and the changes the worked record supports (DD-BW2 Part 2), restated so they apply to any reader. |

### Kind (b): corrections to filed units

Each is checked by a fresh corrections checker (Opus 5.5, live search under the web rule) before it is applied with `python3 kit/thin.py correct`; each gets a dated note in its unit and a line in the hub's `CHANGELOG`.

**B1 · dropped** (fresh check, finding 2: BW5's row 6 follows its own rule).

**B2 · BW7's two pointers to BW8 (F60).**

| Current | New |
|---|---|
| BW8 turns the procedure into something that runs itself. | BW8 turns one stage of the procedure, the fresh check, into a skill. |
| BW8 turns a procedure in this form into a skill and a scheduled run; | BW8 turns one stage in this form into a skill and schedules a different, date-driven check; |

**B3 · BW6's stratified draw (F61), and BW8's companion sentence.** ⚠ Four places in BW6 and one in BW8.

| Unit | Current | New |
|---|---|---|
| BW6 §2 step 2 | Draw at least one claim from every stratum, then more from the largest until the sample reaches its size. | Draw at least one claim from every stratum, then the rest at random from all remaining claims, so larger strata get more in proportion, until the sample reaches its size. |
| BW6 Deliverable C2 | One claim per stratum, then extra draws from the largest strata until the sample reaches *n*; within a stratum, by random number. | One claim per stratum, then the rest at random from all remaining claims, so larger strata get more in proportion, until the sample reaches *n*; by random number. |
| BW6 filled case text | then extra draws from the largest sections, by random number. | then the rest at random from all remaining claims, so larger sections get more in proportion, by random number. |
| BW6 template | then extra draws from the largest strata, by random number"] | then the rest at random from all remaining claims, so larger strata get more in proportion, by random number"] |
| BW8 unsure item 9 | the proportional extra draws in `check.py sample`,  | (empty) |
| BW6 §2 step 3 | 3. **Draw by number, never by eye.** Number the claims in each stratum and pick with a random number. | 3. **Draw by number, never by eye.** Number the claims and pick each draw with a random number: within its stratum for each stratum's first claim, from all remaining claims for the rest. |
| BW8 | Two changes, each for a script's sake: the claims table in item 1 carries a verdict column, so that a script can apply rule C5 rather than the model; and after one claim from every section, the extra draws are taken at random from all remaining claims, so larger sections give more draws in proportion, which is this unit's reading of BW6's "extra draws from the largest strata" in a form a script can repeat from its seed. | One change, for a script's sake: the claims table in item 1 carries a verdict column, so that a script can apply rule C5 rather than the model. After one claim from every section, the extra draws are taken at random from all remaining claims, so larger sections give more draws in proportion, as BW6 states the rule (corrected 17 Nov 2026), in a form a script can repeat from its seed. |

**B4 · BW3's convention on one brief per chat (F42).**

| Current | New |
|---|---|
| - One brief per chat. If the first output misses, change the brief and open a new chat (§5). | - One brief per chat. If the first output misses, change the brief and open a new chat (§5). In a specified project, where briefs are not reworded once work starts, the miss is raised as a flag and the brief changes at a boundary (BW5 §5, §9). |

**B5 · DD-BW2 §7 and Part 1 G (F99).** Source: case file §7 as C2 adds it, from the kit changelog of 4 and 9 Nov 2026.

| Current | New |
|---|---|
| **A publish that had to be repeated.** The case file records none. It says the site is published in two places after each filing, first as an artifact on claude.ai and then on GitHub Pages (§1, note), and that a script restores every file if the course index check fails (§1, note); it records no failed or repeated publish. If one happened, it is not in the record. | **A publish that had to be repeated.** The site is published in two places after each filing, first as an artifact on claude.ai and then on GitHub Pages (§1, note), and a script restores every file if the course index check fails (§1, note). The case file records one repeated publish and one retriggered deploy (§7, added 17 Nov 2026): a layout fault found after a publish on 4 Nov 2026 was fixed and the site published a second time the same day, neither the change's checker nor the verify script having caught it; and on 9 Nov 2026 a GitHub Pages run failed with no job run and was retriggered with an empty commit. It also records publishes the tool first refused until the named files were read or checked against the build, and deploys that did not run when attaching the public repository was refused (§7). |
| Repeated publish: not recorded. | Repeated publish: 1, and 1 failed deploy retriggered (§7, added 17 Nov 2026). |

**B6 · BW7, Dell'Acqua et al.'s first posting (F89).** A check only: whether BW7's date of 22 Sep 2023 and the publisher's 18 Sep 2023 are two postings of the working paper. If they are, nothing changes; if BW7's date is wrong, the checker gives the exact replacement and it is applied after a second check.

**B7 · BW9 §8, the case line (F52).** Applied whether or not A1 is confirmed, as F98, F112 and F123 were.

| Current | New |
|---|---|
| each unit written by one model from a brief, checked by a fresh context and audited by sample (Academy case file §1, §2) | with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9) |

**B8 · The course index's staleness section (F51, F119; fresh check, finding 10).** `kit/index_check.py` refuses a table row for a unit that is not search on, so the table cannot carry BW6 or DD-BW3. One sentence is added under the section's heading, before its table: "The checks of 16 May 2027 also re-read BW6's live-read product facts and DD-BW3's four export and session pages, though both units are search off (syllabus review BW-1, F51, F119)." A record change, not a unit; checked by `index_check.py`.

### Kind (c): the case file

Appended to `generator/data/building-with-ai/case-academy.md` in its addendum style, each line prefixed with its section and dated, from the records extractor's report (lines and sources there), private details removed. Every proposed line under 'Found' in the extractor's report is appended under the section it names, word for word except as corrected below (F92, F105, F99's refused-publish line, F106) and with the F26 status lines as in the note under C2; the extractor's 'Proposed §9 lines' are N1 to N16 in order (its N12 dropped as a repeat of §9). The groups index those lines:

- **C1 (§2):** syllabus chats on Fable (F18); extraction by Sonnet 5.5 agents for the history bibliographies (F18); briefs and prompts (F19); length a guide (F21); rows run with the owner away (F92); effort recorded in none of 53 chats (F18); the decision dates (F35); long units filed above the guide (F21); the history courses' writing models (fresh check, finding 20).
- **C2 (§7):** surfaces, memory, the knowledge's size and retrieval, token totals, a failure traced to a chat's length, usage-limit stops (F4); the seventeen structure-audit findings and their status on 16 Nov 2026 (F26); mirror lag (F28); stopped and restarted work (F29); skills (F62); scheduled tasks and unattended runs (F64); agents' tools, commits and branches, caps, after lost writers, who publishes (F71); where private material is kept (F83); the four publish lines (F99); the private-terms check added 11–12 Nov 2026, after the structure audit (F53). The status lines of the seventeen findings give the fix list's verdict as written, with its qualifier (F2, F5, F11, F12, F13, F14 '(reading)'; F15 '(residual)'), then the extractor's gloss in brackets.
- **C3 (§3):** the research report's agents (Fable 5.1, 27 Oct 2026) (F18); Audit 1's nine sections and 91 claims (F46); the audit rewrites of 28–29 Oct 2026 (F29).
- **C4 (§4):** the auditing models (F18); Audit 2's date, model, units, samples per unit and the 3 of 10 stale claims inside the sample (F46, F47); the public marketing course's audits: claims and model (F18, F46).
- **C5 (§5):** all 36 drafts written by Opus 5.5 and the rows' order (F18, F103); findings not applied as given, per unit (F45); who applied findings (F53, F102); the history courses' check pipeline (F104); the rewrite verdict read as fix (F106).
- **C6 (§1):** first, the public marketing course named (fresh check, finding 17); sections on the site, 1 Nov 2026 (F46); the private courses' build order with dates (F35); the layout's equivalents of INDEX.md, INSTRUCTIONS.md, BUILD-ORDER.md (F63); the start date and the history courses' word counts (F110); the gates before publishing (F53).
- **C7 (§9):** why Audits 3 onward did not run (F105).
- **C8 (§6):** the retrofit figure passes' counts, the drop after two failures in those passes beside §6's three, the figure checkers' model (F53, F107); how re-runs were recorded (F53). §6's line itself is not changed: the course index records two units' figures dropped after a third check, so both rules ran.
- **C9 (§8):** model by task type in the 53 chats (F18); the review's listing, fields, turn definition, breakdowns, pattern counts, rules tested and date (F116); typicality in the review's own words (F117); working files (F118); the ten ranked changes with their counts (F108); how long chats stayed open (F109). The changes are named by what they do, never by the private course's unit codes beyond those §5 already uses.
- **§9 N1 to N16:** the extractor's "records do not" lines, each naming its flags, its N12 dropped (fresh check, finding 16).
- **Corrected lines** (findings 6, 7, 12, 18): F92's line as finding 6's fix; F105's as finding 7's; F99's refused-publish line as finding 12's; F106's "it was not rewritten or re-checked" as "the records show no rewrite and no re-check".

### The flags file

After the changes are applied, in `syllabus-flags.md`: each (a), (b) and (c) flag `resolved (S-BW, 17 Nov 2026: …)` naming its change; each (c) flag whose units still say "not in the case file", or now contradict it, is `carried (S-BW, 17 Nov 2026: case file C…; the units: CP-4)`, resolved by the chat that works CP-4; every other (c) flag `resolved`; each (d) flag gains, at the end of its proposed change, "S-BW (17 Nov 2026): left open; <reason from the table>"; F88 gains "and BW6's and DD-BW3's live-read pages (F51, F119)"; F11 and F32 gain their answers (§4).

## 4 · Two carried questions answered

- **F11 (tier vocabulary).** No brief change: BW2's brief names tiers as a pattern, and BW2 records the four words (small, mid, large, large top rung) as the course's vocabulary; BW3, BW6, BW7 and BW8 use them; BW10 budgets by BW2's routing rows. The flag gains "S-BW: BW2's four words are the course's tier vocabulary; no brief change."
- **F32 (which scheduled task).** No brief change: BW8 took BW4's rot check and said why (F60's record); the flag gains "S-BW: BW8's choice stands; no brief change."

## 5 · Carried proposal

- **CP-4 · Fill the BW units' "not in the case file" cells from the lines S-BW added to the case file** (F4, F18, F26, F28, F35, F46, F47, F53, F62, F63, F64, F71, F83, F92, F103, F104, F105, F106, F107, F108, F109, F110, F114, F116, F117, F118; BW1, BW2, BW4 to BW10, DD-BW1 to DD-BW3). It covers both the blank cells and the statements the case file now contradicts (among them BW7 §5's 'it records none before publishing', DD-BW2 §1, §6, §8 and Part 1, DD-BW3 §2, §6 and Part D's 'the case file does not hold them'): each is corrected, not left standing, each replacement drafted by a fresh Opus 5.5 agent from the case file and checked by a fresh corrections checker before it is applied. ⚠ A pass over twelve filed units; it would put a BW corrections pass into W-SP1's chat, off that row's subject; Pedro may veto it there and keep it for a housekeeping row after W-DD-SP3. Until CP-4 runs, published units state that the case file lacks facts it now holds.

## 6 · Fresh check of this proposal, verbatim

A fresh Opus 5.5 agent (it stated claude-opus-5-5) that read only the packet `/home/claude/work/check-pk/` (this proposal as first written, `syllabus-flags.md`, `units_data.py`, `case-academy.md`, the thirteen filed units, the records extractor's report and the records it read), under the agents' rules. Its write of its report was refused; the report, returned as its reply, is saved here verbatim before any finding was applied (the harness's indentation removed). All 21 findings are applied above; finding 10 is answered by B8 (a note under the staleness heading) instead of a table row, because `kit/index_check.py` refuses a staleness row for a unit that is not search on.

claude-opus-5-5. Verdict: fix. 1 error, 10 should-fix, 10 minor. The write to out/report.md was refused, so the full report follows.

Verdict: fix

Fresh check of the syllabus review BW-1 (S-BW) proposal, 17 Nov 2026. Packet only. The text checks used python str.count on each file.

## Findings

1. [error] proposal.md §2, count line. Current: "(b) corrections B1 to B7 for 6 flags (F42, F43, F52, F60, F61, F89, F99; F43, F52 and F99 also (a) or (c)). (c) 33 (F4, …". Problem: the line lists seven flags under (b) but calls them 6. Under (c) it names 31 items, not 33: the 30 table lines of kind c (F99's "c + b" included) plus F113's case half. The other counts are right: 66 lines; (a) 3; (d) 22; 7 resolved with no change; 61 open plus 5 carried. Fix: if finding 2 is accepted (B1 dropped), write "(b) corrections B2 to B7 for 6 flags (F42, F52, F60, F61, F89, F99; F52 and F99 also (a) or (c)). (c) 31: 30 table lines (F99's c + b among them) and F113's case half (F4, …". If B1 is kept, write "(b) corrections B1 to B7 for 7 flags (F42, F43, F52, F60, F61, F89, F99; F43, F52 and F99 also (a) or (c)). (c) 31: 30 table lines (F99's c + b among them) and F113's case half (F4, …".

2. [should-fix] §3 B1 (BW5 Deliverable 1b, row 6) and table line F43. Current: B1 replaces "| 6 | BW6 · Research and verification | BW1, BW3, BW5 | BW8, BW9 | |" with "… | BW1, BW2, BW3, BW5 | …". Problem: BW5 1b says how the table was built: "each Takes entry is read from the Gives lines of the units named". BW2's Gives line ("the routing table BW7 assigns stages from and BW10 budgets") does not name BW6, so row 6 is right by BW5's own rule. Under B1, row 6 would break that rule, and row 2's Gives column ("BW7, BW10") would then disagree with row 6. The table is not a copy of the AIMS Takes lines either: rows 2, 7, 8 and 10 differ from AIMS too, and no flag raises them. Fix: drop B1. Table line F43 becomes "| F43 | a | BW6 Takes line | A2 below (BW6's Takes line reads BW1, BW2, BW3, BW5). BW5 Deliverable 1b row 6 stands: BW5 reads each Takes entry from the Gives lines of the units named, and BW2's Gives line does not name BW6 |".

3. [should-fix] §3 B7 and A1's note; table line F52. Current: "**B7 · BW9 §8, the case line (F52; only if A1 is confirmed).**", "is corrected by B7 below if A1 is confirmed.", and "| F52 | a | the shared preamble |". Problem: BW9 §8's line is the contradiction F52 itself names. F52 says each unit cites the case file's own wording "until then", and F98, F112 and F123 corrected DD-BW1 to DD-BW3 with no preamble change. Whether BW9 is corrected does not depend on A1. The table also gives F52 kind a only, while the count puts F52 under (b). Fix: "**B7 · BW9 §8, the case line (F52).** Applied whether or not A1 is confirmed, as F98, F112 and F123 were." Then "is corrected by B7 below, whether or not A1 is confirmed." Then the table line reads "| F52 | a + b | the shared preamble; BW9 §8 | A1 below: the case line in the case file's own wording, as F98, F112 and F123 did in three units; B7 below corrects BW9 §8 |".

4. [should-fix] §3 Kind (c), group lists, and the table's C references. Current: "Groups C1 to C9 and the §9 lines N1 to N17 are the extractor's proposed lines, kept word for word except where noted:" followed by group summaries. Problem: the summaries leave out extractor lines, and some disagree with the table.
   - The F18 table line names "model by task type", a §8 line from DD-B2 §2, but C9's list does not include it.
   - F18's effort line (§2) is in no group.
   - F35's decision dates are cited as C1 in the table but missing from C1.
   - F53's private-terms start line (§7) and its re-runs line (§6) are in no group.
   - F29's §3 rewrites line is in no group.
   - F46's §1 sections line (1,581 sections on 152 pages) and its §4 public-course audits line (155 sampled, 712 checked) are in no group.
   - F21's §5 long-units line and its second §2 line are in no group.
   - The F28 table line says "four instances", but the extractor gives six lines.

   Fix: replace the lead-in with "Every proposed line under 'Found' in the extractor's report is appended under the section it names, word for word except as corrected below (F92, F105, F99's refused-publish line, F106) and with the F26 status lines as in the next note; the extractor's 'Proposed §9 lines' are N1 to N17 in order. The groups index those lines:". Then add to the groups:
   - C1: "effort recorded in none of 53 chats (F18); the decision dates (F35); long units filed above the guide (F21)"
   - C2: "the private-terms check added 11–12 Nov 2026, after the structure audit (F53)"
   - C3: "the audit rewrites of 28–29 Oct 2026 (F29)"
   - C4: "the public marketing course's audits: claims and model (F18, F46)"
   - C6: "sections on the site, 1 Nov 2026 (F46)"
   - C8: "how re-runs were recorded (F53)"
   - C9: "model by task type in the 53 chats (F18)"

   In the table, "C2 (mirror lag: four instances)" becomes "C2 (mirror lag: three instances, the site behind the repository, the second publishing place behind the first, and the mirror rule)".

5. [should-fix] §3 C2, last sentence. Current: "The status lines of the seventeen findings use the fix list's own wording." Problem: the extractor's lines paraphrase the fix list. The fix list (records/p30-b4-fixes.md, Summary) marks F2, F5, F11, F12, F13 and F14 "(reading)" and F15 "(residual)". The extractor drops those qualifiers and writes its own glosses instead ("still applies in part" for F1 and F15; "one of five parts done" for F9). Fix: "The status lines of the seventeen findings give the fix list's verdict as written, with its qualifier (F2, F5, F11, F12, F13, F14 '(reading)'; F15 '(residual)'), then the extractor's gloss in brackets." For example, F2 becomes "Status 16 Nov 2026: still applies (reading; no record of removal)."

6. [should-fix] Extractor line F92 (C1). Current: "§2 · Publishing without the owner present (the project changelog, 12–14 Nov 2026): several writing rows ran with the owner away, and the same chat wrote, checked, filed and published the units." Problem: the line misstates the record. The cited rows (docs-CHANGELOG.md:89, :88, :74, :73, :61) say the chat "only staged, applied, filed and published", and fresh agents wrote and checked. Fix: "§2 · Publishing without the owner present (the project changelog, 12–14 Nov 2026): several writing rows ran with the owner away; fresh agents wrote and checked the units, and the main chat staged, applied, filed and published them without waiting for the owner."

7. [should-fix] Extractor line F105 (C7). Current: "…after Audit 2 the next audits of the marketing, AI and UX courses were deferred to a later stage reserved for the auditing model, the auditing model having run short on 29 Oct 2026; on 15 Nov 2026 the owner closed that stage, …". Problem: the line infers a cause. DD-B2:82 records only that an ask confirmed on 29 Oct (sent 30 Oct) notes the owner "low on Fable" and moves the check to a later row, and it adds that "the history gives the order of events and no measured cause". The kit changelog (:62, :748) names Audits 3 to 6 of the marketing and AI courses as owed to the Fable stage (row P49). The cited lines say nothing about the UX course. Fix: "§9 · Audits 3 onward (the kit changelog, 2–3 Nov 2026; the AI course's DD-B2 §4; the method, 15 Nov 2026): after Audit 2, Audits 3 to 6 of the marketing and AI courses were recorded as owed to a later stage reserved for the auditing model; an ask of 29–30 Oct 2026 records the owner low on that model's allowance and moves its check to a later row, which the review gives as the order of events, not a measured cause; on 15 Nov 2026 the owner closed that stage, retired the four-unit audit and left the fresh check and the staleness check as the guards."

8. [should-fix] §5 CP-4, flag list. Current: "(F4, F18, F26, F28, F35, F46, F47, F62, F63, F64, F71, F83, F92, F103, F105, F106, F108, F114, F116; BW1, BW2, BW4 to BW10, DD-BW1 to DD-BW3)". Problem: the C lines also answer filed texts that this list leaves out:
   - BW7 §5: "it records none before publishing … the case file does not say whether one was added". BW7 Part 1 also has [NOT IN CASE FILE] cells (F53).
   - DD-BW2 §1 and Part 1: no total words, start date not recorded (F110); history checks not recorded (F104).
   - DD-BW2 §6: "What the record does not hold" (F107).
   - DD-BW2 §8 and Part 1 H (F109).
   - DD-BW3 §2: "the case file does not say whether those six days were typical" (F117).
   - DD-BW3 §5 (F118).

   Several of these are statements the new case file contradicts, not blank cells. They also include DD-BW2 §8's "the case file does not list them" and DD-BW3 §6's and Part D's "the case file does not hold them". Fix: "(F4, F18, F26, F28, F35, F46, F47, F53, F62, F63, F64, F71, F83, F92, F103, F104, F105, F106, F107, F108, F109, F110, F114, F116, F117, F118; BW1, BW2, BW4 to BW10, DD-BW1 to DD-BW3). It covers both the blank cells and the statements the case file now contradicts (among them BW7 §5's 'it records none before publishing', DD-BW2 §1, §6, §8 and Part 1, DD-BW3 §2, §6 and Part D's 'the case file does not hold them'): each is corrected, not left standing." Add to the ⚠: "Until CP-4 runs, published units state that the case file lacks facts it now holds."

9. [should-fix] §1 (the sentence after the kinds) and §3 "The flags file", on the status of (c) flags. Current: "a (c) flag whose unit cells still read 'not in the case file' says so and names CP-4" (with status resolved). Problem: several of these flags (F26, F28, F35, F47, F63, F105, F116) propose a corrections pass as part of their own change. Marking them resolved removes them from the open set while the filed units contradict the case file, and CP-4 can be vetoed. Fix: in both places, "each (c) flag whose units still say 'not in the case file', or now contradict the case file, is set to `carried (S-BW, 17 Nov 2026: case file C…; the units: CP-4)` and is resolved by the chat that works CP-4; every other (c) flag is `resolved (S-BW, 17 Nov 2026: …)`."

10. [should-fix] Table lines F51 and F119. Problem: F119's own ⚠ says the course index's staleness table, which the staleness checks run from, carries neither BW6 nor DD-BW3. With this proposal, an open flag (F88) remains the only record of their re-reads. Fix: add to §5: "CP-5 · Add to the course index's staleness table, on the row for the checks of 16 May 2027, BW6's live-read product facts (F51) and DD-BW3's four export and session pages (F119), so the check that runs from the table reads them. ⚠ The course index is read by index_check.py and next_prompt.py; the row's format must pass verify.py."

11. [minor] §3 B5, DD-BW2 §7 New. Current: "The case file records two repeats (§7, added 17 Nov 2026):". Problem: Part 1 G's New text counts "Repeated publish: 1, and 1 failed deploy retriggered", so the two texts count differently. Fix: "The case file records one repeated publish and one retriggered deploy (§7, added 17 Nov 2026):".

12. [minor] Extractor line F99, "Publishes refused at first", and B5's matching clause. Current (extractor): "each was read, found equal to the build, and the publish made, never forced." Current (B5): "publishes the tool first refused until the named files were read". Problem: the extractor's count of 21 entries is right, but in kit-CHANGELOG.md:581 the 191 named files were listed and eight of them compared, not read. Fix (extractor): "the named files were read (in one entry, 191 files listed and eight compared), found equal to the build, and the publish made, never forced." Fix (B5): "publishes the tool first refused until the named files were read or checked against the build".

13. [minor] §4 F11. Current: "BW7 and BW10 use them." Problem: BW10 does not use the four tier words; it budgets by BW2's routing rows. "Large, top rung" appears in BW3, BW6, BW7 and BW8. Fix: "BW3, BW6, BW7 and BW8 use them; BW10 budgets by BW2's routing rows."

14. [minor] B3 companion, BW8 Unsure list item 9. Current: "the proportional extra draws in `check.py sample`, " (occurs once). Problem: once B3 is applied, BW6 states the proportional draw, so it is no longer "this unit's design". Fix: add a B3 row for BW8 that replaces it with "" (empty).

15. [minor] B3 companion, BW6 §2 step 3. Current: "3. **Draw by number, never by eye.** Number the claims in each stratum and pick with a random number." (occurs once). Problem: after B3, step 2 draws the rest from all remaining claims, not from within a stratum. Fix: "3. **Draw by number, never by eye.** Number the claims and pick each draw with a random number: within its stratum for each stratum's first claim, from all remaining claims for the rest."

16. [minor] §9 N12 and table line F92. Current: "§9 N12 (whether he reads each unit before publishing)". Problem: the case file's §9 already says this (case-academy.md:133, 16 Nov 2026). N12 repeats it. Fix: drop N12 and renumber, so the N lines run N1 to N16. The F92 line becomes "C1 (rows run with the owner away); §9 already records the rest (16 Nov 2026). DD-BW1's cells: CP-4".

17. [minor] C lines that say "the public marketing course" (F18, F46, F4 extractor lines). Problem: the case file has no such course. Its §1 lists five courses, and "the marketing course" means the private one. Fix: put this line first in C6: "§1 · A second marketing course, public, of 12 units, was created on 11–12 Nov 2026 with this course (the kit changelog); this file calls it 'the public marketing course'." (source: kit-CHANGELOG.md:39).

18. [minor] Extractor line F106 (C5). Current: "it was not rewritten or re-checked". Problem: this is an inference from what the records do not say. Fix: "the records show no rewrite and no re-check".

19. [minor] Table line F115 against F121. Problem: F115's proposed change is a standing rule ("any later correction of a grade … is carried into DD-BW3"), the same kind as F121, but F115 is resolved and F121 is left open. Fix: "| F115 | d | DD-BW3 | Left open with F121: a standing rule for any correction of a grade in BW10 Part 1, DD-BW1 Part 2 or DD-BW2 Part 2 |". The counts become (d) 23 and resolved with no change 6.

20. [minor] C1, F18 (an addition). Problem: kit-CHANGELOG.md:74–75 records that the first history course's 78 reports were written 55 with Fable 5.1 and 23 with Opus 5.5, and the second's 79 all with Opus 5.5. This qualifies case file §2's "One model (Opus 5.5) writes", and no C line carries it. Fix: add to C1 "§2 · Writing models of the history courses (the kit changelog): the first history course's 78 reports were written 55 with Fable 5.1 and 23 with Opus 5.5; the second's 79 all with Opus 5.5."

21. [minor] Note on finding 1. If findings 2 and 19 are both accepted, the count line reads: "(a) 3 (F52, F43, F113). (b) corrections B2 to B7 for 6 flags (F42, F52, F60, F61, F89, F99; F52 and F99 also (a) or (c)). (c) 31: 30 table lines (F99's c + b among them) and F113's case half (…). (d) 23 (… F115 …). Resolved with no change: 6 (F24, F51, F90, F91, F96, F122)."

## Confirmed

- (4) Sorting. syllabus-flags.md holds 61 open, 56 carried and 6 resolved flags (F25, F59, F98, F101, F112, F123). The §2 table has 66 lines with no duplicates. Every open flag appears once, and the only non-open lines are the five carried flags the row names (F83, F92, F99, F108, F109). F11 and F32 are carried and answered in §4. Kind tally: a 2, a+b 1, b 4, c 29, c+b 1, d 22, no change 7, total 66. (a) 3, (d) 22 and 7 are right; (b) and (c) are wrong (finding 1).
- (2) Each Current occurs once in its file: A1, A2 and A3 in units_data.py; B1, B2 (both), B3 (all five), B4, B5 (both), B7 in their units. A1's New fits the PRE string (no quote break, trailing space kept). A2 and A3 fit their double-quoted strings. B1 keeps five cells. B5's G line keeps its form. No New text contains a private term (whole-word scan against private-terms.txt). records-report.md contains none either.
- (1)/(3) The flags read correctly: F42, F43, F52, F60, F61, F89, F99, F113 and the (d) reasons match the flags file. B2 matches BW8: the skill is stage 3, the fresh check, and the scheduled task is BW4's rot check (BW8 §6, Deliverable F). B3 covers all four BW6 places ("largest" occurs only there) and BW8 line 255. BW9 §8 is the only filed unit that still quotes the old preamble line. B4's pointer targets exist (BW5 §5, §9). B5's facts match kit-CHANGELOG.md:598 (session 58, 4 Nov 2026: "Neither checker nor verify had caught it … published a second time") and :512 (session 64, 9 Nov 2026: Pages run failed with no job run, empty commit retriggered, build and deploy jobs succeeded). No DD-BW2 Part 2 change or DD-BW3 text relies on "repeated publish: not recorded".
- (7) A3 matches DD-BW3: Part D restates DD-BW2 Deliverable Part 2's ten changes for any project, with DD-BW2's grades. §6 and Part D say the review's own list is not in the case file. "The worked record" echoes DD-BW2's Gives line. The new clause is consistent with DD-BW3's Takes and Aim.
- (6) No (d) or no-change line needs to be (a) or (b), except as in findings 2, 3 and 19. The standing citation rules (F41, F69, F70, F77, F78) have no unit left to receive them, and the vendor-page retries (F23, F34, F48, F68, F74 to F76, F87, F120) are right for the staleness checks. CP-4's deferral is sound: filling twelve units needs a fresh corrections check per change, which is not a syllabus review's work. It is incomplete as scoped (finding 8), and the flags it carries should not be closed first (finding 9).
- (5) Extractor spot-checks against the cited lines (24 lines):
  - Correct: F4 knowledge size (B4:385, :531); F4 token totals (kit:1203, :256); F4 chat-length failure (docs:77); F4 usage limits and 18% (kit:1297, docs:60); F18 model by task (DD-B2:36–52); F18 research agents on Fable 5.1 (index:60); F18 audit models (index:65, :70, :118, :123, :128, :129); F21 length rule (kit:1238–1239, method:25); F47 3 of the 10 stale claims in the sample (audit-2 front matter, :37, :125); F53 private-terms check from G-0 (kit:39); F62 skills (B4:378, docs:111); F64 no scheduled task (B4:380, p30:142) and unattended rows (docs:146, :145, :122, :89, :74, :62); F83 private material (docs:11, p30:134); F99 two publish events, and 21 refused-first entries counted at :462 to :800; F107 figure counts (kit:1000, :996, :984, :982, :72) and C8's two-fail against three-fail note (index:76, :80); F110 start date and word counts (kit:3, :96, :1413, :74, :75; docs:188); F116 turn definition (DD-B2:32); F117 typicality (DD-B2:18, :139); F118 working files (DD-B2:14, :203–204; kit:738); C9's ten changes (DD-B2:141–197); F26 statuses in substance (p30 Summary).
  - Faults: F92 misstates (finding 6); F105 infers a cause (finding 7); F99's refused-publish line overstates one entry (finding 12); F106 is mildly inferential (finding 18).
  - No proposed line names the owner, a place, a handle or an employer, or carries a session URL.
- §9 N1 to N17: the extractor gives 17 lines and each table reference resolves to the right one. N12 duplicates the existing §9 (finding 16).

No memory, past-chat, Project or web material was used. All facts come from the packet.

