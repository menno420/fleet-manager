# 2026-07-15 — queue-a63-next-triage (fm slice: A#63 + superbot-next STALE triage + heartbeat)

> **Status:** `in-progress`

- **📊 Model:** Claude Fable (Claude 5 family) · high · docs-only

## What is about to happen

- Append owner-queue **A#63**: one merge click for fm PR #227 (lanes.json regen
  fix — green but parked on the merge-on-green owner-merge-only rail because it
  diffs a workflow file).
- Record a dated `docs/fleet-triage.md` entry: **superbot-next verdict STALE
  (stalled mid-close)** — coordinator rebooted 04:20Z, worked to 04:58Z, went
  dark mid-close; PR #490 open born-red; no wake trace since ~05:01Z; remedy in
  the owner's hands (live-advised ~10:1xZ).
- Re-stamp `control/status.md` heartbeat with these facts.
- Run owner_queue + roster_freshness checkers; enders; flip this card last.
