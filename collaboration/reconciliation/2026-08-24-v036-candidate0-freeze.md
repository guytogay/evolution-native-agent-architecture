# ENA v0.3.6 candidate.0 freeze record

Date: 2026-08-24

## Status

`FROZEN_CANDIDATE.0 / PRE_FREEZE_MACHINE_REVALIDATED / AWAITING_FRESH_INDEPENDENT_SEMANTIC_FALSIFICATION / NOT_CURRENT / NOT_RELEASED`

This record freezes the first v0.3.6 Evolution Ecology candidate after author self-falsification, two preserved external machine FAILs, corrective iteration, and a third exact-source external machine PASS.

Machine/structure PASS is not independent semantic acceptance and is not a release decision.

## Frozen candidate.0 identity

Frozen source commit:

`3cb94d98882621acede189d0d47806efae44fb0f`

Effective candidate subtree:

`releases/v0.3.6-candidate/`

Frozen Git tree:

`80f2da918811c26381d65eb5afa8e40f8410a32e`

Current at the same frozen source remains:

`releases/current/`

Git tree:

`9c928b4c99ae72e53c89978cf1d10b7ea068c182`

Base repository commit:

`f14855fdfd57b975195f0b1c261b754bd3058749`

No `releases/current/**` change is part of candidate.0.

The external pass-3 occurrence record was committed afterward at `4d7d5cd34d24908c1a58e0e0602d6f11ca21a881`; that evidence-record commit did not alter the frozen candidate subtree or Current subtree.

## Why the internal candidate baseline still says pre-freeze

The frozen tree's `CANDIDATE-BASELINE.yaml` truthfully records the state immediately before the external freeze decision, including `freeze_eligible: false` and a pending third external revalidation blocker.

The third revalidation then passed on that exact immutable tree. Editing the candidate baseline afterward to say `frozen: true` or `freeze_eligible: true` would create a different tree and invalidate the object that was actually tested.

Therefore frozen status is assigned by this external lineage record to the exact Git tree above. The internal pre-freeze metadata is preserved as occurrence truth, not treated as a contradiction or silently rewritten.

## Pre-freeze machine evidence lineage

### External pass 1 — FAIL

Source:
`79d4562d7e28888617a4063840f2e68f7b570737`

Verdict:
`PREFREEZE_MACHINE_CHECK_FAIL`

Material findings preserved:

- active candidate/adoption identity gate false-BLOCKed truthful wording because of an accidental literal substring dependency;
- the basic contract selftest did not exercise the complete retained composed regression corpus.

Occurrence record:
`collaboration/reconciliation/2026-08-23-v036-external-prefreeze-machine-verification-1.md`

### External pass 2 — FAIL

Source:
`9e9589126d896cd580a2fc04090b9957208ce779`

Verdict:
`PREFREEZE_MACHINE_REVALIDATION_FAIL`

What passed before the blocker:

- Current isolation;
- first active-file correction;
- v2 selftest 10/10;
- inherited `ena_evolve.py` selftest 10/10;
- full inherited composed regression 235/235 (`10 + 164 + 61`), zero unexpected verdicts, zero uncaught exceptions;
- Python compile 7/7.

Remaining findings:

- next previously unreachable LITE wording sentinel produced the same class of false BLOCK;
- ignored Python bytecode exposed a worktree-clean observability gap.

Occurrence record:
`collaboration/reconciliation/2026-08-24-v036-external-prefreeze-machine-revalidation-2.md`

### External pass 3 — PASS

Frozen source:
`3cb94d98882621acede189d0d47806efae44fb0f`

Frozen candidate tree:
`80f2da918811c26381d65eb5afa8e40f8410a32e`

Verdict:
`PREFREEZE_MACHINE_REVALIDATION_PASS`

Independent machine observations included:

- exact Git identity: PASS;
- Current isolation: PASS;
- aggregate `validate_candidate.py`: exit 0, all gates reached, final marker `V036_WORKING_CANDIDATE_PREFREEZE_VALIDATION_PASS` reached;
- evolution-record v2 selftest: PASS 10/10;
- inherited `ena_evolve.py`: PASS 10/10, schema 1.2;
- full inherited composed regression: PASS 235/235, zero unexpected verdicts, zero uncaught exceptions;
- Python compile: PASS 7/7;
- bytecode hygiene: PASS, zero pre-existing/new candidate `__pycache__` or `*.pyc` under the strengthened environment;
- deterministic `regression-results-v033.json`: byte-identical after regeneration;
- post-test worktree: CLEAN;
- failure history preservation: PASS;
- candidate baseline truthfulness: PASS;
- unexpected findings: NONE.

Occurrence record:
`collaboration/reconciliation/2026-08-24-v036-external-prefreeze-machine-revalidation-3.md`

PR #68 machine-verifier report comment:
`issuecomment-5388786244`

## Automated evidence at frozen source

Candidate-specific workflow on exact frozen source:

- run `32669963395` — push — `SUCCESS`;
- run `32669965880` — pull_request — `SUCCESS`.

The external verifier also observed Main Gate and CodeQL success on the exact head.

Automated success proves only represented structure/identity, retained regression, candidate machine consistency, syntax, hygiene, and Current isolation within the checked surfaces. It does not prove external evidence truth, real authority, real recovery, future salience, ecological benefit, philosophical correctness, or release fitness.

## Candidate.0 semantic scope to falsify

The frozen candidate introduces or deepens the following candidate semantics without adding new Constitution IDs:

- `Stimulus / 刺激` and `Mutation Pressure / 变异压力` without forced mutation;
- legitimate long-lived `Latent Variation / 潜伏变异`;
- `stored != expressed != applied != selected`;
- independent lifecycle / expression / selection axes;
- `LATENT | EXPRESSED` expression state;
- cue-triggered hot salience / cold capability as a runtime direction;
- environment-local selection rather than universal scalar fitness;
- Evolution Commons separation of publication, discovery, import, expression/experiment, and local selection;
- popularity/propagation is not proof;
- publisher/receiver autonomy remains bounded by legitimate authority, protected subjects, and external consequence;
- Rescue Plane may restore survivability without acquiring general governance authority;
- canonical ENA evolution depends on a governed reproducible reviewable lineage rather than GitHub metaphysics;
- minimal-intervention/ecological governance direction: govern the semantic/consequence floor rather than every interaction.

All 38 inherited Constitution IDs remain unchanged.

`NEW_CONSTITUTION_IDS = 0`

## Visible residual intentionally frozen for falsification

The inherited `tools/ena_evolve.py` remains the validated v0.3.5 implementation surface and does **not** implement mutation-pressure / latent-reservoir / expression runtime commands.

The candidate instead supplies v2 representation/schema/consistency validation while keeping runtime integration visibly absent.

This is intentionally frozen as an independent-falsifier question:

> Is `schema/validator support != full runtime implementation` an acceptable staged architecture boundary, or is the missing `ena_evolve.py` integration a material release blocker because the new semantics cannot reliably affect actual Agent behavior?

Do not resolve that question by editing candidate.0 during falsification.

## Required next step

Use a **fresh Agent that did not participate in v0.3.6 design, author self-falsification, pre-freeze repair, machine-verifier oracle construction, or the three targeted machine passes**.

Role:

`FRESH_INDEPENDENT_SEMANTIC_FALSIFIER / NOT_AUTHOR / NOT_MACHINE_ORACLE_AUTHOR`

The falsifier must inspect the frozen implementation/semantics itself before accepting author expectations, and should actively search for false confidence, over-governance, evolution starvation, unsafe externalities, incoherent ecology semantics, and legitimate behavior incorrectly blocked.

It must test the exact frozen source/tree above and must not modify candidate.0.

## Freeze rule

Any material correction after this record requires a successor identity such as `v0.3.6 candidate.1` with a new source commit and candidate tree.

Do **not** silently mutate tree `80f2da918811c26381d65eb5afa8e40f8410a32e` and continue calling it candidate.0.

`releases/current/` remains v0.3.5 until a later governed admission/release decision explicitly changes it.
