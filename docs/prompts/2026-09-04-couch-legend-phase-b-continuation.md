# Continuation prompt — Couch Legend, after the long-form redesign landed

> **Status:** `reference` · paste-ready, `continuation-prompt` skill shape,
> written 2026-09-04 at the close of the session that
> landed couch-legend #19 (`4934955`) and fleet-manager #1026 (`66f1b4e`).
> Every state claim in it was
> verified at HEAD on the day it was written; the receiving session re-verifies
> as its first step rather than trusting it.

The prompt below is the artifact. Everything above this line is provenance.

---

```text
CONTINUE: Couch Legend's long-form redesign. Phase A landed (couch-legend #19,
merged 4934955). Review what it actually did, then take the work forward —
phase B is the owner's feel pass and gates C and D, so part of your job is
establishing whether B's answer has arrived and working the ungated lanes if
it has not.

BEFORE YOUR FIRST TOOL CALL — state the task back, inline in this same reply,
in four labelled lines (never one fused paragraph, never a question):
  HE SAID — the ask in your own words, one or two sentences.
  ALREADY SETTLED — what the repo already decided about it, naming the file,
                    or "nothing found yet".
  I INFER — the specs, constraints and scope the ask implies, and the follow-on
            the owner probably wants but did not spell out. Labelled inference.
  LEAST SURE — the one reading you are least sure of; he corrects it in a word.
Then begin. This is the owner's one cheap chance to correct your aim; a first
reply that only announces your first action spends it.

WHERE THINGS STAND

- couch-legend `origin/main` = `4934955` ("Give every chapter something the
  couch keeps", #19). **0 open PRs.** Verified 2026-09-04.
- Branch `claude/couch-legend-design-arch-iwpo96` still exists at `d790461`.
  It is **merged and finished** — do not stack on it. New work restarts from
  `main` on a fresh branch.
- fleet-manager `origin/main` was `aef2429` when this was written and moves
  often; PR #1026 (`66f1b4e`) carried the Couch Legend routes into the hub.
- fleet-manager PR #1028 was open at `8a75072` with `substrate-gate` red on
  the born-red card hold **only** — that is the designed hold, not a defect.
  Believed merged by the time you read this; confirm.
- What phase A shipped, measured by re-running the census instrument at
  `4934955` (`pnpm exec tsx tools/stage-evolution.ts`, exit 0):
    18 stages · **14 introduce a new mechanic** · **3 deepen an existing
    shape** · **17 deliver something new** · 2 gate content rows · 3 have
    delivered scene art · 17 keepsakes minted into 6 couch places.
  Before phase A the same instrument reported 2/18 gating and **0/18**
  introducing. That delta is the point of the whole phase.
- Balance, 27 simulator runs: story close 12.0 d · worst attended dead time
  38.0 min (bound 45) · check-ins 98.0 %, every playing lane ≥ 97.1 % ·
  rebuild rails unchanged. **One stated breach survives:** a sub-2 %
  felt-upgrade reading in 1 of 27 runs, disclosed rather than tuned away.
  It is a real open item, not a rounding artifact — see the sim record.
- IAP: mockups only. `STORE_PREVIEW_ENABLED` is compile-time
  (`VITE_STORE_PREVIEW=1`) and `tools/check-store-preview.ts` asserts the
  production `dist/` contains none of five markers, with a positive control.
  No billing SDK, no store console, no receipts, no money. Unchanged rule.

READ FIRST — a floor, not a boundary

1. `docs/planning/2026-09-04-long-form-redesign.md` — the plan phase A executed
   and the § 8 phase table you are continuing. **This one wins** where it and
   an older doc disagree. *Verified at HEAD 2026-09-04.*
2. `docs/DESIGN.md` § 11 (couch/keepsakes, line 526) and § 12 (monetization,
   line 668) — what shipped and why, in the canonical design record; § 9.6
   (line 361) is the rails those changes are measured against; § 8 item 1
   (line 220) is the open Clarity question phase C answers.
   *Verified at HEAD 2026-09-04.*
3. `docs/sim/2026-09-04-couch-balance.md` — the before/after rail table and the
   one stated breach. *Verified at HEAD 2026-09-04.*
4. `.sessions/2026-09-04-the-couch-keepsakes.md` — the session card: what was
   done, what was conceded in review, what was left. *Verified at HEAD.*
5. In fleet-manager: `docs/repos/couch-legend/README.md` (Layer 2 entry) and
   `docs/owner-comments/couch-legend/README.md` — the second is where the
   owner's phase-B verdict will arrive. It held **0 unconsumed records** on
   2026-09-04. *Snapshot of 2026-09-04 — re-read it, that is the point.*

`docs/research/2026-09-04-long-form-idle-research.md` is the comparator
evidence behind the family portfolio; read it before proposing a family that
is not in it.

DECIDED (do not re-litigate)

- **Keepsakes are the answer to the measured defect**, not minigames: one
  permanent object per chapter, ten effect shapes, six couch places. Chosen
  because it attacks *every chapter* rather than every prestige, needs no new
  currency, cannot touch the Clarity rails, and makes prestige feel like
  continuing rather than restarting.
- **Four to six reusable mechanic families, not 18 bespoke systems** — the
  matrix in the plan § 4 is the contract.
- **Content stays typed and derivation stays pure**: `content.ts` tables →
  `engine.ts` formulas → `actions.ts` mutations → store/save → components.
  The simulator consumes the same action layer. No second simulator, no
  per-stage conditionals, no ad-hoc save fields.
- **Save is v3.** Migration gates the couch fields on `fromVersion >= 3` and
  validates capacity incrementally.
- **Auto-arrange uses `arrangeModeFor`**, not a blanket fill: `fresh-only`
  when the arrangement should not be topped back up. This exists because a
  blanket fill made it impossible to take a keepsake *off* — the next 50 ms
  tick refilled the place.
- **IAP mockups only**, compile-time flagged out of production, seven states,
  prices and product IDs clearly mock. Owner-gated to activate.

REJECTED, AND WHY

- **18 distinct minigames** — the brief's own target was ~4–6 reusable
  families; 18 systems is 18 balance surfaces and 18 idle-safety proofs.
- **`work-nugs` at chapter 2** — measured to break § 9.6 rail 5a widely
  (idle-only felt-upgrade fell to 0.3 %). Moved to chapter 5 and pinned by
  test. **Do not move it back without re-running the rails.**
- **A blanket `fill` auto-arrange** — fixed rail 5a's first break and broke it
  further (idle-only 0.0 %) while also making unequipping impossible.
  `arrangeModeFor` is the shape that survived.
- **An outright Clarity spend for phase C's Morning Routine** — § 9.6 rail 6
  requires banked Clarity to grow **strictly every cycle**, which an
  expenditure breaks as written. Quoted from the plan: *"Allocation, not
  expenditure."* A spend needs new evidence and a rail change, argued
  explicitly, not assumed.
- **A dedicated `added-card-lane` doc route in fleet-manager** — measured not
  to fire (the hook delivers a bounded set per write and existing routes claim
  the slot). Folded into `card-status-write` instead.

OPEN

- **Phase B — does arranging the couch actually feel interesting?** Owner-only.
  Simulation proved it fair, reachable and idle-safe; it cannot prove it is
  interesting. **B gates C and D.** Where his answer lands:
  `docs/owner-comments/couch-legend/`, or straight into the chat.
- **Phase C's shape** — F2 Morning Routine as *allocation* of banked Clarity.
  Undecided in detail; the rail-6 constraint above is the boundary. Do not
  design it past a sketch until B is answered, because a "no" on arranging
  changes what C should be.
- **The one rail breach** — sub-2 % felt-upgrade in 1 of 27 runs. Settled by
  either a tuning change that survives all 27 runs, or an argued decision that
  the bound is wrong. Not by silence.
- **15 of 18 chapters have no scene art.** Phase E, art lane, owner QA at the
  end — but prompt-writing and generation are **not** gated on B.

YOUR FIRST STEP

Do not trust the state above. In couch-legend, from a clean `main`:

    git fetch origin main && git log --oneline -1 origin/main   # expect 4934955 or later
    pnpm install
    pnpm exec tsx tools/stage-evolution.ts                       # expect 14/18 · 3/18 · 17/18

Then read `docs/owner-comments/couch-legend/README.md` in fleet-manager. Its
Unconsumed count is the branch point:

- **Non-zero, and it answers phase B** → open the record, act on it, and
  `python3 tools/owner_comments.py consume couch-legend <id> --actor <card>
  --evidence <PR>` when done. B answered means C or D is live.
- **Zero** → B has not arrived. Say so to the owner in one line and ask him
  for it — then **keep working** on the ungated lanes: the scene packages
  (phase E, via the `image-prompt` skill) and the one rail breach. Do not
  stop; do not start C on a guess.

DONE WHEN

Whichever lane you take, the same bar:

- `pnpm check` passes (`tsc --noEmit` + `vitest run` + `vite build` +
  the store-preview assertion).
- Anything economy-touching went through `pnpm sim` and its numbers are in
  `docs/sim/`, with the archetypes the brief names: balanced, mostly idle,
  active/check-in heavy, prestige-averse, optimization-heavy.
- `python3 bootstrap.py check --strict --added-card <your card>` exits 0 —
  **with the `--added-card` flag.** Without it you are running a different
  query than CI does.
- Behaviour verified against the production bundle, not just compilation:
  `node tools/smoke-couch.mjs`.
- Born-red card first, PR ready immediately, flip the card complete last,
  drive the PR to green yourself.

OUT OF SCOPE

- Real money in any form: no billing SDK, no Play/App Store product creation,
  no receipt verification, no backend purchase service, no store-console
  action, no credential use. Mockups only. Owner-gated.
- Android device claims. No container in this estate has an SDK, emulator or
  device. Chromium is not an Android WebView and must never be reported as one.
- Rewriting phase A. It is merged and reviewed (25 findings across 3 Codex
  rounds plus an independent Gemini pass, all conceded). Fix what you can
  prove is wrong; do not re-do what is only unfamiliar.
- The identity constraints, which are not negotiable: click always satisfying,
  numbers serve mood, away time respected, no fail state, no energy system, no
  attendance punishment, no streak or FOMO mechanics, warm deadpan literary
  humour, the couch as continuity object, stages permanent and moods
  per-afternoon.

LESSONS FROM THIS SESSION

- **A Codex review comment's `commit_id` is not its round.** GitHub re-anchors
  unresolved comments to the newest commit touching the file — 6 of 11 round-1
  comments reported the round-2 head. `original_commit_id` is stable; filter on
  that. Recorded in fleet-manager `docs/CAPABILITIES.md`.
- **`bootstrap.py check --strict` and CI's `substrate-gate` are different
  queries.** Local exited 0 on a tree CI failed. Several checkers only fire on
  the *added* card. Always pass `--added-card`. Recorded as TRAP-010.
- **A test that passes is not proof the edit landed.** One fix silently failed
  to apply (a string-replace anchor stopped matching) and a commit message
  claimed a fix the code did not contain; Codex round 3 caught it, my own test
  was too weak to. Re-read the diff, not the intent.

CLOSE WITH

The `session-close` skill in whichever repo holds your card — run
`python3 bootstrap.py check --strict --added-card <card>` and read its **real**
exit code (never `$?` after a pipe). Update the plan's § 8 phase table if you
moved a phase, `docs/current-state.md` in fleet-manager if estate-level truth
changed, and record any newly verified capability in `docs/CAPABILITIES.md` —
never a limitation. Drive your PR to a terminal state before you stop.
```
