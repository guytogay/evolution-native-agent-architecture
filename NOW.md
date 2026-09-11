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

`96c021ecff39145997be13008d76eb009910797d`

Direct adopter path remains:

```text
FIRST-USE.md
→ A2A.md
→ SURVIVAL.md
→ SAFE-CHANGE.md
→ EVOLUTION.md
→ SLEEP-DREAM-QUICKSTART.md
```

## 2026-09-12 external field-readiness review

A Grok review was treated as decision-changing product feedback rather than commentary.

Accepted corrections:

1. **Reading is not installation.** `tools/ena_preflight.py` now provides a startup/session gate: missing ENA files, incomplete minimum First Use, missing real recovery/rescuer, or stale `SYSTEM.yaml` returns `REFRESH REQUIRED`. README explicitly says acknowledgement/summary does not install a capability.
2. **Two Host profiles.** `SURVIVAL.md` and `SAFE-CHANGE.md` now distinguish resident runtimes from session/coding Agents. Resident Agents may use supervisor + timed rollback; session Agents may use Git/worktree/backup + new session/human recovery. Do not force daemon semantics onto conversational/coding sessions.
3. **Human rescue is first-class.** A2A remains useful where supported but is not a universal installation/safe-change gate. A human or Host-native recovery mechanism may be the selected recovery actor.
4. **First Use is minimum-first.** Unknown facts may remain `UNKNOWN`. Minimum readiness requires confirmed shared settings, one real recovery path, one rescuer, and `ENA.yaml` + freshness-aware `SYSTEM.yaml`.
5. **SYSTEM expires.** `SYSTEM.yaml` now carries `checked_at`, `valid_until`, and `minimum_ready`; consequential self-change rechecks the specific mutable recovery facts it depends on even before global expiry.
6. **No author environment defaults.** Adopter examples no longer present `Asia/Shanghai` / `zh-CN` as product defaults. First Use detects/hints then asks the user to confirm.
7. **Sleep/Dream is explicitly experimental.** Counts, weights, distance bands and cadence are field parameters rather than ENA requirements. Negative/null results are evidence; do not add new Dream modes/sampler complexity without field evidence that the current paths systematically fail.
8. **Speculative isolation is stronger.** New generated candidates live under `evolution/candidates/speculative/`; `tools/candidate_record.py` always writes `truth_status: speculative`. Selected outcomes are recorded separately after reality contact; Dream never directly becomes factual memory.
9. **CI is not field evidence.** ENA Issue #14 now requires one fresh-Agent real runtime chain: First Use → real recovery path → one bounded Safe Change → one evidenced evolution outcome → new session/restart can read persisted state.
10. **Repository relationship is explicit.** New adopters are directed to `guytogay/ENA`; the older repository is described as previous release/research/history, not the install path for the clean product.

Not adopted literally:

- Do **not** archive `evolution-native-agent-architecture` yet. It still carries legacy Current, evidence/history, Issue #208 and maintainer succession. Revisit archival after the clean product has enough field evidence and transition authority no longer depends on this repo.

## Current product evidence state

Reference-tool CI passed for PR #15 before merge. This proves only that the reference tools execute against included examples.

It does **not** prove the product works on a real Host.

Field evidence now has two explicit streams:

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
- do not let Sleep/Dream experimental parameters harden into doctrine without field evidence.

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

1. run ENA Issue #14 on at least one real session/coding Agent Host and one resident Host when practical;
2. confirm `ena_preflight.py` can actually be integrated into a session/startup hook rather than merely invoked manually;
3. collect Sleep/Dream evidence in Issue #12 only after the basic runtime chain works;
4. iterate from concrete friction, failure, null and recovery evidence;
5. do not promote or expand mechanisms from novelty alone.
