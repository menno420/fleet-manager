# Owner comments — durable public feedback records

> **Status:** `living-ledger` · **Tier: TASK**
>
> Everything committed below this directory is **public** because Fleet Manager
> is public. Never put credentials, private-repository contents, private-only
> URLs, third-party contact details, or unreleased specifics here. The website
> must say this before submission; a comment that cannot safely be public needs
> another owner-approved channel.

Fleet Manager owns these repository-specific review records. The control-plane
website may read and submit them, but it is not their source of truth and a
local website queue is not durable. A comment becomes durable only after its
Fleet Manager branch-and-PR change has merged and the record is visible on
`main`.

## Storage contract

- Active records: `docs/owner-comments/<repo>/<id>.json`.
- Preserved history: `docs/owner-comments/<repo>/consumed/<id>.json`.
- Stable routed index: `docs/owner-comments/<repo>/README.md`.
- Cheap estate overview: [`index.json`](index.json), generated from
  [`ESTATE.md`](../ESTATE.md) plus the records. It is a projection, not a second
  repository registry.

The normative [JSON Schema](record.schema.json) is version 1. It requires
`schema_version`, `id`, `repository`,
`created_at`, `state`, `source`, and `comment`. `comment` is the owner's wording
verbatim. `source` requires a surface name and may carry a context string. A
consumed record additionally carries `consumption.at`, `consumption.actor`, and
`consumption.evidence` so the state transition is auditable.

Comment and context strings are untrusted input. Readers and the control-plane
website must escape them as text; they are never templates or trusted Markdown.

```json
{
  "comment": "The owner's exact text, unchanged.",
  "created_at": "2026-08-27T12:00:00Z",
  "id": "oc-20260827t120000z-a1b2c3d4",
  "repository": "websites",
  "schema_version": 1,
  "source": {
    "context": "/repos/websites",
    "surface": "control-plane"
  },
  "state": "unconsumed"
}
```

Ids are 3–80 lowercase URL/path- and Git-ref-safe characters (`a-z`, `0-9`,
`.`, `_`, `-`) and the filename is exactly `<id>.json`; consecutive dots,
trailing dots/`.lock`, and Windows device names are rejected. Ids are unique
across the ledger. Repository spelling and case must match an `ESTATE.md` row;
reserved root filenames and case-folding collisions are rejected. Timestamps
are real RFC3339 UTC values ending in `Z`.

Record bytes are canonical: UTF-8 without invalid surrogates, keys sorted,
two-space JSON indentation, no duplicate/unknown keys, and exactly one final
newline. `tools/owner_comments.py check` is the executable reference for the
ESTATE-membership, timestamp ordering, path, lifecycle, and canonical-byte
rules that JSON Schema alone cannot express.

`check` validates both checkout bytes and the staged Git-object bytes, so an API
commit cannot hide CRLF/noncanonical records behind checkout normalization.
Mutations share a worktree-stable process lock. Their recovery journals live in
Git metadata (never in the committed record tree); the next `check`, `reindex`,
or `consume` deterministically rolls back a process-terminated prepared change
before continuing. Every prepared journal is pinned to its Git `HEAD` and index
tree. If either changed (for example, after switching branches), recovery
quarantines the stale journal and stops without changing the current checkout.
Data moves and generated-index replacements sync their parent directories before
the journal can be marked committed.

## Commands

```text
python3 tools/owner_comments.py check
python3 tools/owner_comments.py reindex
python3 tools/owner_comments.py consume <repo> <id> \
  --actor <session-card-or-actor> --evidence <record-or-PR-link>
```

Consumption is mechanical: act on or explicitly reconcile the feedback, then
run `consume`. Commit the moved JSON and both updated indexes in the same diff.
Never delete the record. Readers seeking **unconsumed** feedback read only the
first section of the per-repository index; consumed history remains visible but
is not active work.

Runtime website submissions use a `claude/owner-comments-<durable-id>` branch,
commit the record and indexes together, and open a normal ready PR to protected
`main`. They never direct-write `main`. The write token needs Contents read/write
and Pull requests read/write; without both, the website must report the write
capability unavailable or pending rather than claim durability.
