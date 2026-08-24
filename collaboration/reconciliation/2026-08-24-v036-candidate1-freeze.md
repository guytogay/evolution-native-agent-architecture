# ENA v0.3.6 candidate.1 freeze record

Date: 2026-08-24

## Status

`FROZEN_CANDIDATE.1 / FALSIFICATION_DRIVEN_SUCCESSOR / FINAL_EXACT_HEAD_MACHINE_PASS / AWAITING_SAME_FALSIFIER_TARGETED_REVALIDATION / NOT_CURRENT / NOT_RELEASED`

This record freezes the first successor to v0.3.6 candidate.0 after fresh independent semantic falsification returned `NEEDS_REVISION`.

The freeze does not claim that the original falsifier's findings are independently closed. It makes the author/reconciliation answer immutable so the same falsifier can target the exact repair rather than a moving object.

## Frozen candidate.1 identity

Frozen source commit:

`4af5d17a1cedcf2850b2b4dfe5446e132023369a`

Effective candidate subtree:

`releases/v0.3.6-candidate/`

Frozen Git tree:

`52a0cc260ec33fc3e332f6ac0f98f5d1e98b565d`

Current at the same frozen source remains:

`releases/current/`

Git tree:

`9c928b4c99ae72e53c89978cf1d10b7ea068c182`

Base repository commit:

`f14855fdfd57b975195f0b1c261b754bd3058749`

No `releases/current/**` change is part of candidate.1.

## Predecessor lineage

Frozen candidate.0:

- source: `3cb94d98882621acede189d0d47806efae44fb0f`;
- tree: `80f2da918811c26381d65eb5afa8e40f8410a32e`;
- freeze record: `15e513a72d59e28f8d3050ef877746f85ab706ba`;
- fresh independent semantic falsification verdict: `NEEDS_REVISION`;
- falsifier PR comment: `issuecomment-5389079667` on PR #68.

Candidate.0 remains immutable evidence and PR #68 was closed without merge after successor handoff.

Candidate.1 Draft PR:

`#69`

Author/reconciliation records:

- `collaboration/reconciliation/2026-08-24-v036-candidate0-independent-semantic-falsification.md`;
- `collaboration/reconciliation/2026-08-24-v036-candidate1-author-reconciliation.md`.

## Why the candidate baseline still says `frozen: false`

Candidate.1 deliberately corrected candidate.0's freeze-identity protocol before this freeze.

Its baseline declares:

`EXTERNAL_RECORD_BINDS_EXACT_IMMUTABLE_TREE`

and predeclares this exact external freeze-record path.

The baseline's `frozen: false` is therefore the truthful occurrence state of the package **before** this external freeze decision. Rewriting the tested package after machine validation merely to change that boolean would create a different candidate tree.

This record assigns frozen identity to exact tree `52a0cc260ec33fc3e332f6ac0f98f5d1e98b565d` without rewriting it.

Any material correction after this record requires a successor identity such as `v0.3.6 candidate.2`.

## Fresh falsifier findings driving candidate.1

The predecessor fresh falsifier classified:

### Material release blockers

- **F-01** — v2 integration-history structural regression versus v1;
- **F-02** — array order masquerading as chronological latest evidence/expression state.

### Material successor repairs

- **F-03** — migration provenance may be lost / local-imported evidence provenance absent;
- **F-04** — Commons packet v1 cannot carry expression/dormancy context;
- **F-05** — expression consequence side lacks a machine-visible obligation connection;
- **F-06** — mixed improved/degraded result may overclaim `SUPPORTED`;
- **F-07** — freeze identity protocol / carrier dependence residuals;
- **F-08** — zh-CN hot kernel omitted `ARCHIVED/RETIRED != selection verdict`;
- **F-09** — inherited `ena_evolve.py` false-BLOCKs latent propose/import by requiring Variation Space, while full runtime absence itself is an acceptable staged boundary.

### Nonblocking / research

- **F-10** — archive consistency asymmetry;
- **F-11** — future salience/application remains unproven field evidence;
- **F-12** — `experiments` versus broader `reality contact` terminology remains research wording.

The falsifier also explicitly withdrew three of its own initial attacks as false positives. That self-correction remains part of the evidence lineage.

## Candidate.1 repair summary

### F-01

v2 restores the predecessor integration-history required contract:

- `integration_id`;
- `time`;
- `target`;
- `result`;
- `selection_state_at_commit`;

and preserves authority/recovery/scope representation, with optional expression state at commit.

### F-02

v2 histories now use machine date-time representation; validator selects latest by parsed chronological time and rejects invalid/unzoned/tied latest timestamps rather than letting array order silently decide.

### F-03

Migration candidate representation now requires structured source provenance. Experiment/evaluation entries can explicitly state `LOCAL | IMPORTED`, and locally selected migrated candidates require local provenance on the represented local evidence path.

### F-04

`adaptation-packet.v1` remains unchanged. Candidate.1 adds additive `adaptation-packet.v2` carrying source expression/dormancy context and source negative-lineage references. Source context is not receiver-local proof.

### F-05

Expression history explicitly represents effect materiality. Only explicitly represented material expression without Variation Space, or harmful/not-supported/archived/retired state that remains expressed, requires a triggered-obligation reference. The repair intentionally does not require approval or Variation Space for every expression.

### F-06

`SUPPORTED` with a represented `DEGRADED` outcome requires an explicit tradeoff; otherwise a more qualified verdict such as `PARTIAL` is required.

### F-07

Candidate.1 predeclares an external exact-tree freeze protocol and this freeze-record path. The zh-CN projection no longer promises an impossible post-test rebind. The candidate validator no longer treats `frozen: false` as an eternal invariant.

### F-08

The zh-CN hot kernel now explicitly preserves:

`归档/退役 != 选择结论`

### F-09

Candidate.1 does **not** deep-integrate v2 into inherited `ena_evolve.py` merely for symmetry.

Instead it truthfully records that:

- the inherited tool remains state schema 1.2;
- it does not implement full mutation-pressure/expression v0.3.6 runtime semantics;
- its `propose` and `import` commands require `--variation-space` and therefore false-BLOCK the candidate.1 legal latent-now/experiment-later path;
- the inherited tool is not the normative v0.3.6 latent proposal/import path while that mismatch exists;
- adaptation-packet.v2 is a representation contract and the inherited tool still emits/accepts v1.

The same falsifier must decide whether truthful non-normative demotion is sufficient targeted closure or whether a small adapter/runtime repair remains required.

### F-10

`ARCHIVED` / `RETIRED` now requires represented archive metadata.

## Final exact-source machine evidence

Exact frozen source:

`4af5d17a1cedcf2850b2b4dfe5446e132023369a`

GitHub Actions on that exact PR head:

- ENA v0.3.6 Candidate Validate — run `32677101732` — `SUCCESS`;
- Main Gate — run `32677101720` — `SUCCESS`;
- CodeQL — run `32677101753` — `SUCCESS`.

Candidate-specific job `97287135336` completed every configured step successfully.

Observed machine markers/results:

- `EVOLUTION_RECORD_V2_SELFTEST_PASS 18`;
- inherited `ena_evolve.py` selftest: PASS, schema 1.2, 10 cases;
- `candidate1-identity-pass`;
- `current-tree-preserved-pass 9c928b4c99ae72e53c89978cf1d10b7ea068c182`;
- `constitution-id-pass 38`;
- `active-file-identity-pass 9`;
- `evolution-record-v2-schema-pass`;
- `adaptation-packet-v2-schema-pass`;
- `bilingual-fixture-structure-pass 8`;
- `field-template-pass`;
- `semantic-boundary-presence-pass 10`;
- `v2-consistency-selftest-pass`;
- `inherited-ena-evolve-boundary-selftest-pass 2`;
- `V036_CANDIDATE1_PREFREEZE_VALIDATION_PASS`.

Inherited composed regression remained:

- migrated v0.3.2: `10/10`;
- inherited corpus: `164/164`;
- successor closure corpus: `61/61`;
- total: `235/235`;
- unexpected verdicts: `0`;
- uncaught exceptions: `0`.

Python compile:

- `7/7`;
- failures: `0`.

Bytecode hygiene:

- no candidate `__pycache__` / `*.pyc` produced.

Post-validation worktree:

`CLEAN`

## Evidence boundary

This machine evidence and freeze do **not** prove:

- independent closure of F-01..F-10;
- external-world evidence truth;
- actual authority or recovery;
- future salience/application;
- universal ecological fitness or philosophical correctness;
- release fitness;
- Current promotion.

Machine green means the repaired represented contracts, selftests, inherited regression, syntax/hygiene, and Current isolation are internally consistent on the checked surfaces.

## Required next step

Return this exact frozen candidate.1 to the **same Agent that produced the fresh independent candidate.0 semantic falsification**.

Role for the next pass:

`SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH / NOT_AUTHOR`

The falsifier should:

1. verify exact frozen source/tree identities;
2. rerun its original P-series counterexamples first, especially F-01/F-02;
3. determine whether each F-01..F-10 repair closes the original defect without creating a new false-BLOCK or over-governance regression;
4. pay special attention to F-05 narrowness, F-03 provenance burden, F-07 freeze protocol, and F-09 non-normative tool demotion;
5. rerun at least one legitimate positive/control case for each repaired machine guard;
6. not modify candidate.1;
7. post a targeted revalidation report to PR #69 if write access remains available.

Targeted revalidation is not fresh independent discovery. Its purpose is defect closure against the falsifier's own prior attacks.

Do not merge or promote Current until that targeted revalidation is reconciled.
