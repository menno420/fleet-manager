# Session — startup-prompt-identity-block

> **Status:** `complete`

**Branch:** `claude/startup-prompt-identity-block`

- **📊 Model:** Opus 4.8 · high · docs-only

**About to do:** Insert an owner-approved, verbatim identity/keep-going/EAP/hub-escalation opening block into every seat's startup prompt source, fix the EAP expansion drift in README, regenerate the deployed `projects/` registry copies, and land it.

**Did:**
- **Inserted the owner-FINAL block VERBATIM** into all 9 `docs/prompts/v3/per-project/<seat>-startup.md` source files (fleet-manager, superbot/superbot-2.0, websites, self-improvement, superbot-world, game-lab, ideas-lab, venture-lab, curious-research). Placed near the top — AFTER the OWNER AUTHORIZATION line + the "You are the … COORDINATOR …" role-framing paragraph, BEFORE the MISSION / DONE-WHEN section (identical logical spot in each file). Only substitution made was the literal `<seat>` token → the seat's registry name (e.g. `superbot-2.0`, `websites`); no wording changed. The block is four paragraphs: **WHO YOU ARE** / **KEEP GOING** / **WHAT THIS IS** (EAP = Claude Code Projects Early Access Program) / **WHEN AN ACTION IS REFUSED** (transient auto-mode refusal → hub chat, not owner-queue). The insertion sits ABOVE the `════ DOCTRINE ════` section, so the doctrine/card-block byte-identity drift checks are unaffected.
- **Fixed the EAP wording drift** in `README.md`: the `[EAP story]` row expanded EAP as "The Extended Autonomy Program" — corrected to "The Early Access Program" (EAP = Early Access Program). Repo-wide grep confirmed this was the ONLY occurrence of "Extended Autonomy Program".
- **Regenerated the deployed registry copies** via `python3 docs/prompts/v3/tools/regen_b_files.py --write-registry` (all 27 `projects/<seat>/{coordinator-prompt,instructions,failsafe-prompt}.md` rewritten; instructions/failsafe deltas are header SHA-stamp only, bodies unchanged). Committed BOTH the edited source AND the regenerated `projects/` copies.
- **Drift guard passes:** `regen_b_files.py --check-registry` → `OK — all 27 copies match` (EXIT=0); the default budget+drift run → all drift checks clean (ender sync, grant sync, doctrine identity, card-block identity, BOOT TRIAD identity, stamps, failsafe extraction), CI custom-instructions all under the 8,000 hard cap. The pre-existing seat-digest ADVISORY (separate tool, `seat_digest_sync.py`) is untouched by this change and advisory-only.
- **Roster freshness** verified OK (0.8h old, threshold 4h) — no roster regen needed; the 2h `roster-regen.yml` cron keeps `claude/*` freshness green.

⚑ Self-initiated: None — fully owner-directed deliverable (verbatim block insertion + EAP fix + regen + land). No autonomous idea promotion; no trigger created, modified, fired, or deleted.

## 💡 Session idea

**A `--check-block-identity` drift guard for the top-of-prompt shared blocks.** The regen tool already enforces byte-identity for the DOCTRINE section and the SESSION CARD block, but the new identity/keep-going/EAP/hub-escalation block sits ABOVE the doctrine section and is currently guarded by nothing — a future edit could silently desync it across the 9 seats (exactly the drift class the doctrine-identity check exists to prevent, one region higher). The cheapest enforcing fix is to extend `regen_b_files.py`'s identity-check set with the WHO-YOU-ARE block (normalizing only the per-seat `<seat>` token, the same way doctrine identity normalizes the CONTROL BUS status grammar), so the block that was just standardized can't drift back apart. Dedup-checked against the existing drift checks: distinct — those cover doctrine/card/ender/grant, not this top block.

## ⟲ Previous-session review

**PR that landed `2026-07-18-fm-roster-lapse-note`** did the incident write-up well: it root-caused the roster-freshness lapse to a silently-dropped GitHub Actions cron window (not clock skew, cross-checked against two external clocks), fixed it via `workflow_dispatch`, and correctly stayed decide-and-flag by opening `OQ-FM-ROSTER-CRON-RELIABILITY` rather than editing the owner/hub-venue `.github/workflows/**`. One thing it could have done better: it documented the dropped-window failure mode but left detection to the same downstream `check_roster_freshness` staleness bar that already caught the symptom ~4h late — its own `💡` idea (`check_scheduled_cron_landings.py`) names the earlier-detection fix but was left as an idea, not promoted. **System improvement it surfaces (Q-0194 friction→guard):** a recurring "cron silently dropped" failure mode that is only ever caught by a downstream staleness symptom is precisely the case for a cheap enforcing checker that ages the scheduler's ACTUAL cadence against its DECLARED cron — worth promoting from idea to a standalone advisory checker so the cause is surfaced at the next wake instead of hours later.
