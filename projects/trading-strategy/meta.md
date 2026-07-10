# trading-strategy — Project package meta

- **Lane state: PARKED GREEN — program COMPLETE.** The research mission is
  done: ORDER 007 (significance bar) and ORDER 008 (one-shot P5 holdout
  evaluation) both executed 2026-07-10; the holdout is **SPENT** (run stamps
  `2026-07-10T16:47Z`, all 13 ledger rows `holdout_unlocked=true`);
  `docs/final-report.md` is FINAL. Verdict: primary AAPL-donchian mechanical
  rule-pass (Sharpe 0.759 > B&H 0.740) but t = 0.02 → RULE-PASS candidate,
  NOT a finding; 2/12 secondaries HOLDOUT-BEAT (chance-level vs the
  pre-registered null); 0/13 clears significance. Sole open action: the
  OWNER MERGE CLICK on PR #37 (terminal classifier refusal — no agent
  retries it). Source: `control/status.md` @ origin/main `ffdd6f6`.
  **⚠ Delta vs the dispatch brief:** the brief described ORDER 008 as the
  pending queue head ("008-holdout"); live HEAD shows it DONE — the
  coordinator prompt encodes the dedicated-fresh-session rule as standing
  doctrine (with 008 as its executed precedent) rather than as a pending
  task.
- **Kit version: v1.7.0** (`substrate.config.json` @ `ffdd6f6`:
  `"kit_version": "1.7.0"`). **⚠ Delta vs the dispatch brief**, which said
  "v1.1.0 (oldest in fleet — upgrade rides next session)" — either the brief's
  inventory row was stale or a kit-upgrade PR landed between the inventory
  SHA (`0e713b9`) and build-time HEAD (`ffdd6f6`). Verify before scheduling
  any upgrade work.
- **Cadence:** recommended `0 */2 * * *` (core-seat stagger: lanes `0 */2`,
  manager `30 */2`; gen-3 standard §2). Deployed today: `0 */4 * * *` on
  `trig_01Mvn5xRmqGmZJNRHgjqyLpN` — stale on two axes (old-chat binding +
  old delegating prompt); F-1 re-arm-then-delete cutover specified in
  `failsafe-prompt.md`.
- **Environment archetype:** `pinned-research`
  (fleet-manager `environments/archetype-pinned-research.sh` @ `0eaa668`;
  "Serves: trading-strategy, websites"). TWO-SOURCE workspace —
  trading-strategy + substrate-kit as cwd children under /home/user (the
  exact layout that killed three gen-1 sessions at provision). Python 3.11
  floor; deps pinned in the repo's `requirements.txt` (pandas 3.0.3, numpy
  2.4.6, yfinance 1.5.1, requests 2.33.1, pytest 9.1.1). The package's
  `setup-script.sh` = the repo's fleet-synced `environments/
  setup-universal.sh` + archetype baseline + the fleet capability-probe
  block.
- **Grants:** write = `menno420/trading-strategy` only (Q-0260 single
  writable repo; substrate-kit is a read source in the env). **Env vars:
  NONE** — yfinance is keyless; git auth is platform-provided (archetype
  header + deployed §3). No secrets ever in repo or env.
- **Codex enabled: unknown (cheap check done).** GitHub issue/PR search for
  "codex" in menno420/trading-strategy = 0 results (2026-07-10) — no @codex
  comment has ever been posted, so the toggle has never been exercised;
  absence is not proof either way (search endpoint is issue-scoped). No
  Codex click appears in the lane's founding package §Owner-clicks.

## Deployed-state per part (2026-07-10)

| Part | This package file | Deployed today | Citation |
|---|---|---|---|
| 1 instructions | `instructions.md` — Q-0265/Q-0264/ORDER-007/holdout-spent re-base (paste block 6,288 chars, <7,000) | **Fitted gen-2 CI deployed 2026-07-10 (~02:05Z), 7,495 chars — PRE-Q-0265** (session shape absent, "holdout until final report phase" now stale, pre-ORDER-007/-008). **Re-paste needed.** Deployed text lives ONLY in fleet-manager (§"Deployed fitted version"); the lane repo carries just the pre-gen-2 proposal with its honesty caveat | fm `docs/proposals/instructions/trading-strategy.md` § Deployed @ `0eaa668`; trading `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md` @ `ffdd6f6` |
| 2 coordinator prompt | `coordinator-prompt.md` — continuous seat brief (stewardship mission, dedicated-session rule for holdout-class orders, pacemaker, parked-green backpressure) | De-facto deployed seat prompt = the ORDER-006 delegating one-liner into the OLD coordinator chat, 4-hourly — **OUTDATED vs Q-0265 on pacing AND binding** | trading `control/inbox.md` ORDER 006 + `control/status.md` ROUTINE STATE @ `ffdd6f6`; inventory-lanes §3 |
| 3 setup script | `setup-script.sh` — setup-universal.sh base + archetype baseline + probe block | Repo file `environments/setup-universal.sh` is fleet-synced and tested, but **whether the owner ever pasted it into the console is unverified from inside** (⚑ open, status item (b): "current pinned env works") | trading `environments/setup-universal.sh` + `control/status.md` ⚑(b) @ `ffdd6f6` |
| 4 failsafe text | `failsafe-prompt.md` — Q-0265 failsafe, `0 */2`, F-1 cutover | **NOT deployed.** Live trigger `trig_01Mvn5xRmqGmZJNRHgjqyLpN` = `0 */4 * * *`, bound to the old chat, prompt = the old delegating ritual — deployed-state stale on two axes | trading `control/status.md` ROUTINE STATE @ `ffdd6f6`; NEXT-BOOT § Coordinator-surface recipes |

## Sources

- trading-strategy @ `ffdd6f6` (origin/main, fetched this build):
  `control/status.md` · `control/inbox.md` (ORDERs 001–008) ·
  `docs/succession/NEXT-BOOT.md` (walls + coordinator recipes) ·
  `docs/succession/QUEUE.md` (program state, all items DONE) ·
  `docs/p5-holdout-protocol.md` (§6 one-shot-then-final, §7 owner-gated
  unlock + dedicated non-author session) ·
  `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md` ·
  `environments/setup-universal.sh` · `requirements.txt` ·
  `substrate.config.json` (kit 1.7.0).
- fleet-manager @ `0eaa668` (origin/main):
  `docs/proposals/instructions/trading-strategy.md` (§2 draft + §"Deployed
  fitted version" — the re-base source) ·
  `environments/archetype-pinned-research.sh` (archetype row/serves).
- Doctrine (as relayed by the dispatch + mirrored in sibling packages):
  Q-0265 continuous mode · Q-0264 sim-worthy escalation · Q-0262 policy 1
  (family-level model names un-null the Model rows) · Q-0263.2
  (never route derivables) · Q-0089 honesty guard · gen-3 deployment
  standard §2 (superbot `docs/planning/gen3-deployment-standard-2026-07-10.md`) ·
  part-4 brief §2b failsafe template.
- Inventories (scratchpad `launch-packages/`): inventory-lanes.md §3 +
  missing-parts matrix; inventory-hub.md §A row 2, §C, §D.

**Last verified:** 2026-07-10 — both repos fetched at the SHAs above during
this build. Model: Fable family (package builder). Scratchpad-only per
dispatch — nothing committed or pushed by this builder; the assembler
commits.
