# ENA v0.3.6 external pre-freeze machine verification — pass 1

Status: `EXTERNAL_MACHINE_VERIFICATION / FAIL / PRE_FREEZE / NOT_SEMANTIC_VALIDATION`

This record preserves the first external pre-freeze machine verification of the v0.3.6 working candidate. It is not independent semantic validation and does not judge release fitness.

## Verified source identity

Repository: `guytogay/evolution-native-agent-architecture`

Source commit verified:
`79d4562d7e28888617a4063840f2e68f7b570737`

Candidate subtree verified:
`85b6615bf7bb5f8f36da6b1baa3e3c374066f00b`

Current subtree verified:
`9c928b4c99ae72e53c89978cf1d10b7ea068c182`

Base commit:
`f14855fdfd57b975195f0b1c261b754bd3058749`

The verifier independently confirmed no `releases/current/**` change between base and source and restored its worktree clean after testing.

## Final external machine verdict

`PREFREEZE_MACHINE_CHECK_FAIL`

The failure was not a candidate semantic verdict. The aggregate pre-freeze validator exited 1 during active-file identity checking.

## Finding E1 — brittle active-adoption identity check false-BLOCKed truthful candidate wording

Severity: `MATERIAL_PREFREEZE_GATE_FALSE_BLOCK`

The candidate file `AGENT-ADOPTION-INSTRUCTION.md` already identified itself as candidate evaluation and stated `DO NOT ADOPT AS CURRENT` plus the actual v0.3.5 Current baseline.

However, `tools/validate_candidate.py` required the exact lower-case substring `not adoption`. The truthful document did not contain that literal phrase, so the gate raised:

`AssertionError: agent instruction still behaves like Current adoption`

This is a false BLOCK in the gate: the represented boundary existed, but the check was coupled to one accidental wording.

Correction after the verified source commit:

- make the candidate boundary explicit in the activity file with `Candidate evaluation is not adoption.`;
- preserve `DO NOT ADOPT AS CURRENT` and the v0.3.5 Current pointer;
- do not reinterpret the failed source as having passed.

Correction commit:
`71cc0f72a34fb9448259a9f0fd3fdc49de249b16`

## Finding E2 — inherited contract selftest did not exercise the full inherited composed regression corpus

Severity: `PREFREEZE_COVERAGE_GAP`

The requested standalone command:

`python releases/v0.3.6-candidate/tools/validate_contracts.py selftest`

passed 10/10, but that selftest does not consume the retained `contract-fixtures.v2.json` and `contract-fixtures.v2.1.json` composed regression corpora.

The external verifier correctly noted that `tools/regression_suite.py` is the repository surface that exercises:

- migrated v0.3.2 selftests;
- inherited 164-case composed corpus;
- successor closure/D-control corpus.

Correction after the verified source commit:

- strengthen `.github/workflows/v036-candidate-validate.yml` to execute `regression_suite.py`;
- add in-memory compile checking of all candidate `tools/*.py`;
- assert post-validation worktree cleanliness;
- keep the evidence boundary explicit.

Correction commit:
`5026052170cb249ab5b90295ede7d50ad747ed32`

## Evidence that passed in external pass 1

The verifier independently observed:

- Current isolation: `PASS`;
- evolution-record v2 selftest: `PASS`, exit 0, `EVOLUTION_RECORD_V2_SELFTEST_PASS 10`;
- inherited `ena_evolve.py selftest`: `PASS`, exit 0, 10 cases, schema 1.2;
- inherited `validate_contracts.py selftest`: `PASS`, exit 0, 10/10;
- Python compile: `PASS`, 7/7;
- post-test worktree: `CLEAN`.

These passing subchecks do not override the aggregate gate failure at the verified source commit.

## Revalidation requirement

Because the candidate was not frozen, the corrections are ordinary pre-freeze authoring changes rather than a successor frozen candidate identity.

Do not freeze from source `79d4562d...`.

A new exact source commit/subtree must be externally re-run after all reconciliation/baseline updates are complete. The next machine verifier may be the same verifier because this is targeted machine revalidation, not fresh independent semantic falsification.

## Boundary

This external machine verification does not prove:

- external-world evidence truth;
- authority or recovery reality;
- fresh-session salience/application;
- Evolution Ecology philosophical correctness;
- release fitness;
- Current promotion.

> A failed gate is evidence even when the gate itself was wrong.
>
> Fix the gate or representation, preserve the failure, then re-run the new exact object.
