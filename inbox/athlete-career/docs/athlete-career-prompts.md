# Prompts: Managing an Athlete's Career

- **S-AC0**, once and alone: the setup row. Its prompt is `docs/athlete-career-S-AC0-prompt.md`, pasted into a new chat on **Sonnet 5.5**. The design is read from an artifact, not a zip. The chat is thin; a fresh **Opus 5.5** registrar does the repo work and a fresh Opus 5.5 agent checks it. It writes no unit.
- **W-AC1 to W-DD-AC3**: one row per unit, printed by `kit/next_prompt.py`. They are worked four to a chat, in writing order, by five chats that all start from the same two-line starter (section 5).

The writing template is not rewritten here. The repo holds a working one for a course of the same build, in `docs/supply-chain-execution-prompts.md` ("Rows W-SCE1 to W-DD-SCE2 · write one unit"), already corrected to the kit by S-SCE0 and W-SCE2. S-AC0 copies it as it stands on the day and replaces its course-specific parts (the course's name, code, slug and paths; Part 8 with Part 9; the two closing sections) with sections 1 to 5 below. Everything else in the template (the thin chat's rules, the agents and their order, the scripts, the checkpoint commits, the quality review, the close) stays as the repo has it.

## 1 · Writer rules

The writer is one fresh Opus 5.5 agent with its packet and nothing else.

1. **Open before citing.** Every reference is found by a search and read at its publisher's page, its DOI address or the issuing body's own page before it carries a claim. The seed bibliography says only that an entry exists.
2. **Source log.** `out/sources.md`: one row per reference with the address opened, what was read (abstract, summary or full text; for a law, the articles read), the date, and the claims it carries. A reference that could not be opened is listed as not opened and carries nothing. A title is the work's own title, never a slug; a figure is cited to the source that reports it, not to one that repeats it; each Sources entry is checked against the publisher's or issuing body's record before hand-in.
3. **Fewer, better.** Prefer one source read in full to three read in abstract. Do not cite to decorate. If a section's support is one textbook's account, grade it practice and say so.
4. **Reputable and verifiable only.** A law firm's note, a press report, a recruiting or agency site may lead you to a text; the text is what you read and cite. An interested party's page is evidence of what that party says, offers or requires, never of how things are.
5. **Grade every claim** by AC1's key. From AC2 on, the key arrives in the packet inside AC1.
6. **Rules are never the reader's.** Each rule or law is its issuing body's text, with its sport or country and the date read, followed by the question the reader puts to their own body.
7. **Portugal.** Where the brief has "In Portugal", read each text at the Diário da República or the body's own page, cite it in Portuguese with its article, give its sense in English as your translation, and label the section one country's worked example. The private-terms check fails on two Portuguese city names (the plain lines of `kit/private-terms.txt`): a source whose title or address holds one is cited without that word where the record allows, and otherwise raised under Needs, never reworded around.
8. **Money.** No fee, rate, commission or typical deal value unless a named source published it, with whose figure, sample, year and currency. Otherwise write "no public figure".
9. **Not advice.** The line once near the top. Legal and tax points are questions with the body or professional to ask. Nothing about investing.
10. **Minors.** Nothing on AC4's refusal list is proposed. From AC5 on, "If the athlete is under 18" closes the body before the Self-check and agrees with AC4.
11. **The roles.** Wherever the coach or the coach's business has a stake in the decision described, name the conflict and say who else decides. Never present the reader's good intentions, or working unpaid, as settling it.
12. **Real people and companies.** No real athlete, coach or family as an example of hardship or failure beyond what they published themselves or a court or inquiry states. No real agent, agency or sponsor assessed, ranked or recommended. Nothing about the Project's owner, his sport, his club, his athletes or his business.
13. **The case** comes from `case-facts.md` only, which carries Sport Psychology's facts; invented facts go in the notes. Sara's and Dani's referrals are respected in anything planned for them.
14. **The closing sections** before the deliverable: "Check before you act", then from AC5 on "If the athlete is under 18", then "Self-check", every answer drawn from the unit's sourced text.
15. **Flags and corrections.** A contradiction with a filed unit or a brief, a mistake noticed in a filed unit, or a need the syllabus does not meet, is written to `out/notes.md` (a contradiction or a mistake under **Contradictions**, a mistake with the quoted passage, what is wrong, the source and the exact replacement; a need under **Needs**), naming every unit it affects and with a proposed change. It is carried by section 4. The writer never rewords a brief.
16. **Hand-in.** As the template's hand-in rule: `out/unit.md`, `out/sources.md`, `out/notes.md` with its three lists (**Case facts**, **Contradictions**, **Needs**), the figures rendered, `out/unsure.md` closing with the `Object:` line, and a reply of six lines at most.

## 2 · The fresh checker's seven passes

One fresh Opus 5.5 agent that has not seen the unit written, with live search. It writes findings (error, should-fix, minor) and edits nothing. A reference that does not exist stops the row.

1. **References exist and match.** Every Sources entry against its publisher's, Crossref's or its issuing body's record: authors, title, journal or publisher, year, volume, pages, DOI; for a law, its number, date and official-journal reference.
2. **Claims against sources.** Every cited claim opened and read against its source; samples and designs stated; an inference from famous athletes or large sponsorships to an unknown athlete labelled; "unverifiable" where the source will not open, never a pass.
3. **Grades.** Each grade against AC1's key; an interested party never graded research or data; an abstract-only reading said to be one.
4. **Rules and Portugal.** No rule or law stated as the reader's; each with its body, its sport or country and the date read; each "In Portugal" text read at its issuing page and fairly translated; no law firm's note or press report standing in for a text.
5. **Safety.** The not-advice line. Minors: nothing from the refusal list; "If the athlete is under 18" agrees with AC4. No supplement recommended. No real person in hardship beyond the rule; no real agent, agency or sponsor assessed. Nothing teaches getting around a rule. The roles conflict named where the coach or the coach's business has a stake. No money figure without source, sample, year and currency.
6. **The case, scope and tone.** Every case fact against `case-facts.md` and, through it, Sport Psychology's register; labelled fictional; never evidence. Nothing about the Project's owner. No coaching, psychology or audience-building method re-taught. The preamble's tone rules; terms defined on first use.
7. **Deliverable and figures.** The deliverable against the brief's wording, built in full on the named case and then as a template; the closing sections present and agreeing with the body; every figure's labels and numbers traced to the text.

It also runs the unit against Part 9 line by line and reads it as the reader in the preamble would.

## 3 · This row in particular

One paragraph per row, appended to the template by `next_prompt.py`.

| Row | Paragraph |
|---|---|
| W-AC1 | Search on. This unit sets the grade key and the glossary that every later unit receives: define each grade so that two readers would agree, with one worked example each, and decide the three hard cases the brief names. State all thirteen claims; test only what this unit opens. |
| W-AC2 | Search on. The course's centre: coach, sponsor and unpaid representative for the same athlete. Fix the forms of the roles declaration, the mandate and the conflict register here; AC9, AC10 and AC15 reuse them. If no study of coach-sponsors is found, say so and grade the reasoning practice. Claim C12 belongs here. |
| W-AC3 | Search on. Every clause is quoted from the rule-maker's own page with the date read. Fix the rules register's columns here; DD-AC3 reuses them. Claim C11 belongs here. |
| W-AC4 | Search on. Dani's referral is under way: the protocol's first line is that nothing commercial is added to her load while it is open. Her coach's own label is one of the two approaches. Fix the refusal list here. Claim C5 belongs here and in AC7. |
| W-AC5 | Search on. Programmes and amounts only from the funder's own page, dated. The shortfall this unit computes is the number AC9 to AC11 work from. Claim C3 belongs here: trace it to the earliest source you can open. The shortfall is also the first thing bundle 2 produces: AC6 to AC8 follow in the same chat. |
| W-AC6 | Search off. The research studied famous athletes: state each sample before any use, and label every transfer. Fix the asset inventory's columns; AC8's sponsor table takes its third column from them. Claim C2 belongs here and in AC8. |
| W-AC7 | Search off. Point to the public personal-brand course for method and re-teach none of it. Sara's referral limits what the plan asks of her; say how. |
| W-AC8 | Search on. Written from the sponsor's seat. Say plainly where the research stops short of small sponsors and unknown athletes. Claims C4, C9 and C10 belong here. |
| W-AC9 | Search on. The reader is now the sponsor. The policy's criteria are written before any athlete is named, and someone other than the coach decides where the coach coaches the candidate. The agreement is read from the athlete's side. The brief points forward to AC12's contract sheet, which is not yet written: build the agreement against the clause list in AC12's brief, say so in the notes, and raise a Need naming AC12 so that its sheet is tested on this agreement. |
| W-AC10 | Search off. Little research exists on how such deals are won: say what was found. The reader's own business is already a sponsor: the unit names that conflict at prospecting, at price and at exclusivity. Claim C1 belongs here and in AC13. |
| W-AC11 | Search on. Disclosure rules from the regulators' own pages, dated; the records are in the public personal-brand course's PB8 Sources. |
| W-AC12 | Search on. Every clause as a question, never as advice. The fictional agreement is written with faults on purpose and each fault is annotated. Test the finished sheet on AC9's two agreements; a fault it finds there is a correction to AC9. Claim C8 belongs here. |
| W-AC13 | Search on. Football is the contrast only. The Court of Justice's 2026 rulings are read at the Court's page, not in commentary. Claim C7 belongs here and in DD-AC2. |
| W-AC14 | Search on. Mostly research: state samples and designs. The coach's interest in the athlete continuing is named as a conflict. Claims C6 and C13 belong here. |
| W-AC15 | Search off. Every part of the plan names the earlier deliverable it comes from. Dani's plan is mostly "not yet", each with its reason. |
| W-DD-AC2 | Search on. Every number with whose it is, the sample, the year, the currency and the date read. Where no public figure exists, say so; invent no range. |
| W-DD-AC1 | Search on. A case needs the athlete's own published account and an independent record. Nothing is inferred about a named person beyond the sources. |
| W-DD-AC3 | Search on. The last unit: every Portugal section re-read at source; each change is a correction to the unit that holds it. The chat then works every correction and flag still open itself (section 5, rule 6) and delivers a closing prompt only if something remains, saying why. |

## 4 · The carry-forward rule (Pedro, standing)

`docs/method.md` §9, with this course's names. It holds for every row, the last included.

1. **What counts.** Any error, mistake, contradiction, unverified claim, missing source or unmet need, found before, during or after a unit is written: by the writer, the fresh checker, the applier, the filer, the corrections checker, a script, or Pedro.
2. **About an AC unit already filed.** It goes into the next row's prompt as a correction, with the unit, the passage, what is wrong and the source. The next chat fixes it first: each change is checked by a fresh agent against its source and the syllabus, applied as an exact replacement, and recorded.
3. **About an AC unit not yet written.** It becomes a flag in `courses/athlete-career/notes/syllabus-flags.md` naming every unit it affects, printed in each of those units' prompts. A flag that would change a brief is proposed, never applied by the chat that raised it.
4. **About the unit being written.** Fixed in the same chat before filing. What cannot be fixed is cut or marked unverified, and carried as in 2.
5. **Every row hands on to the next through the repo.** The next row's prompt, as `kit/next_prompt.py` prints it, holds every open correction, every open flag that names the next unit, and any rule of this document the row showed to be wrong, corrected here. Inside a bundle the chat runs it; at the end of a chat the reply ends with the starter (section 5), which prints it.
6. **Nothing is dropped silently.** A correction or flag leaves the next prompt only when resolved, with the row and the report that resolved it beside it.
7. **The last row** (W-DD-AC3) is followed, in the same chat, by the closing corrections (section 5, rule 6). A closing prompt is delivered only if something remains open, with the reason.

Two additions for this course:

8. **Sport Psychology's register.** A conflict between this course's case and `courses/sport-psychology/notes/case-facts.md` is a correction to this course. A fault found in a filed Sport Psychology unit goes under Corrections in `docs/BACKLOG.md`.
9. **Portugal.** A Portuguese text found changed since an earlier unit cited it is a correction to that unit.

## 5 · The run plan

Set by Pedro on 21 Nov 2026 (22:43). It replaces the six-session plan of P-AC12.

| Chat | Rows, in writing order | Pasted to start it |
|---|---|---|
| Setup | S-AC0 | `docs/athlete-career-S-AC0-prompt.md` |
| Bundle 1 | W-AC1, W-AC2, W-AC3, W-AC4 | the starter |
| Bundle 2 | W-AC5, W-AC6, W-AC7, W-AC8 | the starter |
| Bundle 3 | W-AC9, W-AC10, W-AC11, W-AC12 | the starter |
| Bundle 4 | W-AC13, W-AC14, W-AC15, W-DD-AC2 | the starter |
| Bundle 5 | W-DD-AC1, W-DD-AC3, then the closing corrections | the starter |

**The starter.** One for the whole course. It starts every writing chat and resumes one that stopped part-way:

```
Clone apcanario/learning (shallow, push access).
Managing an Athlete's Career, next bundle. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. Run `python3 kit/next_prompt.py --course athlete-career --bundle 4` and work what it prints in full, unattended.
```

If `kit/next_prompt.py` has no `--course` option when setup runs (it had none at commit 3188250), the second line ends: Run `python3 kit/next_prompt.py --row W-AC1 --bundle 4` and work what it prints in full, unattended. A later chat that has to use `--row` names the first row not yet filed.

Rules:

1. **The clone line.** Every prompt meant to be pasted into a chat opens with exactly this line and says nothing else about getting the repository:
   `Clone apcanario/learning (shallow, push access).`
2. **Setup runs alone.** S-AC0 files the design, builds, verifies and publishes, and writes no unit. In `kit/next_prompt.py` it only adds the course to `QUEUE`, and it checks that another course's row prints byte-identical before and after. No `HOLDS` entry and no `GATES` entry.
3. **Bundles of four.** After setup the course is written in chats of four units each, in writing order; the last chat takes what is left. Each is a thin Sonnet 5.5 main chat with fresh Opus 5.5 agents, run with `python3 kit/next_prompt.py --bundle 4`. Each unit is checked, filed, landed and published before the next begins, so a chat that stops strands nothing. No two units are written in parallel.
4. **One starter per course**, above. The setup row's reply ends with it.
5. **No gate rows.** A point where Pedro reads before more is written sits on a bundle boundary; his starting the next chat is the go. Nothing is his to close by hand. The natural place to read is after bundle 1, when the grade key, the roles declaration, the rules register and the minor's protocol exist; after bundle 2 the first sponsor units do.
6. **Closing corrections.** The last chat, after W-DD-AC3 is filed, works every correction and flag still open itself: each checked by a fresh agent against its source and the syllabus, applied as an exact replacement, recorded. It delivers a closing prompt only if something remains, saying why.
7. **Replies.** A chat gives one reply. It ends with the starter in a code block, not with a long prompt. A task is left for Pedro only where no agent can do it. A proposal is worked in the next row unless he vetoes it; a flag that would change a brief is the one thing that stays proposed, and it is listed in the reply.
8. **The record.** The chats and their units are in the syllabus's section 5; the writing rows of `docs/BACKLOG.md` are grouped the same way; these rules are this section.
