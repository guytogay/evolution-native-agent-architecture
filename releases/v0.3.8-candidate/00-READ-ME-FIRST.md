# ENA v0.3.8-candidate.0 — Read Me First

Status: **NOT_CURRENT / NOT_FROZEN / NOT_RELEASED / ADOPTION-SURFACE SUCCESSOR**

The released adopter-facing baseline remains `v0.3.7 / CURRENT / FIELD_VALIDATION` under `../current/`.

This directory is a successor candidate. Do not treat branch existence or this self-description as promotion.

## If you are evaluating whether to use ENA

Start with only these surfaces:

1. `ADOPTER-QUICKSTART.md` — what ENA is, what you actually need, and what you do **not** need to read;
2. `RUNTIME-ADOPTION-KERNEL.md` — compact Agent-facing semantic/cue surface;
3. `operational/CUE-INDEX.md` — route an ordinary problem to a relevant HOW only when needed;
4. `ENFORCEMENT-MAP.yaml` — distinguish model guidance, machine guards, external controls, and field-evidence claims;
5. `language-projections/semantic-fixtures.v3.yaml` — decision-semantic conformance cases;
6. `tools/` — executable validators/reference tooling where the property is actually machine-guarded.

You do **not** need to read project research, handoffs, adjudications, candidate history, or every optional reference to evaluate ordinary adoption.

## Runtime shape

```text
compact hot semantics
-> ordinary cue
-> retrieve one relevant HOW
-> use the lightest applicable Host mechanism
-> act / WAIT / UNKNOWN / REFUSE / NOT_APPLICABLE
-> observe reality
```

Do not permanently load the full HOW/reference library merely to claim ENA adoption.

## What ENA is not

ENA is not:

- one giant prompt;
- a requirement to implement every bundled reference;
- a claim that prose alone creates security;
- a private vocabulary that every Host must reproduce literally;
- a guarantee that machine validation proves external truth;
- a requirement that adopters reconstruct ENA's research history before useful work.

Equivalent Host-native mechanisms are legitimate when they preserve the required property and boundary.

## Enforcement honesty

Every important protection should be read with its enforcement class.

```text
MODEL_CUE
MACHINE_GUARD
EXTERNAL_CONTROL_REQUIRED
FIELD_EVIDENCE_REQUIRED
```

A `MODEL_CUE` is not silently upgraded into a hard control. A machine validator is not silently upgraded into proof about the outside world.

See `ENFORCEMENT-MAP.yaml`.

## Cold material

Use deeper files only when the current decision needs them:

- `operational/HOW-MAP.md` — practical branches;
- `operational/REFERENCE-INDEX.yaml` — exact optional references/patterns;
- `references/` — optional reusable reference implementations;
- `01-CONSTITUTION.md` and other semantic chapters — exact normative/detail surface;
- lineage/release material — only when identity/history actually changes the decision.

## Candidate proof boundary

Candidate.0 begins from an exact copy of the released v0.3.7 Current subtree and is being changed only on the successor surface.

Before it can become Current it still requires bounded author checks, freeze, independent falsification/validation, reconciliation, and an explicit release decision.

```text
CANDIDATE_EXISTS != CURRENT
MACHINE_PASS != EXTERNAL_TRUTH
TRANSLATED != BEHAVIORALLY_EQUIVALENT
SIMPLER_SURFACE != WEAKER_SEMANTICS
```

> **The adopter should need less project history, not less protection.**
