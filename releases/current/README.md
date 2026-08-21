# ENA v0.3.3 — Current Adoption Baseline

Status: `FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`

This directory is the complete ENA v0.3.3 adoption target. Every effective runtime/adoption document under `releases/current/` belongs to this one flattened version.

Do **not** compose this baseline with older ENA releases, candidates, research artifacts, or branches.

## Start

For low-consequence bounded work:

1. Read `00-READ-ME-FIRST.md`.
2. Read `01-CONSTITUTION.md`.
3. Use `LITE-ADOPTION-INSTRUCTION.md`.
4. Retrieve additional contracts only when the task triggers them.

For STANDARD/HIGH_ASSURANCE or broader persistent adoption:

1. Read `00-READ-ME-FIRST.md`.
2. Perform Self-Positioning using `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`.
3. Read the Constitution and only the contracts/capabilities relevant to the current task/consequence envelope.
4. Use `CURRENT-BASELINE.yaml` as the machine-readable current-version pointer.

Use `CONTRIBUTION-PROTOCOL.md` and `templates/field-experience.v1.yaml` when contributing field evidence or research.

Project research/evidence/history outside this directory remains open and discoverable, but it is not an additional runtime version layer.

## Version and status

`v0.3.3` is the version identity.

`FIELD_VALIDATION` is the current maturity/evidence status.

The two are intentionally separate. Do not invent `BETA/RC` composition layers around this release.

## Release lineage

v0.3.3 is the successor to v0.3.2, carrying the composed claim-pack validation
surface (see `05-CORE-OPERATIONAL-CONTRACTS.md` §5.13). The v0.3.2 semantic
core remains byte-identical. The release lineage is documented truthfully in
`CHANGELOG.md` and `LINEAGE.md`, including the original v0.3.3 candidate's
`NEEDS_REVISION` fresh-validation result and its subsequent correction and
revalidation — historical negative evidence remains visible through the
canonical evidence surfaces (collaboration/inbox/, reconciliation, Git).

## Architectural posture

The shared ENA waist should stay small enough to preserve heterogeneous implementations:

- standardize identity/evidence/authority/effect/recovery/viability properties where interoperability requires them;
- keep Host/model/tool/cognitive implementation choices local where truthful interoperability does not require standardization;
- prefer extending existing contracts over adding parallel ontology;
- prefer decision-changing fixtures/tooling over taxonomy-only validation.

> **Open knowledge does not mean always-loaded knowledge.**
>
> **Research may branch; an adoption baseline must be singular.**
>
> **Universal semantics do not require universal implementation burden.**
