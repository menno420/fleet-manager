# registry/ — machine-readable fleet registries

> **Status:** `reference`
>
> Generated artifacts, one named writer each (central-docs-plan §4 class C:
> "no second hand-maintained copy of any fact, ever — a copy is either
> generated or a pointer"). Do not hand-edit files here.

| File | What | Writer | Source of truth |
|---|---|---|---|
| [`lanes.json`](lanes.json) | The fleet lane registry — lane name, repo, disposition, attribution tokens (central-docs-plan C3) | `scripts/gen_roster.py` (regenerated with every roster generation) | The `LANES` constant in `scripts/gen_roster.py` |
| [`kit-versions.md`](kit-versions.md) | Fleet kit-version table — repo → pinned → tree → drift verdict, incl. the plugin-pin drift check (central-docs-plan C4 / INC-42) | `scripts/gen_kit_versions.py` | Each repo's `substrate.config.json` + `.substrate/state.json` at verified HEADs (never heartbeat prose) |

Planned (plan §3, later phases): `pins.md` (C10, plugin + cross-repo
contract pins / manifest hashes).

Consumers: external repos (websites `app/roster.py` repoint — websites #102;
kit docs that previously derived lane sections from the superseded superbot
`docs/eap/fleet-manifest.md`) read `lanes.json` over
`raw.githubusercontent.com`. fm-internal tools import `gen_roster.LANES`
directly and need no repoint.
