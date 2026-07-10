#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# setup-script.sh — superbot-games (merged games-plugins lane) environment setup
#
# Part 3 of the superbot-games Project package. Owner pastes this into
# claude.ai/code → Environments → <env> → Setup script.
#
# CANONICALIZED 2026-07-10 from the repo's TWO existing setup scripts, which
# live in INCONSISTENT directories at origin/main @ 4493292:
#   - environment/setup-exploration.sh  (singular dir; fleet-template mirror,
#     TESTED 2026-07-09: two runs, repo dir + clean dir, exit 0 both — PR #13)
#   - environments/setup-mining.sh      (plural dir; adds pytest install +
#     kit-check + test-smoke probes — PR #14)
# Base = exploration's (the tested fleet-template shape, matching
# fleet-manager environments/archetype-python-lab.sh, whose header lists
# superbot-games as a consumer); mining's pytest/kit/test probes folded in;
# capability-probe block added (websites docs/project/setup-script.sh
# pattern). CANONICAL HOME going forward: environments/ (plural — the fleet
# convention); the first session should commit this file there and retire the
# two per-lane scripts (flagged in meta.md).
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

  # ORDER-001 collection probe (informational): the CI gate collects 73/121
  # until the collect-ALL-suites fix lands — print the REAL collected count so
  # the session sees the truth at boot. Floor today: 121.
  if [ -n "$PY" ] && [ -d "$repo_dir/tests" ]; then
    count="$( cd "$repo_dir" && "$PY" -m pytest --collect-only -q tests/ games/exploration/tests/ 2>/dev/null | tail -1 )"
    log "$name: full-collection probe (tests/ + games/exploration/tests/): ${count:-unavailable} (expected floor: 121)"
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
log "probe: scheduler/GitHub MCP tools are seat-dependent (mining wall on record: 'No such tool available: mcp__claude-code-remote__send_later') — probe in-session, once, capture verbatim"

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
