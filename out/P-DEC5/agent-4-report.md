# P-DEC5 · agent 4 (packet 4, rebase onto upstream) report

Model: Opus 5.5 (`claude-opus-5-5`). 21 Nov 2026. Commits are on local `main` only. Nothing pushed, and `kit/land.py` not run.

## Verdict

**Ready to land.** The four P-DEC5 commits are replayed onto `origin/main` f660526 (DEC-C landed) with `git rebase --onto origin/main e855c10 main`, and no upstream commit was replayed. Both sides' intent is kept:
- **Baseline:** `baseline.py --check` against upstream's manifest differs in `academy: changed README.md` only. That is our `kit/README.md` prose.
- **Probe:** Source Sans 3 and IBM Plex Mono: ALL CHECKS PASSED.
- **Real brand:** ALL CHECKS PASSED.

Local `main` is upstream plus these commits:

| Commit | What |
|---|---|
| 60a3f9b | agent 1: metrics, brand faces |
| b25bec6 | agent 2: 68ch floor, `course_topo`. The rebase adds the P-DEC11 composition (below) |
| cdd13ac | checker findings |
| 8f9bd24 | close: proposals renumbered, CHANGELOG, prompt re-saved |
| (two more) | the land `--expected` file and this packet's records, then the decoupling note and this report |

## Conflicts and how each was resolved

1. **`kit/build.py`** (commit 2): a textual conflict. Upstream's P-DEC15 `new_interval()` and our lede/`course_topo` block were added at the same place. Both are kept.
   - **The semantic overlap with P-DEC11:** upstream added `small=(2, view)` to `COURSE_TOPO`'s wide layout, used by `ct_fit` for a hero of one or two rises. Our `course_topo` drew in only `box` and `view`, so for a brand whose face adds lede lines, P-DEC11's band would have kept the full DM Sans width.
   - **Fixed in the engine:** `course_topo` now draws `small`'s view in by the same ratio `k` (docstring updated). In DM Sans' metrics it still returns `COURSE_TOPO` itself, so the output is byte-identical.
   - **Tested:** `out/P-DEC5/topo_test.py` gives `out/P-DEC5/topo-compose-test.txt`. In the probe brand, a 2-extra-line lede gives a wide view of (.0824, .1, .9176, .84) and a small view of (.0824, .17, .9176, .76). In the real brand the result is the same object as `COURSE_TOPO`.
   - The probe's courses (PB 12 rises, BW 13) do not reach the small path in a browser.
2. **`kit/baseline.json` and `kit/verify-hashes.json`** (commits 2 to 4): upstream's versions taken. No hash was edited by hand. Both files equal `origin/main` at HEAD.
3. **`docs/BACKLOG.md`** (commit 4): upstream's rows kept exactly.
   - **Removed:** the Proposed P-DEC5 row (unchanged upstream since our start).
   - **P-DEC16:** our text change kept (upstream had not touched the row).
   - **Renumbered:** our two proposals became **P-DEC22** (mono line box: `mono_ascent` and `mono_descent`) and **P-DEC23** (the metrics generator moved into `kit/`). They sit after upstream's P-DEC21 in Carried proposals.
   - **Kept from upstream:** "Next up".
   - **W-DD-SP3 prompt:** `next_prompt.py --row W-DD-SP3` on the merged tree (with `--save`, in a /tmp copy) differed from upstream's saved cell only by the two added bullets P-DEC22 and P-DEC23, so it was saved.
4. **`docs/CHANGELOG.md`** (commit 4): our P-DEC5 row is placed above DEC-C's row, and every upstream row is kept. The row adds this agent to the model column and adds the post-rebase probe and the P-DEC11 composition to the result.
5. **Auto-merged without conflict:** `docs/decoupling.md`, `kit/verify.py`, `kit/README.md`, `kit/courses.py`, `kit/viz.py`.
   - **Preservation:** a script compared every upstream line added since e855c10 in the 10 non-`out/` text files of the row against HEAD: 0 missing.
   - **One sentence added to `docs/decoupling.md` §6** (Notes on P-DEC5): the composition with P-DEC11. `docs/` is not a build input.
6. **Commit messages:** commit 4's message was amended to say P-DEC22/23 and to record the build.py composition. The message of b25bec6 is unchanged from the original (it predates the composition).

## Tests

| Test | Result | Output |
|---|---|---|
| `python3 kit/baseline.py --check` (main tree, after the rebase) | `academy: changed README.md`; academy 457 files, 1 differ; greece 82, 0 differ | `out/P-DEC5/baseline-check-4.txt` |
| Probe: copy of the clone at `/tmp/pdec5r/probe`, `brands/workbench.toml` = `/tmp/wb-probe.toml` (Source Sans 3 / IBM Plex Mono, `[metrics]`, matching `fonts_href`); `python3 kit/build.py --edition marketing-ai`; `cd kit && python3 verify.py --edition marketing-ai` | **ALL CHECKS PASSED**, 0 FAIL, 5 m 43 s, figure geometry included | `out/P-DEC5/probe-verify-run4.txt` |
| Real brand, main tree: same build and verify | **ALL CHECKS PASSED**, 0 FAIL, 5 m 38 s | `out/P-DEC5/real-verify-run4.txt` |

- **Baseline:** the only differing file is the build copy of `kit/README.md`, which our row changes on purpose (the `[metrics]` entry). Nothing else differs.
- **Probe:** P-DEC11's band does not break our topo change. No engine fix was needed beyond the composition above.
- **Real brand:** afterwards `git checkout origin/main -- kit/verify-hashes.json`, so land.py records its own.
- **Not run:** `verify.py --full` (land.py runs it).

## Land command

DEC-C's precedent: `--expected FILE` with one entry per line (52f4e5a, cf5d0de). land.py matches the expected path against the path field of `baseline.py --check`, which here is `README.md`. A bare `academy/README.md` would not match, so the file gives the whole check line (`academy: changed README.md`), which `norm_out` maps to that path, and the repo-relative form as well.

- **No `drop:` lines are needed:**
  - The removed P-DEC5 row predates our start.
  - No upstream line added since the start is missing from HEAD.
- **The file:** `out/P-DEC5/land-expected.txt` is committed.

```
python3 kit/land.py land P-DEC5 --expected out/P-DEC5/land-expected.txt
```

## Files

- **Changed by the row:** `brands/academy.toml`, `brands/workbench.toml` (comment), `docs/BACKLOG.md`, `docs/CHANGELOG.md`, `docs/decoupling.md`, `kit/README.md`, `kit/build.py`, `kit/courses.py`, `kit/verify.py`, `kit/viz.py`, `kit/fonts/` (added files only), and `out/P-DEC5/`.
- **New in `out/P-DEC5/`:** `land-expected.txt`, `baseline-check-4.txt`, `probe-verify-run4.txt`, `real-verify-run4.txt`, `topo_test.py`, `topo-compose-test.txt`, this report. Also committed: `packet-4.md` and `land-notes.md`.
