# Evolution-Native Agent Architecture (ENA) — v0.3.5 candidate.2

Status: **CANDIDATE / FIELD_VALIDATION / NOT_CURRENT**

This directory is the active v0.3.5 successor candidate. The frozen first candidate was independently judged `NEEDS_REVISION`; frozen candidate.1 then received `TARGETED_REVALIDATION_SUPPORTED_WITH_RESIDUALS` from the same DSH falsifier. candidate.2 closes the concrete release-decision residuals and is still neither Current nor a release.

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

## Candidate correction lineage

The first frozen candidate exposed false-confidence paths in `ena_evolve.py`. candidate.1 repaired the material state-machine, migration, closure, and schema-wiring defects by separating lifecycle from selection, requiring represented experiment before formal selection, preserving negative/unknown migration lineage, permitting receiver reselection only after local reality contact, and connecting real tool output to schemas and adversarial regression.

The same falsifier then found only residuals. candidate.2 closes the release-decision items without changing the Constitution:

1. CLI rejects invalid `source_lifecycle_state` rather than relying on schema validation alone;
2. CLI rejects forged `source_authentication` rather than propagating a self-asserted trust label;
3. CLI validates the fixed `transfer_status` claim;
4. committed inherited-regression output is synchronized with its generating suite and CI checks that regeneration stays clean;
5. candidate.1 adversarial regressions remain active and candidate.2 adds residual-closure probes.

No Constitution rule was added merely because an implementation bug was found.

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

Do not treat candidate.2 author intent, passing CI, predecessor verdicts, or this README as acceptance evidence.

Frozen predecessors remain immutable evidence at their recorded commit/tree identities. Do not edit them in place, and do not modify `releases/current/` based on candidate.2 alone.

> **Variation first; selection by reality.**
>
> **Aggressive exploration does not create unowned external authority.**
