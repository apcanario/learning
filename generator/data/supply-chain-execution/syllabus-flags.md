# Syllabus flags: Supply Chain Execution for Product Teams

Raised by the chats that write this course's units. A flag is a contradiction between units or briefs, or a need the syllabus does not meet. A brief is never reworded by the chat that raises a flag: a flag that would change a brief waits for a syllabus review that the Project's owner confirms. `kit/next_prompt.py` passes every open flag that names a unit to that unit's writer.

Status: open (not yet acted on), carried (the named unit's writer was given it and its unit deals with it), resolved (a syllabus review changed a brief or decided not to), dropped.

| # | Date | Raised by | Affects | Flag | Proposed change | Status |
|---|---|---|---|---|---|---|
| F1 | 19 Nov 2026 | S-SCE0 | SCE6, SCE8, SCE9, SCE16, SCE17 | `kit/private_terms.py` passes the owner's employer on this course's pages only as an entry of a dated list: a Markdown list, or a table, that follows a lead-in line naming the analyst firm, the report or the filing, and a year (for example "The vendors named in Gartner's Magic Quadrant for Warehouse Management Systems, 29 April 2026, read in abstract:"). Anywhere else on the page, the employer's name fails the build. Any other company on the private-terms list fails everywhere, list or not, so a dated list that names one cannot be given whole. | Each unit that gives a dated vendor list writes it in that form, every vendor alike; if the list names a company the private-terms check fails outside the employer rule, the writer leaves the list out, says that the list could not be reproduced here, cites where to read it, and raises a flag for the Project's owner. No brief changes. | open |
