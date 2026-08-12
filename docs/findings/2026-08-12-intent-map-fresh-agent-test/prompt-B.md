# Task: produce an intent map for a live owner reply

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

## The owner's message

During a live exchange about the estate's standing directives, the owner was
asked about the standing pace directive recorded in the consolidation program's
directive table, and replied, verbatim:

> "That does not mean we should ever rush things, though it does also not mean
> we can't make progress. What I meant by it is that we should just focus on one
> thing at a time and do it properly from start to finish."

## Your task

Run the intake procedure below over this reply as the current owner ask, as the
session receiving it would, and produce the intent map — exactly the report
format the procedure specifies.

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
