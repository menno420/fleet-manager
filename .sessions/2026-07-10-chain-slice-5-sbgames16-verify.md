# 2026-07-10 — chain slice #5: MANAGER-VERIFY superbot-games#16 (CI collection scope)

> **Status:** `in-progress`

📊 Model: Claude (Fable family) · start 2026-07-10T23:12Z (`date -u`)

## Declared at open (born-red)

Q-0265 continuation-chain slice #5 (worker under the coordinator seat). Lean slice.
About to land:

1. **Inbox re-read at HEAD** — report any ORDER newer than 013 (report, not execute).
2. **MANAGER-VERIFY superbot-games#16** (the review-queue's recommended candidate,
   the fleet's canonical "green gate lies" row): binary check at superbot-games HEAD —
   does the CI pytest step still run `pytest tests/ -q` (73/121, exploration suites
   invisible)? Has ORDER 001 (collect-ALL + count assertion) been executed by any
   commit since `4493292`? Verdict recorded on the row: CONFIRMED-STILL-BROKEN
   (with the exact file@SHA ORDER 001 must change) or FIXED (cite commit).
3. **sb#1920 row** — annotate ONLY if a new substantive @codex comment exists
   (one API call; quota refusals don't count).
4. **`control/status.md`** heartbeat LAST — 23:2xZ stamp, chain-slice #5 record,
   both standing ⚑ owner flags kept.
5. **This card**, flipped `complete` as the deliberate final step.

Landing: born-red card holds the gate red → work → heartbeat + flip → PR ready →
substrate-gate Actions poll → REST squash on green (R12 wall: no direct
self-merge). Family-level model names only (Q-0262). After merge: re-arm the
chain (`send_later`, ~15 min).
