# ENA v0.3.7 candidate.0 — Read Me First

Status: **WORKING_CANDIDATE / ASSEMBLY_IN_PROGRESS / NOT_CURRENT / NOT_FROZEN**

The active adopter baseline is still `releases/current/` = `v0.3.6 / CURRENT / FIELD_VALIDATION`.

This candidate exists to test whether ENA can become substantially more usable without inventing unnecessary new Core law.

## Start here during candidate review

1. `CANDIDATE-BASELINE.yaml` — exact working state, lineage, selected cargo, and assembly gaps;
2. `README.md` — candidate thesis and package boundary;
3. `RUNTIME-ADOPTION-KERNEL.md` — inherited hot/cold semantic kernel; candidate identity wording still requires reconciliation before freeze;
4. `operational/README.md` — the new practical HOW layer being assembled;
5. `references/REFERENCE-MANIFEST.yaml` — machine-readable optionality and applicability contract for selected references.

Do not treat missing Stage-1 paths as silent completion. The baseline explicitly lists them as pending.

## Candidate architecture

The candidate keeps a small hot semantic trunk and grows concrete HOWs outside it:

```text
TELOS / WHAT / WHY
        |
        v
hot cues / durable distinctions
        |
        v
operational routing
        |
        +--> procedure
        +--> optional reference organ
        +--> Host-native pattern
        +--> field/research residual
```

The operational tree may become large. The active context should not.

```text
REPOSITORY_DIVERGENCE != CONTEXT_EXPLOSION
```

## What candidate.0 is expected to add

### Adopter-facing Operational Architecture

- consequence-first cue routing;
- cold HOW map;
- exact reference pointer/index;
- Purpose-Relative Continuity procedure;
- Standing Input procedure;
- Control Retirement procedure;
- Evolution Commons substrate/protocol patterns;
- Host mapping guidance;
- curated Memory Metabolism guidance.

### Optional machine references

General optional:

- Retrieval Obligation 0.5;
- WAIT;
- Authority Lease;
- Effect Lifecycle;
- Recovery Adapter.

Advanced/specialized optional:

- Evidence Envelope;
- Evidence Dependency Map;
- Contested Authorship.

Commitment/Settlement recovered reconstruction remains research lineage for the first candidate unless new material evidence changes that decision.

### Tooling

The intended primary practical evolution tool is a minimal v2 helper that:

- creates valid latent v2 records without forcing an early Variation Space;
- delegates evolution-record semantics to the candidate-local v2 validator;
- exports/imports packet v2 with canonical digest and narrow packet consistency;
- never upgrades imported source selection into receiver-local selection.

The inherited v1.2 `ena_evolve.py` will become explicit legacy compatibility rather than the equally prominent default path.

## Applicability rule

Concrete HOWs must expose when they do **not** apply.

Examples include:

```text
Authority -> NOT_REQUIRED
Contested Authorship -> OUT_OF_SCOPE
Recovery -> independent rescue/drill only when required
Continuity -> NOT_REQUIRED when continuity cannot change the decision
Control Retirement -> KEEP_ACTIVE / UNKNOWN_WAIT when retirement basis is weak
```

A mechanism that can only say “activate me” but cannot say “not applicable” is likely to create false-BLOCK bureaucracy.

## Candidate proof boundary

This candidate may eventually pass deterministic machine checks and still fail independent semantic falsification.

```text
ASSEMBLED != VALIDATED
VALIDATED_BY_AUTHOR != INDEPENDENTLY_FALSIFIED
FROZEN != RELEASED
BRANCH_EXISTS != CURRENT
```

If frozen candidate.0 needs a material correction, a successor candidate identity is required.

> **The final test is whether an Agent can actually live by it.**
