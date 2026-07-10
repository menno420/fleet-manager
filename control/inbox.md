# fleet-manager · inbox

ORDERS to the manager. ONE writer: the owner. The manager reads this at session start
and reports progress in control/status.md.

> Amended 2026-07-10 (round-3 brief §1 + superbot `docs/eap/eap-program-review-2026-07-10.md`
> §5.1): the manager ALSO appends doctrine-amendment ORDERs to itself here — the
> manager-repo inbox is manager-side. Every amendment gets an ORDER + a **named
> next-session owner** + a done-when; never a dangling "some future session".
> Orders below were seeded from the six STANDING DEBTS in superbot
> `docs/planning/round3-launch-pack-2026-07-10.md` §1.

## ORDER 001 · 2026-07-10T12:05Z · status: DONE (executed by the 18:31Z standing-wake pass 2026-07-10, fleet-manager PR #33)
priority: P1
owner: next fleet-manager doctrine session (the first manager wake after this lands)
do: Apply the blueprint amendment proposals **P1–P11** (`docs/findings/fable5-review-2026-07-09.md`
§ blueprint amendments) to `docs/gen2-blueprint.md`, and apply drift fixes **D4/D5/D6**
(incl. the wind-down marker carve-out). REWRITE `init-prompt-universal.md` (the universal
wake-up prompt in `docs/prompts/` — locate at HEAD): remove the false routine promise and
replace it with the **verified routine recipe** (claude-code-remote `create_trigger` /
`send_later` family, seat-dependent — `docs/capabilities.md` CAN entry). Write the manager's
own **MISSION.md** with a done-when (program-review §5.10: the manager holds lanes to
delta-8 but has no mission/done-when of its own).
why: proposals don't get applied is the EAP's biggest process hole (program-review §5.1);
the binding blueprint still contains sentences three HIGH findings falsified; venture-lab
launched on the uncorrected text and hit the exact predicted merge wall twice.
done-when: blueprint changelog records P1–P11 + D4/D5/D6 with provenance; the universal
init prompt contains the verified recipe and no false routine promise; MISSION.md on main
with an explicit done-when line.
✅ DONE: **P1–P11 applied** to `docs/gen2-blueprint.md` with a provenance changelog entry
(finding IDs + landing spots + today-corrections named: P6's "no scheduler primitive"
premise narrowed — self-arm WORKS, the `create_trigger`/`send_later` family is the
verified seat-dependent primitive; P8 additionally bound by the Q-0262 family-level
model-name policy). **D4** applied (`docs/prompts/gen1-winddown-universal.md` — marker
carve-out for merge-blocked lanes + stale "Deployed: not yet" drift fixed). **D5/init
prompt REWRITTEN** (`docs/prompts/init-prompt-universal.md` — dated successor text: false
routine promise removed; verified recipe in: `create_trigger` with cron + prompt +
persistent_session_id (cse_/session_ accepted) OR create_new_session_on_fire=true,
verbatim call+outcome in status, `list_triggers` verify, F-1 rebind-then-`delete_trigger`
cutover, seat-dependent fallback ⚑). **D6/MISSION.md** on main (repo root) with the
explicit done-when line (standing core runs a full week: zero stuck PRs, zero DARK/DEAD
lanes, owner-queue grew only owner-only — then renew or re-scope). This PR: fleet-manager
**PR #33**.

## ORDER 002 · 2026-07-10T12:05Z · status: DONE (executed by the 16:31Z standing-wake pass 2026-07-10, superbot PR #1954 + fleet-manager PR #32)
priority: P1
owner: next fleet-manager rollup/staleness-sweep session
do: Re-stamp superbot `docs/eap/fleet-manifest.md` to post-launch reality (**all rows** —
venture-lab's row still says "Project boot pending owner clicks" while the lane shipped two
products; most rows still carry executed "▶ tonight" plans). Then propose the roster's move
to **generated-from-heartbeats** (program-review §6.2 — one generated roster derived from
`control/status*.md`, owned by fleet-manager) so this staleness class dies structurally.
why: overnight-review finding 1 — the manager's sole-writer file is frozen at the 07-09
pre-launch state; `check_manifest_freshness.py` (superbot #1923) already flags it.
done-when: every manifest row reflects post-launch reality and the freshness checker is
green; a generated-roster proposal is filed (`docs/proposals/`) and routed to the owner-queue
or an ORDER.
✅ DONE: superbot `docs/eap/fleet-manifest.md` fully re-stamped to verified post-launch
reality (superbot **PR #1954** — every row rewritten from launch-readiness + live
`list_triggers` + per-repo `control/status.md` fetch; missing rows added: pokemon-mod-lab,
gba-homebrew, games-plugins merged lane, mobile-lab; trading-lab renamed trading-strategy;
executed "▶ tonight" plans removed); `check_manifest_freshness.py --strict` = **13/13 FRESH,
0 stale**. Generated-roster proposal filed at
`docs/proposals/generated-roster-from-heartbeats.md` and routed as **ORDER 009** below
(agent-doable, not owner-only — owner-queue deliberately untouched). This PR: fleet-manager
**PR #32**.

## ORDER 003 · 2026-07-10T12:05Z · status: new
priority: P1
owner: next fleet-manager doctrine session (may ride with ORDER 001)
do: Review-queue enforcement — adopt an **auto-append rule** (any PR > N lines of runtime
code, or any self-flagged risk, MUST get a `review-queue.md` row; pick and document N) into
the blueprint + `docs/review-queue.md`, and **name a standing drainer** (which session class
drains the queue, at what cadence). Backfill rows for the highest-risk overnight PRs as the
first drain pass.
why: 116 merged PRs / zero rows in any review queue is the current state; that voids the
post-merge-review law the no-pre-merge-review policy rests on (program-review §5.2 — the
queue was the safety valve that justified "no pre-merge review").
done-when: the rule is binding in `review-queue.md` + blueprint; a drainer is named with a
cadence; the first drain pass is logged with at least the highest-risk overnight PRs rowed.

## ORDER 004 · 2026-07-10T12:05Z · status: DONE (executed by the wake-slice session 2026-07-10, fleet-manager PR #27)
priority: P0 (deadline — the free window closes 2026-07-14)
owner: next fleet-manager session of ANY kind (deadline jumps the queue)
do: Build the **fleet economics ledger** BEFORE 2026-07-14: per-lane session/run counts and
whatever cost signal is visible (commit counts, CI minutes, PR counts, routine runs — record
"not measurable" honestly where nothing is visible). Land as
`docs/findings/fleet-economics-2026-07.md` (or similar) with a per-lane table.
why: the free window closes 2026-07-14 with zero cost data collected; the §2a cadence table
was built on zero cost data (program-review §8 names this the time-critical unbuilt idea).
done-when: ledger on main before 2026-07-14 with per-lane counts + a cost-signal column,
honest nulls included; owner-queue/status point at it.
✅ DONE: `docs/findings/fleet-economics-2026-07.md` landed (fleet-manager PR #27, wake-slice
session 2026-07-10T14:44Z) — per-lane table across all 13 repos (merged PRs window+all-time,
default-branch commits, session cards, total Actions runs as the CI-minutes proxy, routine
state), honest nulls for CI-minutes/token/$ (not agent-visible — recorded "not measurable",
never invented), top-3 heaviest lanes + cadence-vs-activity outliers; findings README indexed.
`control/status.md` deliberately untouched by this PR — the owner-queue/status pointer rides
the coordinator's next heartbeat.

## ORDER 005 · 2026-07-10T12:05Z · status: DONE (executed in the PR that filed it)
priority: P1
owner: round-3 brief §1 task-1 session (this one) — DONE
do: Fix the ping-test report's known-false websites "NO ACK" row (two ⚑ flags old).
why: the manager's own report carried a false negative about a sibling lane; websites
actually acked ORDER 006 at +1h39m landed→ack via websites PR #44 (merged
2026-07-09T19:35:59Z).
done-when: the row in `docs/findings/ping-test-2026-07-09.md` is corrected with evidence.
✅ DONE: `docs/findings/ping-test-2026-07-09.md` websites row corrected + "§ Correction
(2026-07-10)" section added (ack rate 2/9-at-sweep → 3/9 final); blueprint §2a ack count
annotated. Same PR as this order (fleet-manager PR #20).

## ORDER 006 · 2026-07-10T12:05Z · status: DONE (executed in the PR that filed it + codetool-lab-fable5 PR)
priority: P1
owner: round-3 brief §1 task-1 session (this one) — DONE
do: Correct the codetool release-wall contradiction — opus4.8 PROVED the Actions
`workflow_dispatch` release route works (2 live releases: v0.1.0 published
2026-07-09T16:56:21Z, v0.2.0 17:57:53Z, both by github-actions[bot]) while
codetool-lab-fable5's succession doc records the same route as closed ("Route closed.
Releases are owner-manual"). Reconcile before any gen-3 lane inherits the wrong lesson.
Also fold the model-comparison **seat-contamination caveat** (overnight-review finding 6:
coordinator + wind-down seats ran claude-fable-5 in at least the sonnet5 and likely fable5
lanes — cross-arm comparisons must score builder seats only) into the experiment records.
why: a gen-3 fable5 successor inheriting "do not re-attempt" would skip a proven release
path; uncaveated comparison data misattributes seat effects to model tiers.
done-when: fable5's `docs/succession/PLATFORM-LIMITS.md` item 4 corrected citing the
opus4.8 evidence; seat-contamination caveat present in fleet-manager `docs/experiments/`.
✅ DONE: seat-contamination caveat folded into `docs/experiments/README.md` (§ Standing
caveats) + `docs/experiments/harness-x-model-2026-07-09.md` (judge-note append) in this PR
(fleet-manager PR #20); fable5 succession doc corrected in **codetool-lab-fable5 PR #14**
(MERGED, squash a6cf1a9 — `docs/succession/PLATFORM-LIMITS.md` item 4 + item 8 rider).

## ORDER 007 · 2026-07-10T13:43Z · status: new
priority: P1
owner: next fleet-manager doctrine session (may ride with ORDER 001/003)
do: Mint the @codex review-relay playbook rule (owner directive Q-0258, 2026-07-10): any
lane session with a review-worthy-but-not-owner-only question posts it as a PR comment
mentioning @codex (one specific question, on the final head; template in superbot
docs/planning/codex-review-integration-plan-2026-06-17.md Part C) instead of parking it
in the owner-queue. Codex is the named standing drainer of the post-merge review
convention; Q-0120 governs the return path (verify, never obey). Fold the rule into the
blueprint/playbook where lane doctrine lives.
why: round-3 brief §1 standing debt 6 — the only one of the seven brief debts that never
got an inbox ORDER (001–006 cover debts 1–5 and 7); the owner is enabling the Codex
GitHub integration across the valuable repos and rates its PR reviews highly (Q-0259
ruling 3 extends this to standing @codex review on substantive superbot-next PRs).
done-when: the rule is written into the lane playbook/blueprint with the Part C template
pointer; ORDER status flipped to done with the landing PR cited.

## ORDER 008 · 2026-07-10T15:33Z · status: DONE (executed by the 18:31Z standing-wake pass 2026-07-10, fleet-manager PR #33)
priority: P1
do: OWNER RULINGS BATCH (owner delegation Q-0262, superbot router, 2026-07-10; routed by
the owner's dispatch session — the lane-inbox halves [kit F-5=Reading A · trading holdout
unlock · superbot-next flag-13 accepted] are routed directly as kit ORDER 011 / trading
ORDER 008 / superbot-next ORDER 009; verify at their HEADs). Fold the fleet-policy half
into doctrine + relay at next lane contact: (1) MODEL-LINE POLICY: family-level model
names ONLY, everywhere (fable-5, opus-4.8; exact IDs never) — un-nulls trading's model
rows. (2) OWNER-ACTION GRAMMAR: the kit's field set wins by definition; venture-lab
conforms at its next kit upgrade. (3) The 8 undeployed instruction packages STAY
undeployed until your gen-3 blueprint delta lands (re-base, then deploy in one sitting).
(4) Roster note: core seat 6 (Q-0261) = the superbot hub Project — owner may veto.
(5) Pokemon concept pick = QoL+ (Q-0262.7), effective when the games program boots
post-core.
why: Q-0262 applied the round-3 recommended answers wholesale; these five are the
fleet-policy half that lives in your doctrine.
done-when: policies folded into their blueprint/playbook homes + launch-readiness rows
ticked where these close items; status acks 008.
✅ DONE: all five fleet policies folded into their doctrine homes (fleet-manager PR #33):
(1) model-line policy → blueprint §1 Model-line item (family-level ONLY, exact IDs never;
merged with amendment P8's "withheld per session policy" token); (2) OWNER-ACTION grammar
→ playbook R17 rider (kit's field set wins by definition; venture-lab conforms at next
kit upgrade); (3) instruction-package hold → blueprint §4 (stay undeployed until the
gen-3 blueprint delta, then re-base + deploy in one sitting); (4) core seat 6 = superbot
hub → owner-queue item 10 RESOLVED (veto-able) + Resolved-batch entry; (5) pokemon
concept = QoL+ (Q-0262.7, effective when the games program boots post-core) → owner-queue
item 4 Track-A RESOLVED. Lane halves verified at their HEADs: kit ORDER 011 **executed**
(#127/#128, Reading A, status 18:22Z); trading ORDER 008 **acked** @ 16:21:48Z (fresh
dedicated session runs it); superbot-next ORDER 009 **applied** in next #105 (flag-13
decision record on main). Owner-queue reconciled to the whole Q-0262 batch in the same
PR; status acks 008 in its orders footer.

## ORDER 009 · 2026-07-10T16:45Z · status: new
priority: P2
owner: a future fleet-manager standing wake (any pass after the current round settles)
do: Implement **generated roster v1** per
`docs/proposals/generated-roster-from-heartbeats.md` (filed by the 16:31Z wake, ORDER 002
part 2): `tools/gen_roster.py` reading each lane's `control/status*.md` over git transport
+ `list_triggers` for live routine state → generated `docs/roster.md` regenerated each
manager wake; then migrate superbot `docs/eap/fleet-manifest.md` to a pointer stub and
retire `check_manifest_freshness.py` per its own kill-switch header.
why: the hand-stamped manifest froze stale twice in 30 hours (grand-review §5, ORDER 002);
regeneration from the heartbeats the freshness checker already reads kills the staleness
class structurally (program-review §6.2, registry-disagreement §5.4).
done-when: `docs/roster.md` generated on main with per-row evidence + one parallel-run wake
comparing it against the hand manifest; manifest pointer-stub migration executed or
explicitly re-scheduled. **Decide-and-flag: this ORDER was self-filed by the manager
(not owner-routed) — the owner may veto by striking it.**
