"""P91 (4 Nov 2026), step 2: date every Greece and Rome report by the work session that filed it, from CHANGELOG.md.

python3 p91_dates.py [--write]

Pedro, 4 Nov 2026: history reports are dated "by work session". The sessions that filed history reports are the ones
whose "At a glance" row raises the Greece or Rome count. In each, the report numbers are read from the session's
title and from its lead lines (a bullet or paragraph that opens in bold: "**Units 0 to 2:**", "**4.1 to 4.5:**",
"**The modules.** 11.3 ..."), in the course the line names (Rome, Roman; Greece, Greek), else the course of the
heading or title it sits under. A lead line that repoints, logs or concerns an audit unit (a pointer, a correction,
session 1's "Unit 12, a quality audit (12.1 to 12.5)", the old audit unit) files nothing and is skipped. "unit N", "units N to M", "units N and M" and "units N, M and K" are whole syllabus units; "a.b to a.c" a
range; "a.b" one module. Only modules in the course's prompts index count; a module takes the first session that
names it. The count each session files must equal the rise its "At a glance" row shows, or the script stops.

A session dated "22 to 24 October 2026" gives its first day, and its modules go in `written_approx` ({course:
[modules]}) beside the `written` map ({course: {module: ISO date}}), so the page can mark the date approximate. A
report no session names is left undated and printed. With --write, provenance.json is rewritten with both maps.
"""
import json, re, sys, pathlib, datetime

R = pathlib.Path(__file__).resolve().parent
CL = (R / 'CHANGELOG.md').read_text(encoding='utf-8').split('\n')
from courses import HISTORY, path as cpath, provenance, save_provenance   # S-DEC5: the inputs are in the course folders
INDEX = {c['id']: list(json.load(open(cpath(c, 'prompts')))) for c in HISTORY}
MONTHS = {m: i for i, m in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                                      'September', 'October', 'November', 'December'], 1)}
SKIP = re.compile(r'pointer|repoint|correction|flagged|logged|audit', re.I)


def course_of(text, default):
    g = re.search(r'\bGree(?:ce|k)\b', text)
    r = re.search(r'\bRom(?:e|an)\b', text)
    if g and r:
        return 'greece' if g.start() < r.start() else 'rome'
    return 'greece' if g else 'rome' if r else default


def modules(text, course):
    """The modules a piece of text names, in the order it names them."""
    idx = INDEX[course]
    out = []
    def unit(u):
        return [m for m in idx if m.split('.')[0] == str(u)]
    t = text
    for m in re.finditer(r'\b(\d+)\.(\d+) to (\d+)\.(\d+)\b', t):
        a, b, c, d = map(int, m.groups())
        if a == c:
            out += [f'{a}.{k}' for k in range(b, d + 1)]
    t = re.sub(r'\b\d+\.\d+ to \d+\.\d+\b', ' ', t)
    # "units 8 to 10", "units 5 and 6", "units 11, 12 and 13" (a list only with "units" and its "and"); then "unit 7"
    for m in re.finditer(r'\b[Uu]nits (\d+(?:, \d+)*) (to|and) (\d+)\b', t):
        first = [int(x) for x in m.group(1).split(', ')]
        nums = list(range(first[0], int(m.group(3)) + 1)) if m.group(2) == 'to' else first + [int(m.group(3))]
        for u in nums:
            out += unit(u)
    t = re.sub(r'\b[Uu]nits \d+(?:, \d+)* (?:to|and) \d+\b', ' ', t)
    for m in re.finditer(r'\b[Uu]nits? (\d+)\b(?!\.)', t):
        out += unit(int(m.group(1)))
    t = re.sub(r'\b[Uu]nits? \d+\b(?!\.)', ' ', t)
    out += re.findall(r'(?<![\d.(])(\d+\.\d+)(?![\d.)])', t)
    return [m for m in out if m in idx]


def sessions():
    """(number, heading date text, body lines) of every session entry."""
    out, cur = [], None
    for ln in CL:
        m = re.match(r'## (.+?) · Session (\d+) · (.*)$', ln)
        if m:
            cur = (int(m.group(2)), m.group(1), m.group(3), [])
            out.append(cur)
        elif ln.startswith('## '):
            cur = None
        elif cur:
            cur[3].append(ln)
    return out


def glance():
    """The "At a glance" table: {session number: (greece count, rome count)}, blanks carried from the row before."""
    rows, g, r = {}, 0, 0
    on = False
    for ln in CL:
        if ln.startswith('## At a glance'):
            on = True; continue
        if on and ln.startswith('## '):
            break
        if on and ln.startswith('| ') and not ln.startswith('| Date'):
            c = [x.strip() for x in ln.strip().strip('|').split('|')]
            n = re.match(r'(\d+)\.', c[1])
            if not n:
                continue
            g = int(re.findall(r'\d+', c[2])[-1]) if re.search(r'\d', c[2]) else g
            r = int(re.findall(r'\d+', c[3])[-1]) if re.search(r'\d', c[3]) else r
            rows[int(n.group(1))] = (g, r)
    return rows


def first_day(head):
    m = re.match(r'(\d+)(?: to (\d+))?(?: (\w+))? (\w+) (\d{4})$', head.strip())
    if not m:
        raise SystemExit(f'cannot read the date {head!r}')
    d1, d2, mon1, mon2, y = m.groups()
    mon = MONTHS[mon1] if mon1 in MONTHS else MONTHS[mon2]
    return datetime.date(int(y), mon, int(d1)).isoformat(), bool(d2)


def main():
    gl = glance()
    nums = sorted(gl)
    rise = {}
    prev = (0, 0)
    for n in nums:
        g, r = gl[n]
        if (g, r) != prev and (g > prev[0] or r > prev[1]):
            rise[n] = (g - prev[0], r - prev[1])
        prev = (max(prev[0], g), max(prev[1], r))
    written = {'greece': {}, 'rome': {}}
    approx = {'greece': [], 'rome': []}
    where = {}
    for num, head, title, body in sorted(sessions()):
        if num not in rise:
            continue
        iso, spans = first_day(head)
        default = course_of(title, None)
        found = {'greece': [], 'rome': []}
        # the title, segment by segment, each in the course it names (else the one before it)
        ctx = default
        for seg in re.split(r', | then |: ', title):
            ctx = course_of(seg, ctx)
            if ctx:
                found[ctx] += modules(seg, ctx)
        ctx = default
        for ln in body:
            if ln.startswith('### '):
                ctx = course_of(ln, ctx); continue
            lead = re.match(r'\s*(?:- )?\*\*(.+?)\*\*(.*)$', ln)
            if not lead or ln.startswith('  '):
                continue
            if SKIP.search(ln):
                continue
            c = course_of(lead.group(1), ctx)
            if c:
                found[c] += modules(lead.group(1) + ' ' + lead.group(2), c)
        new = {'greece': [], 'rome': []}
        for c in found:
            for m in found[c]:
                if m not in written[c] and m not in new[c]:
                    new[c].append(m)
        want = rise[num]
        got = (len(new['greece']), len(new['rome']))
        if got != want:
            raise SystemExit(f'session {num}: the text names {got[0]} new Greece and {got[1]} new Rome reports, "At a glance" shows {want}: '
                             f'{new}')
        for c in new:
            for m in new[c]:
                written[c][m] = iso
                where[(c, m)] = (num, head)
                if spans:
                    approx[c].append(m)
    undated = {c: [m for m in INDEX[c] if m not in written[c]] for c in INDEX}
    # in syllabus order
    written = {c: {m: written[c][m] for m in INDEX[c] if m in written[c]} for c in written}
    approx = {c: [m for m in INDEX[c] if m in approx[c]] for c in approx}
    return written, approx, where, undated, rise


if __name__ == '__main__':
    written, approx, where, undated, rise = main()
    for c in written:
        by = {}
        for m, d in written[c].items():
            by.setdefault(where[(c, m)], []).append(m)
        for (num, head), ms in sorted(by.items()):
            print(f'{c} session {num} ({head}) -> {written[c][ms[0]]}{" approximate" if ms[0] in approx[c] else ""}: {len(ms)} reports: {", ".join(ms)}')
    print(f'dated: {sum(len(v) for v in written.values())}; approximate: {sum(len(v) for v in approx.values())}; '
          f'undated: {sum(len(v) for v in undated.values())} {undated if any(undated.values()) else ""}')
    if '--write' in sys.argv:
        prov = provenance()
        prov['written'] = written
        prov['written_approx'] = approx
        save_provenance(prov)
        print('provenance.json: written and written_approx filled')
