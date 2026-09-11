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

`9ad47c9efa9823167aa42e2062550295a97901d6`

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

The product includes `examples/change/SESSION-GIT-WORKTREE.md` with a concrete safe-change path:

```text
record known-good base commit
→ create isolated change branch + worktree
→ make/test one bounded commit
→ prepare exact recovery before application
→ apply only with git merge --ff-only
→ verify useful operation
→ retain or recover with git revert
```

This is an implementation example for the existing `session` Host profile, not a new ENA subsystem.

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

1. **Validate close to the mutation.** When the Host exposes PostToolUse/Git/IDE/CI/service hooks, run the smallest relevant deterministic check immediately after a bounded change instead of waiting for the whole task to finish. Examples include parser/schema, compilation, type, targeted test, build, health, access and retrieval checks.
2. **Validation/repair trajectory becomes experience.** Preserve linked sequences such as `change → FAIL → bounded repair → PASS` as evolution evidence. Sleep may later consolidate repeated trajectories into narrower procedures, cues or preventive checks when repeated evidence justifies it.
3. **Freshness/drift belongs in long-lived knowledge maintenance.** Knowledge, Agent Cards, connector catalogs, capability inventories and system maps can become stale. Preserve explicit freshness metadata when available; refresh from authoritative sources when practical; otherwise keep stale/unknown status visible instead of silently strengthening old data as current truth.

New product tools/examples:

- `tools/validate_change.py` — wraps a deterministic Host-native check, returns its exit status, and appends compact validation experience;
- `tools/freshness_scan.py` — reports JSONL records as `fresh / stale / unknown` from explicit freshness metadata without inventing a universal TTL;
- `examples/evolution/VALIDATION-TRAJECTORY.example.jsonl`;
- `examples/evolution/FRESHNESS.example.jsonl`.

`tools/change_scaffold.py` now asks each new safe-change package for incremental deterministic checks, validation-event references and final verification.

Reference-tool CI passed for PR #18 before merge. This remains smoke-test evidence, not real-Host field validation.

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
- do not copy Kingdee-specific Harness components into ENA merely because the workshop implementation appeared high quality.

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

1. run ENA Issue #14 on at least one real session/coding Agent Host using the Git/worktree example where appropriate;
2. wire `validate_change.py` or an equivalent Host-native mechanism into at least one real post-change hook and observe whether it shortens defect lifetime;
3. preserve at least one real `FAIL → repair → PASS` trajectory and verify later Sleep can consume it without overgeneralizing from one occurrence;
4. also run a resident Host when practical;
5. confirm `ena_preflight.py` can actually be integrated into a session/startup hook or trusted unattended deployment flow rather than merely invoked manually;
6. field-test Sleep/Dream with cross-session history, knowledge-base material and capability/possibility material in Issue #12;
7. observe real freshness/drift behavior for at least one knowledge/capability source instead of assuming TTLs are useful;
8. verify at least one selected candidate can move through a protected production application path when appropriate;
9. iterate from concrete friction, failure, null and recovery evidence;
10. do not promote or expand mechanisms from novelty alone.
