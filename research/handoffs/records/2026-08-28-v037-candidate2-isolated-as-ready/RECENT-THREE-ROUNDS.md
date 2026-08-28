# Recent Three Rounds

## Round 1 — candidate.2 frozen / #137 fresh intake

Candidate.2 passed exact pre-freeze validation and was externally frozen at source `bda470e0...` / subtree `d5fefc8c...`. One fresh successor review cycle was warranted. Issue #137 and a same-repository blind semantic view were prepared.

## Round 2 — #137 validation-interface abort

The genuinely fresh reviewer followed the stop rule after GitHub auto-rendered a withheld README header during ordinary directory navigation.

Result:
`A_S_ABORTED_BOUNDARY_CROSSING / VALIDATION_INTERFACE_DEFECT / NOT_SEALED / A_P_NOT_STARTED`

This produced no candidate verdict. The occurrence was persisted rather than concealed.

Broader r2 audits showed the defect was not limited to one README: same-repository search/navigation and candidate-local mixed-role files could still expose author-shaped priors.

## Round 3 — physically isolated r3 carrier

A-S and A-P were split into deterministic physically isolated carriers.

A-S physically omits author/history/oracle/project-manager surfaces and uses mechanically declared projections where mixed-role code would otherwise leak old attack maps. A-P contains the exact frozen candidate package and remains withheld until A-S report bytes are SHA-256 sealed.

Final audit run `33131773164` PASS.

Final hashes:
- A-S `dfe15a686668440138bfd624453059d61a0b28625bb9a5e0c185b33eccf9c2da`
- A-P `427a1776aea199f5f27c4bea2827d3c827cf82fab2c8cd403da0e8cc1dd97649`

Next: a genuinely fresh reviewer receives only A-S, seals its report, then receives A-P and stops before Phase B.
