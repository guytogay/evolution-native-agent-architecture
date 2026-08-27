# ENA Project Handoff — Start Here

Status: `CURRENT_SESSION_HANDOFF / TAKEOVER_BOOTSTRAP / NOT_PROJECT_AUTHORITY`

Handoff ID:

`2026-08-27-v037-candidate0-frozen`

Prepared because the current project-manager session is unstable and will be intentionally replaced.

## Executive state

ENA Current remains:

```text
v0.3.6 / CURRENT / FIELD_VALIDATION
```

Current source of truth:

`releases/current/CURRENT-BASELINE.yaml`

The next release line is:

`v0.3.7`

A self-contained candidate exists and is frozen:

```text
candidate identity = v0.3.7-candidate.0
candidate branch   = candidate/v0.3.7-candidate.0
frozen source      = d0e793593184740d9732902e948afd48ed96ae2f
frozen subtree     = cffbf76fe1448b020b637c78d1f7ae46e4c0115b
subtree path       = releases/v0.3.7-candidate/
```

Author-side exact pre-freeze validation passed on those frozen bytes.

Fresh independent semantic falsification has **not** yet been performed.

```text
FROZEN != INDEPENDENTLY_VALIDATED
FROZEN != RELEASED
FROZEN != CURRENT
```

## The most important recent correction

During author validation, the project-manager refactored an adversarial harness from an observed 1080 pass conditions to 188 more structured pass conditions and initially described the reduction as an improvement.

The user correctly challenged this as a possible premature-convergence/ablation risk.

The canonical methodology now includes:

`research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`

Key rule:

```text
COMPRESS REPRESENTATION != COMPRESS POSSIBILITY SPACE
PROVEN_BEHAVIORAL_EQUIVALENCE -> MAY_COMPRESS
UNPROVEN_EQUIVALENCE -> DO_NOT_COLLAPSE
UNKNOWN_SPACE -> EXPAND
```

The frozen candidate record contains the author's older statement that the 1080 -> 188 reduction was an oracle-quality improvement. That statement must now be treated as **unverified author interpretation**, not accepted truth.

The candidate bytes themselves remain frozen and unchanged.

## Exact next action

Before creating the independent-falsification review PR, perform a tree-external:

**1080 -> 188 author-harness anti-ablation audit**.

Goal:

```text
old author attack space
-> recover materially distinct failure shapes
-> map each shape to the newer harness
-> disposition each shape
```

Allowed dispositions include:

```text
PRESERVED
MERGED_AS_PROVEN_EQUIVALENT
REPLACED_BY_STRONGER_ORACLE
RETAINED_OUTSIDE_CURRENT_HARNESS
RETIRED_WITH_EVIDENCE
LOST
UNKNOWN
```

`LOST` and `UNKNOWN` are not successful simplification.

If the audit finds only validation-oracle coverage gaps, repair the **validation method outside the frozen candidate tree**.

If the audit finds a materially distinct attack that can actually break the frozen candidate, keep candidate.0 frozen and enter reconciliation; create candidate.1 only if candidate bytes require material correction.

Only after this audit should the project open a clearly labeled `DO NOT MERGE / INDEPENDENT FALSIFICATION` review PR and hand the exact frozen source/tree to a fresh independent validator.

## Do not do these things yet

- do not modify `releases/current/`;
- do not call v0.3.7 Current;
- do not edit the frozen candidate subtree and continue calling it candidate.0;
- do not create candidate.1 merely because a research residual exists;
- do not accept author workflows/fixtures as the independent test oracle;
- do not skip the 1080 -> 188 anti-ablation audit;
- do not infer frozen identity from the current candidate branch head;
- do not compress materially distinct HOW/failure/evidence branches for a cleaner handoff or validation narrative.

## Takeover read order

A new project-manager session should read, in order:

1. `PROJECT-HUB.md`
2. `releases/current/CURRENT-BASELINE.yaml`
3. `research/handoffs/CURRENT-HANDOFF.yaml`
4. this file
5. `HANDOFF-MANIFEST.yaml`
6. `PROJECT-STATE.md`
7. `research/ACTIVE-RESEARCH.yaml`
8. `research/methodology/README.md`
9. `research/methodology/SESSION-HANDOFF-DISCIPLINE.md`
10. `research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md`
11. `research/plans/PROGRESS.yaml`
12. `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md`
13. `RECENT-THREE-ROUNDS.md`
14. `FILE-CATALOG.md`
15. candidate freeze/handoff records named in `PROJECT-STATE.md`

Then reverify live branch heads before writing.

## First takeover statement expected from the next session

Before substantive work, the next project-manager should be able to state from persisted sources:

```text
Current = v0.3.6
next line = v0.3.7
candidate.0 = frozen, not Current
frozen source/tree = exact values above
independent falsification = pending
immediate next action = 1080->188 anti-ablation audit
Current mutation = forbidden until governed release/promotion
```

If the repository no longer matches this projection, run the Project State Alignment Gate and repair the control plane before continuing.
