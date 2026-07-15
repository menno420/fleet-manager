# Session — 2026-07-15 — curious-research disposition + reboot sweep + heartbeat

> **Status:** `in-progress`

Intent: record the owner's live curious-research PARKED verdict in docs/fleet-triage.md, take a first read-only v3.6 reboot sweep across the roster seats, and refresh control/status.md heartbeat.

## Reboot sweep — first pass (measured 2026-07-15T04:01–04:03Z, `date -u`)

Method: read-only — `control/status.md` at HEAD via raw.githubusercontent.com
for every public seat repo; pokemon-mod-lab (private) via GitHub MCP
`get_file_contents`. Cutoff for "rebooted" = heartbeat `updated:` stamp
AFTER 2026-07-15T03:45Z (when the owner began firing v3.6 reboot prompts).

| Seat repo | Heartbeat `updated:` | Post-03:45Z (rebooted)? |
|---|---|---|
| superbot (hub) | 2026-07-13T18:00:00Z | not yet |
| superbot-next | 2026-07-14T21:28:31Z | not yet |
| substrate-kit | 2026-07-14T21:03Z | not yet |
| websites | 2026-07-14T21:12:44Z | not yet |
| trading-strategy | 2026-07-14T21:17:36Z | not yet |
| venture-lab | 2026-07-14T23:53:28Z | not yet |
| superbot-games | 2026-07-14T11:41:04Z | not yet |
| superbot-idle | 2026-07-14T11:32:05Z | not yet |
| superbot-mineverse | 2026-07-14T18:59:20Z | not yet |
| gba-homebrew | 2026-07-14T21:16:02Z | not yet |
| product-forge | 2026-07-11T19:39:50Z | not yet |
| idea-engine | 2026-07-14T23:42:25Z | not yet |
| sim-lab | 2026-07-14T21:14:50Z | not yet |
| pokemon-mod-lab (private, MCP) | 2026-07-14T05:07:37Z | not yet |
| codetool-lab-fable5 | 2026-07-09T20:06Z | not yet (archived — no reboot expected) |
| codetool-lab-opus4.8 | 2026-07-09T20:11:35Z | not yet (archived — no reboot expected) |
| codetool-lab-sonnet5 | 2026-07-09T20:02:14Z | not yet (archived — no reboot expected) |
| fleet-manager (this repo) | 2026-07-15T03:40:49Z (pre-sweep base; refreshed to 04:04:23Z in this PR) | coordinator LIVE (revival stamp pre-dates the 03:45Z cutoff by ~4 min) |

Result: **0/17 seat-repo heartbeats post-03:45Z** at first measurement —
fully expected ~18 min into the reboot wave (a rebooted seat only stamps at
its session close). Neutral finding, no alarms; next sweep should start
seeing post-cutoff stamps. Registry-only seats (game-lab, SuperBot World,
Ideas Lab, Self Improvement, SuperBot 2.0, Curious Research, retro-games)
have no repo heartbeat to measure. curious-research: PARKED by owner
decision — excluded from reboot expectations entirely.
