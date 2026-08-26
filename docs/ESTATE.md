# The estate — every repository, one line each

> **Status:** `living-ledger`
>
> **What this file is:** the estate index — the one live surface that names
> **every repository the account holds**, what each is for, its state, the
> owner vocabulary that reaches it, where its truth lives, and whether a
> Layer-2 folder exists here. It answers *"which repo owns this request, and
> what do I read next?"* — the question `docs/MAP.md` answers for this repo's
> own tree, one level up.
>
> **Canonical for nothing beyond the enumeration.** Every row is a pointer
> with one line of context; the named repo's own docs win over the row, and a
> built Layer-2 folder wins over the row's summary. Rows carry the date they
> were last verified; a dated row is *visible* staleness, which is the design
> (`repos/README.md` § Threads).
>
> **Every row now has a disposition.** Keep / archive / delete, and
> rework-vs-fresh for each keep, with a stated reason per repo:
> [`planning/2026-08-22-repo-dispositions.md`](planning/2026-08-22-repo-dispositions.md)
> (OD-18, 2026-08-22 — **keep 14 · archive 12 · delete 0**). It is a
> **EXECUTED 2026-08-23 for the nine ungated rows** (program step **R5**, fm
> #912). `MEASURED` by fresh live re-read after the run: **26 repositories, 9
> archived, 0 deleted** — `superbot-games`, `superbot-idle`,
> `superbot-mineverse`, `trading-strategy`, the three `codetool-lab-*` repos,
> `Substrate-kit-app` and `proxybench`. The three gated rows
> (`superbot-next` + `superbot-plugin-hello` on GCB-1, `product-forge` on R2)
> were **not** touched and remain unarchived. Archiving is reversible; the
> disposition reasoning is unchanged.
>
> **Baseline:** **all 28 repositories** verified against the live account,
> `MEASURED` 2026-08-26 (`GET /user/repos`). This line read *"all 27"* until then and was
> wrong for a day: `creator-kit` was created 2026-08-25 and reached no record
> here until the activity log's invisible-work sweep found it
> ([the visibility finding](findings/2026-08-26-cross-session-visibility.md) § 3).
> **That is the failure mode this file is most exposed to** — a repository born
> outside a hub session is invisible to the hub until someone counts. 26 of the
> 28 were verified
> against their own trees on **2026-08-21** by the fleet-wide review
> (fm #878, method and evidence: [`findings/2026-08-21-fleet-estate-review.md`](findings/2026-08-21-fleet-estate-review.md)),
> and the two created after it — **`spider-bot`** (2026-08-24) and
> **`creator-kit`** (2026-08-25) — verified live at registration. Re-derive the account list any time: `list_repos`
> (claude-code-remote MCP), or `GET /user/repos` over the direct-PAT path. Consistency between this
> file, `docs/repos/`, and the doc-routes is checked by
> `python3 scripts/check_estate_index.py` (advisory).

## How to use it

1. The owner names work → find the repo below (the **aliases** column carries
   his vocabulary where it differs from the repo name).
2. Read the row, then the **Layer 2** folder if one exists — *before*
   attaching anything (`repos/README.md` § The working model).
3. No folder → the row's **read first** column names the repo's own entry
   point. Public repos need a raw fetch for read-only work, not `add_repo`.

## Active — where work actually goes now

| repo | what it is · aliases | state (verified 2026-08-21) | read first (in the repo) | Layer 2 |
|---|---|---|---|---|
| `fleet-manager` | this hub — the estate's router and records home | active | `README.md` six-read order | — (its intent: [`intent.md`](intent.md)) |
| `spider-swing` | **Slingy Spider** — Android 2D physics swing game, Godot 4.7.1. The owner's evening product | **active** — build 0.45.0 vc66; signed vc64 sits on Play's internal testing track (2026-08-05); core-feel tuning is the north star | `docs/current-state.md` | [`repos/spider-swing/`](repos/spider-swing/README.md) |
| `spider-bot` | **Spider Bot** — the AI community bot of the **Slingy Spider** Discord server; the GCB plan's clean game-community repo (Python 3.12 + discord.py 2.7 + Railway worker) · "the spider bot", "the community bot" | **active** (verified 2026-08-24) — **LIVE on Railway** (`spider-bot`/`worker`; push to main auto-deploys to production, no PR gate); v0.1.0 + Phase-0 hardening 2026-08-24 (ruff + 78-test pytest harness + informational CI `quality`); tester funnel, human-only roster and AI chat running in the real server | `README.md` → `CLAUDE.md` (the 12 invariants) | [`repos/spider-bot/`](repos/spider-bot/README.md) |
| `couch-legend` | **Couch Legend** — idle stoner sim, the first Grok-prototype graduation; live on Pages · "the Lucid Chronicle" = its looks contract (#3), not a rename | **active** — the life story LANDED 2026-08-21 (#7: adopted tuning, save v2 `lifeHigh`, 18 chapters + 3 painted scenes live, § 9.6 rails re-checked); kit-seeded v1.21.0 (#5: required checks `ci` + `substrate-gate`, land-it-yourself); next: the Android/Capacitor shell (DESIGN § 7) + the owner's late-game feel pass | `docs/DESIGN.md` (binding) | [`repos/couch-legend/`](repos/couch-legend/README.md) |
| `creator-kit` | **Menno Creator Kit** — a reusable starting point for physical ideas in **FreeCAD** and spatial experiments in **Godot**, deliberately usable without coding: eight named parts driven by `freecad/dimensions.txt`, a Godot workbench scene, Windows `.cmd` launchers · "the creator kit", "the FreeCAD thing" | **active, brand new and barely recorded** — created **2026-08-25T21:14:50Z**, one seed commit, 111 files, substrate-kit v1.21.0 vendored. Its own `docs/current-state.md` is still the **unrendered kit template** (every `${...}` slot unfilled) and `.sessions/` holds no card, so **the repo cannot answer for itself yet**. `REASONED`: built on the laptop — Windows launchers and a FreeCAD library are not what a Linux container produces. **Registered 2026-08-26 (fm #947)**, the day after creation, and only because the activity log's invisible-work sweep surfaced it — see [the visibility finding](findings/2026-08-26-cross-session-visibility.md) § 3 | `README.md` | on demand |
| `websites` | estate web surfaces: control-plane · botsite · dashboard (Railway) + review (Pages static since 2026-08-20/21) | **active** — keep-bot-only cutover landed 2026-08-20/21 | `docs/decisions.md` + `.sessions/` | [`repos/websites/`](repos/websites/README.md) |
| `product-forge` | seat-era shell whose living asset is **phone-controller** — shipped Android Bluetooth-HID controller app, v0.22.0 signed releases | **active** (app thread); graduation to own repo = program step R2, next | `products/phone-controller/README.md` | [`repos/product-forge/`](repos/product-forge/README.md) |
| `superbot` | the **FROZEN** repo behind the **LIVE production Discord bot** (Railway `reliable-grace` `worker`). No root README — its entry is `docs/AGENT_ORIENTATION.md`. Hard rail: never touch worker/Postgres uninvited | **frozen behavior/UX oracle** — maintenance class only; the clean game-community successor **exists: `spider-bot`, live since 2026-08-24** (plan: [GCB](planning/2026-08-21-game-community-bot/README.md)), and this repo remains untouched | `docs/AGENT_ORIENTATION.md` → `docs/current-state.md` | [`repos/superbot/`](repos/superbot/README.md) |
| `substrate-kit` | the estate's method kit (single-file `bootstrap.py`, PL register = program law, adopter registry) · "the kit" | **infrastructure** — v1.21.0 cut 2026-08-13; its next worklist lives HERE, not in the kit | `control/status.md` → `docs/PROJECT-CLOSEOUT.md` | [`repos/substrate-kit/`](repos/substrate-kit/README.md) |
| `estate-backups` | **PRIVATE** Actions venue for Railway-Postgres work (sealed-box one-shot secrets) | **infrastructure, dormant** between owner asks; executes `OQ-BOT-DB-BTD6-PRUNE` when answered | `README.md` + the two workflows | [`repos/estate-backups/`](repos/estate-backups/README.md) |

## Paused / owner-gated — real assets, waiting on the owner

> **Four rows in this table are now archived** (2026-08-23, R5): `superbot-games`,
> `superbot-idle`, `superbot-mineverse`, `trading-strategy`. They are read-only,
> still public and still readable — the section keeps them because *paused* is
> still what they are; the archive only makes that visible from outside.

| repo | what it is · aliases | state (verified 2026-08-21) | read first (in the repo) | Layer 2 |
|---|---|---|---|---|
| `superbot-next` | the ground-up bot rebuild · "SuperBot 2.0", "the rebuild" | **complete-parked architecture donor** — 533/533 golden parity green but parity ≠ ported; the former cutover/server-first fork is resolved by the [2026-08-21 game-community plan](planning/2026-08-21-game-community-bot/README.md): clean repo after GCB-1, live `superbot` behavior oracle, this repo untouched. **That clean repo exists: `spider-bot`, live 2026-08-24** — GCB-1's repo-confirmed half is resolved; the archive gate's "no longer being harvested" half is a judgment (spider-bot's extraction ledger is still growing, though archiving blocks writes, never the reads harvesting needs). The archive stays queued R5 work for a session that takes it deliberately | `docs/PROJECT-CLOSEOUT.md` → `docs/current-state.md` | [`repos/superbot-next/`](repos/superbot-next/README.md) |
| `venture-lab` | the commerce lane · "Venture", **Stripe Webhook Test Kit**, **The Night Kiln**, **Lull/DREAMLINE**, **Ultramarine** | **paused by OD-11** (let it sit) — 1 live $29 SKU, 19 ready SKUs, 12 finished books; the repo's own closeout threads (kill clock, publish wave) are SUPERSEDED by OD-11 | `docs/PROJECT-CLOSEOUT.md` | [`repos/venture-lab/`](repos/venture-lab/README.md) |
| `shiftlife` | **PRIVATE** — ShiftLife, shift calendar for shift-working households (binnenvaart first); Expo + Hono/Postgres monorepo | **paused by OD-15** (not active) — stopped 2026-07-27: free core 7/8, reminders *delivery* unbuilt (`OQ-SHIFTLIFE-PHASE0`); `apps/api` code↔live gap standing (merges since `fe2fbbf` not deployed); Railway scope = `OQ-RAILWAY-SHIFTLIFE-SCOPE` | `docs/current-state.md` + `docs/plan-conformance.md` | on demand |
| `gba-homebrew` | original-IP GBA/NDS homebrew: **Lumen Drift** (released) · Wickroad · Brineward · Underroot + web arcade on Pages · "the GBA project" | **complete-parked** — resumes on the owner's A1/A3 pick + playtest verdicts (`OQ-GBA-NEXT-PICKS`); trap: required `NDS ROM build` check reds on cold-cache PRs (BlocksDS 1.21.1 pin unrecoverable; migration branch `claude/nds-toolchain-1-22-3` retained, gba #216 closed per D‑0017) | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `pokemon-mod-lab` | **PRIVATE** rom-hack QoL lab (Emerald): 18 toggles, byte-identical-when-off, source-only rail (R22) | **frozen** — one owner letter unblocks it (`OQ-PML-EMERALD-LETTER`); kit hop owner-held; note: free-plan private repos cannot enable branch protection (measured 403, 2026-08-21) | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `superbot-games` | the bot's game world as pure stdlib Python (mining · fishing · D&D · exploration) — README claims plugin-shipping, tree has no packaging (known drift, program R1) | **📦 ARCHIVED 2026-08-23** (R5) — was complete-parked; kit hop to v1.21.0 queued but **owner-paced** ("no adopter yet", owner 2026-08-14); bridge flip + slice-4 are owner forks | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `superbot-idle` | one idle-game engine + 21 data-only theme packs; its plugin is pinned in superbot-next's lockfile · "the idle engine" (NOT the Couch Legend idle game) | **📦 ARCHIVED 2026-08-23** (R5) — was complete-parked; kit v1.16.0, invisible to the adopter registry (missing from the kit's `fleet-repos.txt` scan roster, as is sim-lab); daily `host-main-advisory` cron still fires | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `superbot-mineverse` | staged browser dashboard over the bot's mining economy · "mineverse"; its closeout is the **SuperBot-World fleet MASTER** | **📦 ARCHIVED 2026-08-23** (R5) — was complete-parked, **off Railway 2026-08-20/21** (service+project deleted; repo stays by owner word). Its own go-live checklist is moot: the web host is gone and the bot-side WRITE PR (sb #2061) closed unmerged. Trap: its `current-state.md` baton says delete a trigger — D‑0015 forbids exactly that | `docs/PROJECT-CLOSEOUT.md` (the MASTER) | on demand |
| `idea-engine` | Ideas Lab, canonical half: 566 fleet-era idea files + the closed 4-gate math-verify loop (P261/V274) | **on-demand standing asset** (OD-4/OD-10) — at rest; resume recipe: its `PROJECT-CLOSEOUT.md` §3 (`HANDOFF.md` is the older layer) | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `sim-lab` | Ideas Lab, evidence half: the 4-gate verification seat + reusable `harness/`. NOTE: "sim-lab" now also names the *method* run inside a target repo (couch-legend did this) | **on-demand, at rest** — no closeout of its own (idea-engine's covers both); heartbeat deliberately historical; kit v1.15.0 and absent from the kit's scan roster | `README.md` + `CONVENTIONS.md` | on demand |
| `curious-research` | the parked gift workshop-notebook (3D printing, robot arm, Arduino) with a live site; shed kit machinery 2026-08-07 | **parked by owner choice** — "gets a new mission later" | `README.md` | on demand |
| `trading-strategy` | closed quant research · "trading-lab": 11 rounds / 5,940 configs / **0 promoted**, holdout SPENT | **📦 ARCHIVED 2026-08-23** (R5) — the archive decision that was open is now **taken and executed**; paper-0001 lane WATCH/FLAT | `docs/PROJECT-CLOSEOUT.md` | on demand |

## Frozen experiments & exemplars — read-only unless the owner says otherwise

> **Five rows in this table are now archived** (2026-08-23, R5): the three
> `codetool-lab-*` repos, `Substrate-kit-app` and `proxybench` — so this
> section's heading is now literally enforced by GitHub for those five, not just
> a convention. `superbot-plugin-hello` is **not** among them: it is gated with
> `superbot-next` on GCB-1 — whose repo-confirmed half resolved 2026-08-24
> (`spider-bot` exists and is live); see the `superbot-next` row for why the
> archive is still a deliberate separate step rather than a formality.

| repo | what it is · aliases | state (verified 2026-08-21) | read first | Layer 2 |
|---|---|---|---|---|
| `superbot-plugin-hello` | the plugin-contract hello-world, hash-pinned in superbot-next's lockfile. **The former "never archive" is CORRECTED 2026-08-22** — and the deciding fact is not the pin but the tree: **`superbot-next` vendors its own copy of this plugin** at `examples/superbot-plugin-hello/` (own `pyproject.toml` + `manifest.py`, measured), resolving it through an installed distribution's `sb.plugins` entry point, so the host never reaches this repo. The lockfile pin is a `manifest_hash`, not a fetchable ref, which is consistent with that. What archiving blocks is *editing* the manifest — still a two-repo change (host pin re-land or FAILED_STARTUP). Disposition: **archive, paired with `superbot-next`** | complete-parked | `README.md` | on demand |
| `codetool-lab-opus4.8` | **mdverify** — released CLI (v0.1.0 + v0.2.0 live, re-verified 2026-08-22). **Keep-unarchived is a records decision, not a technical dependency** — corrected 2026-08-22 (twice). The row first read *"stays unarchived while install URLs pin it"*, which is not a reason: an archived repo stays readable and its URLs keep resolving. The replacement then called it *"a standing OWNER ruling (2026-07-10)"*, which over-reads the source. Traced: the owner's 2026-07-10 ruling is quoted at [`planning/2026-07-12-repo-consolidation-plan.md`](planning/2026-07-12-repo-consolidation-plan.md) `:46` as **_"delete no repos (they are the fleet's memory)"_** — about **deletion**, not archiving, and **since AMENDED by OD-3 (2026-08-08)** to allow cleanup with a stated reason. The *keep-unarchived* verdict is that plan's own reconciliation (`:92`, *"Agree — standing 2026-07-10 ruling + live mdverify releases"*), carried into [`fleet-triage.md`](fleet-triage.md) `:61` via INC-03. So archiving this repo is an open call, resting on a plan verdict rather than an unamended owner instruction | **📦 ARCHIVED 2026-08-23** (R5) — **archived** per the [OD-18 table](planning/2026-08-22-repo-dispositions.md); the *keep-unarchived* line below is the traced history of that open call, now closed | `README.md` + `control/status.md` | on demand |
| `codetool-lab-fable5` | **envdrift** — finished CLI; **R3 DONE 2026-08-22**: v0.1.0@`73ef38d` + v0.2.0@`13a84e5` tagged and released (2 assets each). It had no release workflow at all, so fable5 #20 added one (`workflow_dispatch` + tag input, no PyPI job). **The PyPI name is TAKEN and not ours** — `pypi.org/pypi/envdrift` is `jainal09/envdrift` v11.0.4, a different tool (MEASURED 2026-08-22, HTTP 200). Any record saying PyPI is "one owner click away" for this repo is wrong; publishing would need a new name | **📦 ARCHIVED 2026-08-23** (R5) — R3 satisfied first; the documented git install is **measured working against the archived repo** | `control/status.md` | on demand |
| `codetool-lab-sonnet5` | **cfgdiff** — finished CLI; **R3 DONE 2026-08-22**: v0.1.1@`0b1eb60` tagged, its own `release.yml` published the Release (2 assets). Trap: its `publish-pypi` job fails on every run (no trusted publisher), so the **run reads red while the Release is intact**. `pypi.org/pypi/cfgdiff` is 404 — unpublished, name free (MEASURED 2026-08-22) | **📦 ARCHIVED 2026-08-23** (R5) — R3 satisfied first; its git install is the one **measured** post-archive (`cfgdiff 0.1.1`, exit 0) | `control/status.md` | on demand |
| `Substrate-kit-app` | a one-shot Gemini (AI Studio) experiment: "Substrate Kit Dashboard" React frontend over hardcoded demo data, committed onto a **partial v1.20.2 kit snapshot** — its README, CONSTITUTION and docs are the kit's **verbatim**, so every in-repo surface misidentifies it; copied CI reds by construction | **📦 ARCHIVED 2026-08-23** (R5) — frozen one-shot (2026-08-04, untouched since); the archive **freezes** the total self-misidentification, which is why the README now opens with a correcting notice | `metadata.json` + `package.json` (the only honest self-descriptions) | on demand |
| `proxybench` | single-file proxy benchmark, built mostly as a joke (OD-12: parked, no action) | **📦 ARCHIVED 2026-08-23** (R5) — was parked by OD-12; its stray probe issue #1 was closed first | `README.md` | none needed |

## Archive vs delete — they are NOT interchangeable for the code-tool labs

`MEASURED` 2026-08-22, and it separates two dispositions this index had been
treating as one call.

All three labs are installed **by git URL**, not from a package index —
`pipx install git+https://github.com/menno420/codetool-lab-sonnet5`, and
`envdrift @ git+https://github.com/menno420/codetool-lab-fable5` (their own
READMEs; none of the three is published under its own name — cfgdiff and
mdverify are 404 on PyPI, and the `envdrift` name belongs to someone else).

**The 2026-08-22 releases are NOT on that install path** — added after the fact,
because the row above ("archivable — R3 satisfied") invites the opposite
reading. A bare `git+https://…` URL with no `@ref` resolves to the default
branch HEAD, so the sdists and wheels R3 produced sit *beside* the documented
install command rather than serving it. `REASONED` from pip's documented ref
handling; not tested against these repos. Two consequences worth carrying:

- **R3's real value is narrower than "the tools are now released" suggests.** It
  makes each finished tool **citable and installable at a fixed version**, which
  is better memory than an untagged branch — and memory is what the no-delete
  instinct protects. It does **not** change how anyone actually installs them.
- **A release published immediately before an archive over-signals support.** A
  release reads as distribution; an archive reads as abandonment. If these are
  archived, each README wants one line saying the tool is finished and
  unmaintained, so a fresh version number does not imply active upkeep.

- **Archiving keeps every one of those installs working** — an archived
  repository stays public and clonable; only writes stop. This is the general
  rule for the whole estate: *archiving blocks writes, never reads.*
  **Sourced 2026-08-22** to GitHub's own documentation
  ([archiving-repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories)),
  which states that an archived repo's *"issues, pull requests, code, labels,
  milestones, projects, wiki, releases, commits, tags, branches, reactions,
  code scanning alerts, comments and permissions become read-only"* while it
  stays publicly visible, forkable and searchable. **The `git`-URL install is
  no longer an inference — `MEASURED` 2026-08-23, after the archive:**
  `pip install "git+https://github.com/menno420/codetool-lab-sonnet5"` into a
  clean venv **succeeded, real exit 0**, cloning the archived repo, resolving to
  default-branch HEAD (`ef3b600`), building the wheel and installing
  `cfgdiff-0.1.1`; `cfgdiff --version` then printed `cfgdiff 0.1.1`, exit 0.
  So the documented install path survives archiving, tested rather than
  reasoned. The write half was probed in the same pass and is the mirror image:
  a contents `PUT` to archived `proxybench` returned **403 — _"Repository was
  archived so is read-only."_** — while the read of the same file kept working.
  **Also `MEASURED` and it does not go the way the docs imply:** `search/code`
  coverage is *unchanged* by archiving (`repo:menno420/superbot-games mining`
  returned **292 before and 292 after**), but most of this account was never in
  that index at all — see the warning below.
- **Deleting breaks them**, silently and for anyone who has the command.

## ⚠️ `search/code` does NOT cover this account — dependency sweeps are unreliable

`MEASURED` 2026-08-23, and it is the single most load-bearing thing this pass
found, because a recorded `MEASURED` claim rests on the opposite assumption.

**Archiving is not the cause.** That was tested first and cleared: the one
archive-bound repository that *is* indexed returned **292 hits before the
archive and 292 after** (`repo:menno420/superbot-games mining`), and the
account-wide `Substrate-kit-app user:menno420` sweep returned **10 before and 10
after**. Archiving changes nothing about search, exactly as GitHub's docs say.

**The problem is that most of the account is not in the index at all**, and was
not before any archiving. One query per repository, each using a term read out
of that repository's own files:

**All 26 repositories were probed**, one query each, every search term verified
present in that repository's own files first.

- **Indexed — 7 of 26** (hits): `superbot` (3,576) · `substrate-kit` (472) ·
  `fleet-manager` (308) · `spider-swing` (308) · `superbot-games` (292) ·
  `venture-lab` (230) · `superbot-next` (79).
- **NOT indexed — 19 of 26**, zero hits for a term confirmed present in the
  tree: `superbot-idle` · `superbot-mineverse` · `trading-strategy` ·
  `codetool-lab-sonnet5` · `codetool-lab-fable5` · `codetool-lab-opus4.8` ·
  `Substrate-kit-app` · `proxybench` · `couch-legend` · `curious-research` ·
  `estate-backups` · `gba-homebrew` · `idea-engine` · `pokemon-mod-lab` ·
  `product-forge` · `shiftlife` · `sim-lab` · `superbot-plugin-hello` ·
  `websites`.

`product-forge` was re-probed after its first term turned out not to be in the
root README: `controller` and `bluetooth`, both verified present in
`products/phone-controller/README.md`, both return **0**. `superbot` has no root
README at all and is indexed anyway, so indexing does not track README presence.

**Corrected 2026-08-23, same session, on `@codex` review of fm #912.** The first
version of this note said *"only 3 of 26"* on the strength of **11** probes and
classified the untested 15 with the measured 8. That was over-claiming past the
evidence — the exact failure this file warns about elsewhere. The remaining 15
were then probed and the real number is **7 indexed / 19 not**. The conclusion
below is unchanged and, if anything, stronger.

**What this invalidates.** The `Substrate-kit-app` dependency check recorded at
[`planning/2026-08-22-repo-dispositions.md`](planning/2026-08-22-repo-dispositions.md)
§ 3 — *"account-wide `search/code?q=Substrate-kit-app+user:menno420`: 5 hits, all
in `fleet-manager`. Nothing in the other 25 repositories references it"* — is
**not supported by the method used**. A zero result from an unindexed repository
is indistinguishable from a genuine absence, and at least eight repositories are
unindexed. The conclusion may well still be true; the evidence does not
establish it.

That did **not** change the disposition, and does not need revisiting for that
purpose: `Substrate-kit-app` was archived on **value** (it is the estate's
evidence of what one Gemini one-shot produced), not on the dependency sweep, and
archiving is reversible either way. Where it *would* bite is the deletion call
the same section defers — deletion is irreversible, and it must not rest on this
method.

**The recipe, for the next sweep that matters.** Do not trust
`search/code?q=…+user:menno420` for a completeness claim about this account.
Clone-and-grep instead, or at minimum run the per-repo probe above first and
state which repositories the sweep could actually see. *Honest edge:* what is
measured is the API's returned counts, repeatably, over one session; the
underlying index-coverage rules are GitHub's and not inspectable from here.

So a lab that has served its purpose is an **archive** candidate on the R3
evidence; deletion is a separate, stronger call that costs the install path.
`Substrate-kit-app` looks like the reverse — nothing found installs it, and its
in-repo surfaces misidentify it as the kit, so archiving *freezes* that defect
where deletion removes it. **But the delete recommendation does not follow from
the evidence, corrected 2026-08-22.** "Nothing installs it" rests on the same
four-repo search that this very note says is too narrow to justify a deletion;
recommending one on it contradicted the limit in the paragraph below. **Archive
it too**, and treat deletion as a separate call once a wider dependency check
has actually run. The misidentification is already mitigated by this index and
by the two doc-routes that fire on its name — mitigation an archived repo keeps,
since those live here, not there.

**And archiving is reversible**, which removes the urgency from all of this:
GitHub's documentation states *"You can also unarchive repositories that have
been archived"*, with no stated time limit or condition. An archive that turns
out wrong is undone, so the archive/delete asymmetry is the whole decision —
archiving is a reversible tidy, deletion is not.

**Scope of this check:** the four repositories attached to that session
(`fleet-manager`, `websites`, and the two labs). No account-wide dependency
scan was run, so "nothing depends on these" is established for those four
only. **UPDATE 2026-08-22 — the account-wide scan has now run** for
`Substrate-kit-app`: `search/code?q=Substrate-kit-app+user:menno420` returns
**5 hits, all in `fleet-manager`** (this index and its doc-routes), none in
the other 25 repositories. That widens the check from 4 repos to 26 and
removes the stated blocker on the deletion question — which the
[OD-18 table](planning/2026-08-22-repo-dispositions.md) still answers
**archive**, on value rather than on dependencies. Honest edge: code search
indexes default-branch text, so a consumer outside GitHub would not appear.

## When the owner's words don't name a repo

- **"the bot"** — three candidates since 2026-08-24: the live production bot is `superbot` (frozen oracle, hard rail); `superbot-next` is the parked architecture donor; **the game-community bot is `spider-bot`** (live in the Slingy Spider server — GCB-1 resolved by creation). Slingy-Spider-server work almost certainly means `spider-bot`; say which one you mean before acting.
- **"the idle game"** — ambiguous: the *product* is `couch-legend`; the bot's
  idle *engine* is `superbot-idle`. Recent context decides; ask only if it
  genuinely could be either.
- **"the controller app"** — `product-forge` (phone-controller).
- **"the review site"** — websites' Pages export
  (menno420.github.io/websites); there is **no Railway service behind it**
  since 2026-08-20/21.
- **"backups"** — the *venue* is `estate-backups`; the *recurring bot backup*
  is a `superbot` workflow (weekly). A backup ask usually means both.
- **"the old rebuild" / "SuperBot 2.0"** — `superbot-next`.
- **"research tooling"** — usually `idea-engine`+`sim-lab` (the Ideas Lab
  pair); `curious-research` is the gift notebook; `trading-strategy` is closed
  quant research. Ask which if the context does not say.
- **"the kit"** — `substrate-kit`. The similarly named `Substrate-kit-app` is
  a frozen dashboard experiment that *masquerades* as the kit from inside.

## Cross-repo edges a router must know

- `superbot` → `spider-bot` ← `superbot-next`: the live repo is the behavior/UX oracle; the parked rebuild is the architecture donor; **`spider-bot` is the clean repository the 2026-08-21 plan called for** (created 2026-08-24). Every reuse gets a row in spider-bot's `docs/extraction-ledger.md`; neither source repo is modified, deployed, renamed, or archived by that build.
- `superbot-next` ⇐ `superbot-idle` + `superbot-plugin-hello`: plugins pinned
  by hash in its `plugins.lock.json`; games' adapters were never built (R1).
- `superbot-mineverse` closeout = the SuperBot-World fleet **MASTER**; the
  games/idle closeouts route their fleet-wide threads to it.
- `websites` serves the bot's public surfaces (botsite, dashboard) under the
  old names since W1; `review` is Pages-static.
- `couch-legend` → `product-forge`: the Android/Capacitor step reuses
  phone-controller's keystore/release rails.
- `spider-swing` + `couch-legend` → this repo's `image-prompt` /
  `asset-pipeline` / `audio-prompt` skills carry the art/audio method.
- `substrate-kit` → every adopter (registry `docs/adopters.md`, GENERATED);
  its scan roster misses `sim-lab`, `superbot-idle`, `product-forge`,
  `spider-swing` and `couch-legend` (the last two measured 2026-08-21), so
  registry-driven rollouts cannot see them.
- `shiftlife`'s product plan lives HERE
  (`planning/2026-07-24-app-plan-life-admin.md`); its Railway scope question is
  `OQ-RAILWAY-SHIFTLIFE-SCOPE`.
- `estate-backups` executes DB asks against the bot's Postgres (hard rail
  applies); its one archive so far: Release tag
  `postgres-botsite-final-2026-08-16`.
