# Recent decision-bearing rounds

This is a project-manager continuity projection, not a validator Phase-A briefing.

A fresh candidate.1 Phase-A reviewer must not read this before sealing its report.

## Round 1 — frozen candidate.0 was independently falsified and superseded

Frozen `v0.3.7-candidate.0`:

- source `d0e793593184740d9732902e948afd48ed96ae2f`
- subtree `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`

Fresh blind Phase A sealed at:

`5ba3d241efa460fe170253860ad67045aa1d96a5`

It independently exposed four deterministic gaps involving imported source-context retention, tied-latest packet chronology, archive preservation consistency, and invalid template chronology.

Phase B compared these findings against the candidate's own represented contract and author evidence, classifying all four as material candidate-byte defects / shared blind spots rather than wrong-oracle or intentional-boundary cases.

Result:

`candidate.0 -> NEEDS_REVISION / CANDIDATE_1_REQUIRED`

The frozen predecessor was not edited in place.

## Round 2 — candidate.1 repaired known findings, then deliberately reopened nearby branches

Candidate.1 round 1 repair:

`583ac8133350bdf70a6a87fc8f0b070943f0aca1`

Rather than treating A–D closure as completeness, focused probes expanded into nearby chronology/history space.

Those probes found two further contract-backed defects:

- integration at-commit state could be historically unsupported/mismatched;
- represented source experiment/evaluation history could be structurally empty while still presenting a source-history claim.

They also found a source/receiver candidate-ID collision, but no current contract established global cross-environment uniqueness. That branch remained visible rather than being converted into an invented universal rule.

Candidate.1 round 2 focused repair:

`bc8be8bc02a2b2515cfa1b7eee2c4bd3c2a37f90`

Final evidence:

- targeted run `33052764739` — SUCCESS;
- focused open-branch run `33052764661` — SUCCESS;
- legitimate post-commit reselection remained accepted;
- attack cardinality remained `OPEN`;
- same-falsifier checks were explicitly not called fresh independent Phase A.

Reconciliation record:

`collaboration/reconciliation/2026-08-27-v037-candidate1-successor-repair-reconciliation.md`

## Round 3 — exact candidate.1 was validated, frozen externally, and routed to one fresh blind review

Before exact validation, candidate.1's own status projection was reconciled from stale targeted-repair wording to the actual exact-pre-freeze state. The scoped transform was allowed to change only `CANDIDATE-BASELINE.yaml`; Current remained untouched.

The exact pre-freeze gate then passed:

- workflow: `ENA v0.3.7 Candidate.1 Exact Pre-Freeze Gate`
- run: `33055811978`
- exact source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- exact candidate subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- Current subtree at same source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`

An external freeze record then bound those exact tested bytes without rewriting candidate cargo:

`collaboration/reconciliation/2026-08-27-v037-candidate1-freeze.md`

Post-freeze independence was considered explicitly rather than assumed. Decision:

`FRESH_BLIND_SUCCESSOR_REVIEW_WARRANTED / ONE_REVIEW_CYCLE`

Rationale: executable/validator semantics changed in decision-material areas, and predecessor fresh review had already demonstrated shared author blind spots. This is a local epistemic-rent decision, not a universal rule that every successor must be re-reviewed forever.

Fresh intake is ready:

- Issue `#128`
- branch `validation/v037-c1-blind-phase-a-primary`
- blind entry `collaboration/reconciliation/2026-08-27-v037-candidate1-blind-phase-a-entry.md`
- required report `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-phase-a-primary.md`
- intake head `bac074097579ad930b2e90c46c00773f6f20c86d`

The next project-manager action is to obtain that fresh sealed report, verify its immutable identity, and only then perform Phase B reconciliation.

## Method continuity across all three rounds

Do not compress these rounds into “tests passed, therefore release”. The durable distinctions are:

- independent search-space evidence vs author/same-falsifier evidence;
- frozen occurrence identity vs mutable branch head;
- known defect closure vs completeness;
- visible residual vs automatic release blocker;
- representation compression vs possibility-space compression.

`ATTACK_CARDINALITY = OPEN`
