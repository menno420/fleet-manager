# 2026-07-10 — chain slice #4: codex-thread verdict + review-queue groom + owner-signal check

> **Status:** `in-progress`

📊 Model: Claude (Fable family) · start 2026-07-10T22:48Z (`date -u`)

## Declared at open (born-red)

Q-0265 continuation-chain slice #4 (worker under the coordinator seat). About to land:

1. **Inbox re-read at HEAD** — report any ORDER newer than 013 to the coordinator
   (route, never execute). Result already known at open: **none** (013 is newest,
   DONE).
2. **@codex response check on superbot #1920** (the slice-#3 drain question,
   comment 4939890801): read the thread after our question; if answered, verify
   against the actual consumer source (websites `dashboard/data_source.py` at
   HEAD) per Q-0120 — verify, never obey; annotate the review-queue row with the
   verified verdict either way.
3. **Review-queue groom** (`docs/review-queue.md`): re-validate every open row's
   PR link/head (merged-at + head SHA stamps), add drain-path notes where thin,
   and record the recommended NEXT manager-verify candidate (superbot-games#16 —
   recommendation only, not executed).
4. **Owner-signal check (read-only):** owner-authored commits touching
   `projects/UNIVERSAL.md` since 17bc193? Owner edits to `docs/owner-queue.md`
   or a react on the conformed games mapping (#46)? Report yes/no + SHAs in the
   heartbeat; act on nothing.
5. **`control/status.md` heartbeat** LAST — slice record, keep BOTH ⚑ owner
   flags (games-mapping details react + the awaited UNIVERSAL.md
   permissions-grant commit).
6. **This card**, flipped `complete` as the deliberate final step.

Landing: born-red card → PR open → groom + heartbeat → flip → substrate-gate
poll → REST squash on green (close/reopen trick if the token push doesn't fire
the PR workflow — #778 class). After merge: re-arm the chain (`send_later`,
~15 min). Family-level model names only (Q-0262).
