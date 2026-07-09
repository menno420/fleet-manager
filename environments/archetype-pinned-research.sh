#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-pinned-research.sh — setup script for the "pinned-research" archetype
#
# Canonical copy: menno420/fleet-manager · environments/archetype-pinned-research.sh
# Serves: trading-strategy, websites.
# Shape: pinned-requirements Python research/service lane; zero-to-few secrets;
#        no local DB/Docker; may ship SEVERAL requirements files (websites has
#        three: root + botsite/ + dashboard/).
#
# Derived from environments/templates/setup-universal.sh. CONTRACT (playbook
# R15): NEVER fails the session — always exit 0. THE archetype contract, paid
# for in blood (trading-strategy lost 2 sessions at provision): "the setup
# script must exit 0 on a bare two-source checkout (cwd containing
# trading-strategy/ and substrate-kit/), install only from a repo's own
# manifest, and never assume its cwd is a git repository."
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture --------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:pinned-research] $*"; }

# --- Block 2: archetype baseline (best-effort, non-fatal) -------------------
# pytest is CI's runner and absent from fresh containers (verified);
# python-multipart is websites' known extra beyond its requirements files.
log "baseline extras: pytest python-multipart"
python3 -m pip install --quiet pytest python-multipart \
  || log "extras install failed (non-fatal, continuing)"

# --- Block 3: per-repo setup -------------------------------------------------
# Detection order, most-specific first (every branch guarded):
#   1. scripts/env-setup.sh    -> the repo knows best (interpreter-pin hatch).
#   2. requirements*.txt up to depth 2 -> install EACH individually and
#      non-fatally (websites ships three; one broken file must not block the
#      rest). Existence is guaranteed by find — NEVER a bare `pip install -r`.
#   3. nothing                 -> skip silently.
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal, continuing)"
  else
    reqs="$(find "$repo_dir" -maxdepth 2 -name 'requirements*.txt' -not -path '*/.git/*' 2>/dev/null)"
    if [ -n "$reqs" ]; then
      printf '%s\n' "$reqs" | while IFS= read -r req; do
        [ -f "$req" ] || continue
        log "$name: python3 -m pip install -r ${req#"$repo_dir"/}"
        ( cd "$repo_dir" && python3 -m pip install --quiet -r "$req" ) \
          || log "$name: install of $req failed (non-fatal, continuing)"
      done
    else
      log "$name: no scripts/env-setup.sh or requirements*.txt — skipping"
    fi
  fi
}

# --- Block 4: multi-repo vs single-repo detection ---------------------------
# Multi-source environment: cwd is a WORKSPACE whose child dirs are the git
# clones — trading-strategy's live shape is /home/user containing
# trading-strategy/ + substrate-kit/. The original script assumed single-repo
# cwd here and died (exit 1, 2 dead sessions). This branch is the fix.
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

# --- Block 5: env var presence report (NAMES only — never values) ------------
# websites' lane vars; trading needs none. Presence only, for boot triage.
for v in GITHUB_PAT RAILWAY_API_KEY SITE_PASSWORD DATABASE_URL; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then
    log "env: $v is set"
  else
    log "env: $v is NOT set (fine unless this lane needs it)"
  fi
done

# --- Block 6: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
