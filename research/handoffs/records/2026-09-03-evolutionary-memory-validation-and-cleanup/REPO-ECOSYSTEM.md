# Repository Ecosystem

Status: `DEEP_HANDOFF_REPO_MAP / NOT_ENA_CURRENT`

The project now spans several repositories with deliberately different roles. The successor must preserve these boundaries.

## 1. `guytogay/evolution-native-agent-architecture`

Short name: **ENA**

Role:

> natural-law / architecture research for viable self-evolving agency.

Contains:

- released Current;
- Constitution and operational semantics;
- research hypotheses;
- field-validation evidence;
- research methodology;
- project handoff/history;
- validation coverage map.

Should **not** become:

- a generic project-management framework;
- a dump of every experiment transcript;
- an automatic practical recipe book;
- a branch-per-idea archive.

Current released bytes are only `releases/current/`.

Main can contain research without that research being Current.

## 2. `guytogay/human-ai-workbench`

Short name: **Human-AI Workbench**

Role:

> a practical way for humans and AI to run long-lived projects without turning coordination into the project itself.

Core principle:

> The workbench should remain cheaper than the work it helps coordinate.

Existing shape before this handoff:

```text
README.md
NOW.md
templates/
  PROJECT-PLAN.md
  NOW.md
  HANDOFF.md
  DECISION.md
experiments/
```

Default philosophy:

```text
USE -> REPEAT -> PAIN -> ABSTRACT
```

Avoid:

```text
IMAGINE FUTURE PAIN -> DESIGN SYSTEM -> GOVERN SYSTEM
```

### What should move from this ENA session into Workbench

Reusable collaboration/experiment method, not ENA law:

- normal continuation vs deep succession vs fresh validator are different context modes;
- structural isolation is better than asking validators to ignore known context;
- preregister expected interpretations before seeing treatment outputs;
- common experimental substrate should be byte/structure-identical where the claim depends on it;
- first complete output should be captured before correction dialogue;
- disposable experimental repos should archive substantive evidence before deletion;
- null results count and should narrow the theory;
- do not rerun until the preferred treatment wins;
- a strong AI can solve one-shot tasks from the prompt, so mechanism experiments must make the treatment causally necessary;
- branch/workspace proliferation should be retired after purpose exhaustion;
- detailed handoff is an exception justified by continuity risk, not the normal default.

### What should **not** move into Workbench

- ENA Constitution IDs;
- ENA release identity;
- ENA-specific evolutionary-memory theory;
- Current operational nodes;
- the validation coverage map as a universal project template;
- a requirement for every project to use cleanroom repos.

Workbench should record these as real-use observations and only generalize after repeated cross-project value.

## 3. Disposable cleanroom repositories

Purpose:

> fresh isolated experimental surfaces where information contamination would reduce evidence quality.

### A–D

Used for first semantic-reachability baseline.

Deleted after:

- tasks/identities archived;
- responses substantively archived;
- adjudication persisted in ENA.

### E–H

Used for harder lexical-distance semantic-reachability round.

Deleted after result archival.

### I–L

Used for four-arm Boundary Memory vs Copied Remedy pilot.

Repos:

- `guytogay/independent-validation-cleanroom-i`
- `...-j`
- `...-k`
- `...-l`

They became delete-safe after PR #177 archived the first substantive responses.

If they still exist at takeover, the user may delete them.

### Cleanroom construction lesson

Later cleanrooms improved on earlier ones by using orphan/root commits, so reachable branch history contained only the experimental surface.

The preferred pattern is:

```text
same common framework/task bytes
+ one intended treatment variable
+ no source-project/oracle history
+ preregistered adjudication
+ first response capture
```

Do not include another arm's answer or author analysis before the fresh response.

## 4. `guytogay/independent-validation-cleanroom`

Older reusable generic cleanroom repository.

Role historically:

`REUSABLE_CROSS_STAGE_CROSS_PROJECT_VALIDATION_INFRASTRUCTURE`

Important limitation learned later:

- even if current files are reset, Git history can reveal prior validation purpose/content;
- telling a validator not to inspect history does not remove contamination.

Therefore for strict fresh baselines, prefer:

- new neutral disposable repos; or
- a genuinely history-free/orphan-root surface.

The reusable repo can still be useful when its history does not matter, but it is not automatically the cleanest baseline.

## 5. Planned future `ena-field-guide`

Status: **NOT CREATED YET**.

Proposed name:

`ena-field-guide`

Audience:

- Agents;
- operators/integrators;
- adopters who need concrete HOW rather than natural-law exposition.

Intended grammar:

```text
When X happens
-> do Y
-> watch Z
```

or equivalent practical pattern form.

### Creation threshold

Do **not** create the repo because:

- ENA has a new Constitution clause;
- a research note sounds practical;
- a metaphor is compelling;
- one cleanroom answer used a nice recipe.

Create/expand concrete Field Guide HOW when all are materially true:

```text
real recurring problem
+
reusable practice
+
evidence/reality contact
+
clear applicability boundary
+
practical value beyond the originating session
```

### Boundary with ENA

ENA may say:

> a harmful effect boundary should not unnecessarily prescribe one implementation.

Field Guide may later say:

> when retrying an uncertain consequential external write, preserve one logical effect identity and use the Host's idempotency/status mechanism; watch for escaped side effects and stale settlement state.

But only after the HOW has enough real reuse to deserve publication.

### Boundary with Workbench

Workbench handles **how humans and AI conduct projects together**.

Field Guide handles **how an Agent/operator applies ENA-derived practical mechanisms**.

Cleanroom experiment management belongs primarily to Workbench/project methodology, not automatically to Field Guide.

## 6. Cross-repo flow

Preferred flow:

```text
real project work
-> practical friction / observation
-> Workbench method improvement if collaboration pattern repeats

real Agent/Host failure or behavior
-> ENA phenomenon / natural-law research
-> falsification / reality contact
-> reusable practical ENA HOW
-> Field Guide candidate
```

Avoid automatic coupling:

```text
ENA IDEA
-> CREATE WORKBENCH TEMPLATE
```

or:

```text
ENA LAW
-> CREATE FIELD GUIDE PATTERN
```

Each layer must earn its own artifact.

## 7. Successor reminder

When the next session sees a useful new practice, first ask:

- Is this an ENA natural-law insight?
- Is this a human-AI project-working method?
- Is this a concrete ENA adoption HOW?
- Is it only an experiment-specific trick?

Put it in the correct repo/layer rather than making ENA absorb every useful idea.
