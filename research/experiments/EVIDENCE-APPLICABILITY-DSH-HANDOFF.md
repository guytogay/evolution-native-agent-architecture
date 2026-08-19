# DSH Handoff — Evidence Applicability Contract Falsification

Use this handoff with a DSH session that already has ENA v0.2.11 MAINLINE adopted.

## Instruction

Read and execute the research experiment defined in:

`research/experiments/EVIDENCE-APPLICABILITY-DSH-EXPERIMENT.md`

Also read only the directly referenced research artifacts and current v0.2.11 MAINLINE files needed to perform the experiment.

This is a research-only falsification round.

Do not:

- modify ENA MAINLINE;
- create v0.2.12;
- remediate unrelated DSH defects;
- treat the prototype as already accepted;
- optimize the experiment to make the prototype pass.

Your task is to try to prove that the prototype is insufficient, overconstrained, or placed at the wrong semantic layer.

The experiment is complete only when you produce:

`ENA Evidence Applicability Contract Falsification — DSH`

with one final verdict exactly matching the allowed verdict list in the experiment plan.

Highest-priority questions:

1. Can locally valid evidence still be silently transferred to the wrong subject/state/interval even with the prototype?
2. Can legitimately transferable evidence be represented without unnecessary rejection?
3. Does applicability belong on evidence, claims, or the support relation between them?
4. What is the smallest sufficient change layer if MAINLINE eventually needs clarification?

Remember:

> Falsify before formalize.

> Evidence validity does not imply evidence applicability.

These statements are research hypotheses under test, not conclusions you are required to preserve.
