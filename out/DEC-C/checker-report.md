# DEC-C · fresh check of P-DEC8, P-DEC11, P-DEC15 (21 Nov 2026, Opus 5.5)

Scope: `git diff e855c10d4..HEAD` (8f931ec P-DEC8, 5aada6f P-DEC11, 6d5b665 P-DEC15) against the rows in
`docs/BACKLOG.md` (lines 1844, 1847, 1851), `docs/decoupling.md` §5, §6, §8 and `docs/method.md` §5. Main tree read only.

**Verdict: PASS WITH FINDINGS.** 0 must-fix, 4 should-fix, 6 nits.

## Independent proof (probe `/tmp/check-dec-c`)

- Two copies of the main tree: `after` (HEAD) and `before` (HEAD with `kit/build.py`, `kit/howbuilt.py`, `kit/verify.py`
  checked out at e855c10d4). Built academy, `--edition greece` and `--edition marketing-ai` in both.
- academy: exactly 4 files differ (`building-with-ai-bw`, `sport-psychology-sp`, `supply-chain-execution-sce`, `ux-ia`
  `built.html`), each equal to `before` with the S-NOAUDIT clause removed (1 occurrence each). `new.html` byte-identical.
  brand-a, brand-b, personal-brand-pb keep the clause. `kit/README.md`, `kit/bibliography`, the history bibliographies: 0 differ.
- greece: 0 differ (What's new included).
- marketing-ai: 2 differ: `building-with-ai-bw/built.html` (clause only) and `new.html` (only inside the `<svg>`; text
  outside the svg identical; `data-words` identical; rings per day 5,3,0,4,7 -> 7,4,0,6,10). Matches expected.md and
  expected-P-DEC15.md.
- The `after` rebuild equals the committed `kit/academy/` and `kit/README.md` (git status clean after building): the
  committed outputs are reproducible from the committed code.
- academy `new.html` largest day 221,673 words, `data-rings` 20 = 221673 // 11000, so verify's new scale check (now applied
  to academy too) holds statically.
- `check_dec8.py` re-run on the probe builds: P-DEC8's 5 files pass; it fails only on marketing-ai `new.html`, which is
  P-DEC15's change (the script predates it). Expected.
- The P-DEC11 geometry (`/tmp/dec11-tools/geo.py`, extended to 1 to 16 rises, run on both trees): before, 1 and 2 rises
  fall outside a 347 px band; after, 1 to 5 inside, 6 to 16 outside at 347 and 330 px; at 390 px 6 to 10 outside, 11+
  inside; at 398 px only 6 outside. Academy's homes (11 to 15 rises, 398 to 500 px) are inside.
- `new_interval` edge cases: top 0 -> 1, 0 levels (range skipped, scale passes); top 1..9 -> 1, top levels (range
  skipped); top 10..19 -> 1, 10..19 levels; top 20..109,999 -> top // 10, 10..19 levels (max 19 at top 19, 10 + r//q);
  top >= 110,000 -> 11,000 (academy, greece unchanged; at 110,000 exactly 10 levels, at 109,999 10,999 a level, 10 levels).
  build.py and verify.py copies are textually identical.

Each row does what it says. P-DEC8: data-driven (`d.AUDIT_LOG`), nothing else changed. P-DEC11: `small` view in the
wide `COURSE_TOPO` only (What's new's `NEW_TOPO` untouched), 200 px bound relaxed only at the page's foot with the anchor in
the window (the document is the scroller: `shell.js` uses `window.scrollTo`/`scrollIntoView`, no inner overflow panel, so
`document.scrollingElement` is the right measure). P-DEC15: only `new_layer` uses `new_interval`.

## Findings

### Should-fix

1. **should-fix · `README.md:43`** · The Known limits line still names P-DEC8 as the open remedy for "the closed Fable
   stage" on the How it was built page. Why: P-DEC8 is done; the clause now stays only on courses with `audit_log`
   rows (brand-a, brand-b, personal-brand-pb) by design, and the remaining Fable-stage text on every How it was built page
   is the method table's "Audit cadence" row (`None since 15 Nov 2026 (S-NOAUDIT) ...`), which no row covers. Say what is left
   and drop P-DEC8 from the pointer.

2. **should-fix · `out/DEC-C/P-DEC11-report.md:31` (and `docs/decoupling.md:132`)** · The "1, 2, 6 and 7 rises outside, 3 to 5
   inside" computation, and so the Known limit's "six or more", rests on `/tmp/dec11-tools/geo.py`, which is not saved in
   `out/DEC-C/`. Why: §5's proof must survive the chat; /tmp does not. Save it beside the other scripts. The claim itself
   holds (re-run here, 6 to 16 outside at 330 and 347 px).

3. **should-fix · `README.md:43`, `docs/decoupling.md:132`** · "a course of six or more units whose desktop hero is under about
   400 px" is imprecise in a way that matters for the next filings: at 398 px (Academy's own shortest course hero, brand-b's)
   a six-rise course already falls outside; at 390 px six to ten do, eleven or more do not (equal-word rises, re-run of
   geo.py). Why: a public course reaching six units with a short lede (SCE has 0 of 20 written) can fail desktop motion with
   an Academy-typical hero, not only with a one-line lede. State it as "six to about ten rises, with a hero under about 400
   px", or name the measured cases.

4. **should-fix · BACKLOG P-DEC8 row (line 1844) / `out/DEC-C/P-DEC8-report.md`** · The row requires "re-record the manifest
   after the diff is shown to be only that"; not done in any of the three commits (`p_dec15_baseline-check-final.log`:
   5 differ). Why: until re-recorded, every later `baseline.py --check` reports these 5 files. Owed at the close, after the
   full verify now running.

### Nits

5. **nit · `kit/verify.py:1513`** · `fresh_land` docstring still says it returns `[visible panel, anchor found, anchor top]`;
   it now returns four values (the comment at 1493 was updated, the docstring not).

6. **nit · `kit/verify.py:15-17`** · Module docstring: "What's new's 10 to 25 levels hold for every edition (P-DEC15)". Not
   for an edition whose largest day is under 10 words (line 914 skips the range there; `docs/decoupling.md:139` says "10
   words or more" correctly). Also the run's message (919-920) does not say the range was left out in that case.

7. **nit · `docs/decoupling.md:133`, `kit/verify.py:1494`** · Scope of the 200 px decision. The row asks about "the split
   check's 200 px landing bound"; `lands()` also relaxes the reading deep link (`check_reading`, line 1913). Consistent with
   the stated rule (only a page too short to scroll) and recorded in §6, so acceptable; noting that it goes one check wider
   than the row's wording.

8. **nit · `docs/decoupling.md:128`** · "Proposed rows" still lists P-DEC8, P-DEC11, P-DEC15 as proposed with no mark that
   they were done on 21 Nov; §6 has notes for P-DEC11 and P-DEC15 but none for P-DEC8. Add "(done 21 Nov 2026, DEC-C)".

9. **nit · `out/DEC-C/expected-P-DEC11.md` "Docs" bullet** · Lists `docs/BACKLOG.md` P-DEC11 row among the docs changed; no
   commit touches `docs/BACKLOG.md` (rows not closed, CHANGELOG not written; the reports leave both to the main chat's §8
   close). Not a proof failure; the §8 close is still owed for all three rows.

10. **nit · `out/DEC-C/p_dec15_check.py`, `check_dec11.py`, `check_dec8.py`** · Hard-coded `/home/claude/learning` and
    `HEAD` comparisons: after the commit, `p_dec15_check.py`'s README and `new.html`-against-HEAD checks compare HEAD with
    itself (README check would now fail), so the saved `.out` files are the record, not re-runnable proofs. Fine as a record;
    the independent before/after rebuild above stands in for them.

## Decisions reviewed

- **200 px bound (P-DEC11).** Sound: `SETTLE_JS` still breaks early only inside -5..200; the fourth value needs top > 200,
  top < innerHeight and the document at its foot, which a long page that failed to scroll cannot meet. A short page costs
  the full 3 s wait, no retry (lands on the first attempt).
- **`small` view (P-DEC11).** Sound and inert for every existing course home (fewest rises 11); band .17 to .76 matches a
  330 px hero (.5 - .33, + .9 x .66).
- **`new_interval` (P-DEC15).** Sound: 11,000 kept at >= 110,000 words, academy and greece byte-identical, small editions
  10 to 19 levels, inside 10 to 25; the duplicate in verify.py is identical, and a divergence would show as verify's scale
  failure. No edition-file key to drift.
- No doc, skill or docstring still says 14,000 (kit/README.md fixed; `kit/viz.py:3223` and `kit/build.py:503` mention 14,000
  as history, correctly). `skills/` say nothing about these rows. `kit/README.md` `howbuilt.py` row still true.

Model: Opus 5.5 (claude-opus-5-5).
