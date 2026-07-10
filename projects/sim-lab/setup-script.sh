#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# setup-script.sh — sim-lab environment setup (launch package part 3)
#
# PROVENANCE: derived from fleet-manager environments/archetype-python-lab.sh
# @ origin/main 0eaa668 (the founding package §3 assigns that archetype to
# sim-lab verbatim; superbot round3-founding-package-simulator-2026-07-10.md
# @ dc19b1e), specialized to sim-lab's actual manifests at HEAD 8b8075d:
# the repo is STDLIB-FIRST — no requirements.txt, no pyproject.toml;
# bootstrap.py (kit v1.7.0) and both sims/REFERENCE.md precedents
# (claim_layout_sim, gen3_deployment_sim: `import random`, `import
# statistics`) need only the standard library. A sim that needs a dependency
# pins it inside its own sims/<slug>/ subtree, never repo-globally.
#
# CONTRACT (playbook R15, setup-universal.sh): NEVER fails the session —
# every step is non-fatal and the script ALWAYS exits 0. Never assumes cwd
# is a git repo. Fail-soft + CAPABILITY PROBE (websites pattern): the probe
# is extra important on this seat — tool availability is seat-dependent and
# this seat has already hit real walls (no send_later/create_trigger on the
# coordinator toolset; REST branch-protection reads 403; no gh CLI in the
# builder's own container) — so the probe RECORDS what this container can do
# instead of letting the session rediscover it.
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture ---------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore

log() { echo "[env-setup:sim-lab] $*"; }

# --- Block 2: baseline dev tools (best-effort, non-fatal) -------------------
# sim-lab is stdlib-only, but fresh containers lack pytest/ruff (verified
# fleet-wide) and future harness/ slices may grow tests.
log "baseline dev tools: pytest ruff"
python3 -m pip install --quiet pytest ruff \
  || log "dev-tools install failed (non-fatal, continuing)"

# --- Block 3: per-repo setup (archetype detection order, guarded) -----------
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/requirements.txt" ]; then
    log "$name: python3 -m pip install -r requirements.txt"
    ( cd "$repo_dir" && python3 -m pip install --quiet -r requirements.txt ) \
      || log "$name: pip install failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/pyproject.toml" ]; then
    log "$name: editable install from pyproject.toml"
    ( cd "$repo_dir" && python3 -m pip install --quiet -e '.[dev]' ) \
      || ( cd "$repo_dir" && python3 -m pip install --quiet -e . ) \
      || log "$name: editable install failed (non-fatal, continuing)"
  else
    log "$name: no manifest — stdlib-only lane (EXPECTED for sim-lab at 8b8075d)"
  fi
}

# --- Block 4: multi-repo vs single-repo detection ---------------------------
if [ -d .git ]; then
  REPO_ROOT="$PWD"
  setup_one "$PWD"
else
  REPO_ROOT=""
  found=0
  for d in */; do
    [ -d "$d/.git" ] || continue
    found=1
    setup_one "$PWD/${d%/}"
    case "${d%/}" in sim-lab) REPO_ROOT="$PWD/${d%/}" ;; esac
  done
  [ "$found" -eq 1 ] || setup_one "$PWD"
  [ -n "$REPO_ROOT" ] || REPO_ROOT="$PWD"
fi

# --- Block 5: CAPABILITY PROBE (record, never fail) -------------------------
# Every probe prints a CAPABILITY: or WALL: line the session can grep. The
# discovery rule (docs/CAPABILITIES.md): a guessed wall and a verified wall
# are different facts — this block does the "attempt once, capture the exact
# error" step for the container-level facts at setup time.
log "--- capability probe ---"

# 5a. interpreter + stdlib the sims need
if python3 -c 'import random, statistics, json, sys; print(sys.version.split()[0])' >/tmp/simlab_py 2>&1; then
  log "CAPABILITY: python3 $(cat /tmp/simlab_py) with sim stdlib (random/statistics/json)"
else
  log "WALL: python3 stdlib probe failed: $(cat /tmp/simlab_py 2>/dev/null)"
fi

# 5b. kit gate runnable (stdlib-only; may legitimately RED on an in-progress
# born-red card via the mtime fallback — record verdict, never gate setup)
if [ -f "$REPO_ROOT/bootstrap.py" ]; then
  ( cd "$REPO_ROOT" && python3 bootstrap.py check --strict >/tmp/simlab_check 2>&1 )
  rc=$?
  log "CAPABILITY: bootstrap.py check --strict runs (exit $rc; nonzero can be the documented born-red-card mtime artifact — see control/status.md ORDER 000 note)"
else
  log "WALL: bootstrap.py not found under $REPO_ROOT — wrong checkout shape?"
fi

# 5c. git identity + forward-only push preconditions
git -C "$REPO_ROOT" rev-parse --short HEAD >/tmp/simlab_head 2>&1 \
  && log "CAPABILITY: git repo at $REPO_ROOT HEAD $(cat /tmp/simlab_head)" \
  || log "WALL: git probe failed: $(cat /tmp/simlab_head 2>/dev/null)"

# 5d. cross-repo READ path (the standing intake feed — Q-0264.6 direct pull).
# Read-only, public raw; sim-lab's ONLY sanctioned cross-repo channel.
if command -v curl >/dev/null 2>&1; then
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 20 \
    "https://raw.githubusercontent.com/menno420/idea-engine/main/control/outbox.md" 2>/dev/null)
  if [ "$code" = "200" ]; then
    log "CAPABILITY: idea-engine outbox reachable via public raw (HTTP 200) — intake feed OK"
  else
    log "WALL: idea-engine outbox raw fetch returned HTTP ${code:-<none>} — record in CAPABILITIES.md and retry in-session before declaring the feed down"
  fi
else
  log "WALL: curl not present — probe the intake feed in-session"
fi

# 5e. gh CLI (absent in at least one verified container — the landing lane
# then uses the GitHub MCP / REST instead; CONVENTIONS.md: REST
# merge-on-green is PRIMARY on born-red PRs)
command -v gh >/dev/null 2>&1 \
  && log "CAPABILITY: gh CLI present ($(gh --version 2>/dev/null | head -1))" \
  || log "WALL: gh CLI absent (verified 2026-07-10 in the package-builder container) — use the GitHub MCP tools / REST for PR ops"

# 5f. scheduler tools — NOT probe-able from a shell script. The
# send_later/create_trigger wall is an AGENT-TOOLSET fact, seat-dependent
# (OA-003 @ 8b8075d: "tool not present in session toolset", verbatim).
log "NOTE: send_later/create_trigger availability CANNOT be probed here — the coordinator must re-probe its own toolset each session and record the verbatim result in control/status.md (OA-003)"

# --- Block 6: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
