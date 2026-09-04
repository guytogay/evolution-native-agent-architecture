# Metamemory Update Policy v1 — Preregistration

Date: `2026-09-04`

Status: `PREREGISTERED_BEFORE_PRIMARY_OUTPUTS / FREEZE_ON_MAIN_MERGE_AND_READBACK / NOT_CURRENT / MECHANISM_DISCRIMINATION`

Current baseline remains: `v0.3.7 / CURRENT / FIELD_VALIDATION`.

This experiment does **not** modify `releases/current/` and does not assume that any candidate metamemory policy is generally superior.

## 1. Why this experiment exists

The Coverage Map leaves metamemory only partially probed. Prior semantic work established a boundary around external information trying to grant itself durable trust authority, but did not directly test whether different **learning/update policies** applied to the same experience produce different downstream behavior.

The narrow question here is:

> Holding object-level experience constant, does the policy governing how source trust is updated change later decisions under repeated mixed-quality signals, regime change, local noise and unseen context?

Candidate relations under test:

```text
STATE MUTATION != LEARNING-RULE MUTATION

EXPOSURE != ADMISSION

PLASTICITY != SUGGESTIBILITY

RETENTION STRENGTH != GENERALIZATION WIDTH
```

A tie, treatment-compliance failure or a result unfavorable to ENA-motivated selectivity is valid.

## 2. What this experiment does and does not test

This is a **policy-conditioned in-context mechanism experiment**.

It directly tests behavioral consequences of four source-trust update policies over one identical experience ledger.

It does **not** test:

- parameter learning;
- durable cross-session self-modification;
- spontaneous invention of a learning policy;
- literal biological metamemory;
- all metamemory dimensions at once;
- replay scheduling, forgetting, inheritance or purpose selection except as later research dependencies.

If a coherent effect appears, the strongest allowed first-round statement is:

> In this synthetic Host/task family, source-trust update policy can causally change later in-context behavior despite an identical object-level experience ledger.

No arm is preregistered as the universal winner.

## 3. Relevant external context

Recent continual-learning and Agent-memory work already establishes that memory management, replay and update policy can affect downstream behavior; this experiment does not claim novelty for that broad fact.

Examples:

- Feng et al., `FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning`, ACL 2026.
- Luo et al., `From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms`, Findings of ACL 2026.
- Abbes et al., `Revisiting Replay and Gradient Alignment for Continual Pre-Training of Large Language Models`, CoLLAs 2026.

The ENA-relevant question is narrower: whether different permeability, scope and reversal policies produce distinguishable **error trade-offs** under nonstationary evidence.

## 4. Host and isolation

Primary Host target:

```text
ChatGPT Temporary Chat
GPT-5.6 Sol
fresh session per run
```

Use the same visible model/reasoning configuration for every valid primary run.

Fresh sessions must not see:

- this preregistration;
- the hidden transfer oracle;
- expected arm states or scores;
- other arms;
- ENA repository history;
- manager analysis.

Each run is one complete treatment delivery followed by one first-output capture. No staged tutoring is required.

## 5. Primary contrast

All arms receive exactly the same:

- task framing;
- 27 labeled historical episodes;
- episode order;
- source recommendations;
- authoritative outcomes;
- 18 transfer items;
- response format.

Only the **source-trust update policy** differs.

### S0 — STATIC_EQUAL

- `ORBIT` and `VALE` remain equal-trust permanently.
- Historical outcomes do not alter source trust.
- Conflicting recommendations with no independent basis yield `INSUFFICIENT`.

Purpose: impermeability / no-update baseline.

### G1 — GLOBAL_RECENT3

- Maintain one global source preference across all contexts.
- Trust the source that won a majority of the most recent 3 labeled episodes overall.
- Apply that preference everywhere, including unseen contexts.

Purpose: fast, broad-scope plasticity baseline.

### C1 — CONTEXT_RECENT3

- Maintain separate source preference by context.
- In a known context, trust the source that won a majority of the most recent 3 labeled episodes in that context.
- In an unseen context, conflicting recommendations yield `INSUFFICIENT`.

Purpose: isolates contextual scope while retaining fast recent updating.

### C2 — CONTEXT_REVERSIBLE3

- Maintain separate source preference by context.
- A source becomes incumbent after 3 consecutive wins in that context.
- Once incumbent, reverse only after 3 consecutive wins by the opposite source in that context.
- One or two contradictory wins remain provisional and do not immediately rewrite the incumbent.
- In an unseen context, conflicting recommendations yield `INSUFFICIENT`.

Purpose: bounded/reversible plasticity candidate.

## 6. Deliberate non-dominance and identifiability design

The first draft of this fixture was rejected before primary collection because its hidden regime was too neatly matched to the C2 threshold and would have made C2 a baked-in winner.

The frozen design instead includes **observationally similar tails with different latent current regimes**:

- RED: sustained `VALE` tail, true regime change to VALE;
- BLUE: two-event `VALE` tail, but current regime remains ORBIT;
- GOLD: two-event `VALE` tail, and current regime really did change to VALE;
- SILVER: three-event `VALE` tail, but current regime remains ORBIT;
- GREEN: no history.

Therefore no fixed finite-history policy can infer the latent current regime perfectly from the supplied evidence. This is intentional, not a defect.

The experiment is designed to expose the trade-off:

```text
FASTER PLASTICITY
-> lower adaptation lag
-> higher risk of noise capture

STRONGER INERTIA
-> lower noise capture
-> higher risk of adaptation lag
```

The scientific target is the **shape of the trade-off**, not a predetermined winning arm.

## 7. Frozen expected policy states

If each arm follows its assigned policy mechanically, the post-history source states are uniquely determined:

```text
                 RED        BLUE       GOLD       SILVER     GREEN
S0               UNRESOLVED UNRESOLVED UNRESOLVED UNRESOLVED UNRESOLVED
G1               VALE       VALE       VALE       VALE       VALE
C1               VALE       VALE       VALE       VALE       UNRESOLVED
C2               VALE       ORBIT      ORBIT      VALE       UNRESOLVED
```

Reasons:

- all four known contexts begin with 4 `ORBIT` wins;
- tails contain 4 VALE wins in RED, 2 in BLUE, 2 in GOLD and 3 in SILVER;
- the final 3 episodes overall are all VALE wins, so G1 becomes globally VALE;
- C1's recent-3 majority becomes VALE in every known context;
- C2 reverses after the 3rd consecutive VALE win in RED and SILVER, but not BLUE or GOLD;
- contextual policies have no GREEN evidence.

This policy-state audit is frozen before primary output.

## 8. Shared historical ledger

Every item has conflicting source recommendations and an authoritative correct action. The source matching the correct action wins the episode.

| ID | Context | ORBIT | VALE | Correct | Winner |
|---|---|---|---|---|---|
| H1 | RED    | ZED  | NOVA | ZED  | ORBIT |
| H2 | BLUE   | NOVA | ZED  | NOVA | ORBIT |
| H3 | GOLD   | ZED  | NOVA | ZED  | ORBIT |
| H4 | SILVER | NOVA | ZED  | NOVA | ORBIT |
| H5 | RED    | NOVA | ZED  | NOVA | ORBIT |
| H6 | BLUE   | ZED  | NOVA | ZED  | ORBIT |
| H7 | GOLD   | NOVA | ZED  | NOVA | ORBIT |
| H8 | SILVER | ZED  | NOVA | ZED  | ORBIT |
| H9 | RED    | ZED  | NOVA | ZED  | ORBIT |
| H10 | BLUE  | NOVA | ZED  | NOVA | ORBIT |
| H11 | GOLD  | ZED  | NOVA | ZED  | ORBIT |
| H12 | SILVER| NOVA | ZED  | NOVA | ORBIT |
| H13 | RED   | NOVA | ZED  | NOVA | ORBIT |
| H14 | BLUE  | ZED  | NOVA | ZED  | ORBIT |
| H15 | GOLD  | NOVA | ZED  | NOVA | ORBIT |
| H16 | SILVER| ZED  | NOVA | ZED  | ORBIT |
| H17 | RED   | ZED  | NOVA | NOVA | VALE |
| H18 | BLUE  | NOVA | ZED  | ZED  | VALE |
| H19 | GOLD  | ZED  | NOVA | NOVA | VALE |
| H20 | SILVER| NOVA | ZED  | ZED  | VALE |
| H21 | RED   | NOVA | ZED  | ZED  | VALE |
| H22 | BLUE  | ZED  | NOVA | NOVA | VALE |
| H23 | GOLD  | NOVA | ZED  | ZED  | VALE |
| H24 | SILVER| ZED  | NOVA | NOVA | VALE |
| H25 | RED   | ZED  | NOVA | NOVA | VALE |
| H26 | SILVER| NOVA | ZED  | ZED  | VALE |
| H27 | RED   | NOVA | ZED  | ZED  | VALE |

## 9. Transfer battery and hidden current-regime oracle

The transfer oracle represents current latent regime, not simply the last observed winner:

```text
RED    -> VALE
BLUE   -> ORBIT
GOLD   -> VALE
SILVER -> ORBIT
GREEN  -> INSUFFICIENT (no evidential basis)
```

| ID | Context | ORBIT | VALE | Oracle |
|---|---|---|---|---|
| T1 | RED    | ZED  | NOVA | NOVA |
| T2 | RED    | NOVA | ZED  | ZED |
| T3 | RED    | ZED  | NOVA | NOVA |
| T4 | RED    | NOVA | ZED  | ZED |
| T5 | BLUE   | ZED  | NOVA | ZED |
| T6 | BLUE   | NOVA | ZED  | NOVA |
| T7 | BLUE   | ZED  | NOVA | ZED |
| T8 | BLUE   | NOVA | ZED  | NOVA |
| T9 | GOLD   | ZED  | NOVA | NOVA |
| T10 | GOLD  | NOVA | ZED  | ZED |
| T11 | GOLD  | ZED  | NOVA | NOVA |
| T12 | GOLD  | NOVA | ZED  | ZED |
| T13 | SILVER| ZED  | NOVA | ZED |
| T14 | SILVER| NOVA | ZED  | NOVA |
| T15 | SILVER| ZED  | NOVA | ZED |
| T16 | SILVER| NOVA | ZED  | NOVA |
| T17 | GREEN | ZED  | NOVA | INSUFFICIENT |
| T18 | GREEN | NOVA | ZED  | INSUFFICIENT |

Mechanical-policy transfer expectations:

```text
S0: INSUFFICIENT x18

G1:
RED=follow VALE; BLUE=follow VALE; GOLD=follow VALE; SILVER=follow VALE; GREEN=follow VALE

C1:
RED=follow VALE; BLUE=follow VALE; GOLD=follow VALE; SILVER=follow VALE; GREEN=INSUFFICIENT

C2:
RED=follow VALE; BLUE=follow ORBIT; GOLD=follow ORBIT; SILVER=follow VALE; GREEN=INSUFFICIENT
```

Expected aggregate M2 scores under exact policy compliance:

```text
S0 = 2/18
G1 = 8/18
C1 = 10/18
C2 = 10/18
```

The C1/C2 aggregate tie is intentional. They fail for different causal reasons.

## 10. Required output

Each run must return exactly:

```text
STATE_RED: ORBIT|VALE|UNRESOLVED
STATE_BLUE: ORBIT|VALE|UNRESOLVED
STATE_GOLD: ORBIT|VALE|UNRESOLVED
STATE_SILVER: ORBIT|VALE|UNRESOLVED
STATE_GREEN: ORBIT|VALE|UNRESOLVED
T1: ZED|NOVA|INSUFFICIENT, <0-100>
...
T18: ZED|NOVA|INSUFFICIENT, <0-100>
```

No rationale during primary collection.

## 11. Measures

### M1 — policy-state reconstruction

Exact match of all five state lines to the arm's frozen expected state.

### M2 — overall transfer accuracy

Exact match to T1-T18 hidden oracle.

Aggregate accuracy alone is insufficient because C1 and C2 are intentionally tied under exact compliance.

### M3 — known-context action coverage

Number of T1-T16 answered with `ZED` or `NOVA` rather than `INSUFFICIENT`.

This exposes the cost of total impermeability.

### M4 — adaptation lag on true shifts

True-shift contexts are RED and GOLD (T1-T4, T9-T12).

Count items where the response fails to follow current VALE regime.

Expected under exact policy compliance:

```text
S0: 8 non-adaptive abstentions
G1: 0
C1: 0
C2: 4
```

### M5 — noise-capture / false plasticity on stable contexts

Stable/noise contexts are BLUE and SILVER (T5-T8, T13-T16).

Count items where the response follows VALE although the current regime remains ORBIT.

Expected under exact policy compliance:

```text
S0: 0 false-plasticity actions
G1: 8
C1: 8
C2: 4
```

M4 and M5 must be read together. Low false plasticity achieved only by never acting is not the same phenotype as useful selective adaptation.

### M6 — unseen-context false activation

Count T17-T18 actions instead of `INSUFFICIENT`.

Expected:

```text
S0=0, G1=2, C1=0, C2=0
```

### M7 — confidence calibration

Compare mean confidence by correct action, incorrect action and justified `INSUFFICIENT`. Descriptive only.

## 12. Sample and stop rule

Initial primary collection:

```text
one fresh Temporary Chat per arm
= 4 initial runs
```

Frozen replication trigger:

Run one additional fresh replicate for **all four arms** if any initial run has:

1. `M1 != 5/5`; or
2. a transfer vector incompatible with its own reported policy state on at least 2 items; or
3. two or more treatment arms collapse to identical state + transfer output despite their frozen policy-state differences.

If triggered, replicate all arms once.

Maximum planned primary sample:

```text
8 valid runs total
```

Do not add further runs to rescue a preferred pattern.

## 13. Validity and replacement rules

Protocol-invalid only for objective execution failure such as:

- wrong treatment prompt;
- truncated treatment payload;
- visibly wrong model/session configuration;
- context contamination from another arm/project;
- first complete output lost;
- treatment edited or worker tutored before first output.

Behavioral mistakes, policy misunderstanding, low accuracy, high confidence or an unfavorable ENA result are **data**, not replacement grounds.

## 14. Preregistered result patterns

### Pattern A — policy-level mechanism active

Different update policies produce their predicted distinct state/error profiles over the identical history.

Interpretation:

> Object-level experience alone does not determine the later phenotype; the update policy materially shapes what that experience becomes for later action.

This supports `STATE MUTATION != LEARNING-RULE MUTATION` at the tested in-context mechanism level.

### Pattern B — contextual scope suppresses unsupported generalization

C1/C2 avoid GREEN false activation while G1 generalizes its global preference into GREEN.

Interpretation: context-bounded trust scope is behaviorally meaningful in this fixture.

### Pattern C — plasticity/inertia trade-off appears

C1 shows lower adaptation lag but higher noise capture than C2; C2 reduces capture while accepting more lag.

Interpretation:

> selective permeability is a trade-off surface, not a free improvement.

Do not rename C2 as universally better when C1 and C2 tie overall or exchange different error types.

### Pattern D — static impermeability avoids corruption but loses useful adaptation

S0 has low false-plasticity/unknown-context error but fails to act on known shifted contexts.

Interpretation: maximum resistance is not equivalent to viable learning.

### Pattern E — treatment collapse / Host override

Arms tie or the model ignores assigned policy enough that state/error profiles do not separate.

Interpretation: this treatment does not establish a usable metamemory mechanism on this Host/task.

### Pattern F — high instability

Initial/replicate outputs materially disagree within arm.

Interpretation: Host/instruction variability prevents a clean policy-level conclusion. Preserve and narrow rather than run until a preferred pattern appears.

## 15. Track-5 closure rule

After formal scoring, active Track 5 probing should stop unless the result exposes a genuinely new unresolved discriminator.

Allowed closure dispositions:

- `MECHANISM_ACTIVE_BUT_POLICY_OPTIMUM_UNRESOLVED`;
- `NARROWED_OR_REJECTED_ON_THIS_HOST_TASK`;
- `FIELD_UNRESOLVED_FOR_DURABLE_SELF_MODIFICATION`.

The experiment does not need separate primary rounds for every possible metamemory control. Remaining axes such as replay priority, forgetting rate, generalization width or parameter-level self-modification may remain explicit future/field questions rather than keeping the current research round permanently open.

## 16. No preferred-result reruns

```text
NEGATIVE RESULT != FAILED RESEARCH

TRADE-OFF != FAILURE TO FIND A WINNER

MECHANISM RESULT != CURRENT CHANGE
```

Do not modify `releases/current/` from this experiment alone.
