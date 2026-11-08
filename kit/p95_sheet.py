"""P95 (8 Nov 2026) · the contact sheet of the outline library: every outline drawn as its relief by viz.py's kind
"relief", on a page styled by design/theme.css alone (inlined, as every Academy page is), in the tone of the first
course it serves, at rest (reduced motion), dark and light; each card named by its id, what it depicts, its credit and
its courses. Shots are written under 8,000 px tall.

    python3 p95_sheet.py <folder>     writes <folder>/sheet-dark.png and <folder>/sheet-light.png
"""
import html, json, pathlib, sys

import viz

R = pathlib.Path(__file__).resolve().parent
LIB = R.parent / 'design' / 'outlines'
TONE = {'greece': 1, 'rome': 5, 'brand-a': 3, 'brand-b': 5, 'ux-ia': 4}
NAME = {'greece': 'Greece', 'rome': 'Rome', 'brand-a': 'Personal brand', 'brand-b': 'Building with AI', 'ux-ia': 'Information architecture'}
# the sheet's own layout: only a grid of cards on the theme's tokens; the drawing and its caption are the pages' rules
CSS = '''body{margin:0;padding:16px;background:var(--bg);color:var(--fg);font-family:var(--sans)}
.sheet{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px;--relief-h:230px}
.card{background:var(--card);border:1px solid var(--line);padding:10px}
.card .topo.relief{margin:0 auto}
h1{font-size:18px;margin:0 0 12px}'''


def page(theme):
    lib = json.loads((LIB / 'outlines.json').read_text())
    cells = []
    for o in lib['outlines']:
        d = json.loads((LIB / f'{o["id"]}.json').read_text())
        rel = viz.render(dict(kind='relief', outline=d, tone=TONE[o['courses'][0]]))
        cap = (f'<b>{html.escape(o["id"])}</b> · {html.escape(o["depicts"])}<br>{html.escape(o["credit"])}<br>'
               f'{html.escape(", ".join(NAME[c] for c in o["courses"]))} · {viz.rel_bytes(rel):,} B')
        cells.append(f'<figure class="card relief-fig">{rel}<figcaption>{cap}</figcaption></figure>')
    css = (R.parent / 'design' / 'theme.css').read_text()
    dt = f' data-theme="{theme}"'
    return (f'<!doctype html><html{dt}><head><meta charset="utf-8"><style>{css}\n{CSS}</style></head><body>'
            f'<h1>Outline library · {len(lib["outlines"])} reliefs · {theme}</h1><div class="sheet">{"".join(cells)}</div></body></html>')


def main():
    from playwright.sync_api import sync_playwright
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        for theme in ('dark', 'light'):
            pg = br.new_page(viewport=dict(width=1400, height=900), reduced_motion='reduce', color_scheme=theme)
            pg.set_content(page(theme))
            pg.wait_for_timeout(200)
            h = pg.evaluate('document.documentElement.scrollHeight')
            assert h < 8000, f'the sheet is {h} px tall'
            pg.screenshot(path=str(out / f'sheet-{theme}.png'), full_page=True)
            print(f'{out / f"sheet-{theme}.png"}: 1400 x {h} px')
            pg.close()
        br.close()


if __name__ == '__main__':
    main()
