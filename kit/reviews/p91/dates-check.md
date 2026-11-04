# P91 step 2 · ten dates checked by hand against the session text

`p91_dates.py --write` filled `provenance.json`'s `written` map (157 reports, every Greece and Rome report) and its `written_approx` lists (80 reports, sessions 1 and 4, which span days); its printed mapping is `dates-mapping.txt`. No report is left undated. Every session's count matched the rise its "At a glance" row shows (the script stops otherwise). Ten entries, each read against `kit/CHANGELOG.md` (line numbers at commit of this step):

| # | Report | Script | Session text | Agrees |
|---|---|---|---|---|
| 1 | Greece 0.1 | 2026-10-22, approximate (session 1) | Session 1, "22 to 24 October 2026", line 879: "**Units 0 to 2:** twelve reports written in parallel". The session spans three days, so its first day, marked approximate. | yes |
| 2 | Greece 10.7 | 2026-10-22, approximate (session 1) | Session 1: unit 10 is "Deep dive I, the Trojan War (unit 10, 12 modules)", and line 898: "Troy was written in two halves: 62 of 70 reports". | yes |
| 3 | Greece 11.6 | 2026-10-22, approximate (session 1) | Session 1, line 899: "**24 October:** Alexander, 11.1 to 11.8". The text gives the day itself (24 October); the row's rule gives a multi-day session its first day and marks it approximate, so 22 October, marked approximate. Recorded as a choice in the session entry. | yes, by the rule |
| 4 | Greece 12.4 | 2026-10-25 (session 6) | Session 6, "25 October 2026", line 774: "**Deep dive III, Greek philosophy (12.1 to 12.8):**". | yes |
| 5 | Rome 1.4 | 2026-10-24 (session 2) | Session 2, "24 October 2026", line 856: "**Units 0 to 3:**" (19 reports; At a glance 19). | yes |
| 6 | Rome 4.3 | 2026-10-24 (session 3) | Session 3, "24 October 2026", line 836: "**4.1 to 4.5:** Carthage and Dido; … Hannibal and the Second". | yes |
| 7 | Rome 6.2 | 2026-10-24, approximate (session 4) | Session 4, "24 to 25 October 2026", line 815: "**Unit 6, Augustus (6.1 to 6.4):**". Spans two days: first day, approximate. | yes |
| 8 | Rome 7.5 | 2026-10-25 (session 5) | Session 5, "25 October 2026": the title's "Rome unit 7", and line 794: "7.1 to 7.5, about 15,500 words". | yes |
| 9 | Rome 13.2 | 2026-10-25 (session 6) | Session 6, line 771: "**10.5 (the capstone exam), 13.1 and 13.2:** written, but their checks were stopped by the interruption". | yes |
| 10 | Rome 12.6 | 2026-11-01 (session 40) | Session 40, "1 November 2026", its title "11.7, 11.8, 12.1 to 12.8, 13.3 to 13.8", and line 312: "12.6 The gods of the Aeneid: 3,749; fix (1, 5, 6)". | yes |

Ten of ten agree. Not used as a filing: session 1's "**Unit 12, a quality audit (12.1 to 12.5),** was added to the syllabus" (the old audit unit, renumbered 13 in session 5; the script skips a lead line that concerns an audit), and every lead line that repoints or logs (session 40's "**Units closed.**").
