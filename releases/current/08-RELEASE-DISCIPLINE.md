# 8. Release and Canonical-Lineage Discipline — v0.3.6 Candidate

Status: `WORKING_CANDIDATE / NOT_FROZEN / NOT_CURRENT`.

A deployable ENA adoption version must be self-contained and immutably identifiable.

## Version identity

One adoption version identifies one immutable effective-content state.

`same ena_version -> same effective content`

Material change requires a new version/candidate identity. Research/candidates may branch; the adopter-facing Current remains singular.

## Current remains external to this candidate

While this candidate is unreleased:

- `releases/current/` remains the only adopter-facing baseline;
- candidate success cannot promote itself;
- candidate content must not be described as Current merely because it is newer or philosophically preferred.

`Git main != ENA Current`

`candidate branch != ENA Current`

## Candidate discipline

A candidate is a variation.

`candidate -> author attacks -> freeze -> independent falsification/validation -> targeted correction/revalidation where needed -> reconciliation -> release decision`

If a frozen candidate needs material correction, create a successor identity; do not silently edit the frozen effective-content tree.

A same-falsifier targeted revalidation may verify specific fixes when labeled honestly; it is not fresh independent validation.

Stop candidate succession when decision-changing residuals converge. Visible research questions are not automatic release blockers.

## Canonical ENA evolution

ENA itself is evolvable, but one local Agent/fork cannot mint canonical status by self-description.

Canonical change requires a durable lineage process with properties sufficient to establish:

- proposal/change identity;
- reviewable effective content;
- falsification/validation evidence;
- reconciliation/decision record;
- immutable version identity;
- recoverable/publicly inspectable history appropriate to the project;
- explicit promotion/admission event.

GitHub is the **current project carrier** for this lineage. The semantic requirement is the governed reproducible lineage, not eternal metaphysical dependence on GitHub as a service.

Changing carriers must itself preserve enough lineage/evidence to avoid a silent standards fork masquerading as continuity.

## Frozen Current

`releases/current/` must not be edited in place under an unchanged version identity.

A material Current change requires a new release identity and explicit release decision.

## Source/distribution identity

A release must be built from identified committed source/effective-content bytes.

Release evidence may include source commit/tree, exact file set, byte/hash parity, package digest, and published artifact readback.

Ordinary adopters need the minimum sufficient immutable effective-content identity for what they actually compiled from; they need not reproduce release-author ceremony merely to use Current.

## Language projections

A supported language projection is part of the release file set or otherwise immutably bound to it. Material decision meaning must remain conformant across supported projections.

A projection change that alters material decision meaning is a material version change.

## History and carriers

Preserve historical releases/candidates/evidence as occurrence truth without forcing ordinary adopters to reconstruct history to determine Current.

Repository/carrier availability is an implementation dependency. Project continuity should not require one permanent session, Agent, validator, institution, or hosting vendor to remain forever available or correct.

> **Expose one adoption surface; preserve many historical surfaces.**
>
> **The carrier hosts the lineage; it is not the sovereign of the lineage.**
