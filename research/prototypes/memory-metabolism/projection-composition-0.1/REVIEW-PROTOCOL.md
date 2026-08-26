# Independent cross-prototype composition review protocol

Review target commit:

`28e25cd0406ac3719ff353a028dd2e742078e686`

Status: `REVIEW_PROTOCOL / NOT_REVIEW_EVIDENCE / NOT_CURRENT_BASELINE`

The reviewer must freeze to the target commit above and must not silently follow later branch changes.

## Role

Act as a fresh independent **cross-prototype composition reviewer**.

Do not re-review generic Memory security or Retrieval-lifecycle architecture. Those same-layer review chains are already closed by stop rule.

The only core question is:

> Can a retrieval-sufficiency assessment survive transformation into a different bounded effective Decision Projection without laundering readiness, and can the proposed reconciliation avoid false-BLOCK and certificate-ladder bureaucracy?

## Phase A — blind machine/interface inspection

Before reading #85 discussion, PR comments, Current, or `RECONCILIATION.md`, inspect:

- `retrieval-obligation-0.5/retrieval-obligation.schema.json`
- `retrieval-obligation-0.5/validate_retrieval_obligation.py`
- `iteration-0.6/memory-set.schema.json`
- `iteration-0.6/validate_memory_metabolism.py`
- `projection-composition-0.1/cases.json`
- `projection-composition-0.1/evaluate_projection_composition.py`
- `projection-composition-0.1/selftest.py`

Infer the actual contracts from machine behavior first.

Attack:

1. **Readiness laundering** — can Retrieval `READY` be treated as final readiness after a later lossy projection?
2. **Material omission** — retrieved material limitation/contradiction disappears from the effective projection.
3. **False-BLOCK** — harmless omission, redundant hits, exploratory hits, or faithful compaction unnecessarily force re-evaluation.
4. **Self-declared materiality** — can `decision_material=false` simply launder a material omission?
5. **Self-declared fidelity** — can `PRESERVES_DECISION_EFFECT` simply launder a lossy summary?
6. **Subject staleness** — can a valid assessment survive a later effective-projection change?
7. **Identity overreach** — does the fixture require identical representations when semantic decision effect is preserved?
8. **Certificate ladder** — does the proposed direction require a new universal sufficiency object at every stage?
9. **Stage boundary** — is Retrieval 0.5's `decision.disposition=READY` genuinely stage-local in implementation, documentation, and likely consumption, or does the reference API overstate its level?
10. **Composition beyond projection** — identify whether interpretation/salience/application creates the same failure shape, but do not demand a universal certificate chain unless a distinct shared mechanism is proven.

For each material finding classify it as:

- `REFERENCE_MODEL_BUG`
- `REFERENCE_MODEL_OVERREACH`
- `CROSS_PROTOTYPE_INTERFACE_GAP`
- `HOST_SEMANTIC_TRUST_BOUNDARY`
- `EXTERNAL_EVALUATION_ONLY`
- `POTENTIAL_CORE_GAP`
- `FALSE_ALARM`

One deterministic trace is enough to establish structural reachability.

## Phase B — reconciliation with Current

Only after Phase A, read as needed:

- `projection-composition-0.1/README.md`
- `projection-composition-0.1/RECONCILIATION.md`
- Issue #85
- PR #82 comments
- ENA v0.3.6 Current sections on Local Projection, claim/evidence/support, governance closure, composition, whole effect surface.

Answer:

1. Is `retrieval lifecycle closed != final consequential decision ready` already implied by Current?
2. Does `Sufficiency does not automatically survive a material lossy subject transformation` add a genuinely new ENA property?
3. Is `PRESERVES_DECISION_EFFECT` merely a reference Host assertion, and if so is that honest or vacuous?
4. Can a Host preserve bounded memory without keeping all retrieved records hot?
5. Is a new Retrieval 0.6 justified?
6. Is a Current mutation justified?
7. Would another same-family reviewer pay epistemic rent?

## Stopping rule

If the reviewer finds no materially new shared mechanism beyond:

- stage-local closure;
- subject/applicability revalidation after material transformation;
- Host responsibility for semantic materiality/fidelity;

then cross-prototype review should STOP and #85 should move to reference reconciliation / future naturalistic observation.

Do not recommend another reviewer merely because projection, attention, or context are broad subjects.

## Final verdict

End with exactly one:

- `COMPOSITION_RECONCILIATION_SURVIVES`
- `NEEDS_NARROW_REVISION`
- `READINESS_BOUNDARY_TOO_VACUOUS`
- `PROJECTION_CONTRACT_OVER_SPECIFIED`
- `GENUINE_CORE_GAP_FOUND`

Then state:

- strongest structural false-OK;
- strongest false-BLOCK;
- strongest Host-trust residual;
- minimal property that pays rent;
- whether Retrieval 0.6 is needed: YES/NO;
- whether Current needs a change: YES/NO;
- whether another cross-prototype reviewer is justified: YES/NO;
- whether #85 may move to naturalistic observation after reconciliation: YES/NO/ONLY_AFTER_<condition>.

This review does not authorize repository modification, merge, release, Current mutation, or promotion.
