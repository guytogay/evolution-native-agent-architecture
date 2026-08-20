# 7. Beta Adoption and Field Validation

`v0.3.1-BETA.1` is one complete adoption baseline, not a composition of old releases.

Beta status means:

- real bounded adoption is intended;
- Shadow observation and Canary enforcement are allowed/expected where authorized;
- evidence and counterexamples should be collected;
- the baseline is not yet a Mainline or universal-validation claim.

All field feedback should identify, where possible:

- `ena_version: v0.3.1-BETA.1`;
- baseline/package digest if available;
- relevant Host/runtime/model/tool/route/configuration identity;
- relevant Active Governance Set states;
- task/event and expected behavior;
- observed outcome;
- whether ENA prevented failure, changed a decision, added friction, failed to help, or created a new failure mode;
- evidence references;
- uncertainty and alternative explanations.

Feedback from different hosts is comparable only within its observed applicability envelope. Field recurrence is evidence, not automatic universal truth.

The project should prefer:

`cheap contradiction check -> synthetic/HAR falsification -> disposable experiment -> Shadow production -> Canary enforcement -> broader production -> independent-host replication when decision-critical`

Do not require every mechanism to reach maximal validation before bounded production. Do not run an expensive experiment unless its possible outcomes can change a decision.

> **Use the cheapest evidence that can honestly support the decision.**
>
> **Cheap falsification before expensive validation.**
>
> **Batch variation; concentrate expensive selection.**
>
> **Production before perfection; not production without evidence.**

---
