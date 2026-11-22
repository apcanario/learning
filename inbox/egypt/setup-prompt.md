Clone apcanario/learning (shallow, push access).
Row S-EG0, setup of the course Egyptian history and mythology. Thin main chat on Sonnet 5.5; every agent a fresh Opus 5.5 agent. File the design, build, verify, land and publish. Write no unit. Unattended: ask nothing unless a repo script is refused or the design cannot be read.

Run `python3 kit/land.py start S-EG0`. Before changing anything, save the output of `python3 kit/next_prompt.py --row W-DD-SCE2` to a file outside the repo.

The design is one artifact, https://claude.ai/artifact/X6eax4wJ3sycVTD7kWg7ni. Read it with the artifact reader and open its Files tab: four files as text blocks, each under its file name: `egypt-syllabus.md`, `briefs.md`, `egypt-prompts.md` and `bibliography.md`. Save them outside the repo byte for byte and check each against the sha256 printed beside it.

A registrar (a fresh Agent on model opus) does the repo work from those four files and `skills/new-course`; a second fresh Agent on model opus checks the registration and edits nothing. You never open a brief. No brief is reworded, by anyone.

The registrar:
1. Follows `skills/new-course` steps 4 to 6 for a markdown course, id `egypt`, folder `courses/egypt/`, from `courses/_template/`: `briefs.md` as given; `course.toml` and `pages/` from the syllabus (identity §2, goal and outcomes §3, units and Takes lines §4, writing order and search flags §5, decisions §8); `notes/bibliography.md`, `notes/syllabus-flags.md` opened with flags F1 to F5, and an empty `notes/names.md`; private, History track, family label Personal Mythology, after `rome` in `course_order`; Egypt removed from `planned` in `catalog.toml`.
2. Saves the syllabus as `docs/egypt-syllabus.md` and builds `docs/egypt-prompts.md` as the prompts file's section 0 says, with `prompts_doc` set in the course's `course.toml`.
3. In `kit/next_prompt.py`, adds `egypt` to `QUEUE` and changes nothing else: no `HOLDS` entry, no `GATES` entry, no new option. Then `python3 kit/next_prompt.py --row W-DD-SCE2` prints byte for byte what was saved before; if it does not, the change is undone and redone until it does.
4. Works proposals P-EG2 to P-EG6 of the syllabus's §9, each under its warning; after P-EG2, `python3 kit/baseline.py --check` shows no page of another course changed.
5. Checks every entry of the seed bibliography for existence at Crossref's or the publisher's record, corrects the entry to the record, strikes any it cannot find, and writes how each was checked, in the form of `courses/supply-chain-execution/notes/bibliography.md`. It checks no entry for what it says.
6. Adds Part 9 to `docs/sourcing-standard.md`, the Egypt section to `kit/AGENT-SPEC.md`, and the course's section to `docs/courses-index.md` (0 of 78 written; every unit in writing order with model Opus 5.5, its search flag and its vault path).
7. Adds the writing rows W-EG1 to W-EG57 and W-DD-EG1 to W-DD-EG21 to the queue of `docs/BACKLOG.md`, grouped under one heading per chat exactly as the prompts file's section 0 lists them (Bundle 1 to Bundle 20), with W-EG1's prompt saved by `python3 kit/next_prompt.py --row W-EG1 --save`; and an entry in `docs/site-log.md`.
8. Builds and verifies (ALL CHECKS PASSED, `index_check.py`, `private_terms.py`) and looks at the course home at the three widths.

The checker reads the registration against the four files: every brief byte for byte; every unit's title, order, search flag and Takes line; the goal and outcomes; Part 9 against the syllabus's §6; the template's replaced sections, its clone line and its Reply against the prompts file; the backlog's twenty groups; the `next_prompt.py` diff (one added queue entry) and the byte-identical row; and that nothing outside this course changed in the built site except the home's course list. Its findings are fixed before landing.

Then land (`kit/land.py land`), publish Academy once from a fresh build of the landed HEAD (the artifact, read first, then `kit/deploy.sh`), close the row by `docs/method.md` §8 and refresh the Project mirrors, adding the course's three data mirrors.

One reply. It says what was registered, the bibliography entries struck, the proposals raised (worked in W-EG1's row unless I veto), and any task only I can do. It schedules bundle 1 as the prompts file's section 5b says, or says it has no scheduling tool. It ends with the starter in a code block: the two lines of the prompts file's section 6, or, if `kit/next_prompt.py` has no `--course` option, the same two lines with `--row W-EG1 --bundle 4`.
