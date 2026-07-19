# 2026-07-19 · fm roster-regen cron resilience (second cron line + hub-merge ask)

> **Status:** `complete`

About to happen (declared born-red): fix-slice for the roster-regen scheduler-drop
diagnosis (this hour, read-only pass by the coordinator seat). GitHub's best-effort
scheduler is dropping `roster-regen.yml`'s `40 */2 * * *` windows — run objects were
never created for 00:40Z three nights running, plus 02:40Z tonight; the workflow
itself is healthy (state active, 30/30 recent runs green, chronic +45–140m start
delay). Remedy in this PR: add a second cron line `40 1-23/2 * * *` (odd hours) for
net hourly coverage — regen exits clean when nothing changed, so extra fires cost
~30s each. This PR touches `.github/workflows/**`, so merge-on-green deliberately
skips it: it is opened READY with the blocker named and the merge is queued as
owner-queue item `OQ-FM-ROSTER-CRON-SECOND-LINE` (VENUE:hub). Also: annotate the
`OQ-FM-ROSTER-CRON-RELIABILITY` watch item (verdict reached) and refresh
`control/status.md`.

- **📊 Model:** fable-5 · high · runtime bugfix — roster-regen scheduler-drop resilience (workflow cron line + owner-queue + heartbeat)

## What shipped (PR #344)

- `.github/workflows/roster-regen.yml` — second schedule line `- cron: "40 1-23/2 * * *"`
  (odd hours) under the existing `40 */2 * * *` (even hours) → net hourly firing attempts;
  one dropped window is now covered by the adjacent hour. Provenance comment inline. YAML
  validity verified (`yaml.safe_load` → both cron entries parse).
- `docs/owner-queue.md` — new Active (A) item **`OQ-FM-ROSTER-CRON-SECOND-LINE`**
  (VENUE:hub, six-field: WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFY·RISK, recommendation bolded —
  merge fm PR #344 on green; `merge-on-green.yml` skips workflow diffs by design, so it
  will not self-land). Section-(A) intro updated from "EMPTY (this repo)" to "1 open PR".
  **`OQ-FM-ROSTER-CRON-RELIABILITY`** (the watch) annotated with the verdict — drops DO
  recur (00:40Z never-created 3 nights running: 07-17/18/19; +02:40Z tonight; workflow
  active, 30/30 green, chronic +45–140m delay) — "remedied by
  OQ-FM-ROSTER-CRON-SECOND-LINE once merged"; the watch stays open until the fix lands
  and proves out (honest close only on evidence).
- `control/status.md` — `updated:` → 2026-07-19T03:41Z; diagnosis one-liner + baton
  refresh (hub: product-forge #29 + fm #344; ~06:00Z websites ORDER-036 escalation +
  re-sweep).
- `.substrate/guard-fires.jsonl` — telemetry delta committed (do-not-revert).

**Blocker, by design:** PR #344 touches `.github/workflows/**` → the merge-on-green
workflow deliberately skips it. Parked READY with the blocker named in the body; the
merge is the queued hub-venue action `OQ-FM-ROSTER-CRON-SECOND-LINE`. Not force-merged
from this venue on purpose — the hub venue owns workflow-diff landings.

## Enders

- 💡 **Session idea:** `scripts/gen_hub_queue_baton.py` — derive the night-watch "hub
  queue" baton line live instead of hand-maintaining it: parse `docs/owner-queue.md`
  section (A) for open merge items, check each PR's live state (direct-PAT REST), and
  print the one-liner for `control/status.md` (flagging rows whose PR merged/closed —
  auto-detecting stale OQ merge rows like the retired pokemon #98 one). Distinct from
  `check_owner_queue.py` (static grammar check) and from the already-recorded
  regen-window skip detector (Actions telemetry, different object). Dedup-grepped
  `scripts/` + `docs/ideas/` — no existing hub-queue lister.
- ⟲ **Previous-session review (PR #343, 03:0xZ records slice):** solid honest slice —
  the stall-guard regen (gen #98), the pokemon #98 OQ retirement, and the no-conflict
  origin check were all clean and well-evidenced. What it missed: it recorded the 02:40Z
  window skip as a symptom but did not pull the Actions run list to distinguish
  "delayed" from "run object never created" — exactly the evidence this fix-slice
  needed re-derived one hour later. Workflow improvement: when a records slice observes
  a missed automated window, spend the extra two minutes capturing the run-object
  evidence (run list around the window) in the card, so the follow-up fix-slice starts
  from evidence instead of re-deriving the diagnosis.
- **Doc audit:** the diagnosis is durable in three homes — PR #344 body (full), the
  annotated `OQ-FM-ROSTER-CRON-RELIABILITY` row (verdict + pointer), and the workflow's
  inline provenance comment; `control/status.md` carries the heartbeat + baton. Nothing
  chat-only. Guard-fires delta committed.
- **Claim:** deleted in this flip commit (`bootstrap claim fm-roster-cron-resilience
  --delete`).
