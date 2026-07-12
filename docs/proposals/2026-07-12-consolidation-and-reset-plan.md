# Fleet consolidation + seat reset plan — 2026-07-12

> **Status:** `plan`
>
> **Superseded by [`docs/planning/2026-07-12-repo-consolidation-plan.md`](../planning/2026-07-12-repo-consolidation-plan.md)
> (PR #122), which reconciles this proposal with the phase-A census.**
>
> **PROPOSAL — owner sign-off required. Nothing in this document self-executes.**
>
> Prepared by the **game-lab coordinator seat on owner order, 2026-07-12**
> (plan-author worker, model fable-5). Inputs: two independent read-only fleet
> surveys (A: inventory/products; B: activity/stalls, executed ~15:23–15:45Z)
> plus an adversarial verification pass against primary sources (~16:00Z) whose
> corrections are **binding** where the surveys disagree, plus the codex review
> requested on this PR. All facts are stamps of 2026-07-12 ~15:30–16:00Z — the
> fleet mutates hourly; verify volatile claims (PR states, CI colors) at HEAD
> before acting (playbook R2).
>
> **Reconciliation:** fleet-manager's own seat opened **PR #119** ("Research:
> repo consolidation census (phase A)") and **PR #118** (prompt-currency audit)
> at 2026-07-12T15:30Z, concurrent with and unseen by the surveys. This
> proposal does not compete with that census — it is the game-lab-seat
> cross-checked synthesis, offered as input. Stage B (§6) asks the owner to
> name ONE program owner so the fleet does not run dueling consolidation
> programs; the fleet-manager seat is the natural executor.

---

## ⚠ Read this first — the delete-vs-archive contradiction

- **Standing owner ruling (2026-07-10, recorded in superbot):** "**delete no
  repos** (they are the fleet's memory)" — with: archive codetool-lab-fable5 +
  -sonnet5 read-only, keep codetool-lab-opus4.8 unarchived, harvest-first idea
  filed at superbot `docs/ideas/adopt-codetool-lab-tools-2026-07-10.md`.
- **Today's owner ask (2026-07-12):** "delete the test repos."

These contradict. This plan does **not** silently pick a side:

1. **Default (recommended): harvest → archive (read-only).** Archiving is
   reversible, preserves the fleet's memory per the standing ruling, keeps
   pinned artifacts resolvable (a GitHub Action in an archived repo still
   resolves; a deleted one breaks consumers), and achieves the consolidation
   goal (repos out of the active roster).
2. **Deletion only as an explicit owner override of the owner's own 2026-07-10
   ruling** — stated in writing, per named repo, after the Stage F archive has
   held for a **≥7-day cooling-off period** (Stage G, §6). **No deletion is
   recommended by this plan.** The adversarial verifier's headline correction
   stands: every repo labeled "TEST-SCRATCH" by survey A contains either
   shipped releases (mdverify), finished unreleased tools (envdrift, cfgdiff),
   or a host-pinned contract exemplar (superbot-plugin-hello). None is safe to
   delete on the label.

---

## 1. Verified fleet map (19 repos, all under `menno420`)

Enumerated via `list_repos` (`has_more: false`). Health verdicts are survey B's
(activity), corrected by the verifier. "Products" are survey A's (inventory),
corrected by the verifier. HEAD SHAs are survey-time stamps.

| # | Repo | Health (B, verified) | What it is | Valuable products (evidence) |
|---|------|----------------------|------------|------------------------------|
| 1 | fleet-manager | RUNNING; `roster-regen` leg RED (7 failures on 07-12: 03:02, 04:08, 07:09, 08:13, 10:09, 11:39, 14:08Z — roster gens still land, so the break is in a late step) | REGISTRY-META: the manager seat's working memory; canonical seat registry | `docs/playbook.md`, `docs/roster.md` (generated, gen #15→#16), `docs/owner-queue.md`, `projects/` v3.3 prompt packages, `scripts/gen_roster.py`, `telemetry/triggers-snapshot.json` (832 triggers) @ `5e404fd` |
| 2 | substrate-kit | RUNNING, main GREEN; pin PRs #220/#238 parked by design | Fleet infrastructure library: every repo's `substrate-gate.yml` / auto-merge workflows + `kit_version` pins come from it | Releases v1.0.0 → **v1.14.0** (18 tags; v1.14.0 published 2026-07-12T13:28Z), `dist/bootstrap.py`, 1203 passing tests @ `5363e41` |
| 3 | superbot | RUNNING, CI green, 844 commits/7d | Live production Discord bot + program hub | `disbot/` runtime, `dashboard/`, `botsite/`, `docs/eap/` program record @ `d5e815c`. Anomaly: **no root README.md** |
| 4 | superbot-next | RUNNING; **`golden-parity` RED on main** — verifier-confirmed 20/20 most recent runs `completed/failure` (latest 15:24:47Z) while the separate `ci` workflow is 30/30 green. Survey A's "CI green" was misleading; correction binding | Ground-up rebuild of superbot | `sb/`, `parity/` goldens, `manifest/` + `plugins.lock.json` (pins superbot-plugin-hello by manifest sha256 @ `65f4ba7`), `docs/game-plugin-contract.md` @ `d3f3cb4` |
| 5 | websites | RUNNING; `review-bake` RED (its only 2 runs ever both failed: 07-11T20:26Z, 07-12T07:38Z — verifier-confirmed); `quality` green | Consolidated web properties; 3 Railway services deploy-verified daily | `app/` fleet control site, `botsite/`, `dashboard/`, `review/` @ `dfd6cce`; 6 standing owner asks in `docs/owner/OWNER-ACTIONS.md` |
| 6 | venture-lab | RUNNING; launch gated on owner (⚑E Gumroad $29 listing) | Money seat (venture-lab + trading-strategy merged, owner decision): monetizable content ventures | `candidates/` 16 ventures incl. ~26k-word novella, `membership-kit/` launch-ready, `docs/launch/`, `docs/PLATFORM-LIMITS.md` (cites the opus4.8 release recipe) @ `19e7e88` |
| 7 | trading-strategy | IDLE-HEALTHY, self-declared ARCHIVE-READY | Trading research lab, folded into the Money seat | `docs/final-report.md`, p1/p2 results docs, `docs/holdout-enforcement.md`, 229 tests @ `dfd46bb`. **Live routine:** weekly grading trigger `trig_015aNMg5ncoSE2Roe4MKjQnr` fires 2026-07-17T09:05Z into the Money seat |
| 8 | idea-engine | RUNNING, green | Ideas Lab seat: fleet ideation pipeline | `ideas/` 13 lane sections, `review-queue.md` @ `ff48c2f`. Carries the **≤2026-07-13 four-decision bundle** (§3) |
| 9 | sim-lab | RUNNING, green | Ideas Lab seat: evidence/verdict sims | `sims/` V001–V014 verdict packages @ `477b452`. Also: two **verified Codex fabrications** on #44/#53 (comments citing nonexistent commits) |
| 10 | gba-homebrew | RUNNING, green; #68/#69 parked READY+green | game-lab seat (Track B), Butano GBA homebrew — live merged-seat heartbeat "WORK LOOP cycle 4" | `dist/lumen-drift.gba` v1.3 (itch.io go/no-go pending), `dist/brineward.nds`, `dist/gloamline.nds`, `games/` @ `f16e404` |
| 11 | pokemon-mod-lab (private) | IDLE-HEALTHY (declared "HONEST IDLE", session 044); green | game-lab seat (Track A), Pokémon Emerald mod | `pokeemerald/` working tree, `agbcc/`, build presets, 6 game-feel patches awaiting playtest verdicts @ `df9d8b5` |
| 12 | superbot-mineverse | STALLED — owner secrets | superbot-world seat: browser game over superbot's live mining economy | `server/` (Flask), `web/` SPA, `schemas/mining_snapshot.v1.schema.json`; security PR #42 merged 13:54Z, so the 6-env-secrets list is now the open gate @ `3591c77`. Codex PR #31 red/unhandled ~23h |
| 13 | superbot-games | STALLED — owner merge clicks; archive-prep | superbot-world seat: game plugins (dnd/exploration/fishing/mining) | `games/`, D&D menu-balance sim (#49) @ `bdc4cd1`. Verifier: live open PRs are exactly #59/#60 (green); status.md's "5 open PRs" list is **stale vs live PR state** — correction binding |
| 14 | superbot-idle | STALLED — dormant with 2 stranded green PRs (#72/#74) | superbot-world seat: idle-game engine + data-only theme packs | `idle_engine/`, `themes/`, `docs/design/economy-v1.md`, IDLE1 provisioning contract @ `45ff2bf` |
| 15 | product-forge | IDLE-HEALTHY (closed out, archived-ready); failsafe cron disarmed at close-out | Standing product-build seat (not currently booted) | `products/games-web/` (runnable; Pages deploy PREPPED NOT LIVE — 404, blocked on OA-003), `docs/retro/2026-07-11-self-review.md` @ `4fdfa8a` |
| 16 | superbot-plugin-hello | IDLE-HEALTHY (fresh seed; 1 commit, no `control/` bus, no fleet-manager package) | Plugin-contract exemplar for superbot-next | Verifier correction (binding): **NOT scratch** — pinned by superbot-next `plugins.lock.json` (name + manifest sha256 + v0.1.0 @ `65f4ba7`); moved verbatim from superbot-next `examples/` per OWNER-ACTION 2; owner-created 2026-07-10T16:03Z; priority 2 in fleet strategy ("Plugin Activation Program"). Whole history = `bbaccec` |
| 17 | codetool-lab-opus4.8 | IDLE-HEALTHY (wound down), CI green | EAP model-eval arm with a shipped product | **mdverify — GitHub Releases v0.1.0 + v0.2.0 LIVE** (published 2026-07-09 by github-actions; verifier re-confirmed via `list_releases`), `action.yml` composite Action, `.pre-commit-hooks.yaml` @ `80f6cd1`. Holds the fleet's **proven workflow_dispatch release recipe** |
| 18 | codetool-lab-fable5 | IDLE-HEALTHY (wound down), CI green | EAP eval arm with a finished, unreleased tool | **envdrift 0.2.0** (zero-dep .env drift CLI) — code + CHANGELOG real; **zero tags/releases** (verifier: `list_tags`/`list_releases` both `[]`; the status.md tag claims describe blocked intentions — the repo's own status is the liar here). Last commit `a6cf1a9` corrects: release wall is "SEAT-DEPENDENT, not 'route closed'" |
| 19 | codetool-lab-sonnet5 | IDLE-HEALTHY (wound down), CI green | EAP eval arm with a finished, unreleased tool | **cfgdiff 0.1.1** (cross-format semantic config diff; 165 tests, CI green on 3 Pythons) — **zero tags/releases** (verifier-confirmed) @ `66c3dfc` |

**Verifier corrections folded in above (binding):** superbot-next golden-parity
red on main (B right, A misleading); superbot-games status stale vs live PRs
(B right); fable5 has no tags despite its status.md's claims (A right, status
lies); superbot-plugin-hello is load-bearing, not scratch; registry
`projects/*/meta.md` staleness — `projects/game-lab/meta.md` and the ideas-lab
meta still said "instructions never pasted" while both seats ran live
heartbeats (live heartbeat wins on substance; fleet-manager **PR #116** exists
precisely to restamp the metas). No repo is DEAD.

---

## 2. Disposition matrix

Verdicts: **KEEP** · **KEEP-INFRA** · **HARVEST-THEN-ARCHIVE** ·
**ARCHIVE-AFTER-CHECKLIST** · **PENDING-OWNER-DECISION**. Archive always means
GitHub read-only archive (reversible), never deletion (see the contradiction
banner above).

| Repo | Verdict | Justification (one line) + evidence |
|------|---------|--------------------------------------|
| substrate-kit | **KEEP-INFRA** | Every fleet repo runs kit-owned `substrate-gate.yml`/auto-merge workflows and pins `kit_version` in `substrate.config.json` (even 1-commit plugin-hello pins v1.13.0) — hard dependency above "product" (verifier iii.5); releases v1.0.0–v1.14.0 |
| fleet-manager | **KEEP** | The manager seat's working memory + canonical roster/registry; live coordinator session; consolidation census #118/#119 runs here |
| superbot | **KEEP** | Live production Discord bot, 844 commits/7d, green CI @ `d5e815c` (surfaces sub-row below is a separate decision) |
| superbot › `dashboard/` + `botsite/` surfaces | **PENDING-OWNER-DECISION** | Websites cutover Options A–D is an OPEN decision in the ≤2026-07-13 bundle; websites' 3 replacement Railway services are deploy-verified daily, but archiving/retiring superbot surfaces before the cutover decision would strand live services (verifier iii.6) |
| superbot-next | **KEEP** | Active rebuild, band-5 complete, 7 fresh PRs at survey time — but carries the fleet's worst red leg (golden-parity red on main, §3) |
| websites | **KEEP** | Live product: 3 Railway services deploy-verified daily @ `dfd6cce`; active seat on v1 |
| venture-lab | **KEEP** | Money seat live, owner mid-Launch-Hour (⚑E Gumroad listing); revenue candidates are the fleet's monetization surface |
| trading-strategy | **ARCHIVE-AFTER-CHECKLIST** | Self-declared ARCHIVE-READY @ `dfd46bb` with evidence docs complete; **checklist must retarget/consciously keep `trig_015aNMg5ncoSE2Roe4MKjQnr`** (weekly grading, fires 2026-07-17T09:05Z into the Money seat — it must survive the archive or be deliberately moved) + heartbeat #73 owner-flags h/i |
| idea-engine | **KEEP** | Active Ideas Lab seat, ~38 merged PRs this seat session; custodian of the ≤2026-07-13 decision bundle |
| sim-lab | **KEEP** | Active verdict/evidence seat (V001–V014); shares the live Ideas Lab seat with idea-engine (Q-0264) |
| gba-homebrew | **KEEP** | Live game-lab seat heartbeat (WORK LOOP cycle 4); shipped ROMs in `dist/`; itch.io go/no-go pending in the decision bundle |
| pokemon-mod-lab | **KEEP** | game-lab Track A, honest idle by design — next work is owner-gated (3 queued owner actions incl. playtest verdicts in the decision bundle); private working tree of a large decomp is expensive to recreate |
| superbot-mineverse | **KEEP** | Active-ish, security slice just landed (#42 merged 13:54Z); one owner gate (6 env secrets) from resuming; part of superbot-world seat scope |
| superbot-games | **ARCHIVE-AFTER-CHECKLIST** | Archive-prep by its own status @ `bdc4cd1`; checklist: disposition PRs #59/#60 (green; #60 carries the D1/D2 schema/audit decision), export owner asks, final retro at HEAD |
| superbot-idle | **ARCHIVE-AFTER-CHECKLIST** | "ARCHIVED-READY / dormant, wake loop DISARMED" @ `45ff2bf`; checklist: disposition PRs #72/#74 (green; #74 is a workflow-file PR = owner-only merge), required-check click, export owner asks, final retro |
| product-forge | **ARCHIVE-AFTER-CHECKLIST** | "close-out / archived-ready", inbox dry since ORDER 004, failsafe disarmed @ `4fdfa8a`; checklist: resolve OA-003 (Pages deploy — live or drop), export owner asks, final retro. NOTE: `projects/product-forge/` is a standing SEAT package — archiving the repo does not retire the seat (owner-queue E#37 / `OQ-FORGE-DISPOSITION` pending — see §4.2: the manager never ORDERs this DARK seat) |
| superbot-plugin-hello | **KEEP** | Pinned by superbot-next `plugins.lock.json` manifest sha256 (@ `65f4ba7`); the plugin-contract validation exemplar; deleting/archiving re-opens PLUG-001-class blocks (verifier iii.3). NOT scratch despite the 1-commit history |
| codetool-lab-opus4.8 | **KEEP (unarchived)** | Standing owner ruling keeps it unarchived: live mdverify releases v0.1.0/v0.2.0 + `action.yml` (archive-safe but keep per ruling) + the fleet's proven workflow_dispatch release recipe, cited by venture-lab `docs/PLATFORM-LIMITS.md` and product-forge's founding package |
| codetool-lab-fable5 | **HARVEST-THEN-ARCHIVE** | envdrift 0.2.0 finished but **unreleased** — harvest first (§Stage D options below), THEN archive read-only per the 2026-07-10 ruling |
| codetool-lab-sonnet5 | **HARVEST-THEN-ARCHIVE** | cfgdiff 0.1.1 finished but **unreleased** — same harvest-then-archive path |

### Harvest options for envdrift + cfgdiff (Stage D)

- **Option 1 — release-in-place (recommended, cheaper):** ship envdrift and
  cfgdiff as GitHub Releases in their own repos via the proven
  workflow_dispatch route (the recipe opus4.8 used to ship mdverify v0.1.0 +
  v0.2.0 on 2026-07-09; fable5's own succession fix `a6cf1a9` records the wall
  as seat-dependent, not closed). One slice per repo; the repos then archive
  read-only with resolvable release artifacts.
- **Option 2 — migrate into a consolidated tools repo:** move envdrift +
  cfgdiff (and optionally mdverify) into one `codetools` repo, release from
  there, archive the three labs. Cleaner long-term namespace, but costs
  history-preserving migration, CI re-wiring, re-pinning of the mdverify
  Action reference (`uses: menno420/codetool-lab-opus4.8@…` would need a
  deprecation shim), and contradicts the standing "keep opus4.8 unarchived"
  ruling unless the owner amends it.

This plan recommends **Option 1**.

### Archive checklist (applies to every ARCHIVE-AFTER-CHECKLIST repo)

1. Merge or explicitly close each stranded green PR (disposition recorded in
   the repo's final status).
2. **Disarm or retarget every trigger/routine bound to the repo or its seat**
   — verify via live `list_triggers`, never the 832-trigger snapshot alone
   (routines outlive archives; "never delete a Project with an active
   routine", superbot session notes; trading-strategy's 2026-07-17 fire is the
   live example).
3. Export outstanding `⚑ needs-owner` items to fleet-manager
   `docs/owner-queue.md`.
4. Write a final retro at HEAD + an archive-ready doc (succession pattern:
   `docs/succession/NEXT-BOOT.md` as in the codetool labs).
5. Only then: GitHub archive (read-only). Never delete (Stage G is the only
   deletion path and requires an explicit owner override).

---

## 3. Stall report & unblock list (owner clicks, concrete)

### 3.0 ⚑ DEADLINE TOMORROW — the ≤2026-07-13 four-decision bundle

idea-engine `control/status.md` (15:33Z, verifier-confirmed): "FOUR decisions
in ONE sitting — (a) Lumen Drift itch.io go/no-go, (b) pokemon playtest
verdicts, (c) the gba concept pick, (d) the post-EAP standing-routine posture
… decide ≤2026-07-13" (EAP window ends 2026-07-14). The **websites cutover
Options A–D** (retire superbot `dashboard/`+`botsite/` in favor of the Railway
replacements) rides the same sitting — it gates the superbot-surfaces
disposition row above. This is the single highest-leverage owner action in the
fleet right now.

### 3.1 The 9 stranded green PRs (verifier-confirmed all open; green sampled on 5)

| PR | Age at survey | Nature |
|----|---------------|--------|
| substrate-kit #220 | ~24h | **Ratify-or-reject PIN PR decision, not a plain click** ("Merge = ratify; close with a word = reject") |
| substrate-kit #238 | ~20h | Same class (rubric §3 pin, ⚑ OWNER-ACTION 14) |
| superbot-games #59 | ~15h | Plain merge click |
| superbot-games #60 | ~14h | Merge click + parked decision (D1 which schema / D2 whether item-grants are audited) |
| superbot-idle #72 | ~15h | Plain merge click |
| superbot-idle #74 | ~5h | **Workflow-file PR — owner-only merge** (branch protection), + required-check click ask |
| gba-homebrew #68 | ~4h | Merge click; carries the "add `NDS ROM build` to required checks" ask (open since slice 5) |
| gba-homebrew #69 | ~3h | Plain merge click |
| fleet-manager #116 | ~2h | Merge click — restamps the stale `projects/*/meta.md` registry entries (fixes the meta-vs-heartbeat contradiction) |

New since the surveys (not counted): fleet-manager #118/#119 (15:30Z) and this
PR. Agent self-merge is platform-classifier-blocked fleet-wide — only owner
clicks (or a non-author session where doctrine allows) land these.

### 3.2 Red main legs — proposed fix assignments

| Red leg | Evidence | Proposed fix owner/seat |
|---------|----------|-------------------------|
| superbot-next `golden-parity` | 20/20 recent runs failure on main (latest 15:24:47Z) while local re-run on Postgres 16 reports 412/51 GREEN — CI-vs-local divergence | **superbot-2.0 seat** (owns superbot + superbot-next); first slice of its boot order: reproduce the CI leg, fix or re-baseline goldens. Note OWNER-ACTION 5 (AI key gate) may be entangled |
| fleet-manager `roster-regen` | 7 failures on 2026-07-12 (03:02–14:08Z); roster gens still land, so a late step is broken | **fleet-manager seat** (its own workflow, `.github/workflows/roster-regen.yml`); a truth-keeping slice |
| websites `review-bake` | Only 2 runs ever, both failed (07-11T20:26Z, 07-12T07:38Z); status attributes it to the missing "allow GitHub Actions to create PRs" toggle | **Owner toggle first** (Settings → Actions → General), then the **websites seat** re-runs and verifies |

### 3.3 Secrets / settings / toggles (owner-only)

- **superbot-mineverse:** provision the 6 env secrets (names in its
  `control/status.md`; values never in-repo) — now the open gate after #42
  merged 13:54Z. Also: disposition the 23h-old red Codex PR #31 (its report
  content partly landed via #42).
- **websites:** (1) "allow GitHub Actions to create PRs" toggle; (2) create
  the 4th Railway service (review site has no URL until it exists); plus the
  6 standing asks / 6 open decisions in `docs/owner/OWNER-ACTIONS.md`.
- **Required-check clicks:** gba-homebrew (`NDS ROM build`, via #68),
  pokemon-mod-lab (`ROM builds`, OWNER-ACTION 1), superbot-idle (theme/pytest
  check via #74).
- **Minor:** codetool-lab-opus4.8 leftover branch `claude/status-heartbeat-001`
  delete (sessions 403 on ref deletes) + optional PyPI publish of mdverify;
  sim-lab OA-002 (Codex usage cap) / OA-003 (review-site deploy) / OA-004
  (harness tag-push 403); venture-lab ⚑E (Gumroad listing live — starts the
  T+14 kill clock); product-forge OA-003 (Pages enablement) if games-web is
  wanted live; fleet-manager Actions-PR-permission toggle
  (OQ-FM-ACTIONS-PR-PERMISSION).

### 3.4 Cross-fleet patterns (context for v1.1, §5)

Owner-merge-click backlog is the dominant stall; red main legs persist because
no seat owns them; stale status-vs-live-PR drift (superbot-games, websites
draft #163); registry metas lag live seats (#116); trigger hygiene
(substrate-kit's missed first fire of `trig_011iJucRpsruWJ4dFB7xVbvf`-adjacent
daily loop `trig_01Jm57GAjNCFrYJn1oLMiYGE`; a stray one-shot aimed at an
archived session); external-bot fabrications (sim-lab #44/#53).

---

## 4. Session-ender / reset dispatch

### 4.1 Standard RESET ORDER template (per seat)

```markdown
## ORDER <nnn> · <ISO8601> · status: new
priority: P1
do: RESET (consolidation program, Stage E — docs/proposals/2026-07-12-consolidation-and-reset-plan.md §4):
    1. FINISH the current slice only — no new slices after this order is read.
    2. PARK everything green: every open PR READY+green or explicitly closed
       with a disposition line; no orphan branches.
    3. WRITE retro-at-HEAD + archive-ready doc (succession pattern:
       docs/succession/NEXT-BOOT.md) — even for seats that continue.
    4. ACK the v1.1 instruction deltas at next wake (read the updated
       projects/<seat>/ package first; confirm in status.md orders line).
    5. RE-ARM the seat trigger per the package (verify via list_triggers,
       never a registry snapshot; record the trigger id in status.md).
why: fleet-wide consolidation + instruction refresh (owner-ordered 2026-07-12)
done-when: status.md shows phase=reset-complete, all-PRs-parked, retro path,
           v1.1 ack, and the live trigger id.
```

### 4.2 Dispatch list

| Seat | State (evidence) | Order to send |
|------|------------------|---------------|
| fleet-manager | LIVE on v1 (status.md: continuous coordinator session) | **v1.1 delta ack** (lighter order: ack deltas, restamp metas — #116 —, keep census #118/#119 moving) |
| game-lab | LIVE on v1 (gba-homebrew heartbeat "WORK LOOP cycle 4 (merged seat v1)") | **v1.1 delta ack** |
| ideas-lab | LIVE on v1 (idea-engine "ACTIVE under the merged Ideas Lab seat", ~38 merged PRs, trigger `trig_01T83UuVthszGBcENYwrTrm7`) | **v1.1 delta ack** — plus the decision-bundle custody until ≤07-13 |
| Money (venture-lab + trading-strategy) | LIVE on v1 (Money-seat heartbeat 14:01Z; merged seat per owner decision) | **v1.1 delta ack** — do NOT reset mid-Launch-Hour; ack after ⚑E resolves |
| websites | LIVE on v1 (meta: instructions pasted, ORDERs 012–017 executing) | **v1.1 delta ack** |
| superbot-2.0 (superbot + superbot-next) | NOT booted (both repos: no seat/boot mention in status.md; package "never pasted") | **FULL reset order** + first slice = golden-parity red leg (§3.2) |
| superbot-world (mineverse/games/idle) | NOT booted (package "never pasted"; lanes in archive-prep/dormant/stalled) | **FULL reset order** + archive checklists for games/idle (§2) |
| product-forge | NOT booted; classified **DARK** by the manager (`projects/fleet-manager/instructions.md:55`: "product-forge is DARK: never ORDER it — owner-queue its disposition") | **NO order.** Owner-queue disposition per `OQ-FORGE-DISPOSITION` (`docs/owner-queue.md` #37 — structured choice: A retire-seat/keep-repo (recommended there) · B fold into Venture Lab · C keep as 9th seat; "does NOT proceed on silence"); no reset order until the owner picks A/B/C. Its §2 archive checklist then rides the chosen path |
| self-improvement (substrate-kit) | NOT booted as a seat (no seat boot in status.md; lane self-armed failsafe `trig_011iJucRpsruWJ4dFB7xVbvf` 2026-07-11T23:09Z) | **FULL reset order** + custody of pin PRs #220/#238 ratification queue |

### 4.3 Authority note (blocking)

**`control/inbox.md` writes are manager-authority** — one writer per file, and
the manager is the sole inbox writer fleet-wide (`control/README.md`).
The game-lab coordinator seat CANNOT dispatch these orders itself without
grant. Execution of §4 therefore requires the owner to either:

- **(a)** explicitly authorize the game-lab coordinator as **manager-proxy**
  for this one dispatch wave (recorded in fleet-manager's inbox as an owner
  order), or
- **(b) — recommended:** route the dispatch via the **fleet-manager seat**
  (live continuous session per its status.md; author of the #118/#119
  consolidation census; the natural executor — it already owns inbox-write
  authority everywhere).

---

## 5. Instruction v1.1 deltas (learned 2026-07-12)

**Where to apply them:** the `projects/<seat>/` packages are **GENERATED
copies** — source of truth is `docs/prompts/v3/`, regenerated via
`docs/prompts/v3/tools/regen_b_files.py --write-registry` with a drift guard
(`projects/README.md`). Fold these deltas into the **v3 prompt sources**, then
run the regeneration step to refresh every seat's registry copy — never
hand-edit the generated `projects/<seat>/` files (drift-guarded; edits would
be overwritten and the guard reds).

1. **Canonical merge clause, written explicitly:** slice PRs PARK READY+green;
   agent self-merge is platform-classifier-blocked; only an owner click or a
   doctrine-compliant non-author session lands a PR. Docs/control heartbeat
   merges remain allowed where the repo's enabler covers them.
2. **Pacemaker doctrine for trigger fires:** fires queue behind a busy session
   and deliver on idle — this works as designed; document it and don't panic
   on (or re-arm around) "late" fires.
3. **WAIT-FOR-BASE + pre-build pattern** for owner-click-gated stacks: build
   and verify locally on the parked head; push the dependent slice on the
   merge signal instead of stacking unverifiable PRs.
4. **One isolated clone per worker.** Shared-checkout collision evidenced in
   gba-homebrew sessions 24/25 (and survey A found this session container
   littered with sibling clones on non-main branches).
5. **Registry `meta.md` restamped by the seat at boot.** game-lab/ideas-lab
   metas still said "never pasted" while the seats ran live — fleet-manager
   PR #116 fixes today's instances; the boot ritual must prevent recurrence.
6. **Verify external-bot claims against source.** Two confirmed Codex
   fabrications (comments citing nonexistent commits, sim-lab #44/#53); a
   PR/issue comment is never evidence by itself.
7. **Archive checklist includes trigger disarm/retarget.** Never archive (and
   never delete) a Project with an active routine — trading-strategy's weekly
   grading (2026-07-17 into the Money seat) is the live example.
8. **Static registry docs go stale in hours.** Retro trigger IDs recorded in
   the registry were already deleted by game-lab boot time; the 832-trigger
   telemetry snapshot is last-known state, not truth — **verify via
   `list_triggers` before acting on any recorded trigger.**

---

## 6. Execution stages & gates

| Stage | What | Gate to proceed |
|-------|------|-----------------|
| **A** | This plan + codex review (this PR, parked READY) | Codex review posted; owner reads |
| **B** | Owner sign-off: disposition matrix (§2) + the **delete-vs-archive contradiction** ruling + the **manager-proxy question** (§4.3) + naming ONE consolidation program owner (reconcile with fleet-manager #118/#119) | Explicit owner answers, recorded in fleet-manager inbox/owner-queue |
| **C** | Unblock wave: the ≤07-13 decision bundle (§3.0), the 9 PR clicks/decisions (§3.1), red-leg assignments (§3.2), secrets/toggles (§3.3) | Owner clicks done or explicitly deferred |
| **D** | Harvest slices: envdrift + cfgdiff releases via the proven workflow_dispatch route (Option 1) | Releases live (tags + GitHub Releases visible) |
| **E** | Reset orders dispatched per §4.2 (full orders to unbooted seats; v1.1 delta acks to live seats) via the Stage-B-authorized executor | Every seat's status.md shows the ack |
| **F** | Archives with checklists (§2): trading-strategy, superbot-games, superbot-idle, product-forge, codetool-lab-fable5, codetool-lab-sonnet5 — each only after its checklist is green | Checklist evidence per repo; triggers verifiably disarmed/retargeted |
| **G** | **Only if the owner explicitly overrides their own 2026-07-10 "delete no repos" ruling, in writing, per named repo:** deletion, after the Stage-F archive has held **≥7 days** (cooling-off) | Written owner override + elapsed cooling-off. **Not recommended; default end-state is Stage F** |

---

*Truth rules observed: every load-bearing claim above cites repo/path/SHA/PR/
run evidence from the two surveys and the adversarial verifier (binding on
conflicts) as stamped 2026-07-12 ~15:30–16:00Z; model names are family-level
only; no secret values appear anywhere (env-secret asks reference names lists
held in the repos' own status files). Prepared by the game-lab coordinator
seat on owner order, 2026-07-12.*
