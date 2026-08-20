# ENA v0.3.0 Candidate 2 — Production Readiness & Living Evolution Integration

Status: `CANDIDATE / NOT_MAINLINE / NOT_PROMOTED`
Parent formal baseline: `v0.2.11 MAINLINE`
Parent candidate: `v0.3.0 Candidate 1`
Date: `2026-08-20`

Candidate 1 remains the comprehensive consolidation map. Candidate 2 does not replace that map; it adds the production-readiness layer needed to make ENA usable in real Agents while allowing field operation to feed future ENA evolution.

## Why Candidate 2 exists

Candidate 1 consolidated the broad ENA research surface, but production adoption needs a smaller executable selection surface:

1. a Production Core that can justify consequential claims and preserve recoverability;
2. a Shadow layer that observes cost, value, and failure without blocking work prematurely;
3. a Field Feedback path that lets every ENA-using Agent contribute incidents, friction, counterexamples, and observed value without receiving promotion authority;
4. a Recovery-History contract that prevents state rollback from silently erasing occurrence truth;
5. an ROI-oriented validation funnel so ENA does not become an experiment bureaucracy.

## Production architecture

```text
                 ENA Project / Evolution Plane
              variation / evidence / reconciliation
                         |
                   versioned adoption
                         v
                 Production Runtime Plane
            frozen profile + bounded experiments
                         |
                    field experience
                         |
                         +------------------------>
```

Production Runtime and Evolution Plane are deliberately separated.

A production Agent MUST NOT need to re-evaluate the whole ENA research map for every task. It runs a declared profile. The Evolution Plane handles broader research, reconciliation, and future candidate work.

## Production Core candidate families

The initial high-ROI Production Core is:

- Claim ↔ Evidence Support;
- Triggered Material Obligation Closure;
- Recovery State ≠ Historical Time / Monotonic History Across Restore;
- Layered Capability / Route Binding for hosts that switch models, routes, tools, credentials, adapters, or execution substrates.

These are prioritized because one mechanism can support many consequential claims: completion, deployment, recovery, capability qualification, stage admission, safety coverage, and authority qualification.

## Production Shadow families

Run as observation-first unless consequence requires enforcement:

- Viability Economics / ENA overhead;
- Projection freshness and source lineage;
- Agency-Preserving Uncertainty Resolution;
- Ecological Specialization;
- Influence Integrity / Persuasion Boundary;
- Capability Graph experiments.

Shadow observation MUST NOT be converted into a gate merely because it is measurable.

## Living Evolution loop

Every ENA-using Agent may act as a field node.

Field nodes may contribute:

- `INCIDENT`
- `NEAR_MISS`
- `FRICTION`
- `VALUE_OBSERVED`
- `COUNTEREXAMPLE`
- `PORTABILITY_FINDING`
- `NEW_VARIATION`
- `EVIDENCE_RESULT`

Contribution is intentionally broad.

`Contribution != Reconciliation != Promotion != Mainline Authority.`

No production Agent acquires authority to rewrite ENA merely because it uses ENA or can write to GitHub/Drive.

## Candidate 2 machine artifacts

- `schemas/claim.v1.schema.json`
- `schemas/evidence-support-relation.v1.schema.json`
- `schemas/triggered-obligation.v1.schema.json`
- `schemas/recovery-history-transition.v1.schema.json`
- `schemas/capability-route-binding.v1.schema.json`
- `templates/field-experience.v1.yaml`
- `profiles/production-core-v1.yaml`
- `PRODUCTION-READINESS.md`
- `VALIDATION-PLAN.md`
- `LIVING-EVOLUTION-LOOP.md`
- `RECOVERY-HISTORY-CONTRACT.md`
- `AGENT-LEARNING-ORDER.md`

Schema PASS proves structural conformance only. It does not prove semantic truth.

## Candidate 2 maxims

- `Production before perfection; not production without evidence.`
- `Run a frozen profile; evolve in a separate plane.`
- `Batch variation; concentrate expensive selection.`
- `Use the cheapest evidence that can honestly support the decision.`
- `No experiment without a decision branch.`
- `Rollback state; preserve history.`
- `Every field node may contribute variation; none receives automatic promotion authority.`
- `Production is evidence, not automatic truth.`
- `ENA must pay rent in production.`

## Current status

Candidate 2 is a productionization candidate, not a promoted ENA release.

Formal Mainline remains `v0.2.11 MAINLINE`.

Candidate 1 remains the comprehensive research/consolidation parent. Candidate 2 adds production selection, machine-contract prototypes, field feedback, and recovery-history correction.
