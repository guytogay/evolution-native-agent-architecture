# Evidence Envelope reference prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #94 Reconstruction E, #89 anti-ablation reconstruction, PR #82.

## WHAT

Provide one small reusable carrier for claim/evidence/applicability/provenance/witness information without collapsing several distinct behaviors into one generic `evidence=true` field.

The prototype preserves these as separately testable mechanisms:

```text
EVIDENCE EXISTS
!= EVIDENCE SUPPORTS CLAIM
!= SUPPORT APPLIES TO CURRENT SUBJECT
!= WITNESS IS INDEPENDENT/SURVIVABLE
!= CONFIGURED MECHANISM ACTUALLY ACTIVATED
!= DERIVED PROJECTION PRESERVED MATERIAL INFORMATION
```

The envelope is a **reference organ**, not a truth certificate and not a mandated universal schema.

## WHY

Historical ENA/HAR work repeatedly found concrete failures that can be semantically summarized as `evidence discipline`, but that summary is not enough to implement them:

- valid evidence reused after Host/model/runtime changed;
- no represented mismatch narrated as a direct applicability match;
- true projection omits a material negative dependency;
- configured hook treated as evidence it fired;
- witness shares the same mutable failure domain yet is counted as independent;
- several reports derived from one source are counted as corroborating independent supports;
- provenance metadata exists but is restricted/unavailable to the current consumer;
- historical evidence remains true after its support for a current claim expires.

## HOW — prototype files

- `evidence-envelope.v0.1.json` — compact reference vocabulary and derived semantics;
- `fixtures/evidence-envelope-cases.jsonl` — positive/negative deterministic cases;
- `tools/validate_evidence_envelope.py` — stdlib represented-consistency evaluator;
- `tools/selftest_evidence_envelope.py` — portable mutation/adversarial selftest.

## Design rule — shared carrier, preserved mechanisms

The envelope may carry several mechanisms, but the mechanisms are not considered implemented merely because their fields exist.

For example:

```text
witness.failure_domain_ref present
!= witness survived candidate failure

activation.configured = true
!= invocation happened

provenance.source_refs present
!= source authentic

applicability.status = EXPLICIT_MATCH
!= dimensions actually match unless represented checks support it
```

The validator therefore checks each behavior independently where the record makes the corresponding claim.

## Minimal reference shape

Sections are optional unless a claim requires them.

```yaml
envelope_id: EV-1
subject:
  subject_ref: S1
  subject_type: runtime
  state_identity_ref: optional
  failure_domain_ref: optional

claim:
  claim_ref: C1
  claim_type: capability
  asserted_scope: optional

evidence:
  evidence_refs: [E1]
  observation_or_activity_refs: []

support:
  basis: DIRECT_OBSERVATION | DERIVATION | TRANSFER | INFERENCE | CORROBORATION | UNKNOWN
  limitations: []
  dependency_map_ref: optional

applicability:                 # optional; absence means UNKNOWN
  status: EXPLICIT_MATCH | TRANSFER_WITH_BASIS | NARROWER_THAN_CLAIM | UNKNOWN | NOT_APPLICABLE
  evaluated_dimensions: {}
  changed_dimensions: []
  transfer_or_invariance_basis_refs: []

provenance:                    # optional
  producer_or_actor_ref: optional
  activity_or_transformation_ref: optional
  source_refs: []
  access: OPEN | RESTRICTED | UNKNOWN

witness:                       # optional
  witness_ref: optional
  failure_domain_ref: optional
  independence_claim: NONE | PARTIAL | CLAIMED | UNKNOWN
  survivability: SAME_DOMAIN | EXTERNAL_DOMAIN | UNKNOWN

completeness:                  # optional and dimension-scoped
  claimed_complete_dimensions: []
  known_missing_or_unknown: []

projection:                    # optional when subject is derived/projection
  source_subject_refs: []
  material_omissions: []
  preservation_basis_refs: []

activation:                    # optional
  claimed_level: CONFIGURED | INVOKED | EXECUTED | EFFECT_OBSERVED
  invocation_or_trace_ref: optional
  execution_ref: optional
  effect_observed_ref: optional
```

## Reference behaviors

### EE-P01 — Missing applicability is UNKNOWN

No represented mismatch is not an explicit match.

If `applicability` is absent, the effective represented applicability is `UNKNOWN`.

### EE-P02 — EXPLICIT_MATCH cannot coexist with represented changed dimensions

If material dimensions are represented as changed, the record cannot still claim `EXPLICIT_MATCH`.

### EE-P03 — TRANSFER_WITH_BASIS needs a represented transfer/invariance basis

Changed dimensions may still permit evidence transfer, but the basis must be represented.

The validator does not prove the basis is externally true.

### EE-P04 — Material projection omission blocks silent readiness/applicability transfer

If a projection declares decision-material omissions and has no preservation basis, it cannot claim `EXPLICIT_MATCH` or `TRANSFER_WITH_BASIS` as though the effective subject were unchanged.

This composes with #85 without creating a certificate ladder.

### EE-P05 — Activation levels require increasing execution evidence

```text
CONFIGURED      -> no invocation evidence required
INVOKED         -> invocation_or_trace_ref required
EXECUTED        -> invocation_or_trace_ref + execution_ref required
EFFECT_OBSERVED -> invocation_or_trace_ref + execution_ref + effect_observed_ref required
```

A configured hook is not proof it ran.

### EE-P06 — Same-domain witness cannot be represented as independent/survivable external witness

If subject and witness have the same represented failure domain:

- `independence_claim = CLAIMED` is inconsistent;
- `survivability = EXTERNAL_DOMAIN` is inconsistent.

Different represented domains permit the claim structurally but do not prove real independence.

### EE-P07 — CORROBORATION requires dependency representation

If support basis is `CORROBORATION`, a dependency map/reference must be represented so repeated/circular support is not silently counted as independent multiplicity.

### EE-P08 — Completeness is dimension-scoped

A universal `complete: true` field is intentionally not supported.

Completeness claims name the dimensions claimed complete and what remains missing/unknown.

### EE-P09 — Restricted provenance is not invalid evidence

A consumer may be unable to dereference restricted provenance while evidence presence/support metadata remains representable.

`cannot currently read provenance != evidence never existed`.

### EE-P10 — Historical truth may outlive current support

A valid envelope may preserve historical evidence while current applicability is `NOT_APPLICABLE` or `UNKNOWN`.

No history rewrite is required merely because support expired.

## False-BLOCK controls

The full envelope is not required for trivial/non-material observations.

A minimal record may contain only subject + claim + evidence + support. Missing applicability remains honest `UNKNOWN` rather than making the record invalid.

Do not require:

- cryptographic signatures for every observation;
- an external witness for every local fact;
- a dependency map when support basis is not corroboration;
- activation fields for claims that are not about execution/activation;
- full provenance dereference by every consumer;
- one universal environment ontology.

## Evidence boundary

This prototype checks represented consistency only.

```text
ENVELOPE_VALID
!= EVIDENCE_TRUE
!= WITNESS_INDEPENDENT_IN_REALITY
!= TRANSFER_BASIS_CORRECT
!= PROJECTION_SEMANTICALLY_COMPLETE
!= EFFECT_ACTUALLY_OCCURRED
```

Its purpose is narrower:

> prevent the representation layer from upgrading missing/contradictory information into stronger evidence claims while preserving concrete implementation routes for historically distinct evidence mechanisms.

`CURRENT_CHANGE = NO`
