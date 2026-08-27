# ENA Project Management Discipline

Status: `CANONICAL_CROSS_SESSION_PROJECT_MANAGEMENT_METHOD / MAIN_VISIBLE / NOT_ENA_CURRENT`

This file holds project-management rules that must survive individual session replacement.

It is deliberately outside any one handoff record because reusable management method is not a property of one historical snapshot.

```text
HANDOFF_RECORD = OCCURRENCE / SNAPSHOT
PROJECT_MANAGEMENT_DISCIPLINE = REUSABLE METHOD
```

## 1. Project continuity outranks session continuity

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
```

No project state, method, evidence, decision, or unresolved branch should depend on one conversational session remaining healthy.

## 2. Project state and project method are equally inheritable

A successor who knows only "where we are" but not "how we learned to decide" is not fully onboarded.

```text
TAKEOVER = STATE + METHOD + GOVERNANCE + DECISION LINEAGE + NEXT ACTION
```

The handoff/takeover framework lives under `research/handoffs/`.

The ENA research methodology lives under `research/methodology/`.

Both are mandatory takeover context for a project-manager/session successor.

## 3. Handoff framework and handoff records must not be mixed

The root `research/handoffs/` contains reusable succession framework.

`research/handoffs/records/<handoff-id>/` contains one time-bounded handoff occurrence.

Reusable lessons discovered during an occurrence must be promoted to framework or project methodology.

```text
INSTANCE_DISCOVERS_METHOD
-> PROMOTE_METHOD
-> KEEP_INSTANCE_AS_EVIDENCE
```

Do not leave generic rules trapped inside one dated/frozen record.

## 4. Project-state alignment is a first-class transition operation

A file can have been correct when written and still become stale after later transitions.

```text
INDIVIDUAL_FILE_CORRECT_AT_T
!=
PROJECT_STATE_COHERENT_AT_T_PLUS_1
```

After material phase, branch, candidate, freeze, release, methodology, or handoff transitions, use:

`research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md`

Do not use a new handoff summary to paper over stale canonical control-plane files.

## 5. Reverify live state before writing

Cached SHAs, old PR identities, chat summaries, and directory recency are not live authority.

Before material writes, reverify the relevant branch/ref and exact governed identities.

```text
BRANCH_HEAD_AT_T != BRANCH_HEAD_NOW
BRANCH_HEAD != FROZEN_IDENTITY
```

## 6. Preserve occurrence truth

When a validator, oracle, workflow, or project-manager interpretation is wrong, preserve that occurrence and correct the method or successor state.

```text
VALIDATOR_FAILURE != CANDIDATE_FAILURE
VALIDATOR_PASS != EXTERNAL_TRUTH
```

Separate at least:

- candidate/product defect;
- packaging/navigation defect;
- oracle defect;
- infrastructure failure;
- evidence gap;
- project-state projection drift.

## 7. Frozen identity remains immutable lineage

A frozen candidate is identified by exact source/tree binding, not by a mutable branch head.

Do not modify validated/frozen bytes merely to add narration such as `frozen: true` and then pretend the changed bytes are the validated object.

If material candidate-byte correction is required:

```text
candidate.0 remains frozen occurrence truth
-> candidate.1
```

A research residual alone does not require candidate succession.

## 8. Compression and growth must occur at the right layer

LLMs tend to narrate success as summarization and convergence.

ENA requires explicit discrimination:

```text
WHAT / WHY
-> abstraction/compression may help

HOW
-> concretize / branch / recombine

FAILURE / ADVERSARIAL SPACE
-> expand while materially distinct shapes remain plausible

REPRESENTATION DUPLICATION
-> may compress after equivalence is established
```

Canonical focused method:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

Key invariant:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
```

## 9. Growth also pays complexity rent

Anti-convergence is not a license to maximize file, role, test, branch, or category count.

A new artifact or branch should earn its complexity through distinct behavioral, evidential, governance, or continuity value.

```text
ANTI_CONVERGENCE != MAXIMIZE_ARTIFACT_COUNT
```

## 10. Optional packaging must remain optional

Bundling a reference, procedure, or organ does not make it mandatory at runtime.

```text
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
PACKAGE_INCLUDED != APPLICABLE
```

Project management must resist accidental bureaucracy created by packaging richness.

## 11. Exact next action may be singular while possibility space remains plural

Operational sequencing can select one next project-management action without claiming only one mechanism/failure branch exists.

```text
PLURAL_POSSIBILITY_SPACE
AND
ONE_NEXT_EXECUTION_STEP
```

This is scheduling, not ontological convergence.

## 12. Handoff is applied behavior, not document production

A handoff succeeds only when a successor actually retrieves, verifies, interprets, and applies state and method.

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

If the successor can quote the handoff but still asks the user to reconstruct persisted background, treats branch recency as authority, skips required method, or collapses unproven variation, inheritance failed.

## 13. Project-manager succession and fresh-validator briefing are different jobs

The full handoff framework is designed to prevent project-manager context loss. It must not be mechanically reused as the pre-Phase-A briefing for a fresh independent validator.

```text
PROJECT_MANAGER_SUCCESSION
-> MAXIMIZE_RELEVANT_CONTEXT_CONTINUITY

FRESH_VALIDATOR_PHASE_A
-> MINIMIZE_AUTHOR_SHAPED_PRIMING
```

A different person/model/Agent is not automatically search-space independent if the author gives it the author's detailed attack taxonomy before it has inspected the target.

For fresh independent validation:

```text
EXACT_TARGET + ROLE_BOUNDARY + MINIMAL_TASK
-> INDEPENDENT_PHASE_A
-> PERSIST / SEAL FINDINGS
-> OPEN_AUTHOR_CONTEXT_FOR_PHASE_B
```

The project manager should prepare and route the role-scoped entrypoint, but should not send the fresh validator through the full project-manager handoff first.

A reviewer already materially exposed to author oracle/attack construction may still contribute Phase B, oracle auditing, or reconciliation, but cannot restore `FRESH_INDEPENDENT_PHASE_A` status merely by promising to ignore what it has read.

Canonical focused method:

`research/methodology/INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md`

This is not a general rule that "less information is better". It is an ordering rule: rich author context is delayed until after independent observations are durably captured.

## 14. Promoted lessons from the 2026-08-27 succession

The standardized succession work exposed several durable lessons:

- `research/ACTIVE-RESEARCH.yaml` and `PROGRESS.yaml` can drift behind actual candidate/freeze state; alignment must precede succession.
- the author's initial claim that reducing an observed 1080 pass conditions to 188 was "better" was not justified without anti-ablation lineage; assertion count is not epistemic coverage.
- false-positive validation oracles should be repaired without rewriting occurrence truth.
- frozen candidate identity must remain external and content-addressed.
- handoff framework/method must not be buried inside a dated record.
- outgoing and incoming succession rules have equal continuity importance.
- project-manager context completeness and fresh-validator pre-Phase-A information hygiene have different optimization directions.

Historical occurrence evidence remains in the dated handoff records and collaboration/reconciliation records. This file carries the reusable method forward.
