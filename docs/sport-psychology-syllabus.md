# Sport Psychology for Coaches · syllabus

Drafted 16 Nov 2026 in a design chat on Fable 5.2. **Not in the repo.** Nothing was committed, published or written to the Project. Five files make the course's starting state:

| File | What it is | Goes to |
|---|---|---|
| `syllabus.md` | This file: frame, goal, outcomes, units, order, sourcing part, decisions | `docs/` material and the hub fields |
| `units_data.py` | `PRE`, the 13 units with their briefs, `AIMS` | `generator/data/sport-psychology/units_data.py`, unchanged |
| `case-facts.md` | The fictional case register | `generator/data/sport-psychology/case-facts.md` |
| `bibliography.md` | 97 seed references, checked for existence, and the list of popular claims | `generator/data/sport-psychology/bibliography.md` |
| `prompts.md` | The setup row's prompt and the writing rows' prompt | `docs/BACKLOG.md` rows, through `kit/next_prompt.py` |

## 1 · Frame

**Pick: a coach's course, not a psychologist's. Climate, skills, noticing, referring.**

- Coaches are with athletes daily; clinicians rarely are.
- A stated scope keeps a public course safe to follow.
- Graded evidence is what separates it from online advice.

**Override if:** the readers turn out to be mostly sport psychology students; then the course adds theory and assessment and drops the scope limits.

**Where the evidence pushes back.** Most studies are small. Most samples are university students or adult athletes, not 13-year-olds who win national titles. Several of the techniques coaches most want (talking to yourself by name, reading nerves as readiness, if-then plans) were tested outside sport. Prevalence figures for abuse come from adults remembering their childhood. The course grades every recommendation and names the sample behind it, so a reader sees "moderate" and "weak" often.

## 2 · Identity

| | |
|---|---|
| Title | Sport Psychology for Coaches |
| Code | SP (units SP1 to SP10, DD-SP1 to DD-SP3) |
| `kit/courses.py` entry | `sport-psychology`, family `markdown` |
| Data | `courses/sport-psychology/course.toml` (`[pack]`), `briefs.md`, `notes/` |
| Vault | `courses/sport-psychology/` |
| Fresh checks | `audits/sport-psychology/` |
| Track | New: Coaching (no existing track fits); renamed Sports on 19 Nov 2026 (S-SPORTS) |
| Reader | A coach of athletes aged about 10 to 25, any sport, no psychology training. In the preamble. A public course: the Project's single-reader rule does not apply |
| Case | Three fictional athletes: Dani, 14, judo; Milan, 17, football; Sara, 20, 400 m (`case-facts.md`) |
| Sourcing | `sourcing-standard.md` Part 1 and a new Part 7 (section 6 below) |
| Adapted from | Nothing. No source units |

## 3 · Goal and outcomes

**Goal.** By the end of the course you can adjust what you ask of an athlete to their age and stage; teach a small set of evidence-graded psychological skills in practice and use them on competition day; respond to an athlete's state from their baseline and their own words; keep your language, your handling of weight and your authority on the right side of a line you can state; and recognise the signs that mean referral, with a season plan written for your own squad.

- **Outcome 1 · Know the athlete and the evidence.** An age-and-stage table, a climate audit of your own coaching, and a claim-check you can run on anything you are told (SP1, SP2, SP3).
- **Outcome 2 · Skills in practice and on the day.** An anxiety profile, a skills block, a pressure-training block, a response table, a competition-day protocol, a pocket toolkit and a season plan (SP4 to SP8, SP10, DD-SP3).
- **Outcome 3 · Wellbeing and the coach's line.** A red-flag table and referral plan, a conduct code and comment test, and a protocol for who decides a weight class (SP9, DD-SP1, DD-SP2).

## 4 · Units

Ten core units in four parts and three deep dives. Each brief is in `units_data.py`; nothing below replaces it.

### Part 1 · The athlete and the evidence

| Code | Title | Ships | Search |
|---|---|---|---|
| SP1 | What a coach can do, and how to tell evidence from noise | Scope-of-practice card, claim-check sheet, the grade key | off |
| SP2 | The developing athlete, 10 to 25 | Age-and-stage table, athlete development note | off |
| SP3 | Motivation and the climate you create | Climate self-audit, three session rewrites, a parents' page | off |

### Part 2 · Pressure and skills

| Code | Title | Ships | Search |
|---|---|---|---|
| SP4 | Anxiety, arousal and performing under pressure | Athlete anxiety profile, normal-or-refer table | off |
| SP5 | The cognitive-behavioural toolkit | Eight-week skills block, skill cards | off |
| SP6 | Training under pressure | Four-week pressure block, routine builder | off |

### Part 3 · The coach in the moment

| Code | Title | Ships | Search |
|---|---|---|---|
| SP7 | Reading and responding to an athlete | Baseline sheet, state-response table, asking scripts | off |
| SP8 | Competition day | Competition-day protocol, debrief card, parents' note | off |

### Part 4 · Care, and the whole season

| Code | Title | Ships | Search |
|---|---|---|---|
| SP9 | Wellbeing, red flags and referral | Red-flag table, referral plan, three scripts | **on** |
| SP10 | The season plan | Two formulations, a season plan, a weekly review | off |

### Deep dives

| Code | Title | Ships | Search |
|---|---|---|---|
| DD-SP1 | The coach's line with minors | Comment test with twelve rewrites, conduct code, report-or-not table | **on** |
| DD-SP2 | Weight, body and who decides | Who-decides protocol, language card, scripts, club weighing policy | **on** |
| DD-SP3 | Tuning out the noise | Twelve technique cards, cue-word builder, four-week plan, pocket card | off |

"Search off" does not mean unsourced. Every writer opens every reference it cites (the preamble requires a source log). "On" means the unit also depends on facts that change (safeguarding codes, reporting routes, federation rules, referral tools), which are dated and re-checked after six months.

## 5 · Writing order

SP1 to SP10 in reading order, then DD-SP1, DD-SP2, DD-SP3. One unit per row.

- The course is cumulative: SP1 sets the grades and the scope every later unit uses, and SP10 assembles the sheets of SP2 to SP9.
- No core unit points forward to a deep dive. SP3 and SP6 state their own rules on punishment and pressure; DD-SP1 then examines them.
- DD-SP2 comes after DD-SP1 because it maps weight pressure onto DD-SP1's definitions.
- DD-SP3 is last: it trains its techniques on SP6's pressure ladder and points back to SP8.
- Rewrite gate as in `method.md` §3.

Shape: the `new-course` skill asks for a comparables deep dive and a hard-number one. This subject has neither. Its three deep dives are the two topics that need more room than a core unit (the coach's line, weight) and the one the reader will use most on the day (noise).

## 6 · Sourcing standard, Part 7

To be appended to `docs/sourcing-standard.md` as written.

**Part 7 · Sport Psychology for Coaches (from the shared preamble of `generator/data/sport-psychology/units_data.py`)**

- [ ] Every claim that carries a number, a mechanism or a recommendation is sourced where it is made.
- [ ] Each source is one of: a consensus or position statement of the IOC, ISSP, FEPSAC, AASP, AAP, ACSM or a national body of the same kind, labelled as consensus; a systematic review or meta-analysis; a peer-reviewed primary study; a standard textbook or handbook cited by edition and chapter; for safeguarding and rules, the issuing body's own page, dated.
- [ ] No video, podcast, social-media post, blog, coaching influencer, popular book or press report of a study is cited as a source; one may be named only as the claim under examination.
- [ ] Every reference in Sources is in the unit's source log with the address opened, what was read (abstract or full text) and the date; a claim that rests on an abstract alone says so.
- [ ] Every Sources entry matches its publisher's or Crossref's record: authors, title, journal, year, volume, pages, DOI.
- [ ] Every technique and recommendation carries one of the five grades (strong, moderate, weak, contested, practice), and the grade follows SP1's key.
- [ ] A study's finding states its sample (children, adolescents, students, adult athletes, non-athletes) and its design; a correlation is called a correlation.
- [ ] A finding from adults, students or non-athletes applied to younger athletes is labelled as the unit's inference.
- [ ] An effect size is given in the source's own terms, with the sample it comes from, or not given.
- [ ] A popular claim on the course's list is named as a claim and set against its evidence, or against "no peer-reviewed source found".
- [ ] The unit stays inside the coach's part: nothing teaches assessment, diagnosis or treatment, and each topic of mental health, eating, injury or abuse says where the coach's part ends and who takes over.
- [ ] No weight-loss method, calorie figure or target weight appears; nothing describes a method of self-harm.
- [ ] No law is stated as the reader's; a legal or reporting duty is a question with the body to consult; the unit says it is information, not legal, medical or psychological advice.
- [ ] No real athlete, coach or club is named as an example of abuse, illness or failure unless a cited court, public inquiry or peer-reviewed source names them.
- [ ] Examples come from at least three kinds of sport, and no single sport supplies more than a third of them.
- [ ] Every fact about Dani, Milan and Sara is labelled "(fictional)" on first use, agrees with `case-facts.md`, and is never used as evidence.
- [ ] Nothing about the Project's owner, his sport, his club or his athletes appears (`python3 kit/private_terms.py` prints OK).
- [ ] Where the search flag is on (SP9, DD-SP1, DD-SP2), every code, rule, tool, service or reporting route carries the date it was read on the issuing body's own page.
- [ ] The deliverable is built in full on the case athletes the brief names and then given as a template whose blanks say what goes in them.
- [ ] The unit does not read as advice without evidence. (If it does, the unit fails.)
- [ ] Links are given as links, the DOI address for a paper, so the course bibliography can collect them.

## 7 · Models and chats

- This syllabus: Fable 5.2, as the Project sets for course design.
- The setup row, S-SP0: one chat on Opus 5.5 that reads the repo, registers the course itself and has a fresh Opus 5.5 agent check the result.
- Every writing row: a thin main chat on Sonnet 5.5 that stages packets, launches agents and reads only their short replies. Writer, fresh checker, applier, filer and corrections checker are each a fresh Opus 5.5 agent.
- SP9, DD-SP1 and DD-SP2 get one more fresh Opus 5.5 agent, a safety reader, who reads only for scope and safety (section 8, D6).

## 8 · Decisions taken in this chat

Each stands unless vetoed.

| # | Decision | Override |
|---|---|---|
| D1 | Title "Sport Psychology for Coaches", code SP, a new track, Coaching | Another title or an existing track |
| D2 | A case of three fictional athletes in three kinds of sport, so no sport dominates and the weight unit has a weight-class athlete | One athlete followed through the course |
| D3 | Search on for SP9, DD-SP1, DD-SP2 only; every unit still opens every reference | All thirteen on, at six staleness checks more |
| D4 | Deep dives last, in the order line, weight, noise | The two safeguarding deep dives before SP4, if the line should frame the skills units |
| D5 | No country's law is stated; legal duties are questions with the body to consult | A Portugal appendix to DD-SP1 as a fourteenth unit |
| D6 | A safety reader on SP9, DD-SP1, DD-SP2 | Drop it and rely on the fresh check |
| D7 | Reliefs wait for a later row, as rule 10 of the public courses | Register ten outlines in the setup row |

## 9 · Proposals

- **P-SP1 · For Pedro, by hand.** Before this course is shared outside Academy, one qualified person (a sport psychologist, and for DD-SP1 a club or federation safeguarding officer) reads SP9, DD-SP1 and DD-SP2. Models wrote and checked them; on child safeguarding and mental health that is not enough for a public course. ⚠ Delays public sharing of three units; nothing else waits on it.
- **P-SP2.** The setup row must check two things this chat could not see, because the repo was not opened: that `kit/thin.py` can stage a writer's packet for a course with no source units, and that `kit/next_prompt.py` can print the writing prompt in `prompts.md`, including its course-specific paragraphs. ⚠ May need a kit change before W-SP1; the kit is shared with every course.
- **P-SP3.** `docs/public-courses.md` gains this course in its table and its rules apply to it; rule 4 (source units) does not, as there are none. ⚠ Touches a file the BW rows read.
- **P-SP4 · For Pedro, by hand.** The Project instructions' Purpose line names the courses; this one is not in it (as P38). ⚠ None.

## 10 · What was checked and what was not

- Checked on 16 Nov 2026: that each of the 93 journal references exists and that its authors, title, journal, volume, pages and DOI are as Crossref records them; that the two reports and two books exist, by search.
- Not checked: what any source says. The briefs name topics, not findings, for that reason. The writer of each unit reads the sources; the fresh checker checks every cited claim against them.
- Not opened: the repo. The data file follows the form of `building-with-ai/units_data.py` as mirrored in the Project; the prompts follow row W-DD-BW3 in `claude/BACKLOG-chats.md`.
- `units_data.py` parses: 13 units, 13 `AIMS` entries, one `{GOAL}` slot.

## 11 · Hub fields

For `generator/data/sport-psychology/hub.py`, in the form of `building-with-ai/hub.py`.

- `TITLE` = `'Sport Psychology for Coaches'`; `BAR` = `'SPORT PSYCHOLOGY'`; `BRAND_HTML` = `'SPORT PSYCHOLOGY <span>/</span> FOR COACHES'`
- `GOAL_SP`: the Goal sentence of section 3, beginning lower-case "by the end of the course you can".
- `COURSES`: one entry, `key='SP'`, `slug='sp'`, `units=SP`.
  - `tile`: "For coaches of athletes aged 10 to 25: how young athletes develop, how to teach mental skills that hold under pressure, how to respond on the day, and where a coach's part ends. Every claim sourced and graded."
  - `intro`: "For a coach in any sport with no training in psychology: what changes in an athlete between 10 and 25, the climate your own behaviour creates, what anxiety is and how it is kept going, the skills a coach may teach and how strong the evidence is for each, training under pressure, reading and responding to an athlete, competition day, the signs that mean referral, and a season plan. Three deep dives: the coach's line with minors, weight and who decides, and the techniques an athlete carries into competition. Worked on three fictional athletes in three sports. Ten core units in four parts and three deep dives."
  - `outcomes`: the three Outcomes of section 3.
- `COURSE_NOTE`: "Every unit is sourced to consensus statements, meta-analyses and peer-reviewed studies, grades each recommendation by its evidence, names the sample behind each finding, says where a coach's part ends, and ends with a deliverable built in full on three fictional athletes and then as a template."
- `ORDER`: SP1 to SP10, DD-SP1, DD-SP2, DD-SP3, each `"Opus 5.5"`; `"on"` for SP9, DD-SP1, DD-SP2, `"off"` for the rest.
- `NEXT_UNIT` = `'SP1'`; `STATUS` = `{}`; `READINGS` = `[]`; `VERSION` = `'v1 · <date registered>'`.
- `FRAME`: section 1. `LEARN_NOTE`: "Order of writing: the ten core units in reading order, SP1 to SP10, then the three deep dives; SP9, DD-SP1 and DD-SP2 with search on."
- `BUILD_PICK`: "SP1 first: the scope line and the grade key every later unit uses." Reasons: "Every later unit grades its claims by SP1's key." "It settles what a coach may and may not do." "It clears the popular claims before they recur." Override: "none; the course is cumulative."
- `CHANGELOG` v1: "Course created (new-course skill; row S-SP0): frame, goal and three outcomes, 13 units with one brief each and their Aim, Takes and Gives lines, the shared preamble with the reader persona, the fictional case register, a seed bibliography of 97 references checked for existence, the syllabus-flags file. No unit written."
