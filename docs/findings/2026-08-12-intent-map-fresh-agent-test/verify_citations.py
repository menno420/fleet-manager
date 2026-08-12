#!/usr/bin/env python3
"""Verify agent report citations against a pinned snapshot tree.

Input TSV rows: agent<TAB>file<TAB>start-end<TAB>needle
Two modes (Codex round-1 finding: tolerance must not blur attribution):
  default   — substance: PASS if needle occurs within [start-3, end+3]
  --exact   — attribution: PASS only if needle occurs within [start, end]
MISSING-FILE / NO-MATCH otherwise.
"""
import sys, pathlib

TOL = 0 if "--exact" in sys.argv else 3

def main(root, tsv):
    root = pathlib.Path(root)
    rows = []
    for ln in pathlib.Path(tsv).read_text().splitlines():
        ln = ln.rstrip("\n")
        if not ln or ln.startswith("#"):
            continue
        agent, rel, rng, needle = ln.split("\t", 3)
        rows.append((agent, rel, rng, needle))
    npass = 0
    for agent, rel, rng, needle in rows:
        p = root / rel
        if not p.exists():
            print(f"MISSING-FILE\t{agent}\t{rel}\t{rng}")
            continue
        lines = p.read_text(errors="replace").splitlines()
        if "-" in rng:
            a, b = rng.split("-")
        else:
            a = b = rng
        a, b = max(1, int(a) - TOL), min(len(lines), int(b) + TOL)
        window = " ".join(" ".join(lines[a - 1 : b]).split())
        if " ".join(needle.split()).lower() in window.lower():
            print(f"PASS\t{agent}\t{rel}\t{rng}\t{needle[:50]}")
            npass += 1
        else:
            print(f"NO-MATCH\t{agent}\t{rel}\t{rng}\t{needle[:60]}")
    print(f"== {npass}/{len(rows)} PASS")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
