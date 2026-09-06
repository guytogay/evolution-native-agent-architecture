# 8. Release and Canonical-Lineage Discipline — v0.3.8-candidate.0

Status: `CANDIDATE / NOT_CURRENT / NOT_FROZEN / NOT_RELEASED`.

Released Current remains `v0.3.7 / CURRENT / FIELD_VALIDATION` under `../current/`.

A deployable ENA adoption version must be self-contained and immutably identifiable. Self-description, branch recency, or a successful local check does not create canonical release authority.

## Version identity

One released adoption version identifies one immutable effective-content state.

`same ena_version -> same effective content`

Material change to frozen/released effective content requires successor identity and explicit release decision.

```text
Git main != ENA Current
candidate branch != frozen identity
candidate exists != released
```

## Candidate discipline

A candidate is a governed variation:

`candidate -> author attacks/checks -> exact pre-freeze validation -> freeze -> fresh independent falsification/validation -> targeted correction/revalidation where legitimate -> reconciliation -> release decision`

Candidate.0 is mutable now. If it is later frozen and then requires material correction, create a successor candidate identity; do not silently rewrite the frozen effective-content tree.

A same-falsifier targeted revalidation may verify a specific fix when labeled honestly; it is not fresh independent validation.

Stop candidate succession when decision-changing residuals converge. Visible research questions are not automatic release blockers.

## v0.3.8 candidate birth

Candidate.0 was seeded from the released v0.3.7 Current subtree without changing `releases/current/`.

Working identity:

```text
candidate: v0.3.8-candidate.0
branch: candidate/v0.3.8-candidate.0
seed parent main: 8928693b746864dece2a66d625a01cbc328b0d7e
seed commit: 381f9fdf3d3233fee31d444b6e4bab1ec8c25fcd
source Current tree: f33e73ed997c1b66a4572685ab5474182e136e97
freeze identity: NONE YET
```

The successor scope is adoption/product-surface consolidation, initially driven by Issue #201 plus external usability/projection evidence. This evidence does not itself mint release status.

## v0.3.7 predecessor occurrence truth

Released v0.3.7 remains the singular Current while candidate.0 is being developed.

Its governed candidate.3/freeze/release history remains historical occurrence truth in repository lineage. Candidate.0 may inherit semantic/tool behavior from it but must not narrate predecessor candidate-state sentences as its own present state.

Historical candidate/freeze details belong in lineage/reconciliation records, not the ordinary adopter hot path.

## Canonical ENA evolution

ENA itself is evolvable, but one local Agent/fork cannot mint canonical status by self-description.

Canonical change requires durable lineage sufficient to establish:

- proposal/change identity;
- reviewable effective content;
- falsification/validation evidence;
- reconciliation/decision record;
- immutable version identity;
- recoverable/publicly inspectable history appropriate to the project;
- explicit promotion/admission event.

GitHub is the current project carrier for this lineage. The semantic requirement is governed reproducible lineage, not eternal dependence on one service.

## Current isolation

`releases/current/` remains the singular v0.3.7 adopter-facing surface during candidate.0 work.

Candidate development must not silently edit Current.

A future v0.3.8 promotion would require an explicit governed release operation that establishes the exact new effective-content identity and then makes the adopter-facing Current transition visible and unambiguous.

## Freeze identity

Candidate.0 uses the external-record freeze model:

- finish all material candidate bytes first;
- run exact-source machine validation;
- identify exact source commit and exact candidate subtree;
- record that binding in governed lineage;
- do not rewrite the tested candidate tree merely to insert a post-hoc `frozen: true` marker.

The authoritative freeze property is exact source/tree binding plus governed lineage.

## Source/distribution identity

A release must be built from identified committed source/effective-content bytes.

Release evidence may include:

- source commit/tree;
- exact file set;
- byte/hash parity;
- package digest;
- published artifact readback.

Ordinary adopters need the minimum sufficient immutable effective-content identity; they do not need to reproduce release-author ceremony.

## Language projections

Supported projections must bind to the same candidate/release identity.

Material decision meaning must remain conformant across supported languages.

```text
literal wording parity != decision parity
structural parity != behavioral equivalence
```

A decision-bearing projection defect discovered before freeze is candidate work. A material defect discovered after freeze must follow successor discipline rather than silent rewriting.

## Runtime/reference compatibility

A semantic baseline may retain older compatibility mechanisms only when their actual scope is explicit.

Candidate.0 inherits one primary practical v2 path:

`tools/ena_evolve_v2.py`

and keeps the inherited state/schema 1.2 tool under:

`tools/legacy/ena_evolve_v1_2.py`

Bundled optional references likewise do not become normative Host implementations merely by packaging.

`canonical semantic property != bundled reference implementation != Host mechanism`

## Product-surface release condition

Because candidate.0 is explicitly an adoption-surface successor, release review must include more than machine byte consistency.

It must ask whether:

- human/Agent entrypoints describe one coherent state;
- adopters can identify what to load without reading research history;
- soft/model guidance is not narrated as hard enforcement;
- supported language projections preserve decision-bearing hot semantics;
- conformance fixtures exercise high-value claims made by the adoption surface;
- simplification did not erase applicability or predecessor-valid machine behavior.

## History and carriers

Preserve historical releases/candidates/evidence as occurrence truth without forcing ordinary adopters to reconstruct history to determine Current.

Repository/carrier availability is an implementation dependency. Project continuity should not require one permanent session, Agent, validator, institution, or hosting vendor to remain forever available or correct.

> **Expose one Current; allow many candidates and historical surfaces.**
>
> **Research lineage is inspectable evidence, not default adoption payload.**
>
> **The carrier hosts the lineage; it is not the sovereign of the lineage.**
