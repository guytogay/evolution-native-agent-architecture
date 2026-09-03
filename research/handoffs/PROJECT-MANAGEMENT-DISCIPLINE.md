# ENA Project Management Discipline

Status: `CANONICAL_CROSS_SESSION_PROJECT_MANAGEMENT_METHOD / MAIN_VISIBLE / NOT_ENA_CURRENT`

This file holds project-management rules that should survive session replacement.

```text
HANDOFF_RECORD = OCCURRENCE / SNAPSHOT
PROJECT_MANAGEMENT_DISCIPLINE = REUSABLE METHOD
```

## 1. Project continuity outranks session continuity

```text
PROJECT_CONTINUITY > SESSION_CONTINUITY
```

No project state, method, evidence, decision, or unresolved branch should depend on one conversational session remaining healthy.

## 2. Project state and method are both inheritable

A successor who knows only "where we are" but not "how we learned to decide" is incompletely onboarded when method can change the next decision.

For deep succession:

```text
TAKEOVER = STATE + METHOD + DECISION LINEAGE + NEXT ACTION
```

For ordinary continuation, do not force all of that material hot when `NOW.md` + the relevant artifact is sufficient.

## 3. Handoff framework and occurrence records must not be mixed

`research/handoffs/` contains reusable succession method.

`research/handoffs/records/<handoff-id>/` contains one time-bounded occurrence.

Reusable lessons discovered during an occurrence must be promoted to framework or research methodology.

```text
INSTANCE_DISCOVERS_METHOD
-> PROMOTE_METHOD
-> KEEP_INSTANCE_AS EVIDENCE
```

## 4. Project-state alignment is a transition operation, not a standing ceremony

A file can have been correct when written and still become stale later.

```text
INDIVIDUAL_FILE_CORRECT_AT_T
!=
PROJECT_STATE_COHERENT_AT_T_PLUS_1
```

Use `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` after material routing/method/release transitions, not after every research edit.

## 5. Reverify live state before material writes

Cached SHAs, old PR identities, chat summaries, and branch names are not live authority.

```text
BRANCH_HEAD_AT_T != BRANCH_HEAD_NOW
BRANCH_HEAD != FROZEN_IDENTITY
```

## 6. Preserve occurrence truth

When a validator, oracle, workflow, or project interpretation is wrong, preserve that occurrence and correct the method or successor state.

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

A frozen candidate is identified by exact source/tree binding, not mutable branch recency.

Do not modify frozen/released bytes merely to add narration and then pretend the changed bytes are the validated object.

## 8. Compression and growth occur at different layers

```text
WHAT / WHY
-> abstraction/compression may help

HOW
-> concretize / branch / recombine

FAILURE / ADVERSARIAL SPACE
-> expand while materially distinct shapes remain plausible

REPRESENTATION DUPLICATION
-> compress after equivalence is established
```

Key invariant:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
```

## 9. Growth pays complexity rent

Anti-convergence is not permission to maximize files, roles, branches, tests, or categories.

```text
ANTI_CONVERGENCE != MAXIMIZE_ARTIFACT_COUNT
```

A new artifact or workflow surface must earn its cost through distinct continuity, evidential, behavioral, or coordination value.

## 10. Optional packaging remains optional

```text
BUNDLED_REFERENCE != REQUIRED_RUNTIME_ORGAN
PACKAGE_INCLUDED != APPLICABLE
```

Project management must resist accidental bureaucracy created by packaging richness.

## 11. One next action does not collapse possibility space

```text
PLURAL_POSSIBILITY_SPACE
AND
ONE_NEXT_EXECUTION_STEP
```

Scheduling one experiment next is not a claim that only one research branch matters.

## 12. Handoff is applied behavior, not document production

```text
WRITTEN -> RETRIEVED -> INTERPRETED -> SALIENT -> APPLIED
```

A beautiful handoff that the receiver does not use is not continuity.

## 13. Project-manager succession and fresh validation optimize differently

```text
PROJECT_MANAGER_SUCCESSION
-> PRESERVE RELEVANT CONTEXT CONTINUITY

FRESH_VALIDATOR
-> MINIMIZE AUTHOR-SHAPED PRIMING BEFORE FIRST RESPONSE
```

Do not mechanically reuse a deep project handoff as fresh-validator briefing.

A reviewer already exposed to the author's answer/oracle cannot restore fresh Phase-A independence by promising to ignore it.

## 14. Promoted lessons from the v0.3.7 reconstruction/release period

- candidate/release identity must remain content-addressed rather than branch-addressed;
- false-positive validation oracles should be repaired without rewriting occurrence truth;
- handoff framework/method must not be buried inside a dated record;
- project-manager context completeness and fresh-validator information hygiene are different optimization directions;
- branch names are lifecycle surfaces, not archives;
- open issue or assertion count is not an epistemic quality metric;
- project routing surfaces can drift after transitions and should be aligned when that drift matters.

## 15. Promoted lessons from the 2026-09 cleanroom validation rounds

### 15.1 Structural isolation beats behavioral prohibition

Do not tell a fresh Agent:

> there is an answer/source/research repo elsewhere, but do not look at it.

That instruction itself reveals the hidden surface and asks the validator to suppress curiosity.

Prefer:

```text
CONTAMINATING SURFACE ABSENT
>
CONTAMINATING SURFACE PRESENT + PLEASE IGNORE
```

Separate disposable repos and orphan/root commits can remove Git-history leakage rather than relying on validator obedience.

### 15.2 Common substrate must be actually common

For treatment-arm experiments:

- same framework bytes;
- same task unless task is the intended variable;
- same model/mode where practical;
- only the intended treatment differs.

Verify common tree/blob identity when the experimental claim depends on it.

### 15.3 Preregister interpretation before seeing outputs

Record expected success/failure shapes and unfavorable interpretations before the first response.

This prevents the project from redefining victory after a preferred theory loses.

### 15.4 Capture the first complete response before correction dialogue

Fresh-response evidence is fragile.

```text
FIRST RESPONSE
-> CAPTURE / ARCHIVE
-> THEN ADJUDICATE / CORRECT / DISCUSS
```

Do not train the validator into the expected answer and then count the corrected answer as independent evidence.

### 15.5 Baseline good means nothing needs repairing yet

The semantic-reachability rounds produced 8/8 baseline-good responses.

Therefore:

```text
BASELINE DID NOT FAIL
-> NOTHING TO REPAIR
```

Do not run cue/example/new-rule repair arms just because they were planned before baseline results existed.

### 15.6 Null and negative results are convergence, not embarrassment

The I/J/K/L mechanism pilot produced equally good behavior under no inheritance, full history, successful recipe, and boundary-oriented inheritance.

The correct result was to narrow the stronger boundary-transfer claim, not redesign the same test repeatedly until the preferred arm won.

```text
THEORY DOES NOT WIN
!=
EXPERIMENT FAILED
```

### 15.7 Strong reasoning can saturate a one-shot mechanism fixture

A treatment variable cannot show benefit if the common prompt already exposes all decisive world facts and Current + the base model can derive the answer directly.

Future mechanism experiments must make the inherited/developmental information **causally necessary enough** to discriminate mechanisms.

For developmental memory this means multi-stage experience and multiple novel tasks, not one prompt containing the whole hidden structure.

### 15.8 Preserve raw substantive evidence before deleting disposable infrastructure

Cleanroom repos are temporary. Experimental occurrence truth is not.

Before deleting a cleanroom:

- archive task/treatment identity;
- archive first substantive response;
- archive relevant commit/tree identities;
- record adjudication separately;
- label any fidelity limitation honestly (for example citation wrappers omitted rather than claiming byte-exact UI preservation).

### 15.9 Comprehensive convergence owes every meaningful research branch a disposition

Divergence creates branches; convergence must not simply forget the older ones.

Every major branch should eventually become one of:

```text
SUPPORTED ENOUGH TO CONTINUE
NARROWED
SUBSUMED / DUPLICATE
REJECTED
METAPHOR ONLY
FIELD-UNRESOLVED
```

The living ledger is:

`research/evolution-inbox/EVOLUTIONARY-MEMORY-VALIDATION-COVERAGE-MAP.md`

### 15.10 Do not confuse good final answers with mechanism evidence

A strong model may independently derive a correct answer.

```text
GOOD OUTPUT
!=
TARGET MECHANISM CAUSED OUTPUT
```

When testing retrieval/routing, inspect trace/file-read evidence where available. When testing inheritance, include controls capable of revealing whether inheritance changed behavior.

## 16. Branch hygiene lesson from the 2026-09 succession

The long-lived `research/ena-reconstruction` branch drifted far behind main while retaining three unique files. This produced both bloat and deletion risk.

The correction is:

```text
main = durable continuation
short-lived branch = temporary isolation/review
unique artifact check before deletion
```

Do not merge an old diverged branch wholesale merely because it contains one useful file. Reconcile the useful artifact into a fresh main-based change, then retire the old branch.

Current cleanup audit:

`research/branch-cleanup/2026-09-03-BRANCH-CLEANUP-AUDIT.md`
