#!/usr/bin/env bash
# Product Forge — environment setup script (part 3 of 4)
# Paste into claude.ai/code → Environments → product-forge → setup script.
#
# CONTRACT (fleet R15 / websites pattern): FAIL-SOFT — this script ALWAYS
# exits 0. A red setup kills the session before it can report (the PR #47
# provisioning-death lesson); a missing tool is a capability FINDING for the
# session to record, never a boot failure.
#
# STACK NOTE — DO NOT GUESS DEPS HERE: product subtrees declare their own
# dependencies in their own READMEs (products/README.md: "own pinned deps
# inside the subtree; the repo root stays stdlib-only"). This script installs
# only the basics every session needs. Observed at origin/main 7f05aa8:
# products/games-web/ phase 1 is a static page served by `python3 -m
# http.server` (run.sh) with stdlib-only tests (`jsonschema` optional for
# full-schema validation) — nothing extra required; a future ORDER that
# scopes in node/other stacks amends this script THEN, per its product README.
#
# Provenance: adapted from the fleet defensive shim contract
# (fleet-manager environments/templates/setup-universal.sh, always-exit-0) +
# the websites capability-probe pattern (websites docs/project/setup-script.sh).
# Founding env spec: superbot round3-founding-package-product-forge §3 @ dc19b1e
# (archetype-python-lab.sh verbatim; repo menno420/product-forge only, Q-0260;
# variables: none).

set +e  # fail-soft: no command failure may abort setup
echo "== product-forge setup (fail-soft; every step reports, none aborts) =="

# --- locate the repo (harness clone path varies) -----------------------------
REPO_DIR=""
for d in /workspace/product-forge "$HOME/product-forge" ./product-forge .; do
  if [ -d "$d/.git" ] && [ -f "$d/bootstrap.py" ]; then REPO_DIR="$d"; break; fi
done
if [ -n "$REPO_DIR" ]; then
  echo "[ok] repo at: $REPO_DIR"
else
  echo "[warn] product-forge clone not found at expected paths — session must locate it (finding, not failure)"
fi

# --- basics: python3 + git identity ------------------------------------------
if command -v python3 >/dev/null 2>&1; then
  echo "[ok] python3: $(python3 --version 2>&1)"
else
  echo "[warn] python3 missing — attempting install"
  (sudo apt-get update -y && sudo apt-get install -y python3) >/dev/null 2>&1 \
    && echo "[ok] python3 installed" || echo "[warn] python3 install failed — record verbatim in PLATFORM-LIMITS.md"
fi
git config --global user.name  >/dev/null 2>&1 || git config --global user.name  "Claude (product-forge)"
git config --global user.email >/dev/null 2>&1 || git config --global user.email "noreply@anthropic.com"
echo "[ok] git identity: $(git config --global user.name) <$(git config --global user.email)>"

# --- kit gate sanity (the repo's own verify command) --------------------------
if [ -n "$REPO_DIR" ]; then
  (cd "$REPO_DIR" && timeout 120 python3 bootstrap.py check --strict) \
    && echo "[ok] bootstrap check --strict: green" \
    || echo "[warn] bootstrap check --strict non-zero — diagnose locally (PLATFORM-LIMITS: red check_run output can be empty over the API)"
fi

# --- capability probe (websites pattern: probe once, record, never assume) ----
echo "== capability probe =="
if [ -n "$REPO_DIR" ]; then
  (cd "$REPO_DIR" && timeout 30 git ls-remote origin >/dev/null 2>&1) \
    && echo "[ok] probe: git ls-remote origin reachable" \
    || echo "[warn] probe: git ls-remote failed — capture exact error in-session before declaring a wall"
  (cd "$REPO_DIR" && timeout 30 git push --dry-run origin HEAD >/dev/null 2>&1) \
    && echo "[ok] probe: dry-run push accepted (note: main is ruleset-protected — real pushes go via branch+PR)" \
    || echo "[info] probe: dry-run push refused (expected on protected main; PRs are the landing path)"
fi
command -v gh >/dev/null 2>&1 && echo "[ok] probe: gh CLI present" || echo "[info] probe: no gh CLI — GitHub MCP tools are the API path"
python3 -c "import jsonschema" >/dev/null 2>&1 \
  && echo "[ok] probe: jsonschema importable (games-web full-schema tests)" \
  || echo "[info] probe: jsonschema absent — games-web tests fall back to dependency-free structural checks (by design)"

echo "== setup done =="
echo "NOTE: product subtrees declare their own deps in products/<slug>/README.md —"
echo "install per-product deps in-session per that README, not here."
exit 0
