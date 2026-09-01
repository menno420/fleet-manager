#!/usr/bin/env python3
"""shard_patterns.py — split the 284-pattern catalogue into readable shards for a fan-out.

Why: `docs/findings/data/2026-08-29-agent-error-patterns.jsonl` is 1.47 MB — too
large for one reader to hold whole, and reading it in part is TRAP-008 waiting
to happen. Sorted by repo spread (the strongest signal in the set, per the data
README), then severity, then how many instances are actually listed, and cut
into N shards so each reader gets ~24 rows it can read to the end.

Usage (from the repo root):
    python docs/findings/data/workflows/shard_patterns.py <out_dir> [shards=12]

Writes shard-01.json … shard-NN.json, census-20-repos.json and INDEX.json into
<out_dir>. Read only; never modifies the catalogue. Stdlib only.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
PATTERNS = REPO / "docs/findings/data/2026-08-29-agent-error-patterns.jsonl"
CENSUS = REPO / "docs/findings/data/2026-08-29-repo-instruction-census.jsonl"


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    out = Path(sys.argv[1])
    n_shards = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    out.mkdir(parents=True, exist_ok=True)

    rows = [json.loads(l) for l in PATTERNS.read_text(encoding="utf-8").splitlines() if l.strip()]
    sev = {"high": 0, "medium": 1, "low": 2}
    rows.sort(key=lambda r: (-int(r.get("repo_count") or 0), sev.get(r.get("severity"), 3), -len(r.get("instances") or [])))
    for i, r in enumerate(rows):
        r["_rank"] = i + 1
        r["_listed_instances"] = len(r.get("instances") or [])

    size = (len(rows) + n_shards - 1) // n_shards
    index = []
    for s in range(n_shards):
        chunk = rows[s * size:(s + 1) * size]
        if not chunk:
            break
        p = out / f"shard-{s + 1:02d}.json"
        p.write_text(json.dumps(chunk, ensure_ascii=False, indent=1), encoding="utf-8")
        index.append({"shard": p.name, "rows": len(chunk), "rank_range": [chunk[0]["_rank"], chunk[-1]["_rank"]],
                      "bytes": p.stat().st_size, "names": [c["name"] for c in chunk]})

    census = [json.loads(l) for l in CENSUS.read_text(encoding="utf-8").splitlines() if l.strip()]
    (out / "census-20-repos.json").write_text(json.dumps(census, ensure_ascii=False, indent=1), encoding="utf-8")
    (out / "INDEX.json").write_text(json.dumps({
        "source": str(PATTERNS.relative_to(REPO)), "total_rows": len(rows),
        "sorted_by": "repo_count desc, severity, listed instances desc", "shards": index,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    # The census the corpus contract wants, printed rather than composed by hand.
    print(f"patterns: {len(rows)} rows -> {len(index)} shards "
          f"({', '.join(str(i['bytes']) for i in index)} bytes)")
    print(f"high severity & repo_count>=3: {sum(1 for r in rows if r.get('severity') == 'high' and int(r.get('repo_count') or 0) >= 3)}")
    print(f"no covering mechanism named: {sum(1 for r in rows if not r.get('already_covered_positive'))}")
    print(f"panel-killed (survives=false): {sum(1 for r in rows if r.get('survives') is False)}")
    print(f"census rows: {len(census)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
