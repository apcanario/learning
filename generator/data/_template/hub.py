"""⟨Course family⟩ hub: the content. build_hub.py renders it on design/theme.css.

Copy data/_template/ to data/<slug>/, replace every ⟨…⟩, then: python3 build_hub.py data/<slug>
Prose blocks are HTML strings and may use only theme classes (design/README.md lists them).
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

TITLE = '⟨Hub title⟩'
BAR = '⟨SHORT NAME⟩'
BRAND_HTML = '⟨SHORT⟩ <span>/</span> ⟨NAME⟩'
OUT = '⟨slug⟩.html'
THEME_KEY = '⟨slug⟩-theme'
VERSION = 'v1 · ⟨d Mon yyyy⟩'
LEARN_C, BUILD_C = 'var(--red)', 'var(--orange)'

_ns = {}
exec((HERE / 'units_data.py').read_text(), _ns)
PRE, A = _ns['PRE'], _ns['A']

COURSES = [
    dict(key='A', name='⟨Course A name⟩', color='var(--teal)', units=A, slug='⟨course-slug⟩',
         goal='by the end of the course the reader can ⟨one sentence⟩.',
         tile='⟨One line for the Learn tile.⟩',
         intro='⟨Two sentences: what the course is and is not; how many core units and deep dives (8–10 core, 2 or 3 deep dives).⟩',
         outcomes='<li><strong>Outcome 1</strong> — ⟨measurable⟩ (A1).</li><li><strong>Outcome 2</strong> — ⟨measurable⟩ (A2).</li><li><strong>Outcome 3</strong> — ⟨measurable⟩ (DD-A1).</li>'),
]
COURSE_NOTE = '⟨One line: the sourcing standard and the deliverable rule, as the reader should see them.⟩'

READINGS = []        # per unit filed in courses/<slug>/: dict(id='read-<code lower>', course, title, covers=[code], name, intro);
                     # other written material kept in this folder adds md='<file>'. WRITTEN is derived by kit/build.py from the vault.

DONE_ROWS = []
ORDER = [("A1", "Opus 5.5", "off"), ("A2", "Opus 5.5", "on"), ("DD-A1", "Opus 5.5", "off")]
STATUS = {}          # unit code -> status text in the build-order table once filed
AUDIT_EVERY = 4
AUDIT_ROW = ('Stratified-sample audit of the last four units', 'Fable 5.1', 'on', 'prompt on Audits page')
FINAL_AUDIT = ('Final audit', 'Final audit of the last units plus a full read of the course against its goal', 'Fable 5.1', 'on', '')
NEXT_UNIT, AUDITS_RUN, NEXT_AUDIT = 'A1', 0, 'after four units'

HOME_H1 = '⟨Two hubs: one to learn from, one to build with⟩'
HOME_LEDE = '⟨One or two sentences.⟩ <strong>Learn</strong> is where the finished units are read. <strong>Build</strong> is where they get made.'
LEARN_TILE = ('The courses', 'Goals, outcomes, units, and the written material to read.')
BUILD_TILE = ('How the courses get made', 'Procedure, model rules, every brief, audit prompts, bibliography, changelog.')
FRAME = """<h2 class="hsec">Frame</h2>
<div class="report"><h2>⟨The frame in one line⟩</h2><p>⟨Why this course, for this reader, now.⟩</p></div>
<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>⟨The pick.⟩</strong></p>
  <ul><li>⟨Reason ≤12 words⟩</li><li>⟨Reason⟩</li><li>⟨Reason⟩</li></ul>
  <p class="over"><strong>Override if:</strong> ⟨condition⟩.</p>
</section>"""
LEARN_LEDE = 'Read here. Everything about how the units get written lives in Build.'
LEARN_NOTE = '⟨Order of writing, one sentence.⟩'
LEARNING_NOTE = ''
BUILD_LEDE = 'Method, model rules, and the pages that hold the briefs, the audits and the sources. Nothing here is course content.'
BUILD_PICK = ''
BUILD_BODY = """<div class="report"><h2>Procedure</h2>
  <p>The Learning Project's <code>method.md</code> is the procedure: one chat per unit, brief from Build · Briefs, unit filed to <code>courses/⟨course-slug⟩/&lt;code&gt;-&lt;slug&gt;.md</code>, hub rebuilt, audit every four units.</p></div>"""
ORDER_LEDE = 'One row per unit in writing order; an audit row every fourth written unit.'   # the remaining count is derived by kit/mdcourse.py from ORDER and STATUS; do not type it
ORDER_NOTES = '<div class="report"><ul><li><strong>Why this order:</strong> ⟨reason⟩.</li></ul></div>'
ORDER_FOOT = 'The count starts at {start}.'
BRIEFS_LEDE = 'One brief per unit, self-contained: the shared preamble is baked into every open brief. Copy, paste into a new chat in the Learning Project, one unit per chat. The course itself is read in <a href="#course-{k}">Learn · Course {K}</a>.'
BRIEF_LABEL = 'Opus brief'
AUDITS_LEDE = 'No audit yet. Each audit records: units sampled, claims checked, failures, verdict, and what changed.'
AUDIT_LOG = [('—', 'Nothing audited yet.')]
AUDIT_PROMPTS_NOTE = 'Run in the Learning Project with Fable 5.1 after every fourth written unit. The prompts are method.md §6, verbatim.'
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

BIB_NOTE = 'Every link cited in the written material, alphabetical by title.'
TEMPLATE_LEDE = 'What a project hub needs before the first unit is written: see the new-course skill and design/README.md.'
TEMPLATE_NOTE = ''
TEMPLATE_BLOCKS = []
CHANGELOG = [('⟨yyyy-mm-dd hh:mm⟩', 'v1. Hub created from the template on design/theme.css.')]
