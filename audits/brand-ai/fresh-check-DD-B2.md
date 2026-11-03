---
audit: fresh check
unit: DD-B2 · Deep dive: his unknown unknowns
course: brand-ai · B · Using AI to Build a Brand
model: Opus 5.5 (search off; past-chat tools to re-run a sample of the writer's counts; a Fable 5.1 fresh check is owed, and the unit falls to Audit 6, both deferred by Pedro 31 Oct 2026 to the Fable stage)
date: 2026-11-03
chat: own Opus 5.5 agent context, not shown the writing or the writer's report (P31), in session https://claude.ai/code/session_01KMmgR37RxR23LNtnYJijb7 (row A-5)
verdict: fix · 3 errors, 4 should-fix, 5 minor
---

# Fresh check · DD-B2 · Deep dive: his unknown unknowns

The checker's final report follows verbatim, extracted by script from its hand-back (its `SubagentHandback` message).

**This fresh check was run by Opus 5.5. A Fable 5.1 fresh check is still owed: the course owner deferred Fable 5.1 checks to a later stage on 31 Oct 2026, and this report does not replace that check. The unit falls to Audit 6, the final audit, which is also owed to the Fable stage.** The brief's "by Fable" was set aside by the course owner on 31 Oct 2026, so it is not a finding.

**Copy.** I ran `diff` on /tmp/claude-0/a5/check-DD-B2/DD-B2-check-copy.md against /home/claude/learning/courses/brand-ai/DD-B2-deep-dive-his-unknown-unknowns.md. The two are identical. I read the copy in full (218 lines).

**Brief.** I built it by script, as kit/mdcourse.py does (PRE with {GOAL} replaced by hub.GOAL_B, a blank line, then the fifth field of DD-B2's entry). It is saved at /tmp/claude-0/a5/check-DD-B2/brief.txt. Its asks: review 90 days; classify each ask by task type, model, accepted or not, and turns; find where he asked badly, where the tool was wrong for the job, what he did by hand that a skill already does, and research he paid for and did not need. Deliverable: a personal gap report of the ten highest-leverage changes.

**Errata.** audit-1.html and audit-2.md hold no erratum that touches DD-B2. Audit 1 triggered the rule that every later unit gets a fresh checker, and this check meets it.

**Model readings: how I re-ran them.** The unit says 13 chats have no recorded model. The tools return a commit trailer for most of those chats once you search inside the chat. I ran `conversation_search` inside each chat (query "Co-Authored-By Claude commit") and opened the hits:
- **Chat 11** (status, 28 Oct): Fable trailers.
- **Chat 12**: Fable.
- **Chat 13**: Fable.
- **Chat 14**: Fable.
- **Chat 15**: Fable trailer, and its own changelog row says "Fable 5.1".
- **Chat 17**: Fable.
- **Chat 18**: Opus. Its changelog row reads "Opus 5.5, search off".
- **Chat 22**: Fable.
- **Chat 24**: Fable.
- **Chat 25**: Fable.
- **Chat 33** (29 Oct 20:44, the IA syllabus): Fable.
- **Chat 43**: Opus trailers, then a Fable 5.1 trailer on the "H-2 takes P72 and P73" commit.
- **Chat 52**: the revert commit carries a Fable 5.1 trailer; its baseline commit carries Opus.
- **Chats 46, 47, 49, 50 and 51**: Opus trailers. The history chats 46 and 47 are Opus.
- **Chat 48**: Opus trailers only.

Chat indexes are mine, rebuilt as the unit describes: ordered by first message, with listing time used where the first message was not shown. They match every index the unit cites (2, 3, 5, 7, 23, 27, 34, 36, 37, 39, 40, 45, 48, 52) except where noted below.

# Findings

- [error] [accuracy] §1 table; §2 Models and table; §4 (twice); Deliverable 1, 2 and 6; unsure items 4 and 10; §7 rule 11. The model readings are incomplete, so every count built on them is wrong.
  - Current: `Of the 53 chats, 23 show Opus 5.5, 16 Fable 5.1, one both (its commits carry an Opus trailer, then a Fable one), and 13 show nothing. No chat whose model can be read ran on Sonnet 5.5 or Haiku 5.5 (0 of 40).`
  - Problem: Searching inside each chat finds a model trailer or record for all 53 chats. My reading:
    - Fable 5.1, whole chat: 19 (chats 2, 4, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 19, 21, 22, 24, 25, 26, 33).
    - Both models: 2 (chats 43 and 52).
    - Opus 5.5: 32.
    - Sonnet or Haiku: 0 of 53.
    - The "one both" chat the unit means is 52 (the A-4 row), not 48, and 43 is a second one.
    - Fable whole or part is therefore 21, not 17. 16 of them are not audits; 18 began on 28 Oct and 1 each on 29 Oct, 1 Nov and 2 Nov.
    - Effort is still recorded in none of the 53.
  - Fix: `Of the 53 chats, 32 show Opus 5.5, 19 Fable 5.1 and two both (Opus trailers, then a Fable one: chats 43 and 52); a search inside each chat for its commit trailers finds a model for all 53. None ran on Sonnet 5.5 or Haiku 5.5 (0 of 53).`
  - Basis: `conversation_search` within each chat, 3 Nov 2026; trailers quoted in the hits. Script: /tmp/claude-0/a5/check-DD-B2/recount.py.
  - Same-cause edits, each Current checked to occur once:
    - `| 40 of 53; 13 "not recorded" |` → `| 53 of 53 (a search inside each chat for its commit trailers) |`
    - The crosstab rows. With my labels set so that every type total and median matches the unit's, the rows become:
      - `| Unit writing (15) | 14 | 0 | 1 | 0 | 12 |`
      - `| Infrastructure (15) | 6 | 8 | 1 | 0 | 8 |`
      - `| Audits (6) | 1 | 5 | 0 | 0 | 2.5 |`
      - `| Status (6) | 3 | 3 | 0 | 0 | 10 |`
      - `| Syllabus (2) | 0 | 2 | 0 | 0 | 10 |`
      - `| History writing (2) | 2 | 0 | 0 | 0 | 50.5 |`
      - Figure passes stays `6 | 1 | 0 | 0`.
      - The audit counted as Opus is chat 29, an Opus orchestrator that ran a Fable agent. The task labels are mine, so the rows other than these totals are indicative.
    - `Seventeen chats ran on Fable 5.1 in whole or part. Five were audits or fresh checks; the other twelve were infrastructure (8, counting the switch), a syllabus, a status question, a figure pass and an orchestrator (`count.py`, `count2.py`). Fourteen of the 17 began on 28 October.` → `Twenty-one chats ran on Fable 5.1 in whole or part. Five were audits or fresh checks; the other sixteen were infrastructure (10, counting two switches), two syllabus chats, three status questions and a figure pass (a search inside each chat for its commit trailers). Eighteen of the 21 began on 28 October.`
    - `Fable in 7 of 15, Opus in 3, unknown in 4` → `Fable in 8 of 15, Opus in 6, both in 1`
    - `the 15 infrastructure chats ran on Fable 7, Opus 3, switched 1, unknown 4; no chat that records a model ran on Sonnet or Haiku (0 of 40)` → `the 15 infrastructure chats ran on Fable 8, Opus 6, both 1; no chat ran on Sonnet or Haiku (0 of 53)`
    - `12 of the 17 chats run on Fable 5.1 were not audits or fresh checks; 14 of the 17 began on 28 October` → `16 of the 21 chats run on Fable 5.1 were not audits or fresh checks; 18 of the 21 began on 28 October`
    - `the model can be read in 40 of 53 chats and effort in 0 of 53; 13 chats record no model at all` → `the model can be read in all 53 chats, but only by searching inside each one for its commit trailers; effort in 0 of 53`
    - `The model can be read in 40 of 53 chats; effort in none (`count.py`).` → `The model can be read in all 53 chats, from commit trailers found by searching inside each; effort in none.`
    - `Unit writing: 11 of 15 on Opus, and the one Fable chat in the type is an orchestrator that filed a unit whose front matter records Opus 5.5.` → `Unit writing: 14 of 15 on Opus; the fifteenth (chat 52) carries Opus and then Fable trailers.`
    - Unsure item 4 `4. The 13 chats with no recorded model may include Sonnet or Haiku chats; "0 of 40" is over recorded chats only.` → `4. Each chat's model is read from the commit trailers a search inside it returns; a chat whose commits all came from agents could hide its own model.`
    - Unsure item 10 `10. Chat 48's two commit trailers may come from a Fable agent inside an Opus chat rather than a switch of the chat's model.` → `10. Chats 43 and 52 carry Opus and then Fable trailers; either may be a Fable agent inside an Opus chat rather than a switch of the chat's model.`
    - `Rule 11 (model and effort before the first message): one chat's commits carry two models` → `Rule 11 (model and effort before the first message): two chats' commits carry two models`
    - The note `model read from commit trailers in 24 chats, the filed unit in 9, the ask in 6, another chat's record in 1.` → `model read from commit trailers found by a search inside each chat.`

- [error] [accuracy] §4 Fan-outs; Deliverable 3. The Greek re-checker count is wrong.
  - Current: `In chat 39 alone the Greek pass ran 78 adders, 78 checkers and 59 re-checkers`
  - Problem: In the same session, chat 39 corrected its own changelog from 59 to 62 re-checkers (sed command seen at a search hit). The repository records 62.
  - Fix: `In chat 39 alone the Greek pass ran 78 adders, 78 checkers and 62 re-checkers`
  - Basis: kit/CHANGELOG.md line 319 ("78 adders, 78 checkers, 62 re-checkers"); docs/CHANGELOG.md line 32 ("62 + 2 re-checkers"); search inside chat 39.
  - Same cause: `215 agents (78 adders, 78 checkers, 59 re-checkers)` → `218 agents (78 adders, 78 checkers, 62 re-checkers)`

- [error] [figure] §4 figure 3. Its values come from the wrong count and do not appear in the text.
  - Current: the whole block, beginning `{"kind": "compare", "unit": "", "max": 14, "rows": [{"label": "28 Oct", "value": 14, "tone": 2}, {"label": "29 Oct", "value": 0, ...` (full Current quoted under (7)).
  - Problem: The 29 Oct, 30 Oct, 1 Nov and 2 Nov values (0, 0, 2, 1) are stated nowhere in the text. On the corrected readings the values are 18, 1, 0, 1 and 1.
  - Fix: the JSON given under (7).
  - Basis: as for finding 1.

- [should-fix] [accuracy] §7 DD-B1 rule 27; Deliverable 5; unsure item 5. The overlap count is off.
  - Current: `ten chats began while an earlier one was still open (14 overlapping pairs by first-message and last-update times, an upper bound)`
  - Problem: My script agrees on 14 overlapping pairs. Those pairs hold 12 later chats (4, 6, 7, 8, 9, 10, 11, 15, 33, 34, 35, 53) and 10 earlier ones, so "ten chats began while an earlier one was still open" is wrong.
  - Fix: `twelve chats began while an earlier one was still open (14 overlapping pairs by first-message and last-update times, an upper bound)`
  - Same cause:
    - `10 of 53 chats began while an earlier one was still open` → `12 of 53 chats began while an earlier one was still open`
    - `5. The 10 overlapping chats are counted` → `5. The 12 overlapping chats are counted`
  - Basis: /tmp/claude-0/a5/check-DD-B2/open.py.

- [should-fix] [accuracy] §7 rule 27 and Deliverable 9. The branch evidence is understated.
  - Current: `two figure-pass asks were written for an overnight run over filed course units; of the 39 asks held as text, one names a branch; both runs went ahead on the morning of 30 October instead.`
  - Problem: The figure passes did work on branches. The repo records `p43-rome-wip` and `n5-p57-wip` for the Rome and Greek passes, and chat 37's own commits say "Commit progress to the side branch". So the asks did not name a branch, but the runs used one. As written, the sentence implies the passes ran on `main`.
  - Fix: `two figure-pass asks were written for an overnight run over filed course units; of the 39 asks held as text, one names a branch, though the Rome and Greek passes worked on side branches (`p43-rome-wip`, `n5-p57-wip`, docs/CHANGELOG.md P62 and P65); both runs went ahead on the morning of 30 October instead.`
  - Basis: docs/CHANGELOG.md lines 7, 30 and 31; search inside chat 37.

- [should-fix] [accuracy] §1. The listing-call count is wrong.
  - Current: `Three listing calls of twenty chats each (the second run's) covered the window`
  - Problem: In my rebuild the third call returned 13 chats, not 20.
  - Fix: `Three listing calls (20, 20 and 13 chats; the second run's) covered the window`
  - Basis: `recent_chats` with `before`, 3 Nov 2026.

- [should-fix] [deliverable] Deliverable 1, Bears on.
  - Current: `*Bears on:* B2's routing table, Audits row; B8 rules 21 and 28.`
  - Problem: Rule 28 is DD-B1's rule, not B8's. The unit's own §7 also groups "Rules 21 and 28" under B8 (Current: `Rules 21 and 28 (check usage first; the week's unit and audit before optional agent runs)`).
  - Fix (Deliverable 1): `*Bears on:* B2's routing table, Audits row; B8 rule 21; DD-B1 rule 28.`
  - Fix (§7): `Rule 21 (check usage first) and DD-B1's rule 28 (the week's unit and audit before optional agent runs)`
  - Basis: DD-B1-deep-dive-agents.md §8 ("four rules, numbered after B8's … 28.").

- [minor] [accuracy] §1 and §5. The memory-tool count does not reproduce.
  - Current: `the model called the memory tool in 6 of 53 chats, all in the parts of the chats that were read.`
  - Problem: In the listing blocks I find memory calls in 5 chats (15, 16, 20, 23, 26). The sixth may sit in a saved read I did not open. Partial check.
  - Fix: none required; the unit's unsure item 9 already states the limit.

- [minor] [accuracy] §3. The time of the last status-opened chat does not match.
  - Current: `The last status-opened chat began on 29 October at 19:04`
  - Problem: The 19:04 chat (32) opens "let's execute the next personal brand unit", which is a terse ask, not a status question. The last chat opened by a status question is 31, at 17:43 ("…what's next?").
  - Fix: `The last status-opened chat began on 29 October at 17:43`
  - Basis: read_conversation of chats 31 and 32.

- [minor] [label] §6. The 4× and 15× multipliers are labelled vendor.
  - Current: none.
  - Problem: DD-B1 §8 labels the multipliers "vendor, 2025", and the unit does too. No issue found.

- [minor] [coverage] §1.
  - Current: none.
  - Problem: The brief's 90 days fall to 6. The unit states this and gives the reason; no change.

- [minor] [style] Deliverable 2.
  - Current: `Build and site rows with a `verify.py` pass as their test: Sonnet 5.5, medium; escalate to Opus once if verify fails twice on the same cause. Method, skill and design-decision rows: Opus 5.5, high.`
  - Problem: No count in the unit or in a filed unit backs the efforts "medium" and "high". B2 §8 supports only "Sonnet is enough" for scripts. This is a recommendation without its own evidence; it is acceptable only because it is flagged by its Worked-if test.
  - Fix: keep as is and add ` (efforts by analogy with B2's rows; untested)` after `Opus 5.5, high.`

# Confirmed

- 53 chats in the window. Five listing calls: 20, 20 and 13 chats, then nothing before 05:50 on 28 Oct and only the 17:51 chat after 17:00 on 2 Nov. First message 05:42 on 28 Oct (read of chat 1); last update 17:51 on 2 Nov.
- Turns, all 53 opened for total_turns: 872 in all, median 8, range 2 to 134. Eleven chats have 2 turns (1, 2, 3, 4, 5, 7, 9, 20, 21, 22, 23) and ten have 30 or more. Chat 39 has 134.
- Open time: median 0.93 h (the unit says 0.9); nine chats open 3 h or more; the longest 20.2 h at 43 turns, then 9.9 h at 40 and 8.6 h at 20 (open.py).
- Medians by type, on my labels: audits 2.5, history 50.5, figures 33, status 10, syllabus 10. These agree.
- Fresh-check records (fc.py, plus B8's line read by hand): 20 of 21 filed units carry one (B1 none). 15 had at least one error at their first check. Fable ran 11 and found errors in 9; Opus ran 9 and found errors in 6. All 9 Opus checks are dated 2 Nov and say a Fable check is owed. B6 §2 reads "eleven of fourteen": this agrees.
- Greek pass: 266 figures proposed, 166 passed, 95 fixed, 94 re-passed, 6 dropped; 6/266 = 2.26%. Kept 260 = 166 + 94 (search inside chat 39; kit/CHANGELOG.md line 319).
- The 30 chats without a routing row = 15 + 7 + 6 + 2. Crosstab rows sum correctly (arithmetic).
- Pasted units: the five measured run from 49,594 to 53,516 characters (my reads of chats 3, 4, 5, 7 and 8, ask text without system reminders).
- URL overlaps: Audit 1 holds 82 distinct external URLs in its read (the unit says 81; it has 16 fetched directly and 6 agents). A9 rewrite: 43, of which 33 were Audit 1's (unit: 34). A6 rewrite: 45 fetched, 15 Audit 1's. A6 fresh check: 46, of which 37 were the A6 writer's. Agrees within one, which is the limit of extraction.
- Quotes checked: chat 17 "Model: any (Fable 5.1 or Sonnet 5.5 is enough; no search)"; chat 34 "Another chat beat this one to it"; chat 52's revert "the 15:05 B-13 session is alive and mid-unit"; chat 35 "now just history"; chat 36's ask "Pedro is low on Fable" with "overnight run". Chat 36 began on 30 Oct at 07:14.
- Chat 23: "A4" was taken as the Academy row. The reply says "If you meant the unit, say so and it gets its own chat." Chat 27, "Execute B1, B2 and B3", began on 28 Oct at 22:56.
- Asks at length (12 in the listings): 8 contain "ALL CHECKS PASSED" and 7 contain "publish once". "Fails twice" appears in four figure-chat asks (36 to 39).
- Next-prompt blocks: 15 listing blocks end with a code-block prompt; the unit says 13 ("13 chats … carry"). This is a borderline count by method, so I raise no finding.
- Filed-unit pointers (each unit opened at the section):
  - DD-B3 rules 1 to 10 (Deliverable B): reported right.
  - B8 rules 11 to 24 (Deliverable), including the rule 22 wording "stays off in the Learning Project, whose output is published": reported right.
  - DD-B1 rules 25 to 28 (§8) and boxes 2, 5c, 5d, 6 and 8 (box 6 quoted exactly): reported right.
  - DD-B1 §8 "about 4× … about 15× (vendor, 2025)": reported right.
  - B2 routing table, Audits row, quoted exactly. B2 §8 "For his generator scripts and parsers, Sonnet is enough on this evidence" is exact.
  - B8 §1: "No page gives the number of tokens or messages a plan allows" and rule 21's "No page publishes how many tokens a window holds".
  - B5 §6, the four questions; B5 §3, `file-unit` named among the repository skills.
  - B6 §2, eleven of fourteen; B6 Deliverable A routes research; Deliverable D has the checker open the cited source.
  - B4 F7 (the project instructions paraphrase the method), F13 (account memory flows into the Project), F15 (six private terms in kit/academy) and check 6.
  - B1 §2: re-sending and attention.
- Dated facts: no filed unit's dated fact is contradicted. B4 F15's check is still not in kit/verify.py ("terms" occurs 0 times), which supports Deliverable 4.

# Counts and calculations (re-run by script in /tmp/claude-0/a5/check-DD-B2/)

| Count | Unit | Mine | Result |
|---|---|---|---|
| Chats | 53 | 53 | agrees |
| Total turns | 872 | 872 | agrees |
| Median turns | 8 | 8 | agrees |
| Range | 2–134 | 2–134 | agrees |
| 2-turn chats | 11 | 11 | agrees |
| ≥30 turns | 10 | 10 | agrees |
| Median open | 0.9 h | 0.93 h | agrees |
| ≥3 h | 9 | 9 | agrees |
| Longest three | 20.2 / 9.9 / 8.6 | same | agrees |
| Overlap pairs | 14 | 14 | agrees |
| Chats begun while another open | 10 | 12 | differs |
| Models read | 40 of 53 | 53 of 53 | differs |
| Opus / Fable / both / none | 23/16/1/13 | 32/19/2/0 | differs |
| Fable whole or part | 17 | 21 | differs |
| Fable began 28 Oct | 14 | 18 | differs |
| Non-audit Fable | 12 | 16 | differs |
| Sonnet/Haiku | 0 | 0 | agrees |
| Effort recorded | 0 | 0 | agrees |
| Fresh-check records | 20; 15 err; F 11/9; O 9/6 | same | agrees |
| Greek agents | 215 | 218 | differs |
| Greek figures | 266/166/95/94/6 | same | agrees |
| Drop rate | ~2% | 2.26% | agrees |
| No routing row | 30 | 30 | agrees |
| Pasted range | 49,594–53,516 | same | agrees |
| Audit 1 URLs | 81 | 82 | agrees within extraction |
| A9 overlap | 43/34 | 43/33 | agrees within extraction |
| A6 overlap | 45/15 | 45/15 | agrees |
| A6 check overlap | 46/37 | 46/37 | agrees |
| Memory calls | 6 | 5 found | partial |
| Listing calls | 3 × 20 | 20/20/13 | differs |

**Sample.** I drew a systematic sample: every fifth chat in my index from chat 3 (3, 8, 13, 18, 23, 28, 33, 38, 43, 48, 53), plus chat 11 (a status chat), for 12 chats. I then opened all 53 for turns. Classified by the unit's categories:
- Task types agree for all 12 on a plausible labelling.
- Turns agree.
- Accepted-proxy: 8, 13, 23, 28, 38, 43 and 53 end with a row reported done.
- Model differs in 11 (Fable, not unrecorded), 13 (Fable), 33 (Fable) and 43 (both).

# Deliverable: ten changes

The deliverable is present in full and usable alone. Each change names its count, its rule and a test.

1. **Fable only for checking.** The count supports the change, and supports it more strongly on the corrected figures (16 of 21). Its rule pointer must split B8 rule 21 from DD-B1 rule 28.
2. **Routing row for the machine.** Supported: 30 of 53 chats have no routing row. The efforts are unsupported (see the style finding).
3. **Fan-out down.** Supported by box 6, but the agent count needs the fix (218).
4. **Deploy gate.** Supported: 13 of 16 asks have the session deploy; B4 F15; verify.py has no terms check.
5. **One writer to main.** Supported, on 12 chats and 14 pairs, plus the revert in 52 and the "beat this one" in 34.
6. **Model and effort in the first line.** Effort, 0 of 53, supports it. The model half now rests on "only readable by search", not "13 unrecorded", so it still stands.
7. **Closing procedure as a skill.** Supported: 13 of 16 asks restate the procedure; B5 §6; B4 F7.
8. **Carry an audit's confirmed claims forward.** Supported by the 33 or 34 URL overlap; B8 rule 18.
9. **No overnight run without a branch.** Partly supported. The runs did use side branches, so the count needs the correction, though the asks still did not name them. DD-B3 rule 7 ("never on course units") stands.
10. **Memory off.** Supported (5 or 6 chats; B8 rule 22; B4 F13).

The ranking is the writer's judgement and is said to be.

# Public-site rules

- Quotes no conversation at length: **held**. The longest quoted chat line is one sentence (§4, "Model: any …").
- Names no private person: **held**. A scan for names, the employer, a club and family finds nothing; "he" throughout.
- No personal fact beyond the brief and the filed units: **held**. "He is low on Fable" (§4) is a plan or usage state, already implied by B2 and B8.
- Nothing about his employer: **held**.
- No health, family, money, employer or relationship chat described: **held**. No chat in the window is of those kinds.
- No chat link, id or title: **held**. No chat title from the listing occurs in the unit (scripted check); chats are cited by index and date only.

# Pointers

All the named pointers were opened and are reported right (see Confirmed). One pointer error: "B8 rules 21 and 28", where 28 is DD-B1's (should-fix above). No filed unit's dated fact is contradicted by the history.

# Search mode

The unit is search off, and no web source was used. The product facts it states are dated to the source or pointed to filed units: Fable billing is left to B2 and B8 §1 with "re-read on 2 November 2026"; the multipliers point to DD-B1 §8 as "Anthropic's 2025 figures; vendor". I found none that is neither. I made no web search, because nothing needed one.

# (7) Figures

1. **compare, §2 (chats by task type): PASS.** Every label and value is in line 36. The caption names §2 and count.py. The kind fits (numbers compared).
2. **bars, stacked, §2 (model by task type): FIX.** The values trace to the table but are wrong per finding 1. The caption is fine; the kind fits. Replace the rows with:
   `"rows": [{"label": "Unit writing", "values": [14, 0, 1, 0]}, {"label": "Infrastructure", "values": [6, 8, 1, 0]}, {"label": "Figure passes", "values": [6, 1, 0, 0]}, {"label": "Audits", "values": [1, 5, 0, 0]}, {"label": "Status", "values": [3, 3, 0, 0]}, {"label": "Syllabus", "values": [0, 2, 0, 0]}, {"label": "History writing", "values": [2, 0, 0, 0]}]`
   The caption becomes `"caption": "The model each chat ran on, by task type. §2 of this unit; the writer's tally over 53 chats, model read from the commit trailers a search inside each chat returns."`
3. **compare, §4 (Fable chats by day): FIX (error).** The 29 Oct to 2 Nov values are in no line of the text, and all values change per finding 1.
   - Current: `{"kind": "compare", "unit": "", "max": 14, "rows": [{"label": "28 Oct", "value": 14, "tone": 2}, {"label": "29 Oct", "value": 0, "tone": 2}, {"label": "30 Oct", "value": 0, "tone": 2}, {"label": "1 Nov", "value": 2, "tone": 2}, {"label": "2 Nov", "value": 1, "tone": 2}], "caption": "Chats run on Fable 5.1, in whole or part, by the day they began. §4 of this unit; the writer's tally (count2.py) over the 17 Fable chats among the Project's 53, model read from commit trailers, the ask, or the filed unit."}`
   - Fix: `{"kind": "compare", "unit": "", "max": 18, "rows": [{"label": "28 Oct", "value": 18, "tone": 2}, {"label": "29 Oct", "value": 1, "tone": 2}, {"label": "30 Oct", "value": 0, "tone": 2}, {"label": "1 Nov", "value": 1, "tone": 2}, {"label": "2 Nov", "value": 1, "tone": 2}], "caption": "Chats run on Fable 5.1, in whole or part, by the day they began. §4 of this unit; the 21 Fable chats among the Project's 53, model read from the commit trailers a search inside each chat returns."}`
   - Also add to §4, after "Eighteen of the 21 began on 28 October": ` One began on each of 29 October, 1 November and 2 November, none on 30 October.`
   - The kind fits; a timeline would also do, but compare is acceptable.

# Current check

Every Current above was checked to occur exactly once in /tmp/claude-0/a5/check-DD-B2/DD-B2-check-copy.md. I used `grep -F -c` for plain strings and Python `str.count` for any Current with a backtick, a pipe table row or JSON. All returned 1. Two findings (the vendor-label minor and the coverage minor) carry no Current.

# Notes

- **Files.** Working files are in /tmp/claude-0/a5/check-DD-B2/: brief.txt, table2.json, turns.json, open.py, recount.py, fc.py, and reads/ (copies of my own saved tool results). My write of report.md as the final file was refused, so this reply is the report. report.md holds an earlier working log and then a one-line note that this reply supersedes it.
- **Memory.** Nothing from memory was used. I found no memory text directing an agent.

DD-B2, verdict fix, 3 errors, 4 should-fix, 5 minor

**Maintainer's note (3 Nov 2026, the orchestrating chat of row A-5).** The checker's transcript was checked by script: no memory, Projects, connector, Artifact or other `mcp__*` tool beyond the three past-chat tools it was given (5 listing calls, 38 searches, 59 reads); no web call; nothing opened under the writer's packet, the prompts folder, the lost writers' files or any transcript; it copied twelve files from the session's tool-results folder into its own folder, every one its own saved tool result (checked by script against its transcript), as its prompt allowed. Every finding was verified before it was applied, each as an exact replacement whose Current occurred once in the unit (Python `str.count`), by one script. How each was verified:

- **1 (model readings), applied in part.** The checker's own search results, with the reads it saved, were scanned by script for `Co-Authored-By: Claude <model>` trailers: they bear out its readings for the 13 chats the unit had left unrecorded (chats 11 to 15, 17, 22, 24, 25 and 33 Fable; 46, 47, 49, 50 and 51 Opus) and Opus and Fable trailers in chat 52; chat 18's Opus rests on a changelog row the checker quotes, not on a trailer the scan found. In two chats the writer and the checker each found a trailer the other did not: chat 24 (the writer's saved read shows an Opus trailer, the checker's search Fable ones) and chat 48 (the writer's reads show Opus then Fable, the checker's search Opus only). Read on the union of both, chats 24, 43, 48 and 52 carry both models, so the unit now says 31 Opus, 18 Fable and four both, Fable in whole or part 22 (17 not audits; 18, 1, 0, 2 and 1 by day), infrastructure Fable 8, Opus 5, both 2, status Opus 3, Fable 2, switched 1; the checker's other edits were applied as given, with these numbers in place of its 32, 19, 2 and 21. The table's and the bars figure's "Not recorded" column, now empty, was taken out, and the deliverable's preamble says the model was read for every chat (same cause).
- **2 (Greek re-checkers):** `kit/CHANGELOG.md` session 32 records 78 adders, 78 checkers, 62 re-checkers. Holds.
- **3 (figure 3):** the new values are stated in §4 now (18, 1, 0, 2, 1 on the union reading); fixed with finding 1.
- **4 (overlap), not applied.** The writer's table gives every chat its first-message time (53 of 53); on those times, by script, 14 overlapping pairs hold 10 later chats, as the unit says. The checker's 12 come from its own table, which used the listing time where the first message was not shown. The unit's 10 stands.
- **5 (branches):** `docs/CHANGELOG.md` records `n5-p57-wip` (P62) and the merged branches P65 deleted. Holds.
- **6 (listing calls):** the second run's saved listing results hold 20, 20 and 13 chats. Holds.
- **7 (rule 28):** DD-B1 §8 gives "four rules, numbered after B8's"; rule 28 is DD-B1's. Holds, both places.
- **Minors:** the last status-opened chat (17:43, its opener a "what's next?") applied as the checker read it; the efforts in change 2 flagged "by analogy with B2's rows; untested" applied; the memory-call count (5 found, 6 claimed) left as the unsure list already states its limit; the two minors without a Current needed nothing.

The verdict stands as fix: three errors, one of them in part.
