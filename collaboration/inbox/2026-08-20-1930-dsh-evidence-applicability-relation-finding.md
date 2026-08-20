# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-20T19:30:00+08:00`
Target area: `research / evidence (evidence-applicability prototype falsification)`
Relationship to existing work: `COUNTEREXAMPLE + DEEPER_BOUNDARY_CONDITION`（relates to `research/adversarial-replay/plans/EVIDENCE-APPLICABILITY-AUDIT.md` and HAR-006/HAR-010）

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
  role_this_contribution: "CONTRIBUTOR / EXPERIMENTER / REVIEW_ONLY"
```

These fields describe provenance and technical capability, **not project authority**.

Tool access does not authorize Mainline modification, release, deployment, remediation, or scope expansion.

## Observed facts

Executed the research experiment defined in `research/experiments/EVIDENCE-APPLICABILITY-DSH-EXPERIMENT.md` against the `evidence-applicability-envelope.schema.json` prototype. Empirical results (all run against the actual prototype schema):

1. **6/6 adversarial boundary-transfer envelopes (SUBJECT / INSTANCE / CONFIGURATION_STATE / EPOCH / TIME / ENVIRONMENT) PASS the prototype schema.** The prototype does not detect any of them; detection requires domain reasoning about the claim side.
2. **Claim-side expansion is structurally invisible to the prototype.** Adding a `claim_attempt` field to an attack artifact fails the schema with `Additional properties are not allowed` — the prototype cannot even model the combination "evidence + the claim that misuses it".
3. **False-confidence vector proven**: a benign envelope and an attack-shaped envelope produce identical schema results (PASS/PASS); `transfer_status: NOT_VALIDATED` is declarative, not enforced.
4. **Overconstraint vector proven**: per-property transfer is unrepresentable (a single `transfer_status` applies to the whole `scope` list); a reasonable field `equivalence_proof_ref` is rejected by `additionalProperties: false` on transfer_constraints items.
5. Legitimate-transfer tests: validated transfer (with equivalence evidence refs) PASSES; but equivalence evidence has no first-class recursive model, and cross-epoch invariance cannot be expressed per-property.

## Inference

- **Evidence Applicability belongs on the Evidence → Claim support relation, not on evidence items alone and not on claims alone.** The prototype places the envelope on evidence only; the HAR-006/HAR-010 failure shapes both occur at claim-side expansion, which the prototype structurally cannot see.
- **The prototype is insufficient as-is** for the clarification path: it makes the boundary legible but not enforceable or claim-relative.
- This is consistent with v0.3.2's own 5.1 (Claim ↔ Evidence) and CAP-065, which already move toward a support-relation model — but the v0.3.2 claim/evidence schemas still lack the per-property/per-boundary and root-provenance granularity identified here.

## Suggestion / question

1. When the claim–evidence link contract is formalized, treat applicability as a **relation artifact** (evidence declares observed envelope; claim declares claimed scope; the relation validates claimed ⊆ observed or an evidenced transfer), not as an evidence-only field.
2. Add per-(boundary × scope) transfer semantics so "valid for property P1, not P2" is expressible.
3. Add `root_provenance_ref` / `derivation_path` to independence accounting (matches the six-false-claim contribution's item 5).

## Evidence references

- `research/experiments/EVIDENCE-APPLICABILITY-DSH-EXPERIMENT.md` (experiment plan)
- `research/prototypes/evidence-applicability-envelope.schema.json` + examples
- Empirical outputs: 6 attacks + 4 legitimate-transfer tests + controls (session log; disposable artifacts)
- Full report: Obsidian `90 系统/审计/ENA Evidence Applicability Contract Falsification - DSH-2026-08-20.md`

## Known limitations / unknowns

- Single host, synthetic attacks; two real replay cases (HAR-006, HAR-010) anchor the boundary structure.
- The prototype is explicitly research-only; this contribution does not claim the research is complete or that a specific schema shape is the only correct one.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-20-OB-05"
    rule_ref: "ENA-CAP-065 (claim-evidence support relation) / research experiment plan"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'applicability prototype is sufficient' claim"
    evidence_refs: []
    resolution_reason: "Awaiting project decision on relation-first applicability modeling."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the prototype insufficiency and the support-relation placement finding.
- `NEEDS_EXPERIMENT` / `ACCEPT_FOR_IMPLEMENTATION` (project decision) for the relation-first modeling direction.

## Authority / implementation note

- `advice only`. No research artifact modified; no release change; no promotion request.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
