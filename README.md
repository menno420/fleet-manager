# fleet-manager — the estate router and records home

fleet-manager is the owner's **router and records home**. It helps a fresh
session find the right repository, learn where the last session left off, and
locate the estate-wide records that genuinely belong here. Product truth stays
in each product repository; this repo points to it instead of copying it.

Canonical purpose and boundaries: [`docs/intent.md`](docs/intent.md).
The full map of everything here, one line per area: [`docs/MAP.md`](docs/MAP.md).

## The story in 60 seconds — why this repo exists

The owner runs a personal estate of ~20 repositories (games, a Discord bot,
websites, tooling), built up since **2025-08** — that pre-history is most of the
estate's life. In **July 2026** (07-07 → 07-21) it ran at full intensity as an
**autonomous-Projects program** on Claude Code's **Early Access Program (EAP)**:
parallel Claude "seats", each owning a repo, coordinated from here — which is why
this repo is full of rosters, prompts, ORDERs and telemetry. The EAP concluded
and **the program closed on 2026-07-21**. The seats no longer exist. One owner task survives from that era: **E1**, his own final EAP review
email — owner-reserved, no session touches it.

Since then everything runs in **regular owner-directed sessions, one finished
thing at a time**, working the [consolidation program](docs/planning/2026-07-26-consolidation-program.md).
What he is working on and why: **methods and enforcement before high-value
product work** (OD-13 — make sessions reliable first, via the
[agent-operating-environment roadmap](docs/planning/2026-08-08-agent-operating-environment-roadmap.md)),
with **spider-swing and the superbot repos as the important products** (OD-15).
Most of what you can see here is therefore **memory, not instruction** — the
[map](docs/MAP.md) marks every area CORE, TASK or RECORD so you always know
which you are holding.

## Mandatory reading order — six reads, then you understand the bigger picture

Read these in order on every cold start. Each line says what the read gives
you, so skipping is a decision rather than an accident. A fresh session should
**not** read everything — after these six you know the picture and the
[map](docs/MAP.md) routes everything else.

1. **This README** — purpose, the story, this list, the map.
2. **[`docs/intent.md`](docs/intent.md)** — *why the repo exists*: what
   "working" means to the owner, the non-goals, who does what across
   Claude / ChatGPT / Gemini / Grok / Codex. His words, labelled.
3. **[`docs/current-state.md`](docs/current-state.md)** — *what is true now*:
   live state, work state, what shipped recently.
4. **[The consolidation program](docs/planning/2026-07-26-consolidation-program.md)**
   — *the goals and the plan*: the owner-directive table (OD-1…OD-15), the step
   tracks, the NOW pointer and its standing corrections. It is a `living-ledger`
   and **the** plan — OD-13/14/15 are dated 2026-08-08/10 and the actionable work
   derives from its NOW pointer. **Read it together with
   [the agent-operating-environment roadmap](docs/planning/2026-08-08-agent-operating-environment-roadmap.md)**:
   the roadmap is the methods-and-enforcement subplan that `OD-13` prioritises
   *ahead of* the lettered product steps — not a replacement for the program. A
   session that reads only the program learns the steps but not that OD-13 puts
   the roadmap's phases first.
5. **[`docs/fleet-account-2026-07-26.md`](docs/fleet-account-2026-07-26.md)** —
   *how it came to existence*: the EAP story from 2025-08 to the close,
   owner-reviewed. Read once; do not re-derive the history.
6. **[`docs/owner-reflection-2026-07-21.md`](docs/owner-reflection-2026-07-21.md)**
   — *how the owner thinks*: verification over capability, decide rather than
   default to asking.

After those reads, a session must be able to state without guessing: what this
repo is for, what era it is in, what the owner is working on and why, and what
the next actionable step is. If it cannot, the front door is defective — record
the missing fact rather than compensating by searching harder.

Claude Code also auto-loads [`.claude/CLAUDE.md`](.claude/CLAUDE.md) (hooks,
skills, capabilities, the deeper task-routed path). Other surfaces may not load
anything — this README is deliberately surface-neutral.

## Live map (TASK tier — read when the task touches them)

| Need | Canonical place |
|---|---|
| Everything, one line per area | [`docs/MAP.md`](docs/MAP.md) |
| Why this repo exists and how to decide | [`docs/intent.md`](docs/intent.md) |
| Live hub state | [`docs/current-state.md`](docs/current-state.md) |
| Program progress and next action | [Consolidation program](docs/planning/2026-07-26-consolidation-program.md) |
| Owner-only decisions and manual actions | [`docs/owner-queue.md`](docs/owner-queue.md) |
| **Which repo owns a request** — every repository, one line each | [`docs/ESTATE.md`](docs/ESTATE.md) |
| **What every session did, wherever it ran** (local + cloud) | [`docs/activity/`](docs/activity/README.md) |
| Per-repo entry points and handoffs | [`docs/repos/`](docs/repos/README.md) |
| Verified capabilities and route facts | [`docs/CAPABILITIES.md`](docs/CAPABILITIES.md) |
| Decisions ledger | [`docs/decisions.md`](docs/decisions.md) |
| What is wrong with this repo (edit-pass worklist) | [the full-read audit](docs/audits/2026-08-10-full-read/README.md) |
| Session landing procedure | [`.claude/skills/session-close/SKILL.md`](.claude/skills/session-close/SKILL.md) |

## Historical map (RECORD tier)

The autonomous program's apparatus is preserved, era-bannered, and never a live
channel: [`docs/PROJECT-CLOSEOUT.md`](docs/PROJECT-CLOSEOUT.md) (the hub
closeout) · [`docs/roster.md`](docs/roster.md) · [`control/`](control/README.md) ·
[`telemetry/`](telemetry/README.md) · [`projects/`](projects/README.md) ·
[`docs/prompts/`](docs/prompts/README.md) *(mixed — three live exceptions:
[the Fleet Manager ChatGPT instructions](docs/prompts/chatgpt-project-instructions.md),
[the Couch Legend ChatGPT instructions](docs/prompts/chatgpt-couch-legend-project-instructions.md)
and [the curious-research review prompt](docs/prompts/2026-08-07-curious-research-external-review.md))*.
Never use the historical parts to answer "what is
happening now?" — the [map](docs/MAP.md) lists every RECORD area.

The current files above always win over a dated snapshot. Source and merged
repository state win over every document.
