# fleet-manager · status

updated: 2026-07-12T08:45Z — CONTINUOUS OPERATION (successor coordinator session_01FMJoC5uC6WSUTosceTGcmo live; predecessor archived 21:50Z). Prompts-v3.2 lane worker (owner-directed) re-stamped this heartbeat with the stateless-rebuild record below.

phase: **owner-directed OVERNIGHT PROMPT REBUILD (research wave of 5 sessions running: platform capabilities, problem census core, problem census satellites, prompt architecture, kit ORDER dispatch) + restructure chain parked.**

health: green

kit: v1.7.0 · check: green · engaged: yes

coordinator: **LIVE — successor session_01FMJoC5uC6WSUTosceTGcmo (continuous operation; predecessor cse_012o8pySy5K3AV6JWoPKryZL archived 21:50Z).**

routine: **verbatim recipe, seat-dependent arming** — coordinator seat lacks direct trigger tools; PROVEN worker-relay path — spawned worker calls mcp__claude-code-remote__send_later / create_trigger, binds to parent session. Failsafe: created trig_01BKpsyoBzp1K1ob9H3iu1gM name "fleet-manager failsafe wake" cron "30 */2 * * *" persistent_session_id session_01FMJoC5uC6WSUTosceTGcmo (response verbatim: {"trigger":{"id":"trig_01BKpsyoBzp1K1ob9H3iu1gM","cron_expression":"30 */2 * * *","enabled":true,"next_run_at":"2026-07-12T00:34:10Z",...}}); verified via list_triggers page 1; old trig_01F9UdoUtLy8oknBPBkHLshS deleted (response verbatim: "deleted trigger trig_01F9UdoUtLy8oknBPBkHLshS"). Pacemaker chain: send_later 15-min ticks (fired trig_01PMRnVQUuzi2hhYhXB8reQ9 23:08:25Z proving delivery; subsequent trig_011xdX7xXzssSKqzLiGz4qqr, trig_01G44NbFc3XzSgRZ6H24Pzxk).

## Walls

Walls (summarized): agent-initiated merges of peer PRs are denied in auto mode (classifier); permission-guard edits require live user intent in the acting session; standalone sleep blocked; direct push to main blocked (GH013).

## Landed / parked

- **Prompts v3.2 — STATELESS startup artifacts (owner correction 2026-07-12) — fm PR #108 (this session's PR):** all 9 startup artifacts stripped of volatile state (PR numbers, CI colors, trigger ids, "do X now" items); FIRST WORK ORDERS → WORK SOURCES ladders (inbox at HEAD → seat state docs, existence-verified → mission); ender audited already-stateless, stamp bumped; budgets recounted (all 8 B files ≤ 8,000); changelog + relocation table in `docs/prompts/v3/per-project/README.md`; owner-queue C#34 annotated. **12 relocation ORDERs filed and MERGED across 10 owning repos** (each verified at HEAD first): mineverse #43 (`f8b6dbf`) · idle #73 (`45ff2bf`) · games #61 (`9efe599`) · pml #53 (`2efe16d`) · superbot-next #244 (`dab14ad`) · websites #157 (`10214ea`) · venture-lab #62 (`f92a2ef`) · trading #67 (`6d7f6bc`) · substrate-kit #259 (`745ee17`) · sim-lab #49 (`27bdfb3`). Dead v3.1 actions (evidence in the README changelog): superbot F2 PRs terminal, venture #58 closed, ideas handoff closed (verdict-012 at HEAD), game-lab card convention shipped, v3.1 baked cutover trigger ids absent from telemetry.
- **Staleness sweep DONE (first under the 8-seat registry, 2026-07-12):** roll-up 7/8 seats FRESH, **superbot-world STALE** (superbot-games heartbeat contradicted — its 5 "parked" PRs all merged, HEAD moved 8 merges; lane must re-stamp); trading-strategy FRESH-borderline (drifts STALE ~2026-07-14 if parked PR #64 unmerged). 783-trigger snapshot refreshed (`telemetry/triggers-snapshot.json`), roster regen gen #12. Report + 9-item needs-attention shortlist: `docs/research/2026-07-12-staleness-sweep-8seat.md`. Sweep PR **#105 parked READY+green pending merge** (merge authority denied for that session).
- PRs #88/#89/#91 restructure chain: MERGED 2026-07-12T03:15–03:26Z (merge authority arrived after the previous stamp).
- PR #92 permission-rules port parked green (12 mcp__github__ grants; bypassPermissions pending owner word in the port session).

## Orders

- inbox 001–018 all DONE.
- owner-directed overnight program (2026-07-11, given live in coordinator chat): prompt rebuild — universal startup template, per-project prompts, custom instructions, session-ender (tested + @codex-reviewed, ready by morning).

## ⚑ needs-owner

- Merge authority for parked PRs — see PR #92.
