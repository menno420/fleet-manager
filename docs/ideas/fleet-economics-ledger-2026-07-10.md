---
state: captured
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Fleet economics ledger — know what the fleet costs before the free window closes

> **Status:** `ideas`

**Idea:** instrument the fleet's own operating cost before the EAP free
window closes **2026-07-14**: (1) add a token/estimated-cost line to the
standing telemetry every session card already mandates; (2) a fleet-manager
routine aggregates per-lane cost vs shipped output into one committed
ledger; (3) re-derive the blueprint §2a wake-cadence table (Class A hourly /
B 4-hourly / C daily) with cost as an input — the measured order-pickup SLA
data makes that a real trade-off calculation, not vibes.
**Why worth having:** the entire wake-cadence architecture was designed
during a free evaluation window. Nothing in the corpus measures what the
fleet actually costs to run: token counts were logged only incidentally,
heartbeat economics were argued in PR-rounds not currency, and substrate-kit
explicitly disputed hourly wakes as too expensive (D4) with zero cost data
to settle it. When the window closes, a 10-lane fleet with hourly Class-A
wakes has an unknown burn rate and the owner — a non-coder funding this —
has no number to steer with. Figures will be estimates (agents cannot
precisely meter their own tokens) and post-EAP cost may be denominated in
quota rather than per-token currency — that ambiguity is itself the owner
decision the ledger informs.
**Unblocks:** an informed owner decision on which lanes earn their cadence
post-EAP; right-sizing the remaining free-window burn; the
return-on-agent-labor denominator venture-lab needs anyway. Distinct from
spend-instrument (purchases) and bot-analytics (bot usage): this is the cost
side of the fleet's own operation.
**Provenance:** Fable-5 fleet review finding F12 (verified: no fleet-cost
measurement anywhere at HEAD; venture-lab's per-candidate token accounting
is the only cost rail, one lane only). Synthesis:
[`../findings/fable5-review-2026-07-09.md`](../findings/fable5-review-2026-07-09.md).
**Status:** captured (not approved).
