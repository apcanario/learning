# Prompts document: what changes against the Execution course's

For `docs/supply-chain-planning-prompts.md`. The setup row copies `docs/supply-chain-execution-prompts.md` as it stands in the repo (sections 1 to 4 and the writing template, with every correction its rows have made), changes the course's names, codes, paths, rows (W-SCP1 to W-SCP16, W-DD-SCP1, W-DD-SCP2), Part 8 to Part 9, and the case names, and then makes the changes below. Nothing else in the template changes.

## How the rows run: bundles

- After the setup chat (S-SCP0 alone), the course is written in five chats (syllabus, section 5): W-SCP1 to W-SCP4; W-SCP5 to W-SCP8; W-SCP9 to W-SCP12; W-SCP13 to W-SCP16; W-DD-SCP1 and W-DD-SCP2 with the closing corrections.
- Every writing chat starts from one starter: `python3 kit/next_prompt.py --course supply-chain-planning --bundle 4`, worked in full. The preface and tail that `--bundle` prints apply unchanged: each unit closed, landed and published before the next begins; no question asked; the stop conditions as printed.
- Between units of one chat the next row's prompt is printed afresh, so a correction or flag raised by one unit reaches the next unit of the same chat (carry-forward rule, items 2 and 3).
- The one reply of a chat ends with the line above, not with a long prompt, unless a stop left something only the owner can decide.
- Carry-forward rule, item 7, for this course: the last chat works the closing corrections itself.
- Every prompt of this course opens with the plain line `Clone apcanario/learning (shallow, push access).` and says nothing else about cloning, attaching the repo or approval; the template's sentence that begins "Clone `apcanario/learning` (attach it with add_repo" is replaced by that line (the owner, 21 Nov 2026).
- No gate row and no hold for this course. Nothing is left for the owner by hand that an agent can do.
- Staleness checks: the five search-on units are checked in one chat when the last of them falls due.

## Writer rules that change (section 1 and the template's copy of it)

- Rule 4, grade every claim: by SCP1's key; and state the kind of evidence of every finding (forecasting competition, field experiment, laboratory experiment, simulation, single-company case study, survey) with its data, setting and year.
- Rule 5, vendors: worked product examples use Lathmoor, Ebbfield and Varnby Software.
- Rule 9, scope: replace "No AI features" with: no formula and no worked calculation: a method is given by what goes in, what comes out, what it assumes and when it fails; a quantity by what moves it and in which direction. Statistical, machine-learning and optimisation methods are treated on published evidence; nothing treats generative AI, assistants or agents, and a vendor's word "AI" is reported as the vendor's word. No interview framing. No craft method taught. Nothing about the Project's owner, his employer, his role or his work.
- Rule 10, the two closing sections: "In the planning meeting" and "Self-check".
- New rule, credentials: the source log records for every reference its kind of venue (peer-reviewed journal, academic or professional publisher's book, forecasting competition, association, analyst firm, audited filing, standards body, vendor) and any commercial interest its authors have in what they describe; a real company's practice comes only from a peer-reviewed or published account with named authors or its own audited filing.
- New rule, length: the 2,000 to 6,000 word guide covers the body; the deliverable is not counted.

## Fresh checker's passes that change (section 2 and step 4)

- The pass on grades also fails a finding whose kind of evidence is not stated, and a simulation or a model result presented as a field result.
- The pass on scope fails any formula or worked calculation, and fails a method that is only named, without what goes in, what comes out, what it assumes and when it fails.
- The pass on sources checks the venue and interest columns of the source log, and that no account written by the sellers of a method or co-written by a company about itself is cited without that label.
- The pass on the deliverable reads "In the planning meeting" where it read "On a site visit".
- It runs the unit against Part 9 line by line.

## This row in particular

| Row | Unit | Search | Paragraph for `{PARTICULAR}` |
|---|---|---|---|
| W-SCP1 | SCP1 | on | Search on. This unit sets the grade key, the list of kinds of evidence and the glossary that every later unit receives: define each grade so that two readers would agree, with one worked example per grade and per kind of evidence. The common claims are listed and marked with the unit that tests each; test here only what this unit opens. Log every analyst page as opened or refused (flag F2). |
| W-SCP2 | SCP2 | off | Search off. Sets the demand profile form that SCP3 and SCP6 reuse: fix its columns here. Keep demand, sales, orders and shipments apart in every sentence. |
| W-SCP3 | SCP3 | off | Search off. Claim Q1 belongs here. No formula: each method family by what goes in, what comes out, what it assumes and when it fails (flag F4). State each competition's data and year before any use of its result, and label any transfer to a company's own demand as the unit's inference. |
| W-SCP4 | SCP4 | off | Search off. Claims Q2 and Q3 belong here. No calculation of any measure: say what each rewards and hides. Where the literature is silent on the link from error to stock, say so. |
| W-SCP5 | SCP5 | off | Search off. Sets the role card form reused by SCP7, SCP9, SCP10, SCP11 and SCP14: fix its fields here. Claims Q4 and Q5 belong here. State the sample and setting of every field study before its findings; a laboratory experiment is called one. |
| W-SCP6 | SCP6 | off | Search off. Claims Q6 and Q7 belong here. The trade-off between service and stock is described by what moves it and in which direction, never computed (flag F4). |
| W-SCP7 | SCP7 | off | Search off. Claim Q8 belongs here. The store-ordering study and the record-inaccuracy study each have a specific sample and setting; state both before any use of their numbers. |
| W-SCP8 | SCP8 | off | Search off. Claims Q9, Q10 and Q11 belong here. Keep three kinds of evidence apart throughout: a model's result, a classroom experiment's, and industry data. This is the last unit of chat 2: after it the owner reads SCP1 to SCP8, and his starting the next chat is the go. |
| W-SCP9 | SCP9 | off | Search off. Claim Q12 belongs here: the demand-driven method is described from its authors' own account, labelled an interested party's, and set against the independent assessment, with its design. Requirements planning is a logic described in words; no grid is worked. |
| W-SCP10 | SCP10 | off | Search off. The published fast-fashion accounts name a real retailer: give the company as the papers give it, say who wrote them, and draw nothing about any software from them. Say where a practice is a retailer's and where a distributor's. |
| W-SCP11 | SCP11 | off | Search off. Claim Q13 belongs here. Most of the evidence is single-company cases and surveys: state the design of each before its finding. A maturity model is a claim; name who publishes it. |
| W-SCP12 | SCP12 | off | Search off. Claim Q14 belongs here and in SCP13. Point to the Supply Chain Execution course for order promising by the unit's title only if that unit is filed today; otherwise by course name (flag F6). Workarounds are sourced or labelled the unit's inference. |
| W-SCP13 | SCP13 | on | Search on. The first unit with a product map: it is Lathmoor's, from the case register. The real market appears as one dated list from the analyst report, every vendor alike, in the form flag F1 sets. Claims Q14 and Q15 belong here. |
| W-SCP14 | SCP14 | off | Search off. No new role is invented: a missing role is a flag. Claim Q15 belongs here too. Peer reviews are evidence of what reviewers say, with where any count was read (flag F7), and no product is named. |
| W-SCP15 | SCP15 | on | Search on. Claim Q16 belongs here. Real vendors appear as dated lists only. Every figure in the worked value case is marked fictional. Say plainly where no independent evidence of a planning system's results was found, and list what was searched. End the body with the questions for the reader's own sales and services colleagues. |
| W-SCP16 | SCP16 | off | Search off. The worked memo uses only public evidence and the case register; every figure marked fictional or sourced. |
| W-DD-SCP1 | DD-SCP1 | on | Search on. Start from the bibliography's published company accounts; read each in full or say only the abstract was read; replace any that will not open. State for each who wrote it and their interest. Look for published failures and say what was found. Name a software supplier once, as the account does, and draw nothing from it. |
| W-DD-SCP2 | DD-SCP2 | on | Search on. Every number in its source's own terms with sample, design and year. Corrections to earlier units found here go by the correction route. This is the course's last row: after it is closed, work every correction and flag still open in this same chat, by the correction route, and deliver a closing corrections prompt only if something remains open, saying why. |
