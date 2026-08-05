# 2026-08-05 · hub — settle how Play testers are actually admitted

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **the honest null was hiding a decision, not a detail.** The
Play findings doc recorded tester mechanics as unverified and moved on. That
looked like a small gap. It was not: inside it sat the answer to "how does a
person actually get this game", and one of the two obvious workarounds turns out
to be unavailable by construction while the other is unadvertised.

An honest null is only honest about what it *knows* it is missing. This one was
filed under "mechanics" — a detail-shaped word — and detail-shaped nulls do not
get re-opened, because nothing about them signals that a decision is parked
inside. Worth a habit: when writing a null, say what would *change* if it were
resolved. "Unverified: tester opt-in mechanics" invites a shrug. "Unverified:
whether testers can enrol themselves" does not.

## previous-session review

PR #752 synced the owner queue to the decided name. Since then the owner
published a signed bundle to the internal testing track, found the opt-in link
Console shows, and asked whether pressing it enrols someone. It does not — and
the question exposed that the queue's recruiting advice was thinner than the
schedule advice sitting next to it.

## What landed

- `docs/findings/2026-08-05-google-play-submission-requirements.md` — new **§ 8b**
  with per-track admission quoted from the fetched page, three carry-forward
  consequences, and a **narrowed** null.
- `docs/owner-queue.md` — `OQ-PLAY-CLOSED-TEST` gains the recruiting route it
  lacked and the open-testing correction.

## Measured

Three things the fetched pages settle, each of which had a plausible wrong
answer in circulation *in this session's own chat*:

1. **The opt-in link is an enrolment page, not an invitation.** *"If you're
   running a closed test with a Google Group, users need to join the group
   before opting into your test."*
2. **Open testing cannot come first.** *"Open testing is available when you have
   production access."* Production access is what the closed test unlocks, so
   the ordering is closed → production → open. This session had already named
   open testing to the owner as an available alternative. It is not one, and the
   correction was stated to him plainly rather than quietly fixed in a doc.
3. **Google Groups is the only self-serve admission path before production** —
   groups offer *"Anyone can join"*, and closed testing is the only track that
   accepts groups.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Every quoted sentence comes from a page fetched this session
  ([answer/9845334](https://support.google.com/googleplay/android-developer/answer/9845334),
  [answer/14151465](https://support.google.com/googleplay/android-developer/answer/14151465),
  [groups/answer/2464926](https://support.google.com/groups/answer/2464926)) —
  none from a research model's summary. The prior pass's tester paragraph came
  back ungrounded from a model and was filed as NULL rather than asserted, which
  is the reason there was nothing to retract in the docs.

**Honest null, narrowed not closed:** the closed-track opt-in URL *format*. The
internal link Console shows for this app is `/apps/internaltest/<numeric-track-id>`,
so the widely repeated `/apps/testing/<package-name>` cannot be assumed to be the
closed shape. Console prints the real link.

**Unchanged nulls:** store graphics are still not produced, the privacy policy is
still unhosted, and trademark clearance is untouched.
