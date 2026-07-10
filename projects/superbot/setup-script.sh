#!/bin/bash
# superbot — Claude Project ENVIRONMENT setup script.
# Part 3 of the superbot package. Paste into: claude.ai console → the Project
# the owner starts superbot sessions from → environment settings → "Setup
# script" field. Source of truth is this repo file — re-paste after editing.
#
# Base: fleet-manager environments/archetype-bot-prod.sh (the archetype that
# serves "superbot (legacy)"; fm origin/main 0eaa668) specialized single-repo,
# + the capability-probe block from the round-3 package lineage.
# The bot-prod archetype is the ONLY one allowed production-pointing vars
# (DISCORD_BOT_TOKEN_PRODUCTION, DATABASE_URL, the Railway trio).
#
# Contract (setup-universal.sh R15, every rule paid for by an incident):
#   1. NEVER exit nonzero — a failing setup script kills the session at
#      provisioning. set +e + explicit exit 0; every step degrades to a warn.
#   2. NEVER assume cwd is the repo clone.
#   3. python3.10 ONLY for this repo — CI pins 3.10 (code-quality.yml);
#      bare python3 is 3.11.x in-container and installs into the wrong
#      site-packages (CLAUDE.md CI-parity section; archetypes.md wrinkle #1).
#   4. NEVER checkout/reset — residue is REPORTED, not mutated (a setup
#      script must not destroy in-progress work).
# NOTE: the repo carries its own richer SessionStart hook —
# scripts/claude_session_start.sh (dev env via scripts/setup_dev_env.sh +
# CodeGraph index build, pin @optave/codegraph@3.11.2 in .mcp.json + the hook
# CG_PKG) — which .claude/settings.json fires once the session opens. This
# env script therefore stays MINIMAL: deps + parity + probes; it must not
# duplicate the hook's work.
set +e  # never fail the provision
export PIP_ROOT_USER_ACTION=ignore

warn() { echo "[setup:WARN] $*"; }
note() { echo "[setup] $*"; }
note "Working directory: $(pwd)"

# ── 1. Locate the repo clone (never assume cwd) ─────────────────────────────
REPO_DIR=""
for c in /home/user/superbot /workspace/superbot; do
  [ -e "$c/.git" ] && REPO_DIR="$c" && break
done
if [ -z "$REPO_DIR" ]; then
  for d in /home/user/*/ /workspace/*/; do
    [ -e "${d}.git" ] && [ "$(basename "${d%/}")" = "superbot" ] && REPO_DIR="${d%/}" && break
  done
fi
if [ -n "$REPO_DIR" ] && cd "$REPO_DIR"; then
  note "Repo clone: $REPO_DIR"
else
  REPO_DIR="$(pwd)"
  warn "superbot clone not found under /home/user or /workspace; continuing in $REPO_DIR"
fi

# ── 2. Workspace-residue advisory (report only — NEVER mutate) ──────────────
BRANCH="$(git -C "$REPO_DIR" rev-parse --abbrev-ref HEAD 2>/dev/null)"
if [ -n "$BRANCH" ] && [ "$BRANCH" != "main" ]; then
  note "NOTE — on branch '$BRANCH' (possible previous-session residue)."
  note "       recovery if stale: git checkout main && git pull --ff-only"
fi
[ -n "$(git -C "$REPO_DIR" status --porcelain 2>/dev/null | head -1)" ] && \
  note "NOTE — working tree is dirty (inherited or in-progress changes)."

# ── 3. Interpreter — python3.10 or loudly degraded (CI parity) ──────────────
if command -v python3.10 >/dev/null 2>&1; then
  PY=python3.10
  note "interpreter: python3.10 ($(python3.10 --version 2>&1))"
else
  PY=python3
  warn "python3.10 NOT FOUND — falling back to python3 ($(python3 --version 2>&1)); CI-PARITY RISK: local checks may silently diverge from code-quality.yml"
fi

# ── 4. Dependencies (guarded; repo knows best) ──────────────────────────────
if [ -f "$REPO_DIR/scripts/setup_dev_env.sh" ]; then
  note "running scripts/setup_dev_env.sh (the repo's own dev-env recipe — also run by the SessionStart hook; idempotent)"
  ( cd "$REPO_DIR" && bash scripts/setup_dev_env.sh ) || warn "setup_dev_env.sh failed (non-fatal; the SessionStart hook retries)"
elif [ -f "$REPO_DIR/requirements.txt" ]; then
  note "$PY -m pip install -r requirements.txt"
  ( cd "$REPO_DIR" && "$PY" -m pip install --quiet -r requirements.txt ) || warn "runtime deps install failed (continuing)"
  [ -f "$REPO_DIR/requirements-dev.txt" ] && { ( cd "$REPO_DIR" && "$PY" -m pip install --quiet -r requirements-dev.txt ) || warn "dev deps install failed (continuing)"; }
else
  warn "no scripts/setup_dev_env.sh and no requirements.txt — skipping deps"
fi

# ── 5. Git identity + safety (idempotent) ───────────────────────────────────
git config --global --get user.name  >/dev/null || git config --global user.name  "Claude"
git config --global --get user.email >/dev/null || git config --global user.email "noreply@anthropic.com"
git config --global --add safe.directory "$REPO_DIR" 2>/dev/null || warn "could not set safe.directory"

# ── 6. Env var presence report (NAMES only — never values) ──────────────────
# The observed live set for legacy superbot (fm environments/archetypes.md):
for v in DATABASE_URL DISCORD_BOT_TOKEN_PRODUCTION OPENAI_API_KEY GITHUB_PAT \
         RAILWAY_API_KEY RAILWAY_PROJECT_ID RAILWAY_SERVICE_ID RAILWAY_ENVIRONMENT_ID; do
  if [ -n "$(eval "printf '%s' \"\${$v:-}\"")" ]; then note "env: $v is set"
  else note "env: $v is NOT set (agent sessions usually fine; live-verify/ops paths degrade)"; fi
done
if [ -n "${YOUTUBE_API_KEY:-}" ]; then note "env: YOUTUBE_API_KEY is set"
else note "env: YOUTUBE_API_KEY is NOT set (deploy-required; YouTube features degrade with a warning)"; fi

# ── 7. Capability probes — print the walls so no session guesses ────────────
note "── capability probe ──"
if git -C "$REPO_DIR" ls-remote --heads origin >/dev/null 2>&1; then
  note "git read (ls-remote origin): OK"
  if git -C "$REPO_DIR" push --dry-run origin HEAD:refs/heads/claude/probe-$$ >/dev/null 2>&1; then
    note "git push credential: OK (dry-run accepted)"
  else
    warn "git push credential: ABSENT/blocked — commit locally, record branch+state in the session card, hand landing to a tooled session"
  fi
else
  warn "git read: ls-remote origin FAILED — repo may not be granted to this session"
fi
API_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://api.github.com/rate_limit 2>/dev/null)"
note "api.github.com probe: HTTP ${API_CODE:-none} (403 = proxy repo-grant gate; use GitHub MCP tools — and remember Q-0127: MCP-created PRs need enable_pr_auto_merge)"

# ── 8. Unconditional success (R15 — do not 'improve' this) ──────────────────
note "setup complete (defensive shim: always exit 0)"
exit 0
