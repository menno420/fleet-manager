#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-python-lab.sh — THIN CONFIG for the "python-lab" archetype
# (ORDER 018 R2: ALL logic lives in environments/setup-base.sh — one lineage)
#
# Canonical copy: menno420/fleet-manager · environments/archetype-python-lab.sh
# Serves: substrate-kit, codetool-lab-fable5, codetool-lab-opus4.8,
#         codetool-lab-sonnet5, superbot-games, fleet-manager, venture-lab,
#         sim-lab, product-forge, idea-engine, superbot-idle, mobile-lab.
# Shape: stdlib-or-tiny-deps Python lab; zero secrets; no services.
# Knob table: environments/archetypes.md § "The base shim + knob table".
# CONTRACT (playbook R15, inherited from the base): ALWAYS exits 0.
# ---------------------------------------------------------------------------
set +e

# --- knobs -------------------------------------------------------------------
ARCH_NAME="python-lab"
BASELINE_PIP="pytest ruff build"   # substrate-kit is stdlib-only with NO
                                   # requirements.txt; fresh containers lack
                                   # pytest; `build` covers packaged labs.
PICK_PYTHON_TABLE=""               # no CI-parity pins — bare python3
ENV_REPORT=""                      # zero-secret archetype: nothing to report
GIT_TRIAGE=0

# --- locate + source the base shim (defensive: never die) --------------------
# Resolution: explicit override -> repo-local (cwd IS fleet-manager) ->
# workspace child clone -> alongside this file -> raw fetch (Q-0260 path).
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
