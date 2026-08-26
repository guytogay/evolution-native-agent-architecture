# HOW-A — Git / Merkle-DAG branch + merge

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Use this HOW when durable Agent state is naturally represented as files or versioned text/artifacts and human/audit visibility matters more than very high write throughput.

Typical surfaces:

- `SOUL.md` / durable purpose or refusal files;
- policy/configuration repositories;
- curated memory compilations;
- architecture/config snapshots;
- release/adoption state.

## Concrete mechanism

Represent each durable change as a content-addressed commit/version node with parent links.

Operational sequence:

```text
1. read current branch head(s)
2. compute/resolve common ancestor when histories differ
3. classify relation
   - SAME/EQUIVALENT
   - LOCAL_ANCESTOR_OF_INCOMING
   - INCOMING_ANCESTOR_OF_LOCAL
   - DIVERGED
4. if incoming descends from local -> fast-forward is possible
5. if incoming is stale ancestor -> retain/read as history; do not overwrite head
6. if diverged -> perform three-way merge against common ancestor
7. if conflict is material -> preserve unresolved conflict or explicit branch; do not silently pick by timestamp
8. if reconciled -> create a new merge commit with both relevant parents
9. read back the merged durable surface before claiming integrated state
```

Reference Git operations for a file-backed Host can include:

```bash
git merge-base <local-head> <incoming-head>
git merge --no-ff <incoming-branch>
git log --graph --decorate --oneline --all
```

ENA does not require Git itself; these commands demonstrate one concrete organ.

## Why multiple parents matter

A merge node with two parent histories says:

> this new state descends from both branches.

It does **not** say:

> both branches were semantically correct.

Conflict resolution remains a separate decision with its own evidence/authority.

## Restore behavior

A restored old snapshot should normally become a stale branch/head, not overwrite a known descendant merely because the restore happened later in wall-clock time.

Safe shape:

```text
known shared head = H9
restore local snapshot = H4
-> classify H4 as ancestor/stale
-> resume from H4 only in an explicit isolated branch or rebase/merge path
-> do not narrate H4 as globally latest
```

## Conflict behavior

For material self-definition/policy conflicts:

```text
base:     purpose = A
branch 1: purpose = B
branch 2: purpose = C
```

A text merge that happens to choose B or C is not enough. The Host should preserve conflict/reconciliation evidence and, where the durable-self surface is material, compose with Contested Authorship rather than treating a clean file as proof of legitimate authorship.

## False-BLOCK controls

Do not require merge commits for:

- simple fast-forward histories;
- identical content represented by equivalent commit identity mapping;
- temporary task state;
- caches/indexes that are regenerated rather than treated as canonical history.

Squashing may be acceptable for a local implementation only if the required contributing lineage is retained somewhere else and the loss does not affect later decisions.

## Known limits

This HOW does not solve:

- high-frequency replicated state economically;
- semantic truth of conflicting values;
- external effect settlement;
- authority of the committer;
- hidden branches not fetched/known to the Host.

## Evidence targets

Useful fixtures:

- fast-forward descendant;
- stale restore ancestor;
- two divergent branches with material conflict;
- successful merge preserving two parents;
- force-push/history rewrite attempt;
- squashed merge with and without retained provenance;
- unknown remote state requiring fetch/revalidation before `latest` claim.

`LOCAL_WINNER = FILE/GIT_HOST_CANDIDATE`
