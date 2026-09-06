# 8. Release and Canonical-Lineage Discipline — v0.3.8

Status: `CURRENT / FIELD_VALIDATION / RELEASED`

## Core distinction

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
```

`same ena_version -> same effective content` remains mandatory. Corrections create successor identities rather than silent rewrites.

Current, however, should move when a better bounded successor has paid the evidence cost appropriate to its change.

## Release lanes

- **R0 Field patch/adoption surface** — machine/regression checks + exact release readback + rollback anchor; fresh independent validation may be post-release field evidence.
- **R1 Operational behavior change** — targeted adversarial/independent evidence when decision-material.
- **R2 Core semantic/high consequence** — heavy freeze + fresh independent falsification/reconciliation by default.

v0.3.8 was admitted through R0: no new Constitution IDs and no demonstrated core-contract semantic delta; v0.3.7 remains predecessor rollback/history.

## Rapid succession

```text
observe defect/opportunity
-> smallest useful successor
-> classify R0/R1/R2
-> proportional gates
-> move Current
-> preserve predecessor
-> field selection
```

Do not demand R2 evidence for an R0 change. Open unrelated research is not a release dependency.

GitHub is the current carrier of governed lineage, not a sovereign source of validity.

> **Release immutability protects truth; Current mobility protects evolution.**
