# 2026-09-04 — The handoff was picked up, and it made two hub records wrong

> **Status:** `complete` — merged path: fm #1038, branch
> `claude/spider-bot-ai-ops-sthix0`, restarted from `main` because its previous
> PR (fm #1031) merged. Born red; flipped here as the last step.

- **📊 Model:** Opus 5 · xhigh · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01YCXH5D4omEgguaPYHwVz6d](https://claude.ai/code/session_01YCXH5D4omEgguaPYHwVz6d) · "Spider Bot AI operations bot"

## Previous-session review

fm #1031 merged the continuation prompt at 17:38Z. **At 18:32Z a different
session — Claude Fable 5.1, `session_01XtUDb1BxPVdjkGryVWCKVu` — pushed
`8937191c` to spider-bot#3**, a review pass that read the docs against the tree
and against the live Railway project. It answered the one question that prompt
listed as open and no document held, and it found two things nothing in this
estate had.

## What it found, and why it lands here

**The IaC would have deleted the rollout switches.** `.railway/railway.ts`
declared `preserve()` for exactly the three variables that exist. Railway IaC is
**omit means delete** — measured with a read-only `railway config plan` that
previewed `Delete variable worker.GUILD_ID` when one existing variable was taken
out of the file. So a `GITHUB_TOKEN` or `MOD_*` set in the dashboard at rollout
step 3–5 would have been removed by the next apply. All six switches are now
declared `preserve()`, and a plan with them added and none set reports "already
up to date" — inert until each is used. **fm #1031 raised this as UNKNOWN and
open; four sessions-minutes later it was measured and fixed.** That is the
prompt working exactly as intended, and it is the reason a question written down
as open beats one carried in a head.

**`docs/what-changed.md` told the owner to create `#mod-cases`; the bot resolves
`#case-state`.** Following the owner page as written would have left moderation
silently off — the failure `invariant 4` makes deliberate for a *missing*
channel, delivered instead by a *wrong instruction*.

**And `railway.json` never existed here.** spider-bot's `CLAUDE.md`,
`docs/rollout.md` and its session card all named it; so did **this repo's Layer-2
entry**, which is why the correction lands in fm and not only there. The tree has
held `.railway/railway.ts` alone since spider-bot#1/#2 on 2026-08-25.

## What changed

- `docs/repos/spider-bot/README.md` — `railway.json` → `.railway/railway.ts`,
  and `railway.json` removed from the pattern list it wrongly contained. The
  correction is kept visible with what made it matter rather than quietly
  applied: **the lag that paragraph predicts had already happened and nobody had
  looked** — the live worker ran `bc4f9985` while `main` was `bf4d7527`.
- `docs/prompts/2026-09-04-spider-bot-ai-ops-continuation.md` — the state lines
  moved to `8937191c` / 24 commits, and the OPEN item is struck through and
  marked ANSWERED with the measurement, so the next reader does not re-run an
  investigation that is finished. fm #1030's lesson, applied to my own prompt
  four hours later.

## 💡 Session idea

**A handoff prompt is only as good as its OPEN section, and the proof arrived in
under an hour.** Everything in the prompt's DECIDED and REJECTED lists was
carried so it would not be re-litigated. But the single line that produced new
truth was the one that said *this is unknown and it sits under rollout step 3* —
a different model, in a different session, went and measured it. The prompt's
value was not in what it knew; it was in having named precisely what it did not.

## Close-out

**Landed as fm #1038.** Two hub records brought back to the tree.

`check --strict` held red on the born-red hold as the only finding, read from
the finding lines. The force-push hook named 71 differing files; every one was
main moving forward, established by **blob comparison, not commit list** —
`comm -23` over the sorted `docs/CAPABILITIES.md` and `.substrate/guard-fires.jsonl`
of the discarded head returned **0** lines absent at HEAD, and the five other
files fm #1031 touched are byte-identical on `main`.

**What this card does not claim:** spider-bot#3 is still open at `8937191c`,
green and unmerged, and its deployment is still unverified. The check-in at
18:42Z carries it.
