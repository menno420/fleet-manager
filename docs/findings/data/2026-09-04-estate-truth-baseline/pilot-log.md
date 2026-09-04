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

## 3 · A piped fetch returned a DIFFERENT repository's file, under HTTP 200

The sharpest one, and it was only visible in the transcript. The `spider-swing`
agent's `curl … | python3` fetch of that repo's `README.md` returned a
2,113-byte payload whose content was **`creator-kit`'s README** — the other
pilot agent's repository, running concurrently. HTTP 200, valid base64, clean
decode, no error anywhere. The agent noticed only because the size looked wrong;
re-fetching to disk first returned the correct 21,599-byte file matching the
tree's recorded blob sha `9fb99d71a0832ef82ebdf4fcf1be98f8826f1f67`.

A summary would have said "read the README". The fleet's instructions now
**forbid `curl | python3` for file contents**: fetch to disk, decode from the
file, and cross-check the decoded size and blob sha against the tree listing.

## What the pilot did NOT change

The schema, the reading depth and the contradiction-first framing all survived:
the two agents opened 27 and 42 paths, checked repository claims against the
tree rather than against documents, and returned three evidenced hub-vs-repo
contradictions plus one clean AGREE. That is the shape the fleet wanted, so it
was not touched.
