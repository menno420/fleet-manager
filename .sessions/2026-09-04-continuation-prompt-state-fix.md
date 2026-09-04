# 2026-09-04 — The handoff prompt said one thing in chat and another in the repo

> **Status:** `complete` — merged via fm #1030, branch `claude/couch-legend-docs-handoff-iwpo96`.

- **📊 Model:** Opus 5 · xhigh · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01FAkSXD7ZQ7E7XzysZmLRbF](https://claude.ai/code/session_01FAkSXD7ZQ7E7XzysZmLRbF) · "Couch Legend game design and architecture"

## Previous-session review

Same session, immediately after fm #1028 merged as `2462f52`. That PR added
`docs/prompts/2026-09-04-couch-legend-phase-b-continuation.md`. The owner-review
round on the handing-over reply is what surfaced this.

## 💡 Session idea

The prompt was written before its own PR merged, so its `WHERE THINGS STAND`
section described a PR that was still open and a `main` that had since moved.
When I pasted the prompt into chat I silently refreshed those two facts — and
did not write the refresh back to the file. **The next session reads the file,
not the chat**, so the durable copy was stale in exactly the section that
exists to be trusted, inside a prompt whose own first step is *"Do not trust
the state above."*

## What is about to happen

Bring the committed prompt up to the state that is actually true, so the two
copies say the same thing.

## What changed

- `docs/prompts/2026-09-04-couch-legend-phase-b-continuation.md` — the two
  fleet-manager state lines. `aef2429` → `2462f52` for `main`, and the
  "PR #1028 was open at `8a75072` … believed merged, confirm" bullet replaced
  by the merged fact. Everything else is untouched: the couch-legend state,
  the census numbers and the phase-B gate were all verified at HEAD and are
  unaffected by fleet-manager's own head moving.

## Close-out

**Landed.** Two lines, and the reason they were wrong is worth more than the
lines: a prompt's state section ages between being written and being merged,
and the copy that ages is the one nobody re-reads.

Checked before the force-push rather than after: the branch's previous PR had
merged, so it was restarted from `main` (`git checkout -B … origin/main`). The
force-push hook flagged that the discarded head differed from `main` in
`.substrate/guard-fires.jsonl`; `comm -23` over the two sorted blobs returned
**0** lines present in the old head and absent from `main`, so nothing was
lost.

`python3 bootstrap.py check --strict --added-card
.sessions/2026-09-04-continuation-prompt-state-fix.md` held red on the born-red
hold as the only finding — established by grepping the finding lines, not by
reading the exit code alone — and is expected green at this flip.
