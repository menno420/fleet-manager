#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-coordinator.sh — setup script for the "coordinator" archetype
#
# Canonical copy: menno420/fleet-manager · environments/archetype-coordinator.sh
# Serves: the live `multi-repo` coordinator workspace (fleet-manager sessions
# steering N repos at once: substrate-kit, superbot, superbot-games,
# superbot-next, websites, ... as children of the working dir).
# Shape: cwd is a WORKSPACE, not a repo — the exact shape whose mishandling
# killed sessions in 4+ lanes. Superset behavior: handles every manifest kind
# any child repo may ship (env-setup.sh, requirements.lock, requirements*.txt,
# pyproject.toml) plus the dual-interpreter wrinkle.
#
# Derived from environments/templates/setup-universal.sh. CONTRACT (playbook
# R15): NEVER fails the session — always exit 0. One broken child repo must
# never block the others.
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture --------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:coordinator] $*"; }

# --- Block 2: archetype baseline (best-effort, non-fatal) -------------------
log "baseline dev tools: pytest ruff"
python3 -m pip install --quiet pytest ruff \
  || log "dev-tools install failed (non-fatal, continuing)"

# --- Block 3: interpreter selection ------------------------------------------
# THE 3.10-vs-3.11 wrinkle (environments/multi-repo.md #1): bare python3 is
# 3.11.x; legacy superbot needs python3.10 for CI parity. Pin by repo name;
# a repo's own scripts/env-setup.sh (preferred below) is the durable fix.
pick_python() {
  case "$(basename "$1")" in
    superbot)
      if command -v python3.10 >/dev/null 2>&1; then
        echo python3.10
      else
        log "WARNING: python3.10 not found for superbot — falling back to python3 (CI-parity risk)"
        echo python3
      fi
      ;;
    *) echo python3 ;;
  esac
}

# --- Block 4: per-repo setup -------------------------------------------------
# Detection order, most-specific first (every branch guarded):
#   1. scripts/env-setup.sh -> the repo knows best.
#   2. requirements.lock    -> hash-pinned install (superbot-next).
#   3. requirements*.txt (depth 2) -> each individually, non-fatally
#      (websites ships three).
#   4. pyproject.toml       -> editable install, [dev] first, -e . fallback.
#   5. nothing              -> skip silently (docs-only repo is fine).
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  py="$(pick_python "$repo_dir")"
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/requirements.lock" ]; then
    log "$name: $py -m pip install --require-hashes -r requirements.lock"
    ( cd "$repo_dir" && "$py" -m pip install --quiet --require-hashes -r requirements.lock ) \
      || log "$name: lockfile install failed (non-fatal, continuing)"
  else
    reqs="$(find "$repo_dir" -maxdepth 2 -name 'requirements*.txt' -not -path '*/.git/*' 2>/dev/null)"
    if [ -n "$reqs" ]; then
      printf '%s\n' "$reqs" | while IFS= read -r req; do
        [ -f "$req" ] || continue
        log "$name: $py -m pip install -r ${req#"$repo_dir"/}"
        ( cd "$repo_dir" && "$py" -m pip install --quiet -r "$req" ) \
          || log "$name: install of $req failed (non-fatal, continuing)"
      done
    elif [ -f "$repo_dir/pyproject.toml" ]; then
      log "$name: editable install from pyproject.toml"
      ( cd "$repo_dir" && python3 -m pip install --quiet -e '.[dev]' ) \
        || ( cd "$repo_dir" && python3 -m pip install --quiet -e . ) \
        || log "$name: editable install failed (non-fatal, continuing)"
    else
      log "$name: no manifest — skipping"
    fi
  fi
}

# --- Block 5: multi-repo vs single-repo detection ---------------------------
# Coordinator's home shape is the multi-repo branch; the single-repo branch
# keeps the script correct if it's ever pasted into a one-repo env.
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

# --- Block 6: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
