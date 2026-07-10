# fleet-manager · status
updated: 2026-07-10T16:02:00Z
phase: GEN-2 FLEET LIVE — standing-wake cadence RUNNING (14:36Z pass closed below; overnight launch 00:00–06:15Z: **116 PRs merged fleet-wide, zero stuck** — full record: docs/planning/gen2-launch-record-2026-07-10.md) · launch-readiness pass CLOSED (owner dispatch, section below)
health: green
kit: v1.4.0 · check: green · engaged: yes
coordinator: **LIVE** — session-based coordinator seat booted 2026-07-10 (round-3 pack §1 brief)
routine: fleet-manager 2-hourly standing wake · cron 30 */2 * * * · armed-by-me (id `trig_01QBrp5MjZL3F9mv6KsTXTzN`) — **FIRED ON SCHEDULE 2026-07-10T14:36Z, recurring confirmed by the firing itself**; next run due 2026-07-10T~16:31Z

> **Arming record (verbatim, 2026-07-10T13:40Z — reproducible recipe, first-class):**
> Tool: claude-code-remote `create_trigger` (MCP; verified after with `list_triggers`).
> Args: `name="fleet-manager 2-hourly standing wake"`, `cron_expression="30 */2 * * *"`,
> `persistent_session_id="cse_01V66KdPhtbR1AThhK77kDqr"` (the coordinator session),
> `prompt=` the standing 2-HOURLY WAKE text (stored verbatim in the trigger).
> Result: `{"trigger":{"id":"trig_01QBrp5MjZL3F9mv6KsTXTzN","name":"fleet-manager 2-hourly standing wake","cron_expression":"30 */2 * * *","enabled":true,"next_run_at":"2026-07-10T14:36:04Z", … "persistent_session_id":"session_01V66KdPhtbR1AThhK77kDqr"}}`
> — no error; the passed `cse_…` id was accepted and normalized to `session_…` form;
> recurring cron (not one-shot) confirmed in the `list_triggers` output — **and now by the
> 14:36Z firing itself (see wake record below).**

last-shipped: #30 — launch-readiness checklist (Q-0261 finalize-first, 13 seats, owner-queue synced)
blockers: none

## Launch-readiness pass — 2026-07-10 (owner dispatch)

Owner-dispatched pass, now CLOSED. Deliverable: **`docs/launch-readiness-2026-07-10.md`**
(merged PR #30, squash 7af63f8) — the Q-0261 finalize-first checklist across all 13 seats,
owner-queue synced. Totals for the record:

- **38 OWNER-CLICK** items, of which **5 boot-gating**: kit OA8, Idea Engine Project,
  product-forge repo + Project + check.
- **11 DECISION** items.
- **47 AGENT-DOABLE** items, of which **2 boot-gating agent items**: superbot-next
  ORDER 008, superbot-games ORDER 001 (CI-collection).
- **Round-opening prerequisite:** merge superbot **PR #1948** (Q-0261 material is
  branch-only at 9b35fc46 until it lands).

### Routing outcomes (this pass)

- **superbot-next ORDER 010** (@codex rule, Q-0259 r3) — landed PR #103, squash b63b933.
- **superbot-games ORDER 002** (self-arm wake) — landed PR #21, squash adb5f9b.
- **trading holdout-unlock relay** — **MOOT**: the owner dispatch session already landed it
  as trading ORDER 008 @ fd5e9fe (Q-0262.2).
- **websites OA12 relay** — **MOOT**: websites done=001–008 at d493792 — kit OA12 is
  retirable by its fresh seat.
- ⚠️ The owner-attended dispatch session is landing Q-0262 ORDERs **in parallel**
  (trading 008, superbot-next 009, kit 011 ~15:33Z) — **always re-derive inbox numbers
  at HEAD** before routing.

### Finding — Codex GitHub integration (feeds ORDER 007)

Confirmed **LIVE on superbot-next**: the `chatgpt-codex-connector` bot auto-reviewed
PR #103 (clean). **NOT enabled on fleet-manager** — the bot asked for environment
creation on PR #26. Relevant to ORDER 007 (@codex review-relay rule).

## Wake record — 2026-07-10T14:36Z (first standing-wake pass)

Routine `trig_01QBrp5MjZL3F9mv6KsTXTzN` fired on schedule — the arming record above is
a **verified recurring** recipe, not just a one-shot proof. What that pass did (compressed;
full close-out on PR #28):

- **Fleet-wide session-ender sweep** — 13 repos, verified against git (verdicts below).
- **ORDER 004 executed** — fleet economics ledger @ `docs/findings/fleet-economics-2026-07.md`
  (PR #27, squash 070f8e6). Headline: fleet window 07-08→07-10 = **566 merged PRs /
  937 commits / 230 session cards / 19,892 all-time Actions runs**, superbot ≈92% of runs;
  CI minutes + tokens not measurable (honest nulls).
- **venture-lab archive-ender ORDER routed** (the ENDER-MISSING fix) — venture-lab PR #12,
  squash af11bdb.
- **Stray PR #25 verified + merged** (ab63610) — pokemon-mod-lab **PRIVATE flip confirmed
  via API**; the owner-queue 🚨 URGENT item is retired.

### Ender-sweep verdicts (one line each)

- **ENDER-VERIFIED:** trading-strategy (#34 13:49Z) · websites (#58 13:57Z) · substrate-kit (#125 14:19Z) · superbot-games (#19/#20 13:49–13:53Z)
- **CLEAN-MORNING-ENDER** (terminal, pre-request): pokemon-mod-lab (b5b8ed6 07:50Z) · gba-homebrew (6e18b24 07:18Z)
- **ENDER-MISSING:** venture-lab (heartbeat stale 04:57Z; boot ORDER routed — PR #12 above) · superbot-next (status 01:05Z mid-mission band-5, no close-out)
- **PARTIAL:** superbot (close-out #1949 landed; PR #1948 open = owner-attended live dispatch session, not a stuck PR — now the Q-0261 round-opening prerequisite, see launch-readiness section)
- **N/A-CLOSED:** codetool ×3 (wind-down 07-09; fable5 a6cf1a9 12:07Z was the expected ORDER-006 succession fix)
- Owner informed: **10/13 archive-ready.**

Next wake due **~2026-07-10T16:31Z** · planned slice: advance **ORDER 002** (manifest
re-stamp — most-wrong rows venture-lab + trading-lab) **+ verify the websites 16:00Z
first-fire happened**.

## Lanes (current, one line each — verified at the 14:36Z wake pass; launch-readiness deltas folded in)

- **venture-lab** (gen-2 pilot, live) — 9 PRs landed; 2 sellable products with buyer zips ON MAIN (#9 merged 05:11:50Z: membership-kit v0.2 + template-packs v0.1 + $59 bundle listing); revenue is owner-gated on ⚑A–D (owner-queue item 2). **⚑B/⚑D publish clicks FROZEN 2026-07-10 (night-review D1: headline Stripe path never executed, near-certain live failure) — unfreeze rides the P0 fix ORDER (dispatched) landing with a real-path test.** Heartbeat was stale (04:57Z) at the wake sweep — archive-ender boot ORDER routed (venture-lab PR #12, af11bdb).
- **game-lab Track A / pokemon-mod-lab** (gen-2, live, **PRIVATE — flip confirmed via API at the 14:36Z pass; the 🚨 URGENT owner-queue item is retired**) — ORDER 001 done (#2/#3: retail-match build + dialogue mod + headless proof); QoL+ increments 1–4 shipped (#4–#7); clean morning ender b5b8ed6 07:50Z. Owner: playtest pass + concept pick (owner-queue items 3–4).
- **game-lab Track B / gba-homebrew** (gen-2, live, public) — ORDER 001 done (#3 skeleton); Lumen Drift scope-complete through increment 3 + polish passes; clean morning ender 6e18b24 07:18Z (terminal). Owner: concept pick (owner-queue item 4).
- **substrate-kit / kit-lab gen-2** (live) — overnight run: 12 build PRs (#84–#108 band), 814 tests green, night-cap #109/#110 reconciled; ender verified (#125 14:19Z). **Queue DRY**; the HOT owner item is the F-5 one-letter ruling (owner-queue item 1); P10 check swap + P4 daily loop queued; kit OA8 is a boot-gating OWNER-CLICK (launch-readiness); OA12 retirable (websites relay MOOT, see routing outcomes); kit ORDER 011 landing in parallel from the owner session (~15:33Z).
- **trading-strategy gen-2** (live) — P1 (3 lanes, 590 configs) → P2 validation (14 verdicts, **1 promoted candidate: AAPL-donchian 15/5 daily**) → P3/P4 hardening + transfer (13/13 TRANSFER-FAILED, honestly ledgered) → P5 prep done (#30, pre-registered holdout protocol); ender verified (#34 13:49Z). Holdout unlock: **landed as trading ORDER 008 @ fd5e9fe by the owner session (Q-0262.2)** — the coordinator relay was MOOT.
- **websites gen-2** (live) — ORDER 005 (the gen-1 trap) + ORDER 007 DONE (#50–#54): /queue + /environments shipped, skeleton proven; ender verified (#58 13:57Z); done=001–008 at d493792. Verify the 16:00Z routine first-fire at next wake.
- **superbot** — #1915–#1926 landed (manifest un-drift, collision guard, claim visibility, dashboard feed, recon pass; **#1926 corrections MERGED 06:33Z**); close-out #1949 landed; PR #1948 open = owner-attended live dispatch session **and the Q-0261 round-opening prerequisite** (material branch-only at 9b35fc46 until merged).
- **superbot-next** — stays gen-1 MID-MISSION (band 5 live-testing); overnight #98/#99 only (heartbeat + ideas seed); status 01:05Z, no close-out (ender-missing — watch). **ORDER 010 (@codex rule) landed PR #103 squash b63b933 this pass**; ORDER 009 landing in parallel from the owner session; ORDER 008 is a boot-gating agent item (launch-readiness). Grants still queued (parked).
- **codetool arms ×3** — Projects → CLOSE; repos stay (disposition, launch record §2); fable5 a6cf1a9 12:07Z was the expected ORDER-006 succession fix, nothing new owed.
- **superbot-games / games-plugins gen-2 lane** — the 18-module port merged (#5, 00:00:58Z); enders verified (#19/#20 13:49–13:53Z); **ORDER 002 (self-arm wake) landed PR #21 squash adb5f9b this pass**; ORDER 001 (CI-collection) is a boot-gating agent item (launch-readiness).
- **mobile-lab · 6-repo harness experiment** — ready-not-launched (packages/prompts committed, paste-ready; experiment repos verified NOT created).

## In-flight (don't drop)

- **Q-0261 round-opening prerequisite:** merge superbot PR #1948 (material branch-only at 9b35fc46) — gates the next round open.
- **Parallel owner session:** the owner-attended dispatch session is landing Q-0262 ORDERs in parallel (trading 008 done @ fd5e9fe, superbot-next 009, kit 011 ~15:33Z) — **re-derive inbox numbers at HEAD before routing anything.**
- **Night-review remediation ORDERs (dispatched 2026-07-10 afternoon, one repo at a time per R19):**
  venture-lab P0 (D1/D2/D3 real-Stripe-path fix — gates the ⚑B/⚑D unfreeze);
  superbot-games P0 (CI collects 73/121 tests — collect ALL suites + count assertion; = boot-gating ORDER 001);
  trading-strategy (deflated-Sharpe significance bar before any holdout use + honest AAPL-donchian re-grade);
  pokemon-mod-lab post-flip verify: **DONE at the 14:36Z pass**; R22 every-session check stands.
- **Ender-missing follow-ups (from the 14:36Z sweep):** venture-lab boot ORDER routed (PR #12) — confirm its heartbeat refreshes next wake; superbot-next mid-mission with no close-out — watch, don't interrupt band 5.
- **ORDER 007 input:** Codex integration LIVE on superbot-next (auto-reviewed #103 clean), NOT enabled on fleet-manager (env-creation ask on PR #26) — the relay rule must account for per-repo enablement.
- Owner morning click-list: **docs/owner-queue.md** (HOT first; launch-readiness synced it — 38 OWNER-CLICK / 11 DECISION; the pokemon-mod-lab URGENT item stays retired).
- EAP free window through 2026-07-14; Anthropic follow-up draft rides the email pack (parked queue). ORDER 004 pre-close snapshot is banked (#27).
- CORRECTED 2026-07-10 ~morning (was: PLATFORM GAP both sides): in-Project routine self-arm WORKS (owner-verified; fleet-manager's own routine now recurring-confirmed at 14:36Z) — wake-arm ORDERs dispatched to 6 active lanes; superbot-games self-arm landed (#21). Coordinator/worker + cross-session walls stand (capabilities.md). Recipe pending: first successful lane records the exact tool/UI path; owner fallback only on a recorded lane failure.

orders: 001–003 open (001 doctrine P1–P11+MISSION.md · 002 manifest re-stamp · 003 review-queue enforcement) · 004–006 done (004 #27 economics ledger · 005–006 executed in PR #20 + codetool-lab-fable5 #14) · 007 new (@codex review-relay rule — rides the next doctrine session)
⚑ needs-owner: see docs/owner-queue.md (HOT first; launch-readiness 2026-07-10 synced — 5 boot-gating clicks: kit OA8, Idea Engine Project, product-forge repo+Project+check)
notes: launch record + dispositions + verified overnight numbers: docs/planning/gen2-launch-record-2026-07-10.md. Launch-readiness checklist: docs/launch-readiness-2026-07-10.md (#30). Economics ledger (ORDER 004): docs/findings/fleet-economics-2026-07.md. Fitted (≤7,500-char) Custom Instructions actually deployed to the websites + trading gen-2 Projects are recorded in docs/proposals/instructions/{websites,trading-strategy}.md § "Deployed fitted version".
