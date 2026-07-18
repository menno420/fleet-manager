# Owner queue

> **Status:** `living-ledger` — the ONE deduplicated list of things waiting on the owner.
> **Slimmed 2026-07-17.** The pre-cleanup ~68-slug queue is preserved in git history and in
> the **Resolved / Archive** sections below; this rewrite keeps only the **genuinely-open**
> owner asks, a **closed / no-action** index (ids kept — nothing lost), and the historical
> resolved log. Item ids are stable `OQ-` slugs (content-derived): an item keeps its slug
> through rewrites and its move to Resolved.

## Context

The paste-ready immediate action list is
[owner-actions-2026-07-17.md](owner-actions-2026-07-17.md), and the manager's task set is
[NEXT-TASKS.md](NEXT-TASKS.md). Full prior detail for any item below lives in git history
(pre-cleanup owner-queue) and in each item's original body. Historical lineage of the gen-2
launch that seeded the earliest queue items: [`launch-readiness-2026-07-10.md`](launch-readiness-2026-07-10.md).

---

## Active — genuinely-open owner asks

### (A) GitHub merges — one click each
**EMPTY (this repo)** — 0 open PRs in fleet-manager. Any remaining fleet-wide merges/ready-flips
live in [owner-actions-2026-07-17.md](owner-actions-2026-07-17.md), not here. The one cross-repo
disposition still open is:

- **`OQ-GBA-DRAFT-PILE` — gba-homebrew: dispose the 13 open born-red PRs (cross-repo).**
  WHAT: flip the **3 non-draft** born-red PRs (#154 / #165 / #176) to **ready** — each then
  auto-lands on green (lane-side, no owner click needed) — and decide **consolidate-or-close**
  on the **10 drafts** (#157–#164, #177, #178), which are draft + in-progress card and so
  **cannot** auto-land (draft PRs never trigger the landing workflow).
  WHERE: gba-homebrew → open PRs (https://github.com/menno420/gba-homebrew/pulls).
  WHY: draft PRs never fire the landing workflow; the pile is accumulating >24h.
  UNBLOCKS: the Underroot / brineward arc slices.
  VERIFY: the 13 resolve to landed-or-closed.
  RISK: ✅ reversible. (Cross-ref the parked-arc triage note — fleet-triage 2026-07-17
  "gba main gate repaired" + the 2026-07-18 overnight sweep.)

- **`OQ-POKEMON-98-WORKFLOW-MERGE` — pokemon-mod-lab: merge #98 (workflow-touching carve-out).**
  WHAT: merge [pokemon-mod-lab #98](https://github.com/menno420/pokemon-mod-lab/pull/98)
  "Reconcile QoL patch count to 16 + add CI drift guard" (squash).
  WHERE: https://github.com/menno420/pokemon-mod-lab/pull/98 → "Merge pull request".
  WHY: the diff touches `.github/workflows/rom-builds.yml`, and `merge-on-green.yml` skips
  workflow-file diffs (its GITHUB_TOKEN can't merge `.github/workflows/**` changes), so the PR
  does **not** auto-land — landing needs an owner merge click (or an agent MCP/REST merge). Not
  an agent-capability wall; a carve-out of the one landing workflow.
  UNBLOCKS: the QoL-count CI drift guard (reds any PR whose living docs disagree with `qol.h`).
  VERIFY: PR is green (`mergeable_state: clean`, verified live 2026-07-18) + touches
  `.github/workflows/rom-builds.yml`.
  RISK: ✅ reversible. Provenance: hub PR sweep 2026-07-18. RECORD-ONLY — do not close.
- **`OQ-FORGE-29-WORKFLOW-MERGE` — product-forge: merge #29 (workflow-touching carve-out).**
  WHAT: merge [product-forge #29](https://github.com/menno420/product-forge/pull/29)
  "phone-controller: Gradle CI lane for the Android verdict port" (squash).
  WHERE: https://github.com/menno420/product-forge/pull/29 → "Merge pull request".
  WHY: the PR **adds** `.github/workflows/android-ci.yml` (self-flagged ⚑ OWNER-ACTION), and
  `merge-on-green.yml` skips workflow-file diffs (its GITHUB_TOKEN can't merge
  `.github/workflows/**` changes), so it does **not** auto-land — landing needs an owner merge
  click (or an agent MCP/REST merge). The companion code PR (no workflow file) already
  auto-merged normally, proving the split works.
  UNBLOCKS: green CI on future `products/phone-controller/android/**` changes (unit-tests the
  SDK-free Kotlin verdict port so it can't drift from the Python core).
  VERIFY: PR is green (`mergeable_state: clean`, verified live 2026-07-18) + adds
  `.github/workflows/android-ci.yml`.
  RISK: ✅ reversible. Provenance: hub PR sweep 2026-07-18. RECORD-ONLY — do not close.

### (B) Secrets & GitHub settings (owner-only walls)

- **`OQ-FM-ROSTER-READ-PAT` — `ROSTER_READ_TOKEN` secret.** Create a fine-grained READ-ONLY PAT
  (repo access: **pokemon-mod-lab only**, Contents:read) at
  https://github.com/settings/personal-access-tokens/new, save it as a fleet-manager Actions
  secret `ROSTER_READ_TOKEN` (https://github.com/menno420/fleet-manager/settings/secrets/actions).
  UNBLOCKS: honest pokemon-mod-lab roster rows. ✅ read-only, revocable.
  **Conditional** — only needed **if roster autogen is retained** (currently under the sizing
  review; see NEXT-TASKS.md). Until created, the private lane row degrades honestly to
  UNREADABLE (never false-DEAD).
- **`BAKE_PAT` (websites repo — cross-repo).** A `menno420/websites` Actions secret whose absence
  blocks the websites nightly fleet-data bake / #380-class auto-merge. **Not a fleet-manager
  secret** — listed here only because owner-actions-2026-07-17 §6/D4 references it. Provision on
  the websites repo if the bake is wanted.
- **`OQ-POKEMON-ROM-REQUIRED-CHECK` — pokemon-mod-lab: add required check `ROM builds`.**
  https://github.com/menno420/pokemon-mod-lab/settings/rules → main ruleset → Require status
  checks → add context `ROM builds` (keep substrate-gate). Closes a live gate hole (a red ROM
  build can merge today). Pair with the protect-main item below.
- **`OQ-POKEMON-PROTECT-MAIN` — protect pokemon-mod-lab `main`** (the fleet's only unprotected
  default branch). Settings → Rules → Rulesets → new ruleset on `main` (match what websites has).
  ↩️ reversible. Do at the same sitting as the ROM required-check.
- **`OQ-NEXT-MERGE-QUEUE` — superbot-next: enable merge queue OR drop require-up-to-date** for
  `docs/**` + `control/**`. https://github.com/menno420/superbot-next/settings/rules → main
  ruleset. Kills the update-branch dance on the 6-check ruleset. Not-blocking; chronic time sink.
- **`OQ-KIT-P10-REQUIRED-CHECKS` — substrate-kit: swap required checks to `kit-quality`,
  up-to-date OFF.** Settings → Rules → main ruleset: remove "Kit test suite" + "Cold-adoption
  smoke", add `kit-quality`; set "Require branches up to date" OFF. Retires the legacy alias jobs.
- **`OQ-GBA-ROM-RULESET` — gba-homebrew: make `ROM builds` a required check via a RULESET on
  `main`** (rulesets are token-readable; classic protection reads 403 for GITHUB_TOKEN, so the
  enabler can't see the context otherwise). Settings → Rules → Rulesets → target `main` → require
  `ROM builds`. Lets gba PRs self-land.
### (C) Product / external (cross-repo, owner-only — real accounts/keys)

- **`OQ-VENTURE-STRIPE-KEYS` — venture-lab: Stripe TEST keys.** Paste `sk_test_…`
  (`STRIPE_SECRET_KEY`) + `whsec_…` (`STRIPE_WEBHOOK_SECRET`) into
  `candidates/membership-kit/server/.env` (never committed). Unblocks the only unverified leg of
  the payment path for all 3 products.
- **`OQ-VENTURE-PUBLISH-CLICKS` — venture-lab: publish 3 products** (membership-kit $49 ·
  template-packs $19 PWYW · stripe-webhook-test-kit $29) on gumroad.com; per-product scripts in
  `docs/launch/**/owner-actions.md`. Unblocks the first-revenue path.
- **`OQ-VENTURE-GOTCHA-ARTICLE` — venture-lab: publish the Stripe-webhook gotcha article**
  (`docs/launch/stripe-webhook-test-kit/gotcha-article.md`) on Dev.to/Hashnode. Starts the 14-day
  validation clock candidates #4/#5 wait on.
- **`OQ-WEBSITES-RAILWAY-POSTGRES` — websites: add Railway PostgreSQL** to project
  superbot-websites, copy `DATABASE_URL` into service **botsite**. Unblocks public `/submit`.
- **`OQ-WEBSITES-PAT` — websites: fine-grained PAT** (contents+actions read; actions:write) as
  `GITHUB_TOKEN` on railway.app → superbot-websites → control-plane → Variables. Lifts the 60/h
  anonymous rate limit across every fleet surface.
- **`OQ-GBA-LUMEN-RELEASE` — gba-homebrew: create the Lumen Drift GitHub Release.**
  https://github.com/menno420/gba-homebrew/releases/new → tag `lumen-drift-v1.3` (target main) →
  attach `dist/lumen-drift.gba` (sha256 in `docs/PLATFORM-LIMITS`-noted value) → notes →
  `docs/PLAYING.md`. Agent tag-push is 403-walled. Gives a downloadable player artifact.

### (D) Standing decisions

- **`OQ-FM-APPARATUS-SIZING` — right-size fleet-manager's own apparatus (NEXT-TASKS item 3).**
  WHAT: Decide which fleet-manager self-apparatus workflows/docs to **KEEP** vs **RETIRE/right-size**
  now that the fleet is a smaller set — a right-sizing pass on the self-apparatus.
  WHERE: `.github/workflows/**` (`merge-on-green.yml`, `substrate-gate.yml`, `roster-freshness.yml`,
  `roster-regen.yml`) + the `control/` message-bus (`inbox.md`/`outbox.md`/`status.md`) + the
  roster/telemetry autogen (`docs/roster.md`, `telemetry/triggers-snapshot.json`,
  `telemetry/model-usage.jsonl`) in this repo.
  HOW / recommendation (per actual workflow — a verdict each):
  - **KEEP `merge-on-green.yml`** — the repo's server-side backstop lander (verify-then-squash-merge);
    a useful belt-and-suspenders enabler even though agents also merge their own green PRs directly
    (MCP/REST `merge_pull_request`, fm #308/#309). Do not touch.
  - **KEEP `substrate-gate.yml`** — kit-owned merge gate (session-card / hygiene hold); load-bearing,
    regenerated by `bootstrap.py` on upgrade, never hand-retire.
  - **KEEP `roster-freshness.yml`** — the roster-freshness PR gate (fails a PR on a stale roster
    stamp); cheap, advisory-shaped, keeps the roster honest if regen is retained.
  - **KEEP the three new advisory checkers (S3/S5/S9)** — `scripts/check_owner_queue.py` /
    `check_roster_freshness.py` / `check_docs_links.py` and the S3/S5/S9 drift/staleness checkers;
    stdlib-only, zero coupling to the retired autonomous apparatus, load-bearing for records hygiene.
  - **HOLD / right-size `roster-regen.yml`** — the heaviest self-poll autogen (cron `40 */2 * * *`,
    every 2h → ~12 roster regens/day). A smaller fleet does not need 2-hourly regeneration.
    **Recommended: reduce the cadence** (e.g. daily `40 6 * * *`, keeping `workflow_dispatch` for
    on-demand) rather than delete — reversible, keeps the regen path alive. Delete only if the roster
    itself is retired.
  - **HOLD `control/` message-bus + `telemetry/` snapshots** — the ORDER relay is already retired
    (`control/inbox.md` is historical); keep the files as history, retire only the (now-absent)
    autogen that wrote them. No live workflow regenerates them, so no action beyond leaving them
    historical — revisit only if a real multi-seat fleet returns.
  WHY: the fleet is smaller now; the ORDER-relay + roster autogen was built for the full fleet and
  is over-built for a smaller one. Keep the load-bearing merge/gate/checker
  path; trim the over-built self-poll autogen.
  UNBLOCKS: a lean, intentional manager apparatus; less autogen noise (fewer roster-regen
  runs/PRs) without losing the landing path.
  VERIFY: after execution, the kept workflows (`merge-on-green` / `substrate-gate` /
  `roster-freshness`) still run + green; the reduced `roster-regen` fires on its slower cadence (or
  on `workflow_dispatch`) and the roster stamp stays inside `roster-freshness`'s threshold.
  RISK: ⚠️ — EXECUTION touches `.github/workflows/**` (hub-venue / owner-side, classifier-gated for
  agents); the **RECORD here is ✅ reversible**. Do not self-execute — the cadence edit / any retire
  is an owner/hub-venue action. *(Conditional cross-ref: `OQ-FM-ROSTER-READ-PAT` is only needed if
  roster autogen is retained; a `roster-regen` retire would moot it.)*
- **`OQ-FM-ROSTER-CRON-RELIABILITY` — watch GitHub's scheduler reliability for `roster-regen.yml`.**
  WHAT: watch whether GitHub Actions keeps dropping `roster-regen.yml`'s scheduled cron windows; if
  drops recur (first drop observed 2026-07-18 → roster lapsed to **4.0h** stale before a
  `workflow_dispatch` fix landed Gen #86 / PR #302), migrate roster-freshness to a dedicated **CCR
  routine** (the workflow header documents this fallback).
  WHERE: `.github/workflows/roster-regen.yml` cron (`40 */2`) + a possible CCR routine.
  WHY: GitHub silently drops scheduled cron windows under load; the 2h cadence has no margin against a
  single dropped window before the 4h staleness bar.
  UNBLOCKS: reliable roster freshness without manual dispatch.
  VERIFY: scheduled runs land on cadence / the roster stays <4h stale without manual intervention.
  RISK: ✅ — watch/record only; any migration is an owner/hub-venue action.
- **`OQ-CONSOLIDATION-DELETE-VS-ARCHIVE` — delete vs archive (the repo-consolidation gate).** Two
  of your own instructions contradict ("delete no repos — they are the fleet's memory" vs "delete
  the test repos"); one letter resolves it. **Recommended A** — harvest → archive (read-only),
  delete NOTHING (reversible, honors the standing ruling, still removes repos from the active
  roster). B — deletion, as an explicit written override, per repo, after ≥7-day cooling-off. This
  gates the archive clicks (`OQ-CONSOLIDATION-ARCHIVE-{FORGE,SONNET5,FABLE5}`) and the release
  decisions (`OQ-CFGDIFF-RELEASE-DECISION`, `OQ-ENVDRIFT-RELEASE-DECISION`). Plan:
  [`planning/2026-07-12-repo-consolidation-plan.md`](planning/2026-07-12-repo-consolidation-plan.md).
  *(Re-evaluate scope: fewer live repos may make the whole program moot.)*
- **`OQ-RAILWAY-PROJECT-SPLIT` — websites Railway duplication.** Services exist in BOTH
  `reliable-grace` (live) and `superbot-websites` (parallel copy). Decide the canonical home; the
  Anthropic email links the reliable-grace URLs, so **keep them reachable** while that reference
  stands, then consolidate into `superbot-websites` and retire the duplicates. A drift hazard
  while both deploy.
- **`OQ-CR-SLICER-ANSWER` — curious-research: which slicer do you use?** One word (Cura /
  PrusaSlicer / OrcaSlicer / Bambu Studio). Unblocks that seat's menu-clicks follow-up guide.

### (E) Objection-only / parked (no click unless vetoing)

- `OQ-GAMES-S5-LATE-VETO` — games §5 late-veto, silence=proceed already operating.
- `OQ-R6-MOBILE-LAB-VETO` — ORDER 018 R6 mobile-lab decision, open indefinitely; veto = strike it.
- `OQ-TRADING-OOS-OPTIN` — trading OOS protocol is OPT-IN, never self-executes; file an ORDER only
  if wanted.
- `OQ-STANDING-OBJECTION-NOTES` — kit P4 daily loop self-armed · kit releases cut agent-side ·
  superbot-next D-0064–D-0069 decide-and-flag. Veto any by saying so.

### (F) Seat design decisions — deferred to the seats

These are genuine product/design forks the **SuperBot World / SuperBot 2.0 seats**
inherit; no owner click is blocking now.
- `OQ-IDLE-GENERATOR-PURCHASE` — superbot-idle: add the missing generator-purchase growth verb
  (rec A: geometric cost curve, SIM-pinned).
- `OQ-IDLE-CONTENT-DEPTH` — superbot-idle: depth direction after the upgrade→prestige spine
  (rec A: timed-events scoping).
- `OQ-NEXT-CURATION-RATIFICATIONS` — superbot-next: one-pass ratify the DROP-list (60) +
  settings-prune + D-0083 anchor (reversible pre-cutover, Q-0241 lane).
- **`OQ-IDEA-ROUTING-OWNER-ONLY` — Ideas-Lab items that are owner-only (not auto-routable).**
  The verified 2026-07-18 idea-routing pass
  ([idea-routing-2026-07-18.md](idea-routing-2026-07-18.md)) routed the buildable candidates
  (A–H) to their target lanes; these remaining Ideas-Lab items need an owner decision/action
  and cannot be auto-routed: **V011** review-service deploy · **venture-lab money-gated** items
  (×11, real accounts/keys) · **makerbench** · **trading** (owner-by-design) · **Ideas-Lab
  seat revival**. No agent click lands these — record-only until the owner acts. RISK: ✅.

### (G) Hygiene (whenever — cosmetic, all agent-403-walled)

- Stale-branch deletes: websites ×4 (`claude/harden-verify`, `claude/rework-dashboard`,
  `claude/wire-github-token-docs`, `manager/control-plant`) · gba `claude/brineward-wind` ·
  pokemon-mod-lab `track-a/session-019`, `track-a/session-024`, `claude/eloquent-newton-qaf1ii` ·
  fleet-manager `claude/consolidation-plan-v34`. (`OQ-WEBSITES-STALE-BRANCHES`,
  `OQ-STALE-BRANCH-DELETES-0713`.)
- Spent-chat archive in claude.ai (dead trading gen-1 session, wound-down gen-1 lane chats).
- Release clicks gated on `OQ-CONSOLIDATION-DELETE-VS-ARCHIVE=A`: cfgdiff v0.1.1
  (codetool-lab-sonnet5) · envdrift v0.1.0/v0.2.0 (codetool-lab-fable5) tag+Release before archive.

---

## Closed / no action — ids kept

These once-active items are moot; ids retained so nothing is lost, full bodies in git history.

- **Restructure / trigger-cutover / env re-paste** — superseded; the fleet was not restructured:
  `OQ-RESTRUCTURE-PROJECTS`, `OQ-RESTRUCTURE-INSTRUCTIONS-PASTE`,
  `OQ-RESTRUCTURE-TRIGGER-CUTOVER`, `OQ-ENV-SETUP-REPASTE`, `OQ-PASTE-WAVE`.
  Superseded by [project-recreation-runbook.md](project-recreation-runbook.md).
- **DARK-seat re-wakes** — not re-woken: `OQ-GAMES-DARK-REWAKE-OR-REASSIGN`,
  `OQ-GBA-DARK-REWAKE`, `OQ-FORGE-DARK-NO-ACTION-CONFIRM`, `OQ-KIT-SUBROWS-WINDDOWN-CONFIRM`,
  `OQ-GAMES-S5` re-wakes.
- **Apparatus cron trims** — folded into the apparatus sizing decision (`OQ-FM-APPARATUS-SIZING`):
  `OQ-SUPERBOT-CRON-TRIM`, `OQ-WEBSITES-FM-CRON-TRIM`.
- **Fleet-wide doctrine rulings** — moot: `OQ-HEARTBEAT-DOCTRINE-RULING`,
  `OQ-CODEX-GATE-VS-SUSPEND-RULING`.
- **Overnight dispatch** — superseded: `OQ-THIN-LANE-DISPATCH-2026-07-16`
  (remaining legs were classifier-walled).
- **Time-boxed / window-expired** — deadlines passed: `OQ-TRADING-0717-DOUBLE-GRADING-FIRE`
  (before 2026-07-17 09:00Z; impact ~zero — grade_paper is a no-op until ~August),
  `OQ-SITTING-0714-DECISIONS` (2026-07-14 window closed; any live game/product sub-decisions —
  playtest verdicts, gba Track B, websites cutover — carry forward via the active seats).
- **Mooted by consolidation** — `OQ-FORGE-SETTINGS-RESIDUE`, `OQ-FORGE-PAGES`,
  `OQ-FORGE-DISPOSITION`, `OQ-ITCH-LUMEN-PUBLISH`.
- **Seat env credentials (re-provision if the seat resumes)** — `OQ-NEXT-API-KEY`,
  `OQ-NEXT-HERMES-EGRESS-CREDS` (re-add to the superbot-next env if that lane resumes).
- **Cosmetic / optional** — `OQ-TRADING-ARCHIVE-SESSION`, `OQ-CODEX-FLAPPING` (YAML half already
  resolved; flapping-quota mitigation only).

---

## Resolved 2026-07-17 (agent-side — wake chain restored via native MCP scheduling)

- **`OQ-FM-WAKE-CHAIN-ARM` ✅ RESOLVED 2026-07-17 (agent-side; owner action no longer needed)** —
  wake chain restored agent-side via native MCP scheduling; failsafe
  `trig_01Bo7dZxM9xz2hwR36L424Z8` armed (cron `30 */2 * * *`, enabled, next 2026-07-17T22:36Z,
  coordinator-bound dead-man, persist_session:true) + pacemaker restored. The earlier ask assumed
  a hard wall that was actually the Bash-fallback path + a nondeterministic classifier — native
  scheduling via worker ToolSearch works (see `docs/CAPABILITIES.md` 2026-07-17 UPDATE). UNBLOCKED:
  I4 MANAGER-FAILSAFE.

## Resolved 2026-07-17 (owner execution close-out ~09:17–10:19Z; swept fm PR #281 — state read live per-PR via the GitHub API, Q-0120)

*The 2026-07-16 PR-landing-audit trio, executed by the owner as owner-actions-2026-07-17 §1–§3 this morning. Each PR state below was re-verified live via `get_pull_request` on 2026-07-17 before this sweep.*

- **OQ-WEBSITES-359-MANUAL-MERGE ✅** *(was A#69)* — websites #359 was NOT merged by hand; it was **CLOSED-unmerged** 2026-07-17T09:23:17Z (`merged: false`, was `mergeable_state: blocked`), **superseded** by today's identical-payload bake [#380](https://github.com/menno420/websites/pull/380) which MERGED 2026-07-17T10:19:30Z (merged_by menno420, admin-override — the §5 disposition, not the original "merge #359" ask). Net: the stale-bake concern is cleared; #359 dropped, #380 carries the refresh.
- **OQ-POKEMON-87-CONFLICT-DISPOSITION ✅** *(was A#70)* — owner took **D1 rec = CLOSE** (option B): pokemon-mod-lab [#87](https://github.com/menno420/pokemon-mod-lab/pull/87) CLOSED-unmerged 2026-07-17T10:17:04Z (`merged: false`, `mergeable_state: dirty` — the real control/status.md conflict, superseded by the newer dormancy commits on main). The seat's only stuck PR is cleared; seat-dormancy record stands on main.
- **OQ-READY-FLIP-TRIO-0716 ✅** *(was A#71)* — trio disposed 2026-07-17:
  - gba-homebrew [#153](https://github.com/menno420/gba-homebrew/pull/153) **MERGED** 2026-07-17T09:17:04Z (merged_by menno420) — the DO-FIRST flip; repaired main's substrate-gate red. Its ~27 parked arc PRs still need agent rebases onto this fix (game-lab lane work — see fleet-triage 2026-07-17 note).
  - superbot-idle [#145](https://github.com/menno420/superbot-idle/pull/145) **MERGED** 2026-07-17T09:19:07Z (merged_by menno420) — control stale-claims sweep landed.
  - superbot-games [#149](https://github.com/menno420/superbot-games/pull/149) **CLOSED-unmerged** 2026-07-17T10:17:01Z (`merged: false`, was draft + `do-not-automerge`) — the D3 rec was rebase+merge, but the **owner outcome was CLOSE** (the draft mirror of idle #142 discarded; the reconcile-race guard rides the idle-side fix). Trio net: 2 merged, 1 closed.

## Resolved 2026-07-16 (maintenance wake ~01:1xZ, fm PR #253 — state read live via the GitHub API, Q-0120)

- **OQ-FM-PR227-MERGE ✅** *(was A#63)* — fleet-manager
  [#227](https://github.com/menno420/fleet-manager/pull/227) (lanes.json
  generation-parity fix + roster-regen.yml staging fix) MERGED by the owner
  (merged_by menno420) 2026-07-15T22:47:58Z, head `6d53047` — the
  workflow-diff owner-merge-only rail made this click the sole landing path
  (ORDER 047 leaves technical rails standing; the ask named the wall, not
  ratification). Flagged by this wake's `check_owner_queue.py` run
  (`merged-citation` on the cited PR) and verified live. UNBLOCKS delivered:
  `registry/lanes.json` now stages with every roster-regen cron commit
  (Gen #65 regen ran clean post-merge, roster PR #250).

## Resolved 2026-07-15 (evening oversight wake ~20:3xZ, fm PR #245 — state read live via the GitHub API, Q-0120)

- **OQ-ROLLOUT-INSTALLER-CLICKS ✅** *(was A#68; self-declared RESOLVED
  17:0xZ by fm PR #241, moved to this section by the evening wake — the
  4 `resolved-not-swept` check_owner_queue flags close with this move)* —
  the owner merged all five merge-on-green installer PRs
  2026-07-15T15:29:41–15:29:52Z (each `merged_by menno420`; workflow file
  verified at each repo's live main):
  opus4.8 [#24](https://github.com/menno420/codetool-lab-opus4.8/pull/24)
  15:29:44Z (main `61efaa9`) ·
  fable5 [#17](https://github.com/menno420/codetool-lab-fable5/pull/17)
  15:29:47Z (main `e7ca47c`) ·
  product-forge [#25](https://github.com/menno420/product-forge/pull/25)
  15:29:50Z (main `1efbb3b`) ·
  pml [#89](https://github.com/menno420/pokemon-mod-lab/pull/89)
  15:29:52Z (main `ec63823`) ·
  plugin-hello [#3](https://github.com/menno420/superbot-plugin-hello/pull/3)
  15:29:41Z (main `abd9133`).
  Since PROVEN live in **four** of five (fable5 probe #18 16:54:14Z · pml
  probe #90 15:30:22Z · opus4.8 probe #25 15:30:46Z · product-forge probe
  #26 15:30:14Z — each `merged_by github-actions[bot]`; the last two
  flipped by the evening wake). Coverage headline **18/19 — 17 PROVEN**;
  full table: fleet-triage § 2026-07-15 A#68 note + evening-wake update.
  Residual (hub-side recommendation, on the fleet-triage plugin-hello
  row, NOT an owner click): plugin-hello's automation is INERT — zero CI,
  zero check runs = NOT-ready by design; needs a minimal CI gate
  (agent-doable) or accept-as-inert.

## Resolved 2026-07-15 (queue sweep, 11:4xZ — state read live via the GitHub API, Q-0120)

- **OQ-FABLE5-PR16-MERGE ✅** *(was A#62)* — codetool-lab-fable5 #16 MERGED
  by the owner (merged_by menno420) 2026-07-15T10:54:19Z, head `ba88daa`
  (hygiene: 11 tracked `.pyc` files removed + top-level `.gitignore` added;
  ORDER 026 / consolidation ORDER P1-5). The B#42 archive click
  (OQ-CONSOLIDATION-ARCHIVE-FABLE5) is now gated only on the E#46 envdrift
  letter — its HOW line updated this sweep.

## Resolved 2026-07-12 (owner-live session — Railway/API executed directly)

- **websites `ANTHROPIC_API_KEY` ✅** — set on the LIVE review service
  (`reliable-grace`/review, serving review-production-f027; owner-approved,
  service redeployed 2026-07-12 ~16:0xZ) AND on the parallel
  `superbot-websites`/review service. The websites-order (ORDER 019) B-section
  blocker is pre-cleared; the on-site AI assistant has its key.
- **mineverse web host ✅ (the non-portal 4/6 of OQ-MINEVERSE-ENV-VARS)** —
  Railway project `superbot-mineverse` created, `web` service deployed
  read-only degraded at `https://web-production-97636.up.railway.app` (CLI
  one-shot; auto-deploy verified working same day — item 38 struck), 3 vars
  set (signing key · redirect URI · client id). Remainder split: 2 portal
  steps stay owner (item 17), the write pair stays agent-side (FLAG 2).
- **mineverse sign-in: OWNER PORTAL STEPS COMPLETE ✅ (evening, same day)** —
  the owner registered the redirect URI (proven: Discord's consent screen
  renders on /auth/login) after the OAuth-app reuse (item 17 update). The
  first live sign-in then failed at token exchange — root-caused to
  discord.com/Cloudflare 403ing urllib's default User-Agent (valid
  id+secret; curl UA 200 vs python UA 403 on the same endpoint) — fixed in
  mineverse PR #45 (UA header + server-side error logging). Nothing further
  is owner-side for sign-in; #45's merge auto-deploys and the owner retries.
- **roster-freshness BRIDGED ✅** — `fleet roster regen bridge`
  (`trig_011LrFY1k5cUHRYH6zwTvPvn`, `50 */2 * * *`, fleet-manager env,
  fresh-session) lands parked roster PRs + refreshes the triggers snapshot;
  RETIRED same day: the owner clicked the toggle and the bridge trigger was deleted after live verification (runs 29202721367, PRs #129/#131).

## Resolved 2026-07-11 (P3 curation sweep, ~20:1xZ — every state below re-verified LIVE per PR, Q-0120)

The whole (A) merge group plus the UNIVERSAL-clause trail item, all clicked by
the owner (merged_by menno420 in every case; states read live via the GitHub
API this sweep, not from reports):

- **OQ-GAMES-PR27-MERGE ✅** — superbot-games #27 MERGED 2026-07-11T14:56:05Z,
  merge `50f6774` (Q-0267 theme-readiness delta on main).
- **OQ-GAMES-PR32-MERGE ✅** — superbot-games #32 MERGED 2026-07-11T14:56:17Z,
  merge `f9c2f7a` (survival sim harness + Q-0087 bands in CI).
- **OQ-GAMES-PR38-MERGE ✅** — superbot-games #38 MERGED 2026-07-11T14:56:26Z,
  merge `2f1e7cd` (D&D story design; the story-game code lane is unblocked —
  the walking skeleton in fact already landed as games #48 → `b835f59`).
- **OQ-KIT-PR181-RATIFY ✅** — substrate-kit #181 MERGED (= ratified)
  2026-07-11T14:56:40Z, merge `f7aa633` (T5 re-scope v2; kit's own ledger
  recorded the ratification at `5d4978e`).
- **OQ-UNIVERSAL-MERGE-CLAUSE ✅** *(old items 16 → 13 — the HOT
  owner-provenance item)* — the corrected §2.4 merge-authority clause is LIVE:
  PR #76 MERGED by the owner 2026-07-11T15:26:47Z (merge `e1848ff`,
  UNIVERSAL.md v4 at both locations, cmp-verified during ORDER 017); ORDER 017
  executed fleet-wide via PR #77, MERGED by the owner 2026-07-11T18:40:12Z
  (merge `39b888a`). Trail: #47 merged 14:55:53Z (`5625e3b`,
  intent-signal-only); the §2.4 block was staged by #68 (merged 11:48:30Z,
  `c5e264f`). Successor ask: the paste wave (OQ-PASTE-WAVE) is now
  click-ready.

## Resolved 2026-07-11 (verified)

- **superbot-games #34 MERGED** 13:40:40Z (merge `5147a23`) and **#36 MERGED**
  13:40:50Z (merge `325c567`); **games ORDER-004 self-review LANDED** (games
  PR #47 → main `201f8dd`, 13:41:25Z). The "5 parked PRs" item is now the 3
  merge clicks at A#1–3.
- **pokemon-mod-lab PRIVATE confirmed stuck** (API `private: true` + lane R22
  re-verify 14:07:05Z @`f69ab95`).
- **kit P4 daily-loop half of old item 5 — self-armed agent-side** (kit
  self-review @`2aa7a51`); the P10 half is carried as B#10.
- **Codex hard-cap claim RETIRED → flapping** (evidence at C#20).
- **trading OOS "veto window" framing RETIRED → opt-in** (reframed at E#31).

## Parked (valid, no rush)

- **Account-wide visibility review** — all 13 repos public at the 2026-07-10
  night review; pokemon-mod-lab now private, the rest — including
  fleet-manager (this owner queue is on the open internet) — remain public.
  Decide per-repo public/private; pairs with the §4.9 repo-settings sweep.
- **superbot-next grants** — intents toggles · sacrificial Discord account ·
  capped API key (band 7); folds into the band flow (superbot-next
  `control/status.md` ⚑). *(The API-key half is now the active C#16.)*
- **websites product questions** — domains · /submit Postgres (now active
  D#24) · /admin OAuth+home · restyle · cutover (websites
  `docs/owner/OWNER-ACTIONS.md`, each with a recommended default).
- **Anthropic email pack** — the 2026-07-14 email was sent; the **next** email
  (capability self-knowledge) is drafted paste-ready at
  [anthropic-email-pack.md](anthropic-email-pack.md) — review + send on the
  existing Gmail thread. It folds in the four routines platform bugs (runs
  not inspectable · Runs-panel vs Routines-screen disagreement · arming
  seat-inconsistency · model attribution inconsistent across surfaces;
  evidence: `CAPABILITIES.md` § routine self-arm rider).
- **PyPI trusted-publishing registration** (~2 min) — token-less kit releases.
- **codetool-lab-fable5 (envdrift) v0.1.0 + v0.2.0 tags + Releases** —
  tag-push 403; owner click at Releases → Draft: v0.1.0 @ `73ef38d`, v0.2.0 @
  `13a84e5`. (Provenance of the earlier opus4.8 mislabel correction:
  `projects/codetool-lab-{fable5,opus4.8}/meta.md`; opus4.8's mdverify
  Releases are LIVE.) *(2026-07-12: the release-or-not decision is now
  ACTIVE at E#46, OQ-ENVDRIFT-RELEASE-DECISION — this stays as the click
  surface for the historical tags if E#46 = A.)*
- **codetool archive toggles ×3 (paired DECISION)** — all three repos
  `"archived": false` (API-verified 2026-07-10); recommendation: **wait until
  the gen-3 succession question settles, then archive** (archiving makes the
  repos read-only). *(2026-07-12: PROMOTED — superseded by the consolidation
  plan's sequenced clicks: sonnet5 + fable5 archive at B#41/B#42 after
  Phase 1 + E#45/E#46; opus4.8 stays UNARCHIVED (KEEP-QUIET, mdverify
  release host — per the plan it is NOT one of the three archives; the third
  is product-forge, B#40).)*
- **cfgdiff v0.1.1 release — two clicks (codetool-lab-sonnet5):** (1) PyPI
  pending publisher (owner `menno420`, repo `codetool-lab-sonnet5`, workflow
  `release.yml`, environment `pypi`); (2) `git tag -a v0.1.1 0b1eb60 && git
  push origin v0.1.1` — do NOT tag v0.1.0 at `0260aae` (predates release.yml).
  Tag push is a credential-layer 403 on that seat. *(2026-07-12: the
  release-or-not decision is now ACTIVE at E#45,
  OQ-CFGDIFF-RELEASE-DECISION — these two clicks are the HOW if E#45 = A.)*
- **Paper-doll PNG pack for mining** — art asset, whenever.

### Safe to delete / archive (housekeeping, consolidated 2026-07-10 · 18:31Z wake)

Everything here is verified spent — deleting/archiving loses nothing (all
state is committed in the repos). Do in one sitting whenever convenient.

- **Spent chats (archive in claude.ai):** OLD kit-lab coordinator chat
  (cutover VERIFIED — old trigger deleted, fresh seat live) · dead trading
  gen-1 "ORDER 001 successor" session (= C#19) · wound-down gen-1 lane chats
  generally (succession packages on main; chat context spent by design).
- **Stale branches (agent branch-delete works — 204 via the direct-token path;
  only the proxied path 403s — so these are agent-doable now, not owner-only):** codetool ×2 —
  `claude/status-heartbeat-001` (opus4.8), `test/push-check` (sonnet5) ·
  superbot-games ×2 — `mining/adopt-substrate-kit` (closed-unmerged-deliberate)
  and `mining/grid-encounters` (**verify tip is merged before deleting**) ·
  websites ×4 (= B#11).
- **fleet-manager stale branch (agent branch-delete works — 204 via the direct-token
  path; only the proxied path 403s — agent-doable now, not owner-only):**
  `claude/consolidation-plan-v34` @ 30a48fa — accidental resurrection of PR
  #122's merged head during a parallel merge-back; nothing unique on it (its
  content landed via #122's merge commit fda3182/8f92faa).
- **NOT yet safe:** codetool repo archive toggles ×3 (paired decision above);
  anything holding an open READY PR.

## Resolved 2026-07-11 (earlier — ORDER 010 relay slice)

- **Item 0 (Idea Engine Project):** seat heartbeat/repo trace landed —
  idea-engine `control/status.md` @ `835b260`, phase STEADY; roster gen #4 row
  (fm PR #59, merge `b0639a9`): failsafe `0 */2` armed, chain HOT. Retired per
  the item's own retire condition.
- **Item 9 (product-forge repo + Project), halves 1+2 — overtaken by events:**
  repo exists with the deploy workflow on main (forge PR #13, HEAD `6f5cfad`);
  seat booted and heartbeating (`control/status.md` @ `77f5231`, continuous
  mode + failsafe `0 */2`). Residue: the settings sub-click (now B#9) and
  Pages (now D#26).
- **sim-lab OA-002 (Codex integration):** Codex environments exist for ALL 12
  active fleet repos (owner update 2026-07-11 ~00:2xZ, inbox ORDER 014). Quota
  refusals are RETRY-LATER, never a wall.
  - *Reconciliation (2026-07-14, Slice 0 item 6 / INC-04 — the fm↔sim-lab
    state fork):* the two repos conflated **integration-ENABLED** (done —
    the resolution above stands) with **usage-QUOTA-capped** (still real:
    sim-lab `control/status.md` holds ⚑ OA-002 open with 6+ @codex questions
    pending on quota flaps). Split verdict: enabled = RESOLVED here;
    quota-throughput = OPEN, tracked sim-lab-side (its ledger is the write
    surface) + the flapping evidence at `OQ-CODEX-FLAPPING`. Cross-link:
    sim-lab inconsistency 4.
- **fleet-manager Codex env ask (PR #26):** resolved by the same fleet-wide
  enablement; @codex now PRIMARY on this repo's review-queue rows.
- **Games mapping item 14, Seat B repo-creation click — DONE:**
  `menno420/superbot-idle` exists (public, seeded, pushed
  2026-07-11T00:15:40Z) — the react-by-action on the §5.3 name; remaining veto
  window is E#29.

## Resolved 2026-07-10 (later additions)

- **trading-strategy PR #37 (final P5 holdout report) — MERGED by the owner
  2026-07-10T20:56:34Z** (merged_by menno420, API-verified). Program terminal
  state is ON MAIN: holdout SPENT, report FINAL, 0/13 clears significance.

## Resolved 2026-07-10 (Q-0262 owner-rulings batch, reconciled by the 18:31Z wake)

The owner answered the round-3 decision sheet wholesale (superbot router
Q-0262; routed as inbox ORDER 008 + lane orders):

- **kit F-5 ruling = Reading A** (Q-0262.1) — kit ORDER 011, executed (kit
  #127/#128; headline 1 PASS / 3 FAIL; B1 run-5 unblocked).
- **trading P5 holdout unlock = GRANTED** (Q-0262.2) — trading ORDER 008
  @ `fd5e9fe`; executed; terminal report merged (see above).
- **superbot-next flag-13 disposition = ACCEPTED** (Q-0262.3) — next ORDER
  009, applied in next #105.
- **Core seat 6 = the superbot hub Project** (policy 4) — owner may veto.
- **pokemon concept = QoL+** (Q-0262.7) — effective when the games program
  boots post-core (it since booted; QoL+ is the live concept).
- **The 8 undeployed instruction packages stay undeployed** until the gen-3
  blueprint delta lands, then re-base + deploy in one sitting (policy 3 —
  doctrine at blueprint §4; the deploy sitting is now C#15, held on B#13).
- Fleet policies folded into doctrine same day (fm PR #33): family-level model
  names ONLY (blueprint §1); kit OWNER-ACTION grammar wins by definition
  (playbook R17 rider).

## Resolved since the last rewrite (2026-07-09 → 2026-07-10 morning)

- **🚨→✅ pokemon-mod-lab flipped to PRIVATE** (URGENT item, night-review Q16)
  — done by the owner, re-verified via API; the account-wide visibility review
  moved to Parked.
- Fleet environments created — gen-2 lanes booted in them overnight.
- venture-lab + game-lab launch click-lists executed; gen-1 wind-down pasted
  and completed fleet-wide.
- Merge session done: kit #26 + #49 MERGED ~00:10Z, games #5 MERGED 00:00:58Z.
- Gen-1 wind-down prompt, external ChatGPT campaign, and Anthropic-email items
  consolidated (campaign closed with gen-1; email pack parked above).
