# Session — controller app: repo question answered + Slice 18 built in product-forge

> **Status:** `in-progress`

📊 Model: fable-5 · high · product work under live owner directive

Time: 2026-08-14 · venue: hub chat (booted in fleet-manager, product-forge
attached mid-session — the Slice-4 precedent) · designated branch:
`claude/controller-app-customization-r7utv2`

💡 Session idea: owner, live: orient, look at product-forge's controller app,
answer *"new repo or continue in this repo?"*, then *"further improve it this
session, make it more customizable etc."* OD-13 deprioritizes product work as the
default pick; his live directive selects it for this session (named, per
intent.md § 6 — product work was never blocked).

## Previous-session review

fleet-manager at `108b452`: v1.21.0 rollout phase 3 complete 5/5 (gba unblocked
via owner bypass, program §7 2026-08-14 row). NOW unchanged: E1 owner-reserved,
D2 target open at `OQ-FM-D2-TARGET`, OD-13 standing. product-forge untouched
since Slice 17 (2026-07-24, `81b65bd`).

## What this session did

1. **Six-read cold orientation** — clean; boot diagnostic case one.
2. **Intake intent map** (skill fired per the routing table) — INTENT STATUS:
   RESOLVED; the repo question's destination was already owner-decided (program
   §2 + R2 + the incubator mechanic), only timing was open (MEDIUM,
   decided-and-flagged: graduation is its own next step, not this session's).
3. **Slice 18 in product-forge** (PR #49, v0.18.0): per-widget behavior config,
   long-press alternates, fine position sliders, backup/restore-everything +
   `compile-check.sh` (the no-SDK app compile proof, committed). Fixed en route:
   custom-layout touchpads never received global sensitivity/scroll-invert.
4. **Layer-2 folder `docs/repos/product-forge/`** created on demand (README
   only; depth files honestly not-yet-written): the repo answer, the app thread,
   and the R2 graduation recipe with the measured keystore constraint (stable
   keystore lives ONLY in repo secrets — values unreadable agent-side; three
   carry options recorded, fresh-keystore-plus-backup recommended now that
   Slice 18 makes a signature break costless).

## Verification

product-forge: JVM suites 59/59 · Python 26/26 · compile-check 100 classes / 22
files · gate exit 0 · Codex review awaited before merge (estate rule beats the
seat-era merge-anyway convention) · release verified on the tag with sha256.
fleet-manager: `python3 bootstrap.py check --strict` real exit code before push.

Layer-2 handoff: docs/repos/product-forge/README.md — repo-question + graduation
threads created

## Honest flag — orientation budget

`orientation-budget` fires at **7042/7000 words** on this branch (exit-neutral).
Baseline at HEAD was ~6980 — the ledger's preserved tail, not this session,
holds the budget hostage: my Recently-shipped entry is 62 words and the file
carries ~4400 words of pre-2026-07-19 seat-era entries below its own
"preserved, not current" banner. Left flagged, not contorted around and not
suppressed: the durable fix is an OD-3-amended archive pass over that tail
(move to a dated archive file, pointer left behind) — a records cleanup that
deserves its own decided-and-flagged pass, not a rider on a product slice.

## Result

*(fill at close: PR #49 terminal state, release link, records landed)*
