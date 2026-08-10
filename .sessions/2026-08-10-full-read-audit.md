# 2026-08-10 · hub — full-read audit of fleet-manager (100% of tracked files)

> **Status:** in-progress

- **📊 Model:** opus-5 family · ultracode workflows · review/verify
- Time: 2026-08-10 · venue: Claude Code remote container, owner-live hub chat ·
  branch `claude/fleet-manager-full-audit-lty31q`

💡 Session idea: coverage is only a claim until the ledger is built from what
the readers returned; an agent that reports "batch covered" has told you about
its intention, not its reading.

Layer-2 handoff: null (fleet-manager itself)

## What is about to happen

Every tracked file in this repository — all 833, 30,006,142 bytes as enumerated
at `4b59e9b` — is read by a fan-out of workflow agents. Each agent returns the
explicit list of paths it opened together with a content-derived fingerprint per
path (line count, head and tail slices), and the coverage ledger is assembled
from those returns and then mechanically diffed against `git ls-files`. Findings
are then refuted by independent agents before any of them are reported.

This session READS and REPORTS. The edit pass is a later session and the owner's
call.

## Previous-session review

⟲ fm #837 (D2 truth pass) rebuilt the cold front door so purpose, live state and
next action are recoverable from three files, and removed volatile counts from
boot prose. It proved the route works for a reader who follows it. The question
it left open — and the reason this session exists — is what is true of the files
that route never visits: five consecutive sessions whose stated job was to read
this repo and put it in order all missed that the owner's current plan was
unreachable from the front door, because each read a curated subset and each
subset was internally coherent.

## Close-out

_pending — this card is born red and flips last._
