"""P95 (8 Nov 2026) · a fresh checker's transcript, checked by script (the P31 agent rules): the models its replies
name, the tools it called and how often, every path it read (file_path, path and any absolute path in a Glob or Grep
pattern), whether each is inside its folder (the folder matched with and without its trailing slash), any file under
/root/.claude/ (allowed only if it is one of its own saved results, named in a tool result of the same transcript); and
its report, taken verbatim from its SubagentHandback tool call's message (or, if it made none, its last reply's text).

    python3 p95_transcripts.py <transcript.jsonl> <its folder> <report out .md>
"""
import json, pathlib, re, sys

ALLOWED = {'Read', 'Glob', 'Grep', 'SubagentHandback'}


def main():
    tr, folder, out = pathlib.Path(sys.argv[1]), sys.argv[2].rstrip('/'), pathlib.Path(sys.argv[3])
    models, tools, paths, report, last_text, saved = set(), {}, [], None, None, set()
    for line in tr.read_text().splitlines():
        d = json.loads(line)
        m = d.get('message') or {}
        if not isinstance(m, dict):
            continue
        if m.get('model'):
            models.add(m['model'])
        c = m.get('content')
        if not isinstance(c, list):
            continue
        for x in c:
            if x.get('type') == 'tool_result':
                body = json.dumps(x.get('content'))
                saved |= set(re.findall(r'/root/\.claude/[^\s"\\]+', body))
            if x.get('type') == 'text' and m.get('role') == 'assistant':
                last_text = x['text']
            if x.get('type') != 'tool_use':
                continue
            n = x['name']
            tools[n] = tools.get(n, 0) + 1
            inp = x.get('input') or {}
            if n == 'SubagentHandback':
                report = inp.get('message') or inp.get('report') or json.dumps(inp)
                continue
            for k in ('file_path', 'path'):
                if inp.get(k):
                    paths.append(inp[k])
            for k in ('pattern', 'glob'):
                v = inp.get(k) or ''
                if v.startswith('/'):
                    paths.append(v)
    inside = lambda p: p == folder or p.startswith(folder + '/')
    outside = [p for p in paths if not inside(p) and not (p.startswith('/root/.claude/') and p in saved)]
    bad_tools = sorted(set(tools) - ALLOWED)
    text = report if report is not None else last_text
    out.write_text(text.rstrip() + '\n')
    print(f'{tr.name}: models {sorted(models)}; tools {dict(sorted(tools.items()))}; {len(paths)} paths, '
          f'{len(paths) - len(outside)} inside {folder} (with or without its trailing slash), {len(outside)} outside {outside[:5]}; '
          f'tools not allowed: {bad_tools or "none"}; report from {"its SubagentHandback call" if report is not None else "its last reply"}, '
          f'{len(text):,} characters, first line "{text.strip().splitlines()[0]}"')


if __name__ == '__main__':
    main()
