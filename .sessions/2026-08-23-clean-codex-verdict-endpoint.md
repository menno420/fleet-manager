# 2026-08-23 — A clean Codex verdict is an issue comment, and I wrote "no review arrived" because I never read that endpoint

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #924's card, now on `main`, states: *"No review had arrived by 11:44:48Z —
~24 minutes."* **That is false, and it is my query that was wrong, not the relay.**

`MEASURED` 2026-08-23:

| endpoint | returns for fm #924 |
|---|---|
| `GET /pulls/924/reviews` — what I polled | **0** |
| `GET /issues/924/comments` — what I never read | `chatgpt-codex-connector[bot]` at **`2026-08-23T11:23:57Z`**: *"Codex Review: Didn't find any major issues."* |

So the review answered in **~3 minutes**, comfortably inside the measured ~335 s
relay, and the PR I described as landing unreviewed had in fact **passed review
clean** before it merged.

**The mechanism, and it is the sibling of a fact this estate already records.**
`CAPABILITIES.md:420` warns that *findings* arrive as **inline review comments**,
not in the review body — so read `/pulls/{n}/comments`. The missing half: when
Codex finds **nothing**, it creates **no review object at all** and posts a plain
issue comment instead. A poller watching `/reviews` (and even `/pulls/{n}/comments`,
which I also polled) sees zero on a clean pass and cannot distinguish it from
silence.

**This is the estate's own named failure, in its milder form.** The boot file
records a session that *"waited 150 s, wrote 'no review appeared' into a public
comment as if that were evidence, and merged three minutes before four real
findings landed."* I waited 24 minutes and wrote it into a committed card. The
outcome was benign — the verdict was clean — but **absence of evidence recorded
as evidence of absence is TRAP-003**, and I committed it while the register that
names it sits in the same tree.

## Previous-session review

⟲ fm **#924** (`53bbfff`) — the telemetry delta, merged; its card carries the
false claim corrected here. Checked at `main`: `check --strict` exit 0,
`check_doc_routes --strict` exit 0, telemetry 21,741 lines / 0 unparseable /
0 conflict markers, and **0 open PRs** in fleet-manager or websites.

## What is about to happen

Correct #924's card at its site, and add the clean-verdict endpoint to the
capability ledger beside the inline-comments fact it completes.

## Verify

(filled before the flip — real exit codes, never after a pipe: TRAP-002)
