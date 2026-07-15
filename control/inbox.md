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

## ORDER 019 · 2026-07-12T16:10Z · status: new
priority: P1 — time-sensitive (Anthropic EAP review window through Tue 2026-07-14)
owner: Websites seat (route via the manager's next dispatch; the owner-live superbot
session delivered this order on the owner's behalf — owner-queue item 5 of the
2026-07-12 fleet-drive log)
do: Refresh + upgrade the public program-review site
(`https://review-production-f027.up.railway.app`) per the FULL order at superbot
`docs/owner/websites-review-site-order-2026-07-12.md` (read it raw from superbot main —
the "ORDER (paste-in)" block is the executable body). Four workstreams: **(A)** refresh
ALL data to 2026-07-12 (the scheduler incident, 15→8 seat consolidation, live counts
with as-of stamps, every claim → a public commit, fix the daily auto-refresh);
**(B)** enable the live on-site AI review/interaction assistant (server-side key, Ask +
Review modes, evidence-grounded only, rate-limit + spend cap);
**(C)** rebuild the homepage (one-line what-this-is, key-stats row, 3–5 finding cards,
AI panel, "how this site is organized" map); **(D)** accuracy + polish pass.
PRE-CLEARED: the one owner secret the order anticipated is ALREADY SET — the owner-live
2026-07-12 session provisioned `ANTHROPIC_API_KEY` on BOTH review services (the live
`reliable-grace`/review serving review-production-f027, redeployed same hour, AND the
parallel `superbot-websites`/review). Do NOT re-flag it; build against it.
why: the second Anthropic email (sent 2026-07-12 13:24Z) links this site as the evidence
home; reviewers click it this week. Its data is a 07-11 snapshot and the AI promise isn't
live yet.
done-when: live URL shows 07-12 data + the incident + 8-seat fleet page; the AI panel
answers grounded questions on the public site; homepage leads with the findings; a status
report lands in control/status.md with model choice, rate-limit and spend-cap values.

## ORDER 020 · 2026-07-12T16:10Z · status: new
priority: P1 — reliability (closes the 2026-07-12 silent-outage detection gap)
owner: fleet-manager (the manager itself — fold into the wake ritual / gen_roster.py)
do: Add a per-wake trigger-health check per the FULL order at superbot
`docs/owner/trigger-health-order-2026-07-12.md` (the fenced ORDER block is the executable
body). Each wake: read list_triggers (all pages); flag WEDGED crons
(`enabled ∧ next_run_at < now − 15min`); flag DROPPED one-shots (past `run_once_at`,
still enabled); flag DEAD chains (dropped one-shot + no future tick); recover dark seats
via send_message (the only working cross-session revival path — org policy blocks
cross-session trigger calls); treat a stale docs/roster.md as the regen cron itself
wedged (flag loudly). Keep health output on the roster (Actions substrate) so the
watchdog's record survives a CCR scheduler outage. Do NOT re-edit .claude/settings.json
for recovery-tool prompts (Q-0242 — the allowlist provably doesn't hold; recovery runs
in Routine-spawned sessions whose spawn-time session_context carries the grants).
why: 2026-07-12 ~02:30–08:00Z the scheduler degraded silently — 9 dropped one-shots, 2
wedged crons, two seats dark ~6h. Everything needed to catch it was in list_triggers all
night; nothing was watching. Detection signature verified against the incident registry.
done-when: the check runs automatically each wake AND re-playing the 2026-07-12 registry
snapshot (venture-lab failsafe frozen 06:06, kit-lab loop frozen 06:08, 9 dropped
one-shots) surfaces every one as WEDGED/DROPPED/DEAD in a single wake, with a
send_message recovery attempted the same cycle.

## ORDER 021 · 2026-07-12T17:25Z · status: new
priority: P2 (after ORDER 019's time-sensitive workstreams)
owner: Websites seat
provenance: owner live directive 2026-07-12 (owner-live superbot session, delivered on his
behalf): "there should be a place on the control website that shows all the links of our own
websites and websites we have active business"
do: Build a **web-presence directory** on the control-plane site: one page that lists every
fleet web surface with a link, one-line purpose, and live health. Source it from a COMMITTED
registry file (JSON or md table — your call; agent-updatable by PR, rendered at request time)
so the page is a single source of truth, never hand-maintained HTML. Three sections:
(1) **Our sites** — seed with the verified 2026-07-12 inventory: review-production-f027
(public program review, the Anthropic-email link) · web-production-97636 (mineverse, Games
flagship) · superbot-app (botsite) · superbot-dashboard (Discord-gated) · control-plane-
production-abb0 (owner console) + the three parallel copies dashboard-production-a91b /
botsite-production-cfd7 / review-production-fc91 (label these DUPLICATES pending
OQ-RAILWAY-PROJECT-SPLIT consolidation — do not present as distinct products).
(2) **External business surfaces** — empty at launch but first-class: Gumroad/Lemon Squeezy
listings, itch.io pages, published articles, GitHub Releases, as they go live (venture-lab's
three products + Lumen Drift + games-web are each one owner click away — list them as
"pending publish" rows with what unblocks each).
(3) **Health** — reuse the existing readiness/probe machinery (the control-plane already
probes services) for a per-row live/degraded/down badge with an as-of stamp; never fabricate
liveness (arcade-registry precedent: a dead link renders as an honest status note, not a
button).
why: the owner's recurring pain is "what is live and where do I find it" — today an owner-live
session had to reconstruct the inventory from the Railway API by hand. The fleet has 8+ public
surfaces and a growing external footprint; a self-maintaining directory ends the question.
done-when: the directory page is live on the control-plane behind the existing gate (plus a
public variant if trivially safe — links only, no secrets), rendered from the committed
registry, seeded with the section-1 inventory above, health badges honest, and a status report
lands in control/status.md naming the registry path so other seats know where to add rows.

## ORDER 022 · 2026-07-12T17:40Z · status: new
priority: P1 (rides with ORDER 019 — same sitting; items 1–2 are minutes each)
owner: Websites seat
provenance: owner live directive 2026-07-12 (owner-live superbot session — the "which discussed
things are not yet planned or live" audit); companion to ORDERs 019 + 021.
do: four deltas the 019/021 bodies don't cover —
(1) **Flip the arcade's mineverse card to LIVE** (botsite/data/arcade.json — the #161 design:
data change only): mineverse now serves at `https://web-production-97636.up.railway.app`
(read-only; sign-in one owner click away). Set availability live + the URL (keep the
`?ref=fleet-arcade` attribution convention); status_note stays honest: "read-only demo —
player sign-in launching" until the owner's redirect click lands. Re-verify the URL is 200 at
change time; never ship a dead button.
(2) **Verify the /owner/environments live half NOW** — `RAILWAY_TOKEN` (project-scoped,
superbot-websites/production) was set on control-plane 2026-07-12 and the service redeployed.
The page's GraphQL query shape was explicitly UNVERIFIED until a token existed (#166 deferred
note). Load the page; if the Railway panel renders variable NAMES, record verified; if it
degrades, fix the query against the real API response — that was the designed failure mode,
not an incident.
(3) **Make the daily review-bake actually land** — the workflow regenerates fine but dies at
`gh pr create`: "GitHub Actions is not permitted to create or approve pull requests" (runs
29167034060 + 29184552812; same wall fleet-manager had). Proven fix from today, copy it: arm a
SELF-RETIRING CCR bridge routine (create_trigger, fresh-session, this repo's environment,
offset a few minutes after the bake cron) that lands the parked bake branch/PR each fire and
deletes itself once it observes an Actions run where PR-create succeeded (= the owner ticked
the toggle). Reference implementation: fleet-manager trig_011LrFY1k5cUHRYH6zwTvPvn (armed
2026-07-12; pattern in fleet-manager docs/capabilities.md § rescue venue). Also add the
websites Actions-toggle click to docs/owner-queue-candidates intake so the manager carries it.
(4) **Reconcile stale asks in docs/owner/OWNER-ACTIONS.md + control/status.md**: the
ANTHROPIC_API_KEY ask (SET on BOTH review services 2026-07-12 — live reliable-grace/review
redeployed AND superbot-websites/review), the RAILWAY_TOKEN ask (SET, see item 2), and any
GITHUB_TOKEN residue (#160 already struck it). Strike-with-evidence per your records
convention; do not re-flag satisfied asks.
FENCES (both weeks-scoped, not forever): do NOT move/rename review-production-f027 or
consolidate the duplicate Railway projects during the EAP window (through 2026-07-14) — the
Anthropic email links the live URLs; consolidation is parked as owner-queue
OQ-RAILWAY-PROJECT-SPLIT for after the window.
why: mineverse went live, the token landed, and the bake root-cause got a proven fix — all
TODAY, after 019/021 were written; without this order the arcade lies, the env page stays
unverified, and the review site data silently ages.
done-when: arcade card live + honest; /owner/environments Railway panel verified (or fixed)
with the result in status.md; the bake bridge routine armed + recorded (verbatim create_trigger
call + list_triggers verify in status.md); OWNER-ACTIONS carries zero satisfied-but-open asks.

## ORDER 022 · update 2026-07-12T18:00Z · status: amended — item 3 OBSOLETE (owner clicked both toggles; live-verified)
priority: P1 (unchanged)
owner: Websites seat (unchanged)
do: SKIP ORDER 022 item 3 — do NOT arm the bake bridge routine. The owner ticked "Allow
GitHub Actions to create and approve pull requests" on BOTH repos (fleet-manager + websites)
2026-07-12 ~17:45Z, and the owner-live session live-verified both: websites review-bake
dispatch run 29202721928 → SUCCESS end-to-end (runs 1–2 had died at PR-create);
fleet-manager roster-regen run 29202721367 → SUCCESS and self-landed roster Generations
#17/#18 (PRs #129/#131, opened AND squash-merged by the workflow itself). Instead of the
bridge: confirm the next SCHEDULED bake run also lands (dispatch path proven; cron path
should follow) and record it in status.md. Items 1, 2, 4 and the EAP-window fences stand
unchanged. (The fleet-manager roster bridge trigger was deleted the same hour; owner-queue
item 33 → RESOLVED.)
why: arming a bridge for an already-open permission would waste a standing routine and
mislead the next reader about the wall's state.
done-when: status.md records the next scheduled bake run's conclusion; no bridge trigger
exists for the bake.

## ORDER 020 · update 2026-07-12T18:40Z · status: ✅ DONE (per-wake trigger-health check; fleet-manager PR #133)
priority: P1
do: (append-only DONE flip for ORDER 020 above — no new work ordered; this
block records the execution, fields per the kit's order grammar; written by
the ORDER-020 lane worker as manager delegate.)
why: the ORDER's done-when is met in full — the check runs at every wake by
R26 + the wake-prompt wiring, and re-playing the 2026-07-12 incident registry
surfaces every wedge/drop/dead-chain in a single wake.
done-when: (met in fleet-manager PR #133) check runs automatically each wake
AND the 2026-07-12 registry replay surfaces the venture-lab failsafe wedge,
the kit-lab loop wedge, and the dropped one-shots as WEDGED/DROPPED/DEAD with
a send_message recovery named the same cycle.
✅ DONE: executed (PR #133, lane worker session, model: fable-5, dispatched by
the coordinator). **(1) Detection** — `scripts/check_trigger_health.py` (R26,
stdlib-only): six PASS/FAIL invariants per wake — I1 WEDGED-cron
(`enabled ∧ next_run_at < capture − 15min`), I2 DROPPED one-shot (enabled past
`run_once_at`; QUEUED-vs-LOST flagged as indistinguishable per the spec note),
I3 DEAD-chain (dropped tick + no future tick on the seat session, recovery =
`send_message` that session; Q-0242 venue caveat quoted in the output), I4
manager-failsafe present + unwedged, I5 roster freshness (stale roster = the
regen cron may itself be wedged), I6 snapshot freshness; nonzero exit on any
FAIL; `--selfcheck` offline assertions; `--now` replay mode. **(2) Roster
record (spec step 2 + second-substrate note)** — `scripts/gen_roster.py` now
renders a per-lane "Trigger health" column + a fleet-wide "Trigger health"
section (WEDGED/DROPPED/DEAD detail with lane attribution) from the same
primitives, so the watchdog's record rides the Actions regen cron and survives
a CCR scheduler outage. Health is evaluated AT the snapshot's capture instant
— NEW top-level `captured_at` stamp in the export (telemetry/README.md recipe
step 3; wall-clock eval measured to fabricate 7/9 false wedges on a 2.5h-old
snapshot; fallback ladder documented in `snapshot_eval_time`). **(3) Wake
wiring (stateless — prompts name the check, the script holds the logic)** —
playbook R26; v3 per-project startup + custom-instructions verify lines;
projects/fleet-manager registry copies byte-synced with a delta stamp.
**(4) Proof** — incident replay (mid-outage snapshot `4111da4` @ 06:33Z):
FAIL 5/6 — 6 WEDGED crons incl. venture-lab (frozen 04:06Z), kit-lab loop
(frozen 06:08Z) and the manager's own failsafe, 6 dropped one-shots, 4 DEAD
chains each naming its send_message recovery — the spec's done-when replay.
Live run (committed gen-14 snapshot, capture-instant 11:12Z): FAIL 4/6 — REAL
findings (game-lab failsafe wedged at 10:50Z, 6 dropped, 2 dead chains,
snapshot 7h stale), hand-verified against the raw records; recorded in
control/status.md for the next wake to act on (R26).

## ORDER 020 · update 2026-07-12T19:20Z · status: amended — add the TICK PILE-UP detection signature (live incident, same day)
priority: P1 (unchanged)
owner: fleet-manager (the manager itself — same wake ritual as the base order)
do: Add a FOURTH detection signature to the per-wake trigger-health check: **TICK PILE-UP —
more than one pending pacemaker/work-loop one-shot bound to the SAME session** (same or
near-identical message text). Remedy: prune to the NEWEST tick (delete the rest) and record
the prune in the roster health column + status.md. Also relay the pacemaker discipline rule
to every seat (manager relay or next prompt re-issue): re-arm ONLY after consuming the prior
tick — one outstanding tick per session, ever; a wake with nothing to do re-arms SILENTLY and
must not emit a filler reply.
why: live incident 2026-07-12 evening — the Websites coordinator chat was flooded with
degenerate one-word replies ("court") as stacked pacemaker ticks fired minutes apart; the
registry showed one session with FOUR identical pending ticks (19:11/19:17/19:39/19:57Z) plus
duplicates on two other seats. The owner had to notice it by eye (screen recording); nothing
watched for it. The owner-live session pruned the surplus ticks by hand (deleted
trig_01WDo1jC9KUEqQXpTZto7Qya, trig_01DDuyrSM1DdhHmUUayxw9sH, trig_01XBpwCcn91h5TELTEz7tWcQ;
kept the newest 19:57 tick + the distinct codex-retry one-shot) — that hand-prune is exactly
what this signature automates. (Same sweep also deleted the now-redundant
"Websites review-bake bridge" cron trig_01A49tzPzuG3NeRZsLrUNx3T — the Actions toggle is
live-verified, run 29202721928.)
done-when: the wake ritual flags >1 same-session pending work-loop one-shots as PILE-UP,
prunes to newest, and records it — re-playing tonight's registry (4 stacked sceTGcmo ticks)
would surface and fix it in one wake.

## ORDER 020 · update 2026-07-12T21:58Z · status: ✅ DONE (amendment — I7 TICK-PILE-UP; fleet-manager PR #142)
priority: P1 (unchanged)
do: (append-only DONE flip for the 19:20Z TICK PILE-UP amendment above — no new work
ordered; executed by the successor coordinator, boot 2026-07-12 ~20:30Z, session
continuous.)
why: the amendment's done-when is met — the wake ritual now flags >1 same-session
pending near-identical work-loop one-shots as PILE-UP with prune-to-newest named,
and replaying tonight's registry surfaces the stacked sceTGcmo ticks in one wake.
done-when: (met in fleet-manager PR #142)
✅ DONE:
- TICK PILE-UP added to scripts/check_trigger_health.py as invariant I7 (>1 pending near-identical work-loop one-shot on one session = FAIL; remedy prune-to-newest, recorded in roster health + status.md) — PR #142.
- Fresh registry export committed (telemetry/triggers-snapshot.json, captured_at 2026-07-12T20:41:13Z, 945 records); I7 first evaluation: PASS — no live pile-up (post-prune registry clean; the two same-session SWTK long-fuse checkpoints correctly exempted as distinct deliverables). Replay proof: the pre-prune 18:25:51Z snapshot reds I7 on the incident's 4 stacked sceTGcmo pacemaker ticks with prune-to-newest named — the amendment's done-when.
- Pacemaker discipline relayed 2026-07-12 ~20:55Z via send_message: DELIVERED to substrate-kit (active); websites / game-lab / ideas-lab / superbot-world / venture-lab were INACTIVE (`session_inactive`) — durable copy lives in docs/playbook.md (R26 note); inactive seats pick it up from fm HEAD on next wake. Capability finding appended to docs/CAPABILITIES.md.

## ORDER 023 · 2026-07-12T22:09Z · status: new — GATED: do NOT execute until the owner approves the consolidation plan (owner-queue E#44 / OQ-CONSOLIDATION-DELETE-VS-ARCHIVE letter — the plan's product-forge lane gate)
priority: P1 — consolidation Phase 1 (blocks the owner's Phase 3.1 archive click, B#40 / OQ-CONSOLIDATION-ARCHIVE-FORGE)
owner: Websites seat (route via the manager's next dispatch) — the RECEIVING lane; product-forge is DARK per docs/roster.md gen #21 and never receives ORDERs
do: Rehome product-forge `products/games-web/` per docs/planning/2026-07-12-repo-consolidation-plan.md § "Phase 1 — ORDER P1-1": move the self-contained static character-sheet game UI + `game-state.schema.json` v1.0.1 contract + tests out of menno420/product-forge (forge content is readable cross-repo; execute from the destination side, never as a forge session). Decision criterion (plan/census): FIRST check the websites Fleet Arcade catalog (the slice shipped in websites `06409f5`) — if games-web can host as a playable catalog entry unchanged, land it in the websites arcade; if the right home is instead a bot-game plugin surface, do NOT land it in websites — record that call in your status so the manager re-routes to the superbot-world seat (superbot-games). Record the decision + criterion in the PR body either way.
why: Phase 1 rehoming must land before the Phase 3.1 archive toggle freezes product-forge (plan § Phase 1; archive is sequenced strictly after the migrations).
done-when: games-web + schema + tests live and green in the target repo (or the superbot-games re-route call is recorded for the manager); the new home is recorded manager-side for product-forge's final-status pointer at the Phase 3 close-out; a status report lands in the websites lane's control/status.md heartbeat per its seat grammar.

## ORDER 024 · 2026-07-12T22:09Z · status: new — GATED: do NOT execute until the owner approves the consolidation plan (owner-queue E#44 letter — same forge lane gate as ORDER 023)
priority: P2 — consolidation Phase 1 (rides before the B#40 archive click; small docs-only rehome)
owner: fleet-manager seat (this repo — the RECEIVING lane; product-forge is DARK and never receives ORDERs)
do: Rehome the product-forge retro per docs/planning/2026-07-12-repo-consolidation-plan.md § "Phase 1 — ORDER P1-3": move product-forge `docs/retro/2026-07-11-self-review.md` into fleet-manager `docs/retro/` (read it cross-repo from forge main; docs-only PR here).
why: the retro is fleet memory the plan names for rehoming before the forge archive click (plan § Phase 1).
done-when: the file is merged in fleet-manager docs/retro/ with a Status badge + an index/README link (repo doc gate green); a status report lands in this lane's control/status.md heartbeat per its seat grammar.

## ORDER 025 · 2026-07-12T22:09Z · status: new
priority: P1 — consolidation Phase 1 (blocks the owner's Phase 3.2 archive click, B#41 / OQ-CONSOLIDATION-ARCHIVE-SONNET5)
owner: self-improvement seat (substrate-kit) (route via the manager's next dispatch)
do: Port the two codetool-lab-sonnet5 writeups per docs/planning/2026-07-12-repo-consolidation-plan.md § "Phase 1 — ORDER P1-4": (1) the v0.1.1 release-decision writeup and (2) the differential-testing method doc ("corpus vs a reference parser found 3 real bugs behind green tests") from menno420/codetool-lab-sonnet5 into substrate-kit — the census names kit-lab benchmark practice (substrate-kit `bench/` docs) as the differential-testing home; the release-decision writeup rides with it.
why: the two writeups are the sonnet5 assets the plan rehomes before its archive click (plan § Phase 1; archiving is sequenced strictly after migration).
done-when: both docs merged in substrate-kit; a pointer to their new home is recorded for sonnet5's final status (via the manager if the sonnet5 lane stays wound down — it is STALE-BY-DESIGN); a status report lands in the substrate-kit lane's control/status.md heartbeat per its seat grammar.

## ORDER 026 · 2026-07-12T22:09Z · status: new
priority: P1 — owner-directed archive precondition (blocks the owner's Phase 3.3 archive click, B#42 / OQ-CONSOLIDATION-ARCHIVE-FABLE5)
owner: codetool-lab-fable5 lane (any wind-down session on that repo; the lane is STALE-BY-DESIGN per docs/roster.md gen #21 — not DARK — route via the manager's next dispatch/wake)
do: Repo-hygiene precondition per docs/planning/2026-07-12-repo-consolidation-plan.md § "Phase 1 — ORDER P1-5": remove the committed `__pycache__/*.pyc` under `src/envdrift/commands/` and add the missing top-level `.gitignore` (both verified in tree @ `a6cf1a9`). Owner directive, verbatim per the plan: "fix fable5's committed .pyc files + missing .gitignore before archiving".
why: owner-directed precondition — the archive toggle freezes the tree, so the hygiene fix must land first (plan § Phase 1).
done-when: `git ls-files '*.pyc'` is empty; `.gitignore` exists at repo root; CI green; a status report lands in the fable5 lane's control/status.md heartbeat per its seat grammar.

## ORDER 027 · 2026-07-12T22:09Z · status: new
priority: P2 — consolidation Phase 1 (stranded-PR disposition; minutes of work)
owner: superbot-world seat (superbot-mineverse) (route via the manager's next dispatch)
do: Close (not merge) Codex PR #31 on menno420/superbot-mineverse per docs/planning/2026-07-12-repo-consolidation-plan.md § "Phase 1 — ORDER P1-6", with a one-line disposition comment: its two findings were fixed by merged #42 (`3591c77`) and dispositioned by #43 (`f8b6dbf`). The plan verified #31 still open on 2026-07-12 (state open, mergeable_state blocked, created 2026-07-11T16:41Z) — re-verify at execution time and stand down if already closed.
why: #31 is superseded stranded work; closing it clears the seat's PR queue before the consolidation end-state (plan § Phase 1).
done-when: superbot-mineverse #31 is closed with the disposition comment; a status report lands in the mineverse lane's control/status.md heartbeat per its seat grammar.

## ORDER 028 · 2026-07-12T22:09Z · status: new
priority: P2 — consolidation Phase 1 (must complete before the owner's Phase 3 archive clicks B#40–42)
owner: fleet-manager seat (this repo)
do: Codetool findings-export coverage check per docs/planning/2026-07-12-repo-consolidation-plan.md § "Phase 1 — ORDER P1-7": confirm the three codetool labs' (sonnet5 / fable5 / opus4.8) succession + retro content is fully covered by superbot `docs/eap/gen1-grand-review-2026-07-09.md` + fleet-manager `docs/experiments/harness-x-model-2026-07-09.md`; export any gap into its durable home before the archive clicks.
why: the archive toggles freeze the lab repos read-only — any uncovered finding must be exported first (plan § Phase 1).
done-when: a one-paragraph coverage verdict lands in the owner-queue thread or the plan's follow-up (naming any gap exported and where); a status report lands in this lane's control/status.md heartbeat per its seat grammar.

## ORDER 029 · 2026-07-12T22:12Z · status: standing — owner directive in force on receipt (fleet-wide record; no single-lane execution queue)
priority: P0 — landing doctrine, effective immediately, fleet-wide
owner: all seats (manager relay — recorded on the bus so every lane reads it at its next wake)
do: RECORD + APPLY the owner live directive, verbatim: "you and all your agents should always merge every PR thats ready". Provenance: owner live, fleet-manager coordinator chat, 2026-07-12T22:04Z. Effect: a PR that is READY (non-draft) with every required check COMPLETED green is MERGED by the agent/lane that owns it (squash), citing this directive — parking READY+green PRs for an owner click is no longer the default landing. Designed holds are unchanged: a `do-not-automerge` label, a GATED order (e.g. ORDERs 023/024 above), red or incomplete required checks, and owner-only walls (workflow-file PRs, settings toggles) still hold.
why: owner live directive 2026-07-12T22:04Z — parked-green PRs were accumulating owner clicks the owner does not want to make.
done-when: recorded; landing doctrine updated — this block is on the bus at HEAD, and each seat cites the directive when self-merging from its next wake onward.

## ORDER 030 · 2026-07-13T00:01Z · status: new
priority: P1 — TONIGHT'S finalization mandate
owner: SuperBot 2.0 seat (superbot-next + superbot prod)
do: Owner's words, verbatim: "as much finalization as possible gets done tonight, all finished features properly implemented, simulations and reviews done to find out which commands and buttons should be kept or reworked, at least the full core and all admin and setup functions fully complete and production ready ... I want everything working as intended, and as finished and finetuned as possible" — live testing follows later; the mandate now is completeness + polish. Includes the build side of the minigame/casino consolidation: one section, games grouped, guild-configurable enable-all-or-pick-a-few, panels updating dynamically to the enabled set ("this is more a job for superbot-next, and mostly already exists") — consume SuperBot World's inventory/spec (ORDER 031). Context: these goals are being consolidated into a fleet grounding doc by the hub venue (superbot docs/owner/fleet-grounding.md, pending commit) — read it when it lands.
why: owner goals message — owner live in the fleet-manager coordinator chat, 2026-07-13T00:1xZ.
done-when: finalization sweep lands as green PRs; an evidenced KEEP/REWORK/DROP verdict exists per command/button; core+admin+setup surfaces each report implemented+tested+production-ready; status report in the seat heartbeat.

## ORDER 031 · 2026-07-13T00:01Z · status: new
priority: P1 — games finalization + casino inventory/spec
owner: SuperBot World seat (superbot-games + superbot-idle + superbot-mineverse)
do: Owner's words, verbatim: "finalize the mining game completely as a standalone game, with integration in the exploration/world hub" — review end-to-end first, then extend/improve wherever possible; "same for fishing and the idle game". Card games and all minigames consolidated "into one minigame/casino section" with expanded options ("any kind of minigame they can add should be there"), in sections with enable-all-or-pick-a-few and dynamically updating panels — this seat owns the game inventory, section spec, and per-game readiness; the panel build is superbot-next's (ORDER 030): publish the spec for it via heartbeat/outbox. Context: these goals are being consolidated into a fleet grounding doc by the hub venue (superbot docs/owner/fleet-grounding.md, pending commit) — read it when it lands.
why: owner goals message — owner live in the fleet-manager coordinator chat, 2026-07-13T00:1xZ.
done-when: mining/fishing/idle each have a review+finalize+improve report and landed PRs; the casino inventory+spec is published and referenced in the heartbeat.

## ORDER 032 · 2026-07-13T00:01Z · status: standing
priority: P2 — endless idea cycle (standing)
owner: Ideas Lab seat (idea-engine + sim-lab)
do: Owner's words, verbatim: "keeps producing and testing an endless cycle of ideas for any of the repos or completely unrelated to anything" — continuous harvest→probe→verdict→outbox; SIM-REQUESTs from build seats are priority intake; verdicts route only through the manager. Context: these goals are being consolidated into a fleet grounding doc by the hub venue (superbot docs/owner/fleet-grounding.md, pending commit) — read it when it lands.
why: owner goals message — owner live in the fleet-manager coordinator chat, 2026-07-13T00:1xZ.
done-when: standing — each wake's heartbeat shows cycle throughput (ideas produced/tested/verdicts finalized), honest nulls included.

## ORDER 033 · 2026-07-13T00:01Z · status: standing
priority: P2 — both Venture Lab lanes continue (standing)
owner: Venture Lab seat (venture-lab + trading-strategy)
do: Continue BOTH lanes. Products, owner's words verbatim: "complete as many finished books and sellable products as possible"; "come up with multiple new book ideas as well as write multiple versions of each book"; website-shaped ideas get an explicit WEBSITE-IDEA outbox marker for the manager to route to Websites. Trading, verbatim: "find more strategies to backtest, as well as more stocks, more indicators" — expand the surface continuously, record every result honestly including nulls. Context: these goals are being consolidated into a fleet grounding doc by the hub venue (superbot docs/owner/fleet-grounding.md, pending commit) — read it when it lands.
why: owner goals message — owner live in the fleet-manager coordinator chat, 2026-07-13T00:1xZ.
done-when: standing — per-wake shipped/publish-READY counts, new book ideas + versions, WEBSITE-IDEA markers, and backtest-surface growth in the heartbeat.

## ORDER 034 · 2026-07-13T00:01Z · status: new
priority: P2 — self-thinking research + skill-pack mechanism
owner: Self Improvement seat (substrate-kit)
do: Continue current direction and fold in today's lessons. Owner research mandate, verbatim: "spend more time into finding out how we can let the sessions actually think more for themselves" — rationalize whether actions should ALSO be executed; turn lessons/ideas into permanent solutions; agents "eager to initiate helpful actions"; build the mechanism that "makes agents self initiate structural durable improvement" — a skill-pack method: baked lessons loadable on demand ("prevents it from taking up too much storage in the CLAUDE.md itself, but is still always loadable on demand"), so no session re-discovers problems/workarounds. Seed skills to generalize (verify at superbot HEAD, .claude/skills/, provenance Q-0273): chase-references (resolve every link/name/reference in an ask before acting) and prep-owner-steps ("lead with the link and the copy/paste ready file in chat as a separate block" — map the owner's exact steps, ship every blob he must enter paste-ready). Context: these goals are being consolidated into a fleet grounding doc by the hub venue (superbot docs/owner/fleet-grounding.md, pending commit) — read it when it lands.
why: owner goals message — owner live in the fleet-manager coordinator chat, 2026-07-13T00:1xZ.
done-when: research findings + a shipped or concretely planned kit mechanism reported in the heartbeat; seed skills generalized into kit templates or an evidenced reason why not yet.

## ORDER 035 · 2026-07-13T00:01Z · status: standing
priority: P2 — websites quality bar + self-initiated builds (standing)
owner: Websites seat
do: Owner's words, verbatim: "continue with all they're doing" — control plane, pod websites, Anthropic review website. The quality bar, verbatim: "every website is properly, efficiently created. so that every page shows you immediately what it is, what it does, and the most important features that it has" — audit every live page against this and fix misses. Also, verbatim: "scan the repos and initiate anything that might be able to be done as a website"; execute the existing plan and "not stop until it's all done. And, actually, well made". Context: these goals are being consolidated into a fleet grounding doc by the hub venue (superbot docs/owner/fleet-grounding.md, pending commit) — read it when it lands.
why: owner goals message — owner live in the fleet-manager coordinator chat, 2026-07-13T00:1xZ.
done-when: standing — clarity-bar audit results, plan progress, and self-initiated builds in each heartbeat.

## ORDER 036 · 2026-07-13T00:01Z · status: new
priority: P2 — mass game production beyond GBA/NDS
owner: Game Lab seat (gba-homebrew + pokemon-mod-lab)
do: Owner's words, verbatim: "focus on producing multiple different games ... produce in mass" like Venture Lab — multiple things to test, try out, "maybe even things we can sell"; "not just stick to only the GBA game or NDS, Pokemon games ... make web browser games, or try to make the foundations or plans for actual mobile games" — browser games coordinate with Websites (arcade home); mobile = framework choice + pipeline + running skeleton or an evidenced wall. Context: these goals are being consolidated into a fleet grounding doc by the hub venue (superbot docs/owner/fleet-grounding.md, pending commit) — read it when it lands.
why: owner goals message — owner live in the fleet-manager coordinator chat, 2026-07-13T00:1xZ.
done-when: current tracks keep shipping AND new prototypes/concepts appear per wake (playable slice + one-page concept incl. sellability guess), reported in the heartbeat.

## ORDER 019 · update 2026-07-13T00:10Z · status: ✅ DONE (review site refreshed + live; verified by the manager's sweep)
priority: P1 (was time-sensitive — EAP review window)
do: (append-only DONE flip for ORDER 019 above — no new work ordered; evidence
verified live 2026-07-12T22:1x–22:2xZ by the manager's sweep; recorded by the
coordinator's consolidation-batch worker.)
why: the ORDER's done-when is met — the live review site serves 2026-07-12 data
including the scheduler incident and the 8-seat fleet content.
done-when: (met) live URL shows 07-12 data + incident + 8-seat content.
✅ DONE: review-production-f027 live-fetched and confirmed serving 2026-07-12
data / incident / 8-seat content (bake commit a513ff4). Websites heartbeat
aafad91 records "019/021/022 all DONE".

## ORDER 021 · update 2026-07-13T00:10Z · status: ✅ DONE (web-presence /directory live; verified by the manager's sweep)
priority: P2 (unchanged)
do: (append-only DONE flip for ORDER 021 above — no new work ordered; evidence
verified live 2026-07-12T22:1x–22:2xZ by the manager's sweep; recorded by the
coordinator's consolidation-batch worker.)
why: the ORDER's done-when is met — the directory page is live on the
control-plane, rendered from a committed registry.
done-when: (met) /directory live.
✅ DONE: /directory verified live (websites PR #198, c51d6e7). Websites
heartbeat aafad91 records "019/021/022 all DONE".

## ORDER 022 · update 2026-07-13T00:10Z · status: ✅ DONE (arcade card LIVE + env page verified + OWNER-ACTIONS reconciled; verified by the manager's sweep)
priority: P1 (unchanged; item 3 was already OBSOLETE per the 18:00Z amendment)
do: (append-only DONE flip for ORDER 022 above — no new work ordered; evidence
verified live 2026-07-12T22:1x–22:2xZ by the manager's sweep; recorded by the
coordinator's consolidation-batch worker.)
why: the ORDER's remaining items (1, 2, 4) each verify done live; item 3 was
struck by the 18:00Z amendment (owner clicked both Actions toggles).
done-when: (met) arcade card live + honest; env page verified; OWNER-ACTIONS
carries zero satisfied-but-open asks.
✅ DONE: arcade mineverse card LIVE (websites PR #197, 41d3526); the
/owner/environments live half verified (websites PR #210); OWNER-ACTIONS
reconciled (websites PR #214). Websites heartbeat aafad91 records
"019/021/022 all DONE".

## ORDER 037 · 2026-07-13T00:10Z · status: new
priority: P2 — roster hygiene (one-line fix; unblocks a measurable roster row)
owner: SuperBot World seat (superbot-games; route via the manager's next dispatch)
do: Repair the malformed `updated:` stamp in superbot-games
`control/status-mining.md` — the current value reads
"2026-07-11T (archive-prep…", which is unparseable, so the roster's mining
sub-row cannot be measured. One-line fix: restore a full ISO8601 UTC stamp on
the `updated:` line per the seat heartbeat grammar.
why: the roster regen reads the stamp to compute freshness; an unparseable
stamp makes the sub-row unmeasurable and hides real staleness.
done-when: roster regen shows a parsed verdict for the mining sub-row.

## ORDER 038 · 2026-07-13T00:10Z · status: standing
priority: P1 — review-integrity gate, fleet-wide (manager relay — recorded on the bus so every lane reads it at its next wake)
owner: all seats
do: Adopt sim-lab VERDICT 016 (sim-lab PR #58, squash 0d64f36) as a MANDATORY
pre-trust authenticity gate on every @codex (or any cross-agent reviewer)
reply BEFORE acting on it: run the VERDICT 016 authenticity checks (e.g. every
cited line range must be ≤ EOF of the cited file at the reviewed head) and
treat any reply that fails as fabricated — do not act on it. Evidence: the
gate caught 3/3 fabricated replies with 0/24 false alarms; all three
fabrications fail the line-range≤EOF check alone. This REPLACES outright
suspension of cross-agent review — Q-0120 (verify-never-obey: a reviewer
reply is input to verify against shipped source, never an order) still
governs everything that passes the gate. Provenance: manager decide-and-flag
2026-07-13, owner-vetoable.
why: fabricated reviewer replies were indistinguishable from real ones until
sim-lab VERDICT 016 produced a cheap, evidenced authenticity check; gating
beats suspending a review channel the owner rates highly.
done-when: standing — each seat applies the gate from its next wake onward and
cites it when discarding a failed reply; playbook R24 carries the gate as
doctrine (amended in the PR that filed this ORDER).

## ORDER 039 · 2026-07-13T00:40Z · status: standing
priority: P0-tonight — owner night-run directive, in force on receipt
owner: Fleet Manager seat (the rules within bind all seats)
do: Execute the owner's night-run directive, recorded VERBATIM below.
why: owner live in the fleet-manager coordinator chat, 2026-07-13T00:4xZ (top-precedence owner turn).
done-when: morning tally (~06:00Z) posted in heartbeat + outbox per the directive.

```
DIRECT ORDER — FLEET MANAGER (owner, 2026-07-13, night run). Land this verbatim in your
inbox (top-precedence owner turn), then execute all night.

RULES FOR TONIGHT (Q-0271/Q-0273/Q-0274 — these override any instinct to wait):
1. I am away until morning; that is the system's normal state. Silence = consent = done.
   Never hold or re-confirm finished work.
2. OPEN PRs STAY OPEN — new rule for tonight: land on green where auto-merge arms; where it
   doesn't, leave the PR OPEN and take the next slice. No merge-chasing, no parking-and-
   waiting, no counting open PRs as blockers — I sweep them when I'm back (VENUE:hub). If a
   next slice depends on an open PR, branch from its head and note the base in the PR body.
3. FIND YOUR WORK, in order: your inbox at HEAD → superbot docs/owner/fleet-grounding.md §2
   (my mission + ordered goals for you) → your playbook/backlog at HEAD → your generative
   rung. An empty queue means GENERATE, never idle.
4. NO STALLS UNDER ANY CIRCUMSTANCES: probe before declaring a wall (attempt once, verbatim
   error; quote fresh documented walls instead of re-probing); genuinely-owner-only item →
   six-field owner-queue entry (VENUE:hub if merge/destructive-shaped) → CONTINUE same turn;
   design/feasibility uncertainty → SIM-REQUEST via outbox → CONTINUE.
5. WAKE HYGIENE: exactly one outstanding tick; verify your failsafe ALIVE each wake;
   heartbeat re-stamped LAST each turn; a nothing-to-do wake is a silent no-op.
6. QUALITY FLOOR: CI-green work, honest nulls, evidence over claims; new lessons become
   durable homes (docs/skills), not chat.
MORNING: by ~06:00Z post your tally (SHIPPED / OPEN-PRs / QUEUED / STALLED-with-error) in
your heartbeat + outbox.

YOUR SEAT TONIGHT (you already dispatched my goals as ORDERs 030–036 — good; now run the
night on top of them):
1. WATCHDOG every wake (R26): trigger-health on a fresh export, FAILs acted on same wake;
   any dark seat send_message-revived.
2. TRACK the night: per-seat progress against the 030–036 goals in the roster; stuck-list
   doctrine stands (a genuinely stuck PR gets its blocker named and stops costing attention;
   the pipeline never pauses on it — gba #76 included: queue my 1-click, move on).
3. ROUTE within one wake: verdicts → build seats · SIM-REQUESTs → Ideas Lab · WEBSITE-IDEA
   markers → Websites · World's minigame section spec → SuperBot 2.0.
4. OWNER-QUEUE: verify-first curation all night; VENUE:hub tagging; the ≤07-13 sitting
   bundle + the three one-reply unblocks stay paste-ready at the top.
5. Keep folding the autonomy rider + the two superbot seed skills into your v3 prompt
   sources so the next restamp inherits them.
6. MORNING ROSTER ~06:00Z: per-seat tallies + dropped-tick report + the ROUND-TRIP flag.
```

Manager annotation (post-receipt): gba #76 had already MERGED (0e08695) before this
order arrived — the "gba #76 included: queue my 1-click, move on" clause is satisfied
on the merge side; its remaining owner click is OQ-GBA-ROM-RULESET (B#51).

## ORDER 040 · 2026-07-13T01:32Z · status: standing
priority: P0-tonight — owner final night order, in force on receipt
owner: Fleet Manager seat
do: Execute the owner's final night order, recorded VERBATIM below.
why: owner live in the fleet-manager coordinator chat, 2026-07-13T01:2xZ (top-precedence owner turn).
done-when: TASK 1 v3.5 bodies on main + skim doc; TASK 2 ORDER dispatched; TASK 3 R-rule in playbook + morning roster carries idle-state + rung record.

```
DIRECT ORDER — FLEET MANAGER (owner, 2026-07-13, final order of the night). Land this
verbatim in your inbox (top-precedence owner turn), then execute. Q-0271 rules stand all
night: silence = consent; open PRs stay open, production continues; probe before any wall;
six-field ⚑ + VENUE:hub for anything genuinely mine; never idle.

CONTEXT — WHERE THE HUB STORED TONIGHT'S PROMPTS AND DOCTRINE (all in menno420/superbot,
read via raw; the router Q-blocks are Q-0271…Q-0274):
- docs/owner/fleet-rearm-2026-07-12.md — the AUTONOMY RIDER (§3, Q-0271) + 8 re-arm blocks.
- docs/owner/fleet-night-orders-2026-07-12.md — NIGHT ORDERS v2 (owner-revised goals,
  Q-0273) + the venue correction (§0b, VENUE:hub).
- docs/owner/fleet-direct-orders-2026-07-13.md — the 8 DIRECT ORDER blocks (the shared
  skeleton + the OPEN-PRs-STAY-OPEN night rule; these were pasted to every seat tonight).
- docs/owner/fleet-grounding.md — the living grounding file (Q-0274: missions, venue model,
  per-seat goal ladders — you reviewed it pre-commit).
- docs/owner/curious-research-project-prompts-2026-07-13.md — the NINTH SEAT's founding
  pair (Curious Research: the friend's research/teaching repo; failsafe offset 20 */2;
  binding visual-teaching doctrine).
- docs/fleet-reading-path.md + scripts/fleet_status.py — the Q-0272 multi-repo reading path.
- .claude/skills/chase-references/ + .claude/skills/prep-owner-steps/ — the two seed skills
  (Q-0273 self-initiative program; the kit is generalizing them).

TASK 1 — CENTRALIZE → SYNTHESIZE v3.5 (the registry is the canonical prompt home):
1. Pull the artifacts above into your prompt lane and DIFF them against the currently
   active v3.4 bodies (docs/prompts/v3/ + registry), seat by seat.
2. Produce the v3.5 generation: KEEP every proven v3.4 part (the stateless-pointer
   discipline, boot triad, precedence line, born-red card mechanics, landing doctrine,
   walls-quoting, stagger table) and FOLD IN tonight's decided workflow — the Q-0271 rider
   (never-wait, queue-and-continue, six-field ⚑), the open-PRs-stay-open posture as the
   standing default (land on green where auto-merge arms; never merge-chase; stack on open
   heads), the Q-0272 reading path, the Q-0273 venue model (VENUE:hub tagging) + the two
   skills as UNIVERSAL material, the Q-0274 grounding file as boot reading (each seat reads
   its own §), and the Curious Research pair as the ninth registry seat.
3. Ship it the way you shipped v3.4: registry restamp + a kept/changed note per seat +
   version bump — so the next re-paste (website-served) is one sitting.
   DONE-WHEN: v3.5 bodies on main in your registry, drift rows show v3.5 canonical, and a
   one-page "what changed v3.4→v3.5" the owner can skim.

TASK 2 — DISPATCH TO WEBSITES (their inbox, next free ORDER number): make the prompt
versions BROWSABLE and centralized across the site wherever applicable:
- a version history per seat (v3.3 → v3.4 → v3.5: view any version, diff between versions,
  copy button per body) sourced from YOUR registry — single source of truth, the site only
  renders it, never forks it;
- the deployed-vs-canonical drift row stays, now version-aware;
- surface the same prompt data everywhere it helps (the /prompts library, each seat's page
  on the projects/console surfaces, the owner console) as views of ONE source — no
  duplicated prompt copies anywhere in the site.
  DONE-WHEN: any seat's current + historical prompts are two clicks from the site root,
  and every rendering traces to the registry.

TASK 3 — STANDING BACKUP DOCTRINE (you are the fleet's backup when anything fails; this
extends your oversight-only rail with an owner-authorized escalation ladder — for the
idle-lane case only):
Each wake, alongside the ORDER-020 trigger-health sweep, detect IDLE lanes: heartbeat
stale past ~2× its cadence, no fresh commits/PRs, or no armed wake. Escalate in order,
recording each rung in the roster:
  (1) DISPATCH — a fresh, concrete ORDER into the lane's inbox (its 030–036 goals give
      you the material);
  (2) REVIVE — send_message the seat's session; manually fire fresh-session triggers where
      that path works;
  (3) BACKUP-BUILD — if it is still dead at your NEXT wake, send your own worker agents to
      do the lane's next slice directly in the lane repo: claude/* branch, normal PR,
      PR body marked "manager-backup for <seat>", lane conventions respected (their
      CLAUDE.md/kit gates), one slice per worker; keep going until the lane wakes, then
      hand back via its inbox and stop.
  Genuinely-owner-only failures go to the queue (VENUE:hub) — but a lane being asleep is
  never owner-only anymore: you are the backup.
  DONE-WHEN: the ladder is in your playbook (R-rule), ran at least once tonight if any
  lane qualifies, and the morning roster shows per-lane idle-state + which rung fired.

Morning line (~06:00Z): add to your roster report — v3.5 state, the Websites ORDER number,
and the backup-ladder record.
```

Manager annotation (post-receipt): v3.5 stage-1 fold (Q-0271 rider + seed skills) already
shipped pre-order as PR #151 @ 728dc07; TASK 1 completes the generation.

## ORDER 041 · 2026-07-13T01:32Z · status: new
priority: P1
owner: Websites seat
do: Make the fleet prompt versions BROWSABLE and centralized across the site wherever
applicable — TASK 2 of the owner's final night order (ORDER 040 above), scope verbatim:
a version history per seat (v3.3 → v3.4 → v3.5: view any version, diff between versions,
copy button per body) sourced ONLY from the fleet-manager registry (docs/prompts/v3/ +
projects/<seat>/ copies) as the single source of truth — the site only renders it, never
forks it; the deployed-vs-canonical drift row stays, now version-aware; surface the same
prompt data everywhere it helps (the /prompts library, each seat's page on the
projects/console surfaces, the owner console) as views of ONE source — no duplicated
prompt copies anywhere in the site.
why: owner final night order 2026-07-13 TASK 2 (ORDER 040, owner live in the coordinator
chat 2026-07-13T01:2xZ).
done-when: any seat's current + historical prompts are two clicks from the site root;
every rendering traces to the registry; status report in the websites heartbeat.

## ORDER 042 · 2026-07-13T05:00Z · status: new
priority: P1 — route venture-lab WEBSITE-IDEA markers (night batch 1)
owner: Websites seat
do: Route venture-lab's two WEBSITE-IDEA markers (venture-lab control/outbox.md
"night-run batch 1", ~2026-07-13T01:49Z) into the site, built per ORDER 035's clarity
bar: (1) "The Puddle Museum" interactive kids site / book marketing page (source: books
lane, venture PR #105 packet); (2) a static catalog-storefront auto-generated from
venture docs/publishing/vetting/*.md + OWNER-QUEUE.md (the vetting pipeline is already
structured data). MANAGER NOTE (sweep evidence, 04:5xZ): the seat appears to have
pre-built both on its own initiative — websites #247 (/puddle-museum, merged 04:25:44Z)
and #248 (/products/catalog over the 22 vetting packets @ venture 2c039e3, merged
04:17:31Z) — so the expected first act is VERIFY those two pages against this order's
scope and report, not rebuild.
why: manager routing of ORDER 033's WEBSITE-IDEA lane (venture outbox markers exist for
exactly this fan-out); morning-tally dispatch per ORDER 039/040.
done-when: both sites/pages exist (or are explicitly triaged-with-reason) and the
websites heartbeat says so, citing the PRs.

## ORDER 043 · 2026-07-13T05:00Z · status: new
priority: P1 — SIM-REQUEST priority intake (two build-seat asks)
owner: Ideas Lab seat (idea-engine + sim-lab)
do: Priority-intake two build-seat SIM-REQUESTs per ORDER 032 ("SIM-REQUESTs from build
seats are priority intake"): (1) venture-lab's serialized-fiction pricing feasibility —
Ultramarine 3-part serial at $2.99/episode vs $3.99–$5.99 single volume (venture-lab
control/outbox.md "night-run batch 1", ~01:49Z; packet detail in venture PR #109);
(2) superbot-idle's SIM-001 follow-up — economy-FEEL cluster, three asks: first-upgrade
no-op at low counts, weak prestige payoff (ratio 0.9175 for a 3.49h grind), and the A10
strict-vs-trend ruling + PROVISIONAL-table graduation (superbot-idle control/outbox.md
2026-07-13 SIM-REQUEST entry, ref docs/design/economy-v1.md § SIM-001/Q-0264).
why: ORDER 032 standing priority-intake rule; both asks surfaced via lane outboxes
tonight and route only through the manager.
done-when: verdicts posted to the requesting seats via the manager fan-in (manager
relays each verdict pointer to venture-lab's and superbot-idle's inboxes); cycle ledger
shows both intakes.

## ORDER 044 · 2026-07-13T08:58Z · status: new
priority: P1 — SIM-REQUEST priority intake, batch 2 (seven build-seat asks)
owner: Ideas Lab seat (idea-engine + sim-lab)
do: Priority-intake SEVEN batch-2 SIM-REQUESTs per ORDER 032 ("SIM-REQUESTs from build
seats are priority intake"), sequenced AFTER ORDER 043's two (already relayed as
idea-engine local ORDER 005, 07:51Z — do not duplicate those). Venture pricing (3 —
packet: venture-lab control/outbox.md "night-run MORNING TALLY", ~05:00Z; product
listings/gates in venture docs/publishing/OWNER-QUEUE.md):
(1) photo packs — PWYW-vs-$5, a $3 anchor, and a two-pack bundle (note the packs are
HARD-GATED on owner-held originals; pricing verdict is still serveable now);
(2) Ship-It Bundle — $59 vs $64/$68 anchor points;
(3) narrow-TAM cookbooks — $19 fixed vs PWYW (canonical case: Merge-Wall Cookbook $19).
Superbot-games balance (4 — packet: superbot-games control/outbox.md @ HEAD, all four
marked status: open, each with verbatim-pinned constants + per-request module pointers):
(4) mining-economy-tuning — surface descend-gate shape (depth_access-only gating;
games/mining/core/world.py + equipment.py) + faucet/sink gap (rewards/items vs
market.GEAR_SHOP + structures._FORGE_BUILD_LADDER);
(5) fishing-economy-tuning — pin a per-species sell/reward curve + a fishing progression
curve (games/fishing/inventory/adapter.py empty ProgressionDelta; re-run the pinned
games/fishing/sim/catch_sim.py under new targets per docs/design/fishing-catch-skeleton.md §5);
(6) dnd-escort-double-mint — one traversal mints the safe_passage escort bundle 2×
(games/dnd/core/effects.py _escort_step wired to two options in games/dnd/data/scenes.py);
intended, or mint-at-most-once?
(7) exploration-reward-bands — reconcile games/exploration/quest/catalog.py TIER_CAPS
placeholders against the real Q-0087 dual-track bands + ratify the survival Medium/Hard
gradient (games/exploration/survival/difficulty.py).
Prior art: sim-lab sims/verdict-017-t10-cost-curve/ (cost-curve method) and
sims/verdict-006-idle-economy-sim-kernel/ for the economy asks.
why: ORDER 032 standing priority-intake rule; all seven surfaced via lane outboxes in the
batch-2 sweep (venture morning tally ~05:00Z; games outbox @ HEAD) and route only through
the manager. Venture's fourth tally ask (owner sandbox repo) is owner-gated, routed to
docs/owner-queue.md B#54 (OQ-VENTURE-SANDBOX-REPO), not to this order.
done-when: verdicts posted via the Ideas Lab outbox to the manager, each naming its
requesting seat (venture-lab · superbot-games), for manager relay to the requesting
inboxes; cycle ledger shows all seven intakes.

## ORDER 028 · update 2026-07-13T13:05Z · status: ✅ DONE (codetool findings-export coverage check; this wake's PR)
priority: P2 (unchanged)
do: (append-only DONE flip for ORDER 028 above — no new work ordered; this
block records the execution, fields per the kit's order grammar; written by
the 2026-07-13 FM wake work session as manager delegate.)
why: the ORDER's done-when is met — a coverage verdict naming the one gap and
its export path landed in the plan's follow-up section.
done-when: (met) one-paragraph coverage verdict in the plan's follow-up,
naming any gap and where it exports.
✅ DONE: verdict at docs/planning/2026-07-12-repo-consolidation-plan.md
§ "Follow-up — ORDER P1-7 coverage verdict (2026-07-13)". Summary: the three
labs' succession/retro content is COVERED — grand-review second-hand synthesis
(wind-down audit ✅×4, per-arm PR audit, release-route reconciliation) + the
experiments README/harness-doc contamination caveats — with ONE already-tracked
gap: sonnet5's differential-testing method + v0.1.1 release-decision writeups
are NOT yet in substrate-kit (zero hits at kit HEAD `d916d94`, 2026-07-13);
that export IS open ORDER 025 / plan P1-4, which the B#41 archive click
already gates on. Lab HEADs read: sonnet5 `66c3dfc` · fable5 `a6cf1a9` ·
opus4.8 `80f6cd1`. No new export needed; remaining lab content is
tool-internal and stays readable post-archive.

## ORDER 045 · 2026-07-13T21:38Z · status: open
priority: P0 — EAP final night (the program window closes after tonight)
owner: Fleet Manager seat (this session's PR executes Phases 1+2; Phase 3 fans out)
provenance: owner directive, live in the FM coordinator chat 2026-07-13 ~21:34Z.
do: Owner's words, VERBATIM: "I want you to find out the current state of all repos and
dispatch instructions for all projects so they know what to do, find out if there still
need to be improvements made in existing features or else if the idea lab made any good
plans etc. the goal is to make sure each project has a full list to work on tonight since
it's the last day of the EAP."
Phase 1+2 (sweep + worklist synthesis) executing in this session's PR
(docs/eap-final-night-worklists-2026-07-13.md); Phase 3 (lane fan-out) is a follow-up
dispatch.
why: owner directive 2026-07-13 ~21:34Z — last day of the EAP; every project needs a full
worklist for tonight.
done-when: the worklists doc is on main with a prioritized list per active seat + DARK
dispositions + fleet summary; Phase 3 fan-out dispatched to the lane inboxes.

## ORDER 045 · update 2026-07-13T21:59Z · status: open — amendment 1 (pokemon-mod-lab reactivated by owner override)
priority: P0 (unchanged)
owner: Fleet Manager seat (unchanged)
do: ADD pokemon-mod-lab to ORDER 045's active-seat set. Owner override, live in the
FM coordinator chat 2026-07-13 ~21:53Z, VERBATIM: "pokemon mod lab should continue" —
overrides roster gen #35's DARK/UNREADABLE verdict; the seat is treated ACTIVE for
the EAP final-night exercise. Swept read-only post-override at HEAD `759dee4` (local
clone via the fleet git proxy works; the UNREADABLE wall was the terminal-prompt
access path, not the repo). A 6-item worklist added to
docs/eap-final-night-worklists-2026-07-13.md (top item: post-EAP playtest kit, EAP
window closes 2026-07-14). Parked PRs #57–#59/#61–#65 remain owner-sweep-only —
reference notes, never merge work. Include the seat in the Phase 3 fan-out.
why: owner directive supersedes the roster verdict; the seat carries real,
time-critical buildable work tonight.
done-when: (folds into ORDER 045's done-when) the worklists doc carries the
pokemon-mod-lab seat section + fleet-summary row, and the Phase 3 fan-out includes
the seat.

## ORDER 045 · update 2026-07-14T07:57:55Z · status: done — delivery verified, manager flip
priority: P0 (unchanged)
owner: Fleet Manager seat (unchanged)
do: FLIP ORDER 045 to `status: done` — the delivery is verified complete; no
further work rides this order.
why: every done-when clause is SATISFIED (verification below), so the order
must stop reading as open work in the inbox.
verified: live GitHub, 2026-07-14T07:47Z, zero discrepancies. Worklists doc
`docs/eap-final-night-worklists-2026-07-13.md` on fm main @ `1694bfc`
(blob `6c0750c`) with per-seat prioritized lists for 12 seats including the
pokemon-mod-lab amendment-1 section (swept @ `759dee4`), a `## DARK
dispositions` section (6 entries), and a `## Fleet summary` 12-row table
including the pml row. Phase-3 fan-out: 11/11 lane ORDER PRs verified —
10 MERGED 2026-07-13T22:15:55–22:43:26Z (superbot #2090/ORDER 004 merged
22:43:26Z, superbot-next #418, mineverse #84, idle #103, sim-lab #113,
idea-engine #356, trading-strategy #113, venture-lab #168, substrate-kit
#338, websites #306) + pokemon-mod-lab #66 OPEN parked green by design
(mergeable_state clean, ROM builds ✅ + substrate-gate ✅).
done-when: every clause SATISFIED — the worklists doc is on main with a
prioritized list per active seat + DARK dispositions + fleet summary
(including the amendment-1 pml section and row); Phase 3 fan-out dispatched
11/11 to the lane inboxes.
caveat: pml #66 remains OPEN parked green for the owner click alongside
#57–#65 — it IS the delivery itself, not outstanding work.
provenance: coordinator dispatch 2026-07-14, verified live per Q-0120.

## ORDER 046 · 2026-07-15T03:40Z · status: new
priority: P1
do: record + act on the EAP extension — the program is extended through 2026-07-21
(Anthropic mail, Diana Liu, 2026-07-14T23:07:44Z, subject "Claude Code Projects EAP:
Extending to Tues 7/21"; metadata reference only). The 2026-07-14 dormancy orders are
superseded pending the owner's per-project reboot review; see
docs/pre-reboot-review-2026-07-15.md.
why: fm HEAD had no durable record of the extension (record gap found at 94bad42).
done-when: reboot review executed per the doc; extension noted in all lane inboxes.
provenance: landed by the coordinator on live owner directives, 2026-07-15.

## ORDER 027 · 2026-07-15T04:31:54Z · status: done
priority: P2
do: (status flip) mineverse Codex PR #31 found already MERGED — not closed by this pulse; merged 2026-07-12T19:52:53Z by menno420 (before ORDER 027 was filed at 22:09Z), head d66d9a5, adds docs/pre-provisioning-security-report-2026-07-11.md; per the order's stand-down clause the PR was NOT touched; evidence: https://github.com/menno420/superbot-mineverse/pull/31.
why: Consuming the pre-extension backlog during the 2026-07-15 reboot night.
done-when: This entry — terminal.

## ORDER 042 · 2026-07-15T04:31:54Z · status: done
priority: P1
do: (status flip) venture WEBSITE-IDEA routing verified satisfied: websites PR #247 (/puddle-museum, merged 2026-07-13T04:25:44Z) and PR #248 (/products/catalog over the 22 vetting packets @ venture 2c039e3, merged 2026-07-13T04:17:31Z) both exist and are merged, matching the manager note; seat-side confirmation on record — websites control/outbox.md ("fm 042 SATISFIED (both pages verified live 06:29Z)"). Evidence: https://github.com/menno420/websites/pull/247 · https://github.com/menno420/websites/pull/248.
why: Consuming the pre-extension backlog during the 2026-07-15 reboot night.
done-when: This entry — terminal.

## ORDER 026 · 2026-07-15T04:37Z · status: parked-green
priority: P2
do: (status flip) codetool-lab-fable5 hygiene executed: PR #16 parked-green (all 5 CI checks success; repo has no merge-on-green workflow; ORDER 029 merge authority left to owner/another session) — evidence: https://github.com/menno420/codetool-lab-fable5/pull/16 — `git ls-files '*.pyc'` empty on branch; 11 tracked .pyc removed; top-level .gitignore added.
why: Consuming the pre-extension backlog; unblocks owner archive click B#42.
done-when: Owner merges PR #16 then archives.

## ORDER 025 · 2026-07-15T05:06Z · status: done
priority: P1
do: (status flip) sonnet5 writeup port found already MERGED in substrate-kit — kit PR #340 ("Port fm ORDER 025 writeups into bench docs (ORDER 019 item 5)", merged 2026-07-13T23:28:24Z, commit 0e7191d): both writeups live at kit docs/reports/2026-07-09-cfgdiff-differential-testing-method.md (Status `reference`) and docs/reports/2026-07-09-cfgdiff-v0.1.1-release-decision.md (Status `audit`), each carrying a provenance header to source repo menno420/codetool-lab-sonnet5 @ 66c3dfc and linked from bench/README.md § "Method + practice writeups"; kit heartbeat #348 recorded the completion per the seat grammar ("fm ORDER 025 port: #340 merged … Owner's B#41 archive click unblocked"); this entry records the new-home pointer for sonnet5's final status manager-side (the sonnet5 lane stays wound down, STALE-BY-DESIGN). Re-verified file-by-file at kit HEAD e900008, 2026-07-15 — no re-port performed per the stand-down doctrine. Evidence: https://github.com/menno420/substrate-kit/pull/340.
why: executed — all done-when legs met; the B#41 archive click no longer waits on this order.
done-when: satisfied — this entry is terminal.

## ORDER 026 · 2026-07-15T11:39Z · status: done
priority: P2
do: (status flip) codetool-lab-fable5 PR #16 now MERGED live — merged by the owner (merged_by menno420) 2026-07-15T10:54:19Z, head ba88daa (11 tracked .pyc removed + top-level .gitignore added); state read live via the GitHub API this wake, superseding the 04:37Z parked-green entry. Owner-queue A#62 (OQ-FABLE5-PR16-MERGE) swept to Resolved the same pass; B#42 archive click now gates only on the E#46 envdrift letter. Evidence: https://github.com/menno420/codetool-lab-fable5/pull/16.
why: the parked-green header went stale the moment the owner clicked; queue + inbox reconciled together.
done-when: satisfied — this entry is terminal.

## ORDER 046 · 2026-07-15T11:39Z · status: done
priority: P1
do: (status flip) both done-when legs verified: (1) reboot review executed per docs/pre-reboot-review-2026-07-15.md (on disk at HEAD; the v3.6 reboot ran overnight — see control/status.md ledger #215–#229); (2) extension noted in all LIVE lane inboxes, each verified by raw read this wake (11:39Z): substrate-kit control/inbox.md @ 0d79ac52e (line 296) · gba-homebrew @ 0048a5da9 (line 99) · idea-engine @ 828b18ea5 (line 230) · sim-lab @ 17c45585c (line 249) — all carry the "EAP EXTENDED through 2026-07-21" note verbatim. Dormant/parked seats get owner-queue disposition, not ORDERs, so live-lane coverage completes the leg.
why: the 03:40Z header still read `new` after both legs were satisfied; flipping keeps the inbox truthful.
done-when: satisfied — this entry is terminal.
