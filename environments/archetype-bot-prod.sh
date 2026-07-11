#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-bot-prod.sh — THIN CONFIG for the "bot-prod" archetype
# (ORDER 018 R2: ALL logic lives in environments/setup-base.sh — one lineage)
#
# Canonical copy: menno420/fleet-manager · environments/archetype-bot-prod.sh
# Serves: superbot-next, superbot (legacy). The ONLY archetype that may carry
# production-pointing vars (DISCORD_BOT_TOKEN_PRODUCTION, DATABASE_URL, the
# Railway trio) — every other archetype EXCLUDES them (env-vars.md DANGER rule).
# Shape: production Discord bot; Postgres required; hash-pinned lockfile
# (superbot-next) / 3.10-pinned requirements (legacy superbot).
# Knob table: environments/archetypes.md § "The base shim + knob table".
# CONTRACT (playbook R15, inherited from the base): ALWAYS exits 0.
# ---------------------------------------------------------------------------
set +e

# --- knobs -------------------------------------------------------------------
ARCH_NAME="bot-prod"
BASELINE_PIP=""                    # no baseline — deps come from the repo's
                                   # own lockfile/requirements only
# CI-parity pins: superbot -> python3.10 (code-quality.yml pins "3.10");
# superbot-next -> python3.11 (every ci.yml / named-gates / golden-parity /
# restore-verify job pins "3.11"). A repo's own scripts/env-setup.sh
# (preferred automatically by the base) remains the durable fix.
PICK_PYTHON_TABLE="superbot=python3.10 superbot-next=python3.11"
# Presence report (NAMES only): the fail-fast trio superbot-next refuses to
# boot without (sb/spec/config.py) + legacy superbot's deploy-required
# YOUTUBE_API_KEY (degrades with a warning rather than fail-fast).
ENV_REPORT="DISCORD_BOT_TOKEN_PRODUCTION DATABASE_URL SB_DATA_PLANE YOUTUBE_API_KEY"
ENV_REPORT_HINT="bot boot may fail-fast without it; tests may be fine"
GIT_TRIAGE=1                       # workspace-residue advisory (report only —
                                   # NEVER mutates; 2026-07-10 fleet finding)

# --- locate + source the base shim (defensive: never die) --------------------
BASE=""
for c in "${FLEET_SETUP_BASE:-}" \
         "environments/setup-base.sh" \
         "fleet-manager/environments/setup-base.sh" \
         "$(dirname -- "$0" 2>/dev/null)/setup-base.sh"; do
  [ -n "$c" ] && [ -f "$c" ] && BASE="$c" && break
done
if [ -z "$BASE" ]; then
  BASE="$(mktemp 2>/dev/null || echo "/tmp/setup-base.$$.sh")"
  curl -fsSL --retry 2 --max-time 60 -o "$BASE" \
    "https://raw.githubusercontent.com/menno420/fleet-manager/main/environments/setup-base.sh" \
    || BASE=""
fi
if [ -n "$BASE" ]; then
  . "$BASE"
else
  echo "[env-setup:$ARCH_NAME] setup-base.sh unavailable (no local copy; raw fetch failed) — deps NOT installed; run installs in-session (non-fatal)"
fi
exit 0
