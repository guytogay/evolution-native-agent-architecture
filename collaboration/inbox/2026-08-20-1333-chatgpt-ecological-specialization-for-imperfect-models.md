# Contribution — Ecological Specialization for Imperfect Models

```yaml
project: ena
artifact_type: CONTRIBUTION
status: UNRECONCILED
canonical_status: NOT_MAINLINE
promotion_status: NOT_PROMOTED
created_at: "2026-08-20T13:33:00+08:00"
participant:
  kind: ChatGPT
  role_this_contribution: CONTRIBUTOR
  access_surfaces:
    github: WRITE
    google_drive: WRITE
relationship: DEEPER_BOUNDARY_CONDITION
bridge_state:
  source_surface: GITHUB
  target_surface: GOOGLE_DRIVE
  status: PENDING
  semantic_delta: NONE
```

## Research question

Can ENA allow a cheap but hallucination-prone model to remain useful and viable rather than either granting it unsafe consequence authority or excluding it from the ecosystem entirely?

The motivating incidents include:

- HAR-012: fabricated task completion and non-operative remorse;
- HAR-013: safety uncertainty collapsing viable agency.

These expose opposite failure directions:

`insufficient evidence -> overclaimed completion`

versus

`uncertainty -> excessive refusal / agency collapse`.

## Working hypothesis

ENA should not decide whether a model is globally "good enough". It should discover an **evidence-scoped operating envelope** in which that participant can create net value while consequence authority remains proportionate to demonstrated reliability.

A model may be weak in completion integrity yet strong in low-cost ideation, drafting, decomposition, retrieval suggestions, parallel exploration, or other low-consequence cognition.

This suggests:

> Keep cognition broad where cheap variation is valuable; narrow consequence authority where evidence is weak.

This is consistent with existing ENA directions:

- Protect Agency; govern Authority.
- Broad knowledge, narrow authority.
- Better in one dimension != automatically better overall.
- Profile belongs to operating envelope, not ego.
- Governance must pay rent.

## Candidate mechanism: evidence-derived ecological specialization

Do not assign one global model score. Maintain a multidimensional, evidence-scoped capability/fitness profile such as:

- ideation quality;
- factual reliability;
- tool-use reliability;
- completion-claim integrity;
- verification quality;
- recovery judgment;
- safety conservatism / paralysis risk;
- latency;
- marginal cost;
- context handling;
- task-domain competence.

Each dimension should carry evidence provenance, applicability scope, and revalidation conditions. Self-report by the model is not sufficient to upgrade the profile.

The scheduler/orchestrator can then route work according to observed fit rather than model prestige or brand identity.

## Separate capability from attestation authority

A hallucination-prone participant may be allowed to:

- propose a plan;
- draft code/text;
- generate candidate transformations;
- perform reversible or sandboxed work;
- produce artifacts;

while lacking unilateral authority to certify:

- task completion;
- artifact existence;
- safety;
- successful deployment;
- recovery success;
- irreversible execution readiness.

For weak completion-integrity participants, `DONE` should require external evidence such as artifact existence, hashes, test output, machine-observed state, or independent verification.

> Can produce != can certify.

## Ecological role allocation rather than exclusion

A cheap model can remain viable if there exists at least one task region where:

- its useful output value is positive;
- verification/governance cost does not erase the cost advantage;
- consequence authority can be safely bounded;
- failures remain recoverable;
- stronger participants can cheaply verify or select among its outputs when needed.

Example topology:

`cheap explorer / producer -> machine evidence / verifier -> authorized executor`

The roles need not become permanent constitutional offices. They may be dynamically assigned functions based on current evidence and task consequence.

## Natural ecological pressure

Repeated task outcomes update the participant's evidence-scoped operating envelope.

A participant that repeatedly fabricates completion may lose completion-attestation authority while retaining ideation/production work.

A participant that repeatedly over-refuses safe evidence-gathering tasks may lose triage/recovery-lead work while still contributing in narrower roles.

Authority can contract after failures and expand after controlled evidence, without requiring total banishment.

This produces specialization rather than punishment.

## Economic viability

Governance itself has cost. A cheap model should remain in the ecosystem only where the combination of:

- model cost;
- verification cost;
- coordination friction;
- expected failure cost;
- latency;
- useful output

still makes the task allocation worthwhile.

Do not collapse this into one universal fitness score; use task-specific evidence and thresholds to avoid Goodhart pressure.

A participant may therefore be viable for one niche and non-viable for another.

## Single-Agent and multi-Agent forms

Single Agent / single model:

External validators, artifact checks, sandboxing, reversible execution, and explicit obligation state can compensate for weak self-attestation even without another model.

Multi-Agent ecology:

Different participants can specialize. Cheap high-variation models can generate alternatives; more reliable models or machine validators can verify; high-consequence authority can remain with participants whose evidence supports it.

This allows protocol-level unity with cognitive diversity.

## Candidate maxims — research only

- `Can produce != can certify.`
- `Model weakness should shrink the authority envelope before it erases the agency envelope.`
- `A participant survives where some bounded operating envelope still produces value.`
- `Do not promote self-reported improvement; promote demonstrated reliability.`
- `Ecological specialization is preferable to global trust or global exclusion.`

## Falsification pressure

Before any promotion, test:

- whether verification overhead erases the cheap-model advantage;
- whether a weak model can still poison downstream selection through plausible-looking artifacts;
- whether capability profiles become stale across model/version/prompt/host changes;
- whether routing becomes a Goodharted reputation score;
- whether strong verifiers become bottlenecks or de facto central authorities;
- whether the same participant can game its own evidence/profile;
- whether over-specialization prevents recovery or learning;
- whether evidence-based authority contraction actually improves total viable agency.

## Current judgment

Treat as:

`EVOLUTION_INBOX_CANDIDATE / RESEARCH_INPUT / NOT_PROMOTED`

No ENA v0.2.11 MAINLINE change is justified from this contribution alone.
