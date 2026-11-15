# audits/

Audit reports that are not kit files. Personal Mythology audits stay in `kit/audits/`.

| Path | What |
|---|---|
| `brand-ai/audit-1.html` | Brand + AI Audit 1 page (Fable 5.1, 28 October 2026), saved from its artifact. |
| `brand-ai/fresh-check-B2.md` | B2's fresh-check report (Fable 5.1, 28 October 2026; fix, 3 errors, 10 should-fix, 14 minor), filed from its chat under P18 (28 October 2026); the unit was filed before P17 made this a filing step. |
| `brand-ai/fresh-check-A9.md`, `fresh-check-A2.md`, `fresh-check-A6.md` | The three fresh-check reports (Fable 5.1, 28 October 2026) on the rewritten A9, A2 and A6, filed from their chats under P3 (28 October 2026). Each carries the chat link and verdict in its front matter; every finding was applied before the unit was filed. |
| `brand-ai/fresh-check-A1.md` | A1's fresh-check report (Fable 5.1, 29 October 2026; fix, 1 error, 4 should-fix, 6 minor), from its own agent context; every finding applied before filing. |
| `brand-ai/fresh-check-B3.md` | B3's fresh-check report (Fable 5.1, 29 October 2026; fix, 1 error, 4 should-fix, 9 minor), from its own agent context; every finding applied before filing (the rendering finding by a `design/theme.css` rule). |
| `brand-ai/audit-2.md` | Brand + AI Audit 2 report (Fable 5.1, 29 October 2026; B2, B3, B4, A1 all PASS; errata B2-1 to B2-25 and A1-1, applied the same day), from its own agent context, verbatim under a front matter. |
| `brand-ai/fresh-check-B4.md` | B4's fresh-check report (Fable 5.1, 29 October 2026; fix, 0 errors, 7 should-fix, 9 minor), from its own agent context; every finding applied before filing. |
| `brand-ai/fresh-check-DD-B3.md` | DD-B3's fresh-check report (Fable 5.1, 29 October 2026; fix, 1 error, 3 should-fix, 9 minor), from its own agent context; every finding applied before filing. |
| `personal-brand/audit-1.md`, `audit-2.md`, `audit-3.md` | Course PB's stratified-sample Audits 1 to 3 (Fable 5.2, row F-PB, 14 Nov 2026; Audit 3 re-run with search and a full attribution pass on 15 Nov): each its four unit reports verbatim under one front matter, built by `personal-brand/f-pb/tools/build_audits.py`; all twelve units PASS. |
| `personal-brand/audit-4.md` | Course PB's final audit (Fable 5.2, 14 Nov 2026): a full read of the twelve units against the goal; delivers its goal, no REWRITE; verbatim under a front matter. |
| `personal-brand/f-pb/` | Row F-PB's working record: each auditor's report files (`<code>/`), the four first runs without search (`<code>-run1-no-search/`), Audit 4's (`audit-4/`), the errata the chat worked (`chat/`), `applied.json`, `usage.json` and the scripts (`tools/`). Progress: `personal-brand/F-PB-progress.md`. |
| `fable-stage-assessment-2026-11.md` | The cost assessment of the Fable stage after row F-PB (built by `personal-brand/f-pb/tools/assess.py`): per-unit and total tokens, projections for the rest of stage 5, failure rates by stratum, and the recommendation (sample audit with a full attribution pass). |

A fresh check of a later unit is filed the same way, in its course's folder: `<id>/fresh-check-<code>.md` (`<id>` from the course's entry in `kit/courses.py`: `brand-ai`, `ux`), the chat's final report verbatim under a front matter of audit, unit, course, model, date, chat and verdict. This is the one statement of the rule; `skills/audit-units` (§3b: saved before any finding is applied) and `skills/file-unit` (§6: no filing without it) point here.
