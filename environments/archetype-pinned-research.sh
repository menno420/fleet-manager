#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-pinned-research.sh — THIN CONFIG for the "pinned-research" archetype
# (ORDER 018 R2: ALL logic lives in environments/setup-base.sh — one lineage)
#
# Canonical copy: menno420/fleet-manager · environments/archetype-pinned-research.sh
# Serves: trading-strategy, websites.
# Shape: pinned-requirements Python research/service lane; zero-to-few
# secrets; no local DB/Docker; may be a TWO-SOURCE workspace (the bare
# trading-strategy + substrate-kit checkout that killed three sessions at
# provision — the base's multi-repo branch is tested against exactly it) and
# may ship SEVERAL requirements files (websites has three: root + botsite/ +
# dashboard/ — the base installs each individually). The base also honors
# websites' committed hook name scripts/setup-env.sh.
# Knob table: environments/archetypes.md § "The base shim + knob table".
# CONTRACT (playbook R15, inherited from the base): ALWAYS exits 0.
# ---------------------------------------------------------------------------
set +e

# --- knobs -------------------------------------------------------------------
ARCH_NAME="pinned-research"
BASELINE_PIP="pytest python-multipart"  # pytest is CI's runner and absent from
                                        # fresh containers; python-multipart is
                                        # websites' known extra
PICK_PYTHON_TABLE=""               # both lanes want >=3.11; container default
                                   # python3 (3.11.x) satisfies both
# websites' lane vars (spec §2 check set incl. platform-injected GITHUB_TOKEN
# — its absence is a platform signal); trading needs none. Presence only.
ENV_REPORT="GITHUB_TOKEN GITHUB_PAT RAILWAY_API_KEY SITE_PASSWORD DATABASE_URL"
GIT_TRIAGE=1                       # git-state triage (detached HEAD / dirty
                                   # tree residue report — never mutates)

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
