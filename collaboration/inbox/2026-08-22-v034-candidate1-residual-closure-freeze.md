# ENA v0.3.4-candidate.1 — Residual-Closure Semantic Freeze

Date: 2026-08-22

Status: `FROZEN_CORRECTED_IMPLEMENTATION_CANDIDATE / AWAITING_PRIOR_FALSIFIER_TARGETED_REVALIDATION / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`

## Frozen target

Repository:
`guytogay/evolution-native-agent-architecture`

Candidate path:
`releases/v0.3.4-candidate.1/`

Authoring branch:
`candidate/v0.3.4-runtime-internalization`

Frozen semantic candidate.1 commit:
`4518eeee9405c0b784401b6960dd36fee500a84f`

Frozen candidate.1-directory Git tree:
`4e6642b5c17342fe51d932d67764643c383aba82`

Branch-integration merge preserving both candidate.1 authoring and the transient freeze-record edit history:
`b2cd35c597180625b79088194ccf69b8364911e7`

Independent validation evidence-summary commit:
`7d22928cfd56214cadf955ebf614103a09d8f2eb`

## Predecessor preserved

Original frozen candidate remains:

- path: `releases/v0.3.4-candidate/`
- semantic commit: `ccc66233c1abe6778177a38950af1f7bb2356b93`
- candidate-directory tree: `61cb33562626c3b8f590919c87f4637416f1ee8f`
- freeze record commit: `d4ce9ebff0f83f47090ffea8e44be9bdd6eb7f68`
- independent verdict: `INDEPENDENT_RUNTIME_ADOPTION_VALIDATION_SUPPORTED_WITH_RESIDUALS`

The original candidate directory and its freeze record are not relabeled as candidate.1.

## Why a successor identity is required

The independent validator recommended two changes before promotion:

1. close D14 by binding the persisted Compiled Local Projection to an immutable canonical source identity and adding source-identity drift/revalidation triggers;
2. close D2 by strengthening cross-session persistence claims so a current-session persistence write cannot be relabeled fresh-session adoption without actual-boundary evidence.

Those are material adoption/runtime semantic changes to an already frozen candidate. ENA release/candidate integrity therefore requires a successor candidate identity instead of mutating the frozen original in place.

## candidate.1 correction scope

The successor changes only adoption/runtime identity and the D14/D2 closure surfaces:

- `00-READ-ME-FIRST.md`
- `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`
- `07-ADOPTION-AND-FIELD-VALIDATION.md`
- `AGENT-ADOPTION-INSTRUCTION.md`
- `CANDIDATE-BASELINE.yaml`
- `CHANGELOG.md`
- `LINEAGE.md`
- `LITE-ADOPTION-INSTRUCTION.md`
- `README.md`
- `RUNTIME-ADOPTION-KERNEL.md`

The following inherited high-value surfaces remain the exact original-candidate/v0.3.3 blobs by construction:

- Constitution;
- roles/developmental stages;
- capability map;
- core operational contracts;
- evolution/open-participation document;
- release discipline;
- contribution protocol;
- schemas tree;
- templates tree;
- tools tree including validator, fixtures and regression runner.

No new claim-pack validator/schema mechanism is introduced.

## D14 closure semantics

The Compiled Local Projection now distinguishes:

- human-readable ENA version/candidate label;
- **immutable canonical source identity actually compiled from** (for example Git commit/tree identity or package digest).

A mutable branch or version label alone is explicitly insufficient as a source-integrity anchor.

The cold path now includes source-identity change/conflict/unconfirmability when it can change the decision.

If a Host persists a transformed/paraphrased Runtime Kernel, source/transformation lineage must be preserved; successful storage alone is not semantic-fidelity proof.

The concrete immutable digest is not self-referentially embedded inside the candidate. It is supplied by freeze/distribution evidence and recorded by the adopter at compilation time.

## D2 closure semantics

Before claiming that ENA adoption survives a fresh-session or equivalent decision-critical boundary, the actual claimed boundary must be evidenced.

A current-session memory/configuration write proves only the narrower fact that the persistence object was written. It does not by itself prove that a genuinely fresh session receives, interprets and applies it.

If the claimed persistence scope is narrower, the claim must stay narrow.

## Deliberate residual

The independent validator's optional self-hosted recovery-root hardening suggestion is not promoted into this immediate correction. It remains a residual/field-validation concern unless further evidence makes it decision-worthy.

The genuine fresh-session persistence experiment also remains open evidence work. candidate.1 fixes false-claim semantics; it does not manufacture cross-session evidence on a Host that cannot perform the test.

## Transient authoring incident preserved truthfully

During successor authoring, a GitHub contents-API call briefly created a parallel commit that modified the original candidate freeze record (`d3aafd0ab23cb33a4cfbb59c8be54e6f4b9a13dc`) before the candidate.1 authoring commit had been attached to the branch.

The incident was reconciled by merge commit `b2cd35c597180625b79088194ccf69b8364911e7`, whose final tree restores the original freeze-record blob exactly and includes candidate.1. The transient commit remains visible in Git history; occurrence truth is not erased.

This authoring incident did not change either frozen candidate directory tree.

## Revalidation target

Next actor:
`PRIOR_INDEPENDENT_RUNTIME_ADOPTION_FALSIFIER_TARGETED_REVALIDATION`

The same WorkBuddy validator that found D14/D2 should now independently verify:

1. original frozen candidate/freeze bytes remain recoverable and candidate.1 uses a new identity;
2. candidate.1 directory tree equals `4e6642b5c17342fe51d932d67764643c383aba82`;
3. D14 source-integrity drift is closed without self-referential hash semantics;
4. D2 cross-session claim-strength gap is closed;
5. no new false escalation/de-escalation, reread ritual, false persistence, or recovery overclaim is introduced;
6. inherited validator/schema/tooling semantics remain unchanged;
7. `PERSISTENCE_TEST_UNAVAILABLE` stays an honest experiment limitation if that Host still cannot cross the boundary.

A fresh new validator is not required merely to re-check the prior falsifier's own findings.

Final freeze state:

`v0.3.4-candidate.1 / FROZEN / AWAITING_TARGETED_REVALIDATION / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`
