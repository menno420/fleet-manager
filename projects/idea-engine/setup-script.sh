#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# setup-script.sh — environment setup for the idea-engine seat (core seat 4)
#
# Package part 3 of 4. Derived from the fleet canonical defensive shim
# (fleet-manager environments/templates/setup-universal.sh via
# archetype-python-lab.sh @ fleet-manager 0eaa668) — the founding package §0.3
# specified archetype-python-lab.sh VERBATIM for this env; this copy keeps
# that contract and adds the websites-pattern capability probe (fail-soft,
# findings logged, nothing gates).
#
# Repo reality at idea-engine HEAD c8651f7: NO requirements.txt, NO
# pyproject.toml — bootstrap.py + scripts/{preflight,check_ideas,
# check_sections}.py are pure stdlib (verified by import scan). The baseline
# dev tools below are the archetype's, kept for parity (fresh containers lack
# pytest) and for future manifest growth: the per-repo detection branches stay
# so a later requirements.txt is picked up with zero script changes.
#
# CONTRACT (playbook R15): NEVER fails the session — every step non-fatal,
# ALWAYS exits 0. Never assumes cwd is a git repo (works on a bare
# multi-source checkout: cwd with repos as subdirectories).
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture ---------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:idea-engine] $*"; }

# --- Block 2: archetype baseline (best-effort, non-fatal) -------------------
# idea-engine is stdlib-only today; pytest/ruff cover the kit's check paths
# and any future test surface. `build` kept for archetype parity.
log "baseline dev tools: pytest ruff build"
python3 -m pip install --quiet pytest ruff build \
  || log "dev-tools install failed (non-fatal, continuing)"

# --- Block 3: per-repo setup -------------------------------------------------
# Detection order, most-specific first (every branch guarded):
#   1. scripts/env-setup.sh  -> the repo knows best.
#   2. requirements.txt      -> pip install it (existence-guarded).
#   3. pyproject.toml        -> editable install, [dev] first, bare -e . next.
#   4. nothing               -> skip silently (idea-engine's current branch).
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/requirements.txt" ]; then
    log "$name: python3 -m pip install -r requirements.txt"
    ( cd "$repo_dir" && python3 -m pip install --quiet -r requirements.txt ) \
      || log "$name: pip install failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/pyproject.toml" ]; then
    log "$name: editable install from pyproject.toml"
    ( cd "$repo_dir" && python3 -m pip install --quiet -e '.[dev]' ) \
      || ( cd "$repo_dir" && python3 -m pip install --quiet -e . ) \
      || log "$name: editable install failed (non-fatal, continuing)"
  else
    log "$name: no manifest — skipping (stdlib-only lane; expected for idea-engine)"
  fi
}

# --- Block 4: multi-repo vs single-repo detection ---------------------------
if [ -d .git ]; then
  setup_one "$PWD"
else
  found=0
  for d in */; do
    [ -d "$d/.git" ] || continue
    found=1
    setup_one "$PWD/${d%/}"
  done
  [ "$found" -eq 1 ] || setup_one "$PWD"
fi

# --- Block 5: capability probe (websites pattern — observe, log, never gate) -
# Feeds docs/CAPABILITIES.md's discovery rule: one cheap verified fact per
# line, so the first session starts from findings, not assumptions. Every
# probe is read-only and non-fatal.
log "--- capability probe (informational only) ---"
log "python3: $(python3 --version 2>&1 || echo 'MISSING')"
log "git: $(git --version 2>&1 || echo 'MISSING')"
python3 -c "import pytest" 2>/dev/null && log "pytest importable: yes" || log "pytest importable: NO"
# Kit gate: the one command a wake runs first (stdlib; repo-local).
if [ -f "bootstrap.py" ]; then
  python3 bootstrap.py check --strict --status-only >/dev/null 2>&1 \
    && log "kit control gate: green" \
    || log "kit control gate: red/unavailable (informational — first session investigates)"
elif [ -f "idea-engine/bootstrap.py" ]; then
  ( cd idea-engine && python3 bootstrap.py check --strict --status-only >/dev/null 2>&1 ) \
    && log "kit control gate: green" \
    || log "kit control gate: red/unavailable (informational — first session investigates)"
else
  log "kit control gate: bootstrap.py not found at this layout (informational)"
fi
# Harvest path: this seat reads every other lane via public raw (Q-0260).
# curl may ride the platform proxy; a failure here is a FINDING, not an error.
raw_probe="https://raw.githubusercontent.com/menno420/idea-engine/main/README.md"
if command -v curl >/dev/null 2>&1; then
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$raw_probe" 2>/dev/null)"
  log "public raw read (harvest path): HTTP ${code:-no-response} for $raw_probe"
else
  log "public raw read: curl MISSING (record in CAPABILITIES.md; MCP raw reads may still work)"
fi
log "--- probe end ---"

# --- Block 6: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
