# S-DEC4 packet 1 · engine course ids and the baseline guard (corrections 3 and 4)

Agent: fresh Opus 5.5 (claude-opus-5-5), 20 Nov 2026. Nothing committed, pushed or published.

**Verdict: done.** academy and greece byte-identical after every step; marketing-ai unchanged; `private_terms.py` OK.

## Checks (last lines)

| When | Command | Result | Time |
|---|---|---|---|
| Before any change | `python3 kit/baseline.py --check` | `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` | 2 m 39 s |
| After step 1 (+ courses.py docstring) | `python3 kit/baseline.py --check` | `baseline: clean` (457 / 82, 0 differ) | 2 m 43 s |
| Step 2 guard | `baseline.py --chek`, `--check x`, `-h`, `--edition` | each prints the usage line, exit 1, no build, `kit/baseline.json` untouched (`git status` clean for it) | instant |
| Step 3 | `python3 kit/build.py --edition marketing-ai` before and after, `diff -r` | `marketing-ai: no diff` (36 files, 3.98 MB, built in 20 s) | 20 s each |
| Step 5 | `cd kit && python3 private_terms.py` before and after, outputs compared with `cmp` | identical; `125 files, 0 private terms, 114 warnings: OK` | ~1 s |
| End | `python3 kit/baseline.py --check` | `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` | 2 m 44 s |

No expected differences were listed: none arose. `verify.py` not run (packet 2 owns it).

## Files changed

- `kit/build.py` (1 line), `kit/howbuilt.py` (1 line), `courses/greece/course.toml` (+2), `courses/rome/course.toml` (+1), `kit/courses.py` (docstring +5), `kit/baseline.py` (+12, −1), `kit/private_terms.py` (+39, −2).
- Not changed: `kit/README.md` (no prose it holds was made false; no rehash), `kit/pack.py`, `kit/verify.py`.

## 1 · Course ids out of the engine (M6)

- `build.py` `drawer()`: `dkey = u if c['id'] == 'greece' else f'{c["id"]}:{u}'` became `dkey = c.get('unit_key', '{id}:{unit}').format(id=c['id'], unit=u)`. `courses/greece/course.toml` sets `unit_key = "{unit}"` (its legacy localStorage key); rome and any new history course take the default `"{id}:{unit}"`.
- `howbuilt.py` history page: `word = {'greece': r'\bGree(k|ce)\b', 'rome': r'\bRom(e|an)\b'}.get(cid, re.escape(c['short']))` became `word = c.get('notes_match') or re.escape(c['short'])`. greece sets `notes_match = '\bGree(k|ce)\b'`, rome `notes_match = '\bRom(e|an)\b'` (TOML literal strings, so the backslashes are the regex's). Absent: the escaped `short`, as before.
- Decision: the keys sit after `family_label` with a comment each; the loader passes unknown keys through unchanged, so no `kit/courses.py` code change, only its docstring (a paragraph "Optional history-course keys"). Checked: the dicts load with `{unit}` intact (no placeholder fill touches it).

## 2 · baseline.py guard

- `if sys.argv[1:] not in ([], ['--check']): raise SystemExit(USAGE)` before anything builds. `USAGE = 'usage: python3 kit/baseline.py [--check]   (no argument: rebuild and re-record kit/baseline.json; --check: compare)'`. No argument still re-records exactly as before (same code path; not run, since it would rewrite the manifest).
- Edition names: kept as `EDITION_NAMES = ('academy', 'greece')`. Decision: the manifest is this repo's refactor guard, not a per-edition check; taking every edition from `editions/` would add marketing-ai to the manifest and change what `--check` compares. The docstring now says so, and that another edition is compared by building before and after and diffing (as done here for marketing-ai).

## 3 · Engine history text per edition: decision, keep

Measured in marketing-ai: `viz-examples.html` has 10 lines naming Rome (11 mentions per the packet); `personal-brand-pb/built.html` and `building-with-ai-bw/built.html` carry "the audits run before the Fable stage closed (S-NOAUDIT, 15 Nov 2026)". (Other Fable mentions there are course content: unit front matter and the BW case study.)

Decision: keep both; no build change. Reasons:
- **Figure kinds page.** The Rome/Greek module citations are the provenance of each hard case (why the case exists), beside P-row numbers (P55, P58, P84) that are the same kind of repo history; stripping only the module citations per edition would leave the P-rows and make the engine's reference text depend on which courses an edition holds, for no reader gain. An edition that wants none of it already has the switch: `omit = ["figures"]` drops the page and its home button (`build.py` lines 950 and 1247; greece uses it).
- **S-NOAUDIT clause.** It describes the course's own data (the AUDIT_LOG), not the edition: PB's page in marketing-ai shows the same course and the clause is true there. The right fix is data-driven (drop the clause where the course's `[[pack.audit_log]]` is empty), but that changes academy's BW, SP, SCE and UX `built.html` pages (only brand-ai and personal-brand have audit_log rows), so it breaks the hard limit. An edition-keyed condition would be a kludge. Proposed as a row below (P-DEC8).
- marketing-ai built before and after: `diff -r` empty. Note: the "before" build was taken after step 1 (step 1 touches only history courses' drawer and history How it was built pages, none of which marketing-ai holds).

## 4 · M5 footer link: not done, proposed row

Correction to the packet's premise: the change does **not** touch the greece edition. greece omits `build` (`editions/greece.toml`), so it has no `built.html`; `grep -rl provenance.json kit/editions/greece` finds nothing. Only academy's `greece/built.html` and `rome/built.html` change.

Paste-ready for `docs/BACKLOG.md` Proposed:

```
| P-DEC7 | *Proposed (S-DEC4, chat-3 checker M5).* The history 'How it was built' footer (`kit/howbuilt.py`, the `footer([...])` call of the history page, line 357) links the course's own `courses/<id>/inputs/provenance.json` but not `kit/provenance.json`, which supplies the page's review notes and the kit-wide artefacts: add `gh('kit/provenance.json', 'kit/provenance.json')` after the course's file (a distinct link text: both files are named provenance.json). Expected differences: academy `greece/built.html` and `rome/built.html`, each by that one link only; the greece edition omits `build`, so none of its 82 files changes. Show the diff is only that, then re-record `kit/baseline.json`; the next Academy publish (artifact, then Pages) carries it. ⚠ Academy output changes (2 files); no greece artifact republish. | Chat-3 fresh check M5, left by S-DEC4 packet 1 (it changes academy output) | Any chat after S-DEC4 |
| P-DEC8 | *Proposed (S-DEC4).* The markdown 'How it was built' page (`kit/howbuilt.py`, the hnote above the units table, line 477) says "audits are the data file's AUDIT_LOG, the record of the audits run before the Fable stage closed (S-NOAUDIT, 15 Nov 2026)" on every markdown course, also where the course's `[[pack.audit_log]]` is empty, and so in any new or template course. Drop that clause where the course has no audit_log rows. Expected differences: academy `building-with-ai-bw/built.html`, `sport-psychology-*/built.html`, `supply-chain-execution-*/built.html`, `ux*/built.html` (the courses without audit_log rows; list the exact files from the diff), each by that clause only; brand-ai and personal-brand unchanged; greece edition unchanged (no markdown course). marketing-ai's BW page changes the same way. ⚠ Academy output changes; re-record the manifest after the diff is shown to be only that. | S-DEC4 packet 1, step 3 decision | Any chat after S-DEC4 |
```

## 5 · private_terms.py

- Explicit file arguments were already accepted (`python3 kit/private_terms.py <file>...`); the manual form works: `python3 kit/private_terms.py $(find kit/editions/marketing-ai -type f)` → `36 files, 0 private terms, 39 warnings: OK`.
- Added: `--edition <name>` (every file of `kit/<site>/` from `editions/<name>.toml`, `built.html` included) and the function `edition_files(name)` for packet 2's `verify.py --edition`; an unknown or unbuilt edition stops with a message; `--edition` without a name prints a usage line. With explicit files, a file that is not UTF-8 text is named and skipped (`text_only`), so a future edition with images does not crash the manual form. Docstring updated: the no-argument run is academy's (`PUBLIC`, the `kit/academy` glob).
- No-argument behaviour byte-for-byte: stdout compared with `cmp` before and after, identical; `check()` unchanged (0 hits).
- Results: `--edition marketing-ai` → `36 files, 0 private terms, 39 warnings: OK`. `--edition greece` → `82 files, 31 private terms, 574 warnings` (exit 1). ⚠ For packet 2: greece is a private edition (Pedro's own course) and is expected to name him; a `verify.py --edition` private-terms check should run only on an edition holding public courses (or only on its public courses' pages), else greece fails it.

## Notes for the main chat

- `README.md` line 40 (root, not in this packet's files) documents the `<files>` form; still true, `--edition` not mentioned there.
- marketing-ai build output lives in `kit/editions/marketing-ai/` (git-ignored); rebuilt by this packet, same bytes as before.
