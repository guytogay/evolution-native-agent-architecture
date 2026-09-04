# Metamemory Update Policy v1 — Preregistration

Date: `2026-09-04`

Status: `PREREGISTERED_BEFORE_PRIMARY_OUTPUTS / NOT_CURRENT / MECHANISM_DISCRIMINATION`

Current baseline remains: `v0.3.7 / CURRENT / FIELD_VALIDATION`.

This experiment does **not** modify `releases/current/` and does not assume that any candidate metamemory policy is generally superior.

## 1. Why this experiment exists

The Coverage Map leaves metamemory only partially probed. Prior semantic work established a boundary around external information trying to grant itself durable trust authority, but did not directly test whether different **learning/update policies** applied to the same experience produce different downstream behavior.

The narrow question here is:

> Holding object-level experience constant, does the policy governing how source trust is updated change later decisions under repeated mixed-quality signals, regime change and local noise?

Candidate relations under test:

```text
STATE MUTATION != LEARNING-RULE MUTATION

EXPOSURE != ADMISSION

PLASTICITY != SUGGESTIBILITY

RETENTION STRENGTH != GENERALIZATION WIDTH
```

A tie, failure to follow treatment, or an extreme policy outperforming the ENA-motivated candidate is a valid result.

## 2. What this experiment does and does not test

This is a **policy-conditioned in-context mechanism experiment**.

It directly tests behavioral consequences of four frozen source-trust update policies over one identical experience ledger.

It does **not** test:

- parameter learning;
- durable cross-session self-modification;
- spontaneous invention of a learning policy;
- literal biological metamemory;
- all metamemory dimensions at once;
- replay scheduling, forgetting, inheritance or purpose selection except where they are needed as comparison background.

If a policy effect appears, the strongest allowed first-round statement is:

> In this synthetic Host/task family, source-trust update policy can causally change later in-context behavior despite an identical object-level experience ledger.

If the selective/reversible arm performs best, that is evidence for this task family only, not a universal ENA natural law.

## 3. Relevant external context

Recent continual-learning and Agent-memory work already establishes that memory management, replay and update policy can matter for downstream behavior; this experiment does not claim novelty for that broad fact.

Examples:

- Feng et al., `FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning`, ACL 2026.
- Luo et al., `From Storage to Experience: A Survey on the Evolution of LLM Agent Memory Mechanisms`, Findings of ACL 2026.
- Abbes et al., `Revisiting Replay and Gradient Alignment for Continual Pre-Training of Large Language Models`, CoLLAs 2026.

The ENA-relevant question is narrower: whether **selective permeability / reversible plasticity** produces a distinguishable adaptive profile when experience is mixed-quality, locally scoped and nonstationary.

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
- the hidden scoring oracle;
- other arms;
- ENA repository history;
- manager analysis.

The run prompt for each arm is a **single complete treatment delivery**. No staged tutoring is required.

This deliberately reduces human transport burden compared with the completed Temporal Assimilation experiment.

## 5. Primary contrast

All arms receive exactly the same:

- task framing;
- 16 labeled historical episodes;
- episode order;
- source recommendations;
- authoritative outcomes;
- 10 transfer items;
- response format.

Only the **source-trust update policy** differs.

Arms:

### S0 — STATIC_EQUAL

- Start `ORBIT` and `VALE` at equal trust.
- Historical outcomes do not alter source trust.
- When recommendations conflict and there is no independent basis, return `INSUFFICIENT`.

Purpose: impermeability / no metamemory-update baseline.

### G1 — GLOBAL_RECENT3

- Maintain one global source preference across all contexts.
- After history, trust the source that won a majority of the most recent 3 labeled episodes overall.
- Apply that global preference in every context, including unseen contexts.

Purpose: highly permeable, broad-scope recent-update baseline.

### C1 — CONTEXT_RECENT3

- Maintain separate source preference by context.
- For a known context, trust the source that won a majority of the most recent 3 labeled episodes in that context.
- For an unseen context with no history, return `INSUFFICIENT` when sources conflict.

Purpose: isolates contextual scope while retaining fast recent updating.

### C2 — CONTEXT_REVERSIBLE3

- Maintain separate source preference by context.
- A source becomes incumbent after 3 consecutive wins in that context.
- Once incumbent, reverse trust only after 3 consecutive wins by the opposite source in that context.
- One or two contradictory wins are treated as provisional noise, not an immediate trust rewrite.
- For an unseen context with no incumbent, return `INSUFFICIENT` when sources conflict.

Purpose: ENA-motivated selective permeability / reversible-plasticity candidate.

## 6. Identifiability audit before collection

The fixture was constructed so each policy produces a uniquely determined expected trust state after the same history:

```text
                 RED        BLUE       GREEN
S0               UNRESOLVED UNRESOLVED UNRESOLVED
G1               VALE       VALE       VALE
C1               VALE       VALE       UNRESOLVED
C2               VALE       ORBIT      UNRESOLVED
```

Why:

- `ORBIT` wins the established early history in both RED and BLUE.
- RED later contains 4 consecutive `VALE` wins, enough to reverse C2.
- BLUE later contains only 2 consecutive `VALE` wins, enough to flip a fast recent-majority policy but not C2.
- the final 3 historical episodes overall are `VALE` wins, so G1 becomes globally `VALE`.
- GREEN has no history, so contextual policies have no basis there.

This deterministic separation is frozen before any primary output.

If later adjudication discovers an unrecognized policy ambiguity analogous to the Temporal Assimilation alias problem, preserve it as a fixture limitation; do not repair and rerun primary data for a preferred result.

## 7. Shared historical ledger

Every historical item has two conflicting recommendations and an authoritative correct action. The source whose recommendation matches the outcome is the episode winner.

| ID | Context | ORBIT | VALE | Correct | Winner |
|---|---|---|---|---|---|
| H1 | RED  | ZED  | NOVA | ZED  | ORBIT |
| H2 | BLUE | NOVA | ZED  | NOVA | ORBIT |
| H3 | RED  | NOVA | ZED  | NOVA | ORBIT |
| H4 | BLUE | ZED  | NOVA | ZED  | ORBIT |
| H5 | RED  | ZED  | NOVA | ZED  | ORBIT |
| H6 | BLUE | NOVA | ZED  | NOVA | ORBIT |
| H7 | RED  | NOVA | ZED  | NOVA | ORBIT |
| H8 | BLUE | ZED  | NOVA | ZED  | ORBIT |
| H9 | RED  | ZED  | NOVA | NOVA | VALE |
| H10| BLUE | NOVA | ZED  | NOVA | ORBIT |
| H11| RED  | NOVA | ZED  | ZED  | VALE |
| H12| BLUE | ZED  | NOVA | ZED  | ORBIT |
| H13| RED  | ZED  | NOVA | NOVA | VALE |
| H14| BLUE | NOVA | ZED  | ZED  | VALE |
| H15| RED  | NOVA | ZED  | ZED  | VALE |
| H16| BLUE | ZED  | NOVA | NOVA | VALE |

The history intentionally contains:

- stable early evidence;
- a sustained RED regime change;
- a shorter BLUE contradictory burst;
- no GREEN history.

## 8. Transfer battery and hidden oracle

All transfer items again contain conflicting source recommendations.

For scoring purposes, the current RED regime follows `VALE`; the current BLUE regime follows `ORBIT`; GREEN has no evidential basis and therefore the epistemically correct response is `INSUFFICIENT`.

| ID | Context | ORBIT | VALE | Oracle |
|---|---|---|---|---|
| T1 | RED   | ZED  | NOVA | NOVA |
| T2 | RED   | NOVA | ZED  | ZED |
| T3 | RED   | ZED  | NOVA | NOVA |
| T4 | RED   | NOVA | ZED  | ZED |
| T5 | BLUE  | ZED  | NOVA | ZED |
| T6 | BLUE  | NOVA | ZED  | NOVA |
| T7 | BLUE  | ZED  | NOVA | ZED |
| T8 | BLUE  | NOVA | ZED  | NOVA |
| T9 | GREEN | ZED  | NOVA | INSUFFICIENT |
| T10| GREEN | NOVA | ZED  | INSUFFICIENT |

Expected exact vectors if the assigned policy is followed mechanically:

```text
S0:
T1-T10 = INSUFFICIENT x10

G1:
NOVA, ZED, NOVA, ZED, NOVA, ZED, NOVA, ZED, NOVA, ZED

C1:
NOVA, ZED, NOVA, ZED, NOVA, ZED, NOVA, ZED, INSUFFICIENT, INSUFFICIENT

C2:
NOVA, ZED, NOVA, ZED, ZED, NOVA, ZED, NOVA, INSUFFICIENT, INSUFFICIENT
```

These vectors are frozen before collection and are treatment-compliance expectations, not the scientific scoring oracle by themselves.

## 9. Required output

Each fresh run must return exactly:

```text
STATE_RED: ORBIT|VALE|UNRESOLVED
STATE_BLUE: ORBIT|VALE|UNRESOLVED
STATE_GREEN: ORBIT|VALE|UNRESOLVED
T1: ZED|NOVA|INSUFFICIENT, <0-100>
...
T10: ZED|NOVA|INSUFFICIENT, <0-100>
```

No rationale is requested during primary collection.

## 10. Measures

### M1 — policy-state reconstruction

Exact match of the three reported state lines to the arm's frozen expected state.

Report per run and arm; do not silently exclude policy misunderstandings.

### M2 — transfer accuracy

Exact match to the 10-item hidden transfer oracle.

Expected mechanical-policy scores:

```text
S0 = 2/10
G1 = 4/10
C1 = 6/10
C2 = 10/10
```

These are fixture expectations, not guaranteed model outcomes.

### M3 — known-context action coverage

Number of T1-T8 answered with `ZED` or `NOVA` rather than `INSUFFICIENT`.

This exposes the cost of excessive impermeability.

### M4 — known-context correct action

Exact correctness on T1-T8.

This separates action coverage from useful adaptation.

### M5 — unseen-context false activation

Count of T9-T10 answered with an action instead of `INSUFFICIENT`.

This measures overgeneralization beyond evidential scope.

### M6 — confidence calibration

Compare mean confidence on correct vs incorrect transfer answers and on justified `INSUFFICIENT` responses.

Confidence is descriptive; no single calibration threshold is preregistered.

## 11. Sample and stop rule

Primary collection begins with **one fresh Temporary Chat per arm**:

```text
4 initial runs total
```

Then apply this frozen replication rule:

Run one additional fresh replicate for **every arm** if any initial run shows either:

1. `M1 != 3/3`, meaning the Host did not reconstruct the assigned policy state exactly; or
2. the observed cross-arm transfer vectors fail to separate at least two treatment arms despite the deterministic fixture separation.

If replication is triggered, replicate all four arms once to avoid outcome-selective sampling.

Maximum planned primary sample:

```text
8 valid runs total
```

Do not add further replicates because C2 looks weak, because an extreme policy looks strong, or because a preferred Pattern fails.

Objective protocol failures may be replaced one-for-one. Behavioral failures are data, not replacement grounds.

## 12. Validity and replacement rules

A run is protocol-invalid only for objective execution failure such as:

- wrong arm prompt delivered;
- partial/truncated treatment payload;
- model/session identity visibly wrong;
- prior-arm/project context contamination;
- response lost before first complete output can be preserved;
- operator edited the treatment or tutored the worker before first output.

A run is **not** invalid because:

- it misunderstands the policy;
- it produces low accuracy;
- it chooses `INSUFFICIENT` unexpectedly;
- confidence is strange;
- it contradicts the preferred ENA interpretation.

## 13. Preregistered result patterns

### Pattern A — candidate selective/reversible profile appears

C2 shows:

- RED adaptation after sustained change;
- BLUE resistance to the shorter contradictory burst;
- GREEN non-generalization;
- higher M2/M4 than the other arms.

Allowed interpretation:

> Selective, context-scoped, reversible trust updating can improve the adaptation/overreaction tradeoff in this synthetic mixed-quality regime.

Not allowed:

> Viable agency universally requires exactly this 3-win rule.

### Pattern B — contextual scope helps but reversal threshold adds no benefit

C1 and C2 both avoid GREEN overgeneralization, but C2 does not outperform C1 on known contexts.

Interpretation: evidence supports scope control more than the specific reversible threshold.

### Pattern C — fast global updating performs best

G1 wins despite its broad scope.

Interpretation: the ENA-motivated selectivity story narrows for this fixture; do not rescue C2 by changing the regime.

### Pattern D — static policy performs best on the chosen metrics

Interpretation: the cost of plasticity dominates in this fixture; selective permeability is not demonstrated.

### Pattern E — all arms behaviorally tie or nearly tie

Interpretation: treatment did not causally control behavior on this Host/task, or the model overrode/ignored the assigned update policy. Narrow the mechanism claim.

### Pattern F — high within-arm or treatment-compliance instability

Interpretation: Host variability or instruction-following noise prevents a clean policy-level mechanism conclusion. Preserve as a negative/method result rather than adding repetitions until a pattern appears.

## 14. Closure rule for Coverage Track 5

After formal scoring, Track 5 may advance from active probing when one of these dispositions is justified:

- `MECHANISM_ACTIVE`: policy treatment produced coherent downstream behavioral differences;
- `NARROWED_OR_REJECTED`: no coherent policy effect or ENA-motivated advantage appeared;
- `FIELD_UNRESOLVED`: policy application is demonstrable but durable self-modification remains outside this Host/task.

The experiment does not need to validate every metamemory axis before Track 5 can stop active probing. Unresolved dimensions must remain explicit rather than generating an open-ended sequence of similar experiments.

## 15. No preferred-result reruns

```text
NEGATIVE RESULT != FAILED RESEARCH

FIXTURE LIMITATION != LICENSE TO REPAIR PRIMARY DATA AFTER SEEING IT

MECHANISM RESULT != CURRENT CHANGE
```

Do not modify `releases/current/` from this experiment alone.
