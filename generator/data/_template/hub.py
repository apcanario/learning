"""⟨Course family⟩ hub: the content. kit/mdcourse.py renders it into Academy on design/theme.css.

Copy data/_template/ to data/<slug>/, replace every ⟨…⟩, add the course to kit/courses.py, then: cd kit && python3 build.py && python3 verify.py
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
NEXT_UNIT = 'A1'

HOME_H1 = '⟨Two hubs: one to learn from, one to build with⟩'
HOME_LEDE = '⟨One or two sentences.⟩ <strong>Learn</strong> is where the finished units are read. <strong>Build</strong> is where they get made.'
LEARN_TILE = ('The courses', 'Goals, outcomes, units, and the written material to read.')
BUILD_TILE = ('How the courses get made', 'Procedure, model rules, every brief, bibliography, changelog.')
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
BUILD_LEDE = 'Method, model rules, and the pages that hold the briefs and the sources. Nothing here is course content.'
BUILD_PICK = ''
BUILD_BODY = """<div class="report"><h2>Procedure</h2>
  <p>The Learning Project's <code>method.md</code> is the procedure: one chat per unit, brief from Build · Briefs, unit filed to <code>courses/⟨course-slug⟩/&lt;code&gt;-&lt;slug&gt;.md</code>, fresh-checked before filing, hub rebuilt.</p></div>"""
ORDER_LEDE = 'One row per unit in writing order.'   # the remaining count is derived by kit/mdcourse.py from ORDER and STATUS; do not type it
ORDER_NOTES = '<div class="report"><ul><li><strong>Why this order:</strong> ⟨reason⟩.</li></ul></div>'
ORDER_FOOT = 'The count starts at {start}.'
BRIEFS_LEDE = 'One brief per unit, self-contained: the shared preamble is baked into every open brief. Copy, paste into a new chat in the Learning Project, one unit per chat. The course itself is read in <a href="#course-{k}">Learn · Course {K}</a>.'
BRIEF_LABEL = 'Opus brief'
AUDIT_LOG = []   # the record of audits run; none since the Fable stage closed (S-NOAUDIT, 15 Nov 2026); read by kit/howbuilt.py only

BIB_NOTE = 'Every link cited in the written material, alphabetical by title.'
TEMPLATE_LEDE = 'What a project hub needs before the first unit is written: see the new-course skill and design/README.md.'
TEMPLATE_NOTE = ''
TEMPLATE_BLOCKS = []
CHANGELOG = [('⟨yyyy-mm-dd hh:mm⟩', 'v1. Hub created from the template on design/theme.css.')]
