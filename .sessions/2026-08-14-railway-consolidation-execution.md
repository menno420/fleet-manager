# 2026-08-14 · hub — Railway consolidation executed: churn stopped, duplicates retired, W1 done

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · feature build — the owner's live go on fm #861's
  recommendation: *"You can execute the recommended plan, retire the restarts
  etc and remove the duplicate websites in superbot."* Execute W1 (retire the
  three `reliable-grace` duplicate sites, reclaim the old names), stop the
  bot-restart churn (refresh schedule + worker watch filter), reduce backup
  cadence (verified first), App Sleep on the quiet keep sites, and investigate
  control-plane's egress. HARD RAIL unchanged: never touch `worker` or either
  protected Postgres; `postgres-botsite` is NOT deleted (needs an explicit
  owner amendment — asked, not assumed).

Time: 2026-08-14 · venue: owner-live hub chat (remote session) · branch
`claude/railway-websites-audit-gp7nc7` restarted from `main` @ `76642e2`
(fm #861 merged; same-name branch per the merged-PR rule)

## Previous-session review

⟲ fm #861 (card `.sessions/2026-08-14-railway-websites-audit.md`, complete,
merged `76642e2`): the audit this session executes. Checked at `main`: §7 row
present, OQ-RAILWAY-PROJECT-SPLIT carries the packet, 12/12 Codex findings
conceded in the merged text. Nothing to repair.

## 💡 Session idea

Execute fm #861 § 5 with the owner's explicit go, in measured-impact order,
each mutation verified live after it lands, every Railway call by exact
service id, never project-level.

## Close-out

*(flips with the badge)*
