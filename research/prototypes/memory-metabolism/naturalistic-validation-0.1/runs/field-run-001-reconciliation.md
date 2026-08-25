# Field Run 001 — Cold Reconciliation

Status: `PRIMARY_NATURALISTIC / POST_HOC_MANUAL_AUDIT / NOT_POPULATION_EVIDENCE`

Working task baseline:

`73b57f8990b50f7335940b4c439165e13197c1da`

Working output:

`field-run-001-working-agent-output.md`

## Assessment

`NO_MATERIAL_FAILURE_OBSERVED`

This assessment does **not** mean:

- R0 recall is proven;
- all relevant repository history was retrieved;
- no silent miss was possible;
- the resolver has known recall;
- one natural run validates the architecture.

It means only:

> after the working Agent completed an ordinary pre-existing maintenance task, a separate cold audit found no omitted durable project fact that changed the material S17 verdict or its no-immediate-fix conclusion.

## Independent checks

### 1. Legacy CLI reachability — confirmed

Frozen `releases/current/tools/ena_evolve.py` exposes ordinary `propose` and `import` commands whose `--variation-space` arguments are both declared `required=True`.

`cmd_propose` and `cmd_import` store `args.variation_space` directly.

`cmd_experiment` uses:

`args.variation_space or candidate.get("variation_space")`

and does not itself enforce a v2 expression/materiality decision.

Disposition:

`WORKING CLAIM CONFIRMED`

### 2. Legacy v1 representation contract — confirmed

Frozen `releases/current/schemas/evolution-record.v1.schema.json` requires candidate-level `variation_space` and constrains it to a non-empty string.

Therefore simply making the parser argument optional and storing `None` would make the produced v1 candidate fail its inherited schema.

Disposition:

`WORKING QUALIFICATION CONFIRMED`

### 3. v0.3.6 v2 latent semantics — confirmed

Frozen `releases/current/schemas/evolution-record.v2.schema.json` requires the `variation_space` field but allows `string | null`.

It separately represents:

- `expression_state = LATENT | EXPRESSED`;
- `effect_materiality = MATERIAL | NON_MATERIAL | UNKNOWN`;
- `triggered_obligation_refs`.

Its consistency validator requires Variation Space or a triggered obligation only for represented `EXPRESSED` state whose latest effect materiality is `MATERIAL`.

The first validator selftest accepts the dormant base record.

Disposition:

`WORKING CURRENT-SEMANTIC CLAIM CONFIRMED`

### 4. Shipped v2 latent template — confirmed

Frozen `releases/current/templates/evolution-record.v2.json` is:

- `lifecycle_state = PROPOSED`;
- `expression_state = LATENT`;
- `selection_state = UNASSESSED`;
- `variation_space = null`;
- no experiments/evaluations/expression history.

Disposition:

`WORKING REPRESENTATION CLAIM CONFIRMED`

### 5. Current reference-tool boundary — confirmed

Frozen `releases/current/09-EVOLUTION-METABOLISM.md` section 9.14 explicitly states:

- inherited `tools/ena_evolve.py` does not fully represent the v0.3.6 mutation-pressure / latent-reservoir / expression / packet-v2 semantics;
- v2 schema + v2 validator are the formal represented-consistency surface;
- inherited tool remains state/schema 1.2;
- its required `--variation-space` propose/import path is non-normative for legal latent-now/experiment-later creation/import;
- the rejection must not be narrated as a semantic prohibition that Current does not contain.

Disposition:

`CONFIRMED_FALSE_BLOCK_RELATIVE_TO_CURRENT / TRUTHFULLY_BOUNDED_LEGACY_TOOL`

### 6. Current baseline machine identity — confirmed

Frozen `CURRENT-BASELINE.yaml` explicitly records:

- inherited reference tool state version `1.2`;
- inherited tool is not the normative v2 path;
- latent propose/import false-BLOCK is known;
- latent variation is supported;
- immediate experiment is not required;
- `variation_space_required_at_latent_storage_time = false`;
- materially consequential expression requires Variation Space or triggered obligation.

Disposition:

`WORKING CROSS-LAYER VERDICT CONFIRMED`

### 7. Release gate intentionally preserves the truthful boundary — confirmed

Frozen `.github/workflows/current-validate.yml` machine-checks:

- inherited state version remains 1.2;
- inherited tool is non-normative v2 path;
- the known latent propose/import false-BLOCK remains represented;
- no `expression_state` runtime field exists in the old tool;
- at least two required `--variation-space` declarations still exist;
- actual legacy output continues to validate against the v1 schemas.

Therefore changing only the parser underneath these assertions would make Current's boundary declaration stale/false.

Disposition:

`WORKING RELEASE-GATE CLAIM CONFIRMED`

### 8. Historical F-09 reconciliation — confirmed

Frozen `releases/current/LINEAGE.md` records:

`F-09 CLOSED_BY_TRUTHFUL_BOUNDARY`

and lists the accepted residual:

> inherited `ena_evolve.py` v1.2 false-BLOCKs the normative v0.3.6 latent propose/import path and remains explicitly non-normative for that path.

Disposition:

`WORKING HISTORICAL CLAIM CONFIRMED`

## Did cold audit find a decision-changing omission?

No.

No durable fact found during post-hoc audit changed either material conclusion:

1. `S17 = CONFIRMED_FALSE_BLOCK` relative to v0.3.6 Current semantics;
2. the frozen evidence does not justify a parser-only repair or any immediate Current mutation.

The working Agent's suggested small v2-native author/import adapter remains a **plausible future repair direction**, not a selected or authorized solution. Real Host friction is still needed to establish that another authoring/runtime surface pays governance/maintenance rent.

## Retrieval-lifecycle interpretation

The working report visibly used more than the explicit S17 seed. It connected:

`legacy CLI behavior`
→ `legacy v1 representation contract`
→ `Current 9.14 boundary`
→ `v2 schema/template/validator`
→ `release-gate truth assertions`
→ `historical F-09 reconciliation`.

That is useful field evidence that a bounded generic repository-history reflex can support a real cross-layer maintenance decision without preloading a domain catalog.

However, because the working Host did not expose a complete raw search/tool-call trace, this run does not establish:

- exact scope-discovery sequence;
- resolver recall;
- whether every lookup was triggered by R0 rather than by the explicit task wording;
- retrieval cost;
- whether the final decision would have differed without retrieval.

Therefore `utility_observation` remains `UNKNOWN` rather than being promoted to `CHANGED_MATERIAL_DECISION`.

## Field consequence

No schema or ENA rule change is justified from Run 001.

The differentiated next evidence source should be another **naturally motivated task**, preferably from a different problem family, only when such a task exists. Do not repeat S17 across multiple models merely to count agreement.
