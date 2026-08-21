# Security Policy

## Scope

ENA is an experimental agent-governance architecture and research repository. Security-relevant reports are welcome, including issues in machine-contract validators, evidence/authority boundaries, recovery semantics, CI workflows, release packaging, or repository automation.

The current adoption baseline is under `releases/current/`. Research candidates and prototypes under `research/` are not Mainline or production enforcement unless explicitly stated otherwise.

## Reporting a vulnerability

Please avoid publishing exploit details, credentials, secrets, or other sensitive material in a public Issue or Pull Request.

If GitHub **Private vulnerability reporting** is enabled for this repository, use the repository's **Security → Report a vulnerability** flow.

If private vulnerability reporting is not available, open a minimal public Issue titled **Security contact requested** without exploit details, secrets, or sensitive reproduction data. A maintainer can then arrange an appropriate private channel.

For non-sensitive correctness bugs, false-confidence cases, counterexamples, or research findings, use the normal Issue / contribution workflow described in `CONTRIBUTING.md`.

## What to include

When safe to do so, include:

- affected commit / release / candidate ref;
- affected file or contract surface;
- expected vs actual behavior;
- minimal reproduction steps;
- consequence or false-confidence surface;
- whether the issue affects `releases/current/`, a research candidate, or both;
- any known workaround or containment.

Please distinguish reproducibility from semantic correctness. A validator or fixture replay matching its expected output does not by itself establish that the expectation is correct.

## Disclosure and remediation

Security reports are treated as evidence, not automatic authority to modify or promote ENA. Maintainers will evaluate scope, reproduce the issue where practical, and preserve relevant provenance. Remediation, reconciliation, release, and promotion remain separate decisions.

Do not include real credentials or production secrets in test fixtures. Use synthetic values.
