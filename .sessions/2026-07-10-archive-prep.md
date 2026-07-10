# 2026-07-10 — Archive prep: manager-chat succession package (gen-2 → gen-3 handoff)

> **Status:** `in-progress`

📊 Model: Fable 5 · fleet worker (archive prep, owner-directed) · start 2026-07-10T12:59Z (`date -u`)

## Declared at open (born-red)

The owner is archiving the current manager chat. This PR commits everything from that
session not yet durable, as the successor package (mirrors the gen-1 succession model,
`docs/handoff-2026-07-09.md`). About to land:

1. **`docs/handoff-2026-07-10.md`** (badge: `owner-guidance`) — the manager-successor
   package: read order for the next manager chat, live fleet state, in-flight/promises
   (⚑B/⚑D freeze, gen-3 gate, ORDERs 001–004, economics-ledger deadline, Anthropic
   follow-up), and the hard-won delivery-channel SOP (PR-comment + ack token).
2. **`docs/capabilities.md` — APPEND** — new wall: private repos on this GitHub plan
   cannot enable the auto-merge toggle (owner-verified 2026-07-10); resolution = REST
   merge-on-green (R21).
3. **`docs/dispatch-log.md` — APPEND** — two entries: (a) the pokemon-mod-lab
   visibility saga (public → counter → private; root cause = the private-plan
   auto-merge toggle wall); (b) this archive-prep session.
4. **This card**, flipped `complete` as the deliberate last commit.

Everything reconciled against HEAD `707f666` immediately before composing (R19; no open
PRs, no remediation in flight at the check). Landing: born-red card holds the gate red;
flips as the last commit; **REST merge-on-green** (R21 — private-plan repo, auto-merge
toggle unavailable; no arm attempt).
