# Contributing to ENA

ENA welcomes critique, experiments, field evidence, practical implementations, semantic proposals, and code from humans and AI systems.

## Start here

- For ENA's current adoption semantics, use only `releases/current/`.
- For current project/research work, read `NOW.md`.
- For a specific contribution, read only the Issue/files needed to understand that contribution.

Do not load project history, handoff archives, old release records, or reconciliation directories by default.

## Smallest useful contribution path

Use the smallest surface that preserves the truth you need:

- **Question / bug / friction / counterexample / research idea** -> open or update an Issue.
- **Small text/code change** -> normal branch + Pull Request when isolation/review helps.
- **Field observation** -> Issue or focused evidence artifact if the observation needs durable structure/provenance.
- **Release-changing work** -> use the stronger release validation appropriate to changing `releases/current/`.

A normal contribution does **not** require a candidate freeze, handoff package, reconciliation artifact, release readback, or promotion ceremony unless the contribution actually crosses one of those boundaries.

## Evidence hygiene

When a claim matters, keep these distinctions visible:

- observation vs interpretation;
- claim vs evidence vs applicability;
- local success vs transferable/general success;
- known vs unknown;
- proposed change vs accepted Current semantics.

Prefer a concrete failure, trace, reproduction, or bounded observation over confidence language.

Do not include credentials, API keys, access tokens, private keys, passwords, or unrelated personal/company secrets.

## Research and semantic proposals

ENA is allowed to explore abstract natural-law candidates. A new phrase or elegant abstraction does not automatically deserve a new Constitution invariant.

Useful sequence:

`observation / tension -> candidate distinction -> reality/falsifier -> reuse or clarify existing semantics -> add a new invariant only if a real semantic gap remains`

Practical HOWs may stay Host-specific. Do not universalize an implementation merely because it worked once.

## Code and executable logic

Executable logic should keep executable tests.

- Run the relevant selftests for the code you changed.
- Changes under `releases/current/**` receive the Current validation/regression/package checks.
- Python/security-sensitive changes receive the relevant static/security checks.
- Doc/research-only changes outside Current should not trigger release-style work merely because prose changed.

## Authority

Technical access and contribution do not create unrelated authority.

`Contribution != Acceptance != Release/Promotion Authority`

A Pull Request can be useful even when its proposal remains research-only, Host-specific, partially adopted, or rejected with evidence.

## History and status

Use Git history for history, GitHub Issues for open work, CI for machine-known execution facts, and `NOW.md` for the small amount of live project state needed to continue work.

Avoid copying the same live state into multiple files.

## License

Unless explicitly stated otherwise, contributions intentionally submitted for inclusion in ENA are handled under the repository's Apache License 2.0 terms. See `LICENSE`.
