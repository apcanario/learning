# generator/

Builds every hub page in the Learning Project from content plus `design/theme.css`. Pages are self-contained HTML (theme and script inlined) because a published artifact cannot load an external stylesheet.

| File | What it does |
|---|---|
| `build_hub.py` | Renders a course hub from a data folder: `python3 build_hub.py data/brand-ai` → `hubs/brand-and-ai-courses.html`. Reads `../design/theme.css` and `hub.js` and inlines both. Needs `pip install markdown` for reading pages. |
| `hub.js` | The hub's behaviour, modelled on Personal Mythology's `shell.js`: hash-routed panels, slide-out drawer, top-bar context, theme toggle (remembered per browser, follows the system when unset), copy buttons, and the hub's back navigation (back button with a page history, swipe from the left edge). |
| `data/brand-ai/` | The Brand + AI hub's content. `hub.py` holds every page's text (v5.1's text re-marked with theme classes, plus the v6 notes and changelog line); `units_data.py` (the preamble and the 21 units with their briefs) and `audience-growth-across-platforms.md` (the written material for A2, A6, A9) are byte-for-byte the files in the v5.1 archive. |
| `data/_template/` | A blank hub: one course, three placeholder units, the two audit prompts. Copied by the `new-course` skill. It builds as is. |
| `build_history.py` | Rebuilds the Personal Mythology site on the theme: `python3 build_history.py <kit folder>` copies the kit to a temporary folder, puts `theme.css` in place of `shell.css`, runs the kit's own `build.py` unchanged and writes `hubs/personal-mythology.html`. The kit is not modified. |
| `check_page.py` | Checks a built page at 400 px in dark and light: horizontal overflow and targets under 44 px on every panel, every `<details>` open. Needs Playwright with Chromium. |
| `hubs/` | The built pages, ready to republish: `brand-and-ai-courses.html` (Brand + AI, v6) and `personal-mythology.html` (the history site on the theme). |

## Theme changes reach a page only on rebuild

Editing `design/theme.css` changes nothing that is already published. After any edit: run `build_hub.py` for each data folder and `build_history.py` for the kit, check with `check_page.py`, then republish each page to its existing artifact (`SETUP.md`, "After a theme change"). That is the only propagation path.

## What changed from the v5.1 generator

- **No CSS of its own.** v5.1 carried `css_base.txt` plus about forty lines of hub CSS in the script. Both are gone; the page uses the history site's components (top bar, drawer, `.hero`, `.howto`, `.smod` with `.pbox` prompt boxes, `.hrow`, `.course`, `.pill`, `.report`, `.tbl`). The handful the hub needed and the history site lacked are in `theme.css` section 5.
- **Information architecture unchanged.** Learn (overview, course A, course B, the reading page) and Build (how we build, build order, briefs A and B, audits, bibliography, hub template, changelog), in the same order, with the same text, every brief and both audit prompts byte-identical to v5.1 (checked by extracting all 23 `<pre>` blocks from both pages). The hub's back button and edge swipe, the theme toggle and its `hub-theme` storage key are kept.
- **Layout follows the template.** The drawer slides out at every width; v5.1's persistent desktop sidebar is retired. The top bar is the history bar: menu, back, current page, home, theme.
- **Viewport tag.** v5.1 had none, so phones laid it out 980 px wide.
- **Portable paths.** v5.1 read `css_v4.txt`, `units_data.py` and the research report from absolute scratch paths of the session that made it (and `css_v4.txt` was shipped as `css_base.txt`). Everything is now relative to this folder.
- **Content separated from structure.** v5.1 kept every page's text inside the script. Text now lives in `data/<hub>/hub.py`, so a new hub is a new data folder, not a new script.

## Adding a hub

Use the `new-course` skill, or by hand: copy `data/_template/` to `data/<slug>/`, replace every `⟨…⟩`, run `python3 build_hub.py data/<slug>`, check it, publish it once as a new artifact, and add the link to `courses-index.md`.

## Pages not built here

The two standalone syllabus pages of the history course (Hellas Syllabus, Roma Syllabus) and the standalone Audience Growth research page still carry their own dark-only CSS. Their content is also in the two hubs (the syllabi inside the history site, the research as the Brand + AI reading page), which are on the theme. Rebuilding the standalone pages is a separate job and was not done.
