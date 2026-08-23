# ENA v0.3.5 candidate.1 Freeze — 2026-08-23

Status:

`FROZEN_CANDIDATE.1 / AUTHOR_RECONCILED / AWAITING_TARGETED_SAME_FALSIFIER_REVALIDATION / NOT_CURRENT / NOT_RELEASED`

This record freezes the first revision of the v0.3.5 candidate after independent DSH falsification of the predecessor. It does **not** claim release fitness, fresh independent validation, or Current status.

## 1. Frozen candidate.1 identity

Repository:
`guytogay/evolution-native-agent-architecture`

Frozen candidate.1 source commit:
`e6ff1e76afb8ad8919186786100ec153a5f0d07a`

Package path:
`releases/v0.3.5-candidate/`

Frozen candidate.1 effective-content Git tree:
`ff2cb44c7a5d1b472800180578b5df7baa123aec`

Frozen source root Git tree:
`527e18b6c082e9995f23e9895d71075ed193b34d`

Candidate.1 draft PR:
`#58 — candidate.1: ENA v0.3.5 falsification-driven revision`

The branch name is only a development pointer. Any material change to the package after this freeze requires a successor candidate identity; do not silently edit this frozen tree.

## 2. Predecessor falsification lineage

Frozen predecessor:

- source commit: `eb6d7ba00894ed446903aebe61cd59f0bdb59af7`
- effective tree: `f373e7695348c157dcd48d3ed243ea3079215b8f`
- independent DSH verdict: `NEEDS_REVISION`

The predecessor remains immutable evidence and PR #57 was closed without merge.

Independent reproduced defects driving candidate.1 included:

- zero-experiment positive selection;
- negative migration evidence laundering;
- lifecycle and evidence-selection state conflation;
- archive/integration obscuring selection during export;
- state-blind governance closure;
- evolution-tool/schema disconnection;
- under-checked migration-packet semantic consistency.

No new Constitution rule was added merely because these implementation/schema defects existed.

## 3. candidate.1 repair properties

candidate.1 now separates:

`lifecycle_state = PROPOSED | EXPERIMENTED | INTEGRATED | ARCHIVED | RETIRED`

from:

`selection_state = UNASSESSED | SUPPORTED | PARTIAL | NOT_SUPPORTED | HARMFUL | UNKNOWN`

Material properties under revalidation include:

1. formal selection follows at least one represented experiment;
2. `INTEGRATED != SUPPORTED`;
3. archive/retirement preserve selection history;
4. migration packet purpose derives from source selection state, not lifecycle;
5. source experiments/evaluations/integration/archive/migration lineage are transferred;
6. source negative evidence remains source negative evidence;
7. receiver-side positive reselection is allowed only after local experiment/evaluation and does not rewrite source lineage;
8. packet semantic contradictions are mechanically rejected;
9. packet-local digest is internal consistency, not source authentication;
10. governance closure reads represented evolution state plus explicit inputs, while still not proving omitted real-world blockers absent;
11. actual tool candidate/packet outputs are connected to JSON-schema validation;
12. inherited composed-validator PASS is explicitly regression preservation, not proof of new v0.3.5 semantic coverage;
13. Runtime Kernel carries the reference-tool external-reality boundary;
14. zh-CN first-adoption guidance includes immutable effective-content identity.

## 4. Author-side additional hardening after DSH report

During reconciliation the author additionally noticed that a handcrafted migration packet could claim a non-UNASSESSED selection while omitting source experiments if a caller bypassed external JSON-schema validation. candidate.1 therefore also checks source experiment/evaluation consistency inside `ena_evolve.py` itself.

This is author-side hardening, not independent evidence.

## 5. Automated checks at frozen source commit

At `e6ff1e76...`:

- Validate ENA v0.3.5 candidate — run `32615008446` — SUCCESS;
- Main Gate — run `32615008433` — SUCCESS;
- CodeQL — run `32615008422` — SUCCESS.

Candidate validation includes:

- inherited composed-validator regression suite;
- expanded `ena_evolve.py selftest`;
- `candidate1_adversarial.py` regression probes for predecessor failures;
- actual tool-generated candidate record + migration packet validated against candidate.1 JSON schemas;
- Python compile;
- English/zh-CN Constitution ID parity;
- bilingual fixture structure;
- candidate/projection pointer checks;
- Current isolation.

Passing author/CI checks are not the revalidation verdict.

## 6. Current isolation

At the frozen candidate.1 source commit, `releases/current/` remains exact v0.3.4 tree:

`b237802c08d608bb9be650fe213b7846d3be4bf6`

Comparison from candidate.1 branch base `77f9feb805492f9c8f1c4a1b717361be06338808` to frozen source commit changes only the candidate package and candidate-validation workflow; no `releases/current/**` path changes.

## 7. Required next evidence

Use the **same DSH falsifier session** for targeted revalidation because it owns the original minimal reproductions. Label it honestly:

`SAME_FALSIFIER / TARGETED_REVALIDATION / NOT_FRESH`

It should re-run its prior attacks against the frozen candidate.1 identity and determine whether F-A1/F-A2/F-A3/F-A5/F-A6/F-A10 and PF-A1 are actually closed, whether fixes introduce new false-confidence or evolution-starvation paths, and whether bilingual semantics materially drifted.

Do not ask it to rewrite canonical repository state.

A targeted same-falsifier PASS would support reconciliation of the specified defects; it would not become fresh-adopter evidence or universal model/Host proof.
