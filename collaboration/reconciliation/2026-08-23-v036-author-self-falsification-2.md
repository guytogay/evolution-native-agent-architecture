# ENA v0.3.6 author self-falsification — pass 2

Status: `AUTHOR_SELF_FALSIFICATION / PRE_FREEZE / NOT_INDEPENDENT_VALIDATION`

This pass attacks second-order effects after the first latent/expression corrections.

## Finding B1 — v2 schema inherited a weaker UNKNOWN evidence boundary than the validated reference tool

Severity: `MATERIAL_SEMANTIC_DRIFT`

The inherited v1 JSON Schema required evaluations for `UNKNOWN` but did not require an experiment. The v0.3.5 reference `ena_evolve.py`, however, calls `require_experiment()` before accepting any evaluation, including `UNKNOWN`.

The v0.3.5 semantics also state that any represented selection verdict other than initial `UNASSESSED` follows represented experiment/reality contact.

Blindly copying the old schema condition into v2 would therefore weaken an already-stronger validated implementation boundary.

Correction:

- v2 requires at least one represented experiment for every selection state other than `UNASSESSED`;
- latent untested possibilities remain `UNASSESSED`, which is precisely why immediate selection is no longer required;
- `UNKNOWN` remains available after reality contact when evidence cannot support a stronger verdict.

## Finding B2 — publisher/receiver autonomy could be misread as permission to publish unowned material

Severity: `MATERIAL_EXTERNALITY_AMBIGUITY`

The working baseline contained `receiver_can_block_source_publication_by_default: false` and the Commons prose emphasized publisher autonomy.

That formulation can be over-read as: a receiver or other Protected Subject can never have a legitimate publication veto. This is false when publication includes data, secrets, privacy interests, contractual constraints, shared resources, or other consequences over which the publisher lacks sole authority.

Correction:

- non-adoption by a receiver is not, by itself, a veto over independently authorized publication;
- publication still requires actual publication authority and must respect Protected Subjects / third-party constraints;
- publisher autonomy and receiver autonomy are independence properties, not immunity from consequence ownership.

## Finding B3 — a new v2 schema must preserve inherited positive/negative selection guards

Severity: `MATERIAL_MACHINE_GUARD_GAP`

JSON Schema shape alone can accept a `SUPPORTED` record whose latest evaluation has no `IMPROVED` dimension or empty evidence references. The inherited reference tool already rejects that false-positive path.

If v2 is presented as the candidate machine record, it should not silently become weaker than the validated predecessor tool.

Correction direction:

- companion v2 consistency validator checks latest evaluation matches current selection;
- positive selection requires at least one `IMPROVED` outcome and evidence reference;
- `HARMFUL` requires at least one `DEGRADED` outcome and evidence reference;
- `NOT_SUPPORTED` requires represented outcomes/evidence;
- lifecycle `PROPOSED` cannot coexist with represented experiments; `EXPERIMENTED` requires experiment;
- `INTEGRATED` requires represented experiment, current evaluation, and integration history.

These are represented consistency guards, not external-world proof.

## Disposition

B1/B2/B3: correct before freeze.

No new Constitution ID is justified by these findings; existing Constitution semantics already cover truth, scoped authority, local applicability, and external consequence.
