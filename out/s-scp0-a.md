# S-SCP0 step A and step B (write part): report

Created `courses/supply-chain-planning/` from `courses/_template/`:

- `briefs.md`: byte-identical to `inbox/supply-chain-planning/briefs.md` (cmp). A Preamble and 18 unit sections: SCP1 to SCP16, DD-SCP1, DD-SCP2.
- `course.toml`: registry keys from `courses/supply-chain-execution/course.toml`, changed as the header of `course-pack.toml` says (id, short, label, eyebrow, name, home_id, status, tracks.SCP, tiles.SCP, color var(--teal), data, vault, sourcing_part "Part 9", source_units false, prompts_doc, dated_lists true). `[pack]`: course_note, learn_note, home_lede, order (18 rows), the one `[[pack.courses]]` table and its 18 units from `course-pack.toml`, checked equal with tomllib; the other keys filled in the Execution form (order_lede and order_foot as Execution; title, bar, brand_html, out, theme_key, learn_c teal, build_c gold, home_h1, template_lede, template_note, learn_tile, build_tile; empty `[pack.status]`); a v1 changelog row dated 2026-11-22 22:30. `kit/pack.py` loads it: 18 order rows, 18 units, 18 Aim lines, VERSION v1 · 22 Nov 2026, NEXT_UNIT SCP1.
- `pages/`: the five Execution pages (briefs-lede, build-body, build-pick, frame, order-notes), written for this course from the syllabus (§1 frame and pushback, §5 order and chats, §7 models) and the briefs.
- `notes/case-facts.md`: byte-identical to `inbox/supply-chain-planning/case-facts.md` (cmp). Checks of B not run (left to the other agent).

## Repo against prompt

1. `part` key. `kit/pack.py`'s schema has no part field for a unit and the Execution course's units have none (nor do its pages carry part headings). The `part` keys were dropped from `course.toml` and the parts written as a "Parts" line in `pages/order-notes.md` (Opening SCP1; Part 1 · Demand SCP2–SCP5; Part 2 · Inventory SCP6–SCP8; Part 3 · Supply and the plan SCP9–SCP12; Part 4 · The product, its users and its buyers SCP13–SCP16; Deep dives). A comment in `course.toml` says so.
2. `color` in `[[pack.courses]]`: required by the schema, absent from `course-pack.toml`'s course table; set to `var(--teal)`, the registry colour.
3. `course-pack.toml` header lists the registry changes but not `[pack]` keys title, bar, brand_html, out, theme_key, learn_c, build_c, home_h1, order_lede and the rest; filled in the Execution form (learn_c teal, build_c gold, the swap of Execution's gold/teal).
4. Pages: the template has four pages, the Execution course five (it adds build-pick.md); the Execution form, five, was used. The Execution build-body's gate step (after SCE6) became the read point after SCP8 with no gate row (syllabus §5); the review rule's colour is the course's teal (Execution used its own gold).
5. `reliefs = true` (new-course step 5b) was not set: it belongs with step I (outlines), as verify.py then requires ten outlines. The Execution course does not set it either.
6. The v1 changelog row states the bibliography as "46 references, 42 checked for existence (4 not opened)" and names the syllabus-flags file; steps C and D have not run yet, so the row must be updated if step C changes the count.
7. Prompt said `git add -A`; the only change in the tree was the new course folder plus this report, so both are committed.
