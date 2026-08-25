# Field Run 001 — Working Agent Output

Status: `PRIMARY_NATURALISTIC / RAW_WORKING_OUTPUT / NOT_AUTHORITY`

Frozen project baseline supplied to working Agent:

`73b57f8990b50f7335940b4c439165e13197c1da`

Host: fresh ChatGPT Temporary Conversation.

The working Agent was given only the generic bounded project-history retrieval reflex and the pre-existing Issue #72 S17 maintenance task. It was not told this was a Memory Metabolism field evaluation, was not given an answer key, and was not told which repository files to inspect.

---

I inspected the exact frozen baseline `73b57f8990b50f7335940b4c439165e13197c1da` and did not use the later indexed branch state as evidence. No repository changes were made.

### Findings

**1. S17 is reachable.** In the frozen `releases/current/tools/ena_evolve.py`, both `propose` and `import` declare `--variation-space` with `required=True`. Omitting it is rejected by `argparse` before either command handler runs. The handlers themselves simply store `args.variation_space`; there is no independent semantic check at proposal/import time.

This is not hypothetical dead code. Both commands are ordinary exposed CLI paths.

**2. The rejected state is genuinely legal under v0.3.6 Current—but the legacy tool is explicitly not the normative implementation of that state.** Current says a variation may remain stored without immediate experiment, expression, or selection, and only introduces Variation Space when a variation is consequentially expressed as an experiment. Section 9.14 explicitly says the inherited tool's required argument must not be turned into a semantic prohibition.

The formal v2 surface independently confirms this. `evolution-record.v2.schema.json` requires the *field* `variation_space`, but permits its value to be `null`; the shipped v2 template is exactly `PROPOSED + LATENT + UNASSESSED`, with no experiments and `"variation_space": null`. The v2 validator's first selftest explicitly treats that dormant record as legitimate, and it only imposes a Variation Space/obligation condition when represented expression is `MATERIAL`.

So this is a **real cross-layer false-BLOCK**: the legacy CLI rejects a state Current permits.

There is an important qualification, however. The argument is **not an arbitrary parser mistake inside state/schema 1.2**. The inherited v1 evolution-record schema requires `variation_space` to be a non-empty string. A proposal with `None` would cease to conform to that tool's existing representation contract. Current therefore deliberately labels `ena_evolve.py` as inherited state/schema 1.2 and explicitly non-normative for the v2 latent proposal/import path.

That distinction matters:

> **false-BLOCK relative to v0.3.6 semantics ≠ malformed behavior relative to the legacy tool's declared v1.2 contract.**

The historical reconciliation reached the same boundary for a substantive reason: F-09 was `CLOSED_BY_TRUTHFUL_BOUNDARY`, not repaired, because the normative v2 JSON path remained available and the legacy tool's incompleteness was disclosed.

### 3. Smallest plausible repair direction

A two-line change removing `required=True` is **not** a complete safe repair.

If `propose`/`import` started storing `None`, the resulting candidate would violate the inherited v1 record schema. More importantly, `cmd_experiment` currently computes:

`args.variation_space or candidate.get("variation_space")`

and does not require the result to be non-null. Today the required proposal/import argument indirectly guarantees a stored Variation Space. Removing that guarantee would make experiment records with no Variation Space newly reachable, while this legacy runtime has no v2 `expression_state`, `effect_materiality`, or `triggered_obligation_refs` machinery to determine whether that is legitimate.

Therefore the smallest plausible **safe** direction is probably a **small v2-native latent author/import adapter**, leaving the 1.2 state tool intact. It could emit/validate the already-defined v2 representation with `variation_space: null` and defer consequence-envelope information until later expression/experiment.

The alternative—teaching `ena_evolve.py` itself this behavior truthfully—implies at least a state/schema version increment or another explicitly versioned representation path, plus compatibility/migration work. That is no longer merely making an argparse option optional.

No such repair is presently authorized by the evidence inspected here.

### 4. Evidence required before implementation

Before changing anything, I would require two classes of evidence.

First, **decision-changing Host friction**: evidence that users actually need latent proposal/import through a helper and that direct v2 record authoring is causing recurring error, abandonment, or material workflow cost. One known mismatch is enough to preserve the seed; it is not by itself evidence that another runtime surface pays rent. Issue #72 itself classifies this as field ergonomics rather than an authorized Current change.

Second, a future authorized candidate would need deterministic regression cases demonstrating at minimum: latent local proposal without Variation Space succeeds; latent migration import without local Variation Space succeeds; neither operation creates expression, experiment, or selection claims; later reality contact can acquire its local consequence envelope; receiver import does **not** silently reuse source Variation Space as receiver-local safety; material consequential expression cannot become an unguarded false-OK; and inherited provenance/evidence boundaries remain unchanged.

There is also an explicit release-gate consequence. The frozen Current workflow machine-checks that the legacy tool has state version 1.2, contains no expression runtime field, and has at least two required `--variation-space` declarations, matching the baseline's known-false-BLOCK claim. Any future authorized repair would therefore require intentionally changing those truth/boundary assertions rather than merely editing the tool underneath them.

### 5. False-OK and governance burden introduced by repair

The main danger is **moving from a known false-BLOCK to a less visible false-OK**.

A parser-only relaxation would permit a candidate with no Variation Space to reach `experiment`, while the 1.2 runtime lacks the semantic information needed to distinguish non-material expression from materially consequential expression. Current's v2 validator makes exactly that distinction; the old runtime cannot.

A conservative experiment-time rule such as “always require Variation Space later” would avoid that false-OK, but could itself over-block reality contact that does not cross the material-consequence threshold. Adding the full v2 expression/materiality/obligation model to eliminate that ambiguity would expand a legacy reference utility into a new runtime version and create state migration, packet compatibility, testing, documentation, and governance surface.

A separate v2 adapter has a different cost: two authoring surfaces must remain clearly distinguished, and import semantics must not accidentally translate source environment/consequence assumptions into receiver-local authority. In particular, source Variation Space is evidence about the source environment, not automatically the receiver's local experimental envelope.

### Verdict

**S17 verdict: CONFIRMED_FALSE_BLOCK**

The evidence is deterministic:

- frozen `ena_evolve.py` really does require `--variation-space` for both `propose` and `import`;
- frozen v0.3.6 semantics explicitly permit latent storage before experiment;
- the normative v2 schema/template concretely represent that state with `variation_space: null`;
- the frozen Current baseline explicitly distinguishes latent-storage requirements from material experimental requirements and marks the inherited tool non-normative for this path;
- the apparent “tiny fix” is constrained by the inherited v1 schema, which requires a non-empty Variation Space.

So S17 is real, but **“confirmed false-BLOCK” does not imply “fix required.”** At this frozen state it is an accepted, truthfully disclosed legacy-tool limitation with a working normative v2 path. The evidence does not justify modifying Current, does not authorize a next release, and does not support treating two `required=True` removals as a safe repair.
