# generator/

Since A3 (28 October 2026, `docs/academy.md`) there is no separate hub generator: Academy's `kit/build.py` renders every course, and `kit/mdcourse.py` is the markdown course family. This folder holds only the **data** of the markdown courses.

| Path | What |
|---|---|
| `data/brand-ai/` | The Brand + AI data file set (AD5): `hub.py` (every page's text, `COURSES`, `WRITTEN`, `READINGS`, `AUDIT_LOG`, `ORDER`, `STATUS`, the prose blocks and the course's changelog), `units_data.py` (the preamble and the units with their briefs; never reworded), `units/` (the filed units as `build.py` reads them until A5 reads `courses/` directly), `research/`, `briefs/` (the brief text files handed to writing chats), `audience-growth-across-platforms.md` (the superseded research, kept as a reading). `kit/courses.py` points at `hub.py` with `data=`. |
| `data/_template/` | A blank data folder for a new markdown course: one course, three placeholder units, the two audit prompts. Copied by the `new-course` skill. |

Build, check and publish from the kit: `cd kit && python3 build.py && python3 verify.py` (ALL CHECKS PASSED), publish `kit/academy/` to the Academy artifact (the shell, with the report files `python3 publish_files.py` lists as `files`), then `./deploy.sh` for GitHub Pages. `verify.py` carries the checks the retired `check_page.py` made (phone, tablet and desktop; dark and light; 6 px gaps, 44 px targets, no overflow, no console error) and walks a Brand + AI course, its reading page and its "How it is built" pages.

Retired at A3: `build_hub.py`, `hub.js`, `check_page.py`, `build_history.py`, `hubs/`. The Brand + AI hub artifact and the Audience Growth artifact are deleted; their content is in Academy (`#brand-a`, `#brand-b`, `#read-audience-growth`).
