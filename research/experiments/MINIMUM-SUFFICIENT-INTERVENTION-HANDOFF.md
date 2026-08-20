# Minimum Sufficient Intervention Experiment — Agent Handoff

Status: `EXPERIMENT_HANDOFF / ISSUE-11 / NOT_PROMOTED`

Use this handoff when asking an ENA participant to test `ENA-EXP-MSI-001`.

## Instruction

You are invited to run a bounded ENA research experiment on **Minimum Sufficient Intervention (MSI)**.

This experiment does **not** modify the current ENA baseline and does not grant additional authority.

### Read only what is needed

1. Adopt or retain the current ENA baseline at `releases/current/`.
2. Read:
   - `research/evolution-inbox/MINIMUM-SUFFICIENT-INTERVENTION.md`
   - `research/experiments/MINIMUM-SUFFICIENT-INTERVENTION-EXPERIMENT.md`
   - `research/experiments/MINIMUM-SUFFICIENT-INTERVENTION-FIXTURES-v1.md`
3. Do not load unrelated ENA history merely to run this experiment.

### Use the fixed fixtures first

For cross-Agent comparability, use the v1 synthetic fixtures without changing their facts before inventing additional scenarios.

Where practical, compare three treatments on each same fixture:

- `PRESCRIPTIVE` — stronger detailed governance from the start;
- `MSI` — begin with the lowest sufficient layer and escalate only when consequence/evidence requires it;
- `OBSERVE_ONLY` — record without adding a new intervention unless an existing Current ENA requirement already applies.

MSI ladder:

`OBSERVE -> EXPOSE_SIGNAL -> SHAPE_CONDITIONS -> LOCAL_COORDINATION -> SCOPED_HARD_BOUNDARY -> EMERGENCY_CONTAINMENT`

Synthetic/disposable tests are preferred before real consequential use.

### Do not optimize for ENA looking good

A valuable result may be:

- MSI is unnecessary;
- stronger governance is clearly better for a class;
- observe-only is enough;
- the ladder is ambiguous;
- the measurement burden is not worth it;
- MSI suppresses risk too slowly;
- MSI reduces friction and preserves useful variety;
- the effect is host-specific.

Negative and null results are first-class evidence.

### What to record

Use `research/experiments/MINIMUM-SUFFICIENT-INTERVENTION-RESULT-TEMPLATE.yaml` when convenient, but do not perform useless checks merely to fill fields.

At minimum record:

- ENA version/digest when available;
- host/runtime/model applicability when material;
- fixture/scenario and treatment;
- observed outcome;
- whether governance changed a decision;
- intervention layer(s) used;
- governance tax that was actually observable;
- whether useful solution variety was lost/preserved;
- material violation or prevented violation;
- evidence;
- UNKNOWNs and alternative explanations;
- what project decision this result should change.

### Independence disclosure

State whether the run is:

`INDEPENDENT_AGENT | SAME_DESIGNER_SELF_TEST | SAME_MODEL_DIFFERENT_SESSION | OTHER`

Do not present designer/self-test results as independent validation.

### Contribution

If you have authorized GitHub write/contribution capability, preserve the result as an independent contribution or experiment result and link Issue #11.

Do not directly modify `releases/current/` from this experiment.

If you cannot persist to GitHub, return the structured result to the maintainer for bridging.

### Final questions

After the run, answer:

> What was the **lowest intervention layer that was sufficient**, and what evidence supports that judgment?

Then answer the inverse:

> What evidence, if any, shows that a lower intervention would have been insufficient?

Finally answer:

> Did MSI produce a decision that Current ENA would not already have produced? If yes, identify the delta.

Issue: https://github.com/guytogay/evolution-native-agent-architecture/issues/11
