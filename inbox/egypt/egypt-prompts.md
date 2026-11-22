# Prompts: Egyptian history and mythology

## 0 · The run plan (Pedro, 21 Nov 2026)

These rules govern every chat of this course. Where the copied template says otherwise, these win, and S-EG0 changes the template to match.

1. **Clone line.** Every prompt meant to be pasted into a session, the setup prompt, the starter and each row's prompt as `kit/next_prompt.py` prints and saves it, opens with exactly this line and says nothing else about cloning, attaching the repo, add_repo, registering it or approval:
   `Clone apcanario/learning (shallow, push access).`
2. **Setup runs alone.** Row S-EG0 files the design, builds, verifies and publishes, and writes no unit. In `kit/next_prompt.py` it only adds the course to `QUEUE`, and it checks that another course's row prints byte-identical before and after. No `HOLDS` or `GATES` entry.
3. **Bundles of four.** After setup, the course is written in chats of four units each, in writing order; the last chat takes what is left. Each is a thin Sonnet 5.5 main chat with fresh Opus 5.5 agents, run with `python3 kit/next_prompt.py --bundle 4`: each unit is checked, filed, landed and published before the next begins, so a chat that stops strands nothing.
4. **One starter.** Every writing chat starts from the same two lines (section 6), which also resume a chat that stopped part-way.
5. **No gate rows.** A point where Pedro reads before more is written sits on a bundle boundary; his starting the next chat is the go. Nothing for him to close by hand.
6. **Closing corrections.** The last chat works every correction and flag still open itself, and delivers a closing prompt only if something remains, saying why.
7. **Replies.** A chat's one reply ends with the starter in a code block, not a long prompt. A task is left for Pedro only where no agent can do it. Proposals are worked in the next row unless he vetoes them.
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

It also runs the module against Part 9 line by line.

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

## 4 · The carry-forward rule (Pedro, standing), as this course runs it

Nothing found goes unrecorded or waits for a later audit. It applies to every row of this course, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a module is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or Pedro.
2. **About a module already filed** (this course's, or a Greek or Roman module a writer opened). It goes into the next row's prompt as a correction, with the module, the passage, what is wrong and the source. The next row fixes it first, before it writes: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About a module not yet written.** It becomes a flag in `courses/egypt/notes/syllabus-flags.md` naming every module it affects, and it is printed in each of those modules' prompts as a guideline. A flag that would change a brief is proposed, never applied by the chat that raised it.
4. **About the module being written.** It is fixed in the same row before filing. What cannot be fixed (a source that will not open) is cut or marked unverified in the module, and carried as in 2.
5. **The next row's prompt always exists.** Every row saves the next row's prompt into its row of `docs/BACKLOG.md` (`kit/next_prompt.py --save`), already holding every correction still open, every open flag that names that unit, every carried proposal, and any guideline of the template that the row showed needs updating, with the update made in `docs/egypt-prompts.md`. Inside a bundle the chat prints and works it itself. The chat's reply does not print it: the reply ends with the starter (rule 7 of the run plan), and the starter prints it.
6. **Nothing is dropped silently.** A correction or flag leaves the prompt only when it is resolved, with the row and the report that resolved it written beside it.
7. **The last chat** (bundle 20, after W-DD-EG21 is published) works every correction and flag still open itself, under the same limits as any corrections step. It delivers a closing prompt only if something remains, with the reason each item could not be closed; if nothing remains, the reply says the course is complete and ends without a starter.

## 5 · When a chat stops, and where Pedro reads

A bundle runs its four rows one after another, each to its publish. It stops before its fourth row is closed only when: the session's permission check refuses a repo script; an agent states a model that is not Opus 5.5; a unit gets a second `rewrite` verdict; `verify.py` fails twice on the same check. It then says why in one line, and its reply still ends with the starter, which resumes at the first unit not filed. It never stops to ask a question.

There is no gate row. Two bundle boundaries are worth a read, and starting the next chat is the go:

- **After bundle 1** (EG1 to EG4). The reply states, per unit, the references opened and not opened and the brief items that could not be sourced. This is the test of the access rule: if writers could not open enough, say so before starting bundle 2, and the next chat begins with the change.
- **After bundle 15** (EG57 and the first deep-dive units). The core is complete.

**What Pedro does by hand:** paste the setup prompt once. After that the chats schedule one another (section 5b); he pastes the starter only where a chat could not schedule the next, or to resume one that stopped. No file to attach, no gate to close, no proposal to confirm.

## 5b · Scheduling the next bundle (P-EG7, accepted by Pedro, 21 Nov 2026)

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
6. Adds Part 9 to `docs/sourcing-standard.md`, the Egypt section to `kit/AGENT-SPEC.md`, and the course's section to `docs/courses-index.md` (0 of 78 written; every unit in writing order with model Opus 5.5, its search flag and its vault path).
7. Adds the writing rows W-EG1 to W-EG57 and W-DD-EG1 to W-DD-EG21 to the queue of `docs/BACKLOG.md`, grouped under one heading per chat exactly as the prompts file's section 0 lists them (Bundle 1 to Bundle 20), with W-EG1's prompt saved by `python3 kit/next_prompt.py --row W-EG1 --save`; and an entry in `docs/site-log.md`.
8. Builds and verifies (ALL CHECKS PASSED, `index_check.py`, `private_terms.py`) and looks at the course home at the three widths.

The checker reads the registration against the four files: every brief byte for byte; every unit's title, order, search flag and Takes line; the goal and outcomes; Part 9 against the syllabus's §6; the template's replaced sections, its clone line and its Reply against the prompts file; the backlog's twenty groups; the `next_prompt.py` diff (one added queue entry) and the byte-identical row; and that nothing outside this course changed in the built site except the home's course list. Its findings are fixed before landing.

Then land (`kit/land.py land`), publish Academy once from a fresh build of the landed HEAD (the artifact, read first, then `kit/deploy.sh`), close the row by `docs/method.md` §8 and refresh the Project mirrors, adding the course's three data mirrors.

One reply. It says what was registered, the bibliography entries struck, the proposals raised (worked in W-EG1's row unless I veto), and any task only I can do. It schedules bundle 1 as the prompts file's section 5b says, or says it has no scheduling tool. It ends with the starter in a code block: the two lines of the prompts file's section 6, or, if `kit/next_prompt.py` has no `--course` option, the same two lines with `--row W-EG1 --bundle 4`.
```
