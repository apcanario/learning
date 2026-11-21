# P-DEC5 · fresh check (packet 3)

Model: Opus 5.5 (`claude-opus-5-5`). 21 Nov 2026. Read and report only; nothing edited, committed or pushed.
Diff checked: `git diff e855c10 HEAD` (e0101f7, c828782).

## Verdict

**PASS WITH FIXES.** 0 errors, 3 should-fix, 7 minor.

The diff does what the row says, using the row's first option. `[metrics]` feeds `viz._tw`/`_text`, verify.py serves the brand's vendored faces, and the defaults are DM Sans and Space Mono. The two agent-2 additions are in scope: they fix the remaining probe failures caused by the face (the report measure floor and `course_topo`). Neither is a separate row. No other row is touched.

**Academy and greece are byte-identical.** I ran `python3 kit/baseline.py --check` myself: academy 457 files, 0 differ; greece 82, 0 differ; `baseline: clean`.

The code supports this:
- With no `[metrics]`, `set_metrics` restores `_DEFAULT`. `_MONO` stays 0.612 and `_BASE` stays 0.36, so `_tw` and `_text` do the same float operations as before.
- `course_topo` compares `viz._ADV['sans']` against the same default dict, so `extra` is 0 and it returns the `COURSE_TOPO` object itself.
- The verify floor is 560 × 684/684 = 560.0.
- `FONT_CSS` is `fonts.css` alone when no token names a vendored extra family.
- `set_metrics` resets on every call, so ordering cannot leak state.

I did not reproduce the probe or `verify.py --full`; the packet assigns those elsewhere.

## Should-fix

1. **Probe record committed in `kit/verify-hashes.json`.**
   - **Where:** `kit/verify-hashes.json:359-480` (new `"marketing-ai"` entry, added in c828782).
   - **Evidence:** The recorded global hashes match no file at HEAD. For example:

     | File | Recorded | HEAD |
     |---|---|---|
     | `brands/workbench.toml` | `3517e945…` | `e9404a51…` (`17952a66…` at e855c10) |
     | `design/theme.css` | `414fd48a…` | `1cc7a7c5…` (unchanged by the diff) |
     | `kit/build.py` | `d3819415…` | `94e0a178…` |
     | `kit/viz.py` | `770f3237…` | `2831f945…` |

     So this records an "ALL CHECKS PASSED" run of some other tree, not this repo's marketing-ai. Agent 2 says the change was already in the working tree before its packet. It is outside the row. Because every global hash mismatches, the next run is full and nothing is skipped wrongly. But a passed-run record that was never earned on this tree should not be committed.
   - **Fix:** `git checkout e855c10 -- kit/verify-hashes.json`. Let the chat's own `verify.py --edition marketing-ai` (or `--full`) on the real tree write the record if one is wanted.

2. **A brand that changes `--sans`/`--mono` without `[metrics]` passes silently.**
   - **Where:** `kit/courses.py:139-147`. The header `brands/academy.toml:23` says `[metrics]` is "required in effect".
   - **Evidence:** `_brand` validates `[metrics]` only when it is present. A brand with `tokens.sans = '"Source Sans 3",…'` and no `[metrics]` builds with DM Sans widths. That is the exact S-DEC3 state (24 figure-geometry failures), found only by a full verify run. The same happens with `sans` but no `sansb`: 400 in the new face, 600 in DM Sans, with no message.
   - **Fix:** In `_brand`, after the metrics checks, compare the token's first family with the theme's. If `tokens.sans` names a family other than DM Sans and `sans`/`sansb` are not both in `metrics`, call `_fail(path, '`tokens.sans` changes the face; name its metrics in [metrics] sans and sansb (brands/academy.toml header)')`. Do the same for `tokens.mono` without `metrics.mono`. If a warning is preferred to a stop, print one; but the header's "required in effect" reads as a stop.

3. **`kit/README.md` is stale on served fonts.**
   - **Where:** `kit/README.md:152`.
   - **Evidence:** It still says verify.py serves "DM Sans, Space Mono and Gentium Book Plus… SIL OFL, `fonts/OFL.txt`". It does not mention that a brand's faces are served from `fonts/<face>.css` with `OFL-<face>.txt`, or that Source Sans 3 and IBM Plex Mono are now vendored. The README has no `[metrics]` mention either.
   - **Fix:** Append to that bullet: "; a brand's own faces (P-DEC5) are a `fonts/<face>.css` with their woff2 and `OFL-<face>.txt` (vendored: Source Sans 3 400/600, IBM Plex Mono 400), served when the edition's tokens name the family, and their figure metrics are the brand's `[metrics]` (`brands/academy.toml` header)".

## Minor

4. **`docs/decoupling.md:112` keeps a false present-tense sentence.** "⚠ A brand cannot yet change `--sans` or `--mono`: …" is now immediately contradicted by "Done by P-DEC5". **Fix:** change it to "⚠ At S-DEC3 a brand could not change `--sans` or `--mono`: …; done by P-DEC5 (21 Nov 2026)…".

5. **Wrong package version at `docs/decoupling.md:133`.** It says "(`@fontsource` 5.3.0)" for both faces. `kit/fonts/source-sans-3.css:3` and agent 1's report say `@fontsource/source-sans-3` **5.3.1**; IBM Plex Mono is 5.3.0. **Fix:** "(`@fontsource/source-sans-3` 5.3.1, `@fontsource/ibm-plex-mono` 5.3.0)".

6. **P-DEC16 will be stale once P-DEC5 closes.** At `docs/BACKLOG.md:1852`, P-DEC16 says "a brand still cannot change `--sans` or `--mono` until P-DEC5 has closed" and "after P-DEC5 if the pass wants new body or mono faces". **Fix** (when closing P-DEC5 by §8): "a brand changes `--sans` or `--mono` through its `[metrics]` (P-DEC5); a change of the theme's own `--sans`/`--mono` in `design/theme.css` also needs `viz._SANS`/`_SANSB`/`_MONO` regenerated, and Academy's figures change". `[metrics]` is per brand. If P-DEC16 changes `theme.css`'s faces for Academy, the defaults in viz.py are what must change, and no doc says so.

7. **The table generator is not reachable from the docs.**
   - **Evidence:** `brands/academy.toml:23-34` and decoupling §6 say the tables are "read from the vendored woff2 with fontTools", but the only generator is `out/P-DEC5/font_metrics.py`. Neither doc names it. A brand author has to reverse-engineer the format: first subset holding the glyph, rounding, 0 for missing.
   - **Fix:** name `out/P-DEC5/font_metrics.py table|mono` (and its fontTools and brotli needs) in the academy.toml header line, or move the script to `kit/`.

8. **Validation of the metrics tables is thin.**
   - **Where:** `kit/courses.py:143-147` and `kit/viz.py:525-533`.
   - **Evidence:**
     - A table missing `chars` or `adv` raises a bare `KeyError` traceback in `set_metrics`; only a length mismatch gets a message.
     - `metrics.mono = true` passes the number check, because `bool` is an `int`.
     - `mono <= 0` is not rejected.
     - An absolute path in `metrics.sans` escapes the repo, because `_ROOT / '/x'` is `/x`. Such a file is also not in `verify_scope.global_files` unless it is under `kit/fonts/`.
   - **Fix:** In `_brand`, load each table and `_fail` unless it has `chars` and `adv` of equal length, with numeric `ascent`/`descent` if present. Reject `isinstance(m['mono'], bool) or m['mono'] <= 0`. Require `m[k]` to be relative and under `kit/fonts/`.

9. **A metrics table that equals DM Sans would not reproduce Academy's baselines.**
   - **Where:** `kit/viz.py:530-531`.
   - **Evidence:** Any table with `ascent`/`descent` sets `_BASE` to `(ascent - descent)/2000`. For DM Sans that is (992 - 310)/2000 = 0.341, not the hand-set 0.36. So a brand naming DM Sans's own regenerated table would move every `_text` baseline by 0.019 em. This contradicts the reading that "the tables equal the literals". The mono baseline also stays 0.36 for any mono face; the header documents the limit (1.120/0.361 em) but nothing checks it.
   - **Fix:** Say this in the `_BASE` comment ("the default 0.36 is hand-set; DM Sans' own line box would give 0.341, so a table is for a face other than DM Sans"). Optionally, put `mono_ascent`/`mono_descent` in `[metrics]` and check them against Space Mono's.

10. **The verify measure floor depends on the declared metrics, not the drawn face.**
    - **Where:** `kit/verify.py:2768`.
    - **Evidence:** `floor = 560 * viz._ADV['sans']['0'] / …`. A table whose `"0"` advance is 0 (a glyph the face lacks) gives floor 0, which disables the lower bound. If the tokens name a face the metrics do not describe, the floor follows the metrics. This is acceptable given the 68ch match beside it, but should be stated.
    - **Fix:** `floor = 560 * (viz._ADV['sans'].get('0') or 684) / 684`, using `viz._DEFAULT[0]['sans']['0']` for the 684s. Alternatively, make the `[metrics]` validation (item 8) reject a table with `"0"` = 0.

## Checked and fine

- **Scope:** files touched are viz.py, build.py, verify.py, courses.py, brand comments, decoupling §6/§8, kit/fonts additions and out/P-DEC5. These fit the row except item 1.
- **Licences:** `OFL-source-sans-3.txt` and `OFL-ibm-plex-mono.txt` carry the copyright and full OFL 1.1. The vendored CSS headers name the package, the version and the licence file.
- **Font serving:** in verify.py, `font_file` serves any `kit/fonts/*.woff2` under `/learning-vendored/`, so the new faces are served. `UNSERVED` and `THEME_FONTS` are computed after the extended `FONT_CSS`, so a vendored brand face counts as served and is checked as loaded.
- **Lede parse:** in build.py, `_LEDE` merges `.lede{…}` (line 275, 62ch) and `.lede{font-size:17px;line-height:1.5}` (line 896). Neither is inside a media query. `.hhome .lede` contributes margin only.
- **Markdown hero:** `course_topo(m['sc']['intro'])` is the hero lede `mdcourse.py:539` renders.
- **Privacy:** no private term, brand string or new engine text reaches built output. The new strings are comments, verify-only CSS and JSON outside the build output.
- **`brands/workbench.toml` comment:** accurate (it still changes `--serif` only).
