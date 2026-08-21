# 2026-08-21 — Hub truing after couch-legend's first Android APK

> **Status:** `complete` — branch `claude/couch-legend-android-apk-z62fu3`.
> Hub-side only. The session's substantive work is **couch-legend #11**
> (merged, `02e27ca`), where its own born-red card carries the full close-out,
> the verify ledger and the Codex trail.

- **📊 Model:** opus-5 · estate truing (docs + one route)

## What this is

The session built couch-legend's milestone A — the existing web build wrapped
in the decided Capacitor shell, with CI assembling a **debug-signed APK** the
owner sideloads (`[D-0002]` / `[D-0003]`, DESIGN § 7). That landed in the
product repo. This card covers only what the **hub** had to stop saying.

**Shipped here:**

- `docs/repos/couch-legend/README.md` — the Android thread flips from **NEXT**
  to **MILESTONE A LANDED**, and its stale sibling ("NEXT = the Claude
  implementation session") goes with it, since #7 landed that. The rewrite is
  deliberately blunt about the thing a plan could get wrong: **milestone B is
  owner-gated, not code-gated.** No agent container has an SDK, emulator or
  device, so real Android System WebView behaviour cannot be closed from here
  at any effort — it waits on the owner installing the APK and reporting
  force-stop save survival, crossfade/particle smoothness and offline launch.
- `.claude/hooks/doc-routes.json` — the same correction in the `repo-couch-legend`
  route's `says`. **This is the load-bearing half.** The README is what a
  session reads if it goes looking; the route is what gets pushed at it whether
  it looks or not, and it was about to tell the next session that the Android
  shell was still ahead of it and that an implementation session it already has
  was next.

## Verify

- `python3 -c "import json; json.load(...)"` on `doc-routes.json` → valid;
  `git diff --stat` on it → **1 insertion, 1 deletion**, i.e. the one `says`
  string and nothing else.
- couch-legend #11 merged at `02e27ca` with all four checks green (`ci`,
  `substrate-gate`, `debug apk`, `android merge check`); the APK from the
  `main` run was downloaded, verified (5.26 MB, APK Signature Scheme v2, 27
  bundled web assets, `versionName 0.2.0`) and handed to the owner directly.

## ⚑ Left open deliberately

The application id **`com.menno420.couchlegend`** was taken as the default and
flagged in the PR while objecting is still cheap; it costs a reinstall once the
APK is installed, and is permanent if the game ever ships on Play. Also
unchanged: couch-legend's `android` workflow is **not** a required status check
— making it one is a ruleset change the owner did not ask for.

## 💡 Session idea

**A stale routing string is worse than a stale document, and only one of them
has a mechanism.** This estate already knows that "the fix for an unfollowed
rule is a mechanism that delivers it at the right moment" — `doc-routes.json`
is that mechanism, and it inherits the failure mode of every hand-maintained
record: it goes stale, but *invisibly*, because nobody reads it, they only get
read *to*. The route here was two threads out of date and would have pushed
both errors at the next session with the authority of a hook. Worth a check
that flags a `says` whose named PR numbers or "NEXT =" clause have been
overtaken — the same class the kit's aging/staleness checkers already handle
for documents. **Guard recipe:** the anchor is `route_docs.py` reading
`.claude/hooks/doc-routes.json`; a checker in `tools/` walking every `says` for
`#\d+` references and resolving them against merged-PR state would catch it
mechanically, and it belongs beside `tools/check_doc_routes.py`, which already
parses that file.

## ⟲ Previous-session review

The Android-decisions session (#10, couch-legend) is the one this session
consumed, and it paid off exactly as intended: because `[D-0002]`, `[D-0003]`
and the toolchain probe were already in the ledgers, this session re-verified
the toolchain in one command and went straight to building instead of
relitigating sideload-vs-store. Its own `💡` — that the estate's keystore recipe
would exist in three places once couch-legend signs a release — is still unspent
**by design**: milestone A debug-signs, so no third copy was created.
