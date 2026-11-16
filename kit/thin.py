"""The scripts of the thin main chat (S-BW1, 15 Nov 2026; docs/method.md §4 and §8).

A writing row's chat runs on Sonnet 5.5 and never opens a unit, a source unit, a report or a brief. It stages packets, launches
Opus 5.5 agents, and reads only each agent's reply (at most six lines) and its out/stats.json. Everything that needs a decision
is an agent's; everything that changes a file is one of these commands, which checks its own result and refuses to leave a
half-done change.

  python3 kit/thin.py stage KIND --row W-BW1 DIR [--unit F] [--report F] [--notes F] [--unsure F] [--fixes F] [--stats F,F] [--date D]
        KIND writer | checker | applier | filer. Builds the packet folder DIR for one agent (it must not exist or be empty).
        corrections  --text F --files a,b (repo paths) --briefs BW1,BW4: the corrections, the units they touch, the briefs
                (open_brief), syllabus-flags.md, the case file (the register), the sourcing standard (W-BW5)
        writer  brief.txt (kit/mdcourse.py open_brief), the skill, sourcing standard, figure kinds, case file, source units with
                their fresh-check reports, filed units of the course, flags.txt
        checker unit.md, brief.txt, notes.md, unsure.md, the sourcing standard, the case file, skills/audit-units
        applier unit.md, report.md (the fresh-check report), fixes.json (made from the report by `fixes`)
        filer   unit.md, notes.md, unsure.md, report.md, the course's hub.py, syllabus-flags.md and case file, the course's rows
                of docs/courses-index.md, a template of records.json, filer-rules.txt, the day's corrections reports of the course
                (corrections/, --date, default today) and the stats files given with --stats (C4)
  python3 kit/thin.py fixes REPORT.md FIXES.json
        Parses the findings of a fresh-check report (`[sev] [kind] where; Current: "..."; Problem: ...; Fix: "..."; Basis: ...`)
        into fixes.json: [{id, severity, kind, where, current, fix}].
  python3 kit/thin.py apply UNIT.md FIXES.json APPLY.json
        APPLY.json (the applier agent's decisions): [{id, decision: "apply"|"hold", reason}]. Each applied Current must occur once in
        the unit as it stands when that fix is applied; if one does not, the unit is left unchanged and the failures are listed
        (exit 1). A fix with no decision is held.
  python3 kit/thin.py insert RECORDS.json
        RECORDS.json (the filer agent's output; keys below) is inserted into the repo's files by anchored edits, and every
        changed Python file is compiled and kit/index_check.py is run (C4); if anything fails every file is restored (exit 1).
  python3 kit/thin.py save-report --row W-BW1 --report F --model M --chat URL --date D
        Saves the checker's report verbatim under audits/<course id>/fresh-check-<code>.md with the front matter audits/README.md sets
        out (verdict and counts counted from the report) and prints the line the unit's unsure list gains.
  python3 kit/thin.py assemble UNIT.md UNSURE.md "<fresh-check line>"
        Appends `## Unsure list`, the writer's unsure list and the fresh-check line to the unit (once; refuses a second run).
  python3 kit/thin.py correct REPORT --ids "Change 1,New 2" --map NAME=repo/path,... --note "Correction <date>, found by <who>"
        Applies passed changes of a corrections check as exact replacements and appends the dated note to each unit changed.
  python3 kit/thin.py stats OUTDIR
        Writes OUTDIR/stats.json from the files an agent left there (unit.md, unsure.md, notes.md, report.md, apply.json,
        records.json), counted by script; the chat reads this and the agent's six-line reply, nothing else.

records.json
  row, code, course (the kit/courses.py id), date ("2026-11-15 12:00" for the hub changelog),
  reading   {id, course, title, covers, name, intro}                 -> READINGS of the course's hub.py
  status    "written 15 Nov"                                          -> STATUS[code]
  next_unit "BW2"  (or "—")                                           -> NEXT_UNIT
  version   "v2 · 15 Nov 2026"                                        -> VERSION
  hub_changelog  "v2. BW1 ... filed ..."                              -> top of CHANGELOG (with `date`)
  case_lines     ["..."]                                              -> appended to the course's case file
  flag_rows      [{date, raised_by, affects, flag, proposed}]         -> new rows of syllabus-flags.md (numbered, open)
  flags_carried  ["F3"]                                               -> those rows set to carried
  index_edits    [{old, new}]                                         -> docs/courses-index.md (each old occurs once)
  changelog_row  {date, chat, model, result}                          -> top of docs/CHANGELOG.md (commit cell "this commit")
  kit_bullet     "- **...**"                                          -> top of "Where things stand" in kit/CHANGELOG.md
  kit_session    {heading, body}                                      -> a session entry in kit/CHANGELOG.md
"""
import importlib.util, json, pathlib, re, shutil, sys

R = pathlib.Path(__file__).resolve().parent
ROOT = R.parent
sys.path.insert(0, str(R))


def die(msg, code=1):
    print(msg, file=sys.stderr)
    sys.exit(code)


# ---------------------------------------------------------------------------------------------- fixes / apply

HEAD = re.compile(r'^\[?(error|should-fix|minor)\]?\s+\[([\w-]+)\]\s*(.*?);\s*Current:\s*', re.S)
LABEL = re.compile(r'[;.]\s*(Problem|Fix|Basis):\s*')


def unquote(s):
    """Strip one outer pair of straight or curly double quotes, and nothing else (C2, 15 Nov 2026)."""
    s = s.strip()
    if len(s) >= 2 and s[0] in '"\u201c' and s[-1] in '"\u201d':
        return s[1:-1]
    return s


def parse_finding(ln):
    """One finding line -> (sev, kind, where, current, fix). Current runs up to the first `; Problem:`, Fix from the first
    `Fix:` after Problem up to the last `; Basis:` (or the end), so nested quotes never cut a field (C2, 15 Nov 2026: W-BW4's
    f1 and f3 were truncated and f4 to f6 lost). fix is None when there is no Fix label, '' when the Fix is empty (a deletion)."""
    m = HEAD.match(ln)
    if not m:
        return None
    sev, kind, where = m.groups()
    rest = ln[m.end():]
    labels = [(x.group(1), x.start(), x.end()) for x in LABEL.finditer(rest)]
    prob = next((l for l in labels if l[0] == 'Problem'), None)
    if prob is None:
        return None
    cur = unquote(rest[:prob[1]])
    fx = next((l for l in labels if l[0] == 'Fix' and l[1] > prob[1]), None)
    fix = None
    if fx is not None:
        basis = [l for l in labels if l[0] == 'Basis' and l[1] > fx[1]]
        end = basis[-1][1] if basis else len(rest)
        raw = rest[fx[2]:end].strip()
        fix = '' if raw.lower() in ('', '""', '\u201c\u201d', '(delete)', 'delete') else unquote(raw)
    return sev, kind, where, cur, fix


def cmd_fixes(report, out):
    items = []
    for ln in pathlib.Path(report).read_text(encoding='utf-8').splitlines():
        got = parse_finding(ln.strip())
        if not got:
            continue
        sev, kind, where, cur, fix = got
        fix = fix.replace('\\n', '\n') if fix else fix   # W-BW2: a checker writes a line break inside a Fix as the two characters \n
        # W-BW10: a checker escapes inner double quotes as \" (JSON style) inside a quoted Current or Fix; the unit has plain quotes
        cur = cur.replace('\\"', '"')
        fix = fix.replace('\\"', '"') if fix else fix
        items.append(dict(id=f'f{len(items) + 1}', severity=sev, kind=kind, where=where.strip(), current=cur, fix=fix))
    pathlib.Path(out).write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'{len(items)} findings -> {out}')


def cmd_apply(unit, fixes, decisions):
    p = pathlib.Path(unit)
    text = p.read_text(encoding='utf-8')
    fx = {f['id']: f for f in json.loads(pathlib.Path(fixes).read_text(encoding='utf-8'))}
    dec = {d['id']: d for d in json.loads(pathlib.Path(decisions).read_text(encoding='utf-8'))}
    unknown = [i for i in dec if i not in fx]
    if unknown:
        die(f'apply.json names findings that fixes.json lacks: {unknown}')
    applied, held, bad = [], [], []
    for i, f in fx.items():
        d = dec.get(i)
        if not d or d.get('decision') != 'apply' or f.get('fix') is None or f['fix'] == f['current']:   # '' is a deletion (C2)
            held.append(i)
            continue
        n = text.count(f['current'])
        if n != 1:
            bad.append(f'{i}: Current occurs {n} times')
            continue
        text = text.replace(f['current'], f['fix'], 1)
        applied.append(i)
    if bad:
        die('unit left unchanged; ' + '; '.join(bad))
    p.write_text(text, encoding='utf-8')
    print(f'applied {len(applied)}, held {len(held)}: held = {held}')


def parse_corrections(report):
    """The blocks of a corrections check (`## Change N` / `## New N`, each with File:, a fenced Current and Replacement,
    Result:, Syllabus:) -> {name: dict(file, current, replacement, ok)}; ok when Result is PASS and Syllabus has no conflict."""
    t = pathlib.Path(report).read_text(encoding='utf-8')
    out = {}
    for m in re.finditer(r'(?m)^## ((?:Change|New) \d+)\s*$(.*?)(?=^## |\Z)', t, flags=re.S):
        name, body = m.group(1), m.group(2)
        f = re.search(r'(?m)^File:\s*(?:files/)?(\S+?)[,\s]', body)
        blocks = re.findall(r'(?ms)^(Current|Replacement):[^\n]*\n(`{3,})[^\n]*\n(.*?)\n\2\s*$', body)
        got = {k: v for k, _, v in blocks}
        res = re.search(r'(?m)^Result:\s*(\w+)', body)
        syl = re.search(r'(?m)^Syllabus:\s*(.*)$', body)
        out[name] = dict(file=f.group(1) if f else None, current=got.get('Current'), replacement=got.get('Replacement'),
                         ok=bool(res and res.group(1).upper() == 'PASS' and syl and syl.group(1).lower().startswith('no conflict')))
    return out


def cmd_correct(argv):
    """thin.py correct REPORT --ids "Change 1,Change 2" --map B4-x.md=courses/brand-ai/B4-x.md,... --note "Correction ..."
    Applies the named passed changes as exact replacements (each Current once, in order; nothing written if one fails) and
    appends the note to each unit it changed (W-BW5, 15 Nov 2026)."""
    rep = argv[0]
    opt = {argv[i][2:]: argv[i + 1] for i in range(1, len(argv), 2)}
    ch = parse_corrections(rep)
    mp = dict(x.split('=', 1) for x in opt['map'].split(','))
    texts, bad = {}, []
    for name in [x.strip() for x in opt['ids'].split(',') if x.strip()]:
        c = ch.get(name)
        if not c or not c['ok'] or c['current'] is None or c['replacement'] is None:
            bad.append(f'{name}: not found, not passed, or missing a field'); continue
        path = ROOT / mp.get(c['file'], c['file'] or '')
        if path not in texts:
            if not path.is_file():
                bad.append(f'{name}: no file {path}'); continue
            texts[path] = path.read_text(encoding='utf-8')
        n = texts[path].count(c['current'])
        if n != 1:
            bad.append(f'{name}: Current occurs {n} times in {path.name}'); continue
        texts[path] = texts[path].replace(c['current'], c['replacement'], 1)
    if bad:
        die('nothing written; ' + '; '.join(bad))
    for path, txt in texts.items():
        path.write_text(txt.rstrip('\n') + '\n\n' + opt['note'].strip() + '\n', encoding='utf-8')
    print('corrected: ' + ', '.join(str(p.relative_to(ROOT)) for p in texts))


# ---------------------------------------------------------------------------------------------- insert

def one(text, old, new, what):
    n = text.count(old)
    if n != 1:
        raise ValueError(f'{what}: expected one occurrence, found {n}')
    return text.replace(old, new, 1)


def table_after_sep(text, line):
    """Insert a table row directly under the header separator of the first table."""
    m = re.search(r'^\|[-| ]+\|\s*$', text, flags=re.M)
    if not m:
        raise ValueError('no table separator')
    return text[:m.end()] + '\n' + line + text[m.end():]


def cmd_insert(rec_path):
    rec = json.loads(pathlib.Path(rec_path).read_text(encoding='utf-8'))
    from courses import COURSES
    c = next((x for x in COURSES if x['id'] == rec['course']), None)
    if not c:
        die(f"no course {rec['course']} in kit/courses.py")
    data = ROOT / c['data']
    ddir = data.parent
    files = {}                      # path -> new text
    old = {}                        # path -> old text, for the restore

    def get(p):
        p = pathlib.Path(p)
        if p not in files:
            old[p] = p.read_text(encoding='utf-8')
            files[p] = old[p]
        return files[p]

    try:
        t = get(data)
        if 'reading' in rec:
            r = rec['reading']
            if r['covers'] != [rec['code']]:
                raise ValueError('reading.covers must be [code]')
            ent = '    dict(' + ', '.join(f'{k}={v!r}' for k, v in r.items()) + '),\n'
            if re.search(r'^READINGS = \[\]', t, flags=re.M):
                t = re.sub(r'^READINGS = \[\]', 'READINGS = [\n' + ent + ']', t, count=1, flags=re.M)
            else:
                i = t.index('READINGS = [')
                j = t.index('\n]', i)
                t = t[:j + 1] + ent + t[j + 1:]
        if 'status' in rec:
            m = re.search(r'^STATUS = \{(.*)\}', t, flags=re.M)
            if not m:
                raise ValueError('STATUS is not a one-line dict')
            inner = m.group(1).strip()
            add = f"{rec['code']!r}: {rec['status']!r}"
            t = t[:m.start()] + 'STATUS = {' + (inner + ', ' if inner else '') + add + '}' + t[m.end():]
        if 'next_unit' in rec:
            t = re.sub(r"^NEXT_UNIT = .*$", f"NEXT_UNIT = {rec['next_unit']!r}", t, count=1, flags=re.M)
        if 'version' in rec:
            t = re.sub(r"^VERSION = .*$", f"VERSION = {rec['version']!r}", t, count=1, flags=re.M)
        if 'hub_changelog' in rec:
            t = one(t, 'CHANGELOG = [\n', f"CHANGELOG = [\n    ({rec['date']!r}, {rec['hub_changelog']!r}),\n", 'hub CHANGELOG')
        files[data] = t

        if rec.get('case_lines'):
            case = next((f for f in ddir.glob('case-*.md')), None)
            if case is None:
                raise ValueError('no case file in the data folder')
            files[case] = get(case).rstrip('\n') + '\n' + '\n'.join(rec['case_lines']) + '\n'

        fl = ddir / 'syllabus-flags.md'
        if rec.get('flag_rows') or rec.get('flags_carried'):
            ft = get(fl)
            nums = [int(x) for x in re.findall(r'^\| F(\d+) \|', ft, flags=re.M)]
            n = max(nums or [0])
            for i in rec.get('flags_carried', []):
                ft = re.sub(r'^(\| ' + re.escape(i) + r' \|.*\|) open \|\s*$', r'\1 carried |', ft, count=1, flags=re.M)
            for row in rec.get('flag_rows', []):
                n += 1
                cells = [row[k].replace('|', '/') for k in ('flag', 'proposed')]
                ft = ft.rstrip('\n') + f"\n| F{n} | {row['date']} | {row['raised_by']} | {row['affects']} | {cells[0]} | {cells[1]} | open |\n"
            files[fl] = ft

        if rec.get('index_edits'):
            ix = ROOT / 'docs' / 'courses-index.md'
            it = get(ix)
            for e in rec['index_edits']:
                it = one(it, e['old'], e['new'], 'courses-index edit')
            files[ix] = it

        if 'changelog_row' in rec:
            r = rec['changelog_row']
            cp = ROOT / 'docs' / 'CHANGELOG.md'
            line = '| ' + ' | '.join(str(r[k]).replace('|', '/') for k in ('date', 'chat', 'model', 'result')) + ' | this commit |'
            files[cp] = table_after_sep(get(cp), line)

        kp = ROOT / 'kit' / 'CHANGELOG.md'
        if 'kit_bullet' in rec:
            files[kp] = one(get(kp), '## Where things stand\n\n', '## Where things stand\n\n' + rec['kit_bullet'].rstrip('\n') + '\n', 'kit bullet')
        if 'kit_session' in rec:
            s = rec['kit_session']
            kt = get(kp)
            m = re.search(r'^## \d', kt, flags=re.M)
            if not m:
                raise ValueError('no session heading in kit/CHANGELOG.md')
            files[kp] = kt[:m.start()] + f"## {s['heading']}\n\n{s['body'].rstrip()}\n\n" + kt[m.start():]

        for p, txt in files.items():
            pathlib.Path(p).write_text(txt, encoding='utf-8')
        for p in files:
            if str(p).endswith('.py'):
                compile(pathlib.Path(p).read_text(encoding='utf-8'), str(p), 'exec')
        spec = importlib.util.spec_from_file_location('hub_check', data)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if rec.get('status') and mod.STATUS.get(rec['code']) != rec['status']:
            raise ValueError('STATUS did not take')
        if rec.get('reading') and not any(rec['code'] in x['covers'] for x in mod.READINGS):
            raise ValueError('READINGS did not take')
        import subprocess                                    # C4, 15 Nov 2026: the index must still match after the insert
        ic = subprocess.run([sys.executable, str(R / 'index_check.py')], cwd=str(R), capture_output=True, text=True)
        if ic.returncode != 0:
            raise ValueError('kit/index_check.py failed: ' + (ic.stdout + ic.stderr).strip()[-1500:])
    except Exception as ex:                                  # restore everything
        for p, txt in old.items():
            pathlib.Path(p).write_text(txt, encoding='utf-8')
        die(f'insert failed, every file restored: {ex}')
    print('inserted into: ' + ', '.join(sorted(str(p.relative_to(ROOT)) for p in files if files[p] != old[p])))


# ---------------------------------------------------------------------------------------------- save-report / assemble

def cmd_save_report(argv):
    opt = {argv[i][2:]: argv[i + 1] for i in range(0, len(argv), 2)}
    for k in ('row', 'report', 'model', 'chat', 'date'):
        if k not in opt:
            die('usage: thin.py save-report --row R --report F --model M --chat URL --date D')
    import next_prompt as np
    r = next((x for x in np.rows() if x['row'] == opt['row']), None)
    if r is None:
        die(f"no row {opt['row']}")
    body = pathlib.Path(opt['report']).read_text(encoding='utf-8')
    sev = re.findall(r'^\[?(error|should-fix|minor)\]?\s+\[[\w-]+\]', body, flags=re.M)
    v = re.search(r'verdict[^\n]*?\b(keep|fix|rewrite)\b', body, flags=re.I)
    if not v:
        die('no verdict line in the report')
    counts = f"{sev.count('error')} errors, {sev.count('should-fix')} should-fix, {sev.count('minor')} minor"
    c, code = r['c'], r['code']
    out = ROOT / 'audits' / c['id'] / f'fresh-check-{code}.md'
    head = (f"---\naudit: fresh check\nunit: {code} · {r['unit'][1]}\ncourse: {c['id']} · {r['sc']['name']}\nmodel: {opt['model']}\n"
            f"date: {opt['date']}\nchat: {opt['chat']}\nverdict: {v.group(1).lower()} · {counts}\n---\n\n"
            "The checker's final report, verbatim, from its hand-back. Saved before any finding was applied.\n\n")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(head + body, encoding='utf-8')
    print(f"Fresh check {opt['date']} ({opt['model']}): {v.group(1).lower()} \u00b7 {counts}; report `audits/{c['id']}/fresh-check-{code}.md`")


def cmd_assemble(unit, unsure, line):
    p = pathlib.Path(unit)
    t = p.read_text(encoding='utf-8')
    if '\n## Unsure list' in t:
        die('the unit already has an unsure list')
    p.write_text(t.rstrip('\n') + '\n\n## Unsure list\n\n' + pathlib.Path(unsure).read_text(encoding='utf-8').strip('\n') + '\n\n' + line.strip() + '\n', encoding='utf-8')
    print('unsure list appended')


# ---------------------------------------------------------------------------------------------- stats

def words(t):
    t = re.sub(r'```viz.*?```', '', t, flags=re.S)
    return len(re.findall(r'\S+', t))


def cmd_stats(d):
    d = pathlib.Path(d)
    s = {}

    def rd(n):
        f = d / n
        return f.read_text(encoding='utf-8') if f.exists() else None

    u = rd('unit.md')
    if u is not None:
        s['unit'] = dict(words=words(u), figures=len(re.findall(r'^```viz', u, flags=re.M)),
                         sources=len(re.findall(r'^- .*https?://', u.split('## Sources')[-1], flags=re.M)) if '## Sources' in u else 0,
                         front_matter=u.startswith('---'))
    uns = rd('unsure.md')
    if uns is not None:
        s['unsure'] = dict(claims=len([x for x in uns.splitlines() if re.match(r'\s*(\d+[.)]|[-*])\s', x)]),
                           object_line=bool(re.search(r'^Object:', uns, flags=re.M)))
    n = rd('notes.md')
    if n is not None:
        # a section runs from its heading (any of #, ##, ** forms) to the next of the three; "none" (also "- none found") counts 0 (S-BW1 fix, 15 Nov 2026: headings with # were not read)
        names = ('Source errors', 'Contradictions', 'Needs')
        head = re.compile(r'(?im)^\s*(?:#{1,6}\s*(' + '|'.join(names) + r'|[^\n]*)|\*{2}(' + '|'.join(names) + r'|Flags dealt with)\b.*)$')   # W-BW5: a fourth heading ends Needs; W-BW8: any heading ("## Flags") ends it
        marks = [((m.group(1) or m.group(2) or '').lower(), m.start(), m.end()) for m in head.finditer(n)]
        s['notes'] = {k: 0 for k in names}
        for i, (nm, a, b) in enumerate(marks):
            body = n[b:marks[i + 1][1] if i + 1 < len(marks) else len(n)]
            key = next((k for k in names if k.lower() == nm), None)
            if key is None:
                continue
            if re.search(r'(?im)^\s*(?:[-*]\s*)?none\b', body):
                continue
            s['notes'][key] = len([x for x in body.splitlines() if re.match(r'(\d+[.)]|[-*])\s', x)])   # top-level items only
    rp = rd('report.md')
    if rp is not None:
        sev = re.findall(r'^\[?(error|should-fix|minor)\]?\s+\[[\w-]+\]', rp, flags=re.M)
        v = re.search(r'verdict[^\n]*?\b(keep|fix|rewrite)\b', rp, flags=re.I)
        s['report'] = dict(error=sev.count('error'), should_fix=sev.count('should-fix'), minor=sev.count('minor'), verdict=v.group(1).lower() if v else None,
                           model=(re.search(r'claude-[a-z0-9.-]+', rp) or [None])[0])
    a = rd('apply.json')
    if a is not None:
        a = json.loads(a)
        s['apply'] = dict(apply=sum(x['decision'] == 'apply' for x in a), hold=sum(x['decision'] == 'hold' for x in a))
    rc = rd('records.json')
    if rc is not None:
        r = json.loads(rc)
        s['records'] = dict(keys=sorted(r), flag_rows=len(r.get('flag_rows', [])), index_edits=len(r.get('index_edits', [])), case_lines=len(r.get('case_lines', [])))
    (d / 'stats.json').write_text(json.dumps(s, indent=1), encoding='utf-8')
    print(json.dumps(s))


# ---------------------------------------------------------------------------------------------- stage

def cmd_stage(argv):
    kind = argv[0]
    opt = {}
    pos = []
    i = 1
    while i < len(argv):
        if argv[i].startswith('--'):
            opt[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            pos.append(argv[i])
            i += 1
    if kind not in ('writer', 'checker', 'applier', 'filer', 'corrections') or len(pos) != 1 or 'row' not in opt:
        die('usage: thin.py stage writer|checker|applier|filer --row W-BW1 DIR [--unit F] [--report F] [--notes F] [--unsure F]')
    out = pathlib.Path(pos[0])
    if out.exists() and any(out.iterdir()):
        die(f'{out} is not empty')
    out.mkdir(parents=True, exist_ok=True)
    import next_prompt as np
    import mdcourse
    rs = np.rows()
    r = next((x for x in rs if x['row'] == opt['row']), None)
    if r is None:
        die(f"no row {opt['row']}")
    c, code = r['c'], r['code']
    data = ROOT / c['data']
    ddir = data.parent
    case = next(ddir.glob('case-*.md'), None) or next(ddir.glob('case-facts.md'), None)
    sp = c['sourcing_part'][5:]

    def put(src, name=None):
        src = pathlib.Path(src)
        if not src.exists():
            die(f'missing {src}')
        shutil.copyfile(src, out / (name or src.name))

    def brief():
        (out / 'brief.txt').write_text(mdcourse.open_brief(r['d'], r['sc'], r['unit']), encoding='utf-8')

    if kind == 'writer':
        brief()
        put(ROOT / 'skills' / 'write-unit' / 'SKILL.md', 'write-unit-SKILL.md')
        put(ROOT / 'docs' / 'sourcing-standard.md')
        put(R / 'viz.py')
        if case:
            put(case)
        (out / 'sources').mkdir()
        for f in np.sources(r['d'].AIMS[code][1]):
            put(f, 'sources/' + f.name)
            fc = ROOT / 'audits' / 'brand-ai' / f'fresh-check-{re.match(r"((?:DD-)?[A-Z]+\d+)", f.name).group(1)}.md'   # W-BW5: a deep dive's code has a hyphen
            if fc.exists():
                put(fc, 'sources/' + fc.name)
        (out / 'filed').mkdir()
        for x in r['order']:
            if x in r['filed']:
                put(r['filed'][x], 'filed/' + r['filed'][x].name)
        (out / 'flags.txt').write_text('\n'.join(np.flags(r)), encoding='utf-8')
        (out / 'course-map.txt').write_text(                # W-BW5 (flags F3, F22): every unit's code, title, Aim and Gives line
            'Course map: every unit of the course, in order, with its Aim and its Gives line (what later units take from it).\n\n'
            + '\n'.join(f"{u[0]} · {u[1]}" + (f" — Aim: {r['d'].AIMS[u[0]][0]}. Gives: {r['d'].AIMS[u[0]][2]}." if u[0] in getattr(r['d'], 'AIMS', {}) else '')
                         for u in r['sc']['units']) + '\n', encoding='utf-8')
        (out / 'out').mkdir()
    elif kind == 'checker':
        brief()
        for k in ('unit', 'notes', 'unsure'):
            if k not in opt:
                die(f'--{k} is required')
            put(opt[k], f'{k}.md')
        put(ROOT / 'skills' / 'audit-units' / 'SKILL.md', 'audit-units-SKILL.md')
        put(ROOT / 'docs' / 'sourcing-standard.md')
        if case:
            put(case)
        (out / 'out').mkdir()
    elif kind == 'corrections':                              # W-BW5 (15 Nov 2026): the corrections checker's packet (steps 1b and 7b)
        if 'text' not in opt:
            die('--text (the corrections, as written) is required')
        put(opt['text'], 'corrections.md')
        (out / 'files').mkdir()
        for f in [x for x in opt.get('files', '').split(',') if x]:
            put(ROOT / f, 'files/' + pathlib.Path(f).name)
        (out / 'briefs').mkdir()
        for u in [x for x in opt.get('briefs', '').split(',') if x]:
            ur = next((x for x in rs if x['c']['id'] == c['id'] and x['code'] == u), None)
            if ur is None:
                die(f'no unit {u} in {c["id"]}')
            (out / 'briefs' / f'{u}.txt').write_text(mdcourse.open_brief(ur['d'], ur['sc'], ur['unit']), encoding='utf-8')
        put(ddir / 'syllabus-flags.md')
        if case:
            put(case)
        put(ROOT / 'docs' / 'sourcing-standard.md')
        (out / 'out').mkdir()
    elif kind == 'applier':
        for k in ('unit', 'report'):
            if k not in opt:
                die(f'--{k} is required')
            put(opt[k], f'{k}.md')
        cmd_fixes(opt['report'], str(out / 'fixes.json'))
        (out / 'out').mkdir()
    else:
        for k in ('unit', 'notes', 'unsure', 'report'):
            if k not in opt:
                die(f'--{k} is required')
            put(opt[k], f'{k}.md')
        put(data, 'hub.py')
        put(ddir / 'syllabus-flags.md')
        if case:
            put(case)
        ix = (ROOT / 'docs' / 'courses-index.md').read_text(encoding='utf-8')
        import datetime                                      # C4, 15 Nov 2026: what the filer counts from, and the forms it copies
        (out / 'corrections').mkdir()
        for f in sorted((ROOT / 'audits' / c['id']).glob(f"corrections-{opt.get('date', datetime.date.today().isoformat())}-*.md")):
            put(f, 'corrections/' + f.name)
        if opt.get('stats'):
            (out / 'stats').mkdir()
            for j, f in enumerate(x for x in opt['stats'].split(',') if x):
                put(f, f'stats/{j + 1}-' + pathlib.Path(f).parent.name + '.json')
        (out / 'filer-rules.txt').write_text(
            'Rules for records.json (C4, 15 Nov 2026):\n'
            '1. Every count you write (findings, fixes applied and held, private-unit or filed-unit replacements, flags) is taken from '
            'the corrections reports in corrections/ and the stats files in stats/, counted there, never estimated. A corrections '
            'report counts each replacement it passed; give the total and how many were applied.\n'
            '2. The index status cell of this unit copies the form of the last filed row of this course in index-rows.txt, word for '
            'word but for the code, the date and the report path.\n'
            "3. index_edits always sets the course's count line (\"N of M written\") to the new count, and the unit's row; each old "
            'text is copied exactly from index-rows.txt and occurs once in docs/courses-index.md.\n'
            '4. thin.py insert runs kit/index_check.py after inserting and restores every file if it fails.\n', encoding='utf-8')
        secs = re.split(r'(?m)^(?=## )', ix)                  # C4: the course's whole section (count line, last filed row, this row)
        sec = next((s for s in secs if c['vault'] in s), None)
        stl = next((s for s in secs if s.startswith('## Staleness')), '')   # W-BW5: the staleness table, where a search-on unit gets its row
        sec = (sec or '') + ('\n' + stl if stl else '')
        (out / 'index-rows.txt').write_text(sec if sec else '\n'.join(ln for ln in ix.splitlines() if re.search(r'\b' + re.escape(code) + r'\b', ln)), encoding='utf-8')
        (out / 'records.template.json').write_text(json.dumps(dict(
            row=opt['row'], code=code, course=c['id'], date='YYYY-MM-DD hh:mm',
            reading=dict(id=f'read-{code.lower()}', course=r['sc']['key'], title=r['unit'][1], covers=[code], name=f'{code} · {r["unit"][1]}', intro='…'),
            status='written D Mon', next_unit='…', version='vN · D Mon 2026', hub_changelog='vN. …',
            case_lines=[], flag_rows=[dict(date='D Mon 2026', raised_by=code, affects='…', flag='…', proposed='…')], flags_carried=[],
            index_edits=[dict(old='exact text of the row now', new='the row as filed')],
            changelog_row=dict(date='D Mon 2026', chat='…', model='…', result='…'), kit_bullet='- **…**', kit_session=dict(heading='D Mon 2026 · Session N · …', body='…')),
            ensure_ascii=False, indent=1), encoding='utf-8')
        (out / 'out').mkdir()
    print(f'{kind} packet for {opt["row"]} in {out}: ' + ', '.join(sorted(str(p.relative_to(out)) for p in out.rglob('*') if p.is_file())))


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        die(__doc__)
    cmd = a[0]
    if cmd == 'fixes' and len(a) == 3:
        cmd_fixes(a[1], a[2])
    elif cmd == 'apply' and len(a) == 4:
        cmd_apply(a[1], a[2], a[3])
    elif cmd == 'insert' and len(a) == 2:
        cmd_insert(a[1])
    elif cmd == 'save-report':
        cmd_save_report(a[1:])
    elif cmd == 'assemble' and len(a) == 4:
        cmd_assemble(a[1], a[2], a[3])
    elif cmd == 'stats' and len(a) == 2:
        cmd_stats(a[1])
    elif cmd == 'correct':
        cmd_correct(a[1:])
    elif cmd == 'stage':
        cmd_stage(a[1:])
    else:
        die(__doc__)
