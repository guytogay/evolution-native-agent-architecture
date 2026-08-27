# ENA Handoff — Recent Three Decision-Bearing Rounds

Status: `HANDOFF_CONVERSATION_CONTINUITY / STRUCTURED_SUMMARY / NOT_CANONICAL_AUTHORITY`

Handoff ID: `2026-08-27-v037-candidate0-frozen`

This is not a raw chat transcript. It preserves the latest three project-decision rounds that materially determine the next session's behavior.

`THREE_ROUNDS = MINIMUM_CONTINUITY_WINDOW`, not an information cap.

## Round 1 — candidate.0 freeze and independent-review preparation

### User direction

The user asked the project-manager session to continue advancing ENA through candidate build/validation rather than stop at planning.

### Project-manager action

The session completed candidate.0 assembly, zh-CN operational projection, identity reconciliation, author adversarial work, exact pre-freeze validation, and an external freeze record.

Frozen identity established:

```text
candidate = v0.3.7-candidate.0
source = d0e793593184740d9732902e948afd48ed96ae2f
candidate subtree = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
```

A tree-external fresh independent falsification handoff was also created.

### Durable result

- candidate.0 is frozen;
- Current remains v0.3.6;
- exact pre-freeze run `33011823923` succeeded;
- independent semantic falsification remains pending;
- candidate.0 must not be edited in place after freeze.

### Unresolved consequence

A fresh independent validator still must examine the frozen bytes before release/candidate succession can be decided.

---

## Round 2 — user challenges 1080 -> 188 convergence claim

### User concern

The project-manager had described the author-harness reduction from an observed 1080 pass conditions to 188 structured pass conditions as an improvement.

The user immediately flagged this as dangerous: ENA research cannot assume that a smaller, cleaner summary/harness is better when compression may have erased concrete HOW/failure variation.

The user emphasized a recurring LLM bias:

> LLMs naturally present success through summary/convergence, but ENA sometimes requires the opposite: divergence, enumeration, branching, and preservation of variation.

### Project-manager correction

The session accepted that the earlier claim was too strong.

The corrected rule became:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

A canonical focused methodology was created:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

An incident record and methodology changelog entry were also added.

PR #112 was CI-checked and squash-merged to main at:

`e42f9838294716b2ad34e6a2a0150e5d1cb89027`

### Durable result

Premature convergence / summarization bias is now a canonical ENA research-method concern, not merely a conversational reminder.

### Important self-application during the round

While documenting the new method, the project-manager briefly created duplicate quick-check/checklist files with no independent behavior. Those were removed.

This demonstrated the other side of the rule:

```text
DISTINCT_BEHAVIOR -> PRESERVE/GROW
PROVEN_REPRESENTATION_DUPLICATION -> COMPRESS
```

### Unresolved consequence

The 1080 -> 188 change itself has not yet undergone the new anti-ablation discipline. The newer harness cannot yet be called epistemically superior solely because it is cleaner.

---

## Round 3 — select the next action before independent validation

### User question

The user asked what the project should do next.

### Project-manager recommendation

Do **not** immediately begin independent falsification.

First perform a tree-external **1080 -> 188 anti-ablation audit**.

The audit should recover materially distinct predecessor attack/failure shapes and classify their disposition in the newer harness:

```text
PRESERVED
MERGED_AS_PROVEN_EQUIVALENT
REPLACED_BY_STRONGER_ORACLE
RETAINED_OUTSIDE_CURRENT_HARNESS
RETIRED_WITH_EVIDENCE
LOST
UNKNOWN
```

The goal is not to recreate the number 1080. The goal is to preserve/recover materially distinct adversarial variation.

### Decision logic

If a lost attack only reveals a validator/oracle coverage defect:

```text
repair validation method outside frozen candidate.0
```

If a recovered attack exposes a material frozen-candidate defect:

```text
candidate.0 remains frozen lineage
-> reconciliation
-> candidate.1 only if candidate bytes require material repair
```

After the anti-ablation audit, create a `DO NOT MERGE` independent-falsification review PR and use a fresh validator with Phase A independent inspection before Phase B comparison against author evidence.

### Durable next-action decision

```text
NEXT = 1080_TO_188_ANTI_ABLATION_AUDIT
INDEPENDENT_FALSIFICATION_PR = AFTER_AUDIT
CURRENT_CHANGE = NO
```

---

## Current transition — standardized session handoff

The current user request is to replace this unstable project-manager session and make such handoffs a standardized normal lifecycle behavior.

This handoff package and `research/methodology/SESSION-HANDOFF-DISCIPLINE.md` are the durable response.

The next session should not ask the user to reconstruct the three rounds above; it should continue from the persisted project state after live verification.
