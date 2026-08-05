# Google Play submission requirements — verified for Swingy Spider

> **Status:** `reference`
>
> Researched 2026-08-05 for `menno420/spider-swing`. Every requirement below
> carries the official URL **this session fetched itself**. Claims that could
> not be confirmed against an official page are marked **NULL — unverified**
> rather than dropped or smoothed over.
>
> Method: `gemini-3.1-pro-preview` on the paid key with `google_search`
> grounding produced requirement-plus-URL pairs; each URL was then fetched
> directly. Grounded citations were treated as leads, not facts — and one was
> wrong (§9).

## 0. The two facts that decide the schedule

Everything else here is a form to fill in or a file to build. These two set the
calendar:

1. **A personal developer account created after 2023-11-13 must run a closed
   test with 12 testers opted in continuously for 14 days before it may even
   *apply* for production access**, and the application then takes ~7 days to
   review (§8). That is a **three-week floor** from a standing start, and it
   cannot be shortened by having the build ready.
2. **From 2026-08-31 — 26 days from this writing — new submissions must target
   API 36** (§3). The repository now targets 36, so this is satisfied; it is
   listed because missing it would have meant a rebuild, not a resubmit.

## 1. The artifact: App Bundle, not APK

*Source, fetched: [developer.android.com/guide/app-bundle](https://developer.android.com/guide/app-bundle)*

- Verbatim: *"From August 2021, new apps are required to publish with the
  Android App Bundle on Google Play."* The owner's framing was correct.
- Total compressed download for an install must be **≤ 4 GB**.
- Apps larger than **200 MB** must use Play Feature Delivery or Play Asset
  Delivery. (Not a constraint here — this is a small 2D game.)
- App Bundles **do not support** APK expansion (`.obb`) files.
- From June 2023, new *and existing* TV apps must also be bundles.

**Not stated on that page:** whether APK updates to pre-2021 apps are still
accepted. Irrelevant here — this is a new app — so recorded as **NULL —
unverified** rather than inferred.

## 2. Producing the bundle from Godot

*Source, fetched: [docs.godotengine.org — Exporting for Android](https://docs.godotengine.org/en/stable/tutorials/export/exporting_for_android.html)*

- Verbatim: *"To export an AAB file you need to set up Gradle builds for
  Android."* An AAB cannot come out of the prebuilt-template path the debug
  preset uses.
- **OpenJDK 17** recommended; higher versions supported.
- SDK components: Platform-Tools **35.0.0+**, Build-Tools **35.0.1**, Platform
  **35**, Command-line Tools latest, NDK **r28b (28.1.13356709)**, CMake
  **3.10.2.4988404**.
- Sign with a non-debug keystore and uncheck "Export With Debug".

**Read from Godot 4.7 engine source**, because the class reference documents
`gradle_build/export_format` only as *"Application export format (\*.apk or
\*.aab)"* and never gives the numeric values — a preset is a text file, so the
number is what actually matters:

| Fact | Where |
|---|---|
| `export_format` hint is `"Export APK,Export AAB"`, default `EXPORT_FORMAT_APK`; bounds check proves **APK=0 < AAB=1** | `platform/android/export/export_plugin.cpp` |
| AAB + `use_gradle_build=false` is rejected by the preset validator | same, `export_format` validator |
| Export path must end `.aab` or the export errors | same |
| `DEFAULT_MIN_SDK_VERSION = 24`, `DEFAULT_TARGET_SDK_VERSION = 36` | same |
| Min SDK below 24 is refused — *"the version needed by the Godot library"* | same |
| `--install-android-build-template` exists and pairs with `--export-release` | `main/main.cpp` |

Godot 4.7's default target SDK (36) already equals what Play requires from
2026-08-31. The repository pins both explicitly anyway, so an engine upgrade
cannot move the target level silently.

## 3. Target API level

*Source, fetched: [support.google.com/…/answer/11926878](https://support.google.com/googleplay/android-developer/answer/11926878)
and [developer.android.com/google/play/requirements/target-sdk](https://developer.android.com/google/play/requirements/target-sdk)*

- **From 2026-08-31: new apps and app updates must target Android 16 (API 36)**
  or higher. Extension to **2026-11-01** requestable in the Play Console.
- Existing apps must target **API 35** to remain available to new users on
  devices newer than the app's target.
- Wear OS / Automotive: API 35. Android TV / XR: API 34.
- Permanently private org-internal apps are exempt.

**NULL — unverified:** neither page states the requirement *in force before*
2026-08-31. Practically moot (the build targets 36), and not worth asserting a
number that no fetched page carried.

## 4. Signing

*Source, fetched: [support.google.com/…/answer/9842756](https://support.google.com/googleplay/android-developer/answer/9842756)*

Play App Signing splits the key in two, and conflating them is the classic
mistake:

| | Upload key | App signing key |
|---|---|---|
| Held by | **the developer** | **Google** |
| Format | `.jks` / `.keystore`, RSA **≥ 2048** | public cert `.der` / `.pem`, Google-generated **RSA 4096** |
| Signs | the bundle you upload | the APKs users actually install |
| Register with third-party APIs | ✗ | ✓ — this is the fingerprint services need |

- New apps are *"automatically enrolled in quantum-ready, hybrid signing with
  Google-generated keys"* and **cannot opt out** at creation.
- **A lost upload key is recoverable**: Play Console → *Protected with Play* →
  *Play Store protection* → *Manage Play app signing* → request reset with a new
  certificate. Worth knowing before the panic — losing it does not end the app.
- Never commit: keystores, private keys, `keystore.properties`, or anything
  carrying a keystore password.

**NULL — unverified:** the widely-repeated `-validity 10000` keytool
recommendation is **not** on this page. Gemini attributed it to a different URL
that was not fetched. Do not treat it as a Play requirement.

## 5. Application ID

*Source, fetched: [developer.android.com/build/configure-app-module](https://developer.android.com/build/configure-app-module)*

- At least **two segments**; each segment starts with a letter; characters
  `[a-zA-Z0-9_]`.
- Verbatim: *"Once you publish your app, you should never change the application
  ID. If you change the application ID, Google Play Store treats the upload as a
  completely different app."*

This is why `spider-swing` commits a placeholder rather than a chosen
identifier — see §10.

**Version codes**, from
[developer.android.com/studio/publish/versioning](https://developer.android.com/studio/publish/versioning)
(Gemini-reported, page **not** separately fetched — **treat as unverified**):
positive integer, max 2,100,000,000, cannot be reused, cannot decrease.

## 6. Store listing text

*Source, fetched: [support.google.com/…/answer/9859152](https://support.google.com/googleplay/android-developer/answer/9859152)*

| Field | Limit |
|---|---|
| App name | **30 characters** |
| Short description | **80 characters** |
| Full description | **4,000 characters** |

Limits apply identically to full-width and half-width characters. "Swingy
Spider" is 14 — comfortable.

## 7. Store listing assets

*Source, fetched: [support.google.com/…/answer/9866151](https://support.google.com/googleplay/android-developer/answer/9866151)*

| Asset | Requirement |
|---|---|
| App icon | **512 × 512**, 32-bit PNG **with** alpha, ≤ 1024 KB |
| Feature graphic | **1024 × 500**, JPEG or 24-bit PNG, **no** alpha |
| Screenshots | JPEG or 24-bit PNG, no alpha; min dimension 320 px, max 3840 px; **max side ≤ 2× min side** |
| Screenshot count | **≥ 2** to publish; **≤ 8** per device type |
| **Games specifically** | **≥ 3 landscape 16:9 screenshots at ≥ 1920 × 1080** (or 3 portrait 9:16 at ≥ 1080 × 1920) to be eligible for Play recommendations |

The game renders at a 1280×720 reference viewport in landscape — natively 16:9,
so real 1920×1080 captures are a straight upscale-free capture at a higher
window size, not a redesign.

**Caution carried from this estate's own measurement:** screenshots must be real
captures. Generated video/art fabricates UI and physics — one clip produced
three ATTACH buttons in a single frame. Fine for a feature graphic; never for
anything implying "this is how it plays."

## 8. Developer account and the testing gate

*Sources, fetched: [answer/6112435](https://support.google.com/googleplay/android-developer/answer/6112435)
and [answer/14151465](https://support.google.com/googleplay/android-developer/answer/14151465)*

- **US$25, one-time**, not recurring.
- Payment: MasterCard, Visa, Amex, Discover (US), Visa Electron (non-US).
  **Prepaid cards are not accepted.**
- Verification: *"a valid government ID and a credit card, both under your legal
  name."* If the information is judged invalid, **the fee is not refunded**.
- **The gate that sets the schedule:** personal accounts created after
  **2023-11-13** must run a closed test with **a minimum of 12 testers opted in
  continuously for at least 14 days** before applying for production access. The
  14 days must be *consecutive* — opting out and back in does not accumulate.
  All 12 must still be opted in at the moment of applying. Review then takes
  **~7 days**.

**NULL — unverified:** the D-U-N-S requirement for *organization* accounts.
Gemini cited `answer/13628312`, which was not fetched. Not applicable to a
personal account.

### 8b. How testers join — added 2026-08-05, second pass

*Source, fetched: [answer/9845334](https://support.google.com/googleplay/android-developer/answer/9845334)*

The first pass left tester mechanics as an honest null. Fetching the page
settles it, and overturns the intuitive workaround.

| Track | Admission | Ceiling |
|---|---|---|
| Internal | email list only — *"You can create a list of internal testers by email address."* | 100 |
| Closed | email lists **or Google Groups** — *"you can add testers via email or Google Groups"* | 200 lists × 2,000 |
| Open | *"anyone can join your testing program"* | unlimited (or ≥1,000 cap) |

Three consequences worth carrying to any other app in this estate:

1. **The opt-in link is an enrolment page, not an invitation.** Permission comes
   first: *"If you're running a closed test with a Google Group, users need to
   join the group before opting into your test."* Sharing the link with someone
   who is not admitted does nothing.
2. **Open testing is not a shortcut past the closed test.** *"Open testing is
   available when you have production access."* Production access is what the
   closed test is a precondition for, so the ordering is fixed: closed →
   production access → open. The obvious optimisation is unavailable by
   construction.
3. **Google Groups is the only self-serve admission path.** Groups' *"Who can
   join group"* setting offers *"Anyone can join"* — self-add from the open web,
   no approval ([groups/answer/2464926](https://support.google.com/groups/answer/2464926),
   fetched 2026-08-05). Pointed at a closed track, that produces a genuine
   press-a-link-and-enrol flow **on the same track that satisfies the 12 × 14
   requirement**. Internal testing cannot do this — it takes no groups.

**Still NULL:** the closed-track opt-in URL format. This estate's app shows an
internal link shaped `/apps/internaltest/<numeric-track-id>`, so the commonly
repeated `/apps/testing/<package-name>` cannot be assumed to be the closed shape.
Console prints the real link; that is the only source worth trusting.

## 9. Policy gates — all of them apply to an offline game with no data

*Sources, fetched: [answer/10787469](https://support.google.com/googleplay/android-developer/answer/10787469),
[answer/9859655](https://support.google.com/googleplay/android-developer/answer/9859655),
[answer/9893335](https://support.google.com/googleplay/android-developer/answer/9893335)*

The intuition that a no-accounts, no-ads, no-analytics, fully offline game skips
the privacy paperwork is **wrong**, and it is the most expensive wrong
assumption on this list:

- **Privacy policy URL — required regardless.** Verbatim: *"Even developers with
  apps that do not collect any user data must complete this form and provide a
  link to their privacy policy."* It needs to be a **live public URL**, so it
  needs hosting.
- **Data safety form — required regardless**, for all apps including those on
  closed, open, or production testing tracks. Only *internal* testing is exempt.
  For this game the honest answer to every question is "no data collected".
- **Content rating (IARC) — required.** Apps without a rating are not permitted.
  Misrepresenting content *"may result in its removal or suspension."*
- **Target audience declaration — required** before publishing. Selecting more
  age groups than the app was genuinely designed for is itself a violation; if
  children are not a target audience, the Families requirements (certified ad
  SDKs, parental controls) do not apply.

> **A miscitation caught here, recorded because the method is the point.**
> Gemini cited `answer/9859751` for the content-rating requirement. That page is
> about *publishing status*, not content ratings, and says nothing about IARC.
> The correct page is `answer/9859655`, found and fetched separately. The
> requirement was real; the citation was not. This is exactly the failure the
> "fetch it yourself" rule exists to catch, and it fired on the first pass.

**NULL — unverified:** the government-apps declaration, financial-features
declaration, and advertising-ID declaration. Gemini cited a bare
`support.google.com/googleplay/android-developer` root for the last two — not a
specific page, so nothing to fetch and nothing to confirm. They are plausible
and likely appear in the Play Console's App Content section; they are **not
verified here**, and the Console will list what it actually wants.

## 10. Games-specific

*Gemini's answers in this area returned **zero grounding chunks** — meaning the
model answered from memory, not from search. None of it was fetched. Recorded as
**NULL — unverified** in full, and deliberately not acted on.*

The unverified claims were: Play Games Services is optional; PGS branding
requires achievement/leaderboard UI entry points if adopted; Play Games on PC
requires x86-64 support. **Do not rely on any of these.** They are listed only
so a later session does not mistake "unresearched" for "researched and clear".

The open question from the task brief — *does Play require anything specific to
games?* — is therefore still open, beyond the verified 16:9 screenshot rule in
§7, which is a recommendation-eligibility criterion rather than a gate.

## 11. What landed in the repository

`menno420/spider-swing` PR #162, ADR 0005:

- `Android Release` export preset — Gradle build, `export_format=1` (AAB),
  min/target SDK 24/36, `arm64-v8a` + `x86_64`.
- `.github/workflows/android-release.yml` — dispatch-only, never publishes,
  substitutes owner-set `RELEASE_PACKAGE_ID` / `RELEASE_APP_NAME` and refuses to
  build while unset, builds unsigned until an upload key exists, and proves the
  output is a real bundle (`BundleConfig.pb` + `base/manifest/AndroidManifest.xml`).
- `.gitignore` additions — notably `*.jks.base64` / `*.keystore.base64`, because
  a keystore encoded for a repository secret stops matching `*.jks` and would
  otherwise slip past every existing rule.
- Five contracts in `tests/test_runner.gd` (256/256 green, `verify.py` exit 0),
  two of them mutation-tested.

**The honest gap:** `android-release.yml` has **never run end to end**. It
cannot, from a session — it needs the owner's repository variables. What is
verified is that Godot resolves the preset by name and parses it (the local
export attempt failed only on missing SDK/templates, never on configuration),
and that the identity substitution rewrites the release preset while leaving the
debug preset byte-identical. Expect the first real run to need adjustment.

## 12. Owner-only items

Filed as `OQ-PLAY-ACCOUNT`, `OQ-PLAY-CLOSED-TEST`, `OQ-PLAY-UPLOAD-KEY`,
`OQ-PLAY-PRIVACY-POLICY`, `OQ-PLAY-LISTING`, and `OQ-PLAY-APP-ID` in
[`../owner-queue.md`](../owner-queue.md).
