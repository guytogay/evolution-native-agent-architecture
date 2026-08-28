# Project State — candidate.3 frozen / hardening passed / release preparation supported

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Current subtree: `7dcbb3934883ffa6cc5292a662588cafc1533cff`.

## Frozen candidate.3

- identity: `v0.3.7-candidate.3`
- frozen source: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- candidate files observed: `118`
- exact pre-freeze run: `33150269264` — SUCCESS
- targeted post-freeze run: `33150553992` — SUCCESS
- release hardening run: `33152201566` — SUCCESS
- current: false
- released: false
- material candidate writes: forbidden after freeze

## Candidate succession result

candidate.0 -> candidate.1 -> candidate.2 -> candidate.3 converged under independent/targeted falsification pressure.

Candidate.2 fresh A-S/A-P Phase B required candidate.3. Candidate.3 closed the six material repair classes and preserved inherited contracted behavior. A final release hardening audit then tested adopter traversal, compatibility/relocation, release projection readiness, and evidence-boundary visibility without finding a new material frozen candidate-byte defect.

Final reconciliation:

`CANDIDATE_SUCCESSION_STOP = YES`

`RELEASE_PREPARATION_SUPPORTED`

Hardening reconciliation:

`RELEASE_HARDENING_PASS / NO_MATERIAL_FROZEN_BYTE_DEFECT / RELEASE_PACKAGING_PERMITTED`

Candidate.4 is not justified absent new material evidence.

## Compatibility posture

`VALID_PREDECESSOR_CONTRACT_BEHAVIOR -> PRESERVE`

`SEALED_INVALID_FALSE_OK_OR_CONTRADICTION -> INTENTIONALLY_TIGHTEN`

Observed hardening facts:

- 55 Current files vs 118 candidate files;
- 28 same-path byte-identical;
- 23 same-path modified;
- 67 additive files;
- 4 former top-level removals, all explained by candidate baseline replacement or explicit legacy relocation;
- legacy `ena_evolve.py` exact-byte preserved;
- relocated legacy adversarial probes differ only in truthful legacy/path/module/output labels and execute PASS;
- v0.3.6 core adopter paths remain;
- 38 Constitution IDs preserved;
- inherited 164/164 zero-flip and successor 61/61 preserved;
- candidate-local relative Markdown links: 0 broken.

The intended adopter transition is singular Current `v0.3.6 -> v0.3.7`; candidate identities are governed development lineage.

## Evidence boundaries

Still visible:

- attack cardinality OPEN;
- external authority/receipt/source authenticity not established merely by represented validators;
- natural fresh-session salience, Host applicability, and bilingual behavioral equivalence remain field evidence;
- cross-environment candidate-id namespace uniqueness is not universalized absent contract evidence.

These are not currently demonstrated material release blockers.

## Immediate next action

`MAIN_VISIBLE_CHECKPOINT_THEN_CREATE_RELEASE_V0_3_7_AND_TRANSPLANT_FROZEN_CANDIDATE3`
