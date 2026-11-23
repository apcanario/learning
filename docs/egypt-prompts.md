# Prompts: Egyptian history and mythology

Sections 0 to 7 are the design's prompts file of 21 Nov 2026 (Fable 5.2), filed by row S-EG0 on 23 Nov 2026 with two kinds of edit and no other: "the owner" for the owner's first name, and Part 12 of `docs/sourcing-standard.md` where the design said Part 9 (Parts 9 to 11 were taken by other courses by the day; override 1 of row S-EG0). The writing template that `kit/next_prompt.py` prints follows them.

## 0 · The run plan (the owner, 21 Nov 2026)

These rules govern every chat of this course. Where the copied template says otherwise, these win, and S-EG0 changes the template to match.

1. **Clone line.** Every prompt meant to be pasted into a session, the setup prompt, the starter and each row's prompt as `kit/next_prompt.py` prints and saves it, opens with exactly this line and says nothing else about cloning, attaching the repo, add_repo, registering it or approval:
   `Clone apcanario/learning (shallow, push access).`
2. **Setup runs alone.** Row S-EG0 files the design, builds, verifies and publishes, and writes no unit. In `kit/next_prompt.py` it only adds the course to `QUEUE`, and it checks that another course's row prints byte-identical before and after. No `HOLDS` or `GATES` entry.
3. **Bundles of four.** After setup, the course is written in chats of four units each, in writing order; the last chat takes what is left. Each is a thin Sonnet 5.5 main chat with fresh Opus 5.5 agents, run with `python3 kit/next_prompt.py --bundle 4`: each unit is checked, filed, landed and published before the next begins, so a chat that stops strands nothing.
4. **One starter.** Every writing chat starts from the same two lines (section 6), which also resume a chat that stopped part-way.
5. **No gate rows.** A point where the owner reads before more is written sits on a bundle boundary; his starting the next chat is the go. Nothing for him to close by hand.
6. **Closing corrections.** The last chat works every correction and flag still open itself, and delivers a closing prompt only if something remains, saying why.
7. **Replies.** A chat's one reply ends with the starter in a code block, not a long prompt. A task is left for the owner only where no agent can do it. Proposals are worked in the next row unless he vetoes them.
8. **Record.** The chats are in the syllabus's order section (§5), the backlog's writing rows are grouped the same way, and these rules stand here.

**The chats.** Setup, then twenty bundles: 78 units in writing order, which is the code order.

| Chat | Rows | Units |
|---|---|---|
| Setup | S-EG0 | none: files the design |
| Bundle 1 | W-EG1, W-EG2, W-EG3, W-EG4 | EG1, EG2, EG3, EG4 |
| Bundle 2 | W-EG5, W-EG6, W-EG7, W-EG8 | EG5, EG6, EG7, EG8 |
| Bundle 3 | W-EG9, W-EG10, W-EG11, W-EG12 | EG9, EG10, EG11, EG12 |
| Bundle 4 | W-EG13, W-EG14, W-EG15, W-EG16 | EG13, EG14, EG15, EG16 |
| Bundle 5 | W-EG17, W-EG18, W-EG19, W-EG20 | EG17, EG18, EG19, EG20 |
| Bundle 6 | W-EG21, W-EG22, W-EG23, W-EG24 | EG21, EG22, EG23, EG24 |
| Bundle 7 | W-EG25, W-EG26, W-EG27, W-EG28 | EG25, EG26, EG27, EG28 |
| Bundle 8 | W-EG29, W-EG30, W-EG31, W-EG32 | EG29, EG30, EG31, EG32 |
| Bundle 9 | W-EG33, W-EG34, W-EG35, W-EG36 | EG33, EG34, EG35, EG36 |
| Bundle 10 | W-EG37, W-EG38, W-EG39, W-EG40 | EG37, EG38, EG39, EG40 |
| Bundle 11 | W-EG41, W-EG42, W-EG43, W-EG44 | EG41, EG42, EG43, EG44 |
| Bundle 12 | W-EG45, W-EG46, W-EG47, W-EG48 | EG45, EG46, EG47, EG48 |
| Bundle 13 | W-EG49, W-EG50, W-EG51, W-EG52 | EG49, EG50, EG51, EG52 |
| Bundle 14 | W-EG53, W-EG54, W-EG55, W-EG56 | EG53, EG54, EG55, EG56 |
| Bundle 15 | W-EG57, W-DD-EG1, W-DD-EG2, W-DD-EG3 | EG57, DD-EG1, DD-EG2, DD-EG3 |
| Bundle 16 | W-DD-EG4, W-DD-EG5, W-DD-EG6, W-DD-EG7 | DD-EG4, DD-EG5, DD-EG6, DD-EG7 |
| Bundle 17 | W-DD-EG8, W-DD-EG9, W-DD-EG10, W-DD-EG11 | DD-EG8, DD-EG9, DD-EG10, DD-EG11 |
| Bundle 18 | W-DD-EG12, W-DD-EG13, W-DD-EG14, W-DD-EG15 | DD-EG12, DD-EG13, DD-EG14, DD-EG15 |
| Bundle 19 | W-DD-EG16, W-DD-EG17, W-DD-EG18, W-DD-EG19 | DD-EG16, DD-EG17, DD-EG18, DD-EG19 |
| Bundle 20 | W-DD-EG20, W-DD-EG21 | DD-EG20, DD-EG21 |

**The template.** The writing template is not rewritten here. The repo holds a working one for a course of the same build, `docs/supply-chain-execution-prompts.md`, already corrected to the kit by two rows. S-EG0 copies it to `docs/egypt-prompts.md`, replaces its course-specific parts with sections 1 to 4 below, replaces its opening clone sentence with the clone line (rule 1), and makes its Reply and its next-prompt step follow rules 6 and 7. Everything else in the template (the thin chat's rules, the agent rules, the web rule, the scripts, the checkpoint commits, `kit/land.py`, the publish, the close) stays as the repo has it on the day S-EG0 runs.

## 1 · Writer rules

The writer is one fresh Opus 5.5 agent with its packet and nothing else. One writer per module.

1. **Open before citing.** Every reference is found by a search and read at its publisher's page, its DOI address, an open-access repository or the holding institution's own page before it carries a claim. The seed bibliography says only that an entry is believed to exist.
2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (full text, chapter, abstract, catalogue record), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the work's own title; a figure is cited to the work that reports it, not to one that repeats it; each Sources entry is checked against the publisher's record before hand-in.
3. **Where to look first.** The UCLA Encyclopedia of Egyptology; the open publications of ISAC (Chicago), the Metropolitan Museum, the IFAO and the Egypt Exploration Society; the journal article at its DOI; the museum's own record for an object; the mission's own page for a site. A book that will not open is not cited from memory: use an opened reporter (a peer-reviewed review, an encyclopaedia article), named as the reporter, or leave the name out and state the view unattributed with its grade.
4. **Egyptian texts.** Cite by standard designation and by the translation opened; name the translator. Quote only what was read, under 15 words. Never Budge.
5. **Later sources are later.** State the gap in centuries whenever Manetho, a king list, a classical author or a Ptolemaic temple text is used for an earlier period.
6. **Dates and numbers.** Every date before 664 BC is approximate and follows EG3's convention; a disputed one gives the range. Every number names whose figure it is.
7. **Grade every claim** by EG1's key. From EG2 on, the key arrives in the packet inside EG1.
8. **Dispute boxes.** Wherever sources or scholars differ: a paragraph opening `**Where sources disagree.**`, a named source or scholar on each side, each from an opened text. Several per module.
9. **Claims under examination.** A popular or fringe claim is stated as it circulates, attributed to the kind of source that makes it, set against the evidence, graded, and not mocked. Its promoters' books, sites and films are not Sources.
10. **Faith and identity.** In EG23, EG28, EG56, DD-EG10 and DD-EG21: evidence and named positions; no confession or camp argued for.
11. **Lane.** Every module before this one is filed and in the packet: point to it by code, do not retell it, and open it first. The modules after it are not written: the brief's "Not here" line names what is theirs; give it a sentence and hand off by code. Greek and Roman modules are pointed to by their dotted codes, after opening the copy in `other-courses/`; one that is not in the packet is not pointed to, and the missing module is listed under Needs. A name keeps the English form the first filed module gave it.
12. **Anatomy and style.** `kit/AGENT-SPEC.md`: the forms allowed, 6 to 10 sections, the Self-test (10) and Carry forward (3) with their exact headings, the brief's own deliverable placed before the Self-test. British spelling, no em dashes, no emoji, no preamble. Signs by Gardiner number and description (flag F1).
13. **Figures.** After the draft, the figure pass of `skills/write-unit` §4b. A king list or a sequence of events is a timeline; a line of descent is a tree; competing estimates are a range. Every label and number is already in the sourced text.
14. **Flags and corrections.** A contradiction with a filed module or a brief, a mistake noticed in a filed module (this course's, or a Greek or Roman one), a brief that names a source, number or passage the opened evidence does not bear out, or a need the syllabus does not meet, goes to `out/notes.md`: under **Contradictions** with the quoted passage, what is wrong, the source and the exact replacement; under **Needs** with every module it affects and a proposed change. The writer never rewords a brief; it writes what the evidence carries and flags the brief.
15. **Hand-in.** `out/unit.md` (front matter, the module, the deliverable, Self-test, Carry forward, Sources); `out/sources.md`; `out/notes.md` with **Case facts** written as "none" (the course has no case), **Contradictions** and **Needs**, an empty list written as "none"; the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, references opened and not opened, brief items it could not source).

## 2 · The fresh checker's seven passes

One fresh Opus 5.5 agent per module, with live search, that has not seen the module written. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.

1. **References exist and match.** Every Sources entry against its publisher's or Crossref's record.
2. **Claims against sources.** Every cited claim opened and read against its source; "unverifiable" where the source will not open, never a pass. Every designation of an Egyptian text (utterance, spell, chapter, papyrus, museum number) against an opened edition, translation or record.
3. **Grades.** Each grade against EG1's key. A later source never grades as attested; an announcement never grades above announced; a single scientific study is scientific, not consensus.
4. **Time and number.** Every date before 664 BC approximate and on EG3's convention; every gap between source and event stated; every number with its owner.
5. **Names and positions.** Every view attached to a scholar found in that scholar's opened text or in the named reporter; every dispute box with someone on each side; no claim under examination left standing as fact.
6. **Lane, pointers, tone.** Nothing retold from a filed module, and no fact (a date, a number, a spelling of a name, a museum number) stated differently from a filed module without a flag; nothing taken from a later module's lane beyond a sentence; every pointer opened and true; the preamble's tone and style rules; the faith-and-identity rule where it applies.
7. **Closing material and figures.** The brief's deliverable built in full; ten Self-test questions whose answers agree with the body; three Carry forward ideas; every figure's labels and numbers traced to the text.

It also runs the module against Part 12 line by line.

## 3 · This row in particular

One paragraph per row, read by `kit/next_prompt.py` and printed in that row's prompt.

| Row | Paragraph |
|---|---|
| W-EG1 | Search off. First unit of the course. It sets the grade key every later module receives: define each of the seven grades so that two readers would agree, with a test and one worked Egyptian example each. |
| W-EG2 | Search off. EG3 fixes the chronology the course follows and the form of an approximate date; EG2 fixes the English form of every site name. Later writers take both tables from the filed modules. |
| W-EG3 | Search off. EG3 fixes the chronology the course follows and the form of an approximate date; EG2 fixes the English form of every site name. Later writers take both tables from the filed modules. |
| W-EG4 | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG5 | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG6 | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG7 | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG8 | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG9 | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG10 | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG11 | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG12 | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG13 | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. |
| W-EG14 | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. |
| W-EG15 | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. |
| W-EG16 | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 1.1 from `courses/greece/`. |
| W-EG17 | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 1.1 from `courses/greece/`. |
| W-EG18 | Search on. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG19 | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG20 | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG21 | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG22 | Search off. Royal inscriptions are read as rhetoric, and the module says so. |
| W-EG23 | Search off. Royal inscriptions are read as rhetoric, and the module says so. The faith-and-identity rule applies (writer rule 10). |
| W-EG24 | Search off. Royal inscriptions are read as rhetoric, and the module says so. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 1.3 from `courses/greece/`. |
| W-EG25 | Search off. Royal inscriptions are read as rhetoric, and the module says so. |
| W-EG26 | Search off. Royal inscriptions are read as rhetoric, and the module says so. |
| W-EG27 | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. |
| W-EG28 | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. The faith-and-identity rule applies (writer rule 10). |
| W-EG29 | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 5.2 from `courses/greece/`. |
| W-EG30 | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 11.3, 6.2, 6.7 from `courses/greece/`. |
| W-EG31 | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 0.1 from `courses/greece/`. |
| W-EG32 | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 6.7 and 11.4, 7.1 and 7.2 from `courses/greece/`. |
| W-EG33 | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Rome 2.5 from `courses/rome/`. |
| W-EG34 | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Rome 5.5 from `courses/rome/`. |
| W-EG35 | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.2 from `courses/greece/`; Rome 2.5, 8.4 from `courses/rome/`. |
| W-EG36 | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.1 from `courses/greece/`; Rome 2.1 from `courses/rome/`. |
| W-EG37 | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 2.1 from `courses/greece/`. |
| W-EG38 | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG39 | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG40 | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG41 | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG42 | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.4 from `courses/greece/`; Rome 2.4 from `courses/rome/`. |
| W-EG43 | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG44 | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG45 | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG46 | Search on. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG47 | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.1 from `courses/greece/`. |
| W-EG48 | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. |
| W-EG49 | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. |
| W-EG50 | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.5 from `courses/greece/`; Rome 9.3 from `courses/rome/`. |
| W-EG51 | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. |
| W-EG52 | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 5.6 and 12.1 from `courses/greece/`. |
| W-EG53 | Search off. Flag F1: signs by Gardiner number and description. |
| W-EG54 | Search off. Flag F1: signs by Gardiner number and description. |
| W-EG55 | Search on. Flag F1: signs by Gardiner number and description. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 9.1 from `courses/greece/`; Rome 10.3 from `courses/rome/`. |
| W-EG56 | Search on. Flag F1: signs by Gardiner number and description. The faith-and-identity rule applies (writer rule 10). Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 9.3 from `courses/greece/`; Rome 10.4 from `courses/rome/`. |
| W-EG57 | Search off. Last unit of the core. Written from the filed modules only: the chat adds to the packet every filed module's Carry forward and Self-test sections. It adds no claim. |
| W-DD-EG1 | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG2 | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG3 | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG4 | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG5 | Search on. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG6 | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG7 | Search off. Written from DD-EG1 to DD-EG6 as filed. The claims audit treats each claim on its evidence and mocks none. |
| W-DD-EG8 | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG9 | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG10 | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. The faith-and-identity rule applies (writer rule 10). |
| W-DD-EG11 | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG12 | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG13 | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG14 | Search off. Written from DD-EG8 to DD-EG13 as filed. |
| W-DD-EG15 | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG16 | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG17 | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG18 | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG19 | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG20 | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG21 | Search off. The last unit of the course, written from EG42 to EG46 and DD-EG15 to DD-EG20 as filed. After it is published, this chat works the closing corrections (section 4, point 7). The faith-and-identity rule applies (writer rule 10). |

## 4 · The carry-forward rule (the owner, standing), as this course runs it

Nothing found goes unrecorded or waits for a later audit. It applies to every row of this course, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a module is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or the owner.
2. **About a module already filed** (this course's, or a Greek or Roman module a writer opened). It goes into the next row's prompt as a correction, with the module, the passage, what is wrong and the source. The next row fixes it first, before it writes: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About a module not yet written.** It becomes a flag in `courses/egypt/notes/syllabus-flags.md` naming every module it affects, and it is printed in each of those modules' prompts as a guideline. A flag that would change a brief is proposed, never applied by the chat that raised it.
4. **About the module being written.** It is fixed in the same row before filing. What cannot be fixed (a source that will not open) is cut or marked unverified in the module, and carried as in 2.
5. **The next row's prompt always exists.** Every row saves the next row's prompt into its row of `docs/BACKLOG.md` (`kit/next_prompt.py --save`), already holding every correction still open, every open flag that names that unit, every carried proposal, and any guideline of the template that the row showed needs updating, with the update made in `docs/egypt-prompts.md`. Inside a bundle the chat prints and works it itself. The chat's reply does not print it: the reply ends with the starter (rule 7 of the run plan), and the starter prints it.
6. **Nothing is dropped silently.** A correction or flag leaves the prompt only when it is resolved, with the row and the report that resolved it written beside it.
7. **The last chat** (bundle 20, after W-DD-EG21 is published) works every correction and flag still open itself, under the same limits as any corrections step. It delivers a closing prompt only if something remains, with the reason each item could not be closed; if nothing remains, the reply says the course is complete and ends without a starter.

## 5 · When a chat stops, and where the owner reads

A bundle runs its four rows one after another, each to its publish. It stops before its fourth row is closed only when: the session's permission check refuses a repo script; an agent states a model that is not Opus 5.5; a unit gets a second `rewrite` verdict; `verify.py` fails twice on the same check. It then says why in one line, and its reply still ends with the starter, which resumes at the first unit not filed. It never stops to ask a question.

There is no gate row. Two bundle boundaries are worth a read, and starting the next chat is the go:

- **After bundle 1** (EG1 to EG4). The reply states, per unit, the references opened and not opened and the brief items that could not be sourced. This is the test of the access rule: if writers could not open enough, say so before starting bundle 2, and the next chat begins with the change.
- **After bundle 15** (EG57 and the first deep-dive units). The core is complete.

**What the owner does by hand:** paste the setup prompt once. After that the chats schedule one another (section 5b); he pastes the starter only where a chat could not schedule the next, or to resume one that stopped. No file to attach, no gate to close, no proposal to confirm.

## 5b · Scheduling the next bundle (P-EG7, accepted by the owner, 21 Nov 2026)

1. **At its close**, after its last unit is published and the row closed, the setup chat and every bundle but the last looks for a scheduling tool that starts a new chat in this Project. If it has one, it schedules one run, ten minutes later, whose prompt is the starter (section 6), word for word, and nothing else.
2. **The reply says** that the next bundle is scheduled and for when, and which approval setting the scheduled chat got. It still ends with the starter in a code block.
3. **Model guard.** A chat started by a schedule states its model first. If it is not Sonnet 5.5, it changes nothing, says so in one line and stops; nothing is rescheduled. The pasted starter then runs that bundle.
4. **No chain after a stop.** A chat that stopped for a reason in section 5 schedules nothing. Neither does a chat with no scheduling tool: its reply says so and ends with the starter.
5. **The two read points** (after bundle 1 and after bundle 15) are not held by the schedule: the next bundle starts on its own. To hold one, cancel the scheduled run named in that reply.
6. **The last chat** schedules nothing.

## 6 · The starter

Every writing chat starts from these two lines, in a new chat in the Learning Project. They also resume a chat that stopped part-way.

```
Clone apcanario/learning (shallow, push access).
Egyptian history and mythology, next bundle. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. Run `python3 kit/next_prompt.py --course egypt --bundle 4` and work what it prints in full, unattended.
```

If `kit/next_prompt.py` has no `--course` option when setup runs, the starter is the same two lines with `--row <the first writing row not filed> --bundle 4` in place of `--course egypt --bundle 4`: `--row W-EG1 --bundle 4` from the setup row, and from each bundle's reply the row of the first unit not filed.

## 7 · The setup prompt, row S-EG0

Pasted once into a new chat in the Learning Project, on Sonnet 5.5, alone: no other chat is writing to the repo while it runs.

```
Clone apcanario/learning (shallow, push access).
Row S-EG0, setup of the course Egyptian history and mythology. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. File the design, build, verify, land and publish. Write no unit. Unattended: ask nothing unless a repo script is refused or the design cannot be read.

Run `python3 kit/land.py start S-EG0`. Before changing anything, save the output of `python3 kit/next_prompt.py --row W-DD-SCE2` to a file outside the repo.

The design is one artifact, https://claude.ai/artifact/X6eax4wJ3sycVTD7kWg7ni. Read it with the artifact reader and open its Files tab: four files as text blocks, each under its file name: `egypt-syllabus.md`, `briefs.md`, `egypt-prompts.md` and `bibliography.md`. Save them outside the repo byte for byte and check each against the sha256 printed beside it.

A registrar (a fresh Agent on model opus) does the repo work from those four files and `skills/new-course`; a second fresh Agent on model opus checks the registration and edits nothing. You never open a brief. No brief is reworded, by anyone.

The registrar:
1. Follows `skills/new-course` steps 4 to 6 for a markdown course, id `egypt`, folder `courses/egypt/`, from `courses/_template/`: `briefs.md` as given; `course.toml` and `pages/` from the syllabus (identity §2, goal and outcomes §3, units and Takes lines §4, writing order and search flags §5, decisions §8); `notes/bibliography.md`, `notes/syllabus-flags.md` opened with flags F1 to F5, and an empty `notes/names.md`; private, History track, family label Personal Mythology, after `rome` in `course_order`; Egypt removed from `planned` in `catalog.toml`.
2. Saves the syllabus as `docs/egypt-syllabus.md` and builds `docs/egypt-prompts.md` as the prompts file's section 0 says, with `prompts_doc` set in the course's `course.toml`.
3. In `kit/next_prompt.py`, adds `egypt` to `QUEUE` and changes nothing else: no `HOLDS` entry, no `GATES` entry, no new option. Then `python3 kit/next_prompt.py --row W-DD-SCE2` prints byte for byte what was saved before; if it does not, the change is undone and redone until it does.
4. Works proposals P-EG2 to P-EG6 of the syllabus's §9, each under its warning; after P-EG2, `python3 kit/baseline.py --check` shows no page of another course changed.
5. Checks every entry of the seed bibliography for existence at Crossref's or the publisher's record, corrects the entry to the record, strikes any it cannot find, and writes how each was checked, in the form of `courses/supply-chain-execution/notes/bibliography.md`. It checks no entry for what it says.
6. Adds Part 12 (the design's Part 9) to `docs/sourcing-standard.md`, the Egypt section to `kit/AGENT-SPEC.md`, and the course's section to `docs/courses-index.md` (0 of 78 written; every unit in writing order with model Opus 5.5, its search flag and its vault path).
7. Adds the writing rows W-EG1 to W-EG57 and W-DD-EG1 to W-DD-EG21 to the queue of `docs/BACKLOG.md`, grouped under one heading per chat exactly as the prompts file's section 0 lists them (Bundle 1 to Bundle 20), with W-EG1's prompt saved by `python3 kit/next_prompt.py --row W-EG1 --save`; and an entry in `docs/site-log.md`.
8. Builds and verifies (ALL CHECKS PASSED, `index_check.py`, `private_terms.py`) and looks at the course home at the three widths.

The checker reads the registration against the four files: every brief byte for byte; every unit's title, order, search flag and Takes line; the goal and outcomes; Part 12 against the syllabus's §6; the template's replaced sections, its clone line and its Reply against the prompts file; the backlog's twenty groups; the `next_prompt.py` diff (one added queue entry) and the byte-identical row; and that nothing outside this course changed in the built site except the home's course list. Its findings are fixed before landing.

Then land (`kit/land.py land`), publish Academy once from a fresh build of the landed HEAD (the artifact, read first, then `kit/deploy.sh`), close the row by `docs/method.md` §8 and refresh the Project mirrors, adding the course's three data mirrors.

One reply. It says what was registered, the bibliography entries struck, the proposals raised (worked in W-EG1's row unless I veto), and any task only I can do. It schedules bundle 1 as the prompts file's section 5b says, or says it has no scheduling tool. It ends with the starter in a code block: the two lines of the prompts file's section 6, or, if `kit/next_prompt.py` has no `--course` option, the same two lines with `--row W-EG1 --bundle 4`.
```

---

## Rows W-EG1 to W-DD-EG21 · write one module

Added by S-EG0 (23 Nov 2026): the writing template of `docs/supply-chain-execution-prompts.md` as it stood in the repo on the day (the code block under "Rows W-SCE1 to W-DD-SCE2", with every correction that course's rows made to it: S-SCE0 and its registration check, 19 Nov 2026; W-SCE2, 21 Nov 2026; S-PROMPT1, 22 Nov 2026), taken through the copy `docs/athlete-career-prompts.md` made of it on 23 Nov 2026 (S-AC0), whose changes are the ones section 0 asks for here: the clone line (rule 1) and nothing else about cloning in the three places that spoke of it; step 7's sentence on briefs, step 11's starter rows and the Reply ending with the starter (rules 6 and 7). Then only its course-specific parts were replaced by sections 0 to 4 above: (1) the course's name, "private course" for "public course", its id, code and paths, and its sourcing part (Part 12); (2) the carry-forward rule with section 4, its seven points word for word (the Athlete course's two additions dropped); (3) the writer rules with section 1, its fifteen rules word for word (rule 15 is the course's own hand-in rule, so the Athlete course's rule 16 is not carried); (4) the checker's opening sentence and seven passes with section 2, word for word, its last line naming Part 12; (5) step 2: no case register in the packet, and the Greek and Roman modules a row's paragraph names copied in by the chat under `other-courses/` (section 1, rule 11; section 3; `kit/thin.py` stages no other course's module); (6) step 7: no case facts and no `case_lines` (writer rule 15: Case facts "none"); step 8: the course's front matter (`egypt · EG · Egyptian history and mythology`) and no `case_lines`; (7) step 11 and the Reply name this course (its mirrors, "course EG complete", `--starter egypt`, section 0's rules 3, 4 and 7 for the Athlete course's section 5), and the Reply gains section 5b's scheduling at the chat's close; (8) the row table with section 3 above, word for word, in the four-column form `kit/next_prompt.py` reads (below; the search column from each paragraph's opening "Search on."/"Search off.", which agrees with the course's `order`). The owner's first name, which the design and the Execution template carry, is written "the owner" throughout this file. There is no safety reader and no `GATES` or `HOLDS` entry for this course. Rule 13 of `docs/public-courses.md` (the quality review) applies and is printed by `kit/next_prompt.py` when a module's flags call for it. `kit/next_prompt.py` reads the code block below and the table "This row in particular", fills the slots and prints the result; a row that finds a guideline here wrong corrects it here (section 4, point 5). The template calls a module a "unit", as the kit does.

Slots: `{ROW}` (W-EG4), `{CODE}` (EG4), `{TITLE}`, `{SEARCH}` (on or off), `{PAGE}` (read-eg4), `{SAVE}` (step 11's last clause: the `--save` line, or on the last row the closing corrections prompt), `{SAVEROW}` (step 10's clause on the next prompt), `{NEXTPROMPT}` (the Reply's last item on the last row), `{FILED}` (the paths of this course's filed units), `{FLAGS}`, `{CORRECTIONS}`, `{PROPOSALS}`, `{PARTICULAR}` (the row's paragraph from the table below).

```
Clone apcanario/learning (shallow, push access).
First, run `python3 kit/land.py start <this row>` (it records the start commit and installs the push guard). Row {ROW} of `docs/BACKLOG.md`, in this chat: write, fresh-check and file unit {CODE}, "{TITLE}", of the private course Egyptian history and mythology (`courses/egypt/course.toml`: data `courses/egypt/notes/`, vault `courses/egypt/`, `docs/sourcing-standard.md` Parts 1 and 12; search {SEARCH}); correct every mistake the work finds; flag every contradiction or need that touches another unit; then build, verify, land (`kit/land.py land`), then publish Academy once from a fresh build of the landed HEAD (the artifact, then GitHub Pages), close the row and end the reply with the course's starter line.

Read first: `docs/public-courses.md`, `docs/method.md` §4, §5, §7 and §8, `skills/write-unit`, `skills/audit-units` §3, `skills/file-unit` and the docstring of `kit/thin.py` (the chat reads those, never a unit).

**This is a thin main chat** (method §4). (1) The chat runs on Sonnet 5.5 and the record says which model it ran as. The writer, the fresh checker, the applier, the filer and the corrections checker are each a fresh Agent on model opus, isolated on a packet (the harness may refuse `isolation: worktree`; then the Agent is launched without it and its isolation is the packet folder and its instructions, said in the record). (2) The chat never opens a unit, a report or a brief. It stages each packet with `python3 kit/thin.py stage <writer|checker|applier|filer> --row {ROW} <folder>`, launches the agent, and reads only the agent's reply, at most six lines, and the `out/stats.json` that `python3 kit/thin.py stats <out folder>` writes. Every agent writes its full output to files in its `out/` folder. (3) Scripts, not the chat, check the result: `kit/index_check.py`, `kit/private_terms.py`, the last line of `build.py`, `verify.py`, the publish read-back by sha256. (4) A checkpoint commit follows every agent's return, on `main`; it is landed at step 10 with `kit/land.py` (never a bare push). (5) No unit is uploaded to the Project. If the session's permission check refuses to run the repo's own scripts, stop, say so in one line and ask the owner; never work around it. Where a choice is open, take the most reasonable reading, say so in the record and carry on; ask only if blocked. Fix every error, should-fix and minor finding the work turns up in this chat.

**The carry-forward rule (the owner, standing; `docs/egypt-prompts.md` §4, `docs/method.md` §9).** Nothing found goes unrecorded or waits for a later audit. It applies to every row of this course, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a module is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or the owner.
2. **About a module already filed** (this course's, or a Greek or Roman module a writer opened). It goes into the next row's prompt as a correction, with the module, the passage, what is wrong and the source. The next row fixes it first, before it writes: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About a module not yet written.** It becomes a flag in `courses/egypt/notes/syllabus-flags.md` naming every module it affects, and it is printed in each of those modules' prompts as a guideline. A flag that would change a brief is proposed, never applied by the chat that raised it.
4. **About the module being written.** It is fixed in the same row before filing. What cannot be fixed (a source that will not open) is cut or marked unverified in the module, and carried as in 2.
5. **The next row's prompt always exists.** Every row saves the next row's prompt into its row of `docs/BACKLOG.md` (`kit/next_prompt.py --save`), already holding every correction still open, every open flag that names that unit, every carried proposal, and any guideline of the template that the row showed needs updating, with the update made in `docs/egypt-prompts.md`. Inside a bundle the chat prints and works it itself. The chat's reply does not print it: the reply ends with the starter (rule 7 of the run plan), and the starter prints it.
6. **Nothing is dropped silently.** A correction or flag leaves the prompt only when it is resolved, with the row and the report that resolved it written beside it.
7. **The last chat** (bundle 20, after W-DD-EG21 is published) works every correction and flag still open itself, under the same limits as any corrections step. It delivers a closing prompt only if something remains, with the reason each item could not be closed; if nothing remains, the reply says the course is complete and ends without a starter.

**1. Gate.** `python3 kit/next_prompt.py --list` shows {CODE} as this course's next unit not filed. No REWRITE verdict is open in `docs/courses-index.md`.

**1b. Corrections first** (`docs/public-courses.md` §3 rule 12), under that rule's limits, spelled out as (a) to (f) under the rows when there are any, each change checked by a fresh Agent on model opus against its source and the syllabus before it is applied, its report saved as `audits/egypt/corrections-<date>-<codes>.md`:
{CORRECTIONS}

**1c. Carried proposals**, worked now unless the owner removed one from this list:
{PROPOSALS}

**2. Stage the writer's packet** in one folder outside the repo with `python3 kit/thin.py stage writer --row {ROW} <folder>`. It holds: `brief.txt`, built by script with `open_brief` (the preamble, the Aim, Takes and Gives lines, the unit brief; never reworded, never retyped); `skills/write-unit/SKILL.md`; `docs/sourcing-standard.md` Parts 1 and 12; the figure kinds; `courses/egypt/notes/bibliography.md`; every unit of this course already filed: {FILED}; `flags.txt`. The course has no case register. Where this row's paragraph below names Greek or Roman modules, the chat copies each from `courses/greece/` or `courses/rome/` into the writer's and the checker's packets under `other-courses/` (`kit/thin.py` stages no other course's module). The chat opens none of it.

Open flags that name this unit:
{FLAGS}

**This row in particular.** {PARTICULAR}

**3. The writer.** One fresh Agent on model opus, isolated, that sees only its folder. It states its model in its first line; if that is not claude-opus-5-5, stop at once, change nothing and say so in one line. Tell it:
- A memory snapshot, project instructions or anything of that kind in its context is not a source and must not be used. It uses no memory, past-chat, Projects, connector, Artifact or Agent tool and no `mcp__` tool. It publishes nothing.
- The web rule: WebSearch first; WebFetch only a URL that a search in the same agent returned verbatim, never one typed, printed in a file, edited or reached by a redirect; a refused, redirected or timed-out fetch is "not checked" and is never retried or fetched from a copy.
- It follows `skills/write-unit` §4 to §5, renders every figure before handing in, and writes its files as it goes, so a restart loses little.
- The writer rules of this course (`docs/egypt-prompts.md` §1). The writer is one fresh Opus 5.5 agent with its packet and nothing else. One writer per module.
1. **Open before citing.** Every reference is found by a search and read at its publisher's page, its DOI address, an open-access repository or the holding institution's own page before it carries a claim. The seed bibliography says only that an entry is believed to exist.
2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (full text, chapter, abstract, catalogue record), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the work's own title; a figure is cited to the work that reports it, not to one that repeats it; each Sources entry is checked against the publisher's record before hand-in.
3. **Where to look first.** The UCLA Encyclopedia of Egyptology; the open publications of ISAC (Chicago), the Metropolitan Museum, the IFAO and the Egypt Exploration Society; the journal article at its DOI; the museum's own record for an object; the mission's own page for a site. A book that will not open is not cited from memory: use an opened reporter (a peer-reviewed review, an encyclopaedia article), named as the reporter, or leave the name out and state the view unattributed with its grade.
4. **Egyptian texts.** Cite by standard designation and by the translation opened; name the translator. Quote only what was read, under 15 words. Never Budge.
5. **Later sources are later.** State the gap in centuries whenever Manetho, a king list, a classical author or a Ptolemaic temple text is used for an earlier period.
6. **Dates and numbers.** Every date before 664 BC is approximate and follows EG3's convention; a disputed one gives the range. Every number names whose figure it is.
7. **Grade every claim** by EG1's key. From EG2 on, the key arrives in the packet inside EG1.
8. **Dispute boxes.** Wherever sources or scholars differ: a paragraph opening `**Where sources disagree.**`, a named source or scholar on each side, each from an opened text. Several per module.
9. **Claims under examination.** A popular or fringe claim is stated as it circulates, attributed to the kind of source that makes it, set against the evidence, graded, and not mocked. Its promoters' books, sites and films are not Sources.
10. **Faith and identity.** In EG23, EG28, EG56, DD-EG10 and DD-EG21: evidence and named positions; no confession or camp argued for.
11. **Lane.** Every module before this one is filed and in the packet: point to it by code, do not retell it, and open it first. The modules after it are not written: the brief's "Not here" line names what is theirs; give it a sentence and hand off by code. Greek and Roman modules are pointed to by their dotted codes, after opening the copy in `other-courses/`; one that is not in the packet is not pointed to, and the missing module is listed under Needs. A name keeps the English form the first filed module gave it.
12. **Anatomy and style.** `kit/AGENT-SPEC.md`: the forms allowed, 6 to 10 sections, the Self-test (10) and Carry forward (3) with their exact headings, the brief's own deliverable placed before the Self-test. British spelling, no em dashes, no emoji, no preamble. Signs by Gardiner number and description (flag F1).
13. **Figures.** After the draft, the figure pass of `skills/write-unit` §4b. A king list or a sequence of events is a timeline; a line of descent is a tree; competing estimates are a range. Every label and number is already in the sourced text.
14. **Flags and corrections.** A contradiction with a filed module or a brief, a mistake noticed in a filed module (this course's, or a Greek or Roman one), a brief that names a source, number or passage the opened evidence does not bear out, or a need the syllabus does not meet, goes to `out/notes.md`: under **Contradictions** with the quoted passage, what is wrong, the source and the exact replacement; under **Needs** with every module it affects and a proposed change. The writer never rewords a brief; it writes what the evidence carries and flags the brief.
15. **Hand-in.** `out/unit.md` (front matter, the module, the deliverable, Self-test, Carry forward, Sources); `out/sources.md`; `out/notes.md` with **Case facts** written as "none" (the course has no case), **Contradictions** and **Needs**, an empty list written as "none"; the figures rendered; `out/unsure.md`, up to ten claims it is unsure of, closing with the `Object:` line; a reply of six lines at most (its model, the files it wrote, the counts of its lists, references opened and not opened, brief items it could not source).

**4. The fresh check.** A separate fresh Agent on model opus that has not seen the writing, under the same agent rules, **with live search**: the prompt of `skills/audit-units` §3 with its figures paragraph, on a packet made with `python3 kit/thin.py stage checker --row {ROW} <folder> --unit out/unit.md --notes out/notes.md --unsure out/unsure.md --sources out/sources.md`. The packet holds the course's filed units (`filed/`, from the Execution course's row W-SCE2): the checker checks every pointer the unit makes to a filed unit, and every pointer to one of its own sections against that section's number. It writes `out/report.md` (or returns it as its reply, which the chat saves verbatim, the agent's line `Verdict: {CODE} · keep|fix|rewrite · counts` ahead of it) and replies in at most six lines. Beyond the skill's items it runs the seven passes of `docs/egypt-prompts.md` §2 and reports each by name. One fresh Opus 5.5 agent per module, with live search, that has not seen the module written. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.
1. **References exist and match.** Every Sources entry against its publisher's or Crossref's record.
2. **Claims against sources.** Every cited claim opened and read against its source; "unverifiable" where the source will not open, never a pass. Every designation of an Egyptian text (utterance, spell, chapter, papyrus, museum number) against an opened edition, translation or record.
3. **Grades.** Each grade against EG1's key. A later source never grades as attested; an announcement never grades above announced; a single scientific study is scientific, not consensus.
4. **Time and number.** Every date before 664 BC approximate and on EG3's convention; every gap between source and event stated; every number with its owner.
5. **Names and positions.** Every view attached to a scholar found in that scholar's opened text or in the named reporter; every dispute box with someone on each side; no claim under examination left standing as fact.
6. **Lane, pointers, tone.** Nothing retold from a filed module, and no fact (a date, a number, a spelling of a name, a museum number) stated differently from a filed module without a flag; nothing taken from a later module's lane beyond a sentence; every pointer opened and true; the preamble's tone and style rules; the faith-and-identity rule where it applies.
7. **Closing material and figures.** The brief's deliverable built in full; ten Self-test questions whose answers agree with the body; three Carry forward ideas; every figure's labels and numbers traced to the text.
It also runs the unit against Part 12 line by line and reads it as the reader in the preamble would. Before any fix, `python3 kit/thin.py save-report --row {ROW} --report out/report.md --model <the model it stated> --chat <this session's link> --date <today>` saves the report as `audits/egypt/fresh-check-{CODE}.md`; `python3 kit/thin.py assemble out/unit.md out/unsure.md "<the line it prints>"` gives the unit its unsure list. A `rewrite` verdict sends the unit to a new writer from the same brief, once; a second stops the row with a note.

**5. Apply.** A fresh applier agent (staged with `thin.py stage applier --row {ROW} <folder> --unit <unit> --report <report> --sources out/sources.md`) verifies each finding against the unit and the cited source and writes `out/apply.json` (`apply` or `hold`, with the reason); `python3 kit/thin.py apply <unit> fixes.json out/apply.json` applies it as exact replacements, the unit left unchanged if one fails, the applier re-run on the failures once. The applier's packet also gets the course's filed units and the writer's source log, and it works the report's could-not-verify list too (from the Execution course's row W-SCE2): each item is verified at its source or against the filed unit it points to, and what does not verify is cut or marked unverified in the unit by an exact replacement (`out/extra-fixes.json` and `out/extra-apply.json`, applied with `thin.py apply` after the findings). Every `hold` is recorded with its reason; a held error or should-fix is a flag. A figure that fails is fixed and re-checked by a new agent, as many times as it takes; figures are never dropped. Restarts: when the harness says it is resuming an agent, let it and say so in the record; if an agent is lost, re-run it from the start once; if lost again, start a fresh agent on the same packet that resumes from the lost run's working files. Look for agent transcripts (`.jsonl` under `/root/.claude/` or `/tmp/`); where they exist, check by script that each agent used no tool it was denied and read nothing outside its folder, and take its `"model"` field; where there are none, say so, and the model is the one the agent stated.

**6. Mistakes in filed units of this course** are corrected where they sit, at step 7b. The course has no source units.

**7. Syllabus flags.** Append every Contradiction and Need to `courses/egypt/notes/syllabus-flags.md` (next number, date, raised by {CODE}, the units affected, the flag, the proposed change, status open); set to `carried` each flag this unit was given and dealt with. The course has no case register: the writer's Case facts list is "none" (writer rule 15), and `records.json` carries no `case_lines`; the chat does not open the notes. Change no brief: a flag that would change a brief stays proposed and is listed in the reply (section 0, rule 7); `briefs.md` and the units in `course.toml` are edited only by a syllabus review that the owner confirms. If a flag means the next unit cannot be written as briefed, say so in the first line of the reply and write a syllabus-review prompt in place of the next unit's.

**7b. Proposals now** (`docs/public-courses.md` §3 rule 12): every correction to a filed unit or a record, and every kit fix the work needs, is made in this chat before the build, under that rule's limits, each change to a unit checked by a fresh Agent on model opus first. Only a brief change and a task for the owner stay *proposed*.

**8. File** per `skills/file-unit`, by a fresh filer agent and a script: front matter (model: `Opus 5.5`, the form `docs/courses-index.md` and `kit/index_check.py` use for the model the writer stated; `course:` as `egypt · EG · Egyptian history and mythology`; `next_unit` in records.json is the bare code, `EG2`) on `courses/egypt/{CODE}-<slug>.md`; the filer, staged with `python3 kit/thin.py stage filer --row {ROW} <folder> --unit <unit> --notes <notes> --unsure <unsure> --report <report>`, writes `out/records.json` (the reading-page intro, saying what the unit is, how it was made and its known gaps, among them every reference not opened and every abstract-only claim; `STATUS`, `NEXT_UNIT`, `VERSION`, the hub `CHANGELOG` line, the flag rows, the `docs/courses-index.md` edits with a staleness row if search is on, both changelog entries, the `Object:` line); `python3 kit/thin.py insert out/records.json` inserts it and restores everything if it fails. Then `python3 kit/index_check.py` until it matches and `python3 kit/private_terms.py` prints OK.

**9. Build and verify.** `cd kit && python3 build.py` (read its last line), `python3 verify.py` (ALL CHECKS PASSED), then `python3 verify.py --shots <dir> --page {PAGE}` (check the id it prints) in the background with a one-hour timeout; look at the page's shots at phone and desktop, dark and light, and at every figure's frames. A layout fault is fixed in `design/theme.css` (then `cp design/theme.css kit/shell.css`) or `kit/viz.py`, never in a page.

**10. Publish Academy once.** Before the build you publish, move the row to `docs/CHANGELOG.md`, move its entry in `docs/site-log.md` from Next to Done and {SAVEROW}, so the published Backlog and Changelog pages are current. **Land before you publish** (`docs/method.md` §10): commit everything above, then `python3 kit/land.py land <this row> --expected <file>`; publish only after it exits 0. Right before the publish, `git fetch` and require `git rev-parse HEAD` to equal `git rev-parse origin/main` (if main has moved, `git pull --ff-only` first), rebuild that HEAD (`cd kit && python3 build.py`) and publish that build, never one built before landing. Read the artifact https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH first and compare the live page with the build you started from (`get_artifact` for the live version id; `list_files` for every file's sha256 against `sha256sum` of the start build's files, the `kit/academy/` of the start commit that `out/<this row>/land-start.json` records, saved outside the repo before any build). Send only the files that differ from the live artifact's (their sha256 in `list_files`), found by script, and the shell inside the wrapper the live page carries (its first line and its closing `</body></html>`, taken from the saved live shell by script into a copy outside the repo), with `slug`, `base_version` and mode patch; read the sent files back and compare their sha256 with the build; never a new artifact, never forced. Then `./deploy.sh` once (it reaches its deploy repository itself), and confirm with `gh run` that the deployment succeeded. The publish and deploy identifiers go into the records after the publish, committed and landed again with `kit/land.py`, without republishing.

**11. Close** per `docs/method.md` §8, steps 1 to 5: the row moved to `docs/CHANGELOG.md` with the date, the models and a one-line result; its entry in `docs/site-log.md` moved from Next to Done ("{CODE}, {TITLE}, written"; "course EG complete" on the last unit); corrections left open go to the Corrections section, proposals to Carried proposals with their ⚠ flags; the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` rewritten, and the course's three data mirrors (`claude/egypt-course.toml`, `claude/egypt-briefs.md`, `claude/egypt-syllabus-flags.md`) refreshed when this row changed them (`docs/method.md` §8 step 4: the Project holds the data mirrors only of the course being written, and the row that files that course's last unit deletes them); a row of this course that finds them absent adds all three from their repo files (`project_write` with `local_path`), reading each existing path with `project_read` first; no long prompt is saved for this course: the first row of each group of four in `docs/BACKLOG.md` holds the course's starter line and the others "runs in the chat of <first row>" (section 0, rules 3 and 4), which `--save` keeps; {SAVE}.

**Reply** (section 0, rule 7): under the row's name, what was filed where (words, figures, references opened and not opened); the fresh-check verdict and the result of each of the seven passes; each mistake corrected, in a line; each flag raised, with the units it affects and whether it blocks the next unit; the private-terms result; verify's result; the publish and the deploy; the choices taken. Then, once for the chat: every proposal raised, each with what it does and a ⚠ on any disruption elsewhere (worked in the next row unless the owner vetoes it); every flag that would change a brief, which stays proposed; tasks for the owner, left only where no agent can do the task, and every row under Proposed of `docs/BACKLOG.md` marked for the owner, by row number, as the backlog holds them at the close, repeated in every reply until it is marked done; the backlog hand-off; at the chat's close, the next bundle scheduled as section 5b says (or the line saying there is no scheduling tool, or that the chat stopped). The reply ends with the course's starter line in a code block, as `python3 kit/next_prompt.py --starter egypt` prints it, never a long prompt; on the last row it ends instead with {NEXTPROMPT} in a code block.
```

### This row in particular

Section 3 above, word for word, in the form `kit/next_prompt.py` reads.

| Row | Unit | Search | Paragraph for `{PARTICULAR}` |
|---|---|---|---|
| W-EG1 | EG1 | off | Search off. First unit of the course. It sets the grade key every later module receives: define each of the seven grades so that two readers would agree, with a test and one worked Egyptian example each. |
| W-EG2 | EG2 | off | Search off. EG3 fixes the chronology the course follows and the form of an approximate date; EG2 fixes the English form of every site name. Later writers take both tables from the filed modules. |
| W-EG3 | EG3 | off | Search off. EG3 fixes the chronology the course follows and the form of an approximate date; EG2 fixes the English form of every site name. Later writers take both tables from the filed modules. |
| W-EG4 | EG4 | off | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG5 | EG5 | off | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG6 | EG6 | off | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG7 | EG7 | off | Search off. The earliest material: most claims rest on excavation reports. State the excavator and the season. EG7 sets the transliteration of the five royal names, reused to EG54. |
| W-EG8 | EG8 | off | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG9 | EG9 | off | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG10 | EG10 | off | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG11 | EG11 | off | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG12 | EG12 | off | Search off. The core never explains how a pyramid was built: it points forward to DD-EG1 to DD-EG7 by code. Herodotus and the Westcar Papyrus are later tradition. |
| W-EG13 | EG13 | off | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. |
| W-EG14 | EG14 | off | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. |
| W-EG15 | EG15 | off | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. |
| W-EG16 | EG16 | off | Search off. EG15 quotes only from an opened translation and names it. EG16's isotope and CT studies state their samples. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 1.1 from `courses/greece/`. |
| W-EG17 | EG17 | off | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 1.1 from `courses/greece/`. |
| W-EG18 | EG18 | on | Search on. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG19 | EG19 | off | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG20 | EG20 | off | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG21 | EG21 | off | Search off. EG21 is the core's whole account of Amarna in one module and argues none of the deep dive's disputes: it states that each exists and points forward. |
| W-EG22 | EG22 | off | Search off. Royal inscriptions are read as rhetoric, and the module says so. |
| W-EG23 | EG23 | off | Search off. Royal inscriptions are read as rhetoric, and the module says so. The faith-and-identity rule applies (writer rule 10). |
| W-EG24 | EG24 | off | Search off. Royal inscriptions are read as rhetoric, and the module says so. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 1.3 from `courses/greece/`. |
| W-EG25 | EG25 | off | Search off. Royal inscriptions are read as rhetoric, and the module says so. |
| W-EG26 | EG26 | off | Search off. Royal inscriptions are read as rhetoric, and the module says so. |
| W-EG27 | EG27 | off | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. |
| W-EG28 | EG28 | off | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. The faith-and-identity rule applies (writer rule 10). |
| W-EG29 | EG29 | off | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 5.2 from `courses/greece/`. |
| W-EG30 | EG30 | off | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 11.3, 6.2, 6.7 from `courses/greece/`. |
| W-EG31 | EG31 | off | Search off. The period's chronology is itself disputed: follow EG3 and box the alternatives. Manetho is pointed to EG1. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 0.1 from `courses/greece/`. |
| W-EG32 | EG32 | off | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 6.7 and 11.4, 7.1 and 7.2 from `courses/greece/`. |
| W-EG33 | EG33 | off | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Rome 2.5 from `courses/rome/`. |
| W-EG34 | EG34 | off | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Rome 5.5 from `courses/rome/`. |
| W-EG35 | EG35 | off | Search off. The Greek and Roman courses already told the dynastic and military story: point back and tell the Egyptian side only. Each decree is read in an opened translation. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.2 from `courses/greece/`; Rome 2.5, 8.4 from `courses/rome/`. |
| W-EG36 | EG36 | off | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.1 from `courses/greece/`; Rome 2.1 from `courses/rome/`. |
| W-EG37 | EG37 | off | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 2.1 from `courses/greece/`. |
| W-EG38 | EG38 | off | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG39 | EG39 | off | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG40 | EG40 | off | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG41 | EG41 | off | Search off. No connected native narrative of any myth exists: every element of a story names its earliest source and its date. EG38's field guide is the home of each god's basic facts; the others point to it. |
| W-EG42 | EG42 | off | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.4 from `courses/greece/`; Rome 2.4 from `courses/rome/`. |
| W-EG43 | EG43 | off | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG44 | EG44 | off | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG45 | EG45 | off | Search off. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG46 | EG46 | on | Search on. The core stops at the level of the event for the funerary texts and points forward to DD-EG15 to DD-EG21. Human remains are described with respect; no image of a body is asked for. |
| W-EG47 | EG47 | off | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.1 from `courses/greece/`. |
| W-EG48 | EG48 | off | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. |
| W-EG49 | EG49 | off | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. |
| W-EG50 | EG50 | off | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 8.5 from `courses/greece/`; Rome 9.3 from `courses/rome/`. |
| W-EG51 | EG51 | off | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. |
| W-EG52 | EG52 | off | Search off. Figures of temple wealth, wages and prices each name the papyrus and the study that reports them. EG52 separates what a papyrus shows from what Greek writers later credited to Egypt. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 5.6 and 12.1 from `courses/greece/`. |
| W-EG53 | EG53 | off | Search off. Flag F1: signs by Gardiner number and description. |
| W-EG54 | EG54 | off | Search off. Flag F1: signs by Gardiner number and description. |
| W-EG55 | EG55 | on | Search on. Flag F1: signs by Gardiner number and description. Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 9.1 from `courses/greece/`; Rome 10.3 from `courses/rome/`. |
| W-EG56 | EG56 | on | Search on. Flag F1: signs by Gardiner number and description. The faith-and-identity rule applies (writer rule 10). Copy into the writer's and the checker's packets, under `other-courses/`, the modules the brief points back to: Greek 9.3 from `courses/greece/`; Rome 10.4 from `courses/rome/`. |
| W-EG57 | EG57 | off | Search off. Last unit of the core. Written from the filed modules only: the chat adds to the packet every filed module's Carry forward and Self-test sections. It adds no claim. |
| W-DD-EG1 | DD-EG1 | off | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG2 | DD-EG2 | off | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG3 | DD-EG3 | off | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG4 | DD-EG4 | off | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG5 | DD-EG5 | on | Search on. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG6 | DD-EG6 | off | Search off. Every dimension names the survey it comes from. No construction proposal is presented as established. |
| W-DD-EG7 | DD-EG7 | off | Search off. Written from DD-EG1 to DD-EG6 as filed. The claims audit treats each claim on its evidence and mocks none. |
| W-DD-EG8 | DD-EG8 | off | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG9 | DD-EG9 | off | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG10 | DD-EG10 | off | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. The faith-and-identity rule applies (writer rule 10). |
| W-DD-EG11 | DD-EG11 | off | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG12 | DD-EG12 | off | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG13 | DD-EG13 | off | Search off. The period's reconstructions change with each new find: attribute each to its author from an opened text and present none as settled. |
| W-DD-EG14 | DD-EG14 | off | Search off. Written from DD-EG8 to DD-EG13 as filed. |
| W-DD-EG15 | DD-EG15 | off | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG16 | DD-EG16 | off | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG17 | DD-EG17 | off | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG18 | DD-EG18 | off | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG19 | DD-EG19 | off | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG20 | DD-EG20 | off | Search off. Every spell is cited by its number in the standard edition and read in an opened translation, named. Budge is never used. |
| W-DD-EG21 | DD-EG21 | off | Search off. The last unit of the course, written from EG42 to EG46 and DD-EG15 to DD-EG20 as filed. After it is published, this chat works the closing corrections (section 4, point 7). The faith-and-identity rule applies (writer rule 10). |
