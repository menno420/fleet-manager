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
| **superbot-plugin-hello** | seed — spans SuperBot 2.0 (contract) ↔ SuperBot World (consumers) | 🟢 seeded | **KEEP-QUIET** *(re-verdict 2026-07-14, INC-01: seeded `bbaccec` 2026-07-12T13:29Z, live-re-verified non-empty; pinned by superbot-next `plugins.lock.json` — never archive)* | Contract exemplar, dormant-by-design; idle PLUG-001 unblocked (adapter #75/#78) | none — passive-by-design (no heartbeat) |
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

## How to re-verdict

1. Verify against live source (Q-0120 — never against report text).
2. Edit the row: new verdict + dated one-line evidence citation (SHA / PR).
3. Cross-check the owner-queue: a verdict whose "next action" is an owner
   click must have (or get) an `OQ-` item; cite the slug.
4. Wholesale re-reviews land as a new dated seed note here, not a fork file.
