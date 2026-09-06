# ENA Current — Adopter Quickstart

Status: `CURRENT / FIELD_VALIDATION / HUMAN_INTEGRATION_GUIDE`

Current numeric release identity is defined by `CURRENT-BASELINE.yaml`.

ENA is a design method and operational rule set for Agents that may learn, adapt, use tools, affect external systems, recover, or pass adaptations onward.

Its purpose is viable agency: useful evolution without turning every stimulus into truth, every capability into authority, every stored idea into action, or every local success into universal law.

## Minimum integration

1. Make `RUNTIME-ADOPTION-KERNEL.md` the **only default resident ENA text** for the Agent.
2. Make `operational/CUE-INDEX.md` retrievable when a real problem needs routing.
3. Make `ENFORCEMENT-MAP.yaml` retrievable when you need to know whether a property is model guidance, machine-guarded, externally controlled, or still field evidence.
4. Keep HOWs, references, fixtures, Constitution detail, and research lineage cold until they can change a decision.
5. Prefer an existing Host-native mechanism when it already preserves the required property and boundary.
6. After adoption, and after a material Host/runtime change, do one bounded **local operationalization pass**:
   - identify which relevant ENA boundaries are already embodied by local controls;
   - for a concrete uncovered gap, propose the smallest cheap/reversible Host-native mechanism that could materially improve the decision or recovery boundary;
   - do not install or activate consequential machinery beyond actual authority;
   - explicitly allow `EXISTING`, `PROPOSE`, `NOT_REQUIRED`, and `NOT_APPLICABLE` outcomes;
   - stop when another mechanism would not plausibly pay rent.

This is not a request to install every ENA mechanism. A rescue snapshot, canary, ledger, baseline, watcher, or validator may be useful on one Host and unnecessary on another.

```text
DEFAULT_AGENT_HOT_PAYLOAD = RUNTIME-ADOPTION-KERNEL.md
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
SEMANTIC_ADOPTION != LOCAL_OPERATIONALIZATION
LOCAL_OPERATIONALIZATION != INSTALL_EVERY_CONTROL
```

## What not to do

- Do not paste the whole ENA repository into a system prompt.
- Do not preload Quickstart + Kernel + Cue Index + Enforcement Map as one default bundle.
- Do not treat prose as hard enforcement.
- Do not install every bundled reference merely because it ships with Current.
- Do not make research lineage mandatory adoption context.
- Do not manufacture local machinery where the Host already preserves the property or where no real decision boundary needs it.

## Useful outcomes

`NOT_REQUIRED`, `NOT_APPLICABLE`, `WAIT`, `UNKNOWN`, and `REFUSE` are legitimate when they fit the actual consequence/evidence boundary.

## Evidence strength

Match claims to evidence:

`PROSE_PRESENT | STRUCTURALLY_REPRESENTED | MACHINE_GUARDED | EXECUTED | EXTERNALLY_OBSERVED | INDEPENDENTLY_SUPPORTED`

Machine selftests do not prove external authority, effect settlement, recovery, provenance, or universal Host fitness.

> **Keep one semantic kernel hot; retrieve the HOW; operationalize only where a real local gap earns it; enforce outside the model where the property actually lives.**
