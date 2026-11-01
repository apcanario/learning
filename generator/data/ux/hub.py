"""User Experience: the course data for the family's courses (29 Oct 2026). kit/build.py renders it into Academy through
kit/mdcourse.py (one Academy course per entry in COURSES), on design/theme.css.

The first course is IA · Information Architecture. Everything a reader sees of it is here or in units_data.py beside this
file (the units and their briefs: PRE, IA). Edit content here; edit style only in design/theme.css. Prose blocks are HTML
strings and may use only theme classes (design/README.md lists them).

This family is the Learning Project's one exception to its single-reader rule: the course is written to be handed to other
designers, and its reader is the persona in PRE (Pedro's decision, 29 Oct 2026). The running example, Perqo, is fictional.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# ---- identity --------------------------------------------------------------------------
TITLE = 'User Experience Courses'
BAR = 'USER EXPERIENCE'
BRAND_HTML = 'USER <span>/</span> EXPERIENCE'
OUT = 'user-experience-courses.html'
THEME_KEY = 'ux-theme'
VERSION = 'v4 · 1 Nov 2026'
LEARN_C, BUILD_C = 'var(--blue)', 'var(--orange)'

# ---- units -----------------------------------------------------------------------------
_ns = {}
exec((HERE / 'units_data.py').read_text(), _ns)
PRE, IA = _ns['PRE'], _ns['IA']

GOAL_IA = ("by the end of the course the reader can read any information-architecture artefact a team hands them and say what it claims and what it leaves out; "
           "choose and build the right artefact for a system of a given complexity, from a website's sitemap to a cross-surface interaction map that joins the product map to its decision trees and lifecycles; "
           "place that work inside a product development cycle with a named touchpoint for product management, engineering, content, sales, support and clients; "
           "and deliver a defensible IA when the research, the content or the stakeholders are missing, with every assumption labelled and a test named for each.")
NAME_IA = 'Information Architecture'

COURSES = [
    dict(key='IA', name=NAME_IA, color='var(--blue)', units=IA, goal=GOAL_IA, slug='ia',
         tile="How to read, build and edit the structure behind a product, from a sitemap to a system map, and how to deliver it when the inputs are missing.",
         intro="For a mid-level UX designer, written to be handed on: what information architecture is, the shapes it takes, how to build it at four levels of complexity on one fictional product (Perqo: a website, an employee app, a backoffice), where it sits in the product cycle and in the business, how to validate it, and how to deliver it anyway when the research, the content or the stakeholders are missing. Twelve core units in four parts and three deep dives.",
         outcomes="<li><strong>Outcome 1</strong> — reads and draws every artefact in the catalogue in one notation, chosen by the question it answers (IA1, IA2, IA3, IA4).</li><li><strong>Outcome 2</strong> — delivers the four Perqo IAs at rising complexity, ending in the interaction map that joins product map, decision trees and lifecycles (IA5, IA6, IA7, IA8).</li><li><strong>Outcome 3</strong> — runs IA inside a product cycle: a touchpoint matrix, a validation plan with evidence, and an incomplete-inputs playbook with an assumption register (IA9, IA10, IA11, IA12, DD-IA3).</li>"),
]
COURSE_NOTE = "Every unit is sourced to the field's standard works, Nielsen Norman Group research or peer-reviewed studies, labels vendor guidance and practice as such, carries its figures as drawings built from the unit's own content, and ends with a shipped deliverable built on the fictional Perqo."

# ---- written material (reading pages) ---------------------------------------------------
# A unit is written when its file is in the vault, courses/ux/ (A5); kit/build.py derives WRITTEN from it.
READINGS = [
    dict(id='read-ia1', course='IA',
         title='What information architecture is, and where it sits', covers=['IA1'], name='IA1 · What IA is',
         intro="Unit IA1, written 30 Oct 2026 by Opus 5.5 in an isolated agent context that saw only its brief (P31), search off (used only to verify editions, chapters, dates and URLs); fresh check the same day by a separate Opus 5.5 agent that had not seen the writing: keep, 0 errors, 4 should-fix, 7 minor, all applied (a Fable 5.1 fresh check is owed, row P49). Four definitions (Rosenfeld, Morville and Arango; Covert; Arango; Garrett), the four lines between IA and navigation, the interface, content strategy and the data model, the discipline's history, what an IA deliverable is for, and a first look at Perqo's three surfaces; six figures. Deliverables: a one-page definition sheet for a product team and the Perqo surfaces map later units build on. Known gaps: About Face's argument is from knowledge of the section, not a re-read; Wurman's 1975 coinage is reported secondhand (Resmini and Rosati, from Morville)."),
    dict(id='read-ia2', course='IA',
         title='The shapes IA takes: the artefact catalogue and the course notation', covers=['IA2'], name='IA2 · The shapes IA takes',
         intro="Unit IA2, written 30 Oct 2026 by Opus 5.5 in an isolated agent context that saw only its brief, the writing skill, sourcing Parts 1 and 4, the figure kinds and IA1 (P31), search off (used only to verify editions, chapters, dates and URLs); fresh check the same day by a separate Opus 5.5 agent that had not seen the writing: fix, 3 errors (three figures that read backwards or added labels the text lacked), 10 should-fix, 17 minor, all applied (a Fable 5.1 fresh check is owed, row P49). The catalogue of ten IA artefacts, each with the question it answers, its readers, its fidelity by stage and what it must not be mistaken for; Garrett's visual vocabulary and Brown's site maps and flowcharts, and what each standardises; the five faults to look for first in someone else's artefact; editing without breaking what others rely on; and the course notation every later figure uses; eight figures, one per artefact family plus the legend. Deliverables: the course notation sheet and the artefact decision table. Known gaps: Brown's chapters and the Polar Bear book's navigation and vocabulary chapters were read only at their openings and headings; Garrett's Quick Reference is undated; Shostack 1984 and Harel 1987 from their abstracts and summaries; UML multiplicity from knowledge."),
]

# ---- build order -----------------------------------------------------------------------
DONE_ROWS = []
ORDER = [("IA1", "Opus 5.5", "off"), ("IA2", "Opus 5.5", "off"), ("IA3", "Opus 5.5", "off"), ("IA4", "Opus 5.5", "off"),
         ("IA5", "Opus 5.5", "off"), ("IA6", "Opus 5.5", "off"), ("IA7", "Opus 5.5", "off"), ("IA8", "Opus 5.5", "off"),
         ("IA9", "Opus 5.5", "off"), ("IA10", "Opus 5.5", "off"), ("IA11", "Opus 5.5", "off"), ("IA12", "Opus 5.5", "off"),
         ("DD-IA1", "Opus 5.5", "on"), ("DD-IA2", "Opus 5.5", "on"), ("DD-IA3", "Opus 5.5", "off")]
STATUS = {'IA1': 'written 30 Oct', 'IA2': 'written 30 Oct'}
AUDIT_EVERY = 4
AUDIT_ROW = ('Stratified-sample audit of the last four units', 'Fable 5.1', 'on', 'prompt on Audits page')
FINAL_AUDIT = ('Audit 4', 'Final audit of the three deep dives plus a full read of the course against its goal, and a read-through as the persona', 'Fable 5.1', 'on', '')
NEXT_UNIT, AUDITS_RUN, NEXT_AUDIT = 'IA3', 0, 'Audit 1 after #4 (IA1, IA2, IA3, IA4)'

# ---- prose blocks (theme classes only) ---------------------------------------------------
HOME_H1 = "User Experience: the courses"
HOME_LEDE = "Courses on the practice of UX, written to be handed to other designers. The first is Information Architecture."
LEARN_TILE = ("The courses", "Goals, outcomes, units, and the written material to read.")
BUILD_TILE = ("How the courses get made", "Procedure, model rules, every brief, audit prompts, bibliography, changelog.")

FRAME = """<h2 class="hsec">Frame</h2>
<div class="report">
  <h2>A course for other designers, on the one skill the field documents least well</h2>
  <p>Information architecture is taught in the standard works as a set of systems (organisation, labelling, navigation, search) and shown in practice as a sitemap. The gap is the middle: how the same discipline scales from a brochure site to a backoffice with roles, workflows and three surfaces; how the artefact changes shape as the system does; and what a designer does when the research, the content or the stakeholders that the method assumes are not there. This course is built around that gap, on one fictional product, Perqo, that grows through four levels of complexity, and it is written for a mid-level designer who will be handed it, which makes it the Project's one exception to its single-reader rule (decided 29 Oct 2026).</p>
</div>
<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>One fictional product, four levels, one notation, and a whole part on working without the inputs.</strong></p>
  <ul><li>A single growing example keeps every artefact comparable.</li><li>Levels, not tools: tools change yearly, structures do not.</li><li>The missing-inputs case is the job as it is actually done.</li></ul>
  <p class="over"><strong>Override if:</strong> after IA8 the Perqo example cannot carry a reader's own product; then a second worked example (a content-heavy public site) is added as a deep dive in place of DD-IA3.</p>
</section>
<div class="report"><ul>
  <li><strong>Reader:</strong> a mid-level UX designer, three to six years in, little hands-on research experience. Every brief says so; <code>reader.md</code> is unchanged.</li>
  <li><strong>Example:</strong> Perqo, a fictional flexible-benefits platform: a sales site, an employee app, a managers' backoffice. Every Perqo fact is invented by the unit that needs it and labelled.</li>
  <li><strong>Figures:</strong> three to eight per unit, every one a drawing built from the unit's own content by <code>kit/viz.py</code>; no screenshots, no third-party images. The IA figure kinds are added to the kit before IA1 is written.</li>
  <li><strong>Where the evidence pushes back:</strong> most of the field's guidance is practice, not measurement. The course labels it as such and keeps the measured claims (foraging, breadth versus depth, card-sort reliability, findability failure) separate from the craft advice.</li>
</ul></div>"""

LEARN_LEDE = "Read here. Everything about how the units get written lives in Build."
LEARN_NOTE = "Order of writing: the four parts in order (IA1 to IA12), an audit after each part, then the three deep dives, DD-IA1 and DD-IA2 with search on."
LEARNING_NOTE = ''

BUILD_LEDE = "Method, model rules, and the pages that hold the briefs, the audits and the sources. Nothing here is course content."
BUILD_PICK = """<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>IA1 first, once the kit can draw the course's figures.</strong></p>
  <ul><li>IA2 fixes the notation; IA1 only needs the kinds to exist.</li><li>The four levels (IA5 to IA8) are the course; everything before them is what they rest on.</li><li>Deep dives last, DD-IA1 and DD-IA2 with search on.</li></ul>
  <p class="over"><strong>Override if:</strong> the figure kinds take more than one chat to add; then IA1 and IA2 are written with the four existing kinds and their figures redrawn when the kinds land.</p>
</section>"""
BUILD_BODY = """<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>One chat per unit, in the Learning Project. Copy the unit's brief from this course's Briefs page and paste it into a new chat; never reuse a chat across units. An isolated agent context counts as a chat (method.md §4, P31).</li>
    <li>The unit is written in full with its deliverable and its figures, each figure a fenced <code>viz</code> block of a kind <code>kit/viz.py</code> can draw. Every Perqo fact the unit invents is labelled and kept consistent with the Perqo facts already filed.</li>
    <li>A fresh checker in a new chat (Fable 5.1, <code>skills/audit-units</code> §3b) checks every cited claim and every figure's content against the unit, and the deliverable against the brief; findings are applied as exact replacements and the report filed as <code>audits/ux/fresh-check-&lt;code&gt;.md</code>.</li>
    <li>File the unit at <code>courses/ux/&lt;code&gt;-&lt;slug&gt;.md</code> with the front matter of method.md §7 (<code>skills/file-unit</code>); update this data file, rebuild, verify, publish Academy.</li>
    <li>After every fourth unit, the stratified-sample audit from the Audits page. The first fires after IA4.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Writing: Opus 5.5</strong> for every unit. The deliverable is written in the same chat as its unit.</li>
    <li><strong>Checking and auditing: Fable 5.1</strong>, a fresh context each time, with live search for the audits and for DD-IA1 and DD-IA2.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or audits.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>After every four written units, Fable 5.1 audits by stratified sample: one claim per section per unit, checked against its source; more than one in ten fails → full audit of that unit. Figures count as claims: a sampled figure is checked for whether its labels and numbers match the unit's sourced text. Units written with live search (DD-IA1, DD-IA2) are re-checked for staleness six months after writing.</p>
</section>"""

ORDER_LEDE = "One row per unit in writing order; an audit row every fourth written unit. Opus 5.5 writes; Fable 5.1 checks and audits. \"Search\" means the unit is written with web search on because its facts are current."
ORDER_NOTES = """<div class="report"><ul>
  <li><strong>Why this order:</strong> Part I (IA1 to IA4) gives the definitions, the notation, the research base and the organisation systems every later figure uses; Part II (IA5 to IA8) builds Perqo one level at a time, each level reusing the previous one's objects and labels, so the levels are written in order; Part III (IA9 to IA12) places the finished IA in the cycle and the business and ends with the missing-inputs playbook, which reuses IA7's decisions as its register; the deep dives last, the comparables and the cost one with search on.</li>
  <li><strong>Before IA1:</strong> the figure kinds the course needs (a sitemap and object map with notes, a decision tree with labelled branches, a matrix, a state diagram, a swimlane map, a wireflow) are added to <code>kit/viz.py</code> and <code>design/theme.css</code> §4i as their own backlog row; no unit is written until they draw.</li>
  <li><strong>Audit gate:</strong> no new unit starts while an audit verdict is REWRITE on an earlier one.</li>
</ul></div>"""
ORDER_FOOT = "The count starts at {start}."

BRIEFS_LEDE = "One brief per unit, self-contained: the shared preamble (the reader persona, the Perqo example, the course goal, the sourcing standard, the figure rule, the tone) is baked into every open brief. Copy, paste into a new chat, one unit per chat. Written units show their note instead. The course itself is read in <a href=\"#course-{k}\" data-target=\"course-{k}\">Learn · Course {K}</a>."
BRIEF_LABEL = 'Opus brief'

AUDITS_LEDE = "No audit yet. Each audit records: units sampled, claims checked, failures, verdict (pass / full audit / rewrite), and what changed."
AUDIT_LOG = []
AUDIT_PROMPTS_NOTE = "Run in the Learning Project with Fable 5.1, on command, after every fourth written unit. Paste the units or point at their vault paths. The prompts are method.md §6, verbatim; for this course a sampled figure is a sampled claim."
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

BIB_NOTE = "Every link cited in the written material, alphabetical by title. New units add to this list; a source that fails a staleness check is marked here."

TEMPLATE_LEDE = "What a project hub needs before the first unit is written: see the new-course skill and design/README.md."
TEMPLATE_NOTE = ''
TEMPLATE_BLOCKS = []

# newest first
CHANGELOG = [
    ('2026-11-01 14:00', "v4. Errata (backlog row H-3; Opus 5.5, own agent contexts, P31: one drafter, one checker before anything was applied, one fresh figure-checker per changed figure). IA2 (P74, P75): the notation gains the reading-direction mark, a small triangle by a relationship label that cannot read left to right or top to bottom, pointing at the object it reads towards (section 5.2 Lines and Labels, the legend, the notation sheet); the legend's Screen row says a button is a control, its Surface: Label row says the title is in lower case, a row says nothing is drawn dashed, and its caption names WCAG 2.2, 1.4.1 and says the tones were added; the cross-surface map is redrawn on a grid with two crossings and every label clear, two labels marked, its surface-to-surface labels made verbs from IA1's table (the paragraph before it changed with them), a count at each end of the object lines, approves in Approvals [over the limit], and its caption's fidelity and citations brought to the text. IA1 (P76): figure 2's caption says what it places and why the structure row is shaded. The Fable 5.1 checks owed (P49) cover both."),
    ('2026-10-30 23:50', "v3. IA2 The shapes IA takes: the artefact catalogue and the course notation written (Opus 5.5, isolated agent context, P31; search off), fresh-checked by a separate Opus 5.5 agent (fix, 3 errors, 10 should-fix, 17 minor; all applied; Fable 5.1 fresh check owed, P49) and filed: reading page under course IA, IA2 marked written, eight figures; the course notation is set for every later figure; IA3 next; Audit 1 counter 2 of 4 (deferred by Pedro, P49)."),
    ('2026-10-30 19:30', "v2. IA1 What information architecture is, and where it sits written (Opus 5.5, isolated agent context, P31; search off), fresh-checked by a separate Opus 5.5 agent (keep, 0 errors, 4 should-fix, 7 minor; all applied; Fable 5.1 fresh check owed, P49) and filed: reading page under course IA, IA1 marked written, six figures; IA2 next; Audit 1 counter 1 of 4 (deferred by Pedro, P49)."),
    ('2026-10-29 22:30', "v1. Course IA · Information Architecture created from the template on design/theme.css: the frame, the syllabus (twelve core units in four parts, three deep dives), the shared preamble with the reader persona and the fictional Perqo, one brief per unit, the build order with an audit after each part. Status coming soon; nothing written. The figure kinds the course needs are a backlog row before IA1."),
]
