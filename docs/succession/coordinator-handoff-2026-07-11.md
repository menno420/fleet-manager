# Coordinator succession handoff — 2026-07-11

> **Status:** `handoff` — written ~01:0xZ 2026-07-11 by the outgoing coordinator
> session (`session_01V66KdPhtbR1AThhK77kDqr`, Claude Fable 5 family) as its chat
> was archived. **This is the successor coordinator's ONE-READ state doc.** Boot
> flow: the owner pastes `projects/fleet-manager/reboot-prompt.md` into a fresh
> coordinator chat; that prompt routes here. Everything below was verified at
> origin/main `076fff3` (PR #54) + the live trigger registry (~00:03Z 175-record
> sweep) + the live PR list (~01:00Z). Source precedence unchanged: repos at
> HEAD > this doc > memory of any chat.

## 1. What is LIVE right now (seats + triggers)

Full generated registry: **`docs/roster.md`** (generation #3, 00:09Z — regenerate
first if >2h old, R25). Trigger snapshot: `projects/_inventory/trigger-registry-2026-07-10.md`
(live sweep since: 175 records / 23 enabled). One-line state, verified at gen #3:

| Seat | Wake state (name · cron) | Note |
|---|---|---|
| **fleet-manager (you)** | `fleet-manager failsafe wake` · `30 */2 * * *` · **id `trig_014odnv5h1tkJAFRhix3tGLq`** | ⚠ **bound to the ARCHIVED coordinator chat** (`persistent_session_id=session_01V66KdPhtbR1AThhK77kDqr`). **Your first act = the F-1 cutover** (reboot-prompt step 2). Until then the fleet has NO live manager wake. The archived session's leftover `send_later` chain one-shots may still fire into the dead session — **harmless, ignore, they self-expire**. |
| superbot-next | Builder failsafe · `0 */2 * * *` + hot chain | band-6 games + role/proof_channel EFFECT ports next |
| substrate-kit | `substrate-kit failsafe wake` · `0 */2 * * *` (cutover DONE 23:09:56Z) + hot chain | v1.7.1 out; EAP §6.10 auto-merge enabler shipped |
| websites | lane wake · `0 */4 * * *` + chain | CONTINUOUS; /projects + /reviews + /fleet.json live |
| trading-strategy | failsafe · `0 */2 * * *` + weekly-grading one-shot 07-17T09:00Z | PAPER LANE opens 2026-07-11; protocol BINDING |
| superbot-games (Seat A) | `superbot-games failsafe wake` · `15 */2 * * *` (created 23:47:02Z) + chain | gen-2 boot underway; `order-001-collection-scope` (P0 CI-collection fix) in flight |
| superbot-idle (Seat B) | `superbot-idle failsafe wake` · `45 */2 * * *` (created 23:44:45Z) + chain | LANE BORN 2026-07-10/11: walking skeleton + theme-schema v1; kit v1.7.1 |
| product-forge / idea-engine / sim-lab | failsafes `0 */2` / `0 */2` / `0 1-23/2` + chains | all CONTINUOUS; sim-lab queue EMPTY but tag-push 403 wall (§6) |
| superbot (hub) | no repo trigger (Actions recon loop) | games-idle founding package on main; @codex re-ask on #1920 owed post-quota-reset |
| venture-lab | **NONE — no trigger, no session since 07-10T04:57Z** | stalest live lane; 3 unconsumed ORDERs incl. the P0 Stripe fix (§3) |
| pokemon-mod-lab / gba-homebrew | NONE — parked by design | pokemon ORDER 003 unconsumed |
| codetool ×3 | NONE — wound down | safe-to-delete list in owner-queue |

Codex: **ENABLED fleet-wide on all 12 active repos** (owner, 2026-07-11 — ORDER
014, PR #54). Quota refusals = RETRY-LATER, never a wall (`projects/README.md`).

## 2. This session's arc (what the archive contains — all verifiable in git)

Boot #26 (ORDER 007, routine armed) → ender sweep + economics #27 + heartbeats
#28/#31 → launch-readiness #30 → Q-0265 continuous-mode adoption #33/#36 +
trigger cutover to the failsafe + send_later chain → chain slices
#37/#38/#44/#49/#50/#52/#53 (ORDERs 001–013 all DONE; roster gens 1–3;
review-queue drains; model matrix) → `projects/` registry #39 + gap-closure #42
(+ superbot #1967 frozen-copies banner) + UNIVERSAL #43/#45 → conformed games
mapping #46 (Q-0267 — answered by action: both seats booted) → permissions saga
(#48 clean parts; **owner grant `c23223f`** = UNIVERSAL.md v3; re-land
twice guard-held — §4) → Codex-everywhere #54 (ORDER 014 DONE, 015 filed) →
this close-out #55.

## 3. PENDING OWNER (the click-list at archive time — full detail: `docs/owner-queue.md`)

1. **venture-lab fresh session** — no trigger, no scheduler; 3 unconsumed ORDERs
   (002/003/004) incl. the **P0 Stripe fix** (review-queue #9: D1 defect
   confirmed at HEAD `7558cb2`); ⚑B/⚑D publish clicks stay FROZEN until it lands.
2. **superbot-plugin-hello push** — repo EXISTS but EMPTY (0 refs at 00:07Z
   ls-remote); the superbot-next seeded package push is the unblocked next step.
3. **Attended-session permissions re-land** — owner provenance `c23223f` is on
   main; the per-repo fold must be REBUILT and landed in an owner-attended
   session (§4). PR #47 is open at its born-red card only (`a4b736b`) — it never
   received the fold; use it as the re-land vehicle or close it with a reason.
4. **Games §5 veto window** — the conformed mapping's §5 details
   (`docs/proposals/games-program-mapping-conformed-2026-07-10.md`) stand
   accepted-by-boot; late veto stays open to the owner.
5. **Package paste wave** — owner-queue item 13, **HELD on §4** (paste the
   permissions-folded v2 texts, not the v1s, once the fold re-lands).

## 4. THE PERMISSIONS FOLD REBUILD RECIPE (critical — read before touching it)

**The built fold is LOST.** It existed only in the archived session's ephemeral
worktree/scratchpad, which died with that container. Two landing attempts were
held by the platform's instruction-poisoning guard (a standing permission grant
must be user-reviewed); **deny-wins — never retry around the guard**. The owner
then landed the canonical block himself: **`c23223f`** (UNIVERSAL.md v3, PR #51),
which explicitly directs the re-land citing that SHA. Rebuild = mechanical:

1. Take the `## Permissions & authority` block **VERBATIM** from
   `projects/UNIVERSAL.md` @ `c23223f` (grants: merge-own-green-PRs · trigger
   self-management · worker spawning; exclusions + deny-wins included).
2. Swap it into **all 13 `projects/<repo>/instructions.md`** (the full seat
   packages — not the archive metas), each citing `c23223f` as provenance.
3. **Re-base the 6 old retry passages to deny-wins** (they predate the doctrine
   and tell agents to retry around denials): gba, pokemon, superbot-games,
   trading **landing paths**; venture-lab **refusal branch + meta**;
   product-forge **merge-wall branch**.
4. Bump each touched instructions.md **v1→v2** (in-file stamp), companion
   one-liner in each `coordinator-prompt.md` where the old fold added one.
5. Keep every paste body **<7,500 chars** (Project Custom-Instructions limit
   headroom).
6. **Expect the guard again**: even citing `c23223f`, the guard will likely
   still require an **owner-attended session** (owner live in-chat = the
   user-review the guard wants). Schedule it as an attended slice; if held,
   record and stop — deny-wins.

## 5. ORDER 015 — reconcile note (do not re-author)

ORDER 015 (`control/inbox.md`, filed 00:45Z) asks for Seat A + Seat B founding
packages. **Reality overtook the filing: both seats SELF-BOOTED** (Seat B from
the superbot founding package `docs/planning/round3-founding-package-games-idle-2026-07-10.md`
+ the seeded lane-contract README; Seat A from its succession packs, failsafe
armed 23:47Z, order-001 branch in flight). **The remaining scope is registry
centralization, not authoring**: sweep what the booted seats ACTUALLY run
(prompts, failsafe texts, setup facts — via list_triggers + repo state) into
`projects/superbot-games/` + `projects/superbot-idle/` as v-stamped packages,
regenerate-don't-fork, and mark 015 DONE with that reading recorded. Flag the
reconciliation on the run report (decide-and-flag).

## 6. Known walls + transport catches (full ledger: `docs/capabilities.md`)

- **sim-lab tag-push 403** — `refs/tags` pushes (and GitHub Release creation,
  remote branch deletion) fail 403 through the proxy fleet-wide; branch pushes
  fine. Recorded on capabilities; kit-side release-route note owed at next kit
  contact.
- **git-proxy stale-clone-pack** — the proxy can serve **stale cached clone
  packs** (roster gen #3 caught 9/13 repos at hours-old HEADs on first clone).
  **Never trust a fresh shallow clone: verify `FETCH_HEAD == git ls-remote`
  and re-fetch until they match.** `tools/gen_roster.py` mechanization must
  inherit this step.
- Empty-repo first push fails through the proxy → use the Contents API
  (`push_files`) for commit #1. MCP repo scope + api.github.com are walled for
  brand-new repos from this seat (probe via `list_repos` + raw fetch instead).

## 7. Work ladder at archive (what the successor's first slices are)

After the trigger cutover (reboot-prompt step 2): heartbeat the takeover →
ORDER 015 reconcile (§5) → verify superbot-games `order-001-collection-scope`
merged (flips review-queue #16) → roster regen (due ~02:09Z) + parallel-run vs
superbot manifest (phase-2 decision) → next review-queue manager-verify
(pokemon#8 or gba#12) → @codex re-ask on superbot#1920 post-quota-reset →
`gen_roster.py` mechanization (with the ls-remote verify) → ORDER 010 per-lane
relay (+ trading#21 residue annotation). Standing duties: `control/status.md`
heartbeat as every batch's LAST step; born-red card per slice; REST squash on
green (R21); decide-and-flag; deny-wins.
