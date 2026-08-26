# HOW-A — File/Git tiny resident + exact cold source

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Best when the Agent reliably loads one or more small instruction files and can read a local repository/package on demand.

Typical Hosts:

- coding/CLI Agents;
- repo-scoped Agents;
- file-backed assistants;
- environments where Git/content identity is cheap and trustworthy enough for local source binding.

## Concrete layout

Example:

```text
~/.agent/ENA-KERNEL.md                   # always loaded; small
/work/ena-current/                       # canonical cold package/check-out
  releases/current/...
~/.agent/ena-source.json                 # exact Current identity
~/.agent/ena-router.json                 # optional deterministic navigation map
```

`ENA-KERNEL.md` should contain recognition/interrupt logic, not a shadow copy of all ENA semantics.

Illustrative source identity:

```json
{
  "ena_version": "v0.3.6",
  "current_tree": "7dcbb3934883ffa6cc5292a662588cafc1533cff",
  "release_merge_commit": "74b790741653286e0f01a1483723cdeb065ec3df",
  "cold_root": "/work/ena-current/releases/current"
}
```

## Runtime sequence

```text
fresh session
-> load small resident kernel + source identity
-> ordinary task proceeds
-> material decision shape triggers ENA lookup
-> deterministic router or exact known path selects cold section
-> read canonical file/section
-> if read succeeds: use bounded projection for current decision
-> if read fails/identity mismatches: explicit PARTIAL/FAILED + fallback
```

## Refresh/invalidation

At session start or bounded refresh point:

```text
read configured canonical identity
compare with stored source identity
```

If canonical Current identity changes:

- resident kernel version/pointer may need refresh;
- router target reachability must be rechecked;
- cached/compiled projections become stale until revalidated;
- old source remains historical evidence, not current semantics.

## Failure behavior

If local Git checkout/package disappears or exact target cannot be read:

- material decision: narrow/wait/fetch/recover exact source;
- non-material decision: may proceed with declared semantic uncertainty;
- never narrate `cold retrieval succeeded` from memory alone.

## What this HOW is good at

- precise source identity;
- cheap exact-path fallback;
- auditability;
- easy historical/version comparison;
- low resident context cost.

## What it is bad at

- Hosts with no reliable filesystem/repository access;
- semantic retrieval across large unfamiliar cold packages without a router/index;
- remote-only canonical state when network availability is poor.

## Variants

This HOW itself can have multiple local forms:

- Git worktree + section router;
- immutable release archive + manifest;
- content-addressed package store;
- exact file map without Git if content identity is still stable.

`LOCAL_WINNER = FILE_ORIENTED_HOST_CANDIDATE`
