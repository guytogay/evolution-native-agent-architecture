# Reference Library Selection 001 — Candidate optional HOW library

Status: `RELEASE_SCOPE_DECISION / REFERENCE_SET_SELECTED_WITH_DEFERRED_BRANCHES / CURRENT_UNCHANGED / VERSION_UNASSIGNED`

Date: 2026-08-27

## Purpose

Select which concrete reference organs should be bundled with the next candidate without turning package inclusion into a universal runtime mandate.

```text
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
PACKAGE_INCLUDED != APPLICABLE
REFERENCE_SCHEMA != ENA_ONTOLOGY
```

## General optional references — SELECT

These solve recurring cross-Host operational failures, have concrete applicability/non-applicability boundaries, and are mature enough to justify candidate packaging as optional references.

### Retrieval Obligation 0.5

Disposition: `SELECT / GENERAL_OPTIONAL_REFERENCE`

Reasons:
- independently reviewed and narrowly reconciled;
- binds retrieval sufficiency to effective content identity rather than stable alias alone;
- preserves decision-material freshness and bounded no-hit;
- keeps registry/currentness/completeness/evaluator legitimacy as explicit external residuals.

### WAIT / Autonomous Patience

Disposition: `SELECT / GENERAL_OPTIONAL_REFERENCE`

Reasons:
- small, broadly Host-mappable mechanism;
- prevents silence/timeout from becoming implicit retry;
- preserves `WAKE_READY != AUTHORIZED_TO_RESUME` and `TIMEOUT_REACHED != RETRY_EFFECT`;
- does not force a universal cognitive-mode taxonomy.

### Authority Grant / Lease

Disposition: `SELECT / GENERAL_OPTIONAL_REFERENCE`

Reasons:
- operationalizes existing authority semantics without redefining authority;
- `NOT_REQUIRED` directly controls false-BLOCK/authority anxiety on non-authority-bearing actions;
- conditional epoch binding avoids universal Host machinery;
- composes with effects/recovery while keeping mandate truth external.

### Effect Lifecycle

Disposition: `SELECT / GENERAL_OPTIONAL_REFERENCE`

Reasons:
- addresses high-consequence restart/retry/failover failures across Hosts;
- separates intent, attempt, receipt, commitment;
- preserves materially different HOWs: idempotency, status query, fencing, compensation, WAIT, manual settlement;
- explicitly rejects universal exactly-once claims.

### Recovery Adapter

Disposition: `SELECT / GENERAL_OPTIONAL_REFERENCE`

Reasons:
- operationalizes `checkpoint exists != recovery proven` and `restore success != safe resume`;
- makes independent rescue/drill conditional;
- composes world settlement and authority outputs rather than duplicating them;
- exposes explicit no-resume/uncertainty paths.

## Advanced / specialized optional references — SELECT

These should be bundled when package complexity remains proportional, but kept outside the ordinary hot/default path.

### Evidence Envelope

Disposition: `SELECT / ADVANCED_OPTIONAL_REFERENCE`

Use when decision-material evidence must carry applicability/provenance/witness/activation/projection distinctions across boundaries.

Do not require it for trivial observations. Optional sections and explicit UNKNOWN/non-applicability behavior are part of its value.

### Evidence Dependency Map

Disposition: `SELECT / ADVANCED_OPTIONAL_REFERENCE`

Use primarily for material corroboration where repeated/correlated observations could be narrated as independent support.

Do not require multiple vendors/models or an independence score. Dependency visibility is the mechanism.

### Contested Authorship

Disposition: `SELECT / SPECIALIZED_OPTIONAL_REFERENCE`

Use for material durable self-surface change where origin, endorsement, conflict, revision, or authority-laundering can matter.

Its explicit `OUT_OF_SCOPE_FOR_CONTESTED_AUTHORSHIP` path keeps ordinary cache/memory/task state out of the ceremony.

This reference does not solve ultimate moral/political legitimacy; that unresolved question is not required for the narrower provenance/authorship function.

## Deferred from first candidate reference library

### Commitment / Settlement recovered reconstruction

Disposition: `DEFER_FROM_FIRST_CANDIDATE_REFERENCE_LIBRARY / RETAIN_IN_RESEARCH`

Reason:

The represented mechanism is valuable and cross-organ composition exposed material boundaries, but the durable machine surface is a **recovered reconstruction**, not byte-identical recovery of the earlier lost prototype.

```text
RECOVERED_SEMANTICS != ORIGINAL_BYTES
SAME_CASE_COUNT != SAME_CORPUS
```

Do not lower the evidence bar merely to make the first candidate library look complete.

Reconsider after fresh independent semantic/implementation falsification or when a candidate-critical obligation/settlement requirement makes the decision worth reopening.

The operational HOW map may still explain the obligation/executor/effect/settlement distinction and point to research lineage without bundling the reconstructed machine organ.

## Not selected as universal reference organs

The following remain Host patterns, procedures, field branches, or research rather than machine-reference requirements:

- Tiny Hot Kernel exact phenotype;
- durable workflow engine choice;
- memory storage/index technology;
- target fencing/provider idempotency implementation;
- A2A vs OCI/Git/object-registry transport substrate;
- reputation rehabilitation policy;
- ecology/resource/culture/verification-market mechanisms;
- progressive occurrence/enrichment representation.

Their absence from the bundled machine-reference set is not retirement or deletion.

## Packaging semantics

The candidate baseline/manifest should make optionality explicit rather than relying on prose inference.

A useful representation should distinguish at least:

```text
GENERAL_OPTIONAL_REFERENCE
ADVANCED_OPTIONAL_REFERENCE
SPECIALIZED_OPTIONAL_REFERENCE
HOST_PATTERN
PROCEDURE
FIELD_OR_RESEARCH_ONLY
```

These are packaging roles, not ontology.

For each bundled reference, candidate metadata should make clear:

```text
required_for_complete_adoption = false
default_activation = false
applicability = context/Host dependent
normative_semantic_authority = Current semantic trunk, not reference schema
```

Exact field names remain candidate-build design.

## Release hot/cold rule

None of these reference organs should be automatically injected into every Agent context merely because they ship in the package.

```text
REFERENCE_LIBRARY_BUNDLED
!= REFERENCE_LIBRARY_ALWAYS_HOT
```

Routing remains:

```text
cue/problem
-> semantic property
-> applicable HOW/reference
-> Host mapping
-> act / WAIT / UNKNOWN / not-applicable
```

## Scope result

```text
GENERAL_OPTIONAL_REFERENCES_SELECTED =
  Retrieval Obligation 0.5
  WAIT
  Authority Lease
  Effect Lifecycle
  Recovery Adapter

ADVANCED_SPECIALIZED_REFERENCES_SELECTED =
  Evidence Envelope
  Evidence Dependency Map
  Contested Authorship

DEFERRED_REFERENCE =
  Commitment/Settlement recovered reconstruction

REFERENCE_SET_STABLE_ENOUGH_FOR_CANDIDATE_ASSEMBLY = YES
CURRENT_CHANGE = NO
```

Reopen selection if candidate packaging makes optional references behave like mandatory organs or independent validation reveals a material defect.
