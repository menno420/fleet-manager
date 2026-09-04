# 2026-09-04 — Hand the Spider Bot AI-operations work forward

> **Status:** `in-progress` — branch `claude/spider-bot-ai-ops-sthix0`, restarted
> from `main` because its previous PR (fm #1029) merged. Born red; flipped last.

- **📊 Model:** Opus 5 · xhigh · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01YCXH5D4omEgguaPYHwVz6d](https://claude.ai/code/session_01YCXH5D4omEgguaPYHwVz6d) · "Spider Bot AI operations bot"

## Previous-session review

Same session, continuing after fm #1021 and #1029 merged and spider-bot#3 was
deliberately left open for the owner. The owner asked for a continuation prompt
so the next session can review the PR and take it forward.

## What is about to happen

Write the handoff, and fix two things the preflight for it turned up.

## What changed

- `docs/prompts/2026-09-04-spider-bot-ai-ops-continuation.md` — the prompt,
  identical to the copy pasted into chat. fm #1030's whole lesson was the two
  copies drifting apart, so they were written once and copied, not retyped.
- `docs/prompts/README.md` — a ninth live file.
- `.sessions/2026-09-04-spider-bot-ai-ops.md` — **`22 commits` → `23 commits`**.
  Re-derived with `git rev-list --count origin/main..HEAD` while checking the
  numbers the prompt would state. The card was right when it was written and one
  commit landed after it — the same drift its own *Previous-session review*
  section is about, one day old instead of eleven.
- `docs/CAPABILITIES.md` — the Railway GraphQL route, because reaching it cost a
  detour that no record would have saved.

## What the preflight measured that no record held

**The live worker is not running `main`.** `bc4f9985` is deployed; `main` is
`bf4d7527`; that deploy shows **SKIPPED**, because the commit touched only
`.railway/railway.ts` and the watch patterns are `spiderbot/**`,
`requirements.txt`, `.python-version`. Correct behaviour, and `docs/rollout.md`
predicts it in the abstract — but nothing said it had *already happened*, so
"verify `meta.commitHash == HEAD` after merging" would have compared against a
hash that was never live.

**Everything in spider-bot#3 arrives off — measured, not read off the code.**
The worker carries exactly three application variables (`ANTHROPIC_API_KEY`,
`DISCORD_TOKEN`, `GUILD_ID`; names only, never values). Every switch the
rollout names is unset.

**And one new owner question that no doc holds:** `.railway/railway.ts` declares
`preserve()` for exactly those three. Whether an IaC apply would drop a
dashboard-set `GITHUB_TOKEN` or `MOD_*` is unknown, and it sits directly under
rollout step 3.

## 💡 Session idea

The prompt's own preflight found more than the prompt did: a stale count, a
deployment nobody had looked at, and an unasked owner question — all from
re-deriving numbers that were already written down. **The cheapest audit of a
record is being made to restate it.** `prompt-preflight`'s `NUMBERS` line exists
for exactly this and it earned its place three times in one pass.

## Close-out

Pending — this card is the merge hold.
