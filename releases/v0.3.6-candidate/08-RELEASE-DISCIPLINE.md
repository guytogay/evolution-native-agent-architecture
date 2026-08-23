# 8. Release Discipline — v0.3.5

A deployable ENA adoption version must be self-contained.

## Version identity

One adoption version identifies one immutable effective-content state.

`same ena_version -> same effective content`

Material change requires a new version/candidate identity. Research/candidates may branch; the adoption target remains singular.

The first frozen v0.3.5 candidate was independently falsified. candidate.1 was a successor identity and later received same-falsifier targeted support with residuals. candidate.2 closed those concrete release-decision residuals and received `NARROW_REVALIDATION_SUPPORTED`. None of those successor identities rewrites the frozen predecessor trees.

## Active adopter-facing status model

Beginning with v0.3.5, ENA retires `MAINLINE / NOT_MAINLINE` as an active adopter-facing maturity axis.

Adopters need to know:

- **Current** — which singular baseline should be adopted now;
- **maturity/status** — currently `FIELD_VALIDATION`, later another explicitly defined maturity if justified.

Historical `MAINLINE` and `NOT_MAINLINE` records remain historical occurrence truth and are not rewritten.

`Git main != ENA Current`

## Candidate discipline

A candidate is a variation. It must not promote itself because it is newer, the author prefers it, tests pass, or it better matches the current narrative.

`candidate -> freeze -> independent falsification/validation -> targeted correction/revalidation where needed -> reconciliation -> release decision`

If a frozen candidate needs material correction, create a successor identity such as `candidate.1` or `candidate.2`; do not silently edit the frozen effective-content tree.

A same-falsifier targeted revalidation may verify specific fixes when labeled honestly; it is not relabeled as a fresh independent validator.

Stop creating successor candidates when the decision-changing residual cycle has converged. Visible research residuals are not automatically release blockers.

## Frozen Current

`releases/current/` remains frozen under one version identity. Do not edit Current in place under an unchanged `ena_version`.

A material Current change requires a new release identity.

## Source/distribution identity

A release must be built from identified committed source bytes.

Release-authoring evidence may include source commit/tree, exact file set, byte/hash parity, package digest, and published artifact readback.

Ordinary adopters normally need only the **minimum sufficient immutable effective-content identity** for what they actually compiled from, plus human-readable version/status. They need not reproduce release-author ceremony merely to use Current.

## Language projections

A supported language projection is part of the release file set or otherwise immutably bound to it. It declares source effective-content identity, language tag, projection identity/version, coverage, known gaps, and semantic-conformance evidence where available.

A projection update that changes material decision meaning is a material release change.

## Migration and compatibility

A receiver may use a newer semantic baseline while retaining older Host implementation mechanisms if the semantic baseline and implementation version/scope are explicit, incompatibilities/residuals remain visible, and unsupported equivalence is not invented.

`canonical semantic baseline != Host mechanism version`

## History

Preserve historical releases/candidates/evidence in Git/project history. Do not force ordinary adopters to reconstruct history to determine Current.

> **Expose one adoption surface; preserve many historical surfaces.**
>
> **History is evidence, not a second runtime baseline.**
