"""WCAG 2.x contrast of the theme's light accent tokens against the two light surfaces (P90, 4 Nov 2026).

python3 contrast.py [theme.css]  (default ../design/theme.css)
Reads the light block of section 1 and prints, for every accent token and --dim / --muted / --fg: its contrast on --bg
(the paper) and on --card, and for the accents the contrast of --on-accent text on the accent (a filled button), plus
the eyebrow's .u (the accent mixed 78% with --fg, theme 4a) on both surfaces, and the accent on its own track band
(theme 8: 7% of it over the paper, the darkest surface an accent is text on: the band's "Track" label). Exits 1 if any pair is under 4.5:1.
verify.py runs the same pairs on the built page's computed colours; this is the quick check used to pick the values.
P91 (4 Nov 2026): then the home's new pairs in both themes: a written spine's code (--on-accent on each accent), a
planned spine's code and the volume's label (--muted on --bg), the lit label (--fg on --bg; its arrow, a symbol, the
accent on --bg at 3:1), the shelf's course labels (--fg) and notes (--muted), the live totals (--fg, their labels
--muted), What's new's approximate mark (--muted on --card). Exits 1 if any of these is under its bar either. The dark
accents as text on the page are printed for the record (the house palette, which does not change: blue gives 4.31:1,
so the shelf names its tracks in --fg with the tone as a mark).
P92 (4 Nov 2026): the shelf's pairs are gone with it; the hero's pairs in both themes instead: each area word of the
cycling line and the static line in its area's tone (History red, Marketing teal, Technology purple, User Experience
blue) on the page (--bg: dark, the page; light, the paper), large text (28 px, 600), at 3:1; the static line's dots
(--muted); the headline (--fg, large); the lede (--muted) and the quiet What's new link (--fg, its arrow --muted) at
4.5:1; and every one of them over a contour line of each area's tone at the hero's opacity (--topo-a composited over
--bg, the densest a line gets: two crossing lines never share a pixel at 1 px and full coverage), at the same bars.
verify.py measures the same texts on the built page, pixel by pixel, over the lines actually under them.
P93 (4 Nov 2026): a course home's and What's new's hero texts (the crumbs, the eyebrow and its course label, the
headline, the lede, the outlined button, the flag) over a line of every tone at --topo-a, one line and two stacked in a
pixel, in both themes; and the tile's texts (its chip on each tone, a ghost's outlined chip and line, its title, line
and stats on a card, the status pills on a card). Exits 1 if any is under its bar. verify.py measures the heroes on
the built page at five poses of the move, which is the authority: two rings rarely pass within a pixel."""
import re, sys, pathlib

def rgb(h):
    h = h.lstrip('#'); h = ''.join(c * 2 for c in h) if len(h) == 3 else h
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(v) for v in c)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

def mix(a, b, p):   # color-mix(in srgb, a p, b)
    return tuple(round(x * p + y * (1 - p)) for x, y in zip(a, b))

def dark_tokens(css):
    blk = re.search(r'\n:root\{(.*?)\}', css, re.S).group(1)
    return dict(re.findall(r'--([\w-]+):(#[0-9a-fA-F]{3,6})', blk))

def alpha(css, name, block):
    return float(re.search(r'--' + name + r':([\d.]+)', block).group(1))

def light_tokens(css):
    blk = re.search(r':root\[data-theme="light"\]\{(.*?)\}', css, re.S).group(1)
    return dict(re.findall(r'--([\w-]+):(#[0-9a-fA-F]{3,6})', blk))

ACCENTS = ['red', 'orange', 'teal', 'blue', 'purple', 'gold']

def table(tok):
    bg, card, fg, on = rgb(tok['bg']), rgb(tok['card']), rgb(tok['fg']), rgb(tok['on-accent'])
    rows = []
    for k in ACCENTS + ['dim', 'muted', 'fg']:
        c = rgb(tok[k])
        r = [k, tok[k], ratio(c, bg), ratio(c, card)]
        if k in ACCENTS:
            u = mix(c, fg, .78)
            r += [ratio(on, c), ratio(u, bg), ratio(u, card), ratio(c, mix(c, bg, .07))]
        rows.append(r)
    return rows

if __name__ == '__main__':
    css = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).resolve().parent.parent / 'design/theme.css').read_text()
    tok = light_tokens(css)
    print(f"light surfaces: --bg {tok['bg']} · --card {tok['card']} · --line {tok['line']} · --line-2 {tok['line-2']} · --on-accent {tok['on-accent']}")
    print(f"{'token':8} {'value':8} {'on bg':>6} {'on card':>7} {'button':>6} {'.u bg':>6} {'.u card':>7} {'band':>6}")
    low = []
    for r in table(tok):
        cells = ' '.join(f'{v:6.2f}' for v in r[2:4]) + ('  ' + ' '.join(f'{v:6.2f}' for v in r[4:]) if len(r) > 4 else '')
        print(f'{r[0]:8} {r[1]:8} {cells}')
        low += [f'{r[0]} {v:.2f}' for v in r[2:] if v < 4.5]
    print('ALL PAIRS >= 4.5:1' if not low else 'UNDER 4.5:1: ' + ', '.join(low))
    # P91's shelf pairs went with the shelf (P92); the dark accents as text on the page, for the record
    dk = dark_tokens(css)
    print('(record) dark accents as text on --bg: ' + ', '.join(f'{a} {ratio(rgb(dk[a]), rgb(dk["bg"])):.2f}' for a in ACCENTS))
    # P92: the hero's texts, on the page and over the densest contour line of each area's tone
    AREAS = [('History', 'red'), ('Marketing', 'teal'), ('Technology', 'purple'), ('User Experience', 'blue')]
    blocks = {'dark': re.search(r'\n:root\{(.*?)\}', css, re.S).group(1), 'light': re.search(r':root\[data-theme="light"\]\{(.*?)\}', css, re.S).group(1)}
    for name, t in (('light', tok), ('dark', dark_tokens(css))):
        bg, fg, mu = (rgb(t[k]) for k in ('bg', 'fg', 'muted'))
        a = alpha(css, 'topo-a', blocks[name])
        under = [('the page', bg)] + [(f'a {tn} line at {a}', mix(rgb(t[tn]), bg, a)) for _, tn in AREAS]
        print(f"P92 hero pairs, {name} (--bg {t['bg']}, contour lines at --topo-a {a}):")
        texts = [(f'area word {w} ({tn}, large)', rgb(t[tn]), 3) for w, tn in AREAS]
        texts += [('headline Academy (fg, large)', fg, 3), ('static line dots (muted)', mu, 4.5), ('lede (muted)', mu, 4.5),
                  ("What's new link (fg)", fg, 4.5), ("What's new arrow (muted)", mu, 4.5)]
        for what, c, bar in texts:
            vs = [(where, ratio(c, b)) for where, b in under]
            worst = min(vs, key=lambda x: x[1])
            print(f'  {what:36} on the page {vs[0][1]:5.2f}; lowest over a line {min(v for _, v in vs[1:]):5.2f} ({worst[0]})' + ('' if worst[1] >= bar else f'  UNDER {bar}:1'))
            if worst[1] < bar:
                low.append(f'{name} {what} {worst[1]:.2f} ({worst[0]})')
    print('P92: ALL HOME PAIRS PASS' if not low else 'UNDER THE BAR: ' + ', '.join(low))
    # P93: a course home's and What's new's hero texts over the contour lines of every tone at --topo-a (one line, and
    # two lines stacked in one pixel, where two rings pass within a pixel of each other: alpha 1 - (1 - a)^2), and the
    # tile's texts: the chip (--on-accent on the tone), a ghost's outlined chip (--fg on --card and --bg), a ghost's line
    # (--muted), a tile's title, stats and line (--fg, --muted on --card), the status pills on a tile (on --card)
    low93 = []
    for name, t in (('light', tok), ('dark', dark_tokens(css))):
        bg, card, fg, mu, on = (rgb(t[k]) for k in ('bg', 'card', 'fg', 'muted', 'on-accent'))
        a = alpha(css, 'topo-a', blocks[name]); a2 = 1 - (1 - a) ** 2
        print(f"P93 pairs, {name} (contour lines at --topo-a {a}; two stacked {a2:.3f}). The bar is over one line; since the follow-up of 5 Nov 2026 the layer carries the opacity, so two lines stacked in one pixel composite as one and the two-stacked column is a record of the old worst case only; verify.py measures every hero text on the built page, pixel by pixel, at five poses of the move, and that is the authority:")
        hero = [('crumb link, separator (muted)', mu, 4.5), ('crumb here (fg)', fg, 4.5), ('eyebrow (muted)', mu, 4.5), ('headline (fg, large)', fg, 3),
                ('lede (muted)', mu, 4.5), ('outlined button label (muted)', mu, 4.5), ('outlined button title (fg)', fg, 4.5), ('flag (muted)', mu, 4.5)]
        hero += [(f'eyebrow course label ({c}: .u, 78% with fg)', mix(rgb(t[c]), fg, .78), 4.5) for c in ACCENTS]
        for what, c, bar in hero:
            one = min(ratio(c, mix(rgb(t[tn]), bg, a)) for tn in ACCENTS)
            two = min(ratio(c, mix(rgb(t[tn]), bg, a2)) for tn in ACCENTS)
            print(f'  {what:44} on the page {ratio(c, bg):5.2f}; over one line {one:5.2f}; over two stacked {two:5.2f} (record)' + ('' if one >= bar else f'  UNDER {bar}:1'))
            if one < bar: low93.append(f'{name} {what} {one:.2f}')
        tiles = [(f'chip on {c} (on-accent)', on, rgb(t[c]), 4.5) for c in ACCENTS]
        tiles += [('ghost chip on card (fg)', fg, card, 4.5), ('ghost chip on page (fg)', fg, bg, 4.5), ('ghost line on card (muted)', mu, card, 4.5), ('ghost line on page (muted)', mu, bg, 4.5),
                  ('tile title on card (fg)', fg, card, 4.5), ('tile line and stat labels on card (muted)', mu, card, 4.5)]
        tiles += [(f'pill {k} on card ({c}, 78% with fg)', mix(rgb(t[c]), fg, .78), card, 4.5) for k, c in (('live', 'teal'), ('prog', 'gold'), ('unck', 'orange'), ('next', 'blue'))]
        tiles += [('plain pill on card (muted: soon, not run yet)', mu, card, 4.5), ('plain pill on page (muted)', mu, bg, 4.5)]
        for what, c, b, bar in tiles:
            r = ratio(c, b)
            print(f'  {what:44} {r:5.2f}' + ('' if r >= bar else f'  UNDER {bar}:1'))
            if r < bar: low93.append(f'{name} {what} {r:.2f}')
    print('P93: ALL NEW PAIRS PASS' if not low93 else 'P93 UNDER THE BAR: ' + ', '.join(low93))
    sys.exit(1 if low or low93 else 0)
