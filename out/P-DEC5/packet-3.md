# Packet 3 · P-DEC5 fresh checker (fresh Opus 5.5 agent; has not seen the work)

Repo /home/claude/learning, `main`. You read and report; you never edit, commit or push. Write findings to `out/P-DEC5/checker-findings.md` (each: error / should-fix / minor, file:line, evidence, suggested exact fix); reply in six lines max (verdict, counts, model id).

## The row (P-DEC5, word for word)
Let a brand set `--sans` and `--mono`: give `kit/viz.py` the brand's font metrics and have `verify.py` serve the brand's faces; or document that those two faces are fixed. ⚠ Touches figure geometry: academy's figure boxes must stay byte-identical, so the metrics default to DM Sans and Space Mono. Today `brands/<name>.toml` changes `--serif` only.

## The test (docs/decoupling.md §5)
Academy and greece byte-identical to `kit/baseline.json` (`python3 kit/baseline.py --check`, ~3 min); `verify.py --full` ALL CHECKS PASSED at the end (chat runs it; you do not); in a probe copy a brand setting Source Sans 3 and IBM Plex Mono on marketing-ai passes `verify.py --edition marketing-ai`, figure geometry included (it failed 24 times before).

## The diff to check
`git diff e855c10 HEAD` (two commits; saved at out/P-DEC5/full.diff; fonts are binary). Agents' reports (read after forming your own view): `out/P-DEC5/agent-1-report.md`, `agent-2-report.md`.

## Check
1. Does the diff do what the row's text says, and only that? Anything beyond it (scope creep, files outside the row, other rows touched)?
2. Can any change move a byte of academy/greece output? Reason from the code (defaults, `set_metrics` reset between editions, the `course_topo` change in build.py returning COURSE_TOPO unchanged for DM Sans, ordering/caching). Run `python3 kit/baseline.py --check` yourself.
3. Correctness of `set_metrics` and the brand `[metrics]` validation in `kit/courses.py`: bad paths, missing keys, a brand with tokens changing --sans but no metrics (silent mismatch? should it warn or stop?), ascent/descent use, mono advance, 4 % fallback margin.
4. `verify.py`: serving the brand's faces; the floor scaling for the 68ch measure; any check still assuming DM Sans/Space Mono; `UNSERVED` handling.
5. Docs/comments made false or left stale: `brands/academy.toml` header, `brands/workbench.toml` comments, `docs/decoupling.md` §6 and §8, `kit/README.md`, docstrings of kit/viz.py, kit/verify.py, kit/baseline.py, skills/ and docs mentioning "a brand cannot change --sans or --mono", `docs/BACKLOG.md` rows naming P-DEC5 (P-DEC16's text), licence notices for vendored fonts.
6. Anything private, a brand string or a private term added to engine output.
Scripts go under /tmp. Literal absolute paths with rm -rf. Do not run verify.py --full.
