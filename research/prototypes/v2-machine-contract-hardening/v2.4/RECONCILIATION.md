# V2.4 Phase 1 — Independent-Finding Reconciliation (I01–I16 + CF-1..3 + oracle)

> **Status: RESEARCH — UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED.**
> Frozen candidate `8eb5a9afa4c560645b4c50dc24af7874ed54a4f2` and
> `releases/current/` were NOT modified. The successor lives only under
> `research/prototypes/v2-machine-contract-hardening/v2.4/`.
>
> Method: every finding was **independently reproduced** by DSH against the
> frozen candidate at the exact ref (detached worktree; `reproduce_v23.py` →
> `reproduction-v23.json`), NOT taken on faith from the validator's table.
> Classifications are grounded in the reproduction AND the shipped baseline
> source (`releases/current/tools/validate_contracts.py`), not in the
> validator's identity. The validator's remediation suggestions were treated as
> hypotheses to confirm, not as authority.

## Classification legend

- **CONFIRMED_MATERIAL_DEFECT** — reproduced; real semantic/robustness defect vs the candidate's stated machine-contract purpose.
- **CONFIRMED_BUT_EXPECTED_BOUNDARY** — reproduced; already documented as a residual trust boundary.
- **SEMANTIC_DISAGREEMENT** — reproduced; DSH disagrees (in whole or in part) with the independent expectation.
- **NOT_REPRODUCED** — could not reproduce.
- **NEEDS_EXPERIMENT** — genuine semantic question; needs more evidence; treated separately.

## Reproduction summary (DSH's own run at frozen ref 8eb5a9a)

| Finding | Independent expect | Frozen actual (DSH reproduction) | Reproduction |
|---|---|---|---|
| I01–I05 | BLOCK | **OK** | reproduced (false OK) |
| I06, I07 | OK | **BLOCK** | reproduced (false BLOCK) |
| I08–I13 | BLOCK | **OK** | reproduced (false OK) |
| I14 | UNKNOWN_OR_BLOCK | **OK** | reproduced (overstate) |
| I15, I16 | NO_EXCEPTION | **EXCEPTION** (AttributeError) | reproduced (exceptions) |
| O01–O04 | — | mixed | reproduced (oracle defects + shared blind spot) |

---

## Finding-by-finding reconciliation

### I01 — support target mismatch
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK).
- Actual frozen verdict: `OK`. Independently expected: `BLOCK`.
- ENA semantics: the **shipped baseline already enforces support→claim binding**
  (`validate_contracts.py:48-49`, `CLAIM_REF_MISMATCH`). The frozen candidate's
  registry path dropped it. ENA-CON-029 (claimed issuer ≠ verified issuer).
- Category: **false OK** (borrowed support endorses a claim it does not target).
- Smallest correction: resolved support must bind back to the current claim
  (`claim_ref == claim_id` → else `SUPPORT_TARGET_MISMATCH`) — R2.
- Governance/runtime cost: trivial (one comparison per resolved support).
- Positive control (overconstraint guard): V24-P01 (full-stack, claim_ref matches).

### I02 — recovery, present-but-empty evidence registry
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK).
- Actual frozen verdict: `OK` (raw-ref fallback → distinct roots). Independently expected: `BLOCK`.
- ENA semantics: V2.1/V2.2 "missing registries must NOT silently degrade into
  trusting raw strings"; recovery root derivation must be registry-backed.
  Present-but-incomplete registry = broken evidence, not verified provenance.
- Category: **false OK**; also the semantic inversion the validator identified
  (absent→UNKNOWN is fine; present-but-missing→OK is not defensible).
- Smallest correction: when the evidence registry is SUPPLIED, referenced
  evidence must resolve (missing → `EVIDENCE_REF_UNRESOLVABLE`); when absent →
  `UNKNOWN` (P7 preserved) — R3.
- Governance/runtime cost: low (registry key check per evidence ref).
- Positive control: V24-P03 (full recovery, resolvable distinct-root evidence).

### I03 — independence, present-but-empty root registry
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK). Same family as I02,
  on the root path.
- Actual frozen verdict: `OK` (raw-root fallback). Independently expected: `BLOCK`.
- ENA semantics: independence counted on registry-verified origins, not labels.
- Category: **false OK** (claim of N independent origins rests on unregistered roots).
- Smallest correction: present root registry must resolve each root → missing →
  `ROOT_REF_UNRESOLVABLE`; absent → `UNKNOWN` (P9 preserved) — R3.
- Cost: low. Positive control: V24-P04 (+ V24-A05 malformed negative).

### I04 — model_binding applicability mismatch
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK; applicability regression, CF-3).
- Actual frozen verdict: `OK`. Independently expected: `BLOCK`.
- ENA semantics: baseline `SCOPE_KEYS` = host, runtime_instance, model_binding,
  route, configuration, epoch, time_interval, task_scope
  (`validate_contracts.py:16`). The frozen registry path checked only
  host/runtime_instance/epoch/configuration/environment — it **dropped
  model_binding, route, time_interval, task_scope**.
- Category: **false OK** (claimed envelope not inside observed envelope).
- Smallest correction: route resolved support through the shipped
  `validate_support` (full 8-dimension envelope) — R4.
- Cost: low (reuse of shipped baseline). Positive control: V24-P06 (all 8 dims).

### I05 — claimed runtime, missing observed runtime
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK; CF-3).
- Actual frozen verdict: `OK` (both-present-only mismatch). Independently expected: `BLOCK`.
- ENA semantics: baseline `_scope_mismatches` treats a claimed material
  dimension with no observed value as a mismatch (`validate_contracts.py:39-43`).
- Category: **false OK** (missing observation silently treated as direct match).
- Smallest correction: same as I04 (baseline envelope; missing observed = mismatch) — R4.
- Cost: low. Positive control: V24-P06.

### I06 — legitimate top-level support object
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false BLOCK; composition failure CF-1).
- Actual frozen verdict: `BLOCK` (`SUPPORT_REF_UNRESOLVABLE`). Independently expected: `OK`.
- ENA semantics: the shipped contract evaluates `(claim, support)` pairs
  directly (contract-fixtures mode=support); the top-level support object IS the
  resolvable artifact. Two individually-valid representations disagree in the
  frozen candidate (representation disagreement).
- Category: **false BLOCK** (legitimate composed case rejected).
- Smallest correction: canonical support sources = top-level `support`
  (dict/list) + `support_registry` + `support_relations`, unified — R6.
- Cost: low (one collection function). 
- Positive control: V24-P07; **negative guard (no I01 reopening)**: V24-A01
  (top-level support with wrong claim_ref still BLOCKs).

### I07 — unrelated open obligation poisons narrower claim
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false BLOCK; composition failure CF-2).
- Actual frozen verdict: `BLOCK` (global `validate_obligation` on every
  supplied obligation). Independently expected: `OK`.
- ENA semantics: obligations gate claims via `required_before_claim_refs` and
  via the completion claim's own `required_obligation_refs`; the core
  explicitly permits narrower truthful completion. Global evaluation of
  unrelated obligations is a composition dependence on payload contents.
- Category: **false BLOCK**.
- Smallest correction: claim-aware obligation scoping — only obligations
  referenced by the claim or bound to it are evaluated — R7.
- Cost: low. Positive control: V24-P08; **negative guards**: V24-A02 (the
  claim's OWN open material obligation still BLOCKs — S3 preserved),
  V24-A03 (an obligation explicitly bound to this claim gates it).

### I08 — duplicate support ID, same status, ambiguous
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK).
- Actual frozen verdict: `OK` (first entry wins). Independently expected: `BLOCK`.
- ENA semantics: V2.1 explicit duplicate/ambiguity rejection; ambiguity is not
  status-token difference — two same-status entries with different
  claim_ref/evidence/scope are still ambiguous; resolution order must not
  decide truth.
- Category: **false OK** (order-dependent truth).
- Smallest correction: duplicate IDs rejected when content differs
  (fingerprint); byte-identical entries deduped — R5.
- Cost: low. Positive control: V24-P09 (unique IDs) + V24-P12 (identical dups
  dedupe); negative: V24-A08 (same status, different scope → BLOCK).

### I09 — support evidence ref unresolvable
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK).
- Actual frozen verdict: `OK` (non-empty evidence refs accepted). Independently expected: `BLOCK`.
- ENA semantics: V2.1 `SUPPORT_WITHOUT_EVIDENCE` requires resolved support to
  carry evidence; a non-empty string is not resolvable evidence.
- Category: **false OK**.
- Smallest correction: when the evidence registry is supplied, support evidence
  refs must resolve (missing → `EVIDENCE_REF_UNRESOLVABLE`) — R3.
- Cost: low. Positive control: V24-P01; negative: V24-A10 (missing from
  list-form present registry).

### I10 — verified capability, E5 ref nonexistent
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK).
- Actual frozen verdict: `OK`. Independently expected: `BLOCK`.
- ENA semantics: valid grade token ≠ resolvable evidence ≠ verified capability.
  This is a NEW gap beyond the documented grade-self-declared boundary (freeze
  boundary 2): evidence EXISTENCE is not enforced on this path.
- Category: **false OK**; trust-boundary extension documented.
- Smallest correction: capability evidence refs resolve when the evidence
  registry is supplied — R3.
- Cost: low. Positive control: V24-P02; negative: V24-A07.

### I11 — SELF_ASSERTED mandate source
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK; weak typing).
- Actual frozen verdict: `OK` (deny-list only). Independently expected: `BLOCK`
  or upstream-schema rejection.
- ENA semantics: ENA-CON-029 (claimed issuer ≠ verified issuer); authority is
  not self-declared (V2 ATT-3). A deny-list cannot positively type authority.
- Category: **false OK**; upstream-schema precondition documented as a required
  trust boundary.
- Smallest correction: positive typing — mandate source ∈ explicit authorizing
  vocabulary, or verified via an `authority_registry` grant covering the
  binding — R9.
- Governance/runtime cost: authorizing-source vocabulary must be maintained
  (new legitimate sources must be added or granted via the registry).
- Positive control: V24-P10 (USER_EXPLICIT_GRANT); upstream: V24-P13 (grant
  resolves) + V24-A09 (grant missing → BLOCK); negative preserved: S2.

### I12 — transfer evidence ref unresolvable
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK).
- Actual frozen verdict: `OK`. Independently expected: `BLOCK`.
- ENA semantics: scope transfer/equivalence is itself consequential evidence;
  `TRANSFER_EVIDENCE_REQUIRED` demands evidence_refs — those must resolve.
- Category: **false OK** (expansion authorized by unresolvable evidence).
- Smallest correction: transfer evidence refs resolve when the evidence
  registry is supplied — R3.
- Cost: low. Positive control: V24-P05.

### I13 — full recovery without state evidence
- **Classification: CONFIRMED_MATERIAL_DEFECT** (false OK).
- Actual frozen verdict: `OK`. Independently expected: `BLOCK`.
- ENA semantics: STATE_AND_HISTORY = state restoration AND history continuity;
  V2 required history evidence; the state half was unenforced.
- Category: **false OK**.
- Smallest correction: STATE_AND_HISTORY requires state_restore.evidence_refs
  non-empty and resolved — R8.
- Cost: low. Positive control: V24-P03 (both halves evidenced).

### I14 — SUPPORTED claim with only PARTIAL support
- **Classification: NEEDS_EXPERIMENT / SEMANTIC_CHALLENGE — treated separately
  per the Host instruction.** Demonstrated decision-changing: the frozen
  verdict `OK` overstates the support envelope (a full SUPPORTED claim resting
  only on PARTIAL support). The machine cannot parse assertion narrowing from
  text, so the minimal rule is: PARTIAL-only support for a full SUPPORTED
  claim → **UNKNOWN** (`PARTIAL_SUPPORT_ONLY`; insufficiency = uncertainty, not
  contradiction); an explicitly narrowed claim (`support_claim: "PARTIAL"`) → OK.
  The full assertion-level narrowing semantics remains an open question
  (documented; future experiment required).
- Actual frozen verdict: `OK`. Independently expected: `UNKNOWN_OR_BLOCK`.
  Successor: `UNKNOWN` (within the independent expectation).
- Positive control: V24-P11 (explicitly narrowed partial claim → OK).

### I15 — root registry supplied as list
- **Classification: CONFIRMED_MATERIAL_DEFECT** (exception; R11).
- Actual frozen verdict: **EXCEPTION** `AttributeError: 'list' object has no
  attribute 'get'`. Independently expected: NO_EXCEPTION.
- ENA semantics: registry container shapes must be validated before dispatch;
  a machine contract never raises for a plausible representation.
- Category: **exception** (robustness defect; NOT host-specific).
- Smallest correction: canonical normalization accepts dict-or-list registries;
  malformed → `REGISTRY_MALFORMED`; residual faults fail closed
  (`EVALUATOR_FAULT`) — R11. The I15 payload itself (list, resolvable) → OK.
- Cost: moderate (normalization surface). Positive control: V24-P04;
  negative: V24-A05 (malformed shape).

### I16 — support registry supplied as dict
- **Classification: CONFIRMED_MATERIAL_DEFECT** (exception; R11).
- Actual frozen verdict: **EXCEPTION** `AttributeError: 'str' object has no
  attribute 'get'`. Independently expected: NO_EXCEPTION.
- Same family as I15 on the support path.
- Smallest correction: same (R6/R11). The I16 payload (dict, resolvable) → OK.
- Positive control: V24-P09; negative: V24-A04 (malformed shape).

### CF-1 / CF-2 / CF-3 — composition failures
- CF-1 (valid top-level support + mandatory resolution → false BLOCK) =
  I06 → CONFIRMED_MATERIAL_DEFECT, fixed by R6.
- CF-2 (global obligation validation + claim-specific resolution → false
  BLOCK) = I07 → CONFIRMED_MATERIAL_DEFECT, fixed by R7.
- CF-3 (baseline applicability + registry path → weaker composed validation) =
  I04/I05 → CONFIRMED_MATERIAL_DEFECT, fixed by R4.

### Oracle challenge (O01–O04 + §6/§10.12)
- **Classification: CONFIRMED_MATERIAL_DEFECT of the V2.3 acceptance ORACLE**
  (not of the evaluator): expected verdicts derived from fixture `kind` labels
  (O01), hard-coded migrated IDs (O02), registry-key absence (O03 shared blind
  spot), and representation disagreement (O04). The frozen 53-entry manifest
  remains valid as an authored regression list for the frozen corpus, but not
  as a general semantic oracle.
- Smallest correction: structural oracle deriving expected verdicts from
  semantic preconditions only (acceptance_semantics_v24); verified 20/20
  consistent with the independent expectations (I14 refined UNKNOWN_OR_BLOCK →
  UNKNOWN, documented above).
- Controls: O01–O04 retained in the corpus as oracle-consistency probes.

---

## Phase 1 verdict

- **CONFIRMED_MATERIAL_DEFECT: 16 findings** (I01–I13, I15, I16, oracle).
- **SEMANTIC_CHALLENGE / NEEDS_EXPERIMENT: 1** (I14 — minimal rule implemented,
  full semantics open).
- **CONFIRMED_BUT_EXPECTED_BOUNDARY: 0** (every finding is beyond the documented
  freeze boundaries; the freeze boundaries themselves were confirmed, see §8 of
  the independent report).
- **NOT_REPRODUCED: 0.**

No remediation suggestion was adopted merely because it came from the
independent validator; each was confirmed against the frozen code and the
shipped baseline before being implemented in the successor (see
`v2.4/successor_contract.py` header for the R1–R11 mapping).

## Evidence

- Reproduction: `v2.4/reproduction-v23.json` (DSH run at frozen ref).
- Independent probes (preserved, provenance tagged):
  `v2.4/independent_fixtures.py`.
- Successor replay: `v2.4/results-v24.json` (98 fixtures, 0 unexpected).
- Independent report (evidence): `collaboration/inbox/2026-08-21-ena-v23-independent-validation-gpt56sol.md`.
