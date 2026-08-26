# Distributed History Merge — plural reference HOW family

Status: `RESEARCH_PROTOTYPE_FAMILY / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #89 reconstruction, #94 history/provenance work, PR #82, `HOW-GROWTH-DISCIPLINE.md`.

## WHAT

Preserve useful distributed history when Agent state can branch, replicate, go offline, restore from snapshots, or be edited concurrently.

The practical problem is not merely "keep provenance". A Host must decide what to do when it sees two or more histories that are not obviously one linear latest state.

Concrete relations include:

```text
same occurrence/version
ancestor / stale state
descendant / fast-forward state
concurrent sibling branches
merged/reconciled descendant
unknown causal relation
```

## WHY

Without a concrete merge organ, several failure paths remain possible even if ENA prose says history should be preserved:

```text
Agent A edits durable state offline
Agent B edits the same durable state elsewhere
B has later wall-clock timestamp
-> system keeps B only
-> A's occurrence and disagreement disappear
```

```text
snapshot restore loads old local state
remote/shared history already advanced
-> restored state is narrated as current
-> stale branch overwrites later history
```

```text
merge tool reports one final value
-> no record of both input heads or conflict resolution
-> future Agent cannot distinguish reconciliation from historical rewrite
```

```text
commutative data and semantically conflicting data use the same merge rule
-> automatic merge silently invents agreement
```

## HOW — deliberately plural

This research family does **not** define one universal merge engine. It preserves multiple concrete HOW lineages because different Hosts need different organs.

### HOW-A — Git / Merkle-DAG branch + merge

Best fit:

- file-backed Agents;
- configuration/self-definition repositories;
- human-auditable patches;
- relatively low write frequency;
- conflicts where explicit semantic review is acceptable.

See `HOW-A-GIT-DAG.md`.

### HOW-B — causal context / sibling preservation

Best fit:

- replicated key-value or document state;
- offline/multi-node Agent state;
- higher write frequency;
- need to distinguish ancestor vs concurrent sibling without trusting wall-clock time.

See `HOW-B-CAUSAL-SIBLINGS.md`.

### HOW-C — append-only event sourcing

Best fit:

- workflow engines;
- operational commitments/effects;
- database-backed Agents;
- systems where current state can be rebuilt as a projection from retained occurrences.

See `HOW-C-EVENT-SOURCING.md`.

### HOW-D — CRDT-style merge for declared commutative state

Best fit:

- replicated counters/sets/maps where a mathematically defined join exists;
- state that is genuinely safe to merge without semantic negotiation;
- collaboration/offline replication with convergence requirements.

See `HOW-D-CRDT.md`.

## These HOWs are not interchangeable

Do not infer:

```text
Git works -> vector clocks unnecessary everywhere
CRDT converges -> semantic self-authorship conflict solved
Event log is append-only -> concurrent branches reconciled automatically
Causal context detects concurrency -> it knows which branch is correct
```

A Host may use more than one HOW simultaneously. Example:

```text
SOUL / policy files        -> Git DAG
runtime preference cache   -> CRDT map
workflow commitments       -> event sourcing
replicated memory index    -> causal sibling store
```

That is valid implementation diversity, not architectural inconsistency.

## Shared minimum expectations — interface only

The four HOWs expose some common operational questions, but these do not replace the organs:

1. What is the history/version identity being compared?
2. Can ancestry/causal relation be determined?
3. If state is concurrent, is the Host allowed to auto-merge it?
4. If a merge/reconciliation occurs, are the contributing histories still traceable?
5. Can a stale restore overwrite a known descendant merely because it arrived later?
6. If relation is unknown, does the Host preserve uncertainty instead of inventing `latest`?

These are composition questions, not a mandate for one shared storage schema.

## Planned evidence

Each HOW should earn evidence separately:

```text
HOW-A -> branch/merge/restore fixtures
HOW-B -> ancestor/concurrent sibling fixtures
HOW-C -> append/concurrency/projection/compensation fixtures
HOW-D -> commutative convergence + non-commutative rejection controls
```

A later Host-fit corpus may allow more than one acceptable HOW per scenario. It must not encode a hidden assumption that one implementation is universally best.

## Degradation alarms

Treat these as warning signs:

- replacing all four HOWs with a single `history_ref` field;
- claiming provenance coverage means merge behavior is solved;
- using wall-clock LWW as a universal fallback;
- calling CRDT convergence semantic reconciliation;
- dropping input heads after merge because the final projection is correct;
- turning `multiple HOWs` into one canonical implementation plus three historical examples;
- requiring every Host to implement all four organs.

## Evidence boundary

A structurally correct merge organ does not prove:

- which branch is semantically true;
- which actor had authority;
- whether an external side effect committed;
- whether a conflict can safely be auto-merged;
- whether one HOW is globally fitter than another.

`CURRENT_CHANGE = NO`

`HOW_PLURALITY = ACTIVE`

`LOCAL_FIT_SELECTION = REQUIRED`
