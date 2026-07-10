#!/usr/bin/env bash
# fleet-manager — Claude Project ENVIRONMENT setup script (single-repo fitted).
# Paste into: claude.ai console → Environments → the env attached to the
# fleet-manager Project → "Setup script" field. Source of truth is THIS file
# in projects/fleet-manager/ — re-paste after editing it here.
#
# NOTE ON THE LIVE ENV (2026-07-10): the manager seat currently runs in the
# `multi-repo` coordinator workspace whose deployed script is
# environments/archetype-coordinator.sh (canonical, tested — cwd is a WORKSPACE
# of N repos, not a repo). THIS file is the repo-fitted probe variant per the
# gen-3 standard, for a fleet-manager-only env or as the repo's committed
# package part; it does not replace the archetype for the multi-repo env.
#
# Contract: non-interactive, idempotent, FAIL-SOFT (playbook R15; the
# substrate-kit PR #47 provisioning-death lesson via websites
# docs/project/setup-script.sh, whose probe block this adapts). Nothing here
# may abort: warn and continue; ALWAYS exit 0.
set +e  # never fail the provision; every probe degrades to a warning
export PIP_ROOT_USER_ACTION=ignore

REPO_DIR="${REPO_DIR:-$(pwd)}"
# Multi-repo workspace tolerance: if cwd isn't the repo, find the child clone.
[ -f "$REPO_DIR/bootstrap.py" ] || { [ -d "$REPO_DIR/fleet-manager" ] && REPO_DIR="$REPO_DIR/fleet-manager"; }
warn() { echo "[setup:WARN] $*"; }
note() { echo "[setup] $*"; }

# ── 1. Python ────────────────────────────────────────────────────────────────
# fleet-manager is a docs/coordination repo: bootstrap.py (substrate-kit) is
# stdlib-only; the gate needs python3 + pytest/ruff at most. Any 3.10+ is fine.
note "python3 = $(python3 -V 2>&1)"

# ── 2. Dependencies (best-effort, non-fatal) ────────────────────────────────
# No requirements.txt in this repo (verified @702ba89). Baseline dev tools
# match environments/archetype-coordinator.sh Block 2.
python3 -m pip install -q pytest ruff || warn "dev-tools install failed (non-fatal)"
# Kit gate smoke: prove the repo's own checker runs (never fail provision on red).
if [ -f "$REPO_DIR/bootstrap.py" ]; then
  ( cd "$REPO_DIR" && python3 bootstrap.py check >/dev/null 2>&1 ) \
    && note "bootstrap.py check: ran OK" \
    || warn "bootstrap.py check failed/red — run it manually in-session before pushing"
else
  warn "bootstrap.py not found at $REPO_DIR (wrong cwd?)"
fi

# ── 3. Git identity + safety ────────────────────────────────────────────────
# Idempotent: only fill identity if unset (CCR usually pre-sets it).
git config --global --get user.name  >/dev/null || git config --global user.name  "Claude"
git config --global --get user.email >/dev/null || git config --global user.email "noreply@anthropic.com"
git config --global --add safe.directory "$REPO_DIR" 2>/dev/null || warn "could not set safe.directory"

# ── 4. Capability probes — print the walls so no session guesses ────────────
# (docs/capabilities.md discovery rule: verified facts, never assumptions —
#  and never re-probe a documented wall mid-session; this block probes ONCE
#  at provision so sessions start with proof.)
note "── capability probe ──"

# 4a. Commit signing: CCR envs default commit.gpgsign=true with an SSH signer.
# A missing signer fails every commit with "failed to write commit object".
if [ "$(git config --get commit.gpgsign)" = "true" ]; then
  SIGNER="$(git config --get gpg.ssh.program)"
  if [ -n "$SIGNER" ] && [ -x "$SIGNER" ]; then note "commit signing: ON, signer present ($SIGNER)"
  else warn "commit signing REQUIRED but signer '$SIGNER' missing/not executable — commits may fail; record this wall on the session card, do not silently disable signing"; fi
else
  note "commit signing: off"
fi

# 4b. Git read + PUSH credential. Dry-run push proves the per-session repo
# grant without writing anything.
if git -C "$REPO_DIR" ls-remote --heads origin >/dev/null 2>&1; then
  note "git read (ls-remote origin): OK"
  if git -C "$REPO_DIR" push --dry-run origin HEAD:refs/heads/claude/probe-$$ >/dev/null 2>&1; then
    note "git push credential: OK (dry-run accepted)"
  else
    warn "git push credential: ABSENT/blocked — commit locally, record branch+state in the session card and control/status.md, hand landing to a tooled session"
  fi
else
  warn "git read: ls-remote origin FAILED — repo may not be granted to this session (the add_repo gate)"
fi

# 4c. GitHub API gate (CCR proxy): 403 'not enabled for this session' is the
# per-session repo-grant wall — PR-open/REST-merge must then go through MCP
# tooling or a later tooled session. (REST merge-on-green is this repo's
# landing path — playbook R21 — so this probe is load-bearing here.)
API_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://api.github.com/rate_limit 2>/dev/null)"
note "api.github.com probe: HTTP ${API_CODE:-none} (403 = proxy repo-grant gate; REST merges/PR-open need MCP tooling or a later tooled session)"

note "── setup done (fail-soft: warnings above are walls, not failures) ──"
exit 0
