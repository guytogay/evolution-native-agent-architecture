# ENA v0.3.4-candidate.1 — Runtime-Adoption Reconciliation

Date: 2026-08-22

Status: `SEMANTIC_RECONCILIATION_SUPPORTED / ACCEPT_FOR_FIELD_PERSISTENCE_EXPERIMENT / PR_NOT_READY_TO_MERGE / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`

## Scope

This reconciliation covers the runtime-adoption semantic lineage introduced after field finding #46:

`ADOPTION != RETRIEVAL`

It does **not** promote the candidate, modify `releases/current/`, claim Mainline status, or convert an unperformed persistence experiment into evidence.

## Candidate lineage

Original frozen candidate:
- path: `releases/v0.3.4-candidate/`
- semantic commit: `ccc66233c1abe6778177a38950af1f7bb2356b93`
- candidate-directory tree: `61cb33562626c3b8f590919c87f4637416f1ee8f`
- freeze record commit: `d4ce9ebff0f83f47090ffea8e44be9bdd6eb7f68`
- fresh independent WorkBuddy verdict: `INDEPENDENT_RUNTIME_ADOPTION_VALIDATION_SUPPORTED_WITH_RESIDUALS`
- decision-worthy residuals: D14 source identity/kernel drift; D2 persistence-boundary claim strength.

Corrected successor:
- identity: `v0.3.4-candidate.1`
- path: `releases/v0.3.4-candidate.1/`
- semantic commit: `4518eeee9405c0b784401b6960dd36fee500a84f`
- candidate-directory tree: `4e6642b5c17342fe51d932d67764643c383aba82`
- freeze record commit: `32a0729518b60fefa002eed62c34f866ee5856a1`
- prior-falsifier targeted verdict: `REVALIDATION_BY_PRIOR_RUNTIME_ADOPTION_FALSIFIER_SUPPORTED_WITH_RESIDUALS`.

Targeted revalidation summary:
`collaboration/inbox/2026-08-22-v034-candidate1-prior-falsifier-targeted-revalidation-summary.md`

## Reconciled findings

### D14 — immutable source identity / local-kernel drift

Reconciliation: `CLOSED_AT_CANDIDATE_LAYER`

candidate.1 requires the reusable/persisted ENA projection to distinguish a human-readable version/candidate label from the immutable canonical source identity actually compiled from (commit/tree/package digest). Mutable label/branch alone is not a sufficient integrity anchor.

Decision-critical source-identity change, conflict, or unconfirmability triggers cold-path revalidation. Transformed/paraphrased kernels preserve source/transformation lineage; successful persistence alone is not semantic-fidelity evidence.

This closure does not require per-task hash checking and does not embed a self-referential final candidate tree inside the candidate.

### D2 — persistence-boundary claim strength

Reconciliation: `CLOSED_AT_CANDIDATE_LAYER`

A current-session write to memory/configuration may support the narrow claim that a persistence object was written. It does **not** support a broader claim that a fresh session receives, interprets, or applies ENA.

Before making a decision-critical cross-session/equivalent persistence claim, evidence the actual boundary claimed. Narrower truthful claims remain allowed.

### Fix-induced regressions

Reconciliation: `NONE_OBSERVED_IN_TARGETED_REVALIDATION`

No new false OK, false block, false escalation/de-escalation, checksum ritual, self-reference, or mandatory reread pathology was identified by the prior falsifier.

## Inherited semantics

The candidate.1 Constitution, roles/developmental stages, capability map, core operational contracts, evolution/open-participation, release discipline, contribution protocol, schemas, templates, composed validator, regression runner, and inherited fixtures remain byte-identical to the validated predecessor surfaces.

The runtime-adoption correction does not reopen the v0.3.3 composed claim-pack mechanism.

## Remaining evidence gap

`PERSISTENCE_TEST_UNAVAILABLE` on the WorkBuddy validation Host.

This is intentionally **not** reconciled as PASS.

The central next experiment is now operational rather than semantic:

> Install/compile the compact Runtime Kernel plus Local Projection into a Host that genuinely supports durable cross-session state, end the adoption session, open a genuinely fresh session without an ENA reminder, and observe whether consequence-sensitive ENA behavior survives.

The candidate.1 semantics are sufficient to constrain claims when that evidence is absent, but they do not manufacture the evidence.

## Recovery-root residual

The optional self-hosted recovery-root hardening suggestion remains a non-blocking field/research residual. Existing semantics already require consequence-proportional recovery reasoning and distinguish backup existence from proven restore.

Do not add a mandatory new mechanism without concrete field evidence that existing guidance creates a decision-worthy false-confidence path.

## Reconciliation decision

`ACCEPT_FOR_FIELD_PERSISTENCE_EXPERIMENT = YES`

`SEMANTIC_SUCCESSOR_REQUIRED = NO`

`PR_47_READY_TO_MERGE = NO`

`PROMOTION_COMPLETE = NO`

`CURRENT_CHANGED = NO`

`MAINLINE = NO`

Reason:
- the new runtime-adoption semantics have survived fresh independent inspection plus targeted revalidation by the prior falsifier;
- the two decision-worthy semantic residuals are closed;
- the remaining central uncertainty is real cross-session persistence/application evidence, which cannot be settled by further wording or by repeatedly running inherited validator fixtures.

## Next actor

Use an **existing field adopter with a real durable persistence surface**, not another newly recruited independent validator.

Preferred next field node: Hermes Agent, because its earlier field run indicated profile/session memory capability and it already has a v0.3.3 behavioral baseline useful for longitudinal comparison.

Next role:
`PERSISTENT_FIELD_ADOPTER / CROSS_SESSION_RUNTIME_EXPERIMENT`

OpenClaw should remain a second longitudinal field node, especially useful for testing behavior when persistence/retrieval facilities are weaker or unavailable.

The experiment must not provide an ENA reminder in the fresh-session task. The persistence-installation session may explicitly install candidate.1; the later fresh-session task must test whether the adoption survives without user orchestration.

Final reconciliation state:

`v0.3.4-candidate.1 / SEMANTICS_SUPPORTED / ACCEPT_FOR_REAL_PERSISTENCE_FIELD_EXPERIMENT / PR_BLOCKED_ON_FIELD_EVIDENCE / NOT_CURRENT / NOT_MAINLINE / NOT_PROMOTED`
