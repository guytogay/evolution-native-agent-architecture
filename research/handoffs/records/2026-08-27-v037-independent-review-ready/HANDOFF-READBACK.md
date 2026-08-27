# ENA Handoff Record — Readback

Status: `PRE_MERGE_READBACK_PLAN / COMPLETION_PENDING_MAIN_INTEGRATION`

Handoff ID: `2026-08-27-v037-independent-review-ready`

This record is created as part of the handoff-structure refactor. Final handoff completion requires reading the integrated state back from `main` after the refactor PR merges.

## Pre-merge invariants to preserve

Before/after integration, verify:

- Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`;
- `releases/current/` bytes are unchanged by handoff restructuring;
- frozen candidate.0 remains bound to source `d0e793593184740d9732902e948afd48ed96ae2f` and subtree `cffbf76fe1448b020b637c78d1f7ae46e4c0115b`;
- PR #115 remains `DO NOT MERGE` independent-review surface, not release authority;
- anti-ablation audit remains complete and tree-external;
- `CURRENT-HANDOFF.yaml` resolves to this record;
- handoff framework files are at `research/handoffs/` root;
- historical records are under `research/handoffs/records/`;
- project methodology remains under `research/methodology/` and is explicitly required for takeover;
- reusable project-management method is not trapped inside the dated record;
- immediate project next action remains fresh independent falsification Phase A.

## Required post-merge readback

A completing session must record:

- merged PR number and merge commit;
- Main Gate / applicable CI conclusions;
- `main` Current identity readback;
- `CURRENT-HANDOFF.yaml` resolution;
- required takeover context resolution;
- active research pointer / Progress consistency;
- frozen candidate subtree readback;
- confirmation that old root-level dated handoff directory no longer exists;
- confirmation that old dated record is preserved under `records/`;
- confirmation that reusable handoff/project-management method lives at root, not inside the record.

```text
WRITTEN != HANDOFF_COMPLETE
```

Until post-merge readback is written, this file is a readback plan rather than completion evidence.
