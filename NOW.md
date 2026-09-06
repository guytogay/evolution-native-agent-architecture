# ENA — NOW

This is the default live project-status surface.

## Current

- `v0.3.8 / CURRENT / FIELD_VALIDATION`
- authority: `releases/current/CURRENT-BASELINE.yaml`
- effective adopter package: `releases/current/`
- promotion PR: `#206`
- promotion merge: `625973fb3aa8cc503d0860d2c5f07e021c4dc266`
- predecessor/rollback/history: `v0.3.7`

v0.3.8 was admitted through the `R0_FIELD_PATCH_ADOPTION_SURFACE` lane after prospective Current Validate + Main Gate PASS.

## Release posture

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
PRESERVE_OLD_RELEASES + MOVE_CURRENT_QUICKLY
```

Method:

`research/methodology/RAPID-CURRENT-RELEASE-DISCIPLINE.md`

- R0 — adoption/field patch: machine/regression/readback + rollback; fresh independent evidence may be post-release.
- R1 — operational behavior change: targeted adversarial/independent evidence when decision-material.
- R2 — core semantic/high consequence: heavy freeze/fresh falsification by default.

Open unrelated research is not a release blocker.

## v0.3.8 field-selection focus

v0.3.8 separates adopter payload from research lineage, adds product-first human/Agent entrypoints, exposes enforcement class explicitly, repairs zh-CN hot-surface fidelity and retrieval mappings, expands semantic fixture v3 to 18 cases, and guards the product surface against recurrence.

Primary predecessor evidence: Issue `#201`.

If field use exposes a decision-bearing defect, prefer a bounded `v0.3.9` successor rather than keeping known bad Current bytes in place.

## Research

The evolutionary-memory campaign is closing.

Closure dispositions:
`research/evolution-inbox/EVOLUTIONARY-MEMORY-CLOSURE-DISPOSITIONS.yaml`

Closure audit:
`research/field-validation/2026-09-06-evolutionary-memory-open-track-closure-audit.md`

### Active experiment

**Metamemory Update Policy v1** remains preregistered; primary collection has not started.

Arms:

```text
S0 — STATIC_EQUAL
G1 — GLOBAL_RECENT3
C1 — CONTEXT_RECENT3
C2 — CONTEXT_REVERSIBLE3
```

Initial sample: four one-shot fresh Temporary Chats. Maximum eight only under the frozen all-arm replication trigger. No selective extra runs.

Research next action:

`COLLECT_METAMEMORY_UPDATE_POLICY_V1_INITIAL_PRIMARY`

Metamemory is the only currently planned fresh-session primary. After adjudication, close the campaign unless a genuinely new non-derivable discriminator appears.

## Project rules

```text
SAME_VERSION -> SAME_EFFECTIVE_CONTENT
NEW_BETTER_SUCCESSOR -> MOVE_CURRENT
OPEN_RESEARCH != RELEASE_BLOCKER_BY_DEFAULT
EXPERIMENTS_MUST_PAY_EPISTEMIC_RENT
GOVERNANCE_MUST_CONVERGE
CONTROL_MUST_PAY_RENT
```

## Open work

- #150 — predecessor/field-validation lineage; reconcile toward v0.3.8 field tracking
- #153 — project-operation simplification
- #201 — field evidence that drove v0.3.8; close when reconciliation/readback is recorded
