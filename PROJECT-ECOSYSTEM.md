# ENA Project Ecosystem

Status: `LIVE_PROJECT_OPERATING_BOUNDARY`

ENA is maintained as a small repository ecosystem, not as one isolated repository.

## Canonical repositories

### `guytogay/evolution-native-agent-architecture`

Owns ENA theory, Current/release semantics, Constitution, operational contracts, research evidence, field validation, release discipline, and upstream design decisions.

This repository decides what ENA means and what becomes Current.

### `guytogay/human-ai-workbench`

Owns project-general human-AI working method discovered through real work: continuation/succession, project-state practice, coordination reduction, proportional progression, publication/readback patterns, and experiment-working discipline when those methods generalize beyond ENA.

ENA may generate an occurrence that feeds the Workbench, and Workbench methods may return to improve ENA execution. Do not duplicate the same reusable method canonically in both repositories.

### `guytogay/ena-field-guide`

Owns practical, evidence-backed ENA-derived HOW that has earned reuse in Agent/Host work.

A Field Guide entry must have usable trigger/action/monitor/stop or revalidation boundaries. Upstream theory, a release, or one attractive experiment does not automatically earn downstream admission.

```text
ENA theory / field evidence
-> reusable operating practice earns admission
-> ENA Field Guide
-> later real use may return evidence upstream
```

## Experimental / cleanroom repositories

`guytogay/independent-validation-cleanroom` is reusable cleanroom infrastructure/pattern material.

Round-specific repositories such as:

- `independent-validation-cleanroom-m0`
- `independent-validation-cleanroom-m1`
- `independent-validation-cleanroom-m2`
- `independent-validation-cleanroom-m3`

are disposable execution surfaces. Additional cleanroom repositories may be created when structural isolation materially improves an experiment.

They are not canonical project history merely because they exist.

Before deleting or resetting a temporary cleanroom, preserve any unique decision-relevant material that must survive: preregistration, frozen treatment/fixture identity, first outputs, scoring/adjudication records, negative/null results, and provenance needed to reconstruct the occurrence.

```text
CLEAN_REPOSITORY != INDEPENDENT_AI_WORKER
INFORMATION_ISOLATION != EXECUTION_ISOLATION
TEMPORARY_EXPERIMENT_SURFACE != PERMANENT_ARCHIVE
```

## Cross-repository maintenance rule

The active ENA project manager/session is responsible for maintaining all three canonical repositories when current work crosses their boundaries.

Do not wait for the owner to separately request synchronization when a material result clearly belongs downstream or in Workbench. Route it to the correct canonical repository, while preserving each repository's admission/evidence rules.

Examples:

- ENA semantic/release defect -> ENA;
- repeated project coordination method -> Human-AI Workbench;
- evidence-backed practical ENA operating HOW -> ENA Field Guide;
- isolated/fresh experimental execution -> cleanroom surface;
- cleanroom result -> return the durable evidence/conclusion to its canonical repository before disposal.

```text
RELATED_REPOSITORY != MIRRORED_REPOSITORY
ROUTE_BY_CANONICAL_OWNERSHIP
CITE_PROVENANCE_INSTEAD_OF_COPYING_THEORY_OR_HISTORY
```

## Rapid Current progression

ENA is intended to iterate quickly without sacrificing occurrence truth.

The release discipline is:

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
SAME_VERSION -> SAME_EFFECTIVE_CONTENT
PRESERVE_OLD_RELEASES + MOVE_CURRENT_QUICKLY
```

Operational interpretation:

1. If a bounded defect is discovered while a candidate is still being prepared/reviewed, fix it before promotion rather than knowingly publishing the defect.
2. If a known decision-bearing, bounded, fixable defect is discovered after release, preserve the released occurrence exactly and move Current through the smallest justified successor promptly; do not hold the known fix merely for a future planned version.
3. Do not reserve or manufacture a successor number when there is no demonstrated product value or defect to carry.
4. Unrelated open research does not block a bounded Current correction.
5. Rapid progression does not allow semantic/high-consequence changes to be mislabeled as low-risk.

```text
DEFECT_FOUND_BEFORE_PROMOTION -> FIX_BEFORE_PROMOTION
KNOWN_BOUNDED_CURRENT_DEFECT -> RECORD_OCCURRENCE + SMALLEST_RAPID_SUCCESSOR
FIELD_VALIDATION != KNOWN_DEFECT_TOLERANCE
RELEASE_NUMBER != PROJECT_GOAL
```

Canonical method: `research/methodology/RAPID-CURRENT-RELEASE-DISCIPLINE.md`.

## Human-work minimization

The human owner should not be used as a byte transporter, copy/paste relay, repository bootstrapper, or mechanical experiment runner when the active Agent has tools and authority to perform those steps itself without invalidating the experimental boundary.

Default:

```text
AGENT_CAN_SELF_EXECUTE_WITH_REQUIRED_BOUNDARY -> AGENT_EXECUTES
HUMAN_IN_THE_LOOP != HUMAN_AS_THE_LOOP
HUMAN_JUDGMENT != HUMAN_TRANSPORT
```

Use human action when it is genuinely required, such as:

- consequential judgment/authorization;
- a fresh AI execution surface that available tooling cannot instantiate with the required isolation;
- an external account/device/UI or physical-world boundary unavailable to the Agent;
- another irreducible capability boundary.

When human participation is irreducible, minimize the number of manual steps and keep the reason explicit. Do not preserve manual relay merely because an earlier experiment used it.

## Default continuation behavior

For ordinary continuation:

1. read the live `NOW.md` of the repository where work is active;
2. follow directly relevant cross-repository pointers;
3. independently reverify mutable live facts before writes;
4. work across the ecosystem as needed;
5. update each canonical repository only for truth it owns;
6. avoid full-repository or full-ecosystem audits unless the current decision requires them.

For deep ENA succession, `research/handoffs/CURRENT-HANDOFF.yaml` remains the router. This ecosystem file is a stable scope/ownership rule, not a replacement for a dated handoff occurrence.
