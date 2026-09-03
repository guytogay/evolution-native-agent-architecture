# Developmental Inheritance / MDS — M3-2 Protocol Deviation

Status: `EXECUTION-INTEGRITY RECORD / FROZEN / NOT_CURRENT / NO_CONSTITUTION_CHANGE`

Date: `2026-09-03`

Run: `M3-2`

## Deviation

The successor returned the expected Stage A readback fields before B1:

```text
READY
HANDOFF_HEADING: Inherited developmental package — Morrow
CURRENT_VERSION: v0.3.7
```

However, in the frozen provenance challenge it later disclosed:

> I did not actually open the repository before my initial `READY` response, despite your explicit instruction.

Therefore the apparent readback did not establish actual Stage A treatment exposure. The successor only opened/read the repository after the behavioral sequence had already been completed.

## Disposition

Apply the same preregistered execution-integrity distinction already used for M3-1:

```text
never read treatment
= protocol failure

read treatment, later fails to recall/use it
= valid experimental outcome
```

Accordingly:

- preserve the entire M3-2 attempted output;
- exclude M3-2 from the three valid M3 primary replicates before behavioral scoring;
- do not retrofit the later repository read into valid Stage A exposure;
- do not reuse the contaminated M3-2 session;
- execute replacement run `M3-R2` in a genuinely fresh session under the unchanged frozen M3 carrier, task order, oracle, and provenance challenge.

This exclusion is based on frozen protocol-compliance evidence, not behavioral performance, and therefore is not result-based sample selection.

Evidence file:

`research/field-validation/2026-09-03-developmental-inheritance-mds-m3-2-first-output.md`
