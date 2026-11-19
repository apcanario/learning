# Registration report · S-SCE0 · Supply Chain Execution for Product Teams

Registrar: one isolated Opus 5.5 agent (claude-opus-5-5), 19 Nov 2026. Inputs: the seven files in `/home/claude/scratch/sce` and the clone at `/home/claude/learning` (branch `main`, HEAD `382fee3`). Nothing committed or pushed. No unit written. No brief, no line of `PRE` and no `AIMS` line reworded; the only change to `units_data.py` is the name replacement of (a).

This file is at `out/registration.md` in the clone. `out/` is not ignored by `.gitignore`; the checkpoint commit 82caee5 added this file, so it is tracked (corrected by the registration check, finding 11).

## (a) Names

One web search per name, 19 Nov 2026.

| Name | Result | Action |
|---|---|---|
| Corvane | No company of that name. Near names only: Corvan (a Belgian general trader), Corovan Moving & Storage, Corvaer, Corvalent | kept |
| Ostrel Foods | No match (Omstead Foods, Outcast Foods and others unrelated) | kept |
| Tandric Logistics | No match (Tandet Logistics Inc., a carrier, is the nearest) | kept |
| Halvern Systems | No match (Haven Systems, Haverly Systems, Halverstone) | kept |
| Brindle Software | **Match.** "Brindle", a team of designers and developers that makes software (WordPress plugins: Brindle Booking, QuickPop, SleekAnnounce), mybrindle-com.pages.dev; also "Brindle", a digital-marketing vendor listed on revyse.com | **replaced** |
| Kestrow | No match (Kestrel companies only) | kept |

Replacement coined: **Varnby Software** ("Varnby" in short). One search ("Varnby" software company): no company of that name (only Vårby, a Stockholm suburb, and Varnish Software). Exact replacements of "Brindle" by "Varnby", counted, in a working copy (`/home/claude/scratch/sce-work/`); the originals in `/home/claude/scratch/sce/` are untouched:

| File | Replacements |
|---|---|
| case-facts.md | 4 |
| syllabus.md | 2 |
| prompts.md | 1 |
| units_data.py | 1 (SCE17's brief: "Halvern Systems, Varnby Software, Kestrow") |
| setup-prompt.md | 1 |
| bibliography.md, track-coming-soon.md | 0 |
| **Total** | **9** |

`units_data.py` in the repo equals the original with "Varnby" put back to "Brindle" (`diff` empty). sha256 of the repo copies: units_data.py `cb181b97…d734e`, case-facts.md `263b7c57…9a2a`, bibliography.md `4b25e13d…76f2` (identical to the original, which had no coined vendor name to replace).

## (b) Data folder

- `generator/data/supply-chain-execution/` copied from `_template/`; `units_data.py`, `case-facts.md`, `bibliography.md` put in (after (a)). It parses: 20 units, 20 `AIMS`, one `{GOAL}`.
- `syllabus-flags.md`: the header and status line of sport-psychology's file, the title changed, no rows. One flag was then raised by this row (F1, below, under "Carried forward").
- `hub.py` filled from the syllabus: identity (title, bar, brand, out, theme key, v1 · 19 Nov 2026); one course `SCE`, gold, goal = syllabus §3 word for word but for a lower-case first letter (the page capitalises it), three outcomes word for word with the units that deliver them; `ORDER` SCE1 to SCE18, DD-SCE1, DD-SCE2, all Opus 5.5, search on for SCE1, SCE6, SCE8, SCE9, SCE11, SCE12, SCE16, SCE17, DD-SCE1 (§4/§5); `FRAME` = §1 (pick, three reasons, override, what the course is for, out of scope, no real vendor assessed, where the evidence pushes back); ledes, Build page (procedure, models, review rule, the gate after SCE6), order notes, changelog v1 `2026-11-19 20:22`. No private term.
- `docs/supply-chain-execution-syllabus.md` and `docs/supply-chain-execution-prompts.md` saved (after (a)); the prompts file gained a last section in (i).

## (c) courses.py

`SUPPLY_CHAIN_EXECUTION` added to `COURSES` after `SPORT_PSYCHOLOGY`, in sport-psychology's form: `family='markdown'`, `data='generator/data/supply-chain-execution/hub.py'`, `vault='courses/supply-chain-execution'`, `tracks={'SCE': ('supply-chain', 'Supply chain execution · public')}`, `tiles`, `sourcing_part='Part 8'`, `source_units=False`, `prompts_doc='docs/supply-chain-execution-prompts.md'`, plus a new key `dated_lists=True` (for (e)). New track in `THEMES`: `dict(id='supply-chain', name='Supply Chain', color='var(--gold)', lede=…)`; gold is the one theme colour no track used.

## (c2) Coming soon

**Adaptation.** `NEXT` in `kit/courses.py` is History's list only (the build draws it only in the History track). The repo's form for a non-History track's courses to come is the track's own `planned` list in `THEMES` (added by S-SPORTS for the Sports track): 5-tuples `(short, name, colour, scope, spine)`, drawn as ghost tiles on the home's track section, inside a folded block, each opening to its "spine" line under a label (`planned_label`). Used that form:

- The four courses in the file's order, each: short chip name (Planning, Automation, AI, Last mile), the title word for word, the scope line word for word (without the "Scope." lead), and the teaser: `planned_label = "After this you'll know how to"` (the teaser's bold opening words) and the tuple's last field the rest of the teaser, word for word. On the page the tile opens to "AFTER THIS YOU'LL KNOW HOW TO read a demand forecast …", the whole teaser.
- **Build change (smallest):** a track may set `planned_heading`; the folded block's heading is then that text ("Coming soon" here, "Planned" by default, so History and Sports are unchanged), and the track's count line says "· 4 more coming soon" (default "· N planned"). `kit/build.py`, two lines.
- Checked in the built `kit/academy/index.html`: section `#track-supply-chain`, header count "1 course coming soon · 0 of 20 units · 4 more coming soon" (built page checked) (the first part is the existing G-0 wording for a course with nothing filed, which has no tile and is listed in the drawer), block `#planned-supply-chain` headed "Coming soon", the four ghost tiles in order with title, scope and teaser.
- The "track's page" is the track's section of the home; there is no separate track page in Academy. The planned courses are not in the drawer (only History's are; unchanged).
- No data folder, brief or writing row for any of them. `docs/courses-index.md` gains "## Courses to come (Supply Chain)" after the Personal Mythology one. `docs/BACKLOG.md` gains P-SCE10 (*proposed*).
- Also needed for the build: the hero drawing needs a place per track (`_HERO_AT` in `build.py`; the build stopped without one). Supply Chain placed at top centre (tall .50/.17, wide .50/.13), a planned ring until its first unit is filed. Verify passed it (below).
- Also: the site log has one area per track; added area "Supply Chain" (course SCE) to `SL_AREAS` in `kit/build.py` and `kit/verify.py`, and to the area rule in `docs/site-log.md` and the list in `docs/method.md` §8 (which still said "Coaching"; now "Sports, Supply Chain").

## (d) Public course

`docs/public-courses.md`: the opening paragraph names the fourth course; §1 gains SCE · D1 to D12 from syllabus §8 word for word, in SP's row form (D1 and D12 "Decided by Pedro, 19 Nov 2026", the rest "Stands unless vetoed"); §2's table gains a column for SCE (entry, data, vault, fresh checks with "no safety reader", Parts 1 and 8, 18 core + 2 deep dives, no source units, the case of three operations and three vendors, track Supply Chain (new), flags). §3: rule 4 (does not apply, no source units), rule 8 (the dated-list exception and how `private_terms.py` applies it), rule 9 (case facts appended to "Added by units" at filing: unit, operation, fact), rule 10 (G-R-SCE). Rule 13 applies unchanged.

## (e) Private terms

**Changed**, `kit/private_terms.py` and `kit/private-terms.txt`:

- `PUBLIC` gains `supply-chain-execution`.
- `private-terms.txt` gains a commented block and `employer: Infios`. An `employer:` line is read only by the new `employer()`; `terms()` skips it, so every other course is scanned exactly as before ("Infios" stays a plain fail line too).
- On files of a course with `dated_lists=True` (its vault, data folder and built pages, or any file given with `--course supply-chain-execution`): an employer term fails anywhere except on a line inside a dated list: a Markdown list or table (lines starting `- `, `* `, `1. `, `|`), or a built page's `<ul>`/`<ol>`/table, whose lead-in line names an analyst firm or filing (`DATED_BY`: Gartner, Forrester, IDC, Nucleus Research, MarketScape, Magic Quadrant, Value Matrix, analyst, filing, annual report, 10-K) and a year 1900–2099. An `employer:` term that is not also a plain line (a product name) is checked only on that course's files.
- Proof: (1) on the 97 files of the other public courses and the site log, the old and new scripts give identical hits and identical warnings (114); (2) dummy files: an employer entry in a Markdown list and a table after "Gartner's Magic Quadrant … (29 April 2026)" passes; the same name in a sentence, and in a list with no dated lead-in, fails; in built HTML, a `<ul>` after a `<p>` naming IDC's MarketScape of 2026 passes, a sentence and a table after an undated lead fail; the same file without `--course` fails as before; (3) a temporary `employer: Zorbex` fails on an SCE file outside a list and is not checked without the course (removed after). `python3 kit/private_terms.py`: 105 files, 0 private terms, OK.
- **Not done: product names.** The repo holds no product name of the employer (searched every `.md`, `.py`, `.txt`, `.json`, vault included): only "Infios" in `private-terms.txt` and two private Brand + AI lines. I did not add names from memory. Each product name goes in as its own `employer:` line; until then the check guards only the employer's name. Row P-SCE11 of `docs/BACKLOG.md` asks Pedro for them (added by the registration check, finding 1).
- **Limit:** the dated-list test is mechanical; it cannot tell a real analyst list from any list after a sentence that names an analyst and a year. The fresh checker's pass 4 (vendors) is the real guard.
- **Risk carried forward (flag F1):** "ToolsGroup" (and any other company on the plain list) fails everywhere, list or not, so an analyst list naming it cannot be reproduced whole. Not changed: the instruction allows only the employer in a list.

## (f) Sourcing

`docs/sourcing-standard.md`: opening line now "Parts 2 to 8 … (Part 8 from its course's syllabus, section 6)"; Part 8 appended, "## Part 8 · Supply Chain Execution for Product Teams (from section 6 of `docs/supply-chain-execution-syllabus.md`)", the 22 checklist lines of §6 word for word (with "Varnby Software" from (a)). `thin.py`'s `sourcing_text` picks Parts 1 and 8 for this course (proved in (h)).

## (g) Standing rules

- `docs/method.md` gains "## 9 · Standing rules for every new course": an intro; "The carry-forward rule", prompts.md §4's seven points with the course's names made general (the course's `syllabus-flags.md`; the course's prompts document `docs/<course>-prompts.md`; "the course's last unit in its writing order" for W-DD-SCE2); "The source-credibility floor", the eight items listed in the instruction. It changes no existing course's briefs or units.
- `skills/new-course/SKILL.md` gains step "## 4b. The standing rules (`method.md` §9)": both rules made part of every new course (the floor into the preamble's sourcing standard and the course's part; the carry-forward rule into the course's prompts document, so `next_prompt.py` prints it), not retroactive.

## (h) Staging

- `python3 kit/thin.py stage writer --row W-SCE1 <dir>` worked with no change to the writer path: `brief.txt` (open_brief: preamble with the goal, then Aim, Takes, Gives, then the unit brief), `write-unit-SKILL.md`, `sourcing-standard.md` (opening, Part 1, Part 8 only), `viz.py` (the figure kinds), `case-facts.md`, `bibliography.md`, `filed/` (empty: none yet), `flags.txt` (empty at the time), `course-map.txt`, `out/`.
- `stage checker` (with `--sources`), `stage applier` (1 dummy finding parsed into `fixes.json`) and `stage filer` all worked on W-SCE1 with dummy unit, notes, unsure, sources and report files (`/tmp/stagetest/in/`).
- **One change, `kit/thin.py`:** the filer's rule 5 hard-coded sport-psychology's "Added by units" form (`| <code> | <the fact> | <athlete> |`), wrong for this course's table (`| Unit | Operation | Fact |`). New `case_rule(case)` reads the table's header; for SP's header (or none) it prints the old text unchanged; for SCE: `| <code> | <operation> | <fact> |`.
- Regression: the writer, checker, applier and filer packets of W-DD-SP3 from the old and the new `thin.py` are identical (`diff -r`); `stage writer --row W-BW1` still works.

## (i) Queue and prompt

- **Adaptation:** `QUEUE` in `kit/next_prompt.py` holds course ids, not rows; rows come from each hub's `ORDER`. Appended `'supply-chain-execution'` after `'sport-psychology'`: `--list` shows W-SCE1 … W-SCE18, W-DD-SCE1, W-DD-SCE2 in that order, after W-DD-SP3.
- `next_prompt.py` changes: (1) `doc_parts` accepts a prompts document with no "### The safety reader" block; (2) the last row's "next" text names the course's own reliefs row, `G-R-<key>` (G-R-SP unchanged for SP, G-R-SCE here); (3) `GATES = {'W-SCE7': 'P-SCE6'}`: while row P-SCE6 is in `docs/BACKLOG.md`, W-SCE7's prompt opens with "Do not run until Pedro has closed P-SCE6." (proved: the line is there now, and not on W-SCE6's). Regression: the prompts of W-SP1, W-SP9, W-DD-SP1, W-DD-SP2, W-PB3 and W-BW2 are byte-identical from the old and new script. **W-DD-SP3's printed prompt changes in one place:** its step 11 now saves "the prompt of W-SCE1 (unit SCE1)" instead of "the next row … G-R-SP". That follows from queueing SCE after SP and is correct; the prompt already saved in W-DD-SP3's row was not re-saved.
- `docs/supply-chain-execution-prompts.md` gains "## Rows W-SCE1 to W-DD-SCE2 · write one unit": the sport-psychology template copied, with only these replaced: name, code, slug, paths, Part 8; the writer's sourcing bullets → section 1's rules; the seven passes → section 2's; the row table → section 3, word for word, in the four-column form the script reads (Row | Unit | Search | Paragraph); section 4 added word for word as a paragraph after the thin-chat paragraph; step 5b and the safety-reader mentions dropped; "the coach in the preamble" → "the reader"; "course SP complete" → "course SCE complete"; the Reply's tasks for Pedro → P-SCE1, P-SCE6, P-SCE7. Rule 13 (quality review) is kept: `next_prompt.py` prints it when the flag counts call for it.
- **Template guidelines corrected for this repo** (listed in the section's own note):
  1. Writer rule 11 said flags go to `out/flags.md` "in the form of syllabus-flags.md". The filer's packet has no `out/flags.md`; the filer reads `notes.md`. Now: written to `out/notes.md` under Contradictions or Needs, naming every unit, with a proposed change; the filer writes them into `syllabus-flags.md`.
  2. Writer rule 12 listed `out/flags.md` and `out/stats.json` as the writer's hand-in. `stats.json` is written by the chat with `thin.py stats`. Now: `out/unit.md`, `out/sources.md`, `out/notes.md` (Case facts, Contradictions, Needs), `out/unsure.md` with the `Object:` line, figures rendered, a six-line reply.
  3. The SP template's own sourcing bullets for the writer are replaced by section 1 (which covers each); its agent rules (memory, tools, publishing, the web rule) and its `write-unit` line are kept.
  4. The gate line of W-SCE6's paragraph is printed by the script (`GATES`), not left to the chat.
- Proof on W-SCE2, with a dummy correction (row C-DUMMY in the Corrections section of `docs/BACKLOG.md`) and a dummy flag (F1 naming SCE2, SCE7): W-SCE2's prompt printed both, with the limits (a) to (f); W-SCE3's printed only the correction (corrections are global, as for SP); W-SCE7's printed both. Both dummies removed: `BACKLOG.md` and `syllabus-flags.md` restored from copies, `grep DUMMY` = 0.
- W-SCE1's prompt prints in full (3,024 words), no unfilled slot, no leftover SP, sport, athlete, coach, Part 7 or step 5b (scanned on W-SCE1, W-SCE9, W-DD-SCE2).
- `docs/BACKLOG.md`: new heading "### 4d · Supply Chain Execution for Product Teams (registered 19 Nov 2026, row S-SCE0)" after 4c's last row, intro, 20 rows W-SCE1 … W-DD-SCE2 (spec, model "Sonnet 5.5 (thin main chat; … each a fresh Opus 5.5 agent)", prompt cell naming `next_prompt.py --row`). W-SCE6's and W-SCE7's spec cells carry the gate. "Next up" left at W-DD-SP3.
- `docs/site-log.md` Next: entries 2 to 21, "Write SCE1, The map, the words and the evidence, for Supply Chain Execution for Product Teams." and so on, area Supply Chain; no private term (`private_terms.py docs/site-log.md` OK).

## (j) Gate and proposals

Under Proposed in `docs/BACKLOG.md`: P-SCE1, P-SCE6, P-SCE7, each "*Proposed, for Pedro, by hand.*" with syllabus §9's words (P-SCE6 adds that W-SCE6 still delivers W-SCE7's prompt under the "Do not run until …" line); G-R-SCE *proposed* (P-SCE8's words and the outline-library steps of G-R-SP's row); P-SCE10 *proposed* (§9's words and the four titles). P-SCE2 to P-SCE5 and P-SCE9 are done by (a), (e), (f), (g), (i) of this row and go to the changelog with S-SCE0's close.

## (k) Index

`docs/courses-index.md`: "## Supply Chain Execution (public)" (the course's `short`, the heading `index_check.py` looks for) before "Courses to come", in SP's form: an intro paragraph with "0 of 20 written", then 20 rows in order, "not written", Opus 5.5, the search flag, the vault path by `index_check.slug`. "## Courses to come (Supply Chain)" added at the end. `python3 kit/index_check.py`: "courses-index.md matches the sources" (first run and after every later change).

## Build and verify

- `cd kit && python3 build.py`: "… Supply Chain Execution (public): 0/20 units · shell 538 KB …" (shell was 512 KB).
- `python3 verify.py`, first run (22 min): every check passed but six site-log lines ("the order table has 1 rows, not the site log's 21"), because the 20 Next entries were added after that build. After a second build: `python3 index_check.py` matches; `python3 verify.py` **ALL CHECKS PASSED** (23 min); `python3 private_terms.py` 105 files, OK.
- `kit/README.md` (sizes table) and `kit/academy/index.html` change on every build; `kit/academy/supply-chain-execution-sce/` is new (4 files).

## Every file created or changed

Created: `generator/data/supply-chain-execution/{hub.py, units_data.py, case-facts.md, bibliography.md, syllabus-flags.md}`, `docs/supply-chain-execution-syllabus.md`, `docs/supply-chain-execution-prompts.md`, `kit/academy/supply-chain-execution-sce/` (built), `out/registration.md` (this file; tracked since the checkpoint commit 82caee5).

Changed: `kit/courses.py`, `kit/build.py`, `kit/verify.py`, `kit/thin.py`, `kit/next_prompt.py`, `kit/private_terms.py`, `kit/private-terms.txt`, `kit/README.md` and `kit/academy/index.html` (built), `docs/BACKLOG.md`, `docs/courses-index.md`, `docs/public-courses.md`, `docs/sourcing-standard.md`, `docs/method.md`, `docs/site-log.md`, `skills/new-course/SKILL.md`.

## Carried forward (nothing left only here)

- **Flag F1** in `generator/data/supply-chain-execution/syllabus-flags.md` (open; affects SCE6, SCE8, SCE9, SCE16, SCE17; raised by S-SCE0): the dated-list form `private_terms.py` needs, and what to do when an analyst list names a company on the plain private-terms list. Printed in those units' prompts (checked on W-SCE6).
- **For the main chat's close (setup-prompt step 6):** plain `python3 kit/next_prompt.py --save` saves W-DD-SP3's prompt (the next unfiled row), not W-SCE1's. Use `python3 kit/next_prompt.py --row W-SCE1 --save`.
- Proposals P-SCE1, P-SCE6, P-SCE7 (Pedro by hand), G-R-SCE and P-SCE10 (*proposed*) are rows of `docs/BACKLOG.md`.

## Found wrong in the seven files

1. "Brindle" collides with a real software maker; replaced (a).
2. prompts.md §1 rules 11 and 12 name `out/flags.md` and a writer-made `out/stats.json`, which the repo's thin chat does not use; corrected in the prompts file's template (i).
3. setup-prompt.md (i) asks for rows in `QUEUE`; the repo's `QUEUE` lists courses. Adapted (i).
4. setup-prompt.md (c2) points to `NEXT` as the form for courses to come; that is History's list only; the repo's form for another track is `THEMES[...]['planned']`. Adapted (c2).
5. setup-prompt.md step 6: `next_prompt.py --save` without `--row` saves W-DD-SP3's prompt (above).
6. units_data.py's header comments are stale ("Eighteen core units in four parts"; the syllabus has an opening and three parts; "not yet in the repo"). Left byte-identical, as instructed.
7. syllabus.md's preamble ("**Not in the repo.**") and §10 ("Not checked: whether the six coined names collide…") are now out of date in `docs/supply-chain-execution-syllabus.md`; left as the design chat's record.
8. bibliography.md: R1, R3 and R4 are given at trade-press addresses (mmh.com, dcvelocity.com, supplychain247.com) and A6 at a stock-news page (webull.com). Part 8 bars press rewrites as sources; the writer must reach the issuing body's page. B5's handbook title is marked as from memory. The file says so already; nothing changed.
9. syllabus.md §1/§2 say four public courses; `docs/public-courses.md` called the SP track "Coaching (new)" (stale since S-SPORTS); not changed, not this row's.

## Found wrong in the repo, not fixed

- `docs/BACKLOG.md` §4c: about 130 lines (roughly lines 60 to 190) after the empty table header are orphaned prompt text (two whole writing prompts with no row cell), left by earlier closes. Not touched; `save()` and the 4d rows are unaffected.
- `docs/method.md` §8 named the site-log area "Coaching" (renamed Sports on 19 Nov 2026); corrected while adding Supply Chain.

## Left undone

- Product names of the employer in the private-terms list (none in the repo; see (e)). Carried by row P-SCE11 of `docs/BACKLOG.md` (*proposed*, for Pedro, by hand; added by the registration check, finding 1): until Pedro supplies them, the course is gated only on the employer's own name.
- No screenshots taken (main chat's step 4); built HTML checked by script only.
- No commit, push, publish or Project write (the main chat's).
