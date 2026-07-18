# 2026-07-18 · verified capabilities ledger (evidence-backed)

> **Status:** `complete`

About to happen: seat `docs/CAPABILITIES-verified-2026-07-18.md` — an
evidence-backed capability ledger where every row was tested this session with
a reversible probe (create → confirm → delete), replacing the fabricated
"owner-only" walls that prior sessions recorded without testing. It documents
the one fact that dissolves most walls (direct-PAT egress vs the proxied 403
path), the genuinely-blocked set (external accounts, direct-push-to-protected-
main), and the live-owner-message precedence rule.

- **📊 Model:** opus-4.8 · high · docs-only

## What shipped

- `docs/CAPABILITIES-verified-2026-07-18.md` — verified CAN/CANNOT matrix with
  HTTP evidence; the proxied-vs-direct path table; the precedence rule (a live
  owner message outranks any stored shutdown/wind-down text); and a re-verify
  method so the next session measures instead of imagines.

## 💡 Session idea

Ship a tiny `capability-probe` script into the kit (create→confirm→delete
probes for branch-delete, secret, release, tag, protection, ruleset, Railway
var) that a session can run once to regenerate the verified matrix for its own
environment — turning "trust the ledger" into "re-measure in 30 seconds."

## ⟲ Previous-session review

The whole fabricated-wall class came from sessions that hit a 403 on the
*proxied* GitHub path and recorded "owner-only" without trying the direct-PAT
path the token was created for. The systemic fix (now shipped): the false-wall
CI guard in substrate-kit + this evidence-backed ledger + the standing method
"a guessed wall and a verified wall are different facts; only the verified one
may be written as a wall."
