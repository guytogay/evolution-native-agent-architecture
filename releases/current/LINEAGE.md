# v0.3.5 release lineage

## Base Current

- ENA v0.3.4
- effective Current tree at v0.3.5 work start: `b237802c08d608bb9be650fe213b7846d3be4bf6`
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

The same DSH falsifier re-ran the original attacks under:

`SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH`

Targeted verdict:

`TARGETED_REVALIDATION_SUPPORTED_WITH_RESIDUALS`

The material predecessor failures were mechanically closed and the falsifier found no evolution-starvation/over-governance regression.

Residuals relevant to release decision included:

- N1: CLI did not independently reject invalid migration lifecycle enum;
- N2: CLI could propagate a forged stronger `source_authentication` string;
- N7: committed inherited-regression result still carried the old wrong identity shape.

Additional N3–N6 observations remained research/field residuals.

candidate.1 remains immutable evidence.

## Frozen candidate.2

candidate.2 was created specifically to close N1/N2/N7 before release decision plus the directly adjacent fixed `transfer_status` consistency guard.

Frozen identity:

- source commit: `8393b8b05d34797965c612e8b9ca938d306f6322`
- effective candidate tree: `b10854f191d9641138e2f44278f043f124a2e120`
- freeze-record commit: `34e12333bcbe6cf8a3a2a992040d93012ead868b`

candidate.2 scope:

- CLI validates source lifecycle enum;
- CLI rejects self-edited source-authentication elevation;
- CLI validates fixed transfer status;
- candidate.2 adversarial regressions encode these closures;
- committed regression output is synchronized with its generating suite and CI checks regeneration parity;
- active candidate and zh-CN projection identities were synchronized to candidate.2.

## candidate.2 narrow revalidation

The same DSH falsifier revalidated the residual closures under:

`SAME_FALSIFIER / NARROW_RESIDUAL_REVALIDATION / NOT_FRESH`

Verdict:

`NARROW_REVALIDATION_SUPPORTED`

Reported mechanical results:

- N1 CLOSED;
- N2 CLOSED;
- adjacent transfer-status self-upgrade attack CLOSED;
- N7 CLOSED with zero-diff regeneration;
- candidate.1 regression preservation PASS;
- no new MATERIAL/BLOCKING finding;
- no observed evolution starvation / over-governance regression;
- English/zh-CN Constitution unchanged;
- Current remained v0.3.4 during validation.

Durable summary:

`collaboration/inbox/2026-08-23-v035-candidate2-dsh-narrow-revalidation-summary.md`

## Final reconciliation

Host-side final reconciliation:

- commit: `bbdb0347ee83b1d76d21f54e1c16c6038442b26d`
- decision: `RELEASE_PREPARATION_SUPPORTED`
- candidate succession stop: `YES unless new material evidence appears`

N3–N6 remain explicit research/field residuals rather than being hidden or converted into unsupported new rules.

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

## Release status

v0.3.5 release target:

`CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE`

Beginning with v0.3.5, `MAINLINE / NOT_MAINLINE` is no longer an active adopter-facing maturity axis. Historical records using those labels remain unchanged as history.

The exact released Current tree/package digest/merge identity are release-author evidence and are recorded outside this self-referential file after publication.
