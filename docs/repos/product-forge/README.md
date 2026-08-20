# product-forge / phone-controller — the entry point

> **Status:** `living-ledger` · true as of **2026-08-20**
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
2026-08-20: stable-signed APK releases v0.4.0 → v0.22.0 on the repo's releases
page (signer cert byte-identical v0.18.0 → v0.22.0, v2 signing-block parse),
owner-playtested and field-driven (the Slice 15–17 features all came from
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

### Thread: the app (customization era) — **active**, updated 2026-08-20

Where it stands: **Slices 21+22 / v0.22.0** — the owner's 2026-08-16 ask
(*"recognize keyboards … use the keyboard as input/controls or just as a way
to write. There should also be some extra support for foldable phones"*),
designed first (options · choice · reasons on the pf Slice-21 card § Design)
and shipped as two finished slices:

- **Slice 21 (pf #52, v0.21.0) — physical keyboards.** Detection
  (InputManager, external-alphabetic), capture via `dispatchKeyEvent` under
  an explicit policy (never volume/system keys; dialogs self-exempt), **TYPE
  mode** (live keycode→HID type-through — hid-core `KeyEventMap`, both-side
  modifiers, media keys) and **PAD mode** (key→action bindings through the
  shared `resolveRaw` vocabulary, VoiceStore-pattern store, optional defaults
  behind a confirm), ⌨ toggle visible exactly while a keyboard is attached,
  bindings+mode in backup (additive `pcb`-v1 key), and the `keyboard`
  configChange (hot-plug used to RECREATE and drop the connection). **The
  queued refresh item is CONSUMED**: the Settings-close enumeration is now an
  unconditional refresh guarded only by the open editor. Codex 2 rounds, 6
  findings ([conceded]×4 · [partial]×1 · [survived]×1): the load-bearing fix
  is `HeldKeyLedger` (hid-core) — (device, key)-keyed, reference-counted by
  action identity, per-device release, stateless taps uncounted — built for
  the two round-1 findings and pinned by 8 unit tests.
- **Slice 22 (pf #53, v0.22.0) — foldables.** `smallestScreenSize|density`
  join `configChanges` (a fold used to recreate the activity and drop the
  live HID connection — the manifest's rotation rationale, third instance)
  plus **per-screen layout memory** (sw600 bucket, rotation-invariant:
  compact pad on the cover screen, full pad inside, automatic; connect
  applies host memory, fold applies screen memory, last event wins). AndroidX
  WindowManager postures REJECTED explicitly — the Slice-3 AndroidX-free
  choice stands, recorded not silently skipped. Codex round 1 [conceded]×2
  (onCreate bucket restore · pending flip through the editor), round 2 clean.
- **The L3/R3 premise correction is carried**: the product README no longer
  claims a descriptor revision/re-pair — enum-only on already-transmitted
  bits (fm #864). Device-venue honesty: capture semantics and both
  recreation fixes are REASONED from the platform contract; the owner device
  steps are on both pf cards (§ Verification plan).

**Recorded candidates from the Codex rounds** (neither queued — surface if
the owner asks): hardware-key **macro bindings** (needs a binding-specific
picker; the macro builder is coupled to `PadButtonSpec`), and a
**producer-wide hold-ownership model** (on-screen pads + keyboard + voice
sharing transport state ref-counted — would have to exempt turbo's
deliberate same-bit pulsing; today's last-writer-wins is the app's standing
model, pre-dating the keyboard).

Slice 20 before them: the **PS2 pad as a directly selectable spinner entry**
(owner screenshot feedback; `t:<kind>` key class). Slice 19: the
**PS2 (DualShock) preset** itself
(glyph-colored round diamond, dual sticks, four digital shoulders; no HID
descriptor change, so it installed in place — L3/R3 stick-clicks deferred as
scope. **Premise corrected 2026-08-15, Codex on fm #864:** the live descriptor
already declares **16 button bits** — `ComboHidDescriptor.kt`'s own header,
"Gamepad = 16 buttons" — with the enum stopping at bit 11, so L3/R3 would be an
**enum-only addition on already-transmitted bits: no descriptor change, no
re-pair**).
Slice 18 the prior day (2026-08-14): per-widget behavior config (per-stick
deadzone + invert-Y, D-pad 4/8-way, per-touchpad speed + pen mode), long-press
alternate actions, fine position sliders, **backup/restore-everything**
(insurance for any reinstall or signature change). Slices 10–17 before them:
share/import, macros, voice, overlay play-on-this-phone, recorded gestures,
gyro targets, placeable widgets, true multi-touch, editor polish. Recorded
candidates still open: **BLE-HOGP fallback transport**, and L3/R3 (enum-only,
near-zero cost) if asked for. A future
Play-Store listing with a ~€1 cosmetic supporter pack is groundwork-only
(Slice 9, fairness promise committed in the README).

Pointers (all in product-forge): `products/phone-controller/README.md` (the app,
honest state) ·
`.sessions/2026-08-20-phone-controller-slice21-hardware-keyboard.md` (carries
the full keyboard+foldable DESIGN section, § D1–D6) +
`.sessions/2026-08-20-phone-controller-slice22-foldables.md` +
`.sessions/2026-08-16-phone-controller-slice20-ps2-spinner.md` +
`.sessions/2026-08-15-phone-controller-slice19-ps2-preset.md` +
`.sessions/2026-08-14-phone-controller-slice18-customization.md` (the five
slices) · `products/phone-controller/android/compile-check.sh`
(app-module compile proof, no SDK needed) · `control/status.md` (heartbeat).

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
