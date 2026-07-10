# projects/ — the fleet's Project package registry

> **Status:** `living-registry` — one dir per Project, each holding the complete
> console package for that seat. Assembled 2026-07-10 (package-centralization
> dispatch) from the three-sweep inventory by three parallel builders; committed
> verbatim by the assembler.

## What this registry is

Every claude.ai Project in the fleet runs on **four owner-pasted parts** that
previously lived scattered across superbot planning docs, fleet-manager
proposals, lane repos, and (worst) chat-only surfaces. This registry is their
**single durable home** — per Project:

- `instructions.md` — the Project's Custom Instructions paste block (≤~7,000
  chars; the 8,000-char console cap is a verified wall).
- `coordinator-prompt.md` — the standing seat prompt (or wake/kickoff prompt
  for seatless lanes) pasted as the coordinator chat's first message.
- `setup-script.sh` — the environment Setup-script console field text
  (defensive shim contract: never exits nonzero, never assumes cwd, never
  mutates residue).
- `failsafe-prompt.md` — the `"<seat> failsafe wake"` trigger text (Q-0265:
  send_later ~15-min chain is the pacemaker; the cron is a dead-man failsafe).
- `meta.md` — seat state, cadence, archetype, grants, Codex status, per-part
  deployed-state, and pinned sources. **Read the meta before pasting anything.**

Archive/pre-birth dirs (`codetool-lab-*`, `mobile-lab`, `games-program`) carry
only `meta.md` (+ `expected-seed.md` for games-program): nothing is deployed
there; the metas index succession material and pre-birth checklists.

**Doctrine:**

1. **Source of truth = these files.** The console fields, chat pastes, and
   trigger prompts are *copies*. Edit here first; the owner re-pastes after
   edits. A deployed text with no committed twin is drift (the class this
   registry closes — several live seats ran on chat-only or console-only text).
2. **Regenerate, don't fork.** These packages were re-based onto the gen-3
   born-continuous standard (Q-0265) by the builders. When doctrine moves
   again, regenerate the affected parts from the new standard and stamp
   provenance inline — never hand-fork a deployed copy and let it drift.
   Future distribution belongs to the **kit seat** (substrate-kit currently
   has no setup-script/seat-prompt/failsafe templates — the known kit gap its
   meta names; when those templates ship, this registry becomes their
   render target).
3. **Family-level model names only** (Q-0262 policy 1) — everywhere, including
   in these files.
4. **Probe-once-per-seat** for classifier walls; credential-layer 403s are
   real on every seat tested (the codetool release lesson,
   `codetool-lab-fable5/meta.md`).

## MATRIX — one row per Project (2026-07-10)

Per-part states: **DEPLOYED-verified** (live + verified, text committed) ·
**deployed-stale** (something is live but older/unverified vs this package) ·
**never** (nothing ever deployed as such) · **unknown** (owner-side surface,
no paste record) · **n-a** (deliberately absent).

| Project | Seat status | Cadence (failsafe cron) | 1 instructions | 2 coord prompt | 3 setup script | 4 failsafe | Key flag |
|---|---|---|---|---|---|---|---|
| fleet-manager | LIVE (manager, continuous) | `30 */2 * * *` + ~15-min chain | never (re-base; re-paste on re-boot) | DEPLOYED (live-amended chat) | unknown | **DEPLOYED-verified** (`trig_014odnv5h…`) | sole multi-repo seat (Q-0260 exception); Codex NOT enabled (ask on PR #26) |
| substrate-kit | LIVE | `0 */2 * * *` | deployed-stale (pre-Q-0265 founding §1) | deployed-stale (chat-amended only) | unknown (OA8 paste unconfirmed) | never (OLD standing wake still live — re-arm due) | write-all distribution seat; owns future template distribution |
| superbot-next | LIVE (Builder) | `0 */2 * * *` + chain | never (new draft) | never (new draft) | deployed-by-reference (archetype verbatim) | **DEPLOYED-verified** (fleet reference instance) | Codex LIVE; 6 required checks; REST-squash fast lane |
| idea-engine | LIVE | `0 */2 * * *` (even) + chain | deployed-equivalent | deployed-equivalent (chat) | deployed-by-reference | **DEPLOYED-verified** (committed verbatim) | Q-0265 reference implementation; cadence-PAIRED with sim-lab |
| product-forge | LIVE (continuous) | `0 */2 * * *` + chain | deployed-stale (boot paste, pre-lessons) | deployed-stale (founding §2) | never | armed (`trig_012Evzt…`; text-equality unverified) | already live-continuous; games-web phase-1 SHIPPED (PRs #4+#5); §2b paste = belt-and-braces |
| sim-lab | LIVE | `0 1-23/2 * * *` (odd) — **NOT armed** | deployed-presumed | deployed-stale (boot brief) | deployed-by-reference | **never — seat lacks scheduler tools** (OA-003) | owner arms via Routines screen; cadence-PAIRED with idea-engine (centralize as a pair) |
| websites | LIVE (fresh-session-per-fire, no seat) | `0 */4 * * *` deployed · `0 */2` recommended | deployed-stale (older fm text; re-paste) | deployed-stale (v1 prompt live; v2 unverified) | unknown | trigger DEPLOYED-verified, prompt stale/unverified | only fresh-session lane; cron IS the pacemaker; one 16:01Z silent fire on record |
| trading-strategy | PARKED GREEN — program COMPLETE | `0 */4` stale · `0 */2` spec'd (F-1 cutover) | deployed-stale (pre-Q-0265) | deployed-stale (old delegating one-liner) | unknown | never (live trigger stale on two axes) | **holdout SPENT, report FINAL; PR #37 = owner merge click** (terminal classifier refusal) |
| venture-lab | LIVE-BUT-DARK (no clock, stale heartbeat) | `0 */2` spec'd — NOT armed | never | never | never | never | riskiest lane state; ORDERs 002/003/004 ride fresh boot; ⚑B/⚑D frozen on Stripe P0 |
| superbot-games | PARKED + CLOCKLESS (merged lane) | `0 */2` spec'd — NOT armed | never (current form) | never | unknown (two per-lane scripts, inconsistent dirs) | never | kit **v1.7.0 at HEAD** (heartbeat says v1.2.0 — drift); P0: CI collects 73/121 tests |
| pokemon-mod-lab | LIVE-PARKED · **PRIVATE** | `0 */2` spec'd — NOT armed | deployed-stale (game-lab founding text) | never | unknown | never | private ⇒ raw-read DARK; env-attach is the only path (manager + kit need it too) |
| gba-homebrew | LIVE-PARKED (scope-complete) | `0 */2` spec'd — NOT armed | unknown | never | unknown (repo's own toolchain script proven) | never | Track-B concept pick open; archetype gba-lab unverified-as-a-whole |
| superbot | NO SEAT by design (Q-0264) | none — recon loop is issue-based | n-a (`.claude/CLAUDE.md` IS the deployed text) | n-a (manual kickoff prompt) | unknown | n-a (deliberate absence, documented) | hub + LIVE production bot; Codex LIVE; owner-started sessions only |
| codetool-lab-fable5 | ARCHIVE (Project closed; repo retained) | n-a | n-a | n-a | n-a | n-a | envdrift tags v0.1.0/v0.2.0 PARKED (never pushed); seat-dependent-wall lesson lives here |
| codetool-lab-opus4.8 | ARCHIVE (Project closed; repo retained) | n-a | n-a | n-a | n-a | n-a | mdverify **v0.1.0/v0.2.0 Releases LIVE**; 1 stale branch (owner delete) |
| codetool-lab-sonnet5 | ARCHIVE (Project closed; repo retained) | n-a | n-a | n-a | n-a | n-a | cfgdiff v0.1.1 pending 2 owner clicks (PyPI publisher + tag push) |
| mobile-lab | PRE-BIRTH (no repo, no Project) | n-a | n-a (held gen-2 package; Q-0262.6 re-base first) | n-a | n-a | n-a | bundled with the 6-repo harness experiment (both ready-not-launched, owner-gated) |
| games-program | PRE-BIRTH ×3 repos (Q-0259 r5) | n-a (per-repo at boot) | n-a | n-a | n-a | n-a | mapping DECIDE-AND-FLAG pending; `expected-seed.md` is the per-repo checklist |

## Paste wave — what the owner pastes NOW vs what rides a boot

**NOW (console/chat pastes + one Routines-screen arm) — the click-level list
is the consolidated owner-queue item ("Project package paste wave"):**

1. **substrate-kit** — §2b continuous-mode amendment into the live coordinator
   chat + **OA8**: `projects/substrate-kit/setup-script.sh` (or the archetype)
   into the kit env's Setup-script field.
2. **product-forge** — §2b amendment paste into the live coordinator chat
   (belt-and-braces; the seat already operates continuous per its status).
3. **sim-lab** — arm the failsafe **via the Routines screen** with
   `projects/sim-lab/failsafe-prompt.md` (cron `0 1-23/2 * * *`): the seat
   verifiably lacks `create_trigger`/`send_later` (OA-003) — the lane has NO
   clock until this click.
4. **websites** — re-paste the v2 wake prompt
   (`projects/websites/coordinator-prompt.md`) into trigger
   `trig_017H9Qb9oxtLgUy6sw2gnSHg` (last committed record says v1-era text) +
   re-paste `projects/websites/instructions.md` (deployed text is the older
   pre-Q-0265 fm fitted version); optional: retune `0 */4` → `0 */2`.
5. **trading-strategy** — re-paste `projects/trading-strategy/instructions.md`
   (deployed CI is pre-Q-0265/pre-completion); the failsafe F-1 cutover can
   ride the seat, but the paste is owner-only.
6. **superbot (optional)** — `projects/superbot/instructions.md` only if the
   owner hosts superbot sessions in a Project whose console field is empty;
   `.claude/CLAUDE.md` already auto-loads in-repo.

**Rides a seat's own boot / agent-side (no owner paste now):**

- **fleet-manager** — live chat already operates on the amended model;
  instructions re-paste only needed on a seat re-boot.
- **superbot-next, idea-engine** — live seats current or equivalent; the new
  drafts here canonize text for re-boot/succession.
- **venture-lab** — all four parts ride ORDER 004's fresh boot (arming
  included).
- **superbot-games** — parts ride first merged-lane boot (ORDER 002 arming;
  scheduler tools are seat-dependent — re-probe, fall back to an owner
  Routines-screen arm like sim-lab if absent).
- **pokemon-mod-lab, gba-homebrew** — ride the games-program boot (Q-0259 r5
  mapping first); their unexecuted hourly ORDER 002s are superseded by these
  failsafe texts, never executed.
- **Archives / pre-birth** — nothing to paste by definition.

## Provenance

Built **2026-07-10** from the three-sweep inventory (committed here:
[`_inventory/inventory-hub.md`](_inventory/inventory-hub.md) ·
[`_inventory/inventory-lanes.md`](_inventory/inventory-lanes.md) ·
[`_inventory/inventory-games-new.md`](_inventory/inventory-games-new.md)) by
three parallel builder workers; every package's exact sources + repo SHAs are
pinned in its own `meta.md` (metas cite the inventories by their build-time
scratchpad path `launch-packages/…` — the same files live in `_inventory/`).
Assembled verbatim by the assembly worker (this PR); spot-fix scope was
mechanical-only, none needed.
