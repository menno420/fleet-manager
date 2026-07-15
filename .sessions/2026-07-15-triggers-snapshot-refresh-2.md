# Session — 2026-07-15 — triggers snapshot refresh (17:21Z export)

> **Status:** `in-progress`

- **📊 Model:** Fable · medium · telemetry-only

About to: refresh `telemetry/triggers-snapshot.json` — the 11:50Z capture is
>4h stale (`check_trigger_health` I6 SNAPSHOT-FRESH red, 5.6h at 17:27Z).
Full `list_triggers` export already taken read-only (cursor-to-exhaustion,
capture window 17:14–17:21Z, 20 pages · 1920 records · 0 dupes); this PR
lands the rebuilt snapshot in the existing schema plus this card. Read-only
sweep on the registry — nothing created, deleted, or modified. Worker acting
as the coordinator seat's hands; merge lands via merge-on-green, no
self-merge / no auto-merge armed by this session.
