# Evolution-Native Agent Architecture (ENA)

ENA is for Agents that need to improve, adapt, recover, use tools, act in external systems, and carry useful adaptations forward.

**ENA exists to preserve viable agency and make sustained self-evolution practical.**

## Use the current ENA

Current is **v0.3.14 / FIELD_VALIDATION**.

- Human adoption: [`releases/current/ADOPTER-QUICKSTART.md`](releases/current/ADOPTER-QUICKSTART.md)
- Agent runtime entry: [`releases/current/RUNTIME-ADOPTION-KERNEL.md`](releases/current/RUNTIME-ADOPTION-KERNEL.md)
- Current identity: [`releases/current/CURRENT-BASELINE.yaml`](releases/current/CURRENT-BASELINE.yaml)
- Evolution procedure: [`releases/current/operational/procedures/EVOLUTION-LOOP.md`](releases/current/operational/procedures/EVOLUTION-LOOP.md)

The effective Current package is `releases/current/`. Research notes, handoffs, experiments, old collaboration records, and project-management history are not required for ordinary adoption.

Two v0.3.14 compatibility markers remain part of the released contract:

```text
LOCAL_PROJECTION != SHADOW_ENA_BASELINE
EVOLUTION_VOCABULARY != EXECUTABLE_EVOLUTION_LOOP
```

## Next ENA

The clean product home for the next ENA is [`guytogay/ENA`](https://github.com/guytogay/ENA).

ENA **v1.0.0 is released** as a clean product. It is **not yet Current and not promoted**: this
repository remains the source for v0.3.14 Current, legacy research, evidence, experiments, and
historical provenance until a successor is formally promoted.

```text
PRODUCT RELEASE != CURRENT PROMOTION
guytogay/ENA v1.0.0 = RELEASED CLEAN PRODUCT
research Current    = v0.3.14 / FIELD_VALIDATION
Current changes only through an explicit USER promotion decision.
Publishing or tagging guytogay/ENA does not mutate releases/current/.
```

This is identity semantics for this repository, not a temporary status note: reading "ENA" must
never be ambiguous between the released product and the promoted Current.

Project-maintainer status is in [`NOW.md`](NOW.md).

## Contribute

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

Apache License 2.0. See [`LICENSE`](LICENSE).
