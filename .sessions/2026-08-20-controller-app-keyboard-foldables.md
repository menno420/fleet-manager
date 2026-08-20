# Session — controller app Slices 21+22: physical keyboards + foldables (records)

> **Status:** `in-progress`

📊 Model: fable-5 · high · feature build

Time: 2026-08-20 · venue: remote continuation session (owner directive
2026-08-16, relayed via handoff prompt) · designated branch
`claude/phone-controller-keyboard-foldable-sj4jem`, rebased onto `origin/main`
`0e36e85` after a parallel session landed fm #868 mid-flight

💡 Session idea: owner ask, verbatim (2026-08-16 — first recorded on the pf
Slice-21 born-red card, per the prompt's instruction that it existed nowhere
else): *"improving this app further to recognize keyboards etc that are added
to tablets or phones etc, so you can use the keyboard as input/controls or
just as a way to write. There should also be some extra support for foldable
phones etc. The next session should think about this and try to implement it
as properly as possible"*. "Think about this" read as a design mandate —
options · choice · reasons landed on the card BEFORE app code (pf Slice-21
card § D1–D6), then two slices, each finished properly (OD-6).

## Previous-session review

At session start: product-forge `main` `d5a412f` (= Slice 20 squash),
v0.20.0 the newest release, 0 open PRs; fleet-manager `main` `0f8a728` —
exactly the prompt's WHERE THINGS STAND, re-fetched not assumed. fm main then
moved to `0e36e85` under a parallel session (fm #868, keep-bot worklist) —
expected drift, records branch restarted from it. Layer-2 queued items both
consumed this session: the unconditional Settings-close refresh (shipped in
pf #52) and the L3/R3 premise correction (carried into the product README).

## What this session did (product side, already terminal)

- **pf #52 squash `e69afe5` → tag `phone-controller-v0.21.0`** — physical
  keyboards: InputManager detection, `dispatchKeyEvent` capture policy, TYPE
  mode (hid-core `KeyEventMap`, 9 tests), PAD mode (bindings via `resolveRaw`,
  VoiceStore pattern), ⌨ toggle, backup carriage, `keyboard` configChange,
  the queued refresh refactor, README + L3/R3 correction. Codex two rounds,
  6 findings — **[conceded] ×4 · [partial] ×1 · [survived] ×1**; the big
  concession became hid-core `HeldKeyLedger` (ref-counted holds, per-device
  release, stateless taps uncounted; 8 tests). Slice-18's lesson applied
  live: PR-open left Codex silent ~10 min — treated as non-evidence, the
  explicit `@codex review` trigger answered in ~6.5 min.
- **pf #53 squash `7a53b26` → tag `phone-controller-v0.22.0`** — foldables:
  `smallestScreenSize|density` configChanges hardening (fold no longer
  recreates + drops the connection) + per-screen layout memory (sw600
  bucket). Codex R1 **[conceded] ×2** (onCreate bucket restore · pending
  flip through the editor), R2 **clean** ("Didn't find any major issues").
- **Both releases VERIFIED live**: android-release completed:success both;
  APK + `.sha256` assets attached; sha256 two-way `feaf1d73…` (0.21.0) and
  `0916a484…` (0.22.0); "signing: stable repo keystore" in both run logs;
  signer certificate parsed from the v2 APK Signing Block **byte-identical
  v0.20.0 ↔ v0.21.0 ↔ v0.22.0** (sha256 `7bda3340…`).
- Pre-tag sweeps run both sides of each merge: `d5a412f..main` = exactly the
  #52 squash at tag-21 time; `e69afe5..main` = exactly the #53 squash at
  tag-22 time.

## Honest reds and venue facts (owned, not hidden)

- One CI red this session was self-inflicted: a future-dated heartbeat stamp
  (353 s ahead) red on pf #52's `check` job — heartbeat-guard working as
  built; stamped real UTC since.
- One $?-after-a-pipe misread of a gate exit happened mid-session (the tail
  of a piped gate run echoed `tail`'s exit) — caught in-session, re-run with
  the real exit code; named here because the rule exists for exactly that.
- The local `git push` of tag `phone-controller-v0.21.0` reported
  "Everything up-to-date" while `ls-remote` showed NO remote tag — venue
  quirk, not a wall: both tags went via `POST /git/refs` over direct PAT
  (create verified by `ls-remote` after, both releases fired).
- No Android device or foldable exists in this venue: capture semantics and
  both recreation fixes are REASONED from the platform contract + sources
  read in full; owner device steps are on both pf cards.

## Records (this PR)

§7 row (2026-08-20, both slices) · Layer-2 app thread → Slices 21+22 /
v0.22.0, queued refresh item consumed, L3/R3 correction carried, two new
recorded candidates (hardware-key macro bindings · producer-wide
hold-ownership model — both from Codex rounds, neither queued) ·
current-state "Recently shipped" pointer widened to Slices 18–22 · Layer-2
MEASURED stamp refreshed (v0.4.0 → v0.22.0, cert-match note).

Layer-2 handoff: docs/repos/product-forge/README.md — app thread updated

## Result

- pf #52 MERGED `e69afe5` (v0.21.0) · pf #53 MERGED `7a53b26` (v0.22.0) ·
  both tags live · both releases verified (assets · sha256 · signing line ·
  signer-cert match) — the DONE-WHEN chain for the product half is closed.
- Records in this PR per § Records; `python3 bootstrap.py check --strict`
  run with its REAL exit code before the ready-flip.
