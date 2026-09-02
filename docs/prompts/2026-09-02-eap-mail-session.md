# Continuation prompt — the EAP mail session (drafted 2026-09-02, the review sitting)

> **Status:** `reference` · paste-ready, `continuation-prompt` skill shape,
> preflight run at HEAD `e7e91ea` on the review sitting's branch (main at
> `b32e9b2` + fm #1013 once it lands). Written for a fresh cloud session
> booting with **fleet-manager as its root** (boot triad case one — the hooks
> and skills load only there). The owner's words behind every decision below
> are in `docs/findings/2026-09-02-owner-direction.md` § 5b–5d; this prompt
> points at them rather than restating them.

```text
CONTINUE: Draft the final EAP mail — both parts — from the evidence the night
fleet assembled and the owner's answers in the 2026-09-02 review sitting, so
he can read, edit and send it. He sends; you never do.

BEFORE YOUR FIRST TOOL CALL — state the task back, inline in this same reply,
in four labelled lines (never one fused paragraph, never a question):
  HE SAID — the ask in your own words, one or two sentences.
  ALREADY SETTLED — what the repo already decided about it, naming the file,
                    or "nothing found yet".
  I INFER — the specs, constraints and scope the ask implies, and the follow-on
            the owner probably wants but did not spell out. Labelled inference.
  LEAST SURE — the one reading you are least sure of; he corrects it in a word.
Then begin. This is the owner's one cheap chance to correct your aim; a first
reply that only announces your first action spends it.

HOW HE WANTS TO BE SPOKEN TO (owner, 2026-09-02): every message he sends is
acknowledged at the next natural boundary — a step finished, a tool result
read — with how you understood it and what it changes for the task, the way
the four lines above do at start, so he can see whether his intent landed.
One item at a time, plain language, his pace. No fan-out agents unless he
opts in himself; the word "ultracode" in a message of his is a description,
not an opt-in — the harness misread it twice in two days. No agent runs on
Fable unless he asks for it, in words, for that run (the model-tier entry of
2026-09-02 in docs/decisions.md, as amended the same day). His words may be
corrected for spelling and lightly tightened for clarity when quoted, meaning
unchanged — show him the cleaned sentence beside the original when in doubt
(his rule, 2026-09-02, the typo entry of that day, as amended).

WHERE THINGS STAND (verified at HEAD on 2026-09-02 — re-verify first)
- The mail's working file is docs/planning/2026-08-24-final-eap-email-draft.md:
  Part 1 is a beat table with no sentences (his half, reserved until this
  sitting); Part 2 is the COPY block, 1,686 words by
  `python3 tools/render_eap_mail.py --count` (re-derive; never quote a
  sentence about it), rendering loss-free by `--verify`. Its § 1 lists the
  seven decisions the draft made and how to overturn each; its § 2 lists
  the pre-send calls, two answered 2026-08-25, five still open.
- The evidence is docs/findings/2026-09-02-eap-mail-evidence-report.md
  (930+ lines; § 2 the twelve survivors, § 3 the false-done ledger, § 5 what
  the critics found wrong, § 7 the three spines, § 10 the precondition list)
  with raw JSON under docs/findings/data/2026-09-02-eap-mail-evidence/.
- The four sent mails (8, 12, 16 and 16 July) and two unsent drafts (13 and
  18 July) live in superbot at docs/eap/ (anthropic-email-2-draft-2026-07-11.md
  and anthropic-email-4-classifier-regression-sent-2026-07-16.md are the
  sent bodies; fetch over the direct GitHub API with $GITHUB_PAT). What was
  sent, what came back, and what he promised: docs/findings/2026-08-09-eap-correspondence-record.md
  — note its § 0: four of the five thread-A messages are GONE from the
  mailbox; only the 07-16 21:12 and 21:42 messages survive there.
- fm #1013 (the review sitting's PR) carries the sitting's decisions; it
  should be merged when you read this — confirm with the GitHub API. If it
  is still open, its branch is claude/fleet-manager-review-09-02-sokbbp;
  do not build on it — start from main.
- The Gmail MCP server offers create_draft / list_drafts / update_draft to a
  session; whether a session-created draft is visible and editable to him
  in Gmail's own Drafts view is UNMEASURED as of 2026-09-02 (no ledger
  entry). A session can measure only its own half — that the API creates
  and reads back the draft; his half is him opening Gmail and saying so.

READ FIRST (a floor, not a boundary — each verified at HEAD 2026-09-02)
1. docs/findings/2026-09-02-owner-direction.md § 5b, 5c and 5d — his words
   on the mail, on Projects versus sessions, and his twelve answers to the
   sitting's questions; the DERIVED paragraphs are the addendum's spine.
2. docs/planning/2026-08-24-final-eap-email-draft.md — whole file: § 1
   decisions, Part 1's beat table, the COPY block, § 2's open calls, the
   render/verify/figure-check tools table.
3. docs/findings/2026-09-02-eap-mail-evidence-report.md § 10 first (the
   preconditions), then § 5, § 3 (FD-01, FD-02, FD-17) and § 7 (the winning
   spine and its two REQUIRED patches; do NOT copy its text verbatim — its
   finding-6 body carries the A1-6 framing § 2 corrects).
4. docs/findings/2026-08-09-eap-correspondence-record.md — § 2 (the four
   questions never answered), § 3–4 (his two promises; no vendor agenda
   ever arrived), § 6 (the outcome axis).
Then the two sent mails from superbot, read in full — the overlap rule
below cannot be applied from their headings.

DECIDED (do not re-litigate — owner, 2026-09-02, quoted in § 5b–5d)
- A session drafts the mail; he reads, edits and sends. The report stays
  evidence; the draft is built from it and from his answers.
- SHAPE A (owner, 2026-09-02, at the close of the sitting: "I think we can
  go with A"): Part 2 stays as it is — 1,686 words, the one-page cap he
  chose 2026-08-25 — plus ONE addendum of at most ~450 words framed as the
  Projects-versus-sessions answer below, total near 2,100 words; the shape
  all three judges picked, keeping five rounds of verified Part 2 text
  intact. With it: the false-done ledger IN as the evidence that
  verification is the deciding line — FD-01 (a CI step claimed to run the
  tests and did not, green reported on top), FD-02 (a README declaring
  private, eight PR bodies repeating it, on a world-readable repo), FD-17
  narrowed to its one sub-claim; read docs/findings/night-review-2026-07-10.md
  before using FD-01 or FD-02 (report § 10 item 2). And Part 1 DRAFTED by
  you from the beat table and his § 5d opinions, as a proposal he rewrites
  in his own voice — beat 3, the verdict paragraph, is the one only he can
  supply; say so in the card. B (rewrite Part 2 around the month after)
  and C (the strict one-page cap, no addendum) were offered and not chosen.
- The mail is the record of everything for both sides, the research
  interviews included; their overlap does not change it (his answer 6).
- What the addendum SAYS about Projects versus sessions is his — the six
  plus six answers in § 5c–5d are the content, and the DERIVED answer under
  them is the session's ordering of his words, checked with him. The
  addendum's frame is the answer to Anthropic's own question — what
  would make him choose a Project over a session — in his terms: what the
  two share (everything at the level of capability; a session on a wake
  chain is an autonomous worker too), the three things a Project ADDS
  (verbatim delivery of one rule set into every agent, which measurably
  held; a coordinator that is a mind of its own and keeps several agents
  busy all day on generative work; throughput that was worth eight at once
  only under unlimited usage), and the four things it must FIX (working-
  versus-stalled visible on the home screen; a coordinator that cannot
  report an empty queue while orders sit unread; workers that accept the
  coordinator's authority for merges and gated actions; a channel between
  Projects). His claim that the coordinator handles several tasks at once
  better than a session's fan-out goes in marked as his inference, or not
  at all — his own caveat.
- The overlap rule (the draft's own § 1 decision 2, confirmed by the
  sitting's read of all four sent mails): anything already argued becomes
  ONE pointer line. Already sent: scoped pre-authorization / standing
  grants (12 and 16 July); the venue-scoped denial and workers refusing
  the coordinator (the whole 16 July mail); "Project-level continuous mode
  — never sleep" (12 July ask 1); liveness / fleet visibility (12 July ask
  6); an inter-Project channel (12 July); "what did session N do" (12 July
  ask 7, adjacent to Part 2's ask 3). New and worth full words: Findings
  1–3, the outside-vendor review, asks 1, 2, 4, 5, the instruction box as a
  delivery tier that WORKED, the honest-queue ask, "more organized and
  structured documentation" (his answer 4), and the false-done rows.
- Part 1's material is his § 5d opinions: the 50/50 verdict with
  superbot-next as the worked example (built in days against a weeks
  estimate; code sound, functionality not as intended); permissions as the
  one fix, read by him as a bug, so the FEATURE ask he calls fair is "which
  Projects are active"; he reviews finished products, so unmerged PRs are
  invisible to him; "a couple of hours a day", with his own caveat that he
  is not a typical user. Beat 3 (the verdict paragraph) is the paragraph
  only he can supply.
- The two REQUIRED one-clause patches to Part 2 from the winning spine
  (§ 7) are applied; the "21 of 21 incidents with zero fabrication"
  sentence is qualified so it does not contradict the addendum.
- The instruction-box sort in § 5d (defaults / scaffolding / seat-specific)
  is the answer to "what should have been the product's default"; the
  addendum may cite it in one sentence with the public path.
- Confidentiality (the decisions ledger's confidentiality entry): no third-
  party addresses, no unreleased specifics, vendor messages as metadata
  only; his own words quoted — spelling fixed and lightly tightened for
  clarity at most, meaning, hedges and order unchanged. Settle any
  confidentiality question BEFORE the first push, never before the merge
  (the record's § 0 lesson).
- Codex: this is a large documentation change, so it owes a Codex round at
  flip-readiness (the review-cadence decision of 2026-08-29 as amended
  2026-09-02). One round is required; a fix that changes something a
  reviewer would have an opinion about re-requests on the new head; three
  rounds in total at most, and at round three the exit is fix, verify
  directly, disclose, flip (the cap entry of 2026-09-02; the hook counts
  and denies the fourth). Intermediate pushes are verified by a
  direct source check first, the free-key Gemini pass second on
  gemini-3.6-flash, which has its own per-model daily cap; the per-turn
  review hook runs on gemini-3.5-flash-lite, also on its own cap.

REJECTED, AND WHY
- Re-arguing the classifier / venue denial → the 16 July mail is their best-
  documented finding already; one sentence, as the thing that ended the
  coordinator model for him.
- Copying the winning spine's JSON text verbatim → its finding-6 body and
  patch wording carry the A1-6 framing the report's § 2 corrects (Codex,
  fm #1010 round 14).
- Drafting from the report's summaries → Codex caught real inaccuracies in
  its summary-writing twice; read § 2, § 3, § 5, § 10 themselves.
- Any fan-out for the drafting → the owner did not opt in; one attended
  session writes the mail.
- Sending, or creating the Gmail draft with recipients pre-filled from the
  repo → the three cc addresses are deliberately not in the repo; he adds
  recipients himself in Gmail.

OPEN (what would settle each)
- The judges' optional fourth addendum item (a clean result is
  indistinguishable from a check that never ran — ~100 words). Include only
  if he grants the words; two of three judges wanted it.
- The five open pre-send calls in the draft's § 2 (a–e). Mechanical once
  the shape is fixed; put each to him as the one-word answer the draft
  already names.
- Whether a session-created Gmail draft is visible and editable to him in
  Gmail. Two halves: the API half (create, then list it back) is yours to
  measure in the first step below and goes into docs/CAPABILITIES.md as
  exactly that — "create_draft + list_drafts persistence" — with the
  verbatim result; the owner half is recorded only when he says, in words,
  that he saw and could edit it in Gmail. Never record the broader
  capability from the API read-back alone.

YOUR FIRST STEP
Confirm the state above at HEAD (`git log --oneline -3 origin/main`; fm
#1013's state via the API; `python3 tools/render_eap_mail.py --count` and
`--verify`). Then run the Gmail probe: create one draft titled
"EAP mail — draft in progress (session probe)" with a one-line body and
no recipients, list drafts to confirm the API reads it back, and ask him
to open Gmail and say whether he sees it and can edit it — that sentence
from him, not the list call, is what makes it a capability.
Then open the sitting with the LEAST SURE line answered and the § 10
precondition list as the work order.

DONE WHEN
- docs/planning/2026-08-24-final-eap-email-draft.md carries Part 1 (drafted,
  above the COPY markers, per the file's own option) and the COPY block
  with Part 2 + the addendum + both required patches; `--verify` loss-free;
  `--count` re-derived and every figure in the file matching
  (`python3 tools/check_eap_figures.py` clean).
- Every § 10 precondition ticked in the card: the flagged rows (#4
  UNVERIFIED, #7 PROVENANCE FLAG, #11 WORDING RISK, #1's 9-vs-10) resolved
  or dropped; night-review-2026-07-10 read before FD-01/FD-02; every
  citation re-opened (the critic's 4-for-4 line-anchor drift); every linked
  document confirmed on main; every count re-run and dated.
- The same text staged as a Gmail draft he can edit, or the wall recorded.
- The last Codex round answered on the head that flips (one required, at
  most three; the flip commit itself is the one exempt commit past it);
  `python3 bootstrap.py check --strict` exit 0; the PR landed on green. He
  sends.

OUT OF SCOPE
- Sending the mail, or adding recipients. Re-running any fleet. Editing the
  retained JSON under docs/findings/data/. Any mechanism change (hooks,
  tools, workflows, skills) — a records-and-draft PR only. Re-litigating
  the sitting's decisions in fm #1013.

LESSONS FROM THE REVIEW SITTING
- A mid-turn message from him arrives bare, bypassing the prompt hook
  (measured, n = 2); acknowledge it at the next boundary with how you
  understood it — the session missed this three times the day before.
- The session restated his account of the coordinator problem wrongly
  (cause swapped); quote his words verbatim into the record BEFORE deriving
  from them, and derive in a separate paragraph.
- A wrong claim about which model last night's agents ran on was written
  from inference and caught only by Codex; the retained JSON had the answer
  in one count. Count before you write a number.

CLOSE WITH
This repo's session-close skill: born-red card as the first commit, PR
opened ready, `python3 bootstrap.py check --strict` exit 0, the card flipped
complete as the last commit after the one Codex round answers on that head,
land on green. Anything newly verified — the Gmail draft above all — goes
into docs/CAPABILITIES.md as a dated line with its venue token, capability
OR wall, with the observed result verbatim.
```

**What was verified for this prompt, and what was not.** Verified at HEAD:
every path named above exists; the draft's word count (1,686) and loss-free
rendering come from the tool, not a sentence; the four sent mails and two
unsent drafts were read from superbot over the direct API; the correspondence
record's § 0 (four thread-A messages gone from the mailbox) was read, not
re-queried. Not verified: whether a session-created Gmail draft reaches his
Drafts folder — deliberately left to the receiving session's first step, with
the ledger entry it owes either way.
