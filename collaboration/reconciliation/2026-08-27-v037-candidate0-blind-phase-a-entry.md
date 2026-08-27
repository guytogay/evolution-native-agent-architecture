# ENA v0.3.7 candidate.0 — Blind Phase A entry

Status: `FRESH_INDEPENDENT_PHASE_A / MINIMAL_PRIMING / DO_NOT_MERGE / NOT_RELEASE_AUTHORITY`

Date: 2026-08-27

## Purpose

This is the **pre-Phase-A entrypoint** for a fresh independent validator.

Its job is deliberately different from a project-manager handoff.

```text
PROJECT_MANAGER_TAKEOVER
= STATE + METHOD + GOVERNANCE + DECISION_LINEAGE + NEXT_ACTION

FRESH_VALIDATOR_PHASE_A
= EXACT_TARGET + ROLE_BOUNDARY + MINIMAL_TASK_CONTRACT
```

A project manager should inherit the whole project. A fresh validator should not be primed with the author's attack taxonomy, expected outcomes, reconciliation narrative, or validation oracle before independently inspecting the target.

## Exact target

Inspect only this frozen candidate identity for Phase A:

```text
candidate identity = v0.3.7-candidate.0
source commit      = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree  = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
subtree path       = releases/v0.3.7-candidate/
```

The mutable candidate branch head is not the review identity.

Current remains v0.3.6. This review does not authorize release, promotion, or Current mutation.

## Freshness requirement

The Phase-A validator must not have participated in or materially relied on:

- candidate.0 design or assembly;
- author adversarial fixture/oracle creation;
- acceptance-semantics decisions;
- pre-freeze reconciliation;
- the 1080 -> 188 anti-ablation audit;
- earlier author-side expected verdicts or summaries.

Prior exposure cannot be undone by promising to ignore it. A previously exposed reviewer may contribute later analysis, but must not label that work `FRESH_INDEPENDENT_PHASE_A`.

## Information firewall before Phase A is sealed

Before persisting the Phase-A report, do **not** read or rely on:

- `.github/scripts/v037_candidate_author_attacks.py`;
- `.github/scripts/v037_candidate_anti_ablation.py`;
- `.github/workflows/v037-candidate-prefreeze.yml` or other author validation workflows as semantic oracles;
- `collaboration/reconciliation/2026-08-27-v037-candidate0-author-attacks.md`;
- `collaboration/reconciliation/2026-08-27-v037-candidate0-author-harness-anti-ablation-audit.md`;
- `collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md`;
- author-generated expected verdicts, fixture expectations, green-run interpretations, or candidate acceptance narratives;
- prior PR #115 discussion/review content that reveals author-side attack expectations, if such discussion later exists.

Do not browse the surrounding candidate branch for hints. Read the exact frozen candidate subtree directly.

Candidate-local prose, schemas, tools, references, fixtures, and examples are part of the target and may be inspected because the task is to evaluate what the candidate itself presents to adopters. However, a candidate-local expected fixture must not automatically become the validator's truth oracle.

## Phase A task

Inspect the frozen candidate as if encountering it without author guidance.

Independently determine:

- what material claims the candidate bytes appear to make;
- what actions or decisions a real adopter/Agent could take from them;
- what could make those claims/actions wrong, unusable, overconfident, over-restrictive, incomplete, or misleading;
- what legitimate behavior a validator must avoid falsely blocking;
- what important uncertainty remains undecidable from the package alone.

There is **no required attack taxonomy, fixture count, mechanism count, or finding count**.

```text
AUTHOR_KNOWN_ATTACK_SPACE != POSSIBLE_ATTACK_SPACE
CURRENTLY_IMAGINED_FAILURES != COMPLETE_FAILURE_SPACE
```

Let attack/failure branches grow from the implementation. Do not force findings into predeclared categories merely for presentation symmetry.

## Evidence discipline

For every material finding, distinguish what was actually observed or derived from what would require external evidence.

Useful distinctions include, when they fit the evidence:

```text
PROSE_PRESENT
STRUCTURALLY_REPRESENTED
MACHINE_GUARDED
EXECUTED
EXTERNALLY_OBSERVED
```

and:

```text
DEFINED
APPLICABLE
IMPLEMENTED
ACTIVE
EVIDENCED
```

These are precision aids, not a mandatory ontology.

Prefer deterministic/static reproduction where the failure is derivable. Do not add stochastic experiments merely to make the review look empirical.

## Required Phase-A artifact

Before reading Phase-B material, persist a Phase-A-only report containing at least:

1. role declaration and freshness statement;
2. exact frozen source/subtree inspected;
3. independently derived candidate claims or operational expectations that were tested;
4. material findings with concrete reproduction/evidence;
5. legitimate-behavior / false-BLOCK controls discovered independently;
6. unresolved questions and what evidence could change them;
7. any new attack branches suggested by the implementation that were not fully resolved.

Do **not** force a final candidate verdict in Phase A. The point is to freeze independent observations before author evidence can reshape them.

## Phase-A seal

Phase A is complete only when its report is durably persisted with an immutable commit/content identity.

```text
INDEPENDENT_INSPECTION
-> PERSIST_PHASE_A_FINDINGS
-> ONLY_THEN_OPEN_PHASE_B_CONTEXT
```

After the seal, Phase B may consult the author-side handoff, author harnesses, pre-freeze evidence, reference selftests, language fixtures, anti-ablation audit, and reconciliation history.

## Phase B pointer

After Phase A is sealed, use:

`collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md`

That document is intentionally **Phase-B context**, not the blind Phase-A entrypoint.

## Release boundary

This entrypoint grants no release authority.

Until governed reconciliation says otherwise:

```text
CURRENT = v0.3.6
FROZEN_CANDIDATE = v0.3.7-candidate.0
CURRENT_CHANGE = NO
```
