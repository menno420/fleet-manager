# 2026-08-20 · hub — the keep-bot-only direction captured; the DoS measured; the handoff built

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · idea/planning — the owner asked for a
  continuation prompt so the next session executes the improvement list, and
  added: *"remove the mineverse from railway, the only things we should keep
  is the things that are actually related to the bot etc."* This session
  measures the current state (the crawler fleet now ignores robots.txt and is
  DoS-ing control-plane), captures the decisions/rejections/opens into a
  worklist doc, poses the one HIGH (shiftlife scope) rather than resolving it
  silently, and emits the paste-ready prompt. No Railway mutation this
  session.

Time: 2026-08-20 · venue: owner-live hub chat · branch
`claude/railway-websites-audit-gp7nc7` restarted from `main` @ `0f8a728`
(fm #867 merged)

## Previous-session review

⟲ fm #867 (merged `0f8a728`): the three-answers execution. Checked at `main`:
queue entries and ledger walls present as landed. Nothing to repair.

## 💡 Session idea

Preflight-verified handoff: decisions committed to
[`docs/planning/2026-08-20-railway-keep-bot-only-worklist.md`](../docs/planning/2026-08-20-railway-keep-bot-only-worklist.md)
so the prompt is pointers, not payload.

## Close-out

**Shipped:**
- The worklist doc above — owner quotes, the keep-criterion applied per
  service, DECIDED/REJECTED/OPEN, seven ordered execution slices, explicit
  out-of-scope (shiftlife HIGH guard; the worker/bot-DB rail).
- `OQ-RAILWAY-SHIFTLIFE-SCOPE` — the one-letter HIGH posed, not resolved.
- Fresh measurements recorded in the worklist § 1: 5,001/5,001 Meta-range
  requests in 40 min on `/orders` (~295 MB), zero robots.txt fetches in
  3,001 requests, 4 legit `facebookexternalhit` hits, and 3 × 30 s external
  `healthz` timeouts — the board is intermittently unavailable to humans.
- The paste-ready continuation prompt, delivered in the hub chat (chat is its
  venue; the doc is its durable half).

**Verify:** strict gate at flip (real exit); every path the prompt names
checked at HEAD this session (preflight step 1); Railway states are same-hour
readbacks.

**⚑ decide-and-flag:** `OQ-RAILWAY-SHIFTLIFE-SCOPE` (owner, one letter).

**💡 idea:** the crawler measurements suggest a standing check — the 6-hourly
websites healthcheck could alert when external `healthz` latency exceeds a
threshold (it currently only checks status), catching the next
crawled-into-unavailability episode before a human notices. Routed to the
executing session's discretion.

**⟲ previous-session review:** in the header above.

**Layer-2 handoff:** null (no `docs/repos/` folder for the touched repos; the
worklist doc is the handoff).

**PR:** fm #<n> — <terminal state at flip>.
