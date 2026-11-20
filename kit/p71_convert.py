"""P71-3 (1 Nov 2026): the one-time conversion of the history reports from the kit's HTML fragments
(kit/<course>/r-<id>.html) to Markdown files in the vault (courses/<course>/<id>-<slug>.md), with front matter per
docs/method.md §7. Kept as the record of how the vault files were made; the forms it writes are the ones
mdcourse.history_html reads (docs/p71-3.md). No report's content changes: `--check` renders every converted file back
and compares it with the fragment it came from (the text and every figure's drawing), and a difference stops it.

  python3 p71_convert.py <dir>            convert every written report from <dir>/<course>/r-<id>.html, then check
  python3 p71_convert.py <dir> --check    check only (the vault against those fragments)
The fragments left the kit with this conversion (they are in git history before P71-3: `git show d71ea81:kit/greece/r-6.3.html`).
"""
import html as H, json, re, sys, pathlib
from html.parser import HTMLParser
import mdcourse, viz
from courses import HISTORY, path as cpath, provenance

R = pathlib.Path(__file__).resolve().parent
REPO = R.parent
PROV = provenance()

# `written` from the record (kit/CHANGELOG.md's sessions; the vault for 1 Nov 2026); a module whose session spans two
# days is left without one (docs/p71-3.md lists them)
WRITTEN = {
    'greece': [(r'^12\.', '2026-10-25')],
    'rome': [(r'^[0-4]\.', '2026-10-24'), (r'^7\.', '2026-10-25'), (r'^(8|9|10)\.|^11\.[12]$|^13\.[12]$', '2026-10-25'),
             (r'^11\.[3-8]$|^12\.|^13\.[3-8]$', '2026-11-01')],
}
VOID = {'br', 'wbr', 'img'}


class Node:
    def __init__(self, tag, attrs=None, parent=None):
        self.tag, self.attrs, self.kids, self.parent = tag, dict(attrs or {}), [], parent


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = self.cur = Node('#root')
        self.raw = None

    def handle_starttag(self, t, a):
        n = Node(t, a, self.cur)
        self.cur.kids.append(n)
        if t not in VOID:
            self.cur = n

    def handle_endtag(self, t):
        if t in VOID:
            return
        assert self.cur.tag == t, f'unbalanced </{t}> in <{self.cur.tag}>'
        self.cur = self.cur.parent

    def handle_data(self, d):
        self.cur.kids.append(d)


def parse(s):
    p = Tree()
    p.feed(s)
    p.close()
    return p.root


def raw_pre(frag):
    """The raw text of every <pre class="tree">, in order (the parser has already unescaped it)."""
    return [H.unescape(x) for x in re.findall(r'<pre class="tree">(.*?)</pre>', frag, re.S)]


def esc(t):
    t = t.replace('\\', '\\\\')
    for ch in '*_`[]':
        t = t.replace(ch, '\\' + ch)
    return t.replace('<', '&lt;')


def inline(n, depth=0):
    out = ''
    for k in n.kids:
        if isinstance(k, str):
            out += esc(re.sub(r'\s+', ' ', k))
            continue
        inner = inline(k, depth + 1)
        lead = re.match(r'\s*', inner).group(0)
        trail = re.search(r'\s*$', inner).group(0)
        core = inner.strip()
        if k.tag == 'em':
            mark = '_' if n.tag == 'strong' or depth else '*'
            out += f'{lead}{mark}{core}{mark}{trail}' if core else inner
        elif k.tag == 'strong':
            out += f'{lead}**{core}**{trail}' if core else inner
        elif k.tag in ('sup', 'sub'):
            out += f'<{k.tag}>{inner}</{k.tag}>'
        else:
            raise SystemExit(f'inline <{k.tag}> has no Markdown form')
    return out


def start_safe(s):
    """A paragraph's first characters that Markdown would read as a block marker are escaped."""
    s = s.lstrip()
    if re.match(r'(#|>|[-+] |\d+[.)] )', s):
        m = re.match(r'(\d+)([.)])', s)
        s = (m.group(1) + '\\' + m.group(2) + s[m.end():]) if m else '\\' + s
    return s


def table(n):
    rows = []
    for part in n.kids:
        if isinstance(part, str):
            assert not part.strip()
            continue
        for tr in part.kids:
            if isinstance(tr, str):
                assert not tr.strip()
                continue
            rows.append([inline(c).strip().replace('|', '\\|') for c in tr.kids if not isinstance(c, str)])
    head, body = rows[0], rows[1:]
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * len(head)]
    out += ['| ' + ' | '.join(r) + ' |' for r in body]
    return '\n'.join(out)


def indent(s, n=4):
    return '\n'.join((' ' * n + ln) if ln else ln for ln in s.split('\n'))


class Conv:
    def __init__(self, frag):
        self.pres = raw_pre(frag)
        self.npre = 0
        self.caps = re.findall(r'<figcaption>(.*?)</figcaption>', frag, re.S)    # captions kept exactly, entities too
        self.ncap = 0

    def pre(self, n):
        txt = self.pres[self.npre]
        self.npre += 1
        return '```tree\n' + txt + '\n```'

    def figure(self, n):
        kind = n.attrs['data-viz']
        js = cap = None
        for k in n.kids:
            if isinstance(k, str):
                continue
            if k.tag == 'script':
                js = ''.join(x for x in k.kids if isinstance(x, str))
            elif k.tag == 'figcaption':
                cap = self.caps[self.ncap]
                self.ncap += 1
        d = json.loads(js)
        d = {'kind': d.pop('kind', kind), **d}
        if cap and not d.get('caption'):
            d['caption'] = cap
        lines = [f' {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}' for k, v in d.items()]
        return '```viz\n{\n' + ',\n'.join(lines) + '\n}\n```'

    def cap_html(self, n):
        out = ''
        for k in n.kids:
            if isinstance(k, str):
                out += H.escape(k, quote=False)
            else:
                out += f'<{k.tag}>{self.cap_html(k)}</{k.tag}>'
        return out

    def li(self, n, k, ordered):
        """One list item: a Self-test item (question, then its answer), or an item of plain text with any quotation or
        tree it holds as indented blocks."""
        mark = f'{k}. ' if ordered else '- '
        det = [x for x in n.kids if not isinstance(x, str) and x.tag == 'details']
        if det:
            d = det[0]
            q = Node('#q'); q.kids = n.kids[:n.kids.index(d)]
            assert not any(not isinstance(x, str) and x.tag == 'details' for x in n.kids[n.kids.index(d) + 1:])
            tail = [x for x in n.kids[n.kids.index(d) + 1:] if not (isinstance(x, str) and not x.strip())]
            assert not tail, 'text after a Self-test answer'
            lab = ''.join(x for x in d.kids[0].kids if isinstance(x, str)) if d.kids and not isinstance(d.kids[0], str) else None
            summ = next(x for x in d.kids if not isinstance(x, str) and x.tag == 'summary')
            lab = ''.join(x for x in summ.kids if isinstance(x, str))
            paras = [x for x in d.kids if not isinstance(x, str) and x.tag == 'p']
            assert len(paras) == len([x for x in d.kids if not isinstance(x, str)]) - 1, 'an answer holds more than paragraphs'
            body = [f'{lab}: ' + inline(paras[0]).strip()] + [start_safe(inline(p).strip()) for p in paras[1:]]
            return mark + start_safe(inline(q).strip()) + '\n\n' + '\n\n'.join(indent(b) for b in body)
        parts, cur = [], Node('#t')
        for x in n.kids:
            if not isinstance(x, str) and x.tag in ('blockquote', 'pre'):
                parts.append(('t', cur)); cur = Node('#t')
                parts.append((x.tag, x))
            else:
                cur.kids.append(x)
        parts.append(('t', cur))
        out = []
        for kind, x in parts:
            if kind == 't':
                s = inline(x).strip()
                if s:
                    out.append(start_safe(s))
            elif kind == 'blockquote':
                out.append('> ' + inline(x).strip())
            else:
                out.append(self.pre(x))
        if len(out) == 1:
            return mark + out[0]
        return mark + out[0] + '\n\n' + '\n\n'.join(indent(b) for b in out[1:])

    def block(self, n):
        t, cls = n.tag, n.attrs.get('class', '')
        if t in ('h2', 'h3'):
            return ('#' * int(t[1])) + ' ' + inline(n).strip()
        if t == 'p':
            return start_safe(inline(n).strip())
        if t == 'aside':
            assert cls == 'dispute'
            s = inline(n).strip()
            assert s.startswith('**Where sources disagree.**'), s[:60]
            return s
        if t == 'blockquote':
            return '> ' + inline(n).strip()
        if t == 'div':
            assert cls == 'tbl'
            tb = [x for x in n.kids if not isinstance(x, str)]
            assert len(tb) == 1 and tb[0].tag == 'table'
            return table(tb[0])
        if t == 'pre':
            assert cls == 'tree'
            return self.pre(n)
        if t == 'figure':
            return self.figure(n)
        if t in ('ol', 'ul'):
            items = [x for x in n.kids if not isinstance(x, str)]
            assert all(x.tag == 'li' for x in items)
            lis = [self.li(x, k + 1, t == 'ol') for k, x in enumerate(items)]
            loose = any('\n' in s for s in lis)
            return ('\n\n' if loose else '\n').join(lis)
        raise SystemExit(f'top-level <{t}> has no Markdown form')

    def run(self, frag):
        root = parse(frag)
        out = []
        for n in root.kids:
            if isinstance(n, str):
                assert not n.strip(), f'loose text at the top level: {n[:60]!r}'
                continue
            out.append(self.block(n))
        assert self.npre == len(self.pres)
        return '\n\n'.join(out) + '\n'


from index_check import slug    # method.md §7, the one slug rule


def front(c, i, title):
    model = PROV.get(c['id'], {}).get(i, c['default_model']).split(',')[0].strip()
    when = next((d for pat, d in WRITTEN[c['id']] if re.search(pat, i)), None)
    fm = ['---', f'code: {i}', f'title: {title}', f'course: {c["id"]} · Personal Mythology · {c["short"]}', f'model: {model}']
    if when:
        fm.append(f'written: {when}')
    return '\n'.join(fm + ['search: off', '---', ''])


# ---- the check: the fragment and the Markdown render to the same text and the same drawings -----------------------
BLOCK = r'(?:p|li|ul|ol|h2|h3|div|table|thead|tbody|tr|td|th|blockquote|aside|figure|figcaption|details|summary|pre|svg|g)'


def canon(h):
    """HTML normalised for comparison: entities resolved, whitespace runs collapsed, whitespace at block tags dropped;
    the text inside <pre> kept exactly."""
    pres = []
    h = re.sub(r'(<pre class="tree">)(.*?)(</pre>)', lambda m: m.group(1) + f'\x00{pres.append(H.unescape(m.group(2))) or len(pres) - 1}\x00' + m.group(3), h, flags=re.S)
    h = H.unescape(h)
    h = re.sub(r'\s+', ' ', h)
    h = re.sub(rf'\s*(</?{BLOCK}\b[^>]*>)\s*', r'\1', h)
    return h.strip(), pres


def drawn_fragment(frag):
    return viz.render_html(frag)


def vault_path(c, i):
    return REPO / 'courses' / c['id'] / f'{i}-{slug(c["index"][i]["title"])}.md'


def check(c, i, frag):
    md = vault_path(c, i).read_text(encoding='utf-8')
    a = canon(drawn_fragment(frag))
    b = canon(mdcourse.history_html(md))
    if a != b:
        x, y = a[0], b[0]
        k = next((j for j in range(min(len(x), len(y))) if x[j] != y[j]), min(len(x), len(y)))
        return f'{c["id"]} {i}: differs at {k}:\n  fragment: {x[max(0, k - 120):k + 160]!r}\n  markdown: {y[max(0, k - 120):k + 160]!r}' if x != y else f'{c["id"]} {i}: a tree differs'
    return None


def main():
    only_check = '--check' in sys.argv
    frags = pathlib.Path(next(a for a in sys.argv[1:] if not a.startswith('--')))
    bad, n = [], 0
    for c in HISTORY:
        c['index'] = json.load(open(cpath(c, 'prompts')))
        (REPO / 'courses' / c['id']).mkdir(parents=True, exist_ok=True)
        for i, meta in c['index'].items():
            src = frags / c['id'] / f'r-{i}.html'
            frag = src.read_text(encoding='utf-8')
            if not only_check:
                md = front(c, i, meta['title']) + '\n# ' + meta['title'] + '\n\n' + Conv(frag).run(frag)
                vault_path(c, i).write_text(md, encoding='utf-8')
            err = check(c, i, frag)
            n += 1
            if err:
                bad.append(err)
    for b in bad:
        print(b)
    print(f'{n} reports converted and checked; {len(bad)} differ')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
