# Independent-validator priming incident — candidate.0 Phase A entry

Status: `METHOD_TRIGGER_EVIDENCE / VALIDATION_ROLE_BOUNDARY / NON_NORMATIVE_TO_CURRENT`

Date: `2026-08-27`

## Incident

After the v0.3.7 candidate.0 author-harness anti-ablation audit, the project correctly required a **fresh independent Phase A** before author-oracle comparison.

However, the first independent-validation handoff and PR #115 body supplied the fresh validator, before Phase A, with a detailed author-generated list of high-value attack surfaces and concrete examples covering routing, false-BLOCK pressure, representation/external truth, cross-organ seams, evolution migration, legacy compatibility, zh-CN semantics, hot/cold retrieval, deferred machinery, and candidate-scope economics.

The list was explicitly described as open-cardinality and not an expected-verdict oracle. Even so, it shaped where the validator would look before the validator had independently grown an attack space from the frozen implementation.

The methodological risk is:

```text
FRESH_REVIEWER
-> AUTHOR_SHAPED_SEARCH_PRIORS
-> INDEPENDENT_LABEL
-> SHARED_BLIND_SPOT_CAN_SURVIVE
```

This is weaker contamination than reusing expected verdicts, but it still matters when Phase A's purpose is to discover failure structure the author may not have imagined.

## Root distinction

The project had correctly strengthened **project-manager succession** so that a successor inherits state, method, governance, decision lineage, and next action.

That same richness is not automatically appropriate for a fresh validator before Phase A.

```text
PROJECT_MANAGER_TAKEOVER_CONTEXT
!=
FRESH_VALIDATOR_PRE_PHASE_A_CONTEXT
```

For the project manager, missing context causes continuity failure.
For the fresh validator, too much author-shaped context can cause independence failure.

## Correction

Introduce a minimal-prime blind Phase-A entrypoint that exposes only:

- exact frozen target identity;
- validator freshness/role boundary;
- information firewall against author/oracle surfaces;
- open-ended falsification task;
- minimal evidence discipline;
- requirement to persist Phase-A findings before Phase B.

Keep the original detailed independent-falsification handoff as **Phase-B context and lineage** rather than deleting or rewriting occurrence truth.

## New durable rule

```text
PROJECT_MANAGER_SUCCESSION -> MAXIMIZE_RELEVANT_CONTEXT_CONTINUITY
FRESH_VALIDATOR_PHASE_A     -> MINIMIZE_AUTHOR_SHAPED_PRIMING
PHASE_A_FINDINGS_PERSISTED  -> AUTHOR_CONTEXT_MAY_OPEN_FOR_PHASE_B
```

A reviewer already exposed to author oracles/attack construction cannot restore freshness by promising to ignore prior knowledge.

## Candidate boundary

This incident is a validation-method defect, not a demonstrated candidate-byte defect.

The frozen candidate remains:

```text
source = d0e793593184740d9732902e948afd48ed96ae2f
tree   = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

No candidate.1 is implied by this method correction.
