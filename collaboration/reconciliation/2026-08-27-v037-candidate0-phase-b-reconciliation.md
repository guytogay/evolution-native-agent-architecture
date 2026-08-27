# ENA v0.3.7 candidate.0 — Phase B reconciliation

Status: `NEEDS_REVISION / CANDIDATE_1_REQUIRED / CURRENT_UNCHANGED`

Date: 2026-08-27

## Inputs

Fresh blind Phase-A seal:

- issue: `#121`
- validation branch: `validation/v037-c0-blind-phase-a-primary`
- seal commit: `5ba3d241efa460fe170253860ad67045aa1d96a5`
- report: `collaboration/reconciliation/2026-08-27-v037-candidate0-independent-phase-a-primary.md`
- exact frozen source inspected: `d0e793593184740d9732902e948afd48ed96ae2f`
- exact frozen candidate subtree: `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`

Author-side comparison surfaces opened only after the Phase-A seal:

- candidate-local `tools/ena_evolve_v2.py`
- candidate-local `tools/validate_evolution_record_v2.py`
- candidate-local v2 schemas/template/selftests
- `.github/scripts/v037_candidate_author_attacks.py`
- `.github/workflows/v037-candidate-prefreeze.yml`
- `2026-08-27-v037-candidate0-author-harness-anti-ablation-audit.md`
- candidate evolution/release prose

This reconciliation does not rewrite the sealed Phase-A occurrence.

## Phase-A seal readback

The validation branch was one commit ahead of its main base and changed only the Phase-A report. No `releases/current/` or frozen candidate bytes were modified by the validator.

The fresh report declared that it had not consumed project-manager handoff/oracle/author-attack/reconciliation context before sealing. No evidence found during readback contradicts that declaration.

## Finding disposition

### A — imported record loses source applicability/consequence context

**Disposition:** `MATERIAL_CANDIDATE_DEFECT / AUTHOR_EVIDENCE_MISS / SHARED_BLIND_SPOT`

`export_packet_v2` carries:

- `source_variation_space`
- `evolutionary_subject`
- `protected_subjects`

but `import_packet_v2` does not persist those source values into `migration`. It instead creates receiver-local empty/null values unless caller overrides them. The imported record keeps a packet ref/hash, but the library default packet ref is `inline:adaptation-packet-v2`, which is not itself a durable resolver contract.

Candidate prose states that migration transfers a possibility plus represented source history and that source/receiver results remain separate. Source applicability/consequence context is decision-material lineage; silently making its retention depend on an external packet store weakens the advertised practical import path.

The author harness tested source-selection separation, latent import, transfer status, and digest tampering, but not retention of these source fields. The pre-freeze CLI roundtrip likewise checked receiver selection/expression/Variation-Space state but not source applicability-context retention.

**Required candidate.1 correction:** preserve these source fields explicitly in imported migration provenance while keeping receiver-local fields separate and unselected.

### B — packet tied-latest expression timestamps use a weaker oracle than record validation

**Disposition:** `MATERIAL_CANDIDATE_DEFECT / AUTHOR_EVIDENCE_MISS / SHARED_BLIND_SPOT`

`validate_evolution_record_v2.latest_by_time` rejects tied latest timestamps as ambiguous. Packet validation instead uses `max(...)`, so equal-time contradictory latest entries can be resolved by array order.

This is not an external-authentication question. It is an internal represented-consistency contradiction across two boundaries for the same chronological concept.

The author harness/selftest checked expression-state mismatch but did not mutate a tied-latest packet history.

**Required candidate.1 correction:** packet validation must reject tied latest timestamps consistently with record validation; add mutation-sensitive regression coverage.

### C — archive preservation claim is not bound to the state preserved

**Disposition:** `MATERIAL_CANDIDATE_DEFECT / AUTHOR_EVIDENCE_MISS / SHARED_BLIND_SPOT`

The schema names the field `archive.selection_state_preserved`. Candidate evolution prose states that pruning/archive/retirement must not rewrite selection history. The validator requires archive metadata but does not compare `selection_state_preserved` to the selection state/evaluation it is supposed to preserve.

A record can therefore be machine-valid with top-level/evaluation `SUPPORTED` while archive claims preserved `HARMFUL`.

The existing selftest checks archive presence and harmful-retired expression obligations, but not contradictory preservation metadata.

**Required candidate.1 correction:** bind archive preservation metadata to the represented selection truth, with tests for positive, negative, and unassessed cases.

### D — direct-use template is machine-valid with non-time `created_at`

**Disposition:** `MATERIAL_PACKAGING_AND_VALIDATOR_DEFECT / AUTHOR_EVIDENCE_MISS / SHARED_BLIND_SPOT`

The shipped template contains `"created_at": "candidate-template"`. The schema requires only a non-empty string, and the validator does not parse `created_at`. The selftest explicitly requires the unchanged base template to validate.

Candidate.0 exposes direct schema/template + validator use as a practical path. Therefore validator PASS can currently coexist with a `created_at` value that is not even timestamp syntax.

This does not justify forcing experiments, Variation Space, or selection on latent records.

**Required candidate.1 correction:** make the candidate consistency validator require timezone-aware RFC3339-compatible `created_at`; make the shipped template an explicit uninstantiated template that does not masquerade as a valid instantiated record, and update selftests accordingly.

## Author evidence comparison summary

| Fresh finding | Author harness | Candidate selftest | Exact pre-freeze gate | Phase-B result |
| --- | --- | --- | --- | --- |
| A source applicability-context retention | missed | missed | missed | shared blind spot |
| B tied latest packet expression history | missed | missed | missed | shared blind spot |
| C archive preservation contradiction | missed | missed | missed | shared blind spot |
| D non-time created_at accepted | missed; not targeted | base template intentionally accepted | selftest therefore passed | shared blind spot |

The earlier anti-ablation audit remains valid for the historical 1080->188 failure families it examined, but it did not claim candidate completeness and did not cover these independently discovered shapes.

## False-BLOCK controls that candidate.1 must preserve

Candidate.1 repairs must not collapse legitimate lightweight behavior independently confirmed in Phase A:

- `PROPOSED + LATENT + UNASSESSED` may exist without Variation Space, experiments, evaluations, or selection;
- expression may return to `LATENT` without manufacturing selection;
- source negative evidence does not permanently veto receiver-side re-test in materially different environments;
- optional references remain default-off and non-applicability remains legitimate;
- Authority may be `NOT_REQUIRED` for harmless non-authority-bearing work;
- Purpose-Relative Continuity may return `NOT_REQUIRED`;
- Standing may remain ordinary evidence intake / `NO_FORMAL_STANDING`;
- WAIT machinery is not mandatory when waiting cannot change the decision;
- recovery ceremony is consequence-scoped, not universal;
- control retirement may choose `KEEP_ACTIVE`, `UNKNOWN_WAIT`, immediate retirement, or reversible narrowing as evidence warrants.

## Open attack branches preserved, not collapsed into the four fixes

The following Phase-A branches remain open and must not disappear merely because candidate.1 repairs four deterministic defects:

- integration chronology versus `selection_state_at_commit`;
- use of unauthenticated/shallow source experiment/evaluation claims before receiver-local testing;
- source/receiver candidate-id collision and downstream identity confusion;
- cross-axis historical contradictions outside latest-state guards;
- cumulative optional-reference governance cost under composition;
- natural hot/cold cue salience;
- zh-CN behavioral equivalence;
- Host-native equivalence;
- durable packet-reference retention beyond the repaired self-contained import fields;
- retained composed-validator behavior under novel composed inputs.

These are not automatically release blockers. They remain branches for targeted candidate.1 falsification, field evidence, or residual classification according to decision materiality.

## Candidate verdict

`NEEDS_REVISION`

Reason: four deterministic candidate-local defects permit machine-valid or practical-path states that contradict the candidate's represented-consistency / migration-history / chronology claims. They are repairable without rewriting `releases/current/` and without turning optional/lightweight behavior into mandatory governance.

## Succession recommendation

`CANDIDATE_1_REQUIRED`

Candidate.0 remains frozen occurrence truth. Do not edit its frozen subtree or relabel it as corrected.

Candidate.1 should be a successor effective-content identity containing only justified repairs plus regression coverage and identity/readme/baseline projection necessary to make the successor self-consistent.

## Current boundary

`CURRENT = v0.3.6 / CURRENT / FIELD_VALIDATION`

No Current mutation is authorized by this reconciliation.
