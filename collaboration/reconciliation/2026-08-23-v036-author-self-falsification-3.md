# ENA v0.3.6 author self-falsification — pass 3

Status: `AUTHOR_SELF_FALSIFICATION / PRE_FREEZE / NOT_INDEPENDENT_VALIDATION`

## Finding C1 — inherited field-evidence template carried obsolete identity defaults

Severity: `MATERIAL_EVIDENCE_METADATA_DRIFT`

The inherited `templates/field-experience.v1.yaml` still defaulted:

- `ena_baseline: v0.3.3`;
- `status: UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`.

This is dangerous inside an active v0.3.6 candidate package because a fresh contributor could produce semantically new evidence with stale v0.3.3 identity and a maturity axis retired from active adopter-facing semantics in v0.3.5.

Correction:

- preserve a clearly marked v1 legacy/compatibility template without a false baseline default;
- add `field-experience.v2.yaml` as the active v0.3.6 candidate evidence template;
- candidate baseline points explicitly to v2 active + v1 legacy;
- no template contribution auto-promotes/reconciles candidate state.

## Finding C2 — Chinese Constitution projection still named v0.3.5 candidate

Severity: `IDENTITY_LEAKAGE / CORRECTION_REQUIRED_BEFORE_FREEZE`

The Chinese 38-rule projection itself preserves the inherited rules correctly, but its introduction says it is the v0.3.5 candidate projection. This does not alter rule meaning, yet a direct reader can misidentify the package version.

Required correction before freeze:

- rebind wording to v0.3.6 candidate while explicitly stating the 38 rules are inherited unchanged from v0.3.5 Current;
- do not silently modify the English Constitution or invent new IDs merely to make the projection look new.

## Finding C3 — historical compatibility is not active candidate identity

Severity: `DESIGN_CLARIFICATION`

A self-contained successor may legitimately carry old schemas/tools/fixtures for regression and compatibility. Those artifacts must be labeled or scoped so their historical identity cannot be confused with the active candidate identity.

The goal is not to replace every string `v0.3.5`; it is to distinguish:

`ACTIVE_CANDIDATE_SEMANTICS | INHERITED_VALIDATED_MECHANISM | LEGACY_COMPATIBILITY | HISTORICAL_REGRESSION_EVIDENCE`.

This avoids both identity leakage and pointless version-number churn.
