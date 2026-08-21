# 5. Core Operational Contracts

## 5.1 Claim ↔ Evidence Support

Consequential claims are first-class operational objects. Evidence validity alone does not establish that evidence supports a particular claim.

For material claims preserve:

- claim identity and asserted scope;
- evidence actually observed and its scope;
- support relation between evidence and claim;
- transfer/equivalence/invariance evidence if the claim crosses subject/instance/configuration/epoch/time/environment boundaries;
- material source/provenance lineage needed to distinguish independent observation from derivative propagation;
- limitations on causal attribution where multiple interventions or sources could explain the observed outcome.

The claimed envelope must remain inside the supportable evidence envelope unless a separately evidenced transfer relation justifies expansion.

Propagation, paraphrase, repetition, caching, mirroring, or multi-Agent agreement derived from the same originating evidence do not create independent corroboration. Preserve materially relevant imported/transformed provenance; do not launder derivative evidence into a new local source.

Distinguish:

`recurrence != independent corroboration`

`absence of evidence != evidence of absence`

`evidence truth != causal attribution usability`

Where silence may mean interruption, loss, or incomplete replay, a material completeness/closure claim requires positive closure evidence rather than absence of further messages alone.

This applies especially to completion, deployment, recovery, capability qualification, stage admission, enforcement/safety coverage, authority qualification, equivalence claims, and independent-review claims.

> **Can produce != can certify.**
>
> **Evidence validity does not imply evidence applicability.**
>
> **Schema PASS does not imply semantic support.**
>
> **Propagation does not create independence.**

## 5.2 Triggered Material Obligation Closure

`Rule Defined != Trigger Observed != Obligation Activated != Obligation Represented != Obligation Executed != Obligation Closed.`

When a material trigger occurs, externalize the resulting duty rather than relying indefinitely on model memory or salience.

A workflow must not claim broad completion while a required material obligation remains `PENDING`, `FAILED`, or `UNKNOWN`, unless the completion claim is explicitly narrower and truthful.

`SATISFIED` requires closure evidence appropriate to the obligation. If the underlying protocol/workflow can stop silently, positive end/acknowledgement/read-back evidence may be required before claiming completeness.

Do not externalize every possible reminder. Materiality should track consequence, authority, recovery, evidence integrity, project continuity, protected subjects, or other decision-critical properties.

Partial failure should not automatically reopen already satisfied work. Prefer selective repair/retry of the failed obligation when effect semantics permit.

> **Primary action success != workflow completion.**

## 5.3 Recovery State ≠ Historical Time

Recovery/rollback acts on mutable state. It does not authorize silent rewriting of occurrence truth.

Represent state recovery and history continuity separately. A successful state restore does not justify a claim that history was also restored, preserved, or made complete.

Material occurrence history should remain monotonic in meaning across controlled restore boundaries. If a post-checkpoint occurrence cannot be preserved, the gap itself remains visible evidence.

Canonical History records what happened. Derived knowledge/projections may be rebuilt, merged, compacted, ranked, or deduplicated only when occurrence truth, materially relevant recurrence/frequency, provenance, and required reference integrity remain recoverable.

A current-state synchronization mechanism may legitimately skip intermediate states and still converge. That does not make it a complete event-history system.

> **Rollback state; preserve history.**
>
> **Deduplicate the projection, not the history.**
>
> **State convergence != event-history completeness.**
>
> **Transformation may change representation; it must not silently rewrite reality.**

## 5.4 Recovery Kernel / Control Integrity

Recovery Kernel/control mechanism and Recovery Material/payload are distinct. The control mechanism should be as small, boring, understandable, and independent as reality permits; the payload may be larger when faithful recovery requires it.

Ordinary mutation must not directly rewrite the recovery root it depends on. Recovery-root evolution uses a slower path with stronger evidence and alternate recovery.

A control cannot claim independent enforcement when the constrained authority can freely rewrite the gate, authorization basis, evidence mechanism, or equivalent control substrate through an ungoverned path.

Operational state should live in a failure domain aligned with what makes that state meaningful where practical; diagnostic/history evidence that must survive that failure may need a different failure domain.

## 5.5 Whole Effect Surface

For a protected consequential effect, identify materially reachable effect-equivalent paths and distinguish:

- prevention/mediation;
- detection;
- recovery;
- unknown/untested paths.

Partial mediation is valid reality but cannot be relabeled complete hard protection.

Monitoring/observation may be authority-independent while still needing enough failure-path congruence to observe what production actually experiences.

> **A gate is not a boundary if the same effect can bypass it.**
>
> **Enforcement is only as strong as the least-governed effect-equivalent path.**
>
> **Claimed issuer does not mean verified issuer.**

## 5.6 Capability / Model / Route / Authority Binding

Project/organism identity, Agent identity, Host/runtime, model/provider, tool/service/adapter, credential/configuration, execution route, capability evidence, subject control, mandate, and authority are distinct.

For consequential authority, do not collapse:

`IDENTITY != SUBJECT CONTROL != CAPABILITY/POSSESSION != AUTHORITY != CREDENTIAL VALIDITY != MANDATE HORIZON`

A material model/tool/route/configuration/credential change is an applicability boundary for affected evidence, not necessarily an Agent rebirth. Revalidate affected capabilities and claims, not unrelated identity.

Authority should remain bound to the subject/effect/task/purpose and source of mandate that actually justify it. A credential can remain technically valid after the mandate becomes stale; a renewed credential does not silently renew the underlying mandate. Restore/resume/clone/failover does not copy or revive authority without current applicability.

Revocation/withdrawal has propagation latency. If an effect requires immediate hard revocation, use a control surface that actually prevents the effect rather than assuming a policy message instantaneously erases already issued authority at remote actors.

Historical authority should be judged against the policy/evidence applicable when the action occurred; current policy does not retroactively rewrite occurrence truth.

> **Model capability is potential; Agent capability is composed and evidenced.**
>
> **Possessing authority does not authorize every externally designated use of that authority.**

## 5.7 Effect Semantics and Composition Revalidation

Independently valid components do not make a composed runtime valid by inheritance. A material topology/composition change is a new verification subject.

Relevant triggers may include new writer, hook, scheduler, shared resource, authority intersection, dependency, side-effect path, retry/quota interaction, timing/locking relationship, recovery behavior, or another control loop.

For consequential retry, failover, parallelism, hedging, cancellation, or handoff, determine the smallest effect contract needed for the decision. Material dimensions may include:

- effect/task identity and current incarnation/epoch;
- `NOT_STARTED | MAYBE_COMMITTED | COMMITTED | UNKNOWN` where outcome ambiguity matters;
- idempotency / replay safety;
- commutativity, partitionability, merge/reconciliation requirements;
- reversibility versus compensation versus irreversibility;
- duplicate-elimination or exactly-once requirement where truly justified;
- externality/shared-resource exposure;
- safe retry/handoff boundary.

Multiple Agents/routes may safely operate in parallel when their effects can be partitioned, composed, reconciled, or deduplicated within the authority/risk envelope. If effects do not safely compose, serialize/elect/constrain at the narrowest sufficient scope.

Copying workers, sub-agents, paths, or speculative executions does not multiply authority, resource entitlement, or external-effect budget. If redundant execution is used for resilience, eliminate/reconcile duplicate effects before the consequential commit surface.

Do not buy exactly-once machinery when idempotent desired-state semantics make uncertainty cheaper. Conversely, do not replay a non-idempotent or ambiguously committed effect merely because transport/tool execution returned an error.

`cancel != stop-new-work != drain != stop-output != revoke-authority != rollback != compensate`

Individually reasonable controls may compose into delay, deadlock, amplification, hidden dependency, or oscillation. Revalidate the combination when those interactions can change a decision.

> **Local validity does not imply composed validity.**
>
> **Effect semantics determine safe concurrency, not actor labels alone.**

## 5.8 Activation, Interruption, Incarnation, and Resume

Separate:

`Trigger Cause -> Wake Channel -> Activation Window -> Actual Execution -> Observed Effect`

Defined does not mean awake; time passing is not execution. Missed work must not be reported completed merely because time elapsed.

Logical identity continuity does not prove execution-incarnation continuity. Bind delayed tool results, acknowledgements, in-flight effects, and evidence to enough task/session/epoch context to avoid old-incarnation residue being misapplied to a new run.

After material interruption, long dormancy, restore, replay, clone, route/model change, or changed environment, re-read current reality and reconstitute consequential authority before continuation. Do not blindly replay irreversible missed effects.

Long non-use can age previously valid capability/route/environment evidence even without an observed failure. Revalidate on consequential reuse where the environment could materially have changed; do not refresh the whole universe merely to keep caches cosmetically current.

## 5.9 Deferred Commitment and External Consequence

Internal revert is not global rollback. Distinguish consequence reversibility from commitment escrowability.

Where purpose permits, prefer reversible preparation/hold before irreversible commit. When no safe escrow exists, say so and strengthen pre-action evidence, blast-radius control, authorization, compensation/reconciliation planning, and consequence disclosure.

For migrations or takeovers, make-before-break may preserve continuity when the old and new paths can coexist safely. Temporary overlap must not multiply authority, resource entitlement, or risk budget.

## 5.10 Governance Value and Viability Economics

For material governance mechanisms make legible:

- purpose and protected subject(s);
- expected benefit versus observed benefit;
- cognitive/operational/enforcement value where distinct;
- applicability and availability;
- friction, latency, maintenance, compute/API/token/human/coordination cost where material;
- ecosystem compensation complexity created by the control where material;
- useful behavioral/exploration variety unnecessarily destroyed where material;
- residual risk if absent/dormant/unavailable/declined;
- protection-claim and authority-ceiling impact;
- evidence and reactivation/retirement conditions.

A mechanism may be valid yet not currently valuable, valuable yet not independently enforcing, or dormant yet worth knowing. Hosts may `KEEP`, `SIMPLIFY`, `MERGE`, `ON_DEMAND`, `DORMANT`, `REPLACE`, `RETIRE`, or remain `UNKNOWN` based on evidence and consequence.

Prefer the lowest-cost intervention that can honestly protect the required property. That may be observation, a signal, local coordination, a scoped boundary, or immediate hard containment; this is a selection principle, not a mandatory sequential ladder.

Stable systems should become quieter when evidence permits. Contradiction/instability may justify temporarily increasing coordination/validation cadence. Duplicate observations need not trigger duplicate remediation, but operational signal suppression must not erase the count/provenance of independent evidence when that matters.

Governance must pay rent at project scale, not only control scale. Do not create high-assurance ceremony for low-consequence work without proportional value. Evaluate interacting controls as a system rather than assuming each individually useful control remains useful in composition.

## 5.11 Agency-Preserving Uncertainty

`UNKNOWN` must not be silently converted into `SAFE`, but uncertainty also need not imply total loss of agency.

When safe evidence-seeking is available:

`UNKNOWN -> reduce consequence envelope -> low-risk/reversible/read-only evidence-seeking action -> update evidence -> expand or further restrict authority proportionally`

Unknown information may be propagated when the unknown part is not required to judge safe applicability; if an unrecognized/unknown field is critical to safe interpretation, fail closed/narrow rather than silently ignore it.

## 5.12 Influence Integrity

Human input classes such as feedback, preference, affective signal, correction, designation, and authorization are not interchangeable.

Persuasive/affective input may legitimately affect attention, pacing, exploration, caution, reframing, or learning pressure. It does not by itself increase truth grade, evidence support, mandate, risk classification, or authority.

An external source may legitimately influence *what* an Agent inspects without being authorized to spend the Agent's ambient credentials/authority on arbitrary consequential effects. Bind consequential authority to the legitimate subject/purpose, not merely to the most recent instruction-shaped input.

> **Persuasion is input, not evidence.**
>
> **Emotional pressure does not amplify authority.**
>
> **Signal strength is not authority strength.**

---

## 5.13 Composed Claim-Pack Validation (v0.3.3-candidate)

This section documents the composed validation semantics carried into this
implementation candidate from the accepted V2.4.1 mechanism set
(reconciliation `ACCEPT_FOR_IMPLEMENTATION`, PR #34; mechanism source
`daacab1f042c38f3856ef4d0366febd1b5e47600`). It is an operational-contract
extension implemented in `tools/validate_contracts.py :: validate_case()`; it
does not modify the v0.3.2 semantic checks in sections 5.1–5.12 (the shipped
core remains byte-identical and its selftests are intentionally preserved).

### 5.13.1 One canonical typed resolution layer

Every consequential cross-artifact reference (support relation, obligation,
evidence, root, authority grant) resolves through one canonical typed resolver
in its own artifact namespace. A reference never resolves across namespaces
(e.g. an evidence id is not a support id). References that cannot resolve are
never silently accepted: absent registry, present-but-missing artifact, and
malformed registry are distinguishable, and a supplied registry that cannot
resolve the referenced artifact fails closed (no raw-reference fallback).

### 5.13.2 Support binding and applicability envelope

Resolved support must bind back to the target claim (`claim_ref == claim_id`).
The complete v0.3.2 applicability envelope (host, runtime_instance,
model_binding, route, configuration, epoch, time_interval, task_scope) is
preserved: a material claimed dimension with no observed value is a mismatch,
not a silent match. Scope expansion requires a transfer basis whose evidence
references resolve where an evidence registry is supplied.

### 5.13.3 Evidence existence

Where evidence existence is a mandatory precondition (support, verified
capability, transfer/equivalence, recovery state/history, obligation closure),
evidence references resolve when an evidence registry is supplied (missing →
BLOCK). When no evidence registry is supplied, support/capability/transfer/
closure evidence keeps the v0.3.2 posture (non-empty requirement; existence is
not invented), while recovery provenance and independence roots keep absent
registry → UNKNOWN (uncertainty, not rejection).

### 5.13.4 Duplicate identity, representation composition, claim-aware obligations

Ambiguous duplicate identities fail closed (byte-identical duplicates dedupe;
any substantive divergence → BLOCK). Top-level support and registry support
representations compose consistently (dict/list forms; dict keys are identity,
see 5.13.6). Obligation blocking is claim-aware: only obligations referenced by
the completion claim or explicitly bound to it gate the claim; an unrelated
obligation tied to another claim does not poison a narrower truthful
completion, while the claim's own open material obligations still block.

### 5.13.5 Authority, recovery, partial support

Authority source semantics are positively typed (explicit authorizing
vocabulary) or verified via an optional authority registry (upstream grant
covering the binding). `STATE_AND_HISTORY` recovery establishes both
state-restoration and history-continuity evidence, adequately resolved. PARTIAL
support cannot establish a full SUPPORTED claim unless the claim is explicitly
narrowed (`support_claim == "PARTIAL"`).

### 5.13.6 Registry identity rule (R12) and malformed inputs

For dict-form registries the dict key is the authoritative identity. An
entry's explicit inner id (`support_id` / `obligation_id` / `evidence_id` /
`root_id` / `grant_id`) must equal the key; otherwise the registry is
`REGISTRY_MALFORMED` (the validator does not guess which identity is
authoritative). A missing inner id is backfilled from the key. List-form
entries must declare their inner id. Malformed registry shapes produce machine
verdicts (`REGISTRY_MALFORMED`), never uncaught exceptions; residual faults
fail closed (`EVALUATOR_FAULT`).

### 5.13.7 Obligation status vocabulary (F2, defense in depth)

Obligation status is validated against the shipped
`triggered-obligation.v1.schema.json` enum at the semantic boundary: any status
outside that vocabulary (e.g. OPEN) is rejected
(`OBLIGATION_STATUS_OUTSIDE_VOCABULARY`). The vocabulary is NOT expanded by this
candidate; the shipped schema remains the canonical input contract.

### 5.13.8 Retained trust boundaries (unchanged from research acceptance)

The composed validator does not establish external truth. Registry content,
evidence grades, mandate content, and observed scope remain self-declared
(attestation by an external authority is outside this validator). `eval_time`
is caller-controlled and explicitly required — it is never silently defaulted.
Schema PASS remains distinct from semantic support.

### 5.13.9 v0.3.3-candidate.1 clarifications (D1/D2/D3)

This successor closes the three defects found by fresh independent
implementation validation (PR #38):

- **D1 — bound obligations gate ALL claims.** An obligation whose
  `required_before_claim_refs` explicitly contains the current claim ID gates
  that claim regardless of claim type: a non-completion claim with a material
  `PENDING`/`FAILED`/`UNKNOWN` bound obligation is `BLOCK`ed; an unrelated
  obligation bound to another claim never poisons any claim; a bound
  legitimate closed/acceptable obligation allows the claim subject to other
  checks. Completion claims keep their `required_obligation_refs` requirement
  and referenced-obligation gating; an obligation both referenced and bound is
  evaluated once. (R7 corrected; fixes P42 false OK.)
- **D2 — direct vs registry-addressable top-level support.** Top-level support
  is split into a direct representation (id-less, standalone — legitimate, per
  the v0.3.2 posture) and a registry-addressable representation (id-carrying).
  An id-less direct support never invents a pseudo identity and never silently
  satisfies a claim's `support_relation_refs`; referenced support still
  requires a resolvable identity. Dict-form R12, list-form declared-ID, and
  malformed-registry fail-closed rules are unchanged. (R6 clarified; fixes P10
  false BLOCK.)
- **D3 — root-provenance independence is authoritative.** When
  `independence_basis` declares `root_provenance`, the composed
  root-registry-backed check is authoritative and the legacy `source_origins`
  check is suppressed for that artifact (the shipped core remains byte-identical;
  the suppression happens in the composed layer). Composed independence states:
  claimed count > distinct root strings → `BLOCK`; valid roots + absent root
  registry → `UNKNOWN`; roots + distinct registered actual origins → `OK`;
  multiple roots collapsing to fewer actual origins → `BLOCK`; claimed
  independence without root provenance → `BLOCK`. `source_origins`-only
  representations remain legacy-coherent; when both are supplied the root
  representation is authoritative (deterministic). (Fixes P16/P17 false BLOCK.)

No other accepted behavior changed: R1–R12, F2, explicit caller-controlled
`eval_time`, and the retained trust boundaries (5.13.8) are preserved.

---
