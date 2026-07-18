# Idea routing — 2026-07-18 (verified)

> **Status:** `living-ledger`

*The verified routing record for the Ideas-Lab (sim-lab ↔ idea-engine) verdict mine, produced by
the fm overnight-oversight seat 2026-07-18. Every routed candidate is a real sim verdict whose
target lane, first slice, and verification are named below. **Oversight-only:** recorded here for
the recreated manager / lanes to pick up (per-lane seeding or owner fan-out once lanes are live) —
**not pushed to any target repo** (the ORDER relay is retired and fleet-manager writes only
itself).*

## Provenance (live HEADs — reviewer citations were stale)

- **sim-lab** live HEAD `278d3ae` (the reviewer's routing pass cited stale `3858064`).
- **idea-engine** live HEAD `16b7a2c` (the reviewer cited stale `945135a`). **idea-engine is a
  FROZEN ARCHIVE** per its ORDER 014 — it is a finished mine, not an active writer; routing pulls
  from its committed verdicts, nothing is written back to it.
- Verdict bodies live at `sims/verdict-NNN-<slug>/README.md` in sim-lab.
- **Confidence tiers below:** **CONFIRMED APPROVE** = the verdict was spot-checked against its
  sim README this pass (V010, V012, V018). Everything else is a **reviewer-vetted LEAD** — the
  cited verdict is credible but the lane MUST re-verify it against the live sim README before
  building (Q-0120: verify against source, never against report text).
- **Highest-leverage (reviewer):** **A**, **C+D**, **F**.

## Custody caveat

The ORDER relay is retired and fleet-manager writes only its own repo, so nothing here is pushed to
the target repos. This doc is the hand-off surface: the recreated per-lane seats (or the owner via
a fan-out) pick up the slice for their repo when the lane is live.

## Primary candidates (A–H)

| # | Idea → target repo | Sim verdict | First slice | Verification |
|---|---|---|---|---|
| **A** | Settle-once architecture / economy guard → **superbot-next** | **V010 APPROVE (CONFIRMED)** | superbot one-liner: `roots += "cogs/"` at `check_consistency.py:1151`, then a warn-only `check_settle_once.py` over the atomic-escrow contract | checker runs warn-only first; flips to RED once the tree is clean |
| **B** | `check_doc_cites.py` citation linter → **superbot-next** | **V012 APPROVE (CONFIRMED)** | ~100-line stdlib linter, warn-only first | missing-file → RED once clean |
| **C** | Heartbeat-contradiction linter + "one fact, one home" → **substrate-kit** | V015 (LEAD) | linter that flags a heartbeat fact asserted in >1 home | re-verify V015 vs its sim README first |
| **D** | Backlog low-water signal (`"backlog: low (N)"`) → **substrate-kit** | V021 (LEAD) | emit a low-water line when the idea backlog can't fill the next band | re-verify V021 first |
| **E** | Snapshot stale badge (180s) → **superbot-mineverse** | V056 (LEAD) | badge the served snapshot stale once it is >180s old | re-verify V056 first |
| **F** | Encounter coexistence cooldown contract → **superbot** | **V018 APPROVE (CONFIRMED)** | WINNER **C-cap-4**: combined per-player cap **K=4** over a sliding **3600s** window, atomic-with-claim, landed **BEFORE** the Encounters cog exists | per-source clocks alone leak **8.875/hr** — the combined cap is the guard |
| **G** | Idle-economy 7-param table → **superbot-idle** | V006 (LEAD) | the 7-parameter economy table as a single tuned source | re-verify V006 first |
| **H** | Gloamline best-nights record → **gba-homebrew** | V050 (LEAD) | record the best-nights table — explicitly **NOT** the unjustified "dark edges spawn faster" lever | re-verify V050 first |

## EASY-WIN (reviewer emphasis — take on its own)

**superbot `check_consistency.py:1151` — `roots += "cogs/"`.** A contained, reversible **one-liner**
(part of candidate A / V010) that repairs an **already-shipped but silently-inert** scope-widening:
the `cogs/` root was meant to be in scope and isn't, so the check has been passing vacuously over
that tree. Worth taking **on its own** even if the superbot lane does not take the full settle-once
slice.

## Secondary (doc-cite-only LEADs)

- **V054** → gba-homebrew
- **V057 / V073 / V099** → venture-lab
- **V100** → superbot-games

Each is a doc-citation-strength LEAD only — re-verify the verdict against its sim README before any
lane builds on it.
