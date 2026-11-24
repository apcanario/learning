# Corrections SCE6 needs in SCE1 (for the BACKLOG's Corrections; not applied in W-SCE6)

Source: SCE6 notes, contradiction 1 (a filed row now out of date, not a mistake), with the C8 cell brought into line with SCE6 §10 as fixed by the fresh check (findings 6 and 7). Where the writer's draft said "ERP studies find customisation raises later maintenance (Light 2001, abstract ...)", the fresh check found that Light's abstract reports no rise in cost (finding 6), so the cell below follows the fixed §10. Each Current was counted in the repo's SCE1 file on 24 Nov 2026 and occurs once. Target: courses/supply-chain-execution/SCE1-the-map-the-words-and-the-evidence.md.

## C-SCE6-1 (SCE1 §11, row C8)

Current:
```
| C8 | Cloud software means no more upgrades. | Not searched here. | SCE6 |
```
Replacement:
```
| C8 | Cloud software means no more upgrades. | Tested in SCE6 §10: no source opened says upgrades end in the cloud. NIST's definition of SaaS (SP 800-145, 2011) gives the provider control of the application and the customer only limited user-specific configuration settings [independent], so the upgrade moves to the provider (inference); Gartner's 2022 WMS Magic Quadrant, read in a reprint, says service affects "upgrade cycles and TCO", calls multitenant against dedicated cloud a continuing debate, and says some vendors' microservices architecture "allows continuous upgrades" [analyst]; an ERP review finds SaaS limits deep customisation and moves it to interfaces (Abendroth et al. 2024) [independent], and Light (2001, abstract only) found a customisation needs careful consideration for its impact on future maintenance [independent]. No independent source found. | SCE6 |
```

## C-SCE6-2 (SCE1 front matter intro, claims sentence; only together with C-SCE6-1)

Current:
```
 C1, C2 and C10 are set against what was opened here, C4 against SCE4, and C3, C5 and C6 against SCE5; the other seven are marked "not searched here" with the unit that tests each.
```
Replacement:
```
 C1, C2 and C10 are set against what was opened here, C4 against SCE4, C3, C5 and C6 against SCE5, and C8 against SCE6; the other six are marked "not searched here" with the unit that tests each.
```

## C-SCE6-3 (SCE1 Sources: the four sources C-SCE6-1 cites; sourcing-standard Part 1, as C-SCE5's New item 1)

Current:
```
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 1, 3, 4 and bibliography. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
```
Replacement (Abendroth inserted before it, copied from SCE6 Sources):
```
- Abendroth, A., Bender, B. & Gronau, N. (2024). The Evolution of Original ERP Customization: A Systematic Literature Review of Technical Possibilities. In *Proceedings of the 26th International Conference on Enterprise Information Systems (ICEIS 2024)*, vol. 1, 17–27. https://doi.org/10.5220/0012305500003690 (read at https://scitepress.org/Papers/2024/123055/123055.pdf)
- Bartholdi, J. J., III & Hackman, S. T. *Warehouse & Distribution Science*, release 0.98, revised 28 August 2017. Chapters 1, 3, 4 and bibliography. https://www2.isye.gatech.edu/~jjb/wh/book/editions/wh-sci-0.98.pdf
```

Current:
```
- Gartner. Magic Quadrant and Critical Capabilities index (no headline shown), read 21 November 2026. https://www.gartner.com/magic-quadrant
```
Replacement (the 2022 report added after it, copied from SCE6 Sources):
```
- Gartner. Magic Quadrant and Critical Capabilities index (no headline shown), read 21 November 2026. https://www.gartner.com/magic-quadrant
- Gartner. "Magic Quadrant for Warehouse Management Systems". S. Tunstall, D. Klappich, R. Narang. Published 1 June 2022, ID G00755323. Reprint, read by SCE6 on 24 November 2026. https://dam.infor.com/api/public/content/d8957bc1ac164bf1843965deeaa7e26a?v=d2e94df6
```

Current:
```
- Meyr, H., Wagner, M. & Rohde, J. "Structure of Advanced Planning Systems".
```
Replacement (Light and Mell & Grance inserted before it, copied from SCE6 Sources):
```
- Light, B. (2001). The maintenance implications of the customization of ERP software. *Journal of Software Maintenance and Evolution: Research and Practice* 13(6), 415–429. https://doi.org/10.1002/smr.240 (abstract, read at https://salford-repository.worktribe.com/output/1471899/the-maintenance-implications-of-the-customization-of-erp-software)
- Mell, P. & Grance, T. *The NIST Definition of Cloud Computing*. NIST Special Publication 800-145, September 2011. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-145.pdf
- Meyr, H., Wagner, M. & Rohde, J. "Structure of Advanced Planning Systems".
```

Notes for the corrections checker: SCE1's Sources line says "All addresses opened on 21 November 2026"; the four entries were opened by SCE6 on 24 November 2026, so the checker may want "(opened by SCE6, 24 Nov 2026)" on each. The 2022 reprint address is on a vendor's asset server (F1 note); the private-terms check runs on SCE1 at build like any page. The journal title of Light (2001) differs between the Salford record and the Utah index (fresh check, Could not verify).
