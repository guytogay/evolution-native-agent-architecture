# Evidence Applicability Boundary Audit — ENA v0.2.11 MAINLINE

Status: `RESEARCH_RESULT / NOT_PROMOTED`

Primary replay cases: `HAR-006`, `HAR-010`

## Result

**Current classification: `CLARIFICATION + SCHEMA/TEMPLATE TIGHTENING CANDIDATE`**

No current evidence requires a new Constitution principle.

The v0.2.11 Evidence Model already contains most of the conceptual ingredients: provenance, epoch, limitations, scoped trust, observation window, revalidation, host identity, and the rule that cross-domain transfer is a new claim. The machine-readable contracts do not consistently make the applicability envelope explicit enough to prevent evidence from one runtime subject/state/interval from being silently reused for another.

The evidence base now includes two structurally independent real cases:

- `HAR-006` — runtime instance/configuration-state transfer: observations from different gateway instances/states were incorrectly used to reason about the active 15-second server-side rate limit.
- `HAR-010` — temporal-interval transfer: a morning closure was locally truthful but could not be inherited unchanged as a whole-day completion claim after later activation/events.

These cases support the same boundary structure without requiring the same subsystem.

## Contract audit

| Surface | Subject/host | Epoch/state | Scope | Interval/time | Limitations | Revalidation | Instance/config-state applicability |
|---|---|---|---|---|---|---|---|
| `08-EVIDENCE-MODEL.md` | explicit in prose | epoch explicit; state partly contextual | explicit | observation window discussed | explicit | explicit | implied, not explicit |
| `CAPABILITY-EVIDENCE.template.yaml` | `host_identity` | `epoch_or_version` | per-capability `scope` | `last_verified_at` | not first-class per item | `revalidate_when` | missing |
| `capability-evidence.schema.json` | `host_identity` required | epoch optional | not schema-required | missing | missing | missing | missing |
| `COMPLIANCE-EVIDENCE.template.yaml` | `host_identity` | `host_epoch_or_version` | mostly requirement/integration context | `generated_at` only | explicit in many sections | present per requirement | missing |
| `compliance-evidence.schema.json` | host required | epoch optional | not explicit applicability envelope | missing | supported | supported | missing |
| `SESSION-REALITY.template.yaml` | `host_identity` | epoch + mode + continuity event | authority/runtime environment context | current session only | indirect | reposition/reconstitution semantics | no explicit runtime-instance/config-state identity |

## Replay vectors

### 1. Config default != current session override

Field support: `DERIVABLE`

The current model can record host/epoch and a limitation, but no portable field requires the evidence item to name the exact configuration state or override layer observed.

Likely fix layer: `CLARIFICATION + TEMPLATE/SCHEMA`.

### 2. Gateway restart != session override necessarily cleared

Field support: `DERIVABLE / AMBIGUOUS`

Continuity and epoch semantics exist, but the evidence contract does not explicitly bind an observation to a runtime instance/config-state lineage.

Likely fix layer: `CLARIFICATION + REVALIDATION CONTRACT`.

### 3. One channel healthy != whole system healthy

Field support: `EXPLICIT IN PRINCIPLE`

Existing scoped evidence and truthful health/protection claims already reject this transfer when scope is recorded honestly.

Likely fix layer: `EXAMPLE / NO NEW NORMATIVE RULE`.

### 4. Runtime instance A evidence != runtime instance B evidence

Field support: `MISSING AS FIRST-CLASS MACHINE FIELD`

This is the direct `HAR-006` failure shape.

Likely fix layer: `SCHEMA/TEMPLATE TIGHTENING`.

### 5. Old epoch evidence != current epoch evidence

Field support: `EXPLICIT/DERIVABLE`

Epoch and revalidation semantics exist, though individual evidence schemas do not uniformly require them.

Likely fix layer: `SCHEMA CONSISTENCY`.

### 6. Test environment evidence != production environment evidence

Field support: `DERIVABLE`

Environment assumptions are part of scoped trust/risk semantics but not consistently machine-bound to every evidence item.

Likely fix layer: `APPLICABILITY ENVELOPE`.

### 7. One authority/effect path verified != equivalent path verified

Field support: `EXPLICIT`

`ENA-CON-037` and enforcement-surface semantics already cover this strongly.

Likely fix layer: `NO NEW RULE`.

### 8. Completion at interval T1 != completion over expanded interval T1..T2

Field support: `EXPLICIT IN PROSE / WEAK IN MACHINE CONTRACT`

`HAR-010` shows that a locally truthful completion can become overbroad after silent temporal expansion. The Evidence Model already contains observation-window/revalidation semantics, but the main evidence schemas do not require an explicit observed-from/observed-to applicability interval.

Likely fix layer: `SCHEMA/TEMPLATE TIGHTENING`.

## Minimal research-level applicability envelope

A possible non-normative prototype for an evidence item is:

```yaml
applicability:
  subject_ref: ""
  host_identity: ""
  runtime_instance_ref: ""
  configuration_state_ref: ""
  epoch_or_version: ""
  scope: []
  observed_from: ""
  observed_to: ""
  environment_ref: ""
  transfer_constraints: []
  revalidate_when: []
```

This is a research prototype, not a v0.2.11 change.

## Current judgment

The strongest formulation remains:

> **Evidence validity does not imply evidence applicability.**

and operationally:

> **An observation supports only the subject, state, scope, and interval it actually observed.**

The second independent case strengthens the case that applicability is a recurrent boundary property, but it simultaneously weakens the case for a new Constitution rule because existing ENA prose already handles both failures when scoped evidence/revalidation semantics are applied correctly.

The most economical next move is therefore to prototype first-class applicability fields in research schemas/templates and test whether that removes the ambiguity.

## Next evidence / experiment needed

Before any normative promotion:

1. prototype applicability fields outside MAINLINE and map existing evidence records into them;
2. test whether `HAR-006` and `HAR-010` become unambiguous without adding normative semantics;
3. test one additional environment/production or subject-identity transfer case if available;
4. only consider a normative gap if false cross-boundary inheritance remains possible after explicit applicability + revalidation contracts.
