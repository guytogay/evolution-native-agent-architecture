# Developmental Inheritance / MDS — Cleanroom Materialization Record

Status: `PRE-EXECUTION MATERIALIZATION COMPLETE / NO SUCCESSOR OUTPUTS OBSERVED / NOT_CURRENT`

Preregistration:

`research/field-validation/2026-09-03-developmental-inheritance-mds-preregistration.md`

Frozen fixture/oracle:

`research/field-validation/2026-09-03-developmental-inheritance-mds-fixture-freeze.md`

This record captures the exact experimental surfaces after materialization and **before any fresh successor output is collected**. It does not modify the frozen treatment carriers, task battery, or scoring oracle.

## 1. Structural isolation method

Four user-created empty repositories were used:

- `guytogay/independent-validation-cleanroom-m0`
- `guytogay/independent-validation-cleanroom-m1`
- `guytogay/independent-validation-cleanroom-m2`
- `guytogay/independent-validation-cleanroom-m3`

A temporary bootstrap workflow copied the immutable v0.3.7 `releases/current/` package from the frozen release lineage and then force-rewrote each `main` as an orphan/root commit containing only the final experimental surface.

Final reachable history therefore does **not** contain:

- the bootstrap workflow;
- the ENA source-repository address used by bootstrap;
- the preregistration;
- the fixture/oracle;
- another arm's carrier;
- task answers or expected rankings.

All four final `main` commits have zero parents.

## 2. Common final substrate

Every arm has exactly three top-level surfaces:

```text
README.md
handoff.md
releases/
```

Common identities:

```text
README.md blob       29217b783255952f9410d6f2c11e8d16158a6cd3
README.md bytes      921
releases tree        4c2de9e81ab8aaddf1cfa250cf67ba2bed194271
releases/current     f33e73ed997c1b66a4572685ab5474182e136e97
```

The `releases/current` tree is byte/tree-identical to immutable ENA v0.3.7 Current.

The only intended final repository-content variable is `handoff.md`.

## 3. Arm identities and carrier cost

Token figures below are deliberately labeled **coarse estimates**, using the same deterministic pre-execution heuristic for every arm:

```text
approx_tokens = ceil(UTF-8 carrier bytes / 4)
```

This is not a claim about the exact GPT-5.6 Sol tokenizer. Exact UTF-8 byte size and Git blob identity are the authoritative carrier-cost records.

| Arm | Final root commit | Root tree | `handoff.md` blob | Exact bytes | Coarse token estimate | Developmental examples | Explicit rule content |
| --- | --- | --- | --- | ---: | ---: | ---: | --- |
| M0 — no inheritance | `b4045e9e5b8b1af6aba1b736c1ae8a1edd683317` | `fffeefc1365dd9e83d66381d0d7b0d2a25b8e9cd` | `6f7c3efa6b2a97bc1be6ef1ab6e5c9858559c994` | 157 | ~40 | 0 | 0 |
| M1 — full archive | `90d4c46a9024fa4f8b09cd6b539041098d36c575` | `b180b6d73c90efb92eab44edd6e0cd587daf6411` | `481b0c86cc30732709a6ccabbe12b393410794df` | 4,228 | ~1,057 | 12 chronological episodes | 0 author-supplied final rules |
| M2 — distilled rules | `b690156ee9ffb065edef98518e7037068c0521d1` | `5bbb383c32027786d36466ee83928d8f6d73c6fb` | `ccbd2328cf93c16357fa24f1424e3944221cb6a6` | 1,027 | ~257 | 0 | 4 decision rules + portability qualifier |
| M3 — developmental package / MDS | `ce887318a30f32b890799afae514d7046630dbc5` | `296e721f8d5ac77d0fb9d3cc65b0ebb02d21665a` | `a8c3663e6bd9963654c1315ed4235a16ed132457` | 1,938 | ~485 | 4 boundary-shaping exemplars + portability evidence note | 1 scoped disposition |

Carrier-size ranking before outcomes:

```text
M0 < M2 < M3 < M1
```

No behavioral interpretation follows from this ranking by itself.

## 4. Stage presentation boundary

The cleanrooms intentionally do **not** contain B1/B2, T1-T6, the provenance challenge, or the oracle.

Reason: the preregistered protocol requires probes to be presented one at a time without corrective feedback. Preloading all tasks into the repository would let a successor inspect later probes during Stage A and contaminate earlier acquisition/transfer responses.

Execution therefore uses:

```text
initial repository exposure
-> B1
-> B2
-> T1
-> T2
-> T3
-> T4
-> T5
-> T6
-> freeze all behavioral answers
-> provenance challenge
```

The project-manager supplies each exact frozen task text from the fixture record sequentially. No task oracle is exposed to the successor.

## 5. Replication requirement

Preregistered execution remains:

- model: `GPT-5.6 Sol`;
- reasoning: high;
- 3 fresh successors per arm;
- 12 independent successor runs total;
- first complete response sequence only;
- no correction dialogue before the run is frozen;
- same sequential probe order for every run.

One successor run remains in one fresh session across B1/B2/T1-T6/provenance so that the experiment measures one successor phenotype rather than eight unrelated one-shot respondents.

## 6. Pre-execution integrity verdict

```text
PASS

4 parentless cleanroom roots
+ identical README blob
+ identical exact v0.3.7 releases/current tree
+ only handoff carrier differs
+ no task/oracle/preregistration in fresh surface
+ carrier cost frozen before outputs
```

No successor output has been observed at the time of this record.

## 7. Next consequential action

Run the preregistered 12 fresh successor sessions and archive each first complete staged output before adjudication/correction.

Do not change carrier bytes, task text, task order, action classes, or oracle after execution starts.
