"""Print the paste-ready prompt of a public-course writing row (G-0, 11 Nov 2026; docs/public-courses.md).

python3 kit/next_prompt.py                 the next row: the first unit, in queue order, with no file in its vault
python3 kit/next_prompt.py --row W-PB3     that row
python3 kit/next_prompt.py --list          every row with its unit, search flag and whether it is filed
python3 kit/next_prompt.py --save          also write the prompt into the row's prompt cell in docs/BACKLOG.md
python3 kit/next_prompt.py --bundle 2      the next two rows in one unattended chat: the first row's prompt between a preface
                                           and a tail that has the chat print and work each following row after the one before is closed

The queue is course PB in its ORDER, then course BW in its ORDER (QUEUE below; reorder it there). Everything a prompt
names is read from the sources at the time it is printed: the course entry (courses/<id>/course.toml), the unit's title, search
flag and Takes line (the course's data: kit/pack.py), the source units those lines name (courses/brand-ai/), the units of the
course already filed, the open flags of syllabus-flags.md that name the unit, and the rows of the Corrections section of
docs/BACKLOG.md, which every prompt works first (step 1b). Every proposal a chat raises is dealt with in that chat (step 7b;
Pedro, 12 Nov 2026, 21:31). One template, so every row is briefed
to the same standard and nothing drifts from chat to chat. A course with `prompts_doc` in its courses/<id>/course.toml (S-SP0, 16 Nov 2026:
sport-psychology, docs/sport-psychology-prompts.md) keeps its own template in that document; prompt_doc fills its slots.
S-SCE0 (19 Nov 2026): supply-chain-execution, rows W-SCE1 to W-DD-SCE2, from docs/supply-chain-execution-prompts.md; a
template with no safety reader is allowed; a row in GATES opens with a line saying it waits for its gate row while that
row is still in docs/BACKLOG.md.
"""
import importlib.util, pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
sys.path.insert(0, str(R))
from courses import COURSES
import pack

QUEUE = ('personal-brand', 'building-with-ai', 'sport-psychology', 'supply-chain-execution')   # the courses, in the order their rows run (S-SP0, 16 Nov 2026: rows W-SP1 to W-DD-SP3 come from the hub's ORDER; S-SCE0, 19 Nov 2026: rows W-SCE1 to W-SCE18, W-DD-SCE1, W-DD-SCE2)
HOLDS = {'W-PB5': 'S-PB1', 'W-SP4': 'R-SP1'}   # a writing row that waits for a review row: while the review row is in the queue of docs/BACKLOG.md, no prompt runs past it (Pedro, 12 Nov 2026, 08:30)
GATES = {'W-SCE7': 'P-SCE6'}   # S-SCE0: a row printed while its gate row (a task for Pedro, under Proposed) is still in docs/BACKLOG.md opens with a line saying it is not to be run until he has closed it
SRC = ROOT / 'courses' / 'brand-ai'                      # the private source units
ACADEMY = 'https://claude.ai/artifact/WwmQpUSqAUJvrcmLczppEH'
NOTES = {   # what one row needs beyond the template
    'DD-BW2': "Its records are staged by you, private details removed: copy into the packet the fresh-check reports of `audits/brand-ai/` and `audits/ux/` and the audit reports, each passed through a script that replaces every term of `kit/private-terms.txt` with `[removed]`; a record that still names its private subject after that (a unit title, a sentence about the owner) is left out and listed in the record. The writer takes nothing from outside the packet and the case file.",
    'DD-BW3': "Its source unit is a review of one person's own chats and is full of personal detail: tell the writer to carry over the method and the counts only, as `case-academy.md` §8 states them, and nothing that identifies the person, his projects or his tools.",
    'PB8': "Its second source unit is written for one country: tell the writer that only its structure and its platform-terms evidence carry over, and that no national rate, threshold or statute is stated as the reader's.",
    'BW4': "Its source unit audits the Learning Project itself: the writer takes the findings only as `case-academy.md` §7 states them. If the unit needs more of them, add them to the case file first, from the source unit, private terms removed, and say so in the record.",
}


def load(c):
    return pack.load(c)                 # S-DEC2: the course's pack


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


def corrections():
    """The rows of docs/BACKLOG.md's Corrections section: corrections to filed units or records that the next prompt works
    before its unit (Pedro, 12 Nov 2026, 21:22: a proposed correction is corrected in the following prompt)."""
    t = (ROOT / 'docs' / 'BACKLOG.md').read_text(encoding='utf-8')
    if '## Corrections' not in t: return []
    sec = t.split('## Corrections', 1)[1].split('\n## ', 1)[0]
    out = []
    for ln in sec.split('\n'):
        if not ln.startswith('| ') or ln.startswith('| #') or ln.startswith('|---'): continue
        cells = [x.strip() for x in ln.strip().strip('|').split(' | ')]
        out.append((cells[0], cells[1]))
    return out


def carried():
    """The rows of docs/BACKLOG.md's Carried proposals section: every proposal a chat raised and listed in its reply (standing rule,
    Pedro, 15 Nov 2026: proposals carry on unless he removes them). Each is appended to the next prompt and worked in that chat."""
    t = (ROOT / 'docs' / 'BACKLOG.md').read_text(encoding='utf-8')
    if '## Carried proposals' not in t: return []
    sec = t.split('## Carried proposals', 1)[1].split('\n## ', 1)[0]
    out = []
    for ln in sec.split('\n'):
        if not ln.startswith('| ') or ln.startswith('| #') or ln.startswith('|---'): continue
        cells = [x.strip() for x in ln.strip().strip('|').split(' | ')]
        out.append((cells[0], cells[1], cells[2] if len(cells) > 2 else ''))
    return out


def sources(takes):
    """The private source units a Takes line names: every code before the words 'as source material'."""
    head = takes.split('as source material')[0] if 'as source material' in takes else ''
    out = []
    for code in re.findall(r'\b((?:DD-)?[AB]\d+)\b', head):
        fs = sorted(SRC.glob(f'{code}-*.md'))
        if fs and fs[0] not in out: out.append(fs[0])
    return out


def flags(r):
    """Open and carried rows of the course's syllabus-flags.md whose Affects cell names this unit, alone or inside a range.
    A carried row is passed too (Pedro, 17 Nov 2026): it was carried by an earlier unit, and a unit not yet written that it
    names still has to follow it (F8, the grade key; F14, the interim rule-2 grading)."""
    f = pack.data_dir(r['c']) / 'syllabus-flags.md'
    out, order = [], r['order']
    for ln in f.read_text(encoding='utf-8').splitlines():
        cells = [x.strip() for x in ln.strip().strip('|').split('|')]
        if len(cells) < 7 or not re.match(r'F\d+$', cells[0]) or cells[6] not in ('open', 'carried'):
            continue
        aff, hit = cells[3], False
        for a, b in re.findall(r'((?:DD-)?[A-Z]+\d+) to ((?:DD-)?[A-Z]+\d+)', aff):
            if a in order and b in order and order.index(a) <= order.index(r['code']) <= order.index(b): hit = True
        if r['code'] in re.findall(r'(?:DD-)?[A-Z]+\d+', re.sub(r'(?:DD-)?[A-Z]+\d+ to (?:DD-)?[A-Z]+\d+', '', aff)): hit = True
        if hit: out.append(f'{cells[0]} ({cells[1]}, raised by {cells[2]}{", carried" if cells[6] == "carried" else ""}): {cells[4]}. Proposed: {cells[5]}.')
    return out


QR = 'Quality review'   # a flag row whose text starts so records the quality-review rule (Pedro, 17 Nov 2026, 21:38)


def _flag_rows(r):
    f = pack.data_dir(r['c']) / 'syllabus-flags.md'
    out = []
    for ln in f.read_text(encoding='utf-8').splitlines():
        cells = [x.strip() for x in ln.strip().strip('|').split('|')]
        if len(cells) >= 7 and re.match(r'F\d+$', cells[0]): out.append(cells)
    return out


def _names(aff, unit, order):
    for a, b in re.findall(r'((?:DD-)?[A-Z]+\d+) to ((?:DD-)?[A-Z]+\d+)', aff):
        if a in order and b in order and unit in order and order.index(a) <= order.index(unit) <= order.index(b): return True
    return unit in re.findall(r'(?:DD-)?[A-Z]+\d+', re.sub(r'(?:DD-)?[A-Z]+\d+ to (?:DD-)?[A-Z]+\d+', '', aff))


def quality(r):
    """The quality-review rule (docs/public-courses.md §3 rule 13; Pedro, 17 Nov 2026, 21:38): a unit named by more than 5 flags
    raised before it was written, or by more than 8 counting those raised before and after, is reviewed for quality. Rows whose
    flag starts with 'Quality review' are the rule's own records and are not counted; a resolved one restarts the count after it.
    Returns (before count for this row's unit, [(filed unit, before, total) over a threshold])."""
    rows, order = _flag_rows(r), r['order']
    def counts(u):
        last = max([int(c[0][1:]) for c in rows if c[4].startswith(QR) and c[6].startswith('resolved') and _names(c[3], u, order)] or [0])
        hit = [c for c in rows if not c[4].startswith(QR) and int(c[0][1:]) > last and _names(c[3], u, order)]
        raised = lambda c: re.match(r'(?:DD-)?[A-Z]+\d+', c[2]).group(0) if re.match(r'(?:DD-)?[A-Z]+\d+', c[2]) else ''
        before = [c for c in hit if raised(c) in order and u in order and order.index(raised(c)) < order.index(u)]
        return len(before), len(hit)
    mine = counts(r['code'])[0]
    over = []
    for u in order:
        if u in r['filed']:
            b, n = counts(u)
            if b > 5 or n > 8: over.append((u, b, n))
    return mine, over


def quality_text(r):
    mine, over = quality(r)
    code, cid = r['code'], r['c']['id'] if 'id' in r['c'] else 'sport-psychology'
    if mine <= 5 and not over: return ''
    s = ("**Quality-review rule** (Pedro, 17 Nov 2026, 21:38; `docs/public-courses.md` §3 rule 13): a unit named by more than 5 flags "
         "raised before it is written, or by more than 8 counting those raised before and after, is reviewed for quality, and the rule is "
         "recorded as a flag row whose text begins \"Quality review\" (open until the review is done, then resolved; a resolved row restarts the count). "
         "A quality review is one fresh Agent on model opus, under step 3's agent rules, with live search, not shown the writing, any earlier check "
         "or this chat's reasoning: it runs step 4's seven passes on the whole unit as it now stands, checks the brief and the deliverable are met "
         "in full and every flag the unit was given is dealt with, and lists every claim it could not verify; its report is saved verbatim as "
         "`audits/<course>/quality-review-<code>-<date>.md` before anything is applied; its findings are applied under step 1b's limits; what it "
         "could not verify is cut or marked unverified in the unit, never left silent.")
    if mine > 5:
        s += (f" **{code}** is named by {mine} flags raised before it is written: after step 5 and before step 8, run that review on {code} as "
              f"corrected, apply its findings as step 5 says, and set its \"Quality review\" flag row to resolved (add one if none is open).")
    for u, b, n in over:
        s += (f" **{u}** (filed) is named by {b} flags raised before it was written and {n} in all: run that review on it at step 1b, with the "
              f"corrections, and set its \"Quality review\" flag row to resolved.")
    s += (" At step 7, after this unit's flags are appended, count again with `python3 kit/next_prompt.py --quality`; for every unit newly over "
          "a threshold add an open \"Quality review\" flag row, so the next prompt carries its review.")
    return s


def rel(p):
    return pathlib.Path(p).relative_to(ROOT).as_posix()


LIMITS = ("Work them under these limits, so a correction adds no new error and the chat keeps to its unit. "
          "(a) **Scope.** Only the text a correction names changes, and only as far as it says; no new claim, source or section is added beyond what it cites. "
          "(b) **Check before applying.** One fresh Agent on model opus, under the agent rules of step 3, with live search and the web rule, not shown this chat's reasoning, gets a packet staged by script: the corrections; every filed unit they touch or name; each source they cite (as URLs to search for, never as text); the brief, built with `open_brief`, of every unit they touch and of every unwritten unit whose brief names the changed text, rule or figure; the `syllabus-flags.md` rows they name; the course's register. For each change it returns: the exact Current, which must occur once; the exact replacement; PASS or FAIL against the source, quoting it; and **Syllabus**: whether the change contradicts a brief, a filed unit or the register, or changes something a later brief relies on (quote the brief). It states its model first; if it is not claude-opus-5-5, stop as step 3 says. Save its report verbatim (the chat saves the text the agent returns if the harness refuses it a report file) as `audits/<course>/corrections-<date>-<codes>.md` before anything is applied. "
          "(c) **Apply** only a change that passed with no syllabus conflict, by script, as an exact replacement, with a dated note in the unit (\"Correction <date>, found by <who>\") and a `CHANGELOG` row in its hub; a changed figure is re-checked as step 5 says; a flag the change resolves is set to resolved. "
          "(d) **Do not apply** a change that failed, that needs a brief changed, or that would contradict another filed unit or the register: record it, and add it to `syllabus-flags.md` as a flag for the next syllabus review (rule 7); briefs change only there. "
          "(e) A correction with no content claim (a record or a mirror to refresh) is made as it is written, without the check. "
          "(f) Anything new the check turns up is worked the same way, in a second round, in this chat; only what is still open after that, or what a stopped row leaves, goes into the Corrections section for the next prompt.")


THIN_CHAT = ("**This is a thin main chat** (S-BW1, 15 Nov 2026; method §4: the point is to save the main chat's tokens). "
             "(1) The chat of a writing row runs on Sonnet 5.5 and the record says which model it ran as; a different model is recorded and the row carries on. Course design and syllabus chats run on Fable. The writer, the fresh checker, the applier, the filer and the corrections checker are each a fresh Agent on model opus, isolated on a packet. "
             "(2) The chat never opens a unit, a source unit, a report or a brief. It stages each packet with `python3 kit/thin.py stage <writer|checker|applier|filer> --row <row> <folder>`, launches the agent, and reads only the agent's reply, which the agent is told to keep to six lines at most (its model, what it wrote, its counts), and the `out/stats.json` that `python3 kit/thin.py stats <out folder>` writes by counting the agent's files. Every agent writes its full output to files in its `out/` folder. "
             "(3) Every step that needs judgement is an agent of its own: the **applier** (given the unit, the fresh-check report and the `fixes.json` that `thin.py fixes` makes from it, it verifies each finding against the unit and the cited source line and writes `out/apply.json`, a list of `{id, decision: apply|hold, reason}`; `python3 kit/thin.py apply` then applies it, each Current counted once, the unit left unchanged if one fails), the **corrections checker** (step 1b and 7b) and the **filer** (given the filed unit, its notes and the flags file, it writes `out/records.json`, shaped as `records.template.json` shows; `python3 kit/thin.py insert` inserts it into `hub.py`, the case or register file, `syllabus-flags.md`, `docs/courses-index.md` and both changelogs, restoring every file if anything fails). "
             "(4) Scripts, not the chat, check the result: `kit/index_check.py`, `kit/private_terms.py`, the last line of `build.py`, `verify.py` (ALL CHECKS PASSED) and the publish read-back by sha256. "
             "(5) A checkpoint commit follows every agent's return. "
             "(6) Units are not mirrored into the Project (Pedro, 15 Nov 2026): the chat uploads no unit.")
TRIAL = (" **Trial (S-BW1 rule 6):** this row is the first run of the thin chat. It passes if `verify.py` and `index_check.py` pass and the chat leaves no correction row; if it fails, say so in the reply and the next prompt runs on Opus 5.5 with rules (2) to (5) kept.")

def doc_parts(c):
    """S-SP0 (16 Nov 2026): a course whose rows' prompts are kept in a document (`prompts_doc` in its courses/<id>/course.toml) has there
    the writing template (the code block under "## Rows W-"), the safety reader (the code block under "### The safety reader",
    added as step 5b to the rows the table names) and the table "This row in particular" (row -> paragraph)."""
    t = (ROOT / c['prompts_doc']).read_text(encoding='utf-8')
    block = lambda head: re.search(r'(?m)^' + re.escape(head) + r'.*?\n```\n(.*?)\n```\n', t, flags=re.S).group(1)
    tpl = block('## Rows W-')
    safety = block('### The safety reader') if '\n### The safety reader' in t else None   # S-SCE0: a course may have no safety reader
    part = {}
    for ln in t.split('### This row in particular', 1)[1].splitlines():
        cells = [x.strip() for x in ln.strip().strip('|').split(' | ')]
        if ln.startswith('| W-') and len(cells) >= 4:
            part[cells[0]] = cells[3]
    return tpl, safety, part


def prompt_doc(r, nxt):
    """The prompt of a row whose course keeps its template in a document (doc_parts), its slots filled from the sources."""
    c, code = r['c'], r['code']
    tpl, safety, part = doc_parts(c)
    if r['row'] not in part:
        raise SystemExit(f"{r['row']}: no paragraph in the table \"This row in particular\" of {c['prompts_doc']}")
    done = [r['filed'][x] for x in r['order'] if x in r['filed']]
    cor, car, fl = corrections(), carried(), flags(r)
    if nxt:
        nx = f"{nxt['row']} (unit {nxt['code']})"
    else:
        nx = f"the next row in the Queue of `docs/BACKLOG.md` (no unit of this course is left; its reliefs, row G-R-{r['sc']['key']}, wait for Pedro's confirmation)"   # S-SCE0: the course's own G-R row
    last = r['code'] == r['order'][-1]   # S-SCE0 registration recheck (19 Nov 2026): the last row of this course, not of the queue
    slots = {
        'ROW': r['row'], 'CODE': code, 'TITLE': r['unit'][1], 'SEARCH': r['search'], 'PAGE': 'read-' + code.lower(), 'NEXT': nx,
        'FILED': ', '.join(f'`{rel(f)}`' for f in done) if done else 'none yet',
        'FLAGS': '\n'.join(f'- {x}' for x in fl) if fl else 'none',
        'CORRECTIONS': ('\n'.join(f'- **{a}.** {b}' for a, b in cor if a not in ('\u2014', '—')) + '\n\n' + LIMITS)
                       if [a for a, _ in cor if a not in ('\u2014', '—')] else '- none open',
        'PROPOSALS': '\n'.join(f'- **{a}.** {b}' + (f' ⚠ {x}' if x and not x.startswith('⚠') else f' {x}') for a, b, x in car if a not in ('—',))
                     if [a for a, _, _ in car if a != '—'] else '- none open',
        'PARTICULAR': part[r['row']],
        # registration check of S-SCE0 (19 Nov 2026): the last row writes a closing corrections prompt (prompts doc §4, point 7)
        'SAVE': f"`python3 kit/next_prompt.py --save` saves the prompt of {nx}" if not last else
                ("there is no next unit (the carry-forward rule, point 7): in place of a next unit's prompt, write a closing corrections prompt to the "
                 "standard of this one, listing every row still open in the Corrections section of `docs/BACKLOG.md` and every flag still open in "
                 f"`{pack.data_dir(c).relative_to(ROOT).as_posix()}/syllabus-flags.md`, each with its unit, the passage or flag, what is wrong and its "
                 "source, to be worked under the limits (a) to (f) of step 1b; add it as row C-" + r['sc']['key'] + " at the end of this course's "
                 "section of the Queue of `docs/BACKLOG.md`, the prompt in its prompt cell, and set the backlog's \"Next up\" line to it; do not run "
                 "`--save`; if nothing is open, say so and add no row. The course's reliefs, row G-R-" + r['sc']['key'] + ", wait for Pedro's confirmation"),
        'NEXTPROMPT': 'the next prompt' if not last else 'the closing corrections prompt (or the line saying nothing is open)',
        'SAVEROW': 'save the next prompt in its row (step 11)' if not last else 'add the closing corrections row, if any, as step 11 says',
    }
    out = re.sub(r'\{([A-Z]+)\}', lambda m: slots.get(m.group(1), m.group(0)), tpl)
    left = re.findall(r'\{[A-Z]+\}', out)
    if left:
        raise SystemExit(f'unfilled slots: {left}')
    q = quality_text(r)
    if q:
        i = out.index('\n\n**3. ')
        out = out[:i] + '\n\n' + q + out[i:]
    g = GATES.get(r['row'])
    if g and re.search(r'^\| ' + re.escape(g) + r' \|', (ROOT / 'docs' / 'BACKLOG.md').read_text(encoding='utf-8'), flags=re.M):
        out = f"Do not run until Pedro has closed {g}.\n\n" + out   # S-SCE0: the gate after W-SCE6 (syllabus §5, P-SCE6)
    if safety and 'Step 5b runs.' in part[r['row']]:          # the safety reader, for the rows whose paragraph says so (SP9, DD-SP1, DD-SP2)
        s = re.sub(r'\{([A-Z]+)\}', lambda m: slots.get(m.group(1), m.group(0)), safety)
        i = out.index('\n\n**6. ')
        out = out[:i] + '\n\n' + s + out[i:]
    return out


def prompt(r, nxt):
    c, d, u, code = r['c'], r['d'], r['unit'], r['code']
    if c.get('prompts_doc'):
        return prompt_doc(r, nxt)
    cid, data, vault = c['id'], pack.data_dir(c), c['vault']
    takes = d.AIMS[code][1]
    src = sources(takes)
    done = [r['filed'][x] for x in r['order'] if x in r['filed']]
    earlier = [x for x in r['order'][:r['order'].index(code)] if x not in r['filed']]
    fl = flags(r)
    case = (f'`{rel(data)}/case-facts.md` (Mara\'s register)' if cid == 'personal-brand'
            else f'`{rel(data)}/case-academy.md` (the Academy case file)')
    on = r['search'] == 'on'
    P = []
    P.append(f"Clone `apcanario/learning` (attach it with add_repo, push access; one shallow clone with a generous timeout, about ten minutes; call `register_repo_root` if the session offers it; the repo has no CLAUDE.md). Row {r['row']} of `docs/BACKLOG.md`, in this chat: write, fresh-check and file unit {code}, \"{u[1]}\", of the public course {r['sc']['name']} (`courses/{cid}/course.toml`: data `{rel(data)}/`, vault `{vault}/`, `docs/sourcing-standard.md` Parts 1 and {c['sourcing_part'][5:]}; search {r['search']}); correct every mistake the work finds; flag every contradiction or need that touches another unit; then build, verify, publish Academy once (the artifact, then GitHub Pages), push everything, close the row and end with the next row's prompt. Read first: `docs/public-courses.md` (the decisions and the thirteen rules of these rows), `docs/method.md` §4, §5, §7 and §8, `skills/write-unit`, `skills/audit-units` §3, `skills/file-unit` and the docstring of `kit/thin.py` (the chat reads those, never a unit). {THIN_CHAT}{TRIAL if r['row'] == 'W-BW1' else ''} Commit and push after every agent returns and after every step, on `main`. If the session's permission check refuses to run the repo's own scripts after the fresh clone, stop at once, say so in one line and ask Pedro to approve; never work around it. The safety check refuses an `rm -rf` whose target is a shell variable: use a literal absolute path, or do without the removal. Where a choice is open, take the most reasonable reading, say so in the record, and carry on; ask only if genuinely blocked. Fix every error, should-fix and minor finding the work turns up in this chat; a minor whose own Fix is \"no change required\" is recorded and not applied.")
    P.append("**1. Gate.** `python3 kit/next_prompt.py --list` shows this unit as the next one not filed"
             + (f" (it lists {', '.join(earlier)} as not filed: stop and say so, since the course is written in reading order)" if earlier else "")
             + ". No REWRITE verdict is open in `docs/courses-index.md`.")
    cor = corrections()
    if cor:
        P.append("**1b. Corrections first** (`docs/public-courses.md` §3 rule 12). The rows of the Corrections section of `docs/BACKLOG.md`, left by a chat that could not finish them, are worked now, before the packet is staged, so this unit's writer reads the corrected units. Each row, as it stands:\n"
                 + '\n'.join(f'- **{a}.** {b}' for a, b in cor) + "\n\n" + LIMITS
                 + " Each row worked moves to `docs/CHANGELOG.md` with this row's close, one line of result each. Commit and push after this step.")
    car = carried()
    if car:
        P.append("**1c. Carried proposals** (standing rule, Pedro, 15 Nov 2026: a proposal is listed in the reply on delivery, appended to the next prompt and worked in that chat unless he removes it). Each row below was raised by an earlier chat with its ⚠ flag on what it disturbs elsewhere in the project; work each now, after step 1b and before the packet is staged, a correction to a unit under the limits of step 1b, a kit or record change as it is written; a row Pedro removed from this list before the prompt was pasted is not worked. A brief change or a task only Pedro can do is not in this list; it stays *proposed*. Each row worked moves to `docs/CHANGELOG.md` with this row's close.\n"
                 + '\n'.join(f'- **{a}.** {b}' + (f' ⚠ {c}' if c and not c.startswith('⚠') else f' {c}') for a, b, c in car))
    packet = [f"`brief.txt`, built by script with `kit/mdcourse.py`'s `open_brief(d, sc, u)` from `{rel(ROOT / c['data'])}` and its briefs.md (the preamble, the Aim, Takes and Gives lines, the unit brief; never reworded, never retyped)",
              "`skills/write-unit/SKILL.md`", f"`docs/sourcing-standard.md` Parts 1 and {c['sourcing_part'][5:]}", "the figure kinds (`kit/viz.py`'s docstring and `VIZ_KEYS`)", case]
    if src:
        packet.append("the source units its Takes line names, each with its fresh-check report from `audits/brand-ai/` where one exists: " + ', '.join(f'`{rel(f)}`' for f in src))
    else:
        packet.append("no source unit of the private course (its Takes line names none); the files that line does name")
    packet.append("every unit of this course already filed: " + (', '.join(f'`{rel(f)}`' for f in done) if done else 'none yet'))
    packet.append("`flags.txt`: " + ("the open syllabus flags that name this unit, as printed below" if fl else "empty (no open flag names this unit)"))
    P.append(f"**2. Stage the writer's packet** in one folder outside the repo with `python3 kit/thin.py stage writer --row {r['row']} <folder>`, so that what the writer read is a path check. The script puts in it: " + '; '.join(packet) + ". The chat does not open any of it.")
    if fl:
        P.append("Open flags that name this unit (from `syllabus-flags.md`; the writer deals with each and says how in its notes):\n" + '\n'.join(f'- {x}' for x in fl))
    if code in NOTES:
        P.append("**This row in particular.** " + NOTES[code])
    P.append(f"**3. The writer.** One fresh Agent on model opus, isolated, that sees only its folder. It states its model in its first line; if that is not claude-opus-5-5, stop at once, change nothing and say so in one line (Pedro may accept the model the session gave; the record then names it). Tell it: a memory snapshot, project instructions or anything of that kind in its context is not a source and must not be used; it uses no memory, past-chat, Projects, connector, Artifact or Agent tool and no `mcp__` tool; it publishes nothing; "
             + ("search is on: it searches before writing and dates every fact that can change; " if on else "search is off: it writes from the packet and its knowledge and searches only to re-verify a carried claim or a specific doubtful point; ")
             + "the web rule holds (WebSearch first; WebFetch only a URL that a search in the same agent returned verbatim, never one typed, printed in a file, edited or reached by a redirect; a refused, redirected or timed-out fetch is \"not checked\" and is never retried or fetched from a copy); it re-verifies at its source every claim it carries over from a source unit, and anything it could not re-verify goes on the unsure list or stays out; it follows `skills/write-unit` §4 to §5, renders every figure before handing in, and writes as it goes, so a restart loses little: `out/unit.md` (front matter, the unit, the deliverable, Sources), `out/unsure.md` (up to ten claims, then the `Object:` line) and `out/notes.md` with three lists, each item naming the unit codes it touches: **Source errors** (every mistake found in a source unit: the quoted text, what is wrong, the source that shows it, the exact replacement), **Contradictions** (where this unit's evidence disagrees with a filed unit of this course or with the brief of an unwritten one, read on the course's Briefs data in the packet) and **Needs** (what the unit needed that the syllabus does not give, and what a later unit must now cover or avoid). An empty list is written as \"none\". Its reply to the chat is at most six lines: its model, the files it wrote, the counts of its lists. **Sources and attribution (S-BW1, from what row F-PB found: attribution failed at 8.8 per 100 claims, numbers at 1.1):** a Sources title is the cited page's own headline as the page shows it, never its URL slug and never a site name joined to a page name; a quotation is credited to the person who said it, with the outlet as where it was said, never to the outlet alone; words inside quotation marks are exactly the source's words, and a paraphrase is never put in quotation marks; a figure is cited to the page that states it for that very thing, not to a page that mentions the topic or to a page that repeats it. Each Sources entry is checked against its page's headline before the unit is handed in.")
    P.append(f"**4. The fresh check.** A separate fresh Agent on model opus that has not seen the writing, under the same agent rules, with live search: the prompt of `skills/audit-units` §3 with its figures paragraph, filled from the course's entry, on a packet made with `python3 kit/thin.py stage checker --row {r['row']} <folder> --unit out/unit.md --notes out/notes.md --unsure out/unsure.md` (the unit, its brief, the sourcing parts, {case.split(' (')[0]} and the writer's notes), writing its report to `out/report.md` and replying in at most six lines (its model, the verdict, the counts); where the harness refuses a subagent a report file (W-BW1, 15 Nov 2026: `Subagents should return findings as text`), the agent returns the report as its reply and the chat saves it verbatim to `out/report.md`, with the agent's own line `Verdict: <code> · keep|fix|rewrite · counts` ahead of it, which `save-report` reads. It also (8) verifies each item of the writer's Source errors list against the source named (confirmed / not confirmed), (9) runs the unit against the course's part of the sourcing standard line by line, and (10) reads the unit as the persona in the preamble would and says where it assumes something only the private course's reader would know, and (11) runs an attribution pass: every Sources title against its page's headline, every quotation against its speaker, every pair of quotation marks against the source's exact words, every figure against the page that states it for that thing. Before any fix, `python3 kit/thin.py save-report --row {r['row']} --report <out/report.md> --model <the model it stated> --chat <this session's link> --date <today>` saves the report verbatim as `audits/{cid}/fresh-check-{code}.md` with the front matter `audits/README.md` sets out and prints the fresh-check line; `python3 kit/thin.py assemble out/unit.md out/unsure.md \"<that line>\"` gives the unit its unsure list. A `rewrite` verdict sends the unit back to a new writer from the same brief, once; a second `rewrite` stops the row with a note of where it stopped.")
    P.append("**5. Apply.** A fresh applier agent (staged with `thin.py stage applier --row ROW <folder> --unit <unit> --report <report>`, which makes `fixes.json` from the report) verifies each finding against the unit and the cited source line and writes `out/apply.json` (`apply` or `hold`, with the reason), replying in at most six lines; `python3 kit/thin.py apply <unit> fixes.json out/apply.json` applies it as exact replacements (each Current counted once; the unit is left unchanged if one fails, and the applier is then re-run on the failures once). Every `hold` is recorded with its reason, and a held error or should-fix is a flag. A figure that fails is fixed and re-checked by a new agent from the unit's text without its figures, the captions and the frames `verify.py --shots` saves, as many times as it takes; figures are never dropped (Pedro, 3 Nov 2026). Restarts: when the harness says it is resuming an agent, let it and say so in the record; if an agent is lost, re-run it from the start once; if lost again, start a fresh agent on the same packet that resumes from the lost run's working files. Look for agent transcripts (`.jsonl` under `/root/.claude/` or `/tmp/`); where there are some, check by script that each agent used no tool it was denied and read nothing outside its folder, and take its `\"model\"` field; where there are none, say so, and the model is the one the agent stated.")
    P.append(f"**6. Mistakes elsewhere.** Every confirmed Source error is corrected where it sits: an exact replacement in the private unit under `courses/brand-ai/`, a dated note in that unit (\"Erratum <date>, found by {code}'s writer\"), a changelog row in `courses/brand-ai/course.toml` (a new `[[pack.changelog]]` table above the first, its text starting with the next version, `v<n>. `, which is the course's version; kit/pack.py). A mistake the work finds in a filed unit of this course is fixed the same way in `{rel(ROOT / c['data'])}`. An item the checker did not confirm is recorded and not applied. Each correction is one line in the reply.")
    P.append(f"**7. Syllabus flags.** Append every Contradiction and Need to `{rel(data)}/syllabus-flags.md` as a new row (next number, date, raised by {code}, the units affected, the flag, the proposed change, status open); set to `carried` each flag this unit was given and dealt with. A Contradiction whose remedy is a change to a filed unit's text, not to a brief, is corrected in this chat at step 7b. Change no brief: `units_data.py` is edited only by a syllabus review that Pedro confirms (`docs/public-courses.md` §3, rules 6 and 7). If a flag means the next unit cannot be written as briefed, say so in the first line of the reply and write, as the next prompt, a syllabus-review prompt in place of the unit's.")
    P.append("**7b. Proposals now** (`docs/public-courses.md` §3 rule 12; Pedro, 12 Nov 2026, 21:31: proposals are dealt with before the chat in which they appear ends). Nothing this work uncovers is left as a proposal for later: every correction to a filed unit or a record, and every fix to the kit it needs, is made in this chat before the build of step 9, and one found later (at the build, verify or publish) is made before the publish, rebuilt and re-verified. For corrections to units: " + LIMITS + " Two kinds stay proposed, since this chat may not decide them: a change to a brief (a syllabus review, rule 7, which Pedro confirms) and a task only Pedro can do by hand; each is a *proposed* row, and the reply says why it could not be done. Commit and push after this step.")
    P.append(f"**8. File** per `skills/file-unit` §1, §2, §4, §5 and §6, by a fresh filer agent and a script, not by the chat: front matter (model: the model the writer stated) on `{vault}/{code}-<slug>.md`; the filer, staged with `python3 kit/thin.py stage filer --row {r['row']} <folder> --unit <unit> --notes <notes> --unsure <unsure> --report <report>`, writes `out/records.json` (the reading-page intro, which says what the unit is, how it was made and its known gaps with no private term; `STATUS`, `NEXT_UNIT`, `VERSION`, the hub `CHANGELOG` line, "
             + ("the facts the unit set about Mara with their sections and what it left free, " if cid == 'personal-brand' else "any fact the Needs list asked for that the Project's records hold, private details removed, for `case-academy.md`, ")
             + "the flag rows and the flags carried, the `docs/courses-index.md` edits (the row with the fresh-check path, the count line, the counter, a staleness row if search is on), both changelog entries, and the writer's `Object:` line kept in the changelog row), replying in at most six lines; `python3 kit/thin.py insert out/records.json` inserts it and restores everything if it fails. Then `python3 kit/index_check.py` until it matches and `python3 kit/private_terms.py` prints OK (a hit is fixed in the unit, never in the list). No relief until row G-R.")
    P.append("**9. Build and verify.** `cd kit && python3 build.py` (about five minutes; read its last line, since a build that stops leaves the site stale), then `python3 verify.py` (ALL CHECKS PASSED; read every FAIL line), then `python3 verify.py --shots <dir> --page read-" + code.lower() + "` (check the id it prints; it runs for up to half an hour, so start it in the background with a one-hour timeout and wait for it to end before any figure re-check reads its frames: C3, 15 Nov 2026) and look at the page's shots at phone and desktop, dark and light, and at every figure's frames. A layout fault is fixed in `design/theme.css` (then `cp design/theme.css kit/shell.css`) or `kit/viz.py`, never in a page.")
    P.append(f"**10. Publish Academy once.** Before the build you publish, move the row to `docs/CHANGELOG.md`, move its entry in `docs/site-log.md` from Next to Done (step 11), set the backlog's \"Next up\" line and save the next prompt in its row (step 11), so the published Backlog and Changelog pages, which Academy renders from `docs/site-log.md` alone, are current. Read the artifact {ACADEMY} first and compare the live page with the build you started from (`get_artifact` for the live version id; `list_files` for every file's sha256 against `sha256sum` of the start build's files, which are the `kit/academy/` of the commit you cloned). `publish_files` patches (a republish changes only the files it names) and refuses a shell that does not begin with a doctype: send the files that differ from the start build, found by script, and the shell inside the wrapper the live page carries (its first line and its closing `</body></html>`, taken from the saved live shell by script into a copy outside the repo), with `slug`, `base_version` and mode patch; then read the sent files back and compare their sha256 with the build; never a new artifact, never forced. Then `./deploy.sh` once: attach `apcanario/academy` with add_repo (if refused, carry on and ask Pedro once at the end), clone it once, set `ACADEMY_DIR` to the clone, and confirm with `gh run` that the deployment of the new build succeeded. The publish and deploy identifiers go into the records after the publish, committed without republishing.")
    P.append("**11. Close** per `docs/method.md` §8, steps 1 to 5: the row done and moved to `docs/CHANGELOG.md` with the date, the models and a one-line result;"
             + f"its entry in `docs/site-log.md` (§8 step 1b) moved from Next to Done, dated, one plain sentence (\"{code}, {u[1]}, written\", ending \"course <code> complete\" if it is the course's last unit; no model name, file name, agent, audit or row word, no private term), Next renumbered; "
             + "`kit/CHANGELOG.md` gets its session entry; every task the work uncovered has been done at step 7b, but a brief change or a task for Pedro, each a new row marked *proposed* (a syllabus review, if a flag asks for one, is such a row); every other proposal the work uncovered and could not do at step 7b is a row of the Carried proposals section of `docs/BACKLOG.md` with its ⚠ flag on any disruption elsewhere in the project, and the next prompt, which this step saves, appends it (step 1c); a correction left open after step 7b's second round, or by a row that stopped, is a row of the Corrections section of `docs/BACKLOG.md`, which the next prompt works at its step 1b (rule 12); the rows worked at step 1b move to `docs/CHANGELOG.md` with this row; the Project copies `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` rewritten from `docs/`, and the Project mirrors refreshed with the Projects tool, never a unit (Pedro, 15 Nov 2026: units are not mirrored): only `claude/BACKLOG-chats.md` and `claude/CHANGELOG-chats.md` every time, and the method, `courses-index.md`, the course's `hub.py`, `syllabus-flags.md` and the skill mirrors when this row changed them (read each existing path with `project_read` first, then write it from its repo file with `local_path`). The next prompt is not written by hand: `python3 kit/next_prompt.py --save` prints the prompt of the next unit not filed"
             + (f" ({nxt['row']}, unit {nxt['code']})" if nxt else " (none is left: the next row is G-R, the reliefs of both public courses, and its prompt is written to the standard of this one)")
             + " and saves it in that row of `docs/BACKLOG.md`; run it after filing and before the final build."
             + (f" Here the next row is {hold(nxt)}, the review that holds {nxt['row']}: its prompt is already saved in its row, so `--save` is not run; set the backlog's \"Next up\" line to {hold(nxt)} and give its saved prompt at the end of the reply." if hold(nxt) else ''))
    P.append("**Reply:** what was filed where (words, figures, search used or not); the fresh-check verdict and counts; each mistake corrected, in a line, with the file it was in; each flag raised, with the units it affects and whether it blocks the next unit; the private-terms result; verify's result; the publish and the deploy; the choices taken; the backlog hand-off (row done, the corrections and proposals dealt with in this chat, any left with the reason, next up); **every proposal listed**, each with what it does and a ⚠ flag on any disruption elsewhere in the project, stating that it is appended to the next row's prompt and worked in that chat unless Pedro removes it; then the next prompt in a code block.")
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
    if '--quality' in sys.argv:
        for r in rs:
            if r['code'] in r['filed']: continue
            mine, over = quality(r)
            print(f"{r['code']}: {mine} flags before writing" + (' (over 5)' if mine > 5 else ''))
            for u, b, n in over: print(f"{u}: {b} before, {n} in all (over the rule)")
            break
        sys.exit(0)
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
