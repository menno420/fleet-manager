# Session — controller app follow-up: PS2 (DualShock) preset (Slice 19)

> **Status:** `complete`

📊 Model: fable-5 · high · feature build

Time: 2026-08-15 · venue: hub chat (same conversation as the Slice-18 session;
designated branch restarted from `main` per the merged-branch rule — #859 is
merged history and this PR is a new one)

💡 Session idea: owner, live: *"Improve the controller so it has a ps2 preset."*
Reading stated back: a DualShock-2 **starter template** ("preset" = the
New-layout template set, the app's own vocabulary since Slice 17) — glyph-colored
round △ ○ ✕ □ diamond, D-pad, both sticks center-low, four digital shoulders,
Start/Select; fully customizable; Slice 18's per-widget config applies.

## Previous-session review

Same-day state: #859 merged (`7aa4c22`) then main advanced under parallel
sessions to `196d582` (Railway consolidation #863, which also — correctly —
compressed this session's Slice-18 ledger entry to pointer weight for budget
room). product-forge at `6c33382` + Slice-19 branch; v0.18.0 released and
verified stable-signed.

## What this covers

pf #50 (v0.19.0, versionCode 17): the template in `CustomLayout.kt`
(`templateKinds` + `template("PS2 (DualShock)")` + the `ps()` glyph-button
helper), README feature + ladder lines. **Scope decisions (LOW, decided,
reasons on the pf card):** template not built-in pad · positional mapping
(✕=A ○=B □=X △=Y per the enum's BTN_* comments) · **no L3/R3** —
`GamepadButton` carries bits 0–11 only (`ComboHidDescriptor.kt:228-239`), and
adding stick-click bits is a descriptor revision that forces a re-pair on every
bonded host; deferred until asked for. **No HID descriptor change → v0.19.0
installs in place.**

fleet-manager records (this PR): Layer-2 app thread advanced to v0.19.0 (own
thread block replaced), current-state pointer entry widened to both slices
(net +6 words on a compressed entry), §7 row appended after pf #50 reaches its
terminal state.

Layer-2 handoff: docs/repos/product-forge/README.md — app thread updated

## Verification

pf: compile-check 102/22 green pre-push; Codex requested at PR-open + explicit
comment 04:54:38Z, parked `do-not-automerge` until answered; land on green;
tag `phone-controller-v0.19.0`; verify release asset + sha256 + stable-keystore
log line. fm: `python3 bootstrap.py check --strict` real exit code before the
flip.

## Result

- **pf #50 MERGED** — squash `3c462a6`; Codex two rounds, **4 findings,
  [conceded] ×4** (focus-chip collision · CIRCLE-as-oval, fixed app-wide with
  the inscribed-circle ButtonStyler change — the one flagged behavior change,
  hit-areas untouched · D-pad/stick overlap, geometry re-cut with all 13 rects
  proven pairwise disjoint by a one-off session script (NOT a committed test —
  binds the committed numbers only) · the overlay call site the "app-wide"
  claim missed, surfaced independently by the estate's owner-review hook and
  by Codex round 2, fixed in the flip commit under the stated two-round cap).
- **Release VERIFIED live:** tag `phone-controller-v0.19.0` at `3c462a6` →
  android-release completed:success → `phone-controller-0.19.0.apk`
  (2,459,817 bytes) + `.sha256` attached, job log prints **"signing: stable
  repo keystore"** at 05:09:57Z — installs in place over v0.18.0, no re-pair
  (no HID descriptor change).
- **§7 row appended** (chronological order restored after an insertion slip —
  caught and moved before commit); Layer-2 app thread at v0.19.0;
  current-state pointer widened to both slices.

⟲ Previous-session review: in the card body (§ Previous-session review).
Layer-2 handoff: docs/repos/product-forge/README.md — app thread updated
