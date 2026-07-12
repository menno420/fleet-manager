# 2026-07-12 — seat-digest regen wiring (grounded-skills slice 6, fm side)

> **Status:** `in-progress`

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
