# EAP audit collection — fleet fan-out tracker (2026-07-14)

> **Status:** `living-ledger` — AUDIT-WATCH tracking instrument
>
> Tracking instrument for today's EAP PROJECT AUDIT fan-out: each Project
> lands `docs/audits/eap-project-audit-2026-07-14.md` in its repo(s); later
> sweeps update the table below as audits arrive at each repo's HEAD.
> Synthesis + the final-email draft fires once the **majority** of audits
> are in. Seeded at wake 0845Z from the 2026-07-14T08:34–08:38Z read-only
> scan (all probes via GitHub MCP `get_file_contents` at HEAD + open-PR
> sweeps; citations per row).

## Collection table

Snapshot verdict at seed time: **0 / 13 target repos have the audit doc at
HEAD** (all 13 probed 08:34Z). In flight born-red (open PR, doc not yet on
the PR head at ~08:37Z): **websites #332 · substrate-kit #366 ·
venture-lab #192**. The remaining **10** targets had not started as of
08:38Z. fleet-manager (this repo) landed its own audit before the scan.

| Repo (menno420/) | Audit doc at HEAD? | Landed PR # | Headline numbers | Top ANTHROPIC asks |
|---|---|---|---|---|
| superbot | no (checked 08:34Z) | — | — | — |
| superbot-next | no (checked 08:34Z) | — | — | — |
| substrate-kit | no (checked 08:34Z) — in flight: PR #366 open (created 08:35:28Z; doc not on PR head at 08:37Z) | — | — | — |
| websites | no (checked 08:34Z) — in flight: PR #332 open (created 08:34:39Z, branch `claude/eap-audit-0714`, intentionally born-red; doc not on PR head at 08:37Z) | — | — | — |
| venture-lab | no (checked 08:34Z) — in flight: PR #192 open (created 08:35:21Z; doc not on PR head at 08:37Z) | — | — | — |
| idea-engine | no (checked 08:34Z) | — | — | — |
| sim-lab | no (checked 08:34Z) | — | — | — |
| trading-strategy | no (checked 08:34Z) | — | — | — |
| superbot-idle | no (checked 08:34Z) | — | — | — |
| superbot-games | no (checked 08:34Z) | — | — | — |
| superbot-mineverse | no (checked 08:34Z) | — | — | — |
| pokemon-mod-lab | no (checked 08:34Z) | — | — | — |
| gba-homebrew | no (checked 08:34Z) | — | — | — |
| **fleet-manager** | **YES — DONE** ([`docs/audits/eap-project-audit-2026-07-14.md`](audits/eap-project-audit-2026-07-14.md) at HEAD) | **#189** (merged 2026-07-14T08:23:47Z) | 204 commits on main · 190 PRs (187 merged) in ≈4.6 days · 138 session cards · ≈41 PRs/day (highest-cadence seat) | (1) owner-delegable merge grant + inspectable classifier verdicts (§9.1); (2) trigger/session lifecycle events + tombstones (§9.2); (3) queued cross-session delivery / wake-a-sibling (§9.3); (4) per-session cost/token visibility (§9.4); (5) GitHub read surfaces (settings/rulesets) + `claude/*` branch-delete + fresher PR-state (§9.5) |

**Footnote:** curious-research PR #42 ("EAP project audit — Curious
Research seat", created 08:33:56Z, born-red) is also open with an audit —
outside the 13-target list, tracked here for completeness.

## Update protocol

- Each later sweep re-probes `docs/audits/eap-project-audit-2026-07-14.md`
  at every target repo's HEAD, fills the row (checked-at time, landed PR #,
  2–4 headline numbers, top ANTHROPIC asks quoted from the doc's own
  ranked section), and re-states the running tally.
- When the tally crosses **7 / 13** (majority), the sweep that observes it
  starts the synthesis + final-email draft.
- Absence-on-head during a born-red window is expected, not a failure
  signal — a PR opens minutes before its doc content is pushed.
