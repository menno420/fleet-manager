# 2026-07-12 — seat-digest regen wiring (grounded-skills slice 6, fm side)

> **Status:** `complete`

📊 Model: fable-5

## Scope (what is about to happen)

Wire fleet-manager's prompt-regen tooling (`docs/prompts/v3/tools/`) to consume
the kit's seat-digest machine extraction contract (kit PR #279 @ dc8aeb1,
released in v1.15.0; fm adopted via PR #123 @ d7d264b0 — `docs/seat-digest.md`
planted). Mechanism: fence-prefix match + byte compare over committed adopter
trees, tree-scan only, NEVER importing or executing kit code. Deliverables:

- `docs/prompts/v3/tools/seat_digest_sync.py` — extraction + registry render
  (`--sync`), drift guard (`--check`, the `--check-registry`-style byte-compare),
  prompt-fence guard (any `substrate-kit:*-digest` fence appearing in a paste
  must byte-match the registry render), `--selftest` fixtures.
- Generated registry render(s) `projects/<seat>/seat-digest.md` for seats whose
  source digests are available (today: fleet-manager's own; wave A/B adopters
  picked up on later re-syncs).
- Minimal advisory hook in `regen_b_files.py` default run.

No-third-copy chain honored (kit plan §4.2e): adopter `docs/CAPABILITIES.md` →
adopter `docs/seat-digest.md` (kit-derived render) → fm registry render →
prompt blocks; nothing here is hand-authored content. Manager-owned surfaces
(per-seat pastes, `projects/UNIVERSAL.md` fetch list) are NOT touched — the
required UNIVERSAL wake fetch-list vN bump + owner re-paste is recorded as a
manager/owner ask, not performed.

## Close-out (what shipped — PR #126)

- **`docs/prompts/v3/tools/seat_digest_sync.py`** (new, ~560 lines): vendored
  contract constants (byte-copies of kit `src/engine/grammar.py` @ v1.15.0 /
  dc8aeb1 — the three fence-prefix pairs + `venues=` regex + the 1,500-char
  block budget); `extract_block()` with semantics identical to the kit's
  `check_seat_digest._fenced_block` (markers inclusive, line-anchored prefix
  match, unmatched fence = no verdict); `--sync` renders
  `projects/<seat>/seat-digest.md` GENERATED registry copies (header + marker
  + deterministic body: one section per source repo, the two blocks VERBATIM);
  `--check` (default) = the `--check-registry`-style gate: third-copy guard
  (missing GENERATED header = violation), structural guard (any content
  outside the fenced blocks = violation), budget guard (>1,500 chars/block),
  byte-compare against fresh extraction where source trees are available
  (SKIP notes where not — CI-safe), paste-fence guard (any
  `substrate-kit:*-digest` fence in a per-seat paste or registry prompt copy
  must byte-match the seat's registry render), and contract-sanity alarm
  (fm's own kit-generated digest + capability-seed fences must satisfy the
  vendored prefixes); `--selftest` = 11 fixture cases, all green. Kit code is
  NEVER imported or executed — text reads only.
- **`regen_b_files.py`**: advisory-only hook in the default run (prints
  seat-digest findings, never exit-affecting — kit PL-008 advisory-first for
  unproven checkers) + docstring pointer. Proven drift checks untouched.
- **Registry renders** (extraction verified against trees at origin/main):
  `projects/fleet-manager/seat-digest.md` (own tree, skills 1,425 + walls
  1,046 chars), `projects/game-lab/seat-digest.md` (gba-homebrew @ 557474d,
  pokemon-mod-lab @ 759dee4), `projects/venture-lab/seat-digest.md`
  (venture-lab digest sha256 15d1b761… byte-identical at origin/main
  12a8d34). All blocks ≤ 1,500-char budget.

Verify: `seat_digest_sync.py --selftest` → `selftest: OK` (11/11) ·
`seat_digest_sync.py --check` → OK · `regen_b_files.py` → exit 0 (all 8
seats clean + `seat-digest advisory: clean`) · `--check-registry` → 24/24 ·
`python3 bootstrap.py check --strict` → only this card's designed born-red
hold pre-flip.

## ⚑ Manager/owner asks (recorded, NOT performed — Q-0261.3 / Doctrine 2)

1. **UNIVERSAL wake fetch-list vN bump + owner re-paste** (flagged by the
   kit-side slice-6 session): the wake fetch list in the manager-authored
   startup surfaces (`projects/UNIVERSAL.md` grant lineage + per-seat
   startups) should gain `docs/seat-digest.md` (and `docs/SKILLS.md`) so
   seats fetch the digest at wake; that is a vN bump + owner re-paste of the
   affected artifacts via the edit-registry-first flow. Manager-authored —
   not touched here.
2. **Splicing digest blocks into the per-seat pastes** is manager-authored
   prompt content (the v3.4 restamp lane, open PR #122): the registry
   renders + the paste-fence byte-match guard are ready for it — a spliced
   block that drifts from kit truth now fails `--check`.
3. **Per-seat walls venue overrides**: regen the SOURCE repo's digest with
   `python3 bootstrap.py seat-digest --venue …` in that repo's lane; fm only
   re-syncs. All four onboarded sources currently carry the Project-seat
   default `venues=autonomous-project,any`.
4. **Remaining seats** (superbot-2.0, websites, self-improvement,
   superbot-world, ideas-lab) onboard by re-running `--sync` once their
   repos' kit ≥ v1.15.0 upgrades land (wave A in flight) and current trees
   are available.

## Decide-and-flag

- ⚑ Registry render homed at `projects/<seat>/seat-digest.md` (the
  GENERATED-copy registry precedent), one file per seat with one section per
  source repo — one scan target for prompt assembly, one drift surface.
- ⚑ Multi-repo seats aggregate all their repos' digests in meta.md order
  (seat→repo map cited from `projects/<seat>/meta.md` @ b25b348).
- ⚑ Unavailable source trees degrade `--check` to structure+budget with SKIP
  notes rather than failing — fm CI has no sibling checkouts; byte-compare
  engages wherever trees exist (session environments).
- ⚑ Advisory-first in the regen default run, exit-affecting only via the
  dedicated `--check` mode — mirrors the kit's PL-008 unproven-checker
  posture rather than fm's hard-fail drift checks, until proven.
- ⚑ Synced game-lab + venture-lab (wave-B repos, trees verified at
  origin/main; venture-lab digest byte-identical despite a stale checkout)
  in addition to fm's own seat — live proof of the multi-seat path without
  waiting for wave A.

💡 Session idea: add a `--sync-from-origin` mode that reads each source
repo's digest via `git -C <tree> show origin/main:docs/seat-digest.md`
(plumbing read, still never executing kit code) instead of the working
tree — the venture-lab case this session (stale checkout, digest happened
to be byte-identical) shows working-tree scans inherit checkout staleness;
reading the committed origin/main blob removes that hazard with zero new
access.

⟲ Previous-session review: the v1.15.0 upgrade session (PR #123) left an
exemplary lane-owed list — its "fm seat-digest fence CONSUMPTION = separate
fm follow-up slice, not this lane" line plus the kit-side card's
prerequisites made this session's orientation near-zero-cost. One
improvement: its lane-owed entry named the WHAT but not the WHERE (that the
wiring belongs in `docs/prompts/v3/tools/` next to the regen tool it
extends); a one-line home pointer would have saved the survey pass — the
same guard-recipe discipline the .sessions README already asks for.

Documentation audit: the tool's contract, provenance, and no-third-copy
chain are homed in its module docstring (the durable home for v3 tooling,
regen_b_files precedent) + this card; the extraction contract itself lives
in kit-generated `docs/seat-digest.md` (kit-owned, travels at upgrade); no
docs/ide­as index exists to update in fm; claim deleted this commit.
