# Pilot log — what reading the pilot whole actually changed

> fleet-preflight § 3 requires the pilot's transcripts to be read **completely**
> and what it changed written down, *including "nothing"*. Three things changed.
> All three would have been invisible in a summary.

## 1 · Two hand-typed SHAs were invented, and both agents 422'd

The pilot prompts carried full 40-character SHAs I had composed from 12-character
prefixes printed by an earlier script. Both diverged after those twelve characters:

| repo | in the prompt | the real tip |
|---|---|---|
| `spider-swing` | `fc64a3fbb25f0eef1a4dbbd0b8ad2a89fee7ba60` | `fc64a3fbb25ff8be21a7bbeceb1d5c8275d614f0` |
| `creator-kit` | `741f429a2e96f4bd8c8d0dd25d18a55f8d2ba0f1` | `741f429a2e96587aa27075085b85df889531d2a7` |

Both agents recovered correctly — they re-read `branches/main`, used the real
tip, and put the discrepancy in `walls` rather than proceeding quietly. The
**fix is structural, not a correction**: the fleet's agents now read their own
pinned SHA out of the committed `classification.json` and the prompt never
carries one. A value nobody retypes cannot be mistyped.

## 2 · Agents shared one scratchpad directory and overwrote each other's files

Both pilot agents wrote to the same `scratchpad/` paths (`tree.json`,
`readme_raw.json`). With two agents that is a hazard; with the fleet's
twenty-one first-stage agents it is corruption. Every agent now gets
`scratchpad/eb/<name>/`.

## 3 · One agent read a DIFFERENT repository's file — and the cause is defect 2, not the network

The sharpest one, and it was only visible in the transcript. The `spider-swing`
agent's fetch of that repo's `README.md` produced a 2,113-byte payload whose
content was **`creator-kit`'s README** — the other pilot agent's repository,
running concurrently. No error anywhere. The agent noticed only because the size
looked wrong; re-fetching returned the correct 21,599-byte file matching the
tree's recorded blob sha `9fb99d71a0832ef82ebdf4fcf1be98f8826f1f67`.

> **CORRECTED 2026-09-04, after this document first attributed it to the
> network.** The agent's own wall called it an *"apparent proxy/cache anomaly on
> this environment's egress path"*, and this log repeated that. **It is wrong,
> and the arithmetic settles it:**
>
> | | bytes | blob |
> |---|--:|---|
> | `creator-kit` `README.md` at its pinned SHA | **2,112** | `91d62974b39f` |
> | what the `spider-swing` agent received | **2,113** | — |
> | `spider-swing` `README.md` at its pinned SHA | **21,599** | `9fb99d71a083` |
>
> 2,112 bytes plus one trailing newline from the decode-and-write is 2,113.
> And the transcripts show **both agents reading `$OUT/README.md`** — the same
> path in the shared scratchpad. So the `creator-kit` agent decoded its README
> to that path and the `spider-swing` agent read it back. **Nothing came from
> the network that should not have.** Defects 2 and 3 are one defect, and the
> count of "three things the pilot changed" is honest only because the third
> *fix* was independently worth making.

**Two consequences, and the second is the one worth keeping.**

The instruction added to the fleet — never `curl | python3` for file contents;
fetch to disk, decode from the file, and cross-check the decoded size and blob
sha against the tree listing — was aimed at a cause that did not exist. It stays
anyway, because the **blob-sha cross-check catches either cause** and is the
only step that would have caught this one at the moment it happened rather than
by a reader noticing a suspicious byte count.

The real fix was the per-agent directory (defect 2). **An unexplained result
attracts an exotic explanation**, and the agent, the log and a first reading all
took one; the mundane cause was two processes sharing a filename, already
identified in the paragraph above it. Checking the byte count against the other
repository's file took one API call.

## What the pilot did NOT change

The schema, the reading depth and the contradiction-first framing all survived:
the two agents opened 27 and 42 paths, checked repository claims against the
tree rather than against documents, and returned three evidenced hub-vs-repo
contradictions plus one clean AGREE. That is the shape the fleet wanted, so it
was not touched.
