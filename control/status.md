# fleet-manager · status
updated: 2026-07-11T00:15:00Z
phase: GEN-2 FLEET LIVE — **CONTINUOUS MODE RUNNING (Q-0265): chain slice #7 SHIPPED — ROSTER GENERATION #3 with the biggest delta of any generation: THE GAMES PROGRAM BOOTED (superbot-idle repo LIVE — Seat B boot complete, walking skeleton + theme-schema v1, kit v1.7.1, failsafe `45 */2 * * *` + hot chain; superbot-games Seat A armed — failsafe `15 */2 * * *` created 23:47Z, live chain session, `order-001-collection-scope` branch in flight; the Q-0267 ⚑ details react ANSWERED BY ACTION; `superbot-plugin-hello` still EMPTY) + review-queue trading#21 manager-verified: first row ever CLOSED, RETIRED-SUPERSEDED (promotion label demoted by #36 re-grade · holdout SPENT/report FINAL · paper lane's binding protocol locks the forward subject — zero decision weight left; the two undocumented P1 drops AAPL-SMA/AAPL-MACD confirmed still undocumented but non-load-bearing, annotation rides next trading contact)** · slice #6: superbot-games#5 verify (risk SCOPED, 15/19 behavioral) + permissions grant LANDED OWNER-AUTHORED (`c23223f`, UNIVERSAL.md v3, PR #51) · slice #5: superbot-games#16 CONFIRMED-STILL-BROKEN (fix pointer → tests.yml) · slice #4: @codex quota-blocked + dashboard.json ground truth · slice #3: first drain pass + roster gen #2 · ORDER 013 conformed games mapping (Q-0267) · review-queue enforcement LIVE · doctrine debt PAID · Q-0262 folded
health: green
kit: v1.7.0 · check: green · engaged: yes
coordinator: **LIVE** — session-based coordinator seat booted 2026-07-10 (round-3 pack §1 brief) · operating model CONTINUOUS (Q-0265)
routine: **fleet-manager failsafe wake** · cron 30 */2 * * * · id `trig_014odnv5h1tkJAFRhix3tGLq` (verified live in the 175-record `list_triggers` sweep at ~00:03Z: enabled, last fired 22:35:08Z, next 00:34Z) · pacemaker = ~15-min `send_later` continuation chain, **HOT — chain slice #7 = this PR (#53)**

> **Re-arm record (verbatim, ORDER 011, Q-0265 cutover — executed 2026-07-10T20:26Z,
> re-verified by the 20:43Z chain slice and again by this 21:20Z slice):**
> New trigger created: `trig_014odnv5h1tkJAFRhix3tGLq` · name `"fleet-manager failsafe
> wake"` · `cron_expression="30 */2 * * *"` · created 2026-07-10T**20:26:23Z** ·
> `persistent_session_id="session_01V66KdPhtbR1AThhK77kDqr"` (the coordinator) —
> **verified live** at ~21:15Z this slice: present + enabled in the full 99-record
> `list_triggers` output, last_fired 20:37:34Z, `next_run_at 2026-07-10T22:34:20Z`.
> Old trigger `trig_01QBrp5MjZL3F9mv6KsTXTzN` ("fleet-manager 2-hourly standing wake")
> **deleted — verified gone** (id absent from the same listing).
> Continuation chain: `send_later` pattern, ~15 min per link; chain fire #1 20:43Z =
> the ORDER 003/007 slice (PR #37); **chain fire #2 ~21:00Z = the ORDER 009/010 slice
> (PR #38, this record)**. F-1 rebind-then-delete cutover recipe held.

last-shipped: #53 — chain slice #7: roster generation #3 (GAMES-BOOT delta + stale-clone-cache transport caveat) + trading#21 RETIRED-SUPERSEDED (first closed review-queue row) (this PR); before: #52 slice #6 (superbot-games#5 verify + owner-signal YES on the permissions grant) · **#51 OWNER-LANDED (UNIVERSAL.md v3 permissions block, `c23223f`)** · #50 slice #5 (superbot-games#16 verify) · #49 slice #4 · #44 slice #3 · #46 ORDER 013 conformed games mapping
universal-pointer: **OWNER RULING 2026-07-10 (owner chat ~22:15Z): Custom Instructions = FULL per-repo `projects/<repo>/instructions.md` paste per Project (they survive archives — full text always present); the universal pointer survives ONLY as the wake/start-off prompt** — projects/UNIVERSAL.md restructured to v2 (wake block v2 + Custom-Instructions flow section; v1's universal instructions block retracted); **v3 landed owner-authored `c23223f` (PR #51) with the fleet-canonical Permissions & authority block**
blockers: none

> ## ⚑ OWNER-QUEUE — games program: the details react has been ANSWERED BY ACTION — seats are BOOTED; one click remains (plugin-hello push)
>
> **Observed at roster generation #3 (00:09Z):** the Q-0267 conformed mapping's
> details (`docs/proposals/games-program-mapping-conformed-2026-07-10.md`, PR #46)
> are now REALITY on the ground: **Seat B repo `superbot-idle` EXISTS under exactly
> the proposed name and is LIVE** (boot complete — walking skeleton PR #2, theme-schema
> v1 in progress PR #4 @ 00:01:39Z; founding package consumed from superbot
> `docs/planning/round3-founding-package-games-idle-2026-07-10.md`; failsafe wake +
> hot chain), and **Seat A (superbot-games) is armed** (failsafe wake 23:47:02Z,
> live chain session, `order-001-collection-scope` branch pushed — the P0
> CI-collection fix finally in flight). The manager reads this as the owner's react
> — the mapping's veto points stand accepted-by-boot unless the owner says
> otherwise. **Still owner-open: `superbot-plugin-hello` remains EMPTY** (ls-remote:
> zero refs — the superbot-next seeded-package push is still the unblocked next
> step); owner-queue item 14 reduces to that click + any late veto on the details.

## Chain-slice record — 2026-07-11T~00:00Z fire (chain slice #7, PR #53)

Slice = **inbox re-read + roster generation #3 + the recommended review-queue
manager-verify (trading#21 remainder)**, per the previous heartbeat's work-ladder
pointer:

- **Inbox at HEAD `d156e38`: no ORDER newer than 013** (newest = 013, DONE).
- **Roster generation #3** (R25; gen #2 was 22:15Z): regenerated from all lane
  heartbeats at live HEAD + a fresh 175-record `list_triggers` sweep (23 enabled).
  Headline deltas (full list in `docs/roster.md`): **(1) THE GAMES PROGRAM
  BOOTED** — `superbot-idle` born + live (Seat B) and superbot-games Seat A armed
  with the order-001 fix branch in flight; **(2) substrate-kit trigger cutover
  DONE** (the relay owed since gen #1 — new `substrate-kit failsafe wake`
  23:09:56Z) + kit shipped EAP §6.10 (auto-merge enabler, #152/#153);
  **(3) venture-lab STILL STARVING** (~19h12m, no fire, no trigger — the only
  action-worthy stale lane); forge/sim-lab/idea-engine all HOT (sim-lab: VERDICTs
  003–005 finalized, queue empty, but a NEW platform wall — `refs/tags` push 403;
  idea-engine probing a superbot-games host-seam stub); no lane DARK.
  **Transport caveat banked in the roster header:** the git proxy served stale
  cached clone packs (9/13 repos at pre-22:00Z HEADs on first clone) — every row
  re-fetched until FETCH_HEAD == `ls-remote`; `gen_roster.py` must inherit that
  verify step.
- **trading#21 remainder MANAGER-VERIFIED → row CLOSED, RETIRED-SUPERSEDED**
  (first row ever to reach the review-queue closed section; full verdict there,
  verified against shipped source at trading HEAD `6799a4c`): the promotion label
  is gone (#36 re-grade, t = 0.42 < 1.645; banner on `p2-validation-results.md`;
  rule replaced by `trading_lab.promotion.grade_promotion` + tests), the decision
  it raced is spent (holdout consumed #37, report FINAL, protocol §6 forbids
  re-runs forever), and the paper lane's BINDING pre-registered protocol locks
  the sole forward subject — nothing left for #21's evidence to decide. Residue
  (non-load-bearing): the two P1 drops (**AAPL-SMA, AAPL-MACD** — both starred
  B&H-beats in `p1-trend-following-results.md` yet silently absent from its
  "Survivors for P2" list) are confirmed STILL undocumented at HEAD; a one-line
  historical annotation suggestion rides the next trading lane contact with the
  ORDER 010 relay.
- **Permissions re-land state (as found this slice):** the owner's provenance
  commit `c23223f` (UNIVERSAL.md v3, PR #51) is on main; the built per-repo v2
  fold re-land was **IN FLIGHT but NOT yet merged at write time** — PR #47 open,
  head still at its born-red card (`a4b736b`), the re-land commits visible only
  in a parallel worker's local branch. Re-checked at this PR's merge; whichever
  lands second reconciles by union (never clobber).

## Chain-slice record — 2026-07-10T~23:36Z fire (chain slice #6, PR #52)

Lean slice = **inbox re-read + owner-signal probe + the next review-queue
manager-verify (superbot-games#5)**, per the previous heartbeat's work-ladder
pointer:

- **Inbox at HEAD `c23223f`: no ORDER newer than 013** (newest = 013, DONE).
- **Owner-signal probe — YES, the big one: the awaited permissions grant
  LANDED OWNER-AUTHORED.** `c23223f` (PR #51, author `Menno van Hattum
  <mennovanhattum@gmail.com>`, 2026-07-10T23:25:14Z UTC) rewrites
  `projects/UNIVERSAL.md` to **v3** with the fleet-canonical `## Permissions &
  authority` block; the commit message explicitly names itself the
  user-sourced provenance the instruction-poisoning guard required and directs
  the manager to **re-land the built per-repo v2 instruction fold citing this
  SHA** (grants: merge-own-green-PRs · trigger self-management · worker
  spawning; exclusions + deny-wins included). Flag (2) below updated
  accordingly — keeping it verbatim ("landing owed") would be a known-false
  owner-facing row, the ORDER 005 class. **#46 conformed-mapping thread: NO
  owner comment** (zero comments via API); **reactions are not agent-visible
  from this seat** (REST reactions endpoint proxy-blocked; recorded honestly,
  not inferred) — the games-mapping details react stays awaited.
- **superbot-games#5 MANAGER-VERIFIED — residual risk SCOPED given #16's
  CONFIRMED-STILL-BROKEN.** Headline: the #16 CI-collection gap does **NOT**
  blind #5's own suite — all 10 of the port's test files live under
  `tests/mining/`, the only tree the gate's `pytest tests/ -q`
  (`.github/workflows/tests.yml:45` @ `b134961`) collects, so they run on
  every PR today; the invisible exploration suites are irrelevant to this row.
  File-level map on the row (`docs/review-queue.md`): **15 of the 19 module
  files behaviorally tested + collected; 4 import-only blind (`loadout.py`,
  `names.py`, `taxonomy.py`, `titles.py` — `test_purity.py` imports all 19,
  asserts purity + count, tests no behavior); none fully uncovered.**
  Verified-by-CI today = the 15; blind = the 4 + the verbatim-port-vs-oracle
  claim (no oracle-diff in CI, still non-author-unread). **Fix rides ORDER 001
  as sequenced — CONFIRMED** (collect-ALL + count assertion in `tests.yml`
  protects mining from silent scope loss; it does NOT add the 4 missing
  behavioral tests — that belongs to the gen-2 Seat A boot). Row stays open on
  the verbatim-port read; risk NARROWED.

## Chain-slice record — 2026-07-10T~23:10Z fire (chain slice #5, PR #50)

Lean slice = **the recommended manager-verify (superbot-games#16) + sb#1920 re-check
+ inbox re-read**, per the previous heartbeat's work-ladder pointer:

- **superbot-games#16 MANAGER-VERIFIED — CONFIRMED-STILL-BROKEN at repo HEAD
  `b134961`** (the fleet's canonical "green gate lies" row, crisp binary as
  predicted): the CI pytest step still runs `python3 -m pytest tests/ -q`; the tree
  at HEAD confirms `tests/` contains ONLY `tests/mining/` while exploration's 7 test
  files sit under `games/exploration/tests/` — invisible to the gate. **ORDER 001
  (P0, filed `099664c` 12:47Z) NOT executed by any commit since `4493292`** (only
  kit upgrades #22/#23 landed since). **Precision the verify added:** the row's
  one-line-fix pointer (`substrate-gate.yml:62`) is **STALE** — kit upgrade #22
  relocated the pytest step verbatim into the host carve-out
  **`.github/workflows/tests.yml`** (blob `09b65f4`), so ORDER 001's fix targets
  THAT file: collect-ALL + the count assertion. Escalation: the ORDER is unconsumed
  because the repo has no trigger and both gen-1 lanes are archived — consumption
  rides the gen-2 boot (Q-0267 react, owner-queue item 14). Full verdict on the row.
- **sb#1920: NO new @codex comment** — the thread still ends at the 22:03:53Z
  quota refusal (refusals don't count); row untouched this slice.
- **Inbox at HEAD `af66514`: no ORDER newer than 013** (newest = 013, DONE).

## Chain-slice record — 2026-07-10T~22:50Z fire (chain slice #4, PR #49)

Slice = **@codex response check + review-queue groom + owner-signal check**, per the
previous heartbeat's work-ladder pointer (top item: check the @codex response):

- **@codex on superbot #1920 — QUOTA-BLOCKED, no substantive answer.** The only reply
  after our question (4939890801) is chatgpt-codex-connector[bot]
  [comment 4939891407](https://github.com/menno420/superbot/pull/1920#issuecomment-4939891407)
  @ 22:03:53Z — **7 seconds after the question**: "You have reached your Codex usage
  limits for code reviews" (the earlier quota exhaustion confirmed as cause; re-ask
  post-reset or drain manager-side). **Manager ground truth banked instead (Q-0120
  style — verified against shipped source):** websites `dashboard/data_source.py` at
  HEAD `144dfce` validates `meta.schema_version` ONLY for console.json
  (`console_contract_issue()`); **NO consumer-side check exists for dashboard.json**
  — the question's premise CONFIRMED for the primary consumer; botsite/in-repo half
  still owed. Row annotated (`docs/review-queue.md`).
- **Review-queue groomed:** all 6 remaining open rows re-validated live (every PR
  exists + merged; head SHA + merged-at stamps per row); drain-path notes added
  where thin (superbot-games#5 sequenced after #16's verdict; trading#21 partly
  SUBSUMED by #36's demotion — live remainder = the two undocumented P1 drops;
  pokemon#8 sha1-chain checkable from committed proof fixtures; gba#12 re-check =
  dispatch-tier asserts vs compile-only CI). venture-lab#9: lane HEAD still
  `7558cb2`, fix NOT landed, row open. **Next manager-verify candidate recommended:
  superbot-games#16** (ORDER 001 P0 CI-collection fix still unexecuted — crisp
  binary verify). Recommendation only, not executed.
- **Owner-signal check (read-only): NO on all three.** Main since 17bc193 moved only
  via agent squashes `ced65b4` (#44) and `94b646d` (#46); **no owner-authored commit
  touches `projects/UNIVERSAL.md`**; `docs/owner-queue.md` moved only via #46; zero
  reactions/comments on the #46 conformed-mapping thread. Reported, not acted on.
- **Inbox at HEAD:** no ORDER newer than 013 (newest = 013, DONE).

## Permissions-doctrine fold — 2026-07-10T~22:45Z (owner directive ~22:3xZ) — BUILT, HELD BY GUARD → **UNBLOCKED 23:25Z (owner-landed `c23223f`, see slice #6 record; re-land citing that SHA)**

**Permissions directive folded agent-side; landing HELD.** The canonical
`## Permissions & authority` block (verbatim-identical; names permissions by
name — merge-your-own-green-PRs, trigger self-management, worker spawning;
owner-queue = capability walls only; grant-recipe sentence carrying the
product-forge evidence — the owner's in-session grant cleared the classifier
merge wall, PRs #12/#13 merged) was written into all 13
`projects/<repo>/instructions.md` (→ v2, paste bodies held ≤~7.4k, no rule
removed) + the companion one-liner into all 13 `coordinator-prompt.md` (→ v2)
+ `projects/UNIVERSAL.md` (→ v3 wording home) + `projects/README.md` doctrine
7. **The platform's instruction-poisoning guard refused to commit/land that
content from this session** (same class as the parallel UNIVERSAL-v3 denial:
a standing permission grant sourced only from a coordinator relay must be
user-reviewed) — first denial treated as terminal, no retries. The built fold
sits in the session worktree (branch `claude/permissions-doctrine`, PR #48
carries the clean parts). UNBLOCK = owner-authored landing (owner-queue item
13 rider); the fold then re-lands citing the owner commit as provenance. What
DID land now: owner-queue item 15 (forge Pages click) + the item-13 hold
rider + this record.

## Package-centralization record — 2026-07-10T~21:45Z (owner dispatch, PR #39)

Three parallel builders swept every Project's console package from its scattered
homes (superbot planning docs · fm proposals/prompts · lane repos · chat-only
reconstructions), re-based onto the gen-3/Q-0265 born-continuous standard with
inline provenance stamps; the assembler committed the result verbatim:

- **`projects/` registry LIVE** — one dir per Project: **13 full seat packages**
  (instructions / coordinator-prompt / setup-script / failsafe-prompt / meta:
  the core six + websites, trading, venture-lab, superbot-games,
  pokemon-mod-lab, gba-homebrew, superbot) **+ 5 archive/pre-birth metas**
  (codetool ×3, mobile-lab, games-program) + the three sweep inventories
  (`projects/_inventory/`). Index: `projects/README.md` — registry doctrine
  (source of truth = these files, owner re-pastes after edits,
  regenerate-don't-fork; future distribution = kit-seat templates, the known
  kit gap), the per-Project MATRIX (seat status · cadence · per-part
  deployed-state · key flag), and the paste-wave split.
- **Owner-queue updated:** ONE consolidated paste-wave item (item 13; kit §2b
  + OA8 · forge §2b · **sim-lab failsafe arm via Routines screen — its seat
  lacks the scheduler tools (OA-003)** · websites v2 re-paste + optional
  cadence retune · trading instructions re-paste · superbot optional); the
  Parked **codetool tag mislabel FIXED with provenance** (opus4.8's mdverify
  releases are LIVE; the never-pushed tags are **fable5**'s envdrift — v0.1.0
  @ `73ef38d`, v0.2.0 @ `13a84e5`).
- **websites ORDER 009 dispatched** (coordinator-side) — surface `/projects`
  on the site so the registry is owner-browsable.
- **Notable builder findings** (ground truth vs dispatch premises): trading
  **holdout SPENT + report FINAL**, and its **PR #37 owner-merge click was
  found ALREADY DONE at assembly** (merged_by owner 20:56:34Z, API-verified —
  recorded in owner-queue § Resolved, never added as an open ask);
  **product-forge already live-continuous** with games-web phase-1 SHIPPED
  (PRs #4+#5 — the "expect ORDER 001 pending" premise was ~2h stale);
  **superbot-games kit is actually v1.7.0 at HEAD** (PR #22 — the "v1.2.0,
  5 behind" row was heartbeat drift, not tree state).

## Chain-slice record — 2026-07-10T~22:05Z fire (chain slice #3, PR #44)

Slice = **first review-queue drain pass + roster generation #2**, per the previous
heartbeat's work-ladder pointer:

- **Review-queue drain pass (first ever — the ORDER 003 queue now HAS a drain
  record).** Of the 8 backfilled rows: **superbot#1920** (the only Codex-enabled row)
  drained to **@codex** per R24 — ONE question posted on the merged head
  ([comment 4939890801](https://github.com/menno420/superbot/pull/1920#issuecomment-4939890801)):
  does ANY existing consumer of `dashboard.json` (websites `dashboard/data_source.py`,
  botsite, in-repo) actually read/validate `meta.schema_version`, or is the first
  contract-version bump a silent cross-repo no-op until a consumer-side check exists?
  Response pending — **Q-0120: verify against shipped source, never obey**.
  **venture-lab#9 manager-verified** (highest-consequence Codex-less row): **D1 defect
  CONFIRMED at HEAD `7558cb2`** — confirmed by code: `handle_purchase_event` reads only
  `data.object.customer_email` (null on real events; `customer_details.email` never
  read, session created without `customer_email`), the refusal **returns HTTP 200** so
  Stripe never retries (worse than flagged), `success_url` uses the unsubstituted
  `{CHECKOUT_EMAIL}` + hardcoded localhost, and all 13 tests are synthetic-shape only.
  Full must-cover list for the lane's P0 ORDER 003 is on the row (`docs/review-queue.md`).
  **trading#36** annotated: "drain before holdout" urgency MOOT (holdout spent via #37,
  owner-merged); ordinary drain now.
- **Roster generation #2** (R25): regenerated from all 16 heartbeats at HEAD (git
  transport — shallow blob-filtered clones; direct API proxy-403s from this seat) +
  the fresh 122-record trigger sweep. Headline deltas vs gen #1: **trading pivoted to
  PAPER LANE OPERATIONAL** (4 PRs, opens 07-11) and its failsafe wake **fired for the
  first time** (22:05:49Z); **substrate-kit released v1.7.1 fully agent-side** and the
  adopter wave is rolling (websites #74, venture-lab #14, superbot-games #23, gba #27
  all at v1.7.1); **websites closed ORDER 009 completely** (/projects + /reviews live,
  5 slices); **superbot-next crossed the first parity flip** (#112); **venture-lab
  still starving** (17h18m, no lane fire — only the manager-side kit wave moved HEAD);
  enabled triggers 16 → 20 (continuation one-shots proliferating by design).

## Chain-slice record — 2026-07-10T~21:00Z fire (chain slice #2, PR #38)

Slice = **ORDERs 009 + 010**, per the previous heartbeat's next-chain-slice pointer:

- **ORDER 009 DONE (generated roster v1):** `docs/roster.md` **generation #1** — 17 rows
  (one per lane; superbot-games split exploration/mining), each with heartbeat
  `updated:` stamp + freshness age, phase, orders acked/done, kit version, live trigger
  state (name/cron/last-fire from the 99-record `list_triggers` sweep) and repo@HEAD
  evidence; header: generated-at + **source of truth = the lane heartbeats** + the
  **>24h kill-switch** note. Regeneration duty minted as **playbook R25** (every manager
  wake regenerates, commit-on-change). **Phase 2 decided-and-flagged, NOT executed:**
  superbot manifest → pointer stub + freshness-checker retirement waits for one
  parallel-run wake comparing roster vs manifest (roster proves itself first); owner may
  veto. `tools/gen_roster.py` mechanization is the same follow-up (generation #1 ran as
  a wake procedure).
- **ORDER 010 DONE (model matrix):** `docs/findings/model-matrix-2026-07.md` — per-repo
  Project setting (honest unknowns everywhere except the codetool experiment arms) ·
  card-self-reported families (family-level per Q-0262) · fired-vs-manual where
  determinable · evidence links; the websites 16:01Z cross-surface disagreement cited
  (Routines screen fable-5 vs card sonnet-5, PR #59 squash 2c89e96, re-verified at HEAD).
  Fleet runs ≥3 families same-day (fable-5 / opus-4.8 / sonnet-5); one trigger produced
  two different families across fires — the Routines screen is NOT authoritative;
  per-session self-report stays the least-bad basis. Null conventions to un-null at next
  lane contact (Q-0262): trading "withheld" · gba "ID withheld" · pokemon "lane default" ·
  superbot's newest card template (line missing).
- **Roster staleness verdicts (action-worthy):** **venture-lab 16h23m stale, 3 unconsumed
  ORDERs (002/003/004 incl. the P0 Stripe fix gating frozen ⚑B/⚑D), NO trigger** — its
  "next boot" has no scheduler; owner-queue already carries the boot click. **pokemon-mod-lab**:
  ORDER 003 (visibility verify) landed 12:56Z after its last heartbeat, unconsumed, no
  trigger. Stale-by-design (no action): codetool ×3, superbot-games both lanes, gba.
  Benign: superbot-next heartbeat ~2h behind its hot chain (HEAD 5m old at sweep).

## Doctrine-fold job — 2026-07-10T~20:40Z (Q-0265 continuous mode, MANAGER-ONLY rider)

**Doctrine read at superbot origin/main `6f283b91`** (router Q-0265 continuous-mode
directive + Q-0264 idea pipeline + part-4 brief §2b). Three doctrine folds landed as one
coordinated job: **superbot PR #1962** (gen-3 deployment standard §2 born-continuous),
**fleet-manager PR #36** (blueprint changelog + init-prompt continuous-mode rider +
ORDER 011), **websites routine-prompt v2**. Manager operating model from here:
continuous — the cron is the failsafe, the `send_later` chain is the pacemaker.

## Wake record — 2026-07-10T18:31Z (third standing-wake pass)

ORDER 001 + ORDER 008 executed (PR #33) — blueprint P1–P11 + D4/D5/D6 + MISSION.md;
Q-0262 five fleet policies folded; owner-queue reconciled; superbot #1954 merge
confirmed. Full record: PR #33 + `.sessions/2026-07-10-wake-1831-doctrine.md`.
Staleness-sweep table from that pass is superseded by **`docs/roster.md`** (generated
roster v1, this slice) — the roster is now the sweep's durable home.

## Lanes (one line each — verified at the 00:09Z roster generation #3; full table: docs/roster.md)

- **venture-lab** — ⚠ STALEST LIVE LANE, still worsening (~19h12m; 3 unconsumed ORDERs incl. the P0 Stripe fix; ⚑B/⚑D stay FROZEN; no trigger — boot is an owner click; HEAD unmoved since the kit wave).
- **superbot-idle (NEW — games Seat B)** — **LANE BORN**: boot complete (walking skeleton #2, theme-schema v1 via #4 @ 00:01:39Z), kit v1.7.1, failsafe `45 */2 * * *` + chain HOT.
- **superbot-games (games Seat A)** — **GEN-2 BOOT UNDERWAY**: failsafe `15 */2 * * *` created 23:47Z (first fire 00:15Z pending at sweep), live chain session, `order-001-collection-scope` branch in flight; gen-1 heartbeats stale by design, no gen-2 heartbeat committed yet.
- **pokemon-mod-lab** — LANE PARKED by design; ORDER 003 unconsumed (no trigger); owner: playtest.
- **gba-homebrew** — Lumen Drift SCOPE-COMPLETE; parked.
- **substrate-kit** — **failsafe-wake cutover DONE (23:09:56Z)** — the gen-1 relay debt cleared; EAP §6.10 auto-merge enabler shipped (#152/#153); chain HOT.
- **trading-strategy** — PAPER LANE OPERATIONAL (opens 07-11); kit v1.7.1 (#44); failsafe fired fresh 00:02:27Z; weekly-grading one-shot armed for 07-17.
- **websites** — CONTINUOUS, 9 slices this wake (#64→#83, latest /fleet.json shape-contract test); 4-hourly fired fresh 00:02:41Z.
- **superbot (hub)** — LIVE, HEAD 23:19Z; games-idle founding package on main (consumed by the Seat B boot); @codex re-ask on #1920 still owed post-quota-reset.
- **superbot-next** — Builder seat HOT (kit v1.7.1 at `7c819b1`; chain one-shot 00:16Z); band-6 games + role/proof_channel EFFECT ports next.
- **product-forge / idea-engine / sim-lab** — all CONTINUOUS and fresh; sim-lab finalized VERDICTs 003–005 (queue EMPTY) but hit a **new platform wall: `refs/tags` push 403**; idea-engine probing a superbot-games host-seam stub; forge extending games-web under the standing merge grant.
- **codetool ×3** — wound down, >28h stale by design; safe-to-delete list in owner-queue.

## In-flight (don't drop)

- **Roster parallel-run:** next manager wake compares `docs/roster.md` vs superbot
  `docs/eap/fleet-manifest.md`, fixes generator gaps, then executes phase 2 (manifest →
  pointer stub, checker retirement) unless the owner vetoes; `tools/gen_roster.py`
  mechanization rides the same wake (R25 is the duty either way) — **and must inherit
  the gen-#3 transport lesson: verify FETCH_HEAD == `ls-remote` before trusting a
  shallow clone (stale proxy cache caught this generation, 9/13 repos).**
- **Permissions re-land:** owner provenance `c23223f` on main; the per-repo v2 fold
  re-land was in flight (PR #47, parallel worker) at this slice's write — verify its
  landing next slice; owner-queue item 13 rider resolves on it.
- **Venture-lab staleness:** 3 unconsumed ORDERs + no scheduler — the boot click is the
  unblock (owner-queue); nothing agent-side can consume them until a session runs there.
- **ORDER 010 relay:** per-lane template/card checks + the ground-truth self-report
  instruction ride each next lane contact — **now including the trading#21 residue
  annotation suggestion (the two undocumented P1 drops, AAPL-SMA/AAPL-MACD)**.
- **Review-queue drain:** trading#21 CLOSED this slice (RETIRED-SUPERSEDED — first
  closed row). Open rows: venture-lab#9 (awaits the lane's P0 fix) ·
  superbot-games#16 (fix in flight — `order-001-collection-scope` branch spotted at
  gen #3; verify its merge next slice) · superbot-games#5 (verbatim-port read; 4
  import-only modules) · trading#36 (ordinary drain) · superbot#1920 (@codex re-ask
  post-quota-reset; botsite/in-repo half owed) · pokemon#8 · gba#12. **Next
  manager-verify candidate: pokemon#8 (sha1-chain from committed proof fixtures) or
  gba#12 (dispatch-tier asserts vs compile-only CI).** fleet-manager Codex env ask
  still open on PR #26.
- **sim-lab tag-push 403:** new platform wall recorded on its heartbeat — candidate
  for the capability ledger + a kit-side release-route note at next kit contact.
- **substrate-kit trigger naming:** ~~cutover relay owed~~ **RESOLVED — verified at
  gen #3** (failsafe wake live 23:09:56Z).
- Owner morning click-list: **docs/owner-queue.md**.
- EAP free window through 2026-07-14; economics ledger banked (#27).

orders: **INBOX CLEAR — no open ORDERs; no ORDER newer than 013 at HEAD `d156e38` (re-read this slice).** 013 DONE (conformed mapping, PR #46) · 012 done (PR #41; superseded as a shape by Q-0267) · 009 DONE (PR #38) · 010 DONE (PR #38) · 011 done (re-arm 20:26Z, PR #37) · 003+007 done (PR #37) · 001+008 done (PR #33) · 002 done (superbot #1954 + PR #32) · 004 done (#27) · 005+006 done (PR #20 + codetool-lab-fable5 #14). Work continues via owner dispatches + the wake ladder (chain pacemaker + failsafe cron), NOT via a parked queue.
⚑ needs-owner: **(1) games program — the details react is ANSWERED BY ACTION (seats booted; ⚑ block above): remaining click = the `superbot-plugin-hello` seeded-package push (repo still EMPTY at 00:07Z ls-remote); late veto on the mapping details stays open to you · (2) permissions — grant LANDED owner-authored (`c23223f`); the per-repo re-land is agent-side and in flight (PR #47)**; then docs/owner-queue.md (top: the package paste wave, item 13 — sim-lab's Routines-screen failsafe arm was closed seat-side 20:54Z, rest ~5 clicks; **venture-lab boot click — 3 ORDERs starving incl. the P0 Stripe fix, now the fleet's ONLY action-worthy stale lane**; product-forge Pages click, item 15; venture-lab ⚑A + frozen ⚑B/⚑D)
PROMPT REGISTRY: **fleet-manager `projects/` — canonical, v-stamped (v1 · 2026-07-10 on all 39 prompt files); superbot founding-package copies frozen** (superseded-banner PR superbot #1967); one-writer = manager, lanes propose via ⚑/INTAKE; first full trigger snapshot committed at `projects/_inventory/trigger-registry-2026-07-10.md` (114 triggers; live sweep now 175 records / 23 enabled — see roster gen #3); websites v1-era prompt CONFIRMED deployed — v2 re-paste still owed. **Permissions v2/v3 re-stamp: owner provenance landed (`c23223f`); per-repo re-land in flight (PR #47) — not yet live at this write.**
notes: **operating model = CONTINUOUS (Q-0265) — inbox clear; next chain slices come from the work ladder: verify the permissions re-land (PR #47) landed + paste-wave GO state · owner-signal probe (games-mapping react on fm #46 — largely mooted by the boot, but late-veto watch stays) · next review-queue candidate (pokemon#8 or gba#12) · verify superbot-games `order-001-collection-scope` merged (flips the #16 row) · roster regen if >2h since gen #3 (00:09Z — due ~02:09Z) · roster parallel-run + phase-2 decision · gen_roster.py mechanization (with the ls-remote verify step) · re-ask @codex on #1920 post-quota-reset · ORDER 010 per-lane relay (+ trading#21 residue annotation).** Package registry: **projects/ (README = matrix + paste wave)**. Doctrine at: blueprint (P1–P11 + review-queue + continuous-mode entries), MISSION.md, init-prompt-universal § Current text, playbook R17/R19/R21/R24/R25. Registry: **docs/roster.md (generated, R25 — gen #3 this slice)**. Matrix: docs/findings/model-matrix-2026-07.md. Economics: docs/findings/fleet-economics-2026-07.md. Launch record: docs/planning/gen2-launch-record-2026-07-10.md.
