---
audit: correction check (docs/public-courses.md §3 rule 12; step 6 and 7b of row W-BW1)
date: 2026-11-15
units: B1 (the Source errors list of BW1's writer; verified once by BW1's fresh check, section 8, and checked again here)
course: brand-ai · B · Using AI to Build a Brand
model: claude-opus-5-5 (stated by the checker)
note: saved verbatim from the checker's returned text; the checker could not write files
---

Model: claude-opus-5-5

**Corrections check, B1 (W-BW1 steps 6 and 7b), 15 Nov 2026**

I read only the packet. There is no flags file and out/ is empty. I wrote no files.

**1. claude.ai window**
- Current, line 72: "On claude.ai paid plans, Anthropic's help centre states that the context window is 200K tokens across all models and paid plans, with some models at 500K on Enterprise ([Claude Help Center, usage and length limits](https://support.claude.com/en/articles/11647753))."
- Current, line 74, first sentence: "His Project runs on claude.ai, so his working budget is 200K tokens, a fifth of the figure on the model page."
- Replacement: the writer's text from the notes, item 1, linked to https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans.
- 1b. These consequential edits are not on the writer's list but are needed for consistency:
  - Line 69: "and the one that applies to him is the smaller." → "and on 15 Nov 2026 they agree for his model." The heading date also changes to "(as of 15 Nov 2026)".
  - Line 74: delete the parenthetical "(On 2 Nov 2026 … B8 §1.)", which is now obsolete.
  - Line 84: "a 200K-token window holds roughly 540,000 characters" → "a 1M-token window holds roughly 2.7 million characters", and "around 6 to 7 percent" → "about 1.3 percent". This is the unit's own arithmetic. It adds no source.
- **PASS.** https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans has these table rows: "Claude Opus 5.5 | 1M tokens", "Claude Opus 4.8 | 500K tokens", and the sentence "Outside of these models, Claude's context window size is 200K." The old cited article (11647753) now says: "the newest models support up to a 1M token context window".
- Syllabus: no contradiction. The B8 brief ("Search first for current claude.ai plan limits … (Oct 2026)") is the unit B1 cross-refers to, and the change brings B1 into line with B8's 1M finding. The DD-B3 brief builds on "his setup as B1, B2 and the units written since describe it", so it now inherits 1M. That is correct.

**2. Temperature**
- Current, line 215: "Temperature is an API parameter; none of the claude.ai help articles cited in this unit offers him a temperature setting."
- Replacement: the writer's text from the notes, item 2, linked to https://platform.claude.com/docs/en/build-with-claude/working-with-messages.
- **PASS.** https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md says: "not supported on Claude 4.7 and later models"; "Setting them to a non-default value returns a 400 error"; "use prompting to guide the model's behavior instead."
- Note: line 219 ("even with temperature set to 0 …", from the glossary) can stay, but it now describes models before 4.7 only. I suggest no change there, to avoid adding a claim.
- Syllabus: no brief relies on a temperature setting. The B4 brief's "file temperatures" is a different sense of the word.

**3. Lineup and prices**
Occurrences of "Fable 5.1":
- Line 71: "Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 all have a 1M-token window" → "… Fable 5.2 …", dated 15 Nov 2026.
- Line 88: "As of 28 October 2026: … Fable 5.1 $10 / $50" → "As of 15 November 2026: … Fable 5.2 $8 / $40 (Fable 5.1, still listed, $10 / $50)". The other three prices are unchanged.
- Line 128, chart: label "Fable 5.1" with values 10, 50 → "Fable 5.2" with values 8, 40, and the caption date becomes "15 November 2026".
- Line 195: "As of 28 October 2026 … and Fable 5.1 as June 2026" → "As of 15 November 2026 … and Fable 5.2 as June 2026".

**PASS.** https://platform.claude.com/docs/en/about-claude/models/all-models shows these rows:
- "Claude Fable 5.2 | 1M tokens | 128K tokens | $8 / MTok | $40 / MTok"
- "Claude Fable 5.1 | … | $10 / MTok | $50 / MTok"
- Opus, Sonnet and Haiku 5.5 unchanged, all with cutoff Jun 2026.

https://platform.claude.com/docs/en/models/fable-5-2/overview says "Active (latest)" and "Reliable knowledge cutoff Jun 2026".

Caveats:
- The exact URL B1 cites (.../about-claude/models/overview) was not returned by my search, so I did not check it.
- The all-models page gives no cutoff for Fable 5.1.

Syllabus: no contradiction, but there is a dependency. The B2 brief names "Fable 5.1 as of Oct 2026", and line 88 hands routing to B2. If B2 is filed naming Fable 5.1, B2's routing table and prices go stale. That is a proposal for B2, not a block on B1.

**4. Source titles**
- Line 342: "Anthropic. *Working with messages*." → "*Using the Messages API*". PASS: the page title is "Using the Messages API".
- Line 344: "*Agent Skills overview*" → "*Agent Skills*". PASS: the page title is "Agent Skills" (https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview.md).
- Line 347: "*Updates to our consumer terms*" → "*Updates to Consumer Terms and Privacy Policy*". PASS: H1 "Updates to Consumer Terms and Privacy Policy", "Aug 28, 2025" (https://www.anthropic.com/news/updates-to-our-consumer-terms).
- Line 349: "*Usage and length limits* (article 11647753)" → "*How do usage and length limits work?* (article 11647753)". PASS: the title is "How do usage and length limits work?" (https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work).
- The same titles also appear inline: "*Working with messages*" on lines 140 and 246, "*Agent Skills overview*" on line 250, and "*Updates to our consumer terms*" on line 183. Change them the same way, with the same URLs.
- Syllabus: no effect.

**5. Statelessness**
- Current, line 140: "Anthropic's API documentation says the Messages API is stateless and that the full conversation history is sent with every request ([Anthropic, *Working with messages*](…))."
- Replacement: append the writer's sentence from the notes, item 5, after it.
- **PASS.** https://platform.claude.com/docs/en/build-with-claude/working-with-messages.md says: "With message threads, in beta, the API can keep the conversation, so that each later request sends only the new messages." The page still says "The Messages API is stateless".
- Syllabus: the DD-B1 brief (agents) is unaffected. B1's thesis ("the model keeps nothing between turns") still holds, because the thread is kept by the API, not the model.

**6. Holtzman venue**
- Current, line 215: "[Holtzman et al., "The Curious Case of Neural Text Degeneration", ICLR 2020]". Line 357: "ICLR 2020."
- Replacement: **no change.** The venue is confirmed.
- **PASS for the existing text.** https://mlanthology.org/iclr/2020/holtzman2020iclr-curious gives "Venue: International Conference on Learning Representations", "Year: 2020", and the authors Holtzman, Buys, Du, Forbes, Choi. The listing https://iclr.cc/virtual/2020/poster/1428 exists, but the fetch showed no venue text.
- Syllabus: no effect.

**7a. Memory exclusions**
- Current, line 178: "it never stores government ID numbers, criminal history, financial account numbers or immigration status".
- Replacement: **none for now; keep the text.**
- **NOT CHECKED.** The fetch of https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context.md was refused, and per the web rule I did not retry it. The writer's own read was a summary, so deletion is not supported.
- Syllabus: the B8 brief covers "privacy and retention of what he stores in memory". B8 should re-read the article.

**7b. Long chats**
- Current, line 169: "and that such long chats consume more usage, so a new chat may help".
- Replacement: **no change.** The correction is wrong: the statement is on the page.
- **PASS for the existing text** (https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work):
  - "Longer conversations that trigger automatic context management consume more of your usage limit."
  - "Try starting a new conversation if you're approaching your usage limit in a longer chat."
- Syllabus: consistent with B8 ("when a new chat is cheaper").

**Apply:** 1 (with 1b), 2, 3, 4, 5. Do not apply 6, 7a or 7b.
