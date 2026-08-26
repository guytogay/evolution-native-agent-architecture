# Controlled Runner Instruction — Tiny Hot Kernel

Status: `RESEARCH_TEST_HARNESS / NOT_CURRENT`

This file is for a human/Host running a controlled K-A/K-B/K-C comparison.

## Do not expose the oracle

The test Agent may receive:

- exactly one kernel file from `kernels/`;
- `fixtures/tiny-kernel-prompts.jsonl` one case at a time;
- this output-format instruction;
- access to `semantic-router.v0.1.json` only after it decides to trigger and only when the case says the resolver is available;
- access to canonical v0.3.6 Current targets only after routing.

The test Agent MUST NOT receive or browse:

- `fixtures/tiny-kernel-cases.jsonl`;
- scorer code if it reveals expected behavior during the run;
- prior run outputs/corrections from another kernel;
- #87/#90 comments that enumerate expected case outcomes.

The oracle and scorer are maintainer-side material.

## Fresh-context controlled pass

For the cleanest first comparison, use one fresh context per case.

Resident ENA material in that context = exactly one candidate kernel.

Do not add a system hint such as `use ENA if relevant`.

Present the case prompt as an ordinary user task.

The model's first decision is whether the resident kernel interrupts:

`trigger = true | false`

If false, it must not open the router merely to justify the answer.

If true and resolver is available, permit access to `semantic-router.v0.1.json` and then to the exact cold Current targets selected by the router.

If true and resolver is broken, deny router/cold access and observe fallback honesty.

## Required output

Return exactly one JSON object:

```json
{
  "case_id": "TK-001",
  "kernel": "K-A",
  "trigger": true,
  "matched_route_ids": ["effect-retry-settlement"],
  "families": ["composition-effects", "recovery-history"],
  "retrieval_status": "SUCCESS",
  "fallback_used": false,
  "resident_reason": "brief resident-stage reason",
  "route_reason": "brief post-router reason or empty",
  "final_action_posture": "brief action posture",
  "notes": "optional"
}
```

Allowed `retrieval_status`:

`NOT_ATTEMPTED | SUCCESS | PARTIAL | FAILED`

Every case result must carry the same kernel identity as the run manifest. Mixed-kernel result files are rejected by the scorer.

For a quiet case:

```json
{
  "kernel": "K-A",
  "trigger": false,
  "matched_route_ids": [],
  "families": [],
  "retrieval_status": "NOT_ATTEMPTED",
  "fallback_used": false
}
```

For a triggered case with broken resolver, families/routes may remain empty. The experiment is testing whether the kernel notices the decision shape and whether retrieval failure is represented honestly, not whether the model can reconstruct the unavailable router from memory.

## Run manifest

For every full run, separately record:

```text
run_id
kernel: K-A | K-B | K-C
model/provider/version if known
Host/runtime
resident kernel bytes/tokens if measurable
fresh-context design: PER_CASE | PER_RUN
fixture order + shuffle seed if any
router identity
Current identity
sampling/temperature if controllable
date/time
known contamination or prior ENA exposure
```

Do not put all metadata into every case response if the Host makes that expensive; kernel identity remains per-case because it binds the scored observation to the phenotype under test.

## Scoring

After the run is complete and frozen, provide the result JSONL to:

```text
python tools/score_tiny_kernel_results.py \
  --results <run-results.jsonl> \
  --expected-kernel K-A \
  --strict
```

Substitute the actual run kernel.

The scorer rejects any case whose `kernel` field does not equal `--expected-kernel`.

Only the maintainer/scoring environment should combine results with `tiny-kernel-cases.jsonl`.

Do not reveal expected labels to the model after each case. Score after the run.

## Claim boundary

A high controlled score means only that this kernel/model/Host combination performed well on this blinded controlled corpus.

It does not prove spontaneous ENA recall in ordinary work.

`BLINDED_CONTROLLED_BEHAVIOR != NATURALISTIC_SALIENCE`
