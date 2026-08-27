# ENA v0.3.7 candidate.1 — focused open-branch reconciliation

Status: `TWO_NEW_MATERIAL_DEFECTS / ONE_RESIDUAL / ATTACK_SPACE_REMAINS_OPEN / CURRENT_UNCHANGED`

Date: 2026-08-27

## Why this exists

Candidate.1 first repaired the four deterministic defects sealed by fresh Phase A. The project methodology forbids treating those four repairs as proof that the remaining Phase-A attack space disappeared.

A focused deterministic probe therefore followed three still-open branches without pretending to repeat fresh Phase A.

Probe workflow:

`ENA v0.3.7 Candidate.1 Open Branch Probes`

Run:

`33052192384`

Probe source:

`.github/scripts/v037_candidate1_open_branch_probes.py`

Targeted repair gate already passing before these observations:

`33051985315 / SUCCESS`

## Observed behavior

The focused probe observed:

- a COMMITTED integration can claim `selection_state_at_commit: SUPPORTED` even when the only represented supporting evaluation occurs later;
- a COMMITTED integration can claim `selection_state_at_commit: UNKNOWN` even when a prior represented evaluation already establishes `SUPPORTED`;
- a correct earlier SUPPORTED integration can remain valid after a later HARMFUL re-evaluation, which is a required false-BLOCK control;
- a packet with `source_selection_state: SUPPORTED` can replace `source_experiments` and `source_evaluations` with `[{}]`, recompute its digest, and pass `validate_packet_v2`;
- that shallow source packet can import into a record that still passes the receiver record validator while correctly keeping receiver-local selection `UNASSESSED`;
- source and receiver may currently share the same `candidate_id` string and still validate.

## O-1 — integration time-snapshot inconsistency

**Disposition:** `MATERIAL_CANDIDATE_DEFECT / REPAIR_IN_CANDIDATE1`

The evolution-record schema makes `selection_state_at_commit` a required field of every integration-history item and restricts it to `SUPPORTED`, `PARTIAL`, or `UNKNOWN`.

The existing candidate validator already treats chronology as semantic for expression/evaluation/integration latest-state resolution and its selftest describes a valid committed integration as preserving selection/authority/recovery representation.

Therefore `selection_state_at_commit` cannot honestly be treated as an unconstrained annotation.

The correct repair is **not**:

`selection_state_at_commit == current selection_state forever`

because the probe independently preserved a legitimate post-commit re-evaluation path.

Instead candidate.1 must derive the latest represented evaluation at or before the integration timestamp:

- if one exists, `selection_state_at_commit` must match that snapshot;
- if no represented evaluation exists by that timestamp, a COMMITTED integration may only claim `UNKNOWN` under the existing schema;
- later evaluations may legitimately change current selection without rewriting the historical commit snapshot;
- ties at the commit-time cutoff are ambiguous and must not be silently resolved by array order.

The same item also carries optional `expression_state_at_commit`. When present, it is another historical snapshot and should be checked against represented expression history at or before the same integration time, with the no-history default remaining `LATENT`.

This is a consistency repair, not a new requirement that integration can occur only after positive selection; `UNKNOWN` remains an existing allowed commit state.

## O-2 — shallow source-history objects masquerade as represented history

**Disposition:** `MATERIAL_CANDIDATE_DEFECT / REPAIR_IN_CANDIDATE1`

The packet and imported migration schemas intentionally distinguish transferred source evidence from receiver-local proof. That epistemic boundary remains correct and must be preserved.

However, `source_experiments` and `source_evaluations` are described and consumed as represented source history. An empty object is not structurally a represented experiment or evaluation under the already-existing evolution-record v2 item contracts.

This is distinct from external authenticity:

```text
STRUCTURALLY_REPRESENTED_SOURCE_HISTORY
!=
AUTHENTICATED_SOURCE_TRUTH
```

Candidate.1 should reuse the canonical evolution-record item schemas to validate source experiment/evaluation/integration objects rather than invent a second source-history ontology.

It should also preserve packet-local selection consistency at least to the level necessary to prevent `source_selection_state` from contradicting the latest represented source evaluation. This still does not establish that the source evaluation is true, authentic, or locally applicable.

Receiver-local selection must remain `UNASSESSED` after import until real receiver-local experiment/evaluation occurs.

## O-3 — source/receiver candidate-id collision

**Disposition:** `RESIDUAL / HOST_NAMESPACE_POLICY / NOT_CURRENTLY_A_CANDIDATE_DEFECT`

The probe showed that a source and receiver can use the same candidate-id string while origin and migration provenance still distinguish source versus receiver roles.

No current ENA contract establishes a universal cross-Host/global candidate-id namespace. Forcing inequality would therefore add a new identity law that the evidence does not yet justify and could false-BLOCK legitimate local namespace reuse.

Keep this branch visible for Host mapping, commons/interchange, and future identifier-scope work. Do not block candidate.1 solely on it.

## Other Phase-A branches remain open

This focused pass does not close:

- natural hot/cold cue salience;
- zh-CN behavioral equivalence;
- Host-native equivalence;
- external truth/authority;
- durable packet-reference retention beyond self-contained copied source context;
- cumulative optional-reference governance cost;
- other cross-axis historical contradictions not yet demonstrated as decision-material;
- composed-validator behavior under novel composed inputs.

## Candidate.1 consequence

Candidate.1 remains mutable and not frozen.

Required next action:

1. repair O-1 and O-2 with mutation-sensitive regressions and false-BLOCK controls;
2. rerun inherited + Phase-A-derived targeted regression;
3. run focused open-branch probes again and record whether the demonstrated failures close without collapsing legitimate post-commit reselection or receiver-local UNASSESSED behavior;
4. only then proceed toward exact pre-freeze validation.

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`.
