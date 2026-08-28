# v0.3.7 candidate.2 — reusable clean-room carrier transition

Date: 2026-08-28

Status: `VALIDATION_INTERFACE_SIMPLIFIED / DEDICATED_CLEAN_ROOM_A_S_READY / A_P_WITHHELD / CANDIDATE_UNCHANGED / CURRENT_UNCHANGED`

## Why this transition exists

The physically isolated r3 ZIP carrier solved the candidate.2 repository-navigation priming defect, but ZIP is a transport HOW rather than the governing method.

The user provisioned a reusable dedicated repository:

`guytogay/independent-validation-cleanroom`

The project now uses that repository as the reviewer-facing clean room for candidate.2 A-S. The deterministic r3 capsule remains construction/integrity evidence and a reproducible source for the projected A-S material.

```text
PHYSICALLY_ISOLATED_CARRIER != ZIP
TRANSPORT_FORMAT != METHOD
```

## Reusable clean-room model

The repository identity is reusable validation infrastructure. Its contents are disposable stage state.

```text
CLEAN_ROOM_REPOSITORY_IDENTITY = REUSABLE
CLEAN_ROOM_STAGE_CONTENT = REPLACEABLE
```

After a validation occurrence finishes, durable findings/seals/reconciliation return to the source project. The clean room may then be reset for a new ENA candidate or an unrelated future project.

Historical project context should not accumulate in the clean room by default.

## Candidate.2 A-S state installed

Repository:

`https://github.com/guytogay/independent-validation-cleanroom`

Default branch:

`main`

Current A-S stage commit:

`28dde50c9caaeee3b5c269e28a7be5f07ac29ae5`

Tree:

`42debebed620bd05e6e2635409057f20b57bfa9e`

Commit parents:

`[]`

The parentless commit matters because the normal clean-room branch history does not expose the bootstrap/import process or previous review stages.

Current root surface contains only:

- `README.md`
- `INTAKE-A-S.md`
- `MANIFEST-A-S.json`
- `releases/`

The current state does not contain:

- `.github/`
- `research/`
- `collaboration/`
- `releases/current/`
- source-project handoff/reconciliation/history
- A-P material

## Construction binding

Candidate.2 frozen identity remains:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- candidate subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current subtree at the same source `7dcbb3934883ffa6cc5292a662588cafc1533cff`

The clean-room A-S tree was reconstructed from the final audited r3 A-S package.

Construction evidence remains:

- capsule audit run `33131773164` — SUCCESS
- A-S ZIP SHA-256 `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- A-P ZIP SHA-256 `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

Those ZIP identities are evidence for the construction path, not a requirement that the reviewer consume a ZIP.

## Fresh-review sequence

A genuinely fresh candidate.2 reviewer now receives only the clean-room repository/commit and the instruction to start at the root intake.

Before A-S seal, do not additionally supply:

- the ENA source repository URL as review context;
- Issue #137 or its validation branch;
- project-manager handoff/reconciliation;
- predecessor findings/repair history;
- the A-P supplement.

The reviewer may freely browse/search/execute the clean-room repository because the review surface itself is intended to enforce the A-S information boundary.

A-S output sequence:

```text
CLEAN_ROOM A-S
-> COMPLETE REPORT
-> SHA256(EXACT REPORT BYTES)
-> RECORD DIGEST
-> STOP
```

Only after the project manager verifies/persists that seal may the same reviewer receive A-P material.

## A-P transition

The clean room may be reset/replaced for A-P or A-P may be delivered through another physically controlled carrier. The invariant is not the mechanism; it is that A-P was unreachable through the A-S review surface before the A-S seal existed.

A-P must contain the exact frozen candidate package and the reviewer stops before project-manager Phase B.

## Authority boundary

This transition:

- changes only the validation interface HOW;
- does not modify candidate.2 bytes;
- does not modify Current;
- does not create an A-S seal;
- does not perform A-P;
- does not perform Phase B;
- does not authorize promotion;
- does not close attack cardinality.

Next action:

`GET_GENUINELY_FRESH_REVIEWER_TO_RUN_CANDIDATE2_A_S_IN_DEDICATED_CLEAN_ROOM`
