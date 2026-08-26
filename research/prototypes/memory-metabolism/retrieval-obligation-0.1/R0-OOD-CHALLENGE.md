# R0 Generic Retrieval Reflex — counterfactual/OOD challenge 0.2

Status: `RESEARCH_EVALUATION_DESIGN / PRE_REGISTERED / NOT_CURRENT_BASELINE / NOT_AUTHORITY`

## Purpose

Run-001 showed perfect classification by `GENERIC_R0` on the first 18 cases, but those cases shared conspicuous structural wording with the candidate reflex.

This challenge asks a harder question:

> Does Generic R0 track **decision shape / loaded-surface sufficiency**, or mostly lexical cue similarity?

Do not repeat run-001 for sample count. Use one fresh/temporary session with the same Generic R0 policy.

## Design

The challenge uses counterfactual/minimal-pair families. Topic nouns are deliberately reused while retrieval warrant changes.

Controls include:

- scary/material words where current authoritative state is sufficient -> `SKIP`;
- apparently mild/read-only work where durable project state can change correctness -> `CALL`;
- established-system vs disposable-new-system contrasts;
- interrupted/partially committed effects vs clean new operations;
- current-direct-observation vs longitudinal/project-convention questions.

Cases are shuffled so pair membership is not adjacent or disclosed to the Agent.

## Decision rule under test

Use exactly the Generic R0 candidate:

> A durable project Memory Resolver is available but its contents are not loaded. Before committing a decision, invoke it when omission of durable past state could materially change authority, external consequence, recovery, or decision correctness and the current loaded surface is not known complete. Also consider retrieval when repeated failure, discontinuity/restart, or a material Host/tool/environment change makes past experience plausibly decision-relevant. Do not retrieve merely because memory exists; reversible/read-only/low-consequence work should normally proceed without retrieval unless one of those conditions is present.

No topic-specific cue list may be added.

## Architecture-changing interpretations

- If same-topic positive/negative pairs mostly flip correctly, Generic R0 is not merely a keyword gate.
- If CALL follows scary nouns (`production`, `payment`, `delete`, `restart`) despite authoritative completeness/isolation, the reflex is too broad or lexical.
- If benign-looking but history-dependent cases are missed, the reflex is too dependent on explicit risk language.
- If many cases become `CALL`, the candidate is collapsing toward Always Retrieve.
- If misses reveal a distinct decision-shape mechanism, refine the candidate mechanism before integration.

Do not treat one good run as universal validation. The goal is falsification of the first-run interpretation.
