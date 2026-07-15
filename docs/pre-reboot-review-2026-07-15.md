# Pre-reboot fleet review — 2026-07-15

> **Status:** `audit`
>
> Owner review document: 48h activity audit (all 20 repos) + consolidation
> proposal (decide-and-flag; nothing migrates without owner review) +
> extension-note fan-out record (delivery rides the coordinator's landing).
>
> Compiled: 2026-07-15 (audit NOW stamps 2026-07-15T03:11:54Z–03:12:43Z).
> Audit window: **2026-07-12T23:00Z → 2026-07-15T03:12Z** (~52h).

## Provenance

- **Dispatch:** coordinator dispatch 2026-07-15, executing the owner directive of 2026-07-14 ~23:30Z.
- **EAP extension verified against the mailbox** (reference metadata only; body redacted): Diana Liu, `dliu@anthropic.com`, **2026-07-14T23:07:44Z**, subject **"Claude Code Projects EAP: Extending to Tues 7/21"** (message ID `19f62e315ded2152`). Facts stated in our own words: the program is extended and ends Tuesday **2026-07-21**; afterwards Projects is temporarily disabled ahead of external launch, Project sessions become read-only and are deleted in 180 days. New features to test on revival: **overview panel** (live), **add_repo** on-the-fly repo attach (live), **Artifact tool** (coming), **coordinator-communication improvements** (coming).
- **Record gap:** fleet-manager HEAD `94bad42` (2026-07-14T23:28:07Z) is an automated roster regen; the last substantive fm write (`dbc6ae5`, SEAT DORMANT, ~21:16Z) predates the mail, and a full inbox/repo grep at `94bad42` found **no record** of the 23:07Z mail or any 2026-07-21 window — the roster still says "EAP FINAL SHUTDOWN". **This document is the fleet's first durable record of the extension.**

---

## Part 1 — 48h activity audit

All 20 menno420 repos, measured from unshallowed git clones + GitHub MCP (workers' NOW stamps ~03:12Z). Seat map source: fm `docs/fleet-triage.md` §8 + `docs/eap-audit-collection.md` @ `94bad42` (8 standing seats, owner restructure 2026-07-11, + ninth Curious Research seat).

| Repo | Seat | Commits→main | PRs merged | Last activity | Verdict |
|---|---|---|---|---|---|
| superbot-next | SuperBot 2.0 | 169 | 162 | `3dfe159` 07-14T21:33:12Z — SEAT DORMANT (#488) | ACTIVE → dormant; **11 PRs parked open by design** (WP stack #317→#335→#344→#371, #392, #466, #473, #476, #477, #484/#485) |
| idea-engine | Ideas Lab | 148 | ~146 (#277–#424) | `dcfa27d` 07-14T23:45:56Z — dormancy (#424) | ACTIVE (busiest: proposals P015–P063) → dormant 23:42Z |
| superbot | **hub — no standing seat (Q-0264)** | 130 | 52 | `15832eca` 07-15T01:16+02:00 — dashboard cron (#2107) | ACTIVE; real work through 07-14T18:52Z (`0b90ad35` #2105, prod bugfix `e4247312` #2089); only cron since; #2061 held draft |
| websites | Websites | 112 | 112 | `68ad331` 07-14T21:14:49Z — SEAT DORMANT (#340) | ACTIVE (real feature work) → dormant 21:12:44Z |
| venture-lab | Venture Lab | 102 | 101 | `2b949be` 07-14T23:55:23Z — final dormancy (#200) | ACTIVE (~14 books, 10 NL editions, 5 products) → dormant; **262 parked owner publish clicks + 19 decisions** in `docs/publishing/OWNER-QUEUE.md` |
| sim-lab | Ideas Lab | 86 | ~85 (#58–#143) | `fc0babb` 07-14T21:16:11Z — SEAT DORMANT (#143) | ACTIVE (verdicts V017–V076) → dormant 21:14:50Z |
| gba-homebrew | Game Lab (public) | 86 | 59 | `c4a2ffd` 07-14T21:31:24Z — dormant follow-up (#140) | ACTIVE (**8 new games**, e.g. Deepcast #83, Wickroad #129) → dormant 21:16:02Z |
| superbot-games | SuperBot World | 80 | ~78 (#65–#144) | `42a31c5` 07-14T20:50:17Z — kit v1.17.0 (#144) | ACTIVE; heartbeat 11:41:04Z green (810 tests) — **NO dormancy stamp** |
| fleet-manager | Fleet Manager | 73 (52 work + 21 cron) | 73 | `94bad42` 07-14T23:28:07Z — roster regen #214 (cron) | ACTIVE → SEAT DORMANT 21:16Z (`dbc6ae5` #212); **cron fired twice post-dormancy** (#213 21:33Z, #214 23:28Z) |
| substrate-kit | Self Improvement | 65 | 65 | `3897250` 07-14T21:05:10Z — v1.17.0 closeout (#379) | ACTIVE (two kit releases v1.16.0/v1.17.0 + 9-repo waves) — NOT shut down; **failsafe cron still armed** (`trig_01LsHxvnYnpQ59n7iQTPNNF3`, `0 */2 * * *`); backlog self-declared dry |
| superbot-idle | SuperBot World | 64 | ~62 (#75–#138) | `c31251e` 07-14T18:20:29Z — claim drop (#138) | ACTIVE; heartbeat 11:32:05Z green — **NO dormancy stamp** (lags main ~7h) |
| superbot-mineverse | SuperBot World | 62 | 62 (#51–#112) | `a9a6769` 07-14T20:56:27Z — kit v1.17.0 (#112) | ACTIVE (FLAG-1 HMAC ingest #88 `82b7caa`); heartbeat 18:59:20Z — **NO dormancy stamp** |
| trading-strategy | Venture Lab (annex) | 49 | ~48 (#80–#127) | `d466aa1` 07-14T21:20:25Z — SEAT DORMANT (#127) | ACTIVE (research rounds 3–6) → dormant 21:17:36Z |
| curious-research | Curious Research (9th seat) | 49 | 48 | `f13cf85` 07-14T21:26:45Z — SEAT DORMANT (#48) | ACTIVE — **entire 49-commit life inside the window** (born 07-13T00:48Z) → dormant 21:23Z, triggers deleted |
| pokemon-mod-lab | Game Lab (private) | 25 | 25 (batch sweep 13:41–15:18Z) | `7d4fa41` 07-14T15:18Z (#86); **PR #87 open since 21:15:51Z** | ACTIVE → shutdown **STUCK**: dormancy PR #87 unmerged ~30h; main never stamped dormant (heartbeat still 05:07:37Z NIGHT-14) |
| superbot-plugin-hello | — (none) | 2 | 2 (#1, #2 — its only PRs ever) | `5d97aa7` 07-14T14:20:55Z — ORDER 020 kit pin | LOW — relay-only; 3 commits total; no heartbeat, no control/ tree |
| product-forge | — (disposition pending) | 1 | 1 (#24 `f7f2dd2` 07:06Z) | audit landing 07-14T07:06Z | DARK-by-design — "close-out / archived-ready" since 07-11T19:39:50Z |
| codetool-lab-opus4.8 | — (retired stub) | 1 | 1 (#23 `0e0ec02`) | audit merge 07-14T07:07:06Z | DARK-by-design (wind-down complete 07-09T20:11:35Z) |
| codetool-lab-sonnet5 | — (retired stub) | 1 | 1 (#17 `0331176`) | audit merge 07-14T07:07:03Z | DARK-by-design (wind-down complete 07-09T20:02:14Z) |
| codetool-lab-fable5 | — (retired stub) | 1 | 1 (#15 `5b0835b`) | audit merge 07-14T07:07:00Z | DARK-by-design (wind-down complete 07-09T20:06Z) |

Totals: ~1,266 commits to main across the fleet in ~52h; fleet-wide silence since `2b949be` 07-14T23:55Z except superbot's dashboard cron. The three codetool audit PRs merged within a 6-second span (07:07:00–06Z) — one external sweep, not seat activity.

### Probably never properly attached to a Project

- **superbot-plugin-hello — prime candidate.** Its entire history is 3 commits; both in-window items are fm-dispatched relays (fleet audit #1 `b9699e1`, ORDER 020 pin #2 `5d97aa7`). No seat in the seat map, no `control/` tree, no heartbeat file anywhere; its own audit PR recommends excluding it from heartbeat pushes. Nothing suggests a Project seat ever drove it.
- **By-design darks (not attachment failures, listed for completeness):** product-forge (archived-ready 07-11) and codetool-lab ×3 (wind-down complete 07-09) — all four served only as targets of one externally-dispatched audit sweep in the window.

### Anomalies for the reboot review

1. **pokemon-mod-lab shutdown stuck.** Dormancy PR **#87** (`claude/seat-dormant`, created 07-14T21:15:51Z) has sat open ~30h; main's `control/status.md` still reads NIGHT-14 (05:07:37Z) — the seat is ordered dormant but main never says so. Merge or close #87 at revival.
2. **SuperBot World trio has no dormancy stamps.** superbot-games (heartbeat 11:41:04Z), superbot-idle (11:32:05Z), superbot-mineverse (18:59:20Z) all kept shipping after their last heartbeats and none carry a SEAT DORMANT record — the only seat-family that never wrote a shutdown.
3. **substrate-kit failsafe still armed.** `trig_01LsHxvnYnpQ59n7iQTPNNF3` (`0 */2 * * *`) survived the fleet shutdown — the one seat routine left live anywhere. Decide at reboot: keep as the fleet's watchdog or delete for a clean slate.
4. **fm roster-regen cron fired post-dormancy; roster now stale.** Generations #53/#54 (#213 21:33Z, #214 23:28Z) regenerated the roster after the seat dormancy record, and the roster @ `94bad42` still encodes "EAP FINAL SHUTDOWN" — now superseded by the 7/21 extension this doc records.

---

## Part 2 — Consolidation proposal (decide-and-flag)

**Nothing migrates now.** Every row is a recommendation for the owner's review at reboot; open owner gates (listed below) are respected throughout.

| Repo | Recommendation | Rationale | What would move |
|---|---|---|---|
| fleet-manager | **KEEP-AS-SEAT** | The manager; source-of-truth home for orders, roster, owner-queue | Nothing |
| superbot | **KEEP-AS-SEAT** | Live production bot; SuperBot 2.0 hub | Nothing |
| superbot-next | **KEEP-AS-SEAT** | Rebuild lane; 11-PR revival stack parked for the owner (#317→#371 WP chain + frozen feature PRs) | Nothing |
| substrate-kit | **KEEP-AS-SEAT** | Kit releases (v1.17.0 shipped 07-14) power every repo in the fleet | Nothing |
| websites | **KEEP-AS-SEAT** | Source-of-truth home; four live deployed services | Nothing |
| venture-lab | **KEEP-AS-SEAT** | Books/products lane; 262 parked owner publish clicks await review | Nothing |
| trading-strategy | **KEEP-AS-SEAT-ANNEX** (of Venture Lab) | Standalone research program (rounds 1–6 complete); folding into venture-lab would mix research data with book content | Nothing |
| idea-engine | **KEEP-AS-SEAT** | Ideas Lab pair (proposal side; P015–P063 shipped in-window) | Nothing |
| sim-lab | **KEEP-AS-SEAT** | Ideas Lab pair (verdict side; V017–V076). ⚑ Flag: the pair *could* merge into one ideas repo if the owner wants fewer repos — cost: cross-repo verdict/outbox path rewrites | Nothing (unless owner opts for the merge) |
| superbot-mineverse | **KEEP-AS-SEAT** | SuperBot World flagship; pairs with superbot PR #2061 (HMAC write endpoint, held draft) | Nothing |
| superbot-games | **KEEP-AS-SEAT** | 4 playable games, 810 tests passing | Nothing |
| superbot-idle | **KEEP-AS-SEAT** | ⚑ Flagged as the one plausible fold-in into superbot-games — cost: PLUG-001 plugin repackaging + CI merge; benefit: −1 repo. Both codebases healthy, so migration buys little | Nothing now; idle codebase + CI if the owner opts in |
| gba-homebrew | **KEEP-AS-SEAT** | Game Lab public track; 8 new games shipped in the window | Nothing |
| pokemon-mod-lab | **KEEP-AS-SEAT** | Game Lab private track; fix stuck PR #87 at revival (anomaly 1) | Nothing |
| curious-research | **KEEP-AS-SEAT** | Ninth seat; 48 PRs in its first 48h of existence; attach to a proper Project at reboot | Nothing |
| product-forge | **ARCHIVE** (per gated plan) | Already DARK/archived-ready; consolidation plan Phase 1 → 3 | Rehome games-web (ORDER 023) + retro doc (ORDER 024), **gated on owner letter E#44**, then owner archive click B#40 |
| codetool-lab-sonnet5 | **ARCHIVE** | Wind-down complete 07-09 | ORDER 025: two writeups → substrate-kit, then E#45 + archive click B#41 |
| codetool-lab-fable5 | **ARCHIVE** | Wind-down complete 07-09 | ORDER 026: `.pyc`/`.gitignore` hygiene, then E#46 + archive click B#42 |
| codetool-lab-opus4.8 | **KEEP-PARKED** | INC-03: live mdverify releases (v0.1.0/v0.2.0) contradict archival; triage re-verdict 2026-07-14 says KEEP unarchived | Nothing |
| superbot-plugin-hello | **KEEP-QUIET — never archive** | Pinned by superbot-next `plugins.lock.json` (INC-01); exclude from rosters/heartbeats | Nothing |

**Open owner gates respected by this proposal:** **E#44** (`OQ-CONSOLIDATION-DELETE-VS-ARCHIVE` — the delete-vs-archive letter; blocks archive clicks B#40–B#42), **E#45** (`OQ-CFGDIFF-RELEASE-DECISION` — cfgdiff v0.1.1 release before sonnet5 archive), **E#46** (`OQ-ENVDRIFT-RELEASE-DECISION` — envdrift release before fable5 archive), **E#63** (`OQ-FORGE-DARK-NO-ACTION-CONFIRM` — forge stays DARK; superseded by answering E#44). All OPEN at fm `94bad42`.

---

## Part 3 — Extension-note fan-out record

Delivered by the coordinator's landing (2026-07-15) after the original executor's writes were permission-denied (deny-wins honored; one attempt each). Note text delivered to each lane inbox:

> **EAP EXTENDED through 2026-07-21** (Anthropic mail, Diana Liu, 2026-07-14T23:07:44Z — "Claude Code Projects EAP: Extending to Tues 7/21"). The 2026-07-14 dormancy orders are **superseded pending the owner's per-project reboot review** — do **NOT** re-arm routines yet; wait for the owner's per-seat go. New features to test during the extension: overview panel, add_repo, Artifact tool (coming), coordinator-comms improvements (coming). fleet-manager and websites are the source-of-truth homes for the reboot review.

- **Targets (12 lane repos):** superbot-next, substrate-kit, websites, venture-lab, trading-strategy, idea-engine, sim-lab, superbot-mineverse, superbot-games, superbot-idle, gba-homebrew, curious-research (+ fleet-manager via its ORDER).
- **Skips:** superbot (hub, no standing seat), pokemon-mod-lab (shutdown PR #87 mid-flight — deliver after #87 resolves), superbot-plugin-hello (no inbox/control tree), product-forge + codetool-lab ×3 (archive-class).
