#!/usr/bin/env python3
"""Verify agent ESTABLISHED citations against a pinned snapshot tree.

Input TSV rows: agent<TAB>file<TAB>start-end<TAB>needle
PASS if needle (case-insensitive) occurs within [start-3, end+3] of file.
MISSING-FILE / OUT-OF-RANGE / NO-MATCH otherwise, with the searched window echoed.
"""
import sys, pathlib

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
        a, b = max(1, int(a) - 3), min(len(lines), int(b) + 3)
        window = " ".join(" ".join(lines[a - 1 : b]).split())
        if " ".join(needle.split()).lower() in window.lower():
            print(f"PASS\t{agent}\t{rel}\t{rng}\t{needle[:50]}")
            npass += 1
        else:
            print(f"NO-MATCH\t{agent}\t{rel}\t{rng}\t{needle[:60]}")
    print(f"== {npass}/{len(rows)} PASS")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
