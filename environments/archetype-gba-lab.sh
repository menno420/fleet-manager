#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# archetype-gba-lab.sh — setup script for the "gba-lab" archetype
#
# Canonical copy: menno420/fleet-manager · environments/archetype-gba-lab.sh
# Serves: gba-homebrew (public, Butano), pokemon-mod-lab (PRIVATE,
#         pret/pokeemerald mirror) — the game-lab venture, both tracks.
# Shape:  GBA cross-compile toolchains + headless emulator; zero secrets;
#         no services. Its own archetype because the toolchain is far too
#         heavy to fold into python-lab (devkitARM + agbcc + mGBA).
#
# Every route below was PROVEN in-container by the toolchain scout session
# 2026-07-09 (docs/findings/gba-toolchain-proof-2026-07-09.md):
#   Track A: apt binutils-arm-none-eabi (only extra apt dep) + agbcc per
#            pokeemerald INSTALL.md -> byte-identical retail build, 1m20s
#            full / 2.0s incremental.
#   Track B: official devkitPro installers Cloudflare-403 behind the proxy;
#            working route = leseratte10 community mirror (devkitARM r68
#            packages) + make-rules/crt0 built from devkitPro GitHub
#            sources -> Butano sprites example 17.5s.
#            ⚠ mirror is UNSIGNED community infra (supply-chain caveat).
#   Headless loop: apt mgba-sdl + pip mgba==0.10.2 (MUST stay pinned to the
#            system libmgba 0.10.x) -> boot/run/PNG at ~290 fps.
#
# Derived from environments/templates/setup-universal.sh (the fleet canonical
# shim). CONTRACT (playbook R15): NEVER fails the session — every step is
# non-fatal and the script ALWAYS exits 0. Never assumes cwd is a git repo
# (works on a bare multi-source checkout: cwd with repos as subdirectories).
# ---------------------------------------------------------------------------

# --- Block 1: defensive posture --------------------------------------------
set +e          # a non-zero step must not abort the script
# no set -u; no pipefail — tolerated, never fatal.
export PIP_ROOT_USER_ACTION=ignore
export DEBIAN_FRONTEND=noninteractive

log() { echo "[env-setup:gba-lab] $*"; }

# --- Block 2: archetype baseline (best-effort, non-fatal) -------------------
# apt layer: Track A assembler/linker + headless emulator + extraction tools
# + patch-distribution tooling.
# binutils-arm-none-eabi is the ONLY extra apt dep pokeemerald needs on this
# container (scout-verified); mgba-sdl provides the system libmgba 0.10.x the
# pip binding pins against; zstd unpacks the devkitARM .pkg.tar.zst packages;
# xdelta3 emits base->modded ROM patches — the lane's only distributable form
# (the ROM itself is un-distributable; audit R3a, ORDER 018). flips (Floating
# IPS) is NOT in the Ubuntu apt archive — why-not recorded in archetypes.md
# § "R3 disposition".
log "apt baseline: binutils-arm-none-eabi mgba-sdl zstd xdelta3"
(apt-get update -qq && apt-get install -y -qq \
    binutils-arm-none-eabi mgba-sdl zstd xdelta3) \
  || (sudo apt-get update -qq && sudo apt-get install -y -qq \
    binutils-arm-none-eabi mgba-sdl zstd xdelta3) \
  || log "apt install failed (non-fatal, continuing)"

# pip layer: dev tools + the mGBA binding. PIN mgba==0.10.2 — it must match
# the system libmgba 0.10.x from mgba-sdl (drift on either side breaks ABI).
log "pip baseline: pytest ruff Pillow mgba==0.10.2"
python3 -m pip install --quiet pytest ruff Pillow "mgba==0.10.2" \
  || log "pip baseline failed (non-fatal, continuing)"

# --- Block 3: devkitARM r68 via the leseratte10 mirror (Track B) ------------
# Official devkitPro package infra Cloudflare-403s behind the fleet proxy
# (documented wall — do not re-probe it; docs/capabilities.md). The proven
# route: extract the r68 linux_x86_64 packages from the community mirror,
# then build make-rules + crt0 from devkitPro's GitHub sources.
# ⚠ Supply-chain caveat: the mirror is unsigned community infrastructure.
#
# GATED on homebrew detection (audit R3b, ORDER 018): a pokeemerald-only env
# (Track A: agbcc) never uses devkitARM — pulling an unsigned-mirror
# toolchain it never uses is pure supply-chain surface. Pull it only when a
# checked-out repo actually looks Track-B-shaped (Butano/homebrew: any git
# repo that is NOT pokeemerald-shaped by the Block-4 signature
# include/global.h + Makefile), or when NO repos are visible (unknown/bare
# layout — preserve the proven pre-gate behavior), or when forced.
# Override: GBA_TRACK_B=force (always install) / GBA_TRACK_B=skip (never).
needs_track_b() {
  case "${GBA_TRACK_B:-}" in
    force) return 0 ;;
    skip)  log "GBA_TRACK_B=skip — devkitARM Track-B pull disabled"; return 1 ;;
  esac
  _repos=0
  _trackb=0
  if [ -d .git ]; then
    _dirs="$PWD"
  else
    _dirs=""
    for _d in */; do
      [ -d "$_d/.git" ] && _dirs="$_dirs $PWD/${_d%/}"
    done
  fi
  for _r in $_dirs; do
    _repos=$((_repos + 1))
    if [ -f "$_r/include/global.h" ] && [ -f "$_r/Makefile" ]; then
      continue  # pokeemerald-shaped (Track A) — no devkitARM needed
    fi
    _trackb=1
  done
  [ "$_repos" -eq 0 ] && return 0  # unknown layout: keep the proven default
  [ "$_trackb" -eq 1 ]
}
DKP="${DEVKITPRO:-/opt/devkitpro}"
DKP_MIRROR="${GBA_DKP_MIRROR:-https://wii.leseratte10.de/devkitPro/devkitARM/r68%20%282026-06-10%29}"
if ! needs_track_b; then
  log "no Butano/homebrew-shaped repo detected (pokeemerald-only env) — skipping devkitARM Track-B mirror pull (R3b gate; GBA_TRACK_B=force overrides)"
elif [ -x "$DKP/devkitARM/bin/arm-none-eabi-gcc" ]; then
  log "devkitARM already present at $DKP/devkitARM — skipping install"
else
  log "devkitARM r68 from mirror: $DKP_MIRROR"
  mkdir -p "$DKP" /tmp/dkp-pkgs
  dkp_ok=1
  for pkg in \
      "devkitARM-r68-1-any.pkg.tar.zst" \
      "devkitarm-binutils-2.46.0-1-linux_x86_64.pkg.tar.zst" \
      "devkitarm-gcc-16.1.0-1-linux_x86_64.pkg.tar.zst"; do
    curl -fsSL --retry 2 -o "/tmp/dkp-pkgs/$pkg" "$DKP_MIRROR/$pkg" \
      && tar --zstd -xf "/tmp/dkp-pkgs/$pkg" -C / --strip-components=0 \
           opt/devkitpro 2>/dev/null \
      || { log "package $pkg failed (non-fatal)"; dkp_ok=0; }
  done
  if [ "$dkp_ok" -eq 1 ]; then
    # make-rules + crt0 are NOT in the mirror's r68 dir — build from source
    # (the scout-proven half of the route). Tiny makefiles; seconds to build.
    export DEVKITPRO="$DKP" DEVKITARM="$DKP/devkitARM"
    for src in devkitarm-rules devkitarm-crtls; do
      ( cd /tmp && rm -rf "$src" \
        && git clone --quiet --depth 1 "https://github.com/devkitPro/$src" \
        && cd "$src" && make >/dev/null 2>&1 && make install >/dev/null 2>&1 ) \
        || log "$src build failed (non-fatal — Track B builds may miss make-rules/crt0)"
    done
    log "devkitARM r68 installed at $DKP"
  else
    log "devkitARM install incomplete (non-fatal — Track A + headless loop unaffected)"
  fi
fi
# Persist the env for the session (best-effort; harmless if profile unused).
# Only when the toolchain is actually on disk — a gated-off (pokeemerald-only)
# env gets no dangling DEVKITPRO exports.
if [ -d "$DKP/devkitARM" ]; then
  export DEVKITPRO="$DKP" DEVKITARM="$DKP/devkitARM"
  { echo "export DEVKITPRO=$DKP"; echo "export DEVKITARM=$DKP/devkitARM"; \
    echo 'export PATH="$DEVKITARM/bin:$PATH"'; } >> ~/.bashrc 2>/dev/null \
    || log "bashrc persist failed (non-fatal)"
fi

# --- Block 4: per-repo setup -------------------------------------------------
# Detection order, most-specific first (every branch guarded):
#   1. scripts/env-setup.sh  -> the repo knows best (escape hatch).
#   2. pokeemerald tree      -> build agbcc per INSTALL.md (Track A; only
#      extra apt dep already installed in Block 2).
#   3. requirements.txt      -> pip install it (existence-guarded).
#   4. pyproject.toml        -> editable install, [dev] extra first.
#   5. nothing               -> skip silently (docs-only repo is fine).
setup_one() {
  repo_dir="$1"
  name="$(basename "$repo_dir")"
  if [ -f "$repo_dir/scripts/env-setup.sh" ]; then
    log "$name: running scripts/env-setup.sh"
    ( cd "$repo_dir" && bash scripts/env-setup.sh ) \
      || log "$name: env-setup.sh failed (non-fatal, continuing)"
  elif [ -f "$repo_dir/include/global.h" ] && [ -f "$repo_dir/Makefile" ]; then
    # pokeemerald-shaped tree (Track A): build+install agbcc per INSTALL.md.
    if [ -x "$repo_dir/tools/agbcc/bin/agbcc" ]; then
      log "$name: agbcc already installed — skipping"
    else
      log "$name: building agbcc (pret/agbcc, INSTALL.md route)"
      ( cd /tmp && rm -rf agbcc \
        && git clone --quiet --depth 1 https://github.com/pret/agbcc \
        && cd agbcc && ./build.sh >/dev/null 2>&1 \
        && ./install.sh "$repo_dir" >/dev/null 2>&1 ) \
        || log "$name: agbcc build failed (non-fatal, continuing)"
    fi
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
    log "$name: no manifest — skipping (fresh/docs-only lane is fine)"
  fi
}

# --- Block 5: multi-repo vs single-repo detection ---------------------------
# Multi-source environment: cwd is a WORKSPACE whose child dirs are the git
# clones (this exact shape, unhandled, killed sessions in 4+ lanes).
# Single-repo environment: cwd IS the repo (it has .git).
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

# --- Block 6: unconditional success ------------------------------------------
# The single most important line in the file (R15). Do not "improve" this.
log "setup complete (defensive shim: always exit 0)"
exit 0
