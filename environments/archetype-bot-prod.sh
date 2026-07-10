#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-bot-prod.sh — setup script for the "bot-prod" archetype
#
# Canonical copy: menno420/fleet-manager · environments/archetype-bot-prod.sh
# Serves: superbot-next, superbot (legacy). The ONLY archetype that may carry
# production-pointing vars (DISCORD_BOT_TOKEN_PRODUCTION, DATABASE_URL, the
# Railway trio) — every other archetype EXCLUDES them (env-vars.md DANGER rule).
# Shape: production Discord bot; Postgres required; hash-pinned lockfile
# (superbot-next) / 3.10-pinned requirements (legacy superbot).
#
# Derived from environments/templates/setup-universal.sh. CONTRACT (playbook
# R15): NEVER fails the session — always exit 0; never assumes cwd is a repo.
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture --------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:bot-prod] $*"; }

# --- Block 2: interpreter selection ------------------------------------------
# CI-parity pins, per repo name (2026-07-10 finding: env templates must pin
# the interpreter to match each repo's OWN CI — the pins diverge per repo):
#   superbot      -> python3.10 (code-quality.yml pins "3.10"; CLAUDE.md
#                    CI-parity section — bare python3 is 3.11.x in-container
#                    and installs into the wrong site-packages; the
#                    multi-repo.md wrinkle #1).
#   superbot-next -> python3.11 (every ci.yml / named-gates / golden-parity /
#                    restore-verify job pins "3.11"; next#97's local gates ran
#                    on py3.11 — keep it explicit rather than relying on the
#                    container's bare python3 happening to be 3.11.x).
# A repo's own scripts/env-setup.sh (preferred automatically below) remains
# the durable fix.
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
    superbot-next)
      if command -v python3.11 >/dev/null 2>&1; then
        echo python3.11
      else
        log "WARNING: python3.11 not found for superbot-next — falling back to python3 (CI-parity risk)"
        echo python3
      fi
      ;;
    *) echo python3 ;;
  esac
}

# --- Block 2b: workspace-residue advisory (report only — NEVER mutate) -------
# Persistent workspaces inherit the previous session's clone on a dead branch
# with a dirty tree (2026-07-10 fleet finding). A setup script must never
# checkout/reset on its own (it could destroy in-progress work), so this only
# REPORTS the state and prints the recovery line for the session to run.
residue_check() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  branch="$(git -C "$repo_dir" rev-parse --abbrev-ref HEAD 2>/dev/null)" || branch=""
  dirty="$(git -C "$repo_dir" status --porcelain 2>/dev/null | head -1)" || dirty=""
  if [ -n "$branch" ] && [ "$branch" != "main" ] && [ "$branch" != "master" ]; then
    log "$name: NOTE — on branch '$branch' (possible previous-session residue)."
    log "$name:        recovery if stale: git checkout main && git pull --ff-only"
  fi
  if [ -n "$dirty" ]; then
    log "$name: NOTE — working tree is dirty (uncommitted changes inherited or in progress)."
  fi
}

# --- Block 3: per-repo setup -------------------------------------------------
# Detection order, most-specific first (every branch guarded):
#   1. scripts/env-setup.sh -> the repo knows best (interpreter-pin hatch).
#   2. requirements.lock    -> hash-pinned install (superbot-next's deployable
#      set: pip install --require-hashes -r requirements.lock).
#   3. requirements.txt     -> plain pinned install (legacy superbot).
#   4. nothing              -> skip silently.
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  py="$(pick_python "$repo_dir")"
  residue_check "$repo_dir"
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/requirements.lock" ]; then
    log "$name: $py -m pip install --require-hashes -r requirements.lock"
    ( cd "$repo_dir" && "$py" -m pip install --quiet --require-hashes -r requirements.lock ) \
      || log "$name: lockfile install failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/requirements.txt" ]; then
    log "$name: $py -m pip install -r requirements.txt"
    ( cd "$repo_dir" && "$py" -m pip install --quiet -r requirements.txt ) \
      || log "$name: pip install failed (non-fatal, continuing)"
  else
    log "$name: no manifest — skipping"
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

# --- Block 5: env var presence report (NAMES only — never values) ------------
# The fail-fast trio superbot-next refuses to boot without (sb/spec/config.py:
# DISCORD_BOT_TOKEN_PRODUCTION + DATABASE_URL + SB_DATA_PLANE, all
# required=True, fail-fast posture). Presence only — a test-plane session may
# legitimately lack them.
for v in DISCORD_BOT_TOKEN_PRODUCTION DATABASE_URL SB_DATA_PLANE; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then
    log "env: $v is set"
  else
    log "env: $v is NOT set (bot boot will fail-fast; tests may be fine)"
  fi
done
# Legacy superbot's third deploy-required var (docs/operations/env-vars.md
# "Required" table; read without a default at services/youtube_fetch_service.py
# — degrades with a warning rather than fail-fast, so reported softer).
for v in YOUTUBE_API_KEY; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then
    log "env: $v is set"
  else
    log "env: $v is NOT set (legacy superbot deploy-required; YouTube features degrade)"
  fi
done

# --- Block 6: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
