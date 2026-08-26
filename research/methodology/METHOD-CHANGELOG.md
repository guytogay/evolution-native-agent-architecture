# ENA Research Methodology Changelog

Status: `DURABLE_METHOD_LINEAGE / OPEN_CARDINALITY / NON_NORMATIVE_TO_CURRENT`

Purpose: preserve **why the research method changed**, not merely the latest wording.

A methodology change should be recorded when a concrete research failure, field observation, tool limitation, or reasoning defect materially changes how future ENA research should be conducted.

Do not record every wording edit. Record decision-changing method evolution.

---

## 2026-08-26 — Anti-dissolution / operational architecture correction

Trigger:

- post-v0.3.6 reconciliation repeatedly treated parent semantic coverage as closure of practical engineering questions;
- concrete reference organs and Host adapters were at risk of disappearing from the active research map.

Admitted method:

```text
PROPERTY != ORGAN != HOST_BINDING != EVIDENCE != ADOPTION
WHAT -> WHY -> HOW -> EVIDENCE
```

`CURRENT_ALREADY_COVERS_PARENT_PROPERTY != PRACTICAL_PROBLEM_SOLVED`.

Related durable state: #88, #89.

---

## 2026-08-26 — HOW growth / tree-branching correction

Trigger:

- semantic compression methods useful for the Core were being applied to implementation HOWs;
- plural Host-specific realizations were being compressed into parent principles.

Admitted method:

> **Compress WHAT. Grow HOW. Select by evidence.**

> **Compress the semantic trunk; let concrete HOWs branch.**

```text
ONE_WHAT_WHY -> 0..N_CONCRETE_HOW_BRANCHES
LOCAL_HOW_WINNER != UNIVERSAL_HOW_WINNER
```

External mature mechanisms should be harvested as candidate HOWs instead of requiring ENA to invent every organ from scratch.

Canonical file: `HOW-GROWTH-DISCIPLINE.md`.

---

## 2026-08-26 — Cardinality discovery / anti-pseudo-precision correction

Trigger:

- prompts and fixtures were freezing current inventories into fixed architecture counts;
- arbitrary numeric thresholds risked manufacturing scientific appearance without domain authority.

Admitted method:

```text
REQUESTED_N != DISCOVERED_N
PRESENTATION_N != ONTOLOGY_N
CURRENTLY_OBSERVED_N != FINAL_N
COUNTABLE != SHOULD_BE_QUANTIFIED
N_OUTPUTS != N_INDEPENDENT_SUPPORTS
```

Canonical file: `CARDINALITY-DISCOVERY-GUARD.md`.

---

## 2026-08-26 — Experiment epistemic-rent correction

Trigger:

- proposed multi-model/agent experiments had outcome spaces largely derivable before execution;
- model diversity itself risked being misreported as discovery.

Admitted method:

> **Experiments must pay epistemic rent.**

Prefer static/state-space reasoning and deterministic adversarial fixtures for already reachable bugs. Use experiments where reality can reveal unknown interaction, thresholds, adaptation, emergence, or counterexamples.

Canonical ledger: `ENA-RESEARCH-DISCIPLINE.md`.

---

## 2026-08-26 — Session inheritance activation correction

Trigger:

- a successor session had access to both prior discussion and durable GitHub state but still regressed into selection-induced ablation;
- the old cross-session collaboration file was stale and hard-coded an obsolete Current version;
- methodology was persisted but insufficiently routed/salient.

Admitted method:

```text
DURABLE != DISCOVERABLE
DISCOVERABLE != RETRIEVED
RETRIEVED != SALIENT
SALIENT != APPLIED
```

A research method needs its own runtime adoption path.

Corrective surfaces:

- `research/RESEARCH-START-HERE.md`;
- `SESSION-CONTINUITY-AND-COLLABORATION.md`;
- `research/incidents/SESSION-INHERITANCE-GAP-2026-08-26.md`.

---

## Future entries

Append new entries when research practice materially changes. Preserve superseded methods and the reason they changed; do not silently rewrite the changelog to make the current method appear timeless.
