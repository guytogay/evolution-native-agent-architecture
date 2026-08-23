# ENA v0.3.6 Candidate Lineage

Status: `WORKING_CANDIDATE / NOT_FROZEN / NOT_CURRENT / NOT_RELEASED`.

## Parent baseline

Canonical parent at candidate start:

- ENA Current: `v0.3.5 / CURRENT / FIELD_VALIDATION`;
- Current effective-content tree: `9c928b4c99ae72e53c89978cf1d10b7ea068c182`;
- repository base commit after post-release housekeeping: `f14855fdfd57b975195f0b1c261b754bd3058749`.

## Working lineage

1. Design seed on `candidate/v0.3.6-work`:
   - commit `f48b70f7cb82cd240a97d6d807874def37d67d70`;
   - record `collaboration/inbox/2026-08-23-v036-evolution-ecology-design-seed.md`.

2. Working candidate initialized:
   - commit `5d4b5ea92c9d3bf8972f56e72c3487e03a598623`;
   - draft PR #68.

3. Complete v0.3.5 Current effective-content tree inherited into candidate directory:
   - commit `668a1be941045cb25c86008eaee620340a21b9a6`;
   - no modification to `releases/current/`.

4. Candidate identity + first ecology semantics:
   - commit `4fb504d2b78c958b84eafb20336b579d89323b5f`;
   - candidate baseline, metabolism/ecology, Commons semantics.

5. Candidate Runtime Kernel, canonical-lineage clarification, expression schema v2, and author attack plan:
   - commit `ccdbe0e12d51a2fcdd4b6d3d4f356a7aa8ec015c`.

6. Candidate identity, zh-CN hot path, and bilingual ecology fixtures aligned:
   - identity/lineage/zh-CN alignment commit `aad6cc43e232e64fb3c852eb8da112fc149ac352`;
   - bilingual ecology semantic fixtures commit `3533c630745c994352601b9a23b784312324e143`.

7. Candidate-specific pre-freeze validation surface added and first author falsification repairs applied:
   - candidate validation workflow/validator checkpoint `921e23cbfb9d3c739a3c4cb74adc371e0efcd3ca`;
   - latent/expression identity corrections through `dee537e891da329afe254539a24cceaeb9370d9f`.

8. Second/third author falsification passes tightened selection/Commons boundaries and evidence-template identity:
   - selection/Commons correction checkpoint `dcdc4093bd2b88d3316fb3d4376c69b5e2efff97`;
   - identity/concept-map checkpoint `730565e78c7c20e5f74cb0e43ccc5493194b154d`;
   - field-template/evidence identity checkpoint `9d24e53066055628a022cc098b9517bd798cf7bd`;
   - zh-CN Constitution identity correction `e89737e09237acdb6cfeed183d8c8f15cb1b7091`.

9. Full PR identity sweep and regression hardening:
   - capability-map identity correction `3cf44b5f7298d64ac7e16ed83b12eb589d1b701a`;
   - operational-contract identity correction `c6c583018e99b8f8e2d8ace17a03eb6f8bbd20aa`;
   - pre-freeze validator upgraded to enforce active-file identity and v2 selftest `082782ce3aeca591152b5ba43a3b2bfeb628ab80`.

10. Twenty-four planned attack classes reconciled and pre-freeze evidence boundary encoded:
    - author self-falsification pass 4 `3dbf38383d75422c4cbfde8b1cd473dc76ecbc73`;
    - machine-readable pre-freeze evidence/residual status in `CANDIDATE-BASELINE.yaml` at `b620857e9866cd74ee3b70855c3ee3698179b0f9`;
    - lineage checkpoint `79d4562d7e28888617a4063840f2e68f7b570737`.

11. External pre-freeze machine verification pass 1 tested exact source `79d4562d7e28888617a4063840f2e68f7b570737`:
    - candidate subtree observed `85b6615bf7bb5f8f36da6b1baa3e3c374066f00b`;
    - Current subtree observed/preserved `9c928b4c99ae72e53c89978cf1d10b7ea068c182`;
    - final verdict `PREFREEZE_MACHINE_CHECK_FAIL`;
    - failure preserved in `collaboration/reconciliation/2026-08-23-v036-external-prefreeze-machine-verification-1.md`.

12. Corrections after external pass 1:
    - candidate-evaluation/adoption boundary made explicit in `AGENT-ADOPTION-INSTRUCTION.md` at `71cc0f72a34fb9448259a9f0fd3fdc49de249b16`;
    - workflow strengthened to execute the full inherited composed-validator regression suite, in-memory Python compile, and post-validation worktree-clean check at `5026052170cb249ab5b90295ede7d50ad747ed32`;
    - external failure occurrence record committed at `d6aef1c77792a579238dd3978c1ea7982c923fe8`;
    - machine-readable revalidation blocker encoded at `ff72b2e073161e0ab38e222b2a1e110a823ae19b`.

Later commits must append to this lineage rather than rewrite frozen predecessor identities.

## Machine evidence currently obtained

Author-side v2 represented-consistency replay:

`EVOLUTION_RECORD_V2_SELFTEST_PASS 10`

External machine pass 1 independently established that source `79d4562d...` had:

- Current isolation `PASS`;
- v2 selftest `PASS`;
- inherited `ena_evolve.py selftest` `PASS`;
- inherited basic `validate_contracts.py selftest` `PASS`;
- Python compile `PASS`;
- post-test worktree `CLEAN`;
- aggregate `validate_candidate.py` `FAIL` because of a brittle exact-string active-file identity assertion.

The same verifier also identified that the basic contract selftest did not exercise the full retained v2/v2.1 composed regression corpora. The workflow has been strengthened accordingly.

No passing freeze claim is inherited from the failed source. A new exact source must be revalidated.

## Relationship to v0.3.5 validation

v0.3.5 field validation issue #61 remains a separate evidence stream. Starting v0.3.6 work does not retroactively resolve v0.3.5 fresh-Host salience/application evidence, nor does it invalidate v0.3.5 Current.

Inherited v0.3.5 residuals N3–N6 remain research/field residuals unless new evidence changes their importance.

## Candidate freeze rule

No frozen candidate identity exists yet.

Freeze requires an explicit source commit and candidate effective-content tree after authoring/self-attack converges. Current blocker:

`EXTERNAL_PREFREEZE_MACHINE_REVALIDATION_PENDING_AFTER_GATE_AND_COVERAGE_CORRECTION`

Once frozen, material correction must use a successor candidate identity rather than editing the frozen tree.

## Canonical promotion boundary

A local branch/fork may freely vary ENA but cannot self-promote by writing `CURRENT` into its own metadata.

Canonical promotion requires the governed lineage process defined in `08-RELEASE-DISCIPLINE.md`, including falsification/validation, reconciliation, immutable identity, and explicit admission/release decision.

GitHub is the current carrier for this lineage, not the metaphysical definition of ENA validity.
