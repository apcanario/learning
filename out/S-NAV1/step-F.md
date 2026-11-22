# S-NAV1 · Step F · p95_shots.py on the swell, and the last turn references

Model: Opus 5.5 (claude-opus-5-5), a fresh agent. 22 Nov 2026.

## Verdict

PASS. `kit/p95_shots.py` poses the swell (`topo-swell`) the way `kit/p94_extract.py` (step E) and verify.py's `swellAt`
do. No code reference to the turn or the whole-layer breath remains in kit/. Doc references are listed for the main
chat. No commit, no push, no land.py; `kit/baseline.json` and `kit/verify-hashes.json` untouched.

## Files changed

- `kit/p95_shots.py`: `POSE_JS` no longer reads `--topo-cycle` or poses `topo-turn` on the relief's svg, and no longer
  holds a breath at its top. It reads `--topo-breath` and pauses every `topo-swell` animation on the relief's lines
  (any animated element inside the `.topo.relief` wrapper) at the point p of the sweep (0 at rest, 1 at its top), each
  line's phase (negative delay) honoured: `t = p*bt + d; if t < 0: t = 2*bt - p*bt + d`, as `SWELL_AT_JS` does. The
  docstring describes the swell.
- `out/S-NAV1/step-F.md` (this file).

## Run

- `python3 -c "import p95_shots"` (in kit/): imports; 123 mapped pages, theme key read.
- `python3 kit/p95_shots.py /tmp/snav1f-p95 m11 --widths 390` against the committed academy build (local server,
  vendored fonts; offline): 7 shots (dark and light at rest, five poses). The five pose shots differ from each other
  (md5); pose 1 shows the core rings still and the outer lines out.

## Remaining references (grep of kit/, docs/, skills/ for `topo-turn`, `topo-breathe`, `TOPO_TURN`, `--topo-turn`)

Code in kit/: none live. Every hit records that the turn is gone:
- `kit/p94_extract.py:19`, `kit/verify.py:136`, `kit/verify.py:857`, `kit/build.py:369` (comments: "gone"/"removed").
- `kit/shell.css:39` (= `design/theme.css:39`): comment, "gone".
- Also seen, outside the four terms, history only: `kit/build.py:377`, `:383` (`turned_inside`/`turned_clear` "until
  step D").

History (left as is): `kit/CHANGELOG.md:669`, `:677`; `kit/reviews/p94/check-5.md:49`;
`kit/reviews/p93/check-motion-2.md:31`; `kit/reviews/p93/check-motion-1.md:17`; `docs/BACKLOG.md:1665` (the S-NAV1
row's own text, which names what it removes).

Doc references for the main chat (stale, describe the turn as current):
- `docs/BACKLOG.md:229` and `docs/BACKLOG.md:1683` (P-HK1): the proposed min-height formula uses
  `sin(var(--topo-turn))`; the token is gone (step D: hero min-height is now 370 px, no overscan).
- `design/README.md:62`: token table row `--topo-turn` / `--topo-cycle` (outside the grep scope, found in passing;
  step D listed it with the version history and section 4i row).
- `kit/README.md:70` (build row): "turning and growing", `turned_inside`, `turned_clear` (not one of the four terms;
  step D listed it).
- skills/: none.

## Blockers

None.
