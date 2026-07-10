# Fleet economics ledger — 2026-07 (EAP pre-close snapshot)

> **Status:** `complete` · compiled 2026-07-10T14:44Z
> **Provenance:** ORDER 004 (`control/inbox.md`, P0, deadline 2026-07-14). This is
> the pre-close snapshot that ORDER demanded: **the free EAP window closes
> 2026-07-14**, and this ledger is the per-lane activity/cost-signal record taken
> before it does.
> **Honest-nulls rule: not measured beats invention.** Actual CI minutes, token
> spend, and dollar costs are **NOT visible to agents** from any surface reachable
> this session — every such cell says "not measurable" and no figure below is
> estimated or invented. What IS measurable is recorded with its exact method.

## Method

All counts taken 2026-07-10 ~14:40Z via the GitHub API (MCP tools), except
session-card counts, which were read from each repo's fetched `origin/main` git
tree locally:

- **Merged PRs** — GitHub search `is:pr is:merged repo:menno420/<repo>`
  (`total_count`); window column adds `merged:>=2026-07-08`.
- **Commits (default branch)** — GitHub commit-search API,
  `repo:menno420/<repo> committer-date:>=2026-07-08` (`total_count`; the commit
  search indexes the default branch only). **Validation:** for the 9 repos with
  full (non-shallow) local clones, these API counts matched
  `git rev-list --count origin/main` exactly (e.g. venture-lab 13=13,
  pokemon-mod-lab 64=64, fleet-manager 37=37), so the method is treated as exact,
  not approximate. superbot's all-time count uses `committer-date:>=2000-01-01`.
- **Session cards** — `.md` files under `.sessions/` in the repo's `origin/main`
  tree, excluding the folder README; window = cards date-prefixed 2026-07-08/09/10.
  Repos with no `.sessions/` convention are "not measurable".
- **CI signal** — total Actions workflow runs, REST `actions/runs` `total_count`
  (all-time; the runs API here exposes no created-date filter, so the window is
  not separable — noted per row). This is the **closest visible proxy for CI
  minutes**; actual minutes are not exposed to agents → not measurable.
- **Routine/wake state** — the `routine:` line of each repo's
  `control/status.md` at `origin/main`; "not stated" where the file has no such
  line, "n/a" where the repo has no `control/status.md` at all.

**Window note:** every repo except superbot was created inside the EAP window
(first commits 2026-07-08 → 07-10), so for those rows all-time = window. superbot
predates it; its row shows window / all-time separately.

## Per-lane table

| Lane | Merged PRs (window) | Merged PRs (all-time) | Commits, default branch (window) | Session cards (window / total) | Actions runs (all-time) | CI minutes / token / $ | Routine/wake state (control/status.md) |
|---|---:|---:|---:|---|---:|---|---|
| superbot | 118 | 1,850 | 327 (all-time 5,344) | 62 / 887 | 18,317 | not measurable | n/a — repo has no `control/status.md` (pre-gen-2 home repo; Q-0213 brake lane) |
| superbot-next | 100 | 100 | 101 | 7 / 7 | 561 | not measurable | not stated — no `routine:` line (gen-1 mid-mission, band 5) |
| substrate-kit | 115 | 115 | 174 | 65 / 65 | 398 | not measurable | **armed** — hourly, `trig_01FnqnAQjLU2T8d16iHwWQ2h`, verified twice in-session (PR #125) |
| websites | 55 | 55 | 56 | 33 / 33 | 103 | not measurable | **armed** — 4-hourly, `trig_017H9Qb9oxtLgUy6sw2gnSHg`, first fire unconfirmed (due 16:00Z) |
| trading-strategy | 34 | 34 | 36 | 14 / 14 | 142 | not measurable | **armed** — 4-hourly, `trig_01Mvn5xRmqGmZJNRHgjqyLpN`, fires confirmed 04:08/08:00/12:00Z |
| superbot-games | 19 | 19 | 20 | 10 / 10 | 40 | not measurable | **not armed** — webhook/owner-driven (stated explicitly) |
| venture-lab | 11 | 11 | 13 | 6 / 7 | 18 | not measurable | **unknown** — no `routine:` line; status stale at 04:57Z (the fleet's one ENDER-MISSING lane) |
| pokemon-mod-lab | 12 | 12 | 64 | 8 / 8 | 46 | not measurable | **unknown** — no `routine:` line (hourly wake-arm ORDER dispatched, ack not visible) |
| gba-homebrew | 25 | 25 | 55 | 7 / 7 | 102 | not measurable | **unknown** — no `routine:` line (hourly wake-arm ORDER dispatched, ack not visible) |
| codetool-lab-fable5 | 14 | 14 | 15 | not measurable — no `.sessions/` | 16 | not measurable | not stated — lane wound down 2026-07-09 ("ready for archive") |
| codetool-lab-opus4.8 | 21 | 21 | 22 | not measurable — no `.sessions/` | 44 | not measurable | not stated — lane wound down 2026-07-09 |
| codetool-lab-sonnet5 | 16 | 16 | 17 | not measurable — no `.sessions/` | 26 | not measurable | not stated — lane wound down 2026-07-09 |
| fleet-manager | 26 | 26 | 37 | 18 / 18 | 79 | not measurable | **armed** — 2-hourly, `trig_01QBrp5MjZL3F9mv6KsTXTzN`, verified (this repo's status.md) |
| **Fleet total** | **566** | **2,298** | **937 (window)** | **230 window cards** | **19,892** | not measurable | 4 armed · 1 explicit not-armed · 5 unknown/not stated · 3 n/a-or-wound-down |

Counts are point-in-time (fleet-manager's row predates this ledger's own PR).

## Findings

**Top-3 heaviest lanes by merged PRs (EAP window):**
1. **superbot** — 118
2. **substrate-kit** — 115
3. **superbot-next** — 100

**Top-3 heaviest lanes by Actions runs (CI signal):**
1. **superbot** — 18,317 (all-time; ~92% of the fleet's 19,892 total runs — its
   `code-quality.yml` history dwarfs every other lane combined; window share not
   separable via this API)
2. **superbot-next** — 561
3. **substrate-kit** — 398

**Activity vs. cadence-table expectation (§2a: hourly = venture-lab,
substrate-kit, pokemon-mod-lab, gba-homebrew; 4-hourly = websites,
trading-strategy):**

- **substrate-kit vastly exceeds expectation** — 115 merged PRs and 174 default-
  branch commits in ~44 hours of repo existence. An hourly-wake lane "should"
  produce ~40 wake-sized deliveries in that span; the burst came from continuous
  session chains (the overnight 12-PR build band and the #84–#125 close-out
  chain), not routine fires.
- **gba-homebrew runs hot on CI relative to its size** — 102 Actions runs against
  25 PRs / 55 commits in ~35 hours: highest runs-per-PR ratio (4.1) of any gen-2
  lane (Tier-1 fast-full CI firing per push).
- **pokemon-mod-lab commits ≈ 5× its PR count** (64 commits / 12 PRs) — heavy
  multi-commit branches and direct pushes; its sibling game lane (gba-homebrew)
  shows the same shape (55/25).
- **venture-lab is the LIGHTEST lane by every column** (11 PRs, 13 commits, 18
  runs) — notable because it is the flagship revenue pilot and the only
  ENDER-MISSING lane; the cheapest lane is the one whose ender/ack debt is open.

**Observed in passing (evidence, not a cost figure):** pokemon-mod-lab reported
`"private": true` in the 14:56Z-timestamped API result — the URGENT owner
visibility flip from the owner-queue appears DONE; the lane's ORDER 003
(verify-via-API + record in status) can execute on its next session.

**What this ledger cannot say:** CI minutes consumed, token counts, or dollar
figures — none are exposed on any agent-reachable surface (Actions billing is
owner-only UI; token/harness spend is platform-side). If the owner exports the
Actions usage report before 2026-07-14, run counts above give the per-lane
allocation key.
