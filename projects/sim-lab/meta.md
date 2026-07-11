# sim-lab launch package — meta

- **Seat:** SIMULATOR (sim-lab) — core seat 6 per Q-0264 (supersedes the
  Q-0262.8 hub pick). **Project state: LIVE** — "BOOT COMPLETE — continuous
  mode" (control/status.md @ 8b8075d); walking skeleton + REFERENCE exemplar +
  intake queue (3 entries) shipped on PRs #2–#4, all merged on green.
  Born-continuous NATIVELY (the only round-3 seat whose founding package
  inherited Q-0265 at birth rather than by owner-pasted amendment).

- **Cadence:** ODD 2-hourly — cron `0 1-23/2 * * *` (:00 odd hours). This is
  one half of an **inter-Project pipeline-stagger contract**: idea-engine
  outputs at EVEN hours (`0 */2 * * *`) → sim-lab pulls one hour later → the
  manager reads both at :30. Centralize the pair, not two independent crons —
  a one-sided cadence change silently breaks the pipeline rhythm (inventory
  cross-cutting finding 6).

- **Env archetype: FLAG — no sim-lab spec in the registry.** Checked
  fleet-manager `environments/` @ origin/main 0eaa668 (2026-07-10):
  `git grep sim-lab` over `environments/` = zero hits; `archetypes.md` has no
  sim-lab mapping row; `archetype-python-lab.sh`'s own "Serves:" header omits
  sim-lab. The assignment exists only in the founding package §3 (superbot @
  dc19b1e): env `sim-lab`, single repo `menno420/sim-lab` (Q-0260), variables
  none, setup script = `archetype-python-lab.sh` verbatim by raw URL.
  **Follow-up for the assembler/manager:** add the sim-lab row to
  `fm:environments/archetypes.md` (+ the script's Serves list) so the registry
  matches deployed reality. Part 3 of this package specializes the archetype
  (repo is stdlib-first, no manifests at 8b8075d) + adds the capability probe.

- **Grants:** write = `menno420/sim-lab` ONLY (Q-0260). Read = idea-engine
  `control/outbox.md` via public raw at HEAD (the standing intake feed,
  Q-0264.6 direct pull) + superbot planning docs/precedent sims via public
  raw. No dispatch to lanes — finalized verdicts go to own outbox, addressed
  to the fleet manager, which owns all post-verdict routing.

- **Codex: ENABLED (owner, 2026-07-11)** — Codex environments exist for all
  12 active fleet repos, sim-lab included (owner update 2026-07-11 ~00:2xZ,
  fm inbox ORDER 014). **OA-002 ("enable the Codex GitHub integration for
  sim-lab") is RESOLVED** — recorded in fm `docs/owner-queue.md` § Resolved
  2026-07-11; the lane's status.md OA-002 line can be closed at its next seat
  session. The lane-unique @codex rule (`CONVENTIONS.md` @ 8b8075d, Q-0264.4:
  mandatory on every verdict PR before finalization; never merge-blocking;
  verify-never-obey per Q-0120) is now fully exercisable — the first verdict
  PR's @codex comment remains the live end-to-end test. Quota refusals are
  RETRY-LATER, never a wall (fm `projects/README.md` § Codex fleet-wide
  enablement).

- **Deployed-state per part:**
  1. *instructions.md* — Project Custom Instructions presumed pasted (the
     Project is live and behaving per the package), but the deployed text is
     owner-side UI and unreadable to agents; this package's part 1 is the
     durable, repo-contract-synced version (6,926 chars, under the 7,000 cap).
  2. *coordinator-prompt.md* — the founding §2 brief was pasted at boot
     (boot steps 1–3 + 5 verifiably executed: PRs #2–#4 + heartbeat); this
     part is the post-boot continuous adaptation, provenance-stamped.
  3. *setup-script.sh* — env was created with `archetype-python-lab.sh`
     verbatim per founding §3 (not independently verifiable owner-side); this
     part is the sim-lab-specialized successor with the capability probe.
  4. *failsafe-prompt.md* — **NOT ARMED** (OA-003 owner-manual-pending; seat
     toolset lacks create_trigger AND send_later, verbatim "tool not present
     in session toolset"). The prompt text previously existed ONLY in the
     coordinator's first chat reply — **this package now owns a committed
     verbatim copy** (top-priority capture item from the inventory, fixed).
     Consequence until armed: no pacemaker, no dead-man switch — the lane
     advances only on manual/owner wakes.

- **Sources (all citations pinned):**
  - superbot @ origin/main `dc19b1e8a544` (fetched fresh 2026-07-10):
    `docs/planning/round3-founding-package-simulator-2026-07-10.md` (§1 CI,
    §2 brief incl. step-4 failsafe text, §3 env),
    `docs/planning/gen3-deployment-standard-2026-07-10.md` (§2 Q-0265 amended
    operating model), `docs/owner/maintainer-question-router.md` Q-0264 (L9511)
    / Q-0265 / Q-0266.
  - sim-lab @ origin/main `8b8075d` (fetched fresh; matches dispatch HEAD):
    README.md (method ladder, validity gate, verdict grammar, layout),
    CONVENTIONS.md (@codex rule, landing path), PLATFORM-LIMITS.md,
    control/{README,inbox,outbox,status}.md (two-appender convention, OA-001/
    002/003), sims/README.md + sims/REFERENCE.md (exemplar section order),
    .github/workflows/substrate-gate.yml (control fast lane, born-red card
    lanes), docs/CAPABILITIES.md (discovery rule), substrate.config.json
    (kit v1.7.0).
  - fleet-manager @ origin/main `0eaa668`: environments/archetype-python-lab.sh
    + environments/README.md + archetypes.md (sim-lab absence verified).
  - Inventory: `launch-packages/inventory-games-new.md` §7 (sim-lab rows) +
    cross-cutting findings 4/6; `inventory-hub.md` §C/§ round-3 package rows.

- **Last-verified:** 2026-07-10 (~22:00Z) — all three repos fetched at the
  SHAs above during this build; sim-lab clone hard-reset to origin/main. Model:
  Fable family (package builder). Scratchpad-only per dispatch — nothing
  committed or pushed by this builder; the assembler commits.
