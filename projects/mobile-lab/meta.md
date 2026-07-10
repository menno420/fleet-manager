# mobile-lab — package meta

> **Status: PRE-BIRTH.** No repo, no Project, nothing deployed. A complete **held gen-2
> founding package exists** and is the only artifact. Repos verified NOT created:
> fleet-manager `control/status.md` @ `0eaa668` line 162 ("mobile-lab —
> ready-not-launched; repos NOT created (owner-gated)"); the 2026-07-10 full
> `list_repos` sweep (17 repos, inventory-games-new.md) found no mobile-lab repo; the
> package itself states "NO repo exists" up front.

## The held gen-2 package

**`fleet-manager docs/proposals/instructions/mobile-lab.md` @ `0eaa668`** — full
five-section gen-2 founding package (drafted 2026-07-10 from the fleet corpus review):

- §1 mission: fleet-status companion app (React Native + Expo) rendering the fleet's
  committed `control/status.md` heartbeats on the owner's phone; every milestone
  phone-verifiable by a non-coder; read-only window, **no fleet write path ever**.
- §2 Custom Instructions paste block (worker-instructions, paste-verbatim).
- §3 environment archetype assignment · §4 ORDER 001 draft · §5 divergences.
- Honest unknown named in the header: the classic `expo start` → LAN/tunnel QR loop is
  unverified behind the fleet proxy, so the package makes the **PWA/web-export-to-URL
  loop primary** and the native Expo Go loop a probe-once, owner-account-gated upgrade.

Provenance/gating: the source idea is **captured, not approved** (fleet-manager
`docs/ideas/mobile-lab-lane-2026-07-09.md`; README route: candidate SECOND gen-2 launch
after venture-lab), additionally gated on the spend-instrument discussion (per the
hub-side inventory, row 10 of `docs/proposals/instructions/README.md`'s table @
`0eaa668` era). mobile-lab never ran gen-1 — the owner's idea file IS its proposal.

## The 6-repo harness experiment (bundled ready-not-launched sibling)

The launch record bundles the two in one disposition — fleet-manager
`docs/planning/gen2-launch-record-2026-07-10.md` @ `0eaa668` § Dispositions:
"**mobile-lab + 6-repo harness experiment — ready-not-launched**: packages/prompts
committed and paste-ready; verified this morning that none of the `harness-exp-*` repos
exist (search: 0 results)."

Where the paste-ready material actually lives (the "SOMEWHERE" resolved):

- Design doc: **`fleet-manager docs/experiments/harness-x-model-2026-07-09.md`** @
  `0eaa668` — 3 pairs × 2 arms = 6 repos (`harness-exp-fable-u/p`,
  `harness-exp-opus-u/p`, `harness-exp-sonnet-u/p`), one product per model family
  (gba-play / brandkit / devlog), milestone ladders M1–M7.
- Paste-ready prompts: **`fleet-manager docs/experiments/prompts/pair-fable.md`,
  `pair-opus.md`, `pair-sonnet.md`** @ `0eaa668` — each carries the WRAPPER-U
  (ultracode session) and WRAPPER-P (Project boot) prompt blocks per arm.

Note: the harness experiment is a separate ready-not-launched item that shares
mobile-lab's launch state, not part of the mobile-lab lane itself — kept here because
the hub records them as one disposition line and both are owner-gated on repo creation.

## Launch prerequisites (if/when the owner greenlights)

1. **Re-base the held package onto the gen-3 born-continuous standard FIRST** — the
   Q-0262.6 hold is explicit: the 8 undeployed instruction packages (this one included)
   STAY undeployed until re-based on the manager's gen-3 blueprint delta. Target
   standard: superbot `docs/planning/gen3-deployment-standard-2026-07-10.md` @
   `dc19b1e8` (Q-0265-amended: born continuous, send_later pacemaker, cron =
   `"mobile-lab failsafe wake"`) + `round3-dispatch-part4-brief-2026-07-10.md` §2b
   failsafe-text template. The held package's session-shape/pacing text is gen-2
   (pre-Q-0265) by construction.
2. Owner creates the repo born-right per the gen-3 standard §2 (public, `main`;
   second settings touch after the kit-seed PR: auto-merge ON + required check).
3. Kit seed (substrate-kit, current release) + founding package from the gen-3
   template + env spec added to `fleet-manager environments/` (one env, named
   `mobile-lab`, single-repo attach per Q-0260).
4. The idea-approval + spend-instrument gates are owner/product decisions — this dir
   only records state; nothing here green-lights the launch.
