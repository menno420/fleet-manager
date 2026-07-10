# Games-program mapping proposal (Q-0259 r.5 · ORDER 012)

> **Status:** `proposal — ⚑ OWNER-REVIEW.` Committed 2026-07-10 per the owner dispatch
> (~21:4xZ; ORDER 012 in `control/inbox.md`). One proposed mapping, decide-and-flag;
> alternatives one line each. **FOUNDING PACKAGES DEFERRED until the owner reacts**
> (Q-0259 r5 + the dispatch's explicit done-when). Silence-window doctrine does NOT
> apply here — the dispatch names the owner reaction as the gate.
>
> Supersedes the pre-birth sketch in `projects/games-program/meta.md` +
> `expected-seed.md` (committed via PR #39 @ `3d105d9`): that sketch predates two
> reshaping facts — games-web shipped as the forge's first product, and the read-only
> data API surfaced as the blocker for BOTH games-web phase 2 and websites
> stats/explorer pages. Its Project-1/Project-2 picks are CONFIRMED below; its
> "Project 3 TBN / superbot-games open question" is RESOLVED below; its per-repo seed
> checklist remains valid founding-package input once the owner reacts.

---

## 0 · What superbot PR #1920's pattern actually is (verified, not assumed)

**It is a versioned committed-JSON feed + contract file — NOT a live HTTP service.**
Verified at superbot origin/main (`655e0fea`), merged PR #1920 (2026-07-10T03:27Z):

- **Contract:** `dashboard/data/dashboard_data_contract.json` — version 1, **slice
  semantics** (only `contracted_families` are pinned: `meta` + `bugs`; other families
  stay free until contracted family-by-family with a version bump). Guaranteed fields
  per record; any change to a contracted surface = edit THIS file + bump `version`.
- **Producer:** `scripts/export_dashboard_data.py` — stdlib-only, stamps
  `meta.schema_version`, `DASHBOARD_*` parity constants. **Reads repo-static sources
  only** (AST-parsed subsystem registry, `docs/ideas/`, bug-book, `.sessions/`, env
  scan) — it **never touches the production database**.
- **Checker:** fail-closed `check_dashboard_contract` in
  `scripts/check_dashboard_data.py`, CI-enforced — a producer-side rename of a
  contracted field fails CI in superbot instead of silently blanking a consumer page
  (the BUG-0022 desync class).
- **Consumption:** the websites repo's dashboard fetches the committed
  `dashboard/data/dashboard.json` over **raw.githubusercontent.com** (websites
  `dashboard/data_source.py`) — the estate's cross-repo rule verbatim (websites
  CLAUDE.md): *"cross-repo data arrives only as committed JSON read over
  raw.githubusercontent.com (read-only, forward-only)."*

**The delta that matters for games:** game-state lives in superbot's **production
Postgres**, which the #1920 producer never reads. So "the API over #1920's pattern" =
the contract/checker/committed-feed pattern applied verbatim, **plus a NEW producer
that can see the DB** — that producer is the only genuinely new engineering, and it
pins where the API must live (§2).

Consumer-side, the pattern is already half-adopted: games-web's
`data/schema/game-state.schema.json` (`contract: games-web.character-sheet`, semver)
*explicitly* "mirrors superbot's versioned dashboard-data-contract pattern (superbot
PR #1920)" (games-web README @ forge main `11efb060`), and its phase-2 line is the
blocker verbatim: *"Real-data integration is explicitly out of scope: it needs a
superbot-lane read-only API to serve live game-state on this contract."*

---

## 1 · The mapping — 3 repos → 3 Projects (proposed)

Per Q-0260, Projects are named by their one repo. Post-core lanes → gen-3 pipelined
fast path (all three bootable in one paste wave once packages exist).

| # | Project / repo | Scope (mandate) | Reads from superbot | First shippable increment |
|---|---|---|---|---|
| 1 | **pokemon-mod-lab** (exists, PRIVATE, HEAD `a76ada7`) | Emerald **QoL+** mod line — concept already ruled (Q-0262.7); the 12 shipped game-feel patches are the foundation | Nothing | Next QoL+ patch batch on the 12-patch foundation; ROM-builds CI as required-check prep |
| 2 | **gba-homebrew** (exists, public, kit v1.7.0, HEAD `bc73da7`) | Original GBA homebrew — Lumen Drift SCOPE-COMPLETE; invent-new-games track | Nothing | Lumen Drift release-prep (README/controls/ROM artifact so the owner can PLAY it); first order presents the 2 unpicked concepts as options (the r5 "present a few options" pattern) |
| 3 | **superbot-games** (exists, public, kit v1.7.0, HEAD `4493292`) — **becomes the third dedicated Project** | The Discord-games **engine + content** project: continue the mining port (`games/mining/` core+sim) + exploration quest/encounter engine (`games/exploration/quest/`), 121 tests at HEAD (grep-verified); invent/extend bot-connected games as portable engine modules | **Source, read-only:** superbot game-cog source at pinned SHAs for parity goldens (the held games-mining instruction's own rule: "mint parity goldens AS you port"); **data, later:** the games feed of §2 for balance/telemetry. Never live imports — cross-repo rule above | Fix the known CI gap (gate runs only `tests/` — add `games/exploration/tests`, the one-line change from the overnight review), then next playable mining/quest slice |

- **games-web is NOT a fourth games repo** — it stays product-forge's product (phase 1
  merged, forge PRs #4+#5). The pre-games-web sketch that imagined the web-visual
  layer inside the games program is retired per the dispatch; the program's edge to it
  is a **data edge only** (§3).
- **In-bot game cogs** (~20 live game surfaces at superbot HEAD: mining, fishing,
  farm, blackjack, casino, rps_tournament, deathmatch, creature + creature_battle,
  the btd6 family, economy/inventory/treasury/paragon, counting, four_twenty, xp,
  karma, games_cog…) **stay superbot-owned and live**. The **superbot-next band-6
  games port stays the rebuild's job** (Q-0241 lane; band-6 is the next band after
  band-5 live-drive per the round-3 launch pack). The games program does not take
  over that port — relationship: superbot-games builds engine modules band-6 can
  consume + game design/content improvements that land via superbot-lane
  games-finishing sessions (launch pack §2b); the data feed (§2) gives all three
  Projects read access to live game telemetry without touching the bot.

**Alternatives considered (one line each):**
- *Project 3 = fresh TBN repo, superbot-games stays a hub concern* — rejected: both
  resident gen-1 lanes wound down (PRs #13/#14), leaving the estate's largest games
  codebase ownerless, and Q-0266 volume-first says populate existing material, not
  re-derive an engine in an empty repo; also saves the owner one repo-creation click.
- *Fold superbot-games INTO superbot (a `games/` package in the hub)* — rejected: the
  hub's Q-0213 brake + 13.9k-test CI make it the slowest iteration surface in the
  estate; the ruling asks for dedicated projects.
- *Merge the two GBA repos into one Project* — rejected: r5 says three projects, the
  concepts/toolchains differ (decomp mod vs Butano homebrew), and pokemon-mod-lab's
  PRIVATE carve-out (Q-0260.3) doesn't mix with a public lane.

---

## 2 · The read-only data API — placement (the load-bearing call)

**RECOMMENDATION: the API lives in the superbot lane — a new contracted committed-JSON
feed (working name `dashboard/data/games.json` + `games_data_contract.json`), NOT its
own repo/Project, NOT inside a games repo.**
One-line why: **#1920's pattern co-locates contract + producer + fail-closed checker
with the data's owner, and the game-state owner is superbot** (its Postgres, its
audited service seams per `docs/ownership.md`) — any other home needs production-DB
credentials crossing repos, exactly the live coupling the cross-repo rule exists to
forbid.

Shape (pattern applied verbatim):
- Versioned contract with **slice semantics** — contract only what a consumer renders,
  family by family. **First family = the mining character-sheet**, produced TO
  games-web's already-committed consumer contract (`games-web.character-sheet` schema)
  — the consumer defined the shape first; the producer meets it.
- Fail-closed checker + producer parity constants in superbot CI, same as #1920.
- Consumers (games-web phase 2, websites stats/explorer) fetch the committed JSON over
  raw.githubusercontent.com — read-only, forward-only, zero auth surface.
- **Privacy by construction:** contract slice semantics double as the redaction
  boundary (#1920's `site.json` whitelist precedent) — only opt-in/renderable
  families ship; no raw per-guild dumps.

**Honesty note on "live":** the pattern yields **snapshots at refresh cadence**, not
live state. That satisfies a character-sheet viewer and stats pages (games-web phase 2
is a *viewer*, not a game client). One open engineering question, decided in the
implementing superbot PR (decide-and-flag there, not here): the refresh path — the
existing `dashboard-data-refresh` workflow reads repo-static sources and has no DB
access, so the game-state export needs either (a) a bot-side scheduled task on the
Railway worker (has DB creds) committing the feed via the GitHub API, or (b) a
workflow holding a read-only DB secret. Either stays inside the superbot lane.

**Alternatives (one line each):**
- *Own `games-api` repo/Project* — rejected: cross-repo prod-DB credentials + a fourth
  project the ruling didn't ask for, for zero consumer benefit (consumers read raw
  URLs either way).
- *Inside superbot-games* — rejected: it doesn't own the production data; consumers
  would read a copy-of-a-copy with no CI seam to the producer.
- *Live HTTP endpoint on the Railway worker* — **deferred, not rejected**: the
  true-"live" upgrade path if snapshot cadence ever proves too stale, but it adds an
  auth/privacy/uptime surface and breaks the committed-JSON rule — snapshot-first is
  CORRECT-over-BEST (Q-0266).

**websites stats/explorer:** flagged honestly — no stats/explorer entry exists yet in
websites `docs/ideas/backlog.md` @ `44a9fa6` (grep-verified); the need is the owner's
stated intent in this dispatch. The feed unblocks it the same way it unblocks
games-web; a websites backlog entry should be filed when the first family ships
(routing note in §3).

---

## 3 · Sequence (Q-0266 volume-first: populate → consolidate → maintain)

Owner's read that the API is "likely highest-leverage": **VALIDATED, with one
refinement** — it is the only item that unblocks TWO consumers, but none of the three
game Projects needs it to boot, and it is *superbot-lane* work. So it goes **first
among dependencies, parallel to the boots** — sequencing it strictly before the boots
would idle three lanes on a feed they don't consume on day 1 (anti-volume-first).

1. **NOW (superbot-lane order, next superbot session):** games feed first slice —
   `games_data_contract.json` (version 1, family = mining character-sheet on
   games-web's schema) + DB-reading producer + fail-closed checker + refresh path
   (the (a)/(b) call above, decided in that PR).
2. **PARALLEL (owner paste wave, after owner reacts to THIS proposal):** founding
   packages for the three Projects (gen-3 born-continuous template per
   `projects/games-program/expected-seed.md`), boots pipelined — pokemon-mod-lab
   straight into QoL+; gba-homebrew presents concept options; superbot-games CI fix +
   next playable slice. **HELD until the owner reaction — nothing in this step
   executes from this proposal.**
3. **ON FEED LIVE:** games-web phase 2 (forge order — consumer contract already
   committed, render real data); websites stats/explorer page (websites order + file
   the backlog entry).
4. **LATER (owner-gated, Q-0266 phase 2):** consolidation pass — including whether
   band-6's ported games retire the in-bot originals and whether the feed grows
   leaderboard/economy families.

---

## 4 · Flags on this proposal (veto points)

- ⚑ **superbot-games = Project 3** (resolves meta.md's open question; the biggest
  judgment call here).
- ⚑ **API in the superbot lane as a committed snapshot feed** (not a live service, not
  a new repo) — with the live-endpoint upgrade path named, deferred.
- ⚑ **API parallel to the boots, not gating them** (refines the owner's "first"
  instinct with the dependency evidence).
- ⚑ **Founding packages DEFERRED** — step 2 above waits for the owner's reaction to
  this document. Everything else here is paper; nothing executes.
