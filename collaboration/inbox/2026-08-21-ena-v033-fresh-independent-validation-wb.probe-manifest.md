# Independent Probe Manifest — ENA v0.3.3-candidate

Total probes designed & executed: **43** | PASS: 33 | CHALLENGE: 10

All probes designed from a BLIND read of `validate_contracts.py` (no author oracle consulted). Predicted verdict/code = validator's own; Actual = real execution. CHALLENGE rows: 3 are genuine defects (D1/D2/D3 in report), 7 are harness prediction errors (not candidate bugs).

| ID | Property | Predicted | Actual | Result | Notes |
|---|---|---|---|---|---|
| P01 | SUPPORTED happy path w/ registry + evidence | OK/OK | OK/OK | PASS |  |
| P02 | SUPPORTED claim w/o support refs | BLOCK/CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS | BLOCK/CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS | PASS |  |
| P03 | Referenced support CONTRADICTS | BLOCK/RESOLVED_SUPPORT_CONTRADICTS | BLOCK/RESOLVED_SUPPORT_CONTRADICTS | PASS |  |
| P04 | Referenced support empty status | BLOCK/SUPPORT_NOT_POSITIVE | BLOCK/SUPPORT_NOT_POSITIVE | PASS |  |
| P05 | PARTIAL support, claim not narrowed | UNKNOWN/PARTIAL_SUPPORT_ONLY | UNKNOWN/PARTIAL_SUPPORT_ONLY | PASS |  |
| P06 | PARTIAL support, claim narrowed PARTIAL | OK/OK | OK/OK | PASS |  |
| P07 | Evidence ref declared, registry ABSENT -> baseline OK | OK/OK | OK/OK | PASS |  |
| P08 | Evidence ref declared, registry present, ref missing | BLOCK/EVIDENCE_REF_UNRESOLVABLE | BLOCK/EVIDENCE_REF_UNRESOLVABLE | PASS |  |
| P09 | Support empty evidence_refs WITH registry | BLOCK/SUPPORT_WITHOUT_EVIDENCE | BLOCK/SUPPORT_WITHOUT_EVIDENCE | PASS |  |
| P10 | Top-level support dict WITHOUT id (FLAG-A false BLOCK) | OK/OK | BLOCK/REGISTRY_MALFORMED | CHLG | DEFECT D2 (false BLOCK) |
| P11 | Top-level support dict WITH id, no claim | OK/OK | OK/OK | PASS |  |
| P12 | Duplicate support ids, conflicting content | BLOCK/DUPLICATE_REF_ID | OK/OK | CHLG | harness prediction error (code/field) |
| P13 | Duplicate support ids, identical content -> dedupe | OK/OK | OK/OK | PASS |  |
| P14 | Independence overclaim (string level) | BLOCK/INDEPENDENCE_OVERCLAIMED | BLOCK/INDEPENDENCE_OVERCLAIMED | PASS |  |
| P15 | Independence w/o root_provenance | BLOCK/INDEPENDENCE_WITHOUT_ROOT_PROVENANCE | BLOCK/INDEPENDENCE_OVERCLAIMED | CHLG | harness prediction error (code/field) |
| P16 | Independence count ok, root registry ABSENT -> UNKNOWN | UNKNOWN/ROOT_REGISTRY_UNAVAILABLE | BLOCK/INDEPENDENCE_OVERCLAIMED | CHLG | manifests D3 (indep. composition) |
| P17 | Independence count ok, root registry present, distinct origins | OK/OK | BLOCK/INDEPENDENCE_OVERCLAIMED | CHLG | manifests D3 (indep. composition) |
| P18 | Obligation status outside vocabulary (F2) | BLOCK/OBLIGATION_STATUS_OUTSIDE_VOCABULARY | BLOCK/OBLIGATION_STATUS_OUTSIDE_VOCABULARY | PASS |  |
| P19 | Completion claim w/o obligation refs | BLOCK/COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS | BLOCK/CLAIM_SUPPORTED_WITHOUT_SUPPORT_REFS | CHLG | harness prediction error (code/field) |
| P20 | Completion claim, material PENDING bound obligation | BLOCK/MATERIAL_OBLIGATION_BLOCKS_CLAIM | BLOCK/COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS | CHLG | harness prediction error (code/field) |
| P21 | SATISFIED obligation w/o closure evidence | BLOCK/SATISFIED_WITHOUT_CLOSURE_EVIDENCE | BLOCK/COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS | CHLG | harness prediction error (code/field) |
| P22 | SATISFIED obligation + closure refs, registry ABSENT -> OK | OK/OK | BLOCK/COMPLETION_CLAIM_WITHOUT_OBLIGATION_REFS | CHLG | harness prediction error (code/field) |
| P23 | Authority USER_EXPLICIT_GRANT valid horizon | OK/OK | OK/OK | PASS |  |
| P24 | Authority unknown source, no registry | BLOCK/AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING | BLOCK/AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING | PASS |  |
| P25 | Authority via registry grant valid | OK/OK | OK/OK | PASS |  |
| P26 | Authority registry grant EXPIRED | BLOCK/AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING | BLOCK/AUTHORITY_MANDATE_SOURCE_NOT_AUTHORIZING | PASS |  |
| P27 | Mandate.expires_at expired (direct) | BLOCK/MANDATE_EXPIRED | BLOCK/MANDATE_EXPIRED | PASS |  |
| P28 | Capability VERIFIED, grade E0/E1 only | BLOCK/VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE | BLOCK/VERIFIED_ONLY_STATIC_STRUCTURE_EVIDENCE | PASS |  |
| P29 | Capability VERIFIED, grade E3 valid ref | OK/OK | OK/OK | PASS |  |
| P30 | Capability VERIFIED, invalid grade | BLOCK/EVIDENCE_GRADE_INVALID | BLOCK/EVIDENCE_GRADE_INVALID | PASS |  |
| P31 | Recovery STATE_ONLY | OK/OK | OK/OK | PASS |  |
| P32 | Recovery STATE_AND_HISTORY full ok | OK/OK | OK/OK | PASS |  |
| P33 | Recovery STATE_AND_HISTORY shared roots | BLOCK/HISTORY_EVIDENCE_SHARED_ROOT | BLOCK/HISTORY_EVIDENCE_SHARED_ROOT | PASS |  |
| P34 | Recovery STATE_AND_HISTORY same evidence refs | BLOCK/HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE | BLOCK/HISTORY_EVIDENCE_SAME_AS_STATE_EVIDENCE | PASS |  |
| P35 | R12 dict key != inner id (support_registry) | BLOCK/REGISTRY_MALFORMED | BLOCK/REGISTRY_MALFORMED | PASS |  |
| P36 | Malformed registry (dict value not dict) | BLOCK/REGISTRY_MALFORMED | BLOCK/REGISTRY_MALFORMED | PASS |  |
| P37 | List registry entry without id | BLOCK/REGISTRY_MALFORMED | BLOCK/REGISTRY_MALFORMED | PASS |  |
| P38 | Empty payload + eval_time -> vacuous OK | OK/OK | OK/OK | PASS |  |
| P39 | Missing eval_time -> BLOCK | BLOCK/EVAL_TIME_REQUIRED | BLOCK/EVAL_TIME_REQUIRED | PASS |  |
| P40 | Malformed eval_time -> BLOCK | BLOCK/EVAL_TIME_REQUIRED | BLOCK/EVAL_TIME_REQUIRED | PASS |  |
| P41 | claim_ref mismatch (R2) | BLOCK/SUPPORT_TARGET_MISMATCH | BLOCK/SUPPORT_TARGET_MISMATCH | PASS |  |
| P42 | FLAG-D: bound PENDING obligation, NON-completion claim (expect BLOCK per R7, actual?) | BLOCK/MATERIAL_OBLIGATION_BLOCKS_CLAIM | OK/OK | CHLG | DEFECT D1 (false OK) |
| P43 | FLAG: capabilities verified WITHOUT authority_envelope (trust gap) | OK/OK | OK/OK | PASS |  |