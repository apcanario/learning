# Packet 1: engine course ids and the baseline guard (carried corrections 3 and 4)
Report: out/s-dec4/01-engine.md
Files you may change: kit/build.py, kit/howbuilt.py, kit/baseline.py, kit/courses.py, courses/*/course.toml, kit/private_terms.py, kit/README.md prose (rehash that one baseline entry only if it is the sole change, as S-DEC1 did), kit/pack.py if a new key needs it. Not kit/verify.py (packet 2).
Test: docs/decoupling.md §5. academy and greece byte-identical after every step.

Work
1. `build.py` `dkey` (Greece's legacy unit storage key) and `howbuilt.py` (Greece and Rome review-note regexes) special-case course ids: move each to a course.toml key whose today's value is the default the engine uses when the key is absent. Output byte-identical.
2. `baseline.py` re-records the manifest for any argument except `--check`, and its edition names are academy's: add a guard (an unknown argument stops with a usage line; nothing is re-recorded by accident). Keep `python3 kit/baseline.py` (no argument) writing the manifest as today.
3. Engine text about this repo's history reaches every edition (the Figure kinds page examples cite Rome modules, 11 mentions; the markdown 'How it was built' page names S-NOAUDIT and the closed Fable stage). Decide whether the build keeps them per edition. Hard limit: academy and greece stay byte-identical; so any change applies only to an edition that holds none of the named courses/history (e.g. marketing-ai, a fieldnotes-style edition). Build marketing-ai (`python3 kit/build.py --edition marketing-ai`) before and after; record the diff. If the cleanest reading is "keep, it is the engine's example text", record that decision and why instead.
4. The history 'How it was built' footer links only the course's provenance file, not kit/provenance.json (M5). Doing it changes academy AND greece output: do NOT do it; record it as a proposed row (text ready to paste into docs/BACKLOG.md Proposed, with its expected differences).
5. `private_terms.py` `PUBLIC` and its `kit/academy` glob are academy's. Make `private_terms.py` accept explicit file arguments if it does not already (the manual form is `python3 kit/private_terms.py $(find kit/editions/<site> -type f)`); keep the no-argument behaviour byte-for-byte.
End: baseline clean; `cd kit && python3 private_terms.py` OK. Do not run the full verify.py (packet 2 owns it).
