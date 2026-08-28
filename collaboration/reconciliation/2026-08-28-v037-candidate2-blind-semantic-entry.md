# Fresh independent A-S / A-P entry — ENA v0.3.7 candidate.2

Status: `NEUTRAL_INTAKE / BLIND_A_S_FIRST / NOT_RELEASE_AUTHORITY`

You are acting as a **fresh independent validator** for one frozen ENA candidate.

You did not participate in its design, implementation, repair, adversarial fixture creation, author-side validation, freeze decision, or release decision.

## Exact target

Repository:

`guytogay/evolution-native-agent-architecture`

Frozen candidate identity:

`v0.3.7-candidate.2`

Exact frozen source commit:

`bda470e0a6b170cec61225a905957a501454a2fe`

Exact frozen candidate subtree:

`d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Candidate path:

`releases/v0.3.7-candidate/`

Blind semantic view branch:

`validation/v037-c2-blind-semantic-primary`

Blind-view manifest:

`collaboration/reconciliation/2026-08-28-v037-candidate2-blind-semantic-view.yaml`

The validation branch is an information-role projection of the frozen source. It is **not** a new candidate and is not release authority.

## Sequence

Perform exactly this sequence:

`A-S -> persist/seal A-S -> A-P -> persist A-P -> STOP`

Do not perform project-manager Phase B reconciliation.

## A-S — blind semantic falsification

Before the A-S report is persisted:

- inspect only candidate semantic bytes permitted by the blind-view manifest;
- obey ranged-read restrictions for mixed-role files;
- do not inspect files excluded by the manifest;
- do not inspect the full project-manager handoff, research reconciliation records, predecessor findings, repair narratives, author attack harnesses, expected fixtures, regression results, or other author-side oracle/context;
- do not infer correctness from candidate numbering, status wording, or the fact that this target was frozen;
- grow your own attack tree from the represented contracts and executable semantics you are allowed to inspect.

Independently look for at least these *classes of consequence*, without treating them as a finite checklist:

- false-confidence / false-claim cases the implementation permits;
- legitimate behavior the implementation falsely blocks;
- chronology/order dependence that changes a decision without a represented ordering rule;
- contradictions between duplicated represented facts;
- representation that appears stronger than the evidence it actually carries;
- migration/import/export transformations that silently change claim scope or provenance;
- authority/effect/recovery/wait composition seams that create unjustified permission, denial, replay, completion, or certainty;
- Host/applicability boundaries that are accidentally universalized;
- semantic prose/schema/tool disagreement;
- important open possibilities that should remain residual rather than being forced into a verdict.

Do not assume there is any particular number of findings. `ATTACK_CARDINALITY = OPEN`.

For every finding, distinguish where possible:

- deterministic candidate-byte defect;
- false-block / over-constraint;
- representation/evidence-boundary weakness;
- Host or external-truth boundary;
- intentional/open residual;
- uncertain branch requiring further evidence.

Persist the A-S report at:

`collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary.md`

Commit it to the validation branch and record the immutable commit SHA as the **A-S seal** before opening any A-P-only material.

## A-P — independent package / self-description / oracle audit

Only after A-S is sealed:

- you may inspect the files/ranges withheld by the blind-view manifest from the exact frozen source commit;
- audit full-package self-description, lineage consistency, fixtures, selftests, regression oracles, and package claims;
- compare those materials against your already-sealed A-S attack tree rather than allowing them to rewrite what you independently searched for;
- you may identify additional package/oracle defects discovered during A-P;
- do **not** consume project-manager repair maps or Phase-B reconciliation conclusions.

Persist the A-P report at:

`collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-p-primary.md`

Commit it to the same validation branch, then **STOP**.

## Required report discipline

Both reports must state:

- exact target identity/source/subtree;
- what information boundary was observed;
- whether any boundary was accidentally crossed;
- deterministic reproductions for material findings where feasible;
- legitimate counterexamples/false-block controls where relevant;
- unresolved branches that remain open;
- that successful tests or absence of findings do not close attack cardinality.

Do not modify:

- the frozen candidate bytes as a repair;
- `releases/current/`;
- release/promotion state.

If you discover that the blind view itself leaks predecessor findings, repair narratives, expected outcomes, or other material search-map priming before A-S seal, **stop and report the validation-interface defect instead of continuing a contaminated A-S**.

## Completion boundary

Your role ends when the A-P report is committed.

The project manager will later reconcile your independent artifacts against author-side evidence. You should not predict or perform that reconciliation.
