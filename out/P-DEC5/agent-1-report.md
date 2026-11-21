# P-DEC5 · agent 1 (implementer) report

Model: Opus 5.5 (`claude-opus-5-5`). 21 Nov 2026. Nothing committed or pushed; `land.py` not run.

## Verdict

**Done, the first option.** A brand can now set `--sans` and `--mono`. It names its faces' metrics in an optional `[metrics]` table. `kit/viz.py` sizes figure text from those metrics, and `kit/verify.py` serves the brand's vendored faces. Academy and greece stay byte-identical: `python3 kit/baseline.py --check` gives `baseline: clean` (academy 457 files, 0 differ; greece 82 files, 0 differ; ran three times, the last on the final tree, output in `out/P-DEC5/baseline-check.txt`). The fallback (documenting that the faces are fixed) was not needed.

One finding beyond the packet: **widths alone were not enough.** With Source Sans 3's advance widths, all 24 failures stayed. Each was a link label's line box running 0.6 px past the bottom of its plate. Source Sans 3's hhea line box is 1.424 em (ascent 1024, descent 400). DM Sans' is 1.302 em (992/310). `_text` puts every baseline at a hand-set 0.36 em below the middle of the line. So the brand's sans table also carries the face's ascent and descent, and `_text` centres that face's line box (baseline at `(ascent - descent) / 2` em below the middle of the line). The default stays the literal 0.36.

## Proof that the default metrics equal the old tables

`out/P-DEC5/font_metrics.py proof` reads `kit/fonts/dm-sans-latin(-ext)-{400,600}-normal.woff2` and `space-mono-latin-400-normal.woff2` with fontTools. For each character, the first subset that holds the glyph gives `round(advance * 1000 / unitsPerEm)`, and a missing glyph is 0. The script compares the result with the literals in viz.py (output in `out/P-DEC5/proof.txt`):

```
DM Sans 400: 134 literal values, 134 regenerated, 0 differ
DM Sans 600: 134 literal values, 134 regenerated, 0 differ
Space Mono 400: regenerated 0.612 em, literal 0.612: equal
```

The diff is empty. The literal tables still stay in viz.py as the defaults, so the build needs no font library (brotli, which woff2 needs, is not installed for the repo; I used it from `/tmp/pdec5/pylib`). The default code paths do the same float arithmetic as before: `_MONO * size + ls` with `_MONO = 0.612`, and `size * _BASE[font]` with 0.36.

## How a brand declares its faces

In `brands/<name>.toml` (the schema is in the `brands/academy.toml` header, `[metrics]`):

```toml
[tokens]
sans = '"Source Sans 3",system-ui,-apple-system,Segoe UI,Roboto,sans-serif'
mono = '"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace'

[metrics]
sans = "kit/fonts/source-sans-3-400.metrics.json"
sansb = "kit/fonts/source-sans-3-600.metrics.json"
mono = 0.6
```

It also points `fonts_href` at those families.

- **`sans` and `sansb`:** each is a JSON table `{"face", "from", "chars", "adv", "ascent", "descent"}`. `adv` holds the advances per 1000 em for `viz._CH` (0 for a glyph the face lacks). `ascent` and `descent` are the hhea line box per 1000 em.
- **`mono`:** the mono face's advance, in em.
- **Defaults:** a key left out keeps its default (DM Sans 400/600, Space Mono 0.612, baseline 0.36).
- **Mono's line box:** the mono baseline is not moved, so the header says a mono face's line box must reach no further than Space Mono's (1.120 em up, 0.361 em down). IBM Plex Mono (1.025/0.275) fits.
- **Validation:** `kit/courses.py` checks the keys and that the files exist.
- **Serving the faces:** to have `verify.py` serve the faces, vendor the woff2 into `kit/fonts/` with a `kit/fonts/<face>.css` of `@font-face` rules (URLs `https://fonts.gstatic.com/learning-vendored/<file>.woff2`) and an `OFL-<face>.txt`. `verify.py` adds that CSS to `fonts.css` when the edition's tokens name its family. For academy, greece and marketing-ai today, `FONT_CSS` is still exactly `fonts.css` (checked).
- **Making the tables:** `python3 out/P-DEC5/font_metrics.py table <out.json> "<face>" <subset.woff2>...` and `... mono <woff2>`. This needs fontTools and brotli.

## Files changed and why

| File | Change |
|---|---|
| `kit/viz.py` | Adds `_MONO`, `_BASE`, `_DEFAULT` and `set_metrics(brand)`. `set_metrics` resets to the defaults, then loads the brand's tables. `_tw` reads `_MONO`, and `_text` reads `_BASE[font]`. The comments say what the literals are and record the proof. |
| `kit/build.py` | One line: `viz.set_metrics(B)` after `import viz`. |
| `kit/verify.py` | Adds `viz.set_metrics(brand(EDITION))` after `import viz` (its timeline stem check calls `viz._tw`). `FONT_CSS` is now built after `_TOK` and adds any `kit/fonts/<face>.css` whose family the tokens name. |
| `kit/courses.py` | `_brand` validates the optional `metrics` keys, file paths and the mono number. |
| `kit/fonts/` (added only) | Source Sans 3 400 and 600 and IBM Plex Mono 400, latin and latin-ext woff2 (`@fontsource/source-sans-3` 5.3.1 and `@fontsource/ibm-plex-mono` 5.3.0 from npm). Also `source-sans-3.css` and `ibm-plex-mono.css` (unicode ranges from the packages' `unicode.json`), `OFL-source-sans-3.txt`, `OFL-ibm-plex-mono.txt` (the packages' LICENSE), and `source-sans-3-400.metrics.json` and `source-sans-3-600.metrics.json`. No existing file altered. |
| `brands/academy.toml` | Header only: the `[metrics]` schema. Values unchanged. |
| `brands/workbench.toml` | Comment only: the stale "a brand that changes --sans or --mono breaks figure geometry" now points to `[metrics]`. It still sets only `--serif`. |
| `docs/decoupling.md` | §6: the S-DEC3 ⚠ sentence now ends "Done by P-DEC5" and points to a new "Notes on P-DEC5" block at the end of §6. §8: the first-probe sentence gets "(P-DEC5: 0 with the brand's `[metrics]`)". |

Not touched: `kit/README.md`, `kit/shell.js`, `design/theme.css`, units, briefs, vault, other rows.

## Probe (figure-geometry smoke, not the chat's step 3)

The probe ran in a copy at `/tmp/pdec5/probe`, with `workbench` set to Source Sans 3 and IBM Plex Mono and their `[metrics]` (the brand file is saved at `/tmp/pdec5/wb-with-metrics.toml`). `python3 kit/build.py --edition marketing-ai` built 33 fetched files, 3.97 MB.

`/tmp/pdec5/smoke/smoke.py` imports `verify.py` and runs `check_figures`, `check_phone_figures` and `check_panels(phone)` only (33 s).

- **With `[metrics]`:** fonts loaded were IBM Plex Mono 400 and Source Sans 3 400 and 600. The examples page had 0 geometry faults. Compare and bars on a phone had 0 faults. The phone panels' figure geometry passed: 125 figures on 26 panels. **SMOKE PASSED**.
- **Control, same copy without `[metrics]`:** **24 FAIL**, the same 9 + 15 as S-DEC3.

The full `verify.py --edition marketing-ai` in a probe copy is still the chat's step 3; the full run on the real tree is step 5.

## Notes and left undone

- **Accidental build on the real tree:** a failed `rsync` (not installed) let one `python3 kit/build.py --edition marketing-ai` run in the real tree with the unchanged workbench brand. It wrote only `kit/editions/marketing-ai/`, which git ignores. No tracked file changed (`git status` shows only my edits).
- **Generator location:** the metrics generator is in `out/P-DEC5/font_metrics.py`, because the packet keeps scripts out of `kit/`. If brands are to make their own tables from the repo, the main chat may want to move it to `kit/` (it is referenced only from this report and `docs/decoupling.md` describes the method, not the path).
- **Faces vendored:** only Source Sans 3 400 and 600 and IBM Plex Mono 400. Theme text at weight 500 or 700, or mono 700, would be drawn by the browser from the nearest face. Figure geometry uses only sans 400/600 and mono 400.
- **Verify scope:** adding files to `kit/fonts/` and editing `kit/*.py` makes the next scoped verify a full run (global files), as `verify_scope.py` intends.
- **What `_BASE` covers:** it applies only through `_text` (boxes, plates, node labels). Other kinds place text by their own formulas and passed the smoke unchanged.
