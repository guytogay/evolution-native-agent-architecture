# ENA — NOW

This is the default live project-status surface for ENA work.

Keep it short. Git history stores history; Issues store open work; CI stores machine-known execution facts.

## Current adoption baseline

- Current at this exact moment: `v0.3.7 / CURRENT / FIELD_VALIDATION`
- Adoption authority: `releases/current/CURRENT-BASELINE.yaml`
- Effective adopter-facing package: `releases/current/`
- v0.3.7 is a rollback/history anchor, not a target to keep Current on.

## Release posture changed — rapid Current succession

ENA now separates **version immutability** from **Current mobility**.

```text
IMMUTABLE_VERSION != IMMOBILE_CURRENT
PRESERVE_OLD_RELEASES + MOVE_CURRENT_QUICKLY
```

Project method:

`research/methodology/RAPID-CURRENT-RELEASE-DISCIPLINE.md`

Release validation is risk-tiered:

- `R0 FIELD_PATCH / ADOPTION_SURFACE` — machine regression + exact package/readback + rollback anchor; fresh independent validation may occur after admission;
- `R1 OPERATIONAL_BEHAVIOR_CHANGE` — targeted adversarial/independent evidence when decision-material;
- `R2 CORE_SEMANTIC / HIGH_CONSEQUENCE` — heavy freeze + fresh independent falsification/reconciliation by default.

Open research is not a release blocker unless the successor actually depends on it.

## Active successor — v0.3.8

**v0.3.8-candidate.0 is classified `R0_FIELD_PATCH_ADOPTION_SURFACE`.**

Working branch:

`candidate/v0.3.8-candidate.0`

PR:

`#202 — v0.3.8 candidate.0 — consolidate adopter/product surface`

Primary evidence:

- Issue `#201` — post-release narration drift, zh-CN hot-surface fidelity gaps, concept-map retrieval misfit, fixture gaps, plus positive v0.3.7 tool/routing verification;
- adoption feedback that research lineage and adopter payload are too easy to conflate, and model guidance vs hard/system enforcement needs to be explicit.

Candidate thesis:

```text
RESEARCH LINEAGE != ADOPTION PAYLOAD
SEMANTIC PRECISION != PRESENTATION_VERBOSITY
SOFT_GUIDANCE != HARD_ENFORCEMENT
```

Candidate.0 includes:

- product-first human and Agent entry surfaces;
- machine-readable `ENFORCEMENT-MAP.yaml` with `MODEL_CUE / MACHINE_GUARD / EXTERNAL_CONTROL_REQUIRED / FIELD_EVIDENCE_REQUIRED`;
- repaired zh-CN hot-surface guardrails;
- CON-035 / CON-008 / CON-028 concept-map retrieval repairs;
- semantic-fixture v3 expansion from 12 to 18 cases;
- candidate adoption-surface validator wired into Main Gate;
- exact regression binding for inherited Constitution 01–04 and key machine paths.

Latest candidate Main Gate and CodeQL are PASS. No new Constitution ID and no core contract semantic delta are demonstrated.

**Fresh cleanroom validation is no longer a mandatory pre-release gate for this R0 successor.** Post-admission field evidence can trigger a rapid v0.3.9 if needed.

## Exact release next action

`PROMOTE_V038_THROUGH_R0_RAPID_CURRENT_LANE`

Required remaining work is bounded:

1. merge the candidate package to main as reviewable successor cargo;
2. create exact v0.3.8 release projection;
3. run release/package/regression checks;
4. verify v0.3.7 rollback/history remains recoverable;
5. move `releases/current/` to v0.3.8 under a new immutable version identity;
6. read back the exact promoted Current and continue field validation.

Metamemory research does **not** block v0.3.8.

## Research state

The evolutionary-memory campaign is closing rather than expanding into one experiment per remaining metaphor/mechanism.

Closure dispositions:

`research/evolution-inbox/EVOLUTIONARY-MEMORY-CLOSURE-DISPOSITIONS.yaml`

Closure audit:

`research/field-validation/2026-09-06-evolutionary-memory-open-track-closure-audit.md`

Negative/null results count. Silent disappearance does not.

## Active mechanism experiment

**Metamemory Update Policy v1 remains preregistered and frozen; primary collection has not started.**

Preregistration:

`research/field-validation/2026-09-04-metamemory-update-policy-preregistration.md`

Fixture:

`research/field-validation/fixtures/metamemory-update-policy-v1/`

Primary launch bundle:

`research/field-validation/metamemory-update-policy-v1/PRIMARY-LAUNCH-BUNDLE.md`

Arms:

```text
S0 — STATIC_EQUAL
G1 — GLOBAL_RECENT3
C1 — CONTEXT_RECENT3
C2 — CONTEXT_REVERSIBLE3
```

Initial sample remains four one-shot fresh Temporary Chats. A frozen trigger may replicate all four arms once; maximum eight. No selective extra runs.

Research next action:

`COLLECT_METAMEMORY_UPDATE_POLICY_V1_INITIAL_PRIMARY`

This is the only currently planned fresh-session primary mechanism round. After formal adjudication, close the campaign unless it exposes a genuinely new non-derivable discriminator.

## Admission / evolution rules

```text
SAME_VERSION -> SAME_EFFECTIVE_CONTENT
NEW_BETTER_SUCCESSOR -> MOVE_CURRENT
OPEN_RESEARCH != RELEASE_BLOCKER_BY_DEFAULT
INTERESTING_RESULT != NEW_NATURAL_LAW
NO_NEW_NATURAL_LAW != NO_PRODUCT_SUCCESSOR_NEEDED
GOVERNANCE_MUST_PAY_RENT
```

## Related repositories

- `guytogay/evolution-native-agent-architecture` — ENA theory/mechanisms, Current semantics, candidates and evidence.
- `guytogay/human-ai-workbench` — reusable Human-AI project-working method.
- `guytogay/ena-field-guide` — evidence-backed practical ENA HOW.

## Current open work

- #150 — v0.3.7 field validation / predecessor reality-contact evidence
- #153 — simplify ENA project operations based on actual use
- #201 — adopter-facing findings driving v0.3.8
- #202 — v0.3.8 successor PR
