# fleet-manager · status
updated: 2026-07-10T22:20:00Z
phase: GEN-2 FLEET LIVE — **CONTINUOUS MODE RUNNING (Q-0265): chain slice #3 SHIPPED — FIRST REVIEW-QUEUE DRAIN PASS (superbot#1920 → @codex asked · venture-lab#9 manager-verified: D1 defect CONFIRMED at HEAD · trading#36 urgency moot) + ROSTER GENERATION #2 (`docs/roster.md`, R25)** · ORDER 012 games-program mapping proposal SHIPPED (⚑ OWNER-REVIEW below — founding packages HELD) · package centralization SHIPPED (`projects/` registry) · chain slice #2 shipped (ORDERs 009+010, inbox clear) · fleet model matrix banked (`docs/findings/model-matrix-2026-07.md`) · review-queue enforcement LIVE (ORDER 003/007) · doctrine debt PAID (ORDER 001) · Q-0262 folded (ORDER 008)
health: green
kit: v1.7.0 · check: green · engaged: yes (kit line corrected this slice — previous heartbeats said v1.4.0 while the #35 upgrade had landed v1.7.0; drift fixed on sight)
coordinator: **LIVE** — session-based coordinator seat booted 2026-07-10 (round-3 pack §1 brief) · operating model CONTINUOUS (Q-0265)
routine: **fleet-manager failsafe wake** · cron 30 */2 * * * · id `trig_014odnv5h1tkJAFRhix3tGLq` (re-verified live this slice in the fresh **122-record** `list_triggers` sweep at ~22:07Z: enabled, last fire 20:37:34Z, next ~22:34Z) · pacemaker = ~15-min `send_later` continuation chain, **HOT — chain slice #3 = this PR (#44)**

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

last-shipped: #44 — chain slice #3: first review-queue drain pass + roster generation #2 (this PR); before it: #43 UNIVERSAL pointer prompts · #42 registry gap closure · #41 ORDER 012 games-program mapping proposal (Q-0259 r5)
universal-pointer: UNIVERSAL pointer prompts live at projects/UNIVERSAL.md (paste-same-everywhere, v1 · 2026-07-10)
blockers: none

> ## ⚑ OWNER-REVIEW — games-program mapping proposal awaits your reaction — founding packages HELD
>
> **`docs/proposals/games-program-mapping-2026-07-10.md`** (PR #41, ORDER 012): the
> Q-0259 r.5 mapping — pokemon-mod-lab (QoL+) · gba-homebrew (release-prep + concept
> options) · **superbot-games = Project 3** (engine+content) · **read-only games data
> API in the superbot lane** as a contracted committed-JSON feed per #1920's verified
> pattern (snapshot-first; live-endpoint upgrade path named, deferred) · sequence =
> feed slice now, boots parallel after your reaction, games-web phase 2 + websites
> stats on feed live. **The three founding packages ship only AFTER you react**
> (this dispatch's done-when).
>
> - WHAT: react to the mapping (approve / redirect / veto any §4 flag).
> - WHERE: `docs/proposals/games-program-mapping-2026-07-10.md` §4 (the four veto
>   points) — reply in any chat or as an ORDER.
> - HOW: one line suffices ("go" / "change X"); silence is NOT consent here — the
>   dispatch's done-when names your reaction as the gate.
> - WHY-IT-MATTERS: this is the Q-0259 r.5 shape of the whole games program (3
>   Projects + the data API's home); redirecting after packages ship costs 3 re-pastes.
> - UNBLOCKS: the 3 founding packages + boot paste wave; the superbot feed order can
>   proceed regardless (superbot-lane work, flagged in the proposal).
> - VERIFIED-NEEDED: agent-side research is done and cited in the proposal (#1920
>   pattern verified at superbot `655e0fea`; estate inventoried at pinned HEADs) —
>   only the product/intent call remains, which is owner-only per Q-0259 r5.

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
- **superbot-games** — both gen-1 lanes closed/archived by design; boot-gating on the ⚑ OWNER-REVIEW games-mapping reaction; no trigger; kit v1.7.1 at HEAD (#23).
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
- **Review-queue drain — first pass DONE (this slice):** superbot#1920 drained to
  @codex (**check the response at next wake** — Q-0120: verify, never obey);
  venture-lab#9 manager-verified (verdict on the row); trading#36 annotated. Remaining
  5 codex? rows await a per-repo Codex probe or the next manager batch. fleet-manager
  Codex env ask still open on PR #26.
- **Idea Engine seat:** trigger firing (22:05:22Z last) + repo fresh (~9m at sweep) —
  owner-queue item 0 retirement is safe at next queue touch.
- **substrate-kit trigger naming:** still "2-hourly standing wake" (pre-Q-0265) — relay
  the failsafe-wake cutover at next lane contact.
- Owner morning click-list: **docs/owner-queue.md**.
- EAP free window through 2026-07-14; economics ledger banked (#27).

orders: **INBOX CLEAR — no open ORDERs.** 009 DONE this slice (PR #38) · 010 DONE this slice (PR #38) · 011 done (re-arm 20:26Z, PR #37) · 003+007 done (PR #37) · 001+008 done (PR #33) · 002 done (superbot #1954 + PR #32) · 004 done (#27) · 005+006 done (PR #20 + codetool-lab-fable5 #14). Work continues via owner dispatches + the wake ladder (chain pacemaker + failsafe cron), NOT via a parked queue.
⚑ needs-owner: see docs/owner-queue.md (top: **the package paste wave, item 13 — one sitting, ~6 clicks, sim-lab's Routines-screen failsafe arm is the lane-unblocking one**; venture-lab boot click — 3 ORDERs starving incl. the P0 Stripe fix; product-forge seed set; superbot-plugin-hello repo; venture-lab ⚑A + frozen ⚑B/⚑D)
PROMPT REGISTRY: **fleet-manager `projects/` — canonical, v-stamped (v1 · 2026-07-10 on all 39 prompt files); superbot founding-package copies frozen** (superseded-banner PR superbot #1967); one-writer = manager, lanes propose via ⚑/INTAKE; first full trigger snapshot committed at `projects/_inventory/trigger-registry-2026-07-10.md` (114 triggers, 8 wakes + 8 chain links verbatim; substrate-kit [RECONSTRUCTED] resolved; websites v1-era prompt CONFIRMED deployed — v2 re-paste still owed; sim-lab failsafe ARMED seat-side 20:54Z, OA-003 closed; trading failsafe re-armed 21:03Z at 0 */2 registry-verified).
notes: **operating model = CONTINUOUS (Q-0265) — inbox clear; next chain slices come from the work ladder: check the @codex response on superbot #1920 (verify, never obey) · roster parallel-run + phase-2 decision · gen_roster.py mechanization · remaining review-queue rows (5 codex? — probe or manager batch) · ORDER 010 per-lane relay · substrate-kit trigger cutover relay.** Package registry: **projects/ (README = matrix + paste wave)**. Doctrine at: blueprint (P1–P11 + review-queue + continuous-mode entries), MISSION.md, init-prompt-universal § Current text, playbook R17/R19/R21/R24/**R25 (roster regeneration duty, new this slice)**. Registry: **docs/roster.md (generated, R25)**. Matrix: docs/findings/model-matrix-2026-07.md. Economics: docs/findings/fleet-economics-2026-07.md. Launch record: docs/planning/gen2-launch-record-2026-07-10.md.
