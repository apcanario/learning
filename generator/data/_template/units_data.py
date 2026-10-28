# Units for a new course hub. Copy this folder to data/<course-slug>/ and replace every ⟨…⟩.
# PRE is the shared preamble baked into every open brief; {GOAL} is replaced by the course goal.
# Each unit: (code, title, one-line scope, what it ships, brief). 8–10 core units plus 2 or 3 deep dives (DD-), written last. A brief that starts with
# "WRITTEN" is a note for the brief page only: a unit is written when its file is filed in courses/<slug>/ (A5).
PRE = ("Write one unit of a self-study course ⟨format: e.g. a long-form report for one reader⟩. "
"Length is whatever the topic needs; do not pad and do not cut to a target. "
"Reader: ⟨copy from reader.md; add nothing⟩. "
"Tone: direct, no flattery, no filler. "
"Course goal: {GOAL} "
"Sourcing standard: ⟨copy the course's lines from sourcing-standard.md⟩. "
"Where the unit depends on current facts, search before writing and date the facts. "
"End with the unit's deliverable, built out in full, not described.")

A = [
("A1", "⟨Unit title⟩",
 "⟨One-line scope.⟩",
 "⟨deliverable⟩",
 "Unit A1, ⟨Title⟩. Cover: ⟨items⟩. Deliverable: ⟨the artefact, built in full⟩."),
("A2", "⟨Unit title⟩",
 "⟨One-line scope.⟩",
 "⟨deliverable⟩",
 "Unit A2, ⟨Title⟩. Search before writing. Cover: ⟨items⟩. Deliverable: ⟨the artefact⟩."),
("DD-A1", "Deep dive: ⟨title⟩",
 "⟨One-line scope.⟩",
 "⟨deliverable⟩",
 "Deep dive A1, ⟨Title⟩. Written last. Cover: ⟨items⟩. Deliverable: ⟨the artefact⟩."),
]
