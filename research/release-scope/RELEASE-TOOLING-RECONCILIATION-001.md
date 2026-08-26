# Release Tooling Reconciliation 001 — Evolution v2 practical path

Status: `RELEASE_SCOPE_DECISION / TOOLING_SELECTED_FOR_CANDIDATE / CURRENT_UNCHANGED / VERSION_UNASSIGNED`

Date: 2026-08-27

## Decision

For the next candidate, select a **minimal v2-compatible evolution helper** as the default practical evolution-record / adaptation-packet path.

```text
SELECTED_FOR_CANDIDATE_DEFAULT = TOOL-HOW-C / MINIMAL_V2_HELPER
NOT_SELECTED_AS_PRIMARY_FIX = TOOL-HOW-A / NARROW_LEGACY_REPAIR
LEGACY_V1_2 = RETAIN_ONLY_AS_EXPLICIT_LEGACY_OR_COMPATIBILITY_SURFACE
CURRENT_CHANGE = NO
```

This is a release-scope selection, not authorization to modify `releases/current/`.

## Why not narrow legacy repair as the primary answer

The inherited `releases/current/tools/ena_evolve.py` is not merely too strict about Variation Space. It remains:

- state/schema 1.2;
- adaptation-packet v1;
- without full v0.3.6 expression / latent-reservoir / packet-v2 runtime semantics;
- explicitly non-normative for Current v2 in `CURRENT-BASELINE.yaml` and Current README.

Making `--variation-space` optional would remove one real false-BLOCK but would not make the tool a v2 runtime. It risks increasing false confidence by making a legacy path look more Current-compatible.

```text
FALSE_BLOCK_REMOVED
!=
V2_RUNTIME_SEMANTICS_IMPLEMENTED
```

## Why the minimal v2 helper survived the comparison

Research prototype:

`research/prototypes/ena-evolve-v2-minimal/`

The helper deliberately reuses:

- Current `templates/evolution-record.v2.json`;
- Current `tools/validate_evolution_record_v2.py`;
- Current `schemas/adaptation-packet.v2.schema.json`.

It does not copy the evolution-record semantic consistency rules.

Its additional semantic ownership is deliberately narrow:

- construct a valid `LATENT / UNASSESSED` v2 record, including `variation_space: null` when no real Variation Space exists yet;
- export packet v2 from a Current-valid source record;
- canonical packet digest creation/checking;
- packet-v2 schema validation;
- narrow source expression-history/current-expression consistency;
- preserve represented negative-lineage refs;
- import a packet into a local `MIGRATION_CANDIDATE / LATENT / UNASSESSED` record without promoting source selection.

This supports the key release property:

```text
HELPER_ORCHESTRATES_CURRENT_SEMANTICS
!=
HELPER_REIMPLEMENTS_CURRENT_SEMANTICS
```

## Machine evidence at selection time

GitHub Actions executed successfully for the research prototype:

- deterministic function-level corpus: PASS;
- compile gate: PASS;
- actual CLI round trip: PASS.

CLI path exercised:

```text
new-latent
-> validate-record
-> export-packet
-> validate-packet
-> import-packet
-> validate-record
```

The round trip preserves:

```text
local latent variation_space = null
packet_schema = ena-adaptation-packet.v2
source selection does not become receiver-local selection
imported local variation_space = null
```

Case count is corpus size only and carries no architecture threshold authority.

## Candidate packaging direction

The exact final filename remains a candidate-build detail. The release should expose one clearly preferred v2 practical helper under the ordinary tooling surface.

The old v1.2 implementation may remain for compatibility/history only if the package makes its status unambiguous. Candidate design should prefer one of:

```text
tools/ena_evolve_v2.py              <- preferred v2 path
references/legacy/ena_evolve_v1_2.py
```

or another equally explicit layout.

Do not preserve two equally prominent `ena_evolve` paths whose semantic generations are unclear.

## Legacy compatibility rule

The legacy tool does not need a cosmetic Variation-Space patch merely to remain in lineage.

If retained in the candidate package:

- label it legacy/non-v2;
- keep compatibility behavior testable;
- do not present it as the default Current-generation helper;
- provide migration/adoption guidance toward v2 records/packet path;
- preserve its historical regression value where useful.

If candidate usability testing shows the legacy path causes ambiguity even when labeled, removal from the adopter package may be preferable while Git history preserves lineage.

## Packet-v2 residuals remain visible

The minimal helper does not silently repair unrelated packet-v2 research seams.

In particular:

```text
packet v2 top-level additionalProperties:false
```

still limits portable top-level extension. The prototype selftest keeps this rejection visible rather than inventing a Host extension surface during a tooling decision.

Likewise:

```text
PACKET_VALID != SOURCE_AUTHENTICATED
PACKET_VALID != EVIDENCE_TRUE
PACKET_DIGEST_VALID != LINEAGE_COMPLETE
SOURCE_SELECTION_TRANSFERRED != RECEIVER_LOCAL_SELECTION
```

## Candidate acceptance requirements for this tooling choice

Before release promotion, the candidate version of the helper should prove at least:

1. it validates against the candidate's exact v2 record/packet semantics;
2. latent create/import does not require preallocated Variation Space;
3. source selection/negative evidence remain provenance, not local proof;
4. packet tampering is rejected by digest/schema checks;
5. candidate help/README makes v2 vs legacy status unambiguous;
6. no duplicate shadow evolution semantic engine appears in tooling;
7. language/adopter instructions cover the practical path where material.

## Reopen rule

Reopen this decision if candidate assembly shows that the minimal helper must duplicate substantial evolution lifecycle semantics or cannot support the intended practical path without a second state engine.

Otherwise:

```text
TOOLING_SCOPE = STABLE_ENOUGH_FOR_CANDIDATE_ASSEMBLY
```

`CURRENT_CHANGE = NO`
