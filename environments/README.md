# Environment registry

> **Status:** `living-ledger` — the fleet's registry of Claude Code **environment
> specs** + **reusable templates**. Agents keep it current; the owner reads it when
> creating or editing an environment in claude.ai.

## HARD RULE — no secret values, ever

**NEVER store secret VALUES in this directory — or anywhere in this repo.**
Variable **NAMES** and **placeholders** (`<SET-IN-CLAUDE-AI>`) only. Real values
live solely in the claude.ai environment config (owner-side). A spec that needs a
credential says *which name* to set, never *what* to set it to. This holds even
for "harmless" values (IDs, URLs): if it isn't a name or a placeholder, it doesn't
go here.

## Why this exists — the platform wall

**Agents cannot create or edit Claude Code environments.** The only place an
environment can actually be created or changed is **claude.ai/code → Environments**,
which is owner-side UI (same wall class as playbook R12/R13 — quote it, don't
assume around it). So the split is:

- **Agents** draft and maintain environment **specs** here, from the templates —
  complete, paste-ready, click-level (playbook R11/R16).
- **The owner** pastes them into **claude.ai/code → Environments** — the setup
  script into the Setup script field, the variable names (with real values) into
  the environment variables panel.

The websites control-plane renders this directory read-only at `/environments`
(ORDER 005), so the owner can copy from a browser without opening the repo.

## Map

| File | What |
|---|---|
| [`archetypes.md`](archetypes.md) | **The ≤4 consolidated environment archetypes** (owner directive 2026-07-09): project → archetype mapping, var-name unions, 3.10/3.11 wrinkle, owner paste-steps. Start here. |
| [`archetype-python-lab.sh`](archetype-python-lab.sh) | Tested setup script — stdlib/tiny-dep lab lanes (kit, 3 codetool arms, games, fleet-manager, venture-lab). |
| [`archetype-pinned-research.sh`](archetype-pinned-research.sh) | Tested setup script — pinned-requirements lanes (trading-strategy incl. its two-source workspace shape, websites). |
| [`archetype-bot-prod.sh`](archetype-bot-prod.sh) | Tested setup script — production bot lanes (superbot-next lockfile, legacy superbot 3.10 pin). Only archetype allowed production-pointing vars. |
| [`archetype-coordinator.sh`](archetype-coordinator.sh) | Tested setup script — the live multi-repo coordinator workspace (superset manifest handling). |
| [`templates/setup-universal.sh`](templates/setup-universal.sh) | The proven defensive multi-repo setup shim (playbook R15: exit 0 always) the archetype scripts derive from. |
| [`templates/env-vars.md`](templates/env-vars.md) | Placeholder schema of the standard fleet variable set — names + purpose only, incl. the Railway-trio DANGER note. |
| [`multi-repo.md`](multi-repo.md) | Spec of the CURRENT live `multi-repo` environment, as built 2026-07-09. |
| [`SPEC-TEMPLATE.md`](SPEC-TEMPLATE.md) | The form an agent fills when proposing a new Project's environment. |

## Flow (new Project → running environment)

1. Agent copies `SPEC-TEMPLATE.md` → `environments/<env-name>.md`, fills every
   field (setup script linked from `templates/`, var **names** from
   `templates/env-vars.md`).
2. The spec lands via PR; the owner-queue / `/queue` page carries the ⚑ ask with
   the paste-steps.
3. Owner pastes at **claude.ai/code → Environments** (click path is in every
   spec's "Owner paste-steps" section) and sets real values there.
4. Agent in the new environment verifies setup ran (session boots, deps present)
   and updates the spec's `Verified` line — specs describe reality, not intent.
