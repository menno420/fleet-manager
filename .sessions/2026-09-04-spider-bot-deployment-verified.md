# 2026-09-04 — The deployment the last three cards handed forward, verified

> **Status:** `complete` — merged path: fm #1041, branch
> `claude/spider-bot-ai-ops-sthix0`, restarted from `main` because its previous
> PR (fm #1038) merged. Born red; flipped here as the last step.

- **📊 Model:** Opus 5 · xhigh · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01YCXH5D4omEgguaPYHwVz6d](https://claude.ai/code/session_01YCXH5D4omEgguaPYHwVz6d) · "Spider Bot AI operations bot"

## Previous-session review

Three cards in a row — the tranche card, the handoff card, the follow-up card —
each said the same thing: the deployment is not verified, and that is the item
being handed forward. **The owner merged spider-bot#3 at 18:42:14Z as
`5a7f8a2`**, so it stopped being a handoff and became a check to run.

## What was verified

| check | result |
|---|---|
| `meta.commitHash` on the new Railway deployment | `5a7f8a285a095855e0450b7c237d184344d5a580` — **byte-for-byte equal to `main` HEAD**, which is what `docs/rollout.md` prescribes instead of trusting `SUCCESS` |
| the deployment it replaced | `bc4f9985` → `REMOVING` |
| the worker's own `ready` line | `ready as Spider Bot#7153 in Slingy Spider; AI=True intake=False moderation=off` |
| command sync | `synced 12 guild commands` |

**The bot states the shipped off-state itself, in production.** Three documents
asserted `MOD_MODE=off` / intake off; the fourth thing to say it is the running
process. And `bc4f9985` moving to `REMOVING` is what finally *confirmed* it had
been the serving code while `main` sat at `bf4d7527` — a lag the docs predicted
in the abstract and nobody had looked at until this week.

The missing-channel warning needed reading rather than assuming: **`bot-state`
is pre-existing** (`spiderbot/config.py:57` at `bf4d7527`, checked at both
commits), and `case-state`/`intake-state` missing is the shipped state — rollout
steps 2 and 4, the owner's to create.

**What is NOT verified, and no log line can settle:** nothing was exercised. No
report filed, no message judged, no model call made. The deploy is proven; the
behaviour is not.

## What changed here

- `.sessions/2026-09-04-spider-bot-ai-ops.md` — the "two things deliberately NOT
  claimed" banner is now false and says so, with the correction visible.
- `docs/prompts/2026-09-04-spider-bot-ai-ops-continuation.md` — marked
  **CONSUMED**, ~1 h after it was written, with what it actually bought.
- `docs/prompts/README.md` — back to eight live files.
- spider-bot#4 carries the same record in that repo's own card.

## 💡 Session idea

**A handoff's value is in naming what it does not know.** Everything this
session's prompt carried in DECIDED and REJECTED was carried so it would not be
re-litigated — and none of it was, which is the null result those sections were
built for. The line that produced *new truth* was the one admitting ignorance:
the `preserve()` question marked *NEW, and in no document yet*. A different
model went and measured it and found the IaC would have deleted the rollout
switches. The confident sections cost the most to write and returned nothing;
the uncertain line was three sentences and returned a production defect.

## Close-out

**Landed as fm #1041**, alongside spider-bot#4 (green, `quality` ×2 success at
`10289e0`) which carries the same record in that repo's own card.

`check --strict` held red on the born-red hold as the only finding, read from
the finding lines. The force-push hook named four files; every one was `main`
moving forward, established by blob comparison, and `comm -23` over the
discarded head's `guard-fires.jsonl` returned **0** lines absent at HEAD.

**Still open, and correctly so:** the six owner-only setup steps in
`spider-bot/docs/rollout.md`, and the behaviour that no deploy check can prove.
Rollout step 1 is done; step 2 needs a channel only he can create.
