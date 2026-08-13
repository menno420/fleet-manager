# Session — v1.21.0 rollout: phase-2 review settled, then phase 3 (owner-paced)

> **Status:** `in-progress`
>
> Born-red: this card was the sole FIRST commit on the branch; the review
> finding, the worklist rows, the phase-2-card corrections and the §7 row land
> in the work commits; the `complete` flip is the deliberate LAST commit.

- **📊 Model:** fable-5 · high · review/verify

## previous-session review

The phase-2 session flagged three of its own claims for adversarial re-check,
and all three settled by measurement rather than belief
([`docs/findings/2026-08-13-v1210-phase2-review.md`](../docs/findings/2026-08-13-v1210-phase2-review.md)):

1. **substrate-gate/ast.Num — REASONED → MEASURED, in the venue.** The gate
   failed 3/3 real runs on the PR head whose squash tree is hash-identical to
   the merged `main` (`8a18b731…`; CPython 3.14.6;
   `test_parse_message_shapes`, 1 failed/3672 passed), and the missing merge
   run is CONFIRMED GITHUB_TOKEN auto-merge suppression (push actor
   `github-actions[bot]`, 0 runs of any workflow on the merge SHA; July's
   main runs were the owner's web-UI merges). The card's `:307` was right;
   the handoff prompt's `:306` was the drift.
2. **superbot's "neither documented path fits" — narrowed in place.** `init`
   (both refusals said "run init first"; nobody ran it) succeeds minimally
   (one path) and unlocks `upgrade`, which reproduces `adopt`'s
   over-correction (20 paths, `docs/decisions.md` beside `docs/decisions/`,
   enabler regen) and still vendors no dist. Vendor+pin stands, now measured.
3. **The currency citation — verified right.** `:398-402` is the
   unauthenticated raw step (`get(url, {})` at `:400`, immediate 200 return);
   `:90` is the API-fallback token comment, exactly as the kit #583 comment
   says. Bonus: the KNOWN-FALSE registry cell healed itself — unauthenticated
   raw now serves superbot's pin as 1.21.0 — while the structural defect
   stays filed upstream.

What phase 2 got right held everywhere it was leaned on: the enabler-regen
lesson (sbn #606) fired three more times this session (gba, idea-engine,
mineverse), and the narrow-don't-swap correction doctrine governed every wall
disposition in the wave.

## Order

The owner, live (AskUserQuestion, 2026-08-13): phase 3 is **the five trivial
v1.20.1 hops** — websites, gba-homebrew, venture-lab, idea-engine,
superbot-mineverse — one `upgrade-distribution` run each, never batched;
**trading-strategy is skipped until its archive decision** (its stale row
stays honest). superbot-games and pokemon-mod-lab remain for a batch he has
not named.

## Result — one outcome line per target (skill report format)

- `websites: v1.20.1 → v1.21.0 · sha256 4-way ✔ · bank ✔ byte-identical ·
  carve-outs: none (enabler already current) · PR #499 merged @ 882378abd ·
  tree-verified ✔` — plus its own exact-pin regression test moved per its
  documented ritual, and `docs/SKILLS.md` refreshed via `--apply-docs` after
  Codex R1.
- `gba-homebrew: v1.20.1 → v1.21.0 · sha256 4-way ✔ · bank ✔ byte-identical ·
  carve-outs: enabler host card-guard NOT carried → regen REVERTED
  byte-identical; gate regen kept (purely additive) · PR #215 COMPLETE but
  PARKED ⚑ · do-not-automerge held` — the required `NDS ROM build` breaks on
  every PR today: the BlocksDS rolling repo rotated out the pinned
  `blocksds-toolchain-1.21.1-1` (404; only 1.22.3-1 served; no stable mirror
  found — skylyrac archive paths 404, Wonderful mirrors only ≤1.6.3, no
  blocksds/sdk release artifacts, Wayback rate-limited). Owner fork in the PR
  body: bump (a real toolchain migration) vs re-host the exact bytes
  (hash-pin makes any source safe) vs keep parking. Also: two arc docs'
  Status lines tokenized (`reference`) and `PLATFORM-LIMITS.md:45`
  allowlisted with reason — all three measured pre-existing under the banked
  v1.20.1 dist.
- `venture-lab: v1.20.1 → v1.21.0 · sha256 4-way ✔ · bank ✔ byte-identical ·
  carve-outs: none (gate regen purely additive; enabler current) · PR #289
  merged @ a7220b1d3 · tree-verified ✔`
- `idea-engine: v1.20.1 → v1.21.0 · sha256 4-way ✔ · bank ✔ byte-identical ·
  carve-outs: gate host wake-preflight step re-applied IN the regen (fm #833
  precedent — its own preflight reds without it, verified green in the CI
  venue); enabler regen REVERTED byte-identical · PR #899 merged @ 320acabd9 ·
  tree-verified ✔` — plus `ideas/shiftlife/` created (its required gate had
  been structurally red on every PR since the roster froze with shiftlife
  listed active and no section directory; measured on the card-only head),
  one anti-wall aside reworded, one reason-carrying exception (scope noted).
- `superbot-mineverse: v1.20.1 → v1.21.0 · sha256 4-way ✔ · bank ✔
  byte-identical · carve-outs: gate regen REVERTED (template pytest step
  installs only requirements.txt — this repo keeps deps in
  requirements-dev.txt; the REQUIRED gate would have stayed red past the
  flip) · PR #144 merged @ 9f8047f9e · tree-verified ✔` — the round-1
  "revert" was a measured no-op (`git checkout HEAD --` against the committed
  regen), conceded in-thread on Codex's round-2 catch and redone against the
  merge-base with hash proof (`51f3ea33…` → `bf644599…`).
- Registry regenerated: kit #584 (stamp `2026-08-13T19:23:46Z`) — 8 current ·
  4 honestly stale; superbot's pin cell healed; pokemon-mod-lab reads clean
  after `add_repo` (the private-repo egress scoping is a new ledger entry).

**Adversarial review across the wave: eight Codex rounds, 41 findings.**
Six adopter-side, all `[conceded]` and fixed (among them Codex catching my
false revert claim — the most valuable find of the wave); one `[survived]`
(idea-engine's exception scope, grounds in-thread); one `[conceded]`-deferred
with reason (mineverse's capability-seed fence — its card carries the
follow-up); 33 dist-routed upstream. The kit worklist
([`docs/findings/2026-08-13-substrate-kit-v1210-followups.md`](../docs/findings/2026-08-13-substrate-kit-v1210-followups.md))
grew from 5 to **22 rows**, with the fix order restated: false negatives
first (13, 17, 18), the promotion family as one contract-review unit
(2, 6, 8, 9, 10), then the template defects (14, 16, 22, 15).

## ⚑ Flagged for the owner — decisions not taken

- **gba-homebrew's toolchain fork** (bump vs re-host vs park) — PR #215 body
  carries the full probe record; the upgrade itself is done and parked safely.
- **Make `substrate-gate` required on superbot-next?** Now costed MEASURED:
  every PR would red at the pytest step until `ast.Num` is removed (dead
  `# Python < 3.8` code) or the gate pins the product interpreter (`ci.yml`
  pins 3.11); required-check enforcement itself is unaffected by the
  suppression finding.
- **The orientation-budget freeze** still blocks any current-state.md entry
  (~4 words of headroom, measured by phase 2); this session again recorded
  its work in §7 + the card only. The restructure remains the owner's call.
- **superbot-games' 3-file self-report DRIFT** — its upgrade session should
  reconcile the heartbeat `kit:` lines at source; not done here (unnamed
  batch).

## Verify

- fm gate: `python3 bootstrap.py check --strict` → exit 1 on exactly the
  designed born-red hold on this card; `tools/check_no_false_walls.py
  --strict` → exit 0 CLEAN. (Both real exit codes, no pipes.)
- Every adopter claim above is tree-verified against `origin/main` raw
  contents (version header + pin + dist sha256), never a PR read.

Layer-2 handoff: null (no `docs/repos/<name>/` folders exist for the wave
repos — coverage is spider-swing-only by design; each repo's own session
card carries its handoff)

💡 **The wave was also a 5-tree live test of v1.21.0's checkers, and the
false-positive/false-negative ledger it produced is release-grade evidence.**
Codex re-found the same dist defects independently on up to five trees
(row 3: five sightings) while each tree also surfaced unique ones — the
next kit session should treat per-adopter Codex rounds as a standing part of
release verification, not an adoption formality: eight rounds turned a
5-row worklist into 22 rows, including three P1s no single-tree pass had
found.
