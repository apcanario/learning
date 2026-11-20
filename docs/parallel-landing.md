# Parallel landing

Several chats run at once, each in its own clone, and all land on `main` of the same remote. `kit/land.py` is the one way a chat lands its commits (method.md §10). Never a bare `git push`, never `--force`.

## The two commands

1. **After cloning:** `python3 kit/land.py start <row>`. It records origin/main as the chat's start commit in `out/<row>/land-start.json`. Every check below measures "what others landed" from this commit. Without it, land falls back to the first origin/main this clone fetched, and says so.
2. **To land, in place of the push:** `python3 kit/land.py land <row> --expected <file>`. The working tree must be committed. `<file>` lists the row's own expected build differences, one path per line, in the form `baseline.py --check` prints them (a whole check line can be pasted). It can also hold `drop: <path> :: <line>` for an upstream line the row removed on purpose.

`python3 kit/land.py status [<row>]` shows who holds the lock, the commits landed since the start, and whether the clone is behind. `python3 kit/land.py unlock <row>` removes a lock that names `<row>`, for use after a killed landing.

## What land does

1. **Refuses** if a file is uncommitted, a rebase is in progress, or a tracked file holds conflict markers at the start of a line.
2. **Takes the lock.** The lock is `docs/landing.lock` (row, UTC time, host, a token), committed alone on top of origin/main and pushed as a plain fast-forward. The first push to succeed holds it. If another chat holds it, land polls every 30 s for up to 40 min, then exits 3. A lock older than 90 min is stale: land takes it over and records that in its report. The lock is released in a `finally`, on success, on a stop and on Ctrl-C or SIGTERM. A SIGKILL cannot release it; the next chat treats it as stale after 90 min, or the chat that was killed runs `unlock`. A rerun of the same row in the same clone recognises its own lock.
3. **Rebases** on origin/main. When chat B lands after chat A has already updated the logs and records, B keeps both A's changes and its own. The script resolves only these conflicts:
   - **Add-only union** for `docs/*.md` (the CHANGELOG, the site log, the courses index and the other docs). It applies only when, relative to the merge base, neither side deleted or changed a line and both only inserted. Both insertions are kept, ours after theirs. `docs/CHANGELOG.md` is the exception, being newest first: ours goes on top. A non-blank line both sides inserted is kept once. Afterwards, every table row must keep its table's column count.
   - **`docs/BACKLOG.md` by record.** Each table row, including a multi-line saved prompt, is one record keyed by its first cell, the row id. One side's added, changed or removed record is kept when the other side did not touch it. Three cases go further:
     - The "Next up:" line rewritten on both sides: upstream's line is kept. Ours goes to `out/<row>/land-notes.md` for a human to reconcile, and one line is printed. Land does not stop.
     - A record removed by one side (the row closed) and changed by the other only in its prompt cell: the removal stands, and the changed record goes to land-notes.
     - A record whose prompt cell changed on both sides (each re-saved it): it is regenerated from the merged tree (below), and ours goes to land-notes.
     A record changed in other ways on both sides stops land, and so does prose changed on both sides inside a table region.
   - **Literals merged as data** in `catalog.toml` (every `key = [` array, `planned` included) and in `kit/next_prompt.py` (module constants such as `QUEUE` and `HOLDS`). The text outside the literals merges by add-only union in the TOML; in the Python file it may not change on both sides. A list or array becomes (base ∩ ours ∩ theirs) ∪ ours-added ∪ theirs-added, in theirs' order with ours' additions after theirs. So two chats that remove different entries both see their entry removed. A dict merges key by key, and a key changed on both sides stops land. The merged file must parse (`tomllib`; `compile` and `ast` for Python).
   - **`kit/baseline.json`** by a three-way JSON merge, key by key. The same key changed to different hashes on both sides stops land, and both values are printed.
   - **Build output** (`kit/academy/`, `kit/README.md`, `kit/bibliography/`, `courses/<id>/bibliography/unit-*.md`) and `kit/verify-hashes.json`: upstream's copy is taken, and the build regenerates the file in step 6. A landing with `--no-build` stops instead.
   - **Any other conflicted file** stops, including other code and a function body in `kit/next_prompt.py`. The rebase is aborted, the branch is restored and the lock is released. Land prints both sides and exits 2.

   **After any automatic merge, derived records are refreshed.** `kit/index_check.py` runs in step 5. Then the saved prompts are checked: for each row that `kit/next_prompt.py --list` knows and that has a record in `docs/BACKLOG.md`, land compares the cell with what `--row <id>` prints on the merged tree. A differing cell is re-saved with `--save` only if it was exactly the generated prompt on upstream's tree, so a prompt edited by hand is never overwritten. Such a cell is reported and left for a human. The row named in the lock (our own) is never touched. Land has no way to know which rows other chats are working now (see the last section).
4. **Runs the preservation check** (below).
5. **Runs the sanity checks.** No conflict markers. `kit/baseline.json` and every JSON or TOML file either side touched must parse. `kit/index_check.py` must pass.
6. **Runs the build check** when our commits change anything the build reads, or when build output was regenerated. Only `docs/BACKLOG.md`, `docs/CHANGELOG.md`, `kit/CHANGELOG.md`, `kit/baseline.json`, `kit/verify-hashes.json` and `out/` are exempt. The check is `python3 kit/baseline.py --check`, which rebuilds both editions. Every differing file must be listed in `--expected` or have changed in upstream's own `baseline.json` edits since the start. If all are declared, the baseline is re-recorded (commit `land <row>: baseline re-recorded for expected differences`) and the check must then print clean. Regenerated output is committed.
7. **Runs `python3 kit/verify.py`** (scoped), which must end with ALL CHECKS PASSED. Its record is committed.
8. **Pushes HEAD to main**, plainly. A rejected push means someone pushed without the lock. Land fetches and goes back to step 3 with the lock still held, up to 6 attempts.
9. **Releases the lock**, fast-forwards the local branch and prints the landing report. The report gives the start, the upstream commits absorbed, the lines preserved (and the upstream lines an automatic merge rewrote on purpose), the files auto-merged and how, the notes left for a human, the saved prompts refreshed or left, the baseline and verify results, and the pushed sha. It is also appended to `out/<row>/landing-report.md`. That file and `out/<row>/land-notes.md` are written after the run; commit them with the next landing. The lock token lives in `.git/land/`, never in a tracked file.

A run takes about 3 minutes for the build check and 5 more if the baseline is re-recorded, plus verify. `--no-build`, `--no-verify` and the timing flags exist for the test suite only. They need `LAND_TEST=1` and are refused with `LAND_REAL=1`.

## When land stops (exit 2), and what the chat does

In every case the branch is back where it was before land ran, and the lock is released.

| Stop | What the chat does |
|---|---|
| uncommitted changes, a rebase in progress, conflict markers | commit, finish or abort the rebase, remove the markers; land again |
| rebase conflict the script may not resolve | make the two changes agree by hand in the clone, keeping upstream's lines: `git rebase origin/main`, resolve, continue; land again (the preservation check then checks the hand resolution) |
| the same baseline key changed on both sides | rebase by hand and take upstream's hash; land again: the build check rebuilds, finds the file different, accepts it as upstream-declared or `--expected`, and re-records it |
| files we deleted were changed upstream | restore the file from origin/main, or agree the deletion with the row that changed it; land again |
| PRESERVATION CHECK FAILED | the listed upstream lines are missing from HEAD: restore them. If the row removed one on purpose, add `drop: <path> :: <line>` to `--expected` and say so in the changelog row |
| a JSON or TOML file does not parse, index_check fails | fix it on the combined tree, commit, land again |
| output changed by the combination, not declared by anyone | if these are the row's own expected differences, add them to `--expected`; otherwise find which change produced them before landing |
| verify.py did not pass | fix what it names, commit, land again |
| 6 pushes rejected | someone is pushing without the lock: find out who |

Exit 3 means the lock wait timed out. Run `status`; if the holder is dead and the lock is not yet stale, wait or ask Pedro.

## What the preservation check proves, and what it does not

It takes every line that upstream commits added between the start commit and origin/main, net. Blank lines, whitespace-only lines and lines shorter than 12 characters are ignored. Each line must still be in the same file in the rebased HEAD, as many times as upstream left it. Every file upstream added or renamed must still exist. A file we deleted that upstream changed is a failure, checked before the rebase and after it. Build output and `kit/baseline.json` are left to the build check, which rebuilds them; `baseline.json`'s keys that upstream changed are checked key by key until this landing re-records the baseline.

Upstream lines that an automatic resolution replaced on purpose count as preserved and are listed in the report. This covers a literal re-rendered with both sides' entries (`QUEUE = (...)`), an array entry removed by our side, and a prompt regenerated from the merged tree. Upstream's "Next up" line is simply kept. A union keeps every upstream line, so nothing there needs excusing.

A missing line that already existed at our start is listed as "changed by us, review": our own work may have removed that copy. It does not stop the landing. A missing line that did not exist at our start cannot have been removed by work done from that start. That is the signature of a bad merge, so it is a hard failure unless declared with `drop:`. This is stricter than "removed by one of our commits", deliberately: a hand-resolved rebase turns upstream's lines into our commit's deletions, and the check must still catch it (test T5).

**It proves:** no upstream line or file was silently lost by the rebase, by an automatic resolution or by a hand resolution; with the build check, that the combined tree builds and changes no output nobody declared; with verify, that the combined site passes.

**It does not prove:** that two changes agree in meaning. A unit and a backlog row can each be intact and still contradict each other. It does not see a line moved to another file, a line changed in place (the old text counts as removed, so a row's own edit of an upstream line needs `drop:`), lines under 12 characters, or anything in an untracked file. It also says nothing about pushes made without land. Its automatic resolutions are only as right as their rules: "ours after theirs" can put two rows in an order nobody chose, and a re-rendered literal follows theirs' layout. It cannot tell which rows other chats are working at that moment, because nothing records that on main (`start` writes only to the clone). A prompt cell that another live chat will close may therefore still be re-saved, though only when it was purely generated, and the closing chat's removal then wins by the rule above.
