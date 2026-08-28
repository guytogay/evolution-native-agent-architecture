# ENA v0.3.7 candidate.3 — External Freeze Record

Date: 2026-08-28

Status: `FROZEN_CANDIDATE.3 / EXACT_PREFREEZE_PASS / NOT_CURRENT / NOT_RELEASED / ATTACK_CARDINALITY_OPEN`

## Frozen identity

This record externally freezes the exact candidate.3 bytes already validated. The candidate subtree is **not rewritten** to insert a post-hoc `frozen: true` flag.

Frozen identity:

- candidate: `v0.3.7-candidate.3`
- branch: `candidate/v0.3.7-candidate.3`
- frozen source commit: `b7e88d7adb70396bd671ca97066daf2c120e0adc`
- frozen candidate subtree: `e3a9a20d16cecd78df7f32f19fca56e21159e810`
- Current subtree at frozen source: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- candidate files observed: `118`

Predecessor frozen identity:

- candidate: `v0.3.7-candidate.2`
- source: `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree: `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

## Freeze eligibility evidence

Successor repair reconciliation:

`collaboration/reconciliation/2026-08-28-v037-candidate3-successor-repair-reconciliation.md`

Exact workflow:

`ENA v0.3.7 Candidate.3 Exact Pre-Freeze Gate`

Exact workflow run:

`33150269264` — SUCCESS.

The gate tested detached source `b7e88d...` from a separate research control-plane checkout and ended with the target working tree clean.

Key observed conditions:

- exact source/candidate/Current binding PASS;
- Current isolation PASS;
- retained semantic trunk parity PASS;
- inherited composed-validator corpus 164/164 zero flips;
- successor closure corpus 61/61;
- v2 record selftest 35;
- v2 helper selftest 13;
- all bundled reference selftests PASS;
- inherited author/anti-ablation and candidate.1 successor replays PASS;
- candidate.3 Authority / Effect / transferred-source regressions PASS;
- package identity/lineage/zh-CN truth checks PASS;
- Python compile and no-bytecode/symlink cargo PASS;
- attack cardinality remains OPEN;
- fresh independent candidate.3 validation was **not** claimed;
- external truth was **not** established;
- release authority was **not** assigned by the gate.

## Freeze effect

Effective immediately for project governance:

```text
candidate.3 source b7e88d... + subtree e3a9a20...
= IMMUTABLE FROZEN OCCURRENCE TRUTH
```

Do not write material candidate.3 cargo after this record.

If later reconciliation discovers a material candidate-byte defect requiring correction, candidate.3 remains frozen and the correction requires a new successor identity such as `v0.3.7-candidate.4`.

Candidate.4 is **not** automatically required merely because candidate.3 is frozen or because attack cardinality remains OPEN.

## Post-freeze path

The next bounded step is targeted post-freeze reconciliation of the sealed candidate.2 blockers against this exact frozen candidate.3 identity.

This is not automatically a new full fresh A-S/A-P cycle. The project has already paid for the deliberately bounded final fresh search-space-independence cycle on candidate.2. Additional independent review must pay new epistemic rent rather than become ceremony.

If targeted reconciliation finds no material release blocker, proceed to explicit v0.3.7 release reconciliation/promotion decision.

Current remains:

`v0.3.6 / CURRENT / FIELD_VALIDATION`
