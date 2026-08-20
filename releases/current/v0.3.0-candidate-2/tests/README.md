# Candidate 2 V0/V1 Contract Tests

These tests exercise high-ROI semantic invariants that JSON Schema alone cannot prove.

Run from the Candidate 2 directory:

```bash
python tests/test_candidate2_contracts.py
```

Expected cases:

- same-scope evidence supports a same-scope claim;
- cross-instance evidence without independently declared transfer evidence is rejected;
- cross-instance support may proceed only when a transfer/equivalence/invariance basis and evidence reference are explicit (the referenced transfer evidence still requires normal evidence validation);
- a material observed obligation that is PENDING blocks the referenced completion claim;
- SATISFIED obligation state requires closure evidence;
- state restore success does not support a `STATE_AND_HISTORY` recovery claim when historical continuity is UNKNOWN;
- state restore plus preserved history can support a `STATE_AND_HISTORY` claim.

Current smoke result at Candidate 2 creation: `7/7 passed`.

The JSON schemas for the associated prototype artifacts also passed Draft 2020-12 schema self-validation and the representative structural fixtures were schema-valid. This is deliberate: invalid semantic inheritance can be structurally well-formed, which is why the reference semantic validator exists.

This validator is a Candidate 2 reference mechanism. It is not proof of universal semantic completeness and is not Mainline.
