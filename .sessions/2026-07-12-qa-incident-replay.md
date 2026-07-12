# 2026-07-12 — QA incident replay vs prompts v3 (Wave 3)

> **Status:** `complete`

📊 Model: fable-5 · QA worker dispatched by coordinator · start 2026-07-12 (born-red at open)

## Declared at open (born-red)

QA incident replay: prove every known failure class is prevented by shipped v3 text, or file the gap. Deliverable: docs/research/2026-07-12-qa-incident-replay.md (lands in a later commit on this PR).

## Close-out

Shipped `docs/research/2026-07-12-qa-incident-replay.md` (+ `docs/research/README.md` as the research-reports ledger / reachability root). Replayed all 80 register incidents against the 20 shipped v3 files (docs/prompts/v3/ @ main 8056b7e).

- **Verdicts (recounted from the merged table):** 50 PREVENTED · 19 WEAKLY-PREVENTED · 3 NOT-PREVENTED · 8 NOT-PROMPTABLE.
- **BLOCKERs (NOT-PREVENTED + yes-observed):** I-63 (add_repo/shallow-clone reach path absent; websites B header falsely claims the clause moved to its C block), I-69 (no spawn-liveness/first-heartbeat check on dispatch), I-78 (create_or_update_file raw-text-not-base64 caveat missing everywhere).
- **HIGH:** contradictions C-1 (self-arm vs never-self-arm in one paste), C-2 (trading merge lane unscoped), C-7/C-8 (trigger-id delete lists vs status.md armed registry); drift D-2 (FAILSAFE WAKE ×9 unstamped, gets armed into the registry) / D-3 (PACEMAKER line forked into 3 live variants); the stale-B-files class (8 shipped B files predate A@LANDING — I-71's dispatch line deployed nowhere; I-15; I-30's ORDER-truth caveat missing in 4 seats).
- **Owner-queue gaps (NOT-PROMPTABLE, uncovered):** I-37, I-43, I-52 (HOT — venture #51 public sellable photos), I-55, I-67 (parked unnumbered email-pack item only).
- Verified locally: `python3 bootstrap.py check --strict` clean apart from the designed born-red hold + a pre-existing owner-action advisory.

💡 Session idea: stamp every duplicated prompt block with a one-line canonical-source header (`<!-- canonical: <file>#<block> @ <sha> -->`) at generation time — the GEN-3/PERMISSIONS blocks already prove the pattern works (the audit's only clean negatives), and it would make drift like D-2/D-3 mechanically detectable by a trivial checker instead of requiring a manual 20-file diff audit.

⟲ Previous-session review: the prompts-v3 build session (#98) shipped a strong layered set, but it shipped 8 B files already stale against its own A (pre-edit A@1915599, missing the LANDING dispatch line) and forbade hand-retrofit without providing the regeneration step — the exact drift class this replay's D-1 and stale-B-files findings flagged. Improvement: a prompt-set PR should regenerate all derived pastes from their sources in the same commit (or CI-diff A against the embedded copies), so "derived file lags its template" can never merge.
