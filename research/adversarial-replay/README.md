# Historical Adversarial Replay

Status: `RESEARCH_INFRASTRUCTURE / NON_NORMATIVE`

Historical Adversarial Replay (HAR) uses real historical agent failures to attack the current ENA MAINLINE semantics.

The purpose is **not** to reward ENA for being able to explain an incident after the fact. The purpose is to test whether the current semantics would force an honest claim boundary before or during the failure.

## Core question

For each incident:

> What false protection, health, evidence, authority, completion, provenance, or history claim became possible, and would current ENA v0.2.11 MAINLINE prevent or correctly qualify that claim?

## Pipeline

`Historical incident → observed facts → false claim → boundary crossed → current ENA mapping → expected ENA behavior → verdict`

Allowed primary verdicts:

- `COVERED` — current ENA semantics already make the false claim invalid without material clarification.
- `COVERED_BUT_AMBIGUOUS` — the intended semantics appear present, but wording/field boundaries can plausibly permit an incorrect interpretation.
- `HOST_SPECIFIC` — the failure is mainly an implementation defect, not a Universal semantic gap.
- `CLARIFICATION_GAP` — existing ENA concepts are sufficient in substance, but a portable clarification is needed.
- `NORMATIVE_GAP` — existing ENA cannot honestly express or block the failure class without a new normative semantic.
- `UNKNOWN` — evidence is insufficient.

## Evidence discipline

A replay case must distinguish:

- observed historical fact;
- inference;
- current ENA mapping;
- candidate abstraction;
- unresolved unknowns.

A clever abstraction is not evidence of a Universal gap.

## Current replay set

| Case | Theme | Verdict |
|---|---|---|
| HAR-001 | Session Context Lineage | `CLARIFICATION_GAP` |
| HAR-002 | DSH k-0083 restore/history gap | `COVERED` |
| HAR-003 | Distributed History Merge | `CLARIFICATION_GAP` |
| HAR-004 | Hook registered/ready but never fired | `COVERED` |
| HAR-005 | Context truncation / projection semantics | `COVERED_BUT_AMBIGUOUS` |
| HAR-006 | Evidence Applicability across gateway instances/states | `CLARIFICATION_GAP` |

### Early interpretation

The replay corpus is already doing useful subtraction:

- `Activation Witness / Trigger Effect Evidence` currently looks like a worked example of existing activation semantics rather than a new normative rule.
- the DSH k-0083 incident is already semantically covered by v0.2.11 History/Projection rules; remaining pressure is host implementation and salience.
- `Evidence Applicability Boundary` remains the strongest clarification candidate.
- `General Projection Semantics` remains promising but is not yet justified as a Universal architecture.
- `Distributed History Merge Semantics` needs an independent non-Git multi-writer case before stronger promotion pressure is warranted.

## Promotion discipline

HAR cases enter `research/` first. They do not change MAINLINE.

A future normative candidate should normally require more than one attractive incident, and should demonstrate that existing ENA semantics plus clarification cannot already cover the failure.

> Historical coverage should rise faster than Universal semantic complexity.
