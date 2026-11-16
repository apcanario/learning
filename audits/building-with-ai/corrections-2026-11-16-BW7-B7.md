---
kind: corrections-check
row: W-BW7
course: building-with-ai
date: 2026-11-16
model: claude-opus-5-5
units: [B7]
chat: https://claude.ai/code/session_01KMmgQxb5xyzkrLHQ6hh6WQ
---

The checker's report, verbatim from its reply (the harness refused it a report file), saved before any change was applied.

Model: claude-opus-5-5
Verdict: 3 pass, 0 fail, 0 syllabus conflicts

The Write tool refused to create /tmp/bw7/corr/out/report.md, so the full report is below.

I counted each Current by script (`grep -oF … | wc -l`) in files/B7-content-pipeline.md, and each occurs exactly once. Changes 1 and 2 are both on line 36 but do not overlap. Change 3 is on line 112.

## Change 1
File: B7-content-pipeline.md, §2, the paragraph "Where the brief and the filed units differ" (line 36). Count: 1.
Current:
```
In Doshi and Hauser's experiment, 300 writers wrote eight-sentence stories
```
Replacement:
```
In Doshi and Hauser's experiment, 293 writers (of 500 recruited) wrote eight-sentence stories
```
Result: PASS. The paper recruited 500 participants and analysed 293 writers and stories. The paper does not give 300 as its sample size.
Source: "For the writer study, we recruited 500 participants to participate in the experiment from the Prolific platform." and "...resulting in a total number of writers and stories of 293." (Doshi and Hauser, Science Advances, Exeter repository copy, https://ore.exeter.ac.uk/rest/bitstreams/199326/retrieve, fetched 16 Nov 2026). The PubMed Central copy (https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532) returned a browser check and is not checked.
Syllabus: no conflict. No brief in briefs/, no line of case-academy.md and no flag in syllabus-flags.md mentions Doshi and Hauser or the figure 300.

## Change 2
File: B7-content-pipeline.md, §2, same paragraph (line 36), the sentence after the citation. Count: 1.
Current:
```
That is fiction, judged by strangers, with ChatGPT ideas
```
Replacement:
```
That is fiction, judged by strangers, with GPT-4 ideas
```
Result: PASS. The paper says the story ideas came from GPT-4 through OpenAI's API, not from ChatGPT.
Source: "At the time of the study, we used the API from OpenAI's latest model, GPT- 4." (same Exeter copy, https://ore.exeter.ac.uk/rest/bitstreams/199326/retrieve, fetched 16 Nov 2026).
Syllabus: no conflict. The flags that mention ChatGPT (F5, F34, F48) are about OpenAI's help pages and do not touch this study.

## Change 3
File: B7-content-pipeline.md, §8, the Agarwal bullet "The model's style wins against a writer's own" (line 112). Count: 1.
Current:
```
with and without a Western-centric model's suggestions
```
Replacement:
```
with and without GPT-4o's inline suggestions
```
Result: PASS. The paper names the model, GPT-4o, and says its suggestions came as inline autocomplete.
Source: "In the AI condition, the textbox fetched an inline autocomplete suggestion from GPT-4o if the user paused typing for 100 ms." (Agarwal, Naaman and Vashistha, arXiv 2409.11360 v3, §3.3.1, https://arxiv.org/html/2409.11360v3, fetched 16 Nov 2026). The bullet's other figure also holds: "We conducted a cross-cultural controlled experiment with 118 participants from India and the United States" (same page, Abstract).
Syllabus: no conflict. No brief, flag or line of case-academy.md mentions Agarwal and colleagues.

New: none. In the same passages, "600 evaluators" matches the paper: "There were a total of 3519 evaluations of 293 stories made by 600 evaluators." (Exeter copy). "118 participants" matches the arXiv abstract. I did not re-check the Exeter release's 8.1% and 9%, the v3 date (12 Mar 2025) or the DOI in this run.
