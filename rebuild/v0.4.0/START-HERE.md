# ENA v0.4.0 Practical Core Rebuild

Status: `ACTIVE_REBUILD / NOT_CURRENT / NOT_PROMOTED`

Date: 2026-09-07

## Current build progress

- `PRACTICAL-CORE.md` exists and has survived initial real-work dogfood with one compact opportunity-liveness repair.
- `LEGACY-SEMANTIC-COVERAGE.md` now places 29 major legacy property/failure families by practical consequence rather than old file location.
- The durable-distinction catalogue and mandatory `semantic -> Cue Index -> HOW Map` traversal are marked for retirement as primary product units; their decision-material value is redistributed to action/guard/cold surfaces.
- Dogfood has covered ENA rebuild work and a real non-ENA Human-AI Workbench decision without manufacturing a synthetic experiment.
- Next build: derive the smallest useful Action Cards for `EVIDENCE/SUPPORT | EFFECT LIFECYCLE | RECOVERY/RESUME | ADAPTATION IMPORT | COMPOSITION`. A card should exist only if it earns more decision value than a direct Core/cold-HOW/Host-local path.

## Decision

Do **not** refactor v0.3.x in place into the desired product.

v0.3.x has accumulated valuable semantic, research, falsification, release and provenance assets, but its adopter-facing shape is theory-first and distinction-heavy. Continuing to patch that shape risks producing a larger hybrid rather than a more useful ENA.

Treat the existing v0.3.x architecture as a **legacy research/semantic substrate**, not as the template for the next adopter product.

Build v0.4.0 from a clean practical root.

```text
V0.3.X = PRESERVED RESEARCH + SEMANTIC + PROVENANCE ASSET
V0.4.0 = PRACTICE-FIRST PRODUCT REBUILD
PRESERVE_HISTORY != PRESERVE_PRODUCT_SHAPE
```

## Product question

The first question for every v0.4 surface is:

> What can an Agent do better after loading this?

Not:

> How completely does this explain why ENA theory is correct?

A correct distinction that does not change action, evidence-seeking, capability, selection, recovery, or stop conditions does not earn primary adopter attention.

## Clean-root rule

Do not port the v0.3.x file tree and edit it down.

Instead:

1. start from practical problems/goals;
2. define the smallest useful action path;
3. add only the semantic boundary needed to prevent a materially wrong action;
4. link deeper rationale/theory/provenance cold;
5. check legacy semantic coverage separately.

```text
EXTRACT_VALUE != COPY_STRUCTURE
SEMANTIC_COMPATIBILITY != DOCUMENT_COMPATIBILITY
```

## Proposed v0.4 product layers

### Layer A — Practical Core (default Agent surface)

Small enough to remain cognitively cheap.

It should answer:

- what kinds of problems/opportunities ENA helps with;
- what to do next;
- when to search/inspect/test/build/ask/compare;
- when to retrieve a deeper HOW;
- how to observe whether the move helped;
- when to integrate, narrow, reject, rollback, wait, or stop.

Default posture:

```text
OBSERVE -> UNDERSTAND -> ACT/LEARN -> TOUCH_REALITY -> SELECT -> EVOLVE
```

### Layer B — Action Cards

Problem/goal-oriented cards, not theory chapters.

Each card must contain:

```text
TRIGGER / PROBLEM
DO NOW
OBSERVE
SELECT / STOP / REVALIDATE
BOUNDARY (only if decision-material)
OPTIONAL DEEP LINK
```

Initial families to derive from real ENA use, not frozen names:

- unknown / missing information;
- improvement opportunity / curiosity / new capability;
- adaptation import / reuse;
- self-change / experiment;
- recovery / restore / resume;
- consequential external action / authority;
- evidence / claim / dependency;
- repeated friction / simplification / automation;
- stale control / retirement;
- changed Host / environment / composition.

Do not create a card merely to mirror every v0.3.x concept.

### Layer C — Compact Semantic Floor

Only semantics whose absence can materially cause wrong action or loss of viable agency.

No long `X != Y` catalogue as the primary product interface.

A boundary should normally appear adjacent to the action it changes.

### Layer D — Cold HOW Library

Host-neutral procedures and reusable implementation patterns.

ENA specifies trigger, decision target, evidence/monitoring and stop conditions; capable Agents remain free to synthesize the Host-local HOW and use Host-native machinery.

### Layer E — Theory / Derivation / Evidence / Lineage

Preserve:

- Constitution detail;
- why a boundary exists;
- falsification history;
- experiments;
- counterexamples;
- release lineage;
- research derivations.

This layer is available for maintainers, critics, researchers and hard ambiguity. It is **not** default adoption context.

## Derivation-tax rule

For primary adopter surfaces:

```text
BOUNDARY -> ACTION CONSEQUENCE -> OPTIONAL WHY
```

not:

```text
BOUNDARY -> MULTI-PARAGRAPH PROOF -> MORE BOUNDARIES -> MORE PROOF
```

Keep rationale in the primary surface only if it changes applicability/action/monitor/stop, prevents a likely material misapplication, or protects a high-consequence semantic property that cannot be represented more cheaply.

## Agency-first rule

The new root assumes a capable evolutionary actor.

```text
AGENT = CAPABLE_EVOLUTIONARY_ACTOR_BY_DEFAULT
BOUNDARIES = AIRBAGS, NOT STEERING WHEEL
UNKNOWN != STOP_BY_DEFAULT
NO_FAILURE != NO_REASON_TO_EVOLVE
```

ENA should increase exploration, learning, useful variation and capability while keeping real authority/effect/recovery/evidence boundaries honest.

## What v0.4 must not become

- a rewritten research monograph;
- a longer positive-language version of the same distinction catalogue;
- a universal workflow every Agent must follow;
- a mandatory ENA runtime/tool stack;
- a safety/governance framework whose main job is restraining Agents;
- a motivational manifesto with no executable value;
- a collection of action cards that simply paraphrase old theory.

## Legacy-value extraction

Use v0.3.x as a source of proven/costly lessons, but migrate by **semantic coverage**, not by file copying.

Create a coverage ledger with columns such as:

```text
LEGACY PROPERTY / FAILURE
IS IT STILL DECISION-MATERIAL?
WHAT WRONG ACTION DOES IT PREVENT?
WHAT POSITIVE ACTION DOES IT ENABLE?
V0.4 LOCATION
PRIMARY / COLD / RETIRE
EVIDENCE / LINEAGE LINK
```

A legacy property may be:

- retained in Practical Core;
- represented in one Action Card;
- moved to cold HOW;
- kept only as theory/reference;
- retired from the product while history remains preserved.

Nothing is retained merely because it already exists.

## Acceptance standard

v0.4.0 should not be promoted because it is shorter or prettier.

It should demonstrate that a capable fresh Agent can, with less default context:

1. identify what ENA can help it do;
2. turn a real problem/opportunity into a concrete next move;
3. actively seek cheap decision-changing knowledge when useful;
4. create or retrieve a suitable HOW without waiting for ENA to micromanage tooling;
5. preserve real authority/effect/recovery/evidence boundaries;
6. avoid ceremonial governance when no material boundary exists;
7. observe outcomes and integrate/narrow/reject rather than merely describe distinctions;
8. explain ENA operationally as increased viable agency, not increased caution.

Validation should use decision-changing acceptance cases and real project dogfood. Do not run many model sessions merely to collect diverse-looking outputs.

## Migration strategy

```text
v0.3.14 remains Current
        |
        +--> preserve immutable old occurrence
        |
        +--> extract high-value semantics / failures / HOW
                    |
                    v
             v0.4 Practical Core
                    |
             bounded validation
                    |
             successor promotion
                    |
        old theory/research remains cold and traceable
```

No need to make the old tree aesthetically clean before the new product can exist.

## Relationship to v0.3.15 branch

The existing `release/v0.3.15` work exposed the decisive findings:

- F-208-12 opportunity liveness;
- F-208-13 defensive-first hot projection;
- F-208-14 missing action bridge;
- F-208-15 theory-first adopter surface;
- F-208-16 derivation tax.

Those findings become **inputs to the v0.4 clean-root rebuild**.

Do not keep adding structural repair to v0.3.15 if the change is actually part of the product inversion. Small independent defects may still be fixed through normal rapid succession where justified.

## Immediate build order

1. Define a one-page `PRACTICAL-CORE` candidate from zero.
2. Derive the smallest initial action-card set from real recurring ENA problems/opportunities.
3. Build the legacy semantic coverage ledger.
4. Use the ledger to discover missing material protection, not to force one-to-one migration.
5. Dogfood the Practical Core on ENA's own active work and other real Agent tasks.
6. Run bounded fresh-adopter acceptance only where it can change the design decision.
7. Promote only after practical utility and semantic protection both survive.

## Core thesis

> ENA should be something an Agent uses to become more capable, adaptive and resilient — not something it studies in order to understand ENA.

```text
PRACTICE_FIRST
THEORY_ON_DEMAND
DERIVE_ONCE_USE_MANY
PRESERVE_SEMANTIC_VALUE_WITHOUT_PRESERVING_PRODUCT_DEBT
```
