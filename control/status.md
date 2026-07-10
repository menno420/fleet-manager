# fleet-manager · status
updated: 2026-07-10T22:25:00Z
phase: GEN-2 FLEET LIVE — **CONTINUOUS MODE RUNNING (Q-0265): ORDER 012 games-program mapping proposal SHIPPED (⚑ OWNER-REVIEW below — founding packages HELD) · PACKAGE CENTRALIZATION SHIPPED (`projects/` registry, this PR) — every Project's console package now has ONE committed home** · chain slice #2 shipped (ORDERs 009+010, inbox clear) · generated roster v1 LIVE (`docs/roster.md`, playbook R25) · fleet model matrix banked (`docs/findings/model-matrix-2026-07.md`) · review-queue enforcement LIVE (ORDER 003/007) · doctrine debt PAID (ORDER 001) · Q-0262 folded (ORDER 008)
health: green
kit: v1.7.0 · check: green · engaged: yes (kit line corrected this slice — previous heartbeats said v1.4.0 while the #35 upgrade had landed v1.7.0; drift fixed on sight)
coordinator: **LIVE** — session-based coordinator seat booted 2026-07-10 (round-3 pack §1 brief) · operating model CONTINUOUS (Q-0265)
routine: **fleet-manager failsafe wake** · cron 30 */2 * * * · id `trig_014odnv5h1tkJAFRhix3tGLq` (verified live this slice in the 99-record `list_triggers` sweep: enabled, last fire 20:37:34Z, next ~22:34Z) · pacemaker = ~15-min `send_later` continuation chain, **HOT — chain slice #2 = this PR**

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

last-shipped: #41 — ORDER 012 games-program mapping proposal (Q-0259 r5)
universal-pointer: **OWNER RULING 2026-07-10 (owner chat ~22:15Z): Custom Instructions = FULL per-repo `projects/<repo>/instructions.md` paste per Project (they survive archives — full text always present); the universal pointer survives ONLY as the wake/start-off prompt** — projects/UNIVERSAL.md restructured to v2 (wake block v2 + Custom-Instructions flow section; v1's universal instructions block retracted)
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

## Lanes (one line each — verified at the 21:20Z roster generation; full table: docs/roster.md)

- **venture-lab** — ⚠ STALEST LIVE LANE (16h+; 3 unconsumed ORDERs incl. P0 Stripe fix; ⚑B/⚑D stay FROZEN; no trigger — boot is an owner click).
- **pokemon-mod-lab** — LANE PARKED by design; ORDER 003 unconsumed (no trigger); owner: playtest.
- **gba-homebrew** — Lumen Drift SCOPE-COMPLETE; parked; kit v1.7.0 wave landed at HEAD.
- **substrate-kit** — LIVE, ~18m fresh; v1.7.1 payload staged (#137), release claim open (21:11Z); trigger still pre-Q-0265 naming (standing wake) — cutover candidate at next contact.
- **trading-strategy** — **PROGRAM COMPLETE ON MAIN** (holdout #37 merged: PRIMARY directional, not significant); failsafe wake armed 21:03Z; paper lane is the standing mission.
- **websites** — CONTINUOUS, ~13m fresh; 20:00Z wake landed 3 slices (#64/#67/#69), claiming its ORDER 009; **silent-fire watch CLEARED** (16:01Z + 20:00Z fires both produced landed work per its own heartbeat).
- **superbot (hub)** — LIVE, HEAD 20:53Z; recon loop self-fires via Actions; no control/status.md (roster uses HEAD fallback).
- **superbot-next** — Builder seat HOT (failsafe wake + chain one-shots live); band-5 complete, first parity flip (#112); heartbeat lags chain ~2h (benign).
- **superbot-games** — both gen-1 lanes closed/archived by design; boot-gating ORDERs pending; no trigger.
- **product-forge / idea-engine / sim-lab** — all three CONTINUOUS and fresh (<40m); failsafe wakes firing; sim-lab VERDICT 001 finalized.
- **codetool ×3** — wound down, >25h stale by design; safe-to-delete list in owner-queue.

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
- **Review-queue drain:** first @codex drain of the 8 backfilled rows — trading#36
  time-sensitivity is RESOLVED (holdout already executed via #37; the row drains as
  ordinary post-merge review now). fleet-manager Codex env ask still open on PR #26.
- **Idea Engine seat:** trigger firing (20:01:12Z last) + repo fresh (~8m at sweep) —
  owner-queue item 0 retirement is safe at next queue touch.
- **substrate-kit trigger naming:** still "2-hourly standing wake" (pre-Q-0265) — relay
  the failsafe-wake cutover at next lane contact.
- Owner morning click-list: **docs/owner-queue.md**.
- EAP free window through 2026-07-14; economics ledger banked (#27).

orders: **INBOX CLEAR — no open ORDERs.** 009 DONE this slice (PR #38) · 010 DONE this slice (PR #38) · 011 done (re-arm 20:26Z, PR #37) · 003+007 done (PR #37) · 001+008 done (PR #33) · 002 done (superbot #1954 + PR #32) · 004 done (#27) · 005+006 done (PR #20 + codetool-lab-fable5 #14). Work continues via owner dispatches + the wake ladder (chain pacemaker + failsafe cron), NOT via a parked queue.
⚑ needs-owner: see docs/owner-queue.md (top: **the package paste wave, item 13 — one sitting, ~6 clicks, sim-lab's Routines-screen failsafe arm is the lane-unblocking one**; venture-lab boot click — 3 ORDERs starving incl. the P0 Stripe fix; product-forge seed set; superbot-plugin-hello repo; venture-lab ⚑A + frozen ⚑B/⚑D)
notes: **operating model = CONTINUOUS (Q-0265) — inbox clear; next chain slices come from the work ladder: roster parallel-run + phase-2 decision · gen_roster.py mechanization · first @codex review-queue drain · ORDER 010 per-lane relay · substrate-kit trigger cutover relay.** Package registry: **projects/ (README = matrix + paste wave)**. Doctrine at: blueprint (P1–P11 + review-queue + continuous-mode entries), MISSION.md, init-prompt-universal § Current text, playbook R17/R19/R21/R24/**R25 (roster regeneration duty, new this slice)**. Registry: **docs/roster.md (generated, R25)**. Matrix: docs/findings/model-matrix-2026-07.md. Economics: docs/findings/fleet-economics-2026-07.md. Launch record: docs/planning/gen2-launch-record-2026-07-10.md.
