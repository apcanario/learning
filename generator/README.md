# generator/

Since A3 (28 October 2026, `docs/academy.md`) there is no separate hub generator: Academy's `kit/build.py` renders every course, and `kit/mdcourse.py` is the markdown course family. This folder holds only the **data** of the markdown courses.

| Path | What |
|---|---|
| `data/brand-ai/` | Moved (S-DEC2, 20 Nov 2026) into its pack, `courses/brand-ai/`: `course.toml` `[pack]` (the courses, units, order, changelog, audit log), `briefs.md` (the preamble and every brief, word for word), `pages/*.md` (the long blocks), `notes/` (`audience-growth-across-platforms.md`, `research/`, `briefs/`); read by `kit/pack.py`, whose docstring is the schema. STATUS, NEXT_UNIT, VERSION and the units' READINGS are derived there, from the units' front matter and the changelog. |
| `data/_template/` | A blank data folder for a new markdown course: one course, three placeholder units. Copied by the `new-course` skill; with a `courses/<slug>/course.toml` it is the whole course (A5; S-DEC1). |

Build, check and publish from the kit: `cd kit && python3 build.py && python3 verify.py` (ALL CHECKS PASSED), publish `kit/academy/` to the Academy artifact (the shell, with the fetched files `python3 publish_files.py` lists as `files`), then `./deploy.sh` for GitHub Pages. `verify.py` carries the checks the retired `check_page.py` made (phone, tablet and desktop; dark and light; 6 px gaps, 44 px targets, no overflow, no console error) and walks a Brand + AI course, its reading page and its "How it is built" pages.

Retired at A3: `build_hub.py`, `hub.js`, `check_page.py`, `build_history.py`, `hubs/`. The Brand + AI hub artifact and the Audience Growth artifact are deleted; their content is in Academy (`#brand-a`, `#brand-b`, `#read-audience-growth`).
