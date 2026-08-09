# 2026-08-09 · hub — the kit upgrade's payload question, settled; and the EAP correspondence committed

> **Status:** complete

- **📊 Model:** opus-5 · high · feature build — work OD-13 (kit upgrade first),
  carrying the EAP reconciliation as a live secondary thread

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/kit-upgrade-eap-reconciliation-e9poz5` (restarted from `b10b38c` =
`origin/main` after #830/#831/#832 merged)

💡 Session idea: **the upgrade's premise was never checked, and it is false.**
The plan said "establish which released kit carries `ADVISORY_CENSUS`, then
upgrade to it." The honest answer is **none does** — it landed on substrate-kit
`main` on 2026-08-06, sixteen days after the last release, and sits under
`## [Unreleased]`. So there is no version to upgrade *to*; the payload has to be
*cut* before it can be adopted. That is a different task from the one that was
planned, and the difference was one clone away for two sessions.

Layer-2 handoff: null (fleet-manager itself; substrate-kit cloned read-only for
the version question, not attached for push)

## Previous-session review

⟲ fm #830 recorded the vendored kit as `1.20.1` with **no** `ADVISORY_CENSUS` in
any vendored Python, and was careful to label the *other* half `UNVERIFIED`:
*"Whether any released kit carries `ADVISORY_CENSUS` in executable code was NOT
verified — substrate-kit was never attached."* fm #831 carried that forward
unchanged. This session attached it and answered the question. **The card that
declared the gap is the reason it got closed** — the `UNVERIFIED` label survived
two handoffs intact and pointed the next session straight at the one missing
measurement. That is the certainty legend doing exactly its job.

## What is about to happen

1. **Settle the payload question** against the released artifacts, not the
   changelog prose. *(done — § below)*
2. **Commit the EAP correspondence record**, verified against Gmail rather than
   relayed, and link it from the E1 plan's § 2.
3. **Put the upgrade fork to the owner** with the measurement in hand, because
   the only route to `ADVISORY_CENSUS` is cutting a substrate-kit release, and a
   release is outward-facing and ships to twelve adopters.

## Verification

At close: `python3 bootstrap.py check --strict`, both checkers directly, and
`tools/test_change_guard.py`, real exit codes, each on its own line, never `$?`
after a pipe. Codex review requested while this card is born-red.

## The payload question, settled three ways

`MEASURED` 2026-08-09. Each leg carries its own positive control, per the § 5
rule promoted into `capability-probe` step 3b — the rule exists because this
estate twice read "I found nothing" as "nothing is there", and one of those two
times was about **this exact symbol**.

| leg | result | positive control |
|---|---|---|
| released asset — v1.20.2 `bootstrap.py` (1,345,814 B, sha256 `48ecd478…`) | **0** occurrences of `ADVISORY_CENSUS` | 32 occurrences of `KIT_VERSION` in the same file |
| released asset — v1.20.1 `bootstrap.py` (1,326,908 B, sha256 `d6c4f815…`) | **0** occurrences | 32 occurrences of `KIT_VERSION` |
| tag containment — introduced by `b505d13` (substrate-kit #577, 2026-08-06) | `git tag --contains b505d13` → **empty**, over a **complete** tag set (see below) | the same command on v1.20.1's commit returns `v1.20.1`, `v1.20.2` |
| changelog section | the entry is at `CHANGELOG.md:75`, under `## [Unreleased]`, above `## [1.20.2] - 2026-07-21` | section boundaries computed, not eyeballed |

**The asset leg is the one that decides it**, and it is the one a changelog read
would have skipped: adopters vendor the published `bootstrap.py`, so what that
file contains *is* the payload. The other three legs agree with it, which is why
they are worth recording — three methods agreeing is what makes this a settled
question rather than one more `UNVERIFIED` row.

**The tag leg needed its own completeness check, and it did not have one when
first written.** `git tag --contains` reports only the tags *in the local clone*,
so an empty result is equally consistent with "no release contains it" and "the
clone is missing tags" — and the clone started life as `--depth 1`. Codex raised
exactly this on fm #833 (P2). The gap was in the record, not the fact:
`git fetch --unshallow --tags` had already run (exit 0), `git rev-parse
--is-shallow-repository` returns `false`, and the tag set is **complete by
enumeration — 26 tags locally, 26 from the GitHub tags API, same newest five.**
Recorded here because a leg whose completeness is assumed is not independent
evidence, and this file claimed three independent legs.

**Also measured, and it removes the risk that made this fork look heavy.**
fleet-manager's vendored `bootstrap.py` is **byte-identical** to the released
v1.20.1 asset (same sha256) — clean vendoring, no local drift to reconcile. And
running substrate-kit main's built `dist/bootstrap.py` against this tree:

```
gate-preview — 9 deterministic site(s) in the census; 0 carry findings here
(0 finding(s)). Promoting the pending ones would red this tree: NO.
94 heuristic advisory finding(s) across 6 checker(s) held off the gate channel
```

Exit code 0. So the `[Unreleased]` batch's most consequential item — promoting
six advisory sites to exit-affecting — **would not red fleet-manager**, and the
94 advisory lines that currently bury the verdict at line 92 are exactly what
`ADVISORY_CENSUS` routes off the agent's channel. The probe wrote nothing beyond
the expected guard-fires telemetry append.

## The EAP correspondence — verified, not relayed

The handoff supplied these as facts to commit. They were **derived by a prior
session and relayed through a prompt**, which is a provenance the estate has
been burned by before (fm #830 error #7: agent-quoted fragments called "owner
messages"). Committing them unchecked would have made a chat transcript into a
repo record without adding any verification — so each was re-measured against
Gmail. **Most held exactly. Three were wrong, and a fourth is uncorroborated —
a different verdict, kept different everywhere it is restated.**

Full record and the four corrections:
[`../docs/findings/2026-08-09-eap-correspondence-record.md`](../docs/findings/2026-08-09-eap-correspondence-record.md).

**The one that matters most: the 07-22 read-only-cutoff report is not
corroborated.** `in:sent after:2026/07/21 before:2026/07/24` returns two threads,
neither of them it — no owner-sent mail exists on 07-22 or 07-23. The positive
control passed (the same query correctly returns the 07-21 sent messages), so
this is a real absence in the sent-mail lane, not a broken query. It is recorded
as **uncorroborated with the query that failed to find it**, never as "did not
happen" — it may live on a surface Gmail does not hold.

## The upgrade — v1.20.1 → v1.20.2, landed

Owner ruling 2026-08-09 on the fork below: **"both, in order"** — take the
released tip now, cut v1.21.0 in a dedicated session. This is the first half.

**sha256 agreed four ways** (the skill demands three): the downloaded asset, the
published `bootstrap.py.sha256` companion, `release.json`'s `sha256` field, and
the kit repo's committed `dist/bootstrap.py` at tag `v1.20.2` — all
`48ecd478…`. Contract: `breaking=false`, `requires_state_migration=false`,
`min_upgrade_from=1.0.0`. Rollback banked at
`.substrate/backup/bootstrap-1.20.1.py` (1,326,908 B). Vendored file now matches
the released v1.20.2 asset byte-for-byte.

### The carve-out the upgrade dropped — caught because the kit said so

`upgrade` regenerated the kit-owned `.github/workflows/substrate-gate.yml` and
**removed the host-added `repo checkers (doc routes + no false walls)` step** —
the one wired 2026-08-06 after conflict markers reached `main` and silently
disabled the doc-routing hook. Measured: **0** checker references in the
regenerated file, **3** in the banked pre-regen copy.

**This is the single most dangerous thing in the upgrade**, and it would have
been invisible in a diff skim: the gate still exists, still runs, still goes
green — while no longer running either checker. The comment the step carries is
its own epitaph: *"Self-enforced meant unenforced."* An upgrade that silently
un-enforces a gate is the same failure one layer up.

**It was not invisible, though** — `upgrade` printed the carve-out, named the
step, and banked the pre-regen file. Credit where due: the kit's carve-out
scanner is exactly the *"a machine sees the defect at the moment"* shape
[`../docs/findings/2026-08-09-error-to-mechanism.md`](../docs/findings/2026-08-09-error-to-mechanism.md)
argues for, and it worked with no prompting.

**The regeneration is not all loss** — it also ADDS two real guards, which is
why reverting it wholesale was wrong: a **claims-only fast-lane guard** (a
`claude/*` work PR whose entire diff is `control/claims/**` rode the fast lane
and auto-merged card-less — the #451 race), and a **verify-suite step** driven
by the interview's confirmed `verify_command` instead of hardcoded pytest. Both
kept; the checker step re-applied by hand alongside them.

**Is there a persistent carve-out convention? Checked, and no — for workflows.**
Asked by owner-review, and it should have been checked before the claim was
made rather than after. The kit *does* run a preserve mechanism, but its scope
is digest blocks, not workflow files: `bootstrap.py:17031-17045` defines
`<!-- substrate-kit:*-digest BEGIN/END -->` fences whose *"bytes between a
BEGIN/END pair are the canonical block"* and which regens preserve — for
`seat-digest.md` and the capability ledger. The byte-for-byte guarantee at
`:18617` covers *planted* docs, which are skip-if-exists.

**The gate has no such path, and the writer says so unambiguously.** Read at
`bootstrap.py:19996-20053`: the carve-out branch at `:20030-20047` computes the
host additions, **banks** the live file to `.substrate/backup/…pre-regen-<digest>.yml`
and **reports** each one — and then, at **`:20048`**,
`atomic_write_text(live_path, expected_text)` runs **unconditionally**, outside
that branch. Nothing merges the banked additions back into `expected_text`.
`gate_carveouts()` (`:19433`) is a **detector**, not a preserver.

**So "the next upgrade drops it again" is now read out of the writer**, not
taken from the upgrade's advice message as it was when first asserted. The
three-way fast path at `:19979-19995` confirms the treadmill from the other
side: it skips banking only when the live file matches the previous template
**byte-for-byte**, which the re-applied step guarantees it will not.

**Why by hand, and why not the kit's advised fix.** The kit says host carve-outs
belong in a separate workflow. That is right in general and wrong here *today*:
`substrate-gate` is the **required** status check, so a separate `host-ci.yml`
would run the checkers without blocking anything until the ruleset also made it
required — a policy change that is the owner's call. Re-applying in place
preserves enforcement byte-for-byte and changes no policy. **The cost is real
and stated: the next kit upgrade drops it again.** The durable fix
(`host-ci.yml` + a required-check ruleset edit) is an owner-gated follow-up, not
a thing to take unilaterally.

### `intake` survived — and that corrects a belief this session inherited

The handoff was explicit: *"After the upgrade, RE-APPLY the intake amendment…
the upgrade is what destroys it."* **Measured, `upgrade` did not.** `intake`'s
live `SKILL.md` is byte-identical across it (sha256 `00d13424…`, 8,929 bytes,
all 8 Phase-2 markers).

**But the destroying step exists, it is named, and this upgrade re-armed it.**
The mechanism, read out of the ledger rather than inferred:
**no kit command ever writes `.claude/skills/`.** `upgrade` stages, and
`skills --build` *also* only stages — `cmd_skills`' own docstring
(`bootstrap.py:24405-24412`) says the kit *"never writes a live `.claude/`
tree"*. `docs/CAPABILITIES.md:635-648` records this as a measured capability, names the
real installer — **a hand-run copy loop**, `.substrate/skills/*/SKILL.md` →
`.claude/skills/*/SKILL.md` — and instructs *"re-run after a kit upgrade"*
(`:645`). The loop itself is a bash `cp` over `.substrate/skills/*/` at
`docs/SKILLS-local.md:95-97`, whose own ⚠ at `:104-106` states the consequence:
*"local amendments to a kit-named skill are overwritten … re-apply them after
every upgrade."*

This upgrade staged **14** skills including `intake` (`.substrate/skills/intake/`
mtime `Aug 9 10:28`) — the same 14 the handoff named — refreshing the
**superseded 3,745-byte body** against the live 8,929-byte one.

**The revert is measured on both operands and the operation, not deduced from
the instruction text.** The loop at `docs/SKILLS-local.md:92-100` is an
unconditional `cp "$d/SKILL.md" ".claude/skills/$n/SKILL.md"` over every staged
directory — no comparison, no skip-if-newer. And the two bodies differ in
exactly the way that matters: the **staged** copy contains **0** occurrences of
the Phase-2 markers (`EXPLICIT`/`ESTABLISHED`/`DERIVED`/`INTENT STATUS`) while
the **live** copy contains **8**. So the loop copies a zero-marker body over an
eight-marker one. *(Both copies contain the string `FULLER PICTURE` once — the
live one only in the note explaining that the old body is gone — so that token
alone does not distinguish them, and the marker count is what does.)*

**So the hazard is live, and its trigger is a documented instruction.** Both
docs tell the next session to re-run the loop after an upgrade; doing so reverts
Phase 2. `docs/SKILLS-local.md:111-112` already carries the ⚠ re-apply table with
`session-close` and **`intake`**, and `intake`'s row had recorded the staged
superseded body as *"verified 2026-08-09 … the copy loop reverts Phase 2 in one
command"* **before this session started** — with a `⚠⚠` at `:114-115` warning it
*"bites on the very next session"*. This was that session. The warning was
correct in substance and **wrong only in which command fires it**: the upgrade
alone did not.

So nothing is withdrawn — only the *attribution* moves, from `upgrade` to **the
hand-run loop**. **`intake` needs no re-apply here** because the loop was not
run; it needs one the moment it is.

**And the corollary is the reassuring half, worth keeping in view:** because no
kit command touches `.claude/skills/`, **hand-authored local skills survive
upgrades outright** — they are only invisible to the generated index.

**This claim took three passes to get right, which is the finding.** Draft 1:
*"staged six kit skills and copied none"* — read off `tail -25` of the upgrade
output and stated as a count over the full set (six was the visible tail,
fourteen was the set). That is fm #830's error #17, **generalising over a set
never enumerated**, committed inside the write-up arguing against it. Draft 2
named `skills --build` as the installer — contradicted by its own docstring one
read later. Only draft 3 is measured. Both bad drafts came from the same move:
**answering a mechanism question from the nearest artifact instead of the
authoritative one**, when `docs/CAPABILITIES.md` had the whole answer, dated and
evidenced, the entire time. Surfaced by owner-review asking what evidence
established that staging was the complete operation — a question with no answer,
because nothing had been read about the install path.

## The fork put to the owner

Not re-litigating the decided part: he chose **A, kit upgrade first**, and that
stands. What changed is the route, because the destination turned out not to
exist yet. Stated with the measurement, and work continued on the EAP thread
while it was open rather than stopping on it.

**Both answered 2026-08-09.**

1. **Kit route → "both, in order."** v1.20.2 now (done, above); v1.21.0 cut from
   substrate-kit `main` in a dedicated session. That second session owns a
   *release*, not an upgrade — outward-facing, twelve adopters, and a batch that
   promotes six checkers to exit-affecting. It should re-run the `--gate-preview`
   sweep across the adopter trees rather than trusting this repo's zero.
2. **Confidentiality → "narrow the strict rule."** Recorded as the ledger's
   confidentiality decision, with `owner-reflection` § Confidentiality amended so
   its generic style is that file's editorial choice rather than an estate-wide
   prohibition. What stays out: unreleased specifics he has not himself
   published, third-party contact details, credentials.

**The process lesson from how that second one was reached is worth more than the
ruling.** Codex raised it twice; its second point was that leaving it as an open
ruling *"does not mitigate the disclosure"*, because the repo is public and the
push had already happened — **the born-red gate holds the merge and does nothing
about disclosure.** True, and previously unstated anywhere here. For a public
repo a confidentiality question has to be settled **before the first push**. The
ruling went the way that made it moot; that was luck, not process.

## Close-out

**Landed:** the payload question settled three ways · the vendored kit at
**v1.20.2** with the dropped checker carve-out re-applied and **verified running
in CI** — but **only one of the three**, and the distinction is a false-done I
had to be asked about. Step 8 (`repo checkers`) succeeds on every SHA. The other
two carve-outs have **never executed in CI**: the verify-suite sentinel is step
10, skipped on every run because step 9's born-red hold fails first, and the
claims-only `env:` fix is step 6, skipped because this PR is not a control-only
diff. Both are verified **locally instead**, which is weaker and is said so:
the sentinel command emits **0** mtime-fallback lines, and the injection fix was
tested **by exploit** — with head `claude/";exit 0;#` the old interpolated form
exits 0 having never reached the guard body (silent bypass, reproduced), while
the `env:` form reaches it. They first run in CI on the merge commit and on the
next claims-only PR respectively ·
[`../docs/findings/2026-08-09-eap-correspondence-record.md`](../docs/findings/2026-08-09-eap-correspondence-record.md)
committed and linked from the E1 plan § 2 · the confidentiality ruling (ledger
entry + `owner-reflection` narrowed) · the §7 progress-ledger row.

**`intake` is present and needs no re-apply** — live `SKILL.md` unchanged across
the upgrade, 8 Phase-2 markers, sha256 `00d13424…`. The handoff's re-apply step
was **correctly motivated and wrongly triggered**: the destroying action is the
hand-run copy loop, not `upgrade`, and the loop was not run.

**The honest scoreboard for this session's claims.** Each row below was asserted
before it was established, and every one was caught by an instrument rather than
by re-reading.

**There is deliberately no count in this sentence.** It said *"five"*, then
*"seven"*, and both went stale — the second within minutes, because the table
kept growing as owner-review kept finding things. **Three drifts of the same
tally in one file, in the document that records the summary-outlives-its-table
defect.** Bumping the number a third time would have been treating the symptom:
a hand-maintained count adjacent to a growing table is a stale claim waiting to
happen, and the fix is to let the table be the only place the number exists.
Count the rows if you need it.

| claim | first stated as | ended as | caught by |
|---|---|---|---|
| no released kit carries `ADVISORY_CENSUS` | three legs, one silently incomplete | complete by tag enumeration (26 = 26) | Codex P2 |
| the confidentiality carve-out permits this file | cited `owner-reflection` | citation withdrawn; owner ruling obtained | Codex P1 ×2 |
| correction 4 | *"four did not"* / *"appears not to exist"* | uncorroborated, not disproved | Codex P2 |
| `upgrade` reverts `intake` | *"staged six, copied none"*, then `skills --build` | the hand-run loop; measured 0 markers vs 8 | owner-review ×1, then source |
| the carve-out will be dropped again | from the upgrade's advice message | read out of the writer at `:20048` | owner-review |
| `substrate-gate` runs "the" false-wall scanner | as though one existed | **both** run — fm's at `:170`, the kit's via `check --strict` → `:5596` → `:5628` | owner-review |
| a local dist patch is erased on upgrade | quoted `cmd_upgrade`'s **docstring** (`:26887`) as if it were the implementation | true, and I had **watched** it happen — the banked `bootstrap-1.20.1.py` was created while `bootstrap.py` became 1.20.2 | owner-review |
| the v1.20.2 regression has no live impact | inferred from a green gate — *"green, so nothing in the tree has the shape"* | true, but **the gate never opens `.sessions/`**; searched the corpus instead, 0 real occurrences | owner-review |

**Read the counts off the table; this paragraph deliberately states none.**
Three separate versions of it carried numbers and all three went stale as the
table grew — *"Codex ×3, `Stop` ×2"* (mixing **claims** for one instrument with
**findings** for another), then *"5 claims, 6 findings"*, then a headline
*"Seven"* against eight rows. Codex flagged the last one on fm #833: *"leaving
both tallies in this session record recreates the stale-summary contradiction
this edit says it fixes."* It was right, and the fourth attempt is to stop
writing the number rather than to get it right once more.

**Two things the table alone will not tell you, which is why they are here:**

- **Claims and findings are not the same count.** The confidentiality claim was
  caught **twice**, by Codex P1 in two consecutive rounds, so any instrument
  tally is larger than the row count. Mixing the two produced fm #830's error
  #22 — four different totals for one set — reproduced here in the paragraph
  tallying this session's errors.
- **One defect is out of set and stays listed apart:** the quote attributed to
  `SKILLS-local.md` that actually came from `CAPABILITIES.md:645`, caught by
  `read_before_write`. It is a sourcing defect, not one of the claim rows, and
  folding it in was how an earlier draft inflated its own total.

**The pattern under every row is one move:** answering from the nearest artifact
rather than the authoritative one — a changelog instead of the release asset, a
reporting function instead of the writer, a tail of output instead of the set,
an instruction instead of the code. **Availability is not retrieval**, which is
the finding this repo already holds and which this session re-demonstrated five
times while working on it.

**What that says about the instruments, and it is the useful half:** the
adversarial layer is doing the work the author cannot. Codex caught what was
wrong in the *tree*; the `Stop` hook caught what was wrong in the *reply*;
`read_before_write` caught a quote attributed to a file never opened. **Not one was caught by re-reading my own text** — consistent with the
four-session-old result that no mechanism depending on the author noticing has
ever worked here.

**One genuine self-catch exists elsewhere in the session, and suppressing it
would overstate the case.** `check --strict` exited 1 while
`grep -c "HOLD (by design)"` returned **0** — the two disagreed, so the red might
not have been the born-red hold. Investigating found the hold intact under
changed wording (card selection had switched to the merge-base diff once the
branch had an origin counterpart). **That was caught by a disagreement between
two measurements, not by re-reading** — which is the same property the working
instruments share, and the reason it is worth separating from "self-review".

**Provenance of this scoreboard, stated because it is a claim about my own
work:** it is reconstructed from this session's sequence — each correction is
immediately preceded by an instrument firing, and each commit message names the
instrument, so it is checkable in `git log` on this branch. It is **not** an
independent audit, and a defect no instrument caught and I never noticed would
be invisible to it by construction.

## Two safeguards that are weaker than they read — measured, after being asked

Owner-review asked what *enforces* each. Neither answer was what I had implied.

**1 · The four-way sha256 match is a procedure, not a gate.**
`grep -rn "sha256" tools/*.py scripts/*.py .github/workflows/*.yml` returns
**nothing** (positive control: `sha256` appears 32× in `bootstrap.py`, so the
token is findable). **No standing check verifies that the vendored
`bootstrap.py` still matches any published release.** The four-way compare
happens **once**, by hand, at upgrade time — it is the `upgrade-distribution`
skill's step 3, not an invariant.

I described declining to patch the vendored dist as protecting "this upgrade's
integrity property", which implies enforcement. **It is a convention verified
once.** The decision stands and is arguably *more* justified this way — a local
patch would fork the kit silently and permanently, with nothing to detect it —
but the reason is the absence of a gate, not the presence of one.

**2 · The new re-apply table is prose sitting inside an enforced-looking
structure**, which is worse than plain prose. `docs/SKILLS-local.md` **is**
machine-read — `change_guard.py:57` sets `RE_APPLY_DOC` to it and scopes its
lookup to the **⚠ region** (`:78-107`), and `check_doc_routes.py:43` lists it as
a route referrer. But check A fires on **editing one of the 14 kit-named
skills**. It knows nothing about `docs/SKILLS.md` or `substrate-gate.yml`, so
the *"Generated-file corrections to re-apply"* rows I just added are **read by
nothing**. The skills half of that document is enforced; the half I added is
not, and they sit under the same warning glyph.

**That is this repo's own central failure re-committed**: 116 committed
statements caught 0 of 16, and the fix for an unfollowed rule is a mechanism,
never another statement of it. I have written another statement of it.

**Not building the mechanism here, and the reason is not scope alone.** The
decidable moment exists and is check A's exact shape — a `PreToolUse` warning
when a session edits a kit-**regenerated file** rather than a kit-named skill.
But the promotion rule wants a demonstrated failure first, and there is now
exactly one: the checkers step, dropped this session and caught only because the
kit's own scanner printed it. One instance, one catch, zero misses. **Filed as
the obvious next mechanism with its motivating case already in hand** — the
owner's call whether one instance clears the bar.

**Also honest about the fix itself: the sentinel has never run in CI.** The
verify-suite step is `skipped` on every run so far, because step 9 carries the
born-red hold and later steps do not execute. Its behaviour was verified
**locally** — the sentinel reports *"does not exist (advisory — not a
failure)"* and the residual red is the card hold — but **the first real
exercise of that step will be the merge commit on `main`**, which is precisely
the run the fix exists to protect. Stated rather than left for someone to
discover.

## Upstream kit defects found here — moved to a findable home

**Seven defects in substrate-kit v1.20.2**, all found by Codex reviewing the
vendored dist across seven rounds on this PR, with line numbers, reproductions and
a committed A/B harness:
[`../docs/findings/2026-08-09-substrate-kit-defects.md`](../docs/findings/2026-08-09-substrate-kit-defects.md).

**They were written here first, and that was the wrong home** — raised by
owner-review. A session card is a *record of a past session*; the session that
cuts v1.21.0 walks the read path and would never open a dated card it was not
told about. The boot file already records this exact failure: *"a document that
lives only in a handoff prompt is not in the repo."* **A worklist nobody can
find is a false-done waiting to be reported** — the very class this session's
other half is about. One home now, in `docs/findings/`, not two.

**Independent correction, fm #835:** six of the seven live in the kit's own
false-wall scanner — the checker `substrate-gate` runs as a required status
check — and the completed A/B bank now classifies **five behaviours as new in
v1.20.2** (defects 1, 2, 4, 6, 7) and **two as long-standing** (3, 5). Defect 2's
old red is right for the wrong reason because the valid quote-only control also
reds on v1.20.1. The original one-regression headline and six-defect count were
stale even though the canonical finding had grown to seven. That strengthens,
rather than weakens, the argument for the v1.21.0 session budgeting review time
rather than a version bump.


**Left for the owner:**

1. **v1.21.0** — cut from substrate-kit `main` in a dedicated session (his
   *"both, in order"*). That session owns a **release**, not an upgrade: twelve
   adopters, and a batch promoting six checkers to exit-affecting. It should
   re-run `--gate-preview` across the adopter trees rather than trust this
   repo's measured zero.
2. **The carve-out treadmill** — the durable fix is `host-ci.yml` plus a
   required-check ruleset edit. Deliberately not taken: it is a policy change.
   Until then, **every kit upgrade must re-apply the checker step**, and
   `:20048` guarantees it will need to.
3. **E1 itself** — still owner-reserved and now fully sourced.
