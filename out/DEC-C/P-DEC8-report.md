# P-DEC8 · report (21 Nov 2026, Opus 5.5 agent)

**Verdict: PASSED.** The markdown 'How it was built' page drops the S-NOAUDIT clause where the course has no
`[[pack.audit_log]]` rows; every differing file differs by that clause only; the differing set equals the expected set.

## Steps

1. `python3 kit/baseline.py --check` before the change: `baseline: clean` (academy 457 files, greece 82, 0 differ).
2. `out/DEC-C/expected.md` written before the change. Courses with audit_log rows by script (`out/DEC-C/audit_rows.py`):
   brand-ai 2, personal-brand 4; building-with-ai, sport-psychology, supply-chain-execution, ux, _template 0; greece
   and rome have no pack. Before-copies: `kit/academy` (equal to the manifest, as the check was clean) and a fresh
   `build.py --edition marketing-ai`, both copied to `/tmp/dec8-before/`.
3. Change, `kit/howbuilt.py` `markdown_page`: a local `audit_clause` (the clause text if `d.AUDIT_LOG`, else empty),
   interpolated into the hnote in place of the literal clause. `d` is the pack object already used there
   (`_audit_log_units(d)`); `pack.load` defaults `AUDIT_LOG` to `[]`.
4. `python3 kit/baseline.py --check` after: academy 4 changed (0 added, 0 removed), greece 0:
   - `academy/building-with-ai-bw/built.html`
   - `academy/sport-psychology-sp/built.html`
   - `academy/supply-chain-execution-sce/built.html`
   - `academy/ux-ia/built.html`
   marketing-ai rebuilt after: 1 file differs, `marketing-ai/building-with-ai-bw/built.html`.
5. `python3 out/DEC-C/check_dec8.py /tmp/dec8-before /tmp/dec8-after` (after = symlinks to `kit/academy` and
   `kit/editions/marketing-ai`): for each of the 5 differing files, the before text with the clause removed once
   equals the after text exactly; no file outside expected.md differs; no file added or removed; brand-a, brand-b,
   personal-brand-pb (academy) and personal-brand-pb (marketing-ai) still carry the clause. Output
   `out/DEC-C/check_dec8.out`; word-level diffs `out/DEC-C/diffs/*.worddiff.txt`. Result: PASSED.

## Not done (by instruction)

- Manifest not re-recorded (`kit/baseline.json` unchanged; the main chat re-records after all three rows).
- No `verify.py --full`. No push. The backlog row P-DEC8 is not moved (left to the main chat's §8 close).

Model: Opus 5.5 (claude-opus-5-5).
