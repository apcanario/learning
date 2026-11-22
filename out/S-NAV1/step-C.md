# S-NAV1 · Step C · navigation

Model: Opus 5.5 (claude-opus-5-5), a fresh agent. 21 to 22 Nov 2026.

## Verdict

Done. The navigation is two levels, each one element with stable classes: `nav.main-nav` (Home and the areas, catalog
order) and `nav.sub-nav` (the reader's section: an area's courses on its page, a course's pages and units inside a
course, nothing on the home or the site pages under it). What's new, the Backlog and the Changelog are only at the
home's foot. Every panel and every fetched page is byte-identical to the build before the step; only the drawer, the
CSS and the JS changed. The phone drawer works as before (menu, close, Escape, focus, backdrop, scroll lock, current
item scrolled into view, history from Step A, dark and light, reduced motion). No commit, no push, no land.py,
`kit/baseline.json` and `kit/verify-hashes.json` untouched. No unit, brief, vault or course file changed.

## What changed

**kit/build.py**
- `drawer(c)` (a history course's group): it is now `div.sub-sec[data-navctx=<course id>][data-accordion][role=group]`,
  not a `nav.dlist`. Its "← Academy" row is gone: the main nav holds Home. The rest is unchanged (course home,
  Syllabus and prompts, How it was built, then the unit accordion).
- The root nav (`root_nav_track`, `root_nav`) is replaced by:
  - `main_nav`: `nav.main-nav[aria-label=Main]`, holding `a.ditem.dhome` Home, then one `a.ditem.darea` per track (■ in the
    track's tone, its name, `href="#track-<id>"`). Each area entry has `data-secs`, the course sections it holds, so
    shell.js can mark the area the reader is in.
  - `area_courses(t)`: one `div.sub-sec[data-navctx=track-<id>]` per track (MULTI only). It lists the track's courses as
    the old root group did (history courses, then markdown sub-courses, each `a.ditem.dcourse` with its counts) and
    History's folded planned list (`planned_drawer`), inside `.ditems`. The old "the area's home" row is gone: that is
    the main nav's area entry now.
  - `sub_nav`: `nav.sub-nav[aria-label="In this section"][hidden]`, holding the area groups, then every course group.
  - Both navs sit in `div.dlist`, the drawer's existing scroll list, main first. The drawer, its head, the backdrop,
    the top bar and `<main>` are unchanged.
- The home is unchanged. Its foot already held the links to the Backlog, Figure kinds and the Changelog (above New
  since) and to What's new (last). With the drawer's top rows gone, those are the only links to them.

**kit/mdcourse.py** (the markdown course's group, built for the shell): the same change as `drawer(c)`:
`div.sub-sec[data-navctx=<ctx>][role=group]`, no "← Academy" row. Nothing else in the module changed.

**kit/shell.js** (nav behaviour only)
- `navs` are the sub-nav's groups. `secOf(id)` gives the section of a page: a course's ctx, an area page's own id, or
  none (the home, What's new, the Changelog, the Backlog, Figure kinds).
- `show()` shows that section's group and hides the sub-nav when there is none. The main nav marks where the reader
  is: Home on the home and the site pages under it, an area on its page (`aria-current="page"`) and on every page of its
  courses (`is-active`, `aria-current="true"`). The existing exact-match marking of every `.ditem` is kept.
- `openDrawer()` scrolls the sub-nav's current item into view, or the main nav's when there is none. It still focuses
  the close button.
- The root track groups' start-up code is removed (closed by default, the last read track opened); there are no root
  groups now. Two comments were updated.
- History, routing, `go()`, popstate and hashchange are untouched. Menu, close, backdrop, Escape and the 1100 px
  sidebar sync are untouched.

**design/theme.css → kit/shell.css** (identical; `cmp` clean)
- Version 6.17 line in the header.
- The drawer comment names the two levels.
- `.dtop` becomes `.dtop,.main-nav`, so the main nav is ruled off from the sub-nav as the old top rows were. No other
  rule changed. The existing classes (`.dlist`, `.ditem`, `.dhome`, `.dcourse`, `.ditems`, `.dplan`, `.dunit`) style
  everything, so the phone looks as before apart from the structure.

**kit/verify.py**
- New `check_nav(br, fails, w, h, theme, motion)` with `NAV_JS`, `NAV_FOOT_JS`, `NAV_DRAWER_JS` and `nav_expect()`.
  It checks:
  - `nav.main-nav` and `nav.sub-nav` exist once each, in the drawer's list, main first, in no panel.
  - The main nav is exactly Home and the tracks in catalog order, and it marks the reader's place with the right
    `aria-current`.
  - The sub-nav is hidden on the home and its site pages. On an area page it shows that area's courses (courses.py's
    history courses, then markdown sub-courses). On a course's home, syllabus and first reading page it shows that
    course's group, the course home first and the page marked.
  - What's new, the Changelog and the Backlog are linked at the home's foot, after its courses (null where the edition
    omits them), and in neither nav.
  - Below 1100 px: the menu opens the drawer with both navs on screen, the focus on close and the current item in view;
    Escape closes it and returns the focus; tapping the main nav's area closes the drawer and opens the area; back
    returns.
  - From 1100 px both navs are in the sidebar.
  - No console or page error.
  `main()` runs it at 390 px dark, 390 px light and 1280 px.
- Navigation walk: the `nav` state is the shown sub-nav group or `none`. Home, the Changelog and the Backlog expect
  `none`; an area expects its own id. The course group selectors read `.sub-nav [data-navctx=…]`.
- The course drawer-top checks no longer expect the site row first.
- The root drawer block (top rows Home/What's new/Changelog/Backlog, collapsible track groups) is replaced by: the
  drawer on the home shows the main nav, Home and the track names, and the sub-nav is hidden.
- The drawer box pass covers `AREA_IDS` too, in full and scoped runs.
- Desktop: the scroll list is `.dlist`, and the highlighted item is read in the sub-nav.
- Light contrast: every sub-nav group is shown at once before the drawer is measured.
- Docstring: a "Navigation (S-NAV1 step C)" paragraph; the root drawer lines updated.

**kit/verify_scope.py**: docstring paragraph. The navigation sits outside every panel, so it reaches no page's hash;
its checks are edition-wide and run in every run. A page's `data-ctx` names its sub-nav group. The `self.ctx` comment
is updated. No logic changed.

## Choices (taken, recorded)

- **Where the navs live.** Both are direct children of the drawer's existing scroll list (`div.dlist`), not new
  wrappers. The phone keeps one scrolling list and its look. S-NAV2 can lift them out with CSS alone, for example
  `.dlist{display:contents}` and placing `.main-nav` in a top bar and `.sub-nav` in a sidebar. Each nav is one element
  with no layout rule of its own beyond the `.dtop` rule it shares.
- **One sub-nav, groups inside.** "Once per page" is read as once in the document: one `nav.sub-nav` holding every
  section's group (`div.sub-sec[data-navctx]`), with the reader's group shown. The site is one shell, so a sub-nav per
  section would put many `nav.sub-nav` elements in the page. `data-navctx` is kept on the groups so the scoped verify
  and shell.js keep their keys.
- **Single-track edition (greece).** There is no area page, so the main nav is Home and History. History links to
  `#track-history`, the track's band on the home (the home is the area in that edition), and route() opens the home
  there. It is marked on every Greece page. Greece has no area group in the sub-nav. The alternative, linking History
  to the edition's one course home, would break if a single-track edition held two courses.
- **Site pages under the home.** What's new, the Changelog, the Backlog and Figure kinds have no sub-nav, and the main
  nav marks Home on them (`aria-current="true"`).
- **The home's foot.** No markup change. The home already ends with the rules, the site links (Backlog, Figure kinds,
  Changelog), New since and the What's new link. These follow the area tiles, and they are now the only links to those
  pages besides the hero's quiet What's new link and the pages' own cross-links. Leaving the markup alone keeps the
  home byte-identical and its checks as they are.
- **Dropped rows.** "← Academy" heads no course group, and "the area's home" heads no area list. The main nav carries
  both.
- **Labels.** Main nav `aria-label="Main"`; sub-nav `aria-label="In this section"`; each group `role="group"` with
  its course's or area's name.
- **Course groups unchanged.** The course groups keep their accordion and their remembered open state (localStorage
  key as before). The root track groups' remembered state is no longer read; old keys in a reader's storage are inert.

## Tests

- `python3 kit/baseline.py --check` was clean before the change. After it, 3 differ, 0 added, 0 removed: academy
  `README.md` and `academy/index.html`, greece `editions/greece/index.html`. All three are in `expected-C.txt`.
- **Byte comparison with the build before the step.** The base commit 896d541 was built in a temporary git worktree,
  since removed; academy, greece and marketing-ai were built there.
  - In each edition only `index.html` differs.
  - Its `<main>` (every panel) and its top bar are byte-identical.
  - Stripped of the drawer, `<style>`, `<script>`, `<nav>` and `<svg>`, it is byte-identical.
  - Every fetched page (reading pages, course homes, syllabi, briefs) is byte-identical.
  - Shell: 592 KB, down to 590 KB.
- **`check_nav`.** Harness `/tmp/snav1c/scripts/nav.py`, importing verify.py, never recording. It runs at 320×640,
  390×844, 768×1024 and 1280×800, each in dark and light with reduced motion, and in dark with motion allowed. Then
  `check_history` runs, then the drawer box and overflow checks (BOX_JS, 6 px) on the home, every area page and every
  course home, at 390, 768 and 1280 px, dark and light.
  - academy: 31 pages per run, NAV CHECKS PASSED, no console error. History walk home → track-history → greece → m01,
    three backs and forward, pushState-refused fallback and sandboxed iframe pass.
  - greece: 5 pages, NAV CHECKS PASSED, no console error. Main nav Home · History; the area entry opens the home at
    #track-history.
  - marketing-ai: 9 pages, NAV CHECKS PASSED, no console error. History walk through track-marketing passes.
- **verify.py `main()` with the per-page heavy passes stubbed.** Harness `/tmp/snav1c/scripts/navonly.py`, as step B's.
  It runs: the navigation walk, the three `check_nav` runs, the drawers per section, the main nav on the home, light
  contrast with every sub-nav group shown, and the tablet, desktop and home-tracks checks.
  - marketing-ai: ALL CHECKS PASSED (the record write was stubbed; `git status` shows `kit/verify-hashes.json`
    unchanged).
  - academy and greece: one fail each, "desktop: theme fonts not loaded from fonts/: ['Gentium Book Plus']". This is
    the stub artifact step B recorded: the real `check_panels` opens the details that use that face before the desktop
    font check. No other fail.
  - Light contrast lows: academy 4.29:1, greece 4.3:1 (span.bn, a report's band numeral, large text), marketing-ai
    4.93:1. No text failed.
- **Screens.** Old and new drawers at 390 px, dark and light, on the home, track-history and m23, set side by side
  (`/tmp/snav1c/shots/cmp-390-*.png`). The new drawer uses the same rows, type and rules. Home shows Home and the six
  areas only. The area page shows the main nav, then History's courses and planned row. A unit shows the course group,
  scrolled to the current item, with the main nav above it.
- `kit/index_check.py`: courses-index.md matches the sources. `kit/private_terms.py`: 0 private terms, OK.
- Not run: `verify.py --full` (as instructed).

## For the row's close (outside this step's files)

These docs describe the old drawer and are left for the close:
- design/README.md, section 3 row (`.dlist` "one nav per context"; the drawer's classes).
- The verify docstring's general lines on the drawer at the three widths, which still hold.
- Any kit/README.md or docs/method.md text naming the root drawer's What's new, Changelog and Backlog rows.

`kit/README.md` changed only by the build's size table.

## Blockers

None. No permission check refused a script. The temporary worktree (`git worktree add --detach /tmp/snav1c/old HEAD`)
was removed and pruned; `git worktree list` shows only the clone.
