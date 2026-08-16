# Session — controller app Slice 20: PS2 pad into the spinner (records)

> **Status:** `in-progress`

📊 Model: fable-5 · high · feature build

Time: 2026-08-16 · venue: hub chat (same conversation as Slices 18–19) ·
designated branch `claude/controller-app-customization-r7utv2`, restarted from
`origin/main` per the merged-branch rule (base `25c4733`)

💡 Session idea: owner screenshot of the layout spinner: *"It's not visible
here. Can you make it more easily accessible."* Slice 19 shipped PS2 as a
New-layout template only — his screenshot is the verdict on that scope call.

## Previous-session review

fm main at `25c4733` (a parallel session's records correction — durable-dump
home + backup-artifact flag). This conversation's prior state: pf #50 merged
`3c462a6` + v0.19.0 released (signer cert measured identical to v0.18.0);
fm #864 merged `766207c` with the L3/R3 premise correction.

## What this session did (product side, already terminal)

pf #51 squash `d5a412f`: "PS2 pad" as a directly selectable spinner row —
template-backed (`t:<kind>` key class beside `b:`/`c:`, spliced after NDS),
no create-and-save step; customization still routes through Layouts → New.
README: eleven ready-to-play layouts, the stale "Slices 1–18" counter unstuck.
Codex one round: **1 finding, [conceded] ×1** — the Settings-close refresh
enumeration missed `t:` (the #49 staleness class recurring at the same seam);
fixed in the flip commit. Pre-tag sweep check run both sides of the merge:
`git log 3c462a6..main` = exactly the #51 squash, nothing swept. Tag
`phone-controller-v0.20.0` at `d5a412f`.

## Records (this PR)

§7 row (2026-08-16) · Layer-2 app thread → v0.20.0, with the enumeration→
unconditional-refresh refactor recorded as the NEXT SLICE's first item (the
owner-review hook pushed on the fragility; the bug has recurred once along
exactly that seam, #49 → #51) · current-state pointer widened to Slices 18–20
· MEASURED stamp refreshed.

Layer-2 handoff: docs/repos/product-forge/README.md — app thread updated

## Result

- **pf #51 MERGED** squash `d5a412f`; tag `phone-controller-v0.20.0` at that
  SHA; **release VERIFIED live**: android-release completed:success,
  `phone-controller-0.20.0.apk` (2,461,913 bytes) + `.sha256` attached, and the
  **signer certificate parsed from the v2 APK Signing Block is byte-identical
  to v0.19.0's** (sha256 `7bda3340…` both) — in-place install measured at the
  certificate level, the same check as v0.19.0.
- Pre-tag sweep run both sides of the merge: the tag range holds exactly the
  #51 squash.
- Records in this PR per § Records; the force-push restart of this designated
  branch was tree-verified against the git-state guard's three flagged paths
  (all IDENTICAL to origin/main — the discarded tip was fully squash-merged).
