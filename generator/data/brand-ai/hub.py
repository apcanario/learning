"""Brand + AI: the course data (AD5). Since A3, kit/build.py renders it into Academy through kit/mdcourse.py (one Academy
course per entry in COURSES), on design/theme.css. build_hub.py is retired.

Everything a reader sees of the two courses is here or in the two files beside it:
  units_data.py                          the units and their briefs (PRE, A, B), verbatim from the v5.1 generator
  audience-growth-across-platforms.md    the written material for A2, A6, A9 (the research report)
Text in this file is the v5.1 hub's text, re-marked with theme classes. Edit content here; edit style only in
design/theme.css. Prose blocks are HTML strings and may use only theme classes (design/README.md lists them).
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent

# ---- identity --------------------------------------------------------------------------
TITLE = 'Brand and AI Courses'             # <title>, kept so the republish keeps the artifact's name
BAR = 'BRAND + AI'                         # top-bar label
BRAND_HTML = 'BRAND <span>+</span> AI'     # drawer header
OUT = 'brand-and-ai-courses.html'
THEME_KEY = 'hub-theme'                    # localStorage key for the theme toggle (per artifact)
VERSION = 'v7.1 · 28 Oct 2026'
LEARN_C, BUILD_C = 'var(--red)', 'var(--orange)'

# ---- units -----------------------------------------------------------------------------
# The v5.1 generator ran units_data.py with this one substitution (A1's title); kept so titles match.
_ns = {}
exec((HERE / 'units_data.py').read_text().replace('Positioning: Personal Mythology as a format', 'Positioning: the journey as a format'), _ns)
PRE, A, B = _ns['PRE'], _ns['A'], _ns['B']

GOAL_A = ("by the end of the course the reader can state, in one sentence, who his audience is and what they pay for; run a publishing system that holds a bi-weekly cadence inside 5–7 h/week for twelve months; and read his own channel metrics against sourced benchmarks to decide, with evidence, whether to continue, change format or stop.")
GOAL_B = ("by the end of the course the reader routes each recurring task to the right model and effort level without guessing; briefs any unit, draft or audit so that the first output is usable; keeps a project structure that does not rot; and verifies AI-written material by sampling before trusting it.")
NAME_A = 'Building a Marketable Personal Brand'
NAME_B = 'Using AI to Build a Brand'

COURSES = [
    dict(key='A', name=NAME_A, color='var(--teal)', units=A, goal=GOAL_A, slug='brand',
         tile="Who pays, for what, how long it takes, what it costs in hours, and what the record-as-brand changes.",
         intro="Not \"how to be an influencer\": who pays, for what, how long it takes, what it costs in hours, and what the record-as-brand changes about all of it. Nine core units and two deep dives.",
         outcomes="<li><strong>Outcome 1</strong> — a positioning a stranger can repeat, tested against five sourced comparables (A1, DD-A1).</li><li><strong>Outcome 2</strong> — a publishing system that holds bi-weekly for twelve months inside the hour budget (A3, A5, A8).</li><li><strong>Outcome 3</strong> — a metrics sheet and benchmark table he reads quarterly to decide continue / change format / stop (A6, A9, A7, DD-A2).</li>"),
    dict(key='B', name=NAME_B, color='var(--purple)', units=B, goal=GOAL_B, slug='ai',
         tile="Which model for which task, how to brief, where the setup leaks, and what he doesn't know he's doing badly.",
         intro="Not how LLMs work. Which model for which of his tasks, how to brief so he stops re-explaining, where the project setup leaks, and what he does not know he is doing badly. Eight core units and three deep dives.",
         outcomes="<li><strong>Outcome 1</strong> — a model-routing table for every recurring task, with cost and effort (B1, B2).</li><li><strong>Outcome 2</strong> — a prompt library and a project structure that produce usable first outputs (B3, B4, B5, DD-B3).</li><li><strong>Outcome 3</strong> — a verification protocol and a content pipeline, both run on real work before the course ends (B6, B7, B8, DD-B1).</li>"),
]
COURSE_NOTE = "Not content for its own sake: every unit is sourced to peer-reviewed, platform-official or large-sample data, labels anecdote and vendor data as such, and ends with a shipped deliverable."

# ---- written material (reading pages under Learn) ---------------------------------------
# A unit whose brief starts with "WRITTEN" is written; WRITTEN maps it to its reading page.
READINGS = [
    dict(id='read-audience-growth', md='audience-growth-across-platforms.md', course='A',
         title='Audience growth across platforms (research, superseded)', covers=[], name='Audience growth (research)',
         intro="Superseded on 28 Oct 2026 by the A9, A2 and A6 units, after Audit 1 found 23 of 91 claims failing and the deliverables missing; kept as the record. Research run 27 Oct 2026 across five tracks (YouTube mechanics; Instagram and TikTok; platform strategy; retention and conversion; niche landscape). It stands as the written material for A2, A6 and A9 and feeds A4 and A7. Most figures are correlational and vendor-published; the text says so where it applies. Gaps: no measured calendar-time-to-milestone data, no short-form→long-form conversion rate, no primary newsletter churn, no Portuguese-language RPM or SEO data; the YPP February 2027 threshold is cited via AIR, not verified against YouTube Help."),
    dict(id='read-a9', md='units/A9-what-to-expect-benchmarks.md', course='A',
         title='What to expect: benchmarks', covers=['A9'], name='A9 · Benchmarks',
         intro="Unit A9, rewritten 28 Oct 2026 by Opus 5.5 in its own chat, search on, from its brief after Audit 1; fresh check the same day (Fable 5.1): fix, 2 errors, 15 should-fix, 8 minor, all applied. Deliverables: the expectation sheet (one row per benchmark, source and label on each) and the quarterly checkpoint schedule with its four verdicts. Replaces the research page as the written material for A9. Staleness check due 28 Apr 2027."),
    dict(id='read-a2', md='units/A2-audience-and-platform-economics.md', course='A',
         title='Audience and platform economics', covers=['A2'], name='A2 · Audience and platforms',
         intro="Unit A2, rewritten 28 Oct 2026 by Opus 5.5 in its own chat, search on; fresh check the same day (Fable 5.1): fix, 3 errors, 13 should-fix, 11 minor, all applied. Deliverables: the audience profile (one sentence, with the basis and label for each trait) and the platform allocation for 5–7 hours a week, with the bad-fortnight cut order. Flags for A3: the evidence supports one Short per episode, not the brief's 2–3. Staleness check due 28 Apr 2027."),
    dict(id='read-a6', md='units/A6-how-growth-works-per-platform.md', course='A',
         title='How growth works, per platform', covers=['A6'], name='A6 · Growth per platform',
         intro="Unit A6, rewritten 28 Oct 2026 by Opus 5.5 in its own chat, search on; fresh check the same day (Fable 5.1): fix, 1 error, 9 should-fix, 7 minor, all applied. Deliverables: the per-platform playbook (each rule names its evidence; his own conventions marked) and the metrics sheet read once a quarter on A9's checkpoint dates. Unverified: Studio and Instagram menu locations. Staleness check due 28 Apr 2027."),
    dict(id='read-b2', md='units/B2-choosing-the-model.md', course='B',
         title='Choosing the model', covers=['B2'], name='B2 · Choosing the model',
         intro="Unit B2, written 28 Oct 2026 by Opus 5.5 in its own chat, search on (lineup, prices, plan rules and benchmarks dated that day; staleness check due 28 Apr 2027); fresh check the same day (Fable 5.1): fix, 3 errors, 10 should-fix, 14 minor. Deliverable: the model-routing table for his recurring tasks, with effort, the evidence behind each pick and an override trigger per row. Known gaps, from the writer's unsure list: Artificial Analysis's per-task costs differ between its leaderboard and model pages; the per-model rate at which claude.ai usage is drawn is undocumented; the Shōmen token counts are assumptions; whether self-preference bias carries between sibling models is untested."),
    dict(id='read-b1', md='units/B1-mental-model.md', course='B',
         title='Mental model', covers=['B1'], name='B1 · Mental model',
         intro="Unit B1, written 28 Oct 2026 by Opus 5.5 in its own chat, with live search (Anthropic product facts checked and dated that day; staleness check due 28 Apr 2027). Seven sections in the brief's order, then the deliverable: the five-minute model of how Claude works, as plain prose. Known gaps, from the writer's unsure list: the 200K claude.ai window is taken from an undated help article; the 2.7 characters-per-token figure is arithmetic on Anthropic's glossary, not a measurement; the skill-description cost uses Anthropic's per-skill average; whether claude.ai usage reflects prompt caching, and how much memory a new chat receives, are undocumented; the nondeterminism study was run on Qwen, not Claude."),
]
WRITTEN = {'A2': 'read-a2', 'A6': 'read-a6', 'A9': 'read-a9', 'B1': 'read-b1', 'B2': 'read-b2'}

# ---- build order -----------------------------------------------------------------------
DONE_ROWS = [('—', 'A2 · A6 · A9', 'Audience growth research → rewritten as three units after Audit 1', 'research: Fable 5.1 agents; units: Opus 5.5, fresh-checked by Fable 5.1', 'on', 'rewritten 28 Oct')]
ORDER = [("B1", "Opus 5.5", "off"), ("B2", "Opus 5.5", "on"), ("B3", "Opus 5.5", "off"), ("B4", "Opus 5.5", "off"), ("A1", "Opus 5.5", "off"), ("DD-B3", "Opus 5.5", "on"), ("A3", "Opus 5.5", "off"), ("B5", "Opus 5.5", "off"), ("A4", "Opus 5.5", "off"), ("A5", "Opus 5.5", "off"), ("B7", "Opus 5.5", "off"), ("A7", "Opus 5.5", "off"), ("A8", "Opus 5.5", "on"), ("B6", "Opus 5.5", "off"), ("B8", "Opus 5.5", "on"), ("DD-A1", "Opus 5.5", "on"), ("DD-B1", "Opus 5.5", "off"), ("DD-A2", "Opus 5.5", "off"), ("DD-B2", "Fable 5.1", "off")]
STATUS = {'B1': 'written 28 Oct', 'A9': 'rewritten 28 Oct', 'A2': 'rewritten 28 Oct', 'A6': 'rewritten 28 Oct', 'B2': 'written 28 Oct'}   # unit code -> status text in the build-order table once filed
AUDIT_EVERY = 4
AUDIT_ROW = ('Stratified-sample audit of the last four units', 'Fable 5.1', 'on', 'prompt on Audits page')
FINAL_AUDIT = ('Audit 6', 'Final audit of DD-B2 plus a full read of both courses against their goals', 'Fable 5.1', 'on', '')
NEXT_UNIT, AUDITS_RUN, NEXT_AUDIT = 'B3', 1, 'after three more units (Audit 2 after B3, B4, A1)'

# ---- prose blocks (theme classes only) ---------------------------------------------------
HOME_LEDE = "Two courses for one reader, written one unit at a time. <strong>Learn</strong> is where the finished units are read. <strong>Build</strong> is where they get made: method, briefs, audits, sources, history."
HOME_H1 = "Brand + AI: two courses"
LEARN_TILE = ("The courses", "Goals, outcomes, units, and the written material to read.")
BUILD_TILE = ("How the courses get made", "Procedure, model rules, every Opus brief, Fable audit prompts, bibliography, changelog.")

FRAME = """<h2 class="hsec">Frame</h2>
<div class="report">
  <h2>The brand is the method, and the method is the record</h2>
  <p>Working name to be decided. "I get consumed by something, build a syllabus, go on the journey, and record it so I don't forget it." Karate was season one. The half marathon, the weight loss and the history course are the next journeys; building with AI is the fourth. Plurality is the register, not the hook: each piece leads with one journey and the breadth shows across pieces. ADHD is public under his name (decided 27 Oct 2026); everything else gets a pre-mortem before first disclosure. Failures stay in the record.</p>
</div>
<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>Journeys, recorded.</strong> Shōmen is one path off it, not the engine. Leaving corporate is not on the table for 24 months; this is a build alongside Infios, measured quarterly.</p>
  <ul><li>Generalist brands die on variety and live on a repeatable format.</li><li>The ADHD-creator space sells relatability; this has rigour.</li><li>Every existing output already fits: vlog, syllabi, journal, pcblueprint.</li></ul>
  <p class="over"><strong>Override if:</strong> after six pieces in the format nobody can describe the channel back to him in one sentence. Then the format is wrong, not the breadth.</p>
</section>
<div class="report"><ul>
  <li><strong>Cost:</strong> 5–7 h/week; €0–300 in gear; an editor only after the cadence has held for six months.</li>
  <li><strong>Horizon:</strong> 18–36 months to 1,000 YouTube subscribers at a bi-weekly cadence; a brand that moves Shōmen revenue is a 24-month question at best.</li>
  <li><strong>Where the research pushes back:</strong> the data says season one is one journey in one format, and karate is the thin niche where a 10–20K channel is visible. History and AI are a year-two layer by the format-drift evidence. His call.</li>
</ul></div>"""

LEARN_LEDE = "Read here. Everything about how the units get written lives in Build."
LEARN_NOTE = "Order of writing: B1–B4 first, then A1, DD-B3, A3, A4, A5, A7, A8 with B5–B8 interleaved (B5 beside A3, B7 beside A5), then the four deep dives; DD-A2 and DD-B2 last. The history course keeps its own slot."

LEARNING_NOTE = """<section class="howto edge" style="--hc:var(--blue)"><h2>Now in Academy</h2>
  <p>Since v7 (28 Oct 2026, A3) the two courses are read here, in Academy, with the history courses; the standalone hub is gone. Where the procedure below and the Project's <code>method.md</code> differ, <code>method.md</code> governs: the Project, the vault path, the audit cadence and the review model are set there. The text below is kept as the v5.1 record.</p>
</section>"""

BUILD_LEDE = "Method, model rules, and the pages that hold the briefs, the audits and the sources. Nothing here is course content."
BUILD_PICK = """<section class="howto edge" style="--hc:var(--red)"><h2>Pick</h2>
  <p><strong>B1 first, written by Opus 5.5 in a new chat in a new Project.</strong></p>
  <ul><li>B1 makes every later brief cheaper; it is the cheapest unit.</li><li>A separate Project keeps 21 units out of the personal assistant.</li><li>Fable reads nothing until four units exist.</li></ul>
  <p class="over"><strong>Override if:</strong> the brand course should move first; then A1 first, B1 second, same setup.</p>
</section>"""
BUILD_BODY = """<div class="report">
  <h2>Procedure</h2>
  <ol>
    <li>Make a Project ("Courses — Brand &amp; AI"). Add to its knowledge: this page, the research report, the five notes files. Project instructions, three lines: who the reader is; this page holds every brief; each unit is written in full, not described.</li>
    <li>One chat per unit. Copy the unit's brief from its Briefs page, paste it into a new chat in that Project. Never reuse a chat across units; leaked context is how a course starts repeating itself.</li>
    <li>Save the output to the vault as <code>courses/brand-ai/&lt;code&gt;-&lt;slug&gt;.md</code> (e.g. <code>B1-mental-model.md</code>), same shape as the history course. Hand it to the assistant: it commits, adds the unit to Learn, moves the counters, adds a changelog line.</li>
    <li>Units that need live facts (A8, B2, B8, DD-A1, DD-B3) are written with web search on; the briefs say so. Everything else without.</li>
    <li>After every fourth unit, run the audit prompt from the Audits page. The first fires after B1.</li>
  </ol>
  <h2>Models</h2>
  <ul>
    <li><strong>Writing: Opus 5.5</strong> for all remaining units. The quality gap shows most on long-form synthesis, which is this.</li>
    <li><strong>The shipped deliverable</strong> is written in the same chat as its unit, never separately, so it inherits the unit's reasoning.</li>
    <li><strong>Reviewing: Fable 5.1</strong>, in the personal-assistant Project where this hub lives. One claim per section per unit checked against its source; more than one in ten fails → full audit.</li>
    <li><strong>Not Sonnet or Haiku</strong> for units or audits. They are the right tools for turning a finished unit into posts, a Shorts list or an email; that is B7's pipeline.</li>
  </ul>
</div>
<section class="howto edge" style="--hc:var(--gold)"><h2>Review rule</h2>
  <p>After every four written units, across both courses, Fable 5.1 audits by stratified sample: one claim per section per unit, checked against its source; more than one in ten fails → full audit of that unit. Units written with live search (A2, A6, A9, A8, B2, B8, DD-B3) are re-checked for staleness six months after writing.</p>
  <p class="warn">Audit 1 ran 28 Oct: B1 PASS; A2·A6·A9 REWRITE. The three were rewritten the same day from their briefs, each fresh-checked by Fable 5.1 (A9 2 errors, A2 3, A6 1; all fixed). B2 is next; every unit gets a fresh checker.</p>
</section>"""

ORDER_LEDE = "One row per unit in writing order; an audit row every fourth written unit. Opus 5.5 writes; Fable 5.1 audits and writes the last deep dive, which needs the chat history. \"Search\" means the unit is written with web search on because its facts are current."
ORDER_NOTES = """<div class="report"><ul>
  <li><strong>Why this order:</strong> B1–B4 first so every later brief is cheaper; A1 and A3 next because the Athens edit and the half-marathon season need the positioning and the journey system now; DD-B3 between them (added 28 Oct 2026) so B5, B7 and DD-B1 inherit the practitioners' methods it verifies; B5 beside A3 and B7 beside A5 because they build the same pipeline; A7, A8, B6, B8 once there is a channel to measure; deep dives last, DD-B2 last of all.</li>
  <li><strong>Cadence:</strong> one unit per 3–4 days is the sustainable rate alongside the half-marathon block; that is 10–11 weeks to the end, with audits adding an evening each.</li>
  <li><strong>Audit gate:</strong> no new unit starts while an audit verdict is REWRITE on an earlier one.</li>
</ul></div>"""
ORDER_FOOT = "A2, A6 and A9 are already written as the audience-growth research, which is why the count starts at {start}."

BRIEFS_LEDE = "One brief per unit, self-contained: the shared preamble (reader, brand thesis, course goal, sourcing standard, tone, citation rules) is baked into every open brief. Copy, paste into a new Opus chat, one unit per chat. Written units show their note instead. The course itself is read in <a href=\"#course-{k}\" data-target=\"course-{k}\">Learn · Course {K}</a>."
BRIEF_LABEL = 'Opus brief'

AUDITS_LEDE = "One audit run. Each audit records: units sampled, claims checked, failures, verdict (pass / full audit / rewrite), and what changed."
AUDIT_LOG = [('2026-10-28', "Audit 1 (Fable 5.1, stratified sample, then full audit). Units: A2·A6·A9 (the audience-growth research) and B1. <strong>B1: PASS</strong>, 7 of 7 sampled claims hold, deliverable present. <strong>A2·A6·A9: sample 1 of 8 FAIL → full audit: 91 claims, 23 FAIL, 0 STALE, nothing invented, no conclusion flips → REWRITE</strong>, because the three deliverables (audience profile and allocation; playbook and metrics sheet; benchmarks table and checkpoints) do not exist and two table rows rest on figures no vidIQ page contains. Pattern: qualifiers the source does not carry. One non-accuracy item: a cited creator profile is a minor's; the name comes out. Consequences: B2 waits for the rewrite; every later Brand + AI unit gets a fresh checker (method §1 override). Report: <code>audits/brand-ai/audit-1.html</code>. The three fresh checks that followed (A9 2 errors, 15 should-fix, 8 minor; A2 3/13/11; A6 1/9/7; all applied) are filed as <code>audits/brand-ai/fresh-check-A9.md</code>, <code>fresh-check-A2.md</code> and <code>fresh-check-A6.md</code>.")]
AUDIT_PROMPTS_NOTE = "Run in the personal-assistant Project with Fable 5.1, on command, after every fourth written unit. Paste the units or point at their vault paths."
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

TEMPLATE_LEDE = "What a project hub needs before the first unit is written. Copy this page's structure (the generator scripts are in the zip); change the content. Three requirement sets: the website, the syllabus, the AI rules."
TEMPLATE_NOTE = """<section class="howto edge" style="--hc:var(--blue)"><h2>Since v6</h2>
  <p>The website requirements below are now met by <code>design/theme.css</code>, the Personal Mythology system: the drawer slides out at every width (no persistent sidebar), and a new hub is started with the <code>new-course</code> skill from the generator in the Learning Project. The text below is kept as the v5.1 record.</p>
</section>"""
TEMPLATE_BLOCKS = [
    ('Website UX', """<ul>
      <li>Two hubs, visibly separated by colour: <strong>Learn</strong> (courses, written units, reading pages) and <strong>Build</strong> (method, briefs, audits, bibliography, template, changelog). Home shows both as tiles and the status block.</li>
      <li>Pages, not one scroll; hash-routed so every page has a link. Fixed top bar: menu (left), title, current page, theme toggle. Left sidebar persistent on desktop, drawer on phone; group labels carry the hub colour. 44 px targets.</li>
      <li>A course page shows the course: goal, three outcomes mapped to units, progress, unit cards with status and a "Read" action. Prompts never appear on a course page; they live in Build · Briefs.</li>
      <li>Written material has its own reading page under Learn, linked from the unit cards it covers, with a back link to the course.</li>
      <li>Dark first, light designed not inverted; toggle remembers per browser, follows the system when unset. Fonts DM Sans + Space Mono. Dark: page #0a0a0c, cards #131316, border #1e1e24. Colours: Learn #ff6b6b, Build #f4a261, Course A #2a9d8f, Course B #9b5de5, deep dives #e9c46a, goals #457b9d. No grey as a dominant accent.</li>
      <li>No horizontal overflow at 400 px: long text wraps anywhere; only tables and code may scroll, inside their own container.</li>
    </ul>"""),
    ('Syllabus requirements', """<ul>
      <li>Course = 8–10 core units + 2 or 3 deep dives. Each unit: code, title, one-line scope, a shipped deliverable, an Opus brief. No length rule; the topic decides.</li>
      <li>Course goal in one sentence plus three measurable outcomes, each mapped to the units that deliver it, shown on the course page and baked into every brief.</li>
      <li>Every unit ends with something shipped (a document, a table, a skill, a model), built in full inside the unit, not described.</li>
      <li>Flag units that depend on current facts; they are written with live search and re-checked for staleness six months on.</li>
      <li>Deep dives written last. Two are standing: the comparables (what others did) and the hard-number one (money, time, exit math). A third is allowed when the subject has a documented practice worth verifying against its primary sources (course B: DD-B3); the history courses carry three by their own logic.</li>
      <li>An explicit writing order, with interleaving where two units build the same asset.</li>
      <li>Frame first: the pick, the reasons, the override condition, and where the evidence pushes back. The reader decides; the hub records.</li>
    </ul>"""),
    ('AI prompt and model rules', """<ul>
      <li>One shared preamble per course (reader, thesis, course goal, sourcing standard, tone, citation rules, "search before writing when facts are current"), baked into every brief so each chat is self-contained.</li>
      <li>Sourcing standard: peer-reviewed, platform-official or large-sample vendor data; anecdote and vendor data labelled; no uncited figures; no invented names or numbers; advice without evidence fails the unit.</li>
      <li>One chat per unit. Never reuse a chat across units. The deliverable is written in the same chat as its unit.</li>
      <li>Writing: Opus 5.5. Audit: Fable 5.1 with the stratified-sample prompt every four units (more than one in ten fails → full audit) and the staleness prompt at six months. Sonnet/Haiku only for derivative work.</li>
      <li>Output saved to the vault at <code>courses/&lt;course&gt;/&lt;code&gt;-&lt;slug&gt;.md</code>; the hub adds it to Learn, moves counters, logs the change, extends the bibliography.</li>
    </ul>"""),
]

# newest first; {A} and {B} are the course names
CHANGELOG = [
    ('2026-10-28 12:45', "v7.1. Housekeeping (P14, P15, P3): the syllabus rule reads 2 or 3 deep dives per course; the build-order lede's remaining-unit count is derived from ORDER and STATUS by kit/mdcourse.py instead of typed; the three fresh-check reports of A9, A2 and A6 are filed in audits/brand-ai/ and linked from the Audits page."),
    ('2026-10-28 12:30', "v7. The hub is retired (A3): both courses are read in Academy, each with its own drawer (Units; How it is built: method, build order, briefs, audits, bibliography, changelog) and each written unit as a page with prev/next and Continue. Same data file, same text; the Learn/Build split and the Hub template page are gone from the site (TEMPLATE_BLOCKS stays here for the new-course skill). No unit changed."),
    ('2026-10-28 11:10', "v6.8. DD-B3 Deep dive: how the best practitioners use the tool added to course B (units_data.py), search on: Karpathy's documented practice 2025–26 from his own posts, talks and repositories, and the other methods with a named author and a primary source (Anthropic, OpenAI, Willison, Mollick, spec-driven workflows, the chain-of-thought literature), each graded by evidence and tested for transfer from code to his work; deliverable: method cards and ten operating rules. Placed after A1 in the build order so B5, B7 and DD-B1 inherit it; Audit 2 still after B3, B4, A1. Course B is now 8 core units and 3 deep dives; 22 units, 17 remain. Build-order fix in build_hub.py: rows are numbered as courses-index.md numbers them (B1 is 4, Audit 1 after it, Audit 2 after A1), and the last unit no longer gets a sample-audit row beside the final audit. No written unit changed."),
    ('2026-10-28 10:30', "v6.7. Course B renamed Using AI to Build a Brand (hub.py NAME_B, the filed B units' front matter). Units unchanged."),
    ('2026-10-28 10:10', "v6.6. Home title is the hub's name (Brand + AI: two courses); Academy now lists course A under its Marketing track and course B under Technology, each linking here. No unit changed."),
    ('2026-10-28 09:30', "v6.5. Rebuilt on theme v2 (design/theme.css section 6, responsive): tablet from 768 px widens the column to 760 px and puts course cards in two columns; desktop from 1100 px turns the drawer into a persistent 300 px sidebar with the current page highlighted, no backdrop and no menu button. The phone layout is unchanged. check_page.py now runs a phone, tablet and desktop pass with the 6 px gap and 44 px target checks. No unit changed."),
    ('2026-10-28 08:20', "v6.4. B2 Choosing the model written (Opus 5.5, own chat, search on), fresh-checked by Fable 5.1 (fix, 3 errors, 10 should-fix, 14 minor; every finding applied) and filed: reading page under Learn, B2 marked written, counters moved. Next: B3. The hub now lives in the learning-project repository (NEXT-SESSION.md)."),
    ('2026-10-28 07:30', "v6.3. A9, A2 and A6 rewritten from their briefs (Opus 5.5, one chat each, search on) and fresh-checked by Fable 5.1 in separate chats (A9: 2 errors, 15 should-fix, 8 minor; A2: 3/13/11; A6: 1/9/7; every finding applied as an exact replacement). Each gets its own reading page under Learn; the 27 Oct research page stays as the superseded record. A2 flags A3's 2–3 Shorts per episode as above AIR's crowding line; one Short per episode is the allocation. Audit gate cleared; B2 next."),
    ('2026-10-28 07:05', "v6.2. Audit 1 logged (Fable 5.1): B1 PASS; A2·A6·A9 full audit, 23 of 91 claims failed, REWRITE for the missing deliverables. Rewrites of A9, A2 and A6 started, A9 first; fresh checker added for every later unit."),
    ('2026-10-28 05:55', "v6.1. B1 Mental model written (Opus 5.5, own chat in the Learning Project, search on) and filed: reading page under Learn, B1 marked written, counters moved. Four units are now written, so Audit 1 (Fable 5.1) is due before B2."),
    ('2026-10-27 19:45', "v6. Rebuilt on design/theme.css, the Personal Mythology visual system, in the Learning Project; the hub's own stylesheet is gone. Same pages and order. The drawer slides out at every width (the desktop sidebar is retired); viewport tag added; light mode on the theme's palette. Build and Hub template pages carry a note that the Learning Project's method.md now governs the procedure."),
    ('2026-10-27 19:00', "v5.1. Back button in the top bar (page history inside the hub) and swipe-from-left-edge to go back. New Build · Build order page: eighteen remaining units in writing order with model, search flag and audit rows every fourth unit."),
    ('2026-10-27 18:55', "v5. Split into Learn and Build hubs with their own colours. Course pages now show the course only (goal, outcomes, progress, units with Read / not-written actions); every Opus brief moved to Build · Briefs. Written material gets a reading page under Learn, linked from the units it covers. Home shows the two hubs first."),
    ('2026-10-27 18:50', "v4.2. Courses named plainly: {A} (A), {B} (B)."),
    ('2026-10-27 18:45', "v4.1. Course goals with three outcomes each added to both course pages and to every brief; sourcing standard added to the preamble. Fable audit and staleness-check prompts added."),
    ('2026-10-27 18:40', "v4. Multi-page hub: hash-routed pages, fixed top bar with left sidebar, light mode with toggle, per-course pages with progress, status pills on units, hub-template page. Overflow on deep-dive cards fixed."),
    ('2026-10-27 14:50', "v3. \"How to build\" section added (procedure, models for writing and review). Tabs replaced by a fixed bar with a side menu."),
    ('2026-10-27 14:45', "Page renamed; the borrowed umbrella name removed from the brand thesis and every brief. Umbrella name is open; A1 proposes three."),
    ('2026-10-27 15:00', "v2. Merged into one page: both syllabi, Opus briefs, the audience-growth research, review rule and audit log, bibliography, changelog. Length rules removed."),
    ('2026-10-27 14:30', "Audience-growth research delivered (five tracks). A2, A6, A9 marked written."),
    ('2026-10-27 14:16', "A6 rewritten as per-platform growth mechanics; A9 (benchmarks) added."),
    ('2026-10-27 12:30', "Frame rewritten to the journey-record method; competing ended 25 Oct noted; live journeys listed."),
    ('2026-10-27 09:40', "v1. Assessment, pick, costs, two syllabi (8+2 each), order and cadence."),
]
