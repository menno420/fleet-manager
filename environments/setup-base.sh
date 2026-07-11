#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# setup-base.sh — the fleet's ONE consolidated setup base shim (ORDER 018 R2)
#
# Canonical copy: menno420/fleet-manager · environments/setup-base.sh
# The 4 Python-family archetype scripts (python-lab, coordinator, bot-prod,
# pinned-research) are THIN CONFIGS over this file: each sets the knobs below
# and sources it. gba-lab stays genuinely separate (heavy apt/mirror/source
# toolchain — audit §4.2). Knob table + per-archetype values:
# environments/archetypes.md § "The base shim + knob table".
#
# KNOBS (set by the sourcing config BEFORE sourcing; all optional):
#   ARCH_NAME          log tag (default "base")
#   BASELINE_PIP       space-separated pip packages installed once up front
#   PICK_PYTHON_TABLE  space-separated repo=interpreter CI-parity pins, e.g.
#                      "superbot=python3.10 superbot-next=python3.11".
#                      Missing interpreter -> loud WARN + python3 fallback.
#   ENV_REPORT         space-separated env var NAMES to presence-report
#                      (NAMES only — NEVER values; registry hard rule)
#   ENV_REPORT_HINT    suffix for the NOT-set line (archetype context)
#   GIT_TRIAGE         1 = report per-repo branch/dirty state (NEVER mutates)
#
# Derived from environments/templates/setup-universal.sh. The manifest ladder
# below is the coordinator superset (audit §4.2: coordinator's setup_one is a
# strict superset of python-lab / bot-prod / pinned-research handling).
# CONTRACT (playbook R15): NEVER fails the session — every step is non-fatal
# and the script ALWAYS exits 0. Never assumes cwd is a git repo (works on a
# bare multi-source checkout: cwd with repos as subdirectories).
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture --------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore

ARCH_NAME="${ARCH_NAME:-base}"
log() { echo "[env-setup:$ARCH_NAME] $*"; }
log "python: $(python3 --version 2>&1 || echo 'python3 MISSING')"

# --- Block 2: archetype baseline (best-effort, non-fatal) -------------------
if [ -n "${BASELINE_PIP:-}" ]; then
  log "baseline pip: $BASELINE_PIP"
  # shellcheck disable=SC2086 — word-splitting the package list is intended
  python3 -m pip install --quiet ${BASELINE_PIP} \
    || log "baseline install failed (non-fatal, continuing)"
fi

# --- Block 3: interpreter selection (CI-parity pin table) --------------------
# THE 3.10-vs-3.11 wrinkle (environments/multi-repo.md #1). The pin table is
# DATA, so every archetype that sets it carries every case — including the
# superbot-next→python3.11 pin the coordinator script previously lacked
# (audit §4.2 latent bug, fixed here). A repo's own scripts/env-setup.sh
# (preferred automatically below) remains the durable fix.
pick_python() {
  _name="$(basename "$1")"
  for _pair in ${PICK_PYTHON_TABLE:-}; do
    case "$_pair" in
      "$_name="*)
        _want="${_pair#*=}"
        if command -v "$_want" >/dev/null 2>&1; then
          echo "$_want"
        else
          # >&2: pick_python is command-substituted — a stdout warning would
          # be captured INTO $py and corrupt the interpreter name (latent bug
          # in the pre-consolidation scripts, fixed here).
          log "WARNING: $_want not found for $_name — falling back to python3 (CI-parity risk)" >&2
          echo python3
        fi
        return
        ;;
    esac
  done
  echo python3
}

# --- Block 3b: git-state triage (report only — NEVER mutate) -----------------
# Persistent workspaces inherit the previous session's clone on a dead branch
# with a dirty tree (2026-07-10 fleet finding). A setup script must never
# checkout/reset on its own; this only REPORTS and prints the recovery line.
git_triage() {
  [ "${GIT_TRIAGE:-0}" = "1" ] || return 0
  _dir="$1"
  _n="$(basename "$_dir")"
  command -v git >/dev/null 2>&1 || return 0
  [ -d "$_dir/.git" ] || return 0
  _br="$(git -C "$_dir" symbolic-ref --short -q HEAD 2>/dev/null || echo 'DETACHED HEAD — branch before committing')"
  _dirty=""
  [ -n "$(git -C "$_dir" status --porcelain 2>/dev/null | head -1)" ] \
    && _dirty=" · DIRTY TREE (residue? git checkout main && git pull --ff-only)"
  log "$_n: git: ${_br}${_dirty}"
}

# --- Block 4: per-repo setup (the coordinator-superset manifest ladder) ------
# Detection order, most-specific first (every branch guarded):
#   1. scripts/env-setup.sh OR scripts/setup-env.sh -> the repo knows best
#      (interpreter-pin escape hatch; websites' committed name is setup-env.sh).
#   2. requirements.lock    -> hash-pinned install (superbot-next).
#   3. requirements*.txt (depth 2) -> each individually, non-fatally
#      (websites ships three; one broken file must not block the rest).
#   4. pyproject.toml       -> editable install, [dev] first, -e . fallback
#      (the codetool labs' proven path).
#   5. nothing              -> skip silently (docs-only/stdlib repo is fine).
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  py="$(pick_python "$repo_dir")"
  git_triage "$repo_dir"
  hook=""
  for h in scripts/env-setup.sh scripts/setup-env.sh; do
    if [ -f "$repo_dir/$h" ]; then hook="$h"; break; fi
  done
  if [ -n "$hook" ]; then
    log "$name: running $hook"
    ( cd "$repo_dir" && bash "$hook" ) \
      || log "$name: $hook failed (non-fatal, continuing)"
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
      ( cd "$repo_dir" && "$py" -m pip install --quiet -e '.[dev]' ) \
        || ( cd "$repo_dir" && "$py" -m pip install --quiet -e . ) \
        || log "$name: editable install failed (non-fatal, continuing)"
    else
      log "$name: no manifest — skipping (docs-only/stdlib lane is fine)"
    fi
  fi
}

# --- Block 5: multi-repo vs single-repo detection ---------------------------
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

# --- Block 6: env var presence report (NAMES only — never values) ------------
for v in ${ENV_REPORT:-}; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then
    log "env: $v is set"
  else
    log "env: $v is NOT set (${ENV_REPORT_HINT:-fine unless this lane needs it})"
  fi
done

# --- Block 7: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
