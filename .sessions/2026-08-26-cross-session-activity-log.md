# 2026-08-26 — the estate activity log: what a cloud session can learn about local work

> **Status:** `in-progress` — born red on purpose. About to happen: measure how
> much of a local session's work a cloud session can currently see (answer so
> far: almost none), then build the dedicated section the owner asked for —
> `docs/activity/`, two lanes, a generator, a venue token on the card protocol,
> and the routes that deliver it. Flips to `complete` only after
> `python3 bootstrap.py check --strict` returns a real exit 0 read directly,
> never after a pipe, and after `@codex` has reviewed the exact head.

- **📊 Model:** opus-5 · high · feature build
- **📍 Venue:** cloud-container

## 💡 Session idea

The owner asked a question — *"how well does a cloud session understand what the
local sessions have been doing?"* — and proposed the fix in the same breath. The
question is answerable by measurement rather than opinion, and the measurement
should be in the record before the fix is designed, because it is what decides
the shape.
