#!/bin/bash
# wait until any of the given packet folders has out/DONE that was not there at start (or timeout seconds)
T=${1:-540}; shift
start=$(ls /home/claude/fpb/*/out/DONE 2>/dev/null | sort | tr '\n' ' ')
for i in $(seq 1 $((T/15))); do
  now=$(ls /home/claude/fpb/*/out/DONE 2>/dev/null | sort | tr '\n' ' ')
  [ "$now" != "$start" ] && break
  sleep 15
done
for d in /home/claude/fpb/*/; do c=$(basename $d); printf '%s: %s lines audit, DONE=%s\n' "$c" "$(cat $d/out/audit.md 2>/dev/null | wc -l)" "$( [ -f $d/out/DONE ] && head -c 80 $d/out/DONE | tr '\n' ' ' || echo no)"; done
