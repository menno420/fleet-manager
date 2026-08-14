# Session — controller app: repo question answered + Slice 18 built in product-forge

> **Status:** `complete`

📊 Model: fable-5 · high · product work under live owner directive

Time: 2026-08-14 · venue: hub chat (booted in fleet-manager, product-forge
attached mid-session — the Slice-4 precedent) · designated branch:
`claude/controller-app-customization-r7utv2`

💡 Session idea: owner, live: orient, look at product-forge's controller app,
answer *"new repo or continue in this repo?"*, then *"further improve it this
session, make it more customizable etc."* OD-13 deprioritizes product work as the
default pick; his live directive selects it for this session (named, per
intent.md § 6 — product work was never blocked).

## Previous-session review

fleet-manager at `108b452`: v1.21.0 rollout phase 3 complete 5/5 (gba unblocked
via owner bypass, program §7 2026-08-14 row). NOW unchanged: E1 owner-reserved,
D2 target open at `OQ-FM-D2-TARGET`, OD-13 standing. product-forge untouched
since Slice 17 (2026-07-24, `81b65bd`).

## What this session did

1. **Six-read cold orientation** — clean; boot diagnostic case one.
2. **Intake intent map** (skill fired per the routing table) — INTENT STATUS:
   RESOLVED; the repo question's destination was already owner-decided (program
   §2 + R2 + the incubator mechanic), only timing was open (MEDIUM,
   decided-and-flagged: graduation is its own next step, not this session's).
3. **Slice 18 in product-forge** (PR #49, v0.18.0): per-widget behavior config,
   long-press alternates, fine position sliders, backup/restore-everything +
   `compile-check.sh` (the no-SDK app compile proof, committed). Fixed en route:
   custom-layout touchpads never received global sensitivity/scroll-invert.
4. **Layer-2 folder `docs/repos/product-forge/`** created on demand (README
   only; depth files honestly not-yet-written): the repo answer, the app thread,
   and the R2 graduation recipe with the measured keystore constraint (stable
   keystore lives ONLY in repo secrets — values unreadable agent-side; three
   carry options recorded, fresh-keystore-plus-backup recommended now that
   Slice 18 makes a signature break costless).

## Verification

product-forge: JVM suites 59/59 · Python 26/26 · compile-check 100 classes / 22
files · gate exit 0 · Codex review awaited before merge (estate rule beats the
seat-era merge-anyway convention) · release verified on the tag with sha256.
fleet-manager: `python3 bootstrap.py check --strict` real exit code before push.

Layer-2 handoff: docs/repos/product-forge/README.md — repo-question + graduation
threads created

## Honest flag — orientation budget

`orientation-budget` fires at **7042/7000 words** on this branch (exit-neutral).
Baseline at HEAD was ~6980 — the ledger's preserved tail, not this session,
holds the budget hostage: my Recently-shipped entry is 62 words and the file
carries ~4400 words of pre-2026-07-19 seat-era entries below its own
"preserved, not current" banner. Left flagged, not contorted around and not
suppressed: the durable fix is an OD-3-amended archive pass over that tail
(move to a dated archive file, pointer left behind) — a records cleanup that
deserves its own decided-and-flagged pass, not a rider on a product slice.

## Result

- **product-forge #49 MERGED** — squash `6c33382`, all 5 checks green on the
  reviewed-and-fixed head `8849814`. Codex: 5 findings (1×P1, 4×P2),
  **[conceded] ×5**, fixed pre-merge, tally in the PR thread. First-ever Codex
  review in that repo answered at ~9.6 min (vs fm's 335 s) — the session's
  interim "app not installed" inference was wrong, corrected in place (card ·
  status.md · review-queue.md · this repo's records); the `do-not-automerge`
  park held the PR unmerged through the whole wrong-belief window.
- **Release VERIFIED live:** tag `phone-controller-v0.18.0` at merge SHA
  `6c33382` (REST refs path) → android-release run completed:success →
  release "Phone Controller v0.18.0" carries `phone-controller-0.18.0.apk`
  (2,457,961 bytes) + `.sha256`, and the job log prints **"signing: stable
  repo keystore"** — installs in place over v0.17.0, no re-pair (no HID
  descriptor change).
- **fleet-manager records** (this PR): current-state pointer entry · §7 row ·
  owner-queue corrections · Layer-2 `docs/repos/product-forge/` built.
- **The repo answer delivered:** both, in order — features in product-forge,
  graduation as R2's own step (recipe + keystore constraint recorded in the
  Layer-2 entry).

⚑ Orientation-budget overage flagged (see § Honest flag) — archive pass on the
Recently-shipped tail proposed as its own session.
💡 Session idea: `compile-check.sh`'s stand-in-R pattern generalizes to any
Android repo in the estate without an SDK-bearing container — worth folding
into the kit if a second Android product appears (deliberately not done now;
one adopter is not a pattern).
⟲ Previous-session review: in the card body above (§ Previous-session review).

## Review dispositions (fm #859)

Codex round 1 (10:22:49Z, on `2a8482f`): **1 finding, [conceded]** — the pushed
card carried an in-progress badge + placeholder Result beside a §7 row saying
shipped. This commit is the fix: Result filled with the verified terminal facts
(pf #49 merged `6c33382`; release + stable signing verified), badge flipped.
**Flip-exemption accounting, per session-close 6c:** after reviewed SHA
`2a8482f`, this head adds (a) the card close-out + badge flip (the exempt
class), and (b) one `docs/CAPABILITIES.md` append (the codex cold-repo latency
datum) — (b) is reviewable, so a round-2 review is requested on this head
rather than taking the exemption alone; the `do-not-automerge` park stays on
until that answers. Round cap 2 per the skill; this is round 2.
