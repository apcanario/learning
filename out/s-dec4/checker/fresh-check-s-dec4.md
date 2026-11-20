# Fresh check of row S-DEC4 (verify by scope; course names out of the checks)

Checker: fresh Opus 5.5 (claude-opus-5-5), 20 Nov 2026. I had not seen the S-DEC4 work. I edited nothing in the repo and committed or pushed nothing. Every build and check ran in the probe copy `/tmp/s-dec4-check` (a `cp -r` of the main tree at `bd28d34`). The only file written in the repo is this report. Inputs: `git diff 6cde485 HEAD`, `docs/decoupling.md` §5, §6 and §8, the packets `out/s-dec4/packets/0[0-5]-*.md` and the agents' reports `out/s-dec4/0[1-4]-*.md`. I read the reports after forming my own view of the diff.

**Verdict: PASS WITH FIXES.** 2 errors, 5 should-fixes, 6 minors. The code does what the row asks. The output is byte-identical apart from the two expected files. marketing-ai passes `verify.py --edition` in full, and the scoped run catches a broken unit without writing the record. The errors are (E1) a What's new check that is weaker on the greece edition and has no lower bound on small editions, and (E2) docs and backlog rows the row has made false, which send the next chat to a list that no longer exists.

## Check results (last lines)

| # | Command (probe copy) | Result | Wall |
|---|---|---|---|
| 1 | `python3 kit/baseline.py --check` | `academy: 457 files, 0 differ` / `greece: 82 files, 0 differ` / `baseline: clean` | 2 m 42 s |
| 1 | `git diff 6cde485 --numstat -- kit/baseline.json` | `2 2 kit/baseline.json`: exactly the two hashes, `academy/greece/built.html` and `academy/rome/built.html` | n/a |
| 1 | `git diff 6cde485 -- kit/academy/` | only those two files; each differs by the one added `kit/provenance.json` link in the footer hnote | n/a |
| 1 | `baseline.py --chek` / `--check extra` | usage line, exit 1, `kit/baseline.json` untouched | instant |
| 5 | `python3 kit/build.py --edition marketing-ai` then `python3 kit/verify.py --edition marketing-ai` | first line `full: no passed run recorded for edition marketing-ai (verify-hashes.json)`; `verify-hashes.json: edition marketing-ai recorded, 42 pages` / `ALL CHECKS PASSED` | 23 s + 5 m 59 s |
| 3 | PB2's first figure block given an undocumented key `"colour"`, marketing-ai rebuilt, `verify.py --edition marketing-ai` | first line `scoped: 1 unit (read-pb2), 7 course pages (...) + home; 10 of 42 pages checked (home, new always), and the edition-wide checks`; 1 FAIL (`figure keys: ... figure.colour: not a documented key of matrix`); `verify-hashes.json: not written`; record byte-identical to before (`cmp`) | 2 m 55 s |
| 3 | `verify_scope.Scope` built against a record of `garbage{`, empty, `[1,2]`, `{"marketing-ai": "x"}` and `{"marketing-ai": {"pages": {}}}` | the first two: `full: no passed run recorded ...`; the last three: crash (`AttributeError`, `KeyError 'global'`) (S1) | n/a |
| 6 | `python3 kit/private_terms.py --edition marketing-ai` | `36 files, 0 private terms, 39 warnings: OK` | 1 s |
| 6 | `cd kit && python3 private_terms.py` | `125 files, 0 private terms, 114 warnings: OK` | 1 s |
| main tree | `git status --short` | clean (this report is the only file I wrote) | n/a |

I did not rerun the 25-minute full academy runs. Agent 3's timings (full 24 m 54 s; scoped one-unit filing 4 m 53 s; theme change full 24 m 36 s; `--full` 24 m 35 s; greece scoped 143 s against 342 s; marketing-ai scoped 182 s against 361 s) fit the code and my marketing-ai runs.

## 1 · Byte identity

Clean. The manifest change since 6cde485 is exactly the two expected hashes. No finding.

## 2 · Course names

`kit/verify.py`, scanned by token with comments and docstrings left out, against every course id, short name, sub-course short name and prefix, plus `Greek|Roman|ROME|GREECE|BRAND|m23|m55|rm\d|ux-ia|brand-[ab]|briefs-[ab]|b-a2|b-b3|Mythology`: no course name remains in code. What is left is generic: `brand(...)` (the brand API); the word "mythos/logos" in two messages about the home's History block (lines 2759 and 2760); and the track id `'history'` at line 998 (M1).

Other kit files the row touched:
- `verify_scope.py`, `howbuilt.py` and `courses.py`: none.
- `baseline.py`: `EDITION_NAMES = ('academy', 'greece')`, a recorded decision.
- `private_terms.py`: `PUBLIC` lists four course ids. This predates the row; see M2.
- `build.py`: the row's line is clean. Lines 1060 to 1075 still hold the history track's copy (M1, from before the row).

## 3 · Scope logic

How each source kind reaches the scope. A page's hash covers its built section and its fetched file (`data-src`). A unit page's hash also covers its unit file and its briefs entry; a course page's covers every file under `courses/<id>/`. Every panel in the academy shell maps to a page: 232 unit, 55 course, 5 site. The only unit page without a unit file of its own, `read-audience-growth`, is hashed as a course page. Every site file is the `data-src` of a panel. Nothing fetched is left unhashed.

| Source | Effect | Right? |
|---|---|---|
| unit md (front matter, body) | its reading or report page (unit file) and every course page of its course (course digest); neighbours' pagers through their output; home and What's new always | yes (wider than needed: M3) |
| briefs.md entry | the unit page (`brief_entry`) and every course page (digest) | yes |
| course.toml, pages/, notes/, inputs/ (history syllabus and prompts HTML/JSON), bibliography/ | every course page (digest); unit pages only where their output changes | yes |
| edition and brand toml, catalog.toml | GLOBAL: full run | yes |
| design/theme.css, kit/shell.js, kit/shell.css, kit/fonts/**, kit/*.py (verify.py and verify_scope.py included) | GLOBAL: full run | yes |
| history HTML in kit, kit/provenance.json, kit/reviews/, kit/audits/, docs rendered into pages (method.md, sourcing-standard.md) | the pages whose output they reach (output hash) | yes |
| docs/courses-index.md | `index_check`, edition-wide, every run | yes |
| docs/site-log.md | backlog and changelog pages, always checked | yes |
| kit/private-terms.txt | private terms, edition-wide, every run | yes |
| design/outlines/ (library and uses.json) | library and mapping checked whole every run; a relief reaches its page's output | yes |
| the drawers (shell outside the panels, about 195 KB) | root drawer always; in a scoped run, the drawer of each course a changed page is in. Only a course-folder change can alter a course drawer, and that puts the course home in scope | yes |
| tool versions (Python markdown, Playwright, Chromium) | not hashed | M4 |

The record:
- It is written only after ALL CHECKS PASSED (`fails` empty, at the end of `main()`). An exception before that point writes nothing. Proved: a failed scoped run left the record byte-identical.
- It is kept per edition (`{edition: {global, pages}}`), and each run reads and writes only its own key.
- A missing or unparseable record gives a full run. A record that is valid JSON but has the wrong shape crashes the run instead (S1). The crash is loud, not a silent pass.
- `--full` ignores the record.
- The first line is the mode, printed at import before any check, and it is repeated above the last line.
- A failing check cannot be skipped through the record. A page leaves the scope only when its hash equals the hash recorded after a full pass. A failed run records nothing, so the same pages come back next time.
- `--page` and `--shots` change only the screenshots, never the record.

## 4 · Rules kept

- The hero contour budget of 20 KB is unchanged (verify.py lines 640 and 894; build.py `HERO_INTERVAL` untouched).
- What's new's 10 to 25 levels is unchanged for academy (`FULL`, `courses = "all"`).
- The greece edition's What's new check is weaker (E1).
- The other changes are equivalent or stricter: the New since heading (no crash below six rows, same check at six or more); split anchors `b-b3` → `b-b2` (same kind of check); desktop fonts from the theme tokens (same three for academy); the motion performance loop now fails when it measures nothing.

## 5 · Editions without Greece

On marketing-ai each former Greece assumption now checks something real:

| Former assumption | On marketing-ai now |
|---|---|
| `check_split` | runs `check_split_md` on personal-brand-pb: stubs, one fetch each, prefetch, pager, deep link into unopened briefs, failed fetch and retry, failed course-home fetch and retry |
| phone navigation | the markdown course steps |
| tablet `TAB` | the markdown home's `.cgrid` |
| desktop `#m23` | `read-pb1` (measure 744 px, sidebar highlight) |
| `rp` fallback | the first reading page visited |
| root drawer groups | derived from the visited tracks: Marketing open, Technology closed |
| motion performance loop | measures `personal-brand-pb` |
| fonts | names the unvendored Source Serif 4 |

Each left-out part prints its reason: split (no history course of LEAD's structure), nav (LEAD steps, drawer accordion), desktop (mythos/logos block, unserved font), What's new (scale line), private terms (an edition holding a private course).

Silent:
- The second-history-course navigation steps (`if SECOND:`, line 2541) and the LEAD and SECOND drawers are skipped without a line on an edition that lacks them (S5).
- The How it was built loop is empty when there is no history course. That is correct: nothing to check.
- The P92 desktop tiles take only markdown tiles. Still a real check.

Crash path: an edition with no LEAD and no markdown course with a unit filed fails with an IndexError at line 2682 (`MDSUBS[0][0]`); `rp` and `DESK` are then None (S5).

## 6 · Private terms

None. marketing-ai: 36 files, 0 private terms (by `private_terms.py --edition` and inside `verify.py`). Academy, no argument: 125 files, 0.

## 7 · Docs made false or incomplete

This is listed under E2 and S2/S3 below. Note: the packet's "kit/README.md 'Known limits'" is in the root `README.md`, line 43.

---

## Findings

### Errors

**E1 · What's new: the greece edition lost the 10 to 25 rule, and small editions have no lower bound.** `kit/verify.py` line 908.
- The range is applied only where `FULL` (academy). The greece edition (1 of 8 courses) meets the range: its largest day is 221,673 words, 20 levels. Before the row it was held to the range. Now it is held only to `levels == words // NEW_INTERVAL` and at most 25. That is a check weakened on an edition whose output satisfies the rule.
- The fallback has no lower bound. A What's new whose largest day stands 0 levels, a flat layer (the template test's fieldnotes: 1,170 words), passes because the drawing matches the formula, not because the layer is legible. It does print one line, but it passes for the wrong reason.
- Fix: keep the range wherever the build's scale can reach it, and say so where it cannot. Replace lines 908 to 915 with:

```python
                    if FULL or top[1] >= 10 * NEW_INTERVAL:   # the range Academy's filings set (P93); S-DEC4: any edition whose largest day can reach 10 levels at the build's scale is held to it
                        if not 10 <= top[2] <= 25: fails.append(f'{pid} {label}: its largest day ({top[0]}) stands {top[2]} levels, not 10 to 25')
                    else:
                        if top[2] != int(top[1] // NEW_INTERVAL) or top[2] > 25: fails.append(f'{pid} {label}: its largest day ({top[0]}, {top[1]} words) stands {top[2]} levels, not {int(top[1] // NEW_INTERVAL)} (a level every {NEW_INTERVAL} words, build.py NEW_INTERVAL) at most 25')
                        if not _NEW_SAID:
                            _NEW_SAID.append(1)
                            print(f"What's new: edition {EDITION}'s largest day ({top[0]}, {top[1]:,} words) is under {10 * NEW_INTERVAL:,} words, so the build's scale ({NEW_INTERVAL:,} words a level) cannot raise it to 10 levels; it is checked against that scale, "
                                  f"{int(top[1] // NEW_INTERVAL)} levels, at most 25; the 10 to 25 range is left out here" + (' (it stands 0 levels: no rise is drawn)' if top[2] == 0 else ''))
```

- Also, in `docs/decoupling.md` §6 (S-DEC4 notes), record that an edition below 110,000 words on its largest day is held only to the scale. A 0-level What's new is accepted there by design, or is proposed as a build change (a per-edition `NEW_INTERVAL`). Do not let the code decide this silently.
- Re-run `verify.py --edition greece` after the change (expected: passes, 20 levels in range).

**E2 · Instructions the row made false: the next chat would edit a list that is gone.**
1. `skills/new-course/SKILL.md` line 39 (step 5b): "add the course to `TEXTS` in `kit/p95_library.py` (its vault folder), to `REL_COURSES` in `kit/verify.py`, to `NAMES` in `kit/p96_uses.py`" → "add the course to `TEXTS` in `kit/p95_library.py` (its vault folder), set `reliefs = true` in its `course.toml` (S-DEC4: `verify.py` reads it; `REL_COURSES` is no longer typed), add it to `NAMES` in `kit/p96_uses.py`". The p9x lists stay until P-DEC9. Re-save the skill to the account (§8 risk).
2. `docs/BACKLOG.md` line 405 (G-R-SP) and line 409 (G-R-SCE): "`REL_COURSES` in `kit/verify.py`" → "`reliefs = true` in `courses/<id>/course.toml` (S-DEC4)", in both rows.
3. `README.md` (root) line 43, "Known limits (S-DEC5)". The statement "`verify.py --edition <name>` stops on any edition without Greece until S-DEC4" is now false. Replace the line with: "Known limits (S-DEC4): `verify.py --edition <name>` runs on any edition (marketing-ai and greece pass); a new course also needs its section in `docs/courses-index.md` (`index_check`), and a course of two short units fails the desktop motion check (P-DEC11). The Figure kinds page and the "How it was built" page still carry a few sentences about this repo's own history (Rome examples, the closed Fable stage; P-DEC8), engine text that names no brand and no private term."

### Should-fix

**S1 · A record of the wrong shape crashes the run instead of falling back to full, and an unreadable one is reported as "no passed run recorded".** `kit/verify_scope.py` lines 123 and 151 to 155. The packet asks that a corrupt record fall back to full. Replace `_load` and the line `rec = self._load().get(edition)` with:

```python
        st = self._load()
        rec = st.get(edition) if isinstance(st, dict) else None
        bad = rec is not None and not (isinstance(rec, dict) and isinstance(rec.get('global'), dict) and isinstance(rec.get('pages'), dict))
        if bad: rec = None
```

```python
    def _load(self):
        try:
            st = json.loads(self.state_path.read_text())
        except FileNotFoundError:
            return {}
        except ValueError:
            self.unreadable = True
            return {}
        return st if isinstance(st, dict) else {}
```

Add `self.unreadable = False` before the first `_load()`. The mode for the no-record branch then reads `f'full: {state.name} unreadable or malformed for edition {edition}'` when `self.unreadable or bad`, else as now.

**S2 · `kit/README.md` does not describe the new behaviour.**
- The `verify.py` row (line 101) says nothing of scope, `--full` or the record. Add after its first sentence: "Since S-DEC4 (20 Nov 2026) it checks by scope (`verify_scope.py`): the default run checks the pages whose sources changed since the edition's last passed run, recorded in `kit/verify-hashes.json` (committed), plus the home, What's new, the Changelog, the Backlog and every edition-wide check; a change to `kit/*.py`, `shell.js`, `shell.css`, `design/theme.css`, `kit/fonts/`, `catalog.toml` or the edition's or brand's file, a first run and `--full` check everything; its first line says which and why; the record is written only after ALL CHECKS PASSED."
- The file table has no row for `verify_scope.py` or `verify-hashes.json`.
- Line 148, "(the outline library's lists, `new-course` step 5b, are still typed in `kit/`)", should read "(the relief tools' lists `TEXTS`, `NAMES`, `TONE`/`NAME`, `new-course` step 5b, are still typed in `kit/`, P-DEC9; `verify.py`'s is course.toml `reliefs`)".
- Prose only. Rehash that one baseline entry after showing it is the sole change, as S-DEC1 did.

**S3 · The filing procedure does not say the record is committed.**
- `docs/method.md` §7, line 194: "6. **Commit and push.** The session ends with one commit naming the unit." → "6. **Commit and push.** The session ends with one commit naming the unit, `kit/verify-hashes.json` included (the record `verify.py` writes after ALL CHECKS PASSED, S-DEC4; without it the next chat's first run is a full one)."
- `skills/file-unit/SKILL.md` line 32 (history step 7) and line 51 (markdown step 1): after "`python3 verify.py`" add "(scoped by default: its first line says which pages it checks and why; a kit, theme, brand, edition or catalog change makes it a full run by itself; `--full` forces one; commit `kit/verify-hashes.json` with the filing)".
- `docs/decoupling.md`:
  - §6 needs its "Notes on the rows from S-DEC4", including the edition results (marketing-ai and greece ALL CHECKS PASSED; fieldnotes runs through with 12 content or build findings), the What's new decision (E1), the `private`, `reliefs` and `verify_sample` keys, and the scope reading of M3.
  - §8 first bullet: "names courses in 67 lines … should not move until S-DEC4" → "named courses in 65 lines until S-DEC4, which moved them to course.toml keys and the edition's own courses (0 in code)".
- Root `README.md` line 40: add the `--edition <name>` form of `private_terms.py`.

**S4 · `kit/verify-hashes.json` does not exist in the tree.** The design rests on the record being committed (`verify_scope.py` docstring, 03-scope.md), but no run in the main tree has written it. Until the main chat runs `cd kit && python3 verify.py --full` at the final HEAD and commits the record, the first unit chat after S-DEC4 runs a full 25-minute verify.
- The done-when's timings are proved, in a probe copy.
- Edits after that run do not stale the record dangerously: edits to `docs/site-log.md` or `docs/courses-index.md` only bring the always pages back into scope.

**S5 · Silent skips and a crash path in the passes.**
- `kit/verify.py` line 2541, `if SECOND:`: on an edition without a second history course (greece, marketing-ai) the second-course navigation steps are skipped with no line, unlike every other left-out step. Add `else: print('nav: no second history course with a report 1.2 in this edition; its course home, report, next, last and resume steps are left out')`.
- Lines 2681 to 2684: on an edition with no LEAD and no markdown course with a unit filed (a new history course with only a few reports, or a markdown course before its first filing), `MDSUBS[0][0]` raises IndexError, and `rp` and `DESK` are None.
- Guard: before line 2681, `if not (SECOND or LEAD or MDSUBS): fails.append('tablet and desktop: the edition holds no history course with reports 2.3 to 5.5 and no markdown course with a unit filed; their report checks have no page to open')`. Then make the tablet report read and the desktop `DESK` block conditional on `rp`/`DESK` not being None. It should fail with a reason, never crash and never pass.

### Minor

**M1 · A track id and a track's copy are still in the engine (from before the row).**
- `kit/verify.py` line 998 (`NEXT if t['id'] == 'history'`) and `kit/build.py` lines 1060 to 1075: the History track's "Why history and myth together" copy (mythos/logos, Herodotus, Thucydides) and its planned-courses note, typed in `build.py` and keyed by the track id.
- §1 says "kit/ knows no course and no brand by name". This is a track, not a course, and it is not in the row's 67 lines.
- Proposed row: move the copy to a track page (`catalog.toml` `[[tracks]]` `extra = "pages/…md"`) and `next` to the History track's `planned`, with academy byte-identical.

**M2 · `private_terms.PUBLIC` duplicates the course.toml `private` key.** `verify.py` fails a course that is both, but not a course that is neither. A new course outside `PUBLIC` is therefore never checked by the default run, even though verify treats it as public in other editions. Derive `PUBLIC` as the courses without `private = true`. Academy output is unchanged: the four courses not marked private are exactly today's `PUBLIC`.

**M3 · The scope is wider than the done-when's words.** "A one-unit filing verifies only that unit's pages plus the home" became the unit page, all 7 pages of its course and the four always pages, because a course page hashes its whole folder. This is safe (more, never fewer) and recorded by agent 3. Record the reading in decoupling §6. Related: the full run checks the drawers of the navigation's sample courses only, while a scoped run checks the drawer of any changed course. If that check is valid for every course, the full run should cover every course's drawer (cheap).

**M4 · Tool versions are not hashed.** An upgrade of Playwright, Chromium or the Python markdown package does not force a full run. Add one sentence to the `verify_scope.py` docstring and the README row: "run `--full` after a tool upgrade".

**M5 · Private terms on an edition holding a private course.** The edition's files are all left out, including any public course it also holds. The greece edition no longer runs the academy public-course check it used to run (that check is covered by the default run). Acceptable today because no mixed edition exists. When one does, scan the edition's pages outside the private courses' folders.

**M6 · Unchanged.** The 200 px landing bound on a short briefs page and the two-unit motion failure (fieldnotes) are already proposed as P-DEC11. Agent 1's P-DEC7 (M5) was done by packet 4: drop P-DEC7 from the proposed rows, or mark it done.

## What the agents' reports add after my own reading

- They agree with the diff.
- Agent 4's report gives the rome built.html hashes as `c280859a…` → `18d7de1f…`. The truncated diff I read showed only greece's pair; numstat confirms two changed lines, consistent.
- Agent 2's academy full run (25 m 10 s, ALL CHECKS PASSED) was taken before packet 3 and packet 4's changes. Packet 3's probe re-ran academy full after scope (24 m 54 s). No full academy run exists at the final HEAD (after M5), which is S4's run.
