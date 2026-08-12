# Task: produce an intent map for an owner instruction

> **Status:** `reference` — verbatim prompt template, evidence for the § 4.8 test

You are a fresh session. Your working repository is the directory snapshot at:

    {SNAPSHOT_DIR}

It is a snapshot of the `fleet-manager` repository at a specific past moment.
Treat it as the complete, current state of the repository.

## Hard constraints

- Work ONLY inside the snapshot directory above. Do NOT read any other checkout
  of this repository — in particular, do NOT read `/home/user/fleet-manager` or
  anything outside the snapshot. Do not use git history, GitHub, or the network.
  Everything you may consult is inside the snapshot.
- The snapshot may reference files that do not exist in it; treat a missing
  reference as genuinely missing and say so where it matters.
- Do NOT create or modify any files. Your deliverable is your final message only.
- The procedure text below supersedes any skill files inside the snapshot.

## The owner instruction

The following is an owner instruction for an upcoming work session, preserved as
nine quoted fragments. The quoting and segmentation into nine was done by an
earlier agent; the ellipses are elisions in the preserved record. The fragments
are in their preserved order and together form one message. The owner wrote it
in the third person, describing what the session should do.

1. "read all the required reading order files and more… fully understand the
   fleet manager repo, everything that it possibly wants to or should know is
   documented there"
2. "After, and only after it has fully read and understood the fleet manager
   repo, it should add the superbot repo"
3. "read all files starting in the required reading order, all other important
   docs, a fair share of the session journals"
4. "how the help system works, how the cogs are built, how the helper files are
   used, how everything works together… assert the proper baseline… use its own
   judgements to find which files are in the right state"
5. "games should remain out of scope for now"
6. "properly make use of its ability to call on gemini for reviews… advanced
   models, preferably through vertex but it's also allowed to directly use
   gemini's deep research from my own paid credits"
7. "for the superbot next repo the most important things are to find out which
   parts are genuinely better built"
8. "this should not be the final planning or mapping session… most of what's
   documented is true, tho it should always verify things that aren't sure"
9. "a comprehensive document in the fleet manager repo and a summary in the
   chat, with its next recommended actions: the next agents to use, what they
   should review, how they should act"

## Your task

Do NOT execute this instruction. Your task is to run the intake procedure below
over it, as the session receiving this instruction would, and produce the intent
map — exactly the report format the procedure specifies.

Notes on applying the procedure here:

- ESTABLISHED is a retrieval step: every ESTABLISHED entry must carry a citation
  to a file path (with a line number or section) that exists in the snapshot and
  actually says what the entry claims. Do not cite from memory. If a document the
  procedure names does not exist in the snapshot, record that and move on.
- An OPEN entry must point at the words that leave the question open.
- Classify every unresolved item LOW / MEDIUM / HIGH per the procedure and print
  the INTENT STATUS verdict exactly as specified.
- Where the procedure would have you ask the owner, you cannot — write the
  question(s) you would ask under QUESTIONS FOR OWNER instead.

Your final message must be the report and nothing else: MAIN IDEAS · INTENT MAP
(all seven parts, separately labelled) · INTENT STATUS · MAP TO METHOD ·
DECISIONS FLAGGED · QUESTIONS FOR OWNER · DURABLE?

## The procedure

{PROCEDURE}
