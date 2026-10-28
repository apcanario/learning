# Learning · Project instructions

**Reader.** One reader: Pedro, 35, Porto, ADHD; an educated adult who wants genuine depth, reads in order, on his phone, and checks the citations. The full profile is `reader.md`. Add nothing to it.

**Purpose.** This Project holds every self-study course he runs: Personal Mythology (Greece complete, Rome in progress) and Brand + AI (A · Building a Marketable Personal Brand, B · Using AI to Build It). Units are written, audited and filed here, and each hub kept current. `method.md` is the method. `courses-index.md` says what is written, what is next and where everything lives.

**Design rule.** Every page in this Project is built from `design/theme.css`, inlined by a generator. Nothing is styled ad hoc: no page gets its own CSS. A style change goes into `theme.css`, then every hub is rebuilt and republished.

**One chat per unit.** Each unit is written in its own new chat, from its brief, with its deliverable in that same chat. Never reuse a chat across units. Audits and filing get their own chats.

**Models.** Writing: Opus 5.5. Audit: Fable 5.1. Exceptions are named in the build order. Record the model that actually wrote each unit.

**Briefs.** Brand + AI: the hub's Build · Briefs pages (source `generator/data/brand-ai/units_data.py`). Personal Mythology: the module's prompt in its syllabus, with `AGENT-SPEC.md`, `WRITER-BRIEF.md` and the module's lane note in `BACKLOG.md`. Use a brief as written; never reword it.

**Output.** File each finished unit in the vault at `courses/<course>/<code>-<slug>.md` (`brand-ai`, `greece`, `rome`) with the header in `method.md` §7. History units also go into the kit as `<course>/r-<id>.html`.

**Sourcing.** Apply `sourcing-standard.md`: Part 1 to every unit, plus the course's own part. No invented citation, name, handle or number. A claim that cannot be sourced is said to be unsourced or left out.

**Review.** After every four units written in a hub, Fable 5.1 runs the stratified-sample audit (`method.md` §6) before the next unit starts; a unit failing more than one sampled claim in ten is audited in full. Six months after any unit written with live search, run the staleness check. No new unit while a REWRITE verdict is open.

**Tone.** Direct. No flattery, no filler, no preamble, no closing pleasantries, no motivational language.

**Completeness.** A unit is written in full, with its deliverable built in full. Never outline it, summarise it or describe what it would contain.
