# Fleet triage register — keep / replace / archive / delete

> **Status:** `living-ledger`
>
> The standing, re-reviewable **"should it exist?"** ledger for every fleet
> repo — distinct from `roster.md` (freshness now) and the product catalog
> (what each thing is). **Canonical home: fleet-manager** (centralization plan
> §4 — cross-repo/fleet state lives here), ported 2026-07-11 (P3, fm PR #86)
> from the seed review. Re-verdict rows as reality moves; a verdict is a
> dated judgment, not a decree — cite evidence when you change one.
>
> **Seed provenance:** superbot
> [`docs/planning/fleet-review-2026-07-11.md`](https://github.com/menno420/superbot/blob/main/docs/planning/fleet-review-2026-07-11.md)
> §1 — the owner-directed 2026-07-11 verified full-fleet review (19-agent
> fan-out, every load-bearing claim source-verified, Q-0120). That doc stays
> as the frozen program-narrative snapshot; THIS file is the living register.

## Verdict legend

**KEEP** (active, earns its place) · **KEEP-SEQUENCE** (keep, mid-build,
defined next step) · **KEEP-PARKED** (keep the asset, park the loop) ·
**ARCHIVE** (finished, make read-only, lose nothing) · **SEED** (empty, one
action to activate) · **DELETE** (none).

## Register (verdicts as of 2026-07-11; seed = the fleet review §1, verified)

> **Seat column re-stamped 2026-07-11 (owner restructure directive — 8
> standing seats; slice 3, fm PR #91):** every row now names the standing
> seat that owns the repo post-restructure. Mapping source: slice 1
> (fm PR #88, `projects/README.md` restructure banner). Verdicts/health are
> UNCHANGED by the re-stamp — the restructure moves the seat layer, not the
> repos.

| Repo | Seat (2026-07-11 restructure) | Health | Verdict | One-line rationale | The single next action |
|---|---|---|---|---|---|
| **superbot** (hub / prod bot) | SuperBot 2.0 (owner-session character retained, Q-0264) | 🟢 | KEEP | The oracle + the live product; the whole program's substrate | Normal live-verify of merges; fix the Rule-6 false-green checker (review §3) |
| **superbot-next** (rebuild) | SuperBot 2.0 (Builder side, continuous loop) | 🟡 | KEEP-SEQUENCE | Flagship build, 37/49 ported, boots on real PG; 2 money races to fix pre-cutover | Fix F-001/F-002 wallet races + F-003 parity false-green, then continue ports |
| **substrate-kit** (fleet foundation) | Self Improvement | 🟡 | KEEP | 7 adopters run on it; gate false-green shipped in v1.12.0; #228 was an empty fix | Land the *real* gate fix, cut a patch release *(post-seed: fixes landed via kit #228 successor work — re-verify at next sweep)* |
| **websites** (oversight/control-plane) | Websites | 🟢 | KEEP | 4 real services, 3 live; the fleet's visual control plane; backlog drained | Owner: merge #141 + create the `review` Railway service |
| **venture-lab** (first revenue) | Venture Lab | 🟡 | KEEP | 3 real built products; **critical Stripe fail-open** before publish | 🔴 Fail-closed on partial Stripe config, then publish |
| **superbot-mineverse** (web game) | SuperBot World (flagship) | 🟡 | KEEP | Real read-only demo; login-CSRF + pytest-not-required before secrets | Bind OAuth state to browser + schema-validate; make pytest required |
| **superbot-games** (game engines) | SuperBot World | 🟢 | KEEP | Pure-domain, green, DM-clamp verified; parked on plugin contract (correct) | ~~Owner merge #49 then #50~~ *(post-seed: #49 merged `5d38593` 17:22Z)*; refresh stale status |
| **superbot-idle** (idle engine) | SuperBot World | 🟡 | KEEP-SEQUENCE | 1227 tests, 15 themes; PLUG-001 adapter MERGED (#75, 2026-07-13T01:26Z, self-landed) + wave-4 packs (#76); SIM-001 verdict DELIVERED (sim-lab V038 CONDITIONAL @ `afe18f3` — graduate the PROVISIONAL table) | Act on V038 graduation (seat-side economy-v1.md re-registration) + owner letters E#52/E#53 |
| **product-forge** (web-product forge) | ⚑ owner disposition pending (`OQ-FORGE-DISPOSITION` — not in the 8-seat list) | 🟢 | KEEP | Real games-web, 22 PRs, foundational infra ("home to homeless projects") | Owner: enable GitHub Pages (one toggle — `OQ-FORGE-PAGES`) |
| **gba-homebrew** (GBA game) | Game Lab (public track) | 🟢 | KEEP | Playable committed ROM, reproducible CI build; low-maintenance | Owner: create the Lumen Drift v1.3 Release (`OQ-GBA-LUMEN-RELEASE`) |
| **pokemon-mod-lab** (private ROM mod) | Game Lab (private track — track isolation binding) | 🟢 | KEEP-PARKED | Real 16-patch mod, private, copyright-safe; idle ~18 sessions, all owner-gated | **Pause/slow the hourly wake**; owner playtest verdict unblocks it (`OQ-SITTING-0714-DECISIONS`) |
| **trading-strategy** (quant research) | Venture Lab (research-only annex — backtest engine only) | 🟢 | KEEP-PARKED | Honestly complete (holdout spent, 0/13 cleared); paper lane in warm-up | Leave parked until the 2026-07-17 grading |
| **sim-lab** (evidence/lie-detector) | Ideas Lab (verify half of the generate→verify loop) | 🟢 | KEEP | 67 verdicts (numbering high-water — sim-lab's own count; 62 `sims/verdict-*` dirs on disk, live-verified 2026-07-14 at HEAD `311c461`, INC-14; the seed's "10" was a dated snapshot), self-checks caught a real bug; idle-by-design not stuck | ~~Owner: enable Codex (OA-002)~~ *(post-seed: integration-ENABLED resolved — Codex envs exist for all 12 active repos, ORDER 014; quota-throughput half OPEN sim-lab-side — INC-04 split, 2026-07-14)* |
| **idea-engine** (ideation) | Ideas Lab (generate half) | 🟢 | KEEP | 193 PRs, reports verify true; surfaced a real superbot false-green | Split the 25KB status.md; lift the ≤07-13 owner decision out of the bloat |
| **fleet-manager** (coordination substrate) | Fleet Manager (manager) | 🟢 | KEEP | The de-facto SSOT; roster/queue/inbox real | *(post-seed: the seed's "ledgers drift + stubs unfilled" 🟡 is CLOSED by P1–P3, fm #81–#86)* Keep the custodian loop green |
| **superbot-plugin-hello** | seed — spans SuperBot 2.0 (contract) ↔ SuperBot World (consumers) | 🟢 seeded | **KEEP-QUIET** *(re-verdict 2026-07-14, INC-01: seeded `bbaccec` 2026-07-12T13:29Z, live-re-verified non-empty; pinned by superbot-next `plugins.lock.json` — never archive)* | Contract exemplar, dormant-by-design; idle PLUG-001 unblocked (adapter #75/#78) | ⚠ merge-on-green.yml installed (owner-merged #3, 2026-07-15T15:29:41Z, main `abd9133`) but **INERT** — repo has zero CI, zero check runs = NOT-ready by design, so it merges nothing; hub should add a minimal CI gate (agent-doable) or accept the automation as inert (2026-07-15 addendum, [rollout findings](findings/merge-on-green-rollout-verification-2026-07-15.md)) |
| **codetool-lab-fable5** (envdrift) | none — seat retired to stub (slice 1) | ⚫ parked | **ARCHIVE** *(disposition DECIDED 2026-07-14 — archive, no relaunch; sequenced release-before-archive; see dispatch-log)* | Finished CLI, wound-down, no mission | D5 mirror-before-archive + P1-5 hygiene + tag/Release clicks, then owner archive click (E#44/E#45 gate) |
| **codetool-lab-opus4.8** (mdverify) | none — seat retired to stub (slice 1) | ⚫ parked | **KEEP unarchived** *(re-verdict 2026-07-14, INC-03: this row's old ARCHIVE contradicted the standing 2026-07-10 owner ruling + live mdverify releases v0.1.0/v0.2.0 — the consolidation plan's reconciled verdict wins; decide-and-flag)* | Finished CLI, releases LIVE (the fleet's release exemplar), wound-down | none — dormant KEEP; re-verdict only if the owner rules again |
| **codetool-lab-sonnet5** (cfgdiff) | none — seat retired to stub (slice 1) | ⚫ parked | **ARCHIVE** | Finished CLI, wound-down, no mission | Archive after gen-3 succession settles; pending v0.1.1 tag |

**19 repos · 15 active (all KEEP-family) · 3 ARCHIVE · 1 SEED · 0 DELETE**
(seed tally, unchanged at port time).
*Re-tally 2026-07-14 (Slice 0 item 6 re-verdicts): 17 KEEP-family
(opus4.8 → KEEP per INC-03; plugin-hello → KEEP-QUIET, seeded) ·
2 ARCHIVE (fable5 — decided, sonnet5) · 0 SEED · 0 DELETE.*

## 2026-07-11 owner restructure — 8 standing seats (slice 3 re-stamp)

> Re-stamped 2026-07-11 (restructure directive, slice 3 — fm PR #91, stacked
> on #88/#89). Seat-level heartbeats are **not measured — no seat Project
> exists yet** (owner creates them: `OQ-RESTRUCTURE-PROJECTS`); constituent
> last-seen values below are read from roster **gen #9** (generated
> 2026-07-11T20:25Z, `docs/roster.md` @ that generation) and, for
> fleet-manager, its own `control/status.md`. Never invented — a value that
> could not be read says "not measured".

| Seat | Registry dir (`projects/`) | Constituent repos/lanes | Constituent heartbeats last-seen (gen #9, 2026-07-11T20:25Z) | Seat state at re-stamp |
|---|---|---|---|---|
| Venture Lab | `venture-lab/` (instructions v3) | venture-lab · trading-strategy (research-only annex) | venture-lab 2026-07-11T19:37:09Z · trading 2026-07-11T19:33:12Z | awaiting owner create/paste/boot (OQ-RESTRUCTURE-PROJECTS/-INSTRUCTIONS-PASTE/-TRIGGER-CUTOVER) |
| SuperBot World | `superbot-world/` (v1) | superbot-mineverse (flagship) · superbot-games · superbot-idle | mineverse 2026-07-11T19:45:00Z · games 2026-07-11T19:39:14Z · idle 2026-07-11T19:37:36Z | awaiting owner create/paste/boot |
| Game Lab | `game-lab/` (v1) | gba-homebrew (public) · pokemon-mod-lab (private) — replaces the repo-less retro coordinator | gba 2026-07-11T20:15:00Z · pokemon 2026-07-11T20:03:55Z · retro seat itself: not measured (registry-only, no heartbeat home) | awaiting owner create/paste/boot |
| Ideas Lab | `ideas-lab/` (v1) | idea-engine · sim-lab | idea-engine 2026-07-11T19:53:28Z · sim-lab 2026-07-11T20:20:00Z | awaiting owner create/paste/boot |
| Self Improvement | `self-improvement/` (v1) | substrate-kit | kit 2026-07-11T19:51:53Z | awaiting owner create/paste/boot |
| SuperBot 2.0 | `superbot-2.0/` (v1) | superbot (hub) · superbot-next | superbot 2026-07-11T19:45:00Z · next 2026-07-11T20:20Z | awaiting owner create/paste/boot |
| Websites | `websites/` (v2; coordinator v3) | websites | 2026-07-11T19:49:00Z | Project exists; keeps its trigger — coordinator v3 re-paste owed (OQ-RESTRUCTURE-TRIGGER-CUTOVER, websites bullet) |
| Fleet Manager | `fleet-manager/` (v3) | fleet-manager | 2026-07-11T21:50:00Z (own `control/status.md`, pre-this-slice) | live repo-side; coordinator seat ARCHIVED — successor boots per reboot-prompt v2 (F-1), unchanged by restructure |

Out of the 8: **product-forge** (live seat, disposition pending —
`OQ-FORGE-DISPOSITION`). Retired to stubs (slice 1): codetool-lab ×3 ·
mobile-lab · games-program · superbot-retro (+ 11 merged-source dirs).

## 2026-07-13 · Q-0264 relay-consumption sweep (13:13:45Z, read-only, SHA-cited)

> Dated evidence note (per §How-to-re-verdict pt 4 — dated notes land here, not
> a fork file). Sweep question: have the 9 sim-lab verdicts **V037–V045**
> (finalized at sim-lab @ `afe18f3`, 09:43–11:35Z) and **idea-engine ASK 002**
> — all recorded as relay pointers in fm `control/outbox.md` @ `a32eb2c`
> L468–502 ("Q-0264 FAN-IN" section) — been consumed lane-side? **Answer: no.
> Zero lane-side consumption; all 10 items PENDING manager fan-out**, exactly
> as the relay record's own "coordinator relays at next dispatch" wording
> anticipated. No lane is no-signal (all have fresh heartbeats); no lane
> self-served from the fm outbox either.

| Lane | Verdict / ask | Status | Evidence (lane HEAD-cited) |
|---|---|---|---|
| venture-lab | V037 Ultramarine serial pricing — CONDITIONAL (R3 default arm) | **pending** | venture-lab@`765e1f8`: inbox latest = ORDER 009 (09:11Z night-report ask), no verdict relay; outbox L24 still lists the Ultramarine SIM-REQUEST as PENDING; no "V037" string in any control file |
| venture-lab | V039 photo packs — CONDITIONAL ($5 fixed default + bundle row) | **pending** | venture-lab@`765e1f8`: no "V039" in control/{inbox,status,outbox}.md; outbox L24 lists photo-packs SIM-REQUEST as PENDING |
| venture-lab | V040 Ship-It Bundle — CONDITIONAL ($59 ratified, parked switch rule) | **pending** | venture-lab@`765e1f8`: no "V040" in control files; outbox L24 lists the $59-vs-anchors SIM-REQUEST as PENDING |
| venture-lab | V041 narrow-TAM cookbooks — CONDITIONAL ($19 fixed default) | **pending** | venture-lab@`765e1f8`: no "V041" in control files; outbox L24 lists the $19-vs-PWYW SIM-REQUEST as PENDING |
| superbot-idle | V038 SIM-001 economy-FEEL — CONDITIONAL (graduate PROVISIONAL table; A10 re-wording seat-side) | **pending** | superbot-idle@`b03cc96`: no "V038" in control files; status.md L8 `blockers: SIM-001/Q-0264 … still open`, L94 `RESUME TRIGGER: Q-0264 ruling lands`; inbox latest = ORDER 004 (09:09Z), no verdict relay. **Relay clears this lane's declared RESUME TRIGGER.** |
| superbot-games | V042 mining-economy — APPROVE (2 flagged rows) | **pending** | superbot-games@`57f69be`: no "V042" in control files; status.md L77 + outbox L290 still list mining-economy-tuning SIM-REQUEST as PENDING |
| superbot-games | V043 fishing-economy — APPROVE-WITH-CONSTANTS (wire VERBATIM at the seam) | **pending** | superbot-games@`57f69be`: no "V043" in control files; status.md L78 lists fishing-economy-tuning as PENDING |
| superbot-games | V044 dnd-escort-double-mint — MINT-AT-MOST-ONCE (guard at bundle fold) | **pending** | superbot-games@`57f69be`: no "V044" in control files; status.md L79 lists dnd-escort-double-mint as PENDING |
| superbot-games | V045 exploration-reward-bands — RATIFY-WITH-NULL (numeric import waits on superbot P0 artifact) | **pending** | superbot-games@`57f69be`: no "V045" in control files; status.md L80 lists exploration-reward-bands as PENDING |
| idea-engine → Self Improvement seat | ASK 002 — kit-local `check --strict` ⇒ CI substrate-gate parity (evidence: idea-engine PRs #274/#299) | **pending** | Originator idea-engine@`c807960`: outbox L295 ASK 002 still `status: new` (status.md L6 corroborates). Target substrate-kit@`949875c`: no "ASK 002" / check-parity order in control/inbox.md |

**Pending lane-inbox writes owed (manager fan-out at next dispatch):**
venture-lab ← V037/V039/V040/V041 · superbot-idle ← V038 (clears its RESUME
TRIGGER) · superbot-games ← V042/V043/V044/V045 · substrate-kit (Self
Improvement seat) ← idea-engine ASK 002. Method: read-only (`git fetch` +
`git show origin/main:<file>` per lane); lane HEADs as cited above. Sweep run
from the trigger-health-i1 worker session (fm PR #167, Slice B).

## 2026-07-13 · Q-0264 relay-consumption re-sweep (14:37:33Z, read-only, SHA-cited)

> Dated evidence note (per §How-to-re-verdict pt 4). Read-only re-sweep from
> the wake-14:34Z session (recorded in fm PR #169); prior sweep: PR #167
> (13:13:45Z section above). Since that sweep the manager fan-out has landed
> in all four lane inboxes — this re-sweep asks whether the lanes have
> **consumed** the delivered orders. **Answer: 2 of 4 lanes CONSUMED**
> (venture-lab, substrate-kit); superbot-idle and superbot-games still
> PENDING at HEAD.

| Lane | ORDER | Delivered (PR / main squash) | Verdict | Evidence |
|---|---|---|---|---|
| venture-lab | 010 (V037/V039/V040/V041) | #161 / `84d4bcb` @ 13:42:35Z | **CONSUMED** | PR #163 merged 14:03:14Z (squash `e252b46`) applies all four verdicts + heartbeat "ORDER 010 applied + ack"; follow-on #164 (`d71649b`, 14:29Z), #165 (`5944109`, 14:33Z) |
| superbot-idle | 005 (V038, SIM-001) | #88 / `05a99f5` @ 13:42:59Z | **PENDING** | inbox@`675c347` (blob `15f11c5`): ORDER 005 still `status: new`; status.md@HEAD acked/done ledger stops at 004; lane alive (#89 `e740810` 14:03Z, #90 `675c347` 14:25Z, both unrelated); 0 open PRs |
| superbot-games | 007 (V042–V045) | #80 / `156e2de` @ 13:44:12Z | **PENDING** | inbox@`d6a9526` (blob `75c2609`): ORDER 007 still `status: new`; acked ledger stops at 006; newest heartbeat section = 09:22Z night report; lane alive (#81 groom `d6a9526` 14:04Z, unrelated); 0 open PRs |
| substrate-kit | 018 (ASK 002 → check --strict CI parity) | #329 / `430f7a2` @ 13:43:11Z | **CONSUMED** | PR #332 merged 14:32:29Z (squash `3d58a46`) — check --strict runs inbox + preflight_scripts legs locally, tests pinned; intervening #330 (`481f682`, 13:49Z), #331 (`a4b9808`, 14:06Z) |

**Re-sweep result:** 2 of 4 lanes CONSUMED (venture-lab via #163 `e252b46`;
substrate-kit via #332 `3d58a46`); superbot-idle ORDER 005 and superbot-games
ORDER 007 PENDING — still `status: new` at HEAD with no verdict work started,
though both lanes show unrelated post-delivery merges (alive, not stalled).
Note: the games/kit "tip" SHAs relayed at fan-out (`af36d52`, `9a6caa4`) were
branch heads; the main squash SHAs are `156e2de` / `430f7a2` — delivery
confirmed on main in all four lanes.

## 2026-07-13 · Q-0264 relay-consumption re-check (17:03:39Z, read-only, SHA-cited)

> Dated evidence note (per §How-to-re-verdict pt 4). Read-only re-check from
> the failsafe-wake 16:33Z executor session; prior sweeps: PR #167 (13:13:45Z)
> and PR #169 (14:37:33Z, above). Delta-only: venture-lab 010 and
> substrate-kit 018 were already **CONSUMED** at the 14:37Z re-sweep
> (venture-lab #163 `e252b46`; substrate-kit #332 `3d58a46`) — not
> re-litigated here. This re-check covers only the two lanes left PENDING.

| Lane | ORDER | 14:37Z state | Live HEAD (17:03Z) | Verdict | Evidence |
|---|---|---|---|---|---|
| superbot-idle | 005 (V038, SIM-001) | inbox@`675c347`, status: new; ack ledger stops at 004 | `96cd635` (HEAD advanced) | **STILL-PENDING** | inbox@`96cd635` line 40: `## ORDER 005 · 2026-07-13T13:40:58Z · status: new` (unchanged); status.md@`96cd635` line 9: `orders: acked=000-004 done=000-004` — ledger has not advanced past 004; lane alive (HEAD moved past `675c347` on unrelated work) but the order untouched |
| superbot-games | 007 (V042–V045) | inbox@`d6a9526`, status: new; acked ledger stops at 006 | `d6a9526` (HEAD unchanged) | **STILL-PENDING** | repo HEAD is the same commit as the 14:37Z sweep, so the whole tree is byte-identical; re-fetched anyway: inbox@`d6a9526` line 103: `## ORDER 007 · 2026-07-13T13:42:24Z · status: new`; status.md@`d6a9526` line 13: `orders: acked=001,002,003,004,005,006` — no new commits at all since 14:04Z |

**Re-check result:** 0 of 2 pending lanes consumed since 14:37Z —
superbot-idle ORDER 005 and superbot-games ORDER 007 both STILL-PENDING at
live HEAD. Cumulative Q-0264 consumption: 2 of 4 (venture-lab,
substrate-kit). Next natural checkpoint: the SuperBot World seat's next
failsafe wake (`trig_01QctdbvhdcvuSFsCPxdseae` `15 1-23/2 * * *`, next
~17:15Z per the 16:56Z snapshot — the seat covers superbot-games +
superbot-idle); if a third sweep still finds `status: new`, the manager
should consider a send_message nudge per the ORDER 040 TASK 3 escalation
ladder (rung 2).

## 2026-07-13 · Q-0264 relay-consumption THIRD check (18:40Z, read-only, SHA-cited)

> Dated evidence note (per §How-to-re-verdict pt 4). Read-only third check from
> the failsafe-wake 18:34Z work slice (fm PR #173); prior sweeps: PR #167
> (13:13:45Z), PR #169 (14:37:33Z), and the 17:03:39Z re-check above.
> Delta-only: covers the two lanes left STILL-PENDING at 17:03Z.
> **Answer: BOTH CONSUMED — cumulative Q-0264 consumption now 4 of 4.**

| Lane | ORDER | 17:03Z state | Live HEAD (18:40Z) | Verdict | Evidence |
|---|---|---|---|---|---|
| superbot-idle | 005 (V038, SIM-001) | STILL-PENDING @ `96cd635` | `4c31a2c` (inbox blob `15f11c5`, status blob `cdda9f0`) | **CONSUMED** | status.md@`4c31a2c` (updated 2026-07-13T17:43Z): `orders: acked=000-005 done=000-005`; dedicated "§ ORDER 005 — SIM-001 VERDICT 038 consumed" section — graduation PR #93 (economy-v1.md table PROVISIONAL → SIM-PINNED + A10 re-registered in trend form, zero parameter changes; claim via fast-lane PR #92 merged 17:29:27Z). Inbox thread itself still reads `status: new` — inbox is one-writer (manager), so the ack lives in status.md per the seat grammar |
| superbot-games | 007 (V042–V045) | STILL-PENDING @ `d6a9526` | `ce70d9e` (inbox blob `75c2609`, status blob `b2909a4`) | **CONSUMED** | status.md@`ce70d9e`: `orders: acked=001,002,003,004,005,006,007 done=001,002,003,005,006,007` + done=007 per the order's own clause; dedicated "§ ORDER 007 ACK — 2026-07-13T17:45:47Z" section — V042 APPROVE ratified, V043 wired + V044 guard landed via PR #83 (open READY on the card-guarded enabler at check time), V045 ratified-with-NULL; four SIM-REQUESTs closed in control/outbox.md. Same one-writer-inbox note as above |

**Third-check result:** 2 of 2 previously-pending lanes CONSUMED between
17:03Z and ~17:45Z (both by the SuperBot World seat's 17:15Z failsafe wake
window, as the 17:03Z note predicted). **Cumulative: 4/4** (venture-lab #163,
substrate-kit #332, superbot-idle #93, superbot-games #83). No ORDER 040
TASK 3 escalation needed — the rung-2 send_message nudge contemplated at
17:03Z is moot. Q-0264 fan-out consumption is CLOSED; residue rides lane-side
(idle: tools/simulate.py A10 v2 harness follow-up, flagged in its status;
games: PR #83 landing on its card flip).

## 2026-07-13 · I1b disposition — `trig_011XAWqPeksS8LBrS5G9RvVc` "superbot autonomous dispatch" (20:51Z, read-only, SHA-cited)

> Dated evidence note (per §How-to-re-verdict pt 4). Baton item from the
> failsafe wake 2026-07-13T20:33Z (executor session, fm PR #175): the standing
> I1b AMBIGUOUS-ENABLED WARN row in `check_trigger_health.py` gets its
> classification. The trigger is NOT fleet-manager's — nothing here modifies
> it; the verdict routes to the superbot hub seat via `control/outbox.md`
> (same wake) for disposal by its owner.

**Verdict: DORMANT OWNER-PAUSED REMNANT of the pre-fleet-era superbot
dispatch routine — recommend disposal by its owner (superbot hub seat /
owner console: delete, or annotate-and-leave-paused). Do NOT re-enable or
rebind as-is.**

Registry facts (fresh export, `telemetry/triggers-snapshot.json`
`captured_at 2026-07-13T20:42:00Z`, this wake's PR #175 commit `90e1a7f`):

- `trig_011XAWqPeksS8LBrS5G9RvVc` · name "superbot autonomous dispatch" ·
  cron `0 */3 * * *` · created 2026-06-12T20:15:49Z via `http_api` ·
  environment `env_01CZRF681i8ef2zqt9GgboYy` (superbot).
- `last_fired_at` 2026-07-02T00:07:46Z · `updated_at` 2026-07-02T02:38:10Z ·
  `next_run_at` FROZEN at 2026-07-02T03:07:12Z (11+ days past) · `enabled`
  ABSENT · `ended_reason` ABSENT. Per the CCR `list_triggers` contract, a
  disabled routine with empty `ended_reason` = **user-paused** — i.e. the
  registry shape reads as a console pause action at ~2026-07-02T02:38Z,
  ~2.5h after its last fire, not a platform auto-disable and not a wedge.
- Same-env cross-check (same export): superbot's environment holds exactly
  one ENABLED trigger — the poke-only `suberbot docs reconciliation`
  (`trig_018wP6XTPmf9DLnxrG4RpGVh`). The dispatch trigger's sibling
  `superbot night executor` (`trig_01MWHvQFnRF1dVdZFSP6SM5L`) is likewise
  disabled with no `ended_reason` — the other standing I1b WARN row, same
  remnant class.

Repo evidence (superbot read READ-ONLY over raw.githubusercontent.com at
main = `1cc553651a19016a4b1439f048b49e7baa28dfb1`, ls-remote-verified):

- `docs/operations/autonomous-routines.md@1cc5536` L30: "superbot dispatch —
  the single execution routine | console Schedule (every ~2–3h,
  `0 */2 * * *`, owner-tuned, Q-0146)" — the trigger's stored prompt opens
  with the exact dispatch-routine text ("You are the SuperBot DISPATCH
  routine — the single execution routine that does ALL the project's build
  work…"), confirming identity; the `0 */3` cron on the record is the
  owner-tuned variant the same line anticipates.
- Same file L279–289: the "superbot night executor" was MERGED into dispatch
  (Q-0145, 2026-06-15) — the sibling record is a documented remnant.
- Same file L331: "Pause/kill: toggle a routine off (or delete it) in the
  console" — the pause path matches the registry shape.
- Staleness of the stored prompt: it still carries the Q-0117
  `needs-hermes-review` merge gate (retired by Q-0197 per the same doc's L30)
  and pre-dates the fleet-era continuous-mode seat model (Q-0265). The hub's
  build work is lane-side now (superbot-next; fm inbox ORDER 030), and the
  superbot hub roster row (roster gen #34) is a coordination surface.
- **Doc drift flagged to the superbot seat:** `autonomous-routines.md@1cc5536`
  L395/L406 still present the dispatch console Schedule as the live, reliable
  cadence — false since the 2026-07-02 pause; the disposing session should
  annotate it.

Why "recommend deletion by owner" and not "rebind": deletion is destructive
and the pause was an owner action, so the superbot seat should confirm with
the owner (the stored prompt is preserved verbatim in this repo's committed
snapshots and in superbot `docs/operations/hermes-dispatch-bridge.md`, so
nothing is lost). If the hub ever wants a scheduled execution wake again, the
correct move is a FRESH trigger from current v3.x prompt sources, not
re-enabling this stale-doctrine record.

## 2026-07-14 · Failsafe-wake fan-out verification sweep (05:03:18Z, read-only, SHA-cited)

> Dated evidence note (per §How-to-re-verdict pt 4). Read-only verification
> sweep from the failsafe-wake 04:34Z session (fm PR #185, branch
> `claude/wake-0434z`); observation window 2026-07-14T04:37–04:45Z, all reads
> at live GitHub HEAD. Record stamped 2026-07-14T05:03:18Z (`date -u`).

| Item | State | Verdict | Evidence |
|---|---|---|---|
| pokemon-mod-lab PR #82 ("control: ORDER 007 — correct QoL+ pick Q-0266 citations…") | OPEN, mergeable_state clean, head `18024e4` | **NOT MERGED — no truing needed** | Both checks SUCCESS (ROM builds completed 04:13:25Z; substrate-gate 04:11:21Z). Dispatch-log row already says open — verified consistent at inbox/dispatch-log HEAD `e100bfe` |
| pokemon-mod-lab PR #66 | OPEN, parked (owner-click), head `5b1d71c` | **PARKED, healthy** | Both checks SUCCESS since 2026-07-13T22:20Z, no labels; auto-merge armed-state **NOT MEASURED** (gh CLI absent, REST disabled for session, GitHub MCP omits the auto_merge field) |
| Delivered-ORDER spot-check: superbot ORDER 005 | delivered, `status: new` | **VISIBLE at lane inbox HEAD** | superbot control/inbox.md @ main `50481b7` contains `## ORDER 005 · 2026-07-14T04:09:34Z · status: new` |
| Delivered-ORDER spot-check: substrate-kit ORDER 020 | delivered, `status: new` | **VISIBLE at lane inbox HEAD** | substrate-kit control/inbox.md @ main `c0297d8` contains `## ORDER 020 · 2026-07-14T04:12:12Z · status: new` (last ORDER in file) |

**Overnight fan-out landings (verified ~05:0xZ by the build pass):**
superbot #2094 MERGED 04:18:04Z · substrate-kit #361 MERGED 04:12:59Z ·
idea-engine #396 MERGED 04:10:55Z · sim-lab #127 MERGED 04:11:31Z.

**Sweep result:** all four overnight fan-out PRs landed; both delivered
ORDERs visible at lane inbox HEAD; pokemon-mod-lab #82 open/clean (no
dispatch-log truing needed) and #66 parked-healthy with the auto-merge
armed-state honestly NOT MEASURED for this session's toolset.

## 2026-07-14 · Trigger-health live verification — I1b decode resolved (dispatch 0530Z close)

> Dated evidence note (per §How-to-re-verdict pt 4). Coordinator-verified
> finding, recorded by the dispatch-0530Z close-out worker
> 2026-07-14T05:48Z (`date -u`); quoted verbatim:

"2026-07-14 ~05:35Z live verification (full 17-page list_triggers
pagination, ~1,642 routines): trig_01MWHvQFnRF1dVdZFSP6SM5L (superbot
night executor) and trig_011XAWqPeksS8LBrS5G9RvVc (superbot autonomous
dispatch) are both DISABLED/user-paused (enabled key absent = false;
ended_reason absent = user-paused). The dispatch routine's next_run_at is
frozen at the never-executed 2026-07-02T03:07 slot because a disabled
routine's next_run_at does not advance — the frozen-next_run WARN is the
expected footprint of a pause, NOT a scheduler fault. Neither is wedged;
neither fires until re-enabled. API decoding note for the checker:
`enabled` is OMITTED when false — I1b's ambiguous-enabled class can be
resolved to disabled-when-absent. Superbot ORDER 003 (delete or
annotate-and-leave-paused) remains the right disposition."

Checker follow-through (same PR, decide-and-flag):
`scripts/check_trigger_health.py` I1b now decodes an absent `enabled`
key as disabled, so the standing frozen-next_run WARN for disabled
routines downgrades to INFO (PASS); records stay listed, never dropped.

## Post-sweep final state — 2026-07-14 (measured 15:54–15:59Z)

> Dated evidence note (per §How-to-re-verdict pt 4). Synthesized from the
> three post-sweep measurement workers (windows 15:53–15:59Z, GitHub MCP +
> raw-at-main probes; recorded by the records-truing worker of PR #203,
> ~16:1xZ). Context: the owner's EAP-close PR sweep ran ~13:46–15:57Z and
> was **still in motion at measurement close** — superbot #2058 merged
> 15:55:33Z, superbot-next #312 15:56:42Z, and substrate-kit #373 15:57:20Z
> landed live *under* the measurement; expect further movement (WP legs).

| Repo | Open PRs (by-design holds named) | main HEAD + checks | audit@main | walkthrough@main | Newest heartbeat |
|---|---|---|---|---|---|
| superbot | 2 — #2102 (recon session, in-flight born-red, self-merges on green) · #2061 (held draft by design, deploy-safety) | `e2573407` (#2058 merge, 15:55:33Z) — Code Quality + CodeQL in_progress (fresh merge), 5 other checks success; prior main `30ed76a4` fully green | ❌ **MISSING** | ❌ **MISSING** (sole fleet gap) | 2026-07-13T18:00:00Z (no standing seat, Q-0264; "flip #2058" line now half-stale) |
| superbot-next | 10 — all by-design: WP legs #317/#335/#344/#371 (owner merge order) · #392 (parked) · #466/#473/#476/#477 (`do-not-automerge`) · #474 (claim) | `5981658` (#312 WP-2 merge, 15:56:42Z) — ci/substrate-gate/release success; golden-parity + named-gates in_progress (fresh merge) | ✅ (#468) | ✅ | 2026-07-14T14:30:20Z (fleet's newest) |
| substrate-kit | 0 (#373 merged 15:57:20Z under measurement) | `3092aa3` (#373 merge, 15:57:20Z) — run not yet indexed (seconds-old); v1.16.0 release run success 14:48–14:49Z | ✅ | ✅ (#368) | 2026-07-14T14:56Z (v1.16.0 CUT + VERIFIED) |
| websites | 0 (8 lifeboats closed unmerged 13:46Z; #324 owner-merged 13:54:55Z) | `ee47f8d` (kit v1.16.0 #338, 15:44:54Z) — no run at SHA yet; latest main runs all success | ✅ (#332) | ✅ (#336) | 2026-07-14T13:12:32Z (session closed, EAP wrapped) |
| venture-lab | 0 | `f9e8bfd` (kit upgrade #198, 15:41:54Z) — no runs at SHA (PR-triggered); prior main green | ✅ (seat, covers trading) | ✅ | 2026-07-14T10:21:38Z |
| trading-strategy | 0 | `f5e6e86` (kit upgrade #125, 15:42:20Z) — no runs at SHA; prior main green 14:39Z | ✅ | ✅ | 2026-07-14T10:11:08Z |
| idea-engine | 0 | `a754d7e` (kit upgrade #422, 15:41:59Z) — no runs at SHA; prior main green | ✅ (seat, covers sim-lab) | ✅ (#420) | 2026-07-14T12:51:46Z (EAP CLOSED) |
| sim-lab | 0 | `2725e4a` (#142, 12:53:45Z) — no post-07-12 main runs (PR-triggered); no red anywhere | — by design (seat audit at idea-engine) | ✅ (#141) | 2026-07-14T12:51:32Z (EAP CLOSED) |
| gba-homebrew | 0 | `fd471ba` (kit upgrade #137, 15:42:38Z) — no runs at SHA; newest main runs green 07-13 | ✅ | ✅ | ts 2026-07-14T11:41Z (append-only file) |
| pokemon-mod-lab | 0 — **entire 28-PR parked wave swept** | `7d4fa41` (#86 merge, 15:18:06Z) — rom-builds + substrate-gate SUCCESS | ✅ (#84, blob `69feea6f`) | ✅ (#86, blob `aade289d`) | 2026-07-14T05:07:37Z (pre-sweep content — stale by design until the lane's next write) |
| superbot-mineverse | 0 | `419d559` (kit upgrade #110, 15:45:45Z) — no runs at SHA; prior main green | ✅ (seat-wide, covers games + idle) | ✅ | 2026-07-14T11:34:32Z |
| superbot-games | 1 — #141 (kit v1.16.0 wave): all checks SUCCESS 15:40Z, auto-merge armed, `mergeable_state: clean`, pending merge latency | `717e36c` (#139+#140, 11:42:15Z) — no runs at SHA; prior main green | — by design (seat audit at mineverse) | ✅ (#139) | 2026-07-14T11:41:04Z (ORDER 009 complete) |
| superbot-idle | 0 | `ce5387c` (#132, 11:36:48Z) — no runs at SHA; prior main green | — by design (seat audit at mineverse) | ✅ (#132) | 2026-07-14T11:32:05Z |
| fleet-manager | 1 — #203 (this session, born-red by design) | `7044e4b` (kit upgrade #202, 15:42:28Z) — merge-on-green ×2 success at SHA | ✅ (#189) | n/a (not a walkthrough target) | 2026-07-14T14:07:26Z (pre-sweep — says "hub sweep still pending") |

**pml resolution (the sweep's headline):** PR **#84** (EAP seat audit)
MERGED 15:09:23Z (merge `a877b25f`) · **#85** (ORDER 009 dispatch) MERGED
15:11:37Z (merge `978dc0bd`) · **#68** CLOSED unmerged 15:15:39Z
(superseded by #84 per its own §C-3; was the wave's only red PR) · **#86**
(carries the pml walkthrough) MERGED 15:18:06Z — GitHub auto-retargeted its
base to main when #85's branch merged, no manual re-target needed; its
merge commit IS pml main HEAD `7d4fa41`, CI green. pml at **0 open PRs**.

**Branch-delta verdict:** the sweep deleted **NO branches** — websites 167
live `claude/*` = 167 census (byte-for-byte); superbot-next 148 live vs
146 census (+2 new same-day, 0 deleted). The census corollary (one-time
bulk deletion of the 460 exact-match survivors,
[branch-recreation census](findings/branch-recreation-census-2026-07-14.md))
**stands for a later sitting** (owner-checklist rows 4/11; owner-queue
B#59).

**Loose ends (2):** (1) **superbot hub missing BOTH EAP docs at main
`e2573407`** — the fleet's sole remaining EAP-doc gap; exact fix: one
docs-only superbot PR adding `docs/eap-closeout-walkthrough-2026-07-14.md`
+ `docs/audits/eap-project-audit-2026-07-14.md` (the same "(b) walkthrough"
item every other lane's ORDER carried). (2) **Sweep tail** — superbot-next
WP legs #317→#335→#344→#371 + games #141 still landing at ~16:00Z; no
action, self-resolving (fresh merges carry in-progress CI on their
minutes-old HEADs, normal).

**2026-07-14T19:51Z true-up — loose end (1) CLOSED:** superbot #2105
merged 18:52:49Z; both EAP docs verified at superbot main `0b90ad3`
(squash-merge = HEAD); fleet at 13/13 walkthroughs + audits.

**Heartbeat caveat:** the pml and fleet-manager heartbeats at main
pre-date the sweep (05:07:37Z / 14:07:26Z) and still describe pre-sweep
state — factually superseded; truing rides each lane's normal next wake,
no dedicated dispatch needed.

## 2026-07-15 · curious-research disposition (owner decision, live turn) + first v3.6 reboot sweep (04:01–04:03Z, read-only)

**curious-research verdict: PARKED** (owner decision 2026-07-15, live turn in
the coordinator chat). Purpose complete — the seat is **not** being rebooted
in the v3.6 wave and gets **no extension note** (delivery was twice-walled
— no repo, registry-only seat — and the question is now moot); the seat
awaits **a new mission from the owner** at a time of his choosing. The
Curious Research failsafe (`trig_014XdBFcgKwu2Rd9122NZo3S` · `20 */2 * * *`)
stays as registered; disposition of the trigger itself is the owner's call
when the new mission is defined.

**Reboot-sweep snapshot** (owner began firing v3.6 reboot prompts to most
projects ~2026-07-15T03:45Z; measured 04:01–04:03Z via
raw.githubusercontent.com `control/status.md` at HEAD, pml via GitHub MCP —
read-only, `date -u` wall clock): **0 of 17 seat-repo heartbeats are
post-03:45Z yet** — fully expected this early, since a rebooted seat only
stamps `control/status.md` at its session close, typically well after boot;
**neutral, no alarms**. Newest stamps: fleet-manager 2026-07-15T03:40:49Z
(the coordinator's own LIVE revival stamp, 4 min *before* the cutoff),
venture-lab 2026-07-14T23:53:28Z, idea-engine 2026-07-14T23:42:25Z; the
bulk of the fleet sits on 2026-07-14 EAP-shutdown-era stamps
(superbot-next 21:28Z, gba 21:16Z, trading 21:17Z, sim-lab 21:14Z,
websites 21:12Z, kit 21:03Z, mineverse 18:59Z, games 11:41Z, idle 11:32Z,
pml 05:07Z); superbot hub 2026-07-13T18:00Z (known Q-0264 no-standing-seat
lag), product-forge 2026-07-11 (DARK, archive-ready) and the three
codetool-lab repos 2026-07-09 (STALE-BY-DESIGN, no reboot expected).
Next sweep should start seeing post-03:45Z stamps as rebooted sessions
close; per-seat table in the session card
`.sessions/2026-07-15-cr-disposition-sweep.md` (fm PR #217).

## 2026-07-15 · second v3.6 reboot re-sweep (05:39–05:44Z, read-only)

Measured 05:39–05:44Z (`date -u`; heartbeats via raw.githubusercontent.com
`control/status.md` at HEAD, pml via GitHub MCP as private; newest
default-branch commits via GitHub MCP) against the 04:28Z baseline (fm PR
#220 heartbeat: 9/18 active post-03:45Z). **Delta: 5 seats show new
post-04:28Z activity, and the not-yet-rebooted set is unchanged at 9.** The
headline mover is **substrate-kit**, out of its 04:21Z all-triggers-deleted
STANDBY: heartbeat re-stamped 05:10Z ("EAP EXTENSION ACTIVE … routines
coordinator-managed") now carrying wake trigger `trig_01CUfSZo9Uky9DdpoqpZPcfT`
(a trigger id absent from roster gen #56 — re-arm evidence), newest commit
`5905201` 05:13:04Z (kit #383); the C#61 kit-go hold reads as resolved
lane-side. Also newly active: gba-homebrew `4a61ec9` 05:12:49Z (#143,
wickroad contracts v0.3), idea-engine (heartbeat 05:02:38Z + `85114c5`
05:06:06Z, PROPOSAL 065 round-13), sim-lab `b7a6859` 05:41:04Z (VERDICT 078
rejecting P065 — the generate→verify loop live end-to-end overnight), and
fleet-manager itself (heartbeat 05:04Z + `e4abf1d` 05:07:28Z, #221).
Rebooted-at-baseline but quiet since: superbot-next (newest `ad75bbc`
03:41Z), websites (`3cac461` 03:37:59Z), venture-lab (heartbeat 04:01:46Z,
`520bdfc` 04:10:05Z), pokemon-mod-lab (heartbeat 2026-07-14T05:07Z, newest
commit 2026-07-14T15:18Z). Still not rebooted — newest commits are the
coordinator's own 03:36–03:41Z extension-note relays or older, zero
seat-side post-04:28Z activity: superbot hub, trading-strategy,
superbot-games, superbot-idle, superbot-mineverse, product-forge, and the
three codetool-lab repos (STALE-BY-DESIGN / DARK, no reboot expected for
the last four). Neutral, no alarms: a rebooted seat only stamps at session
close, and the failsafe lattice covers the quiet lanes.

## 2026-07-15 · morning seat delta vs 06:26Z (08:12–08:15Z, read-only)

Measured 08:12–08:15Z (`date -u`; shallow clones at HEAD for heartbeat
`updated:` stamps + newest default-branch commits, codetool labs via
`git ls-remote`) against the 06:26Z baseline (fm heartbeat stamp 06:23:58Z /
`14b5d51`). **Delta: the idea-engine⇄sim-lab loop is the only seat-side
mover, and it is cycling fast** — idea-engine heartbeat re-stamped
07:58:02Z, newest commit `8b8fa6c` 08:01:57Z (#433, "cycles P064–P068
verdicted (V077–V081), loop live"); sim-lab newest commit `23cb87b`
08:13:39Z (#151, VERDICT 082 — WIP-cap dryness floor, P069). The other two
overnight-live lanes are quiet this window: substrate-kit HEAD unchanged at
`22fd280` 06:17:07Z (last act recorded the 06:05Z failsafe fire as honest
idle, #384; heartbeat 06:15Z, FRESH) and gba-homebrew unchanged at
`18ddd08` 06:22:06Z (#145, wickroad growth cut 4 v0.5 — landed just before
the baseline). Automated substrate movement only: fleet-manager roster
regen Gen #57 landed 06:38:33Z (`dbd64a3`, PR #224, roster-regen.yml) and
superbot hub took a bot dashboard-refresh merge `f8e2313` 06:33:22Z
(#2109) — routine, hub heartbeat still 2026-07-13T18:00Z (Q-0264/INC-16
lag, ACTIVE by pushes). **The un-rebooted set is unchanged at 9** (hub,
trading-strategy, superbot-games, superbot-idle, superbot-mineverse,
product-forge, codetool labs ×3): zero seat-side commits in the window —
newest movement remains the coordinator's 03:37–03:41Z EAP-extension-note
relays (trading `458b43c`, games `446a84e`, idle `8a7275d`, mineverse
`b9ade33`) or older (forge `f7f2dd2` 07-14, labs `5b0835b`/`0e0ec02`/
`0331176` unchanged). Rebooted-but-quiet also unchanged: superbot-next
(`ad75bbc` 03:41Z), websites (`3cac461` 03:37:59Z), venture-lab (`520bdfc`
04:10:05Z, heartbeat 04:01:46Z); pokemon-mod-lab still behind the private
auth wall (roster: NOT MEASURED). Neutral, no alarms — the reboot gap was
flagged to the owner in the ~07:10Z morning summary (A#62 + reboot gaps)
and the failsafe lattice covers the quiet lanes.

## 2026-07-15 · superbot-next verdict STALE — stalled mid-close (recon 10:02Z, recorded ~10:2xZ)

**Verdict: STALE (stalled mid-close), remedy in the owner's hands.** Evidence
from the 10:02Z reconnaissance: the superbot-next coordinator rebooted 04:20Z
and worked to **04:58Z**, then went dark **mid-close** — PR **#490** sits open
**born-red** (its in-progress session card never flipped; auto-merge is
armed-but-held by the card gate), and the main-branch heartbeat still falsely
reads **SEAT DORMANT** (pre-reboot residue the stalled close never corrected).
**No wake trace since ~05:01Z despite the 2-hourly failsafe** — the failsafe
lattice did not revive this seat, which is what upgrades the reading from
"quiet" to STALE. The seat's 9 other open PRs are **deliberately parked
owner-gated lanes**, not new drift: WP stack #344/#371/#392,
`do-not-automerge` #466/#473/#476/#477, outbox #484/#485. Net: **nothing
substantive dropped** — all queued work is owner-gated; the only casualty is
the unflipped #490 close + the false-dormant heartbeat. **Remedy is with the
owner** (advised live ~10:1xZ this morning): reply "continue" in the stalled
session so it finishes its close, or boot a fresh v3.6 session which will
adopt/flip #490 at orientation. No coordinator action owed beyond this
record; **revisit next sweep** — if a fresh trace or the #490 flip appears,
re-verdict to LIVE; if still dark, escalate the failsafe-didn't-fire question
as its own trigger-health item.

## 2026-07-15 · oversight-wake staleness sweep (12:51–12:54Z, read-only, SHA-cited)

> Dated evidence note (per §How-to-re-verdict pt 4). Per-lane heartbeat sweep
> from the 12:51Z oversight wake (fm PR #232): `updated:` stamps read via
> raw.githubusercontent.com `control/status.md` at HEAD (pml via GitHub MCP —
> private, raw-walled), HEADs via `git ls-remote`; wall clock `date -u`
> 12:53:42Z. Roster gen #59 (12:03Z, automated regen #231) verified fresh
> (0.8h, checker OK) — this sweep is the independent read on top of it.

| Lane | Heartbeat `updated:` | Age | Verdict | Citation |
|---|---|---|---|---|
| superbot (hub) | 2026-07-13T18:00:00Z | ~42.9h | DARK-heartbeat / hub-STEADY (ACTIVE by pushes, Q-0264 no-standing-seat lag, INC-16) | HEAD `f8e2313` (2026-07-15T06:33:22Z merge) |
| superbot-next | 2026-07-14T21:28:31Z (main; overwrite rides unlanded #490) | ~15.4h | **LIVE — re-verdict, see note below** (close COMPLETE; landing owner-gated) | HEAD `454ec71` 10:39:57Z; PR #490 head `0ea6338`, updated 11:38:39Z |
| substrate-kit | 2026-07-15T12:52Z | ~2m | FRESH | HEAD `4e29182` |
| websites | 2026-07-15T11:56:59Z | ~57m | FRESH | HEAD `4b7c20c` (advanced past roster's `8fb3ac5` @ 12:02:26Z); failsafe `trig_01VRT9F6jYNXym3nn18vVQQK` armed |
| venture-lab | 2026-07-15T04:01:46Z | ~8.9h | STALE-heartbeat (wake chain healthy — failsafe last fired 09:45:15Z, trigger-health OK) | HEAD `520bdfc` 04:10:05Z |
| trading-strategy | 2026-07-14T21:17:36Z | ~15.6h | STALE — by-design (KEEP-PARKED until 2026-07-17 grading) | HEAD `458b43c` |
| idea-engine | 2026-07-15T07:58:02Z | ~4.9h | STALE ⚠ commits-FRESH (ACTIVE, INC-16) | HEAD `828b18e` 11:37:33Z |
| sim-lab | 2026-07-15T04:06:11Z | ~8.8h | STALE ⚠ commits-FRESH (ACTIVE — VERDICT 089 landed mid-sweep) | HEAD `e26996b` 12:06:24Z (#158) |
| gba-homebrew | 2026-07-14T21:16:02Z | ~15.6h | STALE ⚠ commits-FRESH (ACTIVE by pushes) | HEAD `0048a5d` 11:01:26Z |
| pokemon-mod-lab | 2026-07-14T05:07:37Z (measured via GitHub MCP this sweep — raw fetch is auth-walled, roster prints NOT MEASURED) | ~31.8h | DARK-by-stamp / PARKED-owner-gated (its own heartbeat: "queue's session-servable remainder: NONE — every remaining item is owner-gated") | status blob `cf4643a` @ HEAD `7d4fa41` |
| superbot-mineverse | 2026-07-14T18:59:20Z | ~17.9h | STALE (no armed trigger — reboot gap) | HEAD `b9ade33` |
| superbot-games | 2026-07-14T11:41:04Z | ~25.2h | DARK (no armed trigger — reboot gap) | HEAD `446a84e` |
| superbot-idle | 2026-07-14T11:32:05Z | ~25.4h | DARK (no armed trigger — reboot gap) | HEAD `8a7275d` |
| product-forge | 2026-07-11T19:39:50Z | ~3.7d | DARK by standing decision — state UNCHANGED (no disposition note owed) | HEAD `f7f2dd2` unchanged |
| codetool-lab-sonnet5 | 2026-07-09T20:02:14Z | ~5.7d | STALE-BY-DESIGN | HEAD `0331176` unchanged |
| codetool-lab-fable5 | 2026-07-09T20:06Z | ~5.7d | STALE-BY-DESIGN (HEAD moved by the owner's #16 merge 10:54:19Z — expected, A#62 resolution) | HEAD `3f83cbb` |
| codetool-lab-opus4.8 | 2026-07-09T20:11:35Z | ~5.7d | STALE-BY-DESIGN (dormant KEEP, INC-03) | HEAD `0e0ec02` unchanged |
| fleet-manager | this wake | — | FRESH (PR #232) | branch `claude/oversight-wake-0715b` |

**superbot-next re-verdict (supersedes the 10:02Z "STALE — stalled mid-close"
verdict above):** the 10:02Z reading is falsified by later evidence — the seat
resumed and **completed its close-out**: PR #490 body carries a full
"Session close-out (2026-07-15)" section (commits `48246aa`…`0ea6338`; claims
swept, ORDER 023 acked+done, routine disposition recorded — failsafe
`trig_01UC7wiV3n5Vgs3RpSQt4gWz` stays armed, next fire 13:08Z), PR updated
11:38:39Z, and main took `454ec71` at 10:39:57Z. The card flip is NOT
forgotten — it is held by a documented, verbatim-quoted Self-Approval
classifier denial in the PR body; the lane's own recorded landing path is one
owner message in that coordinator chat: **"flip and land #490"**. The
false-dormant main heartbeat clears when #490 lands (its heartbeat overwrite
rides the PR). Verdict: **LIVE, close complete, landing owner-gated** — no
manager action owed beyond this record.

**DARK routing disposition (games · idle · mineverse-STALE · hub-heartbeat):**
all four sit in the known owner v3.6 reboot gap — no armed triggers since the
2026-07-14 EAP shutdown deletions, so no DRAFT ORDER is filed (a trigger-less
seat cannot consume one; writing one would be dead-letter). The standing
owner-queue home for seat boots is **C#36 (OQ-RESTRUCTURE-TRIGGER-CUTOVER)**,
and the gap was flagged to the owner in the ~07:10Z morning summary — carried
again on this wake's heartbeat next-2-tasks, no new queue item (dedup, R11).
product-forge stays excluded per standing decision (state unchanged).

## 2026-07-15 · merge-on-green verification + reboot-gap re-sweep (14:00–14:10Z)

> Dated evidence note (per §How-to-re-verdict pt 4). Read-only 19-repo
> verification sweep from the 14:xxZ dispatched working session (fm PR #233);
> four workers, raw+MCP, wall clock `date -u` 14:00:49–14:01:19Z at start.
> Full per-repo table + citations:
> [`findings/merge-on-green-rollout-verification-2026-07-15.md`](findings/merge-on-green-rollout-verification-2026-07-15.md).
> Headline: **13/19 merge-automation PROVEN (bot merge today) · 5/19
> installer-PR-open (today's 13:41–13:57Z rollout, nothing landed on any
> main) · 1/19 missing (sonnet5, skipped).**

**(a) The five installer-PR lanes — landing paths:**

| Lane | Landing-path note | Citation |
|---|---|---|
| codetool-lab-opus4.8 | no self-landing until owner merges installer [PR #24](https://github.com/menno420/codetool-lab-opus4.8/pull/24) | opened 2026-07-15T13:44:19Z, head `claude/install-merge-on-green` @ `342f793`, self-parked owner-merge-only |
| codetool-lab-fable5 | no self-landing until owner merges installer [PR #17](https://github.com/menno420/codetool-lab-fable5/pull/17) | opened 2026-07-15T13:49:04Z, head `ci/merge-on-green-automation` @ `b37b3ca`, self-parked |
| product-forge | no self-landing until owner merges installer [PR #25](https://github.com/menno420/product-forge/pull/25) | opened 2026-07-15T13:56:45Z, head `ci/merge-on-green` @ `78ff3bc`, self-parked; its body cites #24's 7+h green-unmerged wait as the motivating gap |
| pokemon-mod-lab | no self-landing until owner merges installer [PR #89](https://github.com/menno420/pokemon-mod-lab/pull/89) | opened 2026-07-15T13:56:05Z, head `claude/install-merge-on-green` @ `9e49a1e`, self-parked; #87/#88 sit open awaiting the owner sweep meanwhile |
| superbot-plugin-hello | no self-landing until owner merges installer [PR #3](https://github.com/menno420/superbot-plugin-hello/pull/3) — **and inert even then**: repo has zero CI (no `.github/` at main `5d97aa7`), and the sweep treats zero check runs as NOT-ready by design | opened 2026-07-15T13:41:30Z, self-parked; #1/#2 were hand-merged with zero check runs |

**(b) codetool-lab-sonnet5:** no merge automation at main `0331176` (only
ci.yml + release.yml), rollout skipped it entirely (0 open PRs, no installer
PR at 14:04Z); latest merge #17 2026-07-14T07:07:03Z by menno420 (manual).
Consistent with its ARCHIVE verdict / wind-down state (B#41) — verdict row
unchanged, gap recorded.

**(c) Reboot-gap re-sweep verdicts** (vs the 12:51–12:54Z sweep above; the
DARK/reboot-gap class established there stands — manager relay commits are
not seat-side signal):

| Lane | Heartbeat `updated:` | Age at 14:0xZ | Verdict | Citation |
|---|---|---|---|---|
| superbot-games | 2026-07-14T11:41:04Z (seat-written, ORDER 009 truth-stamp) | ~26.3h | **DARK — reboot gap continues** (no seat-side signal since; only newer main activity is the manager's ORDER 010 relay commit `446a84e` 03:38:31Z) | status @ main `446a84e`; 0 open PRs |
| superbot-idle | 2026-07-14T11:32:05Z (seat-written, ORDER 008 re-stamp) | ~26.5h | **DARK — reboot gap continues** (same pattern; only the ORDER 010 relay `8a7275d` 03:38:39Z since) | status @ main `8a7275d`; 0 open PRs |
| superbot-mineverse | 2026-07-14T18:59:20Z (cross-seat relay written by a games worker) | ~19h | **STALE** (no armed trigger — reboot gap; only the ORDER 009 relay `b9ade33` 03:40:11Z since) | status @ main `b9ade33`; 0 open PRs |
| superbot (hub) | 2026-07-13T18:00:00Z (no-standing-seat/irregular by design, Q-0264) | ~44h (stamp) | **FRESH via HEAD-activity fallback** — same-day merge #2111 at 12:54:46Z (main `3fb5dd0`) + 2 intentional open PRs (#2110 docs 10:24:32Z; #2061 held draft, Q-0193) | HEAD `3fb5dd0`; hub doctrine per status header |

## 2026-07-15 · A#68 installer clicks LANDED — merge-automation coverage 18/19 (oversight wake, 16:59–17:05Z, read-only verify)

> Dated evidence note (per §How-to-re-verdict pt 4). Supersedes the 14:0xZ
> note's "(a)" landing-path table above: the owner merged all five installer
> PRs 2026-07-15T15:29:41–15:29:52Z (each `merged_by menno420`), and the
> workflow file is verified at each repo's live main. Owner-queue A#68
> (OQ-ROLLOUT-INSTALLER-CLICKS) swept to Resolved; full verification table:
> [`findings/merge-on-green-rollout-verification-2026-07-15.md`](findings/merge-on-green-rollout-verification-2026-07-15.md)
> § Addendum 17:0xZ. Recorded by fm PR #241.

| Lane | Landing path NOW | Citation |
|---|---|---|
| codetool-lab-opus4.8 | **self-landing PROVEN** *(flipped 2026-07-15 ~20:3xZ, evening oversight wake, fm PR #245)* — probe [#25](https://github.com/menno420/codetool-lab-opus4.8/pull/25) `merged: true`, merged_by **github-actions[bot]**, merged_at 2026-07-15T15:30:46Z (~62 s after install) | #24 merged 15:29:44Z |
| codetool-lab-fable5 | **self-landing PROVEN** — probe #18 merged_by github-actions[bot] 16:54:14Z | #17 merged 15:29:47Z; main `e7ca47c` |
| product-forge | **self-landing PROVEN** *(flipped 2026-07-15 ~20:3xZ, evening oversight wake, fm PR #245)* — probe [#26](https://github.com/menno420/product-forge/pull/26) `merged: true`, merged_by **github-actions[bot]**, merged_at 2026-07-15T15:30:14Z (~24 s after install; the 7+h green-unmerged wait class is closed) | #25 merged 15:29:50Z |
| pokemon-mod-lab | **self-landing PROVEN** — probe #90 merged_by github-actions[bot] 15:30:22Z, ~30 s after install | #89 merged 15:29:52Z; main `ec63823` (file via MCP Contents API) |
| superbot-plugin-hello | **installed but INERT** — zero CI in repo, zero check runs = NOT-ready by design; needs a minimal CI gate (agent-doable) or accept-as-inert (see register row) | #3 merged 15:29:41Z; main `abd9133` |

Fleet headline *(updated 2026-07-15 ~20:3xZ, evening oversight wake, fm
PR #245 — both former installed-unproven rows flipped PROVEN on live
`merged_by github-actions[bot]` evidence above)*: **18/19 covered — 17
PROVEN · 0 installed-unproven · 1 installed-inert (plugin-hello) · 1
MISSING (codetool-lab-sonnet5, ARCHIVE-candidate B#41 — rollout skipped
it by design).** fm #227 (A#63): conflict RESOLVED by the evening wake
(merge main in + lanes.json regen to Gen #63, head `45ba285`,
mergeable_state now `unstable` = awaiting checks) — owner click applies
on green.

## 2026-07-15 · Evening oversight wake (20:26Z sweep, fm PR #245) — seat staleness verdicts

> Dated evidence note. Probes 2026-07-15T20:26–20:29Z via the GitHub API
> (heartbeat file at HEAD + newest main commit + open PR count per repo).
> The DARK/reboot-gap class from the 12:5xZ / 14:0xZ sweeps above
> **stands and has now crossed the >30h escalation bar for games + idle**
> — the only newer main activity on all three World lanes is the
> externally-dispatched merge-automation verification probe of
> 14:19–14:45Z, which is not seat-side signal (same rule as the
> manager-relay exclusion above). Escalated on owner-queue **C#36**
> (boot-sitting recommendation).

| Lane | Heartbeat `updated:` | Age at 20:26Z | Newest main commit | Open PRs | Verdict |
|---|---|---|---|---|---|
| superbot-games | 2026-07-14T11:41:04Z (seat-written) | **~32.8h** | `1543c4b` #146 probe merge 2026-07-15T14:45:35Z (not seat-side) | 0 | **DARK >30h → ESCALATE** |
| superbot-idle | 2026-07-14T11:32:05Z (seat-written) | **~32.9h** | `a37d00e` #140 probe merge 2026-07-15T14:19:48Z (not seat-side) | 0 | **DARK >30h → ESCALATE** |
| superbot-mineverse | 2026-07-14T18:59:20Z (cross-seat relay) | ~25.5h | `ac2b874` #114 probe merge 2026-07-15T14:24:01Z (not seat-side) | 0 | **STALE** (under the 30h bar) |
| superbot (hub) | (no-standing-seat/irregular by design, Q-0264) | n/a | `82c68e3` merge #2115 2026-07-15T19:41:35Z | 2 (#2110 ready · #2061 held draft, both intentional) | **FRESH via HEAD-activity** (~0.7h) |

## 2026-07-16 · Maintenance-wake staleness sweep (01:10–01:15Z, read-only, fm PR #253)

> Dated evidence note. Probes 2026-07-16T01:10–01:15Z via `fleet_status.py`
> (superbot copy; raw heartbeat reads at HEAD) + this wake's fresh
> `list_triggers` export (telemetry/triggers-snapshot.json,
> captured_at 2026-07-16T01:08:37Z, 1954 records / 14 enabled).
> Context: the owner rebooted the fleet on the v3.7 prompt registry tonight
> (ORDER 048 landed fm #252; owner live turn ~01:0xZ relayed by the
> coordinator) — most seats re-stamped within the hour.

| Lane | Heartbeat `updated:` | Age at 01:10Z | Verdict | Evidence |
|---|---|---|---|---|
| idea-engine | 2026-07-16T01:07:29Z | ~3m | **FRESH** (v3.7 close-out stamp) | raw status @ HEAD |
| venture-lab | 2026-07-16T01:02:15Z | ~8m | **FRESH** | raw status @ HEAD |
| trading-strategy | 2026-07-16T01:01:39Z | ~8m | **FRESH** | raw status @ HEAD |
| superbot-mineverse | 2026-07-16T00:55:09Z | ~15m | **FRESH — reboot gap CLOSED** (ORDER 009 ack, seat-side signal; was STALE 20:26Z) | raw status @ HEAD |
| substrate-kit | 2026-07-16T00:55Z | ~15m | **FRESH** (worker-slice wake 00:39Z) | raw status @ HEAD |
| gba-homebrew | 2026-07-16T00:49:49Z | ~20m | **FRESH — DARK cleared** (ender heartbeat; was DARK ⚠ commits-FRESH at Gen #65) | raw status @ HEAD |
| superbot-next | 2026-07-16T00:22:00Z | ~48m | **FRESH** (merge-queue session landed; main `6047618`) | raw status @ HEAD |
| websites | 2026-07-15T23:00:21Z | ~2.2h | **FRESH** (owner-ender close; failsafe bridge armed) | raw status @ HEAD |
| fleet-manager | 2026-07-15T23:04:37Z | ~2.1h | **FRESH** (this wake re-stamps it) | this PR |
| superbot-games | 2026-07-14T11:41:04Z | ~37.5h | **DARK by own stamp — but header says "status FROZEN — read mineverse's"**: the World seat's live heartbeat is mineverse (FRESH 00:55Z), so the seat is LIVE; the games file itself stays frozen by design. No new escalation; C#34–36 boot-sitting asks remain the owner-side record until the coordinator's morning verification. | fleet_status.py header + mineverse stamp |
| superbot-idle | 2026-07-14T11:32:05Z | ~37.6h | **DARK by own stamp — FROZEN by design** (same pattern as games; seat LIVE via mineverse) | same |
| superbot (hub) | 2026-07-13T18:00:00Z | ~2.3d | **FRESH via HEAD-activity fallback** (INC-16 — hub has no standing seat, Q-0264; newest commit ~16m at Gen #65) | roster Gen #65 divergence note |
| sim-lab | 2026-07-15T04:06:11Z | ~21h | **STALE by stamp — seat LIVE via sibling** (Ideas Lab seat's idea-engine half closed out 01:07Z tonight; sim-lab half last stamped 04:06Z). Watch item: if sim-lab shows no seat-side signal by the next wake, route a dispatch rung (R27) via the coordinator. | raw status @ HEAD |
| curious-research | 2026-07-14T21:23Z | ~28h | **DORMANT by owner order** (2026-07-14 live turn) — by design, never re-wake on staleness | status phase line |
| product-forge | 2026-07-11T19:39:50Z | ~4.2d | **ARCHIVE-READY by design** (close-out complete; awaiting owner archive click) | register row |
| codetool-labs ×3 | 2026-07-09 | ~6d | **STALE-BY-DESIGN** (wind-down complete; B#41/B#42 archive clicks) | register rows |
| pokemon-mod-lab | n/a | n/a | **PRIVATE (auth wall — not DARK)**: raw reads 404; ROSTER_READ_TOKEN pending (B-section ask) | fleet_status.py wall line |

**DEAD verdicts this sweep: none. New DARK routings: none needed** — every
DARK-by-stamp row above is either frozen-by-design (games/idle), design-dormant
(curious-research, labs, product-forge), an auth wall (pml), or covered by
INC-16 HEAD-activity (hub). The 2026-07-15 evening escalation (games+idle DARK
>30h → C#36) is superseded in practice by tonight's v3.7 reboot — mineverse
carries fresh seat-side World signal; the C#34–36 items stay open pending the
coordinator's morning platform-side verification.

**Trigger-registry anomaly (report-only, coordinator-relayed + confirmed in
this wake's export):** legacy `trig_011XAWqPeksS8LBrS5G9RvVc` "superbot
autonomous dispatch" (cron `0 */3 * * *`, `enabled` ABSENT in the API record,
next_run_at frozen 2026-07-02T03:07Z) — already dispositioned by the
2026-07-13 I1b note above and the 2026-07-14 I1b decode (absent `enabled` =
DISABLED; expected pause footprint). This wake's `check_trigger_health.py`
reads it I1b PASS/INFO. No action taken; delete-if-unwanted stays an owner
Routines-screen option. Also noted (capture-window artifact, not a pile-up):
four seat failsafes appear doubled enabled in the 01:08Z snapshot because the
coordinator's live re-arm cutover (new ids created 00:55–01:03Z) overlapped
the export; the coordinator relayed post-verify deletion of the old FM
failsafe (`trig_01LgMqjbBHsNTWMe6T3vaWmk` → successor
`trig_01UNjDKaaiGuUTvyfQGLKLrn`). I8 WARN rows recorded in the snapshot
capture_notes; next wake's export should show the old ids gone — re-check
then, coordinator-seat triggers are report-only for this session.

**I8 re-check (fresh full export 2026-07-16T01:44–01:49Z, 20 pages / 1964
records / 17 enabled → `telemetry/triggers-snapshot.json` captured_at
01:49:00Z, assembled by the new `scripts/assemble_triggers_snapshot.py`;
fm PR #255, read-only): verdict WARN — the doubles are REAL, not a
capture-window artifact.** Per old id: FM `trig_01LgMqjbBHsNTWMe6T3vaWmk`
**ABSENT** (deleted as relayed; successor `trig_01UNjDKaaiGuUTvyfQGLKLrn`
sole FM failsafe, next fire 02:32Z — I4 PASS) · Websites
`trig_01VRT9F6jYNXym3nn18vVQQK` **PRESENT+ENABLED** (new
`trig_01Cn7F2UvE62uDykSYQCDhtF` also enabled, same `45 */2`) · Venture Lab
`trig_01GeQiMM3nHMQTyuLMsWj7q3` **PRESENT+ENABLED** (new
`trig_01Er6TUtwybs9D9EuHCH32qX`, same `45 1-23/2`) · SuperBot World
`trig_01RwQK2cBpgvY2xc2LZPSNtQ` **PRESENT+ENABLED** (new
`trig_01B32hfwxfA67orKfBzQVdmU`, same `15 1-23/2`). Plus a FOURTH pair the
01:08Z export predated: SuperBot 2.0 `trig_01UC7wiV3n5Vgs3RpSQt4gWz` (old,
2026-07-15T04:07Z) + `trig_01E86nBnXqesQTwm6WA4mSUD` (new, 2026-07-16T01:07Z),
same `0 1-23/2`. `check_trigger_health.py` on the fresh snapshot: **PASS —
8/9 green, 1 WARN (I8 ×4 groups: superbot-2.0 · superbot-world · venture-lab
· websites)**. Those seats double-fire each wake window until the old ids are
deleted; disposition (live-verify each pair, delete the OLD id — the NEW ids
are the cutover's installed keepers) belongs to the coordinator seat that ran
the re-arm; this session touched no trigger (report-only per the wake brief).

## 2026-07-16 · night audit (wake session, seats read at origin/main HEAD ~01:15Z)

Verdicts (evidence = each seat's own control/status.md + control/inbox.md + backlog docs):

| seat | verdict | evidence |
|---|---|---|
| superbot (hub) | BUSY | ORDER 004 items 4–8 unfinished (recon guard absent from scripts/); 249 idea files; heartbeat 2.3d stale by design (Q-0264) |
| superbot-next | BUSY | baton: #457 conform sweep + boot cutover; 27-row REWORK backlog (docs/review/curation-report-2026-07-13.md) |
| websites | BUSY | docs/ideas/backlog.md ~1,936 lines; gated on 2 owner clicks (#345, #343) + 1 manager verdict (outbox SIM-REQUEST #355) |
| substrate-kit | BUSY | 48 ideas; archive-ready plan S3–S5 remain (docs/planning/2026-07-15-archive-ready-close-out-plan.md) |
| trading-strategy | BUSY (shallow ~1–2 nights) | round-7 pre-registered plan + Fri 09:00Z grading executor; AMBIGUITY: current-state says round-7 "awaits owner direction" while the plan reads self-startable — owner line requested |
| venture-lab | BUSY (shallow) | baton: grading executor + main-verify proof run; 10 publish-READY SKUs owner-click-gated; stranded telemetry commit d1b0208 not on main at f8ccc60 |
| superbot-games | BUSY | ORDER 008 wiring gated on fm relay of sim verdicts V075/V076; mining gen-2 baton 5 items (control/status-mining.md) |
| superbot-idle | THIN | own "honest thin list"; roadmap items gated; sanctioned filler = catalog wave 6 (ORDER 007 item 1). DISCREPANCY: a roster read tonight called it frozen-by-design; the seat was ACTIVE by pushes ~1h45m before audit |
| superbot-mineverse | THIN | fresh reboot heartbeat 00:55Z; only currently-doable baton item = mirror superbot-idle's #142 reconcile-race fix |
| gba-homebrew | BUSY | NEXT-MENU 7 arcs, in-doc rec B1 = 5 designed Tiltstone cuts (docs/NEXT-MENU-2026-07-15.md) |
| idea-engine | BUSY | standing generative rotation (ORDER 003/004); baton: shepherd parked #444, draft P080 |
| sim-lab | THIN | reactive; queue = 1 item (V092/P079) blocked on idea-engine #444; NOT silent — Ideas Lab shipped sim-lab PRs #146–#162 after its 04:06Z heartbeat stamp (INC-16 heartbeat-lag class) |

Findings: (1) The v3.6/v3.7 reboot is working — 7 seats posted fresh heartbeats
with concrete batons within ~2h (websites 23:00Z · next 23:03Z · kit 23:05Z ·
mineverse 00:55Z · trading 01:01Z · idea-engine 01:07Z · venture 01:12Z); 9/12
seats BUSY with no new dispatch. (2) Top misread class remains
heartbeat-vs-commit divergence (INC-16): 6 seats read DARK/STALE on roster gen
#65 while actively shipping; the pending E#66 doctrine ruling plus
substrate-kit's heartbeat-verb idea (kit docs/ideas/heartbeat-verb-2026-07-09.md)
would retire most false-DARK sweeps. (3) fm ORDER 047/048 fan-out is open: 0
lane inboxes cite them. (4) THIN-lane dispatch and the substrate-kit exchange
were NOT executed: agent-side lane-inbox writes are classifier-walled tonight
(see docs/CAPABILITIES.md, 2026-07-16 entry); routed to the owner queue.
Skipped: pokemon-mod-lab (auth wall, OQ #49). No-ORDER by standing decision:
product-forge (E#63), codetool-labs ×3 (B#41/B#42), plugin-hello (inert). No
repo unreachable; no quota denials.

## 2026-07-16 · night watch (coordinator)

*(Recorded 2026-07-16T06:5xZ by the morning wake slice, fm PR #257. Source:
coordinator-worker observations relayed in the dispatch — **LEADS, not
independently verified** except the rows marked VERIFIED, which were
cross-checked live against GitHub this wake. Q-0120 governs: re-verify any
LEAD against live source before acting on it.)*

**Overnight pulses (coordinator-reported, LEAD):** sweeps at 02:45Z and
04:15Z; 8 seats shipped 01:00–02:45Z and 5 more by 04:15Z; zero genuine CI
failures across the night — every red was a designed born-red HOLD, not a
failure. Not independently measured this wake ("not measured" beats
invention; the per-seat PR lists live with the coordinator session).

**idea-engine #446 — VERIFIED:** self-recovered and MERGED
2026-07-16T02:58:32Z by github-actions[bot], head `dda8a54`
(https://github.com/menno420/idea-engine/pull/446). Coordinator claim
confirmed exactly.

**Open owner dispositions at the morning handoff:**

- **websites #357 — VERIFIED open + DRAFT** (rerun-ci jobs-preflight,
  head `e8f1c78`, updated 01:23:59Z). PR body records the ready-flip
  attempt rate-limited verbatim: "API rate limit already exceeded for
  user ID 225413533"; the coordinator additionally reports a later flip
  attempt classifier-walled (LEAD). Owner one-click: mark ready.
- **websites #343 — VERIFIED RESOLVED:** the bake PR the coordinator
  reported green-but-blocked ~21h (next-bake 07:25Z collision risk)
  MERGED 2026-07-16T04:52:54Z by github-actions[bot], head `0d1d84b` —
  the disposition self-cleared after the report; the 07:25Z bake-collision
  risk is moot.
- **superbot-next #484 / #485 — VERIFIED both open, mergeable_state
  `dirty` (merge-conflicted):** informational lane→manager outbox asks,
  both bodies explicitly "do not auto-merge / arm". Coordinator reports
  them likely superseded and a manager close attempt classifier-denied
  (LEAD — denial text lives with the coordinator session). Disposition
  recommendation: close-with-reason once their outbox content is
  confirmed mirrored at HEAD.
- **Owner-release draft queue (coordinator-reported, LEAD):** superbot
  #2061 · superbot-next #499/#500 · superbot-games #149 · superbot-idle
  #145 · gba-homebrew #153 · trading-strategy #134 · websites #345 —
  drafts held for owner release, in tension with ORDERs 047/048
  (feature PRs land on green; owner never reviews PRs) pending lane
  adoption of the fan-out. Not re-verified per-repo this wake.

**Wall class (recorded):** agent-side directive writes on relayed
authority are classifier-denied — 6+ same-shape denials overnight per the
coordinator (7 recorded in the canonical entry); canonical record +
verbatim sample: docs/CAPABILITIES.md, 2026-07-16 WALL entry. Unlock =
owner-live venue.

## 2026-07-16 PM sweep — fleet oversight wake (PR #262)

**Manager:** wake-0716-pm oversight seat · sweep ~2026-07-16T15:00Z. Live signals: superbot `scripts/fleet_status.py` + raw heartbeat reads + live GitHub PR state. pokemon-mod-lab skipped (DARK/private).

**fleet-manager:** roster Gen #70 generated 2026-07-16T14:35Z (0.3h — fresh). 0 open PRs besides this one; night PRs #253–#256 + Gen-roster PRs #257–#261 all terminal on main. PR #227 verified still MERGED 2026-07-15T22:47:58Z; its owner-queue item (OQ-FM-PR227-MERGE) was already resolved by the earlier fm PR #253 wake — re-confirmed resolved this sweep, no open item remained.

| Seat | Heartbeat (UTC) | Class | State |
|----|----|----|----|
| idea-engine | 2026-07-16T14:33Z | FRESH | PROPOSAL-083 pipeline (PR #453); owner-ask ⚑ |
| trading-strategy | 2026-07-16T14:48Z | FRESH | active; weekly grading |
| substrate-kit | 2026-07-16T14:48Z | FRESH | seat closing, work PR #429 |
| websites | 2026-07-16T09:00Z | FRESH | worker session; PR #365; main green (1588 tests); owner-ask ⚑ |
| sim-lab | 2026-07-16T09:37Z | FRESH | V095 slice (PR #167); green on main |
| venture-lab | 2026-07-16T02:46Z | STALE (~12h) | wake candidate; owner-ask ⚑ |
| superbot-next | 2026-07-16T01:14Z | STALE (~14h) | rebuild loop live; slice #457 dispatched |
| superbot-mineverse | 2026-07-16T00:55Z | STALE (~14h) | ORDER 009 ack; green; owner-ask ⚑ |
| gba-homebrew | 2026-07-16T00:49Z | STALE (~14h) | ender heartbeat; owner-ask ⚑ |
| superbot-games | 2026-07-14T11:41Z | STALE by design | FROZEN (EAP closeout) |
| superbot-idle | 2026-07-14T11:32Z | STALE by design | FROZEN (EAP closeout) |
| product-forge | 2026-07-11T19:39Z | STALE by design | archived; blocked on owner OA-003 (enable GitHub Pages); no wake armed |
| superbot-plugin-hello | none | DARK | plugin scaffold, no heartbeat file — not an active seat |
| pokemon-mod-lab | — | skipped | DARK/private |

**Verdicts:**
- **Wake candidates** (aged-but-active ~12–14h, not by-design frozen): superbot-next, gba-homebrew, superbot-mineverse, venture-lab. Routing a wake ORDER to these lane inboxes is cross-repo → agent-side classifier-walled on relayed authority this turn → flagged to coordinator/owner-live venue, not written here.
- **STALE-by-design (no action):** superbot-games, superbot-idle (FROZEN, EAP-ended 2026-07-14); product-forge (archived, blocked on owner OA-003).
- **DARK:** superbot-plugin-hello (scaffold, no seat), pokemon-mod-lab (private, skip).
- **ORDER 047 & 048 fan-out still OPEN:** 0 lane inboxes cite them (re-confirmed this sweep). Cross-repo lane-inbox appends classifier-walled → owner-live venue. ⚑ coordinator.
- **ORDER 049:** does not exist at HEAD — a prior coordinator session was classifier-blocked before landing it; text unrecoverable from tree. ⚑ coordinator to recover.
- **Owner-ask fan-out:** 8 seats carry `⚑ owner-ask` blocks → candidate for a consolidated owner-queue pass.
- **Trigger health:** I6 SNAPSHOT-FRESH FAIL (triggers snapshot 8.1h stale, 06:47Z export) + I8 DUPLICATE-CRON WARN ×4 (old+new failsafe crons enabled on superbot-2.0/superbot-world/venture-lab/websites). Cutover-seat lane; coordinator session cse_01WwuStAe6JuMatMRdiA8Zsi is verifying/re-arming the FM failsafe cron this turn. ⚑ coordinator.

## 2026-07-16 · late-evening sweep (overnight run)

- **2026-07-16 ~21:45Z late-evening sweep (overnight run):** No verdict changes since the 15:00Z PM sweep. Deltas: roster advanced Gen #71→#74 (regen cron, all-clear); trigger-health now FAIL on I6 (snapshot export 2026-07-16T15:26Z is ~6.3h stale vs 4h bar — refresh `list_triggers` before acting; coordinator-session bound); standing I8 DUPLICATE-CRON WARN ×4 unchanged (keep-OLDEST is a sibling-lane call, not actioned). Roster + owner-queue checks green at HEAD 68f7994.

## 2026-07-17 · overnight run analysis

*Source: coordinator overnight audit 2026-07-17 (git-verified). Window 2026-07-16T21:45Z → 2026-07-17T06:30Z, 15 repos.*

**Run split.** 10 seats produced merged output. idea-engine ↔ sim-lab ran the proposal/verdict pipeline continuously to V104 (last landing 06:20Z). Most other seats did a single menu burst ~22:00–22:25Z, then idled.

**INCIDENT — decision-freeze ("one parked decision froze the loop").** The superbot-next seat produced zero repo output after ~23:00Z despite an awake chat. Its coordinator let the #499/#500 consent question freeze the entire work loop instead of parking only those two PRs — contrary to the standing continue-past-blockers doctrine. The loop resumed the morning of 2026-07-17 after owner contact.

**INCIDENT — draft-parking.** gba-homebrew opened 10 PRs overnight, all left as unmerged drafts (classifier-denied ready-flips; auto-merge skips drafts). pokemon-mod-lab showed the same pattern (2 parked PRs, including its heartbeat). Night output exists; none landed.

**Quiet seats.** superbot-mineverse — no wake fired since ORDER 010 landed 2026-07-16. product-forge — frozen by design.

**EAP recreation A/B note.** These two stall classes (decision-freeze, draft-parking) are exactly what to measure in recreated vs. control projects — see [`docs/project-recreation-runbook.md`](./project-recreation-runbook.md).

## 2026-07-17 · owner execution — gba main gate repaired

*Records close-out of the owner-actions-2026-07-17 §1–§3 execution (09:17–10:19Z; fm PR #281). Per-PR state re-verified live via `get_pull_request` before writing (Q-0120).*

- **gba-homebrew main substrate-gate REPAIRED** via [#153](https://github.com/menno420/gba-homebrew/pull/153) (MERGED 2026-07-17T09:17:04Z, the DO-FIRST flip) — the read-path-reachability orphan-fix that was red since #151. Consequence: the ~27 **parked arc PRs** (#154–#180) do NOT auto-clear; they inherited the gate-red and each need an **agent rebase onto #153's fix** before landing. This is **game-lab seat lane work, NOT a manager task** — flagged here so the next fleet sweep routes it to the lane, not the owner queue.
- **Draft-parking incident (2026-07-16: gba 10 drafts, pokemon 2) partially resolved by owner execution:** pokemon-mod-lab #87 CLOSED-unmerged (10:17:04Z, D1 rec) and #94 MERGED (09:19:06Z, overnight veto menu now on main). The gba draft backlog persists as the rebase-onto-#153 lane work above.

## 2026-07-17 · fm wind-down housekeeping — trigger-snapshot refresh + failsafe dedup evidence (fm PR #288)

*Source: fm wind-down housekeeping PR #288. Triggers read READ-ONLY via `list_triggers` (24-page cursor-to-exhaustion export, captured 2026-07-17T16:32:25Z — 2331 records / 3 enabled), assembled by `scripts/assemble_triggers_snapshot.py`, validated through `check_trigger_health.py`. NO trigger was created, modified, fired, or deleted by this seat.*

- **(a) Sibling duplicate failsafe-cron pairs — the roster-flagged I8 set — have SELF-RESOLVED; recorded here as dedup evidence, NOT actioned (SIBLING-owned; FM never mutates sibling triggers).** The four pairs `roster.md` (Gen #81) still lists:
  - **websites** — `Websites failsafe wake` · `45 */2 * * *` · `trig_01Cn7F2UvE62uDykSYQCDhtF` + `trig_01VRT9F6jYNXym3nn18vVQQK`
  - **venture-lab** — `Venture Lab failsafe wake` · `45 1-23/2 * * *` · `trig_01Er6TUtwybs9D9EuHCH32qX` + `trig_01GeQiMM3nHMQTyuLMsWj7q3`
  - **SuperBot World** — `SuperBot World failsafe wake` · `15 1-23/2 * * *` · `trig_01B32hfwxfA67orKfBzQVdmU` + `trig_01RwQK2cBpgvY2xc2LZPSNtQ`
  - **SuperBot 2.0** — `SuperBot 2.0 failsafe wake` · `0 1-23/2 * * *` · `trig_01E86nBnXqesQTwm6WA4mSUD` + `trig_01UC7wiV3n5Vgs3RpSQt4gWz`

  All eight ids were **enabled** in the prior 2026-07-17T11:43:57Z snapshot; **all eight are ABSENT from the 16:32:25Z exhaustive export** (0 hits across all 24 raw pages, live-verified). The sibling seats collapsed each pair to a single trigger during their own wind-down (new singletons in the export: `SuperBot 2.0 failsafe wake` `trig_01GBaDCsMzgjwPbQCiKzyRDC` created 16:20Z; `Ideas Lab failsafe wake` `trig_01DQu7LbHvP8ZqC31douQTAe` 16:11Z). Consequence: **I8 DUPLICATE-CRON now PASS** (was the standing WARN ×4) — the documented project-recreation dedup sweep is **moot** for this set; no owner/lane action owed. (`roster.md` still shows the old pairs because Gen #81 was built from the 11:43Z snapshot; it self-corrects on the next regen against the refreshed snapshot.)
- **(b) Trigger-health I6 SNAPSHOT-FRESH refreshed this PR.** `telemetry/triggers-snapshot.json` was stale (prior capture 11:43:57Z); the 16:32:25Z full re-export cleared it — **I6 now PASS** (0.0h old vs the 4h bar). Recorded in the snapshot's `_retired` marker as a final I6-clearing refresh; no further refreshes are planned.
- **⚑ Surfaced by the refresh, NOT actioned (no trigger mutations this seat): I4 MANAGER-FAILSAFE now FAIL.** The FM failsafe cron `trig_01An9YmU3KC1kLhB5c9cv4Ax` (`Fleet Manager failsafe wake` · `30 */2 * * *`, enabled in the 11:43Z snapshot) is ABSENT from the 16:32Z export — the FM seat has no enabled standing-cron dead-man backstop. Consistent with the autonomous-apparatus wind-down; flagged for owner awareness, re-arm only if the FM seat is retained past recreation.
- **(c) DRIFT CHECK — registry docs/prompts/v3 == the pasted `v3.7 · 2026-07-15` line: EQUAL. No re-paste owed.**

## 2026-07-18 · overnight oversight sweep (verified read-only vs live GitHub)

*Source: fm overnight-oversight seat, 2026-07-18. Every per-repo claim re-verified live via github MCP (`list_pull_requests` / `get_commit` / `get_check_runs`) before writing (Q-0120 — never against report text). Oversight-only: recorded here, never pushed to sibling repos.*

- **gba-homebrew — 13 open PRs** (was ~27 #154–#180; the rest rebased onto [#153](https://github.com/menno420/gba-homebrew/pull/153)'s read-path-reachability fix / cleared). Split:
  - **3 non-draft born-red: #154, #165, #176** — CHEAPEST FIX: flip each in-progress card to ready → auto-lands on green (lane-side action). These are structurally able to auto-land the moment their card flips.
  - **10 draft born-red: #157, #158, #159, #160, #161, #162, #163, #164, #177, #178** — draft + in-progress card = structurally *cannot* auto-land (draft PRs never trigger the landing workflow); **lane decides consolidate-or-close.**
  - substrate-gate born-red confirmed (#154 / #158 / #165: substrate-gate = failure, ROM builds = success) via check-run conclusions. Lane **ALIVE** (main advancing past #153). → owner-queue `OQ-GBA-DRAFT-PILE`.
- **superbot-mineverse #120 — RESOLVED** (auto-merged 2026-07-17T23:03:35Z by github-actions[bot], head `9ef495e`). No action.
- **product-forge — STALLED confirmed** (main HEAD `1efbb3b`, 2026-07-15T15:30Z, "merge-automation verification probe (#26)"; ~2d old + heartbeat ~6d stale). Consistent with the existing `OQ-FORGE-DISPOSITION` archive-ready row — **CONFIRM only, no new item.**
- **Frozen-by-design (evidence-checked):** superbot-plugin-hello, codetool-lab-fable5 / -opus4.8 / -sonnet5, curious-research. **Fresh / moving:** superbot-next #512, superbot-idle #151, idea-engine #494.
- **CI-confirmation method:** check-run conclusions ARE independently readable via github MCP `get_check_runs` (born-red confirmed that way); the legacy combined-status rollup is uninformative on check-runs-only repos — that is a rollup limitation, **not a proxy wall.**
- **Snapshot-rot note (record, no defect):** the roster Gen-N "backlog cleared" line was already stale ~90 min after generation — the live-recording practice (verify vs live GitHub each wake) IS the correction path; no fix needed.
- **Reviewer thread closed:** fleet health OK — 14 live seats, 0 red main HEADs, 5 frozen-by-design; Ideas Lab is a finished mine.

## 2026-07-18 · hub PR sweep (~16:3xZ) — records reconcile

*Source: fm hub-sweep-record seat, 2026-07-18. Every per-PR state re-verified live via github MCP `get_pull_request` / `get_check_runs` before writing (Q-0120 — never against report text). Oversight-only: recorded here, never pushed to sibling repos. Distinct from the earlier overnight-oversight sweep above (different open-PR set).*

- **Hub PR sweep 2026-07-18T~16:3xZ — 20 repos, 7 open PRs at the sweep instant: 0 hub-merged, 4 held born-red, 2 owner carve-outs, 1 CI-red.**
  - **4 held born-red** (structurally cannot hub-land — in-progress card holds substrate-gate/strict red): gba-homebrew [#177](https://github.com/menno420/gba-homebrew/pull/177) (bestiary cut-2, stacked on cut-1) · [#178](https://github.com/menno420/gba-homebrew/pull/178) (cut-3, stacked on cut-2) · idea-engine [#527](https://github.com/menno420/idea-engine/pull/527) (VERDICT 126, PHASE-1 HOLD) · trading-strategy [#151](https://github.com/menno420/trading-strategy/pull/151) (render_round_results). **Q-0120 correction:** trading #151 was born-red at the sweep instant but **auto-merged 2026-07-18T16:33:51Z** (github-actions[bot]) moments later — so it is NOT still held; **3 remain born-red** (gba #177/#178, idea-engine #527), 6 of the 7 still open now.
  - **2 owner carve-outs** (workflow-touching; `merge-on-green.yml` skips `.github/workflows/**` diffs → no auto-land, needs owner merge click or agent MCP/REST merge — not an agent wall): pokemon-mod-lab [#98](https://github.com/menno420/pokemon-mod-lab/pull/98) (touches `rom-builds.yml`; OPEN, clean) · product-forge [#29](https://github.com/menno420/product-forge/pull/29) (adds `android-ci.yml`, self-flagged OWNER-ACTION; OPEN, clean). → owner-queue `OQ-POKEMON-98-WORKFLOW-MERGE` / `OQ-FORGE-29-WORKFLOW-MERGE` (added this sweep).
  - **1 CI-red awaiting its own session** (flag only, not hub-fixable): superbot [#2148](https://github.com/menno420/superbot/pull/2148) (EAP de-wall evidence pack) — `code-quality` = **failure** on head SHA `fd2cf59` (check-run verified) despite card `complete`. The lane session owns the fix.
  - **Dark-seat watch (no-open-PR signal only — heartbeats NOT pulled, so NOT proof of dark):** codetool-lab-fable5, codetool-lab-opus4.8, codetool-lab-sonnet5, superbot-plugin-hello, superbot-idle, venture-lab, superbot-games, sim-lab, superbot-mineverse. (Several are frozen-by-design per the register; a genuine dark-seat verdict needs a heartbeat read, not just a null PR list.)

## 2026-07-18 · roster-freshness lapse + dropped-cron watch

*Source: fm roster-freshness custodian seat, 2026-07-18. Incident found + fixed live; recorded here per §How-to-re-verdict pt 4 (dated note, not a fork file).*

- **Incident.** At ~2026-07-18T03:28Z the roster (`docs/roster.md`) was found genuinely **4.0h stale** — `scripts/check_roster_freshness.py` RED (EXIT=1) against the 4h threshold.
- **Root cause: GitHub Actions silently dropped the ~00:40Z `roster-regen.yml` cron window** (cron `40 */2 * * *`). The **workflow itself is healthy** — all recent *scheduled* runs `success`, `workflow_dispatch` present; GitHub's own scheduler skipped the window under load (a documented GitHub behavior — scheduled crons are best-effort and can be dropped). **NOT clock skew:** container UTC ≈ real UTC, cross-checked against two external clocks.
- **Fix (clean).** Triggered `roster-regen.yml` via **`workflow_dispatch`** → **Generation #86 landed as PR #302** at ~03:29Z (main `f042f55`). Freshness now **OK — 0.0h, EXIT=0**.
- **Watch-item.** The 2h cadence has **no margin against a single dropped window before the 4h staleness bar**. If GitHub keeps dropping scheduled windows, migrate roster-freshness to the **CCR-routine fallback the workflow's own provenance header already documents** (a dedicated `cron 40 */2` routine). First drop observed 2026-07-18. → owner-queue `OQ-FM-ROSTER-CRON-RELIABILITY`.
- **Venue note.** No workflow code fixed by this seat — `.github/workflows/**` is owner/hub venue; the dispatch is a run-trigger, not a code change.

## 2026-07-18 · fleet-wide stale merge-doctrine sweep

*Source: fm fleet-doctrine-sweep seat, 2026-07-18. Read-only, verified vs each repo's origin/main. Oversight-only: recorded here, never pushed to sibling repos. Findings are framed as records of drift — "repo X's status doc still carries the pre-#308 doctrine" — not standing capability-denial claims.*

- **Purpose.** After the owner reversed the "agents can't merge" doctrine (fleet-manager #308/#309), find sibling repos whose living/binding docs still carry the pre-reversal wording.
- **Result: 10 of 14 already reconciled** (self-corrected 2026-07-18): superbot, superbot-next, superbot-games, superbot-mineverse, websites, venture-lab, idea-engine, sim-lab, trading-strategy, curious-research.
- **STALE — needs a doc reconcile (routed to hub, cross-repo lane-doc edits):**
  - **gba-homebrew** — `control/status.md` still carries the pre-#308 doctrine (~5 lines: :19 "Agent-side arming/merging stays WALLED…", the "agent landing path" section header, and :26/:27/:60 "owner ready-click → enabler lands"). Note: its OWN `docs/CAPABILITIES.md:89` was already corrected 2026-07-18, so the status doc now contradicts the repo's own ledger. Fix → agents merge/flip/arm directly; the enabler is one path, not the only one.
  - **pokemon-mod-lab** — `docs/CAPABILITIES.md:97-100` still carries the uncorrected "Self-merge classifier" seed (every sibling swapped this for the fleet-standard "self-merge is NOT a wall (corrected 2026-07-18)"), plus `docs/current-state.md:89/:324` and `control/status.md:26/:30/:46` still read "owner-merge-only" for `.github/workflows/**` diffs. Fix → swap the seed to the fleet-standard line; the workflow-diff carve-out is partly real (the `merge-on-green.yml` GITHUB_TOKEN can't merge workflow-file diffs) BUT an agent can merge those directly via MCP/REST, so it is not an owner blocker (websites documents this exact case correctly).
  - **superbot-idle** — `control/status.md:84` still carries a borderline past-tense residual ("left the merge decision to owner/coordinator per lane convention"); a one-line "(convention retired 2026-07-18)" pointer suffices. Its OA-003 (make `pytest` a required check) is a legitimate owner/settings item, unchanged.
- **HISTORICAL residual (optional):** substrate-kit `docs/CAPABILITIES.md` append-log newest entries (:105 2026-07-17, :106 2026-07-16) are dated records, but :105 phrases a now-false "standing fleet rule: a session lands a PR ONLY by opening it READY…"; since the log is newest-first with no 2026-07-18 correction above it, a reader hits the false rule first — recommend a one-line dated correction entry on top. Verdict stays historical, not stale.
- **Disposition.** The 3 stale reconciles + the kit pointer are cross-repo living-doc edits → routed to the hub chat (or the lane sessions) for application, same channel as the settings tier; fleet-manager's own docs are already reconciled (#313/#316).

## 2026-07-18 · Websites custody task (owner-relayed, snapshot refresh + record reconcile)

*Source: fm websites-custody seat, 2026-07-18. Owner-relayed custody task. All findings Q-0120-verified against live source (snapshot export + each repo's origin/main at HEAD), not against report text.*

- **Triggers snapshot REFRESHED.** `telemetry/triggers-snapshot.json` replaced with a fresh full `list_triggers` export captured **2026-07-18T14:22:08Z** — **2488 records**, all **9 trigger-health invariants green** (`check_trigger_health.py` VERDICT PASS; **I6 SNAPSHOT-FRESH now PASS**, 0.1h before now vs the 4h bar). The refresh **captures websites' live failsafe `trig_01FYyvu2EytWF5NSEzLU2qLD`** (cron `45 */2`), which **clears the websites control-plane `/prompts` "no failsafe trigger for this seat in the snapshot" drift row** (computed at `app/prompts.py:552` — the "awaiting upstream refresh" state the Websites banner pointed at). It also fixes the roster's "no attributed triggers" for websites (self-corrects on the next roster regen).
- **v3.7 stamp — NOT APPLIED as a verified fact (flagged, decide-and-flag).** No written "stamp Websites v3.7" request exists in the websites→manager channel (outbox / inbox / status / owner-notes checked at HEAD). Websites is live and post-reboot (its ORDER 031/032 acted on the reboot go; `status.md` maintained through 2026-07-18) but its own repo self-stamps only `kit: v1.17.0` — no independent v3.7 marker. Recorded here as **reboot-current BY INFERENCE (not repo-verified)** — do **not** assert a repo-verified v3.7 stamp on the strength of this note.
- **Roster HEAD lag — benign, no action.** The websites roster row (HEAD `9e5aa75` / #404) is ~1 slice behind live (`d8ad1d9` / #406 merged); `docs/roster.md` is GENERATED (do-not-hand-edit) and self-corrects on the next `40 */2` regen. Benign newest-merge lag.
- **SIM-REQUEST #355 (websites outbox — release-drift banner doctrine for botsite arcade pages)** — the one genuine outstanding websites→manager verdict ask. **Manager verdict: A** (bake release tags into `review/data`, keep botsite outbound-free) — matches the seat's own recommendation; simpler + no new outbound dependency. **Flagged decide-and-flag for owner veto.** Delivery of the verdict to the websites inbox is a separate cross-repo step (routed to the hub, same channel as the doctrine-reconcile tier above).

## How to re-verdict

1. Verify against live source (Q-0120 — never against report text).
2. Edit the row: new verdict + dated one-line evidence citation (SHA / PR).
3. Cross-check the owner-queue: a verdict whose "next action" is an owner
   click must have (or get) an `OQ-` item; cite the slug.
4. Wholesale re-reviews land as a new dated seed note here, not a fork file.

## 2026-07-18 · registry meta.md restamp (fleet-prompt-state panel)

*Source: fm meta-restamp seat, 2026-07-18. Docs-only. The websites control-plane
`/prompts` "fleet prompt state" panel parses each `projects/<seat>/meta.md`
"Deployed-state per part" table (`websites app/prompts.py`) and marks a
Custom-Instructions or coordinator-prompt row **stale** when its claim predates
canonical (v3.7 · 2026-07-15) or names a `v1`/`v2`/`gen-2`/`v1-era`/`pre-v3`
token. The best positive state a meta.md prose row can reach is `unverified` —
byte-`in sync` is only reachable from the failsafe trigger snapshot, never from
meta.md.*

- **Canonical:** v3.7 · 2026-07-15. **All 9 standing-seat `meta.md` restamped**
  to a parseable, current-dated (2026-07-18) v3.7 Deployed-state table with a
  `| Part | State |` shape — verified against the live parser that both the
  Custom-Instructions and coordinator-prompt rows now render `unverified` for
  every seat (panel **"8 stale" → cleared**). Each file's top HTML stamp bumped/
  inserted to `<!-- v3.7 · 2026-07-18 · fleet-manager projects registry -->`
  (`projects/README.md` §Doctrine 3); prior per-part detail preserved as a
  historical `<details>` block; no other prose changed.
- **Genuine owner / self-heal residue (named).** The **3 Class-A seats —
  fleet-manager, websites, curious-research — have an OLDER owner console paste
  deployed**; the panel row stays `unverified` (never asserted `in sync`) until
  the owner re-pastes the v3.7 registry copy. This is an **owner-only self-heal,
  per seat** — the registry copy is current, only the deployed paste lags. The
  **6 Class-B seats — venture-lab, superbot-world, superbot-2.0, ideas-lab,
  game-lab, self-improvement — were never console-pasted** (registry IS the
  deployed artifact; no paste owed).
- **Gap flagged (design, not a wall).** There is **NO machine-readable
  "self-heal / seats stamp their own deployed version" channel** — only the
  manager-written quote-on-demand version-stamp doctrine (`projects/README.md`
  §Doctrine 2–3, drift-detected by asking a seat to QUOTE its header). A
  byte-verifiable *deployed-stamp* channel for the CI/coordinator artifacts does
  not exist; only the failsafe trigger snapshot is byte-verifiable
  (`list_triggers` returns the stored prompt verbatim). Recommend flagging to the
  owner as a design gap — the panel's `unverified` verdict is the honest ceiling
  for the paste-bearing parts until such a channel exists; do not assert false
  sync.

## 2026-07-18 · fleet PR sweep (21:05–21:15Z) — coordinator wake records

*Source: fm sweep-records seat, 2026-07-18. Every per-PR state MCP-verified live (all 20 repos swept 21:05–21:15Z) before writing (Q-0120 — never against report text). Oversight-only: recorded here, never pushed to sibling repos. Distinct from the ~16:3xZ hub PR sweep above (open-PR set has moved).*

- **Fleet PR sweep 2026-07-18T~21:15Z — 20 repos, 13 open PRs across 7 repos: 2 green carve-outs awaiting hub, 1 NEW stuck red, 2 gba survivors, 8 in-flight born-reds, 0 stale, 0 strays.**
  - **2 green workflow carve-outs awaiting hub (unchanged):** pokemon-mod-lab [#98](https://github.com/menno420/pokemon-mod-lab/pull/98) · product-forge [#29](https://github.com/menno420/product-forge/pull/29) — both still OPEN + green; `merge-on-green.yml` skips `.github/workflows/**` diffs, so landing is a hub MCP/REST merge (or owner click). → owner-queue `OQ-POKEMON-98-WORKFLOW-MERGE` / `OQ-FORGE-29-WORKFLOW-MERGE` (rows still accurate). **Disposition: hub lands both (baton item 1).**
  - **NEW stuck red: websites [#422](https://github.com/menno420/websites/pull/422)** — automated bake PR; its dispatched `quality` run **29658485481 failed 19:49Z**, and the PR body says it waits for a human hand. **Disposition: websites lane seat to fix/rebake or close** — not hub-mergeable while red.
  - **gba-homebrew pile COLLAPSED (~13 → 2):** only [#177](https://github.com/menno420/gba-homebrew/pull/177) / [#178](https://github.com/menno420/gba-homebrew/pull/178) remain — both now **ready-flipped + auto-merge armed 11:26Z**, held only by the **by-design substrate-gate red** (main's #151 doc orphans). **Disposition: gba lane confirms + clears the gate**; lane work, no owner click. → owner-queue `OQ-GBA-DRAFT-PILE` re-scored RESOLVED this sweep (see queue).
  - **8 in-flight born-red session PRs (working as designed — no action, re-sweep next wake):** websites [#425](https://github.com/menno420/websites/pull/425) / [#428](https://github.com/menno420/websites/pull/428) · substrate-kit [#470](https://github.com/menno420/substrate-kit/pull/470) · idea-engine [#597](https://github.com/menno420/idea-engine/pull/597) · trading-strategy [#152](https://github.com/menno420/trading-strategy/pull/152) · superbot-next [#562](https://github.com/menno420/superbot-next/pull/562) / [#563](https://github.com/menno420/superbot-next/pull/563) · superbot [#2148](https://github.com/menno420/superbot/pull/2148) (still pending its lane fix).
  - **Staleness / strays:** no stale PRs (oldest open ~43h); zero strays beyond the 2 carve-outs above.
- **Trigger-health I8 WARN (sibling lane, attribution only):** two enabled "SuperBot World failsafe wake" crons — `trig_01XJJ88pQaQFRSpVAviCfAZe` (created 2026-07-17) · `trig_01DbcKVWxn6RJPhfyRkgTg6m` (created 2026-07-18T17:08Z). Sibling-seat ids, **left alone per attribution doctrine** (this seat makes no trigger calls against sibling lanes). **Disposition: SuperBot World seat's own BOOT-4 cutover miss — the fix belongs to that seat's next wake** (verify each live, keep one, delete the rest).

## 2026-07-19 · trigger-registry watch items (00:06:22Z capture) — records slice

*Source: fm records slice (PR #341), 2026-07-19. Facts read from the fresh
2026-07-19T00:06:22Z full `list_triggers` export (1962 records, 17 enabled) now
committed as `telemetry/triggers-snapshot.json`. Oversight-only: recorded here,
no trigger calls made against sibling lanes.*

- **2026-07-19 · SBW duplicate failsafe pair PERSISTS at the 00:06Z capture.** Both
  "SuperBot World failsafe wake" crons (`15 1-23/2 * * *`) are still enabled —
  `trig_01XJJ88pQaQFRSpVAviCfAZe` (created 2026-07-17T22:11Z) ·
  `trig_01DbcKVWxn6RJPhfyRkgTg6m` (created 2026-07-18T17:08Z) — and **both fired
  ~23:15Z** (last_fired 23:15:21Z / 23:15:19Z) **into different sessions**: two
  parallel SuperBot World seats are being woken every 2h. I8 WARN unchanged.
  **Disposition unchanged: SuperBot World seat's own BOOT-4 cutover fix** (verify
  each live, keep the oldest, delete the rest) — sibling ids, left alone per
  attribution doctrine. **Escalation tripwire: if the pair is still duplicated at
  the next snapshot capture, raise an owner-queue note** (two woken seats burning
  double wake budget is past the "route to the seat" threshold).
- **2026-07-19 · Venture Lab armed a weekly-grading business cron post-v3.8.**
  NEW `trig_01BDrZZM5dMS6NJLevGxdZR3` "Venture Lab weekly grading (business
  cron)" — `0 9 * * 5`, created 2026-07-18T21:02Z, never fired, next
  2026-07-24T09:07Z. Created ~35 min AFTER the v3.8 zero-routines ender doctrine
  landed on main (fm PR #330, owner-merged 20:27Z) — **read as pre-repaste
  drift, not defiance**: the seat's deployed prompt predates v3.8 (console
  re-paste ask already queued, owner asks item 1). **Disposition: Venture Lab
  seat folds the weekly grading into its work loop per v3.8 when its prompt
  re-paste lands**; sibling id, left alone — no trigger calls made.

## 2026-07-19 · ~06Z morning sweep (05:43–05:45Z, read-only, MCP-verified) — coordinator wake records

*Source: fm morning-sweep worker (PR #346), 2026-07-19. Every per-PR state and
websites fact MCP-verified live 05:43–05:45Z before writing (Q-0120). Oversight-
only: recorded here, never pushed to sibling repos. No trigger calls made.*

- **Fleet open-PR state (05:43Z): 7 open PRs across 5 repos — 1 NEW since the
  03:40Z pass, 0 new stuck reds, 0 green strays.**
  - **NEW:** idea-engine [#622](https://github.com/menno420/idea-engine/pull/622)
    (05:40:33Z, "VERDICT 169 mirror — PROPOSAL 156 APPROVE") — normal lane work,
    expected to self-land on green. No action.
  - **Hub queue confirmed:** product-forge [#29](https://github.com/menno420/product-forge/pull/29)
    still OPEN, `mergeable_state: clean` (workflow carve-out; `OQ-FORGE-29-WORKFLOW-MERGE`) ·
    fleet-manager [#344](https://github.com/menno420/fleet-manager/pull/344) still OPEN
    (odd-hour roster cron; workflow carve-out, `OQ-FM-ROSTER-CRON-SECOND-LINE` rides that PR).
  - **Unchanged known set:** superbot-next [#576](https://github.com/menno420/superbot-next/pull/576)
    (parked by design — classifier-wall doc PR, owner-attended completion) ·
    superbot-next [#571](https://github.com/menno420/superbot-next/pull/571) /
    [#567](https://github.com/menno420/superbot-next/pull/567) (lane docs work, open
    since ~22Z/21:54Z — watch for self-land) · websites
    [#434](https://github.com/menno420/websites/pull/434) (below).
- **websites deep-check (05:44Z, all read at HEAD `a5fdad4`):**
  - `control/status.md`: `updated: 2026-07-18T21:42:45Z`; `orders:` line reads
    `acked=001-035` — **ORDER 036 NOT acked.**
  - [#434](https://github.com/menno420/websites/pull/434) (BAKE_PAT wiring, the 036
    root-cause fix): still OPEN, **`mergeable_state: dirty` — conflict NOT
    resolved**, `do-not-automerge` label still on, last updated 21:28:19Z.
  - **No bake/data-refresh PR or commit on websites main since 21:52:34Z** — newest
    commit is `a5fdad4` (#425, botsite durable /submit). The 2026-07-18 fleet-data
    refresh remains un-relanded.
  - **Failsafe-cron read:** websites failsafe fires `45 */2 * * *`; the 23:45Z,
    01:45Z and 03:45Z windows produced **zero landed output** (no commits, no
    heartbeat bump, no ack). The 05:45Z window was imminent at sweep time
    (05:43Z) — re-checked pre-flip, see the disposition line for the result.
- **ESCALATION DISPOSITION — websites ORDER 036 (decided this sweep):** the lane
  showed **no activity of any kind since 21:52Z** (~8h silent; 036 unacked since it
  landed 21:19:36Z, ~8.5h). Verdict: **websites seat chain possibly stalled
  overnight — ORDER 036 unacked ~9h; disposition: flagged for the owner's morning
  (owner-queue note `OQ-WEBSITES-036-STALL`, info-only) + the lane's next failsafe
  wake.** Not hub-executable: #434 is `do-not-automerge` + owner-gated (ASK-0008
  BAKE_PAT secret half) and conflict-dirty — the rebase + ack + rebake are lane
  work; the secret half is owner work. No trigger calls made against the lane
  (attribution doctrine).
- **Local gate verdicts (05:44Z):** roster FRESH — gen #99, generated-at
  2026-07-19T04:04Z (landed via automated #345 at 04:05:12Z — the Actions lane DID
  fire overnight after the 00:40Z/02:40Z drops), 1.7h old, I5 PASS. Trigger health:
  **8/9 + I6 FAIL** — snapshot capture instant 00:06Z is 5.6h past the 4h bar; this
  sweep's venue makes no trigger-MCP calls, so the export refresh rides the
  coordinator's next wake (disposition, not a wall). I8 SBW duplicate-pair WARN
  unchanged (routed to that seat; tripwire re-arms at the next capture).
  `verify_routine_state.py` → OK, 2 claims verified (C1 failsafe + C3 deleted).

## 2026-07-19 · SBW duplicate-failsafe ESCALATION — tripwire FIRED (06:15:10Z capture) — records slice

*Source: fm records slice (PR #347), 2026-07-19. Facts read from the fresh
2026-07-19T06:15:10Z full `list_triggers` export (2024 records, 17 enabled) now
committed as `telemetry/triggers-snapshot.json`. Oversight-only: recorded here,
no trigger calls made from this venue.*

- **The 00:06Z watch item's escalation tripwire has FIRED.** The tripwire read:
  *"if the pair is still duplicated at the next snapshot capture, raise an
  owner-queue note."* At the second capture (06:15:10Z) both "SuperBot World
  failsafe wake" crons (`15 1-23/2 * * *`) are **STILL both enabled**:
  - `trig_01XJJ88pQaQFRSpVAviCfAZe` — created 2026-07-17T22:11:56Z, last_fired
    2026-07-19T05:15:26Z, next 07:15:00Z.
  - `trig_01DbcKVWxn6RJPhfyRkgTg6m` — created 2026-07-18T17:08:23Z, last_fired
    2026-07-19T05:15:23Z, next 07:15:00Z.
- **Two captures cited:** first at 2026-07-19T00:06:22Z (both fired ~23:15Z —
  last_fired 23:15:21Z / 23:15:19Z, watch item above); second at
  2026-07-19T06:15:10Z (both fired ~05:15Z, ~3s apart, next both 07:15Z). Six
  more hours = three more double-wake windows with no seat-side dedup — past the
  "route to the seat" threshold, exactly as the tripwire defined.
- **Escalation executed: owner-queue item `OQ-SBW-DUP-FAILSAFE` raised (Active,
  VENUE: hub)** — delete one of the pair from the hub chat's trigger tools.
  **Recommendation: delete `trig_01XJJ88pQaQFRSpVAviCfAZe` (the older,
  07-17-created one)** — the 07-18T17:08Z cron is the *current* SBW seat's own
  cutover-armed failsafe, so it is the one whose session binding is live. Note
  honestly: `check_trigger_health.py`'s generic I8 remedy says "keep the
  OLDEST"; that heuristic is seat-blind — here provenance decides (the newer id
  belongs to the seat that is actually running), so the seat-aware
  recommendation inverts it. Either deletion is ✅ reversible (re-create from
  the SBW startup prompt).
- **Attribution doctrine intact:** fm doctrine forbids this seat deleting a
  sibling lane's trigger id — hence the hub-chat routing rather than a direct
  `delete_trigger` from this venue. I8 stays WARN (not FAIL) until the dedup
  lands; VERIFY = the next fm snapshot shows exactly one enabled SBW failsafe.

## 2026-07-19 · owner "nothing-stuck" directive — morning executions (~07:40–08:10Z) — records slice

*Source: fm records slice (PR #351), 2026-07-19T08:38Z. Facts from this
morning's hub workers, merge states re-verified live via the GitHub MCP at
record time (Q-0120). RAW DATA; no trigger-MCP calls from this venue.*

- **Owner live directive, ~2026-07-19T08:00Z (verbatim, provenance record):**
  > "There are 'do not automerge' labels in some repos and I want then gone,
  > nothing should ever be stuck, I'm not going to look through PRs to merge
  > them."
- **product-forge #29 MERGED** — squash-merged directly via MCP
  2026-07-19T07:41:57Z, merge sha `20be7493a7c4d96b3b61e1f2f023ed77ad015e27`;
  `android-ci.yml` verified present on product-forge main. Owner-queue row
  `OQ-FORGE-29-WORKFLOW-MERGE` → **Resolved** (hub queue's last workflow
  carve-out cleared).
- **websites #434 MERGED** — `do-not-automerge` label stripped, then
  squash-merged (merged_at 2026-07-19T07:50:01Z, merge sha
  `403a91def5c315ea75623b574df60fa42cbf8cda`). BAKE_PAT wiring is live in
  `review-bake.yml` with the `|| GITHUB_TOKEN` fallback — degraded-not-broken
  behavior until/unless the BAKE_PAT secret exists (the fallback reproduces
  today's exact behavior). The 2026-07-18 data refresh itself is still
  un-relanded — lane work.
- **Fleet do-not-automerge label sweep (directive execution, facts):**
  - Label **defined in 9 repos**: websites, substrate-kit, fleet-manager,
    superbot, gba-homebrew, idea-engine, venture-lab, superbot-games,
    superbot-next.
  - **Only ONE open item carried it** — websites #434 (stripped + merged,
    above). Nothing else in the fleet is label-stuck as of the sweep.
  - **Label definitions NOT deletable from this venue**: the GitHub MCP
    toolset has no delete-label tool; the REST path returned 401/403
    (verbatim errors recorded by the sweep worker). Per doctrine this is a
    venue/path state, not a wall — the deletions route to the hub queue
    (`OQ-LABEL-DEFS-DELETE`).
  - **websites machinery caveat:** `host-automerge-extras.yml` (from websites
    PR #324) AUTO-RE-CREATES and auto-applies the `do-not-automerge` label on
    workflow-touching `claude/*` PRs — so in websites, deleting the label
    definition alone cannot satisfy the directive; the workflow behavior
    itself needs changing (carve-out removal, below).
- **Carve-out-removal worker dispatch BLOCKED (transient venue denial, NOT a
  wall):** the platform auto-mode classifier's guardrail-removal provenance
  check stopped the dispatch and asked for explicit owner confirmation
  wording; awaiting that confirmation. Recorded per doctrine as an
  attempt-once venue denial — do not generalize.
- **fm #344 (odd-hour roster cron):** still OPEN, `mergeable_state: dirty`,
  head `c2ca6b6` (re-verified live 08:39Z); **owner armed native auto-merge**
  on it; the conflict-fix worker was stopped by the owner pre-push; relaunch
  awaits the owner's "go". Note (drift, recorded): #344's body says it queued
  `OQ-FM-ROSTER-CRON-SECOND-LINE` in `docs/owner-queue.md`, but that edit
  rides the unmerged PR itself — on main the live row is
  `OQ-FM-ROSTER-CRON-RELIABILITY` (annotated this slice).
- **fm #350 (`check_lane_liveness.py`) merged earlier this morning** — slice 1
  of the next-slices queue done; next executable = **regen-window skip
  detector** (`docs/planning/2026-07-19-next-slices.md`).

## 2026-07-19 · 14Z cycle fleet re-sweep (14:12–14:16Z, read-only, MCP-verified) — records slice

*Source: fm records slice (PR #364). Open-PR states verified live via the GitHub
MCP at 14:12–14:15Z (Q-0120). RAW DATA; no trigger-MCP calls from this venue.*

- **Fleet-wide open-PR census (search `is:pr is:open user:menno420`, complete):
  5 open PRs total.** fm #364 (this slice) · sim-lab #258 (born-red VERDICT 184,
  created 14:12Z — ACTIVE session, leave alone) · superbot-next #567 / #571 /
  #576. Nothing else open anywhere — no new strays since the 05:45Z sweep.
- **superbot-next #567 + #571 — open, ZERO check runs on their heads**
  (`ba83969`, `99015dc`; `get_check_runs` → `total_count: 0` on both,
  `mergeable_state: unknown`). Both MCP-app-created (session ended ~22:49Z
  07-18) — the known app-token symptom: workflows never fired, so they are NOT
  green and NOT direct-merge candidates under the green-only carve-out. Route:
  a superbot-next seat (or hub worker) re-push/empty-commit to kick CI, then
  normal green landing. Docs-only diffs, no workflow files — not the
  workflow-diff carve-out class.
- **superbot-next #576 — unchanged**: parked classifier-wall, owner-attended
  completion path stated in its body. Listed, not touched.
- **gba #177/#178 RESOLVED-CLOSED** (the 05:45Z "held by by-design gate red"
  watch): both CLOSED unmerged 2026-07-18T23:21Z as subsumed-by-#179 (cut2/cut3
  content already on main via the #179 stack squash; claims swept via #204).
  gba also landed #205 (EAP close-out doc, 07:38Z) and #206 (dist ROM refresh
  to post-#201 build, 07:55Z). gba lane fully quiet — zero open PRs.
- **websites post-revival throughput: STRONG.** Since 05:45Z, 8 PRs merged —
  #436 (07:26Z heartbeat), #434 (07:50Z BAKE_PAT wiring, owner-armed), #438
  (07:53Z bake proof — PAT identity, real quality check, auto-merge fired:
  BAKE_PAT landing path PROVEN end-to-end), #439 (08:01Z ASK-0008 finalize),
  #440 (08:17Z), #441 (09:22Z /submit live-badge), #442 (11:35Z ORDER 037
  botsite Discord OAuth), #443 (12:15Z ORDER 038 dashboard Discord OAuth);
  #422/#437 stale bakes closed. Zero open. "One Discord login for everything"
  is now code-complete across all three services; the owner unlock is the
  redirect-URI + env-var pastes.
- **fm #344 MERGED** — by the owner (merged_at 2026-07-19T09:22:03Z) after his
  conflict fix; the odd-hour roster cron is live (regens #361 gen#104 13:41Z /
  #363 gen#105 14:06Z observed post-merge). `OQ-FM-ROSTER-CRON-RELIABILITY`
  already marked Resolved in `docs/owner-queue.md` — no drift found.
- **Roster verdict changes (gen #104 → #105, on main):** venture-lab FRESH →
  STALE (~4h31m); superbot-games Seat A dropped its `⚠ commits-FRESH`
  annotation (now plain DARK — pushes quieted); substrate-kit phase advanced
  R11 → R14 SHIPPED. Aging only — no new STALLED verdicts.
- **SBW duplicate failsafe pair PERSISTS in the 14:05:27Z capture** — both
  `trig_01XJJ88pQaQFRSpVAviCfAZe` (07-17T22:11Z) and
  `trig_01DbcKVWxn6RJPhfyRkgTg6m` (07-18T17:08Z) still enabled; I8 WARN
  unchanged. **Second escalation cycle** — `OQ-SBW-DUP-FAILSAFE` (VENUE: hub)
  stands; the hub delete has still not been executed.
- **Workflow-diff strays waiting on the owner's carve-out answer:** none open
  this sweep (the #344 case resolved by owner hand; websites #434 landed by
  owner arm). The pending owner answer (carve-out yes/no) still gates FUTURE
  workflow-diff strays — question stands in the baton.

## 2026-07-19 · R30 landed — workflow-PR merges are agent work (records slice, ~15:3xZ)

*Source: fm records slice (PR #368), written 2026-07-19T15:29Z. RAW DATA; no
trigger-MCP calls from this venue.*

- **Playbook R30 is LIVE on main** — landed by a **sibling session** as fm
  **PR #367**, merged **2026-07-19T14:41:37Z** (merge commit `234303e`,
  head-ref `claude/agent-merge-policy`): `docs/playbook.md` R30 +
  `docs/workflow-pr-merge-policy.md` (binding; owner-live provenance quoted
  therein — "remove my review from it completely … agents should just merge
  it"). Effect: workflow-touching PRs (`.github/workflows/**`) in tended repos
  are **agent-merged** once the merge-side agent verifies, at the exact head
  SHA: (1) Codex reviewed THAT commit, not `CHANGES_REQUESTED`, zero P1/P2
  (inline + summary); (2) every check + commit status green; (3) whole-file
  secret+egress scan clean (patch-less/oversized diff = STOP → owner queue).
  The first attempt (CI `codex-cleared` label gate, fm PR #362) was **closed**
  after Codex's own review found ~7 bypasses — the label path is dead, the
  merge-side re-check is the rule. The owner-queue "carve-out confirmation
  awaited" thread is **ANSWERED** by this (queue annotated this slice).
- **Parallel-writer coordination note (no collision):** the sibling session
  was active on this repo **12:01–14:41Z** (its #362 attempt → close → #367
  land) while this seat's own slices landed alongside (#364 records 14:17Z ·
  #365 build ~14:45Z). Zero merge conflicts, zero duplicated work — separate
  branches + one-file-per-claim + distinct scopes held, exactly the layout the
  claims README's 0%-conflict measurement predicts.
- **Two classifier denials on manager-relayed guardrail-removal dispatches
  (dated, factual — transient venue state per doctrine, not a wall):** twice
  on **2026-07-19**, a manager-relayed worker dispatch to remove the websites
  `host-automerge-extras.yml` carve-out machinery (the label auto-re-create /
  auto-apply behavior) was stopped by the **platform auto-mode classifier's
  guardrail-removal provenance check** — denial class both times: explicit
  owner-confirmation wording requested for removing a guardrail (first: the
  morning dispatch, recorded in the ~08:0xZ records slice, PR #351; second: a
  later relay the same day, recorded at this slice). Per doctrine this is an
  attempt-once, venue-specific classifier state — the cleanup rides the
  owner's live venue (see `OQ-LABEL-DEFS-DELETE` caveat), and once its PR
  exists it lands under R30.

## 2026-07-19 · 18Z cycle — snapshot refresh + SBW THIRD escalation cycle + queue re-scope (records slice)

*Source: fm records slice (fm PR #374), written 2026-07-19T18:0xZ. Snapshot facts
from the verified full 2026-07-19T17:57:56Z export; lane facts from
`check_lane_liveness.py` run at 18:05Z. RAW DATA; no trigger-MCP calls from this
venue.*

- **`telemetry/triggers-snapshot.json` refreshed** from the full
  2026-07-19T17:57:56Z export: **2159 records, 16 enabled** (22 pages,
  0 cursor-overlap dups, +30 new / -0 gone vs the 14:05:27Z capture).
  `check_trigger_health.py` → **PASS 8/9, 1 WARN (I8), exit 0**; I6
  SNAPSHOT-FRESH PASS (0.1h). `verify_routine_state.py --export` →
  **VERDICT OK, fence-sourced, 3 claims verified** (C1 failsafe + C3 deleted +
  V1 volatile fields current post-bump). FM failsafe nominal in the export:
  `trig_01GK4mjoKBP3yCabn9ux1MB2` enabled, last_fired 2026-07-19T16:32:24Z,
  next 2026-07-19T18:31:48Z; one FM pacemaker one-shot pending (~18:28Z) —
  chain alive.
- **SBW duplicate failsafe pair PERSISTS — THIRD escalation cycle.** Both
  "SuperBot World failsafe wake" crons still enabled at 17:57:56Z
  (`trig_01XJJ88pQaQFRSpVAviCfAZe` 07-17T22:11Z ·
  `trig_01DbcKVWxn6RJPhfyRkgTg6m` 07-18T17:08Z); observed double-fires today
  **09:15Z / 13:15Z / 15:15Z / 17:15Z**, next double-fire **19:15Z**. The hub
  delete (`OQ-SBW-DUP-FAILSAFE`, VENUE: hub) has now survived THREE capture
  cycles unexecuted. Aggravating signal: `check_lane_liveness.py` (18:05Z)
  verdicts all three SBW-seat constituent lanes **STALLED** (superbot-games
  Seat A ~9h15m · superbot-idle ~10h39m · superbot-mineverse ~10h39m, all past
  4+ failsafe windows) — the pair is double-waking a seat whose lanes are
  landing nothing.
- **`OQ-LABEL-DEFS-DELETE` → RESOLVED (verified).** `check_label_hygiene.py`
  ground-truth run 1 (2026-07-19T16:15Z, fm PR #370): `HEADLINE: 0 hold-class
  definition(s) · 0 application(s) to OPEN items · 0 repo(s) not measured
  (of 19)` — the 9 queued `do-not-automerge` definitions were deleted between
  the 08:38Z queue write and 16:15Z; the checker run is the item's own VERIFY
  step. Residual re-scoped to new Active item **`OQ-WEBSITES-LABEL-MACHINERY`**
  (owner venue: the relayed `host-automerge-extras.yml` removal dispatch was
  classifier-gated twice on 2026-07-19; once its PR is open it lands under R30).
- **R30 pre-merge checker SHIPPED** — `scripts/r30_merge_check.py` (build
  slice, fm PR #372, merged 17:0xZ): the workflow-PR 3-point verification
  (head-SHA-bound Codex evidence · checks+statuses green · secret+egress scan)
  mechanized with PASS/REVIEW/STOP exits; ground-truthed on fm #344 (REVIEW)
  and fm #362 (STOP).

## 2026-07-19 · 22Z night cycle — snapshot refresh + SBW FOURTH escalation cycle (records slice)

*Source: fm records slice (fm PR #381), written 2026-07-19T21:4xZ. Snapshot facts
from the verified full 2026-07-19T21:34:18Z export (2199 records, 17 enabled,
22 pages); lane facts from `check_lane_liveness.py` run at 21:40Z against that
snapshot. RAW DATA; no trigger-MCP calls from this venue.*

- **`telemetry/triggers-snapshot.json` refreshed** from the full
  2026-07-19T21:34:18Z export: **2199 records, 17 enabled** (22 pages,
  0 cursor-overlap dups, +40 new / -0 gone vs the 17:57:56Z capture).
  `check_trigger_health.py` → **PASS 8/9, 1 WARN (I8), exit 0**; I6
  SNAPSHOT-FRESH PASS (0.1h). `verify_routine_state.py --export` →
  **VERDICT OK, fence-sourced, 3 claims verified** (C1 failsafe + C3 deleted +
  V1 volatile fields current post-bump). FM failsafe nominal in the export:
  `trig_01GK4mjoKBP3yCabn9ux1MB2` enabled, last_fired 2026-07-19T20:32:21Z,
  next 2026-07-19T22:31:48Z; one FM pacemaker one-shot pending (22:05Z,
  "continue the work loop") — chain alive.
- **SBW duplicate failsafe pair PERSISTS — FOURTH escalation cycle.** Both
  "SuperBot World failsafe wake" crons still enabled at 21:34:18Z
  (`trig_01XJJ88pQaQFRSpVAviCfAZe` 07-17T22:11Z ·
  `trig_01DbcKVWxn6RJPhfyRkgTg6m` 07-18T17:08Z); the 18Z entry's predicted
  **19:15Z double-fire happened, and so did 21:15Z** — in-snapshot last_fired
  21:15:27Z / 21:15:30Z (~2.4s apart), both next **23:15Z**. The hub delete
  (`OQ-SBW-DUP-FAILSAFE`, VENUE: hub) has now survived FOUR capture cycles
  unexecuted. Note the remedy flip (PR #380-era I8 text): keep-oldest is NOT
  the rule — the seat's live heartbeat decides; the newest-created
  (`trig_01DbcKVWxn6RJPhfyRkgTg6m`) is the likely keeper.
- **Lane-liveness deltas vs the 20:36Z run (PR #379 detector's first full
  read):** headline now `STALLED: superbot-idle (Seat B) · WAKING-IDLE:
  superbot-idle (Seat B) · asleep: none · DARK: none · not measured: 0`.
  **Recovered:** substrate-kit (was WAKING-IDLE 2-fires/QUIET → LIVE, commit
  21:28Z) · superbot-games Seat A (was STALLED/5-fires → LIVE, commit 20:54Z) ·
  superbot-mineverse (was STALLED/5-fires → LIVE, commit 20:36Z). **Worsened:**
  superbot-idle (Seat B) is the sole STALLED lane, now **WAKING-IDLE (7 fires
  since last output)**, last landed signal 07:26Z (~14h14m) — the duplicate
  pair's double token burn concentrates entirely on a lane landing nothing.
