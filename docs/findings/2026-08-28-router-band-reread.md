# The router band re-read — Q-0063–Q-0272, bodies in full

> **Status:** `audit` · 2026-08-28 · OD-24 review round, **session 2** (the
> genesis dig §11's item 4 — the band session 1 sampled headers-only, which
> verification proved can hide load-bearing owner directives: it hid Q-0266
> once)
>
> **Method.** superbot stays frozen: one raw API fetch of
> `docs/owner/maintainer-question-router.md` at `main` (668,746 bytes; no
> clone, no write). The band Q-0063–Q-0272 — **208 `### Q-`-headed ruling
> sections, whole-population by header regex** (lanes self-reported 210
> bodies read; the +2 is one lane counting unnumbered addendum blocks as
> rulings — the dig's own "210 of 275" headers-only figure is its count by
> its own method, not re-derived here) —
> split into eight whole-ruling chunks, each read **in full** by one reader
> lane (8/8 complete, ~840k subagent tokens), each lane primed with the
> genesis dig and OD-24 and told an honest null is expected. **Every quote below was
> then machine-verified verbatim against the fetched router text: 59/59
> matched** (after markdown/blockquote normalization; the first verification
> query was broken and reported 37 misses — the known-good Q-0266 quote
> "missing" was the tell, TRAP-003's class, caught before anything was
> recorded). Reader interpretations are `REVIEWED`; quotes are the owner's
> or, where a lane flagged it, the ruling's decision text; "absent from fm"
> claims are lane greps, the six headline ones re-run by the session itself.
> Citations are `superbot:docs/owner/maintainer-question-router.md` at the
> 2026-08-28 fetch, by Q-number.
>
> **The one-paragraph result:** the band holds no reversal of the round's
> direction, but it **narrows seven of the genesis dig's claims** (§1),
> carries **~13 standing owner rules and facts no live fm record states**
> (§2), and gives **owner-ratified genesis precedents for most of the dig's
> gap table** (§3) — including three cases where the genesis system already
> built the exact mechanism a gap row presents as an open design question.
> The dominant pattern: the round keeps re-deriving designs the owner
> already ruled on in June; the router is where those rulings live.

## 1 · What this re-read corrects or narrows in the genesis dig

Each row names the dig claim and the ruling that narrows it. The dig itself
now carries a one-line pointer here (its §9 named this band as its thinnest
coverage).

1. **Q-0083 (06-10) — full self-driving was declared the end-state inside
   the genesis era**, two days after Q-0015's "not 100% autonomous": *"just
   to be clear, completely self driving is not yet a near term goal, but
   ultimately there will not be much else left to do if I keep implementing
   at the current speed"* — with autonomy tiers granted area-by-area
   **through the router**. Narrows dig §6.2 (which reads the autonomy
   ambition as a July move) and adds ask-channel provenance.
2. **Q-0107 (06-11) — the REVIEW/grooming loop had a mechanized demand
   structure**: *"After every 10 PRs there should be a docs-only cleanup and
   plan reconciliation"* — owner-amended to 20, auto-fired by
   `reconciliation-trigger.yml` opening a reconcile-labelled issue, with a
   dueness checker. Narrows dig §2's "no machine ever verified any of it":
   the loop's **cadence** was machine-fired; what was prose was the
   substance. (fm's only mention is a dated 07-15 rollout finding.)
3. **Q-0180 (06-19) — the owner's ratified June design accepted the
   merge-vs-review race**: *"make every final push mention @codex in the PR
   for a forced review"* — post-merge review was chosen **because a
   consumption loop existed** (Q-0174: next session fixes flagged-real
   first). Narrows the dig's flip-before-review framing (gap #7): the
   owner-precedented defect is the **missing consumption loop**, not merge
   timing itself; fm's never-merge-before-Codex rule is the stricter
   post-close successor, not the only precedent.
4. **Q-0214 (07-02) — the kit's owner-picked retention posture was
   delete-with-tombstones**, a bounded corpus by construction, with shrink
   duty as checker+routine and a website `/updates` feed as the owner
   surface. Narrows dig §8's "the EAP-era answer to maintain-cost was
   generation + checkers, never fewer files" — and §4's lost-in-extraction
   table has no retention row; whether the kit shipped any of it is
   unexamined (a round question).
5. **Q-0241's own scope clause — never-wait / silence=consent governed the
   rebuild program only**, with Q-0213's ask-first brakes left standing for
   production *"until the owner generalizes this"*. Narrows dig §6.2's
   presentation of Q-0241/PL-002 as his general July intent; whether the
   kit's PL-002 canonicalization preserved that scope is one check the
   round owes.
6. **Q-0258 (07-10) — Codex was made the standing drainer of the review
   lane mid-program**, in a three-lane ask topology (decide yourself ·
   relay to Codex · owner-queue only for genuinely owner-only). Narrows dig
   §6.2's "Codex on PRs is the one external check added, post-close, by his
   instruction" — the instruction is mid-program, and the topology bears on
   the round's ask-channel design. Related: **Q-0117 (06-12)** already
   directed an independent-model reviewer between big steps and `main`
   (so the closed loop survived *despite* an owner directive, not for lack
   of one) — and **Q-0197 (06-22)** shows him retiring that same gate as
   unused friction, the caution for any gap-#7 fix.
7. **Q-0249 (07-06) — a second approximately-dated owner obligation
   existed**: decide AI-spend caps from *"the average of a couple of
   months"* (window lands ~2026-09-07), where dig §10 calls the ~09-09
   trading gate "the estate's only future-dated obligation". The program
   close likely mooted it — but the mooting was never recorded, which is
   itself the owner-words class the dig tracks. Letter candidate, §4.
   *(Adjacent, not a contradiction: Q-0223 (07-03) is an owner
   expectation-vs-reality statement about the kit seven weeks before
   OD-21; the dig's "first recorded" claim is Era-3-scoped and stands.)*

## 2 · Standing owner rules and facts no live fm record carries

Verbatim-verified, each with its bearing; none is estate-law until the
round or the owner routes it — this section is the retrieval surface.

- **Q-0084 (06-10), the merge grant's envelope:** *"it would be great if
  agents would merge their PRs whenever they feel like they are done"* —
  with CI-green-on-final-head, re-sync-main-first, own-session-PR scope.
  The provenance of the practice every session exercises.
- **Q-0191 (06-20):** *"anything that I personally direct the agents to do
  should never be held for review, always merge immediately"* — review
  gates key on who chose the task. With **Q-0269** (07-12): *"any mergable
  PR in finished state just gets merged immediatly … it's not my task"* —
  the owner-trained root of the merge-fast reflex behind TRAP-006/007; any
  flip gate the round builds sits in live tension with these two and must
  block premature flips without recreating the parked-green-PR failure.
- **Q-0128 (06-13):** *"I never want to see such a prompt asking me for my
  confirmation ever again, no matter what it is for"* — enforcement must
  never surface as an interactive prompt (destructive-op trade-off
  accepted). In unresolved tension with OD-24 §3's re-ratified
  confirm-before-send/delete line — letter candidate, §4.
- **Q-0131 (06-13):** he follows agent-provided steps without vetting —
  *"if you wanted to add something destructive you could have easily
  achieved that by steering me"* — with the adopted risk-class labelling
  (✅ safe / ↩️ reversible / ⚠️ irreversible) that `prep-owner-steps` and
  `owner-profile.md` do not carry.
- **Q-0132 (06-13):** the provider-routing **trust** criterion — keep
  Anthropic on any path handling untrusted input (*"not resistant against
  weaponized prompts"*) — bears on OD-13's multi-provider mix; absent from
  fm's provider docs.
- **Q-0172 (06-18):** the ideas lifecycle's demand side is **visibility,
  not approval**: *"ideas can just be turned into a plan at any time
  without my approval, but it should be stated in the session log … so
  [reviewers or I] can easily see, filter and review"* — direct owner
  doctrine for gap #1's conveyor fix.
- **Q-0213 (07-02):** full-access credentials are deliberate (*"so the
  whole project can be completely automated"*), an agent scoped-token
  recommendation explicitly declined — the dated precedent of OD-24 §3.
  With **Q-0229** (07-03): *"I really never deny any requests"* + the
  measured fact that only the environment-level permission mode sits above
  the allow list on the web surface. And **Q-0263** (07-11): *"we spend way
  too much time on safety … this is just a hobby project"* — the doctrine
  is stable intent from June/July, not an 08-28 mood.
- **Q-0242 (07-05):** allowlisting **cannot** silence scheduling-tool
  prompts (measured repeatedly; treat as platform behaviour) — the
  mechanism background behind `[D-0015]` that fm states only as the rule.
- **Q-0248 (07-06):** model-for-task as empirical discipline — the founding
  directive behind PL-004, connected to OD-13's methods track nowhere in
  fm.
- **Q-0254 (07-07/08), the fragments mechanism in his own words:** *"I
  often have big ideas, and when I explain them it's often in pieces … the
  agent repeating my intent back to me in a more complete form will help me
  find out if the agent understood my intent correctly"* — the owner
  statement of the problem roadmap Phase 2 and `intake` exist to solve,
  carried fm-side only as a one-line q-index pointer omitting all three
  addenda; the third addendum makes mapping questions into the repo a
  standing **directive** with his ask bar ("matters AND actionable").
- **Q-0256 (07-09):** dependabot PRs — *"always be reviewed by the first
  session that sees them and then properly merged"* — a generic standing
  rule homed only in the frozen repo.
- **Q-0088 (06-10):** bounded sessions + automatic continuation as the
  designed shape (*"always do 2 tasks and clean up the docs + guide the
  next session"*), plus the owner-measured fact that code quality degrades
  noticeably past ~700–800K context — in no fm record.
- **Q-0136 (06-14):** a prohibition without a paired authorization stalls
  unattended agents (measured on routine dispatch) — the instruction-design
  lesson for kit templates: every "never X" ships with the sanctioned path.

## 3 · Genesis precedents for the round's gap table

The dig's §7 rows gain owner-ratified prior art; the round should route to
these instead of re-deriving:

| gap | genesis precedent (Q, verified quote in body) |
|---|---|
| #1 ideas conveyor | Q-0089 (the one-idea ender's bar: genuine, never filler) · Q-0172 (promote freely, flag visibly) · Q-0144/Q-0164 (reconciliation promotes ideas→plans; depth ≥ cadence, loud THIN flag) |
| #2 journal | Q-0101 — he already ruled once against planting stub docs that rot: *"generating 24 stubs that then rot would be worse than the current gap"* — the 11/14 byte-identical planted journals are the failure mode he pre-judged; strengthens §11's journal letter |
| #3 promotion loop | Q-0106 — agent rule-changes routed through the DISCUSS lane for ratification; the ask-channel's death severed rule-promotion too (one loss, two gaps) · Q-0194's body: fix = cheapest **enforcing** prevention in a fixed order (checker → hook → rule), checkers free-to-ship, hooks/rules owner-gated |
| #4 ask-channel | Q-0169 (his June review-inbox design — OD-21's comment lane's direct ancestor) · Q-0152 (mechanized ⚑ owner-decisions rollup with explicit "none") · Q-0258 (the three-lane topology) · Q-0254 addendum 3 (map questions into the repo — a directive) |
| #6 executor | Q-0107 (the auto-firing reconciliation cadence — a working genesis executor the kit never extracted) · Q-0124 (maintenance belongs to scheduled automation, not manual sessions) · Q-0153 (the daily idea-spotlight re-raise surface — the "standing surface he sees" fork already has a ratified precedent) |
| #7 flip-before-review | Q-0180 + Q-0174 (race accepted **given** a consumption loop; the enforceable defect is consumption) · Q-0197 (he retired an unused review gate for friction — the caution) · Q-0191/Q-0269 (the tension any gate must respect) |
| #8 owner-words capture | Q-0104 — the doc-audit ender's judgment half (*"is anything important from this session not yet documented?"*) is what was never mechanized |
| #9 substance verification | Q-0102 — the owner-stated bar verbatim: *"if there is genuinely nothing to improve, say so and why — do not hallucinate filler"* |
| #12 non-author read | Q-0117/Q-0174/Q-0258 — the reviewer-between-steps directive, the consumption doctrine, and the standing-drainer role |

Also for the round's classification work: **Q-0139** commissioned a
hook-vs-checker-vs-rule-vs-config decision framework
(`superbot:docs/operations/hook-policy.md`) and **Q-0233** a ten-class
critical-review rubric
(`superbot:docs/planning/rebuild-critical-review-rubric-2026-07-03.md`) —
both map onto OD-24 §6's fix families; neither is referenced anywhere in fm
(grep re-run this session). **Q-0195** carries the claims-mechanism's
measured genesis design (per-claim files: 0% merge conflicts vs ~98%
single-file; GC = the reconciliation's job) for the `control/claims/`
disposition §10 defers to this round. **Q-0272** item 3 made the per-repo
reading path kit-template material — routed to the dead Self-Improvement
lane and never shipped; Layer-2/ESTATE.md is its uncredited descendant.

## 4 · Letter candidates (for the round's next owner sitting — not queued)

1. **Q-0128 vs OD-24 §3:** "no confirmation prompts ever" (06-13, his
   strongest phrasing) vs the re-ratified "confirm before sending or
   deleting" line (08-28). Both are his; the round should ask which governs
   kit-planted brakes rather than pick.
2. **Q-0249:** the ~09-07 spend-cap decision window — presumably mooted by
   the program close; one sentence from him records the mooting instead of
   leaving a dangling dated obligation.
3. **Q-0101 as evidence for the journal letter** already queued by §11:
   his own precedent argues the planted-journal skeleton is the
   stub-that-rots he ruled against.

## 5 · Coverage and nulls

Read fully: all 208 ruling sections in the band (8 lanes × 26), the two
context docs per lane. Not re-read: Q-0001–Q-0062 and Q-0273–Q-0275 (the
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
