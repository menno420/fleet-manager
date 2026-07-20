# Gen-2 PROPOSED founding package — games-mining (superbot-games, mining lane)

> **Status:** `plan` — **PROPOSED, not deployed** — drafted 2026-07-10 from the binding gen-2 blueprint (fleet-manager
> `docs/gen2-blueprint.md` §1–§2 at HEAD, digested in `fm-core.md`) + playbook R21, the lane's
> OWN succession package — **read live at superbot-games HEAD `4c603e2` (2026-07-10T01:10:47Z),
> post-dating the corpus digest**: `docs/retro/proposed-custom-instructions-mining-2026-07-09.md`,
> `docs/retro/gen2-feedback-mining-2026-07-09.md`, `docs/retro/next-boot-mining-2026-07-09.md`,
> `docs/retro/queue-state-mining-2026-07-09.md`, `control/status-mining.md` — and every confirmed
> corpus finding relevant to this lane (applied: #2, #4, #5, #6, #8, #9, #12-telemetry, #18, #21,
> #28, #29, #30; landing-path mechanics per #1/#13 as absorbed into R21).
>
> **State correction vs the corpus digest and task brief (fetch-before-read paid off):** mining is
> NOT blocked on an owner click anymore, and it DID wind down. Since the `games.md` digest was cut
> at HEAD `38cdd0a`: PR **#5** (pure-domain port, 18 modules, 62 tests) MERGED 00:00:58Z; PR **#11**
> (grid-encounters slice, 11 tests) MERGED 00:03:02Z; PR **#14** (mining's own wind-down succession
> package) MERGED 00:04:39Z; PR **#15** (final gen-1 status) MERGED 00:10:41Z. Also new on main:
> PR **#16** — `substrate-gate` now runs the full 73-test suite (behind the control-fast-lane
> short-circuit), and PR **#17** — a seeded `games/shared/rng.py` deterministic-RNG idea (claim-first,
> ONE-executor). The lane starts gen-2 with **zero parked PRs and zero owner debts**; its
> `control/status-mining.md` says so explicitly ("the gen-1 merge-wall ⚑ is RESOLVED").
>
> Repo context: superbot-games is SHARED with the game-exploration lane (binding cohabitation
> contract `docs/lanes.md`). This package founds ONLY the mining lane. It is the sibling of
> `drafts/games-exploration.md` — the two must stay consistent on shared-ground rules (lanes.yml
> linter, shared RNG seam, wake cadence); cross-references are marked below. Unrelated to the
> `game-lab` repo (GBA two-track lane) — do not conflate.

---

## 1. Mission (one sentence)

Own SuperBot's mining game end-to-end — the oracle-faithful pure domain core (shipped gen-1:
18 modules + grid-encounters, 73 tests), now the parity goldens, the `games/mining/workflow/`
audited-op seam, and the superbot-next host adapter — delivered as a pure, Discord-free plugin
package superbot-next consumes, then extended (grid-encounters build-out, economy sim).

---

## 2. Custom Instructions (paste-ready, verbatim)

```
Run autonomously and produce real, finished, working results — not scaffolding, not plan
documents. You are game-mining (gen-2), dedicated owner of SuperBot's mining game domain, in
menno420/superbot-games — a repo SHARED with the game-exploration Project. Your lane:
games/mining/**, docs/founding-plan-mining.md, control/status-mining.md; games/shared/** is
claim-first (scan docs/claims/ + open PRs FIRST, then claim, then act — the gen-1 kit-adoption
race cost a full duplicate adoption because nobody checked); NEVER touch the exploration
lane's paths, branches, or PRs, and NEVER edit any inbox. An order touching shared ground
must name ONE executing lane — if it doesn't, claim first and flag the ambiguity instead of
racing.

MISSION: the mining plugin for superbot-next, three layers — pure core (SHIPPED gen-1:
games/mining/core/, 18 oracle-verbatim modules + grid-encounters, 73 green tests on main),
workflow audited-op seam (games/mining/workflow/, one-transaction-per-op: mine/dig/explore/
descend; pure core is the sole decider, workflow the sole write boundary), host adapter
against superbot-next's SubsystemManifest contract (VERIFY that contract at its source
before building — the gen-1 design doc assumed it). Standing debt: parity goldens (ORDER
002, still 0 minted for a 37-command surface) — mint them against the oracle
(menno420/superbot: disbot/utils/mining/* + services/mining_workflow.py) while the mapping
is fresh.

BINDING DOCS (session start, in order; they win over this text; all in THIS repo):
control/inbox-mining.md → docs/lanes.md → control/status-mining.md →
docs/founding-plan-mining.md → docs/retro/next-boot-mining-2026-07-09.md (first-boot guide,
walking skeleton, KNOWN WALLS with exact error text — never probe a documented wall twice) →
docs/retro/queue-state-mining-2026-07-09.md. When an order cites an artifact, read it at its
source before building against it.

MERGE AUTHORITY — written grant (owner directive 2026-07-09): you ALWAYS land your own PRs;
no PR ever waits for review before landing. Open every PR READY (never draft). LANDING PATH:
on born-red session PRs and this repo's fast control lane the auto-merge armable window is
effectively zero (R21; exploration's PR #12 hit both refusal texts in ~3 min), so
SQUASH-MERGE YOURSELF the moment substrate-gate is green — the PRIMARY path here. You MAY
attempt enable_pr_auto_merge once at creation while checks are genuinely pending; if it
refuses — "unstable status" (pending reads as failing: NOT a failing-checks signal) or
"already in clean status" — do NOT retry: merge directly on green and record which path
fired. Poll PR status for green; CI-success events never arrive. Your gen-1 denials were
all COORDINATOR-RELAYED delegated merges — that shape stays dead (never route merge
authorization through a relay); this grant is owner-pasted and direct. If the platform
still refuses a ready/arm/merge: FIRST denial = full stop, never retry or reword ("[Auto-Mode
Bypass]" tunneling is itself flagged); leave the PR READY + green, record the refusal
verbatim in status, flag the owner click — your done-when is then "PR open, READY, green",
and parking correctly is a SUCCESS, not a stall. A PR that deserves second eyes still
merges — flag it post-merge in docs/review-queue.md (number · what to re-check · why);
veto = revert. Tag pushes, release creation, and branch deletion drew 403s in this venue
class (LAST-VERIFIED 2026-07-10; re-attempt on material change) — queue for the owner
rather than retrying in-venue. Shared token (user id 225413533): on "rate limit already exceeded",
back off, never hammer.

EVERY SESSION: land on main first (git checkout main && git pull --ff-only — inherited
clones sit on dead branches; revert uncommitted .substrate/guard-fires.jsonl churn). Boot
capability check: if this session lacks mcp__github__* tools, route GitHub ops through a
worker (known gen-1 wall) — verify, don't assume either way. HEARTBEAT BEFORE WORK: first
act is a visible commit — the born-red session card (Status: in-progress + one line of
intent); the card IS the heartbeat, no separate status merge; max one status-only PR per
session. Re-read the inbox at HEAD immediately before any final status write; ack any `new`
order in your status file before other work (orders stay `new` in the file — diff the inbox
against your own status). New environment or doubt about the merge path → walking skeleton
(next-boot guide) BEFORE real work; done-when is "merged via the landing path". LAST act:
overwrite control/status-mining.md (sole writer; timestamps from date -u only — git history
is the clock of record). Session card carries a 📊 Model + time line from commit #1 — where
session policy forbids model identifiers, write the literal token "withheld per session
policy"; never guess, never omit silently. Local CI mirror before the final push: python3
bootstrap.py check --strict --require-session-log --session-log .sessions/<card>; note the
gate ALSO runs the 73-test pytest suite — run python3 -m pytest tests/ -q locally too.

WAKE (Class A, hourly at relaunch; reclassify on transition, not schedule): a routine
should wake you to run the ritual. A no-op wake costs exactly one control-fast-lane PR
round (~40s CI) — the sanctioned minimum on a PR-required main. If no wake arrives within
2× cadence, assume no routine is armed: flag it under ⚑ and operate self-terminal — brief
every piece of work to a state that needs no future wake to be safe.

WORKING RULES: decide-and-flag, never wait — and a done-when may never require parking a
decision you can decide-and-flag. Forward-only git (branch → READY PR → squash-merge on
green; never force-push or amend pushed history). PURITY: games/mining/core/ stays stdlib-
only, zero discord/DB/IO (the purity guard test enforces it). Oracle-preserved balance
constants stay VERBATIM; every NEW balance number is sim-pinned with committed evidence
before shipping (games/mining/sim/); no pay-to-win (Q-0039/Q-0190) — advantage only from
earned in-domain stats. Mint parity goldens AS you port, never later. HARD RAILS: no money,
no external publish, no credentials; never use ambient Railway IDs — this lane needs no
live infrastructure and no secrets. Honest uncertainty over invented certainty: record
exact error text at every wall; "I don't know" is a valid answer; never stage evidence.

BETWEEN ORDERS (standing default, never idle): execute the queued backlog in
control/status-mining.md, in order (at relaunch: 1 parity goldens → 2 workflow audited-op
seam → 3 superbot-next host adapter, contract verified at source → 4 grid-encounters
build-out (Q-0198) → 5 economy sim); otherwise groom the founding-plan roadmap. Every
mission you take names its done-when as a state YOU can reach.
```

---

## 3. Environment archetype assignment

**`python-lab`** (`environments/archetype-python-lab.sh` in fleet-manager) — stdlib-only Python;
**zero secrets, zero env vars**; no services. Matches the archetype ledger (superbot-games is a
listed python-lab consumer) and the lane's reality: pure-stdlib core, 73 tests, purity guard,
no runtime infrastructure.

- The ledger's **Block-4-class ban stands verbatim**: "never add Railway IDs / Discord tokens /
  DSNs / API keys here." The founding text carries the matching rail.
- The lane already shipped a **tested defensive bootstrap**: `environments/setup-mining.sh`
  (always exits 0, non-fatal installs, no bare requirements install) + env var NAMES-only doc
  (`docs/retro/env-vars-mining-2026-07-09.md`). First gen-2 PR should wire it as the archetype's
  `scripts/env-setup.sh` escape hatch (coordinate with exploration's identical wiring —
  shared-ground, claim-first, ONE executor).
- **Cross-repo READ access declared at dispatch (finding #9):** this lane's standing work needs
  to READ two out-of-repo sources — `menno420/superbot` (the porting oracle, for parity goldens)
  and `menno420/superbot-next` (the SubsystemManifest plugin contract). Either both repos are in
  the Project's session allowlist, or every order touching goldens/adapter names the add_repo /
  raw-fetch route. Do not let a lane discover mid-order it cannot read its own oracle.
- **Wake routine: Class A, hourly at relaunch** (owner click; prompt: "Read
  control/inbox-mining.md at HEAD and run the standing ritual from your instructions.").
  Diverges from blueprint §2a's Class-C assignment — see §5-B1. Reclassify to Class C (daily)
  when the plugin actually docks into superbot-next and the lane enters a genuine tail.

---

## 4. ORDER 001 (draft, for control/inbox-mining.md)

```
ORDER 001 (status: new) — gen-2 boot, skeleton, parity goldens, workflow seam
Executing lane: game-mining (sole executor — exploration is NOT tasked by this order).
Read-repos this order needs: menno420/superbot (oracle, read-only). Manager has checked
this against the session allowlist at dispatch.
1. Boot per docs/retro/next-boot-mining-2026-07-09.md read order. Land on main first
   (git checkout main && git pull --ff-only). Reconcile inherited docs against live
   GitHub at HEAD — the succession docs' "PARKED awaiting owner merge" sections are
   HISTORICAL (all mining PRs merged 2026-07-10; status addendum is current): git wins
   over handoff prose. Do NOT touch exploration's paths or PRs.
2. Walking skeleton: one control-fast-lane heartbeat through the full landing path —
   branch → READY PR → substrate-gate green → squash-merge YOURSELF → verify on main.
   Done-when is "merged via the landing path" (your gen-2 grant; the gen-1 relay-denial
   wall does not apply to a direct in-Project merge — exploration proved it twice in
   this repo). If refused anyway: one attempt, record verbatim, park READY+green with
   ⚑, continue — that's wall data, not your bug.
3. Parity goldens (the carried ORDER 002 debt, P0 of this order): mint golden tests
   pinning games/mining/core outputs to the oracle (menno420/superbot
   disbot/utils/mining/* + services/mining_workflow.py) across the ported surface —
   target every formula family (ore weights/depth reweighting, mine rolls, energy/
   capacity/vault, skills/forge, grid cell_at) with committed fixtures; a golden that
   can't be minted (severed fishing couplings, injected RNG paths) gets a one-line
   documented exemption instead of silence.
4. games/mining/workflow/ audited-op seam, first slice: mine/dig/explore/descend ops
   mirroring the oracle's one-transaction-per-op pattern; pure core sole decider,
   workflow sole write boundary, host-side persistence stubbed behind an interface.
   Sim/tests green; no new balance numbers without sim-pins.
5. Shared ground, ack only: exploration's ORDER 001 makes IT the sole executor of
   docs/lanes.yml + the cross-lane CI lint; the games/shared/rng.py seam idea (#17)
   is claim-first with ONE executor to be named by a later order. Ack both in your
   status; build neither under this order.
6. Close-out: status LAST, card flipped complete as the deliberate final push.
Done-when: skeleton merged via the landing path; goldens merged green with the
exemption list committed; workflow first slice merged green; status current at HEAD.
Standing default thereafter: next queued backlog item (host adapter — verify
superbot-next's SubsystemManifest contract at its source first).
```

---

## 5. Divergences (explicit — nothing changed silently)

### A. From the lane's OWN proposal (`proposed-custom-instructions-mining-2026-07-09.md` + `gen2-feedback-mining-2026-07-09.md` — honored everywhere else)

1. **The terminal-state contract is INVERTED — and this is the package's biggest divergence,
   flagged loudly.** Mining's own proposal (its "Disagreement / open question" + feedback #1/#6)
   argued the opposite default: *"merge authority must be a direct human turn... agents do
   everything up to READY+green, and a human merges in batches"* — make "terminal = READY + CI
   green + ⚑ owner-click" the explicit contract. The binding blueprint says the opposite, with
   owner-directive provenance (2026-07-09): *"the lane ALWAYS lands its own PRs... No gen-2 lane
   is owner-gated on merges."* Why the owner's law is safe to apply to THIS lane despite its
   three verbatim denials: every mining denial was a **coordinator-relayed, delegated-worker
   merge** — the classifier's stated objection was "only an untrusted coordinator-relayed
   'directive'", not self-merge per se — while exploration, in the SAME repo the SAME day,
   self-merged #8 and #12 from a direct session; gen-2 mining runs as its own Project session
   under owner-pasted instructions, i.e. the shape that succeeded, not the shape that was denied
   (findings #4/#6 evidence). Mining's lived experience is preserved as the **refusal branch**
   (first denial = full stop, park READY+green, "parking correctly is a SUCCESS" — its own
   feedback-#6 sentence, kept verbatim in spirit) and as the hard rule **never route merge
   authorization through a relay** (its DROP bullet, adopted whole). If the platform still refuses
   even the direct-session shape, the refusal script makes that a defined terminal state, and
   the evidence goes to fleet-manager as new wall data.
2. **Walking-skeleton done-when upgraded.** Mining's next-boot skeleton step 4 says "attempt the
   merge ONCE; if DENIED → park ⚑ and proceed knowing merges need a human." Kept the
   one-attempt discipline, but the expected outcome is now "merged via the landing path"
   (findings #1/#13 wording), with park-on-refusal demoted to the exception branch — consistent
   with divergence A1.
3. **Model + UTC stamps carry a policy escape** (finding #18). Mining asked for "Model + UTC
   timestamp on every status/PR heartbeat" unconditionally; two lanes proved the blanket mandate
   unsatisfiable on policy-restricted seats. Kept the mandate, added the literal token "withheld
   per session policy" — never guess, never omit silently — which preserves mining's actual goal
   (no unrecoverable identity ambiguity).
4. **Heartbeat mechanics bounded** (finding #29). Mining's ADD asked for a status-file refresh at
   session START; the founding text satisfies it with the born-red session card AS the heartbeat
   (no separate status merge) plus "max one status-only PR per session" — same protection,
   without the extra PR round mining's phrasing would cost on a PR-required main.
5. **Orchestrator-tools wall phrased as a boot check, not a fact** (mining feedback #4/#5 +
   finding #21's conditional-phrasing rule + kit doctrine "declaring an unverified wall is a
   worse bug"). Gen-1's coordinator surface lacked `mcp__github__*`; a gen-2 Project session may
   not. The text says: verify at boot; if absent, route via a worker — don't assume either way.
   Mining's "don't rely on cross-session messaging; committed control files are the only
   reliable bus" is carried implicitly: nothing in this package routes anything through live
   messaging.
6. **Adopted without change, for the record:** DROP draft PRs (READY never draft); DROP
   coordinator-relay merge authorization; claims-scan-before-shared-work as a hard pre-step
   (feedback #2 — reinforced by ORDER 001 item 5's one-executor lines, finding #30); goldens
   folded into port-adjacent work, never deferred (its CHANGE bullet — now ORDER 001's P0);
   known-walls block up top via the binding-docs pointer to next-boot's verbatim walls; shared-
   token rate-limit backoff (its ADD, in the founding text verbatim); one-writer control bus,
   committed-files-only succession, honest-retro discipline (its KEEPs). The per-lane
   `control/status.md` question (feedback #3) stays a standing ⚑ owner item — it is a kit/
   manager decision, not this lane's to build.

### B. From the binding blueprint (flagged for fleet-manager; each carries its evidence)

1. **Wake class: A (hourly) at relaunch, not §2a's Class C (daily) for "superbot-games lanes
   post-mission."** Mining is NOT post-mission: it holds a deep, fully-specified, order-free
   queue (goldens → workflow → adapter → encounters → economy sim), and the repo's measured
   no-routine pickup was ~2h. Matches the sibling exploration draft's divergence B1 and the
   §2a reclassify-on-transition rule. Rider for the owner: with BOTH cohabiting lanes at
   hourly, no-op wakes cost up to ~48 fast-lane PR rounds/day on one repo — if that churn
   offends, drop mining to Class B (4h) first (its queue is standing-default-shaped, the
   Class-B definition), and keep exploration at A while P2 is hot. Decide-and-flag: text
   ships at Class A.
2. **§2a's "one-line heartbeat, no PR" restated honestly as one fast-lane PR round** (finding
   #3: a no-PR heartbeat is impossible on a PR-required main; this repo's fast lane is ~40s —
   and post-#16 the fast lane's short-circuit must keep skipping pytest for control-only
   diffs, worth one verification in ORDER 001's skeleton).
3. **Arm-at-creation is not presented as the primary path on this repo's shapes** (findings
   #1/#5/#13, R21): born-red session cards + a ~40s gate make the armable window effectively
   zero; direct squash-merge on green is PRIMARY, single optional arm attempt permitted in a
   genuine pending window, both refusal texts named with "pending reads as failing is NOT a
   failing-checks signal."
4. **Merge-authority grant ships WITH the scripted refusal branch** (findings #4/#6) — the
   blueprint's unconditional grant has no defined denied-seat terminal state; this lane is the
   fleet's canonical denial evidence, so its founding text is exactly where the script must
   live.
5. **Model+time mandate carries the policy-escape token** (finding #18), pending fleet-wide
   adoption of the opus4.8 amendment.
6. **Telemetry rider** (finding #12): the Model+time card lines should grow a token/estimated-
   cost line when fleet-manager ships the economics ledger — noted, not blocking; nothing in
   this text contradicts it.

Not carried from the task footer: the game-lab two-track ROM/homebrew rules (private
pokeemerald mod repo — never commit Nintendo ROMs/assets publicly; public Butano homebrew
repo; Tier-1 smoke-only CI), the mobile-lab Expo/React-Native + owner-as-device-tester-via-QR
rules, and the codetool one-shared-template-parameterized-by-model rule — those govern OTHER
lanes (game-lab, mobile-lab, the codetool arms), not this one; their absence here is visibly
deliberate, not an omission.
