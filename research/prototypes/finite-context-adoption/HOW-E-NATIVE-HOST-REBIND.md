# HOW-E — Native Host Organ Rebind / Mapping-Only Adoption

Status: `REFERENCE_HOW / RESEARCH_ONLY`

## Host fit

Use this HOW when a mature Host already has concrete organs that realize the relevant ENA properties and adopting a new ENA Current mainly requires **semantic rebinding**, not replacement or duplication of working machinery.

Typical Hosts:

- mature long-lived Agents with native transaction/recovery/state/audit organs;
- systems whose existing mechanisms already separate intent/effect, history/projection, local evidence, wake triggers, recovery roots, or governance closure;
- Hosts where importing ENA-specific schemas/tools would add representation burden without changing a decision.

This HOW exists to prevent a common implementation mistake:

```text
ENA defines/reference-implements property P
Host already realizes P with native organ O
-> adopter installs a second ENA-shaped organ anyway
-> duplicated state / conflicting authority / extra governance burden
```

## Concrete mechanism

Create a **property-to-native-organ binding** plus exact ENA source identity and rebind/freshness evidence.

Illustrative mapping:

```yaml
source_current:
  ena_version: v0.3.6
  current_tree: 7dcbb3934883ffa6cc5292a662588cafc1533cff

bindings:
  mutation_pressure:
    native_organ: wake/metabolism scan
    status: NATIVE_REALIZATION
  latent_variation:
    native_organ: candidate/proposal queue
    status: NATIVE_REALIZATION
  local_selection:
    native_organ: local evidence ceiling
    status: NATIVE_REALIZATION
  rescue_plane:
    native_organ: recovery-root/controller
    status: PARTIAL_NATIVE_REALIZATION
  expression_axis:
    native_organ: null
    status: DORMANT_NOT_DECISION_CHANGING
```

The mapping is **not** a claim that the native organ is equivalent in all dimensions. Each binding should preserve limitations/unknowns where material.

## Runtime sequence

```text
1. resolve canonical ENA Current identity
2. inspect existing Host organs and current decision surfaces
3. bind ENA properties to native organs only where behavior is materially realized
4. mark unneeded/non-applicable mechanisms dormant rather than manufacturing replicas
5. identify actual semantic gaps where no native organ exists
6. change only the gaps or stale semantic bindings that alter decisions
7. preserve prior mapping as history when Current/Host changes
8. observe ordinary work for SALIENT/APPLIED evidence rather than treating the mapping file itself as behavioral proof
```

## Rebind vs mechanism migration

A Current update may require only:

- pointer/source identity update;
- local semantic kernel refresh;
- mapping review for changed properties;
- revalidation of affected native organs.

It does **not** automatically require:

- new ENA record schemas;
- replacement of native state machines;
- migration to ENA reference tools;
- active instantiation of every Current capability;
- bookkeeping for distinctions that do not change Host behavior.

## Concrete decision rule

For each proposed ENA mechanism migration:

```text
Does the Host already have an organ that changes the same material decision?
  |
  +-- YES -> map it; test gaps; avoid duplicate mechanism by default
  |
  +-- PARTIAL -> retain native organ + add only missing adapter/behavior
  |
  +-- NO -> consider another reference HOW / build a new organ
  |
  +-- NOT APPLICABLE -> remain dormant/cold
```

This is not an excuse to call everything "already native". The mapping needs enough concrete behavioral evidence to show what the organ actually does.

## Freshness / invalidation

Rebind review is triggered when a material dimension changes, for example:

- ENA Current identity / property semantics;
- Host state topology or native organ implementation;
- model/runtime where it materially changes the mapping;
- external authority/recovery substrate;
- evidence showing a previously claimed native mapping does not affect actual behavior.

A stale mapping may remain historical evidence but must not be narrated as current adoption.

## What this HOW is good at

- preserves mature Host investment;
- minimizes redundant machinery;
- supports `complete adoption baseline != every mechanism active`;
- turns `Standardize the property; discover the organ` into an implementation procedure;
- exposes where ENA genuinely adds a missing organ instead of rewarding format conformity.

## What it is bad at

- new/immature Hosts with few native organs;
- vague self-reports such as "our system already does that" without inspectable behavior;
- Hosts whose native mechanism is deeply coupled to stale semantics and cannot be independently revalidated.

## False-confidence control

Do not accept:

```text
binding exists
-> native organ equivalent
-> ENA applied
```

A binding is initially:

`WRITTEN / INTERPRETED`

Behavioral maturity still requires naturalistic/controlled evidence appropriate to the property.

## Anti-degradation note

This HOW was added because forcing a DSH-like mature Host into `HOW-D-HYBRID-COMPILED-PROJECTION` would misrepresent its reported phenotype. DSH field evidence says the v0.3.6 rebind updated its semantic pointer/kernel while existing transaction/recovery/wake/risk-routing organs remained the implementation substrate; it deliberately did not instantiate mechanisms that would not change a current decision.

That field observation motivates this HOW but does not prove universal fitness or independently reproduce DSH internals.

## Evidence targets

Useful checks:

- a native organ mapping with a concrete behavior/ref rather than only a label;
- one deliberately unmapped property remains `GAP` rather than being falsely claimed covered;
- one non-applicable property remains dormant without compliance penalty;
- Current identity change makes prior mapping stale until review;
- adding an ENA-specific duplicate organ is rejected when it provides no new decision capability;
- a partial native organ can coexist with a small adapter instead of wholesale migration.

`LOCAL_WINNER = MATURE_NATIVE_ORGAN_HOST_CANDIDATE`

`SEMANTIC_ADOPTION != MECHANISM_MIGRATION`
