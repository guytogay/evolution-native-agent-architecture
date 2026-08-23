# ENA v0.3.5 candidate.2 — final reconciliation

Date: 2026-08-23

## Reconciler role

`HOST_SIDE_RECONCILER / RELEASE_DECISION_COLLABORATOR / NOT_INDEPENDENT_VALIDATOR`

This reconciliation does not relabel author/Host-side work as independent validation.

## Inputs

### First frozen candidate

- source: `eb6d7ba00894ed446903aebe61cd59f0bdb59af7`
- tree: `f373e7695348c157dcd48d3ed243ea3079215b8f`
- DSH verdict: `NEEDS_REVISION`

### Frozen candidate.1

- source: `e6ff1e76afb8ad8919186786100ec153a5f0d07a`
- tree: `ff2cb44c7a5d1b472800180578b5df7baa123aec`
- DSH role: `SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH`
- verdict: `TARGETED_REVALIDATION_SUPPORTED_WITH_RESIDUALS`

### Frozen candidate.2

- source: `8393b8b05d34797965c612e8b9ca938d306f6322`
- tree: `b10854f191d9641138e2f44278f043f124a2e120`
- freeze-record commit: `34e12333bcbe6cf8a3a2a992040d93012ead868b`

### candidate.2 narrow revalidation

- DSH role: `SAME_FALSIFIER / NARROW_RESIDUAL_REVALIDATION / NOT_FRESH`
- verdict: `NARROW_REVALIDATION_SUPPORTED`
- durable summary: `collaboration/inbox/2026-08-23-v035-candidate2-dsh-narrow-revalidation-summary.md`

## Reconciliation finding

The release-decision residual cycle has converged.

The material defects found in the first frozen candidate were closed in candidate.1 and mechanically revalidated. candidate.2 then closed the cheap, concrete residuals N1/N2/N7 plus the adjacent transfer-status self-upgrade class. The same falsifier reproduced the attack shapes against candidate.2 and reported them CLOSED.

No new MATERIAL/BLOCKING issue was reported.

The narrow fixes did not introduce observed evolution starvation, universal signature requirements, new approval roles, or migration prohibition. Receiver-side local experimentation/reselection remains available.

## Why candidate.3 is not justified

N3–N6 remain visible but are not currently release blockers:

- repeated evaluation of one experiment may be legitimate reinterpretation and lacks evidence for a universal prohibition;
- nested source-negative lineage may become a usability problem, but no material false-claim path was demonstrated in this round;
- no in-place archive restore is a reference-tool capability gap, not evidence that evolutionary recovery is impossible;
- migration-lineage depth growth is a scaling hypothesis, not yet a demonstrated release-blocking failure.

Creating candidate.3 solely to eliminate visible residuals would optimize for governance cleanliness rather than decision-relevant risk/evolvability.

`Governance must pay rent.`

Therefore:

`CANDIDATE_SUCCESSION_STOP = YES`

unless new material evidence appears.

## Accepted residuals

Carry N3–N6 into field/research tracking. Do not silently call them solved. Do not add Constitution rules from them without stronger evidence.

## Release decision

candidate.2 is accepted as the semantic/implementation source for preparing ENA v0.3.5 release packaging.

Decision:

`RELEASE_PREPARATION_SUPPORTED`

Target adopter-facing release state:

`v0.3.5 / CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`

v0.3.5 proposes retiring `MAINLINE / NOT_MAINLINE` as an active adopter-facing maturity axis. Historical Mainline/Not-Mainline records remain occurrence truth and are not rewritten.

## Release packaging constraints

Release packaging may change candidate/release metadata and adopter-facing identity labels required to turn the frozen candidate into v0.3.5 Current, but must not silently change the validated material semantics.

At minimum:

- transform candidate identity to v0.3.5 release identity;
- replace `CANDIDATE-BASELINE.yaml` with `CURRENT-BASELINE.yaml` appropriate to the release;
- keep the 38 Constitution semantic IDs and validated Constitution content unchanged unless a packaging-only heading/status edit is proven non-semantic;
- preserve English/zh-CN projection semantic binding and known-gap honesty;
- preserve candidate.2 tool behavior that closed N1/N2/N7;
- keep retained N3–N6 residuals visible in lineage/changelog/research tracking;
- publish one singular `releases/current/` adoption surface;
- verify exact source/tree/package identity, file parity, and published readback before claiming release workflow complete.

## Next meaningful evidence after release

The next high-value evidence is real heterogeneous Host field use of v0.3.5 evolution metabolism, tracked in issue #61.

Do not manufacture candidate.3 or another validator ceremony unless a decision-changing hypothesis appears.

> Variation first; selection by reality.
> Governance must pay rent.
