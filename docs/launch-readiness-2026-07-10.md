# Launch readiness — Q-0261 finalize-first relaunch (2026-07-10)

> **Status:** `reference` · compiled 2026-07-10 ~15:5xZ from the 5-worker sweep
> **Purpose:** the ONE committed checklist of everything to answer / click / fix /
> dispatch before each Project relaunches under the Q-0261 finalize-first order
> (manager → substrate-kit → superbot-next → Idea Engine → Product Forge → sixth
> seat → post-core lanes). Every item is classified **OWNER-CLICK** (only the
> owner's hands can do it), **AGENT-DOABLE** (an agent executes it — mapped to a
> boot or a routed ORDER in the routing table at the end), or **DECISION** (an
> owner ruling; each carries a recommendation).
> **Method:** 5 parallel research workers, 2026-07-10 ~15:10–15:40Z, reading each
> repo at its then-HEAD via git clones + the GitHub MCP. Evidence standard: git /
> API / live `list_triggers` state, **never lane self-reports alone** — every
> claim below carries its file@SHA / PR / commit citation from the reports.
> Reference HEADs: superbot `476228d4` · fleet-manager `e265fb1` · substrate-kit
> `bc468ac` (latest release v1.7.0 @ `93c7bdb`) · superbot-next `ec356d2` ·
> websites `d493792` · trading-strategy `465a67e` · venture-lab `af11bdb` ·
> superbot-games `7b3b77d` · pokemon-mod-lab `a76ada7` · gba-homebrew `b607365`.

**Two standing caveats (read once, apply everywhere):**

1. **The Q-0261 material is NOT on superbot main yet.** The Q-0261 router block,
   the revised dispatch-runbook §3, the three founding packages (Idea Engine ·
   Product Forge · substrate-kit) and `gen3-deployment-standard-2026-07-10.md`
   live ONLY on the unmerged superbot branch `claude/loving-brown-4ichgw` @
   `9b35fc46` — open **PR #1948** (ready, owner-attended dispatch session;
   `git grep Q-0261 origin/main` at `476228d4` returns nothing). **Merging
   #1948 is the first agent action of the round** — until it lands, the ruling
   this whole checklist executes is at risk of being lost with the branch.
2. **The repo-settings REST API is walled from agent seats.** Verbatim, hit
   identically by every worker on every repo (with and without
   `$GITHUB_TOKEN`; no `gh` CLI in the containers): `"GitHub access is not
   enabled for this session. An org admin must connect the Claude GitHub App
   for this organization."` Consequence: `allow_auto_merge` /
   `allow_update_branch` / `delete_branch_on_merge` / required-check lists /
   rulesets are **unreadable first-hand**; what IS verified is visibility,
   `archived`, and the `list_branches` `protected` flag (MCP), plus behavior
   (e.g. superbot auto-merge demonstrably fires on Code Quality). Settings
   claims below are marked secondhand where they rest on in-repo self-reports.

---

## Fleet-wide items (stated once, not repeated per repo)

### DECISION F-1 — do session-bound triggers survive chat archive?

Several standing wake routines are bound to a coordinator chat via
`persistent_session_id` (fleet-manager `trig_01QBrp5MjZL3F9mv6KsTXTzN`, kit-lab
`trig_01FnqnAQjLU2T8d16iHwWQ2h`, trading-strategy `trig_01Mvn5xRmqGmZJNRHgjqyLpN`
per `docs/succession/NEXT-BOOT.md@dfc52cf`). Whether archiving that chat kills
the trigger is **undeterminable from git or any agent surface** (the trigger
record carries no archive semantics; no doc records a test; kit's trigger kept
firing after its lane declared "closed", but closed ≠ archived).
**RECOMMENDATION (one decision, covers the fleet): each new seat self-arms its
own trigger at boot, then `delete_trigger` the old one** — the recipe is proven
(websites ORDER 008, trading ORDER 006/PR #32, kit ORDER 010; `create_trigger`
is agent-callable, account-owned) — zero owner clicks and no reliance on
undefined platform behavior. websites is already archive-immune by construction
(fresh-session-per-fire, `control/status.md@c41d138`); the product-lanes report
adds a free experiment: archive anyway and watch trading-strategy's 16:00Z fire
— if no fresh heartbeat by ~20:15Z, the gen-2 boot re-arms with
`create_new_session_on_fire=true`.

### Kit-version table (latest release: v1.7.0 @ `93c7bdb`, published 2026-07-10T06:38:59Z)

v1.7.0 is a non-breaking MINOR (`breaking=false state_migration=false
min_upgrade_from=1.0.0`). **Every upgrade below is AGENT-DOABLE and rides the
repo's own next boot/session** — no owner action anywhere in this table.

| repo | pinned kit | behind | note |
|---|---|---|---|
| superbot | 1.0.0 | — (vestigial) | pin set when the in-tree kit graduated (#1878–#1884); no bootstrap.py/control/ — never operationally adopted (`substrate.config.json@476228d4`) |
| trading-strategy | 1.1.0 | 6 MINOR | oldest live pin; no `kit:` status line at all (`substrate.config.json@ddaedc5`) |
| superbot-games | 1.2.0 | 5 MINOR | v1.7.0's `adopt --lane` is the upstream fix its standing two-writer ⚑ asked for |
| fleet-manager | 1.4.0 | 3 MINOR | misses order-bus enforcer #87, claim-aware checker #90, OA↔CAPABILITIES xref #98, adopt --lane #103, telemetry #91, #86/#95/#99 fixes |
| websites | 1.6.0 | 1 MINOR | `substrate.config.json@f4b998f` |
| venture-lab | 1.6.0 | 1 MINOR | upgrading clears its one standing advisory (fixed upstream in kit #99) |
| pokemon-mod-lab | 1.6.0 | 1 MINOR | `control/status.md@157ecd9` |
| gba-homebrew | 1.6.0 | 1 MINOR | v1.7.0 ships this repo's own field-reported gate fixes (kit #95/#99) |
| substrate-kit | 1.7.0 | current | it IS the kit; `kit: v1.7.0 released` (status @bc468ac) |

### The settings-API wall

Caveat 2 above, restated as a standing finding: any repo-settings sweep
(auto-merge toggles, required checks, up-to-date rules, branch auto-delete) is
**owner-eyes-only** — agents can neither read nor write those surfaces
(matches kit friction issue #36 report 3; the owner decision sheet's §4.9
repo-settings sweep exists exactly for this). Where a required check is
claimed below, the evidence class is stated (behavioral / in-repo self-report).

---

## Seat 1 — manager / fleet-manager (LIVE)

**Verdict: READY (seat LIVE since ~13:45Z; carried debt: 2 OWNER-CLICK + 2 DECISION, none gating; ORDERs 001/002/003/007 open, all AGENT-DOABLE riding wakes).**

- **Live state:** `control/status.md` fresh at 14:58Z (post-first-standing-wake,
  PR #28/`e265fb1`). Routine **live-verified, not self-report**:
  `trig_01QBrp5MjZL3F9mv6KsTXTzN`, cron `30 */2 * * *`, `enabled=true`,
  `last_fired_at=2026-07-10T14:36:29Z`, `next_run_at=16:31:17Z` (this session's
  own `list_triggers` ~15:10Z). 0 open PRs, only `main` (protected), no stale
  claims.
- **Open ORDERs (all AGENT-DOABLE):** **001** (blueprint P1–P11 + D4/D5/D6,
  init-prompt-universal rewrite — `init-prompt-universal.md:14` still carries
  the false routine promise at HEAD — and manager MISSION.md, absent per
  `git ls-tree`); **002** (fleet-manifest re-stamp — the planned 16:3xZ wake
  slice); **003** (review-queue auto-append rule + named drainer —
  `docs/review-queue.md` has zero rows against a 116-PR autonomous night);
  **007** (mint the @codex review-relay rule, Q-0258). 001/003/007 ride the
  manager's next doctrine session; 002 the next wake.
- **Gap found live:** `list_triggers` shows NO trigger for venture-lab,
  pokemon-mod-lab, or gba-homebrew despite the dispatched self-arm ORDERs —
  AGENT-DOABLE, next manager wake verifies those three lanes' arm ORDERs
  (owner fallback only on a recorded error, per owner-queue item 7's own rule).
- **OWNER-CLICK (non-gating):** account-wide visibility review (parked by the
  owner's own queue; fleet-manager incl. the owner-queue is public —
  `private:false` API-verified) · fleet-wide stale-branch deletion is counted
  under the settings sweep (fleet-manager itself is clean).
- **DECISION:** F-1 above applies to this seat's own trigger at its eventual
  relaunch (re-arm-then-delete, self-service) · the 8 undeployed instruction
  packages — recommendation (already the decision sheet's §4.8): don't paste
  today; re-base on the gen-3 blueprint delta, deploy in one sitting.
- **Also rides any manager session:** kit upgrade 1.4.0 → 1.7.0; handoff-doc
  drift (`docs/handoff-2026-07-10.md` shows ORDER 004 open — DONE as #27;
  cosmetic, HEAD-wins rule covers it).

---

## Seat 2 — substrate-kit (FIRST relaunch)

**Verdict: BLOCKED-ON-10 (8 OWNER-CLICK + 2 DECISION). Boot-gating subset: OA8 setup-script paste + the routine-rebind DECISION; F-5 (OA1, HOT) gates the seat's dispatch though not the boot mechanically.**

Read at main `bc468ac`. Phase: **closed / handoff-ready** (gen-2 session CLOSED
2026-07-10; boot from `docs/gen2/next-boot.md` §0; health green — 819 tests,
`check --strict` exit 0, dist byte-pin clean). Orders 001–010 all acked+done.
Kit at v1.7.0 (current — it IS the kit). Open PRs: 0.

**Q-0261.3 write-all rider + scope guard (the seat's calibration must recite
this):** substrate-kit gets **write access to ALL fleet repos** — the second
Q-0260 exception (manager = read-everywhere oversight; kit = write-everywhere
distribution) for kit upgrades + regenerating kit-owned conventions fleet-wide.
**Hard scope guard, owner-stated:** it must NOT take on other repos' tasks —
lane-repo writes restricted to **kit distribution only** (upgrade PRs, kit-owned
convention regeneration, adoption fixes); never lane domain work, never another
lane's inbox/status. Env: attach ALL fleet repos. Package:
`round3-founding-package-substrate-kit-2026-07-10.md` @ `9b35fc46` (branch-only
until #1948 merges — caveat 1). Source: router Q-0261
(`docs/owner/maintainer-question-router.md@9b35fc46` line 9410) + runbook §3
item 2.

**Boot-gating items:**

1. **OWNER-CLICK — OA8 setup-script paste (gen-2 variant).** Claude console →
   kit environment settings → Setup script field → paste `docs/gen2/setup.sh`
   verbatim. The current script killed a session AT PROVISIONING (PR #47
   casualty: `fatal: not a git repository` + hard-fail on missing
   requirements.txt); agents cannot read or write the settings dialog. The one
   item that can kill the fresh boot itself — do BEFORE the first session. If
   already pasted, the owner says so and the ask is withdrawn (agents can't
   confirm). Effort: 1 paste. Evidence: OA8 @ status.md `bc468ac`.
2. **OWNER-CLICK — OA1, F-5 one-letter ruling (A or B) — HOT.** Reply "A" or
   "B" in any channel; context
   `docs/ideas/rubric-f5-none-regressing-wording-2026-07-09.md`;
   **recommendation on the decision sheet: Reading A.** Run-4 is
   ruling-independent (FAIL both readings) but the ruling flips runs 2–3 (trend
   headline A: 1 PASS/3 FAIL vs B: 3 PASS/1 FAIL), and **B1 run-5 WAITS on it**
   (next-boot §0 non-derivable context) — the seat's HOT dispatch gate
   (owner-queue item 1: "kit-lab's dispatch is paused on it"). v1.7.0's own
   release notes carry the dispute ("disputed pending the F-5 wording ruling").
   Effort: 1 letter.
3. **DECISION — routine rebind (fleet-wide F-1 applies).**
   `trig_01FnqnAQjLU2T8d16iHwWQ2h` (hourly, cron `0 * * * *`) is bound to the
   OLD kit-lab coordinator chat (`session_01Gb1Dq9vgeNkTyBPvvPqTrj`) and still
   live-firing (`last_fired_at=15:08:09Z`, verified via `list_triggers` ~15:10Z
   — the earlier "externally stopped 12:54Z" relay was wrong; the #124
   correction is right). Per F-1: **the new seat re-arms its own routine first
   (recipe proven, ORDER 010 record), then `delete_trigger` the old one** —
   zero owner clicks. Only then archive the old chat.

**Rides the fresh seat's first boot (AGENT-DOABLE):**

- **queue-state.md drift, one-line fix:** `docs/gen2/queue-state.md` "Next-run
  resume points" still ends "ROUTINE STATE: NOT ARMED … EXTERNALLY STOPPED
  12:54Z … nothing fires this Project on its own clock right now" — written at
  #122, contradicted by the #124 correction in status.md/next-boot.md AND the
  live 15:08Z fire. next-boot's "re-verify before believing NOT-ARMED" clause
  defuses it, but the false line sits in one of the three named resume docs —
  strike/correct it first boot (docs-only).
- **OA3 (P4 daily lab loop) — ATTEMPT before treating as owner-only:** status's
  own correction note says try `create_trigger` **fresh-session mode**
  (`create_new_session_on_fire=true`, cron `0 6 * * *`); websites' 13:49Z
  trigger proves fresh-session-per-fire arming works from a lane seat. Owner
  click only on a recorded refusal.
- **OA6 re-scope/withdraw — stale as written:** substrate-kit is ALREADY
  `private:false / visibility:public` (API-verified this pass); the recorded
  wall was the per-SESSION repo allowlist, not visibility, and the documented
  workaround (add_repo / raw read) already works. Fresh seat rewrites the ask
  (residue: fleet environments listing kit in their session allowlists, only IF
  cross-repo MCP reads are wanted over raw fetch).
- **Friction issues #36–#39 triage** (all 4 OPEN, labeled `friction`): #36's
  reports 1–2 SHIPPED as kit #86/#87; report 3 (required-check-blindness wall)
  still true — disposition-comment/close per founding plan §9.1. #37/#38/#39
  (superbot PL-011, superbot-next gate-workflow half, websites
  regeneration-lag checker) — ordinary kit lane / lane repos.
- Resume priorities from next-boot §0: SessionStart handoff-push idea (top
  buildable) · T5 guard-probe re-scope (pin path → daytime `do-not-automerge`
  PR; owner click only at ratification) · model-identity capture check.
- **Legacy-alias job delete WAITS for OA2** — deleting first would wedge every
  merge.

**OA-list dispositions (remaining ⚑ rows, from status.md@bc468ac):**

| item | class | disposition |
|---|---|---|
| OA2 P10 required-check swap | OWNER-CLICK | Settings → Rules → `main` ruleset: REMOVE "Kit test suite" + "Cold-adoption smoke", ADD `kit-quality`, set "Require branches up to date" OFF. Ends the ~35-min queue-stall class + behind-stall (live-hit #107; gen-1 ~70 min lost). First-day friction killer — pairs with OA11 (pick ONE of the two toggles). 2 min. |
| OA4 P5 Railway project | OWNER-CLICK | New project `kit-lab`, europe-west4, scoped token into env. Not boot-gating. ~5 min. |
| OA5 P8 confirm MIT | OWNER-CLICK | one word ("MIT ok"); repo already serves LICENSE=MIT — formalization. 5 s. |
| OA7 superbot pin | DECISION | upgrade superbot's deliberate v1.0.0 pin? Recommendation (on file): adopt at next stable in one hop; **owner silence = accept** — no click required. |
| OA9 self-merge permission rule | OWNER-CLICK (optional, LOW) | blocks nothing (enabler workflow covers it). |
| OA10 branch cleanup + auto-delete toggle | OWNER-CLICK (hygiene, non-blocking) | **46 stale non-main branches, 0 open PRs** (live count this pass); deletion 403 on every agent path (a full session attempted, deleted zero). 1 checkbox + clicks. |
| OA11 "automatically update branches" | OWNER-CLICK | companion/alternative to OA2's up-to-date-OFF; doing OA2 makes this moot. |
| OA12 websites ORDER 005 relay | AGENT-DOABLE | **executor: fleet-manager coordinator** (routing lane ORDERs is the manager's core function; the "owner-routed" framing predates the standing wake). Folds into the next manager wake. |

---

## Seat 3 — superbot-next (Builder)

**Verdict: BLOCKED-ON-4 (3 OWNER-CLICK + 1 DECISION, where the flag-13 click+decision collapse into one one-line owner "accept"). One AGENT-DOABLE item gates the boot loop itself: ORDER 008 is unacked/unexecuted and NO Builder trigger exists — it rides the boot (ack → create_trigger → heartbeat).**

Read at main `ec356d2`. Phase: band-5 BUILD+REPLAY landed (#95/#97), next =
band-5 live-drive then band-6 (games). Heartbeat **stale ~14 h**
(`control/status.md@4318207`, 01:05Z) and pre-dates ORDER 008; sessions #99/#101
committed after without an ender — **ENDER-MISSING confirmed**. 0 open PRs; kit
v1.6.0 (one MINOR behind).

**Boot-gating AGENT item — ORDER 008 (P0, self-arm the wake routine).**
`control/inbox.md@ec356d2` (landed #100/`04436ab` 12:05Z): "SELF-ARM YOUR WAKE
ROUTINE … create_trigger (cron every 2 hours; stagger to even hours :00) …
REQUIRED RECORD: the EXACT create_trigger call … or the VERBATIM denial."
Status: **`new` — unacked, unclaimed, unexecuted**; cross-verified against the
account trigger list: **no Builder trigger exists** (standing routines =
fleet-manager, websites, trading-strategy, kit-lab only). Until it runs the
Builder seat has no wake mechanism. Rides the boot: first wake = ack + execute
ORDER 008 + heartbeat catch-up ender for #99/#101.

**OWNER-CLICKs (finalize-first debt):**

1. **flag-13 corpus-red disposition ruling** — per-class accept/exempt/normalize
   for the 3 old-vs-new output classes. Blocks ORDER-004 item 2, every parity
   pending→ported flip, and the `report` CI leg. **Recommendation (launch pack
   §4 item 5 @ `476228d4`): the owner simply accepts the lane's own proposed
   disposition — a one-line yes.** (The paired DECISION on content is already
   pre-chewed the same way — Q-0240 class, reversible at the parity gate.)
   Evidence: OWNER-ACTION 1 @ `4318207`.
2. **Create the `superbot-plugin-hello` repo** (github.com/new, public, no
   template) — agent repo-create verified 403
   (`docs/retro/project-review-2026-07-09.md` §2 item 2). Blocks ORDER 002's
   done-when + the game-Projects' reference plugin pattern. 1 min.
3. **Relax the require-up-to-date merge rule (or enable merge queue)** —
   rulesets admin-only; every session loses time to the update-branch dance
   (#86/#87 stranded). Directly degrades an unattended 2-hourly Builder loop.
   2 min. Evidence: OWNER-ACTION 3 @ `4318207`; part of the §4.9 sweep.

**Also rides boot / routed:**

- **Encode Q-0259 ruling 3 (standing @codex review on substantive Builder PRs)
  via a manager ORDER** — `grep -ri codex control/ docs/` returns nothing; the
  rule hasn't reached this repo. Executor: fleet-manager (routing table below).
- Kit 1.6.0 → 1.7.0 (v1.7.0's inbox append-only enforcer + claim-aware checker
  are directly relevant to this repo's order bus).
- Delete-list the stale `status/heartbeat-2026-07-09-band1` branch in the ⚑
  block for the owner sweep (content-superseded by #94/#98; deletion = 403 wall).
- Settings context (secondhand): the owner's "6-check ruleset" stands; the
  staged substrate-gate.yml deliberately NOT installed (ci.yml already runs
  `check --strict`). Exact required-check list unreadable (caveat 2).

---

## Seat 4 — Idea Engine (superbot repo)

**Verdict: BLOCKED-ON-2 for the boot itself (1 OWNER-CLICK: create the Project + paste the founding package; 1 DECISION inherited: none — but merge of PR #1948 is the AGENT prerequisite). Repo-wide roll-up from the report: BLOCKED-ON-6 (4 OC + 2 DEC), most counted under their owning lanes here.**

Read at main `476228d4` (fresh — 42nd Q-0107 recon pass merged same hour).
No stale claims; `docs/owner/review-inbox.md@2166c532` zero rows; the repo's
own reconciliation loop self-fires (issue #1951).

**Owner gate — create the Project + paste the founding package.** claude.ai →
New Project on menno420/superbot → paste Custom Instructions (§1, ~4,300 chars)
+ chat brief (§2) from
`docs/planning/round3-founding-package-idea-engine-2026-07-10.md` @ `9b35fc46`
(branch-only — caveat 1) → select the **existing `superbot` environment** (zero
env work by design, runbook §3.4). Project creation has no agent API surface
(verified wall). ~5 min, AFTER #1948 merges.

**The package seeds `control/` at first boot** — superbot has **no control-bus
convention at HEAD** (no `control/`, no bootstrap.py — verified `git ls-tree`);
the package's decide-and-flag design (a): the Idea Engine seat seeds and solely
writes `control/status.md` + `control/outbox.md` at first boot; proposals travel
via outbox to the manager, never other repos' inboxes. So the repo-side gap
**rides the seat's own boot**.

**Merge PR #1948 first (AGENT)** — the only open PR (#1948, ready, head
`e6d38e49`, owner-attended dispatch session; born-red card holds the merge).
Carries Q-0260/Q-0261 + all three founding packages + the gen-3 standard.
First agent action of the round (caveat 1).

**Q-0259 open items at HEAD** (launch pack §4b parenthetical @ `476228d4`):
F-5 (item 1, counted under seat 2) · the settings sweep (9) · the holdout
unlock ORDER (2 — granted in principle, needs the inbox ORDER naming the
protocol doc; routed below) · the venture clicks (10, counted under
venture-lab). Open DISCUSS Qs: **Q-0255** (two stale kit pointers; the
CLAUDE.md half needs owner live-review) and **Q-0257** (dependabot arming —
recommendation on file: status quo + Q-0256; not launch-gating).

**Branches note:** **555 heads (554 non-main)** — stale merged `claude/*`
leftovers; recon passes report "no stale session PR" so unmerged-work risk is
low but unverified per-branch; **deletion walled** (agents 403 on ref deletes;
launch pack §4 item 9 carries the fleet-wide delete ask). Vestigial kit pin
v1.0.0 (see table); adoption of a real release is any-session work and what
retires the pin.

---

## Seat 5 — Product Forge (PRE-BIRTH)

**Verdict: BLOCKED-ON-3 (3 OWNER-CLICK — the repo/Project/required-check seed set; everything else rides its boot).**

The repo does not exist. Launch pack §5 (`round3-launch-pack-2026-07-10.md@476228d4`
lines 311–354): **NEW dedicated repo + Project (`product-forge`), born-right per
the gen-2 blueprint**; owner-corrected 2026-07-10: NOT venture-lab (that lane
stays a revenue-focused manual specialist). Mission: take routed ideas, build
finished shippable products end-to-end.

**Expected-seed checklist (founding package §0 @ `9b35fc46`, branch-only —
caveat 1):**

1. **OWNER-CLICK — create the `product-forge` repo** (public, empty, default
   branch `main`) — repo creation is a verified agent wall.
2. **OWNER-CLICK — create the Product Forge Project** in claude.ai/code, attach
   the repo, paste the founding package (born-right ORDER 000 = blueprint §1
   seed: walking skeleton through the full merge path in the first 20 minutes).
3. **OWNER-CLICK — post-seed required-check click:** after the forge's seed PR
   adds CI, tick *Allow auto-merge* + make the substrate gate / smoke check
   **required** — ORDER 000's report names the exact check and asks once,
   click-level (required check from day 1 so auto-merge works).

**Design decisions already made in the package (decide-and-flag, no owner ask):**
products one-per-subtree (`products/<slug>/`, no cross-product imports,
codetool-labs pattern) · env = `product-forge` repo only on
`archetype-python-lab.sh` · cadence `0 */2 * * *` · Q-0259 r.4 money protocol
baked in (a spend is never executed).

**No environments-registry spec exists yet** — `environments/archetypes.md@e265fb1`
has no `product-forge` row (repo not created). **AGENT-DOABLE: the manager
writes the spec after the repo exists** (python-lab archetype per the package;
routing table below). Everything else — ORDER 000, self-armed routine,
control-bus seed — rides the forge's own first boot.

---

## Seat 6 — sixth core seat (TBN)

**Verdict: BLOCKED-ON-1 (1 DECISION — the owner names the seat; nothing else can start until then).**

Q-0261.1 (@ `9b35fc46`) + runbook §3 item 6: the owner names the sixth standing
seat; candidates = **hub-superbot** (games/maintenance seat) or **websites**.
Package drafted once named.

**RECOMMENDATION: hub-superbot** — the hub carries the ideas pipeline, router,
ledger, and reconciliation machinery every other core seat depends on, and it is
the only core repo without a standing wake, whereas websites already runs armed
as a manual lane (4-hourly fresh-session trigger, archive-immune). One line why:
pick hub-superbot if the goal is bot-product velocity and keeping the system's
roots self-maintaining — which is exactly Q-0261.4's stated intent ("depth over
speed for the system's roots"); pick websites instead only if the goal is a
self-sustaining product loop, and websites' working routine means that loop
already runs without a core seat.

---

## Post-core lanes (pipelined gen-3 standard per Q-0261.4)

### 7. websites

**Verdict: BLOCKED-ON-3 (3 OWNER-CLICK, 0 DECISION) — none gate the boot; boot-level effectively READY.**

Read at HEAD `d493792`. Orders 001–008 all done (`control/status.md@c41d138`,
13:56Z, spot-verified: ORDER 005 = PR #53; ORDER 008 = PRs #56/#57/#58). Routine
**ARMED, fresh-session-per-fire** (`trig_017H9Qb9oxtLgUy6sw2gnSHg`, `0 */4 * * *`,
armed 13:49:36Z) — first fire due 16:00:31Z; first routine-woken heartbeat IS
the verification (rides the boot; conditional owner fallback self-expires).
Archive-safe by construction (F-1). Next-boot brief current
(`docs/planning/queue-state-2026-07-09-winddown.md` § gen-2 addendum, PR #57).
Kit 1.6.0. Required check `quality` on main (secondhand: OWNER-ACTIONS.md
decided row A; verified live via PR #18 `mergeable_state=blocked` per the doc).

- **OWNER-CLICK (conditional, self-expires):** arm external 4-hourly wake ONLY
  if no heartbeat by 2026-07-11 (`OWNER-ACTIONS.md@cb074e4` ask 1).
- **OWNER-CLICK:** provision botsite Postgres + `DATABASE_URL` (Railway →
  superbot-websites; /submit is a labeled stub without a store; D-0005 forbids
  agent Railway mutations). ~3 min.
- **OWNER-CLICK:** fine-grained PAT → control-plane `GITHUB_TOKEN` (lifts the
  anonymous 60 req/h ceiling; lights admin cells + /owner re-run; pages already
  live tokenless). ~5 min.
- **AGENT-DOABLE (rides next websites session):** kit 1.6.0 → 1.7.0 ·
  disposition of `claude/rework-dashboard` @ `a0b459f` — tip = head of PR #9
  **CLOSED-UNMERGED** (env-var-name scrub + template denylist test; small real
  hardening loss if not re-landed elsewhere — 2-min re-check) · 3 other stale
  branches (`claude/wire-github-token-docs` superseded-by-intent;
  `manager/control-plant` landed elsewhere; `claude/harden-verify` tip has
  post-merge commits — verify before the owner deletes; deletion owner-walled).

### 8. trading-strategy

**Verdict: BLOCKED-ON-5 (4 OWNER-CLICK + 1 DECISION — the DECISION is fleet-wide F-1, counted here because this repo's trigger is the exposed one). Only the P5-unlock click gates the remaining roadmap, and it sequences BEHIND agent ORDER 007; the boot itself is not gated (parked green).**

Read at HEAD `465a67e`. Phase PARKED GREEN, owner-gated
(`control/status.md@bad297f`, 13:47Z; close-out PR #34). Routine ARMED AND
RECURRING (`trig_01Mvn5xRmqGmZJNRHgjqyLpN`, `0 */4 * * *`, confirmed fires
04:08/08:00/12:00Z) **but session-bound** (`NEXT-BOOT.md@dfc52cf`) → F-1's
watch-the-16:00Z-fire experiment lives here. Briefs current (NEXT-BOOT.md +
QUEUE.md@d84a2aa, all 8 queue items DONE-stamped). 0 open PRs, only `main` —
cleanest repo in the sweep. Kit **1.1.0** (6 behind, no `kit:` line).

- **AGENT-DOABLE (rides the gen-2 boot, FIRST):** **ORDER 007** (P1, acked,
  parked-open — promotion-significance bar with test + honest AAPL-donchian
  re-grade (+0.079 Sharpe vs ~0.19 SE ≈ 0.4σ; expected DEMOTE) + ledger entry;
  `control/inbox.md@bcd0a70`). **It gates any holdout use and precedes P5;
  holdout stays SEALED throughout** (verified: no holdout_unlocked marker, all
  ledger rows data_end ≤ 2025-01-08, QUEUE.md item 8). Then kit 1.1.0 → 1.7.0
  + add the missing `kit:` line.
- **OWNER-CLICK — P5 holdout-unlock ORDER:** append an ORDER to
  `control/inbox.md` **explicitly naming `docs/p5-holdout-protocol.md` as
  binding** — protocol §7 forbids inferring authorization from anything less.
  Blocks `docs/final-report.md` §Holdout, the lab's terminal deliverable.
  **Sequence AFTER ORDER 007 completes**; QUEUE.md: dispatch a fresh dedicated
  session (not the protocol author) to run it. Note: §4b @ `476228d4` records
  the unlock as "granted in principle" — the manager can draft the ORDER
  decide-and-flag (routing table), with the owner's one-line confirm as the
  veto window.
- **OWNER-CLICK:** paste `environments/setup-universal.sh` into the Project
  env setup-script field (fresh-env sessions die silently at provision without
  it; pinned env works meanwhile). ~1 min.
- **OWNER-CLICK:** tick "Allow auto-merge" (secondhand: arm fails pending-side
  "unstable status" with the toggle off; REST squash-on-green worked for every
  merge — non-blocking). ~30 s.
- **OWNER-CLICK:** archive the dead gen-1 "ORDER 001 successor" session (DOA at
  provision, still lists active). ~30 s.

### 9. venture-lab

**Verdict: BLOCKED-ON-5 (4 OWNER-CLICK + 1 DECISION) — the boot is NOT owner-gated; sharpest state-risk in the fleet: the heartbeat the fresh Project reads is stale-by-design until ORDER 004 executes, and ⚑B/⚑D are FROZEN pending agent ORDER 003.**

Read at HEAD `af11bdb`. `control/status.md@a22b403` **STALE (04:57Z — oldest
live-lane heartbeat)**: still says "PR #9 awaiting owner merge" but **#9 MERGED
05:11:50Z** (squash `95b755b`) — the buyer zips ARE on main. Routine **NOT
ARMED**. **Three unexecuted ORDERs** (`control/inbox.md@f999ddf`): **002**
(self-arm hourly wake), **003 (P0 — fix the real Stripe path D1/D2/D3**:
`customer_details.email` vs null `customer_email`; invalid `{CHECKOUT_EMAIL}`
success-URL placeholder; vendored real Stripe payloads, never synthesized;
zip rebuild via `package.sh`), **004** (gen-2 archive ender: re-stamp
heartbeat, ack 002/003, write the next-boot brief — no succession file exists
on main, verified). All three **ride the fresh boot** (004 names itself the
boot task). Review-queue: 1 stale row (post-merge re-check of #9's
zips/copy/transcript — now actionable). Kit 1.6.0 (upgrade retires its one
standing advisory, fixed in kit #99). 0 open PRs, only `main`.

- **OWNER-CLICK — ⚑A Stripe TEST keys** (`sk_test_…` → `STRIPE_SECRET_KEY`,
  `whsec_…` → `STRIPE_WEBHOOK_SECRET` in `candidates/membership-kit/server/.env`)
  — not frozen; unblocks the live test-mode purchase→webhook→grant E2E. ~10 min.
- **OWNER-CLICK — ⚑B publish membership-kit $49: ❄️ FROZEN.** Do NOT click
  until ORDER 003's done-when is met (merged + real-path HTTP test green +
  status notes "⚑B/⚑D unfreeze requested" + manager relays per playbook R23).
  Evidence: inbox@f999ddf ORDER 003 ("the headline claim has never executed
  against real Stripe … 13 green tests inject synthetic events authored from
  memory").
- **OWNER-CLICK — ⚑D publish template-packs $19 PWYW: ❄️ FROZEN** (same gate;
  the $59 bundle additionally needs ⚑B+⚑D live URLs).
- **OWNER-CLICK (optional) — ⚑C** Supabase + Discord accounts (production
  stack only).
- **DECISION — self-landable merge path:** make `substrate-gate` a required
  check (owner click, gives auto-merge a pending window) OR let the agent
  commit a `GITHUB_TOKEN` merge-on-green workflow (modeled on kit's enabler)?
  **Recommendation: (b) the workflow — agent-doable on the fresh boot, no owner
  click, proven pattern**; the session proved a green `clean` PR is
  agent-unlandable here (two verbatim classifier denials + 0 required checks,
  `PLATFORM-LIMITS@4c1b1c2`).

### 10. superbot-games

**Verdict: BLOCKED-ON-4 (3 OWNER-CLICK + 1 DECISION) — PLUS the flagged AGENT gate: ORDER 001 (CI collects 73 of 121 tests) should be the fresh boot's first act before any lane trusts a green gate; and the repo relaunches CLOCKLESS unless the boot self-arms or the manager dispatches the self-arm ORDER (none was ever sent here).**

Read at HEAD `7b3b77d`. Per-lane status model: mining gen-1 complete green
(@b0541bf), exploration `archived-pending-gen-2` (@7d9663f, close-out 13:47Z).
**Neither lane has a wake routine and no self-arm ORDER exists in the inbox**
(inbox@41ad682 contains only ORDER 001) — the only surveyed repo with no clock
and no order to build one. Kit **1.2.0** (5 behind — and v1.7.0's
`adopt --lane` + `heartbeat_files` is the upstream fix for this repo's standing
two-writer ⚑). 0 open PRs; 2 stale branches (`mining/adopt-substrate-kit`
closed-unmerged-deliberate; `mining/grid-encounters` tip ≠ merged head —
verify before deleting; owner-walled).

- **AGENT-DOABLE (P0, arguably boot-gating) — ORDER 001 CI collection fix:**
  gate still runs exactly `python3 -m pytest tests/ -q`
  (`.github/workflows/substrate-gate.yml@989cfa3`) — `games/exploration/tests/`
  (48 tests) invisible, no collected-count assertion; unacked at HEAD (both
  close-out heartbeats merged after dispatch, neither acks). Done-when: gate
  green with 121+ collected + `orders: acked=001 done=001`. The exploration
  resume item (P2 survival sim) builds exactly in the ungated tree.
- **AGENT-DOABLE:** kit 1.2.0 → 1.7.0 lane-aware migration (resolves the
  two-writer ⚑ agent-side, owner veto stays available) · wake-routine self-arm
  (capability fleet-verified; the in-repo "owner creates the routine" ask
  @7d9663f predates the self-arm verification — **supersede it, don't convert
  it to a click**; ORDER routed below).
- **OWNER-CLICK:** paste gen-2 Custom Instructions into the relaunched
  Project(s) — `docs/gen2-custom-instructions-exploration.md` §B + mining twin
  `docs/retro/proposed-custom-instructions-mining-2026-07-09.md`; agents cannot
  edit Project settings. ~2 min × 2 lanes.
- **OWNER-CLICK (optional):** stale-branch deletion (above; agents 403).
- **OWNER-CLICK (cross-repo):** email Part 1 answers + send decision
  (superbot `docs/eap/gen1-wrapup-email-part1-questions-2026-07-09.md`) —
  gates the gen-1 wrap-up send, not this repo's boot.
- **DECISION — two-writer aggregate status vs kit:** take the v1.7.0
  `adopt --lane` upgrade or formalize the aggregate as manager-written-only?
  **Recommendation: upgrade to v1.7.0 lane-aware adopt** — the upstream fix the
  ⚑ asked for shipped today and keeps the per-lane model without local
  convention debt.

### 11. pokemon-mod-lab

**Verdict: READY — relaunch-ready with two queued orders (002, 003) consumable at first boot; carried: 2 OWNER-CLICK + joint-pick DECISIONs, none blocking the first session. Note: no routine armed → the FIRST relaunch session must be fired by the coordinator/owner; ORDER 002 then removes the dependency.**

Read at HEAD `a76ada7`. **PRIVATE — confirmed** (`"private":true` via API
~15:12Z; the URGENT night-review Q16 flip HAS happened; Nintendo-decomp
exposure closed). Phase LANE PARKED (@157ecd9: sessions 001–008, PRs #2–#10
merged, 12 QoL patches shipped, queue exhausted). Kit 1.6.0. No stale
branches, 0 open PRs. Next-boot brief current (session-008 ender `b5b8ed6`).

- **AGENT-DOABLE (ride the boot):** **ORDER 002** (self-arm hourly wake,
  appended `a17be86` 11:11Z — unacked/unexecuted) · **ORDER 003** (verify
  visibility=private + standing R22 guard, appended `a76ada7` 12:56Z —
  effective now the flip is verified; status lacks the
  `visibility: private — verified <ts> via <surface>` line) · kit 1.6.0 → 1.7.0.
- **OWNER-CLICK:** make `ROM builds` a required status check (Settings → Rules
  → `main` ruleset; merges currently gate on convention — a red ROM build could
  technically merge; REST merge-on-green convention works meanwhile). ~1 min.
  Evidence: ⚑ OWNER-ACTION 1 @157ecd9.
- **OWNER-CLICK:** playtest verdict (keep/revert/tune) on the 4 game-feel
  patches — instant text (#4), auto-run invert-B (#6), HP-bar drain 3× (#7),
  battle message waits ×0.5 (#7); ROM sha1 `c0c08dc5…` after #10. Clears 6 of
  the 8 review-queue rows (`docs/review-queue.md@c2c130b`; rows #2/#8 are
  agent-reviewable). ~20–30 min.
- **DECISION (joint with Track B):** concept pick — Emerald QoL+ / Emerald
  Hard / Nuzlocke. **Recommendation: Emerald QoL+** (the lane's own; 12 shipped
  patches already form its baseline and stay reusable under any pick).
- **DECISION (Q-0259 r.5 mapping):** do the 3 game projects get NEW dedicated
  repos, or do pokemon-mod-lab / gba-homebrew continue as 2 of the 3?
  **Recommendation: keep pokemon-mod-lab as the Emerald-mod project's repo**
  (12 merged patches + vendored toolchain + private rail are heavy sunk
  infrastructure; repo identity carries the legal rail + CI + proof chain);
  spin new repos only for concepts that leave these codebases.

### 12. gba-homebrew

**Verdict: READY — one queued order (002) consumable at first boot; healthy green close-out; owner items are direction/taste, not blockers. Same clockless-first-session caveat as Track A.**

Read at HEAD `b607365`. PUBLIC by design (PLATFORM-LIMITS rail: nothing
Nintendo-derived may enter). Phase: session 7 COMPLETE — **Lumen Drift
SCOPE-COMPLETE** (@67491e8; close-out merged via PR #24). Kit 1.6.0 — v1.7.0
ships this repo's own field-reported substrate-gate fixes (kit #95/#99),
upgrading closes its own loop. 0 open PRs, single branch.

- **AGENT-DOABLE (ride the boot):** **ORDER 002** (self-arm hourly wake,
  appended `b607365` 11:13Z — unacked/unexecuted) · kit upgrade · work the
  **11 outstanding review-queue rows** (`docs/review-queue.md@6755044`: #3, #5,
  #6, #8, #9, #12, #13, #16, #17, #20, #23 — all agent re-check/review work,
  no owner surface).
- **OWNER-CLICK:** play Lumen Drift (~15 min; scope-complete game with zero
  owner eyes on it; informs the concept pick). Build from `main` @
  `f502147`-or-later; concept + controls in
  `docs/concepts/session-1-concepts.md`.
- **DECISION (joint pick, Track B):** Lumen Drift more-scope / Clockwork
  Courier / Shoal. **Recommendation: treat as a pure fork on product taste** —
  everything generic transfers (games/common engine + harness + CI), zero sunk
  work lost; if the owner is silent at relaunch, the coordinator directs
  review-queue + kit-upgrade work without foreclosing anything.
- **DECISION (Q-0259 r.5 mapping, same as Track A):** gba-homebrew continues as
  the picked Track B concept's repo (recommendation: yes — the multi-game
  layout `games/skeleton` / `games/lumen-drift` / `games/common` lives here); a
  second Track B concept would need its own repo under ruling 5 — the
  one-repo-many-games shape and ruling 5's one-repo-per-project shape need
  explicit reconciliation when the picks land.

### 13. codetool-lab ×3 (fable5 · opus4.8 · sonnet5) — combined

**Verdict: N/A-ARCHIVED (Projects CLOSED, no relaunch planned) — but NONE of the three repos is platform-archived: all report `"archived": false` (API ~15:12Z). OWNER-CLICK archive toggle ×3, paired with the gen-3 DECISION below.**

- **OWNER-CLICK — archive toggle ×3** (each repo Settings → Danger Zone →
  "Archive this repository"): the ruling describes them as archived; the
  platform state contradicts it, and unarchived public repos remain writable
  surfaces. ~1 min each. **Paired DECISION — archive now vs leave unarchived
  for a future gen-2/gen-3 boot** (archiving makes the repo read-only and would
  break the NEXT-BOOT write rituals). **Recommendation: leave unarchived until
  the gen-3 succession question is settled, then archive** — the succession
  packs explicitly expect a successor session to commit.
- **OWNER-CLICK — cfgdiff v0.1.1, two clicks (sonnet5):** (1) register the
  PyPI trusted publisher (pypi.org → Publishing → pending publisher: owner
  `menno420`, repo `codetool-lab-sonnet5`, workflow `release.yml`, environment
  `pypi`; ~2 min); (2) `git tag -a v0.1.1 0b1eb60 -m "cfgdiff 0.1.1" && git
  push origin v0.1.1` — and do NOT tag v0.1.0 at `0260aae` (predates
  release.yml, fires nothing). cfgdiff 0.1.1 is on main, unreleased —
  release.yml has NEVER fired (status @476bd93).
- **OWNER-CLICK — stale branches ×2:** `claude/status-heartbeat-001` @
  `ea1b23b` (opus4.8, unmerged leftover) and `test/push-check` @ `0260aae`
  (sonnet5, probe leftover; agent delete 403 verbatim: `error: RPC failed;
  HTTP 403 curl 22 …`). ~10 s each.
- **OWNER-CLICK (parked):** envdrift v0.1.0 (`73ef38d`) + v0.2.0 (`13a84e5`)
  tags + GitHub Releases on fable5 (steps in
  `docs/retro/project-review-2026-07-09.md` §(e)); optional PyPI publishes.
- **Gen-3 successor must-knows carried for the record:** classifier-denial
  walls are **SEAT-DEPENDENT** (fable5's "[Auto Mode Bypass]" denial of the
  workflow_dispatch release route vs opus4.8 publishing two live Releases via
  exactly that route — `docs/succession/PLATFORM-LIMITS.md@96f7d0b`, corrected
  at HEAD `a6cf1a9`); capability-inventory-at-boot doctrine (gen-1's biggest
  waste ~2h, `NEXT-BOOT.md@5eb1c75`); proven release recipe via
  `actions_run_trigger` (runs 29035224581 / 29038899218); inbox orders read
  `status: new` forever — diff against status `done=`; setup scripts must be
  defensive always-exit-0; never write model identifiers into repo artifacts.

---

## Routing table — every AGENT-DOABLE item

**Rides a boot / standing wake** (covered by an existing brief, package, or
queued ORDER — nothing to dispatch):

| item | rides | covered by |
|---|---|---|
| Merge superbot PR #1948 (Q-0261 material to main) | the owner-attended dispatch session that owns it — **first agent action of the round** | its own born-red card flip |
| fm ORDER 002 (manifest re-stamp) | manager wake 16:3xZ | status.md next-wake pointer |
| fm ORDERs 001/003/007 (blueprint+MISSION, review-queue rule+drainer, @codex relay rule) | relaunched manager doctrine session | inbox ORDERs (open) |
| fm: verify self-arm for venture-lab / pokemon-mod-lab / gba-homebrew (no triggers at 15:10Z) | next manager wake | owner-queue item 7's own rule |
| fm kit 1.4.0 → 1.7.0 · handoff-doc drift | any manager session | kit release checklist |
| kit: re-arm own routine, then delete `trig_01Fnqn…` | kit seat first boot | founding package + F-1 recommendation |
| kit: queue-state.md NOT-ARMED strike · OA6 re-scope · OA3 create_trigger attempt · T5 re-scope · SessionStart handoff-push · friction #36–#39 triage · legacy-alias delete (POST-OA2 only) | kit seat first boot / ordinary kit lane | next-boot.md §0 + this checklist |
| superbot: seed `control/status.md` + `control/outbox.md` | Idea Engine first boot | founding package design decision (a) |
| superbot: Q-0255 non-CLAUDE.md pointer · kit adoption v1.7.0 | any superbot session | router Q-0255 / kit checklist |
| superbot-next ORDER 008 (self-arm, **boot-gating**) + heartbeat/ender catch-up + kit 1.6.0→1.7.0 | Builder seat first boot | inbox ORDER 008 (P0) + §2 continuation prompt |
| Product Forge ORDER 000 (blueprint §1 walking skeleton) + self-arm + control seed | forge first boot | founding package (born-right ORDER 000) |
| websites: first-fire verification (16:00Z heartbeat) · kit upgrade · PR #9 content disposition | websites next session/fire | queue-state winddown addendum |
| trading ORDER 007 (significance bar — gates P5) + kit 1.1.0→1.7.0 + `kit:` line | trading gen-2 boot | inbox ORDER 007 + QUEUE.md brief |
| venture ORDERs 004 → 002 → 003 (P0 Stripe fix = the ⚑B/⚑D unfreeze path) + review-queue row + kit upgrade | venture fresh-Project boot | ORDER 004 names itself the boot task |
| superbot-games ORDER 001 (P0 CI 73/121 fix — do FIRST) + kit lane-aware upgrade | games gen-2 first session (either lane, claim-first) | inbox ORDER 001 |
| pokemon ORDERs 002 (self-arm) + 003 (R22 private-verify) + kit upgrade | pokemon next boot (coordinator fires the first session) | inbox ORDERs 002/003 |
| gba ORDER 002 (self-arm) + kit upgrade + 11 review-queue rows | gba next boot (coordinator fires the first session) | inbox ORDER 002 + review-queue ledger |

**ORDER to route** (not covered by any existing boot/brief — the manager
dispatches these):

| inbox | one-line do | executor |
|---|---|---|
| trading-strategy `control/inbox.md` | Append the P5 holdout-unlock ORDER explicitly naming `docs/p5-holdout-protocol.md` as binding — SEQUENCE AFTER ORDER 007 completes; direct a fresh dedicated session (not the protocol author) to run it. Owner granted in principle (§4b @ `476228d4`) → decide-and-flag, owner one-line confirm = veto window. | fleet-manager coordinator |
| superbot-next `control/inbox.md` | Encode Q-0259 ruling 3: standing @codex review request on every substantive Builder PR (rule + where it lives in the boot brief); zero trace of it in the repo today (`grep -ri codex` empty). | fleet-manager coordinator |
| superbot-games `control/inbox.md` | Dispatch the same self-arm wake-routine ORDER the other lanes got (Class A hourly; per-lane claim-first) — the only live repo never sent one; also supersede the stale in-repo "owner creates the routine" ask. | fleet-manager coordinator |
| websites (relay) | Execute kit OA12: relay the websites ORDER 005 message the kit seat couldn't route (kit lacked websites scope; the manager doesn't). | fleet-manager coordinator (next wake) |
| fleet-manager `environments/` | Write the `product-forge` environments-registry spec (python-lab archetype, repo-only scope, per founding package) once the owner creates the repo — no spec exists in `archetypes.md@e265fb1`. | fleet-manager coordinator |

### Per-class totals (fleet-wide, deduplicated)

Dedupe rules: each unique click counted once even when multiple repos cite it
(F-5 under kit; venture ⚑A–D under venture; the §4.9 settings-sweep umbrella is
counted as its individual clicks, not double-counted as a sweep); fleet-wide
stale-branch deletion (superbot 554 · superbot-next 1 · websites 4 · games 2)
counted as ONE sweep item (kit's OA10 and the codetool pair carry their own
rows); the two flag-13 halves (click + content decision) counted as 1 click +
1 decision though they collapse into one "accept" line.

- **OWNER-CLICK: 38** — kit 8 (OA1 · OA2 · OA4 · OA5 · OA8 · OA9 · OA10 ·
  OA11) · superbot-next 3 · Idea Engine 1 · Product Forge 3 · websites 3
  (1 conditional-self-expiring) · trading 4 · venture 4 (2 FROZEN — do not
  surface until ORDER 003's unfreeze) · superbot-games 2 · pokemon 2 · gba 1 ·
  codetool 5 (3× archive as one row-set, 2× branch, PyPI publisher, tag,
  envdrift-parked) · fleet-wide 2 (visibility review parked · stale-branch
  sweep). **Boot-gating: 5** (kit OA8; Idea Engine Project; Product Forge
  repo + Project + required-check). **HOT: 1** (F-5).
- **DECISION: 11** — F-1 routine-vs-archive (fleet-wide, once) · sixth-seat
  naming · 8-packages deployment · OA7 superbot pin (silence=accept) · flag-13
  content · Q-0257 dependabot · venture self-landable path · games two-writer
  vs lane-aware kit · joint 6-concept pick (Tracks A+B) · Q-0259 3-repo
  mapping · codetool archive-now-vs-later. Every one carries a recommendation
  above; per Q-0240/Q-0261 doctrine, all are decide-and-flag defaults the round
  proceeds on unless vetoed — none is a stop-and-wait except where a click is
  physically required (Project/repo creation).
- **AGENT-DOABLE: 47** — 42 ride a boot / standing wake (first table) + 5
  routed ORDERs (second table). **Boot-gating agent items: 2** (superbot-next
  ORDER 008 — no Builder trigger exists; superbot-games ORDER 001 — CI blind
  to 48 of 121 tests, flagged as the fresh boot's first act). Plus the
  round-opening prerequisite: **merge superbot PR #1948** before pasting any
  founding package (they are branch-only until then — caveat 1).
