# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-20T19:00:00+08:00`
Target area: `spec / evidence / research (machine-contract falsification)`
Relationship to existing work: `COUNTEREXAMPLE + NEW_EVIDENCE + SUGGESTION`

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

Six adversarial false-claim vectors were constructed and run against the real v0.3.2 release toolchain (`releases/current/` schemas + `validate_contracts.py`). All artifacts were disposable research inputs; no release file was modified.

| # | Claim vector | Attack | v0.3.2 machine result |
|---|---|---|---|
| 1 | "I know" | claim `status=SUPPORTED` with `support_relation_refs=[]` (zero support), underlying truth UNKNOWN | claim.v1 schema **PASS** |
| 2 | "I verified" | `evidence_refs=["schema-validation-PASS-log"]` used as verification evidence | capability-route-binding schema **PASS** |
| 3 | "I have authority" | post-restore clone + technically valid credential → `authority_envelope` claims approval/revocation rights; no mandate source / expiry / reconstitution evidence (ENA-CON-027 not machine-checked) | capability-route-binding schema **PASS** |
| 4 | "I completed" | WORKFLOW_COMPLETION claim passes; material obligation NOT_REQUIRED without `resolution_reason`; claim side has no reverse obligation linkage | obligation validator FAILS only when obligation submitted standalone; **claim side PASS** |
| 5 | "I recovered" | state restore SUCCESS + `history_continuity.status="PRESERVED"` self-asserted with zero preservation evidence (no delta capture, no evidence_refs) → claims STATE_AND_HISTORY | recovery validator **PASS** (`STATE_AND_HISTORY_RECOVERY_SUPPORTED`) |
| 6 | "These evidence items are independent" | 3 derived summaries with distinct `source_origins` strings all derived from one root log | support validator **PASS** (`SUPPORT_SCOPE_DIRECT_MATCH`) |

Control: the same independence attack with non-distinct origin strings (`ROOT-LOG` x3) is correctly caught (`INDEPENDENCE_OVERCLAIMED`); the laundering variant (distinct labels, one root) is not.

## Inference

- The prose semantics of v0.3.2 are strong and correct ("Schema PASS does not imply semantic support", "Propagation does not create independence", "credential validity != mandate validity", "Rollback state; preserve history"). None of these were falsified.
- The **machine-contract layer is the weak point**: 5/6 false-claim vectors pass the shipped schemas/validator. The common mechanism: status/enum values (SUPPORTED / PRESERVED / VERIFIED / VALIDATED) are self-asserted; validators check that the value is legal, not that the value is evidenced.
- Cross-artifact references are one-directional/conventional: obligation→claim exists, claim→obligation does not; credential and authority_envelope are unrelated; independence counts distinct origin strings, not root provenance.
- This creates false-confidence risk: the shipped validator + selftest (10/10 PASS) invites the reader to believe claims are checked, when in fact only structural shape is checked. This is precisely the misreading the release's own READ-ME warns against, but the tooling shape invites it.

## Suggestion / question

Minimal machine-contract tightening candidates (research-level; not an implementation request):

1. claim contract: require `status=SUPPORTED` → non-empty `support_relation_refs`; add an evidence-grade field (E0–E5 or equivalent) so "static structure PASS" cannot be presented as verification.
2. binding contract: add `mandate_source` / `expires_at` / `reconstitution_evidence_refs`; decouple `authority_envelope` from credential validity (machine-ize ENA-CON-027).
3. completion claim: add `required_obligation_refs` reverse linkage so the claim side can trigger obligation validation.
4. recovery contract: for `claim_scope=STATE_AND_HISTORY`, require `history_continuity.evidence_refs` non-empty and `post_checkpoint_occurrence_delta_captured=true`; do not accept the `PRESERVED` status word alone.
5. independence: add `root_provenance_ref` / `derivation_path` so independent counts are based on root sources, not flattened distinct strings.

## Evidence references

- v0.3.2 release toolchain: `releases/current/schemas/{claim,evidence-support-relation,recovery-history-transition,capability-route-binding,triggered-obligation}.v1.schema.json` + `releases/current/tools/validate_contracts.py` + `contract-fixtures.v1.json`
- Empirical run outputs (disposable, session log): 6 attacks + 2 controls; selftest 10/10 PASS confirmed first
- Full report: Obsidian `90 系统/审计/ENA v0.3.2 Reality Collision - Six False-Claim Vectors - DSH-2026-08-20.md`

## Known limitations / unknowns

- Single host, single model binding, single session; no production workload exercised.
- Attacks are synthetic but constructed from the release's own schema field sets; they were run against the actual shipped toolchain, not a mock.
- Whether some tightening is already planned in project-internal research/evidence is UNKNOWN to me (private repo; only `releases/current/` was read).

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-20-OB-03"
    rule_ref: "ENA-CAP-065 (claim-evidence support relation) / ENA-CAP-066 (obligation closure) / 5.3 (recovery != history)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'v0.3.2 machine contracts resist false claims' claim"
    evidence_refs: []
    resolution_reason: "Awaiting project decision on whether to tighten claim/binding/recovery/independence machine contracts."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the six falsification results (counterexamples are evidence, not defects-by-assertion).
- `NEEDS_EXPERIMENT` or `ACCEPT_FOR_IMPLEMENTATION` (project decision) for the five tightening candidates.

## Authority / implementation note

- `advice only`. No release modification, no Mainline change, no promotion request. Any tightening requires project/user authority and, per release discipline, batched rather than micro-versioned.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
