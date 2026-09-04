# Temporal Assimilation / Developmental Order — Preregistration

Date: `2026-09-04`

Status: `PREREGISTERED_BEFORE_PRIMARY_OUTPUTS / NOT_CURRENT / MECHANISM_DISCRIMINATION`

Current baseline remains: `v0.3.7 / CURRENT / FIELD_VALIDATION`.

This experiment does **not** modify `releases/current/` and does not assume that developmental order matters.

## 1. Why this experiment exists

The completed MDS experiment found:

```text
M0 — no inheritance:    22/36
M1 — full archive:      36/36
M2 — distilled rules:   36/36
M3 — developmental/MDS: 36/36
```

Therefore inherited information mattered in the Morrow fixture, but a developmental/MDS carrier did not outperform distilled rules. The next unresolved question is not another representation comparison. It is whether the **temporal path of acquisition itself** can leave a later behavioral trace when the externally supplied information set is held constant.

Candidate relations under test:

```text
HAVING THE SAME FINAL INFORMATION SET
!=
HAVING BEEN SHAPED BY THE SAME HISTORY

CORRECTION
!=
RECONSOLIDATION
```

A complete tie is a valid narrowing result.

## 2. Known background and what would *not* be novel here

Published work already shows that LLM in-context learning is sensitive to example order and position. Relevant examples include:

- Guo et al., *What Makes a Good Order of Examples in In-Context Learning*, Findings of ACL 2024: https://aclanthology.org/2024.findings-acl.884/
- Xiang et al., *Addressing Order Sensitivity of In-Context Demonstration Examples in Causal Language Models*, Findings of ACL 2024: https://aclanthology.org/2024.findings-acl.386/
- Bhope et al., *OptiSeq: Ordering Examples On-The-Fly for In-Context Learning*, Findings of EMNLP 2025: https://aclanthology.org/2025.findings-emnlp.1353/
- Chu et al., *Towards Order Fairness: Mitigating LLMs Order Sensitivity through Dual Group Advantage Optimization*, ACL 2026: https://aclanthology.org/2026.acl-long.219/

Therefore:

```text
SAME EXAMPLES + DIFFERENT PROMPT ORDER -> DIFFERENT ANSWER
```

by itself would only reproduce generic order sensitivity.

The ENA-relevant question is narrower and stronger: do staged experience, intermediate commitment, feedback and later correction produce a coherent **developmental path dependence** that survives after all arms have received the same external evidence, and does any such effect persist after an identical explicit correction?

## 3. Scope claim

This is a **within-session developmental-path experiment** on a ChatGPT Temporary Chat Host.

It does **not** test durable cross-session memory, parameter learning, literal biological development, or long-term identity continuity.

If an effect appears, the strongest allowed first-round statement is:

> Within this Host/task family, staged acquisition order can alter a later in-context phenotype despite an identical external evidence set.

A stronger claim about durable assimilation across sessions would require later evidence.

## 4. Experimental Host and relay

Primary Host target:

```text
ChatGPT Temporary Chat
GPT-5.6 Sol
fresh session per run
```

Use the same visible model/reasoning configuration for every valid primary run.

The local Codex installation is **transport only**. It is not a scientific participant, scorer, critic or validator.

Relay contract:

1. create one new ChatGPT Temporary Chat for each run;
2. keep all stages for that run in the same Temporary Chat;
3. copy each manager payload exactly, without summarizing, rewriting or adding advice;
4. never reveal a future stage before its turn;
5. capture the first complete Temporary Chat response verbatim;
6. return it to the manager wrapped only with run/stage metadata;
7. do not correct a response, ask follow-ups or retry because the answer looks poor;
8. start a replacement run only for an objective protocol failure, never for behavioral quality;
9. do not expose the ENA repository, this preregistration, the oracle or other arms to the Temporary Chat;
10. Codex may perform mechanical browser/clipboard actions but must not contribute substantive reasoning.

Canonical return wrapper:

```text
[TEMPORARY_CHAT_RELAY]
RUN_ID: <run>
ARM: <arm>
STAGE: <stage>
SOURCE: ChatGPT Temporary Chat (separate tab)
RAW_RESPONSE:
<verbatim first complete response>
```

## 5. Primary experimental contrast

Three arms receive the **same six authoritative training episodes and the same feedback**, with the same number of interaction stages and the same final two-episode suffix. Only the order of the first four episodes differs.

This controls much of the trivial last-example/recency difference while allowing different early hypotheses to form.

### MF — misleading-first

```text
E1 -> E2 -> E3 -> E4 -> E5 -> E6
```

The first two labeled outcomes are consistent with an easy but wrong Aster/Beryl heuristic.

### CF — corrective/boundary-first

```text
E3 -> E4 -> E1 -> E2 -> E5 -> E6
```

Early evidence breaks the Aster/Beryl shortcut before the two shortcut-consistent cases are seen.

### INT — interleaved

```text
E1 -> E3 -> E2 -> E4 -> E5 -> E6
```

Shortcut-supporting and shortcut-breaking evidence are interleaved early.

All three arms share the exact suffix:

```text
E5 -> E6
```

## 6. Synthetic task and hidden rule

The Temporary Chat is told that it is learning an unknown routing rule from sequential feedback.

Input features are arbitrary binary tokens:

```text
Aster = ON/OFF
Beryl = ON/OFF
Coda  = ON/OFF
Dune  = ON/OFF
```

Actions:

```text
ZED
NOVA
```

Frozen oracle, hidden during acquisition:

```text
ZED iff Coda=ON AND Dune=OFF.
Otherwise NOVA.
Aster and Beryl are causally irrelevant.
```

### Authoritative episode set

| Episode | Aster | Beryl | Coda | Dune | Correct action |
|---|---|---|---|---|---|
| E1 | ON | OFF | ON | OFF | ZED |
| E2 | OFF | ON | OFF | OFF | NOVA |
| E3 | ON | ON | OFF | OFF | NOVA |
| E4 | OFF | OFF | ON | OFF | ZED |
| E5 | ON | OFF | ON | ON | NOVA |
| E6 | OFF | ON | ON | ON | NOVA |

E1+E2 jointly permit a plausible early shortcut in which Aster or inverse-Beryl appears decisive. E3+E4 break that shortcut. E5+E6 reveal Dune's role.

## 7. Staged acquisition protocol

Each run is genuinely sequential.

### Acquisition Stage 1

Give the common task instructions and the arm's first unlabeled episode. Require exactly:

```text
ACTION: ZED | NOVA
WORKING_RULE: <one sentence, <= 25 words>
CONFIDENCE: <0-100>
```

### Acquisition Stages 2-6

Each next manager turn contains:

1. the authoritative correct action for the previous episode;
2. the next unlabeled episode;
3. the same required response format.

This creates the causal sequence:

```text
experience
-> prediction / working hypothesis
-> authoritative feedback
-> next experience
```

The model's own intermediate working rules are allowed to differ across arms. That endogenous difference is part of the developmental state under study and must not be normalized away.

### Acquisition close

After feedback for the sixth episode, ask for:

```text
FINAL_RULE: <one sentence, <= 30 words>
CAUSAL_FEATURES: <comma-separated>
IRRELEVANT_FEATURES: <comma-separated>
CONFIDENCE: <0-100>
```

At this point every sequential arm has received the same six externally supplied labeled episodes. Only developmental order and its endogenous response history differ.

## 8. Pre-correction transfer battery

After acquisition closes, give all items below in one frozen turn. Require one line per item with only:

```text
<ID>: <ZED|NOVA|INSUFFICIENT>, <confidence 0-100>
```

No rationale is requested during the primary battery.

Frozen pre-correction oracle:

| ID | Aster | Beryl | Coda | Dune | Oracle |
|---|---|---|---|---|---|
| P1 | ON | ON | ON | OFF | ZED |
| P2 | OFF | OFF | OFF | OFF | NOVA |
| P3 | ON | ON | OFF | ON | NOVA |
| P4 | OFF | ON | ON | OFF | ZED |
| P5 | ON | OFF | OFF | OFF | NOVA |
| P6 | OFF | OFF | ON | ON | NOVA |
| P7 | ON | ON | ON | ON | NOVA |
| P8 | OFF | ON | OFF | ON | NOVA |

Lexical-transfer items use the explicit mapping:

```text
P = Aster
Q = Beryl
R = Coda
S = Dune
```

| ID | P | Q | R | S | Oracle |
|---|---|---|---|---|---|
| L1 | ON | ON | ON | OFF | ZED |
| L2 | ON | OFF | OFF | OFF | NOVA |

Uncertainty item:

```text
U1: Aster=ON, Beryl=OFF, Coda=ON, Dune=UNKNOWN
Oracle: INSUFFICIENT
```

Pre-correction total: **11 items**.

## 9. Identical explicit correction

After the pre-correction battery has been frozen, every arm receives the exact same correction:

```text
AUTHORITATIVE FINAL RULE

ZED iff Coda=ON AND Dune=OFF.
Otherwise NOVA.
Aster and Beryl never affect routing.
If either Coda or Dune is unknown, the routing action cannot be determined from the available information.
```

No arm-specific explanation is allowed.

This creates a second, stronger test:

```text
EXPLICIT CORRECTION
-> does earlier path still leave residual behavior?
```

## 10. Post-correction transfer battery

Use novel combinations, not a repeat of the pre-correction items.

| ID | Aster | Beryl | Coda | Dune | Oracle |
|---|---|---|---|---|---|
| C1 | ON | OFF | ON | OFF | ZED |
| C2 | ON | ON | OFF | OFF | NOVA |
| C3 | OFF | OFF | ON | ON | NOVA |
| C4 | OFF | ON | ON | OFF | ZED |
| C5 | OFF | OFF | OFF | ON | NOVA |
| C6 | ON | ON | OFF | ON | NOVA |

Lexical remap:

```text
J = Aster
K = Beryl
M = Coda
N = Dune
```

| ID | J | K | M | N | Oracle |
|---|---|---|---|---|---|
| C7 | ON | OFF | ON | OFF | ZED |
| C8 | OFF | ON | OFF | OFF | NOVA |

Uncertainty:

```text
C9: Aster=OFF, Beryl=ON, Coda=UNKNOWN, Dune=OFF
Oracle: INSUFFICIENT
```

Post-correction total: **9 items**.

## 11. Primary measures

### M1 — final learned-rule reconstruction

`PASS` only if the acquisition-close response identifies:

- `Coda=ON` as required;
- `Dune=OFF` as required;
- Aster and Beryl as non-causal/irrelevant, or otherwise clearly excludes them from the decision rule.

Preserve the exact text regardless of pass/fail.

### M2 — pre-correction transfer accuracy

Score 1 per exact oracle action across P1-P8, L1-L2 and U1.

Maximum: `11` per run.

### M3 — post-correction transfer accuracy

Score 1 per exact oracle action across C1-C9.

Maximum: `9` per run.

### M4 — developmental debt signatures

Tag exact action failures where applicable:

- `ASTER_FALSE_ACTIVATION`: ZED chosen on an item where Aster=ON but the causal rule requires NOVA;
- `BERYL_FALSE_SUPPRESSION`: NOVA chosen on an item where Beryl=ON but the causal rule requires ZED;
- `DUNE_OVERRIDE_MISSED`: ZED chosen despite Dune=ON;
- `CAUSAL_MISS`: NOVA chosen despite Coda=ON and Dune=OFF;
- `OVERCONFIDENT_UNDERDETERMINATION`: ZED/NOVA chosen when a required causal feature is UNKNOWN.

The same tags apply after explicit correction. A post-correction spurious-cue failure is stronger evidence of residual developmental debt than a pre-correction failure.

### M5 — acquisition trajectory

Preserve each prediction, working rule and confidence before feedback.

Secondary adjudication may classify when the first correct working rule appears and whether a falsified shortcut reappears.

Do **not** use subjective trajectory classification to overwrite primary action scores.

### M6 — calibration

Compare confidence for correct, incorrect and underdetermined items. Treat this as secondary unless an arm difference is large and coherent.

## 12. What counts as developmental assimilation rather than generic order bias

A mere arm difference in final answers is insufficient for a strong developmental interpretation.

Evidence is stronger when all of the following align:

1. the early order induces a predictable working hypothesis;
2. authoritative counterevidence falsifies that hypothesis;
3. the hypothesis or its action signature persists after falsification;
4. later transfer errors are specifically consistent with that earlier hypothesis;
5. the pattern repeats within the same arm across fresh runs.

If outputs vary with order but do not show a coherent path-linked trajectory, classify the result as **generic order sensitivity / unstable in-context inference**, not developmental assimilation.

## 13. Sample and run schedule

Primary target: **9 valid runs**.

```text
MF  = 3 fresh Temporary Chats
CF  = 3 fresh Temporary Chats
INT = 3 fresh Temporary Chats
```

Frozen execution order generated before outputs with seed `20260904`:

```text
CF-1
INT-1
MF-1
MF-2
INT-2
CF-2
CF-3
MF-3
INT-3
```

Do not reorder because an earlier result is interesting or disappointing.

## 14. Validity and replacement policy

Exclude a run only for objective protocol deviation established independently of behavioral quality, including:

- not actually a fresh Temporary Chat;
- wrong arm/order payload;
- future stage leaked early;
- relay substantively rewrote manager payload or model output;
- response was corrected/retried before first-output capture;
- requested Host/model configuration was not used and the mismatch is known;
- cross-run contamination is known.

Preserve every excluded attempt separately with the reason.

Replacement naming:

```text
<ARM>-R1
<ARM>-R2
...
```

Replacement continues until 9 valid primary runs exist. Do not replace a valid run because it scores poorly, ties, looks strange or weakens the preferred hypothesis.

## 15. Preregistered interpretation matrix

### Pattern A — all three arms converge before and after correction

Interpretation:

- no observed developmental-order effect under this Host/task family;
- staged order did not produce measurable residual phenotype beyond final evidence;
- narrow the stronger claim that developmental history is intrinsically non-compressible here.

Do not rerun merely to seek an order effect.

### Pattern B — pre-correction arm differences, post-correction convergence

Interpretation:

- order affects acquisition / working schema;
- identical explicit correction removes the observed behavioral difference;
- support transient path dependence, **not** persistent developmental debt.

### Pattern C — MF underperforms CF/INT before correction and remains worse after identical correction

Interpretation:

- support for residual developmental debt / incomplete reconsolidation within-session;
- strongest if errors match the early Aster/Beryl shortcut and trajectories show its persistence;
- still not evidence of cross-session durable assimilation.

### Pattern D — MF underperforms before correction but catches up immediately after correction

Interpretation:

- misleading-first ordering slows or distorts acquisition;
- correction is sufficient to reconsolidate the tested phenotype.

### Pattern E — INT consistently outperforms both clustered orders before correction

Interpretation:

- interleaving may reduce premature schema commitment in this fixture;
- treat as a mechanism candidate, not a general learning law.

### Pattern F — direct items tie, lexical-transfer items differ

Interpretation:

- any path effect is concentrated in abstraction/generalization rather than basic rule execution.

### Pattern G — accuracy ties but uncertainty/calibration differs coherently

Interpretation:

- path may affect confidence phenotype without affecting action accuracy;
- narrow claims accordingly.

### Pattern H — high within-arm variance or inconsistent direction

Interpretation:

- weak developmental fidelity / unstable Host behavior;
- no strong arm-level mechanism claim.

### Pattern I — differences are explained primarily by immediate position/recency with no coherent working-rule trajectory

Interpretation:

- generic positional/order bias is the better explanation;
- do not promote to ENA developmental assimilation evidence.

## 16. Stop and continuation rules

After 9 valid runs:

1. adjudicate exactly against this preregistration;
2. preserve null/tie results;
3. do not add runs merely because the result is ambiguous or disappointing;
4. if a coherent developmental-debt signal appears, the next step is a different task family and/or cross-Host replication, not more same-fixture repetitions;
5. if all arms tie, narrow the hypothesis and continue the Coverage Map rather than force a positive result;
6. no `releases/current/` change follows directly from this mechanism round.

## 17. Separation from the relay proof

Any earlier relay-proof Temporary Chat response, including `relay-proof-2026-09-04-01`, is a transport test only and is **not** part of this experiment. It was produced before this preregistration and did not receive the frozen ENA/task context required here.
