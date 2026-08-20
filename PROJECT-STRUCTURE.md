# ENA Persistent Project Structure

Status: `PROJECT_INFORMATION_ARCHITECTURE / CURRENT`

This document maps ENA's GitHub and Google Drive surfaces to one semantic project structure. The directory trees do not need byte-for-byte symmetry; their **roles** must remain legible and non-conflicting.

## Semantic areas

| Semantic area | GitHub | Google Drive | Primary role |
|---|---|---|---|
| Project Hub | `PROJECT-HUB.md`, `PROJECT-METADATA.yaml` | `00 Project Hub / ENA - PROJECT HUB` | discovery/current state |
| Mainline | repository specification/source paths | `10 Mainline` index/pointers | accepted canonical state |
| Evolution Inbox | `research/evolution-inbox/` | `20 Research / 00 Evolution Inbox` | unpromoted candidate state/discovery |
| HAR | `research/adversarial-replay/` | `20 Research / 10 Historical Adversarial Replay` | historical adversarial research |
| Experiments | `research/experiments/` | `20 Research / 20 Experiments` | experiment plans/results |
| Prototypes | `research/prototypes/` | `20 Research / 30 Prototypes` | non-normative machine contracts/design prototypes |
| Evidence | `evidence/` | `30 Evidence` | observations/reference material |
| Releases | `releases/` | `40 Releases` | current and archived release artifacts |
| Collaboration Inbox | `collaboration/inbox/` | `50 Collaboration / 10 Inbox` | unreconciled participant contributions |
| Reconciliation | `collaboration/reconciliation/` | `50 Collaboration / 20 Reconciliation` | handling/decision on contributions |
| Templates | repo templates | `50 Collaboration / 30 Templates` | reusable collaboration forms |
| Decisions | `decisions/` | `60 Decisions` | durable architecture/process decisions |
| Archive | historical repo paths/history | `90 Archive` and `40 Releases / 90 Archive` | superseded/legacy material |

## Canonical/mirror rule

Do not maintain two unlabeled current versions of the same semantic artifact.

When similar content exists on multiple surfaces, declare its role:

- `CANONICAL`
- `MIRROR`
- `SNAPSHOT`
- `INDEX`
- `BRIDGE`
- `BACKUP`
- `ARCHIVE`

Current examples:

- GitHub `research/evolution-inbox/README.md` — canonical structured ENA candidate state.
- Drive `ENA Evolution Inbox - INDEX` — discovery/index for humans and Drive-only participants.
- Drive v0.2.11 ZIP/single-file artifacts — durable release artifacts/recovery anchors.
- GitHub source/research lineage — diff-friendly engineering lineage from repository adoption onward.

## Compatibility policy

Information-architecture migration must not silently break older participants.

`research/EVOLUTION-INBOX.md` remains as a compatibility pointer to `research/evolution-inbox/README.md`.

Drive files were moved instead of copied where possible so their file IDs/links remain stable.

`ChatGPT Knowledge` is a legacy/general knowledge location and is no longer the ENA project root.

## Project-first rule

Do not create separate ENA project trees per participant (for example `ChatGPT/ENA`, `Gemini/ENA`, `Hermes/ENA`). Participants contribute to the same persistent project state through declared surfaces and authority boundaries.

## Surface-partition rule

A participant may join with GitHub-only or Drive-only access.

If no participant/automation can observe both surfaces, project state is partitioned. Do not claim synchronization. A bridge/reconciliation participant must preserve provenance and semantic status while relaying contributions.

## Naming rule

Critical concepts expected to be searched must appear literally in paths or index titles. The Drive structure therefore contains a folder and index literally named `Evolution Inbox`.

Avoid vague durable names such as `final`, `latest`, `misc`, `notes`, or `new` without project/type/version/date context.

## Maintenance rule

At project start:

`Registry → Project Hub → Metadata → current canonical state → Inbox/Reconciliation → task-specific material`

At project end:

`persist output → classify artifact/status → reconcile when appropriate → update indexes/metadata only if state changed → keep Current vs Archive honest`

This structure is collaboration infrastructure. It does not modify ENA v0.2.11 normative semantics.
