# Persistent Project Contribution

Project: Evolution-Native Agent Architecture (ENA)
Contribution status: `UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`
Date/time: `2026-08-21T12:10:00+08:00`
Target area: `research / residual closure (v0.3.2 V2.4.1)`
Relationship to existing work: `RESIDUAL_CLOSURE + SUCCESSOR_CANDIDATE`（closes WorkBuddy F1/F2 residuals from PR #30 on the frozen V2.4 successor 47e0e1b；frozen candidates and releases/current/ UNTOUCHED；V2.x research loop terminates）

## Participant provenance

```yaml
participant:
  kind: "DeepSeek Harness"
  runtime_or_model: "deepseek-v4-flash via DeepSeek Harness Web GUI (DSH 0.x local runtime)"
  session_or_run_ref: "session-3b3cd6d7-9ccc-4523-8203-41be2c8b32fb"
  access_surfaces:
    github: "WRITE (PR-based; main requires PR per repo branch protection)"
    google_drive: "NONE"
    other: ["Anytype MCP (knowledge base write)"]
  role_this_contribution: "CONTRIBUTOR / EXPERIMENTER / CANDIDATE_AUTHOR (frozen; NOT independent revalidator)"
```

These fields describe provenance and technical capability, **not project authority**.

Tool access does not authorize Mainline modification, release, deployment, remediation, or scope expansion.

## Observed facts

V2.4.1 is a narrowly scoped convergence step following WorkBuddy independent validation of the frozen V2.4 successor (PR #30, verdict `INDEPENDENT_VALIDATION_SUPPORTED_WITH_RESIDUALS`).

**F1 (primary) — dict-key vs inner-id identity ambiguity: reproduced and closed.**
- Reproduced against frozen 47e0e1b (`reproduce_f1.py` → `reproduction-f1.json`): `IND-02E/O/R/A` silent false BLOCK; `IND-02E-rev` identity confusion (OK).
- Smallest coherent correction (R12, ONE consistent identity rule for ALL registry kinds): dict key authoritative; explicit inner id must equal the key, else `REGISTRY_MALFORMED` (never guess); missing inner id backfilled from the key. Applies uniformly to support_registry, support_relations, evidence_registry, root_registry, obligations, authority_registry.
- After fix: `IND-02E/O/R/A` → BLOCK REGISTRY_MALFORMED (explicit verdict); `IND-02E-rev` → BLOCK (confusion eliminated); key==id and backfill controls all OK.

**F2 (secondary) — OPEN obligation status reaching OK: clarified and closed as defense-in-depth.**
- Shipped `triggered-obligation.v1.schema.json` status enum has no OPEN. Treated as integration-precondition / defense-in-depth (per Host instruction): schema-valid-input precondition machine-enforced at the semantic boundary — status outside the shipped vocabulary → `OBLIGATION_STATUS_OUTSIDE_VOCABULARY`. Vocabulary NOT expanded.

**Regression (one implementation, `successor_contract_v241.py`):**

| Corpus | Count | Result |
|---|---|---|
| Frozen V2.4 (unchanged) | 98 | **98/98 preserved (ZERO verdict flips)** |
| WorkBuddy probes IND-01..17 | 25 | **25/25 matched; oracle vs wb_expect 25/25 consistent** |
| F1/F2 closure controls | 25 | **25/25** |
| TOTAL | 148 | **UNEXPECTED_VERDICTS: 0** (BLOCK 82 / OK 60 / UNKNOWN 6); exceptions 0 |

**Cost:** +17 lines / +1 explicit code vs frozen V2.4; stdlib only; no schema change; no vocabulary expansion.

**Freeze:** successor code ref `daacab1f042c38f3856ef4d0366febd1b5e47600`; freeze record `b3d1698` (FREEZE-MANIFEST-V241.md: blob SHA-256, 148-fixture manifest, cost table, trust-boundary updates). Landed on main via PR #31 (merge `ae0603b`) per the repo's PR-required branch protection.

## Inference

1. **The independently discovered residual is closed without reopening prior protections** — 98/98 frozen V2.4 verdicts preserved, all 25 WorkBuddy probes satisfied, 25 new closure controls pass.
2. **Smallest coherent correction**: one identity rule applied uniformly (not per-registry special cases), one vocabulary gate (no schema/vocabulary expansion). Cost +17 lines, +1 code.
3. **The V2.x research loop terminates here.** Success is closing the residual, then stopping and handing the result toward implementation — not more expansion.

## Suggestion / question

1. **Targeted revalidation by the prior F1 falsifier (WorkBuddy validator)** is the intended next validation step — closed-scope recheck of F1/F2 closure, not another open-ended adversarial expansion. Check out `daacab1` (or freeze tip `b3d1698`/merge `ae0603b`), run `python research/prototypes/v2-machine-contract-hardening/v2.4.1/run_v241.py`; success = `UNEXPECTED_VERDICTS: 0`, exit 0.
2. On revalidation, hand the result toward implementation — adoption/promotion decisions remain Host authority.
3. Do NOT promote or adopt based on this contribution alone.

## Evidence references

- Prototype (research-only): `research/prototypes/v2-machine-contract-hardening/v2.4.1/` (`successor_contract_v241.py`, `acceptance_semantics_v241.py`, `wb_fixtures.py`, `f1_controls.py`, `run_v241.py`, `reproduce_f1.py`, `reproduction-f1.json`, `results-v241.json`, `FREEZE-MANIFEST-V241.md`, `freeze_hashes_v241.py`)
- Prior candidates (UNCHANGED): `.../v2.4/` @ `47e0e1b`; `.../v2.2/cumulative_contract.py` @ `8eb5a9a`
- WorkBuddy validation (reconciled): `collaboration/inbox/2026-08-21-ena-v24-independent-validation-wb.md` (PR #30, merged `371e983`)
- Full report (local): Obsidian `90 系统/审计/ENA v0.3.2 V2.4.1 Residual Closure - DSH-2026-08-21.md`

## Known limitations / unknowns

- Synthetic fixtures; single host/session/model binding; no production workload.
- Registry/grade/mandate content-truth remains self-declared (V2.4 trust boundaries #3/#4); evidence-existence posture (boundary #1) and mandate vocabulary (boundary #2) unchanged.
- The WB report prose says "26 cases"; the executable probe file contains 25 `add()` cases (table also lists 25); 25 is the recorded count.
- The successor is NOT independently validated; targeted revalidation by WB is pending.
- Successor tested locally on Python 3.14 (Windows); language level identical to frozen candidates (3.8-compatible surface; independently tested window 3.8.18/3.12.14/3.13.12).

## Triggered follow-up obligations

```yaml
triggered_obligations:
  - obligation_id: "DSH-2026-08-21-OB-03"
    rule_ref: "ENA-CAP-065/066 + 08-RELEASE-DISCIPLINE (batching)"
    applicability: "APPLICABLE"
    materiality: "MATERIAL_TO_COMPLETION"
    status: "PENDING"
    required_before_claim: "any 'V2.x hardened contract ready for implementation consideration' claim"
    evidence_refs: ["research/prototypes/v2-machine-contract-hardening/v2.4.1/results-v241.json",
                    "research/prototypes/v2-machine-contract-hardening/v2.4.1/FREEZE-MANIFEST-V241.md"]
    resolution_reason: "Awaiting targeted revalidation by the prior F1 falsifier (WB); V2.x research loop stopped."
```

## Requested reconciliation

- `ACCEPT_AS_EVIDENCE` of the F1/F2 closure and the zero-unexpected 148-fixture replay.
- `TARGETED_REVALIDATION` by the prior F1 falsifier (WorkBuddy) of the frozen successor (candidate author excluded by lineage).
- `HOST_DECISION` on handing the result toward implementation (no promotion implied).

## Authority / implementation note

- `advice only`. No release modification; no Mainline change; no promotion request. V2.4.1 lives only under `research/prototypes/`; `releases/current/` untouched; frozen candidates `47e0e1b`/`8eb5a9a` untouched; no v0.2.12 / v0.3.3 created.

## Notes

Do not present this contribution as accepted ENA truth merely because it is committed to GitHub.

Preserve the original contribution even after reconciliation.
