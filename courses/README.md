# courses/

The vault. Finished units are filed here at `courses/<course>/<code>-<slug>.md` with the front-matter header of `docs/method.md` §7, and the vault is the source of every course: `kit/build.py` reads the units from here, and a unit is written when its file is here with front matter; there is no second copy.

Each course folder also holds `course.toml`, the course's entry (S-DEC1, 20 Nov 2026): the keys `kit/courses.py` reads for it, found by folder. A new course is a new folder with its `course.toml`; `catalog.toml` at the repo root holds the tracks, the planned courses and the order.

- `brand-ai/`, `ux/`: the markdown courses' units (A5).
- `greece/` (78 reports) and `rome/` (79): Personal Mythology, every report in Markdown since P71-3 (1 November 2026), converted by script from the kit's HTML fragments with no word changed (`docs/p71-3.md`). The forms a report uses (dispute boxes, the Self-test's answers, ```` ```tree ```` and ```` ```viz ```` blocks) are in `kit/AGENT-SPEC.md`; `kit/mdcourse.py` (`history_html`) renders them and `kit/vault.py` finds a report by its id. A history report's front matter gives the model that wrote it; its review status stays in `kit/provenance.json`, and its curated sources in `kit/bibliography/<course>/r-<id>.md`.
