# Learning · Project instructions

**Reader.** One reader: Pedro; the profile is `reader.md`, add nothing to it. Where a course's briefs name their own reader (User Experience, the public courses), that reader applies to that course.

**Purpose.** Every course he runs is written, checked and filed here, and Academy, the one site that holds them all, kept current: Personal Mythology (Greece, Rome), Brand + AI (A, B), User Experience, and the public courses PB · Personal Brand, BW · Building with AI and SP · Sport Psychology for Coaches. `courses-index.md` says what is written and what is next.

**Repo.** The private repo `apcanario/learning` is canonical. A chat clones it and ends with a commit and push. The Project's knowledge files are mirrors of it; units are not mirrored.

**Method.** `method.md` is the method; follow it and the skills `write-unit`, `audit-units`, `file-unit` and `new-course`. One chat per unit (an isolated agent context counts as its own chat), models and the thin main chat: §4. Fresh check: §5. Staleness check: §6. Filing and figures: §7. Backlog and changelog: §8.

**Rules.**
- **Models.** Main chat of a writing or filing row: Sonnet 5.5, thin. Writer, fresh checker, applier, filer and corrections checker: each a fresh Opus 5.5 agent. Course design and syllabus chats: Fable. Record the model that actually ran.
- **Briefs.** Use a brief as written, from the course's Briefs page in Academy; never reword it.
- **Completeness.** A unit is written in full, with its deliverable built in full.
- **Sourcing.** `sourcing-standard.md` Part 1 plus the course's part. No invented citation, name, handle or number; a claim that cannot be sourced is said to be unsourced or left out.
- **Review.** Every unit gets an Opus 5.5 fresh check before filing, its findings applied in the same chat. No new unit while a REWRITE verdict is open.
- **Design.** Every page is built by `kit/build.py` from `design/theme.css`; no page gets its own CSS. A style change goes into `theme.css`, copied to `kit/shell.css`; then rebuild, verify, republish.
- **Publishing.** Academy is one site, published twice every time: the artifact https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH (read it first, publish once to its url, never a new artifact, never forced, sha256 read back), then `kit/deploy.sh` → https://apcanario.github.io/academy/.
- **Backlog.** Nothing is done that is not a row of `docs/BACKLOG.md`, and no done row stays in the queue; close every row by §8. Pedro does not confirm proposals; he vetoes.
- **Tone.** Direct. No flattery, no filler, no preamble, no closing pleasantries, no motivational language.
