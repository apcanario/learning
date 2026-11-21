# P-DEC4 · Harden kit/pack.py (agent output, 21 Nov 2026)

Model: Opus 5.5 (fresh implementer agent). Baseline commit e855c10. Files changed: `kit/pack.py` only (63 insertions, 10 deletions). Nothing committed or pushed. Probe copy: `/tmp/probe-dec4` (left in place, with the dummy SCE1 filing in it).

## Verdict: done

## What changed (kit/pack.py)

1. **Changelog rows by key name.** `[[pack.changelog]]` and `[[pack.audit_log]]` (same shape, date and text) are no longer read through `_value` (tuple of values in key order); new `_rows(c, pk, key)` builds `(r['date'], r['text'])`. A row whose keys are not exactly `date` and `text` stops the build: `<data>: [[pack.changelog]] row <i> needs exactly the keys date and text, not <keys>`. Both keys added to `_SPECIAL`. Reading: the row names changelog only; audit_log is the same two-key table read the same way, so it is covered too (recorded as a choice).
2. **Insert: clear message for missing `name` or `date`.** At the top of `insert()`, before anything is read or written: `hub_changelog` without a non-empty string `date` -> `records.json: hub_changelog needs `date` ("YYYY-MM-DD hh:mm"), the new changelog row's date`; a `date` that does not start with YYYY-MM-DD -> its own message; `reading` without a non-empty `name` -> `records.json: reading needs `name` (...)`; `reading` without `intro` -> its own message. Before, thin.py printed `insert failed, every file restored: 'name'` / `'date'` (bare KeyError).
3. **briefs.md: duplicate or unmatched `## <code>` stops.** `briefs()` stops on a section name given twice (before: the later one silently won) and on any `## ` line that is not a heading followed by a blank line (before: silently read into the brief above it). `load()` stops on a section that is neither `Preamble` nor a unit code of `[[pack.courses.units]]` (before: ignored). A unit with no section already stopped.
4. **`[pack.status]` code with no unit stops.** `load()` stops on a code that is no unit of `[[pack.courses.units]]`, and on a unit code with no file in the vault (before: both silently ignored, since STATUS is derived only for filed units). Reading of "no unit": both cases, with distinct messages; recorded as a choice. Real data: brand-ai's six overrides are all filed units, so nothing in the repo trips it.
5. Docstring updated (the `[pack.status]`, changelog/audit_log and briefs.md paragraphs). `load()`'s returned attributes are equal in value to the old ones for all 6 markdown courses (checked by script against `git show HEAD:kit/pack.py`); only the attribute insertion order of the namespace differs (CHANGELOG/AUDIT_LOG set later), and nothing in kit/ iterates `vars()` of it.

## Probes (in /tmp/probe-dec4; each input restored with `git checkout` after)

Loader probe = `python3 /tmp/p-dec4-old/load.py <course>` (imports kit/courses and kit/pack, calls `pack.load(c)`: the same call build.py makes).

- **(a) changelog keys in a different order.** Every `[[pack.changelog]]` and `[[pack.audit_log]]` row of `courses/personal-brand/course.toml` rewritten text-before-date (27 rows). New: `loaded personal-brand CHANGELOG[0][0]= 2026-11-17 12:00 VERSION= v16.1 · 17 Nov 2026 AUDIT_LOG[0][0]= 2026-11-14`; the whole loaded object equals the unswapped one (`swapped-key load equals original load: True`). Old pack.py on the same file: `SystemExit a pack needs [pack] version when its top changelog row does not start "v<n>. "` (it took the text as the date).
- **(b) insert missing `name`.** `python3 kit/thin.py insert /tmp/p-dec4-old/rec/noname.json` (the dummy SCE1 record without `reading.name`) -> `insert failed, every file restored: records.json: reading needs `name` ("<code> · <title>" unless the unit's reading page is named otherwise)`, exit 1. Old: `insert failed, every file restored: 'name'`.
- **(c) insert missing `date`.** `python3 kit/thin.py insert /tmp/p-dec4-old/rec/nodate.json` -> `insert failed, every file restored: records.json: hub_changelog needs `date` ("YYYY-MM-DD hh:mm"), the new changelog row's date`, exit 1. Old: `insert failed, every file restored: 'date'`.
- **(d) duplicate `## <code>`.** A second `## IA1` section appended to `courses/ux/briefs.md` -> `courses/ux/briefs.md: section ## IA1 given more than once`, exit 1. Old: loaded silently (exit 0, the later IA1 brief winning).
- **(e) unmatched `## <code>`.** (e1) `## IA99` appended -> `courses/ux/course.toml: briefs.md has ## IA99, which is no unit of [[pack.courses.units]]`, exit 1. (e2) `## IA2` with no blank line after it -> `courses/ux/briefs.md: '## IA2' is not a section heading followed by a blank line (a brief holds no line that starts with "## "; kit/pack.py)`, exit 1.
- **(f) `[pack.status]` code with no unit.** (f1) `SP99 = 'written 1 Nov'` under `[pack.status]` of sport-psychology -> `courses/sport-psychology/course.toml: [pack.status] SP99 is no unit of [[pack.courses.units]]`, exit 1; and `cd kit && python3 build.py` stops with the same line, exit 1. (f2) `"DD-SP3" = 'written 1 Nov'` (a unit, not filed) -> `courses/sport-psychology/course.toml: [pack.status] DD-SP3 has no file in courses/sport-psychology (STATUS is only for filed units)`, exit 1.

## Dry-run filing (thin.py insert of a dummy unit, probe only)

Dummy `courses/supply-chain-execution/SCE1-the-map-the-words-and-the-evidence.md` (front matter code, title, course, model, written 2026-11-21, search on; one line of body). Record `/tmp/p-dec4-old/rec/ok.json`: reading (id read-sce1, course SCE, title, covers, name, intro), status "written 21 Nov", next_unit SCE2, version "v2 · 21 Nov 2026", hub_changelog "v2. SCE1 filed (dummy probe, P-DEC4).", date "2026-11-21 12:00", index_edits (SCE1 row to written, "1 of 20 written", a staleness row). The first two attempts failed in index_check only for missing index edits (status cell, then staleness row) and restored every file, as designed. Third attempt: `python3 kit/thin.py insert /tmp/p-dec4-old/rec/ok.json` -> `inserted into: courses/supply-chain-execution/SCE1-the-map-the-words-and-the-evidence.md, courses/supply-chain-execution/course.toml, docs/courses-index.md`, exit 0. Reloaded: `NEXT_UNIT SCE2 | VERSION v2 · 21 Nov 2026 | STATUS {'SCE1': 'written 21 Nov'} | READINGS ['read-sce1'] | CHANGELOG[0] ('2026-11-21 12:00', 'v2. SCE1 filed (dummy probe, P-DEC4).')`.

## Baseline (main tree)

- Before: `python3 kit/baseline.py --check` -> academy 457 files 0 differ, greece 82 files 0 differ, `baseline: clean` (2 m 3 s). Caveat: my first edits to pack.py landed while this run was building, so it is a mixed before/after run; the clean state at e855c10 is the main chat's stated baseline.
- After (final pack.py, sha256 048261a8e670e02d6085d5407cc9135d52a1ead8a0dc4a2024abbeaca570e19a, unchanged across the run): academy 457 files 0 differ, greece 82 files 0 differ, `baseline: clean` (2 m 4 s).
- verify.py not run (main chat runs `--full` once at the end).

## Open

- Docs that describe pack.py's stops: `docs/decoupling.md` §6 (S-DEC2 notes) and `skills/file-unit` / `new-course` do not list the new stops; the docstring does. Left to the main chat's close (not in my file list).
- `insert()` still raises a bare KeyError if a unit's front matter lacks `written` when `status` is given (`v[code][1]['written']`); outside the row's text, not changed.

## Diff

```diff
diff --git a/kit/pack.py b/kit/pack.py
index 85a4a2b..286944a 100644
--- a/kit/pack.py
+++ b/kit/pack.py
@@ -36,7 +36,8 @@ The `[pack]` table (every key optional unless marked):
   version = "v1 · 1 Jan 2027"               only where the top changelog row does not start "v<n>. " (below)
   order = [["B1", "Opus 5.5", "off"], ...]  ORDER: (code, model, search) rows, writing order          (required)
   done_rows = [[...6 cells...], ...]        DONE_ROWS: earlier material, rows of six cells
-  [pack.status]                             STATUS overrides, only where the derived string is not the typed one
+  [pack.status]                             STATUS overrides, only where the derived string is not the typed one; a
+                                            code that is no unit, or has no file in the vault, stops the build
   A2 = "rewritten 28 Oct"
   [[pack.courses]]                          COURSES, in order: key, name, color, slug, goal, tile, intro, outcomes (required)
   key = "A"  ...
@@ -44,14 +45,17 @@ The `[pack]` table (every key optional unless marked):
   code = "A1"  title = "..."  ...           takes, gives where the course has Aim lines (AIMS); the brief is briefs.md's
   [[pack.readings]]                         READINGS that are not a unit's: id, md (relative to notes/), course, title,
   id = "read-..."  md = "..."  ...          covers = [], name, intro
-  [[pack.changelog]]                        CHANGELOG, newest first: date, text ({A}, {B} = course names)
-  [[pack.audit_log]]                        AUDIT_LOG: date, text
+  [[pack.changelog]]                        CHANGELOG, newest first: date, text ({A}, {B} = course names); read by
+                                            key name, so (date, text) in either order; any other key stops the build
+  [[pack.audit_log]]                        AUDIT_LOG: date, text (read the same way)
   [[pack.template_blocks]]                  any other array of tables: a list of tuples of its values, in key order
                                             (TEMPLATE_BLOCKS: heading, html)
 
 briefs.md: a `## Preamble` section (PRE; `{GOAL}` is filled with the course goal) and one `## <code>` section per unit,
 each section's text between the blank line after its heading and the next heading, its final newlines dropped. Text above
-the first `## ` is a note for the reader and is not read. A brief holds no line that starts with `## `.
+the first `## ` is a note for the reader and is not read. A brief holds no line that starts with `## `. The build stops
+(P-DEC4) on a `## ` line not followed by a blank line, a section given twice, a unit with no section and a section that
+is neither `Preamble` nor a unit's code.
 
 pages/<name>.md: the block NAME (name upper-cased, '-' as '_'), the file's text less its final newline: FRAME (frame.md),
 BUILD_BODY, BUILD_PICK, BRIEFS_LEDE, LEARNING_NOTE, ORDER_NOTES, TEMPLATE_NOTE. The blocks are theme-class HTML, which
@@ -85,7 +89,18 @@ DEFAULTS = dict(
     LEARNING_NOTE='', BUILD_PICK='', FRAME='',
 )
 # the [pack] keys that are not a plain attribute
-_SPECIAL = {'source', 'version', 'order', 'done_rows', 'status', 'courses', 'readings'}
+_SPECIAL = {'source', 'version', 'order', 'done_rows', 'status', 'courses', 'readings', 'changelog', 'audit_log'}
+
+
+def _rows(c, pk, key):
+    """[[pack.changelog]] or [[pack.audit_log]] as (date, text) tuples, read by key name, not key order (P-DEC4)."""
+    out = []
+    for i, r in enumerate(pk.get(key, []), 1):
+        if not isinstance(r, dict) or set(r) != {'date', 'text'}:
+            got = ', '.join(r) if isinstance(r, dict) else type(r).__name__
+            raise SystemExit(f'{c["data"]}: [[pack.{key}]] row {i} needs exactly the keys date and text, not {got}')
+        out.append((r['date'], r['text']))
+    return out
 
 
 def _path(c):
@@ -135,9 +150,21 @@ def vault(c):
 
 
 def briefs(path):
-    """briefs.md: {section name: text}."""
-    parts = re.split(r'(?m)^## (.+)\n\n', path.read_text(encoding='utf-8'))
-    return {parts[i].strip(): parts[i + 1].rstrip('\n') for i in range(1, len(parts), 2)}
+    """briefs.md: {section name: text}. Stops on a `## ` line that is not a section heading followed by a blank line
+    (it would be read into the brief above it) and on a section name given twice (P-DEC4)."""
+    t = path.read_text(encoding='utf-8')
+    where = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
+    parts = re.split(r'(?m)^## (.+)\n\n', t)
+    names = [parts[i].strip() for i in range(1, len(parts), 2)]
+    heads = re.findall(r'(?m)^## .*$', t)
+    if len(heads) != len(names):
+        bad = [h for h in heads if not re.search(rf'(?m)^{re.escape(h)}\n\n', t)]
+        raise SystemExit(f'{where}: {", ".join(repr(h) for h in bad)} is not a section heading followed by a blank line '
+                         '(a brief holds no line that starts with "## "; kit/pack.py)')
+    dup = sorted({n for n in names if names.count(n) > 1})
+    if dup:
+        raise SystemExit(f'{where}: section {", ".join("## " + n for n in dup)} given more than once')
+    return {n: parts[2 * i + 2].rstrip('\n') for i, n in enumerate(names)}
 
 
 def status_text(written):
@@ -195,14 +222,24 @@ def load(c):
             if 'aim' in u:
                 d.AIMS[u['code']] = (u['aim'], u['takes'], u['gives'])
         d.COURSES.append(dict({k: v for k, v in sc.items() if k != 'units'}, units=units))
+    codes = [u[0] for sc in d.COURSES for u in sc['units']]
+    extra = [n for n in bf if n != 'Preamble' and n not in codes]
+    if extra:
+        raise SystemExit(f'{c["data"]}: briefs.md has {", ".join("## " + n for n in extra)}, which is no unit of '
+                         '[[pack.courses.units]]')
     d.ORDER = [tuple(o) for o in pk['order']]
     d.DONE_ROWS = [tuple(r) for r in pk.get('done_rows', [])]
-    d.CHANGELOG = getattr(d, 'CHANGELOG', [])
-    d.AUDIT_LOG = getattr(d, 'AUDIT_LOG', [])
+    d.CHANGELOG = _rows(c, pk, 'changelog')
+    d.AUDIT_LOG = _rows(c, pk, 'audit_log')
     d.VERSION = version(d.CHANGELOG, pk.get('version'))
     # derived from the vault: STATUS, NEXT_UNIT, the units' READINGS
     v = vault(c)
     over = pk.get('status', {})
+    for code in over:
+        if code not in codes:
+            raise SystemExit(f'{c["data"]}: [pack.status] {code} is no unit of [[pack.courses.units]]')
+        if code not in v:
+            raise SystemExit(f'{c["data"]}: [pack.status] {code} has no file in {c["vault"]} (STATUS is only for filed units)')
     d.STATUS = {code: over.get(code) or status_text(fm['written']) for code, (f, fm) in v.items()}
     d.NEXT_UNIT = next((o[0] for o in d.ORDER if o[0] not in v), '—')
     d.READINGS = [dict(r) for r in pk.get('readings', [])]
@@ -233,6 +270,22 @@ def insert(c, rec, get):
     out = {}
     path = ROOT / c['data']
     code = rec['code']
+    # P-DEC4: a missing key says which, before anything is read or written (a bare KeyError printed only 'date')
+    if 'hub_changelog' in rec:
+        dt = rec.get('date')
+        if not isinstance(dt, str) or not dt.strip():
+            raise ValueError('records.json: hub_changelog needs `date` ("YYYY-MM-DD hh:mm"), the new changelog row\'s date')
+        try:
+            datetime.date.fromisoformat(dt[:10])
+        except ValueError:
+            raise ValueError(f'records.json: `date` {dt!r} does not start with a date YYYY-MM-DD')
+    if 'reading' in rec:
+        nm = rec['reading'].get('name') if isinstance(rec['reading'], dict) else None
+        if not isinstance(nm, str) or not nm.strip():
+            raise ValueError('records.json: reading needs `name` ("<code> · <title>" unless the unit\'s reading page is '
+                             'named otherwise)')
+        if not isinstance(rec['reading'].get('intro'), str):
+            raise ValueError('records.json: reading needs `intro` (one line)')
     v = vault(c)
     if ('reading' in rec or 'status' in rec) and code not in v:
         raise ValueError(f'{code} has no file in {c["vault"]}: put the unit, with its front matter, in the vault first')
```
