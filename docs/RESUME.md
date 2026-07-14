# RESUME — start here after the hiatus

> **Status:** `reference`
>
> The revival door for the fleet-manager seat. Written 2026-07-14 as the
> fleet went dormant (owner order: EAP complete, all projects paused for an
> undisclosed period). First read for whichever session wakes this seat back
> up. Everything below was verified against the tree at write time; per the
> truth bar, files and sibling HEADs win over this doc wherever they have
> since moved.

## 1 · What this repo is

fleet-manager is the fleet's source of truth and coordination hub: the
manager seat that steers the ~13-seat / ~19-repo agent fleet through
`control/` (owner-written `inbox.md` orders → manager-written `status.md`
heartbeat) and holds the cross-repo ledgers (roster, owner-queue, triage,
capabilities, dispatch log). The centralization program that makes it the
main SoT is [docs/planning/2026-07-14-central-docs-plan.md](planning/2026-07-14-central-docs-plan.md):
**Slice 0 is complete fm-side** (dispatch-log, 0235Z wake record: "the
Slice 0 items themselves, which are complete fm-side") and **Phase 1 is done
for everything fm-write-scope** (plan's Phase 1 status note @ 06:50Z — it
closes fully when websites + sim-lab execute their lane-side folds).
**Phases 2–5 (doctrine consolidation · pipeline ledgers · archive rescue ·
owner-gated moves) resume on revival.**

## 2 · Boot path for a fresh session

1. `CONSTITUTION.md` (repo root) — the binding working agreement.
2. `control/status.md` — the dormancy record and last-known fleet state.
3. [docs/roster.md](roster.md) (generated fleet roster — its generated-at
   will be stale after the hiatus; trust lane heartbeats per its
   kill-switch note) + [docs/owner-queue.md](owner-queue.md) +
   [docs/playbook.md](playbook.md) (R1–R25 operating rules).

## 3 · Where the EAP finale artifacts live

- **Final-night worklists** (per-seat, ORDER 045):
  [docs/eap-final-night-worklists-2026-07-13.md](eap-final-night-worklists-2026-07-13.md).
- **Audits collection** (all 13 seat audits, collected):
  [docs/eap-audit-collection.md](eap-audit-collection.md).
- **Review docs**: [docs/eap-retrospective.md](eap-retrospective.md) (the
  program retrospective), [docs/eap-story.md](eap-story.md) (the narrative),
  [docs/eap-final-recon-2026-07-14.md](eap-final-recon-2026-07-14.md)
  (final reconciliation sweep).
- **Owner checklist** (53 rows, ~47 still open at dormancy —
  console/credential/decision items for one sitting):
  [docs/eap-owner-checklist-2026-07-14.md](eap-owner-checklist-2026-07-14.md).
- **Final feedback email draft** (body final, scale-context addendum added
  2026-07-14): [docs/eap-final-email-draft-2026-07-14.md](eap-final-email-draft-2026-07-14.md).
- **Final-state triage table** (keep / replace / archive / delete verdict
  per repo): [docs/fleet-triage.md](fleet-triage.md).

## 4 · How to revive the seat

1. **Re-arm the failsafe cron** with the exact stored prompt from
   [docs/prompts/v3/per-project/fleet-manager-startup.md](prompts/v3/per-project/fleet-manager-startup.md)
   (name "Fleet Manager failsafe wake", cron `30 */2 * * *` — the seat's
   slot in the stagger table at
   [docs/prompts/v3/per-project/README.md](prompts/v3/per-project/README.md)
   § "Failsafe cron stagger table"; a foreign trigger in the slot → report,
   never re-slot). The pre-dormancy failsafe
   `trig_01FpTbpXCeGcotnBpTkscAdr` was retired at shutdown (see the
   dormancy heartbeat) — create fresh, verify via `list_triggers`
   (paginate fully) before trusting it.
2. **Restart the pacemaker**: the ~15-min `send_later` continuation chain
   (Q-0265 pattern — ONE send_later per working turn, never stacked; the
   ender arms nothing), per
   [docs/prompts/v3/per-project/fleet-manager-custom-instructions.md](prompts/v3/per-project/fleet-manager-custom-instructions.md).
3. Resume the central-docs-plan phases (§1 above) and drain the batons (§5).

## 5 · Standing batons (open work waiting at dormancy)

- **substrate-kit inbox ORDERs 022 + 023 unconsumed** — the stop-hook
  branch-recreation guard (022) and the scheduled branch-sweep workflow
  template (023, extends 022; remedy settled in
  [docs/findings/branch-recreation-census-2026-07-14.md](findings/branch-recreation-census-2026-07-14.md)).
  Both await a kit release + adopter regeneration; verify at kit HEAD
  before acting.
- **fm ORDER 024 owner-gated** (`control/inbox.md`) — gated on the
  owner-queue E#44 consolidation-plan letter; do not execute until the
  owner approves.
- **superbot follow-up leads** (dispatch-log true-up 2026-07-14T19:51Z):
  the checker-vs-test severity mismatch (superbot
  `.sessions/2026-07-14-eap-docs-closeout.md` — `check_docs.py` reports the
  docs ratchet soft while the twin pytest invariant enforces it hard) and
  the docs-budget ratchet 21 → 22 raise, which carries an explicit
  reversal path once the EAP closeout is consumed.
- **Owner checklist ~47 open rows** — §3 above; deadline rows are gone,
  the rest is a one-sitting sweep whenever convenient.
- **central-docs-plan Phases 2–5** — §1 above; Phase 1 residue = websites
  ORDER 028 + sim-lab ORDER 007 lane-side folds (delivered, `status: new`
  at their HEADs at write time).
