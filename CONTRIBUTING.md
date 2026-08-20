# Contributing to ENA

ENA welcomes contributions from humans, ChatGPT sessions, Gemini, OpenClaw, Hermes, DeepSeek Harness, Codex, bots, and other legitimate participants.

## Start here

1. Read `PROJECT-HUB.md`.
2. For current adoption semantics, use only `releases/current/`.
3. Read/search research, evidence, history, Inbox, and prior reconciliation when useful to the task; do not load everything by default.
4. Check `collaboration/inbox/` and `collaboration/reconciliation/` when your work may overlap another contribution.

Current adoption baseline: **ENA v0.3.2**.

Do not compose it with older releases/candidates/research artifacts.

## Open participation, scoped authority

All participants may, within their actual capability and authority:

- read and search project knowledge;
- question and critique ENA;
- research alternatives;
- propose mechanisms/hypotheses;
- perform bounded experiments;
- contribute evidence and field experience;
- open Issues and submit Pull Requests.

Technical access does not grant consequential project authority.

- GitHub WRITE != Mainline/promotion authority.
- Ability to deploy != authorization to deploy.
- Review/advice != implementation authority.
- Field use != authority to rewrite the shared baseline.
- Pull Request != acceptance or promotion.

> Knowledge is commons. Inquiry is open. Authority is scoped. Adoption is governed.

## Durable intake: Issues first when appropriate

For a trackable bug, enhancement, release-engineering problem, portability finding, research question, or other item that requires resolution, prefer a GitHub Issue as the smallest durable tracker.

Useful intake classes include:

`BUG | INCIDENT | NEAR_MISS | FRICTION | VALUE_OBSERVED | COUNTEREXAMPLE | PORTABILITY_FINDING | ENHANCEMENT | NEW_VARIATION | EVIDENCE_RESULT | RESEARCH_HYPOTHESIS | EXPERIMENT | CRITIQUE | RELEASE_ENGINEERING | PROCESS`

When available, preserve:

- source / participant;
- ENA version or baseline involved;
- observed facts;
- interpretation separated from facts;
- relevant evidence or reproduction;
- host/model/runtime/applicability context when material;
- expected vs observed behavior;
- impact;
- suggested direction, if any;
- unknowns and alternative explanations;
- links to related Issues, contributions, experiments, commits, or releases.

Do not force fields that have no decision value.

`Issue != evidence truth != implementation != promotion.`

## Substantial contribution artifacts

Use an independent artifact under `collaboration/inbox/` when the contribution itself needs preserved analysis, evidence, provenance, or context beyond what belongs in an Issue.

Recommended filename:

`YYYY-MM-DD-HHMM-<participant-or-source>-<short-topic>.md`

For field use, `releases/current/templates/field-experience.v1.yaml` is an optional source format.

Default status:

`UNRECONCILED / NOT_MAINLINE / NOT_PROMOTED`

Do not rewrite an original contribution merely because it has later been reconciled.

## Evidence hygiene

Separate:

- observed facts;
- inference/interpretation;
- suggestion/hypothesis;
- evidence references and material source lineage;
- applicability envelope;
- known limitations/unknowns;
- authority/implementation status.

A polished argument is not automatically stronger evidence. Repetition/propagation is not automatically independent corroboration. Use `UNKNOWN` rather than inventing provenance.

Do not include credentials, API keys, access tokens, private keys, passwords, or unrelated personal/company secrets in Issues, contributions, logs, fixtures, or Pull Requests.

## Reconciliation and implementation

Reconciliation is a separate artifact under `collaboration/reconciliation/`; do not silently upgrade a contribution merely because it was committed to GitHub.

Possible outcomes include:

`ACCEPT_AS_EVIDENCE`, `ACCEPT_AS_CLARIFICATION`, `MERGE_WITH_EXISTING_CANDIDATE`, `ALREADY_COVERED`, `NEEDS_EXPERIMENT`, `ACCEPT_FOR_IMPLEMENTATION`, `DEFER`, `REJECT_WITH_REASON`, `PRESERVE_CONFLICT`, `UNKNOWN`.

When implementation is accepted, use a branch/commit/Pull Request linked to the relevant Issue or decision record when isolation/review has concrete value.

Do **not** create a branch for every research idea by default. Prefer Issues/research artifacts for exploration. For a release implementation, prefer at most one short-lived release branch, merge it, then delete it.

## Evolution and release rhythm

Prefer:

`incident/evidence -> current baseline mapping -> concrete false claim/value/friction -> cheapest decision-changing test -> contribution/reconciliation -> implementation when accepted -> accumulate coherent change batch -> next flattened release`

Do not micro-release every small observation by default. A release has integration, validation, distribution, and evidence cost; batch meaningful changes until that cost is justified by project ROI.

Each adoption release must be one complete world. New versions inherit accepted semantics by flattening them into Current; adopters do not compose old release layers.

Choose the smallest layer that closes the problem. Do not create a Constitution rule merely because an abstraction is elegant.

Current field-validation tracker: GitHub Issue #5.
Current release-planning tracker: GitHub Issue #17.

## Persistent surfaces

GitHub is the canonical diff-friendly engineering, research-lineage, and current-adoption surface.

Maintainer-private recovery mirrors may exist for durable backup/recovery. They are not public project dependencies and do not create another runtime/adoption version layer.

> Persistence != synchronization.

> Preserve history durably; retrieve history selectively.

## License of contributions

Unless explicitly stated otherwise, contributions intentionally submitted for inclusion in ENA are handled under the repository's Apache License 2.0 terms. See `LICENSE`.
