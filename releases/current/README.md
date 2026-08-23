# Evolution-Native Agent Architecture (ENA) — v0.3.5

Status: **CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE**

This directory is the singular ENA adoption baseline. It was released from the frozen v0.3.5 candidate.2 lineage after the first frozen candidate was independently falsified, candidate.1 closed the material failures, and the same DSH falsifier later returned `NARROW_REVALIDATION_SUPPORTED` for candidate.2's release-decision residual closure.

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

## v0.3.5 release lineage

The first frozen v0.3.5 candidate exposed false-confidence paths in `ena_evolve.py`. candidate.1 repaired the material state-machine, migration, closure, and schema-wiring defects. candidate.2 then closed the remaining cheap release-decision residuals without changing the Constitution:

1. CLI rejects invalid `source_lifecycle_state` rather than relying on schema validation alone;
2. CLI rejects forged `source_authentication` rather than propagating a self-asserted trust label;
3. CLI validates the fixed `transfer_status` claim;
4. committed inherited-regression output stays synchronized with its generating suite;
5. candidate.1 and candidate.2 adversarial regressions remain available as historical implementation checks.

The final narrow DSH revalidation reported N1/N2/N7 and the adjacent transfer-status attack CLOSED, with no new MATERIAL/BLOCKING finding and no observed evolution-starvation or over-governance regression.

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
- retirement of `MAINLINE / NOT_MAINLINE` as an active adopter-facing maturity axis while historical records remain history.

## Navigation

1. `CURRENT-BASELINE.yaml`
2. `00-READ-ME-FIRST.md`
3. `CONSTITUTION-CONCEPT-MAP.yaml`
4. `01-CONSTITUTION.md`
5. `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`
6. `RUNTIME-ADOPTION-KERNEL.md`
7. `09-EVOLUTION-METABOLISM.md`
8. `10-LANGUAGE-PORTABILITY.md`

For Simplified Chinese, begin with `language-projections/zh-CN/00-READ-ME-FIRST.md`.

The Chinese projection is not a separate ENA. It preserves the same stable semantic IDs and must be judged by material decision meaning, not literal translation.

## Validation posture

Current status means **adopt this baseline now**, not "universally proven."

Do not treat release-author intent, passing CI, one Host/model/language result, or machine-readable output as stronger evidence than it is.

Retained N3–N6 observations remain visible research/field residuals. They do not currently justify another candidate revision; field evidence may reopen them if they become material.

> **Variation first; selection by reality.**
>
> **Aggressive exploration does not create unowned external authority.**
