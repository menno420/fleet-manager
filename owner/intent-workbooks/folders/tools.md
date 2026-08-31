# What I think the `tools/` folder is for

## Proposed contract

`PROPOSED`: implementations of hub checks, generators, importers, migrations,
and reports. Every tool names the human problem it solves and the canonical data
it reads or writes.

Policy must not exist only in code. One-off scripts should not become permanent
machinery without repeated need. Tools that belong to a product or the shared
kit stay in those repositories.

## Questions for you

1. Which checks are important enough to block a change?
2. When should a useful one-off script be kept?
3. Do you want a plain-language catalogue of tools separate from technical help?

## Your words

`OWNER`:

