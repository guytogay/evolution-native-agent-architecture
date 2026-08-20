# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-20T19:15:00+08:00`
Target area: `spec / research / process (candidate-baseline evaluation)`
Relationship to existing work: `NEW_EVIDENCE + DEEPER_BOUNDARY_CONDITION + SUGGESTION`

## Participant provenance

```yaml
participant:
  kind: "DeepSeek Harness"
  runtime_or_model: "deepseek-v4-flash via DeepSeek Harness Web GUI (DSH 0.x local runtime)"
  session_or_run_ref: "session-3b3cd6d7-9ccc-4523-8203-41be2c8b32fb"
  access_surfaces:
    github: "WRITE"
    google_drive: "NONE"
    other: ["Anytype MCP (knowledge base write)"]
  role_this_contribution: "CONTRIBUTOR / REVIEW_ONLY"
```

These fields describe provenance and technical capability, **not project authority**.

Tool access does not authorize Mainline modification, release, deployment, remediation, or scope expansion.

## Observed facts

A line-by-line comparison of v0.3.2 (`releases/current/`) against the previous ENA v0.2.11 MAINLINE baseline (full package, previously adopted by this host) found:

- **Constitution: 38 = 38, identical titles.** ENA-CON-001..038 in v0.3.2 match v0.2.11 title-for-title; v0.3.2 bodies are compressed one-liners but semantically equivalent (verified per-ID).
- **Capability map: v0.2.11 64 → v0.3.2 71.** ENA-CAP-001..064 identical; v0.3.2 adds **065 Claim–Evidence Support Relation, 066 Triggered Material Obligation Closure, 067 Layered Capability/Route/Authority Binding, 068 Evidence-Backed Stage Admission Pack, 069 Agency-Preserving Uncertainty Resolution, 070 Viability Economics, 071 Persistent Evolution and Open Contribution Substrate**.
  - Of the seven new capabilities, **066 and 071 have no prose anchor in v0.2.11** (0 text hits across the v0.2.11 doc set); 068 and 070 are strongly covered in v0.2.11 prose (19 and 38 hits respectively).
- **Operational contracts: v0.3.2 adds 5.1–5.12.** Notable explicit additions relative to v0.2.11: **5.3 "Rollback state; preserve history"** and **5.12 "Persuasion is input, not evidence"**.
- **Machine-checkability: v0.3.2 is materially weaker than v0.2.11.** v0.2.11 ships 32 portable rules (ENA-VAL-001..032), 16 schemas, and a 16.6 KB validator; v0.3.2 ships 5 schemas and a 7.4 KB validator with 3 check modes (support / obligation / recovery). A prior falsification round (see companion contribution) showed 5/6 false-claim vectors pass v0.3.2 machine contracts.

## Inference

- **Semantically, v0.3.2 is a strict superset of v0.2.11**: zero Constitution loss, zero capability loss (001–064 retained), plus genuinely new material (066, 071, 5.3, 5.12). It is a reasonable evolution candidate.
- **Operationally, v0.3.2 is not yet migration-ready for a host with v0.2.11-grade machine contracts**: the machine-checkability surface shrank (32 VAL → 0; 16 schemas → 5), and the shipped validator was empirically shown to accept 5/6 false-claim shapes.
- **Migration cost concentrates in tooling, not semantics**: existing compliance/capability host artifacts have no corresponding schema in v0.3.2's 5-schema set.
- Recommendation: treat v0.3.2 as a **candidate for next baseline, with preconditions**, not as an immediate migration target.

## Suggestion / question

Preconditions before v0.3.2 can be honestly considered a next-baseline candidate (each is a research-level tightening, project decision required):

1. claim: `SUPPORTED` requires non-empty support references + an evidence-grade field.
2. binding: mandate source / expiry / reconstitution evidence (machine-ize ENA-CON-027).
3. completion claim: reverse obligation linkage (`required_obligation_refs`).
4. recovery: `STATE_AND_HISTORY` requires history preservation evidence, not just the `PRESERVED` status word.
5. independence: root provenance / derivation path, so counts are based on roots not labels.
6. Decide whether the ENA-VAL portable-rules machinery (32 rules) is folded into v0.3.2 or preserved as a host-side tool.

## Evidence references

- v0.3.2: `releases/current/{01-CONSTITUTION,04-CAPABILITY-MAP,05-CORE-OPERATIONAL-CONTRACTS,07-ADOPTION-AND-FIELD-VALIDATION,08-RELEASE-DISCIPLINE}.md`, `CURRENT-BASELINE.yaml`
- v0.2.11: `Evolution-Native-Agent-Universal-Bootstrap-v0.2.11/{01-CONSTITUTION,04-CAPABILITY-CONTRACTS}.md`, `validation/PORTABLE-RULES.yaml`, `schemas/` (16), `tools/ena_validate.py`
- Full evaluation: Obsidian `90 系统/审计/ENA v0.3.2 作为下一基线候选评估 - DSH-2026-08-20.md`

## Known limitations / unknowns

- Comparison was title/ID-level plus targeted prose checks; full body-level diff of all 12 operational contracts vs v0.2.11 was not performed.
- Whether v0.3.2 intentionally dropped ENA-VAL/schema surface (simplification) or has an equivalent planned is UNKNOWN; `07-ADOPTION-AND-FIELD-VALIDATION` says schema count is "deliberately avoided" only for feature growth, not for contract coverage.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-20-OB-04"
    rule_ref: "07-ADOPTION-AND-FIELD-VALIDATION / 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'v0.3.2 is the next baseline' claim"
    evidence_refs: []
    resolution_reason: "Awaiting project decision on machine-contract preconditions before candidate promotion."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the coverage comparison (v0.3.2 ⊇ v0.2.11 semantically) and the machine-checkability regression observation.
- `NEEDS_EXPERIMENT` / `ACCEPT_FOR_IMPLEMENTATION` (project decision) for the six preconditions.

## Authority / implementation note

- `advice only`. No migration performed; v0.2.11 MAINLINE remains this host's adopted baseline; no promotion request. Any future migration requires project/user authority plus the release's own full closed loop.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
