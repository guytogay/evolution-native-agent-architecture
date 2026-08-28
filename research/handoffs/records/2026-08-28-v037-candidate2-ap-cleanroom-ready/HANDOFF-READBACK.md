# Handoff readback — candidate.2 A-P clean-room ready

Assertions:

- Current remains `v0.3.6 / CURRENT / FIELD_VALIDATION`.
- Candidate.2 remains frozen at source `bda470e0a6b170cec61225a905957a501454a2fe` / subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`.
- Fresh A-S report remains exact-byte sealed at SHA-256 `0e6bb214cc3398b34c13fc6a3bebd1f548ae00ea067b4c338e8ce88f42ad955f`.
- A-S report remains unedited after the wrapper-identity correction.
- Originally supplied A-S wrapper SHA `28dde50c9caaeee3b5cfabf51410083dbbb05a93` is superseded as a control-plane identity by actual parentless commit `28dde50c9caaeee3b5c269e28a7be5f07ac29ae5`.
- Actual A-S tree is `42debebed620bd05e6e2635409057f20b57bfa9e`, equal to the tree recorded before the correction.
- Separate A-P clean-room commit is `aea2ed25107145a557b3fe46ca0e4b90e2b90fa9`.
- A-P commit is parentless and has tree `08ac16303d69a6a268197ac26b23c5b20972b727`.
- A-P package subtree is exactly `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`.
- A-P has not started.
- Phase B has not started.
- Candidate repair has not started.
- Next action is `RETURN_SAME_FRESH_REVIEWER_TO_CANDIDATE2_A_P_CLEAN_ROOM`.
- `ATTACK_CARDINALITY = OPEN`.
