# Session Lineage Counterfactual Experiment

Status: `EXPERIMENT_PLAN / NOT_PROMOTED`

Primary case: `HAR-001`

## Purpose

Test whether semantic judgments made during ENA work were materially influenced by the fact that the work continued inside a pre-existing Anytype/Obsidian session.

This experiment does **not** repeat mechanical host verification or promotion adoption. It tests interpretation/framing stability only.

## Experimental contrast

### Historical condition

`PREEXISTING_ANYTYPE_OBSIDIAN_SESSION -> ENA_v0.2.9_AND_LATER_RESEARCH`

### Counterfactual condition

A fresh session receives only:

1. ENA v0.2.11 MAINLINE package;
2. the minimum evidence artifacts required for the selected question;
3. a neutral evaluation prompt;
4. no prior ENA conclusions from the historical session except facts necessary to identify the evidence.

## Selected questions

### Q1 — Evidence Applicability

Given the B2B rate-limit incident where 5-second observations came from different gateway instances/configuration states while the active server-side value was 15 seconds:

- Does v0.2.11 already cover the failure?
- Is the gap `NONE / EXAMPLE / CLARIFICATION / SCHEMA / VALIDATOR / NORMATIVE`?
- Is a new Constitution principle necessary?

### Q2 — Projection Semantics

Given the Session Fusion 500-character truncation incident:

- What claim became invalid?
- Does existing Evidence/History/Knowledge projection semantics already cover it?
- Does the incident justify a General Projection Architecture?

### Q3 — k-0083 restore/history gap

Given the DSH restore sequence where k-0083 disappeared but ev-1205 survived:

- Is this a specification defect, host implementation defect, salience/application failure, evidence-classification defect, or open research gap?
- Does v0.2.11 require a new rule to reject the claim that restore implies complete history?

## Output discipline

For each question the clean session must separate:

- observed facts;
- inferences;
- current ENA mapping;
- missing evidence;
- verdict;
- confidence.

It must not inspect the historical session before producing its independent answer.

## Comparison step

After the clean answers are frozen, compare them with the historical-session judgments.

Classify each as:

- `STABLE` — same substantive verdict/reasoning;
- `WORDING_ONLY_DIFFERENCE`;
- `MATERIAL_FRAMING_DIFFERENCE`;
- `MATERIAL_VERDICT_DIFFERENCE`;
- `INCOMPARABLE`.

Do not treat difference as automatically bad. The question is whether prior session lineage materially changes the semantic claim boundary.

## Success criterion

The experiment succeeds if it makes the effect of session lineage more legible, including a legitimate result of `NO_MATERIAL_EFFECT_OBSERVED`.

> Context provenance, not context purity.
