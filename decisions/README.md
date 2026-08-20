# ENA Decision Records

Status: `PROJECT_DECISION_LINEAGE`

This directory records durable project/process/architecture decisions that should remain understandable after the participant who made them is gone.

A decision record is appropriate when a change materially affects:

- project information architecture;
- collaboration semantics;
- canonical-state interpretation;
- release/promotion process;
- persistent surface roles;
- authority or governance process;
- durable engineering architecture.

Decision records explain **what was decided, why, under what authority/evidence, and what alternatives were rejected**.

They do not rewrite source evidence, and they do not create authority merely because they are committed.

Use `ADR-TEMPLATE.md` for new decisions.

Naming:

`ADR-###-short-kebab-topic.md`

Keep superseded decisions in history and link the superseding ADR instead of deleting the old record.
