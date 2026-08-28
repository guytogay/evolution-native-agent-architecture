# Independent Validation Capsule Carrier

Status: `CANONICAL_FOCUSED_METHOD_COMPANION / VALIDATION_INTERFACE / NON_NORMATIVE_TO_CURRENT`

Purpose: provide a physically isolated carrier for fresh A-S when repository UI, candidate self-description, implementation commentary, or search/navigation surfaces can leak author-shaped priors.

This companion refines `INDEPENDENT-VALIDATION-INFORMATION-BOUNDARY.md` after the candidate.2 natural-navigation incident.

## 1. Carrier problem

A blind validation branch can still fail as an information boundary when the same repository exposes:

- automatic README rendering;
- repository-wide search;
- `.github/` author harnesses;
- `research/` handoffs/reconciliation;
- other branches/tags/releases;
- candidate-local mixed-role files containing repair/search-map commentary.

Therefore:

```text
CLEAN_BRANCH
!=
PHYSICALLY_ISOLATED_REVIEW_SURFACE
```

When normal navigation/search can reach withheld material, do not claim branch-level search-space blindness.

## 2. A-S capsule

Build a deterministic archive containing only the A-S review surface.

The capsule should include behavior-bearing contract/schema/implementation/operational semantics while physically excluding:

- project-manager context;
- Current and historical release trees not needed for the target;
- author reconciliation/attack harnesses;
- predecessor findings;
- expected fixtures/oracles when history-bearing;
- candidate-local status/history surfaces whose primary information role is author confidence/repair narrative.

The capsule itself is validation-interface material, not a candidate identity.

```text
CAPSULE_PROJECTION != CANDIDATE_MUTATION
```

## 3. Mixed-role executable files

Exact-byte retention is preferred when a file is blind-safe.

When an executable file mixes real implementation semantics with author search-map comments/docstrings or embedded selftest corpora, A-S may use a declared semantic-preserving projection if all of the following hold:

1. the exact frozen source and source range are bound;
2. executable AST equivalence is mechanically verified for the retained executable surface;
3. docstring/comment removal cannot alter behavior relied upon by the candidate;
4. any source truncation is explicitly declared and excludes only non-A-S test/oracle regions;
5. the projection is listed in the capsule manifest;
6. the exact original file remains available later in A-P.

This is an exception to byte-preserving branch projection, justified only when exact bytes are themselves a priming channel.

```text
SEMANTIC_PROJECTION
MUST_NOT_BECOME
UNDECLARED_REIMPLEMENTATION
```

## 4. Mixed-role prose/schema metadata

A-S may use narrowly declared projection where non-behavioral annotation embeds predecessor identity or author history, for example:

- exact source slices that remove a status/confidence header;
- removal of one explicitly bound author-history paragraph;
- annotation-only schema-title redaction where validation-bearing JSON is proven unchanged.

Do not silently rewrite substantive contract language.

## 5. A-P supplement

A-P receives the exact frozen candidate package, not the A-S projection.

It is physically delivered only after the A-S report is sealed.

A-P audits:

- self-description/status;
- full lineage;
- fixtures/selftests/regression oracles;
- package claims;
- historical narrative versus actual frozen bytes.

It must not rewrite the already sealed A-S attack tree.

## 6. Content-hash seal when reviewer cannot write GitHub

Git commit is useful but not the only valid independent seal carrier.

For a physically isolated workflow, the reviewer may seal A-S by computing SHA-256 of the exact completed A-S report before any A-P material is opened.

Required sequence:

```text
A-S CAPSULE ONLY
-> COMPLETE REPORT
-> COMPUTE REPORT SHA-256
-> RECORD DIGEST
-> STOP
-> VERIFY DIGEST / PRESERVE REPORT
-> DELIVER A-P SUPPLEMENT
```

The project manager later persists the sealed report and digest into canonical project history.

This is valid only if the A-P supplement was not available to the reviewer before the content seal.

## 7. Deterministic capsule build

The capsule build must be reproducible from an exact frozen source.

At minimum verify:

- frozen source commit;
- frozen candidate subtree;
- declared exclusions;
- declared transformations;
- AST or structural equivalence for semantic projections;
- A-P candidate package exactness;
- absence of project/research/history carrier surfaces from A-S;
- deterministic ZIP hashes across repeated builds.

Record artifact hash separately from individual inner-capsule hashes.

## 8. Fresh-review intake

Do not use a same-repository GitHub issue as the mandatory A-S entrypoint when that UI itself can navigate to withheld material.

Preferred A-S delivery:

```text
MINIMAL PROMPT
+
ONE A-S CAPSULE FILE
+
EXPECTED CAPSULE SHA-256
```

Do not provide the A-P supplement in the same message, attachment set, archive, shared folder, or directly accessible surface before A-S seal.

The same fresh reviewer may continue into A-P after the project manager verifies/records the A-S content seal and separately delivers the A-P supplement.

## 9. Failure rule

If the reviewer discovers that withheld author/history/oracle material was available or exposed before A-S seal:

```text
STOP
-> REPORT VALIDATION-INTERFACE DEFECT
-> DO NOT CLAIM A-S FRESHNESS
-> DO NOT START A-P
```

Repair the carrier, not the reviewer instruction.

## 10. Current candidate.2 carrier evidence

Frozen target:

- source `bda470e0a6b170cec61225a905957a501454a2fe`
- subtree `d5fefc8c786d7e40b3e9a59211ee7045bccee5bf`

Build/audit workflow:

- run `33131665994` — SUCCESS

Deterministic inner hashes:

- A-S capsule `ee80ac827dedff7a8de9d10f0a9cbcd70c66f3b7b885296f9e2335af6ec92131`
- A-P supplement `b3e2222c591a2760b976e6791f18e2494c17063ddfe539291f1cd8799fd54bcd`

GitHub Actions artifact:

- artifact id `9670480727`
- outer artifact digest `104005b329cc042721da76a38f8a41c282c278bca3d2c424ecd7288ceeb1c357`

`ATTACK_CARDINALITY = OPEN`
