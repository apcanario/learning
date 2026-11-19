"""Supply Chain Execution for Product Teams: the course data (19 Nov 2026, row S-SCE0).

kit/build.py renders it into Academy through kit/mdcourse.py (one Academy course per entry in COURSES), on design/theme.css.
Everything a reader sees of the course is here or in units_data.py beside this file (the units and their briefs: PRE, SCE, AIMS).
Edit content here; edit style only in design/theme.css. Prose blocks are HTML strings and may use only theme classes
(design/README.md lists them). This is a public course: no private term may appear in this folder (kit/private_terms.py).
The syllabus is docs/supply-chain-execution-syllabus.md (sections 1 to 5 give the fields below); the decisions are docs/public-courses.md.
The course has no source units: nothing is adapted from another course.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# ---- identity --------------------------------------------------------------------------
TITLE = 'Supply Chain Execution for Product Teams'
BAR = 'SUPPLY CHAIN EXECUTION'
BRAND_HTML = 'SUPPLY CHAIN EXECUTION <span>/</span> FOR PRODUCT TEAMS'
OUT = 'supply-chain-execution.html'
THEME_KEY = 'supply-chain-execution-theme'
VERSION = 'v1 · 19 Nov 2026'
LEARN_C, BUILD_C = 'var(--gold)', 'var(--teal)'

# ---- units -----------------------------------------------------------------------------
_ns = {}
exec((HERE / 'units_data.py').read_text(), _ns)
PRE, SCE, AIMS = _ns['PRE'], _ns['SCE'], _ns['AIMS']   # AIMS: aim, takes, gives per unit

# syllabus §3, word for word but for the first letter (the course page capitalises it)
GOAL_SCE = ('by the end, the reader can take any screen, feature or roadmap item in order, warehouse or transport software, say what physical work it stands for, who uses it and who pays for it, and argue from that what the product should do.')
NAME_SCE = 'Supply Chain Execution for Product Teams'

COURSES = [
    dict(key='SCE', name=NAME_SCE, color='var(--gold)', units=SCE, goal=GOAL_SCE, slug='sce',
         tile='For people who build, sell or implement order, warehouse or transport software with no operations background: how warehouses, transport and orders run, who works in them, how the software that runs them is bought, and what it costs. Every claim sourced and graded.',
         intro='Learning the domain: how warehouses, transport and orders run, who works in them, how the software that runs them is bought, and what it costs. Operations first, then people, then money, with the warehouse given the most room; AI features are out of scope, no real vendor is assessed, and the worked examples use three fictional operations and three fictional vendors. Eighteen core units in an opening and three parts, and two deep dives.',
         outcomes='<li><strong>Outcome 1 · Operations.</strong> Walks one order from promise to delivery and names, at every step, the physical event, the system, the user role and the common failure, without notes (SCE1 to SCE10, DD-SCE2).</li><li><strong>Outcome 2 · Buyers and users.</strong> For a given feature, writes a two-sided case: each buyer card\'s reason to pay and each role card\'s reason to use or avoid it, with the grade of the evidence (SCE5, SCE8, SCE9, SCE11 to SCE15, DD-SCE1).</li><li><strong>Outcome 3 · The market and the money.</strong> Builds a competitor sheet and a total-cost model for a real market from public sources, and writes a product strategy memo that rests on them (SCE6, SCE16, SCE17, SCE18).</li>'),
]
COURSE_NOTE = 'Every unit is sourced to operations research, standard textbooks, industry surveys, analyst reports, audited filings and vendors\' own dated pages, grades every claim (independent, analyst, vendor-reported, practice), assesses no real vendor, and ends with a deliverable built in full on the fictional case and then as a template.'

# ---- written material (reading pages) ---------------------------------------------------
# A unit is written when its file is in the vault, courses/supply-chain-execution/ (A5); kit/build.py derives WRITTEN from it.
READINGS = []

# ---- build order -----------------------------------------------------------------------
DONE_ROWS = []
ORDER = [("SCE1", "Opus 5.5", "on"), ("SCE2", "Opus 5.5", "off"), ("SCE3", "Opus 5.5", "off"), ("SCE4", "Opus 5.5", "off"),
         ("SCE5", "Opus 5.5", "off"), ("SCE6", "Opus 5.5", "on"), ("SCE7", "Opus 5.5", "off"), ("SCE8", "Opus 5.5", "on"),
         ("SCE9", "Opus 5.5", "on"), ("SCE10", "Opus 5.5", "off"), ("SCE11", "Opus 5.5", "on"), ("SCE12", "Opus 5.5", "on"),
         ("SCE13", "Opus 5.5", "off"), ("SCE14", "Opus 5.5", "off"), ("SCE15", "Opus 5.5", "off"), ("SCE16", "Opus 5.5", "on"),
         ("SCE17", "Opus 5.5", "on"), ("SCE18", "Opus 5.5", "off"), ("DD-SCE1", "Opus 5.5", "on"), ("DD-SCE2", "Opus 5.5", "off")]
STATUS = {}          # unit code -> status text in the build-order table once filed
NEXT_UNIT = 'SCE1'

# ---- prose blocks (theme classes only) ---------------------------------------------------
HOME_H1 = 'Supply Chain Execution for Product Teams'
HOME_LEDE = 'For people who build, sell or implement order, warehouse or transport software with no operations background: how warehouses, transport and orders run, who works in them, how the software that runs them is bought, and what it costs. Every claim sourced and graded.'
LEARN_TILE = ('The course', 'Goal, outcomes, units, and the written material to read.')
BUILD_TILE = ('How the course gets made', 'Procedure, model rules, every brief, bibliography, changelog.')

FRAME = """<h2 class="hsec">Frame</h2>
<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>Operations first, then people, then money. Warehouse gets the most room.</strong></p>
  <ul><li>A screen cannot be improved without knowing the physical event behind it.</li><li>Product work needs buyers and costs, not only workflows.</li><li>The warehouse has the deepest research and the most roles.</li></ul>
  <p class="over"><strong>Override if:</strong> readers turn out to work mostly on transport or orders; then Part 2 grows and Part 1 loses a unit.</p>
</section>
<div class="report"><ul>
  <li><strong>What the course is for.</strong> Learning the domain: how warehouses, transport and orders run, who works in them, how the software that runs them is bought, and what it costs. It is the first course of a new public track, Supply Chain. No unit is interview preparation.</li>
  <li><strong>Out of scope.</strong> AI features and any vendor's AI layer. They sit on top of the three systems; the course teaches the systems and the work underneath them.</li>
  <li><strong>No real vendor is assessed.</strong> Worked product examples use fictional vendors. Real vendors appear only as the source of a public statement or as entries in a dated list from an analyst report or a filing, all alike. The reader gets the method and the templates to map and compare real products themselves.</li>
  <li><strong>Where the evidence pushes back.</strong> The operations research on warehouses is solid and old: much of it predates e-commerce at scale. Transport and order management have less of it. Almost everything about the software itself comes from vendors or from analysts whose reports vendors license. Private vendors publish no prices, revenue by product or win rates. Why deals are won or lost has almost no independent evidence. The course grades every claim, so "vendor-reported" and "practice" will appear often, and some sections will say "no independent source found".</li>
</ul></div>"""

LEARN_LEDE = 'Read here. Everything about how the units get written lives in Build.'
LEARN_NOTE = 'Order of writing: the eighteen core units in reading order, SCE1 to SCE18, then DD-SCE1 and DD-SCE2; SCE1, SCE6, SCE8, SCE9, SCE11, SCE12, SCE16, SCE17 and DD-SCE1 with search on.'
LEARNING_NOTE = ''

BUILD_LEDE = 'Method, model rules, and the pages that hold the briefs and the sources. Nothing here is course content.'
BUILD_PICK = """<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>SCE1 first: the execution map, the glossary and the grade key every later unit uses.</strong></p>
  <ul><li>Every later unit grades its claims by SCE1's key.</li><li>Its glossary is extended by every later unit.</li><li>It sets the common claims against their evidence before they recur.</li></ul>
  <p class="over"><strong>Override if:</strong> none; the course is cumulative.</p>
</section>"""
BUILD_BODY = """<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in syllabus order. The chat stages a packet for a fresh writer: the unit's brief from this course's Briefs page, never reworded; the sourcing standard; the fictional case register, <code>generator/data/supply-chain-execution/case-facts.md</code>; the seed bibliography, <code>generator/data/supply-chain-execution/bibliography.md</code>; and every unit of this course already filed. The course has no source units.</li>
    <li>The writer opens every reference before citing it and keeps a source log with the address opened, what was read and the date, grades every claim by SCE1's key, and reports three lists with the unit: facts it invented about the case operations, contradictions with a filed unit or with the brief of an unwritten one, and needs the syllabus does not meet.</li>
    <li>A fresh checker that has not seen the writing runs seven passes: every Sources entry against its publisher's or Crossref's record, every cited claim against its source, the grades, the vendor rules, the case, the scope and tone, and the deliverable and figures against the brief and the text. Its report is filed as <code>audits/supply-chain-execution/fresh-check-&lt;code&gt;.md</code> before any fix; findings are applied as exact replacements.</li>
    <li>Anything found wrong in a filed unit goes into the next unit's prompt and is fixed there first; anything that bears on a unit not yet written is appended to <code>generator/data/supply-chain-execution/syllabus-flags.md</code> and printed in that unit's prompt. A brief is changed only by a syllabus review that the Project's owner confirms. The case register gains the facts a unit invented, with the unit's code.</li>
    <li>The unit is filed at <code>courses/supply-chain-execution/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7; this data file is updated; Academy is rebuilt, verified and published, the artifact and then GitHub Pages.</li>
    <li>After SCE6 the queue stops for a read of the first six units by the Project's owner, so that depth and cost are judged before the other fourteen are written.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Syllabus: Fable 5.2</strong>, as the Project sets for course design.</li>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same context as its unit.</li>
    <li><strong>Fresh check: Opus 5.5</strong>, in a separate context.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or checks.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>Every new unit gets its fresh check before filing: every reference against its record, every cited claim against its source, the deliverable against the brief, every figure against the text. Units written with live search (SCE1, SCE6, SCE8, SCE9, SCE11, SCE12, SCE16, SCE17, DD-SCE1) are re-checked for staleness six months after writing.</p>
</section>"""

ORDER_LEDE = "One row per unit in writing order, which is the reading order. Opus 5.5 writes; a fresh Opus 5.5 context checks each unit before filing. \"Search\" means the unit is written with web search on because its facts are current."
ORDER_NOTES = """<div class="report"><ul>
  <li><strong>Why this order:</strong> SCE1 to SCE18 in reading order, then DD-SCE1, then DD-SCE2. No interleaving: no two units build the same asset. Each of the three systems is taught as an operation before it is taught as a product, then the business part (buyers, the sale, users, implementation, money, the field) ends in the capstone memo. The deep dives come last.</li>
  <li><strong>Gate:</strong> after SCE6 the queue stops for a read of the six units; SCE7 is not written until the read is done.</li>
  <li><strong>Rewrite gate:</strong> no new unit starts while a rewrite verdict is open on an earlier one.</li>
  <li><strong>Carry forward:</strong> an error found in a filed unit goes into the next unit's prompt and is fixed there first; a flag that names a later unit travels to its writer; a flag that would change a brief waits for a syllabus review.</li>
</ul></div>"""
ORDER_FOOT = "The count starts at {start}."

BRIEFS_LEDE = 'One brief per unit, self-contained: the shared preamble (the reader, the scope, the vendor rules, the evidence grades, the case operations, the safety rules, the course goal, the sourcing standard, the tone) is baked into every open brief, followed by the unit\'s Aim, Takes and Gives lines. Written units show their note instead. The course itself is read in <a href="#course-{k}" data-target="course-{k}">Learn · Course {K}</a>.'
BRIEF_LABEL = 'Opus brief'

AUDIT_LOG = []   # the record of audits run; none since the Fable stage closed (S-NOAUDIT, 15 Nov 2026); read by kit/howbuilt.py only

BIB_NOTE = 'Every link cited in the written material, alphabetical by title. New units add to this list; a source that fails a staleness check is marked here.'
TEMPLATE_LEDE = 'What a course needs before the first unit is written: see the new-course skill and design/README.md.'
TEMPLATE_NOTE = ''
TEMPLATE_BLOCKS = []

# newest first
CHANGELOG = [
    ('2026-11-19 20:22', "v1. Course created (new-course skill; row S-SCE0): frame, goal and three outcomes, 20 units with one brief each and their Aim, Takes and Gives lines, the shared preamble with the reader persona, the fictional case register of three operations and three vendors, a seed bibliography of 41 references checked for existence, the syllabus-flags file. No unit written."),
]
