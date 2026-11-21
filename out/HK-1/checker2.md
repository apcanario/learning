# HK-1 · second-pass check of the applied findings

Checker: claude-opus-5-5 (fresh agent, not involved in the work or the first check), 21 Nov 2026. Read only: no repo
file edited, nothing built, verified, committed or published.

**Verdict: PASS with 0 ERROR, 0 SHOULD-FIX and 3 MINOR.** Every first-pass finding in scope (E1, S1, S2, M1 to M5) is fixed as decided.

## First-pass findings: fixed
- **E1 (fixed).** `kit/build.py` `hero_interval.fits` (l.1129) now measures with `sep_bytes` (l.473-476), the
  self-closed to end-tag rewrite that matches verify.py's `new Blob([topo.outerHTML]).size` (HOME_JS l.479). The
  derived interval is 24,500 (19,388 B as verify counts). p-hero1.md reports a Chromium readback equal to that figure.
  The "40 B lower" sentence is corrected in p-hero1.md, and the figures are corrected in the build.py comment and the
  kit/README.md row.
- **S1 (fixed).** The comment at l.1045-1062 and l.1062 says that 24,000 is W-SCE1's value, frozen as the floor by
  decision, and that P92 drew 22,000. It also says History stands 21 levels at 24,000, which is correct
  (510,493 / 24,000 rounds down to 21).
- **S2 (fixed).** `kit/howbuilt.py` `method_section` raises `SystemExit` unless exactly one row is `CADENCE_TOPIC`.
  `docs/method.md` l.23 has exactly one.
- **M1 (fixed).** The bisection is replaced by a scan upward from the floor, after the coarsest interval proves that
  some interval fits. The scan always ends, because `top` always fits. The result is memoised and deterministic.
- **M2 (fixed).** prove_expected.txt 2b shows two checks:
  - The start layer equals the render at 24,000.
  - The new layer equals the render at 24,500, and 24,400 does not fit.
- **M4 (fixed, beyond what was asked).** The README row is now compared exactly (OLD_PHRASE and NEW_PHRASE), not
  normalised.
- **M3 (fixed).** marketing-ai and fieldnotes are listed, and `m3_editions.txt` says PASS. The probe's
  `/tmp/hk1m3/now/kit/build.py` differs from the current file only in comment lines 1055-1057, so the result stands.
- **M5 (fixed).** The template now leaves the key out and names it in a comment. The pack.py docstring says the same.

## Baseline
`git diff kit/baseline.json` against HEAD (9447f39):
- There are 541 entries both before and after. None is added or removed.
- Exactly 10 entries change: academy `README.md`, `index.html`, and the seven markdown `built.html` files; and greece
  `index.html`.
- All 541 hashes equal the files on disk.

Against the first re-record (16:10, copies in `/tmp/hk1chk` and `/tmp/hk1m3/now`), only `academy/index.html` and
`academy/README.md` (`kit/README.md`) differ.

## New findings (MINOR)
1. **`courses/_template/course.toml` l.49: the commented placeholder is invalid TOML once uncommented.**
   - The placeholder reads `'⟨the course's own …⟩'`: the apostrophe in "course's" ends the literal string.
     `tomllib` raises "Expected newline … column 30".
   - Fix: use double quotes, `audit_cadence = "⟨the course's own audit cadence, …⟩"`.
2. **`kit/howbuilt.py` l.125 and l.129: a course that sets `audit_cadence = ''` gets no check.**
   - An empty string is falsy, so the S2 guard is skipped and the page prints the closed Fable cell again. That is the
     same regression S2 closes.
   - Fix: test `cadence is not None` in both places, or make `pack.load` reject an empty `audit_cadence`.
3. **`kit/build.py` l.1137 (and the cost note at l.1055-1057): build time grows without bound as the interval rises.**
   - The scan always starts at the floor and makes one drawing (about 0.43 s) per 100 words of rise.
   - Today it makes 7 drawings. At an interval of 30,000 it would make about 62 (about 27 s); at 40,000, about 162
     (about 70 s).
   - Fix, either of:
     - Record the cost growth in the comment as a known limit.
     - Scan downward from a bisected fitting `hi` only over a bounded window, for example 2,000 words, stating the
       trade-off. The size bumps measured span at most a few steps.

Out of scope, for the coordinator to note: the first pass's S3 (hero bound at other widths) and M6 (What's new has no
budget) are not rows in `docs/BACKLOG.md`, which is unmodified.
