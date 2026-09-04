# 2026-09-04 — "The owner merged it" was an account name read as a person

> **Status:** `complete` — merged path: fm #1043 with spider-bot#6, branch
> `claude/spider-bot-ai-ops-sthix0`, restarted from `main` because its previous
> PR (fm #1041) merged. Born red; flipped here as the last step.

- **📊 Model:** Opus 5 · xhigh · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01YCXH5D4omEgguaPYHwVz6d](https://claude.ai/code/session_01YCXH5D4omEgguaPYHwVz6d) · "Spider Bot AI operations bot"

## Previous-session review

Same session, immediately after fm #1041 and spider-bot#4 merged. The
owner-review round asked what *"the owner merged spider-bot#3"* rested on. It
rested on `merged_by: menno420` from the PR API — and that field cannot mean
what I used it to mean.

## The measurement

`$GITHUB_PAT` is account-scoped, so anything a session does with it is recorded
as the owner doing it.

| PR | actually merged by | `merged_by.login` | timeline `actor` | `performed_via_github_app` |
|---|---|---|---|---|
| spider-bot#3 | **unknown** | `menno420` | `menno420` | `None` |
| spider-bot#4 | **this session, via `$GITHUB_PAT`** | `menno420` | `menno420` | `None` |

Identical. Row 2 is the positive control ([TRAP-003](../docs/traps.md)) and is
the whole reason this is a measurement: without having merged one myself, nine
minutes later, I would have read row 1 as the owner and had no way to say why
not. A GitHub **App** does stamp `performed_via_github_app` — that is how
`merge-on-green` and the Codex connector stay identifiable — so the gap is
specific to PAT-authenticated calls.

**So spider-bot#3 was merged by the owner, or by the sibling session that had
pushed `8937191c` ten minutes earlier.** Both remain open; the record now says
so instead of picking one.

## Why it is not cosmetic

This estate runs several sessions against one account. A production-deploying
PR recorded as *his* decision, when a session may have made it, **launders an
agent action into an owner action** — inside the exact records a later session
reads as authority. And this PR had been deliberately left unmerged on the
stated grounds that the merge was his call, so the attribution is precisely the
fact that would have been checked.

## What changed

- The claim corrected in four merged documents: the hub card, the
  deployment-verified card, the consumed continuation prompt, and spider-bot's
  own tranche card (via spider-bot#5).
- `docs/CAPABILITIES.md` — the measurement, with the control table.
- `.claude/hooks/doc-routes.json` — a route firing on `owner merged` /
  `merged_by` / `he merged it`, so the next session meets this before writing
  the sentence rather than after. 74 routes, 0 errors.

## 💡 Session idea

**Three checkers scan this repo for false walls, stale routes and unflipped
cards; none scans for a claim about who did something.** The wall checker exists
because a limitation written down outlives the session that wrote it. An
attribution does exactly the same and is harder to spot, because it is not
wrong on its face — `merged_by` really did say `menno420`. The defect is a
*type error*: an account is not a person, and in a multi-session estate it is
not even close. The route added here is the cheap version; a checker that flags
person-attribution near an API field name is the version that would have caught
it before four documents carried it.

## Close-out

**Landed as fm #1043**, with [spider-bot#6](https://github.com/menno420/spider-bot/pull/6)
carrying the same correction to that repo's tranche card.

`check --strict` held red on the born-red hold as the only finding, read from the
finding lines; `check_no_false_walls.py` exit 0; `check_doc_routes.py` 74 routes,
0 errors. The new route fired on this card's own text while it was being
written — the positive control for the route, not an assertion that it would.

The spider-bot force-push needed an explicit expected value
(`--force-with-lease=<branch>:<sha>`) because the branch had no remote-tracking
ref after `#4`'s squash; the hook computed the discarded head as
**content-identical to `origin/main`**, so nothing was lost.

**Unchanged by any of this:** the deployment verification. `meta.commitHash`
`5a7f8a285a095855e0450b7c237d184344d5a580` equals `main` HEAD — two printed
strings compared, and who pressed merge does not touch it.
