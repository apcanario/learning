"""Sport Psychology for Coaches: the course data (16 Nov 2026, row S-SP0).

kit/build.py renders it into Academy through kit/mdcourse.py (one Academy course per entry in COURSES), on design/theme.css.
Everything a reader sees of the course is here or in units_data.py beside this file (the units and their briefs: PRE, SP, AIMS).
Edit content here; edit style only in design/theme.css. Prose blocks are HTML strings and may use only theme classes
(design/README.md lists them). This is a public course: no private term may appear in this folder (kit/private_terms.py).
The syllabus is docs/sport-psychology-syllabus.md (its section 11 gives the fields below); the decisions are docs/public-courses.md.
The course has no source units: nothing is adapted from another course of the Learning Project.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# ---- identity --------------------------------------------------------------------------
TITLE = 'Sport Psychology for Coaches'
BAR = 'SPORT PSYCHOLOGY'
BRAND_HTML = 'SPORT PSYCHOLOGY <span>/</span> FOR COACHES'
OUT = 'sport-psychology.html'
THEME_KEY = 'sport-psychology-theme'
VERSION = 'v2 · 17 Nov 2026'
LEARN_C, BUILD_C = 'var(--orange)', 'var(--gold)'

# ---- units -----------------------------------------------------------------------------
_ns = {}
exec((HERE / 'units_data.py').read_text(), _ns)
PRE, SP, AIMS = _ns['PRE'], _ns['SP'], _ns['AIMS']   # AIMS: aim, takes, gives per unit

GOAL_SP = ('by the end of the course you can adjust what you ask of an athlete to their age and stage; teach a small set of evidence-graded psychological skills in practice and use them on competition day; respond to an athlete\'s state from their baseline and their own words; keep your language, your handling of weight and your authority on the right side of a line you can state; and recognise the signs that mean referral, with a season plan written for your own squad.')
NAME_SP = 'Sport Psychology for Coaches'

COURSES = [
    dict(key='SP', name=NAME_SP, color='var(--orange)', units=SP, goal=GOAL_SP, slug='sp',
         tile='For coaches of athletes aged 10 to 25: how young athletes develop, how to teach mental skills that hold under pressure, how to respond on the day, and where a coach\'s part ends. Every claim sourced and graded.',
         intro='For a coach in any sport with no training in psychology: what changes in an athlete between 10 and 25, the climate your own behaviour creates, what anxiety is and how it is kept going, the skills a coach may teach and how strong the evidence is for each, training under pressure, reading and responding to an athlete, competition day, the signs that mean referral, and a season plan. Three deep dives: the coach\'s line with minors, weight and who decides, and the techniques an athlete carries into competition. Worked on three fictional athletes in three sports. Ten core units in four parts and three deep dives.',
         outcomes='<li><strong>Outcome 1 · Know the athlete and the evidence.</strong> An age-and-stage table, a climate audit of your own coaching, and a claim-check you can run on anything you are told (SP1, SP2, SP3).</li><li><strong>Outcome 2 · Skills in practice and on the day.</strong> An anxiety profile, a skills block, a pressure-training block, a response table, a competition-day protocol, a pocket toolkit and a season plan (SP4 to SP8, SP10, DD-SP3).</li><li><strong>Outcome 3 · Wellbeing and the coach\'s line.</strong> A red-flag table and referral plan, a conduct code and comment test, and a protocol for who decides a weight class (SP9, DD-SP1, DD-SP2).</li>'),
]
COURSE_NOTE = 'Every unit is sourced to consensus statements, meta-analyses and peer-reviewed studies, grades each recommendation by its evidence, names the sample behind each finding, says where a coach\'s part ends, and ends with a deliverable built in full on three fictional athletes and then as a template.'

# ---- written material (reading pages) ---------------------------------------------------
# A unit is written when its file is in the vault, courses/sport-psychology/ (A5); kit/build.py derives WRITTEN from it.
READINGS = [
    dict(id='read-sp1', course='SP', title='What a coach can do, and how to tell evidence from noise', covers=['SP1'], name='SP1 · What a coach can do, and how to tell evidence from noise', intro="The course's first unit. It sets out what sport psychology is and who may practise it, the coach's part and where it ends, the kinds of evidence and how to read a study in plain words, what the reviews say about psychology and performance, four cautionary cases from the replication record, the popular claims coaches hear set against their evidence, the five evidence grades that every later unit uses, and five questions to ask of any claim. Its deliverable is a scope-of-practice card, a claim-check sheet and the grade key, each worked on the three fictional athletes and then given as a template. How it was made: written on 17 Nov 2026 by Opus 5.5 with web search off, citing only sources opened in the writing session, then checked by a separate Opus 5.5 context that had not seen the writing (verdict: fix; 48 findings: 2 errors, 30 should-fix, 16 minor). 33 findings were applied and 15 held; in place of the held ego-depletion error, a set of fallback fixes removed the opinion article the case had rested on. Known gaps. (1) References named in the unit or in the writer's notes that the writer did not open, and on which no claim rests: the Delphi study on the coach's role in athlete mental health (Bissett et al., 2020); the 2022 review of sport psychology meta-analyses (Lochbaum et al., 2022), so the unit says nothing on how far psychological variables relate to performance; the original power-posing study and its replication (Ranehill et al., 2015); the two ego-depletion replications (Hagger et al., 2016; Vohs et al., 2021); the grit meta-analysis (Credé et al., 2017); the growth-mindset meta-analyses (Sisk et al., 2018); the reviews on controlling coaching (Bartholomew et al., 2009 and 2011; Fletcher and Sarkar, 2016); Wegner's papers on ironic effects (1994, 1998) and Woodman et al. (2015); Somerville (2016) and Güllich et al. (2022). (2) Claims read from an abstract or summary only: the IOC mental health tools (Gouttebarge et al., 2021), the intervention meta-analysis of Brown and Fletcher (2017), the deliberate-practice meta-analysis (Macnamara et al., 2016), the mental toughness review (Lin et al., 2017), the triune-brain review (Steffen et al., 2022) and the neuro-linguistic programming review (Sturt et al., 2012); the facial-expression review (Barrett et al., 2019) from the publisher's summary page only; the early-specialisation meta-analysis (Güllich and Barth, 2024) from its abstract and parts of the full text; the imagery EEG study (Mustile et al., 2024) from its abstract and methods. (3) 15 fixes from the check are held, because each needed a reference that could not be opened at its publisher's page, an index or a DOI address in the fixing session (search returned only repository copies or press releases, a redirect that may not be followed, or a blocked page), and no fix may rest on a source that was not opened: six on ego depletion (Hagger et al., 2016; Vohs et al., 2021), six on the power-posing replication (Ranehill et al., 2015), two on the size of growth-mindset effects (Sisk et al., 2018) and one on psychological variables and performance (Lochbaum et al., 2022). They will be applied when those references are opened at their publishers' pages. (4) Ego depletion carries no grade: no source of an accepted type on the replications was opened, so the grade key's contested row has no worked example. (5) The unit runs to about 7,000 words before its Sources, over the brief's length guide; it is kept at that length because the topic needs it: the scope line, the grades and the claim checks are what every later unit builds on."),
]

# ---- build order -----------------------------------------------------------------------
DONE_ROWS = []
ORDER = [("SP1", "Opus 5.5", "off"), ("SP2", "Opus 5.5", "off"), ("SP3", "Opus 5.5", "off"), ("SP4", "Opus 5.5", "off"),
         ("SP5", "Opus 5.5", "off"), ("SP6", "Opus 5.5", "off"), ("SP7", "Opus 5.5", "off"), ("SP8", "Opus 5.5", "off"),
         ("SP9", "Opus 5.5", "on"), ("SP10", "Opus 5.5", "off"), ("DD-SP1", "Opus 5.5", "on"), ("DD-SP2", "Opus 5.5", "on"),
         ("DD-SP3", "Opus 5.5", "off")]
STATUS = {'SP1': 'written 17 Nov'}          # unit code -> status text in the build-order table once filed
NEXT_UNIT = 'SP2'

# ---- prose blocks (theme classes only) ---------------------------------------------------
HOME_H1 = 'Sport Psychology for Coaches'
HOME_LEDE = 'For coaches of athletes aged 10 to 25: how young athletes develop, how to teach mental skills that hold under pressure, how to respond on the day, and where a coach\'s part ends. Every claim sourced and graded.'
LEARN_TILE = ('The course', 'Goal, outcomes, units, and the written material to read.')
BUILD_TILE = ('How the course gets made', 'Procedure, model rules, every brief, bibliography, changelog.')

FRAME = """<h2 class="hsec">Frame</h2>
<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>A coach's course, not a psychologist's. Climate, skills, noticing, referring.</strong></p>
  <ul><li>Coaches are with athletes daily; clinicians rarely are.</li><li>A stated scope keeps a public course safe to follow.</li><li>Graded evidence is what separates it from online advice.</li></ul>
  <p class="over"><strong>Override if:</strong> the readers turn out to be mostly sport psychology students; then the course adds theory and assessment and drops the scope limits.</p>
</section>
<div class="report"><ul>
  <li><strong>Where the evidence pushes back.</strong> Most studies are small. Most samples are university students or adult athletes, not 13-year-olds who win national titles. Several of the techniques coaches most want (talking to yourself by name, reading nerves as readiness, if-then plans) were tested outside sport. Prevalence figures for abuse come from adults remembering their childhood. The course grades every recommendation and names the sample behind it, so a reader sees "moderate" and "weak" often.</li>
</ul></div>"""

LEARN_LEDE = 'Read here. Everything about how the units get written lives in Build.'
LEARN_NOTE = 'Order of writing: the ten core units in reading order, SP1 to SP10, then the three deep dives; SP9, DD-SP1 and DD-SP2 with search on.'
LEARNING_NOTE = ''

BUILD_LEDE = 'Method, model rules, and the pages that hold the briefs and the sources. Nothing here is course content.'
BUILD_PICK = """<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>SP1 first: the scope line and the grade key every later unit uses.</strong></p>
  <ul><li>Every later unit grades its claims by SP1's key.</li><li>It settles what a coach may and may not do.</li><li>It clears the popular claims before they recur.</li></ul>
  <p class="over"><strong>Override if:</strong> none; the course is cumulative.</p>
</section>"""
BUILD_BODY = """<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in syllabus order. The chat stages a packet for a fresh writer: the unit's brief from this course's Briefs page, never reworded; the sourcing standard; the fictional case register, <code>generator/data/sport-psychology/case-facts.md</code>; the seed bibliography, <code>generator/data/sport-psychology/bibliography.md</code>; and every unit of this course already filed. The course has no source units.</li>
    <li>The writer opens every reference before citing it and keeps a source log, and reports three lists with the unit: facts it invented about the case athletes, contradictions with a filed unit or with the brief of an unwritten one, and needs the syllabus does not meet.</li>
    <li>A fresh checker that has not seen the writing checks every cited claim against its source, every Sources entry against its publisher's record, the grades, the samples, the scope and safety rules and the spread of sports, the deliverable against the brief and every figure against the text. Its report is filed as <code>audits/sport-psychology/fresh-check-&lt;code&gt;.md</code> before any fix; findings are applied as exact replacements. SP9, DD-SP1 and DD-SP2 also get a safety reader, a third context that reads only for scope and safety.</li>
    <li>Contradictions and needs are appended to <code>generator/data/sport-psychology/syllabus-flags.md</code>; a brief is changed only by a syllabus review that the Project's owner confirms. The case register gains the facts a unit invented, with the unit's code.</li>
    <li>The unit is filed at <code>courses/sport-psychology/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7; this data file is updated; Academy is rebuilt, verified and published, the artifact and then GitHub Pages.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Syllabus: Fable 5.2</strong>, as the Project sets for course design.</li>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same context as its unit.</li>
    <li><strong>Fresh check and safety reader: Opus 5.5</strong>, each in a separate context.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or checks.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>Every new unit gets its fresh check before filing: every cited claim against its source, the deliverable against the brief, every figure against the text. Units written with live search (SP9, DD-SP1, DD-SP2) are re-checked for staleness six months after writing.</p>
</section>"""

ORDER_LEDE = "One row per unit in writing order, which is the reading order. Opus 5.5 writes; a fresh Opus 5.5 context checks each unit before filing. \"Search\" means the unit is written with web search on because its facts are current."
ORDER_NOTES = """<div class="report"><ul>
  <li><strong>Why this order:</strong> SP1 to SP10 in reading order, then DD-SP1, DD-SP2, DD-SP3. The course is cumulative: SP1 sets the grades and the scope every later unit uses, and SP10 assembles the sheets of SP2 to SP9. No core unit points forward to a deep dive. DD-SP2 comes after DD-SP1 because it maps weight pressure onto DD-SP1's definitions. DD-SP3 is last: it trains its techniques on SP6's pressure ladder and points back to SP8.</li>
  <li><strong>Rewrite gate:</strong> no new unit starts while a rewrite verdict is open on an earlier one.</li>
  <li><strong>Syllabus flags:</strong> a unit that finds a contradiction or a need raises a flag; a flag that names the next unit travels to its writer; a flag that would change a brief waits for a syllabus review.</li>
</ul></div>"""
ORDER_FOOT = "The count starts at {start}."

BRIEFS_LEDE = 'One brief per unit, self-contained: the shared preamble (the reader, the scope, the evidence grades, the case athletes, the safety rules, the course goal, the sourcing standard, the tone) is baked into every open brief, followed by the unit\'s Aim, Takes and Gives lines. Written units show their note instead. The course itself is read in <a href="#course-{k}" data-target="course-{k}">Learn · Course {K}</a>.'
BRIEF_LABEL = 'Opus brief'

AUDIT_LOG = []   # the record of audits run; none since the Fable stage closed (S-NOAUDIT, 15 Nov 2026); read by kit/howbuilt.py only

BIB_NOTE = 'Every link cited in the written material, alphabetical by title. New units add to this list; a source that fails a staleness check is marked here.'
TEMPLATE_LEDE = 'What a course needs before the first unit is written: see the new-course skill and design/README.md.'
TEMPLATE_NOTE = ''
TEMPLATE_BLOCKS = []

# newest first
CHANGELOG = [
    ('2026-11-17 13:57', 'v2. SP1 filed (row W-SP1): What a coach can do, and how to tell evidence from noise, written by Opus 5.5 with search off. Fresh check by a separate Opus 5.5 context: fix, 48 findings (2 errors, 30 should-fix, 16 minor); 33 applied and 15 held for want of an opened source, with fallback fixes in place of the held ego-depletion error; ego depletion carries no grade. Six case facts added to the register; 11 syllabus flags raised, none blocking SP2. 1 of 13 written. Next: SP2.'),
    ('2026-11-16 19:30', "v1. Course created (new-course skill; row S-SP0): frame, goal and three outcomes, 13 units with one brief each and their Aim, Takes and Gives lines, the shared preamble with the reader persona, the fictional case register, a seed bibliography of 97 references checked for existence, the syllabus-flags file. No unit written."),
]
