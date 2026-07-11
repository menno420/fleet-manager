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

## ORDER 003 · 2026-07-10T12:05Z · status: DONE (executed by the Q-0265 continuation-chain slice 2026-07-10 ~20:45Z, fleet-manager PR #37)
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
✅ DONE: auto-append rule BINDING in `docs/review-queue.md` header + blueprint changelog —
**N=50 changed lines of runtime/product code** (excludes docs/, control/, .sessions/, pure
test additions) OR any self-flagged risk → mandatory row, appended by the PR's own session
before close (N=50 rationale documented in the file: catches real logic changes, skips
heartbeat/docs churn — decide-and-flag, owner may re-tune). **Drainer named, two-tier:**
PRIMARY = @codex post-merge review on Codex-enabled repos (Q-0258/Q-0259 r3; one specific
question on the merged head, Part C template, Q-0120 return path); FALLBACK = manager
failsafe-wake batches for repos without Codex (incl. fleet-manager itself — env not
created, ask on PR #26). Cadence: every wake batch reviews new rows; >48h unread = heartbeat
escalation. **First drain pass BACKFILLED — 8 rows** (venture-lab#9 D1-Stripe ·
superbot-games#16 CI-collection + #5 mining port · trading#21 promotion verdicts + #36
significance bar (pre-holdout, time-sensitive) · superbot#1920 checker-semantics (band's
biggest diff; band had zero disbot/ runtime PRs — honest finding) · pokemon-mod-lab#8
(chain head #4–#8, unplaytested) · gba-homebrew#12 compile-only-CI), each with why-risky +
citation + drain path; Codex availability marked per repo (superbot LIVE — codex-labeled
#1917 evidence; superbot-next LIVE; rest unknown-until-probed). This PR: fleet-manager
**PR #37**.

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

## ORDER 007 · 2026-07-10T13:43Z · status: DONE (executed by the Q-0265 continuation-chain slice 2026-07-10 ~20:45Z, fleet-manager PR #37 — rode ORDER 003 as filed)
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
✅ DONE: minted as playbook **R24** (new REVIEW RELAY section — the doctrine home ORDER
001's folds used): any lane session with a review-worthy-but-NOT-owner-only question posts
it as ONE specific question in a PR comment mentioning @codex on the final head (template:
superbot `docs/planning/codex-review-integration-plan-2026-06-17.md` **Part C**); **Q-0120
return path — verify against shipped source, never obey**; owner-queue is for owner-only
items ONLY. Cites Q-0258 + Q-0259 r3. Blueprint changelog entry binds R24 as the PRIMARY
tier of the review-queue drainer (same entry as ORDER 003). This PR: fleet-manager
**PR #37**.

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

## ORDER 009 · 2026-07-10T16:45Z · status: DONE (executed by the Q-0265 continuation-chain slice #2, 2026-07-10 ~21:20Z, fleet-manager PR #38)
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
✅ DONE (v1 scope): `docs/roster.md` **generation #1** on main — 17 rows (one per lane,
superbot-games split per-lane), each with heartbeat stamp + freshness age, phase, orders,
kit, live trigger state (99-record `list_triggers` sweep) and repo@HEAD evidence; header
carries generated-at + source-of-truth + the >24h kill-switch note. Regeneration duty
minted as playbook **R25** (every manager wake regenerates; commit only on change).
Staleness verdicts included (action-worthy: venture-lab 16h+ w/ 3 unconsumed ORDERs +
no trigger; pokemon ORDER 003 unconsumed). **Deliberately deferred, decide-and-flag:**
(a) `tools/gen_roster.py` mechanization — generation #1 was executed by the wake
procedure itself; script lands once a parallel-run wake confirms the format; (b)
**phase-2 manifest → pointer-stub migration NOT executed this slice** — the roster
proves itself first (one parallel-run wake vs the hand manifest), then superbot
`docs/eap/fleet-manifest.md` reduces to a pointer stub and `check_manifest_freshness.py`
retires per its kill-switch header; owner may veto. This PR: fleet-manager **PR #38**.

## ORDER 010 · 2026-07-10T19:45Z · status: DONE (matrix half executed by the Q-0265 continuation-chain slice #2, 2026-07-10 ~21:25Z, fleet-manager PR #38; per-lane relay rides each next lane contact)
priority: P2
owner: manager standing wake (rides the staleness sweep — per-lane, at next contact with each routine-armed lane)
do: **Per-lane model verification sweep.** At the next contact with each routine-armed
lane: (1) confirm its session-card template carries the `📊 Model:` line; (2) confirm its
recent fired-session cards record the actual model family (family-level names only, per
Q-0262); (3) **ground-truth step:** instruct fired sessions to record the model identity
their own harness/environment reports — family-level, in commits — so the matrix has a
consistent per-session self-report basis (the Routines screen is NOT a reliable
attribution surface; see `docs/capabilities.md` § routine self-arm rider). Report the
fleet-wide Project-setting vs fired-model matrix.
why: model attribution is inconsistent across surfaces (Routines menu fable-5 vs chat
header + card sonnet-5 on the evidenced websites fire — websites PR #59, squash 2c89e96);
`create_trigger` exposes no model arg, so per-session self-report is the only detector.
done-when: matrix in a findings doc (`docs/findings/`), one row per routine-armed lane:
Project setting · fired-session self-reported family · evidence link.
✅ DONE: `docs/findings/model-matrix-2026-07.md` on main — one row per repo (all 16,
routine-armed lanes covered), each: Project setting (**honest unknown everywhere**
except the codetool experiment arms — not agent-visible on any surface; `create_trigger`
no-model-arg re-confirmed on this slice's 99-record sweep) · card-self-reported families
(family-level per Q-0262; newest ~3–5 cards per repo at HEAD) · fired-vs-manual where
determinable (websites best-labelled; superbot reconcile routine = opus-4.8; fm chain =
fable-5) · evidence links. Cross-surface disagreement cited (websites 16:01Z fire:
Routines screen fable-5 vs card `claude-sonnet-5`, PR #59 squash 2c89e96 — card
re-verified at HEAD 1430f61). Null conventions surfaced: trading "withheld", gba "ID
withheld", pokemon "lane default", superbot newest template drops the line. Steps (1)/(2)
per-lane template+card checks and (3) the ground-truth self-report instruction ride each
next lane contact per the ORDER's own owner line (standing relay, matrix basis banked).
This PR: fleet-manager **PR #38**.

## ORDER 011 · 2026-07-10T20:30Z · status: DONE (re-arm executed 20:26Z; recorded + re-verified by the chain slice ~20:45Z, fleet-manager PR #37)
priority: P1
owner: this coordinator session (the Q-0265 doctrine-fold coordinator; parallel worker executing)
do: Adopt continuous mode for the manager seat itself (owner directive Q-0265, superbot
router, 2026-07-10): re-word the manager's standing trigger to the failsafe-wake pattern
("fleet-manager failsafe wake", same `30 */2 * * *` cadence — on a cron wake, if the
send_later continuation chain is alive, verify that in one line and end; if it stalled,
resume the work loop and re-arm the chain) + arm the ~15-min send_later continuation
chain as the manager's pacemaker; record the re-arm (delete + create calls) verbatim in
control/status.md per the proven cutover recipe.
why: Q-0265 puts ALL six core seats on continuous mode, the manager included; the
doctrine folds (gen-3 standard, blueprint changelog, init-prompt rider) land the pattern
for future seats, but the manager's own live trigger still carries the old
one-bounded-pass prompt.
done-when: trigger registry shows the failsafe-wake trigger (old one deleted), a live
continuation chain is armed, and status.md carries the verbatim re-arm record.
✅ DONE: new trigger **`trig_014odnv5h1tkJAFRhix3tGLq`** "fleet-manager failsafe wake"
(cron `30 */2 * * *`, created 2026-07-10T20:26:23Z, bound to the coordinator session) live;
old `trig_01QBrp5MjZL3F9mv6KsTXTzN` deleted — **both re-verified this slice against the
full 88-record `list_triggers` output** (new trigger present + enabled, next run ~22:34Z;
old id absent). Continuation chain armed on the ~15-min `send_later` pattern; **first chain
fire 20:43Z executed = the ORDER 003/007 slice (this PR)**. Verbatim re-arm record in
`control/status.md` per the proven cutover recipe. This PR: fleet-manager **PR #37**.

## ORDER 012 · 2026-07-10T21:42Z · status: ✅ DONE (proposal committed, PR #41; ⚑ OWNER-REVIEW pending — founding packages HELD)
priority: P1
owner: coordinator (owner-dispatch execution; parallel worker executing)
do: **Propose the games-program repo mapping (Q-0259 r.5)**, reshaped by two facts the
pre-birth sketch predates: (1) **games-web is the forge's first product** (phase 1
merged — the web-visual layer has a home; do NOT reuse the pre-games-web sketch) and
(2) **the versioned READ-ONLY data API over superbot's dashboard-data-contract pattern
(superbot PR #1920) blocks BOTH games-web phase 2 AND websites stats/explorer pages —
the mapping must place and sequence that API.** Ground the placement in what #1920's
pattern actually is (verify at superbot origin/main — committed-JSON vs live service —
before proposing). Cover: pokemon-mod-lab + gba-homebrew (existing repos, likely keep),
whether superbot-games becomes/feeds a dedicated project, what happens to the in-bot
game cogs (superbot-next band-6 port relationship), games-web's phase-2 dependency
edge. Recommendation style: decide-and-flag — one proposed mapping, alternatives one
line each. Sequencing language per Q-0266 (volume-first).
why: Q-0259 r.5 assigns the manager the 3-projects/3-repos mapping decide-and-flag; no
mapping proposal exists (the `projects/games-program/meta.md` sketch is pre-birth
material, drafted before games-web shipped and before the API need surfaced).
done-when: committed mapping proposal + ⚑ OWNER-REVIEW flag in status; **founding
packages only AFTER the owner reacts** (Q-0259 r5 + this dispatch).
✅ DONE: `docs/proposals/games-program-mapping-2026-07-10.md` committed (this PR).
Mapping: pokemon-mod-lab (QoL+ per Q-0262.7) · gba-homebrew (Lumen Drift release-prep
+ concept options) · **superbot-games becomes Project 3** (engine+content; resolves
the meta.md open question). **API placement: superbot lane**, contracted committed-JSON
feed per #1920's actual pattern (verified at superbot origin/main `655e0fea`: contract
file + stdlib repo-static producer + fail-closed checker + raw.githubusercontent
consumption — NOT a live service; the games feed needs one NEW DB-reading producer,
refresh path decided in the implementing superbot PR). games-web stays a forge product;
its phase-2 edge = the feed's first family (mining character-sheet, produced TO its
committed consumer contract). Sequence: feed slice NOW (superbot order) · boots
PARALLEL after owner reacts · phase-2/stats on feed live — the owner's
"API highest-leverage" read VALIDATED with the parallel-not-gating refinement.
**⚑ OWNER-REVIEW flag set in status; FOUNDING PACKAGES HELD until the owner reacts.**
This PR: fleet-manager **PR #41**.

## ORDER 013 · 2026-07-10T22:35Z · status: ✅ DONE (conformed mapping committed, this PR; ⚑ OWNER-QUEUE — react on the DETAILS)
priority: P1
owner: coordinator (owner-dispatch execution, round-3 part-4e; parallel worker executing)
do: **The games mapping is now OWNER-SHAPED via superbot router Q-0267 — produce the
CONFORMED mapping that fills in details; the prior proposal (fm PR #41,
docs/proposals/games-program-mapping-2026-07-10.md) is superseded as a shape and must
be annotated so.** THE DECIDED FRAME (do not re-litigate): Seat A = ONE Project on
existing superbot-games — the whole world ecosystem (exploration + mining + fishing +
world-adjacent), gen-2 relaunch merging the two terminal gen-1 lanes, their succession
packages (docs/retro/, docs/gen2-custom-instructions-exploration.md in that repo) as
boot inputs. Seat B = NEW repo + Project for the idle game, egg farm = first THEME;
template-first: idle-engine CORE + data-only THEME PACKS (same mechanics, different
skin per server), themes CI-validated. Product direction: website-first onboarding —
features/themes chosen on the website BEFORE the bot is invited; websites lane owns
the selector UI; games seats own the manifests it renders. Games ship as plugin
packages on superbot-next's manifest/plugin contract. STILL THE MANAGER'S TO PLACE
(ground in the design doc + evidence, decide-and-flag): (1) the read-only data API —
reconcile the prior superbot-lane committed-JSON placement (#1920) with the
website-first frame: stay/move/split (game-state feed vs theme/feature manifests are
different data)? (2) the theme-manifest contract's home — Seat B repo vs superbot-next
vs websites, + how the websites selector consumes it; (3) the new repo's NAME
(fleet-convention-grounded, 2 alternates); (4) first-shippable sequencing per seat
(Seat A relaunch increment; Seat B skeleton: engine core + egg-farm theme pack + CI
theme validation; websites selector increment; plugin-contract validation via
superbot-plugin-hello) — dependency-honest order. Also: check whether
menno420/superbot-plugin-hello exists now; refresh docs/owner-queue.md's games review
item to the conformed doc; heartbeat with the ⚑ OWNER-QUEUE flag.
why: Q-0267 (owner, live, 2026-07-10 ~22:1xZ) supersedes the ORDER 012 proposal as the
source of the shape — the manager's deliverable becomes conformance + detail-filling,
not an alternative frame.
done-when: conformed mapping committed + supersedes banner on the old proposal +
owner-queue item refreshed + ⚑ OWNER-QUEUE heartbeat.
✅ DONE: `docs/proposals/games-program-mapping-conformed-2026-07-10.md` (this PR).
Details placed: **(1) API SPLIT** — game-state feed stays the superbot-lane
committed-JSON contract feed (#1920, unchanged); theme/feature manifests = committed
files in the game-seat repos + superbot-next's plugin registry, raw-fetched by the
websites selector; provisioning write path = plugin-contract family, setup-code first.
**(2) Theme contract: Seat B drafts v1 + theme-gate CI in-repo**, flagged for promotion
into superbot-next's plugin-contract family (D-0056) when a second game consumes it;
websites raw-fetches schema + themes/*.yaml for the gallery. **(3) Name:
`superbot-idle`** (alternates: superbot-plugin-idle, idle-engine). **(4) Sequence:**
plugin-hello validation push ∥ Seat A relaunch (CI-gap fix → fishing on mining's
substrate) ∥ superbot game-state feed slice → Seat B skeleton (core → schema+CI →
egg-farm → more themes) → websites selector LAST-shippable (needs committed themes) →
setup-code consumption. **superbot-plugin-hello: EXISTS (owner-created, public, pushed
16:03:04Z) but EMPTY** — the superbot-next seeded package push is the unblocked next
step. Old proposal banner + owner-queue item 14 + heartbeat: this PR (fleet-manager
**PR #46**).

## ORDER 014 · 2026-07-11T00:25Z · status: ✅ DONE (executed in the PR that filed it — owner-update propagation, fleet-manager PR #54)
priority: P1
owner: coordinator (owner update relayed 2026-07-11 ~00:2xZ; worker executing)
do: **Propagate the owner's Codex fleet-wide enablement update (near-verbatim):**
"Codex environments now exist for ALL 12 active fleet repos (fleet-manager,
idea-engine, product-forge, sim-lab, substrate-kit, superbot, superbot-games,
superbot-idle, superbot-next, trading-strategy, venture-lab, websites; stale envs
for dead repos deleted)." NOTE THE SIGNAL: the list includes **superbot-idle** —
verify via list_repos/API whether menno420/superbot-idle now EXISTS (the conformed
mapping's proposed Seat B repo, owner-blessed by action if so) and its state.
Changes (one PR): (1) projects/ metas — every Codex-status line → "Codex: ENABLED
(owner, 2026-07-11)" on all 12 active repos; codetool ×3 archive metas note envs
deleted; quota caveat centralized (quota refusals, e.g. superbot#1920 2026-07-10
22:03Z, are RETRY-LATER, never a wall). (2) docs/capabilities.md — retire the
"Codex has no environment for fleet-manager" wall (dated, owner provenance); add
the fleet-wide enablement fact + quota caveat. (3) docs/review-queue.md — @codex
PRIMARY on all 12 repos (fallback tier only for quota windows + archives);
annotate open rows; ORDER 007 relay unblocked for fleet-manager PRs. (4)
docs/owner-queue.md — sim-lab OA-002 → Resolved; item 14 Seat B repo-creation
click DONE if superbot-idle exists (cite); react line → "react-by-action received
for repo name; §5 veto points remain open for objection, founding-package prep
proceeding decide-and-flag". (5) this ORDER appended + flipped ✅ DONE same PR;
ORDER 015 added per the react-by-action. (6) Heartbeat last (00:3xZ stamp).
why: owner update 2026-07-11 ~00:2xZ (live relay to the fleet-manager coordinator)
— fleet-wide Codex enablement + the superbot-idle creation signal must land in the
durable ledgers before the next wake batches drain on stale "no Codex env" facts.
done-when: all six change sets merged in one PR with the superbot-idle verdict
recorded (verified: EXISTS — public, seeded lane-contract README, pushed
2026-07-11T00:15:40Z).

## ORDER 015 · 2026-07-11T00:45Z · status: new
priority: P1
owner: coordinator (next chain slices execute it)
do: **Prepare Seat A (superbot-games relaunch) + Seat B (superbot-idle) founding
packages** per the conformed games mapping
(docs/proposals/games-program-mapping-conformed-2026-07-10.md) + the gen-3
born-continuous standard (Q-0265/Q-0266): per seat — instructions.md ·
coordinator-prompt.md · setup-script.sh · failsafe-prompt.md · meta.md in
projects/<repo>/, version-stamped, decide-and-flag. Seat A merges the two
terminal gen-1 lanes' succession packages as boot inputs (superbot-games
docs/retro/, docs/gen2-custom-instructions-exploration.md) and carries the
ORDER-001 CI-collection fix (review-queue #16, corrected target
.github/workflows/tests.yml) as first-increment work; Seat B builds on the
seeded superbot-idle lane-contract README (engine core → theme schema +
theme-gate CI → egg-farm theme; websites selector LAST-shippable). The owner
may veto any §5 point before the boots (Q-0240 window — silence = proceed).
why: the owner created menno420/superbot-idle under the conformed mapping's
proposed name (react-by-action, 2026-07-11T00:15:40Z) — the mapping's founding
prep is unblocked; ORDER 014 records the enablement context.
done-when: both founding packages committed to projects/ (registry doctrine:
manager sole writer, version stamps, family-level model names), owner-queue
paste-wave items refreshed, and the boot clicks queued with WHAT/WHERE/UNBLOCKS.

## ORDER 015 · update 2026-07-11T01:55Z · status: ✅ DONE (as RE-SCOPED — registry centralization, not authoring; fleet-manager PR #58)
priority: P1
do: (append-only DONE flip for ORDER 015 above — no new work ordered; this
block records the execution, fields per the kit's order grammar.)
why: reality overtook the 00:45Z filing — both games seats SELF-BOOTED before
any founding package was authored (handoff §5), so the executed scope is
registry centralization, not authoring.
done-when: (met in fleet-manager PR #58) both seats' packages committed to
projects/ version-stamped from what the booted seats actually run; matrix +
review-queue reconciled; ⚑ reconciliation flagged in control/status.md.
✅ DONE: executed per the coordinator handoff's reconcile note
(`docs/succession/coordinator-handoff-2026-07-11.md` §5): reality overtook the
filing — **both seats SELF-BOOTED** before any founding package was authored, so
the remaining scope was sweeping what the booted seats ACTUALLY run into
version-stamped `projects/` packages, regenerate-don't-fork. Landed (PR #58, lane
worker session, model: fable-5, dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL):
**(1) Seat A** — `projects/superbot-games/` regenerated in place v1 → **v2**
(seat LIVE: failsafe `trig_019ZgWyL78Rx1sr6LhvL8NE3` `15 */2 * * *` armed
2026-07-10T23:47:02Z, stored prompt VERBATIM-FROM-REGISTRY extracted
2026-07-11T01:26:43Z; order-001 MERGED — superbot-games PR #24, merge SHA
`7d4c347`, fix in `.github/workflows/tests.yml`, floor since 121→147→230 at HEAD
`773fab0`; orders 001+002 DONE per heartbeat 01:17:42Z; kit v1.8.0;
setup-script.sh kept + marked NEVER-DEPLOYED). **(2) Seat B** —
`projects/superbot-idle/` built v1 from the live seat (stub meta → real meta;
HEAD `677b74d`, PRs #1–#25 merged, 216 tests, kit v1.7.1; failsafe
`trig_01TWKGFW8RUsMvxUMt2ndzqA` `45 */2 * * *` armed 23:44:45Z,
VERBATIM-FROM-REGISTRY; NO setup-script.sh — none verifiably deployed, stated in
meta; never-deployed parts say so explicitly instead of inventing content).
**(3)** `projects/README.md` matrix rows + stub list corrected; **(4)**
review-queue superbot-games#16 CLOSED (VERIFIED-FIXED-AND-MERGED). The order's
original done-when items "owner-queue paste-wave items refreshed" and "boot
clicks queued" are MOOT under the re-scope (no boots remain to click — both
seats run; paste-wave note updated in projects/README.md). ⚑ reconciliation
flagged in `control/status.md` per decide-and-flag.

## ORDER 016 · 2026-07-11T01:5xZ · status: new
priority: P0
owner: owner-directed (relayed via a superbot session, 2026-07-11 — the owner
asked for a cross-project instruction + env audit; this ORDER carries its output)
do: **Act on the fleet instruction + environment audit**
(docs/findings/instruction-and-env-audit-2026-07-11.md — READ IT FIRST; every
claim is file:line-cited, verify against the tree per R2). Sequenced:
(1) **FLEET-CRITICAL, route to the owner-queue:** the audit §2.4 corrected
merge-authority clause for projects/UNIVERSAL.md. The current owner-landed block
tells every seat to "arm auto-merge at creation / REST-merge on green" — BOTH are
classifier-walled (terminal), so 12/13 lanes prescribe the walled path as PRIMARY
(only substrate-kit is correct). The corrected clause = "open READY, do nothing
else, the auto-merge-enabler.yml workflow lands it server-side; never call
enable_pr_auto_merge/merge_pull_request yourself; if it can't land, park
READY+green and keep opening PRs — never agent REST-merge." UNIVERSAL.md is
OWNER-PROVENANCE (instruction-poisoning guard) → the owner lands it, not the
manager. Add a six-field owner-queue item with the audit §2.4 paste block.
(2) **After the owner lands §2.4:** re-issue every walled projects/<repo>/
instructions.md (audit §2.2 table) from the corrected block, keeping each repo's
own required-check names/born-red gate, and fix the §3.2 same-file contradictions
(fleet-manager:76-vs-85, trading:92-vs-96) in the same pass; resolve the §3.1
mandatory-block drift (claimed verbatim, present in 0/13); hoist §3.3 into
UNIVERSAL.md.
(3) **Do now (manager-owned, no owner needed):** env **R1** (register sim-lab,
product-forge, idea-engine, **superbot-idle** [live seat, no archetype named],
mobile-lab in archetypes.md + the python-lab Serves: header) and **R5** (point
the codetool-lab-* env fields at archetype-python-lab.sh, not setup-universal.sh
— pyproject [dev] deps silently skip today). File **R2/R3/R4/R6** (one base shim +
3 knobs; gba-lab flips/xdelta + gated devkitARM; retire per-package probe
variants; mobile-lab node-lab decision) as a consolidation lane.
(4) **Per-lane verify** before trusting the "just let the enabler do it" fix: for
each repo confirm auto-merge-enabler.yml is actually installed in
.github/workflows/ AND "Allow auto-merge" + the required check are set — lanes
that structurally can't arm (fast-CI race / no pending window / venture-lab
substrate-gate-not-required / trading Allow-auto-merge-OFF) need the two-party or
GITHUB_TOKEN merge-on-green workflow, not just corrected wording.
why: seats stall on merges and route one-click asks to the owner every night
because the fleet's own canonical instruction prescribes the classifier-walled
merge path (the kit's CAPABILITIES already has the working recipe). Fixing
UNIVERSAL at the root propagates to all 13 lanes. Env consolidation cuts the
setup-script surface ~4→1 and closes a live-seat drift.
done-when: owner-queue item for §2.4 filed; R1+R5 landed; the walled-instruction
re-issue + R2/R3/R4/R6 tracked as their own orders/lane; per-lane enabler-install
verification recorded. (The merge-authority re-issue itself is gated on the owner
landing §2.4 — do not rewrite the owner-provenance UNIVERSAL block yourself.)

## ORDER 016 · update 2026-07-11T06:57Z · status: ✅ DONE (for its now-scope — owner-queue + R1/R5 + verification; fleet-manager PR #68)
priority: P0
do: (append-only DONE flip for ORDER 016 above — no new work ordered; this
block records the execution, fields per the kit's order grammar.)
why: the now-scope items (1)(3)(4) are executed and the gated item (2) +
R2/R3/R4/R6 are tracked as their own orders, per the order's own done-when;
the §2.2 re-issue stays OWNER-GATED on owner-queue item 16.
done-when: (met in fleet-manager PR #68) owner-queue item for §2.4 filed;
R1+R5 landed; the walled-instruction re-issue + R2/R3/R4/R6 tracked; per-lane
enabler-install verification recorded.
✅ DONE: executed (PR #68, lane worker session, model: fable-5, dispatched by
coordinator cse_012o8pySy5K3AV6JWoPKryZL): **(1)** owner-queue item 16 filed —
the audit §2.4 corrected merge-authority clause as a verbatim paste block for
owner-provenance projects/UNIVERSAL.md. **(2)** R1 landed — 5 unregistered
lanes (sim-lab, product-forge, idea-engine, superbot-idle, mobile-lab)
registered in environments/archetypes.md + the archetype-python-lab.sh
Serves: header. **(3)** R5 landed — the 3 projects/codetool-lab-*/meta.md
setup-script fields repointed to archetype-python-lab.sh. **(4)** the §2.2
re-issue + R2/R3/R4/R6 tracked as draft ORDERs 017/018 in
docs/planning/order-016-followups-2026-07-11.md (⚑ drafts, NOT filed — inbox
one-writer rule; coordinator to file). **(5)** per-lane enabler verification
recorded at docs/findings/enabler-install-verification-2026-07-11.md — only
3/13 lanes (substrate-kit, superbot, idea-engine) have auto-merge-enabler.yml
installed; allow_auto_merge + required checks NOT MEASURABLE this session
(walls quoted verbatim in the doc). The §2.2 re-issue itself stays
OWNER-GATED on owner-queue item 16 (never rewrite the owner-provenance
block). ⚑ PR #68 itself is PARKED READY+green — the agent merge was
classifier-denied at dispatch (verbatim denial recorded in the findings doc
§"Live confirmation (same day)"), so a non-author landing is needed
(fleet-manager has NO enabler installed, per the verification table).

## ORDER 017 · 2026-07-11T11:52Z · status: new — GATED: do NOT execute until owner-queue item 16 resolves
priority: P1 — **GATED ON owner-queue item 16 (the §2.4 UNIVERSAL.md merge
clause): do NOT execute until the owner-queue item resolves** (the corrected
block must exist as owner-provenance text before any file is re-issued from
it).
owner: manager (self-executable once the gate clears; no further owner click)
provenance: filed by coordinator direction (cse_012o8pySy5K3AV6JWoPKryZL)
from the ORDER 016 follow-up drafts
(docs/planning/order-016-followups-2026-07-11.md).
do: **do NOT execute until owner-queue item 16 resolves — then re-issue every
walled `projects/<repo>/instructions.md` from the corrected UNIVERSAL merge
clause** (audit §2.2 table — 12 of 13 files prescribe the classifier-walled
arm/REST-merge path as PRIMARY; only substrate-kit is correct; superbot-idle /
games-program / mobile-lab have `meta.md` only and must be *born correct*).
Keep each repo's own required-check names and born-red gate. In the same pass:
(1) fix the **§3.2 same-file contradictions** — `fleet-manager/
instructions.md:76` mandates the REST squash-merge it lists as a classifier
wall at `:85`; `trading-strategy/instructions.md:92` says "MERGE AUTHORITY is
yours" then `:93-96` calls the classifier denial terminal;
(2) resolve the **§3.1 mandatory-block drift** — UNIVERSAL.md + README.md
claim the permissions block is carried verbatim in every `instructions.md`,
but a grep returns zero hits in 0/13; either actually insert the (corrected)
block into each file, or retract the "verbatim" claim and keep it
wake-prompt-only;
(3) execute the **§3.3 hoist** — centralize the ~10 near-verbatim duplicated
rule blocks into a "Fleet-canonical working rules" section of UNIVERSAL.md
(proposed block text in audit §3.3), leaving per-repo files only
repo-specific mission / CI-landing specifics / hard rails. *(Note: the hoist
adds text to owner-provenance UNIVERSAL.md — bundle it into the same
owner-landing sitting as §2.4 / the PR #47 v2 fold, or land it as a follow-up
owner paste; never self-edit that file.)*
Also fold in the **§5.4 per-lane enabler verification** before trusting the
"open READY, do nothing" doctrine per repo: confirm each repo actually has
`auto-merge-enabler.yml` installed in `.github/workflows/` AND "Allow
auto-merge" + a required check set — lanes that structurally can't arm
(fast-CI race / no checks-pending window / venture-lab
substrate-gate-not-required / trading Allow-auto-merge-OFF) get the two-party
non-author review-then-merge or a `GITHUB_TOKEN` merge-on-green workflow
noted in their re-issued file, not just corrected wording.
why: the fleet's canonical instruction tells every seat to do the thing the
platform classifier terminally denies — seats stall on merges and route
one-click asks to the owner nightly; fixing the root then re-issuing
propagates the fix to all 13 lanes (audit §0.1, §2).
done-when: all §2.2 walled rows re-issued from the corrected block (each with
its own required-check names/born-red gate kept); both §3.2 contradictions
gone; §3.1 resolved one way or the other with the claim and the files
agreeing; §3.3 hoist landed via an owner-provenance path; per-lane
enabler/arm status recorded per repo.
> **Per-lane verification landed (2026-07-11, ORDER 016 step 4):**
> `docs/findings/enabler-install-verification-2026-07-11.md`
> — only 3/13 lanes (substrate-kit, superbot, idea-engine) have the enabler
> installed, so **10 lanes need an enabler (or a `GITHUB_TOKEN` merge-on-green
> workflow) INSTALLED — an agent-doable PR per repo — before the corrected §2.4
> wording is true for them**.

## ORDER 018 · 2026-07-11T11:52Z · status: new
priority: P2
owner: manager (delegable to a lane worker; all doc/script work in this repo)
provenance: filed by coordinator direction (cse_012o8pySy5K3AV6JWoPKryZL)
from the ORDER 016 follow-up drafts
(docs/planning/order-016-followups-2026-07-11.md).
do: **Env-consolidation lane — audit R2/R3/R4/R6** (R1+R5 already landed by
the ORDER 016 now-scope session):
(1) **R2 — collapse the 4 Python archetype scripts into ONE base shim + 3
knobs** (`BASELINE_PIP`, `ENV_REPORT` var-list, `pick_python` table) —
coordinator's `setup_one` is already a strict superset of python-lab /
bot-prod / pinned-research manifest handling; the four become ~20–30-line
config diffs. **Fix in-flight: add the missing `superbot-next→python3.11`
case to the coordinator `pick_python` table** — superbot-next is a child of
the live multi-repo (coordinator) env and today installs under bare
`python3`, correct only by luck (audit §4.2 latent bug).
(2) **R3 — gba-lab stays separate; fix two lane gaps:** (a) it installs no
ROM-patch/distribution tooling — confirm pokemon-mod-lab's shipping model and
add `xdelta3`/`flips` if it emits base→modded patches (the ROM itself is
un-distributable); (b) gate the Block-3 devkitARM Track-B mirror pull behind
Butano/homebrew detection so a pokeemerald-only env stops pulling an
unsigned-mirror toolchain it never uses (directly affects the Retro-Games
seat spanning both game repos).
(3) **R4 — retire the per-package `setup-script.sh` probe variants** (dual,
drifting lineage; websites / substrate-kit / fleet-manager metas already flag
it) — pick one lineage; normalize superbot-games' split `environment/` vs
`environments/` dirs.
(4) **R6 — decide mobile-lab's shape before launch:** its Node/Expo toolchain
is orthogonal to all 5 archetypes; if a second JS lane appears, promote a
thin `node-lab` knob on the R2 base rather than repeating the repo
escape-hatch (mobile-lab is registered python-lab-with-escape-hatch as of
ORDER 016 R1, pending this decision).
why: the multi/single-repo detection block is byte-identical in all 5 scripts
and 4 of 5 archetypes are one base shim + a small knob-diff apart —
consolidation cuts the setup-script surface ~4→1, kills the drifting probe
lineage, and fixes a latent interpreter-pin bug on a live env (audit §4.2,
§4.3).
done-when: one base shim + knob table on main with the 4 archetype scripts as
thin configs (superbot-next→3.11 case included); gba-lab's two gaps
dispositioned; probe variants retired to one lineage; a recorded R6 decision
(node-lab knob vs escape-hatch stays) in `environments/archetypes.md`.

## ORDER 018 · update 2026-07-11T13:06Z · status: ✅ DONE (env consolidation R2/R3/R4/R6; fleet-manager PR #73)
priority: P2
do: (append-only DONE flip for ORDER 018 above — no new work ordered; this
block records the execution, fields per the kit's order grammar.)
why: all four items (R2/R3/R4/R6) are executed in one PR; the ORDER's
done-when is met in full — no residue, no gated remainder.
done-when: (met in fleet-manager PR #73) one base shim + knob table on main
with the 4 archetype scripts as thin configs (superbot-next→3.11 case
included); gba-lab's two gaps dispositioned; probe variants retired to one
lineage; a recorded R6 decision in environments/archetypes.md.
✅ DONE: executed (PR #73, lane worker session, model: fable-5, dispatched by
coordinator cse_012o8pySy5K3AV6JWoPKryZL): **(1) R2** —
`environments/setup-base.sh` landed (ONE base shim: the byte-identical
multi/single-repo detection + the coordinator-superset manifest ladder,
parameterized by knobs `BASELINE_PIP` / `PICK_PYTHON_TABLE` / `ENV_REPORT` /
`GIT_TRIAGE`); the 4 Python-family archetype scripts are now ~25-line thin
configs sourcing it (filenames stable — every meta.md pointer keeps
resolving); knob table + notes in `environments/archetypes.md`. The audit
§4.2 latent bug is FIXED — the consolidated pin table carries
`superbot-next→python3.11` for coordinator too — plus a SECOND latent bug
found during consolidation: `pick_python`'s missing-interpreter WARNING was
emitted on stdout inside a command substitution and would have been captured
INTO `$py`, corrupting the interpreter name; now stderr. **(2) R3** —
gba-lab stays a separate full script; (a) FIXED IN-SCRIPT: `xdelta3` added
to the apt baseline (patch-distribution tooling; `flips` deliberately NOT
added — not in the Ubuntu apt archive, would mean another unsigned source
build; why-not recorded in archetypes.md § "R3 disposition"); (b) FIXED
IN-SCRIPT: the Block-3 unsigned devkitARM mirror pull is gated behind
homebrew detection (pokeemerald-only env skips it; bare/unknown layout keeps
the proven default; `GBA_TRACK_B=force`/`skip` overrides). **(3) R4** — the
13 `projects/*/setup-script.sh` probe variants retired to short exit-0
tombstones pointing at the one `environments/` lineage; superbot-games'
`environment/`-vs-`environments/` split is LANE-SIDE (that repo) — listed as
a follow-up on the heartbeat, not edited cross-repo from here. **(4) R6** —
decision recorded in archetypes.md (⚑ decide-and-flag): mobile-lab's repo
escape-hatch STAYS; a `node-lab` knob on `setup-base.sh` is the named
promotion path the moment a second JS lane appears. All shipped scripts
`bash -n` clean + sandbox-tested with stubbed apt/curl/python (multi-repo +
single-repo, 3.11/3.10 pins, fallback WARN, base-unavailable fail-soft,
Track-B gate skip/attempt/override — all exit 0). Thin configs are
re-derived and unverified-as-thin-configs until the next owner paste / lane
boot (Q-0105 posture; noted in archetypes.md).

## ORDER 017 · update 2026-07-11T17:00Z · status: ✅ DONE (instruction re-issue from UNIVERSAL v4; fleet-manager PR #77 — PARKED for the owner)
priority: P1
do: (append-only DONE flip for ORDER 017 above — no new work ordered; this
block records the execution.)
why: the gate cleared — owner-queue item 13 resolved by PR #76 (owner-merged
2026-07-11T15:26:47Z, UNIVERSAL v4 @ `e1848ff`) — and the re-issue executed
in one PR against the prepared edit manifest.
done-when: (met in fleet-manager PR #77, parked READY for the owner's click —
instruction-authority content; no auto-merge armed, no agent merge)
✅ DONE: executed (PR #77, lane worker fable-5, dispatched by coordinator
cse_012o8pySy5K3AV6JWoPKryZL):
- **All 15 §2.2 rows re-issued** from the corrected clause: every
  `projects/<repo>/instructions.md` v1→v2 (superbot-games v2→v3) with the
  canonical Permissions & authority block inserted BYTE-VERBATIM from
  `projects/UNIVERSAL.md:44-81` @ `e1848ff` (cmp-verified per file); each
  repo's own required-check names + born-red gate kept; all 15 files < 7,500
  bytes (paste-safe; websites trimmed 8,382→7,470).
- **§3.2 contradictions gone**: fleet-manager :76 REST-mandate vs :85 wall
  list (both rewritten to park-READY+green); trading-strategy :92 "MERGE
  AUTHORITY is yours" deleted vs :93-96 terminal-denial (survives inside the
  canonical block).
- **§3.1 resolved by INSERTION** (UNIVERSAL is owner-only; its "verbatim in
  every file" claim now TRUE — the claim and the files agree).
- **§3.3 hoist**: staged as the owner paste bundle
  `docs/proposals/universal-v5-hoist-bundle-2026-07-11.md` (v4→v5, owner
  sitting) — NO agent edit to UNIVERSAL.md.
- **§5.4 per-lane enabler status recorded in every file** per
  docs/findings/enabler-install-verification-2026-07-11.md; the two unprobed
  lanes were probed this session via raw fetch: superbot-idle NO enabler
  (auto-merge-enabler.yml 404), superbot-mineverse HAS the enabler (200).
  Enabler lanes (substrate-kit, superbot, idea-engine, + mineverse) say so;
  all others carry park-READY+green + the GITHUB_TOKEN merge-on-green
  standing fix + non-author review-then-merge path.
- **Incident riders folded per-file**: merge-authorization,
  all-checks-COMPLETED, token/CI-poll budget, fresh-clone workers, date -u
  timestamps (all 15); Q-0120 phantom-claim rider into the 8 files missing
  it; silent-fire self-check into websites, gba-homebrew, pokemon-mod-lab.
- **Companion coordinator-prompt.md one-liners updated** (11 files);
  playbook R21 annotated SUPERSEDED; superbot-mineverse :101-104
  supersession note executed; superbot-retro meta.md note + flagged trigger
  re-arm follow-up (registry-verbatim stored prompts NOT edited);
  owner-queue items 13 + 15 refreshed; projects/README.md paste-wave
  registry updated to v2/v3-bodies-only.
