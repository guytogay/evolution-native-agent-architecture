# Distributed History Merge reference prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #94 Reconstruction E, #89 HOW-growth reconstruction, PR #82.

## WHAT

Represent durable history as a causal graph that can remain honestly linear, diverged, stale, or reconciled without silently rewriting one branch as if it never existed.

```text
HISTORY EXISTS
!= ONE CURRENT HEAD IS KNOWN
!= CONCURRENT BRANCHES ARE SEMANTICALLY MERGEABLE
!= RESTORED LOCAL STATE IS CURRENT WORLD STATE
```

This organ is intentionally concrete. It is not replaced by generic provenance or an Evidence Envelope because it has independent operational behavior: parent/head causality, divergence, stale restore, conflict preservation, and explicit reconciliation.

## WHY

Concrete failures include:

```text
offline Agent A changes durable state
offline Agent B changes same state
-> one arrives later by wall clock
-> last-write-wins silently erases the other history
```

```text
old snapshot restored
-> local head looks internally consistent
-> known remote descendant already exists
-> Host narrates restored state as current closed history
```

```text
two material branches conflict
-> merge object points to only one parent
-> losing branch disappears from causal ancestry
```

```text
CRDT-capable non-conflicting branches
-> universal manual-merge ceremony imposed
-> needless false-BLOCK
```

## HOW — reference organ

Files:

- `distributed-history-merge.v0.1.json` — compact state/event/merge vocabulary;
- `fixtures/distributed-history-merge-cases.jsonl` — deterministic linear/diverged/merge/stale/conflict cases;
- `tools/validate_distributed_history_merge.py` — represented causal/reconciliation validator;
- `tools/selftest_distributed_history_merge.py` — mutation/adversarial selftest.

Reference record:

```yaml
history_id: H1
subject_ref: durable-self-or-state
state: LINEAR | DIVERGED | RECONCILED | STALE
closure_claim: NONE | CURRENT_CLOSED
heads: [E3]
known_remote_heads: []
events:
  - event_id: E1
    parents: []
    branch_ref: main
    epoch_ref: EP1
    actor_ref: A1
    kind: APPEND
    payload_digest: sha256:...
  - event_id: E3
    parents: [E1, E2]
    branch_ref: main
    epoch_ref: EP2
    actor_ref: A1
    kind: MERGE
    payload_digest: sha256:...
    merge_strategy: EXPLICIT_MERGE
    resolution_basis_ref: optional
conflicts: []
```

## Reference properties

### DHM-P01 — Event identity is occurrence identity

One `event_id` cannot silently bind different payload digests or causal parents.

### DHM-P02 — Parent causality must be representable and acyclic

Every local parent reference must exist and the graph must remain acyclic.

### DHM-P03 — Heads are derived from the graph

Declared `heads` must equal the terminal events of the represented local graph. Omitting a surviving branch is history loss, not simplification.

### DHM-P04 — Divergence is an honest valid state

Multiple heads are allowed. `DIVERGED` is not a validation failure by itself.

Uncertainty or unresolved siblings may be safer and more truthful than manufacturing a latest winner.

### DHM-P05 — Merge events preserve all merged parents

A `MERGE` event requires at least two causal parents. A reconciliation result must descend from every branch it claims to reconcile.

### DHM-P06 — Material conflicts cannot disappear through wall-clock LWW

A material conflict may remain open or be explicitly resolved. `WALL_CLOCK_LWW` may not close a material conflict while discarding the losing alternative from inspectable history.

### DHM-P07 — Restore may create STALE local state

A restored snapshot may be internally valid yet stale relative to a known remote head.

If a known remote head is not an ancestor of any local current head, `CURRENT_CLOSED` is not allowed.

### DHM-P08 — Conflict resolution is another historical event

A resolution appends/derives a new event. It does not rewrite the original conflicting events as if they never happened.

### DHM-P09 — Non-conflicting CRDT-style auto-merge is allowed

The reference organ does not require manual conflict ceremony when a Host can validly and deterministically merge concurrent non-material/non-conflicting updates.

### DHM-P10 — Linear append-only history remains cheap

A single-head linear history does not need vector clocks, CRDT metadata, or conflict objects merely to satisfy this reference organ.

## Multiple HOW phenotypes are intentional

One ENA property does **not** imply one mandatory organ.

For this surface, several mature implementation families should remain available in parallel:

### Git / Merkle-DAG style

- content/version IDs;
- one or more parents;
- branch heads;
- three-way merge from common ancestry;
- explicit conflict resolution;
- merge commit preserves both parent histories.

Good fit: file/Git Hosts, self-state artifacts, configuration, authored knowledge.

### Causal-context / sibling style

- vector clock, dotted version vector, or equivalent causal context;
- distinguish ancestor from concurrent sibling;
- preserve siblings until domain reconciliation.

Good fit: replicated mutable records and offline writers.

### CRDT style

- operations or states designed to converge under concurrent updates;
- non-conflicting changes merge automatically;
- semantic conflicts may still remain inspectable depending on data type.

Good fit: collaborative/distributed state whose merge semantics are known in advance.

### Event-sourcing style

- append-only event stream is occurrence history;
- current state is a projection;
- optimistic concurrency protects expected stream version;
- reversal uses compensating/new events rather than deleting prior occurrence.

Good fit: workflows, commitments, operational histories, external-effect orchestration.

These are competing/adaptive phenotypes, not steps toward one universal implementation.

```text
ONE PROPERTY
-> MULTIPLE HOWS
-> HOST-LOCAL SELECTION
-> FIELD EVIDENCE
```

A HOW is not retired merely because another HOW exists. Retirement requires demonstrated usefulness failure or function-parity replacement.

## False-BLOCK controls

Do not require:

- distributed clocks for a genuinely single-writer linear file;
- manual conflict review for deterministic non-material CRDT merge;
- one canonical branch name;
- one database or VCS technology;
- wall-clock ordering when causality is already sufficient;
- semantic reconciliation when histories are merely being preserved as divergent candidates.

## Evidence boundary

```text
VALID_CAUSAL_GRAPH
!= SEMANTICALLY_CORRECT_HISTORY
!= AUTHORITY_VALID
!= EXTERNAL_EFFECT_SETTLED
!= ALL_REMOTE_HISTORY_DISCOVERED
```

The organ protects represented causal/reconciliation honesty. It does not prove that every remote branch is known, that a merge is semantically good, or that any actor had authority to produce the events.

`CURRENT_CHANGE = NO`
