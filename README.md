# fleet-manager — the manager Project's home

This repo is the fleet's **records custodian** (Option A custodian-primary —
owner decision 2026-07-11) and the fleet manager's working memory: its
playbook, worker templates, owner queue, dispatch log, and its own protocol
heartbeat.

**Fleet state is canonical HERE**: the generated roster (`docs/roster.md`)
superseded the hand-kept superbot `docs/eap/fleet-manifest.md` on 2026-07-11
and is the fleet-state source of truth, alongside the owner queue, evidence
index, triage register, and triggers snapshot. The EAP **program-narrative
corpus** (the story of the program) stays in **menno420/superbot**
(`docs/eap/`) — indexed from here (`docs/evidence-index.md`), never copied.

**Design rule:** program-narrative truth → superbot `docs/eap/`; fleet-state
records custody + manager-internal memory → here.

## Map

| Where | What |
|---|---|
| [`docs/playbook.md`](docs/playbook.md) | The manager's operating memory — dated, numbered rules (orientation, dispatch, protocol, platform walls, owner interface). |
| [`docs/owner-queue.md`](docs/owner-queue.md) | The one deduplicated queue of things waiting on the owner. |
| [`docs/dispatch-log.md`](docs/dispatch-log.md) | Dated log of what the manager dispatched and shipped. |
| [EAP final-night worklists (2026-07-13)](docs/eap-final-night-worklists-2026-07-13.md) | ORDER 045 fleet sweep — per-seat prioritized night worklists, DARK dispositions, cross-cutting findings. |
| [Central docs plan](docs/central-docs-plan.md) | Fleet documentation centralization plan — what moves where, migration order. |
| [`docs/trigger-health-spec.md`](docs/trigger-health-spec.md) | The per-wake trigger-health spec (R26 / ORDER 020) — canonical here since 2026-07-14 (plan A2). |
| [`docs/q-index.md`](docs/q-index.md) | Repo-qualified Q→pointer table for cross-repo-cited owner decisions (superbot router stays canonical). |
| [Fleet inconsistencies (2026-07-13)](docs/fleet-inconsistencies-2026-07-13.md) | 19-repo review ledger of cross-fleet inconsistencies — fix-now items + ORDER-to-lane rest. |
| [EAP story](docs/eap-story.md) | The Extended Autonomy Program, told start to finish — what was built and how. |
| [EAP retrospective](docs/eap-retrospective.md) | EAP retrospective — what worked, what didn't, what carries forward. |
| [`templates/`](templates/) | Standard preamble blocks pasted into every worker prompt. |
| [`control/`](control/) | Protocol heartbeat — `inbox.md` (owner → manager orders), `status.md` (manager heartbeat). |
