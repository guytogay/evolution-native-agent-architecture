# 8. Release Discipline — v0.3.5 candidate

A deployable ENA adoption version must be self-contained.

## Version identity

One adoption version identifies one immutable effective-content state.

`same ena_version -> same effective content`

Material change requires a new version identity.

Research/candidates may branch. The adoption target remains singular.

## Active adopter-facing status model

Beginning with v0.3.5, ENA proposes retiring `MAINLINE / NOT_MAINLINE` as an active adopter-facing maturity axis.

Adopters need to know:

- **Current** — which singular baseline should be adopted now;
- **maturity/status** — e.g. `FIELD_VALIDATION`, later another explicitly defined maturity if justified.

Historical `MAINLINE` records remain historical occurrence truth and are not rewritten.

`Git main != ENA Current`

The Git default branch is a repository mechanism. Current is the adoption pointer.

## Candidate discipline

A candidate is a variation.

It must not promote itself because:

- it is newer;
- the author prefers it;
- its tests pass;
- it better matches the current project narrative.

Candidate -> falsification/validation -> reconciliation -> release.

## Frozen Current

`releases/current/` remains frozen under one version identity.

Do not edit Current in place under an unchanged `ena_version`.

## Source/distribution identity

A release must be built from identified committed source bytes.

Release-authoring evidence may include:

- source commit/tree;
- exact file set;
- byte/hash parity;
- package digest;
- published artifact readback.

These are release-author obligations.

Ordinary adopters normally need only the **minimum sufficient immutable effective-content identity** for what they actually compiled from, plus human-readable version/status. They need not reproduce release-authoring ceremony merely to use Current.

## Language projections

A supported language projection is part of the release file set or otherwise immutably bound to it.

A projection declares:

- source effective-content identity;
- language tag;
- projection identity/version;
- coverage;
- known gaps;
- semantic-conformance evidence where available.

A projection update that changes material decision meaning is a material release change.

## Migration and compatibility

A receiver may use a newer semantic baseline while retaining older Host implementation mechanisms if:

- the semantic baseline is explicit;
- implementation version/scope is explicit;
- incompatibilities/residuals are visible;
- unsupported equivalence is not invented.

`canonical semantic baseline != Host mechanism version`

## History

Preserve historical releases/candidates/evidence in Git/project history.

Do not force ordinary adopters to reconstruct history to determine Current.

> **Expose one adoption surface; preserve many historical surfaces.**
>
> **History is evidence, not a second runtime baseline.**
