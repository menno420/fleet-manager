#!/bin/bash
# gba-homebrew — Claude Project ENVIRONMENT setup script.
# Part 3 of the gba-homebrew Project package. Paste into: claude.ai console →
# gba-homebrew Project → environment settings → "Setup script" field.
# Source of truth is this repo file — re-paste after editing it here.
#
# Base: fleet-manager environments/archetype-gba-lab.sh (the gba-lab
# archetype — ⚠ UNTESTED AS-A-WHOLE until the lane's first boot, per
# fleet-manager environments/README.md) wrapped in the fleet defensive
# contract (templates/setup-universal.sh, playbook R15) + the
# capability-probe block from the websites/substrate-kit packages.
# The HEAVY toolchain work is delegated to the repo's own PINNED installer,
# tools/setup-toolchain.sh — this wrapper NEVER duplicates its pins.
# Contract (every rule paid for by an incident):
#   1. NEVER exit nonzero — a failing setup script KILLS the session at
#      provisioning. `set +e` + explicit `exit 0`; every step degrades to a
#      [setup:WARN] line.
#   2. NEVER assume cwd is the repo clone — detect and cd, guarded.
#   3. The toolchain installer is `set -euo pipefail` and FAILS HARD on a
#      SHA-256 pin mismatch BY DESIGN (unsigned mirror, trust-on-first-use).
#      This wrapper fail-softs the CALL (a dead mirror must not kill the
#      session) but never bypasses a pin — a WARN here means the session
#      must investigate before building, not re-pin.
#   4. Probe the walls at provision time so no session guesses.
set +e  # never fail the provision
export DEBIAN_FRONTEND=noninteractive
export PIP_ROOT_USER_ACTION=ignore

warn() { echo "[setup:WARN] $*"; }
note() { echo "[setup] $*"; }
note "Working directory: $(pwd)"

# ── 1. Locate the repo clone (never assume cwd) ─────────────────────────────
REPO_DIR=""
if [ -e /home/user/gba-homebrew/.git ]; then
  REPO_DIR=/home/user/gba-homebrew
elif [ -e /workspace/gba-homebrew/.git ]; then
  REPO_DIR=/workspace/gba-homebrew
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

# ── 2. apt baseline (guarded; scout-verified list, archetype-gba-lab) ───────
# binutils-arm-none-eabi: Track-A-shape assembler (harmless here, tiny);
# mgba-sdl: system libmgba 0.10.x the pip binding pins against;
# zstd: unpacks the devkitARM .pkg.tar.zst packages.
note "apt baseline: binutils-arm-none-eabi mgba-sdl zstd"
(apt-get update -qq && apt-get install -y -qq binutils-arm-none-eabi mgba-sdl zstd) \
  || (sudo apt-get update -qq && sudo apt-get install -y -qq binutils-arm-none-eabi mgba-sdl zstd) \
  || warn "apt install failed (continuing — toolchain script installs zstd itself)"

# ── 3. Python basics (guarded) ──────────────────────────────────────────────
# mgba==0.10.2: MUST stay pinned to the system libmgba 0.10.x (scout-proven
# headless loop; PyPI wheels stop at cp311 — see repo review row #17).
python3 -m pip install -q --upgrade pip 2>/dev/null || warn "pip upgrade failed (continuing)"
python3 -m pip install -q "mgba==0.10.2" Pillow || warn "pip mgba==0.10.2/Pillow failed — headless emulator loop unavailable this session (record it, don't re-derive)"
if [ -f requirements.txt ]; then
  python3 -m pip install -q -r requirements.txt || warn "pip install -r requirements.txt failed (continuing)"
else
  note "no requirements.txt — Python tooling is stdlib + mgba/Pillow; skipping"
fi
note "python: $(python3 --version 2>&1) · mgba binding: $(python3 -c 'import mgba; print(mgba.__version__)' 2>/dev/null || echo 'UNAVAILABLE')"

# ── 4. GBA toolchain — delegate to the repo's PINNED installer (fail-soft) ──
# tools/setup-toolchain.sh: devkitARM r68 (leseratte10 mirror, SHA-256 pins),
# devkitarm-crtls v1.2.7 from source, Butano 21.7.1 pinned. Idempotent
# (stamp file skips warm work). NEVER install any of this ad hoc.
if [ -x "$REPO_DIR/tools/setup-toolchain.sh" ] || [ -f "$REPO_DIR/tools/setup-toolchain.sh" ]; then
  note "running tools/setup-toolchain.sh (pinned; idempotent)"
  if bash "$REPO_DIR/tools/setup-toolchain.sh"; then
    note "toolchain OK"
  else
    warn "tools/setup-toolchain.sh FAILED — do NOT install ad hoc and do NOT bypass a pin; read its FATAL line (SHA mismatch = investigate the mirror; network = retry in-session) and record the exact error"
  fi
else
  warn "tools/setup-toolchain.sh not found at $REPO_DIR/tools — wrong clone?"
fi
export DEVKITPRO="${DEVKITPRO:-/opt/devkitpro}"
export DEVKITARM="$DEVKITPRO/devkitARM"
export PATH="$DEVKITARM/bin:$DEVKITPRO/tools/bin:$PATH"
note "toolchain probe: $(command -v arm-none-eabi-gcc >/dev/null 2>&1 && arm-none-eabi-gcc --version 2>/dev/null | head -1 || echo 'arm-none-eabi-gcc UNAVAILABLE')"
note "butano pin: $(git -C "$REPO_DIR/third_party/butano" rev-parse --short HEAD 2>/dev/null || echo 'not cloned')"

# ── 5. Git identity + safety (idempotent; don't fight CCR presets) ──────────
git config --global --get user.name  >/dev/null || git config --global user.name  "Claude"
git config --global --get user.email >/dev/null || git config --global user.email "noreply@anthropic.com"
git config --global --add safe.directory "$REPO_DIR" 2>/dev/null || warn "could not set safe.directory"

# ── 6. Capability probes — print the walls so no session guesses ────────────
note "── capability probe ──"

# 6a. Commit signing (a required-but-missing SSH signer fails every commit).
if [ "$(git config --get commit.gpgsign)" = "true" ]; then
  SIGNER="$(git config --get gpg.ssh.program)"
  if [ -n "$SIGNER" ] && [ -x "$SIGNER" ]; then note "commit signing: ON, signer present ($SIGNER)"
  else warn "commit signing REQUIRED but signer '$SIGNER' missing — commits may fail; record the wall, do NOT silently disable signing"; fi
else
  note "commit signing: off"
fi

# 6b. Git read + PUSH credential (dry-run proves the grant without writing).
if git -C "$REPO_DIR" ls-remote --heads origin >/dev/null 2>&1; then
  note "git read (ls-remote origin): OK"
  if git -C "$REPO_DIR" push --dry-run origin HEAD:refs/heads/claude/probe-$$ >/dev/null 2>&1; then
    note "git push credential: OK (dry-run accepted). Reminder: direct push to main is ruleset-blocked (PLATFORM-LIMITS) — land via PR."
  else
    warn "git push credential: ABSENT/blocked — commit locally, record branch+state in the session card and control/status.md"
  fi
else
  warn "git read: ls-remote origin FAILED — repo may not be granted to this session"
fi

# 6c. GitHub API gate (CCR proxy): out-of-session repos 403 — MCP is the path.
API_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://api.github.com/rate_limit 2>/dev/null)"
note "api.github.com probe: HTTP ${API_CODE:-none} (403 = proxy repo-grant gate; use GitHub MCP tools — the documented merge path)"

# 6d. Repo VISIBILITY guard (fleet R22 — the rail depends on it being public
# by design, and Track A's rail depends on it staying OUT of here; sessions
# must re-verify, this probe is the provision-time first read).
VIS="$(curl -s --max-time 10 https://api.github.com/repos/menno420/gba-homebrew 2>/dev/null | python3 -c 'import sys,json; d=json.load(sys.stdin); print(d.get("visibility","unknown"))' 2>/dev/null)"
note "repo visibility probe: ${VIS:-unknown} (expected: public — this repo is publish-safe by construction; re-verify per session, fleet R22)"

# 6e. Fleet raw-read path (cross-repo reads are raw-only per Q-0260).
RAW_CODE="$(curl -s -o /dev/null -w '%{http_code}' --max-time 10 https://raw.githubusercontent.com/menno420/fleet-manager/main/README.md 2>/dev/null)"
note "raw.githubusercontent.com fleet probe: HTTP ${RAW_CODE:-none} (200 = cross-repo raw reads work)"

note "── setup done (fail-soft: warnings above are walls, not failures) ──"
exit 0
