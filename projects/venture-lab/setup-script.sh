#!/bin/bash
# venture-lab — Claude Project ENVIRONMENT setup script.
# Part 3 of the venture-lab Project package. Paste into: claude.ai console →
# venture-lab Project → environment settings → "Setup script" field.
# Source of truth is this repo file — re-paste after editing it here.
#
# Base: fleet-manager environments/archetype-python-lab.sh contract (the
# archetype the fleet ledger assigns venture-lab; setup-universal.sh shim
# rules, playbook R15) + the capability-probe block from the websites/kit
# package scripts. Contract (every rule paid for by an incident):
#   1. NEVER exit nonzero — a failing setup script KILLS the session at
#      provisioning. `set +e` + explicit `exit 0`; every step degrades to a
#      [setup:WARN] line.
#   2. NEVER assume cwd is the repo clone. Detect and cd, guarded.
#   3. NEVER bare `pip install -r` — guard on file existence (this repo is
#      stdlib-only at the top level; candidate servers have optional deps).
#   4. Probe the walls at provision time so no session guesses (CAPABILITIES
#      discovery rule).
#   5. STRIPE / SECRETS RULE: NEVER hardcode, echo, or log a key VALUE.
#      Probe only for the PRESENCE of expected env var NAMES ([set]/[unset]).
#      Names from candidates/membership-kit/server/.env.example + the fleet
#      env-vars schema (fleet-manager environments/templates/env-vars.md —
#      names only, never values). archetypes.md: venture-lab carries NO env
#      vars at launch — [unset] is the EXPECTED healthy answer; values, when
#      they ever exist, live only in the claude.ai panel or the owner's
#      local server/.env (never the repo).
set +e  # never fail the provision

warn() { echo "[setup:WARN] $*"; }
note() { echo "[setup] $*"; }
note "Working directory: $(pwd)"

# ── 1. Locate the repo clone (never assume cwd) ─────────────────────────────
REPO_DIR=""
if [ -e /home/user/venture-lab/.git ]; then
  REPO_DIR=/home/user/venture-lab
elif [ -e /workspace/venture-lab/.git ]; then
  REPO_DIR=/workspace/venture-lab
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

# ── 2. Python dependencies (all guarded; stdlib-first repo) ─────────────────
if [ -f requirements.txt ]; then
  python3 -m pip install -q -r requirements.txt || warn "pip install -r requirements.txt failed (continuing)"
else
  note "no top-level requirements.txt — stdlib-only repo; skipping"
fi
# Candidate #1's server has its own optional manifest — install if present,
# never assume (mock mode is stdlib-only by design).
if [ -f candidates/membership-kit/server/requirements.txt ]; then
  python3 -m pip install -q -r candidates/membership-kit/server/requirements.txt || warn "membership-kit server deps failed (continuing; mock mode is stdlib-only)"
fi
if command -v pip >/dev/null 2>&1 || python3 -m pip --version >/dev/null 2>&1; then
  python3 -m pip install -q pytest ruff || warn "pip install pytest ruff failed (continuing)"
  note "dev tools: $(python3 -m pytest --version 2>/dev/null || echo 'pytest UNAVAILABLE') · $(python3 -m ruff --version 2>/dev/null || echo 'ruff UNAVAILABLE')"
else
  warn "pip not found; skipping dev tools"
fi
# Kit gate sanity (the repo's quality floor; advisory here, binding pre-push).
if [ -f bootstrap.py ]; then
  python3 bootstrap.py check --strict >/dev/null 2>&1 && note "bootstrap check --strict: exit 0" || warn "bootstrap check --strict nonzero at provision (sessions must fix before pushing)"
fi

# ── 3. Git identity + safety (idempotent; don't fight CCR presets) ──────────
git config --global --get user.name  >/dev/null || git config --global user.name  "Claude"
git config --global --get user.email >/dev/null || git config --global user.email "noreply@anthropic.com"
git config --global --add safe.directory "$REPO_DIR" 2>/dev/null || warn "could not set safe.directory"

# ── 4. Capability probes — print the walls so no session guesses ────────────
note "── capability probe ──"

# 4a. Commit signing (a required-but-missing SSH signer fails every commit).
if [ "$(git config --get commit.gpgsign)" = "true" ]; then
  SIGNER="$(git config --get gpg.ssh.program)"
  if [ -n "$SIGNER" ] && [ -x "$SIGNER" ]; then note "commit signing: ON, signer present ($SIGNER)"
  else warn "commit signing REQUIRED but signer '$SIGNER' missing/not executable — commits may fail; record the wall, do NOT silently disable signing"; fi
else
  note "commit signing: off"
fi

# 4b. Git read + PUSH credential (dry-run proves the grant without writing).
if git -C "$REPO_DIR" ls-remote --heads origin >/dev/null 2>&1; then
  note "git read (ls-remote origin): OK"
  if git -C "$REPO_DIR" push --dry-run origin HEAD:refs/heads/claude/probe-$$ >/dev/null 2>&1; then
    note "git push credential: OK (dry-run accepted)"
  else
    warn "git push credential: ABSENT/blocked — commit locally, record branch+state in the session card and control/status.md"
  fi
else
  warn "git read: ls-remote origin FAILED — repo may not be granted to this session"
fi

# 4c. GitHub API gate (CCR proxy): 403 = per-session grant wall → use MCP.
API_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://api.github.com/rate_limit 2>/dev/null)"
note "api.github.com probe: HTTP ${API_CODE:-none} (403 = proxy repo-grant gate; use GitHub MCP tools instead)"

# 4d. Fleet raw-read path (Q-0260: cross-repo reads ride raw, not attachment).
RAW_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://raw.githubusercontent.com/menno420/fleet-manager/main/README.md 2>/dev/null)"
note "raw.githubusercontent.com fleet probe: HTTP ${RAW_CODE:-none} (200 = cross-repo read seam works)"

# 4e. Stripe/venture env var NAME presence — PRESENCE ONLY, NEVER VALUES.
# Expected [unset] at launch (archetypes.md: no env vars); a candidate going
# live test-mode flips these via owner clicks (⚑A). Never echo a value.
for VAR in STRIPE_SECRET_KEY STRIPE_WEBHOOK_SECRET DISCORD_INVITE_URL SUPABASE_URL SUPABASE_KEY STORE_BACKEND MEMBERS_DB_PATH; do
  if [ -n "$(printenv "$VAR")" ]; then note "env $VAR: [set] (value not shown — never echo key values)"
  else note "env $VAR: [unset] (expected at launch; mock mode)"; fi
done

note "── setup done (fail-soft: warnings above are walls, not failures) ──"
exit 0
