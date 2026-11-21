# P-DEC11 · small course's motion and briefs landing · agent report

Agent: Opus 5.5 (claude-opus-5-5), fresh, 21 Nov 2026. Clone `/home/claude/learning`, branch main, from 8f931ec
(P-DEC8 in; manifest not re-recorded). Probe copies: `/tmp/probe-dec11` (template test), `/tmp/probe-dec11-academy`
(full verify of the changed tree). No push, no reset, manifest not re-recorded.

**Verdict: done.** The template test's 10 desktop motion failures and its briefs landing are fixed; `verify.py --edition
fieldnotes` ALL CHECKS PASSED in the probe; academy and greece byte-identical to the post-P-DEC8 state (only P-DEC8's 4
files differ from the manifest, each with unchanged bytes).

## The row (docs/BACKLOG.md line 1847, word for word)

> | P-DEC11 | *Proposed (S-DEC4).* A course of two short units (the template test's home-composting, 1,170 words a unit) fails verify's motion pass on the desktop: at the five poses one rise's spot ring falls outside the wide layout's frame or in its fade (10 failures, 1280 px, dark and light). Fix in `kit/build.py` (`COURSE_TOPO` wide box/view, or `ct_lattice` for n ≤ 2) so a small course's rises stay inside; and decide whether the split check's 200 px landing bound applies to a page too short to scroll (a two-brief briefs page lands at 248 px). ⚠ Academy output may change (course-home layers): list the expected differences first. | S-DEC4 packet 2, template test | Any chat after S-DEC4 |

## 1 · Reproduction (probe `/tmp/probe-dec11`)

`/tmp/template-test` no longer existed and S-DEC5 kept no file contents, so the template test was recreated by script,
`out/DEC-C/p_dec11_template.py <copy-root>` (refuses the main tree): course `courses/home-composting/` (HC1, HC2, three
sections each, 1,254 and 1,252 words; course.toml with `[pack]`, briefs.md, pages/), track `garden` in `catalog.toml`
(with `hero`), `brands/fieldnotes.toml`, `editions/fieldnotes.toml` (`omit = ["changelog", "backlog"]`) and a
`docs/courses-index.md` section. No `.py` touched by it. `python3 kit/build.py --edition fieldnotes`: 2.3 s.

`cd kit && python3 verify.py --edition fieldnotes --full` before the fix: 14 FAIL (`/tmp/dec11-verify-before.log`):
the 10 `home-composting-hc desktop motion dark|light pose 0…1: the rises ['HC2'|'HC1'] have rings outside the frame or in
its fade` (reproduced), `split: #home-composting-hc-b-hc1 ... top 343`, and 3 courses-index rows (the first version of
the setup script wrote a section without the table; fixed in the script, content only).

## 2 · Cause and fix

Measured (Playwright, 1280 x 800): the hero frame of home-composting is 980 x 347 px; Academy's course homes are 398
(brand-b) to 500 (sport-psychology) px. The wide layout (1000 x 500, slice) in a 347 px hero shows y .153 to .847,
faded from .778; its view `(.04, .1, .96, .84)` assumes 400 to 480 px. With one or two rises the lattice is one row and
the spread is set by the width between them (two: .1193, rings about 45% of the layout's height), so the turned box
corners of the outer rise cross the top of the band (HC2 box `619 91 788 312`). Computed with `ct_fit` itself
(`/tmp/dec11-tools/geo.py`) in a 347 px band: 1, 2, 6 and 7 rises fall outside, 3 to 5 inside; in a 400 px band all
pass. So hero height is the root cause; one or two rises is where the rings are largest.

Fix, `kit/build.py`:
- `COURSE_TOPO` wide gains `small=(2, (.04, .17, .96, .76))`: the band a 330 px hero shows (y .5 ± .33, fade from
  .17 + .9 x .66); comment gives the reason and the measurements.
- `ct_fit`: `view = sp['small'][1] if 'small' in sp and len(rises) <= sp['small'][0] else sp['view']`, used in the
  `turned_inside` test. `NEW_TOPO` has no `small`: What's new unchanged.
- Result in the probe: home-composting's spread .1193 → .0374, boxes `218 123 372 257` and `641 119 764 280`.

Not chosen: a tighter wide view for every course (tried in the probe: all 8 Academy course homes change bytes) and a
hero `min-height` in `design/theme.css` (changes the shell of every page; out of the row's stated scope). ⚠ Left open, in
§6: a course of six or more rises with a hero under about 400 px would still fail; none exists today.

## 3 · The 200 px landing bound (decision: relaxed only for a page too short to scroll)

The bound wants the anchor near the window's top. Measured on fieldnotes' briefs page: at 390 px the page scrolls 38
px at most and stands at 38 (its foot), anchor top 343; at 1280 px it cannot scroll (max 0), anchor 267. The shell did
all it could. `kit/verify.py`:
- `SETTLE_JS` returns a fourth value: the anchor's top is past 200, inside the window, and the page stands at its foot
  (`scrollTop >= scrollHeight - innerHeight - 1`). Its wait loop still breaks only inside -5..200, so a short page is
  read after the full 3 s (no early exit on a transient foot).
- `lands(sec)`: found and (-5..200, or that fourth value). Used by `fresh_land()` and its four callers (the split's
  section link, links into unopened syllabus/briefs/homes, the briefs page's first anchor; the reading deep link).
  A page that can scroll further is still held to the band. The Sources and note deep links keep their own bound.
Recorded in `docs/decoupling.md` §6, "Notes on P-DEC11".

`verify.py --edition fieldnotes --full` after: **ALL CHECKS PASSED**, 2 m 36 s (`/tmp/dec11-verify-after.log`).

## 4 · Expected differences, then the main-tree diff

`out/DEC-C/expected-P-DEC11.md`, written before the main-tree diff. Course homes with two or fewer rises, by
`out/DEC-C/p_dec11_rises.py` (markdown course data and the built wide layouts): academy none (fewest 11: brand-a,
brand-b; supply-chain-execution has no layer), greece none, fieldnotes (probe) home-composting-hc. So: academy
byte-identical to post-P-DEC8, greece 0 differ.

Main tree: change applied (`kit/build.py`, `kit/verify.py`); sha256 of every output root taken before
(`out/DEC-C/p_dec11_sha-before.txt`, 539 files: kit/academy, kit/editions/greece, kit/README.md, kit/bibliography,
courses/{greece,rome}/bibliography); `python3 kit/baseline.py --check` (`out/DEC-C/p_dec11_baseline-check.log`):
academy 457 files, 4 changed (P-DEC8's: building-with-ai-bw, sport-psychology-sp, supply-chain-execution-sce, ux-ia
built.html), 0 added, 0 removed; greece 82, 0 differ. `python3 out/DEC-C/check_dec11.py` (`out/DEC-C/check_dec11.out`):
539 files byte-equal to before (so P-DEC8's 4 unchanged by this row), baseline lists exactly P-DEC8's 4: PASSED. No
word-level diff to save: no file differs.

## 5 · Full verify of the changed tree (probe `/tmp/probe-dec11-academy`, a copy of the main tree with the change)

`cd kit && python3 verify.py --full` (academy): **ALL CHECKS PASSED**, 28 m 50 s, 0 FAIL. `verify.py --edition
marketing-ai --full`: **ALL CHECKS PASSED**, 5 m 57 s. Tails saved: `out/DEC-C/p_dec11_verify-academy-tail.txt`,
`p_dec11_verify-marketing-ai-tail.txt`; fieldnotes logs `p_dec11_verify-fieldnotes-before.log` and `-after.log`.

## Files changed (commit)

- `kit/build.py` (COURSE_TOPO wide `small`, ct_fit), `kit/verify.py` (SETTLE_JS, lands(), five call sites)
- `docs/decoupling.md` §6 (Notes on P-DEC11), `README.md` (Known limits line)
- `out/DEC-C/`: this report, `expected-P-DEC11.md`, `p_dec11_template.py`, `p_dec11_rises.py` and its three `.out`,
  `check_dec11.py`, `check_dec11.out`, `p_dec11_baseline-check.log`, `p_dec11_sha-before.txt`, the verify logs and tails

## Not done (by instruction or scope)

- `docs/BACKLOG.md` row P-DEC11 not moved, `docs/CHANGELOG.md`, `kit/CHANGELOG.md` and `claude/` mirrors not written:
  left to the main chat's §8 close (as P-DEC8). No site-log entry (a kit fix with no visible academy change).
- Manifest not re-recorded; no push; no publish (academy bytes unchanged).
- `kit/verify-hashes.json` not written in the main tree (the full runs were in the probe).

## Proposals

- (⚠ changes every course home's bytes) A minimum desktop hero height for course homes in `design/theme.css`, or a
  wide view derived from the shortest hero, so a course of six or more units with a one-line lede cannot reach the
  band's top. Not needed by any course today.

Model: Opus 5.5 (claude-opus-5-5).
