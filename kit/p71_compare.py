"""P71-3 step 5, the mechanical check: every history report page built from the vault against the same page built
from the HTML fragments on main at the start (a copy of that build's academy/ folder). For each of the reports: the
visible text equal (entities resolved, whitespace runs collapsed) and every figure's SVG identical.

  python3 p71_compare.py <the earlier academy/ folder>
"""
import re, sys, pathlib, json, html as H
from html.parser import HTMLParser
from courses import HISTORY

R = pathlib.Path(__file__).resolve().parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, t, a):
        if t in ('script', 'style'):
            self.skip += 1

    def handle_endtag(self, t):
        if t in ('script', 'style'):
            self.skip -= 1

    def handle_data(self, d):
        if not self.skip:
            self.out.append(d)


TABLE = re.compile(r'\s*(</?(?:table|thead|tbody|tr|th|td|p|li|ol|ul|h[1-6]|details|summary|blockquote|aside|div|section|nav|figure|figcaption|header)\b[^>]*>)\s*')


def text(h):
    """The page's text as a reader sees it. Whitespace at the edge of a block (a table's cells and rows, a paragraph, a
    list item, a details box) is not drawn: a browser starts each block on its own line and drops the spaces and line
    breaks around it. So each block tag counts as one space on both sides, before and after."""
    h = TABLE.sub(r'\1 ', h)
    p = Text(); p.feed(h); p.close()
    return re.sub(r'\s+', ' ', ''.join(p.out).replace('⁠', '⁠')).strip()


def svgs(h):
    return [re.sub(r'\s+', ' ', x) for x in re.findall(r'<svg\b.*?</svg>', h, re.S)]


def main(before):
    before = pathlib.Path(before)
    bad, n, nfig = [], 0, 0
    for c in HISTORY:
        for i in json.load(open(R / c['prompts'])):
            a = (before / c['id'] / f'r-{i}.html').read_text(encoding='utf-8')
            b = (R / 'academy' / c['id'] / f'r-{i}.html').read_text(encoding='utf-8')
            n += 1
            ta, tb = text(a), text(b)
            if ta != tb:
                k = next((j for j in range(min(len(ta), len(tb))) if ta[j] != tb[j]), min(len(ta), len(tb)))
                bad.append(f'{c["id"]} {i}: text differs at {k}: {ta[max(0, k - 80):k + 80]!r} / {tb[max(0, k - 80):k + 80]!r}')
            sa, sb = svgs(a), svgs(b)
            nfig += len(sa)
            if sa != sb:
                bad.append(f'{c["id"]} {i}: {len(sa)} figures before, {len(sb)} after, {sum(x != y for x, y in zip(sa, sb))} drawn differently')
    print('\n'.join(bad))
    print(f'{n} report pages compared, {nfig} figures; {len(bad)} differ')
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
