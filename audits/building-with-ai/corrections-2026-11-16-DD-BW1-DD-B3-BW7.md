# Corrections check: DD-BW1 corrections 1 (16 Nov 2026)

Checker: claude-opus-5-5 (Opus 5.5), fresh agent. All sources read 16 Nov 2026 via WebSearch-returned URLs.

## Change 1
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md
Current:
```
(Sprague et al., arXiv 2409.12183, v3 May 2025)
```
Replacement:
```
(Sprague et al., ICLR 2025; arXiv 2409.12183)
```
Result: PASS. The ICLR proceedings page lists "To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning", Zayne Sprague, Fangcong Yin, Juan Rodriguez, Dongwei Jiang, Manya Wadhwa, Prasann Singhal, Xinyu Zhao, Xi Ye, Kyle Mahowald, Greg Durrett, under "International Conference on Learning Representations 2025 (ICLR 2025) Conference". https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html (read 16 Nov 2026).
Syllabus: no conflict. DD-B3 is private; no brief in the packet names Sprague or relies on its venue. DD-BW1 (brief: "Takes: DD-B3 as source material") already cites ICLR 2025, so this aligns the source unit with it. The sourcing standard asks for venue and year for peer-reviewed work; the preprint label no longer applies.

## Change 2
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md
Current:
```
arXiv 2409.12183, v3 May 2025 (§2.6)
```
Replacement:
```
ICLR 2025, arXiv 2409.12183 (§2.6)
```
Result: PASS. Same source as Change 1: ICLR 2025 proceedings page, https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html (read 16 Nov 2026).
Syllabus: no conflict. This is card P1's primary-source line only. No brief, filed unit or register entry relies on it.

## Change 3
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md
Current:
```
arXiv 2409.12183, v3 May 2025 (preprint). https://arxiv.org/abs/2409.12183
```
Replacement:
```
ICLR 2025; arXiv 2409.12183. https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html
```
Result: PASS. Same source as Change 1. The page title and author list match the title and first author in DD-B3's Sources entry ("Sprague, Z. et al. 'To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning'"). https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html (read 16 Nov 2026).
Syllabus: no conflict. §2.6's inline link still goes to the arXiv abstract, which remains a valid open copy. DD-BW1's Sources entry uses the same proceedings URL.

## Change 4
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md
Current:
```
**A2 · Effective context engineering**
- Author: Anthropic.
```
Replacement:
```
**A2 · Effective context engineering**
- Author: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan and Jeremy Hadfield, Anthropic.
```
Result: PASS. The page reads: "Written by Anthropic's Applied AI team: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, and Jeremy Hadfield," with "Sep 29, 2025". https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (read 16 Nov 2026).
Syllabus: no conflict. DD-B3 is private. No brief or register entry names this post's author.

## Change 5
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md
Current:
```
**A3 · Claude Code best practices**
- Author: Anthropic.
```
Replacement:
```
**A3 · Claude Code best practices**
- Author: Boris Cherny, Anthropic.
```
Result: FAIL. Not checked at source. Two WebSearches did not return the address the correction cites (https://www.anthropic.com/research/claude-code-best-practices), so it could not be fetched under the web rule. The address that searches did return, https://www.anthropic.com/engineering/claude-code-best-practices, redirected on fetch to https://code.claude.com/docs/en/best-practices ("Best practices for Claude Code"). That page has no byline, no date and no "no longer maintained" note, and a redirected fetch counts as not checked. The redirect matches DD-B3's own §2.1 and unsure item 9 record. Read 16 Nov 2026.
Syllabus: no conflict in itself. Flag F41 (two versions of the best-practices page) concerns the current documentation page, not the April 2025 post.

## Change 6
File: BW7-pipelines-raw-material-to-finished-output.md
Current:
```
Measured (working paper)
```
Replacement:
```
Measured (working paper; since published in *Organization Science*, DOI 10.1287/orsc.2025.21838)
```
Result: PASS. The publisher page at https://pubsonline.informs.org/doi/full/10.1287/orsc.2025.21838?af=R (URL as WebSearch returned it; read 16 Nov 2026) carries:
- the title "Navigating the Jagged Technological Frontier: Field Experimental Evidence of the Effects of Artificial Intelligence on Knowledge Worker Productivity and Quality";
- the DOI "https://doi.org/10.1287/orsc.2025.21838" (the page path is the same DOI; the fetch summary associated it with the online appendix);
- an acknowledgement of "two referees at Organization Science";
- "The first working paper of this study was released on September 18, 2023";
- the abstract wording "subjects using AI were 19% less likely to produce correct solutions compared with those without AI".

The journal masthead, volume and date were not shown. The journal is therefore inferred from the orsc DOI prefix and the referee acknowledgement. The replacement claims only the journal and the DOI, and no volume or date.
Syllabus: no conflict. BW7 is public and the change names no private course. BW7's other working-paper references stay accurate, because they cite and quote the working-paper version (HBS WP 24-013, 22 Sep 2023, "19 percentage points"): §2 item 4, §3 ideas paragraph, Sources, unsure item 5. They are not changed, since the correction names only the table cell.

BW7's 22 Sep 2023 date and the publisher's "September 18, 2023" for the first working paper may refer to different postings (SSRN versus HBS WP). This is not checked and not changed.

No flag (F52–F58) or brief relies on the working-paper label. DD-BW1 §3.5 already states both versions.

## Not a text change

- **Source error 3, second part: DD-B3 §2.1 sentence "its URL now redirects to the current Claude Code documentation page, so the April 2025 text could not be opened" and unsure item 9.**
  - Today's fetch of the engineering address redirected to https://code.claude.com/docs/en/best-practices, so the sentence is still true of that address.
  - The research address the correction gives was not returned by any search here.
  - Needs: DD-B3's six-month staleness check (method §6) to try the research address and, if it opens, update §2.1, unsure item 9 and card A3 (Change 5). Unit: DD-B3.
- **Contradiction 2: *Building effective agents* (BW7 §1, §2 table, §10 table, Sources, unsure item 8; BW9 unsure item 8).**
  - On 16 Nov 2026 https://anthropic.com/engineering/building-effective-agents (WebSearch-returned) shows the on-page headline "Building effective agents", "Published Dec 19, 2024" and "Written by Erik S. and Barry Zhang".
  - Only the browser title tag reads "Building effective AI agents \ Anthropic". BW7's title, date and authors therefore match the page, and nothing in BW7 changes.
  - BW9 unsure item 8 records BW9's own refused fetch, which per flag F75 was of the anthropic.com research address. It stays true as a record, and BW9 quotes nothing from the post.
  - Needs: flag F75's clause "a corrections pass re-reads Building effective agents for BW7 §1 if it loads" can be marked done for BW7 §1, because the page loaded and agrees. This is a register/flag update, not a unit text change. Units: BW7, BW9.
- **Contradiction 3: Willison's date for the vibe-coding post (6 February versus 2 February 2025 from the status number).**
  - No filed BW unit dates the post.
  - DD-B3 §1.1 already states both: "On 2 February 2025 (date from the status number; Willison's article gives "February 6th" without a year)". DD-BW1 §1.1 states both.
  - Needs: nothing. Units: DD-BW1 (and DD-B3, already consistent).

## New 1
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md
Current:
```
Sprague et al. is cited as a preprint; 
```
Replacement:
```

```
Result: PASS. This is the consequence that correction 1 itself names: "Its unsure item 10, 'Sprague et al. is cited as a preprint', then falls away". The source is the ICLR 2025 proceedings page, https://proceedings.iclr.cc/paper_files/paper/2025/hash/ead542f13a38179d1b55b88610f959a1-Abstract-Conference.html (read 16 Nov 2026). The replacement is empty: the clause and its trailing space are deleted, so item 10 reads "...gives no venue and none is claimed; the OpenAI agents PDF carries no date...". Apply only together with Changes 1–3.
Syllabus: no conflict.

## New 2
File: DD-B3-deep-dive-how-the-best-practitioners-use-the-tool.md
Current:
```
- Anthropic. *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025.
```
Replacement:
```
- Rajasekaran, P., Dixon, E., Ryan, C. and Hadfield, J. (Anthropic). *Effective context engineering for AI agents*. Anthropic Engineering, 29 September 2025.
```
Result: PASS. DD-B3's Sources entry for the post carries the same organisation-only author as card A2 (Change 4). The page reads "Written by Anthropic's Applied AI team: Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, and Jeremy Hadfield," and "Sep 29, 2025". https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (read 16 Nov 2026). This adds no new source, because it is the same page and fact as Change 4. Drop it if the corrections pass is held strictly to the card line.
Syllabus: no conflict.
