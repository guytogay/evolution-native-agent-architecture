# Candidate.2 clean-room wrapper identity correction and A-P stage transition

Status: `VALIDATION_INTERFACE_CORRECTION / A_P_STAGE_READY / NO_CANDIDATE_MUTATION / NO_CURRENT_MUTATION`

## Trigger

While preparing the separately exposed candidate.2 A-P stage after the fresh A-S report had been content-sealed and merged to `main`, the clean-room bootstrap gate rejected the previously recorded A-S wrapper commit SHA.

The rejected value was:

`28dde50c9caaeee3b5cfabf51410083dbbb05a93`

Direct GitHub readback established that this value is not the actual clean-room A-S commit.

## Actual A-S wrapper identity

The actual candidate.2 A-S clean-room commit is:

`28dde50c9caaeee3b5c269e28a7be5f07ac29ae5`

It is parentless and has tree:

`42debebed620bd05e6e2635409057f20b57bfa9e`

The tree SHA is exactly the A-S tree that the project had already recorded before the wrapper-SHA correction.

Therefore:

```text
RECORDED_A_S_WRAPPER_COMMIT = WRONG
RECORDED_A_S_TREE = CORRECT
ACTUAL_A_S_COMMIT = PARENTLESS
ACTUAL_A_S_COMMIT_TREE = RECORDED_A_S_TREE
REVIEWED_FILE_SURFACE_CHANGED_BY_CORRECTION = FALSE
```

## Independent-review disposition

The fresh A-S reviewer had already recorded in its own report that the requested wrapper commit SHA could not be resolved and that it therefore reviewed the current clean-room bytes only, without substituting the source project repository or external project history.

The exact report remains immutable occurrence truth:

`collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary-r3.md`

Its exact content seal remains:

`0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`

The wrapper-identity correction does not change those report bytes, the reviewed A-S tree, or the fresh-review information boundary.

This is classified as a project validation-interface/control-plane identity defect, not a candidate-byte defect and not reviewer noncompliance.

## A-P stage construction

After correcting the bootstrap binding, the dedicated clean-room repository was rewritten to a new parentless A-P stage:

- repository: `guytogay/independent-validation-cleanroom`
- branch: `main`
- A-P commit: `aea2ed25107145a557b3fe46ca0e4b90e2b90fa9`
- A-P tree: `08ac16303d69a6a268197ac26b23c5b20972b727`
- commit parents: `[]`
- exact frozen candidate subtree under `releases/v0.3.7-candidate/`: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

The A-P root contains only:

- `README.md`
- `INTAKE-A-P.md`
- `MANIFEST-A-P.json`
- `releases/`

The package subtree equals the exact frozen candidate.2 subtree. No `.github`, A-S intake/manifest, ENA project control-plane, Phase-B analysis, or candidate repair material is present in the final A-P stage.

## Sequence

```text
A-S SEALED + PERSISTED
-> WRAPPER IDENTITY CORRECTED WITHOUT CHANGING A-S TREE
-> SEPARATE PARENTLESS A-P STAGE CREATED
-> SAME FRESH REVIEWER MAY CONTINUE A-P
-> REVIEWER STOPS
-> PROJECT MANAGER PHASE B
```

Candidate.2 remains frozen at source `bda470e0a6b170cec61225a905957a501454a2fe` / subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`.

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.

`ATTACK_CARDINALITY = OPEN`
