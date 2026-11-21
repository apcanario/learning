# HK-1 · fresh check of P-HERO1, P-DEC20, P-DEC21 and the expected-differences proof

Checker: claude-opus-5-5 (fresh agent, not involved in the work), 21 Nov 2026. Read only: no repo file edited, nothing
built, committed or published. Scratch work in `/tmp/hk1chk` (a copy of the repo without `kit/academy`, `kit/editions`,
`.git`) and `/tmp/hk1scr` (scripts that exec `kit/build.py` up to the hero interval line, which writes nothing, and a
Chromium page loading a copy of `kit/academy/index.html`).

**Verdict: PATCH.** 1 ERROR, 3 SHOULD-FIX, 6 MINOR. P-DEC20 and P-DEC21 are correct as built; P-HERO1's budget is
measured differently from verify.py, so the academy hero is over 19 KB as verify counts it.

## What was confirmed

- `kit/shell.css` is byte-equal to `design/theme.css` (`cmp`). The only CSS rule added is
  `.panel.home>.hero.has-topo{min-height:380px}`, inside `@media (min-width:768px)` (theme.css 817 to 847). It matches
  only course homes: the nine `section.panel.home` in academy. The root home (`.panel.root`) and What's new
  (`section.panel.log`, `new.html`) do not match. No other `min-height` rule on a hero overrides it. No page has its own CSS.
- The hero layer in the new `academy/index.html` is byte-equal to `viz.render(HERO_TOPO, interval=24400)`, and the start
  build's layer is byte-equal to the same render at 24,000. So P-HERO1 changed the interval and nothing else in the drawing.
  This was checked independently of `prove_expected.py`; `viz.py`, `mdcourse.py` and `courses.py` are unchanged since 9447f39.
- The drawing is deterministic: two renders give the same sha256. Each edition's derived interval:
  - academy: 24,400. The layer is 19,825 B at 24,000 and 19,566 B at 24,300, so 24,400 is the smallest step that fits.
  - greece: 24,000 (5,159 B).
  - marketing-ai: 24,000 (4,356 B).
  - The template edition is not in the repo. It holds one or two small courses, so it stays at 24,000.
- `verify.py` never reads `HERO_INTERVAL` from build.py's source (grep), so removing the literal breaks nothing there.
- `kit/baseline.json` was re-recorded after the proof ran (16:10 against 16:07). It changes the same 10 entries, and each
  new hash equals the file now on disk (checked for 4 of them).
- The P-DEC21 default sentence is true for every markdown course today:
  - `docs/method.md` §5 (fresh check of every unit before filing) and §6 (staleness check six months after a search-on
    unit; the four-unit audit retired) say the same.
  - Each course's `pages/build-body.md` says the same: brand-ai l.18, building-with-ai l.18, personal-brand l.18,
    sport-psychology l.19, supply-chain-execution l.20, ux l.17. Each states the fresh check before filing and the
    six-month re-check of units written with live search.
  - Sport Psychology's extra safety read runs once per unit, before filing; it is not a periodic audit, so "No periodic
    audit" holds there too.
  - `pack.load` copies any `[pack]` key to an attribute (`k.upper()`), and `DEFAULTS` supplies `AUDIT_CADENCE` when a
    course sets none.

## ERROR

**E1 · `kit/build.py` 1117-1120 (`hero_interval.fits`): the 19 KB budget is not measured the way verify.py measures it.**
- verify.py (`HOME_JS` l.479, checked at l.647) measures `new Blob([topo.outerHTML]).size`, the HTML serialization of
  the layer. That serialization writes each self-closed SVG element out in full: `<path .../>` becomes
  `<path ...></path>` (+6 B) and `<circle/>` becomes `<circle></circle>` (+8 B).
- `fits()` measures the source string instead. For academy's layer (12 paths, 2 circles) verify's number is 88 B higher.
- Measured in Chromium on the built `academy/index.html`: build measure 19,428 B, verify's Blob 19,516 B. 19,516 B is
  over `HERO_BUDGET` (19,456 B), so the requirement "every home's hero under 19 KB" is not met as verify counts.
- `p-hero1.md` says "verify.py's Blob measure ran about 40 B lower"; that is wrong, it runs higher.
- verify still passes today, because its limit is 20 KB.

Fix:
1. In `fits()`, measure what verify measures, for example
   `len(re.sub(r'<(\w+)([^<>]*)/>', r'<\1\2></\1>', drawn[k]).encode())`.
   Say in the comment and the docstring that it is verify's outerHTML measure.
2. Rebuild. academy should derive 24,500: 19,300 B in source, about 19,388 B as verify counts. Check it with the same
   Blob measure.
3. Redo `expected-differences.md`, `prove_expected.py` and the baseline, and correct the figures and the "40 B lower"
   sentence in:
   - `p-hero1.md`
   - `kit/README.md`'s `build.py` row ("24,400 for academy")
   - `build.py`'s comment ("academy, 21 Nov 2026: 24,400, History 20 levels")

## SHOULD-FIX

**S1 · `kit/build.py` 1055: `HERO_INTERVAL_MIN = 24000` keeps the last hand-raised value under a new name.**
- 24,000 is exactly W-SCE1's size workaround (22,000, then 23,000, then 24,000). The comment calls it "the design
  density ... not a size workaround".
- The design density P92 chose was 22,000 (`kit/reviews/p92/check-hero-3.md`). The row asks for no hand-raised constant
  to be left.
- Fix, either of:
  - Set the floor to P92's 22,000. Then greece goes from 10 to 11 levels and marketing-ai changes too; list those
    expected differences.
  - Keep 24,000 and say in the comment that it is the value frozen at W-SCE1 and kept as the floor by decision
    (coordinator, HK-1), not as a measured density.

  Also fix the comment's claim "History's 510k words about 20 levels up": at 24,000 History stands 21.

**S2 · `kit/howbuilt.py` 125-126 (`method_section`): if no row matches, the closed Fable sentence comes back silently.**
- If `docs/method.md` §1 renames or rewords the "Audit cadence" topic, no row matches `CADENCE_TOPIC`. Every markdown
  page then prints the closed Fable stage's sentence again, which is the very regression P-DEC21 removes.
- Fix: when `cadence` is given, require exactly one row with `t == CADENCE_TOPIC`, else
  `raise SystemExit("docs/method.md §1 has no 'Audit cadence' row: kit/howbuilt.py CADENCE_TOPIC")`.

**S3 · Unrecorded finding (P-DEC20): the hero bound holds only at the widths verify checks. It should be a Carried
proposal in `docs/BACKLOG.md`.**
- The frame's width follows the window but the hero's height does not. A tablet between 769 and 1099 px needs a frame of
  up to about 565 px to show the whole tall view; course heroes are about 395 to 470 px. A desktop wider than 1280 px
  shows less of the wide view.
- This is recorded only as "⚠ Left" in `docs/decoupling.md` (P-DEC20 notes) and "Proposal, not done" in `p-dec20.md`
  l.104-111, not as a row.
- Fix: add a Carried proposal, e.g. "P-DEC27 · course-home hero bound at every width (min-height in container units, or
  verify at 1024 and 1920)".

## MINOR

**M1 · `kit/build.py` 1052 and 1114 (comment, docstring) and `kit/README.md` (`build.py` row): "the layer shrinking as
the interval grows" is not strictly true, so the bisection may not find the smallest fitting interval.**
- Measured on academy, 22,000 to 30,000 in steps of 100: the layer grows by 5 to 87 B at six steps, for example 23,900 to
  24,000 (+5 B), 27,500 to 27,600 (+87 B) and 28,500 to 28,600 (+50 B).
- Near the budget, the bisection can therefore return a larger interval than the smallest that fits. The result always
  fits, because `hi` is always tested, and today's 24,400 is the smallest.
- Fix: say "returns an interval at which the layer fits, near the smallest (the layer shrinks overall, not at every
  step)". Or, after the bisection, walk down from `hi` while `fits(hi - 1)`.

**M2 · `out/HK-1/prove_expected.py` 152-205: the hero layer is normalised to a placeholder, so any change inside it would
pass.** The proof checks only ring counts, words and sizes. Fix: add the check above,
`layer_new == viz.render(dict(HERO_TOPO, interval=HERO_INTERVAL))` and `layer_start ==` the same render at 24,000. This
checker ran it, and it holds.

**M3 · `out/HK-1/expected-differences.md`: it does not list marketing-ai's (or the template edition's) expected
differences.** These editions are not in the manifest. P-DEC20 changes their `index.html` CSS and P-DEC21 changes their
markdown `built.html` cells. P-HERO1 leaves their interval at 24,000. State this, or build marketing-ai in a probe and
diff it.

**M4 · `out/HK-1/prove_expected.py` 291: the README normaliser is lenient.** It accepts any `build.py` row that names
`HERO_INTERVAL_MIN` and `HERO_BUDGET` and drops `` `HERO_INTERVAL`) ``. Acceptable for a hand edit that `git diff`
shows, but the line should say so: "prose, reviewed by diff, not proved".

**M5 · `courses/_template/course.toml` 46-49 and `kit/pack.py` 34: the template repeats `DEFAULTS` against pack.py's own
rule.** The template's `audit_cadence` is DEFAULTS' text word for word, while pack.py says "a key repeating DEFAULTS
below is left out". The template comment explains why it is there. Fix, either of:
- Add a pack.py note that the template is the exception.
- Make the template's value a placeholder (`'⟨the course's audit cadence, or delete this line to use DEFAULTS⟩'`), as the
  template's other keys are.

**M6 · Unrecorded, same class as P-HERO1: What's new's hero layer has no size budget.**
- `academy/new.html`'s `div.topo` is 15,795 B. It adds a rise per filing day at a fixed `NEW_INTERVAL` (build.py 502),
  against the same 20 KB limit in verify.py (l.905).
- Course-home layers are 8 to 13 KB (ux-ia 12,927, the largest).
- Fix: a Carried proposal to give What's new (and course homes) the same budget rule as `hero_interval`, or to record
  the growth rate and when it reaches 20 KB.
