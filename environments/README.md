# `environments/` — Per-seat environment setup scripts from the autonomous era

> **Status:** `reference`
>
> **Tier: RECORD** — historical record; true of its date, never the answer to what is happening now.
> Where you are in the estate: [the map](../docs/MAP.md).

The seats were terminated 2026-07-21; nothing provisions from here. Kept as the record of how each seat's container was configured.

| file | what it is |
|---|---|
| `README.md` | Registry index for claude.ai environment specs and templates: the no-secret-values hard rule, the agents-draft/owner-pastes split, a file…. |
| `SPEC-TEMPLATE.md` | Fill-in-the-blanks template for proposing a new Project environment — identity, repos, setup script, var NAMES table, model, scopes and o…. |
| `archetype-bot-prod.sh` | Thin ~25-line knob config for the bot-prod archetype (superbot/superbot-next production-var lane) that resolves and sources setup-base.sh…. |
| `archetype-coordinator.sh` | Thin knob config for the coordinator archetype (multi-repo workspace) carrying the full python3.10/3.11 pin table and sourcing setup-base…. |
| `archetype-gba-lab.sh` | Full standalone GBA-lab setup script: apt/pip baseline, gated devkitARM r68 mirror pull with Track-B detection, pokeemerald agbcc build, …. |
| `archetype-pinned-research.sh` | Thin knob config for the pinned-research archetype (trading-strategy, websites) with a five-name env presence report; sources setup-base.…. |
| *…5 more* | see the files themselves — each gist is in [the audit's raw record](../docs/audits/2026-08-10-full-read/raw/gists.tsv). |
