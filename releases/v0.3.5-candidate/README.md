# Evolution-Native Agent Architecture (ENA) — v0.3.5 candidate.1

Status: **CANDIDATE / FIELD_VALIDATION / NOT_CURRENT**

This directory is the active v0.3.5 successor candidate after the frozen first candidate was independently falsified and judged `NEEDS_REVISION`. candidate.1 is not Current and is not a release.

## Purpose

**ENA exists to make sustained self-evolution viable.**

**Evolution is the purpose. Governance protects evolvability.**

ENA should make it easier for an Agent or Agent system to generate variation, learn from reality, retain useful adaptations, discard or archive harmful/stale adaptations, share evidence-bearing adaptations across a population, discover composition effects and emergence, and continue evolving after mistakes.

Safety, evidence, authority, recovery, history, and governance are enabling infrastructure. They must not become a general veto on novelty.

ENA is exploration-forward:

- variation may precede certainty;
- a mutation is not an improvement merely because it was intended as one;
- evidence-backed selection follows reality contact;
- internal self-structure may evolve, but external mandate cannot be self-minted;
- source adaptations/negative evidence may migrate and be locally re-tested;
- local success does not predict composed outcome;
- governance must preserve future correction and stop when further checks no longer change the decision.

## candidate.1 correction focus

Independent falsification of the frozen predecessor mechanically reproduced false-confidence paths in `ena_evolve.py`. candidate.1 therefore:

1. separates `lifecycle_state` from `selection_state`;
2. requires represented experimentation before formal positive/negative selection;
3. preserves negative/unknown selection across integration, archival, and migration;
4. allows receiver-side reselection only after real local experiment/evaluation while retaining source lineage;
5. rejects semantically contradictory migration packets;
6. makes closure read represented evolution state;
7. connects actual tool output to JSON-schema validation;
8. strengthens adversarial regression tests;
9. keeps the reference-tool boundary in the hot Runtime Kernel;
10. fixes zh-CN immutable-source-identity adoption guidance.

These are implementation/schema/document corrections. They do **not** add a new Constitution rule merely because bugs were found.

## Broader v0.3.5 themes

- explicit self-evolution telos;
- event + periodic/idle evolution wake;
- Variation Space and outcome-based selection;
- executable reference evolution metabolism;
- adaptation/negative-evidence migration and Evolution Commons;
- positive as well as negative composition emergence;
- Evolutionary Subject / Protected Subject / Continuity Vector;
- governance closure rather than infinite meta-review;
- lawful redaction/deletion without rewriting occurrence truth;
- effective-loaded-surface persistence evidence;
- English + Simplified Chinese semantic projection;
- Constitution concept map without deleting universal invariants;
- retirement of `MAINLINE / NOT_MAINLINE` as a future active adopter-facing axis.

## Navigation

1. `00-READ-ME-FIRST.md`
2. `CONSTITUTION-CONCEPT-MAP.yaml`
3. `01-CONSTITUTION.md`
4. `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`
5. `RUNTIME-ADOPTION-KERNEL.md`
6. `09-EVOLUTION-METABOLISM.md`
7. `10-LANGUAGE-PORTABILITY.md`

For Simplified Chinese, begin with `language-projections/zh-CN/00-READ-ME-FIRST.md`.

The Chinese projection is not a separate ENA. It preserves the same stable semantic IDs and must be judged by material decision meaning, not literal translation.

## Validation posture

Do not treat candidate.1 author intent, passing CI, predecessor expected behavior, or this README as acceptance evidence.

The frozen predecessor remains immutable evidence at its recorded commit/tree. Do not edit it in place, and do not modify `releases/current/` based on candidate.1 alone.

> **Variation first; selection by reality.**
>
> **Aggressive exploration does not create unowned external authority.**
