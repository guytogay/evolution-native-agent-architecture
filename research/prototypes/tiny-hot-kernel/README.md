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
- `fixtures/tiny-kernel-prompts.jsonl` — **blinded Agent-facing stimuli**. Contains no expected labels.
- `fixtures/tiny-kernel-cases.jsonl` — **maintainer/scorer-only oracle** with expected trigger/family envelopes. Do not expose this to the test Agent.
- `CONTROLLED-RUNNER-INSTRUCTION.md` — operational instructions for running a blinded comparison.
- `EVAL-PROTOCOL.md` — controlled-vs-naturalistic evidence design and error taxonomy.
- `run-manifest.template.json` — records kernel/model/Host/context/order/contamination/footprint so results remain comparable.
- `tools/validate_semantic_router.py` — validates router structure and target section reachability with Python stdlib only.
- `tools/score_tiny_kernel_results.py` — scores frozen Host/model result JSONL against the maintainer-side oracle.
- `tools/selftest_tiny_hot_kernel.py` — validates router, blind/oracle separation, fixtures, and scorer rejection behavior.

## Critical blinding rule

The test Agent MUST NOT see `tiny-kernel-cases.jsonl`, scorer expectations, or prior-kernel corrections during a controlled run.

Agent-visible path:

```text
one kernel candidate
+ one blind prompt
-> resident TRIGGER/QUIET decision
-> if TRIGGER and resolver available: router -> exact cold Current targets
-> result JSON
```

Maintainer-only path:

```text
frozen result JSONL
+ oracle tiny-kernel-cases.jsonl
-> scorer
```

`stimulus != oracle`

A benchmark that leaks its expected trigger/family labels is not evidence of kernel recognition.

## Evaluation contract

A Host/model run should emit one JSON object per blind prompt:

```json
{
  "case_id": "TK-001",
  "kernel": "K-A",
  "trigger": true,
  "families": ["composition-effects", "recovery-history"],
  "matched_route_ids": ["effect-retry-settlement"],
  "retrieval_status": "SUCCESS",
  "fallback_used": false,
  "resident_reason": "brief resident-stage reason",
  "route_reason": "brief post-router reason",
  "final_action_posture": "brief posture",
  "notes": "optional"
}
```

`retrieval_status` vocabulary:

`NOT_ATTEMPTED | SUCCESS | PARTIAL | FAILED`

The scorer measures at least:

- material trigger false-negative;
- irrelevant trigger false-positive;
- primary-family route miss where the resolver is available;
- route overreach outside the allowed family envelope;
- broken-resolver false-success/fallback honesty.

When the resolver is deliberately `BROKEN`, family-routing completeness is **not** scored. Requiring route reconstruction from unavailable cold machinery would turn the benchmark into a false-BLOCK test of resident memorization.

It does **not** prove semantic correctness, naturalistic salience, or decision quality.

## Guardrails

This prototype MUST NOT become:

- a second shadow copy of ENA semantics;
- one hot cue for every Constitution/CAP/schema field;
- a mandatory vector database;
- a universal classifier service;
- a certificate such as `ENA_ROUTED = SAFE`;
- an excuse to claim `no cue noticed = no cue needed`;
- an oracle-leaking benchmark that rewards memorizing expected answers.

The router stores recognition + navigation only. Canonical Current retains normative semantics.

## Research sequence

1. static validate router targets and blind/oracle separation;
2. run the same **blinded** prompts against K-A/K-B/K-C with the same downstream router;
3. inspect FN/FP/wrong-route/fallback topology, not only total accuracy;
4. record model/Host/context/order/footprint in a run manifest;
5. test broken cold resolver/fallback;
6. only then move a promising kernel into real Host implementation and naturalistic fresh-session work.

Do not select a winner by token count or aggregate accuracy alone.
