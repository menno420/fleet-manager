#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# setup-script.sh — Builder seat environment setup (superbot-next)
#
# Derived from the repo's ACTUAL manifests at origin/main @ 9757755:
#   - requirements.txt   = human-edited constraint input (S13, spec 12 §2.C)
#   - requirements.lock  = the deployable set — hash-pinned (pip-compile
#     --generate-hashes); the container installs
#         pip install --require-hashes -r requirements.lock
#   - pyproject.toml     = requires-python ">=3.11"; dependencies read
#     DYNAMICALLY from requirements.txt (one source of truth)
#   - every CI job (ci.yml, named-gates.yml, golden-parity.yml) pins
#     python "3.11" — the interpreter below matches CI, not bare python3.
#
# Pattern: fleet-manager environments/archetype-bot-prod.sh (canonical for
# this repo per the Builder founding package §3) — fail-soft contract (R15):
# NEVER fail the session, always exit 0; report, never mutate.
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture ---------------------------------------------
set +e          # a non-zero step must not abort the script
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:superbot-next] $*"; }

# --- Block 2: interpreter selection (CI parity: py3.11) ----------------------
if command -v python3.11 >/dev/null 2>&1; then
  PY=python3.11
else
  log "WARNING: python3.11 not found — falling back to python3 (CI-parity risk: every superbot-next CI job pins 3.11)"
  PY=python3
fi
log "interpreter: $($PY --version 2>&1)"

# --- Block 2b: workspace-residue advisory (report only — NEVER mutate) -------
if [ -d .git ]; then
  branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)" || branch=""
  dirty="$(git status --porcelain 2>/dev/null | head -1)" || dirty=""
  if [ -n "$branch" ] && [ "$branch" != "main" ]; then
    log "NOTE — on branch '$branch' (possible previous-session residue)."
    log "       recovery if stale: git checkout main && git pull --ff-only"
  fi
  [ -n "$dirty" ] && log "NOTE — working tree is dirty (uncommitted changes inherited or in progress)."
fi

# --- Block 3: dependency install (lockfile-first, per the repo's own docs) ---
# Detection order mirrors archetype-bot-prod.sh: repo's own env-setup.sh >
# hash-pinned lock > plain requirements > skip.
if [ -f scripts/env-setup.sh ]; then
  log "running scripts/env-setup.sh (repo knows best)"
  bash scripts/env-setup.sh || log "env-setup.sh failed (non-fatal, continuing)"
elif [ -f requirements.lock ]; then
  log "$PY -m pip install --require-hashes -r requirements.lock"
  "$PY" -m pip install --quiet --require-hashes -r requirements.lock \
    || log "lockfile install failed (non-fatal, continuing)"
elif [ -f requirements.txt ]; then
  log "$PY -m pip install -r requirements.txt"
  "$PY" -m pip install --quiet -r requirements.txt \
    || log "pip install failed (non-fatal, continuing)"
else
  log "no dependency manifest found — skipping install"
fi

# Test tooling (ci.yml `tests` job installs only pytest + pyyaml; the unit
# suite deliberately runs WITHOUT runtime deps — guarded-import discipline).
"$PY" -m pip install --quiet pytest pyyaml pip-tools \
  || log "test-tooling install failed (non-fatal, continuing)"

# --- Block 4: capability probe block (websites pattern — presence, no values) -
# Discovery rule: check the env → report NAMES only, never values. A missing
# var is a FINDING for docs/CAPABILITIES.md, not a wall — the session attempts
# once and captures the exact error before flagging anything to the owner.

# Fail-fast boot trio (sb/spec/config.py CONFIG_FIELDS, required=True):
for v in DISCORD_BOT_TOKEN_PRODUCTION DATABASE_URL SB_DATA_PLANE; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then
    log "env: $v is set"
  else
    log "env: $v is NOT set (bot boot will fail-fast; unit tests are fine)"
  fi
done

# Live-drive set (band-5+ legs; LIVE-VERIFIED present at 9757755):
for v in SB_APPCMD_SYNC_GUILD_ID SB_INTENT_MSGCONTENT_OK SB_INTENT_MEMBERS_OK; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then
    log "env: $v is set"
  else
    log "env: $v is NOT set (live-drive leg degrades; flag, don't stall)"
  fi
done

# SB_TEST_DB_HOSTS is OPTIONAL AND SILENT (Q-0263.1 / inbox ORDER 011, done):
# absent => any host accepted on the test plane, one loud log at boot.
# NEVER ask the owner for it; do not report it as missing.
[ -n "${SB_TEST_DB_HOSTS:-}" ] && log "env: SB_TEST_DB_HOSTS is set (opt-in allowlist engaged)"

# Container fact (control/status.md live-drive record): HEALTH_HOST default
# '::' cannot bind in this build container (no IPv6) — 127.0.0.1 required.
if [ -z "${HEALTH_HOST:-}" ]; then
  log "env: HEALTH_HOST unset — live boots in this container need HEALTH_HOST=127.0.0.1 (default :: has no IPv6 here)"
fi

# Band-7 deferred set (grant when band 7 starts — never required now):
for v in ANTHROPIC_API_KEY AI_ENABLED; do
  [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ] && log "env: $v is set (band-7 envelope present)"
done

# Postgres probe (parity replay + live boot both need one; report only):
if command -v pg_isready >/dev/null 2>&1; then
  pg_isready >/dev/null 2>&1 && log "postgres: pg_isready OK" \
    || log "postgres: pg_isready NOT ready (parity replay/live boot need a reachable Postgres)"
else
  log "postgres: pg_isready not on PATH (client tools absent — probe skipped)"
fi

# --- Block 5: unconditional success -------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
