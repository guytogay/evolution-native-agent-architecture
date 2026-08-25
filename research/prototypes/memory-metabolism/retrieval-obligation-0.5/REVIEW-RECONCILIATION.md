# Independent Retrieval-Lifecycle Review Reconciliation

Status: `RESEARCH_EVIDENCE / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

Reviewed target:

`retrieval-obligation-0.4 @ 2389bc45bf88a0fc250a9a8d191b80b5cc2e0c32`

Independent verdict:

`NEEDS_NARROW_REVISION`

## Material review findings and dispositions

### F1 — stable returned-record alias can hide content mutation

Disposition: `REFERENCE_MODEL_BUG`

0.4 fingerprinted bare returned record IDs. A Host could mutate content behind `M1` without changing the represented retrieval subject.

0.5 reconciliation:

`record_ref + content_identity_ref`

The validator now binds the represented effective result identity. It still cannot prove that a Host's content identity is truly immutable/versioned.

### F2 — set serialization caused false re-resolution

Disposition: `REFERENCE_MODEL_OVERREACH`

0.4 treated scope/result list order as fingerprint-significant.

0.5 normalizes set-like `selected_scope_refs` and returned-result identities before fingerprinting.

### F3 — every later discovery invalidated closure

Disposition: `REFERENCE_MODEL_OVERREACH`

The shared property is not "highest sequence wins". It is:

> newer represented decision-material retrieval evidence must not be silently ignored.

0.5 uses reference classifications:

`DECISION_MATERIAL | NON_MATERIAL_OBSERVATION`

Only the current represented decision-material discovery/attempt evidence defines the sufficiency subject.

The validator does not prove that the Host classified materiality truthfully.

### F4 — resolver identity could false-block failover

Disposition: `HOST_ORGAN / REFERENCE_MODEL_CLARIFICATION`

`resolver_ref` is now documented as a logical resolver / trust-equivalence identity, not physical instance identity.

### F5 — sufficiency packet does not authenticate evaluator authority

Disposition: `HOST_ORGAN / EXTERNAL_EVALUATION_ONLY`

No new schema-level authority mechanism added.

Subject binding answers applicability, not legitimacy. A Host must give the evaluator/trust boundary real meaning.

### F6 — negative completeness assertions are also Host assertions

Disposition: `EXTERNAL_EVALUATION_ONLY`

`DECLARED_DISCOVERY_COMPLETE` and `DECLARED_SCOPE_COMPLETE` remain bounded represented assertions. Schema PASS does not make them externally true.

Adding another unauthenticated packet would not solve that problem.

### F7 — restore can revive an old locally consistent retrieval subject

Disposition: `ALREADY_COVERED_BY_CURRENT / RESTORE-MODEL`

No retrieval-specific restore mechanism added.

### F8 — registry/neighbor blindness and expansion cost

Disposition: `HOST_ORGAN / NATURALISTIC_VALIDATION`

No graph/search algorithm promoted to shared ENA architecture.

## ENA-level conclusion

No new ENA rule was established.

Subject-bound retrieval sufficiency is a reference application of existing Current semantics around:

- claim/evidence/support separation;
- triggered material obligations;
- subject/effect/applicability binding;
- continuity/revalidation;
- governance closure;
- `schema PASS != semantic truth`;
- `absence of evidence != evidence of absence`.

## Review stopping decision

Do not request another retrieval-lifecycle architecture reviewer after 0.5 unless a materially new structural mechanism appears.

The next differentiated evidence source should be:

- naturalistic Host use;
- an independently authored registry/task set;
- a materially different resolver/Host architecture;
- or a real failure trace not already derivable from the present model.

Further same-layer review no longer pays epistemic rent.
