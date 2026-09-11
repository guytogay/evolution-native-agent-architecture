# Clean ENA SAFE-CHANGE enforcement correction

Date: 2026-09-12

Project-status note only. This is not ENA adopter/runtime content.

External review by Claude Code identified a concrete implementation gap: the clean product documented a SAFE-CHANGE state machine, but the reference tools did not yet enforce those transitions. Grok's field-readiness review simultaneously warned against expanding the conceptual surface before real Host evidence. The accepted correction therefore implements existing promises without adding a new governance layer.

Merged product change:

- repository: `guytogay/ENA`
- PR: `#19` — `Enforce SAFE-CHANGE state transitions`
- main commit: `f6147330293fec4a536096a5eb98dbe905836ed8`

Implemented:

- `tools/safe_change_state.py` provides a non-zero gate for the documented SAFE-CHANGE state machine;
- `preparing -> armed` is blocked while required recovery fields remain unresolved;
- invalid state transitions are rejected;
- `retained`, `restored`, and `failed` require an evidence reference;
- state history is preserved in `transitions.jsonl`;
- `tools/change_scaffold.py` now creates an explicit non-working `rollback.py` placeholder rather than implying rollback is configured;
- ENA control-file parsing used by preflight/validation tools is shared through `tools/control_yaml.py` and fails closed on unsupported YAML constructs instead of silently guessing;
- control parser edge cases are covered by `tools/test_control_yaml.py`, and reference-tool CI runs both parser tests and `self_test.py`;
- `RESCUE.example.yaml`, `STATUS.example.yaml`, README, SAFE-CHANGE and the session Git example were aligned to the executable gate.

Important boundary:

- reference gates have force only when the Host/Agent actually routes work through them;
- direct manual edits can still bypass a reference script unless a Host hook/permission boundary prevents that;
- multi-rescuer locking/idempotent rollback remains Host-dependent and is not falsely claimed as solved by the reference gate;
- no mandatory human/independent-review gate was added for evolution decisions; that would be a new governance mechanism and should wait for field evidence;
- LICENSE/repository metadata concerns from review remain separate repository-maintenance choices, not ENA runtime behavior.

Next action remains real evidence, not more mechanism design:

`RUN_FRESH_AGENT_MINIMUM_RUNTIME_CHAIN_AND_SLEEP_DREAM_FIELD_TRIALS`

In particular, ENA Issue #14 should now exercise the state gate on a real Host rather than merely verifying the scripts in CI.
