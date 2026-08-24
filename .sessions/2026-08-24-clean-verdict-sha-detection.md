# 2026-08-24 — The clean-pass verdict has no `Reviewed commit:` line, and main says it does

> **Status:** `in-progress` — branch `claude/active-projects-overview-kiftou`,
> restarted from `origin/main` at `9bd48b4` (fm #938, merged). Born red on
> purpose: the card is the merge hold (TRAP-006/007). It flips only after
> `python3 bootstrap.py check --strict` returns a real exit 0, read from a
> redirect and never after a pipe, **and** after `@codex` answers on the head
> being flipped.

- **📊 Model:** opus-5 · high · docs-only

## previous-session review

⟲ fm #938 (`9bd48b4` on `main`): TRAP-007, the three card routes, and the round-2
corrections. Checked at `main` — present and correct, except for one instruction
it shipped that is **false**, which this session exists to fix.

## 💡 Session idea

fm #938 landed guidance — in `docs/traps.md` TRAP-007 and in all three card
routes — telling a session to establish that a clean `@codex` verdict covers the
current head by **parsing a `Reviewed commit:` line from the issue comment**.

**That line does not exist in a clean-pass comment.** It was asserted by the
reviewer, propagated by me without checking the actual comment body, and merged.

`MEASURED` 2026-08-24 against the real artifact — fm #938's own clean pass, the
comment created `2026-08-23T23:42:43Z`, 3,155 bytes:

- `'Reviewed commit:' in body` → **False**
- 40-char SHAs present in the body → **`0c1a033fc9c7…` (the reviewed head) and
  `5a3f0878e6…` (the merge preview)**, both only inside `blob/<sha>/…` URLs

The `**Reviewed commit:** \`287b206bb1\`` line is real but belongs to the
**review-object body**, which is the case that already carries `commit_id` and
needs no parsing at all. So the shipped instruction fails in exactly the case it
was written for: a session following it finds no such line and concludes **no
verdict exists** — the same false-negative that made this estate merge two PRs
mid-review.

## What is about to happen

Replace the parse rule in `docs/traps.md` and all three card routes with what the
artifact actually supports, and record the measurement so the next reader does not
have to re-derive it.
