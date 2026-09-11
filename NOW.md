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

`c9479425bd3aa6713674dc142c2c2fe9cebc1dc2`

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

`FIRST-USE.md` now permits non-interactive adoption when timezone, language, ENA home, Host profile, recovery path and rescuer were already supplied by a trusted deployment/workspace policy or Host integration.

Important boundary:

- unattended mode does **not** introduce ENA product defaults;
- a missing value remains unresolved rather than guessed;
- `tools/ena_init.py` accepts caller-provided `--host-profile`, `--recovery`, `--rescuer`, and `--rescuer-type`;
- `--verified-minimum` is explicit and only valid when the caller/integration already verified the supplied recovery/rescue facts;
- `ena_preflight.py` remains the startup/session gate after initialization.

### Session/coding Agent Git example

The product now includes:

`examples/change/SESSION-GIT-WORKTREE.md`

It gives a concrete safe-change path:

```text
record known-good base commit
→ create isolated change branch + worktree
→ make/test one bounded commit
→ prepare exact recovery before application
→ apply only with git merge --ff-only
→ verify useful operation
→ retain or recover with git revert
```

The example explicitly avoids blind `git reset --hard` over later valid history. A conflict during revert stops for human/new-session inspection rather than forcing destructive cleanup.

This is an implementation example for the existing `session` Host profile, not a new ENA subsystem.

## Current product evidence state

Reference-tool CI passed for PR #16 before merge. This proves only that the updated reference tools—including caller-verified preset initialization—execute against included examples.

It still does **not** prove the product works on a real Host.

Field evidence remains:

- ENA Issue #12 — Sleep/Dream field feedback, including negative/null results and parameter evidence;
- ENA Issue #14 — minimum fresh-Agent runtime-chain proof.

Do not claim field validation from smoke tests, documentation review, or an Agent saying the design looks correct.

## Product boundary

Still binding:

- ENA adds capabilities/infrastructure reasoning alone does not provide;
- do not rebuild ordinary model judgment as ENA machinery;
- owner/maintainer explanations are project context unless they independently help an adopter act;
- legacy ENA is evidence/regression/omission-checking material, not the new product blueprint;
- do not re-import old structure, terminology, handoff machinery or closed research merely because it exists;
- do not let Sleep/Dream experimental parameters harden into doctrine without field evidence;
- unattended adoption may consume trusted policy, but may not manufacture missing policy through guessed defaults.

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

1. run ENA Issue #14 on at least one real session/coding Agent Host using the new Git/worktree example where appropriate;
2. also run a resident Host when practical;
3. confirm `ena_preflight.py` can actually be integrated into a session/startup hook or trusted unattended deployment flow rather than merely invoked manually;
4. collect Sleep/Dream evidence in Issue #12 only after the basic runtime chain works;
5. iterate from concrete friction, failure, null and recovery evidence;
6. do not promote or expand mechanisms from novelty alone.
