"""P-DEC5: write a brand's metrics table (viz.set_metrics) from vendored woff2 subsets, or print a mono face's advance.

  python3 out/P-DEC5/font_metrics.py table <out.json> <face name> <subset.woff2>...   advances per 1000 em of viz._CH,
                                                                                      and the face's ascent and descent
  python3 out/P-DEC5/font_metrics.py mono <subset.woff2>                              the advance in em
  python3 out/P-DEC5/font_metrics.py proof                                            DM Sans and Space Mono vs viz's literals

Needs fontTools and brotli (woff2); neither is needed by the build. For each character the first subset whose cmap
holds it gives round(advance * 1000 / unitsPerEm); a character no subset holds is 0 (_tw counts it at 900).
"""
import json, pathlib, sys
sys.path.insert(0, '/tmp/pdec5/pylib')
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'kit'))
from fontTools.ttLib import TTFont
import viz


def table(files):
    fonts = [TTFont(f) for f in files]
    out = []
    for ch in viz._CH:
        v = 0
        for ft in fonts:
            cm = ft.getBestCmap()
            if ord(ch) in cm:
                v = round(ft['hmtx'][cm[ord(ch)]][0] * 1000 / ft['head'].unitsPerEm)
                break
        out.append(v)
    return out


def mono(f):
    ft = TTFont(f); cm = ft.getBestCmap()
    ws = {ft['hmtx'][cm[c]][0] for c in cm if 32 <= c < 127}
    assert len(ws) == 1, f'{f}: not monospaced over ASCII: {sorted(ws)}'
    return ws.pop() / ft['head'].unitsPerEm


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'table':
        out, face, files = sys.argv[2], sys.argv[3], sys.argv[4:]
        rel = [str(pathlib.Path(f).resolve().relative_to(ROOT)) for f in files]
        ft = TTFont(files[0]); u = ft['head'].unitsPerEm   # the line box Chromium uses: hhea (USE_TYPO_METRICS faces agree)
        box = {'ascent': round(ft['hhea'].ascent * 1000 / u), 'descent': round(-ft['hhea'].descent * 1000 / u)}
        pathlib.Path(out).write_text(json.dumps({'face': face, 'from': rel, 'chars': viz._CH, 'adv': table(files), **box},
                                                ensure_ascii=False) + '\n')
    elif cmd == 'mono':
        print(mono(sys.argv[2]))
    elif cmd == 'proof':
        F = ROOT / 'kit' / 'fonts'
        for w, ref in (('400', viz._SANS), ('600', viz._SANSB)):
            got = table([F / f'dm-sans-latin-{w}-normal.woff2', F / f'dm-sans-latin-ext-{w}-normal.woff2'])
            d = [(viz._CH[i], r, g) for i, (r, g) in enumerate(zip(ref, got)) if r != g]
            print(f'DM Sans {w}: {len(ref)} literal values, {len(got)} regenerated, {len(d)} differ' + (f': {d}' if d else ''))
        m = mono(F / 'space-mono-latin-400-normal.woff2')
        print(f'Space Mono 400: regenerated {m!r} em, literal 0.612: {"equal" if m == 0.612 else "DIFFER"}')
