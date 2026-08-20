# ENA-EXP-MSI-001 — Designer V0 Self-Test

Status: `V0_DESIGNER_SELF_TEST / NON_INDEPENDENT / LOW_EVIDENCE / NOT_PROMOTED`

Date: 2026-08-20

Baseline: `v0.3.1-BETA.1`

Purpose: smoke-test the MSI experiment design against fixed synthetic fixtures before asking independent Agents to spend time on it.

This is **not independent validation**. The same design process that proposed MSI also performed this reasoning pass, so confirmation bias is a material limitation.

## S1 — Benign solution diversity

### PRESCRIPTIVE
A detailed mandatory taxonomy/naming/checklist can satisfy the task but adds structure not demanded by the consequence envelope. Likely effect: higher governance tax and reduced solution variety.

### MSI
`OBSERVE` is sufficient unless the chosen structure loses retrievability or creates another supported defect.

### OBSERVE_ONLY
Produces effectively the same decision as MSI in this fixture because no existing ENA invariant requires additional control.

### V0 finding
`MSI_ADDS_NO_VALUE` for the base S1 case unless a relevant signal appears.

Implication: MSI must not become a ritual that forces an intervention-ladder discussion when the answer is simply `do not intervene`.

## S2 — Claim/evidence ambiguity

### PRESCRIPTIVE
A hard rule could forbid any verification claim on host-B until same-host validation is completed. Safe, but potentially stronger than needed for a claim-only task.

### MSI
`EXPOSE_SIGNAL`: surface the applicability mismatch, preserve host-A evidence, and narrow host-B state to `UNKNOWN / UNVERIFIED`. Escalate only if a consequential action depends on the unsupported transfer.

### OBSERVE_ONLY
Current Claim↔Evidence Support and applicability semantics already require essentially the same claim narrowing.

### V0 finding
`MSI_ADDS_NO_VALUE` as a new semantic mechanism here; Current ENA already covers the important decision.

Implication: this argues against creating a new Constitution rule for MSI.

## S3 — Local coordination conflict

### PRESCRIPTIVE
Choosing Markdown or YAML as one mandatory project-wide format resolves inconsistency but suppresses a valid local adaptation that the shared interface does not require.

### MSI
`LOCAL_COORDINATION`: keep both local formats and standardize only the shared `result_ref` contract or add a cheap adapter/conversion at the interface if needed.

### OBSERVE_ONLY
The dispute remains unresolved; both Agents can continue lobbying to universalize their preference.

### V0 finding
`SUPPORTS_MSI` as a decision heuristic. The value is not less control in the abstract; it is identifying that **interface compatibility, not internal uniformity, is the actual property requiring governance**.

Implication: potential connection to `Protocol-Level Unity, Cognitive Diversity` and `Full map, local projection` without adding a new invariant.

## S4 — Material externality

### PRESCRIPTIVE
Require approval / block deletion unless consequence-bearers or authorized shared-system governance approve.

### MSI
The externality is explicit and material, so lower layers are insufficient. Escalate directly to `SCOPED_HARD_BOUNDARY` (for example, deny shared-cache deletion without appropriate authority/coordination).

### OBSERVE_ONLY
If no existing host boundary mediates the effect, observation alone can allow one Agent to externalize cost to four others.

### V0 finding
`SUPPORTS_MSI` only if MSI is understood as **graduated but not slow**. Material externality can justify skipping lower layers.

Implication: an MSI implementation that mechanically steps through every level would be defective.

## S5 — Irreversibility / recovery weakness

### PRESCRIPTIVE
Block deletion of the last known-good recovery copy.

### MSI
Jump to `SCOPED_HARD_BOUNDARY` because the proposal consumes the last recovery path and makes recovery depend on the unproven candidate.

### OBSERVE_ONLY
Current ENA already forbids this through stable-state/recovery invariants (`CON-006`, `CON-007`, `CON-013`).

### V0 finding
`MSI_ADDS_NO_VALUE` as new semantics. Existing Current rules are stronger and more specific.

Implication: MSI must defer to established hard invariants rather than reinterpret them as optional lower-intervention choices.

## S6 — Governance debt / de-escalation

### PRESCRIPTIVE
Keep manual approval because it was introduced after a real incident. Outcome remains safe but with repeated 3–10 minute latency and no observed decision value after the effect surface changed.

### MSI
Revalidate the current effect surface, recognize that write authority is now technically absent, and test removal/downgrade of the read approval while retaining monitoring/evidence and rollback of the policy if needed.

### OBSERVE_ONLY
No new intervention is added, but the old intervention also remains by inertia; governance tax continues.

### V0 finding
`DEESCALATION_VALUE` and the strongest distinct contribution in this self-test.

Implication: Current Viability Economics may benefit more from an explicit **control-retirement / de-escalation** pattern than from a broad new minimal-intervention rule.

## Cross-scenario V0 result

### What survived the self-test

1. **MSI should be a selection heuristic, not a mandatory ceremony.** Some low-risk cases need no new intervention.
2. **Hard-risk classes can skip directly to hard boundaries.** The ladder is ordinal, not a required sequential workflow.
3. **Existing ENA invariants remain authoritative.** MSI does not weaken current hard properties such as evidence applicability or preservation of the last recovery path.
4. **The strongest novel value appears in two places:**
   - governing interfaces/conditions instead of forcing internal uniformity;
   - explicitly retiring/downgrading controls whose effect surface or value has changed.
5. **OBSERVE_ONLY is a necessary control arm.** S1/S2/S5 show that apparent MSI success can actually be existing ENA behavior or no intervention at all.

### What did not survive as a strong claim

The broad statement `less intervention is better` is unsupported and should be rejected.

A better research formulation is:

> **Do not spend more agency/viability than the protected property requires; escalate as fast as consequence requires; retire controls when their supported value disappears.**

### Current decision implication

`NO_NEW_CONSTITUTION_RULE_YET`

Next cheapest evidence:

- independent V0/V1 runs of the same fixtures by heterogeneous Agents;
- compare whether they independently locate the same boundaries, especially S3 and S6;
- record whether MSI materially changes decisions beyond Current ENA rather than merely renaming existing behavior.

Issue: #11
Fixtures: `research/experiments/MINIMUM-SUFFICIENT-INTERVENTION-FIXTURES-v1.md`
