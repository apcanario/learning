# P30 · B4's seventeen findings against the project on 16 Nov 2026

Packet: `B4-context-engineering.md` (Deliverable, C and F; written 29 Oct 2026, errata of 15 Nov 2026), `method.md`, `project-instructions.md`, `BACKLOG.md`, `skills/` (four `SKILL.md`), `repo-listing.txt` (top two levels, 16 Nov 2026). Line numbers are those of the packet files. The packet does not hold `SETUP.md`, `docs/CHANGELOG.md`, `courses-index.md`, `generator/data/brand-ai/hub.py`, `kit/verify.py`, `design/README.md`, the hand-off note, the preferences, the Project's current knowledge list or its settings; where a verdict depends on one of these, the reasoning says so and takes the most reasonable reading, marked **(reading)**. Listed only: nothing was fixed.

Three changes since 29 Oct 2026 bear on most findings:
- **Fable stage closed, no periodic audit** (S-NOAUDIT, 15 Nov 2026): `method.md` line 23, line 53, §6 line 152; `project-instructions.md` line 21; `skills/audit-units/SKILL.md` lines 3, 8.
- **Thin main chat**: units, checks and filing are done by fresh Opus 5.5 agents on packets staged by `kit/thin.py`, and scripts check the result (`method.md` line 102; `project-instructions.md` line 13; `skills/write-unit/SKILL.md` §0; `skills/file-unit/SKILL.md` line 8; `BACKLOG.md` line 119).
- **Units are not mirrored into the Project** (Pedro, 15 Nov 2026; "the 49 copies were deleted that day"): `method.md` line 102 and §8 step 4 (line 207); `project-instructions.md` line 5; `skills/file-unit/SKILL.md` §6 (line 60).

---

## F1 · Project knowledge may be too large to load and mostly holds files no chat needs whole

**Verdict: STILL APPLIES** (in part done; the five-file target has been overtaken by a later rule that mirrors course data files).

What changed:
- **Done:** the largest share, the filed units (26.8% of the knowledge at B4), is gone: "No unit is uploaded" (`method.md` line 207); "Never upload a unit ... the 49 copies were deleted that day" (`skills/file-unit/SKILL.md` line 60); "Units are not mirrored" (`project-instructions.md` line 5).
- **Overtaken:** B4's Brand + AI writing-chat exception (a writing chat reading earlier units from the knowledge because `SETUP.md` §6 said "Attach nothing else") no longer holds: every row clones `apcanario/learning` (`BACKLOG.md` lines 52, 79, 115), and the writer is an agent given "only its brief and paths to filed units" (`method.md` line 97) through `thin.py stage writer` (`BACKLOG.md` line 129).
- **Changed by a later decision:** B4's fix kept five files. The method now refreshes more mirrors than that: `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` every chat, plus "the method, index, hub, flags and skill mirrors" when changed (`method.md` line 207); "`courses-index.md`, the course's `hub.py` and `syllabus-flags.md`, and the method or skill mirrors" (`skills/file-unit/SKILL.md` line 60); S-BW refreshes `claude/building-with-ai-units_data.py`, `-hub.py` and `-syllabus-flags.md` (`BACKLOG.md` line 105). B4's file-unit fix ("re-upload only `courses-index.md`") is therefore not what the skill now says. `method.md` line 7 still says the Project "holds mirrors of `docs/`", which is no longer the whole of it.
- **Not shown:** whether the history-kit files (`roman-syllabus.html`, 153,026 characters at B4, still in the repo: `repo-listing.txt` line 91), the superseded audience-growth research, the build inputs and the records (`pm-status-2026-10-28.md`, `academy.md`, still in the repo: lines 27, 32) are still in the knowledge. The packet holds no current knowledge list. **(reading)** Nothing in the packet records their removal, so they are taken as still there.

What the fix would change now: remove from the knowledge every file outside a set Pedro names (B4's five, or the five plus the course-data mirrors the method now keeps); rewrite `method.md` line 7 and §8 step 4 and `skills/file-unit/SKILL.md` §6 to list that set; drop the `SETUP.md` §2 and §6 edits if `SETUP.md` is no longer the setup chats read (not in the packet). Effort: B4 gave 40 minutes; revised to about 30 minutes (the units are already out; the SETUP §6 change is superseded), plus Pedro's pick of the set.

⚠ Removing the course-data mirrors (`claude/*-hub.py`, `*-units_data.py`, `*-syllabus-flags.md`) contradicts `method.md` §8 step 4, `file-unit` §6 and the saved S-BW prompt (`BACKLOG.md` line 105), which all write them; those three must change in the same chat. The installed `file-unit` skill must be re-saved to the account. `reader.md`, `method.md`, `courses-index.md` and `sourcing-standard.md` are named in the project instructions and must stay.

## F2 · The project instructions are also uploaded as a knowledge file

**Verdict: STILL APPLIES** (reading).

The packet cannot show the knowledge list. What it shows: `docs/project-instructions.md` is still in the repo (`repo-listing.txt` line 33) and was rewritten on 15 Nov 2026 to the text of the instructions field (`BACKLOG.md` line 212, P120); no mirror rule names it (`method.md` line 207; `skills/file-unit/SKILL.md` line 60), so if a knowledge copy exists it is refreshed by no step and goes stale at every edit of the field, which is B4's point. **(reading)** No record of its removal from the knowledge, so taken as still there. The fix is unchanged: remove it from the knowledge (part of F1). Effort: 1 minute, by Pedro or a chat with the Projects tool.

⚠ none.

## F3 · The knowledge mirror already lags the repository

**Verdict: DONE**, by a different fix than B4's.

The lag B4 measured was in the units (A1, B3 not re-uploaded). Units are no longer mirrored at all (`method.md` line 207; `skills/file-unit/SKILL.md` line 60), so that lag cannot recur. For the files that stay, the method now rewrites the Project copies at the close of every chat "so the Project knowledge never lags the repo" (`method.md` §8 step 4, line 207), and the saved row prompts carry it out with the Projects tool ("read each with `project_read` first, then write it with `local_path`": `BACKLOG.md` lines 76, 105; `project-instructions.md` line 23 step 5). B4's GitHub-integration route was not taken; the packet shows no use of it. Whether every mirror is current today cannot be checked from the packet.

## F4 · Two different files are called `BACKLOG.md`

**Verdict: STILL APPLIES** (lower stakes than in October).

Both files still exist (`repo-listing.txt` lines 25 and 46). Bare references remain where the history lane notes are meant: `project-instructions.md` line 15 ("the module's lane note in `BACKLOG.md`"), `method.md` line 3, line 87 ("ordered in `BACKLOG.md`"), line 143 ("its lane note from `BACKLOG.md`"), `skills/write-unit/SKILL.md` §2 ("the module's lane note in `BACKLOG.md`"). The queue disambiguates itself in its header (`BACKLOG.md` line 3). What changed: Greece and Rome are complete (`project-instructions.md` line 5; `method.md` line 5; Rome's queue table is empty, `BACKLOG.md` lines 20 to 23) and every new course is a markdown course (`method.md` line 73; `skills/new-course/SKILL.md` §1), so no chat now needs the lane notes; the bare name now misleads only a chat looking for the queue. The fix would rename `kit/BACKLOG.md` (to `kit/LANES.md`, or move it to an archive as a closed course's record) and point the five references above, and any others in the repo, to the new path. Effort: B4 gave 45 minutes; unchanged (the reference count in the repo today is not in the packet).

⚠ The project instructions' Briefs paragraph is in the claude.ai field, which only Pedro can edit (`BACKLOG.md` line 212, P120); the `write-unit` skill must be re-saved to the account; any kit script that opens `kit/BACKLOG.md` by name (not visible in the packet) must be found by grep first.

## F5 · Three of the preferences collide with the Project's work

**Verdict: NO LONGER APPLIES** (reading).

The three collisions were with how a chat wrote a unit and closed a row:
- (a) and (b), HTML artifact for anything with three sections, and concise bullet format, against a long-form Markdown unit: units are no longer written in the chat Pedro talks to. The writer is a fresh agent that writes `out/unit.md` to a packet folder and replies in at most six lines (`method.md` line 102; `skills/write-unit/SKILL.md` §0; `BACKLOG.md` line 144), and the agents use no Artifact tool (`BACKLOG.md` lines 56, 137). The unit's form is set by the packet and the skill, not by a chat reply.
- (c), "don't volunteer next steps", against handing over the backlog: every row prompt Pedro pastes now asks for the hand-off and the next prompt ("end with the next row's prompt", `BACKLOG.md` lines 52, 79, 115; "Reply: ... then S-BW's prompt", line 78), and `project-instructions.md` line 23 step 4 and `method.md` §8 steps 3 and 5 require it. It is asked for, so the preference's condition no longer bites.

The packet does not show the preferences themselves; whether Pedro added "unless a Project's instructions say otherwise" is not visible. The Scope paragraph of B4's D was not adopted (`project-instructions.md` has no such paragraph), and the reasons for it have gone.

## F6 · The design preferences and the theme agree

**Verdict: NO LONGER APPLIES.**

F6 had no fix; it was "recorded so the next audit does not re-check it". No periodic audit runs: the Fable stage closed on 15 Nov 2026 (`project-instructions.md` line 21; `method.md` line 53; `skills/audit-units/SKILL.md` line 8). Neither the preferences nor `design/theme.css` is in the packet, so the agreement itself was not re-checked.

## F7 · The project instructions carry procedures and paraphrase the method

**Verdict: STILL APPLIES**, larger than in October.

The instructions have grown from 675 words to 862 (`project-instructions.md`, `wc -w` in the C locale) and from 4,421 characters to 5,617. Per paragraph: Purpose 162 words (B4: 147), now listing the kit's scripts; Publishing 59 (B4: 56), now restating the publish procedure down to "sha256 read back" (`skills/file-unit/SKILL.md` §5.3; `BACKLOG.md` line 74); Backlog and changelog 192 (B4: 133), restating `method.md` §8 steps 1 to 5 (lines 203 to 208); Review 63, restating `method.md` §6 and line 53; Models 78, new since B4, restating `method.md` line 102; One chat per unit 85, restating `method.md` line 97 (P31). B4's replacement text (Deliverable, D) is out of date and cannot be pasted as it stands: it says "audit Fable 5.1" and "No unit starts while an audit is due", both retired (`method.md` line 53), and lacks the thin main chat, P31, the vetoes rule (`project-instructions.md` line 23) and the public courses' own readers (line 3). What the fix would change now: redraft D against the current method (rules every chat obeys, the public-site rule, pointers to `method.md` §4, §5, §6, §8 and `file-unit` §5 for procedures), paste it into the field, and copy it to `docs/project-instructions.md`. Effort: B4 gave 20 minutes; revised to about 45 minutes (redraft and check, then Pedro's paste).

⚠ The instructions field is Pedro's to edit (`BACKLOG.md` line 212); two open hand tasks touch the same paragraphs and should go with it: P120 and P-SP4 (Purpose line lacks Sport Psychology, `BACKLOG.md` line 211). `skills/new-course/SKILL.md` §6 adds a course to the Purpose line "only if it stays under 400 words", a limit the instructions already exceed at 862, so P-SP4 is blocked by that rule until F7 shortens them or the rule is changed. Moving procedure out of the instructions makes the thin main chat rely on `method.md`, which its rows already tell it to read (`BACKLOG.md` lines 54, 117).

## F8 · Which units search: four prose copies, three versions

**Verdict: STILL APPLIES** (the `method.md` copy is shown unchanged; the other three are not in the packet).

`method.md` line 113 still reads "Brand + AI units on: A2, A6, A9 (written), A8, B2, B8, DD-A1", the same list B4 quoted at its line 114, still without DD-B3 and B1. Brand + AI is now complete (`BACKLOG.md` line 27), so "(written)" is wrong for the rest of the list too. `SETUP.md` §6 and `hub.py` lines 127 and 139 are not in the packet; **(reading)** taken as unchanged, unless the S-NOAUDIT removal of audit mentions from the website (`method.md` line 53) took the `hub.py` lines with it. The fix is unchanged: replace each list with "the Search column of `courses-index.md`". Effort: 15 minutes; the `hub.py` part needs a rebuild and publish, best done with F9b.

⚠ A `hub.py` edit means a rebuild, `verify.py` and one publish of Academy (artifact, then `deploy.sh`), and its Project mirror refreshed (`skills/file-unit/SKILL.md` line 60); the `method.md` edit means the method mirror refreshed (`method.md` line 207).

## F9 · Stale files and lines still read as current

**Verdict: STILL APPLIES** (part d done; parts a, b, c, e not shown done).

- (a) `docs/handoffs/` is still in the repo (`repo-listing.txt` line 29) and there is no `docs/archive/`; `docs/pm-status-2026-10-28.md` and `docs/academy.md` are still in `docs/` (lines 32, 27), and are still cited as live: "Specs are in `pm-status-2026-10-28.md`" (`BACKLOG.md` line 3), `method.md` line 7 (D4) and line 171 (A5). `kit/NEXT-SESSION.md`, another hand-off file named in `method.md` line 3, is still in the kit (`repo-listing.txt` line 48); its contents are not in the packet.
- (b) `hub.py`'s `BUILD_PICK`, `BUILD_BODY` and `AUDIT_PROMPTS_NOTE` are not in the packet. Pedro's S-NOAUDIT instruction was to "erase the audit mentions from the website" (`method.md` line 53), which may have removed `AUDIT_PROMPTS_NOTE` and the review line; **(reading)** the "separate Project" and "personal-assistant Project" lines are taken as still there until a grep shows otherwise.
- (c) `SETUP.md` §8 is not in the packet. Its "first audit is due after B1" is now wrong twice over, since no audit runs (`method.md` line 53).
- (d) **Done:** the queue no longer has a "(parallel; one unit per chat)" lane heading; section 3 reads "Brand + AI, courses A and B interleaved" and is empty (`BACKLOG.md` lines 25 to 30).
- (e) `design/README.md` and `generator/data/_template/hub.py` are not in the packet; the only `build_hub` mention in the packet is a dated record (`BACKLOG.md` line 187). **(reading)** taken as unchanged; `new-course` still copies `_template/` (`skills/new-course/SKILL.md` §5.1), so a stale line there reaches every new course.

What the fix would change now: grep the repo for "personal-assistant", "build_hub.py", "learning-project", "Next session" and "due after B1"; move the hand-off note, `pm-status-2026-10-28.md`, `academy.md` (once their open items are closed) and `kit/NEXT-SESSION.md` to `docs/archive/`, and repoint `BACKLOG.md` line 3 and `method.md` lines 3, 7 and 171; correct `SETUP.md` §8, `design/README.md` step 3 and `_template/hub.py` line 3; delete what remains of the v5.1 record blocks in `hub.py`, then rebuild, verify and publish. Effort: B4 gave 20 minutes (a, c, d, e) plus 45 minutes (b); revised to about 20 minutes plus 45 minutes, (d) being done and `kit/NEXT-SESSION.md` added.

⚠ Moving `pm-status-2026-10-28.md` and `academy.md` breaks the pointers in `BACKLOG.md` line 3 and `method.md` lines 7 and 171 unless they move in the same commit; the `hub.py` change needs one Academy rebuild and publish (do it with F8); the `_template/` change affects the next new course only.

## F10 · The queue and the record are behind the work

**Verdict: DONE.**

The queue holds no filed unit's row: Brand + AI's section is empty with the note "Complete: A-5 filed DD-A2 and DD-B2 on 2 to 3 Nov 2026, the last of both courses" (`BACKLOG.md` lines 25 to 30), and "Done rows are in `CHANGELOG.md`" (line 214). The procedure that prevents it is now in every row's close: `method.md` §8 step 1 (line 203), `project-instructions.md` line 23 ("no done row stays in the queue"), and each saved prompt's Close step (`BACKLOG.md` lines 76, 105, 171). `docs/CHANGELOG.md` is not in the packet, so the B3 and A1 changelog rows themselves were not seen.

## F11 · The theme reaches the build through a hand copy

**Verdict: STILL APPLIES** (reading for the `verify.py` half).

`kit/shell.css` is still in the repo (`repo-listing.txt` line 92), and the hand copy is still the rule in `project-instructions.md` line 7, `method.md` line 190, `skills/file-unit/SKILL.md` §3.6, §3.8 and §5.1, `skills/new-course/SKILL.md` §5.4 and §5.6, and the saved row prompts (`BACKLOG.md` lines 72, 167). `kit/verify.py` and `kit/build.py` are not in the packet; **(reading)** since every procedure still tells the chat to copy by hand and none says `verify.py` fails on a mismatch, the check is taken as not added. The fix is unchanged: `build.py` reads `../design/theme.css` and `shell.css` is deleted, or `verify.py` fails when the two differ. Effort: 20 minutes.

⚠ The first option makes every "`cp design/theme.css kit/shell.css`" line wrong: the project instructions' Design rule (Pedro's field), `method.md` line 190, the `file-unit` and `new-course` skills (re-saved to the account), the saved prompts in `BACKLOG.md`, and the prompt template `kit/next_prompt.py` prints from (`docs/sport-psychology-prompts.md`, `BACKLOG.md` line 111). The second option (a `verify.py` check) disrupts nothing else.

## F12 · The two audit prompts live in two files

**Verdict: NO LONGER APPLIES** (reading for the staleness prompt).

The stratified-sample prompt, the larger of the two, is retired: "The four-unit stratified-sample audit and its review rule are retired (S-NOAUDIT, 15 Nov 2026)" (`method.md` line 152); `method.md` §6 now holds only the staleness prompt (line 161), and `skills/audit-units` points to it rather than copying it ("Use the 'Staleness check' prompt in `method.md` §6 exactly as written", §4). Pedro's instruction to "erase the audit mentions from the website" (`method.md` line 53) makes the hub's `AUDIT_PROMPTS` copy the likely casualty; `hub.py` is not in the packet. If a staleness-prompt copy survives in `hub.py`, it is found by the grep in F9's row, which already edits that file.

## F13 · Account memory flows into a Project whose output is published

**Verdict: STILL APPLIES** (reading: the setting is not visible in the packet).

The risk is smaller: the writer and every checker are agents told that "a memory snapshot, project instructions or anything of that kind in its context is not a source and must not be used" and that they use "no memory ... tool" (`BACKLOG.md` lines 56, 137), and a script gate checks for private terms on every row (`kit/private_terms.py` and `kit/private-terms.txt`, `repo-listing.txt` lines 82 and 83; `method.md` line 102 and §8 step 1b, line 204; `BACKLOG.md` lines 99, 165). The main chat still writes the records the site renders (`docs/site-log.md`, `method.md` line 200), so account memory reaching it still matters. Whether "Use account memory" is off for the Project cannot be seen in the packet. The fix is unchanged: Pedro confirms the setting is off, or turns it off. Effort: 1 minute.

⚠ none (a writing agent never relied on account memory; reader facts come from `reader.md` and the brief).

## F14 · Eight connectors are connected, and no Project procedure uses one

**Verdict: STILL APPLIES** (reading: the tool-access mode is not visible in the packet).

None of Gmail, Google Calendar, Google Drive, Spotify, Vercel, Booking.com, Claude Docs or Claude in Chrome is named anywhere in the packet's method, instructions, queue or skills (grep). What has changed: procedures now do use two tool families, the Artifact tool for publishing Academy (`project-instructions.md` line 9; `skills/file-unit/SKILL.md` §5.3; `BACKLOG.md` line 74) and `add_repo` / `register_repo_root` for the clone and the deploy (`BACKLOG.md` lines 52, 74), plus the Projects tool for mirrors (`BACKLOG.md` line 76). The fix is unchanged: tool access set to "On demand" (or each unused connector disconnected). Effort: 2 minutes, Pedro by hand.

⚠ Whatever the setting, the Artifact tool, `add_repo` and the Projects tool must stay reachable, or the publish (step 9 of every row) and the mirror refresh fail; "On demand" defers them rather than removing them, so it is safe, but disconnecting must leave those three alone.

## F15 · The public build carries private material

**Verdict: STILL APPLIES** (residual: B4's parts 2 and 3 look done; part 4 and the B1 erratum are not shown).

Done in substance: a private-terms list and a checker exist (`kit/private-terms.txt`, `kit/private_terms.py`, `repo-listing.txt` lines 82, 83), the checker is a gate on every row ("`python3 kit/private_terms.py` prints OK", `method.md` line 204; line 102; `BACKLOG.md` lines 99, 165), and site-log entries carry "no private term" (`method.md` line 200). The terms file sits in the private repo `apcanario/learning` (`project-instructions.md` line 5), not in the public `apcanario/academy`, which meets B4's "outside both repositories" aim for the public side. Not shown: (1) the B1 §3 erratum; whether `private_terms.py` scans the built `kit/academy/` pages, the briefs pages included, or only source files (`method.md` line 204 runs it beside `check_site_log` "on the rebuilt pages", which suggests the built pages, but does not say it); (4) Pedro's decision on the public repository's history, which only he can take. What the fix would change now: confirm by reading `private_terms.py` that it scans `kit/academy/`, confirm the B1 erratum, and put (4) to Pedro. Effort: B4 gave 2 hours for (1) to (3); revised to about 15 minutes to confirm, plus Pedro's decision on (4).

⚠ Rewriting the public repository's history (4) would force-push `apcanario/academy`; GitHub Pages redeploys, and any clone or fork keeps the old commits (B4 F15's GitHub source).

## F16 · Nothing checks for rot between sessions

**Verdict: STILL APPLIES**, with a smaller check than B4's E.

No scheduled task appears anywhere in the packet (grep "scheduled": none). Several of E's six checks now run inside every row instead: (1) filed units still queued, through the close procedure (`method.md` §8 step 1) and `next_prompt.py --list` (`BACKLOG.md` line 121); (6) private terms, through `private_terms.py` (F15). Check (4), the audit prompts, has no object (F12). What remains between sessions: (2) instructions to use retired things (F9), (3) the theme copy (F11, unless it is fixed), (5) the knowledge budget (F1), and the staleness list. E's prompt must also be rewritten: it reads only `courses/brand-ai/` and names `docs/handoffs/` and `generator/data/brand-ai/hub.py` (Deliverable, E). What the fix would change now: either a weekly cloud scheduled task with the reduced prompt and no connectors, or the same greps added to `verify.py`, which every row already runs. Effort: B4 gave 20 minutes; revised to about 20 minutes either way.

⚠ A scheduled task runs and spends usage each week whether or not a row ran; it must make no commit. Adding the checks to `verify.py` instead would fail every build until F9 and F11 are fixed, so it goes after them.

## F17 · The index, the one file every chat needs, is mostly a finished record

**Verdict: STILL APPLIES**, at lower value.

The finished share has grown: Greece and Rome, Brand + AI, User Experience, PB and BW are complete, and the only course in progress is Sport Psychology (`project-instructions.md` line 5; `BACKLOG.md` lines 27, 34, 109). But the premise "the one file every chat needs" has weakened: the thin main chat reads `courses-index.md` only to confirm no REWRITE is open (`BACKLOG.md` lines 58, 85, 121), and scripts read it whole (`index_check.py`, `next_prompt.py --list`, `thin.py`; `method.md` line 193). Its cost now is mainly its Project copy, refreshed when changed (`skills/file-unit/SKILL.md` line 60). `courses-index.md` is not in the packet, so its size today was not measured. The fix is unchanged: finished courses to `docs/courses-index-archive.md`, `index_check.py` taught to read both. A cheaper route with the same effect on the Project is to drop the index from the knowledge under F1, though the project instructions name it. Effort: B4 gave 2 to 3 hours; revised to 3 to 4 hours (six finished courses, and `next_prompt.py` and `thin.py` also read it).

⚠ `index_check.py`, `next_prompt.py`, `thin.py`, the filer's `records.json` edits (`BACKLOG.md` line 165), `method.md` §7 step 5 and `file-unit` §6 all address `courses-index.md` by name; a split that misses one fails `verify.py` on every later row.

---

## Summary

| Finding | Verdict | One line |
|---|---|---|
| F1 Knowledge too large | STILL APPLIES | Units are out; history kit, research, records and build inputs not shown removed; the five-file target conflicts with the course-data mirrors the method now keeps |
| F2 Instructions also a knowledge file | STILL APPLIES (reading) | No record of removal; no mirror step refreshes it |
| F3 Mirror lags repo | DONE | Units no longer mirrored; method §8 step 4 rewrites the mirrors every chat |
| F4 Two `BACKLOG.md` files | STILL APPLIES | Both exist and bare references remain; lower stakes now history is complete |
| F5 Preferences collide | NO LONGER APPLIES (reading) | Units are written by agents to files; every prompt asks for the hand-off |
| F6 Design preferences agree with theme | NO LONGER APPLIES | No fix, and no next audit to spare |
| F7 Instructions carry procedures | STILL APPLIES | Grown to 862 words; B4's text D is stale and must be redrafted |
| F8 Search-on lists | STILL APPLIES | `method.md` line 113 unchanged; other copies not in the packet |
| F9 Stale files and lines | STILL APPLIES | (d) done; hand-off notes, status notes, `hub.py` blocks, `SETUP.md` §8, template line not shown fixed |
| F10 Queue behind work | DONE | No filed unit's row in the queue; close procedure in every row |
| F11 Theme hand copy | STILL APPLIES (reading) | `shell.css` and the copy step everywhere; no `verify.py` check shown |
| F12 Audit prompts in two files | NO LONGER APPLIES (reading) | Stratified audit retired; staleness prompt pointed to, not copied |
| F13 Account memory | STILL APPLIES (reading) | Agents ignore memory and a script gate exists; the setting is not visible |
| F14 Unused connectors | STILL APPLIES (reading) | None used; Artifact, `add_repo` and Projects tools now are |
| F15 Private material in public build | STILL APPLIES (residual) | Terms file and gate exist; B1 erratum, scan scope and Pedro's history decision not shown |
| F16 No rot check | STILL APPLIES | No scheduled task; E reduced to checks 2, 3, 5 and staleness |
| F17 Index mostly finished record | STILL APPLIES | Bigger finished share, smaller payoff; many scripts read it |

**Counts:** still applies 12 · done 2 · no longer applies 3.

## Proposed rows

| P30-F1 | *Proposed.* Cut the Project knowledge to a named set (B4's five, or the five plus the course-data mirrors), delete the rest from the Project, and make `method.md` line 7 and §8 step 4 and `skills/file-unit/SKILL.md` §6 list that set. ⚠ `method.md` §8 step 4, `file-unit` §6 and the saved S-BW prompt refresh course-data mirrors and must change together; the installed `file-unit` skill is re-saved. | B4 F1 (P30, 16 Nov 2026) | Pedro picks the set; then a housekeeping row after W-DD-SP3, Opus 5.5 |
| P30-F2 | *Proposed.* For Pedro by hand, or with P30-F1: remove `project-instructions.md` from the Project knowledge if it is there. ⚠ none | B4 F2 (P30, 16 Nov 2026) | With P30-F1 |
| P30-F4 | *Proposed.* Rename or archive `kit/BACKLOG.md` (the closed history lane notes) and point every bare `BACKLOG.md` reference to its path. ⚠ The project instructions' Briefs line is Pedro's field; the `write-unit` skill is re-saved; kit scripts that open the file by name are found by grep first. | B4 F4 (P30, 16 Nov 2026) | A housekeeping row after W-DD-SP3, Opus 5.5 |
| P30-F7 | *Proposed.* Drafted by a chat, pasted by Pedro: redraft the project instructions as rules plus pointers against the current method (B4's text D is stale), shorten them below the 400-word limit `new-course` §6 sets, and copy them to `docs/project-instructions.md`; add Sport Psychology to the Purpose line. ⚠ Pedro's field; to be done with P120 and P-SP4, which touch the same paragraphs. | B4 F7 (P30, 16 Nov 2026) | Pedro, with P120 and P-SP4 |
| P30-F8 | *Proposed.* Replace the prose lists of search-on units in `method.md` §4 (line 113), `SETUP.md` §6 and `hub.py` with "the Search column of `courses-index.md`". ⚠ The `hub.py` edit needs one rebuild and publish of Academy and its mirror refreshed; do it with P30-F9. | B4 F8 (P30, 16 Nov 2026) | With P30-F9 |
| P30-F9 | *Proposed.* Grep the repo for retired instructions ("personal-assistant", "build_hub.py", "learning-project", "due after B1"); archive the hand-off note, `kit/NEXT-SESSION.md` and, once closed, `pm-status-2026-10-28.md` and `academy.md` in `docs/archive/`; correct `SETUP.md` §8, `design/README.md` step 3, `_template/hub.py` line 3 and the remaining v5.1 blocks in `hub.py`; rebuild, verify, publish. ⚠ `BACKLOG.md` line 3 and `method.md` lines 3, 7 and 171 point at the moved files and must be repointed in the same commit; one Academy publish. | B4 F9 (P30, 16 Nov 2026) | A housekeeping row after W-DD-SP3, Opus 5.5 |
| P30-F11 | *Proposed.* Make `verify.py` fail when `design/theme.css` and `kit/shell.css` differ (or have `build.py` read `theme.css` and retire `shell.css`). ⚠ none for the `verify.py` check; retiring `shell.css` makes the copy step wrong in the project instructions, `method.md`, two skills, the saved prompts and the prompt template. | B4 F11 (P30, 16 Nov 2026) | A housekeeping row after W-DD-SP3, Opus 5.5 |
| P30-F13 | *Proposed.* For Pedro, by hand: confirm "Use account memory" is off for the Learning Project, or turn it off. ⚠ none | B4 F13 (P30, 16 Nov 2026) | Pedro, any time |
| P30-F14 | *Proposed.* For Pedro, by hand: set tool access to "On demand" (or disconnect the eight unused connectors). ⚠ The Artifact tool, `add_repo` and the Projects tool must stay reachable for publishing, cloning and mirrors. | B4 F14 (P30, 16 Nov 2026) | Pedro, any time |
| P30-F15 | *Proposed.* Confirm that `private_terms.py` scans the built `kit/academy/` pages, briefs included, and that B1's erratum is in; then Pedro decides whether the public repository's history is rewritten. ⚠ A history rewrite force-pushes `apcanario/academy` and does not reach existing clones. | B4 F15 (P30, 16 Nov 2026) | The check in the next housekeeping row; the decision Pedro's |
| P30-F16 | *Proposed.* A weekly between-session rot check (a cloud scheduled task with no connectors and no commit, or the same greps in `verify.py`) for retired instructions, the theme copy, the knowledge budget and the staleness dates due in 30 days. ⚠ A scheduled task spends usage weekly; checks added to `verify.py` fail every build until P30-F9 and P30-F11 are done. | B4 F16 (P30, 16 Nov 2026) | After P30-F9 and P30-F11 |
| P30-F17 | *Proposed.* Split `courses-index.md` into a live index and `docs/courses-index-archive.md` for finished courses, and teach `index_check.py`, `next_prompt.py` and `thin.py` to read both (or drop the index from the Project knowledge under P30-F1 instead). ⚠ Every script, skill and filer record that names `courses-index.md` must change in the same chat, or `verify.py` fails on later rows. | B4 F17 (P30, 16 Nov 2026) | After W-DD-SP3, Opus 5.5; low priority |
