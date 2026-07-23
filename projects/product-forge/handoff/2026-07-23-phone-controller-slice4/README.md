# Handoff — phone-controller Slice 4 (usable controller app + downloadable APK)

> **Status:** `landed` · staged and then landed 2026-07-23 by the same hub session
> (owner-live directive: finish the controller app as a downloadable APK usable as a
> BT-HID input device for other Android devices, e.g. driving emulators). Mid-session
> the owner disabled automode and `add_repo` brought product-forge into scope, so these
> exact patches were pushed directly: product-forge PR #33 → squash `ccb1e98` → tag
> `phone-controller-v0.4.0` → Release live with the APK + sha256. This directory stays
> as provenance; `land.sh` is now only needed for a re-land from scratch.

This directory is a **complete, verified, ready-to-push branch** for
`menno420/product-forge`, staged hub-side as a `git format-patch` series (the hub
session's product-forge pushes route through this handoff; any product-forge-scoped
session lands it in ~5 minutes).

## What lands (4 commits → branch `claude/controller-app-android-apk-j7tv10`)

1. `0001` — born-red session card + heartbeat (product-forge conventions).
2. `0002` — **the app**: new pure-JVM `:hid-core` (combo HID descriptor: media +
   keyboard + gamepad; report builders; 16 tests) · transport upgrade (combo device,
   hold-capable inputs, connect-to-bonded, all-release on disconnect) · real controller
   UI (permissions → probe → Discoverable/Connect → three pads) · v0.4.0 + env-driven
   release signing · READMEs (install / pair / emulator mapping).
3. `0003` — **workflows**: `android-ci` uploads the debug-APK artifact + runs
   `:hid-core:test`; new `android-release.yml` publishes a signed APK + sha256 to a
   GitHub Release on a `phone-controller-v*` tag.
4. `0004` — close-out: heartbeat + session card flipped `complete`.

**Verified before staging** (details in the series' session card): Kotlin lanes 29/29
green (kotlinc 2.0.21) · Python canonical suite 26/26 · app module compiles against
android.jar (platform-34) · a real signed `phone-controller-0.4.0.apk` built end-to-end
with aapt2/kotlinc/d8/apksigner and `apksigner verify`-clean · `bootstrap.py check
--strict` green at the series head.

## How to land

From any product-forge-scoped venue (fresh Claude Code session with the repo in scope,
or the owner's machine):

```bash
./land.sh                    # clone → git am → gate check → push branch
```

then open the PR **ready** (base `main`), let `android-ci` + `substrate-gate` run, and
**merge on green**. The diff touches `.github/workflows/**`, so merge-on-green parks it
(owner-merge-only rail) — merging it directly on green under the owner's live directive
is the recorded precedent (product-forge PR #29, `OQ-FORGE-29-WORKFLOW-MERGE`). Prefer
strict rails? Commit `0003` is isolated: land `0001+0002+0004` as the code PR and
`0003` as a companion workflows PR.

After the merge, cut the release:

```bash
git tag phone-controller-v0.4.0 <merge-sha>
git push origin phone-controller-v0.4.0
# android-release publishes phone-controller-0.4.0.apk (+ .sha256) to Releases
```

VERIFY: <https://github.com/menno420/product-forge/releases> shows **Phone Controller
v0.4.0** with the APK attached, and `android-ci` is green on `main`.

## Notes for the landing session

- Signing secrets are OPTIONAL: without `PC_RELEASE_KEYSTORE_B64` /
  `PC_RELEASE_KEYSTORE_PASSWORD` the release lane signs with an ephemeral key
  (installs fine; cross-release in-place updates need the stable secret — see
  product-forge status ⚑ OA-005 for the one-step recipe).
- The owner playtest ask (two physical devices) is ⚑ OA-004 in the landed status.
- Do not rebase/squash-rewrite the series before `git am` — the born-red → complete
  card sequence is the substrate-gate's expected shape.
