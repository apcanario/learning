# Packet 1 · P-DEC5 implementer (fresh Opus 5.5 agent)

Repo: /home/claude/learning (clone of apcanario/learning, main). Do NOT commit, push, or run `land.py`; the main chat does.
Write your full report to `out/P-DEC5/agent-1-report.md`. Reply in six lines at most (verdict, files changed, test results, your model id).

## The row (word for word, `docs/BACKLOG.md` P-DEC5)

> Let a brand set `--sans` and `--mono`: give `kit/viz.py` the brand's font metrics and have `verify.py` serve the brand's faces; or document that those two faces are fixed. ⚠ Touches figure geometry: academy's figure boxes must stay byte-identical, so the metrics default to DM Sans and Space Mono. Today `brands/<name>.toml` changes `--serif` only.

## Your work (step 2 of the chat's prompt)

Give `kit/viz.py` the brand's font metrics (advance widths read from the brand's font files, or a metrics table the brand names), defaulting to DM Sans and Space Mono so academy's figure boxes stay byte-identical, and have `verify.py` serve the brand's faces instead of the two fixed ones. OR, if that cannot be done without moving a byte of academy, document in `brands/academy.toml`'s header and `docs/decoupling.md` §6 that `--sans` and `--mono` are fixed, and say why. Prefer the first; fall back only on proof.

## Read first

`docs/decoupling.md` §5, §6 (S-DEC3 note: "A brand cannot yet change `--sans` or `--mono` ... 24 figure geometry failures: 9 on the Figure kinds page, 15 on phone panels") and §8; the docstrings of `kit/baseline.py`, `kit/viz.py`, `kit/verify_scope.py`; the header of `brands/academy.toml` (the brand schema); `kit/viz.py` lines ~480-510 (`_CH`, `_SANS`, `_SANSB`, `_ADV`, `_tw`, mono fixed at 0.612 em) and every caller of `_tw`/`_ADV`/'mono' width; `kit/verify.py` ~1195-1235 (`FONT_CSS`, `_TOK`, `VENDORED`, `font_file`, `new_page`) and its geometry check; `kit/fonts/` (vendored DM Sans, Space Mono, Gentium woff2 + `fonts.css`); `kit/courses.py` (`brand()`, how brand TOML keys reach the build).

## Files you may change

`kit/viz.py`, `kit/verify.py`, `kit/courses.py` (only to expose a new optional brand key), `kit/build.py` (only to pass the brand's metrics to viz if needed), `kit/fonts/` (add faces; do not alter existing files), `brands/academy.toml` (header/schema comment only; its values must not change output), `brands/workbench.toml` ONLY IF it still sets only `--serif` (leave it so), `docs/decoupling.md` (§6 note and §8 only where they describe what changed), `kit/README.md` prose only if it describes this (its size table is a build output in `baseline.json`: if you edit its prose, say so, the main chat rehashes that one entry), `kit/shell.js`/`design/theme.css` NOT at all. No unit, brief or vault file. Do not touch other rows.

## Constraints

- Academy and greece output must stay byte-identical: `python3 kit/baseline.py --check` must print `baseline: clean` after your change (it takes ~3 min: academy 123 s, greece 33 s). Run it. If viz.py's default metrics are regenerated from the font files, prove they equal the current `_SANS`/`_SANSB`/612 tables exactly (print a diff) before relying on them; if they differ in any value, keep the existing literal tables as the DM Sans defaults.
- Design: brand file names the metrics. Suggested shape (your call): optional brand keys, e.g. `[metrics]` with `sans`, `sansb`, `mono` pointing to vendored font files under `kit/fonts/` (read with fontTools if installed; else a plain table committed in the brand), `mono` advance in em; viz receives them through the same path the brand's other values take. Keep `_tw` fast.
- The faces for the probe are Source Sans 3 (400 and 600) and IBM Plex Mono (400). Get woff2 from npm `@fontsource/source-sans-3` and `@fontsource/ibm-plex-mono` (npm works through the allowlist; install into a scratch dir under /tmp, not the repo). Vendoring them into `kit/fonts/` in the repo: only add what verify.py needs to serve a brand's faces, with their `fonts.css` @font-face rules and OFL notices; verify.py must pick the faces named by the edition's brand tokens (`_TOK`), as it already partly does for `VENDORED`.
- Any python script you write goes under /tmp or `out/P-DEC5/`, never in `kit/` unless it is the engine change. Use literal absolute paths with `rm -rf`.
- Do not run `verify.py --full` on the real tree (a 25-minute run reserved for the chat's step 5). A scoped or `--edition marketing-ai` run is the chat's step 3 in a /tmp probe copy; you may do a quick smoke only of figure geometry if cheap.

## The test (docs/decoupling.md §5)

`python3 kit/baseline.py --check` → `baseline: clean`. Report: the exact diff proving the default metrics equal the old tables, which files you changed and why, how a brand declares its faces, and anything left undone.
