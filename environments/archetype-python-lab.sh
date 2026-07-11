#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-python-lab.sh — setup script for the "python-lab" archetype
#
# Canonical copy: menno420/fleet-manager · environments/archetype-python-lab.sh
# Serves: substrate-kit, codetool-lab-fable5, codetool-lab-opus4.8,
#         codetool-lab-sonnet5, superbot-games, fleet-manager, venture-lab,
#         sim-lab, product-forge, idea-engine, superbot-idle, mobile-lab.
# Shape: stdlib-or-tiny-deps Python lab; zero secrets; no services.
#
# Derived from environments/templates/setup-universal.sh (the fleet canonical
# shim). CONTRACT (playbook R15): NEVER fails the session — every step is
# non-fatal and the script ALWAYS exits 0. Never assumes cwd is a git repo
# (works on a bare multi-source checkout: cwd with repos as subdirectories).
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture --------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:python-lab] $*"; }

# --- Block 2: archetype baseline (best-effort, non-fatal) -------------------
# Every lab lane needs the dev tools even when the repo has no manifest at all
# (substrate-kit is stdlib-only with NO requirements.txt; fresh containers
# lack pytest — verified). `build` covers the packaged labs (hatchling).
log "baseline dev tools: pytest ruff build"
python3 -m pip install --quiet pytest ruff build \
  || log "dev-tools install failed (non-fatal, continuing)"

# --- Block 3: per-repo setup -------------------------------------------------
# Detection order, most-specific first (every branch guarded):
#   1. scripts/env-setup.sh  -> the repo knows best (also the interpreter-pin
#      escape hatch).
#   2. requirements.txt      -> pip install it (guarded by existence check —
#      NEVER a bare `pip install -r`).
#   3. pyproject.toml        -> editable install, [dev] extra first, bare -e .
#      as fallback (the codetool labs' proven path).
#   4. nothing               -> skip silently (docs-only repo is fine).
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
    log "$name: no manifest — skipping (stdlib-only lane is fine)"
  fi
}

# --- Block 4: multi-repo vs single-repo detection ---------------------------
# Multi-source environment: cwd is a WORKSPACE whose child dirs are the git
# clones (this exact shape, unhandled, killed sessions in 4+ lanes).
# Single-repo environment: cwd IS the repo (it has .git).
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

# --- Block 5: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
