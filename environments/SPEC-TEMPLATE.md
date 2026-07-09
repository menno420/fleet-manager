# Environment spec — `<env-name>` (PROPOSED)

> **Status:** `plan` — proposed spec; becomes `living-ledger` once the owner has
> created the env and an in-env session has verified it. **Names + placeholders
> only — NEVER secret values** (`environments/README.md` hard rule).
>
> Copy this file to `environments/<env-name>.md` when proposing a new Project's
> environment; fill every field; delete the guidance italics.

## Identity

- **Name:** `<env-name>` *(short, lane-named — e.g. `trading-strategy`)*
- **Proposed by / date:** `<agent · YYYY-MM-DD>`
- **For Project(s):** `<which claude.ai Project(s) will select this env>`
- **Verified:** `pending owner creation` *(flip to a date after in-env check)*

## Repos

*(every repo the env checks out; one line each: repo — why it's needed)*

- `menno420/<repo>` — `<why>`

## Setup script

Use the canonical shim: [`templates/setup-universal.sh`](templates/setup-universal.sh)
*(link, don't fork — if the lane needs more, ship a `scripts/env-setup.sh` in the
repo instead; the shim prefers it automatically and the repo owns its own setup).*

## Environment variables (NAMES only)

*(smallest set that unblocks the lane — see [`templates/env-vars.md`](templates/env-vars.md);
⚠️ the Railway trio / prod DSN / prod bot token are superbot-lane ONLY)*

| Name | Why this lane needs it | Value |
|---|---|---|
| `<VAR_NAME>` | `<one line>` | `<SET-IN-CLAUDE-AI>` |

## Model

- **Model:** `<default | sonnet | opus | haiku — and why, one line>`

## Scopes / permissions

- **GitHub:** `<which repos the Project's GitHub access must cover>`
- **Other:** `<anything else — MCP servers, network needs — or "none">`

## Owner paste-steps (click path)

1. Open **claude.ai/code → Environments → New environment** (or edit an existing one).
2. **Name** it `<env-name>`.
3. **Add repos:** `<list again, exactly as above>`.
4. **Setup script:** paste the full contents of `templates/setup-universal.sh`.
5. **Environment variables:** add each NAME from the table above with its real
   value (values exist only here — never in the repo).
6. **Save**, then in the target **Project → settings → Environment** select
   `<env-name>`.
7. Reply/ack; the proposing lane will run one session in it and flip
   **Verified** above.
