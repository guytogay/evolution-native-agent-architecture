# Authority Grant / Lease reference prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #91 Reconstruction B, #92 Reconstruction C, #89, PR #82, Effect Lifecycle.

## WHAT

Turn ENA's existing authority property into a small executable reference organ for a single question:

> Does this represented grant authorize this grantee to perform this action on this protected subject, for this task, on this Host/epoch, at this evaluation time?

This prototype does **not** redefine authority. It operationalizes the existing Current separation:

`IDENTITY != SUBJECT CONTROL != CAPABILITY/POSSESSION != AUTHORITY != CREDENTIAL VALIDITY != MANDATE HORIZON`

and the existing property that authority remains bound to the subject/effect/task/purpose/source that justifies it.

## WHY

Two opposite failure modes matter:

```text
credential/capability/history exists
-> Agent narrates current authority
-> mandate was expired/revoked/out-of-scope
```

and:

```text
harmless local/non-authority-bearing action
-> Agent assumes every change requires a formal external grant
-> unnecessary permission seeking / authority anxiety
```

Effect Lifecycle already carries `authority_ref`, but intentionally does not determine whether that authority is currently valid. Therefore:

`EFFECT_RECORD_VALID + authority_ref present != AUTHORITY_CURRENTLY_RESOLVED`

## HOW — this prototype

Files:

- `authority-lease.v0.1.json` — compact reference contract and decision rules;
- `fixtures/authority-lease-cases.jsonl` — positive, negative, uncertainty, renewal, and false-BLOCK controls;
- `tools/validate_authority_lease.py` — stdlib validator/resolver;
- `tools/selftest_authority_lease.py` — targeted regression + Effect Lifecycle seam test.

A grant binds, where represented, to:

- `grantee`;
- allowed action(s);
- protected subject scope;
- task scope;
- Host scope;
- grantee epoch scope;
- optional credential identity binding;
- `valid_from` / `expires_at`;
- revocation time;
- explicit source reference.

Scope breadth is explicit. `*` is an explicit broad scope; omission is not silently treated as universal authority.

## Resolution vocabulary

- `NOT_REQUIRED` — caller says this action is not authority-bearing; no lease is manufactured merely for ceremony.
- `AUTHORIZED` — the represented grant matches the represented query at the evaluation time.
- `NOT_AUTHORIZED` — a represented grant exists but is expired, revoked, not-yet-valid, or out of represented scope.
- `UNRESOLVED` — authority is required but the referenced grant is absent/unresolvable.
- `INVALID_RECORD` — represented grant/query structure is internally inconsistent.

These states are protocol semantics for this reference organ, not a claim that all Hosts must persist the same enum.

## Renewal / succession discipline

Renewal creates a new grant identity. A new grant may point to `supersedes_grant_ref`, but the resolver does not silently infer that the newest grant should authorize an action.

The execution query must name the grant it relies on.

This prevents:

```text
old authority expired
+ newer grant exists somewhere
-> old authority magically becomes valid again
```

and avoids wall-clock/latest authority inference.

## Restore / fork / migration discipline

A grant may explicitly span or restrict Host and grantee epoch. Copying the grant record into a clone/fork does not change those bindings.

An explicit `*` may represent a deliberately cross-Host/cross-epoch grant when the real mandate supports that breadth. The reference organ does not assume such breadth by default.

## Credential boundary

A grant may bind to a `credential_ref`, and a query relying on that grant must present the same represented credential identity.

This is **identity binding only**:

`credential_ref matches != credential externally valid`

Credential validity remains a separate property/evidence question.

## Effect Lifecycle composition seam

Effect Lifecycle answers whether an effect/attempt/receipt/commitment record is internally coherent. Authority Lease answers whether the referenced external authority is currently resolved for that effect context.

For consequential execution:

```text
Effect Lifecycle consistency
+
Authority Lease resolution
-> stronger execution precondition
```

Neither component is allowed to inherit the other's evidence maturity.

## Evidence boundary

This prototype validates represented grant/query relations only.

It does **not** establish:

- that `source_ref` is authentic or currently legitimate in the external world;
- that a credential is cryptographically valid merely because its reference matches;
- that the caller correctly classified `authority_required = false`;
- that every effect-equivalent path has the same authority boundary;
- that external policy has not changed outside the represented record.

`GRANT_REPRESENTED != EXTERNAL_MANDATE_TRUE`

`AUTHORIZED_BY_REPRESENTED_LEASE != WORLD_POLICY_CERTIFIED`

`NOT_REQUIRED_CLASSIFICATION != SELF_PROVING`

`CURRENT_CHANGE = NO`
