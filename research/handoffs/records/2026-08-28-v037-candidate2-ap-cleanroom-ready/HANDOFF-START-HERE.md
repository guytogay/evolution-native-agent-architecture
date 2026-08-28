# Handoff — candidate.2 A-P clean-room ready

Status: `HANDOFF_READY_FOR_SESSION_SUCCESSION`

Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.

Candidate.2 remains frozen, not Current, and not released:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Fresh A-S is complete and content-sealed:

- report `collaboration/reconciliation/2026-08-28-v037-candidate2-independent-a-s-primary-r3.md`
- SHA-256 `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`
- verdict `NOT_CLEARED`
- findings `A-S-01..A-S-04`

A-S wrapper identity correction:

- originally supplied/unresolvable wrapper SHA `28dde50c9caaeee3b5cfabf51410083dbbb05a93`
- actual parentless A-S commit `28dde50c9caaeee3b5c269e28a7be5f07ac29ae5`
- actual A-S tree `42debebed620bd05e6e2635409057f20b57bfa9e`
- reviewed file surface changed by correction: `false`

The separately exposed A-P clean-room stage is now ready:

- repo `guytogay/independent-validation-cleanroom`
- branch `main`
- commit `aea2ed25107145a557b3fe46ca0e4b90e2b90fa9`
- tree `08ac16303d69a6a268197ac26b23c5b20972b727`
- parents `[]`
- package subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Immediate next action:

`RETURN_SAME_FRESH_REVIEWER_TO_CANDIDATE2_A_P_CLEAN_ROOM`

The reviewer completes A-P, returns exact report bytes plus an external SHA-256 digest, and STOPs before project-manager Phase B. Candidate repair remains forbidden until A-P completes and Phase B classifies the findings.

`ATTACK_CARDINALITY = OPEN`
