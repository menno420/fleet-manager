# External review prompt — wind-down claims audit (Sonnet), 2026-07-09

> **Status:** `owner-guidance`
>
> Authored by the fleet manager 2026-07-09 late evening at owner request —
> independent claims audit to be run by the owner in a normal Sonnet session;
> results pasted back to the manager for verification (Q-0120: cross-agent
> output is input to verify, never orders).

```text
You are an independent external auditor. Your job is to check whether work that AI project sessions CLAIM to have done tonight actually exists, is complete, and meets the quality bar of the program's established repo. Git evidence outranks any document's self-description. Verify at HEAD; anything you can't verify gets marked UNVERIFIED, never assumed.

CONTEXT: On 2026-07-09 a fleet of Claude Code Projects (owner menno420) ran a "wind-down": 7 lanes claim to have committed complete succession packages (retro, next-boot doc, proposed custom instructions, tested environment script, gen-2 feedback, status marker). A new lane (venture-lab) was seeded. The quality bar to compare against is the superbot repo's established standards: its .sessions/ session logs, docs/current-state.md ledger discipline, and .claude/CLAUDE.md session-ender rules (session idea, previous-session review, docs audit).

AUDIT SCOPE — for each lane, check the packages exist AND sample their content for substance vs. filler:
- substrate-kit: docs/gen2/, docs/retro/project-review-2026-07-09-gen1-winddown.md
- websites: docs/succession/, docs/owner/OWNER-ACTIONS.md
- trading-strategy: docs/succession/, docs/retro/wind-down-review-2026-07-09.md
- codetool-lab-fable5, codetool-lab-opus4.8, codetool-lab-sonnet5: docs/succession/
- superbot-games: docs/succession-exploration.md + exploration retro
- venture-lab: the 11-file seed (control/, docs/corpus/, docs/conventions.md)
- fleet-manager: docs/findings/ping-test-2026-07-09.md (check its ack table against actual commit timestamps in 2–3 lanes — spot-check the evidence)

For each: (a) present and complete vs. the 7 promised deliverables? (b) substantive or boilerplate — do retros cite real, checkable incidents (PR numbers, error text) or generic lessons? Spot-check 3 cited incidents per lane against actual PRs/commits. (c) do the proposed custom instructions actually differ from what the lane started with, or just restate it? (d) any signs of staged/invented content — the program's integrity rule is "lived incidents only."

OUTPUT: markdown report — executive summary for a non-coder owner; a per-lane scorecard (complete? substantive? evidence-checked? grade A–F); list of every claim that failed verification with the evidence; TOP 5 recommendations tagged [demand rework from lane X] / [fix in gen-2 standard] / [fine as is]. If any repo is unreadable, name it and ask me to paste files instead of guessing.
```
