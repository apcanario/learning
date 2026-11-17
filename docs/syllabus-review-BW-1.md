# Syllabus review BW-1: course BW after DD-BW3

Row S-BW (P125; Pedro, 16 Nov 2026, 23:45). Run on 17 Nov 2026 by a chat on Opus 5.5 (claude-opus-5-5; the row asked for Fable, recorded and carried on), with Pedro present to confirm each brief change. Rules: `docs/public-courses.md` §3, rules 6, 7 and 12 (a brief changes only here, and only as Pedro confirms; a correction is made in the chat that finds it, checked first). Inputs: `generator/data/building-with-ai/syllabus-flags.md` (F1 to F123), `units_data.py` with `AIMS`, `case-academy.md`, the thirteen filed units (`courses/building-with-ai/`), and, for the case-file needs, a fresh Opus 5.5 records extractor's report on the Project's records (`audits/building-with-ai/syllabus-review-BW-1-records.md`, saved from its `out/case-lines.md`). The course is complete (13 of 13): no unit is blocked, and the aim is briefs that match what was filed.

## 1 · What was sorted

Every flag whose status was `open` on 17 Nov 2026 (61), and the five `carried` flags the row names as case-fact needs (F83, F92, F99, F108, F109): 66 lines. Not sorted, because neither open nor named: the other carried flags (their units dealt with them) and the resolved ones (F25, F59, F98, F101, F112, F123). Two carried flags ask the syllabus review a question and get an answer in §4 without a line of their own: F11 (tier vocabulary) and F32 (which scheduled task).

The kinds, as in S-PB1:
- **(a)** a brief, Aim, Takes or Gives line, or the shared preamble, that does not match what was filed or what the case file holds: an exact replacement in `units_data.py`, applied only as Pedro confirms.
- **(b)** a filed unit that holds a mistake, a stale pointer or a statement the records now contradict: an exact replacement, checked by a fresh corrections checker with live search before it is applied, with a dated note in the unit and a line in the hub's `CHANGELOG`.
- **(c)** a fact the case file lacks that the Project's records hold, or a §9 line where they hold none: appended to `case-academy.md`, dated, private details removed.
- **(d)** left open, with the reason: a rule for the staleness checks of 15 and 16 May 2027 or for a later pass, a vendor page still to load, or the filling of unit cells from the facts (c) adds (carried proposal CP-4).

After the changes, (a), (b) and (c) flags are set to `resolved (S-BW, 17 Nov 2026: …)`; a (c) flag whose unit cells still read "not in the case file" says so and names CP-4; (d) flags keep `open` and gain "S-BW (17 Nov 2026): left open; <reason>."

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
| F28 | c | case file §7 | C2 (mirror lag: four instances). BW4 §5's case example: CP-4 |
| F29 | c | case file §7, §9 | C2 (stopped and restarted work: instances); §9 N6 (no count). BW3 §5 and BW4 §4 stand |
| F34 | d | BW4 | Left open: OpenAI's pages still to load; retried at the staleness checks |
| F35 | c | case file §1, §2, §9 | C1, C6 (one build order with dates; the decision dates); §9 N7 (no spec, no non-goals). BW5's [NOT IN CASE FILE] cells: CP-4 |
| F41 | d | BW5, DD-BW1 | Left open: a standing citation rule (the exact URL read) for the staleness checks and any corrections pass; no unit remains to receive it |
| F42 | b | BW3 | B4 below: BW3's convention gains a pointer to BW5 §5 and §9 |
| F43 | a + b | BW6 Takes line; BW5 Deliverable 1b | A2 below (BW6's Takes line reads BW1, BW2, BW3, BW5); B1 below (BW5's build order row 6 the same), applied only if A2 is confirmed |
| F45 | c | case file §5, §9 | C5 (findings not applied as given, per unit); §9 N8 (no total, no false-alarm rate). BW6 §6 stands |
| F46 | c | case file §3, §4, §9 | C3, C4 (claims and sections in the audits); §9 N9. BW6's [UNKNOWN] N: CP-4 |
| F47 | c | case file §4 | C4 (Audit 2's date, model, units; 3 of the 10 stale claims sampled). BW6 Deliverable H: CP-4 |
| F48 | d | BW6 | Left open: OpenAI's deep-research pages still to load; retried at the staleness checks |
| F51 | — | BW6 | Resolved by decision: BW6 stays search off (the build order and the index's staleness table are unchanged); its live-read product facts are re-read with the staleness checks of 16 May 2027, recorded on F88 |
| F52 | a | the shared preamble | A1 below: the case line in the case file's own wording, as F98, F112 and F123 did in three units |
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
| F92 | c | case file §2, §9 | C1 (rows run with the owner away); §9 N12 (whether he reads each unit before publishing). DD-BW1's cells: CP-4 |
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
| F115 | — | DD-BW3 | Resolved, no change (no contradiction found) |
| F116 | c | case file §8, §9 | C9 (how the chats were listed, the fields, breakdowns, pattern counts, rules tested, the review's date); §9 N16. DD-BW3 §6, Parts A and B: CP-4 |
| F117 | c | case file §8 | C9 (the review's own statement that the six days were a heavy-building week, not typical) |
| F118 | c | case file §8, §9 | C9 (where the working files were kept); §9 N17 |
| F119 | d | DD-BW3 | Left open until the check; its four pages are now named on F88 |
| F120 | d | DD-BW3, BW1, BW9 | Left open: the vendors' session-list and chat-search pages still to read |
| F121 | d | DD-BW2, DD-BW3 | Left open: a standing rule for any correction of DD-BW2 Part 2 (CP-4 included) |
| F122 | — | DD-BW3 | Resolved, no change (met) |

Count: 66 lines. (a) 3 (F52, F43, F113). (b) corrections B1 to B7 for 6 flags (F42, F43, F52, F60, F61, F89, F99; F43, F52 and F99 also (a) or (c)). (c) 33 (F4, F18, F19, F21, F26, F28, F29, F35, F45, F46, F47, F62, F63, F64, F71, F83, F92, F99, F102 to F110, F113's case half, F116, F117, F118). (d) 22 (F23, F34, F41, F48, F68, F69, F70, F73, F74, F75, F76, F77, F78, F82, F87, F88, F94, F97, F114, F119, F120, F121). Resolved with no change: 7 (F24, F51, F90, F91, F96, F115, F122).

## 3 · The exact changes

### Kind (a): briefs, applied only as Pedro confirms

Each is an exact replacement in `generator/data/building-with-ai/units_data.py`; the Current text occurs once in the file.

**A1 · The shared preamble's case line (F52; also F98, F112, F123).** Every unit's open brief and the course's Briefs page.

| Current | New |
|---|---|
| "Running case: Academy (real), a library of self-study courses built by one person with Claude in October and November 2026, each unit written by one model from a brief, checked by a fresh context and audited by sample. " | "Running case: Academy (real), a library of self-study courses built by one person with Claude in October and November 2026, with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library. " |

The New wording is the one the corrections checks passed for DD-BW1, DD-BW2 and DD-BW3. BW9 §8 (the one filed unit that still quotes the old line, "each unit written by one model from a brief, checked by a fresh context and audited by sample (Academy case file §1, §2)") is corrected by B7 below if A1 is confirmed.

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

**B1 · BW5 Deliverable 1b, row 6 (F43; only if A2 is confirmed).**

| Current | New |
|---|---|
| \| 6 \| BW6 · Research and verification \| BW1, BW3, BW5 \| BW8, BW9 \| \| | \| 6 \| BW6 · Research and verification \| BW1, BW2, BW3, BW5 \| BW8, BW9 \| \| |

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
| BW8 | Two changes, each for a script's sake: the claims table in item 1 carries a verdict column, so that a script can apply rule C5 rather than the model; and after one claim from every section, the extra draws are taken at random from all remaining claims, so larger sections give more draws in proportion, which is this unit's reading of BW6's "extra draws from the largest strata" in a form a script can repeat from its seed. | One change, for a script's sake: the claims table in item 1 carries a verdict column, so that a script can apply rule C5 rather than the model. After one claim from every section, the extra draws are taken at random from all remaining claims, so larger sections give more draws in proportion, as BW6 states the rule (corrected 17 Nov 2026), in a form a script can repeat from its seed. |

**B4 · BW3's convention on one brief per chat (F42).**

| Current | New |
|---|---|
| - One brief per chat. If the first output misses, change the brief and open a new chat (§5). | - One brief per chat. If the first output misses, change the brief and open a new chat (§5). In a specified project, where briefs are not reworded once work starts, the miss is raised as a flag and the brief changes at a boundary (BW5 §5, §9). |

**B5 · DD-BW2 §7 and Part 1 G (F99).** Source: case file §7 as C2 adds it, from the kit changelog of 4 and 9 Nov 2026.

| Current | New |
|---|---|
| **A publish that had to be repeated.** The case file records none. It says the site is published in two places after each filing, first as an artifact on claude.ai and then on GitHub Pages (§1, note), and that a script restores every file if the course index check fails (§1, note); it records no failed or repeated publish. If one happened, it is not in the record. | **A publish that had to be repeated.** The site is published in two places after each filing, first as an artifact on claude.ai and then on GitHub Pages (§1, note), and a script restores every file if the course index check fails (§1, note). The case file records two repeats (§7, added 17 Nov 2026): a layout fault found after a publish on 4 Nov 2026 was fixed and the site published a second time the same day, neither the change's checker nor the verify script having caught it; and on 9 Nov 2026 a GitHub Pages run failed with no job run and was retriggered with an empty commit. It also records publishes the tool first refused until the named files were read, and deploys that did not run when attaching the public repository was refused (§7). |
| Repeated publish: not recorded. | Repeated publish: 1, and 1 failed deploy retriggered (§7, added 17 Nov 2026). |

**B6 · BW7, Dell'Acqua et al.'s first posting (F89).** A check only: whether BW7's date of 22 Sep 2023 and the publisher's 18 Sep 2023 are two postings of the working paper. If they are, nothing changes; if BW7's date is wrong, the checker gives the exact replacement and it is applied after a second check.

**B7 · BW9 §8, the case line (F52; only if A1 is confirmed).**

| Current | New |
|---|---|
| each unit written by one model from a brief, checked by a fresh context and audited by sample (Academy case file §1, §2) | with a method of one brief per unit, a fresh check and sample audits that the case file records as run on part of the library (Academy case file §1, §2, §5, §9) |

### Kind (c): the case file

Appended to `generator/data/building-with-ai/case-academy.md` in its addendum style, each line prefixed with its section and dated, from the records extractor's report (lines and sources there), private details removed. Groups C1 to C9 and the §9 lines N1 to N17 are the extractor's proposed lines, kept word for word except where noted:

- **C1 (§2):** syllabus chats on Fable (F18); extraction by Sonnet 5.5 agents for the history bibliographies (F18); briefs and prompts (F19); length a guide (F21); rows run with the owner away (F92).
- **C2 (§7):** surfaces, memory, the knowledge's size and retrieval, token totals, a failure traced to a chat's length, usage-limit stops (F4); the seventeen structure-audit findings and their status on 16 Nov 2026 (F26); mirror lag (F28); stopped and restarted work (F29); skills (F62); scheduled tasks and unattended runs (F64); agents' tools, commits and branches, caps, after lost writers, who publishes (F71); where private material is kept (F83); the four publish lines (F99). The status lines of the seventeen findings use the fix list's own wording.
- **C3 (§3):** the research report's agents (Fable 5.1, 27 Oct 2026) (F18); Audit 1's nine sections and 91 claims (F46).
- **C4 (§4):** the auditing models (F18); Audit 2's date, model, units, samples per unit and the 3 of 10 stale claims inside the sample (F46, F47).
- **C5 (§5):** all 36 drafts written by Opus 5.5 and the rows' order (F18, F103); findings not applied as given, per unit (F45); who applied findings (F53, F102); the history courses' check pipeline (F104); the rewrite verdict read as fix (F106).
- **C6 (§1):** the private courses' build order with dates (F35); the layout's equivalents of INDEX.md, INSTRUCTIONS.md, BUILD-ORDER.md (F63); the start date and the history courses' word counts (F110); the gates before publishing (F53).
- **C7 (§9):** why Audits 3 onward did not run (F105).
- **C8 (§6):** the retrofit figure passes' counts, the drop after two failures in those passes beside §6's three, the figure checkers' model (F53, F107). §6's line itself is not changed: the course index records two units' figures dropped after a third check, so both rules ran.
- **C9 (§8):** the review's listing, fields, turn definition, breakdowns, pattern counts, rules tested and date (F116); typicality in the review's own words (F117); working files (F118); the ten ranked changes with their counts (F108); how long chats stayed open (F109). The changes are named by what they do, never by the private course's unit codes beyond those §5 already uses.
- **§9 N1 to N17:** the extractor's seventeen "records do not" lines, each naming its flags.

### The flags file

After the changes are applied, in `syllabus-flags.md`: each (a), (b) and (c) flag `resolved (S-BW, 17 Nov 2026: …)` naming its change; each (c) flag whose unit cells still say "not in the case file" adds "the units' cells: CP-4"; each (d) flag gains, at the end of its proposed change, "S-BW (17 Nov 2026): left open; <reason from the table>"; F88 gains "and BW6's and DD-BW3's live-read pages (F51, F119)"; F11 and F32 gain their answers (§4).

## 4 · Two carried questions answered

- **F11 (tier vocabulary).** No brief change: BW2's brief names tiers as a pattern, and BW2 records the four words (small, mid, large, large top rung) as the course's vocabulary; BW7 and BW10 use them. The flag gains "S-BW: BW2's four words are the course's tier vocabulary; no brief change."
- **F32 (which scheduled task).** No brief change: BW8 took BW4's rot check and said why (F60's record); the flag gains "S-BW: BW8's choice stands; no brief change."

## 5 · Carried proposal

- **CP-4 · Fill the BW units' "not in the case file" cells from the lines S-BW added to the case file** (F4, F18, F26, F28, F35, F46, F47, F62, F63, F64, F71, F83, F92, F103, F105, F106, F108, F114, F116; BW1, BW2, BW4 to BW10, DD-BW1 to DD-BW3), each replacement drafted by a fresh Opus 5.5 agent from the case file and checked by a fresh corrections checker before it is applied. ⚠ A pass over twelve filed units; it would put a BW corrections pass into W-SP1's chat, off that row's subject; Pedro may veto it there and keep it for a housekeeping row after W-DD-SP3.

## 6 · Fresh check of this proposal, verbatim

(Saved below once the checker returns, before any finding is applied.)
