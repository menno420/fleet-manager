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
| **sim-lab** (evidence/lie-detector) | Ideas Lab (verify half of the generate→verify loop) | 🟢 | KEEP | 10 verdicts, self-checks caught a real bug; idle-by-design not stuck | ~~Owner: enable Codex (OA-002)~~ *(post-seed: resolved — Codex envs exist for all 12 active repos, ORDER 014)* |
| **idea-engine** (ideation) | Ideas Lab (generate half) | 🟢 | KEEP | 193 PRs, reports verify true; surfaced a real superbot false-green | Split the 25KB status.md; lift the ≤07-13 owner decision out of the bloat |
| **fleet-manager** (coordination substrate) | Fleet Manager (manager) | 🟢 | KEEP | The de-facto SSOT; roster/queue/inbox real | *(post-seed: the seed's "ledgers drift + stubs unfilled" 🟡 is CLOSED by P1–P3, fm #81–#86)* Keep the custodian loop green |
| **superbot-plugin-hello** | seed — spans SuperBot 2.0 (contract) ↔ SuperBot World (consumers) | ⚪ empty | **SEED** | Empty repo gating two finished engines (idle + games) | 🟢 One word: "push the plugin seed" (`OQ-PLUGIN-SEED-WORD`) |
| **codetool-lab-fable5** (envdrift) | none — seat retired to stub (slice 1) | ⚫ parked | **ARCHIVE** | Finished CLI, wound-down, no mission | Archive after gen-3 succession settles; pending tag/Release clicks |
| **codetool-lab-opus4.8** (mdverify) | none — seat retired to stub (slice 1) | ⚫ parked | **ARCHIVE** | Finished CLI, releases live, wound-down, no mission | Archive after gen-3 succession settles |
| **codetool-lab-sonnet5** (cfgdiff) | none — seat retired to stub (slice 1) | ⚫ parked | **ARCHIVE** | Finished CLI, wound-down, no mission | Archive after gen-3 succession settles; pending v0.1.1 tag |

**19 repos · 15 active (all KEEP-family) · 3 ARCHIVE · 1 SEED · 0 DELETE**
(seed tally, unchanged at port time).

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

## How to re-verdict

1. Verify against live source (Q-0120 — never against report text).
2. Edit the row: new verdict + dated one-line evidence citation (SHA / PR).
3. Cross-check the owner-queue: a verdict whose "next action" is an owner
   click must have (or get) an `OQ-` item; cite the slug.
4. Wholesale re-reviews land as a new dated seed note here, not a fork file.
