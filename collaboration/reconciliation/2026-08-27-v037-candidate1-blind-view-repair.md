# ENA v0.3.7 candidate.1 — blind-view repair reconciliation

Date: 2026-08-27

Status: `CANDIDATE1_FROZEN / PRIOR_BLIND_INTAKE_INVALIDATED / BLIND_SEMANTIC_VIEW_READY / FRESH_A-S_A-P_NEXT / NOT_CURRENT / NOT_RELEASED`

## Frozen object unchanged

`v0.3.7-candidate.1` remains frozen at:

- source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- candidate subtree `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- Current subtree at the same source `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze run `33055811978` — SUCCESS

No candidate.1 or Current byte was changed by this validation-method repair.

## Invalidated intake

Issue `#128` used the full self-describing candidate subtree as blind Phase-A input.

A genuinely fresh reviewer correctly stopped after discovering that permitted candidate-local `CANDIDATE-BASELINE.yaml` disclosed predecessor findings and candidate.1 repair history.

Reviewer state:

`INELIGIBLE_FOR_FRESH_PHASE_A`

No Phase-A report was sealed.

Issue #128 is closed `not_planned` and preserved as occurrence truth for the invalid intake.

## Method defect

```text
CANDIDATE_LOCAL
!=
AUTOMATICALLY_BLIND_SAFE
```

The candidate package legitimately mixes behavior-bearing files with lineage, repair history, expected fixtures, regression/selftest corpora, and prior-probe evidence.

The defect was in the validation interface, not an established candidate behavior defect.

Therefore candidate.2 is **not** created solely for this incident.

Canonical method repair:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

Incident:

`research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md`

## Replacement validation view

Branch:

`validation/v037-c1-blind-semantic-primary`

Entry:

`collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-entry.md`

Manifest:

`collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml`

The view is derived from the exact frozen source. Final construction audit against `ae690346...` showed:

- candidate-side diffs are declared removals of history/oracle/regression/selftest/prior-probe surfaces only;
- no retained candidate file is modified;
- validation metadata is added outside candidate cargo;
- the view is not a candidate identity and has no release authority.

One mixed-role file remains physically exact because it contains core runtime semantics:

`tools/validate_evolution_record_v2.py`

A-S permits ranged reads of its implementation/CLI and withholds the embedded selftest range until the semantic seal.

## Independent-validation sequence

### A-S

Fresh blind semantic falsification against the priming-reduced exact-byte view.

Required report:

`collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-s-primary.md`

Its commit is the A-S seal.

### A-P

Only after A-S seal, independently inspect withheld candidate-local history/oracle/selftest surfaces from the exact frozen source.

Required report:

`collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-p-primary.md`

A-P remains independent but is not represented as search-space blind after candidate-local history opens.

### Stop before Phase B

After A-P is committed, the fresh reviewer stops. Project-manager/author reconciliation opens only afterwards.

## New intake

Issue:

`#131 — Fresh independent A-S/A-P — v0.3.7 candidate.1`

This issue supersedes #128 as the active independent-validation intake.

## Decision rules after independent artifacts

- material candidate-byte defect -> candidate.2 required;
- package/history contradiction that requires candidate bytes to change -> candidate.2 required;
- validation-method defect only -> repair method/interface, not candidate identity;
- no material defect -> proceed to Phase B reconciliation without manufacturing a successor;
- attack cardinality remains open in every case.

## Current

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

No promotion authority is created by the blind-view repair or Issue #131.
