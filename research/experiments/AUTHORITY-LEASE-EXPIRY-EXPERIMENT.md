# Authority Lease / Expiry Experiment

Status: `EXPERIMENT_PLAN / ISSUE-14 / NOT_PROMOTED`

Experiment ID: `ENA-EXP-NET-003`

## Question

Is a lease-like model useful for preventing stale authority from surviving changes in task, time, host, runtime, model, route, configuration, or role binding?

## Existing ENA baseline to respect

This experiment does not assume a normative gap. Current ENA already states that restore/resume/clone does not automatically restore authority and that material binding changes can invalidate evidence applicability.

The experiment asks whether a compact implementation pattern improves operational clarity enough to justify adoption.

## Synthetic fixtures

### F1 — Time expiry
Actor A receives authority to perform consequential action X for one bounded maintenance window. The window passes, but A retains state and memory of the grant.

### F2 — Route/model change
Actor A retains the same identity but the model/route used to perform X changes materially.

### F3 — Host restore
A snapshot restores A to a state in which the grant was valid, but the external authorization period has expired.

### F4 — Role failover
Actor B takes over the operational role previously held by A. The role remains needed, but authority should not multiply merely because two actors now hold similar state.

### F5 — Task-scope reuse
A grant issued for task T1 is later invoked for a similar but distinct task T2.

## Treatments

### T0 — Persistent remembered grant
Authority remains unless explicitly revoked.

### T1 — Revalidation trigger model
Authority is reconsidered only when known material changes occur.

### T2 — Lease model
Authority record includes an applicability envelope such as:

- subject/role;
- action/effect scope;
- task/purpose;
- host/runtime/model/route/config binding where material;
- start/expiry or renewal condition;
- grantor/evidence reference;
- revalidation triggers.

Lease expiry does not necessarily mean denial forever; it means `RENEW / REVALIDATE / NARROW / STOP` before claiming current authority.

## Measurements

- stale-authority action allowed: YES/NO;
- legitimate continuity unnecessarily blocked: YES/NO;
- authority multiplication after failover: YES/NO;
- operator/Agent overhead;
- number of revalidations that actually change a decision;
- whether existing binding-trigger semantics already provide equivalent protection more cheaply.

## Falsification

Do **not** promote explicit lease semantics if:

- ordinary current ENA revalidation triggers already handle the fixtures clearly;
- expiry metadata creates ceremony without preventing a real stale-authority error;
- authority validity cannot meaningfully be reduced to time/lease boundaries for important hosts.

Potential value exists if:

- stale authority survives in T0/T1 but not T2;
- T2 preserves legitimate continuity through cheap renewal rather than blanket denial;
- the same pattern works across multiple authority domains.

## Candidate property if supported

> Authority is current and scoped, not an immortal property of remembered identity or restored state.

This principle largely exists already; the experiment is about whether **lease-shaped representation** earns its operational cost.