# 2026-08-26 — correct a page size published as a commit count

> **Status:** `in-progress` — born red. About to happen: `spider-bot`'s commit
> figure in the merged fm #947 is wrong and main is carrying it. Flips after
> `python3 bootstrap.py check --strict` returns a real exit 0 read directly.

- **📊 Model:** opus-5 · high · docs-only
- **📍 Venue:** cloud-container

## 💡 Session idea

The self-check that catches a number is worth more when it runs *after* the
merge than when it runs before, because before the merge it competes with
momentum. This correction exists because the question "what did you actually
measure?" was asked once more after the PR had already landed.

## What was wrong

fm #947 published *"`spider-bot` … 8 commits in the two days to 2026-08-25"* in
[`findings/2026-08-26-cross-session-visibility.md`](../docs/findings/2026-08-26-cross-session-visibility.md)
§ 5 and [`current-state.md`](../docs/current-state.md). **8 was the `per_page=8`
I had asked for** — the page size, written down as a count. Re-measured:

```
GET /repos/menno420/spider-bot/commits?since=2026-08-24T00:00:00Z&per_page=100
→ 20 commits, oldest 2026-08-24T14:39:58Z, newest 2026-08-25T22:42:55Z
```

**Third instance of one error class in a single session.** `@codex` caught the
other two: a shallow clone's 52 commits presented as the repository's history,
and a hand count presented as the generated table's figure. Every one is a
*sample read as a total*. The conclusion is unchanged and stronger — a live
production repository took 20 uncarded commits in two days.

## ⟲ Previous-session review

[`2026-08-26-cross-session-activity-log.md`](2026-08-26-cross-session-activity-log.md)
built `docs/activity/` and recorded that hand-written numbers were its worst
habit. It then shipped one more. The fix it already landed is the right one and
was simply not applied here: figures in the activity log come from
`tools/estate_activity.py` and cannot go stale. This correction puts the
command beside the number in the prose too.

Layer-2 handoff: null (fleet-manager itself; `spider-bot` was read live, not
attached, and its Layer-2 folder is unchanged).
