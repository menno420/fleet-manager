# Run material

> **Status:** `reference` — run material, not conclusions.

| file | what it is |
|---|---|
| [`CONTRACTS.md`](CONTRACTS.md) | the `fleet-preflight` contract sheet, filled **before** the first review agent spawned and quoted verbatim by the plan |
| [`independent-findings.md`](independent-findings.md) | measurements this session made **itself**, kept separate from the fleet's rows so the fleet's own verification lane cannot be credited with confirming them |
| [`census.txt`](census.txt) | the corpus census, printed by the command that produced it |
| [`survival_rule.py`](survival_rule.py) | the AGGREGATE rule as an executable expression, with its field audit and its kill/survive fixtures. `python3 survival_rule.py` → exit 0 |
| [`capture_literal_scan.py`](capture_literal_scan.py) | the capture-world-literal instrument, with positive and negative controls. `--selftest` → exit 0. **Its D1 detector was retired at 1/12 precision** — the retirement is the finding |
| [`reachability_probe.py`](reachability_probe.py) | the route-graph walk that closes the 2026-08-05 audit's two-tap honest null, written as the PROTOTYPE of the successor's reachability gate: declares its population, asserts a committed floor, walks the shipped manifest. `python3 reachability_probe.py` |
| [`in-flight-direction.md`](in-flight-direction.md) | the owner statement that landed **mid-run**, caught by the sheet's own BASE re-read: what it changes for this review, and the standing action for the synthesis step |
| [`evidence-digest.md`](evidence-digest.md) | every retained fleet row compacted to one line, built for the writing step. **Transcription, not judgement** — `lane-claimed` until re-derived |
| [`refutation-pass.md`](refutation-pass.md) | the adversarial verification the AGGREGATE contract designed as its second filter — **62 of 196 lane strengths refuted**, 34 of them cited in the deliverables. Check any `lane-claimed` figure here before relying on it |
| `raw/` | the fleet's retained output (agent journals, `lane-results.json`, `refutation-pass.json`) |

Nothing in this folder is authoritative for the plan's conclusions; it is the
material that lets someone check them.
