#!/bin/bash
# pokemon-mod-lab — Claude Project ENVIRONMENT setup script (Track A / Emerald).
# Part 3 of the pokemon-mod-lab Project package. Paste into: claude.ai console →
# pokemon-mod-lab Project → environment settings → "Setup script" field.
# Source of truth is this repo file — re-paste after editing it here.
#
# Base: fleet-manager environments/archetype-gba-lab.sh (@ 0eaa668) — the
# archetype mapped to this repo in environments/archetypes.md — REDUCED to the
# Track A subset this repo actually uses (verified against the repo's own
# .github/workflows/rom-builds.yml + docs/capabilities.md @ a76ada7: apt
# binutils-arm-none-eabi + libpng-dev, vendored agbcc/ built + installed into
# the vendored pokeemerald/, headless mGBA loop). The devkitARM/Butano mirror
# blocks are Track B (gba-homebrew) — deliberately NOT included here.
# Capability-probe block from the fleet package pattern (websites
# docs/project/setup-script.sh lineage).
#
# Contract (fleet R15 — every rule paid for by an incident):
#   1. NEVER exit nonzero — a failing setup script kills the session at
#      provisioning. set +e + explicit exit 0; every step degrades to a WARN.
#   2. NEVER assume cwd is the repo clone — detect and cd, guarded.
#   3. Pins: pip mgba==0.10.2 MUST match system libmgba 0.10.x (mgba-sdl) —
#      drifting either side breaks the ABI (toolchain scout 2026-07-09).
#   4. PRIVATE-REPO NOTE: no ROM ever leaves this environment; this script
#      builds and hashes locally only. R22 visibility verification is a
#      SESSION duty via an authenticated get-repo call (GitHub MCP) — the
#      probe below is advisory-only and cannot replace it.
set +e  # never fail the provision

warn() { echo "[setup:WARN] $*"; }
note() { echo "[setup] $*"; }
export PIP_ROOT_USER_ACTION=ignore
export DEBIAN_FRONTEND=noninteractive
note "Working directory: $(pwd)"

# ── 1. Locate the repo clone (never assume cwd) ─────────────────────────────
REPO_DIR=""
for d in /home/user/pokemon-mod-lab /workspace/pokemon-mod-lab; do
  [ -e "$d/.git" ] && REPO_DIR="$d" && break
done
if [ -z "$REPO_DIR" ]; then
  for d in /home/user/*/ /workspace/*/; do
    [ -e "${d}.git" ] && [ -d "${d}pokeemerald" ] && REPO_DIR="${d%/}" && break
  done
fi
if [ -n "$REPO_DIR" ] && cd "$REPO_DIR"; then
  note "Repo clone: $REPO_DIR"
else
  REPO_DIR="$(pwd)"
  warn "pokemon-mod-lab clone not found under /home/user or /workspace; continuing in $REPO_DIR"
fi

# ── 2. Toolchain deps (Track A; mirrors rom-builds.yml + adds headless loop) ─
note "apt: binutils-arm-none-eabi libpng-dev mgba-sdl"
(apt-get update -qq && apt-get install -y -qq binutils-arm-none-eabi libpng-dev mgba-sdl) \
  || (sudo apt-get update -qq && sudo apt-get install -y -qq binutils-arm-none-eabi libpng-dev mgba-sdl) \
  || warn "apt install failed (continuing — ROM build/headless loop degraded)"

# pip: headless-verify loop + kit/dev tools. PIN mgba==0.10.2 (ABI ↔ libmgba 0.10.x).
note "pip: mgba==0.10.2 Pillow pytest ruff"
python3 -m pip install --quiet "mgba==0.10.2" Pillow pytest ruff \
  || warn "pip install failed (continuing)"

# ── 3. agbcc: build + install the vendored compiler into pokeemerald ────────
if [ -x "$REPO_DIR/pokeemerald/tools/agbcc/bin/agbcc" ]; then
  note "agbcc already installed in pokeemerald/tools/agbcc — skipping"
elif [ -d "$REPO_DIR/agbcc" ] && [ -d "$REPO_DIR/pokeemerald" ]; then
  note "building agbcc (vendored; ~fast) + installing into pokeemerald/"
  (cd "$REPO_DIR/agbcc" && ./build.sh >/dev/null 2>&1 && ./install.sh ../pokeemerald >/dev/null 2>&1) \
    && note "agbcc installed" \
    || warn "agbcc build/install failed — sessions must run it before ROM work (docs/capabilities.md recipe)"
else
  warn "vendored agbcc/ or pokeemerald/ missing — not the expected tree at a76ada7-era HEAD"
fi

# ── 4. Optional ROM warm build (full ~1m20s, scout-verified; skippable) ─────
if [ "${SKIP_ROM_WARM_BUILD:-0}" != "1" ] && [ -x "$REPO_DIR/pokeemerald/tools/agbcc/bin/agbcc" ]; then
  note "warm ROM build (make -j; first full build ~1m20s, later incrementals ~2s)"
  if (cd "$REPO_DIR/pokeemerald" && make -j"$(nproc)" >/dev/null 2>&1) && [ -f "$REPO_DIR/pokeemerald/pokeemerald.gba" ]; then
    note "ROM built: sha1 $(sha1sum "$REPO_DIR/pokeemerald/pokeemerald.gba" | cut -c1-12)… (NEVER uploaded — private hard rail)"
  else
    warn "warm ROM build failed — sessions build on demand"
  fi
else
  note "warm ROM build skipped"
fi

# ── 5. Git identity + safety ────────────────────────────────────────────────
git config --global --get user.name  >/dev/null || git config --global user.name  "Claude"
git config --global --get user.email >/dev/null || git config --global user.email "noreply@anthropic.com"
git config --global --add safe.directory "$REPO_DIR" 2>/dev/null || warn "could not set safe.directory"

# ── 6. Capability probes — print the walls so no session guesses ────────────
note "── capability probe ──"
if git -C "$REPO_DIR" ls-remote --heads origin >/dev/null 2>&1; then
  note "git read (ls-remote origin): OK"
  if git -C "$REPO_DIR" push --dry-run origin HEAD:refs/heads/claude/probe-$$ >/dev/null 2>&1; then
    note "git push credential: OK (dry-run accepted; direct push to main stays ruleset-blocked — PR path only)"
  else
    warn "git push credential: ABSENT/blocked — private repo needs the session/env repo grant; hand landing to a tooled session"
  fi
else
  warn "git read FAILED — PRIVATE repo not granted to this session (raw-read does NOT work on private repos, Q-0260 carve-out)"
fi
API_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://api.github.com/rate_limit 2>/dev/null)"
note "api.github.com probe: HTTP ${API_CODE:-none} (403 = proxy repo-grant gate; use GitHub MCP tools)"
# R22 reminder — the probe above is NOT the visibility check. Every session:
# one authenticated get-repo call, read .private/.visibility, record
# 'visibility: private — verified <ISO8601> via <surface>' in control/status.md.
note "R22 (ORDER 003): session MUST verify visibility==private via API and record it in status — every session, no exceptions"
if [ -x "$REPO_DIR/pokeemerald/tools/agbcc/bin/agbcc" ]; then note "toolchain: agbcc READY"; else warn "toolchain: agbcc NOT ready"; fi
python3 -c "import mgba" 2>/dev/null && note "headless loop: pip mgba importable" || warn "headless loop: pip mgba NOT importable"

note "── setup done (fail-soft: warnings above are walls, not failures) ──"
exit 0
