# fleet-manager — the manager Project's home

This repo is the fleet manager's **working memory**: its playbook, worker
templates, owner queue, dispatch log, and its own protocol heartbeat.

It is **NOT program record**. The fleet manifest, EAP evidence, and program
rollups live in **menno420/superbot** (`docs/eap/`).

**Design rule:** program-facing truth → superbot; manager-internal memory → here.

## Map

| Where | What |
|---|---|
| [`docs/playbook.md`](docs/playbook.md) | The manager's operating memory — dated, numbered rules (orientation, dispatch, protocol, platform walls, owner interface). |
| [`docs/owner-queue.md`](docs/owner-queue.md) | The one deduplicated queue of things waiting on the owner. |
| [`docs/dispatch-log.md`](docs/dispatch-log.md) | Dated log of what the manager dispatched and shipped. |
| [EAP final-night worklists (2026-07-13)](docs/eap-final-night-worklists-2026-07-13.md) | ORDER 045 fleet sweep — per-seat prioritized night worklists, DARK dispositions, cross-cutting findings. |
| [Central docs plan](docs/central-docs-plan.md) | Fleet documentation centralization plan — what moves where, migration order. |
| [Fleet inconsistencies (2026-07-13)](docs/fleet-inconsistencies-2026-07-13.md) | 19-repo review ledger of cross-fleet inconsistencies — fix-now items + ORDER-to-lane rest. |
| [EAP story](docs/eap-story.md) | The Extended Autonomy Program, told start to finish — what was built and how. |
| [EAP retrospective](docs/eap-retrospective.md) | EAP retrospective — what worked, what didn't, what carries forward. |
| [`templates/`](templates/) | Standard preamble blocks pasted into every worker prompt. |
| [`control/`](control/) | Protocol heartbeat — `inbox.md` (owner → manager orders), `status.md` (manager heartbeat). |
