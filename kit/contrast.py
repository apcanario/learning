"""WCAG 2.x contrast of the theme's light accent tokens against the two light surfaces (P90, 4 Nov 2026).

python3 contrast.py [theme.css]  (default ../design/theme.css)
Reads the light block of section 1 and prints, for every accent token and --dim / --muted / --fg: its contrast on --bg
(the paper) and on --card, and for the accents the contrast of --on-accent text on the accent (a filled button), plus
the eyebrow's .u (the accent mixed 78% with --fg, theme 4a) on both surfaces, and the accent on its own track band
(theme 8: 7% of it over the paper, the darkest surface an accent is text on: the band's "Track" label). Exits 1 if any pair is under 4.5:1.
verify.py runs the same pairs on the built page's computed colours; this is the quick check used to pick the values."""
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
    sys.exit(1 if low else 0)
