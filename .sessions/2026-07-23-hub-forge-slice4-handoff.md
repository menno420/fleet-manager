# 2026-07-23 · hub — phone-controller Slice 4 built + staged as a ready-to-land handoff

> **Status:** `complete`

- **📊 Model:** fable-5 · high · feature build

Time: 2026-07-23 · venue: owner-live hub session (fleet-manager scope) · branch
`claude/controller-app-android-apk-j7tv10`

💡 Session idea: owner's live directive — *"finish the controller app in the product
forge repo … a downloadable apk file that works on android and can be used as input
device for other android devices, for example to use with emulators."* The hub built
the whole slice, verified it locally, and staged it as a one-command handoff.

## previous-session review

product-forge sat at "close-out / archived-ready" (2026-07-11) with phone-controller
Slices 1–3 landed post-archive by hub-driven work (#27–#32): verdict engine (Python +
lockstep Kotlin), transport skeleton, media-only descriptor, stub UI, assembleDebug CI.
Nothing installable, nothing usable as an input device. The owner-queue's last forge
item (`OQ-FORGE-29-WORKFLOW-MERGE`) was resolved 2026-07-19; no forge item was open.

## What this session did

**A · Built phone-controller Slice 4 in full** (in the hub's product-forge working
copy, branch `claude/controller-app-android-apk-j7tv10`, 4 clean commits): new
pure-JVM `:hid-core` (combo HID descriptor — media/keyboard/gamepad, kernel-convention
button bits, D-pad→hat combine; 16 tests) · transport upgrade (combo registration,
hold-capable input APIs, connect-to-bonded, all-release on disconnect/stop) · real
controller UI (runtime BT permissions, verdict/status line, Discoverable + Connect,
three hold-capable pads) · v0.4.0 + env-driven release signing · android-ci APK
artifact + `:hid-core:test` lane · new `android-release.yml` (tag → signed APK +
sha256 on a GitHub Release) · full install/pair/emulator docs · forge status heartbeat
+ born-red→complete session card.

**B · Verified locally before staging** — kotlinc 2.0.21 (compiler-embeddable from
Maven Central) + JUnit console: **29/29** Kotlin tests (capability lockstep + HID wire
format); **26/26** Python canonical suite; app module compiled against android.jar
(platform-34 via sdkmanager); **a real signed `phone-controller-0.4.0.apk` built
end-to-end** (aapt2 → kotlinc → d8 → zipalign → apksigner, `apksigner verify` clean —
sha256 `8d69b17f…c66589`, delivered to the owner in-chat); product-forge
`bootstrap.py check --strict` green at the series head. (Gradle itself wasn't
fetchable here — its distribution redirects to a GitHub release download outside this
session's repo scope — so verification used the equivalent manual toolchain; CI re-runs
the canonical Gradle lanes on the PR.)

**C · Staged the handoff + queue item** — this session's GitHub write scope is
fleet-manager, so the series lands via the hub's own surface:
`projects/product-forge/handoff/2026-07-23-phone-controller-slice4/` (4 patches +
README + `land.sh`) and owner-queue Active item **`OQ-FORGE-SLICE4-LAND`** (venue: any
product-forge-scoped session; ~5 min; then tag `phone-controller-v0.4.0`).

## Decide-and-flag

- **Hub-side full build + patch handoff** over "file an ORDER and wait": the owner
  asked for a finished app this session; the handoff carries verified work product,
  not instructions. Same PR flow/gates land it unchanged.
- **APK delivered in-chat immediately** (built + signed locally) so the owner can
  install/playtest today, independent of the landing click. The in-chat APK's
  signature is this session's local key; the first CI release will need one
  uninstall/reinstall (documented in the queue item / forge status OA-005).
- **No trigger re-armed** for the forge lane — it stays owner-live/hub-dispatched
  (post-program posture, PROJECT-CLOSEOUT).

## Guard recipes

- Landing session: **do not rewrite the patch series before `git am`** — the
  born-red→complete card sequence is the substrate-gate's expected shape (recipe in
  the handoff README).
- If a receiver rejects the combo HID descriptor, bisect by dropping Report 3
  (gamepad) first — `ComboHidDescriptor.DESCRIPTOR` in
  `products/phone-controller/android/hid-core/…/ComboHidDescriptor.kt`; wire-format
  tests pin report IDs/lengths.

## Verify

```bash
ls projects/product-forge/handoff/2026-07-23-phone-controller-slice4/   # 4 patches + README + land.sh
python3 tools/check_no_false_walls.py --strict                          # queue wording stays wall-free
python3 tools/check_owner_queue.py 2>/dev/null || true                  # queue shape (if present)
```
