# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / ACTIVE_RESEARCH_BRANCH`

ENA uses one persistent project with multiple semantic areas. Participants do not receive separate ENA projects by Agent identity.

Directory organization is navigation, not ontology.

```text
DIRECTORY_SET != NATURAL_ORGAN_TAXONOMY
```

## Canonical project surfaces

| Area | Path | Role |
|---|---|---|
| Project Hub | `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | discovery and project-level routing |
| Current adoption baseline | `releases/current/` | **single complete adopter-facing Current target** |
| Research bootstrap | `research/RESEARCH-START-HERE.md` | small hot entrypoint for continuing ENA research |
| Research directory map | `research/README.md` | research information architecture |
| Research methodology | `research/methodology/` | durable method for how ENA itself is researched |
| Master plan / progress | `research/plans/` | reconstruction-to-release plan and machine-readable execution state |
| Reconstruction | `research/reconstruction/` | archaeology, retention ledgers, gap/degradation audits, closure research |
| External HOW research | `research/external-how/` | current external tools/processes/protocols/framework/community mechanisms mapped to ENA failures |
| Evolution Inbox | `research/evolution-inbox/` | open unpromoted research/candidate state |
| HAR | `research/adversarial-replay/` | historical adversarial/falsification research |
| Experiments | `research/experiments/` | experiments that can pay epistemic rent |
| Prototypes | `research/prototypes/` | non-Current executable/reference organs and candidate HOWs |
| Research incidents | `research/incidents/` | research-process failures and method corrections |
| Evidence | `evidence/` | observations/reference evidence |
| Contributions | `collaboration/inbox/` | unreconciled participant contributions |
| Reconciliation | `collaboration/reconciliation/` | handling/selection of contributions |
| Decisions | `decisions/` | durable architecture/process decisions |

GitHub does **not** maintain duplicate live Current baselines. Superseded releases/candidates remain recoverable through Git history and, when available, maintainer recovery artifacts.

## Research continuation path

A new session continuing the project should use:

```text
PROJECT-HUB.md
-> research/RESEARCH-START-HERE.md
-> research/methodology/
-> research/plans/PROGRESS.yaml
-> research/plans/ENA-RECONSTRUCTION-TO-RELEASE-PLAN.md
-> PR #82 / #89
-> only the relevant workstream / prototype / evidence
```

Do not reconstruct methodology from Issue archaeology unless auditing lineage. The canonical active research method belongs in `research/methodology/`.

Do not reconstruct project progress from conversation summaries. The durable current project execution state belongs in `research/plans/PROGRESS.yaml`.

## Method versus reconstruction

`research/reconstruction/` records recovered topics, audits, retention decisions, and historical engineering state.

`research/methodology/` records ongoing rules for how future ENA research should be performed.

When reconstruction reveals a new durable research discipline, canonicalize it into methodology and preserve the old path as a compatibility pointer where needed.

## External HOW surface

When a WHAT/WHY lacks practical realization, search `research/external-how/` before inventing machinery from scratch.

External sources may supply mature candidate organs, but:

```text
EXTERNAL_POPULARITY != ENA_SELECTION_PROOF
```

Map mechanisms to ENA failure models and Host conditions before selection.

## Maintainer recovery mirror

The maintainer may keep a private complementary durable artifact/research/evidence/recovery surface. Its storage coordinates are intentionally outside public project metadata.

That surface is not required for adoption and does not create another ENA runtime/adoption layer.

## Core information rules

- project-first, not Agent-first;
- one Current adoption baseline;
- broad research and HOW variation may coexist;
- not every accessible artifact is loaded into every task;
- Contribution != Reconciliation != Promotion;
- persistence != synchronization;
- durable != discoverable != salient != applied;
- copy/bridge must preserve provenance and semantic status;
- Current must not be inferred from an archive, old research file, or chat;
- legacy paths may remain as pointers when moving them preserves lineage better than deletion.

> **Preserve history durably; retrieve selectively.**

> **Open knowledge does not mean always-loaded knowledge.**

> **Compress the semantic trunk; let concrete HOWs branch.**
