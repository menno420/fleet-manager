# fleet-manager · status
updated: 2026-07-10T20:40:00Z
phase: GEN-2 FLEET LIVE — standing-wake cadence RUNNING (18:31Z third pass closed below) · **doctrine debt PAID: blueprint amendments P1–P11 applied, MISSION.md on main, init prompt carries the verified routine recipe (ORDER 001)** · Q-0262 owner-rulings batch folded + owner-queue reconciled (ORDER 008) · **Q-0265 CONTINUOUS MODE: doctrine folds landing + manager seat adopting (~20:40Z job below)**
health: green
kit: v1.4.0 · check: green · engaged: yes
coordinator: **LIVE** — session-based coordinator seat booted 2026-07-10 (round-3 pack §1 brief)
routine: fleet-manager 2-hourly standing wake · cron 30 */2 * * * · armed-by-me (id `trig_01QBrp5MjZL3F9mv6KsTXTzN`) — **three consecutive on-schedule fires: 14:36Z + 16:31Z + 18:31Z (18:31:59Z)**; next run due 2026-07-10T~20:31Z

> **Arming record (verbatim, 2026-07-10T13:40Z — reproducible recipe, first-class):**
> Tool: claude-code-remote `create_trigger` (MCP; verified after with `list_triggers`).
> Args: `name="fleet-manager 2-hourly standing wake"`, `cron_expression="30 */2 * * *"`,
> `persistent_session_id="cse_01V66KdPhtbR1AThhK77kDqr"` (the coordinator session),
> `prompt=` the standing 2-HOURLY WAKE text (stored verbatim in the trigger).
> Result: `{"trigger":{"id":"trig_01QBrp5MjZL3F9mv6KsTXTzN","name":"fleet-manager 2-hourly standing wake","cron_expression":"30 */2 * * *","enabled":true,"next_run_at":"2026-07-10T14:36:04Z", … "persistent_session_id":"session_01V66KdPhtbR1AThhK77kDqr"}}`
> — no error; the passed `cse_…` id was accepted and normalized to `session_…` form;
> recurring cron confirmed by the 14:36Z, 16:31Z **and** 18:31Z firings.
> This recipe is now doctrine: `docs/prompts/init-prompt-universal.md` § Current text.

last-shipped: #33 — 18:31Z wake pass (ORDER 001 doctrine debt + ORDER 008 Q-0262 policies + owner-queue reconciliation)
blockers: none

## Doctrine-fold job — 2026-07-10T~20:40Z (Q-0265 continuous mode, MANAGER-ONLY rider)

**Doctrine read at superbot origin/main `6f283b91`** (router Q-0265 continuous-mode
directive + Q-0264 idea pipeline + part-4 brief §2b). Executing the §2b MANAGER-ONLY
rider ("fold Q-0265 into the gen-3 blueprint delta + your doctrine ORDERs so every
future seat is born continuous") — **three doctrine folds landing** as one coordinated
job:

- **superbot PR #1962** — gen-3 deployment standard §2: superseded one-slice pacing
  amended to born-continuous (work loop · ~15-min `send_later` chain pacemaker ·
  cron demoted to "<seat> failsafe wake", 2-hourly stagger kept · backpressure brake ·
  Q-0089 honesty guard · free-window use-excessively posture through 2026-07-14).
- **fleet-manager (this PR)** — blueprint changelog entry (continuous-mode operating
  model supersedes one-slice-per-wake for production seats, Q-0265) + init-prompt
  continuous-mode rider (verified arming recipe untouched) + **inbox ORDER 011**
  (manager seat itself adopts continuous mode — status in-progress, a parallel worker
  is executing the trigger re-word + `send_later` chain right now; its re-arm record
  lands verbatim in this file per the proven cutover recipe).
- **websites PR** — routine-prompt v2 (continuous-mode wake text, Q-0264 escalation
  line into the work-ladder doc).

**Manager operating model from here:** continuous mode — next actions run **ORDER 003
→ 007 → 009 → 010 via the `send_later` continuation chain** (the cron becomes the
failsafe once ORDER 011's re-arm lands), not one-per-wake.

## Critical-finding job — 2026-07-10T~19:50Z (owner-dispatched, between wakes)

**Finding (owner report ~20:00Z + owner correction, framed accordingly):** model
attribution for routine-fired sessions is **inconsistent across surfaces** — the
Routines menu displays fable-5 for ALL project-created routines, while the evidenced
websites fired session's chat header showed "Sonnet 5" and its own card self-reports
`📊 Model: claude-sonnet-5` (websites PR #59, squash 2c89e96, card line 8 verified at
HEAD). Ground truth is undeterminable from any single panel. **Probe:** `create_trigger`
exposes **NO model parameter** (schema: name · prompt · cron_expression · run_once_at ·
persistent_session_id · create_new_session_on_fire · environment_id · notifications);
`list_triggers` (50 records) carries no model field anywhere — no agent-side pin exists;
mitigation = per-session family-level self-report on the card (`📊 Model:` line).
Landed (this PR, **#34**): capabilities rider + experiments caveat 5 + init-prompt
known-limit rider + owner-queue Anthropic-email 4th platform bug + **ORDER 010**
(per-lane model verification sweep w/ ground-truth self-report step, rides the
staleness sweep). Known matrix so far (self-reports from cards, family-level):
websites fire = **sonnet-5** (evidenced); superbot-next recent cards = fable-5;
substrate-kit recent cards = fable-5 + opus-4.8 mixed (fired-vs-manual not
distinguished for those two — ORDER 010 establishes the per-lane basis).

## Wake record — 2026-07-10T18:31Z (third standing-wake pass)

Routine fired on schedule at 18:31:59Z (third consecutive fire). Slice = **ORDER 001 +
ORDER 008** (doctrine session, per the 16:31Z pass's pointer). What this pass did:

- **ORDER 001 EXECUTED (the P1 doctrine debt):** blueprint amendments **P1–P11**
  applied to `docs/gen2-blueprint.md` with a provenance changelog entry (fable5-review
  F-numbers inline; today-corrections named where reality had moved: P6's scheduler
  premise narrowed — self-arm WORKS; P8 merged with the Q-0262 family-level model
  policy). **D4** (wind-down marker carve-out + stale deployment-record fix), **D5**
  (init-prompt-universal REWRITTEN — false routine promise out, VERIFIED recipe in:
  `create_trigger` w/ cron + prompt + `persistent_session_id` (cse_/session_ accepted)
  or `create_new_session_on_fire=true`; record verbatim call+outcome; `list_triggers`
  verify; F-1 rebind-then-`delete_trigger` cutover), **D6** (**MISSION.md** at repo
  root — manager mission + explicit done-when + standing default). Playbook riders:
  R21 P1 arm-timing correction, R19 next-free-ORDER-number rule, R17 grammar policy.
- **ORDER 008 EXECUTED (Q-0262 fleet policies):** all five folded into doctrine homes
  (see inbox ✅ record); lane halves verified at their HEADs — kit ORDER 011 executed
  (#127/#128, Reading A), trading ORDER 008 acked (fresh session runs it), next
  ORDER 009 applied (#105).
- **Owner-queue reconciled to Q-0262:** F-5, holdout unlock, flag-13, seat 6
  (= superbot hub, veto-able), pokemon QoL+, package-hold → Resolved with citations;
  **safe-to-delete/archive list consolidated** (old kit-lab coordinator chat now
  verified-spent; stale-branch set per launch-readiness). Genuinely-open clicks kept:
  Idea Engine Project (but see sweep below), product-forge seed set, kit OA8/OA2,
  superbot-plugin-hello + up-to-date-rule relax, venture-lab ⚑A–D (B/D frozen).
- **superbot PR #1954 (manifest re-stamp) MERGED** 16:42:52Z — confirmed; the 16:31Z
  in-flight item is closed.

### Staleness sweep (18:33–18:37Z; triggers via live `list_triggers`, repos via API @ HEAD)

| lane | verdict | evidence |
|---|---|---|
| substrate-kit | **LIVE** | HEAD 2c77011 18:22:16Z; status `updated: 18:22:00Z` — matches its claims (EAP §6.1 shipped #130/b221c87; §6.3 claimed via fast-lane #132); 2-hourly trigger fired 18:09:56Z |
| websites | **IDLE-parked · ⚠ ONE SILENT FIRE** | trigger `trig_017H9Qb9o…` fired 16:01:32Z (fresh-session mode) but **no repo commit since 13:57:29Z** (HEAD d493792) — the woken session produced nothing visible in ~2.5h. Next fire 20:01Z; per the 16:31Z rule, **escalate only on a second silent fire** — the ~20:31Z wake checks for a post-20:01Z commit and escalates if silent again |
| trading-strategy | **LIVE** | HEAD e713abb 16:24:43Z; status 16:21:48Z — ORDER 007 DONE (significance bar; AAPL-donchian demoted to candidate), ORDER 008 acked, holdout still SEALED; 4-hourly trigger fired 16:06:27Z |
| superbot-next | **LIVE — Builder seat BOOTED** | ORDER 008 self-arm ACKED+DONE with the verbatim record (trigger `builder-wake`, cron 0 */2, fired 18:03:29Z); HEAD f1b4761 18:19:50Z, status 18:25Z — band-5 step 7 complete, live-drive leg done (#109), ORDER 011 done (#107). The 16:31Z ENDER-MISSING flag is CLEARED (fresh heartbeats landing) |
| superbot (hub) | **LIVE** | HEAD b078d8e 18:06:16Z (#1956 dashboard refresh); #1954 merged 16:42:52Z; recon loop self-firing |
| venture-lab | **IDLE-parked (stale-by-design)** | status still 04:57:30Z (pre-boot by design — refresh rides ORDER 004's fresh boot); HEAD af11bdb 14:49:39Z is the manager's own ORDER-004 routing PR #12; **no venture-lab trigger exists** (re-verified) — ORDERs 002/003/004 still ride the lane's next boot |

**Sweep bonus finding:** live triggers include **"idea-engine 2-hourly standing wake"**
(`trig_01KBoHPaq…`, fired 18:05:20Z) — strong evidence the **Idea Engine Project (core
seat 4, owner-queue item 0) has been created and self-armed**. Item 0 annotated
LIKELY-DONE; the ~20:31Z wake confirms via a seat heartbeat/repo trace and retires it.

## Launch-readiness pass — 2026-07-10 (owner dispatch)

Owner-dispatched pass, CLOSED. Deliverable: **`docs/launch-readiness-2026-07-10.md`**
(merged PR #30, squash 7af63f8) — the Q-0261 finalize-first checklist across all 13 seats,
owner-queue synced. Q-0262 has since consumed several of its DECISION rows (see
owner-queue § Resolved 2026-07-10). Routing outcomes: see the doc + PR #31's record.

## Lanes (current, one line each — verified at the 18:31Z wake pass)

- **venture-lab** — 9 PRs landed; 2 sellable products + buyer zips ON MAIN; **⚑B/⚑D publish clicks FROZEN** pending ORDER 003 (P0 real-Stripe-path fix); ORDERs 002/003/004 pending, all ride the fresh boot (heartbeat stale-by-design 04:57Z); no trigger yet.
- **pokemon-mod-lab** — PRIVATE ✅; LANE PARKED; concept pick RESOLVED (QoL+, Q-0262.7, effective post-core); ORDERs 002/003 consumable at first boot; owner: playtest.
- **gba-homebrew** — Lumen Drift SCOPE-COMPLETE; ORDER 002 pending; Track-B concept pick still open (owner-queue item 4).
- **substrate-kit** — fresh seat LIVE (see sweep); EAP §6.1 shipped, §6.3 claimed in-flight; F-5 ruling EXECUTED (Reading A, #127/#128); carried owner items: OA8 paste + P10 check swap.
- **trading-strategy** — LIVE; ORDER 007 done (promotion bar; AAPL-donchian → candidate); ORDER 008 (holdout, GRANTED) awaits its dedicated fresh session; holdout SEALED.
- **websites** — orders 001–008 done; routine fires on schedule but **first woken session produced no commit yet** (one silent fire — watch, escalate on second).
- **superbot (hub)** — #1948 + #1954 merged; named **core seat 6** by Q-0262 (owner may veto); Idea Engine seat: trigger live (see sweep bonus); recon loop self-fires.
- **superbot-next** — **Builder seat LIVE** (ORDER 008 done, builder-wake firing); band-5 step 7 complete, live-drive done; next lane: 3 live-only bugs + EFFECT action ports; ORDERs left: 002 (repo click).
- **superbot-games** — lanes closed green; ORDER 001 (P0 CI-collection) + ORDER 002 (self-arm) pending — boot-gating pair.
- **codetool ×3** — Projects CLOSED; repos retained; safe-to-delete list refreshed (owner-queue § housekeeping).
- **mobile-lab** — ready-not-launched; repos NOT created (owner-gated).

## In-flight (don't drop)

- **websites silent-fire watch:** trigger fired 16:01:32Z, no commit by 18:37Z. Next fire 20:01Z → the ~20:31Z wake checks for a post-20:01Z commit; **second silent fire = escalate** (⚑ owner: look at the websites Project's session list).
- **Night-review remediation ORDERs:** venture-lab P0 Stripe fix (gates ⚑B/⚑D unfreeze) · superbot-games P0 CI-collection (= boot-gating ORDER 001) · trading ORDER 008 holdout run (needs its dedicated fresh session).
- **Self-arm gap:** still NO triggers for venture-lab / pokemon-mod-lab / gba-homebrew / superbot-games (re-verified via `list_triggers` this pass); their ORDERs ride their next boots.
- **Idea Engine seat confirmation** — trigger live (18:05:20Z fire); confirm heartbeat/repo trace next wake, then retire owner-queue item 0.
- **superbot hub founding package** (seat 6, Q-0262 ruling) — manager drafts it; a future wake or the coordinator picks this up (new agent-doable work, not yet an ORDER).
- **ORDER 007 input:** Codex integration LIVE on superbot-next, NOT enabled on fleet-manager (env-creation ask on PR #26).
- Owner morning click-list: **docs/owner-queue.md** (reconciled to Q-0262 this pass; boot-gating clicks now: kit OA8, product-forge repo+Project+check, superbot-plugin-hello repo).
- EAP free window through 2026-07-14; economics ledger banked (#27).

orders: **011 in-progress (manager adopts continuous mode, Q-0265 — parallel worker executing; filed by the ~20:40Z doctrine-fold job)** · 003 open (review-queue enforcement — next slice) · 007 new (@codex review-relay rule — rides 003 if capacity) · 009 new-P2 (generated roster v1 — future wake, owner may veto) · **010 new-P2 (per-lane model verification sweep — rides the staleness sweep; filed by the ~19:50Z finding job, PR #34)** · **001 DONE this pass (PR #33)** · **008 DONE this pass (PR #33)** · 002 done (superbot #1954 + PR #32) · 004–006 done (004 #27 · 005–006 PR #20 + codetool-lab-fable5 #14)
⚑ needs-owner: see docs/owner-queue.md (HOT stack shrank: F-5/holdout/flag-13/seat-6/pokemon all RESOLVED by Q-0262; top remaining: kit OA8 paste, product-forge seed set, superbot-plugin-hello repo, venture-lab ⚑A + frozen ⚑B/⚑D)
notes: **operating model = CONTINUOUS (Q-0265, ~20:40Z job above): next actions ORDER 003 → 007 → 009 → 010 run via the send_later continuation chain, slice after slice — the cron becomes the failsafe once ORDER 011's re-arm lands.** ORDER 003 (review-queue enforcement: auto-append rule + named standing drainer + first drain pass) then 007 (@codex relay rule — same doctrine surfaces) then 009 (generated roster v1) then 010 (per-lane model verification sweep). Also next: websites second-fire check (escalate if silent) + Idea Engine seat confirm. Doctrine now at: blueprint (P1–P11 applied), MISSION.md, init-prompt-universal § Current text, playbook R17/R19/R21 riders. Launch record: docs/planning/gen2-launch-record-2026-07-10.md. Launch-readiness: docs/launch-readiness-2026-07-10.md (#30). Economics ledger: docs/findings/fleet-economics-2026-07.md.
