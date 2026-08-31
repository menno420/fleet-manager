# 2026-08-31 — remove unsupported Superbot combination inference

> **Status:** `in-progress` — remove an agent-created ambiguity that incorrectly
> suggested the Fleet Manager successor might also be the Superbot rebuild.

- **📊 Model:** GPT-5 family · high · docs-only
- **📍 Venue:** local-desktop
- **🔗 Session:** unavailable — Codex desktop does not expose the current task id

💡 Session idea: when owner evidence names two replacement repositories, preserve
them as separate by default; never invent a combined topology without source
evidence from both products.

## Mission

Remove the unsupported ambiguity from the preceding landing record. Verify the
correction against Superbot's own current repository before editing, preserve
the owner's completed workbook unchanged, run Fleet Manager's required check,
and land the correction without an unnecessary external AI review.

## Evidence

- Owner correction, live: the Fleet Manager successor and a rebuilt Superbot are
  separate repositories; no agent was told to combine them.
- `menno420/superbot` main at `5e3a667b2a55bae98a7863dd66492f477dd19546`:
  `docs/owner/fleet-8seat-structure-2026-07-11.md` assigns Fleet Manager to the
  Project Manager hub and assigns `superbot` plus its rebuild to the separate
  SuperBot 2.0 product lane.
- The same live Superbot tree describes itself as the production Discord bot and
  behavioral oracle for a bot rebuild, not as the estate-management successor.

## Previous-session review

The preceding session correctly preserved and merged the owner's first workbook,
but its own content review added an unsupported combined-repository question.
That inference should have been checked against Superbot before it was recorded.

Layer-2 handoff: null (Fleet Manager itself; Superbot was inspected read-only).

