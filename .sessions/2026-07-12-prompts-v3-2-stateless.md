# 2026-07-12 — prompts v3.2: strip volatile state from startup artifacts

> **Status:** `in-progress`

📊 Model: fable-5 · start 2026-07-12 ·
lane worker (owner correction 2026-07-12, dispatched)

## Declared at open (born-red)

Owner correction: startup prompts must never carry volatile state (PR numbers,
CI colors, trigger ids asserted as facts, "do X now" items) — they direct
agents to the repo documents where current state lives. This session: strip
the 9 startup artifacts (8 B files + A template; audit the ender), replace
FIRST WORK ORDERS with durable WORK SOURCES ladders, relocate still-valid
now-actions as ORDERs to the owning repos' inboxes (verified at HEAD first),
regen B files, bump to v3.2, update owner-queue C#34, heartbeat.
