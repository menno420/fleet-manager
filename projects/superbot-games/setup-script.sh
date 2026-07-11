#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# setup-script.sh — superbot-games (Seat A) environment setup
# v2 · 2026-07-11 · fleet-manager projects registry
#
# Part 3 of the superbot-games Project package. Owner pastes this into
# claude.ai/code → Environments → <env> → Setup script.
#
# *** DEPLOYED STATE: NEVER-DEPLOYED AS-WRITTEN (registry draft). ***
# No paste receipt exists for this script; the seat SELF-BOOTED 2026-07-10
# and runs without a registry-verified Setup-script field. What verifiably
# EXISTS at origin/main 773fab0: three scripts in the repo —
# scripts/env-setup.sh (kit-standard), environment/setup-exploration.sh,
# environments/setup-mining.sh (gen-1 per-lane, inconsistent dirs; v1's
# canonical-home consolidation was never executed). This draft remains the
# registry's canonicalized derivation of those (see meta.md deployed-state
# table); refreshed v2 for post-ORDER-001 reality (gate fixed, floor 230).
#
# Python deps — from the ACTUAL manifests: the repo has NO requirements.txt
# and NO pyproject.toml (pure-stdlib domain code); CI (tests.yml) installs
# exactly `pytest`. So: pytest only, best-effort. bootstrap.py needs python3.
#
# CONTRACT (fleet playbook R15): NEVER fails the session — every step
# non-fatal, ALWAYS exits 0.
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture ---------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:superbot-games] $*"; }
log "starting defensive bootstrap ($(date -u 2>/dev/null || echo 'date unavailable'))"

# --- Block 2: interpreter + baseline toolchain -------------------------------
# CI uses setup-python "3.x"; the domain is stdlib-only. pytest is the one dep
# CI installs (tests.yml) — mirror exactly that, nothing more.
PY=""
for cand in python3 python; do
  command -v "$cand" >/dev/null 2>&1 && PY="$cand" && break
done
if [ -n "$PY" ]; then
  log "python: $PY ($("$PY" --version 2>&1))"
  "$PY" -m pip --version >/dev/null 2>&1 || "$PY" -m ensurepip --upgrade >/dev/null 2>&1 \
    || log "WARN: pip/ensurepip unavailable — continuing"
  "$PY" -m pip install --quiet --disable-pip-version-check pytest >/dev/null 2>&1 \
    && log "installed: pytest" \
    || log "WARN: pytest install failed (non-fatal, continuing)"
else
  log "WARN: no python interpreter on PATH — session must self-report this"
fi

# --- Block 3: per-repo setup (fleet-template detection order, guarded) -------
setup_one() {
  repo_dir="$1"; name="$(basename "$repo_dir")"
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal)"
  elif [ -f "$repo_dir/requirements.txt" ]; then
    log "$name: pip install -r requirements.txt"
    ( cd "$repo_dir" && "$PY" -m pip install --quiet -r requirements.txt ) \
      || log "$name: pip install failed (non-fatal)"
  else
    log "$name: no manifest — pure-stdlib lane, nothing to install"
  fi

  # Kit hygiene probe (informational, never fatal)
  if [ -n "$PY" ] && [ -f "$repo_dir/bootstrap.py" ]; then
    ( cd "$repo_dir" && "$PY" bootstrap.py check >/dev/null 2>&1 ) \
      && log "$name: bootstrap.py check — green" \
      || log "$name: bootstrap.py check reported findings / could not run (non-fatal; re-run in-session)"
  fi

  # Full-collection probe (informational): ORDER 001's collect-ALL-suites fix
  # is MERGED (PR #24, merge 7d4c347) — CI itself now floors the count (230 at
  # 773fab0). Print the real collected count so the session sees it at boot.
  if [ -n "$PY" ] && [ -d "$repo_dir/tests" ]; then
    count="$( cd "$repo_dir" && "$PY" -m pytest --collect-only -q tests/ games/exploration/tests/ 2>/dev/null | tail -1 )"
    log "$name: full-collection probe (tests/ + games/exploration/tests/): ${count:-unavailable} (CI floor: 230 at 773fab0 — check tests.yml for current)"
  fi
}

# --- Block 4: multi-repo vs single-repo detection (fleet-template shape) -----
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

# --- Block 5: capability probes (report-only — NEVER mutate, NEVER fatal) -----
# Git identity + push path + branch residue; scheduler MCP tools canNOT be
# probed from bash (seat-dependent, ORDER 002 wall) — re-probe in-session.
if command -v git >/dev/null 2>&1 && [ -d .git ]; then
  branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null)"
  [ -n "$branch" ] && [ "$branch" != "main" ] \
    && log "NOTE: on branch '$branch' (previous-session residue?) — recover: git checkout main && git pull --ff-only"
  git ls-remote --heads origin >/dev/null 2>&1 \
    && log "probe: git remote reachable (ls-remote ok)" \
    || log "probe: git ls-remote FAILED — record the exact error in-session before declaring a wall"
  [ -n "$(git status --porcelain 2>/dev/null | head -1)" ] && log "NOTE: working tree dirty"
fi
log "probe: scheduler/GitHub MCP tools are seat-dependent (gen-1 mining wall on record: 'No such tool available: mcp__claude-code-remote__send_later'; the LIVE Seat A session armed trig_019ZgWyL78Rx1sr6LhvL8NE3 successfully 2026-07-10T23:47Z) — probe in-session, once, capture verbatim"

# --- Block 6: env var contract (NAMES only — never values) --------------------
# This lane needs NO secrets: pure-stdlib, no live infra, no DB, no Discord
# token (host integration is superbot-next's job). Platform-provided only:
#   GITHUB_TOKEN (or platform git-proxy equivalent); HTTPS_PROXY/SSL cert vars
#   (platform-managed — do not unset).
# Explicitly NOT needed (Block-4 ban, archetype ledger): Railway IDs (they
# point at the PRODUCTION bot), Discord tokens, DB URLs, Anthropic keys.
log "env vars: none needed beyond platform git access"

# --- Block 7: unconditional success -------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
