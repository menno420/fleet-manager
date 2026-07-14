# 2026-07-14 — kit upgrade v1.15.0 → v1.16.0

> **Status:** `complete`

- **📊 Model:** fable-5 · medium · mechanical refactor — kit upgrade distribution

about to do (as opened): upgrade the substrate-kit vendored engine from v1.15.0 to v1.16.0 using the canonical two-command recipe (stage verified release asset as `bootstrap.py.new` + `release.json` → `python3 bootstrap.py.new upgrade` → `python3 bootstrap.py upgrade --apply-docs` → `check --strict`). Scope rails per Q-0261.3.

Provenance: substrate-kit v1.16.0 distribution wave (per-adopter worker; asset sha256 bba34e2102cbaf09394f39992f0501ea5cfd542d90301ef67e31a0854ca59170, 980026 bytes, release.json adjacent).

## Work record (PR #202)

- Asset three-way sha256 verified (downloaded == release.json field == coordinator-stated `bba34e21…9170`, 980,026 B, first-try clean download).
- Two-command upgrade complete: `bootstrap.py.new upgrade` then `bootstrap.py upgrade --apply-docs`; report carries the `## Applied (--apply-docs)` section (CONSTITUTION.md, docs/collaboration-model.md, docs/ROUTINES.md, control/claims/README.md — all template-improved, consumer-untouched).
- Banked exactly one new `.substrate/backup/bootstrap-1.15.0.py` (sha256 25d22af9… = the v1.15.0 asset); all pre-existing banks byte-identical. Carve-out scan: `.github/workflows/substrate-gate.yml — ran, 0 found`; live gate kept (kit-owned, already current). capability-seed and seat-digest both "already current".
- NEW v1.16.0 plant `docs/reading-path.md` shipped with an adopt-time UNRENDERED banner (3 unfilled slots) AND as a `[reachable]` orphan — both strict-red. Cures: answered `fleet_dark_repos` / `fleet_status_command` / `fleet_siblings` from tree truth (pokemon-mod-lab private wall; docs/roster.md as the generated one-command orient + sibling map, regenerate-don't-restate) then `render --live`; minimal wiring hunk hand-merged into the diverged docs/AGENT_ORIENTATION.md (planted-doc-set line + reading-path routing paragraph — the standing fm minimal-hunk pattern, #114/#123 precedent).
- Verification: `python3 bootstrap.py check --strict` — green apart from the DESIGNED born-red hold on this card (flips with this commit); repo checkers green (roster freshness OK · owner queue CLEAN · trigger health PASS 9/9); no live CLAUDE.md verify line exists here.
- Lane-owed (untouched per Q-0261.3): heartbeat `kit:` bump in control/status.md (chronic); docs/CAPABILITIES.md diverged delta (master-copy path casing `docs/capabilities.md` → `docs/CAPABILITIES.md`); the rest of the docs/AGENT_ORIENTATION.md template delta beyond the wired hunks (nothing remains — the v1.16.0 delta was exactly the reading-path wiring, both hunks applied); 10 pre-existing `.sessions/` cards carry advisory `model-line-shape` warnings under the new v1.16.0 lint (never exit-affecting — backfill candidate for the lane).

💡 Session idea: the v1.16.0 `docs/reading-path.md` plant lands strict-red-by-design on every adopter (unrendered banner + orphan) — the kit's upgrade path could pre-answer derivable slots (dark repos are knowable from the currency scanner; the orphan wiring is the same AGENT_ORIENTATION hunk every time) or at least downgrade the fresh-plant banner to advisory for one release, so a distribution wave doesn't need per-repo hand-answers to keep the mandatory strict gate green.

⟲ Previous-session review: the walkthrough-sweep session (PR #198) reconciled three straggler-state surfaces into one audit-collection column — good single-surface instinct, and its card's verification section made this session's baseline trivially checkable. Its miss, visible under the new v1.16.0 lint: its `📊 Model:` line (like 9 sibling cards) lacks the three-field payload, so the telemetry harvest records nothing from it. Concrete improvement: one docs-only pass backfilling the 10 flagged cards to the taught `- **📊 Model:** <model> · <effort> · <task-class>` form would make the fm telemetry lane harvestable back to 2026-07-14.
