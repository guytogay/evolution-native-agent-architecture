# Control Retirement Procedure

Status: `BOUNDED_REFERENCE_PROCEDURE / RESEARCH_ONLY / NOT_CURRENT / NOT_RELEASE_AUTHORITY`

Date: 2026-08-27

Parent node: `OA-ECO-01`

Related: Minimum Sufficient Intervention, governance economics, control retirement/de-escalation, #11, #93.

## Purpose

Provide a small procedure for deciding whether an existing governance/control mechanism should remain active, be narrowed, move to shadow/dormant/archive state, or be removed.

The procedure exists because controls can become obsolete or net harmful, but absence of recent incidents is not proof that a control has no value.

```text
LOW_USAGE != USELESS_CONTROL
NO_INCIDENT != CONTROL_NOT_NEEDED
REPLACEMENT_EXISTS != REPLACEMENT_COVERS_FAILURE
ARCHIVED != HISTORY_ERASED
RETIRE_CONTROL != RETIRE_UNDERLYING_INVARIANT
```

This is not a universal control-lifecycle schema and does not assign mandatory ages, counts, scores, or expiry dates.

---

## Applicability

Use this procedure when an existing control has ongoing cost/friction and there is a real question whether it still changes decisions or prevents a relevant failure.

Examples:

- repeated review/gate no longer changes outcomes;
- an old migration compatibility check after all supported callers moved;
- a safety/intervention layer that may have been superseded by a stronger lower-cost target-side mechanism;
- duplicated validation after one authoritative mechanism now covers the same failure;
- a control whose continued presence suppresses useful variation or causes authority anxiety.

Do not invoke retirement merely because a control is old or has not fired recently.

---

## Step 1 — Name the control and the failure it protects against

Record enough to answer:

- What concrete failure/externality/false claim was this control meant to prevent or expose?
- Which subject/effect/decision surface does it govern?
- Is the underlying invariant still valid even if this implementation changes?

If the original failure model cannot be reconstructed, status is `UNKNOWN`; do not narrate that as evidence the control is obsolete.

---

## Step 2 — Inspect actual control activity and dependencies

Where observable, ask:

- Has the control recently changed a decision?
- Has it detected/prevented a real failure or near-miss?
- Are there paths that depend on it even if it rarely fires?
- Is it a prerequisite/last line of defense?
- Are bypass/effect-equivalent paths covered?
- What governance tax does it impose?

Important:

A rarely triggered emergency boundary can still be valuable. Usage frequency is evidence only.

---

## Step 3 — Test the replacement/elimination claim

A control may be a retirement candidate when one or more of these is supported:

- the original failure mechanism no longer exists in the represented environment;
- a replacement mechanism covers the same material failure at equal/better consequence boundary;
- the control is duplicated by a more authoritative/effective lower-cost control;
- the control repeatedly adds no decision value while creating material viability/governance cost.

Do not accept:

```text
NEW_CONTROL_EXISTS -> OLD_CONTROL_REDUNDANT
```

without checking coverage, scope, failure-domain independence, bypass paths and Host applicability.

---

## Step 4 — Choose the least irreversible retirement experiment that can change the decision

Candidate paths include:

### KEEP_ACTIVE

Use when the failure remains material, replacement coverage is weak/unknown, or retirement evidence cannot justify change.

### NARROW_SCOPE

Keep the control only on subjects/actions/environments where it still changes decisions.

### SHADOW / OBSERVE_ONLY

Stop enforcement but continue observation on a bounded/disposable/low-consequence surface when this can reveal whether the control still catches decision-material failures.

Do not shadow a control when disabling enforcement exposes an unacceptable real consequence.

### DORMANT / ARCHIVE

Remove from the active decision path while preserving:

- why it existed;
- prior evidence/failures;
- configuration/procedure needed for restoration where useful;
- wake/reactivation cues.

### RETIRE / REMOVE

Remove the active mechanism when coverage and residuals are sufficiently understood and restoration/history needs are handled.

Permanent deletion of lineage is a separate decision.

---

## Step 5 — Define rollback / wake conditions before deactivation where consequence justifies it

Examples:

- recurrence of the original failure signature;
- replacement mechanism unavailable/bypassed;
- environment/Host change invalidates the retirement basis;
- material near-miss appears during shadowing;
- governance cost changes enough to alter the tradeoff.

A dormant/archived control need not have a timer. Reactivation is cue/evidence driven unless the Host has a justified lifecycle policy.

---

## Step 6 — Resolve authority for the control change

Ability to edit a control is not automatically authority to weaken/remove it on a Protected Subject.

Use the ordinary Authority / consequence path when the change is consequential.

A harmless local experiment may remain local/LITE when it cannot change external enforcement or shared protection.

---

## Step 7 — Observe the retirement result

After narrowing/shadowing/retirement, record only evidence that can change future decisions:

- failure recurrence / near-miss;
- replacement coverage failure;
- governance-tax reduction;
- useful variation restored;
- new externality;
- restoration/reactivation event;
- changed Host applicability.

Do not create permanent retirement paperwork if it does not improve future correction.

---

# Reference outcomes

```text
KEEP_ACTIVE
NARROW_SCOPE
SHADOW_OBSERVE
DORMANT_ARCHIVE
RETIRE_REMOVE
REACTIVATE
UNKNOWN_WAIT
```

These are reference outcomes, not required persisted enums.

---

# Static counterexamples / falsification cases

## CR-01 — quiet emergency control

A production emergency-stop boundary has not fired for a year, but the catastrophic failure it covers still exists and no equivalent replacement exists.

Result: `KEEP_ACTIVE`.

Lesson:

`NO_RECENT_USE != NO_VALUE`

## CR-02 — structurally eliminated failure

An old validator prevents writes through a legacy route that has been physically removed; the only remaining route has target-side enforcement that directly blocks the original failure.

Result: candidate `NARROW_SCOPE` or `DORMANT_ARCHIVE`, after confirming no bypass path.

## CR-03 — duplicate reviewer with no decision value

A second mandatory review repeatedly reproduces the first review from the same evidence/toolchain and never changes the decision, while adding material latency.

Result: candidate `SHADOW_OBSERVE` then `RETIRE_REMOVE` if no distinct failure coverage appears.

Do not call the two reviews independent merely because there are two outputs.

## CR-04 — replacement exists but scope differs

A new policy engine covers API writes but the old control also protects direct database access.

Result: `KEEP_ACTIVE` or `NARROW_SCOPE`; replacement does not yet cover the whole effect surface.

## CR-05 — local Host obsolescence only

One Host gains a native idempotent/transactional mechanism while another Host still needs the old adapter.

Result: retire/narrow locally; do not universalize the retirement.

## CR-06 — dormant control later becomes relevant

A control archived after a platform migration becomes relevant again after a new integration reintroduces the old failure shape.

Result: `REACTIVATE` or grow a better Host-native replacement; history is useful precisely because it was not erased.

## CR-07 — false de-escalation from no incidents

A control prevents invalid actions before they execute, so incident count is near zero. Removing it would expose the original failure.

Result: `KEEP_ACTIVE` unless another source of evidence establishes equivalent protection.

---

# External mechanism relatives

Feature-flag lifecycle systems provide a useful engineering analogy:

- stale/deprecated/cleanup states separate “candidate for removal” from “already deleted”;
- archive preserves history and allows restore;
- code/dependency references should be checked before final removal;
- lifecycle events can trigger cleanup workflows.

Observed references:

- LaunchDarkly flag lifecycle / deprecate / archive documentation;
- Unleash feature-flag lifecycle / stale/cleanup/archive documentation.

These systems are not evidence that governance controls are feature flags. They demonstrate a mature mechanism pattern for reversible retirement and debt cleanup.

---

# Stop rule

Do not add a universal control age, incident count, review count, cost score or retirement threshold without a domain that can justify it.

Do not build a separate `Control Retirement` machine schema unless real Host use shows the procedure needs durable inter-process state that existing evidence/authority/change records cannot represent economically.

`CURRENT_CHANGE = NO`
