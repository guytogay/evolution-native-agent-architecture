# ENA v0.3.7 candidate.3 — Release Hardening Reconciliation

Date: 2026-08-28

Status: `RELEASE_HARDENING_PASS / NO_MATERIAL_FROZEN_BYTE_DEFECT / CANDIDATE_SUCCESSION_STOP_REAFFIRMED / RELEASE_PACKAGING_PERMITTED / NOT_YET_CURRENT / NOT_YET_RELEASED`

## Bound frozen occurrence

- candidate: `v0.3.7-candidate.3`
- frozen source: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen candidate subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- predecessor Current subtree on frozen source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze run: `33150269264 / SUCCESS`
- targeted post-freeze run: `33150553992 / SUCCESS`
- hardening run: `33152201566 / SUCCESS`

The Release Hardening Audit is a project-manager release-engineering audit. It is **not** relabeled as fresh independent A-S/A-P.

## Why this audit existed

The candidate.2 fresh independent cycle paid material epistemic rent, but candidate.3 was a bounded successor. Before release packaging, one extra audit was justified to test practical release risks not identical to predecessor semantic falsification:

1. can an adopter traverse the package without research history;
2. is v0.3.6 -> candidate.3 compatibility explainable rather than silently broken;
3. is candidate -> Current identity projection auditable;
4. do important residual/evidence boundaries remain visible rather than disappearing behind release confidence.

This audit had an explicit stop rule:

`MATERIAL_FROZEN_CANDIDATE_BYTE_DEFECT -> CANDIDATE.4`

Everything else is classified as release packaging, visible residual/field evidence, intentional relocation, or audit-oracle correction.

## Hardening observations

### 1. Adopter traversal

PASS.

The candidate exposes and resolves the adopter/core surfaces and the machine-declared operational path:

`README / 00-READ-ME-FIRST / RUNTIME-ADOPTION-KERNEL -> operational/README -> CUE-INDEX -> HOW-MAP -> REFERENCE-INDEX.yaml -> selected procedure/pattern/reference`

All baseline-bound Operational Architecture paths resolve. Relative Markdown navigation produced `0` broken candidate-local links.

The first hardening attempt had incorrectly guessed nonexistent filenames (`operational/OPERATIONAL-ARCHITECTURE.md`, `operational/REFERENCE-INDEX.md`) and incorrectly expected the candidate baseline 3.1 to retain Current's `core_files` list. Those were audit-oracle defects, not candidate defects; the audit was corrected to use the candidate's actual declared entrypoint fields.

### 2. v0.3.6 -> candidate.3 compatibility inventory

Observed package inventory:

- Current files: `55`
- candidate.3 files: `118`
- same-path exact-byte identical: `28`
- same-path modified: `23`
- added: `67`
- removed from former top-level path: `4`

The four apparent removals are explainable:

1. `CURRENT-BASELINE.yaml` -> candidate development baseline `CANDIDATE-BASELINE.yaml`;
2. `tools/ena_evolve.py` -> `tools/legacy/ena_evolve_v1_2.py` with **exact byte preservation**;
3. `tools/candidate1_adversarial.py` -> `tools/legacy/candidate1_adversarial_v1_2.py`;
4. `tools/candidate2_adversarial.py` -> `tools/legacy/candidate2_adversarial_v1_2.py`.

The two adversarial harness relocations intentionally changed only release-boundary narration/import path/module label/output label needed to point at the explicit legacy v1.2 tool. An observation run (`33152008655`) showed the exact diffs and executed both relocated probes successfully. Their probe logic remains equivalent after normalizing those relocation-only strings.

No unexplained v0.3.6 file removal remained after classification.

All v0.3.6 core adopter paths remain present. Both inherited v1 schemas remain present. The Constitution ID set remains exactly the same `38` IDs.

Executable compatibility was replayed again on the frozen target:

- inherited composed-validator corpus: `164/164`, zero flips required;
- successor closure corpus: `61/61`;
- evolution-record v2 selftest: `35` PASS;
- Authority Lease reference fixtures: PASS;
- Effect Lifecycle reference fixtures: PASS.

The generated regression result was compared byte-for-byte with its checked-in pre-run copy rather than treating a normal rewrite as a dirty-worktree defect.

### 3. Candidate -> Current release projection readiness

PASS WITH REQUIRED RELEASE TRANSFORM.

Frozen candidate.3 uses the external-record freeze model. Its immutable tested bytes intentionally retain pre-freeze candidate self-description such as `WORKING_CANDIDATE / NOT_CURRENT / NOT_FROZEN / NOT_RELEASED`. That is occurrence truth, not a reason to mutate the frozen candidate.

The active candidate identity is explicit on six reader/machine-facing surfaces, including baseline, README, lineage, zh-CN manifest, Operational reference index, and reference manifest. Candidate.2 references in README / Release Discipline are explicitly framed as predecessor lineage/preserved-state history rather than active self-identity.

Therefore release packaging must perform an auditable identity projection:

`v0.3.7-candidate.3 -> v0.3.7 / CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`

and replace `CANDIDATE-BASELINE.yaml` with a truthful `CURRENT-BASELINE.yaml` while preserving validated material semantics.

This is release packaging work, not candidate.4 work.

### 4. Residual / evidence-boundary visibility

PASS.

The candidate continues to expose boundaries including:

- attack/completeness is not proven merely by machine counts;
- represented Authority Lease consistency does not establish external mandate authenticity;
- Effect Lifecycle does not claim exactly-once external execution;
- transferred source evidence is not receiver-local proof;
- Host-native/equivalent realization and universal Host applicability remain environment-relative/evidence-bounded;
- optional references remain optional/default-off rather than universal mandatory organs.

`attack_cardinality = OPEN` remains true. Field truth/external truth is not established by this audit. These are FIELD_VALIDATION / evidence-boundary facts, not newly demonstrated frozen candidate-byte defects.

## Audit-oracle occurrence truth

The hardening audit itself required several corrections before the final PASS:

- candidate baseline shape/file-name assumptions were corrected;
- predecessor-lineage mentions were distinguished from stale active identity;
- legacy relocation was inspected instead of assuming rename == exact-byte identity;
- relocation-only output labels were added to the normalization after exact diff/readback;
- workflow dependency `jsonschema` was added before re-running the candidate validator;
- generated regression bytes were compared explicitly rather than using a naive clean-worktree assertion.

These failed runs are not hidden. They demonstrate why release hardening is useful, but none established a material frozen candidate-byte defect.

## Disposition

`CANDIDATE_SUCCESSION_STOP = YES`

`CANDIDATE.4 = NOT_JUSTIFIED_BY_CURRENT_EVIDENCE`

`RELEASE_PACKAGING = PERMITTED`

Candidate.3 remains immutable. If release packaging/exact release checks later demonstrate a material defect that is genuinely in the frozen candidate semantics/bytes rather than release identity/packaging, then candidate.4 becomes required. Do not manufacture candidate.4 merely because attack cardinality remains open.

## Next action

Follow the proven v0.3.6 release discipline:

1. make this candidate.3 release-preparation state main-visible;
2. create `release/v0.3.7` from that exact main checkpoint;
3. transplant frozen candidate.3 subtree byte-for-byte into `releases/current/` and record the transplant identity;
4. perform only audited release identity/packaging transforms;
5. run exact-head Current/release validation, regressions, language/Constitution checks, Main Gate and CodeQL;
6. read back package/tree/hash evidence;
7. perform explicit release authorization and merge;
8. verify post-merge `releases/current/` identity and update project/handoff state.

Current remains v0.3.6 until that explicit promotion completes.
