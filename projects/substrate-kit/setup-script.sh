#!/bin/bash
# substrate-kit — Claude Project ENVIRONMENT setup script.
# Part 3 of the substrate-kit Project package. Paste into: claude.ai console →
# substrate-kit Project → environment settings → "Setup script" field.
# Source of truth is this repo file — re-paste after editing it here.
#
# Base: substrate-kit docs/gen2/setup.sh (the OA8 paste candidate) + the
# capability-probe block from websites docs/project/setup-script.sh.
# Contract (every rule paid for by an incident):
#   1. NEVER exit nonzero — a failing setup script KILLS the session at
#      provisioning (substrate-kit PR #47 death: "Setup script failed with
#      exit code 1"). `set +e` + explicit `exit 0`; every step degrades to a
#      [setup:WARN] line.
#   2. NEVER assume cwd is the repo clone — the PR #47 casualty ran from
#      /home/user, not the clone. Detect and cd, guarded.
#   3. NEVER bare `pip install -r` — guard on file existence (this repo is
#      stdlib-only at runtime; packaging lives in pyproject.toml).
#   4. Probe the walls at provision time so no session guesses (CAPABILITIES
#      discovery rule; the recorded-push-that-never-landed lesson).
set +e  # never fail the provision

warn() { echo "[setup:WARN] $*"; }
note() { echo "[setup] $*"; }
note "Working directory: $(pwd)"

# ── 1. Locate the repo clone (never assume cwd) ─────────────────────────────
REPO_DIR=""
if [ -e /home/user/substrate-kit/.git ]; then
  REPO_DIR=/home/user/substrate-kit
elif [ -e /workspace/substrate-kit/.git ]; then
  REPO_DIR=/workspace/substrate-kit
else
  for d in /home/user/*/ /workspace/*/; do
    if [ -e "${d}.git" ]; then REPO_DIR="${d%/}"; break; fi
  done
fi
if [ -n "$REPO_DIR" ] && cd "$REPO_DIR"; then
  note "Repo clone: $REPO_DIR"
else
  REPO_DIR="$(pwd)"
  warn "no git repo found under /home/user or /workspace; continuing in $REPO_DIR"
fi

# ── 2. Python dependencies (all guarded) ────────────────────────────────────
if [ -f requirements.txt ]; then
  python3 -m pip install -q -r requirements.txt || warn "pip install -r requirements.txt failed (continuing)"
else
  note "no requirements.txt — stdlib-only repo; skipping"
fi
# CI's only dev tools are pytest + ruff (mirrors .github/workflows/ci.yml).
# Verified 2026-07-09: a fresh container does NOT have pytest preinstalled.
if command -v pip >/dev/null 2>&1 || python3 -m pip --version >/dev/null 2>&1; then
  python3 -m pip install -q pytest ruff || warn "pip install pytest ruff failed (continuing)"
  note "dev tools: $(python3 -m pytest --version 2>/dev/null || echo 'pytest UNAVAILABLE') · $(python3 -m ruff --version 2>/dev/null || echo 'ruff UNAVAILABLE')"
else
  warn "pip not found; skipping dev tools"
fi

# ── 3. Git identity + safety (idempotent; don't fight CCR presets) ──────────
git config --global --get user.name  >/dev/null || git config --global user.name  "Claude"
git config --global --get user.email >/dev/null || git config --global user.email "noreply@anthropic.com"
git config --global --add safe.directory "$REPO_DIR" 2>/dev/null || warn "could not set safe.directory"

# ── 4. Capability probes — print the walls so no session guesses ────────────
note "── capability probe ──"

# 4a. Commit signing (CCR envs may set commit.gpgsign=true with an SSH signer;
# a missing signer fails commits with "failed to write commit object").
if [ "$(git config --get commit.gpgsign)" = "true" ]; then
  SIGNER="$(git config --get gpg.ssh.program)"
  if [ -n "$SIGNER" ] && [ -x "$SIGNER" ]; then note "commit signing: ON, signer present ($SIGNER)"
  else warn "commit signing REQUIRED but signer '$SIGNER' missing/not executable — commits may fail; record the wall in the session card, do NOT silently disable signing"; fi
else
  note "commit signing: off"
fi

# 4b. Git read + PUSH credential (dry-run proves the grant without writing).
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
# known per-session grant wall — PR-open must then use MCP tools.
API_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://api.github.com/rate_limit 2>/dev/null)"
note "api.github.com probe: HTTP ${API_CODE:-none} (403 = proxy repo-grant gate; use GitHub MCP tools instead)"

# 4d. Fleet raw-read path (distribution seat reads sibling trees read-only).
RAW_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://raw.githubusercontent.com/menno420/fleet-manager/main/README.md 2>/dev/null)"
note "raw.githubusercontent.com fleet probe: HTTP ${RAW_CODE:-none} (200 = bootstrap currency's fetch seam works; anything else, record it)"

note "── setup done (fail-soft: warnings above are walls, not failures) ──"
exit 0
