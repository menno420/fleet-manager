#!/usr/bin/env python3
"""Regression suite for .claude/hooks/change_guard.py — run it before touching the hook.

**Why this file exists.** Two Codex rounds on fm #831 found 15 findings, 13 of
them real defects in the hook, every one shipped after testing the author had
called two-directional. That testing was real and covered each defect and its
absence — it did not cover the *traffic the hook sits in*: fenced code,
single-row table edits, MultiEdit payloads, wrapped prose, Markdown bullets whose
leading `-` makes `git grep` exit 129 and fail silent.

So the cases below are deliberately the boring ones. A hook on every file change
is judged by what it does to ordinary work, not by whether it catches the defect
it was written for — a check that cries wolf on a table-cell correction is
ignored inside one session.

    python3 tools/test_change_guard.py      # exit 0 = all pass
"""

import json, os, subprocess, sys
from pathlib import Path

REPO = str(Path(__file__).resolve().parent.parent)
H = ".claude/hooks/change_guard.py"

def run(ev):
    out = subprocess.run(["python3", H], input=json.dumps(ev),
                         capture_output=True, text=True, cwd=REPO)
    return out.stdout.strip()

def pre(fp, **kw):  return {"hook_event_name":"PreToolUse","tool_name":kw.pop("tool","Write"),"tool_input":dict(file_path=fp, **kw)}
def post(fp, **kw): return {"hook_event_name":"PostToolUse","tool_name":kw.pop("tool","Edit"),"tool_input":dict(file_path=fp, **kw)}

T = []
def check(name, got, want):
    ok = (bool(got) == want)
    T.append(ok)
    print(("  PASS " if ok else "  FAIL ") + name + ("" if ok else f"   [{'fired' if got else 'silent'}, wanted {'fire' if want else 'silence'}]"))

BT = chr(96)
print("== F1 malformed delimiter ==")
check("'| | |' must NOT count as a delimiter", run(pre("x.md", content="| a | b |\n| | |\n| 1 | 2 |\n")), True)
check("real delimiter is accepted", run(pre("x.md", content="| a | b |\n|---|---|\n| 1 | 2 |\n")), False)
check("colon-aligned delimiter accepted", run(pre("x.md", content="| a | b |\n|:--|--:|\n| 1 | 2 |\n")), False)

print("== F3 fence identity ==")
check("``` inside ```` stays fenced", run(pre("x.md", content=BT*4+"\n"+BT*3+"\n| not | table |\n"+BT*4+"\n")), False)
check("tilde inside backtick fence stays fenced", run(pre("x.md", content=BT*3+"\n~~~\n| not | table |\n"+BT*3+"\n")), False)
check("real orphan outside fences still caught", run(pre("x.md", content="prose\n\n| 3 | 4 |\n")), True)

print("== F2 dash-prefixed fragment ==")
# Built at runtime, never spelled out: once this suite is committed, any literal
# fixture in it becomes a real survivor in the repo and the "expect silence" case
# starts failing — measured the first time this file was added to the tree.
bullet = "- " + " ".join(["zzq" + w for w in
         "alpha bravo charlie delta echo foxtrot golf hotel india".split()])
check("dash bullet does not crash grep into silence",
      run(post("docs/nonexistent.md", old_string=bullet, new_string="z")), False)
open(os.path.join(REPO, "_probe_dash.md"),"w").write(bullet+"\n")
check("dash bullet FINDS a real survivor",
      run(post("docs/other.md", old_string=bullet, new_string="z")), True)
os.remove(os.path.join(REPO, "_probe_dash.md"))

print("== F5 cap after filtering ==")
keep = "This opening line is preserved verbatim across the edit and is long enough to shingle."
fix  = "The corrected later line carries the claim that must still be hunted for elsewhere ok."
open(os.path.join(REPO, "_probe_later.md"),"w").write(fix+"\n")
check("later-line fix still searched when earlier lines are preserved",
      run(post("docs/other.md", old_string=keep+"\n"+fix, new_string=keep+"\nsomething else entirely now")), True)
os.remove(os.path.join(REPO, "_probe_later.md"))

print("== F6 telemetry ledger is not a survivor ==")
# `check --strict` appends its FINDING MESSAGES to .substrate/guard-fires.jsonl,
# and a finding message quotes the offending text — so after any gate-driven fix
# the old wording still sits in the ledger. Without the pathspec exclusion, check
# C reports that as an un-propagated survivor: a guaranteed false positive on
# every correction the gate itself prompted (fired twice in five minutes on
# fm #833). Built at runtime for the same reason as F2.
# Two sources, deliberately: a first version of this fix excluded only the
# telemetry ledger and left .substrate/backup/ — 16 whole banked dists — still
# searchable, so any edit to text that ever shipped in the kit matched every
# bank at once. Measured on fm #833: 20 .substrate hits with the narrow
# exclusion, 0 with the directory excluded. Test the CLASS, not the instance.
BACKUP = os.path.join(REPO, ".substrate", "backup", "_probe_bank.py")
LEDGER = os.path.join(REPO, ".substrate", "guard-fires.jsonl")
# TEN words, deliberately: check C shingles at 9, so an 8-word fixture is silent
# because it never produces a fragment — which made the first version of the
# exclusion case pass for the wrong reason until the positive control caught it.
telem = "zzt" + " zzt".join(
    "quebec romeo sierra tango uniform victor whiskey xray yankee zulu".split())
_orig = open(LEDGER, "rb").read() if os.path.exists(LEDGER) else None
try:
    with open(LEDGER, "a") as fh:
        fh.write('{"probe": "' + telem + '"}\n')
    check("fragment surviving ONLY in the telemetry ledger is silent",
          run(post("docs/other.md", old_string=telem, new_string="z")), False)
    open(BACKUP, "w").write("# " + telem + "\n")
    check("fragment surviving ONLY in a banked dist is silent",
          run(post("docs/other.md", old_string=telem, new_string="z")), False)
    os.remove(BACKUP)
    # Positive control: the same fragment in an ordinary file must still fire,
    # so the silence above is the exclusion working and not the grep failing.
    open(os.path.join(REPO, "_probe_telem.md"), "w").write(telem + "\n")
    check("same fragment in a normal file still FIRES (positive control)",
          run(post("docs/other.md", old_string=telem, new_string="z")), True)
finally:
    if os.path.exists(os.path.join(REPO, "_probe_telem.md")):
        os.remove(os.path.join(REPO, "_probe_telem.md"))
    if _orig is not None:
        open(LEDGER, "wb").write(_orig)

print("== regressions ==")
old = subprocess.run(["git","show","d7287ea:.sessions/2026-08-08-layer2-ratification.md"],
                     capture_output=True, text=True, cwd=REPO).stdout
r = run(pre("x.md", content=old))
check("real historical defect still caught (6 rows)", r and "6 row(s)" in r, True)
check("hooks README still silent", run(pre(".claude/hooks/README.md",
      content=open(os.path.join(REPO, ".claude/hooks/README.md")).read())), False)
check("fm-local skill silent", run(pre(".claude/skills/owner-brief/SKILL.md", tool="Edit", new_string="x")), False)
check("kit-named skill fires", run(pre(".claude/skills/analysis/SKILL.md", tool="Edit", new_string="x")), True)

print(f"\n{sum(T)}/{len(T)} passed")
sys.exit(0 if all(T) else 1)
