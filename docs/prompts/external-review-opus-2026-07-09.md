# External review prompt — doctrine comparison (Opus), 2026-07-09

> **Status:** `owner-guidance`
>
> Authored by the fleet manager 2026-07-09 late evening at owner request —
> independent doctrine review to be run by the owner in a normal Opus session;
> results pasted back to the manager for verification (Q-0120: cross-agent
> output is input to verify, never orders).

```text
You are an independent external reviewer. You have no stake in the work you are reviewing; your value is skepticism. Do not treat any claim in the documents as true because a document asserts it — verify against the repos at HEAD, and mark anything you cannot verify as UNVERIFIED rather than assuming.

CONTEXT: A fleet of Claude Code Projects (10 GitHub repos, owner menno420) has just gone through a "gen-1 → gen-2" refresh: a new coordination doctrine was written in the repo fleet-manager, and 7 project lanes committed succession packages. The ORIGINAL doctrine this program grew from lives in the superbot repo and is battle-tested over ~1900 PRs.

YOUR TASK — a doctrine comparison. Read both sides:
NEW: menno420/fleet-manager — docs/playbook.md (rules R1–R21), docs/gen2-blueprint.md, docs/prompts/ (esp. venture-lab-draft.md, gen1-winddown-universal.md), docs/owner-queue.md, environments/archetypes.md.
ORIGINAL: menno420/superbot — .claude/CLAUDE.md, docs/collaboration-model.md, docs/owner/ai-project-workflow.md, docs/owner/agent-decision-authority.md (Q-0240/Q-0241), docs/planning/fleet-coordination-protocol-2026-07-09.md.

Answer four questions with evidence (file + quoted line for every claim):
1. CONTRADICTIONS — where does gen-2 doctrine conflict with superbot doctrine, and which side is right for a multi-repo fleet?
2. REGRESSIONS — what problems did superbot's system already solve (session cards, ledger discipline, question router, friction→guard, idea lifecycle) that gen-2 dropped or weakened?
3. DUPLICATION — where do the two doctrines say the same thing in different words, risking drift? Which should be the single source?
4. PORTABILITY — what should be back-ported into superbot, and what superbot wisdom should be forward-ported into the gen-2 blueprint?

OUTPUT: a markdown report — executive summary (plain language, the owner is a non-coder), findings by question with severity (high/med/low) + evidence, then TOP 5 recommendations, each tagged [backport to superbot] / [fix in gen-2] / [accept divergence, document why].
If you cannot read any repo, say exactly which and stop — ask me to paste files. Never review from memory or general knowledge of "how such docs usually look."
```
