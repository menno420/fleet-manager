# Fleet consolidation plan — 2026-07-26 (product topology) · v1

> **Status:** `historical`
>
> **⚠ SUPERSEDED same day by [`2026-07-26-consolidation-plan-v2.md`](2026-07-26-consolidation-plan-v2.md)**
> — the owner pushed back that this repo's own docs had not been read, and he was
> right. v1 was built on the GitHub API census alone and missed
> `owner-reflection-2026-07-21.md` (*"the highest-value work: verification, not
> more shipping"*), the owner's existing 8-Project grouping in `fleet-triage.md`,
> and the standing owner-queue items that already answered two of its three
> questions. **v2 corrects the framing** (review surfaces, not repo count) and
> **reverses one concrete call** (websites' control-plane is the owner's review
> surface — it stays live, it does not get archived).
>
> Kept for provenance: its **census evidence is still sound and is reused by v2** —
> the 22-repo measurement, the stranded-asset table, and the `superbot-games`
> plugin-packaging finding.
>
> Original header follows.
>
> Owner-directed, drafted 2026-07-26 from a live census of
> all 22 repos (GitHub API at the dates below, not from the roster's derived
> snapshot). Owner decisions taken in the hub chat 2026-07-26 are recorded
> inline as **OD-1/2/3**.
>
> **Supersedes** [`2026-07-12-repo-consolidation-plan.md`](2026-07-12-repo-consolidation-plan.md).
> That plan organized the fleet by **agent seat** (19 → 16 repos, 8 seats). The
> seats no longer exist — the autonomous program closed 2026-07-22. This plan
> organizes by **product**, which is what the owner asked for: *"give every main
> feature/idea its own repo while combining things that belong together."*

---

## 1 · The answer to "what's the most valuable thing right now"

**Make `superbot-next` the single home of the bot — pull the games, the idle
engine, the mineverse web app and the bot's two websites into it, and stop
landing new work in old `superbot`.**

It wins on four counts at once:

1. **Biggest structural win available.** Five repos collapse into one — the
   largest single reduction in the fleet, and it removes the fleet's worst
   duplication (`botsite` + `dashboard` exist in *both* `superbot` and
   `websites` today).
2. **It is the prerequisite for the thing the owner named as the goal.** OD-1:
   *"the eventual goal should be to continue with superbot-next because the old
   superbot repo is filled with too much architectural debt."* Live-testing a
   bot whose game plugins live in four other repos is not a sensible exercise.
   Consolidation is step zero of the cutover, not a detour from it.
3. **Every day it waits costs compound interest.** Old `superbot` is still
   taking commits (HEAD 2026-07-26). Work landing there lands in the codebase
   the owner has decided to retire, and has to be ported again later.
4. **It is unblocked.** The other two high-value moves both wait on the owner —
   ShiftLife beta needs an Expo account and beta tester names; the cutover
   itself needs the test-bot token and owner time. This one needs neither.

**The runner-up, for the record:** ShiftLife is the only thing in the fleet on a
revenue path and it is beta-ready (7 of 8 free-core items done, live API on
Railway). It is not first here only because its remaining blockers are owner
clicks, not agent work. If the owner has 20 minutes, spending them on the Expo
account and beta names is worth more than anything on this page.

---

## 2 · What the fleet actually is (census, 2026-07-26)

22 repos. `superbot` was created 2025-08-10. **The other 21 were all created
between 2026-07-07 and 2026-07-24** — during a 15-day autonomous agent program
that closed 2026-07-22. Fifteen of them have `PROJECT CLOSEOUT` as their most
recent commit.

### Alive (real work in the last 7 days)

| Repo | Commits/7d | What it is |
|---|---:|---|
| `superbot` | 100+ | The live Discord bot on Railway. 5,991 commits. Still shipping. |
| `shiftlife` | 37 | Created 2026-07-24. **All 37 commits this week.** Beta-ready consumer app, live API. The only revenue path. |
| `product-forge` | 19 | Almost entirely `phone-controller` — a signed, field-verified Android app. |
| `websites` | 44 | Automated `[bake]` data refresh only. No human/agent work. |
| `fleet-manager` | 100 | Automated roster regen only. No human/agent work. |

### The stranded-asset problem

The fleet's problem is **not** lack of output. It is that finished output is
sitting at zero delivery:

| Asset | State | Delivered |
|---|---|---|
| `superbot-next` | Complete rebuild: 49 subsystems + kernel, **533/533 golden parity**, boots on real Postgres | Never cut over |
| `phone-controller` | Signed APK pipeline, owner-playtested 2026-07-23 | Buried in `product-forge/products/`, a repo marked "archive-ready" |
| venture-lab SKUs | 19 publish-READY + 3 bundles + 6-book fiction series | 1 of ~20 live |
| `envdrift`, `cfgdiff` | Finished, documented CLI tools | **0 releases each** |
| Lumen Drift (GBA) | `lumen-drift-v1.3` tagged, playable web builds | Released ✅ |
| `mdverify` | v0.1.0 + v0.2.0 | Released ✅ |
| `trading-strategy` | 0/13 strategies cleared significance | An honest null — complete, nothing to ship |

---

## 3 · The diagnosis

**The repo topology encodes agent seats, not products.** "One seat = one repo"
was the organizing rule of the autonomous program, and it was a reasonable rule
*for that program* — it gave each agent an unambiguous write scope (ruling
Q-0260: a seat writes only its own repo).

The seats are gone. The repos remain. That is the entire reason there are 22.

The visible symptoms all trace to this one cause:

- `phone-controller`, a real shipped product, lives two directories deep inside
  a repo named after the *seat* that built it.
- `botsite` and `dashboard` exist twice — once in `superbot`, once in
  `websites` — because a rebuild seat was given its own repo.
- The bot's games live in four repos because the game work was split across
  four seats (Seat A, Seat B, mineverse, plugin exemplar).
- `idea-engine` and `sim-lab` are two repos because the ideation *pipeline* had
  two seats — generate and verify — not because they are two products.

Consolidating by product is therefore not a cleanup chore. It is **translating
the fleet out of a dead organizing principle into a live one.**

---

## 4 · The organizing rule

One test, applied to every repo:

> **Does this have its own users, its own release cadence, and its own reason to
> exist if everything around it disappeared?**

- **Yes** → its own repo.
- **No — it exists to serve another product** → fold into that product.
- **No — it is a record of finished work** → archive.

Two hard constraints override the rule and cannot be traded away:

1. **The legal rail.** `pokemon-mod-lab` is a private Pokémon Emerald decomp
   containing Nintendo-copyrighted material; `gba-homebrew` is public, original,
   Butano-only. These **must never share a repo**, regardless of how neatly they
   both say "GBA game." This is the one place where two repos is the *correct*
   answer.
2. **Live release URLs.** `mdverify` has live releases installed from
   `github.com/menno420/codetool-lab-opus4.8`; `substrate-kit` has 26 releases
   that every repo in the fleet vendors by version. Moving either breaks
   working install paths — so neither moves without a redirect plan.

---

## 5 · Target structure — 22 → 9

| # | Repo | Absorbs | Why |
|---|---|---|---|
| 1 | **`shiftlife`** | — | The consumer app + Personal Operations Core. Already clean (`apps/`, `packages/`). The revenue bet. **Untouched by this plan.** |
| 2 | **`superbot-next`** → renamed **`superbot`** at cutover | `superbot-games`, `superbot-idle`, `superbot-mineverse`, `superbot-plugin-hello`, `websites` (botsite + dashboard) | One product, one repo. Everything absorbed here exists *only* to serve the bot. |
| 3 | **`phone-controller`** | graduates out of `product-forge` | Real shipped Android product: own users, own APK release cadence, zero coupling to the fleet. `product-forge`'s own README defines this "graduation" mechanic. |
| 4 | **`gba-homebrew`** | — | Public, original GBA games. Lumen Drift v1.3 shipped. |
| 5 | **`pokemon-mod-lab`** | — | PRIVATE. **Legal rail — never merges with #4.** |
| 6 | **`venture-lab`** | — | **OD-2: stays a live repo.** 19 publish-ready SKUs + the Night Kiln series are inventory the owner intends to sell. |
| 7 | **`substrate-kit`** | the standalone CLIs: `mdverify`, `envdrift`, `cfgdiff`, `proxybench` (as `tools/`) | The portable agent kit (26 releases, vendored fleet-wide) plus four small dev tools that belong nowhere else. |
| 8 | **`fleet-manager`** | `idea-engine`, `sim-lab`, `trading-strategy`, `websites` (control-plane + review), `product-forge` (remainder), the three `codetool-lab-*` shells | Becomes the **records archive** of the closed program. It is already the fleet's records custodian — the natural home. |
| 9 | **`curious-research`** | — | A personal gift repo with an audience of one. Not fleet work; costs nothing; **left alone.** |

**Archived, not deleted (OD-3):** old `superbot` (at cutover), plus the 13
repos absorbed above. GitHub archive is read-only, hidden from the active list,
free, and reversible in one click.

**Result: an active repo list of 9** (8 once old `superbot` is archived at
cutover), down from 22.

### Why `superbot-next` is the survivor, not old `superbot`

Per OD-1. It is also the technically correct direction independent of the debt
argument: the games were **built against superbot-next's plugin contract**, not
the old bot's. Verified live in `superbot-next/plugins.lock.json` —
`superbot-idle-plugin` v0.1.0 and `superbot-plugin-hello` v0.1.0 are already
pinned by manifest hash. Folding them in is completing a design that already
exists, not inventing one.

**One correction to note before anyone plans around it:** `superbot-games` is
*not* yet plugin-packaged — it has no `pyproject.toml` or `manifest.py`, only
pure-domain packages and 103 tests. Its README is accurate that "host-facing
adapters [are] left as a later ladder rung." So W2 below is genuine build work,
not a file move. `superbot-mineverse` is likewise not a plugin — it is a
decoupled web app that consumes a versioned data contract and must never touch
Postgres or hold the bot token. That safety architecture survives the move as a
CI rail, not as a repo boundary.

---

## 6 · The sequence — one thing at a time

Each workstream is independently completable and leaves the fleet working. Do
them in order; none is a prerequisite for ShiftLife, which proceeds in parallel
on its own track.

### W1 — Graduate `phone-controller` *(smallest, safest, do first)*
Move `products/phone-controller/` to its own repo with history preserved
(`git subtree split`). Carry over the APK release workflow and its signing
secret. Leave a pointer in `product-forge`.
**Done when:** the new repo builds a signed APK from a clean clone and its CI is
green. **Risk:** low — nothing depends on it.
**Why first:** it is the one migration with zero blast radius, and it proves the
subtree-split + secrets recipe that W2 and W3 reuse at larger scale.

### W2 — Consolidate the bot into `superbot-next`
Four sub-steps, each its own PR:
- **W2a** — `superbot-idle` + `superbot-plugin-hello` → `plugins/`. These are
  already pinned dependencies; this is the true file move.
- **W2b** — `superbot-games` → `plugins/games/`, **and build the missing
  host-facing adapters** so mining / exploration / D&D / fishing actually load
  under the plugin contract. This is the real engineering in the plan.
- **W2c** — `superbot-mineverse` → `web/mineverse/`, keeping its own Railway
  deploy target and adding a CI rail that fails the build if the web subtree
  imports Postgres or reads the bot token.
- **W2d** — `websites`' `botsite` + `dashboard` → `web/`, resolving the
  duplication against old `superbot` in favour of the `websites` rebuild.
**Done when:** one repo boots the bot with all game plugins loaded and 533/533
parity still green. **Risk:** medium, contained — old `superbot` keeps shipping
untouched throughout.

### W3 — Live-test, then cut over *(owner-gated)*
The blocker is a test-bot token and owner time, not code. Sequence: test guild →
port bands 5–7 live → shadow-run against production → cut over → rename
`superbot-next` to `superbot` → archive the old repo.
**This is the only step that touches the production bot.** Nothing before it
does.

### W4 — Fold the standalone CLIs into `substrate-kit`
`envdrift`, `cfgdiff`, `proxybench` → `tools/`. **`mdverify` moves only with a
redirect plan** — its v0.1.0/v0.2.0 install URLs are live and must keep working
(archived repos keep serving releases, so archiving `codetool-lab-opus4.8`
in place is the safe default).

### W5 — Build the archive
Move the closed programs' records into `fleet-manager`: `idea-engine` and
`sim-lab` verdict ledgers, `trading-strategy`'s null result, `websites`'
control-plane + review, `product-forge`'s remainder. One index page, one
read-only home.

### W6 — Archive the emptied repos
Only after each migration is verified. Thirteen repos, one click each,
reversible.

### W7 — Retire the dead apparatus
`roster-regen.yml` regenerates a roster of seats that no longer exist, ~hourly,
forever. With the fleet at 9 repos and no autonomous seats, the roster, the
trigger-health watchdog and the owner-queue machinery are all monitoring a
program that ended.

**Full CI treatment: [`2026-07-26-ci-consolidation.md`](2026-07-26-ci-consolidation.md).**
Measured live: **97 workflow files, 397 Actions runs/24h, 46% cron** — and ~44%
of the workflow surface is autonomous-agent merge plumbing. The important
sequencing point is that **archiving a repo stops its scheduled workflows**, so
W6 removes ~60 workflow files and ~175 daily cron runs *for free*. Do not
hand-tune 97 files first; land the repo consolidation, then standardize the
survivors on three uniform checks (`test` / `build` / `deploy`).

---

## 7 · What this plan deliberately does not do

- **It does not touch `shiftlife`.** It is the only healthy, actively-built,
  correctly-structured repo in the fleet. Consolidation work should route
  around it, not through it.
- **It does not delete anything** (OD-3).
- **It does not merge the two GBA repos** — see the legal rail in §4.
- **It does not cut over the production bot.** W3 is owner-gated and explicitly
  sequenced behind live testing.
- **It does not re-litigate the 2026-07-12 plan's archive list.** That plan's
  three archive candidates are all handled here, by product logic instead of
  seat logic.

## 8 · Open items for the owner

None blocking — W1 and W2 can start immediately. Two worth knowing:

1. **W3 needs your time and a test-bot token.** It is the gate on retiring the
   architectural debt you named. Everything else in this plan is preparation
   for it.
2. **The `mdverify` redirect** (W4) is the only migration that can break a
   working install URL. Default is to leave it in place and archive around it.
