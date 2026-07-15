# 2026-07-15 — Overnight re-sweep + model-line card grooming

> **Status:** `complete`

About to do (as opened): (A) record the 05:40Z read-only seat re-sweep delta vs the 04:28Z baseline; (B) groom the 8 advisory `📊 Model:` line warnings on the 2026-07-14 / pre-reboot cards to the canonical 3-field payload without inventing values; (C) dated delta entry in `docs/fleet-triage.md`; (D) heartbeat re-stamp. ⚑ Self-initiated grooming slice, contained + reversible (docs/control only).

## Done

- **(A) Re-sweep 05:39–05:44Z** (`date -u`; heartbeats via raw `control/status.md` at HEAD, pml via GitHub MCP; newest commits via GitHub MCP). Delta vs the 04:28Z baseline (fm #220): **5 seats newly active post-04:28Z; not-yet-rebooted set unchanged at 9.**

  | Seat | Heartbeat `updated:` | Newest commit | Post-04:28Z? |
  |---|---|---|---|
  | substrate-kit | **05:10Z** (new trigger `trig_01CUfSZo9Uky9DdpoqpZPcfT` = re-arm evidence) | `5905201` 05:13:04Z (#383) | **YES — resumed from 04:21Z STANDBY** |
  | gba-homebrew | 07-14T21:16Z | `4a61ec9` 05:12:49Z (#143) | **YES** |
  | idea-engine | **05:02:38Z** | `85114c5` 05:06:06Z (P065) | **YES** |
  | sim-lab | 04:06:11Z | `b7a6859` 05:41:04Z (V078) | **YES** |
  | fleet-manager | 05:04:27Z | `e4abf1d` 05:07:28Z (#221) | **YES** (coordinator) |
  | superbot-next | 07-14T21:28Z | `ad75bbc` 03:41:00Z | no (rebooted-then, quiet) |
  | websites | 07-14T21:12Z | `3cac461` 03:37:59Z | no (rebooted-then, quiet) |
  | venture-lab | 04:01:46Z | `520bdfc` 04:10:05Z | no (rebooted-then, quiet) |
  | pokemon-mod-lab | 07-14T05:07Z | `7d4fa41` 07-14T15:18Z | no (rebooted-then, quiet) |
  | superbot (hub) | 07-13T18:00Z | `6be93a0` 03:36:26Z | no — not rebooted |
  | trading-strategy | 07-14T21:17Z | `458b43c` 03:38:26Z (fm relay) | no — not rebooted |
  | superbot-games | 07-14T11:41Z | `446a84e` 03:38:31Z (fm relay) | no — not rebooted |
  | superbot-idle | 07-14T11:32Z | `8a7275d` 03:38:39Z (fm relay) | no — not rebooted |
  | superbot-mineverse | 07-14T18:59Z | `b9ade33` 03:40:11Z (fm relay) | no — not rebooted |
  | product-forge | 07-11T19:39Z | `f7f2dd2` 07-14T07:06Z | no — DARK/archive-ready |
  | codetool-lab ×3 (fable5/opus4.8/sonnet5) | 07-09 | 07-14T07:07Z audits | no — STALE-BY-DESIGN |

- **(B) Grooming:** 8 model-line advisories → 7, all findings now the honest `unstated`-effort class. Shape + class findings **cleared on all 8 cards** (post-sweep-reconcile, wake-0235z/0434z/0633z/0845z/2034z, walkthrough-sweep → canonical 3-field payload, family normalized to `Claude Fable (Claude 5 family)`, task-class `docs-only` derived from each card's own scope statement; pre-reboot-review's off-taxonomy `coordination` → `docs-only (coordination)`, both lines). Effort was **never invented**: none of the 7 shape cards states an effort anywhere (card text, dispatch-log, telemetry all checked) so the segment is filed `unstated` — the harvest now records all 8 cards where it previously recorded nothing; the 7 remaining advisories are the honest residue and can only be cleared by inventing values, which stays refused.
- **(C)** `docs/fleet-triage.md`: dated "second v3.6 reboot re-sweep (05:39–05:44Z)" entry, neutral tone.
- **(D)** `control/status.md` re-stamped 05:47:21Z — #220/#221 merged facts, re-sweep delta headline, fm-actionable backlog DRY (remaining ORDERs owner-gated 023/024 vs E#44 or lane-owned 030–044), grooming fact.
- Checkers: `check_owner_queue` CLEAN · `check_roster_freshness` OK (gen #56, 1.9h < 4h threshold — no in-PR regen) · `bootstrap.py check --strict` passes.

## Enders

- ⚑ Self-initiated: the model-line card-grooming slice (B) — contained, reversible, docs-only; nobody ordered it, the 04:28Z-baseline advisory pile made it the obvious overnight groom.
- 💡 Session idea: teach the kit's model-line grammar a first-class `unstated` effort token (recognized missing-data marker, distinct from drift) — honest backfills of pre-taxonomy cards currently trade a shape advisory for a permanent effort advisory, so the lint nags forever about values that provably cannot be recovered; a recognized token keeps never-invent enforced while letting groomed history go quiet.
- ⟲ Previous-session review (owner-queue-kit-go): clean escalation — the kit STANDBY wall went to owner-queue ask C#61 with the wall evidence recorded after exactly one attempt, and the A#62 fable5 click was batched into the same PR rather than a second wake. Miss worth one improvement: the ask assumed only an owner reply could resolve the hold, but this re-sweep found the kit lane self-resolved 6 minutes after the stamp (05:10Z heartbeat + new trigger) — owner-queue asks that a lane can also resolve lane-side should carry a "re-measure the lane before nudging the owner" note so the next wake verifies before escalating further.
- 📊 Model: Claude Fable (Claude 5 family) · high · docs-only
