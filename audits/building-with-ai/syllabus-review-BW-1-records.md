# Case-file lines proposed from the records (syllabus review, 17 Nov 2026)

Extractor: claude-opus-5-5, working only in the packet. Sources are cited as packet paths and line numbers (`records/<file>:<line>`), or as section numbers where a record has them. Every proposed line follows the case file's convention: the owner is "the owner", the two private courses are "the marketing course" (units A…, DD-A…) and "the AI course" (units B…, DD-B…). No line quotes the owner, names a person, a place, a handle, an employer or a health detail, and none names a private repository. Where a record's own words would carry a private term, the line says it generically.

---

## F4 · Surfaces, plan, memory, token or window measures, failures traced to a long chat or retrieval

**Fact needed:** which surfaces the project ran on and on which plan; whether memory was on; any token or window measure for a unit; whether any failure was traced to a long chat or to retrieval mode.

**Found:**

- §7 · Surfaces (the method's Home line, 28 Oct 2026; the AI course's B4, Deliverable A and unsure item 1, 29 Oct 2026; the project changelog's session links, 10 to 17 Nov 2026): the project's chats ran in one claude.ai Project, which holds copies of files from the repository; filing and writing rows from 10 Nov 2026 on ran as Claude Code sessions on claude.ai attached to that Project, and the Project's documents were seen there as a list by name, which may differ from what a claude.ai chat receives.
  Source: `records/method.md:7`; `records/B4-context-engineering.md:363`, `:531`; `records/docs-CHANGELOG.md:7`–`:23` (session links of the form claude.ai/code/session_…).
- §7 · Memory (the AI course's B4, finding F13, 29 Oct 2026; the AI course's DD-B2, §5, 2 Nov 2026; the B4 fix list, 16 Nov 2026): on the Project's setup as of 28 Oct 2026 account memory flowed into the Project beside the Project's own memory store; in 6 of 53 chats reviewed for DD-B2 the visible turns show the model calling the memory tool; on 16 Nov 2026 the setting was not visible in the records.
  Source: `records/B4-context-engineering.md:377`, `:456`; `records/DD-B2-deep-dive-his-unknown-unknowns.md:102`; `records/p30-b4-fixes.md:116`.
- §7 · Window and retrieval (the AI course's B4, finding F1, 29 Oct 2026, figures as corrected 15 Nov 2026): the Project's knowledge held 33 files, 907,260 characters (about 363,000 tokens at 2.5 characters a token); whether the Project ran in retrieval mode depended on the model and was not known.
  Source: `records/B4-context-engineering.md:385`, `:531`.
- §7 · Token measures (the kit changelog, 27 Oct and 14–15 Nov 2026): the history courses' curated bibliographies were written by one Sonnet 5.5 agent per unit group, 26 groups, about 4.5 million tokens; the public marketing course's four audits used 2.83M tokens for the twelve unit audits and 3.64M for every agent measured.
  Source: `records/kit-CHANGELOG.md:1203`, `:256`.
- §7 · A failure traced to a chat's length (the project changelog, 12 Nov 2026): a chat that had filed two units could not refresh the remaining Project copies, because each needed its whole text read into the chat and the chat's context could not hold it after two units; the rest moved to a later row.
  Source: `records/docs-CHANGELOG.md:77`.
- §7 · Usage limits (the kit changelog, 25 Oct 2026; the project changelog, 14 Nov 2026): the largest history writing session (28 reports) stopped twice on usage limits and resumed both times; an audit chat on 14 Nov 2026 was stopped by a shorter-window limit of the auditing model after 18% of that model's weekly allowance.
  Source: `records/kit-CHANGELOG.md:1297`; `records/docs-CHANGELOG.md:60`.

**Records hold none:** the plan the project runs on; a token or window measure for a single unit's writing; any failure traced to retrieval mode. Searched: all records for "Max", "Ultra", "Pro plan", "subscription", "plan", "weekly limit", "retrieval", "window", "token", "compact", "usage limit".

---

## F18 · Models and effort by task, writing models, research agents, audits after the newer model, cost, recurrence

**Fact needed:** which model and effort ran triage, extraction, summaries, searching, code changes and syllabus work; effort for writing, checking, auditing; which model wrote each of the 36 fresh-checked drafts; the research agents' model; whether audits after the newer auditing model ran on it; cost, usage or time per unit or task; how often each routed task recurs.

**Found:**

- §8 · Model by task type (the AI course's DD-B2, §2 table, over the 53 chats of 28 Oct to 2 Nov 2026, model read from commit trailers): unit writing 15 chats, Opus 5.5 14, switched 1; infrastructure (build, repository, publishing, method and skill files) 15, Opus 5.5 5, Fable 5.1 8, switched 2; figure passes 7, Opus 5.5 6, Fable 5.1 1; audits and fresh checks 6, Opus 5.5 1, Fable 5.1 5; status questions 6, Opus 5.5 3, Fable 5.1 2, switched 1; syllabus design 2, Fable 5.1 2; history-module writing 2, Opus 5.5 2. None ran on Sonnet 5.5 or Haiku 5.5.
  Source: `records/DD-B2-deep-dive-his-unknown-unknowns.md:36`, `:42`–`:52`.
- §2 · Syllabus chats (the method, 15 Nov 2026; the project changelog): from 15 Nov 2026 course design and syllabus chats run on Fable; the two public courses were created on Fable 5.2 (11–12 Nov 2026) and the UX syllabus review ran on Fable 5.1 (3 Nov 2026).
  Source: `records/method.md:102`; `records/docs-CHANGELOG.md:90`, `:114`.
- §2 · Extraction (the kit changelog, 27 Oct 2026): the curated bibliographies of the 137 history reports then written were made by Sonnet 5.5 agents, one per unit group.
  Source: `records/kit-CHANGELOG.md:1203`, `:1240`.
- §2 · Effort (the AI course's DD-B2, §1 and §3, 2 Nov 2026): the effort setting is recorded in none of the 53 chats reviewed.
  Source: `records/DD-B2-deep-dive-his-unknown-unknowns.md:28`, `:42`, `:74`.
- §5 · Writing model of the 36 fresh-checked drafts (the course index, unit tables): every one of the 36 was written by Opus 5.5.
  Source: `records/courses-index.md:61`–`:84` (Model column), `:92`–`:106`.
- §3 · The research report's agents (the course index; Audit 1's provenance note, 28 Oct 2026): the research report behind the first three marketing units was written on 27 Oct 2026 across five tracks by Fable 5.1 research agents.
  Source: `records/courses-index.md:60`; `records/audit-1.html` (Verdicts, "Provenance").
- §4 · Auditing model (the course index; the project changelog): Audits 1 and 2 of the marketing and AI courses ran on Fable 5.1 (28 and 29 Oct 2026); the four audits of the public marketing course ran on Fable 5.2 (14–15 Nov 2026); no audit of the private courses or the UX course ran after Audit 2 (see F105).
  Source: `records/courses-index.md:65`, `:70`, `:118`, `:123`, `:128`, `:129`.

**Records hold none:** effort used for writing, checking or auditing; cost, usage or time per unit or per task; how often each routed task recurs; which model ran triage, summaries or searching as separate tasks (the review's task types do not include them). Searched: DD-B2 §1–§8, both changelogs, the course index, the method, for "effort", "triage", "summar", "cost", "hours", "per unit".

---

## F19 · The texts of a unit brief, the shared preamble, the fresh-check prompt and the audit prompt

**Fact needed:** whether the records hold these texts, and where.

**Found:**

- The shared preamble and the unit briefs of this public course are public: `PRE`, the unit entries and `AIMS` in `units_data.py` (packet copy, lines 7–36, 37–91, 92–132). A unit's brief is the preamble, the unit's Aim, Takes and Gives lines and its own brief, joined (the method §4, Brief template).
- The method holds the brief template verbatim (a shared preamble template and a unit-brief template): `records/method.md:121`–`:143`.
- The method holds the staleness-check prompt verbatim: `records/method.md:158`–`:162`.
- Proposed line: §2 · Briefs and prompts (the method §4 and §6, 15 Nov 2026; this course's data file): a brief is the course's shared preamble, written once and never edited per unit, followed by the unit's own brief; this course's preamble and briefs are public in its data file and on its Briefs page; the staleness check is run with one fixed prompt that the method gives word for word; the private courses' briefs are not reproduced here.

**Records hold none:**
- A private course's unit brief as text: the records name the AI course's B4 brief file and paraphrase its items (`records/fresh-checks/fresh-check-B4.md:14`, Coverage), and B4 finding F15 records that private-course briefs carried private terms (`records/B4-context-engineering.md:460`); no brief text is held.
- The fresh-check prompt: the method describes it (`records/method.md:147`–`:148`); the records name its source (`skills/audit-units` §3b, `reviews/units-9-13/BRIEF.md`) but hold no copy (`records/fresh-checks/fresh-check-IA4.md:118`).
- The stratified-sample audit prompt: B4 F12 records it as 1,547 characters, identical in the method and the AI course's data file on 29 Oct 2026, and retired on 15 Nov 2026 (`records/B4-context-engineering.md:454`; `records/p30-b4-fixes.md:112`); no copy of its text is held.
Searched: all records for "You are auditing four units", "You are re-checking one unit", "BRIEF.md", "verbatim", "brief".

---

## F21 · Whether the unit length was wanted

**Fact needed:** whether the 2,000 to 6,000 range bounded length by intent, and whether the long outputs were wanted.

**Found:**

- §2 · Length (the kit changelog, rules set by the owner on the afternoon of 27 Oct 2026; the method §4): the owner set that length is a guide, not a law: a topic takes the words it needs; the word-count script reports the count as a note and never fails on it; padding is the fault, length is not; the rule was then carried into the method for every course.
  Source: `records/kit-CHANGELOG.md:1238`–`:1239`; `records/method.md:25`, `:107`–`:108`.
- §5 · Long units at the fresh check (the AI course's B4 fresh-check report, 29 Oct 2026): the checker counted B4 at 8,508 words against the brief's 2,000–6,000 and, on the method's length rule, found nothing in it to be padding.
  Source: `records/fresh-checks/fresh-check-B4.md:14`.
- §2 · Records of later units (the project changelog, 12–13 Nov 2026): several units of the public marketing course were filed "above the brief's guide", the record noting that the length rule lets the topic decide.
  Source: `records/docs-CHANGELOG.md:62`, `:73`, `:80`.

**Records hold none:** a statement by the owner on the length of the longest UX unit in particular. Searched: both changelogs, the course index, the method for "length", "words", "guide", "too long", "shorter".

---

## F26 · The structure audit's seventeen findings

**Fact needed:** each finding's layer, kind and fix.

**Found** (the AI course's B4, Deliverable C and F, 29 Oct 2026, corrected 15 Nov 2026; the status of each on 16 Nov 2026 from the fix list `records/p30-b4-fixes.md`). B4 names each finding's layer, evidence, fix, effort and (in F) severity; it does not label findings by the kinds the flag names, so the kind below is given only where B4's own title or evidence uses the word, and is otherwise left out. Proposed lines, one per finding:

- §7 · Structure audit F1 (B4, 29 Oct 2026): layer Project knowledge; the knowledge held 33 files, 907,260 characters, mostly files no chat needed whole (size); fix: cut it to five files and read the rest from the repository by path; severity high. Status 16 Nov 2026: still applies in part (filed units removed from the knowledge on 15 Nov 2026).
- §7 · Structure audit F2 (B4): layer Project knowledge; the project instructions were also uploaded as a knowledge file, the same text reaching the Project twice (duplicate); fix: remove the knowledge copy; severity low. Status 16 Nov 2026: still applies (no record of removal).
- §7 · Structure audit F3 (B4): layer Project knowledge; the knowledge copy already lagged the repository: two units filed on 29 Oct 2026 were missing from the list seen the same day (stale); fix: stop mirroring units, refresh the rest from the repository; severity low. Status 16 Nov 2026: done (units are no longer mirrored, and every chat rewrites the copies it changes).
- §7 · Structure audit F4 (B4): layers repository and knowledge; two different files carried the same name, one the queue of chats and one a writing-lane file, with 39 references by bare name in 16 files; fix: rename one and repoint the references; severity low. Status 16 Nov 2026: still applies.
- §7 · Structure audit F5 (B4): layers the owner's account preferences and the project instructions; three preferences collided with the Project's work (contradiction): a format rule, a concision rule and a rule against volunteering next steps, against long-form Markdown units and the required hand-over; fix: one clause in the preferences and a scope paragraph in the instructions; severity medium. Status 16 Nov 2026: no longer applies.
- §7 · Structure audit F6 (B4): layers preferences and theme; the design preferences and the site's theme agreed; no fix; recorded so a later audit would not re-check it. Status 16 Nov 2026: no longer applies.
- §7 · Structure audit F7 (B4): layer project instructions; the instructions (675 words) carried procedures and paraphrased the method file (duplicate); fix: replace them with rules and pointers; severity medium. Status 16 Nov 2026: still applies; the instructions had grown to 862 words.
- §7 · Structure audit F8 (B4): layers method, setup file, data file; four prose copies of the list of units that search, in three versions (duplicate, contradiction); fix: point each to the course index's Search column; severity medium. Status 16 Nov 2026: still applies.
- §7 · Structure audit F9 (B4): layers repository docs and data file; stale files and lines still read as current (stale): an old hand-off note, retired page blocks rendered on the site, a wrong due date, a contradictory lane heading, two references to a retired build script; fix: archive or correct each, then rebuild and publish; severity medium. Status 16 Nov 2026: one of five parts done.
- §7 · Structure audit F10 (B4): layers queue and changelog; the queue and the record were behind the work: two filed units still queued, no changelog row (stale); fix: move both rows; severity medium. Status 16 Nov 2026: done.
- §7 · Structure audit F11 (B4): layer build; the theme reached the build through a hand copy that no check compared; fix: build from the theme directly, or fail the verify script on a mismatch; severity low. Status 16 Nov 2026: still applies.
- §7 · Structure audit F12 (B4): layers method and data file; the two audit prompts lived in two files, identical that day (duplicate); fix: a rot check, then generate one copy from the other; severity low. Status 16 Nov 2026: no longer applies (the sample-audit prompt retired 15 Nov 2026).
- §7 · Structure audit F13 (B4): layer memory; account memory flowed into a Project whose output is published; fix: turn off account memory for the Project; severity high. Status 16 Nov 2026: still applies (the setting not visible in the records).
- §7 · Structure audit F14 (B4): layer connectors; eight connectors were connected and no Project procedure used one; fix: set tool access to load on demand; severity low. Status 16 Nov 2026: still applies.
- §7 · Structure audit F15 (B4): layer the build and the data it reads; private terms reached three files of the public build (privacy); fix: a build-time redaction list kept outside both repositories, an erratum, a verify-script check, and the owner's decision on the public repository's history; severity high. Status 16 Nov 2026: still applies in part (a terms list and a checker exist; the erratum, the scan's scope and the decision not shown).
- §7 · Structure audit F16 (B4): layer scheduled tasks; nothing checked for rot between sessions (no scheduled task); fix: a weekly scheduled rot check; severity medium. Status 16 Nov 2026: still applies.
- §7 · Structure audit F17 (B4): layer the course index; the index every chat needs was 56% a finished record (size); fix: split it into a live index and an archive; severity low. Status 16 Nov 2026: still applies.
- §7 · Structure audit, status (the fix list, 16 Nov 2026): of B4's seventeen findings, 12 still apply, 2 are done (F3, F10) and 3 no longer apply (F5, F6, F12); none had been worked.

Sources: `records/B4-context-engineering.md:370`–`:381` (layer table), `:385`–`:464` (F1–F17), `:503`–`:523` (fix list with severity); `records/p30-b4-fixes.md:156`–`:178`; `records/docs-CHANGELOG.md:56` (unit copies removed 15 Nov 2026), `:12` (P30 row, 17 Nov 2026).

---

## F28 · A mirror falling behind its source

**Fact needed:** any recorded instance of a copy (a project copy, pasted instructions) falling behind its source.

**Found:**

- §7 · Mirror lag (the AI course's B4, finding F3, 29 Oct 2026): two units filed on 29 Oct 2026 were not in the Project's knowledge list seen the same day, although the filing procedure required the re-upload.
  Source: `records/B4-context-engineering.md:436`.
- §7 · Mirror lag (the project changelog, 28 Oct 2026): the build kit handed over to be put into the new repository was the previous session's copy, not the latest; the later session's changelog entry was restored from the live page.
  Source: `records/docs-CHANGELOG.md:186`.
- §7 · Mirror lag (the project changelog, 12–13 Nov 2026): after two units were filed in one chat, ten Project copies were stale and were re-uploaded from the repository by a separate correction row the next day, the first chat's context having been unable to hold them.
  Source: `records/docs-CHANGELOG.md:77`, `:66`.
- §7 · Site lag (the kit changelog, 10 Nov 2026; the project changelog, 12 Nov 2026): a prompt corrected in the repository after a publish stayed uncorrected on the site's Backlog page until the next publish, the repository being canonical; on 12 Nov 2026 the published Backlog page showed a confirmed item as still proposed until the next publish.
  Source: `records/kit-CHANGELOG.md:496`; `records/docs-CHANGELOG.md:83`.
- §7 · The second publishing place behind the first (the kit changelog, 12–15 Nov 2026): in five filing sessions the site was published as the claude.ai artifact but not deployed to GitHub Pages (the repository attach refused or outside the session's set); later rows deployed it.
  Source: `records/kit-CHANGELOG.md:332`, `:320`, `:283`, `:270`, `:24`; `records/docs-CHANGELOG.md:58`, `:49`, `:70`.
- §7 · Mirror rule (the method §8 step 4, 15 Nov 2026): each chat that works a row rewrites the Project copies of the backlog and changelog in full, so the Project knowledge never lags the repository; units are not mirrored.
  Source: `records/method.md:207`.

---

## F29 · Chats abandoned and briefs rewritten after a miss

**Fact needed:** a count of chats abandoned and briefs rewritten after a miss.

**Found** (instances; no count):

- §7 · Stopped and restarted work (the project changelog and kit changelog, 2 to 16 Nov 2026): on 3 Nov 2026 the owner stopped a UX writing row before its writer had a draft, its one commit was reverted, and a syllabus review the same morning added Aim, Takes and Gives lines to every unit brief of that course and closed four briefs at their seams, which the owner approved; a writer sent its prompt with the brief left as a placeholder was stopped before its first tool call and a new one started (2 Nov 2026); a writer of the public marketing course was stopped by the owner before it saved anything and started again from scratch (13 Nov 2026); a mapping agent's first run stopped because two of its tools were not loaded, and it was resumed (16 Nov 2026).
  Source: `records/docs-CHANGELOG.md:114`, `:117`, `:62`, `:14` (G-R row); `records/kit-CHANGELOG.md:716`.
- §3 · Rewrites from the brief (the course index): the three marketing units Audit 1 failed were rewritten from their briefs on 28 Oct 2026, each in its own chat; one section of a marketing unit was rewritten on 29 Oct 2026 and re-checked.
  Source: `records/courses-index.md:61`–`:63`, `:69`.

**Records hold none:** a count of chats abandoned, or of briefs rewritten, after a miss. Searched: both changelogs, the course index, site log, DD-B2 for "stopped", "abandon", "restart", "started again", "reverted", "rewritten".

---

## F35 · Spec, non-goals, preamble and brief text, a unit list with Takes and Gives, decision dates

**Fact needed:** a spec document; non-goals; preamble or brief text; one course's unit list in build order with its Takes and Gives; the dates of the decisions in BW5 Deliverable 1e.

**Found:**

- Preamble and brief text: see F19 (this course's own, public, in its data file; the method's template).
- §1 · One course's build order (the course index, 3 Nov 2026): the two private courses' 22 units in build order, with the date each was written: A9, A2, A6 and B1 (28 Oct 2026), B2 (28 Oct), B3, B4, A1, DD-B3, A3, B5, A4 (29 Oct; A1 written out of order beside B3), A5 (1 Nov), B7, A7, A8, B6, B8, DD-A1, DD-B1, DD-A2 (2 Nov), DD-B2 (3 Nov, last of both courses, since it reviews the chat history).
  Source: `records/courses-index.md:58`–`:84`; `records/method.md:91`.
- Takes and Gives: the private courses' briefs carry none; the UX course's briefs gained Aim, Takes and Gives lines on 3 Nov 2026 (not in the packet); this course's Takes and Gives are public in its data file (`units_data.py:92`–`:132`).
  Source: `records/method.md:142`; `records/courses-index.md:88`.
- §2 · Decision dates (the method and the kit changelog), proposed as one line: length a guide, not a law (27 Oct 2026); the per-unit fresh check made a rule for the marketing and AI courses after Audit 1 (28 Oct 2026); the repository as the single home (28 Oct 2026); an isolated agent context counts as a new chat (29 Oct 2026); the figure pass added to writing (29 Oct 2026); each chat writes the next row's prompt (31 Oct 2026); every new course a Markdown course (31 Oct 2026); figures fixed until they pass, never dropped (3 Nov 2026); corrections made in the chat that finds them (12 Nov 2026); the standing proposals rule, the thin main chat, units not mirrored into the Project, the end of the audit stage and the site's Backlog and Changelog drawn from one plain log (15 Nov 2026).
  Source: `records/kit-CHANGELOG.md:1238`; `records/method.md:7`, `:51`, `:53`, `:73`, `:97`, `:102`, `:115`, `:148`, `:200`, `:205`, `:207`, `:208`.

**Records hold none:** a spec document for any course; any recorded non-goals; the decisions of BW5 Deliverable 1e by name (that deliverable is not in the packet). Searched: all records for "spec", "non-goal", "out of scope".

---

## F45 · Fresh-check findings rejected or adjusted after verification

**Fact needed:** a count of findings the maintainer rejected or adjusted.

**Found** (per unit, the records' own words; no total is recorded):

- §5 · Findings not applied as given (the course index and the fresh-check reports' maintainer notes, 28 Oct to 10 Nov 2026): A2, one note not applied; A8, one finding held in part; DD-A1, one applied in part; DD-B2, one error applied in part and one should-fix not applied; IA3, one held in part; IA5, one in part and one needing no change; IA6, one pointer that held, not applied; IA8, the search-flag finding not applied (the flag kept off); IA10, one minor recorded at its own fix of no change; IA11, one in part; DD-IA2, three minors needing no change; DD-IA3, one minor needing no change. Every other of the 36 units' findings is recorded as applied.
  Source: `records/fresh-checks/fresh-check-A2.md:300`; `records/fresh-checks/fresh-check-A8.md:162`; `records/fresh-checks/fresh-check-IA3.md:137`; `records/fresh-checks/fresh-check-IA5.md:126`; `records/fresh-checks/fresh-check-IA10.md:92`; `records/fresh-checks/fresh-check-IA11.md:165`; `records/courses-index.md:81`, `:84`, `:97`, `:99`, `:101`, `:102`, `:105`, `:106`; `records/docs-CHANGELOG.md:109`.
- §5 · This course (the project changelog, 15–16 Nov 2026): BW5, 17 applied and 1 held; BW6, 12 applied and 1 held (the search flag); BW8, 22 applied and 1 held; DD-BW3, 12 applied and 2 minor held; BW1 to BW4, BW7 and BW9 all applied.
  Source: `records/docs-CHANGELOG.md:29`, `:39`, `:36`, `:37`, `:38`; `records/kit-CHANGELOG.md:10`, `:14`, `:15`, `:16`, `:17`.

**Records hold none:** a total of rejected or adjusted findings, or a false-alarm rate. Searched: the 37 fresh-check reports' maintainer notes, the course index, both changelogs.

---

## F46 · Checkable claims and sections per unit

**Fact needed:** N (checkable claims) and the section count for the case's units.

**Found:**

- §3 · Audit 1 (Audit 1's report, 28 Oct 2026): the three marketing units were audited as one document of nine sections, 91 cited claims in the full audit; B1 had seven sections and a deliverable.
  Source: `records/audit-1.html` (sections "Verdicts" and "1 · The sample").
- §4 · Audit 2 (Audit 2's report, 29 Oct 2026): one claim per numbered section plus the deliverable: B2 9 sampled and 23 checked, B3 6 and 28, B4 6 and 20, A1 7 and 25.
  Source: `records/audit-2.md:17`, `:37`, `:60`, `:83`, `:107`.
- §1 · Sections (the project changelog, 1 Nov 2026): every unit and report then on the site, 152 pages, held 1,581 sections.
  Source: `records/docs-CHANGELOG.md:131`.
- §4 · The public marketing course's audits (the kit changelog, 14–15 Nov 2026): 155 claims sampled and 712 checked over twelve units.
  Source: `records/kit-CHANGELOG.md:253`.

**Records hold none:** the number of checkable claims in a whole unit, other than the one full audit above. Searched: audit reports, fresh-check reports, both changelogs for "claims", "sections".

---

## F47 · Audit 2's detail

**Fact needed:** whether any of the ten stale claims were sampled; the date, units and model; audits after the newer model.

**Found:**

- §4 · Audit 2 (its report, 29 Oct 2026): run on 29 Oct 2026 by Fable 5.1 with live search, in its own agent context that had not seen the writing, over B2, B3, B4 and A1; B2's sample was 0 of 9 failing with 3 stale, so 3 of the 10 stale claims were among the 28 sampled and 7 were found while checking beyond the sample; the decision rule was applied to the sample only.
  Source: `records/audit-2.md:1`–`:17`, `:37`, `:125`.
- §4 · Later audits: see F18 (the public marketing course's audits ran on Fable 5.2) and F105.

---

## F53 · The pipeline's steps (only the parts still missing)

**Fact needed:** who applied fresh-check findings for the earlier units; any gate before publishing; the figure checkers' model; how re-runs were recorded; when the private-terms check began.

**Found:**

- §2 · Who applied findings (the method §5; the fresh-check reports' maintainer notes; the project changelog, 28 Oct to 15 Nov 2026): until 14 Nov 2026 the findings were verified and applied by the chat that orchestrated and filed the row, recorded as "the maintainer"; that chat ran on Opus 5.5 except where the row's record names another model: Fable 5.1 in two UX rows (9 Nov and 3 Nov 2026) and Fable 5.2 in one (10 Nov 2026); from 15 Nov 2026 (this course's BW1) a separate Opus 5.5 agent, the applier, applied them.
  Source: `records/method.md:147`–`:148`; `records/fresh-checks/fresh-check-B8.md:262`; `records/fresh-checks/fresh-check-IA4.md:116`; `records/docs-CHANGELOG.md:39`, `:109`, `:92`; `records/kit-CHANGELOG.md:500`.
- §1 · Gates before publishing (the method, 15 Nov 2026; the kit changelog): before a publish, scripts must pass: the build's verify script, the course-index check and the private-terms check, then the publish is read back by sha256; attaching the public repository for the second publish was several times refused by the session's permission check and done only after the owner approved it.
  Source: `records/method.md:102`, `:204`; `records/kit-CHANGELOG.md:462`, `:543`, `:643`, `:708`.
- §6 · Figure checkers' model (the kit changelog, 30 Oct 2026 on): every figure check and re-check was run by a separate Opus 5.5 agent.
  Source: `records/kit-CHANGELOG.md:72`, `:980`, `:996`, `:1000`.
- §6 · How re-runs were recorded (the course index; the fresh-check reports): each figure's check count is recorded in the unit's course-index row ("passed on its third check") and in the fresh-check report's maintainer note on the re-check; a row run again is recorded as its own changelog row.
  Source: `records/courses-index.md:94`–`:106`; `records/fresh-checks/fresh-check-IA5.md:236`, `:385`; `records/docs-CHANGELOG.md:50`.
- §7 · Private-terms check, start (the kit changelog, 11–12 Nov 2026): the script that fails the build on a private term in a public course was added when the two public courses were created on 11–12 Nov 2026, after the structure audit of 29 Oct 2026.
  Source: `records/kit-CHANGELOG.md:39`; `records/B4-context-engineering.md:6` (written 2026-10-29).

---

## F62 · Skills

**Fact needed:** whether the case packaged any procedure as a skill, which, and where it was installed.

**Found:**

- §7 · Skills (the AI course's B4, layer table, 29 Oct 2026; the project changelog, 3 Nov 2026; the method): the project kept four skills in its repository, for writing a unit, running a fresh check or audit, filing a unit and starting a course; they were installed on the owner's account under Customize > Skills by hand from files built from the repository (last on 3 Nov 2026, checked identical to the repository's copies); the method tells a chat to file with the filing skill and to run fresh checks with the checking skill.
  Source: `records/B4-context-engineering.md:378`; `records/docs-CHANGELOG.md:111`; `records/method.md:148`, `:171`.

---

## F63 · Repository layout in BW4's and BW5's form

**Fact needed:** whether the repository holds INDEX.md, INSTRUCTIONS.md and BUILD-ORDER.md.

**Found:**

- §1 · Layout names (the method, the course index, B4 F2 and F8): no file named INDEX.md, INSTRUCTIONS.md or BUILD-ORDER.md appears in the records; their equivalents are `docs/courses-index.md` (the index), `docs/project-instructions.md` (a copy of the Project's instructions field) and each course's build order as a list in its data file.
  Source: `records/method.md:87`, `:193`; `records/B4-context-engineering.md:434`, `:446`; `records/docs-CHANGELOG.md:50`.

Searched: all records for "INDEX.md", "INSTRUCTIONS.md", "BUILD-ORDER.md".

---

## F64 · Scheduled tasks

**Fact needed:** whether the case ran any scheduled task, or on what.

**Found:**

- §7 · Scheduled tasks (the AI course's B4, 29 Oct 2026; the B4 fix list, 16 Nov 2026): no scheduled task existed on the setup as of 28 Oct 2026, and none appears in the records of 16 Nov 2026; the weekly rot check B4 proposed was not created.
  Source: `records/B4-context-engineering.md:380`, `:462`; `records/p30-b4-fixes.md:142`.
- §7 · Unattended runs instead (the project changelog, 29 Oct to 14 Nov 2026): several rows were run as chats left unattended overnight or with the owner away, among them two figure-renderer rows (29–30 Oct 2026), two units (1–2 Nov 2026) and the public marketing course's units in pairs (12–14 Nov 2026).
  Source: `records/docs-CHANGELOG.md:146`, `:145`, `:122`, `:89`, `:74`, `:62`.

---

## F71 · The agents' runs

**Fact needed:** tools and permission mode per agent; commits or branches before runs; attempt or spend caps; the trifecta or injected instructions; the rule after lost writers and missing transcripts; who starts the publish; the list of unit files.

**Found:**

- §7 · Agents' tools (the kit changelog, 2 to 10 Nov 2026): where transcripts were kept, a script checked each agent's tool use: writers used search and fetch and no connector, memory, Projects or Artifact tool, each fetched address one a search had returned; page checkers used only read, glob and grep inside their folder; figure re-checkers used no web tool; the AI course's usage-review writer alone was given the past-chat tools.
  Source: `records/kit-CHANGELOG.md:470`, `:486`, `:564`, `:736`–`:740`.
- §7 · Commits and branches (the method, 15 Nov 2026; the AI course's DD-B2, §7 and change 9): a checkpoint commit follows every agent; the history courses' figure passes worked on side branches; of 39 row asks held as text in the six reviewed days, one names a branch and none a worktree.
  Source: `records/method.md:102`; `records/DD-B2-deep-dive-his-unknown-unknowns.md:131`, `:186`.
- §7 · Caps (the kit changelog; DD-B2): figure passes ran at most eight agents at a time and dropped a figure that failed twice; the public marketing course's re-run auditors were held to 40 searches each; four figure-pass asks gave an attempt cap.
  Source: `records/kit-CHANGELOG.md:982`, `:996`, `:251`; `records/DD-B2-deep-dive-his-unknown-unknowns.md:76`.
- §7 · After lost writers and missing transcripts (the kit changelog, 3 and 10–12 Nov 2026): when the second writer was lost, a third resumed from its working files and the lost transcripts were checked by script; where a session kept no transcript on disk, the record says so and the model recorded is the one each agent stated.
  Source: `records/kit-CHANGELOG.md:738`, `:40`; `records/docs-CHANGELOG.md:89`.
- §7 · Who publishes (DD-B2 §7, 2 Nov 2026; the method): the session that works the row publishes and deploys; in 13 of 16 row asks read in full the session was told to.
  Source: `records/DD-B2-deep-dive-his-unknown-unknowns.md:133`; `records/method.md:191`.
- The list of unit files: the course index gives every filed unit's path (`records/courses-index.md:58`–`:149`); this course's folder is already in case file §1.

**Records hold none:** the permission mode of any agent; any spend cap; any agent holding private material, untrusted content and a way out at once, or meeting injected instructions; a rule adopted after the lost writers. Searched: both changelogs, the method, DD-B2 for "permission mode", "bypass", "auto mode", "inject", "untrusted", "budget", "spend".

---

## F83 · Plan, memory settings, training setting, usage measures, recurrence, spend cap, private material, employer policy

**Found:**

- Memory: see F4 (account memory flowed into the Project on 28 Oct 2026; the setting not visible on 16 Nov 2026).
- Usage measures: see F4 (token totals for two batches of agents; 18% of a model's weekly allowance in one audit chat).
- §7 · Where private material is kept (the B4 fix list, 16 Nov 2026; the project changelog, 17 Nov 2026): the private-terms list sits in the private repository, not in the public one the site is deployed from; the audit and review files linked from the site's How-it-was-built pages are kept in the private repository and open only to the site's owner; the usage review's working files and the chat history it read are not published.
  Source: `records/p30-b4-fixes.md:134`; `records/docs-CHANGELOG.md:11`; `records/DD-B2-deep-dive-his-unknown-unknowns.md:14`, `:203`.

**Records hold none:** the plan; "Include sensitive topics in memory"; the training setting; how often each routed task recurs; a spend cap; any employer material or policy. Searched: all records for those terms and "plan", "training", "model improvement", "employer".

---

## F92 · Reading before publishing, per-run budget, agents' tools, effort per unit

**Found:**

- §2 · Publishing without the owner present (the project changelog, 12–14 Nov 2026): several writing rows ran with the owner away, and the same chat wrote, checked, filed and published the units.
  Source: `records/docs-CHANGELOG.md:89`, `:88`, `:74`, `:73`, `:62`, `:61`.
- Per-run limits: see F71. Agents' tools: see F71. Effort: see F18 (recorded in none of 53 chats).

**Records hold none:** whether the owner reads each unit before publishing (DD-B2 rule 4: "nothing in the history records his reading", `records/DD-B2-deep-dive-his-unknown-unknowns.md:121`); any spend budget; effort per unit.

---

## F99 · A publish that had to be repeated, redone, forced, doubled, reverted or failed

**Found** (the records' lines, with their dates):

- Kit changelog, session 58, 4 Nov 2026 (`records/kit-CHANGELOG.md:598`): "**Found after the first publish, fixed and published again.** … Neither checker nor verify had caught it. Rebuilt, verified … and published a second time, each artifact read first and found at this session's own version: Academy v128 … the Greece edition v5 …, Pages … run 41904417910, success."
- Kit changelog, session 64, 9 Nov 2026 (`records/kit-CHANGELOG.md:512`): "`deploy.sh` once … pushed as 07b8ae6 …; its Pages run 42672472296 completed as failure with no job run (\"likely a workflow file issue\" …; `gh run rerun` refused by the token's scope), so one empty commit 11011c1 was pushed to retrigger it: run 42673696140's build and deploy jobs both succeeded and only GitHub's report-build-status job is missing, which marks the run failed".
- Kit changelog, 21 publish entries, 2 to 10 Nov 2026 (`records/kit-CHANGELOG.md:462` to `:800`), e.g. session 67, 10 Nov 2026 (`:462`): "The first publish named six files as unread …; each was read with `paths`, found byte-identical to the start build, and the publish was made on them. … never forced."
- Missed or deferred deploys: session 50, 3 Nov 2026 (`:708`): "the public repository's attach was refused by the session's permission check …; `deploy.sh` not run"; session 62, 9 Nov 2026 (`:543`): "`deploy.sh` did not run at first: the session's permission check refused the attach …; [the owner] approved it at 09:19, and the published build … was deployed"; 12–14 Nov 2026 (`:332`, `:320`, `:283`, `:270`): "GitHub Pages not deployed"; 15 Nov 2026 (`records/docs-CHANGELOG.md:53`): "**Deploy to GitHub Pages not done**: … adding it was denied; recorded as P119", deployed the same day (`:49`).
- Reverted (not a publish): 3 Nov 2026, a writing row's baseline-build commit reverted when the owner stopped the row (`records/docs-CHANGELOG.md:114`); 2 Nov 2026, "one chat reverted its own merge because another session was alive and mid-unit on the same repository" (`records/DD-B2-deep-dive-his-unknown-unknowns.md:131`).
- No record of a forced publish, a doubled publish or a publish to a new artifact; DD-B2's change 7 names them as what a skill should prevent (`records/DD-B2-deep-dive-his-unknown-unknowns.md:178`).

Proposed lines:
- §7 · A publish repeated (the kit changelog, 4 Nov 2026): a layout fault found after a site change was published was fixed, rebuilt, verified and published a second time the same day; neither the change's checker nor the verify script had caught it.
- §7 · A failed deploy (the kit changelog, 9 Nov 2026): one GitHub Pages run failed with no job run; an empty commit retriggered it, and its build and deploy jobs succeeded.
- §7 · Publishes refused at first (the kit changelog, 2 to 10 Nov 2026): in 21 publish entries the publishing tool first refused, naming files the session had not read; each was read, found equal to the build, and the publish made, never forced.
- §7 · Deploys missed (the kit changelog and project changelog, 3 to 15 Nov 2026): in several sessions the second publish, to GitHub Pages, did not run because attaching the public repository was refused or denied; it ran after the owner's approval or in a later row.

---

## F102 · Findings rejected or adjusted, who applied them, findings by kind

**Found:** the per-unit record and who applied, in F45 and F53.

**Records hold none:** a count of findings by kind (figure not on the page, qualifier, author, law, quotation, count, product fact). Each report tags its findings with a category (accuracy, attribution, figure, coverage, style, deliverable), but no record tallies them. Searched: the 37 fresh-check reports, both changelogs.

---

## F103 · The writing model per draft and the order of writing

**Found:**

- §5 · Writing model: Opus 5.5 for all 36 (F18).
- §5 · Order (the course index): the §5 table's rows are the course index's build order, the marketing and AI courses' units numbered 1 to 22 with B1 left out, then the UX course's 1 to 15; the index dates each unit's writing (28 Oct to 3 Nov and 30 Oct to 10 Nov 2026), records A1 as written out of order beside B3, and gives no order within a day.
  Source: `records/courses-index.md:3`, `:58`–`:84`, `:90`–`:106`.

---

## F104 · Whether the history units had a fresh check, and by which model

**Found:**

- §5 · History courses (the method §1 and §5; the kit changelog, 25–27 Oct 2026): the history courses' pipeline from 25 Oct 2026 was a script check, then a fresh checker per report that had not seen it written, then a maintainer pass; when the second history course's reports were reviewed on 27 Oct 2026, its 58 then unaudited reports had been checked in three ways: a quality pass keeping them (13), a quality pass fixing them (26) and the fresh-checker pipeline (17), the capstone apart; the history review measured a mean score of 4.28 for units written without a checker and 4.8 for one unit written with one.
  Source: `records/method.md:22`, `:46`–`:48`, `:147`; `records/kit-CHANGELOG.md:1221`–`:1222`.
- §5 · Second history course (the kit changelog): complete at 79 reports, all written with Opus 5.5 and all checked by a fresh agent.
  Source: `records/kit-CHANGELOG.md:75`.

**Records hold none:** the model of each history fresh checker; which of the first history course's 78 reports had a fresh check.

---

## F105 · Audit 2's detail and why Audits 3 onward had not run

**Found:**

- Audit 2: see F47.
- §9 · Audits 3 onward (the kit changelog, 3 Nov 2026; the method, 15 Nov 2026; DD-B2 §4): after Audit 2 the next audits of the marketing, AI and UX courses were deferred to a later stage reserved for the auditing model, the auditing model having run short on 29 Oct 2026; on 15 Nov 2026 the owner closed that stage, retired the four-unit audit and left the fresh check and the staleness check as the guards.
  Source: `records/kit-CHANGELOG.md:62`, `:748`; `records/DD-B2-deep-dive-his-unknown-unknowns.md:82`; `records/method.md:23`, `:53`.

---

## F106 · The draft with a rewrite verdict at its fresh check

**Found:**

- §5 · The rewrite verdict (B8's fresh-check report and the course index, 2 Nov 2026): the AI course's B8 drew rewrite by the count rule (4 errors, two of one cause, each a one-sentence replacement); the maintainer read it as fix under the method's definition, all findings were applied, and the owner could overrule; it was not rewritten or re-checked; its decision figure was dropped after its third check.
  Source: `records/fresh-checks/fresh-check-B8.md:8`, `:258`, `:275`; `records/courses-index.md:80`.

---

## F107 · Figures: counts, first-check failures, checks to pass, checker model

**Found:**

- §6 · Figures added after writing (the kit changelog, 30 Oct 2026): the marketing and AI courses' twelve filed units, 38 kept and 4 dropped; the second history course, 177 kept and 18 dropped (8 after failing twice), later 180; the first history course, 266 proposed, 166 passed the first check, 95 got a fix, 94 of those passed the re-check, 6 dropped, 260 kept; each checked by a separate Opus 5.5 agent.
  Source: `records/kit-CHANGELOG.md:1000`, `:996`, `:984`, `:982`, `:72`.
- §6 · Figures on the site (the kit changelog): the verify script checked 509 figures on 152 pages on 30 Oct 2026 and 624 at phone width on 3 Nov 2026.
  Source: `records/kit-CHANGELOG.md:988`; `records/docs-CHANGELOG.md:112`.
- §6 · Checks to pass, per unit (the course index): each unit's row gives its figures' check counts, e.g. a sitemap figure passed on its eighth check and two matrices on their seventh.
  Source: `records/courses-index.md:94`–`:106`.
- Note: these retrofit passes dropped a figure that failed twice, where case file §6 says "fails three times"; two units' figures were dropped after a third check (`records/courses-index.md:76`, `:80`).

**Records hold none:** the total of figures declared in all units at one date; a typical number of checks to pass.

---

## F108 · The usage review's ten ranked changes

**Found** (the AI course's DD-B2, Deliverable, over the Project's 53 chats of 28 Oct to 2 Nov 2026; `records/DD-B2-deep-dive-his-unknown-unknowns.md:141`–`:197`). Proposed lines:

- §8 · Change 1, the auditing model only for checking: 17 of the 22 chats run on that model in whole or part were not audits or fresh checks; 18 of the 22 began on the first day; all 9 fresh checks run on the last day ran on the writing model with the auditing model's check owed.
- §8 · Change 2, a routing row for the build and site work: 30 of 53 chats were of task types the routing table had no row for (infrastructure 15, figure passes 7, status 6, syllabus 2); the 15 infrastructure chats ran on the auditing model 8, the writing model 5, both 2; none of 53 ran on a smaller model.
- §8 · Change 3, move a fan-out's workers down once its check has passed: 7 figure chats, median 33 turns, 6 on the writing model; in one pass alone 218 agents; every agent call in the two saved reads that show one (199 and 37) ran on the writing model; 6 of 266 figures dropped.
- §8 · Change 4, no session deploys to the public site without the private-terms check: 13 of the 16 row asks read in full had the session publish and deploy to the public site, where the structure audit had found private terms in the build.
- §8 · Change 5, one writer to the main branch at a time: 10 of 53 chats began while an earlier one was still open (14 overlapping pairs, an upper bound); one chat reverted its own merge because another session was mid-unit; one found another chat had done its work; of 39 asks held as text, one names a branch and none a worktree.
- §8 · Change 6, model and effort in the first line and in the changelog: the model could be read in all 53 chats only by searching each for its commit trailers; effort in 0 of 53.
- §8 · Change 7, the closing procedure in one skill: 13 of the 16 row asks read in full restated the publish procedure; 7 carried the same two-word publish instruction; 13 chats ended by writing the next prompt by hand.
- §8 · Change 8, carry an audit's confirmed claims forward: one rewrite after an audit opened 43 distinct sources, 34 already opened by the audit that morning; another 45, 15 of them the audit's.
- §8 · Change 9, no overnight plan without a branch: two figure-pass asks were written for an overnight run over filed units; of 39 asks held as text, one names a branch; both runs went ahead in the morning instead.
- §8 · Change 10, account memory off in the Project: the model called the memory tool in 6 of 53 chats, in the parts read.
- §8 · Ranking (DD-B2 §8): the ten are ranked by the size of the count each rests on and the share of the work it touches, the writer's judgement on those counts; one item was flagged and not ranked (9 of 53 chats open three hours or more, open time not being active time), and three habits were already fixed in the window and not ranked.

---

## F109 · Hours, usage or cost per unit or row, plan, effort

**Found:** token totals for two batches of agents and one allowance share (F4); effort in none of 53 chats (F18); how long chats stayed open (DD-B2 §2: median 0.9 hours from first message to last update, nine open three hours or more, longest 20.2 hours; open time is not active time; `records/DD-B2-deep-dive-his-unknown-unknowns.md:62`).

**Records hold none:** hours, usage or cost per unit or per row; the plan; effort settings.

---

## F110 · Total words and the build's start date

**Found:**

- §1 · Start (the kit changelog): the first request of the work that became Academy was made on 22 Oct 2026; the first history course was built from 22 to 24 Oct 2026; the claude.ai Project's chat history starts on 28 Oct 2026, the repository being created that day.
  Source: `records/kit-CHANGELOG.md:3`, `:96`, `:1413`; `records/DD-B2-deep-dive-his-unknown-unknowns.md:18`; `records/docs-CHANGELOG.md:188`.
- §1 · Words (the kit changelog): the first history course about 244,000 words, the second about 264,000.
  Source: `records/kit-CHANGELOG.md:74`–`:75`. (The first course's ebook edition of 1 Nov 2026 counts 370,074 words with its 78 chapters, `:826`; the records do not say what each count includes.)

**Records hold none:** a total of words for all courses. Searched: both changelogs, the course index for "words".

---

## F113 · The review's ten ranked changes for DD-BW3

**Found:** as F108; the ten changes and their counts are held in the AI course's DD-B2 Deliverable and can be added to case file §8 in the lines given under F108.

---

## F116 · The usage review's breakdowns and method

**Found** (the AI course's DD-B2, §1–§8, read 2 and 3 Nov 2026):

- §8 · How the chats were listed (§1): through the three past-chat tools only (one lists chats by last update, one searches, one opens a chat at a spot); three listing calls (20, 20 and 13 chats) covered the window, two more found nothing outside it; 16 chats opened, spots in 7 more found by search; counts by two scripts over a table typed from the tool results.
- §8 · Fields (§1): date and first message, task type (seven types, labelled by hand), turns, model (from commit trailers), effort (0 of 53: nothing records it), outcome (39 of 53; 14 not read). A turn is one message on either side; in a chat that runs agents, each agent's completion notice is a turn. "Accepted" was a proxy: a unit filed (7 chats) or the last reply reporting the row done with no later correction (32 chats).
- §8 · Breakdowns (§2): task types as in F18; 872 turns in all, median 8, range 2 to 134; median turns by type: unit writing 12, infrastructure 8, figure passes 33, audits 2.5, status 10, syllabus 10, history writing 50.5; 11 chats took two turns; 10 took 30 or more.
- §8 · Pattern counts (§3–§6): 6 one-line asks naming a code, 2 of them a code with two meanings; 5 chats opened with a status question; 16 asks name two or more rows (median 11.5 turns, against 8 for 31 naming one); 13 of 16 row asks read in full restate the publish procedure; 7 chats on the first day carried a whole unit pasted; 6 chats show a memory-tool call.
- §8 · Rules tested (§7): the AI course's operating rules 1–10, its usage rules 11–24, its agent rules 25–28 and decision rule, and its routing table, mental model, skills and verification units, each given a verdict.
- §8 · Date: the review read the history on 2 and 3 Nov 2026 across three agent runs; the unit is dated 2 Nov 2026 and was filed on 3 Nov 2026.
  Source: `records/DD-B2-deep-dive-his-unknown-unknowns.md:6`, `:14`–`:32`, `:36`–`:60`, `:68`–`:102`, `:112`–`:135`, `:201`; `records/courses-index.md:84`.

**Records hold none:** a definition of an "ask".

---

## F117 · Whether the six days were typical

**Found:**

- §8 · Typicality (DD-B2 §1 and §8): the review's writer states that the six days were a week of heavy building spent on the course machine, that every rate is a six-day rate not to be read as a habit over a season, and that the mix of tasks will not be a normal week's; work before the first day, including the history courses, is outside the tools' reach.
  Source: `records/DD-B2-deep-dive-his-unknown-unknowns.md:18`, `:139`.

---

## F118 · The review's working files

**Found:**

- §8 · Working files (DD-B2 §1 and Sources; the kit changelog, 3 Nov 2026): the review's working table, chat list, tallies and scripts were kept in the writer's packet folder in the session and are not published; when two writers were lost to container restarts, the third resumed from the second's working files in the same packet; the chat history read is private.
  Source: `records/DD-B2-deep-dive-his-unknown-unknowns.md:14`, `:203`–`:204`; `records/kit-CHANGELOG.md:738`.

**Records hold none:** whether the working files were deleted afterwards.

---

## Proposed §9 lines

For every fact the records do not hold, phrased as the case file's §9 does:

- §9 · The records do not say which plan the project runs on, or any token or window measure for the writing of a single unit, or whether any failure was traced to retrieval mode (F4, F83, F109).
- §9 · The records do not say what effort setting was used for any unit, check or audit: the usage review found it recorded in none of 53 chats (F18, F92, F109).
- §9 · The records do not hold hours, usage or cost per unit or per row, or how often each routed task recurs (F18, F83, F109).
- §9 · The records do not hold the text of a private course's unit brief, of the fresh-check prompt or of the retired sample-audit prompt; this course's own preamble and briefs and the staleness prompt are held (F19).
- §9 · The records do not say whether the owner wanted the length of the longest UX unit in particular; the rule is that length is a guide (F21).
- §9 · The records do not count the chats abandoned or the briefs rewritten after a miss; they record instances (F20, F29).
- §9 · The records hold no spec document and no recorded non-goals for any course (F35).
- §9 · The records do not total the fresh-check findings rejected or adjusted, give a false-alarm rate, or count findings by kind (F45, F102).
- §9 · The records do not give the number of checkable claims in a whole unit, except the one full audit of Audit 1 (F46).
- §9 · The records do not say which permission mode any agent ran in, or record a spend cap, an agent meeting injected instructions, or a rule adopted after the lost writers (F71).
- §9 · The records do not say whether "Include sensitive topics in memory" or the training setting was on, or whether account memory was off after 28 Oct 2026; they hold no employer material or policy (F83).
- §9 · The records do not say whether the owner reads each unit before it is published (F92).
- §9 · The records do not give the model of each history fresh checker, or which of the first history course's reports had one (F104).
- §9 · The records do not give the total of figures declared at one date or a typical number of checks to pass (F107).
- §9 · The records do not give a total of words written across all courses (F110).
- §9 · The records do not define an "ask" in the usage review (F116, F114).
- §9 · The records do not say whether the usage review's working files were deleted (F118).
