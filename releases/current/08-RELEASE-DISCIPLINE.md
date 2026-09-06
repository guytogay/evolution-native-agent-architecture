# 8. Release and Canonical-Lineage Discipline — v0.3.10

Status: `CURRENT / FIELD_VALIDATION / RELEASED`

## Core distinction

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
```

`same ena_version -> same effective content` remains mandatory. Corrections create successor identities rather than silent rewrites.

Current should move when a better bounded successor has paid the evidence cost appropriate to its change.

## Release lanes

- **R0 Field patch / adoption / projection / publication coherence** — machine/regression checks + exact readback + rollback anchor; fresh independent validation may be post-release field evidence.
- **R1 Operational behavior change** — targeted adversarial/independent evidence when decision-material.
- **R2 Core semantic/high consequence** — heavy freeze + fresh independent falsification/reconciliation by default.

v0.3.10 is an R0 successor to v0.3.9. It changes publication/release-identity narration and recurrence checks on stable cold surfaces; it does not add Constitution IDs or rewrite core machine semantics.

## R0 atomic transition

For a bounded R0 change, release projection and live project alignment may occur in one reviewed atomic PR when:

- predecessor identity remains recoverable;
- changed surfaces are explicitly bounded;
- Current machine/regression checks cover the changed class;
- root/adopter identity agrees with `CURRENT-BASELINE.yaml`;
- unrelated research is not treated as a blocker.

A second ceremonial post-promotion alignment PR is not required merely to repeat the same transition.

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

Do not demand R2 evidence for an R0 change. Do not hide a semantic/high-consequence change inside an R0 label.

> **Release immutability protects truth; Current mobility protects evolution.**
