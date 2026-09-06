# ENA Evolution-to-Release Master Plan

Status: `ACTIVE_MASTER_PLAN / MAIN_CONTROL_PLANE / RAPID_CURRENT_SUCCESSION`

Updated: 2026-09-06

Historical release detail belongs in Git history, release records, reconciliation artifacts and old handoffs. This file is the live long-horizon plan.

## Goal

ENA must be able to **evolve quickly without lying about what changed**.

```text
TELOS / PURPOSE
      |
      v
WHAT / WHY semantic floor
      |
      +--> plural HOWs
      +--> Host bindings
      +--> evidence / reality contact
      |
      v
small successor
      |
      v
proportional validation
      |
      v
Current moves
      |
      v
field selection -> next successor
```

Two properties must coexist:

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
```

Old releases remain exact occurrence truth. `Current` should move frequently when a bounded better successor has paid the evidence cost appropriate to its actual change.

## Control plane

Permanent continuation surface:

`main`

Live state:

`NOW.md`

Current adoption identity:

`releases/current/CURRENT-BASELINE.yaml`

Rapid release method:

`research/methodology/RAPID-CURRENT-RELEASE-DISCIPLINE.md`

Research closure dispositions:

`research/evolution-inbox/EVOLUTIONARY-MEMORY-CLOSURE-DISPOSITIONS.yaml`

Branches are temporary work surfaces. No long-lived research branch is continuation authority.

## Release lanes

### R0 — Field patch / adoption surface

No Constitution or core-contract semantic delta. Examples: adopter entry, projection fidelity, routing, CI/validator hardening, packaging, enforcement visibility.

Admission is intentionally light:

```text
version identity
+ exact candidate bytes
+ relevant machine/regression PASS
+ rollback anchor
+ explicit residuals
+ release projection/readback
-> Current
```

Fresh independent validation may happen after admission as field evidence.

### R1 — Operational behavior change

Material HOW/tool/policy behavior changes without changing the binding semantic floor.

Use targeted adversarial and independent evidence when it can change the decision. Full cleanroom lifecycle is not automatic.

### R2 — Core semantic / high-consequence change

Constitution/core contract semantics, broad compatibility break, or high-consequence governance change.

Normally use:

```text
candidate -> adversarial validation -> freeze -> fresh independent falsification -> reconciliation -> release
```

Even here, every gate must pay epistemic rent.

## Current release objective

### v0.3.8

Classification:

`R0_FIELD_PATCH_ADOPTION_SURFACE`

Driver:

Issue `#201` + adoption/product usability evidence.

Primary value:

- research lineage separated from adopter payload;
- human and Agent quickstart surfaces;
- explicit soft/model vs machine vs external enforcement classes;
- repaired zh-CN hot-surface fidelity;
- concept-map retrieval fixes;
- broader semantic fixtures;
- regression gate against recurrence.

No new Constitution IDs are planned and no core-contract semantic delta is demonstrated.

The candidate's Main Gate and CodeQL have passed. Therefore the default next move is **release**, not another generic validation cycle.

Exact next action:

`PROMOTE_V038_THROUGH_R0_RAPID_CURRENT_LANE`

Metamemory research is independent and does not block v0.3.8.

## Research plan

The evolutionary-memory mechanism-discrimination campaign is almost closed.

Completed/narrowed work includes:

- semantic reachability;
- boundary memory;
- Developmental Inheritance / MDS;
- Temporal Assimilation / Developmental Order.

The only currently planned fresh-session primary is:

`Metamemory Update Policy v1`

After its formal adjudication, close the campaign unless a genuinely new non-derivable discriminator appears.

Do not manufacture one local experiment per metaphor merely because a coverage cell exists.

## Product evolution loop

After v0.3.8:

```text
field defect / friction / opportunity
-> record evidence
-> classify R0/R1/R2
-> cut smallest useful successor
-> run proportional gate set
-> move Current
-> keep predecessor recoverable
-> observe
```

Prefer v0.3.9 quickly over accumulating known defects for a distant v0.4.0.

Version numbers are identities, not prestige levels.

## Release-latency test

Every blocking step must answer:

```text
What exact failure can this catch?
Would that failure change admission?
Can a cheaper machine/targeted/field check catch it?
```

If not, remove or defer the blocker.

Release delay is itself governance friction and therefore must pay rent under ENA-CON-034 / ENA-CON-038.

## Field-validation posture

`FIELD_VALIDATION` is not a waiting room before a release becomes real. It means the released Current is intentionally exposed to bounded reality contact and may be superseded rapidly as evidence arrives.

```text
FIELD_VALIDATION -> OBSERVE -> SUCCESSOR
```

not:

```text
FIELD_VALIDATION -> FREEZE_CURRENT_FOR_WEEKS
```

Open longitudinal/cross-Host questions remain visible without blocking unrelated successors.

## Invariants

```text
SAME_VERSION -> SAME_EFFECTIVE_CONTENT
NEW_BETTER_SUCCESSOR -> MOVE_CURRENT
OLD_RELEASE -> PRESERVED_ROLLBACK_AND_HISTORY
OPEN_RESEARCH != RELEASE_BLOCKER_BY_DEFAULT
VALIDATION_INTENSITY -> MATERIAL_CHANGE
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
GOVERNANCE_MUST_CONVERGE
CONTROL_MUST_PAY_RENT
NO_CHANGE = VALID_RESEARCH_OUTCOME
BRANCH_EXISTS != PROJECT_AUTHORITY
```

## Closure rule

A release/research step stops when another bounded action no longer has plausible decision-changing value.

The project should optimize for **truthful evolutionary throughput**, not maximum ceremony per version.
