"""P-DEC15: What's new's days per built site, read from the site's new.html hero layer (each rise's data-label and
data-words, the tall and the wide layout), with the largest day's levels at the fixed scale (NEW_INTERVAL = 11000)
and at the per-edition scale this row decides (new_interval: 11000 for a largest day of 110,000 words or more, else
largest // 10, at least 1).

  python3 out/DEC-C/p_dec15_days.py <site-dir> [<site-dir> ...]
"""
import pathlib, re, sys

FIXED = 11000


def new_interval(top):
    return FIXED if top >= 10 * FIXED else max(1, top // 10)


for d in sys.argv[1:]:
    s = (pathlib.Path(d) / 'new.html').read_text(encoding='utf-8')
    rises = re.findall(r'data-label="([^"]*)"[^>]*?data-words="(\d+)"', s)
    lays = len(re.findall(r'data-layout=|class="[^"]*topo-lay', s))
    days = {}
    for l, w in rises:
        days[l] = int(w)
    top = max(days.values()) if days else 0
    iv = new_interval(top)
    print(f'{d}: {len(rises)} rises in the layers, {len(days)} days; largest {top:,} words; '
          f'fixed scale {top // FIXED} levels; per-edition interval {iv:,} -> {top // iv if iv else 0} levels; '
          f'{"unchanged (interval 11000)" if iv == FIXED else "CHANGES"}')
    for l, w in days.items():
        print(f'    {l}: {w:,} words, {w // FIXED} levels fixed, {w // iv} levels per-edition')
