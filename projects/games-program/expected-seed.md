# games-program — expected seed (pre-birth checklist, ×3 repos)

Modeled on how **product-forge's** pre-birth → seed → boot worked (repo created
born-right by the owner, kit-seeded the same day, founding package §0–§4 in superbot
planning, env spec in fleet-manager `environments/`, coordinator booted from the §2
brief). Sources: superbot `docs/planning/gen3-deployment-standard-2026-07-10.md` @
`dc19b1e8` (§2 standards, §3 pipeline, Q-0265-amended operating model) ·
`round3-founding-package-simulator-2026-07-10.md` (the born-continuous-native reference
package) · `round3-dispatch-part4-brief-2026-07-10.md` §2b (failsafe-text template) ·
fleet-manager `environments/` @ `0eaa668`.

Games repos are **post-core lanes** → the gen-3 standard's *pipelined* fast path
applies (Q-0261's one-at-a-time finalize-first rule bound only the core-6).

## Step 0 — mapping (BLOCKS everything; DECIDE-AND-FLAG)

The manager's Q-0259-r5 mapping proposal names the 3 repos (see meta.md: likely
pokemon-mod-lab = Emerald/QoL+ per Q-0262.7, gba-homebrew = second, third TBN).
Until it exists, no repo create, no package draft is final. Flag on the run report;
owner veto window; then proceed.

## Per repo — the checklist

### 1. Repo (owner click; only for the TBN third — the other two exist)
- Create **public**, default branch `main` (gen-3 §2; pokemon-mod-lab keeps its
  pokemon-class PRIVATE exception → stays attached to the manager env, Q-0260.3).
- Second settings touch AFTER the seed PR's CI runs: **Allow auto-merge ON** +
  **required check = the seed's named check (`substrate-gate`)**. The boot ⚑
  OWNER-ACTION names the exact check (product-forge precedent).

### 2. Kit seed (agent work)
- New repo: seed from **substrate-kit at its current release** (v1.7.0 was current at
  inventory time — verify at HEAD; product-forge/sim-lab seeds are the exemplars):
  CONSTITUTION.md · CONVENTIONS.md · PLATFORM-LIMITS.md ·
  control/{README,inbox,status}.md · bootstrap.py + substrate.config.json +
  `.github/workflows/substrate-gate.yml` · claims/ · review-queue.md · docs set
  (CAPABILITIES, AGENT_ORIENTATION, owner-profile, question-router) ·
  `.sessions/<date>-seed.md` seed card.
- Existing repos: **kit upgrade path instead of fresh seed** — gba-homebrew already
  v1.7.0; pokemon-mod-lab is v1.6.0 with an UNRENDERED staged
  `.substrate/claude/CLAUDE.md` (needs upgrade + render). Carry their existing
  control/ history; do not wipe.
- Reconcile stale orders at first boot: the unexecuted **ORDER 002 hourly-self-arm**
  texts in both existing inboxes are superseded by Q-0265 — record superseded, never
  execute. pokemon-mod-lab additionally executes/inherits **ORDER 003
  (visibility=private verify)** as a standing rail.

### 3. Founding package (agent drafts; gen-3 born-continuous template — NOT the held
### gen-2 game-lab texts, per the Q-0262.6 hold)
Model: the **simulator package** (born continuous natively). Four sections per repo:
- **§0 owner pre-clicks** — repo create (if new) / settings touch / Project create /
  env select / package §1+§2 pastes.
- **§1 Custom Instructions** (≤7,500 chars, paste-verbatim): who the Project's agents
  are + the ONE repo (Q-0260) · doctrine-pointer (never restate ceremony) ·
  typical-tasks · reporting bar (**family model names only**, per the Q-0262.4 policy;
  cite commits/PRs; negatives are headlines) · **session shape = continuous work loop
  per Q-0265** (HEAD-first, slice after slice merged-on-green, heartbeat-last,
  decide-and-flag, walls quoted verbatim + probe-once-per-seat) · the game mandate
  line from Q-0259 r5 (continuously improve / invent / mod; **present a few options
  wherever wise rather than asking**; owner plays post-EAP).
- **§2 coordinator chat brief**: mission + done-when · durable-twin pointer · numbered
  BOOT-NOW list ending in **ARM YOUR FAILSAFE** with exact `create_trigger` args —
  name `"<repo> failsafe wake"`, lane cron `0 */2 * * *` (keep the fleet stagger;
  coordinate the 3 lanes' offsets vs idea-engine/sim-lab's even/odd coupling) — plus
  the verbatim `FAILSAFE WAKE (<seat>, Q-0265): …` prompt from part4-brief §2b, the
  send_later continuation-chain arm, and the **owner-manual fallback block if the seat
  lacks the scheduler tools** (sim-lab precedent: `create_trigger`/`send_later` absent
  on a seat is a real, seat-dependent wall — the failsafe TEXT must be committed in
  the package, never chat-only) · known-platform-facts block (gba-lab walls: devkitPro
  Cloudflare-403 → leseratte10 mirror, pinned devkitARM r68/Butano 21.7.1) ·
  **calibration ask** (mission back in one paragraph + concrete first moves + routine
  name/cadence).
- **§4 boot verification**: calibration reviewed → trigger in registry via
  `list_triggers` with exact name/cron (**never wait for the first fire as proof**) →
  boot PR merged + heartbeat at HEAD verified against git → runbook/log tick.

### 4. Environment (agent drafts spec; owner pastes — agents cannot create envs)
- One env per repo, **named exactly like the repo**, single repo attached (Q-0260).
- Setup script = fleet archetype **verbatim**: `archetype-gba-lab.sh` for the two GBA
  repos; the third's archetype depends on its concept (default `python-lab` unless the
  mapping says otherwise). Add each spec to **fleet-manager `environments/`** (the
  registry README's proposal form; no secret values).
- pokemon-mod-lab privacy rider: manager env must have it attached or staleness sweeps
  read DARK-by-privacy (Q-0260.3).

### 5. First orders (manager)
- Project 1: boot straight into the Q-0262.7 QoL+ concept (12-patch foundation).
- Project 2: concept pick still open — first order = present the owner a few options
  (the r5 instruction pattern) and proceed decide-and-flag.
- Project 3: mandate-shaping order from the mapping proposal.

## Divergences from product-forge's seed (recorded so they're deliberate)
- product-forge was **core-6 finalize-first**; these are post-core → pipelined boots,
  all three in one paste wave, are fine (gen-3 §3).
- product-forge's package §2 was written pre-/at-Q-0265 (2-hourly standing wake) and
  needed the §2b amendment paste; these three are **born continuous natively** — write
  them from the simulator package's shape so no amendment paste is ever needed.
- Two of three repos are brownfield (history + parked ⚑s + stale ORDERs) — the seed
  step is upgrade-and-reconcile, not greenfield.
