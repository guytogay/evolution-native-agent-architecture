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
