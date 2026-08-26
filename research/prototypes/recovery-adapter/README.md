# Recovery Adapter reference prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #91 Reconstruction B, #89, PR #82, Effect Lifecycle, Authority Grant / Lease.

## WHAT

Provide a small Host-facing reference organ for two separate decisions:

1. Is there a represented recovery path that is sufficiently reachable/tested to attempt restore?
2. After state restore succeeds, are the represented world-state and authority dependencies sufficiently reconciled to resume consequential work?

This prototype operationalizes existing Current properties rather than introducing a new recovery philosophy.

## WHY

Several false equivalences recur in Agent recovery:

```text
checkpoint exists != recovery proven
backup readable by healthy Agent != rescue reachable when Agent is broken
state restore success != external world rollback
old authority record exists != authority remains current
```

A snapshot can restore `payment pending` after the payment already committed. A clone can restore credentials/configuration while the mandate expired. A recovery controller can exist but share the exact failure domain of the candidate it is supposed to rescue.

## HOW — this prototype

Files:

- `recovery-adapter.v0.1.json` — compact reference contract and decision rules;
- `fixtures/recovery-adapter-cases.jsonl` — recovery-path, uncertainty, post-restore, and false-BLOCK controls;
- `tools/validate_recovery_adapter.py` — stdlib validator/resolver;
- `tools/selftest_recovery_adapter.py` — targeted regressions plus Effect Lifecycle + Authority Lease composition test.

The adapter represents:

- protected recovery subject;
- candidate/control/rescue failure-domain identities;
- whether independent rescue is actually required for this bounded case;
- represented rescue-independence status/evidence;
- recovery locator and access path;
- checkpoint reference;
- reachability status/evidence;
- whether a restore drill is required, and its status/evidence;
- actual restore result/evidence;
- post-restore world reconciliation summary;
- post-restore authority resolution summary.

It does **not** reimplement detailed effect settlement or authority validation. It consumes their bounded outputs/references.

## Reference decision vocabulary

The reference resolver emits one primary action plus diagnostic blockers:

- `ATTEMPT_RESTORE`
- `RESUME`
- `DO_NOT_RESUME`
- `REPAIR_RECOVERY_PATH`
- `RESOLVE_RECOVERY_UNCERTAINTY`
- `REJECT_INCONSISTENT_RECORD`

The blocker list is open-cardinality; the current list is not an ontology-size claim.

## Independent rescue is conditional

A material self-disabling mutation may require a rescue path outside the candidate's failure domain. A disposable local cache may not.

Therefore the adapter has an explicit `independent_rescue_required` input.

```text
independent rescue can be necessary
!= every recovery requires a separate rescue plane
```

If independence is required:

- represented `SHARED_FATE` is a known recovery-path defect;
- `UNKNOWN` remains uncertainty;
- `INDEPENDENT` requires represented evidence refs.

The caller's decision that independence is or is not required remains a trust boundary; this prototype does not self-prove consequence classification.

## Restore drill is conditional

Likewise, `restore_drill.required` is explicit. A high-consequence recovery path may need recent drill evidence; a cheap local recovery need not inherit that ceremony.

`drill not universally required != backup existence proves recovery`

## Post-restore composition

When `restore.status = SUCCESS`, the adapter requires an explicit post-restore summary.

World state:

- `NOT_REQUIRED`
- `CLEARED`
- `ACTION_REQUIRED`
- `UNRESOLVED`

Authority state:

- `NOT_REQUIRED`
- `AUTHORIZED`
- `NOT_AUTHORIZED`
- `UNRESOLVED`

These are adapter-facing summaries, not replacements for their source organs.

A restored Agent may resume only when represented world state is `NOT_REQUIRED | CLEARED` and represented authority is `NOT_REQUIRED | AUTHORIZED`.

`RESTORE_SUCCESS + WORLD_ACTION_REQUIRED -> DO_NOT_RESUME`

`RESTORE_SUCCESS + AUTHORITY_NOT_AUTHORIZED -> DO_NOT_RESUME`

## Composition with existing organs

Effect Lifecycle can provide a world-settlement posture after restart/restore:

```text
SETTLE_COMMITMENT / QUERY_SETTLEMENT / MANUAL_RECONCILIATION
-> world reconciliation remains ACTION_REQUIRED or UNRESOLVED

NO_EFFECT_NEEDED
-> may support world CLEARED for the represented effect scope
```

Authority Lease can provide:

```text
AUTHORIZED | NOT_AUTHORIZED | UNRESOLVED | NOT_REQUIRED
```

The Recovery Adapter consumes those results; it must not upgrade their evidence maturity.

## Evidence boundary

This prototype validates represented recovery relations only. It does not establish:

- that a recovery locator actually exists outside represented evidence;
- that failure-domain labels are externally correct;
- that evidence refs are authentic merely because they are present;
- that the caller correctly classified `independent_rescue_required` or `restore_drill.required`;
- that `world_state = CLEARED` is externally true without the referenced settlement organ/evidence;
- that `authority_state = AUTHORIZED` is externally legitimate without the referenced authority organ/evidence;
- that all effect-equivalent execution paths are covered.

`RECOVERY_ADAPTER_PASS != RECOVERY_DRILL_EXECUTED`

`RESTORE_SUCCESS != SAFE_RESUME`

`CURRENT_CHANGE = NO`
