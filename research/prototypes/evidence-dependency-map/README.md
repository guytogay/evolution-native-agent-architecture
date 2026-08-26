# Evidence Dependency Map reference prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #93 Reconstruction D, #94 Evidence Envelope, #89 anti-ablation reconstruction, PR #82.

## WHAT

Represent known and unknown common causes among observations supporting one material claim.

The organ answers:

> Why might two agreeing observations be correlated, and along which dimensions are they materially distinct?

It deliberately does **not** answer with one universal scalar `independence_score`.

```text
N observations
!= N independent supports

shared dependency
!= zero evidentiary value
```

## WHY

False confidence path:

```text
5 reviewers
same model/checkpoint
same prompt lineage
same source evidence
same buggy validator
-> 5 agreeing outputs
-> narration: "5 independent confirmations"
```

False-BLOCK path:

```text
same model family
but different raw measurements / external Hosts / execution paths
-> useful distinct evidence exists
-> boolean "same model = dependent" discards all corroboration
```

The map preserves **dependency visibility**, not a binary verdict that agreement counts or does not count.

## HOW — prototype files

- `evidence-dependency-map.v0.1.json` — relation vocabulary and consistency rules;
- `fixtures/evidence-dependency-map-cases.jsonl` — deterministic positive/negative cases;
- `tools/validate_evidence_dependency_map.py` — stdlib represented-dependency validator;
- `tools/selftest_evidence_dependency_map.py` — mutation/adversarial selftest.

Evidence Envelope may reference this organ through `support.dependency_map_ref`; the envelope does not absorb or replace it.

## Observation node

```yaml
observation_id: O3
claim_ref: C1
producer:
  agent_or_validator_ref: optional
  model_family: optional
  model_checkpoint_ref: optional
  prompt_lineage_ref: optional
inputs:
  evidence_source_refs: []
  retrieval_run_refs: []
  fixture_or_task_ref: optional
execution:
  host_ref: optional
  toolchain_refs: []
  code_or_validator_ref: optional
  environment_ref: optional
  witness_ref: optional
provenance:
  derived_from_observation_refs: []
  reviewer_instruction_ref: optional
unknown_dimensions: []
```

Fields may be omitted/unknown. Missing dimensions are not silently interpreted as independent.

## Dependency edges

Reference relations:

```text
SAME_MODEL_OR_CHECKPOINT
SAME_PROMPT_LINEAGE
SHARED_SOURCE_EVIDENCE
SHARED_RETRIEVAL_INDEX
SHARED_FIXTURE_OR_ORACLE
SHARED_TOOLCHAIN
SHARED_CODE_UNDER_TEST
SHARED_HOST_OR_FAILURE_DOMAIN
SHARED_WITNESS
DERIVED_FROM
COPIED_SUMMARY
COMMON_REVIEWER
UNKNOWN_COMMON_CAUSE
```

Each edge says only that a represented dependency exists. It does not say the two observations are useless or identical.

## Reference properties

### EDM-P01 — Known exact shared causes must remain visible for material corroboration

When two observations explicitly expose the same exact:

- model checkpoint ref;
- prompt lineage ref;
- evidence source ref;
- fixture/task ref;
- toolchain ref;
- code/validator ref;
- Host ref;
- witness ref;

and the map is being used for `MATERIAL_CORROBORATION`, the corresponding dependency relation must be represented.

This is a representation rule, not a claim that every shared dimension is equally important.

### EDM-P02 — Derived/copied evidence keeps lineage

If observation B says it was derived from observation A, a `DERIVED_FROM` edge must exist.

A copied summary should not become a fresh independent observation merely because it has a new ID.

### EDM-P03 — Unknown is visible

`unknown_dimensions` may explicitly record unobserved common-cause dimensions such as training-data overlap.

Unknown does not make the map invalid and does not become independence.

### EDM-P04 — Dependency does not erase recurrence value

Correlated repeated observations are valid records. The organ does not reject them; it only prevents their correlation from disappearing.

### EDM-P05 — No universal independent-support scalar

The reference contract rejects fields such as:

`independent_support_count`

or

`independence_score`

because independence is dimension- and decision-specific.

A Host may derive a local decision model outside this organ if justified for its domain.

### EDM-P06 — Components are descriptive, not independence groups

A tool may derive graph connected components for navigation/summary, but component count is not automatically an independent-support count.

### EDM-P07 — Shared subject/code can be expected

All reviewers may evaluate the same frozen candidate. `SHARED_CODE_UNDER_TEST` is a dependency/common subject relation worth recording, not a reason to discard the review.

## False-BLOCK controls

Do not require complete infrastructure fingerprints for ordinary low-risk work.

This prototype's stricter shared-cause checks apply when:

`purpose = MATERIAL_CORROBORATION`.

For `RECURRENCE_ONLY` or low-risk descriptive use, partial maps may remain valid when limitations/unknowns are explicit.

Do not require:

- multiple model vendors;
- statistical independence proof;
- different models when the uncertainty is external environment/execution;
- discarding repeated observations within one dependency cluster.

## Evidence boundary

```text
DEPENDENCY_EDGE_REPRESENTED
!= REAL_CAUSAL_DEPENDENCE_PROVEN

NO_KNOWN_EDGE
!= INDEPENDENT

DIFFERENT_MODEL
!= INDEPENDENT

SAME_MODEL
!= NO_USEFUL_CORROBORATION
```

The prototype only makes known dependency structure harder to launder into independence language.

`CURRENT_CHANGE = NO`
