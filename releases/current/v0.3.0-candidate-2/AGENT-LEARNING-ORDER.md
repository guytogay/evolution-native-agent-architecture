# Agent Learning Order — ENA v0.3.0 Candidate 2 Pack

Use this order for Agents learning ENA from a repository clone or offline ZIP.

1. `PROJECT-HUB.md`
2. `README.md`
3. `releases/v0.2.11/README.md`
4. `releases/current/v0.3.0-candidate-1/README.md`
5. `releases/current/v0.3.0-candidate-1/COMPREHENSIVE-CONSOLIDATION.md`
6. `releases/current/v0.3.0-candidate-2/README.md`
7. `releases/current/v0.3.0-candidate-2/PRODUCTION-READINESS.md`
8. `releases/current/v0.3.0-candidate-2/RECOVERY-HISTORY-CONTRACT.md`
9. `releases/current/v0.3.0-candidate-2/VALIDATION-PLAN.md`
10. `releases/current/v0.3.0-candidate-2/LIVING-EVOLUTION-LOOP.md`
11. `releases/current/v0.3.0-candidate-2/profiles/production-core-v1.yaml`
12. Candidate 2 schemas/templates as needed.
13. `CONTRIBUTING.md` before contributing to the ENA project.

## Required interpretation

- `v0.2.11 MAINLINE` is the current **formal normative baseline**. It defines what may honestly be claimed as promoted ENA semantics.
- Candidate 1 and Candidate 2 are not promoted Mainline, but `NOT_PROMOTED` does **not** mean `READ_ONLY` or `DO_NOT_APPLY`.
- Candidate 1 is primarily the broad research/consolidation map and should normally be used as reference unless a specific mechanism is deliberately selected for testing.
- Candidate 2 is explicitly the **active productionization candidate** and is intended to be applied in bounded Shadow / Canary / experimental production where the host has authority to do so.
- During a Candidate 2 pilot, the effective operating stack should be reported as:

```text
ENA v0.2.11 MAINLINE
+ v0.3.0 Candidate 2 experimental production profile / selected mechanisms
+ declared host-local extensions
```

- Do not report a Candidate 2 pilot as `v0.3.0 MAINLINE`, `fully promoted`, or universally validated.
- Candidate 2 must not silently weaken or override v0.2.11 Mainline invariants. If a Candidate mechanism conflicts with Mainline, preserve the conflict and use the promoted invariant until reconciliation explicitly resolves it.
- Learning a candidate does not authorize implementing every candidate mechanism.
- Using ENA does not grant authority to promote ENA changes.
- Local field experience is contribution evidence, not automatic Universal truth.

## For production adopters

**Do apply Candidate 2 selectively. It is not merely reading material.**

Start from:

`releases/current/v0.3.0-candidate-2/profiles/production-core-v1.yaml`

Recommended adoption posture:

1. keep v0.2.11 Mainline as the normative floor;
2. activate the selected Candidate 2 Production Core mechanisms as an explicitly experimental overlay;
3. run Shadow families observation-first;
4. use Canary enforcement for bounded/reversible workloads before widening consequence/authority;
5. record Candidate identity and active mechanism/profile in local state;
6. contribute real incidents, friction, value, counterexamples, and evidence through the Field Experience path;
7. widen, simplify, merge, replace, or retire Candidate mechanisms based on evidence rather than candidate status alone.

The broader Candidate documents should be consulted when a relevant failure occurs, a mechanism is being evaluated, field evidence is being contributed, or reconciliation/research is explicitly requested.

> Formal baseline answers: **what ENA has already promoted.**
>
> Active Candidate answers: **what ENA is deliberately testing in real operation next.**
