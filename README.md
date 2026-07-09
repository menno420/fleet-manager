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
| [`templates/`](templates/) | Standard preamble blocks pasted into every worker prompt. |
| [`control/`](control/) | Protocol heartbeat — `inbox.md` (owner → manager orders), `status.md` (manager heartbeat). |
