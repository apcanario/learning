# S-NAV1 · Step E · the diff sort and the reading-page test

Model: Opus 5.5 (claude-opus-5-5), a fresh agent. 22 Nov 2026.

## Verdict

PASS. Every difference between the build of the start commit 797b1d4 and HEAD 01127ee, in all three editions
(academy, greece, marketing-ai), falls into a named class, and every reading page is byte-identical once its nav and
SVG are stripped. `kit/p94_extract.py` runs again on the new motion. No commit, no push, no land.py, `kit/baseline.json`
and `kit/verify-hashes.json` untouched. No unit, brief, vault, course or CSS file changed. No permission check refused
a script.

## Files changed

- `kit/nav_diff_check.py` (new): the test.
- `kit/p94_extract.py`: the swell in place of the turn and breath.
- `out/S-NAV1/step-E.md` (this file).

`out/S-NAV1/landing-report.md` was already modified in the clone before this step; it was not touched.

## kit/nav_diff_check.py

Usage: `python3 kit/nav_diff_check.py <start-tree> <now-tree> [--edition E ...]`, where each tree is a built repo root.
Or `python3 kit/nav_diff_check.py --build <start-commit> [--now REV] [--edition E ...] [--keep]`. That form makes two
git worktrees under /tmp, builds each edition in each with that tree's own `kit/baseline.py` `build()`, compares, and
removes the worktrees. Exit 0 only when nothing is left unclassified and every reading page is identical. The docstring
gives the whole method.

**Scope.** The scope is what `baseline.py outputs()` writes:
- each edition's site folder;
- for academy, also `kit/README.md`, `kit/bibliography/` and each history course's bibliography folder.

These cases fail:
- an added or removed file;
- a non-HTML file that differs, except README's size table.

**Classification.** It is structural, not a regex over the text.
- `html.parser` tokenises each file. Each token keeps its exact source slice, and an assert confirms the slices rebuild
  the file byte for byte.
- A stack of open elements gives each token its outermost region. The rules apply in this order:
  - shell JS: the longest `<script>` in index.html, the inlined shell.js. The small theme-preload script is not a
    region.
  - theme CSS: the `<style>` in index.html.
  - nav markup: `aside#drawer`, `nav.main-nav`, `nav.sub-nav` and every `nav.crumbs`.
  - the home: `section#home`.
  - area pages: `section.panel#track-*`.
  - SVG lines: an element with class `topo` or `topo-*`, `relief` or `rel-*`, or `svg.topo-l`. The guard: its text
    tokens must be unchanged.
- Regions do not nest and each has a stable key. The tokens outside every region form the file's residue. Each region
  in the residue becomes one placeholder.
- `difflib.SequenceMatcher` aligns the two residues on the exact token slices. An unequal stretch must hold
  placeholders only. A region on one side only must be nav markup or an area page.
- A region on both sides is diffed token by token. Each unequal stretch counts once for its class.
- Any other difference fails. The output gives the file, the tokens and ten tokens of context.

**Reading pages.** These are checked:
- every shell panel other than the home and the area pages;
- every fetched HTML file: reports, units, course homes, syllabi, briefs, bibliography and How it was built pages,
  plus new.html, changelog.html and viz-examples.html.

Each is rebuilt from its tokens with every `<nav>` element, every `<svg>` element and the `style` attribute of a
line-illustration wrapper's start tag left out. The result must be byte-identical between start and now.

**Mutation test (greece).** Three changes were planted in a copy of the HEAD build:
- a letter in a unit paragraph: caught twice, as an other difference and as reading text;
- an attribute on `<main>`: caught as an other difference;
- an attribute on a `topo-l` and a class on a drawer item: allowed, as SVG lines and nav markup.

## Results (start 797b1d4 vs HEAD 01127ee; both runs gave the same output)

The same output came from building in /tmp worktrees with `baseline.build()` and from `--build 797b1d4…`.
"Stretches" are the unequal token runs. "Files" are the files in which that class differs.

| Class | academy | greece | marketing-ai |
|---|---|---|---|
| shell JS | 1 in 1 file | 1 in 1 | 1 in 1 |
| theme CSS | 1 in 1 | 1 in 1 | 1 in 1 |
| nav markup | 320 in 261 | 10 in 2 | 51 in 32 |
| the home | 42 in 1 | 15 in 1 | 21 in 1 |
| area pages | 6 added (1 file) | none (one track) | 2 added (1 file) |
| SVG lines | 9,429 in 245 | 2,037 in 80 | 1,769 in 28 |
| size table (kit/README.md) | 1 in 1 | n/a | n/a |
| files, start/now/differ | 460/460/272 | 82/82/81 | 36/36/35 |
| reading pages identical | 566 (272 fetched, 294 shell panels) | 162 (81, 81) | 76 (35, 41) |
| unclassified | 0 | 0 | 0 |

Greece's nav markup touches two files: index.html (the drawer) and greece/home.html (the area crumb dropped).

## Flagged differences, and what was decided

1. **The line break between added area panels** (academy index.html, marketing-ai index.html).
   - The first run flagged one insert per edition: the six (academy) or two (marketing-ai) `track-*` placeholders
     came with the `\n` text tokens the build writes between panels.
   - Decision: legitimate. These are the separators of the added panels, not content.
   - Rule added and documented in the docstring (WHITESPACE rule): whitespace-only text goes with a region that came
     or went in the same stretch. Whitespace anywhere else still fails. No class was widened.
2. **kit/README.md size table** (academy).
   - It is not one of the six classes in the spec. It is a build output (baseline.py writes it), and step A to D each
     listed it as expected.
   - Handled as an explicit seventh class, "size table". It passes only if every changed line on both sides lies inside
     the markdown table that names index.html with byte sizes; any other README change fails.
   - Recorded here as an addition to the spec's list, not a silent one.
3. **Line-illustration wrapper `style`** (`--ar` on a relief, `--ph` on a drawing).
   - This attribute sits on the wrapper `div.topo…`, outside the `<svg>`.
   - In the diff sort it is part of the SVG lines region (the whole wrapper).
   - For the reading-page test, that one attribute is stripped along with the svg. Step D's own sort did the same with
     the relief's `--ar`.
   - The text inside the wrapper is guarded.

No defect found.

## kit/p94_extract.py

It failed at import: the regex read `--topo-turn`/`--topo-cycle`, which step D removed. Changes:
- It reads `--topo-grow` and `--topo-breath` from shell.css, with the same pattern verify.py uses.
- A pose is now the point p of the swell, 0 at rest and 1 at its top. Each `topo-swell` animation on a separator's
  lines is paused there, its phase (negative delay) honoured, as verify.py's `swellAt` does.
- The old per-svg `transform` field became `scale`: the min and max scale its paths stand at. A still line is at 1.
- The markdown table gained a "Line scales" column.
- The docstring now describes the swell.

Run: `python3 kit/p94_extract.py /tmp/snav1e-p94` against the committed academy build. All 23 pages were extracted. On
m61 the lines' scales at the five poses are 1 / 1.0129 / 1.05 / 1.0871 / 1.1, and the clearances stay positive (3.3 px
right at the top).

Pre-existing, not changed: `choose()` sorts the newer courses (bw, pb, sp, sce) into "brand-b". The choice still
repeats.

## For the row's close (outside this step)

- `kit/p95_shots.py` still poses `topo-turn` and reads `--topo-cycle` in its `POSE_JS`. It imports, but its poses now
  leave the swell unposed. It is an old row tool and was not in this step's packet.
- `kit/README.md` and `design/README.md` could name `nav_diff_check.py` among the kit's tools.

## Blockers

None. The temporary worktrees (/tmp/snav1-start, /tmp/snav1-now and the two `--build` made) were removed and pruned;
`git worktree list` shows only the clone.
