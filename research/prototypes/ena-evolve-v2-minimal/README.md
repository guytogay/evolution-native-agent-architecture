# Minimal ENA v2 evolution helper — research prototype

Status: `RESEARCH_PROTOTYPE / RELEASE_SCOPE_TOOLING_COMPARISON / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

## Question

Can ENA replace the inherited v1.2 `ena_evolve.py` as the practical default path with a **much thinner v2 helper** that reuses Current semantics instead of growing another shadow runtime?

This prototype deliberately tests only the smallest useful path:

```text
new latent v2 record
-> validate with Current evolution-record v2 validator
-> export adaptation-packet v2
-> validate packet schema + canonical digest + narrow packet consistency
-> import as local LATENT / UNASSESSED migration candidate
```

It does **not** implement the full evolution lifecycle.

## Why this prototype exists

Current v0.3.6 explicitly allows latent variation before a Variation Space exists:

```text
variation_space key exists
but value may be null
```

The inherited `releases/current/tools/ena_evolve.py` still requires `--variation-space` on `propose` and `import`, and remains state/schema 1.2 with adaptation-packet v1 semantics. A one-line CLI repair would remove one false-BLOCK but could misleadingly make the old tool look like the preferred v0.3.6 runtime path.

The release-scope alternatives therefore remain:

```text
TOOL-HOW-A  narrow legacy repair + explicit legacy boundary
TOOL-HOW-B  deprecate legacy as primary adopter path
TOOL-HOW-C  minimal v2 helper that reuses Current validator/schema surfaces
```

This directory evaluates TOOL-HOW-C. It does not pre-select it.

## Reuse boundary

The prototype intentionally reuses:

- `releases/current/templates/evolution-record.v2.json`;
- `releases/current/tools/validate_evolution_record_v2.py`;
- `releases/current/schemas/adaptation-packet.v2.schema.json`.

It does **not** copy the evolution-record semantic consistency rules.

The only packet-specific logic added here is:

- canonical packet digest creation/checking;
- schema validation;
- source expression-history/current-expression consistency;
- preservation of represented negative-lineage references;
- receiver import projection that stays `LATENT / UNASSESSED`.

## Critical boundaries

```text
SOURCE_SELECTION_TRANSFERRED != RECEIVER_LOCAL_SELECTION
PACKET_VALID != SOURCE_AUTHENTICATED
PACKET_VALID != EVIDENCE_TRUE
PACKET_VALID != AUTHORITY_GRANTED
PACKET_DIGEST_VALID != DECISION_MATERIAL_LINEAGE_COMPLETE
```

The helper also does not repair the known packet-v2 top-level extension seam. The Current schema still has `additionalProperties: false`; this prototype treats that as an existing portability/research boundary rather than silently inventing an extension mechanism.

## Commands

```text
new-latent
export-packet
import-packet
validate-record
validate-packet
```

`new-latent` leaves `variation_space` null unless the caller already has a real one.

`import-packet` never promotes source selection into local selection. Imported records start as:

```text
origin = MIGRATION_CANDIDATE
lifecycle_state = PROPOSED
expression_state = LATENT
selection_state = UNASSESSED
variation_space = null
```

while source experiments/evaluations/expression/integration/negative-lineage remain under migration provenance.

## Deterministic corpus

`selftest_ena_evolve_v2_minimal.py` currently covers 10 cases, including:

- latent local record with no Variation Space;
- unresolved v2 export;
- digest tamper rejection;
- invalid source record rejection before export;
- harmful source export with negative lineage;
- imported harmful source remaining locally UNASSESSED;
- packet selection/purpose contradiction;
- Current top-level extension rejection remaining visible;
- expressed-history last-expression derivation;
- expression-history/current-state contradiction.

`10` is only current corpus size and has no threshold or ontological authority.

## Decision rule

TOOL-HOW-C becomes stronger than narrow legacy repair only if the prototype stays substantially thinner in semantic ownership:

```text
helper orchestrates Current semantics
!=
helper reimplements Current semantics
```

If future usability requirements force this helper to duplicate most evolution lifecycle/validation rules, prefer deprecating the legacy tool and exposing the canonical records/validators directly rather than creating a second large runtime.

`CURRENT_CHANGE = NO`
