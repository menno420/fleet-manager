# The trap register — the estate's recurring execution mistakes

> **Status:** `binding` · opened 2026-08-23 · program step **D3**, roadmap
> [§ 5.4](planning/2026-08-08-agent-operating-environment-roadmap.md).
>
> **What this is:** the mistakes sessions in this estate *actually keep making*,
> in the structured form roadmap § 5.4 requires — **TRAP · TRIGGER · WHY ·
> REQUIRED PREVENTION · VERIFY · ORIGIN** — each one wired to the moment it
> happens.
>
> **Why it exists:** [`findings/2026-08-08-why-rules-dont-bind.md`](findings/2026-08-08-why-rules-dont-bind.md)
> measured 116 committed statements across 66 files catching **0 of 16**
> incidents, and fm #915 measured the delivery half: **55 doc-routes, none
> naming an execution mistake.** A trap that is only *stated* has never bound
> anything here. So the register is not the deliverable — the **lifecycle** is:
>
> ```
> mistake → trap entry → route/hook reminder → deterministic checker where possible
> ```
>
> **An entry without a route is unfinished work**, not a record. The `route`
> field on every trap below names the `doc-routes.json` id that delivers it, or
> says plainly that it is undelivered and why.

## How to use this file

- **You will not read this file at the moment you need it.** That is the whole
  premise — the route fires and quotes the trap at you instead. If you *are*
  reading it top to bottom, you are auditing, not working.
- **Adding a trap:** it earns a place when it has happened **at least twice**,
  or once with a real cost, and you can name the instances. A trap nobody has
  fallen into is a style preference; keep those out.
- **The ORIGIN field is load-bearing.** It is what stops a future session
  arguing the trap away in the abstract — the instances are named and dated.

---

## TRAP-001 · A dated document read as current state

- **TRIGGER** — you are about to state what is *true now* — a service exists, a
  cron fires, a repo is deployed, a requirement's value, a count — and your
  basis is a document, a file header, a code comment, or a prior session's
  record.
- **WHY** — every document in this estate was written once and describes the day
  it was written; the live surfaces move underneath it. `MAP.md` already closes
  with the rule (*"When a document here contradicts a live surface, the live
  surface wins"*), and stating it there has not prevented a single instance.
- **REQUIRED PREVENTION** — read the **live surface**, with a credential this
  session already holds: `$GITHUB_PAT` over direct egress for anything on
  GitHub, `$RAILWAY_API_KEY` against `https://backboard.railway.com/graphql/v2`
  for anything deployed. If you genuinely cannot, the sentence must carry its
  own provenance: *"per `<doc>` dated `<date>`, not re-verified."* Never launder
  a citation into a measurement.
- **VERIFY** — the claim names **the call and its output**, not a file path and
  line number. "`GET /user/repos` → 26 repositories, 9 archived" passes;
  "`ESTATE.md:44` says nine are archived" does not.
- **ORIGIN** — `MEASURED` 2026-08-23, three instances in one conversation on one
  question, the superbot `botsite/`+`dashboard/` question:
  1. Called superbot's copies vestigial from a Layer-2 doc.
  2. **Retracted a correct finding** on the strength of a workflow header
     comment written 2026-06-17, two months before the cutover it contradicted.
  3. Wrote *"Measuring the live state instead"* and then cited
     `findings/2026-08-14-railway-websites-audit.md:298` — a document.
  The owner corrected it from memory; the live Railway read then agreed with
  him. **The credential was present in the environment the whole time.**
- **ROUTE** — `stamping-a-measured-claim` (fires on Edit/Write of the `MEASURED`
  tag) and `live-state-assertion` (fires on Bash reads of dated records).

---

## TRAP-002 · An exit code read after a pipe

- **TRIGGER** — a shell command containing a pipe, whose result you then read
  with `$?` or `&&`.
- **WHY** — `$?` after `a | b` is **b's** exit code. The failure is silent and
  inverted: the command failed, the check says it passed, and the session
  reports success. This is the estate's single most-restated trap and, until
  today, its least-delivered one.
- **REQUIRED PREVENTION** — do not pipe the command whose exit code you need.
  Redirect to a file and read the code directly (`cmd > out.txt 2>&1; echo $?`),
  or use `${PIPESTATUS[0]}` when the pipe is unavoidable.
- **VERIFY** — the reported exit code came from a command with **no pipe**, or
  from `PIPESTATUS`.
- **ORIGIN** — `MEASURED`: fm #915 counted **26 of 389 session cards** restating
  this trap and **0 of 55 doc-routes** delivering it. It then happened again on
  2026-08-23 during R5: `pip install … | tail -5; echo "PIP_EXIT=$?"` printed
  `PIP_EXIT=0` — which was **`tail`'s** exit code, while the install's real
  status was still unknown. Caught only because the output looked wrong.
  The kit's own gate discipline (*"read its real exit code, never after a
  pipe"*) is stated in the boot file and did not prevent it.
- **ROUTE** — `exit-code-after-a-pipe` (fires on the Bash command itself, before
  it runs).

---

## TRAP-003 · Absence of evidence recorded as evidence of absence

- **TRIGGER** — you are about to write that something is **not** there — not
  indexed, not referenced, not present, no consumers, no next step — and your
  basis is a search that returned nothing.
- **WHY** — an empty result proves your *query ran*, not that the world is
  empty. The query may be wrong, scoped wrong, or aimed at a surface that never
  contained the thing.
- **REQUIRED PREVENTION** — run the **positive control**: make the same query,
  in the same form, find something you already know is present. If it cannot,
  the query is broken, not the world. For a "not in file F" claim specifically,
  **open F** — a keyword search is not a read.
- **VERIFY** — the record states the positive control and its result alongside
  the null.
- **ORIGIN** — `MEASURED`, three instances:
  1. 2026-08-23 — a 26-repo index sweep using `path:README.md` with no search
     term returned 0 for **every** repo including `fleet-manager`; it measured
     nothing. Caught only because a known-good repo also came back empty.
  2. 2026-08-23 — `spider-swing` was recorded as having *"no next-step line
     anywhere in 662 lines"* on the strength of a heading regex. Reading the
     file found the next step at lines 512–514, in prose. The verdict was wrong
     and the method produced it.
  3. 2026-08-09 (fm #830, pre-existing) — a `prompt_routes` probe returned 0 and
     came one sentence from recording a missing route that exists under a
     different key.
- **ROUTE** — `absence-claim` (fires on Edit/Write of absence phrasing).

---

## TRAP-004 · A claim wider than the sample that produced it

- **TRIGGER** — you are about to write a fraction, a total, or a universal
  (*"only 3 of 26"*, *"none of the other 25"*, *"every repo"*) covering a
  population larger than the set you actually measured.
- **WHY** — the unmeasured members get silently classified with the measured
  ones, and the sentence reads as a census when it is a sample. Downstream
  decisions then rest on a number nobody took.
- **REQUIRED PREVENTION** — state **N measured of M total**, and name what the
  unmeasured remainder is. If the claim needs the full population, measure the
  full population — it is usually cheaper than the argument about whether the
  sample generalises.
- **VERIFY** — every count in the claim maps to an item actually probed.
- **ORIGIN** — `MEASURED` 2026-08-23: *"only 3 of 26 repositories are in the
  `search/code` index"* was written from **11** probes, classifying the untested
  15 with the measured 8. `@codex` caught it on fm #912. Probing the remaining
  15 moved the real figure to **7 of 26** — a wider gap than claimed, so the
  conclusion survived, but the evidence had not supported it. A recorded
  `MEASURED` dependency sweep had rested on the same unstated assumption.
- **ORIGIN, second entry — `MEASURED` 2026-08-26, four instances in ONE session,
  two of them inside the document warning about this trap.** Recorded because
  the repeat rate is the finding: a rule with a route still fired four times.
  1. **A ten-repo kit-version census published over all adopters.** The estate's
     own records already contradicted it; the full sweep returned **five live
     versions across 16 adopters**, not three.
  2. **A commit count from a SHALLOW clone.** `git log` in this container
     reported **52 commits, one author, every one squash-merged** — written as a
     property of the repository. `main` holds **966**; `.git/shallow` exists.
     `git rev-list --count HEAD` and `git shortlog` share the defect.
  3. **"All 51 notifications were replays"** — the set described by its
     majority; four were new.
  4. **163 cards reported as 163 sessions**, when one session can land two
     (`.sessions/2026-07-23-hub-forge-slice4-handoff.md` + `-landed.md` say so
     in their own text).
  **What the existing route missed, and why it was widened:** its noun
  allowlist covered `repos|repositories|files|entries` only — so `cards`,
  `commits` and `sessions` were invisible in a repo that counts session cards
  constantly — and **every pattern required a ratio or an `all`/`only`
  qualifier**, so the bare count-only form (*"50 commits"*, *"74 cards"*) matched
  nothing. Replayed against the four sentences above, the route scored **0 of
  4** while its own origin sentence fired. Widened 2026-08-26 (fm #950), plus a
  second route on `git log` for the shallow-clone case, which no phrasing check
  can catch because the sentence is only wrong on this surface.
  **The widening itself then narrowed the route, which is why it now has a
  test.** Replacing the singular noun list with a plural one silently deleted
  `every (repo|repository|file) in` — three forms the route had caught since it
  was written. `@codex` caught it on fm #950; restored, and
  `tools/test_doc_route_patterns.py` now pins **17 cases** (10 must-fire, 3
  must-be-silent, 4 shallow-clone) so a future edit that narrows this table
  fails instead of looking like a widening.
- **ROUTE** — `claim-beyond-the-sample` (fires on Edit/Write of census phrasing,
  ratio **and** count-only forms) · `shallow-clone-commit-counts` (fires on
  Bash `git log` / `git rev-list` / `git shortlog`).

---

## TRAP-005 · The owner corrected from memory and was right

- **TRIGGER** — the owner states something about this estate that contradicts
  what you have just read or concluded.
- **WHY** — he built it, and his statements are source truth per the boot file.
  The failure mode is not disbelieving him outright; it is the softer one —
  treating his correction as a hypothesis to be adjudicated against the
  documents you already misread.
- **REQUIRED PREVENTION** — take the correction as the new baseline and go
  measure the **live surface** to confirm the mechanism, not to test him. A
  probe that disagrees means you took the wrong path.
- **VERIFY** — the follow-up reads a live surface, not another document.
- **ORIGIN** — `MEASURED` 2026-08-23: he said the superbot web services were
  taken offline and should only be live in `websites`. The records said
  otherwise and had been believed twice. The live Railway read returned
  `reliable-grace` = **`Postgres` + `worker`** — exactly what he said, and it
  additionally falsified the audit's claim that `postgres-botsite` was still
  present. **Across four exchanges on this question his recollection beat the
  written record twice and lost zero times.**
- **ROUTE** — undelivered by a hook, and honestly so: a hook cannot see the
  owner's message contradicting a conclusion. This one binds through
  `CONSTITUTION.md` and the boot file's source-truth rule; the register entry
  exists so the instance count is on the record rather than in a transcript.

---

## TRAP-006 · A session card flipped to `complete` before the branch is pushed

- **TRIGGER** — you are about to `git push` a branch whose in-diff
  `.sessions/*.md` card already reads `Status: complete`, in any repo whose
  landing path auto-merges on green (`merge-on-green.yml` here;
  `auto-merge-enabler` elsewhere in the estate).
- **WHY** — the born-red card **is** the merge hold. Two independent guards read
  it: the `substrate-gate` / `quality` check is red while the card says
  `in-progress`, and `merge-on-green.yml:190–213` fetches each in-diff card,
  parses its Status and `continue`s past the merge on `in-progress`. Flipping
  the card *locally before the first push* defeats both at once — the PR is
  born green, the sweep lands it within seconds, and **the review window never
  opens.** The card is not paperwork; it is the lock.
- **REQUIRED PREVENTION** — commit the card **red** and push it red. Flip to
  `complete` as the deliberate last commit, after review has answered. If a PR
  must be opened green for some other reason, apply the `do-not-automerge`
  label, which the workflow honours as an explicit carve-out re-read fresh per
  PR.
- **VERIFY** — after opening the PR, the required check is **red** and the
  reason given is the born-red hold. A green required check on a PR you have
  just opened means the hold is not armed.
- **ORIGIN** — `MEASURED` 2026-08-23, fm **#915**: card flipped locally, both
  commits pushed together, PR opened `08:24:29Z` and merged by
  `github-actions[bot]` at `08:25:06Z` — **37 seconds**, inside the measured
  ~335 s Codex relay. Result: **0 reviews and 0 inline comments** at 503 s,
  against fm #912 the same morning which has its `chatgpt-codex-connector[bot]`
  review. Nothing was harmed — the content was verified — but the PR that
  argued *"documented traps are not delivered"* was itself landed unreviewed by
  a trap documented in two places: the 2026-08-20 railway card
  (*"`merge-on-green` landed #871 before the round-2 review I had requested
  could answer"*) and `docs/repos/superbot/README.md` (*"the auto-merge enabler
  ARMS AT OPEN — disable before requesting review"*).
- **HOW THIS GUARD GETS DISARMED, and it is not hypothetical** — `MEASURED`
  2026-08-23 (Codex, fm #922). `route_docs.py` marks a route fired when the tool
  text merely *contains* the routed doc's path, and persists the whole fired set
  whenever **any** route in the same call produced a hit. So one ordinary combined
  command —

  ```sh
  grep -c TRAP docs/traps.md; curl -sS https://api.github.com/repos/...
  ```

  — persisted `["card-flip-before-push", …]` because the `github-api` route
  supplied the hit, and the next **real** `git push` produced nothing. **fm #920
  merged unreviewed behind exactly that silence.** Fixed by scoping the
  mention-exemption away from `Bash`: a command naming a doc is not an agent
  reading it. The fm #878 defect that branch exists for was a `Read` re-firing
  onto its own directed read, and that still holds.

- **AND a quoted mention disarmed it too, until 2026-08-23.** The `when` regex was
  applied to the raw command, so `grep -n '; git push' docs/traps.md` matched on
  text inside a quoted *argument* and consumed the route. Fixed with an opt-in
  `"code_only": true`, which blanks quoted spans before matching: a Bash command
  is code, its quoted arguments are data. **Opt-in on purpose** — blanking
  globally would break `github-api`, whose patterns legitimately match URLs
  inside quotes.

- **WHAT THE PUSH ROUTE MATCHES** — probed across ten forms, because the first two
  regexes each missed real ones. It fires on every valid push, including git's
  global options and a shell-separated one:

  ```sh
  git push -u origin claude/my-branch          # plain
  git -c http.proxy= -c https.proxy= push      # the estate's proxy-bypass form
  git -C /home/user/websites push              # another worktree
  git -p push origin x  ·  git -P push origin x   # short pager options
  cd /home/user/websites && git push           # after a separator
  ```

  It stays silent on a *mention*, which matters because a route is consumed once
  per session — `echo git push`, `grep -rn 'git push' docs/`, and
  `echo 'remember to git push later'` must not disarm the safeguard before the
  real push happens. That was a live defect (Codex, fm #919 round 3).

- **ROUTE** — **two**, deliberately: `card-flip-before-push` (Bash, on `git push`)
  and `card-status-write` (Edit/Write, on `.sessions/*.md`). One route covering both
  was the first design and it was **useless** — routes fire once per session per ID,
  so writing the born-red card consumed it and the push, the moment the trap actually
  fires, was silent. Reproduced against `route_docs.py`: single route **1-then-0**,
  split **1-then-1** (Codex, fm #919). The push pattern also matches git's global
  options (`git -c http.proxy= … push`, `git -C <path> push`) — the estate's own
  documented proxy-bypass push is exactly that form and the first regex missed it.

---

## TRAP-007 · A card flipped to `complete` while a requested review is unanswered

**This is a COMPLIANCE failure with an existing rule, not a newly discovered
trap.** An earlier draft claimed the flip was *"correct by every written rule"*
and that no rule covered it. **Both were false** (`@codex`, fm #938), and the
correction is the more useful record: the rule existed, was measured, and still
was not followed — which is this estate's own thesis about why rules do not bind,
demonstrated on itself.

- **THE RULE THAT ALREADY SAID SO** —
  [`.claude/skills/session-close/SKILL.md`](../.claude/skills/session-close/SKILL.md)
  `:116-129`, `MEASURED` on fm #827, states the loop verbatim: *"request review on
  the current head → wait, read the inline comments → verify each finding against
  source → if you changed anything a reviewer would have an opinion about: push,
  re-request on the NEW head, and wait again → flip only when the outstanding
  review covers the head you are flipping."* Its step 6c adds the reason: **the
  flip is the merge-eligibility event.**
- **TRIGGER** — you are about to flip an in-diff `.sessions/*.md` card to
  `complete`, or to push after flipping, and a review you requested has not
  answered **on the current head**.
- **WHY IT KEEPS HAPPENING ANYWAY** — the rule lives in a skill a session invokes
  at the *end*, and the losing move happens *before* that. The lander sees card
  `complete` + gate green and cannot know a re-review is pending, so it merges the
  head it has. This is a delivery gap, not a knowledge gap.
- **REQUIRED PREVENTION** — flip only when the outstanding verdict covers the
  current head — and **the two surfaces are checked differently**, which is where
  this goes wrong quietly.
  **A review object carries `commit_id`** — compare it directly; that is the case
  with findings, and it needs no parsing.
  **A clean pass creates no review object at all** — it arrives as an **issue
  comment**, and **its body shape VARIES**, which is the part that bites:

  | observed clean-pass comment | `Reviewed commit:` line? | head also findable as |
  |---|---|---|
  | `…Hooray!` — websites #511, fm #924 | **yes** | — |
  | `Approved — no blocking findings` — fm #938, 2026-08-24 | **NO** (`'Reviewed commit:' in body` → False) | 40-hex SHA in `blob/<sha>/…` URLs, beside the merge-preview SHA |
  | `Approved — no blocking findings` — fm #939, 2026-08-24 | **yes** | 40-hex SHA in URLs |

  **The headline does NOT predict whether the line is present** — fm #938 and
  fm #939 share the `Approved` headline and differ on it. Line presence is an
  **independent variation**, so never branch on the headline.

  **So the rule is: try `Reviewed commit:` first, and when it is absent, extract
  every 40-hex string from the body and test whether your head is AMONG them** —
  presence, not position, because one of them is the merge preview.
  *(fm #938 shipped a version of this block saying the clean comment identifies
  the head *only* through `Reviewed commit:`. That is true of one shape and false
  of the other, and a session meeting the second would find nothing and conclude
  no verdict existed — the false negative this entry exists to prevent. **Do not
  narrow this to one shape in either direction**; two are observed and the vendor's
  own About-block claims a third behaviour, a 👍 reaction, which this estate has
  never seen. `CAPABILITIES.md` § "Codex's CLEAN verdict is an issue comment"
  keeps that unresolved deliberately.)*
  **If the body names no SHA you can match, do not guess** — treat the verdict as
  not covering your head and re-request. If you must re-request after flipping, apply `do-not-automerge`
  **before pushing the completed card** — the push, not the request, is what makes
  the PR mergeable, so a label applied afterwards can lose the race.
- **VERIFY** — before flipping, a verdict exists at the current head SHA. After
  re-requesting, the required check is red or the label is on.
- **ORIGIN** — `MEASURED` 2026-08-23/24, fm **#937**. Round 1 addressed, card
  flipped, re-review requested, further commits pushed. `merge-on-green` merged at
  head `775f1c8`; commits `4a80bf6` and `4ea3962` carrying round 2's six findings
  reached `main` in **neither** —
  `git show origin/main:docs/findings/2026-08-23-owner-direction.md` returned
  missing and `grep -c` on main's `owner-queue.md` returned **1** for the entry
  that was supposed to have moved. `main` carried five known-wrong statements until
  fm #938. **Second instance:** the 2026-08-20 railway card already recorded
  *"`merge-on-green` landed #871 before the round-2 review I had requested could
  answer"* — and produced no register entry, which is why it recurred.
- **DELIVERY** — `MEASURED` 2026-08-24, fm #938, and the first fix was wrong.
  Extending the two existing routes' `says` strings delivered **nothing**:
  `route_docs.py` spends a route on first match, so `card-status-write` was
  consumed writing the born-red card and `card-flip-before-push` on the first red
  push, leaving the flip and the final push silent. Reproduced on the real
  sequence — steps 3 and 4 both SILENT. Fixed two ways: an opt-in **`repeat`**
  flag (an ACTION guard is never spent; a REFERENCE pointer still speaks once) now
  set on `card-flip-before-push`, and a new **`card-flip-to-complete`** route that
  matches the completion transition itself. Re-run post-fix: **1 fires, 2 fires,
  3 fires, 4 fires, and every later push fires.**

## TRAP-008 · A label read as its contents

- **TRIGGER** — you are about to state what something **is** — a repository, a
  document, a folder, a table row, an invariant, a claim under a heading — and
  your basis is its **name, title, heading, or opening clause** rather than the
  thing itself.
- **WHY** — labels are written short; the qualifier that reverses them lives
  downstream, and in this estate it reliably does. `docs/ESTATE.md:85` is 869
  characters on one line, one cell of it 673: the cell opens *"the ground-up
  bot rebuild"* and places *"parity ≠ ported"* ~400 characters later, inside
  the same cell. Finding the line is not reading it.
- **REQUIRED PREVENTION** — read to the end of the unit you are quoting: the
  whole cell, the whole row, the whole file. A pointer is not its document —
  when the boot file names a doc, **open the doc**. A listing command (`ls`,
  `find -name`, `grep -l`, `head -1`, `git ls-tree`) yields **names and counts,
  never contents**: it may locate a thing, it may not characterise one.
- **VERIFY** — the record cites the **line or section actually read**, not the
  path alone. "Per `X.md`" is not a citation; "`X.md:85`, whose cell ends
  `parity ≠ ported`" is.
- **ORIGIN** — `MEASURED`, six instances, all 2026-09-01 in one session
  (fm #997–#1004); full record:
  [`findings/2026-09-01-label-read-as-substance.md`](findings/2026-09-01-label-read-as-substance.md).
  1. `docs/ESTATE.md:85` — `superbot-next` called a finished rebuild; the
     reversing qualifier was in the same cell, ~400 characters on.
  2. The owner was asked to re-name the successor hub. Settled at
     `docs/decisions.md:650` and twice in
     `planning/2026-08-30-fresh-start-redirect.md`. The boot file's **pointer**
     to that doc was read; the doc was not opened.
  3. A `2026-08-31` date-string match in 10 files reported as 10 citations.
     Nine were.
  4. *"No worksheet is longer than 44 lines"* carried forward into
     `owner/intent-workbooks.md` **in the same PR that shipped worksheets at 46
     and 47.**
  5. `docs/MAP.md` proposed as the source for a `docs/` index without being
     opened. It is the **repo-wide** router — its rows cover `.claude/`,
     `.sessions/`, `scripts/`, `tools/`, `bootstrap.py` and `../`.
  6. The door test's level 4 graded from `ls` output alone, **inside the
     document written to describe this very trap**, after five instances had
     already been recorded (regraded, fm #1004).
- **ROUTE** — `listing-is-not-reading` (Bash/Edit/Write, `repeat: true`).
  **Coverage is partial and the split is the point:** the route reaches the
  *sub-file* half — instances 1, 3, 6, where the thing was located and then
  under-read. Instances 2 and 5 are the *never-opened* half, which is
  `.claude/hooks/read_before_write.py`'s existing job. Instance 4 — an
  inherited sentence restated without testing it — is **undelivered**, and a
  checker for it would have to know which claims are inherited.

---

## TRAP-009 · A review loop with no exit condition

- **TRIGGER** — you are about to post a fourth `@codex review` on the same PR,
  or you are re-requesting a round because the previous one "still found
  something".
- **WHY** — three things combine, and none of them says stop. (1) A review
  binds the head it ran on (TRAP-007), so every fix commit is a new head that
  "needs" a round. (2) A reviewer shown a long prose document returns a P2
  almost every time — and on fm #1010 five of the seventeen rounds (5, 10, 12,
  16, 17, by the session's own per-round accounting) found only drift the
  previous round's *own fix* had caused, because the report restated the same
  facts in six places (front-matter summary, § 3, § 5's closing note, § 10, the
  session card, the CONTRACTS sheet) and every correction had to be propagated
  to all of them. (3) The cloud harness's own drive-to-green text reads *"there
  is no round limit: repeated findings on your pushes mean fix the root cause,
  not stop"*, and the session quoted it back in its round-13 comment. "One
  clean round" is therefore not a reachable exit; the loop ran from the first
  request at `02:53Z` to the seventeenth verdict at `06:30Z` and ended only
  when the owner stopped it by hand.
- **REQUIRED PREVENTION** — three rounds, then out: fix what round three
  found, verify the fix without Codex (free-key Gemini, [D-0019], or a direct
  check against source), disclose the residue in the PR comment and the card,
  then flip — or hand off with the state written down. And the structural
  half: **one canonical place per fact.** A number or a mechanism claim lives
  in one section and every other surface points at it; the night session did
  this for the round count at round 7 and for nothing else, which is why the
  drift rounds existed.
- **VERIFY** — each `@codex review` request prints `Codex review round N of 3
  on PR #…` in the tool result; the fourth is denied with the exit spelled
  out. No count means the guard did not load — root is not this repo (boot
  triad case two or three), so run `tools/install_root_hooks.py --apply`.
- **ORIGIN** — `MEASURED` 2026-09-02, fm #1010: 17 review objects on 17
  successive heads (`94af16e` → `8470c9d`), 88 inline review threads, first
  request `02:53:25Z`, last verdict `06:30:05Z`, 26 commits on the PR. The
  rounds were not worthless — factual reversals of the report's own content
  landed as late as rounds 11 (a wrong measurement spliced into a survivor; a
  percentage correction that was itself backwards), 14 (a wrong cause
  attribution; a marker-presence figure read as behavioural compliance) and 15
  (round 14's own diagnosis, wrong) — which is exactly why the exit is
  *disclose-then-flip*, never *merge-regardless*. The rule that should have
  prevented the loop existed: [D-0019], 2026-08-29, *"I don't think It's
  necessary to review after every push, that just wastes the usage limits"* —
  prose in the boot file and the ledger, delivered at no moment. Owner, live,
  2026-09-02: *"I thought there was a rule to prevent this from happening.
  Apparently not a good rule. I think there should be a maximum of 3 review
  rounds at most, never more than that."*
- **route** — none; delivered by a **denying hook** instead,
  [`.claude/hooks/codex_round_guard.py`](../.claude/hooks/codex_round_guard.py)
  (`PreToolUse` on the MCP comment tools and on Bash POSTs to a comments
  endpoint), because a count needs no judgement and a route's reminder would
  be the fourth statement of a rule that three statements did not deliver.
  Suite: `tools/test_codex_round_guard.py`. Decision: [D-0039].

## Coverage — stated so the gap is visible

| trap | delivered by | deterministic checker |
|---|---|---|
| TRAP-001 | 2 routes | not yet — a checker would need to tell a citation from a measurement |
| TRAP-002 | 1 route, fires pre-execution | ✅ **`tools/check_pipe_exit_code.py`**, in the `check --strict` gate |
| TRAP-003 | 1 route | not yet |
| TRAP-004 | 1 route | not yet |
| TRAP-005 | **none** — see its entry | no |
| TRAP-006 | **2 routes** — `card-flip-before-push` (Bash/push) + `card-status-write` (Edit/Write/MultiEdit) | not yet — the check would have to read the PR that does not exist yet |
| TRAP-007 | **2 routes** — `card-flip-to-complete` (Edit/Write/MultiEdit, matches the completion transition) + `card-flip-before-push`, now `repeat: true` so it is never spent | not yet — a checker would have to know a review was *requested*, which is PR state, not tree state |
| TRAP-008 | **1 route** — `listing-is-not-reading` (Bash/Edit/Write, `repeat: true`); reaches instances 1, 3, 6. Instances 2 and 5 are `read_before_write.py`'s; instance 4 is **undelivered** | not yet — a checker would have to know which claims are inherited |
| TRAP-009 | **no route — a denying hook**, `.claude/hooks/codex_round_guard.py` (PreToolUse on the MCP comment tools + Bash POSTs to a comments endpoint) | ✅ the hook **is** the deterministic check — a per-PR count, no judgement; suite `tools/test_codex_round_guard.py` |

**The honest state of this register: nine entries — seven delivered by route (TRAP-006
and TRAP-007 by two each — they share `card-flip-before-push`), one (TRAP-009) delivered
by a denying hook with no route at all, one (TRAP-005) undelivered — and two complete
through the full § 5.4 lifecycle, TRAP-002 by checker and TRAP-009 by the hook itself**
*(re-counted 2026-09-02 when TRAP-009 was added; the sentence below records why the
count is re-read rather than incremented)*

*(This sentence read "seven entries, six delivered" until 2026-09-01, when
TRAP-008 was added directly above it and the count was not re-read. Corrected
in the same change — it is TRAP-008 instance 4's exact class, an inherited
count restated without testing it, committed inside TRAP-008's own PR.)* — mistake → trap entry
→ route → deterministic checker. `tools/check_pipe_exit_code.py` runs in
`python3 bootstrap.py check --strict` via `scripts/preflight.py`, and scans
**executable surfaces only**: `.github/workflows/*.yml|yaml`, `**/*.sh`, **plus
extensionless files carrying a shell shebang** — extension is not the definition
of a shell script, and relying on one leaves a silent gap the day someone adds
`bin/deploy`. It does **not** scan prose: session cards quote this trap
constantly (26 of 389, fm #915), and a checker that fires on its own
documentation gets ignored.

**The exemptions are positional, and that distinction is the whole point.**
`PIPESTATUS` exempts when read *within the window*, at the use site.
`set -o pipefail` exempts only when enabled on a **non-comment line above the
pipe**. The first version of this checker substring-searched the whole file, so
`pipefail` set *after* the pipe, inside a subshell, or merely named in a comment
silently exempted **every** pipe in that file — miss-biased far past what
"exempt the fix" requires, and a good example of a checker that looks like it
works. *Honest limit:* `pipefail` set in a sourced file, or in a function
defined above and called below, is not tracked. The bias stays toward missing a
real instance rather than crying wolf.

**Verified by positive control, not by a clean run** — a clean result from a
broken checker is TRAP-003 itself. 8 fixtures: the plain instance, `PIPESTATUS`,
`pipefail`-before, `||`, `pipefail`-after, `pipefail`-in-a-comment,
`pipefail`-in-a-subshell, and an extensionless shebang script. **5 flagged, 3
passed, zero false positives** — and four of those five were missed by the
first version. `fleet-manager` itself is clean at 18 files, which means more
now than it did before the hardening.

**The remaining four stay at route-level** until an instance shows what a
checker would have to catch. Guessing at one now would produce an instrument
that fires on the wrong thing.

### The coverage boundary, stated because it was found the hard way

**Routes fire on tool calls, not on chat replies.** `route_docs.py` matches
`tool_input` — an `Edit`/`Write` payload or a `Bash` command — so a trap
committed in prose *to the owner* passes every route here untouched. This was
measured immediately: the session that shipped TRAP-004 committed TRAP-004 in
the same message, writing *"full workspace sweep"* before establishing that the
credential could see the whole account. The register caught nothing, correctly,
because no file was written. Closing that would need a different mechanism than
a `PreToolUse` hook — the owner-review Stop hook is the surface that already
reads replies, and pointing it at this register is a candidate next slice, not a
claim that it works today.
