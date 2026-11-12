"""Print the paste-ready prompt of a public-course writing row (G-0, 11 Nov 2026; docs/public-courses.md).

python3 kit/next_prompt.py                 the next row: the first unit, in queue order, with no file in its vault
python3 kit/next_prompt.py --row W-PB3     that row
python3 kit/next_prompt.py --list          every row with its unit, search flag and whether it is filed
python3 kit/next_prompt.py --save          also write the prompt into the row's prompt cell in docs/BACKLOG.md
python3 kit/next_prompt.py --bundle 2      the next two rows in one unattended chat: the first row's prompt between a preface
                                           and a tail that has the chat print and work each following row after the one before is closed

The queue is course PB in its ORDER, then course BW in its ORDER (QUEUE below; reorder it there). Everything a prompt
names is read from the sources at the time it is printed: the course entry (kit/courses.py), the unit's title, search
flag and Takes line (the course's data folder), the source units those lines name (courses/brand-ai/), the units of the
course already filed, and the open flags of syllabus-flags.md that name the unit. One template, so every row is briefed
to the same standard and nothing drifts from chat to chat.
"""
import importlib.util, pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
sys.path.insert(0, str(R))
from courses import COURSES

QUEUE = ('personal-brand', 'building-with-ai')          # the courses, in the order their rows run
HOLDS = {'W-PB5': 'S-PB1'}   # a writing row that waits for a review row: while the review row is in the queue of docs/BACKLOG.md, no prompt runs past it (Pedro, 12 Nov 2026, 08:30)
SRC = ROOT / 'courses' / 'brand-ai'                      # the private source units
ACADEMY = 'https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH'
NOTES = {   # what one row needs beyond the template
    'DD-BW2': "Its records are staged by you, private details removed: copy into the packet the fresh-check reports of `audits/brand-ai/` and `audits/ux/` and the audit reports, each passed through a script that replaces every term of `kit/private-terms.txt` with `[removed]`; a record that still names its private subject after that (a unit title, a sentence about the owner) is left out and listed in the record. The writer takes nothing from outside the packet and the case file.",
    'DD-BW3': "Its source unit is a review of one person's own chats and is full of personal detail: tell the writer to carry over the method and the counts only, as `case-academy.md` §8 states them, and nothing that identifies the person, his projects or his tools.",
    'PB8': "Its second source unit is written for one country: tell the writer that only its structure and its platform-terms evidence carry over, and that no national rate, threshold or statute is stated as the reader's.",
    'BW4': "Its source unit audits the Learning Project itself: the writer takes the findings only as `case-academy.md` §7 states them. If the unit needs more of them, add them to the case file first, from the source unit, private terms removed, and say so in the record.",
}


def load(c):
    spec = importlib.util.spec_from_file_location('np_' + c['id'].replace('-', '_'), ROOT / c['data'])
    d = importlib.util.module_from_spec(spec); spec.loader.exec_module(d)
    return d


def rows():
    out = []
    for cid in QUEUE:
        c = next(x for x in COURSES if x['id'] == cid)
        d = load(c)
        sc = d.COURSES[0]
        units = {u[0]: u for u in sc['units']}
        filed = {}
        for f in sorted((ROOT / c['vault']).glob('*.md')):
            m = re.match(r'((?:DD-)?[A-Z]+\d+)-', f.name)
            if m: filed[m.group(1)] = f
        for code, model, search in d.ORDER:
            out.append(dict(row=f'W-{code}', code=code, c=c, d=d, sc=sc, unit=units[code], model=model, search=search,
                            filed=filed, order=[o[0] for o in d.ORDER]))
    return out


def hold(r):
    """The review row that holds writing row r, if that review row is still in the queue (above the Proposed section)."""
    h = HOLDS.get(r['row']) if r else None
    if not h: return None
    q = (ROOT / 'docs' / 'BACKLOG.md').read_text(encoding='utf-8').split('## Proposed')[0]
    return h if re.search(r'^\| ' + re.escape(h) + r' \|', q, flags=re.M) else None


def sources(takes):
    """The private source units a Takes line names: every code before the words 'as source material'."""
    head = takes.split('as source material')[0] if 'as source material' in takes else ''
    out = []
    for code in re.findall(r'\b((?:DD-)?[AB]\d+)\b', head):
        fs = sorted(SRC.glob(f'{code}-*.md'))
        if fs and fs[0] not in out: out.append(fs[0])
    return out


def flags(r):
    """Open rows of the course's syllabus-flags.md whose Affects cell names this unit, alone or inside a range."""
    f = (ROOT / r['c']['data']).parent / 'syllabus-flags.md'
    out, order = [], r['order']
    for ln in f.read_text(encoding='utf-8').splitlines():
        cells = [x.strip() for x in ln.strip().strip('|').split('|')]
        if len(cells) < 7 or not re.match(r'F\d+$', cells[0]) or cells[6] != 'open':
            continue
        aff, hit = cells[3], False
        for a, b in re.findall(r'((?:DD-)?[A-Z]+\d+) to ((?:DD-)?[A-Z]+\d+)', aff):
            if a in order and b in order and order.index(a) <= order.index(r['code']) <= order.index(b): hit = True
        if r['code'] in re.findall(r'(?:DD-)?[A-Z]+\d+', re.sub(r'(?:DD-)?[A-Z]+\d+ to (?:DD-)?[A-Z]+\d+', '', aff)): hit = True
        if hit: out.append(f'{cells[0]} ({cells[1]}, raised by {cells[2]}): {cells[4]}. Proposed: {cells[5]}.')
    return out


def rel(p):
    return pathlib.Path(p).relative_to(ROOT).as_posix()


def prompt(r, nxt):
    c, d, u, code = r['c'], r['d'], r['unit'], r['code']
    cid, data, vault = c['id'], (ROOT / c['data']).parent, c['vault']
    takes = d.AIMS[code][1]
    src = sources(takes)
    done = [r['filed'][x] for x in r['order'] if x in r['filed']]
    earlier = [x for x in r['order'][:r['order'].index(code)] if x not in r['filed']]
    fl = flags(r)
    case = ('`generator/data/personal-brand/case-facts.md` (Mara\'s register)' if cid == 'personal-brand'
            else '`generator/data/building-with-ai/case-academy.md` (the Academy case file)')
    on = r['search'] == 'on'
    P = []
    P.append(f"Clone `apcanario/learning` (attach it with add_repo, push access; one shallow clone with a generous timeout, about ten minutes; call `register_repo_root` if the session offers it; the repo has no CLAUDE.md). Row {r['row']} of `docs/BACKLOG.md`, in this chat: write, fresh-check and file unit {code}, \"{u[1]}\", of the public course {r['sc']['name']} (`kit/courses.py` entry `{cid}`: data `{rel(data)}/`, vault `{vault}/`, `docs/sourcing-standard.md` Parts 1 and {c['sourcing_part'][5:]}; search {r['search']}); correct every mistake the work finds; flag every contradiction or need that touches another unit; then build, verify, publish Academy once (the artifact, then GitHub Pages), push everything, close the row and end with the next row's prompt. Read first: `docs/public-courses.md` (the decisions and the eleven rules of these rows), `docs/method.md` §4, §5, §7 and §8, `skills/write-unit`, `skills/audit-units` §3b and `skills/file-unit`. The writer and the fresh checker are Opus 5.5 agents; the chat itself only stages, applies, files, builds, publishes and records (method §4, P31), and the record says which model the chat ran as. Commit and push after every step, on `main`. If the session's permission check refuses to run the repo's own scripts after the fresh clone, stop at once, say so in one line and ask Pedro to approve; never work around it. The safety check refuses an `rm -rf` whose target is a shell variable: use a literal absolute path, or do without the removal. Where a choice is open, take the most reasonable reading, say so in the record, and carry on; ask only if genuinely blocked. Fix every error, should-fix and minor finding the work turns up in this chat; a minor whose own Fix is \"no change required\" is recorded and not applied.")
    P.append("**1. Gate.** `python3 kit/next_prompt.py --list` shows this unit as the next one not filed"
             + (f" (it lists {', '.join(earlier)} as not filed: stop and say so, since the course is written in reading order)" if earlier else "")
             + ". No REWRITE verdict is open in `docs/courses-index.md`. The four-unit audits and the Fable 5.1 fresh checks are owed to the Fable stage (Pedro, 11 Nov 2026) and gate nothing.")
    packet = [f"`brief.txt`, built by script with `kit/mdcourse.py`'s `open_brief(d, sc, u)` from `{rel(data)}/hub.py` (the preamble, the Aim, Takes and Gives lines, the unit brief; never reworded, never retyped)",
              "`skills/write-unit/SKILL.md`", f"`docs/sourcing-standard.md` Parts 1 and {c['sourcing_part'][5:]}", "the figure kinds (`kit/viz.py`'s docstring and `VIZ_KEYS`)", case]
    if src:
        packet.append("the source units its Takes line names, each with its fresh-check report from `audits/brand-ai/` where one exists: " + ', '.join(f'`{rel(f)}`' for f in src))
    else:
        packet.append("no source unit of the private course (its Takes line names none); the files that line does name")
    packet.append("every unit of this course already filed: " + (', '.join(f'`{rel(f)}`' for f in done) if done else 'none yet'))
    packet.append("`flags.txt`: " + ("the open syllabus flags that name this unit, as printed below" if fl else "empty (no open flag names this unit)"))
    P.append("**2. Stage the writer's packet** in one folder outside the repo, by script, so that what the writer read is a path check: " + '; '.join(packet) + ".")
    if fl:
        P.append("Open flags that name this unit (from `syllabus-flags.md`; the writer deals with each and says how in its notes):\n" + '\n'.join(f'- {x}' for x in fl))
    if code in NOTES:
        P.append("**This row in particular.** " + NOTES[code])
    P.append(f"**3. The writer.** One fresh Agent on model opus, isolated, that sees only its folder. It states its model in its first line; if that is not claude-opus-5-5, stop at once, change nothing and say so in one line (Pedro may accept the model the session gave; the record then names it). Tell it: a memory snapshot, project instructions or anything of that kind in its context is not a source and must not be used; it uses no memory, past-chat, Projects, connector, Artifact or Agent tool and no `mcp__` tool; it publishes nothing; "
             + ("search is on: it searches before writing and dates every fact that can change; " if on else "search is off: it writes from the packet and its knowledge and searches only to re-verify a carried claim or a specific doubtful point; ")
             + "the web rule holds (WebSearch first; WebFetch only a URL that a search in the same agent returned verbatim, never one typed, printed in a file, edited or reached by a redirect; a refused, redirected or timed-out fetch is \"not checked\" and is never retried or fetched from a copy); it re-verifies at its source every claim it carries over from a source unit, and anything it could not re-verify goes on the unsure list or stays out; it follows `skills/write-unit` §4 to §5, renders every figure before handing in, and writes as it goes, so a restart loses little: `out/unit.md` (front matter, the unit, the deliverable, Sources), `out/unsure.md` (up to ten claims, then the `Object:` line) and `out/notes.md` with three lists, each item naming the unit codes it touches: **Source errors** (every mistake found in a source unit: the quoted text, what is wrong, the source that shows it, the exact replacement), **Contradictions** (where this unit's evidence disagrees with a filed unit of this course or with the brief of an unwritten one, read on the course's Briefs data in the packet) and **Needs** (what the unit needed that the syllabus does not give, and what a later unit must now cover or avoid). An empty list is written as \"none\".")
    P.append(f"**4. The fresh check.** A separate fresh Agent on model opus that has not seen the writing, under the same agent rules, with live search: the prompt of `skills/audit-units` §3b with its figures paragraph, filled from the course's entry, on a packet of the unit, its brief, the sourcing parts, {case.split(' (')[0]} and the writer's `notes.md`. It also (8) verifies each item of the writer's Source errors list against the source named (confirmed / not confirmed), (9) runs the unit against the course's part of the sourcing standard line by line, and (10) reads the unit as the persona in the preamble would and says where it assumes something only the private course's reader would know. Before any fix, save its final report verbatim as `audits/{cid}/fresh-check-{code}.md` with the front matter `audits/README.md` sets out; the unit's unsure list gains the fresh-check line, which says a Fable 5.1 fresh check is owed (P49). A `rewrite` verdict sends the unit back to a new writer from the same brief, once; a second `rewrite` stops the row with a note of where it stopped.")
    P.append("**5. Apply.** Verify each finding against the unit before applying it, as an exact replacement by script (each Current counted once, taken from the saved report by script). A figure that fails is fixed and re-checked by a new agent from the unit's text without its figures, the captions and the frames `verify.py --shots` saves, as many times as it takes; figures are never dropped (Pedro, 3 Nov 2026). Restarts: when the harness says it is resuming an agent, let it and say so in the record; if an agent is lost, re-run it from the start once; if lost again, start a fresh agent on the same packet that resumes from the lost run's working files. Look for agent transcripts (`.jsonl` under `/root/.claude/` or `/tmp/`); where there are some, check by script that each agent used no tool it was denied and read nothing outside its folder, and take its `\"model\"` field; where there are none, say so, and the model is the one the agent stated.")
    P.append(f"**6. Mistakes elsewhere.** Every confirmed Source error is corrected where it sits: an exact replacement in the private unit under `courses/brand-ai/`, a dated note in that unit (\"Erratum <date>, found by {code}'s writer\"), a `CHANGELOG` row and a `VERSION` bump in `generator/data/brand-ai/hub.py`. A mistake the work finds in a filed unit of this course is fixed the same way in `{rel(data)}/hub.py`. An item the checker did not confirm is recorded and not applied. Each correction is one line in the reply.")
    P.append(f"**7. Syllabus flags.** Append every Contradiction and Need to `{rel(data)}/syllabus-flags.md` as a new row (next number, date, raised by {code}, the units affected, the flag, the proposed change, status open); set to `carried` each flag this unit was given and dealt with. Change no brief: `units_data.py` is edited only by a syllabus review that Pedro confirms (`docs/public-courses.md` §3, rules 6 and 7). If a flag means the next unit cannot be written as briefed, say so in the first line of the reply and write, as the next prompt, a syllabus-review prompt in place of the unit's.")
    P.append(f"**8. File** per `skills/file-unit` §1, §2, §4, §5 and §6: front matter (model: the model the writer stated); `{vault}/{code}-<slug>.md`; in `{rel(data)}/hub.py` the `READINGS` entry (its intro says what the unit is, how it was made and its known gaps, with no private term), `STATUS`, `NEXT_UNIT`, `VERSION` and a `CHANGELOG` row; "
             + ("append to `case-facts.md` every fact the unit set about Mara, with its section, and what it left free; " if cid == 'personal-brand' else "add to `case-academy.md`, from the Project's records and with private details removed, any fact the unit's Needs list asked for and the records hold; ")
             + f"`docs/courses-index.md` (the row with the fresh-check path, the count line, the counter, a staleness row if search is on) until `python3 kit/index_check.py` matches; `python3 kit/private_terms.py` prints OK (a hit is fixed in the unit, never in the list). No relief until row G-R: keep the writer's `Object:` line in the changelog row.")
    P.append("**9. Build and verify.** `cd kit && python3 build.py` (about five minutes; read its last line, since a build that stops leaves the site stale), then `python3 verify.py` (ALL CHECKS PASSED; read every FAIL line), then `python3 verify.py --shots <dir> --page read-" + code.lower() + "` (check the id it prints) and look at the page's shots at phone and desktop, dark and light, and at every figure's frames. A layout fault is fixed in `design/theme.css` (then `cp design/theme.css kit/shell.css`) or `kit/viz.py`, never in a page.")
    P.append(f"**10. Publish Academy once.** Before the build you publish, move the row to `docs/CHANGELOG.md`, set the backlog's \"Next up\" line and save the next prompt in its row (step 11), so the published Backlog and Changelog pages are current. Read the artifact {ACADEMY} first and compare the live page with the build you started from (`get_artifact` for the live version id; `list_files` for every file's sha256 against `sha256sum` of the start build's files, which are the `kit/academy/` of the commit you cloned). `publish_files` patches (a republish changes only the files it names) and refuses a shell that does not begin with a doctype: send the files that differ from the start build, found by script, and the shell inside the wrapper the live page carries (its first line and its closing `</body></html>`, taken from the saved live shell by script into a copy outside the repo), with `slug`, `base_version` and mode patch; then read the sent files back and compare their sha256 with the build; never a new artifact, never forced. Then `./deploy.sh` once: attach `apcanario/academy` with add_repo (if refused, carry on and ask Pedro once at the end), clone it once, set `ACADEMY_DIR` to the clone, and confirm with `gh run` that the deployment of the new build succeeded. The publish and deploy identifiers go into the records after the publish, committed without republishing.")
    P.append("**11. Close** per `docs/method.md` §8, steps 1 to 5: the row done and moved to `docs/CHANGELOG.md` with the date, the models and a one-line result; `kit/CHANGELOG.md` gets its session entry; a task the work uncovered that this chat cannot do is a new row marked *proposed* (a syllabus review, if a flag asks for one, is such a row); the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` rewritten from `docs/`, and every changed Project knowledge file re-uploaded with the Projects tool (`courses-index.md`, the course's `hub.py` and `syllabus-flags.md`, the unit; read each existing path with `project_read` first, then write it from its repo file with `local_path`). The next prompt is not written by hand: `python3 kit/next_prompt.py --save` prints the prompt of the next unit not filed"
             + (f" ({nxt['row']}, unit {nxt['code']})" if nxt else " (none is left: the next row is G-R, the reliefs of both public courses, and its prompt is written to the standard of this one)")
             + " and saves it in that row of `docs/BACKLOG.md`; run it after filing and before the final build."
             + (f" Here the next row is {hold(nxt)}, the review that holds {nxt['row']}: its prompt is already saved in its row, so `--save` is not run; set the backlog's \"Next up\" line to {hold(nxt)} and give its saved prompt at the end of the reply." if hold(nxt) else ''))
    P.append("**Reply:** what was filed where (words, figures, search used or not); the fresh-check verdict and counts; each mistake corrected, in a line, with the file it was in; each flag raised, with the units it affects and whether it blocks the next unit; the private-terms result; verify's result; the publish and the deploy; the choices taken; the backlog hand-off (row done, proposed rows, next up); then the next prompt in a code block.")
    return '\n\n'.join(P)


def save(row, text):
    p = ROOT / 'docs' / 'BACKLOG.md'
    lines = p.read_text(encoding='utf-8').split('\n')
    starts = [i for i, ln in enumerate(lines) if ln.startswith(f'| {row} |')]
    if len(starts) != 1:
        raise SystemExit(f'{row}: {len(starts)} rows in docs/BACKLOG.md, expected one')
    i = starts[0]
    j = i
    while not lines[j].rstrip().endswith('|'):      # a saved prompt spans lines up to the one that closes the cell
        j += 1
    cells = lines[i].split(' | ')
    head = ' | '.join(cells[:3])
    lines[i:j + 1] = (head + ' | ' + text + ' |').split('\n')
    p.write_text('\n'.join(lines), encoding='utf-8')


if __name__ == '__main__':
    rs = rows()
    if '--list' in sys.argv:
        for r in rs:
            print(f"{r['row']:10} {r['code']:7} search {r['search']:3} {'filed' if r['code'] in r['filed'] else 'not filed'}  {r['unit'][1]}")
        sys.exit(0)
    if '--row' in sys.argv:
        want = sys.argv[sys.argv.index('--row') + 1]
        k = next((i for i, r in enumerate(rs) if r['row'] == want), None)
        if k is None: raise SystemExit(f'no row {want}')
    else:
        k = next((i for i, r in enumerate(rs) if r['code'] not in r['filed']), None)
        if k is None: raise SystemExit('every public unit is filed; the next row is G-R')
        if hold(rs[k]): raise SystemExit(f"{rs[k]['row']} waits for {hold(rs[k])}: run that row first (its prompt is saved in its row of docs/BACKLOG.md)")
    nxt = next((r for r in rs[k + 1:] if r['code'] not in r['filed']), None)
    text = prompt(rs[k], nxt)
    if '--bundle' in sys.argv:      # several rows in one unattended chat (method §4, P31): this row's prompt between a preface and a tail
        n = int(sys.argv[sys.argv.index('--bundle') + 1])
        todo = []
        for r in [r for r in rs[k:] if r['code'] not in r['filed']]:
            if len(todo) == n or (todo and hold(r)): break
            todo.append(r)
        if len(todo) > 1:
            names = ', then '.join(f"{r['row']} (unit {r['code']})" for r in todo)
            after = next((r for r in rs[rs.index(todo[-1]) + 1:] if r['code'] not in r['filed']), None)
            pre = (f"This chat runs {len(todo)} rows one after the other, unattended (Pedro is away; method §4, P31): {names}. "
                   "Work the first exactly as its prompt below says, to the end of its step 11: filed, built, verified, published to the artifact, deployed to Pages, pushed, its row closed. "
                   "Each unit ends published before the next begins, so a failure later in the night strands nothing. Never ask a question: where the prompt says ask, take the most reasonable reading and record it; "
                   "where it says stop (the permission check refuses the repo's scripts; a writer or checker states a model that is not claude-opus-5-5; a second `rewrite`; a flag that blocks the next unit), stop there, leave what is finished published and pushed, and say in the first line of the reply which row stopped and why. "
                   "Do not write the first row's reply; go on.")
            tail = (f"**Then the next row{'s' if len(todo) > 2 else ''}, in this same chat.** After each row is closed, run `python3 kit/next_prompt.py --row <the next row>` ("
                    + ', '.join(r['row'] for r in todo[1:]) + ") and work what it prints in full, the same way: a new packet folder, a new writer and a new checker, each a fresh agent that has seen nothing of the earlier unit but its filed file; "
                    "the start build for its publish is the build the row before published; clone nothing again. "
                    f"After {todo[-1]['row']} is closed, stop. The next prompt, saved in its row and given at the end of the one reply, is "
                    + (f"the prompt already saved in row {hold(after)} of `docs/BACKLOG.md` (the review that holds {after['row']}; do not run `--bundle`)" if hold(after) else f"`python3 kit/next_prompt.py --bundle {n} --save` (from {after['row']})" if after else "the prompt of row G-R, written to the standard of this one")
                    + ". **One reply for the whole chat:** per row, what its own Reply paragraph asks, under the row's name; then the backlog hand-off and the next prompt in a code block.")
            text = pre + '\n\n' + text + '\n\n' + tail
    if '--save' in sys.argv:
        save(rs[k]['row'], text)
    print(text)
