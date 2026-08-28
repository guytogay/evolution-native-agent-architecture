# Incident — candidate.2 GitHub natural-navigation priming

Date: 2026-08-28

Status: `VALIDATION_INTERFACE_DEFECT / A-S_ABORTED / NOT_SEALED / CANDIDATE_UNCHANGED / CARRIER_REPAIRED_R3`

## Trigger

A genuinely fresh candidate.2 reviewer followed the Issue #137 boundary and began A-S against `validation/v037-c2-blind-semantic-primary`.

Before an A-S seal existed, normal GitHub directory navigation automatically rendered the candidate root `README.md`. That rendered content included an author-status/confidence header the blind-view manifest explicitly marked as withheld until after A-S.

The reviewer correctly stopped and reported:

`A_S_ABORTED_BOUNDARY_CROSSING / VALIDATION_INTERFACE_DEFECT / NOT_SEALED / A_P_NOT_STARTED`

No Phase B occurred. No candidate or Current byte changed. The report is interface-defect occurrence truth only, not an A-S seal or candidate verdict.

## Why this is a method/interface defect

The prior view treated ranged-read/path-avoidance instructions as sufficient. They are not sufficient when the carrier UI can reveal withheld content through normal navigation or repository-wide search.

```text
PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY
PROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY
DECLARED_WITHHOLDING != PHYSICAL_WITHHOLDING
```

A reviewer should not need perfect navigation discipline merely to preserve the epistemic property the validation method claims to provide.

## Wider audit

Follow-up surface audit found that the problem was broader than the candidate root README:

- repository-level `.github/`, `research/`, historical reconciliation and other branches remained reachable/searchable from the same repository UI;
- candidate-local current/status documents could reveal author machine-check or predecessor review narrative;
- some implementation files contained historical PR/falsifier/false-claim commentary even when their executable semantics were legitimate A-S material.

Therefore deleting one README or adding more path warnings would not solve the carrier problem.

## First r3 detector correction

The first isolated-capsule gate overreached and classified ordinary semantic text such as `False BLOCK` as priming. That is not acceptable: the object's own failure vocabulary is part of what a fresh validator must inspect.

```text
SEMANTIC_FAILURE_VOCABULARY != AUTHOR_ATTACK_MAP
```

The detector was narrowed to history-specific signals such as predecessor identity, PR/falsifier lineage, repair/probe naming, expected-result material, author-side confidence/evidence and concrete historical workflow IDs.

## Manifest self-hash correction

A later self-audit found an interface false-confidence bug in the initial r3 manifest inventory: the manifest listed a hash of itself that had been computed before the final manifest rewrite. A final manifest cannot recursively contain a stable hash of its own final bytes.

The final integrity rule is:

```text
MANIFEST_SELF_HASH = EXCLUDED_BY_DEFINITION
PAYLOAD_FILE_HASHES = SHA256_VERIFIED
OUTER_CAPSULE_HASH = SHA256_VERIFIED
```

The manifest inventories every other payload and the outer ZIP digest binds the final manifest bytes.

## Final repair

Use a physically isolated review carrier rather than the project repository UI for A-S:

```text
FROZEN_CANDIDATE
-> REPRODUCIBLE SEMANTIC CAPSULE BUILD
-> PHYSICALLY ISOLATED A-S CAPSULE
-> CONTENT-HASHED A-S REPORT SEAL
-> SEPARATELY DELIVERED A-P SUPPLEMENT
```

The A-S capsule may use declared semantic-preserving projections when exact files are mixed-role and expose author search maps. Such projection must be mechanically auditable against the frozen bytes; it is validation interface material, not candidate mutation.

The A-P supplement contains the exact frozen candidate package but remains physically unavailable until the A-S report content is sealed.

## Final mechanical evidence

Authoritative gate:

- workflow `.github/workflows/v037-candidate2-r3-capsule-build.yml`
- run `33131773164` — SUCCESS

Observed checks:

- A-S physical isolation PASS;
- A-S payload inventory PASS;
- A-P exact frozen candidate package PASS;
- A-P payload inventory PASS;
- repeated deterministic build PASS;
- `ATTACK_CARDINALITY = OPEN`.

Final carrier SHA-256:

- A-S `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- A-P `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

Earlier r3 build run `33131665994` and hashes `ee80ac...` / `b3e222...` are superseded because they predate the manifest inventory correction.

## Candidate identity impact

None.

Frozen candidate.2 remains:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- candidate subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`
- Current subtree at that source `7dcbb3934883ffa6cc5292a662588cafc1533cff`

This incident does not establish a candidate-byte defect and does not require candidate.3.

## Occurrence truth

The aborted reviewer report is evidence of the interface defect only. It is not an A-S seal and must never be counted as candidate.2 independent semantic validation.

Issue #137 and its same-repository branch are superseded as fresh A-S carrier surfaces.
