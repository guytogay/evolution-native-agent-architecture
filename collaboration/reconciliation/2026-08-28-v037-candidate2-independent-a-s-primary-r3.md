# ENA v0.3.7-candidate.2 — Independent A-S Report (primary r3)

## 1. Review identity and boundary

- Review mode: fresh independent A-S clean-room review.
- Requested clean-room repository commit: `28dde50c9caaeee3b5cfabf51410083dbbb05a93`.
- Capsule-declared target identity: `v0.3.7-candidate.2`.
- Capsule-declared source commit: `bda470e0a6b170cec61225a905957a501454a2fe`.
- Capsule-declared candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`.
- Attack cardinality: `OPEN`.
- A-P and Phase B: NOT PERFORMED.

I began from the clean-room root `README.md` and `INTAKE-A-S.md`, then used only material exposed by this clean-room repository state. I did not use author fixtures/oracles, prior findings, project-manager context, Current, historical releases, or A-P material.

Repository-wrapper identity note: in this review environment, direct GitHub resolution of the requested wrapper commit SHA returned an unavailable/not-found response, while the repository root exposed a single-commit A-S capsule and the current root bytes matched the declared A-S intake/manifest surface. I therefore reviewed the current clean-room bytes only and did not substitute any external project repository or history. This limits independent attestation of the wrapper Git object, but not the file-level findings below.

## 2. Overall A-S verdict

**NOT CLEARED.**

I found three substantive represented-semantics/executable-behavior defects, two of which can directly create false authorization or unsafe duplicate-effect posture, plus one A-S sealing-procedure contradiction.

Priority:

1. **A-S-01 — BLOCKER/HIGH:** composed authority resolution can authorize an explicitly revoked or scope-incompatible represented grant.
2. **A-S-02 — BLOCKER/HIGH:** Effect Lifecycle permits a later `NOT_COMMITTED` receipt to override an earlier known `COMMITTED` receipt and return `RETRY_SAME_INTENT`.
3. **A-S-03 — HIGH:** transferred source evolution history lacks local-equivalent chronology/snapshot checks and accepts impossible `INTEGRATED` histories.
4. **A-S-04 — PROCESS BLOCKER:** the intake's exact-file self-hash instruction is not satisfiable as written.

These are not claims about external-world truth. They are contradictions or unsafe gaps inside the represented semantics that the shipped validators themselves claim to check.

## 3. A-S-01 — Composed authority path accepts revoked / out-of-scope represented grants

**Severity:** BLOCKER / HIGH

### Evidence

`05-CORE-OPERATIONAL-CONTRACTS.md` states that authority remains bound to the subject, effect, task/purpose, consequence, and source of mandate, and distinguishes identity/capability/authority/credential validity/mandate horizon. It also describes the composed validator as retaining positively typed/registered authority semantics.

The standalone Authority Lease validator enforces represented temporal and scope semantics, including:

- `valid_from`;
- `expires_at`;
- `status == REVOKED` plus `revoked_at`;
- grantee;
- action;
- protected subject;
- task scope;
- host scope;
- optional grantee epoch;
- optional credential binding.

By contrast, `tools/validate_contracts.py::check_binding()` resolves an authority-registry entry and treats it as authorizing when:

- `agent` is absent or matches;
- `host` is absent or matches;
- `expires_at` parses and is not before evaluation time.

It does not reject on represented `status=REVOKED`, `revoked_at`, `valid_from`, allowed action, protected subject, task scope, grantee epoch, or credential scope. Missing `expires_at` is effectively treated as `2999-12-31`.

### Constructed counterexample

A composed case can contain:

- evaluation date after `revoked_at`;
- a grant with `status: REVOKED`;
- grant scopes naming a different action/subject/task;
- matching `agent`, matching `host`, and future `expires_at`;
- `binding.authority_envelope` non-empty;
- `binding.mandate.source` pointing to that grant.

The represented grant is clearly non-authorizing under the standalone Authority Lease rules, yet the composed binding path produces no authority error. With no other blocking artifacts, the composed case verdict is `OK`.

I reproduced the relevant shipped logic with such a case; the authority state list was empty and the resulting composed verdict was `OK`.

### Why this matters

This is not merely “external mandate authenticity is unproven.” The counterexample supplies explicit represented revocation and scope facts, and the composed validator ignores them. That creates false confidence inside the represented record itself.

It also creates a cross-layer disagreement:

`Core contract authority semantics`
`!=`
`standalone authority-lease represented semantics`
`!=`
`composed-validator authority semantics`

### Required correction

At minimum, the composed authority path should either:

1. delegate to the same represented Authority Lease resolution semantics; or
2. define a distinct composed grant type that cannot carry ignored revocation/scope fields and whose narrower semantics are explicitly documented.

If a registry entry can carry revocation/scope data, the validator must not silently authorize while contradicting those fields.

## 4. A-S-02 — Known COMMITTED effect can be downgraded to retryable NOT_COMMITTED

**Severity:** BLOCKER / HIGH

### Evidence

`references/general/effect-lifecycle/effect-lifecycle.v0.1.json` defines:

- EL-R03: known committed external state outranks restored/local pending narration; a valid represented `COMMITTED` receipt must not cause another realization merely because local state says pending.
- EL-R10: local rollback does not rewrite external occurrence truth.

`validate_effect_lifecycle.py` does reject a `REALIZE` attempt whose sequence occurs after a terminal `COMMITTED`/`COMPENSATED` receipt. However, it does not reject a later receipt for the same effect whose status moves backward from `COMMITTED` to `NOT_COMMITTED`.

`next_action()` sorts receipts by sequence and uses only the latest receipt status. Therefore a later `NOT_COMMITTED` status returns `RETRY_SAME_INTENT`.

### Constructed counterexample

A structurally valid record:

```json
{
  "effects": [{
    "effect_id": "e1",
    "effect_class": "EXTERNAL_IRREVERSIBLE",
    "target": "world",
    "operation": "charge",
    "material_parameters_digest": "d",
    "authority_ref": "a",
    "idempotency_strategy": "NONE"
  }],
  "attempts": [],
  "receipts": [
    {
      "receipt_id": "r1",
      "effect_id": "e1",
      "observed_status": "COMMITTED",
      "evidence_refs": ["ev1"],
      "sequence": 1
    },
    {
      "receipt_id": "r2",
      "effect_id": "e1",
      "observed_status": "NOT_COMMITTED",
      "evidence_refs": ["ev2"],
      "sequence": 2
    }
  ],
  "commitments": [],
  "decision_effect_id": "e1"
}
```

Reproducing the shipped validation/decision logic gives:

```text
errors = []
next_action = RETRY_SAME_INTENT
```

### Why this matters

This can transform “known committed external effect” into “safe to retry same intent.” For an irreversible or non-idempotent external effect, that is exactly the duplicate-effect hazard EL-R03 is meant to prevent.

The correct handling of a later receipt that conflicts with an already known terminal receipt should be conservative. Depending on the intended model, it should be rejected as inconsistent or require manual reconciliation; it must not silently erase the earlier committed occurrence truth.

### Required correction

Enforce monotonic/compatible terminal receipt semantics. Once `COMMITTED` or `COMPENSATED` is represented for an effect, later contradictory non-terminal settlement states must not downgrade it into a retry path. A conflicting later observation should produce `REJECT_INCONSISTENT_RECORD` or `MANUAL_RECONCILIATION` unless an explicit correction/supersession model is represented.

## 5. A-S-03 — Migrated source INTEGRATED history accepts impossible chronology

**Severity:** HIGH

### Evidence

For local `lifecycle_state == INTEGRATED`, `validate_evolution_record_v2.py` performs strong chronology/snapshot checks:

- requires an experiment at or before integration commit time;
- requires an evaluation at or before commit time;
- requires `selection_state_at_commit` to match the latest represented evaluation at/before commit;
- if present, reconciles `expression_state_at_commit` with expression history at/before commit.

For `migration.source_lifecycle_state == INTEGRATED`, `validate_transferred_source_history()` only requires:

- source experiments exist;
- source evaluations exist;
- source integration history exists;
- latest source integration result is `COMMITTED`;
- latest source evaluation matches current source selection and satisfies positive/negative outcome rules.

It does **not** apply the local-equivalent chronology and commit-snapshot checks.

### Constructed counterexample

Transferred source history:

```text
2026-01-01  integration result = COMMITTED
            selection_state_at_commit = UNKNOWN
2026-02-01  first represented experiment
2026-02-02  first represented evaluation = SUPPORTED / IMPROVED
current     source_lifecycle_state = INTEGRATED
            source_selection_state = SUPPORTED
```

Each item is schema-shaped, the current source selection matches the latest source evaluation, and the latest source integration is `COMMITTED`.

Reproducing `validate_transferred_source_history()` semantics produces no consistency error, even though the source was “committed” before any represented experiment or evaluation and the commit snapshot does not match the later evidence.

### Why this matters

The candidate documentation explicitly says migration transfers a possibility plus represented source history, not a conclusion, and that source and receiver results remain separate. That separation is good, but it does not justify accepting internally impossible source history while labeling it represented history.

Imported source context is used to accelerate differential validation. Chronology corruption can inflate confidence about what was known when integration occurred, even if receiver-local selection remains separate.

The validation asymmetry also means a history rejected when local can become accepted after being moved into the migration source-history namespace.

### Required correction

Apply the same relevant chronology/snapshot invariants to transferred source history, at least for source `INTEGRATED` records:

- source experiment at/before source commit;
- source evaluation at/before source commit;
- source `selection_state_at_commit` matches the source evaluation snapshot;
- source expression snapshot/history reconciliation when those fields are represented.

Migration should preserve source/local epistemic separation without weakening internal consistency.

## 6. A-S-04 — Exact final report self-hash requirement is internally unsatisfiable

**Severity:** PROCESS BLOCKER

`INTAKE-A-S.md` requires the SHA-256 of the exact final report bytes to be computed and then recorded in that same report.

That instruction is self-referential: inserting the digest changes the exact file bytes, which changes the digest. Recomputing and replacing it changes the bytes again.

The capsule manifest explicitly recognizes this exact class of problem for itself:

```text
manifest_self_hash = EXCLUDED_BY_DEFINITION
reason = A final manifest cannot recursively contain a stable hash of its own final bytes.
```

Therefore the report-seal instruction and the manifest's own hashing rationale disagree.

I will not write a knowingly false “exact file SHA-256” value into the report. The truthful seal is recorded externally in the returned response and a `.sha256` sidecar. This report itself records the reason the digest is not embedded.

### Required correction

Use one of these non-self-referential constructions:

- external `.sha256` sidecar over exact report bytes;
- signed envelope containing report digest;
- manifest that hashes the report but excludes its own hash by definition;
- explicitly defined normalization that excludes the seal field before hashing.

## 7. Additional observations that did not become findings

- The Effect Lifecycle reference correctly limits machine PASS to represented lifecycle consistency and does not claim external exactly-once.
- The Authority Lease reference explicitly acknowledges that external mandate authenticity and credential validity remain unproven.
- The evolution documentation correctly separates lifecycle, expression, and selection and states that migration does not transfer receiver-local conclusions.
- `MANIFEST-A-S.json` explicitly excludes author fixtures/selftests/regression results and declares AST-equivalent comment/docstring-free projections for selected tools; I did not treat absent excluded materials as defects.
- I did not infer universal applicability from optional reference machinery.

These boundaries are useful, but they do not cure the represented-state contradictions above.

## 8. Reproduction summary

Three independent counterexamples were constructed from the clean-room bytes:

| ID | Target | Result |
|---|---|---|
| `AUTH-REVOKED-SCOPE` | `tools/validate_contracts.py` authority composition | explicit revoked/out-of-scope represented grant -> no authority error -> composed `OK` |
| `EFF-TERMINAL-REGRESSION` | `validate_effect_lifecycle.py` | prior `COMMITTED`, later `NOT_COMMITTED` -> `errors=[]`, `RETRY_SAME_INTENT` |
| `MIG-SOURCE-CHRONOLOGY` | `validate_evolution_record_v2.py` transferred history | source COMMIT before source experiment/evaluation -> no source-history consistency error |

The local execution environment could not clone GitHub directly because outbound DNS/network access from the execution container was unavailable, so executable behavior was independently reconstructed from the clean-room source bytes exposed through the repository browser and exercised with minimal counterexamples. No excluded fixtures/oracles were used.

## 9. Final A-S disposition

A-S review is complete for the available clean-room surface.

**Disposition: NOT CLEARED.**

Blocking/high-priority fixes are required for:

1. composed authority semantics;
2. terminal effect receipt monotonicity/conflict handling;
3. migrated source-history chronology/snapshot parity.

The A-S sealing protocol should also be corrected to use an external or explicitly normalized digest construction.

No A-P review was performed. No Phase B work was performed.

## 10. Content seal recording note

Per A-S-04, the SHA-256 of the exact bytes of this file is intentionally **not embedded inside this file**, because doing so would invalidate the claimed exact-file digest. The exact digest is returned externally with this report and in the sibling `.sha256` sidecar.

STOP.
