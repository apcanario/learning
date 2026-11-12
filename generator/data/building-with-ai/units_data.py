# Units for the public course BW, Building with AI (11 Nov 2026).
# PRE is the shared preamble baked into every open brief; {GOAL} is replaced by the course goal.
# Each unit: (code, title, one-line scope, what it ships, brief). Ten core units in three parts plus three deep dives (DD-),
# written last. A unit is written when its file is filed in courses/building-with-ai/ (A5).
# AIMS: per unit, (aim, takes, gives); kit/mdcourse.py joins them into the brief between the preamble and the unit brief.
# The course is adapted from a private course of the Learning Project; the Takes line names the source units a writer is given.
PRE = ("Write one unit of a self-study course in the long-form report format of the Learning Project's markdown courses: a long-form report in Markdown. "
"Length is whatever the topic needs (2,000–6,000 words); do not pad and do not cut to a target. "
"Reader: an experienced professional who already reasons and writes well (an analyst, a designer, a product manager, a researcher, a lawyer, a founder), "
"uses a chat assistant most days with no method, may not write code, and brings one real project to build through the course (a report, a course, a body of research, a small tool, a content operation); "
"reads in order (each unit assumes the ones before it), reads on a phone, checks the citations, and wants genuine depth rather than a primer. Address the reader as 'you'. "
"This course is written to be shared with anyone; it is an exception to the Learning Project's single-reader rule (decided 11 Nov 2026). "
"Source material: the Takes line names the units of a private course this unit is adapted from. Take their evidence and their structure where they serve this reader; "
"re-verify every claim you carry over against its source before you use it; carry over nothing about that course's own reader "
"(no name, employer, city, health detail, personal project, tool of his own making, handle or household detail appears here); "
"and never refer to the private course or its units, which a reader of this course cannot open. Point only to units of this course, by code (BW4, DD-BW1). "
"Tool stance: state each principle so that it holds for any current assistant; work the detail on Claude (claude.ai and Claude Code), where the source evidence was verified; "
"date every product fact (a limit, a price, a feature, a model name) to the day it was read on the vendor's own page; "
"and end the body, before the deliverable, with a short section 'On other tools' that says which of the unit's claims are specific to Claude and where the equivalent is documented for ChatGPT and for Gemini, "
"cited to the vendor's own documentation, or says that no equivalent was found. "
"Running case: Academy (real), a library of self-study courses built by one person with Claude in October and November 2026, each unit written by one model from a brief, checked by a fresh context and audited by sample. "
"Facts about Academy come only from generator/data/building-with-ai/case-academy.md, cited as 'Academy case file' with its section; never infer a fact about the case that the file does not hold "
"(if the unit needs one, list it in the notes as a need). Label the case '(Academy case)' on its first use in the unit. One project is an anecdote: label it so, and never let it be the only support for a general claim. "
"Deliverables are built twice: in full on the case (or, where the brief says so, on a neutral example with its invented content labelled), then as a template the reader fills for their own project, each blank saying what goes in it. "
"Tone: direct, no flattery, no filler, no motivational language, no 'not X but Y' constructions. "
"Course goal: {GOAL} "
"Sourcing standard: every claim that carries a number, a mechanism or a recommendation is sourced where it is made; acceptable sources are peer-reviewed work and preprints (a preprint labelled as one), "
"vendor documentation and statements (labelled as vendor, dated), named practitioners' own posts, talks and repositories (labelled as practice), and independent benchmarks with their version and date; "
"each method or practice carries an evidence grade: measured, documented practice, or stated opinion; no uncited figures; no invented names, studies, quotations or numbers; "
"if a claim cannot be sourced, say so and leave it out of the deliverable. A unit that reads as advice without evidence is a failed unit. "
"Links are given as links, so the course bibliography can collect them. "
"Figures: where a section's content has a shape, declare it as a fenced viz block of a kind kit/viz.py draws (one to four a unit is a guide; none where nothing has a shape); "
"a figure adds no fact, and its caption says what it shows and where its data comes from. "
"Where the unit depends on current facts (model lineups, prices, plan limits, product features), search before writing and date the facts. "
"End with the unit's deliverable, built out in full, not described.")

BW = [
("BW1", "Mental model",
 "The context window, tokens as cost and attention, what persists and what does not, trained against retrieved knowledge, why the same prompt answers differently.",
 "the five-minute model + a table for diagnosing a failed output",
 "Unit BW1, Mental model. Search before writing. Cover: the context window as the one thing you control; tokens as cost and as attention; what persists inside a chat and across chats, and what a memory feature changes (dated); knowledge from training, knowledge retrieved and what is in the conversation; the training cutoff; why the same prompt gives different answers; what a system prompt, a project instruction and a user message each do; fabrication as a consequence of how a model produces text, not an occasional fault; the layers a current assistant offers (chat, projects, memory, tools and connectors, skills, agents) as a map the later units fill in. Deliverable: a model of how an assistant works that you could say to a colleague in five minutes, as plain prose; and a diagnosis table (the symptom, its likely cause in the model, what to change, the unit that treats it)."),
("BW2", "Choosing the model and the effort",
 "Cost per task, when the small model is the right one, what effort settings do; the method in the unit and the lineup in a dated appendix.",
 "routing table for ten common project tasks",
 "Unit BW2, Choosing the model and the effort. Search before writing. Cover: cost per task rather than per token; the tiers vendors offer (small and fast, mid, large) as a pattern that outlives any lineup; what effort or thinking settings do, from the vendors' documentation; where quality differences show and where they do not, with benchmark evidence and its limits (who runs it, which version, which date); self-preference, and why a check is better run by a different model or a fresh context; a subscription against the API; and a rule for re-deciding when the lineup changes. Then a dated appendix: the current Claude lineup with prices and plan limits as Anthropic states them, and one pointer row each for OpenAI and Google from their own pages. Deliverable: a routing table for ten common project tasks (triage and reformatting, extraction to a table, summary for a named reader, a long first draft, critique of a draft, research with search, deep research, a code change, an audit against sources, a plan or spec), each with tier, effort, the reason and an override trigger, worked on the Academy case; then the template with blank rows."),
("BW3", "Briefing: prompts that hold up",
 "The four parts of a brief that survives, output contracts, negative examples, and the common ways an ask fails.",
 "ten brief templates, each with a worked example",
 "Unit BW3, Briefing: prompts that hold up. Cover: the four parts of a brief that survives (who the reader is, what the output is, the constraints, examples including negative ones); specificity against length; output contracts (format, a length rule, what done looks like); what the evidence and the vendors' guidance say about examples and about where the question sits in a long prompt, each labelled; how a long conversation drifts, and when to restart; the common failures (asking for a plan when you want the thing, burying the ask, stacking unrelated tasks); what the prompting literature measured and on which models. Deliverable: ten templates, each ready to paste and each with a worked example: a research brief, a long-form draft, a critique of a draft, a decision memo, extraction to a table, a summary for a named reader, plan then build, a rewrite in a voice from samples, an audit of claims against sources, a code change with its test."),
("BW4", "Context engineering",
 "Instructions, files, memory, skills, connectors: what belongs where, what loads every turn, when to start a new chat, how a project rots.",
 "project-structure template + rot check",
 "Unit BW4, Context engineering. Cover: the layers a project offers (instructions, knowledge files, memory, skills, tools and connectors, scheduled tasks) and what belongs in each; what loads every turn against what loads on demand, and the cost of each; what happens to a large knowledge set (retrieval) and what that changes; when to start a new chat and when not to; one source of truth and its mirrors; how a project rots (stale files, duplicated rules, instructions that contradict each other) and how to see it early; the Academy case's own structure audit and its seventeen findings. Deliverable: a project-structure template (folders, an instruction file with a word limit, an index file, a table of what goes where) and a rot check as a fifteen-minute monthly procedure, worked on the Academy case; then the template for your project."),
("BW5", "Specifying a project",
 "From idea to spec to build order: units of work one context can finish, a definition of done, a decision log, and how a spec changes.",
 "one-page spec + build order + unit-brief template",
 "Unit BW5, Specifying a project. Search before writing. Cover: why a specification comes before the building, from the spec-driven practice that has a named author and a primary source, each graded as documented practice unless it measured something; what a spec holds for a knowledge-work project (the reader, the goal in one sentence, measurable outcomes, non-goals, a definition of done); cutting the project into units that one context can finish; the build order and its dependencies; one brief per unit, never reworded once work has started; the decision log; the backlog and the changelog as a pair; proposing a task against doing it; how a spec is allowed to change (flags raised during the work, reviewed at a boundary); the Academy case's method as the worked example (syllabus, briefs, build order, one context per unit, fresh check, sample audit). Deliverable: a one-page spec, a build order, a unit-brief template, done-when lines and a decision-log format, worked on the Academy case as it was specified; then the templates for your project."),
("BW6", "Research and verification",
 "Ask, search or deep research, with cost and time; how models fail; how to read a research report; sampling before trusting.",
 "verification protocol with a sampling rule",
 "Unit BW6, Research and verification. Cover: when to ask directly, when to search, when to run multi-agent deep research, with the cost and time of each where a source states them; how models fail (confident, specific, wrong; stale facts presented as current; invented citations), with the studies that measured it; how to read a research report (the hierarchy of sources, vendor data, correlation against cause); why the writer of a text should not be its checker, and what a fresh context changes; the stratified-sample audit as a rule, with the arithmetic of what a clean sample can and cannot show; checking a checker; the Academy case's own first-check and audit numbers, as an anecdote. Deliverable: a verification protocol as a checklist, with a sampling rule by the stakes of the text, the arithmetic shown, and a brief for a fresh checker; then the template for your project."),
("BW7", "Pipelines: raw material to finished output",
 "Chaining steps, routing each to a model, where a model helps a writer and where it flattens a voice, and the rule that the final pass is human.",
 "a pipeline as a runnable procedure",
 "Unit BW7, Pipelines: raw material to finished output. Cover: what a pipeline is (stages, each with a defined input and output and one model); hand-offs as files rather than as conversation; where a human gate sits and what it checks; what the studies on writing with language models found, where a model helps (structure, cuts, options) and where it flattens (first-person prose, humour, endings), with the models and tasks each study used; the rule that the final pass is yours; steps that can be re-run without harm; logging what ran; the Academy case's pipeline (brief, writer, fresh check, applying findings, filing, build, checks, publishing) with the points where it failed. Deliverable: a pipeline written as a runnable procedure (numbered steps, input, output, model, gate, done-when), worked on the Academy case; a second, short worked example on neutral material (interview notes to a report, a summary and an email), its content invented and labelled; then the template for your project."),
("BW8", "Skills and automation",
 "What a skill is, why its description carries the trigger, scheduled tasks and their limits, and when a procedure is worth automating.",
 "one skill written in full, with a trigger test set",
 "Unit BW8, Skills and automation. Cover: the forms a reusable procedure takes (a saved prompt, a project instruction, a skill) and how to choose; what a skill is as its format's own documentation defines it, how triggering works and why the description matters more than the body; testing whether it triggers; scripts inside a skill for the steps that must be exact; scheduled tasks, what they can and cannot touch, dated; counting the repeats before automating; what a skill must never hold. Deliverable: one skill written in full and ready to install, a fresh check of a draft's claims against its sources (it reuses BW6's checker brief): the skill file, a checking script, install steps, a sixteen-request trigger test set, one scheduled task, and its done-when lines."),
("BW9", "Agents",
 "Agent against chat, the autonomy slider, what agents do well and what they quietly wreck, and the guardrails.",
 "agent-use decision rule + guardrail checklist",
 "Unit BW9, Agents. Search before writing. Cover: what an agent is against a chat (tools, loops, autonomy); the autonomy slider and verifiability as the test of what to delegate, each from its primary source; what a coding agent lets someone who does not write code build, and what it does not; subagents and isolated contexts, why they help and what they cost in tokens, as the vendor publishes it, dated; what agents do well (parallel research, repetitive edits, builds with tests) and what they quietly wreck (silent wrong assumptions, overwriting, cost blowups); guardrails (scopes and permissions, dry runs, review gates, version control as the undo for someone who does not write code); injected instructions in material an agent reads, from the primary source on that risk; the Academy case's own agent failures and the rules that followed. Deliverable: an agent-use decision rule in prose with a line that holds on every path, also drawn as a decision figure; a guardrail checklist; and a brief template for a first agent task."),
("BW10", "Cost, limits, privacy",
 "What a plan measures, what burns usage for no gain, when a new chat is cheaper, and what the vendor keeps.",
 "usage rules + a table of what material belongs where",
 "Unit BW10, Cost, limits, privacy. Search before writing. Cover: what a subscription measures and how its usage windows work, as the vendor states today, with a plain statement of what it does not publish; what burns usage for no gain (re-reading large files, giant pastes, chats that never end, research run twice); when a new chat is cheaper; a token budget per task type; caching as far as it is documented; what the vendor keeps, for how long, and the settings that govern training use, each from the vendor's own page, dated; which material belongs in memory, in a project, in a private store or nowhere; work material and an employer's policy, as a question for you to answer. Deliverable: numbered usage rules, each with its source, and a table of what material belongs where; then the template for your project."),
("DD-BW1", "Deep dive: how the best practitioners work",
 "The documented methods that have a named author and a primary source, each graded by its evidence and tested for transfer from code to knowledge work.",
 "method cards + ten operating rules",
 "Deep dive BW1, How the best practitioners work. Written after the ten core units. Search first and open every primary source; date each fact. Cover every method the source unit covers, each rebuilt from its author's own posts, talks, repositories and papers and re-verified today, discarding any practice a secondary source attributes to someone whose own words do not support it; add any method with a named author and a primary source published since the source unit was written (29 Oct 2026). For every method: what it claims, what evidence it rests on, who it was written for, its grade (measured, documented practice, stated opinion), and whether it transfers from software to knowledge work, decided case by case; where a method is for software only, say so and leave it there. Then which of them the ten core units already teach, by code. Deliverable: method cards, one per method (author, primary source with date, the claim in one sentence, the grade, what transfers and what does not), then ten operating rules, each traced to a card."),
("DD-BW2", "Deep dive: one project, with its numbers",
 "What the Academy case built, its error counts at first check, what each audit caught and what failed in operation, taken from the project's own records.",
 "the case report + a ranked list of changes the record supports",
 "Deep dive BW2, One project, with its numbers. Cover, from the Academy case file and the staged records only: what was built, by count; the method as it was run; errors found per unit at the fresh check, as a table; what each sample audit found and what it led to; the kinds of error that recur; figures that failed their checks and what fixing them took; what failed in operation (lost agents, restarts, a publish that had to be repeated); what was recorded about cost in chats and time, and what was not; and what one person's record cannot show (no control, no second project). Label the whole as an anecdote. Deliverable: the case report, and the ten changes the record supports, ranked, each tied to its count and to the unit of this course that teaches it."),
("DD-BW3", "Deep dive: audit your own usage",
 "A method for classifying your own chats by task, model, outcome and turns, with one person's findings as the worked example.",
 "gap-report template + a sixty-minute procedure",
 "Deep dive BW3, Audit your own usage. Written last. Cover: why a review of your own chats finds what a course cannot; the method (choose a window, list every chat, classify each ask by task type, model, outcome and number of turns), with each label defined and its limits said; the patterns to look for (an ask that was badly put, a tool wrong for the job, work done by hand that a saved procedure already does, research paid for twice); testing the rules of BW10 and DD-BW1 against your own record; the privacy of doing this at all; and the worked example from the Academy case file, one person's review of 53 chats over six days, labelled as an anecdote. Deliverable: a classification sheet, a gap-report template, the review as a sixty-minute procedure, and the worked example's highest-leverage changes restated so they apply to any reader."),
]

AIMS = {
'BW1': ("say what the model could see when an output fails, and what to change",
        "B1 as source material",
        "the vocabulary every later unit uses; the diagnosis table BW3, BW4 and BW6 point back to"),
'BW2': ("route each recurring task of your project to a model tier and an effort level, with the reason",
        "B2 as source material; its lineup and prices are re-read, not carried over; BW1",
        "the routing table BW7 assigns stages from and BW10 budgets"),
'BW3': ("brief a task so that the first output is usable",
        "B3 as source material; its ten templates are replaced by ten for general project work; BW1, BW2",
        "the brief form BW5 uses per unit, the checker brief BW6 builds and the stage briefs of BW7"),
'BW4': ("lay out a project so that the model is told what it needs each turn and nothing stale",
        "B4 as source material; its audit is summarised in the Academy case file; BW1, BW3",
        "the project structure BW5 specifies into and BW8 automates"),
'BW5': ("turn an idea into a one-page spec and a build order that one context per unit can finish",
        "DD-B3, its spec-driven section, and docs/method.md as source material; this unit has no counterpart in the private course; BW3, BW4",
        "the spec and build order every later deliverable is built against; the flag-and-review rule BW7 and BW9 rely on"),
'BW6': ("verify AI-written work by sample before you trust it, and know what a clean sample proves",
        "B6 as source material; BW1, BW2, BW5",
        "the checker brief BW8 turns into a skill; the verifiability test BW9 uses to decide what to delegate"),
'BW7': ("write your project's repeated work as a pipeline with a model per stage and a human gate",
        "B7 as source material, for its studies and its pipeline form only; BW2, BW3, BW5, BW6",
        "the procedure BW8 automates and BW9 hands in part to an agent"),
'BW8': ("write one reusable skill for your project and test that it triggers",
        "B5 as source material; its deliverable is replaced; BW4, BW6, BW7",
        "the skill form BW9's agents load"),
'BW9': ("decide which tasks to hand to an agent and with what guardrails",
        "DD-B1 as source material; BW5, BW6, BW7, BW8",
        "the decision rule DD-BW1's methods are tested against; the agent rules BW10 costs"),
'BW10': ("keep a project inside its plan's limits and keep the wrong material out of the tool",
         "B8 as source material; every limit, price and retention fact is re-read; BW1, BW2, BW4, BW9",
         "the usage rules DD-BW3 tests against a reader's own record"),
'DD-BW1': ("name the documented methods worth adopting, with the evidence each rests on",
           "DD-B3 as source material; BW1 to BW10",
           "the operating rules DD-BW3 tests"),
'DD-BW2': ("read one real project's record and say which of the course's rules its numbers support",
           "the Academy case file and the records its row stages (fresh-check reports, audit reports, the changelog), private details removed; B6, for its count of first drafts with an error; BW1 to BW10",
           "the worked record DD-BW3 sets a reader's own review beside"),
'DD-BW3': ("review your own chats and write the ten changes that would save you the most",
           "DD-B2 as source material, for its method and its counts only, every personal detail removed; BW10, DD-BW1, DD-BW2",
           "nothing; it is the course's last unit"),
}
