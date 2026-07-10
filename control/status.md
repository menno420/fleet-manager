# fleet-manager · status
updated: 2026-07-10T23:55:00Z
phase: GEN-2 FLEET LIVE — **CONTINUOUS MODE RUNNING (Q-0265): ⚑ PERMISSIONS GRANT LANDED OWNER-AUTHORED (`c23223f`, UNIVERSAL.md v3, PR #51 — the awaited provenance commit; re-land of the built v2 fold now unblocked, rides the work ladder) · chain slice #6 SHIPPED — review-queue superbot-games#5 MANAGER-VERIFIED: residual risk SCOPED (the #16 CI gap does NOT blind #5's own suite — all 10 test files under `tests/mining/`, collected today; 15/19 modules behaviorally tested, 4 import-only blind: loadout/names/taxonomy/titles; fix rides ORDER 001) · chain slice #5 SHIPPED — review-queue superbot-games#16 MANAGER-VERIFIED: CONFIRMED-STILL-BROKEN at repo HEAD `b134961` (gate still `pytest tests/ -q`, exploration's suite invisible; ORDER 001 unexecuted since `4493292`; fix pointer corrected — kit upgrade #22 relocated the pytest step to `.github/workflows/tests.yml`) + sb#1920 re-check: NO new @codex comment (quota refusal stands) + inbox re-read: no ORDER newer than 013** · chain slice #4 shipped (@codex QUOTA-BLOCKED on superbot#1920 — manager ground truth banked: NO dashboard.json consumer validates `meta.schema_version`; review-queue groomed; owner-signal check NO) · chain slice #3 shipped (first drain pass + roster gen #2) · **ORDER 013 CONFORMED games mapping SHIPPED (Q-0267 owner-shaped frame; ⚑ OWNER-QUEUE below — details react) — supersedes the ORDER 012 proposal as a shape** · package centralization SHIPPED (`projects/` registry) · chain slice #2 shipped (ORDERs 009+010, inbox clear) · fleet model matrix banked (`docs/findings/model-matrix-2026-07.md`) · review-queue enforcement LIVE (ORDER 003/007) · doctrine debt PAID (ORDER 001) · Q-0262 folded (ORDER 008)
health: green
kit: v1.7.0 · check: green · engaged: yes (kit line corrected this slice — previous heartbeats said v1.4.0 while the #35 upgrade had landed v1.7.0; drift fixed on sight)
coordinator: **LIVE** — session-based coordinator seat booted 2026-07-10 (round-3 pack §1 brief) · operating model CONTINUOUS (Q-0265)
routine: **fleet-manager failsafe wake** · cron 30 */2 * * * · id `trig_014odnv5h1tkJAFRhix3tGLq` (last verified live in the 122-record `list_triggers` sweep at ~22:07Z: enabled, last fire 20:37:34Z) · pacemaker = ~15-min `send_later` continuation chain, **HOT — chain slice #6 = this PR (#52)**

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

last-shipped: #52 — chain slice #6: superbot-games#5 manager-verify (coverage map: 15/19 behavioral + collected, 4 import-only) + owner-signal YES on the permissions grant (this PR); just before: **#51 OWNER-LANDED (UNIVERSAL.md v3 permissions block, `c23223f`)** · #50 chain slice #5: superbot-games#16 manager-verify (CONFIRMED-STILL-BROKEN + stale fix pointer corrected) + sb#1920 no-new-comment check; before: #49 chain slice #4 (codex quota-blocked verdict + dashboard.json ground truth + review-queue groom + owner-signal check) · #44 chain slice #3 (first drain pass + roster gen #2) · #46 ORDER 013 conformed games mapping (Q-0267 frame) · #45 Custom-Instructions owner ruling (UNIVERSAL.md v2)
universal-pointer: **OWNER RULING 2026-07-10 (owner chat ~22:15Z): Custom Instructions = FULL per-repo `projects/<repo>/instructions.md` paste per Project (they survive archives — full text always present); the universal pointer survives ONLY as the wake/start-off prompt** — projects/UNIVERSAL.md restructured to v2 (wake block v2 + Custom-Instructions flow section; v1's universal instructions block retracted)
blockers: none

> ## ⚑ OWNER-QUEUE — conformed games mapping awaits owner react — Q-0267 frame, details filled: API/contract/name/sequence
>
> **`docs/proposals/games-program-mapping-conformed-2026-07-10.md`** (PR #46, ORDER
> 013): the mapping is now OWNER-SHAPED (superbot router Q-0267 — Seat A = one
> Project on `superbot-games`, whole world ecosystem; Seat B = new idle-engine repo,
> egg farm = first THEME; website-first onboarding; plugin-native). The old PR #41
> proposal is superseded AS A SHAPE (banner added); its #1920 findings + GBA-lane
> rows carry forward. What awaits you now is the DETAILS react (§5 veto points):
> **(1) API SPLIT** — game-state feed stays superbot-lane (#1920); theme/feature
> manifests = game-seat + plugin-contract committed files raw-fetched by websites;
> provisioning = setup-code first · **(2) theme contract drafted in Seat B**,
> promoted to superbot-next's plugin-contract family later · **(3) new repo name
> `superbot-idle`** (alternates: `superbot-plugin-idle`, `idle-engine`) ·
> **(4) websites selector sequenced LAST-shippable** (website-first = user flow,
> not build order). Owner-queue **item 14** carries the full WHAT/WHERE/UNBLOCKS —
> plus the two real clicks: **create the Seat B repo** and the seeded-package push
> for **`superbot-plugin-hello` (EXISTS since your 16:03Z creation, but EMPTY —
> main/master raw 404)**. The Q-0259-era founding-package HOLD is read as RELEASED
> by Q-0267 (the shaping IS the reaction); package *drafting* proceeds, pasting/boot
> stays your clicks.

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

## Lanes (one line each — verified at the 22:15Z roster generation #2; full table: docs/roster.md)

- **venture-lab** — ⚠ STALEST LIVE LANE, worsening (17h18m; 3 unconsumed ORDERs incl. P0 Stripe fix — **D1 defect re-confirmed live at HEAD by this slice's manager-verify**; ⚑B/⚑D stay FROZEN; no trigger — boot is an owner click). HEAD moved only via the manager-side v1.7.1 kit wave (#14).
- **pokemon-mod-lab** — LANE PARKED by design; ORDER 003 unconsumed (no trigger); owner: playtest.
- **gba-homebrew** — Lumen Drift SCOPE-COMPLETE; parked; kit v1.7.1 wave landed at HEAD (#27).
- **substrate-kit** — **v1.7.1 CUT + PUBLISHED fully agent-side** (tag @ `1cbd666`, release run SUCCESS, sha256 independently verified); adopter wave rolling; trigger still pre-Q-0265 naming — cutover relay still owed.
- **trading-strategy** — **PAPER LANE OPERATIONAL** (4 PRs #40–#43: binding pre-registered protocol, loader rail, grading job; opens 07-11); failsafe wake **fired first time 22:05:49Z**; weekly-grading one-shot armed for 07-17.
- **websites** — CONTINUOUS, ~17m fresh; **ORDER 009 FULLY CLOSED** (/projects #72 + /reviews #75 LIVE-verified; 5 slices this wake); send_later chain live-proven.
- **superbot (hub)** — LIVE, HEAD 22:00Z (#1966); recon loop self-fires via Actions; no control/status.md (roster uses HEAD fallback). @codex question pending on #1920 (this slice).
- **superbot-next** — Builder seat HOT (failsafe last fire 22:06Z + chain one-shot 22:18Z); band-5 complete, **first parity flip** (#112); heartbeat lags chain ~3h (benign).
- **superbot-games** — both gen-1 lanes closed/archived by design; gen-2 boot now rides the Q-0267 conformed-mapping details react (⚑ OWNER-QUEUE item 14; package drafting proceeds per ORDER 013); no trigger; kit v1.7.1 at HEAD (#23).
- **product-forge / idea-engine / sim-lab** — all three CONTINUOUS and fresh (<55m); failsafe wakes firing + chain one-shots armed; sim-lab VERDICT 002 finalized (#8); product-forge carries an owner standing merge grant (review-AFTER, 21:07Z).
- **codetool ×3** — wound down, >26h stale by design; safe-to-delete list in owner-queue.

## In-flight (don't drop)

- **Roster parallel-run:** next manager wake compares `docs/roster.md` vs superbot
  `docs/eap/fleet-manifest.md`, fixes generator gaps, then executes phase 2 (manifest →
  pointer stub, checker retirement) unless the owner vetoes; `tools/gen_roster.py`
  mechanization rides the same wake (R25 is the duty either way).
- **Venture-lab staleness:** 3 unconsumed ORDERs + no scheduler — the boot click is the
  unblock (owner-queue); nothing agent-side can consume them until a session runs there.
- **ORDER 010 relay:** per-lane template/card checks + the ground-truth self-report
  instruction ride each next lane contact (trading/gba/pokemon/superbot null conventions
  named in the matrix).
- **Review-queue drain:** first pass done (slice #3); groom done (slice #4);
  **superbot-games#16 manager-verified DONE (slice #5): CONFIRMED-STILL-BROKEN —
  ORDER 001 must now target `.github/workflows/tests.yml` (pointer corrected on the
  row); consumption rides the superbot-games gen-2 boot.** #1920 @codex ask still
  QUOTA-BLOCKED — re-ask post-reset (websites half already ground-truthed;
  botsite/in-repo half owed; slice #5 re-check: no new comment).
  **superbot-games#5 manager-verified DONE (slice #6): risk SCOPED — its suite IS
  collected today (15/19 modules behavioral, 4 import-only blind); row open on the
  verbatim-port read.** **Next manager-verify candidate: the trading#21 remainder**
  (the two undocumented P1 drops). Remaining codex? rows await
  a per-repo Codex probe or the next manager batch. fleet-manager Codex env ask
  still open on PR #26.
- **Idea Engine seat:** trigger firing (22:05:22Z last) + repo fresh (~9m at sweep) —
  owner-queue item 0 retirement is safe at next queue touch.
- **substrate-kit trigger naming:** still "2-hourly standing wake" (pre-Q-0265) — relay
  the failsafe-wake cutover at next lane contact.
- Owner morning click-list: **docs/owner-queue.md**.
- EAP free window through 2026-07-14; economics ledger banked (#27).

orders: **INBOX CLEAR — no open ORDERs.** 013 DONE (conformed mapping, PR #46) · 012 done (PR #41; superseded as a shape by Q-0267) · 009 DONE (PR #38) · 010 DONE this slice (PR #38) · 011 done (re-arm 20:26Z, PR #37) · 003+007 done (PR #37) · 001+008 done (PR #33) · 002 done (superbot #1954 + PR #32) · 004 done (#27) · 005+006 done (PR #20 + codetool-lab-fable5 #14). Work continues via owner dispatches + the wake ladder (chain pacemaker + failsafe cron), NOT via a parked queue.
⚑ needs-owner: **TWO STANDING FLAGS: (1) the games-mapping details react (⚑ OWNER-QUEUE block above, item 14) — still awaited (slice #6 probe: zero comments on #46; reactions not agent-visible from this seat) · (2) the permissions grant — ✅ LANDED OWNER-AUTHORED (`c23223f`, UNIVERSAL.md v3, PR #51, 23:25Z): thank-you/no-action row — the manager now re-lands the built v2 per-repo fold citing that SHA (agent-side, work ladder; owner-queue item 13 rider resolves on that re-land)**; then docs/owner-queue.md (top: **the package paste wave, item 13 — one sitting, ~6 clicks, sim-lab's Routines-screen failsafe arm is the lane-unblocking one**; **games item 14 — conformed-mapping details react + Seat B repo creation + the superbot-plugin-hello seeded-package push (repo EXISTS but EMPTY)**; **product-forge Pages click, item 15 — free, one toggle**; venture-lab boot click — 3 ORDERs starving incl. the P0 Stripe fix; product-forge seed set; venture-lab ⚑A + frozen ⚑B/⚑D)
PROMPT REGISTRY: **fleet-manager `projects/` — canonical, v-stamped (v1 · 2026-07-10 on all 39 prompt files); superbot founding-package copies frozen** (superseded-banner PR superbot #1967); one-writer = manager, lanes propose via ⚑/INTAKE; first full trigger snapshot committed at `projects/_inventory/trigger-registry-2026-07-10.md` (114 triggers, 8 wakes + 8 chain links verbatim; substrate-kit [RECONSTRUCTED] resolved; websites v1-era prompt CONFIRMED deployed — v2 re-paste still owed; sim-lab failsafe ARMED seat-side 20:54Z, OA-003 closed; trading failsafe re-armed 21:03Z at 0 */2 registry-verified). **Permissions v2/v3 re-stamp is BUILT-HELD, not live** (see fold record).
notes: **operating model = CONTINUOUS (Q-0265) — inbox clear; next chain slices come from the work ladder: RE-LAND the built permissions v2 fold citing owner commit `c23223f` (now unblocked — top of ladder) · roster regen if >2h since gen #2 (22:20Z — due ~00:20Z) · next review-queue candidate (trading#21 remainder — #16 verified slice #5, #5 verified slice #6) · roster parallel-run + phase-2 decision · gen_roster.py mechanization · re-ask @codex on #1920 post-quota-reset (websites half already ground-truthed) · ORDER 010 per-lane relay · substrate-kit trigger cutover relay.** Package registry: **projects/ (README = matrix + paste wave)**. Doctrine at: blueprint (P1–P11 + review-queue + continuous-mode entries), MISSION.md, init-prompt-universal § Current text, playbook R17/R19/R21/R24/**R25 (roster regeneration duty, new this slice)**. Registry: **docs/roster.md (generated, R25)**. Matrix: docs/findings/model-matrix-2026-07.md. Economics: docs/findings/fleet-economics-2026-07.md. Launch record: docs/planning/gen2-launch-record-2026-07-10.md.
