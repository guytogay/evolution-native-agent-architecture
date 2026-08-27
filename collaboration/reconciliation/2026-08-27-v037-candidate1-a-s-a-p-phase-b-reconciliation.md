# ENA v0.3.7 candidate.1 — A-S/A-P Phase B reconciliation

Date: 2026-08-27

Status: `INDEPENDENT_EVIDENCE_ACCEPTED / NEEDS_REVISION / CANDIDATE_2_REQUIRED / CURRENT_UNCHANGED / ATTACK_CARDINALITY_OPEN`

## 1. Exact evidence binding

Frozen candidate.1:

- identity: `v0.3.7-candidate.1`
- frozen source: `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- frozen subtree: `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`
- candidate branch: `candidate/v0.3.7-candidate.1`
- candidate branch remains parked at the frozen source.

Fresh blind-semantic validation:

- setup head: `711a2028ae5644eefa90219e49e3f4325aadc903`
- A-S seal: `2e6b46aeedc1945a03aac93620ad36aa1ccbd70f`
- final A-P commit: `b970148fe9596ea9cad0a2817a3b399a1d2b75f5`
- validation branch: `validation/v037-c1-blind-semantic-primary`

Commit-parent verification:

```text
711a2028...
  -> 2e6b46ae...  A-S report only
  -> b970148f...  A-P report only
```

The setup-to-final comparison contains exactly two added files:

- `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-s-primary.md`
- `collaboration/reconciliation/2026-08-27-v037-candidate1-independent-a-p-primary.md`

No candidate bytes and no `releases/current/` bytes were modified by the independent reviewer.

Therefore the A-S seal and A-P artifact are accepted as valid independent occurrence truth under the declared A-S/A-P information boundary.

## 2. Phase B rule

The independent validator's expected severity is not an oracle.

For each finding, Phase B asks:

1. is the failure reproducible from the exact frozen bytes?
2. does it contradict a candidate-local claim/contract rather than an invented universal rule?
3. is it an external-truth/Host boundary that the candidate already narrows honestly?
4. did author evidence already cover the exact shape, cover only an adjacent shape, or miss it?
5. would fixing it destroy a legitimate lightweight/non-applicable behavior?

## 3. A-S-01 — integration before represented reality contact

Independent finding:

A committed integration can occur before record creation / experiment / evaluation, use `selection_state_at_commit=UNKNOWN`, and later become current `SUPPORTED`.

### Frozen-byte readback

`tools/validate_evolution_record_v2.py`:

- parses `created_at` but does not compare it with the integration timestamp;
- for an `INTEGRATED` record, requires experiment/evaluation arrays to exist somewhere in the record;
- at integration time, if no prior evaluation exists, explicitly accepts `selection_state_at_commit=UNKNOWN`;
- does not require a represented experiment/evaluation to exist at or before the integration commit.

`05-CORE-OPERATIONAL-CONTRACTS.md` states:

```text
variation -> experiment -> observed outcome -> selection -> integration/pruning
```

and more specifically:

```text
Unresolved integration is permitted only when actual reality-contact evidence exists
and the remaining consequence is explicitly bounded.
```

### Author-evidence comparison

Candidate.1 author-side open-branch reconciliation had already repaired a narrower historical-snapshot defect and explicitly preserved:

```text
if no represented evaluation exists by the integration timestamp,
a COMMITTED integration may only claim UNKNOWN under the existing schema
```

That author conclusion correctly prevented false claims of `SUPPORTED`, but it conflated two distinct questions:

```text
WHAT MAY THE COMMIT SNAPSHOT SAY?
!=
MAY INTEGRATION OCCUR BEFORE ANY REALITY CONTACT EXISTS?
```

The fresh A-S branch independently separated them.

### Phase B disposition

`MATERIAL_CANDIDATE_DEFECT / SHARED_BLIND_SPOT / CANDIDATE_2_REPAIR_REQUIRED`

The minimal correction must preserve `UNKNOWN` as a legitimate integration snapshot when reality contact exists but remains unresolved. It must not restore a universal rule that only `SUPPORTED` can integrate. But integration must not be represented before the reality-contact history that is claimed to justify even an unresolved bounded integration.

## 4. A-S-02 — durable migration provenance can contradict itself

Independent finding:

A `MIGRATION_CANDIDATE` record can simultaneously represent contradictory:

- top-level `source_candidate_id` vs `migration.source_candidate_id`;
- top-level `source_packet_sha256` vs `migration.packet_sha256`;
- `migration.packet_purpose` vs `migration.source_selection_state`.

### Frozen-byte readback

The v2 record schema requires the duplicated provenance fields but does not bind their values together. The candidate record validator only requires a migration object and applies receiver-local provenance checks after local selection; it does not compare these duplicate source claims.

Packet-v2 validation and helper import are stricter, but that only proves the helper-produced ingress shape. A durable record later assembled or mutated by another producer can still pass while internally contradicting the packet/source identity it claims to preserve.

### Phase B disposition

`MATERIAL_CANDIDATE_DEFECT / DURABLE_RECORD_PROVENANCE_GAP / SHARED_BLIND_SPOT / CANDIDATE_2_REPAIR_REQUIRED`

This is not a request to authenticate external source truth. The repair is internal represented consistency only:

```text
DUPLICATED_SOURCE_CLAIMS_WITHIN_ONE_RECORD -> MUST_NOT_CONTRADICT
```

Receiver-local selection must remain separate and may remain `UNASSESSED`.

## 5. A-S-03 — irrelevant malformed Authority grants poison NOT_REQUIRED

Independent finding:

For a valid query with `authority_required=false`:

- `grants=[]` -> `NOT_REQUIRED`;
- `grants=[{}]` -> `INVALID_RECORD`.

### Frozen-byte readback

`references/general/authority-lease/tools/validate_authority_lease.py` validates every represented grant and returns `INVALID_RECORD` on any grant error before it reaches the `authority_required is False` branch.

The reference's own purpose is applicability-scoped and explicitly supports a lightweight non-authority path.

### Phase B disposition

`MATERIAL_FALSE_BLOCK / OPTIONAL_REFERENCE_APPLICABILITY_DEFECT / SHARED_BLIND_SPOT / CANDIDATE_2_REPAIR_REQUIRED`

The repair must not weaken validation for authority-required queries. It should prevent data that is not consulted by a legitimate `NOT_REQUIRED` decision from manufacturing ceremony/blockage.

## 6. A-S-04 — equal-sequence effect receipts make retry depend on array order

Independent finding:

Two receipts for one effect with the same integer sequence but contradictory statuses can both validate. `next_action` sorts only by sequence and takes the last list element, so a semantic permutation can alternate between `RETRY_SAME_INTENT` and `NO_EFFECT_NEEDED`.

### Frozen-byte readback

`references/general/effect-lifecycle/tools/validate_effect_lifecycle.py`:

- requires receipt IDs to be unique;
- requires integer `sequence`;
- does not require sequence uniqueness or deterministic same-sequence resolution per effect;
- sorts receipts only on `sequence` before choosing the final represented status.

At an external-effect boundary, list order is not a valid settlement fact.

### Phase B disposition

`MATERIAL_EFFECT_BOUNDARY_DEFECT / ORDER_DEPENDENT_FALSE_CONFIDENCE / SHARED_BLIND_SPOT / CANDIDATE_2_REPAIR_REQUIRED`

A deterministic ambiguity posture is required. The repair must retain legitimate single-receipt decisive states and must not turn every retry into WAIT.

## 7. A-P-05 — candidate.1 self-description drift

The post-seal package audit also found deterministic active-package drift:

- `00-READ-ME-FIRST.md` says `candidate.1` but still says `ASSEMBLED_PENDING_AUTHOR_FALSIFICATION` after author falsification and exact prefreeze work were complete;
- the same file introduces current bundled references as `Candidate.0 bundles:`;
- `09-EVOLUTION-METABOLISM.md` is headed candidate.1 while active prose still says `Candidate.0 ...` without marking those statements as predecessor history;
- the candidate-local v2 validator self-label says `v0.3.6 candidate.1` while shipped under the v0.3.7 candidate package.

The reviewer correctly did **not** classify `frozen:false` / `NOT_FROZEN` in the immutable prefreeze bytes as a contradiction, because the external freeze protocol intentionally preserves prefreeze occurrence truth.

### Phase B disposition

`DETERMINISTIC_PACKAGE_SELF_DESCRIPTION_DRIFT / CANDIDATE_2_PACKAGING_REPAIR`

This is not a new Core semantic defect, but candidate.2 should correct active adopter/reviewer-facing identity/status prose while preserving predecessor/freeze occurrence history where explicitly historical.

## 8. Overall candidate.1 verdict

```text
A-S-01 = MATERIAL_CANDIDATE_DEFECT
A-S-02 = MATERIAL_CANDIDATE_DEFECT
A-S-03 = MATERIAL_OPTIONAL_REFERENCE_FALSE_BLOCK
A-S-04 = MATERIAL_EFFECT_BOUNDARY_DEFECT
A-P-05 = DETERMINISTIC_PACKAGE_SELF_DESCRIPTION_DRIFT

CANDIDATE_1_VERDICT = NEEDS_REVISION
MATERIAL_CHANGE_REQUIRED = TRUE
CANDIDATE_1_MUTABLE_IN_PLACE = FALSE
CANDIDATE_2_REQUIRED = TRUE
ATTACK_CARDINALITY = OPEN
CURRENT_CHANGED = FALSE
```

Candidate.1 remains immutable occurrence truth at:

- source `ae6903464133cb5bcf3cd8909ecae1215fe0b9ba`
- subtree `c0458e0d7ea417b841cbf4c8bf6e64e4aff37319`

## 9. Candidate.2 repair posture

Create successor:

`candidate/v0.3.7-candidate.2`

from the exact candidate.1 frozen source.

Repair semantic radius should remain narrow:

1. require represented reality contact at/before integration while preserving legitimate unresolved `UNKNOWN` snapshots and post-commit reselection;
2. bind duplicated durable migration provenance claims and packet-purpose/source-selection consistency without turning transferred source evidence into local proof;
3. resolve Authority non-applicability before irrelevant grant validation can false-BLOCK;
4. reject or otherwise deterministically narrow contradictory same-sequence effect receipt state while preserving legitimate decisive states;
5. repair candidate.2 active package/self-description projection;
6. add mutation-sensitive regressions for every sealed independent failure shape plus false-BLOCK controls;
7. rerun inherited candidate checks, candidate.1 successor regressions, fresh-A-S-derived regressions, and focused nearby open-branch probes;
8. keep Current `v0.3.6` untouched.

Do not interpret successful targeted repair as a second fresh A-S.

## 10. Independent-review consequence

The A-S/A-P method paid epistemic rent: it exposed failure shapes not recovered by the author-side candidate.1 repair loop, including one case where author reasoning had explicitly stabilized an insufficient boundary.

That result does not imply every successor must mechanically receive infinite fresh reviews. Candidate.2's later independence decision must again be made from marginal epistemic value after exact repair/freeze, not from ritual repetition.

## 11. Next governed action

`CANDIDATE2_FOCUSED_SUCCESSOR_REPAIR`

Then:

```text
focused repair
-> mutation-sensitive regression
-> nearby open-branch probes
-> exact prefreeze gate
-> external freeze if PASS
-> explicit post-freeze independence/release reconciliation decision
```

No promotion is authorized by this record.
