# Method

The one method for every course in the Learning Project. It merges the Personal Mythology method (the kit's `AGENT-SPEC.md`, `WRITER-BRIEF.md`, the Rome writing prompt and review prompt now in `kit/archive/` (`LANES.md`, `NEXT-SESSION.md`), the audit briefs and rubric) with the Brand + AI method (the hub's Build pages and Hub template). Section 1 says where they differed and what the common rule is. The rest is the method in full.

**Existing units stay valid as they are.** The 137 Personal Mythology reports already written (Greece 78, Rome 59) were written, checked and reviewed under the kit's rules and are not re-done, re-filed or re-audited under this one. Nothing here changes a course's content, a syllabus prompt or a brief.

**Home (28 October 2026).** Everything lives in the private repo `apcanario/learning`: `kit/`, `design/`, `docs/` (this file and its neighbours), `courses/` (the vault, and since S-DEC2 each markdown course's data, its pack). The claude.ai Project "Learning" holds mirrors of a named set of repo files and nothing else (§8 step 4). A chat clones the repo and ends with a commit; the kit no longer travels as a zip (`pm-status-2026-10-28.md`, D4).

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
| Per-unit check | `check.py`, then a fresh checker per report, then a maintainer pass (25 Oct 2026 pipeline) | None; the four-unit audit only | Every new unit gets a fresh check before filing (§5); Brand + AI added it on 28 Oct 2026 |
| Audit cadence | Every four complete syllabus units (`review_due.py`), sampling one report in four, scored on the rubric | Every four written units, one claim per section per unit, more than one in ten FAIL → full audit | None since 15 Nov 2026 (S-NOAUDIT): the Fable stage is closed and the four-unit audit retired; the fresh check (§5) and the six-month staleness check (§6) stand. (From 28 Oct to 15 Nov 2026 the rule was a stratified-sample claim audit every four units written in a hub.) |
| Live search | Write from knowledge; search only to verify a specific doubtful point | Flag per unit; on = search first, date facts, staleness check at six months | Every unit carries a search flag; history modules are all off (§4) |
| Length | The prompt's target is a guide, never a law (27 Oct 2026) | 2,000–6,000 words, whatever the topic needs | The topic decides; no padding, no cutting to a number (§4) |
| Writing order | Dependency order: a module starts when every report its lane note names is registered | Explicit build order with interleaving; deep dives last; audit gate | Both (§3) |
| Models | Fable 5.1 or Opus 5.5 wrote; anything not Fable flagged for Fable review | Opus 5.5 writes, Fable 5.1 audits; DD-B2, briefed for Fable, written by Opus 5.5 (the exception set aside 31 Oct 2026) | Writing Opus 5.5, fresh check Opus 5.5; the model that actually wrote a unit is recorded (§4) |
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

**Audit cadence.** Closed 15 Nov 2026 (S-NOAUDIT; Pedro: "let's stop with the fable audits and erase the audit mentions from the website"). The Fable stage is over: no further Fable audit or Fable fresh check of any course, and figures are not audited. What guards a unit now is the fresh check of every new unit before filing (§5), and the staleness check six months after a search-on unit (§6). The audit reports already run stay in `audits/` and `kit/audits/` as the record, and the dated erratum notes they produced stay in the units.

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
6. **Sources:** the unit leaves its source list (Brand + AI: a Sources list of links at the end of the file; history: `courses/<course>/bibliography/r-<id>.md`).

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

- Every hub keeps an explicit build order: one row per unit with model and search flag. Brand + AI's is the hub's Build order page; Personal Mythology's modules were ordered in `kit/archive/LANES.md` in batches of four (both courses are complete). Both are copied into `courses-index.md`.
- A unit starts only when every unit it points back to is filed (history: every report named in its lane note is registered).
- Neighbours share no material: each anecdote, dispute and self-test question has one home; the others point to it by number.
- Where two units build the same asset, write them side by side (Brand + AI: B5 beside A3, B7 beside A5).
- Core before deep dives; deep dives last. Brand + AI: DD-A2 and DD-B2 last, DD-B2 last of all (it reviews the chat history). Personal Mythology: within a deep dive, the synthesis module last (Rome 11.8), and a module whose prompt names another deep dive after that one (Rome 12.6 after 13.2).
- **Rewrite gate:** no new unit starts while a verdict of REWRITE (from a fresh check or a staleness check) is open on an earlier unit.

## 4 · Writing a unit

### One chat per unit
Open a new chat in the Learning Project for each unit. Paste the unit's brief (§4, Brief template). Never reuse a chat across units; leaked context is how a course starts repeating itself. An isolated agent context counts as a new chat (P31, 29 Oct 2026): a chat may orchestrate several units when each is written by a fresh agent on the named model, given only its brief and paths to filed units, each fresh check is a separate agent that has not seen the writing, and the orchestrating chat only files (vault, course data, build, publish). The changelog row names the arrangement. The deliverable is written in the same chat as its unit, never separately, so it inherits the unit's reasoning.

### Models
Writing: **Opus 5.5**. Fresh check: **Opus 5.5**, a separate context (§5). The Fable stage closed on 15 Nov 2026 (S-NOAUDIT): no Fable audit or Fable fresh check runs. Exceptions are named in the build order (Brand + AI DD-B2 was briefed for Fable 5.1 because it reviews the chat history; Pedro set the exception aside on 31 Oct 2026 and it was written by Opus 5.5 on 2 to 3 Nov 2026, with the past-chat tools). Sonnet and Haiku are for derivative work only (posts, Shorts lists, emails from a finished unit), never units or checks. The model that actually wrote a unit is recorded in its header and in `courses-index.md`. Personal Mythology: `register.py` records the model in `provenance.json`; since S-NOAUDIT nothing is flagged for Fable review.

**The thin main chat (S-BW1, 15 Nov 2026).** The chat of a writing row runs on **Sonnet 5.5** and records that; course design and syllabus chats run on **Fable**; the writer, the fresh checker, the applier, the filer and the corrections checker are each a fresh Opus 5.5 agent on a packet. The chat never opens a unit, a source unit, a report or a brief: it stages packets and changes files only with `kit/thin.py` (`stage`, `fixes`, `apply`, `save-report`, `assemble`, `insert`, `stats`), launches agents, and reads only each agent's reply (six lines at most) and its `out/stats.json`; every agent writes its full output to files. Scripts check the result (`index_check.py`, `private_terms.py`, the last line of `build.py`, `verify.py`, the publish read-back by sha256) and a checkpoint commit follows every agent. Trial on W-BW1: it passes if `verify.py` and `index_check.py` pass and the chat leaves no correction row; if it fails, the chat returns to Opus 5.5 and the rest stays. Units are not mirrored into the Project (Pedro, 15 Nov 2026).

### Deliverable rule
A unit is written in full with its deliverable, never outlined or summarised. The deliverable is the course's closing artefact: for Brand + AI, the thing in the unit's "Ships" line (a document, a table, a skill, a model), built in full inside the unit and usable without reading the unit; for Personal Mythology, the Self-test and Carry forward. It follows from the unit's own evidence and adds no unsourced claim.

### Length rule
The topic decides. A prompt's word count ("about 3,000 words") or range ("2,000–6,000") is a guide: some topics need 2,000 words, some 6,000. Plan the section budget, write in one pass, never pad to reach a number and never cut substance to meet one. Padding is a fault; length is not. (`check.py` reports the count as a note only.)

### Live-search flag
Every unit is flagged **on** or **off** in the build order and in `courses-index.md`.
- **Off:** write from knowledge. Search only to verify a specific date, figure or contested point you are unsure of. Every Personal Mythology module is off.
- **On:** the facts are current (prices, platform rules and thresholds, plan limits, model lineups, benchmarks, regulatory status). Search before writing; date each such fact in the text. Six months after it is written, the unit gets the staleness check (§6). Which units are on: the Search column of `courses-index.md`, the one list.

### Figure pass
After the draft, the writer goes through the unit section by section and asks of each whether its content has a shape (P41, 29 Oct 2026). Where it does, it declares the matching figure kind (`kit/viz.py`; the table of shape to kind is `skills/write-unit/SKILL.md` §4b: dated events → timeline, a sequence → flow, a hierarchy → tree or sitemap, numbers compared → compare or bars, a trend over time → line, two measures → scatter, competing estimates → range, a rule with branches → decision, roles or items by sections → matrix, a lifecycle → states, a journey across actors → swimlanes, screens → wireflow, things and their relationships → objects). The figure is drawn from the unit's own sourced text and placed directly after the paragraph or table it draws. One to four figures a unit is a guide, none where nothing has a shape; a brief that names its own number stands (the User Experience briefs: three to eight). The caption says what the figure shows and where its data comes from (section, author, line). The writer renders every figure before handing in. Syntax and rules: §7, Figures.

### Before handing in
In the same chat, the writer runs `sourcing-standard.md` Part 1 and the course's part over the unit, fixes what fails, and lists up to ten claims it is unsure of or could not verify, closing the list with an `Object:` line naming the object the unit discusses most at length, or none (P96: filing maps the page's relief from it, §7 step 4b). That list is where the checker starts (history: `reviews/<session>/<course>-<id>-writer.md`).

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
- **Brand + AI** (and every markdown course, from the `data` folder in its `courses/<id>/course.toml`): the preamble is `PRE` (the `## Preamble` of the course's `briefs.md`, `courses/<id>/briefs.md`, its pack since S-DEC2), with `{GOAL}` replaced by course A's or B's goal; the unit brief is the unit's `## <code>` section of the same file. The hub's Briefs pages show the joined text, ready to copy. Written units show their note instead. Where a course's data has `AIMS` (User Experience since S-1, 3 Nov 2026), three lines sit between the preamble and the unit brief: Aim (what the reader can do after the unit), Takes (the filed units it builds on) and Gives (what later units take from it); `kit/mdcourse.py`'s `open_brief` joins all of it, and a chat builds a brief with nothing else.
- **Personal Mythology:** the preamble is `AGENT-SPEC.md` plus `WRITER-BRIEF.md` (attached to the chat); the unit brief is the module's `<pre>` prompt in the course syllabus (the prompt is the contract) plus its lane note from `kit/archive/LANES.md` and the extra files the lane note names.

## 5 · Checking a unit before filing

- **Personal Mythology:** `python3 check.py <course>/r-<id>.html` until it prints OK (structure, 10 self-test answers, 3 carry-forward items, dispute boxes, British spelling, no em dashes). Then one fresh checker in a new chat that has not seen the unit written, briefed with `reviews/units-9-13/BRIEF.md`, the report, its prompt, its neighbours, the targets of its pointers, its lane note and the writer's unsure list; it writes findings and never edits. The maintainer verifies every finding before applying it, with exact-match replacements.
- **Brand + AI:** the writer's own pass (§4, Before handing in), then, since 28 October 2026 (§1 override triggered by Audit 1), one fresh checker in a new chat that has not seen the unit written: it checks every cited claim against its source and the deliverable against the brief, writes findings (error / should-fix / minor) and never edits; the maintainer applies each finding as an exact replacement. The `audit-units` skill runs it. A figure that fails is fixed and re-checked by a new agent from the unit's text without its figures, the captions and the frames sheets `verify.py --shots` saves (every frame a reader scrolls a figure across, phone and desktop, dark and light; P89, 2 Nov 2026). It is fixed and re-checked until it passes, never dropped (Pedro, 3 Nov 2026: "Don't drop figures, they need to succeed"). The checker's final report is saved verbatim, before any finding is applied, as `audits/<id>/fresh-check-<code>.md`, `<id>` the course entry's (`brand-ai`, `ux`; front matter: `audits/README.md`).

## 6 · Staleness check

The four-unit stratified-sample audit and its review rule are retired (S-NOAUDIT, 15 Nov 2026: the Fable stage is closed, §1). Two checks remain: the fresh check of every new unit before filing (§5) and this one. The audit reports already run stay in `audits/` and `kit/audits/` as the record; the course audits written into a history syllabus (Greek unit 13, Rome unit 14) are course content and stay as their prompts say.

### When
Six months after any unit written with search on (due dates in `courses-index.md`).

### How
Six months after a search-on unit was written, in a new chat (or an isolated agent context) with Opus 5.5 and live search, this prompt, verbatim:

```
You are re-checking one unit written with live search six months ago: {unit code, vault path, date written}. Search again, today, for every fact in it that can change: platform rules and thresholds, prices and plan limits, model lineups, benchmark figures, regulatory status, the numbers attached to named creators. For each: the value in the unit, the value now, the source and date for the new value, and whether the unit's conclusion still holds. End with a verdict: CURRENT / PATCH (list the lines to change) / REWRITE (say which sections). Do not rewrite; report.
```

### After a staleness check
- PATCH: each line is applied as an exact replacement (the current text must occur once), checked before it is applied, with a dated erratum note in the unit.
- REWRITE: the unit is rewritten in a new chat from its brief before any new unit starts (§3, rewrite gate).
- The course's data file gets a `CHANGELOG` row and `courses-index.md` records the check and the next due date.

## 7 · Filing a finished unit and updating its hub

Run the `file-unit` skill, or by hand. Since A5 (`academy.md`) the vault is the source of a markdown course: Academy reads its units from `courses/<course>/`, and a unit is written when its file is there with front matter. Since P71-3 (1 Nov 2026) the same holds for Greece and Rome: a history report is its vault file, Markdown read by `kit/mdcourse.py` (`history_html`, through `kit/vault.py`), and the kit holds no copy (`docs/p71-3.md`).

1. **Name.** `<code>-<slug>.md`: the unit code, then the title in lower case with words joined by hyphens, accents and punctuation dropped (`B1-mental-model.md`, `11.3-politics-in-the-street.md`).
2. **Save to the vault** at `courses/<course>/<code>-<slug>.md`, where `courses/<course>` is a markdown course's `vault` in its `courses/<id>/course.toml` (`courses/brand-ai`, `courses/ux`) and `greece` or `rome` for Personal Mythology. Put the header first as front matter:
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
   Brand + AI: the unit in Markdown, ending with its deliverable and a Sources list of links; this file is what Academy renders, so there is no second copy. Personal Mythology: the report in Markdown below the front matter and a `# <title>` line, in the forms of `kit/AGENT-SPEC.md` (since P71-3; `model` is the writer only, the review status stays in the course's `inputs/provenance.json`); its Sources are the bibliography file in the course folder (step 3), not a list in the report.
   **A new course files Markdown only (P71, §2).** Its unit is this one file: front matter, text, Sources, ` ```viz ` blocks; no HTML, no class, no style and nothing about layout in it, since the build adds all of that for the site and for the EPUB (`build.py --epub <edition>`, `kit/epub.py`).
   **Figures (A8, 28 Oct 2026).** A unit may declare a figure where structure is the content (a timeline, a comparison of numbers, a line of descent, a sequence of steps); `kit/viz.py` draws it as inline SVG at build time and `design/theme.css` §4i styles it. Every course (Personal Mythology too since P71-3): a fenced ` ```viz ` block holding the JSON, `kind` first and `caption` last (until P71-3 a history fragment declared it as `<figure class="viz" data-viz="timeline"><script type="application/json">{…}</script><figcaption>…</figcaption></figure>`). The kinds and fields are in `viz.py`'s docstring: timeline, compare, tree and flow, and, since V1 (29 Oct 2026) for the Information Architecture course, sitemap, objects, decision, matrix, states, swimlanes and wireflow; and since P44 (29 Oct 2026) the data kinds line, bars, scatter, range and a numeric matrix. Academy's Figure kinds page (`#viz-examples`) draws one of each with the block that draws it. A figure's numbers and names are claims: they come from the unit's own sourced text, and the caption says what the figure shows and where its data comes from (module or section, author, line). No figure is drawn by hand, and nothing in a page is styled for one. A compare's and a bars figure's phone drawing is 258 units wide, a 320 px phone's frame, so every bar and its value open whole on any phone, and a printed value sits wholly on its track or wholly beyond the track's end, never across it (P97, P98, 12 Nov 2026; `verify.py`'s `check_phone_figures` checks both).
   *When a unit gets figures (P41, 29 Oct 2026).* The writer's figure pass (§4) decides them; the fresh check checks each one (every label and number traced to the unit's text, the caption names the source, the kind fits the shape); filing screenshots each new figure (`verify.py --shots <dir> --page <panel id>` saves every figure of that panel on its own, at three widths, dark and light, as its frame opens, and since P89 (2 Nov 2026) every frame a reader scrolls it across, stacked and numbered in one sheet, `<width>-<panel>-fig-<nn>-<kind>-frames-<theme>.png`). `check.py` parses and draws every declaration in a history fragment and still fails any other figure, script or style; figure blocks are left out of every word count (`build.py`'s `wc` and `check.py`), so a figure never changes a report's count.
   *Retrofits (decided by Pedro, 29 Oct 2026).* A retrofit that adds figures to a filed unit only visualises data the unit already states: its figures are checked by a separate agent that did not add them, and the unit's prose, citations, written date and word count do not change.
3. **Personal Mythology also files into the kit** (`kit/` in the repo), everything but the report itself, which is only its vault file (P71-3): `python3 check.py ../courses/<course>/<id>-<slug>.md` until OK; the fresh check and maintainer pass (§5); the bibliography file `courses/<course>/bibliography/r-<id>.md` (S-DEC5: the course's syllabus, prompts index, provenance and bibliography sit in its folder, named by its `course.toml`); `python3 register.py <course> "<model>" <id>`; when the syllabus unit is complete, `crosscheck.py` over its modules; `python3 build.py`, `python3 verify.py` (ALL CHECKS PASSED); publish the site to its existing artifact; add the session to `CHANGELOG.md`. The kit's `shell.css` is a copy of `design/theme.css` (repo `README.md`, "After a theme change"); the kit's `build.py` is the one build of the Personal Mythology site.
4. **A markdown course updates its course data** in its `data` file from its `courses/<id>/course.toml`, which is that same file: its pack, the `[pack]` table read by `kit/pack.py` (S-DEC2; AD5; the unit itself stays only in the vault; `kit/thin.py insert` writes it, and filing a unit touches no `.py` file): add `intro` to the unit's front matter, a one-paragraph intro saying what it is and its gaps, and `name` only where it is not "<code> · <title>" (the unit's reading-page entry, id `read-<code>`, course, title, `covers=[code]`, is derived from it; no file path: the build takes the text from the vault, and `WRITTEN` is derived there); `STATUS` ("written <d Mon>", from the front matter's `written`), `NEXT_UNIT` and `VERSION` (from the changelog's top row) are derived, never typed, and a status the front matter cannot give goes under `[pack.status]`; add a `[[pack.changelog]]` row (newest first, its text opening with the new version, `v<n>. `). The unit's links join the course's bibliography automatically. Then, as for history: `cd kit && python3 build.py && python3 verify.py`, publish Academy (the artifact, then `deploy.sh`).
4b. **The page's relief (P96, 8 Nov 2026).** Every reading page shows one object relief or records none: where the text discusses an object at length, not in passing (the writer names it on the `Object:` line closing the unsure list, §4), the page is mapped to an outline of the library `design/outlines/` (P95) in `kit/p96_uses.py` with the sentence that decided it, which writes `design/outlines/uses.json` and `uses-why.md`; an outline the library lacks is added under P95's sourcing and busy-relief rules (`kit/p95_library.py`, `kit/relief.py`); a page that discusses no object is listed as none. Every course keeps at least ten outlines in use (a course with fewer than ten pages, one on every page that discusses an object) and every outline in the library is in use or marked spare; `verify.py` checks both (`file-unit` §4b).
5. **Update `courses-index.md`:** the unit's status, model, date and vault path; for a search-on unit, its staleness date (written + six months). A markdown course's row also carries the path of the unit's fresh-check report, which lives at `audits/<id>/fresh-check-<code>.md`. The index is two files since P30-F17 (17 Nov 2026): `docs/courses-index.md` holds the courses in progress, the staleness table and the courses to come, and `docs/courses-index-archive.md` the finished courses' sections, moved there whole in the chat that files a course's last unit; a REWRITE verdict on any unit is recorded in the live file's Staleness section. `kit/index_check.py` (run by `verify.py`) reads both as one index and checks every row, count line and staleness date against the syllabi, `provenance.json`, the vault and the data files; a filing is not done until it passes.
6. **Commit and push.** The session ends with one commit naming the unit, `kit/verify-hashes.json` included (the record `verify.py` writes after ALL CHECKS PASSED, S-DEC4; without it the next chat's first run is a full one).

**A new course** of either family is a folder, `courses/<id>/`, holding its `course.toml` (S-DEC1, 20 Nov 2026: no file under `kit/` is edited; `kit/courses.py` finds the file; `new-course` skill; `kit/README.md`, "Adding a course"), with its id added to `course_order` in `catalog.toml`: a history course adds `courses/<id>/inputs/` (its syllabus, an empty prompts index, its provenance file) and `courses/<id>/bibliography/` (S-DEC5, 20 Nov 2026), and its reports in `courses/<id>/`, a markdown course adds its pack (`course.toml` with its `[pack]` table, `briefs.md`, `pages/`) in `courses/<slug>/`, copied from `courses/_template/`. It appears on the Academy home after one build; its section in `courses-index.md` is added in the same chat, since `index_check.py` fails without it. It starts with at least ten outlines in the library that its texts will discuss (`new-course` step 5b).

## 8 · Backlog and changelog

`docs/BACKLOG.md` holds every chat still to run, in order, one row each with the model and the prompt to paste. `docs/CHANGELOG.md` holds every chat that has run, newest first. The kit keeps its own `kit/CHANGELOG.md` for the site; a kit session writes both. None of the three is on the site: Academy's Backlog and Changelog pages are rendered from `docs/site-log.md` alone (S-PAGES, 15 Nov 2026), a plain overview by area (Mythology, Marketing, AI, UX, Sports, Supply Chain, Academy) with one entry per unit, course milestone or visible site change; its header gives the rules of an entry (plain words, no private term, housekeeping and corrections folded into the item they served).

At the end of every chat that works a backlog row:
1. Move the row from the Queue to `docs/CHANGELOG.md`: date, spec, model, one-line result, commit.
1b. Update `docs/site-log.md` (S-PAGES): move the row's entry from Next to Done with the date and one plain sentence of what happened (or add it to Done if it had none, or leave it out if the row was housekeeping or a correction, folded into the item it served), renumber Next, and add an entry to Next, in its place in the order, for each item Pedro confirmed into the queue. A writing row's sentence is the unit's code and title, "written", and "course <X> complete" for its last unit. `python3 kit/private_terms.py` prints OK and `verify.py` (`check_site_log`) passes on the rebuilt pages.
2. Every task the work uncovered is a proposal. **Standing rule (Pedro, 15 Nov 2026):** the reply lists every proposal on delivery, each with what it does and a ⚠ flag on any disruption elsewhere in the project; it is written as a row in the Carried proposals section of `docs/BACKLOG.md`, appended to the next row's prompt by `kit/next_prompt.py` (step 1c) and worked in that chat unless Pedro removes it. A brief change or a task only Pedro can do is a row marked *proposed* that nobody works until he confirms it. **Standing rule (Pedro, 17 Nov 2026):** every task left for Pedro by hand (a row under Proposed marked for him) is listed in every chat's reply, with its row number, until he says it is done; the reply never drops one because the chat did not touch it. The W-PB7 same-chat corrections rule is unchanged, from W-PB7 on: a correction to a filed unit or a record, or a kit fix, that the work uncovered is made in the same chat before it closes, each change to a unit checked by a fresh agent against its source and the syllabus before it is applied; only a brief change and a task for Pedro stay proposed, and a correction still open (a stopped row) goes into the Corrections section of `docs/BACKLOG.md` for the next prompt (Pedro, 12 Nov 2026, 21:31; `docs/public-courses.md` §3 rule 12).
3. Hand the backlog to Pedro in the reply, as one short list: the row done, the proposed rows, the row next up. He confirms or edits the proposed rows and names the next row; the next chat starts there.
4. Rewrite the Project copies from the repo. **The Project's knowledge is a named set (P30-F1, 17 Nov 2026):** `reader.md`, `method.md`, `sourcing-standard.md`, `courses-index.md`, `claude/BACKLOG-chats.md`, `claude/CHANGELOG-chats.md`, and, only while a course is being written, that course's three data mirrors (`claude/<course>-course.toml`, `claude/<course>-briefs.md`, `claude/<course>-syllabus-flags.md`). Nothing else is uploaded: every other file is read from the clone. Each chat rewrites `claude/BACKLOG-chats.md` from `docs/BACKLOG.md` and `claude/CHANGELOG-chats.md` from `docs/CHANGELOG.md`, each the full file, so the Project knowledge never lags the repo, and refreshes the method, the index and the course's data mirrors only when the chat changed them. The chat that files a course's last unit deletes that course's three data mirrors from the Project and moves its section of `courses-index.md` to `docs/courses-index-archive.md` (§7 step 5). **No unit is uploaded** (Pedro, 15 Nov 2026: units are not mirrored into the Project; the repo and Academy carry them). Then commit and push.
5. Write the next prompt (Pedro, 31 Oct 2026): the paste-ready prompt for the next row in the Queue that Pedro has confirmed, self-contained, to the standard of the one this chat was given (the clone, the agent rules, each step, every check, the publish, and this step 5, so each prompt asks for the next). Save it in that row's prompt column of `docs/BACKLOG.md` before step 4, and end the reply with it in a code block. A row Pedro does by hand is skipped; the prompt is for the next row a chat runs.

A chat that finds nothing new still hands the backlog over with the next row named. A row that cannot be finished stays in the Queue with a one-line note of where it stopped.


## 9 · Standing rules for every new course

Two rules hold for every course designed from 19 Nov 2026 on, whatever its syllabus says, so that no later course has to be told them (Pedro, standing; first written for Supply Chain Execution for Product Teams, row S-SCE0, `docs/supply-chain-execution-prompts.md` §4). The `new-course` skill makes both part of each new course's preamble, sourcing part, prompts document and writing rows. They add to the rules above and change no existing course's briefs or filed units.

### The carry-forward rule

Nothing found goes unrecorded or waits for a later audit. It applies to every row of the course, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or Pedro.
2. **About a unit already filed.** It goes into the next row's prompt as a correction, with the unit, the passage, what is wrong and the source. The next chat fixes it first, before it writes its own unit: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About a unit not yet written.** It becomes a flag in the course's `syllabus-flags.md` naming every unit it affects, and it is printed in each of those units' prompts as a guideline for the writer. A flag that would change a brief is proposed, never applied by the chat that raised it.
4. **About the unit being written.** It is fixed in the same chat before filing. What cannot be fixed (a source that will not open) is cut or marked unverified in the unit, and carried as in 2.
5. **Every delivery ends with the next prompt.** The reply of every row closes with the prompt for the next unit in a code block, as `kit/next_prompt.py` prints it, already holding: every correction still open on a filed unit, every open flag that names the next unit, and any guideline of the course's writing template that the row showed needs updating, with the update made. A row that finds a rule of the template wrong or unworkable corrects it in the course's prompts document (`docs/<course>-prompts.md`), says what it changed, and the next prompt carries the corrected text.
6. **Nothing is dropped silently.** A correction or flag leaves the next prompt only when it is resolved, with the row and the report that resolved it written beside it.
7. **The last row** (the course's last unit in its writing order) delivers a closing corrections prompt in place of a next unit's, listing every correction and flag still open.

### The source-credibility floor

- **Opened before cited.** Every reference is opened before it is cited: found by a search and read at its publisher's page, its DOI address or the issuing body's own page, and logged in the unit's source log with the address opened, what was read (abstract, reprint or full text) and the date. A reference that could not be opened carries no claim.
- **A short seed bibliography, checked for existence only.** A course's seed bibliography is short, and each entry is checked for existence against Crossref's or the publisher's record before the first unit is written. It is never an authority on what a source says.
- **Graded claims.** Every claim carries an evidence grade from a key that the course's first unit sets; every later unit uses that key.
- **Never sources.** Videos, podcasts, social-media posts, unsigned blogs, lead-generation sites and press rewrites are never sources; one may be named only as the claim under examination.
- **Interested parties.** A statement by an interested party (a vendor, a sponsor, a body that sells what it describes) is labelled as such.
- **Fewer, better.** Fewer sources read in full are preferred to many read in abstract; a claim that rests on an abstract alone says so.
- **Unsourced is said.** A claim that cannot be sourced is said to be unsourced or left out.
- **The fresh checker verifies both.** The fresh checker verifies every reference's record (authors, title, journal or publisher, year, volume, pages, DOI) and every cited claim against its source; a source it cannot open is "not opened", never a pass.
