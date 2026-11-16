---
audit: fresh check
unit: DD-BW3 · Deep dive: audit your own usage
course: building-with-ai · Building with AI
model: Opus 5.5
date: 2026-11-16
chat: https://claude.ai/code/session_01KMmgR2o4QPEmGVEkBpukcP
verdict: fix · 1 errors, 4 should-fix, 9 minor
---

The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.

Verdict: DD-BW3 · fix · 1 error, 4 should-fix, 9 minor

Checker: claude-opus-5-5 (fresh context; has not seen the unit written). Packet only; web: WebSearch, then WebFetch only of addresses a search returned. All fetches 16 Nov 2026.

## Findings

[error] [figure] §3 "Where each pattern is read" (matrix); Current: "{\"label\": \"By hand\", \"cells\": [{\"mark\": \"group\", \"tone\": 4}, null, null, null, null, null, {\"mark\": \"yes\", \"tone\": 3}, null]}, {\"label\": \"Paid twice\", \"cells\": [{\"mark\": \"group\", \"tone\": 4}"; Problem: the "group" mark (count grouped by task type) on the By hand and Paid twice rows is not in the unit's text: §3 groups by task type only for badly put ("if the heavy chats are mostly one task type") and wrong tool ("those whose task type your routing table puts lower"); By hand is counted per procedure and per skill, Paid twice per question; Part B's template likewise groups only Wrong tool by task type. A figure mark the text does not carry adds a fact; Fix: "{\"label\": \"By hand\", \"cells\": [null, null, null, null, null, null, {\"mark\": \"yes\", \"tone\": 3}, null]}, {\"label\": \"Paid twice\", \"cells\": [null"; Basis: unit §3 "Work done by hand" ("for each procedure ... for each skill") and "Research paid for twice" ("count questions"); sourcing-standard Part 1, figure rule.
[should-fix] [style] §4 BW10 table, rule 3; Current: "Model yes; effort only if recorded. See F81 below"; Problem: "F81" is an internal syllabus-flag code from the project's records; a reader of this public course cannot know it and the course never defines it; the note it means is "A note on rule 3" directly below; Fix: "Model yes; effort only if recorded. See the note on rule 3 below"; Basis: brief ("never refer to the private course"; reader is an outside professional); notes.md "Flags dealt with" (F81 is the writer's flag list).
[should-fix] [accuracy] §1, third reason; Current: "measured, on health and other personal goals, none of them about AI tools"; Problem: the source read (White Rose record of Harkin et al. 2016, per unsure item 4) does not name the kinds of goals; its abstract speaks only of "goal progress", "behavioral performance" and behaviour change, so "health" is not on the page the unit cites; Fix: "measured, on personal goals outside AI use (the repository record does not list their domains), none of them about AI tools"; Basis: https://eprints.whiterose.ac.uk/91437/ (abstract; read 16 Nov 2026).
[should-fix] [accuracy] §7 Ranking; Current: "ties go to the change whose failure reached a finished output (DD-BW2, Deliverable Parts 2 and 4; stated opinion there)"; Problem: (a) the tie rule is in DD-BW2 Part 2 only; Part 4's template states no tie rule; (b) Part B Section 4 then breaks ties "by the corrections in the chats behind them, this unit's addition", which §7 does not mention, so the body and the deliverable give different tie rules; Fix: "ties go to the change whose failure reached a finished output (DD-BW2, Deliverable Part 2; stated opinion there) and, where that does not separate them, to the change with more corrections in the chats behind it (this unit's addition, stated opinion)"; Basis: filed/DD-BW2 Deliverable Part 2 ("ties go to the change whose failure reached a filed text") and Part 4 (no tie rule); unit Part B Section 4 header.
[should-fix] [attribution] §8 On other tools, chat-search row; Current: "| Chat search by topic (§2) | BW1 §3, read 15 Nov 2026 | BW1 §10 | BW1 §10 |"; Problem: BW1 §10 has no chat-search row; its nearest row is memory (ChatGPT "Saved memories and chat history"; Gemini "can look at past chats"), so the pointer claims an equivalent BW1 does not document; Fix: "| Chat search by topic (§2) | BW1 §3, read 15 Nov 2026 | Not checked for this unit (BW1 §10 covers ChatGPT's memory and chat history, not search) | Not checked for this unit (BW1 §10 covers Gemini's reference to past chats, not search) |"; Basis: filed/BW1-mental-model.md §10 table.
[minor] [attribution] §2 Choose a window, rule 1; Current: "because BW8 §7 asks for three runs before a procedure is worth automating"; Problem: BW8 §7 has you count runs and decide by arithmetic; three appears as the rule of three it reports (via Wikipedia) and in "Three runs that each needed different steps are three briefs"; it does not itself set three as the threshold; Fix: "because BW8 §7 has you count runs before automating, and the rule of three it reports extracts a procedure on its third repeat"; Basis: filed/BW8 §7 steps 1 to 3.
[minor] [attribution] §7 What a count can carry; Current: "apply its \"clean sample certifies nothing\" to a pattern you did not find"; Problem: words in quotation marks are not BW6's exact words ("a clean sample is permission to proceed with a stated residual risk, and it certifies nothing"); Fix: "apply its rule that a clean sample certifies nothing to a pattern you did not find"; Basis: filed/BW6 §5 "What a clean sample proves".
[minor] [attribution] Part D, change 2; Current: "Put \"figures and qualifiers the source does not carry\" first"; Problem: the quoted phrase reverses DD-BW2's words, which read "qualifiers and figures the source does not carry"; Fix: "Put \"qualifiers and figures the source does not carry\" first"; Basis: filed/DD-BW2 Deliverable Part 2, change 2.
[minor] [attribution] §5 The export; Current: "Treat it as BW10 §7 treats drafts and working files: a private store you control, read when needed, then deleted."; Problem: BW10 §7 puts drafts and working files in a private store "read by name when needed"; it says nothing about deleting them, so "then deleted" is this unit's rule attributed to BW10 (the next sentence already gives the deletion as advice); Fix: "Treat it as BW10 §7 treats drafts and working files: a private store you control, read by name when needed."; Basis: filed/BW10 §7 table row "Drafts, raw notes, working files".
[minor] [label] §2 label 4, Limits; Current: "(Tamkin et al., preprint), which is the reason this label is the most reliable of the four."; Problem: that Clio computes turns without a model does not make a reader's hand count the most reliable label; the ranking is the unit's inference and is unlabelled; Fix: "(Tamkin et al., preprint). A count needs no judgement, which makes this the most reliable of the four labels (stated opinion)."; Basis: arXiv 2412.13678v1 ("Some facets are computed directly (e.g., number of turns)"), https://arxiv.org/html/2412.13678v1.
[minor] [accuracy] §5 The export; Current: "On claude.ai it holds every conversation and the user data for your account"; Problem: the export page as read on 16 Nov 2026 also lists voice recordings you have shared with Anthropic among the export's contents, which matters for a privacy section about what the export copies; Fix: "On claude.ai it holds every conversation, the user data for your account and any voice recordings you have shared with Anthropic"; Basis: Claude Help Center, Export your Claude data, https://support.claude.com/en/articles/9450526-export-your-claude-data (read 16 Nov 2026; exact wording of the page's list not checked, the fetch returned a summary).
[minor] [style] Opening; Current: "It was written with search off. Seven pages were read on 16 November 2026"; Problem: "search off" followed by seven pages read on the web reads as a contradiction to the reader; the product facts were read live, so the filer should also schedule the staleness re-read the writer asks for (notes, Needs 4) even though the front matter says search: off; Fix: "It was written with search off for drafting; seven pages were read on the web on 16 November 2026"; Basis: unit front matter and opening; notes.md Needs 4.
[minor] [style] Part B Section 4 header; Current: "(DD-BW2 Part 2's rule: the count behind each, largest first; ties broken by the corrections in the chats behind them, this unit's addition; a count of one is a flag)"; Problem: companion to the §7 finding: the header drops DD-BW2's own tie rule while naming it as DD-BW2's rule; Fix: "(DD-BW2 Part 2's rule: the count behind each, largest first; ties to the change whose failure reached a finished output, then to the one with more corrections in the chats behind it, this unit's addition; a count of one is a flag)"; Basis: filed/DD-BW2 Deliverable Part 2.
[minor] [coverage] Part D; Current: "The case's review produced ten ranked changes (Academy case file §8), but the case file does not hold them"; Problem: the brief asks for "the worked example's highest-leverage changes restated"; the case file holds none of them, so Part D restates DD-BW2 Part 2's changes and says so plainly; the substitution is correct under the case-file rule and is the syllabus question the writer raised (notes, Contradictions 1); Fix: "no change required"; Basis: case-academy.md §8; brief.txt.

## Coverage (1)

- Why a review of your own chats finds what a course cannot: covered (§1).
- Method: window, list, classify by task type, model, outcome, turns; each label defined with limits: covered (§2); the row unit and turn definition are stated as the unit's own.
- Patterns (badly put, wrong tool, by hand, research paid twice): covered (§3).
- Testing BW10 and DD-BW1 rules against your record: covered (§4).
- Privacy: covered (§5).
- Worked example, 53 chats over six days, labelled anecdote: covered as far as the case file holds it (§6); thin by necessity, and the unit says what is missing.
- Deliverable: classification sheet (Part A), gap-report template (Part B), sixty-minute procedure (Part C): covered in full, on the case, a labelled neutral example and as templates. Worked example's highest-leverage changes (Part D): substituted by DD-BW2 Part 2's ten, with the reason stated (minor above).
- "On other tools" before the deliverable: present (§8).

## Accuracy (2), from the unsure list

1. Export your Claude data: no file format stated. PASS (confirmed). Path Settings > Privacy > Export data; Free, Pro, Max, Ultra; Team/Enterprise after an Owner enables; excludes original uploaded files; not from iOS/Android; 24 hours, may work only once; "Updated this week": PASS. Exact wording of the two quoted strings: unverifiable (fetch returned a summary); content PASS. Voice recordings omitted: minor above.
2. OpenAI export page: "As of April 11, 2023 ChatGPT users on either free or plus plans can get an export": PASS. Path Settings > Data Controls > Export data; "your chat history in chat.html"; "The link in the email expires after 24 hours"; "Updated over a week ago": PASS.
3. Download your Gemini Apps data: Takeout > My Activity > Gemini Apps; "your Gemini chats, generated media, and uploads"; downloading "doesn't delete it from Google's servers": PASS. Page does not address Activity-on or work accounts, as the writer says.
4. Harkin et al. 2016: Psychological Bulletin 142(2), 198-229; 138 studies, N = 19,951; d+ = 0.40; larger effects when outcomes were "reported or made public" and when information was "physically recorded": PASS. "health" goals: not on the record read (should-fix above).
5. Chatterji et al., NBER w34255, September 2025: "Practical Guidance," "Seeking Information," and "Writing" ... "nearly 80% of all conversations"; non-work "from 53% to more than 70%"; "privacy-preserving automated pipeline"; authors as listed: PASS.
6. Clio, arXiv 2412.13678v1, 18 Dec 2024: one million Claude.ai Free and Pro conversations; turns "computed directly"; 94% on a synthetic dataset; "without the need for human reviewers to read raw conversations"; clusters retained only above minimum sizes for unique accounts and conversations; outputs "preliminary and require additional validation"; first six authors as listed, all Anthropic: PASS.
7. Manage sessions: "a saved conversation tied to a project directory"; JSONL at ~/.claude/projects/<project>/<session-id>.jsonl; 30-day retention via cleanupPeriodDays; picker rows (name or generated title, summary or first prompt, time since last activity, git branch, file size); Ctrl+A to every project; /export to plain text; entry format "internal to Claude Code and changes between versions"; desktop app, claude.ai/code and VS Code keep their own lists; page covers the CLI: PASS.
8. Labelling-time estimates and minute allocation: labelled as estimates/stated opinion in §2, Part C and the Part C figure caption: PASS.
9. Row-per-chat and turn definition stated as the unit's own, not the case's: PASS.
10. Part D against DD-BW2 Part 2 as filed: all ten grades and unit pointers match; one quotation reversed (minor above): PASS otherwise.

## Figures (3), labels (4)

Every number names its owner: Chatterji (working paper), Clio (preprint, vendor-authored), Harkin (peer-reviewed), vendor pages (dated 16 Nov 2026), case file (section given), neutral example (invented, labelled), arithmetic (labelled). PASS. Anecdote, vendor, preprint and working-paper labels present; the case is labelled "(Academy case)" on first use and as an anecdote in §1, §5, §6, Part A, Part B. Neutral-example tallies recomputed: types 4/3/3/3/2/1 = 16; models 13/3; outcomes 7/6/1/1/1; 41 messages, median 2; 15 corrections, 12 in chats 3, 4, 9, 15; routing 5; skill loaded 1 of 4; Part B change counts (5; 4 holding 12; 3 of 4; 2 with 7; 2 with 5; 2 with 1): all PASS.

## Deliverable (5)

Present in full: definitions, case sheet, invented 16-row sheet with tallies, template; gap report on case, neutral example and template; sixty-minute table with done-when lines; Part D table. Follows from §2 to §7 and is usable alone. PASS, subject to the tie-rule fix.

## Errata and pointers (6)

No audit errata touch this unit (no audit report in the packet; skipped as instructed). Pointers checked against filed/: BW10 Deliverable Part 1 (twelve rules, grades, "What your record shows" column, rule 3 "on most models", rule 6 15× 2025), BW10 §6 (memory entries survive chat deletion), §8 (five questions), §9, Template D; DD-BW1 Part 2 (ten rules, grades, "synthesis"); DD-BW2 §8, §10 (three verdicts; "supports the rules its stages produce numbers for"), Part 1 lines A, B, C, H (exact), I, Part 2, Part 4 (tenth row reserved for "not recorded"); BW3 §3, §6 (three failures; one artefact per brief, documented practice), template 2; BW2 §1, §5, §7, Deliverable rule 2 (escalation, documented practice); BW6 §4, §5 (draw by number, step 3), §6; BW7 §2, §6, §7 (run log, stated opinion, model that ran); BW8 §3, §4 (pass above 0.5; misfires added as rows), §7: PASS except BW8 §7, BW6 §5 quote, BW10 §7, BW1 §10 and DD-BW2 Part 4 tie rule (findings above).

## Viz (7)

1. flow, §2: notes traced ("Take the shorter of four weeks and the most recent thirty to sixty chats"; "both ends of the list checked" in Part C; "rank by the count behind each change, largest first" §7); caption names section and sources; kind fits a sequence. PASS.
2. matrix, §3: kind fits items by sections; caption names §3 and the units; "group" marks on By hand and Paid twice not in text. FIX (error above; replacement given).
3. compare, §6: 31, 18, 4 from "31 chats ran on Opus, 18 on Fable, 4 on both"; caption names §6 and case file §8, labelled anecdote; numbers compared. PASS.
4. flow, Part C: seven steps and minutes match the Part C table; caption names Part C and labels the minutes as stated opinion; sequence. PASS.

## Writer's source errors (8)

notes.md lists none. Nothing to confirm; the case-file §8 counts the unit uses agree with case-academy.md §8 (confirmed). The source unit itself was not in this packet, so the writer's statement that it agrees with §8 was not checked.

## Sourcing standard Part 1 and Part 6 (9)

Part 1: sourced in place: yes; openable references: yes; source says what the claim says: yes except Harkin "health" and the pointer stretches above; reporter kept separate: yes (DD-BW1, DD-BW2 cited as units); numbers owned: yes; quotations exact: two quotations of course units not exact (minor above), vendor quotes checked verbatim where the fetch allowed; nothing invented: none found; figures add no fact: one fails (error above); unsourced said so: yes ("not in the case file", "not checked"); Sources list complete and nothing extra: yes; closing material agrees with body: yes once the tie rule is aligned.
Part 6: source classes labelled (preprint, working paper, vendor dated, peer-reviewed): yes; evidence grades: yes; study's models and task named, transfer marked as inference: yes (Chatterji ChatGPT consumer; Clio Claude.ai; Harkin non-AI, inference stated); product facts dated: yes (16 Nov 2026; BW1's 15 Nov); "On other tools": present, with "not checked" where not read; private-course material: none; never refers to the private course: yes, apart from the internal flag code "F81" (should-fix above); Academy facts all in case file with section, labelled, never sole support: yes; no uncited figures: yes; deliverable on case or labelled neutral example plus template: yes; not advice without evidence: yes; links as links: yes.

## Reader pass and privacy (10)

Read as the brief's reader: everything rests on earlier units by code and section, which this reader has read in order. One leak: "See F81 below" (should-fix above). "Fable" and "commit trailers" are in the case file and BW2; acceptable. No detail identifies a private person, his projects or tools beyond case-academy.md: the unit uses only the header, §1, §2, §7, §8, §9.

## Attribution pass (11)

Sources titles against headlines: Export your Claude data; Manage sessions; How do I export my ChatGPT history and data?; Download your Gemini Apps data; Clio: Privacy-Preserving Insights into Real-World AI Use; How People Use ChatGPT; Does Monitoring Goal Progress Promote Goal Attainment? A Meta-Analysis of the Experimental Evidence: all PASS. Quotations against speakers: Chatterji abstract, Clio abstract and method, Claude Code page, OpenAI page, Gemini page: PASS; Claude export quotes: unverifiable wording; DD-BW1 rule 6 quote PASS; DD-BW2 line H quote PASS; BW6 and DD-BW2 Part 2 quotes inexact (minor). Figures against pages: all PASS.

## Confirmed

- Chatterji et al., NBER WP 34255, Sept 2025: three topics nearly 80%; non-work 53% to more than 70%; privacy-preserving automated pipeline; author list. https://www.nber.org/papers/w34255
- Tamkin et al., Clio, arXiv 2412.13678v1, 18 Dec 2024: one million Free and Pro conversations; turns computed directly; 94% synthetic reconstruction; no human reading of raw conversations; cluster minimums; preliminary outputs. https://arxiv.org/html/2412.13678v1
- Harkin et al., Psychological Bulletin 142(2), 2016, 198-229: 138 studies, N = 19,951, d+ = 0.40; moderators physically recorded, reported or made public. https://eprints.whiterose.ac.uk/91437/
- Claude export: path, plans (Free, Pro, Max, Ultra; Team/Enterprise via Owner), no uploaded originals, not from mobile apps, 24-hour single-use link, no format stated, "Updated this week". https://support.claude.com/en/articles/9450526-export-your-claude-data
- Claude Code sessions: definition, JSONL path, 30-day cleanupPeriodDays, picker rows, Ctrl+A, /export plain text, internal format warning, separate lists on desktop, web and VS Code. https://code.claude.com/docs/en/sessions.md
- OpenAI export: Data Controls path, chat.html, 24-hour link, Free and Plus as of 11 April 2023, "Updated over a week ago". https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data
- Gemini Takeout: My Activity > Gemini Apps; chats, generated media and uploads; download does not delete from Google's servers. https://support.google.com/gemini/answer/16920332
- Case file §8 figures: 53 chats, six days, whole history; 31/18/4 from commit trailers; four labels by hand; "accepted" proxy; 14 endings not seen; ten ranked changes; §7 "fable" resolution; header "with private details removed"; §9 effort not recorded. case-academy.md
- Arithmetic: 31 + 18 + 4 = 53; 14 / 53 = 26%; 12 + 10 = 22 verdicts; all neutral-example tallies.

DD-BW3 · fix · 1 error, 4 should-fix, 9 minor
