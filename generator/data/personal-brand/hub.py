"""Building a Personal Brand on Instagram and YouTube: the course data (11 Nov 2026).

kit/build.py renders it into Academy through kit/mdcourse.py (one Academy course per entry in COURSES), on design/theme.css.
Everything a reader sees of the course is here or in units_data.py beside this file (the units and their briefs: PRE, PB, AIMS).
Edit content here; edit style only in design/theme.css. Prose blocks are HTML strings and may use only theme classes
(design/README.md lists them). This is a public course: no private term may appear in this folder (kit/private_terms.py).
The decisions behind it are docs/public-courses.md.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# ---- identity --------------------------------------------------------------------------
TITLE = 'Building a Personal Brand'
BAR = 'PERSONAL BRAND'
BRAND_HTML = 'PERSONAL <span>/</span> BRAND'
OUT = 'personal-brand.html'
THEME_KEY = 'personal-brand-theme'
VERSION = 'v5 · 12 Nov 2026'
LEARN_C, BUILD_C = 'var(--teal)', 'var(--orange)'

# ---- units -----------------------------------------------------------------------------
_ns = {}
exec((HERE / 'units_data.py').read_text(), _ns)
PRE, PB, AIMS = _ns['PRE'], _ns['PB'], _ns['AIMS']   # AIMS: aim, takes, gives per unit

GOAL_PB = ('by the end of the course you can state in one sentence who your account is for and what it gives them; have run a publishing system for twelve weeks inside an hours budget you set yourself; and read your Instagram and YouTube numbers against sourced benchmarks each quarter to decide, with evidence, whether to continue, change format or stop.')
NAME_PB = 'Building a Personal Brand on Instagram and YouTube'

COURSES = [
    dict(key='PB', name=NAME_PB, color='var(--teal)', units=PB, goal=GOAL_PB, slug='pb',
         tile='A step-by-step guide to a personal brand and a following on Instagram and YouTube, for someone with a job, a phone and a few hours a week. Every number sourced.',
         intro='For an adult with a real skill, a full-time job and 3 to 10 hours a week: what to expect, how to position the account, how to build a publishing system and make the pieces with a phone, how growth works on YouTube and on Instagram, what the rules are, what pays, and how to read the numbers each quarter. Worked throughout on one fictional creator, Mara Venn, and shipped each time as a template. Ten core units in four parts and two deep dives.',
         outcomes='<li><strong>Outcome 1</strong> — a positioning a stranger can repeat, live on both profiles (PB2, PB3; DD-PB1 sets it beside six documented creators).</li><li><strong>Outcome 2</strong> — a publishing system held for twelve weeks inside your own hours budget (PB4, PB5, PB8).</li><li><strong>Outcome 3</strong> — a quarterly decision to continue, change format or stop, made on your numbers against sourced benchmarks (PB1, PB6, PB7, PB9, PB10; DD-PB2).</li>'),
]
COURSE_NOTE = 'Every unit is sourced to peer-reviewed work, platform-official statements or large-sample data, labels anecdote and vendor data as such, says where no source exists, and ends with a deliverable built in full for a fictional creator and then as a template.'

# ---- written material (reading pages) ---------------------------------------------------
# A unit is written when its file is in the vault, courses/personal-brand/ (A5); kit/build.py derives WRITTEN from it.
READINGS = [
    dict(id='read-pb1', course='PB',
         title='What to expect: odds, timeline, cost', covers=['PB1'], name='PB1 · What to expect',
         intro="Unit PB1, written 12 Nov 2026 by Opus 5.5 in an isolated agent context that saw only its brief (with the Aim, Takes and Gives lines), the writing skill, sourcing Parts 1 and 5, the figure kinds, Mara's register and its source material, search on (every changeable fact dated, checked 12 Nov 2026); fresh check the same day by a separate Opus 5.5 agent that had not seen the writing: fix, 1 error, 6 should-fix, 7 minor, all applied (a Fable 5.1 fresh check is owed). What a one-person account can expect on YouTube and on Instagram from the largest datasets found (vidIQ's studies of 33 million and 137,000 channels, Metricool, Socialinsider, Buffer), each with its sample, date and label; the milestones and the monetisation thresholds as YouTube states them, with the 1 February 2027 change; months to each milestone where data exists; the plateau, who continues, the cost of a phone-only setup, survivor bias and what no dataset measures; four figures. Deliverables: Mara's expectation sheet (21 rows), her hours-and-money budget, her stop rule and the four checkpoint dates of her first year, then all three as templates. Known gaps: the Instagram data is thin: no dataset covers accounts under 1,000 followers or follows new accounts, so the Instagram row for followers at 12, 24 and 36 months is unsourced and left for PB7; Instagram states no thresholds for its earning tools on its public pages; Buffer's frequency model is unpublished and Metricool's growth figure undefined; no dataset follows YouTube channels past 360 days. About 8,200 words with the deliverable."),
    dict(id='read-pb2', course='PB',
         title='Positioning: the sentence a stranger can repeat', covers=['PB2'], name='PB2 · Positioning',
         intro="Unit PB2, written 12 Nov 2026 by Opus 5.5 in an isolated agent context that saw only its brief (with the Aim, Takes and Gives lines), the writing skill, sourcing Parts 1 and 5, the figure kinds, Mara's register, PB1 and its source material, search off (used only to re-check what it carried over, the platforms' name, handle and text-field rules, and the handles chosen for Mara); fresh check the same day by a separate Opus 5.5 agent that had not seen the writing: fix, 1 error, 3 should-fix, 6 minor, all applied (a Fable 5.1 fresh check is owed). What a positioning is, against a description of the person (Ries and Trout); the three patterns a personal brand is built on, a topic, a method or repeatable format and the person, with the evidence on how each survives a change of subject graded (thin: platform tips, one vendor dataset, brand-extension research on products and celebrities, creator cases); the repeat-back test with strangers; the account name against the handle, each platform's limits and change rules dated, and the availability check; the Instagram bio and the YouTube description as the fields that carry it; three figures. Deliverables: Mara's positioning sentence and 60-word expansion, three name options with their checks and the pick, her Instagram profile and YouTube channel copy written in full and counted, and the repeat-back test as a script; then the template. Known gaps: none of the handles could be checked inside the two apps, so the pick is provisional until claimed; Instagram's bio, username and name-field limits rest on third parties; the test's number of strangers, delay and pass mark are conventions with no source. About 6,900 words with the deliverable, above the brief's guide; nothing was cut to meet it."),
    dict(id='read-pb3', course='PB',
         title='Audience and the two platforms', covers=['PB3'], name='PB3 · Audience and platforms',
         intro="Unit PB3, written 12 Nov 2026 by Opus 5.5 in an isolated agent context that saw only its brief (with the Aim, Takes and Gives lines), the writing skill, sourcing Parts 1 and 5, the figure kinds, Mara's register, PB1, PB2 and its source material, search on (every changeable fact dated, checked 12 Nov 2026); fresh check the same day by a separate Opus 5.5 agent that had not seen the writing: fix, 1 error, 5 should-fix, 6 minor, all applied (a Fable 5.1 fresh check is owed). An audience described by what its members do and need, each trait with its basis and label; who uses YouTube and Instagram by age and gender from Pew's 2026 survey (US) and Ofcom's 2025 report (UK, YouTube only); what each platform does for a small account, from the platforms' own statements and vendor datasets on reach and shelf life; what is and is not measured about Shorts or Reels viewers becoming long-form viewers (no published rate); the email list as the channel you own, with the open-rate and conversion data that exists and no follower-to-subscriber rate; how to split 3, 6 and 10 hours a week between the platforms, and what is cut first in a bad week; four figures. Deliverables: Mara's audience profile (PB2's audience tested and kept, ten traits each with its basis and label) and her platform allocation at the three budgets with the cut order (no Shorts at 6 hours; one short email per video once the data-protection question is answered), then both as templates. Known gaps: no survey splits platform use by age across the EU; Instagram's reach split between followers and non-followers is not published for small accounts; Fanpage Karma's sample has no account count; the GetResponse report page and the EUR-Lex text were not re-opened by the fresh check. About 7,500 words with the deliverable, above the brief's guide; most of the excess is the deliverable's tables."),
    dict(id='read-pb4', course='PB',
         title='The content system', covers=['PB4'], name='PB4 · The content system',
         intro="Unit PB4, written 12 Nov 2026 by Opus 5.5 in an isolated agent context that saw only its brief (with the Aim, Takes and Gives lines), the writing skill, sourcing Parts 1 and 5, the figure kinds, Mara's register, PB1 to PB3 and its source material, search off (used to re-open every carried claim and every source it adds, 12 Nov 2026); fresh check the same day by a separate Opus 5.5 agent that had not seen the writing: fix, 0 errors, 8 should-fix, 15 minor, all applied (a Fable 5.1 fresh check is owed). The capture layer recorded during the work itself; the anchor piece and its fortnightly cadence; the derivative layer on Instagram at the rates PB3 set; series and seasons, with the evidence from other settings on bounded goals and fresh starts labelled as inference; batching in two windows a fortnight and what the task-switching research does and does not support; the idea backlog; what is dropped first when a week is lost; YouTube's own statement that it found no link between breaks and views, beside the vendor data on gaps; three figures. Deliverables: the system as a reusable checklist, and Mara's run-in and 12-week calendar with hours per item, every week summed and inside 6 hours; then the template calendar with the rules for 3 and for 10 hours a week. Known gaps: no source gives hours per video or per post, or restoration time per piece, so every hour below the line totals is a labelled planning estimate; the only published editing figure is a vendor rule of thumb without method; Instagram's current scheduling limit was not confirmed. About 9,100 words with the deliverable and templates, above the brief's guide; nothing was cut to meet it."),
]

# ---- build order -----------------------------------------------------------------------
DONE_ROWS = []
ORDER = [("PB1", "Opus 5.5", "on"), ("PB2", "Opus 5.5", "off"), ("PB3", "Opus 5.5", "on"), ("PB4", "Opus 5.5", "off"),
         ("PB5", "Opus 5.5", "off"), ("PB6", "Opus 5.5", "on"), ("PB7", "Opus 5.5", "on"), ("PB8", "Opus 5.5", "on"),
         ("PB9", "Opus 5.5", "on"), ("PB10", "Opus 5.5", "off"), ("DD-PB1", "Opus 5.5", "on"), ("DD-PB2", "Opus 5.5", "off")]
STATUS = {'PB1': 'written 12 Nov', 'PB2': 'written 12 Nov', 'PB3': 'written 12 Nov', 'PB4': 'written 12 Nov'}          # unit code -> status text in the build-order table once filed
AUDIT_EVERY = 4
AUDIT_ROW = ('Stratified-sample audit of the last four units', 'Fable 5.1', 'on', 'prompt on Audits page')
FINAL_AUDIT = ('Audit 4', 'Final audit of the last units plus a full read of the course against its goal, and a read-through as the persona', 'Fable 5.1', 'on', '')
NEXT_UNIT, AUDITS_RUN, NEXT_AUDIT = 'PB5', 0, 'after four units; deferred to the Fable stage (decided 11 Nov 2026), so it gates no unit'

# ---- prose blocks (theme classes only) ---------------------------------------------------
HOME_H1 = 'Building a Personal Brand on Instagram and YouTube'
HOME_LEDE = 'A step-by-step guide to a personal brand and a following on Instagram and YouTube, for someone with a job, a phone and a few hours a week. Every number sourced.'
LEARN_TILE = ('The course', 'Goal, outcomes, units, and the written material to read.')
BUILD_TILE = ('How the course gets made', 'Procedure, model rules, every brief, audit prompts, bibliography, changelog.')

FRAME = """<h2 class="hsec">Frame</h2>
<div class="report">
  <h2>A guide that says what the evidence supports, and where there is none</h2>
  <p>Most advice on growing an account is one person's survivor story or a vendor's sales page. This course keeps the questions a beginner asks (what should I expect, what do I post, how does the algorithm work, when does it pay) and answers each only as far as a source allows: platform documentation, large datasets with their sample and date, peer-reviewed studies, and creator cases with verifiable numbers. Where no source meets that standard the unit says so. It is written for someone who has a job and a few hours a week, on a phone, on two platforms: Instagram for reach and YouTube for depth.</p>
</div>
<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>Ten steps in reading order, one fictional creator, every deliverable twice.</strong></p>
  <ul><li>Steps in order: decide, build, grow, protect, earn, review.</li><li>Mara's worked case keeps deliverables built, never blank forms.</li><li>A template after each lets the reader do their own.</li></ul>
  <p class="over"><strong>Override if:</strong> after PB4 Mara's case cannot carry a reader in a very different niche; then a second, contrasting case is added from PB5 on.</p>
</section>
<div class="report"><ul>
  <li><strong>Reader:</strong> an adult with a real skill, a full-time job, under 1,000 followers, a phone and 3 to 10 hours a week. Every brief says so.</li>
  <li><strong>Example:</strong> Mara Venn, fictional: an accountant who restores mid-century furniture at weekends. Every fact about her is invented by the unit that needs it, labelled, and kept in a register.</li>
  <li><strong>Neutral ground:</strong> no country's tax figures, no single currency; law is a list of questions with the primary source to open for the EU, the UK and the US.</li>
  <li><strong>Where the evidence pushes back:</strong> most published growth figures are vendor data and correlational, and creator histories are a sample of survivors. The course labels both and keeps them out of any deliverable they cannot support.</li>
</ul></div>"""

LEARN_LEDE = 'Read here. Everything about how the units get written lives in Build.'
LEARN_NOTE = 'Order of writing: the ten core units in reading order, PB1 to PB10, then the two deep dives; PB1, PB3, PB6, PB7, PB8, PB9 and DD-PB1 with search on.'
LEARNING_NOTE = ''

BUILD_LEDE = 'Method, model rules, and the pages that hold the briefs, the audits and the sources. Nothing here is course content.'
BUILD_PICK = """<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>PB1 first: what to expect, before any advice on how.</strong></p>
  <ul><li>The expectation sheet is what every later unit is measured against.</li><li>Its source unit is the most generic of the private course.</li><li>Instagram benchmarks are new research; better found early.</li></ul>
  <p class="over"><strong>Override if:</strong> the Instagram data proves too thin for a sheet; then PB1 ships the YouTube rows and PB7 completes it.</p>
</section>"""
BUILD_BODY = """<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in syllabus order. The chat stages a packet for a fresh writer: the unit's brief from this course's Briefs page, never reworded; the source units its Takes line names; every unit of this course already filed; and Mara's register of facts.</li>
    <li>The writer re-verifies every claim it carries over from a source unit and reports three lists with the unit: mistakes found in the source units, contradictions with a filed unit or with the brief of an unwritten one, and needs the syllabus does not meet.</li>
    <li>A fresh checker that has not seen the writing checks every cited claim against its source, the deliverable against the brief, every figure against the text, and the unit against the list of private terms. Its report is filed as <code>audits/personal-brand/fresh-check-&lt;code&gt;.md</code> before any fix; findings are applied as exact replacements.</li>
    <li>Verified mistakes are corrected where they sit, each with a dated note. Contradictions and needs are appended to <code>generator/data/personal-brand/syllabus-flags.md</code>; a brief is changed only by a syllabus review that the Project's owner confirms. Mara's register, <code>generator/data/personal-brand/case-facts.md</code>, is appended at every filing.</li>
    <li>The unit is filed at <code>courses/personal-brand/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7; this data file is updated; Academy is rebuilt, verified and published, the artifact and then GitHub Pages.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same context as its unit.</li>
    <li><strong>Fresh check: Opus 5.5</strong> in a separate context, with a Fable 5.1 fresh check owed to the Fable stage.</li>
    <li><strong>Audits: Fable 5.1</strong>, deferred to the Fable stage (decided 11 Nov 2026); until then no audit gates a unit.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or audits.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>After every four written units, Fable 5.1 audits by stratified sample: one claim per section per unit, checked against its source; more than one in ten fails → full audit of that unit. These audits are owed and run at the Fable stage. Units written with live search (PB1, PB3, PB6, PB7, PB8, PB9, DD-PB1) are re-checked for staleness six months after writing.</p>
</section>"""

ORDER_LEDE = "One row per unit in writing order, which is the reading order; an audit row every fourth written unit. Opus 5.5 writes; Fable 5.1 audits. \"Search\" means the unit is written with web search on because its facts are current."
ORDER_NOTES = """<div class="report"><ul>
  <li><strong>Why this order:</strong> the course is a sequence of steps, so the writing order is the reading order: Part 1 decides (expectations, positioning, audience and platforms), Part 2 builds the machine (the system, the craft), Part 3 explains growth on each platform, Part 4 covers the rules, the money and the quarterly review that reads everything before it; the deep dives last.</li>
  <li><strong>Audit gate:</strong> the four-unit audits are deferred to the Fable stage, so none stops a unit; a REWRITE verdict, once one exists, still does.</li>
  <li><strong>Syllabus flags:</strong> a unit that finds a contradiction or a need raises a flag; a flag that names the next unit travels to its writer; a flag that would change a brief waits for a syllabus review.</li>
</ul></div>"""
ORDER_FOOT = "The count starts at {start}."

BRIEFS_LEDE = 'One brief per unit, self-contained: the shared preamble (the reader, the source-material rule, Mara, the neutral-ground rule, the course goal, the sourcing standard, the tone) is baked into every open brief, followed by the unit\'s Aim, Takes and Gives lines. Written units show their note instead. The course itself is read in <a href="#course-{k}" data-target="course-{k}">Learn · Course {K}</a>.'
BRIEF_LABEL = 'Opus brief'

AUDITS_LEDE = "No audit yet. Each audit records: units sampled, claims checked, failures, verdict (pass / full audit / rewrite), and what changed."
AUDIT_LOG = []
AUDIT_PROMPTS_NOTE = "Run in the Learning Project with Fable 5.1 after every fourth written unit (deferred to the Fable stage). Paste the units or point at their vault paths. The prompts are method.md §6, verbatim."
AUDIT_PROMPTS = [
    ('Stratified-sample audit (every four units)', True, """You are auditing four units of a self-study course written by Opus 5.5 for one reader. Units: {list the four unit codes and their vault paths}.

Method, in this order:
1. For each unit, list its sections. From every section draw one claim that carries a number, a named source, a mechanism or a recommendation. That is the sample; record it before checking anything.
2. Check each sampled claim against the source the unit cites: open the source; confirm the figure, the date, the sample size and that the claim is what the source says, not a stretch of it. Mark each claim PASS, FAIL (wrong, unsupported, miscited, or invented) or STALE (true when written, superseded now, with the newer figure).
3. For each unit compute the failure rate. If more than one claim in ten is FAIL, audit that unit in full: every cited claim, same procedure.
4. Check the deliverable: it exists in full inside the unit, it follows from the unit's evidence, and it is usable without reading the unit.
5. Check against the course goal and sourcing standard (in the unit's preamble): does the unit move the reader toward the stated outcomes, and is anything in it advice without evidence?

Output: a table per unit (section, claim, source, verdict, note); the failure rate; a verdict per unit (PASS / FULL AUDIT RUN, result / REWRITE with the sections named); the three most consequential errors across the four units in plain language; and one line each for the bibliography (new sources to add, sources to mark failed) and the changelog. Do not fix the units; report."""),
    ('Staleness check (six months after a live-search unit)', False, """You are re-checking one unit written with live search six months ago: {unit code, vault path, date written}. Search again, today, for every fact in it that can change: platform rules and thresholds, prices and plan limits, model lineups, benchmark figures, regulatory status, the numbers attached to named creators. For each: the value in the unit, the value now, the source and date for the new value, and whether the unit's conclusion still holds. End with a verdict: CURRENT / PATCH (list the lines to change) / REWRITE (say which sections). Do not rewrite; report."""),
]


BIB_NOTE = 'Every link cited in the written material, alphabetical by title. New units add to this list; a source that fails a staleness check is marked here.'
TEMPLATE_LEDE = 'What a course needs before the first unit is written: see the new-course skill and design/README.md.'
TEMPLATE_NOTE = ''
TEMPLATE_BLOCKS = []

# newest first
CHANGELOG = [
    ('2026-11-12 12:00', "v5. PB4 The content system written (Opus 5.5, own agent context, search off; row W-PB4, P31), fresh-checked by Opus 5.5 in a separate context (fix, 0 errors, 8 should-fix, 15 minor; all applied; Fable 5.1 fresh check owed), its three figures passed, and filed: reading page, PB4 marked written; PB5 next, held by the syllabus review S-PB1; Mara's register gains PB4's facts; PB1 and PB3 §6 gain YouTube's statement on breaks (found by PB4's writer, confirmed by its checker; flag F35); flags F9, F15 and F23 carried, F30 to F35 raised; F2, F5 and F20 back to open after W-PB3 had marked them carried. Audit 1's four units written, owed to the Fable stage. Writer's Object line: none."),
    ('2026-11-12 09:45', "v4. PB3 Audience and the two platforms written (Opus 5.5, own agent context, search on; row W-PB3, P31), fresh-checked by Opus 5.5 in a separate context (fix, 1 error, 5 should-fix, 6 minor; all applied; Fable 5.1 fresh check owed), its four figures passed (the flow's caption fixed as the report gives it), and filed: reading page, PB3 marked written; PB4 next; Mara's register gains PB3's facts; PB1's D2 corrected (publishing and replies 1.25, email 0.25 hours a fortnight; flag F21); flags F2, F5, F14 and F20 carried, F21 to F29 raised. Writer's Object line: none."),
    ('2026-11-12 05:30', "v3. PB2 Positioning: the sentence a stranger can repeat written (Opus 5.5, own agent context, search off; row W-PB2, P31), fresh-checked by Opus 5.5 in a separate context (fix, 1 error, 3 should-fix, 6 minor; all applied; Fable 5.1 fresh check owed), its matrix figure (a finding) and its decision figure (handles broken mid-word on a phone) fixed and each passed a re-check, the flow passed, and filed: reading page, PB2 marked written; PB3 next; Mara's register gains PB2's facts; flags F13 to F20 raised. Writer's Object line: none."),
    ('2026-11-12 03:30', "v2. PB1 What to expect: odds, timeline, cost written (Opus 5.5, own agent context, search on; row W-PB1, P31), fresh-checked by Opus 5.5 in a separate context (fix, 1 error, 6 should-fix, 7 minor; all applied; Fable 5.1 fresh check owed), its four figures passed or fixed and re-checked, and filed: reading page, PB1 marked written; PB2 next; Mara's register gains PB1's facts; flag F1 carried, flags F3 to F12 raised. Writer's Object line: none."),
    ('2026-11-11 23:59', "v1. Course created (new-course skill; backlog row G-0): frame, goal and three outcomes, 12 units with one brief each and their Aim, Takes and Gives lines, the shared preamble with the reader persona, the build order in syllabus order, the syllabus-flags file. Adapted from a private course of the Learning Project; no unit written."),
]
