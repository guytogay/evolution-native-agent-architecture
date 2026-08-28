# Candidate.2 blind-carrier leak incident

Status: `VALIDATION_INTERFACE_INCIDENT / A-S_ABORTED / NO_CANDIDATE_VERDICT / METHOD_REPAIRED`

Date: 2026-08-28

Target:
- identity: `v0.3.7-candidate.2`
- frozen source: `bda470e0a6b170cec61225a905957a501454a2fe`
- candidate subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

## Occurrence

Fresh intake Issue #137 instructed a genuinely fresh reviewer to begin from `validation/v037-c2-blind-semantic-primary`, read only the neutral entry/manifest, perform A-S, persist/seal it, then open A-P.

Before substantive A-S, the reviewer opened the candidate directory page in GitHub to enumerate retained paths. GitHub automatically rendered `README.md` under the directory listing. The rendered content exposed README source lines 1-8, which the blind-view manifest explicitly withheld as `AUTHOR_STATUS_AND_CONFIDENCE_HEADER` until after A-S seal.

The reviewer obeyed the declared stop condition and produced:

`A_S_ABORTED_BOUNDARY_CROSSING / VALIDATION_INTERFACE_DEFECT / NOT_SEALED / A_P_NOT_STARTED`

Report occurrence path:

`collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary.md`

This report is interface-defect occurrence truth. It is **not** an A-S seal and contains no candidate correctness verdict.

## Root cause

The boundary was represented procedurally rather than enforced by the review carrier.

```text
MANIFEST SAYS DO NOT READ RANGE
+
UI AUTOMATICALLY RENDERS RANGE
-> BOUNDARY FAILURE
```

Further r2 audits showed the problem was broader than the root README:

- same-repository natural navigation can reach `.github/`, `research/`, reconciliation and other branches;
- candidate-local files may embed predecessor/repair/status/oracle priors;
- implementation comments/docstrings may contain old PR/falsifier/false-claim search maps;
- repository search can escape a nominal blind branch.

Therefore:

```text
PROCEDURAL_RANGED_READ != INFORMATION_BOUNDARY
PROCEDURAL_PATH_AVOIDANCE != INFORMATION_BOUNDARY
CANDIDATE_LOCAL != AUTOMATICALLY_BLIND_SAFE
```

## Repair evolution

### r2

The first repair physically removed obvious auto-rendered root mixed-role files and created declared projections for mixed-role implementation surfaces. Byte audit passed, but broader surface audit found additional author-shaped priming inside the same repository/candidate surface.

### r3

The review interface was changed from a same-repository blind branch to two physically isolated deterministic carriers:

- A-S capsule: behavior-bearing semantic/implementation surface with author history/oracle/project-manager material physically absent;
- A-P supplement: exact frozen candidate package, supplied only after A-S content seal.

Implementation comments/docstrings may be removed through mechanically checked AST-equivalent projections where those comments themselves contain author attack history.

A-S seal may be an immutable commit or, when the fresh environment lacks GitHub write access, SHA-256 of exact report bytes recorded before A-P is supplied.

## Detector correction

The first r3 gate incorrectly treated ordinary semantic wording `False BLOCK` as author priming. That failure was retained as method evidence and the detector was corrected.

```text
SEMANTIC FAILURE VOCABULARY != AUTHOR ATTACK MAP
```

Blindness must remove prior search-map information without deleting the semantic vocabulary the reviewer is supposed to falsify.

## Manifest correction

A subsequent self-audit found that the initial manifest inventory included a hash of the manifest before its final rewrite. This produced an impossible recursive self-hash claim.

The final rule is:

```text
MANIFEST_SELF_HASH = EXCLUDED_BY_DEFINITION
PAYLOAD_FILE_HASHES = SHA256_VERIFIED
OUTER_CAPSULE_HASH = SHA256_VERIFIED
```

## Final mechanical evidence

Final authoritative carrier gate:
- workflow: `.github/workflows/v037-candidate2-r3-capsule-build.yml`
- run: `33131773164`
- result: PASS

Observed checks:
- A-S physical isolation: PASS
- A-S payload inventory: PASS
- A-P exact frozen candidate package: PASS
- A-P payload inventory: PASS
- repeated deterministic build: PASS
- attack cardinality: OPEN

Final inner carrier hashes:
- A-S: `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- A-P: `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

## Consequence

Issue #137's same-repository intake path is superseded and must not be reused for fresh A-S.

No candidate.2 bytes changed. `releases/current/` did not change. Candidate.2 remains frozen, not Current and not released. Any material candidate correction still requires candidate.3.
