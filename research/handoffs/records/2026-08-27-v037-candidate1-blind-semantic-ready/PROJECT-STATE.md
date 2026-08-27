# Project state — candidate.1 blind semantic validation ready

Date: 2026-08-27

## Current

`v0.3.6 / CURRENT / FIELD_VALIDATION`

No current mutation or promotion is authorized.

## Candidate lineage

### candidate.0

Frozen predecessor:
- source `d0e793593184740d9732902e948afd48ed96ae2f`
- subtree `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`
- fresh Phase-A seal `5ba3d241efa460fe170253860ad67045aa1d96a5`
- Phase-B verdict `NEEDS_REVISION`
- superseded by candidate.1.

### candidate.1

Frozen successor:
- identity `v0.3.7-candidate.1`
- source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- subtree `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- Current subtree at same source `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- exact pre-freeze run `33055811978` — SUCCESS
- release state `NOT_CURRENT / NOT_RELEASED`

## Validation-method transition

The original candidate.1 post-freeze intake was Issue #128 on `validation/v037-c1-blind-phase-a-primary`.

A genuinely fresh reviewer encountered candidate-local predecessor/repair disclosure in the permitted full candidate package and correctly stopped. No Phase-A report was sealed.

Issue #128 is closed as an invalid blind intake, not as candidate acceptance/rejection evidence.

Method incident:

`research/methodology/incidents/2026-08-27-CANDIDATE-SELF-PRIMING-INCIDENT.md`

New distinction:

```text
VALIDATION_INTERFACE_DEFECT != CANDIDATE_BYTE_DEFECT
FULL_PACKAGE_INDEPENDENCE != FULL_PACKAGE_SEARCH_SPACE_BLINDNESS
```

## Active validation view

Branch:

`validation/v037-c1-blind-semantic-primary`

The branch starts from exact frozen source `ae690346...` and removes only declared candidate-local history/oracle/regression/selftest/prior-probe surfaces. Retained candidate files are unmodified exact frozen bytes.

Manifest:

`collaboration/reconciliation/2026-08-27-v037-candidate1-blind-semantic-view.yaml`

One core validator is mixed-role and remains byte-exact; A-S uses declared ranged reads to withhold its embedded selftest corpus.

The validation view is not a candidate and must never be promoted.

## Active independent task

Issue `#131`.

Sequence:

1. A-S fresh blind semantic falsification;
2. persist A-S seal;
3. A-P independent package/self-description/oracle audit from exact frozen source;
4. persist A-P report;
5. stop before Phase B.

A-S report path:
`collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-s-primary.md`

A-P report path:
`collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-p-primary.md`

## Decision after reports

The project manager first verifies report commits and frozen identity, then opens Phase B author reconciliation.

A material candidate-byte defect or package correction requires candidate.2. A validation-interface defect alone does not.

`ATTACK_CARDINALITY = OPEN`
