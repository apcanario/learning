"""Building with AI: the course data (11 Nov 2026).

kit/build.py renders it into Academy through kit/mdcourse.py (one Academy course per entry in COURSES), on design/theme.css.
Everything a reader sees of the course is here or in units_data.py beside this file (the units and their briefs: PRE, BW, AIMS).
Edit content here; edit style only in design/theme.css. Prose blocks are HTML strings and may use only theme classes
(design/README.md lists them). This is a public course: no private term may appear in this folder (kit/private_terms.py).
The decisions behind it are docs/public-courses.md.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# ---- identity --------------------------------------------------------------------------
TITLE = 'Building with AI'
BAR = 'BUILDING WITH AI'
BRAND_HTML = 'BUILDING <span>/</span> WITH AI'
OUT = 'building-with-ai.html'
THEME_KEY = 'building-with-ai-theme'
VERSION = 'v2 · 15 Nov 2026'
LEARN_C, BUILD_C = 'var(--purple)', 'var(--orange)'

# ---- units -----------------------------------------------------------------------------
_ns = {}
exec((HERE / 'units_data.py').read_text(), _ns)
PRE, BW, AIMS = _ns['PRE'], _ns['BW'], _ns['AIMS']   # AIMS: aim, takes, gives per unit

GOAL_BW = ('by the end of the course you can say what the model saw when an output fails; brief a task so that the first output is usable and keep a project structure that does not rot; verify AI-written work by sample before you trust it; and decide what to hand to an agent, with one real project of your own specified and running.')
NAME_BW = 'Building with AI'

COURSES = [
    dict(key='BW', name=NAME_BW, color='var(--purple)', units=BW, goal=GOAL_BW, slug='bw',
         tile='A working method for people who already think well and want to build a real project with AI: brief, structure, specify, verify, automate. Every claim sourced.',
         intro='For an experienced professional who reasons and writes well and uses a chat assistant with no method: how the tool works, which model for which task, how to brief, how to structure and specify a project, how to verify what the machine wrote, how to chain, automate and delegate the work, and what it costs. Principles stated for any assistant, worked on Claude with every product fact dated, and on one real project, Academy, with its own error counts. Ten core units in three parts and three deep dives.',
         outcomes='<li><strong>Outcome 1</strong> — a working model of the tool and a routing table with cost (BW1, BW2, BW10).</li><li><strong>Outcome 2</strong> — a specified project that produces usable first outputs (BW3, BW4, BW5, BW8; DD-BW1 sets it beside the documented methods).</li><li><strong>Outcome 3</strong> — a verification protocol, a pipeline and an agent rule, run on your own project (BW6, BW7, BW9; DD-BW2 and DD-BW3).</li>'),
]
COURSE_NOTE = "Every unit is sourced to peer-reviewed work, vendor documentation or a practitioner's own words, grades each method by its evidence, dates every product fact, says what holds only for one tool, and ends with a deliverable built in full on a real project and then as a template."

# ---- written material (reading pages) ---------------------------------------------------
# A unit is written when its file is in the vault, courses/building-with-ai/ (A5); kit/build.py derives WRITTEN from it.
READINGS = [
    dict(id='read-bw1', course='BW', title='Mental model', covers=['BW1'], name='BW1 · Mental model', intro='The first unit of Building with AI: a working model of what an AI assistant sees and why its outputs fail, built around the context window: what reaches it, tokens as cost and as attention, what persists inside a chat, across chats and with memory, trained, retrieved and in-conversation knowledge and the training cutoff, why the same prompt gives different answers, system prompt, project instruction and user message, and fabrication, with a map of the layers, a section on other tools, and a deliverable in two parts, a five-minute model and a diagnosis table, each built on the Academy case and then as a template. It was written by an AI model (Opus 5.5) from its brief, with live search on 15 Nov 2026; every product fact was read on the vendor\'s page that day and is dated where it appears. A separate model, in a context that had not seen the writing, checked every cited claim, the deliverable against the brief and every figure against the text; it found 1 error, 7 should-fix and 7 minor points, and every finding was applied before filing. Known gaps: the "Treated in" column of the diagnosis table assigns rows to BW3, BW4 and BW6 partly by inference, as the other units\' briefs were not checked against it; Anthropic\'s help-centre pages carry no exact date, so window sizes, memory behaviour and plan lists are dated by the day they were read and may change within days; the help-centre memory article refused the fetch, so its plan list was not checked; OpenAI\'s help-centre pages could not be fetched, so the ChatGPT rows rest on openai.com pages and the API docs; the Gemini skills and Gems dates rest on one undated help page; Holtzman et al. is cited as the arXiv version, its conference venue not confirmed; carrying Anthropic\'s interpretability findings to the model they name is inference; how billing treats the history the API keeps in its beta message threads was not read; and the affiliation of the authors of "Why Language Models Hallucinate" could not be checked, so it is not stated.'),
]

# ---- build order -----------------------------------------------------------------------
DONE_ROWS = []
ORDER = [("BW1", "Opus 5.5", "on"), ("BW2", "Opus 5.5", "on"), ("BW3", "Opus 5.5", "off"), ("BW4", "Opus 5.5", "off"),
         ("BW5", "Opus 5.5", "on"), ("BW6", "Opus 5.5", "off"), ("BW7", "Opus 5.5", "off"), ("BW8", "Opus 5.5", "off"),
         ("BW9", "Opus 5.5", "on"), ("BW10", "Opus 5.5", "on"), ("DD-BW1", "Opus 5.5", "on"), ("DD-BW2", "Opus 5.5", "off"),
         ("DD-BW3", "Opus 5.5", "off")]
STATUS = {'BW1': 'written 15 Nov'}          # unit code -> status text in the build-order table once filed
NEXT_UNIT = 'BW2'

# ---- prose blocks (theme classes only) ---------------------------------------------------
HOME_H1 = 'Building with AI'
HOME_LEDE = 'A working method for people who already think well and want to build a real project with AI: brief, structure, specify, verify, automate. Every claim sourced.'
LEARN_TILE = ('The course', 'Goal, outcomes, units, and the written material to read.')
BUILD_TILE = ('How the course gets made', 'Procedure, model rules, every brief, bibliography, changelog.')

FRAME = """<h2 class="hsec">Frame</h2>
<div class="report">
  <h2>A method, for people who do not need to be taught how to think</h2>
  <p>Courses on AI tools mostly teach prompts or teach code. The reader this course is for needs neither first: they reason and write well already, and what they lack is a method for a whole project: what the model can see, how to brief it, where a project's knowledge should live, how to specify the work so one context can finish a piece of it, and how to check the result without reading every line. The course teaches that method on the reader's own project, states each principle so that it holds for any current assistant, and works the detail on Claude, where the evidence was verified, with every product fact dated.</p>
</div>
<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>Method before tools; one real project as the case, with its error counts.</strong></p>
  <ul><li>Principles outlive a model lineup; dated appendices carry the rest.</li><li>A real record of errors teaches verification better than advice.</li><li>The reader builds their own project unit by unit.</li></ul>
  <p class="over"><strong>Override if:</strong> most early readers turn out to use another assistant; then each unit's section on other tools is widened into a parallel worked example.</p>
</section>
<div class="report"><ul>
  <li><strong>Reader:</strong> an experienced professional who reasons and writes well, uses a chat assistant with no method, may not write code, and brings one real project. Every brief says so.</li>
  <li><strong>Case:</strong> Academy, a real library of courses built by one person with Claude. Its facts come only from the case file, <code>generator/data/building-with-ai/case-academy.md</code>, with private details removed, and it is always labelled as one anecdote.</li>
  <li><strong>Tool stance:</strong> each unit ends its body with a section on other tools, saying what is specific to Claude and where the equivalent is documented.</li>
  <li><strong>Where the evidence pushes back:</strong> most guidance in this field is practice or opinion, studies test models that are already superseded, and a vendor's documentation is a vendor's. The course grades every method and dates every product fact.</li>
</ul></div>"""

LEARN_LEDE = 'Read here. Everything about how the units get written lives in Build.'
LEARN_NOTE = 'Order of writing: the ten core units in reading order, BW1 to BW10, then the three deep dives, DD-BW3 last; BW1, BW2, BW5, BW9, BW10 and DD-BW1 with search on.'
LEARNING_NOTE = ''

BUILD_LEDE = 'Method, model rules, and the pages that hold the briefs and the sources. Nothing here is course content.'
BUILD_PICK = """<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>BW1 first: the mental model every later unit speaks in.</strong></p>
  <ul><li>It is the cheapest unit and makes each later brief shorter.</li><li>Its source unit is already nearly generic.</li><li>BW5, the one unit with no source, comes after four that have one.</li></ul>
  <p class="over"><strong>Override if:</strong> the personal-brand course should finish first; the two courses share no unit, so either order works.</p>
</section>"""
BUILD_BODY = """<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in syllabus order. The chat stages a packet for a fresh writer: the unit's brief from this course's Briefs page, never reworded; the source units its Takes line names; every unit of this course already filed; and the Academy case file.</li>
    <li>The writer re-verifies every claim it carries over from a source unit and reports three lists with the unit: mistakes found in the source units, contradictions with a filed unit or with the brief of an unwritten one, and needs the syllabus does not meet.</li>
    <li>A fresh checker that has not seen the writing checks every cited claim against its source, the deliverable against the brief, every figure against the text, and the unit against the list of private terms. Its report is filed as <code>audits/building-with-ai/fresh-check-&lt;code&gt;.md</code> before any fix; findings are applied as exact replacements.</li>
    <li>Verified mistakes are corrected where they sit, each with a dated note. Contradictions and needs are appended to <code>generator/data/building-with-ai/syllabus-flags.md</code>; a brief is changed only by a syllabus review that the Project's owner confirms. The case file gains a fact only from the Project's own records, never from a unit.</li>
    <li>The unit is filed at <code>courses/building-with-ai/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7; this data file is updated; Academy is rebuilt, verified and published, the artifact and then GitHub Pages.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same context as its unit.</li>
    <li><strong>Fresh check: Opus 5.5</strong> in a separate context.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or checks.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>Every new unit gets its fresh check before filing: every cited claim against its source, the deliverable against the brief, every figure against the text. Units written with live search (BW1, BW2, BW5, BW9, BW10, DD-BW1) are re-checked for staleness six months after writing.</p>
</section>"""

ORDER_LEDE = "One row per unit in writing order, which is the reading order. Opus 5.5 writes; a fresh Opus 5.5 context checks each unit before filing. \"Search\" means the unit is written with web search on because its facts are current."
ORDER_NOTES = """<div class="report"><ul>
  <li><strong>Why this order:</strong> the course is a method, so the writing order is the reading order: Part 1 gives the model of the tool and the choice of model; Part 2 directs it (the brief, the context, the spec); Part 3 builds and trusts (verification before the pipeline, the skill and the agent, since what can be verified decides what is delegated), then cost; the deep dives last, the review of one's own usage last of all.</li>
  <li><strong>Rewrite gate:</strong> no new unit starts while a rewrite verdict is open on an earlier one.</li>
  <li><strong>Syllabus flags:</strong> a unit that finds a contradiction or a need raises a flag; a flag that names the next unit travels to its writer; a flag that would change a brief waits for a syllabus review.</li>
</ul></div>"""
ORDER_FOOT = "The count starts at {start}."

BRIEFS_LEDE = 'One brief per unit, self-contained: the shared preamble (the reader, the source-material rule, the tool stance, the Academy case, the course goal, the sourcing standard, the tone) is baked into every open brief, followed by the unit\'s Aim, Takes and Gives lines. Written units show their note instead. The course itself is read in <a href="#course-{k}" data-target="course-{k}">Learn · Course {K}</a>.'
BRIEF_LABEL = 'Opus brief'

# the record of the audits run before the Fable stage closed (S-NOAUDIT, 15 Nov 2026); read by kit/howbuilt.py only, nothing is added
AUDIT_LOG = []


BIB_NOTE = 'Every link cited in the written material, alphabetical by title. New units add to this list; a source that fails a staleness check is marked here.'
TEMPLATE_LEDE = 'What a course needs before the first unit is written: see the new-course skill and design/README.md.'
TEMPLATE_NOTE = ''
TEMPLATE_BLOCKS = []

# newest first
CHANGELOG = [
    ('2026-11-15 15:00', 'v2. BW1 Mental model filed (row W-BW1): 6,431 words of body and 2,951 of deliverable, 3 figures, written by Opus 5.5 from its brief with search on. Fresh check (Opus 5.5, separate context): fix, 1 error, 7 should-fix, 7 minor, all applied before filing. Corrected elsewhere: a private unit (18 replacements and a note); PB8 and a private legal unit, their citation of Decreto-Lei 57/2008. Object: the context window (§1 and §2)'),
    ('2026-11-11 23:59', "v1. Course created (new-course skill; backlog row G-0): frame, goal and three outcomes, 13 units with one brief each and their Aim, Takes and Gives lines, the shared preamble with the reader persona, the build order in syllabus order, the syllabus-flags file. Adapted from a private course of the Learning Project; no unit written."),
]
