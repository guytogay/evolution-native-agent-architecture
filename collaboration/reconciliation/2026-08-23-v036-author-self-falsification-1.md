# ENA v0.3.6 author self-falsification — pass 1

Status: `AUTHOR_SELF_FALSIFICATION / PRE_FREEZE / NOT_INDEPENDENT_VALIDATION`

Working head inspected: `921e23cbfb9d3c739a3c4cb74adc371e0efcd3ca` plus inherited candidate content.

This record preserves defects found by the authoring process before correction. Later fixes do not erase the occurrence of these findings.

## Finding A1 — latent variation was still forced to name a Variation Space

Severity: `MATERIAL_SEMANTIC_CONTRADICTION`

The candidate prose says a variation may remain latent without immediate experiment or verdict. However `schemas/evolution-record.v2.schema.json` inherited `variation_space` as a required non-empty string, and the v2 template used an empty string that did not validate against its own schema.

Failure modes:

- legitimate latent possibilities without a current experiment surface could be false-blocked;
- the schema would pressure authors to invent a fake Variation Space merely to satisfy structure;
- the provided template was internally invalid.

Required correction:

- keep the field represented but allow explicit `null` before a relevant experiment exists;
- template should use `null` rather than an invented/empty experimental surface;
- consequential expression/experiment still follows the real Variation Space rule when material.

## Finding A2 — expression could still self-assert without represented activation trace

Severity: `MATERIAL_FALSE_CLAIM_PATH`

The v2 schema allowed:

`expression_state = EXPRESSED`

with:

`expression_history = []`

Therefore the new expression axis could repeat an old ENA failure class: a stronger state could be created merely by setting a status field.

It also allowed the current `expression_state` to contradict the latest expression-history state.

Required correction:

- schema: `EXPRESSED` requires at least one expression-history entry;
- semantic validator: latest expression-history state must match current expression state;
- expression transition to `EXPRESSED` requires represented non-empty trigger;
- validation proves represented consistency only, not that the trigger happened in external reality.

## Finding A3 — inherited adoption files leaked v0.3.5 Current identity inside candidate

Severity: `MATERIAL_IDENTITY_LEAKAGE`

`AGENT-ADOPTION-INSTRUCTION.md` inside the v0.3.6 candidate still instructed an Agent to adopt v0.3.5 Current and read `CURRENT-BASELINE.yaml`; `LITE-ADOPTION-INSTRUCTION.md` still presented itself as v0.3.5.

This is truthful historical source content but unsafe as a live candidate file because a tool/Agent may open the file directly rather than first reading the candidate warning.

Required correction:

- candidate copies must identify themselves as candidate-only testing instructions;
- use `CANDIDATE-BASELINE.yaml`;
- explicitly forbid treating candidate testing as adoption/Current proof;
- preserve v0.3.5 originals unchanged under `releases/current/`.

## Finding A4 — candidate machine semantics are intentionally incomplete

Severity: `VISIBLE_RESIDUAL / NOT_YET_A_DEFECT`

The inherited `tools/ena_evolve.py` does not implement mutation pressure, latent-reservoir handling, or expression transitions.

The candidate baseline already states this accurately. Do not patch the large inherited tool merely to make the implementation look complete. First establish whether a small consistency validator is sufficient and whether an actual runtime expression command earns its complexity.

## Disposition

A1/A2/A3: correct before freeze.

A4: keep explicit until implementation evidence justifies change.

No Constitution ID is added as a response to these implementation/identity findings.

> Finding a defect before freeze is evolutionary evidence, not candidate failure to be hidden.
