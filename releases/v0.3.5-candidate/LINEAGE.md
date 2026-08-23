# v0.3.5 candidate.2 lineage

## Base Current

- ENA v0.3.4
- effective Current tree: `b237802c08d608bb9be650fe213b7846d3be4bf6`
- repository base commit for v0.3.5 work: `9d84e179aae9f5f5d8dbabc7be56dee4ae2f8724`

## Frozen first candidate

First v0.3.5 frozen candidate:

- source commit: `eb6d7ba00894ed446903aebe61cd59f0bdb59af7`
- effective candidate tree: `f373e7695348c157dcd48d3ed243ea3079215b8f`
- independent falsifier: DSH / DeepSeek v4-flash with prior ENA/V2/v0.3.3 lineage exposure, independent of v0.3.5 design
- independent verdict: `NEEDS_REVISION`

Mechanically reproduced material problems included zero-experiment selection, negative-evidence migration laundering, lifecycle/selection conflation, state-blind closure, and new-tool/schema disconnection.

The first candidate remains immutable evidence.

## Frozen candidate.1

candidate.1 was created as a successor identity and frozen at:

- source commit: `e6ff1e76afb8ad8919186786100ec153a5f0d07a`
- effective candidate tree: `ff2cb44c7a5d1b472800180578b5df7baa123aec`
- freeze-record commit: `63ca8bdb14bfa4aca213d1dc88287f15572dd5c2`

The same DSH falsifier re-ran the original attacks under the honest role:

`SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH`

Targeted verdict:

`TARGETED_REVALIDATION_SUPPORTED_WITH_RESIDUALS`

The material predecessor failures were mechanically closed and the falsifier found no evolution-starvation/over-governance regression.

Residuals relevant to release decision included:

- N1: CLI did not independently reject invalid migration lifecycle enum;
- N2: CLI could propagate a forged stronger `source_authentication` string;
- N7: committed inherited-regression result still carried the old wrong identity shape.

Additional N3–N6 observations remain research/field residuals rather than being silently erased.

candidate.1 remains immutable evidence.

## candidate.2 trigger and scope

candidate.2 is a second successor identity created specifically to close N1/N2/N7 before release decision, plus the directly adjacent fixed `transfer_status` consistency guard.

It does not change the 38 Constitution rules and does not reopen the broader v0.3.5 semantic design merely because a few implementation residuals existed.

candidate.2 scope:

- CLI validates source lifecycle enum;
- CLI rejects self-edited source-authentication elevation;
- CLI validates fixed transfer status;
- candidate.2 adversarial regressions encode these closures;
- committed regression output is synchronized with its generating suite and CI checks regeneration parity;
- active candidate and zh-CN projection identities are synchronized to candidate.2.

## Primary field/design inputs retained

- Hermes longitudinal runtime adoption/persistence evidence;
- OpenClaw longitudinal adoption/persistence evidence;
- DSH mature-host migration evidence;
- fresh Hermes/Ubuntu first-adoption failure + correction;
- fresh Codex/Windows first-adoption evidence;
- Issue #51 opportunity register;
- maintainer decisions on evolutionary telos, variation, migration, emergence, continuity, multilingual semantics, anti-sovereignty, and retirement of active Mainline status.

Key direction:

`protect self-evolution -> actively enable and accelerate sustained self-evolution`

`governance as center -> governance as evolvability infrastructure`

Current candidate.2 status before freeze:

`AUTHOR_RESIDUAL_CLOSURE / NOT_CURRENT / NOT_RELEASED / NOT_YET_FROZEN`

Passing author tests cannot promote this lineage. candidate.2 requires an exact freeze identity and at least narrow targeted revalidation/reconciliation before release decision.
