# Retrieval Obligation 0.5 — Narrow Reconciliation After Independent Review

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT_BASELINE / NOT_AUTHORITY / NOT_RELEASE_CANDIDATE`

Independent review target: `retrieval-obligation-0.4 @ 2389bc45bf88a0fc250a9a8d191b80b5cc2e0c32`

Independent verdict: `NEEDS_NARROW_REVISION`

The reviewer found no new ENA-level semantic rule. The useful repairs are reference-level and should be completed before naturalistic Host validation.

## 0.5 changes

### 1. Effective result identity

0.4 fingerprinted `returned_record_ids`. A stable alias could therefore keep the same subject fingerprint while the content behind that ID changed.

0.5 represents each returned result as:

`record_ref + content_identity_ref`

The intended property is:

> sufficiency applies to the effective retrieval result that was evaluated, not merely to a reusable record alias.

`content_identity_ref` is a reference encoding. The validator does not prove that a Host's content identity is truly immutable/versioned.

### 2. Semantic-set normalization

0.4 fingerprinted array serialization literally.

0.5 normalizes:
- `selected_scope_refs` as an unordered set;
- `returned_results` by `(record_ref, content_identity_ref)`.

Therefore harmless reordering does not force semantic re-resolution.

This is a reference normalization, not a new ENA rule.

### 3. Decision-material freshness instead of every later event

0.4 required the closure to bind the numerically latest discovery, even if a later discovery was audit-only, duplicate-equivalent, speculative, or failed without changing the sufficiency subject.

0.5 adds reference classifications:

`DECISION_MATERIAL | NON_MATERIAL_OBSERVATION`

The closure must bind the latest represented **decision-material** discovery. The sufficiency fingerprint includes decision-material attempts from that discovery, while non-material observations remain recorded without automatically invalidating the resolved subject.

This does not let the validator prove materiality. A Host can still misclassify a material event as non-material. That remains an external/evaluation truth problem.

Shared property:

> a closure must not silently ignore newer represented decision-material retrieval evidence.

Reference encoding:

> `subject_relevance` and numeric sequence.

### 4. Logical resolver identity

`resolver_ref` is clarified as a logical resolver / trust-equivalence identity, not a physical process, instance, route, or machine identity.

Legitimate failover may remain inside one resolver identity when the Host can justify semantic/trust equivalence.

The shared contract does not define a universal failover protocol.

## Deliberate residuals

0.5 still cannot prove:

- that R0 should have fired;
- that discovery completeness is true;
- that a scope registry is current;
- that the resolver found every relevant record;
- that `content_identity_ref` is truthful/immutable;
- that `subject_relevance` is correctly classified;
- who is authorized/competent to issue sufficiency;
- who is authorized/competent to assert negative completeness;
- restore/current-world freshness;
- Host/tenant namespace equivalence;
- projection/application correctness;
- Search-All economics.

These are not invitations to add more fields automatically.

## Positive/negative trust boundary

`RETRIEVAL_SUFFICIENCY_RESOLVED` remains a useful boundary only if a Host gives the external evaluator real meaning.

Likewise:

`DECLARED_DISCOVERY_COMPLETE`
and
`DECLARED_SCOPE_COMPLETE`

are decision-changing Host assertions, not truths minted by schema acceptance.

A second unauthenticated packet for the negative path would not solve this trust problem.

## No new ENA rule

The reviewer found that the parent semantics are already represented by Current:

- `claim != evidence != support relation`;
- `schema PASS != semantic truth`;
- `absence of evidence != evidence of absence`;
- triggered material obligations should be externalized;
- applicability/authority/evidence must remain bound to the relevant subject;
- restore/clone/failover can invalidate affected applicability;
- governance should stop when another bounded check cannot change the decision.

Therefore:

> Retrieval 0.5 is a reference application/recomposition, not a Constitution candidate.

## Stop rule

Do not request another retrieval-lifecycle architecture reviewer after this narrow reconciliation unless a materially new structural mechanism appears.

The next differentiated evidence source should be naturalistic Host use or an independently authored Host/registry/task distribution.

## Reference machine checks

`selftest.py` contains 17 deterministic cases covering:

- effective result identity changes;
- harmless set reordering;
- non-material later observations;
- material later evidence;
- false-complete discovery as an explicit external residual;
- bounded no-hit;
- decision-context replay;
- fresh re-resolution after subject change;
- logical resolver identity consistency.

A PASS proves represented consistency only.
