# ENA Research Directory

Status: `RESEARCH_INFORMATION_ARCHITECTURE / ACTIVE`

This directory contains non-Current research state. It must remain broad enough to preserve variation while still being navigable by fresh sessions.

## Start here

For any session continuing ENA research:

`RESEARCH-START-HERE.md`

Do not infer Current from this directory. The adopter-facing baseline remains `releases/current/` on the default branch.

## Canonical areas

### `methodology/`

How ENA itself should be researched.

Contains anti-dissolution, HOW growth, cardinality, session-continuity, evidence/experiment discipline, and future methodology discovered from research failures.

This is the canonical home for research method.

### `plans/`

Long-running project execution state.

Key files:

- `ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` — durable plan from current reconstruction through eventual release.
- `PROGRESS.yaml` — machine-readable current phase/state/pointers.

Future sessions should update progress here after material changes instead of relying on chat summaries.

### `reconstruction/`

Anti-ablation archaeology, gap maps, mechanism-retention ledgers, degradation audits, release-closure research, and other reconstruction evidence.

This directory answers **what was recovered / lost / unresolved**, not **how research must always be conducted**. Method files discovered here should be canonicalized into `methodology/` when they become ongoing research discipline.

### `external-how/`

Current external mechanism harvesting from agent frameworks, AI memory systems, durable workflow systems, AI labs, developer communities, protocols, and adjacent engineering fields.

External HOWs are candidate branches, not authority.

### `prototypes/`

Executable/reference organs and machine-checkable candidate HOWs.

Prototype visibility must not be mistaken for ontological importance.

### `experiments/`

Experiments whose result can plausibly reveal decision-changing structure not already derivable statically.

Experiments must pay epistemic rent.

### `adversarial-replay/`

Historical adversarial/falsification lineage and reusable failure evidence.

### `evolution-inbox/`

Open research/candidate intake not yet reconciled into stable research state.

### `incidents/`

Research-process failures that teach how ENA research itself must change.

Example: session inheritance/activation failure.

## Compatibility paths

Some older research method files existed in `research/reconstruction/` or directly under `research/`. They may remain as small pointer files so historical Issue/comment/commit links do not break.

Do not maintain duplicate canonical copies merely for directory symmetry.

## Research tree rule

```text
WHAT / WHY
  may compress into a stable semantic trunk

HOW
  should grow concrete branches where reality supports them

EVIDENCE
  attaches to the branch/Host/claim it actually supports
```

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
WORKING_DIRECTORY_STRUCTURE != ENA_ONTOLOGY
```

This directory map is navigation, not a claim that all future ENA research fits exactly these categories.

> **Preserve variation durably; retrieve selectively; select by evidence.**
