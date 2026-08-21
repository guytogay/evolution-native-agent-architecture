# 7. Adoption and Field Validation

`v0.3.2` is one complete adoption baseline, not a composition of old releases.

Release status: `FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`.

Version identity and maturity are separate: `v0.3.2` names the immutable adoption content; `FIELD_VALIDATION` describes the current evidence posture.

Real bounded adoption is intended. Shadow observation and Canary enforcement are allowed/expected where authorized. The baseline is not a Mainline or universal-validation claim.

## Adoption profiles

Choose the lightest profile that honestly matches consequence:

- `LITE` — bounded low-consequence work; minimum read/representation path in `LITE-ADOPTION-INSTRUCTION.md`.
- `STANDARD` — persistent/project-scale adoption where broader positioning, governance-state representation, or cross-task continuity adds value.
- `HIGH_ASSURANCE` — high-consequence, weak-recovery, sensitive, externality-heavy, or governance/meta work where stronger evidence/enforcement is justified.
- `CUSTOM` — declared local projection with explicit applicability and residual limitations; it does not create a different Constitution.

Profile choice is not a badge. Escalate/de-escalate as task consequence changes. Low-consequence work should not inherit high-assurance ceremony by habit.

## Field reports

All field feedback should identify, where possible and decision-relevant:

- `ena_version: v0.3.2`;
- exact source/package digest or release evidence when available;
- selected adoption profile;
- relevant Host/runtime/model/tool/route/configuration identity;
- relevant Active Governance Set states;
- task/event and expected behavior;
- observed outcome;
- whether ENA prevented failure, changed a decision, added friction, failed to help, or created a new failure mode;
- evidence references and source/provenance independence where material;
- uncertainty and alternative explanations;
- authority/effect context for consequential actions.

Feedback from different hosts is comparable only within its observed applicability envelope. Field recurrence is evidence, not automatic universal truth. Repeated derivative reports are not automatically independent replication.

The project should prefer:

`cheap contradiction check -> synthetic/HAR falsification -> disposable experiment -> Shadow production -> Canary enforcement -> broader production -> independent-host replication when decision-critical`

Do not require every mechanism to reach maximal validation before bounded production. Do not run an expensive experiment unless its possible outcomes can change a decision.

For release/adoption comparisons, distinguish final-state correctness from transition safety: individually valid old/new states can still interact badly during mixed rollout. Version/digest visibility and compatibility narrowing may be required where material.

> **Use the cheapest evidence that can honestly support the decision.**
>
> **Cheap falsification before expensive validation.**
>
> **Batch variation; concentrate expensive selection.**
>
> **Production before perfection; not production without evidence.**

---
