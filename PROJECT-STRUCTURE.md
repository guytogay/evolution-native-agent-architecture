# ENA Project Structure

ENA keeps different truths in different places so that project coordination does not become the project.

## Live surfaces

| Need | Authoritative surface |
|---|---|
| What adopters should use now | `releases/current/` |
| Machine-readable Current identity | `releases/current/CURRENT-BASELINE.yaml` |
| What the project is doing now | `NOW.md` |
| Open questions / work / field contact | GitHub Issues |
| Change history | Git history / Pull Requests |
| Specific evidence or research detail | the relevant `research/` / `evidence/` artifact |

One fact should normally have one live home.

## Cold historical surfaces

The repository contains older project-management machinery such as:

- `PROJECT-HUB.md`;
- `PROJECT-METADATA.yaml`;
- `research/ACTIVE-RESEARCH.yaml`;
- `research/plans/`;
- `research/handoffs/`;
- branch inventories/governance records;
- reconciliation, freeze, validation, and release records.

These remain useful for archaeology, provenance, and exceptional high-consequence work. They are not mandatory takeover context and should not be kept synchronized with `NOW.md` by default.

## Branches

Use a branch when isolation or review has concrete value. Do not create a branch merely because a research thought exists.

A small research/documentation change can normally use one short-lived branch + Pull Request. A release may justify stronger isolation and exact identity checks.

`BRANCH_EXISTS != BRANCH_ACTIVE`

`RELEASE_BRANCH != CURRENT`

## Validation

Validation follows the surface that changed:

- `releases/current/**` -> Current semantic/regression/package checks;
- executable/Python logic -> relevant selftests/static/security checks;
- research/doc-only work outside Current -> normal diff/review, plus only tests that can actually change the decision.

Do not run release ceremony for ordinary prose.

## Session continuation

A new session should normally:

1. read `NOW.md`;
2. read the directly relevant Issue/file;
3. verify Current only if the next decision depends on Current identity;
4. start work when the goal, known state, uncertainty, and next consequential action are clear.

Retrieve old handoff/release/reconciliation material only when a concrete question requires it.

## Release boundary

Released Current remains a higher-consequence identity surface. Do not silently rewrite released bytes under the same version identity. This does not imply that every research note must inherit release governance.

> History can be deep while the live working surface stays small.
