# P93 · the start

The Academy as P92 left it (learning 77a902a, the baseline build of 0cb6dd5; `build.py` and `verify.py` ALL CHECKS
PASSED), shot by `verify.py --shots` with `--page greece --page brand-a --page brand-b --page ux-ia` (and Rome at
320, 360 and 430 px with verify's own page setup and `shoot`, since `--shots` takes the second history course only at
390, 768 and 1280 px): the home (whole), What's new and the five course homes (Greece, Rome, Personal brand
`brand-a`, Building with AI `brand-b`, Information architecture `ux-ia`; the top 2,600 px) at 320, 360, 390
(`phone`), 430, 768 (`tablet`) and 1280 px (`desktop`), dark and light, with reduced motion emulated; and P92's hero
motion sheets at 390 and 1280 px (`*-hero-motion-*`). `verify.py` shoots phones and the tablet at device scale 3;
these are scaled to device scale 2 (2 image pixels to a CSS pixel); the desktop shots are at scale 1.
