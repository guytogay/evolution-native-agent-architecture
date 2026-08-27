# ENA Handoff Record — File Catalog

Status: `TAKEOVER_FILE_MAP / INSTANCE_BOOTSTRAP / NOT_AUTHORITY`

Handoff ID: `2026-08-27-v037-independent-review-ready`

This catalog tells a successor **where to look and why**. Authority remains with the governed source itself.

## A. Project entry and Current

| Path | Role |
|---|---|
| `PROJECT-HUB.md` | stable repository/project entrypoint |
| `releases/current/CURRENT-BASELINE.yaml` | machine-readable Current identity authority |
| `releases/current/` | adopter-facing Current baseline only |

## B. Handoff framework — mandatory succession method

| Path | Role |
|---|---|
| `research/handoffs/README.md` | handoff hierarchy and navigation |
| `research/handoffs/CURRENT-HANDOFF.yaml` | latest intended record pointer + takeover contract |
| `research/handoffs/HANDOFF-PROTOCOL.md` | canonical outgoing + incoming succession rules |
| `research/handoffs/REQUIRED-TAKEOVER-CONTEXT.yaml` | machine-readable mandatory takeover context |
| `research/handoffs/PROJECT-MANAGEMENT-DISCIPLINE.md` | reusable cross-session project-management rules |
| `research/handoffs/records/README.md` | historical/current record semantics |

These are not ENA Current semantics, but they are first-class project-continuity method.

## C. Current handoff record — this occurrence

Root:

`research/handoffs/records/2026-08-27-v037-independent-review-ready/`

| File | Role |
|---|---|
| `HANDOFF-START-HERE.md` | fastest instance-specific bootstrap and exact next action |
| `HANDOFF-MANIFEST.yaml` | machine-readable record identity/state |
| `PROJECT-STATE.md` | detailed current-state projection |
| `RECENT-THREE-ROUNDS.md` | latest decision-bearing conversation continuity |
| `FILE-CATALOG.md` | this map |
| `HANDOFF-READBACK.md` | integration/readback evidence |

## D. Historical handoff records

`research/handoffs/records/2026-08-27-v037-candidate0-frozen/`

This is the predecessor succession occurrence. It is lineage, not the current pointer.

## E. Project research methodology — mandatory takeover context

| Path | Role |
|---|---|
| `research/methodology/README.md` | method index |
| `research/methodology/ENA-RESEARCH-DISCIPLINE.md` | master research-method ledger |
| `research/methodology/CONVERGENCE-DIVERGENCE-DISCIPLINE.md` | convergence, growth, anti-ablation discipline |
| `research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md` | material-transition coherence repair |
| `research/methodology/METHOD-CHANGELOG.md` | method-change lineage |
| `research/methodology/incidents/` | concrete method failures/evidence |

Important distinction:

```text
handoff framework = how operators exchange project responsibility
project methodology = how ENA research itself is performed
```

Both must be inherited.

## F. Active research control plane

| Path | Role |
|---|---|
| `research/ACTIVE-RESEARCH.yaml` | main-visible active research routing authority |
| `research/RESEARCH-START-HERE.md` | research bootstrap |
| `research/plans/PROGRESS.yaml` | fast-moving execution state |
| `research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md` | long-horizon plan |
| `research/BRANCH-GOVERNANCE.md` | branch/candidate/release topology rules |
| `research/BRANCH-INVENTORY.yaml` | branch inventory/lineage aid |

## G. Frozen v0.3.7 candidate.0

| Path / identity | Role |
|---|---|
| `releases/v0.3.7-candidate/` | frozen candidate subtree path |
| `d0e793593184740d9732902e948afd48ed96ae2f` | frozen source commit |
| `cffbf76fe1448b020b637c78d1f7ae46e4c0115b` | frozen candidate subtree SHA |
| `collaboration/reconciliation/2026-08-27-v037-candidate0-freeze.md` | freeze record |
| `collaboration/reconciliation/2026-08-27-v037-candidate0-independent-falsification-handoff.md` | validator handoff |

Candidate branch head is not frozen identity.

## H. Author validation / anti-ablation evidence

| Path | Role |
|---|---|
| `collaboration/reconciliation/2026-08-27-v037-candidate0-author-attacks.md` | author falsification occurrence record |
| `collaboration/reconciliation/2026-08-27-v037-candidate0-author-harness-anti-ablation-audit.md` | 1080 -> 188 anti-ablation audit |
| `.github/scripts/v037_candidate_anti_ablation.py` | tree-external restored attack coverage |
| `.github/workflows/v037-candidate-anti-ablation.yml` | machine gate for that coverage |

Anti-ablation run: `33035656311`.

These are author-side/validation-method evidence, not independent semantic support.

## I. Fresh independent validation surface

PR `#115`:

`DO NOT MERGE: v0.3.7 candidate.0 fresh independent falsification`

Use the exact frozen source/subtree, not the mutable candidate branch head, as review identity.

Phase A must precede author-oracle comparison.

## J. Operational Architecture / selected candidate research lineage

Useful when Phase A needs deeper mechanism context:

- `research/operational-architecture/`
- `research/release-scope/`
- `research/prototypes/`
- `research/experiments/`
- `research/external-how/`

Retrieve selectively; do not make research history a parallel runtime baseline.

## Recommended takeover routes

### Normal project-manager succession

```text
PROJECT-HUB
-> Current baseline
-> CURRENT-HANDOFF
-> handoff framework
-> required project methodology
-> current handoff record
-> ACTIVE-RESEARCH
-> Progress / master plan
-> live ref verification
-> exact next action
```

### Current task: fresh independent validation

```text
CURRENT-HANDOFF
-> current record
-> exact freeze identity
-> PR #115 instructions
-> Phase A direct frozen-byte inspection
-> only then Phase B author evidence comparison
```

### If sources disagree

```text
stop substantive work
-> research/methodology/PROJECT-STATE-ALIGNMENT-GATE.md
-> repair control-plane disagreement
-> resume
```
