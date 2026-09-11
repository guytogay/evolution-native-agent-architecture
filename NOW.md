# ENA — NOW

This is maintainer/project status, not adopter/runtime content.

## Legacy Current

- repository: `guytogay/evolution-native-agent-architecture`
- `v0.3.14 / CURRENT / FIELD_VALIDATION`
- identity authority: `releases/current/CURRENT-BASELINE.yaml`
- effective package: `releases/current/`
- field stream: Issue `#208`

Do not mutate `releases/current/**` without successor identity.

## Clean product home

Repository: `guytogay/ENA`

State: `ACTIVE_DEVELOPMENT / NOT_CURRENT / NOT_PROMOTED`

Latest product correction merged to `main` at:

`f6147330293fec4a536096a5eb98dbe905836ed8`

Direct adopter path remains:

```text
FIRST-USE.md
→ A2A.md
→ SURVIVAL.md
→ SAFE-CHANGE.md
→ EVOLUTION.md
→ SLEEP-DREAM-QUICKSTART.md
```

## 2026-09-12 external field-readiness reviews

The Grok review established the current field-readiness corrections:

1. **Reading is not installation.** `tools/ena_preflight.py` provides a startup/session gate for missing/incomplete/stale First Use.
2. **Two Host profiles.** Resident runtimes and session/coding Agents use different recovery mechanisms.
3. **Human rescue is first-class.** A2A and timed rollback are not universal gates.
4. **First Use is minimum-first.** Explicit `UNKNOWN` values are valid; `SYSTEM.yaml` expires through `checked_at` / `valid_until`.
5. **Sleep/Dream parameters are experimental.** Counts, weights, distance bands and cadence are field parameters rather than ENA requirements.
6. **Speculative candidates are isolated.** Generated candidates live under `evolution/candidates/speculative/` and require reality contact before selected outcomes.
7. **Reference-tool CI is not field evidence.** ENA Issue #14 requires a real fresh-Agent runtime chain; Issue #12 collects Sleep/Dream evidence.
8. **Repository relationship is explicit.** New adopters use `guytogay/ENA`; this older repository remains previous-release/research/history/succession and is not archived yet.

The subsequent Zhipu review largely confirmed the product is now directly usable and identified two remaining adoption-friction gaps. Both were accepted because they reduce Host mapping cost without expanding ENA theory.

### Trusted preset / unattended First Use

`FIRST-USE.md` permits non-interactive adoption when timezone, language, ENA home, Host profile, recovery path and rescuer were already supplied by a trusted deployment/workspace policy or Host integration.

Important boundary:

- unattended mode does **not** introduce ENA product defaults;
- a missing value remains unresolved rather than guessed;
- `tools/ena_init.py` accepts caller-provided `--host-profile`, `--recovery`, `--rescuer`, and `--rescuer-type`;
- `--verified-minimum` is explicit and only valid when the caller/integration already verified the supplied recovery/rescue facts;
- `ena_preflight.py` remains the startup/session gate after initialization.

### Session/coding Agent Git example

The product includes `examples/change/SESSION-GIT-WORKTREE.md` with a concrete safe-change path for durable Git state plus a human or fresh Agent session as recovery. The example is now aligned to the executable SAFE-CHANGE state gate rather than asking an adopter to edit status manually.

## 2026-09-12 cross-session / knowledge / capability Dream scope

Owner clarified that Sleep/Dream material should reflect the Agent's broader accessible life and capability surface, not only the current conversation.

Accepted product changes in `guytogay/ENA` PR #17:

- past and future sessions/task history may feed later Sleep/Dream when the Host or authorized integration exposes them;
- authorized knowledge bases, note systems, project documentation, repositories and connected files may be used as bounded Dream material;
- Dream may include the Agent's current verified tools/skills/connectors/APIs;
- discoverable but not installed/enabled capabilities may also participate as **possibilities**, but must not be treated as already available;
- capability truth should come first from First Use/live Host discovery; an A2A Agent Card may contribute advertised skills/capabilities but does not override live verification;
- a capability-dependent candidate must re-check installation, permissions/authorization and current interface before reality contact or production use;
- a candidate that survives a sandbox/worktree/preview trial is `selected`, not automatically production-applied;
- selected changes that are not already live must be applied to production separately, using `SAFE-CHANGE.md` when critical runtime state is affected, then observed in live operation.

New reference material/tools:

- `examples/evolution/KNOWLEDGE.example.jsonl`;
- `examples/evolution/CAPABILITIES.example.jsonl`;
- `tools/combine_dream_material.py` to combine memory/session material + knowledge material + capability material into one bounded Dream input stream.

Reference-tool CI passed for PR #17 before merge.

## 2026-09-12 workshop-derived validation / feedback / freshness path

A Kingdee Lingji development workshop provided concrete external implementation evidence around Agent harness quality: validation inside the execution loop, deterministic checks after edits, feedback/trajectory retention, checkpoint/recovery infrastructure, tool discovery, Skills/MCP, and memory including Dream. The clean ENA product did **not** copy the product-specific harness architecture.

Three transferable capabilities were added in `guytogay/ENA` PR #18:

1. **Validate close to the mutation.** When the Host exposes PostToolUse/Git/IDE/CI/service hooks, run the smallest relevant deterministic check immediately after a bounded change instead of waiting for the whole task to finish.
2. **Validation/repair trajectory becomes experience.** Preserve linked sequences such as `change → FAIL → bounded repair → PASS` as evolution evidence.
3. **Freshness/drift belongs in long-lived knowledge maintenance.** Knowledge, Agent Cards, connector catalogs, capability inventories and system maps can become stale; keep freshness state explicit rather than silently hardening old data as current truth.

Reference-tool CI passed for PR #18 before merge. This remains smoke-test evidence, not real-Host field validation.

## 2026-09-12 SAFE-CHANGE enforcement correction

Claude Code's review identified a real implementation gap: the product documented a SAFE-CHANGE state machine but the reference code did not yet enforce it. Grok simultaneously advised against adding more mechanisms before real Host evidence. The accepted correction therefore implements the already-promised state machine without adding a new governance layer.

Merged product PR #19 at `f6147330293fec4a536096a5eb98dbe905836ed8` adds:

- `tools/safe_change_state.py` as a non-zero gate for allowed SAFE-CHANGE transitions;
- blocking of `preparing -> armed` while required recovery fields remain unresolved;
- evidence requirements for `retained`, `restored`, and `failed`;
- `transitions.jsonl` for transition history;
- shared strict control-file parsing through `tools/control_yaml.py` instead of duplicated ad-hoc readers;
- fail-closed handling for unsupported control-YAML constructs rather than silent partial parsing;
- parser edge-case tests in `tools/test_control_yaml.py`, run by CI;
- an explicit non-working `rollback.py` placeholder from `change_scaffold.py`, so scaffold creation cannot be mistaken for configured recovery;
- simplified machine-readable `rescue.yaml` / `status.yaml` examples aligned to what the gate can actually enforce.

Important enforcement boundary:

- reference gates only have force when the Host/Agent actually routes work through them;
- direct manual edits can bypass a reference script unless Host hooks/permissions prevent bypass;
- multi-rescuer locking/idempotent rollback remains Host-dependent and is not falsely claimed as solved by the reference gate;
- no mandatory human/independent-review gate was added for evolution decisions because that would be a new governance mechanism without field evidence.

Detailed note:

`research/status-notes/2026-09-12-safe-change-enforcement.md`

## Current product evidence state

Reference-tool CI proves only that the reference tools execute against included examples. It does **not** prove the product works on a real Host.

Field evidence remains:

- ENA Issue #12 — Sleep/Dream field feedback, including negative/null results and parameter evidence;
- ENA Issue #14 — minimum fresh-Agent runtime-chain proof.

Do not claim field validation from smoke tests, documentation review, workshop architecture similarity, or an Agent saying the design looks correct.

## Product boundary

Still binding:

- ENA adds capabilities/infrastructure reasoning alone does not provide;
- do not rebuild ordinary model judgment as ENA machinery;
- owner/maintainer explanations are project context unless they independently help an adopter act;
- legacy ENA is evidence/regression/omission-checking material, not the new product blueprint;
- do not re-import old structure, terminology, handoff machinery or closed research merely because it exists;
- do not let Sleep/Dream experimental parameters harden into doctrine without field evidence;
- unattended adoption may consume trusted policy, but may not manufacture missing policy through guessed defaults;
- inaccessible sessions/knowledge must be recorded as unavailable rather than imagined;
- advertised or discoverable capabilities remain unverified possibilities until checked against live reality;
- deterministic validation proves only the property it directly checks; it is not evidence by itself that an evolution candidate is useful;
- reference enforcement must not be described as stronger than the Host wiring that actually invokes it.

Mandatory deep-succession record remains:

`research/handoffs/records/2026-09-07-v040-clean-product-home/`

A deep successor reads `CONSENSUS-LOCK.md`, then applies newer live state from this file and `CURRENT-HANDOFF.yaml`.

## Repository roles

- `guytogay/ENA` — clean product home.
- `guytogay/evolution-native-agent-architecture` — legacy Current + research/evidence/history + maintainer succession.
- `guytogay/human-ai-workbench` — general human-AI project-working method.
- `guytogay/ena-field-guide` — `SUNSET_AS_INDEPENDENT_PRODUCT / PRESERVE_USEFUL_EVIDENCE_THEN_ARCHIVE`.

## Immediate next action

`RUN_FRESH_AGENT_MINIMUM_RUNTIME_CHAIN_AND_SLEEP_DREAM_FIELD_TRIALS`

Priority order:

1. run ENA Issue #14 on at least one real session/coding Agent Host;
2. route SAFE-CHANGE status transitions through `safe_change_state.py` or an equivalent Host-native gate and observe real friction/bypass attempts;
3. confirm `ena_preflight.py` can actually be integrated into a real session/startup hook;
4. preserve at least one real `FAIL → repair → PASS` validation trajectory;
5. field-test Sleep/Dream with cross-session history, knowledge-base material and capability/possibility material in Issue #12;
6. verify at least one selected candidate can move through a protected production application path when appropriate;
7. iterate only from concrete friction, failure, null and recovery evidence;
8. do not add new mechanisms merely because another review can imagine them.
