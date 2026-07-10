# fleet-manager · status
updated: 2026-07-10T06:30:00Z
phase: GEN-2 FLEET LIVE — morning consolidation after the overnight launch (2026-07-10 00:00–06:15Z: **116 PRs merged fleet-wide, zero stuck** — verified via the merged-PR search, not reports; full record: docs/planning/gen2-launch-record-2026-07-10.md)
health: green
kit: v1.4.0 · check: green · engaged: yes
last-shipped: #18 — morning consolidation (this status rewrite, owner-queue refresh, deployed fitted instructions, launch record, gba-play idea, capability walls)
blockers: none

## Lanes (current, one line each — verified at HEAD 2026-07-10 morning)

- **venture-lab** (gen-2 pilot, live) — 9 PRs landed; 2 sellable products with buyer zips ON MAIN (#9 merged 05:11:50Z: membership-kit v0.2 + template-packs v0.1 + $59 bundle listing); revenue is owner-gated on ⚑A–D (owner-queue item 2). Lane status file predates the #9 merge — the zips are landed, not waiting.
- **game-lab Track A / pokemon-mod-lab** (gen-2, live, PRIVATE) — ORDER 001 done (#2/#3: retail-match build + dialogue mod + headless proof); QoL+ increments 1–4 shipped (#4–#7). Owner: playtest pass + concept pick (owner-queue items 3–4).
- **game-lab Track B / gba-homebrew** (gen-2, live, public) — ORDER 001 done (#3 skeleton); Lumen Drift scope-complete through increment 3 + polish pass 1 (title screen, SRAM); session 6 polish pass 2 WIP at morning read. Owner: concept pick (owner-queue item 4).
- **substrate-kit / kit-lab gen-2** (live) — overnight run: 12 build PRs (#84–#108 band), 814 tests green, night-cap #109/#110 reconciled. **Queue DRY**; the HOT owner item is the F-5 one-letter ruling (owner-queue item 1); P10 check swap + P4 daily loop queued.
- **trading-strategy gen-2** (live) — P1 (3 lanes, 590 configs) → P2 validation (14 verdicts, **1 promoted candidate: AAPL-donchian 15/5 daily**) → P3/P4 hardening + transfer (13/13 TRANSFER-FAILED, honestly ledgered) → P5 prep done (#30, pre-registered holdout protocol). Holdout SEALED, unlock owner-gated (owner-queue item 6).
- **websites gen-2** (live) — ORDER 005 (the gen-1 trap) + ORDER 007 DONE (#50–#54): /queue + /environments shipped, skeleton proven.
- **superbot** (overnight shift) — #1915–#1925 landed (manifest un-drift, collision guard, claim visibility, dashboard feed, recon pass); #1926 OPEN (two one-line eap corrections from the ultracode verification — the only open PR fleet-wide this morning).
- **superbot-next** — stays gen-1 MID-MISSION (band 5 live-testing); overnight #98/#99 only (heartbeat + ideas seed). Grants still queued (parked).
- **codetool arms ×3** — Projects → CLOSE; repos stay (disposition, launch record §2).
- **games mining + exploration** — merged into ONE games-plugins gen-2 lane; **UNBLOCKED** by superbot-games #5 (the 18-module port, merged 00:00:58Z).
- **mobile-lab · 6-repo harness experiment** — ready-not-launched (packages/prompts committed, paste-ready; experiment repos verified NOT created).

## In-flight (don't drop)

- superbot PR #1926 (corrections) — open, READY; lands on green.
- gba-homebrew session 6 (Lumen Drift polish pass 2) — WIP at morning read.
- Owner morning click-list: **docs/owner-queue.md** (8 active items, HOT first).
- EAP free window through 2026-07-14; Anthropic follow-up draft rides the email pack (parked queue).
- PLATFORM GAP (recorded in capabilities.md): routine/trigger creation walled on BOTH sides — lanes run self-terminal; interim wake = a morning "continue" per Project.

orders: acked= done= (no inbox orders for the manager repo)
⚑ needs-owner: see docs/owner-queue.md (8 active + parked)
notes: launch record + dispositions + verified overnight numbers: docs/planning/gen2-launch-record-2026-07-10.md. Fitted (≤7,500-char) Custom Instructions actually deployed to the websites + trading gen-2 Projects are recorded in docs/proposals/instructions/{websites,trading-strategy}.md § "Deployed fitted version".
