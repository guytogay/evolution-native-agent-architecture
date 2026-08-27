# Candidate Self-Priming Incident — 2026-08-27

Status: `METHOD_INCIDENT / BLIND_PHASE_A_INTAKE_INVALIDATED / CANDIDATE1_BYTES_UNCHANGED`

## Trigger

A genuinely fresh reviewer was instructed to perform blind Phase A against frozen `v0.3.7-candidate.1`.

Frozen identity:

- source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- candidate subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`

The reviewer followed the allowed path into the candidate subtree and opened:

`releases/v0.3.7-candidate/CANDIDATE-BASELINE.yaml`

That file itself disclosed material predecessor/repair information, including predecessor Phase-A lineage, `NEEDS_REVISION`, explicit required repair shapes, successor repair commits, and targeted/open-branch validation lineage.

The reviewer correctly stopped and declared:

`INELIGIBLE_FOR_FRESH_PHASE_A`

No Phase-A report was sealed, no candidate bytes were modified, and no Phase B was performed.

Issue `#128` is preserved as the invalid-intake occurrence and closed `not_planned` after recording the contamination.

## What failed

The prior validation method assumed:

```text
CANDIDATE_LOCAL_BYTES
-> SAFE_PHASE_A_TARGET
```

That assumption is false for a self-describing release candidate.

A candidate can legitimately contain two materially different information roles:

```text
BEHAVIOR / CONTRACT / IMPLEMENTATION

and

LINEAGE / REPAIR HISTORY / AUTHOR EVIDENCE
```

When those roles share one package, asking a fresh reviewer to inspect the entire exact package before sealing Phase A creates an internal priming channel.

Observed history-bearing surfaces include at minimum:

- `CANDIDATE-BASELINE.yaml`
- `CHANGELOG.md`
- `LINEAGE.md`

The defect is therefore not merely an external briefing problem.

```text
AUTHOR_PRIMING_CHANNEL
CAN_EXIST_INSIDE_TARGET_PACKAGE
```

## Why this does not require candidate.2

The frozen candidate's lineage and changelog are legitimate traceability surfaces. Removing history from an already frozen candidate solely to make blind review easier would conflate candidate packaging with validator interface design.

No material candidate behavior defect was established by this incident.

Therefore:

```text
VALIDATION_INTERFACE_DEFECT
!=
CANDIDATE_BYTE_DEFECT
```

Candidate.1 remains frozen and immutable.

## Method repair

Fresh validation must distinguish a **blind semantic view** from the full self-describing package.

### Phase A-S — blind semantic falsification

Expose a mechanically bound view containing exact frozen candidate bytes needed to infer and exercise semantics, while withholding candidate-local files whose primary/mixed role discloses predecessor findings, repair history, or author validation lineage.

The view must be a projection, not a new candidate:

```text
FROZEN_CANDIDATE
-> EXACT_BYTE_PRESERVING_PROJECTION
-> BLIND_SEMANTIC_VIEW
```

Every retained candidate file must remain byte-identical to the frozen source. Exclusions must be explicit and auditable.

### Seal A-S

Persist the independent semantic attack tree before opening withheld history-bearing files.

### Phase A-P — independent package/self-description audit

After the semantic seal, the same independent reviewer may inspect the excluded candidate-local history/status surfaces for package consistency, contradictions, stale claims, and misleading self-description.

This stage remains role/oracle independent but is not claimed to be search-space blind with respect to the disclosed history.

### Phase B — author reconciliation

Only after the independent artifacts are persisted may author attack maps, repair narratives, expected verdicts, and reconciliation context be opened.

## New distinction

```text
FULL_PACKAGE_INDEPENDENCE
!=
FULL_PACKAGE_SEARCH_SPACE_BLINDNESS
```

For a self-describing candidate, full-package search-space blindness may be impossible without a projection or packaging split.

The goal is not maximum secrecy. It is to prevent author history from becoming the validator's initial search ontology.

## Packaging lesson

Future candidates should prefer separating:

```text
CURRENT_CANDIDATE_STATE / CONTRACT CLAIMS
```

from:

```text
HISTORICAL_REPAIR / VALIDATION EVIDENCE
```

when doing so improves both adopter clarity and independent validation without sacrificing traceability.

This is a packaging design opportunity, not an automatic requirement to rewrite frozen candidate.1.

## Invariants preserved

- candidate.1 frozen bytes remain immutable;
- Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`;
- prior contaminated reviewer state is not reused as fresh;
- attack cardinality remains open;
- no successful machine gate is relabeled independent evidence;
- candidate.2 is not created without a material candidate-byte correction basis.
