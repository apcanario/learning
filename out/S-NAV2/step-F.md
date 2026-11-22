# S-NAV2 step F · the close (docs/method.md §8)

Model: Opus 5.5 (`claude-opus-5-5`), a fresh agent. 22 Nov 2026. Nothing committed, pushed or landed; `kit/baseline.json` not re-recorded; `kit/land.py` not run. No unit, brief or vault file changed; no code changed (one docstring in `kit/viz.py`).

## Done

1. **Row moved.** S-NAV2 removed from `docs/BACKLOG.md` section 4e (its note says it closed on 22 Nov 2026 and names what it left); a row at the top of `docs/CHANGELOG.md`: 22 Nov 2026, the models (main chat Sonnet 5.5 thin; agents A to F and the checker each a fresh Opus 5.5, claude-opus-5-5), commits d1872fd3d (A), fd8ef300e (B), c3aa94138 (C), 49eba6d05 (D), 7a7437f64 (E), the result.
   - Closed: P-NAV1, P-NAV2, P-NAV4 (decisions already in `design/README.md` and `kit/CHANGELOG.md`), P-HK1 (bound in container units, checked at 1024, 1280, 1920 px). Their Carried rows removed.
   - P-NAV3 moved from Carried to Proposed as a task for Pedro by hand: WebKit would not install (proxy blocks Playwright's hosts); his iPhone check.
   - P-NAV7 stays in Carried, rewritten: waiting for Pedro's `?debug` readout from the artifact (Home > Area > Course > Unit, swipe back) and a check that claude.ai passes `?debug` into the frame.
2. **Site log.** Next row 1 (S-NAV2) moved to Done (2026-11-22, Academy, one plain sentence); Next renumbered 1 to 18. `private_terms.py` OK.
3. **Docs made false, updated:**
   - `docs/method.md` §7: a paragraph on the layouts verify checks, what `--shots` saves, and `PHONE_REF` re-pinned only deliberately by a row that changes the phone.
   - `skills/file-unit/SKILL.md` (§4 step 8, §5 steps 1 and 2) and `skills/new-course/SKILL.md` (step 6): 1280 px is now the tablet landscape layout, the shot layouts add the desktop, the new viewports, the `PHONE_REF` rule. These are account skills too: P-DEC26 (Pedro by hand) now asks him to re-save `file-unit` as well as `new-course`.
   - `design/README.md` "After a theme change" step 4 (the widths, the drawer below 1100 px, sidebar from it, top bar and outline on a desktop, `PHONE_REF`); root `README.md` "After a theme change" step 3 (`PHONE_REF`).
   - `kit/README.md` `verify.py` row: "the area line's four names" now "names, one per track". `kit/viz.py` docstring: the hero's tall layout below 900 px (1100 px before 6.22).
   - `docs/supply-chain-execution-prompts.md` Reply line: the by-hand list (it named P-SCE1 and P-SCE6 only) now names the rule and, on 22 Nov 2026, P-SCE1, P-SCE6, P-NAV3 and P-DEC26.
   - Checked and left: theme.css's 6.5 header entry and design/README's 6.5 paragraph ("four areas", "12 s") are history; kit/README session 14 (300 px sidebar) is history; no "expected tall" text is left; `verify.py`'s docstring and `--shots` text were already corrected by D and E.
4. **Proposals**, new rows under Proposed in `docs/BACKLOG.md` (Proposed, not Carried, as the brief said, so they are not added to W-SCE3, a unit row; each with ⚠):
   - P-NAV8 sidebar at 900 to 1099 px (⚠ `shell.js` 1100 px query; drawer behaviour on tablets; republish).
   - P-NAV9 outline with h3 subsections (⚠ build change; every unit page's markup; the expected-differences proof).
   - P-NAV10 greece one-track home, first tile above the fold at tablet landscape (BUGS 1; ⚠ hero or header design; breaks P-HK1's bound if the hero is lowered).
   - P-NAV11 a way to turn `?debug` on in the artifact if the frame drops the query (⚠ `shell.js` in both artifacts).
   - From the checker's notes, not done by any step: P-NAV12 desktop focus order differs from visual order (note 7), P-NAV13 the home's frame budget unproven against the fault (note 6), P-NAV14 the empty brand-width gap left of the main nav on a desktop home (note 8).
   - Also fixed: a blank line had split P-DEC26 out of the Proposed table; the rows are one table again.
5. **Next up** set to W-SCE3, with "S-NAV2 closed on 22 Nov 2026". Its prompt written with `python3 kit/next_prompt.py --row W-SCE3 --save` (a public-course writing row, so `--save` is the documented way), saved in its row; the same text in `out/S-NAV2/next-prompt.md`. Its step 1c carries P-DEC24, P-DEC27, P-HK2 to P-HK5 and P-NAV7.

## Checks

- `python3 kit/baseline.py --check`: **not clean, 3 files**: `README.md` (shell size 630 KB to 629 KB, plus the one prose fix), `academy/changelog.html` and `academy/index.html` (the site-log entry: Done gains S-NAV2, Next loses it and is renumbered). greece 0. These follow from §8 step 1b and cannot be avoided by a docs-only close: the main chat must land with a "baseline re-recorded (F)" commit and `drop:` entries.
- `python3 kit/index_check.py`: courses-index.md matches the sources.
- `python3 kit/private_terms.py`: OK.

## For the main chat

- `kit/viz.py` is a kit `.py` file: its docstring change makes the landing's verify a full run (about 40 minutes). Revert that one line if a scoped run is wanted.
- Not done here (yours): §8 step 4, the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md`; the publish and deploy identifiers in the changelog row after the publish.
- `out/S-NAV2/landing-report.md` was already modified before this step (E's landing entry); left as it was.
