# P-DEC21 notes (21 Nov 2026, Opus 5.5)

Row: the method table's "Audit cadence" row on every markdown course's How it was built page said "None since 15 Nov 2026 (S-NOAUDIT) ...", the closed Fable stage. Instruction: the row reads each course's own data (a course.toml key with a default for courses that have none), never the closed stage's sentence. Nothing committed, pushed, landed or published.

## Where the sentence came from

Not typed in the engine: `kit/howbuilt.py` `method_rows()` parses `docs/method.md` §1's table and `method_section()` prints, for a markdown course, the "Brand + AI" column and the "Common rule" column. The Audit cadence row's common-rule cell is the S-NOAUDIT sentence. History pages print the same cell (with the Personal Mythology column).

## Change

- `kit/pack.py`: `DEFAULTS` gains `AUDIT_CADENCE` = "No periodic audit. Every new unit gets a fresh check before filing, and a unit written with live search is re-checked for staleness six months after writing." The docstring's `[pack]` schema documents the key `audit_cadence` (a plain string key, so `load()` sets `AUDIT_CADENCE` as for any other; Markdown inline; set only where the course's cadence is not the default; the template names it in a comment, HK-1 M5). Table chosen: `[pack]`, because the value is course data read through `pack.load` with the existing DEFAULTS mechanism; `[howbuilt]` is a brand table.
- `kit/howbuilt.py`: `CADENCE_TOPIC = 'Audit cadence'`; `method_section(family, md_inline, cadence=None)` replaces the common-rule cell of that row with `cadence` when given; `markdown_page` passes `d.AUDIT_CADENCE`. History pages pass nothing, so their row is unchanged. Docstring source list gains the row.
- `courses/_template/course.toml`: a comment naming `[pack]` `audit_cadence` with a placeholder, the key left out (HK-1 M5: first pass copied the default text, against pack.py's rule that a key repeating DEFAULTS is left out). Parses with tomllib; courses.py still skips the folder.
- `kit/howbuilt.py` (HK-1 S2): when a cadence is given and `docs/method.md` §1 has no single `Audit cadence` row, the build stops with a message, instead of printing the closed stage's cell again.
- No course.toml sets the key: every markdown course's cadence today is the default. Checked: `docs/method.md` §1 prose (four-unit audit retired 15 Nov 2026), §5 (fresh check of every new unit before filing), §6 (staleness check six months after a search-on unit); each course's `pages/build-body.md` (brand-ai, personal-brand, building-with-ai, sport-psychology, supply-chain-execution, ux) states the same two checks; no live (non-changelog) course data names a running audit. UX's "Audit 3/4 at n of m" counters are changelog history (latest such row 10 Nov 2026).
- `docs/decoupling.md`: the S-DEC5 "For S-DEC4" bullet now says the markdown page's two S-NOAUDIT mentions were removed by P-DEC8 and P-DEC21 and a history row still names it; a "Notes on P-DEC21" block after P-DEC20's.
- `README.md` (root, Known limits): its sentence "the method table's Audit cadence row on every How it was built page names the closed Fable stage" was the old behaviour; now says a history course's row names it and a markdown course's is its own `audit_cadence`. Not in the caller's file list, but it is the line that described the old behaviour (same line P-DEC20 edited; P-DEC20's text kept).
- `kit/README.md`: not edited; it does not mention the old behaviour, and its size table is unchanged by this item.
- No CSS anywhere.

## Proof

`out/HK-1/p_dec21_prove.py` (start build `/tmp/start/academy` vs rebuilt `kit/academy`): no file added or removed; differing files: `index.html` (P-HERO1, P-DEC20) and seven `built.html`. For each `built.html`, replacing its single Audit cadence `<tr>` with a marker makes start and new identical.

Old row (all seven identical): Audit cadence | Every four written units, one claim per section per unit, more than one in ten FAIL → full audit | None since 15 Nov 2026 (S-NOAUDIT): the Fable stage is closed and the four-unit audit retired; the fresh check (§5) and the six-month staleness check (§6) stand. (From 28 Oct to 15 Nov 2026 the rule was a stratified-sample claim audit every four units written in a hub.)

New row (all seven identical): Audit cadence | Every four written units, one claim per section per unit, more than one in ten FAIL → full audit | No periodic audit. Every new unit gets a fresh check before filing, and a unit written with live search is re-checked for staleness six months after writing.

Files: brand-a, brand-b, building-with-ai-bw, personal-brand-pb, sport-psychology-sp, supply-chain-execution-sce, ux-ia (each `/built.html`). `greece/built.html`, `rome/built.html`: byte-identical to start.

Isolation from P-HERO1/P-DEC20: built the current tree twice, with `kit/pack.py` and `kit/howbuilt.py` at HEAD and with this item's versions (`/tmp/pdec21/without`, `/tmp/pdec21/with`): only the seven `built.html` differ; `index.html` identical, `kit/README.md` (size table) identical. A second build is byte-identical to the first.

Checks: `python3 kit/private_terms.py`: 129 files, 0 private terms, 114 warnings (none in a `built.html`), OK. `python3 kit/index_check.py`: courses-index.md matches the sources. `python3 kit/rot_check.py`: OK. `verify.py` not run.

## Fresh check

The default wording needs an Opus 5.5 fresh check in a separate context before filing (`docs/method.md` §5). This agent had no tool to start one; its own check is above (each clause against method.md §1, §5, §6 and every course's build-body.md). Owed by the caller.

## Left

- The row's middle cell ("Brand + AI before the merge": every four written units ... full audit) is still `docs/method.md`'s, under that column heading; it is the family's pre-merge practice, labelled as such, not a claim about the course.
- The table's hnote still says "From method.md §1"; the cadence cell is now the course's. Saying so would change a second line of every markdown `built.html`; left for a row if wanted.
- History courses' row still prints method.md's S-NOAUDIT cell (out of scope; history pages had to stay unchanged).
- If a brand's method doc has no "Audit cadence" topic, the course value is not shown (the row is only replaced, never added).
