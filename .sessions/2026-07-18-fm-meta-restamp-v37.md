# Session — fm-meta-restamp-v37

> **Status:** `complete`

**Branch:** `claude/fm-meta-restamp-v37-0718`

📊 Model: Opus 4.8 · medium · docs-only

**About to do:** Restamp the 9 `projects/<seat>/meta.md` registry files to a
parseable, current-dated (2026-07-18) v3.7 Deployed-state table so the websites
control-plane `/prompts` fleet-prompt-state panel's "8 stale" count clears to
`unverified`; record the genuine Class-A owner re-paste residue (fleet-manager,
websites, curious-research) and the machine-readable-self-heal design gap in
`docs/fleet-triage.md`.

**Did:**
- **Restamped all 9 standing-seat `projects/<seat>/meta.md`** to a parseable
  `## Deployed-state per part (2026-07-18)` heading + `| Part | State |` table.
  Each Custom-Instructions and coordinator-prompt claim now starts with a `v3.7`
  token dated `2026-07-18` and carries **none** of `v1`/`v2`/`gen-2`/`v1-era`/
  `pre-v3` — the exact conditions the websites `app/prompts.py` parser needs to
  render both rows `unverified` instead of `stale`. **Verified against the live
  parser** (imported `_parse_meta_table` / `_meta_claim` / `_meta_verdict` from
  `websites app/prompts.py`, canonical date 2026-07-15): all 9 seats × both rows
  → `unverified`, zero `stale`. The panel's **"8 stale" count clears.**
- **Class handling (honest, Q-0120 — no false repo-verified sync):**
  - **Class A (older owner paste deployed → owner re-paste is the self-heal
    item): fleet-manager, websites, curious-research** — claim
    `registry-current; owner re-paste to v3.7 ... (not repo-verified)`.
  - **Class B (never console-pasted; registry IS the deployed artifact):
    venture-lab, superbot-world, superbot-2.0, ideas-lab, game-lab,
    self-improvement** — claim `registry-current; never console-pasted`.
- **Bumped each file's top HTML stamp** to
  `<!-- v3.7 · 2026-07-18 · fleet-manager projects registry -->` per
  `projects/README.md` §Doctrine 3 (the 5 slice-1 seats bumped from `v1`;
  fleet-manager / websites / venture-lab / curious-research had none → inserted).
  Prior per-part deployment detail preserved verbatim as a historical
  `<details>` block; no other prose touched.
- **Recorded the residue + design gap** in `docs/fleet-triage.md` under a dated
  `## 2026-07-18 · registry meta.md restamp` note: the 3 Class-A seats owe an
  owner re-paste (owner-only self-heal, per seat) so their row honestly stays
  `unverified`; the 6 Class-B seats owe no paste. **Gap flagged:** no
  machine-readable "self-heal / seats stamp their own deployed version" channel
  exists — only the manager-written quote-on-demand version-stamp doctrine
  (`projects/README.md` §Doctrine 2–3); a byte-verifiable *deployed-stamp*
  channel for CI/coordinator artifacts does not exist (only the failsafe trigger
  snapshot is byte-verifiable). Recommended to the owner as a design gap.
- **Checks green:** `check_no_false_walls.py` CLEAN EXIT=0 (5 docs);
  `check_owner_queue.py` CLEAN EXIT=0; `check_docs_links.py` CLEAN (256 files);
  `bootstrap.py check --strict` EXIT=0 after this flip (the only prior red was
  this card's born-red HOLD). The pre-existing `seat-digest-stale` advisory is
  explicitly never-exit-affecting and out of this docs-only session's scope.
  Guard-fire delta staged, not reverted.

⚑ Self-initiated: None — directed deliverable (owner-relayed panel-staleness
restamp task). Docs/registry-only pass in this repo; no trigger created,
modified, fired, or deleted; no cross-repo write (the residue + design-gap are
recorded here for the hub/owner, not pushed to sibling repos).

💡 Session idea: **A `check_registry_meta_stamp.py` drift guard that mirrors the
websites `/prompts` panel's stale rule locally in fleet-manager.** The panel's
"N stale" count is only visible from the *websites* control-plane; the hub that
OWNS `projects/` has no local detector that a seat's `meta.md` Deployed-state
table has slipped below the canonical version/date or reintroduced a
`v1`/`v2`/`gen-2` token. A stdlib checker parsing each `projects/<seat>/meta.md`
for the `## Deployed-state per part` table and applying the same verdict
(`stale` when claim date < canonical or a pre-v3 token appears) would let the
manager catch panel-staleness *before* a sibling's rendered banner surfaces it —
the same "detect it at the hub, not from a downstream page" axis as the
snapshot-seat-coverage idea the prior session raised. Dedup-checked
`docs/ideas/` — no registry-meta-stamp guard present; novel. Reliability caveat:
canonical version/date would need a single source (a `projects/README.md`
constant or a small `canonical.json`), so ship advisory-only with a kill-switch,
same tier as the other convenience guards.

⟲ Previous-session review: **`.sessions/2026-07-18-fm-websites-custody-snapshot.md`**
(the triggers-snapshot refresh) did its custody job precisely — it cleared the
websites `/prompts` "no failsafe trigger" drift row at its true source (the
committed snapshot) rather than papering over it, and it was rigorously honest
about the v3.7 stamp being *inference, not repo-verified*, which is the exact
Q-0120 discipline this restamp task also had to hold (I likewise wrote every
Class-A claim as `not repo-verified`). What it could have done better ties
directly to this session: it noted the v3.7 stamp was unverified but left the
per-seat `meta.md` Deployed-state tables carrying pre-v3 / older-dated claims —
so the panel's *other* staleness axis (the meta.md prose rows) stayed red and
needed this whole follow-up. Workflow improvement it surfaces: the two panel
inputs (snapshot freshness + meta.md table currency) are maintained by separate
sessions with no shared checklist, so a custody pass can green one axis and
leave the other red without noticing. The `check_registry_meta_stamp.py` idea
above is the concrete fix — a single hub-side guard covering the meta.md axis so
it can't silently lag the snapshot axis again.
