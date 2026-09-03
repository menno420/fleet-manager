# 2026-09-03 — records only: one stale cross-reference in the review-site prompt

> **Status:** `complete` — the review-site continuation prompt's
> first step said "READ FIRST item 3 — the ten-page cold read" after Codex
> round 3 of fm #1014 had moved the cold read to item 2; found while pasting
> the prompt to the owner. One line. Tier 3 (records only, under the
> thresholds), no Codex round owed.

- **📊 Model:** fable-5 · xhigh · review/verify
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01DSyapUpawGhaW1vThaQEvJ](https://claude.ai/code/session_01DSyapUpawGhaW1vThaQEvJ) · "Fleet manager 2026-09-02 review"

## Mission

Fix the one stale cross-reference; nothing else. **Why a third PR from one
session (D-0024 exception, stated):** the defect is in a prompt that landed
minutes earlier and the owner is about to paste it.

## Verify

`python3 bootstrap.py check --strict` — exit 0 after the flip.

⚑ decide-and-flag: none. 💡 Session idea: none. ⟲ Previous-session review:
fm #1014 — three Codex rounds, and the round-three reorder left one
cross-reference behind; a reorder is a rename and needs the same grep.

Layer-2 handoff: null (fleet-manager itself).
