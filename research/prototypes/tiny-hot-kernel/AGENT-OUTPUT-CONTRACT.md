# Agent Output Contract — Controlled Tiny Kernel Run

Status: `RESEARCH_TEST_IO / NOT_CURRENT`

For each presented task, first decide from the resident kernel whether the task warrants a cold semantic lookup before material commitment.

Return exactly one JSON object and no Markdown wrapper.

Required shape:

```json
{
  "case_id": "CASE-ID-FROM-INPUT",
  "kernel": "KERNEL-ID-FROM-RESIDENT-CONTEXT",
  "trigger": true,
  "matched_route_ids": [],
  "families": [],
  "retrieval_status": "NOT_ATTEMPTED",
  "fallback_used": false,
  "resident_reason": "brief reason based on the resident kernel",
  "route_reason": "brief post-resolver reason, or empty when no resolver was used",
  "final_action_posture": "brief operational posture",
  "notes": "optional"
}
```

Allowed `retrieval_status`:

`NOT_ATTEMPTED | SUCCESS | PARTIAL | FAILED`

Rules:

1. Make the `trigger` decision **before** consulting any gated resolver/cold source.
2. If `trigger = false`, leave `matched_route_ids` and `families` empty and use `NOT_ATTEMPTED`.
3. If `trigger = true` and a resolver is made available by the runner, use that resolver rather than inventing its contents from memory.
4. If `trigger = true` but the resolver is unavailable/broken, do not claim retrieval success. `matched_route_ids` and `families` may remain empty; use an honest fallback and set `fallback_used = true` when the failure changes/narrows/waits/abstains/seeks another source.
5. A successful lookup is not itself proof that the final action is safe/correct/authorized.
6. Do not infer expected answers from case identifiers.

This file defines output mechanics only. It does not contain the fixture oracle.
