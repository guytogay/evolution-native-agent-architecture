# Handoff — candidate.3 frozen; v0.3.7 release branch next

Status: `HANDOFF_READY / CANDIDATE3_FROZEN / TARGETED_POSTFREEZE_PASS / RELEASE_HARDENING_PASS / CANDIDATE_SUCCESSION_STOP / RELEASE_PREPARATION_SUPPORTED`

## Canonical state

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`

Frozen final candidate target:

`v0.3.7-candidate.3`

- frozen source: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- exact pre-freeze run: `33150269264` — SUCCESS
- targeted post-freeze run: `33150553992` — SUCCESS
- release hardening run: `33152201566` — SUCCESS
- candidate succession: `STOP`
- release preparation: `SUPPORTED`
- candidate.4: `NOT_JUSTIFIED_BY_CURRENT_EVIDENCE`

Key records:

- `collaboration/reconciliation/2026-08-28-v037-candidate3-successor-repair-reconciliation.md`
- `collaboration/reconciliation/2026-08-28-v037-candidate3-freeze.md`
- `collaboration/reconciliation/2026-08-28-v037-candidate3-targeted-postfreeze-revalidation.md`
- `collaboration/reconciliation/2026-08-28-v037-candidate3-final-release-reconciliation.md`
- `collaboration/reconciliation/2026-08-28-v037-candidate3-release-hardening-reconciliation.md`

## Hardening conclusion

The final hardening audit did not demonstrate a new material frozen candidate-byte defect.

Observed v0.3.6 -> candidate.3 compatibility is explicit:

- all Current core adopter paths remain;
- Constitution ID set remains 38/38;
- inherited composed-valid behavior remains 164/164 zero-flip;
- successor closure corpus remains 61/61;
- legacy `ena_evolve.py` is byte-exact under `tools/legacy/ena_evolve_v1_2.py`;
- candidate1/candidate2 legacy adversarial probes changed only truthful legacy/path/module/output labels and execute PASS;
- no unexplained removed files remain after classifying the candidate baseline and legacy relocations;
- candidate-local Markdown navigation has zero broken relative links;
- Authority/Effect/source-receiver/Host evidence boundaries remain visible.

Frozen candidate.3 still contains pre-freeze candidate identity/status narration by design under the external-record freeze model. Release packaging must project that occurrence into truthful `v0.3.7 / CURRENT / FIELD_VALIDATION` identity without silently changing validated material semantics.

## Immediate next action

`MAIN_VISIBLE_CHECKPOINT_THEN_CREATE_RELEASE_V0_3_7_AND_TRANSPLANT_FROZEN_CANDIDATE3`

Follow the established v0.3.6 release pattern:

1. merge this freeze/revalidation/hardening/control state to `main`;
2. create governed `release/v0.3.7` from that exact main checkpoint;
3. transplant frozen candidate.3 subtree byte-for-byte into `releases/current/` as a separately auditable packaging start;
4. then perform release identity/status packaging only;
5. run exact-head release validation / Main Gate / CodeQL / package parity/readback;
6. explicitly authorize merge only on the exact reviewed release head;
7. post-merge reverify Current and update project alignment/handoff.

Do not modify frozen candidate.3 bytes. A material candidate-byte correction would require candidate.4, but candidate.4 is neither planned nor justified by current evidence.

Attack cardinality remains OPEN. External truth / natural Host behavior remain field evidence boundaries, not candidate blockers by default.
