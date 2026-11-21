# P-DEC8 · expected differences (written before the change)

Row (docs/BACKLOG.md line 1844): drop the clause "audits are the data file's AUDIT_LOG, the record of the audits run
before the Fable stage closed (S-NOAUDIT, 15 Nov 2026)" from the hnote above the units table of the markdown
'How it was built' page (`kit/howbuilt.py`), where the course has no `[[pack.audit_log]]` rows.

Courses with audit_log rows, by script (`out/DEC-C/audit_rows.py`, reading `courses/*/course.toml`):

| course | audit_log rows |
|---|---|
| brand-ai | 2 (keeps the clause) |
| personal-brand | 4 (keeps the clause) |
| building-with-ai | 0 |
| sport-psychology | 0 |
| supply-chain-execution | 0 |
| ux | 0 |
| greece, rome | history courses, no pack (other page, untouched) |
| _template | 0 (not in any edition) |

Built pages carrying the clause today (grep of kit/academy): brand-a, brand-b, personal-brand-pb,
building-with-ai-bw, sport-psychology-sp, supply-chain-execution-sce, ux-ia.

## Expected changed files

academy (kit/, manifest keys), each by removal of that clause only (the text "; audits are ... 15 Nov 2026)" between
"fresh-check-&lt;code&gt;.md</code>" and "."):

- `academy/building-with-ai-bw/built.html`
- `academy/sport-psychology-sp/built.html`
- `academy/supply-chain-execution-sce/built.html`
- `academy/ux-ia/built.html`

marketing-ai (not in the manifest; compared by building before and after):

- `editions/marketing-ai/building-with-ai-bw/built.html`, the same removal

## Expected unchanged

- academy `brand-a/built.html`, `brand-b/built.html`, `personal-brand-pb/built.html` (courses with rows)
- marketing-ai `personal-brand-pb/built.html`
- every other academy file; greece edition: 0 files differ
- every other marketing-ai file
