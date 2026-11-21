"""P-DEC11: recreate S-DEC5's template test in a repo copy (never the main tree): course `home-composting` (two units
HC1, HC2, about 1,170 words each, three sections each), track `garden`, brand and edition `fieldnotes`. S-DEC5's
report gives no file contents; this follows its description and S-DEC4's recreation (out/s-dec4/02-verify-names.md).
No .py under kit/ is touched.

  python3 out/DEC-C/p_dec11_template.py <copy-root>
"""
import pathlib, sys

root = pathlib.Path(sys.argv[1]).resolve()
assert root != pathlib.Path('/home/claude/learning'), 'never in the main tree'
C = root / 'courses/home-composting'
(C / 'pages').mkdir(parents=True, exist_ok=True)

(C / 'course.toml').write_text('''id = "home-composting"
family = "markdown"
short = "Home composting"
label = "HOME COMPOSTING"
name = "Home composting"
color = "var(--teal)"
home_id = "home-composting"
status = "in progress"
tracks.HC = ["garden", "Home composting"]
tiles.HC = "Turning kitchen and garden waste into compost at home."
data = "courses/home-composting/course.toml"
vault = "courses/home-composting"
sourcing_part = "Part 2"
eyebrow = "HOME COMPOSTING"

[pack]
course_note = 'Every unit names its sources and ends with a deliverable built in full.'
order_lede = 'One row per unit in writing order.'
order_foot = 'The count starts at {start}.'
bib_note = 'Every link cited in the written material, alphabetical by title.'
title = 'Home composting'
bar = 'HOME COMPOSTING'
brand_html = 'HOME <span>/</span> COMPOSTING'
out = 'home-composting.html'
theme_key = 'home-composting-theme'
learn_c = 'var(--red)'
build_c = 'var(--orange)'
home_lede = 'A short course on composting at home. <strong>Learn</strong> is where the finished units are read. <strong>Build</strong> is where they get made.'
home_h1 = 'Two hubs: one to learn from, one to build with'
learn_note = 'Written in order, HC1 then HC2.'
template_lede = 'What a project hub needs before the first unit is written.'
template_note = ''
learn_tile = ['The courses', 'Goals, outcomes, units, and the written material to read.']
build_tile = ['How the courses get made', 'Procedure, model rules, every brief, bibliography, changelog.']
order = [
  ['HC1', 'Opus 5.5', 'off'],
  ['HC2', 'Opus 5.5', 'off'],
]

[pack.status]

[[pack.courses]]
key = 'HC'
name = 'Home composting'
color = 'var(--teal)'
slug = 'hc'
goal = 'by the end of the course the reader can run a compost heap at home that turns waste into usable compost.'
tile = 'Turning kitchen and garden waste into compost at home.'
intro = 'A two-unit course on composting at home. It is not a course on industrial composting.'
outcomes = '<li><strong>Outcome 1</strong> — set up a heap with the right mix (HC1).</li><li><strong>Outcome 2</strong> — keep it working and judge when it is done (HC2).</li>'
[[pack.courses.units]]
code = 'HC1'
title = 'Setting up the heap'
scope = 'Site, container, browns and greens.'
deliverable = 'a setup checklist'
[[pack.courses.units]]
code = 'HC2'
title = 'Keeping it working'
scope = 'Moisture, air, heat and the finished compost.'
deliverable = 'a monthly care sheet'

[[pack.changelog]]
date = '2026-11-19 10:00'
text = 'v2. HC2 filed.'
[[pack.changelog]]
date = '2026-11-18 10:00'
text = 'v1. Hub created from the template on design/theme.css.'
''')

(C / 'briefs.md').write_text('''# Home composting · briefs

## Preamble

Write one unit of a short self-study course. Reader: a home gardener. Tone: direct. Course goal: {GOAL} End with the unit's deliverable, built out in full.

## HC1

Unit HC1, Setting up the heap. Cover: site, container, browns and greens. Deliverable: a setup checklist.

## HC2

Unit HC2, Keeping it working. Cover: moisture, air, heat, finished compost. Deliverable: a monthly care sheet.
''')
(C / 'pages/briefs-lede.md').write_text('One brief per unit, self-contained. The course itself is read in <a href="#course-{k}">Learn · Course {K}</a>.\n')
(C / 'pages/build-body.md').write_text('<div class="report"><h2>Procedure</h2>\n  <p>One chat per unit, brief from Build · Briefs, unit filed to <code>courses/home-composting/</code>, checked before filing, hub rebuilt.</p></div>\n')
(C / 'pages/frame.md').write_text('<h2 class="hsec">Frame</h2>\n<div class="report"><h2>Compost at home</h2><p>Kitchen waste is a resource.</p></div>\n')
(C / 'pages/order-notes.md').write_text('<div class="report"><ul><li><strong>Why this order:</strong> setup comes before care.</li></ul></div>\n')

S = ['A heap works when the mix of materials, the water and the air are kept in balance over the weeks.',
     'Brown materials such as dry leaves, straw and torn cardboard give the microbes carbon and keep the heap open.',
     'Green materials such as vegetable peelings, coffee grounds and fresh grass clippings give them nitrogen and water.',
     'Too many greens make a wet, sour heap; too many browns make a dry heap that barely changes for months.',
     'Turning the heap with a fork lets air in, and the microbes that need air work faster than those that do not.',
     'A handful squeezed hard should give a drop or two of water and no more, like a wrung sponge.',
     'Chop large pieces before they go in, because small pieces offer more surface for the microbes to work on.']


def unit(code, title, written, heads):
    body, n = [], 0
    for h in heads:
        body.append(f'## {h}\n')
        for p in range(3):
            para = ' '.join(S[(p + k) % len(S)] for k in range(7))
            body.append(para + '\n')
    text = '\n'.join(body)
    return (f'---\ncode: {code}\ntitle: {title}\ncourse: home-composting · HC · Home composting\nmodel: Opus 5.5\n'
            f'written: {written}\nsearch: off\nintro: Unit {code} of Home composting, written for the template test.\n---\n\n'
            f'# {code} · {title}\n\n{text}\n## Sources\n\n- None cited; template test.\n')


(C / 'HC1-setting-up.md').write_text(unit('HC1', 'Setting up the heap', '2026-11-18', ['1 · The site', '2 · The container', '3 · Browns and greens']))
(C / 'HC2-keeping-it-working.md').write_text(unit('HC2', 'Keeping it working', '2026-11-19', ['1 · Moisture', '2 · Air and heat', '3 · Finished compost']))

cat = root / 'catalog.toml'
t = cat.read_text()
if 'id = "garden"' not in t:
    t = t.replace('\n[[tracks]]\nid = "history"', '\n[[tracks]]\nid = "garden"\nhero = [[0.50, 0.50], [0.50, 0.50]]\nname = "Garden"\ncolor = "var(--teal)"\nlede = "Growing and composting at home."\n\n[[tracks]]\nid = "history"', 1)
    cat.write_text(t)

(root / 'brands/fieldnotes.toml').write_text('''name = "Fieldnotes"
mark = "FIELD<span>/</span>NOTES"
lede = "Short courses for the garden, one unit at a time."
repo = "https://example.org/fieldnotes"
id_base = "https://example.org/fieldnotes/"
fonts_href = "https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Source+Serif+4&display=swap"
log_area = ["Fieldnotes", "The site"]

[storage]
theme = "fn-theme"
tab = "fn-last-report"
units = "fn-groups-open"
last = "fn-last-"
section = "fn-sec-"

[tokens]
serif = '"Source Serif 4",Georgia,serif'

[tokens_light]

[[rules]]
head = "One reader."
text = "Each course is written for a home gardener, to be read in order."

[[rules]]
head = "Built in full."
text = "Each unit ends with its deliverable built in full."
''')
(root / 'editions/fieldnotes.toml').write_text('''title = "Fieldnotes"
courses = ["home-composting"]
omit = ["changelog", "backlog"]
site = "editions/fieldnotes"
brand = "fieldnotes"
url = "https://example.org/fieldnotes/"
deploy_remote = "https://example.org/git/fieldnotes.git"
''')
ci = root / 'docs/courses-index.md'
if '## Home composting' not in ci.read_text():
    ci.write_text(ci.read_text().rstrip('\n') + '\n\n## Home composting\n\nThe template test course. 2 of 2 written.\n\n'
                 '| # | Unit | Course | Title | Status | Model | Search | Path |\n|---|---|---|---|---|---|---|---|\n'
                 '| 1 | HC1 | HC | Setting up the heap | written 18 Nov 2026 | Opus 5.5 | off | `courses/home-composting/HC1-setting-up.md` |\n'
                 '| 2 | HC2 | HC | Keeping it working | written 19 Nov 2026 | Opus 5.5 | off | `courses/home-composting/HC2-keeping-it-working.md` |\n')
for f in sorted(C.glob('HC*.md')):
    print(f.name, len(f.read_text().split('---', 2)[2].split()), 'words')
