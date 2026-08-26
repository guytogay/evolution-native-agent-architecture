# ENA Reconstruction — Cardinality Distortion Audit

Date: 2026-08-26

Status: `RESEARCH_AUDIT / ANTI_DISTORTION / NOT_CURRENT`

Related: `CARDINALITY-DISCOVERY-GUARD.md`, `MECHANISM-RETENTION-LEDGER.md`, #89, #90, PR #82.

## Purpose

Audit active reconstruction/reference surfaces for counts that may have been accidentally promoted from presentation or current inventory into machine-enforced reality structure.

Core distinction:

```text
NORMATIVE_COUNT
OBSERVED_COUNT
PRESENTATION_COUNT
CONTROLLED_EXPERIMENT_COUNT
```

Only `NORMATIVE_COUNT` may constrain the underlying protocol/structure by definition.

`CONTROLLED_EXPERIMENT_COUNT` may be fixed for one benchmark version or isolation condition, but must not be narrated as ontology.

`OBSERVED_COUNT` and `PRESENTATION_COUNT` must not silently become ontology constraints.

---

## Finding C-01 — Finite-context adoption HOW count

**Prior state**

The active selftest registry stopped at HOW-A..D; Host-fit corpus asserted exactly 8 cases; preferred-winner coverage reflected the four-HOW inventory.

**Trigger**

DSH-like mature Host evidence did not fit HOW-D without distorting the Host phenotype. HOW-E Native Host Organ Rebind emerged.

**Classification**

`OBSERVED_COUNT incorrectly hardened into machine coverage assumptions`

**Repair**

- added HOW-E as a new reference behavior rather than forcing it into A-D;
- removed exact 8-case assertion;
- reduced synthetic corpus expectations to property coverage floors;
- marked the HOW registry as currently implemented test coverage, not ontology;
- workflow reports `HOW_CARDINALITY=OPEN`.

**Machine evidence**

Head `2d0f589ea17b6b3b47d026006318a7363e6f25be`, Finite Context Adoption Research run `32927153520`, job `98052250754`: PASS.

**Verdict**

`REAL_CARDINALITY_DISTORTION_FOUND_AND_REPAIRED`

---

## Finding C-02 — Distributed History Merge HOW/fixture count

**Prior state**

Current reference registry contained A-D; Host-fit selftest asserted exactly 8 cases and relatively high count-specific plurality floors; cross-HOW adversarial selftest asserted exactly 16 fixtures.

**Classification**

- A-D registry: `OBSERVED_CURRENT_IMPLEMENTATION_COUNT`;
- 8/16 corpus totals: `ACCIDENTAL_FIXED_COUNT`;
- two-parent merge of two known heads: `NORMATIVE_OPERATION_COUNT` for that operation.

**Repair**

- retained A-D as current executable coverage while declaring cardinality open;
- removed exact 8/16 total-count assertions;
- required non-empty/unique corpora and specific targeted regression IDs instead;
- reduced multi-fit/single-winner conditions to coverage floors rather than population claims;
- retained two-parent lineage assertion for the actual two-head merge case.

**Machine evidence**

Head `c6bfd3890436925dec0aeabe0dfdf28425bcca34`, Distributed History Merge Research run `32927677920`, job `98053720609`: PASS.

**Verdict**

`REAL_CARDINALITY_DISTORTION_FOUND_AND_REPAIRED`

---

## Finding C-03 — Contested Authorship regression corpus

**Prior state**

Selftest asserted exactly 18 fixtures.

**Classification**

`ACCIDENTAL_FIXED_REGRESSION_CORPUS_COUNT`

There is no authorship semantic requiring 18 cases.

**Repair**

Require:

- corpus non-empty;
- unique case IDs;
- targeted regression/control IDs remain present.

Allow additional cases without changing the ontology or breaking the selftest merely because the corpus grew.

**Verdict**

`REPAIRED`

---

## Finding C-04 — Effect Lifecycle regression corpus

**Prior state**

Selftest required exactly 18 unique cases.

**Classification**

`ACCIDENTAL_FIXED_REGRESSION_CORPUS_COUNT`

No lifecycle property makes 18 the natural fixture count.

**Repair**

Require non-empty corpus, unique IDs, and mutation/control dependencies `EL-001`, `EL-003`, `EL-008`, `EL-009`.

**Verdict**

`REPAIRED`

---

## Finding C-05 — Evidence Dependency Map regression corpus

**Prior state**

Selftest asserted exactly 16 fixtures.

**Classification**

`ACCIDENTAL_FIXED_REGRESSION_CORPUS_COUNT`

**Repair**

Require non-empty/unique corpus and targeted regression/control IDs, not total size.

**Verdict**

`REPAIRED`

---

## Finding C-06 — Evidence Envelope regression corpus

**Prior state**

Selftest asserted exactly 22 fixtures.

**Classification**

`ACCIDENTAL_FIXED_REGRESSION_CORPUS_COUNT`

**Repair**

Require non-empty/unique corpus and targeted regression IDs, not total size.

**Verdict**

`REPAIRED`

---

## Finding C-07 — Tiny Hot Kernel 36-case corpus

**Prior state**

Selftest asserted exactly 36 fixture rows and controlled comparison currently uses K-A/K-B/K-C.

**Initial suspicion**

Looks superficially identical to accidental exact-count locks.

**Protocol inspection**

The controlled evaluation intentionally holds the fixture corpus constant while varying the resident kernel. Therefore changing corpus membership silently between candidate runs would break comparability.

**Classification**

- 36 cases: `CONTROLLED_EXPERIMENT_COUNT / BENCHMARK_VERSION_IDENTITY`;
- one kernel file per packet: `NORMATIVE_EXPERIMENTAL_ISOLATION_COUNT`;
- K-A/K-B/K-C: `CURRENTLY_SELECTED_EXPERIMENT_CANDIDATES`, not closed recognizer ontology.

**Repair**

Do **not** remove the 36-case control. Instead:

- rename it `CONTROLLED_CORPUS_VERSION_COUNT`;
- explicitly state that changing it changes the benchmark corpus version/condition;
- declare `CONTROLLED_CORPUS_COUNT_IS_NOT_ONTOLOGY`;
- declare kernel candidate cardinality open outside the benchmark version;
- keep exactly one kernel per packet because that is an isolation rule, not slot-filling.

**Verdict**

`FIXED_COUNT_JUSTIFIED_AFTER_CLASSIFICATION`

This is an important negative control for the audit: cardinality guard must not become a rule that blindly removes all numbers.

---

## Finding C-08 — Memory Metabolism 0.6 / Retrieval Obligation 0.5

**Inspection**

Current active selftests dynamically increment and print executed test counts but do not assert that the corpus/ontology must contain exactly N cases.

**Classification**

`NO_ACCIDENTAL_CARDINALITY_LOCK_FOUND_IN_INSPECTED_SELFTESTS`

**Verdict**

`NO_CHANGE`

---

# General machine-test rule

Prefer:

```text
required semantic property holds
required regression dependency exists
IDs are unique
at least one case exercises behavior X
```

over:

```text
there must be exactly N cases
there must be exactly N HOWs
all currently named categories must each win once
```

unless N is part of the protocol, state machine, benchmark version, or controlled experimental isolation.

## Coverage floor != ontology count

For example:

```text
multi_fit >= 1
single_winner >= 1
```

may be a useful synthetic test coverage floor.

It does **not** claim that reality contains one or any fixed number of such classes.

## Frozen history boundary

Do not retroactively rewrite historical/frozen experimental artifacts merely because their old corpus used a fixed count. Preserve occurrence truth.

Apply the guard to active reference/validator surfaces and clearly classify historical counts when they are consulted.

# Audit conclusion

Cardinality distortion was not hypothetical. Several active selftests had converted current corpus/inventory size into a machine rejection condition.

The correction is not `remove numbers`.

The correction is:

> **Make every enforced number answer what gives that number authority.**

If the answer is merely `because that is how many we happened to have when the test was written`, treat it as suspect.

`CARDINALITY_DISCOVERY = ACTIVE`

`NUMERIC_ASSERTION_REQUIRES_AUTHORITY = YES`

`BENCHMARK_CARDINALITY != ONTOLOGY_CARDINALITY`

`CURRENT_MUTATION = NO`
