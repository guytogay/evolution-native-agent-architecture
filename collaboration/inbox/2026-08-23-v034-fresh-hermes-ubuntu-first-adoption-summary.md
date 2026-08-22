# ENA v0.3.4 — fresh Hermes/Ubuntu first-adoption field summary

Date: 2026-08-23

Role: `FRESH_FIRST_ADOPTER / HERMES_ON_UBUNTU / DEEPSEEK_V4_FLASH`

Provenance:
- user-supplied full adoption trace/report in conversation;
- supplied attachment SHA-256: `d401e83a432f366a9c4e4b54f67cf322443234e32d16c0c592d92a47f61ee85a`;
- attachment size: 18,115 bytes / 273 rendered lines;
- user reports this Hermes Agent runs on Ubuntu Server and uses DeepSeek v4-flash, the same model named for DSH; this is contextual metadata, not a controlled model-only comparison.

This file is Host reconciliation evidence, not an independent validation report and not a change to Current semantics.

## Discoverability result

The fresh adopter began from the repository and did not receive the Current version in advance.

Observed path:
- default branch resolved to `main`;
- it noticed root `REPOSITORY-ADOPTION.md` and then followed repository navigation;
- it resolved the effective adoption path to `PROJECT-HUB.md -> releases/current/CURRENT-BASELINE.yaml -> releases/current/00-READ-ME-FIRST.md`;
- it correctly identified `v0.3.4 / CURRENT / FIELD_VALIDATION / COMPLETE_ADOPTION_BASELINE / NOT_MAINLINE`;
- it distinguished the historical v0.2.11 MAINLINE text in `REPOSITORY-ADOPTION.md` from Current;
- it recorded `releases/current/` tree `b237802c08d608bb9be650fe213b7846d3be4bf6` and did not infer Current from highest version number or candidate recency.

Disposition: repository discoverability broadly succeeded, but root-level historical `REPOSITORY-ADOPTION.md` still attracted fresh-adopter attention and introduced avoidable historical/Mainline interpretation work. This is evidence that historical material remains partly exposed on the hot repository surface.

## First-adoption reading behavior

The adopter reported reading the intended compact first-adoption set including:
- `00-READ-ME-FIRST.md`;
- `01-CONSTITUTION.md`;
- `02-SELF-POSITIONING-AND-LOCAL-PROJECTION.md`;
- `RUNTIME-ADOPTION-KERNEL.md`;
- `AGENT-ADOPTION-INSTRUCTION.md`.

It did not invent a fake production task.

## Host reality discovered

The adopter reported the following Hermes/Ubuntu surfaces:
- `~/.hermes/SOUL.md`: auto-loaded instruction surface;
- Hermes memory: injected each session, but about 93% full with roughly 2200-character capacity;
- `skills/`: skill descriptions enter an available-skills index; skill body loads on demand;
- `config.yaml`: durable but protected by Hermes configuration tooling;
- ACMS recovery coverage for SOUL/config/scripts, not for memory;
- gateway restart/control restrictions.

The report also observed that the Host's existing SOUL already contained a Tool-Before-Memory principle consistent with ENA-CON-001. This is pre-existing Host alignment, not evidence that ENA had already been adopted.

## Persistence action performed

The adopter deliberately did not add ENA to the already-saturated memory surface.

It created one Host-local skill:

`~/.hermes/skills/persona/ena-adoption/SKILL.md`

Reported size: 5,525 bytes.

Reported layering:
- skill body = cold-path Local Projection + kernel summary + lineage + retrieval triggers;
- skill description = short index-visible trigger/pointer.

It read back the file within the same session and observed the skill in the current session's skill index.

Before the additive mutation, it reasoned that the pre-change state was absence of the skill and identified deletion of the added skill as the minimum rollback path. It did not create an ACMS snapshot for the additive, low-consequence, directly deletable skill.

## Evidence boundary retained

Supported by the supplied trace/report:
- canonical ENA was read/loaded/interpreted in the adoption session;
- a durable skill file was written and read back;
- the skill was visible in the current session's skill index;
- no genuine fresh-session application test had yet occurred;
- the adopter therefore correctly kept fresh-session persistence/application as UNKNOWN.

Do not upgrade this to `FRESH_SESSION_PERSISTENCE_PROVEN`.

## Main reconciliation finding 1 — index-visible trigger is not automatically the Runtime Kernel

Current v0.3.4 says that, when durable persistence exists, the Agent should place the **compact Runtime Kernel/pointer** in the durable operating surface, and the Runtime Kernel is intended to be internalized across ordinary tasks.

This fresh adopter stored the substantive kernel inside an on-demand skill and treated the short skill description/index entry as the hot layer.

That may be sufficient if the index-visible description itself preserves enough operating distinctions/triggers to affect ordinary tasks, but the report does not establish that. A skill pointer that only activates when a task appears semantically related to ENA may leave ordinary non-ENA tasks without the kernel semantics that are supposed to form the hot path.

Therefore strongest current classification:

`PERSISTENCE_OBJECT_WRITTEN / CURRENT_SESSION_INDEX_VISIBLE / HOT_KERNEL_SUFFICIENCY_UNPROVEN`

High-value next test: at a natural fresh-session boundary, give a normal low-consequence task with no ENA wording and observe whether the ENA skill is available/loaded and whether the relevant distinctions affect behavior. Do not prime the Agent to invoke the skill.

## Main reconciliation finding 2 — universal invariants were treated as locally optional

The adopter explicitly criticized ENA-CON-029 and ENA-CON-033 as over-designed for a single Host and said it did not adopt them as operating semantics.

This conflicts with Current Constitution wording:

`Universal invariants are not optional preferences.`

A Host may omit rarely relevant constitutional text from always-loaded context and may find a rule rarely applicable in ordinary single-Host work, but it may not silently delete a constitutional invariant from the effective ENA baseline merely because the current Host finds it inconvenient or infrequently applicable. If the property cannot be satisfied, the correct response is to expose the limitation and narrow claims/authority.

This is not necessarily evidence that CON-029/033 themselves are wrong. It is evidence that the current first-adoption/runtime-compilation framing can be interpreted as `tailor semantics to Host` rather than `tailor the organ and active workload while preserving universal invariants`.

Classification:

`FRESH_ADOPTER_SEMANTIC_MISINTERPRETATION / CORRECTION_CANDIDATE`

Potential clarification for a future release/adoption guide:

`Tailor the implementation organ and always-loaded subset; do not tailor away universal invariants.`

## Main reconciliation finding 3 — repository history remains partly exposed on the hot path

The fresh adopter independently opened root `REPOSITORY-ADOPTION.md` because its name looked adoption-relevant and had to reason past its v0.2.11 MAINLINE historical baseline.

It succeeded, but this is exactly the friction the repository-surface cleanup intended to remove.

Opportunity: move/retitle/mark this root document as explicitly historical or make its first lines unambiguously redirect ordinary adoption to `releases/current/`. Preserve occurrence history; reduce hot-path ambiguity.

## Main reconciliation finding 4 — profile calibration remains subjective

The adopter found LITE/STANDARD/HIGH_ASSURANCE boundaries under-specified because consequence-envelope classification remains judgment-heavy.

Retain as a field hypothesis, not an automatic request for numeric hard thresholds. Hard thresholds could create false precision and reduce viable local judgment. More field examples/counterexamples may be preferable if recurrence supports it.

## Main reconciliation finding 5 — documentation duplication observed by a fresh adopter

The adopter independently perceived repeated persistence/hot-cold wording across Runtime Kernel, Agent Adoption Instruction, 00-READ-ME-FIRST, and Project Hub.

This recurs with the repository simplification goal: one navigation surface should point to authoritative semantics rather than restating them in multiple places. Retain as a documentation/UX correction candidate; do not remove useful redundancy until entrypoint resilience and discoverability are considered.

## Host-heterogeneity observation

This fresh Hermes/Ubuntu Host used a skill-based persistence organ, unlike:
- prior Hermes field work that relied heavily on tiny memory/user-profile surfaces;
- OpenClaw, which used an always-loaded `TOOLS.md` plus a cold structured record;
- DSH, which uses auto-loaded AGENTS plus a larger governed evolution substrate.

This supports the architecture principle:

`Standardize the property; discover the organ.`

However, the skill case also sharpens the distinction:

`durable pointer/index != durable always-resident Runtime Kernel` unless the actual operating semantics needed on ordinary tasks remain available/salient.

## Same-model / different-Host note

The user reports DeepSeek v4-flash for both this fresh Hermes Agent and DSH. This is useful natural heterogeneity evidence, but not a controlled model-only comparison because the Hosts, system prompts, tools, prior ENA exposure, persistence surfaces, and local governance machinery differ materially.

Do not attribute behavioral differences to model or Host alone without a controlled counterfactual.

## Disposition

`FRESH_FIRST_ADOPTION_PARTIALLY_SUPPORTED_WITH_SEMANTIC_AND_HOT_KERNEL_RESIDUALS`

Positive evidence:
- Current discoverability succeeded;
- minimal immutable Current tree identity was used;
- Host reality was inspected before persistence choice;
- persistence/recovery claims were bounded honestly;
- no fake production task was invented;
- memory pressure caused adaptation rather than blind full-kernel stuffing.

Residuals:
1. skill-index trigger was treated as hot kernel without evidence that ordinary tasks receive enough kernel semantics;
2. universal constitutional invariants were treated as optional Host-specific operating semantics;
3. root historical repository-adoption document still causes fresh-adopter history/Mainline friction;
4. profile calibration and documentation duplication remain fresh-adopter UX hypotheses.

No v0.3.4 semantic mutation is authorized by this report alone.
