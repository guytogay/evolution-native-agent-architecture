# Independent review 03 — formal-methods / systems-boundary review of iteration 0.5

Review source: fresh ChatGPT temporary conversation supplied by maintainer.

Reviewed target:

`iteration-0.5 @ 6d1370cde1f119e813408dbca0dda77009ab1e30`

Status boundary preserved:

`RESEARCH_PROTOTYPE / DRAFT / NOT_CURRENT_BASELINE / NOT_RELEASE_CANDIDATE`

Reviewer final verdict:

`NEEDS_NARROW_REVISION`

Reviewer stop verdict:

`security-side review should STOP after reconciliation`

## Independent narrow-waist assessment

`PARTIALLY_ORGAN_NEUTRAL`

The reviewer found that iteration 0.5 successfully removed the prior universal-looking access-label lattice, but still treated several reference-mechanism assumptions too strongly: stable opaque-token identity/equality, mandatory boundary objects, exact actor-access sets, exact transition-mode objects, record-ID-based Host resolution, and exact provenance-access references.

The reviewer explicitly rejected the conclusion that a new ENA Constitution rule was needed.

## Material findings

### F1 — effect-equivalent lineage bypass

`relations.DERIVED_FROM` could encode a derivation edge that canonical lineage ignored. A restricted source could therefore influence a compiled record through an effect-equivalent representation while escaping provenance/boundary checks applied to `derived_from` / evidence lineage.

Classification: `REFERENCE_MODEL_BUG + ALREADY_COVERED_BY_CURRENT`.

### F2 — Host resolution not subject-bound

A Host-resolution assertion was keyed only to mutable `record_id` membership. The record content, lineage, boundary transition, resolution ref, Host/time/epoch, or artifact version could change while the same ID remained accepted.

Classification: `REFERENCE_MODEL_BUG`; shared semantic requirement is current resolution bound to the relevant subject/effect; concrete binding organ remains Host-specific.

### F3 — opaque-ref equality unsafe across Host/epoch reuse

Literal equality of an opaque token could be treated as semantic boundary continuity even if the same token was reused with different meaning in another Host/policy epoch.

Classification: `HOST_ORGAN + ALREADY_COVERED_BY_CURRENT`.

### F4 — candidate metadata can itself be an information consequence

A pre-disclosure candidate ID/title/index value may reveal restricted information if it escapes the internal retrieval organ. Candidate != record-content disclosure is not enough to prove candidate metadata has no consequence.

Classification: `REFERENCE_MODEL_BUG / ALREADY_COVERED_BY_CURRENT` when metadata crosses the boundary.

### F5 — provenance handle leakage

A provenance handle may itself reveal restricted source identity even if dereferencing is separately protected. Provenance existence, provenance metadata visibility, and provenance inspection are distinct.

Classification: `REFERENCE_MODEL_BUG or HOST_ORGAN` depending projection semantics.

### F6 — `DEGRADED` evidence availability under-specified

`DEGRADED` could validate even when no evidence remained PRESENT. The vocabulary therefore implied a partial-evidence state it did not enforce.

Classification: `REFERENCE_MODEL_BUG`.

### F7 — simple-Host false-BLOCK / ceremony

A one-user private Host with no multi-tenant/publication boundary was still forced to manufacture explicit access/boundary/projection security objects.

Classification: `REFERENCE_MODEL_OVERREACH`.

### F8 — token inequality treated as semantic boundary change

Two different opaque references that a Host considers semantically equivalent still forced a boundary-change workflow.

Classification: `REFERENCE_MODEL_OVERREACH / HOST_ORGAN`.

## Scaling findings

The old access-label accumulation failure was **not reproduced** in iteration 0.5. No security-specific hot-state accumulation contradiction was established.

Cold provenance growth remains potentially unbounded, but that is the intended cold side of the bounded-active-memory design and returns to the general Memory Metabolism problem rather than a new security defect.

## Vacuity finding

The abstraction was judged **not fully vacuous**. Without trusting the Host, 0.5 still rejected several structurally dishonest representations. However a PASS only established represented separation between memory claims and trusted Host inputs; it did not prove a real security policy was obeyed.

## Things suspected but falsified

- record-level transition claims alone did not make a transition effective;
- public compiled content did not automatically grant provenance inspection;
- `FULL` evidence availability required all reachable represented evidence PRESENT;
- multiple direct boundary refs could not silently collapse without a composition claim;
- no universal policy-epoch object or federation/remapping protocol was justified;
- a universal privacy/noninterference theorem was not appropriate for this prototype.

## Host-specific / out-of-scope remainder

The reviewer explicitly kept the following outside shared Memory Metabolism semantics:

- real policy ordering/equivalence;
- authentic actor entitlement;
- declassification/publication authority;
- tenant and purpose restrictions;
- policy expiry/revocation/epochs;
- semantic sanitization/de-identification;
- privacy inference/re-identification;
- DLP/RBAC/ABAC/IFC machinery;
- concrete subject/version binding mechanism;
- cross-Host policy remapping;
- candidate/provenance metadata observability;
- privacy/policy composition.

## ENA reconciliation

Reviewer conclusion:

- no genuinely new ENA semantic property was discovered;
- the candidate sentence `Memory transformation must not silently widen the legitimate information-use, access, publication, or consequence boundary of represented source information` is already implied by Current as a recomposition/application;
- useful explanatory synthesis: `internal representation change != external authority/boundary change`;
- that synthesis pays explanatory rent, not constitutional rent;
- another generic security/privacy reviewer would not add likely epistemic value after narrow reconciliation.

## Final stopping decision preserved

After deterministic reconciliation of F1–F8, security-focused structural review stops.

Research returns to:

`UNKNOWN-KNOWN / RETRIEVAL REFLEX / BOUNDED DISCOVERY OF COLD MEMORY`.
