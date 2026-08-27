# Handoff readback — candidate.1 frozen / fresh Phase A ready

Date: 2026-08-27

Status: `PRE_INTEGRATION_READBACK_PASS / MAIN_VISIBILITY_PENDING`

This readback was performed from the research integration branch as a receiver-style coherence check before main integration. A final main readback must replace/extend this status after integration.

## Receiver questions

### What is Current?

`v0.3.6 / CURRENT / FIELD_VALIDATION`

No transition in this record authorizes Current mutation.

### What exact object is frozen?

`v0.3.7-candidate.1`

- source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- candidate subtree `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- Current subtree at same source `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze run `33055811978` — SUCCESS
- external freeze record `collaboration/reconciliation/2026-08-27-v037-candidate1-freeze.md`

### What is the project phase?

`CANDIDATE1_FROZEN / FRESH_BLIND_PHASE_A_NEXT / NOT_CURRENT / NOT_RELEASED`

`research/ACTIVE-RESEARCH.yaml`, `research/plans/PROGRESS.yaml`, and `research/handoffs/CURRENT-HANDOFF.yaml` agree on that transition after alignment.

### What is the next action?

`CANDIDATE1_FRESH_BLIND_PHASE_A`

Prepared intake:

- Issue `#128`
- branch `validation/v037-c1-blind-phase-a-primary`
- intake head `bac074097579ad930b2e90c46c00773f6f20c86d`
- blind entry `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md`
- required report `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-phase-a-primary.md`

### What must the project manager not do?

- do not modify/promote Current;
- do not mutate candidate.0 or candidate.1 frozen bytes;
- do not call same-falsifier evidence fresh independent validation;
- do not prime the fresh reviewer with project-manager/author context before Phase-A seal;
- do not close attack cardinality because exact validation passed;
- do not invent a global candidate-ID namespace rule without a governing contract.

### What method governs the next action?

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

combined with the general convergence/divergence discipline and project-state alignment method.

The key role boundary is preserved:

`PROJECT_MANAGER_CONTEXT != FRESH_VALIDATOR_PHASE_A_CONTEXT`

## Live pre-integration observations

Research integration branch after detailed progress alignment:

`aea298f8bdbc262cd01cdf8570c2f1e57d827560`

Main was still:

`2fcc705206beb8ddb0cc1cb3b4d4e0499de5412b`

A compare from main to the research branch showed the research branch ahead with research/control-plane/reconciliation/handoff/tooling changes and **no changes under `releases/current/` or `releases/v0.3.7-candidate/`** at that comparison point.

Therefore the next integration operation may move project-state visibility to main without promoting or rewriting the candidate, provided the final compare remains equally scoped.

## Remaining handoff action

1. integrate the scoped research/control-plane lineage to `main` through normal review/merge;
2. read `CURRENT-HANDOFF.yaml`, Current, Active Research, Progress, freeze identity, validation intake, and Issue #128 back from main/live refs;
3. update this readback to `POST_MERGE_READBACK_PASS` only if they agree;
4. only then treat this handoff record as fully integrated succession evidence.

`WRITTEN != HANDOFF_COMPLETE`
