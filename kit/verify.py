"""Browser checks for academy/, the Academy site (run after build.py).

python3 verify.py [--edition NAME] [--full] [--shots DIR] [--page ID ...]
python3 verify.py [--edition NAME] --layout-shots DIR   (S-NAV2 step E: only the shot layouts, no check, nothing recorded)
S-DEC4 (20 Nov 2026), verify by scope (kit/verify_scope.py): the default run checks only the pages whose sources changed
since the edition's last passed run, recorded in kit/verify-hashes.json, plus the home, What's new, the Changelog and
the Backlog, and runs every edition-wide check (files and the shell, figure keys, opening notes, figure rules, the
split, navigation and the tablet and desktop layouts, the home at every width with and without motion, the navigation (check_nav),
private terms, index_check, the rot check). A page's sources are its built section and fetched file and the course files
the checks hold it against (verify_scope.py says which). A change to kit/*.py, kit/shell.js, kit/shell.css,
design/theme.css, kit/fonts/, catalog.toml or the edition's or its brand's file runs everything, as do a first run with
no record and --full. The first line says which mode and why; the record is written only after ALL CHECKS PASSED.
S-DEC4 (20 Nov 2026): the courses named below are Academy's; the checks name none and read the edition's own courses
(see LEAD, SECOND, MDNAV, SAMPLE and PRIVATE after SITE). A check needing a property the edition's courses lack (a
history course with Greece's structure, a second history course, a markdown course) prints what it leaves out and why;
an edition without a history course runs the split on a markdown course (check_split_md). What's new's 10 to 25 levels
hold for every edition whose largest day is 10 words or more (P-DEC15): the build draws an edition whose largest day is under 10 x NEW_INTERVAL words at its
own scale (build.py new_interval, a tenth of that day), checked against that scale, and the run says so. Private terms: the
default edition's public courses; another edition's own files, but for the folders of its courses marked `private`
(P-DEC13; an edition of private courses only is not checked; a `dated_lists` course's pages as in academy, P-DEC10).
The site is a shell plus one file per report (docs/academy.md A2), since P20 one file per syllabus and per Brand + AI
briefs and bibliography page, and since P22 one file per history course home, so it is served over local HTTP from
academy/, as the artifact and Pages serve it, and every pass that measures a fetched panel first navigates to it
through the shell and waits for the fetch. The split itself is checked: every report, syllabus, briefs, bibliography
and history course home panel is an empty stub whose data-src file exists, no file in academy/ is left unreferenced,
a report is fetched once and kept, a section link into an unopened report, syllabus, briefs page or course home
(a unit card) loads it, a failed fetch shows the retry state (a report and a course home, whose continue button and
unit cards arrive with the fetch), the shell is under 1 MB and the size table in README.md matches the files.
Three widths (design/theme.css section 6): phone 390x844, tablet 768x1024, desktop 1280x800 (the 'desktop' pass; since theme
6.22 the tablet landscape layout), and since S-NAV2 step D a desktop at 1920x1080 for the panel checks. On every panel of every
width, with every <details> opened: no horizontal scroll, no boxed elements closer than 6 px, no interactive target
under 44 px tall (inline links in running text exempt), no console error. Phone: the drawer in each context and the
navigation context (drawer, title, arrows, continue) across home -> Rome -> report -> home -> Greece -> report ->
a Brand + AI course and its reading and build pages, every course's "How it was built" page (A4: fetched through the
shell, one row per written report or unit), the drawer groups (a course's units as an accordion) and the Backlog page; the same panel checks again in the light theme. The Backlog and Changelog pages
(S-PAGES, 15 Nov 2026; check_site_log): rendered from docs/site-log.md alone, every entry in its area and order, newest
first on the Changelog, in plain words with no private term, at 320, 390 and 1280 px, dark and light, without sideways scroll. Tablet: the drawer is still a drawer (off screen until the menu button, 360 px, backdrop).
Desktop pass at 1280 x 800: the drawer is a persistent 240 px sidebar (300 px before theme 6.22; no backdrop, no menu
button, current item highlighted, scrolls on its own) and the top bar spans the content column. Figures (P44): at phone width every figure draws at its natural size
and its frame scrolls to the whole drawing; the cue line shows exactly on the frames that overflow (phone and desktop). With --shots, saves dark and light screenshots (the top 2,600 px, captured from a viewport that tall, P35; the home whole, P90; P92: and the hero's motion sheets, five moments of the area line and the drift, at 390 and 1280 px) at the three widths
of home, What's new (P91; the home and What's new at 320, 360 and 430 px too), Rome and one Rome report, plus every panel id given with --page (a new unit's reading page, a new course home),
and (P41) each figure in a --page panel on its own: <width>-<panel>-fig-<nn>-<kind>-<theme>.png, the figure as its frame
opens; and (P89, p85_frames.py folded in) every frame a reader scrolls that figure across, stacked and numbered in one
sheet: <width>-<panel>-fig-<nn>-<kind>-frames-<theme>.png, at each width, dark and light.
Matrix figures at 320 px (C1, 15 Nov 2026): every matrix that scrolls a 320 px frame keeps a label column in view, at
most 45% of the frame, sticky at its edge and as tall as the drawing (check_matrix_320).
Compare figures on a phone (P97, 12 Nov 2026): every compare figure at 320 and 390 px opens with its longest bar and
its value whole in the frame (its phone drawing, svg.viz-alt).
Figure geometry (FIG_JS; V1, every kind since P55): on the examples page (one figure per kind, then one hard case per
drawing fault P55 fixed, and the blocks that must stop the build) and, in the phone pass, on every panel with figures:
nothing outside the drawing, text inside its box or bar, no two boxes or labels overlapping, no free label over a box.
Links into an unopened panel on a fresh load are measured once the anchor has settled, with one retry (P56).
Reading layout (P68): every unit and report opens on its scope, then the bar and the text, with nothing about how it
was made before the text; each reads one section at a time, every section reached by next, previous and the menu, with
"Section n of N" and the progress bar right at each step; "Whole unit" shows them all; Sources and "How this unit was
made" are closed accordions after the text, and Sources opens from its links; on one page of each course a deep link
to a section and to Sources lands on a fresh load, and Continue and a reload resume at the section last read. The
panel checks measure each reading page whole.
Opening trees (P79): every tree wider than its 358-unit phone frame opens (at data-x0 or data-xr, as shell.js does)
with its root box whole and a box of a lower level in view.
Centred drawings (P50): every sitemap, objects, decision, states and wireflow figure whose drawing starts more than 12 units
in carries data-x0 where it starts, so a phone frame opens on it.
Figure keys (P52): every viz block in the vault, every history figure declaration, every course home figure and every
examples block uses only the keys viz.VIZ_KEYS documents for its kind, and viz.render leaves the block it draws unchanged.
Opening notes (P73): a markdown unit's text before its first heading is a closed accordion after Sources, "The writer's
opening note", on every unit that has one and on none that has not; section 1 opens on its heading; a deep link lands.
Home (P92, 4 Nov 2026; P91's shelf, P90's map and Continue gone), at 320, 360, 390, 430, 768, 1024, 1280 and 1920 px, dark and
light, with reduced motion emulated, and once more at every width with motion allowed: the hero holds the contour
layer and the copy, nothing else: the headline "Academy"; the area line, the areas in courses.py's order, each in
its tone, aria-hidden, no link or focus stop in it; the static line naming them all in their tones, for a screen
reader, and the line shown under reduced motion (with motion allowed the cycling line shows and the static line is for
a screen reader only); the lede; the quiet link "What's new · <code> · <day>" naming the newest dated unit, to #new, at
least 44 px tall, outlined, not filled. The contour layer: aria-hidden, no text, at most HOME_TOPO_MAX (24,148 B from
S-NAV1 step G; 20 KB before), one layout shown (tall
below 900 px, wide from it; 1100 px before theme 6.22), running the full width beside the sidebar while the copy keeps the column; in each layout
one rise per area, its words the area's words as the sources give them (home_expect: a history unit's reports counted
from the vault, a markdown unit from its reading page), standing in the order of its words, in the area's tone. On a
phone the hero is 60 to 80% of the screen and the first area's heading starts inside it; no live totals, no shelf, no
Continue, no map, no eyebrow; the area headers from 768 px the label, the name, the lede and the count, below it the
name only; every tile the chip row with its pill, the title, a tile line of at most two lines, three stats and its own
contour patch (aria-hidden, 4:1, inside the tile; one rise per written unit with its words as the sources give them,
each planned unit marked planned), the whole tile the link and no other link in it; one tile style (P93: History's
planned courses are ghost tiles, checked with every tile by check_tiles); one column below
768 px, two from 768 (three once the width beside the sidebar reaches 960 px, theme 6.22), a track's only tile half the width; History's two folded blocks; the order hero, the area
sections, the constants, the site links (Backlog, Figure kinds, Changelog), New since (What's new's first six rows, its
heading naming its oldest day) and one link to #new, last; no sideways scroll. Every text of the hero is measured
against the pixels under it (the contour lines and the page, shot with the texts made transparent): 4.5:1, 3:1 for
large text. With motion allowed the hero's texts are measured at the five poses of the move (P93; P92's drift, at both
ends and the middle, is gone) with each area word shown in turn. With
reduced motion no animation runs on the home; with motion allowed only transform and opacity animate
(document.getAnimations(), each effect's keyframes), the area words (each harea and harea-y since S-NAV2 step A), the shown contour layout and (P93) every shown
tile's patch.
At 390 px with motion allowed the fresh load's LCP and longest task are printed. On the desktop a history tile, a
markdown tile, the IA tile and the What's new link are clicked and each lands on its page. What's new (P91), at the
same widths: every dated unit and every course start once, newest first, as home_expect orders them, grouped by day
under its heading, each row linking to a page that exists, the approximate dates (provenance.json's written_approx)
marked and no other; its breadcrumbs and title. The drawer on the home: the main nav alone (S-NAV1 step C).
Contrast (P90): in the light theme, every text in the home, What's new (P91), the drawer, the changelog and backlog, each course
home and one reading page of each course, at phone width with every <details> open, reaches 4.5:1 against the
background it sits on (3:1 for large text), the text's opacity and every tint it sits on composited, and no text
and no background under it is pure white; figures are left to the figure checks.
Area pages (S-NAV1 step B, 21 Nov 2026): in an edition of two or more tracks the home's tiles are one per track (the
chip, the status pill, the name, its lede, three stats, its patch: one rise per course of the track, a live course by its
words, a course coming soon or planned flat), each the link to its area page track-<id>; each area page (check_area,
in every run) holds a hero over its courses' topography (check_topo against the sources: the same rises), the
breadcrumbs Home › Area, the eyebrow AREA, the name, the lede and three stats, then the track's band: its live courses'
tiles in catalog order, its own copy and its folded planned list (check_tiles, its ghosts its own planned courses); the
home's tile counts what the band holds; the area pages join the topography, motion, contrast and shot passes; the
navigation walk and the desktop taps reach a course through its area page; the history walk is home -> area -> course
-> unit with three backs. In an edition of one track (greece) none of this applies and the home lists the courses.
Navigation (S-NAV1 step C, 21 Nov 2026; check_nav, at 390 px dark and light and at 1024 x 768, 1280 x 800 and 1920 x 1080): two levels, each one
element in the drawer's list, nav.main-nav before nav.sub-nav, once in the page and in no panel. The main nav is Home and
the areas in catalog order (an edition of one track: Home and its area, whose entry opens the home at the track's band,
#track-<id>, as it has no area page) and marks where the reader is: Home on the home and the site pages under it (What's
new, the Changelog, the Backlog, Figure kinds), an area on its page (aria-current page) and on every page of its courses
(aria-current true). The sub-nav shows the reader's section alone: none on the home and its site pages, an area's
courses (history, then markdown, as courses.py lists them) on its page, a course's group (its home first, the page
itself marked) on its home, syllabus and first reading page. What's new, the Changelog and the Backlog are links at the
home's foot, after its courses, and in neither nav. Below 1100 px the menu opens the drawer with both navs on screen, the
focus on its close button and the current item scrolled into its list; Escape closes it and gives the focus back; an area
entry tapped in it closes it, opens the area and a back returns; from 1100 px under 860 px tall both navs stand in the
sidebar; on a desktop (1100 px and 860 px tall or more) the main nav stands in the top bar and the sub-nav in the sidebar. No console
error. The drawer box checks run on the home, every area page and every course; the light contrast check measures every
group of the sub-nav at once.
Topographies and tiles (P93, 4 Nov 2026), at 320, 360, 390, 430, 768, 1024, 1280 and 1920 px, dark and light: each course home and
What's new carries a contour layer behind its hero (check_topo), against the sources (home_expect: a course home one
rise per unit of the course in its order, a written unit by its words, a planned unit flat; What's new one rise per
day it lists, oldest first, its words the units' and reports' filed that day, the largest day 10 to 25 levels high),
aria-hidden, textless, at most 20 KB, one layout shown, each written rise closing min(2, its levels) rings of its own,
each rise's own rings inside the frame and above its fade, the frame covered by the turned layout; every tile patch
4:1 with its lines inside its frame; no topography on the Changelog, the Backlog, the Figure kinds page or a reading
page. Every tile on every page (check_tiles) has the same classes and fields (the chip of two parts, the status pill,
the title, a line of at most two lines while closed and whole when opened, three stats, its own patch; a planned
course's ghost no stats and one dashed ring), a history unit's tile opens to its module rows with its modules, words
and hours from the vault, a markdown unit's links to its reading page (its brief while it is not written) with its
sections and words from that page, each section's own text counted; one column below 768 px, two from it (three once the
width beside the sidebar reaches 960 px), a lone tile half the width; nothing past an edge, no sideways scroll. With motion allowed (at 1024 and 1920 px the home alone), on every one of these pages and the
home, every running animation animates only transform or opacity, every line of every shown contour drawing swells
(S-NAV1 step D: topo-swell, each line from 1 to 1 + --d x --topo-grow about its rise's core over --topo-breath, read
from shell.css; topo-turn and the whole-layer topo-breathe are gone), each drawing at its own point of the cycle, and at
five poses of the swell (at rest, its quarters, its middle and its top; on the home with each area word shown in turn)
every layer covers its frame, every rise and patch stays inside it and every text over
a topography keeps 4.5:1 (3:1 large) against the pixels under it; under reduced motion no animation runs on any of
them. At 390 px with motion allowed, LCP and the longest task are printed for the home, Greece's home and What's new.
With --shots: the home, What's new and the five course homes at the six widths, and the motion sheets of the home,
Greece and Information architecture at the five poses, 390 and 1280 px.
Section separators (P94, 8 Nov 2026), on every reading page at 320, 390, 768 and 1280 px, dark and light, under reduced
motion and with motion allowed (check_seps): every section with a top-level paragraph ends on one separator, last before
its next and previous, and a section without one has none; its rises, one per paragraph in order, carry the words read
from the page (the cue shell.js puts under a wide figure left out); div.topo.topo-patch.topo-sep, aria-hidden, textless,
at most 6 KB, its lines in the page's tone, its frame 1200:170 and the column's width, 20 px clear at least of the text
above and of the next and previous below (in "Whole unit", of the next section); with motion allowed a swell on each of
its lines (S-NAV1 step D), transform only, each separator at its own phase, and at five poses of the swell every
line inside its frame; none moving under reduced motion; no page wider than the screen. The other topography checks
leave the separators to this one.
Object reliefs (P95, 8 Nov 2026; check_reliefs): the outline library (design/outlines/outlines.json) holds at least ten
outlines for each of the five courses, each with every field, an allowed licence named in its credit, its SVG and its
relief JSON, and a text of each course it serves naming it; every reading page maps a relief exactly when uses.json
maps it one; and each mapped page at 320, 390, 768 and 1280 px, dark and light, with and without motion: the relief under
the scope line as the header's last block, before the section bar; its caption printed exactly (what it shows, "a
stylised outline drawn as a relief from an icon", the credit) with the licence linked to its text; div.topo.relief
aria-hidden and textless, one svg.topo-l with only paths, the halo's path.rl-out and the others without a class (step
G; path.rl-in before), at most viz.REL_MAX bytes (17,821 from S-NAV1 step G; 12 KB before), in the page's
tone, the halo fainter; its frame at the drawing's aspect, the column's width or 280 px tall (340 from 768 px); a swell
on each of its lines (S-NAV1 step D; the paths in groups of one origin, --o, each level's --d) by transform only, at a
phase none of the page's separators has, and at five poses of the swell every line inside its frame; nothing moving
under reduced motion; the page's text naming the object; no page wider than the screen.
The swell (S-NAV1 step D, 22 Nov 2026; check_swell): on the home, an area page, a course home, What's new and a reading
page with a relief and separators, at 320, 390, 768 and 1280 px, dark and light: with motion allowed only transform and
opacity animate, and only the area words and the contour lines; every line of every shown drawing swells, one phase a
drawing; every --d is 0 to 1 (a relief's outer halo 1, a contour drawing's outermost line above 0, an innermost line 0), a rise's own lines move about
its core; at the five poses no join between two lines' stretches opens more than 0.5 px, every patch's, separator's and
relief's lines stay inside the frame, every fitted hero's rises' own rings inside its frame and above its fade (from
390 px); at the top of the swell an innermost line is unmoved and every other at 1 + d x --topo-grow; under reduced
motion no animation runs at all; every relief outline of the library moves (--d > 0; S-NAV1 step G).
Out of view (S-NAV1 step G; check_pause): at 390 px with motion, on the home and a course home (top and foot), back
home through history, at the top level and in a sandboxed iframe: every drawing in view runs and moves, every one out of
view is .off (shell.js's IntersectionObserver), its swells paused and still, every drawing of a hidden panel .off;
under reduced motion no swell exists. The byte and class checks read a drawing without the runtime .off.
The area line's cycle (S-NAV2 step A, Fix 1; check_harea): at every viewport of the home's motion pass (320, 360, 430,
390, 768 and 1280 px, and since step D 1024 and 1920 px), the real line (--n on p.harea the number of its words, the tracks) and a probe copy of it with
3, 4 and 8 words, sampled every 50 ms over two cycles: each word runs harea and harea-y over n x 3 s; at every sample at
most one word above opacity .5 (exactly one but at a cross-fade's middle), never three drawn, two drawn together for
at most the .36 s cross-fade plus a sample, each word shown three seconds a cycle in turn, at rest while fully shown.
PHONE_EXPECTED lists the phone's expected differences from S-NAV2's start (the theme CSS and this line).
The history readout (S-NAV2 step B, Fix 2; check_debug): without ?debug no element, listener or storage key of it
exists and the body is the built shell's; with ?debug at 390 px the panel shows inside the screen, the walk home ->
area -> course -> unit is the same as without it, the log names each go() (pushState, length rising by one) and the
popstate of a history.back(); with pushState refused it names the replaceState fallback on each level; in a sandboxed
iframe it says so; at 1280 x 800 the panel sits inside the screen.
The tablet and desktop layouts (S-NAV2 step D, theme 6.22; check_layouts, check_frames, check_phone_identity,
check_webkit): at 390 x 844, 800 x 1100, 1024 x 768, 1280 x 800, 1440 x 900 and 1920 x 1080, on the home, What's new, the
Changelog, an area page, two course homes and the first reading page of every course, the sidebar, the top bar and the
outline where the spec puts them and nowhere else (a desktop, 1100 px and 860 px tall or more: the top bar across the
screen with the main nav in it, the sidebar only where there is a sub-nav, the outline at a reading page's right; from
1100 px under 860 px tall the 240 px sidebar with both navs, no outline; below 1100 px the drawer), no sideways scroll,
no heading, figure or table past the column, under the sidebar or the outline, cut or clipped; the home's first tiles'
titles and stats above the fold at 1024 x 768 and 1280 x 800; the hero bound (P-HK1) at 1024, 1280 and 1920 px. The 4x
CPU throttle frame test of S-NAV1's fresh check at 1280 x 800 (the median frame and the longest task, check_frames).
The desktop top bar (S-NAV2 step E, check_topbar): at 1100, 1120, 1140, 1280 and 1440 x 900 and 1920 x 1080, dark and
light, on the home and an area page, with the edition's areas and a probe copy of the bar holding eight: the main nav
does not scroll, no item of it is cut or past its edge, and it ends left of the theme and arrow buttons.
The shot layouts (S-NAV2 step E, layout_shots): --shots DIR, and --layout-shots DIR alone, write the first screen of
the home, an area page, a course home and a unit page at 1440 x 900 (desktop), 1280 x 800 (tablet-landscape) and
800 x 1100 (tablet-portrait), dark and light, as <page>-<layout>-<theme>.png.
The phone byte identity: at 320, 360 and 390 px, under reduced motion, the current shell laid out and drawn exactly as
with the start build's theme (PHONE_REF) in its <style>, every element's box and computed style and the screenshot;
PHONE_EXPECTED lists what is expected to differ. WebKit (P-NAV3): check_history and check_pause again in Playwright's
WebKit, or one line saying it is not installed. The home, What's new, topography, tile, area and navigation passes run
at 1024 x 768 and 1920 x 1080 as well, and the panel checks at 1920 x 1080. A subset runs from a script that imports
this file and calls the checks (each takes the browser and the fails list): out/S-NAV2/step-D-probe.py runs step D's
checks alone (--only names them, --edition as here), step-D-probe2.py the home, topography, tile and area passes at given viewports.
Last, index_check.py: docs/courses-index.md against the syllabi, provenance, the vault and the data files (A5).
Then rot_check.py (P30-F11, P30-F16): kit/shell.css is design/theme.css, no live instruction names a retired thing, and
every staleness date past or due within 30 days is printed as a warning.
"""
import sys, json, pathlib, re, threading, functools, math, html as H
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from playwright.sync_api import sync_playwright
import pack   # S-DEC2: a markdown course's data (its pack)
import index_check   # (P39: the browser gets the theme fonts from fonts/, never the network)
import private_terms   # G-0: the public courses carry no private term
import rot_check   # P30-F11, P30-F16: the theme copy, retired instructions, staleness dates due
from courses import COURSES, THEMES, EDITIONS, DEFAULT_EDITION, LOG_AREAS, brand, path as cpath, provenance, sub_pages as _sub_pages
ALL_COURSES = list(COURSES)   # S-DEC4: every course of the repo, before the edition's filter below (the relief library serves them all)
# P70: --edition checks an edition's folder the same way, over the courses and pages it holds (default: the full site,
# the first edition in catalog.toml `edition_order`)
EDITION = sys.argv[sys.argv.index('--edition') + 1] if '--edition' in sys.argv else DEFAULT_EDITION
if EDITION not in EDITIONS:
    raise SystemExit(f'no edition {EDITION!r} in courses.py EDITIONS: {", ".join(EDITIONS)}')
ED = EDITIONS[EDITION]
# S-DEC3: the edition's brand (brands/<name>.toml): the site name the pages carry and the theme's localStorage key
SITE_NAME = brand(EDITION)['name']
THEME_KEY = brand(EDITION)['storage']['theme']
SITE_JSON = json.dumps(SITE_NAME)
OMIT = set(ED['omit'])
if ED['courses'] is not None:
    COURSES = [c for c in COURSES if c['id'] in ED['courses']]
    _tracks = {c.get('theme') for c in COURSES} | {tr for c in COURSES for tr, _ in c.get('tracks', {}).values()}
    THEMES = [t for t in THEMES if t['id'] in _tracks]
HAS = {c['id'] for c in COURSES}
# the folded planned lists the topography/tile passes open: each track's own `planned_anchor` (catalog.toml; N1, DEC-A checker); an empty match list is a selector that finds nothing
PLANNED_SEL = ', '.join('#' + t['planned_anchor'] for t in THEMES if t.get('planned_anchor')) or '[data-none]'
FULL = ED['courses'] is None   # S-DEC4: the edition holds every course (academy)
import viz, viz_examples   # P55: the examples page's hard cases and the blocks that must stop the build
viz.set_metrics(brand(EDITION))   # P-DEC5: the brand's font metrics, as build.py draws with them
# each track and its course cards as the home must show them, from courses.py (A5: a new course needs no edit here)
# G-0 (12 Nov 2026): a markdown course with no unit filed is not live and has no tile on the home (home_expect says the
# same); a unit's file is named by its code, the course's key and a number (A9, DD-IA2, PB1)
def _live(c, k):
    v = pathlib.Path(__file__).resolve().parent.parent / c['vault']
    return any(v.glob(f'{k}[0-9]*.md')) or any(v.glob(f'DD-{k}[0-9]*.md'))
HOME_TRACKS = [t['name'] + ':' + ','.join(
    ['#' + c['home_id'] for c in COURSES if c['family'] == 'history' and c['theme'] == t['id']]
    + ['#' + f"{c.get('prefix', c['id'])}-{k.lower()}" for c in COURSES if c['family'] == 'markdown'
       for k, (tr, _) in c['tracks'].items() if tr == t['id'] and _live(c, k)]) for t in THEMES]

R = pathlib.Path(__file__).resolve().parent
SITE = R / ED['site']
SHELL_MAX = 1024 * 1024   # A2: the shell stays under 1 MB

# S-DEC4 (20 Nov 2026): no course is named in this file. The checks that open a given course's pages read them from the
# edition's own courses (courses/<id>/course.toml): its family, prefix, home and syllabus ids, number, short name and
# label, its tracks (a markdown course's sub-courses), `unit_key`, and three keys kept for the checks: `private` (a
# course of the owner's own, not public: its pages are left out of an edition's private-terms check, P-DEC13),
# `reliefs` (its pages draw object reliefs from design/outlines; was REL_COURSES) and `verify_sample` (its homes are the
# ones the per-page passes sample: topography, motion, shots; an edition holding none samples every course; a full run
# checks every course's drawer, P-DEC14).
# A check that needs a property the edition's courses lack prints what it leaves out and why.
def sub_pages(c):
    """A course's home pages: a history course's one home; a markdown course's one per sub-course (its tracks key),
    <prefix or id>-<key> (build.py md_courses)."""
    return _sub_pages(c)
def rid(c, mod):
    """A history course's report id for a module code ('2.3' -> m23 in a course with prefix m)."""
    return c['prefix'] + mod.replace('.', '')
SHELL_IDS = set(re.findall(r'<section class="panel[^"]*" id="([^"]+)"', (SITE / 'index.html').read_text())) if (SITE / 'index.html').exists() else set()
HIST = [c for c in COURSES if c['family'] == 'history']
# the split, navigation and desktop checks open reports 2.3 to 2.5 (one unit's run of three), 5.2 and 5.5 of a history
# course (Greece's structure): LEAD, the first history course of the edition holding them; SECOND, another history
# course with a report 1.2, whose home stays unopened until the split check's failed-fetch test
SPLIT_MODS = ('2.3', '2.4', '2.5', '5.2', '5.5')
LEAD = next((c for c in HIST if all(rid(c, m) in SHELL_IDS for m in SPLIT_MODS)), None)
SECOND = next((c for c in HIST if c is not LEAD and rid(c, '1.2') in SHELL_IDS), None) if LEAD else None
# the markdown navigation block runs on the edition's first markdown course with a unit filed, each of its live
# sub-courses: (page id, short name, key, briefs page id, brief anchor prefix), as build.py md_courses names them
MDNAV = next((c for c in COURSES if c['family'] == 'markdown' and any(_live(c, k) for k in c.get('tracks', {}))), None)
MDSUBS = [(f"{MDNAV.get('prefix', MDNAV['id'])}-{k.lower()}", short, k,
           f'briefs-{k.lower()}' if MDNAV.get('legacy_ids') else f"{MDNAV.get('prefix', MDNAV['id'])}-{k.lower()}-briefs",
           'b-' if MDNAV.get('legacy_ids') else f"{MDNAV.get('prefix', MDNAV['id'])}-{k.lower()}-b-")
          for k, (tr, short) in MDNAV['tracks'].items() if _live(MDNAV, k)] if MDNAV else []
_samp = [c for c in COURSES if c.get('verify_sample')] or COURSES
SAMPLE = [p for c in _samp for p in sub_pages(c)]   # the course homes the per-page passes visit, in course order
PRIVATE = [c['id'] for c in COURSES if c.get('private')]
HIST_HOMES = {c['home_id'] for c in HIST}
# S-NAV1 step B (21 Nov 2026): an edition of two or more tracks has an area page per track, track-<id> (build.py
# area pages), between the home and its courses: the home shows one tile per track, each area page its courses' tiles,
# its own copy and its planned courses. An edition of one track has none and its home lists the track's courses, as
# before. AREA_OF: each course page (a history course's home, a markdown sub-course's) to its track.
AREA_IDS = ['track-' + t['id'] for t in THEMES] if len(THEMES) > 1 else []
MULTI = bool(AREA_IDS)
AREA_OF = {c['home_id']: c['theme'] for c in HIST} | {f"{c.get('prefix', c['id'])}-{k.lower()}": tr for c in COURSES if c['family'] == 'markdown' for k, (tr, _) in c['tracks'].items()}
HOME_GRID = '#home > .cgrid.areas' if MULTI else '#home .track .cgrid'   # the home's tile grid the tablet and desktop passes measure
# S-DEC4 (20 Nov 2026): verify by scope (verify_scope.py). The default run checks the pages whose sources changed since
# the edition's last passed run (kit/verify-hashes.json) plus the home, What's new, the Changelog and the Backlog, and
# runs every edition-wide check; a change to kit/*.py, shell.js, shell.css, theme.css, the fonts, catalog.toml or the
# edition's or brand's file, a first run and --full check everything. Its first line says which and why. The per-page
# passes below take their pages through SCOPE.only(); the record is written only after ALL CHECKS PASSED.
import verify_scope
SCOPE = verify_scope.Scope(SITE, EDITION, ED['brand'], COURSES, sub_pages, full='--full' in sys.argv)
print(SCOPE.mode, flush=True)
class Quiet(SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
class Server(ThreadingHTTPServer):
    def handle_error(self, request, client_address):   # a fetch the browser dropped on navigating away is not a fault
        if not isinstance(sys.exc_info()[1], (BrokenPipeError, ConnectionResetError)): super().handle_error(request, client_address)
SERVER = Server(('127.0.0.1', 0), functools.partial(Quiet, directory=str(SITE)))
threading.Thread(target=SERVER.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{SERVER.server_port}/index.html'
# the visible panel holds its content: a panel in the shell at once, a report once its fetch has landed (or failed)
READY_JS = """() => { if (document.fonts.status !== 'loaded') return false; const p = [...document.querySelectorAll('.panel')].find(p => !p.hidden);
  return !!p && (!p.hasAttribute('data-src') || p.hasAttribute('data-loaded') || p.hasAttribute('data-failed')); }"""
def ready(pg):
    pg.wait_for_function(READY_JS, timeout=15000)
SHOTS = pathlib.Path(sys.argv[sys.argv.index('--shots') + 1]) if '--shots' in sys.argv else None
PAGES = [a for i, a in enumerate(sys.argv) if i > 0 and sys.argv[i - 1] == '--page']   # extra panels to screenshot
GAP = 6
VX_KINDS = 16  # the examples page carries one figure per kind: four from A8, seven for the IA course (V1), four data kinds
               # and the numeric matrix (P44)
VX_FIGS = VX_KINDS + len(viz_examples.CASES)   # then one hard case per drawing fault P55 fixed
VIEWPORTS = [('phone', 390, 844, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]
HOME_WIDTHS = [('phone320', 320, 640, True), ('phone360', 360, 780, True), ('phone430', 430, 932, True)]   # P91: the home only
# P91: where a tapped link landed (P92: a tile, the What's new link): [visible panel, its target inside it, the target's top, a <details> target open, the viewport height]
LAND_JS = '''(t) => { const v = [...document.querySelectorAll('.panel')].find(p => !p.hidden), e = document.getElementById(t);
  return [v && v.id, !!e && !!v && v.contains(e), e ? Math.round(e.getBoundingClientRect().top) : null, e && e.tagName === 'DETAILS' ? e.open : null, innerHeight]; }'''
SIDE = 240  # the sidebar's width at 1280 x 800, the desktop pass's viewport (theme.css --side; S-NAV2 step C: 240 px in the tablet landscape
            # layout, 1100 px or wider and under 860 px tall; 300 px before; on a desktop 860 px tall or more clamp(240px, 18vw, 300px))

BOX_JS = r'''([scope, gap]) => {
  const root = document.querySelector(scope);
  const els = [];
  root.querySelectorAll('*').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || cs.display === 'inline') return;  // inline code in running text is not a box
    const r = el.getBoundingClientRect(); if (r.width < 2 || r.height < 2) return;
    const b = ['Top','Bottom','Left','Right'].every(s => parseFloat(cs['border'+s+'Width']) > 0 && cs['border'+s+'Style'] !== 'none');
    const bg = cs.backgroundColor, hasBg = bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent';
    if (b || (hasBg && parseFloat(cs.borderTopLeftRadius) > 0)) els.push([el, r]);
  });
  const bad = []; let min = 1e9;
  for (let i = 0; i < els.length; i++) for (let j = i + 1; j < els.length; j++) {
    const [a, ra] = els[i], [b, rb] = els[j];
    if (a.contains(b) || b.contains(a)) continue;
    const hov = Math.min(ra.right, rb.right) - Math.max(ra.left, rb.left);
    if (hov <= 1) continue;
    let g;
    if (ra.bottom <= rb.top + 0.5) g = rb.top - ra.bottom; else if (rb.bottom <= ra.top + 0.5) g = ra.top - rb.bottom; else g = -1;
    if (g < min) min = g;
    if (g < gap - 0.1) {
      const d = e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).join('.') : '') + (e.id ? '#' + e.id : '');
      bad.push(`${d(a)} | ${d(b)} gap ${g.toFixed(1)}`);
    }
  }
  return {n: els.length, min: Math.round(min * 10) / 10, bad: bad.slice(0, 12), nbad: bad.length};
}'''

# interactive targets under 44 px tall or 24 px wide, in the visible panel and in the drawer when it is on screen;
# inline links inside running text are exempt (WCAG 2.5.8 inline exception)
TARGET_JS = r'''(scope) => {
  const small = [];
  const dr = document.getElementById('drawer'), dOn = dr && dr.getBoundingClientRect().left >= 0;
  const roots = [document.querySelector(scope)]; if (dOn) roots.push(dr);
  roots.forEach(root => { if (!root) return; root.querySelectorAll('a[href],button,summary,input,select,[role=button]').forEach(el => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden') return;
    const r = el.getBoundingClientRect(); if (r.width === 0 && r.height === 0) return;
    if (el.tagName === 'A' && cs.display === 'inline') return;
    if (el.closest('.dunit.closed .ditems')) return;
    if (r.height < 43.5 || r.width < 24) small.push((el.tagName + '.' + el.className + ' "' + (el.textContent || '').trim().slice(0, 24) + '"').slice(0, 80) + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
  }); });
  return [...new Set(small)].slice(0, 15);
}'''

# P44: at phone width every figure draws at its natural size (one SVG unit to one CSS pixel) inside its .viz-scroll
# frame; the frame's scroll reaches the whole drawing (scrolled to the end, the drawing's right edge is inside the frame);
# the cue line under the frame shows exactly when the drawing is wider than the frame, and such a frame starts faded on
# the right (data-more="r"). At desktop width (figures scale to the column) the cue and the fade show only on a figure
# wider than its frame and on no other. Runs on the visible panel after its <details> are opened (two frames for shell.js to mark).
FRAME_JS = r'''async ([scope, phone]) => {
  await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
  const bad = []; let n = 0, over = 0;
  document.querySelectorAll(scope + ' .viz-scroll').forEach(f => {
    const svg = [...f.querySelectorAll(':scope > svg')].find(s => s.getBoundingClientRect().width > 0); if (!svg || f.clientWidth === 0) return; n++;   // P83: the drawing shown at this width
    const fig = f.closest('figure'), kind = [...fig.classList].find(c => c.startsWith('viz-') && c !== 'viz-wide');
    const nat = svg.viewBox.baseVal.width, w = svg.getBoundingClientRect().width;
    if (phone && Math.abs(w - nat) > 0.6) bad.push(`${kind}: drawn ${w.toFixed(1)} px wide, natural ${nat}`);
    f.scrollLeft = f.scrollWidth;
    const fr = f.getBoundingClientRect(), sr = svg.getBoundingClientRect();
    if (sr.right > fr.right + 1 || f.scrollWidth < Math.floor(w) - 1) bad.push(`${kind}: scroll ${f.scrollWidth} px does not reach the drawing (${w.toFixed(0)} px)`);
    f.scrollLeft = 0; f.dispatchEvent(new Event('scroll'));
    const o = w > f.clientWidth + 1, cue = f.nextElementSibling;
    const shown = !!cue && cue.classList.contains('viz-cue') && !cue.hidden && cue.offsetHeight > 0;
    if (o) over++;
    if (o !== shown) bad.push(`${kind}: drawing ${w.toFixed(0)} px in a ${f.clientWidth} px frame, cue ${shown ? 'shown' : 'not shown'}`);
    if (o && f.getAttribute('data-more') !== 'r') bad.push(`${kind}: an overflowing frame at its start is marked ${f.getAttribute('data-more')}, expected r`);
    if (!o && f.hasAttribute('data-more')) bad.push(`${kind}: a frame that fits is marked ${f.getAttribute('data-more')}`);
    // P83 (3 Nov 2026): on a phone a bars figure and a one- or two-a-row flow fit their frame; a matrix or compare wider than
    // its frame keeps its label column (.viz-stick) at the frame's left edge however far it is scrolled
    if (phone && o && (kind === 'viz-bars' || kind === 'viz-flow' && [...svg.querySelectorAll('rect.viz-node')].filter(r => +r.getAttribute('y') === 8).length <= 2))
      bad.push(`${kind}: ${w.toFixed(0)} px wide, so it scrolls a ${f.clientWidth} px phone frame (P83: it fits)`);
    const st = f.querySelector('.viz-stick');
    if (phone && o && (kind === 'viz-matrix' || kind === 'viz-compare') && !st) bad.push(`${kind}: scrolls with no label column (.viz-stick) to keep in view (P83)`);
    if (phone && st && getComputedStyle(st).display !== 'none') {
      f.scrollLeft = f.scrollWidth; const sr2 = st.getBoundingClientRect(), fr2 = f.getBoundingClientRect(), ss = st.querySelector('svg');
      if (Math.abs(sr2.left - fr2.left) > 1) bad.push(`${kind}: the label column sits ${(sr2.left - fr2.left).toFixed(0)} px from the frame edge when scrolled to the end (P83: sticky)`);
      if (ss && Math.abs(ss.getBoundingClientRect().height - svg.getBoundingClientRect().height) > 1) bad.push(`${kind}: the label column is not as tall as the drawing`);
      f.scrollLeft = 0; f.dispatchEvent(new Event('scroll'));
    }
  });
  return {n, over, bad: bad.slice(0, 8)};
}'''

# P91 (4 Nov 2026); P92 (4 Nov 2026): what the home and What's new must show, read here from the sources, not from the
# build: each live course's units in order (a history course's syllabus units, the audit unit left out, written when
# every module is in its prompts index; a markdown course's units from its data file, written when its vault file is
# filed) with their words (a history unit's: its reports' words, each counted from its vault file as build.py counts
# a report, before the Self-test, figures left out; a markdown unit's: its reading page as published, from its first
# section to the end of its text), each area's words (its live courses' units), every dated unit (vault front matter
# `written`; provenance.json's `written` map for a history report, `written_approx` marking an approximate one) and
# each course's start (its first dated unit), newest first, ties on a day by build order.
FIGBLOCK = re.compile(r'<figure class="viz[ "].*?</figure>', re.S)
def _wc(frag):
    body = re.split(r'<h2>\s*Self-test', FIGBLOCK.sub(' ', frag))[0]
    return len(re.sub(r'<[^>]+>', ' ', body).split())
def home_expect():
    import importlib.util, vault
    prov = provenance()
    from howbuilt import front
    courses, dated, areas, area_pages = {}, [], [], {}
    for t in THEMES:
        aw = 0
        crs, lives, soon = [], [], []   # S-NAV1 step B: the track's courses for its area page and its home tile: [(short, words)], live markdown ones, markdown ones coming soon
        for c in COURSES:
            if c['family'] == 'history' and c['theme'] == t['id']:
                syl = cpath(c, 'syllabus').read_text()
                idx = json.load(open(cpath(c, 'prompts')))
                units = [(u, re.findall(r'data-id="([\d.]+)">', body)) for u, body in re.findall(r'<section class="unit" id="u(\d+)"[^>]*>(.*?)</section>', syl, re.S)]
                order = [m for _, ms in units for m in ms]
                def rw(m):
                    f = vault.report_html(c, m, draw=False)
                    f = re.sub(r'<(/?)(html|head|body|!doctype[^>]*)>', '', f, flags=re.I)
                    f = re.sub(r'<style.*?</style>|<script.*?</script>', '', f, flags=re.S | re.I)
                    return _wc(re.sub(r'\sstyle="[^"]*"', '', f))
                us, tiles = [], []
                for u, ms in units:
                    tiles.append((f'U{u}', [(m, rw(m) if m in idx else None) for m in ms]))   # P93: every unit's tile, the audit unit's too
                    if u == c['audit_unit']:
                        continue
                    done = all(m in idx for m in ms)
                    us.append((f'U{u}', sum(rw(m) for m in ms) if done else None))
                aw += sum(rw(m) for m in idx if m in order)
                crs.append((c['home_id'], c['short'], sum(rw(m) for m in idx if m in order) or None))
                courses[c['home_id']] = dict(short=c['short'], units=us, tiles=tiles, family='history', tone=c['color'])
                ap = set(prov.get('written_approx', {}).get(c['id'], []))
                for m, d in prov.get('written', {}).get(c['id'], {}).items():
                    if m in idx:
                        dated.append(dict(date=d, rank=order.index(m), home=c['home_id'], code=m, pid=c['prefix'] + m.replace('.', ''), approx=m in ap, course=c['short'], words=rw(m)))
        for c in COURSES:
            if c['family'] != 'markdown':
                continue
            d = pack.load(c)                                   # S-DEC2: the course's pack
            vlt = {}
            for f in (sorted((R.parent / c['vault']).glob('*.md')) if (R.parent / c['vault']).is_dir() else []):
                fm = front(f)
                if fm.get('code'): vlt[fm['code']] = fm
            rid = {r['covers'][0]: r['id'] for r in d.READINGS if 'md' not in r and r.get('covers')}
            order = [o[0] if isinstance(o, (tuple, list)) else o for o in getattr(d, 'ORDER', [])]
            for sc in d.COURSES:
                tr, short = c['tracks'][sc['key']]
                if tr != t['id']:
                    continue
                if not any(u[0] in vlt for u in sc['units']):
                    soon.append(short)
                    continue                                   # a course with nothing filed is not live: no tile
                pid = f'{c.get("prefix", c["id"])}-{sc["key"].lower()}'
                read = lambda code: rid.get(code, f'read-{c["id"]}-{code.lower()}')
                def secs(code):   # P93: each section's own text (not its next and previous buttons or its band's numeral)
                    page = (SITE / pid / f'{read(code)}.html')
                    page = page if page.exists() else next(SITE.glob(f'*/{read(code)}.html'))
                    body = page.read_text(encoding='utf-8').split('<div class="report steps">', 1)[1].split('<div class="process"', 1)[0]
                    parts = re.findall(r'<section class="sec" data-step="\d+">(.*?)</section>(?=<section class="sec"|</div>)', body, re.S)
                    return [_wc(re.sub(r'<span class="bn"[^>]*>.*?</span>', ' ', re.sub(r'<nav class="secnav".*?</nav>', ' ', x, flags=re.S), flags=re.S)) for x in parts]
                sw = {u[0]: secs(u[0]) for u in sc['units'] if u[0] in vlt}
                us = [(u[0], sum(sw[u[0]]) if u[0] in vlt else None) for u in sc['units']]
                aw += sum(w for _, w in us if w)
                lives.append((pid, short, sum(w for _, w in us if w) or None))
                courses[pid] = dict(short=short, units=us, tiles=[(u[0], sw.get(u[0])) for u in sc['units']], family='markdown', tone=sc['color'],
                                    pages={u[0]: read(u[0]) for u in sc['units'] if u[0] in vlt}, briefs={u[0]: (f'{pid}-b-' if not c.get('legacy_ids') else 'b-') + u[0].lower() for u in sc['units']})
                for k, u in enumerate(sc['units']):
                    if u[0] in vlt and vlt[u[0]].get('written'):
                        dated.append(dict(date=str(vlt[u[0]]['written']), rank=order.index(u[0]) if u[0] in order else len(order) + k, home=pid,
                                          code=u[0], pid=read(u[0]), approx=False, course=short, words=sum(sw[u[0]])))
        areas.append(dict(name=t['name'], color=t['color'], words=aw))
        plan = [] if 'planned' in OMIT else t.get('planned', [])
        area_pages['track-' + t['id']] = dict(name=t['name'], color=t['color'], lede=t['lede'], courses=[h for h, _, _ in crs + lives], plans=[x[1] for x in plan],
                                              rises=[(l, w) for _, l, w in crs + lives] + [(l, None) for l in soon] + [(x[0], None) for x in plan])
    dated.sort(key=lambda x: (x['date'], x['rank']), reverse=True)
    rows = [dict(x, kind='unit') for x in dated]
    for home in dict.fromkeys(x['home'] for x in dated):
        f = min((x for x in dated if x['home'] == home), key=lambda x: (x['date'], x['rank']))
        k = next(i for i, r in enumerate(rows) if r['kind'] == 'unit' and r['home'] == home and r['code'] == f['code'])
        rows.insert(k + 1, dict(f, kind='course', pid=home))   # below its first unit
    days, dom = {}, {}
    tone_of = {h: e['tone'] for h, e in courses.items()}
    for x in dated:
        days[x['date']] = days.get(x['date'], 0) + x['words']
        dom.setdefault(x['date'], {}); dom[x['date']][tone_of[x['home']]] = dom[x['date']].get(tone_of[x['home']], 0) + x['words']
    return dict(courses=courses, areas=areas, area_pages=area_pages if MULTI else {}, newest=dated[0] if dated else None, rows=rows, days=sorted(days.items()),
                day_tones=[max(dom[d], key=dom[d].get) for d in sorted(days)])

# P92 (4 Nov 2026): the home's layout, read on the visible home panel at one width. Returns what was found and the
# faults (bad); check_home compares the hero, the tiles and New since with home_expect().
HOME_JS = r'''([tones, opt]) => {   // P93: opt says what the edition holds (an edition may omit the planned courses and the site links)
  const h = document.getElementById('home'), bad = [], out = {bad};
  const phone = innerWidth < 768, desk = innerWidth >= 900, de = document.documentElement;   // S-NAV2 step D: the wide contour layout from 900 px since theme 6.22 (1100 before)
  const vis = e => !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().width > 0;
  const hero = h.querySelector(':scope > header.hero.hhome');
  if (!hero) { bad.push('no hero (header.hero.hhome)'); return out; }
  const resolves = t => !!document.getElementById(t) || [...document.querySelectorAll('.panel[data-anchors]')].some(p => (' ' + p.getAttribute('data-anchors') + ' ').includes(' ' + t + ' '));
  for (const [sel, what] of [['.hbtn.cont, .hbtn.start, [data-long]', 'a Continue button'], ['figure.viz', 'the map (a figure)'], ['.resume, .rmeter', 'the resume card'],
                             ['.tjump', 'the track tiles'], ['.totals, .htot, .htop', 'live totals'], ['.meter', 'a progress meter'], ['.cgo', 'a card button'],
                             ['.shelf, .spine, .shelf-lit', 'the shelf (P91)'], ['.eyebrow', 'an eyebrow line']])
    if (h.querySelector(sel)) bad.push(`the home still has ${what} (${sel})`);
  out.hero = [...hero.children].map(e => e.tagName.toLowerCase() + '.' + [...e.classList].join('.')).join(' ');
  if (out.hero !== 'div.topo div.hcopy') bad.push(`the hero holds ${out.hero}, expected the contour layer and the copy`);
  const copy = hero.querySelector(':scope > .hcopy');
  out.copy = copy ? [...copy.children].map(e => e.tagName.toLowerCase() + '.' + [...e.classList].join('.')).join(' ') : '';
  if (out.copy !== 'h1. p.harea p.harea-all p.lede a.hnew') bad.push(`the hero's copy runs ${out.copy}, expected the headline, the area line, the static line, the lede and the link`);
  const h1 = copy && copy.querySelector(':scope > h1'); if (!h1 || h1.textContent !== __SITE__) bad.push('the headline is not the site name ' + __SITE__);
  // the area line: the four names, in order, each in its tone, hidden from a screen reader; the static line for one
  const al = copy && copy.querySelector('.harea'), st = copy && copy.querySelector('.harea-all');
  const probe = document.createElement('span'); hero.appendChild(probe);
  const tone = v => { probe.style.color = v; return getComputedStyle(probe).color; };
  out.words = al ? [...al.querySelectorAll('.harea-w')].map(w => [w.textContent, getComputedStyle(w).color]) : [];
  out.tones = tones.map(tone); probe.remove();
  if (!al || al.getAttribute('aria-hidden') !== 'true') bad.push('the cycling area line is not hidden from a screen reader');
  if (al && [...al.querySelectorAll('a, button, [tabindex]')].length) bad.push('the area line holds a link or a focus stop');
  out.static = st ? (() => { const c = st.cloneNode(true); c.querySelectorAll('.hsr').forEach(x => x.remove()); return c.textContent; })() : null;   // as seen; the screen reader's commas left out
  out.staticSr = st ? [...st.querySelectorAll('.harea-dot')].map(d => [d.querySelector('[aria-hidden="true"]') ? 1 : 0, d.querySelector('.hsr') ? d.querySelector('.hsr').textContent : null]) : [];
  out.staticTones = st ? [...st.children].filter(e => !e.classList.contains('harea-dot')).map(e => getComputedStyle(e).color) : [];
  out.staticAria = st ? st.getAttribute('aria-hidden') : 'missing';
  out.lineShown = vis(al); out.staticShown = !!st && st.getBoundingClientRect().width > 2 && getComputedStyle(st).clipPath === 'none';
  const lede = copy && copy.querySelector('.lede'); out.lede = lede ? lede.textContent : null;
  // the quiet link: names the newest unit and its day, to #new, at least 44 px, outlined, not filled
  const ln = copy && copy.querySelector('a.hnew');
  if (ln) { const cs = getComputedStyle(ln), r = ln.getBoundingClientRect();
    const vt = e => { const c = e.cloneNode(true); c.querySelectorAll('.hsr').forEach(x => x.remove()); return c.textContent; };   // as seen
    out.linkSr = [...ln.querySelectorAll(':scope > span > [aria-hidden="true"]')].length === 2 && [...ln.querySelectorAll('.hsr')].length === 2;
    out.link = [vt(ln.querySelector('span')), ln.getAttribute('href'), ln.getAttribute('data-target'), Math.round(r.height), cs.backgroundColor, cs.borderTopStyle, parseFloat(cs.borderTopWidth)];
    if (r.height < 43.5) bad.push(`the What's new link is ${r.height.toFixed(0)} px tall, under 44`);
    if (cs.backgroundColor !== 'rgba(0, 0, 0, 0)') bad.push(`the What's new link is filled (${cs.backgroundColor}), not outlined`);
    if (cs.borderTopStyle === 'none' || !(parseFloat(cs.borderTopWidth) > 0)) bad.push('the What\'s new link has no outline');
    if (!out.linkSr) bad.push('the What\'s new link\'s dots are not aria-hidden with a comma for a screen reader');
    if (ln.getAttribute('href') !== '#new' || ln.getAttribute('data-target') !== 'new') bad.push('the What\'s new link does not open #new'); }
  else bad.push('no quiet link to What\'s new');
  // the contour layer: aria-hidden, no text, one layout shown (tall below 900 px, wide from it; 1100 before 6.22), one rise per area
  const topo = hero.querySelector(':scope > .topo');
  if (topo) {
    out.topoBytes = new Blob([(e => { if (!e.classList.contains('off')) return e.outerHTML; const c = e.cloneNode(true); c.classList.remove('off'); return c.outerHTML; })(topo)]).size;   // S-NAV1 step G: the drawing as built, without shell.js's runtime .off
    if (topo.getAttribute('aria-hidden') !== 'true') bad.push('the contour layer is not aria-hidden');
    if (topo.querySelector('text, title, desc') || topo.textContent.trim()) bad.push('the contour layer holds text');
    const shown = [...topo.querySelectorAll('svg.topo-l')].filter(vis);
    out.layout = shown.map(s => s.getAttribute('data-layout'));
    if (out.layout.join() !== (desk ? 'wide' : 'tall')) bad.push(`the contour layout shown is ${out.layout}, expected ${desk ? 'wide' : 'tall'}`);
    out.layouts = [...topo.querySelectorAll('svg.topo-l')].map(s => [s.getAttribute('data-layout'), [...s.querySelectorAll('g.ct-rise, g.ct-plan')].map(g => [g.getAttribute('data-label'), g.classList.contains('ct-plan') ? null : +g.getAttribute('data-words'), +g.getAttribute('data-rings'), getComputedStyle(g.querySelector('path, circle')).stroke, [...g.querySelectorAll('path')].map(e => e.getAttribute('d')).join('').split('z').length - 1])]);
    const tr = topo.getBoundingClientRect(), m = document.querySelector('main').getBoundingClientRect(), cr = copy.getBoundingClientRect();
    out.topoBox = [Math.round(tr.left), Math.round(tr.right), Math.round(cr.left), Math.round(cr.right), Math.round(m.left), Math.round(m.right)];
    const side = innerWidth >= 1100 && innerHeight < 860 ? 240 : 0;   // S-NAV2 step C: the 240 px sidebar of the tablet landscape layout from 1100 px (900 to 1099 px keep the drawer); a desktop home (860 px tall or more) has none
    if (Math.abs(tr.left - side) > 1 || Math.abs(tr.right - de.clientWidth) > 1) bad.push(`the contour layer spans ${tr.left.toFixed(0)}..${tr.right.toFixed(0)}, not the full width beside the sidebar (${side}..${de.clientWidth})`);
    if (cr.left < m.left + 15 || cr.right > m.right - 15) bad.push(`the hero's text runs ${cr.left.toFixed(0)}..${cr.right.toFixed(0)}, outside the column ${m.left.toFixed(0)}..${m.right.toFixed(0)}`);
  } else bad.push('no contour layer');
  // the hero's height: on a phone 60 to 80% of the screen, the first area's heading starting inside the first screen
  const hr = hero.getBoundingClientRect(); out.heroH = [Math.round(hr.height), innerHeight, Math.round(100 * hr.height / innerHeight)];
  if (phone && (hr.height < .6 * innerHeight || hr.height > .8 * innerHeight)) bad.push(`the hero is ${out.heroH[2]}% of the screen, not 60 to 80%`);
  const kids = [...h.children], tracks = kids.filter(e => e.classList.contains('track'));
  const ag = h.querySelector(':scope > .cgrid.areas');   // S-NAV1 step B: with area pages, one tile per track (opt.areas)
  if (opt.areas && (!ag || tracks.length)) bad.push(`the home holds ${tracks.length} track sections and ${ag ? 'a' : 'no'} grid of area tiles; with area pages, one grid of area tiles and no track section`);
  if (!opt.areas && ag) bad.push('the home of an edition of one track holds a grid of area tiles');
  const th = opt.areas ? ag && ag.querySelector('.ctitle') : tracks.length && tracks[0].querySelector('.thead h2');
  out.first = th ? Math.round(th.getBoundingClientRect().top + scrollY) : null;
  if (phone && th && out.first + 10 > innerHeight) bad.push(`the first area's heading starts at ${out.first} px, not inside the first screen (${innerHeight} px)`);
  // nothing sideways, nothing on the hero past the screen
  out.scroll = [de.scrollWidth, de.clientWidth];
  if (de.scrollWidth > de.clientWidth) bad.push(`the page scrolls sideways (${de.scrollWidth} in ${de.clientWidth} px)`);
  copy && copy.querySelectorAll('*').forEach(e => { if (e.closest('.harea-all') && getComputedStyle(e.closest('.harea-all')).clipPath !== 'none') return;   // the static line, clipped for a screen reader
    const r = e.getBoundingClientRect(); if (r.width && (r.right > de.clientWidth + .5 || r.left < -.5)) bad.push(`${e.className || e.tagName} on the hero runs off the screen`); });
  // the order: hero, the area sections, the constants, the site pages, New since, its one link
  out.order = kids.map(e => e.tagName.toLowerCase() + '.' + [...e.classList].join('.')).join(' ');
  const want = ['header.hero.hhome', ...(opt.areas ? ['div.cgrid.areas'] : tracks.map(() => 'section.track')), 'details.howto.rules', ...(opt.site ? ['div.hlinks'] : []), 'section.recent', 'div.hlinks'].join(' ');
  if (out.order !== want) bad.push(`the home runs ${out.order}`);
  // the area headers: from 768 px the label, the name, the lede and the count; below it the name only
  out.heads = tracks.map(t => { const hd = t.querySelector('.thead'); return [t.id, vis(hd.querySelector('.cname')), vis(hd.querySelector('h2')), vis(hd.querySelector('p')), vis(hd.querySelector('.tmeta'))]; });
  out.heads.forEach(([id, c, n, p, m]) => { const ok = phone ? (n && !c && !p && !m) : (n && c && p && m);
    if (!ok) bad.push(`${id}: its header shows label ${c}, name ${n}, lede ${p}, count ${m}; ${phone ? 'below 768 px the name only' : 'from 768 px all four'}`); });
  const site = kids[kids.length - 3], rec = h.querySelector(':scope > .recent'), last = kids[kids.length - 1];
  out.site = site ? [...site.querySelectorAll('a')].map(a => a.getAttribute('href')) : [];
  if (!rec) bad.push('no New since');
  else {
    out.rows = [...rec.querySelectorAll('.hrow')].map(r => [r.getAttribute('data-kind'), r.getAttribute('data-target')]);
    out.since = rec.querySelector('h2').textContent;
    [...rec.querySelectorAll('.hrow')].forEach(r => { if (!r.querySelector('.t small') || !r.querySelector('.pill') || !r.querySelector('.n')) bad.push('a New since row without its date, its course and model line or its pill');
      if (!resolves(r.getAttribute('data-target'))) bad.push(`a New since row links to #${r.getAttribute('data-target')}, no page`); });
    const ln2 = last && last.querySelectorAll('a');
    if (!ln2 || ln2.length !== 1 || ln2[0].getAttribute('href') !== '#new') bad.push('New since is not followed, last on the page, by one link, to What\'s new');
  }
  h.querySelectorAll('.hbtn b, .hbtn span').forEach(el => { if (el.getBoundingClientRect().width > 0 && el.scrollWidth > el.clientWidth + 1) bad.push(`a button's text is cut short: "${el.textContent.trim().slice(0, 40)}"`); });
  // the tiles: every one the same fields, its own contour patch, the whole tile the link
  const cards = [...h.querySelectorAll(opt.areas ? ':scope > .cgrid.areas > a.course.live' : '.track .cgrid > a.course.live')];
  out.cards = cards.map(c => { const p = c.querySelector(':scope > .topo.topo-patch'), s = p && p.querySelector('svg');
    return {home: c.getAttribute('data-target'), href: c.getAttribute('href'),
            rises: p ? [...p.querySelectorAll('g.ct-rise')].map(g => [g.getAttribute('data-label'), +g.getAttribute('data-words')]) : null,
            rings: p ? [...p.querySelectorAll('g.ct-rise')].map(g => [+g.getAttribute('data-words'), +g.getAttribute('data-rings')]) : null,
            plan: p ? [...p.querySelectorAll('g.ct-plan')].map(g => g.getAttribute('data-label')) : null,
            aria: p && p.getAttribute('aria-hidden'), stroke: p && p.querySelector('path') ? getComputedStyle(p.querySelector('path')).stroke : null,
            tone: getComputedStyle(c).getPropertyValue('--c').trim(), pw: p ? Math.round(p.getBoundingClientRect().width) : 0, cw: Math.round(c.querySelector('.ctitle').parentElement.clientWidth),
            ph: p ? Math.round(p.getBoundingClientRect().height) : 0, sw: s ? Math.round(s.getBoundingClientRect().width) : 0}; });
  cards.forEach(c => {
    const name = c.querySelector('.ctitle').textContent;
    const kidc = [...c.children].map(e => e.tagName.toLowerCase() + (e.className && typeof e.className === 'string' ? '.' + [...e.classList].filter(x => x !== 'off').join(' ') : '')).join(' ');   // S-NAV1 step G: not the runtime .off
    if (kidc !== 'div.ctop span.ctitle p div.cstats div.topo topo-patch') bad.push(`${name}: the tile holds ${kidc}, expected the chip row, the title, the tile line, the stats and the patch`);
    const n = c.querySelectorAll('.cstats > span').length; if (n !== 3) bad.push(`${name}: ${n} stats, expected 3`);
    const ctop = c.querySelector('.ctop'); if (!ctop || !ctop.querySelector('.cname') || !ctop.querySelector('.pill')) bad.push(`${name}: no chip and status pill`);
    const pp = c.querySelector(':scope > p'), lh = parseFloat(getComputedStyle(pp).lineHeight);
    if (!opt.areas && pp.scrollHeight > pp.clientHeight + 1) bad.push(`${name}: the tile line is clipped (${pp.scrollHeight} px of ${pp.clientHeight})`);   // S-NAV1 step B: an area tile's line is the track's lede, held to two lines by the tile's clamp as every closed tile's line; the area page shows it whole
    if (Math.round(pp.clientHeight / lh) > 2) bad.push(`${name}: the tile line runs to ${Math.round(pp.clientHeight / lh)} lines`);
    if (c.scrollWidth > c.clientWidth + 1) bad.push(`${name}: the tile scrolls sideways`);
    if (c.querySelectorAll('a').length) bad.push(`${name}: a link inside the tile (the whole tile is the link)`);
    const p = c.querySelector('.topo-patch');
    if (p) { const r = p.getBoundingClientRect(), cr = c.getBoundingClientRect();
      if (Math.abs(r.width / r.height - 4) > .05) bad.push(`${name}: the patch is ${r.width.toFixed(0)} x ${r.height.toFixed(0)}, not 4:1`);
      if (r.left < cr.left || r.right > cr.right + .5) bad.push(`${name}: the patch runs out of its tile`); }
  });
  if (new Set(cards.map(c => c.className)).size > 1) bad.push('the course tiles are not one style');
  (opt.areas ? (ag ? [{id: 'the area tiles', g: ag}] : []) : tracks.map(t => ({id: t.id, g: t.querySelector('.cgrid'), t}))).forEach(({id: tid, g, t}) => {
    const cs = [...g.querySelectorAll(':scope > a.course')];
    const cols = (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(g).gridTemplateColumns);
    if (phone && cols !== 1) bad.push(`${tid}: ${cols} columns below 768 px`);
    const bs = getComputedStyle(document.body), want = document.body.clientWidth - parseFloat(bs.paddingLeft) - parseFloat(bs.paddingRight) >= 960 ? 3 : 2;   // S-NAV2 step C: three across once the width beside the sidebar reaches 960 px (theme.css section 6; step D: the body's content box, the container the query reads, not its border box)
    if (!phone && cols !== want) bad.push(`${tid}: ${cols} column(s) from 768 px, expected ${want}`);
    if (!phone && cs.length === 1) {
      const gw = g.getBoundingClientRect().width, cw = cs[0].getBoundingClientRect().width, gap = parseFloat(getComputedStyle(g).columnGap) || 0;
      if (Math.abs(cw - (gw - gap) / 2) > 2) bad.push(`${tid}: its only tile is ${cw.toFixed(0)} px of a ${gw.toFixed(0)} px grid, expected half`);
    }
    const tk = t && opt.tracks[t.id.slice(6)];   // P-DEC12: a track with its own copy (catalog.toml `extra`) or planned courses keeps them
    if (tk && tk.extra && !t.querySelector('details.howto.rules:not(.planned)')) bad.push(`${t.id}: lost its own copy (${tk.extra})`);
    if (tk && tk.plan && opt.planned && !t.querySelector(`details.planned#${tk.plan}`)) bad.push(`${t.id}: lost its folded planned list #${tk.plan}`);
  });
  // what runs: with reduced motion nothing on the home; with motion allowed only transform and opacity, none on a tile
  out.anims = document.getAnimations().filter(a => a.animationName && a.effect && a.effect.target && h.contains(a.effect.target)).map(a => {   // P93: animations; the transitions of a hover or the theme switch are not
    const t = a.effect.target, props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k)).filter(k => !['offset', 'computedOffset', 'easing', 'composite'].includes(k)))];
    return [t.className && typeof t.className === 'string' ? t.className : (t.getAttribute('class') || t.tagName), props, a.playState, !!t.closest('.course'), a.animationName]; });
  return out;
}'''
HOME_JS = HOME_JS.replace('__SITE__', SITE_JSON)   # S-DEC3: the brand's site name, as a JS string
# S-NAV1 step D: the lines (paths) of the contour drawings shown in an element, a hero's shown layout and every tile's
# patch (a reading page's separators and relief are check_seps' and check_reliefs')
SWELL_LINES_JS = r"""(sel) => [...document.querySelectorAll(sel + ' .topo:not(.topo-sep):not(.relief) > svg.topo-l')].filter(s => getComputedStyle(s).display !== 'none').reduce((n, s) => n + s.querySelectorAll('path').length, 0)"""
MON3 = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# P92: the hero's texts against the pixels actually under them (the contour lines, the page), in the theme in use: each
# text's box and colour are read, every text of the copy is made transparent, the hero is shot, and each text's colour
# is measured against every pixel in its box (4.5:1, 3:1 for large text); the texts are put back.
# S-NAV1 step G (checker finding 2; a proposal for Pedro to veto): the home hero's layer at most 24,148 B (20 KB, 20,480,
# before), 1 KB over build.py's HERO_BUDGET (23,124), raised by the bytes step D's swell attributes (a path and a --d
# per line) took, so the hero keeps its levels (academy: 24,500 words a level, History 20). A course home's, an area's
# and What's new's layers keep 20 KB (check_topo).
HOME_TOPO_MAX = 24148
HERO_TEXTS_JS = r'''() => { const out = [], copy = document.querySelector('#home .hcopy');
  copy.querySelectorAll('h1, .harea-w, .harea-all > span, .lede, .hnew > span').forEach(e => { const cs = getComputedStyle(e), r = e.getBoundingClientRect();
    if (!r.width || cs.display === 'none' || (e.closest('.harea-all') && getComputedStyle(e.closest('.harea-all')).clipPath !== 'none')) return;   // the static line read by a screen reader only
    const size = parseFloat(cs.fontSize), large = size >= 24 || (size >= 18.66 && parseInt(cs.fontWeight) >= 700);
    out.push({what: (e.className || e.tagName.toLowerCase()) + ' "' + e.textContent.trim().slice(0, 18) + '"', color: cs.color, large, x: r.left, y: r.top, w: r.width, h: r.height}); });
  return out; }'''
def hero_contrast(pg, label, fails, motion=False):
    """P92: with motion allowed, every moment that matters; P93: at the five poses of the slow move (POSES; since S-NAV1
    step D the swell: at rest, its top, its quarters and its middle) and, at each, each area word in turn (its animation set to the middle of its showing),
    every animation paused there."""
    if not motion:
        return _hero_contrast(pg, label, fails)
    names = pg.evaluate("[...document.querySelectorAll('#home .harea-w')].map(w => w.textContent)")
    for p in POSES:
        for k, nm in enumerate(names):
            pose(pg, p, k * 3000 + 1500)
            _hero_contrast(pg, f'{label} (pose {p:g} of the sweep, {nm} shown)', fails, only=k)
    pg.evaluate("() => document.getAnimations().forEach(a => a.play())")

def _hero_contrast(pg, label, fails, only=None):
    from PIL import Image
    import io
    pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(60)
    items = pg.evaluate(HERO_TEXTS_JS)
    if only is not None:   # the cycling words: only the one shown at this moment
        ws = [i for i in items if i['what'].startswith('harea-w')]
        items = [i for i in items if not i['what'].startswith('harea-w')] + ws[only:only + 1]
    pg.evaluate("""() => { const s = document.createElement('style'); s.id = 'p92hide'; s.textContent = '#home .hcopy, #home .hcopy * {color: transparent !important; border-color: transparent !important; transition: none !important}'; document.head.appendChild(s); }""")
    pg.wait_for_timeout(60)
    img = Image.open(io.BytesIO(pg.screenshot())).convert('RGB')
    pg.evaluate("document.getElementById('p92hide').remove()")
    k = img.width / pg.evaluate('innerWidth')
    def lum(c):
        f = lambda v: (v / 255) / 12.92 if v / 255 <= 0.04045 else ((v / 255 + 0.055) / 1.055) ** 2.4
        return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])
    worst, each = [99, ''], []
    for it in items:
        fg = [float(v) for v in re.findall(r'[\d.]+', it['color'])[:3]]
        lf = lum(fg)
        box = img.crop((int(it['x'] * k), int(it['y'] * k), int((it['x'] + it['w']) * k), int((it['y'] + it['h']) * k)))
        lo = 99
        for c, _ in [(c, n) for n, c in box.getcolors(box.width * box.height or 1) or []]:
            lb = lum(c); r = (max(lf, lb) + .05) / (min(lf, lb) + .05)
            lo = min(lo, r)
        need = 3 if it['large'] else 4.5
        if lo < worst[0]: worst = [round(lo, 2), it['what']]
        each.append(f'{it["what"].split(chr(34))[1] if chr(34) in it["what"] else it["what"]} {lo:.2f}/{need:g}')
        if lo < need - .005: fails.append(f'home {label}: {it["what"]} reaches {lo:.2f}:1 over the contours under it (needs {need}:1)')
    print(f'home {label} ({pg.evaluate("innerWidth")} px): hero texts over the contours, {len(items)} measured pixel by pixel, lowest {worst[0]}:1 ({worst[1]}); each (lowest/needed): ' + '; '.join(each))

# S-NAV2 step A (Fix 1; Pedro, 22 Nov 2026, his phone: "Sports" and "History" drawn on top of each other under
# "Academy"): the area line's cycle, read from the running animations. The theme times it by --n on p.harea (n x 3 s a
# cycle, each word 100/n percent of it, by linear() easings whose stops are calc()ed from --n, theme 4h), so a new area
# needs no CSS edit. Sampled over two cycles, each animation paused at the time: at every sample at most one word is
# above opacity .5, and exactly one but where two cross at .5 (the middle of a cross-fade); two words are both drawn
# (opacity over .01) for at most the cross-fade, HAREA_CROSS (.36 s, 12% of a word's three seconds), plus a sample; three
# never; each word is shown (above .5) for its three seconds in each cycle, in its order, at rest (no transform) while
# fully shown; each word runs harea (opacity) and harea-y (transform) over n x 3 s. The real line (its --n the number
# of its words, the number of tracks), then a probe: a copy of the line beside it with 3, 4 and 8 words (HAREA_PROBES),
# its --n set to match, measured and removed (the catalog untouched).
# The phone byte-identity check (S-NAV2) expects this one difference on the phone besides the inlined theme CSS:
# PHONE_EXPECTED lists it.
HAREA_STEP, HAREA_WORD, HAREA_CROSS = 50, 3000, 360   # ms: the sampling step; a word's share of the cycle; the cross-fade
HAREA_PROBES = (3, 4, 8)
PHONE_EXPECTED = ('the inlined theme CSS (design/theme.css = kit/shell.css)',
                  'the home hero\'s area line (S-NAV2 Fix 1): style="--n:<number of areas>" on p.harea, and its animation '
                  '(harea and harea-y over n x 3 s, each word 100/n percent of it); every other phone pixel and byte the same')
HAREA_JS = r"""([probe, step, word, cross]) => {
  const real = document.querySelector('#home .harea'), bad = [];
  if (!real) return {bad: ['no area line (p.harea)']};
  let al = real;
  if (probe) {   // a copy of the line beside it with probe words, the real words' tones reused in turn
    al = real.cloneNode(false); al.classList.add('harea-probe'); al.style.setProperty('--n', String(probe));
    const src = [...real.querySelectorAll('.harea-w')];
    for (let i = 0; i < probe; i++) { const w = src[i % src.length].cloneNode(false); w.textContent = 'Probe ' + (i + 1); w.style.setProperty('--k', String(i)); al.appendChild(w); }
    real.after(al);
  }
  const ws = [...al.querySelectorAll('.harea-w')], n = ws.length;
  getComputedStyle(ws[0]).opacity;   // the probe's animations made
  const nv = getComputedStyle(al).getPropertyValue('--n').trim();
  if (+nv !== n) bad.push(`--n on the line is ${nv || 'missing'}, the line has ${n} words`);
  const an = document.getAnimations().filter(a => a.animationName && a.effect && ws.includes(a.effect.target));
  ws.forEach((w, i) => { const mine = an.filter(a => a.effect.target === w), names = mine.map(a => a.animationName).sort().join();
    if (names !== 'harea,harea-y') bad.push(`word ${i + 1} runs ${names || 'nothing'}, expected harea and harea-y`);
    mine.forEach(a => { const d = a.effect.getTiming().duration; if (Math.abs(d - n * word) > 1) bad.push(`word ${i + 1}'s ${a.animationName} lasts ${d} ms, expected ${n} x ${word}`); }); });
  const all = document.getAnimations(), state = all.map(a => [a, a.playState, a.currentTime]);
  an.forEach(a => a.pause());
  const D = n * word, out = {n, samples: 0, zero: 0, multi: [], three: [], overlapMax: 0, shown: ws.map(() => 0), order: [], moved: []};
  let run = 0, last = -1;
  for (let t = 7; t < 2 * D; t += step) {   // 7 ms off the step's grid, so no sample lands on a cross-fade's exact middle
    an.forEach(a => { a.currentTime = t; });
    const op = ws.map(w => parseFloat(getComputedStyle(w).opacity)); out.samples++;
    const up = op.map((o, i) => o > .5 ? i : -1).filter(i => i >= 0), drawn = op.filter(o => o > .01).length;
    if (up.length > 1) out.multi.push([t, op.map(o => +o.toFixed(2))]);
    if (!up.length && Math.max(...op) < .45) out.zero++;   // none shown, away from the middle of a cross-fade
    if (drawn > 2) out.three.push([t, op.map(o => +o.toFixed(2))]);
    run = drawn > 1 ? run + step : 0; out.overlapMax = Math.max(out.overlapMax, run);
    if (t >= D && up.length === 1) { out.shown[up[0]] += step; if (up[0] !== last) { out.order.push(up[0]); last = up[0]; } }
    op.forEach((o, i) => { if (o > .999) { const m = getComputedStyle(ws[i]).transform; if (m !== 'none' && !/^matrix\(1, 0, 0, 1, 0, 0\)$/.test(m)) out.moved.push([t, i, m]); } });
  }
  state.forEach(([a, ps, ct]) => { if (!an.includes(a)) return; a.currentTime = ct; if (ps === 'running') a.play(); });
  if (probe) al.remove();
  out.bad = bad; return out;
}"""
def check_harea(pg, label, fails):
    """S-NAV2 step A (Fix 1): the area line's cycle at this viewport, the real line and each probe (HAREA_JS); with
    motion allowed, on the home."""
    pg.evaluate("location.hash = 'home'"); ready(pg); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(60)
    rows = []
    for probe in (None,) + HAREA_PROBES:
        r = pg.evaluate(HAREA_JS, [probe, HAREA_STEP, HAREA_WORD, HAREA_CROSS])
        tag = f'home {label}: the area line' + (f' (probe of {probe} words)' if probe else f' ({r.get("n")} areas)')
        fails += [f'{tag}: {b}' for b in r['bad']]
        if 'samples' not in r: continue
        n = r['n']
        if r['multi']: fails.append(f'{tag}: two or more words above opacity .5 at {len(r["multi"])} sampled times, the first {r["multi"][:2]}')
        if r['zero']: fails.append(f'{tag}: no word shown at {r["zero"]} sampled times')
        if r['three']: fails.append(f'{tag}: three or more words drawn at once at {len(r["three"])} sampled times, the first {r["three"][:2]}')
        if r['overlapMax'] > HAREA_CROSS + HAREA_STEP: fails.append(f'{tag}: two words drawn together for {r["overlapMax"]} ms, over the {HAREA_CROSS} ms cross-fade')
        if any(abs(x - HAREA_WORD) > 2 * HAREA_STEP for x in r['shown']): fails.append(f'{tag}: the words are shown {r["shown"]} ms in a cycle, expected {HAREA_WORD} each')
        want = [(k + (r['order'][0] if r['order'] else 0)) % n for k in range(len(r['order']))]
        if r['order'] != want or len(r['order']) < n: fails.append(f'{tag}: the words show in the order {r["order"]}, expected each in turn')
        if r['moved']: fails.append(f'{tag}: a fully shown word is not at rest at {len(r["moved"])} sampled times, the first {r["moved"][:2]}')
        rows.append(f'{n} words: {r["samples"]} samples, shown {sorted(set(r["shown"]))} ms each, overlap at most {r["overlapMax"]} ms')
    print(f'home {label}: the area line cycles one word at a time (step {HAREA_STEP} ms, cross-fade {HAREA_CROSS} ms): ' + '; '.join(rows))

def check_home(pg, label, fails, expect, motion=False):
    """P92: the home's layout at one width (HOME_JS): the hero (the headline, the area line and its static line, the
    lede, the quiet link, the contour layer, its rises against the sources), its height, the area headers, the tiles and
    their patches against the sources, the order, New since as What's new's first six rows; and what animates."""
    pg.evaluate("location.hash = 'home'"); ready(pg); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(160)
    # a theme switched by the test fades the tiles' colours (section 7's .15 s transitions): read the page once they are done
    pg.wait_for_function("() => !document.getAnimations().some(a => typeof CSSTransition !== 'undefined' && a instanceof CSSTransition && a.playState === 'running')", timeout=5000)
    r = pg.evaluate(HOME_JS, [[a['color'] for a in expect['areas']], {'planned': 'planned' not in OMIT, 'site': any(k not in OMIT for k in ('backlog', 'coming', 'figures', 'changelog')), 'tracks': {t['id']: {'extra': t.get('extra'), 'plan': t.get('planned_anchor', 'planned-' + t['id']) if t.get('planned') else None} for t in THEMES}, 'areas': MULTI}])
    fails += [f'home {label}: {b}' for b in r['bad']]
    names = [a['name'] for a in expect['areas']]
    if [w for w, _ in r.get('words', [])] != names: fails.append(f'home {label}: the area line reads {[w for w, _ in r.get("words", [])]}, THEMES gives {names}')
    if [c for _, c in r.get('words', [])] != r.get('tones'): fails.append(f'home {label}: the area words are coloured {[c for _, c in r.get("words", [])]}, their tones are {r.get("tones")}')
    if r.get('static') != ' · '.join(names).replace(' · ', ' · '): fails.append(f'home {label}: the static line reads {r.get("static")!r}')
    if r.get('staticTones') != r.get('tones'): fails.append(f'home {label}: the static line\'s words are coloured {r.get("staticTones")}, not their tones')
    if r.get('staticSr') != [[1, ',']] * (len(names) - 1): fails.append(f'home {label}: the static line\'s dots are not aria-hidden with a comma for a screen reader: {r.get("staticSr")}')
    if r.get('staticAria') is not None: fails.append(f'home {label}: the static line is hidden from a screen reader ({r.get("staticAria")})')
    if motion and (not r.get('lineShown') or r.get('staticShown')): fails.append(f'home {label}: with motion allowed the cycling line shows {r.get("lineShown")} and the static line {r.get("staticShown")}, expected the cycling line only')
    if not motion and (r.get('lineShown') or not r.get('staticShown')): fails.append(f'home {label}: under reduced motion the cycling line shows {r.get("lineShown")} and the static line {r.get("staticShown")}, expected the static line only')
    if r.get('lede') != brand(EDITION)['lede']: fails.append(f'home {label}: the lede reads {r.get("lede")!r}')
    nw = expect['newest']
    want_link = f"What's new · {nw['code']} · {int(nw['date'][8:])} {MON3[int(nw['date'][5:7]) - 1]}" if nw else None
    if r.get('link') and r['link'][0] != want_link: fails.append(f'home {label}: the What\'s new link reads {r["link"][0]!r}, expected {want_link!r}')
    if (r.get('topoBytes') or 0) > HOME_TOPO_MAX: fails.append(f'home {label}: the hero\'s contour SVG is {r["topoBytes"]} bytes, over {HOME_TOPO_MAX:,}')
    for name, rs in r.get('layouts', []):
        got = [(l, w) for l, w, _, _, _ in rs]
        want = [(a['name'], a['words'] or None) for a in expect['areas']]
        if got != want: fails.append(f'home {label}: the {name} contours give the rises {got}, the sources give {want}')
        rings = [k for _, w, k, _, _ in rs if w]
        byw = [k for _, k in sorted((w, k) for _, w, k, _, _ in rs if w)]
        for l, w, k, _, z in rs:   # P92 check: every rise reads as a rise, its own top rings closed, not only a stretch of another's
            if w and z < min(2, k): fails.append(f'home {label}: the {name} rise {l} closes {z} ring(s) of its own, under {min(2, k)}')
        if byw != sorted(byw): fails.append(f'home {label}: the {name} rises stand {rings} levels high, not in the order of their words')
        if [s for _, _, _, s, _ in rs] != r.get('tones'): fails.append(f'home {label}: the {name} rises are drawn in {[x[3] for x in rs]}, not their areas\' tones')
    got = {c['home']: c for c in r.get('cards', [])}
    # S-NAV1 step B: with area pages the home's tiles are the areas, each its courses as rises (a live course by its
    # words, one coming soon or planned flat), each the link to its area page
    tiles_want = {a: dict(short=e['name'], units=e['rises']) for a, e in expect['area_pages'].items()} if MULTI else expect['courses']
    if list(got) != list(tiles_want): fails.append(f'home {label}: the tiles are {list(got)}, the sources give {list(tiles_want)}')
    for home, e in tiles_want.items():
        c = got.get(home)
        if not c: continue
        want_r = [(k, w) for k, w in e['units'] if w]
        if [tuple(x) for x in (c['rises'] or [])] != want_r: fails.append(f'home {label}: {e["short"]}\'s patch has the rises {c["rises"]}, the sources give its written units {want_r}')
        if (c['plan'] or []) != [k for k, w in e['units'] if not w]: fails.append(f'home {label}: {e["short"]}\'s patch marks {c["plan"]} planned, the sources {[k for k, w in e["units"] if not w]}')
        if c['aria'] != 'true': fails.append(f'home {label}: {e["short"]}\'s patch is not aria-hidden')
        byw = [k for _, k in sorted(c['rings'] or [])]
        if byw != sorted(byw): fails.append(f'home {label}: {e["short"]}\'s patch rises stand {[k for _, k in c["rings"]]} levels high, not in the order of their words')
        if c['href'] != '#' + home: fails.append(f'home {label}: {e["short"]}\'s tile links to {c["href"]}')
    want_rows = [[x['kind'], x['pid']] for x in expect['rows'][:6]]
    if r.get('rows') != want_rows: fails.append(f'home {label}: New since lists {r.get("rows")}, What\'s new leads with {want_rows}')
    old6 = expect['rows'][:6][-1] if expect['rows'] else None   # S-DEC4: the oldest of the (at most) six rows, as build.py's RECENT[-1]; an edition with fewer filings lists fewer
    if old6 and r.get('since') != f"New since {int(old6['date'][8:])} {MON3[int(old6['date'][5:7]) - 1]}":
        fails.append(f'home {label}: New since\'s heading reads {r.get("since")!r}, its oldest row is {old6["date"]}')
    want_site = [x for x, k in (('#backlog', 'backlog'), ('#coming', 'coming'), ('#viz-examples', 'figures'), ('#changelog', 'changelog')) if k not in OMIT]   # S-NEXT1: Coming next beside the Backlog
    if r.get('site') != want_site: fails.append(f'home {label}: the site links above New since are {r.get("site")}, expected {want_site}')
    an = r.get('anims', [])
    if motion:
        if [a for a in an if any(p not in ('transform', 'opacity') for p in a[1])]: fails.append(f'home {label}: an animation runs on more than transform and opacity: {[a for a in an if any(p not in ("transform", "opacity") for p in a[1])]}')
        # S-NAV1 step D: every line (path) of the shown contour layout and of every tile's patch swells (topo-swell), and
        # nothing else of theirs moves; besides them only the area words
        sw, other = [a for a in an if a[4] == SWELL], [a for a in an if a[4] != SWELL]
        nlines = pg.evaluate(SWELL_LINES_JS, '#home')   # a patch in the closed Planned list is not drawn, but its lines' swell runs
        # S-NAV2 step A: two animations a word, harea (opacity) and harea-y (transform)
        if sorted({a[0].split()[0] for a in other}) != ['harea-w'] or sorted(a[4] for a in other) != sorted(['harea', 'harea-y'] * len(names)) or len(sw) != nlines or any(a[0] != 'path' for a in sw):
            fails.append(f'home {label}: with motion allowed the animations are {len(other)} others ({sorted({(a[0], a[4]) for a in other})[:4]}) and {len(sw)} swells on {sorted({a[0] for a in sw})}, expected harea and harea-y on each of the {len(names)} area words and one swell on each of the {nlines} lines of the shown contour layout and every tile\'s patch (S-NAV1 step D)')
    elif an: fails.append(f'home {label}: under reduced motion {len(an)} animations run: {an[:3]}')
    print(f'home {label}: hero {r.get("heroH")} (px, screen, %), copy {r.get("copy")!r}; area line {[w for w, _ in r.get("words", [])]}, shown {r.get("lineShown")}, static shown {r.get("staticShown")}; '
          f'link {r.get("link") and r["link"][:4]}; contours {r.get("topoBytes")} B, layout {r.get("layout")}, rises {[(l, k, z) for _, rs in r.get("layouts", [])[:1] for l, _, k, _, z in rs]}; '
          f'tiles {[(c["home"], len(c["rises"] or []), len(c["plan"] or [])) for c in r.get("cards", [])]}; heads {[x[1:] for x in r.get("heads", [])][:1]}; '
          f'first area at {r.get("first")} px; New since {len(r.get("rows") or [])} rows; animations {len(an)}; page {r.get("scroll")}')
    hero_contrast(pg, label, fails, motion)
    return r

# P93 (4 Nov 2026): a page's topography at the pose it is in: its hero's layer (header.hero > .topo) and every visible
# tile patch. For each: bytes, aria-hidden, no text, the layouts shown, each layout's rises (label, words or null for a
# planned one, levels, stroke, own closed rings) and, on the shown layout, (a) whether the frame is covered: each corner of
# the frame mapped back through the layout's transform (its computed matrix about its origin) into the layout's own box;
# (b) for a hero, which rises' own rings (data-box, through the SVG's screen matrix) leave the frame or reach into its
# fade (its last 10%); (c) for a patch, whether every line stays inside its frame. And every animation on the page with
# its properties and its directed progress.
TOPO_JS = r"""(pid) => {
  const P = document.getElementById(pid), out = {pid, patches: []};
  if (!P) return out;
  const vis = e => !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().width > 0;
  const covered = (svg, frame) => {
    const cs = getComputedStyle(svg), fr = frame.getBoundingClientRect();
    const lx = parseFloat(cs.left), ly = parseFloat(cs.top), lw = parseFloat(cs.width), lh = parseFloat(cs.height);
    const o = cs.transformOrigin.split(' ').map(parseFloat);
    const M = cs.transform === 'none' ? new DOMMatrix() : new DOMMatrix(cs.transform), I = M.inverse();
    const bad = [];
    for (const [qx, qy] of [[0, 0], [fr.width, 0], [0, fr.height], [fr.width, fr.height]]) {
      const v = I.transformPoint(new DOMPoint(qx - lx - o[0], qy - ly - o[1]));
      const x = v.x + o[0], y = v.y + o[1];
      if (x < -0.5 || y < -0.5 || x > lw + 0.5 || y > lh + 0.5) bad.push([Math.round(qx), Math.round(qy), Math.round(x), Math.round(y)]);
    }
    return {bad, size: [Math.round(lw), Math.round(lh), Math.round(fr.width), Math.round(fr.height)], m: cs.transform};
  };
  const rises = svg => [...svg.querySelectorAll('g.ct-rise, g.ct-plan')].map(g => { const pa = g.querySelector('path, circle');
    return [g.getAttribute('data-label'), g.classList.contains('ct-plan') ? null : +g.getAttribute('data-words'), g.classList.contains('ct-plan') ? null : +g.getAttribute('data-rings'),
            getComputedStyle(pa).stroke, g.classList.contains('ct-plan') ? 0 : ([...g.querySelectorAll('path')].map(e => e.getAttribute('d')).join('').split('z').length - 1)]; });
  const one = (t, hero) => {
    const r = {bytes: new Blob([(e => { if (!e.classList.contains('off')) return e.outerHTML; const c = e.cloneNode(true); c.classList.remove('off'); return c.outerHTML; })(t)]).size, aria: t.getAttribute('aria-hidden'), text: !!(t.querySelector('text, title, desc') || t.textContent.trim()),
               shown: [...t.querySelectorAll(':scope > svg.topo-l')].filter(vis).map(x => x.getAttribute('data-layout')),
               layouts: [...t.querySelectorAll(':scope > svg.topo-l')].map(x => [x.getAttribute('data-layout'), rises(x)]), ph: getComputedStyle(t).getPropertyValue('--ph').trim()};
    const sv = [...t.querySelectorAll(':scope > svg.topo-l')].find(vis);
    if (sv) {
      r.cover = covered(sv, t);
      const fr = t.getBoundingClientRect(), m = sv.getScreenCTM();
      if (hero) {
        r.outside = [];
        sv.querySelectorAll('g.ct-rise[data-box]').forEach(g => { const b = g.getAttribute('data-box').split(' ').map(Number);   // S-NAV1 step D: data-box is the rings' box over every pose of the swell (viz.swell_box)
          for (const [x, y] of [[b[0], b[1]], [b[2], b[1]], [b[0], b[3]], [b[2], b[3]]]) { const q = new DOMPoint(x, y).matrixTransform(m);
            if (q.x < fr.left - .5 || q.x > fr.right + .5 || q.y < fr.top - .5 || q.y > fr.top + .9 * fr.height + .5) { r.outside.push(g.getAttribute('data-label')); break; } } });
        r.frame = [Math.round(fr.left), Math.round(fr.right), Math.round(fr.top + scrollY), Math.round(fr.height)];
      } else {
        let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        sv.querySelectorAll('path, circle').forEach(e => { const b = e.getBoundingClientRect(); if (!b.width && !b.height) return; x0 = Math.min(x0, b.left); y0 = Math.min(y0, b.top); x1 = Math.max(x1, b.right); y1 = Math.max(y1, b.bottom); });
        r.lines = [x0 - fr.left, y0 - fr.top, fr.right - x1, fr.bottom - y1].map(v => Math.round(v * 10) / 10);
        r.ratio = Math.round(fr.width / fr.height * 1000) / 1000;
      }
    }
    return r;
  };
  const hl = P.querySelector(':scope > header.hero > .topo');
  out.hero = hl ? one(hl, true) : null;
  out.anyTopo = P.querySelectorAll('.topo:not(.topo-sep):not(.relief)').length; out.allPatches = P.querySelectorAll('.topo.topo-patch:not(.topo-sep)').length;
  out.lines = [...P.querySelectorAll('.topo:not(.topo-sep):not(.relief) > svg.topo-l')].filter(s => getComputedStyle(s).display !== 'none').reduce((n, s) => n + s.querySelectorAll('path').length, 0);   // S-NAV1 step D   // P94: a reading page's section separators are checked by check_seps; P96: its relief by check_reliefs
  P.querySelectorAll('.topo.topo-patch:not(.topo-sep)').forEach(t => { if (vis(t)) out.patches.push(one(t, false)); });
  out.anims = document.getAnimations().filter(a => a.animationName && a.effect && a.effect.target && P.contains(a.effect.target) && !a.effect.target.closest('.topo-sep')).map(a => {   // animations, not the transitions of a hover or the theme switch
    const t = a.effect.target, props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k)).filter(k => !['offset', 'computedOffset', 'easing', 'composite'].includes(k)))];
    return [(t.getAttribute('class') || t.tagName).split(' ')[0], props, a.playState, a.animationName || '', a.effect.getComputedTiming().progress, !!t.closest('.topo-patch')]; });
  return out;
}"""

# P93: every tile of a page (.course.live): its kind (a link, a disclosure, a ghost), its fields, its patch, its link or
# its rows, the grid it stands in, and anything cut
TILES_JS = r"""(pid) => {
  const P = document.getElementById(pid), out = {tiles: [], grids: [], bad: []};
  if (!P) return out;
  const vis = e => !!e && getComputedStyle(e).display !== 'none' && e.getBoundingClientRect().width > 0;
  const phone = innerWidth < 768;
  P.querySelectorAll('.course.live').forEach(t => {
    if (!vis(t)) return;
    const disc = t.tagName === 'DETAILS', box = disc ? t.querySelector(':scope > summary') : t;
    const kids = [...box.children].map(e => { const k = [...e.classList].filter(x => x !== 'off');   // S-NAV1 step G: not the runtime .off
      return e.tagName.toLowerCase() + (k.length ? '.' + k.join('.') : ''); }).join(' ');
    const p = box.querySelector(':scope > p'), lh = p ? parseFloat(getComputedStyle(p).lineHeight) : 1;
    const patch = box.querySelector(':scope > .topo.topo-patch'), pr = patch && patch.getBoundingClientRect(), tr = t.getBoundingClientRect();
    const sv = patch && patch.querySelector('svg');
    const name = (box.querySelector('.ctitle') || {}).textContent || '?';
    const r = {name, kind: t.classList.contains('ghost') ? 'ghost' : disc ? 'disc' : t.tagName === 'A' ? 'link' : 'other', cls: [...t.classList].filter(c => !['ghost', 'pending'].includes(c)).join(' '),
      mods: [...t.classList].filter(c => ['ghost', 'pending'].includes(c)), spots: sv ? [...sv.querySelectorAll('g.ct-rise')].filter(g => g.querySelector('.ct-spot')).map(g => g.getAttribute('data-label')) : null,
      unseen: sv ? [...sv.querySelectorAll('g.ct-rise')].filter(g => +g.getAttribute('data-rings') === 0 && !g.querySelector('.ct-spot')).map(g => g.getAttribute('data-label')) : null,
      kids, chip: [...box.querySelectorAll('.ctop > .cname > .cpart')].map(x => x.textContent), pill: box.querySelector('.ctop > .pill') ? box.querySelector('.ctop > .pill').textContent : null,
      stats: [...box.querySelectorAll('.cstats > span')].map(x => [x.querySelector('b') ? x.querySelector('b').textContent : null, x.textContent.replace(x.querySelector('b') ? x.querySelector('b').textContent : '', '').trim()]),
      lines: p ? Math.round(p.getBoundingClientRect().height / lh) : 0, ids: t.getAttribute('data-mods'),   /* as painted (P93 check: a stretched line showed a third line under its clamp) */ clipped: p ? p.scrollHeight > p.clientHeight + 1 : false, open: disc ? t.open : null,
      href: t.getAttribute('href'), target: t.getAttribute('data-target'),
      rows: disc ? t.querySelectorAll(':scope > .hrows > .hrow').length : null,
      rises: sv ? [...sv.querySelectorAll('g.ct-rise')].map(g => [g.getAttribute('data-label'), +g.getAttribute('data-words')]) : null,
      plan: sv ? [...sv.querySelectorAll('g.ct-plan')].map(g => g.getAttribute('data-label')) : null,
      aria: patch && patch.getAttribute('aria-hidden'), stroke: sv && sv.querySelector('path, circle') ? getComputedStyle(sv.querySelector('path, circle')).stroke : null,
      tone: getComputedStyle(t).getPropertyValue('--c').trim(),
      pw: pr ? Math.round(pr.width) : 0, ph: pr ? Math.round(pr.height) : 0, pin: pr ? (pr.left >= tr.left - .5 && pr.right <= tr.right + .5) : false,
      sw: t.scrollWidth > t.clientWidth + 1, w: Math.round(tr.width)};
    box.querySelectorAll('.ctitle, .cname, .cstats > span').forEach(e => { if (e.getBoundingClientRect().right > tr.right + .5) out.bad.push(`${name}: ${e.className || e.tagName} runs past the tile's edge`); });
    if (t.querySelector('a') && !disc) out.bad.push(`${name}: a link inside a linked tile`);
    out.tiles.push(r);
  });
  P.querySelectorAll('.cgrid').forEach(g => { if (!vis(g)) return;
    const ts = [...g.children].filter(e => e.classList.contains('course')), gw = g.getBoundingClientRect().width, gap = parseFloat(getComputedStyle(g).columnGap) || 0;
    const gr = g.getBoundingClientRect();
    if (g.querySelector(':scope > details.course.live[open]')) ts.forEach(t => { if (t.tagName !== 'DETAILS' || t.open) return; const st = t.querySelector(':scope > summary > .cstats'); if (st && parseFloat(getComputedStyle(st).marginTop) > 1) out.bad.push(`${t.querySelector('.ctitle') ? t.querySelector('.ctitle').textContent.trim() : t.className}: closed beside an open tile, yet stretched (${Math.round(parseFloat(getComputedStyle(st).marginTop))} px of slack above its stats)`); });   // P93, after the publish
    ts.forEach(t => { const r = t.getBoundingClientRect(); if (r.left < gr.left - .5 || r.right > gr.right + .5) out.bad.push(`${t.querySelector('.ctitle') ? t.querySelector('.ctitle').textContent.trim() : t.className}: the tile runs ${Math.round(Math.max(gr.left - r.left, r.right - gr.right))} px past its grid`); });   // P93 check 3: a column widened past its grid by a part that would not wrap
    out.grids.push([(t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(g).gridTemplateColumns), ts.length, ts.length === 1 ? Math.round(ts[0].getBoundingClientRect().width) : null, Math.round((gw - gap) / 2)]); });
  const de = document.documentElement; out.scroll = [de.scrollWidth, de.clientWidth];
  return out;
}"""

_TM = re.search(r'--topo-grow:([\d.]+);--topo-breath:([\d.]+)s', (R / 'shell.css').read_text())
GROW, BTIME = float(_TM.group(1)), float(_TM.group(2)) * 1000   # S-NAV1 step D: the swell, from the theme: the outermost line's growth (1 + GROW at the top) and the time of one sweep
POSES = (0, .25, .5, .75, 1)   # the two ends of the swell (at rest, at its top), its quarters and its middle
SWELL = 'topo-swell'   # S-NAV1 step D: the one animation of a contour drawing's lines (topo-turn and topo-breathe are gone)
def eased(p):
    """CSS ease-in-out, cubic-bezier(.42, 0, .58, 1), at the point p of the sweep: the share of the move made."""
    lo, hi = 0.0, 1.0
    for _ in range(60):
        t = (lo + hi) / 2
        x = 3 * (1 - t) ** 2 * t * .42 + 3 * (1 - t) * t * t * .58 + t ** 3
        lo, hi = (t, hi) if x < p else (lo, t)
    t = (lo + hi) / 2
    return 3 * (1 - t) * t * t + t ** 3
# S-NAV1 step D: a swell paused at the point p (0 at rest, 1 at its top) of its sweep, its phase (the negative delay)
# taken into account: in the forward iteration where that time is not before the start, else in the reverse one
SWELL_AT_JS = r"""const swellAt = (a, p, bt) => { const d = a.effect.getTiming().delay; let t = p * bt + d; if (t < 0) t = 2 * bt - p * bt + d; a.pause(); a.currentTime = t; };"""
POSE_JS = r"""([p, ta, bt]) => { """ + SWELL_AT_JS + r""" document.getAnimations().forEach(a => { if (!a.animationName) { a.finish(); return; }   // a transition (a hover, the theme switch) is let run out: paused half-way it would outrank every rule
  if (a.animationName === 'topo-swell') swellAt(a, p, bt);
  else { a.pause(); if (ta !== null) a.currentTime = ta; } }); }"""
def pose(pg, p, ta=None):
    """Every contour drawing on the page paused at the point p (0 to 1) of its swell, its own phase taken into account;
    the area words (the home) at ta ms of their cycle."""
    pg.evaluate(POSE_JS, [p, ta, BTIME]); pg.wait_for_timeout(80)

# the texts of a hero over a topography (a course home's, What's new's), as the eye reads them: every element of the
# hero with a text of its own, its colour, the opacity it is drawn at and whether it is large text
HERO_ALL_JS = r"""(pid) => { const h = document.querySelector('#' + pid + ' > header.hero'), out = [];
  h.querySelectorAll('*').forEach(e => { if (e.closest('.topo')) return;
    if (![...e.childNodes].some(t => t.nodeType === 3 && t.textContent.trim())) return;
    const cs = getComputedStyle(e), r = e.getBoundingClientRect(); if (!r.width || cs.display === 'none' || cs.visibility !== 'visible' || e.closest('[hidden]')) return;
    let op = 1; for (let x = e; x && x !== h; x = x.parentElement) op *= parseFloat(getComputedStyle(x).opacity);
    const size = parseFloat(cs.fontSize), large = size >= 24 || (size >= 18.66 && parseInt(cs.fontWeight) >= 700);
    out.push({what: (e.getAttribute('class') || e.tagName.toLowerCase()) + ' "' + e.textContent.trim().slice(0, 18) + '"', color: cs.color, op, large,
              sep: !!e.closest('[aria-hidden="true"]'), x: r.left, y: r.top, w: r.width, h: r.height}); });
  return out; }"""

def _lum(c):
    f = lambda v: (v / 255) / 12.92 if v / 255 <= 0.04045 else ((v / 255 + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])

def texts_contrast(pg, pid, label, fails, tag=''):
    """P93: a hero's texts against the pixels under them, as on the home (P92): every text made transparent, the hero
    shot, each text's colour (at the opacity it is drawn with) measured against every pixel in its box: 4.5:1, 3:1 for
    large text. Returns the lowest ratio."""
    from PIL import Image
    import io
    pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(40)
    items = pg.evaluate(HERO_ALL_JS, pid)
    pg.evaluate("""(pid) => { const s = document.createElement('style'); s.id = 'p93hide'; s.textContent = '#' + pid + ' > header.hero *:not(.topo):not(.topo *) {color: transparent !important; text-decoration-color: transparent !important; transition: none !important}'; document.head.appendChild(s); }""", pid)
    pg.wait_for_timeout(50)
    hb = pg.evaluate(f"(() => {{ const r = document.querySelector('#{pid} > header.hero').getBoundingClientRect(); return Math.ceil(r.bottom + scrollY); }})()")
    img = Image.open(io.BytesIO(pg.screenshot(full_page=True, clip=dict(x=0, y=0, width=pg.evaluate('innerWidth'), height=hb)))).convert('RGB')   # the hero whole, past the screen's foot on a short phone
    pg.evaluate("document.getElementById('p93hide').remove()")
    k = img.width / pg.evaluate('innerWidth')
    worst, each = [99, ''], []
    for it in items:
        nums = [float(v) for v in re.findall(r'[\d.]+', it['color'])]
        fg = [v * 255 for v in nums[:3]] if it['color'].startswith('color(') else nums[:3]   # a color-mix() computes as color(srgb r g b), 0 to 1
        a = it['op'] * (nums[3] if len(nums) > 3 else 1)
        box = img.crop((int(it['x'] * k), int(it['y'] * k), int((it['x'] + it['w']) * k), int((it['y'] + it['h']) * k)))
        lo = 99
        for _, c in box.getcolors(box.width * box.height or 1) or []:
            col = [fg[i] * a + c[i] * (1 - a) for i in range(3)]
            l1, l2 = _lum(col), _lum(c)
            lo = min(lo, (max(l1, l2) + .05) / (min(l1, l2) + .05))
        need = 3 if it['large'] else 4.5
        if lo < worst[0]: worst = [round(lo, 2), it['what']]
        each.append(f'{it["what"][:28]} {lo:.2f}/{need:g}')
        if lo < need - .005:
            fails.append(f'{pid} {label}{tag}: {it["what"]} reaches {lo:.2f}:1 over the contours under it (needs {need}:1)')
    print(f'{pid} {label}{tag} ({pg.evaluate("innerWidth")} px): hero texts over the contours, {len(items)} measured pixel by pixel, lowest {worst[0]}:1 ({worst[1]})')
    return worst[0]

def _build_const(name):
    """S-DEC4: a constant of kit/build.py, read from its source (importing build.py would build the site)."""
    import ast
    for n in ast.parse((R / 'build.py').read_text(encoding='utf-8')).body:
        if isinstance(n, ast.Assign) and any(getattr(t, 'id', None) == name for t in n.targets): return ast.literal_eval(n.value)
    raise SystemExit(f'verify.py: no {name} in kit/build.py')
NEW_INTERVAL = _build_const('NEW_INTERVAL')   # words between two of What's new's contour levels
def new_interval(top):
    """P-DEC15: build.py new_interval, repeated (importing build.py would build the site): NEW_INTERVAL for an edition
    whose largest day reaches 10 levels at it, else a tenth of that day, rounded down, at least 1."""
    return NEW_INTERVAL if top >= 10 * NEW_INTERVAL else max(1, int(top) // 10)
_NEW_SAID = []

def check_topo(pg, pid, label, fails, expect, motion=False, phase=True):
    """P93: one page's topography against the sources: the hero's layer (a course home: one rise per unit of the course
    in its order, a written unit by its words, a planned one flat; What's new: one rise per day it lists, oldest first,
    its words that day's; the largest day standing 10 to 25 levels), aria-hidden, no text, at most 20 KB, one layout
    shown (tall below 900 px, wide from it; 1100 before theme 6.22), each written rise closing min(2, levels) rings of its own, in its tone,
    the frame covered at the pose it is in, each rise's own rings inside the frame and above the fade (at 390 px: inside
    the phone's view); every patch 4:1, its lines inside its frame; with motion allowed only transform or opacity
    animating, every drawing at its own point of the cycle; under reduced motion nothing running. Returns the layer's
    info."""
    r = pg.evaluate(TOPO_JS, pid)
    w = pg.evaluate('innerWidth')
    desk = w >= 900   # S-NAV2 step D: every hero's contours the wide layout from 900 px (theme 6.22; 1100 before)
    h = r.get('hero')
    want = None
    if pid == 'new':
        want = [(d, wd) for d, wd in expect['days']]
    elif pid in expect['courses']:
        want = [(k, wd) for k, wd in expect['courses'][pid]['units']]
    elif pid in expect.get('area_pages', {}) and any(wd for _, wd in expect['area_pages'][pid]['rises']):   # S-NAV1 step B: an area page, one rise per course of the track
        want = list(expect['area_pages'][pid]['rises'])
    if want is not None:
        if not h: fails.append(f'{pid} {label}: no topography behind the hero')
        else:
            if h['aria'] != 'true': fails.append(f'{pid} {label}: the hero\'s layer is not aria-hidden')
            if h['text']: fails.append(f'{pid} {label}: the hero\'s layer holds text')
            if h['bytes'] > 20 * 1024: fails.append(f'{pid} {label}: the hero\'s layer is {h["bytes"]} bytes, over 20 KB')
            if h['shown'] != (['wide'] if desk else ['tall']): fails.append(f'{pid} {label}: the layout shown is {h["shown"]}, expected {"wide" if desk else "tall"}')
            for name, rs in h['layouts']:
                got = [(l, wd) for l, wd, _, _, _ in rs]
                if got != want: fails.append(f'{pid} {label}: the {name} layout gives the rises {got[:4]}..., the sources {want[:4]}...')
                for l, wd, k, _, z in rs:
                    if wd and z < min(2, k): fails.append(f'{pid} {label}: the {name} rise {l} closes {z} ring(s) of its own, under {min(2, k)}')
                strokes = [st for _, _, _, st, _ in rs]
                want_t = expect['day_tones'] if pid == 'new' else None
                if pid != 'new' and len(set(strokes)) != 1: fails.append(f'{pid} {label}: the {name} rises are drawn in {set(strokes)}, not the course\'s one tone')
                if pid == 'new' and len(strokes) == len(want_t) and any(pg.evaluate(f"(() => {{ const e = document.createElement('i'); e.style.color = '{c}'; document.body.appendChild(e); const v = getComputedStyle(e).color; e.remove(); return v; }})()") != st for c, st in zip(want_t, strokes)):
                    fails.append(f'{pid} {label}: the days are drawn in {strokes}, not each in the tone of the course that filed the most words that day ({want_t})')
                if pid == 'new':
                    top = max(rs, key=lambda x: x[1] or 0)
                    iv = new_interval(top[1] or 0)
                    if (top[1] or 0) >= 10:   # P93's 10 to 25 levels; P-DEC15: every edition, at its own scale
                        if not 10 <= top[2] <= 25: fails.append(f'{pid} {label}: its largest day ({top[0]}) stands {top[2]} levels, not 10 to 25')
                    if top[2] != int((top[1] or 0) // iv): fails.append(f'{pid} {label}: its largest day ({top[0]}, {top[1]} words) stands {top[2]} levels, not {int((top[1] or 0) // iv)} (a level every {iv:,} words, build.py new_interval)')
                    if iv != NEW_INTERVAL and not _NEW_SAID:
                        _NEW_SAID.append(1)
                        print(f"What's new: edition {EDITION}'s largest day ({top[0]}, {top[1] or 0:,} words) is under {10 * NEW_INTERVAL:,} words, so it is drawn at its own scale, "
                              f"a level every {iv:,} words (build.py new_interval, not NEW_INTERVAL's {NEW_INTERVAL:,}), {int((top[1] or 0) // iv)} levels")
            c = h.get('cover') or {}
            if c.get('bad'): fails.append(f'{pid} {label}: the frame\'s corners {c["bad"]} fall outside the layout {c.get("size")}: an edge of the drawing shows')
            if h.get('outside') and w >= 390: fails.append(f'{pid} {label}: the rises {h["outside"]} have rings outside the frame or in its fade')
            elif h.get('outside') and not motion: print(f'{pid} {label}: below 390 px the rises {h["outside"]} reach past the narrower window (the row sets 390 px)')
    for k, pt in enumerate(r['patches']):
        if pt['aria'] != 'true' or pt['text']: fails.append(f'{pid} {label}: patch {k + 1} is not aria-hidden or holds text')
        if pt.get('lines') and min(pt['lines']) < -.5: fails.append(f'{pid} {label}: patch {k + 1}\'s lines leave its frame by {[-x for x in pt["lines"] if x < 0]} px')
        if pt.get('ratio') and abs(pt['ratio'] - 4) > .05: fails.append(f'{pid} {label}: patch {k + 1} is {pt["ratio"]}:1, not 4:1')
    an = r['anims']
    if motion:
        odd = [a for a in an if any(x not in ('transform', 'opacity') for x in a[1])]
        if odd: fails.append(f'{pid} {label}: an animation runs on more than transform and opacity: {odd[:3]}')
        nt = (1 if h else 0) + r['allPatches']
        sw = [a for a in an if a[3] == SWELL]   # S-NAV1 step D: one swell on each line of each drawing, nothing else moving there
        if len(sw) != r['lines'] or any(a[0] != 'path' for a in sw): fails.append(f'{pid} {label}: {len(sw)} lines swell, the page\'s {nt} contour drawings have {r["lines"]} lines')
        if [a for a in an if a[3] not in (SWELL, 'harea', 'harea-y')]: fails.append(f'{pid} {label}: other animations run: {[a for a in an if a[3] not in (SWELL, "harea", "harea-y")][:3]}')   # S-NAV2 step A: the area words' two
        # each drawing at its own point of the cycle: the phases build.py gives (--ph), at least 0.9 / n apart for the n
        # drawings of the page (P93 follow-up: at a 10 s sweep the measured progress also carried when each drawing was
        # first shown, a fifth of a second for the tiles in History's Planned list opened after the home, so the check
        # reads the phases themselves; the animations' running is checked above)
        phs = sorted(float(x['ph']) for x in ([h] if h else []) + r['patches'] if x.get('ph'))
        close = [(a, b) for a, b in zip(phs, phs[1:]) if b - a < .9 / max(nt, 1)]
        if phase and (close or len(phs) < len(r['patches']) + (1 if h else 0)): fails.append(f'{pid} {label}: drawings share or lack a phase ({close[:3]}; {len(phs)} phases)')
    elif an: fails.append(f'{pid} {label}: under reduced motion {len(an)} animations run: {an[:2]}')
    if want is None and pid != 'home' and pid not in AREA_IDS and r['anyTopo']: fails.append(f'{pid} {label}: a topography on a page that has none')
    return r

def check_tiles(pg, pid, label, fails, expect):
    """P93: every tile of a page the same fields and its own patch, against the sources: a history unit's tile (its
    modules as rises by their words, the modules written, in all and its hours) opens to its module rows; a markdown
    unit's (its sections by their words; sections, words, hours) links to its reading page, or its brief while it is not
    written; a planned course's ghost (the chip, the title, its scope, no stats, one dashed ring); one class set; a line
    of two lines at most while closed; one column below 768 px, two from it (three once the width beside the sidebar
    reaches 960 px), a lone tile half the width; nothing past an edge, no sideways scroll."""
    r = pg.evaluate(TILES_JS, pid)
    w = pg.evaluate('innerWidth')
    fails += [f'{pid} {label}: {b}' for b in r['bad']]
    if r['scroll'][0] > r['scroll'][1]: fails.append(f'{pid} {label}: the page scrolls sideways {r["scroll"]}')
    ts = r['tiles']
    if len({t['cls'] for t in ts}) > 1: fails.append(f'{pid} {label}: the tiles are not one style: {sorted({t["cls"] for t in ts})}')
    for t in ts:
        nm = t['name']
        base = 'div.ctop span.ctitle p' + ('' if t['kind'] == 'ghost' else ' div.cstats') + ' div.topo.topo-patch' + (' svg.chev' if t['kind'] in ('disc', 'ghost') else '')
        if t['kids'] != base: fails.append(f'{pid} {label}: {nm}: the tile holds {t["kids"]}, expected {base}')
        if len(t['chip']) != 2: fails.append(f'{pid} {label}: {nm}: its chip has {len(t["chip"])} parts')
        if t['kind'] != 'ghost' and not t['pill']: fails.append(f'{pid} {label}: {nm}: no status pill')
        if t['kind'] != 'ghost' and len(t['stats']) != 3: fails.append(f'{pid} {label}: {nm}: {len(t["stats"])} stats, expected 3')
        if not t['open'] and t['lines'] > 2: fails.append(f'{pid} {label}: {nm}: its line runs to {t["lines"]} lines')
        if t['open'] and t['clipped']: fails.append(f'{pid} {label}: {nm}: opened, its line is still cut short')
        if t['aria'] != 'true': fails.append(f'{pid} {label}: {nm}: its patch is not aria-hidden')
        if not t['pin'] or abs(t['pw'] / max(t['ph'], 1) - 4) > .06: fails.append(f'{pid} {label}: {nm}: its patch is {t["pw"]} x {t["ph"]}, not 4:1 inside the tile')
        if t['sw']: fails.append(f'{pid} {label}: {nm}: the tile scrolls sideways')
        if t['unseen']: fails.append(f'{pid} {label}: {nm}: the written parts {t["unseen"]} draw no ring of their own (P93 check: a part under one level takes a spot ring)')
        if (t['kind'] == 'ghost') != ('ghost' in t['mods']): fails.append(f'{pid} {label}: {nm}: a ghost tile without the ghost class, or the reverse')
    want = 3 if pg.evaluate('(s => document.body.clientWidth - parseFloat(s.paddingLeft) - parseFloat(s.paddingRight))(getComputedStyle(document.body))') >= 960 else 2   # S-NAV2 step C: three across once the width beside the sidebar reaches 960 px (step D: the body's content box)
    for cols, n, lone, half in r['grids']:
        if w < 768 and cols != 1: fails.append(f'{pid} {label}: a tile grid in {cols} columns below 768 px')
        if w >= 768 and cols != want: fails.append(f'{pid} {label}: a tile grid in {cols} column(s) from 768 px, expected {want}')
        if w >= 768 and lone is not None and abs(lone - half) > 2: fails.append(f'{pid} {label}: a lone tile {lone} px wide, half the grid is {half}')
    e = expect['courses'].get(pid)
    if e:
        units = [t for t in ts if t['kind'] in ('disc', 'link') or (t['kind'] == 'other')]
        if len(units) != len(e['tiles']): fails.append(f'{pid} {label}: {len(units)} unit tiles, the sources give {len(e["tiles"])} units')
        for t, (code, parts) in zip(units, e['tiles']):
            if e['family'] == 'history':
                want_r = [(m, wd) for m, wd in parts if wd]
                want_p = [m for m, wd in parts if wd is None]
                done = len(want_r)
                if t['kind'] != 'disc': fails.append(f'{pid} {label}: {code}: a history unit tile that is not a disclosure')
                if t['rows'] != len(parts): fails.append(f'{pid} {label}: {code}: {t["rows"]} module rows, {len(parts)} modules')
                if [x[0] for x in t['stats']] != [str(done), str(len(parts)), f'{sum(wd for _, wd in want_r) / 250 / 60:.1f}']: fails.append(f'{pid} {label}: {code}: its stats read {t["stats"]}')
            else:
                want_r = [(f'{code} §{j + 1}', wd) for j, wd in enumerate(parts or [])]
                want_p = [] if parts else [code]
                href = '#' + (e['pages'][code] if parts else e['briefs'][code])
                if t['kind'] != 'link' or t['href'] != href: fails.append(f'{pid} {label}: {code}: the tile links to {t["href"]}, expected {href}')
                ww = sum(parts or [])
                if [x[0] for x in t['stats']] != [str(len(parts or [])), f'{ww:,}', f'{ww / 250 / 60:.1f}']: fails.append(f'{pid} {label}: {code}: its stats read {t["stats"]}')
            if [tuple(x) for x in t['rises'] or []] != want_r: fails.append(f'{pid} {label}: {code}: its patch gives {t["rises"]}, the sources {want_r}')
            if ('pending' in t['mods']) != (not want_r): fails.append(f'{pid} {label}: {code}: marked pending {"pending" in t["mods"]}, but {len(want_r)} of its parts are written')
            if (t['plan'] or []) != want_p: fails.append(f'{pid} {label}: {code}: its patch marks {t["plan"]} planned, the sources {want_p}')
    if pid == 'home' or pid in AREA_IDS:   # S-NAV1 step B: with area pages, each area page holds its track's planned courses and the home none
        gh = [t for t in ts if t['kind'] == 'ghost']
        plans = [n[1] for t in THEMES if pid == 'home' or pid == 'track-' + t['id'] for n in t.get('planned', [])]   # S-SPORTS: a track's own planned courses; P-DEC12: History's too (catalog.toml `next` before)
        if (MULTI and pid == 'home') or 'planned' in OMIT: plans = []
        if (gh or pid in AREA_IDS) and [t['name'] for t in gh] != plans: fails.append(f'{pid} {label}: the ghost tiles are {[t["name"] for t in gh]}, courses.py plans {plans}')
        for t in gh:
            if t['stats'] or t['rises'] or len(t['plan'] or []) != 1: fails.append(f'home {label}: the ghost {t["name"]} shows stats {t["stats"]} or rises, or not one dashed ring ({t["plan"]})')
    return r

# S-NAV1 step B (21 Nov 2026): an area page (track-<id>), read on the shown page at one width: the breadcrumbs (the
# site, then the area, current), the eyebrow AREA, the area's name and lede, three stats; its hero's layer (check_topo
# holds it against the sources); then the track's band: its live courses' tiles in catalog order, each the link to its
# course, its own copy (catalog.toml `extra`) and its folded planned list; nothing sideways. And the home's tile for it:
# its three stats are the band's: its course tiles, their units written and in all.
AREA_JS = r"""(pid) => {
  const P = document.getElementById(pid), out = {bad: []}, bad = out.bad;
  if (!P || P.hidden) { bad.push('not shown'); return out; }
  const hero = P.querySelector(':scope > header.hero.has-topo');
  if (!hero) bad.push('no hero over a topography (header.hero.has-topo)');
  const cr = P.querySelector('.hero .crumbs');
  out.crumbs = cr ? [...cr.children].filter(e => !e.classList.contains('sep')).map(e => [e.textContent, e.getAttribute('href')]) : null;
  out.eyebrow = (P.querySelector('.hero .eyebrow .u') || {}).textContent || null;
  out.h1 = (P.querySelector('.hero h1') || {}).textContent || null;
  out.lede = (P.querySelector('.hero .lede') || {}).textContent || null;
  out.stats = [...P.querySelectorAll('.hero .stats > div > b')].map(b => b.textContent);
  out.kids = [...P.children].map(e => e.tagName.toLowerCase() + '.' + [...e.classList].join('.')).join(' ');
  const band = P.querySelector(':scope > section.track');
  out.tiles = band ? [...band.querySelectorAll(':scope > .cgrid > a.course.live')].map(a => [a.getAttribute('href'), a.getAttribute('data-target'), [...a.querySelectorAll('.cstats > span > b')].map(b => b.textContent)]) : [];
  out.extra = band ? !!band.querySelector(':scope > details.howto.rules:not(.planned)') : false;
  out.plan = band ? [...band.querySelectorAll(':scope > details.planned')].map(d => d.id) : [];
  const home = document.querySelector('#home a.course.live[data-target="' + pid + '"]');
  out.homeTile = home ? [...home.querySelectorAll('.cstats > span > b')].map(b => b.textContent) : null;
  const de = document.documentElement; if (de.scrollWidth > de.clientWidth) bad.push(`the page scrolls sideways (${de.scrollWidth} in ${de.clientWidth} px)`);
  return out;
}"""

def check_area(pg, pid, label, fails, expect):
    """S-NAV1 step B: one area page against catalog.toml and the sources (AREA_JS), and the home's tile for it."""
    pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(80)
    e = expect['area_pages'][pid]
    t = next(x for x in THEMES if 'track-' + x['id'] == pid)
    r = pg.evaluate(AREA_JS, pid)
    fails += [f'{pid} {label}: {b}' for b in r['bad']]
    if r.get('crumbs') != [[SITE_NAME, '#home'], [e['name'], None]]: fails.append(f'{pid} {label}: the breadcrumbs are {r.get("crumbs")}, expected {SITE_NAME} › {e["name"]}')
    if r.get('eyebrow') != 'AREA' or r.get('h1') != e['name'] or r.get('lede') != e['lede']: fails.append(f'{pid} {label}: the hero reads {r.get("eyebrow")!r}, {r.get("h1")!r}, {(r.get("lede") or "")[:40]!r}; expected AREA, its name and its lede')
    if r.get('kids') != 'header.hero.has-topo section.track': fails.append(f'{pid} {label}: the page holds {r.get("kids")}, expected the hero and the track\'s band')
    got = [h for h, _, _ in r.get('tiles', [])]
    if got != ['#' + c for c in e['courses']] or any(h != '#' + tg for h, tg, _ in r.get('tiles', [])): fails.append(f'{pid} {label}: the course tiles link to {got}, the sources give {e["courses"]}')
    if t.get('extra') and not r.get('extra'): fails.append(f'{pid} {label}: lost its own copy ({t["extra"]})')
    want_plan = [t.get('planned_anchor', 'planned-' + t['id'])] if t.get('planned') and 'planned' not in OMIT else []
    if r.get('plan') != want_plan: fails.append(f'{pid} {label}: its folded planned lists are {r.get("plan")}, expected {want_plan}')
    sums = [str(len(r.get('tiles', []))), str(sum(int(s[0]) for _, _, s in r.get('tiles', []))), str(sum(int(s[1]) for _, _, s in r.get('tiles', [])))]
    if r.get('homeTile') != sums: fails.append(f'{pid} {label}: the home\'s tile counts {r.get("homeTile")}, its band holds {sums} (courses, units written, in all)')
    if (r.get('stats') or [None])[:2] != sums[:2]: fails.append(f'{pid} {label}: the hero\'s stats read {r.get("stats")}, its band holds {sums[:2]} (courses, units written)')
    print(f'{pid} {label}: crumbs {" › ".join(x for x, _ in r.get("crumbs") or [])}; {len(got)} course tiles; copy {r.get("extra")}; planned {r.get("plan")}; home tile {r.get("homeTile")}; stats {r.get("stats")}')
    return r

# P91: What's new (#new), fetched through the shell: every dated unit and every course start once, newest first,
# grouped by day under the day's heading, each row linking to a page that exists, approximate dates marked
NEW_JS = r'''() => {
  const p = document.getElementById('new'), bad = [], out = {bad};
  const resolves = t => !!document.getElementById(t) || [...document.querySelectorAll('.panel[data-anchors]')].some(q => (' ' + q.getAttribute('data-anchors') + ' ').includes(' ' + t + ' '));
  const crumbs = p.querySelector('.hero .crumbs'), cr = crumbs ? [...crumbs.children].filter(e => !e.classList.contains('sep')).map(e => e.textContent).join(' › ') : '';
  if (cr !== __SITE__ + " › What's new") bad.push(`the breadcrumbs read "${cr}", not ${__SITE__} › What's new`);
  if (!p.querySelector('.hero h1') || p.querySelector('.hero h1').textContent !== "What's new") bad.push('no "What\'s new" title');
  const days = [...p.querySelectorAll(':scope > section.newday')];
  out.days = days.map(d => d.getAttribute('data-day'));
  out.rows = [];
  days.forEach(d => { const day = d.getAttribute('data-day'), hd = d.querySelector(':scope > h2');
    if (!hd || !hd.textContent.trim()) bad.push(`the day ${day} has no heading`);
    d.querySelectorAll('a.hrow').forEach(r => { const t = r.getAttribute('data-target');
      out.rows.push([r.getAttribute('data-kind'), t, r.getAttribute('data-date'), r.hasAttribute('data-approx'), !!r.querySelector('.approx'), r.getAttribute('href') === '#' + t]);
      if (r.getAttribute('data-date') !== day) bad.push(`#${t} sits under ${day} but is dated ${r.getAttribute('data-date')}`);
      if (!resolves(t)) bad.push(`a row links to #${t}, no page`);
      if (!r.querySelector('.pill') || !r.querySelector('.t small')) bad.push(`#${t}: a row without its pill or its course and model line`); }); });
  if (new Set(out.days).size !== out.days.length) bad.push('a day appears twice');
  for (let i = 1; i < out.days.length; i++) if (out.days[i] >= out.days[i - 1]) { bad.push(`the days are not newest first (${out.days[i - 1]} then ${out.days[i]})`); break; }
  const de = document.documentElement; if (de.scrollWidth > de.clientWidth) bad.push(`the page scrolls sideways (${de.scrollWidth} in ${de.clientWidth} px)`);
  return out;
}'''
NEW_JS = NEW_JS.replace('__SITE__', SITE_JSON)   # S-DEC3: the brand's site name, as a JS string

def check_new(pg, label, fails, expect):
    """P91: What's new against home_expect()'s rows: each once, in order, grouped by day, approximate dates marked."""
    pg.evaluate("location.hash = 'new'"); ready(pg); pg.wait_for_timeout(80)
    r = pg.evaluate(NEW_JS)
    fails += [f"what's new {label}: {b}" for b in r['bad']]
    got = [(k, t) for k, t, *_ in r['rows']]
    want = [(x['kind'], x['pid']) for x in expect['rows']]
    if len(set(got)) != len(got): fails.append(f"what's new {label}: a row appears twice")
    if got != want: fails.append(f"what's new {label}: {len(got)} rows, first {got[:4]}; the sources give {len(want)}, first {want[:4]}")
    ap = {x['pid'] for x in expect['rows'] if x['approx'] and x['kind'] == 'unit'}
    apc = {x['pid'] for x in expect['rows'] if x['approx'] and x['kind'] == 'course'}
    for k, t, d, da, mark, hr in r['rows']:
        if (t in (ap if k == 'unit' else apc)) != da: fails.append(f"what's new {label}: #{t} ({k}) marked approximate {da}, the sources say {not da}")
        if da != mark: fails.append(f"what's new {label}: #{t} carries data-approx {da} but its ≈ mark {mark}")
        if not hr: fails.append(f"what's new {label}: #{t}'s href is not its target")
    print(f"what's new {label}: {sum(1 for x in r['rows'] if x[0] == 'unit')} unit rows, {sum(1 for x in r['rows'] if x[0] == 'course')} course rows, "
          f"{sum(1 for x in r['rows'] if x[3])} approximate, on {len(r['days'])} days")

# P90: WCAG contrast of every text against the background it sits on, the light theme's tokens in use. A text's colour
# is composited with its alpha and the opacity of its ancestors; its background is every background colour under it
# (a tint over a card over the page) composited from the page up. SVG text (figures) is left out.
CONTRAST_JS = r'''(scope) => {
  const parse = c => {
    let m = c.match(/^rgba?\(([^)]+)\)/);
    if (m) { const v = m[1].split(/[\s,\/]+/).filter(Boolean).map(Number); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; }
    m = c.match(/^color\(srgb ([^)]+)\)/);
    if (m) { const v = m[1].split(/[\s\/]+/).filter(Boolean).map(Number); return [v[0] * 255, v[1] * 255, v[2] * 255, v.length > 3 ? v[3] : 1]; }
    return null; };
  const over = (a, b) => [0, 1, 2].map(i => a[i] * a[3] + b[i] * (1 - a[3])).concat([1]);
  const lum = c => { const f = v => { v /= 255; return v <= 0.04045 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }; return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2]); };
  const ratio = (a, b) => { const x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); };
  const hex = c => '#' + c.slice(0, 3).map(v => Math.round(v).toString(16).padStart(2, '0')).join('');
  const roots = [...document.querySelectorAll(scope)];
  const bad = []; let n = 0, min = 99, minAt = '';
  roots.forEach(root => root.querySelectorAll('*').forEach(el => {
    if (el.closest('svg')) return;
    if (![...el.childNodes].some(t => t.nodeType === 3 && t.textContent.trim())) return;
    const cs = getComputedStyle(el); if (cs.visibility !== 'visible') return;
    const r = el.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return;
    if (el.closest('[disabled]')) return;
    let fg = parse(cs.color); if (!fg) return;
    let op = 1, bgs = [];
    for (let e = el; e; e = e.parentElement) {
      const s = getComputedStyle(e); op *= parseFloat(s.opacity);
      const b = parse(s.backgroundColor); if (b && b[3] > 0) { bgs.push(b); if (b[3] >= 1) break; }
    }
    let bg = [255, 255, 255, 1];
    for (let i = bgs.length - 1; i >= 0; i--) bg = i === bgs.length - 1 && bgs[i][3] >= 1 ? bgs[i] : over(bgs[i], bg);
    const col = over([fg[0], fg[1], fg[2], fg[3] * op], bg);
    const size = parseFloat(cs.fontSize), large = size >= 24 || (size >= 18.66 && parseInt(cs.fontWeight) >= 700);
    const k = ratio(col, bg), need = large ? 3 : 4.5; n++;
    const d = el.tagName.toLowerCase() + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/).join('.') : '');
    if (k < min) { min = k; minAt = d; }
    if (k < need - 0.005) bad.push(`${d} "${el.textContent.trim().slice(0, 24)}" ${hex(col)} on ${hex(bg)} ${k.toFixed(2)}:1`);
    if (fg[0] > 254.5 && fg[1] > 254.5 && fg[2] > 254.5) bad.push(`${d} "${el.textContent.trim().slice(0, 24)}" is pure white text (P90: none in light)`);
    if (bgs.some(c => c[0] > 254.5 && c[1] > 254.5 && c[2] > 254.5 && c[3] > 0)) bad.push(`${d} "${el.textContent.trim().slice(0, 24)}" sits on pure white (P90: none in light)`);
  }));
  return {n, min: Math.round(min * 100) / 100, minAt, bad: [...new Set(bad)].slice(0, 12), nbad: new Set(bad).size};
}'''

def check_contrast(pg, fails):
    """P90: the light theme's contrast on the home, the drawer, the changelog and backlog, each course home and the
    first reading page of each course, at phone width, every <details> open."""
    pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')"); pg.wait_for_timeout(50)
    firsts = pg.evaluate("""() => { const seen = {}, out = []; document.querySelectorAll('.panel[data-kind="report"]').forEach(p => {
      const c = p.getAttribute('data-ctx'); if (!seen[c]) { seen[c] = 1; out.push(p.id); } }); return out; }""")
    homes = pg.evaluate("[...document.querySelectorAll('.panel[data-kind=\"course\"]')].map(p => p.id)")
    pids = SCOPE.only([x for x in ['home', 'new', 'changelog', 'backlog', 'coming'] if x not in OMIT] + AREA_IDS + homes + firsts)   # S-NAV1 step B: the area pages   # P91: What's new   # S-DEC4: the run's pages
    worst, total = [99, ''], 0
    for pid in pids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(40)
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) .stepbar .whole[aria-pressed=\"false\"]').forEach(b => b.click())")
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) details').forEach(d => d.open = true)"); pg.wait_for_timeout(40)
        r = pg.evaluate(CONTRAST_JS, f'#{pid}')
        total += r['n']
        if r['min'] < worst[0]: worst = [r['min'], f'{pid} {r["minAt"]}']
        if r['nbad']: fails.append(f'contrast light {pid}: {r["nbad"]} texts under 4.5:1 (3:1 large): ' + '; '.join(r['bad']))
    pg.click('#menuB'); pg.wait_for_timeout(250)
    # S-NAV1 step C: every group of the sub-nav shown at once (each area's, each course's), so every nav text is measured
    pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed')); document.querySelectorAll('#drawer details').forEach(d => d.open = true); document.querySelectorAll('#drawer .sub-nav, #drawer .sub-nav [data-navctx]').forEach(n => n.hidden = false)")
    r = pg.evaluate(CONTRAST_JS, '#drawer'); total += r['n']
    if r['min'] < worst[0]: worst = [r['min'], f'drawer {r["minAt"]}']
    if r['nbad']: fails.append(f'contrast light drawer: {r["nbad"]} texts under 4.5:1: ' + '; '.join(r['bad']))
    pg.click('#closeB'); pg.wait_for_timeout(250)
    pg.evaluate(f"localStorage.removeItem('{THEME_KEY}'); document.documentElement.removeAttribute('data-theme')")
    print(f'contrast (light, phone): {total} texts on {len(pids)} panels and the drawer, lowest {worst[0]}:1 ({worst[1]})')

SHOT_H = 2600
def shoot(pg, path, w, h):
    """The top SHOT_H px of the page (P35, 1 Nov 2026). A full-page capture renders the whole document before it clips,
    which on a long unit at device scale 3 took 80 s (DD-B3, about 10,300 words) and failed past the timeout on longer
    pages; the viewport is made SHOT_H tall and captured as it is, then put back, so the time no longer grows with the
    page."""
    pg.set_viewport_size({'width': w, 'height': SHOT_H}); pg.wait_for_timeout(120)
    pg.screenshot(path=str(path), full_page=False, timeout=60000)
    pg.set_viewport_size({'width': w, 'height': h}); pg.wait_for_timeout(60)

def frames(pg, fig, path, label):
    """P89 (2 Nov 2026; p85_frames.py folded in): every frame a reader scrolls a figure across, shot in turn and stacked
    top to bottom with its number, so a checker sees the whole drawing as the reader meets it. The frames run from where
    the drawing starts (data-x0px, set by shell.js on a centred drawing, else 0) to its right edge, each half a frame
    on from the last, so anything up to half a frame wide (a box, a label) is whole in at least one frame, as it is to a
    reader who scrolls on; a figure that fits its frame is one frame. While they are shot,
    sticky bars are made static (they keep their place in the flow) and fixed ones hidden, so none covers the figure;
    both are put back after and the frame is scrolled back to where it opened. Returns the number of frames."""
    from PIL import Image, ImageDraw, ImageFont
    sc = fig.query_selector('.viz-scroll')
    if not sc:
        return 0
    pg.evaluate("""() => { for (const el of document.querySelectorAll('body *')) { const p = getComputedStyle(el).position;
      if (p === 'sticky' && !el.closest('.viz-scroll')) { el.dataset.p89 = 's'; el.style.setProperty('position', 'static', 'important'); }   // P83: a figure's own label column stays sticky, so the sheets show it as the reader sees it
      else if (p === 'fixed') { el.dataset.p89 = 'f'; el.style.setProperty('visibility', 'hidden', 'important'); } } }""")
    fig.scroll_into_view_if_needed(); pg.wait_for_timeout(60)
    sw, cw, x_open, x0 = sc.evaluate("s => [s.scrollWidth, s.clientWidth, s.scrollLeft, +s.getAttribute('data-x0px') || 0]")
    x, xs, shots = min(x0, x_open), [], []
    # W-BW8 (16 Nov 2026): beside a sticky label column (and its 36 px fades) the clear room is narrower than the frame; the
    # step is a third of that room, so a matrix column up to two thirds of it is clear of both fades in at least one frame
    # (BW8 figure 4's Desktop column was under a fade in every half-frame stop at 360 and 390 px)
    stick = sc.evaluate("s => { for (const e of s.children) if (e.matches('.viz-stick,.viz-stickn') && getComputedStyle(e).display !== 'none') return e.getBoundingClientRect().width; return 0; }")
    step = max(cw // 2, 1) if not stick else max((cw - int(stick) - 72) // 3, 16)
    while True:
        sc.evaluate(f's => {{ s.scrollLeft = {x}; }}'); pg.wait_for_timeout(120)
        x = sc.evaluate('s => s.scrollLeft'); xs.append(x)
        tmp = path.with_name(f'_{path.stem}-{len(shots)}.png')
        fig.screenshot(path=str(tmp), timeout=120000); shots.append(tmp)
        if x + cw >= sw - 1 or len(shots) >= 60:
            break
        x = min(x + step, sw - cw)
    sc.evaluate(f's => {{ s.scrollLeft = {x_open}; }}')
    pg.evaluate("() => { for (const el of document.querySelectorAll('[data-p89]')) { el.style.removeProperty(el.dataset.p89 === 's' ? 'position' : 'visibility'); delete el.dataset.p89; } }")
    ims = [Image.open(s) for s in shots]
    scale = max(1, round(ims[0].width / fig.evaluate('f => f.getBoundingClientRect().width')))   # the device scale
    font, band = ImageFont.load_default(size=12 * scale), 40 * scale
    sheet = Image.new('RGB', (max(i.width for i in ims), sum(i.height + band for i in ims)), (128, 128, 128))
    d, y, n = ImageDraw.Draw(sheet), 0, len(ims)
    for k, (im, xk) in enumerate(zip(ims, xs)):
        note = 'the whole figure fits' if n == 1 else f'scrolled to {xk} of {sw - cw} px; opens at {x_open}'
        d.text((6 * scale, y + 4 * scale), label, fill=(0, 0, 0), font=font)
        d.text((6 * scale, y + 21 * scale), f'frame {k + 1} of {n} ({note})', fill=(0, 0, 0), font=font)
        y += band; sheet.paste(im, (0, y)); y += im.height
    sheet.save(path)
    for s in shots:
        s.unlink()
    return n

def check_panels(pg, label, fails):
    """Every panel, every <details> open: horizontal scroll, 6 px gaps, 44 px targets. Returns (tightest gap, panel count)."""
    ids = SCOPE.only(pg.eval_on_selector_all('.panel', 'ps => ps.map(p => p.id)'))   # S-DEC4: the run's pages
    worst, frames, figs = [], [0, 0], [0, 0]
    for pid in ids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(30)
        if pg.evaluate(f"document.getElementById('{pid}').hasAttribute('data-failed')"): fails.append(f'{label} {pid}: the report did not load')
        # P68: a reading page is measured whole (its "Whole unit" toggle), so every section is checked as before
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) .stepbar .whole[aria-pressed=\"false\"]').forEach(b => b.click())")
        pg.evaluate("document.querySelectorAll('.panel:not([hidden]) details').forEach(d => d.open = true)")
        sw = pg.evaluate('[document.documentElement.scrollWidth, document.documentElement.clientWidth]')
        if sw[0] > sw[1]: fails.append(f'{label} {pid}: horizontal scroll {sw}')
        res = pg.evaluate(BOX_JS, [f'#{pid}', GAP])
        if res['nbad']: fails.append(f'{label} {pid}: {res["nbad"]} boxes closer than {GAP}px: ' + '; '.join(res['bad']))
        if label.startswith('phone') or label == 'desktop':
            fr = pg.evaluate(FRAME_JS, [f'#{pid}', label.startswith('phone')])
            frames[0] += fr['n']; frames[1] += fr['over']
            if fr['bad']: fails.append(f'{label} {pid}: figure frames: ' + '; '.join(fr['bad']))
        if label == 'phone':   # P55: the figure geometry (FIG_JS) of every figure on every panel, once (it does not depend on the width)
            fg = pg.evaluate(FIG_JS, f'#{pid}')
            figs[0] += fg['n']; figs[1] += fg['n'] > 0
            if fg['bad']: fails.append(f'{label} {pid}: figure geometry: ' + '; '.join(fg['bad'][:8]))
        small = pg.evaluate(TARGET_JS, f'#{pid}')
        if small: fails.append(f'{label} {pid}: {len(small)} targets under 44px: ' + '; '.join(small[:6]))
        worst.append((res['min'], pid, res['n']))
    m = min(worst)
    print(f'{label}: panels checked: {len(ids)}; tightest stacked gap {m[0]}px ({m[1]})'
          + (f'; {frames[0]} figure frames at natural size, {frames[1]} scrolling with the cue' + (f'; geometry of {figs[0]} figures on {figs[1]} panels checked' if label == 'phone' else '') if label.startswith('phone') else
             f'; {frames[0]} figure frames, {frames[1]} wider than their frame with the cue, the rest without' if label == 'desktop' else ''))
    return m[0], len(ids)

FONTS = R / 'fonts'
# S-DEC4: the vendored faces the edition's theme uses: design/theme.css --sans, --mono and --serif, as the brand's [tokens]
# leaves or sets them (P39: Academy's three). A face a brand names that is not vendored is never served here (the browser
# draws its fallback); the desktop pass says so
_TOK = {}
for _k, _v in re.findall(r'^\s*--(sans|mono|serif)\s*:\s*([^;]+);', (R.parent / 'design' / 'theme.css').read_text(), re.M): _TOK.setdefault(_k, _v)
_TOK.update({k: v for k, v in (brand(EDITION).get('tokens') or {}).items() if k in ('sans', 'mono', 'serif')})
# P-DEC5: fonts.css holds the theme's own faces; a brand's other faces are each a fonts/<face>.css of their own, added
# when the edition's tokens name its family (so an edition that names none serves fonts.css alone, as before)
_FAM = lambda css: re.findall(r"font-family:\s*'([^']+)'", css)
FONT_CSS = (FONTS / 'fonts.css').read_text() + ''.join(
    css for f in sorted(FONTS.glob('*.css')) if f.name != 'fonts.css'
    for css in [f.read_text()] if any(fam in v for fam in set(_FAM(css)) for v in _TOK.values()))
VENDORED = list(dict.fromkeys(re.findall(r"font-family:\s*'([^']+)'", FONT_CSS)))
THEME_FONTS = [f for f in VENDORED if any(f in v for v in _TOK.values())]
UNSERVED = [v.split(',')[0].strip().strip('"\'') for v in _TOK.values() if not any(f in v for f in VENDORED)]
def font_file(route):
    f = FONTS / route.request.url.rsplit('/', 1)[1]
    if '/learning-vendored/' in route.request.url and f.suffix == '.woff2' and f.exists():
        route.fulfill(status=200, content_type='font/woff2', body=f.read_bytes(), headers={'Access-Control-Allow-Origin': '*'})
    else:
        route.abort()

def new_page(p, br, errors, name, w, h, mobile, motion=False):
    ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=3 if mobile else 1,
                         is_mobile=mobile, has_touch=mobile,  # a real phone or tablet honours the viewport tag
                         color_scheme='dark',                 # P92: the site's default theme; a pass without the toggle is dark (Playwright's default system setting is light, so every 'dark' pass before P92 measured the light theme)
                         reduced_motion='no-preference' if motion else 'reduce')   # P91: every measure and shot sees the home at rest; P92: one pass with motion allowed
    # the theme fonts, from the vendored copy in fonts/ (P39): the page measures and draws what a reader's phone does
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
    ctx.route('**/fonts.gstatic.com/**', font_file)
    pg = ctx.new_page()
    pg.on('console', lambda m: errors.append(f'{name}: {m.text}') if m.type == 'error' else None)
    pg.on('pageerror', lambda e: errors.append(f'{name}: {e}'))
    pg.goto(URL + '#home'); pg.wait_for_timeout(300)
    lay = pg.evaluate('[document.documentElement.clientWidth, visualViewport.scale]')
    return ctx, pg, lay

def check_files(fails):
    """The split on disk: every stub's file exists, nothing in academy/ is unreferenced, the shell is under 1 MB, and
    README.md's size table is the one build.py would write for these files."""
    shell = (SITE / 'index.html').read_text()
    heads = re.findall(r'<section class="panel[^"]*"[^>]*>', shell)
    srcs = [m.group(1) for h in heads for m in [re.search(r' data-src="([^"]+)"', h)] if m]
    # every report and syllabus panel, a markdown course's briefs and bibliography pages, every course home (P22 the
    # history homes; P93 the markdown ones, whose unit tiles and topography would have filled the shell) and every
    # course's "How it was built" page leave the shell (A2, P20, P22, A4, P93)
    must = [h for h in heads if ' data-kind="report"' in h or ' data-kind="syllabus"' in h or re.search(r' id="(briefs-[a-z]+|[a-z-]+-briefs|[a-z-]+-bibliography|[a-z-]+-built)"', h)
            or ' data-kind="course"' in h or ' id="viz-examples"' in h or ' id="new"' in h or ' id="changelog"' in h]   # G-0: the changelog too   # P91: What's new is fetched too; P93: every course home, a markdown course's too
    kept = [h[:80] for h in must if ' data-src="' not in h]
    if kept: fails.append(f'split: {len(kept)} panels should be fetched but are in the shell: {kept[:2]}')
    if len(srcs) != len(must): fails.append(f'split: {len(must)} panels should be fetched but {len(srcs)} carry data-src')
    noanch = [h[:80] for h in must if ' data-src="' in h and ' data-kind="report"' not in h and ' data-anchors="' not in h]
    if noanch: fails.append(f'split: fetched panels without data-anchors: {noanch[:2]}')
    stubs = re.findall(r'(<section class="panel[^"]*"[^>]* data-src="[^"]+"[^>]*>)(.*?)</section>', shell, re.S)
    for h in heads:                                          # P24 (16 Nov 2026): every How-it-was-built page says its audit files are private
        m = re.search(r' id="([a-z0-9-]+-built)"[^>]* data-src="([^"]+)"', h)
        if m and (SITE / m.group(2)).exists():
            pg = (SITE / m.group(2)).read_text(); i, j = pg.find('data-private=""'), pg.find(brand(EDITION)['repo'] + '/')   # S-DEC3: the brand's repo link base
            if i < 0 or (j >= 0 and j < i):
                fails.append(f'{m.group(1)}: no line saying its audit files are private above its first file link (P24)')
    full = [h for h, body in stubs if body.strip()]
    if full: fails.append(f'split: {len(full)} stubs still hold content: {full[0][:80]}')
    on_disk = sorted(str(f.relative_to(SITE)) for f in SITE.rglob('*.html') if f.name != 'index.html')
    missing = sorted(set(srcs) - set(on_disk)); orphans = sorted(set(on_disk) - set(srcs))
    if missing: fails.append(f'split: {len(missing)} fetched files missing: {missing[:3]}')
    if orphans: fails.append(f'split: {len(orphans)} files in academy/ no stub fetches: {orphans[:3]}')
    if any(re.search(r'<(style|script|html|body)\b', (SITE / x).read_text(), re.I) for x in on_disk): fails.append('split: a fetched file carries a style, script or document tag')
    size = len(shell.encode())
    if size >= SHELL_MAX: fails.append(f'split: shell is {size:,} bytes, over the 1 MB limit')
    by = {}
    for x in on_disk:
        by.setdefault(x.split('/')[0] if '/' in x else '.', []).append((len((SITE / x).read_bytes()), x))   # V1: root pages under ./
    table = re.search(r'<!-- sizes:start -->\n(.*?)<!-- sizes:end -->', (R / 'README.md').read_text(), re.S) if EDITION == DEFAULT_EDITION else True
    kb = lambda n: f'{n / 1024:,.0f} KB' if n < 1024 * 1024 else f'{n / 1024 / 1024:.2f} MB'
    if not table: fails.append('README.md has no size table (sizes:start/sizes:end)')
    elif table is True: print(f'edition {EDITION}: no size table (README.md keeps the default edition\'s)')
    else:
        rows = {r.split(' | ')[0].strip('| '): r for r in table.group(1).splitlines()}
        want = {'Shell (`index.html`)': f'| 1 | {kb(size)} | {kb(size)} |'}
        for ctx, fs in by.items():
            want[next((k for k in rows if f'(`{ctx}/`)' in k), ctx)] = f'| {len(fs)} | {kb(sum(n for n, _ in fs))} | {kb(max(fs)[0])} | largest `{max(fs)[1]}`'
        bad = [k for k, v in want.items() if k not in rows or v not in rows[k]]
        if bad: fails.append(f'README.md size table does not match the files: {bad} (rebuild)')
    vx = SITE / 'viz-examples.html'   # V1: the figure examples page, one figure of every kind in viz.py
    if 'figures' in OMIT:
        if vx.exists(): fails.append(f'edition {EDITION}: viz-examples.html is built though the edition leaves it out')
    elif not vx.exists(): fails.append('viz-examples.html: missing (viz_examples.py, run from build.py)')
    else:
        nfig = len(re.findall(r'<figure class="viz ', vx.read_text()))
        if nfig != VX_FIGS: fails.append(f'viz-examples.html: {nfig} figures, expected {VX_FIGS}')
        print(f'viz-examples.html: {nfig} figures')
    big = max((n, x) for fs in by.values() for n, x in fs)
    print(f'split: shell {size / 1024:,.0f} KB (limit 1,024 KB), {len(on_disk)} fetched files in {len(by)} folders, largest {big[1]} {big[0] / 1024:,.0f} KB')
    for ctx, fs in by.items():
        print(f'  {ctx + "/":10} {len(fs):3} files {sum(n for n, _ in fs) / 1024:7,.0f} KB, largest {max(fs)[1]} {max(fs)[0] / 1024:,.0f} KB')

# P58 (30 Oct 2026): the drawing faults the Greek retrofit's checkers met, read from every built figure on every page
# (the shell and each fetched file), so a figure that would show one fails the build. See viz.py's P58 contract.
QUAL = re.compile(r'(?:^|[\s(\[])(c\.|ca\.|by|after|before|from|until)$', re.I)
TEXT_RE = re.compile(r'<text class="([\w-]+)" x="([-\d.]+)" y="([-\d.]+)"[^>]*>(.*?)</text>', re.S)
def _texts(svg):
    import html as H
    return [(m.group(1), float(m.group(2)), float(m.group(3)), H.unescape(re.sub(r'<[^>]+>', '', m.group(4)))) for m in TEXT_RE.finditer(svg)]
def _year(t):
    """A tick label as a signed year (P63): 750 BC or 750 BCE is -750, AD 14 or 14 CE is 14, 1453 is 1453."""
    m = re.fullmatch(r'(\d+) (BC|BCE)', t.strip()) or re.fullmatch(r'(?:AD )?(\d+)(?: CE)?', t.strip())
    return None if not m else -int(m.group(1)) if m.re.pattern.endswith('BCE)') else int(m.group(1))
PHONE_FRAME = 358                                      # P79: a 390 px phone's figure frame (16 px gutters)
def figure_rules(page, name):
    """The P58 faults (and P63's date lines) in one built page's figures, as messages (empty when it has none)."""
    import html as H
    bad, n = [], 0
    prose = re.sub(r'<figure class="viz.*?</figure>', '', page, flags=re.S)
    prose = re.sub(r'<div class="process">.*?<div class="pager">', '', prose, flags=re.S)   # P68: the text, not its sources
    bce = len(re.findall(r'\bBCE\b', prose)) > len(re.findall(r'\bBC\b', prose))
    for m in re.finditer(r'<figure class="viz viz-([\w-]+)[^"]*">(.*?)</figure>', page, re.S):
        kind, svg = m.group(1), m.group(2); n += 1
        where, tx = f'{name} figure {n} ({kind})', _texts(svg)
        if kind == 'timeline':
            for (c1, x1, y1, t1), (c2, x2, y2, t2) in zip(tx, tx[1:]):
                if c1 == c2 == 'viz-label' and x1 == x2 and 0 < y2 - y1 < 20 and QUAL.search(t1) and re.match(r'[(\[]?\d', t2):
                    bad.append(f'{where}: a wrapped event label parts "{t1.split()[-1]}" from its number ("{t1}" / "{t2}")')
            for i, (c, x, y, t) in enumerate(tx):
                if c != 'viz-date':
                    continue
                lab = ' '.join(t2 for c2, x2, y2, t2 in tx[i + 1:i + 8] if c2 == 'viz-label' and x2 == x and 0 < y2 - y < 100)
                if any(g.group(1) in t and 'c.' not in t for g in re.finditer(r'\bc\.\s?(\d+)', lab)):
                    bad.append(f'{where}: the date line "{t}" drops the "c." its label keeps ("{lab}"): give the event "date"')
                if re.search(r'\(c\.\)|\(date approx', lab) and 'c.' not in t:
                    bad.append(f'{where}: the label "{lab}" marks its date approximate because the date line cannot: give the event "date"')
                if any(g.group(1) in t and '/' not in t for g in re.finditer(r'\b(\d+)/(\d+)', lab)):
                    bad.append(f'{where}: the date line "{t}" drops the split year its label keeps ("{lab}"): give the event "date"')
            # P63 (1 Nov 2026): a date line names the year its dot stands at (read from the tick labels), or a century or
            # span of years that contains it; the year is never printed where the text gives only a century.
            ticks = [(x, _year(t)) for c, x, y, t in tx if c == 'viz-ticklabel' and _year(t) is not None]
            if len({x for x, _ in ticks}) >= 2:
                (xa, ya), (xb, yb) = ticks[0], ticks[-1]
                for cx, t in re.findall(r'<circle class="viz-dot[^"]*" cx="([-\d.]+)"[^>]*/>\s*<text class="viz-date"[^>]*>(.*?)</text>', svg):
                    at = ya + (float(cx) - xa) * (yb - ya) / (xb - xa)
                    t = H.unescape(re.sub(r'<[^>]+>', '', t))
                    if not any(viz.date_names(t, round(at) + k) for k in (-1, 0, 1) if round(at) + k):
                        bad.append(f'{where}: the date line "{t}" names neither the year its dot stands at ({round(at)}) nor a century or span that contains it')
        if kind == 'timeline' and 'viz-span ' in svg:         # P84 (16 Nov 2026): a span is a period on the axis, not a key
            ax = re.search(r'<line class="viz-axis" x1="[-\d.]+" y1="([-\d.]+)"', svg)
            guides = [(float(a), float(b)) for a, b in re.findall(r'<line class="viz-spanend" x1="([-\d.]+)" y1="[-\d.]+" x2="[-\d.]+" y2="([-\d.]+)"', svg)]
            groups = re.findall(r'<g data-span="(-?\d+) (-?\d+)" data-text="([^"]*)">(.*?)</g></g>', svg, re.S)
            if len(groups) != svg.count('class="viz-span '):
                bad.append(f'{where}: a span drawn without its data-span group (rebuild with the P84 viz.py)')
            for a, b, want, inner in groups:
                got = ' '.join(t for c, x, y, t in _texts(inner) if c in ('viz-spanlabel', 'viz-spanside'))
                if got != H.unescape(want):
                    bad.append(f'{where}: the span {a} to {b} is labelled {got!r}, not {H.unescape(want)!r}')
                if not viz.span_names(got, a, b):
                    bad.append(f'{where}: the span label {got!r} does not carry its years ({a} to {b})')
                r = re.search(r'<rect class="viz-span[^"]*" x="([-\d.]+)" y="[-\d.]+" width="([-\d.]+)"', inner)
                x1, x2 = float(r.group(1)), float(r.group(1)) + float(r.group(2))
                for gx in (x1, x2):
                    if not ax or not any(abs(g - gx) < 2 and abs(y2 - float(ax.group(1))) < 0.2 for g, y2 in guides):   # round 2: an abutting bar stops 1.5 short of its guide
                        bad.append(f'{where}: the span {got!r} has no guide from its end at {gx:.0f} to the axis')
        if kind == 'timeline':                               # P58 (by eye): no stem runs through another event's text
            import viz as V
            stems = [(float(a), float(b), float(c)) for a, b, c in re.findall(r'<line class="viz-stem" x1="([-\d.]+)" y1="([-\d.]+)" x2="[-\d.]+" y2="([-\d.]+)"', svg)]
            for c, x, y, a, t in re.findall(r'<text class="viz-(label|date)" x="([-\d.]+)" y="([-\d.]+)" text-anchor="(\w+)">(.*?)</text>', svg):
                x, y, t = float(x), float(y), H.unescape(re.sub(r'<[^>]+>', '', t))
                w = V._tw(t, 12, 'sans') if c == 'label' else V._tw(t, 10.5, 'mono')
                x0 = {'start': x, 'middle': x - w / 2, 'end': x - w}[a]
                if any(x0 + 1 < sx < x0 + w - 1 and y1 < y - 4 < y2 for sx, y1, y2 in stems):
                    bad.append(f'{where}: a stem runs through the text "{t}"')
        if kind == 'tree':                                   # P79: a tree wider than its phone frame opens on its root
            wv = float(re.search(r'viewBox="0 0 ([\d.]+)', svg).group(1))
            if wv > PHONE_FRAME:
                nodes = [tuple(map(float, r)) for r in re.findall(r'<rect class="viz-node[^"]*" x="([-\d.]+)" y="([-\d.]+)" width="([\d.]+)"', svg)]
                rx, ry, rw = min(nodes, key=lambda r: (r[1], r[0]))
                x0 = re.search(r'<svg [^>]*?data-x0="([\d.]+)"', svg); xr = re.search(r'<svg [^>]*?data-xr="([\d.]+)"', svg)
                at = min(wv - PHONE_FRAME, max(0, float(x0.group(1)) - 12 if x0 else 0, float(xr.group(1)) - PHONE_FRAME if xr else 0))
                if not (at - 0.5 <= rx and rx + rw <= at + PHONE_FRAME + 0.5):
                    bad.append(f'{where}: a {wv:.0f}-unit tree opens its {PHONE_FRAME}-unit phone frame at {at:.0f}, but its root box spans '
                               f'{rx:.0f} to {rx + rw:.0f}: the first screen shows no root (P79: data-xr)')
                elif not any(at < x + w and x < at + PHONE_FRAME for x, y, w in nodes if y > ry):
                    bad.append(f'{where}: the phone frame opens on the root alone, with no box of a lower level in view')
        if kind in viz.X0_KINDS:                             # P50: a centred drawing names where it starts
            lft, x0 = viz._left(svg), re.search(r'<svg [^>]*?data-x0="([\d.]+)"', svg)
            if lft is not None and lft - 8 > 12 and (not x0 or abs(float(x0.group(1)) - (lft - 8)) > 2):
                bad.append(f'{where}: the drawing starts at {lft:.0f} but the svg ' + (f'names data-x0="{x0.group(1)}"' if x0 else 'carries no data-x0') + ', so a phone frame opens on the margin')
        if bce and kind in ('timeline', 'range') and any(c in ('viz-date', 'viz-ticklabel', 'viz-value') and re.search(r'\b(BC|AD)\b', t) for c, x, y, t in tx):
            bad.append(f'{where}: BC/AD in a figure on a page whose prose writes BCE/CE: set "era": "BCE"')
        if kind == 'range':
            rows = re.split(r'<g data-row="\d+">', svg)[1:]
            if not rows:
                bad.append(f'{where}: a range drawn without its rows (rebuild with the P58 viz.py)')
            for r in rows:
                vals = [t.split(' · ')[0] for c, x, y, t in _texts(r) if c == 'viz-value']
                dup = sorted({v for v in vals if vals.count(v) > 1})
                if dup:
                    bad.append(f'{where}: one range row prints {dup[0]!r} {vals.count(dup[0])} times')
            for e in re.finditer(r'<g data-end="([-\d.]+)"><g data-box=""><rect class="viz-lblbg" x="([-\d.]+)" y="[-\d.]+" width="([-\d.]+)"', svg):
                ex, px, pw = map(float, e.groups())
                if not px - 0.6 <= ex <= px + pw + 0.6:
                    bad.append(f'{where}: a range end label ({px:.0f} to {px + pw:.0f}) does not sit under its end at {ex:.0f}')
            bad += [f'{where}: "{t}": a word unit takes the singular for 1' for c, x, y, t in tx if c == 'viz-value' and re.match(r'1 [a-z]*[^s]s\b', t)]
        if kind == 'objects':
            if svg.count('class="viz-lblbg"') != len(re.findall(r'<g data-box="" data-text=', svg)):
                bad.append(f'{where}: a link label drawn without its data-text, so its lines cannot be checked (rebuild with the P58 viz.py)')
            for g in re.finditer(r'<g data-box="" data-text="([^"]*)">(.*?)</g>', svg, re.S):
                want = ' '.join(H.unescape(g.group(1)).split())
                got = ' '.join(t for c, x, y, t in _texts(g.group(2)) if c == 'viz-linklabel')
                if ' '.join(got.split()) != want:
                    bad.append(f'{where}: the link label {want!r} is cut across lines as {got!r}')
        if kind == 'tree':
            vb = re.search(r'viewBox="0 0 ([\d.]+) ', svg)
            xs = [(float(a), float(w)) for a, w in re.findall(r'<rect class="viz-node[^"]*" x="([-\d.]+)" y="[-\d.]+" width="([\d.]+)"', svg)]
            if vb and xs:
                W_, lo, hi = float(vb.group(1)), min(a for a, w in xs), max(a + w for a, w in xs)
                if hi - lo < W_ - 24 and abs(lo - (W_ - hi)) > 1.5:
                    bad.append(f'{where}: a narrow tree is not centred (margins {lo:.0f} and {W_ - hi:.0f})')
    return bad, n
def check_viz_keys(fails):
    """P52 (1 Nov 2026): every ```viz block in the vault of each markdown course, every figure declaration in a history
    report, every course home figure in courses.py and every block on the examples page carries only the keys
    viz.VIZ_KEYS documents for its kind (a typo or an undocumented key is a figure that does not draw what it says),
    and rendering a block leaves it as it was (viz.render works on a copy)."""
    bad, n = [], 0
    def one(where, d, kind=None):
        nonlocal n
        n += 1
        if kind: d.setdefault('kind', kind)
        bad.extend(f'{where}: {b}' for b in viz.check_keys(d))
    for c in COURSES:
        if (R.parent / c['vault']).is_dir():     # P71-3: a history course's reports are vault Markdown too
            for f in sorted((R.parent / c['vault']).glob('*.md')):
                for i, m in enumerate(viz._FENCE.finditer(f.read_text()), 1):
                    one(f'{c["vault"]}/{f.name} block {i}', json.loads(m.group(1)))
        if c.get('figure'): one(f'courses.py {c["id"]} figure', json.loads(json.dumps(c['figure'])))
    for key, *_, block in viz_examples.EXAMPLES + [(k, w, b) for k, w, b in viz_examples.CASES]:
        before = json.dumps(block, sort_keys=True)
        one(f'viz-examples {key}', json.loads(before)); viz.render(block)
        if json.dumps(block, sort_keys=True) != before: bad.append(f'viz-examples {key}: viz.render changed the block it was given')
    fails += ['figure keys: ' + b for b in bad[:20]]
    print(f'figure keys (P52): {n} blocks read, {len(bad)} undocumented keys')

def check_notes(fails):
    """P73 (1 Nov 2026): a markdown unit's text before its first heading is read at the end, in its own closed accordion,
    "The writer's opening note" (#<pid>-note), between Sources and "How this unit was made": present, closed and
    holding that text on every unit that has an opening, absent on one that has none; section 1 no longer carries it."""
    import mdcourse
    bad, have, none = [], 0, 0
    for c in COURSES:
        if c['family'] != 'markdown' or not (R.parent / c['vault']).is_dir(): continue
        for f in sorted((R.parent / c['vault']).glob('*.md')):
            src = f.read_text()
            m = re.match(r'---\n(.*?)\n---\n', src, re.S)
            if not m: continue
            code = re.search(r'^code:\s*(\S+)', m.group(1), re.M)
            if not code: continue
            built = list(SITE.glob(f'*/read-{code.group(1).lower()}.html'))
            if not built: continue
            pid, page = 'read-' + code.group(1).lower(), built[0].read_text()
            opening = re.sub(r'^#\s.*$', '', src[m.end():].split('\n## ', 1)[0], flags=re.M).strip()
            words = ' '.join(re.sub(r'[*_`\[\]()]', '', opening).split()[:6])
            note = re.search(rf'<details class="acc note"( open)? id="{pid}-note">(.*?)</details>', page, re.S)
            order = [x for x in re.findall(r'<details class="acc (src|note|made)"', page)]
            if opening:
                have += 1
                if not note: bad.append(f'{pid}: the opening note is missing'); continue
                if note.group(1): bad.append(f'{pid}: the opening note is open by default')
                if order != ['src', 'note', 'made']: bad.append(f'{pid}: the accordions run {order}, expected Sources, the note, How this unit was made')
                body = re.sub(r'<[^>]+>', '', note.group(2))
                if words and ' '.join(re.sub(r'[*_`\[\]()]', '', H.unescape(body)).split()).find(words.split()[0]) < 0:
                    bad.append(f'{pid}: the opening note does not hold the unit\'s opening ("{words}…")')
                sec0 = re.search(r'<section class="sec" data-step="0">(.*?)</section>', page, re.S)
                if sec0 and not sec0.group(1).lstrip().startswith('<h2'):
                    bad.append(f'{pid}: section 1 still opens on text before its heading')
            else:
                none += 1
                if note: bad.append(f'{pid}: an opening note on a unit with no opening')
    fails += ['opening note: ' + b for b in bad]
    print(f'opening notes (P73): {have} units with an opening, each with its closed note after Sources; {none} without, none shown')

def check_figure_rules(fails):
    bad, n = [], 0
    for f in [SITE / 'index.html'] + sorted(x for x in SITE.rglob('*.html') if x.name != 'index.html'):
        b, k = figure_rules(f.read_text(), str(f.relative_to(SITE))); bad += b; n += k
    fails += ["figure rules: " + b for b in bad[:20]]
    print(f'figure rules (P58): {n} built figures read, {len(bad)} faults')

# P56 (30 Oct 2026): a link into an unopened panel lands once the fetch is in and the shell has scrolled to the anchor,
# which can take longer than a fixed wait (#s-m23 once measured at top 7319, then passed on a re-run). SETTLE_JS waits,
# frame by frame for up to 3 s, until the anchor's top has held still for 5 frames inside the landing band (-5..200),
# and returns [panel, found, top, at the foot]; fresh_land() measures that way and, if it is still off, reloads and measures once more.
# P-DEC11 (21 Nov 2026): a page too short to scroll its anchor up to the band (a two-brief briefs page: 248 to 343 px)
# lands when the page stands scrolled to its foot (scrollY within 1 px of its most) with the anchor's top inside the
# window: the furthest the shell can take it. A page that can scroll further is still held to the band (lands()).
SETTLE_JS = '''async (id) => { let last = null, same = 0; const t0 = performance.now();
  const foot = () => { const s = document.scrollingElement; return s.scrollTop >= s.scrollHeight - innerHeight - 1; };
  while (performance.now() - t0 < 3000) { await new Promise(r => requestAnimationFrame(r));
    const el = document.getElementById(id), t = el ? Math.round(el.getBoundingClientRect().top) : null;
    same = (t !== null && t === last) ? same + 1 : 0; last = t;
    if (same >= 5 && t >= -5 && t <= 200) break; }   // a page that stops short of the band is read after the full 3 s
  const el = document.getElementById(id), p = [...document.querySelectorAll('.panel')].find(p => !p.hidden);
  const top = el ? Math.round(el.getBoundingClientRect().top) : null;
  return [p && p.id, !!el, top, top !== null && top > 200 && top < innerHeight && foot()]; }'''

def lands(sec):
    """P-DEC11: the anchor is found and its top is in the landing band (-5..200), or past it only because the page is
    too short to scroll further (SETTLE_JS's fourth value: scrolled to its foot, the anchor inside the window)."""
    return bool(sec[1]) and sec[2] is not None and (-5 <= sec[2] <= 200 or bool(sec[3]))

def fresh_land(pg, h, retried):
    """Open URL#h on a fresh load and return [visible panel, anchor found, anchor top, page at its foot] once the anchor has settled;
    one retry (a second fresh load) when it has not landed, recorded in retried."""
    for attempt in (0, 1):
        pg.goto(URL + '#' + h); pg.reload(); ready(pg)
        sec = pg.evaluate(SETTLE_JS, h)
        if lands(sec):
            return sec
        if attempt == 0: retried.append(f'#{h} (top {sec[2]})')
    return sec

# P68 · the reading layout, on one reading page (a unit or a report) already shown: content first (the header with its
# scope, then the bar, then the text; nothing about how the page was made before the text), process last (the two
# accordions after the text, Sources then "How this unit was made", both closed), and the stepper: one section shown
# at a time, "Section n of N" and the progress bar right at every step, next from the first section to the last and
# previous back, the menu reaching every section, "Whole unit" showing all of them and returning to one.
STEP_JS = r'''(pid) => {
  const p = document.getElementById(pid), out = [];
  const r = p.querySelector('.report.steps'), bar = p.querySelector('.stepbar');
  if (!r || !bar || !r.classList.contains('stepping')) return {n: 0, bad: ['no stepper on the page']};
  const secs = [...r.children].filter(s => s.classList.contains('sec')), n = secs.length;
  const vis = () => secs.map((s, i) => s.offsetHeight > 0 ? i : -1).filter(i => i >= 0);
  const want = (k, how) => { const v = vis();
    if (v.length !== 1 || v[0] !== k) out.push(`${how}: sections shown [${v}], expected [${k}]`);
    const sof = bar.querySelector('.sof').textContent.trim(); if (sof !== `Section ${k + 1} of ${n}`) out.push(`${how}: the bar reads "${sof}"`);
    const w = parseFloat(bar.querySelector('.sprog i').style.width); if (!(Math.abs(w - 100 * (k + 1) / n) < 0.1)) out.push(`${how}: progress ${w}%`); };
  const kids = [...p.children], ph = p.querySelector('.phead'), proc = p.querySelector('.process');
  if (kids.indexOf(bar) !== kids.indexOf(ph) + 1 || kids.indexOf(r) !== kids.indexOf(bar) + 1) out.push('not header, bar, text in that order');
  if (!ph.querySelector('h1 + .scope') && (!pid.startsWith('read-') || ph.querySelector('.eyebrow .pill.live'))) out.push('no scope line under the title');
  if (p.querySelector('.phead .prov, .phead .lede, .phead + .lede, .report .prov, .phead .toc')) out.push('process text or the old chips before the text');
  if (+bar.dataset.n !== n || bar.querySelectorAll('.seclist a').length !== n) out.push(`menu ${bar.querySelectorAll('.seclist a').length} items, bar ${bar.dataset.n}, sections ${n}`);
  if (secs.some(s => !s.querySelector(':scope > h2.band .bn'))) out.push('a section without its numbered band');
  const acc = proc ? [...proc.children].map(d => (d.classList.contains('src') ? 'src' : d.classList.contains('note') ? 'note' : d.classList.contains('made') ? 'made' : d.tagName) + (d.open ? ' open' : '')) : [];
  if (!proc || kids.indexOf(proc) !== kids.indexOf(r) + 1 || !['src,made', 'src,note,made'].includes(acc.join())) out.push(`after the text: ${acc.join() || 'nothing'}, expected Sources, the opening note where there is one, then How this unit was made, all closed`);
  want(+p.dataset.step || 0, 'on opening');
  if (+p.dataset.step) [...bar.querySelectorAll('.seclist a')][0].click();
  want(0, 'menu to 1');
  if (n > 1 && (proc.offsetHeight > 0 || p.querySelector(':scope > .pager').offsetHeight > 0)) out.push('the accordions or the next-unit cards show before the last section');
  for (let k = 1; k < n; k++) { secs[k - 1].querySelector(':scope > .secnav .snext').click(); want(k, `next to ${k + 1}`); }
  if (secs[n - 1].querySelector(':scope > .secnav .snext:not(.send)')) out.push('the last section has a next-section button');
  if (proc.offsetHeight === 0) out.push('the accordions are not shown after the last section');
  for (let k = n - 2; k >= 0; k--) { secs[k + 1].querySelector(':scope > .secnav .sprev').click(); want(k, `previous to ${k + 1}`); }
  [...bar.querySelectorAll('.seclist a')].forEach((a, k) => { a.click(); want(k, `menu item ${k + 1}`); });
  bar.querySelector('.whole').click(); if (vis().length !== n) out.push(`"Whole unit" shows ${vis().length} of ${n} sections`);
  bar.querySelector('.whole').click(); if (vis().length !== 1) out.push(`after "Whole unit" off, ${vis().length} sections shown`);
  [...bar.querySelectorAll('.seclist a')][0].click();
  return {n, bad: out};
}'''
# a link into Sources (the menu's, then the one at the end of the last section) opens its accordion and brings it into view
SRC_JS = r'''async (pid) => {
  const p = document.getElementById(pid), d = document.getElementById(pid + '-sources'), out = [];
  const seen = async () => { await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); const t = d.getBoundingClientRect().top; return d.open && t > -5 && t < innerHeight - 40; };
  p.querySelector('.secmenu').open = true; p.querySelector('.secx a[href="#' + pid + '-sources"]').click();
  if (!await seen()) out.push(`the menu's Sources link: open ${d.open}, top ${Math.round(d.getBoundingClientRect().top)}`);
  d.open = false; const secs = p.querySelectorAll('.report.steps > .sec');
  [...p.querySelectorAll('.seclist a')].pop().click();
  secs[secs.length - 1].querySelector('.secnav .send').click();
  if (!await seen()) out.push(`the last section's Sources link: open ${d.open}, top ${Math.round(d.getBoundingClientRect().top)}`);
  d.open = false; [...p.querySelectorAll('.seclist a')][0].click(); window.scrollTo(0, 0);
  return out;
}'''

# P68: with --shots, a --page reading page is also shot in the states its top does not show, one viewport each: the
# section menu open, the end of section 1 (its next button), section 2 just opened by it, the end of the last section
# with the two accordions closed, the two accordions open (at Sources, then at "How this unit was made"), and
# "Whole unit" mid-page
READING_SHOTS = [
    ('2-menu', "(pid) => { window.scrollTo(0, 0); document.querySelector('#' + pid + ' .secmenu').open = true; }"),
    ('3-end-of-1', "(pid) => { const p = document.getElementById(pid); p.querySelector('.secmenu').open = false; p.querySelector('.sec.on .secnav').scrollIntoView({block: 'end'}); }"),
    ('4-section-2', "(pid) => { const a = document.querySelector('#' + pid + ' .sec.on .snext'); if (a) a.click(); }"),
    ('5-last-end', "(pid) => { const p = document.getElementById(pid); [...p.querySelectorAll('.seclist a')].pop().click(); window.scrollTo(0, document.documentElement.scrollHeight); }"),
    ('6-process-open', "(pid) => { const p = document.getElementById(pid); p.querySelectorAll('.process details').forEach(d => d.open = true); document.getElementById(pid + '-sources').scrollIntoView(); }"),
    ('6a-note-open', "(pid) => { const n = document.getElementById(pid + '-note'); if (n) n.scrollIntoView(); }"),
    ('6b-made-open', "(pid) => { document.getElementById(pid + '-made').scrollIntoView(); }"),
    ('7-whole', "(pid) => { const p = document.getElementById(pid); p.querySelectorAll('.process details').forEach(d => d.open = false); p.querySelector('.stepbar .whole').click(); window.scrollTo(0, document.documentElement.scrollHeight * 0.4); }"),
]

# P94 (8 Nov 2026) · the section separators: on one reading page, every section's top-level paragraphs and their
# words, read from the page (each <p> child of the section; its words its text nodes split at white space, a tag a
# break, as build.py's wc counts), against its separator: one separator in a section with a paragraph, none in one
# without, standing last before the next and previous; div.topo.topo-patch.topo-sep, aria-hidden, textless, at most
# 6 KB; one rise per paragraph in order, its data-words that paragraph's words; every line in the page's tone (the
# panel's --cc); the frame 1200:170 and the column's width; in one-section view the text above and the next and
# previous below at least 20 px clear, in "Whole unit" the text above and the next section's band; then, with motion
# allowed, each separator's swell (S-NAV1 step D: one topo-swell on each of its lines, transform only) and at the five
# poses of the swell every line inside its frame; the page no wider than the screen.
SEP_JS = r"""([pid, poses, bt, motion]) => { """ + SWELL_AT_JS + r"""
  const P = document.getElementById(pid), out = {secs: 0, seps: 0, none: 0, bytes: 0, maxb: 0, bad: [], ph: [], anims: 0, poses: 0};
  if (!P) { out.bad.push('no page'); return out; }
  const r = P.querySelector('.report.steps'), bar = P.querySelector('.stepbar'), whole = bar.querySelector('.whole');
  const words = e => { let t = ''; const walk = n => { for (const c of n.childNodes) { if (c.nodeType === 3) t += c.data; else if (c.nodeType === 1) { t += ' '; walk(c); t += ' '; } } }; walk(e); return t.split(/\s+/).filter(Boolean).length; };
  const probe = document.createElement('i'); P.appendChild(probe); probe.style.color = 'var(--cc)'; const tone = getComputedStyle(probe).color; probe.remove();
  const secs = [...r.children].filter(x => x.classList.contains('sec')); out.secs = secs.length;
  const seps = [];
  secs.forEach((sec, k) => {
    const paras = [...sec.children].filter(e => e.tagName === 'P' && !e.classList.contains('viz-cue')).map(words).filter(n => n > 0);   // the cue shell.js puts under a figure or table wider than its frame is the figure's, not a paragraph
    const ts = sec.querySelectorAll('.topo'), t = sec.querySelector(':scope > .topo-sep');
    if (!paras.length) { out.none++; if (ts.length) out.bad.push(`section ${k + 1}: no paragraph, yet ${ts.length} drawing(s)`); return; }
    if (ts.length !== 1 || !t) { out.bad.push(`section ${k + 1}: ${paras.length} paragraphs, ${ts.length} drawings, separator ${!!t}`); return; }
    out.seps++; seps.push([k, t]);
    if ([...t.classList].filter(x => x !== 'off').join(' ') !== 'topo topo-patch topo-sep' || t.tagName !== 'DIV') out.bad.push(`section ${k + 1}: the separator is ${t.tagName}.${t.className}`);
    if (!t.nextElementSibling || !t.nextElementSibling.matches('nav.secnav')) out.bad.push(`section ${k + 1}: the separator is not last before the next and previous`);
    if (t.getAttribute('aria-hidden') !== 'true') out.bad.push(`section ${k + 1}: the separator is not aria-hidden`);
    if (t.textContent.trim() || t.querySelector('text, title, desc')) out.bad.push(`section ${k + 1}: the separator holds text`);
    const b = new Blob([(e => { if (!e.classList.contains('off')) return e.outerHTML; const c = e.cloneNode(true); c.classList.remove('off'); return c.outerHTML; })(t)]).size; out.bytes += b; out.maxb = Math.max(out.maxb, b);
    const cap = 6144 + 135 * Math.max(0, t.querySelectorAll('svg.topo-l g.ct-rise').length - 38);   // W-SCE2: build.py SEP_MAX, SEP_PER for each rise over SEP_FREE
    if (b > cap) out.bad.push(`section ${k + 1}: the separator is ${b} bytes, over ${cap}`);
    const gs = [...t.querySelectorAll('svg.topo-l g.ct-rise')], got = gs.map(g => +g.getAttribute('data-words'));
    if (t.querySelectorAll('svg.topo-l').length !== 1 || t.querySelector('g.ct-plan')) out.bad.push(`section ${k + 1}: ${t.querySelectorAll('svg.topo-l').length} layouts, or a planned ring`);
    const blank = gs.filter(g => !g.querySelector('circle.ct-spot') && !(g.querySelector('path') && g.querySelector('path').getAttribute('d'))).map(g => g.getAttribute('data-label'));   // P94 check: every paragraph shows
    if (blank.length) out.bad.push(`section ${k + 1}: rises ${blank.join(' ')} draw nothing`);
    if (got.join() !== paras.join()) out.bad.push(`section ${k + 1}: rises by words ${got.join(',')}, its paragraphs ${paras.join(',')}`);
    const st = [...new Set([...t.querySelectorAll('path, circle')].map(e => getComputedStyle(e).stroke))];
    if (st.length !== 1 || st[0] !== tone) out.bad.push(`section ${k + 1}: lines in ${st.join(' ')}, the page's tone ${tone}`);
    out.ph.push(parseFloat(getComputedStyle(t).getPropertyValue('--ph')));
  });
  // one section at a time: each separator between its text and its next and previous
  const links = [...bar.querySelectorAll('.seclist a')];
  seps.forEach(([k, t]) => { links[k].click();
    const fr = t.getBoundingClientRect(), up = t.previousElementSibling.getBoundingClientRect(), nav = t.nextElementSibling.getBoundingClientRect(), col = secs[k].getBoundingClientRect();
    if (!fr.width) { out.bad.push(`section ${k + 1}: the separator does not show in its section`); return; }
    if (Math.abs(fr.width / fr.height - 1200 / 170) > .05) out.bad.push(`section ${k + 1}: the separator is ${(fr.width / fr.height).toFixed(3)}:1, not 1200:170`);
    if (Math.abs(fr.width - col.width) > 1) out.bad.push(`section ${k + 1}: the separator is ${fr.width.toFixed(1)} px wide in a ${col.width.toFixed(1)} px column`);
    t.nextElementSibling.querySelectorAll('a').forEach(a => { const sp = a.querySelector('span'), ar = a.getBoundingClientRect(), pr = parseFloat(getComputedStyle(a).paddingRight);   // P94 check: a label past its button
      if (sp && (sp.scrollWidth > sp.clientWidth + 1 || sp.getBoundingClientRect().right > ar.right - pr + .5 || sp.getBoundingClientRect().left < ar.left - .5)) out.bad.push(`section ${k + 1}: "${sp.textContent}" runs past its button`); });
    if (fr.top - up.bottom < 20 || nav.top - fr.bottom < 20) out.bad.push(`section ${k + 1}: the separator ${Math.round(fr.top - up.bottom)} px under the text and ${Math.round(nav.top - fr.bottom)} px over the next and previous (20 at least)`);
  });
  links[0].click();
  // "Whole unit": every separator between its section and the next
  whole.click();
  seps.forEach(([k, t]) => { const fr = t.getBoundingClientRect(), nx = secs[k + 1];
    if (!fr.width) out.bad.push(`section ${k + 1}: no separator shown in "Whole unit"`);
    else if (nx && nx.getBoundingClientRect().top - fr.bottom < 20) out.bad.push(`section ${k + 1}: in "Whole unit" the separator is ${Math.round(nx.getBoundingClientRect().top - fr.bottom)} px over the next section`); });
  out.scroll = [document.documentElement.scrollWidth, document.documentElement.clientWidth];
  // the move
  const an = document.getAnimations().filter(a => a.effect && a.effect.target && a.effect.target.closest && a.effect.target.closest('#' + pid + ' .topo-sep'));
  out.anims = an.length;
  if (!motion) { if (an.length) out.bad.push(`${an.length} animations run on the separators under reduced motion`); }
  else {
    seps.forEach(([k, t]) => { const ls = [...t.querySelectorAll('svg.topo-l path')], mine = an.filter(a => ls.includes(a.effect.target));
      if (mine.length !== ls.length || mine.some(a => a.animationName !== 'topo-swell') || an.some(a => t.contains(a.effect.target) && !ls.includes(a.effect.target)))
        out.bad.push(`section ${k + 1}: ${mine.length} of its ${ls.length} lines swell (${[...new Set(mine.map(a => a.animationName))].join()}), and nothing else may move`); });
    an.forEach(a => { const props = [...new Set(a.effect.getKeyframes().flatMap(f => Object.keys(f)).filter(x => !['offset', 'computedOffset', 'easing', 'composite'].includes(x)))];
      if (props.some(x => x !== 'transform')) out.bad.push(`a separator animates ${props.join(',')}, not transform alone`); });
    for (const p of poses) {
      an.forEach(a => swellAt(a, p, bt));
      out.poses++;
      seps.forEach(([k, t]) => { const fr = t.getBoundingClientRect(); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        t.querySelectorAll('path, circle').forEach(e => { const q = e.getBoundingClientRect(); if (!q.width && !q.height) return; x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); });
        const m = [x0 - fr.left, y0 - fr.top, fr.right - x1, fr.bottom - y1];
        if (Math.min(...m) < -.5) out.bad.push(`section ${k + 1}: at pose ${p} its lines leave the frame by ${m.filter(v => v < 0).map(v => (-v).toFixed(1))} px`);
        out.minclear = Math.min(out.minclear === undefined ? 1e9 : out.minclear, ...m); });
    }
    an.forEach(a => a.play());
  }
  whole.click(); links[0].click(); window.scrollTo(0, 0);
  return out;
}"""

SEP_WIDTHS = [('phone320', 320, 640, True), ('phone', 390, 844, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]

def check_seps(br, fails):
    """P94: every reading page at 320, 390, 768 and 1280 px, dark and light, under reduced motion and with motion
    allowed: SEP_JS on each (the separators against the sections' paragraphs, their place, size, tone and bytes, and
    with motion their move and their lines inside the frame at the five poses); no sideways scroll at 320 px. Prints
    the count and bytes."""
    errs, bad = [], []
    tot = dict(seps=0, none=0, bytes=0, secs=0, poses=0)
    per_page, low = {}, 1e9
    for name, w, h, mobile in SEP_WIDTHS:
        ctx, pg, _ = new_page(None, br, errs, f'seps {name}', w, h, mobile, motion=True)
        ids = SCOPE.only(pg.eval_on_selector_all('.panel[data-kind="report"]', 'ps => ps.map(p => p.id)'))   # S-DEC4: the run's pages
        for pid in ids:
            pg.evaluate(f"localStorage.removeItem('{THEME_KEY}'); document.documentElement.removeAttribute('data-theme')")
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                for motion in (False, True):
                    pg.emulate_media(reduced_motion='no-preference' if motion else 'reduce'); pg.wait_for_timeout(20)
                    r = pg.evaluate(SEP_JS, [pid, list(POSES), BTIME, motion])
                    tag = f'{pid} {name} {theme}{" motion" if motion else ""}'
                    bad += [f'{tag}: {b}' for b in r['bad'][:3]]
                    if r['scroll'][0] > r['scroll'][1]: bad.append(f'{tag}: the page is {r["scroll"][0]} px wide on a {r["scroll"][1]} px screen')
                    if motion:
                        phs = sorted(r['ph']); n = len(phs)
                        close = [(a, b) for a, b in zip(phs, phs[1:]) if b - a < .9 / max(n, 1)]
                        if close or any(x != x for x in phs): bad.append(f'{tag}: separators share or lack a phase ({close[:3]})')
                        if 'minclear' in r: low = min(low, r['minclear'])
                        tot['poses'] += r['poses'] * r['seps']
                    if name == 'phone' and theme == 'dark' and not motion:
                        tot['seps'] += r['seps']; tot['none'] += r['none']; tot['bytes'] += r['bytes']; tot['secs'] += r['secs']
                        per_page[pid] = (r['bytes'], r['seps'], r['maxb'])
        pg.emulate_media(reduced_motion='reduce')
        ctx.close()
    fails += ['separators ' + b for b in bad[:30]]
    if len(bad) > 30: fails.append(f'separators: {len(bad) - 30} more')
    if errs: fails.append('separators: console errors: ' + ' | '.join(errs[:3]))
    big = max(per_page.items(), key=lambda x: x[1][0]) if per_page else ('', (0, 0, 0))
    print(f'separators: {len(per_page)} reading pages, {tot["secs"]} sections, {tot["seps"]} separators, {tot["none"]} sections without a paragraph and so without one; '
          f'{tot["bytes"]:,} bytes in all, the largest {max((v[2] for v in per_page.values()), default=0):,} B, the page with most {big[0]} ({big[1][0]:,} B over {big[1][1]}); '
          f'checked at {", ".join(str(x[1]) for x in SEP_WIDTHS)} px, dark and light, with and without motion; {tot["poses"]:,} separator poses with motion allowed, the closest line {low:.1f} px from its frame')
    return tot, per_page

# P95 (8 Nov 2026) · the object reliefs: the library (design/outlines/) and every page uses.json maps
OUTL = R.parent / 'design' / 'outlines'
REL_FIELDS = ('id', 'file', 'depicts', 'courses', 'keywords', 'source', 'author', 'licence', 'licence_url', 'credit', 'texts')
REL_COURSES = tuple(p for c in ALL_COURSES if c.get('reliefs') for p in sub_pages(c))   # S-DEC4: course.toml `reliefs`, every course of the repo (the library serves them all)
REL_WIDTHS = [('phone320', 320, 640, True), ('phone', 390, 844, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]
REL_JS = r"""([pid, poses, bt, motion, want]) => { """ + SWELL_AT_JS + r"""
  const P = document.getElementById(pid), out = {bad: [], bytes: 0, poses: 0};
  if (!P) { out.bad.push('no page'); return out; }
  const figs = P.querySelectorAll('figure.relief-fig'), f = figs[0], hd = P.querySelector(':scope > header.phead');
  if (figs.length !== 1 || !f) { out.bad.push(`${figs.length} relief figures`); return out; }
  if (f.parentElement !== hd) out.bad.push('the relief is not in the page header');
  const sc = hd.querySelector(':scope > p.scope');
  if (sc && !(sc.compareDocumentPosition(f) & Node.DOCUMENT_POSITION_FOLLOWING)) out.bad.push('the relief is not under the scope line');
  if (f.nextElementSibling) out.bad.push('the relief is not the header\'s last block');
  if (!hd.nextElementSibling || !hd.nextElementSibling.matches('.stepbar')) out.bad.push('the section bar does not follow the header');
  if (f.dataset.outline !== want.id) out.bad.push(`outline ${f.dataset.outline}, mapped ${want.id}`);
  const t = f.querySelector(':scope > div.topo.relief'), cap = f.querySelector(':scope > figcaption');
  if (!t || f.children.length !== 2 || !cap) { out.bad.push('the figure is not one drawing and its caption'); return out; }
  if (cap.textContent.trim() !== want.caption) out.bad.push(`caption "${cap.textContent.trim()}", expected "${want.caption}"`);
  if (!cap.textContent.includes(want.credit)) out.bad.push('the credit is not printed exactly');
  const la = cap.querySelectorAll('a');
  if (la.length !== 1 || la[0].getAttribute('href') !== want.lic || la[0].textContent !== want.licence) out.bad.push('the licence is not linked to its text');
  if ([...t.classList].filter(x => x !== 'off').join(' ') !== 'topo relief' || t.getAttribute('aria-hidden') !== 'true')   // S-NAV1 step G: shell.js's runtime .off aside out.bad.push(`the drawing is ${t.className}, aria-hidden ${t.getAttribute('aria-hidden')}`);
  if (t.textContent.trim() || t.querySelector('text, title, desc')) out.bad.push('the drawing holds text');
  const svgs = t.querySelectorAll('svg'), sv = svgs[0];
  if (svgs.length !== 1 || !sv.classList.contains('topo-l')) out.bad.push(`${svgs.length} svgs, or not svg.topo-l`);
  // S-NAV1 step D: the paths, each in a group of one origin (<g style="--o:...">) where it moves, a level's d in its style
  const paths = [...sv.querySelectorAll('path')], gs = [...sv.querySelectorAll('g')];
  if (!paths.length || [...sv.children].some(e => !['path', 'g'].includes(e.tagName)) || gs.some(g => g.parentElement !== sv || [...g.children].some(e => e.tagName !== 'path') || [...g.attributes].some(a => a.name !== 'style') || !/^--o:-?\d+px -?\d+px$/.test(g.getAttribute('style') || ''))
      || paths.some(p => (p.hasAttribute('class') && p.getAttribute('class') !== 'rl-out') || [...p.attributes].some(a => !['class', 'd', 'style'].includes(a.name)) || (p.hasAttribute('style') && !/^--d:(?:1|\.\d\d?)$/.test(p.getAttribute('style')))))
    out.bad.push('the drawing holds more than inside paths (no class) and rl-out paths (a d, a --d) in groups of one origin (--o)');
  // S-NAV1 step G: an inside line (the outline and the levels inside it) carries no class; only the halo is rl-out
  if (!sv.querySelector('path:not([class])') || !sv.querySelector('path.rl-out')) out.bad.push('no outline or no halo');
  out.bytes = new Blob([(e => { if (!e.classList.contains('off')) return e.outerHTML; const c = e.cloneNode(true); c.classList.remove('off'); return c.outerHTML; })(t)]).size;
  if (out.bytes > __REL_MAX__) out.bad.push(`the drawing is ${out.bytes} bytes, over __REL_MAX__`);
  const probe = document.createElement('i'); P.appendChild(probe); probe.style.color = 'var(--cc)'; const tone = getComputedStyle(probe).color; probe.remove();
  const st = [...new Set(paths.map(p => getComputedStyle(p).stroke))];
  if (st.length !== 1 || st[0] !== tone) out.bad.push(`lines in ${st.join(' ')}, the page's tone ${tone}`);
  const op = parseFloat(getComputedStyle(sv).opacity), ho = parseFloat(getComputedStyle(sv.querySelector('path.rl-out')).strokeOpacity), io = parseFloat(getComputedStyle(sv.querySelector('path:not([class])')).strokeOpacity);
  if (!(op > 0 && op < 1) || !(ho < io)) out.bad.push(`the layer at ${op}, the halo at ${ho} of the lines' ${io}`);
  // the frame: the drawing's aspect, the column's width at most, 280 px tall at most on a phone (340 from 768)
  const fr = t.getBoundingClientRect(), col = hd.getBoundingClientRect(), vb = sv.viewBox.baseVal;
  out.w = fr.width; out.h = fr.height;
  if (Math.abs(fr.width / fr.height - vb.width / vb.height) > .02) out.bad.push(`frame ${(fr.width / fr.height).toFixed(3)}:1, drawing ${(vb.width / vb.height).toFixed(3)}:1`);
  if (fr.width > col.width + .5) out.bad.push(`frame ${fr.width.toFixed(1)} px in a ${col.width.toFixed(1)} px column`);
  const maxh = innerWidth < 768 ? 280 : 340;
  if (fr.height > maxh + .5) out.bad.push(`frame ${fr.height.toFixed(1)} px tall, over ${maxh}`);
  if (Math.abs(fr.height - maxh) > .5 && Math.abs(fr.width - col.width) > .5) out.bad.push(`frame ${fr.width.toFixed(1)} x ${fr.height.toFixed(1)}: neither the column's width nor ${maxh} px tall`);
  out.scroll = [document.documentElement.scrollWidth, document.documentElement.clientWidth];
  const an = document.getAnimations().filter(a => a.effect && a.effect.target && t.contains(a.effect.target));
  out.anims = [...new Set(an.map(a => a.animationName))].join();
  if (!motion) { if (an.length) out.bad.push(`${an.length} animations under reduced motion`); }
  else {
    if (out.anims !== 'topo-swell' || an.length !== paths.length || paths.some(p => !an.some(a => a.effect.target === p))) out.bad.push(`animations [${out.anims}] on ${an.length} of its ${paths.length} lines, not a swell on each (S-NAV1 step D)`);
    an.forEach(a => { const props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k)).filter(x => !['offset', 'computedOffset', 'easing', 'composite'].includes(x)))];
      if (props.some(x => x !== 'transform')) out.bad.push(`animates ${props.join(',')}, not transform alone`); });
    out.ph = parseFloat(getComputedStyle(t).getPropertyValue('--ph'));
    out.sepph = [...P.querySelectorAll('.topo-sep')].map(s => parseFloat(getComputedStyle(s).getPropertyValue('--ph')));
    for (const p of poses) {
      an.forEach(a => swellAt(a, p, bt));
      out.poses++;
      const r = t.getBoundingClientRect(); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
      paths.forEach(e => { const q = e.getBoundingClientRect(); x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); });
      const m = [x0 - r.left, y0 - r.top, r.right - x1, r.bottom - y1];
      if (Math.min(...m) < -.5) out.bad.push(`at pose ${p} its lines leave the frame by ${m.filter(v => v < 0).map(v => (-v).toFixed(1))} px`);
      out.minclear = Math.min(out.minclear === undefined ? 1e9 : out.minclear, ...m);
    }
    an.forEach(a => a.play());
  }
  // the page's text names the object
  const txt = P.querySelector('.report.steps').textContent;
  if (!new RegExp('\\b(?:' + want.kw.map(k => k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')\\b', 'i').test(txt)) out.bad.push('the page\'s text does not name the object');
  return out;
}""".replace('__REL_MAX__', str(viz.REL_MAX))   # S-NAV1 step G: the budget is viz.py's (17,821 B; 12 KB before)


def check_reliefs(br, fails):
    """P95, P96: the outline library (at least ten outlines for each course, each with every field, an allowed licence, its
    SVG and its relief JSON, and a text of each course it serves naming it); every page uses.json maps (in this
    edition) at 320, 390, 768 and 1280 px, dark and light, with and without motion (REL_JS: its place under the scope
    line before the section bar, its caption and credit printed exactly, classes only, aria-hidden and textless, at most
    viz.REL_MAX bytes (17,821 from S-NAV1 step G; 12 KB before), the page's tone, the halo fainter, its frame, a swell on each line by transform only at a phase of its own, its
    lines inside the frame at the five poses of the swell, still under reduced motion, the page's text naming
    the object, no sideways scroll); and no other reading page holding a relief."""
    import mdcourse
    lib = json.loads((OUTL / 'outlines.json').read_text())
    allowed = set(lib['allowed_licences'])
    bad, per = [], {c: 0 for c in REL_COURSES}
    for o in lib['outlines']:
        miss = [k for k in REL_FIELDS if not o.get(k)] + [k for k in ('repository', 'path', 'commit') if not o.get('source', {}).get(k)]
        if miss: bad.append(f'{o.get("id")}: no {", ".join(miss)}')
        if o.get('licence') not in allowed: bad.append(f'{o.get("id")}: licence {o.get("licence")!r} not in {sorted(allowed)}')
        if o.get('licence') not in o.get('credit', ''): bad.append(f'{o.get("id")}: the credit does not name its licence')
        for f in (o['file'], f'{o["id"]}.json'):
            if not (OUTL / f).exists(): bad.append(f'{o["id"]}: {f} missing')
        for c in o['courses']:
            per[c] = per.get(c, 0) + 1
            if not o['texts'].get(c): bad.append(f'{o["id"]}: no text of {c} names it')
    thin = {c: n for c, n in per.items() if n < 10}
    if thin: bad.append(f'the library holds fewer than ten outlines for {thin}')
    print(f'reliefs: the library holds {len(lib["outlines"])} outlines ({", ".join(f"{c} {n}" for c, n in per.items())}), {len(lib["rejected"])} rejected; licences {sorted({o["licence"] for o in lib["outlines"]})}')
    # every reading page on disk: a relief where uses.json maps one, none elsewhere
    pages = {}
    shell = (SITE / 'index.html').read_text()
    for m in re.finditer(r'<section class="panel[^"]*" id="([^"]+)"[^>]*data-kind="report"[^>]*data-src="([^"]+)"', shell):
        pages[m.group(1)] = (SITE / m.group(2)).read_text()
    mapped = {pid: oid for pid, oid in mdcourse.USES.items() if pid in pages}
    # P96: the roll-out. Every course keeps at least ten outlines in use (a course with fewer than ten reading pages, as
    # many as it has pages with a relief, each its own); every outline is in use or marked spare, not both; every
    # mapped page has its deciding sentence in uses-why.md
    if len(mapped) == len(mdcourse.USES):   # the full site, not an edition
        crs = {}
        for pid in pages:
            c = next((h['home_id'] for h in ALL_COURSES if h['family'] == 'history' and re.match(re.escape(h['prefix']) + r'\d', pid)), None) or next((k for k in REL_COURSES if (SITE / k / f'{pid}.html').exists()), None)   # a history report by its course's prefix
            crs.setdefault(c, []).append(pid)
        inuse = {}
        for c, pids in crs.items():
            if c is None:   # a course without `reliefs` (REL_COURSES) (Sport Psychology for Coaches until row G-R-SP, public-courses.md rule 10) shows no relief
                continue
            ids = {mapped[p] for p in pids if p in mapped}
            need = 10 if len(pids) >= 10 else sum(1 for p in pids if p in mapped)
            inuse[c] = len(ids)
            if len(ids) < need: bad.append(f'{c}: {len(ids)} outlines in use, fewer than {need}')
        used = set(mapped.values())
        for o in lib['outlines']:
            if o['id'] not in used and not o.get('spare'): bad.append(f'{o["id"]}: neither in use nor marked spare')
            if o['id'] in used and o.get('spare'): bad.append(f'{o["id"]}: in use and marked spare')
        why = (OUTL / 'uses-why.md').read_text()
        for pid, oid in mapped.items():
            if not re.search(r'\(`' + re.escape(pid) + r'`\) \| ' + re.escape(oid) + r' \| \d+ \| \S', why): bad.append(f'{pid}: no deciding sentence for {oid} in uses-why.md')
        print(f'reliefs: outlines in use per course {", ".join(f"{c} {n}" for c, n in inuse.items())}; {len(used)} of {len(lib["outlines"])} in use, '
              f'{sum(1 for o in lib["outlines"] if o.get("spare"))} spare; {len(mapped)} deciding sentences in uses-why.md')
    for pid, h in pages.items():
        n = h.count('<figure class="relief-fig"')
        if n != (1 if pid in mapped else 0): bad.append(f'{pid}: {n} reliefs, {"1" if pid in mapped else "none"} mapped')
    errs, low, phs = [], 1e9, []
    sizes = {}
    lb = {o['id']: o for o in lib['outlines']}
    for name, w, h, mobile in REL_WIDTHS:
        ctx, pg, _ = new_page(None, br, errs, f'reliefs {name}', w, h, mobile, motion=True)
        for pid, oid in mapped.items():
            if not SCOPE.has(pid): continue   # S-DEC4: the run's pages (the library and the mapping above are checked whole)
            o = lb[oid]
            want = dict(id=oid, caption=mdcourse.relief_caption(o), credit=o['credit'], kw=o['keywords'], lic=o['licence_url'], licence=o['licence'])
            pg.evaluate(f"localStorage.removeItem('{THEME_KEY}'); document.documentElement.removeAttribute('data-theme')")
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                for motion in (False, True):
                    pg.emulate_media(reduced_motion='no-preference' if motion else 'reduce'); pg.wait_for_timeout(20)
                    r = pg.evaluate(REL_JS, [pid, list(POSES), BTIME, motion, want])
                    tag = f'{pid} {name} {theme}{" motion" if motion else ""}'
                    bad += [f'{tag}: {b}' for b in r['bad'][:4]]
                    if r.get('scroll') and r['scroll'][0] > r['scroll'][1]: bad.append(f'{tag}: the page is {r["scroll"][0]} px wide on a {r["scroll"][1]} px screen')
                    if motion and 'minclear' in r:
                        low = min(low, r['minclear'])
                        if any(abs(r['ph'] - x) < 1e-6 for x in r['sepph']): bad.append(f'{tag}: the relief shares a phase with a separator')
                    sizes[pid] = r['bytes']
                    if theme == 'dark' and not motion: phs.append(f'{pid} {name} {r.get("w", 0):.0f}x{r.get("h", 0):.0f}')
        pg.emulate_media(reduced_motion='reduce')
        ctx.close()
    fails += ['reliefs ' + b for b in bad[:30]]
    if len(bad) > 30: fails.append(f'reliefs: {len(bad) - 30} more')
    if errs: fails.append('reliefs: console errors: ' + ' | '.join(errs[:3]))
    print(f'reliefs: {len(mapped)} mapped pages, {len(SCOPE.only(mapped))} in this run ({", ".join(f"{p} {o} {sizes.get(p, 0):,} B" for p, o in mapped.items() if SCOPE.has(p))}), {len(pages) - len(mapped)} reading pages without one; '
          f'checked at {", ".join(str(x[1]) for x in REL_WIDTHS)} px, dark and light, with and without motion; frames {"; ".join(phs)}; '
          f'the closest line {low:.1f} px from its frame over the poses with motion')


# S-NAV1 step D (22 Nov 2026) · the swell (Pedro: "the core will stay the same... the outward lines are moving away from
# the core proportionally to their distance to the core"): every line illustration drawn by viz.py (a hero's layer, a
# tile's patch, a section separator, an object relief) moves its lines only, each about its rise's core by
# 1 + --d x --topo-grow. LINES_JS reads a drawing's lines as the page draws them: each path's subpaths in the drawing's
# units (viz.py writes M x y, then whole-unit relative steps l dx dy, z for a closed ring), its d and its origin.
LINES_JS = r"""const subpaths = d => { const out = []; let cur = null, x = 0, y = 0; const tk = d.match(/[Mlz]|-?\d*\.?\d+/g) || [];
  for (let i = 0; i < tk.length;) { const t = tk[i];
    if (t === 'M') { x = +tk[i + 1]; y = +tk[i + 2]; cur = {pts: [[x, y]], closed: false}; out.push(cur); i += 3; }
    else if (t === 'l') i++;
    else if (t === 'z') { cur.closed = true; i++; }
    else { x += +tk[i]; y += +tk[i + 1]; cur.pts.push([x, y]); i += 2; } }
  return out; };
const lineOf = p => { const cs = getComputedStyle(p); return {p, d: parseFloat(cs.getPropertyValue('--d')) || 0, o: cs.transformOrigin.split(' ').map(parseFloat), subs: subpaths(p.getAttribute('d') || '')}; };
const scr = (m, x, y) => new DOMPoint(x, y).matrixTransform(m);"""
# the amplitude (px) of the furthest-moving point of a line inside a hero's frame, and the frame's size
SWELL_AMP_JS = r"""(sel) => { """ + LINES_JS + r"""
  const t = document.querySelector(sel), fr = t.getBoundingClientRect(), g = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--topo-grow'));
  const sv = [...t.querySelectorAll(':scope > svg.topo-l')].find(s => getComputedStyle(s).display !== 'none'), m = sv.getScreenCTM();
  let amp = 0;
  sv.querySelectorAll('path').forEach(p => { const l = lineOf(p), o = scr(m, l.o[0], l.o[1]);
    l.subs.forEach(s => s.pts.forEach(([x, y]) => { const q = scr(m, x, y);
      if (q.x >= fr.left && q.x <= fr.right && q.y >= fr.top && q.y <= fr.bottom) amp = Math.max(amp, l.d * g * Math.hypot(q.x - o.x, q.y - o.y)); })); });
  return [amp, Math.round(fr.width), Math.round(fr.height)]; }"""
# one page: every contour drawing in it (the hero's shown layout, the tiles' patches, the separators of every section
# shown at once, the relief), with motion allowed: what animates; each line's d, origin and scale at the top of the
# swell; every join between two lines (an end of one line's open stretch on an end of another's) at each pose; and every
# drawing's lines in its frame at each pose (a hero: each rise's own rings, its closed rings, inside the frame and above
# its fade; a patch, a separator, a relief: every line inside its frame). Under reduced motion: no animation at all.
SWELL_JS = r"""([pid, poses, bt, motion, phone]) => { """ + SWELL_AT_JS + LINES_JS + r"""
  const P = document.getElementById(pid), out = {bad: [], drawings: 0, lines: 0, joins: 0, gap: {}, clear: 1e9, moved: 0};
  if (!P) { out.bad.push('no page'); return out; }
  const whole = P.querySelector('.stepbar .whole'), wasWhole = whole && whole.getAttribute('aria-pressed') === 'true';
  if (whole && !wasWhole) whole.click();   // every section's separator shown at once
  const css = [...document.getAnimations()].filter(a => a.animationName !== undefined);
  if (!motion) { if (css.length) out.bad.push(`under reduced motion ${css.length} animations run (${[...new Set(css.map(a => a.animationName))].join()})`);
    if (whole && !wasWhole) whole.click(); return out; }
  const g = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--topo-grow'));
  css.forEach(a => { const props = [...new Set(a.effect.getKeyframes().flatMap(k => Object.keys(k)).filter(k => !['offset', 'computedOffset', 'easing', 'composite'].includes(k)))];
    if (props.some(x => x !== 'transform' && x !== 'opacity')) out.bad.push(`${a.animationName} animates ${props.join(',')}`); });
  const mine = css.filter(a => a.effect && a.effect.target && P.contains(a.effect.target));
  const allPaths = [...P.querySelectorAll('.topo svg.topo-l path')];
  mine.forEach(a => { if (a.animationName === 'topo-swell' && !allPaths.includes(a.effect.target)) out.bad.push(`a swell on ${a.effect.target.tagName}, not a contour line`);
    else if (a.animationName !== 'topo-swell' && a.animationName !== 'harea' && a.animationName !== 'harea-y') out.bad.push(`${a.animationName} runs on ${a.effect.target.tagName}.${a.effect.target.getAttribute('class')}`); });   // a spot or planned ring (a circle) never moves
  const swell = new Map(mine.filter(a => a.animationName === 'topo-swell').map(a => [a.effect.target, a]));
  const vis = e => !!e && e.getBoundingClientRect().width > 0 && getComputedStyle(e).display !== 'none';
  const draws = [...P.querySelectorAll('.topo')].filter(vis).map(t => ({t, sv: [...t.querySelectorAll(':scope > svg.topo-l')].find(s => getComputedStyle(s).display !== 'none')})).filter(x => x.sv);
  const kind = t => t.classList.contains('relief') ? 'relief' : t.classList.contains('topo-sep') ? 'sep' : t.classList.contains('topo-patch') ? 'patch' : 'hero';
  const lines = new Map();
  draws.forEach(({t, sv}) => { out.drawings++;
    const ps = [...sv.querySelectorAll('path')], ls = ps.map(lineOf); lines.set(t, ls); out.lines += ps.length;
    const miss = ps.filter(p => !swell.has(p) && (p.getAttribute('d') || '').length);
    if (miss.length) out.bad.push(`${kind(t)}: ${miss.length} of its ${ps.length} lines do not swell`);
    const delays = new Set(ps.filter(p => swell.has(p)).map(p => swell.get(p).effect.getTiming().delay));
    if (delays.size > 1) out.bad.push(`${kind(t)}: its lines swell at ${delays.size} phases, not one`);
    const ds = ls.map(l => l.d);
    if (ds.some(d => !(d >= 0 && d <= 1))) out.bad.push(`${kind(t)}: a --d outside 0 to 1`);
    // the relief's outer halo is 1; in a contour drawing a line shared with a rise of one level (its only line is its
    // innermost, 0) blends below 1, so there the outermost line only has to move
    if (kind(t) === 'relief' ? Math.max(...ds) !== 1 : (ds.length > 1 && sv.querySelector('g.ct-rise path[d^="M"]') && !(Math.max(...ds) > 0))) out.bad.push(`${kind(t)}: its outermost line has --d ${Math.max(...ds)}`);
    if (kind(t) !== 'relief' && ls.length && !ls.some(l => l.d === 0) && sv.querySelector('g.ct-rise path')) out.bad.push(`${kind(t)}: no line stands still (an innermost line has --d 0)`);
    sv.querySelectorAll('g.ct-rise[data-at]').forEach(gr => { const at = gr.getAttribute('data-at').split(' ').map(Number);   // a line of the rise's own moves about its core
      gr.querySelectorAll('path').forEach(p => { const l = ls[ps.indexOf(p)]; if (!l.d || p.style.getPropertyValue('--o')) return;
        if (Math.abs(l.o[0] - at[0]) > .5 || Math.abs(l.o[1] - at[1]) > .5) out.bad.push(`${kind(t)} ${gr.dataset.label}: a line of its own moves about ${l.o}, its core is ${at}`); }); });
  });
  // the joins: an end of an open stretch on the end of another line's stretch, at rest
  const ends = [];
  draws.forEach(({t}) => lines.get(t).forEach(l => l.subs.forEach(s => { if (!s.closed && s.pts.length > 1) { ends.push([t, l, s.pts[0]]); ends.push([t, l, s.pts[s.pts.length - 1]]); } })));
  const key = new Map(); ends.forEach(e => { const kk = e[2][0] + ',' + e[2][1]; if (!key.has(kk)) key.set(kk, []); key.get(kk).push(e); });
  const joins = []; key.forEach(es => { for (let i = 0; i < es.length; i++) for (let j = i + 1; j < es.length; j++) if (es[i][0] === es[j][0] && es[i][1] !== es[j][1]) joins.push([es[i], es[j]]); });
  out.joins = joins.length;
  const anims = [...swell.values()];
  for (const p of poses) {
    anims.forEach(a => swellAt(a, p, bt));
    let gap = 0;
    joins.forEach(([a, b]) => { const qa = scr(a[1].p.getScreenCTM(), ...a[2]), qb = scr(b[1].p.getScreenCTM(), ...b[2]); gap = Math.max(gap, Math.hypot(qa.x - qb.x, qa.y - qb.y)); });
    out.gap[p] = Math.round(gap * 1000) / 1000;
    if (gap > .5) out.bad.push(`at pose ${p} a join opens ${gap.toFixed(2)} px`);
    draws.forEach(({t, sv}) => { const fr = t.getBoundingClientRect(), k = kind(t);
      if (k === 'hero') {   // each rise's own rings (its closed stretches) inside the frame and above its fade; the home's hero is
        if (phone || pid === 'home') return;   // not fitted to its frame (P92: its rises' peaks are placed in the phone's view; History's outer rings span it), as check_topo
        sv.querySelectorAll('g.ct-rise').forEach(gr => gr.querySelectorAll('path').forEach(pth => { const l = lineOf(pth), m = pth.getScreenCTM();
          l.subs.forEach(s => { if (!s.closed) return; s.pts.forEach(([x, y]) => { const q = scr(m, x, y);
            const c = Math.min(q.x - fr.left, fr.right - q.x, q.y - fr.top, fr.top + .9 * fr.height - q.y); out.clear = Math.min(out.clear, c);
            if (c < -.5) { out.bad.push(`hero ${gr.dataset.label}: at pose ${p} its own ring leaves the frame or reaches its fade by ${(-c).toFixed(1)} px`); } }); }); })); }
      else { let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
        sv.querySelectorAll('path, circle').forEach(e => { const q = e.getBoundingClientRect(); if (!q.width && !q.height) return; x0 = Math.min(x0, q.left); y0 = Math.min(y0, q.top); x1 = Math.max(x1, q.right); y1 = Math.max(y1, q.bottom); });
        const c = Math.min(x0 - fr.left, y0 - fr.top, fr.right - x1, fr.bottom - y1); out.clear = Math.min(out.clear, c);
        if (c < -.5) out.bad.push(`${k}: at pose ${p} its lines leave the frame by ${(-c).toFixed(1)} px`); } });
    if (p === 1) draws.forEach(({t}) => lines.get(t).forEach(l => { const m = new DOMMatrix(getComputedStyle(l.p).transform === 'none' ? undefined : getComputedStyle(l.p).transform);
      if (!l.d) { if (!m.isIdentity) out.bad.push(`${kind(t)}: an innermost line (--d 0) moves (${getComputedStyle(l.p).transform})`); }
      else { out.moved++; if (Math.abs(m.a - (1 + l.d * g)) > 2e-3 || Math.abs(m.d - (1 + l.d * g)) > 2e-3 || Math.abs(m.b) > 1e-6 || Math.abs(m.c) > 1e-6) out.bad.push(`${kind(t)}: a line of --d ${l.d} is at scale ${m.a.toFixed(4)} at the top of the swell, not ${(1 + l.d * g).toFixed(4)}`); } }));
  }
  anims.forEach(a => a.play());
  if (whole && !wasWhole) whole.click();
  return out; }"""


def swell_pages():
    """S-NAV1 step D: the pages check_swell visits: the home, the first area page (an edition of one track has none),
    the first sampled course home, What's new, and the first reading page that shows an object relief (its separators
    with it)."""
    import mdcourse
    shell = (SITE / 'index.html').read_text()
    reads = re.findall(r'<section class="panel[^"]*" id="([^"]+)"[^>]*data-kind="report"', shell)
    rel = next((p for p in reads if p in mdcourse.USES), None)
    course = next((x for x in SAMPLE if x in HIST_HOMES or x in home_expect()['courses']), None)
    return [x for x in ['home'] + AREA_IDS[:1] + [course, 'new', rel] if x]


SWELL_WIDTHS = [('phone320', 320, 640, True), ('phone', 390, 844, True), ('tablet', 768, 1024, True), ('desktop', 1280, 800, False)]

def check_swell(br, fails, pages=None):
    """S-NAV1 step D: SWELL_JS on the home, an area page, a course home, What's new and a reading page with a relief and
    separators (swell_pages), at 320, 390, 768 and 1280 px, dark and light, with motion allowed and under reduced
    motion: with motion, only transform and opacity animate on the page and only the area words and the lines move;
    every line of every shown drawing swells, one phase a drawing; every --d is 0 to 1, a relief's outer halo at 1, a
    contour drawing's outermost line moving (a line it shares with a rise of one level, whose only line is its innermost
    and so 0, blends below 1) and an innermost at 0, and a rise's own lines move about its core; at the five poses of the swell
    (POSES) no join between two lines opens more than 0.5 px, every patch's, separator's and relief's lines stay inside
    its frame and every hero rise's own rings inside the hero's frame and above its fade (from 390 px, and not on the
    home, whose hero is not fitted to its frame, as check_topo);
    at the top of the swell an innermost line has not moved and every other is at 1 + d x --topo-grow; under reduced
    motion no animation runs at all; and (S-NAV1 step G) every relief outline of the library moves, --d > 0. Prints each
    page's joins, its widest gap at each pose and its closest clearance."""
    pages = pages or swell_pages()
    errs, bad, rows = [], [], {}
    # S-NAV1 step G (the fresh check's finding 5): every relief outline (level 0) in the library moves, d > 0 as the page
    # carries it (two decimals), a piece with no level inside its outline too (trireme, toga, bough)
    lib, still = json.loads((OUTL / 'outlines.json').read_text())['outlines'], []
    for o in lib:
        ls = viz.rel_lines(json.loads((OUTL / f'{o["id"]}.json').read_text())['lines'])
        n = sum(1 for ln, dl, _ in ls if ln['lv'] == 0 and not round(dl, 2) > 0)
        if n: still.append(f'{o["id"]} ({n})')
    if still: fails.append(f'swell: relief outlines that do not move (--d 0): {", ".join(still)}')
    print(f'swell: every outline of the {len(lib)} in the library moves (its outline rings at --d > 0)' if not still else f'swell: outlines held still: {still}')
    for name, w, h, mobile in SWELL_WIDTHS:
        for motion in (True, False):
            ctx, pg, _ = new_page(None, br, errs, f'swell {name}', w, h, mobile, motion=motion)
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                for pid in pages:
                    pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(150)
                    if pid in AREA_IDS or pid == 'home': pg.evaluate(f"document.querySelectorAll({PLANNED_SEL!r}).forEach(d => d.open = true)"); pg.wait_for_timeout(60)
                    r = pg.evaluate(SWELL_JS, [pid, list(POSES), BTIME, motion, w < 390])
                    tag = f'{pid} {name} {theme}{" motion" if motion else " reduced"}'
                    bad += [f'{tag}: {b}' for b in r['bad'][:4]]
                    if motion:
                        rw = rows.setdefault(pid, dict(drawings=0, lines=0, joins=0, gap=0.0, clear=1e9, moved=0, runs=0))
                        rw['runs'] += 1; rw['drawings'] = max(rw['drawings'], r['drawings']); rw['lines'] = max(rw['lines'], r['lines']); rw['joins'] = max(rw['joins'], r['joins'])
                        rw['gap'] = max([rw['gap']] + list(r['gap'].values())); rw['clear'] = min(rw['clear'], r['clear']); rw['moved'] = max(rw['moved'], r['moved'])
                        rw.setdefault('gaps', {})
                        for k_, v_ in r['gap'].items(): rw['gaps'][k_] = max(rw['gaps'].get(k_, 0), v_)
                    if pid in AREA_IDS or pid == 'home': pg.evaluate(f"document.querySelectorAll({PLANNED_SEL!r}).forEach(d => d.open = false)")
            ctx.close()
    fails += ['swell ' + b for b in bad[:30]]
    if len(bad) > 30: fails.append(f'swell: {len(bad) - 30} more')
    if errs: fails.append('swell: console errors: ' + ' | '.join(errs[:3]))
    for pid, rw in rows.items():
        print(f'swell {pid}: {rw["drawings"]} drawings, {rw["lines"]} lines ({rw["moved"]} moving), {rw["joins"]} joins; widest join at each pose '
              + ', '.join(f'{k}: {v:.3f} px' for k, v in sorted(rw.get('gaps', {}).items())) + f'; closest line {rw["clear"]:.1f} px inside its frame; {rw["runs"]} runs with motion')
    print(f'swell: {len(pages)} pages ({", ".join(pages)}) at {", ".join(str(x[1]) for x in SWELL_WIDTHS)} px, dark and light, with motion and under reduced motion')
    return rows


# S-NAV1 step G (the fresh check's finding 1): a drawing out of view holds still. shell.js's IntersectionObserver marks
# every .topo out of the viewport .off, and theme 4i pauses its lines' swell there. PAUSE_JS: each drawing of the page
# shown (its shown layout), whether it is in the viewport (2 px clear of an edge, so an edge case reads either way), its
# .off, its swells' play states and current times; and how many drawings of hidden panels are not marked .off.
PAUSE_JS = r"""(pid) => { const P = document.getElementById(pid), out = {draws: [], hiddenOn: 0, swells: 0};
  if (!P) return out;
  const vh = innerHeight, vw = innerWidth;
  out.swells = document.getAnimations().filter(a => a.animationName === 'topo-swell').length;
  [...P.querySelectorAll('.topo')].forEach((t, i) => {
    const sv = [...t.querySelectorAll(':scope > svg.topo-l')].find(s => getComputedStyle(s).display !== 'none'); if (!sv) return;
    const r = t.getBoundingClientRect(); if (!r.width || !r.height) return;
    const inView = r.bottom > 2 && r.top < vh - 2 && r.right > 2 && r.left < vw - 2, outView = r.bottom < -2 || r.top > vh + 2 || r.right < -2 || r.left > vw + 2;
    if (!inView && !outView) return;
    const an = t.getAnimations({subtree: true}).filter(a => a.animationName === 'topo-swell');
    out.draws.push({i, view: inView, kind: t.classList.contains('relief') ? 'relief' : t.classList.contains('topo-sep') ? 'sep' : t.classList.contains('topo-patch') ? 'patch' : 'hero',
      off: t.classList.contains('off'), st: [...new Set(an.map(a => a.playState))].join(), n: an.length, ct: an.slice(0, 3).map(a => a.currentTime)}); });
  out.hiddenOn = [...document.querySelectorAll('.panel[hidden] .topo')].filter(t => !t.classList.contains('off')).length;
  return out; }"""


# the page scrolled so its last drawing that moves (not a planned one, rings only) stands in the middle of the window
# (its hero then out of view)
PAUSE_LAST_JS = r"""(pid) => { const ts = [...document.getElementById(pid).querySelectorAll('.topo')].filter(t => t.getBoundingClientRect().height && t.getAnimations({subtree: true}).length);
  const r = ts[ts.length - 1].getBoundingClientRect(); window.scrollTo(0, scrollY + r.top + r.height / 2 - innerHeight / 2); }"""


def _pause_probe(fr, pid, label, fails, need=('on', 'off')):
    """Two looks at the page 300 ms apart: every drawing in view is not .off, its swells running and moving; every one
    out of view .off, its swells paused and still; no drawing of a hidden panel unmarked. Returns (in view, out of view)."""
    fr.wait_for_timeout(400)   # the observer's callbacks after the last scroll or route
    a = fr.evaluate(PAUSE_JS, pid); fr.wait_for_timeout(300); b = fr.evaluate(PAUSE_JS, pid)
    bi = {d['i']: d for d in b['draws']}
    on = off = 0
    for d in a['draws']:
        e = bi.get(d['i'])
        if not e or e['view'] != d['view'] or not d['n']: continue
        if d['view']:
            on += 1
            if d['off'] or d['st'] != 'running' or e['ct'] == d['ct']: fails.append(f'pause {label} {pid}: a {d["kind"]} in view is {"off" if d["off"] else "on"}, its swells {d["st"]}, {"still" if e["ct"] == d["ct"] else "moving"}; expected on, running, moving')
        else:
            off += 1
            if not d['off'] or d['st'] != 'paused' or e['ct'] != d['ct']: fails.append(f'pause {label} {pid}: a {d["kind"]} out of view is {"off" if d["off"] else "on"}, its swells {d["st"]}, {"still" if e["ct"] == d["ct"] else "moving"}; expected off, paused, still')
    if b['hiddenOn']: fails.append(f'pause {label} {pid}: {b["hiddenOn"]} drawings of hidden panels are not marked off')
    if 'on' in need and not on: fails.append(f'pause {label} {pid}: no drawing in view to check')
    if 'off' in need and not off: fails.append(f'pause {label} {pid}: no drawing out of view to check')
    return on, off


def check_pause(br, fails, w=390, h=844, theme='dark'):
    """S-NAV1 step G: at 390 px (or w by h, in theme) with motion allowed, on the home and a course home (its hero in view, its tiles' patches
    below) and the same course home scrolled to its last drawing (the hero then out of view, that patch in it), after a route
    through history (the course home, then back to the home) and inside a sandboxed iframe (allow-scripts
    allow-same-origin, as check_history): every drawing in view runs and moves, every one out of view is .off, paused and
    still, every drawing of a hidden panel .off; under reduced motion no swell exists at all, scrolled or not."""
    course = next((x for x in swell_pages() if x not in ('home', 'new') and x not in AREA_IDS and x in (HIST_HOMES | set(home_expect()['courses']))), None)
    if not course: fails.append('pause: no course home to check'); return
    errs, seen = [], []
    light = f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')"
    def walk(fr, label):
        if theme == 'light': fr.evaluate(light)
        fr.evaluate(f"location.hash = '{course}'"); fr.wait_for_function(READY_JS, timeout=15000)
        fr.evaluate('window.scrollTo(0, 0)'); seen.append(_pause_probe(fr, course, label, fails))
        fr.evaluate(PAUSE_LAST_JS, course); seen.append(_pause_probe(fr, course, label + ' at its last drawing', fails))
        fr.evaluate('history.back()'); fr.wait_for_function(READY_JS, timeout=15000)
        fr.evaluate('window.scrollTo(0, 0)'); seen.append(_pause_probe(fr, 'home', label + ' back home', fails, need=('on',)))
    tag = f'{w} {theme}'
    ctx, pg, _ = new_page(None, br, errs, 'pause', w, h, w < 1100, motion=True)
    ready(pg); seen.append(_pause_probe(pg, 'home', tag, fails, need=('on',)))
    walk(pg, tag)
    ctx.close()
    ctx, pg, _ = new_page(None, br, errs, 'pause reduced', w, h, w < 1100, motion=False)
    pg.evaluate(f"location.hash = '{course}'"); ready(pg)
    for y in ('0', 'document.documentElement.scrollHeight'):
        pg.evaluate(f'window.scrollTo(0, {y})'); pg.wait_for_timeout(400)
        n = pg.evaluate(PAUSE_JS, course)['swells']
        if n: fails.append(f'pause reduced {course}: {n} swells exist under reduced motion')
    ctx.close()
    ctx = br.new_context(viewport={'width': w + 30, 'height': h + 56}, color_scheme='dark', reduced_motion='no-preference')
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
    ctx.route('**/fonts.gstatic.com/**', font_file)
    host = URL.replace('index.html', '__frame_pause.html')
    ctx.route(host, lambda r: r.fulfill(status=200, content_type='text/html',
              body=f'<!DOCTYPE html><iframe sandbox="allow-scripts allow-same-origin" src="index.html#home" style="width:{w}px;height:{h}px;border:0"></iframe>'))
    pg = ctx.new_page(); pg.on('pageerror', lambda e: errs.append(f'pause iframe: {e}')); pg.goto(host); pg.wait_for_timeout(300)
    fr = pg.frames[1]; fr.wait_for_function(READY_JS, timeout=15000)
    seen.append(_pause_probe(fr, 'home', tag + ' iframe', fails, need=('on',)))
    walk(fr, tag + ' iframe')
    ctx.close()
    if errs: fails.append('pause: console errors: ' + ' | '.join(errs[:3]))
    print(f'pause: {course} and the home at {w} px {theme}, top level and in a sandboxed iframe, with a route back through history: '
          f'{sum(a for a, _ in seen)} drawings in view and {sum(b for _, b in seen)} out of view checked (in, out per look: {seen}); none under reduced motion')


def check_reading(br, fails):
    """P68 on every unit and report of every course, at phone width: STEP_JS and SRC_JS on each; then, on one page of
    each course, a deep link to a section and to Sources on a fresh load, and Continue resuming at the section."""
    errs = []
    ctx, pg, _ = new_page(None, br, errs, 'reading', 390, 844, True)
    pg.evaluate('localStorage.clear()')
    ids = SCOPE.only(pg.eval_on_selector_all('.panel[data-kind="report"]', 'ps => ps.map(p => p.id)'))   # S-DEC4: the run's pages
    nsec, bad = 0, []
    for pid in ids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(20)
        res = pg.evaluate(STEP_JS, pid); nsec += res['n']
        bad += [f'{pid}: {b}' for b in res['bad'][:4]]
        bad += [f'{pid}: {b}' for b in pg.evaluate(SRC_JS, pid)]
    fails += ['reading ' + b for b in bad[:20]]
    # one page per course: deep links and Continue
    sample = []
    for c in COURSES:
        ctxs = [c['home_id']] if c['family'] == 'history' else [f"{c.get('prefix', c['id'])}-{k.lower()}" for k in c['tracks']]
        for cx in ctxs:
            rs = [i for i in ids if pg.evaluate(f"document.getElementById('{i}').dataset.ctx") == cx]
            if rs: sample.append((cx, rs[len(rs) // 2]))
    retried, landed, notes = [], 0, 0
    for cx, pid in sample:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
        n = pg.evaluate(f"document.querySelectorAll('#{pid} .report.steps > .sec').length")
        if n < 2: continue
        k = min(2, n - 1)
        sid = pg.evaluate(f"document.querySelectorAll('#{pid} .report.steps > .sec')[{k}].querySelector('h2').id")
        pg.evaluate('localStorage.clear()')
        sec = fresh_land(pg, sid, retried)
        st = pg.evaluate(f"[+document.getElementById('{pid}').dataset.step, [...document.querySelectorAll('#{pid} .report.steps > .sec')].filter(s => s.offsetHeight > 0).length]")
        if sec[0] != pid or not lands(sec) or st != [k, 1]: fails.append(f'reading: deep link #{sid} gave panel {sec[0]}, top {sec[2]}, step and sections shown {st}, expected {pid} at section {k + 1}')
        else: landed += 1
        # the accordion is at the page's end, so on a short section it lands in view rather than at the top
        pg.goto(URL + f'#{pid}-sources'); pg.reload(); ready(pg); sec = pg.evaluate(SETTLE_JS, f'{pid}-sources')
        op = pg.evaluate(f"!!document.getElementById('{pid}-sources') && document.getElementById('{pid}-sources').open")
        if sec[0] != pid or not op or sec[2] is None or not -5 <= sec[2] <= 844 - 60: fails.append(f'reading: deep link #{pid}-sources gave panel {sec[0]}, top {sec[2]}, the accordion open {op}')
        # P73: the writer's opening note, where the page has one, is closed until a link opens it, and a deep link lands
        if pg.evaluate(f"!!document.getElementById('{pid}-note')"):
            pg.goto(URL + f'#{pid}'); pg.reload(); ready(pg)
            if pg.evaluate(f"document.getElementById('{pid}-note').open"): fails.append(f'reading: #{pid}-note is open before any link opens it')
            pg.goto(URL + f'#{pid}-note'); pg.reload(); ready(pg); sec = pg.evaluate(SETTLE_JS, f'{pid}-note')
            op = pg.evaluate(f"document.getElementById('{pid}-note').open")
            if sec[0] != pid or not op or sec[2] is None or not -5 <= sec[2] <= 844 - 60: fails.append(f'reading: deep link #{pid}-note gave panel {sec[0]}, top {sec[2]}, the note open {op}')
            else: notes += 1
        # Continue: read to section n, leave for the course home, come back through its Continue button; then a reload
        j = n - 1
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg)
        pg.evaluate(f"[...document.querySelectorAll('#{pid} .seclist a')][{j}].click()")
        pg.evaluate(f"location.hash = '{cx}'"); ready(pg); pg.wait_for_timeout(50)
        pg.click(f'#{cx} .hbtn.cont'); ready(pg); pg.wait_for_timeout(50)
        st = pg.evaluate(f"[[...document.querySelectorAll('.panel')].find(p => !p.hidden).id, +document.getElementById('{pid}').dataset.step, [...document.querySelectorAll('#{pid} .report.steps > .sec')].findIndex(s => s.offsetHeight > 0)]")
        if st != [pid, j, j]: fails.append(f'reading: Continue on {cx} after reading section {j + 1} of {pid} gave (panel, step, section shown) {st}')
        pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(50)
        st = pg.evaluate(f"[+document.getElementById('{pid}').dataset.step, [...document.querySelectorAll('#{pid} .report.steps > .sec')].findIndex(s => s.offsetHeight > 0)]")
        if st != [j, j]: fails.append(f'reading: reloading #{pid} after section {j + 1} gave (step, section shown) {st}')
    if errs: fails.append('reading: console errors: ' + ' | '.join(errs[:3]))
    if retried: print(f'reading: fresh-load anchors that landed only on the retry: {", ".join(retried)}')
    print(f'reading: {len(ids)} units and reports, {nsec} sections, each reached by next, previous and the menu, "Whole unit" on and off, '
          f'both accordions closed after the text and Sources opened by its links; deep links to a section ({landed} of {len(sample)}), to Sources and to the opening note ({notes}), '
          f'and Continue and a reload resuming at the section, on one page of each course ({", ".join(p for _, p in sample)})')
    ctx.close()

def check_split(br, fails):
    """In the browser: a stub is empty until opened, its file is fetched once and kept, a section link into an unopened
    report loads it and lands on the section, a failed fetch shows the retry state and the retry loads it. S-DEC4: on a
    history course of the edition with reports 2.3 to 2.5, 5.2 and 5.5 (LEAD); an edition without one checks the same
    on a markdown course's reading pages (check_split_md) and says so."""
    if LEAD is None:
        print('split: no history course with reports ' + ', '.join(SPLIT_MODS) + ' in this edition; the history split checks '
              '(report pager, syllabus, course-home continue) are left out and the stub checks run on a markdown course')
        return check_split_md(br, fails)
    L, S = LEAD, SECOND
    r23, r24, r25 = (rid(L, m) for m in ('2.3', '2.4', '2.5'))
    f23, f24, f25 = (f'{L["home_id"]}/r-{m}.html' for m in ('2.3', '2.4', '2.5'))
    hits, fail = {}, {'on': False}
    def handler(route):
        u = route.request.url.split(str(SERVER.server_port), 1)[1]
        hits[u] = hits.get(u, 0) + 1
        if fail['on'] and u == '/' + f25: route.fulfill(status=503, body='down'); return
        if fail.get('home') and u == f'/{S["home_id"]}/home.html': route.fulfill(status=503, body='down'); return
        route.continue_()
    errs = []
    ctx, pg, _ = new_page(None, br, errs, 'split', 390, 844, True)
    ctx.route('**/*.html', handler)
    stub = pg.evaluate(f"(() => {{ const p = document.getElementById('{r23}'); return [p.getAttribute('data-src'), p.innerHTML.length, p.hasAttribute('data-loaded')]; }})()")
    if stub != [f23, 0, False]: fails.append(f'split: #{r23} before opening is {stub}, expected an empty stub fetching {f23}')
    pg.evaluate(f"location.hash = '{r23}'"); ready(pg)
    got = pg.evaluate(f"[document.getElementById('{r23}').hasAttribute('data-loaded'), document.querySelectorAll('#{r23} .report h2').length, document.querySelector('#{r23} .pager').children.length]")
    if not (got[0] and got[1] and got[2] == 2): fails.append(f'split: #{r23} after opening (loaded, sections, pager links) = {got}')
    pg.evaluate(f"location.hash = '{L['home_id']}'"); ready(pg); pg.evaluate(f"location.hash = '{r23}'"); ready(pg)
    if hits.get('/' + f23) != 1: fails.append(f'split: {f23} fetched {hits.get("/" + f23)} times, expected once')
    pg.wait_for_timeout(700)   # the next report is fetched in the background
    if not pg.evaluate(f"document.getElementById('{r24}').hasAttribute('data-loaded')"): fails.append(f'split: the next report (#{r24}) was not prefetched')
    pg.evaluate(f"document.querySelector('#{r23} .pager a.next').click()"); ready(pg)   # P68: the cards show after the last section; clicked as a link
    if pg.evaluate("location.hash") != f'#{r24}' or hits.get('/' + f24) != 1: fails.append(f'split: pager to #{r24}: hash {pg.evaluate("location.hash")}, fetched {hits.get("/" + f24)} times')
    # a section link into a report not yet opened, on a fresh load
    retried = []
    deep, dpan = (rid(S, '1.2') + '-2', rid(S, '1.2')) if S else (rid(L, '5.2') + '-2', rid(L, '5.2'))   # P70: an edition without a second history course checks one of LEAD's
    sec = fresh_land(pg, deep, retried)
    if sec[0] != dpan or not lands(sec): fails.append(f'split: #{deep} on a fresh load gave panel {sec[0]}, section found {sec[1]}, top {sec[2]}')
    # a syllabus is a stub too (P20): empty until opened, fetched once, its prompts and copy buttons present
    Y = S or L
    sy, sc, sa = Y['syl_id'], Y['home_id'], f'{Y["syl_anchor"]}-u3'
    stub = pg.evaluate(f"(() => {{ const p = document.getElementById('{sy}'); return [p.getAttribute('data-src'), p.innerHTML.length, (p.getAttribute('data-anchors') || '').split(' ').includes('{sa}')]; }})()")
    if stub != [f'{sc}/syllabus.html', 0, True]: fails.append(f'split: #{sy} before opening is {stub}, expected an empty stub fetching {sc}/syllabus.html with its anchors')
    pg.evaluate(f"location.hash = '{sy}'"); ready(pg)
    got = pg.evaluate(f"[document.getElementById('{sy}').hasAttribute('data-loaded'), document.querySelectorAll('#{sy} article.smod pre').length, document.querySelectorAll('#{sy} button.copy').length]")
    if not (got[0] and got[1] >= 80 and got[1] == got[2]): fails.append(f'split: #{sy} after opening (loaded, prompts, copy buttons) = {got}')
    pg.evaluate(f"location.hash = '{sc}'"); ready(pg); pg.evaluate(f"location.hash = '{sy}'"); ready(pg)
    if hits.get(f'/{sc}/syllabus.html') != 1: fails.append(f'split: {sc}/syllabus.html fetched {hits.get(f"/{sc}/syllabus.html")} times, expected once')
    # a link into an unopened syllabus (a unit anchor) and into unopened briefs (a brief's card), on a fresh load
    links = ([(f'{S["syl_anchor"]}-u3', S['syl_id'])] if S else []) + [(f'{L["syl_anchor"]}-{r23}', L['syl_id'])]
    if MDNAV:   # each live sub-course's briefs page, at the brief of its second unit (S-DEC4: was b-a2 and b-b3)
        units = {sc_['key']: sc_['units'] for sc_ in pack.load(MDNAV).COURSES}
        links += [(ba + units[k][min(1, len(units[k]) - 1)][0].lower(), bp) for _, _, k, bp, ba in MDSUBS]
    links += [(f'{L["home_id"]}-u3', L['home_id'])] + ([(f'{S["home_id"]}-u1', S['home_id'])] if S else [])
    for h, want in links:
        if not pg.evaluate(f"!!document.getElementById('{want}')"): continue   # P70: a page the edition does not hold
        sec = fresh_land(pg, h, retried)
        if sec[0] != want or not lands(sec): fails.append(f'split: #{h} on a fresh load gave panel {sec[0]}, element found {sec[1]}, top {sec[2]}')
    # a failed fetch, then the retry
    fail['on'] = True
    pg.evaluate(f"location.hash = '{r25}'"); ready(pg)
    st = pg.evaluate(f"[document.getElementById('{r25}').hasAttribute('data-failed'), !!document.querySelector('#{r25} a.hbtn[data-target=\"{r25}\"]'), document.querySelector('#{r25} h1') && document.querySelector('#{r25} h1').textContent]")
    if not (st[0] and st[1] and st[2]): fails.append(f'split: failed fetch state (failed, retry button, title) = {st}')
    fail['on'] = False
    pg.click(f'#{r25} a.hbtn[data-target="{r25}"]'); ready(pg)
    if not pg.evaluate(f"document.getElementById('{r25}').hasAttribute('data-loaded') && !!document.querySelector('#{r25} .report')"): fails.append('split: retry after a failed fetch did not load the report')
    # a course home is a stub too (P22): its continue button and unit cards arrive with the fetch, and a failed fetch is retried
    if S:
        stub = pg.evaluate(f"(() => {{ const p = document.getElementById('{S['home_id']}'); return p && [p.getAttribute('data-src'), (p.getAttribute('data-anchors') || '').split(' ').includes('{S['home_id']}-u3')]; }})()")
        if stub != [f'{S["home_id"]}/home.html', True]: fails.append(f'split: #{S["home_id"]} stub is {stub}, expected {S["home_id"]}/home.html with its unit-card anchors')
    H_ = L['home_id']
    pg.evaluate("localStorage.clear()"); pg.goto(URL + '#' + H_); pg.reload(); ready(pg); pg.wait_for_timeout(100)
    hm = pg.evaluate(f"[document.getElementById('{H_}').hasAttribute('data-loaded'), document.querySelectorAll('#{H_} details[data-mods]').length, document.querySelectorAll('#{H_} details[data-mods][open]').length, document.querySelector('#{H_} .hbtn.cont').hidden, document.querySelector('#{H_} .hbtn.start').hidden]")
    if not (hm[0] and hm[1] >= 10 and hm[2] == 1 and hm[3] and not hm[4]): fails.append(f'split: #{H_} on a fresh load (loaded, cards, cards open, continue hidden, start shown) = {hm}')
    n0 = hits.get(f'/{H_}/home.html', 0)   # fetched once on this load (earlier fresh loads fetched it too)
    pg.evaluate(f"location.hash = '{r23}'"); ready(pg); pg.evaluate(f"location.hash = '{H_}'"); ready(pg); pg.wait_for_timeout(50)
    hm = pg.evaluate(f"[document.querySelector('#{H_} .hbtn.cont').hidden, document.querySelector('#{H_} .hbtn.cont b').textContent, document.querySelector('#{H_} .hbtn.start').hidden]")
    if hm[0] or not hm[1].startswith('2.3 ') or not hm[2]: fails.append(f'split: #{H_} continue after reading 2.3 (continue hidden, label, start hidden) = {hm}')
    if hits.get(f'/{H_}/home.html', 0) != n0: fails.append(f'split: {H_}/home.html fetched again on a second visit ({hits.get(f"/{H_}/home.html")} in all)')
    fail['home'] = bool(S)   # P70: the failed course-home fetch is tried on the second history course's home, unopened until here; an edition without one skips it
    if not S: print('split: no unopened course home in this edition; the failed course-home fetch is not tried')
    else:
        T_ = S['home_id']
        pg.evaluate(f"location.hash = '{T_}'"); ready(pg)
        st = pg.evaluate(f"[document.getElementById('{T_}').hasAttribute('data-failed'), !!document.querySelector('#{T_} a.hbtn[data-target=\"{T_}\"]')]")
        if st != [True, True]: fails.append(f'split: failed course-home fetch state (failed, retry button) = {st}')
        fail['home'] = False
        pg.click(f'#{T_} a.hbtn[data-target="{T_}"]'); ready(pg); pg.wait_for_timeout(50)
        if not pg.evaluate(f"document.getElementById('{T_}').hasAttribute('data-loaded') && document.querySelectorAll('#{T_} details[data-mods]').length > 5"): fails.append('split: retry after a failed course-home fetch did not load the home')
    other = [e for e in errs if 'fonts.g' not in e and '503' not in e]
    if other: fails.append('split: console errors: ' + ' | '.join(other[:3]))
    if retried: print(f'split: fresh-load anchors that landed only on the retry: {", ".join(retried)}')
    print('split: stubs empty until opened; fetched once, kept and the next report prefetched; links into an unopened report, syllabus, briefs page and course home; failed fetch and retry (report and course home); a course home\'s continue button')
    ctx.close()

def check_split_md(br, fails):
    """S-DEC4: the split on an edition without a history course of LEAD's structure, on the first markdown course with
    three reading pages in one sub-course: its course home and first reading page are empty stubs until opened, each
    fetched once and kept; the next reading page is prefetched and its pager link opens it; a link into an unopened
    briefs page lands on the brief; a failed fetch shows the retry state and the retry loads the page; a failed course
    home fetch likewise."""
    shell = (SITE / 'index.html').read_text()
    reads = re.findall(r'<section class="panel" id="([^"]+)" data-ctx="([^"]+)" data-kind="report"[^>]* data-src="([^"]+)"', shell)
    ctxs = [c_ for c_ in dict.fromkeys(x[1] for x in reads) if sum(1 for x in reads if x[1] == c_) >= 2]
    if not ctxs:
        fails.append('split: no course in this edition has two reading pages; the split is not checked'); return
    cx = ctxs[0]
    mine = [x for x in reads if x[1] == cx]
    (r1, _, f1), (r2, _, f2) = mine[:2]
    # the failed fetch: the course's third reading page, or (a course of two) another of its fetched pages, unopened until then
    r3, f3 = (mine[2][0], mine[2][2]) if len(mine) > 2 else next(((i_, s_) for i_, s_ in re.findall(r'<section class="panel[^"]*" id="([^"]+)" data-ctx="' + re.escape(cx) + r'" data-kind="build"[^>]* data-src="([^"]+)"', shell)
                                                                 if i_ not in (r1, r2)), (None, None))
    homes = {h_: s_ for h_, s_ in re.findall(r'<section class="panel home" id="([^"]+)"[^>]* data-src="([^"]+)"', shell)}
    other_home = next((h_ for h_ in homes if h_ != cx), None)   # a course home not opened before the failed-fetch test
    hits, fail = {}, {'on': False, 'home': False}
    def handler(route):
        u = route.request.url.split(str(SERVER.server_port), 1)[1]
        hits[u] = hits.get(u, 0) + 1
        if fail['on'] and u == '/' + f3: route.fulfill(status=503, body='down'); return
        if fail['home'] and other_home and u == '/' + homes[other_home]: route.fulfill(status=503, body='down'); return
        route.continue_()
    errs, retried = [], []
    ctx, pg, _ = new_page(None, br, errs, 'split', 390, 844, True)
    ctx.route('**/*.html', handler)
    for pid, f in ((cx, homes.get(cx)), (r1, f1)):
        stub = pg.evaluate(f"(() => {{ const p = document.getElementById('{pid}'); return [p.getAttribute('data-src'), p.innerHTML.length, p.hasAttribute('data-loaded')]; }})()")
        if stub != [f, 0, False]: fails.append(f'split: #{pid} before opening is {stub}, expected an empty stub fetching {f}')
    pg.evaluate(f"location.hash = '{cx}'"); ready(pg)
    if not pg.evaluate(f"document.getElementById('{cx}').hasAttribute('data-loaded') && !!document.querySelector('#{cx} a.course')"): fails.append(f'split: #{cx} after opening holds no unit tiles')
    pg.evaluate(f"location.hash = '{r1}'"); ready(pg)
    got = pg.evaluate(f"[document.getElementById('{r1}').hasAttribute('data-loaded'), document.querySelectorAll('#{r1} .report .sec').length]")
    if not (got[0] and got[1]): fails.append(f'split: #{r1} after opening (loaded, sections) = {got}')
    pg.evaluate(f"location.hash = '{cx}'"); ready(pg); pg.evaluate(f"location.hash = '{r1}'"); ready(pg)
    if hits.get('/' + f1) != 1: fails.append(f'split: {f1} fetched {hits.get("/" + f1)} times, expected once')
    if hits.get('/' + homes[cx]) != 1: fails.append(f'split: {homes[cx]} fetched {hits.get("/" + homes[cx])} times, expected once')
    pg.wait_for_timeout(700)   # the next page is fetched in the background
    if not pg.evaluate(f"document.getElementById('{r2}').hasAttribute('data-loaded')"): fails.append(f'split: the next reading page (#{r2}) was not prefetched')
    nx = pg.evaluate(f"(() => {{ const a = document.querySelector('#{r1} .pager a.next'); return a && a.getAttribute('href'); }})()")
    if nx != f'#{r2}': fails.append(f'split: #{r1}\'s pager links {nx}, expected #{r2}')
    else:
        pg.evaluate(f"document.querySelector('#{r1} .pager a.next').click()"); ready(pg)
        if pg.evaluate("location.hash") != f'#{r2}' or hits.get('/' + f2) != 1: fails.append(f'split: pager to #{r2}: hash {pg.evaluate("location.hash")}, fetched {hits.get("/" + f2)} times')
    # a link into an unopened briefs page, on a fresh load: its first anchor
    bm = re.search(r'<section class="panel stack" id="([^"]+)" data-ctx="' + re.escape(cx) + r'"[^>]* data-anchors="([^" ]+)', shell)
    if bm:
        sec = fresh_land(pg, bm.group(2), retried)
        if sec[0] != bm.group(1) or not lands(sec): fails.append(f'split: #{bm.group(2)} on a fresh load gave panel {sec[0]}, element found {sec[1]}, top {sec[2]}')
    else: print(f'split: {cx} has no fetched page with anchors; the link into an unopened page is not tried')
    if r3 is None: fails.append(f'split: {cx} has no third reading page and no other fetched page; the failed fetch is not tried')
    else:
        pg.goto(URL + '#home'); pg.reload(); ready(pg)   # a fresh load: nothing of the course opened or prefetched
        fail['on'] = True
        pg.evaluate(f"location.hash = '{r3}'"); ready(pg)
        st = pg.evaluate(f"[document.getElementById('{r3}').hasAttribute('data-failed'), !!document.querySelector('#{r3} a.hbtn[data-target=\"{r3}\"]')]")
        if st != [True, True]: fails.append(f'split: failed fetch state of #{r3} (failed, retry button) = {st}')
        fail['on'] = False
        pg.click(f'#{r3} a.hbtn[data-target="{r3}"]'); ready(pg)
        if not pg.evaluate(f"document.getElementById('{r3}').hasAttribute('data-loaded') && !document.getElementById('{r3}').hasAttribute('data-failed')"): fails.append(f'split: retry after a failed fetch did not load #{r3}')
    if other_home:
        fail['home'] = True
        pg.evaluate(f"location.hash = '{other_home}'"); ready(pg)
        st = pg.evaluate(f"[document.getElementById('{other_home}').hasAttribute('data-failed'), !!document.querySelector('#{other_home} a.hbtn[data-target=\"{other_home}\"]')]")
        if st != [True, True]: fails.append(f'split: failed course-home fetch state (failed, retry button) = {st}')
        fail['home'] = False
        pg.click(f'#{other_home} a.hbtn[data-target="{other_home}"]'); ready(pg); pg.wait_for_timeout(50)
        if not pg.evaluate(f"document.getElementById('{other_home}').hasAttribute('data-loaded') && !!document.querySelector('#{other_home} a.course')"): fails.append('split: retry after a failed course-home fetch did not load the home')
    else: print('split: no second course home in this edition; the failed course-home fetch is not tried')
    other = [e for e in errs if 'fonts.g' not in e and '503' not in e]
    if other: fails.append('split: console errors: ' + ' | '.join(other[:3]))
    if retried: print(f'split: fresh-load anchors that landed only on the retry: {", ".join(retried)}')
    print(f'split (markdown, {cx}): stubs empty until opened; course home and reading page fetched once and kept, the next page prefetched and its pager link; a link into an unopened page; failed fetch and retry' + (' (reading page and course home)' if other_home else ' (reading page)'))
    ctx.close()

# V1, every kind since P55 (30 Oct 2026): inside every figure, the geometry the eye would otherwise have to check.
#  1. nothing leaves the drawing: no child of the SVG and no text outside its viewBox;
#  2. every text of a box group (<g data-box>, the box its first child: a node, a plate, a bar or a span carrying its
#     label) lies inside that box;
#  3. no two boxes overlap;
#  4. no two texts overlap, and no text outside a box group overlaps a box: a label is never drawn over another label,
#     a bar or a node. A text's box is its em box, which is taller than its ink, so it is inset vertically by a fifth
#     of its height (at most 3 units) on each side before it is compared: two lines of one label sit 13 to 14 apart.
# Measured in the SVG's own units with getBBox, so the width of the page does not matter. Run on the examples page
# (every kind and every fault case P55 added) and, in the phone pass, on every panel that carries figures.
FIG_JS = r'''(sel) => {
  const out = []; const figs = [...document.querySelectorAll(sel + ' figure.viz')];
  const kindOf = f => [...f.classList].find(c => c.startsWith('viz-') && c !== 'viz-wide' && c !== 'viz-numeric').slice(4) + (f.classList.contains('viz-numeric') ? '-numeric' : '');
  const ov = (a, b) => [Math.min(a.x + a.width, b.x + b.width) - Math.max(a.x, b.x), Math.min(a.y + a.height, b.y + b.height) - Math.max(a.y, b.y)];
  const ink = b => { const i = Math.min(3, b.height / 5); return {x: b.x + 0.5, y: b.y + i, width: Math.max(0, b.width - 1), height: Math.max(0, b.height - 2 * i)}; };
  const f1 = v => v.toFixed(1), say = s => `"${s.slice(0, 28)}"`;
  figs.forEach(f => {
    const kind = kindOf(f);
    const sc = f.querySelector('.viz-scroll'), svg = [...sc.querySelectorAll(':scope > svg')].find(s => s.getBoundingClientRect().width > 0) || sc.querySelector('svg'), vb = svg.viewBox.baseVal, T = 0.6;   // P83: the drawing shown at this width
    const outside = b => b.x < -T || b.y < -T || b.x + b.width > vb.width + T || b.y + b.height > vb.height + T;
    [...svg.children].forEach(el => { if (el.tagName === 'defs') return; const b = el.getBBox();
      if (b.width + b.height === 0) return;
      if (outside(b)) out.push(`${kind}: ${el.tagName}.${el.getAttribute('class') || ''} ${say(el.textContent)} leaves the drawing (${f1(b.x)},${f1(b.y)} ${f1(b.width)}x${f1(b.height)} in ${vb.width}x${vb.height})`); });
    const texts = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim()).map(t => [t, t.getBBox()]);
    texts.forEach(([t, b]) => { if (outside(b) && t.parentNode !== svg) out.push(`${kind}: ${say(t.textContent)} leaves the drawing (${f1(b.x)}..${f1(b.x + b.width)} in ${vb.width})`); });
    const boxes = [...svg.querySelectorAll('g[data-box]')].map(g => [g, g.firstElementChild.getBBox()]);
    boxes.forEach(([g, r]) => g.querySelectorAll('text').forEach(t => { if (!t.textContent.trim()) return; const b = t.getBBox();
      if (b.x < r.x - T || b.x + b.width > r.x + r.width + T || b.y < r.y - T || b.y + b.height > r.y + r.height + T)
        out.push(`${kind}: ${say(t.textContent)} outside its box (text ${f1(b.x)}..${f1(b.x + b.width)}, ${f1(b.y)}..${f1(b.y + b.height)}; box ${f1(r.x)}..${f1(r.x + r.width)}, ${f1(r.y)}..${f1(r.y + r.height)})`); }));
    for (let i = 0; i < boxes.length; i++) for (let j = i + 1; j < boxes.length; j++) {
      const [w, h] = ov(boxes[i][1], boxes[j][1]);
      if (w > 0.6 && h > 0.6) out.push(`${kind}: boxes overlap (${say(boxes[i][0].textContent)} and ${say(boxes[j][0].textContent)})`);
    }
    const inks = texts.map(([t, b]) => [t, ink(b), t.closest('g[data-box]')]);
    for (let i = 0; i < inks.length; i++) for (let j = i + 1; j < inks.length; j++) {
      const [w, h] = ov(inks[i][1], inks[j][1]);
      if (w > 0.6 && h > 0.6) out.push(`${kind}: labels overlap (${say(inks[i][0].textContent)} and ${say(inks[j][0].textContent)})`);
    }
    inks.forEach(([t, b, g]) => { if (g) return; boxes.forEach(([bg, r]) => { const [w, h] = ov(b, r);
      if (w > 0.6 && h > 0.6) out.push(`${kind}: ${say(t.textContent)} is drawn over the box ${say(bg.textContent)}`); }); });
  });
  return {n: figs.length, kinds: figs.map(kindOf), bad: out};
}'''

CMP_WIDTHS = [('phone320', 320, 640), ('phone', 390, 844)]
TRACK_WIDTHS = CMP_WIDTHS + [('desktop', 1280, 800)]
CMP_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-compare, figure.viz-bars')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  const bars = [...s.querySelectorAll('rect.viz-bar')].map(b => b.getBoundingClientRect()).filter(r => r.height > 0);
  const vals = [...s.querySelectorAll('text.viz-value')].map(t => t.getBoundingClientRect());
  const tracks = [...s.querySelectorAll('rect.viz-track')].map(t => t.getBoundingClientRect());
  const cross = [];
  for (const v of vals) { const cy = (v.top + v.bottom) / 2;
    const t = tracks.find(t => cy > t.top - 2 && cy < t.bottom + 2);
    if (t && v.left < t.right - 0.5 && v.right > t.right + 0.5) cross.push([v.left, v.right, t.right]); }
  out.push({n: i + 1, kind: f.classList.contains('viz-bars') ? 'bars' : 'compare', frame: [fr.left, fr.right],
            bars: bars.map(r => [r.left, r.right]), vals: vals.map(r => [r.left, r.right]), cross: cross,
            open: sc.scrollLeft, alt: s.classList.contains('viz-alt')}); }
 return out; }"""
def check_phone_figures(br, fails):
    """P97 (12 Nov 2026), widened by P98 (12 Nov 2026) from compare to bars, and from the longest bar to every bar:
    every compare and bars figure, on every page that has one, at 320 and 390 px: the drawing a phone shows (its
    svg.viz-alt) opens unscrolled with every bar and every value whole inside the frame, so the bars are seen to scale
    in one frame. And (P98) at 320, 390 and 1280 px, in the drawing the width shows: no value sits across the end of its
    grey track (wholly on it or wholly beyond its end). Before P97 a compare drew 700 units on a phone; before P98 a
    bars figure's phone drawing was 328 units and scrolled on a 320 px phone, and a value could straddle its track's end."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if SCOPE.has(pid) and (SITE / src).exists() and re.search(r'viz-(compare|bars)\b', (SITE / src).read_text())]   # S-DEC4: the run's pages
    n, nt, bad = 0, 0, []
    for name, w, h in TRACK_WIDTHS:
        errs = []
        phone = w < 768
        ctx, pg, _ = new_page(None, br, errs, name, w, h, phone)
        for pid in pids:
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
            for f in pg.evaluate(CMP_JS, pid):
                where = f'{pid} figure {f["n"]} ({f["kind"]}) at {w} px'
                nt += 1
                for vl, vr, tr in f['cross']:
                    bad.append(f'{where}: a value ({vl:.0f} to {vr:.0f}) sits across the end of its track ({tr:.0f})')
                if not phone:
                    continue
                n += 1
                fl, fr = f['frame']
                if not f['alt']:
                    bad.append(f'{where}: shows its wide drawing, not its phone drawing')
                if f['open'] > 0.5:
                    bad.append(f'{where}: the frame opens scrolled')
                out = [b for b in f['bars'] if b[0] < fl - 0.5 or b[1] > fr + 0.5]
                if out:
                    bad.append(f'{where}: {len(out)} bar(s) not whole in the opening frame ({fl:.0f} to {fr:.0f})')
                vout = [v for v in f['vals'] if v[0] < fl - 0.5 or v[1] > fr + 0.5]
                if vout:
                    bad.append(f'{where}: {len(vout)} value(s) run past the frame')
        if errs: fails.append(f'compare and bars {name}: console errors: ' + ' | '.join(errs[:3]))
        ctx.close()
    fails += bad
    print(f'compare and bars on a phone (P97, P98): {n} figure frames on {len(pids)} pages at 320 and 390 px, every bar and value whole in the opening frame; '
          f'{nt} drawings at 320, 390 and 1280 px checked for a value across its track\'s end; {len(bad)} faults')

MTX_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-matrix')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  if (!s) { out.push({n: i + 1, none: true}); continue; }
  const w = s.getBoundingClientRect().width, over = w > sc.clientWidth + 1;
  const st = [...sc.querySelectorAll(':scope > .viz-stick, :scope > .viz-stickn')].find(x => getComputedStyle(x).display !== 'none');
  const r = {n: i + 1, over, frame: sc.clientWidth, w, stick: st ? st.getBoundingClientRect().width : 0, cls: st ? st.className : ''};
  if (st) { sc.scrollLeft = sc.scrollWidth; await new Promise(r => setTimeout(r, 60));
    const a = st.getBoundingClientRect(), b = sc.getBoundingClientRect(), ss = st.querySelector('svg');
    r.edge = Math.abs(a.left - b.left); r.tall = ss ? Math.abs(ss.getBoundingClientRect().height - s.getBoundingClientRect().height) : 0;
    sc.scrollLeft = 0; sc.dispatchEvent(new Event('scroll')); }
  out.push(r); }
 return out; }"""


def check_matrix_320(br, fails):
    """C1 (15 Nov 2026): every matrix figure, on every page that has one, at 320 px: a drawing that scrolls keeps a label
    column in view (.viz-stickn below 361 px where the matrix has one, else .viz-stick), sticky at the frame's left edge when
    scrolled to the end, as tall as the drawing, and no wider than 45% of the frame, so cells show beside the labels before
    the sideways scroll (BW4 figure 1 showed only its labels at 320 px)."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if SCOPE.has(pid) and (SITE / src).exists() and 'viz-matrix' in (SITE / src).read_text()]   # S-DEC4: the run's pages
    errs, bad, n, sc = [], [], 0, 0
    ctx, pg, _ = new_page(None, br, errs, 'phone320', 320, 640, True)
    for pid in pids:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
        for f in pg.evaluate(MTX_JS, pid):
            n += 1
            where = f'{pid} matrix {f["n"]} at 320 px'
            if f.get('none'):
                bad.append(f'{where}: no drawing shown'); continue
            if not f['over']:
                continue
            sc += 1
            if not f['stick']:
                bad.append(f'{where}: scrolls with no label column in view'); continue
            if f['stick'] > 0.45 * f['frame'] + 0.5:
                bad.append(f'{where}: label column {f["stick"]:.0f} px of a {f["frame"]} px frame (over 45%)')
            if f.get('edge', 0) > 1:
                bad.append(f'{where}: label column {f["edge"]:.0f} px from the frame edge when scrolled to the end')
            if f.get('tall', 0) > 1:
                bad.append(f'{where}: label column not as tall as the drawing')
    if errs: fails.append('matrix 320: console errors: ' + ' | '.join(errs[:3]))
    ctx.close()
    fails += bad
    print(f'matrix figures at 320 px (C1): {n} on {len(pids)} pages, {sc} scrolling, each with a label column at most 45% of its frame; {len(bad)} faults')


LINE_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-linechart')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  const sr = s.getBoundingClientRect();
  const parts = [...s.querySelectorAll('text, circle.viz-pt, polyline, path')].map(t => t.getBoundingClientRect()).filter(r => r.width > 0 || r.height > 0);
  out.push({n: i + 1, frame: [fr.left, fr.right], svg: [sr.left, sr.right], open: sc.scrollLeft,
            alt: s.classList.contains('viz-alt'), parts: parts.map(r => [r.left, r.right])}); }
 return out; }"""
def check_phone_lines(br, fails):
    """P123 (15 Nov 2026): every line figure, on every page that has one, at 320 and 390 px: the drawing a phone shows
    (its svg.viz-alt) is no wider than the frame, opens unscrolled, and every text, point and line of it, the y-axis
    labels, the legend and each point label included, is whole inside the frame. Before P123 a line chart drew 700
    units on a phone and scrolled, so its y-axis and title left the frame and a label could sit at its edge."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if SCOPE.has(pid) and (SITE / src).exists() and re.search(r'viz-linechart\b', (SITE / src).read_text())]   # S-DEC4: the run's pages
    n, bad = 0, []
    for name, w, h in CMP_WIDTHS:
        errs = []
        ctx, pg, _ = new_page(None, br, errs, name, w, h, True)
        for pid in pids:
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
            for f in pg.evaluate(LINE_JS, pid):
                where = f'{pid} line figure {f["n"]} at {w} px'
                n += 1
                fl, fr = f['frame']
                if not f['alt']:
                    bad.append(f'{where}: shows its wide drawing, not its phone drawing')
                if f['open'] > 0.5:
                    bad.append(f'{where}: the frame opens scrolled')
                if f['svg'][1] - f['svg'][0] > fr - fl + 0.5:
                    bad.append(f'{where}: the phone drawing is wider than its frame and scrolls')
                out = [b for b in f['parts'] if b[0] < fl - 0.5 or b[1] > fr + 0.5]
                if out:
                    bad.append(f'{where}: {len(out)} part(s) of the drawing outside the frame ({fl:.0f} to {fr:.0f})')
        if errs: fails.append(f'line figures {name}: console errors: ' + ' | '.join(errs[:3]))
        ctx.close()
    fails += bad
    print(f'line figures on a phone (P123): {n} figure frames on {len(pids)} pages at 320 and 390 px, every part whole in the opening frame, no sideways scroll; {len(bad)} faults')

SCATTER_JS = """async (pid) => { const out = []; const p = document.getElementById(pid);
 for (const [i, f] of [...p.querySelectorAll('figure.viz-scatter')].entries()) {
  const sec = f.closest('.sec'); if (sec && !sec.classList.contains('on')) p.querySelector('.seclist a[data-step="' + sec.dataset.step + '"]').click();
  for (const d of p.querySelectorAll('details')) if (d.contains(f)) d.open = true;
  f.scrollIntoView({block: 'center'}); await new Promise(r => setTimeout(r, 120));
  const sc = f.querySelector('.viz-scroll'), fr = sc.getBoundingClientRect();
  const s = [...sc.querySelectorAll(':scope > svg')].find(x => getComputedStyle(x).display !== 'none');
  const sr = s.getBoundingClientRect();
  const parts = [...s.querySelectorAll('text, circle, rect, line, polyline, path')].map(t => t.getBoundingClientRect()).filter(r => r.width > 0 || r.height > 0);
  out.push({n: i + 1, frame: [fr.left, fr.right], svg: [sr.left, sr.right], open: sc.scrollLeft,
            alt: s.classList.contains('viz-alt'), parts: parts.map(r => [r.left, r.right])}); }
 return out; }"""
def check_phone_scatters(br, fails):
    """P124 (15 Nov 2026): every scatter figure, on every page that has one, at 320 and 390 px: the drawing a phone shows
    (its svg.viz-alt) is no wider than the frame, opens unscrolled, and every text, point and line of it, the y-axis
    labels, the legend and each point label included, is whole inside the frame. Before P124 a scatter drew its natural width
    on a phone and scrolled, so its y-axis and title left the frame and a label could sit at its edge."""
    idx = (SITE / 'index.html').read_text()
    pids = [pid for pid, src in re.findall(r'<section class="panel" id="([^"]+)"[^>]*data-src="([^"]+)"', idx)
            if SCOPE.has(pid) and (SITE / src).exists() and re.search(r'viz-scatter\b', (SITE / src).read_text())]   # S-DEC4: the run's pages
    n, bad = 0, []
    for name, w, h in CMP_WIDTHS:
        errs = []
        ctx, pg, _ = new_page(None, br, errs, name, w, h, True)
        for pid in pids:
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
            for f in pg.evaluate(SCATTER_JS, pid):
                where = f'{pid} scatter figure {f["n"]} at {w} px'
                n += 1
                fl, fr = f['frame']
                if not f['alt']:
                    bad.append(f'{where}: shows its wide drawing, not its phone drawing')
                if f['open'] > 0.5:
                    bad.append(f'{where}: the frame opens scrolled')
                if f['svg'][1] - f['svg'][0] > fr - fl + 0.5:
                    bad.append(f'{where}: the phone drawing is wider than its frame and scrolls')
                out = [b for b in f['parts'] if b[0] < fl - 0.5 or b[1] > fr + 0.5]
                if out:
                    bad.append(f'{where}: {len(out)} part(s) of the drawing outside the frame ({fl:.0f} to {fr:.0f})')
        if errs: fails.append(f'scatter figures {name}: console errors: ' + ' | '.join(errs[:3]))
        ctx.close()
    fails += bad
    print(f'scatter figures on a phone (P124): {n} figure frames on {len(pids)} pages at 320 and 390 px, every part whole in the opening frame, no sideways scroll; {len(bad)} faults')

def check_figures(br, fails):
    """The examples page (V1) through the shell: VX_FIGS figures, one per kind, and the geometry of each (FIG_JS)."""
    if 'figures' in OMIT:
        print(f'figures: edition {EDITION} leaves out the examples page; the figure blocks are still checked (figure keys)'); return
    if not SCOPE.has('viz-examples'):   # S-DEC4: its sources are the kit's (viz.py, viz_examples.py), whose change forces the full run
        print('figures: the examples page is unchanged since the last passed run; left out of this scoped run'); return
    errs = []
    ctx, pg, _ = new_page(None, br, errs, 'figures', 390, 844, True)
    pg.evaluate("location.hash = 'viz-examples'"); ready(pg); pg.wait_for_timeout(200)
    res = pg.evaluate(FIG_JS, '#viz-examples')
    if res['n'] != VX_FIGS: fails.append(f'viz-examples: {res["n"]} figures in the panel, expected {VX_FIGS}')
    if len(set(res['kinds'][:VX_KINDS])) != VX_KINDS: fails.append(f'viz-examples: a kind appears twice among the kinds: {res["kinds"][:VX_KINDS]}')
    # P55: every block the renderer cannot draw honestly stops the build, with a message that says what to change
    for what, block, want in viz_examples.RAISES:
        try:
            viz.render(json.loads(json.dumps(block))); fails.append(f'viz-examples: {what!r} drew; it must stop the build')
        except SystemExit as e:
            if want not in str(e): fails.append(f'viz-examples: {what!r} stopped with {e!s}, which does not say {want!r}')
    fails += ['viz-examples: ' + b for b in res['bad'][:12]]
    if errs: fails.append('viz-examples: console errors: ' + ' | '.join(errs[:3]))
    print(f'figures: {VX_KINDS} kinds and {res["n"] - VX_KINDS} hard cases on the examples page ({", ".join(res["kinds"])}); {len(res["bad"])} geometry faults; '
          f'{len(viz_examples.RAISES)} blocks stop the build as they should')
    ctx.close()

# S-PAGES (15 Nov 2026) · the Backlog and Changelog pages: a plain overview by area, rendered from docs/site-log.md alone
SL_AREAS = [a[0] for a in LOG_AREAS] + [brand(EDITION)['log_area'][0]]   # S-DEC4: catalog.toml `log_areas` (courses.LOG_AREAS), as build.py reads them   # S-DEC3: the site's own area from the brand   # S-SP0: course SP; S-SPORTS (19 Nov 2026): Coaching renamed Sports; S-SCE0: course SCE
SL_WIDTHS = [('phone320', 320, 640, True), ('phone', 390, 844, True), ('desktop', 1280, 800, False)]
# the engine's words, which the two pages leave out (a unit's own title, such as "Agents" or "Prompting", is content)
SL_PLAIN = re.compile(r'\b(Opus|Fable|Sonnet|Haiku|subagents?|(?:fresh|isolated|writer|checker|filer|applier|correction) agents?|'
                      r'agent contexts?|audit\w*|tokens?|chats?|backlog rows?|mirrors?|Corrections section|next prompt)\b'
                      r'|\b[\w/-]+\.(?:py|md|json|css|js|sh|txt)\b', re.I)
SL_JS = """(pid) => { const p = document.getElementById(pid), w = el => el.getBoundingClientRect().width;
  const areas = [...p.querySelectorAll('section.slarea')];
  return {sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth,
    order: [...p.querySelectorAll('[data-sl="order"] table.sl tbody tr')].map(r => [...r.cells].map(c => c.textContent.trim())),
    areas: areas.map(a => ({name: a.dataset.area, rows: [...a.querySelectorAll('table.sl tbody tr')].map(r => [...r.cells].map(c => c.textContent.trim())),
                             dates: [...a.querySelectorAll('td.c-date .sld')].map(d => d.textContent.trim())})),
    over: [...p.querySelectorAll('.sltbl, td')].filter(e => e.scrollWidth > e.clientWidth + 1).length,
    code: Math.max(0, ...[...p.querySelectorAll('td.c-code')].map(w)),
    text: Math.min(9999, ...[...p.querySelectorAll('td.c-text')].map(w)),
    nowrap: [...p.querySelectorAll('td.c-text')].filter(t => getComputedStyle(t).whiteSpace === 'nowrap').length}; }"""
def site_log_rows():
    """docs/site-log.md's two tables, as build.py reads them: Next [(n, code, area, text)], Done [(iso, code, area, text)]."""
    nxt, done, sec = [], [], None
    for ln in (R.parent / 'docs' / 'site-log.md').read_text(encoding='utf-8').split('\n'):
        if ln.startswith('## '):
            sec = ln[3:].strip(); continue
        if sec in ('Next', 'Done') and ln.startswith('|') and not ln.startswith('|---'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            if c[0] not in ('#', 'Date'):
                (nxt if sec == 'Next' else done).append(tuple(c))
    return nxt, done

def check_site_log(br, fails):
    """S-PAGES (15 Nov 2026): the Backlog page holds the overall order (#, code, area, sentence: one row per entry of the
    site log's Next, in its order) and one section per area (code, sentence); the Changelog page one section per area
    (date, code, sentence), newest first, every Done entry once. Both in plain words: no model name, no engine word
    (SL_PLAIN), no file name and no private term (kit/private-terms.txt). At 320, 390 and 1280 px, dark and light: no
    sideways scroll of the page, a table or a cell; the sentence wraps; on a phone the code column at most 72 px and the
    sentence column at least 110 px."""
    if 'backlog' in OMIT and 'changelog' in OMIT:
        print(f'site log: edition {EDITION} leaves out the Backlog and Changelog pages'); return
    nxt, done = site_log_rows()
    bad = []
    # the words, on disk: the backlog panel in the shell and the changelog page beside it
    shell = (SITE / 'index.html').read_text()
    texts = {}
    if 'backlog' not in OMIT:
        m = re.search(r'<section class="panel log slog" id="backlog".*?</section>\s*(?=<section class="panel|$)', shell, re.S)
        texts['backlog'] = m.group(0) if m else ''
        if not m: bad.append('site log: the Backlog panel (.panel.log.slog#backlog) is not in the shell')
    if 'changelog' not in OMIT:
        texts['changelog'] = (SITE / 'changelog.html').read_text() if (SITE / 'changelog.html').exists() else ''
    ft, _ = private_terms.terms()
    PT = private_terms.rx(ft)
    for pid, t in texts.items():
        plain = H.unescape(re.sub(r'<[^>]+>', ' ', t))
        for m in SL_PLAIN.finditer(plain): bad.append(f'site log: the {pid} page says "{m.group(0)}" (not plain)')
        for m in PT.finditer(plain): bad.append(f'site log: the {pid} page carries the private term "{m.group(0)}"')
    seen = 0
    for name, w, h, mobile in SL_WIDTHS:
        for theme in ('dark', 'light'):
            errs = []
            ctx, pg, _ = new_page(None, br, errs, name, w, h, mobile)
            if theme == 'light':
                pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
            where = f'{w} px {theme}'
            for pid in [x for x in ('backlog', 'changelog') if x not in OMIT]:
                pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(80)
                r = pg.evaluate(SL_JS, pid)
                seen += 1
                if [a['name'] for a in r['areas']] != SL_AREAS: bad.append(f'site log {pid} at {where}: areas {[a["name"] for a in r["areas"]]}, expected {SL_AREAS}')
                if r['sw'] > r['cw']: bad.append(f'site log {pid} at {where}: the page scrolls sideways ({r["sw"]} > {r["cw"]})')
                if r['over']: bad.append(f'site log {pid} at {where}: {r["over"]} table(s) or cell(s) overflow')
                if r['nowrap']: bad.append(f'site log {pid} at {where}: {r["nowrap"]} sentence cell(s) do not wrap')
                if mobile and r['code'] > 72: bad.append(f'site log {pid} at {where}: the code column is {r["code"]:.0f} px wide (at most 72)')
                if mobile and r['text'] < 110: bad.append(f'site log {pid} at {where}: a sentence column is {r["text"]:.0f} px wide (at least 110)')
                if pid == 'backlog':
                    want = [[n, c, a, t] for n, c, a, t in nxt]
                    if r['order'] != want: bad.append(f'site log backlog at {where}: the order table has {len(r["order"])} rows, not the site log\'s {len(want)} in order')
                    for a in r['areas']:
                        wa = [[c, t] for n, c, ar, t in nxt if ar == a['name']]
                        if a['rows'] != wa: bad.append(f'site log backlog at {where}: {a["name"]} has {len(a["rows"])} rows, the site log {len(wa)}')
                else:
                    got = sorted(tuple(x[1:]) + (a['name'],) for a in r['areas'] for x in a['rows'])
                    want = sorted((c, t, a) for d, c, a, t in done)
                    if got != want: bad.append(f'site log changelog at {where}: {len(got)} entries shown, the site log has {len(want)}')
                    for a in r['areas']:
                        iso = [d for d, c, ar, t in done if ar == a['name']]
                        if a['dates'] != [short(d) for d in sorted(iso, reverse=True)]: bad.append(f'site log changelog at {where}: {a["name"]} is not newest first')
            if errs: bad.append(f'site log {where}: console errors: ' + ' | '.join(errs[:3]))
            ctx.close()
    fails += bad
    print(f'site log (S-PAGES): {len(nxt)} next and {len(done)} done in docs/site-log.md; Backlog and Changelog checked {seen} times at '
          f'{", ".join(str(x[1]) for x in SL_WIDTHS)} px, dark and light (plain words, private terms, order, areas, no sideways scroll); {len(bad)} faults')

# S-NEXT1 (23 Nov 2026) · the Coming next page (#coming, in the shell beside the Backlog): every course not yet complete,
# from the sources as build.py reads them. In progress: a registered course with some units written ("n of N", a history
# course's units complete of its card units, a markdown sub-course's units filed of its units); Ready to write: one with
# none (its build status 'coming soon'; a history course with no report), "0 of N" and "syllabus and prompts filed";
# Planned: every row of every track's `planned` ('planned' not in OMIT), "theme chosen". Each in course_order (planned:
# tracks in catalog order, then each track's own), exactly once, in its section and with its count, its track's name in
# the track's colour, its link (a course's home; a planned row its track's planned list); no complete course is a row;
# an empty section is left out; the closing line counts the complete courses and links to the home. At 390 px, dark and
# light: no sideways scroll of the page, a table or a cell, and nothing past the right edge.
def coming_expect():
    """(registered [(state, name, track, home id, done, total)] in course order, planned [(name, track, anchor)])."""
    from howbuilt import front
    reg = []
    for c in COURSES:
        if c['family'] == 'history':
            syl = cpath(c, 'syllabus').read_text()
            idx = json.load(open(cpath(c, 'prompts')))
            units = [(u, re.findall(r'data-id="([\d.]+)">', body)) for u, body in re.findall(r'<section class="unit" id="u(\d+)"[^>]*>(.*?)</section>', syl, re.S)]
            done = sum(1 for u, ms in units if u != c['audit_unit'] and all(m in idx for m in ms))
            started = any(m in idx for _, ms in units for m in ms)
            # 'complete' reads the course.toml's typed status, the same value the build reads, so it is not checked independently
            reg.append(('complete' if c['status'] == 'available' else 'progress' if started else 'ready', c['name'], c['theme'], c['home_id'], done, c['card_units']))
        else:
            d = pack.load(c)
            v = R.parent / c['vault']
            codes = {front(f).get('code') for f in (sorted(v.glob('*.md')) if v.is_dir() else [])}
            for sc in d.COURSES:
                tr, _ = c['tracks'][sc['key']]
                n, N = sum(1 for u in sc['units'] if u[0] in codes), len(sc['units'])
                reg.append(('complete' if n == N else 'progress' if n else 'ready', sc['name'], tr, f"{c.get('prefix', c['id'])}-{sc['key'].lower()}", n, N))
    plan = [] if 'planned' in OMIT else [(row[1], t['id'], t.get('planned_anchor', 'planned-' + t['id'])) for t in THEMES for row in t.get('planned', [])]
    return reg, plan

# with no course to list (every registered course complete, no planned row) the build leaves the page and its site link
# out, as an edition's omit would; the checks that read OMIT then expect neither
COMING_EMPTY = 'coming' not in OMIT and (lambda r, p: not p and all(x[0] == 'complete' for x in r))(*coming_expect())
if COMING_EMPTY: OMIT.add('coming')

COMING_JS = r"""() => { const p = document.getElementById('coming'), vw = document.documentElement.clientWidth;
  const txt = (r, s) => { const e = r.querySelector(s); return e ? e.textContent.trim() : null; };
  return {sw: document.documentElement.scrollWidth, cw: vw,
    over: [...p.querySelectorAll('.sltbl, table, td, th')].filter(e => e.scrollWidth > e.clientWidth + 1).length,
    past: [...p.querySelectorAll('*')].filter(e => { const b = e.getBoundingClientRect(); return b.width && b.right > vw + 0.5; }).length,
    secs: [...p.querySelectorAll(':scope > section[data-coming]')].map(s => ({key: s.dataset.coming, head: txt(s, 'h2'),
      rows: [...s.querySelectorAll('table.sl tbody tr')].map(r => ({target: (r.querySelector('a[data-target]') || {dataset: {}}).dataset.target,
        name: txt(r, 'a[data-target] strong'), area: txt(r, '.sla'), tone: (r.querySelector('.sla') || {style: {}}).style.getPropertyValue('--c').trim(),
        count: txt(r, '.slc'), note: txt(r, '.sld')}))})),
    done: txt(p, ':scope > [data-coming="done"]'), home: !!p.querySelector(':scope > [data-coming="done"] a[data-target="home"][href="#home"]')}; }"""

def check_coming(br, fails):
    if COMING_EMPTY:
        sh = (SITE / 'index.html').read_text()
        if re.search(r'id="coming"', sh) or re.search(r'href="#coming"', sh):
            fails.append(f'coming next: edition {EDITION} has no course to list, yet the Coming next page or its link is built')
        else: print(f'coming next: edition {EDITION} has no course to list; the page and its link are left out')
        return
    if 'coming' in OMIT:
        print(f'coming next: edition {EDITION} leaves out the Coming next page'); return
    reg, plan = coming_expect()
    TH = {t['id']: t for t in THEMES}
    want = {'progress': [], 'ready': [], 'planned': []}
    for st, name, tr, home, n, N in reg:
        if st == 'complete': continue
        want[st].append(dict(target=home, name=name, area=TH[tr]['name'], tone=TH[tr]['color'], count=f'{n} of {N}',
                             note='syllabus and prompts filed' if st == 'ready' else None))
    for name, tr, anchor in plan:
        want['planned'].append(dict(target=anchor, name=name, area=TH[tr]['name'], tone=TH[tr]['color'], count=None, note='theme chosen'))
    heads = {'progress': 'In progress', 'ready': 'Ready to write', 'planned': 'Planned'}
    complete = [r for r in reg if r[0] == 'complete']
    bad = []
    if not re.search(r'<section class="panel log slog" id="coming"', (SITE / 'index.html').read_text()):
        bad.append('coming next: the Coming next panel (.panel.log.slog#coming) is not in the shell')
    for theme in ('dark', 'light'):
        errs = []
        ctx, pg, _ = new_page(None, br, errs, 'phone', 390, 844, True)
        if theme == 'light':
            pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
        pg.evaluate("location.hash = 'coming'"); ready(pg); pg.wait_for_timeout(80)
        r = pg.evaluate(COMING_JS)
        where = f'390 px {theme}'
        if r['sw'] > r['cw']: bad.append(f'coming next at {where}: the page scrolls sideways ({r["sw"]} > {r["cw"]})')
        if r['over']: bad.append(f'coming next at {where}: {r["over"]} table(s) or cell(s) overflow')
        if r['past']: bad.append(f'coming next at {where}: {r["past"]} element(s) stand past the right edge')
        wk = [k for k in ('progress', 'ready', 'planned') if want[k]]
        if [s['key'] for s in r['secs']] != wk: bad.append(f'coming next at {where}: sections {[s["key"] for s in r["secs"]]}, expected {wk} (an empty one left out)')
        got_all = [(x['target'], x['name']) for s in r['secs'] for x in s['rows']]
        for k in wk:
            s = next((s for s in r['secs'] if s['key'] == k), None)
            if not s: continue
            if s['head'] != heads[k]: bad.append(f'coming next at {where}: section {k} is headed {s["head"]!r}, not {heads[k]!r}')
            if s['rows'] != want[k]:
                miss = [x['name'] for x in want[k] if x not in s['rows']]
                extra = [x['name'] for x in s['rows'] if x not in want[k]]
                bad.append(f'coming next at {where}: {heads[k]} lists {len(s["rows"])} rows, expected {len(want[k])} in order'
                           + (f'; missing or different {miss}' if miss else '') + (f'; not expected {extra}' if extra else ''))
        for x in [x for k in want for x in want[k]]:
            n = got_all.count((x['target'], x['name']))
            if n != 1: bad.append(f'coming next at {where}: {x["name"]} appears {n} times, expected once')
        for st, name, tr, home, n, N in complete:
            if any(t == home for t, _ in got_all): bad.append(f'coming next at {where}: the complete course {name} is listed as a row')
        k = len(complete)
        if not (r['done'] or '').startswith(f'{k} course{"s are" if k != 1 else " is"} complete') or not r['home']:
            bad.append(f'coming next at {where}: the closing line reads {r["done"]!r} (home link {r["home"]}), expected {k} complete and a link to the home')
        if errs: bad.append(f'coming next {where}: console errors: ' + ' | '.join(errs[:3]))
        ctx.close()
    fails += bad
    print(f'coming next (S-NEXT1): {len(want["progress"])} in progress, {len(want["ready"])} ready to write, {len(want["planned"])} planned, '
          f'{len(complete)} complete; checked at 390 px, dark and light (sections, order, counts, links, tones, no sideways scroll); {len(bad)} faults')

# S-NAV1 (21 Nov 2026), step A: history. Every move is a real history entry (shell.js go() pushes '#'+id), so a back swipe
# walks the site instead of leaving it; popstate restores the panel and the scroll its entry kept; the first load pushes
# nothing. At 390 px: a fresh load holds as many entries as a plain page (no push); home -> area (step B: an edition of
# two or more tracks) -> course -> unit by the links a reader taps (each at a scroll part
# way down, read back before the tap), then history.back() once per level lands on each in turn with its scroll restored
# (2 px), and history.forward() lands on the unit with its own. Then the artifact case: with pushState refused (it throws,
# as a sandboxed frame may) go() falls back to replaceState, the behaviour before S-NAV1: the pages still change and no
# entry is added; and inside a same-origin sandboxed iframe the walk and one back work as at the top level.
HIST_PATH_JS = r'''() => {   // the links a reader taps, level by level: [selector of the link, the panel it opens]
  const kind = id => { const p = document.getElementById(id); return p && p.getAttribute('data-kind'); };
  const first = (from, k) => [...document.querySelectorAll('#' + from + ' a.course[data-target]')].map(a => a.dataset.target).find(t => kind(t) === k);
  // S-NAV1 step B: with area pages, the home's first area tile, then that area page's first course tile
  const area = first('home', 'area');
  if (area) { const course = first(area, 'course');
    return course ? [['#home a.course[data-target="' + area + '"]', area], ['#' + area + ' a.course[data-target="' + course + '"]', course]] : []; }
  const course = first('home', 'course');
  return course ? [['#home a.course[data-target="' + course + '"]', course]] : []; }'''
HIST_UNIT_JS = r'''(cid) => { const p = document.getElementById(cid); p.querySelectorAll('details').forEach(d => d.open = true);
  const a = [...p.querySelectorAll('a[data-target]')].find(a => { const t = document.getElementById(a.dataset.target); return t && t.getAttribute('data-kind') === 'report'; });
  return a ? a.dataset.target : null; }'''
HIST_AT_JS = '''() => ({id: [...document.querySelectorAll('.panel')].find(p => !p.hidden).id, y: Math.round(scrollY),
  max: Math.round(document.documentElement.scrollHeight - innerHeight), n: history.length, hash: location.hash})'''
def _hist_ready(fr):
    fr.wait_for_function(READY_JS, timeout=15000); fr.wait_for_timeout(350)   # the fetch landed and the restore ran

def _hist_walk(fr, label, fails, scroll=True):
    """home -> (area, Step B) -> course -> unit, tapping each link in the page; returns [(panel, y)] per level, home first."""
    _hist_ready(fr)
    at = fr.evaluate(HIST_AT_JS)
    if at['id'] != 'home': fails.append(f'history {label}: the fresh load shows {at["id"]}, not the home'); return None
    links = fr.evaluate(HIST_PATH_JS)
    # S-NAV1 step B: with area pages HIST_PATH_JS returns two levels, [[the home's link to the area, area id], [the area's
    # link to the course, course id]], so the walk reads home -> area -> course -> unit and the backs cover three levels;
    # an edition of one track keeps the one level, home -> course -> unit
    if MULTI and len(links) != 2: fails.append(f'history {label}: the walk found {links}, expected the home\'s area tile, then the area\'s course tile'); return None
    if not links: fails.append(f'history {label}: no course tile on the home'); return None
    levels = []
    def leave(sel, want):
        at = fr.evaluate(HIST_AT_JS)
        if scroll:   # 40% of the page's height; a page with less than 250 px to scroll (S-NAV1 step B: an area page of one course, marketing-ai's) to its foot
            fr.evaluate(f'window.scrollTo(0, {int(at["max"] * .4) if at["max"] * .4 >= 100 else at["max"]})'); fr.wait_for_timeout(350)   # past the save's 200 ms debounce
            at = fr.evaluate(HIST_AT_JS)
            if at['y'] < 30: fails.append(f'history {label}: {at["id"]} scrolls only {at["max"]} px, too short to test its restore')
        levels.append((at['id'], at['y']))
        fr.evaluate('(s) => document.querySelector(s).click()', sel)   # a tap, without Playwright scrolling the link into view
        _hist_ready(fr)
        now = fr.evaluate(HIST_AT_JS)
        if now['id'] != want: fails.append(f'history {label}: {sel} opened {now["id"]}, expected {want}'); return False
        if now['y'] != 0: fails.append(f'history {label}: {want} opened at y={now["y"]}, expected the top')
        return True
    for sel, want in links:
        if not leave(sel, want): return None
    cid = links[-1][1]
    unit = fr.evaluate(HIST_UNIT_JS, cid)
    if not unit: fails.append(f'history {label}: no unit link on {cid}'); return None
    if not leave(f'#{cid} a[data-target="{unit}"]', unit): return None
    at = fr.evaluate(HIST_AT_JS)
    if scroll:
        fr.evaluate(f'window.scrollTo(0, {int(at["max"] * .4)})'); fr.wait_for_timeout(350); at = fr.evaluate(HIST_AT_JS)
    levels.append((at['id'], at['y']))
    return levels

def _hist_ctx(br, **kw):
    ctx = br.new_context(color_scheme='dark', reduced_motion='reduce', **kw)
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
    ctx.route('**/fonts.gstatic.com/**', font_file)
    return ctx

def check_history(br, fails):
    lines = []
    # 1 · the walk and the backs, at the top level
    ctx = _hist_ctx(br, viewport={'width': 390, 'height': 844}, device_scale_factor=3, is_mobile=True, has_touch=True)
    blank = URL.replace('index.html', '__blank_test.html')   # a page with no script: the entries a plain first load holds
    ctx.route(blank, lambda r: r.fulfill(status=200, content_type='text/html', body='<!DOCTYPE html><title>x</title>'))
    pb = ctx.new_page(); pb.goto(blank); base = pb.evaluate('history.length'); pb.close()   # Playwright's about:blank counts
    pg = ctx.new_page(); pg.goto(URL + '#home')
    _hist_ready(pg)
    n0 = pg.evaluate('history.length')
    if n0 != base: fails.append(f'history: the first load holds {n0} entries, a plain page {base} (it must replace, never push)')
    lv = _hist_walk(pg, 'top', fails)
    if lv:
        n = pg.evaluate('history.length')
        if n != n0 + len(lv) - 1: fails.append(f'history: {len(lv)} pages walked left {n} entries, expected {n0 + len(lv) - 1}')
        for want, y in reversed(lv[:-1]):
            pg.evaluate('history.back()'); _hist_ready(pg)
            at = pg.evaluate(HIST_AT_JS)
            ok = at['id'] == want and abs(at['y'] - y) <= 2
            if not ok: fails.append(f'history back: {at["id"]} at y={at["y"]}, expected {want} at y={y}')
            lines.append(f'back -> {at["id"]} y={at["y"]} (kept {y})' + ('' if ok else ' FAIL'))
        for _ in lv[1:-1]: pg.evaluate('history.forward()'); _hist_ready(pg)
        pg.evaluate('history.forward()'); _hist_ready(pg)
        at, (want, y) = pg.evaluate(HIST_AT_JS), lv[-1]
        ok = at['id'] == want and abs(at['y'] - y) <= 2
        if not ok: fails.append(f'history forward: {at["id"]} at y={at["y"]}, expected {want} at y={y}')
        lines.append(f'forward to the end -> {at["id"]} y={at["y"]} (kept {y})' + ('' if ok else ' FAIL'))
        print('history: ' + ' -> '.join(f'{i} (y={y})' for i, y in lv) + '; ' + '; '.join(lines))
    ctx.close()
    # 2 · pushState refused: the fallback is replaceState, the pages still change, no entry is added
    ctx = _hist_ctx(br, viewport={'width': 390, 'height': 844}, is_mobile=True, has_touch=True)
    ctx.add_init_script("history.pushState = function(){ throw new DOMException('refused', 'SecurityError'); };")
    pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL + '#home'); _hist_ready(pg); n0 = pg.evaluate('history.length')
    lv = _hist_walk(pg, 'pushState refused', fails, scroll=False)
    if lv:
        at = pg.evaluate(HIST_AT_JS)
        if at['n'] != n0 or at['hash'] != '#' + lv[-1][0]: fails.append(f'history pushState refused: {at["n"]} entries, address {at["hash"]}; expected {n0} (as loaded) and #{lv[-1][0]}')
        else: print(f'history, pushState refused: replaceState fallback, {" -> ".join(i for i, _ in lv)} shown, no entry added ({n0}), address {at["hash"]}')
    if errs: fails.append('history pushState refused: page errors ' + ' | '.join(errs[:3]))
    ctx.close()
    # 3 · inside a sandboxed iframe (allow-scripts allow-same-origin), as an artifact viewer may hold the page
    ctx = _hist_ctx(br, viewport={'width': 420, 'height': 900})
    host = URL.replace('index.html', '__frame_test.html')
    ctx.route(host, lambda r: r.fulfill(status=200, content_type='text/html',
              body='<!DOCTYPE html><iframe sandbox="allow-scripts allow-same-origin" src="index.html#home" style="width:390px;height:844px;border:0"></iframe>'))
    pg = ctx.new_page(); pg.goto(host); pg.wait_for_timeout(300)
    fr = pg.frames[1]
    lv = _hist_walk(fr, 'iframe', fails)
    if lv:
        fr.evaluate('history.back()'); _hist_ready(fr)
        at, (want, y) = fr.evaluate(HIST_AT_JS), lv[-2]
        if at['id'] != want or abs(at['y'] - y) > 2: fails.append(f'history iframe back: {at["id"]} at y={at["y"]}, expected {want} at y={y}')
        else: print(f'history, sandboxed iframe: {" -> ".join(i for i, _ in lv)}, back -> {at["id"]} y={at["y"]} (kept {y})')
    ctx.close()

# S-NAV2 step B (22 Nov 2026), Fix 2 (P-NAV7): the history readout behind ?debug (kit/shell.js, theme section 10).
# Without ?debug (the address every reader and every other check uses): no element of the readout (.dbg or any dbg-
# class), the body's children exactly the built shell's, no pagehide or pageshow listener on the window (the readout's
# only listeners), the window's and the document's listeners the same types as at the start, no readout key in
# localStorage after the walk. With ?debug at 390 px: the panel is shown, fixed inside the screen, no sideways scroll, its
# three buttons 44 px tall; the walk home -> area -> course -> unit (check_history's links) gives the same panels, scrolls
# and history lengths as without it, and the log holds the load (top level), one "go <id>: pushState" line a level with
# the length rising by one each, then history.back() logs a popstate landing on the course; the summary says pushState
# never threw; Hide folds it, a reload keeps the earlier load's lines, Clear empties the log and its key. With pushState
# refused the log names the fallback on every level ("pushState threw SecurityError, replaceState fallback") and the
# summary counts the throws; inside a same-origin sandboxed iframe it says "in a frame"; at 1280 x 800 the panel sits
# inside the screen. No page error in any pass.
DBG_JS = r"""() => { const b = document.querySelector('.dbg'), r = b && b.getBoundingClientRect();
  return {n: document.querySelectorAll('.dbg, [class*="dbg"]').length, shown: !!b && getComputedStyle(b).display !== 'none',
    pos: b ? getComputedStyle(b).position : null, box: r ? [r.left, r.top, r.right, r.bottom].map(Math.round) : null,
    vw: innerWidth, vh: innerHeight, sw: document.documentElement.scrollWidth,
    btns: b ? [...b.querySelectorAll('button.dbg-b')].map(x => [x.textContent, Math.round(x.getBoundingClientRect().height)]) : [],
    sum: b ? b.querySelector('.dbg-sum').textContent : '', log: b ? b.querySelector('.dbg-log').textContent : '',
    logShown: !!b && getComputedStyle(b.querySelector('.dbg-log')).display !== 'none',
    keys: Object.keys(localStorage).filter(k => /\.debug$/.test(k))}; }"""
DBG_BODY_JS = r"""async () => { const sig = els => [...els].map(e => e.tagName + '#' + e.id + '.' + e.className).join(' | ');
  const t = await (await fetch(location.pathname)).text(), d = new DOMParser().parseFromString(t, 'text/html');
  return [sig(d.body.children), sig(document.body.children)]; }"""
def _listeners(pg):
    """The event types listened for on the window and the document (CDP DOMDebugger.getEventListeners)."""
    cdp = pg.context.new_cdp_session(pg); out = {}
    for name in ('window', 'document'):
        oid = cdp.send('Runtime.evaluate', {'expression': name})['result']['objectId']
        out[name] = sorted(l['type'] for l in cdp.send('DOMDebugger.getEventListeners', {'objectId': oid})['listeners'])
    cdp.detach(); return out

def check_debug(br, fails):
    bad = []
    def ctx_page(**kw):
        ctx = _hist_ctx(br, viewport=kw.pop('viewport', {'width': 390, 'height': 844}), **kw)
        pg = ctx.new_page(); errs = []; pg.on('pageerror', lambda e: errs.append(str(e))); return ctx, pg, errs
    # 1 · without ?debug: nothing of the readout exists
    ctx, pg, errs = ctx_page(is_mobile=True, has_touch=True)
    pg.goto(URL + '#home'); _hist_ready(pg)
    l0 = _listeners(pg); body = pg.evaluate(DBG_BODY_JS); st = pg.evaluate(DBG_JS)
    if st['n']: bad.append(f'debug off: {st["n"]} readout elements without ?debug')
    if body[0] != body[1]: bad.append(f'debug off: the body\'s children {body[1]} are not the built shell\'s {body[0]}')
    if any(t in ('pagehide', 'pageshow') for t in l0['window']): bad.append(f'debug off: the window listens for {l0["window"]}')
    base = _hist_walk(pg, 'debug off', bad)
    l1 = _listeners(pg); st = pg.evaluate(DBG_JS); n_off = pg.evaluate('history.length')
    if l1 != l0: bad.append(f'debug off: the listeners changed during the walk: {l0} -> {l1}')
    if st['n'] or st['keys']: bad.append(f'debug off: after the walk {st["n"]} readout elements, storage keys {st["keys"]}')
    if errs: bad.append('debug off: page errors ' + ' | '.join(errs[:3]))
    ctx.close()
    # 2 · with ?debug: the panel, the walk and a back
    ctx, pg, errs = ctx_page(is_mobile=True, has_touch=True)
    pg.goto(URL + '?debug#home'); _hist_ready(pg)
    st = pg.evaluate(DBG_JS); n0 = pg.evaluate('history.length'); l2 = _listeners(pg)
    if not st['shown'] or st['pos'] != 'fixed': bad.append(f'debug on: the panel shown {st["shown"]}, position {st["pos"]}')
    elif st['box'][0] < 0 or st['box'][2] > st['vw'] or st['box'][1] < 0 or st['box'][3] > st['vh']: bad.append(f'debug on: the panel {st["box"]} leaves the {st["vw"]} x {st["vh"]} screen')
    if st['sw'] > st['vw']: bad.append(f'debug on: the page scrolls sideways ({st["sw"]} > {st["vw"]})')
    if [t for t, _ in st['btns']] != ['Copy', 'Clear', 'Hide'] or any(h < 44 for _, h in st['btns']): bad.append(f'debug on: buttons {st["btns"]}')
    extra = sorted(set(l2['window']) - set(l0['window']))
    if extra != ['pagehide', 'pageshow']: bad.append(f'debug on: the readout adds window listeners {extra}, expected pagehide and pageshow')
    if 'load: top level' not in st['log']: bad.append('debug on: the log does not say the page loaded at the top level')
    lv = _hist_walk(pg, 'debug on', bad)
    if lv and base:
        if lv != base: bad.append(f'debug on: the walk {lv} differs from the walk without ?debug {base}')
        if pg.evaluate('history.length') - n0 != n_off - n0: bad.append('debug on: the walk added a different number of history entries than without ?debug')
        log = pg.evaluate(DBG_JS)['log']
        gos = re.findall(r'go (\S+): pushState \(length was (\d+)\)\s+\[length (\d+)', log)
        want = [i for i, _ in lv[1:]]
        if [g[0] for g in gos] != want: bad.append(f'debug on: the log\'s go() lines {[g[0] for g in gos]}, expected {want}')
        elif any(int(b) != int(a) + 1 for _, a, b in gos): bad.append(f'debug on: a go() line\'s length did not rise by one: {gos}')
        pg.evaluate('history.back()'); _hist_ready(pg)
        st = pg.evaluate(DBG_JS)
        tail = st['log'].split('\n')[-3:]
        if not any(re.search(r'popstate, state \{"y":\d+\}.*hash #' + re.escape(lv[-2][0]) + r'\]', x) for x in tail): bad.append(f'debug on: no popstate to #{lv[-2][0]} after history.back(): {tail}')
        if 'pushState threw no' not in st['sum'] or f'history.length {n0 + len(lv) - 1}' not in st['sum']: bad.append(f'debug on: the summary reads {st["sum"]!r}')
        print(f'debug: without ?debug no readout, listeners {l0["window"].count("popstate")} popstate and {l0["window"].count("hashchange")} hashchange on the window, unchanged by the walk; '
              f'with it {" -> ".join(i for i, _ in lv)} the same walk, {len(gos)} pushState lines, back -> popstate #{lv[-2][0]}; summary: {st["sum"]}')
    pg.click('.dbg .dbg-b:text("Hide")'); st = pg.evaluate(DBG_JS)
    if st['logShown'] or [t for t, _ in st['btns']][2] != 'Show': bad.append('debug on: Hide does not fold the log')
    pg.reload(); _hist_ready(pg); st = pg.evaluate(DBG_JS)
    if '--- a new load ---' not in st['log'] or 'go ' not in st['log'].split('--- a new load ---')[0]: bad.append('debug on: a reload does not keep the earlier load\'s lines')
    pg.click('.dbg .dbg-b:text("Clear")'); st = pg.evaluate(DBG_JS)
    if 'go ' in st['log'] or not st['log'].strip().endswith(']') or 'cleared' not in st['log']: bad.append(f'debug on: Clear left {st["log"]!r}')
    if errs: bad.append('debug on: page errors ' + ' | '.join(errs[:3]))
    ctx.close()
    # 3 · with ?debug and pushState refused: the fallback named on every level
    ctx, pg, errs = ctx_page(is_mobile=True, has_touch=True)
    ctx.add_init_script("history.pushState = function(){ throw new DOMException('refused', 'SecurityError'); };")
    pg.goto(URL + '?debug#home'); _hist_ready(pg)
    lv = _hist_walk(pg, 'debug, pushState refused', bad, scroll=False)
    if lv:
        st = pg.evaluate(DBG_JS); k = len(lv) - 1
        got = len(re.findall(r': pushState threw SecurityError, replaceState fallback', st['log']))
        if got != k or f'pushState threw yes ({k})' not in st['sum']: bad.append(f'debug, pushState refused: {got} fallback lines, summary {st["sum"]!r}; expected {k}')
        else: print(f'debug, pushState refused: {got} fallback lines; summary: {st["sum"]}')
    if errs: bad.append('debug, pushState refused: page errors ' + ' | '.join(errs[:3]))
    ctx.close()
    # 4 · with ?debug inside a same-origin sandboxed iframe; 5 · at 1280 x 800
    ctx, pg, errs = ctx_page(viewport={'width': 420, 'height': 900})
    host = URL.replace('index.html', '__frame_test.html')
    ctx.route(host, lambda r: r.fulfill(status=200, content_type='text/html',
              body='<!DOCTYPE html><iframe sandbox="allow-scripts allow-same-origin" src="index.html?debug#home" style="width:390px;height:844px;border:0"></iframe>'))
    pg.goto(host); pg.wait_for_timeout(300); fr = pg.frames[1]; _hist_ready(fr)
    if 'load: in a frame' not in fr.evaluate(DBG_JS)['log']: bad.append('debug, iframe: the log does not say the page is in a frame')
    ctx.close()
    ctx, pg, errs = ctx_page(viewport={'width': 1280, 'height': 800})
    pg.goto(URL + '?debug#home'); _hist_ready(pg); st = pg.evaluate(DBG_JS)
    if not st['shown'] or st['box'][0] < 0 or st['box'][2] > st['vw'] or st['box'][3] > st['vh'] or st['sw'] > st['vw']: bad.append(f'debug, 1280 x 800: the panel {st["box"]}, page width {st["sw"]}')
    if errs: bad.append('debug, 1280: page errors ' + ' | '.join(errs[:3]))
    ctx.close()
    fails += bad
    print(f'debug readout (S-NAV2 Fix 2): off and on at 390 px, pushState refused, a sandboxed iframe, 1280 x 800; {len(bad)} faults')

# S-NAV1 step C (21 Nov 2026): two levels of navigation, each built once as one element in the drawer's list (build.py
# main_nav, sub_nav): nav.main-nav, Home and the areas in catalog order (an edition of one track: Home and its area,
# whose entry goes to the track's band on the home, #track-<id>), and nav.sub-nav, one group ([data-navctx]) per
# section, the reader's shown: an area page's courses, a course's pages and units, none on the home and the site pages
# under it. What's new, the Changelog and the Backlog are links at the home's foot, in neither nav.
NAV_JS = '''() => { const mains = [...document.querySelectorAll('nav.main-nav')], subs = [...document.querySelectorAll('nav.sub-nav')];
  const m = mains[0], s = subs[0], vis = s ? [...s.querySelectorAll('[data-navctx]')].filter(g => !g.hidden) : [];
  const site = ['#new', '#changelog', '#backlog', '#coming'];
  return {nMain: mains.length, nSub: subs.length, inPanels: document.querySelectorAll('.panel nav.main-nav, .panel nav.sub-nav').length,
    inDrawer: !!(m && s && m.parentElement === s.parentElement && m.closest('#drawer')),
    order: m && s ? !!(m.compareDocumentPosition(s) & Node.DOCUMENT_POSITION_FOLLOWING) : false,
    main: m ? [...m.querySelectorAll('a.ditem')].map(a => [a.dataset.target, a.querySelector('.t').textContent, a.classList.contains('is-active'), a.getAttribute('aria-current')]) : [],
    mainOther: m ? m.querySelectorAll(':scope > :not(a.ditem)').length : -1,
    subHidden: s ? s.hidden : null, groups: vis.map(g => g.dataset.navctx),
    subLinks: vis.length ? [...vis[0].querySelectorAll('a.ditem')].map(a => a.dataset.target) : [],
    subActive: vis.length ? [...vis[0].querySelectorAll('a.ditem.is-active')].map(a => a.dataset.target) : [],
    siteInNav: [...document.querySelectorAll('nav.main-nav a, nav.sub-nav a')].filter(a => site.includes(a.getAttribute('href'))).map(a => a.getAttribute('href'))}; }'''
# where each of the home's links to What's new, the Changelog and the Backlog sits: true when every one follows the
# home's courses (the area tiles, or the last track band in an edition of one track), null when there is none
NAV_FOOT_JS = '''() => { const h = document.getElementById('home'), g = h.querySelector(':scope > .cgrid.areas') || [...h.querySelectorAll(':scope > .track')].pop();
  const out = {}; for (const t of ['new', 'changelog', 'backlog']) { const as = [...h.querySelectorAll(':scope > .hlinks a[href="#' + t + '"]')];
    out[t] = as.length && g ? as.every(a => !!(g.compareDocumentPosition(a) & Node.DOCUMENT_POSITION_FOLLOWING)) : (as.length ? false : null); }
  return out; }'''
NAV_DRAWER_JS = '''() => { const d = document.getElementById('drawer'), m = d.querySelector('nav.main-nav'), s = d.querySelector('nav.sub-nav'), l = d.querySelector('.dlist');
  const box = e => { if (!e || e.hidden) return null; const r = e.getBoundingClientRect(); return [Math.round(r.left), Math.round(r.right), Math.round(r.top), Math.round(r.height)]; };
  const act = d.querySelector('.sub-nav:not([hidden]) [data-navctx]:not([hidden]) .ditem.is-active'), lr = l.getBoundingClientRect(), ar = act && act.getBoundingClientRect();
  return {on: d.classList.contains('on'), locked: document.documentElement.classList.contains('locked'), focus: document.activeElement && document.activeElement.id,
    hidden: d.getAttribute('aria-hidden'), expanded: document.getElementById('menuB').getAttribute('aria-expanded'), main: box(m), sub: box(s), vw: innerWidth,
    actIn: ar ? ar.top >= lr.top - 1 && ar.bottom <= lr.bottom + 1 : null}; }'''

def nav_expect():
    """What the navigation holds, from courses.py (the edition's courses and tracks, catalog order): the main nav's
    entries; each area's courses (its group of the sub-nav: history courses, then markdown sub-courses, as build.py
    lists them); each course section (its data-ctx) to its track and its home."""
    main = [['home', 'Home']] + [['track-' + t['id'], t['name']] for t in THEMES]
    area = {'track-' + t['id']: [c['home_id'] for c in HIST if c['theme'] == t['id']]
            + [f"{c.get('prefix', c['id'])}-{k.lower()}" for c in COURSES if c['family'] == 'markdown' for k, (tr, _) in c['tracks'].items() if tr == t['id']]
            for t in THEMES}
    sec = {c['id']: (c['theme'], c['home_id']) for c in HIST}
    sec |= {f"{c.get('prefix', c['id'])}-{k.lower()}": (tr, f"{c.get('prefix', c['id'])}-{k.lower()}") for c in COURSES if c['family'] == 'markdown' for k, (tr, _) in c['tracks'].items()}
    return main, area, sec

def check_nav(br, fails, w=390, h=844, theme='dark', motion=False, label=None):
    """S-NAV1 step C: nav.main-nav and nav.sub-nav once in the page, in the drawer's list, main before sub, in no panel;
    the main nav Home and the areas in catalog order, marking where the reader is (Home on the home and the site pages
    under it, the area on its page, aria-current page, and on every page of its courses, aria-current true); the sub-nav
    hidden on the home and the site pages, an area's courses on its page, a course's group (its home first, the page
    itself marked) on each of its pages; What's new, the Changelog and the Backlog at the home's foot and in neither nav.
    Then the drawer: below 1100 px the menu opens it with both navs on screen and the focus on its close button, the
    current item scrolled into its list, Escape closes it and gives the focus back; an area entry tapped in it closes it
    and opens the area (in an edition of one track, the home at the track's band), and a back returns; in an edition of
    one track, tapped on the home it adds no history entry (S-NAV1 step G). From 1100 px under 860 px tall the
    two navs stand in the sidebar without the menu (S-NAV2 step C, theme 6.22); on a desktop (1100 px and 860 px tall or
    more) the main nav stands in the top bar from the sidebar's edge and the sub-nav in the sidebar under the bar (S-NAV2
    step D). Run at 390 x 844 (dark and light), 1024 x 768, 1280 x 800 and 1920 x 1080. Every page error and console
    error fails."""
    label = label or f'{w}x{h} {theme}' + (' motion' if motion else '')
    main, area, sec = nav_expect()
    ctx = br.new_context(viewport={'width': w, 'height': h}, color_scheme=theme, reduced_motion='no-preference' if motion else 'reduce',
                         is_mobile=w < 1100, has_touch=w < 1100)
    ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
    ctx.route('**/fonts.gstatic.com/**', font_file)
    pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    pg.goto(URL + '#home'); ready(pg)
    roots = ['home', 'new'] + [x for x in ('changelog', 'backlog', 'coming') if x not in OMIT] + ([] if 'figures' in OMIT else ['viz-examples'])
    firsts = pg.evaluate("""() => { const o = {}; document.querySelectorAll('.panel[data-kind="report"]').forEach(p => { const c = p.getAttribute('data-ctx'); if (!o[c]) o[c] = p.id; }); return o; }""")
    pages = [(x, 'root') for x in roots] + [(a, 'area') for a in AREA_IDS]
    for cx, (tr, home) in sec.items():
        if not pg.evaluate(f"!!document.getElementById('{home}')"): continue
        pages += [(home, cx)] + [(c['syl_id'], cx) for c in HIST if c['id'] == cx and pg.evaluate(f"!!document.getElementById('{c['syl_id']}')")] + ([(firsts[cx], cx)] if cx in firsts else [])
    n0 = len(fails)
    for pid, kind in pages:
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(30)
        r = pg.evaluate(NAV_JS)
        bad = []
        if (r['nMain'], r['nSub'], r['inPanels']) != (1, 1, 0) or not r['inDrawer'] or not r['order']: bad.append(f"{r['nMain']} main-nav, {r['nSub']} sub-nav, {r['inPanels']} in a panel, in the drawer's list {r['inDrawer']}, main first {r['order']}")
        if [x[:2] for x in r['main']] != main or r['mainOther']: bad.append(f"main nav {[x[:2] for x in r['main']]} (+{r['mainOther']} other), expected {main}")
        want = ('home' if kind == 'root' else pid if kind == 'area' else 'track-' + sec[kind][0])
        cur = 'page' if want == pid else 'true'
        act = [[x[0], x[3]] for x in r['main'] if x[2]]
        if act != [[want, cur]]: bad.append(f'main nav marks {act}, expected {[[want, cur]]}')
        if r['siteInNav']: bad.append(f"links to {r['siteInNav']} in the navs")
        if kind == 'root':
            if not r['subHidden'] or r['groups']: bad.append(f"sub-nav shown ({r['groups']}) on a page of the home")
        elif kind == 'area':
            if r['subHidden'] or r['groups'] != [pid] or r['subLinks'] != area[pid]: bad.append(f"sub-nav {r['groups']} {r['subLinks']}, expected [{pid}] {area[pid]}")
        else:
            if r['subHidden'] or r['groups'] != [kind] or not r['subLinks'] or r['subLinks'][0] != sec[kind][1] or r['subActive'] != [pid]:
                bad.append(f"sub-nav {r['groups']}, first {r['subLinks'][:1]}, marked {r['subActive']}, expected [{kind}], first {sec[kind][1]}, marked [{pid}]")
        if bad: fails.append(f'nav {label} #{pid}: ' + '; '.join(bad))
    pg.evaluate("location.hash = 'home'"); ready(pg)
    foot = pg.evaluate(NAV_FOOT_JS)
    want = {'new': True, 'changelog': None if 'changelog' in OMIT else True, 'backlog': None if 'backlog' in OMIT else True}
    if foot != want: fails.append(f'nav {label}: the home\'s links to What\'s new, the Changelog and the Backlog {foot}, expected at its foot {want}')
    # the drawer, from the first course's first reading page (or its home)
    cx = next(iter(firsts), None) or next(iter(sec), None)
    page = firsts.get(cx) or sec[cx][1]
    tr = 'track-' + sec[cx][0]
    pg.evaluate(f"location.hash = '{page}'"); ready(pg); pg.wait_for_timeout(60)
    wait = 400 if motion else 120
    if w < 1100:
        pg.click('#menuB'); pg.wait_for_timeout(wait)
        d = pg.evaluate(NAV_DRAWER_JS)
        if not (d['on'] and d['locked'] and d['focus'] == 'closeB' and d['hidden'] == 'false' and d['expanded'] == 'true'): fails.append(f'nav {label}: the menu does not open the drawer as before: {d}')
        if not d['main'] or not d['sub'] or d['main'][0] < 0 or d['sub'][0] < 0 or max(d['main'][1], d['sub'][1]) > d['vw'] or not d['main'][3] or not d['sub'][3]: fails.append(f'nav {label}: open drawer, main nav {d["main"]}, sub-nav {d["sub"]}, not both on screen')
        if d['actIn'] is False: fails.append(f'nav {label}: the current item is not scrolled into the drawer\'s list')
        pg.keyboard.press('Escape'); pg.wait_for_timeout(wait)
        d = pg.evaluate(NAV_DRAWER_JS)
        if d['on'] or d['locked'] or d['focus'] != 'menuB' or d['hidden'] != 'true': fails.append(f'nav {label}: Escape leaves the drawer {d}')
        pg.click('#menuB'); pg.wait_for_timeout(wait)
    elif h < 860:   # S-NAV2 step C: 1100 px or wider under 860 px tall (the tablet landscape layout), both navs in the 240 px sidebar
        d = pg.evaluate(NAV_DRAWER_JS)
        if not d['main'] or not d['sub'] or d['main'][0] < 0 or d['hidden'] != 'false' or not d['sub'][3]: fails.append(f'nav {label}: the sidebar does not show both navs: {d}')
        if d['main'] and d['main'][1] > side_px(w, h) + 1: fails.append(f'nav {label}: the main nav runs {d["main"][:2]}, outside the {side_px(w, h):.0f} px sidebar')
    else:   # S-NAV2 step D: a desktop (1100 px and 860 px tall or more): the main nav in the top bar, fixed beside the brand; the sub-nav in the sidebar
        d = pg.evaluate(NAV_DRAWER_JS)
        bar = pg.evaluate("Math.round(document.querySelector('.top').getBoundingClientRect().height)")
        sp = side_px(w, h)
        if not d['main'] or d['main'][2] != 0 or d['main'][3] > bar + 1 or abs(d['main'][0] - sp) > 1 or d['main'][1] > w: fails.append(f'nav {label}: the main nav at {d["main"]}, expected in the top bar (top 0, at most {bar} px tall) from the {sp:.0f} px sidebar\'s edge')
        if not d['sub'] or d['sub'][0] < 0 or d['sub'][1] > sp + 1 or d['sub'][2] < bar - 1 or d['hidden'] != 'false' or not d['sub'][3]: fails.append(f'nav {label}: the sub-nav at {d["sub"]} (aria-hidden {d["hidden"]}), expected in the {sp:.0f} px sidebar under the {bar} px bar')
    pg.click(f'#drawer nav.main-nav a.ditem[data-target="{tr}"]'); pg.wait_for_timeout(wait); ready(pg)
    at = pg.evaluate("() => [[...document.querySelectorAll('.panel')].find(p => !p.hidden).id, location.hash, document.getElementById('drawer').classList.contains('on')]")
    if at != [tr if MULTI else 'home', '#' + tr, False]: fails.append(f'nav {label}: the main nav\'s {tr} lands on {at}, expected {[tr if MULTI else "home", "#" + tr, False]}')
    pg.evaluate('history.back()'); pg.wait_for_timeout(120); ready(pg)
    back = pg.evaluate("[...document.querySelectorAll('.panel')].find(p => !p.hidden).id")
    if back != page: fails.append(f'nav {label}: back from the area lands on {back}, expected {page}')
    if not MULTI:   # S-NAV1 step G (the fresh check's finding 9): on the home, the area entry (its band, on the home) adds no entry
        pg.evaluate("location.hash = 'home'"); ready(pg); pg.wait_for_timeout(60)
        n0h = pg.evaluate('history.length')
        if w < 1100: pg.click('#menuB'); pg.wait_for_timeout(wait)
        pg.click(f'#drawer nav.main-nav a.ditem[data-target="{tr}"]'); pg.wait_for_timeout(wait); ready(pg)
        at = pg.evaluate("() => [[...document.querySelectorAll('.panel')].find(p => !p.hidden).id, location.hash, history.length]")
        if at != ['home', '#' + tr, n0h]: fails.append(f'nav {label}: on the home the main nav\'s {tr} gives {at}, expected the home at #{tr} with no new entry ({n0h})')
    if errs: fails.append(f'nav {label}: console errors ' + ' | '.join(errs[:3]))
    ctx.close()
    if len(fails) == n0: print(f'nav {label}: {len(pages)} pages, main nav {" · ".join(x[1] for x in main)}; sub-nav per section; site links at the home\'s foot; drawer from {page} -> {tr} and back')

# ---- S-NAV2 step D (22 Nov 2026): the tablet and desktop layouts of theme 6.22 (S-NAV2 step C), the phone unchanged --
# The spec (Pedro, 21 Nov 2026): a desktop (1100 px wide and 860 px tall or more) has the main nav in a top bar, the
# sub-nav in a persistent sidebar where there is one, a centred column and an on-this-page outline at a unit page's
# right; a tablet landscape (900 to 1099 px, or wider but under 860 px tall) a narrower sidebar from 1100 px (900 to
# 1099 px keep the drawer: step C, NEEDS PEDRO 1, shell.js turns the drawer into the sidebar at 1100 px) and no
# outline; a tablet portrait (768 to 899 px) the drawer; a phone the drawer, untouched.
NEW_VIEWPORTS = [('tab1024', 1024, 768, False), ('wide1920', 1920, 1080, False)]   # beside VIEWPORTS' 1280 x 800 ('desktop': the tablet landscape layout since 6.22)
LAYOUTS = [(390, 844), (800, 1100), (1024, 768), (1280, 800), (1440, 900), (1920, 1080)]   # one of each layout, the desktop at two widths
HERO_AT = (1024, 1280, 1920)   # P-HK1: the hero bound checked at these widths
FOLD_AT = ((1024, 768), (1280, 800))   # the tablet landscape homes whose first tiles must show above the fold
def layout_of(w, h):
    """Which of theme 6.22's layouts a w x h viewport gets (design/theme.css section 6, the S-NAV2 step C block)."""
    if w < 768: return 'phone'
    if w < 900: return 'portrait'
    if w < 1100: return 'landscape'   # the drawer (step C, NEEDS PEDRO 1)
    return 'landscape-side' if h < 860 else 'desktop'
def side_px(w, h):
    """The sidebar's width in px: 240 in the tablet landscape layout from 1100 px, clamp(240px, 18vw, 300px) on a desktop."""
    k = layout_of(w, h)
    return 240 if k == 'landscape-side' else min(300, max(240, .18 * w)) if k == 'desktop' else 0

REGIONS_JS = r"""(pid) => { const de = document.documentElement, P = document.getElementById(pid), r = e => e.getBoundingClientRect();
  const dr = document.getElementById('drawer'), drr = r(dr), tp = r(document.querySelector('.top')), mn = document.querySelector('nav.main-nav'), mr = r(mn);
  const sn = document.querySelector('nav.sub-nav'), sr = r(sn), mainR = r(document.querySelector('main')), bs = getComputedStyle(document.body);
  const sm = P.querySelector('.secmenu'), ol = sm && sm.querySelector('.seclist'), sb = P.querySelector('.stepbar');
  if (sb) { window.scrollTo(0, 0); window.scrollTo(0, Math.max(0, sb.getBoundingClientRect().top - tp.height)); }   // the section bar stuck under the top bar, as the outline beside it is read
  const olr = ol && r(ol), mh = sm ? parseFloat(getComputedStyle(sm, '::details-content').maxHeight) : NaN;   // the outline scrolls inside the menu's ::details-content, at most the window less the bar
  const box = b => [b.left, b.right, b.top, b.bottom].map(Math.round);
  return {W: de.clientWidth, H: innerHeight, kind: P.getAttribute('data-kind'),
    sidebar: getComputedStyle(dr).visibility === 'visible' && drr.right > 0 && drr.width > 0 && !dr.classList.contains('on'),
    drawer: box(drr), aria: dr.getAttribute('aria-hidden'), menu: getComputedStyle(document.getElementById('menuB')).display !== 'none',
    top: box(tp), mainNav: box(mr), mainFixed: getComputedStyle(mn).position === 'fixed', mainVis: getComputedStyle(mn).visibility,
    subHidden: sn.hidden, sub: box(sr), main: box(mainR), pad: [parseFloat(bs.paddingLeft), parseFloat(bs.paddingRight)],
    menuOpen: !!(sm && sm.open), outline: sm && !sm.open && ol.checkVisibility() && olr.width > 0 && olr.height > 0 ? [olr.left, olr.right, olr.top, olr.top + Math.min(olr.height, mh || Infinity)].map(Math.round) : null,   // shown while the menu is closed: the outline (a closed menu's list is content-visibility hidden)
    supports: CSS.supports('selector(::details-content)'), scroll: [de.scrollWidth, de.clientWidth]}; }"""
# every heading, figure and table of the shown panel (a reading page whole, every <details> but its section menu open):
# inside the column and the screen, beside the sidebar, clear of the outline; a heading that hides its overflow not
# cut; a figure's frame that is narrower than its drawing scrolls (overflow-x auto or scroll), never clips; a table that
# scrolls inside its own frame (.tbl) measured by that frame
CLIP_JS = r"""([pid, side, outline]) => { const P = document.getElementById(pid), W = document.documentElement.clientWidth, bad = [];
  P.querySelectorAll('.stepbar .whole[aria-pressed="false"]').forEach(b => b.click());
  P.querySelectorAll('details:not(.secmenu)').forEach(d => d.open = true);
  const m = document.querySelector('main').getBoundingClientRect(), lo = Math.max(side, m.left) - 1, hi = Math.min(W, m.right) + 1;
  const name = e => e.tagName.toLowerCase() + (typeof e.className === 'string' && e.className ? '.' + e.className.split(' ')[0] : '') + ' "' + e.textContent.trim().slice(0, 30) + '"';
  let n = 0;
  const scroller = e => { for (let a = e.parentElement; a && a !== P; a = a.parentElement) if (['auto', 'scroll'].includes(getComputedStyle(a).overflowX)) return a; return null; };
  for (const t of P.querySelectorAll('h1, h2, h3, figure, table')) { const e = t.tagName === 'TABLE' && scroller(t) || t;   // a table scrolls inside its own frame (.tbl): the frame is measured
    const b = e.getBoundingClientRect(); if (!b.width || !b.height) continue; n++;
    if (b.left < lo || b.right > hi) bad.push(`${name(e)} runs ${Math.round(b.left)}..${Math.round(b.right)}, past the column ${Math.round(lo + 1)}..${Math.round(hi - 1)}`);
    if (outline && b.right > outline[0] + 1 && b.left < outline[1]) bad.push(`${name(e)} under the outline`);
    if (/^H[123]$/.test(e.tagName) && getComputedStyle(e).overflowX !== 'visible' && e.scrollWidth > e.clientWidth + 1) bad.push(`${name(e)} cut: ${e.scrollWidth} px in ${e.clientWidth}`);
    if (e.tagName === 'FIGURE') e.querySelectorAll('.viz-scroll').forEach(f => { if (f.clientWidth && f.scrollWidth > f.clientWidth + 1 && !['auto', 'scroll'].includes(getComputedStyle(f).overflowX)) bad.push(`${name(e)}: its frame clips its drawing (${f.scrollWidth} px in ${f.clientWidth}, overflow-x ${getComputedStyle(f).overflowX})`); }); }
  return {n, bad: bad.slice(0, 6)}; }"""
FOLD_JS = r"""() => { const g = document.querySelector('#home > .cgrid.areas') || document.querySelector('#home .track .cgrid'); if (!g) return null;
  const ts = [...g.querySelectorAll(':scope > a.course')], t0 = ts.length && ts[0].getBoundingClientRect().top;
  return ts.filter(t => Math.abs(t.getBoundingClientRect().top - t0) < 2).map(t => [t.getAttribute('data-target'), Math.round(t.querySelector('.ctitle').getBoundingClientRect().bottom), Math.round(t.querySelector('.cstats').getBoundingClientRect().bottom), Math.round(t.getBoundingClientRect().top)]); }"""
HERO_BOUND_JS = r"""(pid) => { const P = document.getElementById(pid), h = P && P.querySelector(':scope > header.hero'); if (!h) return null;
  const bs = getComputedStyle(document.body), W = document.body.clientWidth - parseFloat(bs.paddingLeft) - parseFloat(bs.paddingRight);
  return {H: h.getBoundingClientRect().height, W, root: P.classList.contains('root'), log: P.classList.contains('log'), topo: h.classList.contains('has-topo') || P.classList.contains('root')}; }"""

def layout_pages():
    """The pages the layout check opens: the home, What's new and the Changelog (no sub-nav), the first area page, the
    sampled course homes (the first history and the first markdown one) and the first reading page of every course."""
    hs, ms = [x for x in SAMPLE if x in HIST_HOMES], [x for x in SAMPLE if x not in HIST_HOMES]
    return (['home', 'new'] + [x for x in ('changelog',) if x not in OMIT] + AREA_IDS[:1] + hs[:1] + ms[:1],
            ['home', 'new'] + AREA_IDS + SAMPLE)

def check_layouts(br, fails):
    """S-NAV2 step D: at 390 x 844, 800 x 1100, 1024 x 768, 1280 x 800, 1440 x 900 and 1920 x 1080 (one of each layout of
    theme 6.22, the desktop twice), dark, on the home, What's new, the Changelog, an area page, a history and a markdown
    course home and the first reading page of every course: the sidebar, the top bar and the outline where the spec puts
    them and nowhere else (layout_of: a phone, a tablet portrait and a 900 to 1099 px tablet landscape the drawer off
    screen with its menu button, no sidebar, no outline, the top bar the screen's width; from 1100 px under 860 px tall
    the 240 px sidebar holding both navs, the top bar beside it, no outline; a desktop the top bar across the screen
    with the main nav fixed in it from the sidebar's edge, the sidebar (clamp(240px, 18vw, 300px)) only where there is a
    sub-nav, the content beside it, the outline (the unit's section list, ::details-content) at the right of every
    reading page clear of the column and inside the window, where the browser supports ::details-content, and on no
    other page); no sideways scroll; no heading, figure or table past the column or the screen, under the sidebar or the
    outline, a heading cut or a figure's frame clipping its drawing (CLIP_JS, a reading page whole). At 1024 x 768 and
    1280 x 800 the home's first row of tiles shows its titles and stats above the fold (in an edition of one track, whose
    band header stands between the hero and the tiles, the row starts at least 44 px above it: out/S-NAV2/step-D.md
    BUGS 1). At 1024, 1280 and 1920 px (P-HK1)
    every hero holds its bound (W the width beside the sidebar): a course home's and an area page's at least
    max(370, .4 W - 22) px, What's new's at least .27 W - 22, the home's between .4 W - 22 and .54 W - 22."""
    errs, n0, said = [], len(fails), []
    pages, heroes = layout_pages()
    with_reads = None
    for w, h in LAYOUTS:
        kind, sp = layout_of(w, h), side_px(w, h)
        ctx, pg, _ = new_page(None, br, errs, f'layout {w}x{h}', w, h, w < 900)
        if with_reads is None:   # the first reading page of every course context, as the shell orders them
            with_reads = pages + pg.evaluate("""() => { const seen = {}, out = []; document.querySelectorAll('.panel[data-kind="report"]').forEach(p => { const c = p.getAttribute('data-ctx'); if (!seen[c]) { seen[c] = 1; out.push(p.id); } }); return out; }""")
        nclip = 0
        for pid in with_reads:
            if not pg.evaluate(f"!!document.getElementById('{pid}')"): continue
            pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
            g = pg.evaluate(REGIONS_JS, pid)
            tag, bad = f'layout {w}x{h} ({kind}) #{pid}', []
            report = g['kind'] == 'report'
            if g['scroll'][0] > g['scroll'][1]: bad.append(f'scrolls sideways ({g["scroll"][0]} in {g["scroll"][1]} px)')
            if kind in ('phone', 'portrait', 'landscape'):
                if g['sidebar'] or g['drawer'][1] > 0 or not g['menu'] or g['aria'] != 'true': bad.append(f'expected the drawer off screen with its menu button: drawer {g["drawer"]}, menu {g["menu"]}, aria-hidden {g["aria"]}')
                if g['top'][0] != 0 or abs(g['top'][1] - g['W']) > 1: bad.append(f'the top bar spans {g["top"][:2]}, expected 0..{g["W"]}')
                if g['mainFixed'] or g['mainNav'][1] > 0: bad.append(f'the main nav at {g["mainNav"]} (fixed {g["mainFixed"]}), expected inside the closed drawer')
                if g['outline']: bad.append(f'an outline at {g["outline"]}, none below the desktop')
            elif kind == 'landscape-side':
                if not g['sidebar'] or g['drawer'][0] != 0 or abs(g['drawer'][1] - sp) > 1 or g['menu'] or g['aria'] != 'false': bad.append(f'expected the {sp} px sidebar, no menu button: drawer {g["drawer"]}, menu {g["menu"]}, aria-hidden {g["aria"]}')
                if abs(g['top'][0] - sp) > 1 or abs(g['top'][1] - g['W']) > 1: bad.append(f'the top bar spans {g["top"][:2]}, expected {sp}..{g["W"]}')
                if g['mainFixed'] or g['mainNav'][0] < 0 or g['mainNav'][1] > sp + 1: bad.append(f'the main nav at {g["mainNav"]}, expected in the sidebar')
                if not g['subHidden'] and (g['sub'][0] < 0 or g['sub'][1] > sp + 1): bad.append(f'the sub-nav at {g["sub"]}, expected in the sidebar')
                if g['main'][0] < sp - 1: bad.append(f'the column starts at {g["main"][0]} px, under the sidebar')
                if g['outline']: bad.append(f'an outline at {g["outline"]}, none in the tablet landscape layout')
            else:   # desktop
                if g['top'][0] != 0 or abs(g['top'][1] - g['W']) > 1: bad.append(f'the top bar spans {g["top"][:2]}, expected across the screen 0..{g["W"]}')
                if not g['mainFixed'] or g['mainNav'][2] != 0 or g['mainNav'][3] > g['top'][3] + 1 or abs(g['mainNav'][0] - sp) > 1 or g['mainVis'] != 'visible': bad.append(f'the main nav at {g["mainNav"]} (fixed {g["mainFixed"]}, {g["mainVis"]}), expected in the top bar from {sp:.0f} px')
                if g['menu']: bad.append('the menu button is shown')
                if g['subHidden']:
                    if g['sidebar'] or g['pad'][0]: bad.append(f'a sidebar ({g["drawer"]}, body padded {g["pad"][0]} px) on a page without a sub-nav')
                else:
                    if not g['sidebar'] or g['drawer'][0] != 0 or abs(g['drawer'][1] - sp) > 1 or g['aria'] != 'false': bad.append(f'expected the {sp:.0f} px sidebar: drawer {g["drawer"]}, aria-hidden {g["aria"]}')
                    if g['sub'][0] < 0 or g['sub'][1] > sp + 1 or g['sub'][2] < g['top'][3] - 1: bad.append(f'the sub-nav at {g["sub"]}, expected in the sidebar under the bar')
                    if g['main'][0] < sp - 1: bad.append(f'the column starts at {g["main"][0]} px, under the sidebar')
                if report and g['supports']:
                    o = g['outline']
                    if not o: bad.append('no outline beside the reading page')
                    elif o[0] < g['main'][1] - 1 or o[1] > g['W'] + 1 or o[2] < g['top'][3] - 1 or o[3] > g['H'] + 1: bad.append(f'the outline at {o}, expected right of the column (to {g["main"][1]}) and inside the window')
                elif report and not said: said.append(1); print(f'layout: this browser has no ::details-content; the outline is not expected (the section menu stays)')
                if not report and g['outline']: bad.append(f'an outline at {g["outline"]} on a page that is not a unit')
            c = pg.evaluate(CLIP_JS, [pid, sp if g['sidebar'] else 0, g['outline']]); nclip += c['n']
            bad += c['bad']
            if bad: fails.append(f'{tag}: ' + '; '.join(bad))
        if (w, h) in FOLD_AT:   # the first tiles above the fold on a tablet landscape home
            pg.evaluate("location.hash = 'home'"); ready(pg); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(120)
            f = pg.evaluate(FOLD_JS)
            if not f: fails.append(f'layout {w}x{h}: no tiles on the home')
            elif MULTI:
                low = [x[:3] for x in f if x[1] > h or x[2] > h]
                if low: fails.append(f'layout {w}x{h}: the home\'s first tiles {low} end their title or stats below the {h} px fold')
                else: print(f'layout {w}x{h}: the home\'s first row of {len(f)} tiles shows its titles and stats above the fold (lowest stats at {max(x[2] for x in f)} of {h} px)')
            else:   # an edition of one track: its band's header stands between the hero and the tiles; the row must start above the fold (step D, BUGS: its titles and stats fall below it, for Pedro)
                low = [x for x in f if x[3] > h - 44]
                if low: fails.append(f'layout {w}x{h}: the home\'s first tiles {low} start below the {h} px fold')
                else: print(f'layout {w}x{h}: one track: the home\'s first row of {len(f)} tiles starts above the fold (at {min(x[3] for x in f)} px), its titles end at {max(x[1] for x in f)} and its stats at {max(x[2] for x in f)} of {h} px (S-NAV2 step D BUGS 1)')
        if w in HERO_AT:   # P-HK1: the hero bound at every width
            hb = []
            for pid in heroes:
                if not pg.evaluate(f"!!document.getElementById('{pid}')"): continue
                pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(60)
                b = pg.evaluate(HERO_BOUND_JS, pid)
                if not b or not b['topo']: continue
                W = b['W']
                lo, hi = ((.4 * W - 22, .54 * W - 22) if b['root'] else (.27 * W - 22, None) if b['log'] else (max(370, (.4 if w >= 900 else .5) * W - 22), None))
                if b['H'] < lo - 1 or (hi and b['H'] > hi + 1): fails.append(f'hero {w}x{h} #{pid}: {b["H"]:.0f} px tall beside {W:.0f} px, expected {lo:.0f}' + (f' to {hi:.0f}' if hi else ' or more') + ' (P-HK1)')
                hb.append(f'{pid} {b["H"]:.0f}')
            print(f'hero bound {w}x{h}: ' + ', '.join(hb))
        print(f'layout {w}x{h} ({kind}): {len(with_reads)} pages, {nclip} headings, figures and tables inside the column' + (f', sidebar {sp:.0f} px' if sp else ''))
        ctx.close()
    if errs: fails.append('layout: console errors: ' + ' | '.join(errs[:3]))

# The desktop top bar's main nav (S-NAV2 step E, the fresh check's finding 1: at 1100 to about 1140 px the six areas'
# items needed 745 px in a 704 px bar and "Supply Chain" was cut under the theme button, with the scrollbar hidden).
TOPBAR_AT = [(1100, 900), (1120, 900), (1140, 900), (1280, 900), (1440, 900), (1920, 1080)]
TOPBAR_PROBE = 8   # areas in the probe copy of the bar: the real items, then copies of the first areas to make eight
TOPBAR_JS = r"""(probe) => { const n = document.querySelector('nav.main-nav');
  if (probe) { const ar = [...n.querySelectorAll(':scope > .ditem')].slice(1); for (let k = 0; ar.length + k < probe; k++) { const c = ar[k % ar.length].cloneNode(true); c.removeAttribute('aria-current'); c.classList.remove('is-active'); c.setAttribute('aria-hidden', 'true'); c.removeAttribute('href'); n.appendChild(c); } }
  const r = n.getBoundingClientRect(), cs = getComputedStyle(n), lo = r.left + n.clientLeft, hi = lo + n.clientWidth;
  const btn = [...document.querySelectorAll('.top-in > *')].filter(e => e.getBoundingClientRect().width > 0).map(e => e.getBoundingClientRect().left);
  const its = [...n.querySelectorAll(':scope > .ditem')].map(a => { const b = a.getBoundingClientRect(); return [a.textContent.trim(), Math.round(b.left), Math.round(b.right), a.scrollWidth > a.clientWidth + 1]; });
  return {fixed: cs.position === 'fixed', items: its, lo: Math.round(lo), hi: Math.round(hi), sw: n.scrollWidth, cw: n.clientWidth, sl: n.scrollLeft, btn: btn.length ? Math.round(Math.min(...btn)) : null}; }"""
def check_topbar(br, fails, body=None):
    """S-NAV2 step E: at 1100, 1120, 1140 and 1280 x 900, 1440 x 900 and 1920 x 1080 (the desktop layout, 860 px tall or
    more), dark and light, on the home and the first area page, with the edition's real areas and with a probe copy of
    the bar holding TOPBAR_PROBE areas (copies of its first areas appended): the main nav is fixed in the top bar, does
    not scroll (scrollWidth at most clientWidth), every item lies whole inside it and is not cut itself, and the nav ends
    left of the theme and arrow buttons. body: serve this HTML in place of the built shell (the fail-test's hook)."""
    errs, out = [], []
    for w, h in TOPBAR_AT:
        for th in ('dark', 'light'):
            ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1, color_scheme=th, reduced_motion='reduce')
            ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
            ctx.route('**/fonts.gstatic.com/**', font_file)
            if body: ctx.route(URL, lambda r: r.fulfill(status=200, content_type='text/html', body=body))
            pg = ctx.new_page()
            pg.on('console', lambda m: errs.append(f'topbar {w}x{h}: {m.text}') if m.type == 'error' else None)
            pg.goto(URL + '#home'); pg.wait_for_timeout(150)
            pg.evaluate(f"localStorage.setItem('{THEME_KEY}', '{th}')")
            for pid in ['home'] + AREA_IDS[:1]:
                for probe in (0, TOPBAR_PROBE):
                    pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(100)
                    g = pg.evaluate(TOPBAR_JS, probe)
                    tag, bad = f'topbar {w}x{h} {th} #{pid}' + (f' (probe: {TOPBAR_PROBE} areas)' if probe else ''), []
                    if not g['fixed']: bad.append('the main nav is not in the top bar (not the desktop layout)')
                    if g['sw'] > g['cw'] + 1: bad.append(f'the main nav overflows: {g["sw"]} px of items in {g["cw"]}')
                    cut = [f'{t} {a}..{b}' for t, a, b, c in g['items'] if a < g['lo'] - 1 or b > g['hi'] + 1 or c]
                    if cut: bad.append(f'items cut or past the bar {g["lo"]}..{g["hi"]}: {", ".join(cut)}')
                    if g['btn'] is not None and g['hi'] > g['btn'] + 1: bad.append(f'the main nav runs to {g["hi"]}, under the buttons from {g["btn"]}')
                    if bad: fails.append(f'{tag}: ' + '; '.join(bad))
                    if pid == 'home' and th == 'dark': out.append(f'{w}: {len(g["items"]) - 1} areas {g["items"][-1][2] - g["lo"] + 8} of {g["cw"]} px')
            ctx.close()
    if errs: fails.append('topbar: console errors: ' + ' | '.join(errs[:3]))
    print('top bar (desktop, dark and light, the home and an area page; real and a probe of ' + f'{TOPBAR_PROBE} areas): ' + '; '.join(out))

# S-NAV2's shot layouts (the row's "Before publishing, stop": shots to Pedro): the first screen of the home, an area
# page, a course home and a unit page in the three layouts he judges, dark and light, reduced motion, scale 1.
LAYOUT_SHOTS = [('desktop', 1440, 900, False), ('tablet-landscape', 1280, 800, True), ('tablet-portrait', 800, 1100, True)]
LAYOUT_SHOTS_DIR = pathlib.Path(sys.argv[sys.argv.index('--layout-shots') + 1]) if '--layout-shots' in sys.argv else None
def layout_shots(br, out):
    """Writes <page>-<layout>-<theme>.png to out: page home, area (the first area page), course (the first history
    course home, or the first sampled one) and unit (that course's report 2.3, or the first reading page in the shell);
    layout desktop 1440 x 900, tablet-landscape 1280 x 800, tablet-portrait 800 x 1100; theme dark and light. Each is
    the first screen, as the reader opens the page (a unit on section 1). Run alone with --layout-shots DIR (no check
    runs and nothing is recorded); --shots DIR also writes them into DIR."""
    out = pathlib.Path(out); out.mkdir(parents=True, exist_ok=True)
    shell = (SITE / 'index.html').read_text()
    course = LEAD['home_id'] if LEAD else ([x for x in SAMPLE if x in HIST_HOMES] + SAMPLE)[0]
    m = re.search(r'<section class="panel[^"]*" id="(read-[^"]+)"', shell)
    unit = rid(LEAD, '2.3') if LEAD else (m.group(1) if m else None)
    pages = [('home', 'home'), ('area', AREA_IDS[0] if AREA_IDS else None), ('course', course), ('unit', unit)]
    n = 0
    for lay, w, h, touch in LAYOUT_SHOTS:
        for th in ('dark', 'light'):
            ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1, is_mobile=touch and w < 900, has_touch=touch, color_scheme=th, reduced_motion='reduce')
            ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
            ctx.route('**/fonts.gstatic.com/**', font_file)
            pg = ctx.new_page(); pg.goto(URL + '#home'); pg.wait_for_timeout(150)
            for name, pid in pages:
                if not pid or not pg.evaluate(f"!!document.getElementById('{pid}')"): print(f'layout shots: no {name} page in this edition'); continue
                pg.evaluate(f"localStorage.clear(); localStorage.setItem('{THEME_KEY}', '{th}')")
                pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(300); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(60)
                pg.screenshot(path=str(out / f'{name}-{lay}-{th}.png')); n += 1
            ctx.close()
    print(f'layout shots: {n} in {out} (' + ', '.join(f'{a} #{b}' for a, b in pages if b) + '; ' + ', '.join(f'{l} {w}x{h}' for l, w, h, _ in LAYOUT_SHOTS) + '; dark and light)')

# The 4x CPU throttle frame test of S-NAV1's fresh check (out/S-NAV1/checker.md finding 1, its /tmp/ckscripts/perf.py:
# 5 s of requestAnimationFrame with motion allowed under Emulation.setCPUThrottlingRate 4), here at 1280 x 800. The fault
# it found was the main thread's: p50 frames of 33 to 50 ms and long tasks of 0.9 to 3 s on a course home under the
# throttle (the start build 16.7 ms and none). Measured at S-NAV2 step D (22 Nov 2026) at 1280 x 800, 4x: the course
# and area homes 16.6 to 17.5 ms, no long task; the home 21.1 to 28.3 ms from run to run, and the build before theme
# 6.22's layouts the same (21.1 to 25.3 ms, three runs each): its wide hero's paint on this machine, which draws without
# a GPU. The fault put back (IntersectionObserver removed, so no drawing is paused) gives greece, rome and ux-ia 30.8
# to 32.6 ms at 1280 x 800. So the budget: a course or area home's median at most FRAME_P50_MAX[0] ms, the home's at
# most FRAME_P50_MAX[1] ms (its own paint), no long task over LONGTASK_MAX ms.
FRAMES_JS = r"""async (ms) => { const ts = []; const t0 = performance.now(); let last = t0; window.__lt = 0;
  new PerformanceObserver(l => l.getEntries().forEach(e => { window.__lt = Math.max(window.__lt, e.duration); })).observe({type: 'longtask'});
  while (performance.now() - t0 < ms) { await new Promise(r => requestAnimationFrame(r)); const n = performance.now(); ts.push(n - last); last = n; }
  ts.sort((a, b) => a - b); return {n: ts.length, p50: ts[Math.floor(ts.length / 2)], p95: ts[Math.floor(ts.length * .95)], lt: window.__lt}; }"""
FRAME_P50_MAX, LONGTASK_MAX = (22, 32), 250   # ms: a course or area home (16.6 to 17.5 measured, the fault 30.8 or more), the home (to 28.3 measured); ms
def check_frames(br, fails, w=1280, h=800):
    """S-NAV2 step D: at 1280 x 800 with motion allowed and the CPU throttled 4x (CDP Emulation.setCPUThrottlingRate),
    5 s of requestAnimationFrame on the home, the first area page and the sampled history and markdown course homes:
    the median frame at most FRAME_P50_MAX ms (the home its second value) and no long task over LONGTASK_MAX ms."""
    hs, ms = [x for x in SAMPLE if x in HIST_HOMES], [x for x in SAMPLE if x not in HIST_HOMES]
    out = []
    for pid in ['home'] + AREA_IDS[:1] + hs[:1] + ms[:1]:
        errs = []
        ctx, pg, _ = new_page(None, br, errs, 'frames', w, h, False, motion=True)
        pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(800)
        cdp = ctx.new_cdp_session(pg); cdp.send('Emulation.setCPUThrottlingRate', {'rate': 4}); pg.wait_for_timeout(300)
        r = pg.evaluate(FRAMES_JS, 5000)
        ctx.close()
        out.append(f'{pid} {r["n"]} frames, p50 {r["p50"]:.1f} ms, p95 {r["p95"]:.1f} ms, longest task {r["lt"]:.0f} ms')
        top = FRAME_P50_MAX[pid == 'home']
        if r['p50'] > top or r['lt'] > LONGTASK_MAX: fails.append(f'frames {w}x{h} 4x throttle #{pid}: p50 {r["p50"]:.1f} ms (at most {top}), longest task {r["lt"]:.0f} ms (at most {LONGTASK_MAX})')
        if errs: fails.append(f'frames #{pid}: console errors ' + ' | '.join(errs[:3]))
    print(f'frames {w}x{h}, 4x CPU throttle, motion, 5 s: ' + '; '.join(out))

# The phone byte identity (S-NAV2 spec: "a byte-for-byte check that nothing at 390 px or below changes (computed layout
# and screenshots, and nav_diff_check.py classes: the only differences are theme CSS)"). A stored fixture of computed
# layout would not survive the next unit filed (every page it touches moves), so the start build's phone is derived:
# nav_diff_check proved S-NAV2's every built difference is the theme CSS, the shell JS (the ?debug readout, inert
# without ?debug) and the home's --n on p.harea (inert under the start's CSS); so the current shell served with the
# start's theme in its <style> (PHONE_REF's kit/shell.css, the brand's tokens and comment strip applied as build.py
# applies them) is the start build's phone. Both are loaded at 320 x 640 and 360 x 780 (dark) and 390 x 844 (dark and
# light), under reduced motion, on the home, the first area page, a course home, a reading page (its drawer open too)
# and What's new: every element's box and 35 computed properties of the bar, the drawer and the shown panel, and the
# full-page screenshot, must be identical (a difference must persist in three tries). Expected and not measured here:
# PHONE_EXPECTED (the theme CSS itself; the area line's motion, which reduced motion does not run: check_harea). A row
# that changes the phone on purpose sets PHONE_REF to its own start.
# The phone CSS is frozen at this commit for the byte-identity check: re-pin PHONE_REF deliberately when a row changes the phone's design.
PHONE_REF = '445b0c4ddac9a034074ee05c06ea7166eff50209'   # S-NAV2's start (land.py start, 22 Nov 2026), theme 6.19
PHONE_ID_AT = [(320, 640, 'dark'), (360, 780, 'dark'), (390, 844, 'dark'), (390, 844, 'light')]
DUMP_JS = r"""() => { const props = ['display','position','width','height','margin-top','margin-bottom','margin-left','margin-right','padding-top','padding-left','padding-right','padding-bottom','font-size','line-height','color','background-color','grid-template-columns','min-height','max-width','visibility','opacity','transform','border-left-width','box-shadow','content-visibility','overflow-x','overflow-y','top','left','right','bottom','flex-direction','justify-content','column-gap','row-gap','z-index'];
  const out = [], els = [document.documentElement, document.body, ...document.querySelectorAll('.top, .top *, #drawer, #drawer *, #backdrop, main, main > .panel:not([hidden]), main > .panel:not([hidden]) *')];
  for (const e of els) { const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
    out.push([e.tagName, e.id, e.getAttribute('class'), Math.round(r.left * 10) / 10, Math.round(r.top * 10) / 10, Math.round(r.width * 10) / 10, Math.round(r.height * 10) / 10, props.map(p => cs.getPropertyValue(p)).join('|')]); }
  return [document.documentElement.scrollWidth, document.documentElement.scrollHeight, out]; }"""
def _ref_css():
    """PHONE_REF's kit/shell.css as build.py inlines it for this edition (its tokens appended, its comments stripped
    where the brand strips them), and the current shell.css the same way; None and the reason if PHONE_REF cannot be read
    (a shallow clone fetches the one commit first)."""
    import subprocess
    def show():
        return subprocess.run(['git', 'show', f'{PHONE_REF}:kit/shell.css'], cwd=R.parent, capture_output=True, text=True)
    g = show()
    if g.returncode:
        subprocess.run(['git', 'fetch', '-q', '--depth', '1', 'origin', PHONE_REF], cwd=R.parent, capture_output=True, text=True, timeout=300)
        g = show()
    if g.returncode: return None, None, (g.stderr.strip().splitlines() or ['git show failed'])[0]
    strip = brand(EDITION).get('strip_comments', True)
    t = (lambda c: re.sub(r'/\*.*?\*/', '', c, flags=re.S)) if strip else (lambda c: c)
    return t((R / 'shell.css').read_text()), t(g.stdout), None
def check_phone_identity(br, fails):
    import hashlib
    cur, ref, why = _ref_css()
    if why: fails.append(f'phone identity: the reference theme ({PHONE_REF[:7]}) cannot be read: {why}'); return
    shell = (SITE / 'index.html').read_text()
    if cur not in shell: fails.append('phone identity: the built shell does not inline kit/shell.css as build.py does (rebuild first)'); return
    old = shell.replace(cur, ref, 1).encode()
    hs, ms = [x for x in SAMPLE if x in HIST_HOMES], [x for x in SAMPLE if x not in HIST_HOMES]
    reads = [rid(LEAD, '2.3')] if LEAD else []
    pages = ['home'] + AREA_IDS[:1] + (hs[:1] or ms[:1]) + (reads or [])
    if not reads:   # an edition without a history course: the first markdown reading page in the shell
        m = re.search(r'<section class="panel[^"]*" id="(read-[^"]+)"', shell); pages += [m.group(1)] if m else []
    pages += ['new']
    def measure(start, w, h, th):
        ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=1, is_mobile=True, has_touch=True, color_scheme=th, reduced_motion='reduce')
        ctx.route('**/fonts.googleapis.com/**', lambda r: r.fulfill(status=200, content_type='text/css', body=FONT_CSS))
        ctx.route('**/fonts.gstatic.com/**', font_file)
        if start: ctx.route(URL, lambda r: r.fulfill(status=200, content_type='text/html', body=old))
        pg = ctx.new_page(); pg.goto(URL + '#home'); pg.wait_for_timeout(200)
        pg.evaluate(f"localStorage.setItem('{THEME_KEY}', '{th}')")
        res = {}
        for pid in pages:
            pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(500)
            res[pid] = (pg.evaluate(DUMP_JS), hashlib.sha256(pg.screenshot(full_page=True)).hexdigest())
            if pid in reads or pid.startswith('read-'):
                pg.evaluate("document.getElementById('menuB').click()"); pg.wait_for_timeout(500)
                res[pid + ' drawer'] = (pg.evaluate(DUMP_JS), hashlib.sha256(pg.screenshot()).hexdigest())
        ctx.close()
        return res
    n = retried = nd = 0
    for w, h, th in PHONE_ID_AT:
        for k in range(3):
            a, b = measure(True, w, h, th), measure(False, w, h, th)
            diff = [pid for pid in a if a[pid] != b.get(pid)]
            if not diff: break
            retried += 1
        n += len(a); nd += len(diff)
        for pid in diff:
            la, lb = a[pid][0], b[pid][0]
            first = next((f'{x} -> {y}' for x, y in zip(la[2], lb[2]) if x != y), f'{len(la[2])} -> {len(lb[2])} elements' if len(la[2]) != len(lb[2]) else f'the page {la[:2]} -> {lb[:2]}' if la[:2] != lb[:2] else 'pixels only')
            fails.append(f'phone identity {w}x{h} {th} #{pid}: the layout differs from the start build ({PHONE_REF[:7]}) in three tries: layout {la == lb}, pixels {a[pid][1] == b[pid][1]}; first: {str(first)[:300]}')
    print(f'phone identity: {n} views ({", ".join(pages)}, a reading page\'s drawer open; {", ".join(f"{w}x{h} {th}" for w, h, th in PHONE_ID_AT)}, reduced motion) '
          + (f'{nd} differ from' if nd else 'laid out and drawn byte for byte as') + f' the start build ({PHONE_REF[:7]}, its theme in the current shell); {retried} retries; expected and not measured here: ' + '; '.join(PHONE_EXPECTED))

def check_webkit(p, fails):
    """P-NAV3 (S-NAV2 step D): check_history (go()'s pushes, popstate on back and forward, each entry's scroll kept, the
    replaceState fallback, the sandboxed iframe) and check_pause (the IntersectionObserver's .topo.off, top level and in
    a sandboxed iframe) run again in Playwright's WebKit. Where WebKit is not installed it is left out with one line,
    and the check is Pedro's on an iPhone."""
    try:
        wk = p.webkit.launch()
    except Exception as e:
        print(f'webkit: not available here ({str(e).strip().splitlines()[0][:140]}); history, the scroll save and the pause observer left to an iPhone (P-NAV3)')
        return
    wf = []
    try:
        print(f'webkit {wk.version}:')
        check_history(wk, wf)
        check_pause(wk, wf)
    finally:
        wk.close()
    fails += ['webkit: ' + x for x in wf]
    print('webkit: history, the scroll save and the pause observer ' + (f'{len(wf)} faults' if wf else 'pass'))

def short(iso):
    import datetime
    return datetime.date.fromisoformat(iso).strftime('%-d %b %Y')

def main():
    if LAYOUT_SHOTS_DIR:   # S-NAV2 step E: the shot layouts alone
        with sync_playwright() as p:
            br = p.chromium.launch(); layout_shots(br, LAYOUT_SHOTS_DIR); br.close()
        return
    errors, fails = [], []
    check_files(fails)
    check_viz_keys(fails)
    check_notes(fails)
    check_figure_rules(fails)
    with sync_playwright() as p:
        br = p.chromium.launch()
        check_split(br, fails)
        check_figures(br, fails)
        check_phone_figures(br, fails)
        check_matrix_320(br, fails)
        check_phone_lines(br, fails)
        check_phone_scatters(br, fails)
        check_reading(br, fails)
        check_seps(br, fails)
        check_reliefs(br, fails)   # P95
        check_swell(br, fails)   # S-NAV1 step D
        check_pause(br, fails)   # S-NAV1 step G: a drawing out of view holds still
        check_site_log(br, fails)   # S-PAGES
        check_coming(br, fails)   # S-NEXT1
        check_history(br, fails)   # S-NAV1 step A
        check_debug(br, fails)   # S-NAV2 step B (Fix 2): the ?debug history readout
        check_nav(br, fails)   # S-NAV1 step C: phone, dark
        check_nav(br, fails, theme='light')
        check_nav(br, fails, 1280, 800)
        check_nav(br, fails, 1024, 768)   # S-NAV2 step D: the tablet landscape drawer and the desktop
        check_nav(br, fails, 1920, 1080)
        check_topbar(br, fails)   # S-NAV2 step E: no main nav item cut in the desktop top bar, 1100 to 1920 px
        check_layouts(br, fails)   # S-NAV2 step D: the sidebar, top bar and outline where the spec puts them; the fold; the hero bound (P-HK1)
        check_frames(br, fails)   # S-NAV2 step D: S-NAV1's 4x CPU throttle frame test, at 1280 x 800
        check_phone_identity(br, fails)   # S-NAV2 step D: the phone as the start build's, byte for byte
        check_webkit(p, fails)   # S-NAV2 step D (P-NAV3): history, the scroll save and the pause observer in WebKit, if installed

        # ---- phone ------------------------------------------------------------------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'phone', 390, 844, True)
        if lay != [390, 1]: fails.append(f'phone layout {lay}: expected [390, 1] (missing viewport tag?)')
        else: print('phone layout: 390 px at scale 1')
        check_panels(pg, 'phone', fails)
        pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')"); pg.wait_for_timeout(50)
        check_panels(pg, 'phone light', fails)
        pg.evaluate(f"localStorage.removeItem('{THEME_KEY}'); document.documentElement.removeAttribute('data-theme')")
        # drawer in each context, every unit expanded
        DRAWERS = ['home'] + AREA_IDS + [q for c in COURSES for q in sub_pages(c)]   # P-DEC14: full: the root drawer and every course's drawer context (a history course's home, each markdown sub-course's), not only the ones the navigation visits
        if not SCOPE.full: DRAWERS = ['home'] + AREA_IDS + list(dict.fromkeys(SCOPE.ctx[q] for q in SCOPE.changed if SCOPE.ctx.get(q, 'root') != 'root'))   # scoped: the root drawer and the drawer of each course a changed page is in
        for pid in DRAWERS:
            if not pg.evaluate(f"!!document.getElementById('{pid}')"): continue   # P70: not in this edition
            pg.evaluate(f"location.hash = '{pid}'"); pg.wait_for_timeout(30)
            pg.click('#menuB'); pg.wait_for_timeout(250)
            pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed'))")
            res = pg.evaluate(BOX_JS, ['#drawer', GAP])
            if res['nbad']: fails.append(f'drawer@{pid}: ' + '; '.join(res['bad']))
            sw = pg.evaluate('document.getElementById("drawer").scrollWidth <= document.getElementById("drawer").clientWidth')
            if not sw: fails.append(f'drawer@{pid}: horizontal overflow')
            pg.click('#closeB'); pg.wait_for_timeout(250)

        # navigation context, from a clean slate
        pg.evaluate('localStorage.clear()'); pg.goto(URL + '#home'); pg.reload(); pg.wait_for_timeout(300)
        EXPECT = home_expect()
        check_home(pg, 'phone', fails, EXPECT)
        check_new(pg, 'phone', fails, EXPECT)
        pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
        check_home(pg, 'phone light', fails, EXPECT)
        check_contrast(pg, fails)
        pg.evaluate('localStorage.clear()'); pg.goto(URL + '#home'); pg.reload(); pg.wait_for_timeout(300)
        def state():
            ready(pg)
            return pg.evaluate('''() => ({id: [...document.querySelectorAll('.panel')].find(p => !p.hidden).id,
              nav: document.querySelector('nav.sub-nav').hidden ? 'none' : [...document.querySelectorAll('nav.sub-nav [data-navctx]')].filter(n => !n.hidden).map(n => n.dataset.navctx).join(','),
              u: document.getElementById('curU').textContent, t: document.getElementById('curT').textContent,
              arrows: !document.getElementById('arrows').hidden, prev: !document.getElementById('prevB').disabled, next: !document.getElementById('nextB').disabled,
              cont: [...document.querySelectorAll('.panel:not([hidden]) .hbtn.cont')].map(b => b.hidden ? '(hidden)' : b.querySelector('span').textContent + ' ' + b.querySelector('b').textContent).join('|')})''')
        log = []
        def step(label, expect):
            s = state(); log.append((label, s))
            for k, v in expect.items():
                ok = v(s[k]) if callable(v) else s[k] == v
                if not ok: fails.append(f'nav {label}: {k} = {s[k]!r}, expected {v if not callable(v) else "check"}')
        def tap_course(target):
            """S-NAV1 step B: open a course page from the home as a reader does: with area pages, the home's tile for the
            course's area (the area page checked as a step), then the course's tile there; else the course's tile."""
            if MULTI:
                aid = 'track-' + AREA_OF[target]
                pg.click(f'#home a.course[href="#{aid}"]'); pg.wait_for_timeout(80)
                step(f'{aid} area', dict(id=aid, nav=aid, u='AREA', t=next(x['name'] for x in THEMES if 'track-' + x['id'] == aid), arrows=False))
                pg.click(f'#{aid} a.course[href="#{target}"]'); pg.wait_for_timeout(80)
            else:
                pg.click(f'#home a.course[href="#{target}"]'); pg.wait_for_timeout(80)
        step('home', dict(id='home', nav='none', u='HOME', arrows=False))
        if 'changelog' not in OMIT:
            pg.click('#home a.hbtn[href="#changelog"]'); pg.wait_for_timeout(80)
            step('changelog', dict(id='changelog', nav='none', u=SITE_NAME.upper(), t='Changelog', arrows=False))
            pg.click('#homeB'); pg.wait_for_timeout(80)
        else:   # P70: an edition without the changelog has no button to it and no panel
            if pg.evaluate("!!document.querySelector('a[href=\"#changelog\"], #changelog, a[href=\"#backlog\"], #backlog')"): fails.append(f'edition {EDITION}: a changelog or backlog page or link is built')
        rome_reps = []   # SECOND's reports (S-DEC4: the second history course; Rome in Academy)
        if SECOND:
            S_ = SECOND['home_id']
            tap_course(S_)
            step(f'{S_} home', dict(id=S_, nav=S_, u=f'COURSE {SECOND["num"]}', t=SECOND['short'], arrows=True, prev=False, next=True))
            rome_reps = pg.eval_on_selector_all(f'#{S_} a.hrow', 'as => as.map(a => a.dataset.target)')
        else: print('nav: no second history course in this edition; its course home, report, next, last report, prev and resume steps are left out')
        if rome_reps:
            pg.evaluate(f"document.querySelectorAll('#{S_} details[data-mods]').forEach(d => d.open = true)")
            first = rome_reps[min(4, len(rome_reps) - 1)]
            pg.click(f'#{S_} a.hrow[data-target="{first}"]'); pg.wait_for_timeout(80)
            step(f'{S_} report', dict(id=first, nav=S_, u=lambda u: u.startswith(SECOND['label'] + ' · UNIT ') and u.count(' · ') == 2, arrows=True))
            pg.click('#nextB'); pg.wait_for_timeout(50)
            step(f'{S_} next', dict(nav=S_, id=lambda i: re.match(re.escape(SECOND['prefix']) + r'\d', i) or i in (S_, SECOND['syl_id'])))
            rome_last = pg.eval_on_selector_all(f'.sub-nav [data-navctx="{S_}"] .dunit a.ditem[data-target]', 'as => as.map(a => a.dataset.target)')[-1]
            pg.evaluate(f"location.hash = '{rome_last}'"); pg.wait_for_timeout(50)
            step(f'{S_} last report', dict(id=rome_last, nav=S_, next=False))
            pg.evaluate(f"location.hash = '{rome_reps[0]}'"); pg.wait_for_timeout(50)
            pg.click('#prevB'); pg.wait_for_timeout(50)
            step(f'{S_} prev from first report', dict(id=SECOND['syl_id'], nav=S_, u=SECOND['label'], t='Syllabus and prompts'))
            pg.evaluate(f"location.hash = '{first}'"); pg.wait_for_timeout(50)
        # A4: each history course's "How it was built" page, fetched through the shell, one row per written report
        for cid in [c['home_id'] for c in HIST if 'build' not in OMIT]:
            pg.evaluate(f"location.hash = '{cid}-built'"); pg.wait_for_timeout(50)
            step(f'{cid} how it was built', dict(id=f'{cid}-built', nav=cid, t='How it was built', arrows=True))
            nrow = pg.evaluate(f"document.querySelectorAll('#{cid}-built tr[data-mod]').length")
            nrep = pg.evaluate(f"document.querySelectorAll('.sub-nav [data-navctx=\"{cid}\"] .dunit a.ditem[data-target]').length")
            if nrow != nrep or not nrow: fails.append(f'{cid}-built: {nrow} report rows for {nrep} written reports')
        if 'build' in OMIT and pg.evaluate("!!document.querySelector('[id$=\"-built\"], a[href$=\"-built\"]')"): fails.append(f'edition {EDITION}: a "How it was built" page or link is built')
        pg.evaluate(f"location.hash = '{first}'" if rome_reps else (f"location.hash = '{SECOND['home_id']}'" if SECOND else "location.hash = 'home'")); pg.wait_for_timeout(50)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        step('home again', dict(id='home', nav='none', arrows=False, cont=''))   # P91: no Continue on the home
        if LEAD:   # S-DEC4: the first history course with reports 2.3 and 2.4 (Greece in Academy)
            L_, r23, r24 = LEAD['home_id'], rid(LEAD, '2.3'), rid(LEAD, '2.4')
            tap_course(L_)
            step(f'{L_} home', dict(id=L_, nav=L_, u=f'COURSE {LEAD["num"]}', t=LEAD['short'], prev=False, cont='(hidden)'))
            pg.evaluate(f"document.querySelectorAll('#{L_} details[data-mods]').forEach(d => d.open = true)")
            pg.click(f'#{L_} a.hrow[data-target="{r23}"]'); pg.wait_for_timeout(80)
            step(f'{L_} report', dict(id=r23, nav=L_, u=f'{LEAD["label"]} · UNIT 2 · 2.3', arrows=True, prev=True, next=True))
            pg.click('#nextB'); pg.wait_for_timeout(50)
            step(f'{L_} next', dict(id=r24, nav=L_))
            greek_last = pg.eval_on_selector_all(f'.sub-nav [data-navctx="{L_}"] .dunit a.ditem[data-target]', 'as => as.map(a => a.dataset.target)')[-1]
            pg.evaluate(f"location.hash = '{greek_last}'"); pg.wait_for_timeout(50)
            step(f'{L_} last', dict(id=greek_last, nav=L_, next=False))
            pg.evaluate(f"location.hash = '{r24}'"); pg.wait_for_timeout(50)
            pg.click('#homeB'); pg.wait_for_timeout(80)
            step('home last', dict(id='home', cont=''))
        else: print('nav: no history course with reports ' + ', '.join(SPLIT_MODS) + ' in this edition; its course home, report, next and last steps are left out (the markdown course steps below run)')
        if rome_reps:
            tap_course(SECOND['home_id'])
            step(f'{SECOND["home_id"]} home resumes {SECOND["home_id"]}', dict(id=SECOND['home_id'], cont=lambda c: c.startswith('Continue ') and LEAD['short'] not in c and c != '(hidden)'))
        pg.click('#menuB'); pg.wait_for_timeout(250)
        dr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dtop .ditem .t')].map(t => t.textContent)")
        if rome_reps and dr[:2] != [f'{SECOND["short"]}: course home', 'Syllabus and prompts']: fails.append(f'{SECOND["home_id"]} drawer top: {dr}')   # S-NAV1 step C: the way home is the main nav's
        pg.click('#closeB'); pg.wait_for_timeout(200)
        # the Brand + AI courses (A under Marketing, B under Technology, A3): each its own drawer context with a Units group
        # and a "How it is built" group; written units open reading pages inside the site (never a link out); the reading
        # page is a report (prev/next, continue); the briefs, build order, bibliography and changelog are pages too
        if not MDSUBS: print('nav: no markdown course with a unit filed in this edition; the markdown course steps are left out')
        md_read = None   # the first reading page visited, the tablet pass's report in an edition without a history course
        for bid, short, key, briefs_id, _ in MDSUBS:   # S-DEC4: the edition's first markdown course with a unit filed (Brand + AI in Academy)
            pg.click('#homeB'); pg.wait_for_timeout(80)
            tap_course(bid)
            step(f'{bid} home', dict(id=bid, nav=bid, u=f'COURSE {key}', t=short, arrows=True, prev=False))
            pg.click('#menuB'); pg.wait_for_timeout(250)
            gr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dunit')].map(u => u.querySelector('.ut').textContent + (u.classList.contains('closed') ? ':closed' : ':open'))")
            if gr != ['Units:open', 'How it is built:closed']: fails.append(f'{bid} drawer groups on arrival: {gr}')
            pg.click('#closeB'); pg.wait_for_timeout(200)
            ba = pg.evaluate(f"[...document.querySelectorAll('#{bid} a.course.live')].map(a => a.getAttribute('href'))")   # P93: the unit tiles
            if not ba or not all(h.startswith('#read-') for h in ba): fails.append(f'{bid} written units do not open reading pages: {ba[:3]}')
            # navigation never leaves the site: no artifact link in a hero, a button row or the drawer (a unit's own citations may cite one)
            ext = pg.evaluate(f"[...document.querySelectorAll('.panel[data-ctx=\"{bid}\"] .hero a, .panel[data-ctx=\"{bid}\"] .hlinks a, .panel[data-ctx=\"{bid}\"] .hrows a.hrow:not([target]), [data-navctx=\"{bid}\"] a')].filter(a => a.getAttribute('href').startsWith('http')).map(a => a.href)")
            if ext: fails.append(f'{bid} navigation links out of the site: {ext[:3]}')
            md_read = md_read or ba[0][1:]
            pg.click(f'#{bid} a.course.live[href="{ba[0]}"]'); pg.wait_for_timeout(80)
            step(f'{bid} reading', dict(id=ba[0][1:], nav=bid, u=lambda u: u.startswith(short.upper() + ' · '), arrows=True, prev=True))
            for pid, t in ((f'{bid}-build', 'How it is built'), (f'{bid}-order', 'Build order'), (briefs_id, 'Briefs'), (f'{bid}-bibliography', 'Bibliography'), (f'{bid}-changelog', 'Changelog')):
                pg.evaluate(f"location.hash = '{pid}'"); pg.wait_for_timeout(50)
                step(f'{bid} {t}', dict(id=pid, nav=bid, t=t))
            # A4: the course's "How it was built" page, generated: one row per written unit, read from the front matter
            pg.evaluate(f"location.hash = '{bid}-built'"); pg.wait_for_timeout(50)
            step(f'{bid} How it was built', dict(id=f'{bid}-built', nav=bid, t='How it was built'))
            nrow = pg.evaluate(f"document.querySelectorAll('#{bid}-built tr[data-unit]').length")
            if nrow != len(ba) or not pg.evaluate(f"document.getElementById('{bid}-built').hasAttribute('data-loaded')"):
                fails.append(f'{bid}-built: {nrow} unit rows for {len(ba)} written units, or not fetched through the shell')
            pg.click('#homeB'); pg.wait_for_timeout(80)
            step(f'home after {bid}', dict(id='home', cont=''))
            tap_course(bid)
            step(f'{bid} home resumes', dict(id=bid, cont=lambda c: c.startswith('Continue ') and c != '(hidden)'))
            pg.click('#menuB'); pg.wait_for_timeout(250)
            dr = pg.evaluate("[...document.querySelectorAll('[data-navctx]:not([hidden]) .dtop .ditem .t')].map(t => t.textContent)")
            if dr[:1] != [f'{short}: course home']: fails.append(f'{bid} drawer top: {dr}')   # S-NAV1 step C: the way home is the main nav's
            pg.click('#closeB'); pg.wait_for_timeout(200)
        # S-NAV1 step C: the drawer on the home holds the main nav alone, Home and the areas (check_nav checks every
        # section's sub-nav, the marks and the drawer's behaviour; the root drawer's top rows and track groups are gone)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        pg.click('#menuB'); pg.wait_for_timeout(250)
        dr = pg.evaluate("[...document.querySelectorAll('#drawer nav.main-nav .ditem .t')].map(t => t.textContent)")
        want_top = ['Home'] + [t['name'] for t in THEMES]
        if dr != want_top: fails.append(f'main nav on the home: {dr}, expected {want_top}')
        if not pg.evaluate("document.querySelector('#drawer nav.sub-nav').hidden"): fails.append('the sub-nav is shown on the home')
        pg.click('#closeB'); pg.wait_for_timeout(200)
        # a course drawer is an accordion: opening a second unit closes the first (S-DEC4: a history course's drawer, its
        # units keyed by the course's unit_key; a markdown course's drawer has no unit groups to fold)
        AC = HIST[0] if HIST else None
        if AC:
            ac, uk = AC['home_id'], AC.get('unit_key', '{id}:{unit}')
            pg.evaluate(f"location.hash = '{ac}'"); pg.wait_for_timeout(50)
            pg.click('#menuB'); pg.wait_for_timeout(250)
            pg.click(f'[data-navctx="{ac}"] .dunit[data-unit="{uk.format(id=AC["id"], unit="1")}"] .duh'); pg.wait_for_timeout(30)
            pg.click(f'[data-navctx="{ac}"] .dunit[data-unit="{uk.format(id=AC["id"], unit="2")}"] .duh'); pg.wait_for_timeout(30)
            op = pg.evaluate(f"[...document.querySelectorAll('[data-navctx=\"{ac}\"] .dunit:not(.closed)')].map(u => u.dataset.unit)")
            if op != [uk.format(id=AC['id'], unit='2')]: fails.append(f'{ac} drawer accordion: open units {op}, expected [{uk.format(id=AC["id"], unit="2")!r}]')
            pg.click('#closeB'); pg.wait_for_timeout(200)
        else: print('nav: no history course in this edition; the course drawer accordion (a history course\'s unit groups) is not tried')
        # the backlog page (S-PAGES): the overall order, then the areas, from docs/site-log.md
        if 'backlog' not in OMIT:
            pg.evaluate("location.hash = 'backlog'"); pg.wait_for_timeout(50)
            step('backlog', dict(id='backlog', nav='none', u=SITE_NAME.upper(), t='Backlog', arrows=False))
            nt = pg.evaluate("document.querySelectorAll('#backlog [data-sl=\"order\"] table.sl').length")
            if nt != 1: fails.append(f'backlog page: {nt} order tables, expected one (S-PAGES; check_site_log checks the rest)')
        # the home lists every live course under its track, in courses.py order (history courses, then markdown courses)
        pg.click('#homeB'); pg.wait_for_timeout(80)
        if MULTI:   # S-NAV1 step B: the home holds one tile per track, in catalog order; each area page its live courses
            ht = pg.evaluate("[...document.querySelectorAll('#home > .cgrid.areas > a.course')].map(a => a.getAttribute('href'))")
            if ht != ['#' + a for a in AREA_IDS]: fails.append(f'home area tiles: {ht}, catalog.toml gives {["#" + a for a in AREA_IDS]}')
            tr = pg.evaluate("[...document.querySelectorAll('.panel[data-kind=\"area\"]')].map(p => p.querySelector('.hero h1').textContent + ':' + [...p.querySelectorAll(':scope > .track > .cgrid > a.course')].map(a => a.getAttribute('href')).join(','))")
        else:
            tr = pg.evaluate("[...document.querySelectorAll('#home .track')].map(t => t.querySelector('h2').textContent + ':' + [...t.querySelectorAll('.cgrid a.course')].map(a => a.getAttribute('href')).join(','))")
        if tr != HOME_TRACKS: fails.append(f'home tracks: {tr}, courses.py gives {HOME_TRACKS}')
        h1 = pg.evaluate("[...document.querySelectorAll('.panel[data-kind=\"course\"] h1, #home h1')].map(h => h.textContent)")
        if any(' in the order' in t or t.startswith('The courses') for t in h1): fails.append(f'course titles not self-evident: {h1}')
        title = pg.title()
        if title != ED['title']: fails.append(f'page title {title!r}, expected {ED["title"]}')
        for label, s in log: print(f'  {label:28} {s["id"]:14} nav={s["nav"]:7} {s["u"]} | {s["t"][:40]} | arrows={s["arrows"]} prev={s["prev"]} next={s["next"]} | {s["cont"][:60]}')
        # S-DEC4: the tablet pass reads the second history course's home and one of its reports, or the first's (its report
        # 5.5) in an edition without a second, or the first markdown course's home and first reading page in an edition
        # without a history course
        rp = rome_reps[3] if len(rome_reps) > 3 else (rome_reps[0] if rome_reps else (SECOND['syl_id'] if SECOND else (rid(LEAD, '5.5') if LEAD else md_read)))
        TAB = SECOND['home_id'] if SECOND else (LEAD['home_id'] if LEAD else (MDSUBS[0][0] if MDSUBS else 'home'))   # P70
        TAB_GRID = f'#{TAB} .part .cgrid' if (SECOND or LEAD) else f'#{TAB} .cgrid'   # a markdown course home has no parts
        DESK = rid(LEAD, '2.3') if LEAD else md_read   # S-DEC4: the desktop pass's report
        if rp is None or DESK is None: fails.append('tablet and desktop: the edition holds no history course with reports ' + ', '.join(SPLIT_MODS) + ' and no markdown course with a unit filed; their report checks have no page to open')   # S-DEC4: fail with a reason, never crash
        ctx.close()

        # ---- tablet: wider column, two-column cards, the drawer still a drawer -----------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'tablet', 768, 1024, True)
        if lay[0] != 768: fails.append(f'tablet layout {lay}: expected width 768')
        check_panels(pg, 'tablet', fails)
        pg.evaluate(f"location.hash = '{TAB}'"); ready(pg); pg.wait_for_timeout(50)
        t = pg.evaluate('''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
          return {off: r.right <= 0, menu: getComputedStyle(document.getElementById('menuB')).display !== 'none',
                  main: document.querySelector('main').getBoundingClientRect().width,
                  cols: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(document.querySelector(''' + json.dumps(TAB_GRID) + ''')).gridTemplateColumns),
                  home: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(document.querySelector(''' + json.dumps(HOME_GRID) + ''')).gridTemplateColumns)}; }''')
        if not t['off']: fails.append('tablet: drawer is on screen before the menu button is pressed')
        if not t['menu']: fails.append('tablet: menu button hidden')
        if not 740 <= t['main'] <= 768: fails.append(f'tablet: main column {t["main"]}px, expected about 760')
        if t['cols'] != 2: fails.append(f'tablet: unit cards in {t["cols"]} column(s), expected 2')
        if t['home'] != 2: fails.append(f'tablet: course cards in {t["home"]} column(s), expected 2')
        pg.click('#menuB'); pg.wait_for_timeout(300)
        d = pg.evaluate('''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
          return {left: r.left, w: r.width, backdrop: getComputedStyle(document.getElementById('backdrop')).opacity}; }''')
        if d['left'] != 0 or not 340 <= d['w'] <= 360: fails.append(f'tablet: open drawer at {d}')
        if float(d['backdrop']) < 0.9: fails.append('tablet: backdrop not shown behind the open drawer')
        pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed'))")
        res = pg.evaluate(BOX_JS, ['#drawer', GAP])
        if res['nbad']: fails.append('tablet drawer: ' + '; '.join(res['bad']))
        small = pg.evaluate(TARGET_JS, '#' + TAB)
        if small: fails.append('tablet drawer targets: ' + '; '.join(small[:6]))
        pg.click('#closeB'); pg.wait_for_timeout(300)
        if not pg.evaluate("document.getElementById('drawer').getBoundingClientRect().right <= 0"): fails.append('tablet: drawer did not close')
        # a report, reached through the shell (P13): the column and measure once the fetch has landed
        if rp:   # S-DEC4: None only in an edition the guard above already fails
            pg.evaluate(f"location.hash = '{rp}'"); ready(pg); pg.wait_for_timeout(50)
            tr = pg.evaluate(f"""() => ({{loaded: document.getElementById('{rp}').hasAttribute('data-loaded'),
              main: document.querySelector('main').getBoundingClientRect().width,
              sw: document.documentElement.scrollWidth - document.documentElement.clientWidth,
              ps: document.querySelectorAll('#{rp} .report p').length}})""")
            if not tr['loaded'] or not tr['ps']: fails.append(f'tablet: report {rp} not loaded through the shell: {tr}')
            if not 740 <= tr['main'] <= 768 or tr['sw'] > 0: fails.append(f'tablet: report {rp} column {tr["main"]}px, horizontal scroll {tr["sw"]}px')
            print('tablet: drawer is a drawer (off screen, 360 px with backdrop when open); column', t['main'], 'px; report', rp, 'loaded through the shell,', tr['ps'], 'paragraphs')
        ctx.close()

        # ---- desktop: persistent sidebar ----------------------------------------------------------------------
        ctx, pg, lay = new_page(p, br, errors, 'desktop', 1280, 800, False)
        if lay[0] != 1280: fails.append(f'desktop layout {lay}: expected width 1280')
        check_panels(pg, 'desktop', fails)
        if DESK:   # S-DEC4: None only in an edition the guard above already fails
            pg.evaluate(f"location.hash = '{DESK}'"); ready(pg); pg.wait_for_timeout(80)
            s = pg.evaluate('''() => { const d = document.getElementById('drawer'), r = d.getBoundingClientRect();
              const main = document.querySelector('main').getBoundingClientRect(), top = document.querySelector('.top').getBoundingClientRect();
              const act = d.querySelector('.sub-nav [data-navctx]:not([hidden]) .ditem.is-active');
              const list = d.querySelector('.dlist');   // S-NAV1 step C: the list holding the main nav and the sub-nav scrolls
              return {left: r.left, w: r.width, h: r.height, vh: innerHeight, hidden: d.getAttribute('aria-hidden'),
                      menu: getComputedStyle(document.getElementById('menuB')).display, close: getComputedStyle(document.getElementById('closeB')).display,
                      backdrop: getComputedStyle(document.getElementById('backdrop')).display,
                      mainLeft: main.left, mainW: main.width, topLeft: top.left, topRight: top.right,
                      active: act ? act.dataset.target : null, listScroll: list ? getComputedStyle(list).overflowY : null,
                      measure: getComputedStyle(document.querySelector('#''' + DESK + ''' .report p')).maxWidth,
                      ch68: (() => { const p = document.querySelector('#''' + DESK + ''' .report p'), t = document.createElement('span');
                        t.style.whiteSpace = 'nowrap'; t.textContent = '0'.repeat(68); p.appendChild(t); const w = t.getBoundingClientRect().width; t.remove(); return w; })(),
                      fonts: ''' + json.dumps(THEME_FONTS) + '''.filter(n => ![...document.fonts].some(f => f.family.replace(/"/g, '') === n && f.status === 'loaded')),
                      home: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(getComputedStyle(document.querySelector(''' + json.dumps(HOME_GRID) + ''')).gridTemplateColumns),
                      ml: (t => { if (t.startsWith('repeat(')) return +t.slice(7, t.indexOf(',')); let d = 0, n = 1; for (const ch of t.trim()) { if (ch === '(') d++; else if (ch === ')') d--; else if (ch === ' ' && !d) n++; } return n; })(document.querySelector(''' + json.dumps('.ml-grid' if MULTI else '#home .ml-grid') + ''') ? getComputedStyle(document.querySelector(''' + json.dumps('.ml-grid' if MULTI else '#home .ml-grid') + ''')).gridTemplateColumns : '')}; }''')
            if s['left'] != 0 or s['w'] != SIDE or s['h'] < s['vh'] - 1: fails.append(f'desktop: sidebar not at the left edge, {SIDE} px, full height: {s}')
            if s['hidden'] != 'false': fails.append(f'desktop: sidebar aria-hidden={s["hidden"]}')
            if s['menu'] != 'none' or s['close'] != 'none': fails.append(f'desktop: menu/close buttons shown ({s["menu"]}, {s["close"]})')
            if s['backdrop'] != 'none': fails.append('desktop: backdrop present')
            if s['mainLeft'] < SIDE: fails.append(f'desktop: content starts at {s["mainLeft"]}px, under the sidebar')
            if not 740 <= s['mainW'] <= 768: fails.append(f'desktop: main column {s["mainW"]}px, expected about 760')
            if s['topLeft'] != SIDE or s['topRight'] != 1280: fails.append(f'desktop: top bar spans {s["topLeft"]}..{s["topRight"]}, expected {SIDE}..1280')
            if s['active'] != DESK: fails.append(f'desktop: sidebar does not highlight the current report ({s["active"]})')
            if s['listScroll'] != 'auto': fails.append(f'desktop: sidebar list overflow-y {s["listScroll"]}, expected auto')
            # P39: the measure is 68ch of the report's own font (DM Sans, about 744 px), and fits the 760 px column; P-DEC5:
            # at least 560 px in DM Sans, and in a brand's --sans 560 px scaled by its "0" against DM Sans' (its ch: Source
            # Sans 3's 68ch is 541 px), from the brand's [metrics] (viz.set_metrics); in DM Sans' metrics exactly 560
            floor = 560 * (viz._ADV['sans'].get('0') or viz._DEFAULT[0]['sans']['0']) / viz._DEFAULT[0]['sans']['0']   # the brand's metrics describe the face its tokens name (courses._brand checks "0" is in the table)
            mw = float(s['measure'].replace('px', '')) if s['measure'].endswith('px') else 0
            if abs(mw - s['ch68']) > 2 or not floor <= mw <= s['mainW']: fails.append(f'desktop: report measure {s["measure"]}, expected 68ch ({s["ch68"]:.0f} px) inside the {s["mainW"]:.0f} px column')
            if s['fonts']: fails.append(f'desktop: theme fonts not loaded from fonts/: {s["fonts"]}')
            if UNSERVED: print(f'desktop: the brand names {UNSERVED}, not in fonts/ (verify.py serves only {VENDORED}); its fallback is drawn and measured, and its loading is not checked')
            if s['home'] != 3 or (HIST and s['ml'] != 2): fails.append(f'desktop: home course cards {s["home"]} col, mythos/logos {s["ml"]} col, expected 3 and 2')   # S-NAV2 step C: three across at 1280 x 800 (1040 px beside the sidebar)
            if not HIST: print('desktop: no history course in this edition; the home\'s mythos/logos block (History\'s) is not measured')
        # the sidebar's own targets and gaps, every unit open
        pg.evaluate("document.querySelectorAll('.dunit').forEach(u => u.classList.remove('closed'))")
        res = pg.evaluate(BOX_JS, ['#drawer', GAP])
        if res['nbad']: fails.append('desktop sidebar: ' + '; '.join(res['bad']))
        sw = pg.evaluate('document.getElementById("drawer").scrollWidth <= document.getElementById("drawer").clientWidth')
        if not sw: fails.append('desktop sidebar: horizontal overflow')
        print(f'desktop: sidebar {s["w"]} px at the left, content column {s["mainW"]} px from {s["mainLeft"]} px, current item {s["active"]}, measure {s["measure"]}')
        ctx.close()
        # S-NAV2 step D: the panel checks on a desktop (1920 x 1080: the top bar, the sidebar where there is a sub-nav, the
        # outline beside a unit); 1024 x 768 and 1280 x 800 keep the drawer's and the 1280 pass's columns, checked above
        ctx, pg, _ = new_page(p, br, errors, 'wide1920', 1920, 1080, False)
        check_panels(pg, 'wide1920', fails)
        ctx.close()

        # P91: the home and What's new at 320, 360 and 430 px (390 is the phone pass above), tablet and desktop, dark and
        # light; P92: on the desktop a history tile, a markdown tile, the IA tile and the hero's What's new link each open
        # their page
        for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS[1:] + NEW_VIEWPORTS:   # S-NAV2 step D: and 1024 x 768, 1920 x 1080
            ctx, pg, _ = new_page(p, br, errors, name, w, h, mobile)
            check_home(pg, name, fails, EXPECT)
            check_new(pg, name, fails, EXPECT)
            pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
            check_home(pg, name + ' light', fails, EXPECT)
            if name == 'desktop':
                hs, ms = [x for x in SAMPLE if x in HIST_HOMES], [x for x in SAMPLE if x not in HIST_HOMES]   # S-DEC4: the sampled courses' tiles: the first history one, the first and last markdown ones
                # S-NAV1 step B: with area pages a course's tile is tapped on its area page, and the home's first area tile too
                taps = [('track-' + AREA_OF[x] if MULTI else 'home', f'a.course.live[data-target="{x}"]') for x in dict.fromkeys(hs[:1] + ms[:1] + ms[-1:])] + [('home', 'a.hnew')]
                if MULTI: taps.insert(0, ('home', f'a.course.live[data-target="{AREA_IDS[0]}"]'))
                for at, sel in taps:   # P92: a tile of each family and the quiet link
                    pg.evaluate(f"location.hash = '{at}'"); ready(pg); pg.wait_for_timeout(60)
                    t = pg.evaluate(f"(() => {{ const a = document.querySelector('#{at} {sel}'); return a && a.getAttribute('data-target'); }})()")
                    if not t:
                        continue
                    pg.click(f'#{at} {sel}'); pg.wait_for_timeout(300); ready(pg); pg.wait_for_timeout(300)
                    land = pg.evaluate(LAND_JS, t)
                    if not land[1] or (land[2] is not None and not (-5 if land[0] == t else 56) <= land[2] <= land[4]) or land[3] is False:   # an id inside a page stops clear of the 56 px bar
                        fails.append(f'{at} desktop: tapping {sel} (#{t}) lands on {land}')
                    else:
                        print(f'{at} desktop: {sel} opens #{t} on {land[0]}, at {land[2]} px' + (', its card open' if land[3] else ''))
            ctx.close()

        # P93: the course homes, What's new and the pages without a topography, at every width, dark and light, under
        # reduced motion: each page's topography and tiles against the sources (check_topo, check_tiles), two history
        # unit tiles opened (their rows, their line whole); the home's tiles too
        TOPO_ALL = [x for x in SAMPLE if x in HIST_HOMES or x in EXPECT['courses']] + AREA_IDS + ['new']   # S-DEC4: course.toml `verify_sample` (every course where the edition holds none); S-NAV1 step B: every area page
        NONE_ALL = [x for x in ('changelog', 'backlog', 'coming', 'viz-examples') if (x != 'viz-examples' or 'figures' not in OMIT) and (x not in ('changelog', 'backlog', 'coming') or x not in OMIT)]   # S-NEXT1: Coming next
        TOPO_PAGES, NONE_PAGES = SCOPE.only(TOPO_ALL), SCOPE.only(NONE_ALL)   # S-DEC4: the run's pages (the shots and the LCP pages below take every sampled one)
        for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS + NEW_VIEWPORTS:   # S-NAV2 step D: and 1024 x 768, 1920 x 1080
            ctx, pg, _ = new_page(p, br, errors, name + ' pages', w, h, mobile)
            reads = pg.evaluate("""() => { const seen = {}, out = []; document.querySelectorAll('.panel[data-kind="report"]').forEach(p => { const c = p.getAttribute('data-ctx'); if (!seen[c]) { seen[c] = 1; out.push(p.id); } }); return out; }""")
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                pg.evaluate("location.hash = 'home'"); ready(pg); pg.wait_for_timeout(120)
                pg.evaluate(f"document.querySelectorAll({PLANNED_SEL!r}).forEach(d => d.open = true)"); pg.wait_for_timeout(60)
                check_topo(pg, 'home', f'{name} {theme}', fails, EXPECT); check_tiles(pg, 'home', f'{name} {theme}', fails, EXPECT)
                pg.evaluate(f"document.querySelectorAll({PLANNED_SEL!r}).forEach(d => d.open = false)")
                for pid in TOPO_PAGES + NONE_PAGES + SCOPE.only(reads):
                    pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(120)
                    if pid in AREA_IDS:   # S-NAV1 step B: an area page whole (check_area), its planned courses opened for the tile checks
                        check_area(pg, pid, f'{name} {theme}', fails, EXPECT)
                        pg.evaluate(f"document.querySelectorAll({PLANNED_SEL!r}).forEach(d => d.open = true)"); pg.wait_for_timeout(60)
                    t = check_topo(pg, pid, f'{name} {theme}', fails, EXPECT)
                    if pid in TOPO_PAGES and pid != 'new':
                        pg.evaluate(f"document.querySelectorAll('#{pid} details[data-mods]').forEach((d, k) => d.open = k < 2)"); pg.wait_for_timeout(60)
                        tl = check_tiles(pg, pid, f'{name} {theme}', fails, EXPECT)
                        pg.evaluate(f"document.querySelectorAll('#{pid} details[data-mods]').forEach(d => d.open = false)")
                        if pid in AREA_IDS: pg.evaluate(f"document.querySelectorAll({PLANNED_SEL!r}).forEach(d => d.open = false)")
                        if theme == 'dark': print(f"{pid} {name}: layer {t['hero'] and t['hero']['bytes']} B, layout {t['hero'] and t['hero']['shown']}, frame {t['hero'] and t['hero'].get('frame')}; {len(tl['tiles'])} tiles, {len(t['patches'])} patches, grids {tl['grids'][:2]}")
                    elif pid == 'new' and theme == 'dark':
                        print(f"new {name}: layer {t['hero'] and t['hero']['bytes']} B, layout {t['hero'] and t['hero']['shown']}, frame {t['hero'] and t['hero'].get('frame')}, days {[(l, k) for l, _, k, _, _ in t['hero']['layouts'][0][1]] if t['hero'] else None}")
            ctx.close()

        # P92: with motion allowed, at every width, dark and light: only transform and opacity animate, the cycling area
        # line shows and the static line is for a screen reader only; the hero's texts over the contours; and at 390 px
        # the weight of a fresh load (LCP and the longest task, from the browser's performance entries). P93: on every
        # page: every contour drawing moves (the hero's layer and every tile's patch, transform only, each at its own
        # point of the cycle; nothing else on a page without one; S-NAV1 step D: every line swells), and at the five poses of the swell every layer covers
        # its frame, every rise and patch stays inside it, and every text over a topography keeps its contrast; LCP and
        # the longest task on the home, a course home and What's new
        def perf_of(pg, pid):
            pg.evaluate(f"localStorage.clear(); location.hash = '{pid}'")
            pg.evaluate('''() => { window.__p92 = {lcp: 0, lt: 0, n: 0}; }''')
            pg.reload(); pg.wait_for_timeout(100)
            pg.evaluate('''() => { window.__p92 = {lcp: 0, lt: 0, n: 0};
              new PerformanceObserver(l => l.getEntries().forEach(e => { window.__p92.lcp = Math.max(window.__p92.lcp, e.startTime); })).observe({type: 'largest-contentful-paint', buffered: true});
              new PerformanceObserver(l => l.getEntries().forEach(e => { window.__p92.lt = Math.max(window.__p92.lt, e.duration); window.__p92.n++; })).observe({type: 'longtask', buffered: true}); }''')
            pg.wait_for_timeout(3000)
            return pg.evaluate('window.__p92')
        PERF = {}
        for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS:   # P92 check: every width, not two
            ctx, pg, _ = new_page(p, br, errors, name + ' motion', w, h, mobile, motion=True)
            if name == 'phone':
                PERF_PAGES = ['home'] + TOPO_ALL[:1] + ['new']   # S-DEC4: a course home the edition holds (Greece in Academy), never one it lacks
                if len(PERF_PAGES) < 3 or TOPO_ALL[0] == 'new': fails.append('phone motion: the edition holds no course home to measure LCP and the longest task on')
                for pid in [x for x in dict.fromkeys(PERF_PAGES)]:
                    if not pg.evaluate(f"!!document.getElementById('{pid}')"): fails.append(f'phone motion: #{pid} is not in the edition; nothing measured on it'); continue
                    PERF[pid] = perf_of(pg, pid)
                    print(f"{pid} phone motion: LCP {PERF[pid]['lcp']:.0f} ms, longest task {PERF[pid]['lt']:.0f} ms ({PERF[pid]['n']} long tasks over 50 ms), on a fresh load from the local server")
                pg.evaluate("location.hash = 'home'"); ready(pg)
                # P93 follow-up (Pedro, 4 Nov 2026, 20:16: "The animations dont work, at least on mobile"): at 120 s a sweep the
                # move ran, at 0.6 px/s at most, and read as still. The move must be seen and still be slow. S-NAV1 step D: the
                # peak speed of the furthest-moving point of a line in the home's frame at 390 px (its distance from its core
                # times its d times --topo-grow, over --topo-breath; CSS ease-in-out peaks at 1.6 times the average), between 2
                # and 12 px/s; and an outer line must have moved between two reads 2 s apart
                amp, fw, fh = pg.evaluate(SWELL_AMP_JS, '#home .hhome > .topo')
                v = 1.6 * amp / (BTIME / 1000)
                sel = "[...document.querySelectorAll('#home .hhome > .topo .topo-tall path')].find(p => +getComputedStyle(p).getPropertyValue('--d') === 1)"
                m0 = pg.evaluate(f"getComputedStyle({sel}).transform"); pg.wait_for_timeout(2000)
                m1 = pg.evaluate(f"getComputedStyle({sel}).transform")
                print(f"home phone motion: the swell peaks at {v:.1f} px/s at its furthest-moving point in the frame ({fw} x {fh} px frame, {amp:.1f} px each way, the outermost lines to {1 + GROW:g} over {BTIME / 1000:g} s); an outer line moved in 2 s: {m0 != m1}")
                if not 2 <= v <= 12: fails.append(f"home phone motion: the swell peaks at {v:.1f} px/s, outside 2 to 12 px/s (seen, and still slow; Pedro, 5 Nov 2026: \"it could be faster\")")
                if m0 == m1: fails.append('home phone motion: the outer lines did not move in 2 s')
            for theme in ('dark', 'light'):
                if theme == 'light': pg.evaluate(f"localStorage.setItem('{THEME_KEY}', 'light'); document.documentElement.setAttribute('data-theme', 'light')")
                pg.evaluate("location.hash = 'new'"); ready(pg); pg.evaluate("location.hash = 'home'"); ready(pg); pg.wait_for_timeout(200)   # the home shown afresh, each drawing at its own phase, before any pose
                check_topo(pg, 'home', f'{name} motion {theme}', fails, EXPECT, motion=True)
                check_home(pg, name + (' motion' if theme == 'dark' else ' motion light'), fails, EXPECT, motion=True)
                if theme == 'dark': check_harea(pg, name + ' motion', fails)   # S-NAV2 step A: one area word at a time, at every viewport
                for p_ in POSES:
                    pose(pg, p_, 1500)
                    check_topo(pg, 'home', f'{name} motion {theme} pose {p_:g}', fails, EXPECT, motion=True, phase=False)
                pg.evaluate("() => document.getAnimations().forEach(a => a.play())")
                for pid in TOPO_PAGES + NONE_PAGES:
                    pg.evaluate(f"location.hash = '{pid}'"); ready(pg); pg.wait_for_timeout(250)
                    check_topo(pg, pid, f'{name} motion {theme}', fails, EXPECT, motion=True)
                    if pid in TOPO_PAGES:
                        lows = []
                        for p_ in POSES:
                            pose(pg, p_)
                            check_topo(pg, pid, f'{name} motion {theme} pose {p_:g}', fails, EXPECT, motion=True, phase=False)
                            lows.append(texts_contrast(pg, pid, f'{name} motion {theme}', fails, f' pose {p_:g}'))
                        pg.evaluate("() => document.getAnimations().forEach(a => a.play())")
            ctx.close()
        # S-NAV2 step D: at 1024 x 768 and 1920 x 1080 the home with motion allowed (its layer, its texts, the area line's
        # cycle); the course and area pages' poses stay at the widths above
        for name, w, h, mobile in NEW_VIEWPORTS:
            ctx, pg, _ = new_page(p, br, errors, name + ' motion', w, h, mobile, motion=True)
            pg.evaluate("location.hash = 'new'"); ready(pg); pg.evaluate("location.hash = 'home'"); ready(pg); pg.wait_for_timeout(200)
            check_topo(pg, 'home', f'{name} motion', fails, EXPECT, motion=True)
            check_home(pg, name + ' motion', fails, EXPECT, motion=True)
            check_harea(pg, name + ' motion', fails)
            ctx.close()

        if SHOTS:
            SHOTS.mkdir(parents=True, exist_ok=True)
            for name, w, h, mobile in HOME_WIDTHS + VIEWPORTS:   # P91: the home and What's new at 320, 360 and 430 px too
                ctx, pg, _ = new_page(p, br, [], name, w, h, mobile)
                for theme in ('dark', 'light'):
                    pg.evaluate(f"localStorage.setItem('{THEME_KEY}', '{theme}')")
                    COURSE_SHOTS = ['home', 'new'] + TOPO_ALL[:-1]   # P93: the home, What's new and every course home at every width
                    for pid in ((COURSE_SHOTS + [x for x in PAGES if x not in COURSE_SHOTS]) if name.startswith('phone3') or name == 'phone430' else COURSE_SHOTS + [x for x in [TAB, rp] + PAGES if x not in COURSE_SHOTS]):
                        pg.evaluate(f"localStorage.removeItem('pm-sec-{pid}')")   # P68: each shot opens on section 1
                        if pid == 'home':   # P90: the home is shot as a fresh visit (P91: nothing on it depends on the visit, but the shot stays clean)
                            pg.evaluate(f"localStorage.clear(); localStorage.setItem('{THEME_KEY}', '{theme}')")
                        pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(250); pg.evaluate('window.scrollTo(0, 0)'); pg.wait_for_timeout(50)
                        if pid == 'home':   # P90: the home whole, to New since and the changelog link at its foot (it is a few screens long)
                            pg.screenshot(path=str(SHOTS / f'{name}-{pid}-{theme}.png'), full_page=True, timeout=120000)
                        else:
                            shoot(pg, SHOTS / f'{name}-{pid}-{theme}.png', w, h)
                        if pid in PAGES and pg.query_selector(f'[id="{pid}"] .report.steps'):   # P68: the reading states the top does not show
                            for state, js in READING_SHOTS:
                                pg.evaluate(js, pid); pg.wait_for_timeout(200)
                                pg.screenshot(path=str(SHOTS / f'{name}-{pid}-{state}-{theme}.png'))
                            pg.evaluate("(pid) => { const p = document.getElementById(pid); p.querySelectorAll('details').forEach(d => d.open = false); const w = p.querySelector('.stepbar .whole'); if (w.getAttribute('aria-pressed') === 'true') w.click(); [...p.querySelectorAll('.seclist a')][0].click(); window.scrollTo(0, 0); }", pid)
                        if pid in PAGES:   # P41: each figure of a --page panel, as the reader sees it in its frame (P91: the home has no figure; P92: its contours are not figures, and are in the home shot and the motion sheets)
                            for k, fig in enumerate(pg.query_selector_all(f'[id="{pid}"] figure.viz')):
                                kind = ([c for c in fig.get_attribute('class').split() if c.startswith('viz-') and c != 'viz-wide'] or ['viz-figure'])[0][4:]
                                fig.evaluate("f => { const s = f.closest('.sec'), p = f.closest('.panel'); if (s && !s.classList.contains('on')) p.querySelector('.seclist a[data-step=\"' + s.dataset.step + '\"]').click(); }")   # P68: its section shown first
                                fig.scroll_into_view_if_needed(); pg.wait_for_timeout(30)
                                fig.screenshot(path=str(SHOTS / f'{name}-{pid}-fig-{k + 1:02d}-{kind}-{theme}.png'), timeout=120000)
                                nf = frames(pg, fig, SHOTS / f'{name}-{pid}-fig-{k + 1:02d}-{kind}-frames-{theme}.png', f'{name} · {pid} · figure {k + 1} · {theme}')   # P89
                                print(f'shots: {name} {pid} figure {k + 1} ({kind}) {theme}: {nf} frame' + ('s' if nf != 1 else ''))
                            pg.evaluate('window.scrollTo(0, 0)')
                ctx.close()
            # P92: the hero at five moments; P93: at the five poses of the slow move (POSES: since S-NAV1 step D the
            # swell at rest, at its top, its quarters and its middle; the home's area line at 0, 3, 6, 9 and 12 s of its n x 3 s cycle, n its words (S-NAV2 Fix 1: 18 s with six areas,
            # so words 1 to 5 are posed and the sixth is not; check_harea samples every word), at 390 and 1280 px
            # with motion allowed, dark and light, for the home, a history course home (Greece) and a markdown course
            # home (Information architecture): every animation paused and set to the pose, the hero shot, the five
            # stacked with their times in one sheet (<width>-<page>-motion-<theme>.png)
            from PIL import Image, ImageDraw, ImageFont
            for name, w, h, mobile in (('phone', 390, 844, True), ('desktop', 1280, 800, False)):
                ctx, pg, _ = new_page(p, br, [], name, w, h, mobile, motion=True)
                for pid in ['home'] + list(dict.fromkeys([x for x in TOPO_ALL[:-1] if x in HIST_HOMES][:1] + [x for x in TOPO_ALL[:-1] if x not in HIST_HOMES][-1:])):   # S-DEC4: a history course home and the last sampled markdown one
                    sel = '#home .hhome > .topo' if pid == 'home' else f'#{pid} > header.hero > .topo'   # the layer's own frame: from the top bar to the hero's foot, the full width beside the sidebar (the hero's box is the column), the texts on it
                    for theme in ('dark', 'light'):
                        pg.evaluate(f"localStorage.clear(); localStorage.setItem('{THEME_KEY}', '{theme}')"); pg.goto(URL + '#' + pid); pg.reload(); ready(pg); pg.wait_for_timeout(500)
                        ims, tags = [], []
                        for k, p_ in enumerate(POSES):
                            pose(pg, p_, k * 3000); pg.wait_for_timeout(60)
                            tmp = SHOTS / f'_{name}-{pid}-{k}.png'
                            pg.locator(sel).screenshot(path=str(tmp), animations='allow')
                            ims.append(Image.open(tmp)); tmp.unlink()
                            tags.append(f'{name} · {pid} · {theme} · pose {k + 1} of 5: {p_:g} of the swell ({p_ * BTIME / 1000:.1f} s of {BTIME / 1000:.0f} s: the outermost lines at {1 + GROW * eased(p_):.3f}, the innermost still)' + (f'; area line at {k * 3:.0f} s of its {3 * len(THEMES)} s cycle, word {k % len(THEMES) + 1} of {len(THEMES)}' if pid == 'home' else ''))
                        sc = max(1, round(ims[0].width / pg.evaluate(f"document.querySelector('{sel}').getBoundingClientRect().width")))
                        font, band = ImageFont.load_default(size=12 * sc), 26 * sc
                        sheet = Image.new('RGB', (ims[0].width, sum(i.height + band for i in ims)), (128, 128, 128))
                        d, y = ImageDraw.Draw(sheet), 0
                        for im, tg in zip(ims, tags):
                            d.text((6 * sc, y + 6 * sc), tg, fill=(0, 0, 0), font=font); y += band; sheet.paste(im, (0, y)); y += im.height
                        sheet.save(SHOTS / f'{name}-{pid}-motion-{theme}.png')
                        print(f'shots: {name} {pid} motion sheet, {theme}')
                ctx.close()
            # V1: each figure of the examples page as the reader sees it in its frame, then one sheet per width and theme
            for name, w, h, mobile in (VIEWPORTS if 'figures' not in OMIT else []):
                ctx, pg, _ = new_page(p, br, [], name, w, h, mobile)
                for theme in ('dark', 'light'):
                    pg.evaluate(f"localStorage.setItem('{THEME_KEY}', '{theme}')")
                    pg.goto(URL + '#viz-examples'); pg.reload(); ready(pg); pg.wait_for_timeout(250)
                    shots = []
                    for k, fig in enumerate(pg.query_selector_all('#viz-examples figure.viz')):
                        kind = [c for c in fig.get_attribute('class').split() if c.startswith('viz-') and c != 'viz-wide'][0][4:]
                        fig.scroll_into_view_if_needed(); pg.wait_for_timeout(30)
                        path = SHOTS / f'{name}-viz-{k + 1:02d}-{kind}-{theme}.png'
                        fig.screenshot(path=str(path)); shots.append(path)
                    try:
                        from PIL import Image
                        ims = [Image.open(x) for x in shots]
                        sheet = Image.new('RGB', (max(i.width for i in ims), sum(i.height for i in ims) + 12 * len(ims)), (10, 10, 12) if theme == 'dark' else (232, 228, 220))   # the page colour of each theme (P90: the light paper)
                        yy = 0
                        for im in ims:
                            sheet.paste(im, (0, yy)); yy += im.height + 12
                        sheet.save(SHOTS / f'{name}-viz-examples-{theme}.png')
                    except ImportError:
                        pass
                ctx.close()
            layout_shots(br, SHOTS)   # S-NAV2 step E: the row's three shot layouts
            print('screenshots in', SHOTS)
        br.close()
    errs = [e for e in errors if 'fonts.g' not in e]
    if errs: fails.append('console errors: ' + ' | '.join(errs[:5]))
    ix = index_check.check()   # A5: docs/courses-index.md against the sources it summarises
    fails += ['courses-index.md: ' + x for x in ix]
    print('courses-index.md: ' + (f'{len(ix)} mismatches' if ix else 'matches the sources'))
    # G-0 (11 Nov 2026): no private term in a public course's vault, data folder or built pages. S-DEC4: the default
    # edition (Academy) as before, its public courses (private_terms.py with no argument); another edition over its own
    # built files (private_terms.py --edition; a `dated_lists` course's pages as academy's, P-DEC10). An edition holding
    # only courses marked `private` in their course.toml (the owner's own courses, which name him) is left out and said
    # so; a mixed edition (P-DEC13) is checked over every file but the private courses' folders, which it names
    if EDITION == DEFAULT_EDITION:
        pt = private_terms.check()
        fails += ['private term in a public course: ' + x for x in pt]
        print('private terms in the public courses: ' + (f'{len(pt)} found' if pt else 'none'))
    elif PRIVATE and len(PRIVATE) == len(COURSES):
        print(f'private terms: edition {EDITION} holds a private course ({", ".join(PRIVATE)}), which names its owner; its files are not checked (the public courses are, in the default edition)')
    else:
        fs = private_terms.text_only(private_terms.edition_files(EDITION, skip=PRIVATE))
        pt = private_terms.scan(fs)[0]
        fails += ['private term in the edition: ' + x for x in pt]
        if PRIVATE:
            print(f'private terms: edition {EDITION} holds a private course ({", ".join(PRIVATE)}), which names its owner; its pages are not checked ('
                  + ', '.join(d + '/' for c in COURSES if c['id'] in PRIVATE for d in private_terms.folders(c)) + '), every other file of the edition is')
        print(f'private terms in edition {EDITION}: {len(fs)} files, ' + (f'{len(pt)} found' if pt else 'none'))
    rf, rw = rot_check.check()   # P30-F11, P30-F16 (17 Nov 2026)
    fails += ['rot: ' + x for x in rf]
    print('rot check: ' + (f'{len(rf)} failures' if rf else 'none') + ''.join('\n  warn ' + x for x in rw))
    if fails: print(f'{SCOPE.mode}\nverify-hashes.json: not written (a failed run marks no page as checked)')
    else:   # S-DEC4: only a passed run records the pages' sources as checked
        SCOPE.save(); print(f'{SCOPE.mode}\nverify-hashes.json: edition {EDITION} recorded, {len(SCOPE.pages_now)} pages')
    print('\n'.join('FAIL ' + f for f in fails) if fails else 'ALL CHECKS PASSED')
    return 1 if fails else 0

if __name__ == '__main__':
    sys.exit(main())
