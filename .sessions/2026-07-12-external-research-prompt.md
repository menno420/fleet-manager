# 2026-07-12 — external GPT deep-research prompt

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
fleet-manager worker (external research prompt composition)

## Declared at open (born-red)

Composing the external GPT deep-research prompt (`docs/prompts/external/2026-07-12-gpt-deep-research-prompt.md`) — a self-contained, zero-context briefing embedding the system architecture, the 2026-07-10→12 story, the known-problem census, and the research mission.

## Close-out

- **Deliverable:** `docs/prompts/external/2026-07-12-gpt-deep-research-prompt.md` (~37.8k chars, 7 sections: role/mission · system · story · repo map · known problems · research questions · researcher rules). Linked from `docs/prompts/README.md` (new "External prompts" section).
- **Sources compressed:** all seven 2026-07-12 research docs on main (platform capabilities, core + satellite problem censuses, prompt architecture, QA boot-sim/incident-replay/question-rounds, both staleness sweeps, consolidation census) + the prompt-currency audit (PR #118 branch) + the consolidation-and-reset proposal (PR #121 branch) + `docs/prompts/v3/` set + control/status.md, MISSION.md, owner-queue + substrate-kit `docs/reports/2026-07-12-prompt-template-hardening-input.md`.
- **Hard exclusions verified by grep:** no secret values, no trigger/session ids, no owner email, the private second track unnamed (no repo name/link), no exposure PR/branch/refs path ("media packs" generalized; class-only description), family-level model names only.
- **PR:** #124, parked born-red → flipped complete this commit; landing = REST squash on green (auto-merge arming walled in this repo).

## Enders

- 💡 **Session idea:** the external-briefing compression done here by hand (research corpus → one self-contained prompt) is a repeatable manager artifact — add a `docs/prompts/external/` regen convention (source-list header + "compressed from" stamps) so future external-review prompts can be re-cut from the then-current corpus instead of drafted from scratch; pairs naturally with the kit seat-digest fences (currency-audit delta 12).
- ⟲ **Previous-session review:** the consolidation/v3.4 session (PR #122) declared "Do NOT merge — owner reviews personally" in its PR body while the prompt-currency audit (same day) flagged exactly that pattern — a PR body declaring its own landing path — as the P0 class v3.3 failed to prevent. It did the right thing for an owner-gated plan, but the improvement stands: landing-path declarations belong in the session card/heartbeat grammar, not free-prose PR bodies, so the dictionary rule has one surface to check.
