# substrate-kit v1.21.0 follow-ups — the next kit session's worklist

> **Status:** `reference` · 2026-08-13 · sources: Codex inline review of fm
> #853 (the v1.21.0 adoption diff, head `daf5b7c`) + one residue this session
> found itself. Line numbers are against **vendored v1.21.0**.
>
> **Why this file exists:** the same mechanism that produced
> [the seven-defect worklist](2026-08-09-substrate-kit-defects.md) — Codex
> reading the vendored dist inside an adoption diff — ran again on the release
> that closed it, and returned five findings. Per that worklist's own
> doctrine, **none was patched in fleet-manager**: `cmd_upgrade` overwrites
> the dist and no gate hashes it, so a local patch silently forks one adopter
> and then evaporates. The fixes belong upstream, in the next cut.

## The findings (all Codex, fm #853, P2)

| # | site (vendored v1.21.0) | defect | provenance | why the adoption stands |
|---|---|---|---|---|
| 1 | `bootstrap.py:20183` (workflow generator, verify-step sentinel) | the direct-invocation anchor does not recognise interpreter options — `python3 -u bootstrap.py check --strict` gets NO absent-card sentinel, leaving the mtime-fallback hazard for that shape | **new in v1.21.0** (the sentinel itself is new) | a missed sentinel = the pre-v1.21.0 behaviour, never worse; fm's own confirmed command is the plain form, which IS rewritten |
| 2 | `bootstrap.py:27733` (strict-loop advisory promotion) | a promoted `ADVISORY_GATE_READY` finding prints under the "never exit-affecting" header and records `posture="advisory"` in guard-fires, then fails the command — contradictory output and telemetry | **pre-existing on kit main since #579 (2026-08-06)** — shipped in this release but not authored by it | dormant in practice: the fresh 12-adopter sweep measured 0 promoted-site findings on 12/12 trees |
| 3 | `bootstrap.py:2966` (`check_claim_provenance`, #565) | scans hard-coded `target/docs` instead of `config.docs_root` — silently no findings for non-default layouts | **pre-existing since #565 (2026-08-04)** | advisory checker; every registry adopter runs the default `docs/` |
| 4 | `bootstrap.py:4533` (`check_boot_path`, #579) | infers the agreement via `agreement_home()` file-existence instead of parsing the router's committed pointer — a stale pointer at a missing `.claude/CLAUDE.md` passes when `CONSTITUTION.md` happens to have a boot section, the exact original failure class | **pre-existing since #579** | advisory and deliberately un-gated (its own changelog entry: 11/11 adopters red, hand-edit fix) |
| 5 | `bootstrap.py:5485` (`_CLAUSE_SEP` subordinators + mention region) | a subordinated repudiation ABOUT a quoted mention is severed from it: `The "agents cannot merge" rule is not a wall because it was superseded` stays clear (cue precedes the subordinator), but a predicate carried INSIDE the subordinate clause (`…rule because it is superseded`) now reds where v1.20.2 cleared | **new in v1.21.0** (the defect-7 fix's price) | a false POSITIVE — self-announcing, the cheap direction by the checker's own doctrine; corpus A/B measured 0 newly-flagged lines across both repos' live docs |

## Two more, from the phase-3 wave (Codex, websites #499 R1, 2026-08-13)

The same mechanism ran a third time — Codex reading the vendored v1.21.0 in
an adoption diff — and returned five findings on websites #499: rows 3 and 4
above **re-found independently** (cross-adopter confirmation, same sites),
one adopter-local divergence (seat-digest listing `continuation-prompt` while
the consumer-untouched `docs/SKILLS.md` predated it — resolved on websites
the kit-sanctioned way, `upgrade --apply-docs`), and two NEW dist defects,
recorded here per the same doctrine (nothing patched in a vendored copy):

| # | site (vendored v1.21.0) | defect | provenance | why the adoptions stand |
|---|---|---|---|---|
| 6 | `bootstrap.py:18946` (`_promote_gate_ready`) | **P1** — folds `check_enforcement_strength`'s `strength_advisories` into the exit-affecting promoted set, while that checker's own contract and remediation text promise advisory-only; an adopter deliberately keeping a simpler hand-rolled gate would red every `check --strict` after upgrading | **new in v1.21.0** (the promotion batch) | did not bite websites — its hand-rolled `quality` gate ran `check --strict` to exactly the designed born-red hold this session (`MEASURED`); the fresh 12-adopter sweep measured 0 promoted-site findings |
| 7 | `bootstrap.py:5736` (`_mention_region`) | region boundary taken from the blocklist-match span rather than the enclosing quote — a separator INSIDE the quote (`"…cannot merge when checks fail"`, `"…cannot merge and deploy"`) ends the region early, severing the attached repudiation and redding valid prose | **new in v1.21.0** (the defect-6/7 region logic's second price, beside row 5) | false-POSITIVE direction, self-announcing; corpus A/B measured 0 newly-flagged live lines on both phase-2 repos and websites' tree reds nothing |

Row 6 joins row 2 at the top of the fix order — same family (promotion
contradicting the advisory contract), and the only exit-affecting class here.

**Round 2 on the same PR returned six more (websites #499, head `86a9554`,
all P2, all in the dist, none in the round's own diff):**

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 8 | `bootstrap.py:18945` + `:18948` | two more promoted families violating their checkers' own contracts — `template_sync_advisories` (the checker explicitly allows deliberate divergence with no machine-readable acceptance) and `fastlane_symmetry_advisories` (the checker's documented version-skew tolerance calls a required-check red in that window a fleet bomb) — same class as row 6; the promoted-set membership needs a contract review as one unit | new in v1.21.0 (the promotion batch) |
| 9 | `bootstrap.py:27710` | the designed-hold predicate evaluates PRE-promotion `doc_findings`, so an in-progress card plus any gate-ready advisory prints "nothing to investigate" and then reds for the promoted finding — a directly contradictory CI diagnosis; same family as row 2 (`:27733`) | new in v1.21.0 |
| 10 | `bootstrap.py:27708` | `--gate-preview` combined with `--strict` falls through to the ordinary strict return path and exits 1 on any existing violation, contradicting the CLI contract that the preview "always exits 0" — fleet-sweep automation stops on the first non-clean adopter | new in v1.21.0 |
| 11 | `bootstrap.py:4560` | `check_boot_path`'s agreement `read_text` is unguarded — an existing-but-unreadable agreement raises `OSError` and crashes the whole `check` invocation instead of failing open like the sibling checker | pre-existing since #579 |
| 12 | `bootstrap.py:4500` | boot-entry anchor fragments (`docs/current-state.md#recently-shipped`) are captured as part of the filename, so an anchored existing doc emits `boot-path-unresolved`; anchored ROOT docs are not captured at all — strip and validate `#fragment` separately | pre-existing since #579 |

Rows 8–12 carry the websites #499 Codex threads verbatim; the two-round cap
was reached there with zero adopter-side changes owed (the only round-2-scoped
change had already landed as the `--apply-docs` refresh).

**Rounds on gba-homebrew #215, venture-lab #289, idea-engine #899 and
superbot-mineverse #144 added three more and sharpened row 9** (all P2 unless
marked; every one dist-routed, zero adopter-side changes owed):

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 13 | `bootstrap.py:5873` | **P1** — a qualified reassertion after a repudiation is cleared: `The "agents cannot merge" rule is false in staging but true in production` exits at `rule is false` and emits nothing, where v1.20.2 flagged it — a false **NEGATIVE** (a standing wall stays green), the expensive direction by the checker's own doctrine | new in v1.21.0 (gba #215 R1) — **FIXED upstream, kit #587 (2026-08-28)** |
| 14 | `substrate-gate.yml` template `:278` (pytest step) | the always-planted pytest step keys on `tests/` EXISTENCE; a native/fixture `tests/` dir with no Python tests makes pytest collect nothing and exit 5 → the gate reds permanently on non-Python repos that add one (measured non-bite on gba: no `tests/` dir at all) | new in v1.21.0 (gba #215 R1) |
| 15 | `bootstrap.py:4872` (`check_fastlane_symmetry`) | looks exclusively for `.github/workflows/ci.yml`, but the kit generates the claims-only guard into `substrate-gate.yml` (`LIVE_CI_RELPATH`) — standard adopters hit the early return and the symmetry checker NEVER runs, silently missing the card-less auto-merge hole it exists to catch | new in v1.21.0 (venture-lab #289 R1) |

Row 9 sharpened twice on re-finds: promoted findings are appended AFTER
`load_allowlist()`/`apply_allowlist()` — so a reason-carrying exception
**cannot suppress a promoted finding** (an accepted custom-gate divergence
reds `--strict` permanently), and the fire is recorded `posture="advisory"`
while the exit goes red (telemetry corruption; gba/venture-lab reads).
Cross-adopter re-find tally: row 3 sighted on 4 trees, row 4 on 4 trees —
independent confirmation, same sites, every wave PR.

**The idea-engine #899 / superbot-mineverse #144 rounds added six more:**

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 16 | `substrate-gate.yml` template `:278` (pytest step) | **P1** — the step installs only `requirements.txt`; a repo keeping deps in `requirements-dev.txt` (mineverse, deliberately) collect-fails on imports and the REQUIRED gate stays red past the flip — bit live on mineverse #144, fixed there by reverting the regen | new in v1.21.0 (row 14's sibling — the step's second wrong assumption) |
| 17 | `bootstrap.py:5780` | the occurrence mask is applied to `_REPUDIATION_CUES` but not `_DATED_LINE`/`_FALSE_LABEL`, so `FALSE "agents cannot merge", agents cannot merge` and the dated-supersession variant pass strict — false **NEGATIVE**, joins row 13 at the top | new in v1.21.0 (mineverse #144 R1) — **FIXED upstream, kit #587 (2026-08-28)** |
| 18 | `bootstrap.py:6036` | a digest `BEGIN` fence with no `END` (merge conflict, hand edit, forged marker) exempts every remaining line of `docs/seat-digest.md` from the strict false-wall scan — fails open; the drift check that would notice is advisory-only | new in v1.21.0 (two independent sightings: idea-engine #899 `:6036`, mineverse #144 `:6038`) — **FIXED upstream, kit #587 (2026-08-28)** |
| 19 | `bootstrap.py:3010` | provenance finding paths are computed relative to `docs_root` (`measurements/x.md`, not `docs/measurements/x.md`) — reports point at the wrong artifact and an exception written with the real path can never match | pre-existing since #565 (idea-engine #899 R1) |
| 20 | `bootstrap.py:4492` | the boot-path checker does not recognise the kit's OWN generated `.claude/CLAUDE.md` heading (`## Orientation — read first, in order`) → false `boot-section-missing` on kit-standard repos — observed live on idea-engine's tree this session | pre-existing since #579 (idea-engine #899 R1) |
| 21 | `bootstrap.py:4587` | boot entries the template marks `when present` (`HANDOFF.md`, untracked) are treated as mandatory → false `boot-path-unresolved` on healthy generated agreements | pre-existing since #579 (idea-engine #899 R1) |
| 22 | `substrate-gate.yml` template `:135` (claims-only guard) | **P1** — a `claude/*` PR whose diff is a claim PLUS any other `control/**` file (e.g. `control/status.md`) keeps the control-only lane while `non_claims` is non-empty, so the guard passes and the PR can auto-merge card-less — the exact race the step exists to close. Not a regression on adopters (pre-v1.21.0 gates had no claims guard at all), but the new protection has a hole | new in v1.21.0 (idea-engine #899 R2) |


**One more from the phase-3 review PR (Codex, fm #858 R1, 2026-08-14):**

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 23 | `session-close` skill template (staged `.substrate/skills/session-close/SKILL.md`, step 3; same sentence embedded in `bootstrap.py`) | the template licenses a `do-not-automerge` PR to "wait for the owner" with **no session bound** — contradicting the owner's nothing-waits-in-an-open-PR ruling (fm decisions ledger, 2026-08-14). The fix has **two halves, both required**: the within-session bound in step 3, and an unanswered-fork exit step that lands the handoff on `main` — the terminal card + the owner ask ride a **mergeable records-only PR** before the work PR closes (branch retained) — otherwise the ask strands on a non-default branch no session reads. fm's live skill carries both (re-apply table); the upstream fix takes effect **on the next hand-run copy/install, not on upgrade itself** — upgrades only re-stage `.substrate/skills/`, and the documented `cp` loop is what overwrites the live file (fm SKILLS-local's measured install contract) | template text, pre-existing (predates v1.21.0; surfaced by the ruling, not by a code change) |

**The couch-legend seed round (2026-08-21, couch-legend #5 — a FRESH v1.21.0
`adopt --wire-enforcement` on a TypeScript/vitest repo) added two rows and
the first live bite of row 14:**

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 24 | `bootstrap.py:29710` (`control-inbox.md.tmpl`) vs `:8271` (inbox-order-grammar) | **adopt's own planted `control/inbox.md` seed fails the kit's own strict inbox check**: the template's closing line `*(no orders yet — …)*` is neither the file header nor a `## ORDER` block, so the very first `check --strict` after a clean adopt reds `[inbox-order-grammar]` on kit-planted bytes — fixed on couch-legend by deleting the placeholder line; the upstream fix is a grammar-conforming seed (or a checker carve-out for it), one or the other, not both | seed template predates v1.21.0; first measured live on the couch-legend seed |
| 25 | `bootstrap.py:17061` (`detect_verify_command`) + the adopt-time render seam | two halves, one wrong doc: (a) the derive returns **`npm test`** for any `package.json` with a real test script — it never reads `pnpm-lock.yaml`/`packageManager` (wrong toolchain in a pnpm repo) and prefers `test` over the repo's fuller gate script (`check` = tsc + vitest + build on couch-legend), so the working agreement's "Verifying a change" under-verifies; (b) the provisional derived value **renders into the planted docs as final text at adopt time**, so a later corrected `answer verify_command …` has no `${verify_command}` token left to fill — `render --live` reports 0 unfilled placeholders while the doc still says `npm test`; hand-editing the rendered doc is the only cure. Related paper cut, same slot: the gate-safety NOTE's suggested "runnable rewrite" strips only parentheticals, so it offered `pnpm check; kit discipline: python3 …` — a line that fails at `kit` if pasted | pre-existing (derive + render seam predate v1.21.0); measured on the couch-legend seed |

**Codex round 1 on the seed PR itself (7 findings, 7 conceded + fixed
in-repo) added three more dist/template rows:**

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 26 | `.claude/CLAUDE.md` + `AGENT_ORIENTATION.md` templates (preflight step) | **P1 on the adopter** — the unconditional `git fetch && git reset --hard origin/main` is ordered BEFORE the dirty-tree safeguard prose, so a warm session holding uncommitted foreign work destroys it before ever reaching "stop and report" — fixed on couch-legend by ordering `git status --short` first in both surfaces | template, pre-existing (Codex R1, couch-legend #5) |
| 27 | adopt/`hooks --build` interpreter recording | writes `sys.executable` as an ABSOLUTE path (`/usr/local/bin/python3`) into all four `.claude/settings.json` hook commands and the config `interpreter` — exit 127 in pyenv-style environments, silently disabling every hook; PATH-resolved `python3` works in both venues — fixed on couch-legend in config + template + live settings | pre-existing (Codex R1, couch-legend #5) |
| 28 | adopt heartbeat seed + `heartbeat --full` defaults | the seed and the mechanical writer default `check: green · engaged: yes` while the SAME adopt run prints a 12-item NOT-ENGAGED hold list and `check --strict` exits 1 — fleet readers see a fresh adopter as green before its first gate has ever passed; the writer also offers only `--kit-check {green,red}` while the control contract's own vocabulary includes `red-by-design` (health line) — fixed on couch-legend by writing the honest mid-PR heartbeat by hand | pre-existing (Codex R1, couch-legend #5) |

Row 25 widened by the same round — **three more consumers treat the
free-prose `verify_command` slot as a runnable**: skill templates embed it
in a bash command span (an annotated value renders quality-gate's step 1
unexecutable — bash rejects the `(`), `docs/SKILLS.md` grounds print the
DERIVE-time value (`npm test` survived the corrected answer), and the
working-agreement/architecture/workflow verify sections rendered the derived
value as final text across FOUR docs, not one. The slot's own gate-safety
NOTE proves the kit knows the value may be prose; the render layer doesn't.
(Round 2 sharpened the blast radius: fixing only the INSTALLED skill copies
is not enough — `docs/SKILLS.md`'s documented staged→live copy loop restores
the broken commands from the staged tree, so both trees need the fix until
the template does. Also row 14's third wrong assumption, same round: the
pytest step writes `tests/__pycache__/` into adopters whose planted
search-hygiene appends never cover Python bytecode — a version-specific
`.pyc` then dirties every differently-versioned session's boot tree.)

**Codex round 2 on the same PR (6 findings, 6 conceded + fixed in-repo,
head `9d957a2`) added four more template/design rows:**

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 29 | SessionStart hook (`record_session_anchor`) vs the preflight contract | the hook stamps `session_anchor` into TRACKED `.substrate/state.json` before the agent can look, so the template's own "check `git status` first" boot step meets a dirty tree on EVERY session — and the mandated `git reset --hard` then erases the anchor session-close needs for commit attribution; the anchor either belongs in untracked state or must be re-stamped post-reset by contract (couch-legend #5 R2; fixed in-repo by teaching both preflight surfaces the anchor-only exception + a post-reset `session-start` re-stamp) | pre-existing |
| 30 | `CONSTITUTION.md.tmpl` + `CLAUDE.md.tmpl` boot sections under `--include-claude` | BOTH templates render a "## Boot read path" claiming to be "the one list", and the two lists disagree out of the box (one names `docs/CAPABILITIES.md`, the other repo docs) — two canonical boot lists by construction on any adopter that installs the claude tree; one should render as a pointer (couch-legend #5 R2; fixed in-repo by making CONSTITUTION's section the pointer) | pre-existing |
| 31 | `session-close` skill template (three sites) | promises "let the server-side auto-merge-enabler land it" / "Green then merges server-side" unconditionally, but adopt stages the enabler WITHOUT installing it and cannot flip the repo's Allow-auto-merge setting — an agent following the advertised path deletes its claim, pushes, and ends with the PR open forever; needs an installed-enabler conditional (row 23's sibling) | template, pre-existing (couch-legend #5 R2) |
| 32 | skill templates' `Declared capabilities` lines | three skills declare narrower capabilities than their own mandatory steps — `scope-backlog-item` (edits the status heartbeat; declares read-only), `repo-health` (step 3 fixes docs; declares run), `intake` (may append to the question router; declares read) — and SKILLS.md § Precedence makes declarations the thing that overrides stance, so these skills cannot authorize their own required writes (couch-legend #5 R2; fixed in-repo, both trees + index rows) | template, pre-existing |

**Codex round 3 on the same PR (5 findings, all P1, all conceded + fixed
in-repo, head `b3497dd` fixes; reviewed head `60aa8d6`) added the final two
rows:**

| # | site (vendored v1.21.0) | defect | provenance |
|---|---|---|---|
| 33 | `upgrade-distribution` skill template, step 2 | downloads release assets into the REPO ROOT — but every adopted target already holds `bootstrap.py` + `bootstrap.py.sha256`, and `gh release download` refuses same-name files without `--clobber`, so the documented upgrade flow stops on a collision at its second step on every adopter; download to a temp dir + move (couch-legend #5 R3; fm's own live copy of this skill carries the identical text — same fix due there when the template lands) | template, pre-existing (P1) |
| 34 | `run_upgrade` + the sidecar convention | the upgrade replaces only `bootstrap.py`, never the committed `bootstrap.py.sha256` sidecar the same adoption convention plants (spider-swing and couch-legend both commit one) — every upgrade silently leaves a stale sidecar; on couch-legend, where `tests/test_kit_pin.py` enforces dist==sidecar in the required gate, that reds every future upgrade PR until the skill installs the new sidecar with the dist (couch-legend #5 R3; skill step 5b added in-repo, rollback covers both files) | pre-existing (P1 where a pin test exists) |

Round 3 also widened two rows in place: **row 26** has a third site — the
`upgrade-distribution` skill template's step 1 opens with the same
unconditional `git fetch && git reset --hard` (fixed in-repo with the
status-first + checkout-B form; the boot templates additionally learned the
local-commits leg — `git status` alone passes on a clean feature branch
whose commits a reset would strand). **Row 29** has a sibling artifact — the
SessionStart hook also writes root `HANDOFF.md`, untracked and NOT in the
planted ignore appends, so the boot contract's own "clean tree" expectation
breaks on every boot with a session card present (fixed in-repo by
gitignoring the pointer, matching its never-commit design).

Sighting updates from the same round: **row 14 bit live for the first time**
— couch-legend's `tests/` is vitest-TypeScript, so the planted gate's pytest
step would red on "collected 0 items"; worked around in-repo the productive
way (`tests/test_kit_pin.py`, stdlib Python pinning the vendored dist to its
sha256 sidecar and the config pin to the dist header — the step now verifies
something real). **Rows 20 and 21 sighted on a fresh v1.21.0 adopt**: the
kit's own generated `.claude/CLAUDE.md` heading drew `boot-section-missing`
(fixed in-repo by renaming the heading to `## Boot read path …`), and the
generated agreement's own `HANDOFF.md` "when present" list line would draw
`boot-path-unresolved` (pre-empted in-repo by moving it to prose). Rows
24–34 join the adopter-facing template family in the fix order (with 14, 16,
22, 15, 23) — 26, 29 and 33 first among them: the reset-ordering family
destroys work, 29 makes 26's own safeguard fire on every healthy boot, and
33 stops the documented upgrade flow at its second step on every adopter.

Round-2 sighting updates: row 5 sharpened with the quoted-conditional class
(`The phrase "agents cannot merge when CI is green" is not a wall.` now reds —
idea-engine `:5485`); row 10's second site is the `cmd_check` return
(`:29522`); row 12 re-found at `:4586`; row 3 reached five sightings and
row 20 two. Also adopter-side and NOT the kit's to fix: mineverse's
capability-seed fence differs from kit form, so the v1.21.0 seed's wall
retractions did not refresh there — its card carries the follow-up.

Fix-order restated after the couch-legend seed (2026-08-21, fm #879 — this
supersedes the post-wave order, which is preserved struck-through below):
~~**the false negatives first (13, 17, 18)**~~ **— CONSUMED 2026-08-28,
kit #587 (see the consumption note below); the order now LEADS with the
work-destroyers** — then the work-destroyers and flow-stoppers from the seed round
(**26, 29, 33** — the reset-ordering family destroys work, 29 makes 26's own
safeguard fire on every healthy boot, 33 stops the documented upgrade flow
at its second step; **34** rides with 33 as the same skill's other half),
then the exit-affecting promotion family as one contract-review unit
(2, 6, 8, 9, 10), then the remaining adopter-facing template defects
(14, 16, 22, 15, 23, **24, 25, 27, 28, 31, 32**), then the boot-path family
(4, 11, 12, 20, 21, **30**), then the rest (1, 3, 5, 7, 19).
~~Fix-order restated after the wave: the false negatives first (13, 17, 18),
then the promotion family (2, 6, 8, 9, 10), then the adopter-facing template
defects (14, 16, 22, 15, 23 — 23 added 2026-08-14, fm #858), then the
boot-path family (4, 11, 12, 20, 21), then the rest (1, 3, 5, 7, 19).~~

**Consumption began 2026-08-28 (kit #587, the OD-24 review round's session
2): rows 13, 17 and 18 are FIXED upstream in kit #587** — each reproduced against the
published v1.21.0 asset first (sha256 `8807a00e…`, three-way match), fixed in
`src/engine/checks/check_no_false_walls.py` with named regression pins in
`tests/test_check_no_false_walls_leg.py`, dist regenerated, and corpus-A/B'd
against the kit + fleet-manager live trees (0 newly-flagged, 0
newly-cleared lines) — the A/B re-run at every review round. The PR took a
pre-push adversarial verification round (2 regressions + 2 holes found and
fixed) and three Codex rounds (5 + 6 conceded and fixed, all pinned; R3's 4
verified and deferred as **row 35** below under the two-re-review cap — the
tally 5→6→4 measured non-convergent). The fixes ride kit `main` unreleased —
the next cut is owner-paced. The same PR landed the kit-tree pointer to this
worklist (genesis-dig gap #5): `kit:docs/NEXT-TASKS.md` is superseded into
the route.
**Next per the restated order: the work-destroyers 26, 29, 33 (+34).**
Coupling note (measured while fixing): rows 13/17/18 are separable from the
promotion family (2/6/8/9/10) — the fixes touch only the clearing grammar
and the fence scan, not the promotion seam. Two adjacent uncovered shapes
were found and deliberately left (same clearing-grammar territory, not in
any row's repro): a cue severed from its quoted mention by an apposition
noun (`…"…" claim was superseded, <bare wall>` — the mask patterns carry no
noun slot), and a reassertion-after-cue on the plain-clause path (pre-dates
v1.21.0). Both are recorded in kit #587's session card as candidates for a
future row.

**Row 35 — the reassertion-grammar residuals deferred from kit #587's R3
(2026-08-28; the two-re-review cap's land condition):**

| # | site (kit main post-#587, `src/engine/checks/check_no_false_walls.py`) | defect | provenance |
|---|---|---|---|
| 35 | the row-13 reassertion gate + its cross-line tail | four verified corner cases, none firing on either live tree at land time: (a) an `or`-coordinated negated complement pair (`does not hold or remain in force`) reads as affirmative — false POSITIVE, cheap direction; (b) a later `whereas <other-capability>` clause suppresses the family gate over an earlier real reassertion (`…but remains in force in production, whereas deploys are unrestricted`) — false NEGATIVE; (c) the truth-token vocabulary omits direct state predicates (`active`, `enforced`, `operative`, `valid`) — false NEGATIVE; (d) the cross-line tail treats a Markdown table row as prose continuation — false POSITIVE. Fix family: per-contrast-clause family scoping + token vocabulary + a table-row stop in the tail extension; the adjacent shapes already recorded in kit #587's card (apposition-severed mention cue; reassertion after a plain-clause cue; empty-family comma-cue baseline; FALSE-label family-blindness) belong to the same future fix unit | new in kit #587 (Codex R3, all four execution-verified 2026-08-28); the round tally 5→6→4 measured non-convergent, so the cap landed the PR with these named |

## Residue this session found itself (not Codex)

- **The kit's `tests/test_skills_index_install_contract.py` guard regex is
  vacuous against the very text it guards**: `install\s+with[^.]{0,80}skills`
  cannot cross the period in "bootstrap.py", so it would MISS the old
  defect-5 claim if it ever returned. fm's `tools/ab_kit_scan.py` had the
  same `[^.]` gap and fixed it in fm #853 (`[\s\S]{0,100}?`); the kit test
  needs the same one-line fix. Found by running the harness's positive
  control against the dist that HAS the claim (claim=0 where 1 was true).

## Post-release review pointer (2026-08-13, fm #855)

The phase-2 rollout review re-verified this worklist's currency citation
against the tree (`:398-402` right, `:90` wrong — the kit #583 comment stands)
and measured the superbot-next gate failure in the real venue:
[`2026-08-13-v1210-phase2-review.md`](2026-08-13-v1210-phase2-review.md).

## How to use this

The next kit session takes this file the way this session took the
seven-defect worklist: fix upstream in the **restated order above**
(superseded 2026-08-13, fm #855 — this line originally said "2 and 5 first",
written when the list had five rows; the wave grew it to 22 and the false
negatives now lead), with reproductions before
dispositions, and verify against the published asset, not the changelog.
Rows 1 and 5 carry the fm #853 Codex thread verbatim; rows 2–4 predate the
release and simply had their first non-author read here.
