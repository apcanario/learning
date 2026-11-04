# P92 · the home before the change

The Academy home as P91 left it (learning f155586, the baseline build), shot whole by `verify.py --shots` at 320, 360,
390 (`phone`), 430, 768 (`tablet`) and 1280 px (`desktop`), dark and light, with reduced motion emulated. `verify.py`
shoots phones and the tablet at device scale 3; these are scaled to device scale 2 (2 image pixels to a CSS pixel); the
desktop shots are at scale 1.
