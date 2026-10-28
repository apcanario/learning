# Brief for an overlap checker (Greek 13.3, Rome 14.3)

You check whether a later report repeats, deepens or contradicts an earlier one. You write one Markdown file and change nothing else. You never edit a report.

Kit folder: the path you are given (`KIT`). Paths are relative to it. Reports are `greece/r-<id>.html` and `rome/r-<id>.html`; prompts are `prompts-greece.json` and `prompts-rome.json` (entry `<id>`, field `prompt` or similar; the prompt is each report's contract).

## For each pair you are given (earlier → later)
1. Read both reports in full, body only (stop at the Self-test). Read both prompts.
2. Go through the later report section by section (each h2) and classify it as **new** (material the earlier report does not have), **deeper** (a point the earlier report made, now extended: say exactly what is added), or **repetition** (the earlier report already says this at the same depth). Where a section mixes classes, split it by paragraph. Estimate the share of the later report's body in each class, by word count, to the nearest 5 percent.
3. List every **contradiction** between the two reports: a date, number, name, attribution or verdict given differently. For each say which report is right and name the source that shows it (ancient author and passage, or modern work). If neither is clearly right, say "open" and why.
4. Where the same **dispute box** appears in both (same scholars, same question), say so: the rule is one home and pointers.
5. Verdict by the syllabus rule: a deep dive earns its place if at least 70 percent is new or deeper and there are no unresolved contradictions; a cross-course pair passes if under 15 percent of the later report repeats the earlier; a core pairing (two survey modules sharing ground) passes if under 15 percent repeats and the two divide the subject cleanly. If a pair fails, name the sections to cut and what should replace them.
6. Every proposed edit must be an exact replacement: current text copied verbatim from the HTML (so `s.count(old) == 1` would hold), corrected text, source.

## Output
Write the file you are told to, in this shape, one section per pair:

```
# <Course> <module>: overlap check, <earlier> → <later>

Run with Fable 5.1, 27 October 2026.

## <earlier id> <title> → <later id> <title>
Mechanical: <the shared-shingle and name-Jaccard figures you are given>.
| Section of later report | Class | What is added (if deeper) / what is repeated |
Shares: new n % · deeper n % · repetition n %.
Contradictions:
| # | Earlier says | Later says | Right | Source |
Shared dispute boxes: <none / list>.
Verdict: pass / fail, one sentence.
Edits (exact replacements): <table or "none">.
```

Be terse. Do not praise. Do not edit any file but your own output. When done, reply with only: per pair, the three shares, the number of contradictions, and the verdict.
