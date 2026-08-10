# fleet-manager — the estate router and records home

fleet-manager is the owner’s **router and records home**. It helps a fresh
session find the right repository, learn where the last session left off, and
locate the estate-wide records that genuinely belong here. Product truth stays
in each product repository; this repo points to it instead of copying it.

Canonical purpose and boundaries: [`docs/intent.md`](docs/intent.md).

## Cold orientation — three files, then state the answer

Read these in order:

1. **This README** — purpose, boundary, and the live-versus-historical map.
2. **[`docs/current-state.md`](docs/current-state.md)** — what is true in the
   hub now.
3. **[The consolidation program](docs/planning/2026-07-26-consolidation-program.md)**
   — the authoritative NOW pointer and the next repository in the active step.

After those reads, a cold session must be able to state, without guessing:

- what fleet-manager is for;
- what operating era and work state it is in;
- what the next actionable step is.

If it cannot, the front door is defective. Do not compensate by searching more
files and calling the orientation successful; record the missing fact or
contradiction.

Claude Code also auto-loads [`.claude/CLAUDE.md`](.claude/CLAUDE.md). Other
surfaces may not. The three-file route above is deliberately surface-neutral.

## Live map

| Need | Canonical place |
|---|---|
| Why this repo exists and how to decide | [`docs/intent.md`](docs/intent.md) |
| Live hub state | [`docs/current-state.md`](docs/current-state.md) |
| Program progress and next action | [Consolidation program](docs/planning/2026-07-26-consolidation-program.md) |
| Owner-only decisions and manual actions | [`docs/owner-queue.md`](docs/owner-queue.md) |
| Per-repo entry points and handoffs | [`docs/repos/`](docs/repos/README.md) |
| Verified capabilities and route facts | [`docs/CAPABILITIES.md`](docs/CAPABILITIES.md) |
| Session landing procedure | [`.claude/skills/session-close/SKILL.md`](.claude/skills/session-close/SKILL.md) |

## Historical map

The autonomous Projects program closed in July 2026. Its generated roster,
`control/` bus, committed trigger telemetry, project packages, and prompt
registry are records of that era, not current state.

- [`docs/PROJECT-CLOSEOUT.md`](docs/PROJECT-CLOSEOUT.md) is the historical hub
  closeout and preserves the state and continuation advice known at closure.
- [`docs/fleet-account-2026-07-26.md`](docs/fleet-account-2026-07-26.md) is the
  owner-reviewed account of what the program produced.
- [`docs/roster.md`](docs/roster.md), [`control/`](control/README.md),
  [`telemetry/`](telemetry/README.md), and [`projects/`](projects/README.md) are
  explicitly historical. Never use them to answer “what is happening now?”

The current files above always win over a dated snapshot. Source and merged
repository state win over every document.
