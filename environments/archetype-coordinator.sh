#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-coordinator.sh — THIN CONFIG for the "coordinator" archetype
# (ORDER 018 R2: ALL logic lives in environments/setup-base.sh — one lineage)
#
# Canonical copy: menno420/fleet-manager · environments/archetype-coordinator.sh
# Serves: the live `multi-repo` coordinator workspace (fleet-manager sessions
# steering N repos at once: substrate-kit, superbot, superbot-games,
# superbot-next, websites, ... as children of the working dir).
# Shape: cwd is a WORKSPACE, not a repo; the base's superset manifest ladder
# handles every manifest kind any child repo may ship.
# Knob table: environments/archetypes.md § "The base shim + knob table".
# CONTRACT (playbook R15, inherited from the base): ALWAYS exits 0.
# ---------------------------------------------------------------------------
set +e

# --- knobs -------------------------------------------------------------------
ARCH_NAME="coordinator"
BASELINE_PIP="pytest ruff"
# CI-parity pins (multi-repo.md wrinkle #1). superbot-next=python3.11 was
# MISSING here pre-consolidation (audit §4.2 latent bug — superbot-next, a
# child of this live env, installed under bare python3, correct only by
# luck). Fixed by carrying the full bot-prod table.
PICK_PYTHON_TABLE="superbot=python3.10 superbot-next=python3.11"
ENV_REPORT=""
GIT_TRIAGE=0

# --- locate + source the base shim (defensive: never die) --------------------
# Resolution: explicit override -> repo-local (cwd IS fleet-manager) ->
# workspace child clone (this env's home shape) -> alongside this file ->
# raw fetch (Q-0260 path).
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
