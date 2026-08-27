# 2026-08-27 — durable owner-comment contract

> **Status:** `in-progress` — born red on purpose; the contract, router,
> consume transition, tests, and close-out have not landed yet.

- **📊 Model:** GPT-5 family · high · feature build
- **📍 Venue:** chatgpt-work

## Mission

Make repository-specific owner feedback a Fleet Manager-owned public record:
deterministic JSON records, stable per-repository and root indexes, a
never-delete consume transition, and a literal route a future session can read.
This is the Fleet Manager half only; the website UI and writeback client remain
owned by `websites`.

## 💡 Session idea

Pending implementation evidence.

## ⟲ Previous-session review

The 2026-08-26 estate-execution session specified the durable-record shape and
left the comments merge path, index update, and consume mechanics as named-open
findings. This session implements only that bounded contract; it does not
execute the other estate packets.

Layer-2 handoff: null (Fleet Manager itself; no member repository is being
modified).
