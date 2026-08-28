# 8. Release and Canonical-Lineage Discipline — v0.3.7

Status: `CURRENT / FIELD_VALIDATION / RELEASED`.

A deployable ENA adoption version must be self-contained and immutably identifiable. Candidate.3 is not Current and must not acquire release status by self-description.

## Version identity

One adoption version identifies one immutable effective-content state.

`same ena_version -> same effective content`

Material change requires a new version/candidate identity. Research/candidates may branch; adopter-facing Current remains singular.

`Git main != ENA Current`

`candidate branch != frozen identity`

## Candidate discipline

A candidate is a variation:

`candidate -> author attacks -> exact pre-freeze validation -> freeze -> fresh independent falsification/validation -> targeted correction/revalidation where needed -> reconciliation -> release decision`

If a frozen candidate needs material correction, create a successor identity; do not silently edit its frozen effective-content tree.

A same-falsifier targeted revalidation may verify specific fixes when labeled honestly; it is not fresh independent validation.

Stop candidate succession when decision-changing residuals converge. Visible research questions are not automatic release blockers.

### v0.3.7 candidate.3 current state

Candidate.3 succeeds frozen candidate.2 because candidate.2 fresh A-S/A-P plus Phase B found decision-changing executable defects and package provenance/self-description defects. Candidate.2 remains immutable occurrence truth; candidate.3 repairs only the bounded successor scope and does not reopen `releases/current/`.

Candidate.2 A-S SHA-256: `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`.

Candidate.2 A-P SHA-256: `80987d24a80c2aff90fddd96bc1891ee03c6ac02b25381d8af2a22418ebbe1db`.

Candidate.2 Phase-B disposition: `NEEDS_REVISION / CANDIDATE_3_REQUIRED`.

Candidate.2 frozen source/subtree: `bda470e0a6b170cec61225a905957a501454a2fe` / `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`.

Candidate.3 Round-1 repair gate `33149597432` passed at cargo `55e08740fa2e4b033cfb5bd9e8f7a4214a479f08` with inherited valid composed-validator behavior preserved. Round-2 reconciles package identity/lineage/zh-CN status without expanding executable semantics.

### Predecessor v0.3.7 candidate.2 preserved state

Candidate.2 passed exact pre-freeze machine validation and was externally frozen without rewriting its tested bytes. Fresh A-S/A-P then required candidate.3; its frozen tree must not be edited in place.

### Predecessor v0.3.7 candidate.1 preserved state

Candidate.1 passed exact pre-freeze machine validation, was externally frozen without rewriting its tested bytes, then failed fresh A-S/A-P independent falsification. Its frozen tree must not be edited in place.

### Predecessor v0.3.7 candidate.0 preserved state

Candidate birth base:

`0ad263178ab8b7c21c150012b3c06a5c41a4f41c`

That main commit contains the merged release-scope checkpoint and version selection before candidate bytes were authored.

Candidate.0 has assembled:

- release-local Operational Architecture routing;
- optional reference library with machine-readable default-off policy;
- candidate-local minimal v2 evolution helper with explicit v1.2 legacy demotion;
- decision-bearing zh-CN Operational Architecture projection and paired v3 route fixtures.

At that historical candidate.0 pre-freeze point, assembly machine checks had passed on recorded exact heads while the workspace was still mutable and self-described `NOT_CURRENT / NOT_FROZEN / NOT_RELEASED`. Later external freeze/succession records, not this preserved historical sentence, establish canonical predecessor state.

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

`releases/current/` is still v0.3.6 and must not be edited as a side effect of candidate assembly.

A material Current change requires a new release identity and explicit release decision.

Candidate validation therefore checks Current isolation against the exact release-scope checkpoint.

## Freeze identity

Candidate.0 uses the external-record freeze model:

- finish all material candidate bytes first;
- run exact-source machine validation;
- identify exact source commit and exact `releases/v0.3.7-candidate/` subtree;
- record that binding outside the candidate subtree in governed lineage;
- do not rewrite the tested candidate tree merely to insert a post-hoc `frozen: true` marker.

The authoritative freeze property is exact source/tree binding plus governed lineage.

Candidate.2 material corrections required candidate.3. Any material correction after candidate.3 freeze would require a new successor identity; candidate.4 is not an automatic validation step.

## Source/distribution identity

A release must be built from identified committed source/effective-content bytes. Release evidence may include source commit/tree, exact file set, byte/hash parity, package digest, and published artifact readback.

Ordinary adopters need the minimum sufficient immutable effective-content identity; they need not reproduce release-author ceremony.

## Language projections

Supported projections must be immutably bound to the same candidate/release identity. Material decision meaning must remain conformant across supported languages.

Candidate.3 retains the zh-CN operational decision surfaces and v3 paired route fixtures. Fixture structure/parity does not prove behavioral equivalence; actual model/Host evidence is still required.

## Runtime/reference compatibility

A semantic baseline may retain older compatibility mechanisms only when their actual scope is explicit.

Candidate.3 exposes one primary practical v2 path:

`tools/ena_evolve_v2.py`

and keeps the inherited state/schema 1.2 tool only under:

`tools/legacy/ena_evolve_v1_2.py`

Bundled optional reference schemas likewise do not become normative Host implementations merely by being packaged.

`canonical semantic property != bundled reference implementation != Host mechanism`

## History and carriers

Preserve historical releases/candidates/evidence as occurrence truth without forcing ordinary adopters to reconstruct history to determine Current.

Repository/carrier availability is an implementation dependency. Project continuity should not require one permanent session, Agent, validator, institution, or hosting vendor to remain forever available or correct.

> **Expose one Current; allow many candidates and historical surfaces.**
>
> **The carrier hosts the lineage; it is not the sovereign of the lineage.**
