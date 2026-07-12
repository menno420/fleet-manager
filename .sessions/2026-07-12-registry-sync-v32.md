# 2026-07-12 — registry sync: projects/ seat files to prompts v3.2

> **Status:** `in-progress`

📊 Model: fable-5 · start 2026-07-12 ·
lane worker (owner-directed 2026-07-12, dispatched by coordinator)

## Declared at open (born-red)

The projects/<seat>/ REGISTRY copies are stale — last synced by restructure
PR #89, which predates the overnight prompt rebuild (docs/prompts/v3, now
generation v3.2 stateless, PR #108). This session: for each of the 8 seats
(fleet-manager, superbot-2.0, websites, self-improvement, superbot-world,
game-lab, ideas-lab, venture-lab) regenerate coordinator-prompt.md /
instructions.md / failsafe-prompt.md from their docs/prompts/v3 sources
(regenerate-don't-fork, provenance headers, version bumps per each file's
own convention); minimal projects/README.md pointer update; ship a
--check-registry drift guard next to regen_b_files.py; close out + heartbeat.

## Close-out

Shipped on fm PR #110:

- **All 8 seats × 3 registry files regenerated** from `docs/prompts/v3` @
  `6391b2f1f91b45cba6864693abe700cc5f9aaaca` (owner-directed rebuild
  2026-07-11/12), mapping seat → source: fleet-manager ←
  `fleet-manager-startup.md` · superbot-2.0 ← `superbot-startup.md` ·
  websites ← `websites-startup.md` · self-improvement ←
  `self-improvement-startup.md` · superbot-world ←
  `superbot-world-startup.md` · game-lab ← `game-lab-startup.md` ·
  ideas-lab ← `ideas-lab-startup.md` · venture-lab ←
  `venture-lab-startup.md`. Zero unmappable seats.
- **coordinator-prompt.md** = the seat's v3.2 startup B file VERBATIM below a
  GENERATED-COPY header (source of truth = docs/prompts/v3; version bumps per
  each file's own lineage: fm v3→v4, websites coord v3→v4, venture coord
  v2→v3, all new-seat files v1→v2).
- **instructions.md** = the assembled Custom Instructions paste per the v3.2
  README recipe (core v3.1 lines 1–2 SEAT_NAME-filled + seat C block + core
  remainder STATUS_GRAMMAR-filled). Char counts (fleet budget basis =
  characters, README-table-consistent at +2 separator newlines): fm 7,974 ·
  superbot-2.0 7,996 · websites 7,945 · self-improvement 7,994 ·
  superbot-world 7,999 · game-lab 7,986 · ideas-lab 7,994 · venture-lab
  8,000 — **all ≤ 8,000; none trimmed**. NOTE, stated not hidden: raw UTF-8
  `wc -c` BYTE counts run 8,052–8,111 (multibyte · — ⚠ →) — a property of
  the whole v3.1/v3.2 generation, not this sync; the fleet's verified-wall
  accounting (core file + README table) counts characters.
- **failsafe-prompt.md** = A step-3a FAILSAFE WAKE text (D-2 single source,
  extracted from universal-startup.md at generation time) + the seat's D-7
  stagger-table cron; the table supersedes pre-rebuild crons in the old
  superbot-world (`20 */2`→`15 1-23/2`), game-lab (`50 */2`→`15 */2`) and
  websites (fresh-session model → uniform v3.2 self-bind) copies.
- **Drift guard:** `regen_b_files.py` gained `--write-registry` /
  `--check-registry` (header-insensitive body diff vs the v3 sources;
  exit 0 verified on this tree; default B-regen mode unchanged and
  idempotent). Gate wiring NOT done: substrate-gate.yml is KIT-OWNED (no
  extension point) — follow-up = a sibling workflow per the
  roster-freshness.yml pattern.
- `projects/README.md`: slice-3 banner note + paste-wave supersession
  pointer; MATRIX left historical as its banner already declares.

## 💡 Session idea

Wire `--check-registry` into CI as a sibling workflow (the
roster-freshness.yml pattern exists precisely because substrate-gate.yml is
kit-owned): a ~15-line `registry-drift.yml` running the check on PRs touching
`projects/**` or `docs/prompts/v3/**` would make the D-1/D-9 discipline
enforcing for the registry copies the owner actually reads — today the guard
only fires when someone remembers to run it.

## ⟲ Previous-session review

The v3.2 stateless session (PR #108) left an unusually clean handoff: the
regen script's seat configs carried every fill this sync needed (SEAT_NAME,
CRON_STAGGER, OLD_TRIGGER_SOURCES), so the registry generation could be
derived 100% from committed sources with zero hand-authored prompt text.
Miss: it rebuilt the v3 home but left the projects/ registry — the surface
the owner actually reads — serving pre-rebuild text for a day, with no
tracking artifact saying so. Improvement: a generation bump in docs/prompts/
should ship with (or immediately file an ORDER for) the registry re-sync,
and now the `--check-registry` guard makes that drift visible mechanically.
