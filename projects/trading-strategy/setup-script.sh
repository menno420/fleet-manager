#!/usr/bin/env bash
# trading-strategy — Claude Project ENVIRONMENT setup script.
# Part 3 of the trading-strategy Project package. Paste into: claude.ai
# console → trading-strategy Project → environment settings → "Setup script"
# field. Source of truth is this repo file — re-paste after editing it here.
#
# Base: trading-strategy environments/setup-universal.sh @ ffdd6f6 (itself
# the fleet canonical fleet-manager environments/templates/setup-universal.sh,
# blob 6b4459b, synced 2026-07-09) + the pinned-research archetype's baseline
# (fleet-manager environments/archetype-pinned-research.sh @ 0eaa668) + the
# fleet capability-probe block (websites docs/project/setup-script.sh
# pattern). Python deps come from the repo's OWN manifest: requirements.txt
# @ ffdd6f6 pins pandas==3.0.3 numpy==2.4.6 yfinance==1.5.1 requests==2.33.1
# pytest==9.1.1 (Python 3.11) — installed via the manifest, never inlined.
#
# CONTRACT (fleet playbook R15 — paid for in blood: this lane lost THREE
# gen-1 sessions at provision): this script NEVER fails the session.
#   1. NEVER exit nonzero — `set +e` + explicit `exit 0`; every step
#      degrades to a log line. A failing setup script = dead session, no
#      signal ("Setup script failed with exit code 1", NEXT-BOOT wall #1).
#   2. NEVER assume cwd is the repo — env setup runs at cwd=/home/user with
#      repos as SUBDIRECTORIES (two-source workspace: trading-strategy +
#      substrate-kit). The .git-based detection below is the fix.
#   3. NEVER bare `pip install -r` — guard on file existence.
#   4. Probe the walls at provision time so no session guesses (the
#      CAPABILITIES discovery rule).
set +e   # a non-zero step must not abort the script (no set -u, no pipefail)
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:trading-strategy] $*"; }

# ── 1. Boot triage ──────────────────────────────────────────────────────────
log "cwd: $(pwd)"
log "python: $(python3 --version 2>&1 || echo 'python3 MISSING')"  # lane pins for 3.11

# ── 2. Baseline extras (archetype: pytest is CI's runner, absent from fresh
#      containers — verified 2026-07-09) ─────────────────────────────────────
python3 -m pip install --quiet pytest \
  || log "baseline pytest install failed (non-fatal; requirements.txt also pins it)"

# ── 3. Per-repo setup (detection order, most-specific first; every branch
#      guarded — one broken repo must never block the others) ────────────────
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  # Git-state triage (non-fatal): detached HEAD is normal on fresh clones;
  # a dirty tree = persistent-workspace residue (git checkout main && git pull --ff-only).
  if command -v git >/dev/null 2>&1 && [ -d "$repo_dir/.git" ]; then
    br="$(git -C "$repo_dir" symbolic-ref --short -q HEAD 2>/dev/null || echo 'DETACHED HEAD — branch before committing')"
    dirty=""
    [ -n "$(git -C "$repo_dir" status --porcelain 2>/dev/null | head -1)" ] \
      && dirty=" · DIRTY TREE (residue? git checkout main && git pull --ff-only)"
    log "$name: git: ${br}${dirty}"
  fi
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/requirements.txt" ]; then
    log "$name: python3 -m pip install -r requirements.txt"
    ( cd "$repo_dir" && python3 -m pip install --quiet -r requirements.txt ) \
      || log "$name: pip install failed (non-fatal, continuing)"
  else
    log "$name: no scripts/env-setup.sh or requirements.txt — skipping"
  fi
}

# Multi-repo vs single-repo detection: the pinned-research env is a WORKSPACE
# whose child dirs are the clones (trading-strategy/ + substrate-kit/);
# single-repo cwd (has .git) also works.
TRADING_DIR=""
if [ -d .git ]; then
  setup_one "$PWD"
  TRADING_DIR="$PWD"
else
  found=0
  for d in */; do
    [ -d "$d/.git" ] || continue
    found=1
    setup_one "$PWD/${d%/}"
    case "${d%/}" in trading-strategy) TRADING_DIR="$PWD/${d%/}" ;; esac
  done
  [ "$found" -eq 1 ] || setup_one "$PWD"
fi
[ -n "$TRADING_DIR" ] || TRADING_DIR="$PWD"

# ── 4. Env var presence report (NAMES only — never values; this lane needs
#      NO env vars: yfinance is keyless, git auth is platform-provided) ──────
for v in GITHUB_TOKEN GITHUB_PAT; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then
    log "env: $v is set"
  else
    log "env: $v is NOT set (fine — this lane declares no required vars)"
  fi
done

# ── 5. Capability probes — print the walls so no session guesses ────────────
log "── capability probe ──"

# 5a. Commit signing (a required-but-missing SSH signer fails every commit).
if [ "$(git config --get commit.gpgsign)" = "true" ]; then
  SIGNER="$(git config --get gpg.ssh.program)"
  if [ -n "$SIGNER" ] && [ -x "$SIGNER" ]; then log "commit signing: ON, signer present ($SIGNER)"
  else log "WARN commit signing REQUIRED but signer '$SIGNER' missing — commits may fail; record the wall, do NOT silently disable signing"; fi
else
  log "commit signing: off"
fi

# 5b. Git read + PUSH credential (dry-run proves the grant without writing).
if git -C "$TRADING_DIR" ls-remote --heads origin >/dev/null 2>&1; then
  log "git read (ls-remote origin): OK"
  if git -C "$TRADING_DIR" push --dry-run origin HEAD:refs/heads/claude/probe-$$ >/dev/null 2>&1; then
    log "git push credential: OK (dry-run accepted)"
  else
    log "WARN git push credential: ABSENT/blocked — commit locally, record branch+state in the card and control/status.md"
  fi
else
  log "WARN git read: ls-remote origin FAILED — repo may not be granted to this session"
fi

# 5c. GitHub API gate. KNOWN WALL (NEXT-BOOT): raw curl to api.github.com can
# HANG behind the egress proxy (exit 143, no error) — hence --max-time here,
# and sessions must poll PR checks via the GitHub MCP pull_request_read
# (method get_check_runs), never raw curl loops.
API_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://api.github.com/rate_limit 2>/dev/null)"
log "api.github.com probe: HTTP ${API_CODE:-none/timeout} (timeout/403 = proxy wall; use GitHub MCP tools)"

# 5d. Fleet raw-read path (package + doctrine reads from fleet-manager).
RAW_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://raw.githubusercontent.com/menno420/fleet-manager/main/README.md 2>/dev/null)"
log "raw.githubusercontent.com fleet probe: HTTP ${RAW_CODE:-none} (200 = raw-read seam works)"

# 5e. Data-loader sanity note (no network fetch at provision — Yahoo via the
# default transport is a documented wall; src/trading_lab/data.py is the
# ONLY sanctioned path and the committed cache serves offline work).
[ -d "$TRADING_DIR/data" ] && log "data cache present: $(ls "$TRADING_DIR/data" 2>/dev/null | head -3 | tr '\n' ' ')…" \
  || log "data cache not found at data/ (loader will fetch through the proxy workaround)"

# ── 6. Unconditional success — the single most important line (R15). ────────
log "setup complete (defensive shim: always exit 0)"
exit 0
