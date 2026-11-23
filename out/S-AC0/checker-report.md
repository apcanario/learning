# S-AC0 · checker report

Checker: claude-opus-5-5, a fresh agent, 23 Nov 2026. Read: `inbox/athlete-career/docs/athlete-career-S-AC0-prompt.md` step 3, `docs/BACKLOG.md` row S-AC0 overrides 1 to 13, `out/S-AC0/registration.md`. Compared the working tree against git HEAD and `inbox/athlete-career/`. No file changed but this one (a temporary copy of HEAD's `kit/next_prompt.py` was run from `kit/` and deleted at once; `git status` afterwards shows the same set of changes as before). No memory, past-chat, Projects, connector, Artifact or web tool used.

Verdict: **1 PASS, 2 PASS (one should-fix), 3 PASS, 4 PASS, 5 PASS (one minor), 6 PASS, 7 PASS, 8 PASS, 9 PASS, 10: three findings.**

## 1. briefs.md byte-identical: PASS

`sha256sum`: `courses/athlete-career/briefs.md` and `inbox/athlete-career/courses/athlete-career/briefs.md` both 33308c81d6b43c334d72b4cd482196d533855f2b11335c05831bb50fcdfe1cc3; `cmp`: identical; equal to `inbox/SHA256SUMS`.

## 2. Units in course.toml: PASS, with one should-fix

Script (tomllib) over `inbox/athlete-career/docs/athlete-career-units.toml` and `courses/athlete-career/course.toml`: all 18 codes present; title and scope equal for every unit; `aim` equals the design's Aim with the first letter lower-cased and the final stop dropped (the pack form; `kit/mdcourse.py` adds the stop); `deliverable` equals Ships less its stop; the search flag in `order` equals `search` for every unit (off: AC6, AC7, AC10, AC15). `order` = AC1..AC15, DD-AC2, DD-AC1, DD-AC3. Outcomes: three, word for word with syllabus section 3 (lines 70-72), each with its unit list. `sourcing_part = "Part 11"` (line 29). No `reliefs` key anywhere in the file; no `part` key in any unit. Pack keys `color`, `title`, `bar`, `brand_html`, `out`, `theme_key`, `learn_c`, `build_c`, `home_h1`, `order_lede` present, in the form of `courses/ai-in-supply-chain-execution/course.toml` (lines 44-55 there). `pages/` holds the same five files as supply-chain-execution and ai-in-supply-chain-execution.

**Should-fix (S1): the deep dives' reading order is inverted.** `[[pack.courses.units]]` lists DD-AC2 before DD-AC1 (course.toml, the DD-AC2 block precedes the DD-AC1 block). `kit/build.py` lines 745-748 sort reading pages, the sidebar and the pager's Previous/Next by this list's order ("reading pages in the course's own unit order"), so Academy would read DD-AC2 before DD-AC1. The design's reading order (units.toml; syllabus section 4 table, lines 98-100) is DD-AC1, DD-AC2, DD-AC3, and the course's own `order_lede` says the writing order differs from the reading order only in that DD-AC2 is *written* first. Precedents (sport-psychology, supply-chain-execution) keep the units list in reading order. Fix: move the DD-AC1 block above DD-AC2 in `[[pack.courses.units]]`; leave `order` as it is. Registration item 5 ("all 18, in the design's order") is then true; as it stands it is not.

Minor (M1): Takes on AC3 reads "AC1 to AC2"; the AIE precedent writes two codes as "AIE1, AIE2" and keeps "to" for three or more. Suggest "AC1, AC2". Takes and Gives are the registrar's own (the design gives none); disclosed in registration item 5.

## 3. Case facts against Sport Psychology's register: PASS

Read `courses/athlete-career/notes/case-facts.md` and `courses/sport-psychology/notes/case-facts.md` in full (base entries and every "Added by units" row through DD-SP3). Every carried fact matches: Sara (20, 400 m, second year, first senior season, away from home, eight months back from a season-costing hamstring injury, group of six, coach a man (SP9) of 20 years who coaches two other groups including under-18s (SP9), club welfare officer (SP9), exams January and June (SP2), referral to student health under way: SP9's "appointment is booked" extends rather than contradicts it); Dani (girl, 14, title at 13, five sessions, school weekdays, both parents at competitions, coach a man of 15 years, former competitor, squad 18 aged 11-17, welfare officer (SP1), second coach (SP8), chose the class above with both parents (DD-SP2), eating referral continues (SP6, DD-SP2)); Milan (17, midfielder since 11, decision in the weeks of his final exams (SP2, SP10)). The commercial layer adds facts the register is silent on; none contradicts it; coaches and parents stay unnamed; "Ivo" collides with no register name. Note, not a contradiction: "In AC14 he faces release" should be read by AC14's writer as the possibility of release, since the register leaves the academy's decision open (SP10: weeks 35-38).

## 4. Part 11 appended whole: PASS

Script: the text of `docs/sourcing-standard.md` from "## Part 11 ·" to end equals `docs/athlete-career-sourcing-part-9.md` (inbox) with only "## Part 9 ·" changed to "## Part 11 ·" (5,088 bytes each; the design file has one "Part 9" only). `git diff -U0`: one line changed (the header: "Parts 2 to 10" -> "Parts 2 to 11", plus "; Part 11 from its course's shared preamble"), one blank line and the part appended; Parts 1-10 untouched (headings at lines 7-183 unchanged).

## 5. Prompts document, sections 1 to 5: PASS, with one minor

`diff` of lines 1-117 of `docs/athlete-career-prompts.md` against the design file: seven lines differ, each Part 9 -> Part 11 (lines 6, 41) or the owner's name -> "the owner" (lines 68, 72, 87, 114, 116); then "---" appended. All match `out/S-AC0/prompts-changes.md` A1-A7. In the template part (lines 121-239): every writer rule 1-14 and every checker pass 1-7 of the design appears word for word (script); section 3's eighteen paragraphs are word for word in the four-column table; the carry-forward rule's nine points are word for word. Rules 15 and 16 differ in the template copy only as disclosed (registration item 13).

**Minor (M2):** rule 16 in the template (line 185) appends the Execution template's hand-in rule, which still says "**Case facts** (rule 8), **Contradictions** and **Needs** (rule 11)". Those are the Execution course's rule numbers; in this course the case is rule 13 and flags are rule 15 (rule 8 here is Money, rule 11 The roles). Fix: "(rule 13)" and "(rule 15)" in that appended sentence.

## 6. Courses index: PASS

`docs/courses-index.md` lines 137-160: section "## Managing an Athlete's Career (public)" before "## Courses to come (Personal Mythology)"; paragraph has "0 of 18 written."; 18 rows numbered 1-18 in writing order (AC1..AC15, DD-AC2, DD-AC1, DD-AC3), each "not written | Opus 5.5 | on/off" with the search flag matching `order`, path `courses/athlete-career/<code>-<slug>.md`. `python3 kit/index_check.py`: "courses-index.md matches the sources".

## 7. kit/next_prompt.py: PASS

`git diff kit/next_prompt.py`: one line, `QUEUE` gains `'athlete-career'` last; HOLDS, GATES, CLONE unchanged. `python3 kit/next_prompt.py --row W-SCE3` (SCE is 2 of 20 written, so W-SCE3 is that course's next unfiled row): HEAD's file run on the current tree, the current file, and HEAD's file on a `git archive HEAD` copy in /tmp all give the same bytes, sha256 8b4cce450497cadbe87131d974484fed93e4517c6b6228c87e1e9162e229f8e0 (= the registrar's). `python3 kit/next_prompt.py --row W-AC1`: exit 0, first line the clone line, no unfilled `{SLOT}`, line 45 "**This row in particular.** Search on. This unit sets the grade key and the glossary ...". No flag printed (F1-F3 resolved, F4 dropped), as expected.

## 8. Scope of changes, BACKLOG, flags: PASS

`git status`: modified `catalog.toml`, `docs/BACKLOG.md`, `docs/courses-index.md`, `docs/public-courses.md`, `docs/sourcing-standard.md`, `docs/sports-track-coming-soon.md`, `kit/next_prompt.py`; new `courses/athlete-career/`, `docs/athlete-career-prompts.md`, `docs/athlete-career-syllabus.md`, `out/S-AC0/`. No other kit .py file changed. No HOLDS or GATES entry. `inbox/`: no change in git status; `sha256sum -c inbox/SHA256SUMS`: all OK. BACKLOG: S-AC0 at line 314; W-AC1..W-DD-AC3 at lines 339-380 under five `####` bundle headings (1: AC1-4; 2: AC5-8; 3: AC9-12; 4: AC13-15, DD-AC2; 5: DD-AC1, DD-AC3 and closing corrections); first row of each holds the starter, the others "runs in the chat of <first row>"; G-R-AC under Proposed at line 440 after G-R-AIE, with the fourteen candidates and their expected units; no R-AC, no gate row, no P-AC row. `courses/athlete-career/notes/syllabus-flags.md`: F1-F3 Affects "AC1 to AC15, DD-AC1, DD-AC2, DD-AC3", F4 "none" (dropped, moved to G-R-AC); "every unit" occurs only in the header sentence that forbids it (line 3).

## 9. Owner's name and employer: PASS

`python3 kit/private_terms.py` (default run): "167 files, 0 private terms, 170 warnings: OK", exit 0. Explicit run on every new file: failing hits are the repository handle in clone lines only (accepted precedent: `docs/athlete-career-prompts.md` 101, 110, 128; `docs/athlete-career-syllabus.md` 123; `out/S-AC0/` files) and a private course id in `out/S-AC0/np-before.txt`/`np-after.txt` line 24 (the script's own print, in `out/`; neither the owner's name nor the employer). Script over `git diff -U0` added lines with every plain and employer term of `kit/private-terms.txt`: no employer term; the owner's name only on the one `docs/public-courses.md` line whose old text already held it. Owner-name counts per changed file, HEAD -> now: public-courses.md 15 -> 15, BACKLOG.md 53 -> 53, courses-index.md 1 -> 1, next_prompt.py 39 -> 39, others 0 -> 0. No employer term in any new file.

## 10. Registration "Differences from the design": findings

1. **S1 above (should-fix):** item 5 says the units are "in the design's order"; they are in writing order, which inverts DD-AC1 and DD-AC2 in Academy's reading order. Apply the S1 fix.
2. **`out/S-AC0/expected.txt` is likely incomplete (should-check, main chat).** It lists only the twelve `built.html` paths. The AIE precedent (`out/S-AIE0/expected.txt`) also listed the new course's pages, `README.md`, `academy/changelog.html` and `academy/index.html`; this row also changes the Sports track (catalog `planned`, `planned_note`), so `academy/index.html` (and any track page) will differ. The registrar says so (item 22); the main chat should add those paths before `kit/land.py land --expected`, or land will report undeclared differences.
3. **`docs/sports-track-coming-soon.md` left stale (minor, disclosed in item 12):** its 19 Nov scope, "Neither course below is a backlog row yet" and "Neither syllabus is written before Sport Psychology is complete" now contradict the syllabus and the queue. For the main chat to decide; not this checker's to fix.

Other items 1-4, 6-11, 13-20 checked against the files: they agree with what the files show (Part 11 everywhere the design said Part 9 except the inbox copies; pack keys as listed; outcome closing sentence omitted as stated; the five pages use theme classes with `--hc` as the only inline style; flags F1-F4 as stated; QUEUE placement last; catalog changes as stated; reader line equal to syllabus line 57 with a final stop; syllabus diffs limited to the stated edits a-d).

## For the applier

- S1: `courses/athlete-career/course.toml`: move the `[[pack.courses.units]]` block of DD-AC1 above that of DD-AC2. Then `python3 kit/index_check.py`.
- M2: `docs/athlete-career-prompts.md` line 185, in the appended hand-in text: "(rule 8)" -> "(rule 13)", "(rule 11)" -> "(rule 15)"; add the change to `out/S-AC0/prompts-changes.md`; re-run `python3 kit/next_prompt.py --row W-AC1` (exit 0) and `--row W-SCE3 | sha256sum` (8b4cce45...).
- M1 (optional): AC3 `takes = 'AC1, AC2'`.
- Main chat: complete `out/S-AC0/expected.txt` (finding 10.2); decide on `docs/sports-track-coming-soon.md` (10.3).
