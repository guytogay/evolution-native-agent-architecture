# Independent Report Self-Hash Recursion Incident

Date: 2026-08-28

Status: `VALIDATION_INTERFACE_DEFECT / METHOD_CORRECTION_REQUIRED / NOT_CANDIDATE_DEFECT`

## Incident

The candidate.2 A-S clean-room intake required the reviewer to compute SHA-256 over the exact final report bytes and also record that digest inside the same exact report.

That construction is self-referential:

`report bytes -> digest -> insert digest -> report bytes change -> digest changes`

A stable exact-file self-hash cannot be required without an explicitly defined normalization/exclusion rule.

The fresh independent reviewer correctly refused to invent a false exact-file digest and returned the digest externally. The project manager independently recomputed and verified the exact uploaded report bytes before A-P exposure.

## Corrected rule

For independent A-S/A-P report sealing:

```text
FINAL_REPORT_BYTES
-> SHA-256(final bytes)
-> EXTERNAL SEAL RECORD / SIDECAR / SIGNED ENVELOPE
```

Do **not** require the digest to be embedded inside the bytes it hashes.

If an embedded seal is ever desired, the method must define a deterministic normalization that excludes the seal field from the hashed representation; otherwise the claim is not an exact-file hash.

## Effect on candidate.2

This was A-S-04 and is classified in Phase B as a validation-interface defect. It does not alter candidate.2 bytes and is not a candidate.3 semantic repair requirement.

The A-P intake already used the corrected external-digest shape.

## General lesson

`CONTENT_INTEGRITY_REQUIREMENT != SELF_REFERENTIAL_ENCODING_REQUIREMENT`

`EXACT_REPORT_HASH -> EXTERNAL_DIGEST_BY_DEFAULT`

Interface requirements must themselves be satisfiable and falsifiable.
