# 2026-08-23 — The last verification delta, and the loop that keeps orphaning it

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

The closing verification ran `bootstrap.py check --strict` and
`tools/check_doc_routes.py --strict` against `origin/main` to confirm fm #926
landed clean. Both exit 0. The strict gate appends fire records to
`.substrate/guard-fires.jsonl`, and the kit's rule is to commit that delta.

**The loop worth naming, because it caught me twice today.** Running the gate
*as post-merge verification* produces a delta with no PR to carry it — so the
next stop-hook check finds a dirty tree, and landing that delta requires another
PR, whose own pre-flip gate run produces another delta. fm #924 was the first
instance; this is the second.

**It closes only if the last gate run of a session is the pre-flip one**, whose
delta is committed *with* the flip. Post-merge verification against `main` is
valuable — it is how I confirmed the merged `route_docs.py` actually behaves —
but it must be the **last** thing, with its delta landed by a card like this one
and no further strict run afterwards.

`MEASURED` before committing: **7 appended lines · 0 deletions · 0 unparseable**,
and `git diff --stat origin/main` excluding that file is **empty**.

## Previous-session review

⟲ fm **#926** (merged). Checked at `main`: `codex-verdict-poll` present (62
routes), the `Reviewed commit:` SHA-match requirement present, `stays n=1` gone,
and the dated `LAST-VERIFIED: 2026-08-23` ledger entry present. `check --strict`
and `check_doc_routes --strict` both exit 0 on `main`; **0 open PRs** in either
repo. The P1 that #925 left on `main` is closed.

## What is about to happen

Commit the append. No other change, and no strict run after the flip.

## Adversarial review — clean, and the new mechanism proved itself on it

`@codex` returned a **clean verdict at the exact head `50d964132e`**, posted to
`/issues/927/comments`. **`/pulls/927/reviews` returned `0`** — so the method I
used all morning would have reported *no review* on a PR that had just passed.

That is fm #926's route and ledger entry working end to end, on the first PR
after they landed, against the precise failure that produced them.

## Verify

- `python3 bootstrap.py check --strict` → **exit 1 pre-flip, born-red hold only**;
  its delta is committed *with* this flip, which is what closes the loop this card
  names. **No strict run after the flip** — that is the whole point.
- Delta properties measured before the commit: 7 lines · 0 deletions ·
  0 unparseable · empty diff vs `main` excluding the ledger.
- Verdict matched on the `Reviewed commit:` SHA and the Codex login, on **both**
  surfaces — the discipline `CAPABILITIES.md` requires.

## Layer-2 handoff

`null` — fleet-manager itself; no satellite repo attached.
