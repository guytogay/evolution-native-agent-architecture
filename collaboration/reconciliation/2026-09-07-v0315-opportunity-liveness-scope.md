# v0.3.15 Opportunity Liveness Successor Scope

Status: `R1_CANDIDATE_SCOPE / NOT_CURRENT / NOT_PROMOTED`

Trigger: `F-208-12_VALUABLE_OPPORTUNITY_CAN_REMAIN_LATENT_WITHOUT_LIVENESS_DISPOSITION`

## Observed failure

Current v0.3.14 contains contribution preservation, latent candidates, `WAIT_FOR_CONTEXT`, triggered material obligations, activation/wake semantics and rapid opportunity succession, but does not explicitly connect a maintainer-accepted material opportunity to a required liveness disposition.

ENA's own maintenance reproduced the failure:

- PR #224 reached `ACCEPT_DIRECTION / NO_SUCCESSOR_TRIGGER_YET` without an exact wake/unblock condition;
- Issue #222 preserved multiple plausible design directions without per-direction next/wake/close semantics.

Project-control-plane containment was added by PR #231. This successor candidate evaluates making the same property explicit in adopter-facing ENA operational semantics.

## Intended bounded delta

No new Constitution ID.

No universal scheduler, daemon, deadline, queue implementation, or mandatory database.

No rule that every passing idea must be tracked or tried.

Candidate operational contract:

```text
MATERIAL_OPPORTUNITY_ACCEPTED_FOR_PRESERVATION
-> ADVANCE_NOW | WAIT_FOR_SIGNAL | BLOCKED | REJECT | ARCHIVE
```

Where:

- `ADVANCE_NOW` requires the smallest available decision-changing action when authority/tooling permit;
- `WAIT_FOR_SIGNAL` requires an observable wake condition and first post-wake action;
- `BLOCKED` requires a real boundary and explicit unblock condition;
- `REJECT` and `ARCHIVE` close active work while preserving appropriate provenance;
- arbitrary time-based ceremony is not required;
- a candidate may remain latent indefinitely when its named wake condition never occurs, but it is not an unspecified backlog item.

## Candidate surfaces

Primary:

- `releases/current/CONTRIBUTION-PROTOCOL.md`
- `releases/current/operational/procedures/EVOLUTION-LOOP.md`
- `releases/current/09-EVOLUTION-METABOLISM.md`
- `releases/current/CURRENT-BASELINE.yaml`

Add hot-kernel text only if targeted validation shows cold/on-demand routing is insufficient; do not expand the default hot payload merely for visibility.

## Lane

`R1_OPERATIONAL_BEHAVIOR_CHANGE`

Rationale: the change affects how accepted opportunities are progressed, but is intended to operationalize the existing semantic floor around triggered obligations, activation/wake, latent variation and governance convergence rather than rewrite that floor.

## Targeted adversarial cases

1. cheap reversible decision-changing action is available -> must not remain vague `WAIT`;
2. real future context is required -> valid `WAIT_FOR_SIGNAL` with observable wake condition;
3. missing external authority/tool/Host -> valid `BLOCKED` with unblock condition;
4. vague `more evidence needed` -> incomplete liveness;
5. trivial passing idea -> may be discarded without tracking;
6. useful but currently irrelevant idea -> may remain latent with a named wake context;
7. arbitrary calendar deadline with no applicability change -> must not be required;
8. candidate contradicted or duplicated -> `REJECT` / `ARCHIVE` closes active work;
9. non-defect demonstrated bounded value -> may justify successor without being mislabeled as a bug;
10. liveness disposition must not imply integration, universal fitness, or authority.

## Admission boundary

Do not promote merely because the project-level method sounds attractive. The candidate must:

- preserve v0.3.14 semantics outside the bounded liveness delta;
- pass current machine/regression/readback gates;
- pass the targeted adversarial cases above;
- keep predecessor v0.3.14 recoverable;
- avoid adding hot-payload cost unless that cost pays decision-changing rent.

