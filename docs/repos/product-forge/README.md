# product-forge / phone-controller — the entry point

> **Status:** `living-ledger` · true as of **2026-08-14**
>
> **What this is:** fleet-manager's entry point for `menno420/product-forge` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The repo's own `products/phone-controller/README.md`
> wins on the app, `control/status.md` wins on session state, and the live tree
> wins over both. Depth files (`capabilities.md` · `records.md` ·
> `working-here.md`) are **not yet written** — this folder was created on demand
> (Slice-18 session) and carries only the entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`product-forge` is the closed fleet's **product build seat** — a seat-era shell
(kit v1.7.0, `control/` bus, CONSTITUTION) whose one living asset is
**phone-controller**: a real, shipped Android app that turns a phone into a
customizable Bluetooth-HID controller (keyboard / gamepad / mouse / media / DS-style
touch) for any other device, with no software on the target. `MEASURED`
2026-08-14: stable-signed APK releases v0.4.0 → v0.18.0 on the repo's releases
page, owner-playtested and field-driven (the Slice 15–17 features all came from
his device feedback). Everything else in the repo — `products/games-web/`, the
control bus, the seat docs — is history or migration stock, and the consolidation
program's §2 marks the post-graduation remainder **archive-bound**.

## The repo question, answered (2026-08-14, this session)

*"New repo for the controller app, or continue in product-forge?"* — **Both, in
order.** Feature work continues in product-forge (the proven signed-release
rails), and the app graduates to its own repo as its own finished step — that
graduation is already the standing plan three ways (`OWNER`: program §2 "Phone
Controller | phone-controller (graduated from product-forge)"; step **R2**; the
repo's own owner-confirmed incubator mechanic). It is deliberately **not**
executed mid-feature-session (OD-6: one thing at a time, finished properly).

## Threads

### Thread: the app (customization era) — **active**, updated 2026-08-14

Where it stands: **Slice 18 / v0.18.0** — per-widget behavior config (per-stick
deadzone + invert-Y, D-pad 4/8-way, per-touchpad speed + pen mode), long-press
alternate actions, fine position sliders, **backup/restore-everything**
(insurance for any reinstall or signature change). Slices 10–17 before it:
share/import, macros, voice, overlay play-on-this-phone, recorded gestures, gyro
targets, placeable widgets, true multi-touch, editor polish. The one recorded
candidate still open: **BLE-HOGP fallback transport** for `BLE_HOGP_FALLBACK`
-verdict devices. A future Play-Store listing with a ~€1 cosmetic supporter pack
is groundwork-only (Slice 9, fairness promise committed in the README).

Pointers (all in product-forge): `products/phone-controller/README.md` (the app,
honest state) · `.sessions/2026-08-14-phone-controller-slice18-customization.md`
(this session) · `android/compile-check.sh` (app-module compile proof, no SDK
needed) · `control/status.md` (heartbeat).

### Thread: graduation to `phone-controller` (program step R2) — **next, not started**

The step: subtree-split `products/phone-controller/` into a new `phone-controller`
repo with history, carry `android-ci.yml` + `android-release.yml`, leave a pointer
behind. Done-when (program R2): a clean clone builds a signed APK, CI green,
product-forge remainder ready for the archive queue.

**The one sharp edge — the signing keystore.** `MEASURED` 2026-08-14: the stable
keystore exists **only** as the repo secrets `PC_RELEASE_KEYSTORE_B64` /
`PC_RELEASE_KEYSTORE_PASSWORD` (set 2026-07-24 by the Slice-9 session via
sealed-box REST; product-forge `control/status.md:177` "Keystore lives ONLY in
the repo secret"). Secret **values are unreadable** agent-side, so carrying the
signature needs one of:

1. **Workflow relay** (agent-executable, no owner): a one-shot `workflow_dispatch`
   in product-forge reads the two secrets and writes them into the new repo via
   the API — it needs a token with access to the new repo (the account PAT
   placed as a temporary third secret, then deleted). Route exists; unexercised
   (`REASONED`).
2. **Fresh keystore** (simplest): generate + set new secrets in the new repo —
   the next install on the owner's phone is a one-time uninstall→reinstall, and
   **Slice 18's backup/restore exists precisely so that costs nothing**: backup
   on the old install, restore on the new.
3. **Owner paste**, only if he happens to hold the keystore file — the record
   says he does not (it was generated in-session).

Recommendation recorded 2026-08-14: option 2 unless the owner objects — a
signature break made costless is cheaper than moving credentials between repos.

## External workspaces (roadmap § 5.7 — pointers, never copies)

```yaml
drive:
  folder: null        # none known for this repo, 2026-08-14
chatgpt:
  workspaces: []      # none named for this repo in the record
gemini:
  notebooks: []       # empty until a corpus earns one
```

Null is normal — the mapping is optional and many-to-many. Add a pointer when
the owner names one; never invent a folder to fill the slot.

### Thread: games-web + repo remainder — **parked** (seat-era)

`products/games-web/` is slated for the websites arcade (seat-era ORDERs 023/024,
owner-gated then; re-decide at archive time). After graduation the remainder is
archive-queue per program §2 — cleanup under amended OD-3 needs its stated
reason per item.
