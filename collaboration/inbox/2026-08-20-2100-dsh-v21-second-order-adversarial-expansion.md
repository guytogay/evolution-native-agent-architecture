# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-20T21:00:00+08:00`
Target area: `research / machine-contract hardening (v0.3.2 V2.1)`
Relationship to existing work: `COUNTEREXAMPLE + NEW_EVIDENCE + IMPLEMENTATION_VARIANT`（attacks the V2 prototype at commit `d178ff3`）

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

V2.1 second-order adversarial expansion against the committed V2 hardening prototype (`research/prototypes/v2-machine-contract-hardening/`, commit `d178ff3`). `releases/current/` untouched; no promotion.

**The committed V2 prototype leaks all 11 second-order structural attacks** (0/11 blocked). Its "all-green" result covered only first-layer checks:

| # | Structural attack | V2 committed | V2.1 block |
|---|---|---|---|
| 1 | SUPPORTED → nonexistent support ref | LEAK | SUPPORT_REF_UNRESOLVABLE |
| 2 | completion → nonexistent obligation ref | LEAK | OBLIGATION_REF_UNRESOLVABLE |
| 3 | VERIFIED grade='GARBAGE' | LEAK | EVIDENCE_GRADE_INVALID |
| 3b | VERIFIED grade='E9' | LEAK | EVIDENCE_GRADE_INVALID |
| 4 | mandate expires_at past | LEAK | MANDATE_EXPIRED |
| 4b | mandate expires_at malformed | LEAK | MANDATE_DATE_UNPARSEABLE |
| 5 | recovery distinct refs, same root | LEAK | HISTORY_EVIDENCE_SHARED_ROOT |
| 6 | independence fabricated roots | LEAK | INDEPENDENCE_OVERCLAIMED |
| 7 | no registry supplied at all | LEAK | SUPPORT_REF_UNRESOLVABLE (fail-closed) |
| 8 | duplicate support_id, contradictory statuses | LEAK | DUPLICATE_REF_ID |
| 9 | resolved support, incompatible applicability | LEAK | TRANSFER_EVIDENCE_REQUIRED |

V2.1 minimal additions (registry+resolution fail-closed, grade enum E0..E5, date parse+currency, root-derivation check, root registry): **11/11 blocked, 7/7 positive preserved**. Portability: identical results on a fresh checkout (repo-relative paths; the V2 prototype's hardcoded absolute path is removed).

## Inference

- V2's all-green result was **false confidence at the second layer**: it proved first-layer structural checks, not resolvability/correctness of references.
- The smallest portable machine contract needs a **resolution layer** (refs must resolve, duplicates rejected, applicability checked on resolved artifacts) plus **enum/date/root validation**. Several of these are validator-only; a registry is the one new artifact surface.
- Residual trust boundary: registry/root/grade/mandate **truth** still requires an independent verifier ("claimed issuer != verified issuer"); hardening makes the boundary explicit, it does not eliminate it.

## ENA-VAL summary correction

Previous V2 report said "5/32". **Corrected: 5 material gap families involving 9 rule IDs: `013, 019, 022–025, 028, 030–031`.** Not restored by count; treated only as candidate historical protections whose present value must be demonstrated.

## Suggestion / question

1. Treat the V2 prototype as first-layer evidence only; do not base implementation acceptance on it.
2. If the contract surface is hardened in a future batched release, include a resolution/registry layer and enum/date/root validation (as in V2.1), and require a demonstrable independent-verification path for content-bearing fields before "schema PASS" can be read as semantic support.
3. Portability: prefer repo-relative prototype paths (as done here) so research can run on any checkout.

## Evidence references

- Prototype (research-only): `research/prototypes/v2-machine-contract-hardening/v2.1/` (`run_v21.py`, `fixtures_v21.py`, `results-v21.json`, `README.md`)
- Attacked target: `research/prototypes/v2-machine-contract-hardening/` (V2, commit `d178ff3`)
- Baseline toolchain: `releases/current/tools/validate_contracts.py` + schemas
- Prior: `collaboration/inbox/2026-08-20-2030-dsh-v2-machine-contract-hardening.md`
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.2 V2.1 Second-Order Adversarial Expansion - DSH-2026-08-20.md`

## Known limitations / unknowns

- Synthetic attacks; single host/session/model binding; no production workload.
- Registry/root truth remains self-declared without an independent verifier (documented residual).
- Whether the project accepts the resolution-layer direction or prefers another mechanism is UNKNOWN; advisory only.

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-20-OB-07"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any future 'v0.3.2 hardened contracts resolve references correctly' claim"
    evidence_refs: ["research/prototypes/v2-machine-contract-hardening/v2.1/results-v21.json"]
    resolution_reason: "Awaiting project decision; V2.1 is evidence+recommendation only."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the V2 leak finding (11/11) and the V2.1 closure (11/11 + 7/7).
- `NEEDS_EXPERIMENT` / `ACCEPT_FOR_IMPLEMENTATION` (project decision) for the resolution-layer direction.

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. V2.1 lives only under `research/prototypes/`; `releases/current/` untouched.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
