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
| 13 | `bootstrap.py:5873` | **P1** — a qualified reassertion after a repudiation is cleared: `The "agents cannot merge" rule is false in staging but true in production` exits at `rule is false` and emits nothing, where v1.20.2 flagged it — a false **NEGATIVE** (a standing wall stays green), the expensive direction by the checker's own doctrine | new in v1.21.0 (gba #215 R1) |
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
| 17 | `bootstrap.py:5780` | the occurrence mask is applied to `_REPUDIATION_CUES` but not `_DATED_LINE`/`_FALSE_LABEL`, so `FALSE "agents cannot merge", agents cannot merge` and the dated-supersession variant pass strict — false **NEGATIVE**, joins row 13 at the top | new in v1.21.0 (mineverse #144 R1) |
| 18 | `bootstrap.py:6036` | a digest `BEGIN` fence with no `END` (merge conflict, hand edit, forged marker) exempts every remaining line of `docs/seat-digest.md` from the strict false-wall scan — fails open; the drift check that would notice is advisory-only | new in v1.21.0 (two independent sightings: idea-engine #899 `:6036`, mineverse #144 `:6038`) |
| 19 | `bootstrap.py:3010` | provenance finding paths are computed relative to `docs_root` (`measurements/x.md`, not `docs/measurements/x.md`) — reports point at the wrong artifact and an exception written with the real path can never match | pre-existing since #565 (idea-engine #899 R1) |
| 20 | `bootstrap.py:4492` | the boot-path checker does not recognise the kit's OWN generated `.claude/CLAUDE.md` heading (`## Orientation — read first, in order`) → false `boot-section-missing` on kit-standard repos — observed live on idea-engine's tree this session | pre-existing since #579 (idea-engine #899 R1) |
| 21 | `bootstrap.py:4587` | boot entries the template marks `when present` (`HANDOFF.md`, untracked) are treated as mandatory → false `boot-path-unresolved` on healthy generated agreements | pre-existing since #579 (idea-engine #899 R1) |
| 22 | `substrate-gate.yml` template `:135` (claims-only guard) | **P1** — a `claude/*` PR whose diff is a claim PLUS any other `control/**` file (e.g. `control/status.md`) keeps the control-only lane while `non_claims` is non-empty, so the guard passes and the PR can auto-merge card-less — the exact race the step exists to close. Not a regression on adopters (pre-v1.21.0 gates had no claims guard at all), but the new protection has a hole | new in v1.21.0 (idea-engine #899 R2) |


Round-2 sighting updates: row 5 sharpened with the quoted-conditional class
(`The phrase "agents cannot merge when CI is green" is not a wall.` now reds —
idea-engine `:5485`); row 10's second site is the `cmd_check` return
(`:29522`); row 12 re-found at `:4586`; row 3 reached five sightings and
row 20 two. Also adopter-side and NOT the kit's to fix: mineverse's
capability-seed fence differs from kit form, so the v1.21.0 seed's wall
retractions did not refresh there — its card carries the follow-up.

Fix-order restated after the wave: **the false negatives first (13, 17, 18)**
— they are the checker failing at its one job — then the exit-affecting
promotion family as one contract-review unit (2, 6, 8, 9, 10), then the
adopter-facing template defects (14, 16, 15), then the boot-path family
(4, 11, 12, 20, 21), then the rest (1, 3, 5, 7, 19).

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
