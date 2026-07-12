# Repo consolidation plan — 2026-07-12 (phase B, owner-facing)

> **Status:** `plan`
>
> **Proposed — awaiting owner review. Nothing here self-executes.**
> Finalized from the phase-A census
> ([`research/2026-07-12-repo-consolidation-census.md`](../research/2026-07-12-repo-consolidation-census.md)
> @ `6ac4352`, PR #119), reconciled with the game-lab-seat proposal
> ([PR #121](https://github.com/menno420/fleet-manager/pull/121), since
> **merged to main** — its proposal doc now carries a supersession pointer
> back to this plan), which this plan **cites and supersedes**; this plan
> remains the finalized successor. Phase 1 is agent work; Phases 2–3 are yours.
> Every archive here is a reversible GitHub settings toggle — **nothing is
> deleted, ever, under this plan.**

## What you get, in one paragraph

The fleet today is **19 repos** across 8 seats. After this plan: **16
unarchived repos, same 8 seats**. Three inert lab repos (product-forge,
codetool-lab-sonnet5, codetool-lab-fable5) get their named assets rehomed by
agent PRs (Phase 1), then you click "archive" on each (Phase 3 — reversible).
Along the way you answer a short set of one-letter decisions (Phase 2),
including the cron-cadence trims that cut the fleet's scheduled Actions burn
(~235 runs/day today, concentrated in 3 repos) by roughly 80%. **ARCHIVE-NOW:
none** — no repo is archived before its assets land somewhere safe.

## ⚠ First structured choice — the delete-vs-archive contradiction

Adopted from PR #121's gate #1 (its "Read this first" banner). Two of your own
instructions contradict:

- **Standing ruling, 2026-07-10:** "delete no repos (they are the fleet's
  memory)" — recorded at superbot
  `docs/ideas/adopt-codetool-lab-tools-2026-07-10.md`.
- **Ask, 2026-07-12:** "delete the test repos."

Pick one:

- **A (recommended): harvest → archive (read-only), delete nothing.**
  Reversible, preserves the fleet's memory per your own standing ruling, and
  achieves the consolidation goal (repos out of the active roster). PR #121's
  adversarial verifier found every "test-scratch"-labeled repo holds either
  shipped releases (mdverify), finished unreleased tools (envdrift, cfgdiff),
  or a host-pinned contract exemplar (superbot-plugin-hello) — none is safe to
  delete on the label.
- **B: deletion, as an explicit written override of your 2026-07-10 ruling** —
  per named repo, and only after the archive has held for a **≥7-day
  cooling-off** (PR #121 Stage G). Not recommended.

Answer "contradiction: A" (or B). The rest of this plan assumes A.

## Target end-state (19 → 16 unarchived repos, 8 seats)

Seat → repos table, reproduced from the census § "Proposed end-state":

| Seat | Repos | Notes |
|---|---|---|
| fleet-manager | fleet-manager | coordination layer, unchanged |
| superbot-2.0 | superbot + superbot-next (+ superbot-plugin-hello) | plugin-hello kept as the out-of-tree contract exemplar; superbot itself re-verdicts after CUT-3 |
| websites | websites | live Railway services |
| self-improvement | substrate-kit (+ codetool-lab-opus4.8 kept quiet) | opus4.8 stays as released-tool host (mdverify v0.1.0/v0.2.0, owner-ruled 2026-07-10) |
| superbot-world | superbot-games + superbot-idle + superbot-mineverse | all quiet until the superbot-next plugin host lands, then re-verdict |
| game-lab | gba-homebrew + pokemon-mod-lab | Track B public / Track A private-by-necessity |
| ideas-lab | idea-engine + sim-lab | the Q-0264 pipeline pair |
| venture-lab (money) | venture-lab + trading-strategy | live triggers; paper grading from 2026-07-17 |

**Archived (reversibly): product-forge, codetool-lab-sonnet5,
codetool-lab-fable5.** ARCHIVE-NOW: none.

## Census vs PR #121 — matrix reconciliation

The census (PR #119) and the game-lab proposal (PR #121) were produced
concurrently and independently. Where they touch the same repos:

| Repo | Census | PR #121 | Reconciled |
|---|---|---|---|
| superbot-plugin-hello | KEEP-QUIET (contract exemplar, seeded `bbaccec`) | KEEP — pinned by superbot-next `plugins.lock.json` manifest sha256 @ `65f4ba7` | **Agree: keep, never archive.** The pin claim is **verified at HEAD this session**: superbot-next origin/main @ `1aec607` `plugins.lock.json` pins `superbot-plugin-hello` v0.1.0, manifest_hash `sha256:06023075…`. #121's pinned-dependency evidence *strengthens* the census keep — archiving would re-open PLUG-001-class blocks. Posture stays KEEP-QUIET (dormant-by-design). |
| codetool-lab-opus4.8 | KEEP-QUIET unarchived | KEEP unarchived | **Agree** — standing 2026-07-10 ruling + live mdverify releases v0.1.0/v0.2.0. |
| codetool-lab-sonnet5 / -fable5 | MIGRATE-THEN-ARCHIVE | HARVEST-THEN-ARCHIVE, release-in-place recommended | **Agree — same verdict, different word.** #121's release-in-place (its Stage D Option 1, the proven workflow_dispatch recipe) is adopted here and interacts with Phase 2 decisions 1–2: **release BEFORE archive**, since archiving freezes the tag-push path forever. |
| substrate-kit | KEEP | KEEP-INFRA | **Agree** — every fleet repo pins `kit_version` and runs kit-owned gates. |
| trading-strategy | KEEP | ARCHIVE-AFTER-CHECKLIST | **Census wins: KEEP.** The holdout is SPENT (irreplaceable evidence ledger), paper record paper-0001 is in-flight with first grading 2026-07-17 (`trig_015aNMg5ncoSE2Roe4MKjQnr`), and #121's own checklist rule ("never archive with an active routine") defers it past that date anyway. Re-verdict after the paper lane concludes. |
| superbot-games / superbot-idle | KEEP-QUIET | ARCHIVE-AFTER-CHECKLIST | **Census wins: KEEP-QUIET for now** — both are defined feedstock for the superbot-next plugin host (310 / 1,131 passing tests), and their "checklist" items (disposition the 4 stranded green PRs) are folded into the stranded-work list below regardless. Re-verdict when the plugin host consumes them. |
| product-forge | MIGRATE-THEN-ARCHIVE | ARCHIVE-AFTER-CHECKLIST | **Agree in substance** — rehome 3 named assets first (Phase 1), then archive (Phase 3). |

## Phase 1 — agent migration PRs (start now, no owner action needed)

Each written as a routed ORDER spec (kit grammar: executor / scope /
done-when).

**Product-forge lane gate — codex finding (from the #121 review) applied:**
the product-forge seat is **DARK** per the fleet-manager instructions — it
never receives ORDERs; its disposition is owner-queued. The P1-1/2/3 specs
below therefore name only **non-forge executors**, and the rehomes execute via
non-forge lanes (fleet-manager sessions or the destination repos' own lanes —
product-forge content is readable cross-repo), **only after the owner approves
this plan** (the plan itself is the disposition surface that superseded
owner-queue E#37 / OQ-FORGE-DISPOSITION). That approval gate is the one
exception to this phase's "start now".

**ORDER P1-1 — product-forge: rehome `products/games-web/`**
- executor / owning repo: superbot-world seat (superbot-games) **or** websites
  seat — decided at PR time.
- scope: move `products/games-web/` (self-contained static character-sheet
  game UI + `game-state.schema.json` v1.0.1 contract + tests) out of
  product-forge. **Decision criterion (census):** if the websites Fleet Arcade
  (catalog slice shipped in websites `06409f5`) can host it as a playable
  catalog entry unchanged, it goes to the **websites arcade**; if it is to
  become a bot-game plugin surface instead, it goes to **superbot-games**. The
  executing agent checks the arcade catalog first and records the call in the
  PR body.
- done-when: games-web + schema + tests live and green in the target repo; a
  pointer note lands in product-forge's final status.

**ORDER P1-2 — product-forge: rehome the phase-2 data-API proposal**
- executor / owning repo: superbot seat (superbot).
- scope: move `products/games-web/docs/phase2-data-api-proposal.md` (an
  unanswered API request addressed to the superbot lane) into superbot docs,
  indexed per superbot's docs conventions.
- done-when: the doc is reachable in superbot's doc graph and cited from the
  games-web new home.

**ORDER P1-3 — product-forge: rehome the retro**
- executor / owning repo: fleet-manager seat (this repo).
- scope: move product-forge `docs/retro/2026-07-11-self-review.md` into
  fleet-manager `docs/retro/`.
- done-when: file merged here with a Status badge + README link (repo doc
  gate green).

**ORDER P1-4 — codetool-lab-sonnet5: port the two writeups**
- executor / owning repo: self-improvement seat (substrate-kit).
- scope: port (1) the **v0.1.1 release-decision writeup** and (2) the
  **differential-testing method doc** ("corpus vs a reference parser found 3
  real bugs behind green tests") to their homes — the census names kit-lab
  benchmark practice (substrate-kit `bench/` docs) as the differential-testing
  home; the release-decision writeup rides with it.
- done-when: both docs merged in substrate-kit; sonnet5's final status points
  at them.

**ORDER P1-5 — codetool-lab-fable5: repo-hygiene precondition (owner-directed)**
- executor / owning repo: any wind-down session on codetool-lab-fable5.
- scope: remove the committed `__pycache__/*.pyc` under
  `src/envdrift/commands/` and add the missing top-level `.gitignore` (both
  verified in tree @ `a6cf1a9`; owner: "fix fable5's committed .pyc files +
  missing .gitignore before archiving").
- done-when: `git ls-files '*.pyc'` empty; `.gitignore` at root; CI green.

**ORDER P1-6 — superbot-mineverse: close PR #31**
- executor / owning repo: superbot-world seat (superbot-mineverse).
- scope: close (not merge) Codex PR #31 with a one-line disposition — its two
  findings were fixed by merged #42 (`3591c77`) and dispositioned by #43
  (`f8b6dbf`). **Verified still open this session** (state open,
  mergeable_state blocked, created 2026-07-11T16:41Z).
- done-when: #31 closed with the disposition comment.

**ORDER P1-7 — codetool findings-export coverage check**
- executor / owning repo: fleet-manager seat.
- scope: confirm the three labs' succession/retro content is fully covered by
  superbot `docs/eap/gen1-grand-review-2026-07-09.md` + fleet-manager
  `docs/experiments/harness-x-model-2026-07-09.md`; export any gap before the
  archive clicks.
- done-when: a one-paragraph coverage verdict lands in the owner queue thread
  or this plan's follow-up.

## Phase 2 — owner decisions (one letter each)

**1. cfgdiff v0.1.1 (codetool-lab-sonnet5) — release it?**
- A **(recommended)**: release-in-place via the proven workflow_dispatch
  recipe (the route opus4.8 used to ship mdverify v0.1.0/v0.2.0 on
  2026-07-09). One agent slice; zero tags exist on origin today, and
  **archiving freezes the tag-push path forever**, so this lands before the
  Phase 3 click.
- B: explicitly accept cfgdiff staying unreleased; archive as-is.

**2. envdrift (codetool-lab-fable5) — release/adopt?**
- A **(recommended)**: same release-in-place route (needs a release workflow
  added first — none exists), then archive; optionally adopt envdrift as a
  fleet tool afterwards (your named environment-tidying interest).
- B: accept unreleased; archive after P1-5 lands.

**3. superbot cron trims (the ≈170 runs/day burner)**
- Today: `ci-rerun-watchdog.yml` `*/12 * * * *` ≈120/day +
  `pr-conflict-guard.yml` `*/30 * * * *` ≈48/day.
- A **(recommended)**: watchdog → hourly (24/day) and conflict-guard → every
  2 h (12/day): ≈168/day → ≈36/day, keeping both functions alive.
- B: keep as-is until superbot's post-CUT-3 re-verdict.

**4. websites + fleet-manager cron trims (≈65 runs/day combined)**
- Today: websites `auto-merge-enabler.yml` `13,43 * * * *` = 48/day (its
  healthcheck 6-hourly + review-bake daily ≈5/day more); fleet-manager
  `roster-regen.yml` every 2 h ≈12/day, each firing able to commit to main.
- A **(recommended)**: enabler → event-driven (`pull_request` trigger — the
  enabler only has work when a PR opens) and roster-regen → regen-on-change
  (push-triggered) or 2×/day.
- B: keep as-is.

**⏰ TIME-CRITICAL bundle — decide ≤2026-07-13, one sitting** (from PR #121
§3.0, cited to idea-engine `control/status.md` 15:33Z, verifier-confirmed;
the EAP window ends 2026-07-14). #121's framing: "FOUR decisions in ONE
sitting — (a) Lumen Drift itch.io go/no-go, (b) pokemon playtest verdicts,
(c) the gba concept pick, (d) the post-EAP standing-routine posture." Plus the
websites-cutover choice that rides the same sitting:

- **5a. Lumen Drift v1.3 itch.io — go/no-go?** **Recommended: GO** — the ROM
  is shipped in `dist/`, publishing is reversible (delist), and it starts real
  player feedback.
- **5b. Pokemon-mod-lab playtest verdicts** (6 game-feel patches await your
  play). **Recommended: schedule the playtest sitting** — it is the seat's
  only blocker.
- **5c. GBA next-concept pick.** **Recommended: pick at the same sitting**
  from the concept docs; any letter unblocks the lane.
- **5d. Post-EAP standing-routine posture.** **Recommended: keep the 2-hourly
  failsafes, retire EAP-specific pacemakers** — matches the cost findings
  (failsafes are cheap; the burn is in repo crons, not Routines).
- **5e. Websites cutover Options A–D** (retire superbot `dashboard/` +
  `botsite/` in favor of the Railway replacements). **Recommended: decide now,
  execute after CUT-3** — #121 flags that retiring superbot surfaces before
  the cutover decision would strand live services.

## Phase 3 — owner clicks (settings-only; AFTER Phase 1 lands)

Six-field asks, `docs/owner-queue.md` format:

**3.1 Archive product-forge**
- WHAT: GitHub archive toggle (read-only, reversible).
- WHERE: github.com/menno420/product-forge → Settings → Danger Zone →
  "Archive this repository".
- HOW: one click, after ORDERs P1-1/2/3 are merged.
- UNBLOCKS: removes it from the kit re-render fan-out (it drew re-render PRs
  for nothing on 2026-07-12); ends the 19-repo sprawl's first slice.
- VERIFIED-NEEDED: census § product-forge — self-declared "close-out /
  archived-ready" @ `b25b090` (#23); heartbeat frozen 2026-07-11T19:39:50Z;
  no armed trigger references it (trigger map, 832-record snapshot).
- Blocking: not-blocking; sequenced after Phase 1.

**3.2 Archive codetool-lab-sonnet5**
- WHAT: GitHub archive toggle.
- WHERE: github.com/menno420/codetool-lab-sonnet5 → Settings → Danger Zone.
- HOW: one click, after ORDER P1-4 **and your Phase 2 decision 1** (release
  first if A — the tag path freezes at archive).
- UNBLOCKS: second consolidation slice; no trigger references it.
- VERIFIED-NEEDED: census § sonnet5 — last commit `66c3dfc` (#16) 2026-07-09;
  zero tags on origin; owner ruling 2026-07-10 "archive … after harvest".
- Blocking: not-blocking.

**3.3 Archive codetool-lab-fable5**
- WHAT: GitHub archive toggle.
- WHERE: github.com/menno420/codetool-lab-fable5 → Settings → Danger Zone.
- HOW: one click, after ORDER P1-5 **and your Phase 2 decision 2**.
- UNBLOCKS: third consolidation slice; no trigger references it.
- VERIFIED-NEEDED: census § fable5 — `.pyc`/.gitignore defect verified @
  `a6cf1a9`; owner precondition recorded.
- Blocking: not-blocking.

**3.4 Protect pokemon-mod-lab `main`**
- WHAT: branch protection / ruleset on `main` — the **only unprotected
  default branch in the fleet** (`protected:false` via `list_branches`;
  every other checked repo is protected or has documented required-check
  evidence).
- WHERE: github.com/menno420/pokemon-mod-lab → Settings → Branches (or
  Rules → Rulesets).
- HOW: add a ruleset matching what you set on websites 2026-07-09.
- UNBLOCKS: closes the fleet's one protection gap.
- VERIFIED-NEEDED: census § pokemon-mod-lab + Methods note (rule details
  unverifiable fleet-wide, boolean flag only).
- Blocking: not-blocking, but cheap and worth doing at the same sitting.

## Current stranded work (from PR #121, sample re-verified live this session)

**9 stranded green PRs awaiting your click/decision** (#121 §3.1): substrate-kit
#220 + #238 (ratify-or-reject pin PRs — "Merge = ratify; close with a word =
reject"), superbot-games #59 + #60 (merge clicks; #60 carries the D1/D2
schema/audit decision), superbot-idle #72 + #74 (#74 is a workflow-file PR —
owner-only merge), gba-homebrew #68 + #69 (merge clicks; #68 carries the "add
`NDS ROM build` to required checks" ask), fleet-manager #116 (meta restamp).
**Verified open this session via the GitHub API: superbot-idle #72/#74,
gba-homebrew #68/#69, fleet-manager #116** (plus mineverse #31 above); the
substrate-kit and superbot-games pairs are taken on #121's verifier citation.

**3 red main-CI legs** (#121 §3.2, on citation): superbot-next
`golden-parity` (20/20 recent failures on main → superbot-2.0 seat's first
slice), fleet-manager `roster-regen` (7 failures 2026-07-12, gens still land —
a late step is broken → this seat), websites `review-bake` (both runs ever
failed → your "allow Actions to create PRs" toggle first, then the seat
re-runs). These ride Phase 1/2 as fix assignments, not new asks.

## Cost table — where the scheduled burn is

| Repo | Scheduled burn today | After Phase 2 (recommended letters) |
|---|---|---|
| superbot | **≈170 runs/day** (watchdog ≈120 + conflict-guard ≈48 + dashboard-refresh 2-hourly + backup daily + codeql weekly) | ≈36/day + the non-trim crons |
| websites | **≈53 runs/day** (enabler 48 + healthcheck 4 + review-bake 1) | ≈5/day (enabler event-driven) |
| fleet-manager | **~12 runs/day** (roster-regen 2-hourly, can commit to main) | ~2/day or on-change |
| everything else (15 repos) | **zero** (verified per-repo by grepping `schedule:` at origin/main; superbot-next carries only backup/restore-verify crons) | zero |

Plus **kit re-render fan-out**: 13 kit-planted repos each draw ~1 re-render PR
per kit release — **~9 repos × 2 releases on 2026-07-12 alone**. Every
unarchived dormant planted repo (product-forge today) pays this for nothing;
archiving the three ends their share.

## Corrected premises — two stale findings, fixed explicitly

1. **The trading engine never moved to venture-lab.** Full-history search
   shows no backtest engine ever existed in venture-lab; the real engine lives
   in trading-strategy `src/trading_lab/` (~126 KB, 15 strategy modules, 197
   test functions). The holdout is **SPENT** and paper grading fires
   **2026-07-17** — trading-strategy stays **KEEP**.
2. **superbot-plugin-hello is no longer empty.** Seeded at commit `bbaccec`,
   2026-07-12T13:29Z (6 files incl. the load-bearing
   `[project.entry-points."sb.plugins"]`) — the "empty repo" finding is stale,
   and the repo is now pinned by superbot-next `plugins.lock.json` (verified
   at `1aec607` this session).

## Reversibility statement

Archive only, nothing deleted. All migrations land **before** any archive
toggle. GitHub unarchive is a settings toggle — every step in this plan can be
undone. Deletion exists only behind the First-structured-choice option B:
explicit written owner override, per named repo, after a ≥7-day post-archive
cooling-off. This plan recommends never taking it.

## Provenance & supersessions

- Built from the phase-A census @ `6ac4352` (PR #119) + the prompt-currency
  audit (PR #118, since **merged** —
  `docs/research/2026-07-12-prompt-currency-audit.md` on main @ `d38bafb`).
- **Cites and supersedes [PR #121](https://github.com/menno420/fleet-manager/pull/121)**
  ("Proposal: fleet consolidation + seat reset plan", head `9a5075a`, green,
  docs-only): its delete-contradiction gate, decision bundle, stranded-work
  lists, and harvest options are folded in above; its RESET ORDER template and
  8 v1.1 instruction-delta candidates are **routed to the prompt-v3.4 restamp**
  (deliverable 2 on this branch), not this doc — applied to the
  `docs/prompts/v3/` **sources** with the `projects/<seat>/` copies regenerated
  (`regen_b_files.py` + `--write-registry`), never to the generated copies
  directly (codex #121 finding, already the v3.4 method). **Merged-state note
  (2026-07-12):** #121 has since **merged to main** (19:34Z, `b127b98`) rather
  than being closed; its proposal doc
  (`docs/proposals/2026-07-12-consolidation-and-reset-plan.md`) now carries a
  supersession pointer to this plan, which remains the finalized successor.
- **Supersedes owner-queue E#37 (OQ-FORGE-DISPOSITION):** the census verdict
  MIGRATE-THEN-ARCHIVE replaces E#37's option-A "keep the repo parked"
  framing; the new ask is this plan's Phase 3.1 archive click (after Phase 1
  rehoming), and the seat-registry half (pointer-stub `projects/product-forge/`)
  rides the same disposition.
