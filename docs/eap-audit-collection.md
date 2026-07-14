# EAP audit collection — fleet fan-out tracker (2026-07-14)

> **Status:** `living-ledger` — AUDIT-WATCH tracking instrument
>
> Tracking instrument for today's EAP PROJECT AUDIT fan-out: each Project
> lands `docs/audits/eap-project-audit-2026-07-14.md` in its repo(s); later
> sweeps update the table below as audits arrive at each repo's HEAD.
> Synthesis + the final-email draft fires once the **majority** of audits
> are in. Seeded at wake 0845Z from the 2026-07-14T08:34–08:38Z read-only
> scan (all probes via GitHub MCP `get_file_contents` at HEAD + open-PR
> sweeps; citations per row).

## Collection table

Snapshot verdict at seed time (08:34–08:38Z): **0 / 13 target repos** had the
audit doc at HEAD; in flight born-red: websites #332 · substrate-kit #366 ·
venture-lab #192; the remaining 10 not started. fleet-manager (this repo)
landed its own audit before the scan.

**Sweep 2 verdict (probed 2026-07-14T09:51–09:52Z, `git fetch` + `git
cat-file` at each live origin/main — ground truth, not MCP):
7 / 13 target repos have the doc at HEAD** (superbot-next, substrate-kit,
websites, venture-lab, idea-engine, superbot-mineverse, gba-homebrew).
Seat-coverage view: those 7 docs cover **11 / 13 repos** (venture-lab's
covers trading-strategy; idea-engine's covers sim-lab; mineverse's covers
games + idle; gba's covers its track, with pml's full-seat edition in
flight on pml PR #84). Not covered at HEAD: superbot (hub) and
trading-strategy repo-local (now ordered via its ORDER 015).
**The 7/13 majority threshold is CROSSED at this sweep** — per the update
protocol the synthesis + final-email draft step is now DUE; flagged to the
coordinator as its own lane (this sweep is the closeout record PR #193, not
the synthesis pass). ⚑ Self-initiated flag: majority-crossed call recorded
here rather than starting the synthesis inside the closeout PR.

| Repo (menno420/) | Audit doc at HEAD? | Landed PR # | Headline numbers | Top ANTHROPIC asks |
|---|---|---|---|---|
| superbot | **no** (checked 09:52Z, HEAD `e7d4d68`) — hub narrative corpus lives in its `docs/eap/` by design; closeout ORDER 006 dispatched (#2096) | — | — | — |
| superbot-next | **YES** (checked 09:52Z) | **#468** (merged 2026-07-14T09:47:53Z, `ecc1be7`) | 222 session cards · 466 commits on main · 466 PRs opened / 448 merged / 11 closed / 7 open · ≈1 PR per ~20 min | (1) populate the auto-mode classifier denial `Reason` field ("'No reason provided' denials cost a diagnosis round-trip per incident"); (2) permit read-only `git clone` of a repo `add_repo` already authorized; (3) fresh-session cron delivery 0-for-2 + scheduled-wake reliability (§9) |
| substrate-kit | **YES** (checked 09:52Z; `4a23d7c` = merge of #366, ON MAIN) | **#366** (merged 2026-07-14T09:03:23Z) | 191 session cards · 361 PRs / 350 merged · 452 commits · 19 releases v1.0.0→v1.15.0 · suite 442→1523 tests | (1) read-only `api.github.com` GETs through the agent proxy; (2) MCP PR-state ~25-min staleness — expose TTL/fetched-at; (3) include `auto_merge` in `pull_request_read`; (4) coordinator-surface scheduled-wake primitive; (5) send_later drops need tombstones (B-1/B-5/B-6/B-9/B-10) |
| websites | **YES** (checked 09:52Z; `1c82253` = merge of #332, ON MAIN) | **#332** (merged 2026-07-14T09:01:36Z) | 201 session cards · 353 commits · 332 PRs / 316 merged · 1414 tests across 4 suites | (1) document the classifier's intended consent shape for agent-initiated merges (pain 1, entire >1 h landing tail); (2) MCP staleness signal; (3) branch-deletion 403; (4) proxy 403-vs-404 masking (PR #328); (5) TLS 1.3 in the proxy MITM path (§9/§3) |
| venture-lab | **YES** (checked 09:52Z; `72a9c8a` = merge of #192, ON MAIN; §8 attributions corrected by follow-up #193 `b3c4dbb`) — seat audit, covers trading-strategy too | **#192** (+ #193 follow-up) | 2 lanes ~4.4 d / ~5 d · trading: 5,055 registered configs → 0 promoted · 131+56 stale `claude/*` branches measured | ask A: classifier merge denials (incl. "Reason: No reason provided"); ask B: branch deletion 403; ask D: no-API owner surfaces (routines/Projects/rulesets); ask E: api.github.com + GraphQL walls + `actions_list` ignores `per_page` (bug) |
| idea-engine | **YES** (checked 09:52Z) — covers BOTH Ideas-Lab repos (idea-engine + sim-lab) | **#413** (merged 2026-07-14T09:12:06Z, `8162d1e`) | seat total 545 PRs opened / 543 merged · 772 commits · ≈3.6-day window | (1) cross-repo MCP read scope fixed at session creation (§9.2); (2) branch deletion — 389 undeleted merged branches (§9.3); (3) Write-tool REPORT.md refusal (§9.5); (4) trigger tombstones + cross-session binding + filtered trigger list (§9.4/§10.1) |
| sim-lab | covered — seat audit single-homed at idea-engine (`docs/audits/eap-project-audit-2026-07-14.md@8162d1e` "Covers BOTH repos"); no repo-local doc at HEAD (checked 09:52Z) by design | (via idea-engine #413) | see idea-engine row | see idea-engine row |
| trading-strategy | **no** repo-local doc (checked 09:52Z, HEAD `0ea6950`) — seat-covered by venture-lab #192; repo-local landing ordered via its **ORDER 015** (dispatch PR #122, merged 09:42:26Z) | — | see venture-lab row | see venture-lab row |
| superbot-idle | covered — three-repo seat audit at mineverse (idle pinned @ `a23e67c`); no repo-local doc at HEAD (checked 09:52Z) | (via mineverse #107) | see mineverse row | see mineverse row |
| superbot-games | covered — three-repo seat audit at mineverse (games pinned @ `1c323c1`); no repo-local doc at HEAD (checked 09:52Z) | (via mineverse #107) | see mineverse row | see mineverse row |
| superbot-mineverse | **YES** (checked 09:52Z; `405c834`) — covers games + idle + mineverse | **#107** (merged 2026-07-14T09:11:39Z by github-actions[bot]) | seat total 222 cards · 525 commits · 370 PRs (369 merged, 1 closed, 0 open) · landing medians 4.05 / 0.4 / 1.48 min | (1) agent-merge classifier + single shared identity rate-limit (§9 #1/#5); (2) MCP repo-scope fixed at session creation (§9 #2); (3) fresh-session cron 0-for-2 + trigger hard-deletion without tombstone (§9 #4) |
| pokemon-mod-lab | **in flight** — PR **#84** "EAP project audit 2026-07-14 (full seat edition)" OPEN, `mergeable_state: clean`, head `6349c6c` (opened 09:21:36Z; re-read 09:52Z); covers BOTH pml + gba; parks green by design — repo has no merge automation | — (parked green on #84) | per PR body: 26-parked-PR famine (pml) + 17.5 h refuse-to-arm epoch (gba), full denial ledger | per PR body: classifier/merge friction, scheduling/wake friction — read the doc on the PR head |
| gba-homebrew | **YES** (checked 09:52Z; `687ea9d`) | **#131** (merged 2026-07-14T09:27:00Z) | 280 commits · 88 cards · 130 PRs / 121 merged at 4.1-min median · 11 games in ~4.3 days | (1) silent-empty in-session curl to api.github.com (worse than an error, §9.2); (2) classifier inconsistency — pacemaker re-arm denied after ~20 identical grants (§9.3); (3) `add_repo` denied ~1-in-2 in scheduled wakes (§9.3); (4) tag/release/branch-delete 403s (§9.4) |
| **fleet-manager** | **YES — DONE** ([`docs/audits/eap-project-audit-2026-07-14.md`](audits/eap-project-audit-2026-07-14.md) at HEAD) | **#189** (merged 2026-07-14T08:23:47Z) | 204 commits on main · 190 PRs (187 merged) in ≈4.6 days · 138 session cards · ≈41 PRs/day (highest-cadence seat) | (1) owner-delegable merge grant + inspectable classifier verdicts (§9.1); (2) trigger/session lifecycle events + tombstones (§9.2); (3) queued cross-session delivery / wake-a-sibling (§9.3); (4) per-session cost/token visibility (§9.4); (5) GitHub read surfaces (settings/rulesets) + `claude/*` branch-delete + fresher PR-state (§9.5) |

**Footnote:** curious-research PR #42 ("EAP project audit — Curious
Research seat", created 08:33:56Z, born-red) is also open with an audit —
outside the 13-target list, tracked here for completeness.

## Update protocol

- Each later sweep re-probes `docs/audits/eap-project-audit-2026-07-14.md`
  at every target repo's HEAD, fills the row (checked-at time, landed PR #,
  2–4 headline numbers, top ANTHROPIC asks quoted from the doc's own
  ranked section), and re-states the running tally.
- When the tally crosses **7 / 13** (majority), the sweep that observes it
  starts the synthesis + final-email draft.
- Absence-on-head during a born-red window is expected, not a failure
  signal — a PR opens minutes before its doc content is pushed.
