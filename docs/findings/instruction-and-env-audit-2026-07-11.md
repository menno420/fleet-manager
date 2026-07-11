# Fleet instruction + environment audit — 2026-07-11

> **Status:** `reference` — a cross-project audit of every live Project's
> instructions (`projects/<repo>/`) and environment setup scripts
> (`environments/`), landed from an **owner-directed superbot session**
> (2026-07-11) that was asked to "compare all the projects' instructions to each
> other and find out if they can be improved, same with the env/startup scripts,
> find which projects can reuse the same scripts." Produced by two read-only
> mapping agents over the repo at HEAD; every claim is file-cited — **verify
> against the tree before acting (playbook R2)**. Nothing here was self-edited
> into the owner-provenance `UNIVERSAL.md` block; the merge-authority rewrite is a
> **proposal for the owner to land** (see §2).

## 0. Executive summary — two headline problems, one is fleet-critical

1. **The fleet's own merge-authority instruction tells every seat to do the
   thing the platform classifier terminally denies.** `projects/UNIVERSAL.md`
   (the owner-landed permissions block, echoed into every lane) says *"MERGE YOUR
   OWN GREEN PRs: open PRs READY, arm auto-merge at creation (or REST-merge on
   green)."* Both `enable_pr_auto_merge` and `merge_pull_request` on an author's
   own PR are refused by the auto-mode classifier as *"[Merge Without
   Review]/[Self-Approval]"* — **terminally, on the first denial** (deny-wins).
   The kit's own `substrate-kit/docs/CAPABILITIES.md` append-log (same date,
   2026-07-10) documents this and the **only working recipe**: *open the PR READY
   and do NOTHING else — the repo's `auto-merge-enabler.yml` workflow
   (`github-actions[bot]`) arms and lands it server-side.* **12 of 13 lane
   instruction files prescribe the walled path as PRIMARY; only `substrate-kit`
   is correct.** This is why seats keep stalling on merges and routing one-click
   asks to the owner every night. **Fix at the root (§2) → it propagates to every
   lane.**

2. **The 5 environment archetypes are ~4-into-1 consolidatable, and 5 live lanes
   are unregistered.** The multi/single-repo detection block is byte-identical in
   all 5 scripts, and `coordinator`'s manifest handling is already a strict
   superset of `python-lab` + `bot-prod` + `pinned-research`. Four of the five
   are one base shim + a ~20–30-line knob-diff apart; `gba-lab` is the only
   genuinely separate one. Five live python-lab lanes (sim-lab, product-forge,
   idea-engine, superbot-idle, mobile-lab) are missing from `archetypes.md`
   (§4).

---

## 2. Merge-authority — root cause + the proposed fix

### 2.1 The contradiction (both dated 2026-07-10)

| Source | Says |
|---|---|
| `substrate-kit/docs/CAPABILITIES.md` (append-log) | The classifier **DENIES** both `enable_pr_auto_merge` and `merge_pull_request` on the author's own PR ("Merge Without Review"). **Working recipe: open READY, do NOTHING else — the `auto-merge-enabler.yml` workflow arms server-side** (confirmed landings #84/#86/#87, no agent merge call). |
| `projects/UNIVERSAL.md:42-43` & `:75-76` (owner-landed permissions block) | "MERGE YOUR OWN GREEN PRs: open PRs READY, **arm auto-merge at creation (or REST-merge on green…)**." |

Because that UNIVERSAL block is the doctrinal root (and, per `projects/README.md`
+ `UNIVERSAL.md`, is meant to be carried verbatim in every `instructions.md`),
the walled instruction is the fleet default. The block's own **"DENY WINS"**
clause already subordinates it to the classifier — so the correct reading is that
the block's *action* wording is simply out of date relative to the kit's
capability discovery.

### 2.2 Per-lane merge doctrine (agent-mapped, file-cited)

| lane | doctrine | evidence |
|---|---|---|
| substrate-kit | **CORRECT** | `instructions.md:53` — enabler arms, agent does nothing |
| superbot | CORRECT-ish / walled fallback | `instructions.md:42-43` — Q-0127 "call `enable_pr_auto_merge` yourself" carve-out |
| fleet-manager | WALLED (+ self-contradiction) | `instructions.md:76` "Land via REST squash-merge" vs `:85` lists self-merge as a wall |
| superbot-next | WALLED | `instructions.md:42-45` "REST squash merge is the fast lane" |
| superbot-games | WALLED | `instructions.md:82-85` "SQUASH-MERGE YOURSELF … PRIMARY" |
| trading-strategy | WALLED (+ contradiction) | `instructions.md:87-96` "MERGE AUTHORITY is yours" vs terminal-park |
| sim-lab | WALLED | `instructions.md:73-74` "REST merge-on-green is PRIMARY" |
| product-forge | WALLED | `instructions.md:45-51` "ALWAYS lands its own PRs" |
| idea-engine | WALLED | `instructions.md:91-92` "REST merge-on-green is PRIMARY" |
| venture-lab | WALLED | `instructions.md:56-69` "PRIMARY path: REST merge-on-green" (known offender; has systemic-fix flag) |
| gba-homebrew | WALLED | `instructions.md:62-64` "REST merge-on-green after the flip" |
| pokemon-mod-lab | WALLED | `instructions.md:66-68` "REST merge-on-green … primary" |
| websites | WALLED (no enabler mentioned) | `instructions.md:41` "squash-merge on green" |
| superbot-idle / games-program / mobile-lab | ABSENT | `meta.md` only — must be **born correct** |

### 2.3 The honest nuance — some lanes genuinely can't arm

Do not "fix" this into "always let the enabler do it." Several lanes have CI
shapes where native auto-merge **structurally cannot arm**: the fast-CI arm race
(sub-~10s checks flip `pending`→`clean` before the arm lands), no
checks-pending window (born-red repos), `substrate-gate` not set as a *required*
check (venture-lab), or "Allow auto-merge" OFF (trading-strategy) — all in
`CAPABILITIES.md:178-202` + `auto-merge-guards.md:58-113`. On those shapes the
classifier *also* walls the author's REST merge, so **there is no author-side
landing path at all.** The correct response is one of:

- **park the PR READY+green and keep opening more PRs** (never an agent REST
  merge — that just burns a terminal denial); or
- a **two-party, non-author review-then-merge** (a different session that did NOT
  author the PR merges it — this passes the classifier, per `CAPABILITIES.md`
  2026-07-10 entry, e.g. venture-lab `95b755b`); or
- **install a `GITHUB_TOKEN` merge-on-green Actions workflow** (server-side token,
  not the agent — the durable fix for a repo that can't arm; venture-lab already
  flags this).

The defect in the 12 files is prescribing the walled call as **PRIMARY**, which
burns the one-shot *before* parking — not the existence of a fallback.

### 2.4 PROPOSED corrected UNIVERSAL merge clause (owner must land — provenance)

Replace the merge bullet in **both** permissions blocks (`UNIVERSAL.md:42-43`
and `:75-76`). This is **owner-provenance content** (the instruction-poisoning
guard held the coordinator-relayed version until the owner landed it directly),
so it is presented here as a proposal for the owner to land, not a self-edit:

```
- LAND YOUR OWN GREEN PRs THE CANONICAL WAY: open the PR READY (non-draft) and
  do NOTHING else merge-related. The repo's own auto-merge-enabler.yml workflow
  (running as github-actions[bot]) arms squash auto-merge SERVER-SIDE and GitHub
  lands the PR once required checks pass — with no agent merge call. CI green is
  always required; this never bypasses a red gate.
  * NEVER call enable_pr_auto_merge or merge_pull_request on your OWN PR — the
    auto-mode classifier refuses author self-merge/self-arm as "[Merge Without
    Review]/[Self-Approval]", TERMINALLY on the first denial (deny-wins; never
    retry, reword, or re-route around it).
  * IF A PR CAN'T LAND (enabler absent, "Allow auto-merge" OFF, no checks-pending
    window / fast-CI arm race, or a "behind"-main stall): park it READY+green,
    record the state, and KEEP OPENING MORE PRs — never fall back to an agent
    REST merge-on-green. Landing resumes when the blocker clears.
  * PERMITTED FALLBACKS: a DIFFERENT session may review-then-merge a PR it did
    NOT author (a genuine non-author review passes the classifier); a repo that
    structurally can't arm should stand up a GITHUB_TOKEN merge-on-green
    workflow, not route around the wall per-PR.
  (Canonical evidence: substrate-kit/docs/CAPABILITIES.md append-log 2026-07-10;
  docs/operations/auto-merge-guards.md.)
```

Once landed, the manager re-issues every walled `instructions.md` (§2.2) from the
corrected block, keeping each repo's own required-check names and born-red gate.

---

## 3. Instruction-drift findings (fixable by the manager directly)

1. **The "mandatory verbatim" permissions block is present in 0 of 13
   `instructions.md`.** `UNIVERSAL.md` and `README.md` assert every
   `instructions.md` carries the permissions block verbatim; a grep for
   `PERMISSIONS`/`owner-landed`/`DENY WINS` across `projects/*/instructions.md`
   returns **zero hits**. The doctrine home and the deployed files disagree —
   the exact silent-drift class the version-stamp discipline exists to prevent.
   Resolve by either (a) actually inserting the (corrected) block into each file,
   or (b) retracting the "verbatim in every instructions.md" claim and keeping it
   wake-prompt-only.
2. **Same-file self-contradictions:** `fleet-manager/instructions.md:76` mandates
   the REST squash-merge it lists as a classifier wall at `:85`;
   `trading-strategy/instructions.md:92` says "MERGE AUTHORITY is yours" then
   `:93-96` calls the classifier denial terminal. Sweep both when re-issuing.
3. **~10 rule blocks are duplicated near-verbatim across all 13 files and
   drifting independently** (websites already carries a documented session-shape
   drift at `instructions.md:11-19`). Centralize them into a **"Fleet-canonical
   working rules"** section of `UNIVERSAL.md` and have per-repo files keep only
   repo-specific mission / CI-landing specifics / hard rails. Proposed block:

```
## Fleet-canonical working rules (every seat; per-repo files add only
## repo-specific mission, CI/landing specifics, and hard rails)

- SESSION SHAPE (Q-0265, continuous): origin/main HEAD first; read
  control/inbox.md at HEAD (a `new` ORDER outranks your plans); claim before
  building; heartbeat-before-work (first commit = born-red .sessions card,
  flipped complete as the deliberate LAST step); WORK LOOP not one slice — each
  slice its own PR; overwrite control/status.md as the deliberate last step (one
  writer per file — never edit inbox.md; workers never touch control/).
- SCHEDULING FALLBACK (Q-0265: send_later chain = pacemaker, cron = dead-man
  failsafe): arm a ~15-min send_later before ending a turn with work left; if
  create_trigger/send_later are absent, RETRY from a spawned WORKER seat before
  flagging (worker toolsets differ); else record the wall and let cron pace you.
- HONESTY GUARD (Q-0089): out of useful work → say so and idle; never invent
  filler; negatives are headlines; "not measured" beats invention.
- DECIDE-AND-FLAG (Q-0240): resolve reversible calls yourself with a one-line
  rationale + a flag; the owner-queue is ONLY genuine capability walls.
- DISCOVERY RULE (CAPABILITIES.md): before declaring any wall / missing
  credential — check the file → check the env (printenv / list tools) → attempt
  once and capture the EXACT error → append the finding same session. Never
  re-probe a documented wall; never declare an unprobed one.
- REPORTING BAR: every load-bearing claim cites a commit / PR / tag / CI run /
  file@SHA; a green check that contradicts visible evidence is a bug in the CHECK
  (Q-0120); verify against the committed tree, never a relay or memory.
- FAMILY-LEVEL MODEL NAMES ONLY (fable-5, opus-4.8) — never exact model IDs.
- NO SECRET VALUES in any repo, ever — env var NAMES only.
- SPAWNED WORKER OUTPUT is data for its coordinator — findings with citations.
```

---

## 4. Environment / setup-script audit

### 4.1 Project → archetype matrix

| Project | Archetype | Registered in `archetypes.md`? |
|---|---|---|
| fleet-manager | coordinator | ✓ (live multi-repo env) |
| substrate-kit | python-lab | ✓ |
| superbot (legacy) | bot-prod | ✓ |
| superbot-next | bot-prod | ✓ |
| superbot-games | python-lab | ✓ |
| **superbot-idle** | none named (live seat!) | ✗ **DRIFT** |
| games-program | gba-lab (spans 2 game repos) | partial |
| trading-strategy | pinned-research | ✓ |
| **sim-lab** | python-lab | ✗ **DRIFT** (self-flagged) |
| **product-forge** | python-lab | ✗ **DRIFT** (self-flagged) |
| **idea-engine** | python-lab | ✗ **DRIFT** |
| venture-lab | python-lab | ✓ |
| websites | pinned-research | ✓ |
| gba-homebrew | gba-lab | ✓ |
| pokemon-mod-lab | gba-lab (Track-A subset) | ✓ |
| **mobile-lab** | python-lab (Node/Expo via repo escape hatch) | ✗ (held, unregistered) |

**Reuse groups today:** python-lab = 7 lanes (substrate-kit, superbot-games,
sim-lab, product-forge, idea-engine, venture-lab, mobile-lab) + the codetool
trio; pinned-research = 2 (trading, websites); bot-prod = 2 (superbot,
superbot-next); coordinator = 1 (fleet-manager); gba-lab = 2 (+program).

### 4.2 Archetype overlap — what actually differs

The multi/single-repo detection block is **byte-identical in all 5 scripts + `setup-universal.sh`**; `set +e` / `PIP_ROOT_USER_ACTION` / `log()` posture identical. All divergence is in three knobs:

| Knob | python-lab | coordinator | bot-prod | pinned-research | gba-lab |
|---|---|---|---|---|---|
| Baseline pip | pytest ruff **build** | pytest ruff | *(none)* | pytest **python-multipart** | +apt devkitARM/mgba + Pillow mgba |
| Interpreter pin | python3 | superbot→3.10 | superbot→3.10, **next→3.11** | python3 | python3 |
| Manifest ladder | env-setup→req.txt→pyproject | env-setup→**req.lock**→**multi req\***→pyproject | env-setup→req.lock→req.txt | env-setup\|setup-env→multi req\* | +pokeemerald(agbcc) |
| Extra report | — | — | env-presence + residue | env-presence + git triage | — |

**Load-bearing finding:** `coordinator`'s `setup_one` is a **strict superset** of
python-lab, bot-prod, and pinned-research's manifest handling. So four of five
are *one base shim + a ~20–30-line knob-diff apart*; only **gba-lab** is genuinely
separate (heavy apt + devkitARM + agbcc). **Latent bug:** coordinator's
`pick_python` has no `superbot-next→3.11` case, yet superbot-next is a child of
the live multi-repo (coordinator) env — it installs under bare `python3`, correct
only by luck.

### 4.3 Ranked consolidation recommendations

- **R1 (doc-only, zero risk) — register the 5 unregistered python-lab lanes**
  (sim-lab, product-forge, idea-engine, superbot-idle, mobile-lab) in
  `archetypes.md` + the `Serves:` header of `archetype-python-lab.sh`. Closes the
  biggest drift class with no code change. **superbot-idle is a LIVE seat naming
  no archetype** — highest priority within R1.
- **R2 (biggest surface cut) — collapse the 4 Python scripts into ONE base shim +
  3 knobs** (`BASELINE_PIP`, `ENV_REPORT` var-list, `pick_python` table). python-
  lab/coordinator/bot-prod/pinned-research become ~20–30-line config diffs.
  **Fix in-flight:** add the missing `superbot-next→python3.11` case to the
  coordinator table.
- **R3 — gba-lab: keep it, fix two lane gaps.** (a) It installs **no
  ROM-patch/distribution tooling (no `flips`, no `xdelta3`)** — a pokeemerald
  *mod* that ships to players needs a base→modded patch (the ROM itself is
  un-distributable), so confirm pokemon-mod-lab's shipping model and add
  `xdelta3`/`flips` if it emits patches. (b) Gate the Block-3 devkitARM Track-B
  mirror pull behind Butano/homebrew detection so a pokeemerald-only env stops
  pulling an unsigned-mirror toolchain it never uses. *(This directly affects the
  new Retro-Games seat, which spans both game repos.)*
- **R4 — retire the per-package `setup-script.sh` probe variants** (dual, drifting
  lineage; websites/substrate-kit/fleet-manager metas already flag it). Pick one
  lineage; normalize superbot-games' split `environment/` vs `environments/`
  dirs.
- **R5 — fix the codetool-lab lineage bug:** point the 3 `codetool-lab-*` env
  fields at `archetype-python-lab.sh` (has the `pyproject .[dev]` branch) instead
  of `setup-universal.sh` (silently skips pyproject → their editable dev deps
  never install). Archived labs — low urgency, but a real bug.
- **R6 — decide mobile-lab's shape before launch:** its Node/Expo toolchain is
  orthogonal to all 5 archetypes; if a second JS lane appears, promote a thin
  `node-lab` knob on the R2 base rather than repeating the repo escape-hatch.

---

## 5. Recommended sequencing (for the manager)

1. **Route to the owner (owner-provenance):** the §2.4 corrected merge clause for
   `UNIVERSAL.md` — the owner lands it directly (same guard that required the
   original landing). This is the fleet-critical fix.
2. **After the owner lands §2.4:** re-issue every walled `instructions.md` (§2.2)
   from the corrected block, fixing the §3.2 self-contradictions in the same
   pass; resolve the §3.1 mandatory-block drift; hoist §3.3 into `UNIVERSAL.md`.
3. **Do now (manager-owned, no owner needed):** env **R1** + **R5** (doc-only) and
   file the **R2/R3/R4/R6** consolidation as its own lane of work.
4. **Verify per lane before trusting §2.3:** for each repo, confirm whether its
   `auto-merge-enabler.yml` is actually installed in `.github/workflows/` and
   whether "Allow auto-merge" + the required check are set — the lanes that
   *can't* arm need the two-party or `GITHUB_TOKEN`-workflow path, not just the
   corrected wording.

---

## Method + provenance

Two read-only `general-purpose` mapping agents over `/workspace/fleet-manager` at
HEAD `f8eeaac`, cross-referenced to `substrate-kit` (canonical merge doctrine).
Owner-directed via a superbot session, 2026-07-11. No files under
`projects/UNIVERSAL.md` were edited; §2.4 and §3.3 are proposals. Every "walled"
line is quoted with a `file:line` citation above — re-verify before re-issuing.
