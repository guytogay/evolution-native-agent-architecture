# Tiny Hot Kernel + Semantic Router research prototype

Status: `RESEARCH_PROTOTYPE / NOT_CURRENT / NOT_RELEASE_CANDIDATE`

Related: #87, #89, #90, PR #82.

Source Current used for target navigation:

- ENA: `v0.3.6 / CURRENT / FIELD_VALIDATION`
- Current tree: `7dcbb3934883ffa6cc5292a662588cafc1533cff`
- release merge commit: `74b790741653286e0f01a1483723cdeb065ec3df`

This prototype tests one practical adoption question:

> Can a small always-loaded ENA recognizer notice decision shapes, invoke a bounded router, retrieve the right cold semantics, and stay quiet on irrelevant work without turning router success into a safety certificate?

It deliberately separates two failure surfaces:

```text
resident recognizer quality
!=
semantic router quality
```

A router that works after explicit invocation does not prove a fresh Agent will naturally invoke it. A recognizer that fires does not prove the correct cold scope was resolved.

## Files

- `kernels/K-A-generative-consequence-grammar.md` — decision-shape buckets; moderate size, high model dependence.
- `kernels/K-B-seven-family-index.md` — compact projection of Current's seven concept-map families.
- `kernels/K-C-minimal-interrupt-questions.md` — smallest question-based interrupt surface; highest silent-FN risk.
- `semantic-router.v0.1.json` — research-only deterministic navigation map over existing Current semantics.
- `fixtures/tiny-kernel-cases.jsonl` — shared adversarial / OOD corpus for trigger + route evaluation.
- `tools/validate_semantic_router.py` — validates router structure and target section reachability with Python stdlib only.
- `tools/score_tiny_kernel_results.py` — scores Host/model result JSONL against the shared fixture corpus.

## Evaluation contract

A Host/model run should emit one JSON object per fixture case:

```json
{
  "case_id": "TK-001",
  "trigger": true,
  "families": ["composition-effects", "recovery-history"],
  "matched_route_ids": ["effect-retry-settlement"],
  "retrieval_status": "SUCCESS",
  "fallback_used": false,
  "notes": "optional"
}
```

`retrieval_status` vocabulary:

`NOT_ATTEMPTED | SUCCESS | PARTIAL | FAILED`

The scorer measures at least:

- material trigger false-negative;
- irrelevant trigger false-positive;
- primary-family route miss;
- route overreach outside the allowed family envelope;
- broken-resolver fallback honesty.

It does **not** prove semantic correctness, naturalistic salience, or decision quality.

## Guardrails

This prototype MUST NOT become:

- a second shadow copy of ENA semantics;
- one hot cue per Constitution/CAP/schema field;
- a mandatory vector database;
- a universal classifier service;
- a certificate such as `ENA_ROUTED = SAFE`;
- an excuse to claim `no cue noticed = no cue needed`.

The router stores recognition + navigation only. Canonical Current retains normative semantics.

## Research sequence

1. static validate router targets;
2. run same fixtures against K-A/K-B/K-C with the same downstream router;
3. inspect FN/FP/wrong-route failure topology, not only total accuracy;
4. test broken cold resolver/fallback;
5. only then move to real Host implementation and naturalistic fresh-session work.

Do not select a winner by token count alone.
