---
audit: corrections check
course: supply-chain-execution · Supply Chain Execution for Product Teams
row: W-SCE2
flags: F15
model: Opus 5.5
date: 2026-11-21
chat: https://claude.ai/code/session_01KMmgQyMAq2WNvYqdDDWqnu
result: 1 change, 0 passed, 0 applied
---

The corrections checker's report, verbatim, as it saved it. Saved before anything was applied; nothing was.

## Change 1
File: SCE1-the-map-the-words-and-the-evidence.md
Current:
```
| Cross-docking | Moving goods from receiving to shipping without storing them | Named in de Koster et al. §2.1 [practice]; definition is the course's |
```
Replacement:
```
| Cross-docking | Moving goods from receiving to shipping without storing them | Named in de Koster et al. §2.1 [practice]; described in Bartholdi & Hackman §1.1 [practice] |
```
Result: FAIL. The citation itself holds and needs no new Sources entry (SCE1 already lists release 0.98, "Chapters 1, 3, 4"): §1.1, "Why have a warehouse?" (p. 6), says "each crossdock receives product from many vendors, sorts it, and prepares loads for each store", but nothing in chapter 1 says a crossdock moves goods "without storing them", so the replacement as F15 words it drops "definition is the course's" and leaves the row reading as if the definition were sourced. Keeping "; definition is the course's" at the end of the new cell would pass.
Syllabus: no conflict
