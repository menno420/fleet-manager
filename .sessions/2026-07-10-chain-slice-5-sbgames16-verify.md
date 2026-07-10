# 2026-07-10 — chain slice #5: MANAGER-VERIFY superbot-games#16 (CI collection scope)

> **Status:** `complete`

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

## Done (close-out) · end 2026-07-10T23:18Z (`date -u`)

Declared scope landed exactly (this PR, #50):

- **Inbox at HEAD `af66514`: no ORDER newer than 013** (newest = 013, DONE).
- **superbot-games#16 MANAGER-VERIFIED — CONFIRMED-STILL-BROKEN at HEAD `b134961`.**
  The pytest step still runs `python3 -m pytest tests/ -q`; collection scope
  unchanged (`tests/` holds only `tests/mining/`; exploration's 7 test files under
  `games/exploration/tests/` verified present at HEAD and invisible to the gate).
  ORDER 001 (filed `099664c`, 12:47Z) NOT executed by any commit since `4493292`
  (only kit upgrades #22/#23 landed since). **Precision the verify added:** the
  row's fix pointer `.github/workflows/substrate-gate.yml:62` is **STALE** — the
  v1.2.0→v1.7.0 kit upgrade (#22 @ `4493292`) relocated the pytest step verbatim
  into the host carve-out `.github/workflows/tests.yml` (kit-owned gate regenerates
  on upgrade), so ORDER 001's one-line fix now targets **`tests.yml`** (blob
  `09b65f4` at HEAD): widen collection to ALL suites + add the count assertion.
  Verdict + escalation (P0 ORDER unconsumed; repo has no trigger, both gen-1 lanes
  archived — consumption rides the Q-0267 gen-2 boot) recorded on the row.
- **sb#1920: NO new @codex comment** — thread unchanged (question 4939890801 +
  quota refusal 4939891407 only). No annotation made, per the
  quota-refusals-don't-count rule.
- **`control/status.md`** heartbeat: 23:20Z stamp, chain-slice #5 record, work
  ladder updated (#16 candidate consumed; next: superbot-games#5 or the trading#21
  remainder), both ⚑ owner flags kept (games-mapping react · UNIVERSAL.md
  permissions grant).

## 💡 Session idea

**Kit upgrades should carry a "relocated-pointers" check.** The #16 verify's only
non-binary finding was that a kit upgrade silently moved the fix target
(substrate-gate.yml → tests.yml) out from under a standing review-queue row and an
open P0 ORDER — both still pointed at the old file. A one-line convention for kit
upgrade PRs ("grep the repo's own inbox/queue/docs for paths the upgrade relocates;
annotate or fix the pointers in the same PR") would keep standing orders executable
across upgrades instead of aging into wrong-file instructions.

## ⟲ Previous-session review

Chain slice #4 (PR #49) did the right prep: its groom pass pre-validated every row's
head SHA and explicitly named #16 as the next candidate with the expected binary
outcome — this slice executed in minutes because the target, the ORDER, and the
escalation path were already written down. One miss, now visible: the groom stamped
#16's head as `5c71c61` (the PR's own merge SHA) but didn't note the repo had
ALREADY moved past it (the v1.7.0 kit upgrade #22 landed 20:22Z, before the 22:5x
groom) — a "repo HEAD @ groom time" column next to the row's own head SHA would
have caught the file relocation one slice earlier. Concrete improvement: the groom
template gains that one field, fillable from the same API call that validates the
row.

📊 Model: Claude (Fable family) — family-level only per Q-0262.
