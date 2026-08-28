# v0.3.7 candidate.2 — isolated independent-review carrier r3 reconciliation

Status: `VALIDATION_INTERFACE_REPAIRED / ISOLATED_A-S_CARRIER_READY / A-P_WITHHELD_UNTIL_A-S_SEAL / NOT_CURRENT / NOT_RELEASED`

## Frozen target

- identity: `v0.3.7-candidate.2`
- source: `bda470e0a6b170cec61225a905957a501454a2fe`
- candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current remains: `v0.3.6 / CURRENT / FIELD_VALIDATION`

Candidate.2 bytes were not changed by this work.

## Superseded intake occurrence

Issue #137 / `validation/v037-c2-blind-semantic-primary` produced a validation-interface abort before A-S seal because GitHub auto-rendered a withheld README header during ordinary directory navigation.

Occurrence report:

`collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary.md`

Disposition:

`A_S_ABORTED_BOUNDARY_CROSSING / VALIDATION_INTERFACE_DEFECT / NOT_SEALED / A_P_NOT_STARTED`

This is not a candidate verdict and not an A-S seal.

## r3 carrier architecture

A-S and A-P are now separate physically isolated deterministic ZIP carriers.

A-S contains only the declared independent semantic/implementation review surface. Project-manager context, author history/oracles, Current, historical releases, predecessor-specific regression material and other declared priming surfaces are absent.

Where an implementation file is mixed-role, the carrier may use a mechanically checked derived projection, including AST-equivalent Python with comments/docstrings removed. These are validation-interface projections, not candidate changes.

A-P contains the exact frozen candidate package byte-for-byte, plus A-P intake/manifest metadata outside the candidate directory. It is not supplied until A-S report bytes are content-sealed.

## Final authoritative gate

Workflow:
`.github/workflows/v037-candidate2-r3-capsule-build.yml`

Run:
`33131773164`

Result:
`PASS`

Run established:
- `A_S_PRIMING_DETECTOR=HISTORY_SPECIFIC`
- `SEMANTIC_FAILURE_VOCABULARY_NE_AUTHOR_ATTACK_MAP`
- `A_S_PHYSICAL_ISOLATION=PASS`
- `A_S_PAYLOAD_INVENTORY=PASS`
- `A_P_EXACT_FROZEN_PACKAGE=PASS`
- `A_P_PAYLOAD_INVENTORY=PASS`
- `MANIFEST_SELF_HASH_POLICY=EXCLUDED_BY_DEFINITION`
- `PAYLOAD_INVENTORY_HASH_VERIFICATION=PASS`
- `CAPSULE_DETERMINISM=PASS`
- `attack_cardinality=OPEN`

Final carrier SHA-256:
- `candidate2-as-capsule-r3.zip`: `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- `candidate2-ap-supplement-r3.zip`: `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

A-S manifest tracks 78 non-self payloads. A-P manifest tracks 119 non-self payloads. Manifest self-hash is explicitly excluded because a final document cannot recursively contain a stable digest of its own final bytes. The outer ZIP digest binds the manifest bytes themselves.

## Fresh-review sequence now authorized

```text
FRESH REVIEWER
-> RECEIVE ONLY A-S ZIP
-> READ INTAKE-A-S.md
-> PERFORM INDEPENDENT A-S
-> WRITE candidate2-independent-a-s-primary-r3.md
-> COMPUTE + RECORD SHA-256 OF EXACT REPORT BYTES
-> STOP

SAME REVIEWER STATE
-> ONLY THEN RECEIVE A-P ZIP
-> VERIFY/RECORD A-S DIGEST
-> READ INTAKE-A-P.md
-> PERFORM A-P
-> WRITE candidate2-independent-a-p-primary-r3.md
-> STOP BEFORE PHASE B

PROJECT MANAGER
-> VERIFY CARRIER HASHES + A-S REPORT DIGEST + SEQUENCE
-> PERSIST INDEPENDENT OCCURRENCE TRUTH
-> ONLY THEN PHASE B RECONCILIATION
```

Before A-S seal, do not use the project repository/Issue #137/validation branch as the fresh review surface and do not provide the A-P supplement.

## Authority boundary

This record authorizes a validation-interface replacement only. It does not:
- declare candidate.2 correct;
- create an A-S seal;
- perform A-P;
- perform Phase B;
- promote candidate.2;
- modify Current;
- close attack cardinality.

Next action:
`GET_GENUINELY_FRESH_REVIEWER_TO_RUN_ISOLATED_CANDIDATE2_A-S_R3`
