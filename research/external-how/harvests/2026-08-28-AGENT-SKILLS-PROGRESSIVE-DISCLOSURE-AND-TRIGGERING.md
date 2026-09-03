# External HOW Harvest — Agent Skills Progressive Disclosure and Triggering

Date: 2026-08-28

Status: `EXTERNAL_HOW_HARVEST / HOST_BINDING_REFERENCE / FIELD_TEST_INPUT / CURRENT_UNCHANGED / NOT_SELECTION`

Related: #90, #150, `releases/current/RUNTIME-ADOPTION-KERNEL.md`, `releases/current/operational/CUE-INDEX.md`, `releases/current/operational/HOW-MAP.md` OA-RT-01 / OA-RET-01.

## Research question

Can a mature skills-compatible Host provide a concrete realization of ENA v0.3.7's intended runtime shape:

```text
compact hot cue surface
-> natural relevance recognition
-> cold HOW retrieval
-> deeper reference retrieval only when needed
-> application with freshness/sufficiency boundaries
```

without permanently loading the full Operational Architecture?

This harvest searches for mechanism patterns and field-test failure shapes, not a framework winner.

---

## HOW family A — Agent Skills three-level progressive disclosure

Source class: `OPEN_AGENT_SKILLS_STANDARD / OFFICIAL_VENDOR_DOCUMENTATION`

Sources:

- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- https://github.com/agentskills/agentskills/blob/main/docs/home.mdx
- https://github.com/agentskills/agentskills/blob/main/docs/client-implementation/adding-skills-support.mdx
- https://help.openai.com/en/articles/20001066
- https://openai.com/academy/skills/

Observed mechanism:

```text
startup discovery
  -> only skill name + description are disclosed

relevance/activation
  -> full SKILL.md is loaded when the task appears relevant

execution/deeper retrieval
  -> referenced files/scripts/resources are loaded only as needed
```

Anthropic describes progressive disclosure as the core context-management principle of Agent Skills. The open Agent Skills implementation guidance likewise says a client should disclose the skill catalog without loading full instructions, then allow activation by reading the selected `SKILL.md`. OpenAI's current Skills surfaces use the same reusable workflow / automatic-use model and support the Agent Skills format in Codex/API-facing workflows.

### ENA mapping

This is not a missing Core organ. It is a strong Host-native realization of existing v0.3.7 OA-RT-01:

```text
ENA Runtime Adoption Kernel / cue descriptor
~= skill discovery metadata

CUE-INDEX / HOW-MAP branch
~= selected SKILL.md body

procedure / reference / Host detail
~= deeper skill reference/resource
```

The structural fit is unusually close to ENA's released statement:

```text
internalize the cues; retrieve the HOW
```

Disposition: `HIGH_VALUE_HOST_BINDING_HOW / NO_CURRENT_CHANGE`.

---

## HOW family B — Description-driven trigger routing

Source class: `OPEN_STANDARD_GUIDANCE`

Source:

- https://github.com/agentskills/agentskills/blob/main/docs/skill-creation/optimizing-descriptions.mdx

Observed mechanism:

The skill `description` carries most of the initial routing burden. Under-specified descriptions cause false negatives; over-broad descriptions cause false positives. Current guidance recommends describing user intent rather than internal implementation and testing realistic positive/negative trigger queries, especially near-misses.

### ENA mapping

This turns a vague field question — "will a cue become salient?" — into a concrete Host-binding question:

```text
HOT_DESCRIPTOR_QUALITY
-> retrieval trigger behavior
```

For an ENA Agent-Skills adapter, the descriptor should encode **ordinary problem/failure cues**, not ENA jargon alone. A descriptor that says only "Use ENA for ENA tasks" would make the evaluation trivial and would not test natural cue salience.

Important distinction:

```text
DESCRIPTION_MATCH
!= APPLICABILITY_PROVEN
!= CORRECT_HOW_SELECTED
!= HOW_APPLIED
```

Disposition: `FIELD_TESTABLE_TRIGGER_HOW`.

---

## HOW family C — Real execution trace as trigger evidence

Source class: `OPEN_STANDARD_GUIDANCE`

Sources:

- https://github.com/agentskills/agentskills/blob/main/docs/skill-creation/optimizing-descriptions.mdx
- https://github.com/agentskills/agentskills/blob/main/docs/skill-creation/best-practices.mdx

Observed mechanism:

Skill evaluation guidance recommends observing whether the agent actually loads/invokes the skill and inspecting execution traces, not grading only the final answer. It also recommends realistic positive and near-miss negative tasks.

### ENA mapping

This fits ENA's evidence ladder:

```text
skill exists                  = WRITTEN/AVAILABLE
skill descriptor disclosed    = LOADED_DISCOVERY_METADATA
SKILL.md read                 = RETRIEVED/LOADED_HOW
correct branch interpreted    = INTERPRETED
cue caused timely use         = SALIENT
procedure affected behavior   = APPLIED
```

A final answer that happens to be good without consulting the cold HOW is **not** evidence that ENA's routing mechanism worked.

Disposition: `HIGH_VALUE_FIELD_EVIDENCE_METHOD`.

---

## Failure shape D — Deep-reference stale-cache / no re-read

Source class: `OPEN_STANDARD_COMMUNITY_IMPLEMENTATION_REPORT`

Source:

- https://github.com/agentskills/agentskills/issues/97

Observed failure:

A reported implementation pattern treated a referenced file as effectively "already read" and did not re-read it when later context required a different section/current content.

### ENA mapping

This is a direct Retrieval Obligation failure:

```text
REFERENCE_PREVIOUSLY_READ
!= RELEVANT_BYTES_CURRENTLY_LOADED
!= CURRENT_SUFFICIENCY
```

A skills-compatible Host can implement progressive disclosure while still failing ENA's freshness/sufficiency boundary.

Disposition: `DECISION_DISTINCT_FIELD_FAILURE_SHAPE`.

---

## Failure shape E — Progressive disclosure collapses below SKILL.md

Source class: `OPEN_STANDARD_COMMUNITY_DESIGN_GAP`

Sources:

- https://github.com/agentskills/agentskills/issues/112
- https://github.com/agentskills/agentskills/discussions/162
- https://github.com/agentskills/agentskills/issues/53

Observed failure/question:

A lean `SKILL.md` can still reference large sub-files that are loaded wholesale. Community proposals ask for another descriptor layer on sub-files/references so progressive disclosure can continue at finer granularity, including tool/instruction files.

### ENA mapping

This exposes a second-order context-economics boundary:

```text
HOT_INDEX_SMALL
+ SKILL_TRIGGER_CORRECT
!= TOTAL_RETRIEVAL_COST_BOUNDED
```

ENA should therefore observe not only whether cold retrieval occurs, but **how much unrelated cold material becomes hot after activation**.

Disposition: `FIELD_COST_FAILURE_SHAPE / NO_UNIVERSAL_TIER_COUNT`.

---

## Preliminary comparison with v0.3.7

| External mechanism/failure | Existing ENA node | Gap class |
|---|---|---|
| skill metadata -> full skill progressive disclosure | OA-RT-01 | Host binding, not missing semantics |
| description-driven trigger | Runtime Kernel cues / CUE-INDEX | natural salience remains field evidence |
| execution-trace trigger eval | #150 field evidence | evidence method |
| stale cached reference | OA-RET-01 | freshness/sufficiency Host failure |
| coarse sub-file loading | OA-RT-01 + operational economics | retrieval-cost Host failure |

No new Core property is established by this harvest.

---

## Candidate Host adapter

A research-only adapter can package ENA's runtime router as an Agent Skill:

```text
SKILL metadata
  -> ordinary problem/failure cues only

SKILL body
  -> ENA lightweight pre-router
  -> pointer to exact Current RUNTIME-ADOPTION-KERNEL / CUE-INDEX / HOW-MAP

references
  -> load only the exact selected Operational HOW/procedure/reference needed
```

The adapter must not copy the entire 118-file Current into one always-loaded skill body. It should point to immutable Current paths/identity and preserve the distinction:

```text
HOST_ADAPTER != ENA_CURRENT
```

---

## Field-test questions that can change a decision

1. **Natural positive cue:** Does a realistic prompt that never says "ENA" cause the Host to load the ENA runtime-router skill when the cold HOW would materially help?
2. **Near-miss negative cue:** Does the skill remain cold when the prompt shares words but the consequence/decision boundary makes ENA unnecessary?
3. **Correct branch:** After activation, does the Host retrieve the relevant CUE/HOW branch rather than simply load the skill and improvise?
4. **Freshness:** If a deeper reference was read earlier and later changes or a different section becomes material, does the Host re-resolve current required content rather than rely on path-level cache memory?
5. **Granularity:** How much unrelated cold material is loaded after activation?
6. **False-BLOCK:** Does the adapter preserve `NOT_REQUIRED / NOT_APPLICABLE / lightweight` outcomes rather than triggering ceremony whenever the skill activates?
7. **Evidence layer:** Can traces distinguish `discovered -> activated -> loaded -> interpreted -> applied`, instead of inferring routing from final prose?

These answers are not honestly derivable from static ENA bytes alone. A fresh skills-compatible Host run can therefore pay epistemic rent.

## Current disposition

`EXTERNAL_HOW_SPACE_EXPANDED = YES`

`MISSING_CORE_ORGAN = NO`

`AGENT_SKILLS_HOST_ADAPTER_JUSTIFIED = YES`

`FRESH_HOST_TRIGGER_TEST_JUSTIFIED = YES`

`CURRENT_CHANGE = NO`

Next: build a research-only Agent Skills-compatible runtime-router adapter and a small realistic trigger/freshness evaluation surface. Do not execute the natural-salience test in the already-primed project-manager session and do not treat trigger-rate counts as architecture truth.