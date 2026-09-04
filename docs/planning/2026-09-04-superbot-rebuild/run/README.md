# Run material

| file | what it is |
|---|---|
| [`CONTRACTS.md`](CONTRACTS.md) | the `fleet-preflight` contract sheet, filled **before** the first review agent spawned and quoted verbatim by the plan |
| [`independent-findings.md`](independent-findings.md) | measurements this session made **itself**, kept separate from the fleet's rows so the fleet's own verification lane cannot be credited with confirming them |
| [`census.txt`](census.txt) | the corpus census, printed by the command that produced it |
| [`survival_rule.py`](survival_rule.py) | the AGGREGATE rule as an executable expression, with its field audit and its kill/survive fixtures. `python3 survival_rule.py` → exit 0 |
| [`capture_literal_scan.py`](capture_literal_scan.py) | the capture-world-literal instrument, with positive and negative controls. `--selftest` → exit 0. **Its D1 detector was retired at 1/12 precision** — the retirement is the finding |
| `raw/` | the fleet's retained output (agent journals) |

Nothing in this folder is authoritative for the plan's conclusions; it is the
material that lets someone check them.
