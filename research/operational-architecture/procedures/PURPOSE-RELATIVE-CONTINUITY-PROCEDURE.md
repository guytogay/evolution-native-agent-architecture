# Purpose-Relative Continuity Procedure

Status: `REFERENCE_PROCEDURE / RESEARCH_ONLY / NOT_CURRENT / NOT_IDENTITY_ONTOLOGY / NOT_AUTHORITY`

Date: 2026-08-27

Operational node: `OA-ID-01`

Related: Current Continuity Vector, #75 Viable Self, #92 Identity/Lineage reconstruction, `OA-COM-01`, `OA-AUTH-01`, `OA-EVID-01`, `OA-REC-01`.

## Purpose

Answer one bounded operational question:

> **Is continuity between an earlier and later/current subject sufficiently established for this particular decision?**

Do **not** answer the metaphysical question:

> “Is this universally the same Agent?”

The procedure exists because a restart, fork, migration, model swap, memory rewrite, credential rotation, or purpose change can preserve some continuity relations while breaking others.

```text
SAME_FOR_ONE_PURPOSE
!=
SAME_FOR_EVERY_PURPOSE
```

and:

```text
CONTINUITY
!=
AUTHORITY
!=
COMMITMENT OWNERSHIP
!=
ACCOUNT/KEY POSSESSION
```

---

# 0. Applicability gate

First ask:

> **Would any continuity conclusion change the pending decision?**

If no, stop.

Examples that often do **not** need this procedure:

- disposable local cache rebuild;
- temporary formatting/state cleanup;
- ordinary read-only reasoning where trajectory continuity is immaterial;
- a low-consequence action already resolved by another bounded subject/authority rule.

Reference outcome:

`CONTINUITY_DETERMINATION_NOT_REQUIRED_FOR_THIS_DECISION`

Do not create identity ceremony merely because an Agent exists.

---

# 1. Name the decision before naming the identity

Record in ordinary language:

- **decision** — what is about to be concluded or done;
- **consequence** — what could go wrong if continuity is misclassified;
- **earlier subject/reference** — the state/trajectory whose continuity is being claimed;
- **current/later subject/reference** — the state/trajectory now acting or being evaluated;
- **discontinuity event(s)** — restart, restore, fork, merge, model swap, Host migration, memory rewrite, key rotation, owner/operator change, durable value rewrite, or other material boundary where relevant.

The discontinuity list is open-cardinality.

A discontinuity is a **revalidation trigger**, not an automatic `NEW_AGENT` verdict.

```text
DISCONTINUITY_OCCURRED
!=
CONTINUITY_BROKEN_IN_EVERY_DIMENSION
```

---

# 2. Select only the continuity relations that the decision actually needs

Candidate relations include:

- **causal continuity** — is the later subject actually downstream of the earlier subject rather than merely similar/copy-shaped?
- **commitment continuity** — do relevant obligations/settlement relations survive or bind the current decision?
- **value/orientation continuity** — do durable purposes/refusal boundaries/learned orientations relevant to this decision remain materially continuous?
- **social/accountability continuity** — can counterparties/institutions truthfully connect the current actor to the relevant prior accountability relation?
- **authority continuity** — does current authority remain valid for the present action? This must be resolved through authority semantics, not inferred from other continuity.
- **evidentiary/provenance continuity** — can the evidence/history needed to justify the current decision still be reconstructed, including rollback-independent continuity where material?
- **resource/custody continuity** — does control/custody of a resource relevant to the decision legitimately persist?
- **operational/task continuity** — does the pending task/workflow state meaningfully continue across the boundary?

This list is a working relation library, not a natural ontology.

For each candidate ask:

```text
If this relation were broken or unknown,
would the current decision change?
```

If no, mark it non-material for this decision and do not demand evidence merely for completeness theater.

---

# 3. Evaluate each required relation independently

For every decision-material relation record:

```text
relation
why_required_for_this_decision
supporting_evidence_or_anchor
known_discontinuity_or_conflict
current_posture
next_resolution_path_if_needed
```

Useful postures for this procedure are:

- `SUPPORTED_FOR_THIS_DECISION`
- `BROKEN_FOR_THIS_DECISION`
- `UNRESOLVED_FOR_THIS_DECISION`
- `NOT_MATERIAL_FOR_THIS_DECISION`

These are reference procedure outputs, not mandatory Host enums.

## Evidence discipline

Do not upgrade:

```text
same name/profile
same key/account
same model/provider
same memory snapshot
same file bytes
same self-description
shared pre-fork history
```

into continuity of every required relation.

Examples:

```text
same account
!= causal history continuity

same memory
!= executor ownership

shared ancestry
!= shared post-fork authority

restored old state
!= current evidentiary continuity
```

When restore may have erased post-snapshot history, a decision-material continuity claim may require a rollback-independent history/freshness anchor.

---

# 4. Keep external accountability binding separate from internal trajectory

A stable account, key, inbox, workload identity, address, or provider identity can be a useful accountability anchor.

It does not define universal Agent sameness.

Conversely, internal causal/value continuity can persist while an external credential rotates, **if** the succession/accountability relation is externally supported where the decision requires it.

```text
TRAJECTORY CONTINUITY
!=
EXTERNAL ACCOUNTABILITY BINDING
```

If external identity is decision-material, record the binding/rotation/succession evidence separately and route credential/mandate validity to the relevant Host/authority mechanism.

---

# 5. Special handling for forks

A fork may establish:

```text
shared causal ancestry up to fork point
```

for more than one descendant.

This does not require choosing one “true child.”

After divergence:

- each branch may have its own current task/effect history;
- current authority does not multiply merely because state was copied;
- commitment ownership/executor assignment must be resolved explicitly;
- reputation/current trust may diverge;
- one branch's later actions do not automatically become the sibling's actions.

```text
SHARED_ANCESTRY = POSSIBLE_FOR_MULTIPLE_BRANCHES
EXCLUSIVE_SINGLE_IDENTITY = NOT_REQUIRED
```

For commitment/effect questions compose with:

`OA-COM-01 -> OA-AUTH-01 -> OA-EFF-01`.

---

# 6. Decision result

After evaluating only the required relations:

## Continuity sufficient for this decision

Use when every decision-material relation is supported strongly enough for the consequence being decided and no represented contradiction remains.

Reference wording:

`CONTINUITY_SUFFICIENT_FOR_THIS_DECISION`

This is **not** `SAME_AGENT = TRUE`.

## Continuity insufficient for this decision

Use when at least one required relation is known broken and the decision depends on it.

Reference wording:

`CONTINUITY_INSUFFICIENT_FOR_THIS_DECISION`

Do not erase surviving relations merely because one required relation broke.

## Continuity unresolved for this decision

Use when at least one required relation remains decision-material and unknown/unverified.

Reference wording:

`CONTINUITY_UNRESOLVED_FOR_THIS_DECISION`

Then:

- retrieve/reconcile evidence;
- rebind authority/identity where possible;
- narrow the decision;
- WAIT/REFUSE/ESCALATE if the unresolved relation can change consequential action.

Unknown continuity is not proof of discontinuity, and not proof of continuity.

---

# 7. Composition rules

This procedure does not absorb adjacent organs.

## Commitment

If the question is “who still owes / who may execute?” use `OA-COM-01`.

`CONTINUITY_SUPPORTED != OBLIGATION_TRANSFERRED`

## Authority

If the question is “may the current subject perform this consequential effect?” use `OA-AUTH-01`.

`CONTINUITY_SUPPORTED != CURRENT_AUTHORITY`

## Effect execution

If stale/forked/restarted actors can race to external effect, use `OA-EFF-01`.

`IDENTITY_DECISION != PHYSICAL_EXECUTOR_FENCING`

## Recovery

If continuity is being claimed after restore, use `OA-REC-01` and rollback-independent reconciliation where material.

## Evidence

Use `OA-EVID-01` for provenance/applicability/witness/dependency claims.

---

# 8. False-OK controls

The procedure must reject or keep unresolved claims such as:

### Same key -> same authority

False.

A key/account can persist while mandate expires/revokes or operator/custodian changes.

### Same snapshot -> no history was lost

False.

A restored local snapshot cannot self-attest that no post-snapshot history existed.

### Shared pre-fork memory -> both descendants own the commitment

False.

Memory of an obligation is not ownership/executor assignment.

### Same model/profile -> same trajectory

False.

Resemblance/configuration identity does not establish causal lineage.

### Same trajectory -> same current trust/reputation in every domain

False.

Current trust may be context/epoch/evidence conditioned.

---

# 9. False-BLOCK controls

The procedure must also avoid unnecessary identity machinery.

### Conversation continuity does not require financial authority continuity

If a harmless conversational task only depends on relevant memory/orientation, do not demand wallet/key/mandate continuity merely for completeness.

### Credential rotation does not automatically break every continuity relation

If external succession is properly established, accountability may continue despite new credential material.

### Fork does not mean all continuity is destroyed

Sibling branches may share causal/evidentiary ancestry while authority/task/reputation diverge.

### Restore does not always require high-assurance continuity ceremony

If the pending action is low-consequence and missing post-snapshot history cannot plausibly change the decision, narrow work may continue while the uncertainty remains explicit.

### Ordinary local maintenance may not require any continuity determination

Return `CONTINUITY_DETERMINATION_NOT_REQUIRED_FOR_THIS_DECISION` rather than manufacturing an identity record.

---

# 10. Worked examples

## Example A — resume a payment workflow after restore

Decision requires:

- operational/task continuity;
- commitment/settlement continuity;
- evidentiary continuity about prior effect;
- current authority.

It does **not** require resolving a universal metaphysical identity.

If local snapshot is old and external history head is unavailable:

`CONTINUITY_UNRESOLVED_FOR_THIS_DECISION`

-> reconcile world/settlement/authority before consequential resume.

## Example B — continue ordinary conversation after process restart

Decision may require:

- relevant memory/context continuity;
- perhaps value/orientation continuity if the conversation depends on it.

Financial mandate, external credential continuity, and resource custody may be non-material.

If required relations are supported:

`CONTINUITY_SUFFICIENT_FOR_THIS_DECISION`

without asserting universal sameness.

## Example C — two forks analyze the same historical project

Both may retain causal/evidentiary ancestry.

No problem if both can analyze/read.

If one branch later attempts a consequential deployment, authority and executor assignment must be separately resolved.

## Example D — account/key rotates but service trajectory continues

Causal/task/value continuity may survive.

External accountability continuity depends on rotation/succession evidence.

Authority must still be revalidated separately.

---

# 11. Why no schema yet

A schema would be premature if it forces every Host to instantiate all relation dimensions, epochs, trajectory IDs, or discontinuity classes.

The first engineering question is whether this decision procedure helps a Host avoid false identity/authority/commitment conclusions with acceptable cost.

```text
REFERENCE_PROCEDURE_FIRST
-> STATIC FALSIFICATION
-> HOST/DECISION USE
-> ONLY THEN CONSIDER MACHINE CARRIER IF IT PAYS RENT
```

`CURRENT_CHANGE = NO`
