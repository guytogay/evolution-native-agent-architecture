# 8. Release and Canonical-Lineage Discipline — v0.3.6 Current

Status: `CURRENT / FIELD_VALIDATION`.

A deployable ENA adoption version must be self-contained and immutably identifiable.

## Version identity

One adoption version identifies one immutable effective-content state.

`same ena_version -> same effective content`

Material change requires a new version/candidate identity. Research/candidates may branch; the adopter-facing Current remains singular.

`Git main != ENA Current`

## Candidate discipline

A candidate is a variation.

`candidate -> author attacks -> freeze -> independent falsification/validation -> targeted correction/revalidation where needed -> reconciliation -> release decision`

If a frozen candidate needs material correction, create a successor identity; do not silently edit the frozen effective-content tree.

A same-falsifier targeted revalidation may verify specific fixes when labeled honestly; it is not fresh independent validation.

Stop candidate succession when decision-changing residuals converge. Visible research questions are not automatic release blockers.

v0.3.6 followed this discipline:

- frozen candidate.0 received fresh independent semantic verdict `NEEDS_REVISION`;
- frozen candidate.1 repaired material findings;
- the same falsifier returned `TARGETED_REVALIDATION_PASS_WITH_RESIDUALS`;
- host-side reconciliation concluded `CANDIDATE_SUCCESSION_STOP = YES` and `RELEASE_PREPARATION_SUPPORTED`.

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

## Freeze identity

A freeze may be assigned by an external governed record to an exact already-tested immutable tree. The tested tree need not be rewritten merely to insert a post-hoc `frozen: true` marker.

The authoritative property is the exact source/tree binding plus governed lineage, not a mutable label inside the bytes being frozen.

## Source/distribution identity

A release must be built from identified committed source/effective-content bytes.

Release evidence may include source commit/tree, exact file set, byte/hash parity, package digest, and published artifact readback.

Ordinary adopters need the minimum sufficient immutable effective-content identity for what they actually compiled from; they need not reproduce release-author ceremony merely to use Current.

## Language projections

A supported language projection is part of the release file set or otherwise immutably bound to it. Material decision meaning must remain conformant across supported projections.

A projection change that alters material decision meaning is a material version change.

## Runtime/schema compatibility

A newer semantic baseline may retain an older reference-tool mechanism when all of the following are explicit:

- which semantic surface is normative;
- which runtime/tool version is actually implemented;
- which paths are unsupported or false-BLOCKed by the inherited tool;
- the gap is not silently turned into semantic law;
- no false claim of runtime parity is made.

`canonical semantic baseline != Host mechanism version`

## History and carriers

Preserve historical releases/candidates/evidence as occurrence truth without forcing ordinary adopters to reconstruct history to determine Current.

Repository/carrier availability is an implementation dependency. Project continuity should not require one permanent session, Agent, validator, institution, or hosting vendor to remain forever available or correct.

> **Expose one adoption surface; preserve many historical surfaces.**
>
> **The carrier hosts the lineage; it is not the sovereign of the lineage.**
