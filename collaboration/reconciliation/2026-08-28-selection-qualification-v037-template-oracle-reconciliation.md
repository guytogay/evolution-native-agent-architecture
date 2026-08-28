# Selection Qualification — v0.3.7 template-composition oracle reconciliation

Status: `ORACLE_DRIFT_CONFIRMED / CURRENT_PACKAGE_DEFECT_NOT_DEMONSTRATED / CONTROL_REPAIR_REQUIRED`

Date: 2026-08-28

## Trigger occurrence

Release PR #144 at exact head `67d7c1c71ca969f6215702f38b689c572a865102` triggered `Selection Qualification Research` run `33160523281`.

The prototype's authored 16-case Selection Qualification corpus passed, but Current-composition control #81 failed because `make_supported_current_record()` loaded `releases/current/templates/evolution-record.v2.json` and treated the shipped template as an instantiated record without replacing its `created_at` placeholder.

Observed failure:

`consistency: created_at has invalid date-time 'REPLACE_WITH_RFC3339_TIMESTAMP'`

## Classification

`ORACLE / COMPOSITION-CONTROL DRIFT`

Not demonstrated:

- a v0.3.7 release-package semantic defect;
- a regression in Selection Qualification resolution;
- a reason to weaken the v0.3.7 `created_at` validator;
- a reason to make the shipped template placeholder machine-valid.

The predecessor repair lineage already established the opposite boundary. Candidate.0 fresh Phase A found that the shipped v2 template used a non-time placeholder while selftest treated it as a machine-valid record. Candidate.1 Phase B classified that as a shared blind spot and repaired it by making an uninstantiated template timestamp invalid while keeping helper-instantiated records valid. See `collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md`.

Therefore changing the release template or validator to satisfy the stale Selection Qualification control would reintroduce a previously repaired defect.

## Repair

The Selection Qualification Current-composition control now explicitly instantiates `created_at` with a timezone-aware RFC3339 timestamp before testing the property it actually owns:

- evidence-backed `SUPPORTED` / `HARMFUL` records with `environment={}` remain structurally reachable;
- Selection Qualification still narrows scope-free positive or negative verdicts to `UNQUALIFIED_SELECTION`;
- direct/referenced scope and explicit unknown remain preserved;
- template placeholder validity is explicitly outside this prototype's composition-control scope.

The workflow verification boundary is updated accordingly.

## Evidence boundary

This oracle repair does not modify ENA Current semantics or candidate/release bytes. It only prevents an unrelated template-instantiation precondition from masquerading as Selection Qualification reachability evidence.

`TEMPLATE != INSTANTIATED_RECORD`

`ORACLE_FAILURE != CANDIDATE_DEFECT`

`CURRENT_CHANGE = NO`

## Release consequence

PR #144 should be re-evaluated only after this control repair is merged into `main` and the release branch is resynchronized to that exact main control-plane checkpoint. The release PR's exact reviewed head must then rerun all relevant checks.
