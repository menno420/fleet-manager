# 2026-08-25 — E1: the owner's revision pass, executed against three live calls

> **Status:** `in-progress` — **born red on purpose**, branch
> `claude/final-eap-review-mail-3iw41z` restarted from `origin/main` at `9b2d83a`
> (fm #945 merged; the prior branch `claude/final-eap-mail-x2s9kx` is spent — all
> three of its PRs squash-merged, nothing stacked on it). Flips to `complete`
> only after `python3 bootstrap.py check --strict` returns a real exit 0 read
> directly, never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

The mail was assembled and unsent. This session did **not** draft, send, or
restart it. It did three things: re-measured the one figure the whole length
decision turns on, put the open question to the owner instead of filling it in,
and then executed the three calls he made.

## 🔢 The re-count, because the number moved every time it was told

The handoff's first instruction was to re-count the COPY block, and the reason
is visible in the result — **three committed places carried three different
numbers, and none of them matched the file**:

| where | said | the mail as pasted |
|---|--:|--:|
| the draft, § 2 item 6 | 2,082 | **2,097** |
| `docs/owner-queue.md` | 2,127 | **2,097** |
| the handoff prompt | 2,151 | **2,097** |

**None of the three was right, and neither was the first re-count.** The method
was never stated, and both obvious methods are wrong. Substituting a space for
each emphasis mark splits `**fortnight**,` into `fortnight` + `,` and counts the
bare comma as a word (**+8**); deleting the marks instead leaves the links
block's `-` bullet glyphs standing as words (**+4**). This session's own opening
measurement — **2,151**, the figure put in front of the owner with the length
call — carried the first of those errors and was inflated by ~2.5 %. Counting
the plain text that actually gets pasted gives **2,097**.

**It did not change his decision**, which is why the correction is recorded
rather than re-asked: 2,097 words against a one-page cap is the same call as
2,151, and he chose on the direction. The record now carries the checkable
number, and the number now comes from `python3 tools/render_eap_mail.py --count`
rather than from prose that goes stale — which is the only fix that has ever
worked here.

The route prices were stale by more than the total was. The literal-cap route
was quoted at **~1,227** in one place and **~1,434** in another; measured, the
route lands at **1,473**. *(This session's own first answer here — "~1,478–1,503"
— was computed with the same defective methods described above, and is corrected
for the same reason.)*

## 🔗 The mis-numbered call, which five documents inherited

The length conflict is **item 6** in § 2. It is referred to as **"call 5"** in
five places: § 1 decision 7, § 2 item 7 (three times), and the owner-queue
entry — and the handoff prompt for this session inherited the same error.
Item 5 is the *code-quality restraint* note, which has nothing to decide in it.
Anyone following the pointer landed on the wrong item. Fixed at every site.
§ 2's sending gate also said *"the six calls below"* under a header saying
**seven**; the header was right.

## ❓ The one question, asked rather than filled in

His send-day plan said *"a revision pass and my own section added/edited"*.
`fm #945` recorded, as a P1, that the sentence names **no target** and does not
say whether that is one operation or two — and that a session must not fill it
in. It was put to him at the start, before any edit.

**His answer: two operations, and the revision pass targets the whole
document** — § 1 and § 2 included, not only the COPY block. He reads and
directs; the session executes.

## ✅ The three calls he made, and what each did to the mail

1. **Length (item 6) → the literal cap.** Findings 1–3 keep, **findings 4 and 5
   out**, asks 1–5 keep, **asks 6–14 out**.
2. **The 97.5 % (item 2) → cut the ratio, keep the shape.**
3. **Two ops, whole doc** — recorded above.

**The ratio is cut without losing the evidence.** The contested computation was
the *derived percentage*: the audit's prose says 97.5 % of the 939 MB `public`
schema, its own rows sum to 925 MB = 98.5 %. The rows themselves are not in
dispute, so the mail now quotes them — **949 MB store · 925 MB in three
ingestion-history tables · ~10 MB across every other table combined** — and carries no
percentage at all. That is strictly stronger than either side of the
contradiction and resolves nothing on his behalf.

**Part 2: 2,097 words → 1,473 by the cut → 1,481 as it now stands**, the
difference being the eight-word census fix at consequence 5 below.

## ⚠️ Five consequences, surfaced and not resolved

Each is one line to overturn; none was decided for him.

1. **Ask 8's venue asymmetry is gone** — the 2,115 branches / ~50 PRs figures
   the draft itself calls *"the strongest single argument in the estate"* sat in
   asks 8–9, which the cap removes.
2. **The prior-mail pointer left with them.** Asks 6 and 7 were the only place
   Part 2 pointed back at what the four earlier mails argued — which § 1
   decision 2 requires. The July findings link is **re-labelled to carry that
   pointer itself**, at a cost of ten words, rather than being left orphaned at
   the foot of a mail that no longer references it.
3. **The month-after spine narrows from five findings to three**, and the
   month-after *is* § 1 decision 1's whole rationale for the mail.
4. **Optional finding 6 is dropped**, per item 7's own stated conditional
   (*include on the keep-the-length route, drop on the literal-cap route*) —
   a resolved conditional, not a new decision. It stays drafted; 193 words to
   put back.
5. **Eight words were added — the only content this session added to the mail.**
   The scale paragraph accounted for 19 + 1 of 27 repositories and left **seven
   unexplained**; six adversarial rounds passed over the gap. The sweep has them
   (*created after the program closed*, 7 as of 08-24) and they are **evidence
   for the spine, not filler** — repositories created *after* the program is
   precisely what § 1 decision 1 says the mail exists to report. This is a new
   observation, not a re-opened round.

**Still his, and still open:** item 1 (does he remember sending the capability
pack) and item 3 (his hosting bill in a vendor mail) are **both moot under the
cap** — ask 12 and the €30 lived in the cut material. Item 4 is moot for the
same reason. What genuinely remains is **Part 1, which no session writes**, and
sending.

## 🛠 `tools/render_eap_mail.py` — because the block is markdown and the mail is not

A second send-day defect, unflagged anywhere: **Part 2 carries 27 bold and 12
italic spans** (`--count`) **and hard wraps at 76 columns.** *(This line said
"~90 bold spans" — asserted, never counted. Corrected 2026-08-25 rather than
left standing above the review table below that concedes it: an appended
concession that does not retract the original is the defect this whole mail
reports.)* Pasted straight into a Gmail compose that
is exactly what the vendor reads — literal asterisks through the whole argument,
and wrapping that re-breaks raggedly at their client's width. Six adversarial
rounds and four prior sessions never surfaced it, because every one of them read
the block as markdown, which is the one context where it looks right.

The fix is **not a rendered copy committed beside the source** — that is the
append-without-retract defect finding 2 of this very mail reports, and it would
drift within a day. It is a renderer over the single source: plain text with
paragraphs unwrapped, `--html` for rich paste, and `--count`.

**`--count` is the real payload.** The number was stale in three places and
*wrong in all three*; the fix for that is one command, not a fourth sentence
stating it. Per the kit's own rule — *a check whose failure mode is silence must
be shown to fire* — it ships `--selftest` (13 assertions), and the selftest was
**mutation-tested**: disabling the bold-strip, disabling the paragraph unwrap,
breaking the marker bounds, collapsing the ordered/unordered split and numbering
the bullets each produced **exit 1, all five caught**.

## 🔍 Two claims checked after owner-review asked what was behind them

Both were carried from repo records rather than measured by this session. One
still is; the other is now measured.

1. **"Four of his sent EAP mails are no longer retrievable from Gmail."**
   `MEASURED-PRIOR`, not
   by this session — [the correspondence record](../docs/findings/2026-08-09-eap-correspondence-record.md)
   § 0, which records **five probe runs over four query strings with two
   positive controls** (one per lane) on 2026-08-24. Thread A holds two messages
   where five were recorded; the missing four are the 07-08 introduction review,
   the 07-12 scale-up report, the vendor's 07-14 acknowledgement and the 07-16
   01:52 classifier report. **This session has no Gmail measurement of its own**
   and did not open that file until owner-review asked. **The scope matters:**
   what was measured is *retrievability* — thread A returns two messages where
   five were recorded, with trash covered in one of the two lanes. It is **not**
   a finding that the mails were destroyed, and the record explicitly says no
   cause is recorded and none should be inferred. The § 3 send-record rationale
   rests on that dated finding, not on anything measured here — and it survives
   either reading, since a mail the owner cannot retrieve is not an archive
   whether or not it still exists somewhere.
2. **"Seven repositories were created after the program closed."** Was one table
   row in the sweep. **Now measured directly** — `GET /user/repos` paginated over
   the direct-PAT path, bucketed on `created_at` against the 07-07 → 07-21
   fortnight:

   | bucket | n |
   |---|--:|
   | predating the fortnight | 1 (`superbot`) |
   | inside 07-07 → 07-21 | 19 |
   | **after the close** | **7** — `proxybench` 07-22 · `shiftlife` 07-24 · `spider-swing` 07-28 · `Substrate-kit-app` 08-04 · `estate-backups` 08-16 · `couch-legend` 08-20 · `spider-bot` 08-24 |

   1 + 19 + 7 = 27, matching the account total. The eight words added to the mail
   are correct, and are now backed by a measurement rather than by a row.

## 🔎 Codex round 1 — 9 findings, **9 `[conceded]`, 0 `[survived]`**

Answered at `d7b37d0` after four requests went unanswered past the measured
~335 s (three of which this session invalidated by pushing under them). One P1,
eight P2. Every one was real.

| # | pri | finding | disposition |
|---|---|---|---|
| 1 | **P1** | ask 5 called the DB remainder *"actual user data"*; the audit's next row is 8.4 MB `ai_decision_audit` — itself an audit/history table — plus ~2 MB incl. server logs | `[conceded]` — reworded to *"about 10 MB across every other table combined"*, a storage remainder rather than a user-data subtotal, and **retracted in the sweep too**, where the phrasing was inherited from |
| 2 | P2 | the emphasis figure was wrong in the draft (56 italic / 83 total) **and the program-ledger row still said `~90 bold`** | `[conceded]` — the draft was already fixed; **the ledger row was not, and I had not checked it** |
| 3 | P2 | plain-text bullets rendered as bare two-space indents, so the four links read as unrelated paragraphs | `[conceded]` — visible `- ` glyph; punctuation-only tokens are excluded from `count()`, so no figure moved |
| 4 | P2 | `--selftest` checked `**` and backticks but **not single-asterisk italics** — `*Because*` could render literally and still pass | `[conceded]` — three assertions added; 10 → 13 |
| 5 | P2 | `strip_marks()` flattened `[label](url)` to `label`, dropping the URL — and **`--verify` was blind to it**, applying the same transform to both sides | `[conceded]` — links now render `label (url)`. 0 markdown links in the block today, so no figure moved; it stops a future one vanishing |
| 6 | P2 | `--count` computes but does not **enforce**: the number is hard-coded in five living documents | `[conceded]` — [`check_eap_figures.py`](../tools/check_eap_figures.py), which reads the number out of the prose and compares it |
| 7 | P2 | the output modes were not mutually exclusive: `--html --count > mail.html` exits 0 and writes the **count report** into the file the owner then pastes from | `[conceded]` — argparse exclusive group; the conflict now exits 2 |
| 8 | P2 | the owner-queue said *four* consequences; the draft has five | `[conceded]` — item e added to the queue with its overturn line |
| 9 | P2 | § 2's heading said *three of the seven calls answered*; only **two** are numbered calls, the third answers the separate revision-scope question | `[conceded]` — heading and lead corrected |

**Finding 6 proved itself within the hour.** Fixing the P1 added four words to
ask 5 — **1,477 → 1,481** — which silently falsified **nine** figures across five
documents. The new checker caught all nine. That is the same defect as everything
else this session found, committed by the session that was documenting it.

**And the checker's first version could not have caught them.** It searched each
file for the literal `"1,477"` and compared `int("1,477")` against the computed
`1477` — an `X != X` condition, structurally incapable of failing. Three further
attempts died the same way: a pattern searching a file that lacked the phrase,
then patterns broken by the docs' 76-column hard wrapping, then escaping that
turned `\d` into a literal backslash-d. Each printed **CHECK CANNOT FAIL**
rather than a clean pass, which is the only reason any of it was caught. That is
finding 6 of the mail — *a check whose pattern could not match what it was
searching for, so it could not fail* — reproduced four times over.

## 🔎 Codex round 2 — 5 findings, **5 `[conceded]`, 0 `[survived]`**

At `292327e`. Four P2, one P3. **Two were defects in the checker built to catch
exactly this class**, which is the whole lesson of the round.

| # | pri | finding | disposition |
|---|---|---|---|
| 1 | P2 | `re.search` validated only the **first** occurrence — a stale duplicate in a second document passed because an earlier correct copy satisfied the pattern | `[conceded]` — `finditer`, every occurrence, every file, reported with `path:line` |
| 2 | P2 | the docstring advertised **five** consumers and the code loaded **two**: `owner-queue.md`, `current-state.md` and the § 7 ledger could rot while it exited 0 | `[conceded]` — `CONSUMERS` is now the list, and 15 occurrences across 5 files are checked |
| 3 | P2 | the queue said *"the mail as pasted is 2,097"* — that is the **pre-cut baseline**, contradicting its own `2,097 → 1,481` line one paragraph above | `[conceded]` |
| 4 | P3 | the ledger recorded `--selftest` as **7 assertions** and the tool's docstring still claimed a `9/10` mutation result, both stale after the count reached 13 | `[conceded]` — **and the rewritten checker found a second site Codex had not flagged**, in this card |
| 5 | P2 | this card still asserted **~90 bold spans**, unretracted, directly above the table conceding it was wrong | `[conceded]` — retracted in place |

**Finding 5 is the mail's own thesis, committed inside the record of conceding
it.** The card contained both the original claim and its concession, and left the
original standing — *an appended correction that fails to retract what it
corrects*, which is finding 2 of the outbound mail, in the document reporting
finding 2 of the outbound mail.

**And the liveness probe took three tries to become real.** Corrupting the
literal `"the route lands at **"` was a **no-op**, because the card hard-wraps
between *route* and *lands* — the same wrap defect that had already broken the
patterns once. Rewritten to corrupt by regex. It then still failed, because the
corruption value `9,999` does not match a `(\d+)` group, so the claim **vanished
instead of mismatching** and the probe reported zero problems on a document it
had just broken — visible only as the occurrence count dropping 15 → 14. The
probe now uses a value that still matches, and **asserts the occurrence count is
unchanged**, because a corruption that deletes the claim proves nothing.

Four distinct ways for a check to pass while being incapable of failing, all in
one file, all found by writing the corruption down and watching it not fire.
**Round 3 found a fifth.**

## 🔎 Codex round 3 — 1 finding, **1 `[conceded]`, 0 `[survived]`**

At `efa8b28`. One P2, and it is the fifth way this file has found to pass while
unable to fail — this time in the guard added *last* round to stop the fourth.

**The unchanged-occurrence-count invariant compared the poisoned copy against the
same possibly-incomplete input, so it could not see a claim that had vanished
before the probe began.** Because occurrences were counted **globally**, rewording
the card's `` `--selftest` (13 assertions) `` left the program ledger's copy
satisfying the pattern: total unchanged, no MISMATCH, exit 0 — on a document
whose claim was now unguarded.

**Fixed by pinning the inventory per pattern AND per file** (`EXPECTED_INVENTORY`,
16 locations), and checking the shape *before* the values: if a claim is gone, no
amount of value-checking on what remains can tell you. **Verified against the
exact scenario Codex described** — rewording that one line now yields
`CLAIM VANISHED: claim[11] in .sessions/2026-08-25-e1-owner-revision-pass.md —
expected 1, found 0`, exit 1; restoring it returns exit 0.

One cosmetic defect fixed alongside: folding inventory drift into the value-problem
count made the liveness probe print *"did not fire"* on any run that was already
failing for a different reason. The verdict is now computed from value problems
only, so it stays honest while the run fails.

**The count is now five, and every one was found the same way:** by writing down
what corruption *should* trigger the check and watching it not trigger.

## 🧪 "No mail client is reachable" was a wall, and it took one probe to fall

This session wrote, twice, that neither rendered output could be tested because
no mail client exists in the container — and **tried nothing** before saying so.
Owner-review asked which paths had been tried and what a different one would
look like. The answer was *none*, and there were three:

- **Headless Chromium is installed** (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`;
  `which chromium` returns nothing, which is what the first look relied on).
  Rendered: **27 `<strong>`, 12 `<em>`, 9 `<li>`, 2 lists, 12 paragraphs all
  survive; 0 literal asterisks.** The DOM's 27/12 emphasis split independently
  confirms `--count` by a completely different route — a regex and a browser
  engine agreeing.
- **Structural validation** via stdlib `HTMLParser`: no unclosed tags, no
  mismatched closes.
- **`--eml`**, now shipped: a real `multipart/alternative` message with
  `text/plain` and `text/html`, which parses back through Python's `email`
  module and **opens in Gmail, Thunderbird or Mail**. The owner can see the
  recipient's view before sending. Headers are blank by design — it previews,
  it never sends.

**What is still genuinely unverified** is narrower and worth stating that way:
how *Gmail's editor* treats a paste, which is a property of that editor, not of
the file. The `.eml` is the closest available answer.

**The pattern this belongs to.** `CONSTITUTION.md` and `docs/CAPABILITIES.md`
forbid recording a limitation, and the reason is exactly this: the wall was
written from *one absent binary on `$PATH`*, and it would have shipped as a
standing fact about what this estate can test. Three paths existed. The rule
held; the session did not.

## 📌 The thing the mail's own subject argues for

`OQ-E1-FINAL-EAP-EMAIL` has to be closed with the sent date, subject and
**message id recorded into the repo** — because § 0 of the correspondence
record measured that **four of his own sent mails are no longer retrievable
from Gmail**. § 3 of the draft asked for none of that. It does now.

## previous-session review

fm #945 recorded the owner's send-day sentence verbatim and, correctly, refused
to decompose it — its own P1 was an earlier version of that entry doing exactly
that. This session is the follow-through: the sentence was **put to him** rather
than read, and his answer (*two operations, whole document*) turned out to be
**wider** than the reading fm #944/#945 had been guarding against, not narrower.
The guard was right to hold; the answer was worth the one question.

fm #943's draft and fm #944's scoping both stand. The two defects fixed here
are in what they merged: a word count that was stale in the draft and stale
again, differently, in the queue; and a cross-reference to "call 5" that has
pointed at the wrong item since the search-index call was withdrawn into a
callout and renumbered everything after it.
