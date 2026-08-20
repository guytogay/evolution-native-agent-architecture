# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / CURRENT`

ENA uses one persistent project with multiple semantic areas. Participants do not receive separate ENA projects by Agent identity.

## GitHub semantic areas

| Area | Path | Role |
|---|---|---|
| Project Hub | `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | discovery and current project state |
| Current adoption baseline | `releases/current/` | **single complete adoption target** |
| Evolution Inbox | `research/evolution-inbox/` | open unpromoted research/candidate state |
| HAR | `research/adversarial-replay/` | historical adversarial research |
| Experiments | `research/experiments/` | experiment plans/results |
| Prototypes | `research/prototypes/` | non-current machine/design prototypes |
| Evidence | `evidence/` | observations/reference evidence |
| Contributions | `collaboration/inbox/` | unreconciled participant contributions |
| Reconciliation | `collaboration/reconciliation/` | handling/selection of contributions |
| Decisions | `decisions/` | durable architecture/process decisions |

GitHub does **not** maintain duplicate live release/archive directories. Superseded releases/candidates remain recoverable through Git history.

## Google Drive

Drive is a complementary durable artifact, research, evidence, contribution, and recovery surface. Historical recovery snapshots may exist there without becoming additional ENA runtime/adoption layers.

## Core information rules

- project-first, not Agent-first;
- one Current adoption baseline;
- knowledge/research may remain broad and open;
- not every accessible artifact is loaded into every task;
- Contribution != Reconciliation != Promotion;
- persistence != synchronization;
- copy/bridge must preserve provenance and semantic status;
- current adoption state must not be inferred from an archive or old chat.

> Preserve history durably; retrieve history selectively.

> Open knowledge does not mean always-loaded knowledge.
