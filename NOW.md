# ENA — NOW

This is the default live project-status surface.

## Current

- `v0.3.14 / CURRENT / FIELD_VALIDATION`
- authority: `releases/current/CURRENT-BASELINE.yaml`
- effective adopter package: `releases/current/`
- predecessor / rollback / occurrence truth: `v0.3.13`
- field stream: GitHub Issue `#208` — version-neutral Current field validation

v0.3.14 is a bounded **R0 adoption-surface successor**. It preserves the v0.3.13 R1 evolution loop, 38-ID Constitution, protected semantic floor, and core machine behavior while closing:

- `F-208-09_LOCAL_PROJECTION_PERSISTENCE_CUE_MISSING_FROM_MINIMUM_ADOPTION_PATH`.

A fresh one-shot v0.3.13 adopter review correctly reconstructed the existing Compiled Local Projection contract from the deeper self-positioning file but flagged that Minimum integration did not explicitly tell adopters to preserve the smallest reusable Host facts that repeatedly change decisions. The review otherwise returned `ADOPT_WITH_NONBLOCKING_CLARIFICATIONS` and did not infer mandatory seven-tool installation, continuous self-editing, a universal metric, or universal runtime.

## Evolution contract

Current keeps the v0.3.13 **how to evolve** path unchanged:

```text
signal / idea / correction / failure / success
-> durable inbox / candidate store when decision-relevant
-> latent candidate by default
-> decide whether a trial is worth running
-> decision-relevant before-state + recovery/authority boundary
-> bounded expression / real task / Variation Space when applicable
-> observe outcomes
-> local selection
-> integrate / retain / adapt / dormant / reject / archive
-> wake on relevant signal or environment change
```

Canonical cold HOW:

`releases/current/operational/procedures/EVOLUTION-LOOP.md`

Route:

`Runtime Kernel -> CUE-INDEX -> OA-EVO-01 -> EVOLUTION-LOOP.md -> Host-native organ`

```text
EVOLUTION_VOCABULARY != EXECUTABLE_EVOLUTION_LOOP
PROTECTION_OF_EVOLVABILITY != EVOLUTION_ITSELF
EVOLUTION_LOOP != CONTINUOUS_SELF_EDITING
```

`tools/ena_evolve_v2.py` remains a narrow latent-record / migration packet helper, not a full lifecycle engine.

## Adoption / Host operationalization

After adoption, and after a material Host/runtime change, do one bounded local operationalization pass:

```text
SEMANTIC_ADOPTION != LOCAL_OPERATIONALIZATION
LOCAL_OPERATIONALIZATION != INSTALL_EVERY_CONTROL
```

Inspect which applicable boundaries are already covered by Host-native mechanisms. For a real uncovered gap, propose the smallest cheap/reversible mechanism that could materially change or protect a real decision. `EXISTING`, `PROPOSE`, `NOT_REQUIRED`, and `NOT_APPLICABLE` are valid outcomes. Consequential installation still requires actual authority.

When Host facts repeatedly change decisions, preserve the smallest reusable **Local Projection** needed for those decisions. Reuse existing durable Host-native storage when possible. The Local Projection is an observed-reality cache, not a copied ENA baseline, authority source, or mandatory database.

```text
LOCAL_PROJECTION != SHADOW_ENA_BASELINE
LOCAL_PROJECTION != NEW_AUTHORITY_SOURCE
LOCAL_PROJECTION != MANDATORY_DATABASE
```

## Adoption contract

```text
DEFAULT_AGENT_HOT_PAYLOAD = releases/current/RUNTIME-ADOPTION-KERNEL.md
AVAILABLE_RESOURCE != DEFAULT_HOT_PAYLOAD
HOT_KERNEL != FULL_HOW_LIBRARY
```

For ordinary Agent runtime, only the Runtime Adoption Kernel is resident by default. Cue Index, HOW Map, Evolution Loop, Enforcement Map, fixtures, references, Constitution detail, and research lineage are cold/on-demand.

Human adopters start at `releases/current/ADOPTER-QUICKSTART.md`.

## Share-ready contract

Before recommending Current to another adopter/Agent:

- known decision-bearing defects with a clear bounded fix must be resolved through the smallest successor;
- current machine/regression gates must pass;
- bounded identity/adopter/operational readback must agree with `CURRENT-BASELINE.yaml`;
- unknown future defects remain legitimate field-validation risk, but known unfixed defects are not an acceptable recommendation state.

The same-version rule is machine-enforced by `.github/workflows/current-immutability.yml`: any change under `releases/current/**` must change a canonical Current `ena_version`, otherwise CI rejects the mutation. After F-208-11 the guard also rejects ambiguous/non-canonical top-level version serialization before comparing predecessor and proposed identity.

```text
SAME_VERSION -> SAME_EFFECTIVE_CONTENT
POLICY_DECLARED != MACHINE_GUARDED
GREEN_EXISTING_GATES != COMPLETE_GATE_COVERAGE
MACHINE_GUARD_PRESENT != MACHINE_GUARD_SEMANTICALLY_CLOSED
```

## Release posture

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
PRESERVE_OLD_RELEASES + MOVE_CURRENT_QUICKLY
```

Method: `research/methodology/RAPID-CURRENT-RELEASE-DISCIPLINE.md`

- R0 — adoption / projection / bounded tooling or publication-coherence field patch: machine/regression/readback + rollback;
- R1 — operational behavior change: targeted operational validation + regression/readback + rollback;
- R2 — core semantic/high-consequence change: heavy freeze/fresh falsification by default.

If a bounded defect is found before promotion, fix it before promotion. If a known decision-bearing bounded defect is found after release, preserve the released occurrence and move Current through the smallest justified successor promptly rather than holding the fix for a later planned release.

```text
DEFECT_FOUND_BEFORE_PROMOTION -> FIX_BEFORE_PROMOTION
KNOWN_BOUNDED_CURRENT_DEFECT -> RECORD_OCCURRENCE + SMALLEST_RAPID_SUCCESSOR
FIELD_VALIDATION != KNOWN_DEFECT_TOLERANCE
```

## Active field stream

Issue `#208` follows Current, not one release number. F-208-01 through F-208-11 are the accumulated field findings; new bounded defects should create the smallest justified successor or control-plane fix instead of remaining knowingly unfixed.

`F-208-10_SAME_VERSION_CURRENT_BYTE_MUTATION_NOT_MACHINE_REJECTED` was exposed by external Agent contribution PR `#224`: the PR changed an already released Current kernel while retaining v0.3.14 identity, and the existing gates passed. Control-plane PR `#225` added the version-neutral Current Immutability Guard and merged as `becd83529e58d166f907c519d30da081180d260a`. Current v0.3.14 bytes did not change.

Successor-session re-verification then exposed `F-208-11_SEMANTIC_VERSION_SERIALIZATION_CAN_BYPASS_IMMUTABILITY_GUARD`: the guard compared raw YAML scalar text, so a representation-only change such as quoted `v0.3.14` could look like a changed identity while YAML consumers still saw the same version. Control-plane PR `#228` closed this normalization gap and merged as `b685d709fbcd98bf0412336d64ce5395dc23ad54`. Current v0.3.14 bytes again did not change.

PR `#224` remains useful contribution occurrence/provenance. Its trigger-style positive-rule direction is accepted for further consideration, but the submitted expansion is not semantics-neutral and expands the Durable distinctions section by roughly 4x. Live review retained the original five blockers (#1 continuity, #6 local success, #8 migration, #17 evidence independence, #19 UNKNOWN), identified further narrowing needs, and recorded a compact-hybrid comparison candidate. The current judgment is `ATTRACTIVE_EXPRESSION_DIRECTION != DEMONSTRATED_SUCCESSOR_VALUE`: no successor release is justified yet. It must not be merged into v0.3.14 in place; any eventual adopted refinement requires a successor identity and proportional release assessment.

Recent reality contact also includes reconciled DSH PR `#220`: the tested high-reasoning salience probes were non-discriminating and do not justify a new primary or a claim that the Runtime Kernel is useful/useless.

## Project ecosystem

Canonical scope/ownership: `PROJECT-ECOSYSTEM.md`.

The active project manager/session maintains three canonical repositories as one cooperating project ecosystem while preserving separate ownership boundaries:

- `guytogay/evolution-native-agent-architecture` — ENA theory, Current/release semantics, research/field evidence;
- `guytogay/human-ai-workbench` — reusable project-general human-AI working method;
- `guytogay/ena-field-guide` — evidence-backed practical ENA HOW.

Reusable/disposable `independent-validation-cleanroom*` repositories are experimental execution surfaces, not a fourth canonical knowledge store. Create/reset/delete them as useful for isolation; preserve unique evidence/provenance before disposal.

When available Agent tooling can perform experiment setup, repository operations, transport, scoring, or evidence capture without violating the required boundary, the Agent should execute those steps directly instead of assigning copy/paste or relay work to the human.

```text
ROUTE_BY_CANONICAL_OWNERSHIP
AGENT_CAN_SELF_EXECUTE_WITH_REQUIRED_BOUNDARY -> AGENT_EXECUTES
HUMAN_IN_THE_LOOP != HUMAN_AS_THE_LOOP
CLEAN_REPOSITORY != INDEPENDENT_AI_WORKER
```

## Research status

The evolutionary-memory mechanism-discrimination campaign is **CLOSED**. No active mechanism primary remains. Reopen research only for a concrete decision-changing failure or a genuinely new non-derivable discriminator.

## Open work

- GitHub Issue `#208` — version-neutral Current field validation.
- GitHub PR `#224` — trigger-style Durable distinctions contribution; maintainer disposition remains `ACCEPT_DIRECTION / REQUEST_NARROWING / SUCCESSOR_REQUIRED`; current release judgment is `NO_SUCCESSOR_TRIGGER_YET`.
- `ena-field-guide` PR `#6` — active admission candidate; corrected live restore path still requires a controlled live drill and bounded portable smoke check before admission.
- Maintain Human-AI Workbench and ENA Field Guide when ENA work produces method/HOW material that belongs there; cite rather than mirror.
- Continue reality contact with actual adopters/contributors; do not manufacture a new mechanism experiment merely because the previous campaign is closed.
