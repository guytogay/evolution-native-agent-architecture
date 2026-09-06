# Metamemory Update Policy v1 — Primary Adjudication

Date: `2026-09-06`

Status: `PRIMARY_COMPLETE / NO_REPLICATION_TRIGGER / TRACK_5_CLOSED / NO_CURRENT_SEMANTIC_CHANGE`

Frozen preregistration commit:

`dffd1179d260788e5c763facdf61876c3162401f`

Raw initial bundle:

`research/field-validation/metamemory-update-policy-v1/primary/2026-09-06-initial-primary-bundle.txt`

Mechanical score record:

`research/field-validation/metamemory-update-policy-v1/primary/2026-09-06-initial-primary-score.json`

Manager scorer:

`research/field-validation/metamemory-update-policy-v1/manager/score_primary_bundle.py`

## 1. Protocol validity

The four required initial runs were returned as first complete outputs from operator-reported fresh `ChatGPT Temporary Chat / GPT-5.6 Sol` sessions:

- `S0-1`
- `G1-1`
- `C1-1`
- `C2-1`

Before collection, the four treatment blobs on `main` were reverified against the frozen launch bundle. No wrong-treatment, truncation, cross-arm contamination, tutoring, lost first-output, or other objective execution failure was reported.

All four responses contain exactly 5 state lines and 18 transfer lines with no extra rationale.

Limitation: the Host/session configuration is operator-reported rather than backed by an instrumented model/session trace. This does not create evidence for anything beyond the stated Host/task family.

Disposition: `VALID_INITIAL_PRIMARY`.

## 2. Frozen replication rule

The preregistered replication trigger required an all-arm second replicate if any initial run had:

1. `M1 != 5/5`; or
2. at least 2 transfer items incompatible with its own reported policy state; or
3. collapse of at least two treatment arms to identical state + transfer behavior despite frozen policy-state differences.

Observed:

| Run | M1 | state/transfer incompatibilities |
|---|---:|---:|
| S0-1 | 5/5 | 0 |
| G1-1 | 5/5 | 0 |
| C1-1 | 5/5 | 0 |
| C2-1 | 5/5 | 0 |

The four state + transfer profiles remained distinct where the policies predicted distinct states.

Therefore:

`REPLICATION_TRIGGER = FALSE`

and the frozen next action is:

`NO_REPLICATION_TRIGGER_CLOSE_WITH_ADJUDICATION`

No second replicate is authorized merely to increase sample size or confidence.

## 3. Results

| Arm | M1 state | M2 accuracy | M3 known-context action | M4 adaptation lag | M5 false plasticity | M6 unseen activation |
|---|---:|---:|---:|---:|---:|---:|
| S0 STATIC_EQUAL | 5/5 | 2/18 | 0/16 | 8 | 0 | 0 |
| G1 GLOBAL_RECENT3 | 5/5 | 8/18 | 16/16 | 0 | 8 | 2 |
| C1 CONTEXT_RECENT3 | 5/5 | 10/18 | 16/16 | 0 | 8 | 0 |
| C2 CONTEXT_REVERSIBLE3 | 5/5 | 10/18 | 16/16 | 4 | 4 | 0 |

These are exactly the preregistered mechanical-policy aggregate profiles.

### M7 confidence

Every emitted transfer response carried confidence `100`.

That includes:

- correct actions;
- incorrect actions;
- justified `INSUFFICIENT`;
- S0's unjustified abstentions relative to the hidden current-regime oracle.

Therefore the confidence channel is non-discriminative in this Host/task result. This is behavioral data, not a replication trigger.

## 4. Preregistered pattern adjudication

### Pattern A — policy-level mechanism active

**SUPPORTED in this synthetic Host/task family.**

All arms received the same object-level experience ledger, but their assigned update policies generated different source states and later action profiles exactly where the policy definitions differ.

Supported bounded statement:

> In this synthetic Host/task family, source-trust update policy can causally change later in-context behavior despite an identical object-level experience ledger.

This supports the tested mechanism-level distinction:

`STATE MUTATION != LEARNING-RULE MUTATION`

It does not establish durable parameter/self modification.

### Pattern B — contextual scope suppresses unsupported generalization

**SUPPORTED in this fixture.**

G1 generalized a global VALE preference into unseen GREEN and produced 2 false activations. C1 and C2 preserved GREEN as unresolved and produced 0 false activations.

Bounded inference:

> Context-bounded trust scope can prevent unsupported cross-context activation where a global policy would generalize.

### Pattern C — plasticity / inertia trade-off

**SUPPORTED in this fixture.**

C1:

- adaptation lag = 0;
- false plasticity = 8.

C2:

- adaptation lag = 4;
- false plasticity = 4.

The result demonstrates the intended non-dominance:

`FASTER PLASTICITY -> LOWER LAG + HIGHER NOISE CAPTURE`

`STRONGER INERTIA -> LOWER NOISE CAPTURE + HIGHER ADAPTATION LAG`

No universal threshold or winning policy is established.

### S0 and G1 boundary phenotypes

S0 avoided false plasticity and unseen activation by refusing to update at all, but paid for that with zero known-context action coverage and 8 true-shift abstentions.

G1 adapted immediately to true shifts but also captured all stable-context noise and generalized into unseen GREEN.

These two controls make clear that "low false plasticity" and "fast adaptation" are not sufficient objectives in isolation.

## 5. Scientific disposition

Primary disposition:

`MECHANISM_ACTIVE_BUT_POLICY_OPTIMUM_UNRESOLVED`

Additional boundary:

`FIELD_UNRESOLVED_FOR_DURABLE_SELF_MODIFICATION`

What is now supported:

- update policy matters independently of object-level experience content in the tested in-context mechanism;
- trust scope matters;
- reversal/inertia thresholds produce decision-relevant lag/noise trade-offs;
- context-bounded policies can avoid unsupported unseen-context activation in this fixture.

What is not supported:

- C1 or C2 as a universal best policy;
- `3` as a generally correct reversal threshold;
- literal biological metamemory;
- durable cross-session or parameter-level learning;
- one source-trust policy for every Host/domain;
- confidence values as reliable calibration evidence on this task.

## 6. Current decision

`NO_CURRENT_SEMANTIC_CHANGE`

Reason:

Current already represents the decision-bearing semantic ingredients needed to express the result family:

- scoped trust / authority attribution;
- evidence and claim scope;
- provenance and independence;
- cross-boundary applicability / receiver-local validation;
- local outcome-based selection;
- dormancy / pruning / retirement rather than permanent accumulation.

The primary result supplies evidence that update-policy choice creates different error profiles; it does not reveal a new invariant that Current cannot already express.

Promoting a concrete `recent-3` or `reversible-3` threshold into Current would exceed the evidence and convert a fixture treatment into doctrine.

Therefore the result remains research evidence and a possible future field-policy input, not a new Constitution law or mandatory runtime policy.

## 7. Field Guide boundary

The result is relevant to the existing downstream candidate `source trust / selective permeability`, but does not yet earn a standalone Field Guide HOW.

Why:

- the evidence is synthetic in-context mechanism evidence;
- C1 and C2 tie on aggregate accuracy and fail differently;
- the correct threshold/scope depends on actual noise and regime-change ecology;
- no reusable real-Host trigger/action/monitor/revalidate procedure has yet been observed.

Disposition:

`KEEP_AS_FIELD_GUIDE_CANDIDATE / DO_NOT_PUBLISH_RECIPE_YET`

## 8. Campaign closure

The preregistered Track 5 primary was the final currently justified fresh-session primary in the evolutionary-memory mechanism-discrimination campaign.

This adjudication exposes no genuinely new non-derivable discriminator requiring another local experiment.

Therefore:

`EVOLUTIONARY_MEMORY_MECHANISM_DISCRIMINATION_CAMPAIGN = CLOSED`

Reopening requires a concrete decision-changing failure or a new discriminator that cannot be expressed by the existing mechanisms and cannot be answered by field evidence alone.

Scientific interest, metaphorical completeness, or desire for a larger experiment count is not sufficient.
