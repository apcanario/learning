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
VERSION = 'v1 · 11 Nov 2026'
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
READINGS = []

# ---- build order -----------------------------------------------------------------------
DONE_ROWS = []
ORDER = [("PB1", "Opus 5.5", "on"), ("PB2", "Opus 5.5", "off"), ("PB3", "Opus 5.5", "on"), ("PB4", "Opus 5.5", "off"),
         ("PB5", "Opus 5.5", "off"), ("PB6", "Opus 5.5", "on"), ("PB7", "Opus 5.5", "on"), ("PB8", "Opus 5.5", "on"),
         ("PB9", "Opus 5.5", "on"), ("PB10", "Opus 5.5", "off"), ("DD-PB1", "Opus 5.5", "on"), ("DD-PB2", "Opus 5.5", "off")]
STATUS = {}          # unit code -> status text in the build-order table once filed
AUDIT_EVERY = 4
AUDIT_ROW = ('Stratified-sample audit of the last four units', 'Fable 5.1', 'on', 'prompt on Audits page')
FINAL_AUDIT = ('Audit 4', 'Final audit of the last units plus a full read of the course against its goal, and a read-through as the persona', 'Fable 5.1', 'on', '')
NEXT_UNIT, AUDITS_RUN, NEXT_AUDIT = 'PB1', 0, 'after four units; deferred to the Fable stage (decided 11 Nov 2026), so it gates no unit'

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
    ('2026-11-11 23:59', "v1. Course created (new-course skill; backlog row G-0): frame, goal and three outcomes, 12 units with one brief each and their Aim, Takes and Gives lines, the shared preamble with the reader persona, the build order in syllabus order, the syllabus-flags file. Adapted from a private course of the Learning Project; no unit written."),
]
