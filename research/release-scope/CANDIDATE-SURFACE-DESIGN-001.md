# Candidate Surface Design 001 — Minimal inhabitable release package

Status: `RELEASE_SCOPE_DESIGN / CANDIDATE_SURFACE_WORKING_DECISION / CURRENT_UNCHANGED / VERSION_UNASSIGNED`

Date: 2026-08-27

## Goal

Define the smallest release-local surface that makes ENA practically inhabitable without turning the entire research tree into adopter cargo.

The candidate should preserve the v0.3.6 semantic trunk unless a later release-scope finding demonstrates a real semantic delta.

```text
SEMANTIC_TRUNK_STABLE
+
OPERATIONAL_DISTRIBUTION_SURFACE
+
OPTIONAL_REFERENCE_LIBRARY
+
V2_PRACTICAL_TOOLING
```

## Candidate package shape

Working layout:

```text
releases/<candidate>/
  README.md
  00-READ-ME-FIRST.md
  CURRENT-BASELINE.yaml
  01-CONSTITUTION.md
  02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md
  03-ROLES-AND-DEVELOPMENTAL-STAGES.md
  04-CAPABILITY-MAP.md
  05-CORE-OPERATIONAL-CONTRACTS.md
  06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md
  07-ADOPTION-AND-FIELD-VALIDATION.md
  08-RELEASE-DISCIPLINE.md
  09-EVOLUTION-METABOLISM.md
  10-LANGUAGE-PORTABILITY.md
  RUNTIME-ADOPTION-KERNEL.md
  AGENT-ADOPTION-INSTRUCTION.md
  LITE-ADOPTION-INSTRUCTION.md

  operational/
    README.md
    CUE-INDEX.md
    HOW-MAP.md
    REFERENCE-INDEX.yaml
    procedures/
      PURPOSE-RELATIVE-CONTINUITY.md
      STANDING-INPUT.md
      CONTROL-RETIREMENT.md
    patterns/
      EVOLUTION-COMMONS.md
      HOST-MAPPINGS.md

  references/
    REFERENCE-MANIFEST.yaml
    general/
      retrieval-obligation/
      wait-state/
      authority-lease/
      effect-lifecycle/
      recovery-adapter/
    advanced/
      evidence-envelope/
      evidence-dependency-map/
      contested-authorship/

  schemas/
  templates/
  tools/
    ena_evolve_v2.py
    legacy/
      ena_evolve_v1_2.py

  language-projections/
    semantic fixtures / zh-CN projection
```

Exact filenames may change during candidate build. The functional separation is the decision.

## Minimum adopter traversal

A new adopter should not need to inspect `research/`.

```text
00-READ-ME-FIRST
-> RUNTIME-ADOPTION-KERNEL
-> operational/README
-> operational/CUE-INDEX when the problem needs a concrete HOW
-> operational/HOW-MAP
-> procedure / reference / Host pattern
-> act or honest WAIT / UNKNOWN / not-applicable
```

`operational/HOW-MAP.md` is a cold library. It is not an always-loaded prompt.

## Hot/cold boundary

Always-hot candidate content should remain small:

- telos;
- durable distinctions/cues in `RUNTIME-ADOPTION-KERNEL.md`;
- one pointer that concrete HOW resolution belongs in the operational library.

Do not copy the whole Cue Index or reference schemas into the resident kernel.

```text
HOT_KERNEL -> KNOW_WHEN_TO_RETRIEVE_HOW
HOT_KERNEL != HOW_LIBRARY
```

## Machine-readable optionality

`CURRENT-BASELINE.yaml` should point to a release-local `references/REFERENCE-MANIFEST.yaml` and explicitly state that bundled references are not complete-adoption requirements.

The reference manifest should carry packaging-role metadata such as:

```text
role
required_for_complete_adoption
default_activation
normative_semantic_authority
path
applicability_summary
```

These fields describe packaging/use, not ENA ontology.

Package validation should reject a candidate if a selected optional reference is accidentally marked required/default-active without an explicit release-scope decision.

## Top-level Current-file delta matrix

### Material adopter-facing updates expected

- `README.md` — describe Operational Architecture release value and selected practical surfaces;
- `00-READ-ME-FIRST.md` — route adopters through the new operational entrypoint;
- `CURRENT-BASELINE.yaml` — identify operational entrypoints, reference manifest, v2 practical tool, optionality;
- `RUNTIME-ADOPTION-KERNEL.md` — add the operational HOW retrieval path and update the tool boundary;
- `AGENT-ADOPTION-INSTRUCTION.md` — explain operational adoption and optional reference use;
- `LITE-ADOPTION-INSTRUCTION.md` — make clear that bundled references are not activated merely by complete/LITE adoption;
- `07-ADOPTION-AND-FIELD-VALIDATION.md` — bind reference/Host/field evidence honestly;
- `09-EVOLUTION-METABOLISM.md` — point practical v2 usage to the selected helper and label v1.2 legacy;
- `10-LANGUAGE-PORTABILITY.md` — include operational HOW projection coverage and new fixtures;
- `CHANGELOG.md`, `LINEAGE.md`, package/release manifests — normal release identity/lineage updates.

### Pointer/minor packaging update possible

- `06-EVOLUTION-KNOWLEDGE-AND-OPEN-PARTICIPATION.md` may point to the release-local Commons HOW pattern without changing Commons semantics;
- `08-RELEASE-DISCIPLINE.md` may need packaging/manifest identity wording only if new package surfaces require it.

### Preserve unchanged unless a real semantic contradiction appears

- `01-CONSTITUTION.md`;
- `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`;
- `03-ROLES-AND-DEVELOPMENTAL-STAGES.md`;
- `04-CAPABILITY-MAP.md`;
- `05-CORE-OPERATIONAL-CONTRACTS.md`;
- existing v2 evolution/adaptation schemas and consistency semantics.

This is intentional. A practical release does not need gratuitous semantic churn.

## Tool surface

Preferred candidate path:

```text
tools/ena_evolve_v2.py
```

The candidate may retain the old v1.2 tool only in an explicitly legacy/compatibility path.

Do not expose two equally prominent evolution tools with different semantic generations.

## Reference library boundary

General and advanced references are package cargo, but not semantic authority.

The operational map should route to them only when applicable. A Host-native implementation may satisfy the same property without instantiating the bundled reference schema.

```text
REFERENCE_IMPLEMENTATION
!= REQUIRED_IMPLEMENTATION
```

## Research stays outside adopter package

Do not ship raw:

- archaeology ledgers;
- historical review prompts/results unless release evidence requires them;
- progressive/compaction/composition test laboratories;
- mesocosm plans;
- raw Host experiments;
- abandoned branch internals.

Their conclusions/lineage remain durable in repository research.

## Acceptance for package-surface stability

The surface is stable enough for candidate assembly when:

1. a new adopter can reach a concrete HOW without research paths;
2. bundled-reference optionality is explicit in prose and machine-readable metadata;
3. hot runtime surface remains bounded;
4. zh-CN coverage does not hide the new practical HOW layer behind English-only entry material;
5. deferred research remains discoverable without appearing required;
6. top-level semantic files are not edited merely to make the release look larger.

`CURRENT_CHANGE = NO`
