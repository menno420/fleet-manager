# The router band re-read — superbot:Q-0063–superbot:Q-0272, bodies in full

> **Status:** `audit` · 2026-08-28 · OD-24 review round, **session 2** (the
> genesis dig §11's item 4 — the band session 1 sampled headers-only, which
> verification proved can hide load-bearing owner directives: it hid superbot:Q-0266
> once)
>
> **Method.** superbot stays frozen: one raw API fetch of
> `docs/owner/maintainer-question-router.md` at `main` (668,746 bytes; no
> clone, no write). The band superbot:Q-0063–superbot:Q-0272 — **208 `### Q-`-headed ruling
> sections, whole-population by header regex** (lanes self-reported 210
> bodies read; the +2 is one lane counting unnumbered addendum blocks as
> rulings — the dig's own "210 of 275" headers-only figure is its count by
> its own method, not re-derived here) —
> split into eight whole-ruling chunks, each read **in full** by one reader
> lane (8/8 complete, ~840k subagent tokens), each lane primed with the
> genesis dig and OD-24 and told an honest null is expected. **Every quote below was
> then machine-verified verbatim against the fetched router text: 59/59
> matched** (after markdown/blockquote normalization; the first verification
> query was broken and reported 37 misses — the known-good superbot:Q-0266 quote
> "missing" was the tell, TRAP-003's class, caught before anything was
> recorded). Reader interpretations are `REVIEWED`; quotes are the owner's
> or, where a lane flagged it, the ruling's decision text; "absent from fm"
> claims are lane greps, the six headline ones re-run by the session itself.
> Citations are `superbot:docs/owner/maintainer-question-router.md` at the
> 2026-08-28 fetch, by Q-number.
>
> **The one-paragraph result:** the band holds no reversal of the round's
> direction, but it **narrows seven of the genesis dig's claims** (§1),
> surfaces **a census of standing owner rules with their fm carrier state**
> (§2 — five ABSENT from every fm document, the rest carried only in
> seat-era/reference/raw surfaces or as a different facet of the ruling),
> and gives **owner-ratified genesis precedents for most of the dig's
> gap table** (§3) — including three cases where the genesis system already
> built the exact mechanism a gap row presents as an open design question.
> The dominant pattern: the round keeps re-deriving designs the owner
> already ruled on in June; the router is where those rulings live.

## 1 · What this re-read corrects or narrows in the genesis dig

Each row names the dig claim and the ruling that narrows it. The dig
carries an in-place narrowing pointer **at each affected claim site**
(added on Codex review of fm #959 — the first cut had only generic §9/§11
pointers, which left the superseded readings standing where a later
session would meet them), and its §9 coverage line routes here.

1. **superbot:Q-0083 (06-10) — full self-driving was declared the end-state inside
   the genesis era**, two days after superbot:Q-0015's "not 100% autonomous": *"just
   to be clear, completely self driving is not yet a near term goal, but
   ultimately there will not be much else left to do if I keep implementing
   at the current speed"* — with autonomy tiers granted area-by-area
   **through the router**. Narrows dig §6.2 (which reads the autonomy
   ambition as a July move) and adds ask-channel provenance.
2. **superbot:Q-0107 (06-11) — the REVIEW/grooming loop had a mechanized demand
   structure**: *"After every 10 PRs there should be a docs-only cleanup and
   plan reconciliation"* — owner-amended to 20, auto-fired by
   `reconciliation-trigger.yml` opening a reconcile-labelled issue, with a
   dueness checker. Narrows dig §2's "no machine ever verified any of it":
   the loop's **cadence** was machine-fired; what was prose was the
   substance. (fm's only mention is a dated 07-15 rollout finding.)
3. **superbot:Q-0180 (06-19) — the owner's ratified June design accepted the
   merge-vs-review race**: *"make every final push mention @codex in the PR
   for a forced review"* — post-merge review was chosen **because a
   consumption loop existed** (superbot:Q-0174: next session fixes flagged-real
   first). Narrows the dig's flip-before-review framing (gap #7): the
   owner-precedented defect is the **missing consumption loop**, not merge
   timing itself; fm's never-merge-before-Codex rule is the stricter
   post-close successor, not the only precedent.
4. **superbot:Q-0214 (07-02) — the kit's owner-picked retention posture was
   delete-with-tombstones**, a bounded corpus by construction, with shrink
   duty as checker+routine and a website `/updates` feed as the owner
   surface. Narrows dig §8's "the EAP-era answer to maintain-cost was
   generation + checkers, never fewer files" — and §4's lost-in-extraction
   table has no retention row; whether the kit shipped any of it is
   unexamined (a round question).
5. **superbot:Q-0241's own scope clause — never-wait / silence=consent governed the
   rebuild program only**, with superbot:Q-0213's ask-first brakes left standing for
   production *"until the owner generalizes this"*. Narrows dig §6.2's
   presentation of superbot:Q-0241/PL-002 as his general July intent; whether the
   kit's PL-002 canonicalization preserved that scope is one check the
   round owes.
6. **superbot:Q-0258 (07-10) — Codex was made the standing drainer of the review
   lane mid-program**, in a three-lane ask topology (decide yourself ·
   relay to Codex · owner-queue only for genuinely owner-only). Narrows dig
   §6.2's "Codex on PRs is the one external check added, post-close, by his
   instruction" — the instruction is mid-program, and the topology bears on
   the round's ask-channel design. Related: **superbot:Q-0117 (06-12)** already
   directed an independent-model reviewer between big steps and `main`
   (so the closed loop survived *despite* an owner directive, not for lack
   of one) — and **superbot:Q-0197 (06-22)** shows him retiring that same gate as
   unused friction, the caution for any gap-#7 fix.
7. **superbot:Q-0249 (07-06) — a second approximately-dated owner obligation
   existed**: decide AI-spend caps from *"the average of a couple of
   months"* (window lands ~2026-09-07), where dig §10 calls the ~09-09
   trading gate "the estate's only future-dated obligation". The program
   close likely mooted it — but the mooting was never recorded, which is
   itself the owner-words class the dig tracks. Letter candidate, §4.
   *(Adjacent, not a contradiction: superbot:Q-0223 (07-03) is an owner
   expectation-vs-reality statement about the kit seven weeks before
   OD-21; the dig's "first recorded" claim is Era-3-scoped and stands.)*

## 2 · Standing owner rules and facts, with their fm carrier state

Verbatim-verified, each with its bearing; none is estate-law until the
round or the owner routes it — this section is the retrieval surface.
**Carrier verdicts re-censused on Codex review of fm #959** (a repo-wide
grep per Q-number over `docs/` + `CONSTITUTION.md`; the first cut's
headline "no live fm record carries these" was too strong): **five are
ABSENT from every fm document** (a sixth, superbot:Q-0084, moved to
live-successor carriage on Codex R3); the rest are carried only in seat-era /
RECORD-tier / raw-artifact surfaces, in a `reference`-tier q-index seed
row, or as a **different facet** of the same ruling — each entry names its
verdict, and "live" below means a routed, current-truth surface (the
tiers of `docs/MAP.md`), not any mention anywhere.

- **superbot:Q-0084 (06-10), the merge grant's envelope:** *"it would be great if
  agents would merge their PRs whenever they feel like they are done"* —
  with CI-green-on-final-head, re-sync-main-first, own-session-PR scope.
  **Carrier: live successors, no token** — `CONSTITUTION.md`'s
  merge-your-own-green-PRs doctrine and the session-close skill's
  review-at-current-head requirement carry the envelope's content without
  citing this ruling *(the first cut said ABSENT — the token census missed
  successor carriage; Codex fm #959 R3)*. What the re-read adds is the
  provenance: the practice traces to this 06-10 grant.
- **superbot:Q-0191 (06-20):** *"anything that I personally direct the agents to do
  should never be held for review, always merge immediately"* — review
  gates key on who chose the task. **Carrier: ABSENT.** Its cousin
  **superbot:Q-0269** (07-12, *"any mergable PR in finished state just gets merged
  immediatly … it's not my task"*) **is carried live** — the
  CAPABILITIES.md kit-seed posture rule ("Owner-live session … act and
  merge directly (superbot Q-0269)") — so what the re-read adds there is
  the verbatim and the who-chose-the-task split, not the rule. Together
  they are the owner-trained root of the merge-fast reflex behind
  TRAP-006/007; any flip gate the round builds sits in live tension with
  them.
- **superbot:Q-0128 (06-13):** *"I never want to see such a prompt asking me for my
  confirmation ever again, no matter what it is for"* — enforcement must
  never surface as an interactive prompt (destructive-op trade-off
  accepted). In unresolved tension with OD-24 §3's re-ratified
  confirm-before-send/delete line — letter candidate, §4. **Carrier:
  ABSENT.**
- **superbot:Q-0131 (06-13):** he follows agent-provided steps without vetting —
  *"if you wanted to add something destructive you could have easily
  achieved that by steering me"* — with the adopted risk-class labelling
  (✅ safe / ↩️ reversible / ⚠️ irreversible) that `prep-owner-steps` and
  `owner-profile.md` do not carry. **Carrier: ABSENT.**
- **superbot:Q-0132 (06-13):** the provider-routing **trust** criterion — keep
  Anthropic on any path handling untrusted input (*"not resistant against
  weaponized prompts"*) — bears on OD-13's multi-provider mix. **Carrier:
  one raw audit-artifact row (`audits/2026-08-10-full-read/`); absent from
  the provider docs it belongs in.**
- **superbot:Q-0172 (06-18):** the ideas lifecycle's demand side is **visibility,
  not approval**: *"ideas can just be turned into a plan at any time
  without my approval, but it should be stated in the session log … so
  [reviewers or I] can easily see, filter and review"* — direct owner
  doctrine for gap #1's conveyor fix. **Carrier: a different facet only —
  CONSTITUTION.md cites this ruling as rule-change-proposal provenance;
  the ideas-visibility doctrine itself is uncarried.**
- **superbot:Q-0213 (07-02):** full-access credentials are deliberate (*"so the
  whole project can be completely automated"*), an agent scoped-token
  recommendation explicitly declined — the dated precedent of OD-24 §3.
  With **superbot:Q-0229** (07-03): *"I really never deny any requests"* + the
  measured fact that only the environment-level permission mode sits above
  the allow list on the web surface. And **superbot:Q-0263** (07-11): *"we spend way
  too much time on safety … this is just a hobby project"* — the doctrine
  is stable intent from June/July, not an 08-28 mood. **Carriers: Q-0213
  in seat-era prompts/research only; Q-0229 ABSENT; Q-0263 a q-index seed
  row carrying its derivable-values half only.**
- **superbot:Q-0242 (07-05):** allowlisting **cannot** silence scheduling-tool
  prompts (measured repeatedly; treat as platform behaviour). **Carrier:
  playbook R26, the trigger-health spec and a q-index seed row all carry
  the allowlist-doesn't-hold fact** — the first cut wrongly called this
  uncarried; what the re-read adds is his verbatim and the standing
  treat-as-platform-behaviour directive, beside fm's
  never-delete-a-trigger decision
  ([`../decisions.md`](../decisions.md)).
- **superbot:Q-0248 (07-06):** model-for-task as empirical discipline — the founding
  directive behind PL-004, connected to OD-13's methods track nowhere in
  fm. **Carrier: one seat-era taxonomy side-mention; the OD-13 connection
  is what is uncarried.**
- **superbot:Q-0254 (07-07/08), the fragments mechanism in his own words:** *"I
  often have big ideas, and when I explain them it's often in pieces … the
  agent repeating my intent back to me in a more complete form will help me
  find out if the agent understood my intent correctly"* — the owner
  statement of the problem roadmap Phase 2 and `intake` exist to solve.
  **Carrier: a one-line q-index seed row omitting all three addenda**; the
  third addendum makes mapping questions into the repo a standing
  **directive** with his ask bar ("matters AND actionable").
- **superbot:Q-0256 (07-09):** dependabot PRs — *"always be reviewed by the first
  session that sees them and then properly merged"* — a generic standing
  rule. **Carrier: one seat-era snapshot (`launch-readiness-2026-07-10`);
  no live record, and current-state withdrew a dependabot recommendation
  without citing it.**
- **superbot:Q-0088 (06-10):** bounded sessions + automatic continuation as the
  designed shape (*"always do 2 tasks and clean up the docs + guide the
  next session"*), plus the owner-measured fact that code quality degrades
  noticeably past ~700–800K context. **Carrier: the historical
  eap-retrospective only** *(the first cut said "in no fm record" —
  corrected on the census)*.
- **superbot:Q-0136 (06-14):** a prohibition without a paired authorization stalls
  unattended agents (measured on routine dispatch) — the instruction-design
  lesson for kit templates: every "never X" ships with the sanctioned path.
  **Carrier: ABSENT.**

## 3 · Genesis precedents for the round's gap table

The dig's §7 rows gain owner-ratified prior art; the round should route to
these instead of re-deriving:

| gap | genesis precedent (Q, verified quote in body) |
|---|---|
| #1 ideas conveyor | superbot:Q-0089 (the one-idea ender's bar: genuine, never filler) · superbot:Q-0172 (promote freely, flag visibly) · superbot:Q-0144/superbot:Q-0164 (reconciliation promotes ideas→plans; depth ≥ cadence, loud THIN flag) |
| #2 journal | superbot:Q-0101 — he already ruled once against planting stub docs that rot: *"generating 24 stubs that then rot would be worse than the current gap"* — the 11/14 byte-identical planted journals are the failure mode he pre-judged; strengthens §11's journal letter |
| #3 promotion loop | superbot:Q-0106 — agent rule-changes routed through the DISCUSS lane for ratification; the ask-channel's death severed rule-promotion too (one loss, two gaps) · superbot:Q-0194's body: fix = cheapest **enforcing** prevention in a fixed order (checker → hook → rule), checkers free-to-ship, hooks/rules owner-gated |
| #4 ask-channel | superbot:Q-0169 (his June review-inbox design — OD-21's comment lane's direct ancestor) · superbot:Q-0152 (mechanized ⚑ owner-decisions rollup with explicit "none") · superbot:Q-0258 (the three-lane topology) · superbot:Q-0254 addendum 3 (map questions into the repo — a directive) |
| #6 executor | superbot:Q-0107 (the auto-firing reconciliation cadence — a working genesis executor the kit never extracted) · superbot:Q-0124 (maintenance belongs to scheduled automation, not manual sessions) · superbot:Q-0153 (the daily idea-spotlight re-raise surface — the "standing surface he sees" fork already has a ratified precedent) |
| #7 flip-before-review | superbot:Q-0180 + superbot:Q-0174 (race accepted **given** a consumption loop; the enforceable defect is consumption) · superbot:Q-0197 (he retired an unused review gate for friction — the caution) · superbot:Q-0191/superbot:Q-0269 (the tension any gate must respect) |
| #8 owner-words capture | superbot:Q-0104 — the doc-audit ender's judgment half (*"is anything important from this session not yet documented?"*) is what was never mechanized |
| #9 substance verification | superbot:Q-0102 — the owner-stated bar verbatim: *"if there is genuinely nothing to improve, say so and why — do not hallucinate filler"* |
| #12 non-author read | superbot:Q-0117/superbot:Q-0174/superbot:Q-0258 — the reviewer-between-steps directive, the consumption doctrine, and the standing-drainer role |

Also for the round's classification work: **superbot:Q-0139** commissioned a
hook-vs-checker-vs-rule-vs-config decision framework
(`superbot:docs/operations/hook-policy.md`) and **superbot:Q-0233** a ten-class
critical-review rubric
(`superbot:docs/planning/rebuild-critical-review-rubric-2026-07-03.md`) —
both map onto OD-24 §6's fix families; neither is referenced anywhere in fm
(grep re-run this session). **superbot:Q-0195** carries the claims-mechanism's
measured genesis design (per-claim files: 0% merge conflicts vs ~98%
single-file; GC = the reconciliation's job) for the `control/claims/`
disposition §10 defers to this round. **superbot:Q-0272** item 3 made the per-repo
reading path kit-template material — routed to the dead Self-Improvement
lane and never shipped; Layer-2/ESTATE.md is its uncredited descendant.

## 4 · Letter candidates (items 1–2 queued on Codex fm #959 R3: `OQ-KIT-PROMPT-DOCTRINE` · `OQ-EAP-SPEND-WINDOW-MOOT`)

1. **superbot:Q-0128 vs OD-24 §3:** "no confirmation prompts ever" (06-13, his
   strongest phrasing) vs the re-ratified "confirm before sending or
   deleting" line (08-28). Both are his; the round should ask which governs
   kit-planted brakes rather than pick.
2. **superbot:Q-0249:** the ~09-07 spend-cap decision window — presumably mooted by
   the program close; one sentence from him records the mooting instead of
   leaving a dangling dated obligation.
3. **superbot:Q-0101 as evidence for the journal letter** already queued by §11:
   his own precedent argues the planted-journal skeleton is the
   stub-that-rots he ruled against.

## 5 · Coverage and nulls

Read fully: all 208 ruling sections in the band (8 lanes × 26), the two
context docs per lane. Not re-read: superbot:Q-0001–superbot:Q-0062 and superbot:Q-0273–superbot:Q-0275 (the
dig already read them in full, per its §9); ruling bodies outside the
router (cards, linked docs) except where a lane followed a `Home:` link.
The non-notable remainder — roughly 150 of 208 — was superbot product-local
decision-making (game economy, BTD6 mechanics, settings UX, dispatch
seams, rebuild grammar), each lane's null note naming its own residue; no
lane returned empty and no lane's null contradicts another's findings.
Verification: 59/59 notable quotes matched the router verbatim;
interpretations are the lanes', reviewed but not independently re-derived
— a claim here that changes an action should be re-read at its Q-number
first (the router is frozen; the numbers are stable).

## Appendix — the quote-verification ledger (the 59/59 evidence)

Committed so the headline count is auditable (added on Codex review of
fm #959 — the count was previously reconcilable only against an
uncommitted workflow artifact). One row per notable entry across the
eight lanes; ✓ = every ≥15-char fragment of the quote (ellipses and
bracketed reader notes removed) found verbatim in the router fetch
after markdown/blockquote normalization. Quote heads are truncated —
the full text lives at the Q-number in the frozen router.

| ruling | verified | quote head |
|---|---|---|
| superbot:Q-0083 | ✓ | just to be clear, completely self driving is not yet a near term goal, b… |
| superbot:Q-0084 | ✓ | it would be great if agents would merge their PRs whenever they feel lik… |
| superbot:Q-0088 | ✓ | the only thing I should realistically be doing is adding more ideas and … |
| superbot:Q-0086 | ✓ | I will try to add my AI api keys to your environments variables, so we c… |
| superbot:Q-0089 | ✓ | I noticed that AIs don't really come up with many ideas or improvements … |
| superbot:Q-0101 | ✓ | Cheat-sheet is enough. Folios stay for the high-traffic / complex areas … |
| superbot:Q-0102 | ✓ | if there is genuinely nothing to improve, say so and why — do not halluc… |
| superbot:Q-0104 | ✓ | is anything important from this session not yet documented?… |
| superbot:Q-0106 | ✓ | may be binding for their session, but they are not locked/pinned — they … |
| superbot:Q-0107 | ✓ | After every 10 PRs there should be a docs-only cleanup and plan reconcil… |
| superbot:Q-0114 | ✓ | agent-originated features only … Bug fixes, UX polish, docs, and correct… |
| superbot:Q-0117 | ✓ | if possible we should have hermes review the work first, and then it sho… |
| superbot:Q-0124 | ✓ | please make a note that the reconciliation is always done automatically … |
| superbot:Q-0125 | ✓ | they are all quite old, I … was curious if a session would see them, or … |
| superbot:Q-0126 | ✓ | help prevent agents from duplicating work … they should immediately open… |
| superbot:Q-0128 | ✓ | I never want to see such a prompt asking me for my confirmation ever aga… |
| superbot:Q-0129 | ✓ | it should be clear in the repo that I do not oppose unattended action, a… |
| superbot:Q-0131 | ✓ | the only thing I do is follow the steps you provide, so if you wanted to… |
| superbot:Q-0132 | ✓ | I can't trust chatGPT's AI… not resistant against weaponized prompts… ve… |
| superbot:Q-0136 | ✓ | has a problem dispatching the routines, something about sensitive inform… |
| superbot:Q-0137 | ✓ | the docs are not the system, the docs are a product of the system… |
| superbot:Q-0139 | ✓ | a ruleset for what a hook should define — what something needs to have/d… |
| superbot:Q-0144 | ✓ | so foolproof that if Hermes says 'go write a story about chickens' they … |
| superbot:Q-0153 | ✓ | picks one active docs/ideas/ capture per day … so the owner can mull it … |
| superbot:Q-0164 | ✓ | plan the full band + flag when the backlog can't fill it… |
| superbot:Q-0152 | ✓ | ⚑ Owner decisions needed … so Hermes rolls up what needs the owner inste… |
| superbot:Q-0166 | ✓ | that is not a reason to continue leaving the repo in a bad state.… |
| superbot:Q-0161 | ✓ | find out how to prevent this from happening again, add them to the setti… |
| superbot:Q-0150 | ✓ | the session deadlocks: the very tools needed to cd back or patch anythin… |
| superbot:Q-0169 | ✓ | probably a very high-leverage thing… |
| superbot:Q-0170 | ✓ | never actually made skills for claude … a lot more is possible than we c… |
| superbot:Q-0172 | ✓ | ideas can just be turned into a plan at any time without my approval, bu… |
| superbot:Q-0174 | ✓ | the first priority of any routine should be to fix anything codex flagge… |
| superbot:Q-0180 | ✓ | make every final push mention @codex in the PR for a forced review… |
| superbot:Q-0181 | ✓ | verify against the code at a pinned commit (never a badge / PR-title / s… |
| superbot:Q-0191 | ✓ | anything that I personally direct the agents to do should never be held … |
| superbot:Q-0193 | ✓ | the fact that an agent parroted "restart is your job" means the deploy r… |
| superbot:Q-0194 | ✓ | anytime a session hits something that interrupts the workflow, it should… |
| superbot:Q-0195 | ✓ | make it the reconciliation job, so the repo doesn't fill with thousands … |
| superbot:Q-0197 | ✓ | remove the label and the rule for that completely, it's not being used a… |
| superbot:Q-0210 | ✓ | a lot of things are referred to by question number, so [moving them] mig… |
| superbot:Q-0213 | ✓ | it has been deliberate that this token has full access … so the whole pr… |
| superbot:Q-0214 | ✓ | The kit's default posture is delete-with-tombstones (bounded corpus by c… |
| superbot:Q-0223 | ✓ | that should definitely be fully completed and I was led to believe that … |
| superbot:Q-0229 | ✓ | I really never deny any requests, so isn't there a universal way to allo… |
| superbot:Q-0233 | ✓ | I think it would be a good idea to create a rule or system that finds ex… |
| superbot:Q-0234 | ✓ | My idea is to turn the current repo into an artifact that provides exact… |
| superbot:Q-0241 | ✓ | Q-0241 governs the rebuild program. For the live production bot today, t… |
| superbot:Q-0242 | ✓ | this is also a recurring problem, which I've tried to fix more times tha… |
| superbot:Q-0248 | ✓ | we should also find out ways to properly use the right model for the rig… |
| superbot:Q-0249 | ✓ | budget so far is not really a problem, I'd like to test it for a while t… |
| superbot:Q-0254 | ✓ | unattended sessions or sessions in general that have certain questions d… |
| superbot:Q-0254 | ✓ | I often have big ideas, and when I explain them it's often in pieces … I… |
| superbot:Q-0256 | ✓ | yes dependabot PRs should always be reviewed by the first session that s… |
| superbot:Q-0258 | ✓ | Whenever a session feels something needs the owner's review — as opposed… |
| superbot:Q-0263 | ✓ | we spend way too much time on safety … this is just a hobby project.… |
| superbot:Q-0266 | ✓ | if we get as much production as we can as early as we can, we can then c… |
| superbot:Q-0269 | ✓ | I expect from a normal session that any mergable PR in finished state ju… |
| superbot:Q-0272 | ✓ | first I want you to make sure there is a properly suggested multi repo r… |
