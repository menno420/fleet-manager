# Prompt-currency audit — is v3.3 finished, and is it still current?

> **Status:** `reference`
>
> Owner-directed phase A, 2026-07-12. Three-worker research fan-out (kit deep
> dive · per-seat activity + drift review verified ~15:30–15:40Z · v3.3
> finishedness sweep), synthesized by the shipping worker on PR #118. All
> fleet-manager file citations are at origin/main `5e404fd` unless noted;
> substrate-kit citations at origin/main `5363e41`. Snapshot of its census
> moment — verify claims against the repos before acting (playbook R2).

## 1. Verdict up front

**v3.3 is structurally finished but no longer fully current.** Finished: all
three v3.2 defect-queue items (#7 fresh-session-per-fire, #8 `kit:` line
grammar, #9 stale MCP PR reads) are genuinely closed in the shipped text
(per-project/README.md v3.3 changelog item 4; planned-routes.md §B rows
35/37), the BOOT TRIAD / thorough-boot markers are checker-verified across
all 8 seats (PR #111 QA output), and the registry sync is 24/24
(`--check-registry` OK). Not current: the same day it landed (~11:00Z),
substrate-kit released v1.13.0 + v1.14.0 and the seats kept moving — by
~15:40Z four seats' landing-path lines were contradicted by merged enablers
(websites #167, sim-lab #50, trading #74, mineverse #42), three kit-doctrine
lines went stale (WALLS never-re-probe, six-field ask, BOOT-4
verify-exists), four new kit surfaces are unrouted, and post-landing
evidence exposed two P0 defects in the park-green dictionary entry itself
(the PR #113 "cross-session permission laundering" denial). Net: **16 v3.4
deltas (2 P0 · 11 P1 · 3 P2)** — a v3.4 restamp is warranted, and the speed
of decay argues for generating landing-path lines from live state rather
than hand-restamping them (see flags).

## 2. Kit-impact verdict (substrate-kit v1.13.0 / v1.14.0 / unreleased main)

**One line:** nothing shipped today renames a gate or breaks a v3.3 route,
but three v3.3 lines are now stale against kit truth and the prompts route
to none of today's new planted surfaces.

Impacts (each also a delta in §4):

- **WALLS "never re-probe" vs the v1.14.0 staleness rule.** v3.3 (all 8 CIs,
  e.g. `self-improvement-custom-instructions.md:23`): "**WALLS** (quote,
  never re-probe)". Kit slice 5 (kit PR #274, released in v1.14.0 and
  distributed to adopters today) plants DISCOVERY step 5: an entry older
  than 14 days your work depends on "is a claim, not a fact — re-verify with
  one cheap attempt." → delta 8.
- **Six-field ask lacks the new `RISK:` line.** v3.3 carries "six-field ask =
  WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFY" (CIs e.g.
  `self-improvement-custom-instructions.md:23`; startups e.g.
  `self-improvement-startup.md:110`). Kit PR #272 (v1.14.0) adds the
  expected `RISK: ✅|↩️|⚠` line (grammar.py `RISK_CLASS_LABEL`; advisory
  finding `owner-action-risk-class`; kit re-stamped all 13 of its own
  OWNER-ACTION blocks in #273). The structured-choice "**bolded
  recommendation** / one-letter answer" rule is also absent from v3.3 (grep:
  zero hits). → delta 9.
- **BOOT-4 verifies existence, not delivery.** v3.3
  (`self-improvement-startup.md:35`, doctrine-identical across the 8):
  business cron is "KEPT AS-IS … Verify it exists, record it in the
  heartbeat, leave it." Kit forensics (report PR #262, 09:02Z) + the new
  `routines.md.tmpl` (kit PR #287, merged but **unreleased**) hold
  fresh-session cron delivery at **0-for-2** → "treat as UNVERIFIED-BROKEN
  until a scheduled fire is proven", plus the wedge signature
  (`enabled ∧ next_run_at < now−15min`), the manual-fire trap
  (`fire_trigger` sets `last_fired_at` without advancing `next_run_at`), and
  the failsafe blind-window check. None ride v3.3 (grep: zero hits for
  UNVERIFIED/wedge/last_fired/next_run). → delta 10.
- **Four new planted surfaces are unrouted.** Grep across all 22 v3.3 files:
  zero references to `docs/SKILLS.md` (planted + boot-wired at every adopter
  via kit PR #264, v1.13.0), `/intake` (kit PR #270, v1.14.0),
  `docs/ROUTINES.md` (kit PR #287, unreleased — route when released), or the
  seat-digest fences (kit PR #279, unreleased —
  `substrate-kit:skills-digest`/`walls-digest`, 1,500-char budget, built for
  fleet-manager's seat-prompt regen; the kit changelog itself names the
  fleet-manager regen wiring as "a separate coordinated PR";
  `docs/prompts/v3/tools/regen_b_files.py` has zero digest/SKILLS logic).
  → deltas 11–12.

Explicit no-impact checks (kit side):

- **Gate names / check semantics** — zero commits today under
  `.github/workflows/`; `kit-quality` / `substrate-gate` names unchanged
  (v3.3 `self-improvement-custom-instructions.md:14,:37` still correct); all
  new checkers (`check_skill_grounds`, `check_seat_digest`, extended
  `check_capability_xref` / `check_owner_actions`) are advisory-only.
- **ORDER 015 / `agreement_home` fix (v1.13.0, kit #261)** — v3.3
  orientation is already CONSTITUTION-first; no v3.3 line points at a dead
  `.claude/CLAUDE.md`.
- **Heartbeat-grammar graduation (kit #289)** — v3.3 already carries the
  plain-form rule, bold-negative, and adopters.md deference
  (`self-improvement-startup.md:109`; CI `:37,:44`). Kit caught up to the
  prompts; consistent.
- **Preflight fetch + hard-reset (kit #287 tail)** — v3.3 HARD-SYNC with
  dirty-tree rescue branch already present
  (`self-improvement-custom-instructions.md:11`).
- **Model-line widening (kit #286)** — v3.3 "family-level names only, never
  exact IDs" (`self-improvement-custom-instructions.md:35`) already
  satisfies the widened ban.
- **Evidence block (kit #287)** — every element (probe-not-record,
  tree-over-heartbeat, false-green = checker's bug, ~25-min stale reads)
  already rides v3.3 (Q-0120 entry, TOOL FACTS, TRUTH bar).
- **Self-propagation doctrine (kit #282, unreleased)** — repo-side
  CONSTITUTION text; no v3.3 contradiction (feeds the routing delta only).
- **Venue-scoped capability grammar backward-compat (kit #274)** — old
  5-field appends read as venue `any`, never flagged; v3.3's venue-less
  DISCOVERY wording is incomplete-not-wrong (venue posture carried by BOOT
  TRIAD).
- **ORDER 014 / fm PR #107's 3 queued gaps** (fresh-session-per-fire ·
  `kit:` grammar · stale MCP reads) — all genuinely closed by v3.3; the
  report's five deferred template-graduation rows all shipped kit-side today
  (#287, #289, and the `session-close` landing-path playbook in #265).

## 3. Per-seat one-liners (verified at origin HEADs ~15:30–15:40Z)

1. **fleet-manager — FRESH · prompt matches: YES.** Heartbeat 11:37:32Z
   (#113), HEAD `5e404fd` (#117 roster gen-15, 14:26Z); #116 parked green,
   #118/#119 born-red research; "NO auto-merge enabler here" verified true
   (workflows = roster-freshness/roster-regen/substrate-gate).
2. **SuperBot 2.0 — FRESH · prompt matches: YES.** superbot: 10 merges
   through #2040 (`d5e815c2`, 15:21Z), recon #2042 in flight; hub heartbeat
   07-11 is by-design (Q-0264 fallback). superbot-next: heartbeat 15:05Z,
   parity 50/50, 9-PR wave open (#263–#275), ORDER 016 filed 15:13Z. Enabler
   facts both verified ✓.
3. **websites — FRESH · prompt matches: NO (landing path, both layers).**
   Enabler PR #167 merged 14:56:09Z by menno420 and demonstrably works (#180
   arm-on-open success 15:35:14Z); heartbeat 15:17:20Z current; v3.3
   `websites-startup.md:20` + `websites-custom-instructions.md:15` still say
   "NO auto-merge enabler installed / park green" — contradicting the
   startup's own generic enabler doctrine at :63–64.
4. **Self Improvement (substrate-kit) — FRESH · prompt matches: YES.**
   v1.14.0 released + distributed (trading #74 13:46Z, games #63, gba #71,
   pml #55); HEAD `5363e41` 15:24:45Z; heartbeat 15:35:00Z; only the two
   owner-ratification pins #220/#238 open (`do-not-automerge`, aging,
   correctly routed via status ⚑).
5. **SuperBot World — STALE (3/3 heartbeats contradicted) · startup YES
   (stateless) / CI dictionary premise stale.** mineverse #42 (CSRF) merged
   13:54:21Z by menno420 — but its own on-main heartbeat still says
   "awaiting green + owner merge"; idle heartbeat "dormant" contradicted by
   open #72/#74 (green ~5h); games ORDER 005 truth-stamp still unexecuted.
   `superbot-world-custom-instructions.md:40` SECURITY-BEFORE-SECRETS
   premise is now historical → delta 7.
6. **Game Lab — STALE (by worst constituent, pml) · prompt matches: YES.**
   gba fresh (heartbeat 13:00:22Z; #68/#69 parked green awaiting owner
   clicks); pml heartbeat 07-11 21:03Z contradicted by ORDER 006 (#53) + kit
   #55 (`df9d8b5`), ack owed. "NO enabler in EITHER repo" verified true.
7. **Ideas Lab — FRESH · prompt matches: NO (sim-lab merge line).**
   idea-engine heartbeat 14:23:57Z, 0 open PRs; sim-lab cycling
   PROPOSAL→VERDICT same-day, fully self-landing — `ideas-lab-startup.md`
   MERGE MECHANICS "sim-lab: NO enabler … ORDER 003 is its install order" is
   contradicted (enabler landed sim-lab #50 `e11ed40` 10:28Z; #50–#52
   self-landed). The idea-engine "enabler RACES" half still matches.
8. **Venture Lab — FRESH · venture half YES / trading half NO.** venture-lab
   ACTIVE money seat, heartbeat 14:01Z "owner mid-Launch-Hour", wave through
   #77 (`77074ce` 15:25:50Z, benign lag); trading ARCHIVE-READY with enabler
   self-landing proven (#74 merged_by github-actions[bot] 13:46:23Z) —
   `venture-lab-startup.md:19`'s "Allow auto-merge OFF … MCP squash-on-green
   = the SOLE exception" is contradicted by five enabler self-landings
   today. The "LIVE-BUT-DARK" suspect is CLEAR — no such text exists in v3.3.

Roll-up: 6 FRESH / 2 STALE (superbot-world, game-lab); no DARK, no DEAD.

## 4. v3.4 DELTA LIST (merged + deduped across all three reports)

Overlaps noted once: the sim-lab merge-on-green staleness was found
independently by the finishedness and per-seat reviews (delta 5); the
venture-lab trading-enabler staleness likewise (delta 6); websites #167 and
superbot-world CSRF come from the per-seat review (deltas 4, 7); deltas 8–12
come from the kit deep dive.

> ⚠ **Byte-budget caveat on delta 1:** the CI size gate is 8,000
> chars+bytes and two seats are at the wire — superbot at **7,996 bytes**
> and websites at **7,997**. The proposed +~64-char qualifier breaks the
> gate on both without a compensating trim in the same entry (e.g. "a
> GITHUB_TOKEN workflow" → "GITHUB_TOKEN workflow").

| # | Pri | Artifact / path | Current line (verbatim) | Proposed line | Citation |
|---|---|---|---|---|---|
| 1 | **P0** | all 8 `docs/prompts/v3/per-project/<seat>-custom-instructions.md`, Dictionary "park green" entry (fm line 26) | "…NEVER arm/merge your OWN PR; a DIFFERENT session may review-merge; owner-held/…" | "…NEVER arm/merge your OWN PR; a DIFFERENT session may review-merge on its OWN genuine review only — relayed/dispatched authority = laundering, denied; owner-held/…" (+ compensating trim, see caveat above) | `fleet-manager-startup.md:74,:112`; `platform-capabilities.md:100-102,:130-135`; PR #113 denial (today; n=2 with fm PR #68 / #88/#89) |
| 2 | **P0** | `fleet-manager-custom-instructions.md:14` (Landing path) | "Merge: NO enabler — park green; landing rides a non-author review-merge or a fresh dispatch." | "Merge: NO enabler — park green; landing rides a fresh owner-provenance dispatch or owner click (this lane's recorded denials name relayed authorization — successor review-merge retired)." | `fleet-manager-startup.md:112` lane guard + fm denial record (`platform-capabilities.md` §2.1) + PRs #113/#116 today ("manager-slice landing walled today"); layer contract "a CI entry and its source may never disagree" (per-project/README.md) |
| 3 | **P1** | uncommitted denial record — new append to `docs/capabilities.md` (or findings doc) | (absent — grep "launder" on main + live branches finds only the 2026-07-09/11 precedents) | Append the PR #113 non-author-merge denial verbatim ("cross-session permission laundering"), dated, with session id | deny-wins doctrine "recorded verbatim" (`custom-instructions-core.md:65`); `platform-capabilities.md:102` precedent |
| 4 | **P1** | `websites-startup.md:20` + `websites-custom-instructions.md:15` | "**NO auto-merge enabler installed** (verify at boot; …). Park READY+green; the standing structural fix is a GITHUB_TOKEN merge-on-green workflow…" / "Merge: **NO enabler — park green**; a GITHUB_TOKEN merge-on-green workflow = the standing fix." | Rewrite both to enabler-live semantics: enabler #167 merged 14:56Z, arms claude/* on open; green PRs self-land | websites #167 merged 2026-07-12T14:56:09Z by menno420; #180 `arm-on-open: success` 15:35:14Z; websites HEAD `dfd6cce` |
| 5 | **P1** | all 8 CIs park-green tail clause + `planned-routes.md` §A row 2 + `ideas-lab-custom-instructions.md:14` + `ideas-lab-startup.md:21` *(overlap: finishedness + per-seat)* | "**merge-on-green**: a GITHUB_TOKEN workflow (none committed yet)" / "sim-lab: NO enabler — park green; a GITHUB_TOKEN merge-on-green workflow is the sanctioned fix (ORDER 003 is its install order)" | "**merge-on-green**: a GITHUB_TOKEN workflow (reference: sim-lab, live)" / sim-lab line → "merge-on-green INSTALLED (ORDER 003) — zero agent merge calls"; strike planned-routes §A row 2 with the landing pointer | sim-lab #50 `e11ed40` 10:28Z; #50–#52 self-landed; `staleness-sweep-midday.md` sim-lab row. Also removes a baked volatile fact (D-9 STATELESS) |
| 6 | **P1** | `venture-lab-custom-instructions.md:12` + `venture-lab-startup.md:13,:19` MERGE MECHANICS *(overlap: finishedness + per-seat)* | "trading — the enabler file is present but the repo **'Allow auto-merge' setting is OFF**, and push is GH013-walled; **MCP squash-on-green = repo-local recorded practice, the SOLE exception**…" | "trading: enabler INSTALLED and self-landing proven — canonical path; squash exception RETIRED-superseded" | trading #69/#70/#71/#72/#74 all merged_by github-actions[bot] today (#74 13:46:23Z); `staleness-sweep-midday.md` headline 4 |
| 7 | **P1** | `superbot-world-custom-instructions.md:40` | "**SECURITY BEFORE SECRETS** — the mineverse login-CSRF work **lands before** anything secrets-adjacent; the OAuth env-var asks stay subordinate" | Flip to "CSRF landed (mineverse #42); the open half is owner provisioning of the six OAuth/write secrets — now UNBLOCKED" | mineverse #42 merged 2026-07-12T13:54:21Z by menno420 (`3591c77` = HEAD); startup line :13 self-neutralizes correctly and needs no edit |
| 8 | **P1** | all 8 CIs WALLS clause (e.g. `self-improvement-custom-instructions.md:23`) | "**WALLS** (quote, never re-probe): docs/CAPABILITIES.md" | "**WALLS** (quote; fresh entries never re-probe, >14d re-verify with one cheap attempt): docs/CAPABILITIES.md" | kit PR #274 (v1.14.0, distributed today) DISCOVERY step 5 staleness rule; budget check needed per delta-1 caveat |
| 9 | **P1** | six-field-ask lines, all 8 CIs + startups (e.g. `self-improvement-custom-instructions.md:23`, `self-improvement-startup.md:110`) | "six-field ask = WHAT/WHERE/HOW/WHY/UNBLOCKS/VERIFY" | "…/VERIFY + RISK: ✅\|↩️\|⚠ line; structured choices carry a **bolded recommendation**, answerable with one letter" | kit PR #272 (v1.14.0) `owner-action-risk-class` advisory; kit #273 re-stamped its own 13 blocks; v3.3 grep zero hits for the choice rule |
| 10 | **P1** | BOOT 4 EXCEPTION (e.g. `self-improvement-startup.md:35`) + failsafe-wake doctrine | "KEPT AS-IS … **Verify it exists, record it in the heartbeat, leave it.**" | Verify it **delivers**: fresh-session cron = UNVERIFIED-BROKEN until a scheduled fire is proven (0-for-2 observed); failsafe wakes check the standing loop's last slot (blind-window); wedge signature + manual-fire trap noted | kit forensics PR #262 (09:02Z); kit #287 `routines.md.tmpl` (merged, **unreleased** — align wording at kit release); keep-don't-rebind rule itself stays |
| 11 | **P1** | CI dictionaries + startups routing (all 22 v3.3 files) | (absent — zero references to `docs/SKILLS.md`, `/intake`, `docs/ROUTINES.md`) | Add a **skills** keyword → `docs/SKILLS.md` (boot-wired at every adopter since v1.13.0) and an owner-request route → `/intake` (v1.14.0); route the routine-fired/cutover keyword cluster → `docs/ROUTINES.md` when kit releases #287 | kit #264 (v1.13.0), #270 (v1.14.0), #287 (unreleased); fm itself has `docs/SKILLS.md` at `5e404fd` via fm #115 |
| 12 | **P1** | `docs/prompts/v3/tools/regen_b_files.py` (+ per-project regen doctrine) | (absent — zero digest/SKILLS logic in the regen tool) | Consume kit `substrate-kit:skills-digest` / `walls-digest` fences (1,500-char budget) so seat walls/skills blocks render from kit truth — the ORDER 014 "highest-leverage single change", kit half shipped | kit #279 (unreleased); kit changelog: "Fleet-manager-side wiring … is a separate coordinated PR" — blocked on kit release |
| 13 | **P1** | `per-project/README.md` failsafe cron stagger table (D-7) vs live triggers | Table: game-lab `15 */2` · superbot-world `15 1-23/2` · ideas-lab `30 1-23/2` · venture-lab `45 1-23/2` · superbot `0 1-23/2` | Reconcile to live or re-slot: live shows game-lab at `50 */2`; superbot-world + ideas-lab + venture-lab ALL at `0 */2` (colliding with self-improvement's slot); superbot has NO seat failsafe. Manager is slot arbiter — registry work + seat orders, not just a doc edit | `staleness-sweep-midday.md` trigger section (9 standing crons with ids) vs README stagger table |
| 14 | **P2** | `docs/capabilities.md` vs `docs/CAPABILITIES.md` (I-44) | both files exist at origin/main (`git ls-tree` confirms) | Fold lowercase into the kit-owned `docs/CAPABILITIES.md`, leave a pointer | v3.1-residuals entry ("routed to the fm seat's sweep" — two sweeps since, unfixed) |
| 15 | **P2** | startups' LANDING splice, all 8 (e.g. `fleet-manager-startup.md:43`) | "Landing work rides FRESH dispatch — task + owner provenance in the founding brief (relayed = denied)" | No wording change — upgrade the evidence citation from HYPOTHESIS-adjacent (n=1, fm PR #99; the I-80d over-assertion) to n≥2 once delta 3's record is committed | `qa-incident-replay.md:106` (I-80d); today's #113 denial + #117 owner-live pass confirm both halves |
| 16 | **P2** | `planned-routes.md` §A CSRF-floor row | stopgap = websites inbox thread + startup rail | Watch — promotable to a websites durable doc once websites PR #159 lands (owner click pending); no edit until then | `staleness-sweep-midday.md` headline 2 + shortlist item 4 |

**Count: 16 deltas — 2 P0 · 11 P1 · 3 P2.**

## 5. Explicit "no delta needed" list

- v3.0 KNOWN DEFECTS queue (10 items) — all disposed in v3.1; historical.
- v3.2 defect queue #7/#8/#9 — closed in v3.3 (README changelog item 4;
  planned-routes §B rows 35/37; grep-corroborated).
- ORDER 014 §c entries 1–6 — verified "not affected — already correct" in
  the README itself.
- BOOT TRIAD + thorough-boot markers — checker-verified all 8 seats (PR
  #111 QA output); registry sync 24/24.
- planned-routes §B startup-homed split (no orphaned row) and §C fact
  corrections (all three still accurate at seat HEADs).
- Kit no-impact set (§2): gate names/check semantics, ORDER 015
  `agreement_home`, heartbeat grammar #289, preflight hard-sync, model-line
  widening #286, Evidence block, self-propagation #282, venue-grammar
  backward-compat, boot-triad posture.
- The venture "LIVE-BUT-DARK" suspect — CLEAR; no such text anywhere in
  v3.3 (grep hits only the fm-seat roster vocabulary + codetool-lab note).
- Fleet-manager, superbot, superbot-next, substrate-kit, and game-lab
  merge-mechanics prompt specifics — all verified still true at HEAD.
- CI size gate — all 8 under 8,000 chars+bytes at head (but see the delta-1
  margin caveat: superbot 7,996 / websites 7,997).
- v3.1 residuals I-38, I-58 (remaining race classes), I-66, I-72, and the
  owner-queue gaps (I-37/I-43/I-52/I-55/I-67) — still open, still correctly
  out of prompt scope or deferred.

## 6. Flags for the coordinator

1. **The PR #113 denial is unrecorded in the repo** (delta 3) — deny-wins
   doctrine requires verbatim records; grep finds only the 07-09/11
   precedents. Also notable: **PR #113's own body declared a forbidden
   landing path** ("landing path is REST merge on green") that v3.3
   explicitly bans (`fleet-manager-startup.md:70-72`;
   `custom-instructions-core.md:65`) — a v3.3-native seat did this at
   PR-open; the dictionary didn't prevent it.
2. **Kit `docs/operations/lab-loop.md:102` still carries the falsified
   claim** "the loop cannot arm itself" (called falsified twice by the
   ORDER 014 report; kit lane's fix, still absent at `5363e41`). Two v3.3
   dictionary entries route to that doc
   (`self-improvement-custom-instructions.md:32,:42`), so a v3.3 route
   target carries a known-false claim — fleet-visible integrity issue.
3. **Stagger table vs live triggers** (delta 13) — three seats' failsafes
   collide on one slot and superbot has none; this is registry + seat-order
   work the manager owns, not a prompt edit.
4. **Owner-click backlog of parked-green PRs:** idle #72/#74, games
   #59/#60, gba #68/#69, fm #116, kit pins #220/#238 (aging since 07-11),
   websites draft #163 (enabler skips drafts).
5. **Same-day decay of hand-stamped landing-path facts** — four seats'
   merge lines went stale within ~5 hours of v3.3 landing. Argues for
   delta 12 (digest-driven regen) as the structural fix over serial
   restamps.
6. **superbot-world needs re-stamps** (3/3 heartbeats contradicted) and
   pokemon-mod-lab owes an ORDER-006 ack — seat-order material for the
   next heartbeat cycle.
