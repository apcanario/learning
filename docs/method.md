# Method

The one method for every course in the Learning Project. It merges the Personal Mythology method (the kit's `AGENT-SPEC.md`, `WRITER-BRIEF.md`, `BACKLOG.md`, `NEXT-SESSION.md`, the audit briefs and rubric) with the Brand + AI method (the hub's Build pages and Hub template). Section 1 says where they differed and what the common rule is. The rest is the method in full.

**Existing units stay valid as they are.** The 137 Personal Mythology reports already written (Greece 78, Rome 59) were written, checked and reviewed under the kit's rules and are not re-done, re-filed or re-audited under this one. Nothing here changes a course's content, a syllabus prompt or a brief.

**Home (28 October 2026).** Everything lives in the private repo `apcanario/learning`: `kit/`, `design/`, `docs/` (this file and its neighbours), `generator/`, `courses/` (the vault). The claude.ai Project "Learning" holds mirrors of `docs/`. A chat clones the repo and ends with a commit; the kit no longer travels as a zip (`pm-status-2026-10-28.md`, D4).

## Terms

- **Unit:** what one chat writes. A Brand + AI unit (A1, B4, DD-A2); a Personal Mythology module (Rome 11.3), which the kit calls a report. The history syllabi group modules into numbered "units"; this file calls those **syllabus units**.
- **Course:** a syllabus with its units. **Hub:** the published page for a family of courses (Brand + AI holds courses A and B; Personal Mythology holds Greece and Rome).
- **Vault:** `courses/` in the repo, where finished units are filed.

## 1 · Where the two methods differed, and the common rule

| Topic | Personal Mythology | Brand + AI | Common rule |
|---|---|---|---|
| What a unit ends with | Self-test (10 questions) and Carry forward (3 ideas) | A shipped deliverable, built in full | Every unit ends with its course's closing artefact, built in full in the same chat (§4) |
| Sourcing | Citation precision for ancient and modern scholarship; per-report bibliography file | Source classes for modern evidence (peer-reviewed, platform-official, large-sample vendor, documented case), labels for anecdote and correlation | One checklist in two layers: a common part and each course's own part (`sourcing-standard.md`) |
| Format and filing | HTML fragment per `AGENT-SPEC.md`, kept in the kit, registered and built into the site (Markdown in the vault since P71-3, 1 Nov 2026) | Markdown in the vault at `courses/brand-ai/<code>-<slug>.md` | Every new unit is filed at `courses/<course>/<code>-<slug>.md`; history files also go into the kit (§7) |
| Per-unit check | `check.py`, then a fresh checker per report, then a maintainer pass (25 Oct 2026 pipeline) | None; the four-unit audit only | History keeps the fresh check; Brand + AI adds it only if its first audit fails (§5) |
| Audit cadence | Every four complete syllabus units (`review_due.py`), sampling one report in four, scored on the rubric | Every four written units, one claim per section per unit, more than one in ten FAIL → full audit | Every four units written in a hub, the stratified-sample claim audit; a unit that fails gets its course's full audit (§6). Decided 28 October 2026: this also governs Personal Mythology's remaining modules; `review_due.py` counts modules on this cadence since S3 (1 Nov 2026) |
| Live search | Write from knowledge; search only to verify a specific doubtful point | Flag per unit; on = search first, date facts, staleness check at six months | Every unit carries a search flag; history modules are all off (§4) |
| Length | The prompt's target is a guide, never a law (27 Oct 2026) | 2,000–6,000 words, whatever the topic needs | The topic decides; no padding, no cutting to a number (§4) |
| Writing order | Dependency order: a module starts when every report its lane note names is registered | Explicit build order with interleaving; deep dives last; audit gate | Both (§3) |
| Models | Fable 5.1 or Opus 5.5 wrote; anything not Fable flagged for Fable review | Opus 5.5 writes, Fable 5.1 audits; DD-B2, briefed for Fable, written by Opus 5.5 (the exception set aside 31 Oct 2026) | Writing Opus 5.5, audit Fable 5.1; the model that actually wrote a unit is recorded (§4) |
| Style | British spelling, no em dashes, fragment elements only | Direct, no flattery, no filler, no motivational language, no "not X but Y" | Common tone: direct, no flattery, no filler, no preamble, no closing filler. Each course keeps its own house style |

Five of these are real decisions. Each is a single pick.

**Deliverable.** Pick: the syllabus defines each course's closing artefact; history's is the Self-test and Carry forward.
- History reports already end with an artefact the reader uses.
- Calling it the deliverable keeps all 137 reports valid unchanged.
- One rule ("built in full, same chat") covers both courses.

Override if: you want a history module to ship more (a timeline, a map); then add it to that module's prompt, never retrofit written ones.

**Filing.** Pick: one vault path for every new unit; history units also copied into the kit.
- One place to find every unit, whatever the course.
- The kit's build, checks and site need its own layout.
- A `.md` file can hold the HTML fragment unchanged.

Override if: you want the kit as the only home for history; then the vault holds a one-line pointer file per module.

**Per-unit check.** Pick: history keeps a fresh checker per module; Brand + AI does not, yet.
- The Greek review measured it: units written without a checker scored 4.28.
- With a checker, unit 12 scored 4.8 (`audits/greece-13.4-cohorts.md`).
- Brand + AI's sample audit will show whether it needs one.

Override if: any unit in Brand + AI's first audit fails more than one sampled claim in ten; then every later Brand + AI unit gets a fresh check too. **Triggered 28 October 2026:** Audit 1 failed A2·A6·A9 (23 of 91 claims); from B2 on, every Brand + AI unit gets a fresh checker in a new chat (§5).

**Audit cadence.** Pick: count units per hub; audit every four with the claim-sample prompt.
- One trigger the reader can count without a script.
- Hubs differ in rubric, so their units are not pooled.
- A failed unit still gets the history scorecard, the stronger instrument.

Override if: Fable time is short; then history returns to the kit cadence (four syllabus units, one report in four, scorecard). Not taken on 28 October 2026: strict four-module batches stand (`pm-status-2026-10-28.md`, D3).

**Search flag.** Pick: every unit carries one; every history module is off.
- Classical scholarship does not change in six months.
- "Off" still allows a search to verify one doubtful point.
- Only "on" units owe a staleness check.

Override if: a history module rests on recent archaeology or a new edition; flag it on and date those facts.

## 2 · Unit anatomy

Common to every unit:

1. **Header** (filing metadata, added when filed): code, title, course, model that wrote it, date written, search flag.
2. **Body:** headed sections that answer the brief item by item, in the brief's order. No preamble ("In this unit I will…"), no summary of what is about to be said, no closing pleasantries. Begin with the first section.
3. **Sources in place:** every checkable claim cited where it is made (`sourcing-standard.md`).
4. **Disagreement shown:** where sources or scholars differ, say so and name each side.
5. **Closing artefact:** the course's deliverable, built in full (§4).
6. **Sources:** the unit leaves its source list (Brand + AI: a Sources list of links at the end of the file; history: `bibliography/<course>/r-<id>.md`).

**Every new course is a markdown course (P71, decided by Pedro 31 Oct 2026).** A unit holds only its text, its sources and its figure declarations (` ```viz ` blocks, data only): one Markdown file in the course's vault, front matter first (§7). Everything visual is the build's: the layout, the section bands and steps, the accordions, the drawing of every figure (`kit/viz.py`), the styling (`design/theme.css`). The same files make the site and the ebook (`python3 build.py --epub <edition>`). Greece and Rome were converted to Markdown in the vault on 1 November 2026 (P71-3, `docs/p71-3.md`); no course is in the fragment format now.

Per course:

| | Personal Mythology module | Brand + AI unit |
|---|---|---|
| File | Markdown in the vault since P71-3 (1 Nov 2026): front matter and title, `##` sections (6–10), `###`, paragraphs, lists, `>` quotations under 15 words, pipe tables, ```` ```tree ```` blocks, dispute boxes opening `**Where sources disagree.**`, ```` ```viz ```` figures; no HTML but `<sup>` and `<sub>`, no emoji (`AGENT-SPEC.md`; before P71-3 an HTML fragment in the kit) | Markdown long-form report, "the same long-form report format as his history course" (preamble) |
| Disagreements | `aside.dispute` beginning "Where sources disagree.", several per report, a named source or scholar on each side; required | Where sources conflict, said in the text with each side named (common rule); anecdote, vendor and correlational data labelled as such (preamble) |
| Ends with | `h2` "Self-test" with `ol.quiz` of 10 questions, each answer in `details`; then `h2` "Carry forward" with `ol.carry` of exactly 3 ideas | The deliverable named in the unit's "Ships" line, written in full |
| Pointers | "module 6.5", "Greek module 7.3", "Rome module 13.2", "deep dive module 11.7"; open the target first | Unit codes (A3, B5) |
| Style | British spelling; no em dashes (colons, semicolons, commas; en dashes in ranges); course conventions for names and citations | Tone rules of the preamble |

## 3 · Writing order

- Every hub keeps an explicit build order: one row per unit with model and search flag, an audit row after every fourth unit. Brand + AI's is the hub's Build order page; Personal Mythology's remaining modules are ordered in `BACKLOG.md` in batches of four. Both are copied into `courses-index.md`.
- A unit starts only when every unit it points back to is filed (history: every report named in its lane note is registered).
- Neighbours share no material: each anecdote, dispute and self-test question has one home; the others point to it by number.
- Where two units build the same asset, write them side by side (Brand + AI: B5 beside A3, B7 beside A5).
- Core before deep dives; deep dives last. Brand + AI: DD-A2 and DD-B2 last, DD-B2 last of all (it reviews the chat history). Personal Mythology: within a deep dive, the synthesis module last (Rome 11.8), and a module whose prompt names another deep dive after that one (Rome 12.6 after 13.2).
- **Audit gate:** no new unit starts while an audit verdict of REWRITE is open on an earlier unit, and none starts when an audit is due (§6) until it has run. A writing session that reaches an audit point stops at the unit boundary and says so in its first line.

## 4 · Writing a unit

### One chat per unit
Open a new chat in the Learning Project for each unit. Paste the unit's brief (§4, Brief template). Never reuse a chat across units; leaked context is how a course starts repeating itself. An isolated agent context counts as a new chat (P31, 29 Oct 2026): a chat may orchestrate several units when each is written by a fresh agent on the named model, given only its brief and paths to filed units, each fresh check is a separate agent that has not seen the writing, and the orchestrating chat only files (vault, course data, build, publish). The changelog row names the arrangement. The deliverable is written in the same chat as its unit, never separately, so it inherits the unit's reasoning.

### Models
Writing: **Opus 5.5**. Audit: **Fable 5.1**. Exceptions are named in the build order (Brand + AI DD-B2 was briefed for Fable 5.1 because it reviews the chat history; Pedro set the exception aside on 31 Oct 2026 and it was written by Opus 5.5 on 2 to 3 Nov 2026, with the past-chat tools). Sonnet and Haiku are for derivative work only (posts, Shorts lists, emails from a finished unit), never units or audits. The model that actually wrote a unit is recorded in its header and in `courses-index.md`. Personal Mythology's provenance rule still holds inside the kit: `register.py` records the model, and anything not written or reviewed with Fable 5.1 is flagged for Fable review.

### Deliverable rule
A unit is written in full with its deliverable, never outlined or summarised. The deliverable is the course's closing artefact: for Brand + AI, the thing in the unit's "Ships" line (a document, a table, a skill, a model), built in full inside the unit and usable without reading the unit; for Personal Mythology, the Self-test and Carry forward. It follows from the unit's own evidence and adds no unsourced claim.

### Length rule
The topic decides. A prompt's word count ("about 3,000 words") or range ("2,000–6,000") is a guide: some topics need 2,000 words, some 6,000. Plan the section budget, write in one pass, never pad to reach a number and never cut substance to meet one. Padding is a fault; length is not. (`check.py` reports the count as a note only.)

### Live-search flag
Every unit is flagged **on** or **off** in the build order and in `courses-index.md`.
- **Off:** write from knowledge. Search only to verify a specific date, figure or contested point you are unsure of. Every Personal Mythology module is off.
- **On:** the facts are current (prices, platform rules and thresholds, plan limits, model lineups, benchmarks, regulatory status). Search before writing; date each such fact in the text. Six months after it is written, the unit gets the staleness check (§6). Brand + AI units on: A2, A6, A9 (written), A8, B2, B8, DD-A1.

### Figure pass
After the draft, the writer goes through the unit section by section and asks of each whether its content has a shape (P41, 29 Oct 2026). Where it does, it declares the matching figure kind (`kit/viz.py`; the table of shape to kind is `skills/write-unit/SKILL.md` §4b: dated events → timeline, a sequence → flow, a hierarchy → tree or sitemap, numbers compared → compare or bars, a trend over time → line, two measures → scatter, competing estimates → range, a rule with branches → decision, roles or items by sections → matrix, a lifecycle → states, a journey across actors → swimlanes, screens → wireflow, things and their relationships → objects). The figure is drawn from the unit's own sourced text and placed directly after the paragraph or table it draws. One to four figures a unit is a guide, none where nothing has a shape; a brief that names its own number stands (the User Experience briefs: three to eight). The caption says what the figure shows and where its data comes from (section, author, line). The writer renders every figure before handing in. Syntax and rules: §7, Figures.

### Before handing in
In the same chat, the writer runs `sourcing-standard.md` Part 1 and the course's part over the unit, fixes what fails, and lists up to ten claims it is unsure of or could not verify. That list is where the checker and the auditor start (history: `reviews/<session>/<course>-<id>-writer.md`).

### Brief template
A brief is the shared preamble of its course followed by the unit's own brief. The preamble is written once per course and baked into every brief so each chat is self-contained.

```
SHARED PREAMBLE (one per course; never edited per unit)
Write one unit of a self-study course in <format>. Length is whatever the topic
needs (<guide>); do not pad and do not cut to a target.
Reader: <from reader.md; nothing added>.
<Thesis or frame line, if the course has one.>
Tone: direct, no flattery, no filler<, course additions>.
Course goal: {GOAL}            <- the course's goal sentence, substituted per course
Sourcing standard: <the course's part of sourcing-standard.md, as sentences>.
Where the unit depends on current facts (<which>), search before writing and date the facts.
End with the unit's deliverable, built out in full, not described.

UNIT BRIEF (one per unit)
Unit <code>, <Title>. [Search before writing.] Cover: <every item the unit must
treat, in order>. Deliverable: <the artefact, named precisely>.
```

How each course instantiates it:
- **Brand + AI** (and every markdown course, from its `kit/courses.py` entry's `data` folder): the preamble is `PRE` in `generator/data/brand-ai/units_data.py`, with `{GOAL}` replaced by course A's or B's goal; the unit brief is the fifth field of the unit's entry. The hub's Briefs pages show the joined text, ready to copy. Written units show their note instead.
- **Personal Mythology:** the preamble is `AGENT-SPEC.md` plus `WRITER-BRIEF.md` (attached to the chat); the unit brief is the module's `<pre>` prompt in the course syllabus (the prompt is the contract) plus its lane note from `BACKLOG.md` and the extra files the lane note names.

## 5 · Checking a unit before filing

- **Personal Mythology:** `python3 check.py <course>/r-<id>.html` until it prints OK (structure, 10 self-test answers, 3 carry-forward items, dispute boxes, British spelling, no em dashes). Then one fresh checker in a new chat that has not seen the unit written, briefed with `reviews/units-9-13/BRIEF.md`, the report, its prompt, its neighbours, the targets of its pointers, its lane note and the writer's unsure list; it writes findings and never edits. The maintainer verifies every finding before applying it, with exact-match replacements.
- **Brand + AI:** the writer's own pass (§4, Before handing in), then, since 28 October 2026 (§1 override triggered by Audit 1), one fresh checker in a new chat that has not seen the unit written: it checks every cited claim against its source and the deliverable against the brief, writes findings (error / should-fix / minor) and never edits; the maintainer applies each finding as an exact replacement. The `audit-units` skill runs it. A figure that fails is fixed and re-checked by a new agent from the unit's text without its figures, the captions and the frames sheets `verify.py --shots` saves (every frame a reader scrolls a figure across, phone and desktop, dark and light; P89, 2 Nov 2026). The checker's final report is saved verbatim, before any finding is applied, as `audits/<id>/fresh-check-<code>.md`, `<id>` the course entry's (`brand-ai`, `ux`; front matter: `audits/README.md`).

## 6 · Audit procedure

### When
- **Stratified-sample audit:** after every four units written in a hub, counted from the last audit. Brand + AI counts across courses A and B (A2, A6, A9 and B1 make the first four). Personal Mythology counts its new modules in the batches of `BACKLOG.md`; the kit's `review_due.py` is the alert (rewritten under S3 of `pm-status-2026-10-28.md` to count modules). Run with Fable 5.1, on command, in a new chat in the Learning Project. The next unit waits for it.
- **Staleness check:** six months after any unit written with search on (due dates in `courses-index.md`).
- **Course audits in a syllabus** (Greek unit 13, Rome unit 14) are course content and run as their prompts say.

### How: the stratified-sample audit
Attach or paste the four units (or give their vault paths) and the course's `sourcing-standard.md` part, then this prompt, verbatim:

```
You are auditing four units of a self-study course written by Opus 5.5 for one reader. Units: {list the four unit codes and their vault paths}.

Method, in this order:
1. For each unit, list its sections. From every section draw one claim that carries a number, a named source, a mechanism or a recommendation. That is the sample; record it before checking anything.
2. Check each sampled claim against the source the unit cites: open the source; confirm the figure, the date, the sample size and that the claim is what the source says, not a stretch of it. Mark each claim PASS, FAIL (wrong, unsupported, miscited, or invented) or STALE (true when written, superseded now, with the newer figure).
3. For each unit compute the failure rate. If more than one claim in ten is FAIL, audit that unit in full: every cited claim, same procedure.
4. Check the deliverable: it exists in full inside the unit, it follows from the unit's evidence, and it is usable without reading the unit.
5. Check against the course goal and sourcing standard (in the unit's preamble): does the unit move the reader toward the stated outcomes, and is anything in it advice without evidence?

Output: a table per unit (section, claim, source, verdict, note); the failure rate; a verdict per unit (PASS / FULL AUDIT RUN, result / REWRITE with the sections named); the three most consequential errors across the four units in plain language; and one line each for the bibliography (new sources to add, sources to mark failed) and the changelog. Do not fix the units; report.
```

Decision rule: a unit with more than one sampled claim in ten FAIL is audited in full in the same chat. For a Personal Mythology module the full audit is the kit's scorecard audit (`audits/AUDIT-BRIEF.md` for Rome, `audits/AUDIT-BRIEF-GREECE.md` for Greece, rubric in `audits/greece-13.1-rubric.md` and `audits/rome-14.1-rubric.md`): pass is no dimension below 4 and no factual error; revise is a list of edits fixes it; rewrite is two or more dimensions below 3 or more than two factual errors. When a sample splits by provenance (written with and without a checker), split the stratum (the lesson of Greek 13.4).

Verdicts per unit: PASS · FULL AUDIT RUN, with the result · REWRITE with the sections named. The auditor never edits a unit; it reports.

### How: the staleness check
Six months after a search-on unit was written, in a new chat with Fable 5.1 and live search, this prompt, verbatim:

```
You are re-checking one unit written with live search six months ago: {unit code, vault path, date written}. Search again, today, for every fact in it that can change: platform rules and thresholds, prices and plan limits, model lineups, benchmark figures, regulatory status, the numbers attached to named creators. For each: the value in the unit, the value now, the source and date for the new value, and whether the unit's conclusion still holds. End with a verdict: CURRENT / PATCH (list the lines to change) / REWRITE (say which sections). Do not rewrite; report.
```

### After an audit
- Errata are applied as exact replacements (the current text must occur once), each checked before it is applied; revise items by hand.
- REWRITE: the unit is rewritten in a new chat from its brief before any new unit starts.
- The hub's Audits page gets a log row: date, units sampled, claims checked, failures, verdict, what changed. The bibliography marks any source that failed; the changelog gets one line. `courses-index.md` records the audit and resets the count.
- Personal Mythology: a module reviewed and fixed becomes `"Opus 5.5, reviewed with Fable 5.1"` in `provenance.json` (or `"… (sampled)"` when its stratum was cleared on the sample).

## 7 · Filing a finished unit and updating its hub

Run the `file-unit` skill, or by hand. Since A5 (`academy.md`) the vault is the source of a markdown course: Academy reads its units from `courses/<course>/`, and a unit is written when its file is there with front matter. Since P71-3 (1 Nov 2026) the same holds for Greece and Rome: a history report is its vault file, Markdown read by `kit/mdcourse.py` (`history_html`, through `kit/vault.py`), and the kit holds no copy (`docs/p71-3.md`).

1. **Name.** `<code>-<slug>.md`: the unit code, then the title in lower case with words joined by hyphens, accents and punctuation dropped (`B1-mental-model.md`, `11.3-politics-in-the-street.md`).
2. **Save to the vault** at `courses/<course>/<code>-<slug>.md`, where `courses/<course>` is a markdown course's `vault` in `kit/courses.py` (`courses/brand-ai`, `courses/ux`) and `greece` or `rome` for Personal Mythology. Put the header first as front matter:
   ```
   ---
   code: B1
   title: Mental model
   course: brand-ai · B · Using AI to Build a Brand
   model: Opus 5.5
   written: 2026-10-28
   search: off
   ---
   ```
   Brand + AI: the unit in Markdown, ending with its deliverable and a Sources list of links; this file is what Academy renders, so there is no second copy. Personal Mythology: the report in Markdown below the front matter and a `# <title>` line, in the forms of `kit/AGENT-SPEC.md` (since P71-3; `model` is the writer only, the review status stays in `kit/provenance.json`); its Sources are the bibliography file in the kit (step 3), not a list in the report.
   **A new course files Markdown only (P71, §2).** Its unit is this one file: front matter, text, Sources, ` ```viz ` blocks; no HTML, no class, no style and nothing about layout in it, since the build adds all of that for the site and for the EPUB (`build.py --epub <edition>`, `kit/epub.py`).
   **Figures (A8, 28 Oct 2026).** A unit may declare a figure where structure is the content (a timeline, a comparison of numbers, a line of descent, a sequence of steps); `kit/viz.py` draws it as inline SVG at build time and `design/theme.css` §4i styles it. Every course (Personal Mythology too since P71-3): a fenced ` ```viz ` block holding the JSON, `kind` first and `caption` last (until P71-3 a history fragment declared it as `<figure class="viz" data-viz="timeline"><script type="application/json">{…}</script><figcaption>…</figcaption></figure>`). The kinds and fields are in `viz.py`'s docstring: timeline, compare, tree and flow, and, since V1 (29 Oct 2026) for the Information Architecture course, sitemap, objects, decision, matrix, states, swimlanes and wireflow; and since P44 (29 Oct 2026) the data kinds line, bars, scatter, range and a numeric matrix. Academy's Figure kinds page (`#viz-examples`) draws one of each with the block that draws it. A figure's numbers and names are claims: they come from the unit's own sourced text, and the caption says what the figure shows and where its data comes from (module or section, author, line). No figure is drawn by hand, and nothing in a page is styled for one.
   *When a unit gets figures (P41, 29 Oct 2026).* The writer's figure pass (§4) decides them; the fresh check checks each one (every label and number traced to the unit's text, the caption names the source, the kind fits the shape); filing screenshots each new figure (`verify.py --shots <dir> --page <panel id>` saves every figure of that panel on its own, at three widths, dark and light, as its frame opens, and since P89 (2 Nov 2026) every frame a reader scrolls it across, stacked and numbered in one sheet, `<width>-<panel>-fig-<nn>-<kind>-frames-<theme>.png`). `check.py` parses and draws every declaration in a history fragment and still fails any other figure, script or style; figure blocks are left out of every word count (`build.py`'s `wc` and `check.py`), so a figure never changes a report's count.
   *Retrofits (decided by Pedro, 29 Oct 2026).* A retrofit that adds figures to a filed unit only visualises data the unit already states, so it does not count toward the four-unit audit (§6); its figures are checked by a separate agent that did not add them, and the unit's prose, citations, written date and word count do not change.
3. **Personal Mythology also files into the kit** (`kit/` in the repo), everything but the report itself, which is only its vault file (P71-3): `python3 check.py ../courses/<course>/<id>-<slug>.md` until OK; the fresh check and maintainer pass (§5); the bibliography file `bibliography/<course>/r-<id>.md`; `python3 register.py <course> "<model>" <id>`; when the syllabus unit is complete, `crosscheck.py` over its modules; `python3 build.py`, `python3 verify.py` (ALL CHECKS PASSED); publish the site to its existing artifact; add the session to `CHANGELOG.md`. The kit's `shell.css` is a copy of `design/theme.css` (repo `README.md`, "After a theme change"); the kit's `build.py` is the one build of the Personal Mythology site.
4. **A markdown course updates its course data** in its `data` file from `kit/courses.py` (`generator/data/brand-ai/hub.py`, `generator/data/ux/hub.py`; AD5; the unit itself stays only in the vault): add a `READINGS` entry for the unit's page (id `read-<code>`, course, title, `covers=[code]`, `name`, a one-paragraph intro saying what it is and its gaps; no file path: the build takes the text from the vault, and `WRITTEN` is derived there); set `STATUS[code]` to "written <d Mon>"; move `NEXT_UNIT`, `NEXT_AUDIT` and `AUDITS_RUN`; bump `VERSION`; add a `CHANGELOG` row (newest first). The unit's links join the course's bibliography automatically. Then, as for history: `cd kit && python3 build.py && python3 verify.py`, publish Academy (the artifact, then `deploy.sh`).
5. **Update `courses-index.md`:** the unit's status, model, date and vault path; the audit count for its hub; for a search-on unit, its staleness date (written + six months). A markdown course's row also carries the path of the unit's fresh-check report, which lives at `audits/<id>/fresh-check-<code>.md`. `kit/index_check.py` (run by `verify.py`) checks every row, count line and staleness date against the syllabi, `provenance.json`, the vault and the data files; a filing is not done until it passes.
6. **Check the count.** If this was the fourth unit since the last audit in its hub, the next chat is the audit (§6), not a unit.
7. **Commit and push.** The session ends with one commit naming the unit or the audit.

**A new course** of either family is a folder plus an entry in `kit/courses.py` (`new-course` skill; `kit/README.md`, "Adding a course"): a history course is `kit/<id>/` (its syllabus, an empty prompts index) with its reports in `courses/<id>/`, a markdown course is `generator/data/<slug>/` copied from `_template/` (its vault folder `courses/<slug>/` appears with the first filed unit). It appears on the Academy home after one build; its section in `courses-index.md` is added in the same chat, since `index_check.py` fails without it.

## 8 · Backlog and changelog

`docs/BACKLOG.md` holds every chat still to run, in order, one row each with the model and the prompt to paste. `docs/CHANGELOG.md` holds every chat that has run, newest first. The kit keeps its own `kit/CHANGELOG.md` for the site; a kit session writes both.

At the end of every chat that works a backlog row:
1. Move the row from the Queue to `docs/CHANGELOG.md`: date, spec, model, one-line result, commit.
2. Add every task the work uncovered as a new row marked *proposed*, in the place it belongs. Do not work it.
3. Hand the backlog to Pedro in the reply, as one short list: the row done, the proposed rows, the row next up. He confirms or edits the proposed rows and names the next row; the next chat starts there.
4. Rewrite the Project copies from `docs/`: `claude/BACKLOG-chats.md` from `docs/BACKLOG.md` and `claude/CHANGELOG-chats.md` from `docs/CHANGELOG.md`, each the full file, so the Project knowledge never lags the repo. Then commit and push.
5. Write the next prompt (Pedro, 31 Oct 2026): the paste-ready prompt for the next row in the Queue that Pedro has confirmed, self-contained, to the standard of the one this chat was given (the clone, the agent rules, each step, every check, the publish, and this step 5, so each prompt asks for the next). Save it in that row's prompt column of `docs/BACKLOG.md` before step 4, and end the reply with it in a code block. A row Pedro does by hand is skipped; the prompt is for the next row a chat runs.

A chat that finds nothing new still hands the backlog over with the next row named. A row that cannot be finished stays in the Queue with a one-line note of where it stopped.

